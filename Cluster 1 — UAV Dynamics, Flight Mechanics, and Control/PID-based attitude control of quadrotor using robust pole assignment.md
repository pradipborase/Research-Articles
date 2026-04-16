# PID-based attitude control of quadrotor using robust pole assignment.pdf

## Page 1

International Journal of Dynamics and Control (2024) 12:2385–2397
https://doi.org/10.1007/s40435-023-01372-6
PID-based attitude control of quadrotor using robust pole assignment
and LPV modeling
Mohammad Hossein Kazemi1
· Reza Tarighi2
Received: 5 May 2023 / Revised: 13 December 2023 / Accepted: 19 December 2023 / Published online: 25 January 2024
© The Author(s), under exclusive licence to Springer-Verlag GmbH Germany, part of Springer Nature 2024
Abstract
A novel control strategy is addressed in this paper for tracking control of a Quadrotor attitude based on PID structure. The
nonlinear model of quadrotor including gyroscopic effects is considered for a Polytopic Linear Parameter Varying (LPV)
modeling. Speciﬁcally, the control scheme adopted combines three techniques. On the one hand, the convex LPV controller
using the nonlinearity approach has the advantage of precisely describing the system’s nonlinear behavior by interpolating
local linear models, and one can extrapolate linear controller designs to the nonlinear case considering a more realistic scenario.
The principle component analysis (PCA)-based parameter set mapping is used for creating a low dimensional Polytopic LPV
model. Augmenting the proposed PID-based control action states to the plant states results in an overall plant in the form of
standard robust state feedback control problem where a robust pole assignment controller is designed. An H∞attenuation
level for the tracking error under external disturbances such as wind effects is guaranteed by solving the introduced linear
matrix inequalities (LMIs) to compute the control gains. Simulating the planned controller to a proposed quadrotor shows the
effectiveness of the proposed strategy in attitude control problem against the external disturbances.
Keywords LMI · Polytopic LPV modeling · Quadrotor dynamics · Robust control
1 Introduction
Although, small Quadrotors, are not being more inefﬁcient
from an energetic point of view compared with other aerial
vehicles such as conventional helicopter, they have a simpler
design, hover capability in a ﬁxed point, perpendicular take-
off and landing, and high dexterity and maneuverability.
However, in return for these advantages, they are difﬁ-
cult to control. Because they have fast dynamics and are
exposed to severe aerodynamic effects. In addition, the hard
restrictions imposed by the propellers, along with various
atmospheric disturbances, make more challenging control
problem.
B Mohammad Hossein Kazemi
kazemi@shahed.ac.ir
Reza Tarighi
Tarighi_r@proton.mail.com; s_r_tarighi@azad.ac.ir
1
Electrical Engineering Department, Shahed University,
Persian Gulf Hwy, Tehran 33191-18651, Iran
2
Department of Control Engineering, Faculty of Electrical
Engineering, South Tehran Branch, Islamic Azad University,
Tehran, Iran
Many samples of quadratic applications can be seen in the
real world such as high risk places disasters, and rescue [1–3]
agriculture [4, 5], facilities inspection [6], trafﬁc surveillance
[7] or photogrammetry and mapping [8]. So far, a lot of
work has been done in the ﬁeld of quadrotor control. They
have introduced the control design and development with dif-
ferent types of controllers, such as multi-agent system and
formation control [9–12], linear quadratic regulator [13–15],
feedback linearization, model predictive, sliding mode con-
trol [16, 17], backstepping control approach, [18–20], (LPV)
strategies [21], as well as learning approaches like [22], or
MPC-based deep learning [23].
In [9], cooperative formation control of Quadrotors with
obstacle avoidance and self-collisions based on a hierarchi-
cal MPC approach have been presented. In [10], adaptive
leader follower control for multiple Quadrotors via multiple
surfaces control is provided. Based on the different surface
and settled undirected communication topology, the versatile
pioneer adherent control for numerous quadrotors is talked
about. Cooperative control of numerous UAVs for timber-
land ﬁre observing and location is presented in [11]. In [12],
a study on the arrangement control of numerous Quadrotors
has been introduced. This reference points out the challenges
123

## Page 2

2386
M. H. Kazemi, R. Tarighi
and the propensity of investigate in the ﬁeld of different
quadrotors control.
Quadrotor is a six-degree-of-freedom (DOF) systems with
three degrees of transitional freedom of movement and three
degrees of angular freedom, while having only four control
actions consisting of an entire lifting force and three torques
created by variating the speeds of the motors. Generally, the
control of a quadrotor can be divided in two control prob-
lems: position control as an outer loop and attitude control as
an inner loop with faster dynamics. The inner attitude control
looptracksthecommandedrollandpitchanglescomingfrom
the outer position control loop, plus an externally enforced
yaw angle, by the above mentioned three torques[24–28],
In [24], a robust cascade controller counting a demeanor
controller and a position controller is proposed based on
the progressive control conspire and the vigorous compen-
sating method. The model show is depicted as a MIMO,
a time-varying framework subject to parametric irritations,
nonlinear and coupled elements, outside unsettling inﬂu-
ences, and state and input delays. In [25], the utilization of
a LPV representation of the demeanor subsystem permits to
consider it as free of position one, permitting the utilization of
acascadecontrolstructure,andalsofortheinternaldemeanor
control circle, the proposed qLPV–LQR controller, and pro-
portional integral observer are unraveled in an ideal way by
fathoming a set of LMIs. A super turning sliding mode con-
troller is outlined for a Quadrotor by using a cascaded internal
external circle structure in [26]. The controller is tried against
wind turbulence conditions and displaying vulnerabilities. It
is compared with a commonly used LQR-PD controller and
a nonlinear criticism linearization-based controller. In [27],
the robust adaptive control scheme based on back-stepping
technique is presented that improves the trajectory tracking
performance of the Quadrotor. A new NLPID controller for
stabilizing and controlling a 6-DOF UAV system is proposed
in [28].
Therefore, the attitude control is of great importance that
has attracted more focus in the literature, Since the atti-
tude maneuvers are highly sensitive to external disturbances
[29, 30], considering the problem of external disturbances
attenuation during attitude control design is an essential
purpose [31]. In [32], the problem of attitude control is
examined by presenting a fuzzy adaptive sigmoid general-
ized super-twisting extended state observer to estimate and
to compensate the disturbance with different upper bounds
of the ﬁrst derivative. The sliding mode controller can also
be used as an alternative method for disturbances rejec-
tion [26]. Some researchers have proposed the disturbance
observer-based control techniques for quadrotor attitude
toward external disturbances [30].
Polytopic linear parameter varying (LPV) modeling with
a not stationary behavior [33] can be a convenient operative
way to deal with nonlinear systems, even systems whose non-
linearities are state-dependent, such as quadrotors. A review
on different outlines of the LPV control synthesis practices is
accessible in [34]. In [35], polytopic attitude control using a
nonlinear model of an unmanned helicopter is introduced and
presented. The basis of linearization scheduling, formed by
applying Jacobian of the system equations around the oper-
ating points, can be used to obtain the polytopic model of
a nonlinear system [36]. Quadratic Lyapunov functions that
are afﬁne in the parameter proposed in [37] to verify robust
stability, robust convergence rates, and robust performance
of the LPV systems in terms of LMI feasibility tests.
In [38], a state-feedback proportional–integral control is
offered for LPV systems which is implemented to control
of longitudinal and lateral dynamics of an aircraft and also
in [39], trajectory tracking with state-feedback for rotor-
craft with LPV is presented. Afﬁne LPV systems under
Polytopic model uncertainty are considered in [40], where
the structure of the controller is centralized/decentralized
ﬁxed order output feedback. The proposed controller is a
gain-scheduled PID designed in the form of bilinear matrix
inequality (BMI). In [41], a scheduled PID is designed with a
hybrid synthesis including LMI techniques and evolutionary
search approaches applied to an afﬁne LPV model of a spark-
ignition engine. In [42] a gain-scheduled PID controller with
Smith predictor is introduced to control the open-ﬂow chan-
nel by means of LPV modeling. It is expressed as a convex
state-feedback problem that involves an LMI-based pole
placement problem. The proposed H∞control in [43] deals
with longitudinal and lateral directions. Although its capa-
bility cannot be denied, there is no enlightenment on how
external disturbances affect as well as simultaneous interac-
tion in the longitudinal and transverse directions. The attitude
control is studied in [44] using robust LPV for a Quad-
copter considering state constraints and input saturation. The
scheduling parameters, which consists of some states and the
control inputs, must vary in a speciﬁed polyhedron. However,
since the speeds of propellers are considered as a number of
scheduling signal, a heavy computational load and complex
calculation are some of the most important restrictions of the
usage of the proposed method. Introduced quasi-LPV mod-
eling in [45], is examined based on changes in Quadrotor
mass, rotor speed and the moments of inertia. The proposed
attitude controller consists of two LPV-H∞controllers. The
ﬁrst is to control the roll and pitch angles, and the second
is to control the yaw angle. In [46], modeling and control
design is investigated using output feedback and considering
the motor dynamics. It introduces a simple LPV modeling
that includes only two varying parameters.
In [47], modeling and identiﬁcation of the nonlinear twin
rotor system have been performed applying quasi-LPV con-
cepts. The system is approximated to a Polytopic model
for designing a pole placement controller in the form of
123

## Page 3

PID-based attitude control of quadrotor using robust pole …
2387
state feedback. The main drawback is the high volume of
computations due to the large number of parameters that
increase the LMIs, although the paper uses only the max-
imum and minimum values of the parameters variations are
used to determine the Polytopic vertices. ANA robust Poly-
topic state-feedback is proposed in [24] for the control of
quadrotor, which counteracts the adverse effects of mass
deviations and battery voltage variants. It has only four ver-
tices and does not include other system parameter variations.
In this article, the issue of quadrotor attitude control
has been investigated based on a novel technique using
reduced Polytopic LPV modeling and a hybrid PID control
action in the form of state-feedback. The control objective
includes both H∞disturbance attenuation and LMI region
pole assignment. Although, the proposed controller has a PID
structure, its structure is not decentralized form. This means
that for each quadrotor Euler angle, there is no separate PID
controller, but the controllers operate interactively. In fact, an
overall centralized PID controller is designed for whole of the
quadrotor angles. Its states are augmented to the plant states
and constructing a general linear fractional transformation
(LFT) representation. In this work a quasi-LPV modeling
is introduced to design a PID-based state-feedback control
revealing its main advantage, which is the capability of over-
comingthenonlinearityeffectsofthesystem.Thegyroscopic
term is embedded as a varying parameter alongside other
variable parameters such as Euler angles, angular velocities,
mass and moments of inertia. A set of gridding points is cre-
ated by considering the minimum, maximum, and middle
values of each variable parameter to generate sample linear
plants for building an initial Polytopic model. In the next step,
due to the high number of vertices in the initial built Poly-
topic model, a parameter set mapping with the basis of PCA
algorithm [48], is used to obtain a reduced Polytopic model
by neglecting the less signiﬁcant directions in the parame-
ter space. When the parametric space dimension is large and
the computational complexity may be occurred, this strategy
can be actually valuable [49]. The obtained reduced Poly-
topic model, with the lowest number of vertices, is used for
designing the proposed controller. The control objective is
to assign the poles of the closed loop system at each vertex
inside a prescribed LMI region such that an H∞attenuation
level is guaranteed for the closed loop system under input
disturbances. The control gains are speciﬁed by solving the
related LMIs constraints. The proposed control simulation is
performed on nonlinear model of a quadrotor that is expected
to conﬁrm the effectiveness of the proposed method.
The main contribution of this paper is summarized to
address a control design that combines three techniques to
obtain a convex LPV controller for a quadrotor consider-
ing the gyroscopic effect: introducing sufﬁcient conditions
in the form of LMIs, whose solutions guarantee the control
objectives; the PCA-based parameter set mapping is used
for creating a low dimensional Polytopic LPV model; an H∞
attenuation level of external disturbances beside a robust pole
placement are considered in a PID-based controller.
The paper sections are prepared as follows. Following
sections, some preliminaries on LPV systems, introducing
of the Quadrotor dynamics, Quasi-LPV representation and
Polytopic modeling with PCA algorithm, control design pro-
cedure, numerical simulation and comparison with nonlinear
PID (NLPID) are discussed. Finally, the article ends with a
conclusion in the last section.
2 Preliminaries
Consider a standard closed loop control structure with fol-
lowing state space equations.
˙x  A(μ)x + B1(μ)w + B2(μ)u
(1)
z∞ C(μ)x + D1(μ)w + D2(μ)u
(2)
where x ∈Rn is the state vector, w ∈Rnw is the exogenous
input, u ∈Rnu is the control input, and z∞∈Rnz is the
control objective. The varying parameter μ ∈Rns is assumed
to be in a compact set. It is assumed that all the matrices
have appropriate dimensions and they are constrained to the
following polytope.
P  {(A, B1, B2, C, D1, D2)(μ) |
(A, B1, B2, C, D1, D2)(μ)

N

i1
αi(Ai, B1i, B2i, Ci, D1i, D2i),
N

i1
αi  1,
αi ≥0, i  1, 2, ..., N }
(3)
In other words, the system matrices depend on the time-
varying vector μ(t)  [ μ1(t) ... μN(t)]T .The vertices of
the polytope P, referred as (Ai, B1i, B2i, Ci, D1i, D2i) for
i  1, 2, ..., N.The H∞performanceachievementisdeﬁned
to synthesis a control signal for (1) that provides the smallest
attenuation level γ > 0 such that for any external input w ∈
L2, it is veriﬁed that z∞∈L2, and:
∥z∞∥2 < γ ∥w∥2
(4)
The following lemma gives the sufﬁcient condition of
existence a state-feedback gain matrix K for stabilizing the
closed loop system assuring the attenuation level γ .
Lemma1 [50–52]Ifthereexistasymmetricpositivedeﬁnite
matrix X and a matrix Y with appropriate dimensions such
that the following LMIs are satisﬁed,
123

## Page 4

2388
M. H. Kazemi, R. Tarighi
Fig. 1 Quadrotor and its reference frames
⎡
⎢⎣
Ai X + X AT
i + B2iY + Y T BT
2i
∗
∗
BT
1i
−I
∗
Ci X + D2iY
D1i −γ 2I
⎤
⎥⎦< 0,
i  1, 2, ..., N
(5)
where symbol ∗indicates symmetric blocks in the LMIs,
then the state feedback control gain K  Y X−1 quadrati-
cally stabilizes the uncertain system (1), (2) with disturbance
attenuation γ .
3 Quadrotor dynamics
Mathematical modeling of quadrotor UAV using Newton
Euler approach has been explained in many researches [25,
53]. Quadrotors as an air vehicle have four propellers, two
rotating clockwise and the other two rotating counterclock-
wise. The movement of the quadrotor is due to the rotational
motion of the propellers, such that by increasing or decreas-
ing four propellers speeds all together, a vertical motion
occurs while differing the speed of opposite propellers causes
a roll or pitch motion. The yaw motion is also caused by
torque imbalance between each pair of propellers. Suppose
that for the quadrotor shown in Fig. 1, [φ, θ, ψ]T , [x, y,
z]T , [u, v, w]T , and [p, q, r]T denote the Euler angles, the
position in earth frame, linear velocity, and angular velocity
in body frame, respectively. Assuming the rigidity and sym-
metricity of the body as well as nearing to hover attitude, the
quadrotor dynamic model in earth frame and with consider-
ing wind torque vector τw  [τwx, τwy, τwz]T is described
by the following equations [54, 55].
Table 1 Quadrotor parameters
Symbol
Description
Value
Ix
Moment of inertia along
x-axis
3.4 × 10−3 N m s2
Iy
Moment of inertia along
y-axis
3.4 × 10−3 N m s2
Iz
Moment of inertia along z-axis
6 × 10−3 N m s2
m
The quadrotor mass
0.698 kg
g
Gravitational Acceleration
9.81 m s−2
JT P
Total rotational moment of
inertia along propeller axis
1.3 × 10−6 N m s2
ℓ
Central distance between the
quadrotor gravity and each
motor
0.171 m
cT
Thrust factor
7.62 × 10−8
N
rpm2
cQ
Drag factor
2.68 × 10−9
N
rpm2
Ω min
Minimum propellers speeds
1075 rpm
Ω max
Maximum propellers speeds
8600 rpm
¨x  (cos φ sin θ cos ψ + sin φ sin ψ)U1
m
¨y  (cos φ sin θ sin ψ −sin φ cos ψ)U1
m
¨z  −g + (cos φ cos θ)U1
m
¨φ  ˙θ ˙ψ Iy −Iz
Ix
−JT P
Ix
˙θ Ω r + U2 + τwx
Ix
¨θ  ˙φ ˙ψ Iz −Ix
Iy
+ JT P
Iy
˙φ Ω r + U3 + τwy
Iy
¨ψ  ˙φ ˙θ Ix −Iy
Iz
+ U4 + τwz
Iz
(6)
The control inputs, trust force U1 and three roll, pitch and
yaw torques (U2, U3, U4) are related to the rotors speed
(Ω i, i  1, 2, 3, 4), as follows:
U1  cT (Ω 2
1 + Ω 2
2 + Ω 2
3 + Ω 2
4)
U2  cT .ℓ(−Ω 2
2 + Ω 2
4)
U3  cT .ℓ(−Ω 2
1 + Ω 2
3)
U4  cQ(−Ω 2
1 + Ω 2
2− 2
3 + Ω 2
4)
(7)
All the parameters in the equations as well as the values
considered for them are presented in Table 1, as well as, the
cascaded controller architecture is presented in Fig. 2. The
parameter values for performing the simulations are taken
123

## Page 5

PID-based attitude control of quadrotor using robust pole …
2389
Fig. 2 Cascaded controller architecture
from [25]. The term Ω r which appears in the gyroscopic
effect, is due to an imbalance in the total algebraic sum of
the propellers speeds.
Ω r  −Ω 1 + Ω 2 −Ω 3 + Ω 4
(8)
In the control of robotic systems such as Quadrotor, which
have complex dynamics, we usually ignore the dynamics of
the motors against the dynamics of the robot. The reason is
that we work in a higher level control layer whose purpose
is to specify the torque required to satisfy the control objec-
tives. The lower control layer is responsible for providing
this torque. If it is assumed that this control layer performs
its task correctly, i.e., the motors are equipped with high-
speed torque control hardware compared to the dynamics
of the robot; and then, the dynamics of the motors can be
omitted.
3.1 Quasi-LPV representation and Polytopic
modeling
In this work, the attitude control of quadrotor has been stud-
ied by adjusting the Euler angles according to the desired
reference inputs. The attitude subsystem includes the last
three equations of (6), which means the dynamical equations
of Euler angles with three inputs U2, U3, and U4. Since the
parameter varying are state-depended, we are faced with a
quasi-LPV modeling. This allows us to embed the quadrotor
nonlinearities into the varying parameters and therefore not
only the nonlinearities are disappeared, but also get rid of the
gyroscopic effect. The scheduling signals ρi are related to
the varying parameters of the system according to Table 2.
Their variation ranges are also presented in this table.
Thus, deﬁning xa1 : [φ, θ, ψ]T and xa2 : [ ˙φ, ˙θ, ˙ψ]T
the state space representation of the attitude subsystem can
Table 2 Scheduling signals
ρ
Symbol Variation Range
ρ1
Ix
±10%
ρ2
Iy
±10%
ρ3
Iz
±10%
ρ4
JT P
±10%
ρ5
˙φ
[ −2 +2 ] rad s−1
ρ6
˙θ
[ −2 +2 ] rad s−1
ρ7
Ω
[ −100 +100 ] rad s−1
be expressed in a quasi-LPV form as follows:
˙xa1  xa2
˙xa2 
⎡
⎢⎣
0 μ1 μ2
μ3 0 μ4
μ5 μ6 0
⎤
⎥⎦xa1 +
⎡
⎢⎣
μ7 0
0
0 μ8 0
0
0 μ9
⎤
⎥⎦
⎡
⎢⎣
U2 + τwx
U3 + τwy
U4 + τwz
⎤
⎥⎦
(9)
whereμi’s are the varying parameters with the respect of
scheduling signals as follows:
μ1  −ρ4
ρ1 ρ6
μ6  ρ1−ρ2
2ρ3 ρ5
μ2  ρ2−ρ3
ρ1
ρ6 μ7  1
ρ1
μ3  ρ4
ρ2 ρ7
μ8  1
ρ2
μ4  ρ3−ρ1
ρ2
ρ5 μ9  1
ρ3
μ5  ρ1−ρ2
2ρ3 ρ6
(10)
By considering the xa : [xT
a1, xT
a2]T as the attitude state
vector, the quasi-LPV can be summarized to:
˙xa  Aa(μ)xa + Ba(μ)τw + Ba(μ)ua
(11)
where ua  [U2, U3, U4]T is the input vector, μ  [μ1,
..., μ9]T is the varying parameter vector, and the matrices
Aa(μ) and Ba(μ) are as follows:
Aa(μ) 
	
03×3
I3
03×3 Aa22(μ)

, Ba(μ) 
	
03×3
Ba2(μ)

(12)
and,
Aa22(μ) 
⎡
⎢⎣
0 μ1 μ2
μ3 0 μ4
μ5 μ6 0
⎤
⎥⎦, Ba2(μ) 
⎡
⎢⎣
μ7 0
0
0 μ8 0
0
0 μ9
⎤
⎥⎦
(13)
In order to construct a Polytopic model, we consider only
three values for each scheduling signal: minimum, middle,
123

## Page 6

2390
M. H. Kazemi, R. Tarighi
and maximum of its interval range. In this way, N  3ρ ver-
tices are produced, where ρ  7 is the number of scheduling
signals, and the vertices are noted by:
(Aai, Bai) :
	
03×3
I3
03×3 Aa22i

,
	
03×3
Ba2i


(14)
while we have 9 parameters, and 2μ vertices, where μ  9
is the number of varying parameters, are needed to make a
Polytopic model for the system. In any case, the high num-
ber of vertices requires a high computational volume, and
therefore, in the next section we will reduce the number of
vertices using the PCA-based parameter set mapping tech-
nique. However, the attitude subsystem will be constrained
to the following initial polytope.
Pa  {(Aa, Ba)(μ) | (Aa, Ba)(μ)

N

i1
αi(Aai, Bai) ,
N

i1
αi  1}
(15)
The vertices of the polytope Pa, referred as (Aai, Bai)
for i  1, 2, ..., N. The matrices, are continuous functions,
in terms of parameter vector μ(t) ∈ℜμ, depends on the
scheduling signal ρ(t) ∈ℜρ according to μ(t)  h(ρ(t))
where h : ℜρ →ℜμ is a continuous parameter mapping as
(10).
3.2 PCA Algorithm for LPV Models
In this section, parameter set mapping based on PCA algo-
rithm is used to ﬁnd tighter regions in the space of the
scheduling parameters. By neglecting insigniﬁcant direc-
tions in the mapped parameter space, approximations of LPV
models are achieved which will lead to a less conservative
controller synthesis.
The number of gridding points, N, is chosen sufﬁciently
large concern to system operating range, nonlinearity effects,
and system parameters dimension such that all dynamic
behavior of the quadrotor is captured. On the other hand,
increasing N, causes high complexity in controller com-
putations. To ﬁnd a tighter region in the parameter space,
parameter set mapping on the basis of PCA algorithm is
implemented. The Polytopic LPV model (15) is simpliﬁed to
aspacewithlowerdimensionbyignoringtheslightdirections
in the mapped parameter space. The procedure is explained
in the following accordance with the procedure described in
[48]. For the LPV model (11) and scheduling signal ρ(t),
the mapping η(t)  r(ρ(t)), r : ℜρ →ℜη where η < μ,
should be found such that
˙xa  ˆAa(η)xa + ˆBa(η)ua + ˆBa(η)τw
(16)
Approximates the model (11). The basic details of PCA
can be studied in [56]. The parameters of the Polytopic LPV
model (15) for i  1, 2, . . . , N are gathered to construct a
μ× N data matrix   [μ1, μ2, . . . , μN], where μi is the
varying parameter vector evaluated at i–th vertex. Normal-
izing its rows with zero mean and unit standard deviation to
constructing the normalized data matrix n  (). Next,
performing the following singular value decomposition
n 

ˆU U
	
ˆ 0
0 

	
ˆV T
V T

(17)
and, separating the η signiﬁcant singular values correspond-
ing to ˆU, ˆ, and ˆV . Ignoring the lower singular values leads
to ˆn  ˆU ˆ ˆV T ≈n where ˆn is approximation of the
normalized given data n. The matrix ˆU is used as a basis of
the signiﬁcant column space to realize the reduced mapping
η(t)  r(ρ(t))  ˆU T (h(ρ(t)))  ˆU T (μ(t))
(18)
It means, the approximate mapping of ˆAa(·) and ˆBa(·) in
(16) are related to (11) by:
ˆPa(η) 

ˆAa(η(t)) ˆBa(η(t))



Aa( ˆμ(t)) Ba( ˆμ(t))

(19)
where
ˆμ(t)  −1( ˆUφ(t))  −1( ˆU ˆU T (μ(t)))
(20)
Note that −1 indicates the row-wise rescaling. Thus,
using ˆn to regenerate the new vertices ( ˆAai, ˆBai), the Poly-
topic LPV model (15) is reduced to:
ˆPa 

(Aa, Ba)( ˆμ) | (Aa, Ba)( ˆμ)

ˆN

i1
αi( ˆAai, ˆBai)
,
ˆN

i1
αi  1,
αi ≥0,
i  1, 2, ..., ˆN }
(21)
where
ˆN
 2η is the number of vertices and
ˆPai

Pa( ˆμvi) : ( ˆAai, ˆBai) is the i-th new vertex model such
that:
( ˆAai, ˆBai) :
	
03×3
I3
03×3 ˆAa22i

,
	
03×3
ˆBa2i


(22)
The following fraction of the total variation vη[48], can
be introduced as a criterion for measuring the quality of the
123

## Page 7

PID-based attitude control of quadrotor using robust pole …
2391
Fig. 3 Fraction of total variation vη versus η
approximated Polytopic model (21) relative to actual Poly-
topic model (15) by the singular values in (17).
vη 
η
i1
σ 2
i
μ
i1
σ 2
i
(23)
It should be noted that the fraction of the total variation
is used as a criterion for measuring the approximation qual-
ity, obviously a lower approximation may compromise the
feasibility.
For selecting the appropriate value of η, the relation (23) is
depicted in Fig. 3 for different values of η. Then the suitable
η is chosen in terms of desired acceptable percent of the error
in captured information. Here, choosing η  6, about 78% of
the information is captured and the reduced Polytopic LPV
model (21) will have only ˆN  26  64 vertices.
3.3 Control strategy
The main purpose of the attitude control system is for the
Euler angles xa1 to track the input reference x1r : [φr,
θr, ψr]T , so that the tracking error e1 : x1r −xa1, for
the reduced Polytopic LPV model (21), converges to zero,
asymptotically. Our proposed strategy is adapted from the
structure of a typical PID controller, where
ua  K Pe1 + K D ˙e1 + KI
t
0
e1(σ)dσ
(24)
Deﬁning error vector e : [eT
1 , eT
2 , eT
3 ]T with e2 : ˙e1
and e3 :
 t
0 e1(σ) dσ, and also z∞: α1e1 + α2e2 + α3e3
Fig. 4 Proposed control structure
where αi’s are designing parameters, as an objective signal
for H∞performance improvement, the state equation of the
error system are as follows:
˙e1  e2  ˙x1r −˙xa1  ˙x1r −xa2
˙e2  ¨e1  ¨x1r −˙xa2−
 ¨x1r −Aa22( ˆμ)xa2 −Ba2( ˆμ)(ua + τw)
 Aa22( ˆμ)e2 −Ba2( ˆμ)(ua + τw)
+¨x1r −Aa22( ˆμ)˙x1r
˙e3  e1
(25)
The above error sate equations can be rewrite in the fol-
lowing compact form:
˙e  Ae( ˆμ)e + Be1( ˆμ)dw + Be2( ˆμ)ua
z∞ Cae
(26)
where dw as follows is the total perturbation vector due to
wind torque and differential deviations of the reference input,
and:
Ae( ˆμ) 
⎡
⎢⎣
0
I
0
0 Aa22( ˆμ) 0
I
0
0
⎤
⎥⎦, Be1( ˆμ) 
⎡
⎢⎣
0
0
I −Ba2( ˆμ)
0
0
⎤
⎥⎦,
Be2( ˆμ) 

0 −BT
a2( ˆμ) 0
T
,
Ca 

α1I α2I α3I

, dw 
	
¨x1r −Aa22( ˆμ)˙x1r
τw

(27)
Now, it can be seen that control law (24) is equivalent to a
full state-feedback control law u p  Ke for (26), where K 
[K P, K D, KI]. The control structure is shown in Fig. 4. The
123

## Page 8

2392
M. H. Kazemi, R. Tarighi
Euler angles as Quadrotor’s attitude and their derivatives are
measured and compared with references; and then, the error
signals and the integral of the attitude error are multiplied by
the control gain K to obtain control actions.
The control action signals should ﬁrst be converted to
the motors speed commands by inverse of (7) (shown with
F−1(U)) and after applying the motors speed limits and
ignoring the motors dynamics, the actual angular torques
and the gyroscopic effect are computed by (7) (shown with
F(Ω)) and (8) respectively, and then applied to the Quadro-
tor dynamics. Note that since the trust force U1 is effective
in speed calculations, we have to use a conventional altitude
controller to keep the Quadrotor at an almost constant height.
We used a simple PID controller for this purpose.
Thestate-feedbackgainmatrix K forstabilizingtheclosed
loop system assuring the H∞attenuation level γ is computed
by solving the LMIs that are introduced in the following
theorem.
Theorem 1 If there exist a symmetric positive deﬁnite
matrix X and a matrix Y with appropriate dimensions such
that the following LMIs are satisﬁed,
⎡
⎢⎣
Qai
∗
∗
ˆBT
a1i
−I
∗
Ca X D1 −γ 2I
⎤
⎥⎦< 0, i  1, 2, ..., ˆN
(28)
where
Qi :
⎡
⎢⎣
0
I
0
0 ˆAa22i 0
I
0
0
⎤
⎥⎦X + X
⎡
⎢⎣
0
I
0
0 ˆAa22i 0
I
0
0
⎤
⎥⎦
T
+
⎡
⎢⎣
0
−ˆBa2i
0
⎤
⎥⎦Y + Y T
⎡
⎢⎣
0
−ˆBa2i
0
⎤
⎥⎦
T
(29)
and,
ˆBa1i :
⎡
⎢⎣
0
0
I −ˆBa2i
0
0
⎤
⎥⎦, D1 

0 0

(30)
Supposethat all matrices havetheappropriatedimensions.
Then, the control law (24) with control gain K  Y X−1
quadratically stabilizes the uncertain system error system
(26) with disturbance attenuation γ .
Proof the proof is straightforward by applying the Lemma
1 to the uncertain error system (26). If the following substi-
tution is made in Eqs. (1) and (2):
A(μ)  Ae( ˆμ),
B1(μ)  Be1( ˆμ)
B2(μ)  Be2( ˆμ),
C(μ)  Ca,
Then the LMI (5) is converted to the LMI (28) and the
theorem is proved.
□
To improve the performance of the controller, a pole place-
ment objective is added to the previous controller. Therefore,
the LMI region D, a ’conic sector’ of the complex plane with
inner angle about 139°, it means and apex at the ( −2β,
0), is considered for assigning the poles of the closed loop
Polytopic LPV model. The LMI region D is described by:
D  {z ∈C :
fD(z) < 0}
fD(z)  L + zM + zMT
(31)
where matrices L and M are:
L 
	
β 0
0 β

, M 
	
sin(δ)
cos(δ)
−cos(δ) sin(δ)

(32)
If there exist a symmetric positive deﬁnite matrix X and
a matrix Y such that the following LMIs are satisﬁed
	
βX + sin δ(Vi + V T
i )
cos δ(Vi −V T
i )
cos δ(V T
i
−Vi)
βX + sin δ(Vi + V T
i )

< 0
(33)
where
Vi :
⎡
⎢⎣
0
I
0
0 ˆAa22i 0
I
0
0
⎤
⎥⎦X +
⎡
⎢⎣
0
−ˆBa2i
0
⎤
⎥⎦Y,
(34)
for i  1, ..., ˆN,
Then, the control law (24) with control gain K  Y X−1
quadratically D-stabilizes the uncertain error system (26) for
the desired LMI region (31) [57].
As a result, computing the LMI conditions (28) and (33)
for the same variables X and Y result in the control gain K 
Y X−1 with the quadratic H∞performance with disturbance
attenuation γ that assign the closed loop poles in D.
4 Numerical simulation
This section describes the performance of the proposed con-
trol scheme applied to the quadrotor dynamics (6) to examine
against the nonlinearity effects, gyroscopic effect, exogenous
disturbances and parameter perturbations.
123

## Page 9

PID-based attitude control of quadrotor using robust pole …
2393
0
5
10
15
20
Time (s)
-0.1
0
0.1
0.2
0.3
0.4
Euler Angles (rad)
r
r
r
Fig. 5 Attitude system outputs by H∞control with attenuation level
γ  1
Before the controller design stage, LPV modeling of
the system has been done. For LPV modeling, the process
described in Sect. (1–3) has been carried out and the ini-
tial Polytopic model (15) has been extracted. Then the PCA
technique is programmed according to Sect. (2–3) and a
reduced Polytopic model with 64 vertices is obtained. Then,
by solving LMIs (28) and (33), the gains of the controller are
obtained, and at the end, the system is simulated in the MAT-
LAB/Simulink environment according to the block diagram
in Fig. 4.
First, we consider three reference signals as pulses with
different amplitudes values and different pulse durations, as
the set points for Euler angles. Then implementing the pro-
posed H∞control with disturbance attenuation γ , to the
attitude system, the responses are shown in Fig. 5. It is
observed that the responses have an appropriate damping
coefﬁcient, an acceptable percent of overshoot, and no steady
state error.
Now implementing the wind effect to the proposed atti-
tude controller. It is considered that wind disturbance torques
about 1 Nm are arisen on the roll, pitch, and yaw axes at
times t  6 s, t  7 s, and t  5 s for 5, 3, and 7 s durations,
respectively. Figure 6 shows the attitude angles. An excel-
lent disturbance attenuation can be seen in this ﬁgure for the
proposed H∞control with disturbance attenuation γ .
It is clear that the lower the attenuation level γ , the greater
the disturbance attenuation. This can be well seen in Fig. 7,
which plots the roll angle for different values of γ . Note that
due to the clearer appearance and also similarity in behavior
of all the three Euler angles, only the roll angle is drawn in
this ﬁgure and subsequent ﬁgures.
As mentioned in the controller design section, we try to
improve the controller performance by adding a pole assign-
ment objective to the last controller. An LMI region D in the
form of a ’conic sector’ of the complex plane with inner angle
0
5
10
15
20
Time (s)
-0.1
0
0.1
0.2
0.3
0.4
Euler Angles (rad)
r
r
r
Fig. 6 Attitude system outputs by H∞control with attenuation level
γ  1 against the wind disturbances
0
5
10
15
20
Time (s)
-0.1
0
0.1
0.2
0.3
0.4
Roll Angle
(rad)
r
=1
=5
=10
Fig. 7 Attitude roll angle by H∞control for different values for atten-
uation level γ against the wind disturbances
about 139°, it means damping ratio about 0.35, and apex at
the ( −2β, 0), is considered for assigning the poles of the
closed loop Polytopic LPV model. Figure 8 shows the roll
angle response against the wind disturbances for different
values for γ and β. As can be seen in this ﬁgure, for opti-
mal values γ ∗ 0.8 and β∗ 12, wind turbulence has not
been able to affect the roll angle and deﬂect it. It should be
noted that there is also a similar behavior for pitch and yaw
angles, which has been avoided due to the increasing number
of ﬁgures.
The control effort (angular torques) and the required
speeds of the motors to produce this effort are shown in
Figs. 9 and 10, respectively. It can be seen that the speeds
of the motors belong to the predeﬁned range speciﬁed in
Table 1.
123

## Page 10

2394
M. H. Kazemi, R. Tarighi
0
5
10
15
20
Time (s)
-0.1
0
0.1
0.2
0.3
0.4
Roll Angle
(rad)
=0, =1
=4, =1
=8, =1
=12, =1
*=12, *=0.8
Fig. 8 Attitude roll angle by H∞control and pole placement for differ-
ent values for γ and β against the wind disturbances
0
5
10
15
20
Time (s)
-1
-0.5
0
0.5
1
Quadrotor Torques (Nm)
U2
U3
U4
Fig. 9 Angular torques (control effort) applied to the quadrotor
0
5
10
15
20
Time (s)
0
2000
4000
6000
8000
10000
Motors Speeds (rpm)
1
2
3
4
Fig. 10 Speeds of the motors
0
2
4
6
8
10
12
14
16
18
20
Time (s)
-0.1
-0.05
0
0.05
0.1
0.15
0.2
0.25
0.3
0.35
0.4
Euler Angles (rad)
(proposed)
(NLPID)
(proposed)
(NLPID)
(proposed)
(NLPID)
Ref
GA Method
GA Method
GA Method
Fig. 11 Comparison of the proposed controller response with NLPID
and GA response
0
5
10
15
20
Time (s)
-1.5
-1
-0.5
0
0.5
1
Euler Angles (rad)
(proposed)
(NLPID)
(proposed)
(NLPID)
(proposed)
(NLPID)
Ref
6
6.2
6.4
6.6
0.31
0.315
0.32
0.325
Fig. 12 Comparison of the proposed controller response with NLPID
response in the presence of wind disturbances
The proposed method in [28] is considered to compare
the capabilities of the proposed controller. In [28], nonlin-
ear PID (NLPID) controllers are designed for roll, pitch,
and yaw angles of a Quadrotor, where their parameters are
tuned using Genetic Algorithm (GA) to minimize a multi-
objective output performance index. To demonstrate how
works parameters are tuned using (GA) is shown in Fig. 11.
TheDifferenttypestuningofAlgorithmsselectedparameters
and Optimization methods are presented in [58–60].Fig. 11
compares our optimal case (γ ∗ 0.8 and β∗ 12) response
with NLPID and GA response. The very appropriate behav-
ior of the proposed method toward NLPID can be easily seen
in this ﬁgure. This performance is more highlighted in the
presence of wind disturbances. For this reason, the effect of
wind turbulence about 0.6 Nm on both controllers is shown
in Fig. 12. It is observed that the wind disturbance was able
to severely impair the NLPID response, while not having a
signiﬁcant effect on the proposed controller response.
123

## Page 11

PID-based attitude control of quadrotor using robust pole …
2395
5 Conclusion
In this paper, a method was proposed for Quadrotor attitude
tracking control based on the structure of a typical PID con-
troller, in the form of state feedback, using the H∞control
theory in order to deal with external disturbances, which are
mainly of the wind type and gyroscopic effects. By intro-
ducing suitable scheduling signals, a quasi-LPV modeling
was introduced to cover the nonlinear effects of Quadrotor
dynamics as well as its gyroscopic effects.
Gridding the scheduling signals in their variation ranges,
an initial high-dimensional Polytopic model is obtained. Due
to the high number of vertices of the initial Polytopic model,
the parameter set mapping is implemented based on the PCA
algorithm to achieve a tighter region in the parameter space.
The proposed control is derived from a typical PID controller
in the form of a state feedback control, except that it has a
centralized structure and not a decentralized one. Therefore,
it is deﬁnitely superior to the traditional PID control that is
applied to each axis separately; while, it is easy to consider
extra control objectives, which here has been the disturbance
rejectionandpoleplacement.Theproposedcontrolhasasim-
ple structure and low consuming computation time because
it is in fact same PID with interactive in all axes. Although
the proposed control design may seem complicated and time-
consuming, because of the drawback related to the increase
in the LMIs and the increase in the computation volume, but
it should be said that in the proposed controller all the LMIs
are solved off-line and its computing time is not a problem in
the real time implementation. However, there has been exten-
sive research on the computational complexity of LMIs so far
[61, 62]. As future works, the following can be mentioned.
The proposed control strategy can be expanded on Quadrotor
maneuver control, where in addition to the attitude control,
the position control and also the tracking of a desired path is
the main problem. Another suggestion is to improve the pro-
posed control from a ﬁxed control and upgrade it to a variable
structure dependent on scheduling variables. In this way, the
conservatism of the proposed control will be signiﬁcantly
reduced.
Acknowledgements The authors consider it necessary to acknowledge
and thank the computer site of Shahed University for their cooperation
in providing the necessary hardware to prepare this article.
Author contributions The author contributions can be summarized to:
Considering the gyroscopic effects and other nonlinearities of the sys-
tem in the Polytopic modeling. Using PCA algorithm to reduce the size
of Polytopic model data. Providing the proposed control under the PID
structure for easier practical implementation.
Funding No funding was received to assist with the preparation of this
manuscript.
Data availability Data availability is not possible.
Code Availability Code Availability is not applicable.
Declarations
Conﬂict of interest The authors have no competing interests to declare
that are relevant to the content of this article.
References
1. Kumar P V, Challa A, (2015) GIS based Fire Rescue System for
Industries using Quad copter – A Novel Approach, In: International
Conference on Microwave, Optical and Communication Engi-
neering (ICMOCE), doi: https://doi.org/10.1109/ICMOCE.2015.
7489693.
2. Bashi OID, Hasan WZW, Azis N (2017) Quadcopter Sensing
System for Risky Area. IEEE Regional Symposium on Micro
and Nanoelectronics (RSM). https://doi.org/10.1109/RSM.2017.
8069152
3. Saha H, Basu S, Auddy S, Dey R, Nandy A, Pal D, (2018)A low
cost fully autonomous GPS ( Global Positioning System ) based
Quad copter for disaster management, In: IEEE 8th Annual Com-
puting and Communication Workshop and Conference (CCWC)
doi: https://doi.org/10.1109/CCWC.2018.8301782.
4. Navia J, Mondragon I, Patino D, Colorado J (2016) Multispectral
mapping in agriculture : terrain mosaic using an autonomous. Inter-
national Conference on Unmanned Aircraft Systems (ICUAS).
https://doi.org/10.1109/ICUAS.2016.7502606
5. Daroya R, Ramos M, (2017)NDVI Image Extraction of an Agri-
cultural Land Using an Autonomous Quadcopter with a Filter-
modiﬁed Camera. In: IEEE International Conference on Control
System, Computing and Engineering (ICCSCE), pp: 24–26.
6. Nikolic J, Leutenegger S, Burri M, Huerzeler C, Siegwart
R,(2013)A UAV System for Inspection of Industrial Facilities. In:
IEEE Aerospace Conference ,doi: https://doi.org/10.1109/AERO.
2013.6496959.
7. Chen Y M, Dong L, Oh J S,(2007) Real-time video relay for
UAV trafﬁc surveillance systems through available communica-
tionnetworks.In: IEEE WirelessCommunicationsandNetworking
Conference, (WCNC), pp. 2608–2612, doi: https://doi.org/10.
1109/WCNC.2007.485.
8. Nex F, Remondino F (2014) UAV for 3D mapping applications: A
review. Appl Geomatics 6(1):1–15
9. Eskandarpour A, Majd V J, (2014)Cooperative formation control
of quadrotors with obstacle avoidance and self collisions based on a
hierarchical MPC approach, In: 2nd RSI/ISM International Confer-
ence on Robotics and Mechatronics, (ICRoM 2014), pp:351–356.
10. Abbas R, Wu QH (2016) Adaptive leader follower control for
multiple quadrotors via multiple surfaces control. J Beijing Inst
Technol 25(4):526–532. https://doi.org/10.15918/j.jbit1004-0579.
201625.0411
11. Ghamry K A, Zhang Y, (2016)Cooperative control of multi-
ple UAVs for forest ﬁre monitoring and detection, In: 12th
IEEE/ASME International Conference on Mechatronic and
Embedded Systems and Applications (MESA) .
12. Hou Z, Wang W, Zhang G, Han C,(2017)A survey on the formation
control of multiple quadrotors, In: 14th International Conference
on Ubiquitous Robots and Ambient Intelligence, URAI 2017, pp:
219–225, doi: https://doi.org/10.1109/URAI.2017.7992717.
13. Bouabdallah S, Noth A, Siegwart R (2004) PID vs LQ control
techniques applied to an indoor micro Quadrotor. IEEE/RSJ Inter-
national Conference on Intelligent Robots and Systems (IROS)
3:2451–2456
123

## Page 12

2396
M. H. Kazemi, R. Tarighi
14. Hoffmann G M, Tomlin C J, (2007)Quadrotor Helicopter Flight
Dynamics and Control: Theory and Experiment, AIAA Guidance,
Navigation and Control Conference and Exhibit, August 2007,
pp:1–20.
15. Martins L, Cardeira C, Oliveira P (2019) Linear quadratic regu-
lator for trajectory tracking of a quadrotor. IFAC-PapersOnLine
52(12):176–181
16. Wang C, Chen Z, Sun M (2017) Sliding mode control of a
quadrotor helicopter. Zhongnan Daxue Xuebao (Ziran Kexue
Ban)/Journal of Central South University (Science and Technol-
ogy) 48(4):1006–1011. https://doi.org/10.11817/j.issn.1672-7207.
2017.04.021
17. Benallegue A, Mokhtari A, Fridman L, (2006) Feedback lineariza-
tion and high order sliding mode observer for a quadrotor UAV.
In: Proceedings of the 2006 International Workshop on Variable
Structure Systems,pp:365–372, doi: https://doi.org/10.1109/VSS.
2006.1644545
18. Tripathi VK, Behera L, Verma N (2016) Design of sliding mode
and backstepping controllers for a quadcopter, doi: https://doi.org/
10.1109/NATSYS.2015.7489097
19. Tripathi VK, Behera L, Verma N, (2016) Disturbance observer
based backstepping controller for a quadcopter. In: IECON Pro-
ceedings (Industrial Electronics Conference), pp: 108–113, doi:
https://doi.org/10.1109/IECON.2016.7794007.
20. Huo X, Huo M, Karimi HR (2014) Attitude stabilization control
of a quadrotor UAV by using backstepping approach. Math Probl
Eng. https://doi.org/10.1155/2014/749803
21. He ZF, Zhao L (2015) Quadrotor trajectory tracking based on quasi-
LPV system and internal model control. Math Probl Eng. https://
doi.org/10.1155/2015/857291
22. Hwangbo J, Sa I, Siegwart R, Hutter M (2017) Control of a
Quadrotor with Reinforcement Learning. IEEE Robot Autom Lett
2(4):2096–2103. https://doi.org/10.1109/LRA.2017.2720851
23. Zhang T, Kahn G, Levine S, Abbeel P, (2016)Learning deep control
policies for autonomous aerial vehicles with MPC-guided policy
search,In: ProceedingsIEEEInternational Conference onRobotics
and Automation, pp: 528–535, doi: https://doi.org/10.1109/ICRA.
2016.7487175.
24. Liu H, W, Zuo Z, Zhong Y, (2017) Robust Control for Quadrotors
with Multiple Time-Varying Uncertainties and Delays. IEEE Trans
Ind Electron 64(2):1303–1312. https://doi.org/10.1109/TIE.2016.
2612618
25. Trapiello C, Puig V, Morcego B (2019) Position-heading quadro-
tor control using LPV techniques. IET Control Theory Appl
13(6):783–794. https://doi.org/10.1049/iet-cta.2018.6147
26. Jayakrishnan HJ (2016) Position and attitude control of a quadro-
tor UAV using super twisting sliding mode. IFAC-PapersOnLine
49(1):284–289. https://doi.org/10.1016/j.ifacol.2016.03.067
27. Bhatia AK, Jiang J, Zhen Z, Ahmed N, Rohra A (2019) Projection
modiﬁcation based robust adaptive backstepping control for multi-
purpose quadcopter UAV. IEEE Access 7:154121–154130. https://
doi.org/10.1109/ACCESS.2019.2946416
28. Najm AA, Ibraheem IK (2019) Nonlinear PID controller design
for a 6-DOF UAV quadrotor system. Eng Sci Technol an Int J
22(4):1087–1097. https://doi.org/10.1016/j.jestch.2019.02.005
29. Castillo A, Sanz R, Garcia P, Qiu W, Wang H, Xu C (2019) Dis-
turbance observer-based quadrotor attitude tracking control for
aggressive maneuvers. Control Eng Pract. https://doi.org/10.1016/
j.conengprac.2018.09.016
30. Ahmed N, Raza A, Shah SAA, Khan R (2021) Robust Composite-
Disturbance Observer Based Flight Control of Quadrotor Attitude.
J Intell Robot Syst Theory Appl. https://doi.org/10.1007/s10846-
021-01463-6
31. Nie L, Cai B, Zhu Y, Yang J, Zhang L (2021) Switched linear
parameter-varying tracking control for quadrotors with large atti-
tude angles and time-varying inertia. Optim Control Appl Methods
42(5):1320–1336. https://doi.org/10.1002/oca.2729
32. Jiao R, Chou W, Rong Y, Dong M (2021) Anti-disturbance atti-
tude control for quadrotor unmanned aerial vehicle manipulator via
fuzzy adaptive sigmoid generalized super-twisting sliding mode
observer. Journal Vib Control. https://doi.org/10.1177/10775463
21989495
33. Scherer CW, Mohammadpour J (2012) Control of Linear Parameter
Varying Systems with Application. Springer
34. Hoffmann C, Werner H (2014) A Survey of Linear Parameter-
Varying Control Applications Validated by Experiments or High-
Fidelity Simulations, In: IEEE Trans Control Syst Technol.,
pp:1–18
35. Tarighi R, Mazinan A H., Kazemi M H, (2021) Polytopic Atti-
tude Control System for Nonlinear Unmanned Rotorcraft, Iran. J
Sci Technol Trans Electr Eng, doi: https://doi.org/10.1007/s40998-
021-00412-1
36. Rugh WJ, Shamma JS (2000) Research on gain scheduling. Auto-
matica 36:1401–1425
37. Cox PB, Weiland S, Roland T (2018) Afﬁne parameter-dependent
Lyapunov functions for LPV systems with afﬁne dependence.
IEEE Trans Automat Contr 9286:1–8. https://doi.org/10.1109/
TAC.2018.2824982
38. Huang B, Lu B, Li Q (2019) A proportional–integral-based robust
state-feedback control method for linear parameter-varying sys-
tems and its application to aircraft. Proc Inst Mech Eng Part G
J Aerosp Eng 233(12):4663–4675. https://doi.org/10.1177/095441
0018822366
39. Tarighi R, Mazinan AH, Kazemi MH (2020) Trajectory tracking of
nonlinear unmanned rotorcraft based on polytopic modeling and
state feedback control. IETE J Res. https://doi.org/10.1080/0377
2063.2020.1779136
40. Veselý V, Ilka A (2017) Generalized robust gain-scheduled PID
controller design for afﬁne LPV systems with polytopic uncer-
tainty. Syst Control Lett. https://doi.org/10.1016/j.sysconle.2017.
04.005
41. Kwiatkowski A, Werner H, Blath JP, Ali A, Schultalbers M (2009)
Linear parameter varying PID controller design for charge control
of a spark-ignited engine. Control Eng Pract. https://doi.org/10.
1016/j.conengprac.2009.06.005
42. Bolea Y, Puig V, Blesa J (2014) Gain-scheduled smith predic-
tor PID-based LPV controller for open-ﬂow canal control. IEEE
Trans Control Syst Technol 22(2):468–477. https://doi.org/10.
1109/TCST.2013.2257776
43. Feng B (2015) Robust control for lateral and longitudinal channels
of small-scale unmanned helicopters. J Control Sci Eng. https://
doi.org/10.1155/2015/483096
44. Soltanpour MR, Hasanvand F (2019) Robust linear parameter vary-
ing attitude control of a quadrotor unmanned aerial vehicle with
state constraints and input saturation subject to wind disturbance.
Trans Inst Meas Control. https://doi.org/10.1177/014233121988
3452
45. Pham TH, Ichàlal D, Mammar MS (2019) LPV and Nonlinear-
based control of an autonomous quadcopter under variations of
mass and moment of inertia. IFAC-PapersOnLine 52(28):176–183.
https://doi.org/10.1016/j.ifacol.2019.12.371
46. Pham TH., Mammar S,(2019) Quadrotor LPV Control using Static
Output Feedback IEEE 16th International Conference on Network-
ing, Sensing and Control (ICNSC), May 2019, pp: 74–79
47. Rotondo D, Nejjari F, Puig V (2013) Quasi-LPV modeling, identiﬁ-
cation and control of a twin rotor MIMO system. Control Eng Pract
21(6):829–846. https://doi.org/10.1016/j.conengprac.2013.02.004
123

## Page 13

PID-based attitude control of quadrotor using robust pole …
2397
48. Kwiatkowski A, Werner H (2008) PCA-based parameter set
mappings for LPV models with fewer parameters and less over-
bounding. IEEE Trans Control Syst Technol 16(4):781–788
49. Jabali MBA, Kazemi MH (2017) A new LPV modeling approach
using PCA-based parameter set mapping to design a PSS. J Adv
Res 8(1):23–32
50. Wu H, Fei Y (1999) Mixed H2/H∞guaranteed-cost control for
uncertain linear systems. IFAC Proc Vol. 32(2):3508–3513
51. Khargonekar PP, Member S, Rotea MA (1991) Mixed H2 /HO
Control: a convex optimization approach. IEEE Trans Automat
Control 36(7):824–837
52. Tarighi R, Mazinan AH, Kazemi MH (2023) Integral-based robust
LPV control of nonlinear ﬂight systems. Proc Inst Mech Eng Part
G J Aerosp Eng 237(4):809–823
53. Beard R W (2008) Quadrotor Dynamics and Control. In: Brigham
Young University, pp: 1–47.
54. Bouabdallah S, (2007)Design and Control of Quadrotors With
Application To Autonomous Flying, Lausanne, EPFL, doi: https://
doi.org/10.5075/epﬂ-thesis-3727.
55. Bouabdallah S, SiegwartR, (2005)Backstepping and sliding-mode
techniques applied to an indoor micro Quadrotor, In: Proceedings
- IEEE International Conference on Robotics and Automation, pp
2247–2252, doi: https://doi.org/10.1109/ROBOT.2005.1570447
56. JinL,LiS,YuJ,HeJ(2018)Robotmanipulatorcontrolusingneural
networks: A survey. Neurocomputing. https://doi.org/10.1016/j.ne
ucom.2018.01.002
57. Chilali M, Gahinet P (1996) H∞design with pole placement
constraints: an LMI approach”. IEEE Trans Automat Contr
41(3):358–367. https://doi.org/10.1109/9.486637
58. Adenso-Díaz B, Laguna M (2006) Fine-tuning of algorithms
using fractional experimental designs and local search. Oper Res
54(1):99–114. https://doi.org/10.1287/opre.1050.0243
59. Hutter F, Hoos HH, Leyton-Brown K, Stützle T (2009) ParamILS:
an automatic algorithm conﬁguration framework. J Artif Intell Res.
https://doi.org/10.1613/jair.2808
60. Hutter F, Hoos H H., Leyton-Brown K, (2011)Sequential model-
based optimization for general algorithm conﬁguration. In: Lecture
Notes in Computer Science (including subseries Lecture Notes in
Artiﬁcial Intelligence and Lecture Notes in Bioinformatics). 6683:
507–523.
61. Oishi Y, Kimura H (2003) Computational complexity of random-
ized algorithms for solving parameter-dependent linear matrix
inequalities. Automatica 39(12):2149–2156
62. Gupta A, Köro˘glu H, Falcone P (2019) Computation of low-
complexity control-invariant sets for systems with uncertain
parameter dependence. Automatica. https://doi.org/10.1016/j.auto
matica.2018.12.020
Springer Nature or its licensor (e.g. a society or other partner) holds
exclusive rights to this article under a publishing agreement with the
author(s) or other rightsholder(s); author self-archiving of the accepted
manuscript version of this article is solely governed by the terms of such
publishing agreement and applicable law.
123
