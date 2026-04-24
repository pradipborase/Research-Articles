# Deep_Reinforcement_Learning_Multi-UAV_Trajectory_Control_for_Target_Tracking.pdf

## Page 1

IEEE INTERNET OF THINGS JOURNAL, VOL. 8, NO. 20, OCTOBER 15, 2021
15441
Deep Reinforcement Learning Multi-UAV
Trajectory Control for Target Tracking
Jiseon Moon
, Member, IEEE, Savvas Papaioannou
, Member, IEEE, Christos Laoudias
, Member, IEEE,
Panayiotis Kolios
, and Sunwoo Kim
, Senior Member, IEEE
Abstract—In this article, we propose a novel deep rein-
forcement learning (DRL) approach for controlling multiple
unmanned aerial vehicles (UAVs) with the ultimate purpose of
tracking multiple ﬁrst responders (FRs) in challenging 3-D envi-
ronments in the presence of obstacles and occlusions. We assume
that the UAVs receive noisy distance measurements from the
FRs which are of two types, i.e., Line of Sight (LoS) and non-
LoS (NLoS) measurements and which are used by the UAV
agents in order to estimate the state (i.e., position) of the FRs.
Subsequently, the proposed DRL-based controller selects the
optimal joint control actions according to the Cramér–Rao lower
bound (CRLB) of the joint measurement likelihood function to
achieve high tracking performance. Speciﬁcally, the optimal UAV
control actions are quantiﬁed by the proposed reward function,
which considers both the CRLB of the entire system and each
UAV’s individual contribution to the system, called global reward
and difference reward, respectively. Since the UAVs take actions
that reduce the CRLB of the entire system, tracking accuracy is
improved by ensuring the reception of high quality LoS measure-
ments with high probability. Our simulation results show that the
proposed DRL-based UAV controller provides a highly accurate
target tracking solution with a very low runtime cost.
Index Terms—Multiagent deep reinforcement learning (DRL),
multitarget tracking, unmanned aerial vehicle (UAV).
I. INTRODUCTION
N
OWADAYS, unmanned aerial vehicles (UAVs) have
become a promising technological platform offering high
mobility, ﬂexible deployment, and low cost [1], [2]. Thanks to
the aforementioned advantages, UAVs are widely operated in
various application scenarios, such as wireless communication
support [3]–[5], surveillance [6], delivery [7], [8], and search
Manuscript received November 22, 2020; revised February 6, 2021;
accepted March 19, 2021. Date of publication April 19, 2021; date of
current version October 7, 2021. This work was supported by the MSIT
(Ministry of Science and ICT), South Korea, through the ITRC (Information
Technology Research Center) Support Program under Grant IITP-2021-2017-
0-01637, supervised by the IITP (Institute for Information & Communications
Technology Planning & Evaluation). The work of Savvas Papaioannou,
Christos Laoudias, and Panayiotis Kolios was supported in part by the
European Union’s Horizon 2020 Research and Innovation Programme
under Grant 739551 (KIOS CoE) and in part by the Republic of Cyprus
through the Directorate General for European Programmes, Coordination and
Development. (Corresponding author: Sunwoo Kim.)
Jiseon Moon and Sunwoo Kim are with the Department of Electronic
Engineering, Hanyang University, Seoul 04763, South Korea (e-mail:
jiseonmoon@hanyang.ac.kr; remero@hanyang.ac.kr).
Savvas Papaioannou, Christos Laoudias, and Panayiotis Kolios are with
the KIOS Research and Innovation Center of Excellence, University
of Cyprus, Nicosia 1678, Cyprus (e-mail: papaioannou.savvas@ucy.ac.cy;
laoudias@ucy.ac.cy; pkolios@ucy.ac.cy).
Digital Object Identiﬁer 10.1109/JIOT.2021.3073973
and rescue (SAR) [9]–[11]. That said, SAR missions could
be extremely challenging and dangerous. Nowadays, SAR
missions respond to devastations caused by ﬂoods, storms,
maritime accidents, earthquakes, hazardous materials releases,
etc. The ﬁrst responders (FRs) often face various risky and
dangerous situations, and they are required to work in areas,
where public services are unavailable and the infrastructure
is destroyed and disrupted (e.g., during ﬂoods with downed
power lines and gas leaks). Motivated by this, we believe that a
team of autonomous mobile agents (e.g., UAVs) could become
an important aid in many SAR missions by accurately track-
ing the FRs in the aforementioned challenging conditions. A
robust and accurate multi-UAV tracking system for SAR mis-
sions not only can provide the required level of safety to the
FRs but also allows for better organization and coordination of
the rescue team, thus minimizing the need to place the rescuers
in danger situations.
Various sensors, such as lidars and cameras, are nowadays
mounted on UAVs to enable FRs with comprehensive envi-
ronmental perception and help them successfully complete
their missions. Cameras mounted on UAVs are mainly used
to detect and track people, objects, or natural disasters (e.g.,
wildﬁre, ﬂood, and earthquake). Frequently, the target posi-
tion is detected and estimated by image processing and deep
learning [12], [13] techniques. UAVs can also be equipped
with RF sensors to provide, received signal strength (RSS),
round-trip time (RTT), and time of arrival (TOA) type
of measurements, which are combined with ﬁltering tech-
niques to enable advanced navigation and target localization
capabilities [14]–[17].
In this work, we are interested in the control of multiple
UAVs for accurately tracking multiple FRs in the disaster
environment. As illustrated in Fig. 1, we consider a scenario,
where a group of UAVs is used to track multiple FRs in the
ground in order to assist the SAR mission. We assume that
the FRs carry id-linked radio transmitters, such as Bluetooth
or ultrawideband (UWB) tags. The UAVs receive the FRs
radio transmissions and use this information to accurately
localize them. We assume that the environment comprises
of obstacles, occlusions, and large structures; thus, the mea-
surements received by the UAVs at any time can be of two
types, namely, Line-of-Sight (LoS) and non-LoS (NLoS) mea-
surements. The objective of this work is to control the UAV
team operating in the aforementioned challenging conditions
in order to provide optimized tracking of the FRs (i.e., the
targets).
2327-4662 c⃝2021 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 10:14:20 UTC from IEEE Xplore.  Restrictions apply.

## Page 2

15442
IEEE INTERNET OF THINGS JOURNAL, VOL. 8, NO. 20, OCTOBER 15, 2021
Fig. 1.
Illustration of multiple UAVs system for FRs tracking. During the
SAR mission, multiple UAVs track the FRs in a 3-D environment and receive
noisy distance measurements from the FRs. UAVs adjust their position in
order to estimate the state of FRs accurately.
The target tracking performance can be quantiﬁed by the
Cramér–Rao lower bound (CRLB), which is used in the esti-
mation theory to derive a lower bound of the variance of an
unbiased estimator. In the localization system analysis, the
CRLB implies that the localization error at a given position is
greater than or equal to X meters given the conditions in the
region of interest, including the number of the signal sources,
the geometry of the RF receiver and sources, and the statistical
characteristics of the measurements [18]. In other words, the
CRLB becomes larger (i.e., higher localization error should be
expected) when fewer measurements are available to estimate
the FR position or when the geometry of the UAVs is not
suitable. Hereafter, we intend to combine CRLB with deep
reinforcement learning (DRL) to decide the control actions
of multiple UAVs in order to achieve accurate multitarget
tracking.
Reinforcement learning (RL) is a type of machine learn-
ing algorithm that considers how agents take decisions in an
environment. By introducing the neural network as a function
approximator in the training stage, DRL overcomes tradi-
tional RL shortcomings with a ﬁnite number of states and
actions [19]. Interestingly, there have been several efforts
regarding the application of DRL to multiple UAV systems
in recent years, including network security [20], communi-
cation optimization [21]–[23], and target tracking and navi-
gation [24]–[27]. Motivated by the recent advances in DRL
techniques and applications, in this work, we propose a novel
control framework that combines the theory of DRL with the
theory of state estimation through the utilization of CRLB.
Speciﬁcally, we design a novel reward function for our DRL-
based framework, which in each time-step quantiﬁes the
achievable CRLB according to the applied joint UAV control
actions. That said, through the agent–environment interaction,
multiple UAVs learn an optimal policy that enhances the track-
ing performance and maximizes expected cumulative reward.
Consequently, the UAVs adjust their trajectories to optimize
the target state estimation by selecting the joint control actions,
which achieve the lower CRLB.
The main contributions of this article are the following.
1) We propose the ﬁrst DRL-CRLB-based framework to
control multiple UAVs in such a way so that multiple
FRs are being optimally tracked in challenging 3-D
environments in the presence of both LoS and NLoS
conditions.
2) We design a novel reward function using the CRLB of
the target state estimator. The total reward is composed
of subrewards, which account for the CRLB of the entire
system and the individual contribution of each UAV,
thus enabling the proposed DRL framework to learn the
optimal policy.
3) We verify the proposed approach through extensive
simulation experiments and compare it with existing
solutions.
The remainder of this article is organized as follows.
Section II reviews the related work on UAV control and tar-
get tracking. Section III introduces the background of the
Markov decision process (MDP), DRL, and dueling network.
Section IV describes the system model. The CRLB for the
FR state estimator is presented in Section V. Section VI
introduces our DRL-based multiple UAV control system for
target tracking. Section VII presents the simulation results in
the performance evaluation. Finally, Section VIII provides the
concluding remarks.
II. RELATED WORK
In this section, we summarize the most relevant works to
the problem tackled in this article. Speciﬁcally, we discuss
the most recent UAV trajectory optimization and DRL-based
techniques for UAV control and we brieﬂy summarize the main
target tracking techniques, which have been used in related
problems.
In
recent
years,
some
works
on
the
trajectory
optimization for the UAV-aided networks have been studied.
Li et al. [28], [29] proposed a multiple rechargeable UAVs
control technique in order to provide seamless and long-term
services to the ground nodes. In [28], multiple UAVs adjust
their trajectories, transmit power, and the node assignment by
solving the UAV conﬁguration optimization problem, which
is represented by the nonconvex problem. In [29], multiple
UAVs determine their deployment and charging strategy
using the discrete particle swarm optimization (DPSO)
algorithm. Binol et al. [30] proposed the time-efﬁcient UAV
trajectory optimization techniques to collect trafﬁc data from
the roadside units. To solve the problem, they introduce
metaheuristic methods genetic algorithm (GA) and harmonic
search and compare the performance of two methods.
A variety of approaches have been proposed for DRL-based
UAV trajectory control to ﬁt various applications. For instance,
in order to secure the UAV transmitter against being wire-
tapped, UAV jammers send jamming signals to eavesdroppers
by adjusting the ﬂying direction, transmit power level, and
jamming power level [20]. By exploiting the dueling deep
Q-network (DQN), multiple UAVs adjust their movement to
maximize downlink capacity, covering ground terminals [21].
In [22] and [23], an energy-efﬁcient UAV control method is
proposed. Each of the UAVs selects its ﬂying direction and
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 10:14:20 UTC from IEEE Xplore.  Restrictions apply.

## Page 3

MOON et al.: DEEP REINFORCEMENT LEARNING MULTI-UAV TRAJECTORY CONTROL FOR TARGET TRACKING
15443
distance, considering the communications coverage, fairness,
and connectivity. For the problem of UAVs control for tar-
get tracking and navigation, Bhagat and Sujit [24] considered
that persistent target tracking is a challenging task in an urban
environment since a UAV equipped with a camera has a lim-
ited ﬁeld of view (FOV). They constructed a DQN, called
target following DQN, with ﬁnite action space and designed a
reward function that considers whether a target is within the
FOV or not. In [25], a UAV path planning scheme is proposed
for target tracking and obstacle avoidance. Deep determinis-
tic policy gradient (DDPG) allows a UAV to be operated in
continuous action space by combining DQN with an actor-
critic algorithm, which utilizes two networks (actor-network
and critic-network) to determine the best action and evalu-
ate the selected action, respectively. The reward function is
designed considering the angle between the UAV and target
and how smooth the UAV trajectory is. In [26] and [27], DRL
enables a single UAV to navigate from origin to destination by
continuously controlling the UAVs’ ﬂight distance and direc-
tion. They consider the agent’s state as sensory measurements,
including angle and distance between the UAV’s position and
destination. Whenever a UAV executes the selected action,
it receives a nonsparse reward, which considers the distance
between the UAV and destination/obstacle [26]. On the other
hand, a UAV only receives a sparse reward when it reaches
its destination [27].
Regarding
the
single
target
tracking
problem,
Wang et al. [15] proposed a UAV motion planning algo-
rithm for target’s state estimation. The unscented Kalman
ﬁlter (UKF) is used to estimate the target state, while UAV
trajectory, including acceleration and turn rate, is determined
by the motion planner. In [14], an extended Kalman ﬁl-
ter (EKF)-based target tracking technique is proposed. A
single UAV estimates a moving target state and then predicts
the optimal trajectory from the estimated target’s state. In the
presence of multiple targets, the recursive Bayesian ﬁltering
is used to formulate the multiple target searching and tracking
problem [17]. Multiple UAVs manage their trajectories for
searching and tracking, depending on whether the target
is detected. Sung and Tokekar [16] exploited the Gaussian
mixture probability hypothesis density ﬁlter to estimate the
number of targets and track target trajectories. This solution
deals with complex environments, where the number of
targets is unknown and varying.
In this work, we address the multiple UAVs control problem
for tracking multiple targets. The proposed DRL-based con-
troller constructs a deep dueling Q-network with continuous
state space and discrete action space and applies a particle
ﬁlter to estimate the multiple target states.
III. BACKGROUND
Here, we introduce the background of MDP, DRL, and
dueling network.
A. MDP Formulation
We model the proposed UAV control problem as MDP. An
MDP is deﬁned as a tuple {S, A, P, R, γ }, which consists
of ﬁve elements, i.e., states, actions, transition probabilities,
rewards, and discount factor. The state in a state space S
should be observable from the environment. The action in an
action space A is determined by the agent’s movement. The
state and action space of MDP can be either continuous or
discrete. In this article, we consider the state space is contin-
uous, and the action space is discrete. A set of state transition
probability P = {p(sk+1|sk, ak)|sk, sk+1 ∈S, ak ∈A} is
made up of the transition probability p(sk+1|sk, ak), which
is deﬁned by the distribution of the next state sk+1 given
the current state sk and taken action ak. When the agent
takes action ak at the state sk, the agent receives a reward
r(sk, ak) from a set of rewards for all possible state–action
pairs R = {r(sk, ak)|sk ∈S, ak ∈A}. The last element
γ ∈[0, 1] is the discount factor, which indicates the cur-
rent value for the reward obtained in the future. A policy
π = p(ak|sk) is a mapping from the agent’s state to action
and gives the probability of selecting a candidate action at the
current state sk [31].
The agent observes its state sk ∈S from the environ-
ment and takes action ak ∈A according to the policy. The
interaction between agent and environment can be represented
by trajectory (s0, a0, r0, s1, a1, r1, . . . ). The cumulative
discounted reward, called return, is given by
Gk = Rk + γ Rk+1 + γ 2Rk+2 + · · · =
∞

τ=0
γ τRk+τ.
(1)
The value function (state-value function) Vπ(s, a) at state s is
the expected return when the state is s under policy π, and it
is given by
Vπ(s) = Eπ[Gk|sk = s] = Eπ
 ∞

τ=0
γ τRk+τ|sk

.
(2)
The Q-value function (action-value function) under policy π
is deﬁned as the expected return for taking action a in state s,
and it is represented as follows:
Qπ(s, a) = Eπ[Gk|sk = s, ak = a]
(3)
= Eπ
 ∞

τ=0
γ τRk+τ|sk, ak

.
(4)
The value function and Q-value function have a relation-
ship of Vπ(s) = Ea∼π(s)[Qπ(s, a)]. The advantage function
represents the importance of each action, deﬁned by the
value function and Q-value function. The advantage func-
tion subtracts the value function from the Q-value function
Aπ(s, a) = Qπ(s, a) −Vπ(s), and has a relationship of
Ea∼π(s)[Aπ(s, a)] = 0.
B. Deep Reinforcement Learning
The objective of RL is to ﬁnd an optimal policy π∗to
maximize the Q-value function. The optimal Q-value function
Q∗is the maximum expected return achievable from a given
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 10:14:20 UTC from IEEE Xplore.  Restrictions apply.

## Page 4

15444
IEEE INTERNET OF THINGS JOURNAL, VOL. 8, NO. 20, OCTOBER 15, 2021
state–action pair, obtained using Bellman’s optimality [32]
Q∗(sk, ak) = arg max
π
E
⎡
⎣
τ≥0
γ τRk+τ|sk, ak, π
⎤
⎦
= E
	
R + γ max
ak+1 Q∗(sk+1, ak+1)|sk, ak, π

. (5)
For MDP with a ﬁnite number of states and actions, the
optimal Q-value function can be approximated by updating
Q-table iteratively, where rows represent the potential states,
and columns represent actions.
However, the table-based Q learning is difﬁcult to apply to
large-scale problems with continuous state or action because
of the memory capacity caused by a lot of states and actions.
Likewise, our multiple UAVs control problem cannot be rep-
resented as table-based Q learning because the state space of
multiple UAVs is inﬁnite.
To solve this problem, DRL introduces a deep neural
network Q(sk, ak; θ) to approximate the optimal Q-value func-
tion, where parameter θ is the weights of a neural network,
named the Q-network. During the DRL training stage, the
agent’s transition (sk, ak, rk, sk+1) is stored into a replay
memory D. To achieve sufﬁcient learning, minibatches are
randomly drawn from the replay memory to adjust Q-network
weight rather than using the batches of consecutive samples.
The Q-network is updated by minimizing the loss function,
which is given by
Loss(θ) = Esk,ak,rk,sk+1

(yk −Q(sk, ak; θ))2
(6)
with
yk = r(sk, ak) + γ max Q−
sk+1, ak+1; θ−
(7)
where the target value yk is a summation of reward of state–
action pair r(sk, ak) and the maximum discounted Q-value of
the target network Q−, which is parameterized by the weights
of the target network θ−. The weight of the target network θ−
is updated by Q-network θ every N timesteps.
C. Dueling Deep Q-Network
In this article, we utilize a dueling architecture to achieve
robust estimates of Q-value function. The dueling architec-
ture decouples fully connected (FC) layers into two streams
rather than using a single stream of FC layers, i.e., the original
deep Q network. In the dueling architecture, one stream of FC
layers is a value function estimator V(sk; θ, θβ) that outputs a
scalar, and the other stream is an advantage function estimator
A(sk, ak; θ, θα) that outputs a |A|-dimensional vector. Here, θα
and θβ denote the weights of the advantage function estima-
tor and value function estimator, respectively. According to the
advantage function deﬁnition, these two streams are combined
to calculate the Q-value function, as follows:
Qπ(s, a) = Vπ(s) + Aπ(s, a).
(8)
However, Q(sk, ak; θ, θα, θβ) is the only parameterized esti-
mate of the Q-value function. Moreover, it is impossible to
obtain Vπ(s) and Aπ(s, a) uniquely for a given Qπ(s, a). To
solve this issue, we modify the combination of the two streams
to obtain the Q function as follows:
Q

sk, ak; θ, θα, θβ

= V

sk; θ, θβ

+

A(sk, ak; θ, θα) −max
a′
k∈A A

sk, a′
k; θ, θα


.
(9)
Due to the above modiﬁcation, the advantage function esti-
mator A(sk, ak; θ, θα) has zero advantage for the selected
action. Besides, for a∗= arg maxa′∈A Q(sk, ak; θ, θα, θβ) =
arg maxa′∈A A(sk, ak; θ, θα), we get Q(sk, a∗
k; θ, θα, θβ)
=
V(sk; θ, θβ).
Alternatively, the Q-value function is obtained by replacing
the max operator with an average as follows [33]:
Q

sk, ak; θ, θα, θβ

= V

sk; θ, θβ

+
⎛
⎝A(sk, ak; θ, θα) −1
|A|

a′
k∈A
A

sk, a′
k; θ, θα

⎞
⎠.
(10)
Hence, the stream V(sk; θ, θβ) of FC layers estimates the value
function, and the other stream A(sk, ak; θ, θα) provides the
estimate of the advantage function.
IV. SYSTEM MODEL
In this section, we outline the modeling assumptions used
in the proposed framework. In particular, we describe the FR
dynamic model, UAV dynamic model, and the UAV sensing
model.
A. First Responder Dynamics
We assume that during a SAR mission, there are N (where
N is known and ﬁxed) FRs (i.e., targets) on the ground that
need to be tracked. At timestep k, the state vector of the jth
target is represented by
xj
k =

xj, ˙xj, ¨xj, yj, ˙yj, ¨yj, zj, ˙zj, ¨zj⊺
k
(11)
where xj, yj, and zj are the Cartesian coordinates of the jth
target position, ˙xj, ˙yj, and ˙zj denotes the speed of the jth target
along the x, y, and z directions and, ﬁnally, ¨xj, ¨yj, ¨zj is the
acceleration of the jth target along the x, y, and z directions in
3-D space.
During their operations, the FRs encounter sudden and
unexpected changes in their motion patterns. In order to
account for this uncertainty, the dynamic model of the FRs
is composed of a command process vector νk = [νx, νy, νz]⊺
k
and a random acceleration vector bk = [¨x, ¨y, ¨z]⊺
k , where the
total acceleration is ak = νk + bk. The command processes
νx,k, νy,k, and νz,k take values from each set of the discrete
acceleration level Lx, Ly, and Lz. The command process vec-
tor νk is formulated as a Markov chain with a set of ﬁnite
states L = Lx × Ly × Lz = {v1, . . . , vL} and transition prob-
ability Ll¯l = p(νk = v¯l|νk−1 = vl), l,¯l = {1, . . . , L}. The
transition probability is given by
Ll¯l =
 pl,
if l = ¯l
(1 −pl)/(L −1),
if l ̸= ¯l.
(12)
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 10:14:20 UTC from IEEE Xplore.  Restrictions apply.

## Page 5

MOON et al.: DEEP REINFORCEMENT LEARNING MULTI-UAV TRAJECTORY CONTROL FOR TARGET TRACKING
15445
Fig. 2.
Admissible control actions, where UAV is at the origin and Nθ = 6.
The ﬁrst autoregressive (AR) model is adopted to represent
the correlation feature of random acceleration, which is given
by [34]
bk+1 = α	bk + ωk
(13)
where α	 ∈(0, 1) is the reciprocal of the acceleration time
constant. The random acceleration vector ωk = [ωx, ωy, ωz]⊺
k
is a multivariate normal distribution with ω ∼N(03×1, σ 2
ωI3),
where I3 is an identity matrix of dimension 3 × 3. Hence, the
dynamics of the jth FR at timestep k can be expressed by the
following discrete-time system [35]:
xj
k = xj
k−1 + ννk + ωωk
(14)
where the matrices , ν, and ω are represented as follows:
 =
⎡
⎣
˜
03×3
03×3
03×3
˜
03×3
03×3
03×3
˜
⎤
⎦, i =
⎡
⎣
˜i
03×1
03×1
03×1
˜i
03×1
03×1
03×1
˜i
⎤
⎦
(15)
˜ =
⎡
⎣
1
k
k2/2
0
1
k
0
0
α	
⎤
⎦, ˜ν =
⎡
⎣
k2/2
k
0
⎤
⎦, ˜ω =
⎡
⎣
k2/2
k
1
⎤
⎦
(16)
where the subscript i of the matrix ˜i represents ν or ω, 03×1
is a zero matrix of dimension 3×1, and 03×3 is a zero matrix
of dimension 3 × 3.
B. UAV Dynamics
We assume that a team of M UAVs operate in the environ-
ment and monitor the FRs. At timestep k, the state vector of
the ith UAV is represented by ui = [ui
x, ui
y, ui
z]⊺
k . The UAV
dynamics are formulated as
ui
k = ui
k−1 + an = ui
k−1 +
⎡
⎣
d cos (nθ)
d sin (nθ)
0
⎤
⎦
(17)
where d is a constant distance that the UAVs can move at
each timestep k and θ = 2π/Nθ is the unit steering angle.
The admissible control actions which can be taken by UAV
are shown in Fig. 2. The action control an, n = {1, . . . , Nθ}
denotes the ﬂight direction along x, y, and z axis. UAVs deter-
mine the ﬂight direction by choosing one action from discrete
action space {a1, a2, . . . , aNθ } ∈A.
C. UAV Sensing Model
We consider that each UAV is equipped with a range sen-
sor that measures the distance between the ith UAV and the
jth target. UAVs receive distance measurements from ground
targets every timestep. The measurement model is represented
as follows:
yij
k = h

cj
k, ui
k

+ wij
k =
cj
k −ui
k

2 + wij
k
(18)
where cj = [xj, yj, zj]⊺is the jth target position, the function
h(cj, ui) is the Euclidean distance of the ith UAV, and the jth
target, and wij
k is measurement noise between the ith UAV and
the jth target. Due to various obstacles in the environment, the
UAVs receive LoS and NLoS measurements from targets as
shown in Fig. 1. For this reason, we model the measurement
noise wij
k as [18], [36]
wij
k ∼

λij N

0, σ 2
LoS

+

1 −λij
N

μNLoS, σ 2
NLoS

(19)
where N(0, σ 2
LoS) denotes LoS measurement characteristics,
i.e., as a Gaussian distribution with zero mean and variance
σ 2
LoS and N(μNLoS, σ 2
NLoS) denotes the NLoS measurements
statistical proﬁle, i.e., as a Gaussian distribution with mean
μNLoS and variance σ 2
NLoS. The measurement noise model is
thus a mixture model of LoS and NLoS components, and the
ith UAV receives LoS component from the jth target with
probability λij, which is formulated as follows:
λij = p

ij
=
1
1 + α exp

−β

ij −α

(20)
where ij = arcsin ((ui
z −zj) / ∥cj −ui∥2) is the elevation
angle between the ith UAV and the jth target. The two parame-
ters α and β relate to the ratio of the structured area to the total
land area and the number of buildings per unit land area [37].
V. CRAMÉR–RAO LOWER BOUND OF FIRST RESPONDERS
STATE ESTIMATOR
This section describes the CRLB of the FRs position, which
is the main criterion to quantify the system performance. Also,
we brieﬂy introduce the optimal UAV joint control actions
according to the CRLB as discussed in [36].
A. CRLB of FRs Position
CRLB is a lower bound of variance on the unbiased estima-
tor, which represents achievable estimator performance. The
CRLB of all target positions is formulated by
var

ˆFk

≥tr

J−1(Fk)

(21)
where tr(·) means the trace of a square matrix, which is
the sum of the diagonal elements of the matrix, and Fk =
[c1
k, . . . , cN
k ] is a vector that contains the all-target position.
The Fisher information matrix (FIM) J(Fk) is given by [38]
J(Fk) = −E

∂2 ln (Yk|Xk)
∂F2
k

.
(22)
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 10:14:20 UTC from IEEE Xplore.  Restrictions apply.

## Page 6

15446
IEEE INTERNET OF THINGS JOURNAL, VOL. 8, NO. 20, OCTOBER 15, 2021
Fig. 3.
Overview of the DRL-based FR tracking system. The green part depicts that the FR’s state is updated by prediction density in the time prediction stage,
and the posterior distribution in the measurement update stage. The blue part represents DRL-based control. Agents observe their state from the environment
and select actions according to the dueling network, where the yellow part is the value function estimator and the blue part is the advantage estimator. For
agent–environment interaction, each agent learns a policy to maximize the Q-value and share a global Q-value estimator.
The joint measurement likelihood function, considering the
UAV sensing model presented in Section IV-C, is approxi-
mated by a single Gaussian distribution as follows:
(Yk|Xk) =
M

i=1
N

j=1
N

yij
k|h

cj
k, ui
k

+ μi,j
k ,

σ ij
k
2
(23)
where Yk = yij
k(i, j), i ∈{1, . . . , M}, j ∈{1, . . . , N} is distance
measurement from the jth target received by the ith UAV at
timestep k, and Xk(j) = xj
k, j ∈{1, . . . , N} is the jth target
state at timestep k. According to the UAV sensing model, the
mean and variance of the joint measurement are given by
μij
k =

1 −λij
k

μNLoS
(24)

σ ij
k
2
= λij
k

σ 2
LoS −

μij
k
2
+

1 −λij
k

σ 2
NLoS + μ2
NLOS −

μij
k
2
. (25)
The joint measurement likelihood function can be repre-
sented by the log-likelihood function ln (Yk|Xk)
M

i=1
N

j=1
⎧
⎪⎨
⎪⎩
ln
1
√
2πσ ij
k
−

yij
k −h

cj
k, ui
k

−μij
k
2
2

σ ij
k
2
⎫
⎪⎬
⎪⎭
.
(26)
According to derivation in [36], the FIM J(Fk) is represented
in the form of a block-diagonal matrix
J(Fk) = diag([J1, J2, . . . , JN]).
(27)
The CRLB of all target state is expressed as the sum of each
target’s CRLB
var

ˆFk

≥
N

j=1
tr

J−1
j

.
(28)
B. UAVs Optimal Control Actions
CRLB-based control is described as an extension to a greedy
algorithm. At each timestep, candidate positions are deter-
mined by the UAV’s current position and action space A,
deﬁned in Section IV-B. The CRLB for all candidate positions
is calculated using the predicted target position ˜xk since the
actual target position is unknown. UAVs select optimal action
combination U∗
k corresponding to minimum CRLB among
candidate positions, which is given by
U∗
k = arg min
Uk
N

j=1
tr

J−1
j,Uk

(29)
where Uk = {a1
k, . . . , aM
k } is a combination of UAV control
action, and Jj,Uk represents FIM calculated by the jth pre-
dicted target position and UAVs position changed by control
action Uk.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 10:14:20 UTC from IEEE Xplore.  Restrictions apply.

## Page 7

MOON et al.: DEEP REINFORCEMENT LEARNING MULTI-UAV TRAJECTORY CONTROL FOR TARGET TRACKING
15447
VI. PROPOSED DEEP REINFORCEMENT LEARNING-BASED
UAV TRAJECTORY CONTROL
We introduce a DRL-based multiple UAV control algorithm
for accurate target state estimation. First, we present details
of the DRL algorithm, including state, action, and reward
design. Then, we describe the target state estimation using
the Bayesian ﬁltering.
Fig. 3 illustrates an overview of the DRL-based FR track-
ing system. The system consists of two parts: 1) FR estimation
and 2) DRL-based controller parts. The FR estimation part is
composed of time prediction stage and measurement update
stage, where the states of FRs predicted and corrected accord-
ing to the prediction density p(xk|Y1:k−1) and the posterior
distribution p(xk|Y1:k), respectively. In the time prediction, the
state of FRs ˜xk is predicted using a probabilistic model based
on the target dynamics. After the time prediction stage, the
DRL-based controller operates in order to adjust UAV’s posi-
tion. In the DRL-based UAV controller, the ith UAV observes
state si
k, moves its position ui
k by taking action ai
k, and gets a
reward ri
k through the UAV-environment interaction. The input
of the DRL-based controller (i.e., state of the UAV) is deter-
mined by the position of UAV and the predicted target position
obtained in the time prediction of the FR estimation part. Then,
in the measurement update stage, the states of FRs ˆxk are cor-
rected through the measurement likelihood function obtained
from distance measurements, which are received by UAVs.
The details are described in the next sections.
A. DRL-Based Controller Design
The components of the DRL-based UAV controller form
a Markov Decision Process or MDP (i.e., Section III-A)
and include the elements: state, action, reward function, and
training process.
1) State: The state vector of the ith agent at timestep k con-
siders UAV position and target position, which is represented
by si
k = [ui
k, pi1
k , . . . , piM
k , qi1
k , . . . , qiN
k ] ∈R3(M+N). The state
vector of the ith agent consists of three parts as follows.
1) ui: Absolute coordinates of the ith agent.
2) pi¯i: Relative coordinates between the ith agent and the
¯ith agent.
3) qij: Relative coordinates between the ith agent and the
jth target.
The relative coordinates between the ith agent and the ¯ith
agent is given by pi¯i = (u¯i −ui)⊺, where i,¯i ∈{1, . . . , M},
and i ̸= ¯i. Each relative coordinates pi¯i is concatenated into
one vector [pi1, . . . , piM] ∈R1×3(M−1). The relative coordi-
nates between the ith agent and the jth target is given by
qij = (˜cj −ui)⊺, where j ∈{1, . . . , N} and ˜cj
k is the pre-
dicted target position extracted from the predicted target state
˜xj
k. Each relative coordinates qij is concatenated into one vec-
tor in order [qi1, . . . , qiN] ∈R1×3N. The input size of DRL
varies with the number of agents and targets.
2) Action: In each timestep, the ith agent selects action ai
k
from discrete action space A deﬁned in Section IV-B. The
selected action determines the next position of the UAV. If the
action combination selected by the DRL-based controller is
likely to cause collisions between UAVs, the selected action
is replaced by another action among the action space.
3) Reward: The agent observes its state from the environ-
ment and takes action. Through this interaction, each agent
receives a scalar reward from the environment. UAVs make
a decision to maximize cumulative reward, and they aim to
improve target tracking performance by minimizing CRLB .
The reward of the ith agent at timestep k comprises of three
subrewards, and it is formulated as follows:
ri
k = R1,k + R2,k −Ri
3,k.
(30)
The reward ri
k aggregates subrewards into a single scalar,
whose form is most widely used in multiobjective prob-
lems [39]. The selected action combination from the DRL-
based control should be a solution, called Pareto-optimal,
which maximizes the reward in a multiobjective problem [40].
In above equation, R1 and R2 correspond to global reward,
and R3 to difference reward [41], [42]. The global reward,
denoted as G(sk, ak), is given to the agents based on the util-
ity of the entire system. All agents receive the same global
reward, regardless of the effect of each agent’s action on the
entire system. On the other hand, difference reward Di quan-
tiﬁes each agent’s individual contribution to the entire system.
The difference reward is given by
Di

si
k, ai
k

= G(sk, ak) −G

s−i
k , a−i
k

(31)
where the counterfactual G(s−i
k , a−i
k ) is the global reward with-
out the ith agent’s contribution to the system, calculated by
assuming the ith agent is not present. As mentioned before,
global reward functions R1,k and R2,k are given by G1(sk, ak)
and Gs(sk, ak), respectively. For Ri
3,k, the utility of the entire
system is represented by G3(sk, ak), and the difference reward
of the ith agent Di
3,k is expressed by the difference between
G3(sk, ak) and G3(s−i
k , a−i
k ).
The CRLB variation reward R1,k is a global reward related
to how much CRLB is decreased
R1,k = η1 × G1(sk, ak) = η1 ×
 −m
M −m
+ κ1

. (32)
The utility of the entire system is the CRLB difference
 = k−1 −k between at timestep k −1 and timestep
k. All agent get positive R1 when they move to a position
with lower CRLB. The absolute value of the CRLB differ-
ence is substantial when the tracking performance signiﬁcantly
improves or worsens, comparing timestep k and timestep k−1.
The tuning parameters m and M determined via experi-
ments are the minimum bound and the maximum bound of
CRLB difference, respectively, where 95% of CRLB differ-
ence is in the range of [m, M]. Two parameters are used
to scale the CRLB difference and make the 95% of the ﬁrst
term in parentheses in the range of [0,1]. The parameter κ1
adjusts the range of G1(sk, ak) to [−0.5, 0.5]. The parameter
η1 denotes the magnitude of reward functions R1.
The CRLB magnitude reward R2,k is a global reward
representing how small the CRLB k is at time k
R2,k = η2 × G2(sk, ak) = η2 ×

e−δ·k + κ2

.
(33)
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 10:14:20 UTC from IEEE Xplore.  Restrictions apply.

## Page 8

15448
IEEE INTERNET OF THINGS JOURNAL, VOL. 8, NO. 20, OCTOBER 15, 2021
For reward function R2, the utility is CRLB of the target state
estimator. As CRLB increases, the rewards awarded to all
agents decrease exponentially. The tuning parameter δ deter-
mined by experiments is the degree to which the reward is
reduced. The parameter κ2 adjusts the range of G2(sk, ak) to
[−0.5, 0.5] and the value in parentheses is positive if CRLB
k is smaller than 0.7 ∗(1/δ). The parameter η2 changes the
magnitude of reward functions R2.
The difference reward Ri
3,k quantiﬁes the ith agent’s contri-
bution to tracking performance
Ri
3,k = η3 × Di
3,k
(34)
where the tuning parameter η3 changes the range of the reward.
We deﬁne reward Di
3,k as follows:
Di
3,k =
G3(sk, ak) −G3

s−i
k , a−i
k


J−1
j⋆

−i
=
J−1
j⋆

J−1
j⋆

−i
−1
(35)
with
j⋆= argmax
j∈{1,2,...,N}
'''' J−1
j
−

J−1
j

−i
''''
(36)
where J−1
j
is inverse FIM of the jth target for all agents in
the system, and (J−1
j
)−i is inverse FIM of the jth target when
the ith agent is excluded from the entire system. The notation
j⋆means a target with the largest difference between J−1
j
and
(J−1
j
)−i. The utility of Ri
3,k considers CRLB of the j⋆th target;
in other words, the effect of the presence of the ith agent
on the j⋆th target tracking performance. The utility of UAV
system G3(sk, ak) = J−1
j⋆
is the CRLB of the j⋆th target state
estimator, and G3(s−i
k , a−i
k ) = (J−1
j⋆)−i is the CRLB of the
j⋆th target state estimator when the ith agent is absent. The
difference between G3(sk, ak) and G3(s−i
k , a−i
k ) is normalized
to (J−1
j
)−i to adjust the range of Di
3,k to [−1, 0]. The difference
reward of the ith agent approaches −1 when the ith agent has a
signiﬁcant impact on the CRLB of the j⋆th target. Therefore,
the total reward ri
k is obtained by subtracting the difference
reward Ri
3,k.
4) Reinforcement Learning Training: A conventional DRL
process is introduced in Section III-B. The blue part in Fig. 3
illustrates the overall structure of the DRL-based multiple UAV
controller. Each agent observes its state and selects an action
from the global dueling network described in Section III-C.
The global network is updated by the interaction of distributed
agents. The details of the multiple UAVs control algorithm are
provided in Algorithm 1. In the beginning, the Q network is
initialized with random weights of θ. The weights of the target
Q network are replicated as the weights of Q network θ−= θ.
Also, a replay memory, which stores the recent ND transition
tuples, is initialized (lines 1–3). With every new episode, the
DRL-environment is initialized and, thus, the agents learn var-
ious tracking strategies by trial and error during each episode
composed of consecutive K timesteps without any stopping
criterion (line 4–6). Each agent selects an action corresponding
to maximum Q value with probability 1 −ϵ or randomly with
probability ϵ. The probability ϵ decreases as the training is
repeated (lines 7 and 8). The transition sample (si
k, ai
k, ri
k, si
k+1)
Algorithm 1: Multi-UAV Control for Target Tracking
Based on DRL
Input : State vector of i-th agent
Output: Action of agent i-th agent
1 Initialize Q network Q with random weights of θ;
2 Initialize target Q network Q−with weights θ−= θ;
3 Initialize replay memory D to capacity ND;
4 for Episode : = 1, . . . , Nt do
5
Initialize environment;
6
for Timestep k: = 1, . . . , K do
7
for Agent i: = 1, . . . , M do
8
Select a greedy action
ai
k = arg max
ak
Qi(si
k, ak) with probability 1 −ϵ
or a random action with probability ϵ;
9
Execute action ai
k;
10
Store the transition sample

si
k, ai
k, ri
k, si
k+1

in
replay memory;
11
end
12
Sample minibatch from replay memory D;
13
Calculate target value using (7);
14
Calculate loss value using (6);
15
Update Q network;
16
Update target Q network every N time steps;
17
end
18 end
is stored in the replay memory D (lines 9 and 10). A mini-
batch consisting of NB transition tuples is sampled uniformly
from all transitions in replay memory D to calculate the target
values and loss function. The weights of the Q network are
updated, while reducing the loss function with the optimizer.
Then, target Q network is updated, duplicating the weights of
Q network every N timesteps (lines 12–16).
B. FRs State Estimation
We use particle ﬁltering [43] to estimate the posterior dis-
tribution of the target states given the noisy measurements. As
shown in Fig. 3, the target position is ﬁrst predicted, and then
used as the input to the DRL-based controller. After the loca-
tions of UAVs are determined by the DRL-based controller,
the target position is corrected in the measurement update
step. The main concept of the particle ﬁlter is to construct a
posterior distribution p(xk|Y1:k) of target state xk, given mea-
surements Y1:k = {y1, y2, . . . , yk} up to timestep k. The time
prediction and measurement update is computed as follows:
p(xk|Y1:k−1) =
(
p(xk|xk−1)p(xk−1|Y1:k−1)dxk−1 (37)
p(xk|Y1:k) =
p(yk|xk)p(xk|Y1:k−1)
)
p(yk|xk), p(xk|Y1:k−1)dxk
(38)
where p(xk|xk−1) ∼N(	xk−1 + ννk, ω⊺
ωσω) is a prob-
abilistic model of the state evolution (transitional density)
deﬁned by (14), and p(yk|xk) is a measurement likelihood
function deﬁned by (18).
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 10:14:20 UTC from IEEE Xplore.  Restrictions apply.

## Page 9

MOON et al.: DEEP REINFORCEMENT LEARNING MULTI-UAV TRAJECTORY CONTROL FOR TARGET TRACKING
15449
TABLE I
SIMULATION PARAMETERS
The green part in Fig. 3 shows the target state estimation
process in the proposed system. In the time prediction stage,
the jth predicted target state ˜xj
k is determined by prediction
density p(xj
k|Yj
1:t−1) and is calculated as follows:
˜xj
k =
(
xj
k p

xj
k|Yj
1:k−1

dxj
k.
(39)
The predicted target state ˜xj
k is used as input of the DRL-
based controller to select the UAVs’ actions. Then, each UAV
moves to their new position according to actions selected by
the DRL-based controller and receives distance measurements
from the ground targets.
The posterior distribution p(xk|Y1:k) depends on measure-
ment likelihood p(yk|xk) calculated by distance measurements.
The measurement likelihood function of the jth target is
given by
p

y1j
k , . . . , yMj
k |xj
k, u1
k, . . . , uM
k

=
M

i=1
p

yij
k|xj
k, ui
k

(40)
where p(yij
k|xj
k, ui
k) = N(yij
k|h(˜cj
k, ui
k)+μij
k, (σ ij
k )2) is measure-
ment likelihood function of the jth target and the ith UAV. The
posterior distribution is obtained by Bayes’ theorem (38) and
the estimated target position ˆxj
k is obtained as follows:
ˆxj
k =
(
xj
k p

xj
k|Yj
1:k

dxj
k.
(41)
VII. SIMULATION RESULTS AND ANALYSIS
To evaluate the performance of the proposed approach, we
have divided our evaluation into ﬁve main parts. The ﬁrst
section introduces settings for target tracking simulation. In
the following two sections, the results of single-target track-
ing and multitarget tracking are presented. We present the
CRLB of the target state estimator and localization error to
verify the tracking performance of DRL-based control, com-
pared to CRLB-based control [36] (mentioned in Section V-B),
GA-based control [44] and DPSO-based control [45]. The
DRL-based control should maintain the CRLB of the target
estimator during the entire timesteps at the same level as the
CRLB-based control, where it always selects an optimal action
combination. The localization error is deﬁned as mean squared
error (MSE) between the estimated target position and real
target position, which is formulated as
MSE = E
⎡
⎣
N

j=1

xj −ˆxj2
⎤
⎦.
(42)
In the fourth section, we present two metrics, reward and run-
time, to prove that the proposed approach is effective for
real-time tracking. Finally, the last section shows that the
CRLB-based control needs to be replaced with alternative
control methods in larger-scale problems.
A. Simulation Setup
Our experiments are conducted on the Ubuntu 16.04 server
with Intel i7-4790K. We use three fully connected layers with
50 neurons and ReLU activation, Relu(x) = max(0, x). The
third layer is connected to two streams, estimators of the value
function, and advantage function. The size of replay memory is
ND = 5000, and minibatch is randomly sampled consisting of
NB = 128 transition tuples selected from replay memory D.
After the training stage, each agent selects its action corre-
sponding to the maximum Q-value from the trained network
to verify the performance of the trained network. Detailed
simulation parameters are presented in Table I.
B. Experiment 1: Single Target Tracking
In this experiment, there is one ground target, whose
initial
state
vector
is
set
to
[x, ˙x, ¨x, y, ˙y, ¨y, z, ˙z, ¨z]⊺
=
[40, 0.4, 0, 40, 0.4, 0, 0, 0, 0]⊺
with
units
m,
m/s,
m/s2,
m,
m/s,
m/s2,
m,
m/s
and
m/s2.
The
initial
posi-
tions of three UAVs are [x, y, z]
=
[20, 25, 25]⊺
m,
[60, 25, 25]⊺m, and [40, 65, 25]⊺m. The discrete accel-
eration
level
is
set
to
L
=
Lx × Ly × Lz
=
{(0, 0, 0), (1, 0, 0), (−1, 0, 0), (0, 1, 0), (0, −1, 0)} in units
of m/s2.
Fig. 4 shows 3-D trajectories of three UAVs, and Fig. 5
presents the elevation angle between UAVs and the target.
Fig. 6 is the probability of LoS, where the environment is
urban. At the initial state, three UAVs are the same dis-
tance away from the target. They maintain elevation angles
about 45◦with the target, and the probability that three UAVs
receive LoS is 0.75. When UAVs start monitoring missions, all
UAVs the track ground target for entire timestep. At timestep
1 ≤k ≤10, Three UAVs move closer to the target position
around [40, 40, 0] m. The elevation angle increases from 45◦to
over 65◦, and UAVs receive get LoS measurement from target
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 10:14:20 UTC from IEEE Xplore.  Restrictions apply.

## Page 10

15450
IEEE INTERNET OF THINGS JOURNAL, VOL. 8, NO. 20, OCTOBER 15, 2021
Fig. 4.
Trajectories of three UAVs and one target.
Fig. 5.
Elevation angle between UAVs and target.
Fig. 6.
Probability of LoS (α = 0.7, β = 10) in the urban environment.
with over probability of 0.99. Between timestep 10 ≤k ≤50,
the target begins to move long distances, as its speed increases.
UAVs adjust their ﬂight direction to catch up with the target.
When timestep is between 50 and 80, the target hovers around
[50 m, 70 m, 0 m], and UAVs also ﬂy close to the target.
Elevation angles of three UAVs are around 75◦during this
time, and they receive LoS measurement with probability of
0.998. After timestep k ≥80, UAVs select their action that
move to trajectory of the target while keeping a certain dis-
tance from the target. Through these results, we conﬁrmed that
each UAVs select their own actions according to the trained
network, and UAVs adjust their trajectories, where they receive
LoS measurement from target with a high probability.
Fig. 7.
CRLB of four UAV control methods.
Fig. 8.
MSE of four UAV control methods over 100 Monte Carlo
experiments.
Figs. 7 and 8 present CRLB and localization error when
UAVs track the target moving in the trajectory shown in Fig. 4
by four UAV controls: 1) DRL-based control; 2) CRLB-based
control; 3) DPSO-based control; and 4) GA-based control. The
CRLB and localization error of each control are averaged over
100 Monte Carlo experiments. The initial CRLB is around
178.78 for four control schemes. During the entire timestep,
CRLB and MSE of the CRLB-based control decrease more
than the other controls because UAVs adjust their position
corresponding to minimum CRLB among candidate positions.
After timestep k ≥10, CRLB and MSE of all control schemes
decrease to about 2.2, although there are ﬂuctuations in CRLB
and MSE of four control schemes. The CRLB and track-
ing error depict that the three control methods excluding
the CRLB-based control have a level of CRLB that is not
signiﬁcantly different from the CRLB of the CRLB-based
control. Through these simulation results, we observe that
DRL-based control achieves comparable tracking performance
to the CRLB-based control, which is the optimal control
scheme.
C. Experiment 2: Multiple Target Tracking
In this experiment, there are two targets, whose initial vec-
tor are [x, ˙x, ¨x, y, ˙y, ¨y, z, ˙z, ¨z]⊺= [250, 0, 0, 200, 0, 0, 0, 0, 0]
and [250, 0, 0, 300, 0, 0, 0, 0, 0] with units m, m/s, m/s2, m,
m/s, m/s2, m, m/s, and m/s2. Four UAVs are placed in
a square shape in the middle of two targets. The initial
state vectors of four UAVs are [x, y, z] = [240, 240, 25]⊺m,
[240, 260, 25]⊺m, [260, 240, 25]⊺m, and [260, 260, 25]⊺m.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 10:14:20 UTC from IEEE Xplore.  Restrictions apply.

## Page 11

MOON et al.: DEEP REINFORCEMENT LEARNING MULTI-UAV TRAJECTORY CONTROL FOR TARGET TRACKING
15451
Fig. 9.
Trajectories of four UAVs and two targets.
Fig. 10.
Elevation angle between four agents and target 1.
Fig. 11.
Elevation angle between four agents and target 2.
The discrete acceleration level is L = Lx × Ly × Lz =
{(0, 0, 0), (1, 0, 0), (−1, 0, 0), (0, 1, 0), (0, −1, 0)} in units
of m/s2.
Fig. 9 is the 3-D trajectories of four UAVs and two tar-
gets for entire timesteps. Figs. 10 and 11 are elevation angles
between four UAVs and each target. Fig. 12 shows the prob-
ability that UAVs receive LoS measurement in the rural
environment. In this environment, it is possible to ensure suf-
ﬁcient LoS at a lower elevation angle than the environment
in Experiment 1. When all UAVs and targets are in the initial
state k = 1, agent 1 and agent 3 are close to target 1 with the
same distance. The other two agents are far from target 1, but
closer to target 2. Four agents maintain elevation angles of 30◦
with the target, which is closer to themselves. It means that
they receive LoS component with a probability of 0.7 from the
Fig. 12.
Probability of LoS (α = 0.5, β = 10) in the rural environment.
Fig. 13.
CRLB of four UAV control methods.
closer target. For target that is far from all UAVs, the initial
elevation angle is about 20◦and UAVs obtain LoS component
with a probability of 0.3. For timesteps 1 ≤k ≤10, agent 1
and agent 3 move in −y direction to get closer to target 1.
They achieve an elevation angle at least 50◦with target 1 and
ensure LoS measurement with a probability of 0.98. Likewise,
agent 2 and agent 4 start to move toward the target 2 in the +y
direction. Two agents maintain elevation angle over 40◦, col-
lecting LoS measurement with a probability of 0.93. During
timestep 10 ≤k ≤30, agent 1 and agent 3 move toward the
target 1, and agent 2 and agent 4 track target 2. Two agents are
assigned to one target and ensure sufﬁcient LoS measurement
from the assigned target at least a probability of 0.93. The
two targets have different trajectories between the timestep
30 ≤k ≤55, which means the target 1 moves long distance
about from [250 m, 215 m, 0 m] to [280 m, 245 m, 0 m] and
the target 1 goes around [265 m, 315 m, 0 m]. To obtain LoS
measurement from each assigned target, agent 1 and agent 3
move similar to the trajectories of target 1; in the same man-
ner, agent 2 and agent 4 ﬂy in the vicinity of target 2. For
that period, each agent achieves the elevation angle over 50◦
with the assigned target and receives LoS measurement with
a probability of more than 0.98. After timestep k ≥55, all
UAVs steer their ﬂight direction properly, maintaining the ele-
vation angle with two targets over 50◦to guarantee sufﬁcient
LoS measurements. It is conﬁrmed that the action combina-
tion selected from the DRL-based controller enables the group
of UAVs to maintain a high elevation angle and collect LoS
measurement from the multiple targets.
Figs. 13 and 14 illustrate CRLB and localization error,
where
the
results
are
average
over
100
Monte
Carlo
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 10:14:20 UTC from IEEE Xplore.  Restrictions apply.

## Page 12

15452
IEEE INTERNET OF THINGS JOURNAL, VOL. 8, NO. 20, OCTOBER 15, 2021
TABLE II
REWARD OF DRL-BASED CONTROL AND CRLB-BASED
CONTROL IN EVALUATION STAGE
Fig. 14.
MSE of four UAV control methods over 100 Monte Carlo
experiments.
experiments. For four control schemes, it is shown that CRLB
is greatly reduced from 1123 to 10 between timestep 1 ≤
k ≤10. During that time, CRLB-based control has the best
performance among the other controls because CRLB-based
control enables UAVs to select action combinations corre-
sponding to minimum CRLB. For timestep 10 ≤k ≤80, the
three control methods except for the GA-based control main-
tain CRLB values between timestep 3 and 8; however, the
GA-based control has a noticeably large CRLB among the all
UAV control schemes. After k ≥80, the tracking performance
of GA-based control improved, and its CRLB value is reduced
to 8; hence, all UAV controls maintain similar performance.
For the DRL-based control, it maintains the low CRLB value
of about 5 and attains similar tracking performance as the
CRLB-based control for the entire timestep. Besides, as shown
in Fig. 14, localization error follows the same tendency as
CRLB. We observe that DRL-based control achieves the com-
parable tracking performance to the CRLB-based control and
performs well in the multiple target tracking scenarios.
D. Reinforcement Learning Performance
We investigate the performance of DRL-based control con-
cerning the reward function that all agents receive during
the training stage and evaluation stage ﬁrst. The cumulative
difference reward Rdiff, cumulative global reward Rglob, and
cumulative total reward Rtot in one iteration are calculated as
follows:
Rdiff = 1
K
K

k=1
N

i=1
Ri
3,k
(43)
Rglob = 1
K
K

k=1

R1,k + R2,k

(44)
Fig. 15.
Total reward curve versus the training iteration of Experiment 1.
Fig. 16.
Total reward curve versus the training iteration of Experiment 2.
Rtot = 1
K
K

k=1
N

i=1
ri
k
(45)
where K is the total timestep, presented in Table I. Figs. 15
and 16 illustrate the cumulative total reward Rtot received by all
agents for training iteration in Experiment 1 and Experiment 2,
respectively. In Figs. 15 and 16, total rewards increase and con-
verge over the whole training stage, and it means that agents
learn policy to maximize the reward by repeating the training
iteration. Table II represents Rdiff, Rglob, and Rtot of two control
methods in the evaluation stage. In CRLB-based control, UAVs
receive greater Rdiff, Rglob, and Rtot than DRL-based con-
trol because UAVs always take optimal action with minimum
CRLB at their current positions. There is noticeable difference
in Rdiff between two controls, but DRL-based control achieves
comparable Rglob to CRLB-based control in the evaluation
stage. It means that although the contribution of individual
UAVs to the tracking system is low, DRL-based control main-
tains similar tracking performance to CRLB-based control by
building adequate geometry for target tracking.
There is a distinct difference between DRL-based control
and three control methods in runtime. Runtime increases with
the number of UAVs, the number of targets, and the size of
action space. First, the runtime complexity of the CRLB-based
control is O(NM
θ ), which increases with the size of action
space Nθ to the power of the number of UAVs M because the
CRLB-based controller calculates the CRLB of possible action
combinations to determine optimal action combination corre-
sponding to the minimum CRLB. The runtime complexity of
the DRL-based control is O(1) because the UAVs select their
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 10:14:20 UTC from IEEE Xplore.  Restrictions apply.

## Page 13

MOON et al.: DEEP REINFORCEMENT LEARNING MULTI-UAV TRAJECTORY CONTROL FOR TARGET TRACKING
15453
TABLE III
COMPARISON OF RUNTIME BY CONTROL METHODS
actions from the trained network. In order to verify the suit-
ability of DRL-based control in real-time tracking, we present
the time it takes for all UAVs to select their actions every
timestep, as shown in Table III. In Experiment 1, DRL-based
control takes 0.01 s to select one action; however, CRLB-based
control takes 56 times longer than DRL-based control, and the
runtime of DPSO-based control and GA-based control requires
about 47 times and 77 times than that of DRL-based con-
trol, respectively. In Experiment 2, DRL-based control spends
0.02 s taking one action. DRL-based control is about 61 times
faster than CRLB-based control, 59 times faster than DPSO-
based control, and 101 times faster than GA-based control.
It is conﬁrmed that DRL-based control achieves comparable
performance to CRLB-based control and is more suitable for
real-time tracking than the existing algorithms.
E. Performance in Larger-Scale Problem
The CRLB-based control is intractable in the larger-scale
problem with numerous UAVs and large size of action space
because the complexity of the CRLB-based control to select
one action combination increases exponentially with the num-
ber of UAVs. Thus, an alternative control method is needed,
such as DRL-based control, DPSO-based control, and GA-
based control. Since the previous two experiments are rela-
tively small-scale problems, the advantages of the alternative
control method are not noticeable. The GA-based control takes
more time than the CRLB-based control in Experiment 1 and
Experiment 2. However, in larger-scale problems, the DPSO-
based control and GA-based control take less time than the
CRLB-based control because the DPSO-based control and
GA-based control ﬁnd a suboptimal solution by iteratively
improving the candidate solutions.
In this experiment, there are one target whose initial vec-
tor are [x, ˙x, ¨x, y, ˙y, ¨y, z, ˙z, ¨z]⊺= [250, 0, 0, 200, 0, 0, 0, 0, 0]
with units m, m/s, m/s2, m, m/s, m/s2, m, m/s, and m/s2.
Eight UAVs are located in the vicinity of the target. The ini-
tial state vectors of eight UAVs are [x, y, z]⊺= [240, 240, 25],
[240, 260, 25], [260, 240, 25], [260, 260, 25], [240, 250, 25],
[260, 250, 25], [250, 240, 25], and [250, 260, 25] with unit
m. The rest of the parameters are the same as those set
in Experiment 2. There are 65 536 action combinations that
consider the action space of all UAVs.
Fig. 17 is the CRLB of four control methods for ten
timesteps, which is averaged over ten Monte Carlo experi-
ments. Table IV is average and standard deviation of runtime
to select one action combination. As shown in Fig. 17, the
CRLB-based control has the lowest CRLB among the four
control methods. The other three control methods achieve
Fig. 17.
CRLB of four control methods in the larger-scale problem.
TABLE IV
COMPARISON OF RUNTIME BY CONTROL METHODS
IN LARGE-SCALE PROBLEMS
similar performance as the CRLB-based control, ﬁnding a
suboptimal action combination. Regarding runtime to select
one action combination, the DRL-based control takes 0.02 s,
which requires the least time. The CRLB-based control takes
the most time to select an optimal solution by calculating the
CRLB of all action combinations. The GA-based control and
DPSO-based control select a suboptimal action combination at
every timestep and are advantageous in terms of runtime than
CRLB-based control. Through the experiment in the larger-
scale problem, it is conﬁrmed that CRLB-based control can be
replaced with alternative control methods: DRL-based control,
DPSO-based control, and GA-based control, and that DRL-
based control is the most suitable method for real-time tracking
while achieving performance close to the CRLB-based control.
VIII. CONCLUSION
It is expected that the multiple UAV control scheme for
target tracking is essential for the SAR mission in the disas-
ter environment. This article has studied DRL-based multiple
UAVs control to accurately track multiple FRs in the ﬁelds,
decreasing CRLB of FRs state estimator. The state of each
UAV is obtained by positions of other UAVs and targets.
According to the trained Q-network, each of the UAVs selects
its action control (i.e., ﬂight direction). We exploited a reward
function consisting of global reward and difference reward to
quantify the effectiveness of the selected actions. Simulation
results demonstrated that the proposed DRL-based multiple
UAVs control is an algorithm that can replace CRLB-based
control, which is advantageous for real-time tracking. For tar-
gets with various paths, DRL-based control enables multiple
UAVs to track/localize target position accurately by improv-
ing the performance of the target state estimator. Besides,
UAVs maintain an elevation angle between UAVs and targets
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 10:14:20 UTC from IEEE Xplore.  Restrictions apply.

## Page 14

15454
IEEE INTERNET OF THINGS JOURNAL, VOL. 8, NO. 20, OCTOBER 15, 2021
to ensure sufﬁcient the LoS probability from targets. DRL-
based control achieves low CRLB comparable to that of the
CRLB-based control and requires runtime at least 56× faster
than CRLB-based control.
REFERENCES
[1] Y. Zeng, R. Zhang, and T. J. Lim, “Wireless communications
with unmanned aerial vehicles: Opportunities and challenges,” IEEE
Commun. Mag., vol. 54, no. 5, pp. 36–42, May 2016.
[2] J. Wang, C. Jiang, Z. Han, Y. Ren, R. G. Maunder, and L. Hanzo,
“Taking drones to the next level: Cooperative distributed unmanned-
aerial-vehicular networks for small and mini drones,” IEEE Veh. Technol.
Mag., vol. 12, no. 3, pp. 73–82, Sep. 2017.
[3] S. Zhang, H. Zhang, B. Di, and L. Song, “Cellular UAV-to-X communi-
cations: Design and optimization for multi-UAV networks,” IEEE Trans.
Wireless Commun., vol. 18, no. 2, pp. 1346–1359, Feb. 2019.
[4] S. Zhang, H. Zhang, Q. He, K. Bian, and L. Song, “Joint trajectory
and power optimization for UAV relay networks,” IEEE Commun. Lett.,
vol. 22, no. 1, pp. 161–164, Jan. 2018.
[5] N.
Namvar,
A.
Homaifar,
A.
Karimoddini,
and
B.
Maham,
“Heterogeneous
UAV
cells:
An
effective
resource
allocation
scheme for maximum coverage performance,” IEEE Access, vol. 7,
pp. 164708–164719, 2019.
[6] H. Huang and A. V. Savkin, “An algorithm of reactive collision free 3-D
deployment of networked unmanned aerial vehicles for surveillance and
monitoring,” IEEE Trans. Ind. Informat., vol. 16, no. 1, pp. 132–140,
Jan. 2020.
[7] K. Peng et al., “A hybrid genetic algorithm on routing and scheduling
for vehicle-assisted multi-drone parcel delivery,” IEEE Access, vol. 7,
pp. 49191–49200, 2019.
[8] K. Dorling, J. Heinrichs, G. G. Messier, and S. Magierowski, “Vehicle
routing problems for drone delivery,” IEEE Trans. Syst., Man, Cybern.,
Syst., vol. 47, no. 1, pp. 70–85, Jan. 2017.
[9] M. Erdelj, E. Natalizio, K. R. Chowdhury, and I. F. Akyildiz, “Help from
the sky: Leveraging UAVs for disaster management,” IEEE Pervasive
Comput., vol. 16, no. 1, pp. 24–32, Jan.–Mar. 2017.
[10] P. Rudol and P. Doherty, “Human body detection and geolocalization
for UAV search and rescue missions using color and thermal imagery,”
in Proc. IEEE Aerosp. Conf., Big Sky, MT, USA, Mar. 2008, pp. 1–8.
[11] C. Yuan, Z. Liu, and Y. Zhang, “Fire detection using infrared images for
UAV-based forest ﬁre surveillance,” in Proc. IEEE Int. Conf. Unmanned
Aircraft Syst. (ICUAS), Miami, FL, USA, Jun. 2017, pp. 567–572.
[12] W. Zhang, K. Song, X. Rong, and Y. Li, “Coarse-to-ﬁne UAV target
tracking with deep reinforcement learning,” IEEE Trans. Autom. Sci.
Eng., vol. 16, no. 4, pp. 1522–1530, Oct. 2019.
[13] M. Wan, G. Gu, W. Qian, K. Ren, X. Maldague, and Q. Chen,
“Unmanned aerial vehicle video-based target tracking algorithm using
sparse representation,”
IEEE Internet Things J., vol. 6, no. 6,
pp. 9689–9706, Dec. 2019.
[14] C. G. Prevost, A. Desbiens, and E. Gagnon, “Extended Kalman ﬁlter for
state estimation and trajectory prediction of a moving object detected by
an unmanned aerial vehicle,” in Proc. IEEE Amer. Control Conf. (ACC),
2007, pp. 1805–1810.
[15] L. Wang, Y. Li, H. Zhu, and L. Shen, “Target state estimation and
prediction based standoff tracking of ground moving target using a ﬁxed-
wing UAV,” in Proc. IEEE Int. Conf. Control Autom. (ICCA), 2010,
pp. 273–278.
[16] Y. Sung and P. Tokekar, “GM-PHD ﬁlter for searching and tracking an
unknown number of targets with a mobile sensor with limited FOV,”
2018. [Online]. Available: arXiv:1812.09636.
[17] T. Furukawa, F. Bourgault, B. Lavis, and H. F. Durrant-Whyte,
“Recursive Bayesian search-and-tracking using coordinated UAVs for
lost targets,” in Proc. IEEE Int. Conf. Robot. Autom. (ICRA), Orlando,
FL, USA, May 2006, pp. 2521–2526.
[18] F. Gustafsson and F. Gunnarsson, “Mobile positioning using wireless
networks: Possibilities and fundamental limitations based on available
wireless network measurements,” IEEE Signal Process. Mag., vol. 22,
no. 4, pp. 41–53, Jul. 2005.
[19] V. Mnih et al., “Human-level control through deep reinforcement
learning,” Nature, vol. 518, no. 7540, pp. 529–533, 2015.
[20] Y. Zhang, Z. Zhuang, F. Gao, J. Wang, and Z. Han, “Multi-agent deep
reinforcement learning for secure UAV communications,” in Proc. IEEE
Wireless Commun. Netw. Conf. (WCNC), 2020, pp. 1–5.
[21] Q. Wang, W. Zhang, Y. Liu, and Y. Liu, “Multi-UAV dynamic wireless
networking with deep reinforcement learning,” IEEE Commun. Lett.,
vol. 23, no. 12, pp. 2243–2246, Dec. 2019.
[22] C. H. Liu, Z. Chen, J. Tang, J. Xu, and C. Piao, “Energy-efﬁcient UAV
control for effective and fair communication coverage: A deep reinforce-
ment learning approach,” IEEE J. Sel. Areas Commun., vol. 36, no. 9,
pp. 2059–2070, Sep. 2018.
[23] D. Chen, Q. Qi, Z. Zhuang, J. Wang, J. Liao, and Z. Han, “Mean ﬁeld
deep reinforcement learning for fair and efﬁcient UAV control,” IEEE
Internet Things J., vol. 8, no. 2, pp. 813–828, Jan. 2021.
[24] S. Bhagat and P. B. Sujit, “UAV target tracking in urban environ-
ments using deep reinforcement learning,” 2020. [Online]. Available:
arXiv:2007.10934.
[25] B. Li and Y. Wu, “Path planning for UAV ground target tracking via
deep reinforcement learning,” IEEE Access, vol. 8, pp. 29064–29074,
2020.
[26] C. Wang, J. Wang, Y. Shen, and X. Zhang, “Autonomous navigation of
UAVs in large-scale complex environments: A deep reinforcement learn-
ing approach,” IEEE Trans. Veh. Technol., vol. 68, no. 3, pp. 2124–2136,
Mar. 2019.
[27] C. Wang, J. Wang, J. Wang, and X. Zhang, “Deep-reinforcement-
learning-based autonomous UAV navigation with sparse rewards,” IEEE
Internet Things J., vol. 7, no. 7, pp. 6180–6190, Jul. 2020.
[28] X. Li, H. Yao, J. Wang, S. Wu, C. Jiang, and Y. Qian, “Rechargeable
multi-UAV aided seamless coverage for QoS-guaranteed IoT networks,”
IEEE Internet Things J., vol. 6, no. 6, pp. 10902–10914, Dec. 2019.
[29] X. Li, H. Yao, J. Wang, X. Xu, C. Jiang, and L. Hanzo, “A near-optimal
UAV-aided radio coverage strategy for dense urban areas,” IEEE Trans.
Veh. Technol., vol. 68, no. 9, pp. 9098–9109, Sep. 2019.
[30] H. Binol, E. Bulut, K. Akkaya, and I. Guvenc, “Time optimal multi-
UAV path planning for gathering its data from roadside units,” in Proc.
IEEE Veh. Technol. Conf. (VTC-Fall), 2018, pp. 1–5.
[31] M. L. Puterman, Markov Decision Processes: Discrete Stochastic
Dynamic Programming. New York, NY, USA: Wiley, 2014.
[32] R. S. Sutton and A. G. Barto, Reinforcement Learning: An Introduction.
Cambridge, MA, USA: MIT Press, 2018.
[33] Z. Wang, T. Schaul, M. Hessel, H. Hasselt, M. Lanctot, and N. Freitas,
“Dueling network architectures for deep reinforcement learning,” 2015.
[Online]. Available: arXiv:1511.06581.
[34] Z. R. Zaidi and B. L. Mark, “Mobility tracking based on autoregres-
sive models,” IEEE Trans. Mobile Comput., vol. 10, no. 1, pp. 32–43,
Jan. 2011.
[35] L. Mihaylova, D. Angelova, S. Honary, D. R. Bull, C. N. Canagarajah,
and B. Ristic, “Mobility tracking in cellular networks using particle
ﬁltering,” IEEE Trans. Wireless Commun., vol. 6, no. 10, pp. 3589–3599,
Oct. 2007.
[36] S. Papaioannou et al., “Coordinated CRLB-based control for tracking
multiple ﬁrst responders in 3D environments,” in Proc. IEEE Int. Conf.
Unmanned Aircr. Syst. (ICUAS), 2020, pp. 1475–1484.
[37] A. Al-Hourani, S. Kandeepan, and S. Lardner, “Optimal LAP altitude
for maximum coverage,” IEEE Wireless Commun. Lett., vol. 3, no. 6,
pp. 569–572, Dec. 2014.
[38] Y. Bar-Shalom, X. R. Li, and T. Kirubarajan, Estimation With
Applications to Tracking and Navigation: Theory Algorithms and
Software. New York, NY, USA: Wiley, 2004.
[39] I. Y. Kim and O. L. de Weck, “Adaptive weighted sum method for
multiobjective optimization: A new method for pareto front generation,”
Struct. Multidiscipl. Optim., vol. 31, no. 2, pp. 105–116, 2006.
[40] J. Wang, C. Jiang, H. Zhang, Y. Ren, K. C. Chen, and L. Hanzo,
“Thirty years of machine learning: The road to pareto-optimal wireless
networks,” IEEE Commun. Surveys Tuts., vol. 22, no. 3, pp. 1472–1514,
3rd Quart., 2020.
[41] A. K. Agogino and K. Tumer, “Analyzing and visualizing multiagent
rewards in dynamic and stochastic domains,” Auton. Agents Multi-Agent
Syst., vol. 17, no. 2, pp. 320–338, 2008.
[42] M. Colby and K. Tumer, “Fitness function shaping in multiagent
cooperative coevolutionary algorithms,” Auton. Agent Multi-Agent Syst.,
vol. 31, no. 2, pp. 179–206, 2017.
[43] B. Ristic, S. Arulampalam, and N. Gordon, Beyond the Kalman Filter:
Particle Filters for Tracking Applications. Boston, MA, USA: Artech
House, 2003.
[44] D. E. Golberg, Genetic Algorithms in Search, Optimization, and Machine
Learning. Boston, MA, USA: Addison-Wesley, 1989.
[45] W. Chen, J. Zhang, H. S. H. Chung, W. Zhong, W. Wu, and Y. Shi,
“A novel set-based particle swarm optimization method for discrete
optimization problems,” IEEE Trans. Evol. Comput., vol. 14, no. 2,
pp. 278–300, Apr. 2010.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 10:14:20 UTC from IEEE Xplore.  Restrictions apply.

## Page 15

MOON et al.: DEEP REINFORCEMENT LEARNING MULTI-UAV TRAJECTORY CONTROL FOR TARGET TRACKING
15455
Jiseon Moon (Member, IEEE) received the B.S.
degree in information communication engineering
from Inha University, Incheon, South Korea, in 2019.
She is currently pursuing the combined master’s and
Ph.D. degrees with the Department of Electronics
and Computer Engineering, Hanyang University,
Seoul, South Korea.
Her research interests include wireless localiza-
tion/positioning systems, multitarget tracking, and
location-aware communications.
Savvas Papaioannou (Member, IEEE) received the
B.S. degree in electronic and computer engineer-
ing from the Technical University of Crete, China,
Greece, in 2011, the M.S. degree in electrical engi-
neering from Yale University, New Haven, CT, USA,
in 2013, and the Ph.D. degree in computer sci-
ence from the University of Oxford, Oxford, U.K.,
in 2017.
He
is
currently
a
Research
Associate
with
the KIOS Research and Innovation Center of
Excellence, University of Cyprus, Nicosia, Cyprus.
His research interests include multiagent and autonomous systems, state esti-
mation and control, multitarget tracking, probabilistic inference, Bayesian
reasoning, and intelligent UAV systems and applications.
Dr. Papaioannou is a member of the ACM and also a reviewer for various
journals and conferences within the IEEE and ACM associations.
Christos Laoudias (Member, IEEE) received the
Diploma degree in computer engineering and infor-
matics and the M.Sc. degree in integrated hard-
ware and software systems from the University of
Patras, Patras, Greece, in 2003 and 2005, respec-
tively, and the Ph.D. degree in computer engineering
from the University of Cyprus, Nicosia, Cyprus, in
2014.
He was leading the Geolocation Technology
Group, Huawei Ireland Research Center, Dublin,
Ireland. He is a Research Lecturer with the KIOS
Research and Innovation Center of Excellence (CoE), University of Cyprus,
leading various projects and activities related to localization, tracking, and
navigation in wireless networks. During his doctoral studies and later as
a Postdoctoral Fellow with KIOS CoE, he coached the development of
several award-winning indoor localization prototype systems, which have
been released under open-source license. His research interests include posi-
tioning and tracking technologies, mobile and pervasive location-awareness,
fault-tolerant location estimation, and location-based services.
Panayiotis Kolios received the B.Eng. and Ph.D.
degrees in telecommunications Engineering from
King’s College London, London, U.K., in 2008 and
2011, respectively.
He is currently a Research Assistant Professor
with the KIOS Research and Innovation Center of
Excellence, University of Cyprus, Nicosia, Cyprus.
His interests focus on both basic and applied
research on networked intelligent systems. Some
examples of such systems include intelligent trans-
portation systems, autonomous unmanned aerial
systems, and the plethora of cyber–physical systems that arise within the
Internet of Things. Particular emphasis is given to emergency response aspects
in which faults and attacks could cause disruptions that need to be effectively
handled.
Dr. Kolios is an active member of the IEEE, contributing to a number of
technical and professional activities within the association.
Sunwoo Kim (Senior Member, IEEE) received
the
B.S.
degree
from
Hanyang
University,
Seoul,
South
Korea,
in
1999,
and
the
Ph.D.
degree from the Department of Electrical and
Computer Engineering, University of California at
Santa Barbara, Santa Barbara, CA, USA, in 2005.
Since 2005, he has been working with the
Department of Electronic Engineering, Hanyang
University, where he is currently a Professor. He
is also the Director of the 5G/Unmanned Vehicle
Research Center, funded by the Ministry of Science
and ICT, Gwacheon, South Korea. He was a Visiting Scholar with the
Laboratory for Information and Decision Systems, Massachusetts Institute
of Technology, Cambridge, MA, USA, from 2018 to 2019. His research
interests
include
wireless
communication/positioning/localization,
signal
processing, vehicular networks, and location-aware communications.
Prof. Kim is an Associate Editor of IEEE TRANSACTIONS ON VEHICULAR
TECHNOLOGY.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 10:14:20 UTC from IEEE Xplore.  Restrictions apply.
