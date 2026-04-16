# Nonlinear System Identification of a UAV Model with Distributed Aerodynamics and Flexible Structure.pdf

## Page 1

CEAS Aeronautical Journal (2023) 14:661–677
https://doi.org/10.1007/s13272-023-00674-x
ORIGINAL PAPER
Nonlinear system identiﬁcation of a UAV model with distributed
aerodynamics and ﬂexible structure
Benjamin Herrmann1
· Julian Theis1 · Frank Thielecke1
Received: 27 February 2023 / Revised: 8 June 2023 / Accepted: 26 June 2023 / Published online: 25 July 2023
© The Author(s) 2023
Abstract
This paper presents the nonlinear system identiﬁcation of a slightly ﬂexible 25kg ﬁxed-wing UAV in the time-domain using
a computationally efﬁcient distributed aerodynamics model and a linear structural dynamics representation. The equations of
motion are formed by making use of the free vibration modes of the structure and the mean axes formulation. The structural
modes and mode shapes are determined from ground vibration tests. The distributed aerodynamics, accounting for elastic
deformations, are modeled using a quasi-steady stability and control derivative approach and by applying strip theory. Initial
distributions for the derivatives are obtained from vortex-lattice-method calculations. For matching the model response to the
measured response, parameters for scaling the initial derivative distributions are introduced. The ﬂexible model is subsequently
identiﬁed based on ﬂight test data using the output error method in the time-domain and maximum-likelihood estimation. A
good overall identiﬁcation result is achieved with a close match of the fast aircraft dynamics. Finally, an evaluation is given
on the suitability of the identiﬁed model for real-time simulation, loads’ estimation, and active load control law design.
Keywords Nonlinear system identiﬁcation · Aeroelastic modeling · UAV · Flight tests
List of symbols
ax, ay, az
Translational accelerations expressed in OB R
coordinates, m/s2
bcm
Position vector of OBG relative to OB R to, m
bN P
Position vector of neutral point relative to OBG,
m
br,N P
Rigid-body position vector of neutral point rel-
ative to OBG, m
br,SP
Rigid-body position vector of structure support
point relative to OBG, m
C A,F
Coefﬁcient vector of aerodynamic forces
C A,M
Coefﬁcient vector of aerodynamic moments
CD
Drag coefﬁcient
CD0
Zero drag coefﬁcient
Cl
Roll moment coefﬁcient
B Benjamin Herrmann
benjamin.herrmann@tuhh.de
Julian Theis
julian.theis@tuhh.de
Frank Thielecke
frank.thielecke@tuhh.de
1
Institute of Aircraft Systems Engineering, Hamburg
University of Technology, Nesspriel 5, 21129 Hamburg,
Germany
Cl0
Zero roll moment coefﬁcient
CL
Lift coefﬁcient
CL0
Zero lift coefﬁcient
CLα,ϕ=0
Lift curve slope of unswept wing, 1/rad
CLδc
Lift stability derivative of control surfaces, 1/rad
Cm
Pitch moment coefﬁcient
Cm0
Zero pitch moment coefﬁcient
Cn
Yaw moment coefﬁcient
CY
Side force coefﬁcient
CYβ
Side force stability derivative, 1/rad
CYδr
Side force rudder control derivative, 1/rad
c
Wing aerodynamic mean chord, m
ci
Local strip chord, m
D
Diagonal matrix with entries {s, c, s}, m
d
Elastic (translational) deformation vector in
OB R coordinates, m
dV
Volume element, m3
y
Local strip width, m
F A
Vector of aerodynamic forces, N
Fext
Vector of external forces, N
FMP
Vector of forces and moments at mass point, N
and N·m
FSG
Vector of internal loads at strain gauge, N and
N·m
123

## Page 2

662
B. Herrmann et al.
G
Gravity acceleration vector, m/s2
h
Altitude, m
J
Inertia tensor, kg·m2
k
K-factor of induced drag
k_C
Scaling parameter for derivative distribution
M A
Vector of aerodynamic moments, N·m
Mext
Vector of external moments, N·m
m
Aircraft mass, kg
N
Number of samples
ne
Number of elastic modes
n f
Number of ﬂaperons
ns
Number of strips
OAS
Local aerodynamic strip frame
OBG
Global body-ﬁxed frame
OB R
Body-reference frame (center of mass)
OBS
Local strip-ﬁxed frame
OBSG
Strain gauge sensor frame
OI
Inertial reference frame
p
Position vector of mass element relative to OB R,
m
p, q,r
Angular rates (roll, pitch, yaw), rad/s
ps
Static pressure, Pa
q
Dynamic pressure, Pa
q A
Dynamic pressure of relative ﬂow, Pa
q N
Dynamic pressure of normal ﬂow, Pa
Qη j
Generalized forces of j-th mode, N·m
r
Position vector of mass element relative to OI,
m
r0
Position vector of origin of OB R, m
Si
Local strip surface area, m2
Sref
Wing reference surface area, m2
s
Half wing span, m
s
Undeformed position vector relative to OB R, m
T
Air temperature, deg
T B R I
Transformation matrix from OI to OB R
T BS BG
Transformation matrix from OBG to OBS
T BS B R
Transformation matrix from OB R to OBS
T BSG B R
Transformation matrix from OB R to OBSG
TSGMP
Transformation matrix from mass point forces/
moments to strain gauge internal loads
Tϕ
Transformation matrix from the undeformed
strip to OBS
tinit
Time of initial maneuver condition, s
Ui
Theil’s inequality coefﬁcient for i-th output
u, v, w
Translational velocities expressed in OB R coor-
dinates, m/s
uI, vI, wI Translational velocities expressed in OI coordi-
nates, m/s
u A, vA, wATranslational aerodynamic velocities, m/s
u
Input vector
V
Translational velocity vector of OB R, m/s
VA
Aerodynamic velocity at OB R, m/s
V A,i
Local aerodynamic velocity vector, m/s
V N,i
Local normal ﬂow vector, m/s
VT AS
True airspeed, m/s
v
Measurement noise vector
X0
Steady ﬂow-separation point
y
System output vector
ˆy
Simulation model output vector
yd
Deterministic system output vector
α
Angle of attack, rad
αeff
Effective angle of attack, rad
β
Angle of sideslip, rad
βeff
Effective angle of sideslip, rad
tϵT
Time delay of downwash at tailplane, s
δa
Aileron deﬂection, rad
δc
Control surface deﬂection, rad
δe
Elevator deﬂection, rad
δ f
Flaperon deﬂection, rad
δr
Rudder deﬂection, rad
ϵb
Bending strain, 0.01%
ϵs
Shear strain, 0.01%
ϵt
Torsion strain, 0.01%
ϵT
Induced downwash angle, rad
ε0, εe
Rigid and elastic twist angle, rad
η
Generalized displacement coordinate
λ
Longitude, deg
μ
Generalized mass, kg·m2
ν0, νe
Rigid and elastic dihedral angle, rad
ω
Angular velocity vector of OB R, rad/s
ωA
Aerodynamic angular velocity vector of OB R,
rad/s
ωn
Undamped natural (modal) frequency, rad/s
ρ
Air density, kg·m−3
ξ
Structural (modal) damping ratio
ϕ
Latitude, deg
ϕ
Elastic angular deformation vector relative to
OB R, rad
ϕe
Elastic sweep angle, rad
ϕ25c
Rigid sweep angle at quarter chord line, rad
, , 
Euler angles (roll, pitch, yaw), rad
 j
Mode shapes
ang, j
Mode shapes for elastic angular deformation
trans, j
Mode shapes for elastic translational deforma-
tion

Estimation parameter vector
0
Initial estimation parameter vector
i
Estimation parameter
(·)|B R
(·) expressed in OB R
1 Introduction
Main drivers in aircraft development, in addition to safety,
relate to the need of an increased fuel efﬁciency to reduce
operational cost and fulﬁll increasingly demanding envi-
123

## Page 3

Nonlinear system identiﬁcation of a UAV model...
663
ronmental regulations. The efforts have led to constructing
aircraft with lighter structures and higher aspect ratio wings
which thus become more ﬂexible. Due to the increase in
ﬂexibility, such wings are characterized by lower natural fre-
quencies and exhibit increased in-ﬂight deformations. These
can lead to a coupling of rigid-body motion and elastic defor-
mation through the aerodynamic forces and moments [1,
2]. Flight control systems further complicate the interaction,
possibly leading to degraded [3] or unstable [4] control per-
formance.Therefore,theseinteractionsneedtobeconsidered
in the design models for ﬂight control systems.
Depending on the characteristics of the aircraft, the pur-
pose of application, or the availability of experimental data,
different modeling frameworks are required. In the context of
this work, the objective is the development of an aeroelastic
model for a slightly ﬂexible 25kg ﬁxed-wing UAV that can
be adapted based on ﬂight test data using system identiﬁca-
tion techniques in the time-domain. The model is intended
for real-time simulation, loads’ estimation, and active load
control law design. Therefore, a model of moderate com-
plexity with a limited number of state variables is required.
Beyond that, it is desired to maintain a distributed aerody-
namics model, such that local forces and moments can be
calculated.
An overview of different aerodynamics modeling and sys-
tem identiﬁcation activities including applications for ﬂexi-
ble aircraft is given in [5]. The modeling of ﬂexible aircraft
is suggested with an additional dynamic-pressure-dependent
part associated with each stability and control derivative of
a classical model structure. However, this approach is only
valid provided that the rigid-body and structural frequencies
are sufﬁciently separated. A uniﬁed framework for model-
ing ﬂexible aircraft is presented in [6] and later in [7]. The
equations of motion are derived by Lagrange’s equation and
the principle of virtual work. Further, the authors make use
of a modal representation of the structure and the mean
axes constraints to minimize inertial coupling between the
rigid-body and elastic degrees of freedom (assuming small
deformations). The nonlinear equations of motion of the
ﬂexible aircraft then simplify and are presented in terms of
the nonlinear equations of the rigid-body motion and addi-
tional linear differential equations for the modal deﬂections
of the structure. The equations are solely coupled by the
aerodynamic forces and moments. The modeling of aero-
dynamics is further proposed with a quasi-steady stability
and control derivative approach and by applying strip the-
ory. Strip theory is a simple method often found in models
concerned with the investigation of wake vortex encounter,
namely aerodynamic interaction models (AIM) [8–10]. In
strip theory, the lifting surfaces of the aircraft are divided
into spanwise strips. Each strip is then treated as a two-
dimensional airfoil with its local geometric and aerodynamic
characteristics. This approach allows for the resolution of
local relative ﬂow conditions and the resulting change in
force and moment distributions. However, the effects of
three-dimensional ﬁnite span wing are neglected. Outside
aerodynamic interaction models, the application of strip the-
ory is, e.g., found in real-time full-envelope aerodynamic
models for small UAVs [11]. The modeling methodology of
[6] was further adopted in later works by various authors, in
[12] together with quasi-steady strip aerodynamics, and in
[13, 14] together with unsteady aerodynamics using modi-
ﬁed strip theory [15, 16] to account for the effects of ﬁnite
span and indicial functions [17, 18]. The work of [12, 13]
both aimed at modeling only incremental aerodynamics due
to elastic deformations, assuming the availability of a rigid-
body ﬂight mechanics and aerodynamics model. System
identiﬁcation techniques for ﬂexible aircraft in combination
with the framework of [6, 7] can be found in [19, 20] for the
identiﬁcation of a high-performance glider. Although keep-
ing the quasi-steady derivative approach for modeling the
aerodynamic forces, moments, and generalized loads, the
derivatives are not determined by applying strip theory, but
directly estimated as parameters within the parameter estima-
tion process. This modeling approach is a the straightforward
extension of the traditional rigid-body approach to a ﬂexible
structure, which can be easily combined with system iden-
tiﬁcation techniques. However, the distributed property of
the aerodynamics model is lost. Other applications of sys-
tem identiﬁcation for ﬂexible aircraft are found, e.g., in [21]
for the in-ﬂight identiﬁcation of structural modes using an
eigensystem realization algorithm (ERA).
Given the review on the literature, the framework of [6, 7]
is a powerful method for modeling slightly ﬂexible aircraft.
Further, strip theory is simple yet effective for modeling local
aerodynamic forces and moments. The objective of this work
is to maintain this strip aerodynamics model while allow-
ing for the adaption of the model using system identiﬁcation
techniques in the time-domain. The paper is structured as fol-
lows. Section2 introduces the slightly ﬂexible unmanned test
aircraft G-Flights Dimona and summarizes the test activities
that were performed. Section3 describes the modeling of the
test aircraft. Within this section, the equations of motion are
developed using the free vibration modes of the structure
and the mean axes formulation of [6]. Further, the model-
ing of quasi-steady strip aerodynamics is explained. Finally,
Sect. 4 presents the identiﬁcation and evaluation of the ﬂex-
ible model.
2 Unmanned test aircraft G-Flights Dimona
The slightly ﬂexible test aircraft G-Flights Dimona, depicted
in Fig.1, is an unmanned replica of the HK36 Super Dimona
at a scale of 1:3. It is driven by an electrical motor with a
maximum power of 4kW, and has a total mass of 25kg and a
123

## Page 4

664
B. Herrmann et al.
Fig. 1 Test aircraft G-Flights Dimona
length of 2.4m. The original wings of the aircraft have been
replaced by custom spar, rib, and foil manufactured wings
with increased span and ﬂexibility. The total wingspan of the
aircraft is 5.4m with a total wing surface area of 1.68m2. The
aircraft can either be controlled by a safety pilot via remote
control or by a ﬂight control computer. It is equipped with
a total of four control surfaces at the trailing edge of each
wing: inner/outer ailerons and inner/outer ﬂaperons, which
are used for lateral–directional control and for load control.
The aircraft further comprises a rudder for lateral–directional
control and two elevators for longitudinal control and load
control.
2.1 Test instrumentation
The aircraft is equipped with the standard test instrumen-
tation of a rigid-body aircraft and an additional test instru-
mentation integrated into the structure of fuselage, wings,
and empennage. The standard test instrumentation com-
prises several sensors, computers, and radio equipment. An
industry-grade high-precision inertial navigation platform
(INS) supported by dual antennas is used for the measure-
ment of GPS position, attitude, velocities, and accelerations.
An increased position accuracy of 0.02 m is achieved with a
third antenna on ground providing differential GPS correc-
tion. Airspeed, angle of attack, angle of sideslip, static air
pressure, and air temperature are measured by three air data
systems (ADS). They each consist of a ﬁve-hole-probe with
an additional inertial measurement unit (IMU) and tempera-
ture sensor for measurement correction. The airdata systems
are located at the left (ADS1) and the right (ADS2) wing
as well as at the vertical tail (ADS3). The air data systems
were developed in-house and calibrated in wind tunnel exper-
iments [22]. The standard test instrumentation is completed
by a data recorder computer and separate real-time ﬂight con-
trol computer. The ﬂight control computer serves as the main
host for GNC applications and issues control outputs to the
servo actuators. Further, it supports direct code deployment
from Matlab/Simulink. Data distribution between the sen-
sors and computers is implemented via Ethernet-network and
Controller Area Network (CAN). Table 1 lists the available
Table 1 Standard measurement parameters
Name
Symbol
Unit
Latitude
ϕ
deg
Longitude
λ
deg
Altitude
h
m
Roll angle

rad
Pitch angle

rad
Heading

rad
Roll rate
pINS
rad/s
Pitch rate
qINS
rad/s
Yaw rate
rINS
rad/s
Longitudinal velocity
uINS
g
m/s
Lateral velocity
vINS
g
m/s
Vertical velocity
wINS
g
m/s
Longitudinal acceleration
aINS
x
m/s2
Lateral acceleration
aINS
y
m/s2
Vertical acceleration
aINS
z
m/s2
Angle of attack
αADS1-3
deg
Angle of sideslip
βADS1-3
deg
Static pressure
pADS1-3
s
Pa
Dynamic pressure
qADS1-3
Pa
Air temperature
T ADS1-3
◦C
measurement parameters of the standard test instrumenta-
tion.
The additional test instrumentation is distributed at var-
ious sections along the fuselage, wings, and empennage to
measure structural dynamics and loads. It comprises sev-
eral IMUs and strain gauges (shear, bending, and torsion)
which are concentrated in load measurement stations (LMS).
Figure2 displays the distribution of the sensors along the
test aircraft. Since the measurement of loads and structural
dynamics for wings and empannage is of prime importance,
most sensors are located in these areas.
2.2 Ground vibration test and modal analysis
Considering the slight ﬂexibility of the test aircraft, the
assumption of linear structural dynamics is reasonable.
Therefore, it was decided to represent the elastic deforma-
tion of the structure by a set of free vibration modes and
mode shapes. To determine the structural modes of the air-
craft, a ground vibration test (GVT) and experimental modal
analysis was performed at the Technische Universität Berlin.
Hammer and shaker inputs were used to excite the structural
vibrations of the aircraft. The ﬁrst seven structural modes up
to the ﬁrst symmetric wing torsion mode were identiﬁed and
considered for the structural dynamics model. Details on the
measurement setup, test execution, and results are presented
123

## Page 5

Nonlinear system identiﬁcation of a UAV model...
665
Fig. 2 Distribution of additional
test instrumentation along the
test aircraft
Inertial Measurement Unit (IMU)
Strain gauge (SG)
LMS1
LMS2
LMS3
LMS4
LMS5
LMS6
LMS7
LMS8
LMS9
LMS10
LMS11 / LMS12
LMS13
LMS14
Table 2 First seven identiﬁed
structural modes of the
G-Flights Dimona
Mode
Deﬁnition
Modal
Modal
frequency ωn
damping ξ
(Hz)
(%)
1
First symmetric wing bending
3.97
0.85
2
First antisymmetric wing bending
8.56
1.38
3
First antisymmetric vertical tailplane bending
11.18
1.24
4
First symmetric in-plane wing bending
13.21
1.83
5
Second symmetric wing bending
14.60
1.79
6
First symmetric horizontal tailplane bending
17.24
2.76
7
First symmetric wing torsion
25.83
1.91
in [23]. The structural mode shapes were subsequently deter-
mined from a ﬁnite-element (FE) model adapted to the GVT
data. Table 2 lists the seven structural modes with modal
frequency ωn and modal damping ξ. Figure3 further visual-
izes the modes. Especially, the ﬁrst symmetric wing bending
mode exhibits a low natural frequency. Considering the servo
actuator bandwidth of 6.74 Hz, it is the mode likely to be
excited by control action or atmospheric disturbance.
2.3 Flight tests
A comprehensive ﬂight test campaign was performed to
acquire ﬂight data for system identiﬁcation. The campaign
included a total of seven ﬂights with 109 maneuvers per-
formed. All maneuvers were executed with the help of
an in-house developed autopilot for aerodynamic param-
eter identiﬁcation [24], which was adapted based on an
a priori estimation of the rigid-body dynamics. Details
on the overall concept and main components of the test
setup are given in [25]. A variety of classical maneuvers
speciﬁcally designed for the identiﬁcation of the rigid-body
dynamics were ﬂown [26]. They comprised multiple lon-
gitudinal maneuvers including 3-2-1-1 maneuvers, pulse
maneuvers and level deceleration maneuvers. Further, differ-
ent lateral–directional maneuvers were performed including
bank-to-bank maneuvers and rudder doublets. A full descrip-
tion of the maneuver characteristics is presented in [24].
The longitudinal maneuvers were executed by the eleva-
tors, while the lateral–directional maneuvers were executed
by the ailerons, ﬂaperons, and rudder. To identify the indi-
vidual control effectiveness of ailerons and ﬂaperons, four
different control conﬁgurations were varied within the bank-
to-bank maneuvers: execution of the maneuvers by (1) inner
and outer ailerons, (2) only inner ailerons, (3) only outer
ailerons, and (4) inner and outer ﬂaperons. The maneuvers
were ultimately repeated around different trim velocities in
the range of VT AS = 18–30m/s.
3 Flexible aircraft model
This section describes the ﬂexible aircraft model. The mod-
eling methodology is based on the framework of [6] and strip
theory. The equations of motion are developed by represent-
ing the structural dynamics with free vibration modes and
making use of the mean axes constraints. The aerodynamic
strip forces and moments are modeled using a quasi-steady
stability and control derivative approach.
3.1 Equations of motion
The position r of an arbitrary mass element ρdV of an elas-
tic body can be expressed in an inertial reference frame OI
(xI, yI , zI) in terms of its relative position p to a body-
reference frame OB R (x, y, z) and the position r0 of the
origin of OB R (see Fig.4). The speciﬁed positions of the mass
element in the inertial and body-reference frames are then
related by the expression r = r0 + p. The body-reference
axes OB R may rotate with an angular velocity ω and their ori-
entation may be deﬁned by an arbitrary Euler angle sequence.
The axes move with the body but are not necessarily attached
to a material point.
123

## Page 6

666
B. Herrmann et al.
Fig. 3 Visualization of the ﬁrst
seven structural modes of the
G-Flights Dimona
Mode 1, ω  = 3.97 Hz
n
Mode 2, ω  = 8.56 Hz
n
Mode 3, ω  = 11.18 Hz
n
Mode 4, ω  = 13.21 Hz
n
Mode 5, ω  = 14.60 Hz
n
Mode 6, ω  = 17.24 Hz
n
Mode 7, ω  = 25.83 Hz
n
123

## Page 7

Nonlinear system identiﬁcation of a UAV model...
667
Fig. 4 Deﬁnition of a mass element’s position using inertial OI
(xI , yI , zI ) and body OB R (x, y, z) reference frames
Assume that a modal description of the structure is avail-
able (e.g., from ground vibration tests and ﬁnite-element
model), such that the elastic deformation d at a point (x, y, z)
can be expressed in terms of mode shapes  j(x, y, z) and
the generalized displacement coordinates η j(t) by
d(x, y, z, t) =
ne

j=1
 j(x, y, z)η j(t),
(1)
where ne denotes the number of elastic modes of the uncon-
strained, undamped vibration problem. Then, the position of
the mass element relative to OB R can be separated into its
undeformed part s(x, y, z) (rigid body) and its deformation
part d(x, y, z, t). The body-reference frame OB R may be
used to develop the equations of motion of the unconstrained
elastic body, assuming that each mass element is treated as
a point mass. When doing so, inertial coupling can occur
between the rigid degrees of freedom and the elastic degrees
of freedom. However, it is found that with a suitable choice
of OB R satisfying the mean axes constraints and the origin of
OB R located at the instantaneous center of mass, the inertial
coupling can be neglected [6, 27].
The mean axes, ﬁrst introduced by [28], deﬁne a body
frame for which the relative translational and angular
momenta, due to the elastic deformation, are zero for all
time t ≥0. Combined with the modal description of the
structure and only assuming small deformations (i.e., defor-
mation and deformation rate are colinear), the constraints can
be expressed by [6, 7]
ne

j=1
dη j
dt

V
 j ρ dV = 0,
ne

j=1
dη j
dt

V
s ×  j ρ dV = 0.
(2)
Itcanbeshownthatfortheconstraintstobesatisﬁed,theelas-
tic degrees of freedom must be orthogonal to the translational
and rotational rigid-body degrees of freedom, respectively
[6, 29]. These conditions are guaranteed when the elastic
deformations are represented by free vibration modes and
the body-reference frame OB R is located at the instantaneous
center of mass. The decoupled equations of motion of the
elastic body are then given by [6, 13]
˙V|B R = −ω|B R × V|B R + T B R I G
I + 1
m Fext

B R
(3)
˙ω|B R = −J−1(ω|B R × (Jω|B R)) + J−1Mext|B R
(4)
¨η j = −2ξ jωn, j ˙η j −ω2
n, jη j + 1
μ j
Qη j .
(5)
The ﬁrst two equations are formally equivalent to the stan-
dard nonlinear rigid-body ﬂight dynamic equations for the
translational and rotational degrees of freedom. Within these
equations, V|B R and ω|B R denote the translational and angu-
lar velocity vectors of the body-reference axes OB R with
respect to the inertial reference axes OI, expressed in body-
reference coordinates. The gravity acceleration vector G|I is
expressed in OI coordinates and transformed to OB R with
the transformation matrix T B R I. The aircraft mass is m and
the inertial tensor J. Note that with the assumption of small
deformations, J is considered constant. The vectors Fext|B R
and Mext|B R denote the sum of external forces and moments
expressed in coordinates of OB R. Only aerodynamic forces
are considered in this work. The last Eq.5 represents the ne
linear differential equations for the structural dynamics in
generalized coordinates. Within these equations, η j denotes
the generalized displacement, ωn, j the undamped natural fre-
quency, ξ j the modal damping ratio, μ j the generalized mass,
and Qη j the generalized forces of each mode. Given the non-
linearrigid-bodyequationsofmotionandthelinearequations
of motion of the structure decoupled as presented, a coupling
is solely due to Fext|B R, Mext|B R, and Qη j .
3.2 Quasi-steady strip aerodynamics
The aerodynamic forces and moments of the test aircraft
are modeled by applying strip theory. All effective lifting
surfaces, i.e., wings, horizontal tail, and vertical tail, are
divided into a ﬁnite number of spanwise strips. Each strip
is then treated as a two-dimensional airfoil with its own geo-
metric and aerodynamic characteristics. The aerodynamic
characteristics are modeled by means of quasi-steady param-
eters. This implies that the resultant aerodynamic forces and
moments at every time instant have reached their steady-state
values and are only dependent on the instantaneous conﬁg-
uration and local relative ﬂow. The aerodynamic forces and
123

## Page 8

668
B. Herrmann et al.
moments of the fuselage are expressed by additional quasi-
steady parameters acting on the center of mass.
Consider the aircraft with its lifting surfaces divided into
a ﬁnite number of ns spanwise strips, each with local width
dyi, local chord ci, and local surface area Si. Each strip is
assigned a structure support point (SP) at its centerline for
which the instantaneous deformation (elastic translational
deformation and elastic angular deformation) is known from
the superposition of structural mode shapes and generalized
displacements coordinates. The aircraft can then be treated
as a discrete structure of interconnected points, as shown in
Fig.5, which mark the elastic axes of the lifting surfaces.
For the modeling of aerodynamic forces and moments,
each strip is further assigned two aerodynamic control points
along its centerline, i.e., a neutral point (NP), which is
assumed at the 25%-chord position and a zero pressure point
(PP0) which is assumed at the 50%-chord position. In strip
theory, the strips themselves are assumed non-deformable.
Therefore,theirmotioncanbedescribedsimilartothemotion
of a ﬂat plate, as indicated in Fig.5 for the ith strip.
The instantaneous position of each strip’s structure sup-
port point, neutral point, and zero pressure point can be
described relative to a global body-ﬁxed frame OBG. The
frame OBG is aligned with the body-reference axes OB R (ori-
gin at the center of mass) but is translated by a vector bcm,
considered constant due to the assumption of small deforma-
tions [7]. Further, a local strip-ﬁxed frame OBS is introduced
which deﬁnes the instantaneous translation and orientation of
the strip’s 25%-chord line. Its origin is located at the neutral
point and its orientation relative to OBG is deﬁned by three
rotations. The three rotation angles are the rigid and elastic
dihedral angles (ν0,i, νe,i), the rigid and elastic twist angles
(ε0,i, εe,i), and the rigid and elastic sweep angles (ϕ25c,i,
ϕe,i). The rotation from OBG to OBS is given by the transfor-
mation matrix T BS BG. With the alignment of OBG and OB R,
the transformation matrix T BS BG equals T BS B R.
Let bN P,i denote the instantaneous position of the strip’s
neutral point relative to the global body-ﬁxed axes OBG.
Further deﬁne br,N P,i as the rigid-body part of the position
vector and
d(xi, yi, zi, t) =
ne

j=1
trans, j(xi, yi, zi)η j(t)
(6)
ϕ(xi, yi, zi, t) =
ne

j=1
ang, j(xi, yi, zi)η j(t)
(7)
as the elastic translational deformation and elastic angu-
lar deformation vectors of the ith structure support point
along and about the body-reference axes, respectively. In
the equations, trans, j contains the mode shapes for elas-
tic translational deformation and ang, j the mode shapes for
elastic angular deformation. Then, under the assumption of
no chord-wise deformation of the strip, the position bN P,i
relative to the body-ﬁxed axes OBG is calculated by
bN P,i(t) = br,N P,i + d(xi, yi, zi, t)
+Tϕ,i(t)(br,N P,i −br,SP,i)
(8)
with br,SP,i denoting the rigid-body position vector of
the ith strip structure support point and Tϕ,i denoting the
transformation matrix of the rotation about OB R from the
undeformed strip to OBS with the angles given by the elastic
angular deformation in Eq.7. Note that bN P,i is indicated
time varying to distinguish between the non-time-varying
terms in the equation. This notation is omitted for simpliﬁ-
cation in the following. Similar expressions can be derived
for the position vectors of structure support point and zero
pressure point.
The aerodynamic characteristics of the strips are mod-
eled with quasi-steady parameters. In this sense, each strip
is assigned a local non-dimensional lift coefﬁcient CL,i and
a local non-dimensional drag coefﬁcient CD,i, where each
coefﬁcient itself is formed by stability and control deriva-
tives normalized by Si /Sref
CL,i = CL0,i + CLα,ϕ=0,i ·

1 +

X0,i
2

· αeff,i
+
nc

n=1
CLδc,n ,i · δc,n
(9)
CD,i = CD0,i + ki · C2
L,i.
(10)
In the equations, CL0,i and CD0,i are the strip’s zero lift and
drag coefﬁcient, CLα,ϕ=0,i indicates the lift curve slope of
the unswept strip, αeff,i is the strip’s local effective angle of
attack, ki is the strip’s k-factor of induced drag, and CLδc,n ,i
and δc are the nc control derivatives and deﬂections of the
available control surfaces, respectively. Steady stall effects
are included in terms of Kirchhoff’s theory of ﬂow separa-
tion and an approximation of the steady ﬂow-separation point
X0,i based on hyperbolic tangent [26]. For vertical stabilizer
strips, the non-dimensional lift coefﬁcient is interpreted as a
side force coefﬁcient CY,i with the effective angle βeff,i. All
termsareassumedtoactonthestrip’sneutralpoint,exceptfor
CL0,i and CLδc,n ,i ·δc,n, which are assumed to act on the strip’s
zero pressure point and a variable point along the centerline
asafunctionofthedeﬂection[30],respectively.Theyareulti-
mately transferred to the strip’s neutral point. The additional
moments caused thereby are expressed in terms of non-
dimensional moment coefﬁcients Cl,i (roll), Cm,i (pitch), and
Cn,i (yaw). Non-dimensionality is achieved through divid-
ing the moments by s (roll, yaw) and c (pitch), respectively.
Finally, the aerodynamic characteristics of the fuselage are
modeled by additional non-dimensional force and moment
coefﬁcients with classical 1-point stability derivatives.
123

## Page 9

Nonlinear system identiﬁcation of a UAV model...
669
Fig. 5 Position and orientation
of the ith strip relative to the
global body-ﬁxed frame OBG
and deﬁnition of the local
strip-ﬁxed frame OBS
Fig. 6 Local relative ﬂow at the
ith strip and force and moment
coefﬁcients (assuming ϕe,i = 0)
To calculate the effective angles in Eq.9, the local relative
ﬂow at each strip has to be determined. This is achieved by
summing all individual ﬂow components at OBS, i.e., the
linear aerodynamic velocity of OB R, plus additional terms
due to rotation about OB R, and the velocity of the structure
V A,i|B R = V A|B R + ωA|B R × (bN P,i −bcm)
+
ne

j=1
trans, j(xi, yi, zi)˙η j.
(11)
The induced velocity due to elastic angular deformation
about the structure support point is neglected. In Eq.11,
V A|B R andωA|B R denotethelinearandangularaerodynamic
velocity vector at OB R, respectively. Downwash effects are
taken into account at tailplane strips by the induced down-
wash angle ϵT ,i. It is proportional to the angle of attack at
OB R and ﬂaperon deﬂections, delayed by tϵT ,i, the time the
ﬂow requires to reach the tailplane strips [31]
ϵT ,i(t) = ∂ϵT
∂α · α(t −tϵT ,i) +
n f

n=1
∂ϵT
∂δ f ,n
· δ f ,n(t −tϵT ,i).
(12)
Herein, ∂ϵT /∂α and ∂ϵT /∂δ f ,n denote the partial derivatives of
the downwash angle to the angle of attack at OB R and n f
ﬂaperon deﬂections. In this work, the calculation of tϵT ,i is
simpliﬁedbytakingthemeandistancebetweenwingandhor-
izontal or vertical tail strip neutral points along xB R, divided
by the airspeed VA at OB R. The downwash angles are then
used to correct the local relative ﬂow at the tailplane strips.
The local relative ﬂow is originally deﬁned in the local strip
aerodynamic frame OAS, but as given in Eq.11, is already
123

## Page 10

670
B. Herrmann et al.
expressed in components along OB R. Then, the angle of
attack αi and angle of sideslip βi of the local relative ﬂow
deﬁne the orientation of OAS relative to OB R. The local rel-
ative ﬂow at the i-th strip is illustrated in Fig.6.
With the transformation matrix T BS B R, the local relative
ﬂow from Eq.11 can be expressed in OBS coordinates. It is
then straight forward to calculate the effective angles needed
for the calculation of the aerodynamic force coefﬁcient in
Eq.9 from the relative ﬂow components u A,i, vA,i, and wA,i,
by
αeff,i = arctan
wA,i|BS
u A,i|BS
	
,
βeff,i = arcsin
vA,i|BS
|V A,i|
	
.
(13)
Indicated in Fig.6, the orientation of the force and moment
coefﬁcients is either given along the coordinates of OAS
(deﬁned by αi and βi) or along the normal ﬂow compo-
nent V N,i, but overall rotated about the body-reference axis
xB R by the rigid and elastic dihedral angle.1 They can be
expressed in components of the body-reference axes OB R
throughasequenceofrotationsinvolvingtheseanglesandare
summarized to coefﬁcient vectors for the aerodynamic forces
C A,F
i
|B R and moments C A,M
i
|B R, respectively. The resulting
forces and moments at either the neutral point (strips) or the
center of mass (fuselage) are then given by
F A
i |B R = q N,i Sref C A,F
i
|B R
(14)
M A
i |B R = q N,i Sref D C A,M
i
|B R
(15)
with the diagonal matrix D, which has the main diagonal
elements {s, c, s}, and the effective dynamic pressures of the
normal ﬂow for wing and horizontal tail strips (Eq.16a) and
vertical tail strips (Eq.16b) as
q N,i = q A,i cos2(βeff,i)
(16a)
q N,i = q A,i cos2(αeff,i).
(16b)
The forces and moments of all strips are ultimately trans-
ferred to the center of mass and summed up for the equations
of motion of the rigid-body degrees of freedom. The general-
ized forces Qη j for the equations of the structural dynamics
can be obtained by ﬁrst transferring all strip forces and
moments to their respective structure support points. Then,
the resulting strip forces and moments are collected in vector
form and are subsequently transformed with the transposed
1 Assuming no elastic sweep angle ϕe,i = 0. If ϕe,i ̸= 0, a further
rotation is given by this angle.
mode shapes
Qη j = T
j
⎡
⎢⎢⎢⎢⎢⎢⎣
F A
x
F A
y
F A
z
M A
x
M A
y
M A
z
⎤
⎥⎥⎥⎥⎥⎥⎦
SP
.
(17)
4 Flexible model identiﬁcation and
evaluation
This section is concerned with the identiﬁcation of the ﬂex-
ible aircraft model and the evaluation of the results. Prior
to the actual parameter estimation, a simulation model is
assembled and implemented in Matlab/Simulink. Given
the equations of motion of the ﬂexible aircraft and the quasi-
steadystripaerodynamicsmodel,themodeliscombinedwith
additional models from the in-house library FLYSim. These
include an earth and atmosphere model, a wind and turbu-
lence model, and an actuator model for the representation of
servo and control surface dynamics. Moreover, a propulsion
model and landing gear model are added. Subsequently, a
suitable set of maneuvers is selected. This is accomplished
by post-processing the gathered ﬂight test data and transfer-
ring all the available measurement parameters listed in Table
1 to the center of mass. Moreover, the load measurement
parameters are corrected by the dead weight of the structure.
The selection of maneuvers is based on different criteria,
such as precision of maneuver execution, dynamic pressure
variations, and atmospheric disturbance.
4.1 Parameter estimation
The estimation of model parameters is performed with the
in-house tool DAVIS, using the output error method in the
time-domain, as depicted in Fig.7, and maximum-likelihood
estimation [26]. Based on an initial a priori estimation of the
model parameters 0, the simulation model is excited by the
same inputs u(t) as in the maneuvers of the ﬂight tests (see
Sect. 2.3) and the simulated model response ˆy(t) is compared
to the measured aircraft system response y(t). Only measure-
ment noise v(t) is considered to corrupt the deterministic
system output yd(t). Applying a maximum-likelihood func-
tion,theresponseerror y(t)−ˆy(t)isminimizedinaniterative
optimization process through adaption of the model param-
eters by the parameter change . To this end, sensitivities
∂ˆy/∂ of the model output with respect to the model param-
eters are calculated.
Suitable model parameters i to be estimated need to be
deﬁned. Since the structural dynamics model was identiﬁed
123

## Page 11

Nonlinear system identiﬁcation of a UAV model...
671
Fig. 7 Block schematic of the output error method with maximum-
likelihood function [26]
from GVT data, only parameters of the strip aerodynamics
model are estimated. Initial distributions of the normal-
ized stability and control derivatives are obtained from
three-dimensional vortex-lattice-method calculations of the
aircraft in the open source software tool xflr5. The aircraft
is modeled with its rigid shape lifting surfaces but without
fuselage as advised by xflr5. The inﬂuence of lifting sur-
face thickness is neglected and treated as an uncertainty. To
this end, all lifting surfaces are divided into spanwise strips
based on geometric properties and the resolution of local ﬂow
effects. A total number of 48 wing strips, 8 horizontal tail
strips, and 5 vertical tail strips are considered. Subsequently,
the locations of the strips are used to deﬁne associated struc-
ture support points as described in Sect. 3.2 and determine
the structural mode shapes from the adapted FE-model. The
resulting distributions are shown in Fig.8.
According to the aerodynamic parametrization of the
non-dimensional force coefﬁcients, separate distributions are
obtained for zero coefﬁcients, stability derivatives, and con-
trolderivatives.Theassociatedcontrolsurfacedeﬂectionsare
δa,in and δa,out for inner and outer ailerons, δ f ,in and δ f ,out
for inner and outer ﬂaperons, δr for the rudder, and δe for the
elevators. Each wing control surface is assumed to only inﬂu-
ence the lift of all strips on the side of the wing it is attached
to. Parameters for linearly scaling the initial distributions
are introduced and deﬁned as estimation parameters. In this
way, the initial distributions can be adapted in the estimation
process with a limited number of estimation parameters. On
the other hand, the achievable solution is constrained by the
qualitative shapes of the initial distributions. Separate scal-
ing parameters are deﬁned for each lifting surface, i.e., wings,
horizontal tail, and vertical tail. Scaling parameters for the
control derivative distributions of opposite control surfaces
are either paired or grouped based on the control allocations
used in the ﬂight tests (indicated in Fig.8 with the color code).
The additional stability derivatives of the fuselage and down-
-2
0
2
yBR (m)
0
0.1
0.2
0.3
 CLx,i (-) or (1/rad)
a)
-0.4
0
0.4
yBR (m)
0
0.02
0.04
0.06
 CLx,i (-) or (1/rad)
b)
-0.3 -0.2 -0.1
zBR (m)
-0.05
0
0.05
 CYx,i (-) or (1/rad)
c)
-2
0
2
yBR (m)
0
2
4
6
8
 CD0,i (-)
10-4d)
-0.4
0
0.4
yBR (m)
1.2
1.3
1.4
 CD0,i (-)
10-4 e)
-0.3 -0.2 -0.1
zBR (m)
1.2
1.3
1.4
1.5
1.6
 CD0,i (-)
10-4 f)
Fig.8 Initialderivativedistributionsfrom xflr5:a)wingliftwithCL0,i
(
), CLα,i (
), CLδ f ,i(
), CLδa,in ,i (
), CLδa,out ,i (
), b) horizontal
tail lift with CLα,i (
), CLδe ,i (
), c) vertical tail side force with CYβ,i
(
), CYδr ,i (
), d) to f) parasitic drag of wing, horizontal, and vertical
tail
wash parameters are treated as direct estimation parameters
with no effect on the distributions. Stall parameters and k-
factors of induced drag are determined separately from ﬂight
data and the vortex-lattice-method calculations, respectively,
and kept ﬁxed for the estimation. Measurement outputs of
the rigid-body motion (center of mass) are selected and set
as criteria for the parameter estimation
y =
 VT AS α β ˙p ˙q ˙r p q r    ax ay az u v w T .
(18)
Herein, VT AS, α, and β are the true airspeed, angle of attack,
and angle of sideslip, p, q, andr the roll, pitch, and yaw rates,
, , and  are the Euler angles for roll, pitch, and yaw, and
u, v, and w are the translational velocities expressed on OB R
coordinates.
The values and relative standard deviations of the ﬁnal
estimated distribution scaling parameters are listed in Table
3. A value close to 1 indicates an estimation result close to the
initial distributions from xflr5. This is found for the param-
eter k_CYβ of the vertical tail, the parameters k_CLα,wing and
k_CLα,htp of the wing and the horizontal tail, and the param-
eter k_CLδa,out of the outer ailerons. Least agreement with
the initial distributions from xflr5 are found for the param-
eters k_CD0 of all lifting surfaces, k_CL0,wing of the wing,
and k_CLδe of the elevators. The result of k_CD0 being sig-
niﬁcantly underestimated by xflr5 is expected considering
the interpolation of viscous drag from two-dimensional polar
data associated with the calculation method. Low relative
123

## Page 12

672
B. Herrmann et al.
Table 3 Estimated distribution scaling parameters
i
Value
Rel. std. deviation (%)
k_CD0
3.1389
1.95
k_CYβ
0.9988
0.82
k_CYδr
0.8234
1.33
k_CL0,wing
0.3105
3.26
k_CLα,wing
1.1425
0.87
k_CLα,htp
0.8897
0.76
k_CLδ f
0.7746
1.09
k_CLδe
0.5646
0.74
k_CLδa,in
0.7401
1.08
k_CLδa,out
0.9731
0.99
Table 4 Estimated additional parameters
i
Value
Rel. std. deviation (%)
∂ϵT /∂α
0.411
1.75
∂ϵT /∂δ f
0.0248
1.72
CYβ,fuse
−0.1295
11.82
Cl0,fuse
−0.0017
1.01
Cm0,fuse
−0.0378
4.87
standard deviations are achieved for all estimated distribu-
tion scaling parameters.
Table 4 further lists the values and relative standard devi-
ations of the ﬁnal estimated additional parameters of the
fuselage and downwash. Only a few parameters for the most
dominant fuselage effects are incorporated in the ﬁnal param-
eter set. An increased relative standard deviation is only
observed for the parameter CYβ,fuse of the fuselage.
Matching plots of the identiﬁcation result are shown in
Fig.9 for longitudinal and lateral maneuvers with measure-
ment parameters at the center of mass. A good overall
identiﬁcation result is achieved for all maneuvers. Espe-
cially, the fast aircraft dynamics are matched well, which
is important for control law design. Good matches are also
achieved for the translational rigid-body accelerations (ax,
ay, az), which are directly related to the external forces act-
ing on the aircraft. Note that gravitational accelerations are
not measured by the sensors. Some model deﬁciencies are
found for the measurement parameters true airspeed VT AS
and pitch angle , which indicate slight deviations of the
model’s pitching moment to the measured aircraft’s pitch-
ing moment. Unexpected model behavior is also observed
in the last part of the level deceleration maneuver. However,
judging from the control action of ailerons and rudder, an
undetected asymmetric atmospheric disturbance is suspected
to inﬂuence the maneuver.
Table 5 Theil’s inequality coefﬁcient of the identiﬁcation result
Measurement parameter
Symbol
Ui
Altitude
h
0.050
True airspeed
VT AS
0.268
Roll angle

0.190
Pitch angle

0.215
Angle of attack
α
0.277
Angle of sideslip
β
0.160
Roll rate
p
0.183
Pitch rate
q
0.192
Yaw rate
r
0.168
Longitudinal acceleration
ax
0.292
Lateral acceleration
ay
0.263
Vertical acceleration
az
0.193
The identiﬁcation result is further analyzed by means of
Theil’s inequality coefﬁcient (TIC) [32]. First introduced in
the ﬁeld of economics, the coefﬁcient provides a measure of
the accuracy of a prediction from a model with its value rang-
ing from zero to unity. Due to its simplicity, it is often adopted
for system identiﬁcation (e.g., [20]). The Theil’s inequality
coefﬁcient Ui is deﬁned as
Ui =

1
N
N
k=1(yi(tk) −ˆyi(tk))2

1
N
N
k=1(yi(tk))2 +

1
N
N
k=1( ˆyi(tk))2
,
(19)
with N denoting the number of samples, and yi(tk) and
ˆyi(tk)), as previously deﬁned, denoting the measured aircraft
system response and simulated model response, respectively.
However, in the calculation of the coefﬁcient, these outputs
are implemented as the variations from the initial condition
yi(tinit) [33]. In the present case of a sequence of multiple
maneuvers, the initial condition of each individual maneuver
has to be used. Table 5 lists the Theil’s inequality coefﬁcient
for all measurement parameters of the identiﬁcation result in
Fig.9. A value of zero corresponds to a perfect model pre-
diction, whereas values close to unity indicate signiﬁcantly
different responses. Values below 0.3 are said to indicate a
good agreement of measured and simulated responses [34].
As can be seen from Table 5, this is the case for all mea-
surement parameters. The differences in TIC values further
conﬁrm the visual impression of the identiﬁcation result in
Fig.9.
4.2 Evaluation of structural load distribution
In a ﬁnal step, the identiﬁed model is evaluated with regard
to its capability to estimate distributed structural loads and
its use in active load control law design. To this end, struc-
123

## Page 13

Nonlinear system identiﬁcation of a UAV model...
673
Fig. 9 Identiﬁcation result for
longitudinal/lateral maneuvers
with measurement parameters at
the center of mass, measurement
(
), simulation (
), and
maneuver separation (
)
-10
-5
0
5
e
(deg)
-10
0
10
a,in
(deg)
-10
0
10
a,out
(deg)
-5
0
5
r
(deg)
0
10
20
f,in/out
(deg)
120
180
240
 h
(m)
20
25
30
VTAS
(m/s)
-20
0
20
(deg)
-15
-5
5
(deg)
-5
0
5
(deg)
-10
0
10
(deg)
-20
0
20
 p
(deg/s)
-20
0
20
 q
(deg/s)
-20
0
20
 r
(deg/s)
-2
-1
0
 ax
(m/s2)
-1
0
1
 ay
(m/s2)
0
20
40
60
80
100
120
Time [s]
-20
-10
0
 az
(m/s2)
tural loads measured at wing load measurement stations are
compared to the model outputs. The outputs are constructed
as part of a separate loads model and capture the internal
loads acting on the strain gauges of the load measurement
stations. Aerodynamic forces and moments as well as iner-
tial forces at local mass points (MP) are considered. The
mass points are deﬁned based on the locations of the strain
gauges and a detailed CAD model. The aerodynamic strip
forces and moments are allocated and transferred to these
mass points considering their elastic points of attack. Elastic
position vectors of the mass points can be obtained simi-
lar to Eq.8 and an interpolation of mode shapes  j(x, y, z)
at the mass point positions, assuming a rigid connection
between mass point and elastic axis. Next, inertial forces
are added. Local accelerations are derived based on [35]
which include rigid-body accelerations and the effects of
elastic deformation on angular rates and translational accel-
eration. The total forces and moments at the mass points
FMPi = [Fx Fy Fz Mx My Mz]T are then used to calcu-
late the internal loads FSGi = [Qx Qy Qz Mx My Mz]T
by transferring them to the strain gauge positions. Figure10
exempliﬁes the internal loads at SG10 on the right wing.
For the single pair of MP10 and SG10 with individual distance
[x, y, z] from mass point to strain gauge along the axes
of OB R, the internal loads at SG10 due to the forces and
moments at MP10 can be derived according to [36, 37] as
⎡
⎢⎢⎢⎢⎢⎢⎣
Qx
Qy
Qz
Mx
My
Mz
⎤
⎥⎥⎥⎥⎥⎥⎦
SG10
=
⎡
⎢⎢⎢⎢⎢⎢⎣
1
0
0
0
0
0
0
1
0
0
0
0
0
0
1
0
0
0
0
−z
y
1
0
0
z
0
−x
0
1
0
−y
x
0
0
0
1
⎤
⎥⎥⎥⎥⎥⎥⎦
·
⎡
⎢⎢⎢⎢⎢⎢⎣
Fx
Fy
Fz
Mx
My
Mz
⎤
⎥⎥⎥⎥⎥⎥⎦
MP10
(20)
FSG10 = TSG10MP10 · FMP10.
(21)
123

## Page 14

674
B. Herrmann et al.
Fig. 10 Calculation of internal loads in OB R: a) position of strain gauges (SG) and mass points (MP) on the right wing; b) sum of forces and
moments at SG10 (section A–A)
Similarly, the internal loads from other pairs of mass points
and strain gauges can be calculated, each by applying the
respective distance from mass point to strain gauge. For the
total internal loads at all strain gauges on the right wing, a
total transformation matrix can be constructed with each of
the transformation matrices corresponding to single pairs of
mass points and strain gauges, as shown in Eq.20, to
⎡
⎢⎢⎢⎢⎣
FSG10
FSG09
FSG08
FSG07
FSG06
⎤
⎥⎥⎥⎥⎦
=
⎡
⎢⎢⎢⎢⎣
TSG10MP10
0
· · ·
0
TSG09MP10 TSG09MP09 · · ·
0
TSG08MP10 TSG08MP09 · · ·
0
TSG07MP10 TSG07MP09 · · ·
0
TSG06MP10 TSG06MP09 · · · TSG06MP06
⎤
⎥⎥⎥⎥⎦
·
⎡
⎢⎢⎢⎢⎣
FMP10
FMP09
...
FMP06
⎤
⎥⎥⎥⎥⎦
.(22)
As seen in the equation, the forces and moments at all mass
points MP6 to MP10 contribute to the total internal loads at
the innermost strain gauge SG6.
With Eq.22, the internal loads at the strain gauges are
given in components of OB R which is compliant with the
calibration axes of the sensors on the G-Flights Dimona.
However, if the calibration is given in the sensor coordi-
nate systems OBSGi , in a ﬁnal step, the internal loads need
to be transformed into the sensor coordinate systems with
the transformation matrices T BSGi B R. The rotation angles
are then given by the sum of rigid-body and elastic angular
deformation angles at the sensor positions relative to OB R.
The latter can be determined through an interpolation of
mode shapes for elastic angular deformation ang, j(x, y, z)
at the sensor positions and generalized displacement coordi-
nates η j(t). The same overall approach is used to calculate
the internal loads at the strain gauges on the left wing and
empennage.
Figure11 compares the shear forces Qz measured at mid-
dle and inner load measurement stations along the wing (see
Fig.2) to the respective outputs of the structural loads’ model
for the same maneuver sequence.
Close matches are found for all shear forces for the majority
of maneuvers. This result indicates a plausible representa-
tion of the actual load distribution along the wing. Moreover,
the close match of shear forces at inner load measurement
stations Qz,LMS5 (left wing) and Qz,LMS6 (right wing) is in
good agreement with the identiﬁcation result of az, since
both stations capture the majority of aerodynamic loads. An
unexpected model behavior is solely found for the inner load
measurement stations during ﬂaperon bank-to-bank maneu-
vers, where the effects of local load increase/decrease due to
ﬂaperon deﬂection and the resulting rotation of the aircraft
are not represented correctly. It is suspected that either the
negligence of a dedicated fuselage model within xflr5 and
therewith negligence of wing–fuselage interaction effects on
the initial derivative distributions, or the load application on
the inner load measurement stations is a possible cause of
the deviation.
Three-dimensional effects on the induced angle of attack
were investigated in [38] with a 1g and 2.5g wind tunnel
wing shape and were found to cause deviations in the sec-
tionalaerodynamicloadsifnotproperlymodeled.Theeffects
were observed to be approximately proportional to the wing’s
elastic twist. With the initial derivative distributions being
derived from three-dimensional vortex lattice method cal-
culations of the rigid aircraft shape only, these effects are
not accounted for and thus add to the uncertainty of the
results. However, considering the moderate magnitudes of
elastic twist experienced during the maneuvers and the plau-
sible load distributions found from the evaluation of shear
forces in Fig.11, this uncertainty is considered small. If more
aggressive maneuvers or gust encounters with larger elastic
deformations and increased elastic mode participation are
123

## Page 15

Nonlinear system identiﬁcation of a UAV model...
675
Fig. 11 Identiﬁcation result for
longitudinal/lateral maneuvers
with measured shear forces on
the wing, measurement (
),
simulation (
), and maneuver
separation (
)
-80
-40
0
Qz,LMS3
(N)
-200
-100
0
Qz,LMS5
(N)
-200
-100
0
Qz,LMS6
(N)
0
20
40
60
80
100
120
Time [s]
-80
-40
0
Qz,LMS8
(N)
to be investigated in the future, the inﬂuence of the three-
dimensional effects on the induced angle of attack is expected
to increase. In this case, even unsteady aerodynamic effects
can become important for slightly ﬂexible aircraft as repre-
sented by the G-Flights Dimona [13].
Based on these results, the identiﬁed model is capable
of computing realistic distributed aerodynamic forces and
moments and thus is well suited for state of the art model-
based load estimation techniques [36]. This aspect combined
with the simple model structure also provides a suitable basis
for real-time simulation and the design of active load control
laws.
5 Conclusion
A control-oriented modeling framework for slightly ﬂexible
aircraft suitable for parameter identiﬁcation in the time-
domain was presented. It combines linear structural dynam-
ics and a distributed quasi-steady aerodynamics model using
strip theory. The applicability of the modeling framework
was demonstrated for a slightly ﬂexible 25kg ﬁxed-wing
UAV. Free vibration modes and mode shapes of the structure
were obtained from ground vibration tests. Initial distribu-
tions for the stability and control derivatives of the strip
aerodynamics were derived from three-dimensional vortex-
lattice-method steady-ﬂow calculations. They were subse-
quentlyadaptedbasedonﬂighttestdatausingtheoutputerror
method in the time-domain and maximum-likelihood esti-
mation. The use of scaling parameters for adapting the initial
distributions is demonstrated to be an efﬁcient approach for
achieving a limited number of estimation parameters. A good
overall identiﬁcation result and close match of the fast air-
craft dynamics was achieved. Good agreement with the initial
derivative distributions was found for the lift curve slope and
angle of sideslip-dependent stability derivative distributions,
while viscous drag effects were signiﬁcantly underestimated
by the vortex-lattice-method calculations. Further, the eval-
uation of the structural load distribution measured along the
wing demonstrated the capability of the model to compute
realistic distributed aerodynamic forces and moments. The
resultant computationally efﬁcient model provides a suit-
able basis for real-time simulation, loads’ estimation, and
active load control law design. The latter highly beneﬁt
from the capability of the strip aerodynamic model struc-
ture to yield distributed forces and moments. Possible future
workincludes theimprovement of thederivativedistributions
based on high-ﬁdelity numerical or experimental data.
Acknowledgements The authors would like to acknowledge Lothar
Desel and Rasmus Köhler for their support during the ﬂight test cam-
paign. Special thanks is further devoted to Karsten Henning for his
contribution to this work. Parts of this work have been presented previ-
ously at the 6th CEAS Conference on Guidance, Navigation and Control
(EuroGNC) [39].
Funding Open Access funding enabled and organized by Projekt
DEAL. This work was funded by the research project “Advanced load
analysis and observer methods for innovative aircraft conﬁgurations”
(ELASTIK), which is supported by the German Federal Ministry for
EconomicAffairsandClimateActioninthenationalLuFoV-3program.
Any opinions, ﬁndings, and conclusions expressed in this document are
those of the authors and do not necessarily reﬂect the views of the other
project partners.
Availability of data and materials Not applicable.
Declarations
Conﬂict of interest The authors have no competing interests to declare
that are relevant to the content of this article.
Ethics approval Not applicable.
Consent to participate Not applicable.
Consent for publication Not applicable.
Code availability Not applicable.
Open Access This article is licensed under a Creative Commons
Attribution 4.0 International License, which permits use, sharing, adap-
tation, distribution and reproduction in any medium or format, as
long as you give appropriate credit to the original author(s) and the
source, provide a link to the Creative Commons licence, and indi-
cate if changes were made. The images or other third party material
in this article are included in the article’s Creative Commons licence,
unless indicated otherwise in a credit line to the material. If material
is not included in the article’s Creative Commons licence and your
intended use is not permitted by statutory regulation or exceeds the
permitteduse,youwillneedtoobtainpermissiondirectlyfromthecopy-
123

## Page 16

676
B. Herrmann et al.
right holder. To view a copy of this licence, visit http://creativecomm
ons.org/licenses/by/4.0/.
References
1. Livne, E.: Future of airplane aeroelasticity. J. Aircraft 40(6), 1066–
1092 (2003). https://doi.org/10.2514/2.7218
2. Waszak, M.R., Davidson, J.B., Schmidt, D.K.: A simulation study
of the ﬂight dynamics of elastic aircraft. Technical Report NASA
CR 4102 Vols. 1 and 2, NASA (1987)
3. Kubica, F.: New ﬂight control laws for large capacity aircraft exper-
imentation of Airbus A340. In: ICAS, Congress, 21st, Melbourne,
Australia (1998)
4. Tuzcu, I., Meirovitch, L.: Effects of ﬂexibility on the stability of
ﬂying aircraft. J. Dyn. Syst. Meas. Contr. 127(1), 41–49 (2004).
https://doi.org/10.1115/1.1870040
5. Jategaonkar, R., Fischenberg, D., von Gruenhagen, W.: Aerody-
namic modeling and system identiﬁcation from ﬂight data-recent
applications at DLR 41(4), 681–691 (2004). https://doi.org/10.
2514/1.3165
6. Waszak, M.R., Schmidt, D.K.: Flight dynamics of aeroelastic vehi-
cles 25(6), 563–571 (1988). https://doi.org/10.2514/3.45623
7. Schmidt, D.K., Raney, D.L.: Modeling and simulation of ﬂexi-
ble ﬂight vehicles. J. Guid. Control. Dyn. 24(3), 539–546 (2001).
https://doi.org/10.2514/2.4744
8. Pete, K., Smith, S., Vicroy, D.: Model validation for wake-
vortex/aircraft encounters. In: AIAA Atmospheric Flight Mechan-
ics Conference. American Institute of Aeronautics and Astro-
nautics, Denver, Colorado (2000). https://doi.org/10.2514/6.2000-
3979
9. De Bruin, A.: S-wake assessment of wake vortex safety. National
Aerospace Laboratory NLR (2003)
10. Fischenberg, D.: A method to validate wake vortex encounter mod-
els from ﬂight test data. In: 27th International Congress of the
Aeronautical Sciences (2010). International Council of the Aero-
nautical Sciences Nice, France
11. Selig, M.: Modeling full-envelope aerodynamics of small UAVs
in realtime. In: AIAA Atmospheric Flight Mechanics Confer-
ence. American Institute of Aeronautics and Astronautics, Toronto,
Ontario, Canada (2010). https://doi.org/10.2514/6.2010-7635
12. Silvestre, F., Paglione, P.: Dynamics and control of a ﬂexible air-
craft. In: AIAA Atmospheric Flight Mechanics Conference and
Exhibit. American Institute of Aeronautics and Astronautics, Hon-
olulu, Hawaii (2008). https://doi.org/10.2514/6.2008-6876
13. Silvestre, F.J., Luckner, R.: Experimental validation of a ﬂight
simulation model for slightly ﬂexible aircraft 53(12), 3620–3636
(2015). https://doi.org/10.2514/1.j054023
14. Andrews, S.: Modelling and simulation of ﬂexible aircraft : han-
dling qualities with active load control. PhD thesis (2011)
15. Yates, E.C.: Modiﬁed-strip-analysis method for predicting wing
ﬂutter at subsonic to hypersonic speeds. J. Aircr. 3(1), 25–29
(1966). https://doi.org/10.2514/3.43702
16. Weissinger, J.: The lift distribution of swept-back wings. Technical
Report NACA-TN-1120, National Advisory Committee for Aero-
nautics (1947)
17. Wagner, H.: Über die Entstehung des dynamischen Auftriebes
von Tragﬂügeln. ZAMM - Zeitschrift für Angewandte Mathematik
und Mechanik 5(1), 17–35 (1925). https://doi.org/10.1002/zamm.
19250050103
18. Leishman, J.G.: Unsteady lift of a ﬂapped airfoil by indicial con-
cepts. J. Aircr. 31(2), 288–297 (1994). https://doi.org/10.2514/3.
46486
19. de Oliveira Silva, B.G.: Data gathering and preliminary results of
the system identiﬁcation of a ﬂexible aircraft model. In: AIAA
Atmospheric Flight Mechanics Conference. American Institute of
Aeronautics and Astronautics, Portland, Oregon (2011). https://
doi.org/10.2514/6.2011-6355
20. de Oliveira Silva, B.G., Moennich, W.: System identiﬁcation of
ﬂexible aircraft in time domain. In: AIAA Atmospheric Flight
Mechanics Conference. American Institute of Aeronautics and
Astronautics, Minneapolis, Minnesota (2012). https://doi.org/10.
2514/6.2012-4412
21. Garrec, C.L., Kubica, F.: In-ﬂight structural modes identiﬁca-
tion for comfort improvement by ﬂight control laws 42(1), 90–92
(2005). https://doi.org/10.2514/1.3733
22. Niemann, C., Montel, M., Thielecke, F.: Development of an air data
system for an unmanned research aircraft. In: Deutscher Luft-und
Raumfahrtkongress (2014)
23. Henning, K., Montel, M., Thielecke, F.: Experimentelle Ermit-
tlung der modalen Strukturparameter eines skalierten Flugver-
suchstraegers mittels Low-Cost Sensoren. In: Deutscher Luft- und
Raumfahrtkongress DLRK, Muenchen, Germany (2017)
24. Krings, M., Henning, K., Thielecke, F.: Flight test oriented autopi-
lot design for improved aerodynamic parameter identiﬁcation. In:
Advances in Aerospace Guidance. Navigation and Control, pp.
265–276. Springer, Berlin (2013)
25. Krings, M., Annighoefer, B., Thielecke, F.: Ultra - unmanned low-
cost testing research aircraft. In: American Control Conference
ACC (2013)
26. Jategaonkar, R.: Flight Vehicle System Identiﬁcation?: a Time
Domain Methodology. American Institute of Aeronautics and
Astronautics, Reston, Virginia (2006)
27. Keyes, S.A., Seiler, P., Schmidt, D.K.: Newtonian development of
the mean-axis reference frame for ﬂexible aircraft. J. Aircr. 56(1),
392–397 (2019). https://doi.org/10.2514/1.c035041
28. Milne, R.D.: Dynamics of the deformable aeroplane. Technical
report, Aeronautical Research Council London (United Kingdom)
(1964)
29. Canavin, J.R., Likins, P.W.: Floating reference frames for ﬂexible
spacecraft. J. Spacecr. Rocket. 14(12), 724–732 (1977). https://doi.
org/10.2514/3.57256
30. Schlichting, H., Truckenbrodt, E.: Aerodynamik des Flugzeuges:
Zweiter Band. Springer, Berlin (1960). https://doi.org/10.1007/
978-3-642-53046-3
31. Brockhaus, R., Alles, W., Luckner, R.: Flugregelung. Springer,
Berlin (2011). https://doi.org/10.1007/978-3-642-01443-7
32. Theil, H.: Economic Forecasts and Policy, 2nd edn. Contributions
to economic analysis. North-Holland Publishing Company, Ams-
terdam (1975)
33. Leuthold, R.M.: On the use of theil’s inequality coefﬁcients.
Am. J. Agr. Econ. 57(2), 344–346 (1975). https://doi.org/10.2307/
1238512
34. Murray-Smith, D.J.: Methods for the external validation of
contiuous system simulation models:a review. Math. Comput.
Model. Dyn. Syst. 4(1), 5–31 (1998). https://doi.org/10.1080/
13873959808837066
35. Grauer, J.A., Boucher, M.J.: Output measurement equations for
ﬂexible aircraft ﬂight dynamics. Technical Report No. NASA/TM-
2018-220102, NASA STI Program Ofﬁce (2018)
36. Montel, M., Thielecke, F.: Efﬁcient and accurate technology for air-
craft loads estimation. CEAS Aeronaut. J. 11(2), 461–474 (2019).
https://doi.org/10.1007/s13272-019-00423-z
37. Luderer, O., Thielecke, F.: Validation of a hybrid loads observer
for a subscale test aircraft with distributed electric propulsion. In:
33rd Congress of the International Council of the Aeronautical
Sciences, ICAS 2022, Stockholm, Sweden (2022). International
Council of the Aeronautical Sciences (ICAS). http://hdl.handle.
net/11420/14391
38. Barriety, B., Boin, J.-P., Chandre-Vila, O., Mauermann, T.: Fast
ﬂuid-structure computational method taking into account non-
123

## Page 17

Nonlinear system identiﬁcation of a UAV model...
677
linear aerodynamic. In: International Forum on Aeroelasticity and
Structural Dynamics (IFASD) (2019)
39. Herrmann, B., Theis, J., Thielecke, F.: System Identiﬁcation of a
Nonlinear UAV Model with Distributed Aerodynamics and Flex-
ible Structure. In: 6th Conference on Guidance, Navigation and
Control CEAS (2022)
Publisher’s Note Springer Nature remains neutral with regard to juris-
dictional claims in published maps and institutional afﬁliations.
123
