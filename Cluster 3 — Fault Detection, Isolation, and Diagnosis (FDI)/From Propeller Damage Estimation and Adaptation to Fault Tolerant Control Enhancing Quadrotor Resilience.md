# From Propeller Damage Estimation and Adaptation to Fault Tolerant Control Enhancing Quadrotor Resilience.pdf

## Page 1

IEEE ROBOTICS AND AUTOMATION LETTERS, VOL. 9, NO. 5, MAY 2024
4297
From Propeller Damage Estimation and Adaptation
to Fault Tolerant Control: Enhancing
Quadrotor Resilience
Jeffrey Mao
, Jennifer Yeom
, Suraj Nair
, and Giuseppe Loianno
, Member, IEEE
Abstract—Aerial robots are required to remain operational even
in the event of system disturbances, damages, or failures to ensure
resilient and robust task completion and safety. One common
failure case is propeller damage, which presents a signiﬁcant chal-
lenge in both quantiﬁcation and compensation. In this letter, we
propose a novel adaptive control scheme capable of detecting and
compensating for multi-rotor propeller damages, ensuring safe and
robust ﬂight performances. Our solution combines an L1 adaptive
controller with an optimization routine for damage inference and
compensation of single or dual propellers, with the capability to
seamlessly transition to a fault-tolerant solution in case the damage
becomes severe. We experimentally identify the conditions under
which the L1 adaptive solution remains preferable over a fault-
tolerant alternative. Experimental results validate the proposed
approach demonstrating the ability of our solution to adapt and
compensate onboard in real time on a quadrotor for damages even
when multiple propellers are damaged.
Index Terms—Aerial systems: mechanics and control, aerial
systems: applications.
I. INTRODUCTION
M
ICRO Aerial Vehicles (MAVs) such as quadrotors are
becoming ubiquitous in applications such as search and
rescue and aerial photography [1]. However, MAV-related ac-
cidents hinder the growth of the industry and erode public
conﬁdence in drone safety. As a result, it is necessary to develop
inference and control approaches that can guarantee safe and
reliable ﬂight in case of system damage. Propellers on MAVs
are susceptible to damage, especially in the event of collisions
or after prolonged use, primarily due to their size, location,
and lightweight construction. In addition, detecting the occur-
rence and location of propeller failures is challenging. Indirectly
sensing individual motor thrusts is further complicated due to
Manuscript received 19 October 2023; accepted 28 February 2024. Date of
publication 25 March 2024; date of current version 29 March 2024. This letter
was recommended for publication by Associate Editor G. Xin and Editor L.
Pallottino upon evaluation of the reviewers’ comments. This work was supported
in part by DEVCOM ARL under Grant DCIST CRA W911NF-17-2-0181, in
part by NSF CAREER Award under Grant 2145277, in part by DARPA YFA
under Grant D22AP00156-00, in part by Qualcomm Research, Nokia, and in
part by NYU Wireless. (Jeffrey Mao and Jennifer Yeom are co-ﬁrst authors.)
(Corresponding author: Jeffrey Mao.)
The authors are with the Tandon School of Engineering, New York University,
Brooklyn, NY 11201 USA (e-mail: jm7752@nyu.edu; jennifer.yeom@nyu.edu;
surajkiron@nyu.edu; loiannog@nyu.edu).
Video: https://youtu.be/elVO0-tkPs0
This
letter
has
supplementary
downloadable
material
available
at
https://doi.org/10.1109/LRA.2024.3380923, provided by the authors.
Digital Object Identiﬁer 10.1109/LRA.2024.3380923
Fig. 1.
L1 adaptive and fault-tolerant control with one damaged propeller
(circled in red dash). The fault-tolerant controlled quadrotor is forced to spin
(over 1000 deg/sec).
the nonlinear dynamics of the quadrotor and the difﬁculty of
measuring higher order angular acceleration or moment terms.
Our work speciﬁcally introduces an adaptive control scheme
for quadrotors to autonomously infer and adjust ﬂight behavior
in response to propeller damages or failures.
This work makes the following contributions. First, we pro-
pose a propeller damage estimation technique by combining
an L1 Adaptive algorithm and an optimization routine with
no need for direct RPM (Rotations Per Minute) measurements
or estimation of angular accelerations, making it suitable for
low-cost systems. Second, we propose a holistic control scheme
coupling the L1 adaptive and fault-tolerant controller modules
for autonomous transition from L1 adaptation to the fault-
tolerant mode in situations where adaptation alone proves to be
insufﬁcient for ensuring safe and effective ﬂight. This approach
enhances the system’s capability to manage the full range of
propeller damage. Finally, we demonstrate the performance of
the damage estimation and controller design in extensive real-
world experiments and compare our estimation method to using
astandardPID(ProportionalIntegralDerivative)controller.This
is the ﬁrst work to tackle precise estimation and compensation
of propeller damage rather than considering a reduction of effec-
tiveness of a motor-propeller pair. Challenges include unequal
loss between thrust and torque coefﬁcients along with additional
2377-3766 © 2024 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 08:48:53 UTC from IEEE Xplore.  Restrictions apply.

## Page 2

4298
IEEE ROBOTICS AND AUTOMATION LETTERS, VOL. 9, NO. 5, MAY 2024
noise on the system from damaged propellers as well as the
unavailability of direct RPM measurements.
II. RELATED WORKS
Damage Estimation: Research in fault estimation covers a
variety of vehicles detailed in this survey [2] such as ﬁxed
wings and rotary aerial robots. We can divide methods han-
dling propeller damage into two categories: empirical and state
estimation methods. Empirical works address propeller damage
estimation through parameter identiﬁcation [3] or sensor noise
analysis[4].Theapproachproposedin[3]successfullyestimates
the loss of effectiveness of a single motor but is only tested in
simulation, whereas [4] uses accelerometer noise to estimate
propeller damage, but is only tested on a minuscule amount of
propeller damage.
Other works rely on state estimation to accurately measure the
damage[5],[6].Thesetypicallyhaveaslowerresponsetimethan
empirical methods, and are only able to handle motor damage
estimation rather than propeller damage as in the proposed work.
They typically assume the damage from the propeller motor pair
can be represented as a scaled factor of each individual RPM. For
the case of propeller damage, this assumption is not accurate.
The thrust and torque coefﬁcients scale with the propeller radius,
r, as a function of r4 and r5 respectively [7]. This increases the
complexity of our propeller damage compared to the problems
in [5], [6], [8]. Typically a reduced state Kalman Filter [5], [6],
[9] is used in either a single [5], [9] or cascaded [10], [11]
form. These studies test their systems by artiﬁcially injecting a
fault that decelerates the motor rather than testing true propeller
damages. State estimation through cascaded Kalman Filters can
infer and adapt up to 60% motor damage in [11]. However,
it is only tested in simulation for motor damage and does not
include the possibility to switch to the fault-tolerant mode. Our
work negates up to 40 −60% propeller damage in real-world
experiments as shown in Fig. 1. Uniquely, [8] implements a
Kalman ﬁlter method to detect a complete loss of a propeller
and is able to detect a fault within 0.1 s of occurrence. However,
this method requires accurate RPM measurements and cannot
adapt to propeller damage.
Damage Compensation: Once propeller damage is estimated,
there are two options to incorporate damage compensation into
control. The ﬁrst option is adaptation where the damaged pro-
peller is given a scaled up motor action [5], [6] to compensate for
the damage. This adaptation is effective for small and medium
damages but is unable to stabilize the robot for severe damages.
The second option is to employ a fault-tolerant control strategy
that completely disables the damaged propeller [3], [12] but
sacriﬁces yaw control.
A few adaptive techniques are Incremental Nonlinear Dy-
namic Inversion (INDI) [13], dual loop disturbance ob-
servers [14], and L1 [15], [16], [17]. These works provide
additional control actions that augment the capabilities of a base-
line controller to reject some actuator damages or disturbances.
However, none of the above works provides an estimate to judge
when propeller damage is too severe for adaption as shown in
the proposed work. Other methods exist for adaptation [18],
[19],[20],throughmodelidentiﬁcationorautomaticgaintuning,
but cannot adapt to rapid changes. In this work, we design an
L1 adaptive technique to compensate and accurately estimate
propeller damage. Unlike INDI [13] that requires angular accel-
eration which is difﬁcult to estimate, our method only requires
Fig. 2.
MAV model with inertial and body frame deﬁnitions.
angular velocity which can be obtained from an on board Inertial
Measurement Unit (IMU).
Existing fault-tolerant control strategies are adept at ensuring
robust control even in the event of single or multiple rotor fail-
ures [2], [13], [21], [22]. However, these solutions require iden-
tifying the faulty propeller, and sacriﬁcing yaw control which
results in a rapid yaw spin as depicted in Fig. 1 making them
unsuitable for small to medium damages. Our work introduces a
holisticcontrolschemedesignedtodetect,infer,andcompensate
for propeller damage, with the capability to smoothly transition
to a fault-tolerant solution when severe damage is detected
allowing effective operations for safe recovery and navigation.
III. METHODOLOGY
A. Preliminaries
We use two coordinate frames to represent the dynamics
of the system. As shown in Fig. 2, we choose the inertial
reference frame as

e1
e2
e3

and the body ﬁxed frame as

b1
b2
b3

. The origin of the body frame is aligned with
the center of mass of the MAV. The body frame follows the East
North Up (ENU) coordinate system. The ﬁrst axis b1 is aligned
to the heading and the third axis, b3 aligns with the thrust vector
of the vehicle. The dynamics of the system can be written as
˙p = v,
m ˙v = mge3 + q ⊗fe3,
˙q = 1
2q ⊗
 0
Ω

,
M = J ˙Ω + Ω × JΩ,
(1)
where p ∈R3, and v ∈R3 are the position and velocity in the
worldframe.R ∈SO(3)isarotationmatrixfromthebodyﬁxed
frame to the inertial frame, q is the quaternion representation of
R, and ⊗is quaternion multiplication. f, m, g are the thrust,
mass and gravity respectively, Ω ∈R3 is the angular velocity
with respect to the body frame, M =

M1
M2
M3
⊤are the
moments around the three body frame axes, and J ∈R3×3 is the
robot inertia matrix.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 08:48:53 UTC from IEEE Xplore.  Restrictions apply.

## Page 3

MAO et al.: FROM PROPELLER DAMAGE ESTIMATION AND ADAPTATION TO FAULT TOLERANT CONTROL: ENHANCING
4299
Fig. 3.
The cascaded control scheme, shows the L1 Adaptation Controller
(blue), receives the partial state feedback from the system. The Fault Tolerant
Controller (pink) is activated only once damage estimate exceeds 50%.
B. Control Design
We adapt the geometric controller derived in [23] for the pos-
sibility of propeller damage, or fully losing one or two opposing
rotors in ﬂight. An outer controller solves for the desired attitude
R, thrust f, and angular velocities Ω. The inner controller solves
for the moments required to control the attitude of the MAV. The
geometric controller tracks position p and yaw ψ by generating
force and moments control signals. The L1 augmentation is
inserted into the controller as seen in Fig. 3. The L1 controller
uses a state predictor to estimate the partial state [v⊤Ω⊤]⊤with
the unknown disturbances. The adaptation law compares the
prediction to the measured state and generates the control output
to compensate for disturbances. If the adaptation law accurately
estimates the unknown disturbances then the tracking error will
converge to zero [24] assuming the augmented action is with in
the actuator limits.
1) Outer-Loop Controller: As per the standard geometric
control algorithm, the thrust vector is normalized and chosen
as the third body axis, or thrust vector b3 as
b3 =
˙v + ge3
∥˙v + ge3∥.
(2)
Next, we formulate the rotation matrix based on ψ or the yaw of
the vehicle. We denote the individual elements of the thrust vec-
tor as b3 =

b3x
b3y
b3z
⊤. We can formulate a quaternion
representing the desired tilt, qtilt, and yaw rotation qψ such as
in [25]. The below quaternion formulations are all scalar ﬁrst
notation.
qtilt =
1

2(1 + b3z)

1 + b3z
−b3y
b3x
0

,
qψ =

cos(0.5ψ)
0
0
sin(0.5ψ)

.
(3)
Multiplying the quaternion qtilt and qψ we formulate the full
vehicle’s rotation with qd being the quaternion representation
of desired orientation, Rd. A rotation matrices representation of
(3) is in [21]
qd = qtilt ⊗qψ.
(4)
The ﬁrst control input, thrust, is solved for with
f = m (kp(p −pd) + kv(v −vd) + ˙vd + ge3) · b3,
(5)
Algorithm 1: L1 Adaptation Control Step [k] →[k + 1].
Input: Measured velocities vm[k], Ωm[k]
Output: L1 Force and Moment fL1[k], ML1[k]
State: Predicted velocities vp[k], Ωp[k]
L1 Adaption control law Section III-C1
1:
Calculate the Disturbances, σ[k] (11)
2:
fL1[k] = LPF(−σ3[k])
3:
ML1[k] = LPF(−σ4:6[k])
State Predictor (Update) Section III-C2
4:
Solve for ˙vp[k] ((12)) and ˙Ωp[k] (13)
5:
Solve for vp[k + 1] and Ωp[k + 1] (14)
6:
Update the Current [k] with the Next State [k + 1]
7:
Add fL1[k] the base thrust control (5)
8:
Add ML1[k] to the base moment control (10)
where pd and vd are desired position and velocity of the vehicle
and kp, kv ∈R3 are the gains for the respective errors. Lastly,
the desired angular velocity Ωd, is
 0
Ωd

= 2q−1
d ⊗˙qd,
(6)
as a function of the desired ˙b3 and ˙ψ such as in [25].
2) Inner-Loop Controller: The inner controller solves for the
secondcontrolinput,moment,fromtheerrorinattitudeanderror
in angular velocity. In a traditional geometric controller [23],
the attitude tracking error, eR is calculated by using the rotation
matrices as
eR = 1
2(R⊤
d R −R⊤Rd)∨,
(7)
where the ∨term converts a skew-symmetric matrix to vector
form. For the fault-tolerant controller, we use a reduced attitude
error metric to decouple the yaw control that shows improved
performances as demonstrated in our recenter work [21] for the
fault-tolerant control case
eRreduced = b3 d × b3,
(8)
where b3 d is the normalized desired thrust vector and b3 is
the current z axis of the body ﬁxed frame we get from the
localization. The cross product of b3 d and b3 measures how
much the actual direction deviates from the desired direction.
The angular velocity error, eΩ is calculated by
eΩ = Ω −R⊤RdΩd.
(9)
The moments are calculated using
M = −kReR −kΩeΩ + Ω × JΩ,
(10)
where kR and kΩ are rotation and angular velocity gains.
C. Adaptive Control
We supplement our controller with an L1 adaptive controller
by including two elements: 1) an adaption law to solve for an
action to counteract the un-modeled disturbances on the system,
and 2) a state predictor to estimate a predicted state, linear vp
and angular Ωp velocities given the L1 action and un-modeled
disturbances.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 08:48:53 UTC from IEEE Xplore.  Restrictions apply.

## Page 4

4300
IEEE ROBOTICS AND AUTOMATION LETTERS, VOL. 9, NO. 5, MAY 2024
1) L1 Adaptation Law: First, we characterize the distur-
bances σ =

f ⊤
ext
M⊤
ext
⊤which represents the un-modeled
force and moments on the vehicle both expressed in the body
frame. These disturbances are obtained using the error between
the predicted state velocity

v⊤
p
Ω⊤
p

generated from the state
predictor in Section III-C2 and measured velocities, (vm, Ωm).
Let k denote the discrete time step of the system. We set a
diagonal gain deﬁned by the user K ∈R6×6 to generate a
speciﬁc gain, A, based on the time step, dt, between k and
k + 1 time instants with
A = (exp(K · dt −I)−1K) exp(K · dt),
σ[k] =
mR⊤
0
0
J

A
vm[k]
Ωm[k]

−
vp[k]
Ωp[k]

.
(11)
We solve the additional action μL1 =

fL1
M⊤
L1
⊤from our
disturbance σ. The moment disturbance estimates σ4:6 and
disturbance along the thrust axis σ3 can be negated by providing
an equal but negative compensation to cancel the disturbance
μL1 = −σ3:6. We implement an exponential Low Pass Filter
(LPF) to mitigate the noise present in the state estimation,
achieving smoother results: μL1 = −LPF(σ3:6). fL1 and ML1
are added to (5) and (10) respectively and reﬂected in Fig. 3.
2) State Predictor: Separately, once we solve for the action
μL1 and external disturbances σ, we solve for the next predicted
velocities of our system, (vp[k], Ωp[k]) →(vp[k + 1], Ωp[k +
1]). First, we solve for the linear and angular acceleration ˙vp[k]
and ˙Ωp[k] as
˙vp[k] = (f[k] + fL1[k])
m
Re3
	



actuation
+ 1
mRσ1:3[k]
	



disturbance
+ ge3
	

gravity
,
(12)
˙Ωp[k] = J−1(M[k]+ML1[k]
	



actuation
+ σ4:6[k]
	 
 
disturbance
−Ωm[k] × JΩm[k]
	



cross
).
(13)
Finally, we integrate over a time step dt with a weighted average
of the measurement and the predicted velocities. A weighted
average is used to ﬁlter the noise inherent in the measured
velocity
vp[k + 1]
Ωp[k + 1]

=(1 −λ)
vp[k]
Ωp[k]

+λ
vm[k]
Ωm[k]

+dt
 ˙vp[k]
˙Ωp[k]

.
(14)
The weighted average term is λ = K · dt. This is predicted value
is looped backed into our L1 control law (11) in the next time
step k + 1
D. Propeller Damage Estimation
We estimate the propellers’ damage using our augmented
control. We assume that in nominal ﬂight conditions a quadratic
relationship between the ith propeller thrust and corresponding
motor speed fi = kfrealω2
i where kfreal represents the true thrust
coefﬁcient of the propeller and ωi is the motor speed of the ith
propeller. A damaged propeller spinning at the original RPM
provides lower thrust due to the change in kfreal. We quantify
our propeller damages on the thrust coefﬁcient by the following
mismatch index
kfmis = 1 −kfreal
kfmodel
,
(15)
wherekfmodel is thethrust coefﬁcient usedbyour controller. When
a propeller gets damaged, both the thrust coefﬁcient kf and
torque coefﬁcient km are affected. The two coefﬁcients decay
as functions of the propeller radius r4 and r5 respectively [7].
Due to this relationship, a damaged propeller spinning at higher
RPM will provide adequate thrust but less torque than a healthy
propeller. The L1 adaptive law compensates for both thrust and
torque mismatch requiring the healthy propellers’ RPMs to com-
pensate for the damaged propeller’s lower torque. As the thrust
and torque coefﬁcients are highly coupled, we formulate an
optimization problem for damage estimation. First, we initialize
a baseline estimate of our propeller damage for each propeller.
Next, we identify damaged and undamaged propellers to form a
prior. Finally, we perform a null-space projection optimization.
We can estimate our initial guess kfreal using the additional
RPM spin that L1 provides to our system. Speciﬁcally, let ωi now
be the RPM for motor i given by the geometric controller without
L1 compensation and ωL1i be the RPM for motor i with L1
compensation. Supposing that L1 adaptation has compensated
for the propeller damage, we will have
kfmodelω2
i = kfrealω2
L1i.
(16)
Converting terms we have an initial guess
kfreal = kfmodel · ω2
i
ω2
L1i
.
(17)
Next, we identify the damaged propellers using our initial
estimate di within a 5% threshold as
di =

0.0
if kfmis ≤0.05
kfmodel ·
ω2
i
ω2
L1i
if kfmis > 0.05.
(18)
This threshold is set as undamaged propellers are likely to have
negative damage due to torque mismatch. However a negative
damage is physically impossible. A detailed explanation of this
concept is discussed in Section V.
We then formulate our estimate as a quadratic programming
problem. Let Let k =

kf1real
kf2real
kf3real
kf4real
⊤repre-
sent the true thrust coefﬁcients we wish to solve for and d ∈
R4×1 is a vector where each component di is obtained from (18).
The goal of our optimization is to ﬁnd a solution that matches the
propeller motor dynamics while also being close to our initial
estimate described in (18) without torque mismatch as
min
k
(k −d)⊤(k −d),
s.t. Ak = b.
(19)
Here, A and b are deﬁned as
A =
⎡
⎣
ω2
L11
ω2
L12
ω2
L13
ω2
L14
dxω2
L11
dxω2
L12
−dxω2
L13
−dxω2
L14
−dyω2
L11
dyω2
L12
dyω2
L13
−dyω2
L14
⎤
⎦,
b =

f
M1
M2
⊤,
(20)
where b represents the desired force and moments of the
quadrotor commanded by the nominal control without L1 and
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 08:48:53 UTC from IEEE Xplore.  Restrictions apply.

## Page 5

MAO et al.: FROM PROPELLER DAMAGE ESTIMATION AND ADAPTATION TO FAULT TOLERANT CONTROL: ENHANCING
4301
Fig. 4.
Comparison between estimated damage and true damage with a real-world MAV during a 1.1 m/s ﬂight. Propeller damage is estimated using (17). True
Propeller damage is solved by measuring the coefﬁcient on a thrust bench.
Fig. 5.
Tracking RMSE averaged over 3 axes vs Propeller Damage at hover
with various levels of propeller damage.
ωL1 =

ωL11
ωL12
ωL13
ωL14
⊤are the RPMs from the
combination of L1 and nominal geometric system, dx and dy
represent the distance from the propeller to the center of mass
in the body frame projected on axes b1 and b2 respectively. To
prevent the torque effect from L1 control we remove the fourth
row of our constraints along with M3 (the torque components)
from our optimization. The L1 controller drives the error to
zero between desired and executed action through the use of
supplemental control action [24]. We construct our equality
constraint in(20) torepresent this behaviour wherethereal thrust
coefﬁcients must be consistent with the supplemental action that
generates the desired action. The optimum based on null-space
projection is
k = A⊤
AA⊤−1 (b −Ad) + d.
(21)
Finally, we convert k to percentage form using (15).
E. Fault-Tolerant Transition
We leverage our propeller damage estimate, (21) to deter-
mine when to switch to fault-tolerant control. Our fault-tolerant
control is implemented based on our previous work [21] which
was only tested in simulation. From the qualitative results with
damaged propellers, we set a threshold at 50% damage. Based
on our vehicle’s thrust-to-weight ratio of 2.5:1, we experimen-
tally verify that 50% damage provides a safety margin within
the limit. Once the threshold is met, the system automatically
transitions to the fault-tolerant control per our control design as
shown in Fig. 3.
IV. RESULTS
Our experiments are conducted in a ﬂying space of 10 × 6 ×
4 m3 at the Agile Robotics and Perception Lab (ARPL) at New
York University. The environment is equipped with a Vicon
motion capture system which provides accurate pose estimates
at100 Hz.ThisisfusedwithIMUmeasurementsthroughanUn-
scented Kalman Filter to provide state estimates at 500 Hz. The
robot,basedonourpreviouswork[26],isequippedwithaVOXL
2 ModalAITM and four brushless motors and modiﬁed to obtain
a 2.5 to 1 thrust to weight ratio with total a weight of 700 g. We
set the K such that λ = Diag

0.4
0.4
0.4
0.1
0.1
0.1

.
A. L1 Performance Study
To evaluate the tracking performance, the quadrotor is com-
manded to follow an ellipse of radius 1 m in x, 0.6 m in y,
and 0.1 m in z for each case of propeller damage as well as
under fault-tolerant control with one disabled propeller. The
trajectory is completed with and without L1 adaptive control.
This ellipse is ﬂown at three different speeds: 12, 8, and 5 s
periods. We observe in Table I that the RMSE reduces when
the L1 adaptation is switched on in all cases and has lower
tracking error than fault-tolerant for propeller damages below
40%. We also see in Fig. 5 the position error grows in the L1
Off case as the severity of propeller damage increases while L1
maintains accurate tracking performance despite the degree of
propeller damage. However when the damage reaches greater
than 40%, the error starts becoming too prominent for the
adaptive control to negate. In these cases, transitioning to a
fault-tolerant controller is preferable.
B. Propeller Damage Estimation
The L1 adaptive controller has demonstrated suitability and
robustness to propeller damage compensation. In this section,
we show that Section III-D represents an accurate estimate of
the propeller damage, kfmis, even when the aerial robot is in
motion. To calculate the various levels of propeller damage,
we use a thrust bench to calculate the true thrust coefﬁcient
of the damaged propeller, kfreal and undamaged propeller, kfmodel,
coefﬁcient. We then use (15) to calculate the damage, kfmis. We
test4levelsofpropellerdamagebasedonkfmis:Nodamagerefers
to kfmis = 0%. Low damage refers to kfmis = 20%. Medium
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 08:48:53 UTC from IEEE Xplore.  Restrictions apply.

## Page 6

4302
IEEE ROBOTICS AND AUTOMATION LETTERS, VOL. 9, NO. 5, MAY 2024
Fig. 6.
Simultaneous propeller damage (propellers 2 and 3) for MAV moving 0.5 m/s in a circle. Both PID (green) and L1 (blue) approaches for propeller damage
estimation are shown.
Fig. 7.
Propeller damage estimate of an undamaged vehicle under 3 different experimental conditions. Hover Baseline refers to a hover with no external forces.
Figure Eight refers to ﬂying a trajectory in the shape of an eight with a max velocity of 3 m/s. Hover fan on refers to stabilizing the vehicle under a fan blowing
wind at 3 m/s.
Fig. 8.
Real-world experiments with damage injected to propeller 1. Fault-tolerant transition threshold is set to 50%.
TABLE I
TRACKING RMSE (IN METERS) WHERE kfMIS REPRESENTS THE THRUST LOSS
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 08:48:53 UTC from IEEE Xplore.  Restrictions apply.

## Page 7

MAO et al.: FROM PROPELLER DAMAGE ESTIMATION AND ADAPTATION TO FAULT TOLERANT CONTROL: ENHANCING
4303
Fig. 9.
Position tracking performance after propeller damage is injected in real-world ﬂight. The 80% damage case shows a high yaw rate because it triggers
fault-tolerant control, causing a rapid spin unlike the 30% damage case.
Damage refers to kfmis = 40%. High damage refers to kfmis =
60%. In Fig. 4, we report the estimates of a single damaged
propeller at the aforementioned levels while the quadrotor is
executing an ellipse trajectory with a max speed of 1.1 m/s. This
method is able to estimate the error with an error range of 4%.
In terms of individual actuator forces, this represents 8.3 g of
thrust on a 700 g drone. Next, we estimate dual propeller damage
simultaneously in Fig. 6. We compare two methods for damage
estimation. First, we use L1 complimentary actions shown in
blue. Next, we replace the L1 adaptive control with an integral
term in a PID controller for complimentary action in green.
We substitute ωL1i with the actions generated by an additional
integralcontrollertoestimatethepropellerdamagefollowingthe
same inference and optimization procedure as Section III-D. The
integral term is placed over the velocity expressed in the body
frame. While the integral term can compensate some damage,
it is unsuitable for damage estimation. The L1 complimentary
actions on the other hand can be used to accurately estimate the
propeller’s damage.
Furthermore, we test the effects of medium speed ﬂight
(3 m/s) and external disturbances on our propeller damage
estimation. In Fig. 7, we show the results of 3 experiments.
First, we show a control case where the quadrotor is in hover
without external disturbances and no damages. Second, we show
the same vehicle in hover with 3 m/s wind disturbance. Third,
we show a ﬂight without external disturbances ﬂying at 3 m/s.
Ideally, the desired estimated damage should be 0%. Overall, we
notice that the fan has a signiﬁcant effect on damage estimation
around 20%, but it is not enough to trigger a transition. Medium
speed motions at 3 m/s instead cause minimal but noticeable
deviations from around 0% to ±10%.
C. Fault-Tolerant Transition
We study the rise-time and effectiveness of our transitioning
mechanism by artiﬁcially injecting a fault mid-ﬂight. This fault
is produced by corrupting a motor input to spin slower. In our
experiments, we tested the reliability of our system given 40
trials by injecting 30%, 40%, and 50% damages in a real drone.
30% damage injection has a 100% success rate of not transition
whereas the 50% case shows a 100% successful transitions. The
40% injection has a 87.5% success rate for not transitioning and
a 12.5% false positive transition. Our method did not produce
any false negative.
Additionally, we inject an 80% damage fault in a real-world
experiment to show that our latency is low enough for practical
uses. The damage estimation of the affected propeller rises to
50% in 0.15 s, triggering the transition to fault-tolerant control.
Fig. 8 shows the damage estimation in real-world experiments
with 30%, 50%, and 80% damage injections along with tran-
sition times when relevant. When the fault-tolerant controller
is activated (i.e., > 50% damage cases), we stop the inference
and estimation process. Fig. 9 shows the corresponding position
tracking performances for the non transitioning 30% case and
the transitioning 80% damage case. We see our methodology
can autonomously transition and stabilize the drone despite the
injection of heavy propeller damage. For visualization purposes,
the last values are repeated instead of cut when the inference
stops after the fault tolerant control is triggered.
V. DISCUSSION
The presented results show the beneﬁt of the proposed adap-
tive control scheme for damage estimation and compensation.
However, L1 adaptation can only correct a disturbance if the
actions are within the actuator constraints [24]. Therefore a
switching threshold for adaptive to fault-tolerant control should
reﬂect this constraint. Our system has a 2.5:1 thrust to weight
ratio which enables ﬂight adaptive control with up to 60%
damage without switching to fault-tolerant control. We choose
to use a switching threshold of 50% to allow some safety margin.
For any quadrotor capable of fault-tolerant ﬂight, a 2:1 thrust
to weight ratio minimum is required. Therefore, a conservative
switching threshold of 40% damage can be considered. Research
has shown that L1 adaptive control is effective on a variety of
quadrotors from 27 g Crazyﬂie [27], 70 g Parrot Mambo [15], to
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 08:48:53 UTC from IEEE Xplore.  Restrictions apply.

## Page 8

4304
IEEE ROBOTICS AND AUTOMATION LETTERS, VOL. 9, NO. 5, MAY 2024
our heavy weight platform 700 g along with theoretical guaran-
tees [24]. Our propeller damage estimation method is based on
the steady state adaptive properties of L1 [24], making it equally
generalizable to other platforms.
One limitation of our approach is that we only consider single
or dual propeller damages cases. Damaged propellers in a near
hovering state will spin faster, and undamaged propellers will
spin slower or remain at nominal speeds. A reverse effect in
hover (lower RPMs of damaged propellers) is highly unlikely,
so using the 5% threshold represents a conservative method to
detect propeller damage. Imagine a single damaged propeller
that is spinning clockwise. The damaged propeller must spin
faster to match the original thrust. However, this produces less
torque than the original undamaged propeller creating a yaw
acceleration. In order to counteract this yaw acceleration, the
two counterclockwise propellers will spin slower. The opposite
undamaged clockwise propeller remains consistent with slight
deviations. Thesameprincipleholdsforthecaseoftwodamaged
propellers. In the adjacent case, a counterclockwise and clock-
wise torque both decrease. This results in a cancelling effect
where the more damaged propeller’s opposite will slow down
a constant amount. In the diagonal case, while a similar thrust
can be achieved, the alternative spinning undamaged propellers
must reduce their corresponding speeds to counteract the yaw
acceleration. These actions are handled by our adaption law (11),
and our optimization method is only for damage estimation.
VI. CONCLUSION
In this paper, we presented an adaptive inference and control
strategy to ensure safe quadrotor ﬂight in case of propeller dam-
age. Our approach incorporates an L1 adaptive control technique
in conjunction with a fault-tolerant mode. We propose a method
to quantify propeller damage using L1 adaptation that allows
smooth transitioning to fault tolerant control in the case of severe
damage. The proposed method can effectively account for all
range damages from low to severe levels.
Future works will attempt recovery and estimation during
more aggressive maneuvers [28]. We would also like to see if the
proposed approach can be extended to other thrust curve models,
especially for ﬂight envelopes where the quadratic relation is an
inaccurate approximation.
REFERENCES
[1] M. Idrissi, M. Salami, and F. Annaz, “A review of quadrotor unmanned
aerial vehicles: Applications, architectural design and control algorithms,”
J. Intell. Robot. Syst., vol. 104, no. 2, 2022, Art. no. 22.
[2] G. K. Fourlas and G. C. Karras, “A survey on fault diagnosis and fault-
tolerant control methods for unmanned aerial vehicles,” Machines, vol. 9,
no. 9, 2021, Art. no. 197.
[3] P. Lu and E.-J. van Kampen, “Active fault-tolerant control for quadrotors
subjected to a complete rotor failure,” in Proc. IEEE/RSJ Int. Conf. Intell.
Robots Syst., 2015, pp. 4698–4703.
[4] B. Ghalamchi and M. Mueller, “Vibration-based propeller fault diagno-
sis for multicopters,” in Proc. Int. Conf. Unmanned Aircr. Syst., 2018,
pp. 1041–1047.
[5] S. P. Madruga, T. P. Nascimento, F. Holzapfel, and A. M. N. Lima,
“Estimating the loss of effectiveness of UAV actuators in the presence
of aerodynamic effects,” IEEE Robot. Automat. Lett., vol. 8, no. 3,
pp. 1335–1342, Mar. 2023.
[6] R. C. Avram, X. Zhang, and J. Muse, “Quadrotor actuator fault diagnosis
and accommodation using nonlinear adaptive estimators,” IEEE Trans.
Control Syst. Technol., vol. 25, no. 6, pp. 2219–2226, Nov. 2017.
[7] A. S. Sanca, P. J. Alsina, and J. D. J. F. Cerqueira, “Dynamic modelling
of a quadrotor aerial vehicle with nonlinear inputs,” in Proc. IEEE Latin
Amer. Robot. Symp., 2008, pp. 143–148.
[8] B. A. S. van Schijndel, S. Sun, and C. C. de Visser, “Fast loss of effec-
tiveness detection on a quadrotor using onboard sensors and a Kalman
estimation approach,” in Proc. Int. Conf. Unmanned Aircr. Syst., 2023,
pp. 1–8.
[9] S. S. Alex, A. E. Daniel, and B. Jayanand, “Reduced order extended
Kalman ﬁlter for state estimation of brushless DC motor,” in Proc. 6th
Int. Symp. Embedded Comput. Syst. Des., 2016, pp. 239–244.
[10] A. G. Rot, A. Hasan, and P. Manoonpong, “Robust actuator fault diag-
nosis algorithm for autonomous hexacopter UAVs,” IFAC-PapersOnLine,
vol. 53, no. 2, pp. 682–687, 2020.
[11] Y. Zhong, Y. Zhang, W. Zhang, J. Zuo, and H. Zhan, “Robust actuator fault
detection and diagnosis for a quadrotor UAV with external disturbances,”
IEEE Access, vol. 6, pp. 48169–48180, 2018.
[12] A. Abbaspour, S. Mokhtari, A. Sargolzaei, and K. K. Yen, “A survey on ac-
tive fault-tolerant control systems,” Electronics, vol. 9, 2020, Art. no. 1513.
[13] S. Sun, X. Wang, Q. Chu, and C. D. Visser, “Incremental nonlinear fault-
tolerant control of a quadrotor with complete loss of two opposing rotors,”
IEEE Trans. Robot., vol. 37, no. 1, pp. 116–130, Feb. 2021.
[14] X. Yu, X. Zhou, K. Guo, J. Jia, L. Guo, and Y. Zhang, “Safety ﬂight control
for a quadrotor UAV using differential ﬂatness and dual-loop observers,”
IEEE Trans. Ind. Electron., vol. 69, no. 12, pp. 13326–13336, Dec.
2022.
[15] Z. Wu et al., “L1 adaptive augmentation for geometric tracking con-
trol of quadrotors,” in Proc. IEEE Int. Conf. Robot. Automat., 2022,
pp. 1329–1336.
[16] M. Mühlegg, P. Niermeyer, G. P. Falconi, and F. Holzapfel, “L1 fault
tolerant adaptive control of a hexacopter with control degradation,” in
Proc. IEEE Conf. Control Appl., 2015, pp. 750–755.
[17] M. Li, Z. Zuo, H. Liu, C. Liu, and B. Zhu, “Adaptive fault tolerant
control for trajectory tracking of a quadrotor helicopter,” Trans. Inst. Meas.
Control, vol. 40, no. 12, pp. 3560–3569, 2018.
[18] A. Saviolo, J. Frey, A. Rathod, M. Diehl, and G. Loianno, “Active learning
ofdiscrete-timedynamicsforuncertainty-awaremodelpredictivecontrol,”
IEEE Trans. Robot., vol. 40, pp. 1273–1291, 2024.
[19] F. Crocetti, J. Mao, A. Saviolo, G. Costante, and G. Loianno, “GAPT:
Gaussian process toolkit for online regression with application to learning
quadrotor dynamics,” in Proc. IEEE Int. Conf. Robot. Automat., 2023,
pp. 11308–11314.
[20] A. Loquercio, A. Saviolo, and D. Scaramuzza, “AutoTune: Controller
tuning for high-speed ﬂight,” IEEE Robot. Automat. Lett., vol. 7, no. 2,
pp. 4432–4439, Apr. 2022.
[21] J. Yeom, G. Li, and G. Loianno, “Geometric fault-tolerant control of
quadrotors in case of rotor failures: An attitude based comparative study,”
in Proc. IEEE/RSJ Int. Conf. Intell. Robots Syst., 2023, pp. 4974–4980.
[22] M. W. Mueller and R. D’Andrea, “Stability and control of a quadrocopter
despite the complete loss of one, two, or three propellers,” in Proc. IEEE
Int. Conf. Robot. Automat., 2014, pp. 45–52.
[23] T. Lee, M. Leok, and N. H. McClamroch, “Geometric tracking control of a
quadrotor UAV on SE(3),” in Proc. IEEE 49th Conf. Decis. Control, 2010,
pp. 5420–5425.
[24] M. Khammash, V. Vittal, and C. Pawloski, “Analysis of control perfor-
mance for stability robustness of power systems,” IEEE Trans. Power Syst.,
vol. 9, no. 4, pp. 1861–1867, Nov. 1994.
[25] M. Watterson and V. Kumar, “Control of quadrotors using the hopf
ﬁbration on SO(3),” in Proc. 18th Int. Symp. Robot. Res.. Springer, 2019,
pp. 199–215.
[26] G. Loianno, C. Brunner, G. McGrath, and V. Kumar, “Estimation, control,
and planning for aggressive ﬂight with a small quadrotor with a single
camera and IMU,” IEEE Robot. Automat. Lett., vol. 2, no. 2, pp. 404–411,
Apr. 2017.
[27] K.Huang,R.Rana,G.Shi,A.Spitzer,andB.Boots,“DATT:Deepadaptive
trajectory tracking for quadrotor control,” in Proc. 7th Annu. Conf. Robot
Learn., 2023, pp. 326–340.
[28] J. Mao, S. Nogar, C. M. Kroninger, and G. Loianno, “Robust active
visual perching with quadrotors on inclined surfaces,” IEEE Trans. Robot.,
vol. 39, no. 3, pp. 1836–1852, Jun. 2023.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 08:48:53 UTC from IEEE Xplore.  Restrictions apply.
