# computation-14-00051.pdf

## Page 1

Academic Editor: Andry Sedelnikov
Received: 10 January 2026
Revised: 7 February 2026
Accepted: 9 February 2026
Published: 14 February 2026
Copyright: © 2026 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license.
Article
Robust Backstepping-Sliding Control of a Quadrotor UAV with
Disturbance Compensation
Vicente Borja-Jaimes 1
, Jorge Salvador Valdez-Martínez 2
, Miguel Beltrán-Escobar 2,
Guillermo Ramírez-Zúñiga 2
, Adriana Reyes-Mayer 2 and Manuela Calixto-Rodríguez 2,*
1
Departamento de Ingeniería Electrónica, Centro Nacional de Investigación y Desarrollo
Tecnológico (CENIDET), Tecnológico Nacional de México, Interior Internado Palmira s/n, Palmira,
Cuernavaca 62490, Morelos, Mexico; vicente.bjp@cenidet.tecnm.mx
2
División Académica de Mecánica Industrial, Universidad Tecnológica Emiliano Zapata del Estado de Morelos,
Av. Universidad Tecnológica No. 1, Emiliano Zapata 62760, Morelos, Mexico;
jorgevaldez@utez.edu.mx (J.S.V.-M.); miguelbeltran@utez.edu.mx (M.B.-E.);
guillermoramirez@utez.edu.mx (G.R.-Z.); adrianareyes@utez.edu.mx (A.R.-M.)
*
Correspondence: manuelacalixto@utez.edu.mx
Abstract
Quadrotor unmanned aerial vehicles (QUAVs) are widely used in civil and defense applica-
tions, yet reliable trajectory tracking remains challenging under external disturbances and
limited sensing. Conventional backstepping–sliding mode controllers ensure robustness
only by selecting discontinuous gains larger than the disturbance bound, which increases
chattering and limits the use of smooth switching functions. This paper addresses these
limitations by integrating explicit disturbance compensation into a backstepping–sliding
framework through a super-twisting observer (STO). The STO reconstructs matched distur-
bances acting on the translational and rotational dynamics in real time, and the estimated
signals are directly injected into the control law. This approach enables effective distur-
bance rejection beyond the nominal sliding gain while preserving robustness under smooth
control actions. Simulation results under single- and multi-frequency perturbations demon-
strate accurate disturbance reconstruction (FIT indices above 95%), improved tracking
performance, and a significant reduction in chattering. The proposed strategy provides a
robust control solution for QUAVs operating in uncertain environments.
Keywords:
quadrotor
unmanned
aerial
vehicles;
robust
nonlinear
control;
backstepping–sliding mode control; super-twisting observer; smooth sliding-mode control
1. Introduction
Quadrotor unmanned aerial vehicles (QUAVs) are widely used in civilian, industrial,
and defense applications owing to their high maneuverability, hovering capability, and
suitability for autonomous navigation tasks [1,2]. Their widespread deployment in in-
spection, mapping, precision agriculture, and search-and-rescue operations increasingly
demands control strategies that ensure reliable trajectory tracking under uncertain and
dynamic conditions [3,4]. Despite significant progress in nonlinear control methods, achiev-
ing consistent performance in QUAVs remains challenging [5,6]. This is largely due to
the underactuated structure of the vehicle, the strong coupling between translational and
rotational dynamics, and the persistent influence of external disturbances such as wind
gusts, payload variations, and sensor noise [7,8].
Computation 2026, 14, 51
https://doi.org/10.3390/computation14020051

## Page 2

Computation 2026, 14, 51
2 of 28
To address these challenges, extensive research has been devoted to the development
of robust control strategies [9]. Classical robust control frameworks, such as H∞control and
µ-synthesis, have been investigated for QUAVs, providing systematic robustness guaran-
tees typically derived from linearized models in the frequency domain, but often at the cost
of conservative designs and increased implementation complexity [10,11]. More recently,
predictive and hybrid disturbance-rejection approaches—including model predictive con-
trol for aerial payload transportation [12] and active disturbance rejection generalized
predictive control [13]—have been proposed to handle constraints and disturbance es-
timation explicitly; however, their practical deployment commonly relies on linearized
representations and entails online optimization or frequency-domain tuning requirements
that may limit real-time applicability.
Among robust nonlinear control strategies, backstepping control has gained promi-
nence for underactuated systems due to its recursive design structure and its ability to
handle nonlinearities systematically [14]. However, despite its strong theoretical foun-
dation, classical backstepping control assumes full state availability and tends to exhibit
performance degradation in the presence of modeling uncertainties and disturbances [15].
To enhance robustness, sliding mode control (SMC) techniques have been widely adopted,
leveraging their capability to reject matched disturbances and enforce finite-time conver-
gence through discontinuous control actions [16].
Recent studies have demonstrated the effectiveness of backstepping–sliding mode
frameworks in QUAV applications. For instance, in [17], a cascade active disturbance
rejection control strategy combined with backstepping sliding-mode control was proposed
to achieve robust trajectory tracking under model uncertainties. Adaptive backstepping
sliding-mode approaches have also been investigated to cope with uncertain environmen-
tal parameters and external disturbances, as reported in [18], where adaptive laws are
employed to compensate for unknown dynamics and improve tracking accuracy. Simi-
larly, adaptive backstepping controllers incorporating disturbance estimators have been
proposed to address parametric uncertainties and slowly varying perturbations [19].
From a comparative standpoint, existing robust control approaches for QUAVs differ
primarily in the way disturbances are modeled, estimated, and compensated within the
control loop, as well as in their computational and implementation requirements [14–16].
Frequency-domain robust controllers and predictive strategies typically rely on linearized
models and indirect disturbance attenuation mechanisms, whereas nonlinear designs
based on backstepping and sliding modes explicitly exploit system nonlinearities and
matched disturbance rejection, often at the expense of high switching gains or full
state availability [17–19].
While these contributions demonstrate the viability of backstepping–sliding mode
control architectures under uncertainty, they also reveal that performance and robustness
are strongly influenced by how disturbance-related information is modeled, estimated, and
incorporated into the control law. Most existing designs either rely on implicit disturbance
attenuation or treat disturbances as bounded but unknown signals, without explicitly
feeding reconstructed disturbance information back into the control law. As a result,
disturbance rejection is typically achieved indirectly, through conservative gain selection
rather than explicit compensation.
As a consequence, the robustness of conventional SMC-based designs depends on
selecting a discontinuous control gain that exceeds the worst-case disturbance magnitude.
In practical applications, such disturbance bounds are seldom available a priori and cannot
be assumed to remain constant across different operating conditions [20]. Huge sliding
gains, although theoretically ensuring robustness, inevitably induce chattering, increase
actuator wear, and amplify measurement noise—effects that are particularly detrimental
https://doi.org/10.3390/computation14020051

## Page 3

Computation 2026, 14, 51
3 of 28
for small-scale aerial platforms [21]. To mitigate chattering, smooth switching functions
such as saturation, sigmoid, or hyperbolic tangent mappings have been introduced [21].
However, these continuous approximations reduce the effective robustness margin, and
tracking performance degrades. This persistent trade-off between robustness and smooth
actuation remains a fundamental limitation of conventional SMC and its variants [22].
Several works have attempted to address this limitation through adaptive and
observer-based strategies [23,24]. Adaptive backstepping and sliding-mode schemes have
been proposed to estimate disturbance online and adjust controller gains accordingly [25,26].
Neural-network-based estimators, such as radial basis function neural networks, have
also been integrated with backstepping sliding-mode control to approximate complex
disturbance signals [27]. While effective, such approaches often introduce increased com-
putational complexity and require extensive tuning or training data, which may limit their
applicability in real-time embedded systems.
Higher-order sliding mode techniques offer an alternative and computationally ef-
ficient solution [28]. Among them, second-order sliding modes—particularly the super-
twisting algorithm (STA)—ensure finite-time convergence with continuous control action,
thereby mitigating chattering effects while preserving robustness [29]. When embed-
ded in observer structures, the resulting super-twisting observer (STO) enables finite-time
estimation of unmeasured states and lumped uncertainties without requiring output deriva-
tives [28]. STO-based observers have been successfully employed for state estimation in
QUAVs with limited sensing capabilities [30,31].
Despite these developments, a key differentiating factor between adaptive-SMC and
observer-based schemes is how disturbance-related information is incorporated into the
control law and how the associated robustness margins are achieved. In most existing
observer-based designs, the STO is primarily used to reconstruct unmeasured variables,
while the disturbance-related information contained in the observer injection terms is not
explicitly exploited for control design [20]. Although disturbance observers and extended
state observers have been incorporated into backstepping frameworks [32,33], the explicit
reconstruction and direct compensation of matched disturbances within a backstepping–
sliding mode control law—particularly under conditions where the sliding gain is deliber-
ately chosen below the disturbance magnitude—remains insufficiently explored [34].
This paper addresses this gap by proposing a disturbance-compensated control archi-
tecture for QUAVs that integrates a backstepping–sliding mode controller (BSMC) with a
super-twisting observer (STO). Unlike conventional approaches, the STO is not only used
for state reconstruction but is explicitly exploited to reconstruct matched disturbances in
real time and inject them directly into the control law. This mechanism enables effective
disturbance rejection without requiring large sliding-mode gains, thereby allowing smooth
control implementations while preserving finite-time convergence and robustness.
The main contributions of this work are summarized as follows:
•
A disturbance-compensated backstepping–sliding mode control architecture for
QUAVs, in which a super-twisting observer is integrated to explicitly reconstruct
matched disturbances acting on both translational and rotational dynamics.
•
An explicit disturbance reconstruction and compensation mechanism that directly
exploits the STO injection terms within the control law, enabling robust trajectory
tracking without requiring a priori knowledge of disturbance bounds or high-gain
discontinuous control actions.
•
A smooth sliding-mode realization achieved through observer-based disturbance
compensation, which allows the use of continuous switching functions—such as the
hyperbolic tangent—while preserving robustness and finite-time convergence.
https://doi.org/10.3390/computation14020051

## Page 4

Computation 2026, 14, 51
4 of 28
•
A Lyapunov-based stability analysis that explicitly accounts for bounded disturbances
and disturbance estimation errors, and establishes a quantitative link between distur-
bance estimation accuracy and the required robustness margins.
The effectiveness of the proposed control strategy is rigorously evaluated through
multiple simulation scenarios, including nominal operation, single-frequency and multi-
frequency disturbances, and smooth sliding-mode implementation. Quantitative per-
formance indices and disturbance reconstruction metrics demonstrate that the pro-
posed BSMC–STO scheme achieves superior tracking accuracy, enhanced disturbance
rejection, and smoother control action compared to the nominal backstepping–sliding
mode controller.
The remainder of this paper is organized as follows. Section 2 presents the quadrotor
dynamic model, observer formulation, and controller design. Section 3 describes the
simulation scenarios and presents the results. Finally, Section 4 presents the conclusions.
2. Dynamic Modeling, Observer Design, and Robust Control of
the QUAV
This section presents the methodological framework adopted for the modeling, ob-
servation, and control of the quadrotor unmanned aerial vehicle (QUAV) under matched
external disturbances. First, a nonlinear dynamic model of the QUAV is formulated, ex-
plicitly incorporating bounded perturbations in the translational and rotational dynamics.
Second, a super-twisting observer (STO) is developed to reconstruct the unknown dis-
turbances affecting the QUAV. Building upon these estimates, an observer-based robust
backstepping–sliding mode control strategy is then designed to ensure accurate trajectory
tracking and disturbance rejection. Finally, the stability of the combined observer–controller
scheme is established using Lyapunov analysis.
2.1. Dynamic Model of the Quadrotor with External Disturbances
Quadrotor unmanned aerial vehicles (QUAVs) are aerial robotic systems that combine
a compact mechanical architecture with high maneuverability, making them well-suited
for diverse applications in civil, industrial, and defense sectors. From a control-theoretic
perspective, QUAVs are underactuated nonlinear systems with coupled translational and
rotational dynamics, possessing six degrees of freedom but only four independent control
inputs [35]. These control inputs are generated by the collective and differential thrusts
of the four rotors and regulate the total vertical lift as well as the roll, pitch, and yaw
torque [6]. This intrinsic underactuation, together with strong nonlinear coupling between
the translational and rotational dynamics, poses significant challenges for the design of
robust and stable control laws [6,35].
The motion of the QUAV is described by a nonlinear dynamic model derived from
the Euler–Lagrange formulation. In this work, a widely adopted modeling framework is
employed, which assumes small angular displacements and angular rates. This assump-
tion enables the simplification of nonlinear trigonometric couplings while preserving the
dominant dynamic characteristics of the vehicle, as reported in [36].
The state vector of the QUAV model is defined as X =
h
ϕ,
.
ϕ, θ,
.
θ, ψ,
.
ψ, x,
.x, y,
.y, z,
.z
iT
,
where ϕ, θ, ψ denote roll, pitch, and yaw angles, respectively, and x, y, and z represent
the vehicle position expressed in the inertial reference frame. The even-indexed states
correspond to the associated angular and linear velocities. The control inputs are the
collective thrust µ1, and the control torques µ2, µ3, and µ4, applied about the body-fixed
axes to regulate the vehicle attitude and translational motion.
To account for unknown exogenous effects, the QUAV dynamic model is augmented
with disturbance terms. In this work, external disturbances are modeled as matched
https://doi.org/10.3390/computation14020051

## Page 5

Computation 2026, 14, 51
5 of 28
disturbances entering the system through the same channels as the control inputs. This
assumption is justified by the quadrotor’s actuation structure, in which the total thrust and
control torques directly influence the translational and rotational dynamics, respectively [1].
Disturbances such as wind gusts, aerodynamic drag variations, and parametric uncertain-
ties primarily affect these dynamics additively and can therefore be reasonably represented
as matched disturbances [15]. Under these assumptions, the nonlinear state-space model of
the QUAV with external perturbations can be written as
.
X =


x2
x4x6a1 + x4x6 + b1µ2 + ξ2
x4
x2x6a2 −x2x6 + b2µ3 + ξ4
x6
x2x4a3 + x2x4 + b3µ4 + ξ6
x8
µxµ1/m + ξ8
x10
µyµ1/m + ξ10
x12
µ1/m(Cx3Cx1) −g + ξ12


,
(1)
where X = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12] ∈R12 is the state vector, m is the
mass of the QUAV, g is the gravitational acceleration, and the rest of the parameters of the
QUAV model are defined as follows
a1 =
Iyy −Izz

/Ixx,
a2 = ((Izz −Ixx))/Iyy,
a3 =
Ixx −Iyy

/Izz,
b1 = 1/Ixx,
b2 = 1/Iyy,
b3 = 1/Izz,
µx = (Sx5Sx1 + Cx5Sx3Cx1),
µy = (−Cx5Sx1 + Sx5Sx3Cx1),
(2)
where C and S denote the cosine and sine trigonometric functions, respectively. The pa-
rameters a1, a2, and a3 are coupling coefficients arising from differences in the quadrotor’s
moments of inertia. The constants b1, b2, and b3 represent input scaling factors that map
the applied control torques to the corresponding angular accelerations. The control inputs
are the collective thrust and the roll, pitch, and yaw torques, denoted by µ1, µ2, µ3, and
µ4, respectively. Finally, ξi, for i = 2, 4, . . . , 12 denotes unknown but bounded matched
disturbances. Although the disturbances acting on the rotational dynamics are dominant
and have a stronger influence on the quadrotor behavior, disturbance terms affecting
the translational acceleration channels are also considered. These terms represent sec-
ondary uncertainties such as aerodynamic effects and thrust variations and are included
for completeness [1]. Their presence does not increase the structural complexity of the
control law, as they are handled in a unified manner by the proposed observer-based
backstepping–sliding mode framework.
It is acknowledged that perturbations, including sensor noise, unmodeled coupling
effects, and structural asymmetries, may introduce unmatched disturbance components.
Although sliding-mode-based control laws cannot completely reject such disturbances,
their effects are typically bounded and appear as performance degradation rather than
https://doi.org/10.3390/computation14020051

## Page 6

Computation 2026, 14, 51
6 of 28
instability [15]. The proposed control strategy, combined with the super-twisting observer,
enhances robustness against the dominant matched disturbances, which are the primary
source of performance deterioration in practical quadrotor operations.
2.2. Super-Twisting Observer for Disturbance Estimation
In practical applications, especially on cost-constrained platforms, QUAVs often lack
direct measurements of linear and angular velocities. Onboard sensors typically provide
position and orientation through GPS, barometers, and low-cost IMUs, while velocity
variables must be estimated using observer-based techniques [1].
The limited availability of measured variables presents a significant challenge for
feedback control design, especially when the system is subject to external perturbations.
To overcome this limitation, a super-twisting observer (STO) is developed to estimate the
unmeasurable velocity states and simultaneously reconstruct the matched perturbations
affecting the system [20].
In this framework, only the translational position (x, y, z) and the attitude angles
(ϕ, θ, ψ) are assumed to be directly measurable. Accordingly, the QUAV dynamic model is
reformulated into a structure suitable for observer synthesis by partitioning the state vector
as X1 = [x1, x3, x5, x7, x9, x11]T ∈R6 which contains the measurable position and attitude
angles, and X2 = [x2, x4, x6, x8, x10, x12]T ∈R6 corresponding to the unmeasured linear
and angular velocity components. Under this state partitioning, the system dynamics can
be rewritten in the following form
.
X1 = X2,
.
X2 = F(t, X1, X2, M) + Ξ2,
(3)
where F(t, X1, X2, M) captures the system nonlinearities and control inputs and is ex-
pressed as
F(t, X1, X2, M) =


x4x6a1 + x4x6 + b1µ2
x2x6a2 −x2x6 + b2µ3
x2x4a3 + x2x4 + b3µ4
µxµ1/m
µyµ1/m
µ1/m(Cx3Cx1) −g


,
(4)
and Ξ2 = [ξ2, ξ4, ξ6, ξ8, ξ10, ξ12]T ∈R6 collects the unknown but bounded external distur-
bance components acting on the rotational and translational dynamics. The control input
vector is defined as M =

µ2, µ3, µ4, µx, µy, µ1
T.
The proposed STO is expressed as
.
ˆX1 = ˆX2 + V1,
.
ˆX2 = F
t, X1, ˆX2, M
 + V2,
(5)
where ˆX1 ∈R6, ˆX2 ∈R6 are the observer state estimates, and V1 ∈R6, V2 ∈R6 are
correction terms defined as
V1 = Γ
X1 −ˆX1
1/2sign
X1 −ˆX1

, V2 = Bsign
X1 −ˆX1

,
(6)
https://doi.org/10.3390/computation14020051

## Page 7

Computation 2026, 14, 51
7 of 28
with gain vectors Γ = [γ1, . . . , γ6]T, and B = [β1, . . . , β6]T. The function F
t, X1, ˆX2, M

is
defined by substituting ˆX2 into the nonlinear dynamic expressions as
F
t, X1, ˆX2, M
 =


ˆx4 ˆx6a1 + ˆx4 ˆx6 + b1µ2
ˆx2 ˆx6a2 −ˆx2 ˆx6 + b2µ3
ˆx2 ˆx4a3 + ˆx2 ˆx4 + b3µ4
µxµ1/m
µyµ1/m
µ1/m(Cx3Cx1) −g


.
(7)
Letting
∼
X1 = X1 −ˆX1 and
∼
X2 = X2 −ˆX2 denote the estimation errors, the correspond-
ing error dynamics can be written as
.∼
X1 =
∼
X2 −Γ

∼
X1

1/2
sign
∼
X1

,
(8)
.∼
X2 = F(t, X1, X2, M) −F
t, X1, ˆX2, M
 −Bsign
∼
X1

+ Ξ2.
(9)
A finite-time convergence property for the estimation error can be established under
the standard assumptions typically invoked for super-twisting-type observers. In particular,
if the nonlinear term F(t, X1, X2, M) is locally Lipschitz with respect to its arguments, and
if uncertainty term F(t, X1, X2, M) −F
t, X1, ˆX2, M
 −Bsign
∼
X1

+ Ξ2, admits a known
uniform upper bound F+ > 0, then the estimation error is guaranteed to converge to the
origin in finite time. Based on this requirement, the observer gains are selected such that
B = 1.1F+ and Γ = 1.5F+1/2 are satisfied [37,38].
Remark: In practical implementations, the bound F+ does not need to be known
exactly. It can be selected using conservative estimates based on physical constraints of the
quadrotor, such as bounds on angular rates, velocities, actuator limits, and expected external
disturbances. Such bounds are commonly obtained from prior modeling knowledge,
simulation studies, or experimental tuning, and their conservative selection does not
compromise the finite-time convergence property of the STO [38].
In sliding mode theory, it is well established that the equivalent output injection term
of a sliding-mode observer encapsulates essential information about unmodeled dynamics,
external disturbances, and uncertain inputs acting on the systems [37]. This property arises
from the fact that, under ideal sliding conditions, the injection term must asymptotically
counteract the unknown input to enforce the sliding manifold. As such, it can be leveraged
as a foundation for disturbance reconstruction in nonlinear control systems, including
mechanical platforms such as QUAVs [39].
In
the
present
framework,
the
STO
estimates
all
the
even
states,
(i.e.,
X2
=
[x2, x4, x6, x8, x10, x12]T) based on the measurements of the odd states (i.e.,
X1 = [x1, x3, x5, x7, x9, x11]T). Since the finite time convergence of the STO guarantees
the existence of a time t0 > 0 such that, for all t ≥t0, the dynamics of the observation
errors satisfy
.∼
X1 = 0 and
.∼
X2 = 0. Under this condition, the error dynamics in Equation (9)
reduce to
0 = F(t, X1, X2, M) −F
t, X1, ˆX2, M
 −Bsign
∼
X1

+ Ξ2.
(10)
https://doi.org/10.3390/computation14020051

## Page 8

Computation 2026, 14, 51
8 of 28
Note that since one way of the sliding mode is established
ˆX2
=
X2, then
F(t, X1, X2, M) −F
t, X1, ˆX2, M
 = 0; therefore, the equivalent output injection term
Xeq is given by
Xeq =

Bsign
∼
X1

eq
= Ξ2.
(11)
From a theoretical perspective, the equivalent injection signal corresponds to the
average value of an ideal infinite-frequency switching process. Consequently, the injection
term contains high-frequency components that must be attenuated. To eliminate the high-
frequency component, we will use the filter of the form
T
.
Xeq = −Xeq + Bsign
∼
X1

,
(12)
where T denotes the filter time constant, selected such that h ≪T ≪1, and h is the
sampling step. The filtered equivalent injection signal is then used to define the disturbance
estimate vector as
ˆΞ2 ≜Xeq,
(13)
which relates to the actual disturbance vector according to
Ξ2 = ˆΞ2 + Ξ2,
(14)
where Ξ2 represents the bounded estimation error introduced by the filtering process.
The resulting estimation error Ξ2 explicitly captures the delay introduced by the filtering
process and is formally accounted for in the subsequent stability analysis.
Hence, the proposed STO provides a direct estimate of the external disturbance vector
from the filtered equivalent output injection signal. The resulting reconstruction error
remains bounded and is primarily determined by the filter time constant and the sampling
period. This disturbance estimate is then used in the control design to enhance robustness
against external perturbations, as detailed in the following section.
2.3. Disturbance-Compensating Backstepping Sliding Mode Controller
In QUAV applications, robust trajectory tracking must be achieved despite the pres-
ence of uncertainties and external disturbances, particularly when only partial-state mea-
surements are available. Traditional backstepping-sliding mode controllers (BSMC) offer
robustness through discontinuous control actions, but they typically neglect explicit dis-
turbance reconstruction, leading to conservative designs and limited performance under
dynamic perturbations [20].
In this work, we enhance the classical BSMC framework by integrating an active dis-
turbance compensation mechanism based on STO estimates. The core idea is to exploit the
STO’s correction term, which—under sliding motion—converges to the equivalent injection
needed to cancel matched perturbations. These estimates are then directly incorporated
into the control law, improving robustness and reducing steady-state error. The design
avoids dependence on velocity measurements and assumes only position and attitude
signals are available.
Let the state vector of the quadrotor unmanned aerial vehicle (QUAV) be defined as
X =
"
X1
X2
#
,
(15)
https://doi.org/10.3390/computation14020051

## Page 9

Computation 2026, 14, 51
9 of 28
where X1 = [x1, x3, x5, x7, x9, x11]T denotes the vector of attitude angles and position
coordinates, and X2 = [x2, x4, x6, x8, x10, x12]T represents the corresponding angular and
linear velocities.
The desired trajectory is defined as
Xd =
"
X1d
X2d
#
,
(16)
where X1d = [x1d, x3d, x5d, x7d, x9d, x11d]T denote the desired attitude and position vari-
ables, and X2d =
.
X1d their corresponding derivatives. Accordingly, the tracking error
vectors are defined as
E1 = X1d −X1,E2 = X2d −X2.
(17)
The QUAV dynamics can be written in second-order form as
.
X1 = X2,
.
X2 = F(t, X1, X2) + G(X1, X2)M+Ξ2,
(18)
where M =

µ2, µ3, µ4, µx, µy, µ1
T is the control input and Ξ2 = [ξ2, ξ4, ξ6, ξ8, ξ10, ξ12]T
denotes matched external disturbances.
The nonlinear vector field is defined as
F(t, X1, X2) =


x4x6a1 + x4x6
x2x6a2 −x2x6
x2x4a3 + x2x4
0
0
−g


,
(19)
and the control effectiveness matrix is given by
G(X1, X2) = diag

b1, b2, b3, µ1
m , µ1
m , Cx3Cx1
m

.
(20)
Substituting Equation (18) into the second equation of (17) yields
.
E2 =
.
X2d −F(t, X1, X2) −G(X1, X2)M −Ξ2.
(21)
Sliding Surface Definition
To ensure finite-time convergence of the tracking errors, a first-order sliding manifold
Σ = [σ1, σ3, σ5, σ7, σ9, σ11]T is defined as
Σ = −E2 −λE1 =


−e2 −λe1
−e4 −λe3
−e6 −λe5
−e8 −λe7
−e10 −λe9
−e12 −λe11


,
(22)
where λ > 0. The parameter λ is a design constant that determines the relative weight
between position and velocity tracking errors in the sliding surface. Increasing λ accelerates
convergence of the tracking errors but increases the control effort, while smaller values
result in smoother responses with slower convergence. In practice, λ is selected to achieve
https://doi.org/10.3390/computation14020051

## Page 10

Computation 2026, 14, 51
10 of 28
a compromise between transient performance and actuator limitations, and their value is
chosen sufficiently small to avoid excessive sensitivity to measurement noise [15,20].
Once Σ = 0 is reached, the error dynamics satisfy a stable linear differential equa-
tion, thereby ensuring the exponential convergence of the tracking errors. Differentiating
Equation (22) and using Equation (21), the sliding surface dynamic is obtained as
.
Σ = −
.
X2d + F(t, X1, X2) + G(X1, X2)M + Ξ2 −λE2.
(23)
Equivalent Control Design
The control objective is to design M such that the reachability condition ΣT .
Σ < 0
is satisfied. To this end, the control input is decomposed into a continuous nominal
component and additional terms devoted to robustness.
The control input is decomposed as
M = Meq + Msw + MΞ,
(24)
where Meq is the equivalent control defined as
Meq = F(t, X1, X2) +
.
X2d + λE2 =


−x4x6a1 −x4x6 +
.x2d + λe2
−x2x6a2 + x2x6 +
.x4d + λe4
−x2x4a3 −x2x4 +
.x6d + λe6
.x8d + λe8
.x10d + λe10
g +
.x12d + λe12


.
(25)
The equivalent control represents the continuous term that enforces sliding mo-
tion along the manifold under nominal conditions (i.e., neglecting switching and
disturbance dynamics.
The discontinuous control term is defined as
Msw = −k1sgn(Σ) −k2Σ =


−k1sign(σ1) −k2σ1
−k1sign(σ3) −k2σ3
−k1sign(σ5) −k2σ5
−k1sign(σ7) −k2σ7
−k1sign(σ9) −k2σ9
−k1sign(σ11) −k2σ11


(26)
where k1, k2 are constant positive gains. This term constitutes the discontinuous compo-
nent of the control law and is introduced to guarantee the reachability condition of the
sliding manifold.
Remark.
Unlike conventional backstepping–SMC designs, the proposed framework does not
rely on high-gain discontinuous terms for disturbance rejection. Instead, robustness is explicitly
achieved through observer-based disturbance compensation, improving modularity and reducing
control chattering.
Disturbance Compensation
To guarantee robustness against external disturbances, the compensated control law is
defined as
https://doi.org/10.3390/computation14020051

## Page 11

Computation 2026, 14, 51
11 of 28
MΞ = −ˆΞ2 =


−ˆξ2
−ˆξ4
−ˆξ6
−ˆξ8
−ˆξ10
−ˆξ12


(27)
where MΞ = −ˆΞ2, is the disturbance compensation term obtained from the equivalent
output injection term of the STO (as defined in Equation (13)). Incorporating the estimated
disturbance into the control law allows for active compensation of matched perturbations,
effectively attenuating their influence on the closed-loop dynamics.
Owing to the diagonal structure of G(X1, X2) each control channel can be explicitly
isolated, yielding the following individual control laws.
µ2 = 1
b1
−k1sign(σ1) −k2σ1 −a1x4x6 −x4x6 +
.x2d + λ1e2 −ˆξ2

,
(28)
µ3 = 1
b2
−k1sign(σ3) −k2σ3 −x2x6a2 + x2x6 +
.x4d + λe4 −ˆξ4

(29)
µ4 = 1
b3
−k1sign(σ5) −k2σ5 −x2x4a3 −x2x4 +
.x6d + λe6 −ˆξ6

(30)
µx = m
µ1
−k1sign(σ7) −k2σ7 +
.x8d + λe8 −ˆξ8

(31)
µy = m
µ1
−k1sign(σ9) −k2σ9 +
.x10d + λe10 −ˆξ10

(32)
µ1 =
m
Cx3Cx1
−k1sign(σ11) −k2σ11 + g +
.x12d + λe12 −ˆξ12

(33)
where σi with i ∈{1, 3, 5, 7, 9, 11} denote the individual components of the sliding surface
vector Σ. The terms ej with j ∈{2, 4, 6, 8, 10, 12} represent the first-order derivatives
of the position and attitude tracking errors, while the signals
.xjd denote the first-order
derivative of the reference trajectory. The quantities ˆξj denote the estimates of the matched
external disturbances.
The coefficients b1, b2, b3 are known positive control effectiveness parameters associ-
ated with the roll, pitch, and yaw torque channels, respectively, while m denotes the total
mass of the vehicle. The trigonometric terms C and S denote the cosine and sine functions,
respectively, and g is the gravitational acceleration.
The positive constants k1 and k2 are the sliding-mode gains that determine the con-
vergence speed toward the sliding manifold and the damping behavior along the surface,
respectively. And λ > 0 is a design parameter that shapes the transient response of the
tracking error dynamics.
Finally, the control inputs µ1, µ2, µ3, and µ4 correspond to the collective thrust and the
roll, pitch, and yaw control torques of the QUAV, respectively. The variables µx and µy are
virtual control inputs introduced in the backstepping design to regulate the translational
motion in the horizontal plane.
2.4. Lyapunov Stability
This subsection is devoted to the stability analysis of the proposed BSMC–STO strat-
egy. A Lyapunov framework is employed to establish the convergence properties of the
closed-loop system, explicitly accounting for bounded disturbances and observer-induced
estimation errors.
https://doi.org/10.3390/computation14020051

## Page 12

Computation 2026, 14, 51
12 of 28
Assumption 1. The desired trajectory Xd, as well as its first- and second-time derivatives,
are bounded.
Assumption 2. The external disturbance vectorΞ2 ∈R6is bounded, i.e.,
∥Ξ2∥< Ξm, Ξm > 0
(34)
Assumption 3. The super-twisting observer provides a bounded disturbance estimation error
defined as
Ξ2 = Ξ2 −ˆΞ2,
(35)
such that
Ξ2
 < Ξe, where Ξe > 0 is a known finite constant.
Theorem 1. Consider the nonlinear quadrotor system described by Equations (3) and (4) and the
sliding surface Σdefined in Equation (22). Suppose that Assumptions 1–3 are satisfied.
If the proposed backstepping–sliding mode control law, together with the super-
twisting-based disturbance estimation scheme, is applied, and the control gains k1 > 0 and
k2 > 0 are selected such that
k1 > Ξe,
(36)
then the sliding variable Σ reaches the origin in finite time. Consequently, the sliding
manifold is reached in finite time, and the closed-loop quadrotor system is robust with
respect to bounded matched disturbances.
Proof. Consider the following positive definite Lyapunov function candidate defined on
the sliding surface as
V = 1
2ΣTΣ,
(37)
clearly, V > 0 for all Σ ̸= 0, and V = 0 if and only if Σ = 0. Taking the time derivative of V
along the system trajectories yields
.
V = ΣT .
Σ.
(38)
From the sliding surface dynamics in Equation (23) and the closed-loop error dynamics
obtained after applying the control law, one has
.
Σ = Msw + Ξ2.
(39)
where Ξ2 denotes the disturbance estimation error vector.
The switching control term is defined as
Msw = −k1sign(Σ) −k2Σ.
(40)
Substituting into
.
V yields
.
V = −ΣTk1sign(Σ)−ΣTk2Σ+ΣTΞ2
(41)
Using the inequality ΣTsign(Σ) = ∥Σ∥, and applying the Cauchy–Schwarz inequality
to the disturbance estimation error, one obtains
.
V ≤−k1∥Σ∥−k2∥Σ∥2 + ∥Σ∥Ξe.
(42)
Therefore,
.
V ≤−(k1 −Ξe)∥Σ∥−k2∥Σ∥2.
(43)
https://doi.org/10.3390/computation14020051

## Page 13

Computation 2026, 14, 51
13 of 28
By selecting the scalar gain k1 such that k1 > Ξe, if follows that
.
V < 0 for all Σ ̸= 0.
Hence, the siding surface is finite-time reachable.
It is worth emphasizing that the disturbance estimation provided by the STO directly
reduces the required magnitude of the discontinuous control gains. This feature signifi-
cantly mitigates chattering while preserving finite-time convergence, constituting a key
advantage over conventional sliding mode control approaches that rely solely on high-gain
switching actions.
3. Results
This section presents a comparative evaluation of the proposed disturbance-compensated
backstepping–sliding mode controller (BSMC) across four simulation scenarios. In all cases,
the QUAV is required to track a reference trajectory under various disturbance condi-
tions. The scenarios assess the controller’s behavior when (i) no compensation is applied,
(ii) disturbance estimation and compensation are activated, (iii) perturbations vary in fre-
quency, and (iv) a smooth hyperbolic tangent (tanh) function replaces the discontinuous
sign function.
All simulations were executed in MATLAB 2024b using a fixed-step numerical inte-
gration scheme with a step size of 0.0001 s. The total simulation time for each simulation
scenario was set to 15 s, and the QUAV was initialized from rest conditions. The physical
parameters of the QUAV employed in the simulations are summarized in Table 1. The
desired trajectory of the angles and positions {ϕ, θ, ψ, x, y, z} in the simulation study
were selected as {0.1sin(0.4t), 0.05cos(0.4t), π
6 sin(0.6t), sin(t), cos(t), 0.5t}, which combine
smooth oscillatory motion in the lateral and angular coordinates with a linear ascent in the
vertical direction.
Table 1. Nominal parameters of the QUAV model [35].
Parameter
Symbol
Value
Mass
m
1.4 kg
Arm length
l
1 m
Moment of inertia along the x-axis
Ixx
0.0116 kg m2
Moment of inertia along the y-axis
Iyy
0.0116 kg m2
Moment of inertia along the z-axis
Izz
0.0232 kg m2
The controller parameters were set as k1 = 1, k2 = 1, and λ = 1. The parameter λ
influences the convergence rate of the position error; higher values accelerate error decay
but may increase control effort. The gain k2 governs the damping of the sliding variable,
improving steady-state smoothness while mitigating oscillations. The discontinuous gain
k1 provides robustness against bounded disturbances and estimation errors; larger values
enhance disturbance rejection at the cost of increased chattering.
The observer gains Γ and B were chosen sufficiently large to dominate the expected
disturbance bounds and ensure finite-time convergence of the estimation errors. The STO
gains were set as Γ = [16, 16, 16, 16, 16, 16]T, and B = [8, 8, 8, 8, 8, 8]T. Both controller
and observer gains remained consistent across all simulation cases. This consistent tuning
ensures that observed performance variations are attributable exclusively to disturbances
and to the activation of the compensation mechanism, rather than to gain re-adjustment.
External disturbances are modeled as bounded sinusoidal functions and are injected
into the six acceleration channels of the QUAV. Unless otherwise stated, the disturbance
applied is ξ = 10sin(0.5t), a value intentionally selected to exceed the discontinuous sliding-
mode gains used in the simulations. This choice is deliberate. Classical SMC guarantees
robustness only when the gain exceeds the peak disturbance amplitude. By violating this
https://doi.org/10.3390/computation14020051

## Page 14

Computation 2026, 14, 51
14 of 28
condition in Case 1, the limitations of the nominal BSMC are exposed, whereas Cases 2–4
show how disturbance reconstruction and compensation can restore robustness even under
gain-deficient conditions.
The control performance is quantified using standard evaluation metrics, including
the integral squared error (ISE) and the integral absolute error (IAE), defined as follows
ISE =
Z T0
0
E2dt,IAE =
Z T0
0
|E|dt,
(44)
where E = Xd −X is the tracking error vector, Xd ∈R12 denotes the desired trajectory state
vector, X ∈R12 represents the actual state vector, and T0 is the total simulation time.
To quantitatively assess the accuracy of the disturbance reconstruction performed
by the super-twisting observer (STO), the fit index (FIT) is employed as an additional
performance metric. The FIT criterion, based on the normalized root-mean-square error
(NRMSE), provides a percentage-based measure of how closely the estimated disturbance
matches the true injected disturbance. This metric is particularly relevant in Cases 2–4,
where disturbance compensation relies directly on the observer-generated estimates. The
FIT is defined as
FIT =
Ξ2(:, i) −ˆΞ2(:, i)

∥Ξ2(:, i) −mean(Ξ2(:, i))∥
(45)
where Ξ2 denotes the true disturbance vector and ˆΞ2 denotes its estimate obtained via the
STO. A FIT value close to 1 (or 100%) indicates excellent reconstruction accuracy, whereas
lower values reflect diminished correspondence between the true and estimated signals.
Remark: The proposed control law is derived in continuous time and evaluated
through numerical simulations. Practical implementation aspects related to finite-precision
arithmetic and discretization effects are not explicitly considered in this study. Rounding
errors introduced by digital processors can be regarded as bounded perturbations on
the control inputs, whose effect is mitigated by the inherent robustness of the proposed
control structure [21].
3.1. Case 1—Nominal BSMC Without Disturbance Compensation
This first simulation scenario evaluates the baseline performance of the BSMC without
incorporating disturbance compensation. The QUAV is subjected to a sinusoidal distur-
bance of the form 10sin(0.5t), injected into the translational and rotational dynamics. The
disturbance amplitude is deliberately selected to exceed the sliding gains, thereby violating
the classical matching condition required for robustness in conventional SMC. This config-
uration highlights the inherent limitation of standard SMC when the discontinuous control
gain is smaller than the magnitude of the external disturbance.
Figure 1 illustrates the tracking performance of the quadrotor’s translational and
rotational variables under the nominal BSMC when no disturbance compensation is applied.
As expected, due to the violation of the sliding-gain condition, the controller is unable to
counteract the disturbances, and the QUAV fails to track the prescribed reference trajectory.
In the angular position (ϕ, θ, ψ), the actual responses diverge from the reference shortly
after the maneuver begins, displaying pronounced oscillations whose amplitude and
phase are strongly influenced by the injected disturbance. Although partial alignment
with the reference is intermittently observed—most notably near the final seconds of the
simulation—accurate tracking is never achieved. The translational position (x, y, z) exhibit
even more pronounced degradation. The x- and y-axis responses show large deviations
during the entire trajectory, while the z-axis motion displays a persistent drift that prevents
convergence to the desired altitude profiles.
https://doi.org/10.3390/computation14020051

## Page 15

Computation 2026, 14, 51
15 of 28
 
Figure 1. Position and attitude tracking response of the QUAV under Case 1.
Figure 2 depicts the three-dimensional trajectory of the QUAV under the nominal
BSMC without disturbance compensation. The QUAV deviates sharply from the desired
path immediately after the maneuver begins, reflecting the controller’s inability to coun-
teract the injected sinusoidal disturbance whose amplitude surpasses the selected sliding
gains. Throughout most of the simulation, the vehicle remains significantly displaced from
the reference trajectory, exhibiting large oscillations and drift in all spatial coordinates as
a direct consequence of the violated matching condition. Only near the final segment of
the simulation does the quadrotor partially converge toward the commanded path, yet a
noticeable offset persists, confirming that the nominal BSMC cannot enforce robust tracking
when the disturbance magnitude exceeds the discontinuous control authority.
 
Figure 2. Three-dimensional flight trajectory of the QUAV under Case 1.
https://doi.org/10.3390/computation14020051

## Page 16

Computation 2026, 14, 51
16 of 28
To further assess the controller behavior, Figure 3 presents the tracking error signals for
both the position and orientation of the QUAV. As observed, none of the error trajectories
converge to the origin; instead, all exhibit a characteristic oscillatory pattern driven by the
external disturbance. In the rotational variables (ϕ, θ, ψ), the errors initially drift away from
zero and subsequently evolve periodically, with peak-to-peak amplitudes close to 0.2 rad,
reflecting the controller’s inability to counteract a perturbation whose magnitude exceeds
the sliding gain. A similar behavior is evident in the translational errors, particularly in
the lateral y-axis, where the deviation grows significantly during the first seconds of flight
and persists throughout the trajectory, consistent with the pronounced lateral drift seen
in the 3D path. Although a slight reduction in the error magnitude appears near the end
of the simulation—when the disturbance phase momentarily aligns with the controller
dynamics—the signals never approach a neighborhood of zero, confirming that the sliding
surfaces cannot be enforced under gain-deficient conditions.
Figure 3. Position and orientation tracking errors of the QUAV under Case 1.
Table 2 summarizes the quantitative tracking performance obtained in Case 1, using
the baseline BSMC without disturbance compensation. As expected from the qualitative
behavior observed in Figures 1–3, the error indices confirm that the controller fails to
guarantee accurate tracking when the amplitude of the injected sinusoidal disturbance
exceeds the selected sliding-mode gains. The ISE and IAE values for all position and
orientation variables are significantly elevated, reflecting persistent tracking deviations that
persist throughout the maneuver. In particular, the lateral position y exhibits the largest
degradation (ISE = 0.619259, IAE = 1.704568). The angular variables (ϕ,θ,ψ) show slightly
lower error magnitudes, yet their indices remain substantially higher than those typically
associated with stable sliding behavior, corroborating the inability of the controller to reject
perturbations whose magnitude surpasses the discontinuous control gain. Overall, these
metrics provide quantitative evidence that the nominal BSMC structure, without explicit
disturbance cancellation, is unable to maintain stability and accurate tracking under the
imposed disturbance profile, thereby motivating the development of the compensation
strategy evaluated in the subsequent cases.
https://doi.org/10.3390/computation14020051

## Page 17

Computation 2026, 14, 51
17 of 28
Table 2. Tracking error indices (ISE and IAE) under Case 1.
State Variable
Description
ISE
IAE
x1 = ϕ
Roll angle
0.104884
0.918579
x3 = θ
Pitch angle
0.104884
0.918579
x5 = ψ
Yaw angle
0.101693
0.845984
x7 = x
Position (x-axis)
0.101735
0.870135
x9 = y
Position (y-axis)
0.619259
1.704568
x11 = z
Position (z-axis)
0.101767
0.843183
3.2. Case 2—BSMC with STO-Based Disturbance Estimation and Compensation
This second simulation scenario evaluates the performance of the proposed disturbance-
compensated BSMC in conjunction with the STO. Unlike Case 1, where the controller
operates without access to disturbance information, the STO reconstructs in real time the si-
nusoidal perturbations injected into the translational and rotational dynamics of the QUAV
model. The estimated disturbance signals are then explicitly incorporated into the control
law, enabling the controller to counteract the perturbation rather than relying solely on dis-
continuous sliding-mode action. Importantly, the same controller and observer gains used
in Case 1 are retained here, ensuring that any performance improvement arises exclusively
from activating the estimation–compensation loop rather than from gain retuning.
Figure 4 illustrates the position and attitude tracking response of the QUAV when
the disturbance-compensation mechanism is activated through the STO. In contrast to the
degraded performance observed in Case 1, the trajectories in both position and attitude now
exhibit close and uniform correspondence with the reference signals throughout the entire
maneuver. The observer-based reconstruction of the injected sinusoidal disturbance enables
the controller to counteract its effect in real time, thereby preventing the large deviations
and phase lags previously induced by the perturbation exceeding the sliding gains. As
shown in Figure 4, both the translational and rotational variables converge smoothly to
the desired trajectories shortly after the transient phase, with minimal overshoot and no
oscillatory distortions characteristic of unmatched sliding conditions.
 
Figure 4. Position and attitude tracking response of the QUAV under Case 2.
https://doi.org/10.3390/computation14020051

## Page 18

Computation 2026, 14, 51
18 of 28
Figure 5 depicts the three-dimensional flight trajectory of the QUAV under Case 2. The
results show that the actual trajectory closely follows the helical reference path across all
spatial dimensions, with negligible deviation throughout the maneuver. In contrast to the
significant errors observed in Case 1, the compensated controller keeps the vehicle tightly
confined to the desired trajectory, even during segments with strong curvature or rapid
vertical transitions.
Figure 5. Three-dimensional flight trajectory of the QUAV under Case 2.
Figure 6 shows the STO-based reconstruction of disturbances injected into the transla-
tional and rotational dynamics of the QUAV. In each subplot, the estimated disturbance
closely follows the injected sinusoidal signal after a brief transient, demonstrating consis-
tent convergence and minimal steady-state deviation. The FIT values—between 96.56% and
96.57%—confirm the high accuracy of the estimation, reproducing the amplitude and phase
characteristics of the applied perturbations. This reliable reconstruction is essential for the
effectiveness of the compensation mechanism activated in Case 2, and the results substan-
tiate the STO’s capability to provide disturbance information with sufficient precision to
enhance closed-loop robustness.
Figure 7 shows the position and orientation tracking errors of the QUAV under Case
2. All error trajectories decay rapidly from their initial offsets, converging to zero without
overshoot or oscillation. Rotational errors converge within the first few seconds, while
translational errors follow a similar trend with slightly slower dynamics due to coupled
motion. The small steady-state residuals are consistent with the bounded disturbance
reconstruction accuracy reported in Figure 6.
Table 3 summarizes the QUAV’s tracking performance under Case 2, using the ISE
and IAE indices. The angular variables (ϕ,θ,ψ) exhibit low accumulated error, reflecting
the fast convergence observed in the attitude responses. The translational variables also
show small error magnitudes, with the x- and z-axes achieving particularly low ISE and
IAE values, consistent with their smooth tracking behavior. The slightly higher indices on
the y-axis correspond to the more demanding components of the reference trajectory but
remain within acceptable bounds for stable operation. Overall, the metrics confirm that the
disturbance-compensated controller maintains accurate tracking despite the presence of
external perturbations.
https://doi.org/10.3390/computation14020051

## Page 19

Computation 2026, 14, 51
19 of 28
Magnitude (rad/s2)
Magnitude (rad/s2)
Magnitude (rad/s2)
Magnitude (m/s2)
Magnitude (m/s2)
Magnitude (m/s2)
Figure 6. Disturbance reconstruction using the STO under Case 2.
Figure 7. Position and orientation tracking errors of the QUAV under Case 2.
Table 3. Tracking error indices (ISE and IAE) under Case 2.
State Variable
Description
ISE
IAE
x1 = ϕ
Roll angle
0.005050
0.100597
x3 = θ
Pitch angle
0.005050
0.100597
x5 = ψ
Yaw angle
0.101693
0.004308
x7 = x
Position (x-axis)
0.000500
0.032058
x9 = y
Position (y-axis)
0.531726
1.032139
x11 = z
Position (z-axis)
0.000000
0.000628
https://doi.org/10.3390/computation14020051

## Page 20

Computation 2026, 14, 51
20 of 28
3.3. Case 3 –BSMC with STO-Based Compensation Under Multi-Frequency Disturbances
In this third scenario, the QUAV is subjected to a more demanding perturbation envi-
ronment to assess the robustness of the proposed compensation strategy as the disturbance
spectrum becomes richer and more representative of real-world operational conditions.
Unlike Case 2—where a single-frequency sinusoidal disturbance was applied uniformly
across all velocity channels—here each of the six acceleration equations is excited by a sinu-
soid of identical amplitude but distinct frequencies. This configuration introduces phase
and excitation-rate variations across the translational and rotational dynamics, producing a
heterogeneous disturbance profile that is significantly harder to counteract and commonly
encountered in outdoor flights, where wind gusts, platform vibrations, and aerodynamic
coupling do not act coherently.
Figure 8 shows the tracking response of the QUAV when subjected to the multi-
frequency disturbance scenario of Case 3. At the qualitative level, the trajectories closely
resemble those obtained in Case 2. The actual variables follow their references with no
visually appreciable degradation in the transient or steady-state segments, despite the
higher spectral richness of the injected perturbations. The attitude and position responses
remain well aligned with their respective commands, and no additional oscillatory behavior
or tracking drift is apparent from the plots.
Figure 8. Position and attitude tracking response of the QUAV under Case 3.
Figure 9 illustrates the three-dimensional trajectory followed by the QUAV in Case
3. The vehicle traces the helical path with a high degree of fidelity, maintaining a smooth
ascent and consistent lateral progression. The alignment between the actual and reference
paths indicates that the disturbance compensation remains effective at the spatial level,
confirming that the controller preserves the global motion pattern despite the increased
variability in the excitation of the translational dynamics.
Figure 10 depicts the reconstruction of the multi-frequency disturbances injected into
the translational and rotational acceleration channels of the QUAV. Under this more de-
manding excitation profile—characterized by the superposition of sinusoidal components
with different frequencies—the STO maintains reliable convergence, reproducing the main
amplitude and phase characteristics of the injected signals after a brief transient. Although
https://doi.org/10.3390/computation14020051

## Page 21

Computation 2026, 14, 51
21 of 28
the disturbance profiles exhibit faster oscillations and increased spectral richness compared
with the single-frequency conditions of Case 2, the observer accurately captures their
overall structure across all channels.
Figure 9. Three-dimensional flight trajectory of the QUAV under Case 3.
Magnitude (rad/s2)
Magnitude (rad/s2)
Magnitude (rad/s2)
Magnitude (m/s2)
Magnitude (m/s2)
Magnitude (m/s2)
Figure 10. Disturbance reconstruction using the STO under Case 3.
The FIT percentages, which range from 92% to 95%, confirm that the STO preserves
high estimation accuracy despite the additional dynamic complexity introduced in this
scenario. The slight reduction in accuracy relative to Case 2 is expected and reflects
the inherent difficulty of reconstructing rapidly varying, multi-harmonic perturbations.
Nevertheless, the consistency of the FIT values among all acceleration-governing states
demonstrates the robustness of the STO and its capability to deliver disturbance estimates
with sufficient precision to support effective compensation within the BSMC framework.
https://doi.org/10.3390/computation14020051

## Page 22

Computation 2026, 14, 51
22 of 28
Figure 11 presents the tracking errors obtained in Case 3. A clear distinction emerges
between the attitude and position variables; the angular errors converge rapidly with
negligible residual oscillations, indicating that the rotational subsystem remains largely
insensitive to the gain reduction. In contrast, the translational errors exhibit the expected
periodic components inherited from the injected disturbances, particularly in the y and z
dynamics, where the multi-frequency content is more apparent. Despite these oscillatory
patterns, the error amplitudes remain bounded and small, showing that the closed-loop
structure effectively contains the disturbance influence even under a less aggressive obser-
vation scheme.
Figure 11. Position and orientation tracking errors of the QUAV under Case 3.
Table 4 summarizes the ISE and IAE indices obtained in Case 3. The attitude errors
maintain uniformly low magnitudes, with ISE values on the order of 10−3 and IAEs below
0.1, confirming that the rotational subsystem remains largely unaffected by the multi-
frequency disturbances. The translational dynamics also exhibit small error indices in
the x- and z-axes, reflecting effective compensation and stable tracking. As expected,
the y-axis—where the injected disturbance contains the richest spectral content—shows
noticeably higher ISE and IAE values. Yet, these remain bounded and consistent with the
oscillatory patterns observed in the error trajectories. Overall, the indices indicate that the
STO-assisted BSMC preserves satisfactory tracking accuracy across all variables despite the
increased disturbance complexity introduced in Case 3.
Table 4. Tracking error indices (ISE and IAE) under Case 3.
State Variable
Description
ISE
IAE
x1 = ϕ
Roll angle
0.004887
0.098933
x3 = θ
Pitch angle
0.004886
0.098899
x5 = ψ
Yaw angle
0.000009
0.004316
x7 = x
Position (x-axis)
0.000523
0.032833
x9 = y
Position (y-axis)
0.532516
1.032802
x11 = z
Position (z-axis)
0.000000
0.000737
https://doi.org/10.3390/computation14020051

## Page 23

Computation 2026, 14, 51
23 of 28
3.4. Case 4 –BSMC with STO-Based Compensation Using a Smooth Tanh-Based Sliding Function
In this fourth scenario, the QUAV is subjected to the same multi-frequency distur-
bance conditions described in Case 3. However, the discontinuous sign function in the
BSMC is replaced with a smooth hyperbolic tangent function. This modification enables
a continuous sliding action with reduced chattering while deliberately operating with a
sliding gain smaller than the magnitude of the injected disturbances. Under these more
challenging conditions, the goal is to assess whether robustness is preserved when the
inherent discontinuity of the traditional sliding mode is removed. The compensation mech-
anism remains unchanged. The STO reconstructs the heterogeneous disturbance profile and
feeds its estimate back into the control law. As shown in the subsequent results, accurate
disturbance estimates enable the controller to maintain effective disturbance rejection and
closed-loop stability. Moreover, the proposed smooth tanh-based formulation preserves
robustness and produces smoother control action without degrading tracking performance.
Figure 12 shows the position and attitude tracking response of the QUAV under Case 4.
The transition from the discontinuous sign function to the smooth tanh-based sliding action
does not produce any noticeable degradation in tracking performance. All translational
and rotational variables follow their references with comparable accuracy to the previous
scenarios. The trajectories remain well aligned throughout the maneuver.
 
Figure 12. Position and attitude tracking response of the QUAV under Case 4.
Figure 13 shows the three-dimensional trajectory obtained in Case 4. The QUAV
follows the reference trajectory with small deviations throughout the maneuver. The
observed radial and vertical deviations during ascent remain bounded and do not drift,
suggesting that the reduction in switching activity does not adversely affect the disturbance-
rejection capability of the STO-assisted controller.
Figure 14 shows the tracking errors obtained when the smooth tanh-based sliding
term is used. As in previous cases, the attitude errors decay rapidly and remain near zero,
confirming that the reduced discontinuity in the control law does not compromise the
stabilization of the rotational subsystem. For the translational dynamics, the errors retain
the periodic signatures induced by the multi-frequency disturbances, though with slightly
smoother envelopes than in Case 3, reflecting the effect of the softened sliding action.
https://doi.org/10.3390/computation14020051

## Page 24

Computation 2026, 14, 51
24 of 28
Importantly, these oscillations remain bounded and of small amplitude, indicating that
disturbance compensation remains effective even under a less aggressive control structure.
Overall, the results verify that the tanh replacement preserves robustness while reducing
chattering and yielding well-behaved error trajectories.
Figure 13. Three-dimensional flight trajectory of the QUAV under Case 4.
Figure 14. Position and orientation tracking errors of the QUAV under Case 4.
Table 5 summarizes the ISE and IAE indices for Case 4 under multi-frequency distur-
bances, with the discontinuous sign function replaced by a smooth tanh-based formulation.
The attitude variables remain accurately regulated, with ISE values on the order of 10−3
and IAEs near 0.1, indicating effective control of the rotational dynamics despite the re-
duced sliding gain and the absence of discontinuous switching. For translational motion,
the tracking errors along the x- and z-axes remain small and bounded, whereas the y-
axis—subject to the richest spectral excitation—exhibits larger but still well-contained error
https://doi.org/10.3390/computation14020051

## Page 25

Computation 2026, 14, 51
25 of 28
indices. Overall, the close agreement with Case 3 confirms that the STO-assisted BSMC
preserves its robustness and disturbance rejection capability while enabling continuous
control that mitigates chattering without compromising tracking accuracy.
Table 5. Tracking error indices (ISE and IAE) under Case 4.
State Variable
Description
ISE
IAE
x1 = ϕ
Roll angle
0.004682
0.105351
x3 = θ
Pitch angle
0.004717
0.107822
x5 = ψ
Yaw angle
0.000021
0.015050
x7 = x
Position (x-axis)
0.000578
0.044468
x9 = y
Position (y-axis)
0.533590
1.041481
x11 = z
Position (z-axis)
0.000024
0.017045
Figure 15 shows the control effort produced under Case 4, where the discontinuous
sign function of the sliding term is replaced by its smooth tanh-based counterpart. The
four control signals exhibit the expected attenuation of high-frequency components that
previously characterized the discontinuous formulation, leading to noticeably smoother
actuation profiles despite the presence of multi-frequency disturbances. The thrust and
torque commands remain well-structured and free of the high-frequency switching inherent
in classical SMC, indicating that the continuous approximation effectively suppresses
chattering while preserving sufficient control authority.
 
Figure 15. Control inputs of the BSMC-STO using a smooth tanh-based sliding function under Case 4.
It is worth emphasizing that the simulation scenarios presented in this section are
intentionally formulated under deterministic conditions. This choice allows isolating and
clearly highlighting the fundamental contribution of the proposed BSMC–STO scheme,
namely, its ability to preserve robust trajectory tracking when the switching gain is selected
smaller than the disturbance magnitude, a condition under which the classical BSMC fails.
By explicitly compensating matched disturbances through the observer-based injection
term, the proposed approach enables the use of smooth switching functions without loss of
https://doi.org/10.3390/computation14020051

## Page 26

Computation 2026, 14, 51
26 of 28
robustness, which directly translates into reduced chattering and smoother control actions.
The inclusion of sensor noise, processor noise, and actuator saturation effects, while highly
relevant for practical implementations, would require additional noise-aware observer
or filtering mechanisms and is, therefore, left for future investigation, particularly in the
context of experimental validation.
4. Conclusions
This study addressed the problem of robust trajectory tracking for quadrotor un-
manned aerial vehicles (QUAVs) in the presence of unknown but bounded external distur-
bances affecting both translational and rotational dynamics. A disturbance-compensated
backstepping–sliding mode control (BSMC) framework was proposed, in which a super-
twisting observer (STO) is integrated into a conventional BSMC structure to enable active
disturbance rejection.
Simulation results clearly demonstrate the limitations of the nominal BSMC when
the magnitude of external disturbances exceeds the selected discontinuous control gains.
Under such conditions, the baseline controller is unable to maintain the sliding manifold,
leading to a pronounced degradation in both position and attitude tracking performance.
By contrast, when the STO-based disturbance estimation and compensation mecha-
nism is incorporated, the closed-loop behavior improves substantially. Without modifying
the nominal controller gains, the proposed BSMC–STO scheme consistently restores robust
tracking performance in both position and attitude tracking. The STO accurately recon-
structs the matched disturbances, as quantified by the reported FIT indices, and the explicit
injection of these estimates into the control law effectively attenuates their impact on the
closed-loop dynamics.
The effectiveness of the proposed framework was further evaluated under multi-
frequency disturbance scenarios, in which the QUAV dynamics are subjected to perturba-
tions with distinct temporal characteristics. Even under these heterogeneous excitation
conditions, the STO maintains reliable disturbance reconstruction accuracy, and the con-
troller preserves accurate tracking performance without requiring gain retuning.
In addition, replacing the discontinuous sign function with a smooth hyperbolic
tangent function significantly reduces chattering while preserving robustness, provided
that disturbance estimates are available. The resulting smooth sliding behavior leads
to well-conditioned control inputs and bounded tracking errors, further demonstrating
that observer-based disturbance compensation effectively reduces reliance on strongly
discontinuous control actions.
It is important to emphasize that the robustness properties established in this work are
derived under the standard matching condition commonly assumed in sliding-mode-based
control frameworks. Within this framework, the proposed BSMC–STO scheme explicitly
compensates matched external disturbances acting on the quadrotor dynamics. An explicit
evaluation of robustness with respect to parametric uncertainties would require extending
the observer structure with adaptive or parameter-estimation mechanisms.
Future work will focus on experimental validation, the inclusion of sensor and actuator
nonidealities, extension to fault scenarios, and adaptive tuning of the observer and control
gains to further enhance robustness under rapidly varying operating conditions.
Author Contributions: Conceptualization, V.B.-J. and M.C.-R.; methodology, V.B.-J.; software, V.B.-J.;
validation, V.B.-J., J.S.V.-M. and A.R.-M.; formal analysis, V.B.-J., A.R.-M., G.R.-Z., M.B.-E., J.S.V.-M.
and M.C.-R.; investigation, V.B.-J. and M.C.-R.; resources, V.B.-J. and G.R.-Z.; data curation, V.B.-J. and
A.R.-M.; writing—original draft preparation, V.B.-J.; writing—review and editing, V.B.-J., A.R.-M.,
G.R.-Z., M.B.-E., J.S.V.-M. and M.C.-R.; visualization, J.S.V.-M. and A.R.-M.; supervision, V.B.-J. and
https://doi.org/10.3390/computation14020051

## Page 27

Computation 2026, 14, 51
27 of 28
M.C.-R.; project administration, V.B.-J. and M.B.-E. All authors have read and agreed to the published
version of the manuscript.
Funding: This research received no external funding.
Data Availability Statement: The original contributions presented in this study are included in the
article. Further inquiries can be directed to the corresponding author.
Acknowledgments: We would like to thank the Mexican people who supported this research through
the SECIHTI (Secretaria de Ciencia, Humanidades, Tecnología e Innovación— Secretary of Science,
Humanities, Technology and Innovation), Mexico.
Conflicts of Interest: The authors declare no conflicts of interest.
References
1.
Idrissi, M.; Salami, M.; Annaz, F. A Review of Quadrotor Unmanned Aerial Vehicles: Applications, Architectural Design and
Control Algorithms. J. Intell. Robot. Syst. 2022, 104, 22. [CrossRef]
2.
Ahmed, F.; Mohanta, J.C.; Keshari, A.; Yadav, P.S. Recent Advances in Unmanned Aerial Vehicles: A Review. Arab. J. Sci. Eng.
2022, 47, 7963–7984. [CrossRef]
3.
Sonugür, G. A Review of Quadrotor UAV: Control and SLAM Methodologies Ranging from Conventional to Innovative
Approaches. Robot. Auton. Syst. 2023, 161, 104342. [CrossRef]
4.
Obaid, L.; Hamad, K.; Al-Ruzouq, R.; Dabous, S.A.; Ismail, K.; Alotaibi, E. State-of-the-Art Review of Unmanned Aerial
Vehicles (UAVs) and Artificial Intelligence (AI) for Traffic and Safety Analyses: Recent Progress, Applications, Challenges, and
Opportunities. Transp. Res. Interdiscip. Perspect. 2025, 33, 101591. [CrossRef]
5.
Lopez-Sanchez, I.; Moreno-Valenzuela, J. PID Control of Quadrotor UAVs: A Survey. Annu. Rev. Control 2023, 56, 100900.
[CrossRef]
6.
Rinaldi, M.; Primatesta, S.; Guglieri, G. A Comparative Study for Control of Quadrotor UAVs. Appl. Sci. 2023, 13, 3464. [CrossRef]
7.
Meng, W.; Zhang, X.; Zhou, L.; Guo, H.; Hu, X. Advances in UAV Path Planning: A Comprehensive Review of Methods,
Challenges, and Future Directions. Drones 2025, 9, 376. [CrossRef]
8.
Telli, K.; Kraa, O.; Himeur, Y.; Ouamane, A.; Boumehraz, M.; Atalla, S.; Mansoor, W. A Comprehensive Review of Recent Research
Trends on Unmanned Aerial Vehicles (UAVs). Systems 2023, 11, 400. [CrossRef]
9.
Guettal, L.; Chelihi, A.; Ajgou, R.; Touba, M.M. Robust Tracking Control for Quadrotor with Unknown Nonlinear Dynamics
Using Adaptive Neural Network Based Fractional-Order Backstepping Control. J. Frankl. Inst. 2022, 359, 7337–7364. [CrossRef]
10.
Hamza, A.; Hossam, A.; El-Badawy, A. Robust H∞Control for a Quadrotor UAV. In Proceedings of the AIAA Science and
Technology Forum and Exposition (AIAA SciTech 2022), San Diego, CA, USA, 3–7 January 2022. [CrossRef]
11.
Panza, S.; Lovera, M.; Sato, M.; Muraoka, K. Structured µ-Synthesis of Robust Attitude Control Laws for a Quad-Tilt-Wing
Unmanned Aerial Vehicle. J. Guid. Control Dyn. 2020, 43, 2258–2274. [CrossRef]
12.
Urbina-Brito, N.; Guerrero-Sánchez, M.E.; Valencia-Palomo, G.; Hernández-González, O.; López-Estrada, F.R.; Hoyo-Montaño,
J.A. A Predictive Control Strategy for Aerial Payload Transportation with an Unmanned Aerial Vehicle. Mathematics 2021, 9, 1822.
[CrossRef]
13.
Cheng, Y.; Dai, L.; Li, A.; Yuan, Y.; Chen, Z. Active Disturbance Rejection Generalized Predictive Control of a Quadrotor UAV via
Quantitative Feedback Theory. IEEE Access 2022, 10, 37912–37923. [CrossRef]
14.
Mulualem, Y.L.; Jin, G.G.; Kwon, J.; Ahn, J. Backstepping Sliding Mode Control of Quadrotor UAV Trajectory. Mathematics 2025,
13, 3205. [CrossRef]
15.
Labbadi, M.; Boukal, Y.; Cherkaoui, M. Robust Nonlinear Backstepping SMC for QUAV Subjected to External Disturbances. Stud.
Syst. Decis. Control 2022, 384, 103–122. [CrossRef]
16.
Kuang, J.; Chen, M. Adaptive Sliding Mode Control for Trajectory Tracking of Quadrotor Unmanned Aerial Vehicles under Input
Saturation and Disturbances. Drones 2024, 8, 614. [CrossRef]
17.
Xu, L.X.; Ma, H.J.; Guo, D.; Xie, A.H.; Song, D.L. Backstepping Sliding-Mode and Cascade Active Disturbance Rejection Control
for a Quadrotor UAV. IEEE/ASME Trans. Mechatron. 2020, 25, 2743–2753. [CrossRef]
18.
Hou, Y.; Chen, D.; Yang, S. Adaptive Robust Trajectory Tracking Controller for a Quadrotor UAV with Uncertain Environment
Parameters Based on Backstepping Sliding Mode Method. IEEE Trans. Autom. Sci. Eng. 2025, 22, 4446–4456. [CrossRef]
19.
Xie, W.; Cabecinhas, D.; Cunha, R.; Silvestre, C. Adaptive Backstepping Control of a Quadcopter with Uncertain Vehicle Mass,
Moment of Inertia, and Disturbances. IEEE Trans. Ind. Electron. 2022, 69, 549–559. [CrossRef]
20.
Borja-Jaimes, V.; García-Morales, J.; Escobar-Jiménez, R.F.; Guerrero-Ramírez, G.V.; Adam-Medina, M. A Backstepping Sliding
Mode Control of a Quadrotor UAV Using a Super-Twisting Observer. Appl. Sci. 2025, 15, 10120. [CrossRef]
21.
Yesmin, A.; Sinha, A. Sliding Mode Controller for Quadcopter UAVs: A Comprehensive Survey. Drones 2025, 9, 625. [CrossRef]
https://doi.org/10.3390/computation14020051

## Page 28

Computation 2026, 14, 51
28 of 28
22.
Zhao, C.; Li, W.; Hao, S.; Gao, R.; Wu, S.; Li, H. Global Fast Terminal Sliding Mode Control for Trajectory Tracking Control of
Quadrotor UAVs. Sensors 2025, 25, 7480. [CrossRef]
23.
Yu, S.; Fan, X.; Qi, J.; Wan, L.; Liu, B. Attitude Control of Quadrotor UAV Based on Integral Backstepping Active Disturbance
Rejection Control. Trans. Inst. Meas. Control 2024, 46, 703–715. [CrossRef]
24.
Chen, F.; Jiang, R.; Zhang, K.; Jiang, B.; Tao, G. Robust Backstepping Sliding-Mode Control and Observer-Based Fault Estimation
for a Quadrotor UAV. IEEE Trans. Ind. Electron. 2016, 63, 5044–5056. [CrossRef]
25.
Maaruf, M.; Abubakar, A.N.; Gulzar, M.M. Adaptive Backstepping and Sliding Mode Control of a Quadrotor. J. Braz. Soc. Mech.
Sci. Eng. 2024, 46, 630. [CrossRef]
26.
Ahmed, N.; Hajlaoui, K.; Ma, M. Adaptive Backstepping Trajectory Tracking Control without Velocity Measurements for
Quadrotor UAVs under Multiple Unknown Disturbances. Int. J. Dyn. Control 2025, 13, 306. [CrossRef]
27.
Wei, L.; Tan, M.K.; Lim, K.G.; Teo, K.T.K. Adaptive Disturbance Stability Control for Uncrewed Aerial Vehicles Based on
Radial Basis Function Neural Networks and Backstepping Sliding-Mode Control. IEEE Trans. Aerosp. Electron. Syst. 2025, 61,
11208–11219. [CrossRef]
28.
Zhao, Z.; Cao, D.; Yang, J.; Wang, H. High-Order Sliding Mode Observer-Based Trajectory Tracking Control for a Quadrotor UAV
with Uncertain Dynamics. Nonlinear Dyn. 2020, 102, 2583–2596. [CrossRef]
29.
Rosales, C.; Vacca Sisterna, C.; Rossomando, F.; Gandolfo, D.; Soria, C.; Carelli, R. Super-Twisting Adaptive Control of a Quadrotor.
ISA Trans. 2025, 166, 241–249. [CrossRef] [PubMed]
30.
Shi, D.; Wu, Z.; Chou, W. Super-Twisting Extended State Observer and Sliding Mode Controller for Quadrotor UAV Attitude
System in Presence of Wind Gust and Actuator Faults. Electronics 2018, 7, 128. [CrossRef]
31.
Chen, A.J.; Sun, M.J.; Wang, Z.H.; Feng, N.Z.; Shen, Y. Attitude Trajectory Tracking of Quadrotor UAV Using Super-Twisting
Observer-Based Adaptive Controller. Proc. Inst. Mech. Eng. G J. Aerosp. Eng. 2021, 235, 1146–1157. [CrossRef]
32.
Wu, Y.; Ling, G.; Shi, Y. Robust Trajectory Tracking Fault-Tolerant Control for Quadrotor UAVs Based on Adaptive Sliding Mode
and Fault Estimation. Computation 2025, 13, 162. [CrossRef]
33.
Sun, Z.; Xiao, M.; Li, D.; Chu, J. Tracking Controller Design for Quadrotor UAVs under External Disturbances Using a High-Order
Sliding Mode-Assisted Disturbance Observer. Meas. Control 2025, 58, 155–167. [CrossRef]
34.
Hassani, H.; Mansouri, A.; Ahaitouf, A. Model-Based Robust Tracking Attitude and Altitude Control of an Uncertain Quadrotor
under Disturbances. Int. J. Aeronaut. Space Sci. 2024, 25, 1464–1478. [CrossRef]
35.
Hernández-Pérez, M.A.; Delgado-Reyes, G.; Borja-Jaimes, V.; Valdez-Martínez, J.S.; Cervantes-Bobadilla, M. An Adaptation
of a Sliding Mode Classical Observer to a Fractional-Order Observer for Disturbance Reconstruction of a UAV Model: A
Riemann–Liouville Fractional Calculus Approach. Mathematics 2023, 11, 4876. [CrossRef]
36.
Borja-Jaimes, V.; Coronel-Escamilla, A.; Escobar-Jiménez, R.F.; Adam-Medina, M.; Guerrero-Ramírez, G.V.; Sánchez-Coronado,
E.M.; García-Morales, J. Fractional-Order Sliding Mode Observer for Actuator Fault Estimation in a Quadrotor UAV. Mathematics
2024, 12, 1247. [CrossRef]
37.
Li, Y.; Tan, P.; Liu, J.; Chen, Z. A Super-Twisting Extended State Observer for Nonlinear Systems. Mathematics 2022, 10, 3584.
[CrossRef]
38.
Salgado, I.; Chairez, I.; Moreno, J.; Fridman, L.; Poznyak, A. Generalized Super-Twisting Observer for Nonlinear Systems. IFAC
Proc. Vol. 2011, 44, 14353–14358. [CrossRef]
39.
Chughtai, M.R.; Ahmad, I.; Mughees, A.; Iqbal, M.; Almakhles, D.; Abdelrahim, M. Third-Order Sliding Mode Control for
Trajectory Tracking of Quadcopters Using Particle Swarm Optimization. Drones 2025, 9, 172. [CrossRef]
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.
https://doi.org/10.3390/computation14020051
