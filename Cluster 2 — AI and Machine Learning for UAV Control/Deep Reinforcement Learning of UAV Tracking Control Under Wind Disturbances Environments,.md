# Deep Reinforcement Learning of UAV Tracking Control Under Wind Disturbances Environments,.pdf

## Page 1

IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 72, 2023
2510913
Deep Reinforcement Learning of UAV Tracking
Control Under Wind Disturbances Environments
Bodi Ma , Member, IEEE, Zhenbao Liu , Senior Member, IEEE, Qingqing Dang , Wen Zhao ,
Jingyan Wang , Yao Cheng , and Zhirong Yuan
Abstract— Aiming at the problems of strong nonlinearity,
strong coupling, and unknown interference encountered in the
flight control process of unmanned aerial vehicles (UAVs) in
a complex dynamic environment and reinforcement-learning-
based algorithm generalization, this study presents an innovative
incremental reinforcement-learning-based algorithm for UAV
tracking control in a dynamic environment. The main goal is
to make a UAV able to adjust its control policy in a dynamic
environment. The UAV tracking control task is transformed
into a Markov decision process (MDP) and further investigated
using an incremental reinforcement-learning-based method. First,
a policy relief (PR) method is used to make UAVs capable of
performing an appropriate exploration in a new environment.
In this way, a UAV controller can mitigate the conflict between
a new environment and the current knowledge to ensure better
adaptability to a dynamic environment. In addition, a significance
weighting (SW) method is developed to improve the utilization of
episodes with higher importance and richer information. In the
proposed method, learning episodes that include more useful
information are assigned with higher importance weights. The
numerical simulation, hardware-in-the-loop (HITL) experiments,
and real-world flight experiments are conducted to evaluate the
performance of the proposed method. The results demonstrate
high accuracy and effectiveness and good robustness of the
proposed control algorithm in a dynamic flight environment.
Manuscript
received
22
November
2022;
revised
12
March
2023;
accepted 25 March 2023. Date of publication 11 April 2023; date of current
version 2 May 2023. This work was supported in part by the National Natural
Science Foundation Fund under Grant 52072309, in part by the Key Research
and Development Program of Shaanxi Province under Grant 2019ZDLGY14-
02-01, in part by the Shenzhen Fundamental Research Program under Grant
JCYJ20190806152203506, in part by the Aeronautical Science Founda-
tion of China under Grant ASFC-2018ZC53026, in part by the Beijing
Institute of Spacecraft System Engineering Research Project under Grant
JSZL2020203B004, in part by the Innovation Foundation for Doctor Dis-
sertation of Northwestern Polytechnical University under Grant CX2021033,
in part by the Basic Research Program of Taicang under Grant TC2021JC09,
and in part by the Natural Science Foundation of Shaanxi Province under
Grant 2023-JC-QN-0003 and Grant 2023-JC-QN-0665. The Associate Editor
coordinating the review process was Dr. Mohamad Forouzanfar. (Correspond-
ing author: Zhenbao Liu.)
Bodi Ma, Qingqing Dang, and Wen Zhao are with the School of
Civil
Aviation,
Northwestern
Polytechnical
University,
Xi’an
710072,
China
(e-mail:
mabodi@mail.nwpu.edu.cn;
dangqingqing@nwpu.edu.cn;
zhaowen@nwpu.edu.cn).
Zhenbao
Liu
is
with
the
School
of
Civil
Aviation,
Northwestern
Polytechnical University, Xi’an 710072, China, and also with the Research and
Development Institute in Shenzhen, Northwestern Polytechnical University,
Shenzhen 518071, China (e-mail: liuzhenbao@nwpu.edu.cn).
Jingyan
Wang
and
Yao
Cheng
are
with
the
Beijing
Institute
of
Spacecraft
System
Engineering,
Beijing
100094,
China
(e-mail:
wangjingyan.npu@gmail.com; chengyao.012@gmail.com).
Zhirong Yuan is with the 365 Institute, Northwestern Polytechnical
University, Xi’an 710072, China (e-mail: yzhirong@tom.com).
Digital Object Identifier 10.1109/TIM.2023.3265741
Index Terms— Dynamic environment, reinforcement learn-
ing, tracking control, unmanned aerial vehicles (UAVs), wind
disturbances.
I. INTRODUCTION
U
NMANNED aerial vehicles (UAVs) have gained growing
attention in the commercial and industrial fields owing
to their characteristics of strong maneuverability, economi-
cal cost, and rapid development [1], [2], [3]. Also, due to
these conveniences, UAVs have been widely applied in many
applications, including traffic analysis, logistics and trans-
portation, and resource exploration [4], [5], [6]. According to
the differences in vehicle frame and flight mode, UAVs can
be roughly divided into multirotor UAVs, fixed-wing UAVs,
and flapping-wing aircraft [7], [8], [9]. Multirotor UAVs have
the advantages of lightness, compactness, maneuverability,
convenient take-off and landing, and an ability to realize aerial
hovering and stable low-altitude flight, making them become
one of the most widely applied aircraft.
To ensure UAV can achieve desired flight missions, a grow-
ing amounts of researches have been attracted to the imple-
mentation and application of robust UAV controller [4], [10],
including proportional–integer–derivative (PID) control, the
active disturbance rejection control (ADRC) control algorithm,
the robust H∞control theory, and so on. In practical engi-
neering, the traditional PID solution has been widely applied
due to its robust and feasible characteristics. In [11], the
gain scheduled PID algorithm for UAV attitude control was
proposed; this algorithm can ensure a stable system state
during the transition phase. In addition, Rosale et al. [12]
designed a novel adaptive PID controller and applied an
extended Kalman filter algorithm to filter the measurement
errors, but its performance can degrade in a highly nonlinear
control system. Certain improvements have been made to
enhance the control accuracy. The controller proposed in [13]
used a fuzzy mechanism to adjust controlled gains at various
phases adaptively for speeding up the convergence. Yu et al.
[14] proposed an adaptive sliding mode controller which has
been designed to compensate for compound uncertainties from
a nonlinear dynamic system. In [15], the Euler–Lagrange
mechanical equation was used to derive and estimate the influ-
ences of UAV control model uncertainty. The novel sliding
mode control method was proposed to ensure the robustness
and accuracy of a controller. LaValle et al. [16] proposed the
random trees method to handle the path-planning problem and
1557-9662 © 2023 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 10:16:54 UTC from IEEE Xplore.  Restrictions apply.

## Page 2

2510913
IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 72, 2023
speed up the exploration process. The scientist, Sanyal pro-
posed the efficient and robust control strategy which developed
the controller based on the special Euclidean group of rigid
body motions, using SE(3) methodology [17], [18]. Xu et al.
[19] proposed a cascade ADRC (CADRC) algorithm, which
implemented a supplementary high-gain design parameter in
the CADRC model. In [20], the adaptive fast terminal sliding
mode controller was implemented to track the desired path of
multirotor aircraft, which used a nonlinear fast terminal sliding
surface to eliminate tracking errors and attenuate fluctuations.
The wind disturbances in the outdoor flight area denote
an inevitable issue which has a significant influence on the
accuracy of UAV flight control. Many research works have
engaged to address this problem. An adaptive control scheme
and a robust controller have been implemented in [21], where a
synthesized control framework was used to eliminate the wind
disturbances by air drag. Song et al. [1] proposed an innovative
sliding mode control strategy, where the optimized radial basis
function was used to increase the disturbances rejection. Sim-
ulation experiments and real-world tests were carried out to
corroborate the control performance. In [22], an efficient slid-
ing model control method was proposed, where the adaptive
control law was used to eliminate the disturbances. Chen et al.
[4] designed an optimized adaptive sliding mode control for
multirotor UAVs. The double-layer sliding mode structure was
used to estimate the wind disturbances and eliminate tracking
errors. Traditional flight control technologies, such as PID
control and sliding mode control, have achieved good control
effects in practical engineering tasks and can ensure a certain
accuracy of trajectory and attitude control. However, in the
face of flight control tasks with high real-time requirements
and highly dynamic environment, the existing technology still
has many defects and challenges caused by a strong reliance
on models and the difficulty in the flexible real-time correc-
tion of control strategy presets. As flight missions become
more and more complicated, the strong nonlinearity of flight
environment and the UAV dynamics models have more and
more serious impacts on precise control. Compared with the
traditional control strategies, artificial-intelligence-based con-
trol technology has obvious advantages regarding the accuracy,
model dependence, real-time performance and predictability
and plays an increasingly important role in the field of UAV
wind resistance and high-precision flight control. It has been a
strategic technology leading the further development of UAV.
Deep neural network has strong capacities for handling the
nonlinear control system [10]. Moon et al. [23] developed a
deep reinforcement learning (DRL)-based tracking controller
for UAV. The global reward and difference reward functions
were deduced for estimating the contribution of each air-
craft in the entire system. Thus, the agents were able to
receive a high-resolution measurement signal for improving
the accuracy of tracking controller. Wu et al. [24] proposed
a fixed-wing UAV decision making mechanism which is
composed by interfered fluid dynamical system guidance law,
back-stepping control loops, and learning-based maneuver
controller. The classical control theory, linear ADRC method
is implemented to eliminate the external disturbances. The
relevant simulations are conducted to test the performance of
the proposed method in the obstacle environment. In [25],
the data-driven UAV navigation method is proposed. In this
framework, the UAV is assumed to fly at the same altitude in
the 2-D environment. The A* algorithm is used which gener-
ated the training samples under wind disturbances. The DRL
model is implemented to learn the navigation solution for UAV.
Birnbaum et al. [26] proposed the UAV health monitoring
and security system to enhance UAVs’ control performance
under various external environments. By detecting significant
changes, such as wind weather, in the flight, the predefined
actions can be activated to address the external disturbances.
In [27], the DRL-based landing control method for fixed-wing
UAV is proposed. The learning-based model is trained in the
wind environment to learn the control policy under external
disturbances. Kaifang et al. [28] proposed a maneuver con-
troller for UAV in dynamic unknown environments, using the
reinforcement learning solution. The Markov decision process
(MDP) combined with the Lyapunov guidance vector field
framework is established to describe the flight control model
in the target tracking and motion planning flight mission,
and certain improvements were achieved in simulation exper-
iments. Kaushik et al. [29] proposed a DRL framework for
handling a UAV formation control mission. The innovative
reward function was deduced to ensure collision avoidance in
formation flight, and a cooperation tracking strategy was used
for tracking the target with cooperative information. In [30],
a transfer learning-based algorithm was implemented in a
DRL-based framework to enable a UAV to use the learning
knowledge without retraining. The learning efficiency was
verified by the simulation tests.
To solve the above-mentioned problems, this work intro-
duces a novel reinforcement-learning-based UAV tracking
control algorithm under wind disturbances. A policy relief
(PR) algorithm is proposed to encourage the exploration,
and a significance weighting (SW) method is developed for
making drones be better adapted to dynamic environments.
The random wind disturbance signal has been implemented
on numerical dynamic environment in the learning process
for improving the robustness of the controller. Furthermore,
a novel reward function is designed, which can increase the
learning efficiency. In all, this article is developed to study
the multirotor aircraft tracking control problem under wind
disturbances using reinforcement learning methodology. The
contribution includes the following. The main contributions
of this study can be summarized as follows.
1) This work provides a new DRL-based UAV tracking
control method under wind disturbances. To make the
controller be adjustable and robust when there are
changes and disturbances in flight area, the PR mech-
anism is designed to encourage proper exploration in
learning phase, which lessens the imbalances between
the new knowledge and learning knowledge. Moreover,
the SW method is proposed for ensuring the UAV be
faster and better adapted to various changes.
2) This study analyzes the characteristics of the whole
stage of the tracking flight control task. To
achieve
optimal performance, a novel reward function is pro-
posed, including sparse reward item to enhance the
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 10:16:54 UTC from IEEE Xplore.  Restrictions apply.

## Page 3

MA et al.: DRL OF UAV TRACKING CONTROL UNDER WIND DISTURBANCES ENVIRONMENTS
2510913
Fig. 1.
Flow diagram of the proposed reinforcement-learning-based control
algorithm in dynamic environments.
diversity of flight data and increase the efficiency of
learning process.
3) Comparative experiments and analysis, including numer-
ical simulation, hardware-in-the-loop (HITL) test, and
real-world flight experiments, are conducted to verify
the merits of the proposed tracking control algorithm
compared with latest relative solutions. The experimen-
tal results demonstrate that the proposed algorithm is
satisfactory in practical engineering with high accuracy
and good robustness.
The rest of this article is organized as follows. Section II
describes the proposed method, introducing specific improve-
ments and providing technical details. Section III presents the
experimental results and analysis. Finally, Section IV presents
conclusions.
II. INCREMENTAL REINFORCEMENT LEARNING BASED
UAV CONTROL
This section presents the innovative reinforcement-learning-
based UAV control algorithm that enables a UAV to learn a
control strategy by interaction with a dynamic environment.
The problem of UAV tracking control is formulated as an
MDP problem, and a novel deep deterministic policy gradient
(DDPG) algorithm is used to construct a UAV tracking control
model. The state space, action space, and reward function
are presented. The incremental-learning-based mechanism is
implemented into an RL-based controller to make a UAV
adjustable to a dynamic environment. To enhance the robust-
ness and stability of a UAV under unknown disturbances, the
DDPG tracking control framework is optimized by PR and
SW. Fig. 1 illustrates the process of the proposed method.
A. Problem Description
In this study, an innovative DDPG-based control algorithm
has been used to solve the MDP problems with continuous
actions. By representing the policy as a policy function,
a deterministic policy gradient method can map a state to a
deterministic action. In this study, external disturbances are
regarded as changes in a flight environment, and changes
in environments have been formulated as a series of split
tasks in time series where each task correlates with a specific
characteristic in the correlated time series. The state transition
function has drift during changes in an environment, but
the state and action spaces remain the same. Assume that a
dynamic environment set D is D = [E1, . . . , Et−1, Et, . . .],
where Et represents a specific characteristic of a dynamic
environment at the tth time frames. The main purpose of an
RL-based model is to generate an optimal control strategy
that can maximize the desired persistent reward J(θ) under
parameter θ. The desired long-term reward is expressed as
follows:
J(θ) = Eϵ∼π(ϵ)[r(ϵ)] = Eϵ∼π(ϵ)
" ∞
X
i=0
γ iri
#
(1)
where ϵ = {s0, a0, s1, a1, . . .} means a training episode, ri is
the immediate reward after interaction with an environment,
and γ is the discount factor. According to the theorem of
policy gradient, the formula for the basic policy gradient
algorithm is defined by the following equation:
∇θ J(πθ) =
Z
ϵ
∇θπθ(s)∇a Qπ(s, a)

a=πθ(s)
dϵ
= Es∼πϵ

∇θπθ(s)∇a Qπ(s, a)|a=πθ(s)

.
(2)
During the time of the learning process, the policy approxi-
mation is implemented to optimize the parameters of model,
which can be expressed as follows:
θ∗
t−1 = arg max
θ∈Rd
JEt−1(πθ).
(3)
The external disturbances are described as changes in
environmental characteristic. The function of the designed
incremental learning method is to enable a UAV to update its
parameters θ∗
t−1 to an optimized value θ∗
t automatically when
the environment characteristics transfer into Et at the tth time
θ∗
t = arg max
θ∈Rd
JEt(πθ).
(4)
In this way, an agent is able to update its existing knowl-
edge according to the changes in a dynamic environment.
An innovative reinforcement learning control method is inte-
grated with the incremental learning process for the UAV
control, which includes PR and an SW mechanism. The
detailed implementations are demonstrated in Section II-C and
Section II-D.
B. Design of System State and Reward Function
A reinforcement-learning-based control strategy, which
enables a UAV to track the target accurately, is
developed.
In the flight mission, the movement relationship between a
UAV and a target plays an imperative part in the control
strategy design. The 10-D vector S∗
t is used to represent the
state of the current UAV which is chasing the target in a flight
task, and it is given by the following equation:
S∗
t = {1Pt, 18t, 1Vt, Bt}T ∈R10.
(5)
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 10:16:54 UTC from IEEE Xplore.  Restrictions apply.

## Page 4

2510913
IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 72, 2023
S∗
t could be divided into several subset vectors. 1Pt =
(1x, 1y, 1z) means the relative distance between the current
vehicle and the target in three axes. 18c = (1φ, 1θ, 1ψ)
represents the relative attitude angle, including roll, pitch, and
yaw. The relative velocity between the UAV and the target is
denoted as Vc = (vx, vy, vz), and Bc is the battery state of the
vehicle. Considering the kinematic relationship between the
UAV and the target in tracking flight, as well as the past flight
state, we define the tracking control state as follows:
St =

S∗
t , S∗
t−1, S∗
t−2, S∗
t−3
	T ∈R40.
(6)
The state space in the designed tracking control model contains
the current flight state and past three history state data frames.
A multirotor aircraft is mainly controlled by the pulling force
of the rotors. By changing the rotation speed of the front and
rear rotors, the rotation speed difference is generated, and the
pitch control is realized through the differential. Therefore, the
action space could be expressed as a = {u1, u2, u3, u4, u5, u6},
where ui means the rotating speed of a rotor i.
The proper design of the reward function is one of the most
crucial factors in the RL-based model construction process.
An effective reward function can provide a faster convergence
and a better performance in experiments. This study analyzes
the characteristics of the whole stage of the tracking flight
control task. To reach the optimal performance, a novel reward
function, including state deviation value, energy consumption,
and sparse reward obtained when a vehicle is reaching the
target interval, is designed as follows:
rt = −(w1|1Pt| + w2|18t| + w3|1Vt|
+ w4|Bt −Bt−1|) + r+
P + r+
V
(7)
where wi denotes the weight of the corresponding terms.
Immediate reward implements deviation value as a penalty
item, including position deviation, velocity deviation, and
attitude angle deviation. When the control performance is not
adequate, the penalty item will be large, and the penalty value
will approach zero when an aircraft approaches the steady
state. Setting an immediate reward in this form demonstrates
that the agent’s policy goal is to control a UAV to fly stably at
a steady-state point throughout the flight mission. r+
P , r+
V , and
r−
done denote the sparse reward items improving the sample
diversity of flight data and enhancing the learning efficiency
of the agent.
C. PR Method
In a dynamic changing environment, the reinforcement-
learning-based control model tends to use a local optimum
instead of the whole state–action space, which may lead
the model to fall into a local optimum [31]. The reason
for this is that an agent has insufficient exploration during
in the learning process, and its parameters are overfitted to
the existing environment. To make an agent be adjustable
to the environmental changes and strengthen an appropriate
exploration, this study designs a PR method. In particular, θ
represents the current parameter set of an action network in an
environment Et, and πθ is the policy derived from the current
parameters. Thus, the PR strategy is designed as follows:
πr(a | s) =
(
Un(A(s)),
η ≤k
πθ(a | s),
η > k
(8)
where η = η0 ∗0.999λ, representing the PR probability, where
η0 is the initial probability of the PR mechanism, and λ is
the number of training steps; k is the presetting probability
threshold. When η > k, the action is generated by the current
policy πθ; otherwise, the action is calculated by the uniform
distribution Un(A(s)), where A(s) is the available action set
corresponding to the state space.
To make the PR mechanism practicable and unbiased, the
general statistic technique [32] and importance sampling [33]
are implemented to calculate the policy gradient. Think of
the object of reinforcement-learning-based model in (1), and
r(ϵ) = P∞
i=0 γ iri is the entire reward of an episode ϵ. In the
PR mechanism, it is in necessary to evaluate the expected value
of r(ϵ) under the initial distribution of ϵ ∼πθ(ϵ), while it is
going to sample from a novel policy distribution ϵ ∼πr(ϵ) in
the dynamic changing environment. Therefore, the inspection
of importance sampling is given as follows:
Eϵ∼πθ(ϵ)[r(ϵ)] =
Z
ϵ
πθ(ϵ)r(ϵ)dϵ
=
Z
ϵ
πθ(ϵ)
πr(ϵ)r(ϵ)πr(ϵ)dϵ
= Eϵ∼πr(ϵ)
πθ(ϵ)
πr(ϵ)r(ϵ)

.
(9)
Furthermore, the calculation process of the policy gradient is
rewritten as follows:
∇θ J(θ) = Eϵ∼πr(ϵ)
πθ(ϵ)
πr(ϵ)∇θπθ(ϵ)∇a Qπθ(ϵ)

.
(10)
The design of the PR mechanism is inspired by the con-
ventional RL technique named the epsilon-greedy exploration.
The action policy is implemented to incorporate certain types
of random actions that can enhance the exploration of an agent.
This study is inspired by the epsilon-greedy algorithm and
purposes an appropriate exploration strategy for the implemen-
tation of THE policy gradient method. To achieve a tradeoff
between exploration and exploitation, a significance sampling
mechanism is developed to achieve collaboration with the PR
method.
D. SW Method
The control strategy obtained from the existing environ-
ments may provide a modest performance in a dynamic
changing environment since its parameters have learned the
knowledge about characteristics from the original environ-
ment, and the policy may not be optimal for new environment.
However, direct application of parameters may decrease the
performance of an agent in the long term when interacting with
a new environment because initializing the neural networks
parameters may cause them to fall into a local optimal point
which is overfitted to the previous environments [34], [35],
[36]. In addition, parameters may transfer from current local
optimal point to another, because the optimization can be
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 10:16:54 UTC from IEEE Xplore.  Restrictions apply.

## Page 5

MA et al.: DRL OF UAV TRACKING CONTROL UNDER WIND DISTURBANCES ENVIRONMENTS
2510913
influenced by pathological curves. In the learning process,
the model tends to perform the action that is feasible for
the existing environment. This is because an agent has to be
trained to have the prior knowledge necessary for handling
the problems in the previous environment. Therefore, it is
essential to make an agent be adjustable to the environmental
changes. In the dynamic environment, the example episodes
may not achieve the optimal performance because their param-
eters are updated based on information from the previous
environment. Different episodes may obtain various rewards
under a dynamic environment. The training episodes with
more rewards are supposed to have more importance and
more information in the learning process [35], [37]. Therefore,
in this study, a higher weight is assigned to episodes with a
higher reward value, which is beneficial for improving the
convergence speed of the model. Inspired by the mentioned
perception and related literature, the representation of designed
significance weight is given by the following equation:
w
ϵi
= 1
ρ
r
ϵi
+ ξ

,
i = 1, . . . , n
(11)
where the ξ is a tiny mathematical constant, n is the number
of samples in a mini-batch, and ρ is the normalization item
making the weight metric of mini-batch equivalent to one.
Based on the DDPG theorem [38], the direct gradient ascent
function in (2) can be rewritten as follows:
∇θ J(θ) = Eϵ∼πr(ϵ)

w(ϵ)∇θπθ(ϵ)∇a Qπθ (ϵ)

.
(12)
Based on the above SW method, an agent can update its
parameters tending to the region of parameter space that is
more appropriate for the current dynamic environment.
E. Integrated Method
Algorithm 1 demonstrates how the designed incremen-
tal reinforcement learning method works for UAV control
in dynamic environments. Wind disturbance is regarded as
changes in the environment, and the controller is designed so
that it can adjust its characteristic in a dynamic environment
using the above-mentioned method. A random wind distur-
bance signal has been implemented on numerical dynamic
environment in the learning process. The model is designed
to be able to interact with various environments represented
as a set D = [E1, . . . , Et−1, Et, . . .], where Et denotes a
type of wind disturbance characteristic at the tth time series.
In the first interaction with the environment, an agent learns
the original policy through a standard policy gradient strategy,
as presented in lines 2 and 3. During the following interaction
phase, the neural network parameters are initialized based
on the learned policy, which is optimal for the preceding
environment, as shown in line 5. In this way, the agent is able
to directly use the information from the previous environment
since it has learned the basic feature representation of the
environment and state–action spaces. Then, the PR algorithm
is implemented to achieve an appropriate exploration with
higher diversity, as given in line 6. To improve the convergence
speed of the learning process, the SW method is adopted to
assign higher significance weights to the samples accomplish-
ing with higher total rewards, as demonstrated in lines 7 and 9.
Algorithm 1 Incremental Reinforcement-Learning-Based
UAV Control Method in Dynamic Environment
Input: Environment serialsD = [E1, . . . , Et−1, Et, . . .]; current
time step t(>0); parameter set;
Output: Optimal policy parameters
Data: Testing set x
1 if t equals to 1 then
2
Initialize the parameters from beginning
while no converged do
3
Sampled m episodes:
∇θ J(θ) = Eϵ∼πr (ϵ)[w(ϵ)∇θπθ(ϵ)∇a Qπθ (ϵ)]
θ t ←θ t + α∇θt J(θ t)
4 else
5
Update the training episodes η ←0
Update the parameter set
while no converged do
6
if η ≤k then
7
πr(a | s) = Uniform (A(s)), ∀s
Select m samples from πr
Calculate the significance weights for learning
episodes by (11)
∇θ J(θ) = Eϵ∼πr (ϵ)[w(ϵ) πθ (ϵ)
πr (ϵ) ∇θπθ(ϵ)∇a Qπθ (ϵ)]
8
else
9
Select m samples from πθ
Calculate the significance weights for learning
episodes by (11)
∇θ J(θ) = Eϵ∼πr (ϵ)[w(ϵ)∇θπθ(ϵ)∇a Qπθ (ϵ)]
10
θ t ←θ t + α∇θt J(θ t)
η ←η + m
u ←u + 1u
Furthermore, the policy networks’ parameters are updated in
proportion to achieve the gradient till convergence, as shown
in line 10. Finally, the policy suitable for dynamic changing
environment is obtained.
III. EXPERIMENTAL RESULTS
To evaluate the performance of the proposed incremental
reinforcement-learning-based UAV control strategy in dynamic
changing environments, a series of experiments were per-
formed, including numerical simulation test, multiple wind
disturbance tests, HITL experiments, and a real-world flight
test. In addition, to investigate the designed reinforcement-
learning-based control algorithm further, it was compared with
several state-of-the-art techniques, including the RL-based
method and classic control method. Two evaluation criteria—
root mean square error (RMSE) indicators and maximum
(MAX) indicators of tracking errors—are used to quantita-
tively assess the tracking control performance of the proposed
method. M is defined as the samples size, and ei denotes the
position tracking error. The corresponding formulations are
given as follows:
RMSE =
v
u
u
t 1
M
M
X
i=1
e2
i
∀i ∈A
(13)
MAX = max(|e(i)|).
(14)
The experimental setup and results’ analysis are described in
the following.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 10:16:54 UTC from IEEE Xplore.  Restrictions apply.

## Page 6

2510913
IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 72, 2023
Fig. 2.
Framework of the proposed method.
Fig. 3.
Test accuracy of the proposed method with increasing number of
historical state data frames.
A. Experimental Configuration and Parameters Setting
The proposed reinforcement-learning-based control algo-
rithm was implemented in Python using TensorFlow [39].
The DDPG framework, consisting of online critic network,
target critic network, online actor network, and target actor
network, was used. The network architectures of the target
critic network and target actor network were the same as
those of the online critic network and online actor network,
respectively. The network structure of the designed method is
shown in Fig. 2, where it can be seen that there were four
hidden layers in both the actor network and critic network.
The input and output of the actor network were a system
state s ∈R40 and action a ∈R6, respectively. The number
of neural points in the actor network’s hidden layers was 64,
128, 256, and 64, respectively. The architecture of the designed
incremental reinforcement learning control model is shown in
Fig. 2. For the critic network, the hidden layer structure was
128–256–128–64. There were 4000 episodes in the training
phase for learning.
Since there is no sufficient mature mathematical theory
to support the process of setting parameters, it is not easy
to choosing appropriate parameters’ value in the RL-based
model, which requires extensive trial and error and practical
experience [40], [41]. In the proposed method, the tracking
Fig. 4.
Relationship between control accuracy and parameter set (η0, k) in
numerical test.
Fig. 5.
Average rewards per episode.
control state contains the current flight state and the past
three flight data frames. That is, because historical flight
data usually have strong correlations to the current flight
state, which are helpful for neural network to obtain better
comprehensive estimation for current state and generate more
appropriate control signal. In
experiments, we noted that
the control accuracy in terms of RMSE and maximum errors
could be improved by initially increasing the number of
past data frames in flight state, which is shown in Fig. 3.
It is observable that the control errors decrease rapidly and
then tend to improve with the growing number of historical
data frames. Thus, we have chosen the past three historical
data as the part of current flight state to obtain optimum
performance.
For the weight coefficient of each item in the reward
function, we empirically select the value of parameters in
reward function. All the tracking control errors are defined
as negative penalty item, which will have large value when
the control results are neither stable nor accurate. When the
policy controls vehicle approach steady state, the penalty value
is close to zero. Setting an immediate reward in this way aims
to control UAV to stably fly at a desired state throughout
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 10:16:54 UTC from IEEE Xplore.  Restrictions apply.

## Page 7

MA et al.: DRL OF UAV TRACKING CONTROL UNDER WIND DISTURBANCES ENVIRONMENTS
2510913
Fig. 6.
RMSE performance per episode.
the flight mission. Specifically, we set w1 = 0.4, w2 = 0.4,
w3 = 0.2, and w4 = 0.02. That is, because the position control
and attitude control have more importance in the designed
control method, and the velocity control item and energy
cost item have been assigned with less weight for their low
priority comparing with the first two items. Spare reward is
activated when the UAV reached the specific flight state, such
as tracking with high accuracy, reaching unavailable state. r+
P
is the position precision reward item. The agent will obtain a
sparse positive reward once the position error is within 0.2 m.
The value of r+
P is 5 if these conditions are met; otherwise, r+
P
is zero. r+
V is the velocity precision reward item, and it will be
activated with the positive value 5 once the velocity tracking
error is within 0.1 m/s. When the control command guides
the drone to reach the unavailable state, the sparse plenty
r−
done will be implemented with the negative reward −100.
The mentioned three sparse rewards will only be activated
under some certain conditions. If the specific condition is met,
the reward will be triggered with specific rewards. Otherwise,
it will be set to zero.
In the proposed PR model, the setting of preset probability
threshold and initial probability might tend to influence the
control results. The cross-validation method is used to select
the optimal parameter set (η0, k), in which the candidates’
set of η0 is chosen as [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
and the candidates’ set of k is [0.4, 0.5, 0.6, 0.7, 0.8, 0.9].
Fig. 4 illustrates the relationship between RMSE value and
parameters’ setting (η0, k). It can be seen that the optimal
performance can be achieved with the parameter set (η0 =
0.4, k = 0.7).
B. Training in Numerical Simulation Environments
The random initial flight state selection strategy and wind
disturbance were implemented into the numerical system to
simulate changes in a dynamic environment. The ablation
experiments were conducted to explore how do PR and SW
strategies influence the results of the designed control model.
Four methods were used for learning in dynamic changing
environments as follows.
1) Proposed Method: This method used both the PR (PR)
method and the SW method in experiments, and it was denoted
as the PRSW control method;
2) PR: This method implemented the PR strategy without
using the SW strategy in testing;
3) SW: This method implemented the SW strategy without
the PR strategy in testing;
4) DDPG: In this method, neither the PR nor SW mecha-
nisms were used in the DDPG framework, which was used as
a baseline in the ablation study.
The
average
reward
over
a
batch
of
learning
episodes
was
used
to
evaluate
and
analyze
the
performance of the reinforcement-learning-based tracking
control
method.
The
average
reward
was
defined
by:
GAve = (1/NeNt) PNe
i=1
PNt
t=1 ri
t , where GAve represents the
average return through bunch of Ne episodes, and ri
t means
the received reward for accomplishing the learned control
action at time step t of certain episodes e. In the learning
stage, the average reward was evaluated every ten episodes.
Fig. 5 illustrates the learning results in terms of GAve of
different variations in the methods in the ablation study. First,
the results of the baseline methods DDPG and SW were
compared, and it was concluded that the SW mechanism
could improve the performance of the baseline algorithm.
In the learning phases, the SW strategy was used to expand
the opportunities of accepting samples with high importance,
which enabled improving the capability in terms of average
reward. The SW strategy could encourage an appropriate
exploration in the initial learning stage and accelerate the
convergence speed. Next, the performance in terms of GAve of
the PR mechanism was also more capable than the variation
in baseline, which demonstrates that the PR strategy could
effectively improve the controller’s adaption ability to dynamic
changing environments. Besides, the average reward of PRSW,
which included the PR and SW mechanisms, increased the
fastest and accomplished the best results, among all the
methods, almost through the entire learning phase. In addition,
GAve of the PRSW grew rapidly and converged faster than
those of the other three variants of methods. The ablation
experiments in the numerical simulation environment have
shown that the proposed method can significantly improve the
learning effectiveness.
The evaluation metric of RMSE is also provided in this
section. First, from the learning process represented by the
RMSE position performance in Fig. 6, the proposed method
learns faster and achieves the better convergence speed than
other methods. In the beginning of the learning process,
the proposed method dose not achieve the accuracy control
performance and the RMSE indicators in the early episodes
are higher. That is because the parameters of neural networks
are not converged to the optimal status in the initial stage.
The proposed PR and SW algorithm are able to provide
sufficient exploration and guidance for the learning process,
which contributes to improving the stability and quality of the
training process. Moreover, the detailed convergence speed,
computation energy, RMSE indicator, and inference time are
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 10:16:54 UTC from IEEE Xplore.  Restrictions apply.

## Page 8

2510913
IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 72, 2023
TABLE I
EVALUATION METRIC ABOUT LEARNING PROCESS
Fig. 7.
UAV’s desired position and actual position.
listed on the Table I. As demonstrated in Table I, the inference
time of the proposed method is faster than other solutions
while using the similar computation consumption. It can be
seen from the above analysis that the learning process of the
proposed method achieves the stability and convergence within
4000 episodes while other three methods still suffer from
lower rewards and higher errors in the limited training time.
According to the above analysis, the stability and effectiveness
about the learning process of the proposed method are verified.
The tracking control experiments were conducted in numer-
ical simulation for digging into the control performance of
the proposed method and to compare it with the performance
of the state-of-the-art control method, the CADRC algorithm.
The vehicle started from the initial position (2, 0, 0) and began
to track the desired trajectory of movements. The comparison
of the trajectory tracking results and attitude control errors
of the proposed method and the CADRC method in three
channels is shown in Figs. 7 and 8, while the position tracking
errors and attitude control errors are shown in Fig. 9. The
solid black line represents the desired tracking signal, the
blue dashed line represents the response tracking result of
the PRSW, and the orange dashed line denotes the response
tracking result of classical control-based CADRC method.
When the UAV was tracking the desired trajectory, the position
tracking errors of the proposed RL-based control method were
within ±0.15 m, and the attitude control errors were no more
than ±0.2◦. In practical application, we explain the mean posi-
tion tracking error within 0.5 m as the acceptable performance,
because the UAV is able to conduct lots of flight missions
Fig. 8.
Attitude control results in numerical experiments.
Fig. 9.
Position control errors in numerical experiments.
under that control precision. The corresponding results of
numerical errors are summarized in Table II. In Table II,
it can be seen that the proposed method achieved better control
results than CADRC; however, the gap is not very large in
the first set of numerical simulation. The reason is that in
the ideal environment of numerical experiment, it is easy for
many SOTA controllers to achieve good performance without
considering any real-world restrictions [1], [4]. According
to the results, compared with the vehicle implemented with
the CADRC algorithm, the UAV implemented with the pro-
posed RL-based control algorithm had a better ability to
track the desired trajectory movements and achieved smaller
control errors in terms of position, velocity, acceleration,
and attitude control. The numerical experimental results have
demonstrated that the designed method can be effectively
applied to the UAV tracking control flight in the simulation
environments.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 10:16:54 UTC from IEEE Xplore.  Restrictions apply.

## Page 9

MA et al.: DRL OF UAV TRACKING CONTROL UNDER WIND DISTURBANCES ENVIRONMENTS
2510913
TABLE II
TRACKING ERRORS IN NUMERICAL SIMULATION WITHOUT
EXTERNAL DISTURBANCES
C. HITL Experiments Under Wind Disturbances
For the purpose of testing the robustness and feasibility of
the designed control algorithm under wind disturbances, the
HITL experimental platform has been established. The HITL
platform, as shown in Fig. 10(a), contains flight computer for
implementing control model, environment simulator, actuators,
batteries, and ground station. The flight control computer is
the core part and determines the performance and safety of
the system. The proposed RL-based control model of UAV
is running on the flight computer where the control model
can receive the feedback of multirotor’s flight state (i.e.,
velocity, position, and attitude angle) and calculate the control
command to actuators. The flight computer receives the remote
commands of the ground console through the serial port utility
and executes the corresponding tasks. The sampling frequency
of the HITS system is 600 Hz, which meets the requirements
of high-fidelity simulation system. We adopt Airsim [42] as
flight environment simulator, including environment module,
virtual sensor modules, airframes model, physical engine,
rendering interface, and an interface API for the control
model. In the simulation test, Airsim consumes the actuator
signals generated by the proposed controller to figure out
force and thrust generated by each actuator. This is then used
by the physics engine to compute the kinetic properties of
the drone. This in turn generates simulated sensor data and
feed it back to the flight controller. The virtual sensor model
of IMU, gyroscope, magnetometer (compass), and barome-
ter implemented in HITL is MPU6500, GY9250, bmm150,
and icp10111, respectively. The version of this simulator is
AirsimV1.8 with UE5. The HILT experimental platform is
applied on a computer with Intel core i7-8700 CPU, a NVIDIA
GTX-2080 GPU, and 16-GB RAM. After receiving the remote
control instructions from the console software, the flight
control computer generates control instructions according to
flight states and finally drives the motor and steering gear
to make the UAV take automatic flight control. The flight
control computer receives the remote control commands of
the ground console through the serial port server and executes
the corresponding flight tasks. The flight control computer
publishes the state data and actuator data of the aircraft to the
2-D and 3-D situation software through the serial port server.
Finally, the flight information of the entire flying stage was
transferred to the ground state for visualization and analysis.
Fig. 10(b) shows the experimental platform consists of a
self-developed UAV. Weighing approximately 5 kg with a
maximum takeoff weight of about 11 kg, the self-developed
UAV can easily carry equipment as heavy as a Lidar VLP-16.
Used with a 32 000-mAh battery, it can fly for up to 45 min.
Its diagonal wheelbase is 1045 mm, and the maximum flight
speed is 9 m/s.
Fig. 10.
HITL simulation platform and self-developed UAV. (a) HITL
simulation platform. (b) Self-developed UAV.
Fig. 11.
Trajectory tracking control results in various wind environments.
Since the Airsim simulator had a strong capacity for
simulating the wind field environment in a flying mission,
we applied three different types of wind disturbances using
the environment simulator for demonstrating the disturbance
rejection performance of the proposed method. As shown in
Fig. 11, in the first zone of the flight field, wind disturbances
were constant; in the middle zone of the flight region, wind
disturbances were set to the changing wind, which meant the
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 10:16:54 UTC from IEEE Xplore.  Restrictions apply.

## Page 10

2510913
IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 72, 2023
Fig. 12.
Position control errors in various wind environments.
Fig. 13.
Attitude control errors in various wind environments.
speed and torque of wind were randomly generated in the
simulator; finally, in the last zone, there was a strong wind gust
acting on the last segment of the flight trajectory. As shown in
Fig. 12, both the PRSW and CADRC control algorithms could
fly along the given trajectory in the whole wind field and the
deviation of the RL-based method was smaller than that of
the CADRC. The attitude control errors while the vehicle was
passing through the wind region are shown in Fig. 13, where it
can be seen that the stabilization performance of the proposed
algorithm was less affected by the wind disturbance type
compared with those of the other control methods. Specifically,
the angle offset of the UAV using the proposed method had a
slight shift at the beginning of interference and then returned
to the stable state in the middle and late periods of wind
disturbance, which made it faster than another method. Thus,
the proposed control algorithm had good robustness under
various types of wind disturbances.
The comparison experimental results under wind distur-
bances are analyzed and discussed to test the performance of
the proposed tracking control method comparing with other
SOTA methods further. The experimental setting of wind
disturbances is the same as those in the above-mentioned
experiments. As shown in Table III, the RMSE performance
of the proposed method in multievaluation channels is smallest
TABLE III
COMPARISON EXPERIMENTS WITH LATEST METHODS
UNDER WIND DISTURBANCES
TABLE IV
RMSE PERFORMANCE OF THE PROPOSED METHOD AND CADRC
CONTROLLER IN THE REAL-WORLD ENVIRONMENT UNDER
WIND DISTURBANCES
among other four latest controllers. Moreover, the maximum
errors of the proposed method are also significantly smaller
than other methods. That is because the designed RL-based
solution has learned appropriate control policy under external
disturbances in the learning phase and provides robustness
capability to disturbance force. The comparison results show
that the proposed method achieves better robustness compared
with latest methods.
D. Real-World Flight Experiments
To investigate the reliability of the proposed control algo-
rithm further, it was analyzed experimentally using a real-
world multirotor UAV platform. Fig. 10(b) shows the designed
self-developed multirotor UAV, which uses the NVIDIA Jetson
Nano as the flight control computer. The AH100B sensor
was adopted as the inertial measurement unit (IMU) model,
which could precisely measure the flight state parameters (i.e.,
attitude angle, angle rate, and velocity). A Lidar system was
implemented to assist in the measurement of real-time data.
The flight data were collected and transferred to the ground
state for observation. Fig. 14 shows the real-world flight test
setup. The multirotor aircraft was commanded to track the
desired path in experiments. Comparative experiments on the
proposed method and CADRC controller were implemented
under the same conditions.
As shown in Fig. 15, the multirotor using the control method
could track the desired path with high precision. The initial
position of the UAV was defined as (10, 5, 0). The UAV took
off from the initial position, rising up to 30 m, and then started
to move along the elliptical path with an average speed of
approximately 2.8 m/s. After flying around the elliptical path,
the vehicle returned and began landing in the initial position.
The curve of airspeed changes is shown in Fig. 16, where it
can be seen that the airspeed of the UAV fluctuated during
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 10:16:54 UTC from IEEE Xplore.  Restrictions apply.

## Page 11

MA et al.: DRL OF UAV TRACKING CONTROL UNDER WIND DISTURBANCES ENVIRONMENTS
2510913
Fig. 14.
UAV tracking scene in real-world flight test. (a) Video snapshot of
the 10th second of the real-world experiments. (b) Video snapshot of the 30th
second of the real-world experiments. (c) Video snapshot of the 50th second
of the real-world experiments.
the flight phase. The attitude angle curve of the UAV during
the flight test is shown in Fig. 17, where it can be seen
that there were certain jumps and fluctuations, which were
mainly caused by the wind disturbances in the outside flight
environment. The vehicle was robust and adaptive enough to
resist the disturbances and return to its desired movement
state in the changing flight environment. Table IV summarizes
the RMSE value of two controllers. From Table IV, it can
be observed that compared with the CADRC controller, our
proposed RL-based controller has higher control accuracy in
the real-world scenario under wind environments. Through
the above relevant flight experiments, the high precision and
high effectiveness of tracking performance as well as strong
robustness of the proposed control method were confirmed.
Fig. 15.
3-D trajectory of tracking control task in real-world flight test.
Fig. 16.
Velocity control results in real-world flight test.
Fig. 17.
Attitude control results in real-world flight test.
IV. CONCLUSION
This article proposes an innovative reinforcement-learning-
based UAV tracking control algorithm in a dynamic environ-
ment, which can handle various types of wind disturbances
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 10:16:54 UTC from IEEE Xplore.  Restrictions apply.

## Page 12

2510913
IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 72, 2023
during the tracking mission. The main goal of this study is
to make the controller adjustable and robust when there are
changes and disturbances in a flight environment. The PR
mechanism is designed to encourage proper exploration in the
learning phase, which reduces the imbalances between the new
and existing knowledge. The SW method is used to enable an
agent to adapt to various environments better. The random
wind disturbance signal has been implemented on numerical
dynamic environment in learning process for improving the
robustness of the controller. Furthermore, a novel reward
function is designed, which can increase the learning effi-
ciency. Finally, a set of experiments, including the numeri-
cal simulation, HITL experiments, and the real-world flight
test, are performed to verify the capacity and robustness of
the proposed method under changing dynamic environments.
The results demonstrate that the proposed RL-based control
algorithm is effective and practical. In current research work,
we focused on the control accuracy of the proposed method
under wind disturbances and did not consider the collision
avoidance function in multiobstacles’ existing environments.
In the future work, we will endeavor to investigate the collision
avoidance problem of UAV in complex environments via
external sensor system including Lidar and visual navigation
module.
REFERENCES
[1] Y. Song, Z. Liu, J. Han, W. Zhao, and N. Li, “Coordinated turn of
fixed-wing aircraft under wind interface on integral backstepping,” IEEE
Trans. Instrum. Meas., vol. 70, pp. 1–18, 2021.
[2] J. Yuan et al., “Global optimization of UAV area coverage path planning
based on good point set and genetic algorithm,” Aerospace, vol. 9, no. 2,
p. 86, 2022.
[3] A. He et al., “Full mode flight dynamics modelling and control of
stopped-rotor UAV,” Chin. J. Aeronaut., vol. 35, no. 10, pp. 95–105,
Oct. 2022.
[4] L. Chen, Z. Liu, H. Gao, and G. Wang, “Robust adaptive recursive slid-
ing mode attitude control for a quadrotor with unknown disturbances,”
ISA Trans., vol. 122, pp. 114–125, Mar. 2022.
[5] B. Ma, Z. Liu, F. Jiang, Y. Yan, J. Yuan, and S. Bu, “Vehicle detection
in aerial images using rotation-invariant cascaded forest,” IEEE Access,
vol. 7, pp. 59613–59623, 2019.
[6] X. Zou, Z. Liu, W. Zhao, and C. Zhang, “Optimal hovering control of a
tail-sitter via model-free fast terminal slide mode controller and cuckoo
search algorithm,” in Proc. Int. Conf. Unmanned Aircr. Syst. (ICUAS),
Jun. 2021, pp. 978–984.
[7] H. Gao, Z. Liu, B. Wang, and C. Pang, “Flight dynamics and control of
a new VTOL aircraft in fixed-wing mode,” in Proc. Int. Conf. Unmanned
Aircr. Syst. (ICUAS), Sep. 2020, pp. 1650–1657.
[8] Q. Quan, R. Fu, M. Li, D. Wei, Y. Gao, and K.-Y. Cai, “Practical
distributed control for VTOL UAVs to pass a virtual tube,” IEEE Trans.
Intell. Vehicles, vol. 7, no. 2, pp. 342–353, Jun. 2022.
[9] Y. Zou, H. Zhang, and W. He, “Adaptive coordinated formation control
of heterogeneous vertical takeoff and landing UAVs subject to parametric
uncertainties,” IEEE Trans. Cybern., vol. 52, no. 5, pp. 3184–3195,
May 2020.
[10] H. Eslamiat, A. K. Sanyal, and C. Lindsay, “Discrete time optimal
trajectory generation and transversality condition with free final time,” in
Proc. Int. Conf. Unmanned Aircr. Syst. (ICUAS), Jun. 2021, pp. 843–852.
[11] P. Poksawat, L. Wang, and A. Mohamed, “Gain scheduled attitude
control of fixed-wing UAV with automatic controller tuning,” IEEE
Trans. Control Syst. Technol., vol. 26, no. 4, pp. 1192–1203, Jul. 2018.
[12] C. Rosales, S. Tosetti, C. Soria, and F. Rossomando, “Neural adaptive
PID control of a quadrotor using EFK,” IEEE Latin Amer. Trans., vol. 16,
no. 11, pp. 2722–2730, Nov. 2018.
[13] H. K. Tran, J.-S. Chiou, N. T. Nam, and V. Tuyen, “Adaptive fuzzy
control method for a single tilt tricopter,” IEEE Access, vol. 7,
pp. 161741–161747, 2019.
[14] Y. Yu, J. Guo, C. K. Ahn, and Z. Xiang, “Neural adaptive distributed
formation control of nonlinear multi-UAVs with unmodeled dynamics,”
IEEE Trans. Neural Netw. Learn. Syst., early access, Mar. 16, 2022, doi:
10.1109/TNNLS.2022.3157079.
[15] X. Shao, G. Sun, W. Yao, J. Liu, and L. Wu, “Adaptive sliding mode
control for quadrotor UAVs with input saturation,” IEEE/ASME Trans.
Mechatronics, vol. 27, no. 3, pp. 1498–1509, Jun. 2022.
[16] S. M. LaValle et al., “Rapidly-exploring random trees: A new tool for
path planning,” Dept. Comput. Sci., Iowa State Univ., Ames, IA, USA,
Tech. Rep. 9811, 1998.
[17] S. P. Viswanathan, A. K. Sanyal, and R. R. Warier, “Finite-time stable
tracking control for a class of underactuated aerial vehicles in SE(3),”
in Proc. Amer. Control Conf. (ACC), May 2017, pp. 3926–3931.
[18] R. R. Warier, A. K. Sanyal, M. H. Dhullipalla, and S. P. Viswanathan,
“Finite-time stable trajectory tracking and pointing control for a class of
underactuated vehicles in SE(3),” in Proc. Indian Control Conf. (ICC),
Jan. 2018, pp. 190–195.
[19] L. X. Xu, H. J. Ma, D. Guo, A. H. Xie, and D. L. Song, “Backstepping
sliding-mode and cascade active disturbance rejection control for a
quadrotor UAV,” IEEE/ASME Trans. Mechatronics, vol. 25, no. 6,
pp. 2743–2753, Dec. 2020.
[20] V. K. Tripathi, A. K. Kamath, L. Behera, N. K. Verma, and S. Nahavandi,
“An adaptive fast terminal sliding-mode controller with power rate
proportional reaching law for quadrotor position and altitude tracking,”
IEEE Trans. Syst., Man, Cybern., Syst., vol. 52, no. 6, pp. 3612–3625,
Jun. 2022.
[21] B. Zhao, B. Xian, Y. Zhang, and X. Zhang, “Nonlinear robust adaptive
tracking control of a quadrotor UAV via immersion and invariance
methodology,” IEEE Trans. Ind. Electron., vol. 62, no. 5, pp. 2891–2902,
May 2015.
[22] Z. Wang and T. Zhao, “Based on robust sliding mode and linear
active disturbance rejection control for attitude of quadrotor load UAV,”
Nonlinear Dyn., vol. 108, pp. 3485–3503, Mar. 2022.
[23] J. Moon, S. Papaioannou, C. Laoudias, P. Kolios, and S. Kim, “Deep
reinforcement learning multi-UAV trajectory control for target tracking,”
IEEE Internet Things J., vol. 8, no. 20, pp. 15441–15455, Oct. 2021.
[24] J. Wu, H. Wang, Y. Liu, M. Zhang, and T. Wu, “Learning-based fixed-
wing UAV reactive maneuver control for obstacle avoidance,” Aerosp.
Sci. Technol., vol. 126, Jul. 2022, Art. no. 107623.
[25] B. Wang, J. Xie, and J. Chen, “Data-driven multi-UAV navigation in
large-scale dynamic environments under wind disturbances,” in Proc.
AIAA Scitech Forum, 2021, p. 1284.
[26] Z. Birnbaum, A. Dolgikh, V. Skormin, E. O’Brien, and C. Stracquodaine,
“Unmanned aerial vehicle security using behavioral profiling,” in Proc.
Int. Conf. Unmanned Aircr. Syst. (ICUAS), 2015, pp. 1310–1319.
[27] C. Tang and Y.-C. Lai, “Deep reinforcement learning automatic landing
control of fixed-wing aircraft using deep deterministic policy gradient,”
in Proc. Int. Conf. Unmanned Aircr. Syst. (ICUAS), Sep. 2020, pp. 1–9.
[28] W. Kaifang, L. Bo, G. Xiaoguang, H. Zijian, and Y. Zhipeng,
“A learning-based flexible autonomous motion control method for UAV
in dynamic unknown environments,” J. Syst. Eng. Electron., vol. 32,
no. 6, pp. 1490–1508, Dec. 2021.
[29] P. Kaushik, A. Garg, and S. S. Jha, “On learning multi-UAV policy for
multi-object tracking and formation control,” in Proc. IEEE 18th India
Council Int. Conf. (INDICON), Dec. 2021, pp. 1–6.
[30] N. H. Chu, D. T. Hoang, D. N. Nguyen, N. Van Huynh, and
E. Dutkiewicz, “Joint speed control and energy replenishment optimiza-
tion for UAV-assisted IoT data collection with deep reinforcement trans-
fer learning,” IEEE Internet Things J., vol. 10, no. 7, pp. 5778–5793,
Apr. 2023.
[31] S. S. Gu, T. Lillicrap, R. E. Turner, Z. Ghahramani, B. Schölkopf, and
S. Levine, “Interpolated policy gradient: Merging on-policy and off-
policy gradient estimation for deep reinforcement learning,” in Proc.
Adv. Neural Inf. Process. Syst., vol. 30, 2017, pp. 1–10.
[32] D. Koller and N. Friedman, Probabilistic Graphical Models: Principles
and Techniques. Cambridge, MA, USA: MIT Press, 2009.
[33] S. Levine and V. Koltun, “Guided policy search,” in Proc. Int. Conf.
Mach. Learn., 2013, pp. 1–9.
[34] K. Kawaguchi, “Deep learning without poor local minima,” in Proc.
Adv. Neural Inf. Process. Syst., vol. 29, 2016, pp. 1–9.
[35] Z. Ren, D. Dong, H. Li, and C. Chen, “Self-paced prioritized curricu-
lum learning with coverage penalty in deep reinforcement learning,”
IEEE Trans. Neural Netw. Learn. Syst., vol. 29, no. 6, pp. 2216–2226,
Jun. 2018.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 10:16:54 UTC from IEEE Xplore.  Restrictions apply.

## Page 13

MA et al.: DRL OF UAV TRACKING CONTROL UNDER WIND DISTURBANCES ENVIRONMENTS
2510913
[36] J. Martens et al., “Deep learning via hessian-free optimization,” in Proc.
ICML, vol. 27, 2010, pp. 735–742.
[37] T. Schaul, J. Quan, I. Antonoglou, and D. Silver, “Prioritized experience
replay,” 2015, arXiv:1511.05952.
[38] D. Silver, G. Lever, N. Heess, T. Degris, D. Wierstra, and M. Riedmiller,
“Deterministic policy gradient algorithms,” in Proc. Int. Conf. Mach.
Learn., 2014, pp. 387–395.
[39] M. Abadi et al., “TensorFlow: A system for large-scale machine learn-
ing,” in Proc. 12th USENIX Symp. Operating Syst. Design Implement.
(OSDI), 2016, pp. 265–283.
[40] S. Aradi, “Survey of deep reinforcement learning for motion planning of
autonomous vehicles,” IEEE Trans. Intell. Transp. Syst., vol. 23, no. 2,
pp. 740–759, Feb. 2022.
[41] X. Li, H. Jiang, Y. Liu, T. Wang, and Z. Li, “An integrated deep
multiscale feature fusion network for aeroengine remaining useful
life prediction with multisensor data,” Knowl.-Based Syst., vol. 235,
Jan. 2022, Art. no. 107652.
[42] S. Shah, D. Dey, C. Lovett, and A. Kapoor, “AirSim: High-fidelity visual
and physical simulation for autonomous vehicles,” in Field and Service
Robotics. Cham, Switzerland: Springer, 2018, pp. 621–635.
Bodi Ma (Member, IEEE) received the B.S. and
M.S. degrees from Northwestern Polytechnical Uni-
versity, Xi’an, China, in 2016 and 2019, respectively,
where he is currently pursuing the Ph.D. degree in
means of transport applied engineering.
His main research interests include intelligent con-
trol systems, UAV tracking control, reinforcement
learning, and formation control.
Zhenbao Liu (Senior Member, IEEE) received
the B.S. and M.S. degrees from Northwestern
Polytechnical University, Xi’an, China, in 2001 and
2004, respectively, and the Ph.D. degree from the
University of Tsukuba, Tsukuba, Japan, in 2009, all
in electrical engineering and automation.
He is currently a Professor with Northwestern
Polytechnical University. He was a Visiting Scholar
with Simon Fraser University, Burnaby, BC, Canada,
in 2012. His current research interests include
autonomous unmanned systems, formation control,
and intelligent control and simulations.
Dr. Liu is an Associate Editor of IEEE ACCESS.
Qingqing Dang received the Ph.D. degree from
Beihang University, Beijing, China, in 2019.
He
is
currently
an
Assistant
Professor
with
Northwestern
Polytechnical
University,
Xi’an,
China.
His
current
research
interests
include
autonomous unmanned systems, formation control,
and intelligent control and simulations.
Wen Zhao received the M.S. degree in control
engineering from Shanghai University, Shanghai,
China, in 2014, and the Dr.Eng. degree in modern
mechanical engineering from Waseda University,
Tokyo, Japan, in 2019.
He has been a Post-Doctoral Researcher with
Sugano Laboratory, Waseda University, since 2020.
He is currently an Associate Professor with the
School of Civil Aviation, Northwestern Polytech-
nical University, Xi’an, China. He has authored or
coauthored several journals and conference papers in
the field of robotics and control theory. His research interests include robotics,
embedded software/hardware design, data processing, sensor technology,
control theory and modeling, and electronic system design.
Jingyan Wang is currently a Researcher with the Beijing Institute of
Spacecraft System Engineering, Beijing, China. Her main research interests
include UAV control systems and simulation.
Yao Cheng is currently an Engineer with the Beijing Institute of Spacecraft
System Engineering, Beijing, China. Her main research interests include UAV
navigation, health management, and deep learning methods.
Zhirong Yuan is currently a Researcher with 365
Institute,
Northwestern
Polytechnical
University,
Xi’an, China. His main research interests include
UAV control system and UAV formation control.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 10:16:54 UTC from IEEE Xplore.  Restrictions apply.
