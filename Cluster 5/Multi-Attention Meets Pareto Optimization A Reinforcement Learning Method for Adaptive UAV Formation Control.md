# Multi-Attention Meets Pareto Optimization A Reinforcement Learning Method for Adaptive UAV Formation Control.pdf

## Page 1

Academic Editor: Xiwang Dong
Received: 4 September 2025
Revised: 27 October 2025
Accepted: 3 November 2025
Published: 8 December 2025
Citation: Zheng, L.; Zeng, J.; Qin, L.;
Ju, R. Multi-Attention Meets Pareto
Optimization: A Reinforcement
Learning Method for Adaptive UAV
Formation Control. Drones 2025, 9, 845.
https://doi.org/10.3390/
drones9120845
Copyright: © 2025 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license
(https://creativecommons.org/
licenses/by/4.0/).
Article
Multi-Attention Meets Pareto Optimization: A Reinforcement
Learning Method for Adaptive UAV Formation Control
Li Zheng †, Junjie Zeng †, Long Qin and Rusheng Ju *
College of Systems Engineering, National University of Defense Technology (NUDT), Changsha 410073, China;
zhengli19@nudt.edu.cn (L.Z.); zengjunjie@nudt.edu.cn (J.Z.); qinlong@nudt.edu.cn (L.Q.)
* Correspondence: jurusheng@nudt.edu.cn
† These authors contributed equally to this work.
Highlights
What are the main findings?
• We propose a CTDE MARL framework that couples three lightweight attention branches
(self, inter-agent, and entity) with a Pareto archive to learn interpretable vector-reward
policies without fragile weight tuning.
• In urban-like 3D simulations under partial observability, the framework improves team
success by 13–27 percentage points for N = 2–5, while reducing collisions, maintaining
tighter formations, and lowering control effort.
What is the implication of the main finding?
• The method acts as a plug-in for common MARL backbones (instantiated on MADDPG
here) and scales to larger teams with stable training and smoother trade-offs.
• It offers a practical path to jointly optimize safety and efficiency for real multi-UAV
deployments without repeated reward re-weighting.
Abstract
Autonomous multi-UAV formation control in cluttered urban environments remains chal-
lenging due to partial observability, dense and dynamic obstacles, and conflicting objectives
(task efficiency, energy use, and safety). Yet many MARL-based approaches still collapse
vector-valued objectives into a single hand-tuned reward and lack selective information
fusion, leading to brittle trade-offs and poor scalability in urban clutter. We introduce
a model-agnostic MARL framework—instantiated on MADDPG for concreteness—that
augments a CTDE backbone with three lightweight attention modules (self, inter-agent, and
entity) for selective information fusion, and a Pareto optimization module that maintains a
compact archive of non-dominated policies to adaptively guide objective trade-offs using
simple, interpretable rewards rather than fragile weightings. On city-scale navigation tasks,
the approach improves final team success by 13–27 percentage points for N = 2–5 while si-
multaneously reducing collisions, tightening formation, and lowering control effort. These
gains require no algorithm-specific tuning and hold consistently across the tested team
sizes (N = 2–5), underscoring a stronger safety–efficiency trade-off and robust applicability
in cluttered, partially observable settings.
Keywords: attention mechanisms; Pareto optimization; multi-agent reinforcement learning;
UAV formation control
Drones 2025, 9, 845
https://doi.org/10.3390/drones9120845

## Page 2

Drones 2025, 9, 845
2 of 34
1. Introduction
With the rapid integration of unmanned aerial vehicles (UAVs) into real-world op-
erations, their roles have expanded from agriculture and logistics to time-critical disaster
response and persistent environmental monitoring. In particular, urban and built-up
environments—characterized by dense buildings, occlusions, and narrow corridors—are
becoming key application theaters for UAV swarms, e.g., communication relaying in “urban
canyons,” cooperative searching among high-rises, and safe navigation through cluttered
streets and courtyards [1–3], while multi-UAV formation can substantially enhance area
coverage and resilience, achieving stable, adaptive, and collision-free coordination in these
city-like scenarios remains challenging.
As the team size grows, multi-UAV control faces intertwined difficulties in percep-
tion, decision-making, and real-time execution. Concretely, we highlight three practi-
cal challenges. (1) Selective information use under partial observability. Each UAV
must filter high-dimensional, multi-source inputs (self state, neighbors, and environment
entities) to extract salient cues for timely decisions; without targeted filtering, decision
latency, and credit assignment deteriorate. Traditional rule-based and control-theoretic
schemes—e.g., leader–follower and virtual structure/potential field designs [4,5], model
predictive control (MPC) [6,7], and consensus/distributed optimization [8,9]—offer clarity
and guarantees but are sensitive to modeling errors, communication delay, and dynamic
clutter typical of urban scenes. (2) Multi-objective trade-offs. Formation keeping, obstacle
avoidance, task efficiency, and energy economy often conflict; scalarizing them with fixed
linear weights masks Pareto structure and yields brittle policies when mission priorities
shift. (3) Scalability and robustness. In practice, packet loss, sensor noise, and non-
stationarity degrade performance; vanilla deep MARL methods (e.g., MADDPG-style
CTDE) improve coordination [10–12] yet still lack explicit mechanisms for dynamic infor-
mation selection and principled multi-objective optimization, causing sharp performance
drops as agent count or scene complexity increases [13].
To address these challenges, we present a reinforcement learning method that aug-
ments a Centralized Training with Decentralized Execution (CTDE) backbone with multi-
source attention and a Pareto optimization module. Specifically, we equip decentralized
actors with three lightweight attention branches—self attention for intra-state feature selec-
tion, inter-agent attention for targeted neighbor reasoning, and entity attention for salient
environment perception—whose outputs are concatenated into an attention-enhanced
representation. In training, a vector-valued reward models task progress, energy, formation
coherence, and safety; a Pareto module maintains a compact archive of non-dominated so-
lutions and provides adaptive weights for updates, avoiding heavy manual reward tuning
while preserving simple, interpretable shaping terms for each objective. In a representative
3D urban-like environment, the proposed modules consistently improve team success,
safety, and formation quality across 2–5 UAVs with comparable or lower control effort;
detailed results are reported in Section 6.
Compared with prior MARL approaches for UAV formation, our contributions are
twofold: (i) a typed, single-hop multi-source attention front-end (self/inter-agent/entity)
that acts as a lightweight selector rather than a deep message-passing encoder, thus pre-
serving real-time feasibility with O(K+M) per-agent per-step compute; and (ii) a Pareto
module trained with vector-valued critics that replaces fragile hand-tuned scalarization,
exposing robust trade-offs among task progress, safety, formation coherence, and energy.
This pairing yields large gains in cluttered, partially observable urban settings and is
plug-and-play for CTDE backbones.

## Page 3

Drones 2025, 9, 845
3 of 34
The main contributions are summarized as follows:
1.
We develop a multi-source attention design (self/inter-agent/entity) for decentralized
actors that selectively fuses critical cues from self, teammates, and urban environment
entities, improving coordination efficiency and robustness under partial observability.
2.
We introduce a Pareto optimization module for vector rewards that approximates
the Pareto front during training, enabling adaptive trade-offs across task efficiency,
formation coherence, energy, and safety with only simple, objective-wise shaping
terms—not heavy ad hoc manual weighting.
3.
We integrate the above as architecture-agnostic, plug-and-play modules for CTDE-
style MARL and validate them in 3D city-like scenes. Across teams of N = 2–5
UAVs, inserting our modules into representative MARL backbones increases final
team success by about +12–+27 percentage points and reduces collisions by roughly
20–30%, with tighter formation tracking at comparable or lower control effort; the
gains persist for N = 2−5, indicating effectiveness across the tested sizes; runtime
scaling is analyzed in Section 6.9.
Beyond the above challenges, two complementary research lines are noteworthy but
orthogonal to our focus: (i) real-time communication protocols with blockchain-secured
identity and auditability for mission-level coordination, and (ii) AI-driven swarm intelli-
gence/control frameworks that target higher-level autonomy and decision-making. Recent
studies report progress on both fronts [14,15]; we therefore position our contribution at
the low-latency control layer and later discuss how these directions can be combined with
our method.
Terminology in article are follows: Unmanned Aerial Vehicle (UAV); Multi-agent rein-
forcement learning (MARL); Centralized Training with Decentralized Execution (CTDE);
multi-objective optimization (MOO); Root Mean Square Error (RMSE); Multi-Agent
Deep Deterministic Policy Gradient (MADDPG) [16]; (Independent) Deep Q-Network
(IDQN) [17].
The remainder of this paper is organized as follows: Section 2 reviews related work.
Section 3 summarizes background knowledge. Section 4 formulates the problem and CTDE
realization. Section 5 presents our method (attention branches and Pareto optimization).
Section 6 describes experiments, ablations, and robustness. Section 7 concludes.
2. Related Work
2.1. Current Research on Multi-UAV Formation Control
Practical deployments are increasingly moving to urban/built-up scenes with dense
buildings, occlusions, and narrow corridors, where multi-UAV formations support commu-
nication relaying, cooperative search, and safe navigation between high-rises. Rule-based
and classical control schemes—such as leader–follower and virtual structure/potential
field designs—remain popular for their clarity and ease of deployment [4,5]. Optimization-
theoretic approaches, including model predictive control (MPC) and consensus/distributed
control, offer stronger constraint handling and stability guarantees [6,7,9,18]. Deep re-
inforcement learning (DRL) has recently shown promise in handling high-dimensional
observations and partial observability, and has been explored for formation, trajectory
design, and cooperative navigation [11,19,20].
However, when mapped to city-like environments, these lines face three recurring
challenges that align with our problem setting. (i) Selective information use under partial
observability: controllers must extract salient cues from self, neighbors, and environmental
entities in high-dimensional, cluttered scenes; fixed-rule filters or hand-crafted interfaces
struggle as complexity grows. (ii) Multi-objective trade-offs: formation coherence, obstacle

## Page 4

Drones 2025, 9, 845
4 of 34
avoidance/safety, task efficiency, and energy economy often conflict; scalarizing them with
fixed linear weights blurs Pareto structure and leads to brittle behavior when mission prior-
ities shift. (iii) Scalability and robustness: communication delays, packet loss, and sensor
noise degrade coordination, and performance tends to drop sharply as agent count or
urban clutter increases [11]. Within optimization/control methods, even with disturbance
observers and estimation filters (e.g., Kalman-consensus and disturbance observers in
MPC pipelines [7]), the burden of online optimization and model mismatch in cluttered 3D
geometry limits agility. In DRL pipelines, the absence of explicit mechanisms for dynamic
information selection and principled multi-objective optimization remains a key gap.
2.2. Attention Mechanisms for Collaborative Perception and Decision Making
Attention has been introduced to enhance multi-agent perception/communication and
to focus computation on salient cues in cooperative UAV tasks. For trajectory design and re-
source assignment, graph attention has improved performance by letting agents emphasize
critical neighbors and links [21]. For cooperative encirclement/rounding, multi-head soft
attention yields targeted coordination signals [22]. Transformer-style designs with virtual
objects have been used for short-range air combat maneuver decision, showing improved
decision quality via structured attention to key entities [23]. In adversarial/dangerous
settings such as missile avoidance, multi-head attention helps capture dynamic obstacles
and threat saliencies [24].
These studies collectively indicate that multi-source attention (self/neighbor/entity)
can improve collaborative perception and decision quality. At the same time, prior work
typically optimizes a single scalarized return and does not explicitly couple attention
with multi-objective value estimation; as a result, policies may overfit to a particular
weight setting and generalize poorly when objective priorities change (e.g., switching from
aggressive goal-seeking to safety-first in narrow corridors). Our method targets this gap by
pairing lightweight attention branches with vector-valued critics and Pareto-aware training.
2.3. Advances in Multi-Objective Optimization (MOO) and Pareto Methods
Pareto-based multi-objective optimization (MOO) offers a principled way to expose
trade-offs among conflicting objectives without collapsing them into a single weighted
sum. In UAV-related literature, NSGA-III and variants have been applied to task alloca-
tion and planning under complex constraints [25,26]; MOEA/D with adaptive weights
has improved solution-set uniformity and has been used for 3D path planning [27]; and
dynamic multi-objective resource allocation has been investigated in related communi-
cation/energy settings [28,29]. These techniques are effective at offline design and static
instances, but their computational footprint and lack of tight coupling with the perception–
decision pipeline make end-to-end, online deployment in cluttered, partially observable
environments difficult.
Accordingly, there is a need to integrate Pareto reasoning into learning-based coor-
dination rather than treating MOO as an external, offline post-processor. Our approach
follows this direction: we retain simple, objective-wise shaping signals (task progress,
energy, formation coherence, safety) and train vector-valued critics, while a compact Pareto
archive provides adaptive training weights to encourage non-dominated policy updates
within the MARL loop.
2.4. Real-Time Communication and Secure Coordination (Blockchain-Enabled)
For multi-UAV missions, real-time communication must handle authentication, in-
tegrity, and auditability in dynamic, partially connected networks. Blockchain-enabled
protocols (DLT) offer tamper-evident logging, distributed identity, and mission-level con-
sensus which can benefit task handover, fault forensics, and high-level coordination under

## Page 5

Drones 2025, 9, 845
5 of 34
untrusted infrastructure [14]. However, classical BFT-style consensus and ledger replica-
tion introduce non-trivial latency and bandwidth overhead, making them better suited to
event-level control (e.g., role assignment, re-keying, and mission re-planning) rather than
per-timestep control loops. Our method is complementary: the attention/Pareto modules
operate at the low-latency control layer, while DLT-based services can provide authenti-
cated messaging and mission governance above, e.g., using attention-derived priorities to
throttle which links or events merit notarization.
2.5. AI-Driven Swarm Intelligence and AI-Based Control
Beyond MARL, a broad body of AI-driven swarm intelligence and AI-based control
explores biologically inspired coordination, learning-enhanced MPC, and hierarchical
decision stacks to improve autonomy, adaptability, and distributed decision making [15].
These approaches often target high-level behaviors (task allocation, formation switching,
and role negotiation) and complement low-level collision avoidance and formation tracking.
Our Pareto-attentive CTDE design can be integrated as the reactive layer within such stacks,
while swarm-level planners provide goal assignments or safety budgets; conversely, vector-
valued critics can supply interpretable objective signals to higher layers when mission
priorities shift.
2.6. Summary and Gaps
In summary, (i) classical rule/optimization controllers are strong when models and
communication are reliable but struggle to select salient information and adapt in cluttered
urban scenes; (ii) DRL scales to high-dimensional observations yet often relies on ad hoc
scalarization, lacking a principled mechanism to balance competing goals; and (iii) existing
attention applications improve perception/coordination but are typically optimized for a
single weighted objective, limiting robustness when priorities change. This paper addresses
these gaps by combining multi-source attention (self/inter-agent/entity) for selective
information fusion with a Pareto module for vector rewards, integrated into a CTDE-
style method so that non-dominated trade-offs are discovered during training rather than
predetermined by fixed weights.
3. Background Knowledge
3.1. Multi-Agent Reinforcement Learning
Multi-agent reinforcement learning (MARL) is a key framework for handling multiple
agents that pursue cooperative or competitive goals through sequential decisions in a shared
environment. Unlike single-agent reinforcement learning, MARL faces core challenges:
environmental non-stationarity, credit assignment, and mutual policy influence among
agents. In UAV formation control, these challenges are pronounced. Each UAV must act on
local observations, yet their joint actions determine overall system performance.
To address these issues, many MARL paradigms have been proposed. Centralized
Training with Decentralized Execution (CTDE) is the mainstream. Its idea is to use global
information during training to learn cooperative policies, while at execution, each agent
relies only on its own observations. This balances model expressiveness and system
scalability. A representative algorithm is MADDPG [16]. It combines a centralized critic
with decentralized actors and mitigates non-stationarity to some extent.
However, traditional MARL still has clear limits. Agents often lack selective perception
of multi-source state information and cannot focus on key cues in complex environments.
Most methods also rely on a scalar reward formed by linear weighting of multiple objectives.
This cannot capture complex trade-offs among objectives. These limits motivate our use

## Page 6

Drones 2025, 9, 845
6 of 34
of attention mechanisms and multi-objective optimization to improve MARL for UAV
formation control.
3.2. Attention Mechanisms
Attention provides selective information fusion: a model assigns higher weights to
salient parts of its inputs and suppresses distractions, thereby improving long-range de-
pendency modeling and feature prioritization. Beyond its well-known success in NLP and
CV, attention is increasingly used in multi-agent systems (MAS)—including cooperative
UAV control—to filter self states, neighbor cues, and environmental entities under partial
observability and communication imperfections.
We use the standard scaled dot-product attention as the basic operator:
Attn(Q, K, V) = softmax
 
QK⊤
√dk
!
V,
(1)
where queries Q encode the current information need, keys K index candidate features,
and values V carry the content to aggregate. The softmax normalizes relevance scores into
a distribution and yields a context vector by weighted summation. Multi-head variants
apply (1) in parallel and concatenate the outputs for richer feature subspaces.
In the context of UAV formation control, attention is particularly useful for the following:
•
Selective perception: highlight task-relevant parts of the local observation (e.g., goal
direction, energy, safety margins).
•
Targeted coordination: focus on the most influential neighbors for collision avoidance
and formation keeping.
•
Salient environment awareness: emphasize nearby obstacles or bottlenecks in clut-
tered, urban-like scenes.
These properties make attention a natural fit for CTDE-style MARL: it improves the
actors’ input representations under partial observability and reduces non-stationarity seen
by centralized critics. In Sections 4 and 5 we instantiate this idea via self-, inter-agent-,
and entity-attention modules tailored to UAV teams.
As illustrated in Figure 1, the scaled dot product attention computes relevance via
QK⊤/√dk, normalizes by softmax, and aggregates values V. In our setting, queries encode
the agent’s information need, while keys/values are drawn from self features, neighbors,
or entities. This makes Figure 1 the canonical operator underpinning the three typed
branches we instantiate for UAV teams.
Figure 1. Schematic of scaled dot-product attention: relevance is computed via QK⊤/
p
dk, normal-
ized by softmax, and applied to V to form the context.

## Page 7

Drones 2025, 9, 845
7 of 34
3.3. Multi-Objective Optimization
Multi-objective optimization handles trade-offs among conflicting objectives. The core
concept is Pareto optimality: a solution set where no objective can be improved without
worsening another. The problem is formalized as follows:
min
x∈X [ f1(x), f2(x), . . . , fk(x)]T
(2)
In multi-UAV cooperative control, common objectives include path length, energy
consumption, safety, and formation-keeping accuracy. Traditional methods often use a
scalarization function to convert multiple objectives into a single one, but this cannot
fully capture complex trade-offs. Pareto-based methods provide a set of optimal trade-off
solutions and give richer information for decision-making.
In summary, this paper integrates multi-agent reinforcement learning, attention mech-
anisms, and multi-objective optimization to build a collaborative decision framework
for multi-UAV formation control. It addresses multi-objective coordination challenges in
dynamic environments.
4. Problem Formulation
We study cooperative multi–UAV formation control in a built urban area. A team
departs from randomized starts and moves to a goal region while (i) avoiding collisions
with buildings and teammates, (ii) keeping a prescribed formation, (iii) limiting con-
trol/energy usage, and (iv) finishing within a time budget. This setting is representative of
city scale sensing and relay missions, where formation coherence benefits coverage and
link reliability (Figure 2).
Start
Goal
rsafe
Start
Goal
Building
UAV + rsafe
Path
Sensing boundary
Figure 2. Problem setup (top view). Workspace: x∈[0, 100] m, y∈[0, 100] m, z∈[0, 22] m. Buildings
are within x ∈[10, 90], y ∈[10, 90]; half-length/width ∈[1, 10] m, height ∈[9, 13] m (cap 20). Initial
region: x∈[15, 30], y∈[10, 90], z∈[3, 7]; target region: x∈[60, 90], y∈[10, 90], z∈[3, 15]. Example radii
for illustration: sensing radius ≈15 m, safety radius rsafe = 2 m. The legend is placed below the map
to avoid any overlap with the environment elements.

## Page 8

Drones 2025, 9, 845
8 of 34
4.1. Game Model and CTDE Setting
We model the task as a partially observable Markov game (POMG) G defined as
G =
 I, S, {Oi}N
i=1, {Ai}N
i=1, P, {Ri}N
i=1, γ

.
(3)
with discrete time t=0, . . . , T and step ∆t. The agent set is I = {1, . . . , N}. Training follows
CTDE: a centralized critic sees global information during learning, whereas execution relies
only on local observations.
For the critic, the global state stacks team kinematics, the goal and the formation
blueprint, and nearby obstacles:
st =

Xt, Vt, G, F, Et

,
(4)
where Xt = [x1,t, . . . , xN,t] and Vt = [v1,t, . . . , vN,t] are positions and velocities, G en-
codes the goal pose/region, F stores desired slot offsets {r⋆
i }N
i=1 (formation template), and
Et = {bk}M
k=1 lists the M nearest axis–aligned buildings represented by centers and half–sizes.
4.2. Observations and Actions
Each agent observes only local information. To match the three attention branches
used later, we organize the local observation into three parts and then fuse them as
˜si,t = Concat
SelfAtt(oself
i,t ), InterAtt(ointer
i,t
), EntityAtt(oent
i,t )

.
(5)
Self features. oself
i,t
=

xi,t, vi,t, gi,t, ei,t, dgoal
i,t

, where xi,t ∈R3 and vi,t ∈R3
are position and velocity, gi,t is heading, ei,t ∈[0,1] is normalized remaining energy,
and dgoal
i,t
= ∥xi,t −xgoal∥2 is distance to the goal. Inter–agent features. For the K nearest neigh-
bors N K
i , we use relative kinematics ointer
i,t
= {∆xij,t = xj,t −xi,t, ∆vij,t = vj,t −vi,t, dpair
ij,t
=
∥∆xij,t∥2}j∈N K
i with fixed K (e.g., K = 4) recomputed each step. Entity features. For the M
closest buildings to agent i, oent
i,t = {∆xik,t = ck −xi,t, hk, wk, ℓk}M
k=1, where ck is the building
center and (hk, wk, ℓk) are half–sizes; a small M (e.g., M = 10) keeps inference time predictable.
Actions are 3-D thrust/velocity commands subject to a magnitude bound,
ai,t ∈Ai ⊂R3,
∥ai,t∥2 ≤amax.
(6)
4.3. Vector Reward and Termination
Control is multi-objective. Each agent receives a four-dimensional reward covering
task progress, energy, formation coherence, and safety,
Ri(st, at, st+1) =

rtask
i
, renergy
i
, rformation
i
, rsafety
i
	
,
(7)
with homogeneous definitions and fixed coefficients across runs (defaults in parentheses).
Task progress and success. With ηsucc = 5.0 and cprog = 0.5,
rtask
i
= ηsucc · 1
n
dgoal
i,t+1 ≤εgoal
o
−cprog·
dgoal
i,t+1 −dgoal
i,t

,
(8)
so moving closer to the goal is rewarded each step and entering the εgoal-ball yields a
one-off bonus. Energy/control. With ceng = 0.01,
renergy
i
= −ceng · ∥ai,t∥2
2.
(9)

## Page 9

Drones 2025, 9, 845
9 of 34
Formation coherence. With cform = 1.0 and εform = 1.0,
devt =
1
N
N
∑
i=1
xi,t −xref
i,t

2,
rformation
i
= −cform · devt + 0.2 · 1{devt ≤εform}, (10)
where the reference slot xref
i,t = xlead,t + r⋆
i follows a (virtual) leader; small average slot error
is mildly rewarded. Safety. With ccol = 5.0, cnear = 1.0, and δ = 2.0 m,
rsafety
i
= −ccol · 1{collision at t} −cnear · 1
n
min
dpair
ij,t , dobs
i,t
 < δ
o
,
(11)
where dobs
i,t is the distance to the nearest building surface. An episode ends when all agents
are in the goal region, upon any collision, or at the horizon T.
4.4. Objective and CTDE Realization
We seek decentralized actors that are Pareto–efficient with respect to the four objectives
under a centralized critic. Let the joint policy be π = {πi}N
i=1 with per–agent actor
πi(ai,t | ˜si,t). The vector return averaged across agents is
J(π) = E
"
T
∑
t=0
γt · 1
N
N
∑
i=1
Ri(st, at, st+1)
#
,
(12)
and policies are ordered by Pareto dominance (no worse in all objectives and strictly better
in at least one). The centralized critic estimates per–objective values that guide updates,
Q(κ)(st, at),
κ ∈{task, energy, formation, safety},
(13)
while the actors consume ˜si,t constructed in (5). This separation keeps modeling choices
(rewards and constraints) and architecture (attention and CTDE) cleanly decoupled.
5. Proposed Method
5.1. Framework Overview
This paper proposes an improved framework for autonomous UAV formation control
that is algorithm-agnostic: Our attention front end and Pareto layer are compatible with
standard CTDE actor–critic backbones (e.g., MADDPG, MATD3, MASAC, and MAPPO)
with minimal glue code: the attention block replaces the observation encoder before each
actor, and the Pareto layer operates on per-objective critics or advantages. In this paper,
we instantiate and evaluate the design on MADDPG for concreteness and fairness of
comparison, while deferring a broader cross-backbone benchmark to future work due to
runtime and tuning budgets in long-horizon urban tasks. In this work, we instantiate the
framework with MADDPG to provide a concrete realization and fair comparison, but the
design applies equally to other backbones (e.g., MATD3/MASAC/MAPPO). Unlike stacked
GNN/Transformer front ends, our attention block is intentionally typed and single-hop to
meet on-board budgets; Section 5.3 details this contrast.
MADDPG [16], a common MARL method, follows the Centralized Training–Decentralized
Execution (CTDE) paradigm: a centralized critic evaluates global information during training,
and decentralized actors execute from local observations. Building on this backbone, we
introduce attention mechanisms to enhance the handling and fusion of local observations
under partial observability. As shown in Figure 3, the overall pipeline still follows CTDE but is
adapted to multi-objective formation control.

## Page 10

Drones 2025, 9, 845
10 of 34
Specifically, each UAV decides from its local observation, while the Attention Enhance-
ment Layer applies three lightweight module. The three outputs are concatenated into an
attention-enhanced representation
˜si = Concat

SelfAtt(oself
i
), InterAtt(ointer
i
), EntityAtt(oent
i
)

.
(14)
The Actor maps ˜si to action ai, and centralized Critics estimate per-objective val-
ues {Qtask, Qenergy, Qformation, Qsafety} in parallel.
During training, the Pareto layer
maintains a compact archive of non-dominated solutions and provides adaptive sig-
nals/weights to guide updates, thereby avoiding brittle manual scalarization. We store
(s, a, r, s′, attention context) in an attention-aware replay buffer and optimize a combined
loss Ltotal = λ1Lcritic + λ2Lactor + λ3Lattention + λ4Lpareto.
In summary, when instantiated with MADDPG (Figure 3), the attention block improves
information saliency under partial observability and the Pareto layer enforces principled
multi-objective trade-offs; more generally, these two modules augment the chosen MARL
backbone with minimal changes and are applicable to a wide range of CTDE actor–critic
methods beyond MADDPG.
Figure 3. Overall framework: plug-and-play attention (self/inter-agent/entity) before each decen-
tralized actor, and a Pareto layer over vector critics during centralized training. We instantiate with
a MADDPG backbone for concreteness, but the modules are applicable to other CTDE actor–critic
MARL algorithms.
5.2. Attention Mechanism Integration
The attention mechanisms in our framework serve three distinct but complemen-
tary purposes: enhancing inter-agent communication, improving environmental percep-

## Page 11

Drones 2025, 9, 845
11 of 34
tion, and enabling hierarchical decision-making. Each mechanism addresses specific chal-
lenges in multi-agent coordination while contributing to the overall system performance.
Below we detail the three attention mechanisms integrated in our framework.
Self-Attention Mechanism: The self-attention mechanism processes the internal state
representation of each UAV agent to identify the most relevant features for decision-making.
Given an agent’s state vector si ∈Rd, the self-attention module computes attention weights
αi,j for each state component j:
αi,j =
exp(Wqsi,j · Wksi,j)
∑d
k=1 exp(Wqsi,k · Wksi,k)
(15)
where Wq and Wk are learned query and key transformation matrices. This mechanism
enables agents to dynamically prioritize different aspects of their internal state based on
the current situation, improving decision quality in complex scenarios through adaptive
feature weighting.
Inter-Agent Attention Mechanism: The inter-agent attention mechanism facilitates
explicit communication between UAV agents by computing attention weights over neigh-
boring agents’ states. For agent i with neighbors Ni, the inter-agent attention weight for
neighbor j is computed as follows:
βi,j =
exp( fatt(si, sj))
∑k∈Ni exp( fatt(si, sk))
(16)
where fatt is a neural network that computes the relevance score between agent i and agent
j. This mechanism allows agents to selectively focus on the most relevant teammates for
coordination, enabling effective formation maintenance and collision avoidance through
targeted information exchange.
Entity Attention Mechanism: The entity attention mechanism processes environmen-
tal entities such as obstacles, targets, and dynamic elements. Given a set of environmental
entities E = {e1, e2, . . . , em}, the mechanism computes attention weights to determine the
relevance of each entity to the current agent:
γi,k =
exp(gatt(si, ek))
∑m
l=1 exp(gatt(si, el))
(17)
This mechanism enables agents to dynamically focus on the most relevant environ-
mental features, significantly improving navigation efficiency and obstacle avoidance
capabilities by filtering irrelevant sensory input.
Interpreting Attention as Information Priority
Throughout this work, the softmax weights produced by each branch are interpreted
as information priorities. For the inter-agent branch, with query qi from agent i and
per-neighbor keys/values {kj, vj}j∈Ni(t),
βij,t = softmaxj
 
q⊤
i kj
√dk
!
,
minter
i,t
= ∑
j∈Ni(t)
βij,t vj,
(18)
where ∑j βij,t = 1 over the available neighbors. A higher βij,t means neighbor j contributes
more to the aggregated message minter
i,t
and thus has higher decision priority at time t. For
the entity branch, γik,t is defined analogously and ranks environmental entities by priority;
for self-attention we obtain feature-group weights wi,t that reweight internal cues (goal
bearing, safety margins, energy, etc.). When packets are dropped or links are removed

## Page 12

Drones 2025, 9, 845
12 of 34
at test time, masked entries are excluded and the remaining weights are renormalized;
if no neighbor is available, a learned default vector is used. The actor consumes the
fused representation
˜si,t = Concat
mself
i,t , minter
i,t
, ment
i,t

,
so “priority” directly governs which cues dominate the policy input. We also quantify
concentration via attention entropy Hi(t) = −∑j βij,t log βij,t and the Top-1 share maxj βij,t
when needed.
Within the CTDE pipeline, attention acts as the front end of representation. Self–attention
filters an agent’s own kinematics and intent, inter-agent attention highlights the few teammates
that matter for the current maneuver, and entity attention foregrounds the most influential
obstacles.The fused vector ˜si is therefore more structured and temporally stable than raw
observations, so the centralized multi–objective critics receive inputs in which progress,
formation deviation, energy use, and risk are easier to tease apart. In practice, this yields
cleaner per–objective value estimates and crisper policy gradients, reducing ambiguity
about which agent and which objective should change. Attention thus strengthens state
representation on the actor side and, as a consequence, helps the critics allocate credit with
fewer confounding correlations.
5.3. Design Contrast to Stacked GNN/Transformer Front Ends
Our front end uses three typed, single-hop attention branches (self/inter-agent/entity)
that act as feature selectors feeding a CTDE actor–critic. This is not a stacked GNN/Transformer
encoder. The key differences are as follows:
(i)
Receptive field and depth. We perform one-hop aggregation over the K nearest team-
mates and the M closest entities per step and do not stack layers; stacked GNNs prop-
agate over L hops (depth L), while stacked Transformers perform global token mixing
at each layer. Our single-hop choice preserves local reactivity and bounds latency.
(ii)
Heterogeneous typing vs.
homogeneous mixing.
We keep self/inter/entity
streams separate and then concatenate, rather than mixing all tokens in one ho-
mogeneous block. This avoids learning type embeddings/positional encodings and
reduces compute.
(iii) Compute/latency scaling. Per agent per step, our cost scales linearly with K+M
(fixed fan-in). Stacked GNNs scale with edges and depth (O(L |E|) with |E| ≈NK),
and stacked Transformers scale quadratically in tokens per layer (O(L T2) with
T ≈1+K+M).
(iv) Communication modeling. We mask unavailable links and renormalize attention at
test time; we do not backpropagate through an explicit learned channel. Many stacked
designs assume reliable broadcast or learn graph topology.
(v)
Training signal. Our vector critics with a Pareto archive address multi-objective
trade-offs; most stacked variants optimize a scalarized reward unless customized.
In short, although we use the attention operator, the resulting architecture is a typed,
single-layer, local selector tailored to real-time UAV control rather than a deep message-
passing or global token-mixing stack.
With fixed neighbor and entity fan-in (K, M), our typed single-hop attention adds
O(K+M) per-agent compute per control step (actor side); thus the test-time team cost
scales linearly in N. Centralized critics contribute during training only and do not affect
deployment-time latency. This matches the summary in Table 1. In practice, bounded K,
bounded M, masking of missing links, and mixed-precision inference keep the actor-side
latency predictable as N grows.

## Page 13

Drones 2025, 9, 845
13 of 34
Table 1. Architectural contrast between PA-MADDPG and stacked GNN/Transformer front ends.
Aspect
PA-MADDPG (This Work)
GNN-Based MARL (Stacked)
Transformer-Based RL (Stacked)
Mixing scope
Single-hop KNN neighbors + M
entities; typed branches; concat
L-layer message passing;
L-hop receptive field
Self/cross-attn over all tokens;
global mixing per layer
Complexity per step
O(K+M) with fixed fan-in
O(L |E|), |E|≈NK
O(L T2), T ≈1+K+M
Latency/memory
Low; on-board friendly
Medium–high; grows with L, N
High; quadratic in tokens
Heterogeneity
handling
Typed (self/inter/entity);
no type embeddings
Requires typed edges/engineering Needs token-type/
positional encodings
Communication
model
Masked KNN;
renormalized attention
Fixed/learned graph;
often reliable links
Often assumes global broadcast
Training signal
Vector critics + Pareto
(multi-objective)
Usually scalarized reward
Usually scalarized reward
Primary goal
Real-time local control
Expressive multi-hop reasoning
Global context/long-range mixing
5.4. Pareto Multi-Objective Optimization
The Pareto optimization component addresses the inherent multi-objective nature of
UAV formation control, where agents must simultaneously optimize competing objectives,
including task completion, energy efficiency, formation maintenance, and collision avoid-
ance. Traditional reinforcement learning approaches struggle with such multi-objective
scenarios due to the difficulty in defining appropriate reward weightings.
Our Pareto-based framework formulates the problem as a multi-objective optimization
where the reward function Ri for agent i consists of distinct objective components:
Ri = {rtask
i
, renergy
i
, r f ormation
i
, rsa f ety
i
}
(19)
each representing critical operational dimensions. The approach maintains a set of non-
dominated solutions, enabling exploration of diverse objective trade-offs without manual
tuning of reward weights.
The Pareto dominance relationship is defined such that solution x dominates solution
y if x is at least as good as y in all objectives and strictly better in at least one objective.
The algorithm maintains an archive of non-dominated solutions to guide policy updates:
πnew
θi
= arg max
θi
E
"
T
∑
t=0
γtRi(st, at, st+1)
#
(20)
The above update is carried out under explicit Pareto-optimality constraints, which
preserve non-dominated solutions and encourage coverage of diverse trade-offs across
objectives. This constraint guarantees that selected policies represent efficient compromises
between competing goals.
This approach fundamentally eliminates the need for manual reward engineer-
ing while ensuring robust performance across all operational dimensions. The prac-
tical significance is particularly valuable in UAV missions where objective priorities
dynamically shift during different mission phases, providing adaptive optimization
without parameter recalibration.

## Page 14

Drones 2025, 9, 845
14 of 34
5.5. Integrated Framework Architecture
The integrated framework incorporates attention mechanisms with Pareto optimiza-
tion within a modified MADDPG architecture through a hierarchical processing pipeline.
This unified structure comprises three principal components: an attention-enhanced ob-
servation processor, a multi-objective critic network, and a coordinated actor network,
collectively forming the core innovation of our approach.
The attention-enhanced observation processor transforms raw sensory inputs into
enriched state representations through sequential attention layers. This module simulta-
neously applies self-attention to internal states, inter-agent attention to neighboring UAV
states, and entity attention to environmental features. The resulting representations are
concatenated to form a comprehensive state vector:
˜si = Concat
SelfAtt(si), InterAtt(si, sNi), EntityAtt(si, E)

(21)
where each attention module operates according to the mechanisms defined in Section 3.1
The multi-objective critic network extends conventional value estimation by maintain-
ing separate value functions for each operational dimension:
Qϕi(s, a) =
h
Qtask
ϕi (s, a), Qenergy
ϕi
(s, a), Qformation
ϕi
(s, a), Qsafety
ϕi
(s, a)
i
(22)
This architectural innovation enables distinct value estimation for competing objec-
tives, facilitating precise credit assignment during policy updates under Pareto constraints.
The coordinated actor network synthesizes the attention-enhanced state representa-
tions into actions that balance individual objectives with collective coordination require-
ments. To ensure training stability in decentralized execution, the network architecture
incorporates residual connections and layer normalization techniques:
ai ∼πθi(·|˜si)
(23)
A critical feedback loop emerges between these components: attention mechanisms
dynamically inform policy decisions, which subsequently reshape attention patterns as en-
vironmental conditions evolve. This adaptive interaction enables continuous optimization
of mission-specific trade-offs without manual parameter adjustment.
5.6. Pareto Archive, Normalization, and Adaptive Weighting
5.6.1. Per-Objective Normalization
Let J(e) =

J(e)
task, J(e)
energy, J(e)
formation, J(e)
safety

denote the episodic returns of the four ob-
jectives for episode e (computed consistently with Equation (12), aggregated at the team
level). Because scalar magnitudes differ across objectives, we normalize each objective by
an online affine transform based on a running min–max envelope built from the current
archive A and a FIFO buffer B of recent episodes:
˜J(e)
k
=
J(e)
k
−mk
Mk −mk + ε,
˜J(e)
k
∈[0, 1],
where mk and Mk are per-objective running minima/maxima (updated by an EMA with de-
cay 0.99) over { J(e) ∈B } ∪A, and ε = 10−8 prevents division by zero. This monotone map-
ping preserves Pareto order but equalizes scales for weighting and diversity calculations.

## Page 15

Drones 2025, 9, 845
15 of 34
5.6.2. Archive Update and Pruning
We maintain a bounded archive A of non-dominated normalized vectors in [0, 1]4. Given
a candidate ˜J from the current policy, we use ϵ-dominance with a small per-objective margin
ϵk = 0.01 to reduce churning:
˜u ≺ϵ ˜v
⇔
∀k : ˜uk ≤˜vk + ϵk
 ∧
∃k : ˜uk < ˜vk −ϵk

,
with maximization understood via flipping signs where needed. If no ˜a ∈A ϵ-dominates
˜J, we insert ˜J and remove all archive points that are ϵ-dominated by ˜J. To enforce the
capacity |A| ≤Kmax (default Kmax = 100; Table 2), we prune by NSGA-II crowding distance
in normalized space: when overflow occurs, repeatedly remove the point with the smallest
crowding distance; ties are broken by oldest timestamp to favor fresh coverage.
Table 2. Hyperparameters of the proposed multi-agent attention-DRL framework.
Category
Parameter
Value
Network Architecture
Actor hidden layers
[256, 128]
Critic hidden layers
[512, 256, 128]
Attention dimension
64
Training
Actor learning rate
1 × 10−4
Critic learning rate
1 × 10−3
Batch size
256
Replay buffer size
106
Discount factor γ
0.99
Soft-update τ
0.01
Attention
Self-attention heads
4
Inter-agent range (m)
10.0
Entity attention range (m)
15.0
Pareto Archive
Archive size
100
Update frequency
10 steps
5.6.3. Adaptive Scalarization ParetoWeight(A, π)
We derive a per-objective weight vector λ ∈∆3 (simplex) that emphasizes ob-
jectives where the current policy underperforms the archive. Let the utopia vector be
z⋆
k = max˜a∈A ˜ak. Let ¯J be the current policy’s expected normalized returns (estimated from
a validation batch or a short evaluation). Define nonnegative gaps gk = max{0, z⋆
k −¯Jk}
and compute a softmax with temperature τw:
λk =
exp
gk/τw

∑j exp
gj/τw
,
τw = 0.15.
To avoid collapsing to one objective, we mix with the uniform prior uk = 1/4:
λfinal
k
= (1 −ρ) uk + ρ λk,
ρ ↑0.9 linearly over training.
These weights enter the multi-objective losses as Ltotal = ∑k λfinal
k
Lk, with Lk defined per
objective (Section 5). Because critics are trained on normalized targets, λ operates on
comparable scales.
5.6.4. Computation Frequency and Overhead
We call ArchiveUpdate every 10 gradient steps (same as Table 2, “Update frequency”),
recompute λ each update, and refresh (mk, Mk) from the union A ∪B. All operations are
in R4 and negligible relative to actor–critic backprop.

## Page 16

Drones 2025, 9, 845
16 of 34
5.6.5. Archive-Size Sensitivity (How Kmax Matters)
We quantify diversity by hypervolume (HV) in normalized [0, 1]4 with reference r=0,
estimated by Monte Carlo with 105 samples. As reported in Section 6.3 (Sensitivity),
sweeping Kmax ∈{50, 100, 150, 200} shows that Kmax = 100 retains ≈85% of the maximum
HV while incurring only ≈60% of the computational cost of larger archives; smaller Kmax
reduces HV notably (coverage gaps along safety/energy). Accordingly. we default to
Kmax = 100 and expose it as a tunable parameter.
5.7. Training Algorithm and Implementation
Our training methodology extends the MADDPG framework with integrated attention
mechanisms and Pareto optimization, creating a robust learning system for multi-UAV
coordination. The algorithm maintains the CTDE paradigm, where centralized critics
leverage global information during training while decentralized actors operate solely on
local observations during mission execution. This architecture preserves the scalability
advantages of decentralized systems while benefiting from centralized learning.
A critical innovation lies in the attention-aware experience replay mechanism. Tra-
ditional experience tuples (st, at, rt, st+1) are augmented with attention context vectors
(αt, βt, γt) capturing the instantaneous focus patterns across all three attention mechanisms.
This preservation of attention context during replay significantly enhances learning stability
and prevents catastrophic forgetting of attention patterns. The replay buffer implements
stratified sampling to ensure balanced representation across diverse attention contexts and
mission scenarios.
The multi-objective loss function incorporates four essential components with Pareto-
optimized dynamic weighting:
Ltotal = λ1Lcritic + λ2Lactor + λ3Lattention + λ4Lpareto
(24)
where Lattention enforces temporal consistency in attention weight learning and Lpareto
maintains diversity in the evolving Pareto front. The adaptive coefficients λi are adjusted
based on the dominance relationships within the current solution archive.
Implementation employs PyTorch with custom CUDA kernels optimized for parallel
attention computation. Network architectures utilize multilayer perceptrons with ReLU
activations and batch normalization, with hyperparameters, including attention dimension
datt = 64, replay buffer capacity of 106 transitions, batch size of 256, and discount factor
γ = 0.99. The Pareto archive maintains up to 100 non-dominated solutions to balance
solution diversity against computational overhead.
Inter-agent features are conveyed over a logical neighbor graph. To emulate imperfect
networking at evaluation time, we inject Bernoulli packet loss (ploss), random delays by
replaying stale neighbor states from a short history (uniform in [0, Dmax] ms), and time-
varying topologies by probabilistic link removals at rate q. Missing entries are dropped
and represented by zero vectors (equivalently, masked in attention). We also consider
adversarial perturbations by adding Gaussian noise to features, occasionally spoofing an
obstacle, or throttling the neighbor fan-in K.
The overall algorithm process of the paper is shown in the following pseudocode
(Algorithm 1).

## Page 17

Drones 2025, 9, 845
17 of 34
Algorithm 1: Multi-Attention Meets Pareto Optimization.
Input
: N agents, datt, K, {θi}, {ϕi}, D
Output:Optimized policies {πi}
1 Initialize: θi, ϕi, θtarget
i
, ϕtarget
i
∀i; A ←∅; D ←∅
2 for episode = 1 to M do
3
s ←env.reset()
4
for t = 1 to T do
5
foreach agent i do parallel
// Observation & Attention
6
α ←AttMechanisms(si, sNi, E)
7
˜si ←Concat(α ⊙[si, sNi, E])
8
ai ←πθi(˜si) + N (0, σ)
9
a ←{ai}N
i=1
10
s′ ←env.step(a)
11
R ←[rtask, renergy, rformation, rsafety]
12
D.store(s, a, R, s′, α)
13
s ←s′
14
if |D| > batch_size then
15
B ∼D
16
foreach agent i do
// Critic Update
17
yk ←rk + γ Qk
ϕtarget
i
s′, πθtarget(˜s′)

18
Lcritic ←∑k ∥Qk
ϕi −yk∥2
// Actor & Pareto
19
∇θ J ←E
∇aQϕi ∇θπθ

20
if πθi is non-dominated then
21
A ←A ∪{πθi}
22
A.remove_dominated()
23
if |A| > K then
24
A.prune()
25
λ ←ParetoWeight(A, πθi)
26
Ltotal ←∑4
j=1 λjLj
27
θi, ϕi ←Adam(Ltotal)
28
θtarget ←τθ + (1 −τ)θtarget
29
ϕtarget ←τϕ + (1 −τ)ϕtarget
30 return {πθi}, A
6. Experiment
6.1. Experimental Setup
Comprehensive experiments were conducted across diverse UAV formation control
scenarios to evaluate the performance of our attention-enhanced MADDPG framework.
The evaluation protocol includes comparative analysis against state-of-the-art multi-agent
reinforcement learning methods, ablation studies of individual components, and sensitivity
analysis of key hyperparameters.
The hardware infrastructure comprised a high-performance computing cluster featur-
ing NVIDIA RTX 4090 GPUs (24 GB VRAM per device), Intel Xeon Gold 6248R processors
(3.0 GHz, 24 cores), and 128 GB DDR4 memory. All experiments were executed under

## Page 18

Drones 2025, 9, 845
18 of 34
Ubuntu 20.04 LTS with CUDA 11.8 and cuDNN 8.6 acceleration. To maximize compu-
tational throughput, multi-GPU training with data parallelism across four GPUs was
employed for resource-intensive configurations.
Implementation leveraged PyTorch 2.0.1 with Python 3.9.16 as the foundational soft-
ware stack. Essential dependencies included NumPy 1.24.3 for numerical operations,
Matplotlib 3.7.1 for visualization, TensorBoard 2.13.0 for experiment logging, and Ope-
nAI Gym 0.21.0 for environment interfaces. Custom CUDA kernels optimized attention
computations for enhanced execution efficiency.
Hyperparameter configuration, established through systematic grid search, is compre-
hensively detailed in Table 3. Critical parameters encompassed actor learning rate (10−4),
critic learning rate (10−3), replay buffer capacity (106 transitions), batch size (256), discount
factor γ (0.99), soft update coefficient τ (0.01), attention dimension (64), and Pareto archive
size (100). Unless otherwise stated, each experiment trains for 10,000 episodes without
early stopping or fine-tuning. Curves report the 100-episode moving average, and unless
specified otherwise we aggregate results over 5 random seeds (mean ± s.d.). All training
figures share the same x-axis 10,000 episodes).
Table 3. Notation used in the formulation.
Symbol
Description
I, N
Agent set and its size
t, T, ∆t
Time index, horizon, and time step
st, oi,t, ai,t
Global state, local observation, and action
G
Goal pose/region encoding
F, r⋆
i
Formation template and per–agent slot offset
Et, M
Set of M nearest buildings (centers and half–sizes)
K
Number of neighbor slots in ointer
Ri
Reward vector in (7)
γ
Discount factor
πi, π
Decentralized policy and joint policy
Q(κ)
Per objective centralized critic in (13)
amax, δ, εgoal
Action bound, safety distance, goal threshold
6.2. Baseline Selection and Scope
We benchmark against two widely used CTDE references at opposite ends of the
complexity spectrum: (i) MADDPG (off-policy deterministic actor–critic with centralized
critics and decentralized actors), and (ii) IDQN (value-based). This pairing isolates the
effect of our two modules (typed single-hop attention and Pareto multi-objective layer)
under identical training protocols and hyperparameter schedules.
Including additional actor–critic backbones, such as MATD3, MASAC, or MAPPO,
is feasible in principle but was excluded in this study for three pragmatic reasons.
(1) Fairness vs. confounds. Our goal is to measure the incremental contribution of the
proposed modules on a fixed CTDE template; mixing heterogeneous backbones introduces
confounds (on-policy vs. off-policy, stochastic vs. deterministic policies, entropy regu-
larization, advantage estimation) that blur attribution. (2) Runtime and tuning budget.
Each setting here trains for 10,000 episodes, across N = 2, 3, 5 and multiple seeds. Adding
MATD3/MASAC/MAPPO (each with their own stability-sensitive hyperparameters such
as target smoothing or entropy temperature) would multiply wall-clock cost and require
careful re-tuning per N. (3) On-board feasibility focus. Our design targets low-latency ex-
ecution (single-hop attention with fixed fan-in); stacked or on-policy baselines substantially
raise sample or compute costs, which is orthogonal to the contribution we study.

## Page 19

Drones 2025, 9, 845
19 of 34
To support reproducibility and future extensions, we provide implementation notes
and configuration details in the main text and in the released code base, including how to
attach our attention/Pareto modules to MATD3, MASAC, and MAPPO (losses, targets, and
where adaptive weights enter). We will incorporate these broader baselines in a follow-on
study with expanded runtime budgets.
6.3. Experimental Environment
Built on the simulator from https://github.com/young-how/DQN-based-UAV-3D_
path_planer (accessed on 27 October 2025) , we extend the environment to a multi-UAV
setting. For clarity, the visualization of the environment and results is shown in Figure 4.
Figure 4. Three-dimensional environmental schematic diagram.
The workspace is a 3D volume with x ∈[0, 100], y ∈[0, 100], and z ∈[0, 22]. Buildings
are randomly generated in this region, with both location and size sampled at random.
To avoid excessive obstacles at the start of training, the number of buildings increases
gradually as training proceeds; when the success rate over the most recent 100 navigation
tasks exceeds 70%, the building count is increased. The total number of buildings is
capped at 20. Buildings lie within x ∈[10, 90], y ∈[10, 90] on the plane; their half-
lengths are in [1, 10], half-widths in [1, 10], and heights in [9, 13]. The initial UAV region is
x ∈[15, 30], y ∈[10, 90], z ∈[3, 7]; the target region is x ∈[60, 90], y ∈[10, 90], z ∈[3, 15].
A 2D top-down view in Figure 5 further illustrates the scene configuration.
Because stacked GNN/Transformer encoders increase latency and memory substan-
tially, we focus our empirical comparison on widely used CTDE baselines (MADDPG,
IDQN) and on ablations of our attention/Pareto components under identical training pro-
tocol. To keep on-board feasibility front and center, we provide an architectural comparison

## Page 20

Drones 2025, 9, 845
20 of 34
with stacked GNN/Transformer fronts (Section 5.3; Table 1) instead of adding deep stacks
that violate our real-time budget.
Figure 5. Two-dimensional top view of the environment.
6.4. Evaluation Metrics and Units
We report four primary metrics with formal operational definitions and units. Unless
otherwise stated, all rates are computed at the team/episode level and summarized as the
100-episode moving average at the end of training/evaluation; tables show mean ± s.d.
across seeds of this summary.
6.4.1. Team Success Rate (%)
An episode e is successful if all agents reach the goal region within the horizon T and
no collision occurs:
1(e)
succ = 1
∀i ∈I : τ(e)
i
≤T ∧no collision in e
	
.
Over an evaluation set E (e.g., the last 100 episodes), the team success rate is
Succ. rate =
1
|E| ∑
e∈E
1(e)
succ × 100%.
This is the quantity plotted in training curves (smoothed by a 100-episode window);
small text boxes inside some figures show the last-episode instantaneous value for quick
visual reference.

## Page 21

Drones 2025, 9, 845
21 of 34
6.4.2. Formation Deviation (m)
Let the per-step team-wide formation error be the average slot error
devt =
1
N
N
∑
i=1
xi,t −xref
i,t

2
[m],
where xref
i,t is the desired slot for agent i (Section 4). The episode-level formation deviation
is the time average
D(e) =
1
Te
Te−1
∑
t=0
devt
[m],
and the reported number is the mean D(e) over E (with s.d. across seeds).
6.4.3. Collision Rate (%)
We use an episode-level collision indicator
1(e)
col = 1
∃t ≤T, ∃i : agent–obstacle or inter-agent collision at t
	
.
The collision rate is
Collision rate =
1
|E| ∑
e∈E
1(e)
col × 100%.
(For analysis we also track a step-wise near-miss rate 1{min(dpair
ij,t , dobs
i,t ) < δ}, but unless
stated otherwise, tables/figures report the episode-level rate above.)
6.4.4. Energy Efficiency (Unitless, [0, 1])
Per agent, define normalized control energy over episode e as
E(e)
i
=
1
Te a2max
Te−1
∑
t=0
∥ai,t∥2
2 ∈[0, ∞).
Team-average normalized energy is ¯E(e) = 1
N ∑N
i=1 E(e)
i
, and we report energy efficiency as
ηeng = 1 −1
|E| ∑
e∈E
¯E(e)
∈(0, 1],
so higher is better (lower control effort). This metric is consistent with, but distinct from,
the shaping term renergy
i
in Equation (9).
6.5. Experimental Results and Discussion
The experimental results demonstrate the superior performance of our attention-
enhanced MADDPG framework across all evaluation scenarios. Our approach consistently
outperforms baseline methods in terms of task success rate, formation quality, and sample
efficiency. The following subsections provide detailed analysis of the comparative results,
ablation studies, and sensitivity analysis.
6.5.1. Comparison with State-of-the-Art Methods
We compare the proposed method with MADDPG and IDQN under 2, 3, and 5 agents.
All methods use the same network architecture and training setup to ensure fairness. In the
2, 3, and 5-agent settings, our method achieves higher overall task success than MADDPG
and IDQN. As the number of agents grows, performance remains stable. Figures 5–8
further shows the training curves of success rate for 2-agent to 5-agent in 10,000 episodes.

## Page 22

Drones 2025, 9, 845
22 of 34
The training results for scenarios with 2, 3, and 5 agents are presented in Table 2. Unless
otherwise stated, the success rates reported in the text and tables are average team success
rates, computed as the 100-episode moving average at the end of training and summarized
as mean ± s.d. The small text boxes that appear inside some figures indicate the single
last-episode value for quick visual reference; this instantaneous value can differ from the
averaged metric we report in the text, which explains the small numerical discrepancies.
Figure 6. This combo graph shows the training curves of success rate for 2-agent in 10,000 episodes.
Figure 7. This combo graph shows the training curves of success rate for 3-agent in 10,000 episodes.

## Page 23

Drones 2025, 9, 845
23 of 34
For two agents (N = 2), our method attains an average team success rate of 84.6%
(100-episode moving average at the end of training; mean ± s.d. over 5 seeds), versus 57.4%
for MADDPG and 47.8% for IDQN, i.e., +27.2 and +36.8 percentage points.
For three agents (N = 3), our method reaches an average team success rate of 83.1% (same
metric), compared with 70.4% (MADDPG) and 58.1% (IDQN), i.e., +12.7 and +25.0 points.
For five agents (N = 5), our method achieves an average team success rate of 81.7%
(same metric), while MADDPG and IDQN obtain 68.6% and 55.7%; gains are +13.1 and
+26.0 points.
Figure 8. This combo graph shows the training curves of success rate for 5-agent in 10,000 episodes.
In all visualizations, higher softmax weight means higher information priority: the
largest inter-agent weight identifies the primary teammate for coordination at that step,
while the darkest obstacle indicates the most influential entity for immediate safety.
In Figures 5–7, the baselines rise quickly in the first ∼3k episodes and then drift
downward. Two factors explain this pattern. First, the curriculum in environmental setup
increases obstacle density once the rolling success exceeds 70%, which shifts the data
distribution from sparse to cluttered layouts and breaks the policies that have adapted
to the earlier regime. Second, off-policy value learning with replay mixes old (easy) and
new (hard) experiences, so the critic targets become non-stationary; in DDPG/DQN-style
learners, this often amplifies overestimation and causes policy chattering in dense scenes.
Seeds, Metrics, and Statistical Testing
Unless otherwise noted, we report statistics over n = 5 independent random seeds
for each method, where a seed fixes network initialization, environment randomization
(starts/buildings), and minibatch shuffling. For each seed we compute the average team
success rate as the 100-episode moving average at the end of training (Section 6.1). Group
summaries are given as mean ± s.d., together with two-sided 95% confidence intervals
(CIs) based on Student-t with n−1 degrees of freedom. Pairwise method comparisons
use Welch’s t-test (unequal variances), and we report Hedges’ g as an unbiased effect
size. For N = 2 we have full five-seed runs (Tables 4 and 5); for N = 3, 5 we currently

## Page 24

Drones 2025, 9, 845
24 of 34
report single-seed point estimates due to compute limits (replication package will include
multi-seed runs in a follow-up update).
By contrast, our approach degrades less after the curriculum switch: the atten-
tion modules yield a cleaner state representation for the critic, and the multi-objective
(task/formation/safety/energy) signals regularize updates when the environment hardens,
reducing regressions. For clarity, evaluation curves are reported with deterministic actors
(no exploration noise).
Table 4. N = 2, five-seed statistics for average team success rate (%). Mean ± s.d. and two-sided 95% CIs
(Student-t, n = 5).
Method
Mean ± s.d. (%)
95% CI (%)
Ours
84.6 ± 3.36
[80.43, 88.78]
MADDPG
57.4 ± 1.33
[55.75, 59.05]
IDQN
47.8 ± 1.93
[45.40, 50.20]
Table 5. N = 2, pairwise comparisons on average team success (%). Welch’s t-test (two-sided), with de-
grees of freedom (df), p-value, and Hedges’ g. ∆is the mean difference in percentage points (pp).
Comparison
∆(pp)
t (df)
p-Value
Hedges’ g
Ours vs. MADDPG
+27.2
16.82 (d f = 5.22)
< 10−5
9.60
Ours vs. IDQN
+36.8
21.22 (d f = 6.38)
< 10−6
12.12
Overall average team success rates after training for N ∈{2, 3, 5} are summarized in
Table 6.
Table 6. Team success rate (%) after training.
Method
N = 2
N = 3
N = 5
PA-MADDPG (ours)
84.6
83.1
81.7
MADDPG
57.4
70.4
68.6
IDQN
47.8
58.1
55.7
The superior performance of our method can be attributed to several key factors. First,
the attention mechanisms enable more effective information processing and agent coordi-
nation, leading to better formation maintenance and obstacle avoidance. The self-attention
mechanism helps agents focus on relevant state features, while inter-agent attention facili-
tates explicit coordination signals. Second, the Pareto optimization framework effectively
balances multiple objectives without requiring manual reward tuning, resulting in more
robust policies. Third, the integrated architecture creates synergistic effects between atten-
tion and multi-objective optimization, leading to emergent coordination behaviors that are
difficult to achieve with traditional methods.
6.5.2. Ablation Study on Attention Mechanisms
A systematic ablation study was conducted to validate the individual contributions of
each attention component by progressively removing mechanisms from the full framework.
This analysis quantifies the specific impact of self-attention, inter-agent attention, and entity
attention on overall system performance. Five configurations were evaluated: the complete
framework with all attention components; removal of entity attention; removal of inter-
agent attention; removal of self-attention; and a baseline without any attention mechanisms.
The detailed results are summarized in Table 7.

## Page 25

Drones 2025, 9, 845
25 of 34
Table 7. Ablation study results of attention modules. Bold entries indicate the best (most favorable)
result among all configurations for each metric.
Configuration
Success
Rate (%)
Formation
Dev. (m)
Collision
Rate (%)
Energy
Efficiency
Full Model
88.7 ± 1.8
1.47 ± 0.15
3.2 ± 0.8
0.86 ± 0.04
w/o Entity Attention
87.1 ± 2.3
1.89 ± 0.21
4.7 ± 1.1
0.81 ± 0.05
w/o Inter-Agent Attention
82.4 ± 2.8
2.15 ± 0.26
6.3 ± 1.4
0.78 ± 0.06
w/o Self-Attention
85.7 ± 2.5
1.98 ± 0.23
5.1 ± 1.2
0.79 ± 0.05
w/o All Attention
78.5 ± 2.8
2.31 ± 0.22
6.8 ± 1.2
0.74 ± 0.06
The ablation results reveal several critical insights. First, inter-agent attention demon-
strates the most significant individual impact, with its removal causing the largest per-
formance degradation (success rate dropping to 82.4%). This highlights its essential role
in maintaining coordination stability and preventing collisions. Second, entity attention
proves crucial for environmental awareness, as its absence increases collision rates and
reduces navigation efficiency. Third, self-attention contributes substantially to energy
optimization, with its removal noticeably decreasing control efficiency. Finally, the syner-
gistic effects between attention mechanisms exceed their individual contributions, enabling
emergent coordination behaviors that significantly surpass baseline capabilities.
6.5.3. Effectiveness of Pareto Multi-Objective Optimization
To validate the efficacy of Pareto multi-objective optimization, we conducted com-
parative analyses against traditional weighted-sum reward methods with various manual
weight configurations. This evaluation specifically assesses the capability to discover di-
verse high-quality trade-offs between competing objectives without manual parameter
tuning. Five baseline configurations were tested, each emphasizing different objectives as
detailed in Table 8.
Table 8.
Baseline weighted-sum reward configurations.
Notes: Safety-focused increases the
penalty/weight for collisions and near-misses while keeping task progress moderate; Task-focused
increases goal-reaching progress terms and success bonuses; Energy-focused increases control-effort
regularization and discourages actuation bursts; Formation-focused tightens slot-tracking terms and
rewards small formation RMSE; Balanced applies uniform scalarization across all objectives. All
variants share the same architecture and training schedule and differ only in reward scalarization.
Configuration
wtask
wenergy
wformation
wsafety
Safety-Focused
0.4
0.1
0.2
0.3
Task-Focused
0.5
0.2
0.2
0.1
Energy-Focused
0.3
0.4
0.2
0.1
Formation-Focused
0.3
0.1
0.5
0.1
Balanced
0.25
0.25
0.25
0.25
Quantitative results in Table 9 demonstrate that our Pareto approach achieves superior
or comparable performance across all objectives simultaneously. In contrast, weighted-sum
methods excel only in their specifically emphasized objectives while compromising others.

## Page 26

Drones 2025, 9, 845
26 of 34
Table 9. Quantitative comparison of Pareto and weighted-sum methods.
Method
Task
Success
Formation
Quality
Energy
Efficiency
Safety
Score
Overall
Score
Safety-Focused
84.2 ± 2.1
0.78 ± 0.05
0.71 ± 0.06
0.94 ± 0.02
0.82
Task-Focused
91.1 ± 1.9
0.75 ± 0.06
0.69 ± 0.07
0.83 ± 0.04
0.80
Energy-Focused
82.7 ± 2.3
0.72 ± 0.07
0.89 ± 0.03
0.81 ± 0.05
0.81
Formation-Focused
85.4 ± 2.0
0.92 ± 0.03
0.68 ± 0.08
0.79 ± 0.06
0.81
Balanced
87.3 ± 2.2
0.83 ± 0.04
0.76 ± 0.05
0.85 ± 0.03
0.83
Pareto (Ours)
88.7 ± 1.8
0.91 ± 0.04
0.86 ± 0.04
0.93 ± 0.02
0.91
The Pareto optimization approach demonstrates four key advantages. First, solu-
tion diversity enables discovery of multiple high-quality trade-offs, providing operators
with adaptable deployment options for varying mission requirements. Second, objective
balance ensures superior performance across all metrics simultaneously, avoiding the
compromise in non-emphasized objectives observed in weighted-sum methods. Third, au-
tomatic discovery eliminates domain-specific manual weight tuning that typically requires
extensive expert knowledge. Finally, adaptive optimization maintains diverse solutions
during training, guiding exploration toward promising regions of the objective space for
more effective learning.
6.5.4. Hyperparameter Sensitivity Analysis
Understanding the sensitivity of our method to key hyperparameters is essential for
practical deployment and parameter tuning. A comprehensive sensitivity analysis was
conducted on three influential parameters: attention dimension, learning rates, and Pareto
archive size. This investigation provides critical insights into the approach’s robustness
and offers practical guidance for parameter selection across diverse operational scenarios.
The analysis of learning rate combinations revealed relative robustness within reason-
able ranges, as illustrated in Figure 3. Optimal performance emerged at an actor learning
rate of 10−4 and critic learning rate of 10−3, balancing training stability with rapid conver-
gence. Higher actor rates exceeding 10−3 induced training instability, while rates below
10−5 significantly slowed convergence.
Evaluation of Pareto archive sizes between 50 and 200 demonstrated that smaller
archives limited solution diversity, while archives larger than 150 provided diminishing
returns with disproportionate computational costs. The selected size of 100 maintained 85%
of maximum diversity with only 60% of the computational overhead of larger archives.
Robustness was quantified under various noise conditions and parameter perturba-
tions, with results detailed in Table 10. Performance remained reasonable even under
substantial sensor noise (σ = 0.2) and significant parameter variations (±20% from opti-
mal values), confirming practical applicability in real-world UAV systems. Robustness
was quantified under various noise conditions and parameter perturbations, with results
detailed in Table 10.
The sensitivity analysis confirms robust performance under moderate parameter
variations while retaining sufficient sensitivity to benefit from precise tuning. Identified
optimal parameters—attention dimension 64, learning rates 10−4/10−3, archive size 100—
deliver consistent performance across scenarios. Combined with demonstrated resilience
to noise and perturbations, these characteristics establish the method’s suitability for real-
world UAV deployment.

## Page 27

Drones 2025, 9, 845
27 of 34
Table 10. Robustness evaluation under different perturbations (absolute degradation from nominal
88.7%).
Condition
Success Rate (%)
Performance Degradation (pp)
Nominal
88.7 ± 1.8
–
Sensor Noise (σ = 0.1)
85.4 ± 2.1
3.3
Sensor Noise (σ = 0.2)
82.3 ± 2.8
6.4
Learning Rate +20%
87.9 ± 2.3
0.8
Learning Rate −20%
86.5 ± 2.0
2.2
Attention Dim ±25%
85.7 ± 2.2
3.0
Archive Size ±30%
87.2 ± 1.9
1.5
The comprehensive experimental evaluation validates the effectiveness and robustness
of our attention-enhanced MADDPG framework for UAV formation control. Superior
performance across metrics, verified component contributions, and consistent operation
under diverse conditions position this approach as a promising solution for real-world
multi-agent UAV applications.
6.6. Per-Episode Trajectories and Energy Breakdown
Figure 9 visualizes representative top-down trajectories for N ∈{2, 3, 5} under our
method, MADDPG [16], and IDQN [17].
Our policy exhibits smoother turns, earlier widening before narrow corridors,
and fewer near-miss events. The most challenging maneuvers are (i) coordinated lane-
change around tall blocks with short sight lines, and (ii) concave pockets that require a
brief back-off before re-approach; both highlight the role of entity- and inter-agent attention
in prioritizing imminent threats.
Figure 9. Cont.

## Page 28

Drones 2025, 9, 845
28 of 34
Figure 9. Representative top-down trajectories comparing ours, MADDPG, and IDQN (best seed per
method; same map). Ours shows earlier widening and fewer sharp re-plans near bottlenecks.
Table 11 reports per-UAV energy proxies (mean squared control per step, normalized
to [0, 1]). Ours reduces actuation bursts during tight turns, yielding lower peak and average
control effort while maintaining formation quality. Qualitatively, this stems from stabilizing
the critic’s per-objective signals (task/formation/safety/energy) through the Pareto layer
and filtering inputs via typed attention.
Table 11. Per-UAV normalized energy proxy (mean ± s.d.; lower is better).
Team Size
Ours
MADDPG [16]
IDQN [17]
N = 2
0.86 ± 0.04
0.93 ± 0.05
0.97 ± 0.06
N = 3
0.84 ± 0.05
0.91 ± 0.05
0.95 ± 0.06
N = 5
0.83 ± 0.05
0.90 ± 0.05
0.94 ± 0.06
6.7. Robustness Under Time-Varying Networks, Packet Loss, and Interference
We evaluate trained policies under networking impairments at test time only. Packet
loss uses ploss ∈{0, 0.05, 0.10, 0.20}; random delay replays stale neighbor states with
Dmax ∈{50, 100, 150} ms; time-varying topology removes links at rate q while keeping
a KNN budget. We also add Gaussian noise to features, inject a spoofed obstacle with a
small probability, and throttle the neighbor fan-in to K′ = 2 for short windows. Metrics
include team success, collision rate, formation deviation, control energy, and decision
latency (mean/95th). We observe graceful degradation for ploss ≤0.10 and Dmax ≤100 ms,
indicating robustness to moderate networking imperfections.

## Page 29

Drones 2025, 9, 845
29 of 34
Preliminary Zero-Shot Results
Without retraining, we evaluate the trained policy under the above protocol (single
run; 100-episode moving average at the end of evaluation). Results are summarized in
Table 12.
Table 12. Zero-shot robustness under networking impairments (single run; 100-episode moving
average at end of evaluation). Note: results are from a single run; “±” denotes the standard deviation
over the last 100 episodes (moving window).
Setting
Success Rate (%)
Nominal (no loss, no delay, static topo)
88.7 ± 1.8
ploss = 0.10
79.2 ± 1.5
Dmax = 100 ms
71.2 ± 2.4
q = 1 link/s (time-varying topology)
81.6 ± 2.2
Performance decreases with stronger impairments, but remains acceptable under
moderate packet loss and delay. For instance, success drops by 9.5 pp at ploss = 0.10 and
by 7.1 pp under q = 1 link/s; the largest impact stems from Dmax = 100 ms (17.5 pp).
6.8. Interpreting Attention During Flight
We log per-branch softmax weights during a fixed evaluation rollout (seeded, no
exploration). For inter-agent attention, neighbors are re-ranked by distance at each step
to obtain a consistent y-axis (1 . . . K). Figure 10 visualizes the temporal evolution: the
inter-agent branch peaks on the most threatening teammate during collision-prone turns
and relaxes once separation is reestablished; entity attention peaks on the closest obstacle
faces in narrow passages. Figure 11 provides top-down snapshots at three timestamps that
align with the dashed markers in Figure 10. These patterns align with the intended roles
of the three branches and help explain the smooth degradation observed under moderate
networking impairments.
Figure 10. Cont.

## Page 30

Drones 2025, 9, 845
30 of 34
Figure 10. Attention dynamics during a representative flight (seeded, no exploration). Each panel
shows, from top to bottom: (i) a heatmap over time of inter-agent vs. entity attention (softmax;
colorbar in [0, 1]); (ii) attention-weight time series for the inter-agent branch and the two nearest
obstacles; (iii) spatial distances (inter-UAV, nearest obstacle) with the safety threshold for context.
Vertical dashed lines mark the timestamps visualized in Figure 11.
Figure 11. Top-down snapshots at three timestamps (left to right: t = 45, t = 150, t = 255) from the
same rollout as Figure 10. Edge thickness encodes inter-agent attention from the focal UAV, while
obstacle shading (and labels) encodes entity attention.
Edge thickness and obstacle shading are proportional to per-step information priority
from the inter-agent and entity branches, respectively.
6.9. Runtime Profiling and Scalability (N = 2–5; Analysis and Extrapolation)
We report practical runtime considerations to complement Table 1. For deployment,
only the decentralized actors run; centralized critics are used in training only. Under a fixed
neighbor/entity budget (K, M), the per-agent actor compute per step scales as O(K+M),
so the team-level decision latency grows approximately linearly in N. This is a direct conse-
quence of our typed, single-hop design that avoids stacked GNN/Transformer encoders.

## Page 31

Drones 2025, 9, 845
31 of 34
In our implementation (PyTorch, attention dimension datt = 64), we use capped K and
M and mask unavailable links. With these settings, we observed near-linear growth of de-
cision latency across the tested sizes N = 2, 3, 5 during evaluation. Extrapolating this linear
trend suggests that moderate increases in N (e.g., around 10 agents) remain compatible with
real-time control as long as (K, M) are kept bounded. Further engineering—such as batch-
ing multiple agents on a single device, mixed-precision or INT8 inference, and throttling
the neighbor fan-in under load—can reduce the slope.
Empirical wall-clock validation beyond N = 5 is left to future work due to com-
pute/time constraints; here we restrict claims to N = 2−5 and provide the above analysis
to clarify the expected scaling behavior.
6.10. Runtime and Memory Profile
All timings were measured with batch size = 1 at inference (team step), using PyTorch
2.0 on an RTX 4090 (GPU) and an i7-12700 (CPU). “Team-step latency” denotes the wall-
clock time to compute one action step for the entire team (N agents). GPU RAM is the peak
resident memory during inference.
Table 13 summarizes the runtime profile on GPU and CPU for different team sizes and
methods.
Table 13. Runtime profile (mean over 3 runs; RTX 4090/i7-12700). Team-step latency refers to one
environment step for the whole team.
N
Method
Team-Step (ms, GPU)
FPS (GPU)
GPU RAM (GB)
Team-Step (ms, CPU)
FPS (CPU)
2
Ours
0.55
1810
0.9
3.2
312
2
MADDPG
0.50
2000
0.8
2.9
345
3
Ours
0.72
1390
1.1
4.1
244
3
MADDPG
0.66
1510
1.0
3.7
270
5
Ours
1.05
950
1.4
6.8
147
5
MADDPG
0.97
1030
1.3
6.1
164
Training throughput (environment steps per second) is reported in Table 14. Despite a
small overhead introduced by the attention selector, our method remains in the millisecond
regime per team step and thus compatible with on-board execution budgets when K+M
is fixed.
Table 14. Training throughput (environment steps per second, mean ± s.d., RTX 4090).
N
Ours
MADDPG
IDQN
2
9.8k ± 0.3k
10.4k ± 0.4k
12.1k ± 0.5k
3
8.6k ± 0.2k
9.1k ± 0.3k
10.7k ± 0.4k
5
7.1k ± 0.2k
7.5k ± 0.2k
8.9k ± 0.3k
7. Conclusions
This paper proposes a unified multi-agent reinforcement learning framework that in-
tegrates hierarchical attention mechanisms with Pareto-based multi-objective optimization
to address fundamental challenges in autonomous UAV formation control within dynamic,
partially observable environments. Key theoretical contributions include a comprehensive
attention architecture combining self-attention, inter-agent attention, and entity attention,
enabling adaptive context-aware information selection; a Pareto optimization module main-
taining a compact archive of non-dominated policies that eliminates manual reward-weight
tuning while ensuring convergence; and a centralized-training-decentralized-execution
framework preserving MADDPG’s convergence guarantees with linear execution complex-

## Page 32

Drones 2025, 9, 845
32 of 34
ity scaling. Extensive experiments across N = 2, 3, 5 agents show consistent gains in team
success (by 13–27 pp over MADDPG and 25–37 pp over IDQN), alongside lower collision
rates (21–28% relative reductions) and improved formation tracking at comparable control
effort. Ablation studies confirm each attention mechanism provides unique performance
benefits, while sensitivity analyses show graceful degradation (≤7.5%) under realistic noise
and parameter perturbations.
Future research will pursue three complementary directions: conducting outdoor field
trials with heterogeneous UAVs to quantify sim-to-real transfer gaps; extending attention
mechanisms to handle dynamic communication topologies; and integrating meta-learning
for efficient policy transfer across mission types. The resulting framework provides a
generalizable foundation for large-scale multi-agent coordination in autonomous logistics,
disaster response, and distributed sensing applications.
This study is simulation-based, while this allows broad coverage of urban layouts
and controlled ablations, it cannot replace hardware-in-the-loop (HIL) or field validation.
We plan a small-scale pilot with 2–3 micro-UAVs (indoor motion capture or UWB), fol-
lowing a safety-first protocol (geofencing, emergency stop) and reporting team success,
collision count, formation RMSE, and command latency. We will also integrate a HIL loop
(e.g., PX4-SITL/ROS 2) to measure end-to-end delay from perception to actuation. These
steps are orthogonal to the proposed learning method and will be pursued once facilities are
available. A broader empirical study of stacked GNN/Transformer front ends (2–6 layers)
under the same protocol is left for future work; our codebase exposes drop-in modules so
that such baselines can be evaluated when compute and flight-test resources permit.
Also, we restricted empirical validation to N = 2−5 due to compute/time constraints.
Although the actor-side cost scales linearly in N for fixed (K, M), verifying real-time latency
for N > 10 under hardware and communication constraints is planned in future work. We
will additionally explore batched/quantized inference and adaptive neighbor throttling. We
plan to couple our low-latency control layer with a lightweight DLT-based identity/logging
service for authenticated event-level coordination, and to embed the learned Pareto-
attentive actors inside AI-driven swarm stacks for task-level autonomy. A key engineering
question is balancing ledger/security overhead with real-time constraints; our attention-
derived priority scores offer a natural throttle for when to escalate events to mission-level
consensus. A broader cross-backbone benchmark (MATD3/MASAC/MAPPO) is planned.
Author Contributions: Conceptualization, L.Z. and R.J.; methodology, L.Z.; software, L.Z.; resources
(initial environment), J.Z.; validation, L.Z. and J.Z.; formal analysis, L.Z.; investigation, L.Z.; data
curation, L.Z.; visualization, L.Z.; writing—original draft preparation, L.Z.; writing—review and
editing, R.J. and J.Z.; supervision, R.J. and L.Q.; project administration, R.J. All authors have read and
agreed to the published version of the manuscript.
Funding: This research received no external funding.
Data Availability Statement: The data are not publicly available due to manufacturer restrictions.
Sample images and code can be requested from the authors.
Acknowledgments: The authors thank Junjie Zeng for contributing the initial course-project environ-
ment upon which our multi-UAV simulation was extended, and the anonymous reviewers for their
constructive comments that helped improve this paper.
Conflicts of Interest: The authors declare no conflicts of interest.

## Page 33

Drones 2025, 9, 845
33 of 34
Abbreviations
The following abbreviations are used in this manuscript:
UAV
Unmanned Aerial Vehicle
MARL
Multi-agent reinforcement learning
MADDPG
Multi-Agent Deep Deterministic Policy Gradient
CTDE
Centralized Training with Decentralized Execution
DRL
Deep Reinforcement Learning
MPC
Model Predictive Control
MOEA
Multi-Objective Evolutionary Algorithm
RMSE
Root Mean Square Error
References
1.
Mohsan, S.A.H.; Othman, N.Q.H.; Li, Y.; Alsharif, M.H.; Khan, M.A. Unmanned aerial vehicles (UAVs): Practical aspects,
applications, open challenges, security issues, and future trends. Intell. Serv. Robot. 2023, 16, 21–29. [CrossRef] [PubMed]
2.
Chen, J.; Zhou, R.; Sun, G.; Li, Q.; Zhang, N. Distributed formation control of multiple aerial vehicles based on guidance route.
Chin. J. Aeronaut. 2023, 36, 368–381. [CrossRef]
3.
Sha, H.; Guo, R.; Zhou, J.; Zhu, X.; Ji, J.; Miao, Z. Reinforcement learning-based robust formation control for Multi-UAV systems
with switching communication topologies. Neurocomputing 2025, 611, 128591. [CrossRef]
4.
Liu, Z.; Li, J.; Shen, J.; Wang, X.; Chen, P. Leader–follower UAVs formation control based on a deep Q-network collaborative
framework. Sci. Rep. 2024, 14, 4674. [CrossRef] [PubMed]
5.
Zhen, Q.; Wan, L.; Li, Y.; Jiang, D. Formation control of a multi-AUVs system based on virtual structure and artificial potential
field on SE(3). Ocean. Eng. 2022, 253, 111148. [CrossRef]
6.
Chevet, T.; Vlad, C.; Maniu, C.S.; Zhang, Y. Decentralized MPC for UAVs Formation Deployment and Reconfiguration with
Multiple Outgoing Agents. J. Intell. Robot. Syst. 2020, 97, 155–170. [CrossRef]
7.
Yan, D.; Zhang, W.; Chen, H.; Shi, J. Robust control strategy for multi-UAVs system using MPC combined with Kalman-consensus
filter and disturbance observer. ISA Trans. 2022, 135, 35–51. [CrossRef]
8.
Hunt, S.; Meng, Q.; Hinde, C.; Huang, T. A Consensus-Based Grouping Algorithm for Multi-agent Cooperative Task Allocation
with Complex Requirements. Cogn. Comput. 2014, 6, 338–350. [CrossRef]
9.
Lizzio, F.F.; Capello, E.; Guglieri, G. A Review of Consensus-based Multi-agent UAV Implementations. J. Intell. Robot. Syst. 2022,
106, 43. [CrossRef]
10.
Saifullah, M.; Papakonstantinou, K.G.; Andriotis, C.P.; Stoffels, S.M. Multi-agent deep reinforcement learning with centralized
training and decentralized execution for transportation infrastructure management. arXiv 2024, arXiv:2401.12455v1. [CrossRef]
11.
Zhang, Y.; Zhao, W.; Wang, J.; Yuan, Y. Recent progress, challenges and future prospects of applied deep reinforcement learning:
A practical perspective in path planning. Neurocomputing 2024, 608, 20. [CrossRef]
12.
Zhang, K.; Yang, Z.; Baar, T. Multi-Agent Reinforcement Learning: A Selective Overview of Theories and Algorithms. In Handbook
of Reinforcement Learning and Control; Springer: Cham, Switzerland, 2021.
13.
Scaramuzza, D.; Kaufmann, E. Learning Agile, Vision-based Drone Flight: From Simulation to Reality. In Robotics Research;
Springer: Berlin/Heidelberg, Germany, 2023.
14.
Shahar, F.S.; Sultan, M.T.H.; Nowakowski, M.; Łukaszewicz, A. UGV–UAV Integration Advancements for Coordinated Missions:
A Review. J. Intell. Robot. Syst. 2025, 111, 69. [CrossRef]
15.
Kumar, I.; Suman, S. A Review: AI based Unmanned Aerial Vehicle (UAV) Control for Improved Autonomy, Adaptability and
Decision-Making. Int. J. Environ. Sci. 2025, 11, 171–177. [CrossRef]
16.
Lowe, R.; Wu, Y.; Tamar, A.; Harb, J.; Abbeel, P.; Mordatch, I. Multi-Agent Actor-Critic for Mixed Cooperative-Competitive
Environments. In Proceedings of the Advances in Neural Information Processing Systems (NeurIPS), Long Beach, CA, USA,
4–9 December 2017.
17.
Tampuu, A.; Matiisen, T.; Kodelja, D.; Kuzovkin, I.; Korjus, K.; Aru, J.; Aru, J.; Vicente, R. Multiagent Cooperation and
Competition with Deep Reinforcement Learning. PLoS ONE 2017, 12, e0172395. [CrossRef]
18.
Siwek, M. Consensus-Based Formation Control with Time Synchronization for a Decentralized Group of Mobile Robots. Sensors
2024, 24, 20. [CrossRef]
19.
Liu, Y.; Liu, Z.; Wang, G.; Yan, C.; Wang, X.; Huang, Z. Flexible multi-UAV formation control via integrating deep reinforcement
learning and affine transformations. Aerosp. Sci. Technol. 2025, 157, 109812. [CrossRef]
20.
Zou, Z.; Wu, Y.; Peng, L.; Wang, M.; Wang, G. Multi-UAV maritime collaborative behavior modeling based on hierarchical deep
reinforcement learning and DoDAF process mining. Aerosp. Syst. 2025, 8, 447–466. [CrossRef]

## Page 34

Drones 2025, 9, 845
34 of 34
21.
Feng, Z.; Wu, D.; Huang, M.; Yuen, C. Graph Attention-based Reinforcement Learning for Trajectory Design and Resource
Assignment in Multi-UAV Assisted Communication. IEEE Internet Things J. 2024, 11, 27421–27434. [CrossRef]
22.
Wei, Z.; Wei, R. UAV Swarm Rounding Strategy Based on Deep Reinforcement Learning Goal Consistency with Multi-Head Soft
Attention Algorithm. Drones 2024, 8, 731. [CrossRef]
23.
Jiang, F.; Xu, M.; Li, Y.; Cui, H.; Wang, R. Short-range air combat maneuver decision of UAV swarm based on multi-agent
Transformer introducing virtual objects. Eng. Appl. Artif. Intell. 2023, 123, 106358. [CrossRef]
24.
Zhang, C.; Song, J.; Tao, C.; Su, Z.; Xu, Z.; Feng, W.; Zhang, Z.; Xu, Y. Adaptive Missile Avoidance Algorithm for UAV Based on
Multi-Head Attention Mechanism and Dual Population Confrontation Game. Drones 2025, 9, 382. [CrossRef]
25.
Deb, K.; Jain, H. An Evolutionary Many-Objective Optimization Algorithm Using Reference-Point-Based Nondominated Sorting
Approach, Part I: Solving Problems with Box Constraints. IEEE Trans. Evol. Comput. 2014, 18, 577–601. [CrossRef]
26.
Jin, Y.; Feng, J.; Zhang, W. UAV Task Allocation for Hierarchical Multiobjective Optimization in Complex Conditions Using
Modified NSGA-III with Segmented Encoding. J. Shanghai Jiao Tong Univ. Sci. 2021, 26, 431–445. [CrossRef]
27.
Xiao, Y.; Yang, H.; Liu, H.; Wu, K.; Wu, G. AAV 3-D Path Planning Based on MOEA/D With Adaptive Areal Weight Adjustment.
Aerosp. Electron. Syst. IEEE Trans. 2025, 61, 753–769. [CrossRef]
28.
Ma, M.; Wang, C.; Li, Z.; Liu, F. A Proactive Resource Allocation Algorithm for UAV-Assisted V2X Communication Based on
Dynamic Multi-Objective Optimization. IEEE Commun. Lett. 2024, 28, 2814–2818. [CrossRef]
29.
Yang, Y.; Zhang, X.; Zhou, J.; Li, B.; Qin, K. Global Energy Consumption Optimization for UAV Swarm Topology Shaping.
Energies 2022, 15, 2416. [CrossRef]
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.
