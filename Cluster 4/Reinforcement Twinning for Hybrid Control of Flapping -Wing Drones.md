# Reinforcement Twinning for Hybrid Control of Flapping -Wing Drones.pdf

## Page 1

Reinforcement Twinning for Hybrid Control of
Flapping-Wing Drones
Romain Poletti1,2 , Lorenzo Schena1,3, Lilla Koloszar1, Joris
Degroote2, and Miguel Alfonso Mendez1,4,5
1 von Karman Institute for Fluid Dynamics, Waterloosesteenweg 72,
Sint-Genesius-Rode, Belgium
2 Department of Electromechanical, Systems and Metal Engineering, Ghent
University, Sint-Pietersnieuwstraat 41, Gent, Belgium
3 Vrije Universiteit Brussel, Pleinlaan 2, Elsene, Brussels, Belgium
4Aero-Thermo-Mechanics Laboratory, ´Ecole Polytechnique de Bruxelles, Universit´e
Libre de Bruxelles, Av. Franklin Roosevelt 50, Brussels, Belgium
5 Aerospace Engineering Research Group, Universidad Carlos III de Madrid, Av. de
la Universidad 30, Legan´es, Spain
E-mail: romain.poletti@vki.ac.be
Abstract.
Controlling the flight of flapping-wing drones requires versatile controllers
that handle their time-varying,
nonlinear,
and underactuated dynamics from
incomplete and noisy sensor data.
Model-based methods struggle with accurate
modeling, while model-free approaches falter in efficiently navigating very high-
dimensional and nonlinear control objective landscapes.
This article presents a
novel hybrid model-free/model-based approach to flight control based on the recently
proposed reinforcement twinning algorithm. The model-based (MB) approach relies on
an adjoint formulation using an adaptive digital twin, continuously identified from live
trajectories, while the model-free (MF) approach relies on reinforcement learning. The
two agents collaborate through transfer learning, imitation learning, and experience
sharing using the real environment, the digital twin and a referee. The latter selects
the best agent to interact with the real environment based on performance within
the digital twin and a real-to-virtual environment consistency ratio. The algorithm
is evaluated for controlling the longitudinal dynamics of a flapping-wing drone, with
the environment simulated as a nonlinear, time-varying dynamical system under the
influence of quasi-steady aerodynamic forces. The hybrid control learning approach is
tested with three types of initialization of the adaptive model: (1) offline identification
using previously available data, (2) random initialization with full online identification,
and (3) offline pre-training with an estimation bias, followed by online adaptation.
In all three scenarios, the proposed hybrid learning approach demonstrates superior
performance compared to purely model-free and model-based methods.
arXiv:2505.18201v1  [cs.RO]  21 May 2025

## Page 2

Reinforcement Twinning for Hybrid Control of Flapping-Wing Drones
2
1. Introduction
Insects and hummingbirds defy gravity with their outstanding flight abilities: they can
hover stably in gusty conditions, take off vertically and perform rapid escape maneuvers.
Inspired by these aerial masters, engineers have designed Flapping Wing Micro Air
Vehicles (FWMAVs) to navigate the tight and hazardous spaces encountered in search,
rescue, and reconnaissance missions. Pioneering work by [1] led to the first successful
hovering flight of a hummingbird-like MAV, followed by various FWMAVs ranging from
centimeter-scale [2, 3] to decimeter-scale designs [4, 5, 6, 7]. Their flight dynamics is
intrinsically unstable, requiring continuous control of wing motion.
While extensive
research has been conducted on FWMAV control [8], state-of-the-art controllers do not
yet allow to replicate the exceptional capabilities of biological flyers [9, 10, 11]. Control
challenges arise from the MAV’s nonlinear dynamics, reliance on unsteady and poorly
understood aerodynamic forces [12], and vulnerability to parametric uncertainties and
sensor noise inherent to small-scale manufacturing [7].
The literature on FWMAV control methods can be broadly classified into traditional
model-based (MB) and model-free (MF) approaches. Model-based control methods use a
model of the FWMAV dynamics. Common control approaches include standard stability
tools (e.g., Routh-Hurwitz criteria and root locus methods [13, 14, 15, 7, 16, 17, 18])
and Linear-Quadratic Regulator (LQR) methods for balancing control performance and
power constraints [19, 20, 21, 22]. These methods were applied to control hovering and
vertical flights using Linear Time Invariant (LTI) models or their approximate analytical
solutions [23, 24].
LTI models are derived from the FWMAV equations of motion by neglecting the
wing dynamics, cycle-averaging the aerodynamic forces, and by linearizing the equations
around a fixed point [8].
Because these simplifications are not valid for wing-beat
frequencies similar to natural body frequencies, complex wing motion parametrization,
and agile maneuvers [8, 25], control using nonlinear formulations of the FWMAV
dynamics have also been explored with pseudo-inverse allocation schemes [26, 27],
model-predictive control (MPC) [28, 29], and central pattern generators [30].
An
extensive review of the model-based strategies applied to flapping-wing flight control
is found in [8, 11].
From a modeling point of view, these MB approaches are static because they
do not model the time-varying uncertainties of flapping-wing prototypes arising from
manufacturing tolerances and electromechanical wear and noise. Adaptive controllers
were proposed to account for manufacturing uncertainties and unmodeled dynamics
using Lyapunov’s direct method in [31, 32] and using an adaptive MPC in [33]. The
approaches mitigate model biases but primarily focus on closed-loop dynamics and the
system’s response to actuation. The authors of Ref. [34] employ the recursive least
squares (RLS) method and an adaptive pole placement control (APPC) scheme to adapt
an LTI system and its controller based on live trajectories of a bird-like drone. However,
this method is limited to linear models and suffers from robustness issues. Furthermore,

## Page 3

Reinforcement Twinning for Hybrid Control of Flapping-Wing Drones
3
many model-based approaches are susceptible to becoming trapped in suboptimal
performance regions, particularly those that rely on gradient-based optimization.
Alternatively, MF approaches operate without prior knowledge of system dynamics,
relying solely on input–output data and trial-and-error exploration [35, 36, 37]. These
methods naturally account for FWMAV uncertainties captured in measurements and
interface well with nonlinear control laws [38].
Two broad categories of MF methods have been applied to FWMAVs. The first
identifies system behavior from data to adaptively tune a controller, including techniques
such as model-free adaptive variable structure control (MFAVSC) [25], incremental
proportional-integral-derivative control (iPID) [39], and fuzzy neural networks (FNN)
[40]. However, these methods often rely on local models, limiting scalability across varied
flight conditions.
The second category uses pure trial-and-error, with reinforcement
learning (RL) [41] being the most widely used approach for biomimicry. For instance,
Deep-Q Learning (DQN) has been used to study the energy advantages of fish schooling
[42, 43], while more recent work applies Proximal Policy Optimization (PPO) with
transformers [44] and Twin Delayed Deep Deterministic Policy Gradient (TD3) [45, 46]
to control wing pitch dynamics.
The first reinforcement learning applications to flapping wings focused on lift
optimization [47, 48, 49].
More recently, [50] utilized the Soft Actor-Critic (SAC)
method to train a bumblebee model to hover in gusty conditions while the authors in
[51, 52] applied Deep Deterministic Policy Gradient (DDPG) to train a hummingbird-
like robot and its digital twin to execute an escape maneuver with remarkable physical
similarity to real hummingbirds. Nevertheless, the application of RL to flight control
remains limited due to its sample inefficiency, requiring extensive trial-and-error with
no guaranteed convergence [52].
More recently, hybrid MB-MF methods have emerged to accelerate the learning
process of model-free approaches using model-based strategies. Among the most popular
hybrid methods, Model-Based Reinforcement Learning (MBRL) has been used in
robotics, with diverse models including artificial neural networks [53], physics-informed
networks [54], and dynamical models derived from first principles [55]. Model-based
policies have been used to warm-start an MF policy [56, 57] and filter out suboptimal
policies [58].
Ref.
[59] introduces a more active form of agent collaboration by
blending a model-free policy update with an approximate model-based one, weighted
by the discrepancy between real and predicted costs. Another hybrid strategy—policy
switching—deploys only the best-performing agent while continuing to train others using
a model. A notable example is the hierarchical Mixtures of Experts (HME) framework
[60, 61], which favors MB policies in regions where MF uncertainty is high.
Within this class of hybrid methods, the authors recently proposed a dual-
agent MBRL framework called Reinforcement Twinning [62]. This approach enables
collaboration between a model-free (MF) and a model-based (MB) agent through
transfer learning, imitation learning, and shared experience. The MB agent synthesizes
control via adjoint-based optimization using a physics-based model that is continuously

## Page 4

Reinforcement Twinning for Hybrid Control of Flapping-Wing Drones
4
updated with real-time data, while the MF agent follows a standard actor-critic
reinforcement learning scheme. This synergy aims to combine the sample efficiency of
MB control with the robustness of MF strategies. In all test cases considered, accurate
model identification was achieved within just a few iterations, making model quality a
key factor in shaping the MB–MF interaction.
This work extends the Reinforcement Twinning framework with two contributions.
First, we consider a scenario where model identification is much more difficult and less
efficient than in the cases presented in [62]. More specifically, in this work we train a
nonlinear model from real-time trajectories generated by an in-house flight simulator
during the controller training. Second, we introduce a new “referee” which enables a
more sophisticated interaction between the MF and MB agent, using a trust ratio that
weights the MB controller performance with the model identification performance. To
the authors’ knowledge, the proposed model and hybrid control methods are novel and
have never been applied to control the flight of flapping-wing drones.
The rest of the article is organized as follows. Section 2 defines the test case that
focuses on a flapping-wing drone executing a take-off and hover maneuver analogously
to hummingbird flights [63]. Section 3 details the reinforcement twinning approach,
including the model-free and model-based methods and their collaboration scheme.
Section 4 defines the simulation environment to which this algorithm is applied, and
Section 5 shows the results of the assimilation and control.
Section 6 discusses the
outcomes and perspectives of this work.
2. Problem definition
The control problem aims to determine the flapping kinematics that generates
aerodynamic forces to optimally steer an FWMAV to the desired position in the shortest
time. The FWMAV is modelled as a spherical body with two semi-elliptical, rigid and
massless wings as in previous works [64, 62, 65] (see Figure 1a). The rigid wings have a
mean chord length c = 1 cm, a span R = 5 cm, a thickness b = 3%c. The spherical body,
also rigid, has a weight mb = 3 g, a radius Rb = c and a moment of inertia I = 1.2e −5
kgm2. The body center serves as the instantaneous center of rotation, with the wing
root lying 2.25 cm away along the spanwise direction.
We focus on the control of the longitudinal dynamics of the drone’s body, which
has three degrees of freedom with respect to the ground frame (xyz)I:
a vertical
translation z (along zI), a horizontal translation x (along xI) and a pitch rotation
angle θ defined between the x-axis of the body frame (xyz)b and the inertial frame.
Assuming symmetric flapping motion with respect to (xz)I, the yaw, roll, and lateral
displacement are all equal to zero, and thus the drone’s trajectory is composed by the
state vectors s = [ ˙x, ˙z, ˙θ, x, z, θ]T. Starting from rest at the origin (s0 = 0), the goal
is to ascend vertically to reach the state ˜s = [0, 0, 0, 0, 1, 0]T as soon as possible and
before the final time T0 = 1.5 s. This final time was inspired by similar maneuvers
of hummingbirds in [63] and this short duration allows for challenging the controller’s

## Page 5

Reinforcement Twinning for Hybrid Control of Flapping-Wing Drones
5
(a)
(b)
Figure 1: (a) Schematic of the flapping-wing drone control problem and (b) focus on
the wing kinematics defined by the flapping angle ϕ and the pitching angle α
training while reducing the computational cost.
The identification of the optimal control law—hereafter referred to as the control
policy proceeds iteratively. In each attempt, control performance is evaluated over a time
interval t ∈[0, T0], defining an episode. Within this episode, a trajectory is recorded,
and the control performance is assessed. Each trajectory consists of Nc = fcT0 samples,
collected at the end of each flapping cycle, occurring at a constant frequency fc. The
time axis for each episode is thus discretized as {tk = k∆t}Nc
k=1 with ∆t = 1/fc and the
trajectory error at the k-th cycle is defined from the cycle-averaged state vector:
ek = sk −˜s
with
sk = fc
Z k/fc
(k−1)/fc
s(t)dt .
(1)
To evaluate the controller performance, the trajectory error is split into velocity
errors evel,k (first three entries of ek), and position errors epos,k (last three entries of ek).
The reward rk is then defined as:
rk(ek) = −||epos,k||2
2 −η||evel,k ◦h(epos,k)||2
2 ,
(2)
where ◦denotes the Hadamard product (entry by entry) and η is a scalar weight. The
function h(epos,k) is designed to cancel the contribution of the velocity error when the
drone is far from the target position and penalizes high velocities when the target is
approaching. This is formulated as a vector of three Gaussian functions with standard
deviations σ = [σx, σz, σθ]:
h(epos,k) = exp

−

epos,k ◦epos,k ◦1
σ2

(3)

## Page 6

Reinforcement Twinning for Hybrid Control of Flapping-Wing Drones
6
where the exponential function here acts on each entry of its power.
To maximize the reward (equation (2)), the drone must continuously adapt its
flapping kinematics, which are defined by three Euler angles, as illustrated in Figure 1.
These angles are: (1) the stroke plane angle β, defined between xb and xs, where (xyz)b
is the body frame and (xyz)s is the stroke frame that establishes the stroke plane (xy)s
in which the wingtip remains constrained; (2) the flapping angle ϕ, measured between
the feathering axis yp and ys; and (3) the pitching angle α, defined between xp and the
chord-normal direction xw of the wing-attached frame (xyz)w (offset in Figure 1b for
clarity purposes).
The flapping angle and the pitching angle follow the same harmonic functions for
both wings:
ϕ(t) = Aϕ cos(2πfct) + Aoff
(4)
α(t) = Aα sin(2πfct)
(5)
where fc = 20 Hz is the frequency for the flapping and pitching motion and Aα = 45◦
is the pitching amplitude. Aϕ and Aoff are the flapping amplitude and mean flapping
angles that form the control actions a = [Aϕ, β, Aoff] with the angle of the stroke plane,
similarly to [66]. Other options are found in [67, 9, 68].
These three control actions are linked to the cycle-averaged state with the clipped
and scaled proportional derivative (PD) policy:
π(ek; wa) =


Aϕ
β
Aoff

= tanh(Waek + b) + 1
2
(amax −amin) + amin
(6)
where Wa ∈R3×6 is the weight matrix, with wa denoting its transformation into a
vector wa ∈R18×1, which, together with the bias vector b ∈R3×1 defines the control
policy. Actions are scaled in the range [amin −amax] with amax = [88◦, 30◦, 0.5◦] and
amin = [50◦, −30◦, −0.5◦], taking inspiration from natural flyers. Compared to similar
works (e.g. [24]), the parametrization (6) includes cross-correlation and bias terms to
increase the policy robustness to both bias and random errors [31, 69].
3. Reinforcement twinning method
The reinforcement twinning (RT) algorithm is used to train the policy defined in
equation (6).
The algorithm was first proposed in Ref.
[62], to which the reader
is referred for more details. We here present a short review focusing on the general
principle (Section 3.1), the algorithms used for the model-free (Section 3.2) and model-
based (Section 3.3) optimization, and finally the cooperation mechanisms between the
two control approaches (Section 3.4).

## Page 7

Reinforcement Twinning for Hybrid Control of Flapping-Wing Drones
7
Real 
environment:
NLTV system
Virtual 
environment:
NLTI system
Replay 
buffer 
Policy referee
Control reward
Adjoint grad
Reference 
trajectory
Data-assimilation
DDPG grad
Model- free 
control
Model- 
based 
control
Control cost
Assimilation
 Cost
Adjoint grad
Replay 
buffer 
Replay 
buffer 
Training 
signal
I/O signal
I/O signals
Critic
2
1
1.a
1.b
3
4
5
6
8
9
10
12
11
6.a
6.b
9’
12.a
12.b
Assimilation buffer
7
Figure 2: Block diagram of the Reinforcement Twinning algorithm hybridizing a model-
free (1.a) and model-based (1.b) policy to train a control agent π (1.) using a virtual
environment (8.) assimilated from live data of the real environment (3.).
3.1. General principle
Figure 2 illustrates the main components of the RT algorithm, labelled (1) to (12).
Two policies are parameterized according to equation (6): a model-free policy, denoted
πmf(ek; wa,mf) (1.a), and a model-based policy, denoted πmb(ek; wa,mb) (1.b). These
policies interact through a referee ((2), see Section 3.4), which determines which of
these interacts with the real environment (3), designating it as the live policy π(ek; wa)
(1). The real environment emulates the drone’s flight dynamics using a nonlinear time-
varying model described in Section 4.1. However, such a model is considered unknown to
the RT algorithm, which can only interact with the environment through its policies and
get feedback from the collected rewards. The check notation is used to identify cycle-
averaged trajectory errors, actions, and rewards collected by the live policy as it interacts
with the real environment. These constitute the transition vectors (ˇek, ˇak, ˇek+1, ˇrk),
stored in the replay buffer DR1 (5) (collecting up to NR1 transitions), while the cycle-
average states and actions are stored in the assimilation buffer DA (7) (collecting up to
NA state-action pairs). These buffers constitute the memory of the RT agent and use
different strategies to define which transition vectors and state-action pairs are to be

## Page 8

Reinforcement Twinning for Hybrid Control of Flapping-Wing Drones
8
Algorithm 1 Reinforcement Twinning (RT) Algorithm
Initialize the algorithm’s weights including the critic (wq), the model-free policy (wa,mf),
the model-based policy (wa,mb), and the closure law (wp).
procedure RT Updates(wq, wa,mf, wp, wmb)
Step 1: Collect Nc transitions into DR1 and Nc state-action pairs into DA as the
live policy π(ˇe; wa) interacts with the real environment for one episode.
Step 2: Update the critic weights wq and policy weights wa,mf using the DDPG
algorithm (6) and mini-batches from DR1.
Step 3: Replay the Ne episodes from DA on the virtual environment, collect the
associated virtual state-action pairs in DR2 and compute the assimilation cost.
Step 4: Update the virtual environment closure law wp using the adjoint-based
data-assimilation loop (9) and state-action pairs in DR2.
Step 5: Collect Nc state-action pairs in DR3 and compute the associated control
cost as the model-based policy π(e; wa,mb) interacts with the virtual environment.
Step 6:
Update the policy weights wa,mb using the adjoint-based data-
assimilation loop (12) and state-action pairs in DR3.
Step 7: Evaluate the best-performing policy, deploy it live, and enable policy
collaboration through the policy referee (2).
end procedure
maintained in memory. The replay buffer DR1 uses a first-in, first-out (FIFO) strategy
while the assimilation buffer DA maintains the Ne = NA/Nc trajectories that maximize
the buffer variance ξ, to retain the most diverse set of state-action pairs.
The buffer variance is computed from the set of trajectory matrices Si ∈RNc×6,
Si = concat(ˇs0, ..., ˇsNc) with i ∈[1, Ne] and the concat operator that horizontally stacks
the trajectory states:
ξ =
1
NA
Ne
X
i=1
Tr((S −Si)(S −Si)T) ,
(7)
where S = 1/Ne
PNe
i=1 Si is the average trajectory matrix and Tr denotes the trace
operator. The importance of having a diverse set of state-action pairs is evaluated in
Section 5 where the variance maximization criteria are compared with the minimal error
criteria according to which the trajectories retained in the buffer are those minimizing
the errors with the target trajectories.
After each episode, these buffers are used by two optimisation loops. A subset
of the transitions from the replay buffer DR1 are sampled to train the model-free
policy (1.a) using the optimisation loop (6) described in 3.2.
The Ne trajectories
from the assimilation buffer DA are sampled to train a simplified model of the real
environment, which serves as a virtual environment (8) to train the model-based policy
(1.b). The simplified model in the virtual environment is based on a computationally
cheap nonlinear time-invariant model (Section 4.2), and its training leverages an adjoint-
based data-assimilation loop (9, Section 3.3) using the replay buffer DR2 (10). The

## Page 9

Reinforcement Twinning for Hybrid Control of Flapping-Wing Drones
9
model training consists in identifying a closure law p = g(s; wp) that predicts some
unknown parameters p in the model.
The model-based policy is derived from the
virtual environment using a second adjoint-based optimization loop (12, Section 3.3)
and a third replay buffer DR3 (11).
In summary, the reinforcement twinning algorithm consists of training in real time
a virtual environment of an unknown environment, using solely input-output data, while
at the same time training a model-free and a model-based control policy that interact via
a policy referee, a set of memory buffers, and the virtual environment itself. Algorithm
1 gives the pseudocode of the algorithm. The following subsections detail the training
of the virtual environment and the two control agents, along with the policy referee
governing their interaction.
3.2. Model-free policy updates
After the interaction of the live policy with the real environment (Step 1 of algorithm
1), the optimization loop (6 in Figure 2) trains the model-free policy to maximize the
cumulative reward in the real environment. This is defined as:
ˇRa =
Nc−1
X
k=0
ˇrk(ˇek, ˇak),
(8)
where ˇrk is the instantaneous reward computed from equation (2).
This loop is based on the classic Deep Deterministic Policy Gradient (DDPG)
reinforcement learning algorithm. This is an off-policy actor-critic approach proposed
in [70]. The algorithm drives the policy update with the help of a critic neural network
q(sk, wmf; wq) (6.a on Figure 2) estimating the action-value function, also known as the
Q value. The latter defines the expected reward from a given state while following a
certain policy [41]. In this work, the critic network (or, in short, the q-network) consists
of 2 internal layers of 256 neurons with RELU activation functions, characterized by a
set of weights wq. This network is trained to minimize the mean squared Bellman error
(MSBE) using mini-batches randomly sampled from the replay buffer DR1 and a target
critic network characterized by weights wq′ (see [70] for more details).
The target network has the same topology as the critic network, with its weights
wq′ updated following the soft update wq′ = ζwq +(1−ζ)wq′, with ζ a small parameter
to promote learning stability [70]. The gradient of the critic network is used to compute
the gradient of the reward function with respect to the weights ((6.b) in Figure 2), which
is driving the training of the model-free policy:
∂Ra
∂wa,mf
= E∼DR1
∂q(ˇe, ˇa; wq)
∂ˇa
∂πmf(ˇe; ˇa)
∂wa,mf

,
(9)
where the expectation E indicates an average performed on the mini-batch. Compared
to the original DDPG formulation [70], the critic wq and actor weights wa are updated
nq and na times after each episode in the real environment to keep the parallelism with

## Page 10

Reinforcement Twinning for Hybrid Control of Flapping-Wing Drones
10
the model-based approach. In Algorithm 1, the update of both the critic network and
the model-free policy are carried out in Step 2.
3.3. Model-based policy updates
After the model-free optimization loop (Step 2 of algorithm 1), two model-based
optimisation loops are run to (1) learn the closure law of the virtual environment ((9)
on Figure 2) and (2) train the policy πmb(e; wa,mb) based on this model ((12) on Figure
2). These are Steps 3 to 6 in Algorithm 1.
Both optimization problems aim to find the parameters, wp for the closure and
wa,mb for the model-based policy, that minimizes their respective cost functions, Jp and
Ja. The virtual environment training is based on the Ne episodes (trajectories) saved
in the assimilation buffer DA. The real actions are sampled from DA to replay the Ne
episodes in the virtual environment in Step 3. The virtual states-action pairs (sk, ak)
are saved in the replay buffer DR2 and the assimilation cost is calculated by averaging
over the Ne trajectories:
Jp(s, ˇs, wp) = E∼DA
(Z T0
0
h
(s(t) −ˇs(t))2 + αp||wp||2
i
dt
)
,
(10)
where the first term is the mean squared error between the real states ˇs(t) saved in
DA and the virtual states s(t) while the second term penalizes large weights, hence
promoting a robust model across diverse flight trajectories [64].
The cost function
is minimised using the gradients ∂Jp/∂wp computed with the continuous adjoint
method. The motivation for formulating the adjoint problem in its continuous form
(and consequently the cost functions) is to preserve flexibility in choosing numerical
schemes for forward and backward integration.
For each episode, a terminal value
problem is solved for the associated adjoint state λp using the states-action pairs of DR2
on the same temporal grid:
( ˙λp
= −∂f
∂s
Tλp −∂Jp
∂s
T
λp(T0)
= 0 .
(11)
where f(s, a, wp) is the flow map of the virtual environment defined in Section 4.2. The
partial derivatives ∂f/∂s and ∂Jp/∂s are computed using symbolic computation, taking
advantage of the simple analytical expression from the model. The cost gradients with
respect to wp is finally computed as:
dJp
dwp
= E∼DA
n Z To
0
h
λT
p
∂f
∂wp
+ ∂Jp
∂wp
i
dt
o
,
(12)
where the expectation involves averaging over the Ne episodes in the buffer.
This
gradient updates the model parameters using the ADAM optimizer [71], running for
ng iterations. This constitutes Step 4 of the Algorithm. At the end of these, the model
is considered sufficiently accurate to be used to update the model-based policy. A virtual

## Page 11

Reinforcement Twinning for Hybrid Control of Flapping-Wing Drones
11
episode is then run with the current best model-based policy πmb(e, wmb). The states-
action pairs are saved in the replay buffer DR3 and the control cost is computed using
the continuous formulation of the cumulative reward (equation (8)):
Ja(s, ˜s, wa,mb) =
Z T0
0
r(t)dt.
(13)
This computation is carried out in Step 5 of the algorithm. Finally, as for the
assimilation, the adjoint equations are solved to compute the gradient cost:
∂Ja
∂wa,mb
=
Z To
0
λT
a
∂f
∂a
∂πmb
∂wa,mb
dt ,
with
( ˙λa
= −∂f
∂s
Tλa −Ja
∂s
T
λa(T0)
= 0 ,
(14)
This is used to run nmb iterations of ADAM optimizer to update policy weights
wa,mb. This is Step 6 of the algorithm.
3.4. The learning feedback between model-free and model-based
Following the updates of πmf (Step 2) and πmb (Step 6), a policy referee governs the
policy interaction as shown in Figure 3 with labels (1) to (8).
The model-free and
model-based policy (1) first interacts with the virtual environment (2) for one episode
to compute the associated control costs (equation (13)). The costs are designated as live
Ja,live and idle Ja,idle depending on the type of live policy that is held in the digital signal
p (3). The latter is 1 if the model-free policy has interacted with the real environment
(Step 1) and zero otherwise. Live and idle costs are used by three distinct cooperation
mechanisms labeled (4), (5) and (6) in Figure 3.
In the left branch (4), inspired by surrogate modelling [72] or trust region
optimization methods [73], a real-to-virtual environment trust ratio (RVET in 4.a) is
computed based on the live policy cost in the virtual environment Ja,live and in the real
environment ˇ
Ja,live for two successive episodes i −1 and i:
RVETi = ( ˇ
J a,i −ˇ
J a,i−1)
(J a,i −J a,i−1) = ∆ˇ
J a
∆J a
,
(15)
where the live subscript has been omitted for brevity and the · notation indicates a
moving average applied on the cost function of the real and virtual environment. This
allows for capturing a general trend of the cost evolution over the training episodes. The
RVET assesses the consistency of the virtual environment with the real environment
and thus the reliability of evaluating the policy performance from virtual episodes. The
RVET must exceed a threshold RVETl to ensure that a decrease/increase in control
cost in the virtual environment results in a decrease/increase in the real environment
and must be below RVETu to ensure sufficient environment similarity.
A comparator (4.b) verifies these conditions; if either fails, a consistency check
is performed (4.c and 4.d). Counter (4.c) increases for each episode in which RVET

## Page 12

Reinforcement Twinning for Hybrid Control of Flapping-Wing Drones
12
EN
Counter
MET fail
signal
Policy switch 
signal
RES
Consistency 
check
Comparator
Weight 
cloning
Virtual environment
NOT
Comp-
arator
NOT
XOR
OR
SW
SW
EN
mf to
mb
OR
Policy 
cloning
Policy 
switch
Trust 
ratio
Live/idle 
router
1
a
Counter
RES
Comparator
Counter
RES
Comparator
Digital signal
Analog signal
Enable
Reset
RES
EN
SW
Switch
SW
Policy type
b
c
d
b
c
a
c
b
a
1
8
2
3
4
5
6
7
Figure 3: Block diagram of the policy referee showing the cooperation mechanisms
between the model-based and model-free policy used to define the live policy
falls outside the range defined by RVETl and RVETu. When the counter exceeds the
threshold CM (comparator (d)), an RVET fail signal is triggered. The signal is input
into the policy switch block (7), forcing the model-free policy to become live.
The
underlying idea is to rely solely on the model-free policy if the virtual environment is
not sufficiently reliable. In this condition, the training of the model-based policy πmb
is also paused until the model predictions are again considered sufficiently reliable in
accordance with the RVET test.
In the central branch of Figure 3, the referee compares the live and idle costs using
the threshold TJ (5.a). If the live policy consistently underperforms the idle policy
for Cπ episodes, a policy switch signal is raised ((5.b) and (5.c)). The latter signal
inverts the type of policy p by passing through an XOR gate. The XOR output, ORed
with the RVET fail signal, toggles the switch from the switch policy block (i.e. the
previously idle policy becomes live). This second mechanism allows the live policy to

## Page 13

Reinforcement Twinning for Hybrid Control of Flapping-Wing Drones
13
select the better-performing policy, and the consistency check prevents premature policy
switching.
In the right branch, a comparator (6.a) checks if the normalized weight update dwa
of the idle policy is below the threshold Tw (which suggests that the policy learning is
stuck in local minima) or if the live policy strongly and consistently outperforms the idle
policy (using threshold TJi). Following a consistency check ((6.b) and (6.c)), a weight
cloning signal is triggered. This cloning signal, ORed with the RVET signal, is then
used in block (8) to clone weights between policies (model-based to model-free or vice
versa depending on the type of live policy p). This third mechanism allows the referee
to rescue the idle policy if this is stuck at a local minimum; it prevents policy divergence
and facilitates swift exploration of high-performing action spaces.
The three cooperation mechanisms facilitate collaboration between model-free and
model-based policies. In addition, the second mechanism enables indirect collaboration
through the exchange of experiences between policies. When the model-based policy
performs best and interacts with the real environment, its transitions are stored in the
replay buffer DR1 and used to guide updates for the model-free policy. These state-action
spaces contribute to improving the training of both critics and model-free policies within
the reinforcement learning framework (Section 3.2).
Similarly, when the model-free
policy interacts with the environment, its trajectories can be stored in the assimilation
buffer to refine the quality of transitions and, in turn, improve the predictive capability
of the virtual environment.
4. Model definition
4.1. The real environment: The NLTV system
The real environment emulates the flight dynamics of the flapping-wing drone defined
in Section 2.
To simplify its multibody equations of motion [74, 75], the dynamics
of the wings is neglected. This reduces the equations to those of a standard aircraft
subjected to external wing forces, body forces, and gravity applied at the barycenter
[76]. This simplification is common in control and stability analyses [8]. Focusing on
the longitudinal dynamics, the Newton-Euler equations can be formulated in the body
frame:


¨xb
¨zb
¨θb

=


F b
x/mb
F b
z /mb
T b
y/mb

+


−g sin(θb) −˙θb ˙zb
g cos(θb) + ˙θb ˙xb
0

,
(16)
where (F b
x,w, F b
z,w, T b
y) are the aerodynamic loads in the body frame (denoted by
the superscript b), calculated at each instant of the wingbeat cycle, making the
nonlinear system (16) time-varying (NLTV). The derivative of the system state sb =
[ ˙xb, ˙zb, ˙θb, xb, zb, θb] allows equation (16) to be written in the compact form:

## Page 14

Reinforcement Twinning for Hybrid Control of Flapping-Wing Drones
14
dsb
dt = g1(sb, a, t) + g2(sb),
(17)
where g1 is the time-varying vector that gathers the aerodynamic forces and g2 gathers
the remaining terms.
Forces are estimated based on the quasi-steady aerodynamic model [77] that
decomposes the total force into four independent contributions. Only one component is
retained in this work as it outweighs the other three when the wing kinematics is smooth
(equations (4) and (5)). This contribution captures the influence of the leading-edge
vortex (LEV) that stably attaches on the leeward side of the wing when the wing flaps
at high angles of attack [78]. Leveraging the blade element method, the lift L(t) and
the drag D(t) are formulated as:
"
L(t)
D(t)
#
= 1
2ρ
"
CL(αe)
CD(αe)
# Z ∆R+R
∆R
||Uw(t, r)||2
2c(r)dr,
(18)
where ρ is the density and where Lw(t) is perpendicular to Dw(t) which is aligned with
the relative velocity between the drone and the air Uw. The latter sums up the flapping
velocity of the wing and the pitching and the translational motion of the body. It is
expressed in the wing frame (xyz)w as:
Uw(r, t, u) = Rw
y (α)

Rp
z(ϕ)Rb
y(β)


0
˙θb
0

+


0
0
˙ϕ



×


0
r
0

+ Rw
y (α)Rp
z(ϕ)Rb
y(β)


˙xb
0
˙zb

,
(19)
where R defines a rotation matrix for which the subscript indicates the axis of rotation
belonging to the frame referenced by the superscript.
The complete set of rotation
matrices are provided in [62, 79]. In equation (18), CL,w and CD,w model the LEV
dependency on the effective angle of attack αe = cos−1(Uw,z/||Uw||2) defined as the
angle between the chord direction zw (Figure 1b) and the velocity of the wing Uw:
CL = a sin(2αe)
(20)
CD = b + c (1 −cos(2αe)),
(21)
where a, b, c are empirical constants calibrated with CFD simulations [77]. The lift and
drag are finally transformed in the body frame to complete equation (16):


F b
x
0
F b
z

= Rb
y(−β)Rp
z(−ϕ)Rw
y (−α)Ry(αe)


D
0
L

,
(22)
and the pitch moment T b
y is computed similarly using the center of pressure position
xw
c = [0, R2, 0].

## Page 15

Reinforcement Twinning for Hybrid Control of Flapping-Wing Drones
15
4.2. The virtual environment: NLTI system
The virtual environment is based on a nonlinear time-invariant (NLTI) formulation
of the drone dynamics.
NLTI models have a simpler and computationally cheaper
formulation compared to the NLTV system from the real environment. This gives a
higher chance that such a model could allow the RT algorithm to run in real time on
a microcontroller installed on board of a flapping-wing drone. The stability of NLTI
systems can also be studied using standard tools.
Most NLTI models are derived from the NLTV system using the averaging theorem
[80, 9]. The system (17) must first be transformed into the canonical form using the
rescaled time variable τ = 2πft :
dsb
dτ = ϵ
h
g1(sb, a, τ) + g2(sb)
i
.
(23)
For small ϵ = 1/(2πfc) (i.e. large frequencies), the averaging theorem shows that
the direct time dependence of the system can be removed [81]:
dsb
dt = g1(sb, a, wp) + g2(sb),
(24)
where the equation was transformed back to the original time variable.
The key
approximation of the averaging theorem involves cycle-averaging the force vector
g1(s, a) = fc
R 1/fc
0
g1(s, a, τ)dτ using the average state s instead of the instantaneous
state s. However, substituting equation (22) into this integral does not yield a simple
analytical solution without further simplification. For example, the state dependency of
the wing force is ignored in [9, 19, 27] and high-order terms are neglected in [82, 81]. The
present work proposes a different approach to define g1 and improve the state predictions
in various flight scenarios encountered during training. Specifically, g1 is formulated as
a polynomial function of the state s and control variables a = [Aϕ, β, Aoff]:
g1 = W0


Aϕ
β
Aoff

+ W1


A2
ϕ
β2
A2
off

+ W2


AϕAoff
Aϕβ
Aoffβ

+ W3


˙x
˙z
˙θ

+ W4


˙x˙z
˙x˙θ
˙θ˙z


+ W5


˙x
2
˙z
2
˙θ
2

+ W6


Aϕ ˙x
β ˙x
Aoff ˙x

+ W7


Aϕ ˙z
β ˙z
Aoff ˙z

+ W8


Aϕ˙θ
β ˙θ
Aoff˙θ

,
(25)
where W0, W1, W2, W3, W4, W5, W6, W7, W8 ∈R3×3 are the closure coefficients nwp =
81 that must be assimilated using trajectories generated by the real environment (see
Section 3.3).
Four possible simplifications of this model are investigated in Section 5.1. Labeling
the various formulations with growing level of complexity from 1 to 5, so that the full
model is “model 5” (M5), and the most simplified one is “model 1” (M1), with no state

## Page 16

Reinforcement Twinning for Hybrid Control of Flapping-Wing Drones
16
feedback (W3 = W4 = W5 = W6 = W7 = W8 = 0). The “model 2” (M2) is the classic
LTI formulation used in the literature of hovering flight [8, 11], comprising the first and
fourth term (W1 = W2 = W4 = W5 = W6 = W7 = W8 = 0), while “model 3” (M3)
is a combination of models 1 and 2 (W4 = W5 = W6 = W7 = W8 = 0) and finally
“model 4” (M4) also includes the second order term (W6 = W7 = W8 = 0).
5. Results
This section is divided into four subsections.
Section 5.1 evaluates the different
NLTI systems described in Section 4.2 to determine the best trade-off between model
complexity and performance. The identified model serves as a template for the adaptive
model in the RT algorithm.
The following subsections analyze control performance
under three different scenarios, each varying in the initialization of the closure law
parameters wp. In the first scenario (Section 5.2), RT training starts with parameters
that were pre-calibrated offline, simulating a situation where a large dataset is available
before deploying the RT on a new FWMAV prototype. In the second scenario (Section
5.3), RT training begins with randomly initialized weights, representing the opposite
case, where no prior data or knowledge is available before deployment. In the third
scenario (Section 5.3), we consider the presence of a significant bias in the model
parameters. This simulates situations where the FWMAV undergoes a physical change
during operation (e.g., due to damage) or where a substantial bias exists in the pre-
training data. In both cases, the objective is to assess how quickly the RT framework
can adapt the model while simultaneously addressing the control challenge.
5.1. Model selection
To evaluate the NLTI models proposed with equation (25), a database of ntr = 100
trajectories is generated using the real environment and a set of random control
actuations.
These are sampled from a stationary Gaussian process in time, with a
mean taken randomly within the action space and a covariance matrix with a length
scale tuned to ensure gradual variations of the control actions throughout an episode.
All the trajectories from the database start from ˇs = 0 and are cycle averaged to be
compatible with the virtual environment. 20 out of the 100 trajectories are used to train
the NLTI models using the continuous adjoint-based approach (Section 3.3). The rest
of the trajectories are used to test the model’s predictive capability.
Figure 4a shows five test trajectories with the dimensionless states x′ = x/R and
z′ = z/R, with R being the wing span. The trajectories are predicted by the NLTV
model in the role of the real environment and M3 and M5 of the NLTI model (Section
5.1) in the role of the virtual environment. The predictions of M3 and M5 closely follow
the ones from the real environment. Figure 4b provides a more detailed comparison of
the trajectories across the three degrees of freedom of the flapping-wing drone, plotted
against the dimensionless time t′ = tfc. The results indicate that M3, with 39 learning

## Page 17

Reinforcement Twinning for Hybrid Control of Flapping-Wing Drones
17
parameters, achieves a performance comparable to that of M5, which has 81 learning
parameters. Over long trajectories (5 to 6 meters), the discrepancy between the NLTI
and NLTV models becomes more pronounced.
−50
−25
0
25
50
75
100
x′ (−)
−100
−80
−60
−40
−20
0
20
40
z′ (−)
Real
M3
M5
(a)
−50
0
50
100
x′ (-)
0
5
10
15
20
25
30
t′ (-)
−100
−50
0
z′ (-)
0
5
10
15
20
25
30
−50
0
θ (°)
0
5
10
15
20
25
30
Real
M3
M5
(b)
Figure 4: (a) Comparison of open-loop trajectories generated by the real environment
and the virtual environment (Model 3 (M3) and Model 5 (M5)) using the testing dataset,
and (b) detailed view of the x, z, and θ states of the trajectories over time.
For a systematic evaluation of all the performance of the model, keeping the ratio of

## Page 18

Reinforcement Twinning for Hybrid Control of Flapping-Wing Drones
18
20 trajectories for training and 80 for testing, the integrated testing error over the entire
trajectory is illustrated in Figure 5, together with the associated Pearson correlation
coefficient. Model 1 exhibits the poorest performance, with the scatter points displaying
the highest dispersion, emphasizing the crucial role of the state feedback in the force
formulation. Model 2, an LTI system that incorporates these terms, shows improved
correlation between virtual and real trajectories, though noticeable dispersion remains,
as seen in Figure 5. This confirms that higher-order terms are necessary for accurately
predicting trajectories across different flight regimes. Model 3, which includes second-
order terms of control actions, significantly enhances performance. The longitudinal,
vertical, and pitching positions exhibit a clear linear trend, with Pearson’s correlation
coefficients exceeding 0.99. Adding the second-order terms of the state (i.e. W4, W5 in
(25)) as in M4 and the cross-talk terms (i.e. W6, W7, W8 in (25)) in M5 does not result
in a significant improvement, at least for the length of the trajectories investigated in
these test.
−100
−50
0
50
100
−100
−50
0
50
100 ρx = 0.970
ρz = 0.967
ρθ = 0.857
M1
−100
−50
0
50
100
−100
−50
0
50
100 ρx = 0.978
ρz = 0.985
ρθ = 0.931
M2
−100
−50
0
50
100
−100
−50
0
50
100 ρx = 0.999
ρz = 0.996
ρθ = 0.991
M3
−100
−50
0
50
100
−100
−50
0
50
100 ρx = 0.999
ρz = 0.995
ρθ = 0.983
M4
−100
−50
0
50
100
−100
−50
0
50
100 ρx = 0.999
ρz = 0.996
ρθ = 0.991
M5
x′ (−)
z′ (−)
θ (deg)
Figure 5:
Scatter plot of the trajectories computed with the real and the virtual
environment for five closure laws assimilated from the real trajectories.
Therefore, for the purposes of this work, model M3 is considered as the best
compromise between accuracy and complexity.

## Page 19

Reinforcement Twinning for Hybrid Control of Flapping-Wing Drones
19
100
101
102
Episode
−1.7
−1.3
−0.9
−0.5
−0.1
ˇRa/ ˇRa,0 (-)
RT
Model −free
(a)
100
101
102
Episode
−1.2
−0.9
−0.6
−0.3
0.0
Ra/Ra,0 (-)
πmf
πmb
p
c
0
20
40
60
80
100
p and c (%)
(b)
Figure 6: Comparison of cumulative rewards for (a) RT and DDPG training and (b)
model-based and model-free policies, along with policy type and weight cloning signals
during RT training.
5.2. Policy training with offline model calibration
This section evaluates the performance of the RT algorithm in training the control
policy (equation (6)) using M3 as the closure law for the virtual environment. The
model is pre-calibrated offline as in Section 5.1, ensuring state predictions similar to the
real environment. It is then assumed that the real-to-virtual environment trust ratio
satisfies RV ETl < RV ET < RV ETu from the outset of policy training (see Figure 3).
Table 1 lists the key hyperparameters used for the training. To evaluate the benefits of
hybridizing model-free and model-based control, the learning and control performances
of the RT are compared to the traditional DDPG algorithm, implemented in its classic
stand-alone model-free approach. This corresponds to steps 1 and 2 in Algorithm 1.
General Parameters
T0 (s)
∆t (s)
Nc
Nep
Ns
1.5
0.05
30
250
25
Model Parameters
Model-Free
Model-Based
NR1
na
nq
np
Ne
nG
nmb
2000
30
30
39
5
50
30
Referee Parameters
CM
Cπ
Cw
TJ
TJi
Tw
RV ETl
RV ETu
2
5
5
1
0.8
0.05
0
40
Table 1: Hyperparameters used by the reinforcement twinning algorithm.
Figure 6a shows the cumulative reward (equation (8)) over 250 training episodes

## Page 20

Reinforcement Twinning for Hybrid Control of Flapping-Wing Drones
20
for the two control strategies. The figure displays the mean and the 95% confidence
interval, calculated from Ns = 25 training instances with randomly initialized policy
weights. During the first five episodes, actions are sampled from the trajectory database
to explore the state space and populate the replay buffer. This process allows faster
convergence of the model-free policy in both the RT and the model-free algorithm. At
the end of this exploratory phase, the cumulative reward from the RT training increases
significantly and rapidly converges to the highest value, with negligible variance. The
model-free reward increases more gradually and converges to a lower mean cumulative
reward with a larger variance, indicating a less effective control policy.
Figure 6b analyzes in more detail the performances of the RT, showing the
cumulative reward for the model-based (dashed line) and the model-free (dash-dotted
line) policies, evaluated in the virtual environment. The policy type p and weight cloning
c signals are also displayed as percentages across the Ns cases.
By default, the live policy begins as model-free. Its cumulative reward remains
larger than the model-based for Cπ episodes, after which a switch occurs (see policy
type signal p) and the model-based policy becomes live. Over the next Cw episodes,
the model-based policy significantly and consistently outperforms the model-free policy.
This activates the weight cloning signal c, cloning the model-based weights wa,mb into
wa,mf. As a result, the cumulative reward from the model-free policy sharply increases
at episode 9.
The remaining episodes are carried out mostly with the model-based
policy while the two reward functions converge, and multiple weight cloning occurs in
the model-free weights. For this specific test case, where RT can rely on an accurate
model of the real environment from the beginning of the training, the model-based policy
drives the overall training and acts as a safeguard to the model-free policy exploration.
In this first case, the model-free policy does not support the model-based policy
training; however, this collaboration was not needed.
The model-based policy does
not face problematic local minima during its training and maintains consistent control
performance from the virtual to the real environment, thanks to marginal modeling
errors.
The good control performance of the RT algorithm is verified in Figure 7. Figure
7a focuses on the time evolution of the dimensionless x′, z′ positions and the θ angle,
while Figure 7b shows their time derivative. In these plots, the right axis shows the
contribution to the cycle-reward (equation 2) due to the performances in each degree
of freedom. The curves are represented with a mean and a 95% confidence interval
computed from the Ns training cases. High-frequency oscillations in the state evolution
are due to the periodic forces generated by the flapping motion of the wing.
Figure 7a and 7b show that the drone ascends with maximal acceleration for the
first flapping cycles until it reaches a peak velocity, starting from which it decelerates
to stabilise around z = 1 m (z′ = 20). This evolution is directly linked to the flapping
amplitude Aϕ that is maximal at t′ = 0, decreases as the drone approaches the target
and stabilises to an angle such that the lift balances the weight.
According to the
drone dynamics (equation 16), the flapping angle also influences the longitudinal and

## Page 21

Reinforcement Twinning for Hybrid Control of Flapping-Wing Drones
21
pitching motion, which show small deviations from zero. These motions influence back
the flapping angle considering the fully coupled formulation of the policy (equation (6)).
The longitudinal and pitching motions are stabilised by slightly varying the stroke plane
and the mean flapping angles during the episode. The analysis shows that the state error
in z′ is the main contributor to the reward within the first 20 cycles. After this period,
the state error in the pitching direction becomes more influential due to slight heading
drift.
The largely different variances in the control actions shown in Figure 7c gives an
indication on the relative importance of their contribution to the success of the control
task. More specifically, it shows that the flapping amplitude Aϕ is more important than
the control on the stroke plane angle β and the mean flapping angle Aoff. This result
suggests that an alternative ’reward shaping’ could slightly enhance control performance.
Increasing the weight of the vertical position reward may accelerate learning but could
also introduce slightly more drift in the other two degrees of freedom.
5.3. Policy training with online twinning
The previous case employs reinforcement twinning with a dynamic model pre-calibrated
on a database of diverse flight trajectories.
Acquiring such extensive data is often
impractical, particularly when the drone dynamics is unknown: fully random actions
could damage the drone, and an overly limited action space might results in trajectories
that are not sufficiently diverse and informative.
Furthermore, sequentially training
the model and then the policy can be sample-inefficient, as even a partially calibrated
model can provide valuable guidance to the model-based and model-free policies. This
section investigates the simultaneous training of the model and the policy, starting from
randomly initialised wp and wa. The training is conducted over Ns runs using the same
hyperparameters as in the previous test case (Table 1).
Four control strategies are considered: (1) a fully model-free approach (only steps
1 and 2 in Algorithm 1), (2) a fully model-based approach (steps 1,3,4,5, and 6 in
Algorithm 1) and two implementations of the full RT algorithm, differing in the way
the assimilation buffer DA is filled. These are the maximum-variance and the minimum-
error criteria described in Section 3.1.
As for the cases in Section 5.2, actions are
sampled from a Gaussian process for the first Ne = 5 episodes for all methods. This
allows populating the assimilation and replay buffers (DA and DR1) with demonstration
trajectories, accelerating the training of the model, the critic network, and the model-
free policy. Once the assimilation buffer is full, the policy begins interacting with the
environment, and the assimilation buffer is updated following either the maximum-
variance or the minimum-error criteria.
Figure 8a shows the evolution of the cumulative reward for the four approaches.
In terms of sample efficiency, it is clear that the model-based method has the poorest
performance, exhibiting the slowest convergence, the lowest mean cumulative reward,
and the largest variance. This is due to the policy’s blind reliance on the model, hence

## Page 22

Reinforcement Twinning for Hybrid Control of Flapping-Wing Drones
22
0
20
t′ (−)
−0.4
−0.2
0.0
0.2
0.4
x (m)
0
20
t′ (−)
0.00
0.25
0.50
0.75
1.00
z (m)
0
20
t′ (−)
−10
0
10
θ (°)
0.000
0.001
0.002
0.003
0.004
0.005
rx
0.00
0.05
0.10
0.15
0.20
rz
0.000
0.005
0.010
0.015
0.020
rθ
(a)
0
20
t′(−)
−0.4
−0.2
0.0
0.2
0.4
˙x′ (m/s)
0
20
t′ (−)
0.00
0.25
0.50
0.75
1.00
˙z′ (m/s)
0
20
t′ (−)
−100
−50
0
50
100
˙θ (°/s)
0.0000
0.0005
0.0010
0.0015
rx
0.000
0.005
0.010
0.015
rz
0.00
0.01
0.02
0.03
0.04
0.05
rθ
(b)
0
10
20
30
t′ (−)
60
70
80
Aφ (°)
0
10
20
30
t′ (−)
−2
−1
0
1
2
β (°)
0
10
20
30
t′ (−)
−0.02
0.00
0.02
0.04
Aoff (°)
(c)
Figure 7: Vertical ascent and hover trajectories shown with (a) the drone positions, (b)
the drone velocities resulting from a RT trained policy, and (c) the control actions.
the closure parameters wp, which must be identified while simultaneously training the
policy. As these parameters are randomly initialized, the training of the model-based
policy begins from a poor model. This leads to policy bias, as policy improvements in
the virtual environment often fail to translate to improvements in the real environment.
Interestingly, the incorrect mapping between the virtual and the real environments
allows the live policy to jump between different action spaces erratically; although this
further deteriorates the control learning performances, it helps improve the assimilation
buffer diversity and, consequently, the model calibration.

## Page 23

Reinforcement Twinning for Hybrid Control of Flapping-Wing Drones
23
In the presence of a poor model, the model-free approach has a significant
performance margin over the model-based policy, according to all metrics: convergence,
variance, and average reward at the end of the training. In the model-based versus
model-free dilemma, the scenario explored in this section represents the opposite
condition of the previous section. This motivates the interest in the hybrid approach
proposed in this work. Both RT formulations achieve faster convergence and higher
cumulative reward than the model-free and the model-based approaches.
The RT
overtakes the model-free around episode 30. The reason can be inferred from the plots
in Figures 8b and 8c. Figure 8b tracks the averaged percentage of training cases where
the live policy is model-free, while Figure 8c shows the percentage of cases where the
model is inconsistent with the real environment. This occurs when RVET (equation
(15)) falls outside the range defined with RVETl and RVETu, as described in Section
3.4. Around episode 30, the model failure has decreased considerably, signaling that
the data assimilation has improved the consistency of the virtual model with the real
environment. Following this model improvement, model-based optimization of the policy
begins. The higher sample efficiency of this optimisation allows the model-based policy
to rapidly outperform the model-free policy, as evidenced by the decreasing model-free
percentage in Figure 8c.
However, as control performances improve, the live policy
visits new trajectories in the real environment where model accuracy deteriorates,
prompting the live policy to switch back to the model-free approach. This oscillating
dynamic between brief attempts of model-based and extended attempts with model-free
is repeated until the end of training.
For the maximum variance assimilation buffer, the average model failure percentage
decreases over the training, increasing the amount of model-based policy actions in the
real environment.
On the contrary, for the minimum error assimilation buffer, the
average model failure percentage increases over the training, increasing the amount of
model-free policy actions in the real environment. The model guides the training of the
live policy until it can not further mimic the real environment, rendering model-based
policy updates unreliable. Nevertheless, the net effect of both RT formulations is the
enhancement of learning performance over the pure model-free approach.
The RT training has a smaller variance than the model-free training, showing that
the hybrid approach streamlines the exploration in the state-space. When the model-
free policy diverges, the model-based policy often performs better and becomes live to
redirect the control actions toward more optimal regions. On the other hand, when the
model is not consistent with the virtual environment, the model-free policy can explore
and improve the policy, leveraging the past experiences of the model-based policy in the
replay buffer.
Figure 8a also reveals that maximizing trajectory variance in DA leads to slightly
faster convergence than minimizing trajectory-target error. This performance gap stems
from model overfitting during minimum-error training, as seen in Figure 9b, which
shows the states from the virtual and real trajectories stored in the assimilation buffer
in the final training episode (for the Ns cases). The states mostly cluster around the

## Page 24

Reinforcement Twinning for Hybrid Control of Flapping-Wing Drones
24
0
50
100
150
200
250
Episode
−2.5
−2.0
−1.5
−1.0
−0.5
ˇRa/ ˇRa,0 [-]
Model-free
Model-based
RT - max variance
RT - min error
(a)
0
50
100
150
200
250
Episode
40
60
80
100
Model −free %
RT - max variance
RT - min error
(b)
0
50
100
150
200
250
Episode
40
60
80
100
Model failure %
RT - max variance
RT - min error
(c)
Figure 8: (a) Comparison of cumulative rewards among the model-free approach, the
model-based approach, and the RT approach, using two different saving strategies for
the assimilation buffer. (b) Comparison of the model-free percentage and (c) model-
failure percentage for the two strategies.
target trajectory compared to the wider state space covered in the maximum variance
DA in Figure 9a. Nevertheless, both buffering approaches result in successful model
assimilation, as demonstrated by the linear trend linking real and virtual states. The
Pearson correlation coefficients are lowest for pitching motions, suggesting a greater
challenge in capturing rotational dynamics, particularly for the minimum-error strategy
where most of the angles live around 0. One could weight the contributions of the model
errors in 10 to decrease the model failure and model-based policy percentage in training

## Page 25

Reinforcement Twinning for Hybrid Control of Flapping-Wing Drones
25
(Figure 8). However, given that these angles cluster around 0 (Figure 9a), the absolute
modelling error still allows to give valuable guidance to the control policy training.
−40
−20
0
20
40
−40
−20
0
20
40
ρx = 0.987
ρz = 0.997
ρθ = 0.951
x′ (−)
z′ (−)
θ (deg)
(a)
−20
−10
0
10
−20
−10
0
10
ρx = 0.975
ρz = 0.998
ρθ = 0.611
x′ (−)
z′ (−)
θ (deg)
(b)
Figure 9: Comparison of the states saved in the assimilation buffer after the RT training
following (a) the maximum-variance strategy and (b) the minimum-error strategy.
Figure 10a (top) provides additional details on the assimilation, showing the
normalised cost over the training episodes. This cost decreases by 3 orders of magnitude
for the two buffering strategies during the first 50 episodes. After that, it oscillates,
indicating further calibrations of the weights wp. This is also due to new trajectories
that are saved in the assimilation buffer as shown in Figure 10a (bottom), which shows
the update percentage of the assimilation buffer. The assimilation buffer following the
minimum error strategy is more often updated across the training.
Finally, Figure 10b on the right depicts the Q-value averaged over the mini-batches
sampled from the replay buffer throughout the training.
The Q-value exhibits an
initial overshoot attributed to the overestimation bias of the DDPG algorithm [83].
Subsequently, it decreases and converges, with faster convergence when using the
reinforcement twinning algorithm. This improvement results from the transitions saved
in the replay buffer when the model-based policy interacts with the real environment.
These transitions allow to train the critic network in action-state spaces with higher
potential rewards, leading to better updates of the model-free policy according to
equation (9). The model-based policy allows then to improve the model-free policy,
which in turn improves the model-based policy through the twinning of the model and
the policy cloning. This demonstrates the symbiotic functioning of the two agents.
5.4. Policy training with online twinning and model biases
This last test case combines the training setups of the two previous cases. Training
begins with the offline-calibrated M3, based on the trajectory database generated in
5.1. However, the database originates from a real environment with slightly different

## Page 26

Reinforcement Twinning for Hybrid Control of Flapping-Wing Drones
26
10−4
10−3
10−2
10−1
100
Jp/Jp,0
RT - max variance
RT - min error
0
50
100
150
200
Episode
0
25
50
75
100
DA update (%)
RT - max variance
RT - min error
(a)
0
50
100
150
200
250
Episode
−10
−8
−6
−4
−2
0
Q
Model-free
RT - max variance
RT - min error
(b)
Figure 10: (a) Comparison of the assimilation cost for the two RT training (top) and the
update percentage in the assimilation buffer (bottom). (b) Comparison of the Q-value
predicted by the critic network during the RT and model-free training.
dynamics than the one used in the current training. Online twinning is thus necessary to
compensate for the model biases. Such drift of the environment dynamics is common for
flapping-wing drone prototypes, where precise characterisation is challenging due to their
miniature scale. Additionally, their dynamics can change in-flight due to component
damage or payload variations.
This third test case focuses on two environment defaults relative to the trajectory
database: 1) a 33% increase in drone mass (referred to as “mass bias” hereafter), and
2) a 3 mm longitudinal offset of the drone’s centre of pressure (referred to as “cop bias”
hereafter).
The model-free and model-based policies are initialised with random weights, and
the training hyperparameters are summarised in Table 1. The buffering strategy of the
assimilation buffer is the maximum variance.
As for Section 5.3, Figure 11a shows the mean cumulative reward and the 95%
confidence interval based on Ns training cases, Figure 11b shows the percentage of
live policies using the model-free policy and Figure 11b shows the percentage of cases
for which the model is inconsistent with the real environment as defined by equation
(15). Initially, the model cannot be trusted, and the model-free policy is driving the
real environment. As this policy interacts with the real environment, transitions are
collected in the assimilation buffer, allowing the model closure to compensate for its
inconsistency with the real environment. Confidence is again built in the model as seen
with a decrease of model-free percentage (Figure 11b) and a higher consistency between
the real environment and the model (Figure 11c). The cumulative reward then rapidly

## Page 27

Reinforcement Twinning for Hybrid Control of Flapping-Wing Drones
27
increases until convergence, characterised by a low variance (Figure 11a). The model-
based policy contributions are visible on the cumulative reward function, showing nearly
vertical jump at the beginning of the training.
Figure 11d shows the averaged x −z trajectories of the drone controlled using
policies trained for the mass and cop bias cases.
Arrows are also overlaid on the
trajectory to indicate the drone’s heading every five flapping cycles. These trajectories
were obtained without applying policy bias in the longitudinal direction, as this term
must converge to zero for the target considered.
The drone successfully ascends
vertically and hover, exhibiting small oscillations along the longitudinal direction while
maintaining a near horizontal heading (i.e. θ ≈0◦). In the mass bias cases, the drone
slightly overshoots the target. This behaviour could be improved with further tuning of
the weights from the reward function (equation (2)).
6. Conclusion and perspectives
This work has presented an extended formulation of the Reinforcement Twinning (RT)
algorithm [62] and applied it to the control of flapping-wing drones. The RT algorithm
combines a model-free policy trained via actor-critic reinforcement learning and a
model-based policy optimized through adjoint-based data assimilation, with both agents
interacting via a dynamic policy referee and supporting each other’s learning.
Compared to the original formulation, the RT framework has been significantly
enhanced through the introduction of a trust-based policy selection mechanism,
improved collaboration strategies, and full online model identification. A cycle-averaged
surrogate model incorporating second-order terms was trained using adjoint-based data
assimilation, providing a computationally efficient and adaptive virtual environment.
The improved RT algorithm was evaluated across three control scenarios, varying
in prior knowledge and model bias. When the virtual environment was pre-calibrated,
RT demonstrated significantly higher sample efficiency than standard reinforcement
learning, with the model-based agent driving early training. In fully online settings,
the RT framework enabled rapid model adaptation and consistently outperformed both
standalone model-free and model-based approaches. Even in the presence of substantial
model bias, RT successfully corrected the surrogate model and maintained efficient
policy learning within a limited number of episodes. These results confirm the benefits of
the hybrid architecture and, more broadly, demonstrate the potential of RT as a general-
purpose learning framework for real-time control in dynamically evolving environments.
Future work will extend the framework to lateral and full 3D flapping dynamics,
incorporating coupled wing-body effects in the real environment. These additions may
reduce the accuracy of the current surrogate models during agile maneuvers, prompting
ongoing exploration of enhanced closures, local model interpolation, or time-varying
formulations.
A key direction will be to further integrate the two learning modes,
allowing the model-based policy to more directly exploit real-environment experience
gathered by the model-free agent.

## Page 28

Reinforcement Twinning for Hybrid Control of Flapping-Wing Drones
28
0
50
100
150
200
250
Episode
−3.5
−3.0
−2.5
−2.0
−1.5
−1.0
−0.5
0.0
ˇRa/ ˇRa,0 [-]
cop bias
mass bias
(a)
0
50
100
150
200
250
Episode
20
40
60
80
100
Model −free %
cop bias
mass bias
(b)
0
50
100
150
200
250
Episode
0
20
40
60
80
100
Model failure %
cop bias
mass bias
(c)
−0.06
−0.04
−0.02
0.00
0.02
0.04
0.06
x (m)
0.00
0.25
0.50
0.75
1.00
z (m)
t’=0
t’=5
t’=10
t’=15
t’=20
t’=25
t’=0
t’=5
t’=10
t’=15
t’=20
t’=25
Cop bias
Mass bias
(d)
Figure 11: (a) Cumulative rewards for the RT approach using the maximum-variance
assimilation buffer, starting from a virtual environment calibrated offline with estimation
biases in mass and centre of pressure (cop). (b) and (c) show the model-free and model-
failure percentages during training for the two cases. (d) shows the resulting x −z
trajectories of the drone during vertical ascent.
Acknowledgements
Romain Poletti and Lorenzo Schena were supported by Fonds Weten- schappelijk
Onderzoek (FWO), Project No. 1SD7823N and 1S67925N. The work was also partially
supported by the European Research Council (ERC) under the European Union’s
Horizon Europe research and innovation programme, through a Starting Grant awarded
to M. A. Mendez (grant agreement No. 101165479 — RE-TWIST). The views and
opinions expressed are those of the authors only and do not necessarily reflect those of
the European Union or the European Research Council. Neither the European Union
nor the granting authority can be held responsible for them.

## Page 29

Reinforcement Twinning for Hybrid Control of Flapping-Wing Drones
29
7. References
[1] Keennon M, Klingebiel K and Won H 2012 Development of the nano hummingbird: A tailless
flapping wing micro air vehicle 50th AIAA aerospace sciences meeting including the new horizons
forum and aerospace exposition p 588
[2] Ma K Y, Chirarattananon P, Fuller S B and Wood R J 2013 Science 340 603–607
[3] Hsiao Y H, Kim S, Ceron S, Ren Z and Chen Y 2024 Advanced Intelligent Systems 6 2300059
[4] Zhang J, Fei F, Tu Z and Deng X 2017 Design optimization and system integration of robotic
hummingbird 2017 IEEE International Conference on Robotics and Automation (ICRA) (IEEE)
pp 5422–5428
[5] Kar´asek M, Muijres F T, De Wagter C, Remes B D and De Croon G C 2018 Science 361 1089–1094
[6] Phan H V, Kang T and Park H C 2017 Bioinspiration & biomimetics 12 036006
[7] Wang H, Farid Y, Wang L, Garone E and Preumont A 2024 Hovering flight of a robotic
hummingbird: Dynamic observer and flight tests Actuators vol 13 (MDPI) p 91
[8] Taha H E, Hajj M R and Nayfeh A H 2012 Nonlinear Dynamics 70 907–939
[9] Schenato L, Campolo D and Sastry S 2003 Controllability issues in flapping flight for biomimetic
micro aerial vehicles (mavs) 42nd IEEE International Conference on Decision and Control
(IEEE Cat. no. 03CH37475) vol 6 (IEEE) pp 6441–6447
[10] Taylor G and Thomas A 2002 Journal of theoretical biology 214 351–370
[11] Orlowski C T and Girard A R 2012 Progress in Aerospace Sciences 51 18–30
[12] Poletti R, Barucca M, Koloszar L, Mendez M and Degroote J 2023 Development of an fsi
environment for the aerodynamic performance assessment of flapping wings X International
Conference on Computational Methods for Coupled Problems in Science and Engineering
[13] Sun M and Wang J K 2007 Journal of Experimental Biology 210 2714–2722
[14] Kar´asek M and Preumont A 2012 International Journal of Micro Air Vehicles 4 203–226
[15] Aurecianus S, Phan H V, Kang T and Park H C 2020 Bioinspiration & Biomimetics 15 056004
[16] P´erez-Arancibia N O, Ma K Y, Galloway K C, Greenberg J D and Wood R J 2011 Bioinspiration
& Biomimetics 6 036009
[17] Hu K, Deng H, Xiao S, Yang G and Sun Y 2024 Journal of Bionic Engineering 21 1191–1207
[18] Biswal S, Mignolet M and Rodriguez A A 2019 Bioinspiration & biomimetics 14 026004
[19] Deng X, Schenato L and Sastry S S 2006 IEEE transactions on robotics 22 789–803
[20] Abbasi S H, Mahmood A, Khaliq A and Imran M 2022 Journal of Intelligent & Robotic Systems
105 79
[21] Bhatia M, Patil M, Woolsey C, Stanford B and Beran P 2014 Journal of Guidance, Control, and
Dynamics 37 592–607
[22] Xiong Y and Sun M 2009 Acta Mechanica Sinica 25 13–21
[23] Tahmasian S, Woolsey C A and Taha H E 2014 Longitudinal flight control of flapping wing micro
air vehicles AIAA Guidance, Navigation, and Control Conference p 1470
[24] Yao J and Yeo K 2019 Bioinspiration & Biomimetics 14 056005
[25] Khosravi M and Novinzadeh A 2021 Aerospace Science and Technology 112 106525
[26] Doman D B, Oppenheimer M W and Sigthorsson D O 2010 Journal of guidance, control, and
dynamics 33 724–739
[27] Oppenheimer M W, Doman D B and Sigthorsson D O 2011 Journal of guidance, control, and
dynamics 34 204–217
[28] Zhu B, Zuo Z, Sun L, Zou Y and Xia K 2018 Model predictive control for a 3-dof flapping-wing
unmanned aerial vehicle with control constraints 2018 3rd International Conference on Advanced
Robotics and Mechatronics (ICARM) (IEEE) pp 548–553
[29] Zheng H, Chen W and Xie F 2024 IEEE Access
[30] Chung S J and Dorothy M 2010 Journal of guidance, control, and dynamics 33 440–453
[31] Chirarattananon P, Ma K Y and Wood R J 2014 Bioinspiration & biomimetics 9 025004
[32] Fei F, Tu Z and Deng X 2023 Bioinspiration & Biomimetics 18 026003

## Page 30

Reinforcement Twinning for Hybrid Control of Flapping-Wing Drones
30
[33] Zhu B and Zuo Z 2017 Adaptive model predictive control for set-point tracking of a single-dof
flapping-wing unmanned aerial vehicle 2017 13th IEEE International Conference on Control &
Automation (ICCA) (IEEE) pp 861–866
[34] Chand A N, Kawanishi M and Narikiyo T 2016 Advanced Robotics 30 1039–1049
[35] Vignon C, Rabault J and Vinuesa R 2023 Physics of fluids 35
[36] Din A F U, Mir I, Gul F and Akhtar S 2023 Journal of Ambient Intelligence and Humanized
Computing 14 4005–4022
[37] Pino F, Schena L, Rabault J and Mendez M A 2023 Journal of Fluid Mechanics 958 A39
[38] Tedrake R, Jackowski Z, Cory R, Roberts J W and Hoburg W 2009 Learning to fly like a bird
14th International symposium on robotics research. Lucerne, Switzerland (Citeseer)
[39] Chand A N, Kawanishi M and Narikiyo T 2016 Non-linear model-free control of flapping wing
flying robot using ipid 2016 IEEE International Conference on Robotics and Automation (ICRA)
(IEEE) pp 2930–2937
[40] Guo Q, Hu M, Wei R, Xu J and Song H 2008 Hovering control based on fuzzy neural networks
for biomimetic flying robotic 2008 International Conference on Information and Automation
(IEEE) pp 504–508
[41] Sutton R S 2018 A Bradford Book
[42] Verma S, Novati G and Koumoutsakos P 2018 Proceedings of the National Academy of Sciences
115 5849–5854
[43] Zhu Y, Pang J H, Gao T and Tian F B 2022 Bioinspiration & Biomimetics 18 015003
[44] Wang Z, Lin R, Zhao Z, Chen X, Guo P, Yang N, Wang Z and Fan D 2024 Journal of Fluid
Mechanics 984 A9
[45] Beckers D and Eldredge J D 2024 arXiv preprint arXiv:2404.01506
[46] Novati G, Mahadevan L and Koumoutsakos P 2019 Physical Review Fluids 4 093902
[47] Motamed M and Yan J 2007 A reinforcement learning approach to lift generation in flapping
mavs: Experimental results Proceedings 2007 IEEE International Conference on Robotics and
Automation (IEEE) pp 748–754
[48] Bayiz Y E, Hsu S J, Aguiles A N, Shade-Alexander Y and Cheng B 2019 Experimental learning
of a lift-maximizing central pattern generator for a flapping robotic wing 2019 International
Conference on Robotics and Automation (ICRA) (IEEE) pp 1997–2003
[49] Xiong M, Wei Z, Yang Y, Chen Q and Liu X 2023 Bioinspiration & Biomimetics 18 046010
[50] Xue Y, Cai X, Xu R and Liu H 2023 Biomimetics 8 295
[51] Fei F, Tu Z, Zhang J and Deng X 2019 Learning extreme hummingbird maneuvers on flapping
wing robots 2019 International Conference on Robotics and Automation (ICRA) (IEEE) pp
109–115
[52] Tu Z, Fei F and Deng X 2021 IEEE Transactions on Robotics 37 1742–1751
[53] Liu X and MacArt J F 2024 Physical Review Fluids 9 013901
[54] Liu X Y and Wang J X 2021 Proceedings of the Royal Society A 477 20210618
[55] Lutter M, Silberbauer J, Watson J and Peters J 2021 Differentiable physics models for real-world
offline model-based reinforcement learning 2021 IEEE International Conference on Robotics and
Automation (ICRA) (IEEE) pp 4163–4170
[56] Farshidian F, Neunert M and Buchli J 2014 Learning of closed-loop motion control 2014 IEEE/RSJ
International Conference on Intelligent Robots and Systems (IEEE) pp 1441–1446
[57] Qu G, Yu C, Low S and Wierman A 2020 arXiv preprint arXiv:2006.07476
[58] Freed B, Wei T, Calandra R, Schneider J and Choset H
[59] Chebotar Y, Hausman K, Zhang M, Sukhatme G, Schaal S and Levine S 2017 Combining
model-based and model-free updates for trajectory-centric reinforcement learning International
conference on machine learning (PMLR) pp 703–711
[60] Yamada S, Watanabe A and Nakashima M 1997 Advances in Neural Information Processing
Systems 10
[61] Pinosky A, Abraham I, Broad A, Argall B and Murphey T D 2023 The International Journal of

## Page 31

Reinforcement Twinning for Hybrid Control of Flapping-Wing Drones
31
Robotics Research 42 337–355
[62] Schena L, Marques P A, Poletti R, Ahizi S, Van den Berghe J and Mendez M A 2024 Journal of
Computational Science 82 102421
[63] Ortega-Jim´enez V M and Dudley R 2018 Journal of Experimental Biology 221 jeb191171
[64] Calado A, Poletti R, Koloszar L K and Mendez M A 2023 Physics of Fluids 35
[65] Poletti R, Calado A, Koloszar L K, Degroote J and Mendez M A 2024 Physics of Fluids 36
[66] Faruque I A, Muijres F T, Macfarlane K M, Kehlenbeck A and Humbert J S 2018 Biological
cybernetics 112 165–179
[67] Taylor G K 2001 Biological Reviews 76 449–471
[68] JIE Y 2018
[69] Tu Z, Fei F, Liu L, Zhou Y and Deng X 2021 IEEE Robotics and Automation Letters 6 2114–2121
[70] Lillicrap T 2015 arXiv preprint arXiv:1509.02971
[71] Kingma D P 2014 arXiv preprint arXiv:1412.6980
[72] Koziel S, Ciaurri D E and Leifsson L 2011 Computational optimization, methods and algorithms
33–59
[73] Nocedal J and Wright S J 1999 Numerical optimization (Springer)
[74] Samin J C and Fisette P 2003 Symbolic modeling of multibody systems vol 112 (Springer Science
& Business Media)
[75] Sun M, Wang J and Xiong Y 2007 Acta Mechanica Sinica 23 231–246
[76] Etkin B and Reid L D 1995 Dynamics of flight: stability and control (John Wiley & Sons)
[77] Lee Y J, Lua K B, Lim T T and Yeo K S 2016 Bioinspiration and Biomimetics 11 1–27 ISSN
17483190
[78] Eldredge J D and Jones A R 2019 Annual Review of Fluid Mechanics 51 75–104
[79] Cai X, Kolomenskiy D, Nakata T and Liu H 2021 Journal of Fluid Mechanics 915 1–46 ISSN
14697645
[80] Khalil H K and Grizzle J W 2002 Nonlinear systems vol 3 (Prentice hall Upper Saddle River, NJ)
[81] Taha H E, Hajj M R and Nayfeh A H 2014 Journal of Guidance, Control, and Dynamics 37
970–979
[82] Cheng B and Deng X 2011 IEEE Transactions on Robotics 27 849–864
[83] Fujimoto S, Hoof H and Meger D 2018 Addressing function approximation error in actor-critic
methods International conference on machine learning (PMLR) pp 1587–1596
