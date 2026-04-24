# Aerial_Manipulation_using_Model_Predictive_Control_for_Opening_a_Hinged_Door.pdf

## Page 1

Aerial Manipulation using Model Predictive Control
for Opening a Hinged Door
Dongjae Lee1, Hoseong Seo1, Dabin Kim1, and H. Jin Kim2
Abstract— Existing studies for environment interaction with
an aerial robot have been focused on interaction with static
surroundings. However, to fully explore the concept of an
aerial manipulation, interaction with moving structures should
also be considered. In this paper, a multirotor-based aerial
manipulator opening a daily-life moving structure, a hinged
door, is presented. In order to address the constrained motion
of the structure and to avoid collisions during operation, model
predictive control (MPC) is applied to the derived coupled
system dynamics between the aerial manipulator and the door
involving state constraints. By implementing a constrained
version of differential dynamic programming (DDP), MPC can
generate position setpoints to the disturbance observer (DOB)-
based robust controller in real-time, which is validated by our
experimental results.
I. INTRODUCTION
Physical interaction with a surrounding environment has
been a research topic of growing interest in aerial robotics.
[1] Most studies have been carried out with a hardware
platform called unmanned aerial manipulator (UAM), an
unmanned aerial vehicle attached with one or more manip-
ulators, with which various real-life applications are investi-
gated such as maintenance tasks [2] and autonomous sensor
installation and retrieval operation [3]. One compelling em-
ployment could be an interaction with a moving structure
in the surroundings. Although most of the latest works on
UAM physical interaction [4], [2], [5] have focused on an
inspection on a static structure, further expansion of the
capability of an aerial robot cannot be overlooked. If we
can facilitate a UAM to move any movable surrounding
structure, a more exhaustive exploration can be performed
by accessing once unreachable places, pushing or pulling a
movable structure; also, a more active response to disaster
or rescue operation can be achieved with its augmented
versatility.
There are at least two additional issues in addressing
a movable structure compared to an interaction with a
static counterpart: 1) structure dynamics, and 2) collision
avoidance. Contrary to a static structure, a movable structure
*This material is based upon work supported by the Ministry of Trade,
Industry & Energy(MOTIE, Korea) under Industrial Technology Innovation
Program. No.10067206, ‘Development of Disaster Response Robot System
for Lifesaving and Supporting Fire Fighters at Complex Disaster Environ-
ment’.
1Dongjae Lee, Hoseong Seo, and Dabin Kim are graduate students
of the Department of Mechanical and Aerospace Engineering, Seoul
National University, Seoul, South Korea {ehdwo713, hosung37,
dabin404}@snu.ac.kr
2 H. Jin Kim is a faculty of the Department of Mechanical and
Aerospace Engineering, Seoul National University, Seoul, South Korea
hjinkim@snu.ac.kr
Fig. 1: A composite image of an aerial manipulator opening a
hinged door in the direction of the blue arrow. A transparent
ﬁgure is the initial state of the system, and a vivid ﬁgure
represents the desired state of the system.
contains its own dynamics which often entails signiﬁcant
force/torque reaction. Without proper modeling or estimation
on the movement of the structure, it cannot be guided to the
desired position; furthermore, collision avoidance with this
dynamic structure cannot be guaranteed which is necessary
for safe operation.
As part of such topics, this paper handles the problem of
a UAM opening a hinged door. It deals with a particular
application of a multirotor-based UAM operating a mov-
able structure like doors, windows, and heavy cargo. This
problem requires additional consideration on the movement
of the structure which would involve intrinsic constraints,
which is, in our case, a hinge constraint. Moreover, crash
prevention with a dynamic structure, the door, and a static
structure, a doorframe, is considered along with a self-
collision avoidance in generating a collision-free trajectory.
After modeling the combined dynamics of the UAM and
the hinged door, we applied model predictive control (MPC)
to ensure dynamic feasibility and collision avoidance of a
generated trajectory. State constraints which are formulated
from kinematic relationships are imposed on the optimal
control problem, and the generated trajectory from MPC
is tracked by a disturbance observer-based robust controller
designed in [6].
A. Related Works
In [2], tool handling aerial manipulator is suggested while
in contact with a vertical surface. For a contact-based inspec-
tion task, a motion planning algorithm presented in [7] is val-
idated with experiments using a multidirectional thrust aerial
vehicle [8]. An omnidirectional aerial vehicle for contact-
2020 IEEE International Conference on Robotics and Automation (ICRA)
31 May - 31 August, 2020. Paris, France
978-1-7281-7395-5/20/$31.00 ©2020 IEEE
1237
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 12:21:34 UTC from IEEE Xplore.  Restrictions apply.

## Page 2

based inspection on a curved surface is presented in [5] with
state estimation and disturbance rejection. However, none of
these considers a moving structure, and since the planner
suggested in [7] is based on a sampling-based method, it
cannot be applied for an online scenario.
There exist some studies about an aerial manipulator
coping with a movable structure. In [9], a dual-armed aerial
manipulator is employed to perform three different tasks, and
the one about a movable structure is a valve-turning task.
However, in this scenario, only a rotational motion in the z-
axis is required for the task, and certainly, more issues have
to be considered for less constrained tasks. In [10], the author
presents an experiment of an aerial manipulator operating an
unknown drawer. Coupled dynamics between the UAM and
the drawer are derived, and the desired force is computed
through the velocity of the drawer. However, a structure
with only a translational motion is considered, and collision
avoidance is not explicitly addressed. In [11], an aerial
vehicle opens a hinged door with a proposed mechanism.
Though suitable for this particular purpose, versatility that a
general UAM contains seems to lack in this approach.
MPC has been utilized not only as an optimal controller
for aerial vehicles but also as an optimal planner. In [12], an
explicit MPC is used to generate ofﬂine control policies for
an aerial manipulator interacting with a static structure. Later,
in [13], MPC with SLQ is presented for an online optimal
control input computation. Similar techniques are applied in
many other papers to produce an online optimal trajectory for
a multirotor with a suspended load [14], and for a multirotor
with a network delay [15]. In this paper, MPC is utilized as a
sub-optimal planner generating a trajectory complying with
dynamics and constraints.
B. Contributions
To the best of our knowledge, this paper presents the ﬁrst
attempt for a UAM to open a hinged door while avoiding
collisions. Simpliﬁed dynamics and state constraints are
formulated to construct an MPC problem, and by adopting
a constrained version of differential dynamic programming,
dynamically feasible and online-applicable trajectories sat-
isfying constraints are generated. Finally, our proposed ap-
proach is validated through real experiments.
C. Outline
This paper is structured as follows. In Section II, prob-
lem description with general assumptions throughout the
paper are explained. Kinematics, dynamics and simpliﬁed
dynamics are all derived in Section III. In Section IV,
problem formulation for MPC with various state constraints
guaranteeing collision-free trajectories are presented. Control
framework, experimental setup and results are explained in
Section V, while conclusions are drawn in Section VI.
II. PROBLEM DESCRIPTION
This paper considers the problem of a UAM opening a
hinged door. Unlike interaction with a static structure, the
problem of interacting with a movable structure requires
Fig. 2: Reference frames of the aerial manipulator in the door
opening scenario
deliberation on the movement of the structure as well.
Furthermore, to assure safe operation, constraints on colli-
sion avoidance should be reﬂected. Such collision avoiding
constraints in this scenario would involve avoiding collision
with a door, a doorframe, and itself.
To satisfy the need for both being aware of the structure’s
movement and generating a constraint-abiding trajectory,
MPC is applied. An integrated model of the coupled dy-
namics between the UAM and the hinged door is developed,
and three independent constraints are applied to the optimal
control problem.
Following assumptions are made throughout this paper:
• The weight of the robotic arm attached to the bottom
of the multirotor is negligible compared to that of the
whole system.
• Servomotors in the robotic arm have negligible dy-
namics and are assumed to follow the desired velocity
command with little time delay.
• The end-effector’s tip and the door’s surface are rigidly
connected.
• Physical properties of the door (i.e., mass moment of
inertia, width, height, and position) are known.
With the followed assumptions, equations of motion and
constraints for the system are developed.
III. EQUATIONS OF MOTION
In this section, equations of motion (EoM) of the whole
system including the multirotor-based UAM and the hinged
door are derived. A general dynamical model of the system
is ﬁrst introduced by Lagrange equation, and a simpliﬁed
dynamics is then suggested for real application.
A. Notations
In order to clarify further derivations, basic notations for
variables and parameters that describe the system are prede-
ﬁned. Other additional variables and parameters adopted for
notational simplicity are deﬁned across the paper.
The position of the UAM P ∈R3, the lower part of the
door hinge Ph ∈R3, and the end-effector Pe ∈R3 are
all expressed in the inertial world frame FW centered at
1238
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 12:21:34 UTC from IEEE Xplore.  Restrictions apply.

## Page 3

OW . The attitude of the aerial vehicle and the angle of the
door are each denoted by ZYX Euler angle Φ ∈R3 and
α ∈R1 in FW . For the rotational velocity of the aerial
vehicle in the vehicle’s body frame FB centered at OB,
Ω∈R3 is employed. OB is positioned at the center of mass
(CoM) of the UAM. ηi, where i = 1, · · · , 4, describes each
servomotor angle composing the multirotor-attached robotic
arm in FB, and they are concatenated as H. Conventionally,
˙∗denotes an element-wise time derivative of an arbitrary
matrix ∗. Among these variables, state variables that describe
the coupled EoM of the UAM and the hinged door are
deﬁned as x = [Φ α ˙Φ ˙α H]T ∈R12, while inputs to the
system are deﬁned as u = [ft T ˙Hd]T ∈R8 where ft ∈R1,
T ∈R3, and ˙Hd ∈R4 each denotes a thrust, torque of the
multirotor, and a desired servomotor speed all in FB.
Parameters for the UAM are mA ∈R1, IA ∈R3×3, li ∈
R1, which are mass, mass moment of inertia at OB, and ith
robotic arm’s linkage length, respectively. For the parameters
of the door, mass moment of inertia at Ph ID ∈R1, the
shortest distance from Pe to the door hinge DV ∈R1, the
projected distance of the relative position vector between Pe
and Ph to the door hinge
DH ∈R1, and the door width
Dw ∈R1 and height
Dh ∈R1 are used. Additionally,
RA ∈R1 is used to describe the radius of the multirotor
including blades in the XY plane of the frame FB.
B. Kinematics
To derive a uniﬁed dynamical model of the UAM and the
door while assuring that constraint forces do not appear, La-
grange dynamics are employed. Required kinematic relations
for the derivation are listed in this subsection.
With a rotation matrix Rt from the frame FB to FW and
a position vector d of the end-effector from OB described
in FB, the kinematic constraint between the UAM and the
door can be written as the following:
P + Rtd = Ph + [DV cos α DV sin α DH]T
(1)
Deﬁning a new conﬁguration vector q = [Φ α]T ∈R4,
Jacobian matrices mapping ˙q to ˙P, Ω, and ˙α can be written
as ˙P = Jt ˙q −Rt ˙d, Ω= Jr ˙q, and ˙α = Jα ˙q. Note that q
is chosen to describe the dynamic behavior of the multirotor
and the door independent from the motion of the robotic arm,
based on the assumption of negligible servomotor dynamics.
C. Dynamics
To apply Lagrange equation about q and ˙q, kinetic and
potential energies are calculated as follows:
K = 1
2

˙PT MA ˙P + ΩT IAΩ+ ˙αT ID ˙α

,
P = mAgP T e3
(2)
where MA = diag(mA, mA, mA), and e3 = [0 0 1]T . By
calculating the Lagrange equation with external forces τq, the
EoM of the multirotor and the door can be drawn analytically
from the below equation:
d
dt
∂L
∂˙q −∂L
∂q = τq,
L = K −P,
(3)
The entire system’s EoM from the equation (3) combined
with the motions of the servomotor is as follows:
˙x = f(x, u) =


˙q
M −1
q
(−(Cq ˙q + Gq) + τ)
˙Hd


(4)
where Mq, Cq, and Gq are mass, Coriolis, and gravitational
matrices induced from the equation (3), and τ = τq + τext
with τext denoting unmodeled forces and torques from the
manipulator and the door. Detailed derivation can be found
in [16] where a sufﬁciently slow servomotor speed during
the entire horizon is assumed. Since servomotors are speed-
controlled, with a proper control strategy assuring input
limits, the assumption can be satisﬁed.
D. Simpliﬁed Dynamics
A simpliﬁed dynamical model for the whole system is
derived in this subsection. Necessity for the simpliﬁed dy-
namics can be summarized as follows. Since our approach
to handle the door opening scenario with a UAM includes
an optimal planner in a receding horizon manner, a more
concise model though including all sufﬁcient information of
the system dynamics would be more advantageous in terms
of computation time. With some additional assumptions, the
number of system states can be reduced, and numerical
matrix inversion is no longer required which is mandatory
in the equation (4).
The simpliﬁed version is derived with the following two
assumptions:
• Multirotor’s rotational dynamics is negligible.
• UAM is in a quasi-static state in translational motion
during its operation.
The ﬁrst assumption can be justiﬁed from the fact that a
multirotor’s low rotational inertia and its ability to generate
high torque ensure that the onboard controller is able to
control the angular velocity of the vehicle sufﬁciently fast.
Several other papers [17], [18] include this assumption in
their dynamical model for multirotor planning. Secondly,
considering the door’s relatively higher inertia compared to
that of the UAM, the second assumption can be assumed
without losing generality. Similar research carried out for
operating a drawer with a UAM in [10] also assumed this
quasi-static motion to generate the desired path. Thanks to
the ﬁrst assumption, we can redeﬁne the states and inputs
for the system as xs = [Φ α ˙α H]T ∈R9, and us =
[ft Ωd Hd]T ∈R8, where Ωd denotes a desired angular
velocity of the UAM in FB. Furthermore, according to
the second assumption, introducing an action-reaction force
FR between the UAM and the hinged door, FR can be
written as FR = mge3 + ftRte3 where g is a gravitational
acceleration. Then, the nominal dynamics of the hinged door
can be represented as ID ¨α = −nDT FRDV where nD =
[sin α −cos α 0]T stands for a unit normal vector to the
door surface pointing to the opposite direction to the UAM.
Therefore, the door’s angular acceleration can be rearranged
as ¨α = g(Φ, α)ft, and the whole system dynamics with the
1239
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 12:21:34 UTC from IEEE Xplore.  Restrictions apply.

## Page 4

redeﬁned states xs and inputs us are as follows:
˙xs = fs(xs, us) =


W(Φ)Ωd
˙α
g(Φ, α)ft
˙Hd


(5)
where W(Φ) is a mapping matrix such that ˙Φ = W(Φ)Ω.
IV. TRAJECTORY GENERATION USING
MODEL PREDICTIVE CONTROL
This section contains ingredients and recipes for a model
predictive control problem that produces a desired trajectory
to the robust controller. Starting with a problem formulation,
hard constraints for avoiding a collision, and an optimal
control solver yielding a sub-optimal solution in less than
a second, thus enabling a real-time application are presented
sequentially. By solving an optimal control problem at every
time interval, our MPC algorithm could generate a dynam-
ically feasible and safe trajectory applicable to a real-world
experiment.
A. Problem Formulation
Considering a discretization over time with a time interval
∆t, for the given time horizon HO, an initial state xk, and
an initial input sequence Uk = {uk, · · · , uk+HO−1} at the
kth time element, the MPC problem can be formulated as
follows:
min
Uk Jk = lf(xk+HO) +
k+HO−1
X
i=k
l(xi, ui)∆t,
s.t. xk+1 = fD(xk, uk),
xk ∈X,
uk ∈U
(6)
where fD(xk, uk), X ⊂Rnx, and U ⊂Rnu each denotes
a discretized dynamics, a state constraint set, and an input
constraint set with nx = 9 and nu = 8. Dynamics fD, states
xk, and inputs uk are discretized based on the simpliﬁed
model in equation (5). Since the door’s state is included in
the system states xk, through the quadratic cost function with
respect to state and input error, state and input trajectories
for opening the door while spending minimum energy can
be generated. The terminal cost lf and the stage cost l are
deﬁned with each variable’s desired value denoted with a
superscript of d as follows:
lf(xk+HO) =1
2∥xk+HO −xd
k+HO∥2
L,
l(xi, ui) =1
2∥xi −xd
i ∥2
Q + 1
2∥ui −ud
i ∥2
R
(7)
B. Hard Constraints
To ensure a safe operation for the scenario, several hard
constraints on states should be considered. In this section,
three types of constraints for collision avoidance are han-
dled: self-collision avoidance, door collision avoidance, and
doorframe collision avoidance. These constraints are ﬁrst
derived using kinematic relationship and organized into a
Fig. 3: Conﬁguration of the robotic arm.
state constraint set X as in equation (6). No hard constraints
on inputs are considered in this paper; therefore, the input
constraint set is set to be U = Rnu. First of all, unlike
a general multirotor, our UAM’s additional freedom in the
robotic arm should be carefully managed to avoid a crash
between the multirotor airframe and the robotic arm. To
ensure this self-collision avoidance, following constraints are
devised:
S3
z ≤0
S4
z ≤0
dz ≤0
(8)
where S3, S4, and d are position vectors of the 3rd ser-
vomotor, the 4th servomotor, and the end-effector of the
robotic arm described in FB while having their origins at
OB as in the Fig. 3, and the subscript z in ∗z denotes the
third component of a vector ∗. Since OB is assumed to be
centered at the CoM of the multirotor, and these vectors
are all described in FB, the above constraints imply that
the robotic arm must always stay below the airframe of the
multirotor. Note that all three position vectors S3, S4, and
d are a function of H which can be derived with forward
kinematics; therefore, these constraints can be formulated
only with system states.
The second constraint, which is avoiding collision with
the door, is constructed as follows:
nT
D(Rtd) ≥RA max
θ
n
nT
D

Rt
cos θ sin θ 0T o
(9)
In equation (9), the left-hand side indicates the shortest
distance between the CoM of the UAM and the door surface,
and the right-hand side quantiﬁes the distance between the
CoM of the UAM and the multirotor’s airframe closest to
the door surface. If we introduce nB
D = RT
t nD ∈R3, a door
surface unit normal vector in FB, the equation (9) can be
arranged as follows:
(nB
D)T d ≥RA
q
(nB
Dx)2 + (nB
Dy)2
(10)
Since all variables in this constraint are functions of states
xs only, this second constraint can also be formulated only
with the system states.
The last doorframe avoiding constraint is formulated as
the following:
PHy + RA ≤Py ≤PHy + Dw −RA
(11)
1240
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 12:21:34 UTC from IEEE Xplore.  Restrictions apply.

## Page 5

Fig. 4: Overall control and planning structure of the aerial
manipulation system.
where subscript y of ∗y denotes the second component of
a vector ∗. This equation can be further organized and can
only be expressed with states as
DV sin α + RA + Dw ≤dW
y ≤DV sin α −RA
(12)
where dW (Φ, H) = Rtd is the end-effector position vector
from the CoM of the UAM described in the frame FW .
C. Optimal Control Solver
Based on the problem and constraints formulated in the
subsection IV-A and IV-B, the existing algorithm of the
constrained version of differential dynamic programming in
[19] is employed to handle nonlinear dynamics with state
constraints. This solver could generate an optimized nominal
trajectory satisfying constraints in about 30 Hz with a time
horizon of 1 second.
V. EXPERIMENTS
A. Control Framework
Overall control framework is illustrated in the Fig. 4. Φ,
α, ˙α, and H with f as their superscript denotes ﬁnal target
states xf
s. Since only observable states from the UAM are P,
˙P, Φ, Ω, H, and ˙H, states for the door have to be converted
in state converter in Fig. 4 as:
α = arctan
 
−Phy + Py + dW
y
−Phx + Px + dW
x
!
˙α =







˙Px + dW
Rx + ˙dW
x
−DV sin α
,
if α ̸= nπ
˙Py + dW
Ry + ˙dW
y
DV cos α
,
otherwise
(13)
where n ∈Z, ˙dW = Rt ˙d, and dW
R
= Rt ˆΩd. ˆ∗is a hat
operator describing a cross product between two vectors as
ˆab = a × b. This state conversion is based on the kinematic
equation (1) and its time derivatives.
After the MPC module receives all state information, it
generates state and input trajectories for certain time steps
H∆t. These trajectories are translated back into the aerial
manipulation’s desired position and velocity by the state
converter, using a similar process as in the equation (13).
Among the series of desired position and velocity for both
the multirotor and the robotic arm’s servomotors, the ﬁrst
arrived desired setpoints are subscribed to the controller as
new setpoints. The robotic arm in the ﬂow chart contains an
inherent velocity controller, and therefore desired velocity is
depicted to be directly published to the robotic arm.
Stability is one of the inevitable and challenging problems
in controlling an aerial manipulator. Although the input
trajectory subscribed from MPC could be directly applied
to the ﬂight controller (FCU) for attitude control, which is
Pixhawk 2 in our case, it is hard to guarantee stability during
ﬂight. Consequently, we adopt a disturbance observer-based
robust controller implemented in [6] for position control
where its stability is fully analyzed along with experimental
validations. This controller generates the desired attitude and
angular velocities again to the ﬂight controller by which we
can ensure the aerial manipulation’s stability.
B. Experimental Setup
We use a DJI F550 multirotor frame with 2312E mo-
tors controlled by 420Lite electronic speed controllers. The
robotic arm is composed of ROBOTIS dynamixel XH430
series, and frames of OPEN MANIPULATOR-X. As the
onboard computer, Intel NUC running Robot Operating
System (ROS) in Ubuntu 16.04 executes MPC-based tra-
jectory planner, DOB-based robust position controller, and
navigation algorithm with VICON. As in Fig. 4, the vehicle’s
attitude is controlled by the onboard low-level controller in
Pixhawk 2. In addition, to address a realistic scenario, a door
with its width and height of Dw = 1.2 m, and Dh = 1.6 m
is employed. The weight of the door is about 11kg, and with
these values, the mass moment of inertia of the door can be
calculated as ID ≈5.28 kgm2.
Weight matrices, desired ﬁnal states and inputs for the
optimal problem are designed as
L = Q =diag[5 5 3 9 8 0.05 0.1 0.1 0.1],
R =diag[0.1 5 5 13.5 10 10 10 10],
xf =[0 0 −7π
18
π
9 0 0 π
2 −π
2 0]T
(14)
where xf denotes a ﬁnal desired state which is used as
xd
k+HO = xf. We set the initial door state as α = π/2
and ˙α = 0.
C. Results
In the experiment, an aerial manipulator pushing a cus-
tomized hinged door is conducted. Thanks to the capability
of considering the state constraints in planning trajectory,
the aerial manipulator successfully opens the door without
collision as illustrated in Fig. 1. The history of the states
during the experiment is described in Fig. 5. As expected,
the door angle α tends to converge to the desired ﬁnal value,
implying that the door is sufﬁciently opened. Furthermore,
followed by the changes in the door angle α, the vehicle’s
yaw motion ψ rotates accordingly. However, discrepancies
between the desired and measured states, especially in α and
1241
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 12:21:34 UTC from IEEE Xplore.  Restrictions apply.

## Page 6

Fig. 5: History of the states during the door opening experi-
ment. The black line represents measured value. The dashed
red line describes the predicted state from the MPC module.
The green line represents the desired state of the system xf.
All units on the y axis are degree.
ψ, occur due to the fact that the assumption 3 happens to
be violated intermittently during the experiment. Although
it is assumed that the end-effector is ﬁrmly attached to the
door surface, uncertainty in door parameters and unmodeled
dynamics between the UAM and the door seem to cause a
faster door movement which results in a detachment between
the door surface and the end-effector. Force control strategy
like impedance control seems to be capable of handling this
problem, and we leave it as a future work.
VI. CONCLUSION
In this paper, a systematic methodology for an aerial
manipulator operating a hinged door is presented. Coupled
equations of motion encompassing the aerial manipulator and
the hinged door are ﬁrst derived and later simpliﬁed to be ap-
plicable to an online-solvable optimal control problem. State
constraints guaranteeing a safe trajectory are proposed, and
the formulated MPC problem is solved with a constrained
DDP algorithm. Generated trajectory is then tracked by a
DOB-based robust controller, which provides stability during
execution. For future studies, along with the one mentioned
in the subsection V-C, a robotic arm with higher degrees of
freedom in the end-effector is anticipated to provide better
maneuverability while in interaction.
REFERENCES
[1] F. Ruggiero, V. Lippiello, and A. Ollero, “Aerial manipulation: A
literature review,” IEEE Robotics and Automation Letters, vol. 3, no. 3,
pp. 1957–1964, 2018.
[2] H. W. Wopereis, W. L. Van De Ridder, T. J. Lankhorst, L. Klooster,
E. M. Bukai, D. Wuthier, G. Nikolakopoulos, S. Stramigioli, J. B. En-
gelen, and M. Fumagalli, “Multimodal aerial locomotion: An approach
to active tool handling,” IEEE Robotics & Automation Magazine,
vol. 25, no. 4, pp. 57–65, 2018.
[3] S. Hamaza, I. Georgilas, M. J. Fernandez, P. J. Sanchez-Cuevas,
T. Richardson, G. Heredia, and A. Ollero, “Sensor installation and
retrieval operations using an unmanned aerial manipulator,” IEEE
Robotics and Automation Letters, 2019.
[4] K. Alexis, G. Darivianakis, M. Burri, and R. Siegwart, “Aerial robotic
contact-based inspection: planning and control,” Autonomous Robots,
vol. 40, no. 4, pp. 631–655, 2016.
[5] K. Bodie, M. Brunner, M. Pantic, S. Walser, P. Pf¨andler, U. Angst,
R. Siegwart, and J. Nieto, “An omnidirectional aerial manip-
ulation
platform
for
contact-based
inspection,”
arXiv
preprint
arXiv:1905.03502, 2019.
[6] S. Kim, S. Choi, H. Kim, J. Shin, H. Shim, and H. J. Kim, “Robust
control of an equipment-added multirotor using disturbance observer,”
IEEE Transactions on Control Systems Technology, vol. 26, no. 4, pp.
1524–1531, 2017.
[7] M. Tognon, E. Cataldi, H. A. T. Chavez, G. Antonelli, J. Cort´es, and
A. Franchi, “Control-aware motion planning for task-constrained aerial
manipulation,” IEEE Robotics and Automation Letters, vol. 3, no. 3,
pp. 2478–2484, 2018.
[8] M. Tognon, H. A. T. Ch´avez, E. Gasparin, Q. Sabl´e, D. Bicego,
A. Mallet, M. Lany, G. Santi, B. Revaz, J. Cort´es, et al., “A truly-
redundant aerial manipulator system with application to push-and-slide
inspection in industrial plants,” IEEE Robotics and Automation Letters,
vol. 4, no. 2, pp. 1846–1851, 2019.
[9] M. Orsag, C. Korpela, S. Bogdan, and P. Oh, “Dexterous aerial
robots—mobile manipulation using unmanned aerial systems,” IEEE
Transactions on Robotics, vol. 33, no. 6, pp. 1453–1466, 2017.
[10] S. Kim, H. Seo, and H. J. Kim, “Operating an unknown drawer using
an aerial manipulator,” in 2015 IEEE International Conference on
Robotics and Automation (ICRA).
IEEE, 2015, pp. 5503–5508.
[11] H. Tsukagoshi, M. Watanabe, T. Hamada, D. Ashlih, and R. Iizuka,
“Aerial manipulator with perching and door-opening capability,” in
2015 IEEE International Conference on Robotics and Automation
(ICRA).
IEEE, 2015, pp. 4663–4668.
[12] G. Darivianakis, K. Alexis, M. Burri, and R. Siegwart, “Hybrid predic-
tive control for aerial robotic physical interaction towards inspection
operations,” in 2014 IEEE international conference on robotics and
automation (ICRA).
IEEE, 2014, pp. 53–58.
[13] M. Neunert, C. De Crousaz, F. Furrer, M. Kamel, F. Farshidian,
R. Siegwart, and J. Buchli, “Fast nonlinear model predictive control
for uniﬁed trajectory optimization and tracking,” in 2016 IEEE inter-
national conference on robotics and automation (ICRA). IEEE, 2016,
pp. 1398–1404.
[14] C. Y. Son, H. Seo, T. Kim, and H. J. Kim, “Model predictive control
of a multi-rotor with a suspended load for avoiding obstacles,” in 2018
IEEE International Conference on Robotics and Automation (ICRA).
IEEE, 2018, pp. 1–6.
[15] D. Jang, J. Yoo, C. Y. Son, H. J. Kim, and K. H. Johansson,
“Networked operation of a uav using gaussian process-based delay
compensation and model predictive control,” in 2019 International
Conference on Robotics and Automation (ICRA).
IEEE, 2019, pp.
9216–9222.
[16] D. Lee, D. Jang, H. Seo, and H. J. Kim, “Model predictive control
for an aerial manipulator opening a hinged door,” in 2019 19th In-
ternational Conference on Control, Automation and Systems (ICCAS).
IEEE, 2019, p. to appear.
[17] D. Brescianini and R. D’Andrea, “Computationally efﬁcient trajectory
generation for fully actuated multirotor vehicles,” IEEE Transactions
on Robotics, vol. 34, no. 3, pp. 555–571, 2018.
[18] H. Seo, D. Lee, C. Y. Son, C. J. Tomlin, and H. J. Kim, “Robust
trajectory planning for a multirotor against disturbance based on
hamilton-jacobi reachability analysis,” in 2019 IEEE/RSJ International
Conference on Intelligent Robots and Systems (IROS).
IEEE, 2019,
p. to appear.
[19] B. Plancher, Z. Manchester, and S. Kuindersma, “Constrained un-
scented dynamic programming,” in 2017 IEEE/RSJ International
Conference on Intelligent Robots and Systems (IROS).
IEEE, 2017,
pp. 5674–5680.
1242
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 12:21:34 UTC from IEEE Xplore.  Restrictions apply.
