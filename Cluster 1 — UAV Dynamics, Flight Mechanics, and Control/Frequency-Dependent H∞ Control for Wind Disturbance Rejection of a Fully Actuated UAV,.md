# Frequency-Dependent H∞ Control for Wind Disturbance Rejection of a Fully Actuated UAV,.pdf

## Page 1

Robotica (2024), 1–15
doi:10.1017/S0263574724000523
RESEARCH ARTICLE
Frequency-dependent H∞control for wind disturbance
rejection of a fully actuated UAV
Jérémie X. J. Bannwarth, Shahab Kazemi
and Karl Stol
Department of Mechanical and Mechatronics Engineering, University of Auckland, Auckland, New Zealand
Corresponding author: Shahab Kazemi; Email: shahab.kazemi@auckland.ac.nz
Received: 5 October 2023; Accepted: 25 March 2024
Keywords: Multirotor UAV; disturbance rejection; H∞control
Abstract
In this paper, an H∞dynamic output feedback controller is experimentally implemented for the position regulation of
a fully actuated tilted-rotor octocopter unmanned aerial vehicle (UAV) to improve wind disturbance rejection during
station-keeping. To apply the lateral forces, besides the standard tilt-to-translate (attitude-thrust) movement, tilted-
rotor UAVs can generate vectored (horizontal) thrust. Vectored-thrust is high-bandwidth but saturation-constrained,
while attitude-thrust generates larger forces with lower bandwidth. For the ﬁrst time, this paper emphasizes the
frequency-dependent allocation of weighting matrices in H∞control design based on the physical capabilities of the
fully actuated UAV (vectored-thrust and attitude-thrust). A dynamic model of the tilted-rotor octocopter, including
aerodynamic eﬀects and rotor dynamics, is presented to design the controller. The proposed H∞controller solves
the frequency-dependent actuator allocation problem by augmenting the dynamic model with weighting transfer
functions. This novel frequency-dependent allocation utilizes the attitude-thrust for low-frequency disturbances and
vectored-thrust for high-frequency disturbances, which exploits the maximum potential of the fully actuated UAV.
Several wind tunnel experiments are conducted to validate the model and wind disturbance rejection performance,
and the results are compared to the baseline PX4 Autopilot controller on both the tilted-rotor and a planar octocopter.
The H∞controller is shown to reduce station-keeping error by up to 50% for an actuator usage 25% higher in
free-ﬂight tests.
1. Introduction
Performing outdoors is one of the most essential multirotor unmanned aerial vehicle (UAV) applica-
tions [1, 2]. However, wind disturbances can adversely aﬀect the performance of UAVs and destabilize
them. Many studies have focused on active disturbance rejection with automatic control in multirotor
UAVs [3, 4]. H∞control is a well-known method for its high disturbance rejection and stability robust-
ness, which has been widely used to address diﬀerent UAV problems [5–7]. The combination of model
predictive control and H∞was designed for the wind disturbance rejection of quadrotors in simulation
[8, 9]. In another simulation study, Massé et al. [10] incorporated a thorough aerodynamics model in their
plant model and compared the control performances of linear quadratic regulation (LQR) and structured
H∞synthesis. Structured H∞design was shown to provide a more reliable framework in wind distur-
bance rejection compared to LQR. In an experimental study, Dai et al., presented acceleration feedback
(AF) enhanced H∞control to deal with the wind disturbance on an underactuated hexacopter [11]. The
experimental results suggested the superiority of AF-enhanced H∞over H∞control in eﬀectiveness and
robustness against wind disturbance.
Disturbance rejection through control is inherently limited by the bandwidth of the actuators. Planar
UAVs (with all the rotors parallel) are underactuated which further limits the bandwidth of the actuation
along translational axes [12]. Planar UAVs must change their attitude to produce lateral thrust, which
is not desirable during station-keeping (attitude-thrust). Meanwhile, vectored-thrust (horizontal thrust)
C⃝The Author(s), 2024. Published by Cambridge University Press. This is an Open Access article, distributed under the terms of the Creative
Commons Attribution licence (http://creativecommons.org/licenses/by/4.0/), which permits unrestricted re-use, distribution and reproduction,
provided the original article is properly cited.
https://doi.org/10.1017/S0263574724000523 Published online by Cambridge University Press

## Page 2

2
Jérémie X. J. Bannwarth et al.
UAVs, as fully actuated systems, can produce thrust in the body xy-plane without generating moments
(as opposed to planar rotors). One way to achieve vectored-thrust is to attach one or more rotors on
servomotors to actively adjust their tilt angle [13–16]. This technique increases the number of moving
parts and thus decreases reliability. Also, the servomotor bandwidth is a limiting factor, particularly
under the inﬂuence of large gyroscopic moments.
Another way to design fully actuator UAV is to have (omnidirectional) ﬁxed rotors by arranging
them at extreme angles against each other [17, 18]. The downsides of this method are an increase in
mass and reduction in hover eﬃciency. Finally, UAVs with passively tilted rotors [19–26] can be used to
achieve vectored-thrust. Their rotors are tilted around diﬀering axes, increasing the controllable degrees
of freedom of the system. In this study, a passive tilted-rotor octocopter is presented to simplify the con-
trol problem through a speciﬁc rotor tilt pattern and reduce the coupling between thrust generation and
attitude control. Current vectored-thrust UAV literature is split between actuator allocation (convert-
ing virtual control signals, such as desired body torques and thrusts, to physical actuator commands)
and control design. While some studies concentrated on designing actuator allocation schemes [13, 22],
some other researchers considered wind disturbance rejection as a control goal and designed a controller
accordingly. Many controllers such as adaptive [19], robust chattering-free [21], and integral SMC [24]
were designed and simulated for vectored-thrust UAV disturbance rejection, while none of them were
implemented experimentally.
This paper introduces a novel H∞synthesis tailored for fully actuated UAVs (tilted-rotor octocopter),
aiming to enhance wind disturbance rejection. H∞synthesis is used due to its ability to weigh com-
peting control goals in the frequency domain. Traditionally, the determination of weighting matrices
relied on experimental data [5]. However, this work proposes an experimental implementation of a
novel frequency-dependent weighting function allocation, building on the vectored-thrust capability of
the fully actuated UAV. Notably, this work incorporates the physical capabilities of the fully actuated
UAV into the frequency-dependent allocation. The new controller optimally assigns weights, utilizing
attitude-thrust for low-frequency disturbances and vectored-thrust for high-frequency disturbances. This
frequency-dependent actuator allocation is desirable because the maximum horizontal thrust that can
be produced by changing the attitude of the UAV is signiﬁcantly larger than what is achievable using
the vectored-thrust. This recognition is critical, as vectored-thrust is more prone to actuator saturation
and better suited for smaller amplitude, higher-frequency commands. By harnessing the UAV’s ability
to generate vectored-thrust, the controller achieves a targeted response to wind disturbances with diﬀer-
ent frequencies. This allows the total capacity of the fully actuated UAV in wind disturbance rejection
while keeping an acceptable performance. In other words, this frequency-dependent weighting is applied
to use attitude control to reject low-frequency disturbances and use vectored-thrust for high-frequency
disturbances. The rest of the paper is organized as follows.
Initially, the tilted-rotor octocopter setup is introduced, and its coordinate frame and physical char-
acteristics are presented. A comprehensive model including the eﬀects of wind disturbances and rotor
dynamics is proposed in Section 3. Section 4 describes the design of the proposed H∞controller. The
ﬂight performance is experimentally examined in a wind tunnel in Section 5. Finally, conclusions are
drawn in Section 6.
2. The physical setup and coordinate frame
The presented tilted-rotor octocopter is designed and built based on a parameter sweep process to
maximize agility for a given endurance and payload [25, 26] (see Fig. 1). The bandwidth from the
vectored-thrust design is ten times higher than a comparable tilt-to-translate design. The maximum
produced vectored-thrust is 24% of its weight. With reference to Fig. 1b, producing a net force along
the x-axis is achieved by increasing the thrust of rotors 3 and 6, while decreasing the thrust of rotors
2 and 7. The moment generated by this operation can then be canceled by increasing the thrust of
rotors 1 and 8 and decreasing that of rotors 5 and 4. Table 1 lists the parameters of the selected design.
Vectors expressed by W, B, and Mi are expressed in the world, body, and ith-motor frame, respectively.
https://doi.org/10.1017/S0263574724000523 Published online by Cambridge University Press

## Page 3

Robotica
3
Figure 1. (a) Photo of the tilted-rotor octocopter that is used in this work. (b) The front and back rotors
(1, 4, 5, 8) are tilted about the body x-axis, while the left and right rotors (2, 3, 6, 7) are tilted around
the body y-axis. The rotors of the UAV are equally distributed around the center of mass.
The world frame and body frame use the typical north-east-down and front-right-down conventions,
respectively. The rotors are tilted at an angle ζ.
3. Dynamics
Wind introduces uncertainties in the aerodynamic forces acting on the UAV. Modeling these forces
accurately is challenging due to the dynamic and unpredictable nature of wind. However, a compre-
hensive dynamic model is needed to design the model-based controller. The position of the UAV in
the world frame is deﬁned as ξ = [ x
y
z]T, and its attitude is deﬁned by the Hamilton quaternion
q = [ q0
q1
q2
q3 ]T = [ q0
qT
1: 3 ]T [27]. The absolute angular velocity of the craft expressed in the
body frame is deﬁned as Bν = [ Bp
Bq
Br]T. Using Newton–Euler formulas, the acceleration of the
UAV is obtained as
¨ξ = 1
mt

G + W
B R
BT + BFaero

,
(1)
where WG = [ 0
0
9.81mt ]T is the weight vector, BT is the total rotor thrust, W
B R is the rotation matrix
from the body frame to world frame, and BFaero represents the aerodynamic force acting on the frame.
Likewise, the angular acceleration of the UAV is
B ˙ν = I−1
B
Bτ −Bν ×

IB
Bν

+ BMaero

,
(2)
where IB = diag(Ixx, Iyy, Izz) represents the mass moment of inertia of the frame, Bτ is the total rotor
torque, and BMaero is the aerodynamic moment acting on the frame. The frame aerodynamic forces and
moments are deﬁned as
https://doi.org/10.1017/S0263574724000523 Published online by Cambridge University Press

## Page 4

4
Jérémie X. J. Bannwarth et al.
Table 1. Parameters of tilted-rotor octocopter.
Parameter
Description
Unit
Value
N
Number of rotors
–
8
DUAV
Rotor-to-rotor diameter
m
0.500
Dprop
Propeller diameter
m
0.1524
ζ
Rotor tilt angle
degree
31
mt
Total UAV mass
kg
1.7
Ixx, Iyy
x -/y axis MMoI
kg m2
0.0240
Izz
z-axis MMoI
kg m2
0.1051
IR,zz
Motor z-axis MMoI
kg m2
3.290 × 10−6
cτ
Rotor drag coeﬃcient
N m s2/rad2
1.041 × 10−8
KE
Motor back-EMF constant
V s/rad
0.004126
I0
Motor no-load current
A
0.6
R
Motor resistance

0.117
BFaero = −1
2ρairAUAVU2
app,f
Cx,f

αf

cosβf
Cx,f

αf

sinβf
Cz,f

αf
T
BMaero = 1
2ρairAUAVDUAVCM,f

αf

U2
app,f
−sinβf
cosβf
0 T ,
(3)
where αf and βf are the inﬂow angle and sideslip angle of the apparent wind vector (Fig. 2a), AUAV =
πD2
UAV
4
is the area of the UAV, and Cx,f(αf), Cz,f(αf), and CM,f(αf) are dimensionless aerodynamic coeﬃcients
deﬁned in ref. [28]. In the body frame, the apparent wind vector is expressed as BUapp,f = −B
WR(˙ξ + WU),
where WU = −[ Ux
Uy
Uz ]T is the wind velocity vector.
The total force BT = N
i=1
BTi, and torque Bτ = N
i=1 (Bτ i −Bν(Mi
BRMiIR
Miωi)), are generated
by all the rotors, where Miωi = [ 0
0
ωi ]T represents the angular speed of the ith-rotor, and MiIR =
diag(0, 0, IR,zz) is the combined mass moment of inertia of the motor and rotor. The forces and torques
acting on a single rotor are
BTi = Mi
BR
Ti,xycosβi
Ti,xysinβi
Ti,z
T ,
Bτ i = Mi
BR
⎡
⎢⎣
Mi,xysinβi
Mi,xycosβi
(−1)i+1 
bω2
i + IR,zz ˙ωi

⎤
⎥⎦+ BLi×BTi,
(4)
where βi and αi represent the sideslip angle and inﬂow angle of the wind on the ith-rotor (see Fig. 2b).
The (−1)i+1 term accounts for the rotor direction. The aerodynamic forces and moments acting on each
rotor are deﬁned as
Ti,xy = −1
2ρairApropDpropCx,i (αi, λi) ωiUapp,i
Ti,z = −1
2ρairApropDprop

DpropCz,1,iω2
i + Cz,2,i (αi) ωiUapp,i

,
Mi,xy = −1
2ρairApropD2
propCM,i (αi, λi) ωiUapp,i,
(5)
where Aprop =
πD2prop
4
is the area covered by the propeller. Cx,i(αi, λi), Cz,1,i, Cz,2,i(αi), and CM,i(αi, λi) are
dimensionless aerodynamic coeﬃcients deﬁned in ref. [6]. Due to the oﬀset between the rotors and the
center of mass of the UAV, the apparent wind velocity at each rotor is aﬀected by the rotational speed
of the UAV and is given by
https://doi.org/10.1017/S0263574724000523 Published online by Cambridge University Press

## Page 5

Robotica
5
Figure 2. Aerodynamic forces and moments acting on octocopter frame and the ith-rotor. (a) Side view
of the frame when the sideslip angle βf = 0. (b) Side view of the rotor when the sideslip angle βi = 0.
MiUapp,i = BMiR
BUapp,f + Bν × BLi

,
(6)
where BLi represents a position vector from the center of the UAV to the ith-rotor and is deﬁned as
BLi = 1
2DUAV
cosγi
sinγi
0T .
(7)
Note that in Eq. (7), γi = 45i −22.5◦is the angle from the positive body x-axis to the arm holding
rotor i and is measured positive counterclockwise around the body z-axis (see Fig. 1b). The angular
acceleration of the ith-rotor is given by
˙ωi = 1
IR,zz
KT
R (Vi −I0R −KEωi) −cτω2
i

,
(8)
where I0 is the motor idle current and R is the motor resistance [25]. KE is the back-EMF constant,
KT = KE is the motor torque constant, and cτ is the rotor torque aerodynamic constant. Finally, Vi is the
input voltage to the motor. The PWM to motor voltage mapping for the motors is obtained by mounting
a single motor on a RCBenchmark Series 1580 Thrust Stand. The relationship between the normalized
PWM signal sent to a motor (χi ∈[0, 1]), and the input voltage is Vi = 6.982χi + 2.351.
4. Control architecture
To conduct the wind disturbance rejection while hovering at a ﬁxed location, a cascaded closed-loop
controller is designed and implemented for the presented tilted-rotor octocopter. For the implementation
board and software, a Pixhawk Cube board running the PX4 Autopilot Firmware is employed. Note that
https://doi.org/10.1017/S0263574724000523 Published online by Cambridge University Press

## Page 6

6
Jérémie X. J. Bannwarth et al.
Figure 3. The control implementation architecture.
the cascaded structure used in this work is mostly identical to that of the position hold control mode of
the baseline (BL) PX4 Autopilot version 1.8.2 [29].
The BL closed-loop control architecture is split into inner and outer loops. The inner loop controls
the desired UAV attitude (orientation) and comprises of a globally stable nonlinear quaternion-based
angular controller [30], and PID control for angular rate. Meanwhile, for the outer loop, the position
controller consists of a proportional gain acting on the position error and a PID velocity controller for
each axis. In this work, for the outer loop, a novel H∞dynamic output feedback controller is designed
to improve the wind disturbance rejection performance.
Fig. 3 illustrates the closed-loop cascaded architecture. As only performance in front-facing wind is
investigated, the desired yaw angle ψdes = 0◦for the remainder of this work. The output of the H∞block
is converted to a desired attitude, qdes, and the normalized thrust BTdes = [ BTdes,x
BTdes,y
BTdes,z ]T.
The attitude controller outputs desired normalized roll, pitch, and yaw torques, in the form of BCη =
[ Cφ
Cθ
Cψ ]T.
The actuator allocation is performed by the motor mixer. Note that the motor mixer accepts the desired
thrust, BTdes, and torque commands, BCη, in the body frame, whereas the position controller operates in
the world frame. To deal with this, two virtual acceleration signals in the world frame are introduced; the
virtual attitude-thrust acceleration aA,des ∈R3 and the virtual vectored-thrust (horizontal) acceleration
aH,des ∈R3. Initially, aH,des is rotated to the body frame, yielding
BaH,des = WBRaH,des =
 BTdes,x
BTdes,y
BaH,des,z
T .
(9)
The ﬁrst two elements in the x and y-axis can be produced by the tilted rotors. Yet, BaH,des,z is an
unintended side eﬀect of the vectored-thrust scheme when the UAV is not level and must be compensated
using attitude control. This element is isolated, rotated back to the world frame, and added to the desired
attitude acceleration. Consequently, the total attitude acceleration ades is deﬁned as
ades = aA,des + W
B R
⎡
⎢⎣
0
0
BaH,des,z
⎤
⎥⎦.
(10)
The PX4 Autopilot thrust-to-quaternion algorithm converts the total attitude acceleration setpoint to
the desired quaternion, qdes, and vertical thrust, BTdes,z, that can be fed to the motor mixer (see Fig. 3). The
desired vertical thrust is simply the magnitude of the desired attitude acceleration, BTdes,z = −∥ades∥2.
In the next step, the motor mixer maps the desired thrust,BTdes, and the torque command, BCη, into
a vector of PWM signals (χ) to be sent to the motors (see Fig. 3). Details of how the motor mixer is
constructed can be found in ref. [26]. The motor mixer is designed to accept vectored-thrust commands.
The motor mixer depends on the angle between the rotor arms, γ = 45◦, and the tilt angle of the rotors,
ζ, such that
https://doi.org/10.1017/S0263574724000523 Published online by Cambridge University Press

## Page 7

Robotica
7
Figure 4. H∞closed-loop control schematic with weighting matrices.
χ =
⎡
⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎣
−Sγ/2
Cγ/2
1
a
−b
1
−Cγ/2
Sγ/2
−1
−b
a
1
−Cγ/2
−Sγ/2
1
b
a
1
−Sγ/2
−Cγ/2
−1
−a
−b
1
Sγ/2
−Cγ/2
1
−a
b
1
Cγ/2
−Sγ/2
−1
b
−a
1
Cγ/2
Sγ/2
1
−b
−a
1
Sγ/2
Cγ/2
−1
a
b
1
⎤
⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎦

BCη
BTdes

,
(11)
where Sγ/2 = sin (γ/2), Cγ/2 = cos (γ/2), a = 2 tan(γ/2)
tan (ζ) , and b =
2
tan ζ. For comparison, the elements of
the fourth and ﬁfth column of the motor mixer matrix in Eq. (11) are zero in the BL PX4 motor mixer
matrix.
4.1. Linearized plant
Synthesizing the H∞controller requires a linearized model of the plant. The attitude is expressed as
η = [ φ
θ
ψ ]T, where φ, θ, and ψ are the roll, pitch, and yaw angles of the octocopter, respectively.
The motor mixer and attitude controller are included in the plant model. The input vector of the plant is
deﬁned as u = [ aT
A,des
aT
H,des ]T, and the wind velocity (wd = WU) is the disturbance input (see Fig. 4).
The state vector is x = [ ξ T
˙ξ
T
ηT
BνT
ωT
xT
PID ]T (27 states), where ω = [ ω1
ω2
· · ·
ω8 ]T is
the rotors’ angular speed vector and xPID is a vector containing the internal states of the angular rate loop.
The pitch and roll rate controllers use PID controllers with a second-order derivative ﬁlter (three states
each). The yaw rate controller uses a PI controller and only has one state. The attitude controller already
stabilizes the internal attitude and angular velocity states. Therefore, the output vector only contains the
integral of position, position, and velocity of the UAV, y = [ 
ξ T
ξ T
˙ξ
T ]T.
The system is trimmed for the wind velocity U* = [ 5.6
0
0 ]T m/s. This velocity corresponds to
approximately 50% of the feasible velocity range of the boundary layer wind tunnel used. In the trimming
algorithm, position and rate states are constrained to zero. Also, the vectored-thrust is not used at steady
state, which simpliﬁes the trimmed input to u* = [ a*T
A,des
0 ]T. As expected, the trimmed pitch angle,
θ * = −8.25◦, is negative, corresponding to the UAV pitching into the wind to counteract its drag force.
The model is then linearized around the calculated operating point (resulting from the trim process)
using MATLAB’s linearize function. The linearized model now needs to be augmented by weighing
matrices before controller synthesis.
The disturbance rejection, regulation performance, and actuator usage are competing and need to
be weighted. Therefore, the linearized model also needs to be augmented by weighting matrices. The
linearized plant and H∞controller dynamics to be designed are denoted as the transfer function matrices
G(s) and K(s), respectively. Wu(s), Wd(s), Wo(s), and Ws(s) represent the actuator, wind disturbance,
https://doi.org/10.1017/S0263574724000523 Published online by Cambridge University Press

## Page 8

8
Jérémie X. J. Bannwarth et al.
Figure 5. Fitting ﬁrst-order transfer function to x-axis wind spectrum.
output, and sensor noise weighting matrices, respectively (see Fig. 4). The regulated output vector, z =
[ zT
out
zact
T ]T, and the disturbance input vector, w = [ wT
sens
wd
T ]T, are deﬁned. The actuator weighting
matrix is deﬁned as Wu(s) = diag(Wu,A(s), Wu,A(s), Wu,A(s), Wu,H(s), Wu,H(s)), where
Wu,A (s) = 50.1 s + ωco
s + 10ωco
, Wu,H (s) = 8.91 s + ωco
s + 0.1ωco
,
(12)
where ωco is the desired cross-over frequency (the frequency at which the vectored-thrust should take
over from the attitude control). The controller should use the attitude controller for low-frequency
disturbances and vectored-thrust for high-frequency disturbances. This frequency-dependent actuator
allocation is desirable because the maximum attitude-thrust of the UAV is signiﬁcantly larger than
vectored-thrust. Consequently, vectored-thrust is more likely to saturate the actuators and is better suited
to smaller amplitude, higher-frequency commands. The ﬁrst three diagonal elements of Wu(s) corre-
spond to the desired virtual attitude-thrust, and the last two correspond to the desired vectored-thrust.
The virtual attitude-thrust is penalized at high frequencies, while vectored-thrust is penalized at low fre-
quencies. The locations of zeros and poles are chosen based on a desired cross-over frequency, ωco = π
rad/s. This frequency is chosen to be below the cutoﬀfrequencies of aA,des,x and aA,des,y, which are 8 rad/s.
The DC gains of the attitude and vectored-thrust transfer functions are chosen to be 14 dB and 19 dB,
respectively, by the trial-and-error process to prevent actuator saturation.
The wind disturbance weighting matrix, Wd, can be deemed as a function that shapes white noise into
the expected spectrum of the wind. Fig. 5 shows the x-axis wind spectrum of the wind tunnel and a ﬁrst-
order transfer function ﬁtted to it. The high-frequency roll-oﬀof the spectrum is -28.5 dB/dec, which
cannot be replicated using a transfer function. An asymptotic approximation is used to ﬁnd the corner
frequency of the spectrum (24.1 rad/s). Wd is given the same corner frequency, but its magnitude is set
to 15 dB through trial-and-error to improve disturbance rejection while preventing actuator saturation,
yielding
Wd (s) = 5.62
24.1
s + 24.1I,I ∈R3×3,
(13)
where I is the identity matrix. The output and sensor noise weighting matrices are arbitrarily
chosen as
Wo = 1
2I, Ws = 1
20I, I ∈R9×9.
(14)
Finally, the Laplace domain weighing matrices and linearized plant model are combined.
4.2. H∞output feedback position controller
In the previous section, after trimming the plant, ﬁnding the operating point, and linearizing the plant
around the operating point, the model was augmented with weighting matrices. According to Fig. 4, the
https://doi.org/10.1017/S0263574724000523 Published online by Cambridge University Press

## Page 9

Robotica
9
state space dynamics of the controller, K(s) = (AK, BK, CK, DK), are
˙xK = AKxK + BKy,
u = CKxK + DKy,
(15)
where xK is the internal state vector of the controller, and AK, BK, CK, and DK are constant matrices.
This controller is an output feedback controller because it acts on the measured output, y, rather than on
the system state, x, that is described in Section 4.1.
H∞techniques often use a high number of states, which can be undesirable and computationally
expensive for real-time applications. Typical H∞synthesis algorithms, such as MATLAB’s inbuilt hin-
fsyn, create full-order controllers with the same number of states as the plant. The octocopter plant in
this work will result in a 38th-order controller. Combined with the controller’s nine inputs and ﬁve out-
puts, a discrete implementation will require more than two thousand multiplication operations at each
time step. This complexity causes a substantial computational burden for the onboard ﬂight controller,
Pixhawk Cube. The open-source HIFOO 2.0 toolbox (MATLAB) [31] solves this issue by allowing for
the creation of reduced order controllers using an optimization-based algorithm. Therefore, HIFOO 2.0
synthesizes the controller from the linearized model described in Section 4.1. The reduced order con-
troller (order of 1) is created to keep the performance like the full-order controller while signiﬁcantly
reducing the computation cost. Note that implementing the resulting controller on the original system
requires accounting for the trimmed input, u* (see Section 4.1).
AK = −11.0,
(16)
CK =
−2.82
2.55
−0.956
5.99
0.0202 T ,
BK = [ 0.847
−2.39
. . .
−0.239
−0.0859 ]1×9,
DK =
⎡
⎢⎢⎣
−0.0616
· · ·
−0.0147
...
...
...
0.0155
· · ·
0.0111
⎤
⎥⎥⎦
5×9
.
For the attitude control part, by choosing the Lyapunov candidate function as V(z, q) = qT
1: 3q1: 3 +
(q0 −1)2, where z ∈{ z1
z2 } corresponds to the upper and lower hemisphere of the space of unit quater-
nions, we can show that V(z, q) > 0 and ˙V(z, q) < 0 (see detailed proof of stability in ref. [28]). This
shows that the attitude controller stabilizes the internal attitude and angular velocity states. For the ana-
lytical proof of stability of the position control part, since Wu(s), Wd(s), Wo(s), and Ws(s) are positive
deﬁnite, we can use the standard linear matrix inequality positive deﬁnite solution (See Appendix B
of [11] for the detailed proof of stability). Meanwhile, from Eq. (16) for the newly designed position
controller, the controller has a single pole at -11 rad/s. Fig. 6 shows the pole-zero map of the closed-loop
system, including the linearized model and the controller. It can be seen that all poles are in the open
left halfplane, proving the stability of the linear closed-loop position control system. Note that the other
poles to the far left have been removed to improve visibility.
Fig. 7 shows the Bode magnitude plot of the transfer function from the wind disturbance input,
Ux(s), to the attitude and vectored-thrust accelerations. The magnitude responses of these transfer func-
tions indicate which actuator is used to compensate for wind disturbances. The magnitude response of
vectored-thrust control is lower than that of attitude control at all frequencies due to the higher DC gain of
the weighting function used. Nevertheless, the relative magnitudes of the transfer functions are not con-
stant; at low frequencies, the attitude control response is 25 dB higher than the vectored-thrust response,
whereas the diﬀerence narrows down to 10.1 dB as ω →∞. These magnitude responses demonstrate
the desired frequency-dependent actuator allocation as the vectored-thrust is not used at low frequen-
cies to prevent saturation and is used increasingly at higher frequencies to improve disturbance rejection.
https://doi.org/10.1017/S0263574724000523 Published online by Cambridge University Press

## Page 10

10
Jérémie X. J. Bannwarth et al.
Figure 6. Upper half of the pole-zero map close to the imaginary axis for the linearized plant and
closed-loop system.
Figure 7. Magnitude response of the transfer functions from the wind disturbance to the desired
accelerations.
The peaks of both responses are at 2.5 rad/s, which is close to the cross-over frequency of the actuator
weighting functions at π rad/s.
5. Free-ﬂight experiments
5.1. Free-ﬂight station-keeping performance
UAVs encounter a range of disturbances beyond wind, including atmospheric factors like turbulence and
thermal updrafts, environmental elements, obstacles in the ﬂight path, potential sensor inaccuracies and
noise, communication disruptions, electromagnetic interference, and the risk of system faults. Physical
interaction is also another considerable source of disturbance, in which the UAV is interacting through
a tool with the surrounding environment. In this paper, however, we assumed all other factors negligible
compared to the wind and turbulence disturbances. Also, the UAV is not in contact with its surroundings
(free ﬂight).
To validate the performance of the H∞controller for wind disturbance rejection, and conducting a
comparison, a comprehensive experiment is designed. Three cases are considered: the tilted-rotor octo-
copter with the H∞controller, the tilted-rotor octocopter with the BL controller, and a planar version of
the octocopter with the BL controller. The UAV is ﬂown inside the wind tunnel in a test section outﬁtted
with motion capture cameras to provide position feedback (see Fig. 8a). A disturbance-generating grid
is mounted ahead of the ﬂight location to generate turbulence intensities of approximately 10%.
Note that the octocopter is powered by two 40A power supplies through an approximately 3 m long
tether, as shown in Fig. 8a. The power supplies are set to 13V to account for a measured 2V drop
across the tether. This tethered solution is chosen over traditional batteries as it allows faster testing
https://doi.org/10.1017/S0263574724000523 Published online by Cambridge University Press

## Page 11

Robotica
11
Figure 8. Wind disturbance rejection experiment. (a) Octocopter station-keeping in the boundary
layer wind tunnel, University of Auckland. (b) RMS error of the position norm. (c) RMS rotation error.
(d) Mean RMS of the motor PWM signals.
by removing the need to swap and charge batteries. Furthermore, the constant power supply voltage
provides consistency between and during tests.
Three wind speeds of Umean = {0, 5.6, 12.8} m/s are investigated. Each ﬂight starts with the UAV
sitting on the ﬂoor, midway between the wind tunnel walls and 3.8 m away from the turbulence grid.
The operator then switches the UAV to position hold mode to track a position setpoint at the center of
the wind tunnel. The second phase of the experiment involves setting the wind tunnel to the desired
speed setting and waiting for the transients to decay before recording the response of the UAV. Each
ﬂight yields 100 s of usable data after removing all transient behaviors.
Through 72 experimental tests, it was demonstrated that despite increasing the mean wind speed
from 5.6 m/s to 12.8 m/s and also adding 10% turbulence intensity, the hovering RMS position error
norm remained smaller than 5 cm (Fig. 8b). RMS principal axis rotation error also remained smaller
than 1.5◦(Fig. 8c). This shows that the presented linearized model-based controller (linearized based
on 5.6 m/s wind with no turbulence) is valid for the actual nonlinear system operating under diﬀerent
conditions. These results are also promising compared to another experimental study on H∞control
(with a hexacopter roughly the same size of the octocopter used in this study) [11], where the RMS
position error was calculated between 10 to 15 cm. Note that in ref. [11], the wind disturbance was
generated by a simple fan, without turbulence (with the average wind speed of 7.5 m/s). Meanwhile, this
study generated its wind disturbance in the wind tunnel, with 10% turbulence.
Fig. 8(b-d) shows the main performance metrics obtained from the experimental data. The presented
H∞controller signiﬁcantly outperforms both BL cases in position error (see Fig. 8b). At the maximum
wind speed of 12.8 m/s, the H∞controller yields an RMS position error norm (σξ) 51% lower than the
BL tilted case and 38% lower than the BL planar case. At 0 and 5.6 m/s, there is a signiﬁcant overlap
between the recorded data points for the two BL controllers. However, overlap at 12.8 m/s is minimal,
with the BL planar case resulting in a 21% lower RMS error norm than the BL tilted case. The BL planar
setup has a higher thrust ceiling, allowing it to outperform the BL tilted conﬁguration slightly.
The RMS principal axis rotation error (σ), denoting the shortest rotation between the measured
and desired orientations, shows considerable overlap of the three data sets at non-zero wind speeds (see
https://doi.org/10.1017/S0263574724000523 Published online by Cambridge University Press

## Page 12

12
Jérémie X. J. Bannwarth et al.
Figure 9. Tilted-rotor octocopter response to a step change in desired vectored-thrust acceleration
in altitude hold mode. (a) Desired normalized horizontal accelerations, (b) Attitude, (c) Translational
acceleration, (d) and motor PWM signals.
Fig. 8c). Therefore, the conﬁguration does not have a signiﬁcant eﬀect on the attitude control perfor-
mance at those wind speeds. However, at zero wind speed, the BL planar case yields an RMS rotation
error over twice as large as the other controllers. This diﬀerence is mainly due to the low yaw control
authority of the planar arrangement, which results in higher errors. These increased errors are not seen
at higher wind speeds, which could be due to the aerodynamic loadings acting on the UAV, but further
experimentation is required to identify the source of this behavior.
Wind resistance increases energy consumption as the UAV works harder to overcome the wind dis-
turbances. Having an energy-eﬃcient control strategy to optimize UAV ﬂight endurance and battery life
in the presence of wind is important. The mean RMS of the motor commands (σ χ) is similar for both
tilted cases at zero wind speed. However, the actuator usage of the H∞controller is 23% and 25% higher
than the BL tilted case at 5.6 and 12.8 m/s, respectively (Fig. 8d). This means the H∞controller yields
signiﬁcantly improved station-keeping performance compared to the BL tilted conﬁguration for only a
marginal increase in actuator usage. The BL controller on the planar case requires signiﬁcantly more
https://doi.org/10.1017/S0263574724000523 Published online by Cambridge University Press

## Page 13

Robotica
13
actuator usage across all wind speeds, which is again due to the lack of yaw authority. Resolving this
issue would involve replacing the motors and propellers with larger ones.
5.2. Vectored-thrust demonstration
To demonstrate the vectored-thrust capability and validate the motor mixer presented in Eq. (16), an
experiment is carried out on the tilted-rotor octocopter with zero wind speed. The UAV is manually
ﬂown at an initial altitude of 1.25 m. A step command is applied along the positive Bx-axis at t = 0.5 s
(see Fig. 9a). Despite the command, the attitude of the UAV does not change signiﬁcantly, with all angles
remaining below 0.25◦(see Fig. 9b). Meanwhile, according to Fig. 9c, the UAV accelerates forward at
a rate of around 2.4 m/s2. Fig. 9d shows how the motor mixer immediately converts the desired Bx-axis
command to a PWM diﬀerential. Producing the horizontal acceleration without aﬀecting the attitude of
the UAV validates the motor mixer matrix.
6. Conclusion
A robust H∞output feedback controller was designed and implemented within a cascaded control
structure to regulate the position of a tilted-rotor octocopter under wind disturbances while hovering
at a point. The tilted pattern of the octocopter allows for high-bandwidth, yet saturation-constrained
vectored-thrust, which is not feasible on typical tilt-to-translate planar UAVs. The problem of frequency-
dependent actuator allocation, which is largely ignored in current vectored-thrust UAV literature, is
solved by augmenting the plant model with weighting transfer functions. Reduced order H∞synthesis
is conducted on a linearized version of the augmented model to yield robust performance. 72 free-ﬂight
wind tunnel tests were conducted at wind speeds of 0, 5.6, and 12.8 m/s to compare the H∞controller’s
performance to that of the BL controller on both a tilted and planar octocopter. The H∞controller sig-
niﬁcantly reduced the RMS position error for a slight increase in actuator usage. The H∞RMS position
error decreased by 51% compared to the BL tilted case and 38% to the BL planar case. Conversely,
its actuator usage is 25% higher than the BL tilted case. In free-ﬂight experiments, the octocopter pro-
duced a forward acceleration of 2.4 m/s2 when subjected to a vectored-thrust step while regulating its
pitch angle to less than 0.25◦, successfully demonstrating the eﬀectiveness of the new motor mixer.
Author contribution. JXB: writing initial draft, methodology, experiments, and data analysis. SK: writing, review, and revision.
KS: supervision, review.
Financial support. The research reported in this article was conducted as part of “Enabling unmanned aerial vehicles (UAVs) to
use tools in complex dynamic environments UOCX2104,” which is funded by the New Zealand Ministry of Business, Innovation
and Employment.
Competing interests. The authors declare no competing interests exist.
Ethical approval. None.
References
[1] B. Zhou, J. Yi, X. Zhang, L. Chen, D. Yang, F. Han and H. Zhang, “An autonomous navigation approach for unmanned
vehicle in outdoor unstructured terrain with dynamic and negative obstacles,” Robotica 40(8), 2831–2854 (2022).
[2] T. Elmokadem and A. V. Savkin, “A method for autonomous collision-free navigation of a quadrotor UAV in unknown
tunnel-like environments,” Robotica 40(4), 835–861 (2022).
[3] T.-J. Lin and K. A. Stol, “Faster navigation of semi-structured forest environments using multirotor UAVs,” Robotica 41(2),
735–755 (2023).
https://doi.org/10.1017/S0263574724000523 Published online by Cambridge University Press

## Page 14

14
Jérémie X. J. Bannwarth et al.
[4] Y. Guo, B. Jiang and Y. Zhang, “A novel robust attitude control for quadrotor aircraft subject to actuator faults and wind
gusts,” IEEE/CAA J Autom Sin 5(1), 292–300 (2018). doi: 10.1109/jas.2017.7510679.
[5] J. Hu, C. Bohn and H. R. Wu, “Systematic H∞weighting function selection and its application to the real-time control of
a vertical take-oﬀaircraft,” Control Eng Pract 8(3), 241–252 (2000).
[6] Z. Latif, A. Shahzad, A. I. Bhatti, J. F. Whidborne and R. Samar, “Autonomous landing of an UAV using H∞based model
predictive control,” Drones 6(12), 416 (2022).
[7] M. Rich, N. Elia and P. Jones, “Design and Implementation of an H∞Controller for a Quadrotor Helicopter,” In: 21st
Mediterranean Conference on Control and Automation, Platanias, Greece, (2013) pp. 1189–1198.
[8] G. V. Raﬀo, M. G. Ortega and F. R. Rubio, “An integral predictive/nonlinear H∞control structure for a quadrotor
helicopter,” Automatica 46(1), 29–39 (2010). doi: 10.1016/j.automatica.2009.10.018.
[9] M. Chen and M. Huzmezan, “A combined MBPC/2 DOF H inﬁnity controller for a quad rotor UAV,” AIAA Gui, Navi, Cont
Conf Exhi 5520 (2003), 1–9. doi: 10.2514/6.2003-5520.
[10] C. Massé, O. Gougeon, D.-T. Nguyen and D. Saussié, “Modeling and Control of a Quadcopter Flying in a Wind Field:
A Comparison Between LQR and Structured H∞Control Techniques,” In: 2018 International Conference on Unmanned
Aircraft Systems, Dallas Marriott City, USA (2018) pp. 1408–1417. doi: 10.1109/ICUAS.2018.8453402.
[11] B. Dai, Y. He, G. Zhang, F. Gu, L. Yang and W. Xu, “Wind disturbance rejection for unmanned aerial vehicles using
acceleration feedback enhanced H∞method,” Auton Robot 44(7), 1271–1285 (2020).
[12] J. Zeng, H. Zhong, Y. Wang, S. Fan and H. Zhang, “Autonomous control design of an unmanned aerial manipulator for
contact inspection,” Robotica 41(4), 1145–1158 (2023).
[13] P. Zheng, X. Tan, B. B. Kocer, E. Yang and M. Kovac, “TiltDrone: A fully-actuated tilting quadrotor platform,” IEEE Robot
Auto Lett 5(4), 6845–6852 (2020). doi: 10.1109/lra.2020.3010460.
[14] M. Bhargavapuri, J. Patrikar, S. R. Sahoo and M. Kothari, “A Low-Cost Tilt-Augmented Quadrotor Helicopter: Modeling
and Control,” In: 2018 International Conference on Unmanned Aircraft Systems, Dallas Marriott City, USA (2018)
pp. 186–194. doi: 10.1109/ICUAS.2018.8453376.
[15] T. Anzai, M. Zhao, M. Murooka, F. Shi, K. Okada and M. Inaba, “Modeling and Control of Fully Actuated 2D Transformable
Aerial Robot with 1 DoF Thrust Vectorable Link Module,” In: 2019 IEEE/RSJ International Conference on Intelligent
Robots and Systems, Macau, Macau (2019) pp. 2820–2826. doi: 10.1109/IROS40897.2019.8967725.
[16] S. Panza, M. Lovera, M. Sato and K. Muraoka, “Structured μ-synthesis of robust attitude control laws for quad-tilt-wing
unmanned aerial vehicle,” J Guid Control Dyn 43(12), 2258–2274 (2020). doi: 10.2514/1.g005080.
[17] D.
Brescianini
and
R.
D’Andrea,
“An
omni-directional
multirotor
vehicle,”
Mechatron
55,
76–93
(2018).
doi: 10.1016/j.mechatronics.2018.08.005.
[18] B. Crowther, A. Lanzon, M. Maya-Gonzalez and D. Langkamp, “Kinematic analysis and control design for a nonplanar
multirotor vehicle,” J Guid Control Dyn 34(4), 1157–1171 (2011). doi: 10.2514/1.51186.
[19] J. M. Arizaga, H. Castaneda and P. Castillo, “Adaptive Control for a Tilted-Motors Hexacopter UAS Flying on a Perturbed
Environment,” In: 2019 International Conference on Unmanned Aircraft Systems, Atlanta, USA (2019) pp. 171–177.
doi: 10.1109/ICUAS.2019.8798048.
[20] H. Das, “A Comparative Study between a Cant Angle Hexacopter and a Conventional Hexacopter,” In: International
Conference on Control, Instrumentation, Communication and Computational Technologies, Kumaracoil, India (2016)
pp. 501–506. doi: 10.1109/ICCICCT.2016.7988002.
[21] D. Kotarski, P. Piljek, H. Brezak and J. Kasać, “Chattering-free tracking control of a fully actuated multirotor with passively
tilted rotors,” Trans Famena 42(1), 1–14 (2018). doi: 10.21278/tof.42101.
[22] J. Y. S. Lee, K. K. Leang and W. Yim, “Design and control of a fully-actuated hexrotor for aerial manipulation applications,”
J. Mech. Robot 10(4), 1–10 (2018). doi: 10.1115/1.4039854.
[23] P. J. Sanchez-Cuevas, A. Gonzalez-Morgado, N. Cortes, D. B. Gayango, A. E. Jimenez-Cano, A. Ollero and G. Heredia,
“Fully-actuated aerial manipulator for infrastructure contact inspection: Design, modeling, localization, and control,”
Sensors 20(17), 4708 (2020). doi: 10.3390/s20174708.
[24] C. Yao, J. Krieglstein and K. Janschek, “Modeling and sliding mode control of a fully-actuated multirotor with tilted
propellers,” IFAC-PapOnL 51(22), 115–120 (2018). doi: 10.1016/j.ifacol.2018.11.527.
[25] Z. J. Chen, K. A. Stol and P. J. Richards, “Preliminary design of multirotor UAVs with tilted-rotors for improved disturbance
rejection capability,” Aerosp Sci Technol 92, 635–643 (2018). doi: 10.1016/j.ast.2019.06.038.
[26] Z. J. Chen, J. X. J. Bannwarth, K. A. Stol and P. J. Richards, “Analysis of a Multirotor UAV with Tilted-Rotors for the
Purposes of Disturbance Rejection,” In: Proceedings of the 2018 International Conference on Unmanned Aircraft Systems,
Dallas, TX, USA (2018) pp. 864–873. doi: 10.1109/ICUAS.2018.8453383.
[27] S. R. Nekoo, J. Á. Acosta and A. Ollero, “Quaternion-based state-dependent diﬀerential Riccati equation for quadrotor
drones: Regulation control problem in aerobatic ﬂight,” Robotica 40(9), 3120–3135 (2022).
[28] J. X. J. Bannwarth, Z. J. Chen, K. A. Stol, B. A. MacDonald and P. J. Richards, “Aerodynamic force modeling of multirotor
unmanned aerial vehicles,” AIAA J 57(3), 1250–1259 (2019). doi: 10.2514/1.j057165.
[29] L. Meier, D. Agar, B. Küng, T. Gubler, D. Sidrane, J. Oes, A. Babushkin, M. Charlebois, R. Bapst, D. Mannhart, A. D.
Antener, J. Goppert, A. Tridgell, P. Riseborough, M. Grob, M. Whitehorn, S. Wilks, K. Mohammed, S. Smeets, P. Kirienko,
N. Marques, C. Tobler, J. Jansen, M. Rivizzigno, D. Gagne, B. Siesta, J. R. de Souza, F. Achermann and J. Lecoeur, “PX4
ﬁrmware: V1.8.2 stable release,” Zenodo, (2018). doi: 10.5281/zenodo.1493485.
https://doi.org/10.1017/S0263574724000523 Published online by Cambridge University Press

## Page 15

Robotica
15
[30] D. Brescianini, M. Hehn and R. D’Andrea, “Nonlinear quadrocopter attitude control: Technical report,” ETH Zürich, Zürich,
Switzerland, (2013). doi: 10.3929/ETHZ-A-009970340.
[31] S. Gumussoy, D. Henrion, M. Millstone and M. L. Overton, “Multiobjective robust control with HIFOO 2.0,” IFAC Proceed
Vol 42(6), 144–149 (2009). doi: 10.3182/20090616-3-il-2002.00025.
Cite this article: J. X. J. Bannwarth, S. Kazemi and K. Stol, “Frequency-dependent H∞control for wind disturbance rejection
of a fully actuated UAV”, Robotica. https://doi.org/10.1017/S0263574724000523
https://doi.org/10.1017/S0263574724000523 Published online by Cambridge University Press
