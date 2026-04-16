# A constrained reinforcement learning based approach for cooperative control of multi-UAV in dense obstacle environments.pdf

## Page 1

SCIENCE CHINA
Technological Sciences
Print-CrossMark
January 2026, Vol. 69, Iss. 1, 1120601:1–1120601:15
https://doi.org/10.1007/s11431-025-3076-2
c⃝Science China Press 2026
tech.scichina.com
link.springer.com
. RESEARCH PAPER.
A constrained reinforcement learning based approach for
cooperative control of multi-UAV in dense obstacle environments
Jian GU & Yin WANG*
School of Astronautics, Nanjing University of Aeronautics and Astronautics, Nanjing 211106, China
Received May 24, 2025; accepted September 28, 2025; published online January 4, 2026
Abstract
Formation control of multiple unmanned aerial vehicles (UAVs) is a fundamental challenge for advanced cooperative
tasks. In dense obstacle environments, machine learning-based formation control algorithms face signiﬁcant challenges due to the
high environmental complexity and UAV dynamics, particularly manifested as an explosion in state space dimensionality and poor
obstacle avoidance robustness. To address these issues, this paper proposes a threat-aware subspace feature extraction mechanism
and constraint learning algorithm within a deep reinforcement learning (DRL) framework. Our approach ﬁrst reconstructs spatial
distributions of high-threat obstacles and UAV kinematic characteristics from LiDAR point cloud data to reduce state space
dimensionality. Then, we solve the obstacle avoidance problem using a novel constrained reinforcement learning framework.
This framework employs a safety-oriented penalty function instead of conventional posterior penalties to explicitly enforce safety
constraints, thereby preventing dangerous actions. We rigorously prove the algorithm’s convergence and stability using Lyapunov
stability theory. Comparative experiments carried out in the high-ﬁdelity AirSim environment have demonstrated that the proposed
algorithm outperforms the state-of-the-art methods, where the convergence speed improves by 36.36%, stability increases by
18.22%, and mission success rate rises by 5.6%.
Keywords
unmanned aerial vehicles, deep reinforcement learning, threat-aware subspace feature extraction, constraint learning
algorithm, Lyapunov stability theory
Citation:
Gu J, Wang Y. A constrained reinforcement learning based approach for cooperative control of multi-UAV in dense obstacle environments. Sci China
Tech Sci, 2026, 69(1): 1120601, https://doi.org/10.1007/s11431-025-3076-2
1
Introduction
Deep reinforcement learning (DRL) based UAV technol-
ogy is increasingly used in disaster response, logistics, and
environmental monitoring [1, 2].
Compared with model-
based control algorithms that rely heavily on accurate math-
ematical models, deep reinforcement learning stands out
for its excellent learning ability and ﬂexibility in solving
sequential decision problems [3, 4].
However, deep rein-
forcement learning based control algorithms still face many
challenges [5, 6].
In dense obstacle environments, the
state space dimension explodes [7, 8] and the robustness
is poor [9, 10].
These challenges place higher demands
on the reliability and adaptability of control policies [11].
* Corresponding author (email: yinwangee@nuaa.edu.cn)
As the number of UAVs and environmental complexity
increase, the state space expands exponentially, leading to
prohibitive computational costs [12, 13] and slow conver-
gence. This may result in non-convergence or being trapped
in local optima [14, 15].
To mitigate this, eﬃcient algo-
rithms are needed to compress the state space [16]. Anjali
et al. [17] proposed an autoencoder-based reduction method
(AERed) that decreases computational complexity and ac-
celerates training but risks losing critical state information.
Huang et al. [18] addressed this by employing hierarchical
DRL to decompose complex tasks into smaller sub-tasks, ef-
fectively reducing the state space. Similarly, Liu et al. [19]
leveraged hierarchical DRL with a sub-goal mechanism to
alleviate dimensionality explosion while improving explo-
ration eﬃciency.
However, these methods require further

## Page 2

Gu J, et al.
Sci China Tech Sci
January 2026, Vol. 69, Iss. 1, 1120601:2
mechanisms to allocate subtask coordination, thus increasing
the complexity of the design.
Maintaining the safe operation of UAVs in dense obsta-
cle environments is still a challenging task [20, 21].
Mi-
randa et al. [22] enhanced system stability and adaptability
by designing sophisticated reward functions. In this method,
the posterior penalty mechanisms were used to account for
hazardous behaviors, which necessitate collision experiences
during training. This scheme constrains the agent’s capac-
ity to acquire safe policies, even when the learning algorithm
has converged. To deal with this problem, Gangopadhyay
et al. [23] integrated control barrier functions (CBFs) to en-
force collision avoidance, thus improving system robustness.
However, CBF implementation may induce excessive evasive
maneuvers, diminishing learning eﬃciency, and potentially
hindering task completion. While these approaches advance
safety protocols, they introduce critical trade-oﬀs between
cautionary measures and operational performance that war-
rant further investigation.
To address the challenges of multi-UAV formation control
in dense obstacle environments, this paper proposes threat-
aware constrained optimization (TACO), a multi-UAV coop-
erative control framework. The contributions of this paper
include:
(1) We introduced a threat-aware subspace feature extrac-
tion mechanism aimed at reducing the observation space di-
mension of multi-UAV control algorithms. The threat-aware
subspace extracts the spatial distribution and kinematic fea-
tures of high-threat UAVs from LiDAR perception data, ef-
fectively enhancing the eﬃciency and ﬂexibility of the DRL
network. A threat function was also constructed to quantify
collision risks in dense obstacle environments.
(2) To optimize the policy network’s exploration direc-
tion, we utilized a constraint optimization framework based
on penalty functions. The threat function was embedded as a
penalty term into the Actor neural network of deep reinforce-
ment learning to prevent potentially dangerous actions. This
method signiﬁcantly improved the system’s safety in dense
obstacle environments.
(3) To ensure the stability of the policy iteration process,
we constructed a Lyapunov function. Through theoretical
analysis, we provided stability guarantees for UAVs to ac-
tively avoid exploring dangerous action spaces during train-
ing, while ensuring the reliability and safety of the control
strategy.
The rest of this paper is structured as follows: Section 2
formulates the problem scenario, UAV model, and threat-
aware subspace modeling; Section 3 presents the TACO al-
gorithm architecture, including constraint optimization and
stability analysis; Section 4 evaluates performance through
AirSim simulations; and Section 5 concludes the paper. This
work provides theoretically grounded and practically feasible
solutions for multi-UAV control operating in dense obstacle
environments.
2
Problem formulation
This section formulates the key components of the model-
free UAV control problem in dense obstacle environments.
First, we deﬁne the problem scenario and mission require-
ments. Next, we present the kinematic model of a single
UAV in two-dimensional space. Then, we introduced the Li-
DAR data processing ﬂow for environmental perception in
detail. Finally, we proposed an innovative threat perception
subspace modeling method. Together, these contents form
the mathematical foundation of the subsequent reinforcement
learning framework.
2.1
Problem statement and background
As illustrated in Figure 1,
we looked at a situation
with many obstacles where a group of UAVs, called
U (ui ∈U, i = 1, 2, . . . , N), has N identical UAVs.
In this
case, the UAV group needs to map essential obstacles. The
UAVs must stay close together and ﬁnish the mission quickly
to avoid being detected. Because communication is limited
in the area, the UAVs cannot use it to work together, which
makes it harder for them to move around. In these conditions,
the UAVs use only LiDAR to sense the environment and ad-
just their positions and movements based on the nearby UAVs
they can see.
Figure 1
(Color online) Problem scenario considered in this paper.

## Page 3

Gu J, et al.
Sci China Tech Sci
January 2026, Vol. 69, Iss. 1, 1120601:3
2.2
UAV kinematics model
Assuming UAVs maintain a constant altitude, their move-
ment can be accurately modeled in a two-dimensional plane.

˙xi = vxi,
˙yi = vyi,
˙vxi =
(
vc
xi −vxi
)
/τv,
˙vyi =
(
vc
yi −vyi
)
/τv.
(1)
It describes the kinematic behavior of each UAV i in a
two-dimensional plane. In this model, ˙xi and ˙yi represent the
UAV’s velocities along the x and y axes, respectively. The
terms ˙vxi and ˙vyi refer to the accelerations in the x and y di-
rections. The variables vxi and vyi denote the UAV’s current
velocities, while vc
xi and vc
yi represent the commanded veloc-
ities that the UAV aims to achieve. τv is the time constant
related to the UAV’s dynamics, which deﬁnes how quickly it
can adjust its velocity.
2.3
LiDAR point cloud processing
As shown in Figure 2, we processed LiDAR point cloud data
by scanning the environment with a LiDAR sensor to gener-
ate a 3D point cloud. The data was reﬁned through noise
removal, downsampling, and ground segmentation. Noise
removal eliminates invalid points caused by errors or inter-
ference, improving data quality. Downsampling reduces the
number of points while keeping essential features, which
lowers computational complexity. Ground segmentation sep-
arates the ground from other objects, enhancing the UAVs’
ability to recognize obstacles. These steps optimize the point
cloud data, providing accurate environmental information.
2.4
Threat-aware subspace feature extraction mecha-
nism
In multi-UAV formation control tasks, ensuring the forma-
tion’s stability and the mission’s success requires UAVs to
adapt to dense obstacle environments and avoid potential
risks. UAVs must continuously perceive the movements of
neighboring UAVs and adjust their policies to maintain safe
coordination. To achieve this, we introduced a threat func-
tion that quantiﬁes the interaction risks between UAVs and
integrated it into the policy optimization framework.
To accelerate the exploration speed, we select the most
threatening UAVs and obstacles to calculate the threat as-
sessment factor for the current UAV. By computing the threat
factors for all targets and ranking them, we choose the most
threatening targets for policy optimization, improving learn-
ing eﬃciency and reducing computational load. As shown
in Figure 3, to accurately model threat assessment, the UAV
threat factor is represented as ζi,k and the obstacle threat fac-
tor as ζi,b. As shown below:
ζi,k = Wd · fd
(di,k
) + Wv · fv
(vi,k, ςi,k
)
+ Wa · fa
(ai,k, ϑi,k
) ,
(2)
ζi,b = Wo · fo
(di,b
) ,
(3)
where Wd, Wv, Wa, Wo are weighting coeﬃcients used to
consider the inﬂuence of distance,
velocity,
accelera-
tion, and obstacles in risk assessment.
The functions
fd
(di,k
) , fv
(vi,k, ςi,k
) , fa
(ai,k, ϑi,k
) , fo
(di,b
) measure the risks
associated with relative distance, velocity, acceleration, and
obstacles, respectively. Distance is the most fundamental fac-
tor in threat assessment. To emphasize the higher risk posed
by closer UAVs, we use an exponential decay function to
model the impact of relative distance.
fd
(di,k
) = exp
−
d2
i,k
σ2
d
,
(4)
where di,k =
√
(xi −xk)2 + (yi −yk)2 is the Euclidean dis-
tance between UAV i and UAV k. This function ensures that
the threat coeﬃcient increases sharply when UAVs are close
and gradually decreases when UAVs are far apart, preventing
distant objects from excessively inﬂuencing the risk assess-
ment.
In addition to distance, velocity plays a crucial role in risk
assessment. The relative velocity between UAVs is calcu-
lated as follows:
Figure 2
(Color online) Point cloud processing. (a) Sensor scanning; (b) original point cloud; (c) noise reduction, downsampling, and ground
segmentation.

## Page 4

Gu J, et al.
Sci China Tech Sci
January 2026, Vol. 69, Iss. 1, 1120601:4
Figure 3
(Color online) Point cloud clustering and obstacle detec-
tion.
vi,k = ∥vi −vk∥=
√
(vxi −vxk
)2 +
(
vyi −vyk
)2,
(5)
where vi =
(
vxi, vyi
)
and vk =
(
vxk, vyk
)
are the velocity vec-
tors of UAV i and UAV k, respectively. Velocity alone reﬂects
only part of the collision risk, so we introduce the relative ve-
locity angle ςi,k to determine whether the UAVs are moving
towards or away from each other.
ςi,k = cos−1
( (vi −vk) · (si −sk)
∥vi −vk∥· ∥si −sk∥
)
.
(6)
If ςi,k = 0◦, the UAVs are moving directly towards each
other, increasing the risk of collision; whereas if ςi,k =
180◦, they are moving away from each other, reducing the
risk.
Based on this, we deﬁne the modiﬁed velocity risk
factor:
fv
(vi,k, ςi,k
) =
vi,k

vmax
· (1 + ας cos ςi,k
) ,
(7)
where ςδ is a tuning parameter that adjusts the inﬂuence of
direction on risk assessment. This formula ensures that the
collision risk is higher when the relative velocity is high and
the UAVs are directly approaching each other, while the risk
decreases when they move in opposite directions.
Acceleration is also a critical factor in decision-making.
The relative acceleration between UAVs is calculated as fol-
lows:
ai,k = ∥ai −ak∥=
√
(axi −axk
)2 +
(
ayi −ayk
)2,
(8)
where ai =
(
axi, ayi
)
and ak =
(
axk, ayk
)
represent the accel-
eration vectors of UAV i and UAV k, respectively. To more
accurately assess risk, we introduce the relative acceleration
angle ϑi,k, deﬁned as
ϑi,k = cos−1
( (ai −ak) · (si −sk)
∥ai −ak∥· ∥si −sk∥
)
.
(9)
If ϑi,k = 0◦, the UAVs are accelerating towards each other, in-
creasing the risk of collision. In contrast, if ϑi,k = 180◦, they
are accelerating away from each other, reducing the risk. The
modiﬁed acceleration risk factor is deﬁned as
fa
(ai,k, ϑi,k
) =
ai,k

amax
· (1 + αa cos ϑi,k
) .
(10)
In this context, αa is a directional inﬂuence parameter that
ensures the risk increases when accelerating towards each
other and decreases when moving away.
We consider the distance from the obstacle to the UAV
for obstacle assessment and use a similar exponential de-
cay function to model this eﬀect. The obstacle threat factor
fo
(di,b
) is deﬁned as follows:
fo
(di,b
) = exp
−
d2
i,b
σ2o
,
(11)
where di,b represents the distance to the obstacle, σo controls
the decay rate. This method ensures that the closer the ob-
stacle, the higher the threat coeﬃcient, thereby dynamically
adjusting the UAV’s strategy to avoid potential risks from ob-
stacles.
During the threat target selection process, the system per-
forms a comprehensive evaluation and ranking of threat val-
ues for all nearby UAVs and obstacles, then selects the top 5
most threatening targets (including n UAVs and m obstacles,
where n + m = 5). The total threat value of these selected
targets can be calculated using the following formula:
ζmax
i
=
n
∑
k=1
ζi,k +
m
∑
b=1
ζi,b.
(12)
Therefore, for the current UAV, the total threat coeﬃcient
ζi based on the selected n UAVs and m obstacles is
ζi = max {0, ζmax
i
−ε} ,
(13)
where ε is a hyperparameter deﬁning the threat tolerance
threshold.
To balance the system’s tolerance for minor threats with a
strong response to serious threats, Penalty function ϕ (ζi) is
designed as a piecewise function:
ϕ (ζi) =

0,
if ζi ⩽0,
ζ2
i ,
if ζi > 0.
(14)
No penalty is imposed when the threat value remains be-
low the predeﬁned threshold, preventing overreaction to neg-
ligible risks. Conversely, when the threat value exceeds this
threshold, the penalty grows quadratically with threat sever-
ity. This quadratic scaling intensiﬁes the system’s avoidance
response to high-risk scenarios while maintaining the penalty
function’s continuity and diﬀerentiability.

## Page 5

Gu J, et al.
Sci China Tech Sci
January 2026, Vol. 69, Iss. 1, 1120601:5
3
The proposed method
This section models the multi-UAV cooperative decision-
making problem using a partially observable Markov deci-
sion process to address the issues of low obstacle avoidance
safety and poor task eﬃciency caused by high-dimensional
state spaces in multi-UAV systems operating in dense ob-
stacle environments. A constrained penalty function opti-
mization framework is proposed to ensure safe exploration
and theoretical proofs of convergence and stability. Finally,
a deep reinforcement learning framework is developed to
achieve multi-UAV cooperative control in dense obstacle en-
vironments.
3.1
Reinforcement learning-based UAVs formation
We consider an extension of multi-agent Markov decision
processes (MDPs) known as partially observable Markov
games [24, 25]. A Markov game involving N agents is de-
ﬁned by a set of states S describing all possible conﬁgu-
rations of the agents, a set of actions A1, . . . , AN for each
agent, and a set of observations O1, . . . , ON. To select actions,
each agent i uses a stochastic policy πθi : Oi × Ai 7→[0, 1],
which generates the next state according to the state transi-
tion function: T : S × A1 × . . . × AN 7→S. Each agent
i receives a reward based on a function of the state and the
agent’s actions ri : S × Ai 7→R, and receives a private ob-
servation oi : S 7→Oi related to the state. A distribution
determines the initial state: ρ : S 7→[0, 1]. The agents
start from the initial state distribution ρ, where the initial
state set I = {s | ρ(s) > 0} ⊆S represents all possible
state distributions in the state space. The threat function:
pi : S × A1 × · · · × AN →P maps the global state s and
the joint actions of all agents (a1, . . . , aN) to the return on in-
vestment pi (s, a1, . . . , aN) for agent i. Here, the threat func-
tion is similar to the reward function but focuses more on
measuring the agent’s gain in a speciﬁc state and action. To
simplify the representation, the global state and joint action
pair at the next time step (st+1, a1,t+1, . . . , aN,t+1
) are denoted
as
(
s′, a′
1, . . . , a′
N
)
. Each agent i aims to maximize its total
expected return Ri = ∑T
t=0 γtrt
i, where γ is the discount factor
and T is the time horizon. In the multi-agent system, the pol-
icy of each agent i is controlled by the parameter θi [26,27].
Policy gradient methods are fundamental approaches in re-
inforcement learning, aiming to maximize the expected long-
term return:
J(θ) = Eτ∼πθ[R(τ)],
(15)
R(τ) =
T
∑
t=0
γtrt,
(16)
where τ = (s0, a0, s1, a1, . . .) is the trajectory, and R(τ) is the
cumulative discounted return.
To optimize the policy parameters θ, we need to compute
the gradient of the objective function J(θ) with respect to θ.
According to the policy gradient theorem, the gradient of the
objective function is
∇θJ(θ) = Eτ∼πθ

T
∑
t=0
∇θ log πθ (at | st) · Qπθ (st, at)
,
(17)
where Qπθ (st, at) is the state-action value function. Estimat-
ing the gradient using Monte Carlo sampling can lead to high
variance and requires many trajectories to stabilize training.
Deterministic policy gradients reduce variance using a deter-
ministic policy (rather than a stochastic one) and are suitable
for continuous action spaces.
The deterministic policy: µθ(s) aims to maximize the ex-
pected return:
J(θ) = Es∼ρµ [Qµ (s, µθ(s))] ,
(18)
where ρµ is the state distribution. For deterministic policies,
the gradient is
∇θJ(θ) = Es∼ρµ
[
∇θµθ(s) · ∇aQµ(s, a)|a=µθ(s)
]
.
(19)
The gradient is propagated through the chain rule to the
gradient of the action-value function: ∇aQµ. Deterministic
policies reduce the randomness of actions, lowering the vari-
ance of gradient estimation. They are suitable for continuous
actions, directly outputting continuous actions without sam-
pling.
In multi-agent environments, each agent’s policy aﬀects
the learning of other agents, leading to a non-stationary envi-
ronment. This issue is addressed through centralized training
and decentralized execution.
Each agent: i aims to maximize its expected return:
J (θi) = Eo∼D [Ri (o, a1, . . . , aN)] ,
(20)
where Eo∼D represents the expectation of observation o on
the state distribution D.
For UAV i, the gradient is
∇θiJ (θi)
= Eo∼D
[
∇θiµi (oi; θi) · ∇aiQµ
i (oi, a1, . . . , aN; ϕi)
ai=µi(oi;θi)
]
,
(21)
where oi is the local observation of UAV i, Qµ
i is the central-
ized critic, which takes the states and actions of all UAVs as
input.
The goal of the critic is to minimize the temporal diﬀer-
ence error, and the loss function of the updated critic network

## Page 6

Gu J, et al.
Sci China Tech Sci
January 2026, Vol. 69, Iss. 1, 1120601:6
is
Li (ϕi) = E
[(
Qµ
i (oi, ai; ϕi) −
(
ri + γQµ
i
(o′
i, µi
(o′
i; θ′
i
) ; ϕ′
i
)))2]
,
(22)
where ri is the immediate reward, γ is the discount factor, o′
i
and µi
(
o′
i
)
are the next state and the action generated by the
policy.
In this way, each UAV can learn the optimal policy in a
multi-agent environment, considering the behavior of other
UAVs and potential collaboration. In dense obstacle envi-
ronments, conventional methods face signiﬁcant challenges,
including the curse of dimensionality, complex coordination
constraints, and diﬃculty balancing safety with eﬃciency.
These issues are particularly pronounced in UAV forma-
tion control, where machine learning-based approaches often
struggle with state space explosion and brittle obstacle avoid-
ance policies. As illustrated in Figure 4, our solution ad-
dresses these challenges through a dual approach: (1) threat-
aware subspace dimensionality reduction and (2) constrained
policy optimization.
The threat-aware feature extraction mechanism processes
LiDAR point cloud data to reconstruct spatial distributions
of high-threat obstacles and capture UAV kinematic char-
acteristics.
This approach reduces state space dimension-
ality while preserving critical safety information, improv-
ing DRL network eﬃciency. Additionally, robustness is en-
hanced through a constrained RL framework that utilizes a
safety-oriented penalty function, replacing conventional pos-
terior penalties to prohibit dangerous actions explicitly. This
guarantees the satisfaction of safety constraints [28–30].
3.2
Penalty function solution framework
Traditional methods rely on posterior penalty mechanisms,
which suﬀer from safety lag and low exploration eﬃciency.
Therefore, during the policy iteration process, we actively
avoid exploration paths that involve potentially dangerous
actions. In the policy iteration process, this paper proposes
a constraint optimization framework based on penalty func-
tions, which modiﬁes the objective function by introducing
motion constraints in the form of penalty functions.
The
modiﬁed objective function is
Jz (θi) = J (θi) −λi · Eo∼D,ai∼µi
[ϕ (ζi)] ,
(23)
where Jz (θi) is the objective function after introducing the
penalty function, λi is the penalty coeﬃcient used to bal-
ance exploration and exploitation, and Eo∼D,ai∼µi
[ϕ (ζi)] is the
penalty term, representing the cost generated during the ex-
ploration process, typically calculated based on the losses in-
curred by exploration behaviors.
The gradient of the modiﬁed objective function is
∇θiJz (θi) = ∇θiJ (θi) −λi · ∇θiEo∼D,ai∼µi
[ϕ (ζi)] ,
(24)
Figure 4
(Color online) Problem scenario considered in this paper.

## Page 7

Gu J, et al.
Sci China Tech Sci
January 2026, Vol. 69, Iss. 1, 1120601:7
where ∇θiJ (θi) is the gradient of the original objective func-
tion, and ∇θiEo∼D,ai∼µi
[ϕ (ζi)] is the gradient of the penalty
function.
Since ζi is a threat function and the observa-
tion distribution D(o) depends on the policies of all agents
µ = {µ1, . . . , µN}, the chain rule is used to decompose the
gradient of the penalty function:
∇θiEo∼D,ai∼µi
[ϕ (ζi)] = Eo∼D,ai∼µi
[∇θiµi (oi) · ∇aiϕ (ζi)] . (25)
Combining the original gradient with the penalty function
gradient, the ﬁnal policy gradient is obtained:
∇θiJz (θi)
= Eo∼Di,ai∼µi
[
∇θiµi (oi) (∇aiQi(o, a) −λi∇aiϕ (ζi))
|ai=µi(oi)
]
,
(26)
where ∇θiµi (oi) is the gradient of the policy function with
respect to the parameters θi, ∇aiQi (o, a1, . . . , aN) is the gra-
dient of the Critic network with respect to the action ai, and
∇aiϕ (ζi) is the gradient of the penalty function with respect
to the action ai. By adjusting λi, the inﬂuence of the penalty
function on policy optimization can be controlled, thereby
avoiding dangerous actions during the exploration process.
The Q-network of the Critic network is updated based on
the Bellman equation by minimizing the temporal diﬀerence
error to optimize the network parameters. The loss function
is
JQi (wi) = E(o,a,r,o′)
[1
2
(Qi(o, a) −(ri + γQ′
i
(o′, µθ′(o))))2
]
,
(27)
where ri is the immediate reward for agent i. Q′
i (o′, µθ′(o))
is the output of the target Critic network, used to stabilize
training. γ is the discount factor.
The gradient of the Critic network is
∇wiJQi = ∇wiQi(o, a) (Qi(o, a) −(ri + γQ′
i
(o′, µθ′(o)))) . (28)
3.3
Convergence and stability proof
This paper provides proofs of the algorithm’s convergence
and stability to ensure that the reinforcement learning algo-
rithm can ultimately ﬁnd the optimal solution and maintain
stable updates during training.
Assumption
1
Learning
Rate
Condition
(Robbins-
Monro):
∞
∑
k=0
βθi(k) = ∞,
∞
∑
k=0
β2
θi(k) < ∞,
(29)
where {βθi(k)} is the learning rate sequence for each agent.
The ﬁrst term ensures that the learning rate decays slowly
enough to allow the algorithm to update parameters until con-
vergence.
The second term ensures that the learning rate
decays fast enough to prevent noise accumulation, possibly
leading to divergence.
Assumption 2 (Diﬀerentiability): θi ∈Θi, wi ∈Wi are
compact sets. All neural network approximations are Lips-
chitz continuous.
Assumption 3 (Square Integrability of Martingale Diﬀer-
ence): The stochastic noise term δθi,k+1 satisﬁes
E [δθi,k+1 | Fk
] = 0,
E
[δθi,k+1
2 | Fk
]
⩽∞,
(30)
where Fk is the information domain up to time k. The ﬁrst
term ensures the zero-mean property of the noise, guarantee-
ing that the stochastic gradient is an unbiased estimate. The
second term ensures square integrability, limiting the noise
amplitude to prevent it from disrupting convergence.
Theorem 1 (Stochastic Approximation Theorem): Con-
sider the stochastic approximation iteration:
θi,k+1 = θi,k −βθi(k)∇θi,k Jz
(θi,k
) + δθi,k+1.
(31)
(1) Step size condition: Satisﬁes the Robbins-Monro con-
dition.
(2) Function property: ∇θi,k Jz
(θi,k
) is Lipschitz continuous
and globally asymptotically stable.
(3) Noise property: The noise δθi,k+1 is a martingale dif-
ference and square integrable.
(4) Boundedness: The iterative process {θi,k
} is almost
surely bounded.
Proof of Theorem 1:
When the above four conditions are satisﬁed, θi,k almost
surely converges to the stable point:
∇θi,k Jz
(θi,k
) = 0.
(32)
Condition (1) has already been satisﬁed in Assumption 1.
Below, we will be able to prove the other three conditions.
Lemma 1 ∇θi,k Jz
(θi,k
) is Lipschitz continuous and globally
asymptotically stable.
Proof: In the convergence analysis, Lipschitz continuity is
a key assumption used to ensure the boundedness of gradi-
ents and the stability of the update process. The Lipschitz
continuity of the policy network, Q-function, and penalty
function is explained separately below:
The parameterized form of µi (oi; θi) is a deep neural net-
work, and its activation function satisﬁes Lipschitz continu-
ity. Furthermore, the network weights θi lie within a compact
set Θi, so the gradient of the policy network satisﬁes
∇θiµi (oi; θi) −∇θiµi
(oi; θ′
i
) ⩽Lµi
θi −θ′
i
 ,
(33)
where Lµi is the Lipschitz constant determined by the net-

## Page 8

Gu J, et al.
Sci China Tech Sci
January 2026, Vol. 69, Iss. 1, 1120601:8
work structure and parameter range.
Q-Network Qi (o, a; wi) is also Lipschitz continuous.
Since the Q-network takes global observations o and joint
actions a as inputs, its gradient satisﬁes
∇aiQi (o, a; wi) −∇aiQi
(o, a′; wi
) ⩽LQi
a −a′ ,
(34)
where LQi is the Lipschitz constant of the Q-network, de-
pending on the network structure and the compactness of the
parameter space.
Penalty function ϕ (ζi) is a piecewise function, and its
derivative is continuous and piecewise Lipschitz at ζi , 0.
The gradient of the penalty function satisﬁes:
∇aiϕ (ζi) −∇aiϕ (ζ′
i
) ⩽Lϕi
ζi −ζ′
i
 ,
(35)
where Lϕi is the Lipschitz constant. Since the gradients of the
policy network, Critic network, and penalty function are all
Lipschitz continuous, the policy gradient ∇θi,k Jz
(θi,k
) is also
Lipschitz continuous. The Lipschitz constants of the individ-
ual components jointly determine their Lipschitz constant.
Lemma 2 Noise δθi,k+1 is a martingale diﬀerence and
square integrable.
The noise term in the policy gradient update must satisfy
the martingale diﬀerence property and be square integrable
to ensure the convergence of stochastic approximation.
Proof: The policy gradient estimation noise for each agent
i is
δθi,k+1 = ˆ∇θiJz
(θi,k
) −E
[ ˆ∇θiJz
(θi,k
) | Fk
]
,
(36)
where ˆ∇θiJz
(θi,k
) is the stochastic gradient estimate of the ob-
jective function Jz (θi) . E
[ ˆ∇θiJz
(θi,k
) | Fk
]
is the conditional
expectation of the stochastic gradient. Fk is the information
set up to step k.
Since the samples in the experience replay buﬀer D are
independent of the current parameters θi,k,the expectation of
the noise term is zero:
E [δθi,k+1 | Fk
] = 0.
(37)
Therefore, {δθi,k+1
} is a martingale diﬀerence sequence
(MDS).
Because the policy network, Q-function, and penalty func-
tion are all Lipschitz continuous, the gradient norms are
bounded:
∇θiJz
(θi,k
) ⩽Lθi,
(38)
where Lθi is an upper bound related to the Lipschitz constant.
Thus, the norm of the stochastic gradient also satisﬁes this
bound. The variance of the noise term satisﬁes
E
[δθi,k+1
2 | Fk
]
⩽2E
[ ˆ∇θiJz
(θi,k
)
2]
⩽2L2
θi < ∞.
(39)
This indicates that {δθi,k+1
} is a square integrable martin-
gale diﬀerence sequence.
Lemma 3 The iterative process {θi,k
} is almost surely
bounded.
Using ordinary diﬀerential equations (ODEs) to simplify
the analysis of optimization algorithms facilitates the study
of system behavior and stability. Through ODEs and Lya-
punov theory, convergence can be intuitively proven, and pa-
rameter behavior near boundaries can be eﬀectively handled,
ensuring system stability.
Proof: The continuous dynamic system is described by the
ODE:
˙θi(t) = −∇θiJz (θi(t)) .
(40)
There exists a locally asymptotically stable equilibrium
point θ∗
i , which satisﬁes:
∇θiJz
(θ∗
i
) = 0.
(41)
By mapping discrete updates to the continuous system,
convergence can be proven through stability analysis.
To prove TACO’s convergence, we employ Lyapunov sta-
bility theory. By constructing a Lyapunov function and an-
alyzing its time derivative, we prove the stability of the dy-
namic system at local minima.
First, we construct a candidate Lyapunov function:
L (θi) = Jz (θi) −Jz
(θ∗
i
) ,
(42)
where θ∗
i is a local minimum of the objective function Jz (θi)
satisfying
∇θiJz
(θ∗
i
) = 0.
(43)
This function satisﬁes two key properties: L (θi) ⩾0, be-
cause Jz
(
θ∗
i
)
is a local minimum. L
(
θ∗
i
)
= 0, meaning θ∗
i is
the minimum point of the Lyapunov function.
We compute the time derivative of the Lyapunov function
along the trajectory of the dynamic system. The dynamic
system is described by the continuous-time equation:
˙θi(t) = −∇θiJz (θi(t)) .
(44)
Taking the derivative of L (θi) along the system trajectory,
we obtain
dL (θi)
dt
= ∇θiJz (θi)T ˙θi = −
∇θiJz (θi)
2 ⩽0.
(45)
This shows that the Lyapunov function monotonically de-
creases along the system trajectory, and the derivative is zero
if and only if ∇θiJz (θi) = 0, meaning the system reaches the
equilibrium point θ∗
i .
When the parameters approach the boundary of the feasi-

## Page 9

Gu J, et al.
Sci China Tech Sci
January 2026, Vol. 69, Iss. 1, 1120601:9
ble region ∂Θi, we ensure that the parameters do not exceed
the boundary through a projection operation ΓΘi. The pro-
jected update rule is
θi,k+1 = ΓΘi
[θi,k −η∇θiJz
(θi,k
)] ,
(46)
where η is the step size. In the continuous-time dynamic sys-
tem, the projected derivative is deﬁned as
dL (θi)
dt
= ∇θiJz (θi)T · lim
η→0
ΓΘi
[θi −η∇θiJz (θi)] −θi
η
.
(47)
According to the properties of the projection operator, for
any θi ∈Θi and vector ϖ, we have
(θi −ΓΘi
[θi −ηϖ])T (ΓΘi
[θi −ηϖ] −θi
) ⩽0.
(48)
Substituting ϖ = ∇θiJz (θi), we obtain
(θi −ΓΘi
[θi −η∇θiJz (θi)])T
(ΓΘi
[θi −η∇θiJz (θi)] −θi
) ⩽0.
(49)
Therefore, the time derivative satisﬁes
dL (θi)
dt
=∇θiJz (θi)T · lim
η→0
ΓΘi
[θi −η∇θiJz (θi)] −θi
η
⩽0.
(50)
This shows that even near the boundary, the time deriva-
tive of the Lyapunov function remains non-positive, and the
system maintains stability near the boundary. According to
Lyapunov stability theory, if there exists a Lyapunov func-
tion L (θi) satisfying L (θi) ⩾0 and L
(
θ∗
i
)
= 0, and its
time derivative dL(θi)
dt
⩽0 with the derivative being zero only
when θi = θ∗
i , then the dynamic system is locally asymp-
totically stable at θ∗
i . In TACO, the constructed Lyapunov
function satisﬁes these conditions, so the dynamic system
˙θi = −∇θiJz (θi) is locally stable at the local minimum θ∗
i ,
meaning the parameter sequence {θi,k
} almost surely con-
verges to θ∗
i .
3.4
Threat-aware cooperative control for multi-UAV
DRL framework
3.4.1 Observation space
Figure 3 illustrates the process of point cloud clustering and
obstacle detection. In environments densely populated with
obstacles, processing all detected obstacles typically results
in signiﬁcant computational overhead, which can impede the
convergence speed of training.
To address this issue, we
preprocess LiDAR point cloud data by prioritizing extract-
ing information about nearby critical obstacles while ﬁltering
out non-essential targets. Subsequently, these optimized fea-
tures are combined with the UAV’s own state and the states
of neighboring UAVs to construct a more concise observa-
tion vector. This approach signiﬁcantly reduces computa-
tional complexity, enhances decision-making eﬃciency, and
improves the system’s overall stability. Ultimately, the sys-
tem can achieve rapid and robust obstacle avoidance and co-
operative control in highly complex environments.
The observation vector ot
i contains critical environmental
and state information necessary for task execution. Speciﬁ-
cally, the observation vector includes the UAV’s position vec-
tor pt and velocity vector vt. Additionally, the UAV perceives
only the relative positions of obstacles within its local area,
represented by the obstacle position vector oobs .
As shown in Figure 3, a point cloud clustering algorithm
is employed to distinguish obstacles. The UAV calculates the
position of the nearest point within each cluster to measure
its distance to the obstacles accurately. At the same time, the
UAV can monitor the relative positions and velocities of other
UAVs, denoted by oo U and vo U, respectively. These data are
integrated into the UAV’s observation vector, structured as
follows:
ot
i =
[
pt, vt, oobs, oo U, vo U
]
.
(51)
This observation vector provides the UAV with compre-
hensive state information, including its own status and the
characteristics of its surrounding environment.
This ap-
proach allows the UAV to gradually learn to make eﬀective
decisions in dense obstacle environments based on dynamic
changes.
3.4.2 Action space
In multi-UAV collaborative tasks, each UAV’s motion control
is deﬁned within a continuous action space, allowing for ﬂex-
ible adjustment of velocity commands in a two-dimensional
plane. This design enables UAVs to dynamically adapt their
motion states based on environmental changes, thereby ef-
fectively maintaining formation structures and avoiding ob-
stacles.
For the UAV labeled i, its velocity command can be ex-
pressed as
vc
i =
[
vc
xi, vc
yi
]
,
(52)
where each velocity component ranges from −vmax to vmax ,
representing the maximum speed limits in the horizontal and
vertical directions. The system calculates the UAV’s direc-
tional adjustment φi and target speed Vi through the policy
neural network. Based on this, combined with the introduced
noise term ϕnoise
i
, the actual velocity commands can be com-
puted using the following formulas:

vc
xi = Vi cos
(
φi + ϕnoise
i
)
,
vc
yi = Vi sin
(
φi + ϕnoise
i
)
.
(53)

## Page 10

Gu J, et al.
Sci China Tech Sci
January 2026, Vol. 69, Iss. 1, 1120601:10
This design considers theoretical motion control and sim-
ulates real-world uncertainties by introducing noise terms,
thereby enhancing the system’s robustness.
3.4.3 Network architecture
The network architecture of our multi-UAV obstacle avoid-
ance system employs two deep neural networks (DNNs) to
implement the actor-critic framework.
The actor network
maps environmental observations to optimal actions, fea-
turing three fully connected (FC) layers with 128 neurons
each.
The ﬁrst two hidden layers utilize Rectiﬁed Linear
Unit (ReLU) activations, while the output layer applies hy-
perbolic tangent activation to produce bounded action values
within the range of [−1, 1]. Meanwhile, the critic network
adopts an identical three FC layer architecture (128 neurons
per layer) to evaluate state-action values, with its single neu-
ron output layer using linear activation for unrestricted value
estimation. This symmetric yet functionally distinct architec-
ture enables eﬀective policy optimization while maintaining
computational eﬃciency.
3.4.4 Reward function
In complex environments, achieving multiple objectives and
completing diverse tasks simultaneously presents signiﬁ-
cant challenges, primarily due to potential conﬂicts be-
tween temporal demands and priorities. For multi-UAV sys-
tems, obstacle avoidance requires rapid response capabilities,
while multi-agent coordination relies on global long-term
planning policies.
Traditional single-scale reward mech-
anisms typically focus solely on short-term or long-term
goals, limiting the system’s ability to eﬀectively balance
the two, potentially leading to overly conservative decision-
making or ineﬃcient task execution.
This paper pro-
poses a multi-timescale reward function that integrates short-
term, medium-term, and long-term objectives by introducing
weighting coeﬃcients to address this issue. This method en-
sures that immediate demands are met while also considering
global planning goals. Compared to traditional approaches,
this strategy signiﬁcantly enhances the system’s decision-
making ﬂexibility, robustness, and environmental adaptabil-
ity, optimizing UAVs’ operational eﬃciency in complex
scenarios.
The reward function rt designed in this study con-
sists of three components:
short-term reward rs
t , mid-
term reward rm
t , and long-term reward rl
t.
The system
can optimize the decision-making process across diﬀerent
timescales by assigning corresponding weighting coeﬃcients
to each component.
The mathematical expression is as
follows:
rt = α1 × rs
t + α2 × rm
t + α3 × rI
t .
(54)
3.4.5 Experience replay design
Experience Replay’s design addresses non-stationarity and
sample eﬃciency in multi-agent environments by storing and
reusing historical experiences. The replay buﬀer D stores
interaction data at each time step, including states, actions,
rewards, and following states, in the form of (ot, at, rt, ot+1).
A batch of experiences is randomly sampled during train-
ing to update the policy and value function networks. The
core functions of experience replay include breaking tempo-
ral correlations, improving sample eﬃciency, and mitigating
non-stationarity.
By randomly sampling historical experi-
ences, agents can learn from diverse data, reducing ﬂuctu-
ations during training and enhancing the stability and con-
vergence of policies. This mechanism is particularly crucial
in multi-agent collaborative tasks, enabling agents to learn
optimal policies in complex environments.
Such a strategy is particularly eﬀective for tasks that re-
quire an in-depth understanding of environmental dynam-
ics, such as multi-UAV formation control, where the agent
must grasp the relative motion among formation members
and obstacles. The detailed training process is outlined in
Algorithm 1.
4
Simulation and analysis
4.1
Simulation environment
The experimental environment was constructed using Air-
Sim, a high-precision virtual simulation platform based on
Unreal Engine that can provide highly realistic physical sim-
ulations for robotic systems. All experiments were conducted
on a desktop computer equipped with 64 GB of RAM and a
GeForce RTX 4090 GPU. The formation control algorithm
proposed in this study is based on a reinforcement learning
framework and implemented using PyTorch.
Figure 5 illustrates our simulation environment: a 4 m ×
8 m ﬂat terrain densely populated with UAVs and trees. The
experiment employed a ﬁve-UAV formation using identical
quadrotors (15 cm diameter each), equipped with VLP-16 Li-
DAR sensors (10 Hz scan rate, 100 m range, 0.1◦−0.4◦angu-
lar resolution). To create a challenging obstacle environment,
we randomly distributed 50 trees with minimum spacing con-
straints to prevent overlap, while ensuring obstacle-free start
and target zones for all UAVs. To evaluate the formation’s
navigation capabilities in a dense obstacle environment, the
initial and target positions of the UAVs were conﬁned to re-
gions within 1.5 meters on either side of the area.
Figure 5(a) presents a top-down 3D visualization of the
training environment, depicting ﬁve UAVs navigating a
densely obstructed area with their ﬂight trajectories marked
in diﬀerent colors. The red dashed boxes demarcate two crit-
ical zones: (1) a densely treed region corresponding to the

## Page 11

Gu J, et al.
Sci China Tech Sci
January 2026, Vol. 69, Iss. 1, 1120601:11
Algorithm 1
Training algorithm for multi-UAV
Initialize the parameters of the Critic and Actor networks for UAV
Initialize an empty replay buﬀer
for episode = 1 to number of episodes do
for t = 1 to length of episode do
Compute threat-aware function (oi, ai) →ζi
For each UAV i, select action at
i
Interact with the environment, obtain a multi-time-scale reward and observe the next state for the next time step.
Store the quadruple array (ot, at, rt, ot+1) in the replay buﬀer D
Randomly select experiences from the replay buﬀer D
for UAV i = 1 to N do
Update the parameters of the Critic networks. Actor update with penalized objective Eo∼D,ai∼µi ⌈ϕ (ζi)⌉.
Perform a soft update on the parameters of the Target Critic and Target Actor networks.
end for
end for
end for
Figure 5
(Color online) AirSim simulation of Multi-UAV formation control. (a) Top-down 3D map; (b) snapshot of the environment in
AirSim at episode 80.
80th training episode and (2) the ﬁnal episode, both rep-
resenting high-complexity scenarios that signiﬁcantly chal-
lenge multi-UAV formation control. A circular target zone
with a radius of 0.5 m is marked, requiring precise formation
maintenance during the ﬁnal approach, which is particularly
critical in the terminal ﬂight phase. Figure 5(b) provides a de-
tailed view of the forest environment within AirSim, focus-
ing on the area enclosed by the red dashed box in Figure 5(a).
The colored trajectories (with blue solid lines indicating pri-
mary ﬂight directions) reveal how the UAVs maintain for-
mation integrity while dynamically avoiding obstacles in this
complex, densely vegetated environment.
4.2
Training analysis
4.2.1 Training settings
The primary objective of this study is to train UAVs to
achieve formation control in dense obstacle environments
and successfully reach the target area. The UAVs completed
a total of 105 training episodes during the training process.
Table 2 provides a detailed list of the key parameters for Al-
gorithm 1, while Table 1 outlines the speciﬁc parameter con-
ﬁgurations for the UAV model. To ensure consistency and
reliability in the experimental evaluation, all subsequent ex-
periments strictly adhered to the parameter settings speciﬁed
in Tables 1 and 2.
For a comprehensive evaluation, we compare our proposed
algorithm against ﬁve baseline methods in Table 3, selected
to represent most UAV control and collision avoidance ap-
proaches.
To ensure robust performance comparisons, this paper
computed the Root Mean Square Error (RMSE) and variance
using training data from episodes exceeding 2 × 104 steps.
This approach focuses on stable, converged behavior while
mitigating the inﬂuence of early-training ﬂuctuations. Al-
though collisions are treated as task failures, the simulation
continues until the preset episode terminates. This design
enables the system to extract learning signals from failures,
iteratively reﬁne its strategy, and enhance obstacle avoidance
capabilities across episodes.
4.2.2 Training analysis
The comparative analysis in Figure 6 and Table 4 shows
apparent performance diﬀerences among UAV control algo-
rithms. TACO achieves faster convergence within 14000 iter-
ations while maintaining low control error with an RMSE of
3.68 and a slight variance of 13.56, resulting in remarkably
stable training dynamics as evidenced by the table and ﬁgure

## Page 12

Gu J, et al.
Sci China Tech Sci
January 2026, Vol. 69, Iss. 1, 1120601:12
Table 1
Simulation parameters
Parameters
Value
Number of UAVs
5
UAVs radius (m)
7.5 × 10−2
Task area (m2)
32
Minimum safety distance (m)
1 × 10−2
Target area radius rg
max(m)
0.50
Speed range (m/s)
0 –−0.50
Acceleration range (m/s2)
0 –−0.40
Table 2
Algorithm parameters
Parameters
Value
Discount factor
0.95
Inertial update rate
10−2
Experience pool size
5 × 105
Batch size
128
Critic network learning rate
10−3
Actor network learning rate
10−4
Number of episodes
105
Length of episode
170
α1, α2, α3
0.35, 0.30, 0.35
Number of fully connected layers
3
Number of hidden layers
3
Size of fully connected layer
64
Size of hidden layer
64
Table 3
Comparison of UAV formation control methods based on
key technical dimensionsa)
Algorithm
State space processing
Obstacle avoidance method
TACO [25,26]
Threat-aware subspace
Penalty function
TACO-P [28,29]
Threat-aware subspace
–
TACO-TAS-P [30]
–
–
TACO-CBF [31]
Threat-aware subspace
CBF
TACO-CORA [22]
Threat-aware subspace
CORA
TACO-AERed [17]
AERed
Penalty function
a) TACO, Threat-aware constrained optimization; P, the algorithm is miss-
ing the Penalty function; TAS-P, the algorithm is missing the threat-aware sub-
space and Penalty function; CBF, control barrier function; CORA, complex
obstacle avoidance reward function; AERed, autoencoder reduction method.
data. Ablation studies systematically demonstrate the criti-
cal roles of these components. The TACO-P variant removes
the penalty function, while the threat perception capability is
retained. However, degraded performance is observed, with
an RMSE of 4.69, 24000 iterations required for convergence,
and higher variance. A more substantial performance decline
is observed in TACO-TAS-P, which eliminates both compo-
nents. This variant demonstrates the worst metrics across all
categories, including the highest RMSE of 5.05, the most sig-
niﬁcant variance of 25.51, and the most unstable training pat-
terns. Alternative methods show diﬀerent trade-oﬀs. TACO-
CBF replaces the penalty function with a control barrier func-
tion for safety. However, this leads to excessive avoidance
behaviors and lower learning eﬃciency.
As a result, the
RMSE is 4.82, with convergence requiring 22000 iterations
and a variance of 20.28. Compared to TACO, TACO-CBF
has an 18.22% higher RMSE and takes 36.36% longer to
converge. TACO-CORA improves obstacle modeling with
complex reward adjustments. However, this complicates the
reward function, making convergence more diﬃcult, requir-
ing 52000 iterations. TACO-AERed uses autoencoders for
state dimensionality reduction. This improves computational
eﬃciency but sacriﬁces crucial threat information. This re-
sults in an incomplete performance proﬁle, with an RMSE of
4.54 and convergence taking 35000 iterations.
4.3
Test analysis
This study evaluates four UAV swarm coordination algo-
rithms (TACO, TACO-CBF, TACO-P, TACO-TAS-P, TACO-
CORA, and TACO-AERed) in cluttered environments
through systematic experimentation. The evaluation frame-
work employs Monte Carlo simulation across 1000 randomly
conﬁgured test scenarios. Each scenario features a 4 m×8 m
operational area containing 50 randomly placed obstacles
with strictly maintained minimum inter-obstacle spacing of
0.65 m. The experimental setup involves a ﬁve-UAV forma-
tion, with initial positions and target destinations randomly
assigned within designated zones to ensure unbiased perfor-
mance assessment while maintaining consistency with train-
ing conditions.
4.3.1 Results and analysis
To evaluate UAV collision avoidance and formation stability
in dense obstacles, metrics included minimum obstacle dis-
tance dobs
min, inter-UAV distance dUAV
min , average speed V, task
completion time ts, and success rate. dobs
min measures obsta-
cle avoidance, dUAV
min reﬂects formation stability, V assesses
movement eﬃciency, and ts tracks the time for the last UAV
to reach the target.
Table 5 presents a comprehensive comparative analysis of
six UAV formation control algorithms, focusing on collision
avoidance and formation stability. TACO demonstrates supe-
rior performance by leveraging its threat-aware subspace fea-
ture extraction mechanism to process LiDAR data eﬀectively.
This approach reduces state space dimensionality while pri-
oritizing high-threat obstacles, enabling TACO to achieve
optimal safety metrics, including the highest minimum ob-
stacle distance of 4.12 × 10−2 m and in-ter-UAV distance of
4.34 × 10−2 m. The algorithm maintains eﬃcient operation
with an average speed of 4.25 × 10−1 m per second and com-
pletes tasks in just 14.10 seconds while achieving a remark-
able success rate of 93.10%.
In contrast, TACO-CBF incorporates Control Barrier
Functions to enhance safety through strict collision avoid-

## Page 13

Gu J, et al.
Sci China Tech Sci
January 2026, Vol. 69, Iss. 1, 1120601:13
Figure 6
(Color online) Comparison of average reward curves.
Table 4
Performance comparison of UAV formation control algorithms in terms of RMSE
Algorithm
RMSE
Variance
Convergence episodes (×1000)
RMSE improvement
vs. TACO-CBF (%)
Convergence episodes
improvement vs. TACO-CBF (%)
TACO
3.68
13.56
14
18.22
36.36
TACO-CBF
4.50
20.28
22
–
–
TACO-P
4.69
22.01
24
–
–
TACO-TAS-P
5.05
25.51
–
–
–
TACO-CORA
4.61
21.22
52
–
–
TACO-AERed
4.54
20.57
35
–
–
Table 5
Performance comparison of UAV formation control algorithms in obstacle-density environments
Algorithm
dobs
min (m)
dUAV
min (m)
V (m/s)
tg (s)
Success rate (%)
TACO
4.12 × 10−2
4.34 × 10−2
4.25 × 10−1
14.10
93.10
TACO-CBF
2.71 × 10−2
3.59 × 10−2
4.23 × 10−1
14.20
88.20
TACO-P
1.47 × 10−2
3.81 × 10−2
4.21 × 10−1
14.60
83.70
TACO-TAS-P
6.70 × 10−3
6.90 × 10−2
4.23 × 10−1
–
–
TACO-CORA
1.96 × 10−2
3.20 × 10−2
4.22 × 10−1
14.40
85.40
TACO-AERed
2.42 × 10−2
2.88 × 10−2
4.21 × 10−1
14.20
85.20
ance constraints, resulting in improved minimum obstacle
distance of 2.71 × 10−2 m. However, this safety improve-
ment comes at the cost of reduced operational eﬃciency,
as evidenced by slower speeds and increased task comple-
tion time of 14.20 s, leading to a slightly lower success
rate of 88.20%. The penalty function-free TACO-P variant
shows signiﬁcant performance degradation with the longest
task completion time of 14.60 s and the lowest success rate
of 83.70%, due to its inability to eﬀectively enforce safety
constraints during training. TACO-TAS-P, which omits the
threat-aware subspace feature extraction, performs poorly
across all metrics as its inability to prioritize high-risk areas
leads to deﬁcient collision avoidance and compromised for-
mation stability. While TACO-CORA attempts to improve
safety through a sophisticated reward function, this com-
plexity negatively aﬀects learning eﬃciency, resulting in in-
creased task completion time of 14.40 s and reduced success
rate of 85.40%. Finally, TACO-AERed achieves computa-
tional eﬃciency through dimensionality reduction, but suf-
fers from information loss in critical state data, leading to
suboptimal decision-making, with a success rate of 85.20%
and increased task completion time of 14.20 s.
Figure 7 presents a comparative analysis of four TACO
variant algorithms for multi-UAV trajectory planning in a
dense obstacle environment. The red dashed boxes highlight
high-threat areas to emphasize diﬀerences: TACO, through

## Page 14

Gu J, et al.
Sci China Tech Sci
January 2026, Vol. 69, Iss. 1, 1120601:14
the construction of a threat-aware subspace, enables agents
to proactively avoid dangerous regions, while the introduc-
tion of a penalty function further optimizes the paths, result-
ing in more stable policy convergence and avoiding unnec-
essary exploratory actions. In contrast, TACO-P, lacking a
penalty function, exhibits greater path ﬂuctuations. In the
areas marked by the red dashed circles, the UAV trajecto-
ries show more pronounced oscillations, with some agents
even entering high-threat zones, indicating reduced stability
and safety in path planning. TACO-CBF, on the other hand,
enhances safety constraints among UAVs through CBF, en-
suring agents maintain suﬃcient spacing to avoid proxim-
ity or entry into high-risk areas.
However, due to CBF’s
overly strict safety restrictions, UAV movement may stag-
nate and path search eﬃciency may decrease in complex en-
vironments, where UAVs stagnate or detour excessively dur-
ing path exploration. This not only diminishes exploration
capability but also reduces mission execution eﬃciency. The
weakest baseline algorithm, TACO-TAS-P, which lacks both
threat-aware subspace and penalty function, demonstrates the
lowest path quality.
Figure 8 shows a detailed comparison of the trajectory dif-
ferences among the algorithms in a dense obstacle environ-
ment, focusing on an enlarged view at frame 68. This view
highlights the UAV behavior of each algorithm, making it
easier to compare their formation control performance. Un-
der the control of the TACO algorithm, the UAV trajectories
are relatively smooth, with natural obstacle-avoidance be-
haviors, and the agents maintain appropriate spacing, avoid-
ing excessive clustering or dispersion.
Particularly in the
areas marked by the red dashed circles, the UAVs eﬀec-
tively avoid high-threat obstacles without signiﬁcant stagna-
tion or abnormal twists. This indicates that TACO’s TAS and
penalty function can guide agents to perform reasonable ob-
stacle avoidance in complex environments, ensuring mission
safety and stability. Under the TACO-CBF algorithm, the
agents strictly adhere to safety spacing, with more aggres-
sive obstacle-avoidance paths that prevent proximity or en-
try into high-risk zones. However, due to the stringent safety
constraints imposed by the CBF, the exploration capability of
the UAVs is somewhat limited. While this design enhances
absolute safety, it also reduces convergence eﬃciency, result-
Figure 7
(Color online) Flight trajectories of UAV formation control algorithms across dense obstacle scenarios. (a) TACO; (b) TACO-CBF;
(c) TACO-P; (d) TACO-TAS-P.
Figure 8
(Color online) Detailed analysis of UAV trajectories in dense obstacle environments. (a) TACO; (b) TACO-CBF; (c) TACO-P.

## Page 15

Gu J, et al.
Sci China Tech Sci
January 2026, Vol. 69, Iss. 1, 1120601:15
ing in longer, more circuitous paths that impact mission ex-
ecution eﬃciency. The TACO-P variant removes the penalty
function module, leading to greater instability in trajectory
performance. As seen in the ﬁgure, the agents’ trajectories
within the red dashed circle areas show signiﬁcant deviations,
with some paths entering threat zones and even unnecessary
exploratory contacts. This suggests that without the penalty
function, the constraints during policy optimization are insuf-
ﬁcient, causing larger trajectory oscillations and less stable
behavior in high-threat regions.
5
Conclusion
The TACO algorithm reduces state space dimensionality
by reconstructing high-threat obstacle distribution and UAV
kinematics from LiDAR data.
A safety-oriented penalty
function is applied in a constrained RL framework to pre-
vent dangerous actions, ensuring that the policy always meets
safety constraints. The convergence and stability of the algo-
rithm are proven using Lyapunov stability theory. Compara-
tive experiments in the AirSim environment show that our al-
gorithm outperforms state-of-the-art methods, with a 36.36%
improvement in convergence speed, 18.22% increase in sta-
bility, and a 5.6% rise in mission success rate.
Acknowledgements
This work was supported by the National Natural
Science Foundation of China (Grant Nos. U20B2001, 12102178).
References
1
Xue Y, Chen W. A UAV navigation approach based on deep reinforce-
ment learning in large cluttered 3D environments. IEEE Trans Veh
Technol, 2023, 72: 3001–3014
2
Cheng N, Wu S, Wang X, et al. AI for UAV-assisted IoT applications:
A comprehensive review. IEEE Internet Things J, 2023, 10: 14438–
14461
3
Fax J A, Murray R M. Information ﬂow and cooperative control of
vehicle formations. IEEE Trans Automat Contr, 2004, 49: 1465–1476
4
Jadbabaie A, Lin J, Morse A S. Coordination of groups of mobile au-
tonomous agents using nearest neighbor rules. IEEE Trans Automat
Contr, 2003, 48: 988–1001
5
Kushleyev A, Mellinger D, Powers C, et al. Towards a swarm of agile
micro quadrotors. Auton Robot, 2013, 35: 287–300
6
Michael N, Fink J, Kumar V. Cooperative manipulation and transporta-
tion with aerial robots. Auton Robot, 2011, 30: 73–86
7
Matos D M, Costa P, Sobreira H, et al. Eﬃcient multi-robot path plan-
ning in real environments: a centralized coordination system. Int J
Intell Robot Appl, 2025, 9: 217–244
8
Nowzari C, Cort´es J. Distributed event-triggered coordination for av-
erage consensus on weight-balanced digraphs. Automatica, 2016, 68:
237–244
9
Zheng D, Zhang H, Zheng Q. Consensus analysis of multi-agent sys-
tems under switching topologies by a topology-dependent average
dwell time approach. IET Control Theor Appl, 2017, 11: 429–438
10
Polycarpou M M, Yang Y, Passino K M. Cooperative control of dis-
tributed multi-agent systems. IEEE Control Syst Mag, 2001, 21: 1-27
11
Yan L, Stouraitis T, Vijayakumar S. Decentralized ability-aware adap-
tive control for multi-robot collaborative manipulation. IEEE Robot
Autom Lett, 2021, 6: 2311–2318
12
Saska M, Von´asek V, Krajn´ık T, et al. Coordination and navigation of
heterogeneous MAV-UGV formations localized by a ‘hawk-eye’-like
approach under a model predictive control scheme. Int J Robotics Res,
2014, 33: 1393–1412
13
Francesca G, Brambilla M, Brutschy A, et al. AutoMoDe-Chocolate:
Automatic design of control software for robot swarms. Swarm Intell,
2015, 9: 125–152
14
Wang W, Ru L, Lv M, et al. Layered autonomous decision framework
and DDQN-enhanced training for the BVR air game. Guid Navigat
Control, 2025, 05: 41–55
15
Hao S, Zhang Z, Huo M, et al. Enhancing unmanned ground vehi-
cle evasion through generative adversarial imitation learning in UAV
pursuit scenarios. Guid Navigat Control, 2025, 05: 149–154
16
Khamis A, Hussein A, Elmogy A. Multi-robot task allocation: A re-
view of the state-of-the-art. In: Koubaa A, Martłnez-de Dios J, eds.
Cooperative Robots and Sensor Networks 2015. Studies in Computa-
tional Intelligence, vol 604. Cham: Springer, 2015. 31–51
17
Anjali , Dai H N, Kumar J, et al. AERed: An autoencoder-decoder
dimensionality reduction method for wearable-based human activity
recognition. IEEE Sens J, 2023, 23: 29804–29814
18
Huang X, Ling J, Yang X, et al. Multi-agent mix hierarchical deep
reinforcement learning for large-scale ﬂeet management. IEEE Trans
Intell Transp Syst, 2023, 24: 14294–14305
19
Liu C, Zhu F, Liu Q, et al. Hierarchical Reinforcement learning with
automatic sub-goal identiﬁcation. IEEE CAA J Autom Sin, 2021, 8:
1686–1696
20
Wang Y, Zhu F. Distributed dynamic event-triggered control for multi-
agent systems with quantization communication. IEEE Trans Circuits
Syst II, 2024, 71: 2054–2058
21
Qin L, He X, Yan R, et al. Distributed sensor fault diagnosis for a
formation of multi-vehicle systems. J Franklin Inst, 2019, 356: 791–
818
22
Miranda V R F, Neto A A, Freitas G M, et al. Generalization in deep
reinforcement learning for robotic navigation by reward shaping. IEEE
Trans Ind Electron, 2024, 71: 6013–6020
23
Gangopadhyay B, Dasgupta P, Dey S. Safe and stable RL (S2RL)
driving policies using control barrier and control Lyapunov functions.
IEEE Trans Intell Veh, 2023, 8: 1889–1899
24
Cheng M, He S, Lin M, et al. RL and DRL based distributed user ac-
cess schemes in Multi-UAV networks. IEEE Trans Veh Technol, 2025,
74: 5241–5246
25
Garc´ıa J, Fern´andez F. A comprehensive survey on safe reinforcement
learning. J Mach Learn Res, 2015, 16(1): 1437-1480.
26
Zeng D, Jiang Y, Wang Y, et al. Robust adaptive control barrier func-
tions for input-aﬃne systems: Application to uncertain manipulator
safety constraints. IEEE Control Syst Lett, 2024, 8: 279–284
27
Chen Y F, Liu M, Everett M, et al. Decentralized non-communicating
multi-agent collision avoidance with deep reinforcement learning. In:
2017 IEEE International Conference on Robotics and Automation
(ICRA). Singapore, 2017
28
Pan T, Dong H, Deng B, et al. Robust cross-drone multi-target asso-
ciation using 3D spatial consistency. IEEE Signal Process Lett, 2024,
31: 71–75
29
Zhu Y, Mottaghi R, Kolve E, et al. Target-driven visual navigation in
indoor scenes using deep reinforcement learning. In: 2017 IEEE Inter-
national Conference on Robotics and Automation (ICRA). Singapore,
2017. 3357-3364
30
Yu G, Shen Y. Event-triggered distributed optimisation for multi-agent
systems with transmission delay. IET Control Theor Appl, 2019, 13:
2188–2196
31
Jankovic M, Santillo M, Wang Y. Multiagent systems with CBF-based
controllers: Collision avoidance and liveness from instability. IEEE
Trans Contr Syst Technol, 2024, 32: 705–712
