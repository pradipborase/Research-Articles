# event_triggered_cascade_active_disturbance_rejection_control_for_quadrotor_trajectory_tracking.pdf

## Page 1

Event-Triggered Cascade Active Disturbance
Rejection Control for Quadrotor Trajectory Tracking
Xin Chen 
Haibei Power Supply Company of State Grid Qinghai Electric Power Company
Kai Chen 
Haibei Power Supply Company of State Grid Qinghai Electric Power Company
Fuhua Qiang 
Haibei Power Supply Company of State Grid Qinghai Electric Power Company
Yongke Sun 
Haibei Power Supply Company of State Grid Qinghai Electric Power Company
Xin Lai 
Haibei Power Supply Company of State Grid Qinghai Electric Power Company
Research Article
Keywords: quadrotor UAV, trajectory tracking, cascade active disturbance rejection control, event-
triggered mechanism, particle swarm optimization, extended state observer
Posted Date: March 2nd, 2026
DOI: https://doi.org/10.21203/rs.3.rs-8853188/v1
License:   This work is licensed under a Creative Commons Attribution 4.0 International License.  
Read Full License
Additional Declarations: No competing interests reported.

## Page 2

Event-Triggered Cascade Active Disturbance
Rejection Control for Quadrotor Trajectory
Tracking
Xin Chen1,2*, Kai Chen1,2, Fuhua Qiang1,2, Yongke Sun1,2, Xin
Lai1,2
1Haibei Power Supply Company of State Grid Qinghai Electric Power
Company.
2State Grid Qinghai Electric Power Company.
*Corresponding author(s). E-mail(s): xin chen1231120@163.com;
Contributing authors: kai chen1232025@163.com;
Fuhua Qiang123@163.com; Yongke sun123@163.com;
xin lai123@outlook.com;
Abstract
This paper presents an event-triggered cascade active disturbance rejection con-
trol (CADRC) approach for quadrotor trajectory tracking. The proposed method
decouples the system into position and velocity subsystems, with dedicated
extended state observers (ESOs) and controllers designed for each subsystem to
achieve accurate estimation and compensation of system nonlinearities, coupling
eﬀects, and external disturbances. To further optimize computational resource
utilization, a hybrid event-triggering mechanism incorporating both static and
dynamic thresholds is developed. This mechanism updates system states and con-
trol commands only at triggering instants, signiﬁcantly reducing computational
overhead. Additionally, an online self-tuning method based on particle swarm
optimization (PSO) is introduced to enhance controller adaptability. Simulation
results validate the robustness and eﬃciency of the proposed approach.
Keywords: quadrotor UAV, trajectory tracking, cascade active disturbance rejection
control, event-triggered mechanism, particle swarm optimization, extended state
observer
1

## Page 3

1 Introduction
With the rapid advancement of unmanned aerial vehicle (UAV) technologies, quadro-
tors have demonstrated vast application potential across military [1, 2] and civilian
[3, 4] domains due to their unique ﬂight performance characteristics. As a vertical
take-oﬀand landing (VTOL) platform capable of stationary hovering and agile maneu-
vering, quadrotor systems exhibit superior environmental adaptability compared to
ﬁxed-wing UAVs, enabling the execution of complex missions within conﬁned and
challenging airspace. However, quadrotors are inherently underactuated systems with
strongly coupled nonlinear dynamics. Addressing model uncertainties, inter-channel
coupling eﬀects, and nonlinearities to achieve stable control has become a focal point
in current international research.
In the domain of traditional control methods, PID control [5, 6] has dominated
early UAV control systems due to its simple structure and ease of implementation. PID
control exhibits poor adaptability to nonlinear and strongly coupled systems, making
it diﬃcult to handle complex disturbances. To address this limitation, researchers have
introduced sliding mode control (SMC) [7, 8]. The SMC controller demonstrates strong
robustness against systems with parametric uncertainties. Modern control methods,
such as adaptive control [9, 10] and model predictive control (MPC) [11, 12], have
gradually gained attention. Adaptive control possesses the ability to actively adjust
to dynamic systems, making it suitable for systems with uncertainties. During the
control process, it continuously modiﬁes its own parameters to adapt to variations in
the controlled plant. However, adaptive control requires a mathematical model where
the system structure is known, and uncertainties are limited to unknown parameters.
MPC, rooted in optimization theory, is well-suited for constrained control problems.
Nevertheless, its performance heavily depends on model accuracy.
From an implementation perspective, the constrained computational resources
onboard UAV platforms necessitate stringent requirements for both real-time perfor-
mance and computational eﬃciency in control algorithms. Current mainstream control
methods typically employ ﬁxed-frequency time-triggered mechanisms, which, while
simple to implement, incur signiﬁcant unnecessary computational and communication
overhead during periods of stable ﬂight conditions.
Event-triggered control (ETC) has emerged as an innovative control strategy and
gained signiﬁcant attention in the ﬁeld of UAVs [13–15]. Unlike conventional time-
triggered control (TTC), which operates with ﬁxed sampling intervals and oﬀers
straightforward implementation, ETC presents a more resource-eﬃcient alternative
particularly valuable for systems with limited computational and communication capa-
bilities. Rather than executing control updates periodically, this approach dynamically
determines update instants based on real-time system state evaluations. Importantly,
these eﬃciency improvements are achieved while maintaining guaranteed closed-
loop stability, thereby optimizing resource utilization without compromising system
performance [16, 17].
Active disturbance rejection control (ADRC), developed by Han in the 1990s [18],
employs an extended state observer (ESO) to estimate and compensate disturbances
in real time. Unlike conventional methods, ADRC requires no precise system model
and demonstrates exceptional robustness and disturbance rejection capabilities.
2

## Page 4

Recent years have seen remarkable progress in ADRC theory. The observer design
has evolved from nonlinear to linear ESO [19, 20] for easier tuning, with advanced
variants like adaptive [21, 22], fuzzy [23, 24] and neural network [25] ESOs achieving
better disturbance estimation. Researchers have also developed hybrid approaches by
integrating ADRC with SMC [26], MPC [27] and adaptive control [28], signiﬁcantly
enhancing system performance. Furthermore, intelligent parameter tuning methods
using grey wolf optimization [29] and reinforcement learning [30] have greatly improved
practicality in real-world applications of ADRC.
This study focuses on the trajectory tracking control of quadrotor UAVs, with the
main research contents outlined as follows:
1. A cascaded active disturbance rejection control (CADRC) scheme is proposed,
where the system is decoupled into position and velocity subsystems. Separate ESOs
and controllers are designed for each subsystem.
2. A hybrid event-triggering mechanism incorporating both static and dynamic
thresholds is developed. This approach enables system state and control command
updates only at triggered instants, signiﬁcantly reducing computational resource
consumption.
3. To enhance control system adaptability, an online self-tuning method based on
particle swarm optimization (PSO) is introduced for automatic controller parameter
adjustment.
2 Modeling
Quadrotor UAVs represent a typical underactuated and strongly coupled nonlinear
system. Accurate modeling of such systems forms the basis for eﬀective control. To
accurately characterize the motion of quadrotor, the system structure is illustrated in
Fig. 1.
Two coordinate systems are established: the body-ﬁxed frame B(Ob, Xb, Yb, Zb)
and the inertial frame E(Oe, Xe, Ye, Ze). During quadrotor motion, the inertial frame
remains stationary as an absolute reference. The body-ﬁxed frame varies with changes
in quadrotor attitude. The inertial frame facilitates intuitive description of kinematic
states such as UAV position and velocity. Conversely, the body-ﬁxed frame proves more
suitable for analyzing dynamic eﬀects including aerodynamic forces and propulsion
moments. Coordinate vector transformations between these frames are implemented
through rotation matrices. These matrices are typically computed following the con-
ventional sequence: yaw ﬁrst, then pitch, and ﬁnally roll. The rotation matrices for
yaw angle ψ, pitch angle θ, and roll angle ϕ are respectively given by:
Rψ =


cos ψ −sin ψ 0
sin ψ
cos ψ
0
0
0
1

, Rθ =


cos θ
0 sin θ
0
1
0
−sin θ 0 cos θ

, Rϕ =


1
0
0
0 cos ϕ −sin ϕ
0 sin ϕ
cos ϕ


(1)
The transformation matrix from the body-ﬁxed frame B to the inertial frame E,
denoted as RB−E, can be derived by exploiting the orthogonality property of rotation
3

## Page 5

matrices:
RB−E = RT
E−B = (Rϕ · Rθ · Rψ)T
=


cos ψ cos θ cos ψ sin θ sin ϕ −sin ψ cos ϕ cos ψ sin θ cos ϕ + sin ψ sin ϕ
sin ψ cos θ sin ψ sin θ sin ϕ + cos ψ cos ϕ sin ψ sin θ cos ϕ −cos ψ sin ϕ
−sin θ
cos θ sin ϕ
cos θ cos ϕ


(2)
Fig. 1 Structure diagram of the Quadrotor.
In the modeling process, the following assumptions are adopted:
Assumption 1. The quadrotor UAV is modeled as a rigid body, neglecting elastic
deformation during ﬂight.
Assumption 2. The quadrotor UAV is considered a symmetric rigid body with
uniformly distributed mass, where the center of gravity coincides with the origin of
the body-ﬁxed frame.
The gravitational force acting on the quadrotor in the inertial frame is expressed
as:
Me =

0 0 Mg
T
(3)
where M denotes the total mass of the quadrotor airframe, and g represents the
gravitational acceleration constant.
The lift force acting on the quadrotor in the body-ﬁxed frame is given by:
Fb =

0 0 Fl
T =
"
0
0
4
X
i=1
Fi
#T
(4)
where Fl denotes the total lift force generated by all rotors, and Fi(i = 1, . . . , 4)
represents the individual lift force produced by the ith rotor.
4

## Page 6

By combining Eq. (2) and (4), the expression of the lift force in the inertial frame
can be derived as:
Fe =

Fx Fy Fz
T = RB−EFb = Fl


cos ψ sin θ cos ϕ + sin ψ sin ϕ
sin ψ sin θ cos ϕ −cos ψ sin ϕ
cos θ cos ϕ


(5)
During ﬂight, the aerodynamic drag acting on the quadrotor can be expressed in
the following form:
Fa =

ka ˙x ka ˙y ka ˙z
T
(6)
where ka denotes the aerodynamic drag coeﬃcient.
For the quadrotor system, the moment expression is formulated as:
τ =


τx
τy
τz

=


l(−F1 + F2 + F3 −F4)/
√
2
l(F1 + F2 −F3 −F4)/
√
2
kc(F1 −F2 + F3 −F4)


(7)
where l represents the length of the rotor arms, and kc denotes the moment
coeﬃcient.
Based on Assumption 2, the moment of inertia matrix of the unloaded quadrotor
can be derived as:
J =


Jx 0
0
0 Jy 0
0
0 Jz


(8)
The dynamic model of the quadrotor UAV is derived as:
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
¨x = (Fx −ka ˙x) /M
¨y = (Fy −ka ˙y) /M
¨z = (Fz −ka ˙z) /M −g
¨ϕ = τx/Jx + ˙θ ˙ψ (Jy −Jz) /Jx
¨θ = τy/Jy + ˙ϕ ˙ψ (Jz −Jx) /Jy
¨ψ = τz/Jz + ˙ϕ ˙θ (Jx −Jy) /Jz
(9)
By introducing virtual control variables U1, U2, U3, U4 in the control system,
deﬁned as:

U1 U2 U3 U4
T =

Fl τx τy τz
T
(10)
and combining with Eq. (4) and (7), the control input of the UAV can be derived as:


U1
U2
U3
U4

=


Fl
τx
τy
τz

=


1
1
1
1
−l
√
2
l
√
2
l
√
2
−l
√
2
l
√
2
l
√
2 −l
√
2 −l
√
2
kc
−kc
kc
−kc




F1
F2
F3
F4


(11)
5

## Page 7

By combining Eq. (9) and (11), the control model for the quadrotor UAV with
variable payload can be derived as:
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
¨x = [U1(cos ψ sin θ cos ϕ + sin ψ sin ϕ) −ka ˙x] /M
¨y = [U1(sin ψ sin θ cos ϕ −cos ψ sin ϕ) −ka ˙y] /M
¨z = [U1(cos θ cos ϕ) −ka ˙z] /M −g
¨ϕ = U2/Jx + ˙θ ˙ψ (Jy −Jz) /Jx
¨θ = U3/Jy + ˙ϕ ˙ψ (Jz −Jx) /Jy
¨ψ = U4/Jz + ˙ϕ ˙θ (Jx −Jy) /Jz
(12)
3 Controller Design
3.1 Cascade ADRC Design with Event-Triggered Mechanism
Due to the physical structure of quadrotor, the control system is decoupled into an
outer-loop position control and an inner-loop attitude control, with the controller
architecture illustrated in Fig. 2.
Position control is achieved indirectly through attitude adjustment of the UAV.
The system implements three sub-controllers in both the position and attitude loops,
with parameters optimized via PSO. To address the motion characteristics of quadro-
tor, the sub-controllers are further stratiﬁed into position controllers and velocity
controllers, constructing a CADRC controller.
Fig. 2 A dual-loop CADRC framework based on event-triggered mechanism for the quadrotor.
Taking the altitude channel Z as an example, by introducing a new virtual control
variable hz = z2, the dynamic relationship can be reformulated as:
Position Subsystem: Sz1 : ˙χz1 = hz + ωz1;
Velocity Subsystem: Sz2 : ˙χz2 = Uz + ωz2
where ωz1 and ωz2 represent the disturbances and system nonlinearities in the two
subsystems, respectively.
The design of CADRC comprises two key steps:
6

## Page 8

Step 1: For the subsystem Sz1, the ESO can be formulated as:
 ˙ˆαz1 = ˆαz2 + hz + lz1 (ρz1 −ˆαz1)
˙ˆαz2 = lz2 (ρz1 −ˆαz1)
(13)
where bαzi(i = 1, 2) are estimates of the state variable αzi(i = 1, 2), and the design
of the observer gain lzi(i = 1, 2) is required to satisfy the matrix Az1 =

−lz1 1
−lz2 0

being
a Hurwitz matrix. The variable ρz1 represents the sampled value of system state z1(t)
at the event triggering instant tz1
p
for observer (13). This value serves as the state
estimate for the current control cycle.
The event-triggering mechanism for this observer is designed as follows:

ρz1(t) = z1
tz1
p

, t ∈

tz1
p , tz1
p+1

tz1
p+1 = inf

t > tz1
p ||z1(t) −ρz1(t)| > γz1
	
(14)
The virtual control variable hz is designed as follows:
hz = kz1(zd −ˆαz1) −ˆαz2
(15)
where kz1 represents the tunable controller parameter.
Step 2: For the subsystem Sz2, the ESO can be formulated as:



˙ˆβz1 = ˆβz2 + σz + lz3

ρz2 −ˆβz1

˙ˆβz2 = lz4

ρz2 −ˆβz1

(16)
where bβzi(i = 1, 2) denotes the estimated values of the state variables βzi(i = 1, 2).
The observer gains lzi(i = 3, 4) must be designed such that the matrix Az2 =

−lz3 1
−lz4 0

is Hurwitz. The variable ρz2 represents the sampled value of system state z2(t) at the
event-triggering instant tz2
p for observer (16).
The event-triggering mechanism for this observer is designed as follows:

ρz2(t) = z2
tz2
p

, t ∈

tz2
p , tz2
p+1

tz2
p+1 = inf

t > tz2
p ||z2(t) −ρz2(t)| > γz2
	
(17)
The observer triggering thresholds γz1 and γz2 are designed as ﬁxed values.
The virtual control variable Uz is derived through the following design formulation:
Uz = kz2

hz −ˆβz1

−ˆβz2
(18)
where kz2 denotes the tunable controller gain.
The control design for the x and y channels in the position controller follows a
similar approach to the Z channel. In these channels, the control variables Ux and Uy
are computed by the controller based on the desired displacement values xd and yd.
7

## Page 9

In the position controller, the sampled values of virtual control variables Ux, Uy,
Uz and yaw angle ψ at the event-triggering instant tψ
p are utilized to compute the
desired roll and pitch angles ϕd, θd and The control variable U1:
ϕd = arctan
 
cos θ
tθ
q
 Ux sin ψ
tψ
p

−Uy cos ψ
tψ
p

Uz
!
(19)
θd = arctan
 
Ux cos ψ
tψ
p

+ Uy sin ψ
tψ
p

Uz
!
(20)
U1 =
Uz
cos ϕ

tϕ
q

cos θ
tθq

(21)
The variables σx, σy, and σz are computed based on the sampled values of con-
trol variable U1(t). The event-triggering mechanism for this controller is designed as
follows:
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
σ1(t) = U1(τ 1
q ), t ∈[τ 1
q , τ 1
q+1)
σx(t) = σ1(t)
cos ψ
tψ
p

sin θ
tθ
p

cos ϕ
tϕ
p

+ sin ψ
tψ
p

sin ϕ
tϕ
p

σy(t) = σ1(t)
sin ψ
tψ
p

sin θ
tθ
p

cos ϕ
tϕ
p

−cos ψ
tψ
p

sin ϕ
tϕ
p

σz(t) = σ1(t) cos ϕ
tϕ
p

cos θ
tθ
p

τ 1
q+1 = inf
n
t > τ 1
q ||U1(t) −σ1(t)| > M 1
1 e−M 1
2 ˆet
o
(22)
where M 1
1 represents the threshold extremum factor and M 1
2 denotes the error
sensitivity factor. The controller triggering threshold is determined by the trajectory
estimation error ˆet through the following relation:
ˆet =
q
(ˆαx1 −xd)2 + (ˆαy1 −yd)2 + (ˆαz1 −zd)2
(23)
Remark 1. For quadrotor systems exhibiting strong coupling dynamics, the
tracking error should be evaluated as a three-dimensional trajectory deviation. The
event-triggered mechanism prevents real-time state measurements in Eq. (23). The
ESO estimates are consequently employed for both event-triggering conditions (14),
(17) and trajectory tracking error computation.
The attitude channel control design follows a similar approach to the position chan-
nel. The controller event-triggering mechanism diﬀers slightly from Eq. (22). Taking
the roll channel as an example, its event-triggering mechanism is formulated as:
(
σ2(t) = U2
τ 2
q

, t ∈

τ 2
q , τ 2
q+1

τ 2
q+1 = inf
n
t > τ 2
q ||U2(t) −σ2(t)| > M 2
1 e−M 2
2 |ˆαϕ1−ϕd|o
(24)
8

## Page 10

3.2 Online Self-Tuning of CADRC Parameters based on
Particle Swarm Optimization
The Particle Swarm Optimization (PSO) algorithm ﬁnds optimal solutions by simulat-
ing collective behaviors observed in biological groups such as bird ﬂocks or ﬁsh schools.
This study develops an ADRC strategy with online parameter self-tuning based on
PSO. The cascade subcontroller requires tuning for six parameters [l1, l2, l3, l4, k1, k2],
while the complete quadrotor control system involves 36 tunable parameters in total.
Introducing observer bandwidth and controller bandwidth simpliﬁes the parameter
tuning process. The controller parameters can be systematically determined through
the following bandwidth-based relationships:
l1 = ω2
o1, l2 = 2ωo1, l3 = ω2
o2, l4 = 2ωo2, k1 = ω2
c, k2 = 2ωc
(25)
In both attitude and position controllers, the sub-controllers exhibit control
objectives of comparable magnitude. Consequently, identical parameter sets can be
employed for both attitude and position control. This simpliﬁcation reduces the total
number of tunable parameters from thirty-six to six, with three parameters allocated
for attitude control and three for position control, while maintaining guaranteed con-
trol eﬀectiveness. The parameters to be adjusted are [ωoa1, ωoa2, ωca, ωop1, ωop2, ωcp].
Remark 2. During the controller parameter tuning process, the quadrotor cannot
derive displacement control inputs directly from the reference trajectory, but requires
indirect adjustment through desired attitude values. The six controllers function as
a coupled system when acting on the controlled plant, which inherently constrains
individual sub-controller tuning.
In the PSO, each particle maintains its own position and velocity vectors, which
are updated according to the following rules:
V t+1
i
= wV t
i + c1r1
Pbesti −Xt
i

+ c2r2
Gbest −Xt
i

(26)
Xt+1
i
= Xt
i + V t+1
i
(27)
where i indexes particles in the swarm, V t
i and Xt
i denote the velocity and posi-
tion of particle i at iteration t. Each particle tracks its historical best position Pbesti,
while Gbest represents the global optimum. The algorithm employs an inertia weight
w, acceleration constants c1 and c2, along with uniformly distributed random num-
bers r1, r2 ∈[0, 1]. Through iterative updates of these particle states, the algorithm
eﬃciently explores the solution space.
In the PSO algorithm, adjusting the inertia weight w enables appropriate solutions
for diﬀerent optimization problems. Typically, larger w values facilitate global explo-
ration, allowing particles to search broader regions of the solution space. Conversely,
smaller w values emphasize local reﬁnement, promoting faster convergence toward
optimal solutions. This study implements a linear decreasing inertia weight strategy
to dynamically adjust w, with the update rule formulated as:
w = wini −
t
tmax
(wini −wfin)
(28)
9

## Page 11

where wini and wfin denote the initial and ﬁnal values of the inertia weight,
respectively, while tmax speciﬁes the maximum number of iterations.
The ﬁtness function directly determines optimization eﬀectiveness by quantita-
tively evaluating particle quality. While an overly complex design may reduce iteration
counts, the computational overhead can compromise overall eﬃciency. Therefore,
ﬁtness function design must balance guidance capability with computational eﬃciency.
For trajectory tracking objectives, the tracking error between the quadrotor and
its reference trajectory serves as the key performance metric. For quadrotor systems
operating in three-dimensional space, the trajectory tracking error is mathematically
deﬁned as:
eq =
q
(x −xd)2 + (y −yd)2 + (z −zd)2
(29)
In quadrotor ﬂight control, attitude stability and trajectory tracking accuracy hold
equal importance. To quantitatively evaluate oscillation severity in attitude angles,
this study employs standard deviation as the performance metric. Taking the roll angle
ϕ as an example, its standard deviation is computed as:
sϕ =
v
u
u
t 1
n
n
X
i=1
ϕi −ϕ
2
(30)
where n denotes the sample size and ¯ϕ represents the sample mean.
The ﬁtness function designed in this study is formulated as:
Y = a
Z t
0
τeq(τ)dτ + b (sϕ + sθ + sψ)
(31)
where a and b represent positive weighting coeﬃcients, and sϕ, sθ, and sψ denote the
standard deviations of roll, pitch, and yaw angles, respectively. The function design
incorporates time as an error weighting factor. Under this formulation, the ﬁtness
function output Y exhibits an inverse correlation with controller performance–lower
Y values indicate superior control eﬀectiveness.
Remark 3. Quadrotors require ﬂight control systems that simultaneously sat-
isfy both trajectory tracking precision and attitude stability requirements. Simulation
results demonstrate that omitting attitude angle constraints in the ﬁtness func-
tion design leads to rapid trajectory convergence at the expense of pronounced
high-frequency attitude oscillations, ultimately degrading actual ﬂight performance.
To enable online self-tuning via the PSO algorithm, the following event-triggering
mechanism is implemented:



ω(·) = ωoa, ωca, ωop, ωcp
ω(·)(t) = ω(·)(tp), t ∈[tp, tp+1)
tp+1 = inf {t > tp + ¯t|eq(t) > γp}
(32)
where tp denotes the triggering instant for parameter adaptation, while tp+1 rep-
resents the subsequent triggering instant. The minimum triggering interval ¯t and
10

## Page 12

designed constant threshold γp collectively prevent Zeno behavior through enforced
time separation.
The integration of PSO for online parameter tuning in CADRC proceeds through
the following steps:
Step 1: Initialize the particle swarm when either ﬁrst-time operation occurs,
or tracking error exceeds the threshold while maintaining the minimum triggering
interval;
Step 2: Execute PSO to determine globally optimal parameters through iterative
computation;
Step 3: Update controller parameters and compute real-time tracking error.
4 Stability Analysis
4.1 Convergence Analysis of the Cascade Extended State
Observer
The estimation error of the Cascade Extended State Observer (CESO) is formally
deﬁned as ˜αi = αi −bαi, ˜βi = βi −bβi, (i = 1, 2). Combining Eqs. (13) and (16), the
dynamics of the estimation error system can be derived as:
 ˙˜α1 = ˙α1 −˙ˆα1 = −l1 ˜α1 + ˜α2 −l1 (ρ1 −α1)
˙˜α2 = ˙α2 −˙ˆα2 = −l2 ˜α1 + ˙ω1 −l2 (ρ1 −α1)
(33)
( ˙˜β1 = ˙β1 −˙ˆβ1 = −l3 ˜β1 + ˜β2 −l3 (ρ2 −β1)
˙˜β2 = ˙β2 −˙ˆβ2 = −l4 ˜β1 + ˙ω2 −l4 (ρ2 −β1)
(34)
Deﬁne δ1 = ρ1 −α1, δ2 = ρ2 −β1. The system (33), (34) can be written as:
( ˙˜α = A1 ˜α −B1δ1 + B3 ˙ω1
˙˜β = A2 ˜β −B2δ2 + B3 ˙ω2
(35)
where:
˙˜α =
 ˙˜α1
˙˜α2

, ˙˜β =
" ˙˜β1
˙˜β2
#
, A1 =

−l1 1
−l2 0

, A2 =

−l3 1
−l4 0

B1 =

l1
l2

, B2 =

l3
l4

, B3 =

0
1

Before proceeding with the proof, we state the following assumption:
Assumption 3. All external disturbances and unmodeled dynamics, along with
their time derivatives, are uniformly bounded. Speciﬁcally, there exist positive
constants ˙ωi > 0 such that ∥˙ωi∥≤˙ωi.
Theorem 1. Consider the quadrotor system (12), equipped with the ESOs (13),
(16) and event-triggered mechanisms (14), (17). There exist observer gains li(i =
1, 2, 3, 4) such that all estimation errors converge to an arbitrarily small compact set.
11

## Page 13

Proof. For the coupled estimation error dynamics of the quadrotor system,
consider the composite Lyapunov function:
V1 = ˜αT P1 ˜α + ˜βT P2 ˜β
(36)
The matrices P1 and P2 are symmetric positive-deﬁnite and satisfy AT
i Pi +PiAi =
−I(i = 1, 2). The time derivative of V1 is:
˙V1 = ˙˜αT P1 ˜α + ˜αT P1 ˙˜α + ˙˜βT P2 ˜β + ˜βT P2 ˙˜β
= (A1 ˜α −B1δ1 + B3 ˙ω1)T P1 ˜α + ˜αT P1(A1 ˜α −B1δ1 + B3 ˙ω1)
+ (A2 ˜β −B2δ2 + B3 ˙ω2)T P2 ˜β + ˜βT P2(A2 ˜β −B2δ2 + B3 ˙ω2)
= ˜αT (AT
1 P1 + P1A1)˜α −2˜αT P1B1δ1 + 2˜αT P1B3 ˙ω1
+ ˜βT (AT
2 P2 + P2A2)˜β −2˜βT P2B2δ2 + 2˜βT P2B3 ˙ω2
(37)
Given that | ˙ωi| ≤˙ωi and the triggering condition enforces δi ≤γi(i = 1, 2), Eq.
(37) can be derived:
˙V1 ≤−∥˜α∥2 + 2∥˜α∥
∥P1B3∥˙ω1 −∥P1B1∥γ1

−∥˜β∥2 + 2∥˜β∥
∥P2B3∥˙ω2 −∥P2B2∥γ2

(38)
Let:
c1 = ∥P1B3∥ω1 −∥P1B1∥γ1
c2 = ∥P2B3∥ω2 −∥P2B2∥γ2
When the errors satisfy ∥˜α∥> c1 and ∥˜β∥> c2, the ˙V1 fulﬁlls ˙V1 ≤0, indicating
convergence of the ESO estimation errors. The errors ˜α and ˜β are uniformly ultimately
bounded. Their convergence thresholds can be arbitrarily adjusted by properly tuning
the observer gains li(i = 1, 2, 3, 4), allowing the error bounds to be constrained within
any prescribed compact set.
4.2 Stability Analysis of Control Systems
Assumption 4. The reference signal v and its derivative ˙v are bounded.
Let v1 and v2 represent v and ˙v, respectively. The controller tracking errors are
deﬁned as e1 = α1 −v1 and e2 = β1 −h. By combining Eqs. (15), (18) with the
estimation error dynamics, the tracking error system dynamics can be derived as
follows:
˙e1 = ˙α2 −v2 = α2 + h −v2
= k1(v1 −ˆα1) + v2 −ˆα2 + α2 −v2
= −k1e1 + k1 ˜α1 + ˜α2
(39)
˙e2 = ˙β2 −˙h = β2 + σ −˙h
= k2

h −ˆβ1

+ h −ˆβ2 + β2 −˙h + [U (τq) −U(t)]
= −k2e2 + k2 ˜β1 + ˜β2 + [U (τq) −U(t)]
(40)
12

## Page 14

where [U(τq) −U(t)] represents the error introduced by the event-triggered
mechanism of the controller.
Theorem 2. Consider the quadrotor system described by Eq. (12), equipped with
the controller (18) and subject to event-triggered mechanisms (22) and (24). There
exist controller gains k1 and k2 that guarantee bounded tracking errors.
Proof. The Lyapunov function is deﬁned as:
V2 = 1
2e2
1 + 1
2e2
2
(41)
The time derivative is given by:
˙V2 = e1 ˙e1 + e2 ˙e2
= e1 (−k1e1 + k1 ˜α1 + ˜α2) + e2

−k2e2 + k2 ˜β1 + ˜β2 + [U (τq) −U(t)]

= −k1e2
1 + k1e1 ˜α1 + e1 ˜α2 −k2e2
2 + k2e2 ˜β1 + e2 ˜β2 + e2 [U (τq) −U(t)]
(42)
By applying Young’s inequality, we obtain:
k1e1 ˜α1 ≤v1e2
1
2
+ k2
1 ˜α2
1
2v1
,
e1 ˜α2 ≤v2e2
1
2
+ ˜α2
2
2v2
k2e2 ˜β1 ≤v3e2
2
2
+ k2
2 ˜β2
1
2v3
,
e2 ˜β2 ≤v4e2
2
2
+
˜β2
2
2v4
e2 [U (τq) −U(t)] ≤v5e2
2
2
+ [U (τq) −U(t)]2
2v5
(43)
where vi(i = 1, · · · , 5) are positive constants. Substituting Eq. (43) into (42) yields:
˙V2 = −κ1e2
1 −κ2e2
2 + Π
(44)
where:
κ1 = k1 −v1
2 −v2
2
κ2 = k2 −v3
2 −v4
2 −v5
2
Π = k2
1 ˜α2
1
2v1
+ ˜α2
2
2v2
+ k2
2 ˜β2
1
2v3
+
˜β2
2
2v4
+ [U (τq) −U(t)]2
2v5
(45)
Theorem 1 guarantees the boundedness of the state variables ˜α and ˜β. Furthermore,
by design of the event-triggering mechanisms, [U(τq) −U(t)] is bounded. Through
proper selection of control gains k1 and k2 to ensure κ1 > 0 and κ2 > 0, all track-
ing errors are uniformly ultimately bounded, and the closed-loop system achieves
asymptotic stability.
4.3 Analysis of the Zeno Phenomenon
The Zeno phenomenon, which refers to the occurrence of inﬁnitely many triggering
events within a ﬁnite time interval, must be rigorously excluded in the proposed ETC
13

## Page 15

scheme. Since both the observer and controller incorporate event-triggered mecha-
nisms, a formal proof is required to demonstrate that the designed triggering conditions
prevent Zeno behavior.
Theorem 3. For the quadrotor system described by Eq. (12) with event-triggering
mechanisms (14), (17), (22), and (24), there exist strictly positive parameters that
guarantee the exclusion of Zeno behavior in the closed-loop system.
Proof. For the event-triggered mechanism in the observation channel, the trig-
gering mechanisms for velocity and position states follow similar designs. Taking the
z-axis as an example, the actual system output z1(t) is diﬀerentiable and satisﬁes
| ˙z1(t)| ≤L, where L is a ﬁnite positive constant. Let ∆t1 = t−tz1
p . Then, the following
holds:
|z1(t) −z1(tz1
p )| ≤L∆t1
(46)
When the event-triggering mechanism is satisﬁed, the following holds:
z1(t) −z1
tz1
p
 > γz1
(47)
Consequently, it can be derived that:
L∆t1 > γz1
∆t1 > γz1
L = ι1
(48)
The event-triggering mechanism guarantees a strictly positive minimum inter-event
interval, denoted by ι1, which ensures the exclusion of Zeno behavior in the observer’s
event-triggered scheme.
For the event-triggering mechanism of control channel, consider U2 as an example.
The controller output is diﬀerentiable and satisﬁes | ˙U2(t)| ≤K, where K is a ﬁnite
positive constant. Let ∆t2 = t −τ 2
q . Then, the following results hold:
U2(t) −U2
τ 2
q
 ≤K∆t2
(49)
When the event-triggering mechanism is met, the following holds:
U2(t) −U2
τ 2
q
 > M 2
1 e−M 2
2 |ˆαϕ1−ϕd|
(50)
Thus, we obtain the following result:
K∆t2 > M 2
1 e−M 2
2 |ˆαϕ1−ϕd|
∆t2 > M 2
1
K e−M 2
2 |ˆαϕ1−ϕd| = ι2
(51)
By Theorems 1 and 2, the term |bαϕ1 −ϕd| is bounded, and consequently
e−M 2
2 |bαϕ1−ϕd| remains bounded. This guarantees the existence of a strictly positive
minimum inter-event interval ι2, which precludes Zeno behavior in the event-triggered
mechanism of controller.
14

## Page 16

5 Simulation Experiments
The eﬀectiveness and robustness of the proposed CADRC approach were veriﬁed
through MATLAB simulations, with a conventional ADRC controller serving as the
baseline for comparison. The simulation was conﬁgured with a 20-second duration and
a ﬁxed step size of 0.01 seconds. The quadrotor’s initial position and attitude were set
to zero values [ x y z ϕ θ ψ ]T = [ 0 0 0 0 0 0 ]T . The parameter conﬁgurations for
the quadrotor system, PSO algorithm, and event-triggered mechanism are presented
in Table 1.
The drone executes a simpliﬁed urban patrol mission comprising four phases (total
duration: 20 seconds) before returning to its origin:
Phase 1 (t ≤5 s): Simultaneous constant-velocity ﬂight along x and z axes at 3
m/s each.
Phase 2 (5 s << t ≤10 s): Constant-velocity ﬂight along y-axis at 3 m/s.
Phase 3 (10 s << t ≤15 s): Reverse constant-velocity ﬂight along x-axis at -3 m/s.
Phase 4 (15 s << t ≤20 s): Reverse constant-velocity ﬂight along y-axis at -3 m/s.
With the desired yaw angle ψd = 0◦maintained throughout, the quadrotor com-
pletes this rectangular trajectory cycle while tracking the prescribed path. The system
incorporates zero-mean Gaussian noise with a standard deviation of 1 as external
disturbances in both the attitude and position control channels.
Table 1 The parameters for the quadrotor system, particle swarm optimization algorithm (PSO),
and event-triggered mechanism.
Quadrotor System
PSO
Event-Triggered Mechanism
Notation
Value
Notation
Value
Notation
Value
M
2.5 (kg)
n
50
γ1
0.01
l
0.6 (m)
d
4
γ2
0.03
g
9.8 (m/s2)
wini
0.8
M 1
1
5
kc
0.06 (N·m/m2)
wfin
0.2
M 2
1 /M 3
1
1000
ka
0.02 (N·m/m2)
c1/c2
2
M 4
1
10
Jx
1.4 (kg·m2)
max iter
15
M2
10
Jy
1.4 (kg·m2)
γp
0.15
Jz
2.8 (kg·m2)
t
2
15

## Page 17

Fig. 3 Quadrotor 3D trajectory tracking.
Figure 3 presents the 3D trajectory tracking performance of the quadrotor during
the simpliﬁed urban patrol mission. The simulation results demonstrate eﬀective track-
ing of the predeﬁned rectangular trajectory across all four ﬂight phases. A comparative
analysis between the CADRC and conventional ADRC methods reveals superior tra-
jectory adherence during transitional phases where motion direction changes occur,
with the proposed CADRC algorithm exhibiting closer alignment to the desired path.
Notably, the CADRC controller maintains high tracking precision even under sensor
noise conditions, thereby validating the robustness of the control strategy.
Fig. 4 The trajectory tracking errors of the quadrotor.
Figure 4 presents the trajectory tracking error characteristics of the quadrotor
UAV. A comparative analysis of the error curves between the ADRC and CADRC con-
trol strategies reveals that, consistent with the results shown in Figure 3, the CADRC
16

## Page 18

controller demonstrates superior transient response performance during trajectory
switching phases. Speciﬁcally, the CADRC generates smaller overshoot compared to
the conventional ADRC controller while maintaining consistently lower tracking errors
throughout the entire control process. The proposed CADRC method achieves a 65.3%
reduction in root-mean-square (RMS) error compared to conventional ADRC, with
measured values of 0.092 versus 0.265 respectively. This quantiﬁes the superior tracking
precision of the cascaded event-triggered architecture.
Fig. 5 The event-triggered instant of PSO algorithm.
As shown in Figure 5, the PSO algorithm triggered parameter adjustments at ﬁve
distinct time instants: initial startup (t = 0 s), t = 2.02 s, t = 5.09 s, t = 10.08 s,
and t = 15.08 s. These parameter updates were activated when abrupt transitions in
the quadrotor’s reference trajectory caused instantaneous increases in tracking error,
thereby satisfying the event-triggering conditions.
Fig. 6 The instant and sampled error of the observation event triggering mechanism.
Taking the displacement along the x-axis as an example, we analyze the event-
triggered mechanism of observer. Figure 6 illustrates both the triggering instants and
corresponding thresholds for the x-axis observation channel. The results demonstrate
that the observer performs state sampling and data transmission only when the sam-
pling error between measured and actual values exceeds the predeﬁned threshold.
Compared to continuous triggering approaches, this event-triggered strategy achieves
a 43.45% reduction in data transmission frequency.
17

## Page 19

Fig. 7 The instant and sampled error of the control event triggering mechanism.
Figure 7 presents the event-triggering instants and corresponding thresholds
for control input U1. When correlated with the error curves in Figure 4, a clear
adaptive thresholding strategy emerges: the triggering threshold decreases during peri-
ods of larger tracking errors to prioritize control accuracy, while adopting higher
thresholds when errors diminish to reduce triggering frequency. This time-varying
event-triggered mechanism achieves a 84.05% reduction in data transmission compared
to ﬁxed-threshold approaches.
The simulation results demonstrate that the event-triggered CADRC approach out-
performs conventional ADRC in both trajectory tracking precision and computational
eﬃciency. The cascaded control structure eﬀectively decouples position and velocity
regulation, while the event-triggering mechanism signiﬁcantly reduces system resource
utilization without compromising performance. Furthermore, the PSO-based online
parameter tuning enhances the controller’s adaptability to external disturbances.
6 Conclusion
This study addresses the trajectory tracking control problem for quadrotor by propos-
ing a CADRC method with event-triggered mechanisms. Through hierarchical system
design, we independently construct ESOs and controllers for both position and velocity
subsystems, achieving precise disturbance estimation and compensation while enhanc-
ing control accuracy. The incorporation of event-triggered mechanisms ensures system
state and control signal updates only when necessary. Simulation results demon-
strate signiﬁcant reductions in data transmission volume for both observation and
control channels, substantially lowering computational resource consumption without
compromising performance.
Compared to conventional ADRC, the cascaded structure of CADRC exhibits
stronger robustness against dynamic payload variations and external disturbances.
Furthermore, the online parameter tuning via PSO enhances the controller’s adaptive
capability, enabling rapid adjustment to system parameter changes. Theoretical anal-
ysis conﬁrms the method’s stability and guarantees the absence of Zeno behavior in
the event-triggered mechanism.
18

## Page 20

Future work will investigate fault-tolerant control strategies for actuator failures
during ﬂight. We plan to integrate fault detection and diagnosis techniques into the
quadrotor system to improve operational reliability during mission execution.
Acknowledgements
This work is supported by Science and Technology Project of State Grid Qinghai
Electric Power Company (QHKJ-05-25-02).
Data Availability
The datasets generated during and/or analyzed during the current study are available
from the corresponding author on reasonable request.
Author Contributions
Xin Chen:Xin Chen conceptualized the cascade active disturbance rejection control
(CADRC) framework integrated with the event-triggered mechanism. He designed
the hierarchical control architecture, formulated the theoretical foundation, and
drafted the manuscript.Kai Chen:Kai Chen implemented the simulation platform
using MATLAB, developing the software for control algorithms and performing for-
mal analysis of trajectory tracking performance. He validated the robustness of the
proposed method under external disturbances and contributed to data curation.Fuhua
Qiang:Fuhua Qiang derived the quadrotor dynamics model, decoupled the system into
position and velocity subsystems, and conducted parameter conﬁguration for simu-
lation experiments. He assisted in investigating the system’s response under varying
ﬂight conditions.Yongke Sun:Yongke Sun was responsible for visualization, gener-
ating key results such as 3D trajectory plots and error comparisons. He provided
computational resources and contributed to reviewing and editing the manuscript,
particularly in enhancing the clarity of graphical presentations.Xin Lai:Xin Lai super-
vised the research progress. He provided critical feedback during manuscript revision
and ensured alignment with industrial application requirements.
References
[1] Cai, K., Yu, H., He, W., Liang, X., Han, J., Fang, Y.: An enhanced-coupling
control method for aerial transportation systems with double-pendulum swing
eﬀects. IEEE/ASME Transactions on Mechatronics 29(3), 2302–2315 (2024)
https://doi.org/10.1109/TMECH.2023.3316423
[2] Jin, X., Che, W., Wu, Z., Deng, C.: Robust adaptive general formation control
of a class of networked quadrotor aircraft. IEEE Transactions on Systems, Man,
and Cybernetics: Systems 52(12), 7714–7726 (2022)
19

## Page 21

[3] Xiao, M., Liang, J., Ji, L., Sun, Z., Li, Z.: Aerial photography trajectory-tracking
controller design for quadrotor uav. Measurement and Control 55(7–8), 738–745
(2022) https://doi.org/10.1177/00202940221115634
[4] Zheng, L., Hamaza, S.: Albero: Agile landing on branches for environmental
robotics operations. IEEE Robotics and Automation Letters 9(3), 2845–2852
(2024) https://doi.org/10.1109/LRA.2024.3349914
[5] Lopez-Sanchez, I., Moreno-Valenzuela, J.: Pid control of quadrotor uavs: A survey.
Annual Reviews in Control 56, 100900 (2023)
[6] Zhang, H., Feng, Q.: Design and implementation of attitude control for quadrotor
uav based on adaptive fuzzy pid. In: 2022 41st Chinese Control Conference (CCC),
pp. 3533–3538 (2022). IEEE
[7] Lian, S., et al.: Adaptive attitude control of a quadrotor using fast nonsingular
terminal sliding mode. IEEE Trans. Ind. Electron. 69(2), 1597–1607 (2022) https:
//doi.org/10.1109/TIE.2021.3057015
[8] Pan, J., Shao, B., Xiong, J., Zhang, Q.: Attitude control of quadrotor uavs based
on adaptive sliding mode. International Journal of Control, Automation and
Systems 21(8), 2698–2707 (2023)
[9] Tan, L., Shen, Z., Yu, S.: Adaptive fault-tolerant ﬂight control for a quadrotor
uav with slung payload and varying cog. In: 2019 3rd International Symposium
on Autonomous Systems (ISAS), pp. 227–231 (2019). https://doi.org/10.1109/
ISASS.2019.8757704 . IEEE
[10] Nguyen, D.V., Zhao, H., Giang, L.N., Van Thuan, S., Hu, J.: A dual adaptive
control strategy for quadrotor uavs under model uncertainties and external sensor
disturbances. Journal of Electrical Engineering & Technology 20(3), 1775–1788
(2025)
[11] Jung, W., Bang, H.: Fault and failure tolerant model predictive control of quadro-
tor uav. International Journal of Aeronautical and Space Sciences 22(3), 663–675
(2021)
[12] Wang, D., Pan, Q., Shi, Y., Hu, J., Zhao, C.: Eﬃcient nonlinear model predic-
tive control for quadrotor trajectory tracking: Algorithms and experiment. IEEE
Transactions on Cybernetics 51(10), 5057–5068 (2021)
[13] Cao, C., Luo, Z., Zhao, Z.: Event-triggered adaptive control for quadrotor
unmanned aerial vehicle with prescribed performance. Transactions of the
Institute of Measurement and Control 46(16), 3073–3081 (2024)
[14] Zhu, C., Chen, J., Iwasaki, M., Zhang, H.: Event-triggered deep learning control
of quadrotors for trajectory tracking. IEEE Transactions on Industrial Electronics
20

## Page 22

71(3), 2726–2736 (2023)
[15] Xu, L.-X., Wang, Y.-L., Wang, F., Long, Y.: Event-triggered active disturbance
rejection trajectory tracking control for a quadrotor unmanned aerial vehicle.
Applied Mathematics and Computation 449, 127967 (2023)
[16] Han, Y., Li, J., Wang, B.: Event-triggered active disturbance rejection con-
trol for hybrid energy storage system in electric vehicle. IEEE Transactions on
Transportation Electriﬁcation 9(1), 75–86 (2022)
[17] Cao, Z., Niu, B., Zong, G., Zhao, X., Ahmad, A.M.: Active disturbance
rejection-based event-triggered bipartite consensus control for nonaﬃne nonlin-
ear multiagent systems. International Journal of Robust and Nonlinear Control
33(12), 7181–7203 (2023)
[18] Han, J.: From pid to active disturbance rejection control. IEEE Trans. Ind.
Electron. 56(3), 900–906 (2009) https://doi.org/10.1109/TIE.2008.2011621
[19] Gao, Z.: On the centrality of disturbance rejection in automatic control. ISA
transactions 53(4), 850–857 (2014)
[20] Chang, Y., Zhou, F., Yan, H., Huang, W., Luo, G.: Noise and interference sup-
pression control method of dc-dc buck converters based on cascaded ﬁlter ladrc.
International Journal of Control, Automation and Systems 22(5), 1526–1536
(2024)
[21] Lu, Y., Tan, C., Ge, W., Zhao, Y., Wang, G.: Adaptive disturbance observer-
based improved super-twisting sliding mode control for electromagnetic direct-
drive pump. Smart Materials and Structures 32(1), 017001 (2022)
[22] Peng, Z., Liu, L., Wang, J.: Output-feedback ﬂocking control of multiple
autonomous surface vehicles based on data-driven adaptive extended state
observers. IEEE Transactions on Cybernetics 51(9), 4611–4622 (2020)
[23] Prieto, P.J., Plata-Ante, C., Ram´ırez-Villalobos, R.: Fuzzy extended state
observer for the fault detection and identiﬁcation. ISA transactions 128, 11–20
(2022)
[24] Li, Z., Yan, H., Zhang, H., Wang, M., Zeng, L.: Generalized fuzzy extended state
observer design for uncertain nonlinear systems: An improved dynamic event-
triggered approach. IEEE Transactions on Fuzzy Systems 30(11), 4867–4875
(2022)
[25] He, T., Wu, Z.: Neural network disturbance observer with extended weight matrix
for spacecraft disturbance attenuation. Aerospace Science and Technology 126,
107572 (2022)
21

## Page 23

[26] Roman, R.-C., Precup, R.-E., Petriu, E.M.: Hybrid data-driven fuzzy active dis-
turbance rejection control for tower crane systems. European Journal of Control
58, 373–387 (2021) https://doi.org/10.1016/j.ejcon.2020.08.001
[27] Bekhouche, R., Khoucha, F., Benrabah, A., Benbouzid, M., Benmansour, K.:
An improved active disturbance rejection model predictive power control with
circulating current reduction for grid-connected modular multilevel converter.
Electric Power Components and Systems 49(15), 1212–1226 (2022)
[28] Tian, M., Wang, B., Yu, Y., Dong, Q., Xu, D.: Adaptive active disturbance
rejection control for uncertain current ripples suppression of pmsm drives. IEEE
Transactions on Industrial Electronics 71(3), 2320–2331 (2023)
[29] Ren, J., Chen, Z., Yang, Y., Sun, M., Sun, Q., Wang, Z.: Grey wolf optimiza-
tion based active disturbance rejection control parameter tuning for ship course.
International Journal of Control, Automation and Systems 20(3), 842–856 (2022)
[30] Wang, Y., Fang, S., Hu, J.: Active disturbance rejection control based on deep
reinforcement learning of pmsm for more electric aircraft. IEEE Trans. Power
Electron. 38(1), 406–416 (2023) https://doi.org/10.1109/TPEL.2022.3206089
22
