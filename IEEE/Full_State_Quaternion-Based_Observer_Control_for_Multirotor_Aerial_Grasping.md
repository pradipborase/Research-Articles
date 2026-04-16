# Full_State_Quaternion-Based_Observer_Control_for_Multirotor_Aerial_Grasping.pdf

## Page 1

Full state quaternion-based observer control
for multirotor aerial grasping
I. García-Mosqueda1,2, A. Tevera-Ruiz1,3, H. Abaunza2,∗, P. Castillo1, A. Sanchez-Orta3, J.D. Chazot1
Abstract— This paper presents an enhanced observer con-
trol strategy for multirotor aerial grasping. Unlike previous
approaches, which focused solely on translational dynamics, this
method incorporates dual observers—one for the translational
subsystem and another for the rotational dynamics. By lever-
aging quaternions, the proposed control framework provides
a singularity-free representation of orientation while naturally
decoupling rotational and translational dynamics. This allows
the system to be treated as fully actuated in both position and
orientation, improving disturbance rejection and compensating
for torques induced by off-center or asymmetrically shaped ob-
jects during grasping. A passive, non-actuated gripper further
enhances the drone’s ability to interact with objects in real-
world scenarios. Experimental validations confirm the robust-
ness and adaptability of the proposed approach, demonstrating
its effectiveness in handling dynamic variations in mass and
torque while maintaining stable flight.
I. INTRODUCTION
Unmanned Aerial Vehicles (UAVs), particularly quadro-
tors, have gained significant attention in recent years, not
only for their roles in surveillance and data collection [1], but
also for more complex interactions with the environment. In
particular, applications such as obstacle avoidance [2], object
collection [3], and aerial manipulation have increased their
interest in improving the UAVs’ ability to physically interact
with objects. These advances not only transform research
fields, but also drive technological innovation in industries.
UAVs implemented in real world applications were origi-
nally designed to use integrated sensors and cameras for data
capture, and were not intended for carrying external payloads
[4]. As a result, when it comes to object manipulation
tasks—such as picking up or transporting items—specialized
drones and complex, often expensive grippers are typically
required. This highlights the challenge of integrating payload
handling capabilities into systems that were not initially
designed for such purposes [5]. However, UAVs’ versatility
across various sectors, including security, manufacturing, and
environmental monitoring, continues to expand [6].
Previous work has explored the development of both actu-
ated and non-actuated grippers to enhance a drone’s capacity
for object handling. Actuated grippers, which provide control
over force and pose, are widely used but introduce challenges
1 Université de technologie de Compiègne, CNRS, Heudiasyc/Roberval,
Compiègne,
France.
(ateverar,castillo)@hds.utc.fr,
jean-daniel.chazot@utc.fr
2 Tecnológico de Monterrey, School of Engineering and Sciences, Jalisco,
Mexico. (A00834571,habaunza)@tec.mx
3 CINVESTAV-Saltillo, Robotics and Advanced Manufacturing, Mexico.
(alejandro.tevera,anand.sanchez)@cinvestav.edu.mx
∗Corresponding Author
related to system weight and complexity [7], [8]. Non-
actuated designs, on the other hand, aim to reduce energy
consumption and complexity, offering precise control with
lower power requirements [9]. However, these systems still
need to address the disturbances caused by external forces,
such as the mass and torque variations encountered when
grasping objects of different shapes and sizes.
One significant challenge when UAVs interact with objects
is compensating for the disturbances that arise, especially
when the object’s mass or geometry causes unpredictable
forces on the UAV. While earlier approaches have employed
disturbance observers for compensating external forces dur-
ing object manipulation [10], the impact of rotational dy-
namics on the UAV’s stability during such tasks has been
less explored. Notably, research has implemented systems
such as the Uncertainty and Disturbance Estimator (UDE)
[11], as well as various forms of Disturbance-Observer-Based
Control (DOBC) [12], [13] to improve trajectory tracking
and disturbance rejection in UAV systems. However, these
methods primarily focus on either translational dynamics or
rotational stability, with little emphasis on integrating both
aspects into a unified framework.
The primary contribution of this paper is the development
of a quaternion-based observer control system for multirotor
UAVs performing aerial grasping tasks. This approach inte-
grates two distinct observers (one for the translational and
another for the rotational dynamics) thus allowing the system
to act as fully actuated in both position and orientation.
Building upon the approach presented in [14], this work uses
an almost decoupling translational and rotational dynamics
based on virtual fully actuated system through the use
of a desired quaternion [15]. By utilizing quaternions for
rotational dynamics, this method offers a singularity-free
representation of the UAV’s orientation, which aids in decou-
pling the rotational and translational dynamics, enhancing the
overall stability of the UAV when interacting with objects.
Furthermore, this new control structure improves the UAV’s
ability to reject disturbances from off-center grasps or objects
with non-uniform shapes, allowing for more flexible and
reliable aerial manipulation.
The remainder of the paper is organized as follows: In
section II the quadrotor model and the quaternion-based
control approach are presented. Section III is used to outline
the dual-observer implementation. In section IV details on
the experimental setup and results are introduced in graphs.
Finally, in section V the implications of the results and
suggested directions for future research are discussed.
2025 International Conference on
Unmanned Aircraft Systems (ICUAS)
May 14-17, 2025. North Carolina, USA
979-8-3315-1328-3/25/$31.00 ©2025 IEEE
170
2025 International Conference on Unmanned Aircraft Systems (ICUAS) | 979-8-3315-1328-3/25/$31.00 ©2025 IEEE | DOI: 10.1109/ICUAS65942.2025.11007917
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:38:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 2

II. QUADROTOR MODELING AND CONTROL
A. Quaternion dynamic model of the quadrotor
Based on the blade element theory, each rotor i
∈
{1, . . . , 4} in a symmetric quadrotor (see Fig. 1) generates
a thrust fi := CT ρApr2ω2
i and a torque τi := CQρApr3ω2
i
as a function of its angular velocity ωi, the air density ρ,
the blade area Ap, the rotor radius r, and the aerodynamic
coefficients CT and CQ [16]. Thus, the total thrust force
⃗Fth, acting vertically in the body reference frame, can be
calculated as
⃗Fth :=


0
0
Fth

=


0
0
f1 + f2 + f3 + f4

,
and similarly, the total torque vector, acting in the same
reference frame, can be expressed as
⃗τ :=


τx
τy
τz

=


(−f1 −f2 + f3 + f4)l cos(π/4)
(−f1 + f2 + f3 −f4)l cos(π/4)
P4
i=1 τi

,
where l is the arm length of the quadrotor, extending from
the center of mass to each motor.
Defining the state of the quadrotor as
X :=


⃗p
˙⃗p
q
⃗Ω

,
(1)
where ⃗p ∈R3 is the position of the quadrotor in the inertial
reference frame, ˙⃗p is its velocity, q := q0 + [q1 q2 q3]⊺∈
H represents its orientation in quaternion form, and ⃗Ω:=
[ωx ωy ωz]⊺is its angular velocity in the body reference
frame. Thus, based on the expressions the total force and
torque acting on the center of mass, the dynamic model of
the quadrotor can be written as
˙X = d
dt


⃗p
˙⃗p
q
⃗Ω

=


˙⃗p
q ⊗
⃗Fth
m ⊗q + ⃗g + ⃗γF
1
2q ⊗⃗Ω
J−1(⃗τ + ⃗γr −⃗Ω× J⃗Ω)

,
(2)
where ⊗represents the quaternion product, m and J are
the mass and inertia matrix of the quadrotor, respectively,
⃗g := [0 0 −9.81]⊺is the gravitational acceleration vector,
and ⃗γF , ⃗γr ∈R3 are unknown perturbation vectors.
Fig. 1: Total thrust force ⃗Fth and torque ⃗τ illustrated in [16].
B. Underactuation problem of the quadrotor
It is important to note that the dynamic system expressed
in (2) is underactuated, with 6 degrees of freedom (3 for
rotation and 3 for translation) and 4 control inputs (one for
the total thrust force Fth and three for the torques ⃗τ ∈R3).
However, the rotational subsystem is fully actuated and can
be written as
˙Xr =

1
2q ⊗⃗Ω
J−1(⃗τ + ⃗γr −⃗Ω× J⃗Ω)

,
(3)
According to [16] and [17], a quaternion logarithm mapping
can be used to define an axis-angle rotational error between
the quadrotor current orientation q and a desired rotational
reference qd as
⃗ϑe := 2 ln(q∗
d ⊗q),
(4)
where q∗
d is the conjugate quaternion of qd, and ⃗ϑe symbol-
izes the quadrotor orientation error expressed in its axis-angle
notation. Considering small changes of qd, its derivative
holds that
˙⃗ϑe = d
dt
⃗ϑe = d
dt2 ln(q∗
d ⊗q) ≈⃗Ω.
(5)
Therefore, the rotational error subsystem can be rewritten as:
˙Xϑe = d
dt
"
⃗ϑe
⃗Ω
#
≈

⃗Ω
J−1(⃗τ + ⃗γr −⃗Ω× J⃗Ω)

.
(6)
Defining the effects of the unknown rotational perturba-
tions and the Coriolis term (which could vary in grasping
tasks), as ⃗γτ = ⃗γr −⃗Ω× J⃗Ω, the rotational error equation is
rewritten as:
˙Xϑe ≈

03×3
I3×3
03×3
03×3

Xϑe +

03×1
J−1(⃗τ + ⃗γτ)

.
(7)
The first control’s goal is to design a nominal controller
stabilizing the system in its linear part and then, propose an
observer that will compensate the nonlinearities components
and the external perturbations. Thus, for the nominal con-
troller the term ⃗γτ ≈[0 0 0]⊺is neglected and therefore, the
controller can be defined as:
⃗τ = J

−2Kpr ln(q∗
d ⊗q) −Kdr⃗Ω

,
(8)
where Kpr and Kdr are positive diagonal matrices containing
the proportional and derivative gains, respectively.
Now, considering the translational subsystem
˙Xt=
"
˙⃗p
q ⊗
⃗Fth
m ⊗q + ⃗g + ⃗γF
#
,
(9)
the nominal controller (8) can ensure that q →qd if ⃗γτ is
properly compensated. Rewriting from (2) the translational
subsystem, it follows that
˙Xt ≈
"
˙⃗p
qd ⊗
⃗Fth
m ⊗qd + ⃗g + ⃗γF
#
.
(10)
171
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:38:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 3

Using the methodology proposed in [16]-[15], a virtual
control force ⃗Fu ∈R3 can be defined as
⃗Fu := qd ⊗
⃗Fth
m ⊗qd + ⃗g,
so that the translational model becomes as follows:
˙Xt ≈

˙⃗p
⃗Fu + ⃗γF

=
03×3
I3×3
03×3
03×3

Xt +
 03×1
⃗Fu + ⃗γF

.
(11)
Since the control force ⃗Fu can be designed using any
control strategy, the desired quaternion qd is determined as
the composition of two quaternions:
qd := qxy ⊗qz,
(12)
where qxy represents the minimal rotation required to align
the thrust vector ⃗Fth with the control force ⃗Fu [17], [15].
This quaternion is derived from the Euler-Rodrigues formula
as:
qxy := ±
v
u
u
u
u
u
t
1+
⃗Fu
∥⃗Fu∥·


0
0
1


2
+
⃗Fu
∥⃗Fu∥×


0
0
1




⃗Fu
∥⃗Fu∥×


0
0
1




v
u
u
u
u
u
t
1−
⃗Fu
∥⃗Fu∥·


0
0
1


2
,
(13)
The second quaternion, qz, introduces a desired rotation
around the z-axis (commonly referred to as the yaw angle),
and it is computed as:
qz = cos
ψd
2

+


0
0
1

sin
ψd
2

,
(14)
where ψd denotes the target yaw orientation.
In order to establish a reference for evaluating control
performance, a proportional-derivative (PD) state feedback
controller has been used to regulate the translational dy-
namics of the quadrotor. Similarly as the rotational error
model, a nominal force control ⃗Fu can be proposed under
the assumption that external disturbances are negligible, i.e.,
⃗γF ≈[0 0 0]⊺. Then,
⃗Fu = −Kpt(⃗p −⃗pd) −Kdt( ˙⃗p −˙⃗pd) −m⃗g,
(15)
where Kpt and Kdt are diagonal, positive-definite gain ma-
trices responsible for the proportional and derivative actions,
respectively. Here, ⃗pd ∈R3 denotes the desired position
vector, while m represents the mass of the quadrotor.
Notice from (15) that ⃗Fu = 0 only when the quadrotor is
on the floor, otherwise the mass is compensated and therefore
(13) is also valid.
The process of computing the desired orientation and
corresponding control inputs can be summarized in the
following steps:
• Compute the control force: Determine the control
force ⃗Fu using Eq. (15), which defines the translational
dynamics based on the desired position and velocity.
• Determine the intermediate quaternion: Substitute
the control force ⃗Fu into Eq. (13) to compute the
intermediate quaternion qxy, representing the alignment
of the thrust vector.
• Incorporate the desired yaw angle: Integrate the
desired yaw angle ψd through Eq. (14) to obtain the
complete target quaternion qd, which fully defines the
desired orientation.
• Apply the control torque: Use Eq. (8) to apply the
necessary control torque that ensures accurate tracking
of the computed quaternion qd.
• Calculate the total thrust: Finally, compute the total
thrust required to maintain the desired trajectory as:
Fth = ∥⃗Fu∥.
(16)
III. UNCERTAINTY AND DISTURBANCE ESTIMATOR
While the nominal controllers defined in Eqs. (8) and (15)
assume an ideal environment without external disturbances
and rely on precise, constant inertial parameters, real-world
scenarios often present unpredictable perturbations. These
disturbances can stem from environmental factors like wind
gusts or, as explored in this work, variations in payload due to
object grasping. To better capture these practical effects, the
rotational and translational dynamics described by Eqs. (7)
and (11) can be reformulated into two decoupled, linear
systems with external disturbances as:
˙Xϑe ≈AϑeXϑe + Bϑe [⃗τ + ⃗γτ] ,
(17)
˙Xt ≈AtXt + Bt
h
⃗Fu + ⃗γF
i
,
(18)
where Aϑe=At:=
03×3 I3×3
03×3 03×3

and Bϑe=Bt:=
03×3
I3×3

.
A. Disturbance rejection controllers
The proposed control strategy involves estimating dis-
turbance forces and torques using two observers based on
the Uncertainty and Disturbance Estimator (UDE) approach
[11]. Specifically, two estimations, ˆ⃗γτ(t) and ˆ⃗γF (t), are
designed to satisfy ˆ⃗γτ(t) →⃗γτ(t) and ˆ⃗γF (t) →⃗γF (t),
respectively. These estimates are then incorporated into the
controllers described in (8) and (15).
1) Rotational subsystem: The control input for the trans-
lational system is defined as:
⃗τ(t) = J

−2Kpr ln(q∗
d ⊗q) −Kdr⃗Ω−ˆ⃗γτ(t)

,
(19)
From the rotational subsystem (17), the reduced-order ob-
server following the UDE design procedure yields
⃗γτ(t) = B+
ϑe
h
˙Xϑe(t) −AϑeXϑe(t) −Bϑe⃗τ(t)
i
,
(20)
where B+
ϑe =

03×3 I3×3
is the pseudoinverse of Bϑe.
Since (20) cannot be directly computed, the following esti-
mation is proposed:
˙ˆ⃗γτ(t) = −Γϑeˆ⃗γτ(t)
+ ΓϑeB+
ϑe
h
˙Xϑe(t) −AϑeXϑe(t) −Bϑe⃗τ(t)
i
,
(21)
172
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:38:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 4

where Γϑe ≜diag(Γϑe1, Γϑe2, . . . , Γϑe6) with Γϑej > 0
for j : {1, . . . , 6}. To avoid the term ˙Xϑe(t), the following
change of variable is applied
ˆξϑe(t) = ˆ⃗γτ(t) −ΓϑeB+
ϑeXϑe(t).
(22)
Taking the derivative of (22) and introducing the system
model results in the reduced-order observer:









˙ˆξϑe(t) =−Γϑe ˆξϑe(t)−
Γ2
ϑeB+
ϑe +ΓϑeB+
ϑeAϑe

Xϑe(t)
−Γϑe⃗τ(t),
ˆ⃗γτ(t) = ˆξϑe(t) + ΓϑeB+
ϑeXϑe(t),
ξϑe(0) =−ΓϑeB+
ϑeXϑe(0).
(23)
2) Translational disturbance rejection:
An estimation
ˆ⃗γF (t) is designed such that ˆ⃗γF (t) →⃗γF (t) and then added
to the controller as
⃗Fu(t) = −Kpt(⃗p−⃗pd)−Kdt( ˙⃗p−˙⃗pd)−m(⃗g+ˆ⃗γF (t)). (24)
From (18), the reduced-order observer following the UDE
design procedure yields
⃗γF (t) = B+
t
h
˙Xt(t) −AtXt(t) −Bt ⃗Fu(t)
i
,
(25)
where B+
t =
03×3 I3×3
is the pseudoinverse of Bt. Since
(25) cannot be directly computed, the following estimation
is proposed:
˙ˆ⃗γF (t) = −Γtˆ⃗γF (t)
+ ΓtB+
t
h
˙Xt(t) −AtXt(t) −Bt ⃗Fu(t)
i
,
(26)
where Γt ≜diag(Γt1, Γt2, . . . , Γt6) with Γtj > 0 for j :
{1, . . . , 6}. To avoid the term ˙Xt(t), we apply the change of
variable
ˆξt(t) = ˆ⃗γF (t) −ΓtB+
t Xt(t).
(27)
Taking the derivative of (27) and introducing the system
model results in the reduced-order observer:









˙ˆξt(t) = −Γt ˆξt(t) −
Γ2
tB+
t + ΓtB+
t At

Xt(t)
−Γt ⃗Fu(t),
ˆ⃗γF (t) = ˆξt(t) + ΓtB+
t Xt(t),
ξt(0) = −ΓtB+
t Xt(0).
(28)
The control strategy is then completed by numerically com-
puting ˆξϑe(t) and ˆξt(t), and introducing systems (23) and
(28) into their respective control laws (19) and (24). Thus,
all the information required by the observers depends on the
system states and control inputs.
IV. RESULTS
This section presents two stages of evaluation. First, nu-
merical simulations are used to compare the performance of a
classical PD controller under three conditions: a) without
estimators, b) with a translational UDE, and c) with
a full UDE (applied to both translational and rotational
dynamics). In addition, the Luenberger estimator, as
described in [18], is also included in the analysis. Second,
experimental results are provided for two scenarios: one
without estimator and the other using the full UDE.
To simplify the analysis, a color code is used in this section
to identify each simulation and experiment.
A. Numerical simulations
The simulations were developed in MATLAB R2024b
with an Euler numerical integrator, with a step-size of 1
[ms], in a personal computer with an i7-13650HX processor
and 32 GB of RAM. The physical parameters of the UAV
were chosen to approximate real flying conditions under a
controlled environment. The mass of the UAV is 0.405 [kg]
and its inertia matrix is defined in (29).The initial conditions
are defined as ⃗p(0) = [0 0 0]⊺[m], and q(0) = [1 0 0 0]⊺.
J =


2098
63.577538
−2.002648
63.577538
2102
0.286186
−2.002648
0.286186
4068

e−6 [kg · m2]
(29)
The desired task corresponds to regulating the Cartesian
position to ⃗pd =
1
2
2⊺[m]. Also, a non-constant
disturbance, in translational coordinates, is considered as
⃗γF =
sin(ωf t)
cos(ωf t)
2 sin(ωf t)⊺with ωf = 0.5
[Hz] ∀t ≥10 [s]. Using the feedback gains for the controller
and observers shown in Table I, the following figures show
a comparison among each simulation performing the same
desired task.
TABLE I: Parameters for numerical simulations.
Simulation
Kpr
Kdr
Kpt
Kdt
Γϑe
Γt
Without
40
8
2
1
-
-
Luenberger
2
0.5
Trans. UDE
-
0.5
Full UDE
15
1
As shown in Fig. 2a, the performance during the first
seconds is the same for all. Once the disturbance is applied,
at t ≥10, the contribution of the observers is used in the
control signals. In particular, the behavior of the full UDE
helps to quickly compensate the error norm as presented
in Fig. 2b, where the error norm from the other methods
remains bounded but not fully compensated. The proposed
rotational estimation proves effective the handling of non-
constant disturbances along the time. This compensation is
also shown in Fig. 2c, where the thrust produced by the full
UDE reaches the required value faster to maintain the UAV
closer to the desired position than the others.
A similar behavior can be seen in Fig. 3, where the
desired positions are reached only under ideal conditions.
However, when non-constant disturbances are applied, the
performance decreases if observers are not used. While the
translational UDE and Luenberger perform capability, the
inclusion of rotational estimations (full UDE) improves the
non-constant disturbances compensation, as shown in Figs.
3a-c. Even though the disturbances in the z-axis are around
50 % of the UAV’s weight, the full UDE reduces the error
more effectively than the translational UDE or Luenberger
observer.
173
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:38:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 5

0
5
10
15
20
25
30
0
0.005
0.01
0.015
0.02
0
5
10
15
20
25
30
0
0.5
1
1.5
2
2.5
3
0
5
10
15
20
25
30
0
2
4
6
8
10
Fig. 2: General comparison of numerical simulations. (a) shows the torque
norm, ||⃗τ||, whereas in (b) the translational error norm ||⃗p −⃗pd|| is
presented. Finally, (c) depicts the applied thrust ⃗Fth.
0
5
10
15
20
25
30
0
0.5
1
1.5
0
5
10
15
20
25
30
0
0.5
1
1.5
2
2.5
3
0
5
10
15
20
25
30
0
0.5
1
1.5
2
2.5
Fig. 3: Comparison of translational regulation to desired position (black
dashed line). (a) illustrates the X coordinate, whereas the Y and Z coordi-
nates are shown in (b) and (c), respectively.
Fig. 4 highlights the advantages of using observers to han-
dle disturbances. In particular, Fig. 4a shows that the accu-
mulative error from the full UDE is the smallest, whereas the
translational UDE and Luenberger behave in a similar way.
Notice also that the full UDE achieves the error convergence
along the time, even subject to non-constant disturbances, as
shown in Fig. 4b. In contrast, the worst case corresponds to
the case without observers, as it is expected, where the error
convergence is not achieved. Likewise, the full UDE has the
fastest response as depicted in Fig. 4c, whereas the others
are continuously dealing with the disturbances even when
they were applied a few seconds before. A summary of the
metrics, as well as the error mean and its standard deviation,
is presented in Table II.
0
5
10
15
20
25
30
0
10
20
0
5
10
15
20
25
30
0
2
4
6
8
10
0
5
10
15
20
25
30
0
50
100
150
200
250
Fig. 4: Error metric analysis of numerical simulations. (a) depicts the
Integral Absolute Error (IAE), (b) shows the Integral Squared Error (ISE),
and (c) presents the Integral Time Absolute Error (ITAE).
TABLE II: Summary of simulation results.
Simulation
IAE [m]
ISE [m²]
ITAE [m·s]
Mean
Std. Dev.
Without
16.1198
8.0793
221.4028
0.0066
0.3419
Luenberger
11.6928
6.3339
126.3605
0.0165
0.3289
Trans. UDE
10.4555
6.0484
105.5268
0.0176
0.3241
Full UDE
6.4931
5.5243
24.1687
0.0266
0.3184
* The mean and standard deviation are given in meters.
B. Experimental results
Based on the numerical simulation results, the full UDE
is expected to offer strong performance under non-constant
disturbances. Therefore, two study cases were proposed
to evaluate properly its behavior. The first study case
corresponds to using only the PD controller without
observers, as described in (8) and (15), whereas the
174
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:38:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 6

second one includes the full UDE, based on (19) and
(24). A video of the second experiment is available at:
https://youtu.be/z2qvN5186J4.
These experimental results were obtained using Fl-AIR
(Framework libre AIR) [19], an open-source C++ platform
designed for deploying robotic applications, especially for
UAVs. In Fig. 5, the general experimental setup is presented,
where a Parrot AR.Drone 2.0 was equipped with a passive
gripper mounted on its underside to grasp a target object. The
OptiTrack [20] motion capture system is used to measure
the position of the UAV and the target object, while the
attitude in quaternions and angular velocities are given by
the UAV’s internal Inertial Measurement Unit (IMU). The
onboard computer processes the OptiTrack and IMU data
to compute the control signal, as well as the full UDE, to
perform the desired task. Notice that the ground station only
works as a monitor, which helps to reduce response time.
Fig. 5: Experimental setup and desired task. This trajectory was desgined
to evaluate the UAV’s behavior while it is transporting an object, which
generates torques on each axis due to its own inertial matrix.
The proposed task consists of taking the UAV off to
regulated to the initial position Pinit. Once stabilized, the
target position then is acquired to compute a quintic poly-
nomial trajectory, which will be followed until reaching a
preparatory position above the object Pprep, defined with a
z-offset. Then, the UAV descends to take the object at Pobject
and subsequently returns to the preparatory position Pprep.
Finally, the UAV transports the object to the initial position
Pinit, as depicted in Fig. 5. The use of a quintic polynomial
trajectory ensures a smooth and feasible motion path that
satisfies the constraints on position and velocity.
TABLE III: Parameters for experimental results.
Experiment
Kpr
Kdr
Kpt
Kdt
Γϑe
Γt
Without
1.2
0.15
0.2
0.1
-
-
Full UDE
5
1
The controller and observer parameters used in the ex-
periments are presented in Table III. These parameters were
tuned based on the original weight of the UAV (without the
gripper and the weight of the object), in order to properly
evaluate the estimation capabilities and the real performance
of the PD controller when the conditions change. The weight
of the gripper is 0.04 [kg], and the object is 0.13 [kg], which
is less than the recommended maximum payload [14].
Fig. 6a illustrates how the control torques present a
bounded behavior in both experiments. However, the torques
applied in the full UDE generally remain more consis-
tent, as a consequence of the estimation. In contrast, the
experiment without estimation requires greater variations
in torque, which could imply a higher power demand. A
similar situation occurs in Fig. 6b, where the error norm
is continuously increasing given that the initial tuning is not
adequate for the new mass and inertial matrix of the system if
any observer is used. This is due to the controller being tuned
for the original system parameters, which do not account for
the added mass and the altered inertial matrix. In contrast, the
full UDE correctly compensates these changes, maintaining
performance even during the object manipulation phase,
particularly during the ascent from Pobject to Pprep, which
could be a potentially critical point in the task.
Notice
that this estimation also impacts the thrust signal, where the
full UDE maintains a nominal value even during the object
grasping phase, as demonstrated in Fig. 6c.
Fig. 6: General comparison of experimental results. The torque norm ||⃗τ||
is presented in (a), the translational error norm ||⃗p −⃗pd|| is shown in (b),
and the applied thrust ⃗Fth is depicted in (c).
Fig. 7a shows how the full UDE adequately handles the
accumulative error, which highlights its robustness during
all the grasping tasks performed. Similarly, it is capable
of compensating for large errors that could directly affect
the accuracy of the task, as Fig. 7b indicates, maintaining
175
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:38:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 7

2
4
6
8
10
12
14
16
0
20
40
2
4
6
8
10
12
14
16
0
10
20
30
40
2
4
6
8
10
12
14
16
0
100
200
300
400
500
Fig. 7: Error metric analysis of experimental results. (a) depicts the Integral
Absolute Error (IAE), (b) shows the Integral Squared Error (ISE), and (c)
indicates the Integral Time Absolute Error (ITAE).
stable flight. Moreover, the quick response of the full UDE
allows a reduction in the ITAE metric (Fig. 7c), ensuring
good performance. Finally, a summary of the experimental
results is presented in the Table IV.
TABLE IV: Summary of experimental results.
Experiment
IAE [m]
ISE [m²]
ITAE [m·s]
Mean
Std. Dev.
Without
36.0900
39.4965
428.5023
0.3382
1.75600
Full UDE
4.9567
0.9799
46.2604
0.1080
0.2411
* The mean and standard deviation are given in meters.
V. CONCLUSION AND FUTURE WORK
This paper presented a full-state observer controller based
on quaternions, which was validated through numerical
simulations and experiments in grasping tasks. The nu-
merical simulations demonstrated the advantages of using
a quaternion-based observer to effectively compensate for
unknown parameters and external, non-constant disturbances
such as varying mass.
As a result, the proposed approach can be applied in
various scenarios where traditional controllers may require
re-tuning or prior knowledge about the task. Experimental
results, obtained using a Parrot AR.Drone 2.0 in a grasping
task, showed low cumulative errors, robustness, and faster
responses, as indicated by the IAE, ISE, and ITAE metrics.
The findings of this paper encourage further research
on improving controllers, particularly observers, to enhance
the performance of traditional controllers under varying
conditions. With advances in artificial intelligence, observers
could integrate adaptive laws to use external information to
improve task performance over time.
ACKNOWLEDGMENTS
This work was supported by the Grant 1144112 of the
SECIHTI of Mexico Government and a MESR scholarship
in France and by the School of Engineering and Sciences at
Tecnológico de Monterrey, Guadalajara Campus, Mexico.
REFERENCES
[1] V. S. Kumar, M. Sakthivel, D. A. Karras, S. K. Gupta, S. M. P.
Gangadharan, and B. Haralayya, “Drone surveillance in flood affected
areas using firefly algorithm,” in 2022 International Conference on
Knowledge Engineering and Communication Systems (ICKES), pp. 1–
5, IEEE, 2022.
[2] W. R. Roderick, M. R. Cutkosky, and D. Lentink, “Bird-inspired
dynamic grasping and perching in arboreal environments,” Science
Robotics, vol. 6, no. 61, p. eabj7562, 2021.
[3] S.-J. Kim, D.-Y. Lee, G.-P. Jung, and K.-J. Cho, “An origami-inspired,
self-locking robotic arm that can be folded flat,” Science Robotics,
vol. 3, no. 16, p. eaar2915, 2018.
[4] J. S. Patel, C. Al-Ameri, F. Fioranelli, and D. Anderson, “Multi-time
frequency analysis and classification of a micro-drone carrying pay-
loads using multistatic radar,” The Journal of Engineering, vol. 2019,
no. 20, pp. 7047–7051, 2019.
[5] M. Hassanalian and A. Abdelkefi, “Classifications, applications, and
design challenges of drones: A review,” Progress in Aerospace Sci-
ences, vol. 91, pp. 99–131, 2017.
[6] M. Ayamga, S. Akaba, and A. A. Nyaaba, “Multifaceted applicability
of drones: A review,” Technological Forecasting and Social Change,
vol. 167, p. 120677, 2021.
[7] H. Zhang, E. Lerner, B. Cheng, and J. Zhao, “Compliant bistable grip-
pers enable passive perching for micro aerial vehicles,” IEEE/ASME
Transactions on Mechatronics, vol. 26, no. 5, pp. 2316–2326, 2020.
[8] O. B. Schofield, K. H. Lorenzen, and E. Ebeid, “Cloud to cable: A
drone framework for autonomous power line inspection,” in 2020 23rd
Euromicro Conference on Digital System Design (DSD), pp. 503–509,
IEEE, 2020.
[9] M. Lieret, J. Lukas, M. Nikol, and J. Franke, “A lightweight, low-cost
and self-diagnosing mechatronic jaw gripper for the aerial picking with
unmanned aerial vehicles,” Procedia Manufacturing, vol. 51, pp. 424–
430, 2020.
[10] W.-H. Chen, J. Yang, L. Guo, and S. Li, “Disturbance-observer-based
control and related methods—an overview,” IEEE Transactions on
industrial electronics, vol. 63, no. 2, pp. 1083–1095, 2015.
[11] A. Castillo, R. Sanz, P. Garcia, and P. Albertos, “Robust design of the
uncertainty and disturbance estimator,” IFAC-PapersOnLine, vol. 50,
no. 1, pp. 8262–8267, 2017.
[12] A. Moeini, A. F. Lynch, and Q. Zhao, “A backstepping disturbance
observer control for multirotor uavs: Theory and experiment,” Inter-
national Journal of Control, vol. 95, no. 9, pp. 2364–2378, 2022.
[13] J. Chen, R. Sun, and B. Zhu, “Disturbance observer-based control for
small nonlinear uav systems with transient performance constraint,”
Aerospace Science and Technology, vol. 105, p. 106028, 2020.
[14] D. Gandulfo, A. Varela, P. Castillo, and H. Abaunza, “Quaternion-
based observer control for multirotor uavs, an application to unactuated
grasping,” in 2024 International Conference on Unmanned Aircraft
Systems (ICUAS), pp. 1347–1353, IEEE, 2024.
[15] J. Cariño, H. Abaunza, and P. Castillo, “A fully-actuated quadcopter
representation using quaternions,” International Journal of Control,
vol. 96, no. 12, pp. 3132–3154, 2023.
[16] H. Abaunza, Robust tracking of dynamic targets with aerial vehicles
using quaternion-based techniques. PhD thesis, Université de Tech-
nologie de Compiègne, 2019.
[17] J. Carino, H. Abaunza, and P. Castillo, “Quadrotor quaternion control,”
in 2015 International Conference on Unmanned Aircraft Systems
(ICUAS), pp. 825–831, IEEE, 2015.
[18] V. Léchappé, M. Cirrincione, and Q.-L. Han, “Approximation of the
disturbance dynamics by extended state observer using an artificial
delay,” in 21st IFAC World Congress, (Berlin (Virtual), Germany),
July 2020.
[19] G.
Sanahuja,
“FL-AIR
(Framework
Libre
Air),”
https://gitlab.utc.fr/uav-hds/flair/flair-src, 2025.
[20] OptiTrack, “Motion capture systems,” https://optitrack.com, 2025.
176
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:38:23 UTC from IEEE Xplore.  Restrictions apply.
