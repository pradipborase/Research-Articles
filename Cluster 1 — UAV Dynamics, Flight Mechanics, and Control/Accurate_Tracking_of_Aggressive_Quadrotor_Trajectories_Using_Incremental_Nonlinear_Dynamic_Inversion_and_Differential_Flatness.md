# Accurate_Tracking_of_Aggressive_Quadrotor_Trajectories_Using_Incremental_Nonlinear_Dynamic_Inversion_and_Differential_Flatness.pdf

## Page 1

IEEE TRANSACTIONS ON CONTROL SYSTEMS TECHNOLOGY, VOL. 29, NO. 3, MAY 2021
1203
Accurate Tracking of Aggressive Quadrotor
Trajectories Using Incremental Nonlinear
Dynamic Inversion and Differential Flatness
Ezra Tal
, Graduate Student Member, IEEE, and Sertac Karaman
, Member, IEEE
Abstract—Autonomous unmanned aerial vehicles (UAVs) that
can execute aggressive (i.e., high-speed and high-acceleration)
maneuvers have attracted signiﬁcant attention in the past few
years. This article focuses on accurate tracking of aggressive
quadcopter trajectories. We propose a novel control law for
tracking of position and yaw angle and their derivatives of up
to fourth order, speciﬁcally velocity, acceleration, jerk, and snap
along with yaw rate and yaw acceleration. Jerk and snap are
tracked using feedforward inputs for angular rate and angular
acceleration based on the differential ﬂatness of the quadcopter
dynamics. Snap tracking requires direct control of body torque,
which we achieve using closed-loop motor speed control based
on measurements from optical encoders attached to the motors.
The controller utilizes incremental nonlinear dynamic inversion
(INDI) for robust tracking of linear and angular accelerations
despite external disturbances, such as aerodynamic drag forces.
Hence, prior modeling of aerodynamic effects is not required. We
rigorously analyze the proposed control law through response
analysis and demonstrate it in experiments. The controller
enables a quadcopter UAV to track complex 3-D trajectories,
reaching speeds up to 12.9 m/s and accelerations up to 2.1 g, while
keeping the root-mean-square tracking error down to 6.6 cm, in a
ﬂight volume that is roughly 18 m × 7 m and 3-m tall. We also
demonstrate the robustness of the controller by attaching a drag
plate to the UAV in ﬂight tests and by pulling on the UAV with
a rope during hover.
Index Terms—Aggressive maneuvering, differential ﬂatness,
drone racing, ﬂight control, incremental control, nonlinear
dynamic inversion (NDI), quadcopter, robust control, trajectory
following.
NOMENCLATURE
◦
Hamilton quaternion product.
•◦n
nth Hadamard (element-wise) power.
[•]×
Cross-product matrix.
Manuscript received February 25, 2020; accepted May 9, 2020. Date of
publication June 19, 2020; date of current version April 12, 2021. Manuscript
received in ﬁnal form June 6, 2020. This work was supported in part by the
Ofﬁce of Naval Research (ONR) under Grant N00014-17-1-2670. This article
was presented at the 57th IEEE Conference on Decision and Control (CDC)
2018 [1]. Recommended by Associate Editor A. Serrani. (Corresponding
author: Ezra Tal.)
The authors are with the Department of Aeronautics and Astronautics,
Massachusetts Institute of Technology (MIT), Cambridge, MA 02139 USA,
and also with the Laboratory for Information and Decision Systems, Massa-
chusetts Institute of Technology (MIT), Cambridge, MA 02139 USA (e-mail:
eatal@mit.edu; sertac@mit.edu).
This
article
has
supplementary
downloadable
material
available
at
https://ieeexplore.ieee.org, provided by the authors.
Color versions of one or more of the ﬁgures in this article are available
online at https://ieeexplore.ieee.org.
Digital Object Identiﬁer 10.1109/TCST.2020.3001117
a
Linear acceleration in inertial frame, m/s2.
ab
Linear acceleration including gravitational
acceleration
in
body-ﬁxed
frame,
i.e.,
as measured by IMU, m/s2.
bx, by, bz
basis vectors of body-ﬁxed frame.
Cn
nth order differentiability class.
fext
External disturbance force vector in inertial
frame, N.
g
Gravitational acceleration, m/s2.
G1
Propeller speed control effectiveness matrix.
G2
Propeller acceleration control effectiveness
matrix.
H(s)
Low-pass ﬁlter transfer function.
ix, iy, and iz
Standard basis vectors.
j
Jerk in inertial frame, m/s3.
J
Vehicle moment of inertia matrix, kg·m2.
Jyy
Vehicle moment of inertia around by-axis,
kg·m2.
Jrz
Motor rotor and propeller moment of inertia,
kg·m2.
kθ and kq
Scalar control gains.
kG
Linearized
pitch
control
effectiveness,
kg·m2/(rad·s).
kμz
Propeller torque coefﬁcient, kg·m2/rad2.
kτ
Propeller thrust coefﬁcient, kg·m/rad2.
Kx, Kv,
Diagonal control gain matrices.
Ka, Kξ
K and KIω
lx
Moment
arm
component
parallel
to
bx-axis, m.
ly
Moment
arm
component
parallel
to
by-axis, m.
m
Vehicle mass, kg.
M(s)
Motor
(control)
dynamics
transfer
function.
N I
Transfer function corresponding to nonincre-
mental controller.
p
Polynomial relating motor speeds to throttle
inputs.
q
Vehicle pitch rate around by-axis, rad/s.
rυ
Yaw direction vector in inertial frame.
R
Body-ﬁxed
to
inertial
frame
rotation
matrix.
s
Laplace variable.
1063-6536 © 2020 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:47:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 2

1204
IEEE TRANSACTIONS ON CONTROL SYSTEMS TECHNOLOGY, VOL. 29, NO. 3, MAY 2021
s
Snap in inertial frame, m/s4.
S
Angular rate to yaw rate transformation.
SO(3)
3-D special orthogonal group.
t
Time, s.
T
Thrust, N.
T
Circle group.
v
Velocity in inertial frame, m/s.
x
Position in inertial frame, m.
α
Vehicle
pitch
acceleration
around
by-axis, rad/s2.

Modeling error parameter.
ζ
Throttle command vector.
θ
Vehicle pitch angle, rad.
μ
Control moment vector, N·m.
μext
External disturbance moment vector,
N·m.
ξ
Normed quaternion attitude vector.
ξw, ξ x, ξ y, and ξ z
Elements of ξ.
ξ c
Incremental command relative to cur-
rent attitude.
ξ e
Vector of error angles in body-ﬁxed
frame.
σ ref(t)
Reference trajectory function, m, rad.
τ
Speciﬁc thrust, m/s2.
τm
Motor dynamics time constant, s.
υ
Vehicle yaw angle, rad.
ω
Deviation from hover state motor rota-
tion speed, rad/s.
ω0
Hover state motor rotation speed, rad/s.
ω
Vector of four motor rotation speeds,
rad/s.

Vehicle angular velocity in body-ﬁxed
frame, rad/s.
I. INTRODUCTION
H
IGH-SPEED aerial navigation through complex environ-
ments has been a focus of control theory and robotics
research for decades. More recently, drone racing, in which
remotely operated rotary-wing aircraft are piloted through
challenging, obstacle-rich courses at very high speeds, has
further inspired and popularized this research direction. Devel-
opment of fully autonomous drone racers requires accurate
control of aircraft during aggressive, i.e., high speed and agile,
maneuvers. At high speeds, aerodynamic drag, which is hard
to model, becomes a dominant factor. This poses an important
challenge in control design. In addition, accurate tracking of a
reference trajectory with fast-changing acceleration requires
considering its higher order time derivatives, i.e., jerk and
snap. In contrast, control design for rotary-wing, vertical
take-off and landing (VTOL) aircraft at low speeds typically
neglects both aerodynamics and higher order derivatives.
In this article, we propose a novel control design for
accurate tracking of aggressive trajectories using a quad-
copter aircraft, such as the one shown in Fig. 1. The pro-
posed controller generates feedforward control inputs based
on differential ﬂatness of the quadcopter dynamics and uses
incremental nonlinear dynamic inversion (INDI) to handle
external disturbances, such as aerodynamic drag.
Fig. 1.
Quadrotor with body-ﬁxed reference system and moment arm
deﬁnitions.
Nonlinear dynamic inversion (NDI), also called feedback
linearization, enables the use of a linear control law by
transforming the nonlinear dynamics into a linear input–output
map [2]–[4]. Although variants of NDI were quickly developed
for ﬂight control [5]–[9], it is well known that exact dynamic
inversion inherently suffers from lack of robustness [10]. As a
result, other nonlinear control methods, e.g., adaptive sliding
mode [10]–[12] and backstepping designs [13], have been con-
sidered in order to achieve robustness in ﬂight control. More
recently, an incremental version of NDI has been developed
[14], [15] based on earlier derivations [16], [17], which provide
robustness by incrementally applying control inputs based on
inertial measurements. In the existing literature, the INDI
technique has been applied to quadcopters for stabilization,
e.g., for robust hovering [18], [19], but not for trajectory
tracking.
Differential ﬂatness, or feedback linearizability, of a dynam-
ics system allows expressing all state and input variables in
terms of a set of ﬂat outputs and its derivatives [20]–[24]. In
the context of ﬂight control, this property enables reformu-
lation of the trajectory tracking problem as a state tracking
problem [9], [25]. Speciﬁcally, it enables consideration of
higher order derivatives of the reference trajectory through
feedforward state and input references, which has also been
applied to control [26]–[29].
Quadcopter aircraft are relatively easy to maneuver and
experiment with. Arguably, these qualities make them ideal
for drone racing events. For the same reasons, they have been
heavily used as experimental platforms in robotics and control
theory research since the start of this century [30]–[33]. Com-
plex trajectory tracking control systems have been designed
and demonstrated for aircraft in motion capture rooms, where
the position and the orientation of the aircraft can be obtained
with high accuracy [34]–[40]. Agile maneuvers for quadcopter
aircraft have also been demonstrated [41], [42]. Despite being
impressive, these demonstrations have showcased complex
trajectories only at relatively slow speeds, e.g., less than 2 m/s,
so that aerodynamic forces and moments may be neglected.
At higher speeds, aerodynamic effects heavily inﬂuence the
vehicle dynamics. This has been addressed in recent research
through modeling [29], [43], [44], estimation [45], [46], and
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:47:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 3

TAL AND KARAMAN: ACCURATE TRACKING OF AGGRESSIVE QUADROTOR TRAJECTORIES
1205
learning [47] of aerodynamic drag effects toward tracking
control in high-speed ﬂight.
The main contribution of this article is a trajectory
tracking control design that achieves accurate tracking dur-
ing high-speed and high-acceleration maneuvers without
depending on modeling or estimation of aerodynamic drag
parameters. The design exploits differential ﬂatness of the
quadcopter dynamics to generate feedforward control terms
based on the reference trajectory and its derivatives up to
fourth order, i.e., velocity, acceleration, jerk, and snap. Model-
ing inaccuracies and disturbances due to aerodynamic drag are
compensated for using incremental control based on the INDI
technique. This control design is novel in the following ways.
First, the design incorporates direct tracking of reference snap
through accurate control of the motor speeds using optical
encoders attached to each motor. We recognize that snap is
directly related to vehicle angular acceleration and thus to the
control torque acting on the quadcopter. Accurate application
of torque commands is achieved by precise closed-loop control
of the motor speeds using measurements from the optical
encoders. To the best of our knowledge, the direct control over
snap using motor speed measurements is novel. In contrast,
trajectory tracking control based on body rate inputs, e.g.,
using a typical inner-loop ﬂight controller, is incapable of
truly considering reference snap. Second, we develop a novel
INDI control design for quadcopter trajectory tracking. Thrust
and torque commands are applied incrementally for robustness
against signiﬁcant external disturbances, such as aerodynamic
drag, without the need to model or estimate said disturbances.
As far as we are aware, the proposed controller is the ﬁrst
design that is tailored for trajectory tracking, as existing
INDI ﬂight control designs focus on state regulation, e.g., for
maintaining hover under external disturbances. Third, we pro-
vide and evaluate a novel implementation of INDI angular
acceleration control that includes nonlinear computation of the
control increments, as opposed to the existing implementations
that use inversion of linearized control effectiveness equations.
Finally, we demonstrate the proposed controller in experiments
and rigorously analyze the beneﬁts of the key aspects of our
control design through response analysis. In our experiments,
the proposed control law enables an unmanned aerial vehi-
cle (UAV) to track complex 3-D trajectories, reaching speeds
up to 12.9 m/s and accelerations up to 2.1 g, while keeping
the root-mean-square (rms) tracking error down to 6.6 cm,
in a ﬂight volume that is roughly 18 m long, 7 m wide, and
3 m tall. We also demonstrate the robustness of the controller
by attaching a drag plate to the UAV in ﬂight tests and by
pulling on the UAV using a tensioned wire during hover. The
improved performance due to the tracking of reference jerk
and snap through feedforward angular velocity and angular
acceleration inputs is also demonstrated both in theoretical
analysis and in experiments.
A preliminary version of this article was previously pre-
sented at the 57th IEEE Conference on Decision and Control
(CDC 2018) [1]. The signiﬁcant extensions introduced in
this article include a reformulation of the controller using
quaternion attitude representation, a more elaborate description
of its architecture, the response analysis in its entirety, and new
experimental results at increased speeds. The application of the
singularity-free quaternion representation enables tracking of
very aggressive trajectories that would incur singular states if
an Euler angle representation were used.
This article
is
structured as
follows. In
Section
II,
the quadrotor model is speciﬁed, and we show how differential
ﬂatness is used to formulate feedforward control inputs in
terms of the reference trajectory. In Section III, we describe
the architecture of the trajectory tracking controller and its
individual components. Analysis in Section IV illustrates the
robustness of INDI and the effect of the feedforward control
inputs through response modeling. Finally, we give experimen-
tal results from real-life ﬂights in Section V.
II. PRELIMINARIES
In this section, we describe the quadrotor dynamics model
and its differential ﬂatness property. Speciﬁcally, we show how
the control system utilizes this property to track the reference
trajectory jerk and snap through feedforward angular rate and
angular acceleration inputs.
A. Quadrotor Model
We consider a six-degree-of-freedom (DOF) quadrotor,
as shown in Fig. 1. The unit vectors shown in the ﬁgure are
the basis of the body-ﬁxed reference frame and form the
rotation matrix R = [bx by bz] ∈SO(3), which gives
the transformation from the body-ﬁxed reference frame to
the inertial reference frame. The basis of the north-east-down
(NED) inertial reference frame consists of the columns of the
identity matrix [ix iy iz].
The vehicle translational dynamics are given by
˙x = v
(1)
˙v = giz + τbz + m−1fext
(2)
where x and v are the position and velocity in the inertial
reference frame, respectively. Equation (2) includes three
contributions to the linear acceleration. First, the gravita-
tional acceleration g is in the downward direction. Second,
the speciﬁc thrust τ is the ratio of the total thrust T and
the vehicle mass m. Note that the thrust vector is always
aligned with the bz-axis so that the quadrotor must pitch
or roll to accelerate forward, backward, or sideways. Finally,
the external disturbance force vector fext accounts for all other
forces acting on the vehicle, such as aerodynamic drag.
The rotational dynamics are given by
˙ξ = 1
2ξ ◦
(3)
˙ = J−1(μ + μext − × J)
(4)
where  is the angular velocity in the body-ﬁxed reference
frame and ξ = [ξw ξ x ξ y ξ z]T is the normed quaternion
attitude vector so that Rx = ξ ◦x ◦ξ−1 with ◦the Hamil-
ton product. Note that a zero magnitude element is implied
when multiplying three-element vectors with quaternions. The
matrix J is the vehicle moment of inertia tensor. The control
moment vector is indicated by μ, and the external disturbance
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:47:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 4

1206
IEEE TRANSACTIONS ON CONTROL SYSTEMS TECHNOLOGY, VOL. 29, NO. 3, MAY 2021
moment vector is indicated by μext. The third term of (4)
accounts for the conservation of angular momentum.
Each propeller axis is assumed to be aligned perfectly with
the bz-axis so that all motor speeds are described by the
four-element vector ω > 0. The total thrust T and control
moment vector in body-reference frame μ are given by
 μ
T

= G1ω◦2 + G2 ˙ω
(5)
where ◦indicates the Hadamard power
G1 =
⎡
⎢⎢⎣
lykτ
−lykτ
−lykτ
lykτ
lxkτ
lxkτ
−lxkτ
−lxkτ
−kμz
kμz
−kμz
kμz
−kτ
−kτ
−kτ
−kτ
⎤
⎥⎥⎦
(6)
with lx and ly the moment arms shown in Fig. 1, kτ the
propeller thrust coefﬁcient, and kμz the propeller torque coef-
ﬁcient, and
G2 =
⎡
⎢⎢⎣
0
0
0
0
0
0
0
0
−Jrz
Jrz
−Jrz
Jrz
0
0
0
0
⎤
⎥⎥⎦
(7)
with Jrz the rotor and propeller moment of inertia. The second
term in (5) represents the control torque directly due to
motor torques. Due to their relatively small moment of inertia,
the contribution of the motors to the total vehicle angular
momentum may be neglected.
B. Differential Flatness
The controller aims to accurately track the reference trajec-
tory deﬁned by the following function:
σ ref(t) = [xref(t)T υref(t)]T
(8)
which
consists
of
four
differentially
ﬂat
outputs,
i.e.,
the quadrotor position in the inertial reference frame xref(t) ∈
R3, and the vehicle yaw angle υref(t) ∈T, where T denotes
the circle group. From this time, we do not explicitly write
the time argument t everywhere.
For (8) to be dynamically feasible, it is required that xref is
of differentiability class C4, i.e., its ﬁrst four derivatives exist
and are continuous, and that υref is of class C2. The temporal
derivatives of xref are successively the reference velocity vref,
the reference acceleration aref, the reference jerk jref, and the
reference snap sref, all in the inertial reference frame. Similarly,
temporal differentiation of υref gives the yaw rate ˙υref and the
yaw acceleration ¨υref.
The quadcopter dynamics are differentially ﬂat so that we
can express its states and inputs as a function of σ ref(t) and
its derivatives. This enables reformulation of the trajectory
tracking problem as a state tracking problem. In this section,
we derive expressions for the angular rate reference ref and
the angular acceleration reference ˙ref in terms of trajectory
jerk, snap, yaw rate, and yaw acceleration. These reference
states will be applied as feedforward inputs in the trajectory
tracking control design.
Taking the derivative of (2) yields the following expression
for jerk:
j = τR
iz
T
× + ˙τbz
(9)
where [•]× indicates the cross-product matrix, and variations
in the unmodeled external force fext are neglected. This
external force consists chieﬂy of body drag and rotor drag
[48], [49]. Both contributions can be included in the differen-
tial ﬂatness transform [29], but the resulting controller will
depend on a vehicle-speciﬁc aerodynamics model. Instead,
we forgo modeling of the external force and use sensor-based
control to directly compensate for it. Therefore, our controller
is able to handle external disturbances without depending on
a vehicle-speciﬁc model, as described in Section III.
By taking the derivative once more, the following expression
for snap is found:
s = R

¨τiz + (2 ˙τ + τ[]×)

iz
T
× + τ

iz
T
× ˙

.
(10)
According to typical aerospace convention, we deﬁne yaw as
the angle between ix and the vector
rυ = 
 b1
x
b2
x
0 T
(11)
with superscripts indicating individual elements of bx. Taking
the derivative of (11) using ˙R = R[]×, we obtain the
following expression for the yaw rate:
˙υ = rυ × ˙rυ
rT
υrυ
=

 −b2
x b1
x

rT
υrυ
 0
−b1
z
b1
y
0
−b2
z
b2
y




S
 = S
(12)
and, by the product rule, the following expression for the yaw
acceleration:
¨υ = S ˙ + ˙S.
(13)
An expression for the derivative ˙S is omitted here for brevity,
but it can be obtained by applying the product rule to the
expression for S given in (12). From (9) and (12), we obtain
the angular rate reference
 ref
˙τref

=
 τR[iz]T
×
bz
S
0
−1 jref
˙υref

(14)
and from (10) and (13), the angular acceleration reference
 ˙ref
¨τref

=
 τR[iz]T
×
bz
S 0
−1
 sref
¨υref

−
 R(2 ˙τ + τ[]×)[iz]T
×
˙S

.
(15)
Note that these expressions also contain reference signals for
the ﬁrst and second derivatives of speciﬁc thrust. However,
as we are unable to command the corresponding ﬁrst and sec-
ond derivatives of the motor speed, these references remain
unused by the controller.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:47:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 5

TAL AND KARAMAN: ACCURATE TRACKING OF AGGRESSIVE QUADROTOR TRAJECTORIES
1207
TABLE I
OVERVIEW OF TRAJECTORY TRACKING CONTROLLER COMPONENTS
Fig. 2.
Position and velocity control. The blue area contains the PD control design, as described in Section III-A.
Fig. 3.
Acceleration and attitude control. The blue area contains the INDI linear acceleration and yaw control, as described in Section III-B. The green
area contains the computation of angular rate and angular acceleration references based on differential ﬂatness, as described in Section II-B. The red area
contains the attitude and angular rate control, as described in Section III-C. The yellow area contains the INDI angular acceleration control, as described in
Section III-D.
III. TRAJECTORY TRACKING CONTROL
The control design consists of several components based
on various control methods. Table I gives an overview of
the components with their respective methodology, references,
and control outputs. The control architecture is visualized in
three block diagrams. Fig. 2 shows the outer-loop position
and velocity controller, as described in Section III-A. The
intermediate control loop shown in Fig. 3 controls linear accel-
eration, attitude and angular rate, and angular acceleration,
as described in Sections III-B–III-D, respectively. Finally,
vehicle moment and thrust are directly controlled through
closed-loop motor speed control in the inner loop, as shown
in Fig. 4 and described in Section III-E.
The controller utilizes a vehicle state estimate consisting
of position, velocity, and attitude. In addition, motor speed
measurements are obtained from optical encoders, and linear
acceleration and angular rate measurements are obtained from
the inertial measurement unit (IMU). For the application of
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:47:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 6

1208
IEEE TRANSACTIONS ON CONTROL SYSTEMS TECHNOLOGY, VOL. 29, NO. 3, MAY 2021
Fig. 4.
Motor control and computation of ﬁltered signals. The blue and green areas contain the moment and thrust control (including motor speed command
saturation resolution), and the motor speed control, respectively. Both are described in Section III-E. The UAV block represents the UAV hardware, including
ESCs, motors, and sensors. The red area contains the computation of ﬁltered signals based on IMU and optical encoder measurements.
incremental angular acceleration control, angular acceleration
measurements are obtained by numerical differentiation of the
measured angular rate. A low-pass ﬁlter (LPF) is required
to alleviate the effects of noise, e.g., airframe vibrations,
on measurements obtained directly from the IMU. We denote
the LPF outputs using the subscript f , e.g., by  f and ˙ f
for the angular rate output and its derivative, respectively.
The gravity-corrected LPF acceleration output in the inertial
reference frame is obtained as follows:
a f = (Rab + giz) f .
(16)
A. PD Position and Velocity Control
Position and velocity control is based on two cascaded
proportional–derivative (PD) controllers. The resulting con-
troller is mathematically equivalent to the following single
expression:
ac = Kx(xref −x) + Kv(vref −v) + Ka

aref −a f

+ aref
(17)
with K• indicating diagonal gain matrices. The subscript ref is
used to indicate the values obtained directly from the reference
trajectory. In contrast, the subscript c indicates the commanded
values that are computed in one of the control loops. For
example, aref is obtained directly from the reference trajectory
as the second derivative of xref, while ac is computed based on
(17) and includes terms based on the position, velocity, and
acceleration deviations. The ﬁrst three terms in (17) ensure
tracking of position and velocity references, whereas the ﬁnal
term serves as a feedforward input to ensure tracking of
the reference acceleration. The control utilizes the inertial
reference frame with—in our implementation—identical gains
for the horizontal ix- and iy-directions, but separately tuned
gains for the vertical iz-direction. The commanded acceleration
is used to calculate thrust and attitude commands, as will be
shown in Section III-B.
B. INDI Linear Acceleration and Yaw Control
Existing literature presents the derivation of an INDI linear
acceleration controller using the Taylor series approxima-
tion [19]. In this section, we arrive at equivalent control
equations through an intuitive derivation that follows the
practical working of the INDI notion based on the estimation
of the external force acting on the quadrotor.
An expression for the external force in terms of measured
acceleration and speciﬁc thrust is obtained by rewriting (2) as
follows:
fext = m

a f −(τbz) f −giz

(18)
where τ is the speciﬁc thrust calculated according to (5) using
motor speed measurements. Identical LPFs must be used to
ensure that equal phase lag is incurred by acceleration and
thrust measurements [18]. Note that the speciﬁc thrust vector
and the linear acceleration [see (16)] are both transformed into
the inertial reference frame prior to ﬁltering. This order is
appropriate because the external force in the inertial reference
frame fext is assumed to be slow-changing relative to the
LPF dynamics, as described in Section II-B. Substitution of
(18) into (2) gives the following expression for the current
acceleration:
a = τbz + giz + m−1fext
= τbz + giz + m−1
m

a f −(τbz) f −giz

= τbz −(τbz) f + a f .
(19)
The speciﬁc thrust vector command that results in the com-
manded acceleration prescribed by (17) can be computed using
the following incremental relation based on (19):
(τbz)c = (τbz) f + ac −a f .
(20)
The incremental nature of (20) enables the controller to
achieve the commanded acceleration despite possible distur-
bances or modeling errors. If the commanded value is not
obtained immediately, the thrust and attitude commands will
be incremented further in the subsequent control updates. This
principle eliminates the need for integral action anywhere in
the control design.
The thrust magnitude command is obtained as
Tc = −m∥(τbz)c∥2
(21)
with the negative sign following from the deﬁnition that
thrust is positive in the bz-direction. The incremental attitude
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:47:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 7

TAL AND KARAMAN: ACCURATE TRACKING OF AGGRESSIVE QUADROTOR TRAJECTORIES
1209
command ξc represents the rotation from the current attitude
to the commanded attitude and is obtained in two steps. First,
the minimum rotation to align −bz with the thrust vector
command (τbz)c is obtained. Second, a rotation around bz
is added to satisfy the yaw reference υref. For the ﬁrst step,
we transform the normalized thrust vector command to the
current body-ﬁxed reference frame as follows:
(−bz)b
c = ξ −1 ◦(−bz)c ◦ξ.
(22)
The appropriate rotation to align the current −bz with (τbz)c
is then given by
¯ξc =
 1 −iT
z (−bz)b
c
−iz × (−bz)b
c


(23)
where hat refers to quaternion normalization, i.e., ˆξ
=
(ξ/∥ξ∥2). For the second step, the yaw reference normal vector
is ﬁrst transformed to the intermediate attitude command frame
as follows:
¯nυref = (ξ ◦¯ξc)−1 ◦

 sinυref
−cos υref
0 T ◦(ξ ◦¯ξc).
(24)
Next, we obtain the following rotation that makes bx coincide
with the plane deﬁned by normal vector ¯nυref :
ξ υ =


1
0
0
−
¯n1
υref
¯n2
υref
T
(25)
with superscripts indicating individual elements of ¯nυref.
Equation (25) implicitly selects between tracking of υref and
υref + π rad based on minimizing the magnitude of rotation.
Due to continuity of υref, this does not cause any unwanted
switching, but it does prevent unwanted discontinuities such
as a π rad rotation around bz to maintain yaw tracking when
pitching through ±(π/2) rad. Note that (23) and (25) incur
singularities if iz = (−bz)b
c and ¯n2
υref
= 0, respectively.
However, by computing the attitude command relative to the
current attitude, we move these singularities far away from
the nominal trajectory. Moreover, they are straightforwardly
detected and resolved by selecting any direction of rotation.
Finally, the incremental attitude command is obtained as
ξ c = ¯ξc ◦ξ υ.
(26)
C. PD Attitude and Angular Rate Control
In this section, we describe the attitude and angular rate
controller. This controller speciﬁes the angular rate command
and is thus solely based on angular kinematics. This has two
major advantages compared with incorporating control torque
or motor speeds. First, the attitude controller does not consider
any model-speciﬁc parameters, such as the vehicle inertia
matrix J. Therefore, the control design avoids discrepancies
due to model mismatches and has vehicle-independent gains.
Second, accurate torque control cognizant of the external
moment μext can be performed separately using sensor-based
INDI, as described in Section III-D. This eliminates the need
to incorporate a complicated disturbance model in the attitude
controller, which further improves controller robustness and
simplicity.
The three-element angle vector ξ e associated with the
incremental attitude command ξ c is computed as follows:
ξ e = 2 arccos ξw
c
1 −ξw
c ξw
c

 ξ x
c
ξ y
c
ξ z
c
T .
(27)
Using these error angles, the angular acceleration command is
obtained as
˙c = Kξξ e + K

ref − f

+ ˙ref
(28)
where ref and ˙ref are the angular velocity and angular
acceleration feedforward terms deﬁned in (14) and (15),
respectively. The resulting attitude controller not only tracks
the attitude command but also angular rate and acceleration.
This enables tracking of trajectory jerk and snap, which is
essential for accurate tracking of aggressive trajectories, as will
be shown analytically in Section IV and experimentally in
Section V. In contrast, trajectory tracking control based on
body rate inputs, e.g., using an off-the-shelf ﬂight controller,
is incapable of truly considering reference snap, because snap
corresponds to the vehicle angular acceleration, as shown
in (15).
D. INDI Angular Acceleration Control
Robust tracking of the angular acceleration command ˙c is
achieved through INDI control. We rewrite (4) into the follow-
ing expression for the external moment based on the measured
angular rate, angular acceleration, and control moment:
μext = J ˙ f −μ f +  f × J f
(29)
with μ f the control moment in the body-ﬁxed reference frame,
obtained from the measured motor speeds by (5) and low-pass
ﬁltering. Analogous to the external force in Section III-B,
the external moment μext is assumed slow-changing with
regard to the LPF dynamics. Substitution of (29) into (4) then
gives
˙ = J−1(μ + μext − × J)
= J−1(μ + (J ˙ f −μ f +  f × J f ) − × J)
= ˙ f + J−1(μ −μ f ).
(30)
In (30), it is assumed that the difference between the gyro-
scopic angular momentum term and its ﬁltered counterpart is
sufﬁciently small to be neglected because the term is relatively
slow changing compared with the angular acceleration and
control moment and moreover is second order. By inversion of
the ﬁnal line, we obtain the following incremental expression
for the commanded control moment:
μc = μ f + J
 ˙c −˙ f

.
(31)
E. Inversion-Based Moment and Thrust Control, and
Integrative Motor Speed Control
In Sections III-B and III-D, we have found expressions for
the commanded thrust Tc and control moment μc, respectively.
Tracking of these commands requires control of the motor
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:47:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 8

1210
IEEE TRANSACTIONS ON CONTROL SYSTEMS TECHNOLOGY, VOL. 29, NO. 3, MAY 2021
Fig. 5.
Motor (propeller removed) with optical encoder for rotational speed
measurement. Note the optical encoder lens on the right and the accompanying
reﬂective strip on the motor hub.
speeds, as evidenced by the direct relation given in (5). State-
of-the-art INDI implementations for quadrotors are based on
linearization of this relation and do not accurately model
transient behavior [18], [19]. Our proposed implementation
is based on a nonlinear inversion of the control effectiveness
and explicitly incorporates the motor response time constant;
as such, it provides a more accurate computation of control
inputs.
In order to achieve fast and accurate closed-loop motor
speed control, we employ optical encoders that measure the
motor speeds. The availability of motor speed measurements
furthermore enables accurate calculation of the thrust and
control moment, as required by the INDI controller in (20)
and (31). In practice, the optical encoder, shown in Fig. 5,
measures the motor rotational speed by detecting the passage
of stripes on a reﬂective strip attached to the motor hub.
As such, the optical encoder provides a high-rate, accurate,
lightweight, and unintrusive manner to obtain the motor speed.
The motor speed corresponding to the commanded thrust
and control moment is found by inverting the nonlinear control
effectiveness (5). In order to do so, we estimate the effect of
the motor speed command on the motor speed derivative using
the following ﬁrst-order model:
˙ω = τ −1
m (ωc −ω)
(32)
with τm the motor dynamics time constant. After equating
to the control moment and thrust commands, the resulting
equation
 μc
Tc

= G1ω◦2
c + τ −1
m G2(ωc −ω)
(33)
can be solved numerically, e.g., using Newton’s method. Inver-
sion of this nonlinear control effectiveness relation improves
the accuracy of thrust and control moment tracking when
compared with the linearized inversion that does not consider
the motor transient response as given by (52).
Inversion of (33) may lead to infeasible, i.e., saturated,
motor speed commands. We address this ﬁrst by altering the
control moment around bz. Since the control effectiveness is
relatively much smaller around this axis, this is most likely to
resolve the command saturation. Moreover, it typically least
affects vehicle stability and position tracking since rotation
purely around the bz-axis does not alter the thrust vector.
If ω and ¯ω are, respectively, the minimum and maximum
feasible motor speeds, then the set of bz control momenta—
excluding Jrz contributions—that result in feasible motor speed
commands is
max
kμz
kτ

4kτω2 + Tc ±
μy
c
lx
−μx
c
ly

−kμz
kτ

4kτ ¯ω2 + Tc ±
μy
c
lx
+ μx
c
ly

≤μz
c
≤min
kμz
kτ

4kτ ¯ω2 + Tc ±
μy
c
lx
−μx
c
ly

,
−kμz
kτ

4kτω2 + Tc ±
μy
c
lx
+ μx
c
ly

.
(34)
If this set is nonempty, we set μz
c to equal the boundary closest
to the original moment command. The motor speed command
is then obtained as
ωc =

G−1
1
 μc
Tc
◦1
2
.
(35)
Note that due to Jrz contributions, the actual bz control
moment will not exactly be equal to μz
c. However, we still
obtain the feasible control moment that is closest to the orig-
inal commanded moment because kμz and Jrz have identical
signs in (6) and (7), respectively. If there exists no μz
c that
results in feasible motor commands, we consider a reduction
or limited increase in the thrust magnitude command Tc based
on the reasoning that the application of thrust is only effective
in the correct direction, i.e., at the correct vehicle pitch and
roll. Since adjustment of Tc results in equal magnitude shift
of the constraints, it is straightforward to verify whether there
exists an acceptable value of Tc such that the lower and upper
boundaries in (34) coincide. If so, Tc is set to this value and
μz
c to the feasible point, after which (35) is used to compute
the motor speed commands. If not, μz
c is set to the average
of the lower and upper boundaries in (34), and any infeasible
motor speed commands resulting from (35) are clipped.
Finally, the throttle vector ζ that contains the motor elec-
tronic speed control (ESC) commands is obtained as follows:
ζ = p(ωc) + KIω

ωc −ωdt
(36)
with p a vector-valued polynomial function relating motor
speeds to throttle inputs. This function was obtained by
regression analysis of static test data. Integral action is added
to account for changes in this relation due to decreasing battery
voltage. The measured motor speed signal ω remains unﬁltered
here to minimize phase lag.
IV. RESPONSE ANALYSIS
Incremental control and the tracking of high-order reference
derivatives are two key aspects of our control design. In
this section, we theoretically verify the advantages of these
features, namely, the improved robustness of incremental
control in comparison to nonincremental control and the
improved trajectory tracking accuracy due to the considera-
tion of high-order reference trajectory derivatives, i.e., jerk
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:47:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 9

TAL AND KARAMAN: ACCURATE TRACKING OF AGGRESSIVE QUADROTOR TRAJECTORIES
1211
Fig. 6.
Linearized closed-loop forward acceleration dynamics, with pitch acceleration dynamics in blue area.
and snap. The purpose of this section is to provide an intuitive
understanding of how these aspects improve tracking perfor-
mance. In order to analyze the behavior of the closed-loop
system, we use linearized dynamics and control equations,
as the resulting simpliﬁcations allow for easier qualitative
interpretation. However, the observations in this section also
apply to the full, nonlinear dynamics and control equations.
Our ﬁndings are validated and quantitatively assessed using
real-life ﬂights in Section V.
We consider forward and pitch movement around the
hover state. The subscript x indicates the forward component,
e.g., ax,ref = aT
refix, and the subscript y the pitch component,
e.g., μy = μT iy. In the hover condition, τ = −g, θ = 0, and
 = 03×1 so that (2) and (4) can be linearized to obtain
ax = −gθ + m−1 fx,ext
(37)
Jyy ˙q = μy + μy,ext
(38)
where θ is the pitch angle and Jyy is the vehicle moment of
inertia about the by-axis. Similarly, the INDI linear accelera-
tion control law (20) is linearized to obtain the error angle
−gθe = −gθ f + ax,ref −(ax) f + gθ
(39)
where −gθ f represents the forward component of the speciﬁc
thrust vector and (ax) f represents the ﬁltered forward accelera-
tion as obtained by (16). The commanded pitch acceleration αc
is obtained by taking the pitch component of (28) as follows:
αc = kθθe + kq

qref −q f

+ αref
(40)
where qref = −( jx,ref/g) and αref = −(sx,ref/g) by lin-
earization of (14) and (15). The scalar control gains kθ and
kq are obtained by selecting the pitch elements from the
corresponding control gain matrices described in Section III.
Next, we linearize the angular acceleration and moment
control laws. The four motors can be modeled collectively,
as the system is linearized around the hover state where all
motors have identical angular speeds. The scalar value ω refers
to the deviation from the hover state motor speed ω0, or,
equivalently, to half of the angular speed difference between
the front and rear motor pairs. Equating (31) and (33) and
isolating the pitch channel give
ωc =
(ω0 + ω)2
f + Jyy(4lxkτ)−1(αc −α f ) −ω0
(41)
with the factor 4 due to the number of motors. Linearization
around the hover state gives
ωc = ω f + Jyyk−1
G (αc −α f )
(42)
with the linearized control effectiveness gain kG = 8ω0lxkτ,
so that μy = kGω.
In order to analyze the robustness properties provided by
the proposed incremental controller, i.e., (39) and (42), it is
compared with a regular, i.e., nonincremental, controller with
linearized equations
θc,N I = −ax,ref
g
,
ωc,N I = Jyy
kG
αc
(43)
where αc is still given by (40) using θe = θc −θ, and the
subscript N I is used to indicate the nonincremental controller.
A. Robustness Against Disturbance Forces and Moments
An overview of the resulting linearized closed-loop accel-
eration dynamics is given in Fig. 6. From the blue area,
we obtain the following pitch acceleration dynamics:
α
αc
(s) =
Jyyk−1
G
M(s)
1−M(s)H(s)kG J −1
yy
1+ Jyyk−1
G
M(s)
1−M(s)H(s)kG J −1
yy H(s)
= M(s)
(44)
α
μy,ext
(s) =
J −1
yy
1 +
H(s)M(s)
1−H(s)M(s)
= J −1
yy (1 −H(s)M(s))
(45)
with α(s) the pitch acceleration, i.e., α(s)
=
sq(s)
=
s2θ(s). The LPF transfer function is denoted by H(s), e.g.,
(α f /α)(s) = H(s), and the motor (control) dynamics are
denoted by M(s), i.e., (ω/ωc)(s) = M(s). In (44), we observe
that the closed-loop angular acceleration dynamics are solely
determined by the motor dynamics [18]. Hence, the aggres-
siveness of trajectories that can be tracked is theoretically
limited by only the bandwidth of the motor response. This
is also the case for a nonincremental version of the controller.
The disturbance moment μy,ext is fully counteracted using
incremental control based on the two feedback loops in the
blue shaded area of Fig. 6: the expected angular acceleration
from the motor speeds, i.e., (kG/Jyy)ω f , and the measured
angular acceleration α f , which includes the effects of the dis-
turbance moment. As shown in (45), the counteraction depends
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:47:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 10

1212
IEEE TRANSACTIONS ON CONTROL SYSTEMS TECHNOLOGY, VOL. 29, NO. 3, MAY 2021
Fig. 7.
Simulated disturbance response using the proposed incremental controller and a nonincremental controller. (a) Position response to fx,ext step input.
(b) Position response to μy,ext step input.
TABLE II
TRAJECTORY TRACKING CONTROLLER GAINS
on H(s) and M(s) so that the ability to reject disturbances is
limited by the bandwidth of both the LPFs and the motors.
To the contrary, in a nonincremental controller, the α f and
ω f feedback loops are not present so that α = J −1
yy μy,est.
The disturbance moment now propagates to the attitude and
position control loops without the damping term from (45),
as there is no closed-loop angular acceleration control that
directly evaluates the moments acting on the vehicle.
We obtain similar results for the disturbance force fx,ext,
which is corrected for incrementally using the difference
between the acceleration due to thrust, i.e., −gθ f , and the
true acceleration including the disturbance force, i.e., (ax) f .
All in all, the proposed incremental controller maintains iden-
tical nominal reference tracking performance for both angular
and linear accelerations while achieving superior disturbance
rejection of external moments and forces when compared to
the nonincremental controller.
In order to evaluate the effect of the disturbance force
and moment on the position tracking error, we close the
loop around Fig. 6 using the position and velocity controller
given by (17). Fig. 7 shows the resulting step responses for
both incremental and nonincremental control. The response
was simulated using the platform-independent control gains
given in Table II, a second-order Butterworth ﬁlter with cutoff
frequency equal to 188.5 rad/s (30 Hz), and the ﬁrst-order
motor model given by (32) with τm set to 20 ms. It can
be seen that the proposed incremental controller is able to
counteract the disturbances and reaches zero steady-state error,
whereas the nonincremental controller is unable to do so.
In order to null the steady-state errors due to force and
moment disturbances, integral action must be added to the
nonincremental controller. This is not necessary in the case of
INDI so that our proposed control design is able to quickly
and wholly counteract disturbance forces and moments while
avoiding the negative effects that integral action typically
has on the tracking performance, e.g., degraded stability, and
increased overshoot and settling time.
Fig. 8.
Simulated angular acceleration step response for various modeling
errors using the proposed incremental controller.
B. Robustness Against Modeling Errors
The
proposed
control
design
requires
only
a
few
vehicle-speciﬁc parameters. Nonetheless, it is desirable that
tracking performance is maintained if inaccurate parameters
are used, e.g., because control effectiveness data obtained
from static tests may not be representative for the entire ﬂight
envelope. The linearized control equations described earlier
incorporate the ratio of the moment of inertia Jyy and the
linearized control effectiveness kG. We denote the values used
in the controller ¯Jyy and ¯kG and deﬁne the modeling error 
such that
¯Jyy
¯kG
=  Jyy
kG
.
(46)
This leads to the following pitch acceleration dynamics for the
proposed incremental NDI controller and the nonincremental
controller described earlier:
α
αc
(s) =
M(s)
( −1)H(s)M(s) + 1
(47)
α
αc N I
(s) = M(s).
(48)
It can be seen that the error acts as a simple gain in
the nonincremental controller, leading to an incorrect angu-
lar acceleration. On the contrary, the proposed incremental
controller compares the expected angular acceleration from
the motor speeds, i.e., (¯kG/ ¯Jyy)ω f , to the measured angular
acceleration, i.e., α f , to implicitly correct for the modeling
error. The corresponding angular acceleration responses for
several values of  are shown in Fig. 8. The ﬁgure shows
that the modeling error affects the transient response, but the
incremental controller is able to correct for it and quickly
reaches the commanded acceleration value even for very large
model discrepancies.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:47:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 11

TAL AND KARAMAN: ACCURATE TRACKING OF AGGRESSIVE QUADROTOR TRAJECTORIES
1213
Fig. 9.
Simulated linear acceleration tracking response for various modeling errors. (a) Using the proposed incremental controller. (b) Using a nonincremental
controller.
In order to assess the effect of modeling errors on acceler-
ation tracking, we simulate the time response to the following
acceleration reference:
ax,ref(t) = 1
2 tanh
4
3πt −2π

+ 1
2
(49)
which is C2, i.e., the corresponding jerk and snap signals
are continuous, and has boundary conditions ax,ref(0)
=
jx,ref(0) = sx,ref(0) = jx,ref(3) = sx,ref(3) = 0 and ax,ref(3) =
1 m/s2. The responses for various values of  are shown
in Fig. 9. It can be seen that the incremental controller is
able to accurately track the reference signal even when large
modeling errors are present. When nonincremental control is
used, the tracking performance declines more severely with
growing modeling error.
C. Jerk and Snap Tracking
Jerk and snap tracking is a crucial aspect of the proposed
controller design that enables tracking of fast-changing accel-
eration references. It is embodied by the feedforward terms kqs
and s2 in the nominator of the acceleration response transfer
function
ax
ax,ref
(s) =
M(s)s2 + kqs + kθ

s2 + kq H(s)M(s)s + kθ M(s).
(50)
These feedforward terms add two zeros to the closed-loop
transfer function. These zeros—in combination with the
LPF—act essentially as a lead compensator and help improve
the transient response of the system. Effective placement of
the zeros through tuning of kq leads to improved tracking
of a rapidly changing acceleration input signal, e.g., during
aggressive ﬂight maneuvers.
Fig. 10 shows the simulated acceleration responses with
and without jerk and snap tracking to the reference signal
deﬁned in (49). It can be seen that the inclusion of jerk
and snap tracking causes a faster response, resulting in more
accurate acceleration tracking. In Section V, we show that the
improvement is also achieved in practice.
V. EXPERIMENTAL RESULTS
In
this
section,
experimental
results
for
high-speed,
high-acceleration ﬂight are presented. A video of the exper-
iments is available at https://youtu.be/K15lNBAKDCs. We
evaluate the performance of the trajectory tracking controller
Fig. 10.
Simulated linear acceleration tracking response using the proposed
controller with and without jerk and snap tracking.
on two trajectories that include yawing, tight turns with
acceleration up to over 2 g, and high-speed straights at up
to 12.9 m/s. Furthermore, we examine the effect of the
feedforward inputs based on the reference trajectory jerk and
snap. We establish the independence of any model-based drag
estimate by attaching a drag-inducing cardboard plate that
more than triples the frontal area of the vehicle. Robustness
against external disturbance forces is further displayed by
pulling on a string attached to the quadcopter in hover. Finally,
we compare the proposed nonlinear INDI angular acceleration
control to its linearized counterpart.
A. Experimental Setup
Experiments were performed in an indoor ﬂight room
using the quadcopter shown in Fig. 1. The quadrotor body
is machined out of carbon ﬁber composite with balsa wood
core. The propulsion system consists of T-Motor F35A ESCs
and F40 Pro II Kv 2400 KV motors with Gemfan Hulkie
5055 propellers. Adjacent motors are mounted 18 cm apart.
The quadcopter is powered by a single 4S LiPo battery. Its
total ﬂying mass is 609 g.
Control computations are performed at 2000 Hz using an
onboard STM32H7 400-MHz microcontroller running custom
ﬁrmware. On this platform, the total computation time of a
control update at 32-bit ﬂoating-point precision is 16 μs. Lin-
ear acceleration and angular rate measurements are obtained
from an onboard Analog Devices ADIS16477-3 IMU at
2000 Hz, while position, velocity, and orientation measure-
ments are obtained from an OptiTrack motion capture system
at 360 Hz with an average latency of 18 ms. The latency
is corrected for by propagating motion capture data using
integrated IMU measurements. Motor speed measurements are
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:47:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 12

1214
IEEE TRANSACTIONS ON CONTROL SYSTEMS TECHNOLOGY, VOL. 29, NO. 3, MAY 2021
Fig. 11.
Experimental ﬂight results for 3-D trajectory. (a) Forward yaw. (b) Constant yaw.
Fig. 12.
Experimental ﬂight results for 3-D trajectory: forward yaw (blue line) and constant yaw (red line). (a) Euclidean norm of position error. (b) Yaw error.
(c) Euclidean norm of velocity. (d) Euclidean norm of acceleration.
obtained from the optical encoders at approximately 5000 Hz.
The motor speed and IMU measurements are low-pass ﬁltered
using a software second-order Butterworth ﬁlter with a cutoff
frequency of 188.5 rad/s (30 Hz).
The platform-independent controller gains listed in Table II
were
used. In
addition, the
controller requires several
platform-speciﬁc parameters, namely, vehicle mass m, moment
of inertia J, motor time constant τm, control effectiveness
matrices G1 and G2, and the gain and polynomial ﬁt used
by the motor speed controller. We obtained control effec-
tiveness data from static tests. In experiments, it was found
that using the controller on a different quadcopter (with
different dynamic properties, inertial sensors, and propulsion
system) required no changes to controller algorithms or gains.
After updating only the aforementioned platform-speciﬁc para-
meters, the controller performed without loss of tracking
accuracy.
B. Evaluation of Proposed Controller
In this section, we evaluate the performance of the trajectory
tracking controller on two trajectories: a 3-D trajectory that
includes a high-speed straight and fast turns, and a roulette
curve trajectory consisting of fast successive turns resulting
in high jerk and snap. The 3-D trajectory is generated from
a set of waypoints using the method described in [50]. The
trajectory is ﬂown with two yaw references: forward yaw, i.e.,
with the bx-axis in the velocity direction, and constant yaw set
to zero. Fig. 11 shows the corresponding reference trajectories,
along with experimental results. The forward yaw trajectory
is ﬂown in a slightly shorter time. Performance data for both
trajectories are given in Table III and shown in Fig. 12. Over
the forward yaw trajectory, a maximum speed of 12.9 m/s is
achieved, while the rms tracking error is limited to 6.6 cm. The
vehicle attains a maximum proper acceleration of 20.8 m/s2
(2.12 g). Similar values can be observed for the constant yaw
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:47:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 13

TAL AND KARAMAN: ACCURATE TRACKING OF AGGRESSIVE QUADROTOR TRAJECTORIES
1215
Fig. 13.
Experimental ﬂight results for roulette curve trajectory: reference trajectory (green line), proposed controller (blue line), without jerk and snap
tracking (red line), and with drag plate attached (magenta line). (a) Position. (b) Euclidean norm of position error. (c) Euclidean norm of velocity. (d) Euclidean
norm of acceleration.
TABLE III
3-D TRAJECTORY TRACKING PERFORMANCE FOR EXPERIMENTS
WITH FORWARD YAW AND CONSTANT YAW
trajectory. The most signiﬁcant difference are reductions in
rms yaw tracking error from 5.1◦to 1.9◦, and in maximum
yaw tracking error from 13◦to 6.4◦.
The second, roulette curve trajectory is deﬁned as
σ ref(t) =
⎡
⎢⎢⎣
r1 cos k1t + r2 cos k2t + r3 sin k3t
r4 sin k1t + r3 sin k2t + r5 cos k3t
rz
0
⎤
⎥⎥⎦
(51)
with r1 = 6 m, r2 = 1.8 m, r3 = 0.6 m, r4 = −2.25 m,
r5 = −0.3 m, r6 = −0.45 m, k1 = 0.28 rad/s, k2 =
2.8 rad/s, k3 = 1.4 rad/s, and rz a constant offset. The
trajectory, shown in Fig. 13(a), contains fast, successive turns.
Accurate tracking is particularly demanding as it requires fast
changes in acceleration, i.e., large jerk and snap, requiring
high angular rates and angular accelerations. A single lap is
traversed in 22.4 s. The position tracking error is shown in blue
in Fig. 13(b), and tracking performance metrics are given in the
ﬁrst column of Table IV. A comparison of the position tracking
error to the values in Table III conﬁrms that the controller
achieves consistent performance across trajectories. Due to
its arduous nature, the roulette curve trajectory is particularly
TABLE IV
ROULETTE CURVE TRAJECTORY TRACKING PERFORMANCE FOR THE
PROPOSED CONTROLLER, JERK AND SNAP TRACKING DISABLED,
AND DRAG PLATE ATTACHED
suitable to
expose differences in
tracking performance.
Therefore, we use the trajectory deﬁned by (51) to examine
several modiﬁcations in Sections V-C and V-D. In all cases,
the trajectory parameters are identical to those given earlier.
C. Jerk and Snap Tracking
The red curves in Fig. 13 correspond to our proposed
control design, but with jerk and snap tracking disabled,
i.e., ref = ˙ref = 03×1. Examination of the ﬁgures shows
the signiﬁcant improvement in trajectory tracking performance
obtained through the tracking of the jerk and snap feedforward
terms. This observation is conﬁrmed by comparing the ﬁrst
two columns of Table IV. It can be seen that the rms position
tracking error increases from 9.0 to 16.8 cm when jerk and
snap tracking are disabled. In Section IV, it was shown
that lead compensation provided by jerk and snap tracking
results in improved performance when tracking fast-changing
acceleration commands. This effect can also be observed
in Fig. 13. It can be seen that the system response has less
overshoot when jerk and snap tracking are enabled, which
conforms the analytical response of the linearized system.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:47:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 14

1216
IEEE TRANSACTIONS ON CONTROL SYSTEMS TECHNOLOGY, VOL. 29, NO. 3, MAY 2021
Fig. 14.
Quadrotor with 16 cm × 32 cm cardboard drag plate.
D. Increased Aerodynamic Drag
The magenta curves in Fig. 13 correspond to the trajectory
tracking controller as described in this article but using the
quadcopter with the attached drag plate. The drag plate is a
16 cm × 32 cm cardboard plate that is attached to the bottom
of the quadrotor, as shown in Fig. 14. The plate more than
triples the frontal surface area of the quadrotor and, as such,
has a signiﬁcant effect on the aerodynamic force and moment
that act on the vehicle, especially during high-speed ﬂight, and
fast pitch and yaw motion. The ﬂight controller is not adapted
in any way to account for either these aerodynamic effects or
the changes in mass and moment of inertia.
Comparison of columns (i) and (iii) in Table IV shows that
the drag plate does not signiﬁcantly affect position tracking
performance. Yaw tracking performance is also consistent,
except when the drag plate generates an external yaw moment
that causes motor speed saturation and very large momen-
tary yaw tracking error. The consistent tracking performance
demonstrates the robustness property of INDI. Controllers that
depend on the estimation of drag forces based on velocity,
such as [29] and [43], may suffer from much larger loss of
tracking performance when the aerodynamic properties of the
vehicle are modiﬁed. Instead of depending on a model-based
drag estimate, INDI counteracts the disturbance force and
moment by sensor-based incremental control. The controller
implicitly estimates the external force by (18). In Fig. 15,
it can be seen that the drag plate has a signiﬁcant effect
on the external disturbance force; its estimated magnitude
is approximately tripled. In order to counteract the greater
external force, commanded thrust and vehicle pitch increase
when the drag plate is attached.
E. Nonlinear Control Effectiveness Inversion
We also compare our proposed nonlinear inversion of the
control effectiveness (33), with linearized INDI as presented in
[19]. In the latter case, control moment and thrust commands
are tracked using linearized inversion of (5) as follows:
ωc = ω f +

2G1 + t−1G2

 μc −μ f
Tc −T f

+ t−1G2B(ωc −ω f )

(52)
where B is the one-sample backshift operator and t is the
controller update interval. This linearized inversion does not
Fig. 15.
Estimated external disturbance force for roulette curve trajectory:
proposed controller (blue line) and with drag plate attached (magenta line).
Fig. 16.
Euclidean norm of position error for hover with disturbance force
through tensioned wire.
Fig. 17.
Estimated external disturbance force for hover with disturbance
force through tensioned wire.
consider local nonlinearity of (5), nor does it consider the tran-
sient response of the motors. Therefore, nonlinear inversion of
(33)—as described in Section III-E—theoretically results in
improved tracking of the angular acceleration command and
thereby in improved trajectory tracking performance.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:47:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 15

TAL AND KARAMAN: ACCURATE TRACKING OF AGGRESSIVE QUADROTOR TRAJECTORIES
1217
Fig. 18.
Quadrotor in hover with disturbance force through the tensioned wire. (a) Time is 22 s. (b) Time is 28 s. (c) Time is 40 s.
In experimental ﬂights, we found that the difference
between nonlinear and linearized inversion does not lead to
signiﬁcant differences in tracking performance for our quadro-
tor system. However, we found that the failure to properly
consider the transient response of the motors in (52) can
be detrimental to controller performance. In particular, if the
motor time constant τm and the controller interval t differ
greatly, this may result in fast yaw oscillations. Consideration
of the motor time constant τm, as in (33), resolves this issue.
F. Hover With Disturbance Force
For a constant σ ref input, i.e., hover, the controller con-
sistently achieves subcentimeter position tracking error if no
external disturbance is purposely applied. In this section,
we present results for hover with an external disturbance force
through a tensioned wire. One end of the wire is attached to
the bottom plate of the quadrotor. We pull on the other end
of the wire to drag the vehicle away from its hover position.
In Fig. 16, it can be seen that the quadrotor maintains its
position to within at most 4 cm, while a changing disturbance
force is applied through the wire. The largest position error
occurs around 10 s when an external force of approximately
3.7 N is applied. Fig. 17 shows the estimated external distur-
bance force, computed according to (18). The force component
in the iz-direction has a small steady-state value due to
discrepancy between true and estimated thrust. Comparison
to Fig. 18 shows that the direction of the estimated external
disturbance force vector corresponds to the direction of the
wire. For example, at 22 s, Fig. 17 shows that the external force
has a negative component in the ix-direction and a positive
component in the iy-direction, and in Fig. 18(a), the wire is
indeed tensioned in the negative ix- and positive iy-direction.
VI. CONCLUSION
In this article, we proposed a novel control system for
the tracking of aggressive, i.e., fast and agile, trajectories for
quadrotor vehicles. Our controller tracks the reference position
and yaw angle with their derivatives of up to fourth order,
speciﬁcally the position, velocity, acceleration, jerk, and snap
along with the yaw angle, yaw rate, and yaw acceleration using
incremental NDI and differential ﬂatness. The tracking of snap
was enabled by closed-loop control of the propeller speeds
using optical encoders attached to each motor hub. The result-
ing control system achieves 6.6-cm rms position tracking error
in agile and fast ﬂight, reaching a top speed of 12.9 m/s and
acceleration of 2.1 g, in an 18-m-long, 7-m-wide, and 3-m-tall
ﬂight volume. Our analysis and experiments demonstrated the
robustness of the control design against external disturbances,
making it particularly suitable for high-speed ﬂight where
signiﬁcant aerodynamic effects occur. The proposed controller
does not require any modeling or estimation of aerodynamic
drag parameters.
ACKNOWLEDGMENT
The authors thank Gilhyun Ryou for help with the
experiments.
REFERENCES
[1] E. Tal and S. Karaman, “Accurate tracking of aggressive quadrotor tra-
jectories using incremental nonlinear dynamic inversion and differential
ﬂatness,” in Proc. IEEE Conf. Decision Control (CDC), Dec. 2018,
pp. 4282–4288.
[2] J.-J.
E.
Slotine
and
W.
Li,
Applied
Nonlinear
Control.
Upper Saddle River, NJ, USA: Prentice-Hall, 1991.
[3] A. Isidori, Nonlinear Control Systems. New York, NY, USA: Springer,
1995.
[4] S. Sastry, Nonlinear Systems: Analysis, Stability, and Control. New York,
NY, USA: Springer-Verlag, 1999.
[5] S. A. Snell, D. F. Enns, and W. L. Garrard, “Nonlinear inversion
ﬂight control for a supermaneuverable aircraft,” J. Guid., Control, Dyn.,
vol. 15, no. 4, pp. 976–984, Jul. 1992.
[6] D. J. Bugajski and D. F. Enns, “Nonlinear control law with application
to high angle-of-attack ﬂight,” J. Guid., Control, Dyn., vol. 15, no. 3,
pp. 761–767, May 1992.
[7] J. Hauser, S. Sastry, and G. Meyer, “Nonlinear control design for
slightly non-minimum phase systems: Application to V/STOL aircraft,”
Automatica, vol. 28, no. 4, pp. 665–679, Jul. 1992.
[8] D. Enns, D. Bugajski, R. Hendrick, and G. Stein, “Dynamic inversion:
An evolving methodology for ﬂight control design,” Int. J. Control,
vol. 59, no. 1, pp. 71–91, Jan. 1994.
[9] T. J. Koo and S. Sastry, “Output tracking control design of a helicopter
model based on approximate linearization,” in Proc. 37th IEEE Conf.
Decision Control, Dec. 1998, pp. 3635–3640.
[10] D. Lee, H. Jin Kim, and S. Sastry, “Feedback linearization vs. Adaptive
sliding mode control for a quadrotor helicopter,” Int. J. Control, Autom.
Syst., vol. 7, no. 3, pp. 419–428, Jun. 2009.
[11] R. Xu and U. Ozguner, “Sliding mode control of a quadrotor helicopter,”
in Proc. 45th IEEE Conf. Decis. Control, Mar. 2006, pp. 4957–4962.
[12] T. Madani and A. Benallegue, “Backstepping sliding mode control
applied to a miniature quadrotor ﬂying robot,” in Proc. 32nd Annu.
Conf. IEEE Ind. Electron., Nov. 2006, pp. 700–705.
[13] E. Frazzoli, M. A. Dahleh, and E. Feron, “Trajectory tracking control
design for autonomous helicopters using a backstepping algorithm,” in
Proc. Amer. Control Conf. (ACC), 2000, pp. 4102–4107.
[14] S. Sieberling, Q. P. Chu, and J. A. Mulder, “Robust ﬂight control
using incremental nonlinear dynamic inversion and angular acceleration
prediction,” J. Guid., Control, Dyn., vol. 33, no. 6, pp. 1732–1742,
Nov. 2010.
[15] P. Simplício, M. D. Pavel, E. van Kampen, and Q. P. Chu, “An accelera-
tion measurements-based approach for helicopter nonlinear ﬂight control
using incremental nonlinear dynamic inversion,” Control Eng. Pract.,
vol. 21, no. 8, pp. 1065–1077, Aug. 2013.
[16] P. Smith, “A simpliﬁed approach to nonlinear dynamic inversion based
ﬂight control,” in Proc. 23rd Atmos. Flight Mech. Conf., Aug. 1998,
pp. 4461–4469.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:47:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 16

1218
IEEE TRANSACTIONS ON CONTROL SYSTEMS TECHNOLOGY, VOL. 29, NO. 3, MAY 2021
[17] B. Bacon and A. Ostroff, “Reconﬁgurable ﬂight control using nonlin-
ear dynamic inversion with a special accelerometer implementation,”
in Proc. AIAA Guid., Navigat., Control Conf. Exhib., Aug. 2000,
pp. 4565–4579.
[18] E. J. J. Smeur, Q. Chu, and G. C. H. E. de Croon, “Adaptive incremental
nonlinear dynamic inversion for attitude control of micro air vehicles,”
J. Guid., Control, Dyn., vol. 39, no. 3, pp. 450–461, Mar. 2016.
[19] E. J. J. Smeur, G. C. H. E. de Croon, and Q. Chu, “Cascaded incremental
nonlinear dynamic inversion for MAV disturbance rejection,” Control
Eng. Pract., vol. 73, pp. 79–90, Apr. 2018.
[20] M. Fliess, J. Lévine, P. Martin, and P. Rouchon, “Sur les systèmes
non linéaires différentiellement plats,” CR Acad. Sci. Paris, vol. 315,
pp. 619–624, Dec. 1992.
[21] P. Martin, “Contribution á l’étude des systèmes différentiellement plats,”
Ph.D. dissertation, Dept. Centre Automatique Syst., École Nationale
Supérieure des Mines de Paris, France, 1992.
[22] M. van Nieuwstadt, M. Rathinam, and R. M. Murray, “Differential
ﬂatness and absolute equivalence of nonlinear control systems,” SIAM
J. Control Optim., vol. 36, no. 4, pp. 1225–1239, Jul. 1998.
[23] P. Martin, R. M. Murray, and P. Rouchon, “Flat systems, equivalence and
trajectory generation,” California Inst. Technol., Pasadena, CA, USA,
Tech. Rep. 2003.008, 2003.
[24] M. Fliess, J. Lévine, P. Martin, and P. Rouchon, “Flatness and defect of
non-linear systems: Introductory theory and examples,” Int. J. Control,
vol. 61, no. 6, pp. 1327–1361, Jun. 1995.
[25] P. Martin, “Aircraft control using ﬂatness,” in Proc. IMACS/IEEE-
SMC Multiconference CESA Symp. Control, Optim. Supervision, 1996,
pp. 194–199.
[26] G. Rivera, O. Sawodny, T. E. Simos, G. Psihoyios, and C. Tsitouras,
“Flatness-based tracking control and nonlinear observer for a micro
aerial quadcopter,” in Proc. AIP, 2010, pp. 386–389.
[27] J. Ferrin, R. Leishman, R. Beard, and T. McLain, “Differential ﬂat-
ness based control of a rotorcraft for aggressive maneuvers,” in Proc.
IEEE/RSJ Int. Conf. Intell. Robots Syst., Sep. 2011, pp. 2688–2693.
[28] T. Engelhardt, T. Konrad, B. Schafer, and D. Abel, “Flatness-based
control for a quadrotor camera helicopter using model predictive control
trajectory generation,” in Proc. 24th Medit. Conf. Control Autom. (MED),
Jun. 2016, pp. 852–859.
[29] M. Faessler, A. Franchi, and D. Scaramuzza, “Differential ﬂatness of
quadrotor dynamics subject to rotor drag for accurate tracking of high-
speed trajectories,” IEEE Robot. Autom. Lett., vol. 3, no. 2, pp. 620–626,
Apr. 2018.
[30] G. Hoffmann, D. G. Rajnarayan, S. L. Waslander, D. Dostal, J. S. Jang,
and C. J. Tomlin, “The Stanford testbed of autonomous rotorcraft for
multi agent control (STARMAC),” in Proc. 23rd Digit. Avionics Syst.
Conf., 2004, p. 12.
[31] I. Kroo et al., The Mesicopter: A Miniature Rotorcraft Concept. Phase
II Interim Report. Stanford, CA, USA: Stanford University, 2000.
[32] P. Pounds, R. Mahony, P. Hynes, and J. M. Roberts, “Design of a four-
rotor aerial robot,” in Proc. Australas. Conf. Robot. Autom. (ACRA),
2002, pp. 145–150.
[33] T. Hamel, R. Mahony, R. Lozano, and J. Ostrowski, “Dynamic modelling
and conﬁguration stabilization for an X4-ﬂyer,” in Proc. 15th IFAC
World Congr., 2002, pp. 217–222.
[34] M. Valenti, B. Bethke, G. Fiore, J. How, and E. Feron, “Indoor multi-
vehicle ﬂight testbed for fault detection, isolation, and recovery,” in Proc.
AIAA Guid., Navigat., Control Conf. Exhib., Aug. 2006, pp. 6200–6217.
[35] J. P. How, B. Behihke, A. Frank, D. Dale, and J. Vian, “Real-time indoor
autonomous vehicle test environment,” IEEE Control Syst., vol. 28, no. 2,
pp. 51–64, Apr. 2008.
[36] S. Zarovy et al., “Experimental study of gust effects on micro air
vehicles,” in Proc. AIAA Atmos. Flight Mech. Conf., Aug. 2010,
pp. 7818–7844.
[37] G. Ducard and R. D’Andrea, “Autonomous quadrotor ﬂight using a
vision system and accommodating frames misalignment,” in Proc. IEEE
Int. Symp. Ind. Embedded Syst., Jul. 2009, pp. 261–264.
[38] N. Michael, D. Mellinger, Q. Lindsey, and V. Kumar, “The GRASP
multiple micro-UAV testbed,” IEEE Robot. Autom. Mag., vol. 17, no. 3,
pp. 56–65, Sep. 2010.
[39] M. Ol, G. Parker, G. Abate, and J. Evers, “Flight controls and perfor-
mance challenges for MAVs in complex environments,” in Proc. AIAA
Guid., Navigat. Control Conf. Exhib., Aug. 2008, pp. 6508–6529.
[40] S. Bieniawski, D. Halaas, and J. Vian, “Micro-aerial vehicle ﬂight in
turbulent environments: Use of an indoor ﬂight facility for rapid design
and evaluation,” in Proc. AIAA Guid., Navigat. Control Conf. Exhib.,
Aug. 2008, pp. 6512–6522.
[41] D. Mellinger, N. Michael, and V. Kumar, “Trajectory generation and
control for precise aggressive maneuvers with quadrotors,” Int. J. Robot.
Res., vol. 31, no. 5, pp. 664–674, Apr. 2012.
[42] M. Muller, S. Lupashin, and R. D’Andrea, “Quadrocopter ball jug-
gling,” in Proc. IEEE/RSJ Int. Conf. Intell. Robots Syst., Sep. 2011,
pp. 5113–5120.
[43] J. Svacha, K. Mohta, and V. Kumar, “Improving quadrotor trajectory
tracking by compensating for aerodynamic effects,” in Proc. Int. Conf.
Unmanned Aircr. Syst. (ICUAS), Jun. 2017, pp. 860–866.
[44] J.-M. Kai, G. Allibert, M.-D. Hua, and T. Hamel, “Nonlinear feedback
control of quadrotors exploiting ﬁrst-order drag effects,” in Proc. 20th
IFAC World Congr., 2017, pp. 8189–8195.
[45] H. Liu, D. Li, Z. Zuo, and Y. Zhong, “Robust three-loop trajectory
tracking control for quadrotors with multiple uncertainties,” IEEE Trans.
Ind. Electron., vol. 63, no. 4, pp. 2263–2274, Apr. 2016.
[46] H. Huang, G. M. Hoffmann, S. L. Waslander, and C. J. Tomlin, “Aerody-
namics and control of autonomous quadrotor helicopters in aggressive
maneuvering,” in Proc. IEEE Int. Conf. Robot. Autom. (ICRA), 2009,
pp. 3277–3282.
[47] A. P. Schoellig, F. L. Mueller, and R. D’Andrea, “Optimization-based
iterative learning for precise quadrocopter trajectory tracking,” Auto.
Robots, vol. 33, nos. 1–2, pp. 103–127, Aug. 2012.
[48] G. Hoffmann, H. Huang, S. Waslander, and C. Tomlin, “Quadrotor
helicopter ﬂight dynamics and control: Theory and experiment,” in Proc.
AIAA Guid., Navigat. Control Conf. Exhib., Aug. 2007, pp. 6461–6480.
[49] P. Martin and E. Salaun, “The true role of accelerometer feedback in
quadrotor control,” in Proc. IEEE Int. Conf. Robot. Autom., May 2010,
pp. 1623–1629.
[50] G. Ryou, E. Tal, and S. Karaman, “Multi-ﬁdelity black-box optimization
for time-optimal quadrotor maneuvers,” in Proc. Robot., Sci. Syst. (RSS),
2020.
Ezra
Tal
(Graduate
Student
Member,
IEEE)
received the B.Sc. and M.Sc. degrees from the
Faculty of Aerospace Engineering, Delft University
of Technology, Delft, The Netherlands, in 2012 and
2015, respectively. He is currently pursuing the
Ph.D. degree with the Massachusetts Institute of
Technology, Cambridge, MA, USA.
In 2012, he was a Visiting Student with the
Technion–Israel
Institute
of
Technology,
Haifa,
Israel. In 2015, he visited the NASA Ames Research
Center (ARC), Mountain View, CA, USA, as a
Graduate Research Intern. His current research interests include differential
games and robust control theory, particularly for applications in planning and
control of robotics vehicles.
Mr. Tal was a recipient of the Huygens Talent Scholarship, and the NASA
Group Achievement Award as part of the Adaptive Aeroelastic Wing Shaping
Control Team at ARC.
Sertac Karaman (Member, IEEE) received the S.M.
degree in mechanical engineering and the Ph.D.
degree in electrical engineering and computer sci-
ence from the Massachusetts Institute of Technology
(MIT), Cambridge, MA, USA, in 2009 and 2012,
respectively.
He is currently an Associate Professor of aeronau-
tics and astronautics with MIT. He studies the appli-
cations of probability theory, stochastic processes,
stochastic geometry, formal methods, and optimiza-
tion for the design and analysis of high-performance
cyber–physical systems. The application areas of his research include driver-
less cars, unmanned aerial vehicles, distributed aerial surveillance systems,
air trafﬁc control, certiﬁcation and veriﬁcation of control systems software,
and many others.
Dr. Karaman was a recipient of the IEEE Robotics and Automation Society
Early Career Award in 2017, the Ofﬁce of Naval Research Young Investigator
Award in 2017, the Army Research Ofﬁce Young Investigator Award in 2015,
and the National Science Foundation Faculty Career Development (CAREER)
Award in 2014.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:47:23 UTC from IEEE Xplore.  Restrictions apply.
