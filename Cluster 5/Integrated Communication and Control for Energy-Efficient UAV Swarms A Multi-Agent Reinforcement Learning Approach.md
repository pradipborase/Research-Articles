# Integrated Communication and Control for Energy-Efficient UAV Swarms A Multi-Agent Reinforcement Learning Approach.pdf

## Page 1

1
Integrated Communication and Control for
Energy-Eﬀicient UAV Swarms: A Multi-Agent
Reinforcement Learning Approach
Tianjiao Sun, Ningyan Guo, Haozhe Gu, Yanyan Peng, and Zhiyong Feng, Senior Member, IEEE,
Abstract—The
deployment
of
unmanned
aerial
vehicle
(UAV) swarm-assisted communication networks has become an
increasingly vital approach for remediating coverage limitations
in infrastructure-deficient environments, with especially press-
ing applications in temporary scenarios, such as emergency
rescue, military and security operations, and remote area
coverage. However, complex geographic environments lead to
unpredictable and highly dynamic wireless channel conditions,
resulting in frequent interruptions of air-to-ground (A2G)
links that severely constrain the reliability and quality of
service in UAV swarm-assisted mobile communications. To
improve the quality of UAV swarm-assisted communications in
complex geographic environments, we propose an integrated
communication and control co-design mechanism. Given the
stringent energy constraints inherent in UAV swarms, our
proposed mechanism is designed to optimize energy eﬀiciency
while maintaining an equilibrium between equitable communi-
cation rates for mobile ground users (GUs) and UAV energy
expenditure. We formulate the joint resource allocation and
3D trajectory control problem as a Markov decision process
(MDP), and develop a multi-agent reinforcement learning
(MARL) framework to enable real-time coordinated actions
across the UAV swarm. To optimize the action policy of UAV
swarms, we propose a novel multi-agent hybrid proximal policy
optimization with action masking (MAHPPO-AM) algorithm,
specifically designed to handle complex hybrid action spaces.
The algorithm incorporates action masking to enforce hard
constraints in high-dimensional action spaces. Experimental
results demonstrate that our approach achieves a fairness index
of 0.99 while reducing energy consumption by up to 25%
compared to baseline methods.
Index Terms—Unmanned aerial vehicle, multi-agent rein-
forcement learning, energy-eﬀicient, 3D trajectory control,
resource allocation.
I. Introduction
U
NDER the constraints of complex electromagnetic
environments, traditional terrestrial wireless com-
munication networks face challenges including degraded
propagation channels, constrained topological structures,
scarce spectrum resources, and limited coverage [1]. In
contrast, unmanned aerial vehicle (UAV) swarms effec-
tively overcome the limitations of traditional terrestrial
wireless networks by leveraging their three-dimensional
Tianjiao Sun, Ningyan Guo, Haozhe Gu, Yanyan Peng, and
Zhiyong Feng are with the Key Laboratory of Universal Wireless
Communications,
Ministry
of
Education,
Beijing
University
of
Posts
and
Telecommunications,
Beijing
100876,
China
(e-mail:
suntianjiao@bupt.edu.cn,
guoningyan@bupt.edu.cn,
Gu_haozhe@bupt.edu.cn,
pengyanyan@bupt.edu.cn,
fengzy@bupt.edu.cn).
mobility [2] [3], dynamic networking capability, flexible
spectrum reuse, and extended coverage, thereby providing
communication services for ground users (GUs) [4] - [7].
Therefore, UAV swarm-assisted communication networks
have gained growing popularity in both civilian and
military applications, such as emergency rescue, military
and security operations, and remote area coverage [8] [9].
Prior works have investigated joint communication re-
source allocation and trajectory control for UAV swarms,
primarily using conventional optimization methods such
as convex optimization. Qiu et al. [10] propose an eﬀi-
cient iterative algorithm for joint optimization of user
association and UAV-mounted base station placement,
utilizing gradient ascent, dual-domain coordinated de-
scent, and bipartite graph matching techniques. Using a
successive convex approximation (SCA) algorithm, Shen
et al. [11] address multi-UAV interference coordination
through joint trajectory design and power control. Liu
et al. [12] employ the SCA algorithm to maximize sys-
tem throughput through joint optimization of vehicle
communication scheduling, UAV power allocation, and
trajectories. Zhu et al. [13] propose a suboptimal solution
for joint user clustering, transmit/receive beamforming,
and UAV placement. In multi-UAV assisted systems,
Zhang et al. [14] investigate the co-optimization of UAV
trajectories, user association, and beamforming using an
alternating optimization algorithm.
However, these works predominantly use simplified line
of sight (LoS) channel models for air-to-ground (A2G)
links, which facilitate trajectory optimization and average
performance analysis. In reality, complex urban envi-
ronments [15] introduce severe signal obstruction that
significantly degrades A2G link quality. When channel
states are unknown a priori, deep reinforcement learning
(DRL) has demonstrated strong potential for solving
dynamic and non-convex UAV communication problems
[16] [17]. Multi-agent reinforcement learning (MARL) is
particularly suitable for UAV swarm-assisted communica-
tion and control systems. Existing MARL methods are
broadly categorized by action space nature: discrete or
continuous.
• Discrete Action Spaces: Zhong et al. [18] propose
a mutual deep Q-network (MDQN) algorithm for
joint 3D trajectory and power allocation optimiza-
tion in UAVs. Won Joon Yun et al. [19] investi-
gate a model-free MARL-based collaborative scheme
arXiv:2509.23905v1  [cs.LG]  28 Sep 2025

## Page 2

2
for autonomous surveillance UAVs, targeting energy-
eﬀicient and reliable surveillance. Wang et al. [20]
develop a Q-value mixing (QMIX)-based algorithm to
jointly optimize the trajectories of UAVs and sensor
node scheduling, minimizing the time-average total
expected age of information.
• Continuous Action Spaces: In a practical user roaming
scenario served by multiple UAVs [21], a hybrid re-
ward multi-agent proximal policy optimization (HR-
MAPPO) algorithm is proposed to jointly optimize
UAVs’ trajectory and beamforming to maximize the
sum data rate. Xu et al. [22] investigate multi-UAV
trajectory design for uplink data collection task using
the Q-network in DRL. In [23] and [24], multiple
UAVs are deployed to serve ground users on contin-
uous maps. The former introduces the multi-agent
long short-term memory-deep deterministic policy
gradient (LSTM-DDPG) method to maximize data
collection, while the latter utilizes the proximal pol-
icy optimization (PPO) to minimize the cumulative
content acquisition delay for users.
Nevertheless, the aforementioned studies predominantly
address discrete or continuous action spaces in isolation,
often overlooking the complexities inherent to hybrid
action space scenarios. This limitation substantially con-
strains the decision-making capacity of UAV swarms in
dynamic real-world environments. Although the latest
work [25] investigates the UAV data collection with
discrete variables (radar, communication, movement) and
continuous variables (transmit power, flying direction,
velocity), it ignores the obstruction impact on A2G links
in complex geographic environment, which is a critical
factor for reliable communication performance.
Existing research on UAV swarm-assisted integrated
communication and control systems still faces critical tech-
nical challenges in practical deployment. First, the unpre-
dictability and dynamics of the channel in real-world lead
to frequent interruptions of the A2G link, which seriously
degrades communication fairness and quality of service.
Second, UAV swarms are limited by current decision-
making capabilities and lack essential mechanisms to
coordinate their actions. To address these, a novel MARL
framework is proposed to enable autonomous decision-
making in UAV swarm-assisted integrated communication
and control systems. The main contributions of this paper
are summarized as follows:
1) To enhance quality of communication service in
complex geographic environment, we propose a UAV
swarm-assisted integrated communication and con-
trol co-design mechanism. Considering the energy
constraints of UAV swarms, we formulate an objec-
tive function that characterizes the trade-off between
the fairness-constrained communication rates for
ground users and UAVs’ energy consumption.
2) We model the UAV swarm’s resource allocation
and 3D trajectory control as a Markov decision
process (MDP) and propose a MARL framework
Subcarriers
Obstructed Area
Fig. 1. UAV swarm-assisted communication network.
as a solution, which facilitates decision-making on
collaborative actions among UAVs in real time.
3) To address hybrid action space challenges in UAV
swarms, we propose a novel multi-agent hybrid
proximal policy optimization with action masking
(MAHPPO-AM) algorithm that guarantees hard
constraints in high-dimensional action spaces via
action masking.
4) Experimental results demonstrate that our approach
achieves a fairness index of 0.99 while reducing
energy consumption by up to 25% compared to
baseline methods.
The remainder of this paper is organized as follows.
Section II presents the system model and problem for-
mulation. In Section III, Markov decision process (MDP)
is formally defined and we present the MARL-based
solution to the optimization problem. Simulation results
are presented and discussed in Section IV. In Section V,
we conclude the whole paper.
II. System Model and Problem Formulation
A. System Model
As shown in Fig.1, we focus on a UAV swarm-assisted
orthogonal frequency division multiple access (OFDMA)
downlink communication network in obstructed outdoor
environments, where M UAVs are deployed as aerial
base stations to serve K mobile ground users via N
orthogonal subcarriers for each UAV. The sets of UAVs,
users, and subcarriers are denoted as M = {1, 2, ..., M},
K = {1, 2, ..., K}, and N = {1, 2, ..., N}. It is assumed
that channel resources are insuﬀicient to serve all the
users simultaneously, i.e., MN ≤K, making resource
allocation critical for enhancing system performance. Each
UAV allocates orthogonal subcarriers to its served ground
users, eliminating intra-UAV interference. However, since
all the UAVs share the same N subcarriers, users served
by different UAVs on the same subcarrier may suffer from
mutual interference.
Meanwhile, buildings and other obstacles may cause
severe obstruction to the A2G links and drastically weaken
the received signal strength of users in obstructed area. To
ensure that UAV swarms can effectively serve these users,

## Page 3

3
it is essential to design UAV trajectory that maximize
downlink communication performance. We consider the
UAVs’ trajectory and resource allocation by discretizing
the entire time horizon into T equally-spaced time slots.
The duration of each timeslot is Ts. In a 3D Cartesian
coordinate, the instantaneous location of UAV m within
timeslot t is denoted by qm(t) = [xm(t), ym(t), hm(t)]T ,
where q(t) = {q1(t), ..., qM(t)} with t ∈T = {1, ..., T}.
The horizontal coordinate of ground user k is denoted by
uk(t) = [xk(t), yk(t)]T .
1) UAV-GU Communication Model
According to the 3GPP Release 15 [26], we can obtain
the A2G channel model between each UAV and ground
user. The path loss depends on LoS and non-line-of-sight
(NLoS) link states and the design formulas of path loss
LLoS/NLoS(t) between the user k and UAV m can be
expressed as (1), shown at the bottom of the page, where
fc denotes carrier frequency, and the 3D distance from
UAV m to user k at timeslot t is denoted as (2).
In the propagation model, the probability of LoS is
denoted as PLoS(t) in (3), shown at the bottom of the
page, where d0 = max[294.05 · log10hm(t) −432.94, 18]
and p1 = 233.98 · log10hm(t) −0.95. Logically, the NLoS
probability is PNLoS(t) = 1 −PLoS(t). Thus, the mean
path loss between the UAV m and user k can be given by
Lm
k (t) = PLoS · LLoS + PNLoSLNLoS.
(4)
Considering small-scale fading, the channel gain from the
UAV m and user k at timeslot t can be calculated by
gm
k (t) = Hm
k (t) · 10−Lm
k (t)/10,
(5)
where Hm
k (t) is the fading coeﬀicient [27] between UAV
m and user k.
To facilitate formulation, we define a set of binary
variables ϕ(t) = {ϕk,m,n(t)|k ∈K, m ∈M, n ∈N} as
the indicators for resource allocation involving channel
assignment and the user association, where ϕk,m,n(t) = 1
refers to user k served by UAV m on channel n at timeslot
t and ϕk,m,n(t) = 0 means otherwise. Note that p(t) =
{pm,n(t)|m ∈M, n ∈N} is the set of transmit power
of the UAV swarm, and pm,n(t) denotes the downlink
transmit power of UAV m on channel n within timeslot t.
Hence, in timeslot t, signal-to-interference-plus-noise ratio
(SINR) received by user k from UAV m on channel n can
be expressed by
γk,m,n(t) =
pm,n(t)|gm
k (t)|2
M
P
j=1,j̸=m
pj,n(t)
gj
k(t)

2
+ σ2
,
(6)
where
σ2
denotes
the
noise
power
and
the
term
PM
j=1,j̸=m pj,n(t)
gj
k(t)

2
in the denominator refers to the
co-channel interference. Therefore, the link rate achieved
by user k at timeslot t [15] is given by
Rk(t) =
M
X
m=1
N
X
n=1
ϕk,m,n(t) log (1 + γk,m,n(t)).
(7)
The total achievable rate by all the ground users at
timeslot t is
Rc(t) =
K
X
k=1
Rk(t).
(8)
Thus, the total achievable rate before timeslot t is
¯R(t) = Rc(1) + ... + Rc(t),
(9)
and the achievable rate by the ground user k before
timeslot t is
¯Rk(t) = Rk(1) + ... + Rk(t).
(10)
However, maximizing the total transmission rate may
lead to inequity, where the UAV may tend to be close to
some users with good channel conditions, while obstructed
users suffer from low rate all the time. To tackle this issue,
we refer to [28] and define the rate ratio of user k as
fk(t) =
¯Rk(t)
¯R(t) .
(11)
Then Jain’s fairness index [29] is employed to measure the
fairness among users
ˆf(t) =
PK
k=1 fk(t)
2
K
PK
k=1 fk(t)2.
(12)
where ˆf(t) ∈[0, 1]. The smaller the differences among the
rate ratios {fk(t)}k∈K are, the greater fairness index ˆf(t)
is. Notably, both the fairness index and the total rate are
LLoS/NLoS(t) =
 30.9 + (22.25 −0.5log10hm(t))log10dm
k (t) + 20log10fc,
if LoS,
max{LLoS, 32.4 + (43.2 −7.6log10hm(t))log10dm
k (t) + 20log10fc}, if NLoS.
(1)
dm
k (t) =
q
hm
2(t) + [xm(t) −xk(t)]2 + [ym(t) −yk(t)]2.
(2)
PLoS(t) =





1,
if
q
(dm
k (t))2 −(hm(t))2 ≤d0,
d0
√
(dm
k (t))2−(hm(t))2 + exp

−√
(dm
k (t))2−(hm(t))2
p1
+ d0
p1

,
if
q
(dm
k (t))2 −(hm(t))2 > d0.
(3)

## Page 4

4
the functions of the UAV swarm trajectory q, transmit
power p, and channel allocation ϕ. Then the total fair
rate during the whole mission can be defined as
R(t) = ˆf(t)Rc(t).
(13)
2) UAV Energy Consumption Model
UAV swarm-assisted communication systems face the
challenge of energy limitations, and the energy con-
sumption of the UAV consists of two parts: one for
communication and the other for propulsion energy to
generate thrusts. In practice, the communication energy
is often much smaller than flight energy by two orders
of magnitude [30]. As a result, the propulsion energy
consumption of the UAV must be taken into account.
For clarity, we consider only the acceleration component
aligned with the UAV’s velocity and ignore the component
perpendicular to it. Under this assumption, it is reasonable
to allow the UAV to change its flight direction instanta-
neously without incurring additional energy consumption,
as a quadrotor UAV can easily maneuver by adjusting the
rotational speed of its four rotors. The thrust of rotors is
a function of UAV velocity vm(t) and acceleration ac
m(t).
And vm(t) = ∥vm(t)∥is the UAV speed. Then the thrust
of UAV m can be expressed as
||F(vm)|| =
m′ac
m + 1
2ρSF P ||vm||vm −m′g
 ,
(14)
where m′ denotes the UAV mass. ρ and SF P are the air
density and fuselage equivalent flat plate area, respec-
tively. g denotes the gravity acceleration vector. Consid-
ering vm(t)
∆= ˙qm(t) and ac
m(t)
∆= ¨qm(t), ˙qm(t) and ¨qm(t)
denote the first- and second-order derivative with respect
to t, respectively. The propulsion power is essentially a
function of the UAV trajectory qm(t). Then with a given
trajectory qm(t), the propulsion energy of UAV m at a
timeslot can be expressed as (15), shown at the bottom
of the page, where δ denotes the local blade section drag
coeﬀicient; cT is the thrust coeﬀicient based on disc area; A
and cS denote the disc area and rotor solidity, respectively;
cf is the incremental correction factor of induced power;
τc denotes the climb angle. Further, the total propulsion
energy consumption of the UAV swarm is given by
E(t) =
M
X
m=1
Em(t).
(16)
B. Problem Formulation
In this paper, we propose a resource allocation and
trajectory control mechanism for UAV swarms in 3D
space. Specifically, the total achievable rate Rc(t) of
mobile ground users is first modeled as a function of the
subcarrier-user correlation coeﬀicient ϕk,m,n(t), the UAV
subcarrier transmit power pm,n(t), and the UAV trajectory
qm(t) based on the A2G channel model specified by the
3GPP protocol. Subsequently, the UAV energy consump-
tion Em(t) is modeled as a function of UAV trajectory
qm(t). Due to the size and weight constraints, on-board
batteries with limited energy will lead to endurance and
performance degradation. Thus, energy eﬀiciency, defined
as the information bits per unit energy consumption, is a
critical issue in UAV swarm-assisted communication and
control. Finally, the optimization objective of this paper
is to maximize the long-term energy eﬀiciency of the UAV
swarm, which can be formulated as
(P1):max
ϕ,p,q
T
X
t=1
ηee(t)
(17)
s.t.
||qm(t) −qj(t)|| ≥dmin,
m, j ∈M, m ̸= j,(18)
0 ≤vm(t) ≤vmax,
(19)
0 ≤||ac
m(t)|| ≤amax,
(20)
hmin ≤hm(t) ≤hmax,
(21)
K
X
k=1
ϕk,m,n(t) ≤1,
(22)
M
X
m=1
N
X
n=1
ϕk,m,n(t) ≤1,
(23)
N
X
n=1
pm,n(t) ≤pmax,
(24)
where
ηee(t) =
ˆf(t)Rc(t)
E(t)
.
(25)
The optimization objective captures the trade-off between
ensuring fair communication rates for mobile users and
minimizing the UAVs’ energy consumption. In practice,
constraint (18) enforces a safe distance between UAVs to
prevent collisions. Constraints (19), (20), and (21) indicate
the limitations of UAVs’ flying speed, acceleration, and
height. Constraints (22) and (23) ensure that each UAV
serves at most one user on one subcarrier and each user
can be only served by at most one UAV. Constraint (24)
limits the total power budget of each UAV. Apparently, the
optimization objective is mixed-integer and non-convex,
which is generally NP-hard. As such, conventional convex
optimization methods are inadequate for solving it in real
time. To address this challenge, we propose a multi-agent
reinforcement learning framework as an effective solution.
Em(t) =

δ
8

||F ( ˙qm,¨qm)||
cT ρA
+ 3||vm||2 q
ρc2
SA||F ( ˙qm,¨qm)||
cT
+ m′||g||||vm|| sin τc

Ts+
 
(1 + cf)||F( ˙qm, ¨qm)||
q
||F ( ˙qm,¨qm)||2
4ρ2A2
+ ||vm||4
4
−||vm||2
2
 1
2
+ 1
2ρSF P ||vm||3
!
Ts.
(15)

## Page 5

5
III. Multi-Agent Reinforcement Learning-based Solutions
In this section, the UAV swarm’s resource allocation
and 3D trajectory control are considered as a sequential
decision process, i.e., a decision is made at each single
step based on the current observation. Under the MARL
framework, UAVs play the role of agents whose goal is to
maximize long-term energy eﬀiciency while ensuring fair
communication.
A. Markov Decision Process Definitions
Mathematically, the complete MDP can be denoted by
a tuple {S, A, P, r, γ}, where S is the state space, A is the
action space, P is the state transition probability, r is the
reward at each step, and γ is the discount factor. In each
timeslot, the UAV m chooses an action am with policy
πm(am|sm). The joint action a ∈A of all the UAVs causes
an environment transition from the current state s ∈S
to the next state s′ ∈S following the state transition
P(s′|s, a), which is unknown to all the UAVs. And the
mutual goal of all the UAVs is to maximize the cumulative
discounted total return
G =
T
X
t=1
γt−1rt.
(26)
As discussed in Section II-B, (P1) involves combina-
torial optimization and is highly coupled between the
variables, which makes it diﬀicult for traditional convex
optimization to solve in real-time. Fortunately, multi-
agent RL algorithms allow each agent to make an optimal
decision following its learned policy through a trial-and-
error way. To fit the problem of resource allocation and
trajectory control into a MARL framework, the essential
elements of the Markov decision process can be defined as
follows.
1) State Space
As mentioned in Section II-A, the link rate is related to
the path loss between the UAV and mobile GUs. However,
the locations of the UAVs and GUs are easier to obtain
than path loss, as most mobile GUs are equipped with
global positioning system (GPS) sensors. Besides, the
locations of GUs change all the time. As a result, the state
space includes the GUs’ locations {uk(t), k ∈K} and the
UAVs’ locations {qm(t −1), m ∈M} from the previous
timeslot such that UAVs can deal with the movement of
GUs. Moreover, since the flight energy consumption of a
UAV is a function of the UAV’s speed, the state includes
the UAVs’ speed {vm(t −1), m ∈M} from the previous
timeslot, which also aims to remind the UAV not to exceed
the acceleration constraint. Thus, the state can be defined
as
s(t) = {uk(t), qm(t −1), vm(t −1)|k ∈K, m ∈M}, (27)
and has 3(K + M + 1) dimensions.
2) Hybrid Action Space
The action decided by the UAV m consists of user-
channel assignment,transmit power allocation, and UAV’s
trajectory, which can be defined as
am(t) = {ϕk,m,n(t), pm,n(t), qm(t)|k ∈K, m ∈M, n ∈N}.
(28)
• User-Channel Assignment: ϕk,m,n(t) ∈{0, 1} denotes
a binary discrete variable,and ϕk,m,n(t) = 1 refers
to the user k served by UAV m on channel n at
timeslot t. The user-channel assignment for UAV
m can be expressed as (29), shown at the bottom
of the next page, where
K
P
k=1
ϕk,m,n(t)
≤
1 and
M
P
m=1
N
P
n=1
ϕk,m,n(t) ≤1.
• Transmit Power Allocation: {pm,n(t)|m ∈M, n ∈N}
denotes the downlink transmit power of UAV m on
channel n within timeslot t and pmax denotes the
UAV’s total power budget in each timeslot. We also
assume that the total power budget of each UAV is
limited, i.e.,
N
P
n=1
pm,n(t) ≤pmax.
• UAV’s Trajectory: In 3D space, we utilize the spher-
ical coordinate (vm(t), θ(t), φ(t)) to describe the
UAV’s speed and flight direction more conveniently,
where vm(t) ∈(0, vmax) is the UAV’s speed, θ(t) ∈
(0, 2π) is the azimuthal angle, and φ(t) ∈(π/3, 2π/3)
is known to be the polar angle. Such a definition al-
ways satisfies the constraints of the UAV’s maximum
speed and pitch angle in each time slot.
In summary, the action of UAV m actually consists of
five parts (30), shown at the bottom of the next page.
Thus, the joint action space of all UAVs can be expressed
as,
a(t) = {a1(t), ..., aM(t)}.
(31)
3) Reward
In MARL, reward serves as a measure of how favorable
an action is under a given state. By appropriately design-
ing the reward function, the original non-convex objective
(P1) can be transformed into a problem of maximizing
cumulative reward. Given that we aim to maximize long-
term energy eﬀiciency while ensuring fair communication,
the immediate reward can be defined as follows,
r(t) = ηee(t).
(32)
B. Design of the MAHPPO-AM Algorithm
In this section, we propose an MAHPPO-AM algorithm
to solve the UAV swarm-assisted integrated communi-
cation and control co-design. We first design the action
masking of the algorithm and then provide the optimiza-
tion process of the multi-agent RL algorithm.
1) Action Masking
In MARL, the purpose of action masking is to restrict
the agent’s action space to exclusively select valid actions
that conform to the rules and constraints of the environ-
ment [31]. Hence, the approach is especially critical for
discretized user-channel assignment actions. On the one
hand, the mechanism constructs a dynamic feasible action

## Page 6

6
space by means of predefined constraint rules. Compared
with conventional policy networks that directly output
unfiltered action distributions, this constraint-embedded
approach fundamentally prevents invalid allocation, such
as multiple users on the same channel or overcapacity
resource allocation. Consequently, this approach ensures
that the output decisions meet communication fairness
requirements at each timeslot.
On the other hand, the exploration space of agent
is compressed to the valid policy subspace by masking
invalid actions. This mechanism not only reduces the
sample waste of invalid exploration, but also accelerates
the gradient optimization process by reducing the pol-
icy search dimension. Based on real-time environmental
observations, action masking is designed to satisfy hard
constraints in high-dimensional discrete action spaces.
Specifically, it ensures that user-channel assignment ϕ
satisfies the following constraints:
• Global GU Constraint: Each user is served by
at
most
one
UAV
on
a
single
channel,
i.e.,
M
P
m=1
N
P
n=1
ϕk,m,n(t) ≤1.
• Global
Channel
Constraint:
Each
channel
is
assigned
to
a
maximum
of
M
UAVs,
i.e.,
M
P
m=1
K
P
k=1
ϕk,m,n(t) ≤M.
• UAV Constraint: Each UAV serves at most one
user
or
on
one
subcarrier,i.e.,
K
P
k=1
ϕk,m,n(t)
≤
1,
N
P
n=1
ϕk,m,n(t) ≤1.
The dynamic valid action space is defined as ˜Vt ⊆K ×
M × N, and elements (k, m, n) satisfy (33), shown at the
bottom of the page. Iterating over (k, m, n) ∈K×M×N ,
those satisfying ˜Vt are filtered to form a candidate action
set Vt. For each (k, m, n) ∈Vt, the normalized probability
can be calculated by
P(k, m, n) =
ezk,m,n
P
(k′,m′,n′)∈Vt ezk′,m′,n′ ,
(34)
where zk,m,n is the output logits of the m-th agent’ policy
network. The action masking restricts the policy search to
the valid space ˜Vt ⊆K × M × N by dynamically filtering
invalid actions, thus supporting the constrained coupling
of multi-agent collaborative decision-making.
2) MAHPPO-AM Algorithm
Traditional PPO algorithms are diﬀicult to deal with
both discrete and continuous action spaces. In order
to solve this problem, we investigate a multi-agent hy-
brid proximal policy optimization algorithm to address
the UAV swarm-assisted integrated communication and
control co-design. As shown in Fig. 2, the proposed
MAHPPO-AM algorithm adopts an Actor-Critic struc-
ture. The UAV swarm-assisted scenario contains multiple
agents, so multiple actor networks are used to provide
behavioral decisions for the agents, and the number of
actor networks is equal to the number of M agents. To
effectively tackle the hybrid action space, we add output
branches for the corresponding continuous and discrete
actions in each actor network to obtain discrete actions ad
and continuous actions ac. The five branches share several
front layers that encode state information and output
user-channel assignment, transmit power, UAV’s speed,
azimuth, and polar angle, respectively. The actor branches
that provide discrete actions output the probability of
choosing different possible actions simultaneously, which
is achieved by adding a softmax function to the end of
these branches. At the same time, the actor branches that
provide continuous actions output the mean and standard
deviation of the actions, and the continuous actions are
Gaussian distributed.
In the MAHPPO-AM algorithm, ϕ and θm are denoted
as the parameters of the critic network and the actor
network, where θm denotes the parameter of the actor
network corresponding to the m-th agent. In the UAV
swarm-assisted integrated communication and control sys-
tem, the inputs to the Actor-Critic network consist of
state vectors, which are GUs’ locations, UAVs’ locations,
and UAVs’ speed. In practice, these state vectors are
concatenated into a single vector. The actor network
ϕm =


ϕ1,m,1
ϕ1,m,2
...
ϕ1,m,N−1
ϕ1,m,N
...
...
...
...
...
ϕK,m,1
ϕK,m,2
...
ϕK,m,N−1
ϕK,m,N

,
(29)
am(t) = {ϕk,m,n(t), pm,n(t), vm(t), θm(t), φm(t)|k ∈K, m ∈M, n ∈N}.
(30)
˜Vt =











(k, m, n)|
M
X
m′=1
N
X
n′=1
ϕk,m′,n′(t) = 0
|
{z
}
Global GU Constraint
∧
M
X
m′=1
K
X
k′=1
ϕk′,m′,n(t) < M
|
{z
}
Global Channel Constraint
∧
N
X
n′=1
ϕk,m,n′(t) = 0
|
{z
}
UAV−GU Constraint
∧
K
X
k′=1
ϕk′,m,n(t) = 0
|
{z
}
UAV−Channel Constraint











.
(33)

## Page 7

7
…
…
…
…
…
Hybrid Actors
Critic
Memory
Buffer
Discrete Actor
Continuous Actor
－
×
Forward
Backward
…
…
…
…
…
…
da
ca
a
c
Experience
(
| )
t
t
a s

( )
t
V
s


( )
t
V
s

1
1
1
2
,
, ,
s a r s


2
2
2
3
,
, ,
s a r s


1
,
, ,
j
j
j
j
s a r s +


M Actors
State
M Masks
ˆ
tA
Subcarriers
Occlusion Area
Fig. 2.
The framework of MAHPPO-AM algorithm. The algorithm consists of multiple actor networks and a global critic network. All
state vectors observed from the environment are concatenated and sent to the actors and critic, respectively. Each actor outputs discrete
actions ad and continuous actions ac for its corresponding agent. The critic outputs the predicted state value. The memory buffer stores
previous experience.
outputs the policy πθ(at|st), which is the distribution of
the action at predicted at the state st. The critic network
outputs the predicted state value V π
ϕ (st), which is the
expected cumulative return of state st and guides the
update of all actor networks during the training phase.
First, we introduce the objective of the critic network
in the algorithm. The experience is obtained through a
Markov decision process, which describes the interaction
between the agents and the environment in the multi-agent
RL. We can then obtain the reward for each timeslot in
the experience, and the real cumulative return at state st
is given by
V ′π(st) =
T
X
t′=t
γt′−trt′,
(35)
where γ ∈[0, 1] denotes a discount factor that balances
long-term and short-term return. The sampled value
V π
ϕ (st) is used as the expected value of the cumulative
return to train the critic network, which has the following
loss function
Lc(ϕ) = ||V π
ϕ (st) −V ′π(st)||2.
(36)
Then, we present the objective of the actor network.
According to the trust region policy optimization [32], we
maximize the objective as follows
max
θ
Et
 πθ(at|st)
πθold(at|st)
ˆAt

,
(37)
where πθ(at|st) is the current policy and πθold(at|st) is
the old policy for collecting trajectories. In addition, the
advantage function
ˆAt denotes the deviation of action
at from the mean action at the state st. To reduce the
deviation, an exponentially-weighting method is employed
to obtain the generalized advantage estimation (GAE) [34]
ˆAt =
T
X
t′=t
(γλ)t′−t rt + γV π
ϕ (st+1) −V ′π(st)

.
(38)
Since the loss clipping policy has been proven effective
in training actor network, the clipped loss can be expressed
as
rt(θ) =
πθ(at|st)
πθold(at|st),
(39)
LCLIP (θ) = Et
h
min(rt(θ) ˆAt, clip(rt(θ), 1 −ϵ, 1 + ϵ) ˆAt)
i
,
(40)
where ϵ is a hyperparameter that controls the range of
clipped rt(θ). Finally, the objective function of the actor
network can be written as
La(θ) =
M
X
m=1

LCLIP (θm) + ζEt [H(πθm(at|st))]

,
(41)
where H(πθm(at|st)) is an entropy bonus that encourages
exploration and ζ is a balancing hyperparameter. The
critic network is supposed to fit an unknown state value
function, while the actor networks should provide a policy

## Page 8

8
to maximize the fitted state value. During the training
process, the network parameters are dynamically updated
by gradient optimization, which guides the critic and ac-
tors to gradually converge toward their optimal objectives.
The proposed MAHPPO-AM algorithm is summarized in
Algorithm 1.
Algorithm 1 MAHPPO-AM Algorithm for UAV Swarm-
assisted Integrated Communication and Control Co-design
1: Initialize parameters of critic and actor networks as ϕ
and θm, m ∈M;
2: Initialize the memory buffer ¯
M, batch size B, sample
reuse time ¯K and learning rate lr;
3: for episode = 1, . . . , Ep do
4:
Randomly select two obstructed areas;
5:
Randomly generate mobile GUs’ locations;
6:
Initialize the system state s1;
7:
for t = 1, . . . , T do
8:
Sample at ∼πθ (at | st) with action masking;
9:
Execute at to obtain its corresponding reward rt
and the next state st+1;
10:
Store tuple ⟨st, at, rt, st+1⟩in the memory buffer
¯
M;
11:
Current state st ←st+1;
12:
if ¯
M is filled then
13:
Compute state value in ¯
M using:
V ′π (st) = PT
t′=t γt′−trt′;
14:
Compute advantage for states in ¯
M based on
ˆAt =
TP
t′=t
(γλ)t′−t 
rt + γV π
ϕ (st+1) −V ′π(st)

;
15:
for i = 1, . . . ,
 ¯K × ( ¯
M/B)

do
16:
Sample a mini-batch of B tuples from ¯
M;
17:
Compute the loss of critic network:
Lc(ϕ) =
V π
ϕ (st) −V ′π (st)

2;
18:
Compute the loss of actor network:
La(θ) =
M
X
m=1

LCLIP (θm) + ζEt [H(πθm(at|st))]

;
19:
Update critic with ϕ ←ϕ −lr∇ϕLc(ϕ);
20:
for m = 1, . . . , M do
21:
Update actor with θm ←θm−lr∇θmLa(θ);
22:
end for
23:
end for
24:
Clear memories in ¯
M.
25:
end if
26:
end for
27: end for
IV. Simulation Results
In the 3D coordinate, we focus on an urban area of 1,500
× 1,500 m2, i.e., X = 1500, Y = 1500, and Z = 100. The
initial positions of the UAVs are fixed. The initial position
of user k is randomly and uniformly distributed on the
ground. Between any two consecutive time slots, i.e., t and
t + 1, user k moves a distance dk(t) in a direction θk(t),
TABLE I
Parameters and Values
Parameter
Symbol
Value
Number of UAVs
M
3
Number of GUs
K
9
Number of
subcarriers
N
3
Number of time
slots
T
60
Duration of each
time slot [33]
Ts
1s
Altitude of UAVs
hm(t)
[40m, 100m]
Maximum
acceleration of
UAVs [35]
amax
5m/s2
Maximum speed of
UAVs [35]
Vmax
20m/s
Safe distance
between UAVs [15]
dmin
25m
Maximum travel
distance of GUs
dmax
10m
UAV
aerodynamics
parameters [33]
ρ, A, δ, cS,
SF P , cT , cf
1.225kg/m3,
0.79m2,
0.012,
0.1,
0.01m2,
0.3,
0.13
Weight of the UAV
and gravitational
acceleration [33]
m′, ∥g∥
2kg, 9.8m/s2
Maximum power
of UAVs [15]
pmax
30dBm
Carrier frequency
[18]
fc
2GHz
Noise density [15]
σ2
-107dBm
MAHPPO-AM
algorithm
parameters [36]
lr, B, ¯
K, ¯
M, Ep,
γ, λ, ϵ, ζ
0.0001,
256,
20,
2048,
2000,
0.95,
0.95, 0.2, 0.001
where dk(t) and θk(t) are uniformly distributed in the
ranges of (0, dmax) and (0, 2π), respectively. dmax denotes
the maximum distance a mobile user can move in a time
slot. When a mobile user reaches the boundary of the area,
it will reverse its direction and continue moving within
the coverage area. To better simulate severe obstruction to
A2G links caused by ground buildings, two small areas are
randomly selected as obstructed areas in the initialization.
For default system parameters, Table I summarizes the
parameters used in the conducted numerical simulations.
In the proposed MAHPPO-AM algorithm, each actor
network consists of fully connected layers, where the first
two layers are the shared layers containing 256 and 128
neurons, respectively. Also, each output branch includes
2 layers, and the first layer contains 64 neurons, as well
as the structure of the last layer is determined by the
type and dimension of its corresponding actions. The critic
network consists of 4 fully connected layers containing 256,
128, 64, and 1 neuron, respectively.
For comparison, we adopt the following two schemes:
• Hybrid Proximal Policy Optimization (HPPO) [37]:

## Page 9

9
0
250
500
750
1000
1250
1500
1750
2000
Episode
1
2
3
4
5
6
7
Total Return
MAHPPO-AM
HPPO
Exploration
Fig. 3. Training process of the MAHPPO-AM algorithm and the two
baseline methods.
1
2
3
4
5
6
7
8
T
otal Return
0.00
0.02
0.04
0.06
0.08
0.10
0.12
0.14
MAHPPO -AM
HPPO
Exploration
Fig. 4.
Histogram of total return for the MAHPPO-AM algorithm
and the two baseline methods.
X
0
200
400
600
800
1000
1200
1400
Y
0
200
400
600
800
1000
1200
1400
Z
0
20
40
60
80
100
UE final location
UAV final location
UAV 1 trajectory
UAV 2 trajectory
UAV 3 trajectory
Fig. 5. 3D Trajectory of the UAV swarm.
0
200
400
600
800
1000
1200
1400
X
0
200
400
600
800
1000
1200
1400
Y
UE final location
UAV final location
UAV 1 trajectory
UAV 2 trajectory
UAV 3 trajectory
Fig. 6. 2D Trajectory of the UAV swarm.
As a single-agent algorithm, all UAVs share the same
actor network to generate the corresponding actions
simultaneously.
• Exploration: It has the same framework as the
MAHPPO-AM algorithm. Still, the agents only per-
form the current policy to interact with the environ-
ment and collect experience without gradient updates
on the policy parameters.
Fig. 3 shows the training process of the MAHPPO-
AM algorithm and the two baseline methods. The curves
are smoothed by taking the average of the five near-
est values at each point. The proposed MAHPPO-AM
method achieves optimal convergence performance over
2,000 training episodes, with its total return steadily
increasing from 3.5 to around 5. This trend suggests that
the proposed algorithm is effective in learning a policy
that balances the mobile users’ fair communication rates
and the UAVs’ energy consumption. In contrast, HPPO
eventually converges to a total return between 3 and
4, which reflects the limitations of a single agent when
dealing with UAV swarm collaboration. With total return
converging between 2 and 3, the Exploration method
demonstrates the ineffectiveness of just collecting data
without updating the policy parameters. Fig. 4 shows the
histograms obtained over 100-time simulation for the three
methods. According to the statistics, the average return
for the MAHPPO-AM, HPPO, and Exploration is 4.60,
2.82, and 2.80, respectively. These results show that the
MAHPPO-AM method performs relatively well in training
and simulation.
Fig. 5 and Fig. 6 depict the 3D trajectory and 2D tra-
jectory of the UAV swarm obtained by the MAHPPO-AM
method, respectively. And the gray area is the obstructed
area. The 3D trajectory provides a comprehensive view of
the UAV swarm’s spatial movement and altitude variation,
while the 2D trajectory clearly illustrates the swarm’s
coverage of mobile users and the spatial coordination
among UAVs. By comparing the two figures, UAV 1 and
UAV 2 can optimize their flight trajectory by minimizing
unnecessary travel distance and altitude adjustments while

## Page 10

10
0.04
0.06
0.08
0.10
0.12
0.14
0.16
Energy Efficiency (kbits/J)
0.0
0.2
0.4
0.6
0.8
1.0
CDF
T=40
T=50
T=60
T=70
T=80
Fig. 7. Energy eﬀiciency comparison for different T steps.
0.86
0.88
0.90
0.92
0.94
0.96
0.98
1.00
F
airness Index
0.0
0.2
0.4
0.6
0.8
1.0
CDF
MAHPPO -AM
HPPO
Exploration
0.996
0.998
1.000
0.6
0.8
1.0
Fig. 8.
Fairness index comparison for the MAHPPO-AM algorithm
and the two baseline methods.
TABLE II
ENERGY EFFICIENCY COMPARISON
Time Slots
T=40s
T=50s
T=60s
T=70s
T=80s
Energy Eﬀiciency
(kbits/J)
0.0978
0.0984
0.1024
0.0961
0.0979
maintaining communication quality, so as to reduce energy
consumption. The trajectories of the UAV swarm reflect
that the MAHPPO-AM method is able to intelligently
allocate the coverage area of UAVs based on the spatial
distribution of mobile users. Moreover, the UAV swarm is
capable of providing fair service for mobile users with lower
energy consumption, while avoiding situation in which
certain users cannot be served due to their presence in
obstructed areas.
Based on the proposed MAHPPO-AM method, Fig.
7 compares the cumulative distribution function (CDF)
of the average long-term energy eﬀiciency over 100-time
simulation for different T steps. As summarized in Table
II, the system achieves the optimal energy eﬀiciency when
T = 60s. It is worth noting that the energy eﬀiciency
instead decreases at T = 70s, which indicates that the
energy eﬀiciency is not positively correlated with T.
Overall, increasing T tends to enhance system energy
eﬀiciency, but T = 60s appears to be a threshold beyond
which further increases lead to performance degradation.
Therefore, we set T = 60s in our simulation experiments.
Fig. 8 illustrates the CDF of the fairness index over
100-time simulation, where the average fairness index for
the MAHPPO-AM, HPPO, and Exploration is 0.9888,
0.9887, and 0.9808, respectively. As shown in the figure,
the communication fairness of the three methods performs
well, largely due to the effectiveness of the action masking
applied during training. Although the average fairness
index of MAHPPO-AM and HPPO methods is nearly
identical, MAHPPO-AM performs more prominently in
the high-fairness interval. Specifically, when the fairness
14
15
16
17
18
19
20
21
22
Energy Consumption (kJ)
0.00
0.02
0.04
0.06
0.08
0.10
0.12
0.14
MAHPPO -AM
HPPO
Explo ation
Fig. 9.
Histogram of energy consumption for the MAHPPO-AM
algorithm and the two baseline methods.
index exceeds 0.99, the probability of MAHPPO-AM is
greater than that of the HPPO method. In contrast, the
fairness index of Exploration method is significantly infe-
rior to the proposed approach. These results demonstrate
that the proposed MAHPPO-AM method provides more
reliable communication services in high fairness demand
scenarios.
Fig. 9 displays the histograms of the energy con-
sumption over 100-time simulation obtained by differ-
ent methods, where the average energy consumption for
the MAHPPO-AM, HPPO, and Exploration is 14.88kJ,
19.86kJ, and 19.88kJ, respectively. As observed, the
MAHPPO-AM method reduces average energy consump-
tion by approximately 25% compared to the baseline
methods. Meanwhile, the energy consumption distribution
of MAHPPO-AM shows a sharp and narrow peak, indi-
cating that its energy consumption is also more stable.
The above results demonstrate that the MAHPPO-AM

## Page 11

11
method executes a more energy-eﬀicient policy.
V. Conclusion
This paper investigates a UAV swarm-assisted inte-
grated communication and control co-design mechanism to
enhance communication fairness and quality of service in
complex geographic environment. Considering the energy
constraints of UAV swarms, we formulate an objective
function that characterizes the trade-off between the
fairness-constrained communication rates for ground users
and UAVs’ energy consumption. We model the UAV
swarm’s resource allocation and 3D trajectory control as
a Markov decision process and propose a multi-agent RL
framework as a solution, which facilitates decision-making
on collaborative actions among UAVs in real time. To
address hybrid action space challenges in UAV swarms, we
propose a novel MAHPPO-AM algorithm that guarantees
hard constraints in high-dimensional action spaces via
action masking. The simulation results show that our
approach achieves a fairness index of 0.99 while reducing
energy consumption by up to 25% compared to baseline
methods.
References
[1] Zeng Y, Wu Q, Zhang R, “Accessing From the Sky: A Tutorial
on UAV Communications for 5G and Beyond,”Proceedings of the
IEEE. 2019, 107(12): 2327–2375.
[2] Luo Q, Luan T H, Shi W, Fan P, “Deep Reinforcement Learn-
ing Based Computation Offloading and Trajectory Planning
for Multi-UAV Cooperative Target Search”, IEEE Journal on
Selected Areas in Communications. 2023, 41(2): 504–520.
[3] Sun W-B, Zhao L, Yang X, Wang L, Meng W-X, “Joint
Topology Reconstruction and Resource Allocation for UAV-IoT
Networks,”IEEE Internet of Things Journal, 2024: 1–1.
[4] Ning Z, Yang Y, Wang X, Song Q, Guo L, Jamalipour A, “Multi-
Agent Deep Reinforcement Learning Based UAV Trajectory
Optimization for Differentiated Services,”IEEE Transactions on
Mobile Computing, 2023: 1–17.
[5] A. Bera, S. Misra, C. Chatterjee and S. Mao, “CEDAN: Cost-
Effective Data Aggregation for UAV-Enabled IoT Networks,”
IEEE Transactions on Mobile Computing, vol. 22, no. 9, pp.
5053-5063, 1 Sept. 2023, doi: 10.1109/TMC.2022.3172444.
[6] Xing R, Su Z, Luan T H, Xu Q, Wang Y, Li R, “UAVs-Aided
Delay-Tolerant Blockchain Secure Offline Transactions in Post-
Disaster Vehicular Networks,” IEEE Transactions on Vehicular
Technology,2022, 71(11): 12030–12043.
[7] Gaydamaka A, Samuylov A, Moltchanov D, Ashraf M, Tan B,
Koucheryavy Y, “Dynamic Topology Organization and Main-
tenance Algorithms for Autonomous UAV Swarms,” in IEEE
Transactions on Mobile Computing, 2023: 1–17.
[8] Wu Q, Xu J, Zeng Y, Ng D W K, Al-Dhahir N, Schober
R, Swindlehurst A L, “A Comprehensive Overview on 5G-
and-Beyond Networks With UAVs: From Communications to
Sensing and Intelligence,” IEEE Journal on Selected Areas in
Communications, 2021, 39(10): 2912–2945.
[9] Zhou Z, Zhuang Y, Li H, Huang S, Yang S, Guo P, Zhong L,
Yuan Z, Xu C. MR-FFL, “A Stratified Community-Based Mutual
Reliability Framework for Fairness-Aware Federated Learning
in Heterogeneous UAV Networks,”in IEEE Internet of Things
Journal, 2024: 1–1.
[10] C. Qiu, Z. Wei, X. Yuan, Z. Feng, and P. Zhang, “Multiple UAV-
mounted base station placement and user association with joint
fronthaul and backhaul optimization,” IEEE Trans. Commun.,
vol. 68, no. 9, pp. 5864–5877, Sep. 2020.
[11] C. Shen, T.-H. Chang, J. Gong, Y. Zeng, and R. Zhang, “Multi-
UAV interference coordination via joint trajectory and power
control,” IEEE Trans. Signal Process., vol. 68, pp. 843–858, 2020.
[12] X. Liu, B. Lai, B. Lin, and V. C. M. Leung, “Joint communica-
tion and trajectory optimization for multi-UAV enabled mobile
Internet of Vehicles,” IEEE Trans. Intell. Transp. Syst., vol. 23,
no. 9, pp. 15354–15366, Sep. 2022.
[13] L. Zhu, J. Zhang, Z. Xiao, X.-G. Xia, and R. Zhang, “Multi-
UAV aided millimeter-wave networks: Positioning, clustering,
and beamforming,” IEEE Trans. Wireless Commun., vol. 21, no.
7, pp. 4637–4653, Jul. 2022.
[14] R. Zhang, Y. Zhang, R. Tang, H. Zhao, Q. Xiao and C. Wang,
“A Joint UAV Trajectory, User Association, and Beamforming
Design Strategy for Multi-UAV-Assisted ISAC Systems,” IEEE
Internet of Things Journal, vol. 11, no. 18, pp. 29360–29374, 15
Sept. 2024, doi: 10.1109/JIOT.2024.3430390.
[15] P. Yi, L. Zhu, Z. Xiao, R. Zhang, Z. Han and X.-G. Xia, “3-D Po-
sitioning and Resource Allocation for Multi-UAV Base Stations
Under Blockage-Aware Channel Model,” IEEE Transactions on
Wireless Communications, vol. 23, no. 3, pp. 2453–2468, March
2024, doi: 10.1109/TWC.2023.3300332.
[16] X. Liu, M. Chen, Y. Liu, Y. Chen, S. Cui and L. Hanzo,
“Artificial Intelligence Aided Next-Generation Networks Relying
on UAVs,” IEEE Wireless Communications, vol. 28, no. 1, pp.
120–127, February 2021, doi: 10.1109/MWC.001.2000174.
[17] S. Yin and F. R. Yu, “Resource Allocation and Trajectory De-
sign in UAV-Aided Cellular Networks Based on Multiagent Rein-
forcement Learning,” IEEE Internet of Things Journal, vol. 9, no.
4, pp. 2933–2943, 15 Feb. 2022, doi: 10.1109/JIOT.2021.3094651.
[18] R. Zhong, X. Liu, Y. Liu and Y. Chen, “Multi-Agent Rein-
forcement Learning in NOMA-Aided UAV Networks for Cel-
lular Offloading,” IEEE Transactions on Wireless Commu-
nications, vol. 21, no. 3, pp. 1498–1512, March 2022, doi:
10.1109/TWC.2021.3104633.
[19] W. J. Yun et al., “Cooperative Multiagent Deep Reinforcement
Learning for Reliable Surveillance via Autonomous Multi-UAV
Control,” IEEE Transactions on Industrial Informatics, vol. 18,
no. 10, pp. 7086–7096, Oct. 2022, doi: 10.1109/TII.2022.3143175.
[20] X. Wang, M. Yi, J. Liu, Y. Zhang, M. Wang, and B. Bai,
“Cooperative data collection with multiple UAVs for information
freshness in the Internet of Things,” IEEE Trans. Commun., vol.
71, no. 5, pp. 2740–2755, May 2023.
[21] Q. Gao, R. Zhong, H. Shin and Y. Liu, “MARL-Based UAV
Trajectory and Beamforming Optimization for ISAC System,” in
in IEEE Internet of Things Journal, vol. 11, no. 24, pp. 40492-
40505, 15 Dec.15, 2024, doi: 10.1109/JIOT.2024.3453195.
[22] S. Xu, X. Zhang, C. Li, D. Wang, and L. Yang, “Deep
reinforcement learning approach for joint trajectory design in
multi-UAV IoT networks,” IEEE Trans. Veh. Technol., vol. 71,
no. 3, pp. 3389–3394, Mar. 2022.
[23] K. Li, W. Ni, Y. Emami, and F. Dressler, “Data-driven flight
control of Internet-of-Drones for sensor data aggregation using
multi-agent deep reinforcement learning,” IEEE Wireless Com-
mun., vol. 29, no. 4, pp. 18–23, Aug. 2022.
[24] J. Ji, K. Zhu, and L. Cai, “Trajectory and communication
design for cache-enabled UAVs in cellular networks: A deep
reinforcement learning approach,” IEEE Trans. Mobile Comput.,
vol. 22, no. 10, pp. 6190–6204, Oct. 2023.
[25] Z. Bai, J. Shi, Z. Li, M. Li and X. Liao, “An MA-HPPO
Approach for Multi-UAV Data Collection,” IEEE Transactions
on Wireless Communications, vol. 23, no. 12, pp. 17974–17986,
Dec. 2024, doi: 10.1109/TWC.2024.3458194.
[26] “Technical Specification Group Radio Access Network; Study
on Enhanced LTE Support for Aerial Vehicles,” 36.777, 3GPP,
2018, version 15.0.0.
[27] J. Lyu, Y. Zeng, and R. Zhang, “UAV-aided offloading for
cellular hotspot,” IEEE Trans. Wireless Commun., vol. 17, no.
6, pp. 3988–4001, Jun. 2018.
[28] C. H. Liu, Z. Chen, J. Tang, J. Xu, and C. Piao, “Energy-
eﬀicient UAV control for effective and fair communication cov-
erage: A deep reinforcement learning approach,” IEEE J. Sel.
Areas Commun., vol. 36, no. 9, pp. 2059–2070, Sep. 2018.
[29] R. K. Jain, D.-M. W. Chiu, and W. R. Hawe, “A quantitative
measure of fairness and discrimination,” Eastern Res. Lab., Digit.
Equip. Corp., Hudson, MA, USA, 1984.
[30] Y. Zeng and R. Zhang, “Energy-eﬀicient UAV communication
with trajectory optimization,” IEEE Trans. Wireless Commun.,
vol. 16, no. 6, pp. 3747–3760, Jun. 2017.

## Page 12

12
[31] S. Huang and S. Ontañón, “A Closer Look at Invalid Action
Masking in Policy Gradient Algorithms,” FLAIRS, vol. 35, May
2022.
[32] J. Schulman, S. Levine, P. Abbeel, M. I. Jordan, and P. Moritz,
“Trust region policy optimization,” in Proc. Int. Conf. Mach.
Learn. (ICML), Lille, France, Jul. 2015, pp. 1889–1897.
[33] X. Dai, B. Duo, X. Yuan and M. D. Renzo, “Energy-Eﬀicient
UAV Communications in the Presence of Wind: 3D Modeling
and Trajectory Design,” IEEE Transactions on Wireless Com-
munications, vol. 23, no. 3, pp. 1840–1854, March 2024, doi:
10.1109/TWC.2023.3292290.
[34] J. Schulman, P. Moritz, S. Levine, M. I. Jordan, and P.
Abbeel, “High-dimensional continuous control using generalized
advantage estimation,” in Proc. Int. Conf. Learn. Represent.
(ICLR), San Juan, Puerto Rico, May 2016.
[35] R. Ding, F. Gao and X. S. Shen, “3D UAV Trajectory Design
and Frequency Band Allocation for Energy-Eﬀicient and Fair
Communication: A Deep Reinforcement Learning Approach,” in
IEEE Transactions on Wireless Communications, vol. 19, no. 12,
pp. 7796-7809, Dec. 2020, doi: 10.1109/TWC.2020.3016024.
[36] Z. Hao, G. Xu, Y. Luo, H. Hu, J. An and S. Mao,“Multi-
Agent Collaborative Inference via DNN Decoupling: Intermediate
Feature Compression and Edge Learning,” in IEEE Transactions
on Mobile Computing, vol. 22, no. 10, pp. 6041-6055, 1 Oct. 2023,
doi: 10.1109/TMC.2022.3183098.
[37] Z. Fan, R. Su, W. Zhang et al., “Hybrid Actor-Critic Reinforce-
ment Learning in Parameterized Action Space,” in Proc. Int.
Joint Conf. Artif. Intell. (IJCAI), 2019.
