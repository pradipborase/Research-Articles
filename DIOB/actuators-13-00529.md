# actuators-13-00529.pdf

## Page 1

Citation: Mousavi, R.; Mousavi, A.;
Mousavi, Y.; Tavasoli, M.; Arab, A.;
Kucukdemiral, I.B.; Fekih, A.
Observer-Based Adaptive Neural
Control of Quadrotor Unmanned
Aerial Vehicles Subject to Model
Uncertainties and External
Disturbances. Actuators 2024, 13, 529.
https://doi.org/10.3390/act13120529
Academic Editor: Liang Sun
Received: 27 November 2024
Revised: 19 December 2024
Accepted: 20 December 2024
Published: 21 December 2024
Copyright: © 2024 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed
under
the
terms
and
conditions of the Creative Commons
Attribution (CC BY) license (https://
creativecommons.org/licenses/by/
4.0/).
Article
Observer-Based Adaptive Neural Control of Quadrotor
Unmanned Aerial Vehicles Subject to Model Uncertainties and
External Disturbances
Rashin Mousavi 1,†, Arash Mousavi 1,†, Yashar Mousavi 2,*
, Mahsa Tavasoli 3
, Aliasghar Arab 4
,
Ibrahim Beklan Kucukdemiral 2
and Afef Fekih 5
1
Department of Electrical Engineering and Applied Sciences, Paradise Research Center, Jahrom 7416813647,
Iran; rashinmousavi66@gmail.com (R.M.); arash.mousavi@ieee.org (A.M.)
2
Department of Applied Science, School of Computing, Engineering and Built Environment, Glasgow
Caledonian University, Glasgow G4 0BA, UK; ibrahim.kucukdemiral@gcu.ac.uk
3
Department of Applied Science & Technology, North Carolina A&T State University,
Greensboro, NC 27411, USA; mtavasoli@aggies.ncat.edu
4
Department of Mechanical and Aerospace Engineering, New York University, New York, NY 10012, USA;
aliasghar.arab@nyu.edu
5
Electrical and Computer Engineering Department, University of Louisiana at Lafayette, P.O. Box 43890,
Lafayette, LA 70504, USA; afef.fekih@louisiana.edu
*
Correspondence: seyedyashar.mousavi@gcu.ac.uk
†
These authors contributed equally to this work.
Abstract: Quadrotor unmanned aerial vehicles (QUAVs) are widely recognized for their versatility
and advantages across diverse applications. However, their inherent instability and underactuated
dynamics pose significant challenges, particularly under external disturbances and parametric model
uncertainties. This paper presents an advanced observer-based control framework to address these
challenges, introducing a high-gain disturbance observer (HGDO) integrated with a neural-network-
based adaptive fractional sliding mode control (NN-AFSMC) scheme. The proposed HGDO-NN-
AFSMC ensures robust position and attitude tracking by effectively compensating for external
disturbances and model uncertainties. A direct control approach is employed, significantly reducing
computational complexity by minimizing the need for frequent online parameter updates while
maintaining high tracking precision and robustness. The stability of the control system is rigorously
analyzed using Lyapunov theory, and comprehensive simulation studies validate the proposed
scheme’s superior performance compared to other advanced control approaches, particularly in
dynamic and uncertain operational environments. The proposed HGDO-NN-AFSMC achieves
a position tracking error of less than 0.03 m and an attitude tracking error below 0.02 radians,
even under external disturbances and parametric uncertainties of 20%. Compared to conventional
robust feedback linearization (RFBL) and nonsingular fast terminal sliding mode control (NFTSMC),
the proposed method improves position tracking accuracy by 25% and reduces settling time by
approximately 18%.
Keywords: quadrotor UAV control; adaptive control; high-gain disturbance observer; neural-network-
based control; external disturbance; model uncertainty
1. Introduction
In recent years, quadrotor unmanned aerial vehicles (QUAVs) have garnered consider-
able attention from the engineering community due to their wide range of applications in
both military and civilian sectors, including product delivery, emergency rescue missions,
infrastructure inspection, surveillance, aerial photography, and mapping. The versatility
of these applications relies on the QUAV’s ability to hover stably, maneuver precisely,
and maintain operational safety [1–3]. The key advantages of QUAVs include vertical
Actuators 2024, 13, 529. https://doi.org/10.3390/act13120529
https://www.mdpi.com/journal/actuators

## Page 2

Actuators 2024, 13, 529
2 of 23
take-off and landing capabilities, cost-effectiveness, simple manufacturing processes, and
agile flight dynamics. In micro air vehicles (MAVs), a related category of aerial systems,
significant advancements have also been achieved in their design and operation. MAVs,
widely used for surveillance, environmental monitoring, and confined-space operations,
rely on low Reynolds number aerodynamics characterized by unsteady phenomena such
as vortex generation and wake interactions [4,5]. Biomimetic designs inspired by natu-
ral flyers, like cicadas, have further optimized MAV efficiency, leveraging flapping-wing
mechanisms to improve lift and thrust [4]. These developments in MAV aerodynamics
have served as inspirations for enhancing the adaptability and performance of other aerial
systems. However, despite these benefits, the development of advanced control systems
for QUAVs remains challenging due to their underactuated and coupled dynamics, as
well as their sensitivity to external disturbances and model uncertainties [6]. Effective
control technologies must, therefore, ensure that QUAVs can operate safely and efficiently,
meeting the high standards for responsiveness and sustainability required by Industry 4.0.
Addressing external disturbances and compensating for model uncertainties are essential
to enhance QUAV stability and precision in real-world conditions. Without these robust
mechanisms, QUAVs can be unstable, limiting their reliability in critical applications. As
a result, studying advanced control methods focused on disturbance rejection and uncer-
tainty compensation is vital for achieving consistent and reliable performance across a wide
range of mission-critical scenarios.
The highly intricate and nonlinear nature of QUAV dynamics presents significant
challenges in developing control systems that can effectively manage their operational
complexities [7–9]. Existing control approaches, both linear and nonlinear, often depend on
precise model parameters, which are challenging to measure accurately in practical settings,
thereby complicating their deployment. Adaptive control methods, while designed to
mitigate parameter uncertainties and respond to external disturbances, still face limitations
in fully capturing the multifaceted dynamics of quadrotors [10]. Additionally, the inherent
underactuation of quadrotors adds to these challenges, as it complicates precise position
and attitude control, which are essential for stable and efficient operation. This need for
adaptable and robust control methods for accurate tracking under uncertain conditions
has driven considerable research interest in this area [11–15]. Addressing various issues
such as sensor noise, model inaccuracies, unmodeled dynamics, and a range of external
disturbances remains essential for effective control design [16–18]. A systematic analysis
of different control techniques, including their strengths and limitations, is crucial in
identifying the most efficient strategies for handling the uncertainties that affect QUAV
performance. In this context, several studies offer innovative control strategies that handle
model uncertainties and external disturbances effectively. For example, in [19], a geometric
adaptive robust hierarchical control method was designed for underactuated quadrotors,
minimizing the effects of nonlinearities, uncertainties, and dynamic coupling. Similarly,
the authors in [20] proposed two adaptive robust control strategies—bounded adaptive
control and asymptotic adaptive control—that stabilize the attitude of quadrotors even
amid uncertain parameters, control input limitations, and external disturbances. These
strategies ensure asymptotic stability by estimating key physical parameters, managing
input saturation, and suppressing external disturbances. Additionally, [21] presented an
approach for robust adaptive tracking control in quadrotors by combining a self-tuning
regulator in the inner loop with a proportional–integral (PI) controller in the outer loop,
resulting in improved robustness and tracking performance compared to the reference
adaptive control model. Furthermore, in [16], a backstepping-based adaptive control
framework was introduced to address parameter uncertainties, external disturbances, and
sensor noise in QUAVs. This method avoids issues related to trigonometric singularities
in Euler angles, maintains bounded estimation and tracking errors, and shows superior
performance compared to proportional–integral–derivative (PID), standard backstepping,
and geometric control approaches.

## Page 3

Actuators 2024, 13, 529
3 of 23
Advanced control methods, including neural network (NN)-based approaches and
adaptive sliding mode control (SMC), have seen increased use to enhance the tracking
precision of QUAVs [22–25]. The operational stability of quadrotors, however, is frequently
compromised by external disturbances and inherent model uncertainties, which can lead
to instability or even catastrophic failure in critical situations. This has driven extensive
research into reliable control strategies that ensure QUAVs maintain stable performance
and accurate tracking despite these external disturbances. For instance, in [26], a nonlinear
observer-based SMC approach was developed specifically for QUAV control, with the
nonlinear observer bolstering the robustness of the SMC to maintain effective trajectory
tracking. In another study [27], an adaptive control scheme was developed that integrates
a fast terminal SMC with NN capabilities to counteract external disturbances and model
uncertainties. The scheme leverages NN for approximating unknown system dynamics
and adaptive laws for estimating disturbance bounds, while fast terminal SMC acceler-
ates convergence. Similarly, a nonsingular terminal SMC approach enhanced with state
feedback and a disturbance observer (DO) was introduced for QUAV attitude control, effec-
tively addressing external disturbances [28]. In [13], an adaptive fast-reaching nonsingular
terminal SMC was designed for QUAVs to achieve rapid error convergence even in the face
of model uncertainties and disturbances, outperforming traditional adaptive SMC in track-
ing accuracy and robustness. Further, a finite-time tracking control approach combined
an NN-based control scheme with adaptive tuning for NN parameters and an auxiliary
system to handle input saturation challenges, effectively addressing external disturbances
and parametric uncertainties [29]. Another method, described in [30], uses learning-based
robust tracking control that integrates a NN with an enhanced weight updating mechanism
to handle time-varying and coupling uncertainties. This approach provides stable and accu-
rate position and attitude tracking, demonstrating superior performance over conventional
adaptive dynamic programming (ADP) and linear quadratic regulator (LQR) methods
under varying disturbance conditions. Despite these advancements, several significant
challenges persist within the literature. Many existing studies either simplified the complex
dynamics of QUAVs or failed to address the full range of uncertainties encountered in real-
world operations. Additionally, conventional methods often have a high computational
overhead, which can restrict their use in real-time applications. These limitations under-
score the pressing need for more robust, computationally efficient control strategies capable
of managing the unpredictable and complex nature of QUAV operations effectively.
DO-based control has demonstrated efficacy in improving quadrotor trajectory track-
ing. However, many existing DOs are characterized by complex structures that increase the
computational load on flight controllers [14,31–35]. While advancements in flight controller
processing power have been significant, the high computational requirements associated
with autonomous or semiautonomous flight operations—coupled with the inherent weight
and power limitations of quadrotors—continue to constrain the available computing re-
sources. Consequently, there is an ongoing demand for DOs that are both simple and
computationally efficient. Additionally, these complex DOs often come with numerous
tuning parameters, necessitating an intensive calibration process to achieve a rapid conver-
gence rate [36–39]. Among the nonlinear observers, high-gain observers (HGOs) stand out
for their simplicity and speed. HGOs utilize high gain to obtain state estimates, rapidly
offering several beneficial attributes. First, their design and implementation are relatively
straightforward, as they replicate the system model with a specific gain, the calculation
of which is explicit. Second, HGOs are easy to tune through a single scalar design pa-
rameter, simplifying the tuning process. Lastly, they deliver global or semiglobal stability
for a wide range of systems [40–42]. These advantageous features, however, come with a
trade-off: conventional HGOs are susceptible to amplifying measurement noise, although
recent designs have mitigated this issue. Building on the strengths of HGOs, their use
in disturbance estimation has led to the development of high-gain disturbance observers
(HGDOs) [43,44]. Despite their potential, HGDOs remain underexplored for quadrotor

## Page 4

Actuators 2024, 13, 529
4 of 23
applications, particularly in real-world scenarios where measurement errors and external
disturbances are prevalent.
Despite the advances in observer-based estimation, adaptive estimation, and neural
network (NN)-based adaptive control for QUAVs, challenges persist in achieving robust
performance without compromising design targets or imposing high computational de-
mands on the system [45–47]. It remains critical to evaluate these methods systematically
to identify their limitations and areas where further refinement is needed to address the
complex control needs of QUAVs in practical applications. This study was driven by the
goal of developing a more resilient and adaptive control strategy capable of handling
the varied challenges QUAVs encounter in real-world environments. In response to the
identified limitations of the existing approaches, this paper proposes an HGDO combined
with an adaptive NN-based control strategy to estimate external disturbances and tackle
modeling uncertainties efficiently while keeping computational overhead minimal. The
primary contribution of this work lies in its adaptive control scheme, which was designed
to maintain reliable system performance even under the influence of significant external
disturbances. By leveraging NN-based approximations within the control framework, this
approach achieves precise trajectory tracking across a wide range of operational conditions.
The proposed methodology includes a nested NN-based adaptive sliding mode control
(NN-AFSMC) strategy for controlling QUAVs. The control design prioritizes accurate posi-
tion and attitude tracking and incorporates a direct approach that reduces computational
complexity, enhancing robustness by limiting online parameter updates. This novel control
scheme ensures that the quadrotor can execute tasks with high precision and reliability,
making it adaptable to complex operational environments. Moreover, a key innovation of
this method is the indirect integration of NNs within the adaptive SMC framework, which
reduces the computational demands associated with real-time implementation. Unlike
traditional direct NN-based methods that require the extensive online updating of NN
parameters, the proposed approach simplifies the adaptation process by focusing on scalar
virtual parameters instead of full vector updates. This design choice not only streamlines
the control implementation but also strengthens system robustness, making it well suited
for applications that demand high stability and adaptability in the presence of external
disturbances. The contributions of this work to the current literature are summarized
as follows:
•
A comprehensive dynamic model of a QUAV is developed, addressing the limitations
of previous studies that often relied on oversimplified models and neglected the
intricate coupling between attitude and position dynamics.
•
A novel integration of a high-gain disturbance observer (HGDO) and NN approxima-
tion capabilities with adaptive sliding mode control (AFSMC) is formulated to handle
external disturbances and model uncertainties effectively. This approach retains the
complexity of aerodynamic drag and other nonlinear effects, enhancing the control
system’s adaptability to realistic operational conditions.
•
The proposed method introduces a virtual parameter concept, enabling the indirect
use of neural networks, which substantially minimizes the need for frequent parameter
updates. This results in a control approach that is not only computationally efficient
but also structurally straightforward and cost-effective, ensuring the precise tracking
of position and attitude.
•
The robustness and disturbance tolerance of the proposed control strategy are val-
idated against robust feedback linearization and nonsingular fast terminal sliding
mode control approaches. Extensive simulations demonstrate the effectiveness of the
approach under a variety of challenging conditions, underscoring its reliability and
applicability in dynamic environments.
The remainder of this paper is structured as follows: Section 2 describes the problem
statement by defining the QUAV model. Section 3 presents the developed high-gain
disturbance observer. The proposed NN-AFSMC control scheme is investigated in Section 4,

## Page 5

Actuators 2024, 13, 529
5 of 23
and the simulation results and respective discussions are provided in Section 4. Finally,
Section 6 concludes this paper.
2. Detailed QUAV Model
This section presents the dynamic model of a QUAV used for delivery operations.
The quadrotor, depicted in Figure 1, features four rotors, with rotors 1 and 3 rotating
counterclockwise and rotors 2 and 4 rotating clockwise, whose specifications are illustrated
in Table 1. These rotations generate control forces and moments, enabling flight maneuver-
ability. The quadrotor dynamics are described using two coordinate systems: the inertial
frame E = {xe, ye, ze}, which represents the global reference, and the body-fixed frame
B = {xb, yb, zb}, attached to the vehicle. Assuming the quadrotor operates as a rigid body,
the Newton–Euler equations are used to describe its motion.
F1
F3
F2
F4
Rotor 1
Rotor 2
Rotor 3
Rotor 4
𝜼
𝝆
𝝌
𝒙𝒃
𝒚𝒃
𝒛𝒃
Figure 1. The configuration of a delivery quadrotor UAV.
The quadrotor’s position in the inertial frame is denoted as ω = [x, y, z]T ∈R3, and its
orientation relative to the inertial frame is represented by Euler angles ν = [ρ, χ, η]T ∈R3.
Concentrating on position control, the quadrotor’s dynamics can be mathematically ex-
pressed as follows [16]:
¨x = (cos ρ sin χ cos η + sin ρ sin η) Tat
m −Φx ˙x
m ,
¨y = (cos ρ sin χ sin η −sin ρ cos η) Tat
m −Φy ˙y
m ,
¨z = (cos ρ cos χ) Tat
m −g −Φz ˙z
m ,
¨ρ = ˙χ ˙η Iy −Iz
Ix
−˙χ ¯Θ Ir
Ix
−˙ρΦρ
Ix
+ τaρ
Ix
,
¨χ = ˙ρ ˙η Iz −Ix
Iy
−˙ρ ¯Θ Ir
Iy
−˙χΦχ
Iy
+ τaχ
Iy
,
¨η = ˙ρ ˙χ Ix −Iy
Iz
−˙ηΦη
Iz
+ τaη
Iz
.
(1)
where m represents the mass of the quadrotor, g is the gravitational acceleration, and
I = [Ix, Iy, Iz] are the moments of inertia. Aerodynamic damping effects are characterized
by Φx, Φy, and Φz. The parameter Ir denotes the rotor inertia, and ¯Θ = Θ4 + Θ3 −Θ2 −Θ1
captures the net angular momentum contribution from the rotors. The control thrust Tat
and torques τaρ, τaχ, and τaη are expressed as

## Page 6

Actuators 2024, 13, 529
6 of 23
Tat = k(Θ2
1 + Θ2
2 + Θ2
3 + Θ2
4),
(2)
τaρ = kl(Θ2
3 −Θ2
1),
(3)
τaχ = kl(Θ2
4 −Θ2
2),
(4)
τaη = b(Θ2
2 −Θ2
1 + Θ2
4 −Θ2
3),
(5)
where k is the thrust coefficient, b is the drag coefficient, and l is the distance from the rotor
axis to the quadrotor’s center of mass.
Table 1. Technical specifications of quadrotor blades and system.
Specification
Details
Unit
Chord length
0.254
m
Twist angle
−24 to 24
◦C
Airfoil type
Wortmann FX63-137
–
Rotor diameter
0.3
m
Blade number
2
per rotor
Blade material
Carbon fiber
Tip speed
80–100
m/s
Mechanism
Fixed pitch
–
Motor type
Brushless DC motors
–
Battery
11.1 Li-Po
V
Maximum payload
1
kg
Flight time
20–25
min
Weight
1.5–2
kg (including battery and payload)
Remark 1. To ensure numerical stability and avoid singularities in the control model, the roll (ρ)
and pitch (χ) angles are constrained to the interval (−π
2 , π
2 ). This restriction eliminates issues at
singular configurations such as χ = ± π
2 or ρ = ± π
2 .
To design an effective control system for the QUAV, let the inputs from the rotors be de-
fined as u1 = Tat, u2 = τaρ, u3 = τaη, and u4 = τaχ. Based on the dynamic equations in (1),
while accounting for the effects of external disturbances, δa(·) = [δx(·), δy(·), δz(·)]T ∈R3
and δb(·) = [δρ(·), δχ(·), δη(·)]T ∈R3, the translational dynamics ˙ω and rotational dynam-
ics ˙p can be reformulated as follows:
¨ω = Autr(t) + ϖ1(·) + δa(ω, t),
(6)
¨p = Bur(t) + ϖ2(·) + δb(p, t),
(7)
where ur = [u2, u3, u4]T and utr = [Ux, Uy, Uz]T. Here, Ux, Uy, and Uz are the virtual
control inputs for longitudinal, lateral, and altitude motion, respectively, defined as
Ux = (cos ρ sin χ cos η + sin ρ sin η)u1,
Uy = (cos ρ sin χ sin η −sin ρ cos η)u1,
Uz = (cos ρ cos χ)u1.
(8)
The matrices A = ζ12I3×3 and B = [ζ13
ζ14
ζ15]TI3×3, along with the terms ϖ1(·)
and ϖ2(·), are given by
ϖ1(·) =


−ζ1 ˙x
−ζ2 ˙y
−ζ3 ˙z −g

,
ϖ2(·) =


ζ4 ˙χ ˙η −ζ9 ˙χ ¯Θ −ζ6 ˙ρ
ζ7 ˙ρ ˙η −ζ8 ˙ρ ¯Θ −ζ5 ˙χ
ζ10 ˙ρ ˙χ −ζ11 ˙η

.

## Page 7

Actuators 2024, 13, 529
7 of 23
The parameters ζi (i = 1, . . . , 15) are defined as
ζ1 = Φx
m ,
ζ2 = Φy
m ,
ζ3 = Φz
m ,
ζ4 = Iy −Iz
Ix
,
ζ5 = Φχ
Iy
,
ζ6 = Φρ
Ix
,
ζ7 = Iz −Ix
Iy
,
ζ8 = Ir
Iy
,
ζ9 = Ir
Ix
,
ζ10 = Ix −Iy
Iz
,
ζ11 = Φη
Iz
,
ζ12 = 1
m,
ζ13 = 1
Ix
,
ζ14 = 1
Iy
,
ζ15 = 1
Iz
.
The system consists of four motor-propeller actuators, each potentially influenced by
unmeasurable factors. These factors can cause the actual actuator input, uai, to differ from
the intended input, ui. This relationship is expressed as
uai = ui + ψi(t),
(9)
where ψi(t) represents the unmeasurable, time-varying component of the control input,
constrained within certain bounds. From this point forward, time dependence is omitted
for simplicity.
By incorporating the actuator uncertainties from (9) into the dynamics of (6) and (7),
the revised equations become
¨ω = Autr + AKΘψ1 + ϖ1(·) + δa(ω, t),
(10)
¨p = Bur + Bψr + ϖ2(·) + δb(p, t),
(11)
where ψr = [ψ2, ψ3, ψ4]T, and KΘ is a control matrix capturing the influence of the
rotor angles:
KΘ =


cos ρ sin χ cos η + sin ρ sin η
cos ρ sin χ sin η −sin ρ cos η
cos ρ cos χ

.
Remark 2. The quadrotor is an underactuated system, characterized by six degrees of freedom
(x, y, z, ρ, χ, η) and four control inputs (u1, u2, u3, u4). By substituting the actual input u1 with
virtual control inputs Ux, Uy, and Uz, a control strategy can be devised in a manner analogous to
that use for conventional systems.
This work focused on developing an adaptive control strategy to address modeling
uncertainties and external disturbances. The objective was to ensure that the system outputs
[x, y, z, η] closely track the desired reference trajectories [xd, yd, zd, ηd]T. The following
assumptions form the basis for the proposed control framework:
Assumption 1. The parameters ζ1, ζ2, . . . , ζ15 are unknown but lie within bounded ranges. Addi-
tionally, ψi, representing unmeasurable and time-varying actuator uncertainties, is bounded and
can change rapidly. Specifically, there exists an unknown scalar ¯ψ such that |ψi| ≤¯ψ < ∞.
Assumption 2. The desired position and orientation trajectories, denoted as ωd, pd, ˙ωd, ˙pd, ¨ωd, ¨pd,
are bounded. Moreover, the states of the system are assumed to be fully measurable and accessible
for the control design.
Assumption 3. External disturbances, represented as δa and δb, are bounded such that ∥δa∥≤¯δ1
and ∥δb∥≤¯δ2, where ¯δ1 and ¯δ2 are unknown constants. The norm ∥· ∥refers to the L1 norm,
defined as ∥χ∥= R t
0 |χ(α)| dα.
Remark 3. Accurately identifying system parameters is often infeasible due to the complexities of
real-world operational conditions, making Assumption 1 both practical and necessary. Additionally,

## Page 8

Actuators 2024, 13, 529
8 of 23
this assumption is widely utilized in managing actuator uncertainties [48]. Assumptions 2 and 3
are commonly adopted in tracking control problems for quadrotors to ensure the stability and
robustness of the system [49,50].
3. High-Gain Disturbance Observer
This section presents the design of an HGDO to estimate disturbances d1 and d2,
denoted by their estimates ˆd1 and ˆd2. The proposed HGDO is formulated as follows:



˙ˆd1 = 1
ϵ1

d1 −ˆd1

,
˙ˆd2 = 1
ϵ2

d2 −ˆd2

,
(12)
where 1/ϵ1 and 1/ϵ2 are the observer gains. Each equation in (12) represents a first-order
filter with the transfer function
1
ϵis+1.
Remark 4. According to Assumption 3, Let us define the j−th component of di by dj
i such that
it satisfies
 ˙dj
i
 ≤δj
i.
(13)
The disturbances typically encompass unknown external forces, the gyroscopic effects of rotors,
or aerodynamic influences such as drag. Although detailed models for gyroscopic and aerodynamic
effects are available in the literature [51], these effects can be aggregated into disturbance terms
for each axis. The HGDO is particularly advantageous as it estimates the amplitudes of such
disturbances, thereby reducing the reliance on complex dynamic models.
By selecting small positive values for ϵi, the settling time of the observer is reduced,
ensuring the rapid convergence of ˆdi to di. To express the system in state-space form, let
us define the following variables: x1 = a, x2 = ˙a, x3 = b, x4 = ˙b, d1 = δa
m , d2 = I−1δb,
u1 = KΘu1
m , u2 = ur[ζ13, ζ14, ζ15]T, g = [0, 0, g]T, where I is the unit matrix. Additionally,
let ¯K = [ ˙χ ˙ηζ4, ˙ρ ˙ηζ7, ˙ρ ˙χζ10]T. Using these definitions, the dynamics in (1) are rewritten as















˙x1 = x2,
˙x2 = −g + u1 + d1,
˙x3 = x4,
˙x4 = ¯K + u2 + d2.
(14)
The unknown disturbances di can be extracted from (14) as



d1 = ˙x2 + g −u1,
d2 = ˙x4 −¯K −u2.
(15)
Based on these dynamics, the HGDO for the quadrotor is proposed as



˙ˆd1 = 1
ϵ1

˙x2 + g −u1 −ˆd1

,
˙ˆd2 = 1
ϵ2

˙x4 −¯K −u2 −ˆd2

.
(16)
Assuming that the initial disturbance estimates are zero, i.e., ˆdi(0) = 0, the formulation
in (16) has the drawback of amplifying measurement noise due to the inclusion of the
derivatives of the system states. To address this issue, inspired by the approach in [52],
auxiliary variables ξ1 and ξ2 are introduced:

## Page 9

Actuators 2024, 13, 529
9 of 23
ξ1 = ˆd1 −x2
ϵ1
,
ξ2 = ˆd2 −x4
ϵ2
.
(17)
The dynamics of these auxiliary variables are given as



˙ξ1 = −1
ϵ1

ξ1 + x2
ϵ1

+ 1
ϵ1 (g −u1),
˙ξ2 = −1
ϵ2

ξ2 + x4
ϵ2

+ 1
ϵ2 (−¯K −u2).
(18)
To establish the convergence properties of the observer, the disturbance estimation
error is defined as ˜di = di −ˆdi. Differentiating ˜di and using (17) yields



˙˜d1 = ˙d1 −

ξ1 + ˙x2
ϵ1

,
˜d2 = ˙d2 −

ξ2 + ˙x4
ϵ2

.
(19)
Using the dynamics of (18) in (19), the disturbance estimation error dynamics can be
expressed as
˙˜di = −1
ϵi
˜di + ˙di.
(20)
The solution to this differential equation can be obtained by multiplying both sides by
e
1
ϵi t and integrating over the interval [0, t], resulting in
˜di(t) = ˜di(0)e−1
ϵi t +
Z t
0 e−1
ϵi (t−γ) ˙di(γ)dγ.
(21)
Rewriting (21) in a component-wise form and applying the absolute value
operator gives
 ˜dj
i(t)
 ≤
 ˜dj
i(0)e−1
ϵi t
 +

Z t
0 e−1
ϵi (t−γ) ˙dj
i(γ)dγ
.
(22)
Using the triangle inequality [53], which states that

R t
0 χ(υ)dυ
 ≤R t
0 |χ(υ)|dυ,
one obtains
 ˜dj
i(t)
 ≤
 ˜dj
i(0)e−1
ϵi t
 +
Z t
0
e−1
ϵi (t−γ) ˙dj
i(γ)
dγ.
(23)
Integrating (23) over [0, t] yields
Z t
0
 ˜dj
i(γ)
dγ ≤
Z t
0
 ˜dj
i(0)e−1
ϵi γ
dγ +
Z t
0
Z τ
0 e−1
ϵi (τ−γ) ˙dj
i(γ)
dγ

dτ,
(24)
where the first term on the right-hand side in (24) can be bounded as ϵi
 ˜dj
i(0)
. The second
term is equivalent to
h(t) ∗˙dj
i(t)
, where h(t) = e−t/ϵi and ∗represent the convolution
operator. Applying Young’s convolution theorem [54], one has
h(t) ∗˙dj
i(t)
 ≤∥h(t)∥
 ˙dj
i(t)
.
(25)
Since the L1-norm of h(t) is ∥hi(t)∥= ϵi, it follows that
Z t
0
 ˜dj
i(γ)
dγ ≤ϵi
 ˜dj
i(0)
 + ϵi
 ˙dj
i
.
(26)
From the definition of the L1-norm and using (13), one obtains
 ˜dj
i(t)
 ≤ϵi
 ˜dj
i(0)
 + δj
i

,
(27)

## Page 10

Actuators 2024, 13, 529
10 of 23
which leads to
 ˜di(t)
 ≤ϵi
 ˜di(0)
 + δi

.
(28)
Since ϵi is a small positive constant, (28) demonstrates that the disturbance estimation
error remains bounded and converges to a small value, verifying the effectiveness of the
developed HGDO.
4. HGDO-NN-AFSMC Controller Design
In this section, an NN-AFSMC position and attitude control strategy is proposed
for QUAVs based on an HGDO to address modeling uncertainties and external distur-
bances. Let us define the translational and rotational tracking errors as eω = ω −ωd
and ep = p −pd, respectively.
To achieve robust tracking, two sliding surfaces are
defined as
s1
s2

=
υ1eω + Dλ−1eω + ˙eω
υ2ep + Dλ−1ep + ˙ep

,
(29)
where Dλ(·) denotes the Riemann–Liouville fractional derivative of order 0 < λ < 1, and
υ1 > 0 and υ2 > 0 are user-defined constants.
Taking the time derivative of (29) yields
˙s1
˙s2

=
υ1 ˙eω + Dλeω + Autr + AKΘψ1 + ϖ1(·) + δa −¨ωd
υ2 ˙ep + Dλep + Bur + Bψr + ϖ2(·) + δp −¨pd

.
(30)
To simplify the analysis, the nonlinear terms are defined as
¯H1(·) = υ1 ˙eω + Dλeω + AKΘψ1 + ϖ1(·) + δa −¨ωd,
¯H2(·) = υ2 ˙ep + Dλep + Bψr + ϖ2(·) + δp −¨pd.
(31)
Both ¯H1(·) and ¯H2(·) consist of uncertain parameters and unmeasurable variables,
making their direct inclusion in the control law impractical. Even if the analytical expres-
sions for these terms were derived, incorporating them into the control design would
increase the system’s complexity and reduce the controller’s flexibility.
Radial basis function NNs (RBFNNs), a subset of NNs, are widely recognized for
their effectiveness in accurately approximating complex nonlinear functions, provided
they are appropriately designed and configured [55–58]. This property can be leveraged to
handle the nonlinearities and uncertainties encapsulated in ¯H1(·) and ¯H2(·). By employing
RBFNNs, these terms can be approximated as
 ¯H1(·)
¯H2(·)

=
w∗T
1 χ1(Ω1) + Φ1(Ω1)
w∗T
2 χ2(Ω2) + Φ2(Ω2)

,
(32)
where Ωi = [ωi, ωd,i, ˙ωi, ˙ωd,i, ¨ωi], i = 1, 2 represents the input vector to the NN. The term
w∗T
i
∈Rn denotes the ideal weight vector, where n is the total number of neurons in the
hidden layer. The terms Φi represent the approximation errors, and χi(Ωi) are the Gaussian
activation functions defined as
χi(Ωi) =
1
√2πℓi
exp
 
−∥Ωi −χi∥2
2ℓ2
i
!
,
i = 1, 2,
(33)
where χi and ℓi are constants representing the center and width of the basis function,
respectively.
It is important to note that both Φi and w∗T
i
are bounded, satisfying ∥Φi∥≤Φm,i and
∥w∗T
i ∥≤wm,i, where Φm,i and wm,i are unknown positive constants.
Theorem 1. Considering the quadrotor’s translational dynamics as outlined in (6), and assuming
that Assumptions 1–3 hold true, the control algorithm is designed to guarantee that the tracking

## Page 11

Actuators 2024, 13, 529
11 of 23
error eω remains ultimately uniformly bounded (UUB). By setting ˙si = 0, the control inputs for the
translational and rotational subsystems can be expressed as utr = −1
A ¯H1(·) and ur = −1
B ¯H2(·),
respectively. The adaptive control law is then defined as
utr
ur

=
−1
A ¯H1(·) −(k1 + 1/2)s1 −g1 ˆβ1s1χ2
1
−1
B ¯H2(·) −(k2 + 1/2)s2 −g2 ˆβ2s2χ2
2

,
(34)
with the adaptive law
" ˙ˆβ1
˙ˆβ2
#
=
−µ1 ˆβ1 + g1∥s1∥2χ2
1
−µ2 ˆβ2 + g2∥s2∥2χ2
2

,
(35)
where ˆβi(0) ≥0, ki > 0, gi > 0, and µi > 0 (i = 1, 2) are user-specified design parameters. The
variable ˆβi represents the estimate of βi, defined as βi = w2
m,i.
Proof of Theorem 1. Applying the control law given in (34) results in the following closed-
loop error dynamics:
˙s1
˙s2

=
−(k1 + 1/2)As1 −Ag1 ˆβ1s1χ2
1
−(k2 + 1/2)Bs2 −Bg2 ˆβ2s2χ2
2

.
(36)
Given that the matrices {A, B} are symmetric and positive-definite, the following
inequalities hold: sT
1 As1 ≥κa∥s1∥2 and sT
2 Bs2 ≥κb∥s2∥2, where 0 < κa ≤κmin{A} and
0 < κb ≤κmin{B}. Here, κmin represents the smallest eigenvalue of the respective matrix.
Consider the following Lyapunov function candidate,
V1
V2

=
" 1
2sT
1 s1 +
1
2β1 ˜β2
1 + 1
2 ˜dT
1 ˜d1
1
2sT
2 s2 +
1
2β2 ˜β2
2 + 1
2 ˜dT
2 ˜d2
#
,
(37)
where ˜β1 = β1 −κa ˆβ1 and ˜β2 = β2 −κb ˆβ2 represent the virtual parameter estimation errors.
Using (32) and (36), the time derivative of V1,2 can be expressed as
 ˙V1
˙V2

=

sT
1 ˙s1 −
˜β1
β1
˙ˆβ1 + ˜dT
1 ˙˜d1
sT
2 ˙s2 −
˜β2
β2
˙ˆβ2 + ˜dT
2 ˙˜d2


(38)
=
"
sT
1
−(k1 + 1/2)As1 −Ag1 ˆβ1s1χ2
1 + w∗T
1 χ1 + Φ1 + ˜d1
 −˜β1 ˙ˆβ1 + ˜dT
1 ˙d1 −˜dT
1 ˙ˆd1
sT
2
−(k2 + 1/2)Bs2 −Bg2 ˆβ2s2χ2
2 + w∗T
2 χ2 + Φ2 + ˜d2
 −˜β2 ˙ˆβ2 + ˜dT
2 ˙d2 −˜dT
2 ˙ˆd2
#
.
Applying the Young inequality, one obtains
"
sT
1 w∗T
1 χ1 ≤g1β1∥s1∥2χ2
1 +
1
4g1
sT
2 w∗T
2 χ2 ≤g2β2∥s2∥2χ2
2 +
1
4g2
#
,
(39)
"
sT
1 Φ1 ≤1
2κa∥s1∥2 +
1
2κa Φ2
m,1
sT
2 Φ2 ≤1
2κb∥s2∥2 +
1
2κb Φ2
m,2
#
,
(40)
sT
1 ˜d1 ≤1
2∥s1∥2 + 1
2∥˜d1∥2
sT
2 ˜d2 ≤1
2∥s2∥2 + 1
2∥˜d2∥2

.
(41)
By employing the adaptive law in (35) and substituting the inequalities from (39)–(41)
into (38), the following expression is obtained:

## Page 12

Actuators 2024, 13, 529
12 of 23
˙V1 ≤−(k1 + 1/2)κa∥s1∥2 + g1 ˜β1∥s1∥2χ2
1 + 1
4g1
(42)
+ 1
2κa
Φ2
m,1 + 1
2κa∥s1∥2 + µ1 ˜β1 ˆβ1 −g1 ˜β1∥s1∥2χ2
1 + ˜dT
1 ˙d1 −˜dT
1 ˙ˆd1
≤−k1κa∥s1∥2 + 1
4g1
+ 1
2κa
Φ2
m,1 + µ1 ˜β1 ˆβ1 + ˜dT
1 ˙d1 −˜dT
1 ˙ˆd1,
˙V2 ≤−(k2 + 1/2)κb∥s2∥2 + g2 ˜β2∥s2∥2χ2
2 + 1
4g2
+ 1
2κb
Φ2
m,2 + 1
2κb∥s2∥2 + µ2 ˜β2 ˆβ2 −g2 ˜β2∥s2∥2χ2
2 + ˜dT
2 ˙d2 −˜dT
2 ˙ˆd2
≤−k2κb∥s2∥2 + 1
4g2
+ 1
2κb
Φ2
m,2 + µ2 ˜β2 ˆβ2 + ˜dT
2 ˙d2 −˜dT
2 ˙ˆd2.
To enhance disturbance adaptation, an auxiliary parameter is introduced, defined
as follows:
" ˙ˆd1
˙ˆd2
#
=
 ˙d1 −¯ξ1 ˜d1
˙d2 −¯ξ2 ˜d2

,
(43)
where ¯ξ1,2 > 0 are constant gains introduced to ensure a reduction in the disturbance
estimation error over time. By substituting (43) into (42) and utilizing the inequalities
0 < µ1 ˜β1 ˆβ1 ≤µ1 1
κa (β2
1 −˜β2
1) and 0 < µ2 ˜β2 ˆβ2 ≤µ2 1
κb (β2
2 −˜β2
2), (42) can be further
simplified and expressed as
˙V1 ≤−

k1 + 1
2

κa∥s1∥2 −µ1
κa
˜β2
1 −¯ξ1∥˜d1∥2 + 1
4g1
+ 1
2κa
Φ2
m,1 + µ1
κa
β2
1,
(44)
˙V2 ≤−

k2 + 1
2

κb∥s2∥2 −µ2
κb
˜β2
2 −¯ξ2∥˜d2∥2 + 1
4g2
+ 1
2κb
Φ2
m,2 + µ2
κb
β2
2.
Considering the constants Ψ1 =
1
4g1 +
1
2κa Φ2
m,1 + µ1
κa β2
1 < ∞and Ψ2 =
1
4g2 +
1
2κb Φ2
m,2 +
µ2
κb β2
2 < ∞, ensuring that the derivatives of the Lyapunov functions, ˙V1,2, are strictly
negative requires that the constants Ψ1 and Ψ2 satisfy the following condition:
Ψ1
Ψ2

<



k1 + 1
2

κa∥s1∥2 + µ1
κa ˜β2
1 + ξ1∥˜d1∥2

k2 + 1
2

κb∥s2∥2 + µ2
κb ˜β2
2 + ξ2∥˜d2∥2

.
(45)
To ensure that ˙V1,2 < 0 regardless of the values of ∥si∥2, ˜β2
i , and ∥˜di∥2, i = 1, 2, the
constants Ψ1,2 must satisfy the conditions
(
Ψ1
=
1
4g1 +
1
2κa Φ2
m,1 + µ1
κa β2
1 < 0,
Ψ2
=
1
4g2 +
1
2κb Φ2
m,2 + µ2
κb β2
2 < 0.
(46)
Since these parameters are inherently positive, it becomes necessary to ensure that
Ψ1,2 are minimized relative to the chosen control gains k1,2, µ1,2, and ξ1,2 in the Lyapunov
function. To achieve this, the control parameters k1,2, κa,b, µ1,2, and ξ1,2 must be selected
such that (k1 + 1/2)κa, (k2 + 1/2)κb, µ1/κa, µ2/κb, and ξ1,2 are sufficiently large to domi-
nate Ψ1,2. This ensures that the negative terms in ˙V1,2 exceed the positive constants Ψ1,2,
resulting in a negative value for ˙V1,2.
Furthermore, given that ˙V1,2 are negative semidefinite and bounded, it follows that the
Lyapunov functions V1,2 ∈L∞are ultimately bounded, meaning V1,2 ∈L∞. The L∞-norm
is defined as the maximum absolute value, given by ∥x∥∞= maxi |xi| for a vector x, or
∥f ∥∞= supt | f (t)| for a function f (t). Consequently, the boundedness of V1,2 guarantees
that the sliding variables s1,2 are also bounded, implying s1,2 ∈L∞. Considering the
bounded nature of ˙s1, along with the boundedness of ˆβ1,2 and χ1,2, it can be inferred that:

## Page 13

Actuators 2024, 13, 529
13 of 23
∥˙s1∥
∥˙s2∥

≤


k1 + 1
2
∥A∥∥s1∥+ g1∥ˆβ1∥∥s1∥∥χ1∥2 ≤G1∥s1∥+ G2,
k2 + 1
2
∥A∥∥s2∥+ g2∥ˆβ2∥∥s2∥∥χ2∥2 ≤G3∥s2∥+ G4,

,
(47)
where {G1, G2, . . . , G4} represent the constants determined by the maximum values of the
bounded terms. Additionally, ˆβ1,2 ∈L∞is established due to the bounded nature of the
adaptive law in (35). Since ˆβ1,2, s1,2, and χ1,2 are confirmed to be bounded, it follows that
"
∥˙ˆβ1∥
∥˙ˆβ2∥
#
≤
µ1∥ˆβ1∥+ g1∥s1∥2∥χ1∥2
µ2∥ˆβ2∥+ g1∥s2∥2∥χ2∥2

.
(48)
Hence, ˙eω ∈L∞, eω ∈L∞, and uatr ∈L∞. This indicates that all internal system
signals are bounded.
Remark 5. The novelty of the proposed adaptation law lies in its streamlined structure, which pri-
oritizes minimizing the computational complexity of online parameter updates while ensuring both
stability and convergence. Instead of updating a high-dimensional weight matrix as in traditional
NN-based control methods, this law focuses on a virtual scalar parameter. This scalar is governed
by a carefully constructed Lyapunov function, guaranteeing system stability and the convergence of
tracking errors to a small neighborhood around zero. Additionally, the adaptation law is designed to
handle bounded uncertainties robustly, allowing the control system to adapt to real-time variations
without significant computational overhead.
By considering (8) and employing the trigonometric identity sin2(·) + cos2(·) = 1, it
can be deduced that u2
1 = U2
x + U2
y + U2
z. Given that utr is defined as utr = [Ux, Uy, Uz]T
and using the virtual control utr as formulated in (34), the actual control input u1 can be
determined directly as
u1 = ∥utr∥=
q
U2x + U2y + U2z.
(49)
Furthermore, the desired roll and pitch references, ρd and χd, are derived from the
virtual position controller, as elaborated in [59]. According to (8), the system exhibits six
degrees of freedom {ρ, χ, η, Ux, Uy, Uz}. Here, Ux, Uy, and Uz are determined using (34),
while the desired yaw trajectory ηd is predefined as an additional reference. Consequently,
ρd and χd are calculated following the methodology in [59]:
ρd = arcsin
Ux sin(ηd) −Uy cos(ηd)
∥utr∥

,
(50)
χd = arctan
Ux cos(ηd) + Uy sin(ηd)
Uz

.
(51)
It is worth noting that, to ensure the calculation of ρd and χd is singularity-free,
three conditions must be satisfied. First, the magnitude of the virtual control vector,
∥utr∥=
q
U2x + U2y + U2z, must be strictly positive (∥utr∥> 0) to prevent undefined values
in the denominator of ρd. Second, the argument of the arcsin function, Ux sin(ηd)−Uy cos(ηd)
∥utr∥
,
must lie within the interval [−1, 1] to ensure the arcsin function remains real-valued. Third,
the denominator in χd, Uz, must not equal zero (Uz ̸= 0) to avoid undefined results in the
arctan function.
Remark 6. The presented control strategy directly estimates the lumped uncertainties by leveraging
NN capabilities. Unlike conventional approaches requiring online updates of a weight matrix
wi for each approximation, this method only updates scalar parameters (βi). This significantly
reduces computational complexity, especially for high-dimensional systems. The proposed framework
simplifies neural adaptive control design while maintaining efficiency, as is further discussed in the
subsequent sections.

## Page 14

Actuators 2024, 13, 529
14 of 23
Remark 7. The selection of hidden layer neurons in the NN strikes a balance between tracking
accuracy and computational efficiency. Initially, a minimal number of neurons are selected, with
increases made gradually until no significant improvement in tracking performance is observed. This
methodology ensures optimal results without adding unnecessary complexity to the control system.
Remark 8. The parameters κa and κb play a pivotal role in stability analysis during the develop-
ment of the controller. However, these parameters are not embedded within the control algorithm
itself, removing the need for precise analytical predictions. This reduces computational overhead
significantly. Furthermore, the control design does not depend on prior knowledge of lumped un-
certainties ¯H1(·) and ¯H2(·). Once implemented, the control system does not require modifications
or reprogramming, even under changing operational conditions for the QUAV (e.g., parameter
variations or uncertainty bounds), as long as these changes remain within the assumed bounds
specified in Assumptions 1 and 3.
Remark 9. The proposed framework integrates an HGDO with an online adaptive mechanism to
estimate disturbances and approximate unknown uncertainties in real time. This approach addresses
the unpredictable nature of disturbances and uncertainties, which renders pretraining impractical.
The control strategy employs direct NN-based adaptive sliding mode control, focusing on virtual
scalar parameters rather than requiring extensive online updates of large NN weight matrices.
This design ensures robust, accurate control while meeting real-time requirements in dynamic and
uncertain environments.
5. Simulation Analysis
To validate the effectiveness and robustness of the proposed HGDO-NN-AFSMC
controller, extensive simulation studies were conducted under challenging operating con-
ditions. This section provides a detailed analysis of the simulation results, focusing on
trajectory tracking performance and real-time computational efficiency.
5.1. Simulation Results
This section investigates the reliability of the proposed HGDO-based NN-AFSMC
controller by evaluating the position and attitude-tracking capabilities across a spiral flight
in the presence of external disturbances and model uncertainties. Table 2 illustrates the
model parameters.
Table 2. Parameter settings for the quadrotor UAV.
Variable
Value
Unit
m
2.0
kg
g
9.81
m/s
l
0.2
m
k
9.56E −6
N·s2
b
1.14E −7
N·s2/rad2
Φρ, Φχ, Φη
1.20E −6
N·s/rad
Φx, Φy, Φz
1.20E −2
N·s/rad
Ix
0.75
N·s2/rad
Iy
0.75
N·s2/rad
Iz
1.50
N·s2/rad
The performance of the proposed control approach for spiral trajectory tracking
was compared against robust feedback linearization (RFBL) [60] and nonsingular fast
terminal sliding mode control (NFTSMC) [61] under the influence of external disturbances
and model uncertainties. The evaluation considered a spiral trajectory defined as xd =
cos(0.2t), yd = sin(0.2t), and zd = 0.4t, with a constant yaw path given by ηd = 0. To test
robustness, variations in system parameters and external disturbances were introduced,

## Page 15

Actuators 2024, 13, 529
15 of 23
including a 50% change in rotary inertia, a 25% change in aerodynamic drag coefficients,
and external disturbances given by δa = [0.8 sin(t), 0.2 cos(t) + 0.4 sin(t), 2.1]T and δb =
[0.4 + 0.3 sin(8t), 0.75, 1.8 + 0.35 cos(40t)]T. The initial conditions for the system were set
as x0 = (0.5, −0.5, 0)T [m] for position and p0 = (0.2, 0.25, 0.2)T [rad] for attitude. The
parameters of the proposed HGDO-NN-AFSMC control scheme were defined as ϵ1,2 = 0.01,
k1 = 250, k2 = 270, g1 = g2 = 0.2, and µ1 = µ2 = 0.7. Additionally, the NN configuration
included n = 40 neurons, a uniform NN center at χ1,2 = 0, and a Gaussian function width
of ℓ1,2 = 4.
Remark 10. The considered external disturbances, δa = [0.8 sin(t), 0.2 cos(t) + 0.4 sin(t), 2.1]T
and δb = [0.4 + 0.3 sin(8t), 0.75, 1.8 + 0.35 cos(40t)]T, incorporate low-frequency components
(sin(t), cos(t)), high-frequency components (cos(40t)), and constant biases. These configurations
ensure the proposed controller’s robustness under both gradual variations and rapid dynamic changes,
which are often more challenging for conventional control schemes. The high-frequency component
(cos(40t)) approaches the upper threshold for practical quadrotor UAV studies, as actuator and
aerodynamic limitations make disturbances beyond this range unrealistic. The adopted disturbances
comprehensively tested the system’s capability to handle uncertainty and rapid variations.
Figure 2 illustrates the disturbance estimation performance of the HGDO for varying
gain values. Among the examined configurations, the results indicate that ϵ = 0.05 yields
the most favorable disturbance estimation outcomes, characterized by superior conver-
gence speed and minimal estimation error. Accordingly, the significant influence of ϵ on
the accuracy and response time of the estimation process can be observed, highlighting its
importance in effectively calibrating the disturbance observer to enhance performance. The
control signals generated by the proposed approach are depicted in Figure 3, demonstrating
that they remain uniformly bounded and continuous, which aligns with the theoretical
analyses, ensuring the stability of the closed-loop system under varying operating condi-
tions. As observed, when subjected to external disturbances and model uncertainties, the
control signal amplitudes increase to counteract the adverse effects of these disturbances,
ensuring robust system performance. This adaptive behavior highlights the ability of the
HGDO-NN-AFSMC controller to compensate for uncertainties and maintain the desired
system dynamics effectively. Additionally, the control signals exhibit minimal oscillations,
indicating a smooth and efficient response to external disturbances, which is essential for
practical applications involving precision.
Moreover, as depicted in Figures 4 and 5, the comparative analysis of rotational and
translational trajectory tracking demonstrates that the proposed controller consistently sur-
passes the performance of the RFBL and NFTSMC approaches. In particular, the enhanced
tracking precision of HGDO-NN-AFSMC is evident in the minimized deviation from the
reference trajectory, even under significant disturbances. The improvement stems from
the HGDO’s ability to effectively estimate and compensate for external disturbances and
the NN-AFSMC’s adaptive nature, which dynamically adjusts to model uncertainties. As
the zoomed-in insets illustrate, the proposed control scheme maintains a tighter adherence
to the desired paths compared to the other methods during transitions and critical points
such as the peaks and troughs of the references. Table 3 provides a detailed comparison of
the mean attitude and rotational tracking errors for the three control approaches—RFBL,
NFTSMC, and the proposed HGDO-NN-AFSMC—evaluated under external disturbances
and model uncertainties during spiral flight. The results highlight that the proposed
HGDO-NN-AFSMC achieves the lowest tracking errors across all rotational states (ρ, χ, µ)
and translational coordinates (x, y, z), demonstrating its superior robustness and precision.
Notably, the errors in the critical z-axis and yaw tracking (µ) are significantly reduced
compared to RFBL and NFTSMC, showcasing the effectiveness of the HGDO in estimating
disturbances and the NN-AFSMC’s adaptive capability in handling uncertainties.

## Page 16

Actuators 2024, 13, 529
16 of 23
Figure 2. The imposed external disturbances on the QUAV and their estimations with different gains.
Figure 3. HGDO -NN-AFSMC control signals for the spiral flight tracking under external disturbances
and model uncertainties.

## Page 17

Actuators 2024, 13, 529
17 of 23
Figure 4. Comparative rotational tracking performance for the spiral flight under external distur-
bances and model uncertainties.
Figure 5. Comparative attitude tracking performance for the spiral flight under external disturbances
and model uncertainties.

## Page 18

Actuators 2024, 13, 529
18 of 23
Table 3. Comparison of the mean tracking error performances under disturbances and uncertainties.
Tracking Error (Mean)
RFBL
NFTSMC
HGDO-NN-AFSMC
ρd −ρ (rad)
0.0013
0.0012
0.0005
Rotational
χd −χ (rad)
0.0035
0.0033
0.0015
µd −µ (rad)
0.0575
0.0516
0.0298
xd −x (m)
0.0780
0.0741
0.0222
Attitude
yd −y (m)
0.0034
0.0033
0.0016
zd −z (m)
0.2110
0.1513
0.0210
The 3D trajectory tracking performance, as shown in Figure 6, further validates the
robustness of the HGDO-NN-AFSMC controller. While both the RFBL and NFTSMC
approaches exhibit notable deviations from the reference path, the proposed method
adheres closely to the desired trajectory, with errors confined within a significantly narrower
margin. As observed, HGDO-NN-AFSMC consistently demonstrates higher fidelity in
tracking the reference trajectories across all attitude states. This is largely due to the seamless
integration of the HGDO and NN-AFSMC, which collectively enable the controller to
handle high-frequency variations and abrupt trajectory changes with stability and precision.
The HGDO-NN-AFSMC method closely follows the reference trajectories even during high-
frequency variations or abrupt transitions, showcasing its robustness and precision. This
superior tracking performance is a direct result of the combined effects of the external
HGDO and the NN-AFSMC, which dynamically adjusts to uncertainties and disturbances.
Figure 6. Comparative 3D tracking performance for the spiral flight under external disturbances and
model uncertainties.
5.2. Real-Time Computational Analysis
This section provides a detailed analysis of the computational demands of the pro-
posed HGDO-NN-AFSMC controller real-time requirements with respect to the RFBL
and NFTSMC approaches. The computational structure of the proposed controller is
streamlined through two key features:
•
The HGDO estimates external disturbances using a first-order filtering mechanism
(Equation (16)) with a single observer gain ϵ. This results in low computational com-

## Page 19

Actuators 2024, 13, 529
19 of 23
plexity while ensuring rapid convergence and minimal estimation errors. As shown
in Figure 2, ϵ = 0.05 provides the best trade-off between accuracy and response time.
•
Instead of updating the full NN weight matrix in real time, the proposed method
leverages a virtual scalar parameter ˆβi (Equation (35)), which dramatically reduces the
number of online computations compared to traditional adaptive neural controllers.
To quantify the real-time computational demands, simulations for a spiral trajectory
were conducted on a standard machine with the following specifications: Intel i7-8700
CPU, 16 GB RAM, MATLAB R2023a. Table 4 summarizes the number of operations
per loop and the corresponding computation times. As it is observed, the HGDO-NN-
AFSMC achieves a favorable trade-off between computational complexity and robustness.
Although RFBL has a slightly faster computation time (1.10 ms), its performance degrades
significantly in the presence of large disturbances and model uncertainties (Section 5.1).
Moreover, compared to NFTSMC, which incurs higher computational overhead due to
its nonlinear terms and finite-time convergence dynamics, the proposed method offers
25% faster execution while maintaining superior tracking accuracy (Figures 4–6). In this
context, the combination of HGDO for rapid disturbance estimation and NN-AFSMC for
adaptive control ensures real-time implementation feasibility without sacrificing precision
or robustness. As demonstrated, the proposed approach strikes an optimal balance between
computational efficiency and tracking performance, making it ideal for dynamic and
uncertain environments.
Table 4. Computational requirements of different control methods.
Method
Operations/Loop
Computation Time (ms)
HGDO-NN-AFSMC
∼65 operations
1.85 ms
RFBL
∼50 operations
1.10 ms
NFTSMC
∼90 operations
2.45 ms
6. Conclusions
This study explored a robust control strategy for achieving precise position and atti-
tude tracking in quadrotor UAVs under the influence of model uncertainties and external
disturbances. A compound control framework was proposed, combining a high-gain dis-
turbance observer (HGDO) with an adaptive neural-network-based fractional sliding mode
control (NN-AFSMC) scheme. By leveraging a comprehensive and detailed dynamic model
that captures the intricate nonlinear behaviors of QUAVs, the developed control scheme ad-
dresses the challenges of maintaining stable tracking performance in real-world operating
conditions. A key novelty lies in the integration of virtual parameters with NNs, effectively
reducing the number of online-updated parameters. This enhancement results in a control
structure that is not only computationally efficient but also straightforward to implement,
making it highly practical for real-time applications. The simplicity and adaptability of
the proposed method ensure accurate position and attitude tracking without imposing
significant computational demands. Theoretical analyses and extensive simulation studies
confirmed the effectiveness of the proposed control approach. Additionally, the extensive
simulations provided comparative results, demonstrating the ability of the HGDO-NN-
AFSMC controller to outperform robust feedback linearization (RFBL) and nonsingular fast
terminal sliding mode control (NFTSMC), especially under varying external disturbances
and model uncertainties. These results emphasize the applicability of the proposed method
in addressing real-world challenges for quadrotor UAV operations. The results demonstrate
superior tracking accuracy and robustness compared to other advanced control methods
in the presence of external disturbances and model uncertainties. These findings validate
the potential of the HGDO-NN-AFSMC controller for practical applications requiring high
precision and reliability in dynamic and uncertain environments.
In future work, experimental validation of the proposed control framework will be
conducted to evaluate its practical applicability and robustness in real-world scenarios. In

## Page 20

Actuators 2024, 13, 529
20 of 23
addition, advanced machine learning algorithms, such as reinforcement learning, can be
integrated to dynamically adjust the control parameters in real- time based on the opera-
tional conditions and environmental changes to enhance the adaptability and robustness
of the control scheme. Moreover, employing a hybrid control framework that integrates
reinforcement learning with the existing HGDO-NN-AFSMC could allow the system to
learn optimal control strategies while retaining the robust disturbance rejection capabilities
of the current method. Furthermore, a study could leverage the capabilities of digital
twins to provide a real-time, virtual replica of the QUAV system, enabling the continuous
monitoring and simulation of various operational scenarios. In this context, the deploy-
ment of digital twins in conjunction with real QUAVs can facilitate extensive testing and
fine-tuning of control schemes, ensuring they are well prepared for real-world challenges.
This dual-testing methodology could also help identify potential implementation issues
and accelerate the development of more efficient and reliable UAV control strategies. The
combined approach of digital and physical testing can significantly enhance the reliability
and efficiency of the developed approach. Additionally, while the proposed framework
was specifically designed for quadrotor UAVs, its modular design and robust features make
it applicable to a variety of other underactuated systems, such as robotic manipulators,
marine vessels, or fixed-wing aircraft. Future studies can explore the generalization of
this control framework to these domains by adapting the system dynamics and control
parameters accordingly. For example, in robotics, the framework can be used to achieve
precise trajectory tracking under uncertain payload conditions, while in aerospace applica-
tions, it can enhance stability and adaptability in challenging environmental conditions like
high turbulence. Such generalizations will not only validate the versatility of the proposed
method but also broaden its practical suitability in multiple disciplines.
Author Contributions: Conceptualization, R.M. and A.M.; methodology, R.M. and A.M.; software,
R.M. and A.M.; validation, Y.M., M.T., and A.A.; formal analysis, Y.M.; investigation, R.M., A.M., and
Y.M.; writing—original draft preparation, R.M. and A.M.; writing—review and editing, Y.M., M.T.,
A.A., I.B.K., and A.F.; supervision, Y.M., I.B.K., and A.F.; project administration, Y.M. All authors
have read and agreed to the published version of this manuscript.
Funding: This research received no external funding.
Data Availability Statement: The data supporting the findings of this study are available from the
corresponding author upon reasonable request, as the research is still ongoing.
Conflicts of Interest: The authors declare no conflicts of interest.
Abbreviations and Symbols
The following abbreviations, parameters, and symbols are used in this manuscript:
Abbreviations
3D
Three-Dimensional
ADP
Adaptive Dynamic Programming
DO
Disturbance Observer
FTSMC
Fast Terminal Sliding Mode Control
HGDO
High-Gain Disturbance Observer
LQR
Linear Quadratic Regulator
NFTSMC
Nonsingular Fast Terminal Sliding Mode Control
NN
Neural Network
NN-AFSMC
Neural Network-based Adaptive Fractional Sliding Mode Control
PID
Proportional–Integral–Derivative
QUAV
Quadrotor Unmanned Aerial Vehicle
RBFNN
Radial Basis Function Neural Network
RFBL
Robust Feedback Linearization
SMC
Sliding Mode Control
UAV
Unmanned Aerial Vehicle

## Page 21

Actuators 2024, 13, 529
21 of 23
Parameters and Symbols
a
System parameter
Φx, Φy, Φz
Translational aerodynamic damping coefficients
b
Drag coefficient
Φρ, Φχ, Φη
Rotational aerodynamic damping coefficients
d
Distance between the rotors
ψ
Yaw angle
e1, e2, e3
Position tracking errors
ψi
Actuator uncertainties
fx, fy, fz
External forces acting on the quadrotor
ρ
Roll angle
g
Gravitational acceleration
τ
Torque
h
Height of the quadrotor
θ
Pitch angle
Ix, Iy, Iz
Quadrotor moments of inertia
υ1, υ2
Sliding surface design constants
J
Moment of inertia matrix
α
Adaptation gain
k
Thrust coefficient
β
Learning rate in NN
k1, k2
Sliding mode control gains
βi
Virtual parameter for NN approximation
l
Rotor arm length (distance from center)
δ
Disturbance magnitude
m
Quadrotor mass
δa, δb
External disturbances
I
Identity matrix
ϵ
Small positive constant
n
Number of neurons in NN
ϵi
Observer gain in HGDO
p
Orientation vector
η
Rotational aerodynamic damping coefficient
q
Quaternion components
γ1, γ2
Control gains
r
Rotor speed
κ
Control parameter for stability
s1, s2
Sliding surface variables
λ
Fractional derivative order
Tat
Total thrust force
µ1, µ2
Adaptive update rate constants
t
Time
ν
Adaptive parameter
u1
Total thrust control input
Φi
NN approximation error
u2, u3, u4
Control torques along roll, pitch, and yaw x, y, z
Position coordinates in inertial frame
vx, vy, vz
Velocities in the inertial frame
w∗T
i
Ideal NN weight vector
References
1.
Hou, Y.; Chen, D.; Yang, S. Adaptive Robust Trajectory Tracking Controller for a Quadrotor UAV With Uncertain Environment
Parameters Based on Backstepping Sliding Mode Method. IEEE Trans. Autom. Sci. Eng. 2023, 1–11. [CrossRef]
2.
Zhou, Z.; Hu, J.; Chen, B.; Shen, X.; Meng, B. Target Tracking and Circumnavigation Control for Multi-Unmanned Aerial Vehicle
Systems Using Bearing Measurements. Actuators 2024, 13, 323. [CrossRef]
3.
Hui, N.; Guo, Y.; Han, X.; Wu, B. Robust H-Infinity Dual Cascade MPC-Based Attitude Control Study of a Quadcopter UAV.
Actuators 2024, 13, 392. [CrossRef]
4.
Wan, H.; Dong, H.; Gai, K. Computational investigation of cicada aerodynamics in forward flight. J. R. Soc. Interface 2015,
12, 20141116. [CrossRef]
5.
Wang, S.; Wang, S.; Fu, X.; Deng, X. A wall-boundary-natural transitional Reynolds-stress model for high-order wing-body
simulations. Phys. Fluids 2024, 36, 084115. [CrossRef]
6.
Liu, B.; Wang, Y.; Sepestanaki, M.A.; Pouzesh, M.; Mobayen, S.; Rouhani, S.H.; Fekih, A. Event-trigger-based adaptive barrier
function higher-order global sliding mode control technique for quadrotor UAVs. IEEE Trans. Aerosp. Electron. Syst. 2024,
60, 5674–5684. [CrossRef]
7.
Avram, R.C.; Zhang, X.; Muse, J. Nonlinear adaptive fault-tolerant quadrotor altitude and attitude tracking with multiple actuator
faults. IEEE Trans. Control. Syst. Technol. 2017, 26, 701–707. [CrossRef]
8.
Du, Y.; Huang, P.; Cheng, Y.; Fan, Y.; Yuan, Y. Fault tolerant control of a quadrotor unmanned aerial vehicle based on active
disturbance rejection control and two-stage Kalman filter. IEEE Access 2023, 11, 67556–67566. [CrossRef]
9.
Ke, C.; Cai, K.Y.; Quan, Q. Uniform passive fault-tolerant control of a quadcopter with one, two, or three rotor failure. IEEE Trans.
Robot. 2023, 39, 4297–4311. [CrossRef]
10.
Ramírez-Neria, M.; Luviano-Juárez, A.; González-Sierra, J.; Ramírez-Juárez, R.; Aguerrebere, J.; Hernandez-Martinez, E.G. Active
Disturbance Rejection Control for the Trajectory Tracking of a Quadrotor. Actuators 2024, 13, 340. [CrossRef]
11.
Ma, Q.; Jin, P.; Lewis, F.L. Guaranteed Cost Attitude Tracking Control for Uncertain Quadrotor Unmanned Aerial Vehicle Under
Safety Constraints. IEEE/CAA J. Autom. Sin. 2024, 11, 1447–1457. [CrossRef]
12.
Mallavalli, S.; Fekih, A. An Observer-based Backstepping Integral Nonsingular Fast Terminal Sliding Mode Fault Tolerant Control
Design for Quadrotors Under Different Types of Actuator Faults. Int. J. Control. Autom. Syst. 2023, 21, 4015–4031. [CrossRef]
13.
Mobayen, S.; El-Sousy, F.F.; Alattas, K.A.; Mofid, O.; Fekih, A.; Rojsiraphisal, T. Adaptive fast-reaching nonsingular terminal
sliding mode tracking control for quadrotor UAVs subject to model uncertainties and external disturbances. Ain Shams Eng. J.
2023, 14, 102059. [CrossRef]
14.
Mousavi, Y.; Zarei, A.; Mousavi, A.; Biari, M. Robust optimal higher-order-observer-based dynamic sliding mode control for
VTOL unmanned aerial vehicles. Int. J. Autom. Comput. 2021, 18, 802–813. [CrossRef]
15.
Liu, K.; Yang, P.; Wang, R.; Jiao, L.; Li, T.; Zhang, J. Observer-based adaptive fuzzy finite-time attitude control for quadrotor
UAVs. IEEE Trans. Aerosp. Electron. Syst. 2023, 59, 8637–8654. [CrossRef]

## Page 22

Actuators 2024, 13, 529
22 of 23
16.
Wang, J.; Zhu, B.; Zheng, Z. Robust adaptive control for a quadrotor UAV with uncertain aerodynamic parameters. IEEE Trans.
Aerosp. Electron. Syst. 2023, 59, 8313–8326. [CrossRef]
17.
Ma, W.; Hu, M.; Hao, W.; Wang, H.; Wang, P. Nonlinear Robust Fault-Tolerant Tracking Control of a Tri-Rotor UAV against
Actuator’s Abnormal Behavior. Actuators 2023, 12, 140. [CrossRef]
18.
Arab, A.; Mousavi, Y.; Yu, K.; Kucukdemiral, I.B. Safety Prioritization by Iterative Feedback Linearization Control for Collaborative
Robots. In Proceedings of the 2024 IEEE Conference on Control Technology and Applications (CCTA), Newcastle upon Tyne, UK,
21–23 August 2024; IEEE: Piscataway, NJ, USA, 2024; pp. 811–816.
19.
Liang, W.; Chen, Z.; Yao, B. Geometric adaptive robust hierarchical control for quadrotors with aerodynamic damping and
complete inertia compensation. IEEE Trans. Ind. Electron. 2021, 69, 13213–13224. [CrossRef]
20.
Huang, T.; Li, T.; Chen, C.P.; Li, Y. Attitude Stabilization for a Quadrotor Using Adaptive Control Algorithm. IEEE Trans. Aerosp.
Electron. Syst. 2023, 60, 334–347. [CrossRef]
21.
Lei, W.; Li, C.; Chen, M.Z. Robust adaptive tracking control for quadrotors by combining PI and self-tuning regulator. IEEE Trans.
Control. Syst. Technol. 2018, 27, 2663–2671. [CrossRef]
22.
Yang, P.; Feng, K.; Ding, Y.; Shen, Z. Fast terminal sliding mode control based on finite-time observer and improved reaching law
for aerial robots. Actuators 2022, 11, 258. [CrossRef]
23.
Tashakkori, A.; Talebzadeh, M.; Salboukh, F.; Deshmukh, L. Forecasting gold prices with MLP neural networks: A machine
learning approach. Int. J. Sci. Eng. Appl. 2024, 13, 13–20.
24.
Dadkhah, D.; Moheimani, S.R. Combining H∞and resonant control to enable high-bandwidth measurements with a MEMS
force sensor. Mechatronics 2023, 96, 103086. [CrossRef]
25.
Yang, P.; Wang, Z.; Zhang, Z.; Hu, X. Sliding mode fault tolerant control for a quadrotor with varying load and actuator fault.
Actuators 2021, 10, 323. [CrossRef]
26.
Ahmadi, K.; Asadi, D.; Merheb, A.; Nabavi-Chashmi, S.Y.; Tutsoy, O. Active fault-tolerant control of quadrotor UAVs with
nonlinear observer-based sliding mode control validated through hardware in the loop experiments. Control. Eng. Pract. 2023,
137, 105557. [CrossRef]
27.
Gao, B.; Liu, Y.J.; Liu, L. Adaptive neural fault-tolerant control of a quadrotor UAV via fast terminal sliding mode. Aerosp. Sci.
Technol. 2022, 129, 107818. [CrossRef]
28.
Nguyen, N.P.; Oh, H.; Moon, J. Continuous nonsingular terminal sliding-mode control with integral-type sliding surface for
disturbed systems: Application to attitude control for quadrotor UAVs under external disturbances. IEEE Trans. Aerosp. Electron.
Syst. 2022, 58, 5635–5660. [CrossRef]
29.
Liu, K.; Wang, R.; Wang, X.; Wang, X. Anti-saturation adaptive finite-time neural network based fault-tolerant tracking control
for a quadrotor UAV with external disturbances. Aerosp. Sci. Technol. 2021, 115, 106790. [CrossRef]
30.
Mu, C.; Zhang, Y. Learning-based robust tracking control of quadrotor with time-varying and coupling uncertainties. IEEE Trans.
Neural Netw. Learn. Syst. 2019, 31, 259–273. [CrossRef] [PubMed]
31.
Mousavi, Y.; Zarei, A.; Kucukdemiral, I.B.; Fekih, A.; Alfi, A. Disturbance observer and tube-based model reference adaptive
control for active suspension systems with non-ideal actuators. IFAC-PapersOnLine 2023, 56, 1075–1081. [CrossRef]
32.
Dadkhah, D.; Moheimani, S.R. Design, Fabrication, and Control of a Double-Stage MEMS Force Sensor. IEEE/ASME Trans.
Mechatronics 2024, 1–11. [CrossRef]
33.
Mousavi, Y.; Alfi, A.; Kucukdemiral, I.B.; Fekih, A. Tube-based model reference adaptive control for vibration suppression of
active suspension systems. IEEE/CAA J. Autom. Sin. 2022, 9, 728–731. [CrossRef]
34.
Arab, A.; Mousavi, Y. Optimal control of wheeled mobile robots: From simulation to real world. In Proceedings of the 2020
American Control Conference (ACC), Denver, CO, USA, 1–3 July 2020; IEEE: Piscataway, NJ, USA, 2020; pp. 583–589.
35.
Shafai, B.; Zarei, F. Positive Stabilization and Observer Design for Positive Singular Systems. In Proceedings of the 2024 63rd
IEEE Conference on Decision and Control (CDC), Milan, Italy, 16–19 December 2024; IEEE: Piscataway, NJ, USA, 2024.
36.
Xu, S. Disturbance Observer-Based Adaptive Fault Tolerant Control with Prescribed Performance of a Continuum Robot.
Actuators 2024, 13, 267. [CrossRef]
37.
Mousavi, Y.; Bevan, G.; Kucukdemiral, I.B.; Fekih, A. Observer-based high-order sliding mode control of DFIG-based wind
energy conversion systems subjected to sensor faults. IEEE Trans. Ind. Appl. 2023, 60, 1750–1759. [CrossRef]
38.
Zarei, A.; Mousavi, Y.; Mosalanezhad, R.; Atazadegan, M.H. Robust voltage control in inverter-interfaced microgrids under
plug-and-play functionalities. IEEE Syst. J. 2019, 14, 2813–2824. [CrossRef]
39.
Xu, J.; Fang, L.; Wang, H.; Zhao, Q.; Wan, Y.; Gao, Y. Observer-Based Finite-Time Prescribed Performance Sliding Mode Control
of Dual-Motor Joints-Driven Robotic Manipulators with Uncertainties and Disturbances. Actuators 2024, 13, 325. [CrossRef]
40.
Sun, Z.; Liu, H.; Li, K.; Su, W.; Jiang, Y.; Chen, B. A Disturbance Observer-Based Fractional-Order Fixed-Time Sliding Mode
Control Approach for Elevators. Actuators 2024, 13, 438. [CrossRef]
41.
Mousavi, Y.; Bevan, G.; Kucukdemiral, I.B.; Fekih, A. Active fault-tolerant fractional-order terminal sliding mode control for
dfig-based wind turbines subjected to sensor faults. In Proceedings of the 2022 IEEE IAS Global Conference on Emerging
Technologies (GlobConET), Arad, Romania, 20–22 May 2022; IEEE: Piscataway, NJ, USA, 2022; pp. 587–592.
42.
Xie, X.; Zheng, J.; Zhang, L. A Composite Control Method Based on Model Predictive Control and a Disturbance Observer for the
Acquisition, Tracking, and Pointing System. Actuators 2024, 13, 417. [CrossRef]

## Page 23

Actuators 2024, 13, 529
23 of 23
43.
Errouissi, R.; Viswambharan, A.; Shareef, H. Adaptive high-gain observer-based control for grid-tied LCL filter systems.
IEEE Trans. Ind. Appl. 2023, 59, 5059–5073. [CrossRef]
44.
Won, D.; Kim, W.; Tomizuka, M. Nonlinear control with high-gain extended state observer for position tracking of electro-
hydraulic systems. IEEE/ASME Trans. Mechatron. 2020, 25, 2610–2621. [CrossRef]
45.
Zhou, S.; Wang, M.; Jia, J.; Guo, K.; Yu, X.; Zhang, Y.; Guo, L. Fault Separation Based on An Excitation Operator with Application
to a Quadrotor UAV. IEEE Trans. Aerosp. Electron. Syst. 2024, 60, 4010–4022. [CrossRef]
46.
Rostam-Alilou, A.A.; Zhang, C.; Salboukh, F.; Gunes, O. Potential use of Bayesian Networks for estimating relationship among
rotational dynamics of floating offshore wind turbine tower in extreme environmental conditions. Ocean. Eng. 2022, 244, 110230.
[CrossRef]
47.
Wang, H.; Cui, G.; Li, H. Fixed-time adaptive tracking control for a quadrotor unmanned aerial vehicle with input saturation.
Actuators 2023, 12, 130. [CrossRef]
48.
Wang, W.; Wen, C. Adaptive actuator failure compensation control of uncertain nonlinear systems with guaranteed transient
performance. Automatica 2010, 46, 2082–2091. [CrossRef]
49.
Zhao, B.; Xian, B.; Zhang, Y.; Zhang, X. Nonlinear robust adaptive tracking control of a quadrotor UAV via immersion and
invariance methodology. IEEE Trans. Ind. Electron. 2014, 62, 2891–2902. [CrossRef]
50.
Islam, S.; Liu, P.X.; El Saddik, A. Robust control of four-rotor unmanned aerial vehicle with disturbance uncertainty. IEEE Trans.
Ind. Electron. 2014, 62, 1563–1571. [CrossRef]
51.
Martini, S.; Sönmez, S.; Rizzo, A.; Stefanovic, M.; Rutherford, M.J.; Valavanis, K.P. Euler-Lagrange modeling and control of
quadrotor UAV with aerodynamic compensation. In Proceedings of the 2022 International Conference on Unmanned Aircraft
Systems (ICUAS), Dubrovnik, Croatia, 21–24 June 2022; IEEE: Piscataway, NJ, USA, 2022; pp. 369–377.
52.
Won, D.; Kim, W.; Shin, D.; Chung, C.C. High-gain disturbance observer-based backstepping control with output tracking error
constraint for electro-hydraulic systems. IEEE Trans. Control. Syst. Technol. 2014, 23, 787–795. [CrossRef]
53.
Saitoh, S. Generalizations of the triangle inequality. J. Inequal. Pure Appl. Math 2003, 4, 5.
54.
Carlen, E.A.; Lieb, E.H.; Loss, M. A sharp analog of Young’s inequality on SN and related entropy inequalities. J. Geom. Anal.
2004, 14, 487–520. [CrossRef]
55.
Zhao, W.; Gu, L. Adaptive PID Controller for Active Suspension Using Radial Basis Function Neural Networks. Actuators 2023,
12, 437. [CrossRef]
56.
Tavasoli, M.; Lee, E.; Mousavi, Y.; Pasandi, H.B.; Fekih, A. Wipe: A novel web-based intelligent packaging evaluation via machine
learning and association mining. IEEE Access 2024, 12, 45936–45947. [CrossRef]
57.
Mousavi, A.; Mousavi, R.; Mousavi, Y.; Tavasoli, M.; Arab, A.; Fekih, A. Artificial Neural Networks-Based Fault Localization in
Distributed Generation Integrated Networks Considering Fault Impedance. IEEE Access 2024, 12, 82880–82896. [CrossRef]
58.
Zhang, C.; Feng, Y.; Wang, J.; Gao, P.; Qin, P. Vehicle sideslip angle estimation based on radial basis neural network and unscented
Kalman filter algorithm. Actuators 2023, 12, 371. [CrossRef]
59.
Islam, S.; Liu, P.; El Saddik, A. Nonlinear adaptive control for quadrotor flying vehicle. Nonlinear Dyn. 2014, 78, 117–133.
[CrossRef]
60.
Sadiq, M.; Hayat, R.; Zeb, K.; Al-Durra, A.; Ullah, Z. Robust Feedback Linearization based Disturbance Observer Control of
Quadrotor UAV. IEEE Access 2024, 12, 17966–17981. [CrossRef]
61.
Labbadi, M.; Cherkaoui, M. Robust adaptive nonsingular fast terminal sliding-mode tracking control for an uncertain quadrotor
UAV subjected to disturbances. ISA Trans. 2020, 99, 290–304. [CrossRef]
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.
