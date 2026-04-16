# Estimation_of_Unmodeled_Dynamics_Nonlinear_MPC_and_Adaptive_Control_Law_With_Momentum_Observer_Dynamic.pdf

## Page 1

Received 16 April 2024, accepted 27 May 2024, date of publication 30 May 2024, date of current version 6 June 2024.
Digital Object Identifier 10.1109/ACCESS.2024.3407684
Estimation of Unmodeled Dynamics: Nonlinear
MPC and Adaptive Control Law With
Momentum Observer Dynamic
BRYAN S. GUEVARA
1, LUIS F. RECALDE
2, VIVIANA MOYA
3,
JOSÉ VARELA-ALDÁS
2, (Member, IEEE), DANIEL C. GANDOLFO
1,
AND JUAN M. TOIBERO
1
1Instituto de Automática, Consejo Nacional de Investigaciones Científicas y Técnicas (CONICET), Universidad Nacional de San Juan, San Juan J5400, Argentina
2Centro de Investigación de Ciencias Humanas y de la Educación (CICHE), Universidad Indoamérica, Ambato 180103, Ecuador
3Facultad de Ciencias Técnicas, Universidad Internacional del Ecuador, Quito 170411, Ecuador
Corresponding author: José Varela-Aldás (josevarela@uti.edu.ec)
This work was supported in part by Universidad Indoamérica (UTI); in part by Universidad Internacional del Ecuador (UIDE); and in part
by the Instituto de Automática (INAUT), Consejo Nacional de Investigaciones Científicas y Técnicas (CONICET), Universidad Nacional
de San Juan (UNSJ).
ABSTRACT This article proposes an enhancement to estimate unmodeled dynamics within the simplified
dynamic model of a quadcopter by integrating three key methodologies: Nonlinear Model Predictive Control
(NMPC), a Momentum Observer Dynamics (MOD), and an adaptive control law. Termed as Adaptive NMPC
with MOD, this integrated approach leverages NMPC, implemented using the CasADi framework, for real-
time decision-making, while the momentum observer facilitates system state estimation and uncertainty
mitigation. Simultaneously, the adaptive control law adjusts parameters to estimate errors in unmodeled
dynamics. Through digital twin and Model in Loop (MiL) simulations, the effectiveness of this framework
is demonstrated. Specifically, the study focuses on the simplified quadcopter model, acknowledging often
overlooked inherent dynamics resulting from the simplification by not considering the nonlinearities induced
by the drone’s attitude angles. Addressing these unmodeled dynamics is critical, and the Adaptive NMPC
with MOD method emerges as a robust solution, showcasing its potential across various scenarios.
INDEX TERMS NMPC, adaptive control, disturbance estimation, UAV dynamics, momentum observer,
CasADi.
I. INTRODUCTION
S everal recent studies have demonstrated interest in devel-
oping advanced control algorithms for various applications
using unmanned aerial vehicles (UAV) due to their extensive
range of applications in different areas of compliance, such
as transportation and logistics, civil, maintenance, security,
and even military applications [1], [2]. One of the primary
uses of UAVs is in executing specific tasks such as following
a desired trajectory, position, and path tracking [3]. Thus,
it becomes necessary to program UAVs to follow a predeter-
mined path or to reach a specific location. This capability is
The associate editor coordinating the review of this manuscript and
approving it for publication was Ming Xu
.
crucial in many applications, such as surveying large areas of
land or delivering goods to a particular destination that may
be far away from the control center or pilot’s location [4].
Another significant area of interest is visual servo control
[5]. It involves using visual feedback information to control
the motion of the UAV. This technology proves useful when
the drone needs to interact with its environment, such as
in search and rescue operations and when capturing aerial
photos or videos [6]. It is also useful to detect points of
interest like gates to pass through, where tools using computer
vision and artificial intelligence have provided significant
development [7]. Obstacle avoidance control using artificial
intelligence is also a critical area of focus [8]. It uses AI
algorithms to enable the UAV to detect and avoid obstacles.
VOLUME 12, 2024
 2024 The Authors. This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.
For more information, see https://creativecommons.org/licenses/by-nc-nd/4.0/
77121

## Page 2

B. S. Guevara et al.: Estimation of Unmodeled Dynamics
This technique is particularly important in ensuring the safety
and reliability of UAV operations, especially in complex and
unpredictable environments [9]. Finally, formation control
of multiple UAVs is another exciting area of research [10].
This area involves coordinating the movement of a group of
UAVs to work together to achieve a common goal. Therefore,
it has potential applications in several areas, such as swarm
robotics, where a group of robots work together to perform
tasks that would be difficult or impossible for a single
robot to accomplish [11]. On the other hand, one of the
main challenges that come when working with UAVs in real
environments is the presence of external disturbances. Most
controller design approaches do not consider uncertainties
in mathematical models [12] in either partially structured
or unstructured spaces. These uncertainties can generate
external disturbances such as noise, communication delays,
wear and tear, flight system failures, and variation of the
payload mass [13], [14]. These factors can significantly affect
the performance and reliability of the UAV. Furthermore, the
internal dynamics of the robot change at every instant of time
due to the desired task. This means that the control system
may no longer be effective, and the dynamic parameters must
be updated despite the uncertainties to which the system
may be subjected [15]. One solution is the use of adaptive
control. It is a method used in automatic control systems
that allows the controller to adapt to unknown or changing
conditions [16]. This makes it an ideal option for UAVs,
as it enables the control system to adjust to changes in the
machine’s internal dynamics during the execution of desired
tasks [17].
A. RELATED WORK
The development of UAV has had significant advancements
with the integration of Model Predictive Control (MPC) to
improve tracking performance in UAVs [18], in particular its
variants Nonlinear Model Predictive Control (NMPC), and
Adaptive Nonlinear Predictive Control, enhancing trajectory
tracking, energy optimization, and safety, while focusing on
a Moment Observer-Based approach to further improve the
results of the models proposed.
NMPC, as a variant of MPC, is mainly used due to its
accuracy and computational efficiency in trajectory tracking,
offering substantial improvements over baseline feedback
controllers [19]. Its application extends to sophisticated tasks
such as obstacle avoidance [20], showcasing MPC’s capa-
bility in allowing navigation through dynamic environments.
The technology also proves adaptable across various UAV
types, from fixed-wing to quadrotors, addressing challenges
from precision landing [21] to agile flight [22].
Regarding safety and reliability in UAV deployment,
NMPC provides practical strategies for collision avoid-
ance [23], [24] and dynamic obstacle negotiation [25], [26].
It is important to also remark how NMPC allows stable
and accurate control during visual-based tasks [27]. The
methodology facilitates coordinated maneuvers, which is
evident in studies on multi-UAV encirclement [28] and
formation control [29] emphasizing its utility in complex
operational scenarios, where fault-tolerant control provides
a robust solution for handling faults and disturbances [30].
NMPCs also provide a solution to the energy effi-
ciency concern, with reduced consumption in quad-rotor
systems [31] and highlighting the importance of real-time
implementation efficiency [32]. Computational burden may
also decrease thanks to effective control performance through
simulations and experiments with NMPC [18]. Additionally,
system identification and collision avoidance integrated
within NMPC frameworks [33] allow safety during flight
without losing performance. Lastly, MPC-based naviga-
tion [34] and explicit MPC approaches [35] further validate
the model’s adaptability and effectiveness in real-world
applications such as constrained environments, underscoring
its potential to enhance UAV operational capabilities across
various conditions and tasks.
Other control strategies derived from Model Predictive
Control, such as adaptive and robust control frameworks
and nonlinear and fuzzy logic approaches, are summarized,
aiming at improving trajectory tracking, attitude stabilization,
obstacle avoidance, and payload transportation in unmanned
aerial vehicles (UAVs) and multi-rotor systems. Path tracking
and several Adaptive Model Predictive Control (ANMPC)
techniques applied in quadrotors have resulted in high pre-
cision in several tasks, like carrying unknown payloads [36],
or following desired trajectories and stabilizing attitudes
under dynamic conditions [37], enhancing the path tracking
capabilities of autonomous systems [38]. These methodolo-
gies are improved by incorporating advanced algorithms like
the Laguerre-based Adaptive MPC, or robust and nonlinear
MPC strategies, which offer significant improvements in
control accuracy and robustness against disturbances and
uncertainties [39], [40] and also in cases that the model
requires to adapt it to varying linear parameters.
Moreover, obstacle avoidance and mission planning for
aerial platforms have been addressed through adaptive model
predictive control strategies and differential evolution-based
distributed MPC, facilitating safer and more efficient
aerial operations, particularly in complex environments like
autonomous ship landing [10], [15]. Integrating active dis-
turbance rejection and backstepping-based adaptive control
further emphasizes the focus on ensuring performance and
enhancing stability against external perturbations [41]. This
approach extends to autonomous load transporting systems,
where adaptive control and model reference adaptive control
techniques are pivotal in coordinating flight formations and
managing load transportation with high stability and accu-
racy [42]. Another examination of nonlinear and adaptive
intelligent control techniques and their application in various
control systems, include quadrupedal robots and unmanned
rotorcrafts, showcasing their versatility and effectiveness
across different platforms [43], [44], [45]. It is worth
noting that all presented works underscore the importance
of performance, precision, and payload optimization in
77122
VOLUME 12, 2024

## Page 3

B. S. Guevara et al.: Estimation of Unmodeled Dynamics
aerial systems through the development of robust adaptive
control strategies and nonlinear model predictive path
tracking approaches. These innovations not only enhance
the control and maneuverability of UAVs but also ensure
their adaptability to diverse and challenging operational
scenarios [46], [47]. The next paragraph will focus on the
approach of Observer-Based models as an additional tool to
further improve the control system of UAVs using combined
control methods.
Observer-based models choose one or more variables
to analyze in order to control the effects of uncertainties
or disturbances as an ‘‘observer’’ like outside the model.
As this work focuses on a Momentum-Observer model,
this subsection will showcase works that have researched
this area in UAVs and other kinds of robots. Regarding
Momentum-Observed Based (MOB) models, [48] introduces
a MOB algorithm using LSTM for collision detection,
learning model uncertainties without a precise dynamics
model. This approach, validated on a real robot, improves
traditional MOB methods by better handling model errors and
friction effects. Another work proposes a Nonlinear Extended
State Momentum Observer (NESMO) for sensor-less colli-
sion detection in robots under model uncertainties [49]. This
paper presents NESMO for sensor less collision detection,
addressing sensitivity and noise immunity challenges in
current methods. Utilizing a fractional power function and
time-varying damping ratio, NESMO improves monitor-
ing bandwidth and noise immunity, with a novel TVT
to distinguish collision signals from disturbances, proven
effective on a 6-DOF robot. Finally, [50] reveals an SMO
model for collaborative robots, leveraging sliding mode
control for high-accuracy, minimal-delay collision detection
without joint acceleration measurement, enhancing safety
and reliability in human-robot interactions.
B. MAIN CONTRIBUTIONS
The paper presents the following contributions in the
field. Primarily, it introduces a cutting-edge approach by
integrating adaptive laws with a MOD, thus significantly
enhancing the controller’s adaptability and precision in
response to dynamic system changes. This fusion not only
amplifies the robustness of the control strategy but also
creates opportunities for real-time adjustments in the face of
uncertainties or varying operating conditions. Additionally,
the paper delves into the challenging task of estimating
perturbation dynamics in the simplified UAV dynamic model,
offering a comprehensive comparative analysis of various
identification methods. By doing so, it provides valuable
insights into effective techniques for addressing unknown or
uncertain system models, thereby advancing the state-of-the-
art in system identification and control methodologies.
C. OUTLINE
The article is structured into chapters to present its content
systematically. It begins with an introduction emphasizing
the importance of accurately modeling dynamics in UAV
frameworks. Chapters 2 and 3 explore the background of
the topic, focusing on the kinematic and dynamic model of
quadcopter. Chapters 4 through 7 present the formulation
of Nonlinear Model Predictive Control, Adaptive MPC
Controller, MPC with Dynamic Moment Observer, and
Adaptive MPC with Moment Observer. Chapter 8, the results
section, provides a detailed analysis of the case study,
including a comparison of the experimental framework and
the control laws utilized. Finally, Chapter 9 presents the
conclusions drawn from the study
II. KINEMATIC MODEL
Figure 1 shows
the quadcopter platform, where the
world-fixed inertial frame is represented by ⟨I⟩with the
following unit vectors

Ix, Iy, Iz
	
and the body-fixed frame
attached to quadcopter movements is defined by ⟨B⟩with the
unit vectors

Bx, By, Bz
	
, where the center of mass (CoM) is
aligned.
FIGURE 1. UAV reference frame DJI Matrice 100.
This work considers that it is enabled to rotate only in
yaw (ψ) defined in the vertical axis Bz and does not consider
the rotational movements of Pich and roll because the angles
on the horizontal axis Bx and By are relatively small in
flights that are not agile. In addition, the multirotor’s low-
level controller ensures stable hovering flight. The position
and orientation of quadcopter is define by:



ηx = ηx0 + a cos(ψ) −b sin(ψ)
ηy = ηy0 + a sin(ψ) + b cos(ψ)
ηz = ηz0 + c
ηψ = ψ,
(1)
and defined vectorially by η
=
ηx ηy ηz ηψ
⊺
∈
R4 respect to the frame ⟨I⟩, where the values (ηx0, ηy0, ηz0)
are the locations of the center of mass and (a, b, c) values
define the displacement of the point of interest measured
from the CoM. The evolution of the point of interest over
time represents the instantaneous kinematics of the quadrotor,
VOLUME 12, 2024
77123

## Page 4

B. S. Guevara et al.: Estimation of Unmodeled Dynamics
expressed in matrix form is:


˙ηx
˙ηy
˙ηz
˙ηψ

=


cos(ψ) −sin(ψ) 0 −ρ1
sin(ψ)
cos(ψ) 0 ρ2
0
0
1
0
0
0
0
1




νl
νm
νn
νω


(2)
where ν =
νl νm νn νω
⊺∈R4 define the linear (νl, νm, νn)
and angular (νω) velocities in ⟨B⟩frame; the expressions ρ1 =
a sin(ψ) + b cos(ψ) and ρ2 = a cos(ψ) −b sin(ψ) represent
the additional behavior considering the displacement of the
point of interest. Equation (2) is expressed in the compact
form as:
˙η(t) = J(ψ(t))ν(t),
(3)
where J(ψ(t)) ∈R4×4 is the Jacobian matrix which allows
the linear mapping between the control maneuverability
velocities ν to the evolution of the point of interest ˙η.
III. DYNAMIC MODEL
Most unmanned aerial vehicles (UAVs) used in development
are equipped with low-level PID controllers within their
motors. These controllers adjust the voltages required for
attitude and altitude control based on reference speeds [51].
This setup effectively leverages the advantages offered by
software development kits (SDKs) provided by commercial
drone manufacturers for developers and researcher.
The dynamic model (4) presented in [33] expresses a sim-
plified dynamic model ˙ν(t) = f(ξ, ν(t), µ(t)), considering
linear and rotational velocities as the input signals of the
system.


µl
µm
µn
µω

=


ξ1
0
0
ξ2
0
ξ3
0
ξ4
0
0 ξ5
0
bξ6 aξ7 0 ξ8(a2 + b2) + ξ9




˙νl
˙νm
˙νn
˙νω


+


ξ10
ωξ11
0 aωξ12
ωξ13
ξ14
0 bωξ15
0
0
ξ16
0
aωξ17 bωξ18 0
ξ19




νl
νm
νn
νω


(4)
To simplify the notation, the dynamic model of the UAV
can be written in its compact form as:
µn(t) = Mn(ξ, a, b)˙ν(t) + Cn(ξ, ν, a, b)ν(t),
(5)
where Mn(ξ, a, b) ∈R4×4 is a positive definite matrix,
which define the mass and inertia matrix of the quadcopter;
Cn(ξ, ν, a, b)
∈
R4×4 is the Coriolis and Centripetal
matrix; µ =
µl µm µn µω
⊺
∈R4 are the reference
maneuverability velocities; and ˙ν
=
˙νl ˙νm ˙νn ˙νω
⊺
∈
R4 are the accelerations generated in the system. The
dynamic model presented in (5) can be represented as a
regressor matrix of the system Yn and the vector of dynamic
parameters ξ,
Mn(ξ, a, b)˙ν(t) + Cn(ξ, ν, a, b)ν(t) = Yn(˙ν, ν, a, b)ξ, (6)
where, the vector ξ =
ξ1 ξ2 .. ξp
⊺∈Rp, with p = 19,
is the vector of unknown dynamic parameters represented
TABLE 1. Valores de ξ.
in Table 1, encompassing the internal dynamics of the
quadrotor. These parameters constitute a combination of
values associated with the physical, mechanical, electri-
cal, and aerodynamic phenomena influencing the robotic
system.
However, (6) does not consider the unmodeled dynamics
inherent in the simplified model and the incidence of external
perturbations that may change the internal configuration
of the UAV, so that an uncertainty velocities term Sτ u is
introduced:
µT (t) = Mn(ξ, a, b)˙ν(t) + Cn(ν, ξ, a, b)ν(t) + Sτ u,
(7)
where µT
=
µn + µext represents the total velocities
applied on the platform and it is the sum of the nominal
active velocities µn, and the external perturbation velocities
µext ∈R4.
IV. MPC CONTROLLER
This section describes the formulation of the optimal control
problem to plan the trajectory tracking over a finite prediction
horizon l ∈[t, t + N], as shown in Figure 2. The prediction
of the generalized nonlinear kinematic-dynamical system is
defined as:
˙x(t) = Ax(t) + Bµ(t),
A =
04×4
J(ψ)
04×4 −M−1
n Cn

, B =
04×4
M−1
n

,
(8)
where x(t) =
η⊺ν⊺⊺∈X and µ(t) ∈U are the state and
input to the system; and ˙x(t) =
˙η⊺˙ν⊺⊺. An intermediate
cost function ℓt is defined as:
ℓt(˜η, µ) = 1
2(˜η⊺(t)Q˜η(t) + µ⊺(t)Rµ(t)).
(9)
At the last instant of time the final prediction cost function
ℓf is defined as:
ℓf (˜η) = 1
2 ˜η⊺(N)Q˜η(N).
(10)
where Q and R are positive definite design gain matri-
ces for the error and input system, respectively. The
NMPC is defined as the solution to the optimal control
77124
VOLUME 12, 2024

## Page 5

B. S. Guevara et al.: Estimation of Unmodeled Dynamics
FIGURE 2. Nominal NMPC general scheme.
FIGURE 3. Adaptive NMPC general scheme.
problem (OCP):
min
˜η(.),µ(.) ℓf (˜η(N)) +
Z N
t
ℓt(˜η(t), µ(t))dt
(11a)
subject to:
˙x = f(x(t), µ(t))
(11b)
x(0) = x0
(11c)
ν ∈[νmin, νmax]
(11d)
µ(t) ∈U
∀t ∈[0, N −1]
(11e)
x(t) ∈X
∀t ∈[0, N]
(11f)
where the NOCP (11a) is solved considering the initial
conditions (11c) and translated into a nonlinear program-
ming formulation (NLP) using the direct multiple shooting
method [52]. (11b) define the system dynamics considered
as a constraint. Equations (11d) to (11e) and (11f) define the
input and state constraints, respectively.
V. ADAPTIVE NMPC CONTROLLER
Figure 3 shows the general scheme for solving the trajectory
tracking problem as the direct sum of the optimal control
actions generated by the NMPC subject to the constraints
and the estimation of the unmodeled dynamics that have an
adaptive compensation character against the perturbations to
which the quadrotor may be subjected.
Due to the changes in the internal dynamics and the effect
of the uncertainties that affect the quadrotor dynamic model,
velocity errors ˜ν = µc −ν are generated, which are the
difference between the velocities of the optimal controller and
the actual velocities of the robot. The dynamic model (7) can
be rewritten in the regressor matrix form:
µT (t) = Yn(˙ν, ν)ξn + Yu(˙ν, ν)ξu.
(12)
From here onwards, the subscript ‘n’ refers to the
nominal dynamic model obtained by offline identification.
The subscript ‘u’ refers to the dynamics not modeled in
the simplified dynamic model which includes the unknown
external disturbances. Considering the error between the
approximate uncertainty model and the real uncertainty, it is
obtained:
Yu(˙ν, ν)ˆξu ≈Yu(˙ν, ν)ξu + Yu(˙ν, ν)˜ξu,
(13)
where, ˆξ and ξ are the estimated and real dynamics
parameters, respectively, whereas ˜ξ = ˆξ −ξ is the vector
of parameter error. In order to estimate the uncertainties
in the dynamic parameters and the non-modeled dynamics,
the NMPC output is assumed to produce an optimal input
µc(t) ≈Yn(˙ν, ν)ξn, and the following Adaptive Non Linear
MPC is proposed:
µT (t) = µc(t) + Yu(˙νr, νr)ˆξu
(14)
= µc(t) + ˆµu(t).
(15)
The adaptable component Yu(˙νr, νr)ˆξu =: ˆµu(t) serves
two purposes by providing an estimation of the disturbance
and generating the necessary adjustments in the system’s
dynamics. Also, the following parameter-updating law is
proposed:
Yu( ˙υr, υr)ˆξu = ˆMu(ξ)˙νr + ˆCu(ξ)νr + Krσ,
(16)
˙ˆξu = 0−1Y⊺
u σ.
(17)
where, the undesirable steady-state position errors are
constrained to lie on a sliding surface σ = ˜ν + 3˜η, where
3 is a constant diagonal gain matrix of velocity errors. Here,
νr = σ + ν represents the modified reference velocity.
To demonstrate the tracking error global convergence, the
following Lyapunov candidate function is considered,
V = 1
2σ ⊺Muσ + 1
2
˜ξ
⊺0˜ξ,
(18)
where 0 ∈Rp×p is a positive definite diagonal matrix.
From (18), the time derivative of the Lyapunov candidate
along the system’s trajectories is,
˙V = −σ ⊺[µu −Mu˙νr −Cuνr] + ˜ξ
⊺0˙˜ξ.
(19)
From equations (16), (17), and (19), and considering that
˙˜ξ = ˙ˆξ due to the parameters are scalar values, then,
˙V = −σ ⊺[ ˜Mu˙νr + ˜Cuνr + Krσ] + ˜ξ
⊺0˙˜ξ
(20)
= −σ ⊺Krσ + ˜ξ
⊺[0˙ˆξ −Y⊺
u σ]
(21)
= −σ ⊺Krσ ≤0.
(22)
The expression (22). indicates that the output errors
approach the sliding surface over time.
σ = ˜ν + 3˜η = 0.
(23)
Furthermore, the expression (23) suggests that the sliding
surface σ approaches zero, indicating the system’s conver-
gence towards an equilibrium state. However, to affirm that
VOLUME 12, 2024
77125

## Page 6

B. S. Guevara et al.: Estimation of Unmodeled Dynamics
the system attains a stable state where both the steady-state
velocity error ˜ν and the steady-state position error ˜η converge
to zero, it is necessary to demonstrate the vanishing of the
steady-state velocity error as well. This can be accomplished
by substituting the desired velocity νd with a virtual
‘reference velocity’ νr [53]:
νr = νd + 3˜η,
(24)
it is defined that,
σ = ˜νr = νr −ν
The control law and adaptation law become,
ˆµu(t) = ˆMu(ξ)˙νd + ˆCu(ξ)νd + Kr ˜ν,
(25)
with,
˙ˆξu = 0−1Y⊺
u ˜ν.
(26)
Once more, global convergence of the tracking can be
demonstrated by employing the Lyapunov function:
V = 1
2 ˜ν⊺Mu˜ν + 1
2
˜ξ
⊺0˜ξ,
(27)
Similarly, in the previous demonstration, instead of (18),
the result obtained is,
˙V = −˜ν⊺Kr ˜ν ≤0
(28)
The expression (28) suggests that the steady-state velocity
error of the aircraft is zero. Consequently, this implies that
˜η →0 as t →∞. The adaptive controller designed for
the perturbations defined by equations (16) and (17) achieves
global asymptotic stability and ensures zero steady-state error
for UAV positions.
VI. MPC WITH MOMENTUM OBSERVER DYNAMICS
The generalized momentum of the platform p ∈R4 is:
p = Mnν.
(29)
From model in (5) the time temporaly evolution of p is
written as
˙p = µτ + ˙Mnν −Cnν
(30)
= µτ + C⊺
n ν,
(31)
where the property ˙Mn = Cn + C⊺
n is used. As presented
in [54], from (30), the dynamics of the momentum observer
is deduced
˙ˆp = µ + ˆµext + C⊺
n ν
(32)
˙ˆµext = Ko(˙p −˙ˆp),
(33)
where ˆµext is the external perturbation velocity estimation,
and Ko is the positive diagonal gain matrix of the observer.
The resulting output from the observer is the estimation of
FIGURE 4. MOD-NMPC general scheme.
external disturbance, which is obtained by integrating (33) as
follows,
ˆµext = Ko

p(t) −
Z t
t0
(µn + ˆµext + C⊺
n ν)dt −p(0)

.
(34)
The monitored signal ˆµext, is also referred to as the residual
vector. Ideally, this vector, resembling an abstract sensor,
allows the momentum observer to function like a virtual
sensor, detecting external velocities across the entirety of the
UAV’s structure.
The dynamic relationship between the external velocities
µext and ˆµext is expressed as:
˙ˆµext = Ko(µext −ˆµext)
(35)
This equation represents a first-order, low-pass, stable,
linear, and decoupled estimation of the external forces, with
the property ˆµext ≈µext as Ko approaches infinity.
Figure 4 shows the general scheme for solving the
trajectory tracking problem as the direct sum of the optimal
control actions generated by the NMPC subject to the
constraints and the estimation of the unmodeled dynamics
that have an adaptive compensation character against the
perturbations to which the quadrotor may be subjected.
The combination of Momentum Observer Dynamics and
NMPC, called MOD-NMPC, is defined as:
min
˜η(.),µ(.)
Z N
t
ℓt(˜η(t), µ(t))dt + ℓf (˜η(N))
(36a)
subject to:
˙x = f(x(t), µn(t), ˆµext(t))
(36b)
x(0) = x0
(36c)
ν ∈[νmin, νmax]
(36d)
µ(t) ∈U
∀t ∈[0, N −1]
(36e)
x(t) ∈X
∀t ∈[0, N]
(36f)
In which it is considered that the estimated disturbance ˆµext
at time t remains the same throughout the horizon [t, t + N].
VII. ADAPTIVE NMPC WITH MOD SCHEME
We suppose that the Momentum Observer Dynamic is
designed such that the difference ∥µext −ˆµext∥is minimized;
however, there exists a residual error ˜µext such that:
ˆµext ≈µext + ˜µext
(37)
77126
VOLUME 12, 2024

## Page 7

B. S. Guevara et al.: Estimation of Unmodeled Dynamics
FIGURE 5. Adaptive NMPC with MOD general scheme.
FIGURE 6. Digital twin of DJI matrice 100.
Figure 5 shows the general scheme that this work
proposes as combination of adaptive control with NMPC
and Momentum Observer Dynamics to generate a control
action that minimizes, adapts, and estimates the external
disturbances acting on the aircraft body, using control law 38.
µn(t) ≈µc(t) + ˆµu(t) −ˆµext(t)
(38)
≈µc(t) + Yu(˙νr, νr)ˆξu −ˆµext
(39)
If the error remains minimal, the observer term ˆµext
approaches the actual uncertainty Yu(˙ν, ν)ξu, then ˆµu(t) ≈
˜µext. Without consistently stimulating references, this sug-
gests that ˆµu(t) ̸≈
ˆµext(t). Nevertheless, it does indicate
that the NMPC dynamics roughly approach the genuine
dynamics.
VIII. RESULT
The proposed controllers in this article are evaluated and val-
idated through simulation experiments applied to the digital
twin of the quadcopter DJI Matrice 100 quadrotor, utilizing
a dynamic model identified within a real experimentation
framework [19]. This analysis compares the proposals in a
MiL framework [55] using the robotics simulation software
Webots [56], as shown in Figure 6.
The experiment involves testing four baseline scenarios by
applying perturbations:
1) Nominal NMPC
2) Adaptive NMPC
3) MOD-NMPC
4) Adaptive NMPC with MOD
Achieving ideal results is possible by using an NMPC
problem that is fully aware of the disturbances applied
to the model. The main goal of this work is to precisely
estimate unmodeled dynamics and leverage them to enhance
the robustness of the NMPC. All methods employ the same
intermediate and final cost function, fine-tuned in terms of
gain matrices to attain optimal performance in the nominal
case.
In order to evaluate the runtime performance of the
advanced control algorithm, the experiments are performed
on a single ground station PC (Intel i7-8850H, 2.6 GHz,
hexa-core 64-bit), with the loop control running at 30 Hz,
this means a time horizon of 1s whit N = 30. The OCP
solver is based in IPOP Multiple Shooting algorithm provided
by CasADi [57]. The communication between the node
controller and the UAV node is facilitated through ROS.
1) EXPERIMENTAL SETUP
For the implementation of the simulated experiments, the
following constraints, initial conditions, and gain matrices
are established for the proposed controller. Considering that
the maximum velocity of the desired trajectory is reached
when the derivative of the function is at its peak, it is inferred
that µmax
=
4 4 4 0.5⊺[ m
s ]; µmin
= −µmax; η0
=
0 0 1 0⊺[m]; Moreover, ν0
=
0 0 0 0⊺[ m
s ]; weight
matrix for cost function Q = 1.5I4×4 and R = diag[1 1 1 1];
weight matrix for adaptive law  = 2I4×4, 3 = 0.2I4×4 and
0 = diag[1 1 1 1].
When a perturbation appears, the robot’s acceleration is
described by the following differential equation,
˙ν = Mn(ξ, a, b)−1[−Cn(ξ, ν, a, b)ν + Sτ u + µ]
(40)
VOLUME 12, 2024
77127

## Page 8

B. S. Guevara et al.: Estimation of Unmodeled Dynamics
TABLE 2. Desired trajectory for experiments.
FIGURE 7. Nominal NMPC experiment results.
The perturbation, denoted by Sτ u =
τux τuy τuz τuψ
⊺∈
R4, is described by the function as follows:
τux(t) =



0
t < 5 ∨t > 25
2
5 ≤t < 10
0.5
10 ≤t < 15
−1.8
15 ≤t < 20
1.5
20 ≤t < 25
τuy(t) = 2 sin(0.1 t) + 1.5 cos(0.06t)
τuz(t) = 2 sin(0.05t) + 2 cos(−0.025t)
τuψ (t) = 1.5sign(0.2 sin(0.04t) + 3 cos(−0.04 t))
(41)
The main objective of the controller proposed in this work
is to track the reference trajectory defined in Table 2 over the
frame ⟨I⟩during the incidence of disturbances not considered
in the dynamic model.
A. NOMINAL NMPC EXPERIMENT
The evaluation is conducted with consideration to pertur-
bation functions acting as external signals modifying the
system dynamics. The results depicted in Figures 7.a and 7.b
illustrate that the NMPC with nominal model alone is not
robust enough against perturbations. In Figures 7.c and 7.d,
the error and control actions are observed respectively.
This highlights the necessity of integrating adaptive control
mechanisms, such as MOD, to enhance the system’s error in
real-world scenarios.
Figure 8 shows that the duration to solve the optimal
control problem for the NMPC consistently falls below
5.2 ms for a 1-second horizon. It is recognized that
computational performance is contingent upon the hardware
employed, suggesting scalability with a more robust ground
station PC.
FIGURE 8. MPC solver execution time.
FIGURE 9. Adaptive NMPC experiment results.
FIGURE 10. Adaptive law disturbance estimation results.
B. ADAPTIVE NMPC EXPERIMENT
Figure 9.a and 9.b depict the obtained behavior closely
aligned with the desired trajectory. This is because the errors
observed in Figure 9.c converge to zero, and the control
actions in Figure 9.d are bounded.
In Figure 10, a comparison is presented between the
components of disturbances generated by (41) and those
estimated by the adaptation law with NMPC. The illustration
vividly demonstrates the algorithm’s exceptional capability to
approximate the disturbances introduced to the aircraft. This
observation underscores the effectiveness of the adaptive con-
77128
VOLUME 12, 2024

## Page 9

B. S. Guevara et al.: Estimation of Unmodeled Dynamics
FIGURE 11. MOD-NMPC experiment results.
FIGURE 12. MOD disturbance estimation results.
trol mechanism in mitigating external disturbances, thereby
enhancing the system’s overall robustness and performance.
C. MOD-NMPC EXPERIMENT
Figure 11.a and Figure 11.b illustrate the aircraft’s behavior
resulting from the implementation of MOD-NMPC as
outlined in (36). The outcomes demonstrate that the proposed
controller effectively mitigates perturbations affecting the
system, even when they are highly agile. This is evident in
how the errors remain bounded, as depicted in Figure 11.c,
along with the control actions shown in Figure 11.d.
Consequently, the quadrotor maintains its desired trajectory
even in the presence of unknown disturbances.
Figure 12 depicts the comparison between estimated and
real disturbances. This comparison offers a general under-
standing of the disturbances that can affect the system while
also being estimable. It confirms that the moment observer
effectively estimates the velocities impacting the system and
altering the internal configuration of the quadrotor, thanks to
the filtering characteristics ensuring a smooth approximation
to the estimated values.
D. ADAPTIVE NMPC WITH MOD EXPERIMENTS
In Figure 13.a and 13.b, an improved trajectory tracking
is observed in the presence of disturbances. Figure 13.c
FIGURE 13. Adaptive NMPC with MOD experiment results.
demonstrates that the control error ˜η =
˜ηx ˜ηy ˜ηz ˜ηψ
T ∈
R4 converges to values close to zero in the presence of
external disturbances applied in the simulation. Specifically,
the control errors are bounded, achieving a final characteristic
error |˜η| < 0.1, and are different from zero, i.e., ˜η = ηd−η ̸=
0. Finally, the control actions are depicted in Figure 13.d.
Figure 14 illustrates the estimation of perturbations
affecting the internal configuration of the quadrotor during
the real experimental test, showcasing the evident presence
of non-modeled dynamics. While the MOD action estimates
the external velocities perturbing the system, the adaptation
law estimates the estimation error, ensuring its convergence
to zero, i.e., ˆµu(t) ≈˜µext.
The estimation of non-model dynamics, expressed as
external disturbances, offers insight into phenomena not
accounted for during the development of the mathematical
model of the robotic system. The results confirm the
robustness of the proposed controller, which is a combination
of NMPC, the adaptation-estimation law, and the momentum
observer dynamic.
E. DISCUSSIONS
This work combines a dynamic momentum observer and
an adaptive estimation law with a model-based predictive
controller subject to constraints to estimate unmodeled
disturbances in order to solve the trajectory tracking task.
The results of the simulated tests show that the momentum
observer estimation law and the adaptive control law allow
estimating the component of the unmodeled dynamics that
serves both to estimate the disturbance and to generate the
necessary adaptation in the system dynamics to dissipate
control errors. Furthermore, the NMPC is structured as a
nonlinear programming problem, employing the multiple
shooting method. Its cost function encompasses both the
kinematic and dynamic models of the quadrotor.
The tests utilize the MiL framework and external distur-
bances were introduced to simulate disruptive behavior for
the system. This allowed demonstrating the robustness of the
proposed controller by combining the optimal input of the
predictive controller and the estimation of the disturbance
unknown to the system, ensuring that the steady-state error
converges to values close to zero despite the incidence of
external disturbances that modify the system’s dynamics. The
VOLUME 12, 2024
77129

## Page 10

B. S. Guevara et al.: Estimation of Unmodeled Dynamics
FIGURE 14. Results of adaptive law and MOD disturbance estimation.
use of the CasADi framework ensures that the time required
to find the optimal solution remains below the sampling time,
addressing a significant challenge in using predictive control
schemes in critical flight system conditions.
IX. CONCLUSION
This work develops and validates a robust controller, which
combines NMPC incorporating a cost function that considers
both the kinematic and dynamic models of the quadrotor to
produce an optimal input for the nominal model, coupled with
the momentum observer acting as a virtual sensor, along with
an adaptive law for estimating non-modeled dynamics that
affect and modify the system’s dynamics, aiming to mitigate
control errors caused by external disturbances. The proposed
controller is evaluated through simulated experiments using
the CasADi nonlinear programming framework, known for
its high computational efficiency. In the simulated tests,
fictitious disturbances are generated, and the adaptation law
accurately estimates values close to the real ones, thus
validating the functionality of the proposed controller.
ACKNOWLEDGMENT
The authors would like to thank the CICHE Research
Center and the SISAu Research Group for the support and
development of this work. The results of this work are
part of the Project ‘‘Tecnologías de la Industria 4.0 en
Educación, Salud, Empresa e Industria’’ developed by
Universidad Indoamérica. Supplementary Material Code:
https://github.com/bryansgue/MPC_Adaptive_MOD.
REFERENCES
[1] F. Ahmed, J. Mohanta, A. Keshari, and P. S. Yadav, ‘‘Recent advances in
unmanned aerial vehicles: A review,’’ Arabian J. Sci. Eng., vol. 47, no. 7,
pp. 7963–7984, 2022.
[2] K. Nonami, F. Kendoul, S. Suzuki, W. Wang, and D. Nakazawa,
Autonomous Flying Robots: Unmanned Aerial Vehicles and Micro Aerial
Vehicles. Tokyo, Japan: Springer, 2010.
[3] B. Rubí, R. Pérez, and B. Morcego, ‘‘A survey of path following control
strategies for UAVs focused on quadrotors,’’ J. Intell. Robotic Syst., Theory
Appl., vol. 98, pp. 241–265, May 2020.
[4] L. D. P. Pugliese, F. Guerriero, and G. Macrina, ‘‘Using drones for
parcels delivery process,’’ Proc. Manuf., vol. 42, pp. 488–497, Jan. 2020.
[Online].
Available:
https://www.sciencedirect.com/science/article/
pii/S2351978920305928
[5] L. Yang, Z. Liu, X. Wang, and Y. Xu, ‘‘An optimized image-based visual
servo control for fixed-wing unmanned aerial vehicle target tracking with
fixed camera,’’ IEEE Access, vol. 7, pp. 68455–68468, 2019.
[6] B. S. Morse, C. H. Engh, and M. A. Goodrich, ‘‘UAV video coverage
quality maps and prioritized indexing for wilderness search and rescue,’’ in
Proc. 5th ACM/IEEE Int. Conf. Human-Robot Interact. (HRI), Mar. 2010,
pp. 227–234.
[7] F. Buele, V. Moya, A. Tirira, A. Pilco, and Q. Lei, ‘‘Training in ‘first
person view’ systems for racing drones,’’ in Proc. 5th Int. Conf. Artif. Intell.
Comput. Appl. (ICAICA), Nov. 2023, pp. 256–261.
[8] B. Park and H. Oh, ‘‘Vision-based obstacle avoidance for UAVs via
imitation learning with sequential neural networks,’’ Int. J. Aeronaut.
Space Sci., vol. 21, pp. 768–779, Sep. 2020.
[9] Z. Ma, C. Wang, Y. Niu, X. Wang, and L. Shen, ‘‘A saliency-based
reinforcement learning approach for a UAV to avoid flying obstacles,’’
Robot. Auto. Syst., vol. 100, pp. 108–118, Feb. 2018. [Online]. Available:
https://www.sciencedirect.com/science/article/pii/S0921889017301136
[10] B. Zhang, X. Sun, S. Liu, and X. Deng, ‘‘Adaptive differential
evolution-based distributed model predictive control for multi-UAV
formation flight,’’ Int. J. Aeronaut. Space Sci., vol. 21, pp. 538–548,
Jun. 2020.
[11] A. Franchi, C. Secchi, M. Ryll, H. H. Bulthoff, and P. R. Giordano,
‘‘Shared control : Balancing autonomy and human assistance with a group
of quadrotor UAVs,’’ IEEE Robot. Autom. Mag., vol. 19, no. 3, pp. 57–68,
Sep. 2012.
[12] A. L. Salih, M. Moghavvemi, H. A. F. Mohamed, and K. S. Gaeid,
‘‘Modelling and PID controller design for a quadrotor unmanned air
vehicle,’’ in Proc. IEEE Int. Conf. Autom., Quality Test., Robot. (AQTR),
May 2010, pp. 1–5.
[13] C. Fu, A. Sarabakha, E. Kayacan, C. Wagner, R. John, and J. M. Garibaldi,
‘‘Input uncertainty sensitivity enhanced nonsingleton fuzzy logic con-
trollers for long-term navigation of quadrotor UAVs,’’ IEEE/ASME Trans.
Mechatronics, vol. 23, no. 2, pp. 725–734, Apr. 2018.
[14] S. Islam, P. X. Liu, and A. El Saddik, ‘‘Robust control of four-rotor
unmanned aerial vehicle with disturbance uncertainty,’’ IEEE Trans. Ind.
Electron., vol. 62, no. 3, pp. 1563–1571, Mar. 2015.
[15] K. Xia, S. Lee, and H. Son, ‘‘Adaptive control for multi-rotor UAVs
autonomous ship landing with mission planning,’’ Aerosp. Sci. Technol.,
vol. 96, Jan. 2020, Art. no. 105549.
[16] D. E. Seborg, T. F. Edgar, and S. L. Shah, ‘‘Adaptive control strategies for
process control: A survey,’’ AIChE J., vol. 32, no. 6, pp. 881–913, 1986,
doi: 10.1002/aic.690320602.
[17] N. Koksal, H. An, and B. Fidan, ‘‘Backstepping-based adaptive control
of a quadrotor UAV with guaranteed tracking performance,’’ ISA Trans.,
vol. 105, pp. 98–110, Oct. 2020.
[18] D. Wang, Q. Pan, Y. Shi, J. Hu, and C. Zhao, ‘‘Efficient nonlinear
model predictive control for quadrotor trajectory tracking: Algorithms
and experiment,’’ IEEE Trans. Cybern., vol. 51, no. 10, pp. 5057–5068,
Oct. 2021.
[19] B. S. Guevara, L. F. Recalde, J. Varela-Aldás, V. H. Andaluz,
D. C. Gandolfo, and J. M. Toibero, ‘‘A comparative study between
NMPC and baseline feedback controllers for UAV trajectory tracking,’’
Drones, vol. 7, no. 2, p. 144, 2023. [Online]. Available: https://www.
mdpi.com/2504-446X/7/2/144
[20] J. C. Pereira, V. J. S. Leite, and G. V. Raffo, ‘‘Nonlinear model predictive
control on SE(3) for quadrotor trajectory tracking and obstacle avoidance,’’
in Proc. 19th Int. Conf. Adv. Robot. (ICAR), Dec. 2019, pp. 155–160.
[21] S. H. Mathisen, K. Gryte, T. A. Johansen, and T. I. Fossen, ‘‘Non-
linear model predictive control for longitudinal and lateral guidance of
a small fixed-wing UAV in precision deep stall landing,’’ in Proc. Amer.
Inst. Aeronaut. Astronaut., 2016, pp. 6–8. [Online]. Available: https://
api.semanticscholar.org/CorpusID:53467771
77130
VOLUME 12, 2024

## Page 11

B. S. Guevara et al.: Estimation of Unmodeled Dynamics
[22] S. Sun, A. Romero, P. Foehn, E. Kaufmann, and D. Scaramuzza,
‘‘A comparative study of nonlinear MPC and differential-flatness-based
control for quadrotor agile flight,’’ IEEE Trans. Robot., vol. 38, no. 6,
pp. 3357–3373, Dec. 2022.
[23] T. Baca, D. Hert, G. Loianno, M. Saska, and V. Kumar, ‘‘Model predictive
trajectory tracking and collision avoidance for reliable outdoor deployment
of unmanned aerial vehicles,’’ in Proc. IEEE/RSJ Int. Conf. Intell. Robots
Syst. (IROS), Oct. 2018, pp. 6753–6760.
[24] B.
Lindqvist,
S.
S.
Mansouri,
A.-A.
Agha-Mohammadi,
and
G. Nikolakopoulos,
‘‘Nonlinear
MPC
for
collision
avoidance
and
control of UAVs with dynamic obstacles,’’ IEEE Robot. Autom. Lett.,
vol. 5, no. 4, pp. 6001–6008, Oct. 2020.
[25] I. B. P. Nascimento, A. Ferramosca, L. C. A. Pimenta, and G. V. Raffo,
‘‘NMPC strategy for a quadrotor UAV in a 3D unknown environment,’’ in
Proc. 19th Int. Conf. Adv. Robot. (ICAR), Dec. 2019, pp. 179–184.
[26] C. Zhao, D. Wang, J. Hu, and Q. Pan, ‘‘Nonlinear model predictive control-
based guidance algorithm for quadrotor trajectory tracking with obstacle
avoidance,’’ J. Syst. Sci. Complex., vol. 34, no. 4, pp. 1379–1400, 2021.
[27] K. Zhang, Y. Shi, and H. Sheng, ‘‘Robust nonlinear model predictive
control based visual servoing of quadrotor UAVs,’’ IEEE/ASME Trans.
Mechatronics, vol. 26, no. 2, pp. 700–708, Apr. 2021.
[28] A. T. Hafez, A. J. Marasco, S. N. Givigi, M. Iskandarani, S. Yousefi,
and C. A. Rabbath, ‘‘Solving multi-UAV dynamic encirclement via model
predictive control,’’ IEEE Trans. Control Syst. Technol., vol. 23, no. 6,
pp. 2251–2265, Nov. 2015.
[29] H.-S. Shin, M.-J. Thak, and H.-J. Kim, ‘‘Nonlinear model predictive
control for multiple UAVs formation using passive sensing,’’ Int. J.
Aeronaut. Space Sci., vol. 12, no. 1, pp. 16–23, Mar. 2011.
[30] F. Nan, S. Sun, P. Foehn, and D. Scaramuzza, ‘‘Nonlinear MPC for
quadrotor fault-tolerant control,’’ IEEE Robot. Autom. Lett., vol. 7, no. 2,
pp. 5047–5054, Apr. 2022.
[31] R. Benotsmane and J. Vásárhelyi, ‘‘Towards optimization of energy
consumption of Tello quad-rotor with MPC model implementation,’’
Energies, vol. 15, no. 23, p. 9207, 2022. [Online]. Available: https://www.
mdpi.com/1996-1073/15/23/9207
[32] B. B. Carlos, T. Sartor, A. Zanelli, G. Frison, W. Burgard, M. Diehl,
and G. Oriolo, ‘‘An efficient real-time NMPC for quadrotor position
control under communication time-delay,’’ in Proc. 16th Int. Conf. Control,
Autom., Robot. Vis. (ICARCV), Dec. 2020, pp. 982–989.
[33] L. F. Recalde, B. S. Guevara, C. P. Carvajal, V. H. Andaluz, J. Varela-Aldás,
and D. C. Gandolfo, ‘‘System identification and nonlinear model
predictive control with collision avoidance applied in hexacopters UAVs,’’
Sensors, vol. 22, no. 13, p. 4712, Jun. 2022. [Online]. Available:
https://www.mdpi.com/1424-8220/22/13/4712
[34] B. Lindqvist, S. S. Mansouri, and G. Nikolakopoulos, ‘‘Non-linear MPC
based navigation for micro aerial vehicles in constrained environments,’’
in Proc. Eur. Control Conf. (ECC), May 2020, pp. 837–842.
[35] C. Liu, H. Lu, and W.-H. Chen, ‘‘An explicit MPC for quadrotor
trajectory tracking,’’ in Proc. 34th Chin. Control Conf. (CCC), Jul. 2015,
pp. 4055–4060.
[36] V. N. Sankaranarayanan, S. Roy, and S. Baldi, ‘‘Aerial transportation
of unknown payloads: Adaptive path tracking for quadrotors,’’ in Proc.
IEEE/RSJ Int. Conf. Intell. Robots Syst. (IROS), Oct. 2020, pp. 7710–7715.
[37] P. T. Jardine, S. N. Givigi, S. Yousefi, and M. J. Korenberg, ‘‘Adaptive
MPC using a dual fast orthogonal Kalman filter: Application to quadcopter
altitude control,’’ IEEE Syst. J., vol. 13, no. 1, pp. 973–981, Mar. 2019.
[38] K. Yang, S. Sukkarieh, and Y. Kang, ‘‘Adaptive nonlinear model predictive
path tracking control for a fixed-wing unmanned aerial vehicle,’’ in Proc.
AIAA Guidance, Navigat., Control Conf., 2009, pp. 65–74. [Online].
Available: https://arc.aiaa.org/doi/abs/10.2514/6.2009-5622
[39] O. J. Gonzalez Villarreal, J. A. Rossiter, and H. Shin, ‘‘Laguerre-based
adaptive MPC for attitude stabilization of quad-rotor,’’ in Proc. UKACC
12th Int. Conf. Control (CONTROL), Sep. 2018, pp. 360–365.
[40] G. Garimella, M. Sheckells, and M. Kobilarov, ‘‘Robust obstacle avoidance
for aerial platforms using adaptive model predictive control,’’ in Proc.
IEEE Int. Conf. Robot. Autom. (ICRA), May 2017, pp. 5876–5882.
[41] W. Wenjie, H. Zhen, C. Rui, J. Feiteng, and S. Huiming, ‘‘Trajectory
tracking control design for UAV based on MPC and active disturbance
rejection,’’ in Proc. IEEE CSAA Guid., Navigat. Control Conf. (CGNCC),
Aug. 2018, pp. 1–5.
[42] A. Altan, Ö. Aslan, and R. Hacioglu, ‘‘Model reference adaptive control
of load transporting system on unmanned aerial vehicle,’’ in Proc. 6th Int.
Conf. Control Eng. Inf. Technol. (CEIT), Oct. 2018, pp. 1–5.
[43] M. V. Minniti, R. Grandia, F. Farshidian, and M. Hutter, ‘‘Adaptive CLF-
MPC with application to quadrupedal robots,’’ IEEE Robot. Autom. Lett.,
vol. 7, no. 1, pp. 565–572, Jan. 2022.
[44] Q. Xu, Z. Wang, and Y. Li, ‘‘Fuzzy adaptive nonlinear information fusion
model predictive attitude control of unmanned rotorcrafts,’’ Aerosp. Sci.
Technol., vol. 98, Mar. 2020, Art. no. 105686. [Online]. Available:
https://www.sciencedirect.com/science/article/pii/S1270963819307680
[45] H. Mo and G. Farid, ‘‘Nonlinear and adaptive intelligent control
techniques for quadrotor UAV—A survey,’’ Asian J. Control, vol. 21,
no. 2, pp. 989–1008, Mar. 2019. [Online]. Available: https://onlinelibrary.
wiley.com/doi/abs/10.1002/asjc.1758
[46] D. Hanover, P. Foehn, S. Sun, E. Kaufmann, and D. Scaramuzza,
‘‘Performance, precision, and payloads: Adaptive nonlinear MPC for
quadrotors,’’ IEEE Robot. Autom. Lett., vol. 7, no. 2, pp. 690–697,
Apr. 2022.
[47] A. Didier, A. Parsi, J. Coulson, and R. S. Smith, ‘‘Robust adaptive model
predictive control of quadrotors,’’ in Proc. Eur. Control Conf. (ECC),
Jun. 2021, pp. 657–662.
[48] D. Lim, D. Kim, and J. Park, ‘‘Momentum observer-based collision
detection using LSTM for model uncertainty learning,’’ in Proc. IEEE Int.
Conf. Robot. Autom. (ICRA), May 2021, pp. 4516–4522.
[49] Y. Li, Y. Li, M. Zhu, Z. Xu, and D. Mu, ‘‘A nonlinear momentum observer
for sensorless robot collision detection under model uncertainties,’’
Mechatronics, vol. 78, Oct. 2021, Art. no. 102603. [Online]. Available:
https://www.sciencedirect.com/science/article/pii/S0957415821000866
[50] S. Long, X. Dang, S. Sun, Y. Wang, and M. Gui, ‘‘A novel sliding
mode momentum observer for collaborative robot collision detection,’’
Machines, vol. 10, no. 9, p. 818, Sep. 2022. [Online]. Available:
https://www.mdpi.com/2075-1702/10/9/818
[51] Q. Quan, Introduction to Multicopter Design and Control. Singapore:
Springer, 2017.
[52] S. Yang, ‘‘A trust-region method for multiple shooting optimal control,’’
M.S. thesis, School Elect. Eng. Comput. Sci. (EECS), KTH, Stockholm,
Sweden, 2022.
[53] J. J. Slotine and W. Li, ‘‘On the adaptive control of robot manipulators,’’
Int. J. Robot. Res., vol. 6, no. 3, pp. 49–59, Sep. 1987. [Online]. Available:
http://journals.sagepub.com/doi/10.1177/027836498700600303
[54] S. Haddadin, A. De Luca, and A. Albu-Schäffer, ‘‘Robot collisions: A
survey on detection, isolation, and identification,’’ IEEE Trans. Robot.,
vol. 33, no. 6, pp. 1292–1312, Dec. 2017.
[55] C. Ke, K.-Y. Cai, and Q. Quan, ‘‘Uniform fault-tolerant control of a
quadcopter with rotor failure,’’ IEEE/ASME Trans. Mechatronics, vol. 28,
no. 1, pp. 507–517, Feb. 2023.
[56] O. Michel, ‘‘Webots: Professional mobile robot simulation,’’ Int. J. Adv.
Robot. Syst., vol. 1, no. 1, pp. 39–42, Mar. 2004. [Online]. Available:
http://www.ars-journal.com/International-Journal-of-Advanced-Robotic-
Systems/Volume-1/39-42.pdf
[57] J. A. E. Andersson, J. Gillis, G. Horn, J. B. Rawlings, and M. Diehl,
‘‘CasADi: A software framework for nonlinear optimization and optimal
control,’’ Math. Program. Comput., vol. 11, no. 1, pp. 1–36, Mar. 2019.
BRYAN S. GUEVARA received the degree in
mechatronic engineering from the University of
the Armed Forces—ESPE, in 2018, and the
master’s degree in control systems engineering
from the National University of San Juan, in 2024,
where he is currently pursuing the Ph.D. degree
in control systems engineering. He received the
DAAD Scholarship (German Academic Exchange
Service) through the Funding Program: Third
Country Programme Latin America, in 2022, for
the Ph.D. degree. His research interests include aerial robotics, dynamic
systems modeling, and optimal control.
VOLUME 12, 2024
77131

## Page 12

B. S. Guevara et al.: Estimation of Unmodeled Dynamics
LUIS F. RECALDE received the Graduate degree in
mechatronics engineering from the University of
the Armed Forces (ESPE), in 2021. He is currently
pursuing the master’s degree in control systems
engineering with the National University of San
Juan, Argentina. He is currently a Researcher with
CICHE, Universidad Indoamérica. His research
interests include nonlinear model predictive con-
trol (NMPC) and reinforcement learning (RL).
Over the past few years, he has actively merged
control theory with machine learning.
VIVIANA MOYA received the degree in electron-
ics and control engineering from Escuela Politéc-
nica Nacional (EPN), Quito, Ecuador, in 2016, and
the Ph.D. degree in control systems engineering
from the National University of San Juan (UNSJ),
Argentina, in 2021. She is currently a Lecturer and
a Researcher with Universidad Internacional del
Ecuador. Her doctoral studies were supported by
the DAAD Scholarship from Germany. Her profes-
sional interests include teleoperation systems and
automatic control. In recent years, she has been also focusing on artificial
intelligence and computer vision.
JOSÉ VARELA-ALDÁS (Member, IEEE) is cur-
rently pursuing the Ph.D. degree in electronic engi-
neering from the University of Zaragoza, Spain.
He is an Associate Professor with Universidad
Indoamérica, where he is teaching the follow-
ing subjects: robotics, electrical engineering, and
electricity and industrial electronics. His research
interests include control systems, robotics, the IoT,
and virtual reality. He was the Winner of the
Best Young Researcher at IEEE Ecuador, in 2023.
In 2024, he will serve as the President for the Robotics and Automation
Society, IEEE Ecuador.
DANIEL C. GANDOLFO received the degree in
electronic engineering and the Ph.D. degree in
control systems engineering from the National
University of San Juan (UNSJ), Argentina, in
2006 and 2014, respectively. He was an Automa-
tion Engineer in the industry, until 2009. Currently,
he is a Researcher with Argentinean National
Council for Scientific Research (CONICET) and
an Associate Professor with the Institute of Auto-
matics, UNSJ-CONICET, Argentina. His research
interests include algorithms for management energy systems and optimal
control strategies with application in unmanned aerial vehicles (UAV).
JUAN M. TOIBERO received the degree in elec-
tronic engineering from National Technological
University, Parana, Argentina, in 2002, and the
Ph.D. degree in control systems engineering from
the National University of San Juan, Argentina,
in 2007. He has been a Full Professor with the
Instituto de Automática, National University of
San Juan, since 2002, and a full-time Researcher
with CONICET, since 2011. His research interests
include the automatic control of mobile robotic
platforms, nonlinear control design, the inclusion of dynamic models, and
the applications of USVs (unmanned surface vessels) in environmental
monitoring, surveillance, and control.
77132
VOLUME 12, 2024
