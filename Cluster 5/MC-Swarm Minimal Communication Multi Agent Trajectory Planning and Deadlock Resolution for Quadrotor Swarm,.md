# MC-Swarm Minimal Communication Multi Agent Trajectory Planning and Deadlock Resolution for Quadrotor Swarm,.pdf

## Page 1

1
MC-Swarm: Minimal-Communication Multi-Agent
Trajectory Planning and Deadlock Resolution for
Quadrotor Swarm
Yunwoo Lee1 and Jungwon Park2∗
Abstract—For effective multi-agent trajectory planning, it is
important to consider lightweight communication and its po-
tential asynchrony. This paper presents a distributed trajectory
planning algorithm for a quadrotor swarm that operates asyn-
chronously and requires no communication except during the
initial planning phase. Moreover, our algorithm guarantees no
deadlock under asynchronous updates and absence of communi-
cation during flight. To effectively ensure these points, we build
two main modules: coordination state updater and trajectory
optimizer. The coordination state updater computes waypoints
for each agent toward its goal and performs subgoal optimization
while considering deadlocks, as well as safety constraints with
respect to neighbor agents and obstacles. Then, the trajectory
optimizer generates a trajectory that ensures collision avoidance
even with the asynchronous planning updates of neighboring
agents. We provide a theoretical guarantee of collision avoidance
with deadlock resolution and evaluate the effectiveness of our
method in complex simulation environments, including random
forests and narrow-gap mazes. Additionally, to reduce the total
mission time, we design a faster coordination state update using
lightweight communication. Lastly, our approach is validated
through extensive simulations and real-world experiments with
cluttered environment scenarios.
Index Terms—Path Planning for Multiple Mobile Robots,
Collision Avoidance, Distributed Robot Systems.
I. INTRODUCTION
T
HE compactness of quadrotor drones enables the oper-
ation of multi-agent systems in cluttered environments.
While small teams of drones can be manually controlled by
human pilots, large-scale swarms require autonomous coordi-
nation, where multi-agent trajectory planning (MATP) serves
as a critical component. Over the past decade, MATP has
been extensively studied, leading to its adoption in various
applications, such as surveillance [1], inspection [2], and
transportation [3].
Many existing MATP frameworks rely on synchronous
coordination, where agents repeatedly exchange information to
maintain consistency during planning and execution [4]. How-
ever, as the number of agents increases, the communication
load grows significantly, often resulting in message delays and
packet losses. These issues degrade overall performance, as
1The author is with AI Institute of Seoul National University, Seoul,
South Korea, and Carnegie Mellon University, Pittsburgh, PA, USA (e-mail:
yunwoo333@gmail.com)
2The author is with the Department of Mechanical System Design En-
gineering, Seoul National University of Science and Technology (SEOUL-
TECH), Seoul, South Korea (e-mail: jungwonpark@seoultech.ac.kr)
∗: corresponding author
Fig. 1: Demonstration of a goal-reaching mission with eight quadro-
tors in a narrow-gap environment.
agents may operate based on inconsistent or outdated informa-
tion. Without a robust and carefully engineered communication
infrastructure, maintaining synchronization becomes increas-
ingly impractical. To address these limitations, recent studies
have explored asynchronous MATP, which relaxes communi-
cation requirements by allowing agents to operate with limited
or delayed information [5]. However, most existing approaches
still depend on partial data exchange (e.g., previous planning
results), leaving them vulnerable to the same communication
limitations they aim to overcome.
In addition to the communication constraints, deadlock
resolution is another critical factor in ensuring the successful
completion of swarm tasks. Deadlocks can occur not only
from the increased number of agents but also in confined
environments, such as warehouses, where agents may block
one another’s paths and fail to reach their goals. While several
methods have been proposed to resolve deadlocks, many
either lack theoretical guarantees [6] or rely on synchronous
updates [7], making them unsuitable for large-scale [8] or
communication-constrained settings [9].
In this paper, we present MC-Swarm, an asynchronous
and distributed MATP method that ensures deadlock reso-
lution with minimal communication. The proposed frame-
work consists of two main components: coordination state
update and trajectory optimization. During the coordination
state update, each agent determines its coordination state,
which includes waypoint, subgoal, and collision constraints,
while considering deadlock resolution. Here, a waypoint is
an intermediate target on the path to the final goal, and a
subgoal is a local target that guides the agent toward the
arXiv:2505.08593v1  [cs.RO]  13 May 2025

## Page 2

2
waypoint. Based on this coordination state, each agent then
independently optimizes its trajectory toward the goal. Our
update policy ensures consistency in subgoal and waypoint
information among agents, resolves deadlocks, and enables
collision avoidance with obstacles and neighboring agents,
despite asynchronous operation and lack of communication.
Then, the trajectory of each agent is optimized towards its
goal, based on the calculated subgoals and safety constraints.
To accommodate varying communication constraints, we intro-
duce two variants of the method: a no-communication version
(MC-Swarm-N) and a lightweight communication version
(MC-Swarm-C). In the communication-free variant, agents
exchange only their start and goal positions during the initial
planning phase; no further communication is required during
the flight. In the lightweight communication variant, limited
information is shared to accelerate the coordination process
and reduce the overall mission time. The proposed method
provides theoretical guarantees of deadlock resolution and
collision avoidance. The proposed method is particularly well-
suited for goal-reaching tasks, and its effectiveness is validated
through extensive comparisons with state-of-the-art (SOTA)
approaches and real-world experiments, as shown in Fig. 1.
Table I summarizes the comparison with the SOTA algo-
rithms, and the main contributions of this paper are as follows:
• An asynchronous and distributed multi-agent trajectory
planning (MATP) strategy that eliminates the need for
communication after the initial planning phase.
• A subgoal optimization method that guarantees deadlock
resolution without communication, demonstrating supe-
rior performance in cluttered or narrow environments
where SOTA algorithms often fail.
• A trajectory optimization method that guarantees colli-
sion avoidance under asynchronous and communication-
free updates by individual agents.
• A coordination strategy that reduces total mission time
by enabling limited communication.
The structure of the remainder of this article is as follows.
Section II reviews the related literature, and the problem for-
mulation is presented in Section III. Then, Section IV explains
the methods of waypoint updates, subgoal optimization, and
collision constraints. In Section V, we present trajectory op-
timization to make drones reach subgoals while guaranteeing
the drone’s safety. Section VI describes the comparison tests
with SOTA algorithms through simulations and validates the
proposed method through hardware demonstration. Finally,
Section VII concludes this paper.
II. RELATED WORK
A. Communication-Aware MATP
Trajectory planning for multirotor UAV swarms has been
extensively studied over the past decade. Early works primarily
adopted centralized approaches [10–12], in which a central
node aggregates global information and plans trajectories for
all agents. However, these methods face scalability limitations
and impose high communication overhead, as all data must
be processed by a single point. To overcome these issues, dis-
tributed MATP methods have gained attention [13–15]. These
TABLE I: Comparison with the State-of-the-Art Algorithms.
Method
Communication settings
Theoretical guarantee
Asynch.
Com-free
Colli-Av
Dead-res
MADER [16]
✓
✕
✕
✕
EGO-v2 [18]
✓
✕
✕
✕
DREAM [20]
✓
✕
✕
△
GCBF+ [21]
✓
✓
✕
✕
RBL [22]
✓
✓
✓
△
LTL-based [23]
✕
✕
✓
✓
DLSC-GC [24]
✕
✕
✓
✓
Ours∗
✔
✔
✔
✔
{Asynch., Com-free, Colli-Av, Dead-res} are short for {Asynchronous,
Communication-free, Collision avoidance, Deadlock resolution}.
✓means that the algorithm explicitly considers the corresponding item.
△means that it considers the corresponding item, but in obstacle-free space.
∗means our no-communication-based method, MC-Swarm-N.
approaches distribute computation across agents to enhance
scalability and reduce communication load. Nevertheless, most
of them rely on synchronous updates and implicitly assume
perfect communication, which may not hold in practice.
To tackle the potential imperfections in communication,
asynchronous trajectory planning methods have been studied.
[5] and [16] compute collision-avoidance motions in a de-
centralized and asynchronous manner using a check-recheck
scheme based on a tight outer polyhedral representation
constructed with the MINVO [17] basis. [18] proposes an
MATP method that utilizes the GCOPTER [19] optimizer
by incorportating collision constraints into the optimization
cost. Although both methods can compute trajectories quickly,
they do not guarantee mission success in complex environ-
ments, as potential deadlocks are not considered. Furthermore,
inter-agent collision avoidance relies on access to the pre-
viously planned trajectories of other agents, which requires
communication. [20] introduces an asynchronous inter-robot
collision avoidance strategy based on discretized separating
hyperplane trajectories. The method involves minimal com-
munication, requiring only the exchange of trajectory start
times among agents. Although it ensures inter-agent collision
avoidance, it does not address deadlock situations. [21] enables
communication-free swarm coordination by leveraging graph
control barrier functions under the assumption that each agent
can obtain the positions of neighboring agents through onboard
sensing. Similar to the aforementioned methods, it lacks
guarantees for collision avoidance or deadlock resolution in
obstacle-rich environments.
B. Collision Avoidance and Deadlock Resolution in MATP
In the field of MATP, collision avoidance is essential, and
various methods for deadlock resolution have been studied
to ensure goal convergence. [25–27], which avoid inter-agent
collision using buffered Voronoi cells, attemp to resolve
deadlocks by applying the right-hand rule. [28] proposes a
group adaptation mechanism that divides the entire UAV group
into subgroups for better collision avoidance and deadlock
resolution, along with control strategies to prevent both in-
tergroup and intragroup collisions. [29] proposes an approach
that implicitly resolves deadlocks by leveraging global path
planning results.

## Page 3

3
Although the above methods work well in mild conditions
(e.g., sparse-obstacle environment), there has been work aimed
at theoretically guaranteeing their safe operation with a larger
number of agents and their applicability in cluttered settings.
[30] based on force-based motion planning, guarantees that
a safe distance is maintained between agents. However, in
narrow spaces, this method can cuase agents to fail to move
toward the goal and instead oscillate in place. [23] employs
a high-level mission planner that adopts the benefits of both
linear temporal logic (LTL) and a local planner to resolve
issues such as deadlock and collision. However, since the LTL-
based module is fully centralized, a synchronized communi-
cation is required. [22] is most similar to our work direction
in that it does not require synchronization or communication
between robots and provides theoretical guarantees for goal
convergence and safety. It uses the Lloyd-based algorithm [31]
to address various issues, but it does not consider collision
avoidance for obstacles or deadlock resolution taking obstacles
into account. In contrast, we guarantee both safety and goal
convergence in complex and narrow environments caused by
obstacles.
C. Comparison with the Previous Works
Over the past few years, we have proposed MATP methods
focusing on theoretical guarantee of collision avoidance (CA)
and dealock resolution (DR). The following are some of our
representative works.
• LSC [32]: guarantees CA
• DLSC [33]: guarantees CA
• DLSC-GC [24]: guarantees CA and DR
Both LSC and DLSC perform CA based on linear safe
corridors, but differ in their DR methods: LSC utilizes
higher priority-based subgoal planning, while DLSC adopts
mode-based subgoal planning. While DLSC shows supe-
rior goal convergence performance in narrow environments
such as mazes, it lacks a theoretical guarantee of deadlock-
freedom. In contrast, DLSC-GC guarantees safety using vari-
ants of safe corridors and deadlock resolution through linear
programming-based subgoal planning, but it is designed under
the assumption of perfect synchronization and communication.
In this paper, we propose the MATP algorithm, which extends
this approach to systems that operate under lightweight or even
communication-free settings, while still ensuring CA and DR.
III. PROBLEM FORMULATION
Suppose that N homogenous robots navigate in a static
obstacle environment O. Our goal is to generate safe and
deadlock-free trajectories while minimizing network commu-
nication during flight.
Throughout this paper, we will use the notation in Table
II. A calligraphic uppercase letter denotes a set (e.g., I), a
bold uppercase letter means a matrix (e.g., A), an italic letter
means a scalar value (e.g., r), and a bold lowercase letter
indicates a vector (e.g., x). The superscript with parenthesis
(e.g., x(h)) indicates the state update step of the symbol, and
the superscript will be omitted when the symbol is from the
current state update step.
TABLE II: Nomenclature
Symbol
Definition
x(h)
This superscript indicates that the symbol is
sampled or planned at the state update step h.
It is omitted if the symbol is from the current
state update step.
G = (V, E), d
Grid space (V: grid vertices, E: grid edges), grid
size d > 2
√
2r
N, I
The number of agents, set of agents I
=
{1, ⋯, N}.
pi(t), vi(t), ui(t)
Position, velocity, and control input of agent i.
vmax, umax
Agent’s maximum velocity and acceleration.
O
Space occupied by the static obstacles.
r, C
Agent’s radius, collision model.
zi, si
Desired goal and start point of agent i, respec-
tively.
h, Ts, th
Current state update step, state update period, and
time at the state update step h. th = t0 + hTs.
Tr
Maximum trajectory replanning period.
ˆpi, wi, gi
Estimated position, waypoint, subgoal of agent i,
respectively.
Si, Vi
Safe flight corridor (SFC), modified Buffered
Voronoi Cell (BVC).
M, M, T, ∆t
The number of steps to plan, M = {0, ⋯, M},
planning horizon, and planning time step. Thus,
T = M∆t.
∥x∥, ∥x∥∞, ∣πi∣
Euclidean norm, L-infinity norm, makespan of
the path πi.
0, ⊕, Conv(X),
[a, b], [p, q]
Zero vector, Minkowski sum, convex hull oper-
ator, closed scalar interval between a and b, and
line segment between two points p and q.
A. Assumption
In this paper, we make the following assumptions:
• (Obstacle and sensing) The obstacle space O is provided
as prior knowledge. Each agent can observe the positions
of other agents and static obstacles without sensing delay.
Systems equipped with ultra-wideband sensors [18] can
be candidate options capable of tracking the positions of
all agents.
• (Grid-based planner) All agents share the same grid space
G = (V, E), where the grid size d is larger than 2
√
2r
and r is the radius of the agent. The agent positioned on
the grid does not collide with static obstacles.
• (Mission) The agent’s start point and desired goal are
assigned to one of vertices of the grid space G, and
different agents have different start point and desired goal.
• (Synchronization) Each robot’s clock is synchronized
before navigation using a protocol such as Network Time
Protocol (NTP) [34].
B. Agent Dynamics
In this paper, we model agent i ∈I in double-integrator
dynamics as follows:
˙pi(t) = vi(t)
˙vi(t) = ui(t)
(1)
where pi(t), vi(t), ui(t) ∈R3 are the position, velocity, and
control input of agent i, respectively. The velocity and input
constraints are given by:
∥vi(t)∥∞< vmax, ∥ui(t)∥∞< umax, ∀t
(2)

## Page 4

4
Fig. 2: Planning process of the proposed algorithm executed by each agent
where ∥⋅∥∞is the L-infinity norm, and vmax, umax are the
agent’s maximum velocity and acceleration, respectively.
C. Collision Avoidance
1) Inter-agent collision avoidance: The necessary condi-
tion for collision avoidance between the agents i, j ∈I is
given by:
∥pi(t) −pj(t)∥≥2r,
∀t
(3)
where r is the radius of the agent.
2) Static obstacle avoidance: The necessary condition for
collision avoidance between agent i and static obstacles is
given by:
(pi(t) ⊕C) ∩O = ∅, ∀t
(4)
C = {x ∈R3 ∣∥x∥< r}
(5)
where ⊕is the Minkowski sum, O is the space occupied by the
static obstacles, and C is the sphere-shaped collision model.
D. Overview
Fig. 2 illustrates the flowchart of the proposed method,
which consists of two main modules. The first module is the
coordination state update module, responsible for synchroniz-
ing the coordination state among agents. In this work, the co-
ordination state is defined as shared information necessary for
collision avoidance and deadlock resolution, such as collision
constraints, subgoals, and waypoints.
To remove network communication during flight, each agent
first plans waypoints using a grid-based multi-agent pathfind-
ing (MAPF) algorithm (Sec. IV-A). Next, it generates a Safe
Flight Corridor (SFC) and a modified Buffered Voronoi Cell
(BVC) for collision avoidance (Secs. IV-B and IV-C). Finally,
the subgoal is optimized using the waypoints and collision
constraints to prevent deadlock (Sec. IV-D).
The second module is the trajectory planning module,
which allows each agent to asynchronously plan a safe and
deadlock-free trajectory based on the updated coordination
state (Sec. V). These modules operate independently with
different periods. Specifically, the coordination state is updated
at a fixed interval Ts, whereas the trajectory planning occurs
at random intervals, up to a maximum replanning period of
Tr. The details of each module are described in the following
sections.
Algorithm 1: Coordination state update
Input: Desired goal z∀i∈I, start time t0, and obstacle
space O
Output: Coordination state H
1 waitUntil(t0);
2 h ←0;
3 while mission is not finished do
4
ˆp∀i∈I ←detectAgentsPositions();
5
w∀i∈I ←updateWaypoints(w
(h−1)
∀i∈I , g
(h−1)
∀i∈I , z∀i∈I);
6
for ∀i ∈I do
7
Si ←buildSFC(ˆpi, g
(h−1)
i
, wi, O);
8
Vi ←buildBVC(ˆp∀i∈I, g
(h−1)
∀i∈I );
9
gi ←subgoalOpt(g
(h−1)
i
, wi, Si, Vi);
10
end
11
H ←{w∀i∈I, g∀i∈I, S∀i∈I, V∀i∈I};
12
waitUntil(th+1);
13
h ←h + 1;
14 end
IV. COORDINATION STATE UPDATE
In this paper, coordination state is defined as the shared
information among agents required for collision avoidance and
deadlock resolution. For instance, in MADER [16] and DLSC
[33], previously planned trajectories serve as the coordination
state because they are used to generate collision constraints.
Synchronizing this coordination state is essential to ensure
collision avoidance and deadlock resolution. However, many
existing methods require extensive network communication
to achieve this synchronization. To address this issue, we
introduce a coordination state update method that does not
rely on network communication during flight.
Algorithm 1 outlines the update process of the coordination
state, which consists of waypoints, subgoals, and collision
constraints. Each agent receives the agent’s desired goals and
the start time t0 as input. After the start time t0, each agent
detects the current positions of all agents and updates the
waypoints based on the previous waypoints, subgoals, and
desired goals independently (lines 4-5 of Algorithm 1, Sec.
IV-A). Next, collision constraints, such as Safe Flight Corridor
(SFC) and modified Buffered Voronoi Cell (BVC), are con-
structed using only the current positions of the agents, which
eliminates the need for inter-agent communication. (lines 7-8

## Page 5

5
of Algorithm 1, Secs. IV-B and IV-C). Subgoal optimization is
then performed using the waypoints and collision constraints
to prevent deadlocks (line 9 of Algorithm 1, Sec. IV-D).
The coordination state is updated with the new waypoints,
subgoals, and collision constraints (line 11 of Algorithm 1).
This process is repeated at the state update period Ts until the
mission is completed.
The proposed approach (MC-Swarm-N) requires network
communication only during initialization, not during flight, to
update the coordination state. Therefore, it reduces network
dependency compared to the previous works [33, 35], which
require continuous network communication to synchronize the
coordination state.
A. Waypoint Update
In this work, waypoints derived from a grid-based multi-
agent pathfinding (MAPF) are used to guide agents toward
their desired goals. Algorithm 2 presents the proposed way-
point update method. First, each agent executes the MAPF
algorithm on the grid space G (line 1 of Algorithm 2). The
start points for the MAPF are assigned to the waypoints at the
previous state update step w
(h−1)
i∈I
, and the goal points are set
to the desired goals zi∈I. If it is the first time to run the MAPF,
the start points are assigned to the agents’ current position.
In this work, we use Priority Inheritance with Backtracking
(PIBT) [36] for the MAPF algorithm because it is a fast and
scalable algorithm that guarantees goal reachability, meaning
that the agent reaches its desired goal within a finite time.
However, since PIBT is not an optimal MAPF algorithm, the
makespan of the generated path may not decrease over time,
potentially causing a livelock. To address this, we compare
the makespan of the current path π∀i∈I with the previous one
π
(h−1)
∀i∈I and use the path with the shorter makespan (lines 2-4
of Algorithm 2). Next, we update the agent’s waypoint to the
second waypoint of the path (the waypoint one step after the
start point) if the subgoals of all agents reach their respective
waypoints (lines 5-6 of Algorithm 2), i.e.:
g
(h−1)
i
= w
(h−1)
i
, ∀i ∈I
(6)
where g
(h−1)
i
and w
(h−1)
i
are the subgoal and waypoint at the
previous state update step, respectively. If this condition is not
met, we reuse the previous waypoint (lines 7-9 of Algorithm
2).
After that, we check whether the agent has the same way-
point as other agents. If two agents have the same waypoint,
one of them restores the waypoint to the previous one (lines
12-13 of Algorithm 2). This process is repeated until there are
no duplicated waypoints. Lemma 1 presents that each agent
has a different waypoint by the proposed algorithm.
Lemma 1. For the agents i ∈I and j ∈I\{i}, w
(h)
i
≠w
(h)
j
holds for every state update step h.
Proof. If h = 0, all waypoints are the second waypoints of
π∀i∈I by line 6 in Algorithm 2. Thus, the agent cannot have
the same waypoint to the other agents. Assume that there was
no duplicated waypoints at the state update step h −1. Then,
agents i and j cannot have the same waypoints at the state
Algorithm 2: Waypoints update
Input: Prev. waypoints w
(h−1)
∀i∈I , prev. subgoals g
(h−1)
∀i∈I ,
and desired goal z∀i∈I
Output: Waypoint for current state update step w∀i∈I
// Grid-based MAPF
1 π∀i∈I ←runMAPF(w
(h−1)
∀i∈I , z∀i∈I);
2 if h > 0 and ∣π
(h−1)
i
∣≤∣πi∣for ∀i ∈I then
3
π∀i∈I ←π
(h−1)
∀i∈I
4 end
// Waypoint update
5 if h = 0 or g
(h−1)
i
= w
(h−1)
i
for ∀i ∈I then
6
w∀i∈I ←second waypoint of π∀i∈I;
7 else
8
w∀i∈I ←w
(h−1)
∀i∈I ;
9 end
// Conflict resolution
10 if h > 0 then
11
for ∀i ∈I do
12
if wi = wj, ∃j ∈I\{i} then
13
wi ←w
(h−1)
i
;
14
goto line 10;
15
end
16
end
17 end
18 return w∀i∈I
update step h because the agent’s waypoint is restored to the
previous one if duplicated waypoints are detected (See lines
10-17 in Algorithm 2). Therefore, w
(h)
i
≠w
(h)
j
holds for every
state update step h by mathematical induction.
■
B. Static Obstacle Avoidance
Safe flight corridor (SFC) [37] is utilized to prevent collision
with static obstacles. SFC is defined as a convex set that
prevents the agent from a collision with static obstacles:
(S ⊕C) ∩O = ∅
(7)
where S is the SFC, C is an obstacle collision model, O is the
obstacle space, and ⊕is the Minkowski sum. In this work, we
construct the SFC as follows:
Si =
⎧⎪⎪⎪⎪⎪⎨⎪⎪⎪⎪⎪⎩
S({ˆpi, w
(0)
i })
h = 0
S({ˆpi, g
(h−1)
i
, wi})
h > 0, (9)
S({ˆpi, g
(h−1)
i
})
h > 0, else
(8)
(Conv({ˆpi, g
(h−1)
i
, wi}) ⊕C) ∩O = ∅
(9)
where Si is the SFC for agent i, S(P) is a convex set that
includes the point set P and satisfies (S(P)⊕C)∩O = ∅, ˆpi
is the estimated position of agent i and Conv(⋅) is the convex
hull operator that returns a convex hull of the input set. In this
work, S(P) is generated using the axis-search method [38].
We first initialize the SFC as the axis-aligned bounding box
that contains the point set P. Then, we expand the SFC if the

## Page 6

6
SFC is expandable in axis-aligned direction. This process is
repeated until the SFC is not expandable. Note that the SFC
in (8) always contains the line segment between two points ˆpi
and g
(h−1)
i
. Therefore, the SFC does not block the agent when
it tries to converge to the subgoal.
C. Inter-Agent Collision Avoidance
Buffered Voronoi cell (BVC) [39] is utilized for inter-agent
collision avoidance. Original BVC is defined as a half-space
that satisfies the following conditions:
¯Vi = {x ∈R3 ∣(x −ˆpj) ⋅ni,j −di,j ≥0, ∀j ≠i}
(10a)
ni,j =
ˆpi −ˆpj
∥ˆpi −ˆpj∥
(10b)
di,j = r + 1
2∥ˆpi −ˆpj∥
(10c)
where ¯Vi is the BVC, and r is the agent’s radius. In this paper,
we modify the BVC, similar to [35], to enable the agents to
converge to the subgoal more quickly:
Vi = {x ∈R3 ∣(x −cj,i) ⋅ni,j −di,j ≥0, ∀j ≠i}
(11a)
ni,j =
ci,j −cj,i
∥ci,j −cj,i∥
(11b)
di,j = r + 1
2∥ci,j −cj,i∥
(11c)
where Vi is the modified BVC, ci,j is the point on the
line segment [ˆpi, g
(h−1)
i
] that is closest to the line segment
[ˆpj, g
(h−1)
j
], and [a, b] is the line segment between two points
a and b. Similar to the SFC, modified BVC includes the
line segment between ˆpi and g
(h−1)
i
, as shown in Fig. 3.
Therefore, each agent can converge to its subgoal without
being obstructed by collision constraints. Lemma 2 shows that
the modified BVC guarantees collision avoidance between the
agents.
Lemma 2. If pi ∈Vi, pj ∈Vj, then ∥pi −pj∥≥2r.
Proof. Since pi ∈Vi, pj ∈Vj, we have the following
inequalities by adding (11a) for the agents i, j:
(pi −cj,i) ⋅ni,j + (pj −ci,j) ⋅nj,i
−(di,j + dj,i) ≥0
(12)
This can be simplified using ni,j = −nj,i, (11b), and (11c):
(pi −pj) ⋅ni,j + (ci,j −cj,i) ⋅ni,j
−(di,j + dj,i) ≥0,
(13a)
(pi −pj) ⋅ni,j ≥2r
(13b)
Therefore, ∥pi −pj∥≥(pi −pj) ⋅ni,j ≥2r holds by
Cauchy–Schwarz inequality.
■
D. Subgoal Optimization
A subgoal is an intermediate target point that allows agents
to follow their waypoints without causing deadlock. One sim-
ple way to determine a subgoal is to assign the waypoint as a
subgoal directly. However, this approach may lead to deadlock
because agents can be blocked by collision constraints before
Fig. 3: Collision constraints used in the proposed algorithm. The
triangles are estimated positions, and the circles are subgoals at the
previous state update step. The gray region represents static obstacles,
and the color-shaded regions denote the feasible region that satisfies
all collision constraints.
reaching the subgoal. To address this issue, we introduce
a subgoal optimization method that preemptively prevents
deadlock. First, we compute a feasible region for the agent
that satisfies all collision constraints. Next, we find the subgoal
closest to the waypoint within this feasible region and on the
grid. More precisely, the subgoal is determined by solving the
following optimization problem:
minimize
gi
∥gi −wi∥
subject to
gi ∈[si, wi]
if h = 0
gi ∈[g
(h−1)
i
, wi]
if h > 0
gi ∈Si ∩Vi
(14)
where gi is the subgoal, wi is the waypoint, si is the start
point of agent i, and [⋅, ⋅] represents a line segment connecting
two points. Lemmas 3 and 4 show the key properties of the
proposed subgoal optimization. Lemma 3 demonstrates that
the subgoal and waypoint are always on the same grid edge,
and Lemma 4 indicates that the subgoals of two agents cannot
be on the middle of the same grid edge.
Lemma 3. gi, g
(h−1)
i
, and wi are always on the same grid
edge e ∈E.
Proof. If h = 0, si and wi(t0) are on the same grid edge
because si is on the grid vertex by the assumption and si and
wi(t0) are the consecutive waypoints of the path generated
by the grid-based MAPF. Since gi(t0) ∈[si, wi(t0)] holds
by the constraint of (14), gi(t0) and wi(t0) are on the same
grid edge.
Assume that g
(h−1)
i
and w
(h−1)
i
are on the same grid edge.
If g
(h−1)
i
≠w
(h−1)
i
, then wi = w
(h−1)
i
holds by the waypoint
update rule (6). Thus, we obtain [gi, wi] ⊂[g
(h−1)
i
, wi] =
[g
(h−1)
i
, w
(h−1)
i
] by the constraint in (14). It implies that gi,
g
(h−1)
i
, and wi are on the same grid edge. If g
(h−1)
i
= w
(h−1)
i
,
then we have [gi, wi] ⊂[g
(h−1)
i
, wi] = [w
(h−1)
i
, wi]. Since
w
(h−1)
i
and wi are the consecutive waypoints of the path
generated by the grid-based MAPF, gi, g
(h−1)
i
, and wi are on
the same grid edge. Thus, Lemma 3 holds by mathematical
induction.
■

## Page 7

7
(a) t = ti
(b) Naive method, t = tj
(c) Proposed method, t = tj
Fig. 4: Comparison of trajectory planning when using the most recent collision constraint (naive method) and the conservative constraint
(proposed method). The color-shared region represent collision constraint used for trajectory planning, and ti and tj are time when agents
i and j update their trajectory, respectively.
Lemma 4. If gi and gj are on the same grid edge e ∈E, then
gi or gj must be on the vertex of the grid.
Proof. Assume that both gi and gj are not on the vertex of the
grid. Then, there exists the replanning step hi ≤hj < h that
satisfies w
(hi)
i
≠w
(hi+1)
i
= ⋯= w
(h)
i
and w
(hj)
j
≠w
(hj+1)
j
=
⋯= w
(h)
j
without loss of generality. Here, we can observe
that gi ∈[w
(hi)
i
, w
(hi+1)
i
] and gj ∈[w
(hj)
j
, w
(hj+1)
j
] due to
the waypoint update rule (6).
If
hi
=
hj,
then
we
have
[w
(hi)
i
, w
(hi+1)
i
]
=
[w
(hi)
j
, w
(hi+1)
j
] because gi and gj are on the same grid edge,
but not on the vertex of the grid. However, it is impossible be-
cause the path generated from MAPF algorithm does not cause
collision. If hi < hj, then [w
(hi)
i
, w
(hi+1)
i
] = [w
(hj)
j
, w
(hj+1)
j
]
holds because gi and gj are on the same grid edge, but not on
the vertex of the grid. It implies that w
(hi+1)
i
= w
(hj)
i
= w
(hj)
j
or w
(hi+1)
i
= w
(hj+1)
i
= w
(hj+1)
j
. However, both of them are
impossible due to Lemma 1. Therefore, gi or gj must be on
the vertex of the grid.
■
The proposed subgoal optimization method offers two main
advantages. First, it ensures that each agent can reach its
subgoal because the path to the subgoal cannot be blocked by
collision constraints. Second, it prevents agents from blocking
each other since it assigns the subgoal to a unique grid
edge. Additionally, the proposed subgoal optimization method
does not cause optimization failure because g
(h−1)
i
satisfies all
constraints of (14).
V. TRAJECTORY PLANNING
A. Trajectory Optimization
Based on the coordination state, each agent plans its trajec-
tory asynchronously. Even if agents share the same coordina-
tion states, it is challenging to guarantee collision avoidance
without network communication because agents cannot know
when other agents will plan their trajectories. For instance,
assume that agents i and j update their trajectories at time ti
and tj (ti ≤tj), respectively . If the agents only use the most
recent collision constraint when planning their trajectories, a
collision may occur because there exists a region that both
agents consider safe as shown in Fig. 4b.
To address this issue, we introduce conservative collision
constraints, inspired by discretized separating hyperplane tra-
jectories (DSHT) [20, 40]. Suppose that the maximum tra-
jectory replanning period is given by Tr. To avoid collision,
we plan the trajectory using the collision constraint generated
from time t −Tr −Ts to t, where t is the current time and
Ts is state update period. This ensures collision avoidance
because the agents share at least one collision constraint,
as shown in Fig. 4c. This approach is similar to DSHT in
using conservative collision constraints, but DSHT requires
continuous network communication to update the constraints,
whereas the proposed method does not.
For trajectory optimization, we formulate the cost functions
to minimize the distance to the subgoal and the acceleration
of the trajectory. The trajectory must satisfy the input and
velocity constraints for dynamical feasibility, and the agent
should stop at the end of planning horizon to prevent collision
in case of optimization failure. To summarize, the trajectory
optimization problem for agent i at time t is formulated as the
following quadratic programming (QP) problem:
min
ui,k
Ji(ui,k)
s.t.
xi,k+1 = Axi,k + Bui,k
∀k ∈{0, ⋯, M −1}
pi,k ∈S
(h)
i
∩V
(h)
i
∀k ∈M, ∀h s.t.
th ∈[t −Tr −Ts, t]
∥vi,k∥∞< vmax
∀k ∈M
∥ui,k∥∞< umax
∀k ∈M
vi,M = 0
(15)
Ji(ui,k) = we∥pi,M −g
(hl)
i
∥2 + wa
M−1
∑
k=0
∥ui,k∥2
(16)
where Ji is the cost function, xi,k = [pT
i,k, vT
i,k]T , pi,k, vi,k,
and ui,k are the state, position, velocity, and control input
of agent i at time step k, respectively. M is the number of
steps to plan, M = {0, ⋯, M}, Tr is the maximum replanning
period, Ts is the state update period, and S
(h)
i
and V
(h)
i
are
the SFC and the modified BVC at the state update step h,
respectively. A and B are matrices that represents the agent
dynamics (1), 0 ∈R3 is the zero vector, vmax and umax are
the agent’s maximum velocity and acceleration, respectively.
hl is the latest state update step, and we, wa > 0 are the
weight coefficients. This problem can be solved by using a
conventional convex solver.
Similar to original BVC [39], the proposed algorithm may
cause optimization failure due to infeasible constraints. In such
cases, the agent follows the previously planned trajectory. We

## Page 8

8
note that the proposed algorithm ensures collision avoidance
regardless of optimization failure, thanks to the final stop
constraint (vi,M = 0) (Please refer to Theorem 2).
B. Theoretical Guarantee
This section describes the theoretical guarantee of the
proposed method. We will denote the planning horizon of
trajectory optimization problem (15) by T and the planning
time step by ∆t. Hence, T = M∆t holds.
1) Collision avoidance: Theorem 1 shows the sufficient
condition for collision avoidance of the proposed algorithm.
Theorem 1. If the trajectory replanning period is less than the
maximum replanning period Tr and there is no optimization
failure, then the agents do not collide with other agents or
static obstacles.
Proof. (Static obstacle avoidance) There exists the state update
step h∗that satisfies th ∈[t−Tr −Ts, t] because the length of
the interval is equal to or greater than the state update period
Ts. Therefore, (pi,k ⊕C) ∩O ⊂(S
(h∗)
i
⊕C) ∩O = ∅holds
for ∀i ∈I, k ∈M due to the constraint of (15). Thus, all
agents do not collide with static obstacles by (4).
(Inter-agent collision avoidance) Suppose that the latest
trajectory planning time of the agents i and j are ti and
tj, respectively, and ti
≤tj without loss of generality.
Then, tj −ti < Tr holds because the replanning period is
less than Tr. Assume that the state update step h∗satisfies
th∗∈[ti −Ts, ti]. Note that such state update step must exist
since the length of the interval [ti −Ts, ti] is equal to the
state update period Ts. Then, we obtain th∗∈[ti −Ts, ti] ⊂
[tj −Tr−Ts, ti] = [ti−Tr−Ts, ti]∩[tj −Tr−Ts, tj] because
tj −ti < Tr. This means that pi,k ∈V
(h∗)
i
and pj,k ∈V
(h∗)
j
holds for ∀k ∈M due to the constraint of (15). Thus, there
is no collision between agents by Lemma 2.
■
Moreover, the proposed algorithm guarantees collision
avoidance regardless of the optimization failure if the planning
horizon is less than the maximum replanning period.
Theorem 2. If the planning horizon T and trajectory replan-
ning period are less than the maximum replanning period
Tr, then the agents do not cause collision regardless of the
optimization failure.
Proof. Despite of optimization failure, the agents do not
collide with static obstacles because the previously planned
trajectories do not collide with static obstacles. Suppose that
the latest trajectory planning time of the agents i and j are ti
and tj, respectively, and ti ≤tj without loss of generality.
(Case 1) If tj −ti < T, then there exists the state update
step h∗that satisfies th∗∈[ti −Ts, ti]. Therefore, we obtain
th∗∈[ti −Ts, ti] ⊂[tj −Tr −Ts, ti] = [ti −Tr −Ts, ti] ∩
[tj −Tr −Ts, tj] because tj −ti < T < Tr. This means that
pi,k ∈V
(h∗)
i
and pj,k ∈V
(h∗)
j
holds for ∀k ∈M due to the
constraint of (15). Thus, there is no collision between agents
by Lemma 2.
(Case 2) If tj −ti ≥T, then agent i stops at pi,M due to
the constraint (vi,M = 0) in (15). Here, we can observe that
pi,M ∈V
(h)
i
holds for ∀h such that th > ti + T because
pi,M = ˆp
(h)
i
∈V
(h)
i
if th > ti + T. This implies that there
exists the state update step h∗that satisfies pi,M ∈V
(h∗)
i
and
pj,k ∈V
(h∗)
j
for ∀k ∈M. Thus, there is no collision between
agents by Lemma 2.
■
2) Deadlock resolution: We define agent i to be in a
deadlock if it remains stationary at its current position and
does not reach its target, i.e.:
pi(t) = pi(td) ≠zi, ∀t > td
(17)
where td is the time when the deadlock starts. Lemmas 5 and
6 present the sufficient condition for subgoal convergence and
deadlock resolution of the proposed algorithm, respectively.
Lemma 5. If the mission is solvable for the grid-based MAPF,
there exists a state update step hd such that gi converges to
g
(hd)
i
for ∀i ∈I.
Proof. Assume that there does not exist a state update step
hd such that g
(h)
i
converges to g
(hd)
i
. Then, gi converges to
wi because the cost function of the subgoal optimization (14),
∥gi−wi∥, is strictly decreasing over time due to the constraint
gi
∈[g
(h−1)
i
, wi]. Moreover, wi converges to a specific
point because we only use the path πi whose makespan is
monotonically decreasing when we update the waypoint (See
lines 2-4 of Algorithm 2). Therefore, gi converges to a specific
point, which contradicts the assumption. Thus, there must
exists a state update step hd such that gi converges to g
(hd)
i
for ∀i ∈I.
■
Lemma 6. If there exists agent i that satisfies ˆpi ≠gi, then
the proposed algorithm does not cause deadlock.
Proof. If deadlock occurs, then the position and subgoal of
the agents are converged to specific points by the definition of
deadlock and Lemma 5. Assume that ˆpi and gi converge to
pi,d and gi,d after time td, respectively, and pi,d ≠gi,d. Then,
the optimal solution of (15), u∗
i,k, must satisfy u∗
i,k = 0 for
∀k ∈M after time td.
Let us define the following control input ˜ui,k:
˜ui,k =
⎧⎪⎪⎪⎪⎨⎪⎪⎪⎪⎩
λni,d
k = 0
−λni,d
k = 1
0
k > 1
(18)
ni,d =
gi,d −pi,d
∥gi,d −pi,d∥
(19)
where λ > 0. We can prove that ˜ui,k is one of feasible
solutions of the trajectory optimization problem (15) if λ is
small enough. First, [pi,d, gi,d] = [ˆp
(h)
i
, g
(h)
i
] ∈S
(h)
i
∩V
(h)
i
holds for all h such that th > td. Therefore, ˜ui,k satisfies the
collision avoidance constraint since the trajectory is always on
the line segment [pi,d, gi,d]. Second, ˜ui,k satisfies the velocity
and input constraints if λ < umax and λ∆t < vmax. Third,
˜ui,k satisfies the final stop constraint since the agent follows
double-integrator dynamics. Thus, ˜ui,k is a feasible solution
of (15) if λ < umax and λ < vmax/∆t.

## Page 9

9
The cost difference between u∗
i,k and ˜ui,k is given by:
Ji(u∗
i,k) −Ji(˜ui,k)
= wed2
i −we(di −λ∆t2)2 −wa(2λ2)
= we(2diλ∆t2 −λ2∆t4) −wa(2λ2)
= (2wedi∆t2)λ −(we∆t4 + 2wa)λ2
= aλ −bλ2
(20)
where di
=
∥gi,d −pi,d∥, a
=
2wedi∆t2
>
0, and
b = we∆t4 + 2wa > 0. If 0 < λ < a/b, we obtain
Ji(u∗
i,k)−Ji(˜ui,k) > 0. Therefore, u∗
i,k = 0 is not the optimal
solution, which contradicts the assumption that ˆpi converges
to pi,d where pi,d ≠gi,d. Therefore, the proposed algorithm
does not cause deadlock if there exists agent i that satisfies
ˆpi ≠gi.
■
Using Lemmas 5 and 6, we can prove that the proposed
algorithm guarantees deadlock resolution.
Theorem 3. If the mission is solvable for the grid-based
MAPF and d > 2
√
2r, then the proposed algorithm does not
cause deadlock.
Proof. Assume that the proposed algorithm causes deadlock
after time td. Then, the agents satisfy the following condition
by Lemmas 5 and 6:
ˆp
(h)
i
= g
(h)
i
= g
(hd)
i
∀i ∈I, ∀h > hd
(21)
where hd is the state update step when deadlock happens.
The subgoal optimization problem (14) of agent i ∈I can be
reformulated as follows:
minimize
δ
subject to
δ ∈[0, 1]
wi + δ(g
(h−1)
i
−wi) ∈Si ∩Vi
(22)
where δ is a variable such that gi = wi + δ(g
(h−1)
i
−wi).
By (21), we have Conv({ˆpi, g
(h−1)
i
, wi}) = [g
(h−1)
i
, wi]. This
implies that the condition (9) is satisfied because g
(h−1)
i
and
wi are always on the same grid edge by Lemma 3 and this grid
edge does not collide with static obstacles. Therefore, the SFC
constraint in (22) can be omitted since gi ∈[g
(h−1)
i
, wi] ⊂Si.
Accordingly, the Lagrangian function of (22) for agent i ∈I
is formulated as follows:
L = δ −λ0δ + λ1(δ −1)
+
∑
j∈I\{i}
λi,j(di,j −(wi + δ(g
(h−1)
i
−wi) −cj,i) ⋅ni,j)
(23)
where λ0, λ1, and λi,j are the Lagrangian multipliers. The
stationary condition of KKT conditions [41] is given by:
∂L
∂δ = 1 −λ0 + λ1 −
∑
j∈I\{i}
λi,j(g
(h−1)
i
−wi) ⋅ni,j = 0 (24)
If h > hd, then δ∗= 1 is the optimal solution of the subgoal
optimization problem (22) due to (21). Therefore, λ0 = 0 holds
by the complementary slackness condition of KKT conditions.
Fig. 5: Example of blocking agents. The square dots, circle dots,
and color-shaded regions represent waypoints, subgoals, and agents’
feasible regions, respectively.
Moreover, we have g
(h−1)
i
= gi, ci,j = gi, and cj,i = gj due
to (21). Thus, we can simplify (24) as follows:
∑
j∈I\{i}
λi,j
(gj −gi)T (wi −gi)
∥gi −gj∥
= 1 + λ1
(25)
To fulfill the above condition, there must exist an agent j ∈
I\{i} that satisfies λi,j > 0 and (gj −gi)T (wi −gi) > 0
because λ1 ≥0 and λi,j ≥0 by the dual feasibility of KKT
conditions. Furthermore, λi,j > 0 implies that the following
equations hold due to the complementary slackness of KKT
conditions:
di,j −(wi + (g
(h−1)
i
−wi) −cj,i) ⋅ni,j = 0
(26)
r + 1
2∥gi −gj∥−(wi +(gi −wi)−gj)⋅
gi −gj
∥gi −gj∥= 0 (27)
∥gi −gj∥= 2r
(28)
To summarize, if the proposed algorithm causes deadlock
after time td, there must exist an agent j that satisfies the
following conditions for each agent i ∈I:
(gj −gi)T (wi −gi) > 0
(29)
∥gi −gj∥= 2r
(30)
Let us define agent B(i) ∈I that satisfies (29) and (30) as
a blocking agent of agent i, where B(⋅) indicates the blocking
agent of the given agent. Fig. 5 illustrates the example of the
blocking agent. In the figure, the yellow agent is the blocking
agent of the red agent because the yellow agent prevents the
red agent from reaching the waypoint w1. Similarly, the green
agent is the blocking agent of the yellow agent, and the blue
agent is the blocking agent of the green agent.
Since there are a finite number of agents in I, there must
exist an agent q ∈I that satisfies the following:
∆(q) ≥∆(i), ∀i ∈I
(31)
where ∆(i) = ∥wi −gi∥. As discussed earlier, agent q must
have its blocking agent B(q) ∈I, and gq and gB(q) must be

## Page 10

10
on different grid edges by Lemma 4. Therefore, ∆(B(q)) is
given by:
∆(B(q)) = { d −2r + ∆(q),
if D > 0
d −
√
4r2 −∆(q)2,
else
(32)
where D is defined as follows:
D = (wB(q) −gB(q))T (wq −gq)
(33)
If d > 2
√
2r, we obtain ∆(B(q)) > ∆(q), which contradicts
the assumption that agent q satisfies (31). Therefore, at least
one agent does not have a blocking agent, ensuring that the
proposed algorithm does not cause a deadlock.
■
C. Enhancing Waypoint Update Speed via Communication
The communication-free method (MC-Swarm-N) requires
that, for waypoint updates, agents often wait until all agents’
subgoals have reached their waypoints, which may increase
the overall flight time. To mitigate this issue, Algorithm 3
introduces a faster waypoint update method using minimal
communication. Each agent locally identifies which agents’
subgoals have reached the waypoint. The algorithm then
updates the waypoint only for agents that all agents agree
have reached their respective waypoints, whereas Algorithm 2
pauses the update until all subgoals of agents arrive at their
waypoints.
To elaborate, each agent communicates a set of agent indices
ei indicating which agents it observes to have reached their
respective waypoints. The intersection of these sets across all
agents, es = ⋂i∈I ei, identifies the agents for which all peers
agree that the subgoals have been reached (line 2 of Algorithm
3). Only the agents whose indices belong to es proceed to
update their waypoints, while the remaining agents retain their
current subgoals (lines 7–13 of Algorithm 3).
For example, suppose I = {1, 2, 3}, and agent 1, 2, and 3
perceive that the subgoals of agents {1, 2, 3}, {1, 2}, and {2, 3}
have arrived at their waypoints, respectively: e1 = {1, 2, 3},
e2 = {1, 2}, and e3 = {2, 3}. In this case, only the waypoint
of agent 2 is updated since all agents agree that the subgoal
of agent 2 has reached its waypoint: es = {2}. This approach
maintains consistency across agents while significantly reduc-
ing communication overhead. Moreover, this accelerates the
waypoint update speed because agents do not need to wait
until all agents’ subgoals reach their waypoint, reducing the
total flight time. The planner that uses Algorithm 3 instead of
Algorithm 2 is referred to as MC-Swarm-C.
D. Estimation Error Handling
Our system requires all agents to detect the positions of
other agents, which makes the proposed algorithm naturally
subject to state estimation errors. To mitigate the possible
negative effects on safety due to the errors, we incorporated an
additional safety margin into the agent’s collision model. This
safety margin is determined based on the maximum tracking
error observed during preliminary experiments measuring the
quadrotor’s tracking error. Specifically, in the validation, we
employ quadrotors with a 7.5 cm radius, corresponding to the
size of Crazyflie 2.1 quadrotors, but their radii are regarded
as 15 cm in the algorithm.
Algorithm 3: Waypoints update (communication ver.)
Input: Prev. waypoints w
(h−1)
∀i∈I , prev. subgoals g
(h−1)
∀i∈I ,
e∀i∈I, and desired goal z∀i∈I
Output: Waypoint for current state update step w∀i∈I
// Grid-based MAPF
1 do lines 1-4 in Algorithm 2
2 es ←CheckMutualIndex(e∀i∈I)
// Waypoint update (modified)
3 if h=0 then
4
w∀i∈I ←second waypoint of π∀i∈I;
5
goto line 14
6 end
7 for j = 1 to N do
8
if h = 0 or j ∈es then
9
wj ←second waypoint of πj;
10
else
11
wj ←w
(h−1)
j
;
12
end
13 end
// Conflict resolution
14 do lines 10-17 in Algorithm 2.
15 return w∀i∈I
VI. VALIDATION
In this section, the proposed method is validated through
both simulations and hardware experiments. For simulations,
tests are run with 30 different scenarios for each number of
agents, varying the map configuration and the agents’ initial
positions. We then measure the success rate, total flight time,
and computation time per agent. The performance of the
proposed algorithms are investigated by comparing it with the
following state-of-the-art asynchronous MATP algorithms.
• MADER [5]: Collision check-recheck-based
• EGO-v2 [18]: Gradient-based optimization-based
• DREAM [20]: Separating hyper-plane trajectory-based
• GCBF+ [21]: Graph neural network-based
We evaluate the performance of both proposed methods,
described as follows:
• MC-Swarm-N: Communication-free-based (waypoint up-
date using Algorithm 2),
• MC-Swarm-C: Commnucation-based (waypoint update
using Algorithm 3).
For parameters, we set the collision model of the agent with
radius r∀i = 0.15 m, and the maximum axis-wise velocity
and acceleration of the agents are vmax = 1.0 m/s and
amax = 5.0 m/s2, respectively. The update parameters, such
as the state update period, maximum replanning period, and
planning period, used in validation are set as Ts = 0.02 s,
Tr = 0.2 s, and ∆th = 0.1 s. For the MAPF algorithm, the
grid resolution d is set to 0.5 m. For trajectory optimization,
we set the planning horizon T = 1.0 s, with the number of
steps M = 5 and time step ∆t = 0.2 s, and the weight
parameters in the cost (16) are set as we = 0.01 and wg = 0.1.
In the implementation, Octomap [42] is used to represent the
obstacle environment, and the IBM CPLEX QP solver [43]

## Page 11

11
Fig. 6: Simulation result in empty space. Spheres, splines, and
shaded regions represent agents, whole flying paths, and collision-
free regions, respectively.
TABLE III: Simulation results in empty spaces.
N
Method
Success rate [%]
Flight time [s]
Runtime [ms]
5
DREAM
100
4.77
2.59
MC-Swarm-N
100
4.33
2.27
MC-Swarm-C
100
4.82
2.25
10
DREAM
100
6.76
5.30
MC-Swarm-N
100
7.12
3.73
MC-Swarm-C
100
6.52
3.43
15
DREAM
93.3
11.3
22.5
MC-Swarm-N
100
8.63
5.07
MC-Swarm-C
100
7.36
5.63
20
DREAM
70.0
12.79
34.1
MC-Swarm-N
100
10.8
7.23
MC-Swarm-C
100
7.97
9.62
The bold number indicates the best result.
is used for trajectory optimization. We use a laptop with an
Intel i7-10750H CPU for simulations and an Intel NUC with
an i7-1260P CPU for experiments, respectively.
A. Simulation in Obstacle-Free Space
We conduct the simulations with 5 to 20 agents in a 3×3×1
m3 obstacle-free space. We execute 30 trials for each number
of agents, randomly assigning start and goal points for each
test. Fig. 6 shows the simulation result carried out by MC-
Swarm-N, and Table III summarizes the result. Our methods
successfully accomplish the mission, whereas DREAM fails
to complete it due to a deadlock that occurs as the number of
agents increases. Additionally, although MC-Swarm-C takes
more time than MC-Swarm-N to complete the mission with
5 agents, it becomes faster as the number of agents increases,
with the time difference growing more significant.
B. Simulation in Obstacle Space
We perform goal-reaching simulations in two types of
obstacle environments. First, we test our algorithm in random
forests. Forty box-shaped obstacles are deployed in random
positions, and all agents are on a circle with 4 m radius
at initial time, as shown in Fig. 7a. Then, all agents are
commanded to move to their goal points, which are antipodal
to their start points. Second, we conduct the test in a narrow-
gap maze. With a maze environment in the center, all agents
start from the left and right sides and exit through the opposite
side, as shown in Fig. 7b. There is only one entrance on each
side of the maze, and the path to their destinations is unique.
Only a single agent can pass through the corridor at a time.
Fig. 7 illustrates the simulation results conducted using MC-
Swarm-N, while Table IV provides a summary of the results.
(a) Random forest
(b) Narrow maze
Fig. 7: Simulations in 3D obstacle environments using MC-Swarm-N
(top: top-down view, bottom: side view). Splines and spheres show
the reported trajectories and agents, respectively.
(a) Random forest
(b) Narrow maze
Fig. 8: Simulations in 2D obstacle environments using MC-Swarm-
N. Splines and spheres show the reported trajectories and agents,
respectively.
TABLE IV: Simulation results in 3D obstacle spaces.
Method
Success rate [%]
Flight time [s]
Runtime [ms]
Forest
GCBF+
0.00
-
-
MADER
43.3
19.5
226
EGO-v2
83.3
14.5
5.19
MC-Swarm-N
100
26.9
2.61
MC-Swarm-C
100
19.7
2.81
Maze
GCBF+
0.00
-
-
MADER
0.00
-
-
EGO-v2
0.00
-
-
MC-Swarm-N
100
65.9
3.04
MC-Swarm-C
100
36.7
2.86
The bold number indicates the best result.
TABLE V: Simulation results in 2D obstacle spaces.
Method
Success rate [%]
Flight time [s]
Runtime [ms]
Forest
GCBF+
0.00
-
-
MC-Swarm-N
100
33.3
2.00
MC-Swarm-C
100
23.5
2.08
Maze
GCBF+
0.00
-
-
MC-Swarm-N
100
99.9
3.17
MC-Swarm-C
100
63.0
2.14
The bold number indicates the best result.
GCBF+ failed to reach the goal in both environments as the
agents got stuck between obstacles. While MADER and EGO-
Swarm succeeded in some cases in the forest environment with
short total flight time, they failed in all cases in the maze
environments, which are significantly denser. On the other
hand, the proposed methods achieve a 100% success rate by
resolving deadlocks.
Additionally, we test the planner in 2D spaces with the same
obstacle layout as in the 3D spaces, making the scenarios more

## Page 12

12
Fig. 9: Hardware demonstration setup.
(a) Third person view (t = 10 s)
(b) Flight history, (t = 38.2 s)
Fig. 10: Real-world experiments using the no-communication method
(MC-Swarm-N) with eight quadrotors. (a): Snapshots of flight at t =
10 s. (b): Reported flight paths and snapshots at the end time.
(a) Third person view (t = 10 s)
(b) Flight history, (t = 24.9 s)
Fig. 11: Real-world experiments using the communication-based
(MC-Swarm-C) with eight quadrotors. (a): Snapshots of flight at
t = 10 s. (b): Reported flight paths and snapshots at the end time.
challenging than the 3D cases, as feasible motions must be
found within the x–y plane. Fig. 8 and Table V summarize
the simulation results, and only our methods succeeds in the
tasks without any failure.
C. Experiments
For hardware demonstration, we set up a validation system,
as shown in Fig. 9. Eight Crazyflie [44] quadrotors are
employed, each of which communicates with and is controlled
by a separate Intel NUC computer. Also, an additional laptop is
used to receive data from the Optitrack motion capture system,
and the positional data of the quadrotors is asynchronously
transferred to the computers via a router.
In the demonstration, we allow the drones to move within
an 8 × 5 m2 2D space, where eight 1 × 1 m2 box-shaped
obstacles are arranged to form a narrow-gap maze. Each
agent is assigned to reach a goal point that is symmetric to
the start point with respect to the origin, passing through a
0.5 m gap. Through experiments, we show successful goal-
reaching scenarios, and Table VI, Figs. 10 and 11 summarize
TABLE VI: Reported results in hardware experiments
Method
MC-Swarm-N
MC-Swarm-C
Flight time [s]
38.2
24.9
Runtime [ms]
2.18
2.25
The bold number indicates the best result.
the flights. Fig. 10 shows the result with MC-Swarm-N, while
Fig. 11 presents the result with MC-Swarm-C. Figs. 10a and
11a show snapshots 10 seconds after the start of the flight.
Unlike the communication-free method, the communication-
based method’s faster update speed allows the agents to exit
the confined space earlier and move closer to the destination at
the same time. Ultimately, the communication-based method
requires communication but leads to completing the mission
more quickly, as shown in Table VI.
VII. CONCLUSION
We presented the asynchronous and distributed trajectory
planning algorithm for quadrotor swarms. By ensuring that the
agents have the same coordination states, such as waypoints,
subgoals, and safety constraints, we enabled the quadrotor
swarm to operate asynchronously without communication be-
tween the agents. We proved that the proposed algorithm
guarantees 1) collision avoidance against the other agents and
static obstacles and 2) deadlock resolution. Additionally, to
improve the slow operation speed, we proposed a method that
relies on communication but enables fast coordination state
updates, thereby reducing the overall flight time. We confirmed
that the proposed methods achieve a 100% success rate in
environments with densely located obstacles, while the state-
of-the-art (SOTA) algorithms show poor performance. Lastly,
we conducted the challenging hardware demonstration in the
narrow-gap environments with eight Crazyflie quadrotors, and
there was no collision and deadlock during the flight.
REFERENCES
[1] Y. Miao, K. Hwang, D. Wu, Y. Hao, and M. Chen, “Drone swarm path
planning for mobile edge computing in industrial internet of things,”
IEEE Transactions on Industrial Informatics, vol. 19, no. 5, pp. 6836–
6848, 2022.
[2] S. Ivi´c, B. Crnkovi´c, L. Grbˇci´c, and L. Matlekovi´c, “Multi-uav trajectory
planning for 3d visual inspection of complex structures,” Automation in
Construction, vol. 147, p. 104709, 2023.
[3] B. E. Jackson, T. A. Howell, K. Shah, M. Schwager, and Z. Manchester,
“Scalable cooperative transport of cable-suspended loads with uavs using
distributed trajectory optimization,” IEEE Robotics and Automation
Letters, vol. 5, no. 2, pp. 3368–3374, 2020.
[4] C. Toumieh and A. Lambert, “Decentralized multi-agent planning using
model predictive control and time-aware safe corridors,” IEEE Robotics
and Automation Letters, vol. 7, no. 4, pp. 11 110–11 117, 2022.
[5] K. Kondo, R. Figueroa, J. Rached, J. Tordesillas, P. C. Lusk, and J. P.
How, “Robust mader: Decentralized multiagent trajectory planner robust
to communication delay in dynamic environments,” IEEE Robotics and
Automation Letters, vol. 9, no. 2, pp. 1476–1483, 2023.
[6] M. Abdullhak and A. Vardy, “Deadlock prediction and recovery for
distributed collision avoidance with buffered voronoi cells,” in 2021
IEEE/RSJ International Conference on Intelligent Robots and Systems
(IROS).
IEEE, 2021, pp. 429–436.
[7] Y. Chen, M. Guo, and Z. Li, “Deadlock resolution and recursive feasibil-
ity in mpc-based multi-robot trajectory generation,” IEEE Transactions
on Automatic Control, 2024.
[8] J. Hou, X. Zhou, N. Pan, A. Li, Y. Guan, C. Xu, Z. Gan, and F. Gao,
“Primitive-swarm: An ultra-lightweight and scalable planner for large-
scale aerial swarms,” arXiv preprint arXiv:2502.16887, 2025.

## Page 13

13
[9] F. Amigoni, J. Banfi, and N. Basilico, “Multirobot exploration of
communication-restricted environments: A survey,” IEEE Intelligent
Systems, vol. 32, no. 6, pp. 48–57, 2017.
[10] F. Augugliaro, A. P. Schoellig, and R. D’Andrea, “Generation of
collision-free trajectories for a quadrocopter fleet: A sequential convex
programming approach,” in 2012 IEEE/RSJ international conference on
Intelligent Robots and Systems.
IEEE, 2012, pp. 1917–1922.
[11] J. Park, J. Kim, I. Jang, and H. J. Kim, “Efficient multi-agent trajectory
planning with feasibility guarantee using relative bernstein polynomial,”
in 2020 IEEE International Conference on Robotics and Automation
(ICRA).
IEEE, 2020, pp. 434–440.
[12] S. Tang and V. Kumar, “Safe and complete trajectory generation for
robot teams with higher-order dynamics,” in 2016 IEEE/RSJ Interna-
tional Conference on Intelligent Robots and Systems (IROS).
IEEE,
2016, pp. 1894–1901.
[13] C. Toumieh and D. Floreano, “High-speed motion planning for aerial
swarms in unknown and cluttered environments,” IEEE Transactions on
Robotics, 2024.
[14] S. H. Semnani, A. H. de Ruiter, and H. H. Liu, “Force-based algorithm
for motion planning of large agent,” IEEE Transactions on Cybernetics,
vol. 52, no. 1, pp. 654–665, 2020.
[15] H. Pan, M. Zahmatkesh, F. Rekabi-Bana, F. Arvin, and J. Hu, “T-star:
Time-optimal swarm trajectory planning for quadrotor unmanned aerial
vehicles,” IEEE Transactions on Intelligent Transportation Systems,
2025.
[16] J. Tordesillas and J. P. How, “Mader: Trajectory planner in multiagent
and dynamic environments,” IEEE Transactions on Robotics, 2021.
[17] ——, “Minvo basis: Finding simplexes with minimum volume enclosing
polynomial curves,” Computer-Aided Design, vol. 151, p. 103341, 2022.
[18] X. Zhou, X. Wen, Z. Wang, Y. Gao, H. Li, Q. Wang, T. Yang, H. Lu,
Y. Cao, C. Xu, et al., “Swarm of micro flying robots in the wild,” Science
Robotics, vol. 7, no. 66, p. eabm5954, 2022.
[19] Z. Wang, X. Zhou, C. Xu, and F. Gao, “Geometrically constrained tra-
jectory optimization for multicopters,” IEEE Transactions on Robotics,
vol. 38, no. 5, pp. 3259–3278, 2022.
[20] B. S¸enbas¸lar and G. S. Sukhatme, “Dream: Decentralized real-time
asynchronous probabilistic trajectory planning for collision-free multi-
robot navigation in cluttered environments,” IEEE Transactions on
Robotics, 2024.
[21] S. Zhang, O. So, K. Garg, and C. Fan, “Gcbf+: A neural graph control
barrier function framework for distributed safe multi-agent control,”
IEEE Transactions on Robotics, 2025.
[22] M. Boldrer, A. Serra-Gomez, L. Lyons, J. Alonso-Mora, and L. Fer-
ranti, “Rule-based lloyd algorithm for multi-robot motion planning
and control with safety and convergence guarantees,” arXiv preprint
arXiv:2310.19511, 2023.
[23] J. Alonso-Mora, J. A. DeCastro, V. Raman, D. Rus, and H. Kress-
Gazit, “Reactive mission and motion planning with deadlock resolution
avoiding dynamic obstacles,” Autonomous Robots, vol. 42, no. 4, pp.
801–824, 2018.
[24] J. Park, Y. Lee, I. Jang, and H. J. Kim, “Decentralized trajectory planning
for quadrotor swarm in cluttered environments with goal convergence
guarantee,” The International Journal of Robotics Research, vol. 0, no. 0,
p. 02783649241312352, 0.
[25] D. Zhou, Z. Wang, S. Bandyopadhyay, and M. Schwager, “Fast, on-line
collision avoidance for dynamic vehicles using buffered voronoi cells,”
IEEE Robotics and Automation Letters, vol. 2, no. 2, pp. 1047–1054,
2017.
[26] A. Pierson, W. Schwarting, S. Karaman, and D. Rus, “Weighted buffered
voronoi cells for distributed semi-cooperative behavior,” in 2020 IEEE
international conference on robotics and automation (ICRA).
IEEE,
2020, pp. 5611–5617.
[27] M. Abdullhak and A. Vardy, “Deadlock prediction and recovery for
distributed collision avoidance with buffered voronoi cells,” in 2021
IEEE/RSJ International Conference on Intelligent Robots and Systems
(IROS).
IEEE, 2021, pp. 429–436.
[28] L. Luo, X. Wang, J. Ma, and Y.-S. Ong, “Grpavoid: Multigroup collision-
avoidance control and optimization for uav swarm,” IEEE Transactions
on Cybernetics, vol. 53, no. 3, pp. 1776–1789, 2021.
[29] Z. Mao, M. Hou, H. Li, Y. Yang, and W. Song, “Multi-uav cooper-
ative motion planning under global spatio-temporal path inspiration in
constraint-rich dynamic environments,” IEEE Transactions on Intelligent
Vehicles, 2024.
[30] S. H. Semnani, A. H. de Ruiter, and H. H. Liu, “Force-based algorithm
for motion planning of large agent,” IEEE Transactions on Cybernetics,
vol. 52, no. 1, pp. 654–665, 2020.
[31] S. Lloyd, “Least squares quantization in pcm,” IEEE transactions on
information theory, vol. 28, no. 2, pp. 129–137, 1982.
[32] J. Park, D. Kim, G. C. Kim, D. Oh, and H. J. Kim, “Online distributed
trajectory planning for quadrotor swarm with feasibility guarantee using
linear safe corridor,” IEEE Robotics and Automation Letters, vol. 7,
no. 2, pp. 4869–4876, 2022.
[33] J. Park, Y. Lee, I. Jang, and H. J. Kim, “Dlsc: Distributed multi-agent
trajectory planning in maze-like dynamic environments using linear safe
corridor,” IEEE Transactions on Robotics, 2023.
[34] D. Mills, J. Martin, J. Burbank, and W. Kasch, “Network time protocol
version 4: Protocol and algorithms specification,” Tech. Rep., 2010.
[35] J. Park, I. Jang, and H. J. Kim, “Decentralized deadlock-free trajectory
planning for quadrotor swarm in obstacle-rich environments,” in 2023
IEEE International Conference on Robotics and Automation (ICRA).
IEEE, 2023, pp. 1428–1434.
[36] K. Okumura, M. Machida, X. D´efago, and Y. Tamura, “Priority inheri-
tance with backtracking for iterative multi-agent path finding,” Artificial
Intelligence, vol. 310, p. 103752, 2022.
[37] M. E. Flores, “Real-time trajectory generation for constrained nonlinear
dynamical systems using non-uniform rational b-spline basis functions,”
Ph.D. dissertation, California Institute of Technology, 2008.
[38] J. Park, J. Kim, I. Jang, and H. J. Kim, “Efficient multi-agent trajectory
planning with feasibility guarantee using relative bernstein polynomial,”
in 2020 IEEE International Conference on Robotics and Automation
(ICRA), 2020, pp. 434–440.
[39] D. Zhou, Z. Wang, S. Bandyopadhyay, and M. Schwager, “Fast, on-line
collision avoidance for dynamic vehicles using buffered voronoi cells,”
IEEE Robotics and Automation Letters, vol. 2, no. 2, pp. 1047–1054,
2017.
[40] B. S¸enbas¸lar and G. S. Sukhatme, “Asynchronous real-time decentral-
ized multi-robot trajectory planning,” in 2022 IEEE/RSJ International
Conference on Intelligent Robots and Systems (IROS).
IEEE, 2022, pp.
9972–9979.
[41] S. Boyd, S. P. Boyd, and L. Vandenberghe, Convex optimization.
Cambridge university press, 2004.
[42] A. Hornung, K. M. Wurm, M. Bennewitz, C. Stachniss, and W. Burgard,
“Octomap: An efficient probabilistic 3d mapping framework based on
octrees,” Autonomous robots, vol. 34, no. 3, pp. 189–206, 2013.
[43] I. CPLEX, “12.7. 0 user’s manual,” 2016.
[44] W. Giernacki, M. Skwierczy´nski, W. Witwicki, P. Wro´nski, and
P. Kozierski, “Crazyflie 2.0 quadrotor as a platform for research and
education in robotics and control engineering,” in 2017 22nd interna-
tional conference on methods and models in automation and robotics
(MMAR).
IEEE, 2017, pp. 37–42.
Yunwoo Lee Yunwoo Lee received his B.S. degree
in Electrical and Computer Engineering and his
Ph.D. degree in Mechanical and Aerospace En-
gineering from Seoul National University, Seoul,
South Korea, in 2019 and 2025, respectively. He
is currently working for the AI Institute of Seoul
National University and conducting on-site research
at Carnegie Mellon University. His current research
interests include multi-robot systems and vision-
based trajectory planning for MAVs.
Jungwon Park received the B.S. degree in electrical
and computer engineering in 2018, and the M.S and
Ph.D. degrees in mechanical and aerospace engineer-
ing at Seoul National University, Seoul, South Korea
in 2020 and 2023, respectively. He is currently an
assistant professor at Seoul National University of
Science and Technology (SeoulTech), Seoul, South
Korea. His current research interests include path
planning and task allocation for distributed multi-
robot systems. His work was a finalist for the Best
Paper Award in Multi-Robot Systems at ICRA 2020
and won the top prize at the 2022 KAI Aerospace Paper Award.
