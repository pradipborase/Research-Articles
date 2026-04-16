# A_Practical_Perspective_on_the_Drone-With-a-Slung-Load_Problem.pdf

## Page 1

A practical perspective on the drone-with-a-slung-load problem
Fateme Aghaee1, Karam Eliker1, and Jerome Jouffroy1
Abstract— Controlling a system consisting of a drone carry-
ing a payload with a cable is a problem of practical importance
within UAV control. Contrarily to previous work, this paper
investigates a control scheme for this problem where neither
the deviation angles of the cable nor the mass of the load
are known or measured, with an emphasis on simplicity and
applicability on a wide array of available flight controllers.
Our approach combines differential-algebraic considerations
for motion planning and trajectory generation, together with
simple controllers used for feedback. Simulation results are
proposed to illustrate the potential of the approach.
I. INTRODUCTION
In the area of UAV control, control of multirotors with a
load suspended by a cable, also referred to as slung-load has
gained significant popularity over the past few years [1]–[4].
Regarding control design, it is indeed an interesting problem,
the system under consideration being nonlinear, underactu-
ated, and presenting potentially challenging oscillations. But
it is also practically relevant: in terms of mechanism, it is
indeed generally easy or convenient to attach a load to a
cable suspended under a drone using simple attachments and
hooks, especially when compared to having a special device
to place/retain a payload rigidly under a multirotor drone.
Among the different approaches used to address this
control problem, differential flatness has gained significant
attention [5], [6]. Seen as an extension of controllability for
nonlinear systems, flatness allows the parametrization of a
system state and inputs using the so-called flat outputs and
a finite number of their derivatives. One of the many advan-
tages of such a perspective is to allow one to perform motion
planning in a simple manner, without solving differential
equations.
However, the vast majority of the above-cited studies
use the knowledge of the mass of the load, as well as
measurement of the angles between the load and the drone
as starting assumptions in order to solve the control problem.
With regard to actual drone operations, this is rarely the
case in practice. Indeed, the load mass is meant to change
as per the requirements of the mission and is not always
known in advance, while measuring the deflection angles
of the cable for an outdoor operation requires a sensing
mechanism attached under the drone, typically an unactuated
gimbal equipped with encoders. Nonetheless, many drones
transporting loads with cables do not currently use such
mechanisms (see for example [7]).
While a somewhat straight approach to tackle a lack
of information regarding the load mass and its deflection
1
Department of Mechanical and Electrical Engineering, Univer-
sity
of
Southern
Denmark,
Alsion
2,
6400
Sønderborg,
Denmark
aghaee@sdu.dk, karameliker@sdu.dk, jerome@sdu.dk
angles would consist in an estimation scheme for all miss-
ing measurements, doing so is not with different potential
pitfalls such as difficulty in design, analysis and, especially
important for practical reasons, tuning. In order to retain
the advantages and performances of differential flatness, this
paper will use the latter technique, but taking a slightly
different perspective than current studies on drone control.
Indeed, taking as the starting point earlier references on crane
control using flatness (see [8], [9] and [10], we only perform
the nonlinear controllability analysis and subsequent motion
planning on a subpart or projection of the drone-slung-load
dynamical model not directly involving the load mass nor
the deflection angles. This is especially useful for rest-to-
rest trajectories that are of primary importance with regard
to practice in operational scenarios. Once the main part of
control decisions is taken care of by motion planning, model
inaccuracies and kinetics (including the unknown load mass)
can be compensated for by a simple feedback controller, here
materialized by a well-known active disturbance rejection
controller (ADRC).
The rest of this paper is organized as follows. Section II
briefly introduces and motivates the drone-with-a-slung-load
model. Then, Section III considers a selection of a part of
this model and proves its flatness property. In Section IV,
we present the control architecture of our approach, which
includes motion planning and feedback control, with a focus
on simplicity and practicality, while Section V illustrates
the approach with a few simulation results. Brief concluding
remarks end this paper.
II. MODELLING
Consider a drone carrying a payload by an attached cable
as shown in Figure 1. The variables used in this paper are
listed in Table I.
In the following, we make the following assumptions
about the system (see also [11] for similar assumptions):
• The attached cable is mass-less and taut and installed
at the mass center of the drone.
• The payload is always situated under the drone, i.e.
the swing angles α and β are within the range of
(−π/2, π/2).
• The drone and the payload are both assumed to be point
masses, and the effect of aerodynamics on the drone,
cable, and payload are neglected.
Note that the cable suspending the load being attached
to the center of the gravity (COG) of the drone, the payload
will not have any effect on the rotational motion of the drone
[12].
2024 International Conference on Unmanned Aircraft Systems (ICUAS)
June 4-7, 2024. Chania, Crete, Greece
979-8-3503-5788-2/24/$31.00 ©2024 IEEE
899
2024 International Conference on Unmanned Aircraft Systems (ICUAS) | 979-8-3503-5788-2/24/$31.00 ©2024 IEEE | DOI: 10.1109/ICUAS60882.2024.10557054
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:38:15 UTC from IEEE Xplore.  Restrictions apply.

## Page 2

Fig. 1: Pendulum angle parametrization for the drone with
cable-suspended cable
TABLE I: Symbol Definitions
Symbol
Definition
m, mp ∈R
Mass of the drone and the payload
g ∈R
Gravitational constant
I
Inertial frame
Bp, B
Payload and drone body frame
p = [x, y, z]⊤∈R3
Position of the drone in I
pp = [xp, yp, zp]⊤∈R3
Position of the payload in I
α, β ∈R
Swing angles of the payload
l ∈R
Cable length
η = [p⊤, α, β]⊤∈R5
Generalized coordinates vector
R ∈SO(3)
Rotation matrix from B to I
f ∈R
Thrust directed along negative z-
axis in B
F = [F1, F2, F3]⊤∈R3
Inertial control force
w = [w1, w2, w3]⊤∈R3
Additional environment forces and
disturbances
P, K ∈R
Potential and kinetic energy
M(η) ∈R5×5
Mass matrix
C(η, ˙η) ∈R5×5
Coriolis matrix
G(η) ∈R5
Gravity vector
Mij, Cij, Gij ∈R
An array of matrix with i and j as
the row and column
T ∈R
Tension on the cable
uF F , uF B ∈R3
Feedforward and feedback control
pd = [xd, yd, zd]⊤∈R3
Desired position of the drone
cd, ρ ∈R
Drag coefficient, air density
vr, vwind ∈R3
Relative and wind velocity
A ∈R3
Reference area
lx, ly, lz ∈R
Length, width and height of drone
The geometric constraint between the drone and payload
positions (see Figure 1) is expressed by
pp = p + L
(1)
with
L =


sin β
−sin α cos β
cos α cos β

l,
(2)
where l is the length of the cable, and α, β are the swing
angles of the payload.
A dynamical model of the drone-payload system can be
obtained by the Lagrangian method [13]. Considering η =
[p⊤, α, β]⊤, the Euler-Lagrange equations with respect to η
are given by
d
dt
∂E
∂η

−∂E
∂˙η = τ + τd,
(3)
where the Lagrangian is E = K −P, the generalized forces
vector is τ = [F⊤, 01×2]⊤and F = fRez with ez =
[ez,1, ez,2, ez,3] = [0, 0, 1]⊤. The additional environmental
forces disturbances such as wind are shown in the τd =
[w⊤, 01×2]⊤. The potential and kinetic energy of the drone-
payload system are
P = −g(mz + mpzp)
(4)
K = 1
2
m( ˙p)⊤p + mp( ˙pp)⊤pp
(5)
so that we have the dynamical model
M(η)¨η + C(η, ˙η) ˙η + G(η) = τ + τd
(6)
where the elements of the mass matrix M are





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





M11 = M22 = M33 = m + mp,
M44 = mpl2 cos2(β)
M55 = mpl2
M15 = M51 = mpl cos(β)
M24 = M42 = −mpl cos(α) cos(β)
M25 = M52 = mpl sin(α) sin(β)
M12 = M13 = M14 = M21 = M23 = 0
M31 = M32 = M41 = M45 = M54 = 0
(7)
while the elements of the Coriolis matrix C are








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








Cij = 0,
for
i = 1, 2, 3
and
j = 1, 2, . . . , 5
C14 = C55 = 0
C15 = −mpl ˙β sin(β)
C24 = mpl( ˙α sin(α) cos(β) + ˙β sin(β) cos(α))
C25 = mpl( ˙α sin(β) cos(α) + ˙β sin(α) cos(β))
C34 = mpl( ˙β sin(α) sin(β) −˙α cos(β) cos(α))
C35 = mpl( ˙α sin(α) sin(β) −˙β cos(α) cos(β))
C44 = −mpl2( ˙β cos(β) sin(β)
C45 = −C54 = mpl2 ˙α cos(β) sin(β)
(8)
and the elements of the gravity vector G are given by







G11 = G21 = 0
G31 = −(mp + m)g
G41 = mpgl cos(β) sin(α)
G51 = mpgl cos(α) sin(β)
.
(9)
Since the mass matrix M(η) is invertible, a state-space form
of dynamical model (6) can easily be obtained.
Note that there are alternative ways to describe the above
drone-payload system. Indeed, a straightforward and equiva-
lent Newtonian approach would introduce a force represent-
ing the tension in the cable, so that we would have
m¨p = F + mgez + fT + w,
(10)
where the force vector along the cable fT is given by
fT =


sin β
−sin α cos β
cos α cos β

T.
(11)
900
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:38:15 UTC from IEEE Xplore.  Restrictions apply.

## Page 3

Then, the payload dynamics are simply expressed as
mp¨pp = −fT + mpgez.
(12)
III. DIFFERENTIAL FLATNESS
This section briefly recalls the definition of differential
flatness and proves the flatness property of a subset of the
drone-with-a-slung-load system.
A system is differentially flat if one can find a set of
outputs such as the states and the inputs of the system can
be written as functions of these outputs. Following [14], the
definition of a flat system is given as follows.
Definition 1: A nonlinear system
˙x = g(x, u)
(13)
where x ∈Rn and u ∈Rm, is differentially flat if there is
a vector σ called flat output, consisting of m differentially
independent variables functions of the state, the input, and
its derivatives, ie we have
σ = ζ(x, u, ˙u, ..., u(s−1))
(14)
such that the state and the input vectors are functions of the
flat output and its derivatives, ie we have
x = µ(σ, ˙σ, ¨σ, . . . , σ(q−1))
(15)
and
u = ν(σ, ˙σ, ¨σ, . . . , σ(q)),
(16)
where α, µ and ν are vectors of smooth functions and s and
q are finite indices.
In the following, we will focus on the differential-algebraic
equations (DAEs) describing the pendulum behavior of the
drone-payload system represented in (1)-(2) and (11)-(12)
and prove its flatness property. Note that, in doing so, the
variable p representing the drone position is here regarded
as an input.
Theorem 1: The system consisting of (1)-(2) and (11)-
(12) with dynamic variables pp, T, α, β and input p is dif-
ferentially flat, with σ = [σx, σy, σz]⊤= pp = [xp, yp, zp]⊤
as flat output.
Proof:
Rewriting DAEs (11)-(12) using flat output(s)
σ = pp gives
mp¨σx
=
−T sin β
(17)
mp¨σy
=
T sin α cos β
(18)
mp(¨σz −g)
=
−T cos α cos β.
(19)
To obtain T as a function of σ and its derivatives, square
(17),(18),(19) and add them together to get
m2
p
¨σ2
x + ¨σ2
y + (¨σz −g)2
= T 2
(20)
whereby, since cable tension T ≥0 by assumption, T is
readily obtained after a square root. Then, divide (18) by
(19) to get
tan α =
¨σy
g −¨σz
,
(21)
so that α is computed thanks to the arctan function. Having
equation (21) to the corresponding sine function expression
sin α =
¨σy
q
¨σ2y + (¨σz −g)2 .
(22)
Replace sin α in equation (18) using (22), and divide eq. (17)
by eq. (18) to get
tan β = −
¨σx
q
¨σ2y + (¨σz −g)2
(23)
so that we have β as functin of σ and derivatives.
Then, rewrite equations (1)-(2) as
σx −x
=
l sin β
(24)
σy −y
=
−l sin α cos β
(25)
σz −z
=
l cos α cos β.
(26)
Notice that eq. (19) multiplied by eq. (25) is equal to eq.
(18) multiplied by eq. (26), while eq. (19) multiplied by eq.
(24) is equal to eq. (17) multiplied by eq. (26), so that we
have
(¨σz −g)(σy −y)
=
¨σy(σz −z)
(27)
(¨σz −g)(σx −x)
=
¨σx(σz −z).
(28)
Squaring all (24)-(26) equations and add them to get the
obvious expression
(σx −x)2 + (σy −y)2 + (σz −z)2 = l2
(29)
from which it can easily be inferred that z is a function of
corresponding to the length constraint on the cable. Isolating
σy −y in (27) and σx −x in (28), use these expressions in
(29) to obtain
σz −z =
l(¨σz −g)
q
¨σ2x + ¨σ2y + (¨σz −g)2 ,
(30)
from which it can easily be inferred that z is a function of
σ and derivatives. Finally, use again relations (27) and (28)
to obtain
σy −y =
l¨σy
q
¨σ2x + ¨σ2y + (¨σz −g)2
(31)
and
σx −x =
l¨σx
q
¨σ2x + ¨σ2y + (¨σz −g)2
(32)
which completes the proof of our theorem.
Note that expressions (27)-(29) are inspired by earlier
work on Flatness applied on gantry cranes by Fliess et al.
[8], and predating their seminal paper [14]. Remarkably but
somewhat unsurprisingly, these dynamic equations do not
depend on the mass parameter of the payload, as is known
in the related standard dynamic behavior of an undamped
pendulum.
901
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:38:15 UTC from IEEE Xplore.  Restrictions apply.

## Page 4

IV. CONTROL DESIGN
The overall structure of the control system, shown in Fig-
ure 2, consists of a simple tracking controller, with feedback
on the position of the drone based on the well-known ADRC
paradigm (see for example [15]). The desired positions of
the drone over time are obtained thanks to the developments
of the previous section, such that the former are, in turn,
functions of the desired trajectories of the payload.
From a control perspective and seen from the drone, the
model used is now
m¨p = F + mgez + mh(p, ˙p, w, fT )
(33)
where the term h(p, ˙p, w, fT ) gathers the effect of the
unknown tension, unmodelled dynamics and external distur-
bances. The structure of our controller is expressed as
F
=
m¨pd −mgez
+
KP (ˆp −pd) + KD(ˆ˙p −˙pd) −mˆh
(34)
where the two first terms are feedforward terms, and the
three next terms come from the linear ADRC controller,
with ˆp, ˆ˙p, ˆh being estimates provided by an Extended-State
Observer (ESO). Time-varying term pd(t) is the desired
trajectory of the drone. These different elements are detailed
below.
A. Extended-State Observer
Using the well-known ESO concept, rewrite the above
dynamics (33) as
˙q1 = q2
˙q2 = 1
mF + gez + q3
˙q3 = ˙h(p, ˙p, w, fT ),
(35)
with q1 := p, q2 := ˙p and q3 := h (note that the first
time-derivative of h is assumed to be bounded).
The corresponding ESO reads
˙ˆq1 = ˆq2 + B1(q1 −ˆq1)
˙ˆq2 = 1
mF + gez + ˆq3 + B2(q1 −ˆq1)
˙ˆq3 = B3(q1 −ˆq1),
(36)
where the observer gain matrices B1, B2 and B3 are chosen
as diagonal matrices with each term i of the diagonal tuned
using the parametrized pole placement technique, ie b1,i =
3ωi, b2,i = 3.2ω2
i , b3,i = ω3
i , and ωi > 0 is the observer
bandwidth.
The related control parameters KP , KD in (34), again diag-
onal matrices, are chosen in such a way that s2+KDs+KP
is Hurwitz.
B. From drone to payload desired trajectories
As we have seen in the previous section and the differential
flatness property of a subset of the overall model, the position
of the drone can be obtained by relatively simple functions
of the position of the payload and its derivatives. Hence the
desired drone position trajectory pd = [xd, yd, zd]⊤can also
Fig. 2: The structure of the control system
be obtained as functions of desired payload trajectories, ie
we have
xd = σx,d −
l¨σx,d
q
¨σ2
x,d + ¨σ2
y,d + (¨σz,d −g)2
(37)
yd = σy,d −
l¨σy,d
q
¨σ2
x,d + ¨σ2
y,d + (¨σz,d −g)2
(38)
zd = σz,d −
l(¨σz,d −g)
q
¨σ2
x,d + ¨σ2
y,d + (¨σz,d −g)2 ,
(39)
and similarly for the derivatives ˙pd and ¨pd necessary to
controller (34).
C. Payload Trajectory Generation
To define the desired payload trajectories, polynomials are
used because of their computer efficiency. Furthermore, the
desired trajectories should be defined so that the position,
velocity, acceleration, and their derivatives up to the fourth
order (ie following for example (39), the second-derivative
of the drone position depends on the fourth derivative of the
payload position) be sufficiently smooth. Therefore, we take
ten boundary conditions (ie five initial conditions and five
final conditions), meaning a polynomial of order n = 9. A
polynomial trajectory is expressed as
σκ,d(t) = a9t9 + a8t8 + a7t7 + . . . + a1t + a0
(40)
where κ = [x, y, z]. Consider the polynomial coefficients put
in vector form
a = [a9, a8, . . . , a0]⊤
(41)
and the corresponding time vector
λ(t) = [t9, t8, . . . , t2, t, 1],
(42)
where time variable t is defined on interval t ∈[t0; tf], t0 =
0 is the starting time of the trajectories and tf is the time
for which the trajectories should reach their final values. The
boundary conditions are specified in c as
c(t) = [σκ,d(t0), ˙σκ,d(t0), ¨σκ,d(t0), σκ,d(t0)(3), σκ,d(t0)(4),
σκ,d(tf), ˙σκ,d(tf), ¨σκ,d(tf), σκ,d(tf)(3), σκ,d(tf)(4)]⊤(43)
and define Λ as a matrix of λ and its derivatives evaluated
at the initial and final times as
Λ(t) = [λ(t0), ˙λ(t0), ¨λ(t0), λ(t0)(3), λ(t0)(4),
λ(tf), ˙λ(tf), ¨λ(tf), λ(tf)(3), λ(tf)(4)]⊤.
(44)
902
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:38:15 UTC from IEEE Xplore.  Restrictions apply.

## Page 5

Then, the coefficients a can simply be obtained as
a = Λ−1c,
(45)
so that we desired trajectories σκ,d(t) can be calculated by
using (45) in (40).
V. SIMULATION STUDY
To illustrate the potential of the proposed control architec-
ture, a simulation in MATLAB/Simulink was implemented
for the 3D model of the drone-payload system presented
in section II. The parameters considered in the model are
assumed to be m = 70kg, mp = 100kg, l = 14.4m, and
g = 9.81m/s2 and inspired by [7]. By using these parameters,
we wish to simulate a scenario that is closer to real-world
circumstances, enabling us to evaluate the applicability and
efficacy of our suggested control structure.
The initial velocity of the drone is considered to be zero.
We aim to transfer the payload from a desired initial state
to a desired final state in a desired time duration by the
attached cable with a length of l from the COG of the drone.
Furthermore, to evaluate the robustness of the proposed
control, a sudden disturbance at t = 10s is injected into
the system. For the simulation test, the disturbance force
approximates the effect of the wind with velocity of 10
m/s. For this, we use basic aerodynamic calculations with
w = 1
2cdρA · v2
r with reference area A = [lylz, lxlz, lxly]⊤
and relative velocity of vr = ˙p −vwind. The magnitude of
the disturbance force for a wind speed with a magnitude of
10 m/s, drone dimensions 1.6 × 1.6 × 0.412m, ρ = 1.225
and cd = 0.4 is shown in Figure 3.
Fig. 3: The magnitude of the injected disturbance force
Figure 4 shows the displacement of the load carried by
the drone with the cable in 3D from the initial position
of pp
0 = [4, 2, −17.4]⊤to the desired position of pp
d =
[18, 20, −23.4]⊤in tf −t0 = 18s. In Figure 5 the reference
trajectories σx,d, σy,d and σz,d start at t0 from the initial
position, and reach the desired position in 18s where the
load follows these trajectories. Furthermore, the reference
trajectories σx,d, σy,d, and σz,d are smooth functions to
ensure a minimum number of oscillations for α and β during
the transient and after the transfer duration. In particular, the
departure and arrival must be sufficiently smooth. It means
that ˙σκ,d = ¨σκ,d = σκ,d(3) = σκ,d(4) = 0 at t0 = 0s
and tf = 18s. Furthermore, there is significant resilience
against external disturbances since the external disturbances
Fig. 4: Payload displacement with the drone with the attached
cable
Fig. 5: The position of the payload as the flat output and its
reference
Fig. 6: The position of the drone and its reference
injected into the system at t = 10s are quickly damped down
and attenuated. Figure 6 shows the drone’s position which
903
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:38:15 UTC from IEEE Xplore.  Restrictions apply.

## Page 6

Fig. 7: The magnitude of inertial control force
Fig. 8: The rotational angles of the cable
follows its reference.
Figure 7 displays the inertial control force, and the rota-
tional angles of the cable are shown in Figure 8.
It is clear from these simulation results that the slung pay-
load can be smoothly transported from the desired starting
position to the desired final position.
VI. CONCLUDING REMARKS
In the present work, we looked at drone-with-a-slung-load
problem with primary objective the position of the load.
With the mass of the load not always known in practice,
we proposed a controller architecture whereby the focus was
simplicity, so the approach can be used with many different
attitude controllers, and did not need the knowledge of the
above-mentioned mass nor the deviation angles of the cable.
Contrarily to most current work, the core of our approach
relies on the use of differential flatness on only a part of
the overall drone-payload dynamics. Future work will focus
on further robustness characterization and extensions of the
proposed approach.
REFERENCES
[1]
S. Yang, B. Xian, J. Cai, and G. Wang, “Finite-time
convergence control for a quadrotor unmanned aerial
vehicle with a slung load,” IEEE Transactions on
Industrial Informatics, 2023.
[2]
G. Yu, J. Reis, D. Cabecinhas, R. Cunha, and C.
Silvestre, “Reduced-complexity active disturbance re-
jection controller for quadrotor-slung-load transporta-
tion,” IEEE Transactions on Systems, Man, and Cy-
bernetics: Systems, 2023.
[3]
S. Yang and B. Xian, “Energy-based nonlinear adap-
tive control design for the quadrotor uav system with a
suspended payload,” IEEE Transactions on Industrial
Electronics, vol. 67, no. 3, pp. 2054–2064, 2019.
[4]
J. E. Sierra-Garc´ıa and M. Santos, “Intelligent control
of an uav with a cable-suspended load using a neural
network estimator,” Expert Systems with Applications,
vol. 183, p. 115 380, 2021.
[5]
K. Sreenath, T. Lee, and V. Kumar, “Geometric control
and differential flatness of a quadrotor uav with a
cable-suspended load,” in 52nd IEEE Conference on
Decision and Control, IEEE, 2013, pp. 2269–2274.
[6]
J. Zeng, P. Kotaru, M. W. Mueller, and K. Sreenath,
“Differential flatness based path planning with direct
collocation on hybrid modes for a quadrotor with
a cable-suspended payload,” IEEE Robotics and Au-
tomation Letters, vol. 5, no. 2, pp. 3074–3081, 2020.
[7]
“Flyingbasket introduces the fb3 heavy-lift drone.”
(January 12, 2024), [Online]. Available: https://
flyingbasket.com/fb3-order.
[8]
M. Fliess, J. L´evine, and P. Rouchon, “A simplified
approach of crane control via a generalized state-
space model,” in [1991] Proceedings of the 30th IEEE
Conference on Decision and Control, IEEE, 1991,
pp. 736–741.
[9]
B. Kiss, J. L´evine, and P. Mullhaupt, “A simple
output feedback pd controller for nonlinear cranes,” in
Proceedings of the 39th IEEE Conference on Decision
and Control (Cat. No. 00CH37187), IEEE, vol. 5,
2000, pp. 5097–5101.
[10]
B. Kiss, J. L´evine, and P. Mullhaupt, “Control of a
reduced size model of us navy crane using only motor
position sensors,” in Nonlinear control in the year
2000 volume 2, Springer, 2001, pp. 1–12.
[11]
E. L. de Angelis, F. Giulietti, and G. Pipeleers, “Two-
time-scale control of a multirotor aircraft for sus-
pended load transportation,” Aerospace Science and
Technology, vol. 84, pp. 193–203, 2019.
[12]
K. Klausen, T. I. Fossen, and T. A. Johansen, “Non-
linear control with swing damping of a multirotor uav
with suspended load,” Journal of Intelligent & Robotic
Systems, vol. 88, pp. 379–394, 2017.
[13]
R. Mahony, V. Kumar, and P. Corke, “Multirotor
aerial vehicles: Modeling, estimation, and control of
quadrotor,” IEEE robotics & automation magazine,
vol. 19, no. 3, pp. 20–32, 2012.
[14]
M. Fliess, J. L´evine, P. Martin, and P. Rouchon, “Flat-
ness and defect of non-linear systems: Introductory
theory and examples,” International journal of control,
vol. 61, no. 6, pp. 1327–1361, 1995.
[15]
Z. Gao, “Active disturbance rejection control: A
paradigm shift in feedback control system design,” in
2006 American control conference, IEEE, 2006, 7–pp.
904
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:38:15 UTC from IEEE Xplore.  Restrictions apply.
