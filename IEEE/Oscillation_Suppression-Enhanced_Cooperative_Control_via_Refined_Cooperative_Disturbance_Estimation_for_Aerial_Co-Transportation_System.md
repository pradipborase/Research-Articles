# Oscillation_Suppression-Enhanced_Cooperative_Control_via_Refined_Cooperative_Disturbance_Estimation_for_Aerial_Co-Transportation_System.pdf

## Page 1

IEEE TRANSACTIONS ON AUTOMATION SCIENCE AND ENGINEERING, VOL. 22, 2025
8371
Oscillation Suppression-Enhanced Cooperative
Control via Refined Cooperative Disturbance
Estimation for Aerial Co-Transportation System
Lidan Xu , Hao Lu , Jianliang Wang , Senior Member, IEEE, Hyondong Oh , Senior Member, IEEE,
Xiang-Gui Guo , Member, IEEE, and Lei Guo , Fellow, IEEE
Abstract— This article focuses on the oscillation suppression-
enhanced
cooperative
control
design
for
the
aerial
co-transportation system consisting of two quadrotors and
a tethered pipe. The system dynamics are analyzed in depth,
which yields a decoupled model under multiple disturbances by
utilizing the variation linearization technique and coordinate
transformations. Based on this model, a refined cooperative
disturbance estimation strategy is developed to capture the
angle dynamics of the cables without direct measurements of
swing angles. Then the estimation results are used for designing
a cooperative control law to guarantee the performance in
rapid suppression of the payload oscillation and in accurate
positioning of the quadrotors under system uncertainties. The
stability and convergence of the overall system is established
using
Lyapunov
theory.
Finally,
experiments
validate
and
demonstrate the superiority of the proposed method over the
existing ones.
Note to Practitioners—This paper is motivated by the require-
ment of safe control schemes for aerial co-transportation systems.
The unexpected oscillation of the payload may result in serious
accidents, and therefore efficiently suppressing the payload swing
is the main concern of the research. Nevertheless, the cascaded
underactuation property and the complicated couplings among
the drones make it difficult to directly control the payload. Up till
Received 12 June 2024; revised 16 August 2024; accepted 19 October 2024.
Date of publication 31 October 2024; date of current version 26 March 2025.
This article was recommended for publication by Associate Editor C. Zhang
and Editor M. Dotoli upon evaluation of the reviewers’ comments. This
work was supported in part by the National Natural Science Foundation
of China under Grant 62173024, Grant 62173028, Grant 62233015, and
Grant 62273024; in part by Zhejiang Natural Science Foundation under Grant
LZ22F030012; in part by the Innovation Team of University in Guizhou
Province under Grant 2022033; in part by Guangdong Basic and Applied
Basic Research Foundation under Grant 024A1515011493; in part by the
Program for Changjiang Scholars and Innovative Research Team under Grant
IRT_16R03; in part by the Science, Technology and Innovation Project of
Xiongan New Area under Grant 2023XAGG0062; in part by the Near Space
Technology and Industry Guidance Fund under Grant LKJJ-2023008-01; and
in part by Beijing Natural Science Foundation under Grant 4232060 and Grant
IS23065. (Corresponding author: Hao Lu.)
Lidan Xu and Lei Guo are with the School of Cyber Science and Technol-
ogy, Beihang University, Beijing 100191, China.
Hao Lu and Xiang-Gui Guo are with Beijing Engineering Research Center
of Industrial Spectrum Imaging, School of Automation and Electrical Engi-
neering, University of Science and Technology Beijing, Beijing 100083, China
(e-mail: haolu@ustb.edu.cn).
Jianliang Wang is with Hangzhou Innovation Institute, Beihang University,
Hangzhou, Zhejiang 310052, China.
Hyondong Oh is with the Department of Mechanical Engineering, Ulsan
National Institute of Science and Technology, Ulsan 44919, South Korea.
Digital Object Identifier 10.1109/TASE.2024.3485237
now, at the cost of additional weight and more complicated
structure, most existing methods relying on extra sensors to detect
the states of the payload for feedback control. Accounting for
the foregoing problems, this article presents a novel sensorless
control scheme for suppressing the payload oscillation. The cable
angles are estimated using only the states of the drones. Moreover,
cooperative control laws are designed based on the estimated
results so that both antiswing and positioning performance are
guaranteed. All these aspects are verified by rigorous theoretical
analysis and hardware experiments.
Index Terms— Cooperative transportation, oscillation sup-
pression, cooperative control, refined cooperative disturbance
estimation.
I. INTRODUCTION
D
RONE delivery has achieved significant development
in the past few years because it offers a faster and
more versatile solution compared with ground transportation.
To increase the load capacity of the aerial transportation sys-
tem, one can either use a large aerial vehicle or employ more
drones to transport a payload cooperatively. Due to the limited
capability of a single aerial vehicle, cooperative transportation
by more vehicles is proved to be a more preferable choice,
which has some apparent advantages, such as higher payload
capacity [1], lower overall cost [2], and inherent mission
redundancy [3]. The aerial co-transportation systems have
gained extensive adoption across a variety of fields. In the
research [4], three quadrotors were tasked with transporting
a point-mass payload over a 45-meter outdoor span, with
the assistance of air dampers to bolster the system stability.
Additionally, a fleet of four Crazyflie drones was employed to
collaboratively carry a white fabric in a decentralized manner,
as detailed in the study [5]. Moreover, aerial co-transportation
systems have carved out a specialized role in the realm of
precision agriculture. As highlighted in the work [6], a pair
of quadrotors, equipped with a fluid tank and a pump, were
utilized to haul a pipe with nozzles spraying pesticide on crops.
The number of drones used in aerial transportation depends
on the payload scale and the task objective, e.g., manipulat-
ing the payload attitude or simply transporting the payload
from one place to another. For the slung-load transporta-
tion, under the condition that the payload mass is within
the load capacity range of the drones, using two drones to
transport a one-dimensional rigid body, such as a rod or a
1558-3783 © 2024 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:37:18 UTC from IEEE Xplore.  Restrictions apply.

## Page 2

8372
IEEE TRANSACTIONS ON AUTOMATION SCIENCE AND ENGINEERING, VOL. 22, 2025
beam, can be cost-effective and energy-efficient. Since the
one-dimensional rigid body does not have a rotation degree
of freedom around the body axis, and therefore two drones
are enough to achieve pose tracking of a rod-like object [7].
Generally, for a two-dimensional or three-dimensional rigid
body, at least three drones are needed to achieve the full-pose
control [8]. Considering that transporting the rod-like object is
a common requirement in practice, we investigate the scenario
of two quadrotors cooperatively transporting a slender pipe.
The use of more drones complicates the dynamic structure
of the overall system than the single-drone case and exacer-
bates the problems inherent in aerial transportation such as
payload oscillation [9], communication delay [10], suspen-
sion failures [11], and obstacle collision [12]. Among these
problems, payload oscillation is common and serious in aerial
cable-suspended systems [13]. The cascaded underactuation
characteristics of the suspended transportation system makes
it extremely difficult to suppress the payload swing, especially
with two-drone case [13]. Although using three or more
drones can relieve the payload swing to some extent, it is
of low efficiency to transport a rod due to loss of lift force.
Compared with the payload swing problem in the one-drone
case [14], two-drone collaborative transportation brings about
the additional coupling and interference between the drones.
By exploiting the coupling and interference among the two
drones, this paper aims to better attenuate the payload swing
for aerial co-transportation systems.
For the aerial transportation system, the existing strategies
proposed to reduce the payload oscillation can be broadly
classified into two categories: open-loop and closed-loop
strategies. Input shaping [15], [16], [17] and trajectory plan-
ning [18], [19], [20] are verified to be two types of efficient
open-loop methods in the experiments. For the single-drone-
payload case in [15] and [16], input shapers are utilized to
generate payload swing-free reference command, while for the
two-drone-payload case in [17], input shapers are introduced
to reduce both the residual oscillations of the payload and the
follower. As far as trajectory planning is concerned, dynamic
programming [18] and reinforcement learning [19] technique
are employed to optimize the trajectory to generate payload
swing-free maneuver for single-drone-payload system. In addi-
tion, a trajectory planning method based on a value-function
approximation algorithm is proposed in [20] to address the
problem of cable-suspended load transportation using three
quadrotors such that the payload can be transported smoothly
from the starting location to the target location. Although these
feedforward methods can effectively reduce the swing of the
payload caused by the movement of the drones, oscillations
excited by the initial cable angle offset, wind disturbance,
or the sudden collisions due to interaction of the payload with
the environment can not be dealt with appropriately, which
may lead to the instability of the system.
In terms of closed-loop methods, the authors in [21] design
a nonlinear hierarchical control (NHC) law based on the
energy storage function for a single drone to asymptotically
stabilize the quadrotor-payload system. Similar to this method,
an interconnection and damping assignment-passivity based
control (IDA-PBC) strategy is successfully applied in [22]
for a single drone to attenuate the payload’s swing. The
essence of these methods is damping injection and energy
dissipation. Following this core idea, the authors in [23]
develop a time-domain passivity observer (PO) for the three-
drone-payload system to detect the energy flow and use an
adaptive damping term to ensure that the storage function of
the whole system is continuously decreasing, which guarantees
the bounded stability in the experiment. In addition, a tension
estimation-based position control strategy is proposed in [24]
to achieve formation tracking (FT) for three-drone-payload
case in the experiment.
To suppress the payload oscillation in a more refined and
efficient way, several methods have introduced the cable angle
information or the payload position in feedback control [16],
[25], [26], [27]. For single-drone-payload case, the deflection
angle of the cable attached to the load is measured by a
magnetic encoder in [16] to implement the delayed feedback
approach, which can effectively deal with the perturbations
on the payload. For two-drone-payload case, an energy-based
control strategy is employed in [25] to suppress the cable
swing, where the motion capture system is utilized to obtain
the payload position. In addition, GPS modules [26] and
onboard cameras [27] are equipped on the aerial transportation
systems for implementing the so-called load priority design,
which can directly manipulate the position of the payload.
Instead of installing extra sensors for cable-related or
payload-related measurement, an almost globally convergent
nonlinear observer is designed in [28] to estimate the full
state of the tethered drone for trajectory tracking control,
only using conventional onboard sensors as an accelerometer
and a gyroscope. Similarly, a state observer is established
in [29] to estimate the swing angle of the cable for pre-
cise trajectory tracking of the drone. In addition, a filtering
technique based on a set of recursive equations is proposed
in [30] to estimate the swing angle without relying on extra
sensors. However, the aforementioned methods [28], [29],
[30] can only be applied to the single-drone-payload case
since they do not consider the coupling and interference
between the two drones caused by the suspended payload.
Furthermore, only simulations are made in these articles, and
model uncertainties and disturbances in engineering practice
are not taken into consideration. For the single-drone-payload
case in [31], the cable force on the drone is treated as
a type of periodic disturbance, and is estimated through a
known-frequency disturbance observer. This disturbance esti-
mate is used directly to compensate the disturbance via the
so-called multiple observers based anti-disturbance control
(MOBADC), the effectiveness of which is validated by a flight
test of trajectory tracking, but swing attenuation of the payload
is not considered. To the best of our knowledge, there is no
existing method which can estimate the swing angles of the
cables in two-drone cooperative transportation under model
uncertainties without direct measurement of the payload.
In this article, an aerial co-transportation system consisting
of two quadrotors and a tethered pipe is considered, and a
refined cooperative disturbance estimation strategy is proposed
to estimate the directions of the cables only using the motion
measurement of the quadrotors. Based on the estimates, the
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:37:18 UTC from IEEE Xplore.  Restrictions apply.

## Page 3

XU et al.: OSCILLATION SUPPRESSION-ENHANCED COOPERATIVE CONTROL
8373
cooperative controllers are designed to stabilize the whole
aerial co-transportation system. The main contributions are
summarized in the following aspects:
1) Instead of treating the cable force on the quadrotor as
the periodic disturbance as in [31], the proposed strategy
establishes the detailed cable force dynamics on the
two quadrotors, corresponding to “refined”. Then, the
variation-based linearization technique and coordinate
transformations are conducted to transform the coupled
system dynamics into a decoupled model for estimation
and control purpose.
2) Based on the decoupled linear model, a new refined
cooperative disturbance estimation strategy is developed
for the first time to estimate the cable directions despite
of multiple disturbances. The local swing observer uses
the exchanged information of the estimate and the
states from the neighbor quadrotor, corresponding to
“cooperative”.
3) Utilizing the estimated cable-direction information,
a cooperative control law is designed to simultaneously
achieve accurate quadrotor positioning and efficient pay-
load swing suppression. To our best knowledge, such
swing-angle estimation-based control law for coopera-
tive transportation by two drones has not been reported
in previous studies. Real-world flight tests are carried
out to verify the effectiveness of the proposed algorithm.
The test results show that the proposed method achieves
better performance than existing methods in payload
swing suppression.
II. MODELING AND SIMPLIFICATION
A. Mathematical Preliminaries
For attitude representation of a rigid body, rotation matrix
A ∈SO(3) is utilized, where
SO(3) =
n
A ∈R3×3|A⊤A = AA⊤= I3, det(A) = 1
o
denotes the special orthogonal group [32]. Here I3 ∈R3×3 is
the identity matrix and det(A) denotes the determinant of the
matrix A.
The set of 3 × 3 skew-symmetric matrix is denoted as
so(3) = {B ∈R3×3|B⊤= −B},
which corresponds to the tangent space of SO(3) at the
identity I3 ∈SO(3), i.e., the Lie algebra of SO(3).
To describe the direction of a cable, unit vector q ∈S2 is
adopted, where
S2 = {q ∈R3|q⊤q = 1}
denotes the unit sphere manifold embedded in R3 [32].
The angular velocity of a cable associated with the direction
q ∈S2 lies in the tangent space TqS2, where
TqS2 = {h ∈R3|h⊤q = 0}.
The Euclidean norm of a matrix C ∈Rm×n is defined as
∥C∥=
q
λmax(C⊤C),
Fig. 1.
Schematic of the collaborative transportation system.
where
λmax(·)
denotes
the
largest
eigenvalue
of
the
matrix.
For vector ω = [ωx, ωy, ωz]⊤, we define the mapping (·)× :
R3 →so(3) as
ω× =


0
−ωz
ωy
ωz
0
−ωx
−ωy
ωx
0

,
and its inverse mapping (·)∨: so(3) →R3 as
(ω×)∨=
ωx
ωy
ωz
⊤.
By utilizing the differentiable manifolds such as SO(3) and
S2 for configuration description, the models considered in
this paper are expressed in a coordinate-free fashion to avoid
singularities and complexities that are associated with local
parameterizations [33], e.g., Eq. (3) and Eq. (4).
B. Configuration Description
We consider two quadrotors carrying a pipe through two
massless cables as shown in Fig. 1, where the cables are
assumed to be attached to the center of mass (CoM) of the
quadrotors. Throughout this paper, the variables related to the
payload are denoted by the subscript 0, and the variables for
the ith quadrotor are denoted by the subscript i ∈{1, 2}. The
unit vectors are defined as e1 = [1, 0, 0]⊤, e2 = [0, 1, 0]⊤,
and e3 = [0, 0, 1]⊤. We choose the north-east-down (NED)
frame as the inertial frame FI = {OI, xI, yI, zI}, with OI
fixed at a point on the ground. The body-attached frame FB0 =
{OB0, xB0, yB0, zB0} for the payload is defined, with its origin
OB0 at the CoM of the payload; xB0 axis points along the
pipe toward the attachment point of the first cable; zB0 axis
is perpendicular to xB0, locates in the vertical plane, and
points downward; yB0 axis completes the right-hand frame.
The body-attached frame for the ith quadrotor is denoted by
FBi = {OBi , xBi , yBi , zBi } as shown in Fig. 1. The cables
are assumed taut and the lengths of the cables are assumed
fixed. For the sake of the following discussion, some symbols
presented in this article are summarized in Table I.
Since the cables are taut and of fixed lengths, the relation-
ship between the CoM position of the payload p0 and that of
the ith drone pi is
pi = p0 + (−1)i+1ρi R0e1 −liqi
= p0 + R0ρi −liqi,
i = 1, 2,
(1)
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:37:18 UTC from IEEE Xplore.  Restrictions apply.

## Page 4

8374
IEEE TRANSACTIONS ON AUTOMATION SCIENCE AND ENGINEERING, VOL. 22, 2025
TABLE I
NOMENCLATURE
where the vector
ρi = (−1)i+1ρi e1 ∈R3
(i = 1, 2)
(2)
is used for notation simplicity.
In summary, the configuration of the presented system is
described by the position p0 and the attitude R0 of the
payload, the direction qi (i = 1, 2) of the cables pointing
from the CoM of the ith quadrotor to the load, and the attitude
Ri (i = 1, 2) of the quadrotors, and it can be shown that
this configuration evolves on the Cartesian product of the
manifolds R3 × SO(3) × (S2 × SO(3))2.
C. Complete Nonlinear Model
The ith quadrotor can generate a thrust −fi Ri e3 (i = 1, 2)
with respect to the inertial frame FI and a torque τ i ∈R3
(i = 1, 2) with respect to its body-fixed frame FBi .
Based on the assumption that the cables are attached to
CoMs of the quadrotors, the body angular velocity of the
ith quadrotor i ∈R3 (i = 1, 2) is only subject to the
corresponding control torque τ i (i = 1, 2) and the associated
disturbance d Ri (i = 1, 2). See Eq. (5) on the next page.
Furthermore, the body angular velocity i (i = 1, 2) does not
affect the dynamics of the payload and the cables directly.
Therefore, we consider a simplified dynamic model where
the attitude kinematics and dynamics of each quadrotor are
ignored, i.e., the configuration of the whole system lies in the
manifold R3 × SO(3) × S2 × S2. The kinematics of the
multi-body system are represented as
˙p0 = ˙p0,
˙R0 = R0×
0 ,
˙qi = ωi × qi,
i = 1, 2,
(3)
where the body angular rate of the payload is denoted by
0 ∈R3, and the angular velocity of the ith cable is denoted
by ωi = qi × ˙qi ∈TqS2, satisfying q⊤
i ωi = 0 (i = 1, 2).
The dynamic equations of the system are modeled as [33]
mT ¨p0 +
2
X
i=1
mi(−R0ρ×
i ˙0 + liq×
i ˙ωi) +
2
X
i=1
mi R0(×
0 )2ρi
+mili∥ωi∥2qi = mT ge3 +
2
X
i=1
(ui + d pi ) + d p0,
¯J0 ˙0 +
2
X
i=1
miρ×
i R⊤
0 ( ¨p0 + liq×
i ˙ωi + li∥ωi∥2qi)
+×
0 ¯J00 =
2
X
i=1
ρ×
i R⊤
0 (ui + d pi + mige3) + d R0,
mili ˙ωi −miq×
i [ ¨p0 −R0ρ×
i ˙0 + R0(×
0 )2ρi]
= −q×
i (mige3 + ui + d pi ),
i = 1, 2,
(4)
where mT = P2
i=0 mi and ¯J0 = J0 −P2
i=1 mi(ρ×
i )2 are
used for notation simplicity, and ρi (i = 1, 2) is as in (2).
The control force ui ≜−fi Ri e3 ∈R3 (i = 1, 2) is regarded
as the control inputs for this model (4).
Remark 1: In this model, the bandwidth of the control
inputs ui (i = 1, 2) depends on the attitude loop of the
quadrotors given as:
˙Ri = Ri×
i ,
i = 1, 2
Ji ˙i + ×
i Jii = τ i + d Ri ,
i = 1, 2,
(5)
which are ignored in the simplified model (3) and (4). The atti-
tude dynamics of the quadrotors are assumed to be sufficiently
fast and accurate to track the desired attitude command [34].
Therefore, one can consider the control design of ui (i = 1, 2)
and τ i (i = 1, 2) separately. In this paper, we mainly focus
on the design of ui (i = 1, 2) and adopt the method in [35]
for tracking of the control forces.
In summary, the simplified system kinematics (3) and
dynamics (4) evolving on the tangent bundle of the config-
uration manifold are derived, and they are described by the
general coordinates ( p0, R0, q1, q2) and the general velocities
( ˙p0, 0, ω1, ω2).
Remark 2: What is not considered in the model (4) is the
damping force or the so-called Rayleigh dissipation force [36],
which is difficult to model precisely in practice. Therefore,
readers can consider that this damping force is included in
the disturbance d pi (i = 0, 1, 2) or d R0.
III. MODEL DECOUPLING AND TRANSFORMATION
It is nontrivial to reveal the relation among the system states
and how the states evolve under the effects of the control
inputs ui (i = 1, 2) and the disturbances d pi , d Ri (i = 1, 2)
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:37:18 UTC from IEEE Xplore.  Restrictions apply.

## Page 5

XU et al.: OSCILLATION SUPPRESSION-ENHANCED COOPERATIVE CONTROL
8375
based on the nonlinear coupled dynamics (4). Despite of
being local approximation, linearization of the model pro-
vides us an insight into the structure of this nonlinear
system and gives a simplified framework for control and
estimation design. In this section, we present a method to
decouple the system dynamics by linearizing the differential
equations in (3) and (4) about a given desired equilib-
rium1 ( p0d, ˙p0d, R0d, 0d, qid, ωid) (i = 1, 2), simplifying
the model, and transforming the coordinates. For simplicity,
we consider the ideal situation where the desired equilibrium
is given by

p0d, 03×1, I3, 03×1, (e3, 03×1)2
.
(6)
At this desired equilibrium, the control input for the ith
quadrotor is
uid = −(mi +
m0ρ j
ρ1 + ρ2
)ge3,
i, j = 1, 2,
i ̸= j,
(7)
and the disturbances (d p0, d R0, d p1, d p2) are all assumed
zero.
Remark 3: The equilibrium of the system is not limited to
the simplest configuration R0d = I3 as considered in this
paper. As a matter of fact, the proposed method can be applied
to any stable configuration of the aerial cable-suspended
transportation system. Here the stability of the configuration
can be verified by the positive definiteness of the potential
matrix as shown in [1].
A. Linearized Model
In this subsection, we exploit the variation linearization
techniques described in [37] to obtain the linear dynamics. The
infinitesimal variations of the general coordinates are denoted
by (δ p0, δR0, δq1, δq2) and the infinitesimal variations of
the general velocities by (δ ˙p0, δ0, δω1, δω2). The individual
elements of these variations are represented as
δ p0 = p0 −p0d,
δ ˙p0 = ˙p0 −˙p0d = ˙p0,
δR0 ≈R0dη×
0 = η×
0 ,
δ0 ≈(R⊤
0dδ ˙R0)∨= ˙η0,
δqi ≈ξi × qid = −e×
3 ξi,
i = 1, 2,
δωi ≈qid × δ ˙qi = −e×
3 e×
3 ˙ξi,
i = 1, 2,
(8)
where the vectors η0 ∈R3 and ξi ∈R3 (i = 1, 2) are treated
as linear approximations of the errors between the desired and
actual states of the system on SO(3) and S2, respectively [38].
In addition, the variations of the control inputs are given by
δui = ui −uid ∈R3,
i = 1, 2.
(9)
Based on the equations in (8), the linearized dynamics
can be constructed using coordinates (δ p0, η0, e×
3 ξ1, e×
3 ξ2),
its derivatives (δ ˙p0, ˙η0, e×
3 e×
3 ˙ξ1, e×
3 e×
3 ˙ξ2), the control inputs
δui (i = 1, 2), and the disturbances (d p0, d R0, d p1, d p2).
Since the third element of ξi (i = 1, 2) and ˙ξi (i = 1, 2)
1States and inputs of the desired equilibrium are represented with a
subscript d.
is not used in the coordinates and its derivatives, the matrix
E12 = [e1, e2]⊤is introduced to simplify the state vector. The
final state vector and its derivative are given by
δs = [δ p⊤
0 , η⊤
0 , ξ⊤
1 E⊤
12, ξ⊤
2 E⊤
12]⊤∈R10,
δ˙s = [δ ˙p⊤
0 , ˙η⊤
0 , ˙ξ
⊤
1 E⊤
12, ˙ξ
⊤
2 E⊤
12]⊤∈R10,
(10)
and the corresponding control inputs and disturbances are
given by
δu = [δu⊤
1 , δu⊤
2 ]⊤∈R6,
d = [d⊤
p0, d⊤
p1, d⊤
p2, d⊤
R0]⊤∈R12.
(11)
The linearized equations of the simplified dynamic model are
given in matrix form by
Mδ¨s + Kδs = Luδu + Ldd,
(12)
where the explicit expressions of the matrices M, K, Lu and
Ld are given in (13), as shown at the bottom of the next
page.
Remark 4: Although linearization based on local coordi-
nates (e.g. rope swing angles in [39]) can also lead to a
linear model, these local coordinates may lead to ambiguities
of the attitude representations, e.g., ambiguity of Euler angles.
In contrast, the variation-based linearization method here
gives a unique and coordinate-free treatment [32].
By combining the system kinematics δ˙s = δ˙s, the linearized
system can be written in a state space form as
δ˙¯s = ¯Aδ¯s + ¯Bδu + ¯Dd,
(14)
where δ¯s = [δs⊤, δ˙s⊤]⊤∈R20 and
¯A =
 010×10
I10
−M−1K
010×10

,
¯B =
 010×6
M−1Lu

,
¯D =
 010×12
M−1Ld

.
(15)
The rotation freedom of the pipe η0,x is not under con-
trol in this modeling setting [33] and is subject to the
disturbance dR0,x:
¨η0,x =
1
J0,x
dR0,x,
(16)
which can be derived by expanding the equation (14). In prac-
tice, this rotation freedom is constrained by the mechanism
of the cable attatchment. In addition, the change of η0,x has
no first-order effects on the other states in (10). Therefore,
we choose to neglect the states η0,x and ˙η0,x, and assume that
this zero dynamics are stable.
Omitting the rotation freedom η0,x and its derivative ˙η0,x,
the reduced state vector and its derivative are selected as
δsr = [δ p⊤
0 , η⊤
0 E⊤
23, ξ⊤
1 E⊤
12, ξ⊤
2 E⊤
12]⊤∈R9,
δ˙sr = [δ ˙p⊤
0 , ˙η⊤
0 E⊤
23, ˙ξ
⊤
1 E⊤
12, ˙ξ
⊤
2 E⊤
12]⊤∈R9,
(17)
where the matrix E23
= [e2, e3]⊤is introduced. Under
Assumption 1, the reduced linearized equations of the sim-
plified model are given in the matrix form by
Mrδ¨sr + Krδsr = Lr
uδu + Lr
dd,
(18)
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:37:18 UTC from IEEE Xplore.  Restrictions apply.

## Page 6

8376
IEEE TRANSACTIONS ON AUTOMATION SCIENCE AND ENGINEERING, VOL. 22, 2025
where the explicit expressions of the matrices Mr, Kr, Lr
u
and Lr
d are given in (19), as shown at the bottom of the page.
By combining the system kinematics δ˙sr = δ˙sr, the reduced
linearized system can be rewritten as
δ˙¯sr = ¯Arδ¯sr + ¯Brδu + ¯Dr d,
(20)
where δ¯sr = [(δsr)⊤, (δ˙sr)⊤]⊤∈R18 and
¯Ar =

09×9
I9
−(Mr)−1Kr
09×9

,
¯Br =

09×6
(Mr)−1Lr
u

,
¯Dr =

09×12
(Mr)−1Lr
d

.
(21)
B. Coordinate Transformation
We
assume
that
only
the
states
of
the
quadrotors
( pi, ˙pi, Ri, i) (i = 1, 2) are available for feedback control,
which can be seen as outputs of the complete nonlinear
model composed by (3), (4), and (5). Similar to the common
practice which changes the coordinates of the system from the
configuration space to the operation space, we can change the
system coordinates by utilizing the holonomic constraints (1).
Linearizing the equation (1) yields
δ pi = δ p0 + δR0ρi −liδqi
= δ p0 −ρ×
i η0 + li e×
3 ξi
= δ p0 −ρ×
i E⊤
23E23η0 + li e×
3 E⊤
12E12ξi,
i = 1, 2,
(22)
where δ pi = pi −pid (i = 1, 2) denotes the infinitesimal
variation of the CoM position of the ith quadrotor, and
ρi (i = 1, 2) denotes the vector pointing from the CoM
of the payload to the ith cable attachment point on the
payload with respect to the payload frame FB0, as mentioned
in (2).
Then, the new state vector and its derivative are defined as
follows
δsct = [δ p⊤
1 , δ p⊤
2 , ξ⊤
1 E⊤
12, ξ⊤
2 E⊤
12]⊤∈R10,
δ˙sct = [δ ˙p⊤
1 , δ ˙p⊤
2 , ˙ξ
⊤
1 E⊤
12, ˙ξ
⊤
2 E⊤
12]⊤∈R10,
(23)
satisfying
δsct = Tδsr,
(24)
M =


mT I3
−P2
i=1 miρ×
i
m1l1e×
3 E⊤
12
m2l2e×
3 E⊤
12
P2
i=1 miρ×
i
¯J0
m1l1ρ×
1 e×
3 E⊤
12
m2l2ρ×
2 e×
3 E⊤
12
−m1E12e×
3
m1E12e×
3 ρ×
1
m1l1I2
02×2
−m2E12e×
3
m2E12e×
3 ρ×
2
02×2
m2l2I2


,
K =


03×3
03×3
03×2
03×2
03×3
03×3
03×2
03×2
02×3
02×3
m0gρ2
ρ1 + ρ2
I2
02×2
02×3
02×3
02×2
m0gρ1
ρ1 + ρ2
I2


,
Lu =


I3
I3
ρ×
1
ρ×
2
−E12e×
3
02×3
02×3
−E12e×
3


,
Ld =


I3
I3
I3
03×3
03×3
ρ×
1
ρ×
2
I3
02×3
−E12e×
3
02×3
02×3
02×3
02×3
−E12e×
3
02×3


(13)
Mr =


mT I3
−P2
i=1 miρ×
i E⊤
23
m1l1e×
3 E⊤
12
m2l2e×
3 E⊤
12
P2
i=1 mi E23ρ×
i
E23 ¯J0E⊤
23
m1l1E23ρ×
1 e×
3 E⊤
12
m2l2E23ρ×
2 e×
3 E⊤
12
−m1E12e×
3
m1E12e×
3 ρ×
1 E⊤
23
m1l1I2
02×2
−m2E12e×
3
m2E12e×
3 ρ×
2 E⊤
23
02×2
m2l2I2


,
Kr =


03×3
03×2
03×2
03×2
02×3
02×2
02×2
02×2
02×3
02×2
m0gρ2
ρ1 + ρ2
I2
02×2
02×3
02×2
02×2
m0gρ1
ρ1 + ρ2
I2


,
Lr
u =


I3
I3
E23ρ×
1
E23ρ×
2
−E12e×
3
02×3
02×3
−E12e×
3


,
Lr
d =


I3
I3
I3
03×3
02×3
E23ρ×
1
E23ρ×
2
E23
02×3
−E12e×
3
02×3
02×3
02×3
02×3
−E12e×
3
02×3


(19)
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:37:18 UTC from IEEE Xplore.  Restrictions apply.

## Page 7

XU et al.: OSCILLATION SUPPRESSION-ENHANCED COOPERATIVE CONTROL
8377
where the matrix T ∈R10×9 is
T =


I3
−ρ×
1 E⊤
23
l1e×
3 E⊤
12
03×2
I3
−ρ×
2 E⊤
23
03×2
l2e×
3 E⊤
12
02×3
02×2
I2
02×2
02×3
02×2
02×2
I2

.
(25)
The matrix T is of full column rank so that this matrix can
be seen as an immersion mapping and has a left inverse T† ∈
R9×10. Therefore, the dynamic model (20) can be transformed
into
δ˙¯sct = ¯Actδ¯sct + ¯Bctδu + ¯Dct d,
(26)
where δ¯sct = [(δsct)⊤, (δ˙sct)⊤]⊤∈R20 and
¯Act =

010×10
I10
−T(Mr)−1Kr T†
010×10

,
¯Bct =

010×6
T(Mr)−1Lr
u

,
¯Dct =

010×12
T(Mr)−1Lr
d

.
(27)
C. Linearized Dynamics of Out-of-Plane Oscillation
We consider the oscillation of the payload in the Y direction,
or the out-of-plane dynamics as shown in Fig. 2, which can
be extracted from the linear model (26) as below
δ ¨p1,y = −
m0gρ2
m1(ρ1 + ρ2)ξ1,x + 1
m1
δu1,y + 1
m1
dp1,y,
δ ¨p2,y = −
m0gρ1
m2(ρ1 + ρ2)ξ2,x + 1
m2
δu2,y + 1
m2
dp2,y,
¨ξ1,x = −gρ2(m0m1ρ2
1 + J0,zm0 + J0,zm1)
J0,zm1l1(ρ1 + ρ2)
ξ1,x
+
1
m1l1
δu1,y −gρ1(J0,z −m0ρ1ρ2)
J0,zl1(ρ1 + ρ2)
ξ2,x
+
1
m1l1
dp1,y −
1
m0l1
dp0,y −
ρ1
J0,zl1
dR0,z,
¨ξ2,x = −gρ1(m0m2ρ2
2 + J0,zm0 + J0,zm2)
J0,zm2l2(ρ1 + ρ2)
ξ2,x
+
1
m2l2
δu2,y −gρ2(J0,z −m0ρ1ρ2)
J0,zl2(ρ1 + ρ2)
ξ1,x
+
1
m2l2
dp2,y −
1
m0l2
dp0,y +
ρ2
J0,zl2
dR0,z.
(28)
Remark 5: A similar method of modeling and control can
also be applied to the payload oscillation in other directions,
but we do not expand it here due to space limitation.
Remark 6: In [31], the dynamics of the cable and the pay-
load are not considered, and the cable force on the quadrotor
is modeled as a type of periodic disturbance independent of
the quadrotor dynamics. In contrast, the proposed model (28)
provides a more detailed and precise description of the trans-
portation system, which reveals the relationship between the
states of the quadrotors and the states of the cables clearly.
Assumption 1: The mass distribution of the pipe is assumed
to be uniform so that the CoM of the payload is located at the
center point of the line connecting the two suspension points,
i.e., ρ1 = ρ2 = l0 or ρ1 + ρ2 = 03×1, where l0 is the half
length of the pipe. Under this condition, the moment of inertia
about the body-attached axis zB0 satisfies J0,z = 1
3m0l2
0.
Fig. 2.
Out-of-plane oscillation of the payload.
To transform the system (28) into a cascade structure for
control purpose, we introduce the coordinate transformation
ζi = ξi,x −1
li
δpi,y,
i = 1, 2,
(29)
where −liζi = δpi,y −liξi,x (i = 1, 2) corresponds to the
variation of Y position of the ith attachment point on the
payload. By combining Assumption 1 and the coordinate
transformation (29), the model (28) can be simplified as
δ ¨pi,y = −m0g
2mili
δpi,y −m0g
2mi
ζi + 1
mi
δui,y + 1
mi
dpi,y,
¨ζi = −2g
li
ζi + g
li
ζ j −2g
l2
i
δpi,y + g
l1l2
δp j,y −
1
m0li
dp0,y
+ (−1)i · 3
m0l0li
dR0,z,
i, j = 1, 2,
i ̸= j.
(30)
Remark 7: Assumption 1 describes a specific condition that
the mass distribution of the pipe is uniform, which is a
common situation for industrial products. This condition is
utilized to simplify the expressions in the rest of the paper,
but it does not affect the generality of the proposed method.
To be explicit, for the mass-center-offset or nonuniform-mass-
distribution case, the coordinate transformation in (29) can
also be utilized to simplify the model (28), which would result
in a more complicated model than the current model (30),
and if the model parameters ρ1, ρ2, and J0,z are known,
similar procedures in section IV-A and IV-B can be applied for
cooperative estimation and control of the two-drone-payload
system.
From the perspective of anti-disturbance control [40], [41],
[42], [43], the equations in (30) can be further split into two
parts. The first part is the model of the quadrotors as
˙xi = Ai xi + Bi(δui,y + dζi + dpi,y),
i = 1, 2,
(31)
where xi = [δpi,y, δ ˙pi,y]⊤(i = 1, 2) corresponds to the states
of the quadrotors, dζi = −m0g
2 ζi (i = 1, 2) and dpi,y (i = 1, 2)
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:37:18 UTC from IEEE Xplore.  Restrictions apply.

## Page 8

8378
IEEE TRANSACTIONS ON AUTOMATION SCIENCE AND ENGINEERING, VOL. 22, 2025
can be treated as the matched disturbance, and
Ai =
"
0
1
−m0g
2mili
0
#
,
Bi =


0
1
mi

,
i = 1, 2.
The second part is the exogenous model of the disturbance dζi
as
˙wi = Wiiwi + Wi jw j + Hii xi + Hi j x j + Di d0,
dζi = Vwi,
i, j = 1, 2,
i ̸= j,
(32)
where the internal state of the disturbance dζi is denoted by
wi = [ζi, ˙ζi]⊤,
i = 1, 2,
(33)
and the unmodeled disturbance is denoted by
d0 = [dp0,y, dR0,z]⊤.
(34)
The matrices used in (32) are listed below as
Wii =


0
1
−2g
li
0

, Wi j =
" 0
0
g
li
0
#
,
Hii =


0
0
−2g
l2
i
0

,
Hi j =
" 0
0
g
l1l2
0
#
,
Di =


0
0
−1
m0li
(−1)i · 3
m0l0li

,
V =
h
−m0g
2
0
i
,
i, j = 1, 2,
i ̸= j.
Assumption 2: There exist unknown upper bounds for dp0,y,
dR0,z, and ˙dpi,y (i = 1, 2), i.e.,
|dp0,y| ≤¯d1,
|dR0,z| ≤¯d2,
| ˙dpi,y| ≤¯d3,
i = 1, 2.
(35)
Remark 8: The disturbance force dp0,y and the disturbance
torque dR0,z on the payload are assumed to be upper bounded,
which is reasonable since the changing rate of the practi-
cal physical systems is inherently bounded. In addition, the
disturbance force dpi,y (i
= 1, 2) on the ith quadrotor,
including mass uncertainty and motor degradation, changes
slowly around its equilibrium so that the time derivative of
dpi,y (i = 1, 2) can be assumed upper bounded [31].
The coupling between the states of the disturbance wi
(i = 1, 2) and the states of the quadrotors xi (i = 1, 2) is
explicitly presented in the model (32), which illustrates that
the established model is more refined than the one used in [31].
Since the methods in [41], [42], and [43] are developed only
for estimation of the disturbance independent of the system
states, they are not applicable for estimation of this coupled
disturbance. Hence, an effective solution to estimating the
disturbance dζi and dpi,y separately is proposed in the next
section.
IV. COOPERATIVE CONTROL ALGORITHM DESIGN
In this section, a refined cooperative disturbance estimation
strategy is designed to estimate the modeled disturbance dζi
and the derivative-bounded disturbance dpi,y, separately.
Based on the estimates, cooperative controllers are then devel-
oped to stabilize the whole system.
A. Refined Cooperative Disturbance Estimation Strategy
For the aerial co-transportation system considered in this
paper, the cable direction qi (i = 1, 2) is unmeasurable, so
the state of the modeled disturbance wi (i = 1, 2) in (32) can
not be obtained directly. Let ˆwi = [ˆζi, ˙ˆζi]⊤(i = 1, 2) denote
the estimates of wi (i = 1, 2). Swing observers are designed
to estimate ˆwi (i = 1, 2):
˙zwi = (Wii −Lw Bi V)(zwi + Lwxi) + Wi j(zw j + Lwx j)
+ (Hii −Lw Ai)xi + Hi j x j −Lw Bi(δui,y + ˆdpi,y),
ˆwi = zwi + Lwxi,
ˆdζi = V ˆwi,
i, j = 1, 2,
i ̸= j,
(36)
where zwi
(i
=
1, 2) is an auxiliary variable, Lw
=
diag{lw1,lw2} ∈R2×2 is the observer gain, ˆdζi = −m0g
2 ˆζi
denotes the estimate of dζi , and ˆdpi,y denotes the estimate of
the disturbance dpi,y, which is introduced to reduce the effect
of model uncertainties and nonlinearity on estimation accuracy
of wi.
The disturbance observer to estimate the derivative-bounded
disturbance dpi,y (i = 1, 2) is designed as [40]
˙z pi,y = −lp(z pi,y + lpmiδ ˙pi,y) + m0glp
2
ˆζi
+ m0glp
2li
δpi,y −lpδui,y
ˆdpi,y = z pi,y + milpδ ˙pi,y,
(37)
where z pi,y (i = 1, 2) is an auxiliary variable and lp is the
observer gain.
In principle, the swing observer shown in (36) belongs
to a specific class of disturbance observers [40], which are
designed for the disturbance with exogenous models, and
here it is used to capture the states of the cable directions.
The disturbance observer shown in (37) belongs to the class
of nonlinear disturbance observers [40], which is used to
estimate the derivative-bounded disturbance. This combination
of the two types of disturbance observers is similar to the
anti-disturbance methods in in [41], [42], and [43]. It is noted
that ˆdpi,y requires no information from the other quadrotor,
while
ˆwi requires information exchange of zwi and xi with
the other quadrotor. These information exchanges improve
the estimation performance. Therefore, we claim “refined” to
highlight the accurate disturbance modeling rather than simply
treating the cable force as a periodic disturbance as in [31],
and “cooperative” to explain the utilization of exchanged
information in the proposed swing observer.
B. Cooperative Control Law
The control objective is to develop control laws for the two
quadrotors to achieve the following behaviors.
1) The Y positions of quadrotor 1 and quadrotor 2 converge
to the desired equilibrium:
xi = [δpi,y, δ ˙pi,y]⊤→02×1,
i = 1, 2.
(38)
2) The Y positions of the attachment points on the payload
converge to the desired equilibrium:
wi = [ζi, ˙ζi]⊤→02×1,
i = 1, 2.
(39)
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:37:18 UTC from IEEE Xplore.  Restrictions apply.

## Page 9

XU et al.: OSCILLATION SUPPRESSION-ENHANCED COOPERATIVE CONTROL
8379
Fig. 3.
Control block diagram of the system.
If we directly follow the control design principle in [31], the
control input for the ith quadrotor takes the form as
δui,y = −K xxi −ˆdζi −ˆdpi,y,
i = 1, 2,
(40)
where K x = [kx1, kx2] is the control gain for position stabiliza-
tion of the quadrotors, ˆdζi (i = 1, 2) and ˆdpi,y (i = 1, 2) are
used for disturbance compensation. Since this controller (40)
simply compensates all the disturbance encountered by the
quadrotors, only precise position tracking of the quadrotors
can be achieved.
Different from the control design (40), our proposed control
input δui,y (i = 1, 2) takes the following form
δu1,y = −K xx1 −K w ˆw1 −K co ˆw2 −ˆdp1,y,
δu2,y = −K xx2 −K w ˆw2 −K co ˆw1 −ˆdp2,y,
(41)
where K w = [kw1, kw2], and K co = [kco1, kco2] are the
control gains for swing suppression. In this cooperative control
law (41), ˆwi = [ζi, ˙ζi]⊤are treated as the position and velocity
feedback of the ith attachment point on the payload for
oscillation suppression. In addition, including the information
exchange term ˆw2 in δu1,y and the information exchange term
ˆw1 in δu2,y tend to make the motion of the two quadrotors
more coordinated.
The structure of the control system, summarized by the set
of Eqs. (36), (37), and (41), is illustrated in Fig. 3.
C. Stability and Convergence Analysis
Combining (31) and (41), the closed-loop system is
described as
˙xi = (Ai −Bi K x)xi + Bi(V −K w)wi −Bi K cow j
−Bi K w ˜wi −Bi K co ˜w j −Bi ˜dpi,y,
i, j = 1, 2,
i ̸= j,
(42)
where ˜wi = ˆwi −wi (i = 1, 2) denotes the estimation error
of the swing observer (36) and ˜dpi,y = ˆdpi,y −dpi,y (i = 1, 2)
denotes the estimation error of the disturbance observer (37).
Based on (31), (32), (34), and (36), the estimation error
dynamics of wi are derived as
˙˜wi = (Wii −Lw Bi V) ˜wi + Wi j ˜w j −Lw Bi ˜dpi,y
−Di d0,
i, j = 1, 2,
i ̸= j.
(43)
Similarly, the estimation error dynamics of dpi,y are derived
by combining (31) and (37) as
˙˜dpi,y = −lp ˜dpi,y + m0glp
2
˜ζi −˙dpi,y
= −lp ˜dpi,y −lpV ˜wi −˙dpi,y,
i = 1, 2.
(44)
Finally, the whole system based on (42), (43), and (44) yields
the equation (45), as shown at the bottom of the next page,
which can be reorganized into the compact form as
˙δi = 5iiδi + 5i jδ j + µi,
i, j = 1, 2,
i ̸= j.
(46)
where the explicit expressions of δi (i = 1, 2), 5i j (i, j =
1, 2), and µi (i = 1, 2) are presented in (45). Then the overall
dynamics can be obtained as
˙δ1
˙δ2

|{z}
˙δ
=
511
512
521
522

|
{z
}
5
δ1
δ2

|{z}
δ
+
µ1
µ2

| {z }
µ
.
(47)
Theorem 1: Consider the system (47) and the given positive
parameters γ1, γ2. Under Assumption 1 and 2, if there exist
constant lp, gain matrices K x, K w, K co, and Lw satisfying
5 + 5⊤+ 2γ1I14 < 014×14,
(48a)
γ1 −
1
4γ2
> 0,
(48b)
then
the
signals
of
the
overall
closed-loop
system
(xi, wi, ˜wi, ˜dpi,y) (i = 1, 2) are bounded stable.
Proof: Similar to the proof in [41], considering µ as the
input to the system (47), the remaining ˙δ = 5δ is the original
unforced system. Using V (δ) = 1
2δ⊤δ as a Lyapunov function
candidate, the time derivative of V (δ) along the trajectory of
˙δ = 5δ + µ is
˙V (δ) = 1
2δ⊤(5⊤+ 5)δ + µ⊤δ
= −γ1∥δ∥2 +
2
X
i=1
µ⊤
i δi
≤−γ1∥δ∥2 +
2
X
i=1

w⊤
i Di d0 −˜w⊤
i Di d0 −˜dpi,y ˙dpi,y

≤−γ1∥δ∥2 +
2
X
i=1
h
∥wi∥∥Di d0∥+ ∥˜wi∥∥Di d0∥
+ | ˜dpi,y|| ˙dpi,y|
i
(49)
where the condition (48a) is used.
Based on the definition of the vector δi (i = 1, 2) in (45)
and δ in (47), the following inequalities hold for i = 1, 2
∥wi∥≤∥δi∥≤∥δ∥
∥˜wi∥≤∥δi∥≤∥δ∥
| ˜dpi,y| ≤∥δi∥≤∥δ∥
(50)
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:37:18 UTC from IEEE Xplore.  Restrictions apply.

## Page 10

8380
IEEE TRANSACTIONS ON AUTOMATION SCIENCE AND ENGINEERING, VOL. 22, 2025
Substituting (50) into (49) yields
˙V (δ) ≤−γ1∥δ∥2 + ∥δ∥·
2
X
i=1
2∥Di d0∥+ | ˙dpi,y|

= −γ1∥δ∥2 + ∥δ∥
·
2
X
i=1
 

−2
m0li
dp0,y, (−1)i · 6
m0l0li
dR0,z
⊤ + | ˙dpi,y|

≤−γ1∥δ∥2 + ∥δ∥·
2
X
i=1
 2
m0li
|dp0,y| +
6
m0l0li
|dR0,z|
+ | ˙dpi,y|

≤−γ1∥δ∥2 + ∥δ∥·
2
X
i=1
 2
m0li
¯d1 +
6
m0l0li
¯d2 + ¯d3

(51)
where Assumption 2 has been used for inequality scaling.
Define the constant 1 =
2P
i=1
2
m0li ¯d1 +
6
m0l0li ¯d2 + ¯d3, and it
follows from Young’s inequality that:
∥δ∥· 1 ≤γ212 +
1
4γ2
∥δ∥2
(52)
Therefore, the time derivative of Lyapunov function yields
˙V (δ) ≤−(γ1 −
1
4γ2
)∥δ∥2 + γ212
= −(2γ1 −
1
2γ2
)V (δ) + γ212
(53)
Based on the condition (48b) and Lyapunov boundedness
theory [44], we can conclude that the system (47) is uni-
formly ultimately bounded, implying the boundedness of δ,
and thereby the boundedness of the signals (xi, wi, ˜wi, ˜dpi,y)
(i = 1, 2), which completes the proof.
V. SIMULATION STUDIES
Simulation studies based on the complete model [33]
are
carried
out
to
validate
the
proposed
oscillation
suppression-enhanced cooperative control strategy. System and
control parameters are listed in Table II, where Rx(θ) denotes
TABLE II
PARAMETERS USED IN THE SIMULATIONS
the rotation transformation around the xI axis by the angle θ
Rx(θ) =


1
0
0
0
cos θ
−sin θ
0
sin θ
cos θ

.
The disturbance exerted on the quadrotors and the payload
are set as
d p0 =



[0, 0, 0]⊤, N,
0 ≤t < 10s
[0, 5, 0]⊤, N,
10 ≤t < 10.2s
[0, 0, 0]⊤, N,
10.2 ≤t ≤30s
d pi = [0, 0.1, 0]⊤, N,
i = 1, 2
d R0 = d R1 = d R2 = 03×1, N · m
(54)
In the simulation, the pipe is released from its initial
condition at time t = 0 and then subject to a sudden impact
at t = 10s as shown in Eq. (54). The control objective is to
suppress the payload swing by the two quadrotors for system


˙xi
˙wi
˙˜wi
˙˜dpi,y


|
{z
}
˙δi
=


Ai −Bi K x
Bi(K w + V)
Bi K w
−Bi
Hii
Wii
02×2
02×1
02×2
02×2
Wii −Lw Bi V
−Lw Bi
01×2
01×2
−lpV
−lp


|
{z
}
5ii


xi
wi
˜wi
˜dpi,y


|
{z
}
δi
+


02×2
02×2
Bi K co
02×1
Hi j
Wi j
02×2
02×1
02×2
02×2
Wi j
02×1
01×2
01×2
01×2
0


|
{z
}
5i j


x j
w j
˜w j
˜dp j,y


|
{z
}
δ j
+


02×1
Di d0
−Di d0
−˙dpi,y


|
{z
}
µi
,
i, j = 1, 2,
i ̸= j
(45)
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:37:18 UTC from IEEE Xplore.  Restrictions apply.

## Page 11

XU et al.: OSCILLATION SUPPRESSION-ENHANCED COOPERATIVE CONTROL
8381
stabilization. The desired positions pid (i = 1, 2) of the two
quadrotors are chosen based on the desired equilibrium of the
pipe ( p0d, R0d), the length of the pipe 2l0, and the length of
the ith cable li (i = 1, 2).
In addition, five methods (NHC in [21], IDA-PBC in [22],
MOBADC in [31], PO in [23], FT in [24]) are chosen
for comparison since they also only use the states of the
quadrotors for stabilization of the whole system.
A. Attachment Point Estimation
First, the positions of the attachment points on the payload
with respect to the inertial frame FI can be approximately
estimated based on the definition of the vector ξi (i = 1, 2)
in (8) as
p0i = pi + liqi = δ pi + liδqi + pid + liqid
≈δ pi −li e×
3 ξi + pid + liqid,
i = 1, 2.
(55)
Then, the Y position of the ith attachment point on the payload
can be estimated by
ˆp0i,y = δpi,y −li ˆξi,x = −li ˆζi,
i = 1, 2,
(56)
where ˆξi,x (i = 1, 2) and ˆζi (i = 1, 2) denote the estimates of
the states ξi,x (i = 1, 2) and ζi (i = 1, 2), respectively.
To give out the ground truth, the positions of the attachment
points on the payload p0i ∈R3 (i = 1, 2) are computed by
p0i = p0 + (−1)i+1l0R0e1,
i = 1, 2.
(57)
Here, the Y positions of the attachment points are expanded
as
p0i,y = p0,y + (−1)i+1l0 cos θ0 sin ψ0,
i = 1, 2,
(58)
where the Euler angles θ0 and ψ0 representing the attitude of
the payload. Therefore, the expressions (58) can be used to
compute the ground truth of the Y positions p0i,y (i = 1, 2).
The comparison of the actual states p0i,y (i = 1, 2) and
the estimates ˆp0i,y (i = 1, 2) in the simulation is depicted
in Fig. 4. It can be concluded from Fig. 4 that whether the
system is subject to the initial state offset at t = 0 or external
disturbance excitation at t = 10s, the linearized estimates can
quickly converge to the actual states in a short time period so
that they can be utilized for real time feedback control.
B. Swing Suppression
Time evolution of the payload position in the Y direction for
different methods is depicted in Fig. 5, from which an intuitive
observation is that all the methods can successfully suppress
the payload oscillation, and the proposed method achieves
the fastest convergence speed in payload swing suppression
whether under the initial state offset at t = 0 or external
disturbance excitation at t = 10s in the simulation. This result
reveals the superiority of the proposed method in oscillation
suppression of the payload over the other methods.
Fig. 4.
Estimation results of the Y positions of the attachment points in
the simulation. The light red part denotes the time period of response to the
initial state offset at t = 0, and the light blue part denotes the time period of
response to the sudden impact on the payload at t = 10s.
Fig. 5.
Time evolution of the CoM position of the payload in the Y direction
in the simulation. The light red part denotes the time period of response to
the initial state offset at t = 0, and the light blue part denotes the time period
of response to the sudden impact on the payload at t = 10s.
VI. EXPERIMENTAL IMPLEMENTATION
To demonstrate the effectiveness of the proposed refined
cooperative disturbance estimation strategy and cooperative
control law in practical implementation, real-world flight tests
are performed in an indoor flight test environment. The test
facility consists of Optitrack motion capture system, ground
station, and quadrotor platforms, which have been used to
support various research projects (see [31] and [45] for
details). A video demonstrating these scenarios is available at
https://youtu.be/KIUFwnfmHZk. System and control parame-
ters in the experiments are same as those in the simulation
except for the initial condition.
In the experiments, we set the tripod as a landmark fixed
on the ground as shown in Fig. 6. To ensure fairness in
the comparison experiments with other algorithms, the pipe
is pushed until it reaches the landmark and then released
so that the initial conditions for the experiments of different
algorithms are guaranteed to be the same. In addition, control
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:37:18 UTC from IEEE Xplore.  Restrictions apply.

## Page 12

8382
IEEE TRANSACTIONS ON AUTOMATION SCIENCE AND ENGINEERING, VOL. 22, 2025
Fig. 6.
Experimental schematic.
TABLE III
MEAN AND STD OF ABSOLUTE ERROR AND
RSME OF ESTIMATION RESULTS
parameters for all the algorithms have been carefully selected,
and the push-and-release process is repeated and averaged
for nine times for each algorithm to have a consistent result.
The related experimental data is recorded through the ground
station.
Five other methods (NHC in [21], IDA-PBC in [22],
MOBADC in [31], PO in [23], FT in [24]) are also chosen
for experimental comparison. The experimental results further
validate the merits of the controller (41) in payload swing
suppression.
A. Attachment Point Estimation
Since the position of the payload p0 and the Euler angles
θ0 and ψ0 of the payload are measured by the motion capture
system, the ground truth of the Y positions p0i,y (i = 1, 2)
can be computed through (58). The comparison of the ground
truth p0i,y (i = 1, 2) and the estimates ˆp0i,y (i = 1, 2) in the
experiment is depicted in Fig. 7, where the three peaks of the
curves correspond to the moment when the pipe is pushed to
the fixed position. The estimation results are further evaluated
using absolute errors and Root Mean Square Errors (RMSE).
The mean and standard deviation of the absolute errors and the
RMSE of the Y positions of the attachment points comparing
with the ground truth are shown in Table III. One can conclude
from Table III that the proposed swing observer can estimate
the positions of the attachment points on the payload with
small errors comparing with the ground truth from the motion
capture system. This illustrates that our swing observer (36)
can provide accurate information about the position of the
payload in real time for closed-loop control.
Fig. 7.
Estimation results of the Y positions of the attachment points in the
experiment.
Fig. 8.
Time evolution of the CoM position of the payload in the Y direction
in the experiment.
TABLE IV
COMPARISON OF THE PERFORMANCE OF PAYLOAD SWING SUPPRESSION
B. Swing Suppression
In each experiment, we record the time when the payload is
released as t = 0 and collect the Y position data of the payload
in the following thirty seconds. As shown in Fig. 8, the lines
show the average Y position of the payload in nine repeated
experiment. The performance of the methods in [21], [22],
[23], [24], and [31] is also shown in Fig. 8 for comparison.
We define yi as the amplitude of the ith local maximum of
the lines in Fig. 8. Here the first three local maxima of the
lines from t = 0, i.e., y1, y2, y3, are selected for comparison,
which are recorded in Table IV. It can be observed from
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:37:18 UTC from IEEE Xplore.  Restrictions apply.

## Page 13

XU et al.: OSCILLATION SUPPRESSION-ENHANCED COOPERATIVE CONTROL
8383
the recorded values of y1 that the payload is released from
almost the same Y position, because the differences of these
methods in y1 are millimeter level, which is close to the
limits of measurement accuracy of the motion capture system.
Based on this observation and the recorded values of y2 and
y3 in Table IV, it can be inferred that the payload swing
magnitude of the FT method decays fastest in the comparison
methods [21], [22], [23], [24], [31]. In contrast with the FT
method, the proposed method reduces the magnitude y2 and
y3 by 20.7% and 26.9%, respectively. On top of this, the
improvements are even significant at 54.9% and 68.7%, when
compared with the MOBADC method. Therefore, it is not
difficult to draw the conclusion that the proposed method
achieves the fastest convergence of the payload position in
the Y direction, which is consistent with the simulation result
in Fig. 5.
In addition, two extra indexes are defined to evaluate the
performance of the payload swing suppression. One index is
the settling time ts for the magnitude of p0,y to enter the
allowable level of residual vibration, which is defined as the
section [−0.15m, 0.15m], and the other index is the integration
of the magnitude of the residual vibration during the settling
time period [0, ts]:
χ =
Z ts
0
|p0,y(t)|dt
(59)
The larger the swing magnitude during the settling time period,
the larger the index χ will be. Compared with the settling
time ts, the index χ highlights the swing range and the
swing frequency of the payload. The comparisons of different
methods based on the two indexes (ts and χ) are also presented
in Table IV. As shown in the table, the settling time ts of the
proposed method is less than that of the IDA-PBC method
by 40.7%, and even much less than that of the rest of the
compared methods. On top of this, as long as the index χ
is concerned, the proposed method also achieves the smallest
number, which is smaller than the second smallest value (IDA-
PBC) by 21.2%. The quantitative results further illustrate the
superiority of the controller (41) in rapid oscillation suppres-
sion of the payload. In general, we attribute the excellent
performance of the proposed method to the refined cooperative
disturbance estimation strategy (36) (37) and the cooperative
control law (41), which derive the precise estimates of the
cable states and utilize them for feedback control, respectively.
VII. CONCLUSION
In this article, a systematic and complete treatment from
system modeling, control design, to experimental verification
has been developed for oscillation suppression-enhanced coop-
erative control of the aerial co-transportation systems. The
effectiveness of the proposed refined cooperative disturbance
estimation strategy has been verified in the experiments.
In addition, it has been demonstrated experimentally that
the proposed cooperative controller can achieve better perfor-
mance than the existing methods thanks to the well-designed
refined cooperative disturbance estimation strategy and the
cooperative control law. Although the proposed method can be
employed to estimate the cable directions even under the effect
of model uncertainties and nonlinearity, it requires accurate
knowledge of specific model parameters, such as the lengths
of the two cables and the mass of the payload. To adapt to the
case with uncertain model parameters, the adaptive estimation
technique [46] may be employed in the future.
REFERENCES
[1] N. Michael, J. Fink, and V. Kumar, “Cooperative manipulation and trans-
portation with aerial robots,” Auto. Robots, vol. 30, no. 1, pp. 73–86,
Jan. 2011.
[2] M. Bernard, K. Kondak, I. Maza, and A. Ollero, “Autonomous
transportation and deployment with aerial robots for search and
rescue missions,” J. Field Robot., vol. 28, no. 6, pp. 914–931,
Nov. 2011.
[3] L.
Xu,
H.
Lu,
J.
Wang,
H.
Oh,
X.-G.
Guo,
and
L.
Guo,
“Force-coordination
control
for
aerial
collaborative
transportation
based
on
lumped
disturbance
separation
and
estimation,”
IEEE
Trans.
Aerosp.
Electron.
Syst.,
vol.
60,
no.
5,
pp. 6037–6049,
Oct. 2024.
[4] K. Dong, R. Ding, S. Bai, X. Cai, and P. Chirarattananon, “Stabilizing
aerodynamic dampers for cooperative transport of a suspended pay-
load with aerial robots,” Adv. Intell. Syst., vol. 5, no. 9, Sep. 2023,
Art. no. 2300112.
[5] R. Cotsakis, D. St-Onge, and G. Beltrame, “Decentralized collaborative
transport of fabrics using micro-UAVs,” in Proc. Int. Conf. Robot. Autom.
(ICRA), May 2019, pp. 7734–7740.
[6] A. Hegde and D. Ghose, “Multi-quadrotor distributed load transportation
for autonomous agriculture spraying operations,” J. Guid., Control, Dyn.,
vol. 45, no. 5, pp. 944–951, May 2022.
[7] P. O. Pereira and D. V. Dimarogonas, “Pose and position trajectory
tracking for aerial transportation of a rod-like object,” Automatica,
vol. 109, Nov. 2019, Art. no. 108547.
[8] K. Sreenath and V. Kumar, “Dynamics, control and planning for coop-
erative manipulation of payloads suspended by cables from multiple
quadrotor robots,” in Proc. Robot., Sci. Syst. IX, Berlin, Germany,
Jun. 2013, pp. 1–8.
[9] X. Liang, H. Lin, P. Zhang, S. Wu, N. Sun, and Y. Fang, “A nonlin-
ear control approach for aerial transportation systems with improved
antiswing and positioning performance,” IEEE Trans. Autom. Sci. Eng.,
vol. 18, no. 4, pp. 2104–2114, Oct. 2021.
[10] E. Rossi et al., “Coordinated multi-robot trajectory tracking con-
trol over sampled communication,” Automatica, vol. 151, May 2023,
Art. no. 110941.
[11] X. Liang, Z. Su, W. Zhou, G. Meng, and L. Zhu, “Fault-tolerant control
for the multi-quadrotors cooperative transportation under suspension
failures,” Aerosp. Sci. Technol., vol. 119, Dec. 2021, Art. no. 107139.
[12] H. Lee, H. Kim, and H. J. Kim, “Planning and control for collision-free
cooperative aerial transportation,” IEEE Trans. Autom. Sci. Eng., vol. 15,
no. 1, pp. 189–201, Jan. 2018.
[13] E. Bulka, C. He, J. Wehbeh, and I. Sharf, “Experiments on collab-
orative transport of cable-suspended payload with quadrotor UAVs,”
in Proc. Int. Conf. Unmanned Aircr. Syst. (ICUAS), Jun. 2022,
pp. 1465–1473.
[14] J. Zeng, P. Kotaru, M. W. Mueller, and K. Sreenath, “Differential flatness
based path planning with direct collocation on hybrid modes for a
quadrotor with a cable-suspended payload,” IEEE Robot. Autom. Lett.,
vol. 5, no. 2, pp. 3074–3081, Apr. 2020.
[15] C. Adams, J. Potter, and W. Singhose, “Input-shaping and model-
following control of a helicopter carrying a suspended load,” J. Guid.,
Control, Dyn., vol. 38, no. 1, pp. 94–105, Jan. 2015.
[16] K. Klausen, T. I. Fossen, and T. A. Johansen, “Nonlinear control with
swing damping of a multirotor UAV with suspended load,” J. Intell.
Robotic Syst., vol. 88, nos. 2–4, pp. 379–394, Dec. 2017.
[17] T. Chen and J. Shan, “Cooperative transportation of cable-suspended
slender payload using two quadrotors,” in Proc. IEEE Int. Conf.
Unmanned Syst. (ICUS), Oct. 2019, pp. 432–437.
[18] I. Palunko, R. Fierro, and P. Cruz, “Trajectory generation for swing-
free maneuvers of a quadrotor with suspended payload: A dynamic
programming approach,” in Proc. IEEE Int. Conf. Robot. Autom.,
May 2012, pp. 2691–2697.
[19] A. Faust, I. Palunko, P. Cruz, R. Fierro, and L. Tapia, “Automated aerial
suspended cargo delivery through reinforcement learning,” Artif. Intell.,
vol. 247, pp. 381–398, Jun. 2017.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:37:18 UTC from IEEE Xplore.  Restrictions apply.

## Page 14

8384
IEEE TRANSACTIONS ON AUTOMATION SCIENCE AND ENGINEERING, VOL. 22, 2025
[20] X. Li, J. Zhang, and J. Han, “Trajectory planning of load transporta-
tion with multi-quadrotors based on reinforcement learning algorithm,”
Aerosp. Sci. Technol., vol. 116, Sep. 2021, Art. no. 106887.
[21] X. Liang, Y. Fang, N. Sun, and H. Lin, “Nonlinear hierarchical control
for unmanned quadrotor transportation systems,” IEEE Trans. Ind.
Electron., vol. 65, no. 4, pp. 3395–3405, Apr. 2018.
[22] M. E. Guerrero-Sánchez, D. A. Mercado-Ravell, R. Lozano, and
C. D. García-Beltrán, “Swing-attenuation for a quadrotor transport-
ing a cable-suspended payload,” ISA Trans., vol. 68, pp. 433–449,
May 2017.
[23] K. Mohammadi, S. Sirouspour, and A. Grivani, “Passivity-based
control of multiple quadrotors carrying a cable-suspended payload,”
IEEE/ASME Trans. Mechatronics, vol. 27, no. 4, pp. 2390–2400,
Aug. 2022.
[24] X. Zhang, F. Zhang, and P. Huang, “Formation planning for teth-
ered multirotor UAV cooperative transportation with unknown payload
and cable length,” IEEE Trans. Autom. Sci. Eng., vol. 21, no. 3,
pp. 3449–3460, Jul. 2024.
[25] Y. Chai, X. Liang, Z. Yang, and J. Han, “Energy-based nonlinear
adaptive control for collaborative transportation systems,” Aerosp. Sci.
Technol., vol. 126, Jul. 2022, Art. no. 107510.
[26] J. Geng and J. W. Langelaan, “Cooperative transport of a slung load
using load-leading control,” J. Guid., Control, Dyn., vol. 43, no. 7,
pp. 1313–1331, Jul. 2020.
[27] G. Li, R. Ge, and G. Loianno, “Cooperative transportation of cable
suspended payloads with MAVs using monocular vision and inertial
sensing,” IEEE Robot. Autom. Lett., vol. 6, no. 3, pp. 5316–5323,
Jul. 2021.
[28] M. Tognon and A. Franchi, “Dynamics, control, and estimation for aerial
robots tethered by cables or bars,” IEEE Trans. Robot., vol. 33, no. 4,
pp. 834–845, Aug. 2017.
[29] J. Wang, X. Yuan, and B. Zhu, “Geometric control for trajectory-tracking
of a quadrotor UAV with suspended load,” IET Control Theory Appl.,
vol. 16, no. 12, pp. 1271–1281, Aug. 2022.
[30] E. L. de Angelis, “Swing angle estimation for multicopter slung
load
applications,”
Aerosp.
Sci.
Technol.,
vol.
89,
pp. 264–274,
Jun. 2019.
[31] K. Guo, J. Jia, X. Yu, L. Guo, and L. Xie, “Multiple observers based
anti-disturbance control for a quadrotor UAV against payload and wind
disturbances,” Control Eng. Pract., vol. 102, Sep. 2020, Art. no. 104560.
[32] T. Lee, M. Leok, and N. H. McClamroch, Global Formulations of
Lagrangian and Hamiltonian Dynamics on Manifolds. Cham, Switzer-
land: Springer, 2017.
[33] T. Lee, “Geometric control of quadrotor UAVs transporting a cable-
suspended rigid body,” IEEE Trans. Control Syst. Technol., vol. 26, no. 1,
pp. 255–264, Jan. 2018.
[34] P. O. Pereira and D. V. Dimarogonas, “Pose stabilization of a bar
tethered to two aerial vehicles,” Automatica, vol. 112, Feb. 2020,
Art. no. 108695.
[35] S. Omari, M.-D. Hua, G. Ducard, and T. Hamel, “Hardware and
software architecture for nonlinear control of multirotor helicopters,”
IEEE/ASME Trans. Mechatronics, vol. 18, no. 6, pp. 1724–1736,
Dec. 2013.
[36] F. Bullo and A. D. Lewis, Geometric Control of Mechanical Systems:
Modeling, Analysis, and Design for Simple Mechanical Control Systems.
Cham, Switzerland: Springer, 2019.
[37] F. A. Goodarzi and T. Lee, “Stabilization of a rigid body payload with
multiple cooperative quadrotors,” J. Dyn. Syst., Meas., Control, vol. 138,
no. 12, Dec. 2016, Art. no. 121001.
[38] T. Lee, M. Leok, and N. H. McClamroch, “Stable manifolds of sad-
dle equilibria for pendulum dynamics on S2 and SO(3),” in Proc.
50th IEEE Conf. Decis. Control Eur. Control Conf., Dec. 2011,
pp. 3915–3921.
[39] X. Liang, Z. Zhang, H. Yu, Y. Wang, Y. Fang, and J. Han, “Anti-
swing control for aerial transportation of the suspended cargo by dual
quadrotor UAVs,” IEEE/ASME Trans. Mechatronics, vol. 27, no. 6,
pp. 5159–5172, Dec. 2022.
[40] W. Chen, J. Yang, L. Guo, and S. Li, “Disturbance-observer-based
control and related methods—An overview,” IEEE Trans. Ind. Electron.,
vol. 63, no. 2, pp. 1083–1095, Feb. 2016.
[41] H. Lu, C. Liu, L. Guo, and W.-H. Chen, “Flight control design
for small-scale helicopter using disturbance-observer-based backstep-
ping,” J. Guid., Control, Dyn., vol. 38, no. 11, pp. 2235–2240,
Nov. 2015.
[42] C. Liu and W.-H. Chen, “Disturbance rejection flight control for small
fixed-wing unmanned aerial vehicles,” J. Guid., Control, Dyn., vol. 39,
no. 12, pp. 2810–2819, 2016.
[43] Y.
Zhu,
L.
Guo,
J.
Qiao,
and
W.
Li,
“An
enhanced
anti-
disturbance attitude control law for flexible spacecrafts subject to
multiple disturbances,” Control Eng. Pract., vol. 84, pp. 274–283,
Mar. 2019.
[44] H. K. Khalil, Nonlinear Systems, 3rd ed., Upper Saddle River, NJ, USA:
Prentice-Hall, 2002.
[45] J. Jia, K. Guo, X. Yu, W. Zhao, and L. Guo, “Accurate high-
maneuvering trajectory tracking for quadrotors: A drag utilization
method,” IEEE Robot. Autom. Lett., vol. 7, no. 3, pp. 6966–6973,
Jul. 2022.
[46] A. Glushchenko and K. Lastochkin, “Exponentially stable adaptive
observation for systems parameterized by unknown physical param-
eters,” IEEE Trans. Autom. Control, vol. 69, no. 8, pp. 5635–5642,
Aug. 2024.
Lidan Xu received the B.S. degree from Beihang
University, China, in 2019, where he is currently
pursuing the Ph.D. degree with the School of Cyber
Science and Technology.
His research interests include geometric con-
trol, force regulation, cooperative manipulation, and
interaction planning under disturbance.
Hao Lu received the B.Sc. degree in measurement-
control technology and instrumentation from Harbin
Institute of Technology, Weihai, China, in 2010,
and the Ph.D. degree in precision instrument and
machinery from Beihang University, Beijing, China,
in 2016.
He
was
a
Visiting
Ph.D.
Student
with
the
Department of Aeronautical and Automotive Engi-
neering, Loughborough University, Loughborough,
U.K., from 2013 to 2014. He was a Senior Engi-
neer with Beijing Electro-Mechanical Engineering
Institute, Beijing, from 2016 to 2020. He was an Associate Research Fellow
with Hangzhou Innovation Institute, Beihang University, Hangzhou, China,
from 2020 to 2024. He is currently an Associate Professor with the School of
Automation and Electrical Engineering, University of Science and Technol-
ogy Beijing, Beijing. His research interests include anti-disturbance control,
constrained control, cooperative control, and autonomous decision-making for
unmanned aerial vehicles.
Jianliang Wang (Senior Member, IEEE) received
the B.E. degree in electrical engineering from
Beijing Institute of Technology, Beijing, China,
in 1982, and the M.S.E. and Ph.D. degrees in
electrical engineering from Johns Hopkins Uni-
versity, Baltimore, MD, USA, in 1985 and 1988,
respectively.
From 1988 to 1990, he was a Lecturer with Bei-
hang University, Beijing, China. From 1990 to 2019,
he was a tenured Associate Professor with Nanyang
Technological University, Singapore. Since 2020,
he has been a Senior Researcher/Professor with Hangzhou Innovation Institute,
Beihang University. His current research interests include multi-agent systems,
UAVs and UAMs, vehicular platoon systems, and fault-tolerant control.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:37:18 UTC from IEEE Xplore.  Restrictions apply.

## Page 15

XU et al.: OSCILLATION SUPPRESSION-ENHANCED COOPERATIVE CONTROL
8385
Hyondong Oh (Senior Member, IEEE) received the
B.Sc. and M.Sc. degrees in aerospace engineering
from Korea Advanced Institute of Science and Tech-
nology (KAIST), South Korea, in 2004 and 2010,
respectively, and the Ph.D. degree in autonomous
surveillance and target tracking guidance of multiple
UAVs from Cranfield University, U.K., in 2013.
He was a Lecturer in the field of autonomous
unmanned vehicles with Loughborough University,
U.K., from 2014 to 2016. He is currently an Asso-
ciate Professor with the Department of Mechanical
Engineering, Ulsan National Institute of Science and Technology (UNIST).
His research interests include autonomy, decision-making under uncertainty,
learning-based perception, planning and control, and swarming/flocking con-
trol for unmanned systems.
Xiang-Gui Guo (Member, IEEE) received the B.S.
degree from the College of Electrical Engineer-
ing, Northwest University for Nationalities, China,
in 2005, the M.S. degree from the College of Electri-
cal Engineering and Automation, Fuzhou University,
China, in 2008, and the Ph.D. degree in control sci-
ence and engineering from Northeastern University,
China, in 2012.
He was a Post-Doctoral Fellow with the School
of Electrical and Electronic Engineering, Nanyang
Technological University, Singapore. He is currently
a Professor with the School of Automation and Electrical Engineering,
University of Science and Technology Beijing, Beijing, China, and is also
a part-time Professor with the Autonomous Intelligent Systems Department,
Hangzhou Innovation Institute, Beihang University, Hangzhou, China. His
research interests include multi-agent systems, fuzzy systems, fault-tolerant
control, and vehicular platoon control.
Lei Guo (Fellow, IEEE) was born in Qufu, China,
in 1966. He received the B.S. and M.S. degrees
from Qufu Normal University in 1988 and 1991,
respectively, and the Ph.D. degree from Southeast
University, Nanjing, China, in 1997.
From 1991 to 1994, he was a Lecturer with Qing-
dao University, Qingdao, China. From 1997 to 1999,
he was a Post-Doctoral Fellow and an Associate Fel-
low with Southeast University. From 1999 to 2000,
he was a Post-Doctoral Fellow with IRCCyN,
Nantes, France. From 2000 to 2005, he was a
Research Associate/Fellow/Visiting Professor with Loughborough University,
UMIST, and Manchester University, U.K., respectively. From 2004 to 2006,
he was a Professor with Southeast University. Since 2006, he has been
a Distinguish Professor and the Director of the Space Intelligent Control
Research Center, Beihang University, Beijing, China. Currently, he is a Guest
Chair Professor. He is an Academician of the Chinese Academy of Sciences
(CAS). He has published more than 480 articles, seven monographs, and has
more than 180 authorized invention patents. His research interests include
anti-disturbance control theory and applications, intelligent navigation, and
control technology of unmanned systems. He is a fellow of IET, Chinese
Association of Automation (CAA), and China Association of Inventions (CAI.
He was a recipient of the National Nature Science Awards in 2013, the
National Technology Invention Award in 2018, and the National Pioneer
Innovation Award of China in 2023. He also obtained the Gold Medal of the
International Exhibition of Inventions of Geneva, Nuremberg, and Türkiye,
for bio-inspired navigation sensors, compound-eye-inspired navigation sys-
tems, and biomimetic flying robots, respectively. He is the Director of the
Navigation, Guidance, and Control Committee of CAA.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:37:18 UTC from IEEE Xplore.  Restrictions apply.
