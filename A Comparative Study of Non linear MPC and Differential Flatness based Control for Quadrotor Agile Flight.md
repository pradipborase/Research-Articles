# A Comparative Study of Non linear MPC and Differential Flatness based Control for Quadrotor Agile Flight.pdf

## Page 1

1
This paper has been accepted for publication in the
IEEE Transactions on Robotics (T-RO), 2022. ©IEEE
A Comparative Study of Nonlinear MPC and
Differential-Flatness-based Control for Quadrotor
Agile Flight
Sihao Sun, Angel Romero, Philipp Foehn, Elia Kaufmann and Davide Scaramuzza
Abstract—Accurate trajectory-tracking control for quadrotors 
is essential for safe navigation in cluttered environments. How-
ever, this is challenging in agile flights d ue t o n onlinear dynam-
ics, complex aerodynamic effects, and actuation constraints. In 
this article, we empirically compare two state-of-the-art control 
frameworks: the nonlinear-model-predictive controller (NMPC) 
and the differential-flatness-based controller (DFBC), by tracking 
a wide variety of agile trajectories at speeds up to 20 m/s (i.e., 
72 km/h). The comparisons are performed in both simulation 
and real-world environments to systematically evaluate both 
methods from the aspect of tracking accuracy, robustness, and 
computational efficiency. W e s h ow t h e s u periority o f  N M PC in 
tracking dynamically infeasible trajectories, at the cost of higher 
computation time and risk of numerical convergence issues. For 
both methods, we also quantitatively study the effect of adding 
an inner-loop controller using the incremental nonlinear dynamic 
inversion (INDI) method, and the effect of adding an aerodynamic 
drag model. Our real-world experiments, performed in one of 
the world’s largest motion capture systems, demonstrate more 
than 78% tracking error reduction of both NMPC and DFBC, 
indicating the necessity of using an inner-loop controller and 
aerodynamic drag model for agile trajectory tracking.
MULTIMEDIA MATERIAL
Code: https://agilicious.dev/
Video: https://youtu.be/SEZJ-OIR8Bo
I. INTRODUCTION
A. Motivation
Quadrotors are extremely agile. Exploiting their agility is
crucial for time-critical missions, such as search and rescue,
monitoring, exploration, aerial delivery, drone racing, recon-
naissance, and even flying cars [1, 2]. An accurate trajectory-
tracking controller is required to safely execute high-speed
trajectories in cluttered environments. However, most ap-
proaches struggle to handle joint effects in agile flights, such as
nonlinear dynamics, aerodynamic effects, and actuation limits.
Recently, nonlinear model predictive control (NMPC) has
drawn much attention for quadrotor control thanks to advances
in hardware and algorithmic efficiency [3–11]. NMPC par-
ticularly excels in handling control limits, and its predictive
nature is believed to be beneficial for trajectory tracking at high
All authors are with the Robotics and Perception Group, University of
Zurich, Switzerland (http://rpg.ifi.uzh.ch). This work was supported by in part
by the National Centre of Competence in Research (NCCR) Robotics, through
the Swiss National Science Foundation (SNSF), in part by the European
Union’s Horizon 2020 Research and Innovation Programme under grant agree-
ment No. 871479 (AERIAL-CORE), and in part by the European Research
Council (ERC) under grant agreement No. 864042 (AGILEFLIGHT).
Fig. 1: Top: Our quadrotor tracking a race trajectory. Bottom:
Box plot comparing the position tracking root-mean-square-error
(RMSE) of NMPC, DFBC, and their variations with INDI inner-
loop, with or without considering aerodynamic drag effects. For each
method, data are collected from real-world flights tracking different
reference trajectories with speeds up to 20 m/s (i.e., 72 km/h) and
accelerations up to 5g.
speeds [3]. A recent study has demonstrated its performance
in tracking aggressive trajectories up to 20 m/s [4].
However, NMPC is computationally extremely demanding
compared to the state-of-the-art non-predictive method: the
differential-flatness-based controller (DFBC) [12, 13]. This
method also shows great potential in accurately tracking agile
trajectories autonomously. A recent study has used DFBC to
track trajectories up to 12.9 m/s with 2.1 g accelerations, with
only 6.6 centimeters position tracking error [13]. Although the
state-of-the-art DFBC has not achieved agile flights as fast as
NMPC showed in [4], its high computational efficiency and
tracking accuracy render the necessity of applying NMPC for
agile trajectory tracking questionable. Therefore, a compara-
tive study of NMPC and DFBC is needed to provide insights
for future research on fully autonomous agile flights, in order
to further improve their efficiency and reliability.

## Page 2

2
B. Contribution
This article presents the first comparative study of the
two state-of-the-art tracking controllers: NMPC and DFBC
method, in fast trajectory tracking with speed up to 20 m/s
(i.e., 72 km/h) and 5 g accelerations. Specifically, we select
the NMPC method that uses the full nonlinear dynamics
with proper actuator bounds and regards single rotor thrusts
as control inputs. This NMPC has been applied in previous
works, such as [3, 5]. For a fair comparison, we improve
the DFBC method used in [12, 13] with a control allocation
approach using constrained quadratic programming [14] also
to consider control input limits.
All experiments are conducted in both simulations and the
real world. The simulations compare in both ideal and practical
conditions with model-mismatch, estimation latency, and ex-
ternal disturbances. The real-world experiments are conducted
in one of the world’s largest motion capture systems, with
30×30×8 m3 flight volume. Multiple agile trajectories are
selected as reference, including not only dynamically feasible
trajectories, but also dynamically infeasible trajectories that
require thrusts exceeding the maximum capacity of the quadro-
tor motors, which is likely to happen in high-speed flights due
to model mismatch. These tests investigate the performance
of both methods in the presence of significant high-speed-
induced aerodynamic effects, inevitable system latency, and
on an onboard embedded computer.
The experimental results reveal that NMPC is considerably
more computationally demanding, and more prone to suffer
from numerical convergence issues in the presence of large
external force disturbances. However, NMPC also excels in
tracking dynamically infeasible trajectories, making it more
suitable for tracking time-optimal trajectories that violate the
rotor thrust constraints.
In addition, this study also highlights the importance of im-
plementing an inner-loop controller for robustification. Specif-
ically, we select the incremental nonlinear dynamic inversion
(INDI) method as the inner-loop angular controller, thanks
to its simplicity in implementation and demonstrated robust-
ness in various real-world experiments [15, 16] including a
combination with DFBC [13]. As for NMPC, differently from
the state-of-the-art using a PID as the low-level control [4],
we propose a method to hybridize NMPC with INDI that
considers the real input limits of the quadrotor instead of con-
straints on virtual inputs. Real-world flight results demonstrate
more than 78% position tracking error reduction of NMPC
and DFBC with an INDI inner-loop. We also reveal that a
well-selected inner-loop controller is more crucial than simply
considering the aerodynamic effects, as is compared in Fig. 1.
Apart from the technical contribution, this paper can also be
regarded as a tutorial for non-expert readers on agile quadrotor
flight. We encourage the practitioners to use the presented
results as a baseline for further development of both DFBC
and NMPC approaches.
II. RELATED WORK
In this paper, we classify the trajectory tracking controller
into two categories: non-predictive and predictive methods.
While the predictive methods encode multiple future time-
steps into the control command, the non-predictive methods
only track a single reference step. In the following, we
review works towards improving quadrotor trajectory tracking
accuracy from these two different categories. A more com-
prehensive survey of quadrotor position and attitude control
methods can be found in the literature (e.g., see [17, 18]).
A. Non-predictive Quadrotor Trajectory Tracking Control
Unlike most fixed-wing aircraft, quadrotors are inherently
unstable. Therefore, the initial work of quadrotor control
aimed at achieving stable hovering and near-hover flights.
Thanks to the small-angle assumptions in these conditions,
linear control methods such as PID and LQR demonstrate
sufficiently good performance (see, e.g., [19, 20]).
However, as the requirements for agile flight emerges, these
assumptions are no longer valid. Nonlinearities from the atti-
tude dynamics are the first problem to tackle. For this reason,
nonlinear flight controllers are proposed, such as feedback
linearization [21] and backstepping [22]. In order to cope
with the singularities of Euler angles as the nonlinear attitude
representation, quaternions are widely adopted to parametrize
the attitude [23]. In addition, the authors of [24] propose the
geometric tracking controller to directly control the quadrotor
on the manifold of the special Euclidean group SE(3), showing
almost globally asymptotic tracking of the position, velocity,
and attitude of the quadrotor.
A seminal work [25] reveals that quadrotors are differ-
entially flat systems. By virtue of this property, given the
time-parameterized 3D path, one can derive the reference
attitude, angular rate, and accelerations. These references can
be sent to a closed-loop flight controller as feedforward terms,
while additional feedback control is required to address model
mismatch and external disturbances. As such, differential-
flatness based controller (DFBC) has significantly improved
the tracking performance at relatively high speeds [12, 13].
As the flying speed increases, a quadrotor starts experienc-
ing non-negligible aerodynamic effects, including drag [26],
aerodynamic torque [27], and variation of thrusts [28]. Authors
of [12] show that the aerodynamic drag does not affect the
differential flatness of a quadrotor. Thus they adopt a first
order aerodynamic model with feedforward terms derived from
the reference trajectory to improve the tracking performance.
Since an accelerometer can directly read external forces, [13]
leverages accelerometer measurements to improve the tracking
accuracy instead of resorting to an aerodynamic drag model.
This method also demonstrates remarkable performance in
disturbance rejection and platform adaptability.
Effectively handling control input limits is a remaining
challenge for non-predictive methods, including DFBC. So far,
existing methods have prioritized the position tracking over
heading using various approaches, such as redistributed pseudo
inversion [29], weighted-least-square allocation [30], control-
prioritization method [31, 13], and constrained-quadratic-
programming allocation [32]. While these methods can mit-
igate the actuator saturation effect when the trajectories are
dynamically feasible, its performance in tracking dynamically

## Page 3

3
infeasible trajectories is still questionable. In this work, we will
push the limit of DFBC to conduct agile trajectory tracking
tasks to a much higher flight speed and acceleration than
the state-of-the-art, and study its performance in tracking
dynamically infeasible trajectories where violating rotor thrust
limits becomes inevitable.
B. Model Predictive Control for Quadrotor Trajectory Track-
ing
Model predictive control (MPC) is a prevalent method in
robots thanks to its predictive nature and ability to handle input
constraints[10, 33]. It generates control commands in receding
horizon fashion, which minimizes the tracking error in the
predicted time horizon by solving constrained optimization
problems.
However,
MPC
is
very
computationally
demanding
compared with non-predictive methods. Especially, using
nonlinear-MPC (NMPC) with a full-state nonlinear model of
a quadrotor was computationally intractable onboard early-
age unmanned-aerial vehicles (UAVs). For this reason, linear-
MPC (LMPC) is adopted in many studies for only position
control [34], or control linearized model based on small-
angle assumptions [35]. Therefore, these LMPC methods
cannot fully capture nonlinearities in rotational dynamics, and
underperforms NMPC methods [10, 33]
Separating flight controllers into high-level position control
and low-level attitude control is another common approach
to simplify the model and alleviate the computational load
of NMPC [6, 7, 9]. However, in such a cascaded control
architecture, the high-level controller cannot precisely capture
the real quadrotor capability because they often ignore the
effects of system limitation (such as [6]), or introduce a virtual
constraint on states [9]. Consequently, the command fed into
the lower-level controller is either too conservative to achieve
agile flights, or over-aggressive that causes instability.
Thanks to the recent development in hardware and nonlinear
optimization solvers [36–38], running NMPC with a nonlinear
full dynamic model becomes computationally tractable on an
embedded computer. Hence, recently, some studies start using
the full-nonlinear dynamic model, and regarding single rotor
thrusts as inputs for NMPC, thus are able to fully exploit
quadrotors capability [3–5]. These methods either directly
use the optimized single rotor thrust commands [3], or send
intermediate states from the solution (such as the angular rates)
to a low-level controller [4, 5]. A recent study [4] demonstrates
the ability of the full-model NMPC with a PID low-level
controller in tracking a pre-planned race trajectory at speed up
20 m/s which surpasses the top speed of 12.9 m/s reported
in [13] using DFBC, in spite of a much larger tracking error
(0.7 m v.s. 0.066 m).
Although running NMPC is realizable on modern embedded
computers, it still requires significantly more computational
resources than non-predictive methods represented by DFBC.
For this reason, NMPC may suffer from numerical conver-
gence issues, especially when the platform lacks a sufficient
computational budget. Moreover, the advantage of NMPC be-
comes questionable as DFBC can also address input limits us-
ing the control allocation technique and generate feedforward
Fig. 2: Coordinate definitions and propeller numbering convention.
control leveraging differential-flatness property. Therefore, it is
necessary to compare these two methodologies and understand
at what conditions each approach is preferable to provide
insights and recommendations for future applications.
III. PRELIMINARIES
A. Notations
Throughout the paper, we use subscription r to indicate
the reference variables derived from the reference trajectory.
Subscription d indicates the desired value, which is calculated
from a higher-level controller. We use bold lowercase letters
to represent vectors and bold uppercase letters for matri-
ces; otherwise, they are scalars. Two right-handed coordinate
frames are used in this paper: they are the inertial-frame FI :
{xI, yI, zI} with zI pointing upward opposite to the gravity,
and the body-frame FB : {xB, yB, zB} with xB pointing
forward and zB aligned with the collective thrust direction
(see Fig. 2). Vectors with superscription B are expressed in the
body-frame; others without any superscription are expressed
in the inertial-frame. The rotation from FI to FB is repre-
sented by rotational matrix R(q) = [xB, yB, zB] ∈SO(3)
parameterized by quaternion q = [qw, qx, qy, qz]T ∈S3. We
use subscript {x, y, z} to represent the imaginary components
of a quaternion, namely qx,y,z = [qx, qy, qz]T . Operator
diag(A1, A2, ..., An) denotes a diagonal matrix with scalars
or matrices (A1, A2, ..., An) as diagonal entries.
B. Quadrotor Model
1) Quadrotor Rigid-Body Model: The quadrotor model is
established using 6-DoF rigid body kinematic and dynamic
equations. For translational dynamics, we have
¨ξ = (TzB + f a)/m + g,
(1)
where ξ denotes the position of the quadrotor center of gravity
(CoG); T and m are the collective thrust and total mass
respectively; g ∈is the gravitational vector; f a indicates the
exogenous aerodynamic drag force during high-speed flights.
The rotational kinematic and dynamic equations are ex-
pressed as
˙q = 1
2q ⊗

0
ΩB

,
(2)
Iv ˙Ω
B = IvαB = −ΩB × IvΩB + τ + dτ,
(3)
where ⊗denotes the quaternion multiplication operator. Ωis
the angular velocity of FB with respect to FI. Its derivative,

## Page 4

4
namely angular acceleration, is denoted by α . Throughout
the paper, we use its projection on FB, namely ΩB
=
[Ωx, Ωy, Ωz]T , since its directly measurable from the inertial
measurement unit (IMU). Iv indicates the inertia matrix of the
entire quadrotor. τ is the resultant torque generated by rotors.
dτ is the model uncertainties on the body torque, which can
come from high-order aerodynamic effects, center of gravity
bias, or distinction among rotors.
The collective thrust and rotor generated torques are func-
tions of rotor speeds:

T
τ

= G1u + G2 ˙ω + G3(Ω)ω
(4)
where
u = ctω◦2
(5)
represents the thrust generated by each rotor and ◦indicates the
Hadamard power. ct is the thrust coefficient. ω is the vector of
angular rates of each propeller. G1 to G3 are matrices defined
as
G1 =


1
1
1
1
l sin β
−l sin β
−l sin β
l sin β
−l cos β
−l cos β
l cos β
l cos β
cq/ct
−cq/ct
cq/ct
−cq/ct


(6)
G2 =


0
0
0
0
0
0
0
0
0
0
0
0
Ip
−Ip
Ip
−Ip


(7)
G3 =


0
0
0
0
IpΩy
−IpΩy
IpΩy
−IpΩy
−IpΩx
IpΩx
−IpΩx
IpΩx
0
0
0
0


(8)
where cq is the torque coefficient; β and l are geometric
parameters defined as per Fig. 2. Ip is the inertia of the rotor
around zB.
Terms G2 ˙ω and G3(Ω)ω are torques respectively due
to angular acceleration of rotors and gyroscopic effects,
which are usually neglected for controller design. However,
in Sec IV-C, we will revisit the INDI method [13] for angular
acceleration control that takes into account effects of the
inertial torque term G2 ˙ω.
2) Aerodynamic Drag Model:
Quadrotors during high-
speed flight experience significant aerodynamic drag forces,
which need to be precisely modeled to improve tracking
accuracy while minimizing the computational overhead. In this
work, we use an aerodynamic drag model which captures the
major effects, and is proved effective in works such as [12].
f B
a =


−kd,xvx
−kd,yvy
−kd,zvz + kh
v2
x + v2
y



(9)
where [vx, vy, vz] = R(q)T ˙ξ (i.e., the projection of velocity
in the body frame; here we assume zero wind-speed). kd,x,y,z
and kh are positive parameters can be identified from flight
data.
IV. METHODOLOGIES
This section elaborates the two control methods compared.
A nonlinear NMPC method is selected that considers the thrust
limits of each rotor, the full nonlinear dynamics, and the
aerodynamic effects. As for the DFBC method, we improve
the state-of-the-art such that these factors are also addressed,
which ensures a fair comparison with NMPC. Finally, both
methods are augmented with an INDI controller [15] to convert
the single rotor thrust commands to rotor-speed commands,
while improving the robustness against model uncertainties
and disturbances on the rotational dynamics. The control
diagrams of both methods are illustrated in Fig. 4 and Fig. 3.
A. Nonlinear Model Predictive Controller
NMPC generates control commands by solving a finite-time
optimal control problem (OCP) in a receding horizon fashion.
Given a reference trajectory, the cost function is the error
between the predicted states and the reference states in the time
horizon, meaning that multiple reference points in the time
horizon are used. In order to conduct numerical optimizations,
we discretize the states and inputs into N equal intervals over
the time horizon τ ∈[t, t + h] of size dt = h/N with h
denoting the horizon length, yielding a constrained nonlinear
optimization problem:
uNMPC = argmin
u
N−1
X
k=0
||xk −xk,r||Q + ||uk −uk,r||Qu

+ ||xN −xN,r||QN
s.t.
xk+1 = f(xk, uk),
x0 = xinit,
ΩB ∈
h
ΩB
min ΩB
max
i
,
u ∈[umin umax] ,
(10)
Note that, we use the thrust of rotors u defined in (4) and (5)
as the control input of NMPC. The state vector is defined as
x =
h
ξ ˙ξ q ΩBi
, and
Q = diag
Qξ, Qv, Qq, QΩ

, QN = Q
(11)
The reference state vector xr and input ur can be obtained
from a trajectory planner which generates full states such
as the one introduced in [4]. Function f (xk, uk) is the
discretized version of nonlinear quadrotor model (1)-(5). The
same as many other works (see, e.g., [3, 39]), we omit G2
and G3 related terms in (4) as their effects are negligible.
xinit is the current state estimation when solving the OCP.
umin and umax are minimum and maximum values of motor
thrusts. Constraints on angular velocities are also added, which
is found beneficial for improving the stability of NMPC
according to [5]. Note that in the above optimization problem,
the following abuse of notation is used when calculating
quaternion error:
q −qr =
q ⊗q−1
r

x,y,z
(12)
The above NMPC solves the full nonlinear model of a
quadrotor, instead of resorting to a cascaded structure, or linear
assumptions. In this paper, this quadratic nonlinear optimiza-
tion problem is solved by a sequential quadratic programming

## Page 5

5
(SQP) algorithm executed in a real-time iteration scheme [40].
We implement this algorithm using ACADO [41] toolkit with
qpOASES [42] as the solver. More implementation details are
given in Sec. V.
B. Differential-Flatness Based Controller
Quadrotors are differentially flat systems [25], namely, all
the states and inputs can be written as algebraic functions
of the flat outputs and their derivatives. This allows a direct
mapping from the flat outputs (positions ξ and heading ψ)
to the angular rates and angular accelerations, which are
leveraged by DFBC as feed-forward terms to improve the
tracking accuracy.
In the following, we introduced the DFBC method improved
from a previous work [25], where the original geometric atti-
tude controller is replaced by the tilt-prioritized method [31].
We also use the quadratic-programming based control allo-
cation [14] to address input constraints. These modifications
are beneficial in tracking dynamically infeasible trajectories,
as will be discussed in Sec. VI-D. Fig. 4 presents an overview
of this method.
1) Desired Attitude and Collective Thrust: First of all, we
calculate the desired acceleration from a PD controller:
¨ξd = Kξ (ξr −ξ) + Kv

˙ξr −˙ξ

+ ¨ξr
(13)
where Kξ and Kv are positive-definite diagonal gain matri-
ces. Then from (1) and (9), the desired thrust Td and thrust
direction zB,d are obtained as
TdzB,d =

¨ξd −g

m −R(q)f B
a
(14)
Given reference heading angle ψr, we get an intermediate
axis xC,d, by which the desired attitude can be obtained by
the following equations:
xC,d = [cos ψr, sin ψr, 0]T ,
(15)
yB,d =
zB,d × xC,d
||zB,d × xC,d||,
(16)
R(qd) = [xB,d, yB,d, zB,d].
(17)
where qd is the desired attitude expressed by the quaternion.
2) Reference Angular Velocity and Acceleration: We lever-
age the differential flatness property of a quadrotor to derive
the reference angular velocity and angular accelerations. Using
them into the attitude control can help in tracking jerk and snap
(3rd and 4th order derivatives of position ξ), which is found
beneficial to the tracking performance [13].
Taking the derivative of both sides of (1) and assuming a
constant external aerodynamic force f a, we have
m
...
ξ = ˙TzB + TΩ× zB.
(18)
Then given reference jerk
...
ξ r and substitute it for
...
ξ in (18),
we get
hΩ≜Ω× zB = (m
...
ξ r −˙TzB)/T,
(19)
by which the reference angular velocity can be obtained as
ΩB
r =
h
−hΩ· yB,
hΩ· xB,
˙ψrzI · zB
iT
,
(20)
where ψr is the reference heading angle.
We further take the derivative on both sides of (18) and uses
snap reference
....
ξ r to replace
....
ξ , yielding
hα ≜˙Ω× zB
= m
T
....
ξ r −
 
Ω× (Ω× zB) + 2 ˙T
T Ω× zB +
¨T
T zB
!
.
(21)
Then the desired angular acceleration can be obtained as
αB
r =
h
−hα · yB,
hα · xB,
¨ψrzI · zB
iT
.
(22)
Note that in (20) to (22) we use the current attitude
{xB, yB, zB}, angular velocity Ω, and collective thrust T
instead of their references. Hence, the drone still follows the
reference jerk
...
ξ r and snap
....
ξ r even though its attitude,
angular rates, and collective thrust have been deviated from
the reference.
Above derivations for ΩB
r and αB
r need the value of col-
lective thrust T and its derivatives. While T can be calculated
from (4)(5) with measured rotor speed ω, its derivatives ( ˙T
and ¨T) are unable to be directly measured. For this reason, we
approximate them by using reference jerk
...
ξ r and snap
....
ξ r.
Multiplying (dot-product) both sides of (18) by zB, we have
˙T = m
...
ξ r · zB
(23)
and its derivative
¨T = m
....
ξ r · zB + m(Ω× zB) ·
...
ξ r.
(24)
Equation (23) and (24) are then substituted into (18)-(22) to
calculate ΩB
r and αB
r .
3) Tilt-Prioritized Attitude Control: Quadrotors use rotor
drag torques to achieve heading control. The control effective-
ness of heading is around one order of magnitude lower than
pitch and roll. As a consequence, heading control is prone to
cause motor saturations. Fortunately, the thrust orientation of
a quadrotor (namely tilt) is independent of its heading angle.
Thus tilt-prioritized control has been proposed in [31] that
regulates the reduced-attitude (pitch and roll) error ˜qe,red and
yaw error ˜qe,yaw separately as follows:
[qe,w, qe,x, qe,y, qe,z]T = qd ⊗q−1,
(25)
˜qe,red =
1
q
q2e,w + q2e,z


qe,wqe,x −qe,yqe,z
qe,wqe,y + qe,xqe,z
0

,
(26)
˜qe,yaw =
1
q
q2e,w + q2e,z
[0
0
qe,z]T .
(27)
Subsequently, the desired angular acceleration can be obtained
by the following attitude control law:
αB
d = kq,red˜qe,red + kq,yawsgn(qe,w)˜qe,yaw
+ KΩ(ΩB
r −ΩB) + αB
r
(28)
where kq,red and ke,yaw are positive gains for reduced-attitude
and yaw control respectively. Setting a relatively high kq,red

## Page 6

6
Nonlinear
MPC
(10)
INDI
(32)-(35)
Fig. 3: The control diagram of the model predictive controller with an INDI inner-loop controller.
PD Controller
(13)
Thrust vector
decomposition
(14) - (17)
Tilt-prioritized 
attitude controller
(25) - (28)
QP-based
Control 
allocation
(31)
Differential
flatness 
(18) - (24)
INDI
(32)-(35)
Thrust Estimation
(4)(5)
Fig. 4: The control diagram of the differential-flatness-based controller, combined with an INDI inner-loop controller.
over ke,yaw is helpful in improving position tracking accuracy
while preventing input saturations. αB
r in (28) performs as
a feed-forward term. It is worth noting that, the inclusion of
αB
r seems to be reasonable from a theoretical perspective [31],
although removing it has been found to have almost no effect
in our real-world experiments.
4) Quadratic-Programming-Based Control Allocation: The
control allocation module generates thrust commands of each
individual rotor from desired collective thrust Td and angular
acceleration αB
d . The same as NMPC, we also neglect the G2
and G3 terms in (4). Then from (3) and (4), we obtain the
direct-inversion control allocation:
u = G−1
1

Td
IvαB
d + ΩB × IvΩB

,
(29)
uDFBC = max (umin, min(u, umax))
(30)
This, however, does not consider input limits and may cause
loss of control. For instance, an excessive collective thrust
command can saturate all motors and consequently disable
the attitude control.
An effective alternative to address saturations is the
quadratic-programming based allocation that solves the fol-
lowing optimization problem:
uDFBC = argmin
u


Td
IvαB
d + ΩB × IvΩB

−G1u

W
s.t.
u ∈[umin umax] ,
(31)
where W
∈R4×4 is a positive-definite diagonal weight
matrix. Each diagonal entry respectively indicates the weight
on the thrust, pitch, roll and yaw channels. Generally, setting
a relatively high weight on pitch and roll (see Table. I) is
advantageous to prevent quadrotor loss-of-control when motor
saturations are inevitable (e.g., tracking dynamically infeasible
trajectories). If the solution is originally within control bounds,
the result is the same as the direct-inversion allocation from
(30). As for the implementation details, we solve this quadratic
programming problem using an Active-Set Method from the
qpOASES solver [42].
C. Incremental Nonlinear Dynamic Inversion
After obtaining thrust commands from (10) or (31), one can
use (5) to directly obtain the rotor speed command. However,
the above-mentioned controllers neglects the unmodeled term
dτ in the rotational dynamics (3), which are found detrimental
to the overall control performance.
Modeling dτ is very challenging for real-world systems.
Therefore, we resort to incremental nonlinear dynamic inver-
sion (INDI), a sensor-based controller that uses instantaneous
sensor measurement, instead of an explicit model, to represent
system dynamics, thus being robust against model uncertain-
ties and external disturbances. The performance and robustness
of INDI have been demonstrated in previous research (see,
e.g., [15, 13, 16]) with proven stability [43].
We use INDI as the inner-loop controller of both NMPC and
DFBC for fair comparisons. The hybridization of INDI and
DFBC is similar to a related work [13], except for the attitude
controller and control allocation introduced in the previous
section. Here, a method is proposed to effectively combine
INDI with NMPC to improve its robustness against rotational
model uncertainties.
After knowing the single rotor thrust command uDFBC
or uNMPC from (31) and (10) respectively, we can retrieve

## Page 7

7
the desired collective thrust, and desired angular acceleration
using (3) and (4), yielding

ˆTd
Iv ˆαB
d + ΩB × IvΩB

= G1uDFBC/NMPC.
(32)
Note that, for the DFBC method, ˆTd and ˆαB are different from
those derived from (14) and (28) if the optimal cost of (31)
is non-zero. Then from INDI, we can get the desired body
torque (see (30) and (31) of [13] for detailed derivations)
τ d = τ f + Iv

ˆαB
d −˙Ω
B
f

(33)
Hence, the effect of unmodeled dτ is captured by filtered
angular acceleration measurement ˙Ω
B
f and filtered body torque
τ f, where
τ f = ¯G1ω◦2
f + ∆t−1 ¯G2 (ωf −ωf,k−1)
(34)
is calculated from rotor speed measurements. ΩB
f and ωf are
low-pass filtered body-rate and rotor speeds with the same
cut-off frequencies. Thus they have a similar amount of delay
and can be synchronized. In this paper, we use a second-order
Butterworth filter with a 12 Hz cut-off frequency. Note that we
use subscript k −1 to indicate the last sampled variable, and
∆t is the sampling interval. ¯G1 and ¯G2 respectively indicate
matrices formed by the last three rows of G1 and G2.
Then from (14), the following equation is obtained to solve
rotor speed command ωc:
 ˆTd
τ d

= G1ω◦2
c + ∆t−1G2 (ωc −ωc,k−1) ,
(35)
with the only unknown ωc which can be solved numerically.
Differently from [13], the motor time constant is not needed
in (35).
The INDI inner-loop controller converts the original thrust
inputs from the high-level controller to rotor speed commands.
Because this conversion is through algebraic equations, system
delay typically seen in the cascaded control structures can be
effectively circumvented. The advantage of INDI over classical
PID inner-loop controller will be demonstrated in Sec. VII.
V. IMPLEMENTATION DETAILS
Before elaborating on the simulation and real-world ex-
periments, we introduce the implementation details and ex-
perimental setups. Both NMPC and DFBC flight controllers
are implemented in an open-sourced flight stack Agili-
cious [44] programmed in C++, with ACADO [41] toolkit
and qpOASES [42] as external libraries. A wrapper in ROS
environment is also written which allows data logging, inter-
facing, and network communication. The controller gains are
listed in Table I and the inertial and geometric parameters of
the tested quadrotor are listed in Table II. These parameters
are used for both simulation and real-world experiments.
In the simulation experiments, the flight software runs on
a laptop at 300 Hz while the frequency of NMPC is limited
to 100 Hz for consistency with the real-world experiments.
The rotor speed command is sent to a simulator included
in Agilicious that uses a 4th-order Runge-Kutta integrator to
propagate quadrotor dynamic equations (1)-(4) at 500 Hz. To
simulate the motor dynamics, rotor speed commands generated
by the controllers pass through a low-pass filter with a 30 ms
time constant. The drag model (9) is also included to study the
effect of aerodynamics, of which the parameters are included
in Table II. The quadrotor states from the simulator are directly
fed into the controllers unless a dedicated state estimation error
is simulated.
The real-world experiment is performed in an indoor arena
equipped with a motion capture system (VICON), with a
30 × 30 × 8 m3 tracking volume, as is shown in Fig. 1.
The flight software runs at 300 Hz on an onboard NVIDIA
Jetson TX2 embedded computer. It includes the control algo-
rithms (DFBC/NMPC and INDI inner-loop), and an extended
Kalman filter fusing VICON (400 Hz) and IMU measurements
(500 Hz) to obtain the full-state estimates. While DFBC runs
at 300 Hz, the frequency of NMPC is limited to 100 Hz due to
its computational complexity. The INDI inner-loop also runs at
300 Hz no matter which controller is being used. The onboard
computer sends rotor speed commands of individual rotors
to a low-level RadixFC board. The latter runs a customized
firmware based on the open-source NuttX real-time operating
system at 500 Hz to perform closed-loop rotor speed control,
and sends rotor speed and IMU measurements to the onboard
computer. We refer the users to Agilicious for more details
about the hardware.
TABLE I: Controller gains and parameters
NMPC
DFBC
Qξ
diag(200, 200, 500)
Kξ
diag(10, 10, 10)
Qv
diag(1, 1, 1)
Kv
diag(6, 6, 6)
Qq
diag(5, 5, 200)
kqx, kqy, kqz
150, 150, 3
QΩ
diag(1, 1, 1)
KΩ
diag(20, 20, 8)
Qu
diag(6, 6, 6, 6)
W
diag(0.001, 10, 10, 0.1)
dt
50 ms
N
20
TABLE II: Quadrotor Configurations
Parameter(s)
Value(s)
m
[kg]
0.75
l
[m]
0.14
β
[deg]
56
Iv
[gm2]
diag(2.5, 2.1, 4.3)
(umin, umax)
[N]
(0, 8.5)
cq
[Nm2]
2.37e−8
ct
[N2]
1.51e−6
kd,x, kd,y, kd,z

[kg/s]
(0.26, 0.28, 0.42)
kh
[kg/m]
0.01
VI. SIMULATION EXPERIMENTS
In a set of controlled experiments in simulation, we examine
DFBC and NMPC to address the following research questions:
(i) Given the computational budget and a well-identified
model, which control approach achieves better tracking perfor-
mance? (ii) How do these two approaches perform in tracking
dynamically infeasible trajectories, which inevitably lead to
actuator saturation? (iii) How do these two approaches perform
in simulated practical situations with a model mismatch,
external disturbances, state estimation latency? Note that in
this section, both methods are tested with the augmentation of
the INDI inner-loop controller. In this section, we use NMPC

## Page 8

8
and DFBC to represent those with INDI and an aerodynamic
drag model for readability.
A. Reference Trajectories
Multiple elliptical reference trajectories on both horizontal
and vertical planes are generated for testing the tracking
performance. The results of tracking these simple trajectory
primitives can further reflect the performance of tracking more
complex 3D trajectories. These trajectories are parameterized
by the maximum velocity Vmax, maximum acceleration amax,
and ellipticity n. Specifically, the horizontal reference trajec-
tories are expressed as:
ξr(t) = [rmax sin(kt), rmin cos(kt), 5]T ;
(36)
and the vertical reference trajectories are
ξr(t) = [rmax sin(kt), 0, 5 + rmin cos(kt)]T
(37)
where
rmax = V 2
max/amax, k = amax/Vmax, rmin = rmax/n. (38)
The heading angle of each horizontal reference trajectory is
selected to always point at the center of the ellipse; for vertical
trajectories, the reference heading angles are kept constant.
Specifically, 144 reference trajectories are generated by com-
bining parameters amax ∈{10, 20, 30, 40, 50, 60} m/s2,
Vmax ∈{5, 10, 15, 20} m/s, n ∈{1, 2, 5}.
Tracking some of these trajectories may require the quadro-
tor to exceed its thrust limitations. These trajectories are
referred to as dynamically infeasible. In many time-critical
applications, such as autonomous drone racing, rotors need to
reach their full thrust limits to fully exploit the agility of the
platform and achieve faster lap times. Designing such an agile
time-optimal trajectory requires a perfect model that captures
real thrust limits and aerodynamic effects in high-speed flights.
Without this model, the generated trajectory may exceed the
quadrotor capabilities and becomes dynamically infeasible to
accurately follow. Since such an accurate model is usually
unattainable, studying the performance when tracking these
infeasible trajectories is necessary.
For the simulated quadrotor with the configurations given
in Table II, there are 68 infeasible trajectories and 76 feasible
trajectories. They are determined by being tracked by a modi-
fied NMPC without thrust limits imposed. If the applied thrust
exceeds the maximum thrust of the real drone, the trajectory
is marked as infeasible. The feasibility of each reference
trajectory is given in Table III
B. Evaluation Criteria
In the following comparisons, we use the root mean square
error (RMSE) of position and heading as the precision metric
of a method. The crash rate is another criterion to show the
robustness of a method. A certain flight is defined as crashed
if its position ξ violates the following spatial constraint at an
arbitrary instant:
inf{ξr(t)} −b ≤ξ ≤sup{ξr(t)} + b.
(39)
We select b = [5, 5, 5]T meters in this study.
TABLE III: Dynamical feasibility of reference trajectories. (feasi-
ble:✓; infeasible:✗)
(a) Horizontal trajectories.
amax
[m/s2]
n = 1
n = 2
n = 5
Vmax [m/s]
Vmax [m/s]
Vmax [m/s]
5
10
15
20
5
10
15
20
5
10
15
20
10
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
20
✓
✓
✓
✓
✓
✓
✓
✓
✗
✓
✓
✓
30
✓
✓
✓
✓
✗
✓
✓
✓
✗
✗
✓
✓
40
✓
✓
✓
✓
✗
✓
✓
✓
✗
✗
✗
✓
50
✗
✗
✗
✗
✗
✗
✗
✗
✗
✗
✗
✗
60
✗
✗
✗
✗
✗
✗
✗
✗
✗
✗
✗
✗
(b) Vertical trajectories.
amax
[m/s2]
n = 1
n = 2
n = 5
Vmax [m/s]
Vmax [m/s]
Vmax [m/s]
5
10
15
20
5
10
15
20
5
10
15
20
10
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
20
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
30
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
40
✗
✗
✗
✗
✗
✗
✗
✗
✗
✗
✗
✗
50
✗
✗
✗
✗
✗
✗
✗
✗
✗
✗
✗
✗
60
✗
✗
✗
✗
✗
✗
✗
✗
✗
✗
✗
✗
C. Tracking Dynamically Feasible Trajectories
First of all, we compare the performance of NMPC and
DFBC in tracking 76 feasible trajectories. We perform the test
in an ideal condition with perfect model knowledge and state
estimates. Since only feasible trajectories are tracked, there is
no saturation of single rotor thrusts and both methods succeed
in tracking all trajectories without a single crash.
In this set of tests, we fine-tune the parameters of both
methods (listed in Table. I) such that they achieve a similar
position tracking error. Fig. 5 compares the boxplots of NMPC
and DFBC when tracking trajectories with different reference
maximum accelerations. Both methods have similar position
RMSE in these flights. As for the heading tracking, NMPC
has an average heading RMSE of 2.0 deg, which is better
than 5.8 deg of DFBC.
D. Tracking Dynamically Infeasible Trajectories
1) Tracking Accuracy: Fig. 6 shows the box plot of position
and heading RMSE of NMPC and DFBC in tracking the
previously generated 68 infeasible trajectories. Crashed flights
are excluded from this plot (see Fig. 7 for the crash rate). We
find that the DFBC method shows smaller position RMSE in
tracking trajectories with lower acceleration. However, as the
reference acceleration grows, NMPC significantly outperforms
DFBC. In general, NMPC outperforms DFBC by 48% on
position tracking (0.40 m vs. 0.77 m). As for the heading
tracking, NMPC has a noticeably less (62%) RMSE than
the DFBC method (12.7 deg vs. 33.4 deg). The advantage
of NMPC over DFBC becomes particularly relevant if the
reference acceleration exceeds the maximum thrust (∼5g) of
the tested quadrotor.
2) Crash Rates: Fig. 7 compares the crash rates of DFBC
and NMPC in tracking all the infeasible trajectories. NMPC
(solid-blue) outperforms DFBC (red-dash-dot), especially in
tracking trajectories with high reference accelerations.

## Page 9

9
10
20
30
40
Maximum acceleration [m/s2]
0
0.1
0.2
0.3
0.4
Position RMSE [m]
NMPC
DFBC
(a)
10
20
30
40
Maximum acceleration [m/s2]
0
5
10
15
20
Heading RMSE [deg]
NMPC
DFBC
(b)
Fig. 5: Boxplot of tracking error (RMSE) in tracking different dy-
namically feasible trajectories (76 in total) categorized by maximum
accelerations.
20
30
40
50
60
Maximum acceleration [m/s2]
0
0.5
1
1.5
2
2.5
3
Position RMSE [m]
NMPC
DFBC
(a)
20
30
40
50
60
Maximum acceleration [m/s2]
0
20
40
60
80
100
Heading RMSE [deg]
NMPC
DFBC
(b)
Fig. 6: Boxplot of tracking error (RMSE) in tracking different dy-
namically infeasible trajectories (68 in total) categorized by maximum
accelerations. Crashed flights are removed from these analyses (see
Fig. 7 for the crash rate).
Here, we also demonstrate contributions of the tilt-
prioritized attitude controller and the quadratic-programming
based allocation presented in Sec. IV. We replace them respec-
tively with the conventional geometric attitude controller [24]
and the direct-inversion allocation (30). The resultant crash
rates are shown in Fig. 7 as well. It is obvious that the DFBC
method tested in this study shows a significantly lower crash
rate in tracking infeasible trajectories.
20
25
30
35
40
45
50
55
60
Maximum acceleration [m/s2]
0
20
40
60
80
100
Crashe rate [%]
NMPC
DFBC
DFBC w/o QP based allocation
DFBC w/o tilt-prioritization
Fig. 7: Crash rates of NMPC, DFBC, and DFBC with different setups:
DFBC without quadratic-programming based allocation, DFBC with-
out tilt-prioritized attitude controller but using the geometric attitude
controller.
E. Robustness Study
While previous simulations are carried out in an ideal
condition, this section studies the robustness of NMPC and
DFBC methods in the following non-ideal conditions:
• Model mismatch, including the center of gravity bias,
mass mismatch, thrust and torque coefficients model
mismatch, and error of aerodynamic drag model.
• External disturbances. In details, we simulate constant
external forces along xI, or external torques along both
xB and yB. These disturbances last for 5 seconds.
• Position, velocity, and attitude estimation latency. This
aims at studying the effect of latency from such as signal
transmission, state estimation algorithms, and sensors.
As angular rates are measured directly by IMU with
negligible latency, we only study the latency on pose and
velocity estimates.
These robustness studies are conducted using only the feasible
trajectories since NMPC already shows its advantage over
DFBC in tracking infeasible trajectories. We set the position
RMSE as 5.0 m and heading RMSE as 90 deg for those
crashed flights.
Table IV and Table V respectively present the results
without and with INDI inner-loop. NMPC shows substantially
higher robustness than DFBC against model uncertainties
and disturbances on rotational dynamics due to CoG bias
or external moments. Adding an INDI inner-loop controller
can improve the robustness against these uncertainties. Even
so, NMPC still slightly outperforms DFBC when both are
augmented by an INDI inner-loop controller.
Unlike the rotational dynamics, NMPC shows a higher crash
rate while experiencing model uncertainties and disturbances
acting on the translational dynamics. For example, when the
real mass is 30% higher, both controllers generate fewer thrusts
than required to track the trajectory, resulting in a constant
position tracking error. With this tracking error, NMPC fails
to converge in over 10% of flights and crashes the drone.
The same reason also explains the significantly higher crash
rate of NMPC in the presence of large external disturbances.
Fig. 8 shows an example where NMPC failed in converging
and crashed the drone after experiencing a 10 N external
force disturbance. Note that adding INDI inner-loop does not
improve the performance of either controller to reject distur-
bances in the translational dynamics. A previous research [13]

## Page 10

10
TABLE IV: Tracking performance comparisons in different types of non-ideal conditions commonly seen in practice without INDI inner
loop. Each number shows the mean and standard deviation (SD) across tracking 76 dynamically feasible trajectories.
Position RMSE [m]
(mean ± SD)
Heading RMSE [deg]
(mean ± SD)
Crash Rate
[%]
NMPC
DFBC
NMPC
DFBC
NMPC
DFBC
Baseline
0.084 ± 0.049
0.084 ± 0.041
2.13 ± 3.38
5.91 ± 11.90
0
0
+50% Drag
0.183 ± 0.066
0.194 ± 0.084
2.11 ± 3.35
8.56 ± 15.46
0
0
+100% Drag
0.286 ± 0.109
0.305 ± 0.139
2.25 ± 3.38
9.07 ± 11.44
0
0
-30% Mass
0.320 ± 0.105
0.477 ± 0.109
2.27 ± 3.38
11.26 ± 17.77
0
0
+30% Mass
0.809 ± 1.455
0.687 ± 1.001
11.77 ± 27.21
7.21 ± 14.11
10.7
0
10% CoG bias
0.264 ± 0.094
1.499 ± 1.802
2.67 ± 3.42
25.95 ± 35.69
0
20
15% CoG bias
0.464 ± 0.557
3.039 ± 2.216
4.58 ± 10.94
53.62 ± 41.95
1.3
56
-30% ct
0.939 ± 1.415
0.998 ± 1.216
12.30 ± 27.13
8.79 ± 18.01
10.7
0
+30% ct
0.245 ± 0.085
0.36 ± 0.076
2.05 ± 3.34
6.63 ± 10.87
0
0
-30% cq
0.085 ± 0.052
0.084 ± 0.041
2.03 ± 3.37
6.23 ± 13.03
0
0
+30% cq
0.084 ± 0.051
0.084 ± 0.04
2.07 ± 3.38
5.81 ± 11.81
0
0
5N Ext. force
0.252 ± 0.042
0.302 ± 0.031
5.08 ± 3.58
17.42 ± 14.59
0
0
10N Ext. force
0.716 ± 1.019
0.689 ± 0.524
12.59 ± 19.07
24.59 ± 16.28
5.3
1.3
15N Ext. force
1.870 ± 1.892
1.391 ± 1.069
32.13 ± 35.38
32.54 ± 20.58
26.7
6.7
0.1Nm Ext. moment
0.153 ± 0.038
0.270 ± 0.098
3.26 ± 3.35
12.04 ± 13.45
0
0
0.2Nm Ext. moment
0.319 ± 0.545
2.538 ± 2.079
5.85 ± 10.71
54.89 ± 31.08
1.3
41.3
0.3Nm Ext. moment
0.566 ± 0.907
4.949 ± 0.439
10.87 ± 17.27
89.16 ± 6.88
4.0
98.7
10ms Latency
0.085 ± 0.065
0.097 ± 0.099
2.07 ± 3.34
5.79 ± 11.05
0
0
30ms Latency
0.158 ± 0.183
0.333 ± 0.976
5.04 ± 10.47
13.73 ± 25.87
0
4.0
50ms Latency
3.450 ± 2.217
0.669 ± 1.247
65.00 ± 38.65
54.82 ± 30.02
66.7
5.3
TABLE V: Tracking performance comparisons in different types of non-ideal conditions commonly seen in practice with INDI inner loop.
Each number shows the mean and standard deviation (SD) across tracking 76 dynamically feasible trajectories.
Position RMSE [m]
(mean ± SD)
Heading RMSE [deg]
(mean ± SD)
Crash Rate
[%]
NMPC
DFBC
NMPC
DFBC
NMPC
DFBC
Baseline
0.082 ± 0.047
0.085 ± 0.043
2.03 ± 3.35
5.83 ± 11.40
0
0
+50% Drag
0.184 ± 0.067
0.194 ± 0.084
2.10 ± 3.33
8.48 ± 14.50
0
0
+100% Drag
0.288 ± 0.11
0.306 ± 0.139
2.25 ± 3.32
9.32 ± 11.99
0
0
-30% Mass
0.320 ± 0.106
0.477 ± 0.108
2.26 ± 3.36
10.42 ± 14.19
0
0
+30% Mass
0.747 ± 1.372
0.686 ± 0.999
10.60 ± 25.66
7.11 ± 13.97
9.3
0
10% CoG bias
0.081 ± 0.047
0.099 ± 0.104
2.09 ± 3.32
6.46 ± 13.65
0
0
15% CoG bias
0.083 ± 0.051
0.378 ± 1.117
2.05 ± 3.30
10.70 ± 22.52
0
5.3
-30% ct
1.362 ± 1.764
1.004 ± 1.212
19.98 ± 33.88
10.06 ± 19.06
18.7
1.3
+30% ct
0.244 ± 0.085
0.359 ± 0.076
2.13 ± 3.52
6.14 ± 9.58
0
0
-30% cq
0.082 ± 0.049
0.086 ± 0.047
2.08 ± 3.35
6.01 ± 11.69
0
0
+30% cq
0.082 ± 0.046
0.085 ± 0.046
2.07 ± 3.34
5.83 ± 11.61
0
0
5N Ext. force
0.254 ± 0.051
0.302 ± 0.033
5.03 ± 3.48
17.58 ± 14.77
0
0
10N Ext. force
0.725 ± 1.018
0.690 ± 0.524
12.38 ± 19.02
24.81 ± 16.28
5.3
1.3
15N Ext. force
1.872 ± 1.891
1.393 ± 1.070
32.14 ± 35.35
32.97 ± 20.80
26.7
6.7
0.1Nm Ext. moment
0.083 ± 0.048
0.087 ± 0.049
2.49 ± 3.22
7.95 ± 12.46
0
0
0.2Nm Ext. moment
0.087 ± 0.051
0.113 ± 0.088
3.19 ± 3.35
13.65 ± 17.25
0
0
0.3Nm Ext. moment
0.298 ± 0.962
0.764 ± 1.663
8.40 ± 17.29
26.93 ± 29.41
4.0
13.3
10ms Latency
0.087 ± 0.088
0.099 ± 0.106
2.21 ± 3.44
5.73 ± 11.65
0
0
30ms Latency
0.280 ± 0.802
0.265 ± 0.800
8.39 ± 20.12
14.34 ± 25.85
2.7
2.7
50ms Latency
3.480 ± 2.235
0.694 ± 1.294
64.02 ± 39.96
52.29 ± 29.12
68.0
6.7
implemented INDI in the position control (INDI outer-loop)
for DFBC by virtue of its cascaded structure and improved
its translational robustness. On the contrary, hybridizing INDI
outer-loop with NMPC seems challenging owing to its non-
cascaded nature.
The two methods also perform differently in the presence
of system latency. While NMPC slightly outperforms DFBC
when the system latency is lower than 30 ms, as the latency
grows, NMPC shows a much higher crash rate (68.0%) than
DFBC (6.7%). As Fig. 9 shows, we repeat the tests under
30 ms and 50 ms latency with a high-gain setup and a low-
gain setup. In both setups, these gains are tuned such that
both controllers have identical average position RMSE in the
ideal condition. As is expected, reducing gains will alleviate
the effect of estimation latency. Interestingly, we observe that
NMPC is more sensitive to the gain selections when system
latency is larger than 30 ms.
F. Effect of Controller Parameters
Controller performance is dominated by the parameters or
gains. However, finding optimal controller gains can be tedious
and highly dependent on the drone parameters. Thus this sec-

## Page 11

11
0
5
10
15
20
Time [s]
0
20
40
60
80
Position RMSE [m]
NMPC
DFBC
10N external force
Fig. 8: Position tracking error for a loop trajectory (Vmax = 15m/s,
amax = 40m/s2, n = 1). Grey area indicates the period with 10 N
lateral disturbances acting on the drone. NMPC failed to converge and
crashed the drone, while the DFBC method succeeds in recovering
the drone after the external disturbance disappeared.
0
10
20
30
40
50
Latency [ms]
0
0.5
1
1.5
2
2.5
3
position RMSE [m]
NMPC
DFBC
high-gains
low-gains
Fig. 9: Position RMSE of NMPC and DFBC in the presence of
different amounts of estimation latency, with different sets of control
gains. Results using gains of previous studies are shown in dash-dot
lines. NMPC shows higher sensitivity to the gain selections when
estimation latency appears.
tion performs a sensitivity analysis to provide insights into the
effect of controller parameters on the tracking performance.
We set the control parameters given in Table I as the baseline,
and compare the tracking performance with altered parameters
with respect to the baseline.
1) Nonlinear MPC: Fig. 10 shows the effect of changing
elements of the weight matrix Q. The position tracking
performance is highly correlated with Qξ and Qv. Among
all the parameters, the position weight Qξ plays the most
important role. A larger penalty on the position error results in
a smaller tracking error. However, as Qξ continues growing,
the NMPC starts to destabilize the drone. We believe that this
is due to the presence of actuator dynamics in the simulation,
which introduces system delay and causes instability with
high gain controllers. Note that in real-world experiments,
system latency can be larger due to state estimation algorithms
and signal transmissions, which further reduces the permitted
maximum Qξ. Another observation is that increasing QΩ
also adversarially affects the position tracking performance as
it dilutes the power of position weights. Regarding heading
control, as is expected, increasing Qq,z can improve the
heading tracking performance while causing little effect on
position tracking.
2) Differential Flatness Based Control:
The controller
gains of DFBC consists of position, attitude gains and weight
matrix for control allocation. The gains are selected to make
the position error ξe = ξ −ξr a second-order system:
¨ξe + 2ζξωn,ξ ˙ξe + ω2
n,ξξe = 0
(40)
10 -1
10 0
10 1
10 2
10 3
Q / Q base
0
100
200
300
Pos RMSE / RMSEbase  [%]
Q
Qv
Qq,x , Q q,y
Qq,z
Q
10 -1
10 0
10 1
10 2
10 3
Q / Q base
0
100
200
300
Heading RMSE / RMSE base  [%]
Q
Qv
Qq,x , Q q,y
Qq,z
Q
Fig. 10: Position (top) and heading (bottom) tracking RMSE of
the NMPC method in different control parameters. The vertical
axis represents the ratio between RMSE and that from a baseline
parameter setup. The horizontal axis represents the ratio between the
control parameter and the baseline parameter. The RMSE of those
crashed flights are clamped at 300% of RMSEbase
where ζξ and ωn,ξ are damping ratio and natural frequency,
respectively. Then substituting (13) into (40) and replacing ¨ξd
with ¨ξ (assuming a perfect inner-loop attitude control), we can
calculate the position control gains as follows:
Kξ = diag(ω2
n,ξ, ω2
n,ξ, ω2
n,ξ), Kv = 2ζξ
p
Kξ.
(41)
Similarly, the attitude gains can be designed as:
kq,x = kq,y = ω2
n,xy, kq,z = ω2
n,z,
(42)
KΩ= 2ζqdiag(
p
kq,x,
p
kq,y,
p
kq,z).
(43)
where ζq is the damping ratio, ωn,xy and ωn,z are desired
natural frequencies of reduced attitude and yaw errors respec-
tively.
Fig. 11 presents the relationship between tracking error
and closed-loop natural frequency. Both time constants and
tracking errors are normalized by the baseline gains given in
Table I. A higher frequency indicates a higher control gain,
leading to less tracking error. However, high gains are also
prone to suffer from system delay and subsequently cause
instability.
Weighting matrix W is selected based on tuning in the
simulation without sophisticated calculation. It aims at leaving
more priority to the tilt control over collective thrust and yaw.
An example of inappropriate selection of W is an identical
matrix, which makes the QP-based allocation identical to a
direct inversion. The performance in terms of crash rate has
been compared in Fig. 7 necessity of using a well-tuned W
in tracking dynamically infeasible trajectories.
VII. REAL-WORLD EXPERIMENTS
We conduct the experiments on a quadrotor in an instru-
mented tracking arena. A set of aggressive trajectories are

## Page 12

12
TABLE VI: Tracking performance of different methods in real-world experiments
References
Position Tracking RMSE [m]
Heading Tracking RMSE [deg]
Type
Vmax [m/s]
amax [m/s2]
NMPC+PID [4]
NMPC
NMPC+INDI
NMPC+INDI
(w/o drag model)
DFBC
DFBC+INDI
DFBC+INDI
(w/o drag model)
NMPC+PID [4]
NMPC
NMPC+INDI
NMPC+ INDI
(w/o drag model)
DFBC
DFBC + INDI
DFBC+ INDI
(w/o drag model)
Loop A
10.2
20.7
0.280
0.548
0.068
0.215
0.897
0.073
0.242
6.801
11.274
8.450
8.972
73.842
4.411
9.395
Loop B
13.4
35.9
0.369
0.930
0.117
0.261
-
0.125
0.252
11.618
22.193
9.714
10.478
-
10.496
11.489
Slant Loop A
8.2
12.6
0.241
0.458
0.077
0.156
0.535
0.109
0.163
6.951
19.795
5.987
6.870
17.755
7.521
8.032
Slant Loop B
12.9
30.8
0.447
0.777
0.116
0.217
-
0.138
0.305
7.729
18.382
8.282
8.816
-
9.171
10.047
Vertical Loop A
7.7
14.6
0.197
0.206
0.069
0.172
0.181
0.082
0.127
1.558
5.131
1.108
1.274
30.901
1.151
1.530
Vertical Loop B
11.5
32.9
0.482
0.350
0.126
0.314
-
0.177
0.196
19.000
6.019
2.415
1.900
-
15.495
8.632
Oscillate A
10.9
20.7
0.327
0.212
0.058
0.259
0.310
0.164
0.210
1.641
7.369
2.029
1.960
50.210
3.977
1.911
Oscillate B
14.0
36.5
0.375
0.290
0.125
0.377
-
0.129
0.294
2.708
9.228
2.386
2.902
-
2.763
3.821
Hairpin A
7.7
14.6
0.185
0.352
0.024
0.146
0.350
0.049
0.124
4.733
7.100
3.745
4.255
38.980
5.913
5.873
Hairpin B
11.5
32.9
0.390
0.479
0.099
0.274
1.797
0.117
0.166
7.965
15.748
7.343
8.017
68.139
10.163
8.004
Lemniscate A
9.5
13.6
0.225
0.324
0.056
0.184
0.423
0.068
0.216
3.576
9.074
3.689
4.109
37.235
2.605
2.243
Lemniscate B
14.2
36.0
0.314
0.564
0.130
0.290
-
0.128
0.287
7.335
15.952
6.280
6.659
-
4.986
5.403
Split-S
14.2
25.5
0.292
0.352
0.096
0.262
-
0.087
0.239
9.411
13.253
6.409
5.259
-
17.888
18.929
Racing Track A
11.9
22.1
0.280
0.424
0.108
0.212
0.552
0.102
0.240
6.806
10.434
6.566
7.706
37.731
4.336
5.390
Racing Track B
16.8
28.5
0.369
0.546
0.130
0.320
3.797
0.152
0.359
11.930
14.672
9.318
8.805
57.810
8.249
7.719
Racing Track C
19.4
37.3
0.712
0.758
0.238
0.329
-
0.259
0.480
11.235
19.936
11.754
9.876
-
14.695
15.498
Mean
0.343
0.473
0.102
0.249
0.982
0.122
0.244
7.562
12.848
5.967
6.116
45.845
7.739
7.745
Standard deviation
0.130
0.207
0.067
0.048
1.161
0.164
0.051
4.499
5.434
3.054
3.136
18.175
4.768
4.964
0
0.5
1
1.5
2
2.5
3
2
n / 
2
n,base
0
100
200
300
Pos RMSE / RMSEbase  [%]
n,xy
n,z
0
0.5
1
1.5
2
2.5
3
2
n / 
2
n,base
50
100
150
200
250
300
Heading RMSE / RMSE base  [%]
n,xy
n,z
Fig. 11: Position (top) and heading (bottom) tracking RMSE of the
DFBC method in different control gain settings. The vertical axis
represents the ratio between RMSE and the RMSE from a baseline
gain setup. The horizontal axis represents the ratio between the
controller gains and the baseline gains. RMSE of the crashed flights
are clamped at 300% of RMSEbase
TABLE VII: Performance in tracking three dynamically infeasible
trajectories in real-world experiments. Position and heading RMSE
comparisons between NMPC and DFBC with INDI inner-loop.
Reference
Vmax
[m]
amax
[m/s2]
Position RMSE [m]
Heading RMSE [deg]
NMPC
+INDI
DFBC
+INDI
NMPC
+INDI
DFBC
+INDI
Vertical Loop C
12.1
48.5
0.318
0.919
2.469
25.608
Loop C
15.7
49.3
0.762
1.829
13.439
25.876
Lemniscate C
19.0
54.5
0.570
1.237
11.680
53.262
Average RMSE
0.550
1.328
9.196
34.915
executed to compare the closed-loop tracking performance of
NMPC and DFBC in the presence of joint effects such as
model mismatch, state estimation error, and system latency.
The real-world experiments also highlight the contributions of
the INDI low-level controller, the aerodynamic force model,
to both NMPC and DFBC methods.
Experiments are conducted in tracking different reference
trajectories, ranging from simple loop trajectories to FPV
drone racing tracks (see Table. VI). Trajectories with the same
3D shape but different velocities and accelerations are also
tested. The 3D paths of these trajectories are illustrated in
Fig. 12.
We evaluated NMPC and DFBC, with and without the INDI
inner-loop controller. NMPC with a PID low-level controller is
also tested for comparison, implemented to track time-optimal
trajectory in [4]. In the following, these methods consider
aerodynamic drag models by default, unless further mentioned.
The position tracking RMSE and heading tracking RMSE are
listed in Table. VI and Table. VII.
A. Contribution of the INDI and Drag Model
Table VIII compares the average RMSE of both methods
and shows the effect of the INDI inner-loop controller, and
the effect of the aerodynamic drag model. For NMPC and
DFBC, neglecting aerodynamic drag would increase position
tracking error by 144% percent and 122%, respectively.
In contrast to the aerodynamic drag model, removing the
INDI low-level controller influences more on the tracking ac-
curacy. For NMPC, we see more than 364% and 115% increase
in position and heading RMSE if INDI is not used. For DFBC,
removing INDI leads to a more severe consequence: more
than 705% and 492% of position and heading RMSE increase.
In fact, DFBC without INDI cannot successfully track some
of these trajectories without crashing the drone. These results
indicate that, an adaptive/robust inner-loop controller plays a

## Page 13

13
Fig. 12: Tested trajectories in real-world experiments. From top-left to bottom right, they are: Loop, Oscillate, Hairpin, Slant-loop, Vertical-
loop, Split-S, Lemniscate, Racing-trajectory.
−5.0
−2.5
0.0
2.5
5.0
7.5
10.0
12.5
x [m]
−6
−4
−2
0
2
4
6
8
y [m]
0.0
0.5
1.0
1.5
Position Error [m]
0
1
2
3
4
5
6
5
10
15
20
Flight Speed [m/s]
Time [s]
Reference
NMPC+PID
NMPC+INDI
DFBC+INDI
Fig. 13: Tracking performance of the Race Track C with a maximum speed up to 20 m/s. NMPC and DFBC with INDI inner-loop show
similar tracking performance. Both outperform the state-of-the-art NMPC with a PID inner-loop controller [4]
more important role than the drag model in accurately tracking
aggressive trajectories.
We also make comparisons against the control method used
in [4], which uses PID as the inner-loop controller of NMPC.
This comparison is made in tracking a time-optimal trajectory
generated off-line using the algorithm proposed in [4]. In this
task, the quadrotor needs to fly through multiple gates in a
predefined order. Fig. 13 demonstrates the tracking results,
including the 3D path and the position error. Clearly, both
NMPC and DFBC augmented by INDI significantly outper-
form this NMPC with PID inner-loop controller. Comparative
results on other reference trajectories can be found in Table VI.
On average, the proposed NMPC with the INDI approach
shows a position RMSE of 0.102 m, which is 70% lower than
the position RMSE of NMPC with PID low-level controller
(0.343 m).
B. Tracking Dynamically Infeasible Trajectories
In these real-world experiments, we also track three dynam-
ically infeasible trajectories that exceed the maximum thrust of
the tested quadrotor. Comparative results of NMPC and DFBC
are given in Table VII. Clearly, NMPC shows significantly
higher tracking accuracy than DFBC when tracking these
TABLE VIII: Position and heading tracking RMSE of NMPC and
DFBC methods. Adding INDI as the inner-loop improves the perfor-
mance significantly for both methods.
Position RMSE [m]
Heading RMSE [deg]
NMPC+INDI
0.102
(↑0%)
5.967
(↑0%)
NMPC+INDI (w/o drag model)
0.249
(↑144%)
6.116
(↑3%)
NMPC
0.473
(↑364%)
12.848
(↑115%)
DFBC+INDI
0.122
(↑0%)
7.739
(↑0%)
DFBC+INDI (w/o drag model)
0.271
(↑122%)
7.745
(↑0.07%)
DFBC
0.982
(↑705%)
45.845
(↑492%)
dynamically infeasible trajectories, which is consistent with
the simulation results in Sec. VI.
Fig. 14 presents the 3D path tracking the Loop C reference
trajectory. Tracking such a reference loop trajectory requires a
higher collective thrust than the maximum thrust of the tested
quadrotor. Hence the quadrotor cannot follow the reference
trajectory and both control methods make the quadrotor take
the shortcut to fly inside the reference trajectory. While DFBC
results in a chaotic trajectory, NMPC makes the drone fly a
much more regular loop trajectory with a smaller radius than
the reference, thus requiring less collective thrust. The differ-
ence on the side-view is more distinctive: NMPC has much
higher altitude tracking accuracy than the DFBC method.

## Page 14

14
-6
-4
-2
0
2
4
6
x [m]
-5
-4
-3
-2
-1
0
1
2
3
4
5
y [m]
Reference
DFBC+INDI
NMPC+INDI
-6
-4
-2
0
2
4
6
x [m]
0.5
1
1.5
2
z [m]
Fig. 14: Top and side view of the trajectory tracking a dynamically in-
feasible trajectory (black-dash) using NMPC (blue-solid) and DFBC
method (red-dash-dot).
0
1
2
3
4
5
6
Time [s]
0
1
2
3
4
5
6
7
Proc. Time [s]
10 -5
QP allocator
INDI
DFBC
Fig. 15: CPU time of DFBC+INDI while tracking the Race Track C
trajectory.
C. Computational Time
Fig. 15 and 16 respectively show the CPU time of DFBC
and NMPC with INDI as the inner-loop controller while
tracking the Race Track C trajectory. The computation time of
DFBC is generally faster than 0.025 ms, which is significantly
faster compared with NMPC that takes around 3 ms. In
addition, both QP and INDI modules spend less than 0.01 ms
CPU time.
Fig. 17 compares the average computational time of gen-
erating each control commands of NMPC and DFBC, with
INDI using all the flight data. Each data point in the box
plot represents the average computing time of a single flight.
As is expected, NMPC requires significantly longer time to
generate a single control command (2.7 ms) compared with
DFBC (0.020 ms). Be that as it may, both methods can run
onboard at sufficiently high frequency (≥100 Hz) to achieve
accurate tracking of agile trajectories.
0
1
2
3
4
5
6
Time [s]
10 -6
10 -5
10 -4
10 -3
10 -2
Proc. Time [s]
INDI
NMPC
Fig. 16: CPU time of NMPC+INDI while tracking the Race Track C
trajectory. Note that the vertical axis is presented in the log scale.
Fig. 17: Processing time to generate each control command of NMPC
and DFBC methods.
VIII. DISCUSSION
According to the simulation and real-world flight results, we
conclude that both NMPC and DFBC, with an INDI inner-loop
controller, can track highly aggressive trajectories with similar
accuracy as long as the reference trajectories are dynamically
feasible.
The advantage of NMPC appears when tracking dynam-
ically infeasible trajectories that violate the rotor thrust
constraints. Even though DFBC also uses the constrained-
quadratic programming for control allocation, it only considers
a single reference point; thus, the actions taken are too short-
sighted to avoid future violations of these constraints. By
contrast, NMPC tracks the infeasible trajectory using future
predictions, including multiple reference points that minimize
the tracking error and respect single rotor constraints. Such
difference helps NMPC outperform DFBC by 48% and 62%
on position and heading accuracy, respectively, if the reference
trajectories are dynamically infeasible.
NMPC also demonstrates higher robustness against the
rotational model mismatch. In real-world experiments, we
also performed tests without INDI low-level controller for
comparisons. As such, both methods suffered from model
uncertainties on the rotational dynamics. In this condition,
NMPC was still able to track all the trajectories, whereas
DFBC experienced several crashes and had much higher
tracking RMSE against NMPC.
However, NMPC also has limitations. For example, the
biggest disadvantage of NMPC is that it requires significantly
higher computational resources. On our tested hardware, the
average solving time of the nonlinear NMPC is around 2.7
ms, while DFBC needs only 0.020 ms, which is around 100

## Page 15

15
times faster. This renders it impractical to run NMPC on some
miniature aerial vehicles with a limited computational budget,
such as Crazyflie [45]. By contrast, we can deploy DFBC on
light-weighted drones with low-end processors and conduct
agile flights at speeds over 20 m/s, as long as the platform has
enough thrust-to-weight ratio.
Another disadvantage of NMPC is that it potentially suffers
from numerical convergence issues. Unlike DFBC, which has
proof of stability or convergence of each sub-module, the
nonlinear NMPC used in this comparison relies on the nu-
merical convergence of the nonlinear optimization algorithm.
Unfortunately, rigorous proof of its convergence is still an open
question. In fact, nonlinear NMPC tends to fail in converging
when the current position is too far from the reference, either
caused by large external force disturbances or an error in
the thrust-to-weight ratio model. For example, our robustness
study shows a 10% higher crash rate of NMPC than DFBC
when the real mass is 30% higher than the model. In addition,
we also observe that NMPC is more prone to fail in converging
than DFBC in the presence of large system latency.
In summary, NMPC is not superior to DFBC in all sce-
narios. If the reference trajectories are dynamically feasible,
DFBC can achieve similar tracking performance while con-
suming only 1 percent of the control resource that NMPC
requires. However, it is difficult to justify the feasibility of a
trajectory near the physical limitations of the platform because
of the model uncertainties such as aerodynamic effects.
Hence, NMPC excels at exploiting the full capability of
an autonomous drone in a safer and more efficient manner,
due to its advantage in handling the infeasibility of reference
trajectories. Future work may further hybridize NMPC with
differential flatness property to reduce the NMPC computa-
tional cost while retaining its advantage in handling dynami-
cally infeasible trajectories. The reason why NMPC failed in
converging also needs further investigation in order to deal
with larger amount of model uncertainties.
IX. CONCLUSION
This work systematically compares NMPC and DFBC, two
state-of-the-art quadrotor controllers for tracking agile trajec-
tories. Simulation and real-world experiments are extensively
performed to evaluate the performance of both methods in
terms of accuracy, robustness, and computational efficiency.
We report the advantages and disadvantages of both methods
according to the results. This work also evaluates the effect
of INDI inner-loop control on both methods. Real-world flight
results at up to 20 m/s demonstrate the necessity of applying
an INDI inner-loop on both NMPC and DFBC approaches.
The effect of the high-speed aerodynamic drag model is also
evaluated, which is found less influential compared to the
inner-loop controller.
ACKNOWLEDGMENT
We thank Thomas L¨angle and Leonard Bauersfeld for their
help in experiments and photo rendering. We also appreciate
the valuable feedback from Yunlong Song, Dr. Antonio Lo-
quercio, Drew Hanover, and Dr. Xuerui Wang from TU Delft.
REFERENCES
[1] G. Loianno and D. Scaramuzza, “Special issue on fu-
ture challenges and opportunities in vision-based drone
navigation,” Journal of Field Robotics, vol. 37, no. 4,
pp. 495–496, 2020.
[2] S. Rajendran and S. Srinivas, “Air taxi service for urban
mobility: A critical review of recent developments, future
challenges, and opportunities,” Transportation research
part E: logistics and transportation review, vol. 143,
p. 102090, 2020.
[3] D. Bicego, J. Mazzetto, R. Carli, M. Farina, and
A. Franchi, “Nonlinear model predictive control with
enhanced actuator model for multi-rotor aerial vehicles
with generic designs,” Journal of Intelligent & Robotic
Systems, vol. 100, no. 3, pp. 1213–1247, 2020.
[4] P. Foehn, A. Romero, and D. Scaramuzza, “Time-
optimal planning for quadrotor waypoint flight,” Science
Robotics, vol. 6, no. 56, p. eabh1221, 2021.
[5] G. Torrente, E. Kaufmann, P. F¨ohn, and D. Scaramuzza,
“Data-driven mpc for quadrotors,” IEEE Robotics and
Automation Letters, vol. 6, no. 2, pp. 3769–3776, 2021.
[6] M. Kamel, K. Alexis, M. Achtelik, and R. Siegwart,
“Fast nonlinear model predictive control for multicopter
attitude tracking on so(3),” in 2015 IEEE Conference on
Control Applications (CCA), pp. 1160–1166, IEEE, 2015.
[7] M. Kamel, T. Stastny, K. Alexis, and R. Siegwart,
“Model predictive control for trajectory tracking of un-
manned aerial vehicles using robot operating system,” in
Robot operating system (ROS), pp. 3–39, Springer, 2017.
[8] A. Murilo and R. V. Lopes, “Unified nmpc framework
for attitude and position control for a vtol uav,” Proceed-
ings of the Institution of Mechanical Engineers, Part I:
Journal of Systems and Control Engineering, vol. 233,
no. 7, pp. 889–903, 2019.
[9] E. Small, P. Sopasakis, E. Fresk, P. Patrinos, and G. Niko-
lakopoulos, “Aerial navigation in obstructed environ-
ments with embedded nonlinear model predictive con-
trol,” in 2019 18th European Control Conference (ECC),
pp. 3556–3563, IEEE, 2019.
[10] H. Nguyen, M. Kamel, K. Alexis, and R. Siegwart,
“Model predictive control for micro aerial vehicles: A
survey,” in 2021 European Control Conference (ECC),
pp. 1556–1563, IEEE, 2021.
[11] A. Romero, S. Sun, P. Foehn, and D. Scaramuzza,
“Model predictive contouring control for time-optimal
quadrotor flight,” IEEE Transactions on Robotics, pp. 1–
17, 2022.
[12] M. Faessler, A. Franchi, and D. Scaramuzza, “Differen-
tial flatness of quadrotor dynamics subject to rotor drag
for accurate tracking of high-speed trajectories,” IEEE
Robotics and Automation Letters, vol. 3, no. 2, pp. 620–
626, 2017.
[13] E. Tal and S. Karaman, “Accurate tracking of aggres-
sive quadrotor trajectories using incremental nonlinear
dynamic inversion and differential flatness,” IEEE Trans-
actions on Control Systems Technology, vol. 29, no. 3,
pp. 1203–1218, 2020.

## Page 16

16
[14] T. A. Johansen and T. I. Fossen, “Control allocation—a
survey,” Automatica, vol. 49, no. 5, pp. 1087–1103, 2013.
[15] E. J. Smeur, Q. Chu, and G. C. de Croon, “Adaptive
incremental nonlinear dynamic inversion for attitude con-
trol of micro air vehicles,” Journal of Guidance, Control,
and Dynamics, vol. 39, no. 3, pp. 450–461, 2016.
[16] S. Sun, X. Wang, Q. Chu, and C. de Visser, “Incremental
nonlinear fault-tolerant control of a quadrotor with com-
plete loss of two opposing rotors,” IEEE Transactions on
Robotics, vol. 37, no. 1, pp. 116–130, 2020.
[17] T. P. Nascimento and M. Saska, “Position and attitude
control of multi-rotor aerial vehicles: A survey,” Annual
Reviews in Control, vol. 48, pp. 129–146, 2019.
[18] H. Lee and H. J. Kim, “Trajectory tracking control of
multirotors from modelling to experiments: A survey,”
International Journal of Control, Automation and Sys-
tems, vol. 15, no. 1, pp. 281–292, 2017.
[19] S. Khatoon, D. Gupta, and L. Das, “Pid & lqr control
for a quadrotor: Modeling and simulation,” in 2014
international conference on advances in computing, com-
munications and informatics (ICACCI), pp. 796–802,
IEEE, 2014.
[20] W. Dong, G.-Y. Gu, X. Zhu, and H. Ding, “Modeling and
control of a quadrotor uav with aerodynamic concepts,”
in Proceedings of World Academy of Science, Engineer-
ing and Technology, no. 77, p. 437, World Academy of
Science, Engineering and Technology (WASET), 2013.
[21] H. Voos, “Nonlinear control of a quadrotor micro-uav us-
ing feedback-linearization,” in 2009 IEEE International
Conference on Mechatronics, pp. 1–6, IEEE, 2009.
[22] T. Madani and A. Benallegue, “Backstepping control for
a quadrotor helicopter,” in 2006 IEEE/RSJ International
Conference on Intelligent Robots and Systems, pp. 3255–
3260, IEEE, 2006.
[23] E. Fresk and G. Nikolakopoulos, “Full quaternion based
attitude control for a quadrotor,” in 2013 European
control conference (ECC), pp. 3864–3869, IEEE, 2013.
[24] T. Lee, M. Leok, and N. H. McClamroch, “Geomet-
ric tracking control of a quadrotor uav on se (3),” in
49th IEEE conference on decision and control (CDC),
pp. 5420–5425, IEEE, 2010.
[25] D. Mellinger and V. Kumar, “Minimum snap trajectory
generation and control for quadrotors,” in 2011 IEEE
international conference on robotics and automation,
pp. 2520–2525, IEEE, 2011.
[26] R. Mahony, V. Kumar, and P. Corke, “Multirotor aerial
vehicles: Modeling, estimation, and control of quadro-
tor,” IEEE Robotics and Automation magazine, vol. 19,
no. 3, pp. 20–32, 2012.
[27] S. Sun, C. C. de Visser, and Q. Chu, “Quadrotor gray-box
model identification from high-speed flight data,” Journal
of Aircraft, vol. 56, no. 2, pp. 645–661, 2019.
[28] H. Huang, G. M. Hoffmann, S. L. Waslander, and
C. J. Tomlin, “Aerodynamics and control of autonomous
quadrotor helicopters in aggressive maneuvering,” in
2009 IEEE international conference on robotics and
automation, pp. 3277–3282, IEEE, 2009.
[29] M. Faessler, D. Falanga, and D. Scaramuzza, “Thrust
mixing, saturation, and body-rate control for accurate
aggressive quadrotor flight,” IEEE Robotics and Automa-
tion Letters, vol. 2, no. 2, pp. 476–482, 2016.
[30] E. Smeur, D. H¨oppener, and C. De Wagter, “Prioritized
control allocation for quadrotors subject to saturation,”
in International Micro Air Vehicle Conference and Flight
Competition, no. September, pp. 37–43, 2017.
[31] D. Brescianini and R. D’Andrea, “Tilt-prioritized quadro-
copter attitude control,” IEEE Transactions on Control
Systems Technology, vol. 28, no. 2, pp. 376–387, 2018.
[32] H. Zaki, M. Unel, and Y. Yildiz, “Trajectory control of a
quadrotor using a control allocation approach,” in 2017
International Conference on Unmanned Aircraft Systems
(ICUAS), pp. 533–539, IEEE, 2017.
[33] M. Kamel, M. Burri, and R. Siegwart, “Linear vs
nonlinear mpc for trajectory tracking applied to rotary
wing micro aerial vehicles,” IFAC-PapersOnLine, vol. 50,
no. 1, pp. 3463–3469, 2017.
[34] M. Bangura and R. Mahony, “Real-time model predic-
tive control for quadrotors,” IFAC Proceedings Volumes,
vol. 47, no. 3, pp. 11773–11780, 2014.
[35] K. Alexis, G. Nikolakopoulos, and A. Tzes, “On tra-
jectory tracking model predictive control of an un-
manned quadrotor helicopter subject to aerodynamic
disturbances,” Asian Journal of Control, vol. 16, no. 1,
pp. 209–224, 2014.
[36] B. Houska, H. J. Ferreau, and M. Diehl, “Acado
toolkit—an open-source framework for automatic control
and dynamic optimization,” Optimal Control Applica-
tions and Methods, vol. 32, no. 3, pp. 298–312, 2011.
[37] Y. Chen, M. Bruschetta, E. Picotti, and A. Beghi,
“Matmpc-a matlab based toolbox for real-time nonlin-
ear model predictive control,” in 2019 18th European
Control Conference (ECC), pp. 3365–3370, IEEE, 2019.
[38] J. A. Andersson, J. Gillis, G. Horn, J. B. Rawlings, and
M. Diehl, “Casadi: a software framework for nonlinear
optimization and optimal control,” Mathematical Pro-
gramming Computation, vol. 11, no. 1, pp. 1–36, 2019.
[39] M. Jacquet and A. Franchi, “Motor and perception
constrained nmpc for torque-controlled generic aerial
vehicles,” IEEE Robotics and Automation Letters, 2020.
[40] M. Diehl, H. G. Bock, H. Diedam, and P.-B. Wieber,
“Fast direct multiple shooting algorithms for optimal
robot control,” in Fast motions in biomechanics and
robotics, pp. 65–93, Springer, 2006.
[41] R. Verschueren, G. Frison, D. Kouzoupis, N. van Duijk-
eren, A. Zanelli, R. Quirynen, and M. Diehl, “Towards a
modular software package for embedded optimization,”
IFAC-PapersOnLine, vol. 51, no. 20, pp. 374–380, 2018.
[42] H. J. Ferreau, C. Kirches, A. Potschka, H. G. Bock, and
M. Diehl, “qpoases: A parametric active-set algorithm
for quadratic programming,” Mathematical Programming
Computation, vol. 6, no. 4, pp. 327–363, 2014.
[43] X. Wang, E.-J. Van Kampen, Q. Chu, and P. Lu, “Stabil-
ity analysis for incremental nonlinear dynamic inversion
control,” Journal of Guidance, Control, and Dynamics,
vol. 42, no. 5, pp. 1116–1129, 2019.
[44] P. Foehn, E. Kaufmann, A. Romero, R. Penicka, S. Sun,

## Page 17

17
L. Bauersfeld, T. Laengle, G. Cioffi, Y. Song, A. Loquer-
cio, and D. Scaramuzza, “Agilicious: Open-source and
open-hardware agile quadrotor for vision-based flight,”
AAAS Science Robotics, 2022.
[45] W.
Giernacki,
M.
Skwierczy´nski,
W.
Witwicki,
P. Wro´nski, and P. Kozierski, “Crazyflie 2.0 quadrotor
as a platform for research and education in robotics
and control engineering,” in 2017 22nd International
Conference on Methods and Models in Automation and
Robotics (MMAR), pp. 37–42, IEEE, 2017.
Sihao Sun (1992, China) received the B.Sc. and
M.Sc. degrees in aerospace engineering from Bei-
hang University, Beijing, China, in 2014 and 2017,
respectively. In 2020, He received a Ph.D. degree
in aerospace engineering from Delft University of
Technology, Delft, the Netherlands. From 2020 to
2021, he was first a visiting scholar and then a
postdoctoral researcher in the Robotics and Per-
ception Group, University of Zurich, Switzerland.
His research interests include system identification,
aerial robotics, and nonlinear control.
Angel Romero (1993, Spain) received a MSc de-
gree in ”Robotics, Systems and Control” from ETH
Zurich in 2018. Previously, he received a B.Sc. de-
gree in Electronics Engineering from the University
of Malaga in 2015. He is currently working toward a
Ph.D. degree in the Robotics and Perception Group
at the University of Zurich, finding new limits in
the intersection of machine learning, optimal con-
trol, and computer vision applied to super agile
autonomous quadrotor flight under the supervision
of Prof. Davide Scaramuzza.
Philipp Foehn (1991, Switzerland) received a M.Sc.
degree in ”Robotics, Systems and Control” from
ETH Zurich, Switzerland, in 2017. In 2021, Philipp
received his Ph.D. degree in robotics from the Uni-
versity of Zurich, where worked on autonomous
agile drones. His studies focused on trajectory gen-
eration, model predictive control, and vision-based
state estimation, all in the context of low-latency,
agile flight at the limits of the performance envelope
of quadrotors.
Elia Kaufmann (1992, Switzerland) obtained the
M.Sc. degree in Robotics, Systems and Control at
ETH Zurich, Switzerland in 2017. Previously, he
received a B.Sc. degree in Mechanical Engineering
(2014). Since 2017, he is pursuing a Ph.D. degree in
Computer Science at the University of Zurich under
the supervision of Davide Scaramuzza. He is broadly
interested in the application of machine learning
to improve perception and control of autonomous
mobile robots.
Davide Scaramuzza (1980, Italy) received a Ph.D.
degree in robotics and computer vision from ETH
Zurich, Switzerland, in 2008, followed by postdoc-
toral research at both ETH Zurich and the Uni-
versity of Pennsylvania, Philadelphia, USA. He is
a Professor of Robotics and Perception with the
University of Zurich, where he does research at
the intersection of robotics, computer vision, and
machine learning, aiming to enable autonomous,
agile navigation of micro drones using standard and
neuromorphic event-based cameras. From 2009 to
2012, he led the European project sFly, achieving the first autonomous vision-
based navigation of microdrones in GPS-denied environments, which inspired
the visual-navigation algorithm of the NASA Mars helicopter. He has served
as a consultant for the United Nations on topics such as disaster response
and disarmament, as well as the Fukushima Action Plan on Nuclear Safety.
He coauthored the book Introduction to Autonomous Mobile Robots (MIT
Press). For his research contributions, he won prestigious awards, such as a
European Research Council (ERC) Consolidator Grant, the IEEE Robotics
and Automation Society Early Career Award, an SNF-ERC Starting Grant, a
Google Research Award, a Facebook Distinguished Faculty Research Award,
and several paper awards. In 2015, he co-founded Zurich-Eye, today Facebook
Zurich, which developed the hardware and software tracking modules of the
Oculus VR headset, which sold over 10 million units. Many aspects of his
research have been prominently featured in wider media, such as The New
York Times, The Economist, Forbes, BBC News, Discovery Channel.
