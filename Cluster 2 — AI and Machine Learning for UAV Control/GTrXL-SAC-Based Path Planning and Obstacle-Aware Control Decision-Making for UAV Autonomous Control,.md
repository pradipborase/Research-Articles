# GTrXL-SAC-Based Path Planning and Obstacle-Aware Control Decision-Making for UAV Autonomous Control,.pdf

## Page 1

Academic Editor: Pablo Rodríguez-
Gonzálvez
Received: 20 February 2025
Revised: 26 March 2025
Accepted: 1 April 2025
Published: 3 April 2025
Citation: Huang, J.; Cui, Y.; Xi, G.;
Bai, S.; Li, B.; Wang, G.; Neretin, E.
GTrXL-SAC-Based Path Planning
and Obstacle-Aware Control
Decision-Making for UAV Autonomous
Control. Drones 2025, 9, 275. https://
doi.org/10.3390/drones9040275
Copyright: © 2025 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license
(https://creativecommons.org/
licenses/by/4.0/).
Article
GTrXL-SAC-Based Path Planning and Obstacle-Aware Control
Decision-Making for UAV Autonomous Control
Jingyi Huang 1,†
, Yujie Cui 1
, Guipeng Xi 1, Shuangxia Bai 2,†
, Bo Li 1,†
, Geng Wang 1,*
and Evgeny Neretin 3
1
School of Electronics Information, Northwestern Polytechnical University, 127 Youyi West Road,
Xi’an 710072, China; hjy803@mail.nwpu.edu.cn (J.H.); cyj0118@mail.nwpu.edu.cn (Y.C.);
xiguipeng@mail.nwpu.edu.cn (G.X.); libo803@nwpu.edu.cn (B.L.)
2
School of Computing, City University of Hong Kong, 83 Tat Chee Avenue, Kowloon Tong,
Hong Kong SAR, China; sx.bai@my.cityu.edu.hk
3
Moscow Aviation Institute, Moscow 125993, Russia; e.s.neretin@mai.ru
*
Correspondence: wanggeng@nwpu.edu.cn
†
These authors contributed equally to this work.
Abstract: Research on UAV (unmanned aerial vehicle) path planning and obstacle avoid-
ance control based on DRL (deep reinforcement learning) still faces limitations, as previous
studies primarily utilized current perceptual inputs while neglecting the continuity of flight
processes, resulting in low early-stage learning efficiency. To address these issues, this
paper integrates DRL with the Transformer architecture to propose the GTrXL-SAC (gated
Transformer-XL soft actor critic) algorithm. The algorithm performs positional embedding
on multimodal data combining visual and sensor information. Leveraging the self-attention
mechanism of GTrXL, it effectively focuses on different segments of multimodal data for
encoding while capturing sequential relationships, significantly improving obstacle recog-
nition accuracy and enhancing both learning efficiency and sample efficiency. Additionally,
the algorithm capitalizes on GTrXL’s memory characteristics to generate current drone
control decisions through the combined analysis of historical experiences and present states,
effectively mitigating long-term dependency issues. Experimental results in the AirSim
drone simulation environment demonstrate that compared to PPO and SAC algorithms,
GTrXL-SAC achieves more precise policy exploration and optimization, enabling superior
control of drone velocity and attitude for stabilized flight while accelerating convergence
speed by nearly 20%.
Keywords: SAC; self-attention mechanism; Transformer; UAV control decision-making;
multimodal data
1. Introduction
The extensive adoption of unmanned aerial vehicles (UAVs) stems from their supe-
rior maneuverability and capacity to accommodate diverse sensor payloads. Notably,
in high-risk operational domains such as military engagements, UAVs are deployed to
execute preprogrammed combat missions and reconnaissance operations. Concurrently,
continuous technological innovations and declining manufacturing costs have driven their
proliferation in commercial sectors, with applications ranging from logistics to environ-
mental monitoring. Statistical forecasts underscore this trend: Projections from the Federal
Aviation Administration (FAA) indicate that registered UAV systems in the United States
will exceed 1.88 million units over a five-year period, reflecting their exponential expansion
across industries [1].
Drones 2025, 9, 275
https://doi.org/10.3390/drones9040275

## Page 2

Drones 2025, 9, 275
2 of 30
The multifunctionality and flexibility of UAVs make them ideal for industries such
as surveillance [2], precision agriculture [3], search and rescue missions [4], aerial combat
decision-making [5,6] and cargo delivery [7]. However, due to the reliance on manual
control and the limitations of radio communication, UAVs cannot achieve optimal perfor-
mance in complex, dynamic environments, thereby reducing the overall system efficiency.
As a result, many researchers have focused on the development of highly autonomous
UAVs, enabling them to navigate and perform designated tasks based on their surrounding
environment [8]. To achieve this goal of autonomous control, UAVs must possess the
ability to perceive and understand their environment and leverage onboard computers and
sensors to compute the appropriate actions to take.
In complex urban environments or other confined spaces, UAVs face numerous chal-
lenges. They are required to perform precise navigation within limited spaces, necessitating
higher levels of autonomy and perception to adapt to rapidly changing environments and
respond quickly when encountering obstacles or other flight threats [9,10]. In this context,
this paper focuses on the motion of UAVs in low-altitude, narrow corridor environments,
addressing the demands of indoor UAV applications. The study focuses on quadrotor UAVs
equipped with sensors such as vision and GPS and investigates methods for autonomous
obstacle perception and control decision-making in narrow corridors. When executing
tasks in such environments, the control system of the UAV must possess strong robustness
to maintain stability and replan in response to changes in the task.
With the advancement of technology, the application of artificial intelligence (AI) has
surged. AI is considered an ideal tool for solving complex problems that lack clear solutions
or require extensive manual adjustments in traditional approaches [11]. Compared to con-
ventional cognitive algorithms, AI can detect anomalies, predict potential scenarios, adapt
to changes, and uncover patterns that humans might overlook [12]. However, there are
still many challenges in applying AI to autonomous UAV flight control, including reducing
training time, improving computational power, decreasing complexity, and rapidly adapt-
ing to new environments [13]. Deep reinforcement learning (DRL) [14], as a representative
algorithm, has made significant progress and has demonstrated outstanding performance
in complex competitive games. DRL enables UAVs to acquire optimal behavioral strategies
by interacting with unknown environments, mapping states to actions.
In UAV flight missions using DRL algorithms as control strategies, there exist multiple
optimal strategies. Deterministic policy deep learning (DL) algorithms are often limited by
local optima and cannot guarantee the discovery of a globally optimal strategy. Therefore,
this paper adopts two excellent stochastic policy reinforcement learning (RL) algorithms
to implement UAV perception and obstacle avoidance: the on-policy proximal policy
optimization (PPO) algorithm, based on policy gradient, and the off-policy soft actor–
critic (SAC) algorithm, based on the actor–critic framework. The choice of these two
algorithms aims to address the challenges encountered in continuous control problems.
Additionally, the stochastic nature of these algorithms enables better handling of complex
flight environments while avoiding the risk of getting trapped in local optima.
During UAV path planning and obstacle-aware control decision-making in narrow
corridor environments, each episode may encompass hundreds of steps, where each
decision-making step may depend on the global state of the entire episode. Currently,
RL primarily relies on long short-term memory (LSTM) networks to provide memory
support for agents [15]. While some memory architectures focusing on memory tasks and
partially observable environments have emerged, their application in RL remains limited
due to implementation complexities. In contrast, Transformers have been extensively tested
across many challenging domains [16]. A substantial body of research indicates that the
Transformer architecture offers significant advantages in handling sequential information

## Page 3

Drones 2025, 9, 275
3 of 30
and outperforms LSTM in terms of performance and usability. Therefore, it is considered
an ideal choice for addressing partially observable RL problems. Based on this, this paper
explores the application of Transformers in RL by integrating them into the PPO and SAC
algorithms, proposing a UAV control method based on DRL and Transformers.
2. Related Work
The UAV flight control based on artificial intelligence algorithms mainly includes
optimization-based methods and learning-based methods. The optimization-based meth-
ods primarily involve bio-inspired metaheuristic algorithms. These algorithms include the
genetic algorithm (GA) [17], ant colony optimization (ACO) [18], particle swarm optimiza-
tion (PSO) [19], the fruit fly optimization algorithm (FOA) [20], the wolf pack algorithm
(WPA) [21], and the differential evolution algorithm (DEA). These are evolutionary algo-
rithms based on biological models and optimized through biologically inspired features. In
these evolutionary algorithms, the initial population is typically generated randomly. In the
genetic algorithm, solutions are modified, and the most suitable solutions for the objective
function are selected to move to the next generation. Although the genetic algorithm has a
relatively high computational cost, with the advancement of technology, it is possible to
rapidly generate feasible paths in small environments using field-programmable gate arrays
(FPGA) and graphics processing units (GPU). The PSO algorithm updates the position of
each particle in the environment based on its best-known position and the best-known po-
sition of the swarm, thereby obtaining the optimal path. However, evolutionary algorithms
suffer from premature convergence. To address this issue, mutation operations need to be
performed regularly in the genetic algorithm to increase population diversity. Additionally,
combining the PSO algorithm with adaptive decision operators can resolve premature
convergence, and the improved PSO algorithm is capable of generating solutions superior
to those obtained by genetic algorithms, PSO, and firefly algorithms [19]. In the ACO
algorithm, the introduction of a specific chaotic factor induces disturbances, overcoming
the problems of local optima and premature convergence inherent in the algorithm [22].
Learning-based UAV control methods focus more on real-time decision-making during
flight, allowing the UAV to make sequential decisions without the need to acquire prior
environmental information [23]. This approach utilizes sensor data and real-time status
information to guide the UAV’s flight while simultaneously monitoring environmental
changes and making real-time decisions to successfully execute tasks.
In recent years, DRL and other learning methods have made significant progress in the
field of UAV navigation in unknown environments, becoming one of the focal points of re-
search. DL is a commonly used tool in vision-based UAV navigation, applied to tasks such
as target recognition and localization, image segmentation, and extracting depth informa-
tion from monocular or stereo images. Based on this, several researchers have successfully
applied deep neural networks (DNNs) for the recognition of roads and streets in urban
areas, achieving autonomous UAV navigation in extremely challenging environments
and reaching high levels of autonomous driving [24]. Menfoukh proposed an image en-
hancement method for vision-based UAV navigation using convolutional neural networks
(CNNs) [24]. Back [25] introduced a vision-based UAV navigation method utilizing CNNs,
completing tasks such as path tracking, disturbance recovery, and obstacle avoidance.
Pearson et al. proposed a method for autonomous UAV path tracking and steering using
real-time photographs and CNNs [26]. Chhikara et al. introduced a deep convolutional
neural network with genetic algorithm (DCNN-GA) architecture, where the genetic algo-
rithm is used to adjust the network’s hyperparameters. The trained DCNN-GA achieves
indoor autonomous navigation for UAVs through transfer learning [27]. This growing body

## Page 4

Drones 2025, 9, 275
4 of 30
of research demonstrates the effectiveness of deep learning techniques in enhancing UAV
navigation, enabling autonomous flight in complex and dynamic environments.
RL allows an agent to make decisions based on its current state and historical experi-
ences, learning an optimal strategy by maximizing cumulative rewards. A strategy refers
to the agent’s approach to decision-making, determining how the agent reacts and what
actions it takes in various situations. By incorporating artificial potential fields to improve
the classic Q-learning algorithm, it is possible to prevent the algorithm from getting stuck
in local optima, enabling UAV navigation in dynamic environments [23]. However, in
large-scale environments, RL-based methods tend to be computationally expensive and
can struggle with convergence.
DRL, which combines DL and RL, has achieved notable success in the field of video
games and has been effectively applied to UAV navigation. DRL methods enable UAVs to
make decisions based on their current state and continuously optimize the learned control
policies through interaction with the environment. The main advantage of DRL lies in its
ability to learn complex control strategies from data through environmental interactions,
without the need for explicit modeling of the problem. For example, Oualid et al. employed
an end-to-end CNN to fuse data from multiple sensors for controlling the UAV’s movement
and orientation [28]. This approach not only enabled UAV navigation on a 2D plane but
also allowed the UAV to avoid obstacles in dynamic environments. The deep deterministic
policy gradient (DDPG) algorithm, a method based on the Actor-Critic architecture, is
commonly used for UAV control. In this architecture, the Actor selects actions for the
UAV to perform in a continuous space, while the Critic evaluates the quality of the current
policy. The UAV control method based on DDPG enables the UAV to reach dynamic targets
successfully [29]. However, there remains an 82% to 84% probability that the UAV will
avoid collisions while reaching the destination. He et al. proposed a vision-based DRL
algorithm that models the navigation problem as a MDP and uses the twin delayed deep
deterministic policy gradient (TD3) algorithm to train UAV policies [30]. The asynchronous
advantage actor–critic (A3C) algorithm has also demonstrated high efficiency in multi-UAV
applications. Additionally, Liu et al. developed an A3C-based algorithm that uses an
improved policy gradient to update the target network by considering the observations
of the actor network, facilitating distributed energy-efficient autonomous navigation for
multi-UAVs under long-term communication coverage [31]. These studies highlight the
widespread application of DRL in visual navigation and multi-UAV collaboration, demon-
strating the effectiveness of DRL algorithms in UAV control decision-making. However,
challenges remain, and further exploration is needed to address existing limitations:
•
Challenges in UAV Modeling
Precise modeling of UAVs has long been a challenging task [32,33]. Currently, UAV
decision-making methods based on DRL often simplify the UAV system, treating it as a
point mass and neglecting critical attitude information. This simplification can lead to
a degradation in algorithm performance when applied to real-world scenarios. There-
fore, there is a need for further research into more accurate and detailed UAV modeling
approaches to better capture the complex flight dynamics and control characteristics of
UAVs [34].
•
Long-Term Dependency Problem in DRL
In DRL, the long-term dependency problem refers to the challenge of the current
action and state being linked to actions and states from a previous period. Existing algo-
rithms often struggle to effectively capture and utilize these temporal dependencies [35,36].
Additionally, the agent typically only receives meaningful rewards in the later stages of
training, making it difficult to develop an effective strategy [37,38]. Therefore, a key chal-

## Page 5

Drones 2025, 9, 275
5 of 30
lenge is determining how to establish an effective policy over a sequence of time steps
in order to maximize long-term cumulative rewards. In the context of UAV perception
and decision-making, the agent needs to remember past decisions or states in order to
consider this information when making future decisions. However, current DRL methods
typically rely on update strategies based on recent experiences, which limits their ability to
capture and exploit long-term temporal information. As a result, there is a need to explore
solutions to the long-term dependency problem in order to improve the training efficiency
and generalization ability of DRL algorithms in complex tasks.
To address the limitations of current methodologies for UAV path planning and
obstacle-aware perception, this study introduces a deep reinforcement learning (DRL)-
and Transformer-integrated perception-control framework, designated as the GTrXL-SAC
algorithm, to mitigate long-term dependency constraints in autonomous UAV operations.
The framework implements positional embeddings on multimodal data combining visual
and sensor inputs, which enables the DRL agent to decode spatiotemporal relationships
within sequential data streams and precisely reconstruct their structural hierarchies. By in-
tegrating the GTrXL module into the SAC architecture, we exploit its dual mechanisms—a
memory-augmented system preserving historical states and a self-attention architecture
modeling inter-element dependencies—thus accelerating the acquisition of environmental
dynamics. This synergistic integration facilitates context-aware synthesis of past expe-
riences with real-time observations, enabling adaptive policy generation under partial
observability conditions.
The proposed methodology synergistically integrates GTrXL architecture with mul-
timodal data fusion, yielding a unified framework for autonomous UAV navigation that
concurrently addresses path planning and obstacle-aware control. Through rigorous exper-
imental validation, the framework achieves statistically significant performance improve-
ments in dynamically complex environments when benchmarked against conventional
baseline algorithms.
3. Theoretical Foundations and Core Principles
3.1. AirSim Simulation Environment
AirSim is a high-fidelity visual and physical simulation platform developed by Mi-
crosoft in 2017 [39] based on a virtual reality simulation environment powered by Unreal
Engine 4 (UE4). The goal of this paper is to enable a quadrotor UAV to achieve autonomous
navigation in a corridor environment, effectively simulating real-time decision-making
similar to that of a human pilot. Using the Python 3.7 API of the AirSim 1.8.1 simulation
platform, the UAV’s front-facing camera images and state information are captured and
provided as input to the agent. The trained agent then returns real-time flight control com-
mands. The quadrotor UAV uses these control commands to manage its pose during flight.
The overall architecture during training is shown in Figure 1, where the UAV interacts
with the environment to gather experience data for policy optimization. The objective
is for the agent to learn the optimal strategy for controlling the UAV’s flight, guiding it
to avoid obstacles and reach a designated target point. When the UAV successfully tra-
verses the narrow corridor, a stop command is executed. A collision is detected via the
collision API, and if a collision occurs, the task is considered a failure. Multiple training
sessions are conducted in each corridor environment, with the training process and results
being recorded.

## Page 6

Drones 2025, 9, 275
6 of 30
Figure 1. AirSim overall architecture.
3.2. Quadrotor UAV Model
This paper takes a quadrotor UAV as the research object and defines it as a rigid body
model with six degrees of freedom. As shown in Figure 2, four input control quantities
{u1, u2, u3, u4} drive the rotation of four motors. The thrust Fi and torque τi generated by
the control quantity ui are both along the normal direction, and the magnitude of the force
can be calculated according to Equations (1) and (2).
Figure 2. Physical model of a quadrotor UAV.
Fi = CTρω2
maxD4ui
(1)
τi = 1
2π Cpowρω2
maxD5ui
(2)
where CT and Cpow represent the thrust coefficient and power coefficient of the motor,
respectively, ρ is the air density, D is the diameter of the propeller, and ωmax is the maximum
angular velocity of rotation. The attitude of the UAV is represented using a quaternion,
which is usually expressed as a four-component vector.
q =
"
q0
qv
#
(3)
where q0 is a scalar, and qv = [q1, q2, q3]T is a vector.
The attitude angles of the UAV can be solved using a quaternion.
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
ϖ = arctan

2(q0q1+q2q3)
1−2(q2
1+q2
2)

ϑ = arcsin(2(q0q2 −q1q3))
ψ = arccos

2(q0q3+q1q2)
1−2(q2
2+q2
3)

(4)
where ϖ ∈[−π, π], ψ ∈[−π, π], and ϑ ∈[−π
2 , π
2 ] represent the roll, yaw, and pitch angles
of the UAV, respectively.

## Page 7

Drones 2025, 9, 275
7 of 30
The flight control model of the UAV includes kinematic and dynamic models. Based
on the flight control model of the UAV, real-time calculation of the position and attitude
information of the UAV can be performed.
•
Kinematic Model of the UAV
The kinematic model is not affected by mass and force, but only considers factors such
as position, velocity, attitude, and angular velocity. The input of the kinematic model is
velocity and angular velocity, and the output is position and attitude. The kinematic model
includes position kinematics and attitude kinematics.
In the Earth-fixed coordinate system, the center of gravity of the UAV is at point Pe:
˙Pe = ve
(5)
where ve is the velocity of the UAV.
The attitude kinematics model is defined as follows:

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

˙q0 = −1
2qT
v wb
˙qv = 1
2
q0I3 + [qv]×

wb
s.t.[qv]× =


0
−q3
q2
q3
0
−q1
−q2
q1
0


(6)
where wb represents the angular velocity of the UAV in the body-fixed coordinate system,
and I3 is the identity matrix.
•
Dynamic Model of the UAV
The dynamic model of the UAV is related to the mass and rotational inertia of the
UAV. The input of the dynamic model of the UAV is thrust and torque (pitch, roll, and yaw
torques), and the output is velocity and angular velocity. Similarly, the dynamic model of
the UAV includes position dynamics and attitude dynamics. The position dynamics model
is defined as follows:
˙ve = ge3 −f
mRe3
R =


cos ϑ cos ψ
cos ψ sin ϑ sin ϖ −sin ψ cos ϖ
cos ψ sin ϑ cos ϖ + sin ψ sin ϖ
cos ϑ sin ψ
sin ψ sin ϑ sin ϖ + cos ψ cos ϖ
sin ψ sin ϑ cos ϖ −cos ψ sin ϖ
−sin ϑ
sin ϖ cos ϑ
cos ϖ cos ϑ


(7)
where m represents the mass of the UAV, f represents the magnitude of the total thrust,
g represents the acceleration due to gravity, e3 = [0, 0, 1]T represents a unit vector, and
R represents the transformation matrix from the body coordinate system to the Earth
coordinate system.
The attitude dynamics model is defined as
J · ˙
wb = −wb ×

J · wb
+ Ga + ø
(8)
where ø = [τx, τy, τz]T represents the torque generated by the thrusters, J represents the
rotational inertia, and Ga = [Ga,ϖ, Ga,ϑ, Ga,ψ] represents the gyroscopic moment.
By integrating the kinematics and dynamics models of a UAV, the control model of a
quadrotor UAV can be obtained.

## Page 8

Drones 2025, 9, 275
8 of 30

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

˙Pe = ve
˙ve = ge3 −f
mRe3
˙q0 = −1
2qT
v wb
˙qv = 1
2
q0I3 + [qv]×

wb
J · ˙wb = −wb ×

J · wb
+ Ga + ø
(9)
3.3. Soft Actor-Critic (SAC) Algorithm in Reinforcement Learning
The SAC algorithm is a model-free, non-deterministic policy method that optimizes
stochastic policies through asynchronous updates. It has demonstrated superior perfor-
mance on various RL benchmark tasks [40,41].
The entropy of the SAC policy π is defined as
H(π(· | st)) = E(−log π(· | st))
(10)
where st denotes the state of the agent at time step t. The SAC algorithm enhances the
objective of traditional RL by incorporating policy entropy:
J(π) =
T
∑
t=0
γtE(st,at)∼π[R(st, at) + αH(π(· | st))]
(11)
where α is the entropy regularization coefficient, γ is the discount factor, and R(st, at)
represents the reward received in state st when executing action at.
The corresponding value function is given by
V(s) = E(st,at)∼π
"
T
∑
t=0
γt(R(st, at) + αH(π(· | st)) | st = s)
#
(12)
By constructing a flexible Bellman equation to maximize entropy, the entropy is
treated as part of the reward during the iterative process. When computing the action value
function Q(st, at), the entropy of the current state is also taken into account. Thus, the state
action value function Q(st, at) is defined as
Q(st, at) = R(st, at) + γEst+1,at+1∼π[Q(st+1, at+1) −α log(π(·|st+1 ))]
(13)
The SAC algorithm is implemented based on neural networks, including the policy
network πθ(st, at), the Q-network Qϕi(st, at), and the target Q-network Qϕi′(st, at), where
θ, ϕi, ϕi′(i ∈{1, 2}) denotes the parameters of the neural networks. The parameters of
the target Q-network Qϕi′(st, at), denoted as ϕi′, are periodically updated by copying from
the learned Q-network Qϕi(st, at). SAC is an offline policy algorithm that stores a series of
transition tuples {(st, at, rt, st+1)}N
t=1 in the experience replay buffer D. During the training
of network parameters, a batch of transition tuples is randomly sampled from the replay
buffer, and stochastic gradient descent (SGD) is applied to minimize the following loss
objectives for θ and ϕi:
JQ(ϕi) =
T
∑
t=0
E(st,at,st+1)∼D
1
2

Qϕi(st, at) −R(st, at) −γVϕi′(st+1)
2
(14)
where Vϕi′(st+1) = Eat+1∼πθ
h
Qϕi′(st+1, at+1) −α log πθ(at+1|st+1 )
i
.
Jπ(θ) = Est∼D,at∼πθ
log πθ(at|st) −Qϕ(st, at)

(15)
where Qϕ(st, at) = min
Qϕ1(st, at), Qϕ2(st, at)

.

## Page 9

Drones 2025, 9, 275
9 of 30
During training, the fixed entropy regularization coefficient can lead to instability
due to the continuous variation of rewards. Therefore, by formulating a constrained
optimization problem to limit the weight of the policy entropy, the regularization coefficient
can be adjusted across different states, thereby improving the stability of the training
process, as shown in the following equation:
max
π0,...,πT E
"
T
∑
t=0
R(st, at)
#
s.t.∀t, H(πt) ≥H0
(16)
When the action is adaptively adjusted, the loss function is expressed as
J(α) = Est∼D,at∼πϕ[−α log πt(at|(st, α)) −αH0]
(17)
where H0 represents the target entropy.
3.4. Attention Mechanism: Gated Transformer-XL (GTrXL) Architecture
Transformer has achieved breakthrough success in natural language processing due to
its ability to efficiently integrate information over long time spans and its scalability to large
datasets. As a result, many researchers have suggested that the Transformer’s capability to
handle long-term dependencies could potentially improve performance in partially observ-
able RL settings. However, in practical experiments, large-scale Transformers have failed
to be successfully applied to RL. The classical Transformer faces significant optimization
challenges, leading to performance comparable to random policies. To enhance perfor-
mance, complex learning rate adjustments or specialized weight initialization schemes
are often required. Nevertheless, these measures are still insufficient for RL. To address
this challenge, Parisotto [42] introduced a Transformer variant called Gated Transformer-
XL(GTrXL), which outperforms LSTM in various memory-intensive environments. GTrXL
stabilizes the training process by reordering the normalization layers and incorporating
new gating mechanisms. Compared to the traditional Transformer, GTrXL learns faster and
more stably. The framework of GTrXL is illustrated in Figure 3a.
(a)
(b)
Figure 3. (a) The GTrXL architecture. (b) The TrXL-I architecture.
•
Identity Map Reordering
Although traditional Transformers utilize residual networks, the subsequent appli-
cation of normalization layers alters the values passed through at each stage. GTrXL
introduces the concept of “identity map reordering”, which involves moving the nor-
malization layers inside the residual connections, transforming the residual process from
LayerNorm(x + MultiHeadAttention(x)) to x + MultiHeadAttention(LayerNorm(x)), x
denotes an individual input value in the input sequence (x1, · · · , xn) of the Transformer
model. This change enables an identity mapping from the input of the first layer to the
output of the final layer. The model incorporating this “identity map reordering” is referred
to as TrXL-I, as illustrated in Figure 3b. The reordering of the normalization layers creates

## Page 10

Drones 2025, 9, 275
10 of 30
a path within each submodule that includes two linear layers. ReLU is applied to the
activations of the submodule output before passing it through.
•
Relative Positional Encoding
The basic multi-head self-attention operation does not explicitly account for the order
of the sequence, as it is permutation-invariant. To capture more extensive bidirectional
context representations, relative positional encoding and a memory scheme are employed.
In this setup, an additional memory tensor M(l) ∈RT ×D with T steps is introduced, which
remains unchanged during weight updates. The formula for the multi-head attention
submodule in this setting is as follows:
Y(l) = LN

E(l−1) + RMHA

SG

M(l−1)
, E(l−1)
(18)
In this context, LN refers to layer normalization, SG is a stop-gradient function, and
RMHA denotes relative multi-head attention with relative positional encoding. E(l−1)
represents the input to the submodule, which is the embedding from the previous layer,
denoted as E(l−1) ∈RT×D. Here, T denotes the time step, and D refers to the hidden
dimension. l ∈[0, L] represents the layer index in a total of L layers.
•
The Gating Layer
To further improve the model’s performance and optimization stability, the residual
connections are replaced with gating layers. The final computation process of GTrXL is
as follows:
¯Y(l) = RMHA

LN
h
SG

M(l−1)
, E(l−1)i
Y(l) = g(l)
MHA

E(l−1), ReLU

¯Y(l)
¯E(l) = f (l)
LN

Y(l)
E(l) = g(l)
MLP

Y(l), ReLU

¯E(l)
(19)
where g denotes a gating function. MLP refers to a multi-layer perceptron. The gated
recurrent unit (GRU) is employed as the gating layer, with its robust gating mechanism
being adapted to function as a non-associated activation function within the deep network:
r = σ

W(l)
r y +U(l)
r x

z = σ

W(l)
z y + U(l)
z x −b(l)
g

ˆh = tanh

W(l)
g y + U(l)
g (r ⊙x)

g(l)(x, y) = (1 −z) ⊙x + z ⊙ˆh
(20)
4. UAV Control Based on the GTrXL-SAC Algorithm
The SAC algorithm, as an RL approach, can enhance environmental perception and
learning performance when combined with GTrXL. The sequence modeling and attention
mechanisms of GTrXL enable more effective learning of the dynamic characteristics of the
environment, thereby improving the performance of SAC in complex tasks. Consequently,
this paper introduces the GTrXL-SAC algorithm by integrating GTrXL with SAC. The
GTrXL-SAC algorithm achieves superior performance in UAV control, particularly in
handling long sequences of information, leveraging memory and attention mechanisms,
and improving RL efficiency. The comprehensive architectural framework for UAV path
planning and obstacle-aware perception-control tasks, based on the GTrXL-SAC algorithm,
is systematically illustrated in Figure 4.

## Page 11

Drones 2025, 9, 275
11 of 30
Figure 4. Architectural diagram of the GTrXL-SAC algorithm.
4.1. Mathematical Modeling of Decision Problems
DRL algorithms provide UAV with the ability to perceive their environment and make
decisions based on current observations. GTrXL, as a powerful sequence modeling tool,
is capable of effectively handling information over long time horizons and has achieved
significant success in fields such as natural language processing. In UAV control, since
flight is a continuous process, it is crucial to account for the impact of previous observations
and actions on current decision-making. Memory plays a vital role in enabling the UAV to
understand past states and actions, and the memory and attention mechanisms in GTrXL
can better capture and leverage this information.
Therefore, this paper proposes the GTrXL-SAC algorithm by combining the GTrXL
and SAC algorithms. This algorithm takes full advantage of the memory capacity of GTrXL,
allowing the RL process to consider both historical information and current observations in
order to make more comprehensive and informed decisions. Additionally, the self-attention
mechanism in GTrXL enables the model to focus on information from different positions in
the input sequence, improving the efficiency of obstacle detection.
4.1.1. Problem Formulation
To enhance the representational efficiency and solvability of UAV mission objectives,
the proposed algorithm formally integrates UAV path planning and obstacle-aware percep-
tion tasks within a partially observable Markov decision process (POMDP) framework. This
formulation systematically addresses state uncertainty through belief-space optimization
while maintaining adaptability to dynamic environmental constraints.
P = ⟨S, A, Υ, R, Ω, O⟩
(21)
where, S, A, Υ, R, Ω, O denote the state space, action set, transition function, reward func-
tion, observation set, and observation function, respectively.
•
State Space
In this paper, the state space of the UAV is defined using both the UAV’s own state data
and multimodal data, which integrates the images recorded by the UAV’s front-mounted
camera along with its own state information.
S1 = [Pe, ve, q] = [px, py, pz, vx, vy, vz, q]
(22)

## Page 12

Drones 2025, 9, 275
12 of 30
S2 = [S1, image]
(23)
where Pe = [px, py, pz] represents the position vector of the UAV in the Earth coordinate
system, ve = [vx, vy, vz] represents the velocity vector of the UAV in the Earth coordinate
system, and q is the quaternion representing the UAV’s attitude.
When detecting obstacles, gradient calculation is performed using grayscale images.
A color image is obtained through an API interface, with each pixel having a range of over
16 million (255 × 255 × 255). The computational load for processing color images is too
large, so it is necessary to convert the image to grayscale.
•
Action Space
Due to the highly nonlinear nature of the kinematic and dynamic models of multi-rotor
UAVs, the direct application of model-free RL for end-to-end control remains challenging.
To address this limitation, this paper proposes a hierarchical control decision-making
framework that integrates RL with conventional PID control. Figure 5 illustrates the
architecture of this hierarchical model, which synergizes high-level policy learning with
low-level stability guarantees.
Figure 5. Schematic diagram of the hierarchical decision-making model architecture.
The RL policy governs the upper-level decision-making process, where the action
space of the RL model is defined as the UAV’s velocity vector during flight control, as
formalized in Equation (24). At the low-level control layer, a PID controller maps the
generated velocity commands into motor actuation signals, enabling precise execution
of pitch, roll, yaw, acceleration, and deceleration maneuvers. This hierarchical training
architecture significantly enhances both the policy performance and convergence rate of
the RL framework through two synergistic mechanisms.
A = [vx, vy, vz]
(24)
4.1.2. Long-Term Dependency Modeling in Sequential Decision Processes
Local environmental information derived from sensor and image data defines the
historical observation sequence within time window η.
Ht =

ot−η, ot−η+1, · · · , ot
	
(25)
Enhanced state representations are generated via GTrXL:
ht = GTrXL(Ht) =
η
∑
k=0
δt−k · Φ(ot−k)
(26)
where Φ() denotes the observation embedding function (integrating sensor/image data),
and δt−k is dynamically computed through multi-head attention mechanisms. The mecha-
nism effectively mitigates the vanishing gradient problem.

## Page 13

Drones 2025, 9, 275
13 of 30
4.1.3. Objective Function and Operational Constraints
•
Objective Function
Maximize the entropy-regularized expected return under the SAC framework:
π∗= arg max
π E(s,a)∼ρπ
"
T
∑
t=0
γt(R(st, at) + αH(π(· | st)))
#
(27)
•
Reward Function and Operational Constraints
The aim of this study is to develop a method for planning the flight path of a UAV
within a narrow corridor to accomplish specific flight tasks. The task requires the UAV to
avoid obstacles in the environment as quickly as possible while ensuring safety, ultimately
reaching the destination successfully. Therefore, the time required to complete the flight
task and the avoidance of collisions are considered the primary objectives in UAV flight
decision-making. To achieve this, two types of reward functions are defined in this study:
continuity-based rewards and sparsity-based rewards. If the reward function only includes
sparse rewards, it will fail to accurately evaluate the UAV’s decision-making process before
avoiding obstacles. Conversely, if the reward function only includes continuous rewards,
the RL algorithm may fail to receive rewards over long periods, leading to a dilemma
of perpetual exploration. This situation can severely affect the convergence speed of the
algorithm, or even prevent it from converging altogether. Therefore, by considering both
continuity-based and sparsity-based rewards, a more comprehensive evaluation of the
UAV’s flight strategy can be achieved.
The designed reward function includes components related to position, velocity,
and collisions. The position reward is further divided into sparse position rewards and
continuous position rewards. The sparse position reward indicates the successful passage
of the UAV through a specific obstacle:
r1(p) = 2 · (1 + np/Nb)
(28)
where np denotes the number of obstacles navigated by the UAV, and Nb represents the
total number of obstacles within the entire channel.
The positional reward is formulated as a continuous function of the distance between
the UAV’s current coordinates and the target destination, specifically defined as
r2(p) =
q
(px,t −px,t−1)2 + (py,t −py,t−1)2 + (pz,t −pz,t−1)2
q
dx2 + dy2 + dz2
(29)
where (px,t, py,t, pz,t) and (px,t−1, py,t−1, pz,t−1) denote the UAV’s positional coordinates at
time steps t and t −1, respectively, while (dx, dy, dz) represents the destination coordinates
throughout the mission.
In the experimental setup, the entire channel is aligned along the Y-axis with its origin
designated as the starting point. To guide the UAV toward the target direction, a continuous
velocity-based reward mechanism is implemented.
r3(v) =
(
0.03 · vy,
i f
vy > 0
−0.1,
else
(30)
To ensure the UAV maintains a sufficiently high velocity during flight, a velocity-based
sparse reward function is formulated.

## Page 14

Drones 2025, 9, 275
14 of 30
r4(v) =
(
−0.1,
i f
v < vmin
0,
else
(31)
In the event of a collision, the UAV mission is classified as failed, and a collision
penalty is rigorously defined within the reward structure.
r5 =
(
−2,
i f
collision
0,
else
(32)
Synthesizing the above components, the comprehensive reward function R is mathe-
matically formulated as
R = r1(p) + r2(p) + r3(v) + r4(v) + r5
(33)
where the task-specific dynamic constraints are
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
vmin < v ≤vmax(Velocity Constraint)
pe
t −poi
t

2 ≥dsa f e, ∀i ∈[1, Nb](Safety Margin)
ϖ ∈[−π, π], ψ ∈[−π, π], ϑ ∈[−π
2 , π
2 ](Attitude Constraint)
Zmin ≤pz < Zmax(Altitude Constraint)
(34)
4.2. The Algorithm Flow
This section mainly introduces the workflow of the GTrXL-SAC algorithm and pro-
vides the pseudocode. The algorithm consists of two main stages. The GTrXL perception
processing is described as follows, with the overall pseudocode of the algorithm presented
in Algorithm 1.
Phase 1
Perception and Decision-Making Phase
Phase 1-1 Initialize the parameters of the policy network (Actor) parameters θ, the
Q-network (Critic) parameters ϕ1, ϕ2, and the target Q-network parameters
ϕ1′, ϕ2′. Both the actor and critic networks incorporate GTrXL. If the state in-
formation includes images, a CNN is used within the network to process the
image data.
Phase 1-2 The sensor information is embedded and encoded in terms of relative position
to represent the current input state:
position_embedding(st) = [st · sin(pos/100002i/d mod el), st · cos(pos/100002i/d mod el)] (35)
where st represents the current input state.
Phase 1-3 After receiving the input embedding, GTrXL computes the UAV’s action at.
at = GTrXL(PE)
(36)
As shown in Figure 4, the internal operation flow of GTrXL for obtaining the
action is as follows:
1.
Acquire Memory Information;
2.
Merge Memory Information with Current Input Embedding PE: x1 =
[memory, PE];
3.
Perform Normalization;
4.
The attention distribution is computed according to the equation
Attention(Q, K, V) = so f t max( QKT
√
dk )V;

## Page 15

Drones 2025, 9, 275
15 of 30
5.
The attention distribution and positional encoding (PE) are processed
through a gating mechanism (GRU1) to obtain the result o1, with the
internal computation described by Equation (20);
6.
Perform normalization;
7.
The multilayer perceptron (MLP) computation: Here, the MLP essentially
refers to a fully connected neural network;
8.
The result o1 and the output of the multilayer perceptron are processed
through a gating mechanism (GRU2) to obtain the final output o;
9.
The output is passed through a softmax function to obtain the UAV’s
action at = so f t max(o).
Phase 1-4 Update the memory information.
Algorithm 1 Pseudocode for the GTrXL-SAC algorithm.
Input: Initialize an empty experience pool, entropy regularization coefficient, maximum
simulation steps per round T, step size start_size for starting with the policy network,
and batch size batch_size for training.
Output: UAV flight strategy.
1. Initialize the strategy network weights θ, Q network weights ϕ1, ϕ2, and target Q
network weights ϕ1′ ←ϕ1, ϕ2′ ←ϕ2.
2. For episode = 0, 1, ..., n:
3.
Reset the environment and obtain the initial state s0.
4.
While the task is not completed:
5.
IF t < start_size:
6.
at = random().
7.
ELSE
8.
The Actor network outputs an action at = πθ(st) ;
9.
The UAV executes an action at, obtains the next state st+1, and calculates the
reward rt;
10.
The transition tuple < st, at, rt, st+1 > is stored in the experience pool.
11.
IF the number of transition tuples stored in the experience pool > batch_size:
12.
Based on formula
JQ(ϕi) =
T
∑
t=0
E(st,at,st+1)∼D

1
2

Qϕi(st, at) −r(st, at) −γVϕi′(st+1)
2
, calculate the loss
value of the Q network and compute the gradient ∇ϕJ(ϕ) with respect to the
parameters ϕ ;
13.
Compute the loss value of the policy network based on Equation
Jπ(θ) = Est∼D,at∼πθ
log πθ(at|st) −Qϕ(st, at)

, and calculate the gradient ∇θ J(θ) of the
parameter θ with respect to the loss;
14.
Compute the loss value of the entropy regularization coefficient based on
Equation J(α) = Est∼D,at∼πϕ[−α log πt(at|(st, α)) −αH0], and calculate the gradient
∇αJ(α) of the parameter α.
15.
Update the parameters θ, ϕi, ϕi′(i ∈{1, 2}) of the policy network and
Q-network according to optimization algorithms;
16.
Update the target Q-network.
17.
End IF
18.
Jump to step 5.
19. End For
5. Network Architecture and Parameter Design
5.1. Network Architecture Design
This paper designs and implements the GTrXL-PPO and GTrXL-SAC algorithms based
on the actor–critic architecture, which includes the actor network, critic network, and
experience pool. Both GTrXL-PPO and GTrXL-SAC share the same actor network structure,
but their critic networks differ slightly. In GTrXL-PPO, the critic network takes the current

## Page 16

Drones 2025, 9, 275
16 of 30
state as an input, while in GTrXL-SAC, the critic network receives both the state and the
action as inputs. The study presents two variations of the actor–critic architecture: one
based on sensor data and another based on multimodal data that combines both image and
sensor information.
5.1.1. Actor–Critic Architecture Based on Sensor Data
The input to the actor neural network is the state space S1 = [Pe, ve, q], as de-
fined in the MDP, which includes the UAV’s position vector, velocity vector, and attitude
quaternion. By combining these sensor inputs, a 1 × 10 dimensional vector, denoted as
st = [pt
x, pt
y, pt
z, vt
x, vt
y, vt
z, qt], is obtained. Since these data are of low dimensionality, a neural
network architecture consisting of two fully connected layers and four GTrXL layers is used
for the actor network, as shown in Figure 6a. The input dimension of GTrXL is 48, with
4 attention heads and an embedding dimension of 48. This design is compared to a fully
connected neural network consisting of five fully connected layers, as shown in Figure 6b.
(a)
(b)
Figure 6. (a) Diagram of the actor network architecture with sensor information as input. (b) Diagram
of the actor network architecture with sensor information as input for comparative experiments.
The input to the critic network consists of the state space and action space of the MDP.
The critic networks of the GTrXL-PPO and GTrXL-SAC algorithms differ slightly in the
initial fully connected layers, while the remaining structures are identical. Here, we focus
on describing the critic network architecture of the GTrXL-SAC algorithm. Similar to the
actor neural network, the critic network employs a neural architecture that includes two
fully connected layers followed by four layers of GTrXL, as shown in Figure 7a. In this
design, the input dimension of GTrXL is 48, with 4 attention heads and an embedding
dimension of 48. This design is compared with a fully connected neural network containing
four fully connected layers, as illustrated in Figure 7b.
(a)
(b)
Figure 7. (a) Diagram of the critic network architecture with sensor information as input. (b) Diagram
of the critic network architecture with sensor information as input for comparative experiments.
5.1.2. Actor–Critic Architecture Based on Multimodal Data
In terms of input, this section utilizes multimodal data, including both sensor data and
image data. The collected image data consist of grayscale images with a size of 144 × 256.
Given that image data are high-dimensional, they cannot be directly concatenated with
sensor data and input into the neural network. Therefore, additional processing of the
image data is required. In this study, a CNN is employed to process the images. The

## Page 17

Drones 2025, 9, 275
17 of 30
network consists of six convolutional layers, four pooling layers, and one fully connected
layer, with the specific architecture shown in Figure 8.
Figure 8. The convolutional neural networks for processing image information.
As shown in Figure 9a, the grayscale image with a size of 144 × 256 is first processed.
After passing through the convolutional and pooling layers, the image is transformed
into a 72-dimensional vector. Meanwhile, the 10-dimensional flight state data (including
position, velocity, and attitude) are processed through a fully connected layer to produce
a 48-dimensional vector. These two sets of vector data are then combined and processed
through four layers of GTrXL, yielding a 48-dimensional output. Finally, the output is
passed through a fully connected layer to produce the UAV’s decision-making action.
To validate the performance advantage brought by GTrXL, a comparative experiment is
conducted where a CNN is used to process the multimodal data. This network consists
of six convolutional layers, four pooling layers, and five fully connected layers, as shown
in Figure 9b.
(a)
(b)
Figure 9. (a) The actor network architecture diagram for multimodal data input. (b) The actor
network architecture diagram for multimodal data input used in comparative experiments.
The actor network architecture diagram for multimodal data input used in comparative
experiments. As shown in Figure 10a, the process begins by processing a grayscale image
with dimensions of 144 × 256. After passing through convolutional and pooling layers, the
image is transformed into a 72-dimensional vector. Simultaneously, the 10-dimensional
flight state data, which include position, velocity, and attitude, are processed through fully
connected layers to generate a 24-dimensional vector. Additionally, the UAV’s velocity
is processed through another fully connected layer, producing another 24-dimensional
vector. These three sets of vector data are then concatenated and passed through four
layers of the GTrXL model, resulting in a 48-dimensional output. Finally, this output is
processed through a fully connected layer to generate the value function, which evaluates
the quality of the actions taken. For comparison, the performance of the GTrXL-based
improved algorithm is validated by contrasting it with a traditional convolutional neural
network, as shown in Figure 10b.

## Page 18

Drones 2025, 9, 275
18 of 30
(a)
(b)
Figure 10. (a) The critic network architecture diagram for multimodal data input. (b) The critic
network architecture diagram for multimodal data input used in comparative experiments.
The network architecture of the actor, which takes multi-modal data as input, is shown
in Table 1.
Table 1. The parameters of the actor network architecture for multimodal data input.
Neural Network Name
Convolutional Kernel Parameters/
Input and Output Dimensions
Activation Function
Convolutional Layer-1
Convolutional Kernel: 3 × 3 × 16 Stride: 1
ELU
Pooling Layer-1
Convolutional Kernel: 4 × 4 Stride: 2
-
Convolutional Layer-2
Convolutional Kernel: 3 × 3 × 32 Stride: 1
ELU
Pooling Layer-2
Convolutional Kernel: 4 × 4 Stride: 2
-
Convolutional Layer-3
Convolutional Kernel: 3 × 3 × 32 Stride: 1
ELU
Pooling Layer-3
Convolutional Kernel: 3 × 3 Stride: 2
-
Convolutional Layer-4
Convolutional Kernel: 3 × 3 × 16 Stride: 1
ELU
Pooling Layer-4
Convolutional Kernel: 3 × 3 Stride: 2
-
Convolutional Layer-5
Convolutional Kernel: 3 × 3 × 8 Stride: 1
ELU
Convolutional Layer-6
Convolutional Kernel: 3 × 3 × 4 Stride: 1
ELU
Fully Connected Layer-1
Input and Output Dimensions: (10, 48)
Tanh
Fully Connected Layer-2
Input and Output Dimensions: (120, 48)
Tanh
GTrXL-1
Input and Output Dimensions: (48, 48)
-
GTrXL-2
Input and Output Dimensions: (48, 48)
-
GTrXL-3
Input and Output Dimensions: (48, 48)
-
GTrXL-4
Input and Output Dimensions: (48, 48)
-
Fully Connected Layer-3
Input and Output Dimensions: (48, 3)
Softmax
The critic network architecture with multimodal data as input is shown in Table 2.
Table 2. Critic network architecture with multimodal data as input.
Neural Network Name
Convolutional Kernel Parameters/
Input and Output Dimensions
Activation Function
Convolutional Layer-1
Convolutional Kernel: 3 × 3 × 16 Stride: 1
ELU
Pooling Layer-1
Convolutional Kernel: 4 × 4 Stride: 2
-
Convolutional Layer-2
Convolutional Kernel: 3 × 3 × 32 Stride: 1
ELU
Pooling Layer-2
Convolutional Kernel: 4 × 4 Stride: 2
-
Convolutional Layer-3
Convolutional Kernel: 3 × 3 × 32 Stride: 1
ELU
Pooling Layer-3
Convolutional Kernel: 3 × 3 Stride: 2 -
Convolutional Layer-4
Convolutional Kernel: 3 × 3 × 16 Stride: 1
ELU
Pooling Layer-4
Convolutional Kernel: 3 × 3 Stride: 2
-
Convolutional Layer-5
Convolutional Kernel: 3 × 3 × 8 Stride: 1
ELU
Convolutional Layer-6
Convolutional Kernel: 3 × 3 × 4 Stride: 1
ELU

## Page 19

Drones 2025, 9, 275
19 of 30
Table 2. Cont.
Neural Network Name
Convolutional Kernel Parameters/
Input and Output Dimensions
Activation Function
Fully Connected Layer-1
Input and Output Dimensions: (10, 24)
Tanh
Fully Connected Layer-2
Input and Output Dimensions: (10, 24)
Tanh
Fully Connected Layer-3
Input and Output Dimensions: (120, 48)
Tanh
GTrXL-1
Input and Output Dimensions: (48, 48)
-
GTrXL-2
Input and Output Dimensions: (48, 48)
-
GTrXL-3
Input and Output Dimensions: (48, 48)
-
GTrXL-4
Input and Output Dimensions: (48, 48)
-
Fully Connected Layer-4
Input and Output Dimensions: (48, 1)
Softmax
The overall training process is as follows: First, the UAV captures environmental image
information through its front camera. These image data, along with sensor information,
are fed into the actor network of the RL model for decision-making, resulting in the UAV’s
flight speed. Based on the reward function designed in Section 4.1.3, the reward value
corresponding to a specific speed in the current state is computed. The UAV’s state, action,
and reward are stored in the experience replay buffer, which serves as the training data for
the RL model. During training, samples are randomly drawn from the experience buffer to
train the RL model.
5.2. Algorithm Parameter Design
Table 3 lists the various parameters of the GTrXL-PPO algorithm. The learning rate
refers to the learning rate in the Adam optimizer. The policy update constraint ε is used
to limit the policy gradient updates during training to prevent abnormal changes in the
RL policy. EPS represents the policy exploration factor in the GTrXL-PPO algorithm.
The discount factor γ indicates the degree to which future rewards are discounted when
calculating the value function. The parameter λ is the coefficient for the extended advantage
function and is used to adjust the variance and bias of the advantage function. The number
of sampling episodes represents the number of episodes sampled during each training
iteration of the GTrXL-PPO algorithm. The batch size refers to the number of experience
samples randomly sampled from the experience buffer during each training step of the
RL model. The maximum number of training episodes denotes the maximum number of
training episodes for the GTrXL-PPO algorithm. The maximum steps per episode indicates
the maximum number of steps for each sampling episode, which refers to the number
of interactions between the UAV and the environment. The Loss_coeff_value represents
the coefficient of the value loss term in the GTrXL-PPO algorithm’s loss function. The
Loss_coeff_entropy represents the coefficient of the entropy loss term in the loss function
of the GTrXL-PPO algorithm.
Table 3. The parameters of the GTrXL-PPO algorithm.
Parameters
Values
Parameters
Values
lr
0.0004
batch_size
256
ε
0.2
Maximum episodes
1000
EPS
1−10
Maximum steps per episode
200
γ
0.995
Loss_coeff_value
0.5
λ
0.97
Loss_coeff_entropy
0.01
Number of sampling episodes
10

## Page 20

Drones 2025, 9, 275
20 of 30
The parameter settings for the GTrXL-SAC algorithm are detailed in Table 4. The initial
value of the entropy regularization coefficient is set to 0.2, and it is automatically decayed
during training according to Equation (16). The learning rate represents the learning rate in
the Adam optimization algorithm. The experience pool size refers to the maximum number
of experience samples that can be stored in the experience replay buffer. The batch size
indicates the number of experience samples randomly sampled from the experience pool
during each training iteration of the RL model. Exploration noise represents the exploration
factor in the GTrXL-SAC algorithm’s policy. The training start step refers to the point
at which training begins once the number of samples in the experience pool reaches the
specified number of steps.
Table 4. The parameters of the GTrXL-SAC algorithm.
Parameters
Values
Entropy regularization coefficient
Initialized to 0.2 with automatic decay
lr
0.0006
Experience replay buffer size
100,000
batch_size
256
Exploration noise
0.1
Target network update frequency
1
Training start steps
1000
6. Experimental Design and Results Analysis with Discussion
In this section, the algorithm’s performance will be discussed from two perspectives:
training speed and control stability. First, the effectiveness of incorporating the Transformer
architecture into RL is validated by comparing the training process of GTrXL-PPO to PPO
and GTrXL-SAC with SAC. Next, the superiority of the Transformer architecture in RL is
further demonstrated by comparing the UAV flight trajectories guided by the resulting
policies. It is worth noting that experiments are conducted using both sensor data and
multimodal data, which integrates image and sensor information, to comprehensively
evaluate the model’s performance.
6.1. Simulation Environment Design
Figure 11 clearly illustrates the obstacles present in the environment and their spe-
cific locations. Three simulation environments are designed, all of which feature narrow
corridors with obstacles arranged along the y-axis.
In Environment 1, four different types of obstacles are set up. The first is a cylindrical
obstacle with a y-coordinate of 5 m; the second is a beam-shaped obstacle located at a
y-coordinate of 20 m; the third is a square channel situated at a y-coordinate of 25 m; and
the fourth is an S-shaped narrow curve positioned at a y-coordinate of 35 m. The endpoint
is also located at a y-coordinate of 35 m. Environment 2 contains the same four types of
obstacles as in Environment 1, but their sizes and positions are distributed differently, with
the endpoint at a y-coordinate of 45 m. Environment 3 introduces four different types
of obstacles, including a U-shaped channel, an arched narrow passage, and an inclined
cylindrical obstacle.
In all three simulation environments, the UAV’s initial coordinates are set to (0, 0, 0).
The success criteria for the flight task are that the UAV must avoid collisions throughout
the entire process, skillfully navigate around obstacles, and ultimately reach the endpoint
safely. Given the size of the experimental scenario, the UAV’s speed limit is set to 2 m/s.
To validate the effectiveness of the proposed GTrXL-SAC algorithm, we first compare
the training speed of the algorithms. By observing the learning curves of GTrXL-PPO

## Page 21

Drones 2025, 9, 275
21 of 30
versus PPO and GTrXL-SAC versus SAC under the same task conditions, we can assess
the impact of the GTrXL architecture on accelerating model convergence. If the algorithms
incorporating GTrXL perform better under the same number of iterations, it would indicate
a superior advantage in improving training speed.
Figure 11. Experimental simulation environment diagram.
Next, we compare the control stability of the policies. The performance of policies
trained by different algorithms is evaluated on UAV flight tasks, considering factors such as
UAV flight trajectory, velocity curve, attitude curve, and decision step length. This allows
us to assess the contribution of the GTrXL architecture to enhancing the control stability of
the policy, ensuring the effectiveness of the learned policies in real-world tasks.
Additionally, two experimental settings will be used: sensor data and multimodal
data. This helps us to verify the model’s generalizability under different input conditions
and to confirm the performance of the GTrXL architecture when handling multimodal data,
offering a more comprehensive evaluation of its applicability.
Through the above analyses, a thorough and in-depth argument will be provided
to demonstrate the superiority of the GTrXL-PPO and GTrXL-SAC algorithms, which
incorporate the GTrXL architecture, in RL tasks.
6.2. Experiment 1: UAV Perception and Control with Sensor Data as Input
In Experiment 1, sensor data are used as input to compare the convergence perfor-
mance during training and the flight performance during testing of the PPO, GTrXL-PPO,
SAC, and GTrXL-SAC algorithms. It is important to note that during testing with the actor
network, the actions will be deterministic, meaning the “average” expected action will be
the actual action taken during testing. However, during training, a normal distribution is
used to introduce noise and expand the exploration space for the policy.
•
Training Speed Comparison
In Environment 1, the reward curves during the training process for the PPO, GTrXL-
PPO, SAC, and GTrXL-SAC algorithms are shown in Figure 12a. As observed, both the PPO
and GTrXL-PPO algorithms failed to converge throughout the training process. Specifically,
the PPO algorithm achieved a maximum reward of 11.3 during training, while the GTrXL-
PPO algorithm reached a maximum reward of 9.4. In contrast, the SAC algorithm attained
a maximum reward of 33.7 during training, but its final converged value was only around
20. Similarly, the GTrXL-SAC algorithm achieved a maximum reward of 27.7 and ultimately

## Page 22

Drones 2025, 9, 275
22 of 30
converged around 20, with both algorithms being limited by local optima. Notably, during
the entire training process, the GTrXL-SAC algorithm exhibited a rapid increase in reward,
reaching a relatively high reward value after approximately 100 episodes.
(a)
(b)
(c)
Figure 12.
Reward curves for GTrXL-PPO and GTrXL-SAC algorithms with sensor data input:
(a) Environment 1. (b) Environment 2. (c) Environment 3.
Figure 12b illustrates the reward curves of the PPO, GTrXL-PPO, SAC, and GTrXL-
SAC algorithms in Environment 2. Throughout the training process, the maximum reward
achieved by the PPO algorithm was 7.5, while the GTrXL-PPO algorithm reached a max-
imum reward of 14.3. Similar to Environment 1, neither the PPO nor the GTrXL-PPO
algorithm managed to reach convergence during training. The SAC algorithm achieved a
maximum reward of 27.1 during training and converged around a reward of 27. In contrast,
the GTrXL-SAC algorithm reached a maximum reward of 44.3, ultimately converging
around a reward of 44. The SAC algorithm experienced a rapid reward increase between
400 and 450 episodes. However, starting from episode 460, it became trapped in a local
optimum, only converging to a local maximum. In contrast, the GTrXL-SAC algorithm
escaped the local optimum around episode 400, continued to improve its rewards, and
successfully converged.
Figure 12c presents the reward curves of the PPO, GTrXL-PPO, SAC, and GTrXL-SAC
algorithms in Environment 3. Throughout the training process, the maximum reward
achieved by the PPO algorithm was 7.8, while the GTrXL-PPO algorithm reached a maxi-
mum reward of 9.4. Similarly to previous environments, neither the PPO nor the GTrXL-
PPO algorithm achieved convergence during training. The SAC algorithm attained a
maximum reward of 18.68 during training and converged around a reward of 18. However,
starting from episode 550, the SAC algorithm became trapped in a local optimum, only
converging to a suboptimal solution. In contrast, the GTrXL-SAC algorithm achieved a
maximum reward of 52.3 and eventually converged around a reward of 52. Throughout the
training process, the reward values of the GTrXL-SAC algorithm consistently outperformed
those of the SAC algorithm. Between episodes 200 and 300, the reward of the GTrXL-SAC
algorithm rapidly increased and converged around episode 320, with the convergence
value being approximately three times higher than that of the SAC algorithm.
•
Comparison of Testing Results
During testing, the policy is applied without noise, using a deterministic strategy to
guide the UAV’s motion. Based on the training results, the policies learned by the PPO,
GTrXL-PPO, SAC, and GTrXL-SAC algorithms in Environment 3 are selected for testing.
The control stability of the policies is evaluated by comparing the UAV’s flight trajectory,
speed curve, and attitude curve.

## Page 23

Drones 2025, 9, 275
23 of 30
The flight trajectories (sensor data) of the PPO, GTrXL-PPO, SAC, and GTrXL-SAC
algorithms in Environment 3 are shown in Figure 13a. The PPO algorithm fails to provide
adequate guidance, resulting in the UAV not flying toward the target point. The GTrXL-
PPO algorithm is able to guide the UAV toward the target point, but it fails to recognize
the first obstacle and is consistently blocked by it, making it difficult to reach the target.
Both the SAC and GTrXL-SAC algorithms can utilize sensor data to derive strategies that
successfully guide the UAV in completing its flight mission. However, the flight trajectory of
the UAV under the GTrXL-SAC strategy is much smoother. In contrast, the UAV following
the SAC strategy continuously sways left and right throughout the flight, resulting in a
winding trajectory that does not reflect typical UAV flight behavior in real-world scenarios.
This also imposes high maneuverability demands on the UAV. Figure 13b demonstrates the
AirSim-recorded data of the UAV controlled by the GTrXL-SAC algorithm during obstacle
avoidance in Environment 3. The UAV has precisely navigated through four obstacles in
the environment and successfully reached the target destination.
(a)
(b)
Figure 13. (a) Three-dimensional flight trajectories (sensor data) of UAVs controlled by the GTrXL-
PPO and GTrXL-SAC algorithms in Environment 3. (b) AirSim-recorded data (sensor data) of UAVs
controlled by the GTrXL-SAC algorithm during obstacle avoidance in Environment 3.
In Figure 14a, the UAVs guided by the SAC and GTrXL-SAC strategies exhibit a
steadily increasing trajectory along the y-axis, indicating that both UAVs consistently
approach the target point in a stable manner. The flight speed of the UAV using the SAC
strategy is approximately twice that of the UAV using the GTrXL-SAC strategy. The UAV
with the GTrXL-SAC strategy performs no unnecessary maneuvers along the x and z axes,
moving only when it needs to avoid obstacles. In contrast, the UAV with the SAC strategy
often exhibits unnecessary movements along the x and z axes.
In Figure 14b, the flight speed curves of UAVs executing flight decisions with the PPO,
GTrXL-PPO, SAC, and GTrXL-SAC algorithms are shown. From the x-axis speed curve,
it can be seen that, during flight tasks, the flight speed of the UAV using the GTrXL-SAC
algorithm is mostly comparable to that of the UAV using the SAC algorithm, but with
smoother transitions and fewer fluctuations in speed. In the y-axis speed curve, during
the first five steps, the speed trends of the GTrXL-SAC and SAC algorithms are similar,
with both gradually increasing to a maximum value. Afterward, while the SAC algorithm
maintains a constant y-axis speed of 1.8 m/s throughout the task, the GTrXL-SAC algorithm
stabilizes its y-axis speed at 1 m/s. Throughout the entire flight decision-making process,
the GTrXL-SAC algorithm only adjusts the z-axis speed when encountering obstacles.
Comparing the speed curves across all three axes, it is clear that the GTrXL-SAC algorithm

## Page 24

Drones 2025, 9, 275
24 of 30
is able to maintain stable speed while ensuring safe obstacle avoidance, allowing the UAV
to complete the flight task safely and efficiently.
(a)
(b)
(c)
Figure 14. Trajectory, speed, and attitude curves (sensor data) of UAVs controlled by the GTrXL-PPO
and GTrXL-SAC algorithms in Environment 3. (a) Three-axis trajectory curves of the UAV. (b) Speed
curves of the UAV. (c) Euler angle curves (pitch, roll, and yaw) of the UAV.
As observed in Figure 14c, compared to the SAC algorithm, the roll angle curve of
the UAV using the GTrXL-SAC algorithm exhibits smoother changes with fewer sudden
shifts. From the pitch angle curve, it can be seen that, in order to avoid obstacles, the pitch
angle of the GTrXL-SAC algorithm changes only during the first five steps, remaining more
stable with fewer fluctuations compared to the SAC algorithm. In the yaw angle curve, it is
evident that the GTrXL-SAC algorithm maintains forward flight throughout, with the UAV
continuously facing the target, leading to higher task completion efficiency.
The PPO algorithm is an on-policy method that suffers from low sample efficiency,
making it difficult to train effectively. In contrast, SAC is an off-policy algorithm that
specifically addresses the issue of low sample efficiency, allowing it to converge more
easily. Experimental results show that when using simple sensor data as input, the training
reward curve of the PPO algorithm fails to converge. Even when the GTrXL structure is
introduced in GTrXL-PPO, resulting in a slight increase in rewards during some episodes,
it still struggles to converge and fails to successfully complete the flight task. Throughout
the entire training and testing process, the performance of both PPO and GTrXL-PPO is
subpar, falling behind that of the SAC and GTrXL-SAC algorithms.
Moreover, the above results indicate that, compared to the traditional SAC algorithm,
the introduction of the GTrXL structure in GTrXL-SAC leads to significant improvements
in both training speed and control stability.
6.3. Experiment 2: UAV Perception and Control with Multimodal Data as Input
In Experiment 2, multimodal data, which integrate both image and sensor information
as input, are used to compare the convergence performance during training and the flight
performance during testing across the PPO, GTrXL-PPO, SAC, and GTrXL-SAC algorithms.
•
Comparison of Training Speeds
To assess the impact of incorporating multimodal image information on algorithm
performance, experiments were conducted using the same hyperparameters as in Exper-
iment 1, with an initial learning rate of 0.0006. Figure 15 displays the reward curves
obtained from training across three environments. It can be observed that, compared to
using single-sensor information, the inclusion of image data significantly enhances the
convergence performance of the algorithms. Specifically, in Figure 15a, the introduction

## Page 25

Drones 2025, 9, 275
25 of 30
of image information enables the PPO algorithm to begin optimizing the policy and to
achieve higher rewards in Environment 1. However, in all three environments, neither the
PPO nor the GTrXL-PPO algorithms were able to reach convergence.
(a)
(b)
(c)
Figure 15. Reward curves for GTrXL-PPO and GTrXL-SAC algorithms with multimodal data input:
(a) Environment 1. (b) Environment 2. (c) Environment 3.
In all three environments, the SAC algorithm exhibited a strong convergence trend,
consistently increasing and eventually converging to a reward value of approximately 50
between the 700th and 800th episodes, successfully completing the task. However, under
the current hyperparameters and experimental setup, the GTrXL-SAC algorithm achieved
rapid growth earlier than SAC, with rewards quickly increasing to 20 around the 150th
episode during the early stages of training. However, the network subsequently became
trapped in a local optimum and failed to improve further. Upon analysis, it is suspected
that the current hyperparameter settings or training configuration caused the model with
GTrXL to prematurely stop learning, leading to early convergence. As seen in Figure 15c,
the reward for the GTrXL-SAC algorithm briefly peaked at 52 around the 190th episode,
but then stagnated in a local optimum. This may have been due to an overly high learning
rate, which caused the model parameters to skip over the optimal solution during training,
ultimately preventing the model from converging.
In particular, the reward function of the GTrXL-SAC algorithm exhibited noticeable
fluctuations, which aligns with the characteristic of unstable gradients during the early
stages of training caused by an excessively high learning rate. Therefore, it was considered
beneficial to reduce the learning rate to make the model’s weight updates more stable, with
the aim of improving the training process. The learning rates for both the GTrXL-PPO and
GTrXL-SAC algorithms were adjusted to 0.0001 and were gradually decayed as the number
of episodes increased.
The convergence curves of the algorithms after adjusting the learning rate in Envi-
ronment 1 are shown in Figure 16a. From the figure, it can be observed that, compared
to using sensor data, the PPO algorithm performs better in terms of convergence when
multimodal data are used as input, gradually exploring the policy in the desired direction.
Additionally, the GTrXL-PPO algorithm demonstrates faster convergence and ultimately
achieves a higher reward value compared to the traditional PPO algorithm. Specifically,
the PPO algorithm’s reward converged to 17, while the GTrXL-PPO algorithm’s reward
converged to 21, indicating superior performance. Unfortunately, neither algorithm was
able to discover the optimal policy. In contrast, the SAC algorithm converged at episode 768,
with a reward value of 48.3 and a maximum reward of 51.92. The GTrXL-SAC algorithm
converged even earlier, at episode 557, with a reward value of 51.5. In terms of convergence
speed, the GTrXL-SAC algorithm improved the convergence rate by 21.1% compared to the
SAC algorithm in Environment 1.

## Page 26

Drones 2025, 9, 275
26 of 30
(a)
(b)
(c)
Figure 16.
Reward curves for GTrXL-PPO and GTrXL-SAC algorithms with multimodal data input:
(a) Environment 1. (b) Environment 2. (c) Environment 3.
The convergence curves of the algorithms after adjusting the learning rate in En-
vironment 2 are shown in Figure 16b. In Environment 2, the PPO algorithm failed to
effectively explore in the right direction within 1000 episodes, while the GTrXL-PPO algo-
rithm, although exploring in the correct direction, was not able to learn effectively. The
SAC algorithm converged at episode 863, with a reward value of 49.5 and a maximum
reward of 50.7. In contrast, the GTrXL-SAC algorithm converged earlier, at episode 630,
with a reward value of 51.2. In terms of convergence speed, the GTrXL-SAC algorithm
improved the convergence rate by 23.3% compared to the SAC algorithm in Environment 2.
The convergence curve of the algorithm in Environment 3 is shown in Figure 16c. In
Environment 3, the performance of the PPO and GTrXL-PPO algorithms is similar to that
observed in Environment 2. The SAC algorithm converges at episode 763, with the reward
value converging to 51, and the maximum reward being 52.7. In contrast, the GTrXL-SAC
algorithm converges at episode 577, with the reward value converging to 51.8. In terms of
convergence speed, the GTrXL-SAC algorithm demonstrates an 18.6% improvement over
the SAC algorithm in Environment 3.
•
Comparison of Testing Results
During the testing phase, the optimal strategies (network parameters corresponding
to the maximum reward) obtained by each algorithm in Environment 2 were compared.
The stability of these strategies in guiding the UAV’s flight was then evaluated in terms of
flight trajectory, speed, and attitude. As observed in Figure 17a both the PPO and GTrXL-
PPO algorithms encountered collisions with the third obstacle during training, failing
to successfully navigate past it. However, compared to the PPO algorithm, the strategy
learned by the GTrXL-PPO algorithm was more stable during the UAV’s flight, avoiding
excessive swaying. The strategies trained by both the SAC and GTrXL-SAC algorithms
successfully guided the UAV over the obstacles and to the target point, completing the flight
task. Despite the larger decision steps of the GTrXL-SAC algorithm, its flight trajectory
was smoother, with sharp turns only occurring when encountering obstacles. Figure 17b
demonstrates the AirSim-recorded data of the UAV controlled by the GTrXL-SAC algorithm
during obstacle avoidance in Environment 3. The UAV has precisely navigated through
four obstacles in the environment and successfully reached the target destination.
As observed from Figure 18, in terms of UAV control stability, GTrXL-SAC outperforms
the others, followed by GTrXL-PPO, while SAC and PPO exhibit relatively lower stability.
This suggests that by incorporating the GTrXL architecture, the agent is able to make
joint decisions based on both historical and current information, allowing it to detect
obstacles earlier and adjust its actions in advance, thus avoiding sharp changes in speed and

## Page 27

Drones 2025, 9, 275
27 of 30
attitude. Both the GTrXL-PPO and GTrXL-SAC algorithms show significant improvements
in training speed and control stability.
(a)
(b)
Figure 17. (a) Three-dimensional flight trajectories (multimodal data) of UAVs controlled by the
GTrXL-PPO and GTrXL-SAC algorithms in Environment 2. (b) AirSim recorded data (multimodal
data) of UAVs controlled by the GTrXL-SAC algorithm during obstacle avoidance in Environment 2.
(a)
(b)
(c)
Figure 18. Trajectory, speed, and attitude curves (multimodal data) of UAVs controlled by the GTrXL-
PPO and GTrXL-SAC algorithms in Environment 2. (a) Three-axis trajectory curves of the UAV.
(b) Speed curves of the UAV. (c) Euler angle curves (pitch, roll, and yaw) of the UAV.
From the results of Experiment 1 and Experiment 2, it is evident that the on-policy
PPO algorithm is not suitable for the UAV control problem discussed in this paper, which
involves navigating through a narrow corridor. The PPO algorithm performs poorly in
terms of sample efficiency, and the update of the policy is highly dependent on the currently
available samples. If, during training, decision samples with high rewards (defined in this
paper as successfully passing an obstacle) are not obtained, then the policy will struggle
to train effectively. Although the GTrXL-PPO algorithm, which incorporates the GTrXL
architecture, shows some improvement in training and testing performance compared to
PPO, it is still constrained by the characteristics of the PPO algorithm. As a result, it fails to
converge and is unable to successfully guide the UAV to complete the task.
The SAC algorithm, as an off-policy algorithm, is well-suited for the UAV control prob-
lem addressed in this paper. It is capable of converging quickly and successfully guiding
the UAV to complete the designated flight tasks. The introduction of the GTrXL architecture
in the GTrXL-SAC algorithm results in significant improvements in both training speed
and control stability. Compared to the SAC algorithm, the GTrXL-SAC algorithm achieves

## Page 28

Drones 2025, 9, 275
28 of 30
approximately a 20% increase in training speed while also demonstrating greater stability
in the policy. It is able to identify obstacles earlier and adjust speed and posture in advance,
thereby avoiding issues such as sudden speed changes and large oscillations in posture.
Furthermore, through separate experiments on sensor data and multimodal data, the
superiority of multimodal data in agent training was further validated. The results show
that multimodal data provide the agent with more comprehensive and rich information,
leading to faster convergence during RL training and making it less likely to get trapped
in local optima. This underscores the importance of considering multiple data sources in
order to enhance system performance and robustness in UAV control tasks. In summary,
the GTrXL-SAC algorithm demonstrates significant improvements in both training speed
and control stability, offering strong support for its application in specific environments.
7. Conclusions and Future Work
UAVs, owing to their inherent versatility and operational flexibility, have garnered
extensive utilization across diverse industrial and civilian domains. A critical challenge in
contemporary UAV research lies in the realization of fully autonomous control and naviga-
tion capabilities. This study specifically addresses UAV maneuverability within confined
corridor environments and investigates DRL-based methodologies for autonomous percep-
tion and control systems. The principal contributions and findings of this investigation are
delineated as follows.
To address the limitations of oversimplified UAV modeling in current research, this
investigation employs a quadrotor UAV platform to establish an autonomous perception
and decision-making control framework through DRL. The UAV’s flight operations are
formally formulated as a POMDP, with rigorous mathematical definitions of state space,
action space, and reward function. The proposed model processes multimodal sensory in-
puts to generate velocity commands that actuate a high-fidelity six-degree-of-freedom UAV
simulation model, incorporating comprehensive kinematic and dynamic characteristics
for maneuverability analysis. Implementation employs both on-policy PPO and off-policy
SAC reinforcement learning algorithms. Experimental validation in constrained corridor
environments demonstrates that the PPO algorithm exhibits suboptimal performance in
acquiring high-value training samples and policy optimization, while the SAC algorithm
demonstrates superior suitability through rapid exploration capability and effective policy
refinement, enabling successful mission completion. Furthermore, comparative analysis
reveals that multimodal data integration significantly enhances agent perception through
richer information representation, thereby accelerating algorithm convergence compared
to unimodal sensor input configurations.
To address the challenge of long-term temporal dependencies in UAV decision-making
processes under conventional DRL frameworks, this study presents a novel integration
of DRL with Transformer architecture through the proposed GTrXL-SAC algorithm. The
methodology initiates with positional encoding of multimodal inputs, subsequently em-
ploying GTrXL’s self-attention mechanism to establish inter-sequence correlations within
multimodal data streams, thereby substantially improving obstacle recognition precision.
Furthermore, the architecture capitalizes on GTrXL’s memory retention capabilities to syn-
thesize UAV control decisions through synergistic analysis of historical operational patterns
and real-time environmental states. Experimental validation demonstrates that the GTrXL-
PPO variant achieves enhanced policy exploration accuracy compared to baseline PPO
implementations, though constrained by suboptimal sample efficiency and convergence
rates. Comparatively, the GTrXL-SAC algorithm exhibits a 20% acceleration in convergence
speed relative to conventional SAC approaches. Flight performance evaluations reveal the
GTrXL-SAC framework’s superior command over UAV velocity and attitude parameters,

## Page 29

Drones 2025, 9, 275
29 of 30
resulting in enhanced flight stability compared to GTrXL-PPO implementations during
complex navigation tasks.
Author Contributions: Conceptualization, J.H.; Methodology, J.H. and Y.C.; Software, Y.C.; Valida-
tion, J.H.; Formal analysis, G.X.; Investigation, E.N.; Resources, B.L.; Writing—original draft, J.H.;
Writing—review & editing, S.B.; Supervision, B.L. and G.W. All authors have read and agreed to the
published version of the manuscript.
Funding: This research was funded by the Key Research and Development Program of Shaanxi
Province (Grant No. 2023-GHZD-33), the Open Project of the State Key Laboratory of Intelligent Game
(Grant No. ZBKF-23-05), and the National Nature Science Foundation of China (Grant No. 62003267).
Data Availability Statement: The original contributions presented in this study are included in the
article material. Further inquiries can be directed to the corresponding author.
Acknowledgments: We are grateful to our colleagues for their valuable feedback and constructive
discussions that enriched this study.
Conflicts of Interest: The authors declare no conflicts of interest.
References
1.
Federal Aviation Administration; U.S. Department of Transportation. FAA Aerospace Forecast: Fiscal Years 2024–2044. 2024.
Available online: https://www.faa.gov (accessed on 2 November 2024).
2.
Gohari, A.; Ahmad, A.B.; Rahim, R.B.A.; Supa’at, A.S.M.; Razak, S.A.; Gismalla, M.S.M. Involvement of Surveillance Drones in
Smart Cities: A Systematic Review. IEEE Access 2022, 10, 56611–56628. [CrossRef]
3.
Zhang, C.; Kovacs, J.M. The application of small unmanned aerial systems for precision agriculture: A review. Precision Agric.
2012, 13, 693–712.
4.
Osorio Quero, C.; Martinez-Carranza, J. Unmanned aerial systems in search and rescue: A global perspective on current challenges
and future applications. Int. J. Disaster Risk Reduct. 2025, 118, 105199. [CrossRef]
5.
Xiao, Z.W.; Fu, X.W. A Cooperative Detection Game: UAV Swarm vs. One Fast Intruder. J. Syst. Eng. Electron. 2023, 34, 1565–1575.
6.
Li, B.; Wang, J.; Song, C.; Yang, Z.; Wan, K.; Zhang, Q. Multi-UAV roundup strategy method based on deep reinforcement learning
CEL-MADDPG algorithm. Expert Syst. Appl. 2024, 245, 123018. [CrossRef]
7.
Xu, Q.; Yi, J.; Wang, X.; Niu, M.-B.; Miah, M.S.; Wang, L. Secure Unmanned Aerial Vehicle Communication in Dual-Function
Radar Communication System by Exploiting Constructive Interference. Drones 2024, 8, 581. [CrossRef]
8.
AlMahamid, F.; Grolinger, K. Autonomous Unmanned Aerial Vehicle navigation using Reinforcement Learning: A systematic
review. Eng. Appl. Artif. Intell. 2022, 115, 105321.
9.
Wu, J.H.; Ye, Y.; Du, J. Multi-objective reinforcement learning for autonomous drone navigation in urban areas with wind zones.
Autom. Constr. 2024, 158, 105253.
10.
Fu, X.W.; Zhu, J.D.; Wei, Z.Y.; Wang, H.; Li, S.L. A UAV Pursuit-Evasion Strategy Based on DDPG and Imitation Learning. Int. J.
Aerosp. Eng. 2022, 2022, 3139610.
11.
Russell, S.J.; Norvig, P. Artificial Intelligence: A Modern Approach, 4th ed.; Pearson: London, UK, 2020.
12.
Chalapathy, R.; Chawla, S. Deep Learning for Anomaly Detection: A Survey. arXiv 2019, arXiv:1901.03407.
13.
Caballero-Martin, D.; Lopez-Guede, J.M.; Estevez, J.; Graña, M. Artificial Intelligence Applied to Drone Control: A State of the
Art. Drones 2024, 8, 296. [CrossRef]
14.
Arulkumaran, K.; Deisenroth, M.P.; Brundage, M.; Bharath, A.A. Deep Reinforcement Learning: A Brief Survey. IEEE Signal
Process. Mag. 2017, 34, 26–38. [CrossRef]
15.
Hochreiter, S.; Schmidhuber, J. Long Short-Term Memory. Neural Comput. 1997, 9, 1735–1780. [CrossRef] [PubMed]
16.
Vaswani, A.; Shazeer, N.; Parmar, N.; Uszkoreit, J.; Jones, L.; Gomez, A.N.; Kaiser, L.; Polosukhin, I. Attention Is All You Need.
arXiv 2024, arXiv:1706.03762.
17.
Roberge, V.; Tarbouchi, M.; Labonté, G. Fast genetic algorithm path planner for fixed-wing military UAV using GPU. IEEE Trans.
Aerosp. Electron. Syst. 2018, 54, 2105–2117. [CrossRef]
18.
Chen, J.; Ye, F.; Jiang, T. Path planning under obstacle-avoidance constraints based on ant colony optimization algorithm.
In Proceedings of the 2017 IEEE 17th International Conference on Communication Technology (ICCT), Chengdu, China, 27–30
October 2017; pp. 1434–1438.
19.
Liu, Y.; Zhang, X.; Guan, X.; Delahaye, D. Adaptive sensitivity decision based path planning algorithm for unmanned aerial
vehicle with improved particle swarm optimization. Aerosp. Sci. Technol. 2016, 58, 92–102. [CrossRef]

## Page 30

Drones 2025, 9, 275
30 of 30
20.
Zhang, X.; Lu, X.; Jia, S.; Li, X.Z. A novel phase angle-encoded fruit fly optimization algorithm with mutation adaptation
mechanism applied to UAV path planning. Appl. Soft Comput. 2018, 70, 371–388.
21.
Chen, Y.B.; Mei, Y.S.; Yu, J.Q.; Su, X.L.; Xu, N. Three-dimensional unmanned aerial vehicle path planning using modified wolf
pack search algorithm. Neurocomputing 2017, 266, 445–457.
22.
Zhang, D.Q.; Xian, Y.; Li, J.; Lei, G.; Chang, Y. UAV path planning based on chaos ant colony algorithm. In Proceedings of the
IEEE 2015 International Conference on Computer Science and Mechanical Automation (CSMA), Hangzhou, China, 23–25 October
2015; pp. 81–85.
23.
Yan, C.; Xiang, X. A path planning algorithm for uav based on improved q-learning. In Proceedings of the IEEE 2018 2nd
International Conference on Robotics and Automation Sciences (ICRAS), Wuhan, China, 23–25 June 2018; pp. 1–5.
24.
Menfoukh, K.; Touba, M.M.; KhenfriI, F.; Guettal, L. Optimized Convolutional Neural Network architecture for UAV navigation
within unstructured trail. In Proceedings of the IEEE 2020 1st International Conference on Communications, Control Systems and
Signal Processing (CCSSP), El Oued, Algeria, 16–17 May 2020; pp. 211–214.
25.
Back, S.; Cho, G.; Oh, J.; Tran, X.T.; Oh, H. Autonomous UAV trail navigation with obstacle avoidance using deep neural networks.
J. Intell. Robot. Syst. 2020, 100, 1195–1211.
26.
Maciel-Pearson, B.G.; Carbonneau, P.; Breckon, T.P. Extending deep neural network trail navigation for unmanned aerial vehicle
operation within the forest canopy. In Proceedings of the 19th Annual Conference Towards Autonomous Robotic Systems, Bristol,
UK, 25–27 July 2018; Springer International Publishing: Cham, Switzerland, 2018; pp. 147–158.
27.
Chhikara, P.; Tekchandani, R.; Kumar, N.; Chamola, V.; Guizani, M. DCNN-GA: A deep neural net architecture for navigation of
UAV in indoor environment. IEEE Internet Things J. 2020, 8, 4448–4460.
28.
Doukhi, O.; Lee, D.J. Deep reinforcement learning for autonomous map-less navigation of a flying robot. IEEE Access 2022,
10, 82964–82976.
29.
Bouhamed, O.; Ghazzai, H.; Besbes, H.; Massoud, Y. Autonomous UAV navigation: A DDPG-based deep reinforcement
learning approach. In Proceedings of the 2020 IEEE International Symposium on circuits and systems (ISCAS), Sevilla, Spain,
10–21 October 2020; pp. 1–5.
30.
He, L.; Aouf, N.; Whidborne, J.F.; Song, B.F. Deep reinforcement learning based local planner for UAV obstacle avoidance using
demonstration data. arXiv 2020, arXiv:2008.02521.
31.
Liu, C.H.; Ma, X.X.; Gao, X.D.; Tang, J. Distributed energy-efficient multi-UAV navigation for long-term communication coverage
by deep reinforcement learning. IEEE Trans. Mob. Comput. 2019, 19, 1274–1285.
32.
Mellinger, D.; Kumar, V. Minimum snap trajectory generation and control for quadrotors. In Proceedings of the 2011 IEEE
International Conference on Robotics and Automation, Shanghai, China, 9–13 May 2011; pp. 2520–2525. [CrossRef]
33.
Daniel, M. Trajectory Generation and Control for Quadrotors; University of Pennsylvania: Philadelphia, PA, USA, 2012.
34.
Zhang, Y.J.; Huang, Y.J.; Liang, K.; Cao, K.; Wang, Y.F.; Liu, X.C.; Guo Y.Z.; Wang, J.Z. High-precision modeling and collision
simulation of small rotor UAV. Aerosp. Sci. Technol. 2021, 118, 106977.
35.
Deverett, B.; Faulkner, R.; Fortunato, M.; Wayne, G.; Leibo, J.Z. Interval timing in deep reinforcement learning agents. arXiv 2024,
arXiv:1905.13469.
36.
Schrittwieser, J.L.; Antonoglou, I.; Hubert, T.; Simonyan, K.; Sifre, L.; Schmitt, S.; Guez, A.; Lockhart, E.; Hassabis, D.; Graepel, T.;
et al. Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model. arXiv 2024, arXiv:1911.08265.
37.
Gupta, S.; Singal, G.; Garg, D. Deep Reinforcement Learning Techniques in Diversified Domains: A Survey. Arch. Computat.
Methods Eng. 2021, 28, 4715–4754. [CrossRef]
38.
Mienye, I.D.; Swart, T.G.; Obaido, G. Recurrent Neural Networks: A Comprehensive Review of Architectures, Variants, and
Applications. Information 2024, 15, 517. [CrossRef]
39.
Shital, S.; Dey, D.; Chris, L.; Ashish, K. AirSim: High-Fidelity Visual and Physical Simulation for Autonomous Vehicles. arXiv
2017, arXiv:1705.05065.
40.
Tuomas, H.; Aurick, Z.; Pieter, A.; Sergey, L. Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a
Stochastic Actor. arXiv 2018, arXiv:1801.01290.
41.
Tuomas, H.; Aurick, Z.; Kristian, H.; George, T.; Sehoon, H.; Jie, T.; Vikash, K.; Henry, Z.; Abhishek, G.; Pieter, A.; et al. Soft
Actor-Critic Algorithms and Applications. arXiv 2018, arXiv:1812.05905.
42.
Parisotto, E.; Song, H.F.; Rae, J.W.; Pascanu, R.; Gulcehre, C.; Jayakumar, S.M.; Jaderberg, M.; Kaufman, R.L.; Clark, A.;
Noury, S.; et al. Stabilizing Transformers for Reinforcement Learning. arXiv 2020, arXiv:1910.06764.
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.
