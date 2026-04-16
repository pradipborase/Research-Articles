# Sim-to-Real Transfer in Reinforcement Learning for Maneuver Control of a Variable-Pitch MAV.pdf

## Page 1

Sim-to-Real Transfer in Reinforcement
Learning for Maneuver Control of a
Variable-Pitch MAV
Zhikun Wang
and Shiyu Zhao
Abstract—Reinforcement
learning (RL)
algorithms
can
enable high-maneuverability in unmanned aerial vehicles
(MAVs), but transferring them from simulation to real-world
use is challenging. Variable-pitch propeller (VPP) MAVs offer
greater agility, yet their complex dynamics complicate the
sim-to-real transfer. This article introduces a novel RL frame-
work to overcome these challenges, enabling VPP MAVs to
perform advanced aerial maneuvers in real-world settings.
Our approach includes real-to-sim transfer techniques, such
as system identiﬁcation, domain randomization, and curricu-
lum learning to create robust training simulations and a sim-
to-real transfer strategy combining a cascade control system
with a fast-response low-level controller for reliable deploy-
ment. Results demonstrate the effectiveness of this framework
in achieving zero-shot deployment, enabling MAVs to perform
complex maneuvers such as ﬂips and wall-backtracking.
Index Terms—Aircraft control, control systems, learning
control systems.
I.
INTRODUCTION
I
N recent years, the ﬁeld of robotics has witnessed remarkable
progress in developing intelligent and agile autonomous sys-
tems [1], [2], [3]. Unmanned aerial vehicles (MAVs) have par-
ticularly emerged as a focal point of research and innovation
due to their widespread applications across domains such as sur-
veillance [4], reconnaissance [5], disaster management [6], and
environmental monitoring [7]. Despite these promising applica-
tions, achieving advanced aerial maneuvers with MAVs
presents substantial challenges for future development. The
complexity of performing sophisticated maneuvers, such as
rapid rotational movements and precise positional adjustments,
demands a delicate balance between stability, agility, and preci-
sion. MAVs must be able to adapt to dynamic environments,
which requires sophisticated control systems capable of manag-
ing these diverse and often conﬂicting requirements.
Traditional ﬁxed-pitch MAVs have demonstrated effective
ﬂight control for various tasks [8], [9], [10]. However, when it
comes to performing complex aerobatic maneuvers that require
rapid and precise adjustments for large-scale MAVs, ﬁxed-pitch
rotors reveal signiﬁcant limitations. The ﬁxed pitch MAV relies
on the change of rotor speed to vary thrust, which is limited by
the rotor’s moment of inertia. This constraint further restricts its
ability to perform rapid changes in both positive and negative
thrust, which are essential for advanced maneuvers. Conse-
quently, the lack of variable pitch control in ﬁxed-pitch systems
impedes their ability to adapt to the dynamic requirements of
complex aerobatic tasks.
To overcome these limitations, researchers have explored the
use of variable-pitch-propeller (VPP) MAVs. VPP systems allow
for independent adjustment of each actuator’s pitch angle, which
signiﬁcantly enhances the vehicle’s maneuverability and control
authority [11], [12]. By enabling dynamic changes in thrust mag-
nitude and magnitude, VPP mechanisms facilitate more complex
aerial maneuvers, such as agile ﬂips, precise hovering, and rapid
directional changes. This increased ﬂexibility allows MAVs to
perform advanced aerial feats and adapt to a wider range of oper-
ational scenarios. However, the integration of VPP systems also
introduces additional complexity in the control algorithms
required to manage these dynamic capabilities effectively.
Although VPP mechanisms improve MAV control, tradi-
tional controllers still face limitations. The aforementioned stud-
ies [13], [14] have primarily addressed control methods for
achieving speciﬁc equilibrium states for maneuvers. However,
current methods are weak facing high maneuvers particularly in
handling complex dynamic behaviors and aerodynamic uncer-
tainties. Reinforcement learning (RL) has emerged as a power-
ful tool to overcome these limitations [15], [16]. RL trains
agents to maximize rewards through trial and error [17] and has
proven effective in managing complex, high-dimensional chal-
lenges and long planning trajectories [18], [19]. The utilization
of RL allows us to develop an autonomous learning agent that
uses real-time sensory information to adapt and reﬁne its control
policies through the process of trials and errors [20], [21], [22].
While RL has proven beneﬁcial in enhancing MAV control,
transitioning RL to practical applications with VPP mechanisms
presents unique challenges. First, it requires the design of a VPP
MAV system that can execute rapid and precise pitch angle
adjustments, essential for advanced maneuvers. Secondly, effec-
tive integration demands crafting accurate state representations,
Received 27 September 2024; revised 30 December 2024; accepted
20 March 2025. Date of publication 15 April 2025; date of current
version 5 September 2025. This work was supported by the National
Natural
Science
Foundation
of
China
under
Grant
62473320.
(Corresponding author: Shiyu Zhao.)
The authors are with WINDY Lab, Department of Artiﬁcial Intelligence,
Westlake University, Hangzhou 310024, China (e-mail: wangzhikun@
westlake.edu.cn; zhaoshiyu@westlake.edu.cn).
Digital Object Identiﬁer 10.1109/TIE.2025.3558030
1557-9948 © 2025 IEEE. All rights reserved, including rights for text and data mining, and training of artificial intelligence and similar technologies.
Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html
for more information.
IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS, VOL. 72, NO. 10, OCTOBER 2025
10445
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:32:50 UTC from IEEE Xplore.  Restrictions apply.

## Page 2

reward functions that capture the desired dynamics of complex
maneuvers, and controllers capable of coordinating motor adjust-
ments. Furthermore, while simulation-based training offers a cost-
effective means of data collection, it often involves inherent
discrepancies with real-world conditions. Our research aims to
bridge this gap by transitioning RL-based controllers from virtual
simulations to real-world applications, focusing on achieving
agile control over VPP MAVs amidst signiﬁcant aerodynamic
interference (Fig. 1). This includes demonstrating advanced
maneuvers, such as ﬂips and wall-backtrack, which showcase sig-
niﬁcant improvements in maneuver robustness and versatility.
The contributions of this article are as follows.
1) Development of an RL deployment framework: We
developed an RL deployment framework to enable
highly agile ﬂight for VPP MAVs. This framework inte-
grates curriculum learning, domain randomization, cas-
cade control systems, and system twins, effectively
minimizing the reality gap and ensuring seamless transi-
tion from simulation training to real-world performance.
2) Creation of a high-performance VPP MAV testing plat-
form: We also created a high-performance testing plat-
form
for
VPP
MAVs,
featuring
high-frequency
hardware, quick-response MAVs, and auxiliary compo-
nents. This platform signiﬁcantly enhances thrust control
precision and maneuverability, enabling reliable deploy-
ment in real-world scenarios.
As a result, the proposed controller is successfully deployed
to the practical with zero-shot transfer, achieving advanced aero-
batic maneuvers such as ﬂips and wall-backtracking. This con-
ﬁrms the effectiveness of our proposed framework in enabling
agile and precise control for VPP MAVs without the need for
extensive prior tuning or adjustment.
II.
METHODOLOGY
A.
Notation and System Dynamics
Due to the fact that the maneuver is conﬁned to a two-
dimensional plane, we opted for a planar MAV as the control
scheme in order to simplify experimentation [23]. A variable-
pitch propeller actuator is equipped with a servo mechanism
capable of adjusting the thrust magnitude of its propellers. This
innovative design imparts the MAV with enhanced agility and
dynamic capabilities. The planar VPP MAV is modelled as a
rectangular cuboid with uniform mass distribution.
The MAV and the deﬁnition of the coordinate system is rep-
resented by a 2-D dynamic model, as shown in Fig. 2. The posi-
tion and velocity of the center point of the MAV is p 2 R2 and
v 2 R2, respectively. The orientation is denoted as R 2 R22,
which is the rotation matrix from the body frame to the global
frame, where h 2 R is the angle difference between body and
world frames. The angular speed is q 2 R. Let m and l denote
the mass and half length of the stick, I the moment of inertia, fi
is the thrust generated by the ith actuator, f and s are the total
thrust and torque given by
f ¼ f1 þ f2
s ¼ ðf1 −f2Þl:
(1)
Then, the overall state vector is ½p,h,v,q 2 R6 and the
dynamic model is
p
: ¼ v
mv
: ¼ −mge2 þ fRe2
R
:
¼ R½q
_q ¼ −s=I
(2)
Fig. 2.
Illustration of the plane variable-pitch MAV and the deﬁnition of
the coordinate system.
Fig. 1.
Illustration of the plane variable-pitch MAV achieve maneuver
approach. The virtual simulation environment is built with real-world sys-
tem parameters, and the real-world implementation directly employs the
trained controller from the simulation.
10446
IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS, VOL. 72, NO. 10, OCTOBER 2025
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:32:50 UTC from IEEE Xplore.  Restrictions apply.

## Page 3

where g ¼ 9:81 is the gravity acceleration, e2 ¼ ½0,1T and
R ¼
cos h
−sin h
sin h
cos h


,
½q ¼
0
−q
q
0


is the planar rotation matrix. For instance, considering the target
position pt and angle ht, the observed relative position is Dp ¼
pt −p and relative angle is Dh ¼ ht −h.
B.
Task Formulation
High-maneuver control of a VPP MAV involves two main
objectives: achieving the desired attitude rapidly and preventing
the MAV from dropping to the ground. During aggressive
maneuvers such as ﬂips, the MAV must execute swift orienta-
tion changes while maintaining sufﬁcient lift to sustain altitude.
Intuitively, an agent that completes a maneuver must operate at
high speeds and make precise control adjustments, which
increases the probability of failure due to the complex dynamics
involved. Therefore, the optimal maneuver control strategy
must deﬁne the best trade-off between these competing objec-
tives of agility and stability.
To effectively utilize RL algorithms, we have carefully
designed the observation spaces based on the analysis of the sys-
tem
dynamics
as
st ¼ ½Dpx,Dpy,vx,vy,sinðDhÞ,cosðDhÞ,q,
Cpx,Cpy 2 R9: These observations represent the MAV’s rela-
tive position, velocity, relative angle (in both sine and cosine
forms), angular velocity and accumulated position residuals,
respectively.
By representing the angle Dh using its sine and cosine com-
ponents, we avoid discontinuities that occur at the 6p bound-
aries. This approach maps the angle to a connected set of
rotation S1, providing a continuous representation that simpliﬁes
learning and improves the network’s ability to generalize [24].
The position residual integral is deﬁned as Cp ¼ Rt
n¼0cnDpðnÞ,
where DpðnÞ represents the position error at time step n and c ¼
0:9 is a smoothing coefﬁcient that gradually decreases the inﬂu-
ence of past errors, preventing numerical instability over long time
intervals. Including Cpx and Cpy in the state vector allows the
agent to account for accumulated deviations from the desired tra-
jectory, improving control accuracy.
The action vector corresponds to the control inputs for the
MAV and is deﬁned as at ¼ ½f,q 2 R2, corresponds to the
desired total thrust and angular velocity. Each action dimension
is deﬁned within the range ½−1,1. These normalized actions are
mapped to real-world values based on pretested parameters,
where thrust commands are mapped to a maximum value of
610 N, and angular velocity commands are mapped to a maxi-
mum of 612 rad=s. The mapped values are then processed
through the low-level angular velocity control and control allo-
cation algorithms to compute the servo outputs for each
propeller.
C.
Reward Design
The primary objective of the network is to ensure that the
MAV reaches the desired target point at the correct angle. A
well-designed reward function guides the learning process and
effectively shapes the behaviors of the agent. The reward
function is composed of ﬁve constituent terms, encompassing
position error, orientation error, ﬂight stability, and the integral
of position error. The rationale underlying this reward function
is twofold: to facilitate the accurate tracking of the desired posi-
tion by the aerial vehicle and simultaneously enhance the overall
stability of its motion.
1) The ﬁrst component of the reward function is the posi-
tion reward. To strongly penalize the reward if the posi-
tion error is too far away from the reference point, the
position reward is given by rp ¼ 1=ð1 þ 10kDpk2
2Þ.
2) The orientation reward is intended to minimize the angle
difference between the current and target orientations.
Speciﬁcally, since it’s a planar maneuver, the angle dif-
ference should be less than p. Otherwise, the system will
be encouraged to ﬂip from the other side. The orientation
reward is deﬁned as ro ¼ ð1 þ cosðDhÞÞ=2.
3) The stability reward maintains steadiness at the target
position. It is determined as rv ¼ 1=ð1þ j v j2
2Þrp and
rx ¼ 1=ð1 þ kxk2
2Þrp to account for both linear and
angular velocity stability.
4) The current reinforcement learning input only represents
the system’s current state, which may result in uncor-
rected steady-state errors. To detect and correct these
long-term errors, we incorporated decaying positional
difference integral information into the controller. This
integral information accumulates positional differences
and gradually decays, helping the controller to identify
and correct long-term errors, thereby enhancing the sys-
tem’s stability and accuracy. The integral of the position
residual is given by ri ¼ 1=ð1 þ kCpk2
2Þ.
In total, the reward design is given as
R ¼ wprp þ rpðworo þ wvrv þ wxrxÞ þ wiri
(3)
where wp, wp, wv, wx and wi are corresponding weights.
D.
Policy Training
We train our agent using the proximal policy optimization
(PPO) approach. A typical PPO neural network (NN) comprise
two parts, an actor NN and a critic NN. The actor NN is an agent
that works in the environment whereas the critic NN evaluates
the performance of the agent.
1)
Training Environment: Our reinforcement learning envi-
ronment is developed based on Isaac Gym, as illustrated in
Fig. 1. Isaac Gym is a GPU-based parallel robotic simulation
environment designed for research and experimentation in
robotics and reinforcement learning. It provides parallel physics
simulation capabilities, enabling the training and validation of
agents across various environments, thereby signiﬁcantly reduc-
ing simulation time. The overall parallel environments rollouts
on up to 8192 which helps to increase the diversity of the col-
lected environment interactions.
2)
Asymmetric Network Structure: We designed different
network structures for the actor and critic networks. The actor
network is optimized for deployment on a microcontroller,
which imposes limitations on network size due to its hardware
constraints. Consequently, the actor network’s ﬁrst layer
WANG AND ZHAO: SIM-TO-REAL TRANSFER IN RL FOR MANEUVER CONTROL
10447
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:32:50 UTC from IEEE Xplore.  Restrictions apply.

## Page 4

comprises 96 nodes with the ReLU activation function, while
the second layer consists of 64 nodes with the Tanh activation
function. The subsequent layers are fully connected. In contrast,
the critic network is exclusively used during the training phase
and does not require deployment on the microcontroller. There-
fore, it is designed with a larger network size to leverage more
parameters for better performance. Speciﬁcally, the critic net-
work consists of two parts. The ﬁrst part is an LSTM network
that compresses information over ﬁve time steps. The second
part is a two-layer MLP, with each layer containing 512 nodes.
III.
REAL-TO-SIM TRANSFER
A major challenge in applying reinforcement learning to real-
world scenarios is the real-to-sim gap, which arises from the
limitations of simulators in accurately representing reality. This
gap occurs when actions in the simulation lead to outcomes that
differ from what is expected in the real world, resulting in sig-
niﬁcant discrepancies. To bridge this gap, we have employed
several strategies.
A.
System Identification
The most straightforward way is to improve the simulator’s
realism through careful calibration. First, we add more detailed
simulation to indicate the delays in control signals, and latency
in actuator response:
1) Adding a ﬁrst-order transfer function GðsÞ ¼ ð1=Ts þ 1Þ
to servo adjustments, with the parameter determined
from the relationship between thrust commands and their
response characteristics.
2) Incorporating aerodynamic drag fd ¼ kd j v j v into the
dynamics model. The drag coefﬁcient kd was estimated
using least-squares ﬁtting, based on thrust commands
and the corresponding recorded acceleration values.
3) Implementing a disturbance model inﬂuenced by the
propeller angle for motor speed. The variation in motor
speed with respect to propeller angle changes was simu-
lated by ﬁtting a polynomial equation to the recorded
thrust test data.
Second, to address the impact of auxiliary equipment on the
MAV’s movement, this article replicate these facilities within
the simulation platform. This approach effectively reduces envi-
ronmental inﬂuence.
B.
Domain Randomization Methods
To further enhance the training process, we use domain ran-
domization methods to highly randomize the parameters in sim-
ulation in order to cover the real distribution of the real-world
data despite the bias between the model and real world.
1) Adding noise based on the accuracy of the sensors.
2) Randomizing
variations
in
system
identiﬁcation
parameters.
Observation noise and aerodynamic uncertainty are scaled
according to the difﬁculty level. This scaling allows the network
to initially focus on acquiring fundamental control skills in a
less noisy and more predictable environment. As the difﬁculty
level increases, the network is gradually exposed to higher lev-
els of noise and uncertainty, promoting the development of
robust control strategies capable of handling complex real-
world conditions.
Additionally, we employ parameter randomization within the
system to broaden the observation and action domains. This
ensures that the neural network learns the correct relationship
between observations and actions, minimizing data-dependent
parameter sensitivity.
C.
Curriculum Learning
A dynamic learning rate approach is employed to adjust the
learning rate adaptively during training. Initially set at 3e−4, the
learning rate is maintained for the ﬁrst 10% of the total epochs.
Subsequently, it is linearly reduced to 9e−5 by the 70% epoch
mark and remains constant at this value until the completion of
the training process.
We used curriculum learning method by incorporating a task
difﬁculty level into the training environment to facilitate a pro-
gressive learning process. Initially set at 0 for the ﬁrst 10% of
the total training epochs, the difﬁculty level is linearly increased
to 1 by the midpoint of the training and remains constant there-
after. During the early stages of training, with difﬁculty levels
below 0.4, tasks are simpliﬁed to require only one reward crite-
rion per episode, such as either the position or angle target.
D.
Spectral Normalization
In neural network training and deployment, it is crucial to
ensure that the network’s output responds to input changes in a
stable and controlled manner. If the network is overly sensitive
to minor input changes, it becomes susceptible to noise and small
input errors, which can negatively affect its generalization ability
and stability. To prevent large differences in the output caused
by small perturbations in the input, we applied spectral normali-
zation to the actor network. Speciﬁcally, during training with
PPO, we imposed Lipschitz constraints with constant L on all
layers. By considering the entire network as a composite function
f mapping from state s to action a, the scaling relationship com-
plies with the following equation:kfðs1Þ −fðs2Þk=ks1 −s2k  L,
where s1 and s2 are two different states, k  k is L2-norm of the
Hilbert space R. Since activation functions like ReLU and Tanh
naturally satisfy the 1-Lipschitz condition, applying Lipschitz
constraints to the layers of the network ensures that the overall
Lipschitz constant is controlled. This approach allows us to build
a network that is robust to input perturbations, thereby improving
the reliability and stability of the policy.
IV.
SIM-TO-REAL DEPLOYMENT
In addition to the real-to-sim transfer challenge, deployment
presents another issue. Real-world conditions, such as aerody-
namics, wind turbulence and sensor errors, introduce unpredict-
able variables that differ from the virtual environment. These
discrepancies create performance gaps, as trained models may
struggle to generalize when dealing with the complex dynamics
and physical limitations of real-world scenarios, especially
10448
IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS, VOL. 72, NO. 10, OCTOBER 2025
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:32:50 UTC from IEEE Xplore.  Restrictions apply.

## Page 5

during maneuvers. To address this, we designed and imple-
mented a comprehensive cascade control strategies to mitigate
the sim-to-real challenge.
A.
System Twin
To migrate the entire system from simulation to reality, we
replicate the same structure in both the simulated and real envi-
ronments. The system architecture for the VPP MAV control is
shown in Fig. 3.
The system is composed of two main subsystems: the RL
training system and the practical validation system. Both use the
same RL-based hierarchical control system, which includes a
neural network controller, a high-frequency angular velocity PD
controller, and a power distribution system.
Additionally, apart from the shared system described above,
both the virtual training system and the practical validation sys-
tem have their own unique subsystems. In the virtual training
system, we have developed a sample-based thrust simulation
system to ﬁt the thrust response latency in the real-world envi-
ronment. This system aims to mitigate the dynamic response dif-
ferences between the simulation and reality. In the validation
environment, we have also implemented an additional thrust
adaptive control system, and an indoor positioning system utiliz-
ing data from multiple sources. The indoor positioning system
contains a Vicon motion capture system to estimate the position,
orientation, and velocity of the VPP MAV, alongside an
onboard inertial measurement unit (IMU) for estimating angular
velocity.
B.
Cascade Control
The control system is hierarchically organized into three
interconnected layers. At the base is the adaptive actuator
control layer, which is responsible for adjusting motor speeds
and servo angles to generate the desired thrust in both simulated
and real-world environments. This layer receives the target
forces for each actuator and computes the corresponding motor
and servo commands, ensuring accurate actuation and seamless
performance across diverse conditions.
Building on this base, the angular velocity control layer is
designed to manage rotational dynamics effectively. By process-
ing the target angular velocities, it calculates and outputs the
required actuator forces necessary to facilitate precise orienta-
tion adjustments. This enables the MAV to execute agile ﬂight
maneuvers and rapid attitude transitions, which are critical for
high-performance operations.
At the highest level, the system incorporates an RL-based
control layer that employs reinforcement learning techniques to
optimize control strategies. This layer enhances the MAV’s
adaptability and decision-making capabilities by processing the
current states and desired positions to determine the target angu-
lar velocities. Furthermore, it integrates a perception module for
sensor fusion, enabling accurate state estimation by combining
data from multiple sensors.
To ensure robust high-agility control, a Kalman ﬁlter was
developed to address the challenges of noise and latency inher-
ent in the sensor systems. The IMU provides high-frequency
(1000 Hz) measurements of angular velocity and linear accelera-
tion, which are essential for capturing rapid dynamics but are
prone to noise and drift. Complementing this, the Vicon system
delivers highly accurate position and orientation data at a lower
frequency (100 Hz), offering stability and precision but with
limited responsiveness to fast dynamics. The Kalman ﬁlter com-
bines these complementary data sources, balancing responsive-
ness and accuracy to provide reliable state estimation.
To seamlessly transition the entire system from simulation to
reality, we implemented the same hierarchical structure in both
environments. The system architecture for the VPP MAV con-
trol is illustrated in Fig. 4 and comprises two main subsystems:
the RL training system and the practical validation system. Both
subsystems utilize the same RL-based hierarchical control sys-
tem, which includes a neural network controller for high-level
strategy, a high-frequency angular velocity PD controller for
precise orientation control, and a power distribution system.
C.
Adaptive Actuator Controller
Secondly, in conventional MAV systems, ﬁxed-pitch propel-
lers generally create a linear relationship between throttle input
and motor speed. Conversely, the mapping of throttle input to
motor control for VPP MAVs differs due to the additional com-
plexity introduced by the variable-pitch mechanism. A VPP
actuator incorporates two controllable components: a motor and
a servo. Consequently, implementing a low-level adaptive con-
troller speciﬁc to VPP actuators is essential. This adaptive con-
troller is required to modulate throttle input alongside pitch
changes to accommodate variations in propeller blade resistance
and maintain consistent motor speed.
Given that the VPP actuator constitutes a multiple-input, mul-
tiple-output system, our control loop design aims to decouple its
Fig. 3.
Overview of the proposed VPP MAV control system.
WANG AND ZHAO: SIM-TO-REAL TRANSFER IN RL FOR MANEUVER CONTROL
10449
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:32:50 UTC from IEEE Xplore.  Restrictions apply.

## Page 6

two input-output relationships. To achieve this, we initiate a
series of tests to elucidate the interdependencies among blade
angle, rotational speed, and thrust. Subsequently, we individu-
ally model and ﬁt these relationships, thereby deriving the vary-
ing rotational speeds under different operational conditions. By
utilizing the derived thrusts, we employ forward control to stabi-
lize the actuator’s rotational speed. This is seamlessly integrated
with a rotational speed feedback control mechanism, ensuring
the actuator’s stability and effective management of diverse
operational demands.
Based on actual tests of thrust, speed, and blade angle, we
found that the actuator produces signiﬁcant vibrations and a
decrease in thrust when the speed and blade angle are too large.
To ensure that the thrust meets the algorithm requirements, we
tested the motor’s operating range of the MAV and found that
the current weight of the MAV requires the motor to maintain at
least 4000 rpm. Also, when the speed exceeds 5000 rpm, the
blade vibration increases rapidly. Therefore, we used 4500 rpm
as the target speed for control and tested and ﬁtted the formula
between the speed, servo angle, and thrust.
Assuming the propeller speed is almost steady, the thrust T
and drag D of propellers are modelled by
T ¼ kTxa
(4)
D ¼ kD1x2 þ kD2x2a2 þ kD3xa
(5)
where a is the propeller pitch angle, x is the propeller rotat-
ing speed, kT,kD1,kD2 and kD3 are constants relating to the
physical and aerodynamic properties of the propellers.
The motor-propeller equation can be modeled by
I _x ¼
ðV −x=kVÞ 1
R −i0

 1
kQ
−D
(6)
i ¼ ðV −x=kVÞ 1
R
(7)
where V is the voltage applied to the motor, i is the current,
kV,kQ,R and i0 are the motor related constants. Substituting
(5) and (7) to (6) gives
I _x ¼ ði −i0Þ 1
kQ
−kD1x2 −kD2x2a2 −kD3xa
which reduces to
a ¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
I _x −ði −i0Þ 1
kQ þ kD1x2
−kD2x2
þ
kD3
2kD2x


s
−kD3
2kD2x:
(8)
According to (8), we could ﬁnd that propeller pitch angle is
related to i,x and _x. Recall the assumption that the propeller is
working at an almost constant speed which gives
_x ¼ 0
and x is a constant, we can simplify (8) to
a ¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
g0ði −i0Þ þ g1
p
−g2:
(9)
Therefore, by measuring the current motor speed and electric
current, we can estimate the current thrust using data obtained
from pretests.
We ﬁrst tested the effectiveness of thrust control using a ﬁt-
ting curve designed based on polynomial regression. Due to the
complexity of the VPP structure and the presence of gaps
between structural components during installation, signiﬁcant
discrepancies emerged between thrust and servo control angle
after overall assembly, resulting in thrust errors during practical
VPP usage, as shown in Fig. 5(a). Furthermore, the nonlinear
variation in blade resistance due to changes in blade pitch angle
also contributes to thrust errors during practical VPP usage.
Subsequently, we evaluated the thrust response of the VPP
actuator under the autonomous adaptive thrust algorithm con-
trol. As depicted in the Fig. 5(b), the thrust response was notably
more accurate.
Fig. 4.
Overview of the components and data ﬂow for the practical planar VPP MAV system.
10450
IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS, VOL. 72, NO. 10, OCTOBER 2025
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:32:50 UTC from IEEE Xplore.  Restrictions apply.

## Page 7

V.
EXPERIMENT
A.
Experiment Setup
1)
VPP MAV Hardware: In this article, the VPP MAV and
its components, along with the data ﬂows, are depicted in the
middle of Fig. 4. The aircraft’s frame is crafted from a single
5 mm thick carbon ﬁber board, chosen to achieve both a light-
weight structure and reduced vibrations. To connect servos and
VPP actuators, 3D printing is utilized for producing all neces-
sary connectors.
The pitch control mechanisms, which are designed for small
helicopter tail rotors, are depicted on the right side of Fig. 4. Ser-
vos are positioned away from the actuator, closer to the center,
in order to reduce the total inertia. A pushrod is employed to
actuate the propeller pitch adjustments.
The deployment process utilized an optimized actor network
and FreeRTOS to ensure efﬁcient task management and real-
time performance. The actor network, featuring a compact two-
layer structure, delivers fast computation and precise control for
high-frequency tasks. FreeRTOS facilitated synchronized opera-
tion of critical processes, such as RL-based control at 100 Hz
and gyro ﬁltering at 1000 Hz. These efﬁcient methods allow the
system to maintain real-time performance without interruptions
or delays.
2)
Plane Support Hardware: In order to migrate the MAV’s
maneuver from the three-dimensional plane to two-dimensional
space, we attempted to establish an auxiliary device that can
ensure that the MAV is limited to movement within a vertical
plane while being inﬂuenced by the gravitational environment.
This support frame design is constructed by two parallel linear
sliding guides and a basic support frame, shown in Fig. 1.
Despite our efforts to balance the mass on both sides of the slid-
ing guides, the remaining inertia caused by its mass cannot be
completely eliminated. This residual effect may still impact the
MAV’s
trajectory
in
space,
thereby
introducing
certain
discrepancies between its behavior and true three-dimensional
dynamics. However, it is important to note that the overall
mobility of the MAV is not signiﬁcantly affected.
B.
Baseline Comparison on Methods
We ﬁrst benchmarked the performance of our policy in train-
ing environments across four different setups: the basic setup
(VA), the setup with trigonometric function angle representation
(TA), the setup with position integral information (PI), and the
setup incorporating both trigonometric function angle represen-
tation and position integral information (All). The results are
presented in Fig. 6.
The data indicates that incorporating position integral infor-
mation signiﬁcantly enhances the agent’s performance. In con-
trast, the trigonometric function angle representation provides a
modest improvement when applied in a visual environment,
likely due to the reduced noise and uncertainty in such settings.
Additionally, we evaluated the policy under different initiali-
zation conditions, including a broader range of randomizations
and noisy situations to better simulate practical scenarios.
Table I summarizes the average performance over 100 randomly
sampled trajectories. Our method achieved a success rate of
98% in the target maneuver test, even with noisy and random-
ized initial states. Furthermore, it yielded the lowest position
error compared to policies trained with only partial methods or
without our proposed methods. While the randomized initializa-
tion approach enhances the drone’s ability to handle diverse
conditions, it also introduces extreme or challenging scenarios
that are inherently difﬁcult to recover from, increasing the likeli-
hood of crashes. Additionally, different RL networks exhibit
Fig. 5.
Experimental results compare the tracking of target thrust by a
VPP actuator using different methods, where the commanded thrust is
represented by the red dotted line and the response thrust is depicted by
the blue solid lines. (a) Shows the thrust response with polynomial regres-
sion, whereas. (b) Shows the thrust response with adaptive actuator
controller.
Fig. 6.
Baseline reward comparison of the proposed methods with basic
setup (VA), with trigonometric function angle representation (TA), with
position integral information (PI), and with both of them (All).
TABLE I
PERFORMANCE ON RANDOMLY GENERATED INITIAL STATES
Setups
Pos. Err.
Inv. Pos. Err.
Fail Rate
VA
0.035 m
0.082 m
8%
TA
0.038 m
0.073 m
8%
PI
0.022 m
0.034 m
6%
All
0.017 m
0.023 m
2%
Note: We report the tracking error and number of crashes on 100
test tracks.
WANG AND ZHAO: SIM-TO-REAL TRANSFER IN RL FOR MANEUVER CONTROL
10451
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:32:50 UTC from IEEE Xplore.  Restrictions apply.

## Page 8

varying levels of adaptability; some perform well in typical sce-
narios but struggle under extreme conditions, leading to failures.
C.
Real-World Result and Analysis
Finally, we test the performance of our policy-generated con-
troller on a practical VPP MAV to verify its transferability.
1)
Flip Experiment: In the Flip experiment, the primary goal
is to achieve precise positioning and orientation after the ﬂip
while minimizing additional movement. Therefore, higher
weightings are assigned to position (wp ¼ 0:8) and orientation
(wo ¼ 0:8)
to
emphasize
accuracy.
Meanwhile,
velocity
(wv ¼ 0:2) and angular velocity (wx ¼ 0:2) are assigned lower
weightings, reﬂecting less importance on movement dynamics
during the maneuver. Integral error (wi ¼ 0:2) is similarly
weighted to ensure stability without overemphasizing cumula-
tive deviations.
The experimental setup involves commanding the MAV to
execute ﬂip maneuvers, as illustrated in the Fig. 7(b1)–7(b4),
similar to the simulation scenario shown in Fig. 7(a1)–7(a4).
The complete states, trajectories of the MAV and its correspond-
ing commands are shown in Fig. 8(a).
It can be found that there is a steady-state error in the current
system, which has two main causes. First, our practical tests
revealed that the lack of torque control, combined with gaps
between the slider and the slide rail, causes the slider to get
stuck during operation. This issue is particularly pronounced
when the control outputs are small, as the provided thrust is
insufﬁcient to overcome the sticking. In these situations, the
small control outputs fail to generate enough thrust to free the
stuck slider, preventing the complete elimination of the steady-
state error. Second, due to the limitations of the microcontrol-
ler’s performance, we are currently using residual integral as an
input to try to reduce this issue. Although this method has allevi-
ated the problem to some extent, there is still room for
improvement.
2)
Wall-Backtrack Experiment: The wall-backtrack experi-
ment is designed to evaluate the MAV’s performance during a
complex aerobatic maneuver. This maneuver requires the MAV
to transition from a hover position, execute a half-roll to achieve
a vertical orientation, and then backtrack to its original
hover position.
In the wall-backtrack experiment, the goal shifts to ensuring
the MAV reaches a vertical orientation as a priority while main-
taining sufﬁcient position control to avoid ground collisions. Ori-
entation (wo ¼ 1) is given the highest weighting to prioritize the
vertical alignment. Position (wp ¼ 0:5) is moderately weighted
to ensure the MAV avoids falling but does not over-constrain its
Fig. 7.
VPP MAV performs maneuvers in the simulation and real-world with the trained NN. (a1) to (a4) Illustrate the performance for the planar
variable-pitch MAV perform ﬂips from an upward attitude to a downward one in simulated environment, where (b1) to (b4) are the practical images. (c1)
to (c4) Depict the wall-backtrack maneuver in simulated environment, where (d1) to (d4) are the real-world performance. The MAV aims to locate at 1.2
m in x axis and 1.25 m in y axis.
10452
IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS, VOL. 72, NO. 10, OCTOBER 2025
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:32:50 UTC from IEEE Xplore.  Restrictions apply.

## Page 9

position. Lower weightings for velocity (wv ¼ 0:1), angular
velocity (wx ¼ 0:1), and integral error (wi ¼ 0:1) reﬂect a
reduced emphasis on these factors, as movement speed and
cumulative deviations are less critical in this context.
Initially, we trained the target platform in a virtual environ-
ment but found that the thrust-to-weight ratio was insufﬁcient to
support such high-difﬁculty maneuvers. To address this issue,
we increased the thrust-to-weight ratio to 2.5 in the simulation,
and the results are shown in Fig. 7(d1)–7(d4). Simultaneously,
we directly transferred the same network to the real environ-
ment, and the results are depicted in Fig. 7(e1)–7(e4). The com-
plete states, trajectories of the MAV, and its corresponding
commands are presented in Fig. 8(b). Remarkably, despite the
thrust-to-weight ratio limitation in reality, the MAV was able to
leverage the elastic properties of its frame to assist in completing
the maneuver, albeit with larger positional errors. This unex-
pected behavior, which was not explicitly trained for in the sim-
ulation, highlights the robustness of the RL-based controller.
VI.
CONCLUSION
This article presents a purely RL-based controller designed
for a planar MAV to execute ﬂip maneuvers. We validated the
controller’s performance by successfully demonstrating ﬂip and
wall-backtrack maneuvers in both simulated and real-world
environments. This research extends the RL algorithm’s capa-
bilities from simulation to practical application, providing agile
and maneuverable MAVs capable of captivating aerial displays.
Future work will explore the algorithm’s performance in a 3-D
environment without plane support platform.
ACKNOWLEDGMENT
The authors thank Zhao Ma, Peidong Huo, and Weicong
Zhang for helping with the real-world experiments and valuable
technical suggestions.
REFERENCES
[1] L. Antonio, K. Elia, R. Rene, M. Matthias, K. Vladlen, and S. Davide,
“Learning high-speed ﬂight in the wild,” Sci. Robot., vol. 6, no. 59,
2021, Art. no. eabg5810.
[2] W. Xie, D. Cabecinhas, R. Cunha, and C. Silvestre, “Adaptive
backstepping control of a quadcopter with uncertain vehicle mass,
moment of inertia, and disturbances,” IEEE Trans. Ind. Electron., vol.
69, no. 1, pp. 549–559, 2021.
[3] Q. Sun, J. Fang, W. X. Zheng, and Y. Tang, “Aggressive quadrotor
ﬂight using curiosity-driven reinforcement learning,” IEEE Trans. Ind.
Electron., vol. 69, no. 12, pp. 13838–13848, Dec. 2022.
Fig. 8.
Time evolution of the VPP MAV’s position, velocity, and rotation in simulation and the real world using the trained neural network. (a) and (b)
Shows the ﬂight data for the planar variable-pitch MAV perform wall-backtrack and 360-degree ﬂip, respectively. The reference trajectory is shown with
purple dot lines, while the red dashed lines indicate the moments when the pilot switches the maneuver trigger.
WANG AND ZHAO: SIM-TO-REAL TRANSFER IN RL FOR MANEUVER CONTROL
10453
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:32:50 UTC from IEEE Xplore.  Restrictions apply.

## Page 10

[4] J. Delmerico et al., “The current state and future outlook of rescue
robotics,” J. Field Rob., vol. 36, no. 7, pp. 1171–1191, 2019.
[5] A.
Petrovski
and
M.
Radovanovic,
“Application
of
detection
reconnaissance technologies use by drones in collaboration with c4irs
for military interested,” Contemporary Macedonian Defence, vol. 21,
no. 40, 2021, Art. no. 117.
[6] S. M. S. M. Daud et al., “Applications of drone in disaster management:
A scoping review,” Sci. Justice, vol. 62, no. 1, pp. 30–42, 2022.
[7] X. Zhou et al., “Swarm of micro ﬂying robots in the wild,” Sci. Robot.,
vol. 7, no. 66, 2022, Art. no. eabm5954.
[8] Y. Song, A. Romero, M. Muller, V. Koltun, and D. Scaramuzza,
“Reaching the limit in autonomous racing: Optimal control versus
reinforcement learning,” Sci. Robot., vol. 8, no. 82, 2023, Art. no.
eadg1462.
[9] A. Loquercio, E. Kaufmann, R. Ranftl, A. Dosovitskiy, V. Koltun, and
D. Scaramuzza, “Deep drone racing: From simulation to reality with
domain randomization,” IEEE Trans. Robot., vol. 36, no. 1, pp. 1–14,
Jan. 2020.
[10] G. Yang et al., “The grand challenges of science robotics,” Sci. Robot.,
vol. 3, no. 14, 2018, Art. no. eaar7650.
[11] B. Michini, J. Redding, N. K. Ure, M. Cutler, and J. P. How, “Design
and ﬂight testing of an autonomous variable-pitch quadrotor,” in Proc.
IEEE Int. Conf. Robot. Autom. (ICRA). Piscataway, NJ, USA: IEEE
Press, 2011, pp. 2978–2979.
[12] T. Pang, K. Peng, F. Lin, and B. M. Chen, “Towards long-endurance
ﬂight: Design and implementation of a variable-pitch gasoline-engine
quadrotor,” in Proc. 12th IEEE Int. Conf. Control Automat. (ICCA).
Piscataway, NJ, USA: IEEE Press, 2016, pp. 767–772.
[13] M. Cutler and J. P. How, “Analysis and control of a variable-pitch
quadrotor for agile ﬂight,” J. Dyn. Syst. Meas. Contr., vol. 137, no. 10,
pp. 101002–101016, Oct. 2015.
[14] M. Cutler and J. How, “Actuator constrained trajectory generation and
control for variable-pitch quadrotors,” in Proc. AIAA Guid. Navigat.
Control Conf., 2012, pp. 4777–4792.
[15] S.
Zhao,
Mathematical
Foundations
of
Reinforcement
Learning.
New York: Springer Press, 2025.
[16] J. Lin, L. Wang, F. Gao, S. Shen, and F. Zhang, “Flying through a
narrow gap using neural network: An end-to-end planning and control
approach,” in Proc. IEEE/RSJ Int. Conf. Intell. Robots Syst. (IROS).
Piscataway, NJ, USA: IEEE Press, 2019, pp. 3526–3533.
[17] R. S. Sutton and A. G. Barto, Reinforcement Learning: An Introduction.
Cambridge, MA, USA: MIT Press, 2018.
[18] O. Vinyals et al., “Grandmaster level in StarCraft II using multi-agent
reinforcement learning,” Nature, vol. 575, no. 7782, pp. 350–354, 2019.
[19] I. Masmitja et al., “Dynamic robotic tracking of underwater targets
using reinforcement learning,” Sci. Robot., vol. 8, no. 80, 2023, Art. no.
eade7811.
[20] J. Xu et al., “Learning to ﬂy: Computational controller design for hybrid
UAVS with reinforcement learning,” ACM Trans. Graph. (TOG),
vol. 38, no. 4, pp. 1–12, 2019.
[21] J. Hwangbo et al., “Learning agile and dynamic motor skills for legged
robots,” Sci. Robot., vol. 4, no. 26, 2019, Art. no. eaau5872.
[22] J. Panerati, Z. Hehui, Z. Siqi, X. James, P. Amanda, and A. P.
Schoellig, “Learning to ﬂy a gym environment with pybullet physics for
reinforcement learning of multi-agent quadcopter control,” in Proc.
IEEE/RSJ Int. Conf. Intell. Robots Syst. (IROS), 2021, pp. 7512–7519.
[23] G. Wu and K. Sreenath, “Safety-critical control of a planar quadrotor,”
in Proc. Am. Control Conf. (ACC). Piscataway, NJ, USA: IEEE Press,
2016, pp. 2252–2258.
[24] Y. Zhou, C. Barnes, J. Lu, J. Yang, and H. Li, “On the continuity of
rotation representations in neural networks,” in Proc. Conf. Comput.
Vision Pattern Recognit. (CVPR), 2019, pp. 5745–5753.
Zhikun Wang received the B.S. degree in auto-
mation engineering from Beijing Forestry Univer-
sity of Automation, China, in 2016, and the M.S.
and Ph.D. degrees in automatic control and sys-
tems engineering from the University of Shef-
ﬁeld, U.K., in 2018 and 2022, respectively.
He was a Postdoctoral Researcher with the
Intelligent
Unmanned
Systems
Laboratory,
School
of
Engineering,
Westlake
University,
Hangzhou, China. Currently, he is an Associate
Researcher with the Department of Artificial
Intelligence, Westlake University. His research interests include reinforce-
ment learning, MAV control, and robotics.
Shiyu
Zhao
received
the
B.E.
and
M.E.
degrees in automation engineering from Beijing
University of Aeronautics and Astronautics, Bei-
jing, China, in 2006 and 2009, respectively, and
the Ph.D. degree in electrical and computer
engineering from the National University of Sin-
gapore, Singapore, in 2014.
Currently, he is an Associate Professor with
the School of Engineering and the Director of
the Intelligent Unmanned Systems Laboratory,
Westlake University, Hangzhou, China. Before
he joined Westlake University, he was a Lecturer with the Department of
Automatic Control and Systems Engineering, University of Sheffield,
U.K. His research interests include sensing, estimation, and control of
multirobot systems.
10454
IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS, VOL. 72, NO. 10, OCTOBER 2025
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:32:50 UTC from IEEE Xplore.  Restrictions apply.
