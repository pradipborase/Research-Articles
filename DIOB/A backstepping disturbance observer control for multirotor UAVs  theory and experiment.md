# A backstepping disturbance observer control for multirotor UAVs  theory and experiment.pdf

## Page 1

International Journal of Control
ISSN: 0020-7179 (Print) 1366-5820 (Online) Journal homepage: www.tandfonline.com/journals/tcon20
A backstepping disturbance observer control for
multirotor UAVs: theory and experiment
Amir Moeini, Alan F. Lynch & Qing Zhao
To cite this article: Amir Moeini, Alan F. Lynch & Qing Zhao (2022) A backstepping disturbance
observer control for multirotor UAVs: theory and experiment, International Journal of Control,
95:9, 2364-2378, DOI: 10.1080/00207179.2021.1912393
To link to this article:  https://doi.org/10.1080/00207179.2021.1912393
Published online: 05 May 2021.
Submit your article to this journal 
Article views: 806
View related articles 
View Crossmark data
Citing articles: 13 View citing articles 
Full Terms & Conditions of access and use can be found at
https://www.tandfonline.com/action/journalInformation?journalCode=tcon20

## Page 2

INTERNATIONAL JOURNAL OF CONTROL
2022, VOL. 95, NO. 9, 2364–2378
https://doi.org/10.1080/00207179.2021.1912393
A backstepping disturbance observer control for multirotor UAVs: theory and
experiment
Amir Moeini, Alan F. Lynch and Qing Zhao
Department of Electrical and Computer Engineering, University of Alberta, Edmonton, AB, Canada
ABSTRACT
This paper presents a backstepping disturbance observer based control (DOBC) for trajectory tracking
motion control of multirotor Unmanned Aerial Vehicles (UAVs). Two disturbance observers (DO) estimate
external force and torque disturbances acting on the UAV. A nonlinear backstepping dynamic state feed-
back is proposed which uses the DO estimates to achieve exponential stability for the closed-loop tracking
error under constant disturbances. The stability analysis accounts for the entire nonlinear vehicle model
which includes translational and rotational dynamics. Software-in-the-loop simulation and experimen-
tal results are presented showing the effectiveness of the proposed method using the commonly used
PX4/Pixhawk development framework.
ARTICLE HISTORY
Received 9 May 2020
Accepted 15 March 2021
KEYWORDS
Backstepping control;
disturbance observer-based
control (DOBC); unmanned
aerial vehicles (UAVs)
1. Introduction
Multirotor Unmanned Aerial Vehicles (UAVs) are popular due
to their simple robust electro-mechanical design, high manoeu-
vrability, and low-cost. They are used in environment monitor-
ing, terrain mapping, emergency response, and other applica-
tions (Kendoul, 2012). Increased adoption depends on a high-
performance motion controller which can track desired 3D
position and yaw trajectories. There are a number of challenges
involved in improving motion control given the system’s under-
actuated nonlinear dynamics, bounded input, unmeasured and
time-delayed states, and external disturbances. These challenges
have attracted significant interest from the research community.
This paper focuses on improving the robustness of nonlinear
motion control to external force and torque disturbances. This
robustness is clearly important for improving the performance
and safety in a range of environments. For example, in outdoor
applications, the UAV is subject to disturbances such as wind-
gusts or changes in thrust due to nearby obstacles. As confirmed
by the interest shown in recent literature on the topic, improv-
ing the robustness of motion control is clearly an important
practical and theoretical problem.
Many linear and nonlinear motion control laws have been
proposed (Hua et al., 2013). Typically linear control is based
on an approximate linear model. Examples of linear designs
include Proportional-Integral-Derivative (PID) control in Hua
et al. (2013) or Linear Quadratic (LQ) optimal control in Liu
et al. (2016) and Nonami et al. (2010). Since linear designs
lead to a local convergence result, nonlinear control methods,
which directly account for system nonlinearity, have been pro-
posed to achieve a wider operating range. Examples of nonlinear
methods include backstepping in Castillo et al. (2005), feedback
linearisation in Koo and Sastry (1998), sliding mode in Reinoso
et al. (2016), and differential flatness in Kumar (2011), Faessler
CONTACT Alan F. Lynch
alan.lynch@ualberta.ca
Department of Electrical and Computer Engineering, University of Alberta, Edmonton, T6G 1H9 AB, Canada
et al. (2018) and Poultney et al. (2018). However, most of the
proposed methods suffer from a lack of any rigorous analysis
of robustness to external disturbances. Some exceptions which
address robustness include adaptive techniques (Cabecinhas
et al., 2014; Goodarzi et al., 2015), integral state augmenta-
tion (Bouabdallah, 2007; Omari et al., 2013), sliding surfaces
(Madani & Benallegue, 2006; Sumantri et al., 2013), or distur-
bance observer-based control (DOBC) (Dong et al., 2014; He
et al., 2014; Lee et al., 2016; Shao et al., 2018). We review the
relevant subset of these papers below which are related to the
proposed nonlinear DOBC.
We remark that many proposed methods have an inner-
outer loop control structure which separates the design for the
translational and rotational subsystems. This leads to a sim-
ple design and is found in field-tested autopilots (Meier, 2018).
However, most methods which have this structure do not anal-
yse the effect of inner-outer loop coupling on the stability of the
entire (i.e. combined rotational and translational) system. The
method we propose does not take an inner-outer loop structure
and features a stability analysis which accounts for the entire
dynamics.
A number of researchers have applied adaptive control to
improve robustness. An adaptive backstepping controller is
developed in Cabecinhas et al. (2014) with asymptotically sta-
ble tracking error for constant force disturbances. The state of
the system is augmented with thrust and its time derivative, and
overparameterization of the disturbance estimate leads to two
third-order update laws. A saturation function limits thrust and
a projection operator avoids wind-up of force estimates. The
overparameterization, projection operator, and saturation sig-
nificantly increase the complexity of the control. The method is
validated experimentally with the controller implemented on a
ground computer using Matlab. Work in Goodarzi et al. (2015)
© 2021 Informa UK Limited, trading as Taylor & Francis Group

## Page 3

INTERNATIONAL JOURNAL OF CONTROL
2365
designs an adaptive nonlinear control which compensates for
disturbances. To avoid the singularities of Euler angles or the
unwinding phenomenon of quaternions, the controller is devel-
oped on SE(3), i.e. it uses rotation matrices to represent attitude.
Separate attitude and position control modes are proposed. In
both modes, adaptive laws compensate the effect of constant
disturbances. The position mode provides position tracking by
relating the direction of desired thrust to the position error.
This direction defines a column of the desired rotation matrix.
Almost global attractiveness is guaranteed in the case of con-
stant disturbances provided certain gain conditions are satisfied.
The authors do not consider the effect of mode switching on the
stability of the hybrid system. The method is validated in simu-
lation and experiment but the effect of external disturbances is
not investigated.
Integral augmentation is another method used for improv-
ing robustness and is combined with nonlinear control with an
inner-outer loop structure in Omari et al. (2013). The effect of
rotor drag and blade flapping is included in the dynamic model
and controller design. The outer loop controller is designed
to control position and linear velocity. To achieve robustness
against model uncertainty and external disturbances, saturated
integrators with fast desaturation are employed. The approach is
experimentally validated for various reference trajectories and
in the presence of wind forces. However, only asymptotic (as
opposed to exponential) stability is proven for the outer loop
design and the effect of inner-loop tracking error on closed-loop
performance is not considered.
Sliding mode control is commonly used to improve robust-
ness in a range of applications. A nonlinear sliding surface
(NSS) method with inner-outer loop structure is presented in
Sumantri et al. (2013). Experimental results are presented which
include an external disturbance from a small fan. Motion is
constrained as the UAV is attached to a stand for safety. Work
in Madani and Benallegue (2006) combines backstepping and
sliding mode techniques. The dynamics is divided into four sub-
systems: lateral position, altitude, yaw, and actuator dynamics.
To avoid complex expressions for the control law, low-pass fil-
tered derivatives are employed to estimate derivatives of the
virtual control. Asymptotic stability of the closed-loop is derived
without accounting for subsystem interaction. The sign func-
tion used in the sliding surface equation is approximated by a
continuous function to address chattering. However, the effect
of this approximation is not investigated in the stability proof.
The method is validated on a stand which limits motion to
vertical and yaw DoF.
DOBC is presented in a number of papers. Work in He
et al. (2014) combines a DO with backstepping for a traditional
helicopter UAV. Low-pass filtered derivatives of virtual con-
trols are employed for angular acceleration estimation. Filter-
ing estimation error leads to ultimate boundedness of tracking
error. Work in Shao et al. (2018) integrates an inner-outer loop
backstepping control with an extended state observer (ESO)
to account for parametric uncertainty and disturbances. Lin-
ear and angular velocity are assumed unmeasured and esti-
mated by the ESO alongside the disturbance. For simplify-
ing the control expressions, dynamic surface control is used.
The inner-loop control relies on simplified rotational dynam-
ics. The design yields ultimately bounded tracking error for
time-varying disturbances. The method is validated in sim-
ulation. Work in Dong et al. (2014) proposes a DOBC with
backstepping and inner-outer loop structure. Simplified rota-
tional dynamics is considered and the translational system is
approximated near hover. A range of system uncertainty is con-
sidered: unstructured model error, input delay, and external
disturbances. Ultimate boundedness is proven and simulation
and experimental results are presented using a fan as a distur-
bance. Work in Lee et al. (2016) presents a linear DOBC for
hover control. The inverse of the model’s transfer function is
used to estimate the external force disturbance. This estimate
is used in an inner-outer loop control structure. Stability analy-
sis is performed using the Small Gain Theorem. Simulation and
experimental results are presented including a comparison with
backstepping without a DO.
In this work, we propose a nonlinear backstepping DOBC
for multirotor UAV trajectory tracking. The DO improves the
closed-loop’s robustness to external force and torque distur-
bances. Although the idea of using a DO and backstepping
state feedback is not new e.g. Cabecinhas et al. (2014) and Shao
et al. (2018), the particular closed-loop structure of the pro-
posed DOBC is a main contribution. Specifically, the DO error
dynamics is LTI, globally exponentially stable, and depends only
on disturbance estimate error. The disturbance estimate error
feeds the tracking error dynamics in a cascade interconnection.
This cascade structure makes the stability analysis, implemen-
tation, and controller tuning straightforward. In particular, the
convergence of the tracking error is proven by analysing the sys-
tem dynamics in the error coordinates defined from the back-
stepping procedure. It is shown that the tracking error dynamics
is Linear Time-varying (LTV) with the disturbance estimate
error acting as a system input. Using LTV system stability anal-
ysis, exponential stability is proven in the presence of constant
disturbances. Exponential convergence is an important prop-
erty since it ensures robust closed-loop stability and ultimate
boundedness of the tracking error in the case of time-varying
disturbances. The simplicity of the proposed control is seen in
comparison with our previous work (Moeini et al., 2019) where
a more general controller structure is used. Here, expressions for
the control are too complex for on-board implementation and
only Matlab simulation results are presented.
Another important aspect of this work is that the control
design relies on the entire system dynamics, i.e. the coupled
translational and rotational rigid body dynamics. This avoids
having to make common simplifying assumptions typical of
designs with inner-outer loop structure (e.g. linear approxima-
tion of the rotational dynamics) during the closed-loop sta-
bility analysis of the entire rotational and translational system
dynamics (Martin & Salaün, 2010). Although designs based
on the entire dynamics exist in the literature, such designs
do not explicitly address robustness to disturbances (Poult-
ney et al., 2019) or provide experimental testing (Cabecinhas
et al., 2014).
Another important contribution of this work is the valida-
tion performed in simulation and experiment using the stan-
dard PX4 autopilot under realistic flight conditions. The PX4
firmware is a widely-used and open source project intended for
research and commercial use. It runs on a number of hard-
ware platforms including the Pixhawk family. Although the

## Page 4

2366
A. MOEINI ET AL.
proposed design was simulated in Matlab initially, we present
a Software-In-The-Loop (SITL) simulation where the DOBC
runs in a virtual environment which matches that of autopi-
lot hardware running PX4. SITL simulation is an important
step in the development of flight controllers since it allows for
safe and efficient debugging and tuning. This is compared with
most existing simulation results which are mostly Matlab-based
(Antonelli et al., 2018; Moeini et al., 2019; Shao et al., 2018)
and do not capture the many real-world constraints of on-board
implementation (e.g. multi-rate measurements, control, and
state estimation, bounded signals, and constrained hardware
resources).
The proposed method is also implemented experimentally
using the Applied Nonlinear Control Lab (ANCL) quadro-
tor platform in the presence of a wind disturbance. In sim-
ulation and experiment, the proposed method is compared
with a traditional backstepping controller and the built-in PX4
motion controller. The results demonstrate improved perfor-
mance for the proposed backstepping DOBC. It is important
to note that our implementation does not require simplify-
ing approximations (e.g. small-angle assumptions, negligible
coupling between inner and outer loops) that are common in
work with experimental validation (Antonelli et al., 2018; Dong
et al., 2014; Shao et al., 2018). By basing our work on the open
source and commonly used PX4 platform, our results are acces-
sible to the research community. The self-contained PX4 code
used in the paper is available online at Moeini and Lynch (2020)
and can be used to reproduce our results. Other experimental
work suffers from controller implementation on ground station
computers (Cabecinhas et al., 2014, 2015). In this case, the wire-
less connection can limit the reliability and performance of the
design.
The organisation of the paper is as follows: Section 2 presents
the quadrotor modelling. In Section 3, the DOBC is presented
and its stability proof given. In Section 4, the proposed method
is validated in simulation and experiment.
2. Quadrotor dynamics
In this section, we review a traditional rigid body quadrotor
model and establish notation for control design. The dynam-
ics of the quadrotor has been presented in many works such
as Castillo et al. (2005) and Bouabdallah (2007). We consider
a traditional quadrotor UAV as shown in Figure 1. Two refer-
ence frames are needed: a fixed inertial navigation frame N with
orthonormal basis {n1, n2, n3} and a body frame B whose origin
is at the vehicle’s centre of mass (CoM) and with orthonormal
basis {b1, b2, b3}. We define b1 to point in the forward direction
of vehicle, b2 pointing right, and b3 pointing down. The config-
uration of the quadrotor belongs to the special Euclidean group
SE(3), and includes the position p ∈R3 of the origin of B rel-
ative to N, and the orientation R ∈SO(3) of B with respect to
N. We assume each propeller generates thrust in the −b3 direc-
tion and denote the total thrust created by all the propellers by
the scalar input u ≥0, i.e. the thrust vector is −ub3. Control-
ling individual propeller speeds creates an input torque denoted
τ ∈R3 which is expressed in B. To simplify the presentation
of the controller design, we take torque τ and thrust u as the
system inputs. However, the actual physical inputs to the UAV
Figure 1. DiagramofaquadrotorshowingbodyframeB andnavigationframeN.
propellers are PWM signals to the Electronic Speed Controller
(ESC), which are denoted Wi, i = 1, 2, 3, 4. We assume a one-
to-one relation between the torque and thrust (u, τ) and the
physical inputs Wi, i = 1, 2, 3, 4. For a quadrotor in “cross”
configuration we have
u
τ

=
⎡
⎢⎢⎣
Ku
Ku
Ku
Ku
−Kuℓs
Kuℓs
Kuℓs
−Kuℓs
Kuℓc
−Kuℓc
Kuℓc
−Kuℓc
−Kτ
−Kτ
Kτ
Kτ
⎤
⎥⎥⎦
⎡
⎢⎢⎣
˜W2
1
˜W2
2
˜W2
3
˜W2
4
⎤
⎥⎥⎦
(1)
where Ku is a thrust constant, Kτ is a counter torque con-
stant, ℓis arm length,  is the angle between the arm and b1
axis, s = sin , c = cos , and ˜Wi is a normalised PWM
signal defined by ˜Wi = (Wi −Wmin)/(Wmax −Wmin) where
Wmin and Wmax are the minimum and maximum values of Wi,
respectively. Therefore, ˜Wi ∈[0, 1] and the inputs (u and τ) are
bounded. However, we do not explicitly account for this satu-
ration in the control design. The multirotor dynamics can be
expressed by
˙p = v
(2a)
m˙v = mgn3 −uRn3 + df
(2b)
˙R = RS(ω)
(2c)
J ˙ω = −ω × Jω + τ + dτ
(2d)
where v ∈R3 is linear velocity expressed in N, ω ∈R3 is angu-
lar velocity expressed in B, m is mass, J is inertia, g is the
gravity constant, and n3 = [0, 0, 1]⊤. The force disturbance df ∈
R3 and torque disturbance dτ ∈R3 are unknown and used to
model external disturbances such as wind gusts or other model
uncertainties. The skew operator S(·) : R3 →so(3) is defined as
S(x) =
⎡
⎣
0
−x3
x2
x3
0
−x1
−x2
x1
0
⎤
⎦,
where x =
⎡
⎣
x1
x2
x3
⎤
⎦.
In Section 3, we use ZYX Euler parameterisation for deriving
the control for the yaw or heading angle. We denote the Euler
angles as η = [φ, θ, ψ]⊤, where φ, θ and ψ are roll, pitch, and
yaw, respectively. The rotational kinematics (2c) expressed in η
are ˙η = W(η)ω with
W(η) =
⎡
⎣
1
sφtθ
cφtθ
0
cφ
−sφ
0
sφ/cθ
cφ/cθ
⎤
⎦
where tθ = tan θ.

## Page 5

INTERNATIONAL JOURNAL OF CONTROL
2367
3. Disturbance observer based control (DOBC) design
This section designs a trajectory tracking controller for the
quadrotor dynamics (2). Given smooth bounded desired tra-
jectories for position and yaw, denoted by pd ∈R3 and ψd ∈
R, respectively, we derive a dynamic state feedback control for
inputs u and τ to ensure exponential convergence of the tracking
errors p −pd and ψ −ψd in the presence of bounded constant
disturbances df and dτ. The full state measurement is assumed
available. The proposed design adopts a backstepping approach
inspired by Cabecinhas et al. (2014) and the references within.
As discussed in the previous section, the approach in Cabecin-
has et al. (2014) relies on six-dimensional parameter update
laws to estimate df , whereas the proposed method uses one 3-
dimensional DO for force disturbance estimation. Decoupling
the observer from the state feedback ensures a minimal order
of 3 for the DO of df . Since p and ψ can be independently con-
trolled, the design is divided into two sections: position and yaw
control.
3.1 Disturbance observer
We consider the DO for estimating the force disturbance
ˆdf = zdf + kdf mv
(3a)
˙zdf = −kdf ˆdf −kdf (mgn3 −uRn3)
(3b)
where zdf ∈R3 is the observer state, ˆdf ∈R3 is disturbance esti-
mate, and kdf > 0 is an observer gain. Assuming df is constant
(i.e. ˙df = 0) and defining ˜df = df −ˆdf , observer (3) has error
dynamics
˙˜df = −(˙zdf + kdf m˙v)
= kdf ˆdf + kdf (mgn3 −uRn3) −kdf (mgn3 −uRn3 + df )
= −kdf ˜df
(4)
which is globally exponentially stable.
3.2 Position tracking control
In this section, we design a controller for position tracking.
We start by defining a tracking error δ1 = p −pd and the first
Lyapunov function candidate V1 = 1
2∥δ1∥2. Using (2a) gives
˙V1 = δ⊤
1 ˙δ1 = δ⊤
1 (v −vd)
(5)
where vd = ˙pd. Taking v as a virtual control to (5) we choose
α1 = vd −k1δ1 as its desired value, where k1 > 0 is a scalar
controller gain. Defining the second error coordinate as δ2 =
mv −mα1 we get
˙δ1 = −k1δ1 + δ2/m.
(6)
Substituting this expression into (5) we have ˙V1 = −k1∥δ1∥2 +
δ⊤
1 δ2/m. Next, considering the second Lyapunov function can-
didate V2 = V1 + 1
2∥δ2∥2 and taking its time derivative we have
˙V2 = −k1∥δ1∥2 + 1
mδ⊤
2 δ1 + δ⊤
2 ˙δ2.
(7)
Substituting df = ˆdf + ˜df and ˙α1 into the expression for ˙δ2 gives
˙δ2 = m˙v −m˙α1
= mgn3 −uRn3 + ˆdf + ˜df −m˙vd + mk1v −mk1vd
(8)
where we have used (2b). Hence, substituting (8) into (7) gives
˙V2 = −k1∥δ1∥2 + 1
mδ⊤
2 δ1 + δ⊤
2 (mgn3 −uRn3 + ˆdf + ˜df
−m˙vd + mk1v −mk1vd).
(9)
We denote α2 as the desired value for the second virtual control
uRn3 and take
α2 = mgn3 + ˆdf −m˙vd + mk1v −mk1vd + 1
mδ1 + k2δ2
(10)
where k2 > 0 is a controller gain. We remark that the vir-
tual input uRn3 is the thrust vector expressed in inertial frame
N. Introducing the third error coordinate δ3 = α2 −uRn3 and
substituting (10) into (9) gives
˙V2 = −k1∥δ1∥2 −k2∥δ2∥2 + δ⊤
2 δ3 + ˜d⊤
f δ2.
(11)
and
˙δ2 = −δ1/m −k2δ2 + δ3 + ˜df .
(12)
Now considering V3 = V2 + 1
2∥δ3∥2 as the third Lyapunov
function candidate and taking its time derivative, by substitut-
ing (11) we get
˙V3 = −k1∥δ1∥2 −k2∥δ2∥2 + δ⊤
2 δ3 + ˜d⊤
f δ2 + δ⊤
3 ˙δ3
(13)
where
˙δ3 = ˙α2 −˙uRn3 −uRS(ω)n3
= ˙ˆdf −m¨vd + k1(mgn3 −uRn3 + df ) −mk1˙vd
+ 1
m(v −vd) + k2(mgn3 −uRn3 + df
−m˙vd + mk1v −mk1vd) −˙uRn3 −uRS(ω)n3.
(14)
Substituting (4) and df = ˆdf + ˜df in (14) we obtain
˙δ3 = β + (kdf + k1 + k2)˜df −˙uRn3 −uRS(ω)n3
(15)
where β is a function of known variables
β = −m¨vd + k1mgn3 −k1uRn3 + k1ˆdf −mk1˙vd
+ 1
mv −1
mvd + k2mgn3 −k2uRn3 + k2ˆdf
−k2m˙vd + k2mk1v −k2mk1vd.
Hence, substituting (15) into (13) gives
˙V3 = −k1∥δ1∥2 −k2∥δ2∥2 + δ⊤
2 δ3
+ δ⊤
3 (β −˙uRn3 −uRS(ω)n3)
+ ˜d⊤
f (δ2 + (kdf + k1 + k2)δ3)

## Page 6

2368
A. MOEINI ET AL.
The terms uRS(ω)n3 and ˙uRn3 can be written as
uRS(ω)n3 = R
⎡
⎣
uω2
−uω1
0
⎤
⎦,
˙uRn3 = R
⎡
⎣
0
0
˙u
⎤
⎦.
Since u is the system input, we can assign the value of ˙u at this
stage and continue the backstepping design with uRS(ω)n3 as a
virtual control. So we choose
˙u = n⊤
3 R⊤(β + δ2 + k3δ3)
(16)
where k3 > 0 is a controller gain. Letting δ4 = α3 −uRS(ω)n3
where
α3 = R[I −n3n⊤
3 ]R⊤(β + δ2 + k3δ3)
(17)
gives us
˙δ3 = −δ2 −k3δ3 + δ4 + (kdf + k1 + k2)˜df .
(18)
The choice (16) and (17) cancels the effect of indefinite terms
δ⊤
2 δ3 and δ⊤
3 β in ˙V3 and adds a damping term −k3∥δ3∥2.
We have
˙V3 = −k1∥δ1∥2 −k2∥δ2∥2 −k3∥δ3∥2 + δ⊤
3 δ4
+ ˜d⊤
f (δ2 + (kdf + k1 + k2)δ3).
Considering V4 = V3 + 1
2∥δ4∥2 as a new Lyapunov function
candidate, we have
˙V4 = −k1∥δ1∥2 −k2∥δ2∥2 −k3∥δ3∥2 + δ⊤
3 δ4
+ ˜d⊤
f (δ2 + (kdf + k1 + k2)δ3) + δ⊤
4 ˙δ4
where
˙δ4 = ˙α3 −˙uRS(ω)n3 −uRS(ω)2n3 −uRS( ˙ω)n3
(19)
and
˙α3 = RS(ω)[I −n3n⊤
3 ]R⊤(β + δ2 + k3δ3)
+ R[I −n3n⊤
3 ]S(ω)⊤R⊤(β + δ2 + k3δ3)
+ R[I −n3n⊤
3 ]R⊤( ˙β + ˙δ2 + k3 ˙δ3).
Calculating expressions for ˙β, ˙δ2 and ˙δ3 and substituting df =
ˆdf + ˜df we obtain
˙β = ˙β′ +

k1kdf + 1
m2 + k2kdf + k1k2

˜df
˙δ2 = ˙δ′
2 + ˜df
˙δ3 = ˙δ′
3 + (kdf + k1 + k2)˜df
where ˙β′, ˙δ′
2 and ˙δ′
3 are the known parts of ˙β, ˙δ2 and ˙δ3,
respectively, and given by
˙β′ = −m...v d −k1 ˙uRn3 −k1uRS(ω)n3 −mk1¨vd
+ 1
m2 (mgn3 −uRn3 + ˆdf ) −1
m ˙vd
−k2 ˙uRn3 −k2uRS(ω)n3 −k2m¨vd
+ k2k1(mgn3 −uRn3 + ˆdf ) −k1k2m˙vd
˙δ′
2 = mgn3 −uRn3 + ˆdf −m˙vd + mk1v −mk1vd
˙δ′
3 = β −˙uRn3 −uRS(ω)n3.
Therefore, the known part of ˙α3 can be defined by ˙α′
3 : ˙α3 =
˙α′
3 + kR[I −n3n⊤
3 ]R⊤˜df where
˙α′
3 = RS(ω)[I −n3n⊤
3 ]R⊤(β + δ2 + k3δ3)
+ R[I −n3n⊤
3 ]S(ω)⊤R⊤(β + δ2 + k3δ3)
+ R[I −n3n⊤
3 ]R⊤( ˙β′ + ˙δ′
2 + k3 ˙δ′
3)
and
k =

k1kdf + 1
m2 + k2kdf + k1k2

+ 1 + k3(kdf + k1 + k2).
Now we can write the expression for ˙V4 as
˙V4 = −k1∥δ1∥2 −k2∥δ2∥2 −k3∥δ3∥2
+ δ⊤
4 (˙α′
3 + δ3 −˙uRS(ω)n3 −uRS(ω)2n3 −uRS( ˙ω)n3)
+ ˜d⊤
f (δ2 + (kdf + k1 + k2)δ3 + kR[I −n3n⊤
3 ]R⊤δ4)
At this stage, we define a desired value for the rate of angular
velocity ˙ωd, such that
δ⊤
4 (˙α′
3 + δ3 −˙uRS(ω)n3 −uRS(ω)2n3 −uRS( ˙ωd)n3)
= −k4δ⊤
4 δ4
where k4 > 0 is a controller gain. This leads to the expres-
sion −k4∥δ4∥2 appearing in ˙V4. Considering the structure for
S( ˙ωd)n3, we can write the above equation as
δ⊤
4 R
⎡
⎣
˙ωd2
−˙ωd1
0
⎤
⎦u = δ⊤
4 (˙α′
3 + δ3 −˙uRS(ω)n3
−uRS(ω)2n3 + k4δ4).
(20)
Now using the fact that the third component of R⊤δ4 is zero, we
conclude that (20) is satified by selecting
˙ωd1 = −n⊤
2 R⊤
u
(˙α′
3 −˙uRS(ω)n3 −uRS(ω)2n3 + δ3 + k4δ4)
(21a)
˙ωd2 = n⊤
1 R⊤
u
(˙α′
3 −˙uRS(ω)n3 −uRS(ω)2n3 + δ3 + k4δ4).
(21b)
In order to obtain the expressions for the torque input τ which
achieves position tracking, we consider ˙ωd3 = 0. Now we try to
get the expression for torque which is the actual sytem input.

## Page 7

INTERNATIONAL JOURNAL OF CONTROL
2369
From the rotational dynamics, we consider
τ = J ˙ωd + ω × Jω −ˆdτ
(22)
where, ˆdτ is the torque disturbance estimate introduced to
cancel the effect of dτ. From (22) and (2d), we get
˙ω = ˙ωd + J−1˜dτ.
(23)
Substituting (21) and (23) in ˙δ4, gives us
˙δ4 = −δ3 −k4δ4 + uRS(n3)J−1˜dτ + kR[I −n3n⊤
3 ]R⊤˜df .
(24)
Now we can write the following expression for ˙V4
˙V4 = −k1∥δ1∥2 −k2∥δ2∥2 −k3∥δ3∥2 −k4∥δ4∥2
+ δ⊤
4 uRS(n3)J−1˜dτ + ˜d⊤
f (δ2 + (kdf + k1 + k2)δ3
+ kR[I −n3n⊤
3 ]R⊤δ4).
Therefore, at this stage, we design a torque disturbance observer
using the same observer structure we used for the force distur-
bance
ˆdτ = zdτ + kdτ Jω
(25a)
˙zdτ = −kdτ ˆdτ −kdτ (−ω × Jω + τ)
(25b)
which results in exponentially stable error dynamics ˙˜dτ =
−kdτ ˜dτ, where kdτ > 0.
The closed-loop stability of the proposed backstepping con-
troller is summarised by the following theorem.
Theorem 3.1: Given system (2) with constant disturbances df
and dτ, bounded smooth reference trajectory pd and assum-
ing u> 0, the equilibrium [δ⊤
1 , δ⊤
2 , δ⊤
3 , δ⊤
4 , ˜d⊤
f , ˜d⊤
τ ]⊤= 0 of the
closed-loop dynamics is exponentially stable with dynamic state
feedback control (3), (16), (21), (22) and (25).
Proof: Denoting δ = [δ⊤
1 , δ⊤
2 , δ⊤
3 , δ⊤
4 ]⊤and ˜d = [˜d⊤
f , ˜d⊤
τ ]⊤
then from (6), (12), (18) and (24) the tracking error dynamics is
˙δ = Aδ + B(t)˜d
(26)
where
A =
⎡
⎢⎢⎣
−k1I3
I3/m
03
03
−I3/m
−k2I3
I3
03
03
−I3
−k3I3
I3
03
03
−I3
−k4I3
⎤
⎥⎥⎦,
B(t) =
⎡
⎢⎢⎣
03
03
I3
03
(kdf + k1 + k2)I3
03
kR[I −n3n⊤
3 ]R⊤
uRS(n3)J−1
⎤
⎥⎥⎦.
where I3 denotes the 3 × 3 identity matrix and 03 denotes the
3 × 3 zero matrix. Using the result (Marino & Tomei, 1995,
Lemma. III.1), we can show the equilibrium of (26) is exponen-
tially stable if its zero-input dynamics is exponentially stable,
∥B(t)∥< BM for some constant BM, and input ˜d is exponen-
tially convergent. Since the eigenvalues of A have negative real
parts for any k1, k2, k3, k4 > 0, we know the zero-input dynam-
ics of (26) is exponentially stable. Also, ∥B(t)∥is bounded since
the rotation matrix R and thrust u are bounded. Since the distur-
bance estimate error dynamics is exponentially stable, we know
˜d is exponentially convergent, i.e. ∥˜d∥≤Me−αt, where α, M >
0. Therefore, the equilibrium [δ⊤
1 , δ⊤
2 , δ⊤
3 , δ⊤
4 , ˜d⊤
f , ˜d⊤
τ ]⊤= 0 of
closed-loop (2), (3), (16), (21), (22), and (25) is exponentially
stable.
■
3.3 Yaw and position tracking control
In this subsection, we develop a controller to track trajectories
for yaw using τ3. Given a smooth bounded reference trajectory
ψd, we define the tracking error ϵ1 = ψ −ψd, and consider
the Lyapunov function candidate Vψ1 = 1
2∥ϵ1∥2 whose time
derivative is ˙Vψ1 = ϵ1( ˙ψ −˙ψd). We take ˙ψ as a virtual con-
trol and define ϵ2 = ˙ψ −αψ1, where αψ1 = ˙ψd −kψ1ϵ1 is the
desired value for ˙ψ, and kψ1 > 0 is a controller gain. We obtain
˙Vψ1 = −kψ1∥ϵ1∥2 + ϵ1ϵ2. Defining the second Lyapunov func-
tion candidate as Vψ2 = Vψ1 + 1
2∥ϵ2∥2, we get
˙Vψ2 = ˙Vψ1 + ϵ2˙ϵ2 = −kψ1∥ϵ1∥2 + ϵ1ϵ2 + ϵ2( ¨ψ −˙αψ1)
(27)
where ˙αψ1 = ¨ψd −kψ1( ˙ψ −˙ψd). At this stage, we can imme-
diately assign the value of ¨ψ since it is directly related to ˙ω which
can be considered as the system input. Next, we present the rela-
tion between ¨ψ and ˙ω. Taking time derivative of ˙η = W(η)ω
gives ¨η = ˙W(η)ω + W(η) ˙ω. From the last row of this equation,
we have
¨ψ = n⊤
3 ˙W(η)ω + sφ
cθ
˙ω2 + cφ
cθ
˙ω3.
(28)
Since ˙ω2 and ˙ω3 are not measurable, we replace them by their
desired values using (23):
¨ψ = n⊤
3 ˙W(η)ω + sφ
cθ
˙ωd2 + cφ
cθ
˙ωd3 +
sφ
J22cθ
˜dτ2 +
cφ
J33cθ
˜dτ3
(29)
where ˜dτ = [˜dτ1, ˜dτ2, ˜dτ3]⊤, and Jij is the (i, j)th entry of J. In
order to simplify (29) and without loss of generality, we have
considered the practical case of J diagonal. Now, if we consider
˙ωd3 as
˙ωd3 = cθ
cφ

˙αψ1 −ϵ1 −kψ2ϵ2 −n⊤
3 ˙W(η)ω −sφ
cθ
˙ωd2

(30)
and substitute (30) into (28), we obtain
¨ψ = ˙αψ1 −ϵ1 −kψ2ϵ2 +
sφ
J22cθ
˜dτ2 +
cφ
J33cθ
˜dτ3.
(31)
We observe (30) has singular points at φ = π/2 + kπ, k ∈Z.
Further, from the definition of W(η), θ = π/2 + kπ, k ∈Z
are singular points for the Euler angles. We must therefore
assume (φ, θ) ∈S = {(φ, θ) : −π/2 < φ < π/2, −π/2 < θ <
π/2} when controlling yaw and position. Considering the Lya-
punov function candidate V5 = V4 + Vψ2 and substituting (31)
into (27) results
˙V5 = −k1∥δ1∥2 −k2∥δ2∥2 −k3∥δ3∥2 −k4∥δ4∥2 −kψ1∥ϵ1∥2

## Page 8

2370
A. MOEINI ET AL.
−kψ2∥ϵ2∥2 + ˜d⊤
τ (uJ−1S(n3)⊤R⊤δ4 + Gϵ2)
+ ˜d⊤
f (δ2 + (kdf + k1 + k2)δ3 + kR[I −n3n⊤
3 ]R⊤δ4)
where G = [0,
sφ
J22cθ ,
cφ
J33cθ ]⊤.
Theorem 3.2: Given system (2) with constant disturbances
df and dτ and bounded smooth reference trajectories pd, ψd,
assuming u> 0 and provided (φ, θ) ∈S, the equilibrium
[δ⊤
1 , δ⊤
2 , δ⊤
3 , δ⊤
4 , ϵ1, ϵ2, ˜d⊤
f , ˜d⊤
τ ]⊤= 0 of the closed-loop system
is exponentially stable with dynamic state feedback control
(3), (16), (21), (22), (25) and (30).
Proof: The procedure of the proof is similar to the proof of
Theorem 3.1 except matrices A and B are
A =
⎡
⎢⎢⎢⎢⎢⎢⎣
−k1I3
I3/m
03
03
03×1
03×1
−I3/m
−k2I3
I3
03
03×1
03×1
03
−I3
−k3I3
I3
03×1
03×1
03
03
−I3
−k4I3
03×1
03×1
01×3
01×3
01×3
01×3
−kψ1
1
01×3
01×3
01×3
01×3
−1
−kψ2
⎤
⎥⎥⎥⎥⎥⎥⎦
,
B(t) =
⎡
⎢⎢⎢⎢⎢⎢⎣
03
03
I3
03
(kdf + k1 + k2)I3
03
kR(I −n3n⊤
3 )R⊤
uRS(n3)J−1
01×3
01×3
01×3
G⊤
⎤
⎥⎥⎥⎥⎥⎥⎦
.
■
An important contribution of this work is the decoupled
structure of the control law. The DO design is decoupled from
the state feedback control and this simplifies the controller
expressions and allows for implementation on a commonly used
autopilot such as PX4/Pixhawk. Also, assuming ˜d is an input
the closed-loop tracking error dynamics is linear, and exponen-
tially stability can be readily proven. This should be compared
to the adaptive backstepping control in Cabecinhas et al. (2014)
which achieves asymptotic stability. In fact, most of the men-
tioned existing work in Section 1 only provides asymptotic
stability results, sometimes only for an outer loop subsystem
(Shao et al., 2018) or for approximate models (Dong et al., 2014;
Lee et al., 2016).
4. Experimental validation
Simulation and experimental flight test of the proposed control
law are necessary for validating its performance. This testing
demonstrates if the design can tolerate unmodelled effects such
as measurement noise and input saturation under typical oper-
ating conditions. In this section, we present SITL simulations
and experimental flight testing results.
Table 1. ANCL-Q3 model parameters.
J1
J2
J3
m
ℓ

Ku
Kτ
0.03 kg2
0.03 kg2
0.05 kg2
1.6 kg
0.165 m
1.00 rad
7.75 N
0.8 N m
4.1 Hardware platform
The hardware components of the ANCL quadrotor platform
consist of a quadrotor vehicle ANCL-Q3, a Vicon MCS, and a
QGroundControl ground station (QGC).
4.1.1 The quadrotor vehicle ANCL-Q3
The ANCL-Q3 quadrotor is shown in Figure 2 which con-
sists of a 3D Robotics quadrotor do-it-yourself (DIY) frame in
a cross configuration equipped with a Pixhawk 1 flight con-
troller which has a 180 MHz ARM CPU, two 3D accelerometers,
two 3D gyroscopes, a 3D magnetometer, and a pressure sensor
(Meier et al., 2012). ANCL-Q3 includes a 2.4 GHz LairdTech
transceiver connected to the Pixhawk to receive data from the
MCS. The Pixhawk is also connected to a Spektrum satellite
receiver which is paired to a Spektrum DX8 transmitter. The
DX8 enables manual control and allows the operator to switch
between different control modes. A RN-XV WiFly Module is
used to connect the PX4 to the local network via WiFi. ANCL-
Q3 is powered by a 12 V, 3 cell, 5000 mAh lithium polymer
battery (LiPo). This provides a flight time of about 10 min-
utes. The Pixhawk outputs a PWM signal to Afro 30 A ESCs
which are connected to Turnigy 1100 KV Brushless Outrun-
ner Motors. The diameters of the APC propellers are 11". The
Pixhawk logs data onto its SD card. The mass of the quadro-
tor is 1.6 kg including the battery. The quadrotor is designed
Figure 2. The ANCL-Q3 quadrotor vehicle.
Figure 3. Visualizing the simulated motion control in jMAVSim.

## Page 9

INTERNATIONAL JOURNAL OF CONTROL
2371
such that it hovers at approximately 50% of its maximum
thrust. This ensures enough thrust is available when aggressive
manoeuvres are required. Table 1 lists model parameters in (2)
and (1).
4.1.2 The motion capture system (MCS)
The MCS uses a network of eight Vicon Bonita 3 (B3) cameras,
a Windows PC, and a 2.4 GHz LairdTech transceiver paired to
the one on-board ANCL-Q3. The B3 is a 0.3 MP near infrared
(NIR) camera with maximum frame rate of 240 frames per sec-
ond (fps) and a resolution of 640 × 480. The quadrotor can be
detected by using four 38.1 mm reflective markers mounted on
its frame. The position and yaw of the UAV are estimated by
the MCS which introduces a constant 10 ms delay (Fink, 2018).
Linear velocity is estimated using a low-pass filtered finite dif-
ference of position. The data rate of LairdTech transceiver
is about 100 Hz and includes a constant 15 ms delay (Fink,
2018).
4.1.3 The ground station
The quadrotor communicates to a ground control station run-
ning QGC (Meier, 2017) that is an open-source ground control
Table 2. Root mean square error (RMSE) of the steady-state position tracking error
in the SITL/jMAVSim simulation.
Controller
PX4MC
BS
BSDOBC
RMSE(∥˜p∥) m
0.9583
0.2907
0.0268
Figure 4. Trajectory tracking error, controller inputs, force and torque disturbance estimates for the BSDOBC in the SITL/jMAVSim simulation. (a) Tracking error. (b)
Normalized controller inputs. (b) Force disturbance estimates and (c) Torque disturbance estimates.

## Page 10

2372
A. MOEINI ET AL.
Figure 5. Desired and actual trajectories for the control methods simulated using SITL/jMAVSim. (a) PX4MC. (b) BS and (c) BSDOBC.
software and can be used for flashing the Pixhawk, parame-
ter tuning, data visualisation, status monitoring, and mission
planning. QGC and PX4 are connected through WiFi. The
Figure 6. Norm of trajectory tracking error simulated using SITL/jMAVSim.
MAVLink protocol (Meier, 2015) is used for communication
from the MCS to ANCL-Q3 and between ANCL-Q3 and QGC.
4.2 On-board controller implementation
We implement our proposed control on the PX4 autopi-
lot firmware which is an active and mature open-source
project intended for research and commercial applications
(Meier, 2018). PX4 runs on a number of hardware platforms
and various robot types. It has a modular structure where
individual autopilot functionality (e.g. motion control, state
estimation) is separated into self-contained modules which each
runs as a task on NuttX RTOS platforms (e.g. Pixhawk) or as
a thread within the main PX4 process on POSIX platforms
Table 3. Observer and controller gains used in experiment.
k1
k2
k3
k4
kψ1
kψ2
kdf
14
8.5
1.5
1.5
3.1
1.3
2.7

## Page 11

INTERNATIONAL JOURNAL OF CONTROL
2373
(e.g. SITL). This modular structure has a number of advan-
tages. For example, adding a new control method to the sys-
tem is relatively straightforward as only a small component
of the code with a well-defined interface needs to be modi-
fied. The so-called PX4 middleware supports communication
between the modules, sensor device drivers, and communi-
cation outside PX4. Module communication is implemented
with the micro-object request broker (uORB) which provides
a publish/subscribe bus. Using uORB, publishers send messages
(e.g. a UAV control input) onto a bus instead of sending the mes-
sages directly to specific subscriber modules. Also, subscribers
receive messages as soon as there are updates. PX4 provides
driver modules for the hardware components (e.g. IMU, GPS
and PWM outputs) and libraries for programming (e.g. matrix
computation).
To implement the backstepping DOBC we created a new
module using the v1.5.5 release of PX4. To simplify its
Figure 7. Experimental results: tracking error. (a) PX4MC. (b) BS and (c) BSDOBC.
implementation the module uses a so-called “Block” structure
in the Controller Library contained in px4/src/lib/contro-
llib. This library simplifies the process of subscription and
publication. The library also provides functions for numerical
integration which are used in the disturbance observer (3) and
integration for thrust in (16). The controller module also uses
the PX4 Matrix Library (https://github.com/PX4/Ma
trix) to improve the readability of the control law expressions
given in Section 3. Control gains are implemented using PX4’s
parameter system. This simplifies controller tuning by allow-
ing users to adjust gains from the PXH command line or from
QGC. Roll, pitch and angular velocity are estimated onboard by
an AHRS module attitude_estimator_q which uses the
Pixhawk IMU measurements. Position and linear velocity are
obtained from local_position_estimator which uses
the MCS and IMU data. Further details on the modules used are
in Fink (2018).

## Page 12

2374
A. MOEINI ET AL.
4.3 SITL jMAVSim simulation
Performing a simulation that recreates the actual flight condi-
tions and matches on-board implementation has several advan-
tages when developing motion control algorithms. SITL simu-
lation is a method that allows you to run the actual autopilot
code and investigate its behaviour without any hardware. In
this method, the code is running on a PC and is interfaced
with a simulator that models the vehicle dynamics and the
environment conditions (e.g. wind-gust). Therefore, SITL sim-
ulation can be an important step to the actual flight testing, by
accelerating the debugging process and controller tuning.
In this section, we present SITL simulation results by employ-
ing the PX4 SITL framework and the jMAVSim simulator. SITL
and jMAVSim are built into the PX4 project. The jMAVSim sim-
ulator receives PWM inputs from the autopilot code and outputs
GPS position, IMU and barometer measurements related to the
simulated UAV motion.
jMAVSim is developed in Java and employs java3d
library for visualisation of a 3D virtual flight environment.
Figure 3 shows a screenshot of this visualisation. Communi-
cation between PX4 and jMAVSim is done by the MAVLink
protocol using localhost User Datagram Protocol (UDP). A
PXH shell, similar to NSH shell in the Pixhawk/NuttX platform,
facilitates code debugging and controlling the modules. It can be
used to set the parameters, start and stop the modules and listen
to the PX4 messages.
The UAV’s model parameters can be hardcoded in the
Simulator class. To match the real experiment presented in
Section 4, we chose the model parameters as specified in Table 1
with a cross (or “x”) vehicle configuration. The jMAVSim
simulator accepts normalised torque and thrust inputs from
PX4 and therefore includes thrust saturation. To model the
actuator dynamics, the normalised inputs are low-pass filtered
to generate individual rotor thrust (see class Rotor). The
time constant of the low-pass filter is set to 5 ms. To recre-
ate the actual flight conditions, jMAVSim adds adjustable time
delay to GPS measurements and zero mean Gaussian noise
to the gyro, accelerometer and magnetometer measurements.
The default numbers for these parameters were chosen. The
Figure 8. Experimental results: p1-p2 plot. (a) PX4MC. (b) BS and (c) BSDOBC.

## Page 13

INTERNATIONAL JOURNAL OF CONTROL
2375
thrust constant is scaled such that normalised thrust is 0.51 in
hover.
un = 0.51 + u −mg
60
(32)
This value was obtained from the stock PX4 controller
mc_pos_control when the quadrotor is in hover. The
torque commands τ1, τ2 and τ3 are also normalised by factors
nτ1 = 0.33, nτ2 = 0.33 and nτ3 = 1, respectively.
Environmental disturbances can be easily generated in
jMAVSim. We use this feature to create the force distur-
bance df . The model that generates the force disturbance is
in the AbstractMultiCopter class and the force distur-
bance it outputs is proportional to the airspeed i.e.
df = c · (w −v)
(33)
where c is a drag coefficient whose default value 0.03 Ns/m is
used and w ∈R3 is the wind velocity vector expressed in N. The
wind velocity is a random process whose variance and mean can
be controlled by the user and is obtained from
dw
dt = −w
τ +

W
τ + ν

(34)
where we take W = [0, −20, 0]T m/s as the constant which
determines the mean steady-state value of w, τ = 2 s and
ν = [ν1, ν2, ν3]T ∈R3 where its components are Gaussian
white noise processes with zero mean and variance (τσwk)2,
i.e. N(0, (τσwk)2), where σw1 = 6 m/s, σw2 = 8 m/s, σw3 = 0.
The parameters σwk and W can be set using the GUI or can be
coded in the Simulator class. To investigate the effectiveness
of the proposed method to reject torque disturbances, a sim-
ple model for the torque disturbance is added to the jMAVSim
simulation model using
dτ = −cτ · ω
(35)
where cτ = 0.3 N ms = rad is the drag coefficient.
To evaluate the performance of the controller the reference
trajectory is taken as figure-8 given by pd(t) = [A sin(2πt/T) +
Figure 9. Experimental results: normalised control inputs. (a) PX4MC. (b) BS and (c) BSDOBC.

## Page 14

2376
A. MOEINI ET AL.
1, B sin(4πt/T), −0.85]⊤m, with A = 1.5 and B = 0.75. The
velocity of the trajectory is increased by decreasing T from 20
at t = 0 to 12 in 8 seconds. The setpoint for yaw is zero. In
order to investigate the benefit of the DO, the backstepping dis-
turbance observer-based control (BSDOBC) is compared to the
backstepping controller (BS) and the built-in PX4 position con-
trol (PX4MC). Extensive simulation was performed at different
values for controller gains while monitoring the RMS value of
the tracking error. This testing led to optimal values k1 = k2 =
k3 = k4 = 7. We observed that lower values of gain generally
led to larger RMS error while larger values destabilised the UAV.
After tuning k1 = k2 = k3 = k4 a similar process was used to
find optimal observer gains kdf = 0.5 and kdτ = 0.5. The vehi-
cle is initialised in hover at p(0) = [0.5, 0.5, −1]⊤m. Hence, a
relatively large initial error exists when the controller is switched
on, i.e. ˜p(0) = [0.5, 0.5, −0.15]⊤m.
Simulation results for the BSDOBC are shown in Figure 4.
As can be observed, the tracking error converges to an accept-
able neighbourhood of the origin in approximately 10 s and
remains there. The normalised torques and thrust inputs are in
Figure 4(b). The inputs have reasonable magnitude and remain
unsaturated throughout the simulation. As expected, the thrust
has an average value close to 0.51 N. The disturbance estimates
are shown in Figure 4(c,d). We observe ˆdf1 has a steady-state
average value of approximately −0.1 N and contains oscilla-
tions at the frequency of the reference trajectory. The steady-
state average value of ˆdf2 is about −4 N which is consistent
with the applied wind disturbance in the −n2 direction. The
steady-state average value of ˆdf3 is almost 0.3 N which is due
to modelling error. We observe the estimate for the torque dis-
turbance is almost zero. This is consistent with the disturbance
Figure 10. Experimental results: disturbance estimates.
model (35) and the small angular velocity of the quadrotor along
the figure-8 trajectory.
The simulation results for the actual and desired trajectories
are shown in 2D for all controllers in Figure 5. Table 2 pro-
vides the root mean square of the position error (RMSE) in
steady-state. The trajectory of the norm of the tracking error
is in Figure 6. We observe from Table 2 that the BSDOBC
control achieves the lowest RMSE values. The 2D plots clearly
reflect this reduced error and the effectiveness of the distur-
bance observer in improving the tracking performance. The
code which reproduces this simulation is available online for
public use (Moeini & Lynch, 2020).
4.4 Physical experiment
In this section, we investigate the performance of the pro-
posed controller implemented on the ANCL quadrotor plat-
form. External disturbances are created with a fan which was
placed at a height of about 0.85 m (relative to the fan’s cen-
tre) and 3 m away from the UAV’s initial position. The fan
has a blade diameter of about 0.6 m and it produces an air-
flow of about 1.6 m/s in the direction of the n1 axis. We remark
that the airflow due to the fan will alter the thrust generation
of the vehicle, and this change in aerodynamics is difficult to
model. As in the simulation, the reference trajectory is a figure-8
given by pd(t) = [A sin(2πt/T) + 1, B sin(4πt/T), −0.8]⊤m,
with A = 0.7 and B = 0.3. The velocity of the trajectory is
increased as a function of time by decreasing T from 20 to 12
in 8 seconds. The setpoint for yaw is zero. As in the simulation,
the BSDOBC is compared with BS and PX4MC controllers.
The experiment consists of flying close to the starting point
of the reference trajectory manually. Then the controller is
switched to setpoint regulation mode (using the stock PX4 con-
trol) with setpoint pd(0) = [1, 0, −0.8] m. Next, one of the three
trajectory tracking controllers is enabled and the fan turned on.
The controller gains for the BSDOBC are in Table 3. In order
to tune the controller gains, the lateral position subsystem was
considered initially. We began with small values of k1, k2, k3, k4
and the remaining 2 DoF (i.e. yaw and altitude) controlled by
the stock PX4 motion controller. The RMS value of the steady-
state tracking error was observed as k1, k2, k3, k4 and torque
normalisation parameters nτ1, nτ2 and nτ3 were systematically
varied. A similar procedure was applied to tune the other 2 DoF
which are affected by kψ1, kψ2 and the thrust normalisation
(32).
The resulting tracking errors, p1-p2 plot, control inputs and
disturbance estimates are shown in Figures 7–10, respectively.
As can be observed from Figures 7 and 8, the BSDOBC pro-
vides better performance in the steady state compared with the
BS and PX4MC controllers. We observe an offset about 20 cm
in the n1 direction for the tracking error of the BS controller.
This offset is due to the applied force disturbance from the
Table 4. Experimental results: mean and RMSE of position tracking error.
Controller
˜p1(mean)
˜p2(mean)
˜p3(mean)
˜p1(RMSE)
˜p2(RMSE)
˜p3(RMSE)
∥˜p∥(RMSE)
PX4MC (m)
−0.0193
0.0037
−0.0337
0.2598
0.2036
0.0467
0.2810
BS (m)
0.1509
−0.0312
−0.0089
0.1796
0.0497
0.0475
0.1501
BSDOBC (m)
0.0433
−0.0101
−0.0010
0.0952
0.0380
0.0346
0.0668

## Page 15

INTERNATIONAL JOURNAL OF CONTROL
2377
Figure 11. Experimental setup.
fan and since the BS control has no disturbance compensa-
tion. The force disturbance estimate is shown in Figure 10. The
average steady-state value of ˆdf1 is about 0.5 N. From Figure 9,
we observe the torques are noisy which is mainly due to the
noise in angular velocity measurements. The steady-state aver-
age value and RMSE of the tracking error for the three methods
are shown in Table 4. We observe the BSDOBC achieves better
performance which is to be expected as it estimates and com-
pensates for the disturbance force. Figure 11 shows a picture of
the experimental setup. A video of the experiment is provided
at https://youtu.be/-90w_FPmNWE.
5. Conclusion
This paper has proposed a nonlinear position and yaw track-
ing control which combines backstepping with a DO to increase
its robustness to external force disturbances. The DO error
dynamics is decoupled from the tracking error dynamics and
the cascade structure of the closed-loop makes the stability anal-
ysis, implementation, and tuning straightforward. Exponential
stability is proven for the constant disturbance case. The method
is validated in SITL simulation and flight experiment using
the commonly used PX4 autopilot firmware. The BSDOBC is
compared with a stock PX4 inner-outer loop control and a
traditional backstepping method. The BSDOBC demonstrates
improved tracking performance and robustness relative to these
controllers.
Disclosure statement
No potential conflict of interest was reported by the authors.
Funding
This work was supported by the Autonomous Systems Initiative Major
Innovation Fund, Alberta Ministry of Jobs, Economy and Innovation [grant
number RCP-19-001-MIF].
References
Antonelli, G., Cataldi, E., Arrichiello, F., Giordano, P. R., Chiaverini,
S., & Franchi, A. (2018). Adaptive trajectory tracking for quadro-
tor MAVs in presence of parameter uncertainties and external dis-
turbances. IEEE Transactions on Control Systems Technology, 26(1),
248–254. https://doi.org/10.1109/TCST.2017.2650679
Bouabdallah, S. (2007). Design and control of quadrotors with application to
autonomous flying [Ph.D. dissertation]. École Polytechnique Fédérale,
Lausanne, Switzerland.
Cabecinhas, D., Cunha, R., & Silvestre, C. (2014). A nonlinear quadro-
tor trajectory tracking controller with disturbance rejection. Control
Engineering Practice, 26, 1–10. https://doi.org/10.1016/j.conengprac.2013.
12.017
Cabecinhas, D., Cunha, R., & Silvestre, C. (2015). A globally stabilizing
path following controller for rotorcraft with wind disturbance rejec-
tion. IEEE Transactions on Control Systems Technology, 23(2), 708–714.
https://doi.org/10.1109/TCST.2014.2326820
Castillo, P., Lozano, R., & Dzul, A. (2005). Modelling and control of mini
flying machines. Springer-Verlag.
Dong, W., Gu, G.-Y., Zhu, X., & Ding, H. (2014). High-performance trajec-
tory tracking control of a quadrotor with disturbance observer. Sensors
and Actuators A, 211, 67–77. https://doi.org/10.1016/j.sna.2014.03.011
Faessler, M., Franchi, A., & Scaramuzza, D. (2018). Differential flatness of
quadrotor dynamics subject to rotor drag for accurate tracking of high-
speed trajectories. IEEE Robotics and Automation Letters, 3(2), 620–626.
https://doi.org/10.1109/LRA.2017.2776353
Fink, G. (2018). Computer vision-based motion control and state estima-
tion for unmanned aerial vehicles (UAVs) [Ph.D. dissertation], Dept. of
Electrical and Computer Engineering, University of Alberta, Edmonton,
AB.
Goodarzi, F. A., Lee, D., & Lee, T. (2015). Geometric adaptive track-
ing control of a quadrotor unmanned aerial vehicle on SE(3) for agile
maneuvers. Transactions of the ASME, Journal of Dynamic Systems, Mea-
surement and Control, 137(9), 091007:1–12. https://doi.org/10.1115/1.
4030419
He, Y., Pei, H., & Sun, T. (2014). Robust tracking control of helicopters
using backstepping with disturbance observers. Asian Journal of Control,
16(5), 1387–1402. https://doi.org/10.1002/asjc.v16.5
Hua, M.-D., Hamel, T., Morin, P., & Samson, C. (2013). Introduction to
feedback control of underactuated VTOL vehicles: A review of basic
control design ideas and principles. IEEE Control Systems Magazine,
33(1), 61–75. https://doi.org/10.1109/MCS.2012.2225931
Kendoul, F. (2012). Survey of advances in guidance, navigation, and con-
trol of unmanned rotorcraft systems. Journal of Field Robotics, 29(2),
315–378. https://doi.org/10.1002/rob.20414
Koo, T. J., & Sastry, S. (1998). Output tracking control design of a heli-
copter model based on approximate linearization. Proceedings of IEEE
conference on Decision and Control, Tampa, FL (pp. 3635–3640).
Lee, S. J., Kim, S., Johansson, K. H., & Kim, H. J. (2016). Robust acceler-
ation control of a hexarotor UAV with a disturbance observer. Proceed-
ings of IEEE conference on Decision and Control, Las Vegas, NV (pp.
4166–4171).
Liu, C., Pan, J., & Chang, Y. (2016). PID and LQR trajectory tracking
control for an unmanned quadrotor helicopter: Experimental studies. Pro-
ceedings of 35th Chinese Control Conference, Chengdu, China (pp.
10845–10850).
Madani, T., & Benallegue, A. (2006). Backstepping sliding mode control
applied to a miniature quadrotor flying robot. Proceedings of IECON
2006 – 32nd Annual Conference in IEEE Industrial Electronics, Paris,
France (pp. 700–705).
Marino, R., & Tomei, P. (1995). Adaptive observers with arbitrary expo-
nential rate of convergence for nonlinear systems. IEEE Transactions
on Automatic Control, 40(7), 1300–1304. https://doi.org/10.1109/9.400
471
Martin, P., & Salaün, E. (2010). Design and implementation of a low-cost
observer-based attitude and heading reference system. Control Engi-
neering Practice, 18(7), 712–722. https://doi.org/10.1016/j.conengprac.
2010.01.012
Meier, L. (2015). Mavlink: Micro air vehicle communication protocol.
[Online]. https://mavlink.io/en/
Meier, L. (2017). QGroundControl. Institute for Visual Computing, Swiss
Federal Institute of Technology Zurich. [Online]. Retrieved January 1,
2018, from http://www.qgroundcontrol.org/
Meier, L. (2018). PX4 autopilot. Institute for visual computing, Swiss Federal
Institute of Technology Zurich. [Online]. https://px4.io/
Meier, L., Tanskanen, P., Heng, L., Lee, G., Fraundorfer, F., & Pollefeys, M.
(2012). Pixhawk: A micro aerial vehicle design for autonomous flight

## Page 16

2378
A. MOEINI ET AL.
using onboard computer vision. Autonomous Robots, 33(1–2), 21–39.
https://doi.org/10.1007/s10514-012-9281-4
Mellinger, D., & Kumar, V. (2011). Minimum snap trajectory generation and
control for quadrotors. Proceedings on IEEE international conference on
Robotics and Automation, Shanghai, China (pp. 2520–2525).
Moeini, A., & Lynch, A. (2020). Modified px4 autopilot firmware. [Online].
https://github.com/ANCL/UAV_DOBBS
Moeini, A., Lynch, A., & Zhao, Q. (2019). Disturbance observer based non-
linear control of a quadrotor UAV. Advanced Control for Applications,
2(1), 1–20. https://doi.org/10.1002/adc2.24
Nonami, K., Kendoul, F., Suzuki, S., Wang, W., & Nakazawa, D. (2010).
Autonomous control of a mini quadrotor vehicle using LQG controllers.
In Autonomous flying robots (pp. 61–76). Springer Japan. [Online].
https://doi.org/10.1007/978-4-431-53856-1_3
Omari, S., Hua, M.-D., Ducard, G., & Hamel, T. (2013). Nonlinear control of
VTOL UAVs incorporating flapping dynamics. Proceedings of IEEE inter-
national conference on Intelligent Robots and Systems, Tokyo, Japan (pp.
2419–2425).
Poultney,
A.,
Gong,
P.,
&
Ashrafiuon,
H.
(2019).
Integral
backstepping control for trajectory and yaw motion tracking of
quadrotors.Robotica, 37(2), 300–320. https://doi.org/10.1017/S02635747
18001029
Poultney, A., Kennedy, C. R., Clayton, G. M., & Ashrafiuon, H. (2018).
Robust tracking control of quadrotors based on differential flatness:
Simulations and experiments. IEEE/ASME Transactions on Mecha-
tronics, 23(3), 1126–1137. https://doi.org/10.1109/TMECH.2018.2820
426
Reinoso, M. J., Minchala, L. I., Ortiz, P., Astudillo, D. F., & Ver-
dugo, D. (2016). Trajectory tracking of a quadrotor using sliding
mode control. IEEE Latin America Transactions, 14(5), 2157–2166.
https://doi.org/10.1109/TLA.2016.7530409
Shao, X., Liu, J., Cao, H., Shen, C., & Wang, H. (2018). Robust dynamic
surface trajectory tracking control for a quadrotor UAV via extended
state observer. International Journal of Robust and Nonlinear Control, 28,
2700–2719. https://doi.org/10.1002/rnc.v28.7
Sumantri, B., Uchiyama, N., Sano, S., & Kawabata, Y. (2013). Robust track-
ing control of a quad-rotor helicopter utilizing sliding mode control
with
a
nonlinear
sliding
surface.
Journal
of
System
Design
and
Dynamics,
7(2),
226–241.
https://doi.org/10.1299/jsdd.7.
226
