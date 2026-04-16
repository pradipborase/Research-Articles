# electronics-15-00408-v2.pdf

## Page 1

Academic Editor: Luca Patanè
Received: 14 December 2025
Revised: 9 January 2026
Accepted: 13 January 2026
Published: 16 January 2026
Copyright: © 2026 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license.
Article
Tracking Control of Quadrotor UAVs with Prescribed
Performance and Prescribed-Time Convergence Under Arbitrary
Initial Conditions
Tiantian Xiao 1,2, Jinlong Guo 3,4, Jintao Chen 2, Dawei Sun 1,*, Daochun Li 1 and Jinwu Xiang 1
1
School of Aeronautical Science and Engineering, Beihang University, Beijing 100191, China;
zb2105114@buaa.edu.cn (T.X.); lidc4@buaa.edu.cn (D.L.); xiangjw@buaa.edu.cn (J.X.)
2
Department of Fundamental Theory, Qiyuan Lab, Beijing 100084, China; chenjintao@qiyuanlab.com
3
National Center of Excellence for Engineer Education, Northwestern Polytechnical University, Xi’an 710072,
China; guojinlong@mail.nwpu.edu.cn
4
Department of Unmanned System, The 208th Research Institute, Beijing 102202, China
*
Correspondence: dwsun@buaa.edu.cn
Abstract
Quadrotor unmanned aerial vehicles demonstrate broad application prospects, yet existing
research still lacks a comprehensive solution that simultaneously addresses efficiency, dis-
turbance rejection, environmental adaptability, and precision in their control performance.
To achieve prescribed-time convergence and prescribed tracking performance, this work
proposes a composite control scheme that integrates prescribed-performance control, dis-
turbance estimation, and terminal sliding-mode control. First, a prescribed-time adaptive
composite disturbance observer is developed to estimate and compensate for system com-
posite disturbances, and a stability analysis shows that the disturbance estimation error
converges to a small neighborhood of the origin within a prescribed time. Second, the
system is decomposed into position and attitude subsystems, enabling tailored hierarchical
control-law design and analysis based on their distinct dynamics. For position control,
a prescribed-performance control method is employed, incorporating a prescribed-time
performance function that accommodates large initial deviations, thereby guaranteeing
convergence of the position-tracking errors to a small neighborhood within a specified time.
For attitude control, a prescribed-time terminal sliding-mode surface and corresponding
control law are designed to eliminate singularities and ensure convergence of the attitude er-
rors to a small neighborhood within a predetermined time. The stability of both subsystems
is rigorously substantiated through theoretical analysis. Finally, comparative simulation
results confirm the effectiveness and superiority of the proposed control strategy.
Keywords: prescribed time; prescribed performance; disturbance observation; sliding
mode
1. Introduction
Quadrotor unmanned aerial vehicles (QUAVs) have demonstrated significant ap-
plication potential in various domains, including disaster rescue, package delivery, and
military reconnaissance, owing to their exceptional maneuverability and vertical take-off
and landing capabilities [1]. However, in complex real-world operational environments,
QUAVs still face substantial challenges in control efficiency, disturbance rejection, environ-
mental adaptability, and trajectory-tracking accuracy [2]. Conventional control approaches
typically focus on enhancing individual performance aspects, such as precise tracking
Electronics 2026, 15, 408
https://doi.org/10.3390/electronics15020408

## Page 2

Electronics 2026, 15, 408
2 of 21
control or disturbance-rejection-based tracking control [3]; yet, the multifaceted nature of
control performance has not been comprehensively addressed from multiple perspectives
in existing studies.
To handle the coupled nonlinear dynamics inherent in QUAV models, hierarchical
control strategies have been widely adopted. He Ming et al. [4] underscores the impor-
tance of hierarchical control architectures, providing theoretical support for the position-
loop-attitude-loop hierarchical design employed in this work. Raffo et al. [5] proposes a
backstepping-based cascaded control framework; however, its performance is highly sensi-
tive to initial conditions. Iltayed et al. [6] designs an adaptive sliding-mode hierarchical
controller, but the resulting convergence time depends on initial states, and its disturbance
attenuation capability remains limited. A critical deficiency common to existing methods is
the significant degradation of convergence performance under large initial state deviations,
which fails to meet the stringent timeliness requirements of certain application scenarios.
Recent developments in resilient UAV control have further emphasized the importance
of disturbance rejection in real-world tracking scenarios. Cui et al. [7] investigates coopera-
tive path planning for autonomous aerial vehicles in wildlife tracking applications, demon-
strating that robust coordination mechanisms are essential for maintaining performance
under communication constraints and environmental uncertainties. Xu et al. [8] proposed
an adaptive finite-time attitude tracking control scheme for quadrotors that addresses actua-
tor faults and external disturbances with guaranteed prescribed performance, highlighting
the critical need for fault-tolerant mechanisms with transient performance guarantees.
Liu et al. [9] developed secure formation control strategies for multi-agent cyber-physical
systems under denial-of-service (DoS) attacks and component faults, showing that resilient
control architectures become essential when system reliability is compromised by adver-
sarial conditions. These recent works underscore that modern UAV applications demand
control strategies that can simultaneously handle disturbances, guarantee transient perfor-
mance, and maintain robustness under adverse conditions—motivations that directly align
with the objectives of this paper.
To address the robust control problem of QUAVs, researchers have explored Prescribed-
Time Control (PTC) methods that use time-varying gain functions to guarantee system
convergence in a prescribed finite time. For instance, Polyakov et al. [10] establish a rig-
orous theoretical foundation for PTC, while Wang et al. [11] apply it to UAV control. Liu
Hao et al. [12] design a prescribed-time sliding-mode controller for both the position and
attitude loops of a quadrotor, achieving stabilization of pose within a predetermined time.
Yang Weiping [13] identifies the realization of prescribed-time convergence with guaran-
teed performance for the entire system as a key direction for future research. Meanwhile,
Prescribed Performance Control (PPC) methods [14] focus on constraining the tracking
error within prespecified bounds. Recent advances have integrated prescribed perfor-
mance with adaptive control techniques [15], demonstrating improved robustness for
nonlinear interconnected systems through event-triggered mechanisms and prespecified-
performance-driven strategies. Integrating PTC with PPC offers synergistic advantages but
also presents significant challenges: conventional PPC approaches typically employ fixed
performance bounds, rendering controller robustness sensitive to initial conditions. When
the initial tracking error is large, these bounds often need to be relaxed to avoid constraint
violations, thereby degrading transient performance [14]. Specifically, classical PPC meth-
ods require the initial condition to satisfy |zj(0)| < p(0), where zj(0) is the initial tracking
error and p(0) is the initial performance bound. This requirement cannot be guaranteed
when initial conditions are arbitrary or unknown, limiting the practical applicability of
conventional PPC in scenarios with large initial deviations.
https://doi.org/10.3390/electronics15020408

## Page 3

Electronics 2026, 15, 408
3 of 21
On the other hand, sliding-mode control (SMC) has been extensively applied to
quadrotor attitude control due to its finite-time convergence properties [16,17]. However,
traditional terminal sliding-mode control suffers from singularity issues, and its conver-
gence time depends on the initial conditions. To mitigate this, Labbadi et al. [18] proposes
a nonsingular terminal sliding-mode control method to eliminate singularities, yet the
convergence time still cannot be prescribed a priori.
Furthermore, accurate estimation and compensation of disturbances are crucial for
enhancing the robustness and tracking accuracy of UAVs. Ding Xilun et al. [19] reviews re-
cent advances in rotorcraft UAV dynamic modeling and disturbance analysis, emphasizing
that precise disturbance compensation is pivotal for improving control performance. Liao
Jian et al. [20] design a linear extended state observer (LESO) for disturbance estimation,
but its estimation accuracy and convergence speed are limited. Cao et al. [21] propose
a finite-time disturbance observer, yet its convergence characteristics depend on initial
system parameters. Wang et al. [22] develop an adaptive sliding-mode control scheme to
enhance robustness and compensate for disturbances. Liu et al. [23] proposed a fixed-time
disturbance observer-based control approach for quadcopter suspension transportation
systems, demonstrating that fixed-time convergence properties can significantly enhance
disturbance rejection performance in payload manipulation tasks with strict temporal
requirements. Such fixed-time observer techniques show promise for broader UAV control
applications in which rapid, bounded disturbance estimation is essential. Nevertheless,
within the domain of QUAV control, approaches that simultaneously account for unknown
disturbances, prescribed-time performance guarantees, and highly dynamic initial condi-
tions remain insufficiently investigated.
In summary, existing robust control methods for QUAVs share several common limita-
tions [24]: (1) sensitivity to initial conditions; (2) inefficiency in disturbance estimation and
compensation; and (3) lack of precise tracking control with prescribed-time performance
bounds. To address these challenges, this paper proposes a trajectory-tracking control
scheme for QUAVs that achieves prescribed performance within a prescribed time under
highly dynamic initial conditions and in the presence of complex disturbances. Based on a
decoupled QUAV dynamic model, we develop a prescribed-time disturbance observer, a
position-loop control law (emphasizing precise trajectory tracking), and an attitude-loop
control law (emphasizing rapid and robust stabilization). Specifically, to compensate for
disturbance effects, an adaptive composite disturbance observer with prescribed-time
convergence is designed. For position control, a novel prescribed performance function
independent of initial states is proposed based on PPC, along with its corresponding control
law. For attitude control, a prescribed-time nonsingular terminal sliding-mode surface
and its associated control law are constructed. The main contributions of this work are
as follows:
•
Initial-condition-independentprescribed performance control: A novel prescribed
performance control method that achieves performance constraint satisfaction within
a prescribed time regardless of the magnitude of initial tracking errors, addressing a
fundamental limitation of conventional prescribed performance control methods that
require the initial error to be smaller than the initial performance bound. This is real-
ized through a smooth transition function that decouples the initial error magnitude
from the performance bound, transforming the original tracking error into a scaled
variable that is inherently small at the initial instant, thereby ensuring satisfaction of
the performance constraint for arbitrary initial conditions—a capability not achievable
by standard prescribed performance control approaches and directly addressing the
robustness requirements highlighted in recent resilient UAV tracking literature [8].
https://doi.org/10.3390/electronics15020408

## Page 4

Electronics 2026, 15, 408
4 of 21
•
Prescribed-time convergent nonsingular terminal sliding-mode controller: A con-
troller that enables rapid stabilization of the attitude loop to a small neighborhood
of the origin within prescribed time. The prescribed-time convergence property is
embedded in the sliding surface design through power-law terms whose coefficients
are explicitly derived from the user-specified convergence time parameter, ensuring
that the convergence time bound is determined a priori rather than depending on the
system’s initial state.
•
Prescribed-time adaptive disturbance observer: An observer that enhances system
robustness and disturbance rejection capability with guaranteed ultimate boundedness
within a fixed time.
2. Problem Formulation and Preliminaries
The mathematical model of quadrotor UAVs is primarily based on coordinate trans-
formations and rigid-body dynamics. The dynamic model of quadrotor UAVs is given
as [25]





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





¨x = [U1(cos φ sin θ cos Ψ + sin φ sin Ψ) −Kx ˙x + fx]/m
¨y =

U1(cos φ sin θ sin Ψ −sin φ cos Ψ) −Ky ˙y + fy

/m
¨z = [U1(cos φ cos θ) −mg −Kz ˙z + fz]/m
¨φ =

U2 + (Iy −Iz) ˙θ ˙Ψ −Kφωφ + fφ

/Ix
¨θ =

U3 + (Iz −Ix) ˙φ ˙Ψ −Kθωθ + fθ

/Iy
¨Ψ =

U4 + (Ix −Iy) ˙φ ˙θ −KΨωΨ + fΨ

/Iz
(1)
where (U1, U2, U3, U4) are the motor torques that govern the three position coordinates
(x, y, z) and three attitude angles (φ, θ, Ψ) of the quadrotor UAVs; Ii(i = x, y, z) repre-
sent the moments of inertia about the x, y, and z-axes of the body coordinate system,
fi(i = x, y, z, θ, φ, Ψ) refer to disturbances; and Ki(i = x, y, z, θ, φ, Ψ) represent the aerody-
namic drag coefficients. Additionally, m represents the mass of the quadrotor, and g is the
acceleration of gravity. In the dynamic model, U1 is allocated to the displacements along
the x, y and z directions such that the entire quadrotor control system can be decomposed
into a position control system governed by U1 and an attitude control system controlled by
U2, U3 and U4. For the purpose of feedback linearization, the virtual control inputs along
the x, y and z directions
ux, uy, uz

are introduced as [25]:





ux = [U1(cos φ sin θ cos Ψ + sin φ sin Ψ)]/m
uy = [U1(cos φ sin θ sin Ψ −sin φ cos Ψ)]/m
uz = [U1(cos φ cos θ −mg)]/m
(2)
Based on the dynamic model of the quadrotor UAVs and the specified desired yaw
angle Ψd, along with the three virtual control inputs, the desired roll angle, pitch angle, and
thrust U1 can be determined as follows [20]:









U1 = m
q
u2x + u2y + (uz + g)2
φd = arcsin
h m(ux sin Ψd−uy cos Ψd)
U1
i
θd = arctan
h m(ux cos Ψd+uy sin Ψd)
m(uz+g)
i
(3)
Remark 1. To avoid domain violations in the arcsin function, saturation protection is implemented
in practice:
φd = arcsin

sat
m(ux sin Ψd −uy cos Ψd)
U1
, −0.99, 0.99

where sat(x, a, b) = max(a, min(b, x)).
https://doi.org/10.3390/electronics15020408

## Page 5

Electronics 2026, 15, 408
5 of 21
The objective of this paper is to design control laws for QUAVs achieving prescribed
performance bounds and prescribed-time satisfaction under arbitrary initial conditions. To
theoretically guarantee the robust performance of the proposed control law, the following
lemma is introduced.
Lemma 1 ([26]). For a general smooth nonlinear system in the form of
˙x = f (x), f (0) = 0, x ∈Rn
(4)
If there is a continuous function V(x) that satisfies
˙V(x) ≤−

π/γTc
p
αβ

αV(1−γ/2)(x) + βV(1+γ/2)(x)

,
(5)
where α > 0, β > 0, 0 < γ < 1 and Tc > 0, then system (4) is globally prescribed-time stable, i.e.,
V(x) converges to a small neighborhood of the origin within prescribed time TC.
Lemma 2 (Properties of Hyperbolic Tangent Function). For the hyperbolic tangent function
tanh : R →(−1, 1), the following properties hold:
(i) x tanh(x) > 0 for all x ̸= 0;
(ii) tanh(x) is strictly increasing and odd: tanh(−x) = −tanh(x);
(iii) 0 < tanh(x)
x
< 1 for all x ̸= 0;
(iv) limx→0
tanh(x)
x
= 1.
Proof. Property (i) follows from tanh(x) = ex−e−x
ex+e−x having the same sign as x.
Property (ii):
d
dx tanh(x) = sech2(x) =
4
(ex+e−x)2 > 0, and the odd property is immedi-
ate from the definition.
Property (iii): For x > 0, since e2x > 1 + 2x, we have tanh(x) = e2x−1
e2x+1 < e2x−1
2
< x.
The lower bound follows from tanh(x) > 0 for x > 0.
Property (iv) follows from L’Hôpital’s rule or the Taylor series tanh(x) = x −x3
3 +
O(x5).
3. Prescribed-Time Adaptive Composite Disturbance Observer Design
and Analysis
To effectively counteract the effect of unknown disturbances on the QUAVs, a compos-
ite disturbance observer with prescribed-time convergence and adaptive mechanisms is
introduced in this section. The observer design employs an auxiliary system (Equation (8))
that serves as a virtual reference to enable indirect disturbance estimation. By defining
the auxiliary error ei = vi −ϑi and designing its adaptive law (Equation (12)), we con-
vert the disturbance estimation problem into a stabilization problem for ˜ei, for which
prescribed-time convergence can be rigorously guaranteed via Lemma 1. This auxiliary
system technique is analogous to classical extended state observer (ESO) design but with
prescribed-time convergence guarantees.
First, note that the drone model can be rewritten as follows:
˙vi = ui + di, i = x, y, z, φ, θ, Ψ,
(6)
https://doi.org/10.3390/electronics15020408

## Page 6

Electronics 2026, 15, 408
6 of 21
where







vx = ˙x,
vy = ˙y,
vz = ˙z







vφ = ˙φ,
vθ = ˙θ,
vψ = ˙ψ







uφ = U2I−1
x ,
uθ = U3I−1
y ,
uψ = U4I−1
z







dx = fxm−1 −Kxm−1 ˙x,
dy = fym−1 −Kym−1 ˙y,
dz = fzm−1 −Kzm−1 ˙z







dφ = fφ −KφωφI−1
x ,
dθ = fθI−1
y
−KθωθI−1
y ,
dψ = fψI−1
z
−KψωψI−1
z
(7)
By defining auxiliary systems as
˙ϑi = ui + ei,
(8)
where the auxiliary error is defined as: ei = vi −ϑi, the relationship between auxiliary error
and disturbance is established as follows. Taking the time derivative of ei = vi −ϑi and
substituting Equations (6) and (8):
˙ei = ˙vi −˙ϑi = (ui + di) −(ui + ei) = di −ei
(9)
This identity is crucial for the observer design. The prescribed-time adaptive composite
disturbance observer is designed as follows [27]:
bdi = bei + ˙ei
(10)
Substituting ˙ei = di −ei:
ˆdi = ˆei + di −ei
Therefore, the observation error becomes the following:
˜di = di −ˆdi = di −(ˆei + di −ei) = ei −ˆei = ˜ei
(11)
where the adaptive law follows that
˙bei = ˙ei + a1 sign(ei)|ei|1−γ1 + a2 sign(ei)|ei|1+γ1 + a3 tanh(ei),
(12)
in which parameters satisfy the following:
a1 =
πη1/2
1
γ1T1β1/2
1
1
2
1−γ1
2
, a2 =
πβ1/2
1
γ1T1η1/2
1
1
2
1+ γ1
2
,
a3 > 0, γ1 ∈(0, 1), η1 > 0, β1 > 0
https://doi.org/10.3390/electronics15020408

## Page 7

Electronics 2026, 15, 408
7 of 21
To demonstrate the performance of the disturbance observer analytically, the adaptive
estimation error is defined as follows:
ei = ei −bei
(13)
Then, the derivative of the auxiliary error can be shown to satisfy the following:
˙ei = −a1 sign(ei)|ei|1−γ1 −a2 sign(ei)|ei|1+γ1 −a3 tanh(ei)
(14)
Now, consider candidate Lyapunov functions given as follows:
¯Vi = 1
2e2
i
(15)
The derivative of ¯Vi is as follows:
˙¯Vi = ˜ei ˙˜ei
= −a1|˜ei|2−γ1 −a2|˜ei|2+γ1 −a3 ˜ei tanh(˜ei)
(16)
By Lemma 2(i), ˜ei tanh(˜ei) ≥0 for all ˜ei ∈R. Therefore,
˙¯Vi ≤−a1|˜ei|2−γ1 −a2|˜ei|2+γ1.
(17)
Using |˜ei| = (2 ¯Vi)1/2,
˙¯Vi
≤−a1(2 ¯Vi)
2−γ1
2
−a2(2 ¯Vi)
2+γ1
2
= −a12
2−γ1
2
¯V
1−γ1
2
i
−a22
2+γ1
2
¯V
1+ γ1
2
i
(18)
By the parameter selection, we have the following:
a12
2−γ1
2
=
πη1/2
1
γ1T1β1/2
1
,
a22
2+γ1
2
=
πβ1/2
1
γ1T1η1/2
1
Therefore,
˙¯Vi ≤−
π
γ1T1
p
η1β1

η1 ¯V
1−γ1
2
i
+ β1 ¯V
1+ γ1
2
i

.
(19)
According to Lemma 1, ei converges to a small neighborhood of the origin within a
prescribed time T1 when disturbances are constant. Since edi = ei, the observer can estimate
constant composite disturbances within prescribed time T1.
Remark 2. The term −a3 ˜ei tanh(˜ei) is always non-positive by Lemma 2(i), which strictly enhances
the convergence rate. However, it does not contribute to the prescribed-time mechanism, which is
solely determined by the power terms with exponents 1 −γ1/2 and 1 + γ1/2.
Theorem 1. (Ultimate Boundedness under Time-Varying Disturbances)
Consider the disturbance observer (8)–(12) with time-varying disturbances di(t) satisfying
the following:
| ˙di(t)| ≤Dmax,
∀t ≥0
Then for any ε > 0, if a3 > 2Dmax
ε
, there exists a finite time Tε ≥T1 such that
| ˜di(t)| ≤ε,
∀t ≥Tε
https://doi.org/10.3390/electronics15020408

## Page 8

Electronics 2026, 15, 408
8 of 21
Proof. From Equation (14):
˙˜di = −a1sign( ˜di)| ˜di|1−γ1 −a2sign( ˜di)| ˜di|1+γ1 −a3 tanh( ˜di) + ˙di
Consider the set Sε = {x ∈R : |x| ≤ε}.
At the boundary | ˜di| = ε, assume without loss of generality ˜di = ε > 0:
˙˜di
 ˜di=ε ≤−a1ε1−γ1 −a2ε1+γ1 −a3 tanh(ε) + Dmax
For small ε, using Lemma 2(iv), tanh(ε) ≥ε/2 (by continuity). A sufficient condition
for Sε to be positively invariant is as follows:
a3 · ε
2 > Dmax
which gives ε > 2Dmax
a3
.
For any initial ˜d0 outside Sε, finite-time reaching is guaranteed by the dominant power
terms, with reaching time bounded by Tε −T1 ≤˜d2
0/(2δ) for some δ > 0.
4. Prescribed-Time Controller Design for QUAVs
Based on the estimate of disturbance from the aforementioned disturbance observer,
this section develops a QUAVs’ controller ensuring robust and accurate tracking with
prescribed-time performance satisfaction. The hierarchical control structure is illustrated
in Figure 1, which shows the outer position loop generating virtual controls (ux, uy, uz)
via the PPC-based controller, the coordinate transformation converting these to desired
attitude angles (φd, θd) and thrust U1, the inner attitude loop using the NTSM controller to
generate motor torques (U2, U3, U4), and the disturbance observer providing estimates ˆdi
to both controllers. (The solid line represents the real signal, and the dashed line represents
the virtual signal).
Figure 1. Overall Architecture of the Proposed Control Scheme.
https://doi.org/10.3390/electronics15020408

## Page 9

Electronics 2026, 15, 408
9 of 21
4.1. Design of Prescribed-Time and Prescribed-Performance Controller for Position Loop
First, a prescribed-time control law for position control is designed for robust tracking.
To accomplish the position system control objective, the position tracking error of the
QUAVs is defined as follows:
zx = x −xd, zy = y −yd, zz = z −zd
(20)
where

zx, zy, zz
T represents the position tracking error vector, [xd, yd, zd]T includes the
desired reference values for the three position components, and the actual output values
for the three position components are [x, y, z]T. The prescribed performance function can
be designed as follows [28]:
p(t) =
( 
p0 −t
T2

exp

1 −
t
T2−t

+ p∞, 0 ≤t < T2
p∞, t ≥T2
(21)
where p0 > 1 and p∞are design parameters, and T2 is a prescribed time parameter.
To render the prescribed performance control independent of initial conditions, the
following function is introduced [29]:
ξ =
(
ξ0 + (1 −ξ0)
1−cos( πt
T2 )
2
, t < T2
1, t ≥T2
(22)
Remark 3. The smooth cosine transition function ξ(t) with ξ(0) = ξ0 ≈0 (e.g., ξ0 = 0.001)
ensures: (1) Initial-condition decoupling: The transformed error sj1(0) = ξ0zj(0) becomes arbi-
trarily small regardless of the magnitude of zj(0), guaranteeing |sj1(0)| < p(0) for any initial
tracking error. (2) Continuity of control: The function satisfies ξ(t) ∈C∞for all t ≥0, with
˙ξ(t) = π(1−ξ0)
2T2
sin( πt
T2 ) continuous at t = T2 (where ˙ξ(T−
2 ) = 0 = ˙ξ(T+
2 )), eliminating dis-
continuities in control terms containing ˙ξ. For t < T2, while sj1 = ξzj grows with ξ(t), the
simultaneous decay of the performance bound p(t) ensures that the constraint |sj1| < p(t) is
maintained, which in turn bounds the physical error as |zj| < p(t)/ξ(t).
Then if we define





sx1 = ξzx, sx2 = ˙x −αx
sy1 = ξzy, sy2 = ˙y −αy
sz1 = ξzz, sz2 = ˙z −αz
,
(23)
it follows that their derivatives satisfy the following:





˙sx1 = ˙ξzx + ξ( ˙x −˙xd), ˙sx2 = ux + dx −˙αx
˙sy1 = ˙ξzy + ξ( ˙y −˙yd), ˙sy2 = uy + dy −˙αy
˙sz1 = ˙ξzz + ξ( ˙z −˙zd), ˙sz2 = uz + dz −˙αz
.
(24)
Note that if the control law is designed such that
−p(t) < sj1 < p(t), j = x, y, z
(25)
it follows from ξ(0) = ξ0 ≈0 that sj1(0) = ξ0zj(0) ≈0, which implies that −p(0) <
sj1(0) < p(0) can be satisfied regardless of the value of zj(0), and after T2, sj = ξzj always
holds true.
https://doi.org/10.3390/electronics15020408

## Page 10

Electronics 2026, 15, 408
10 of 21
To achieve the desired performance constraints, consider candidate Lyapunov func-
tions with barriers designed as follows [29]:
Vj1 = 1
2 ln
p2
p2 −s2
j1
, (j = x, y, z).
Lemma 3 (Boundedness of barrier Lyapunov function components). For the barrier Lyapunov
function Vj1 = 1
2 ln
p2
p2−s2
j1 with |sj1| < p, the following properties hold:
(i) The normalized error satisfies the following:
s2
j1
p2 −s2
j1
≥2Vj1
(ii) When |sj1| < p, there exist positive constants ℓj and ℓj such that
ℓj ≤

sj1
p2 −s2
j1
 ≤ℓj.
(iii) For the performance function p(t) defined in (21), there exists a constant Mp > 0
such that

˙p(t)
p(t)
 ≤Mp,
∀t ≥0.
Proof. (i) From the definition, e2Vj1 =
p2
p2−s2
j1 , which yields the following:
p2 −s2
j1 = p2e−2Vj1
Therefore,
s2
j1
p2 −s2
j1
=
p2 −(p2 −s2
j1)
p2 −s2
j1
= e2Vj1 −1 ≥2Vj1
where the last inequality follows from ex ≥1 + x for all x ∈R.
(ii) Since |sj1| < p is maintained by the barrier, and p(t) ≥p∞> 0, the function
ℓj(t) =
sj1
p2−s2
j1 is bounded.
(iii) Computing ˙p(t) from (20) for t < T2:
˙p(t) = −1
T2
exp

1 −
t
T2 −t

+ (p0 −t
T2
) exp

1 −
t
T2 −t

·
T2
(T2 −t)2 .
Since p(t) ≥p∞, the ratio | ˙p/p| remains bounded for all t ≥0.
It follows that
˙Vj1
=
sj1
p2−s2
j1
˙sj1 −˙psj1/p

= ℓj
 ˙ξzj + ξ
sj2 + αj −˙jd
 −˙psj1/p

= ℓjξ
sj2 + αj −˙jd
 + ℓj
 ˙ξzj −˙psj1/p

,
(26)
where ℓj =
sj1
p2−s2
j1 .
According to Young’s inequality, for any λj > 0, we have the following:
−ℓj ˙psj1/p ≤
ℓ2
j s2
j1
2λj
˙p2
p2 + λj
2
https://doi.org/10.3390/electronics15020408

## Page 11

Electronics 2026, 15, 408
11 of 21
By Lemma 3(ii) and (iii), there exists ρj1 > 0 such that
ℓ2
j s2
j1
2λj
˙p2
p2 ≤ρj1
for all t ≥0 and all |sj1| < p.
By plugging it into (26), we can obtain the following:
˙Vj1 ≤ℓjξ
 
sj2 + αj −˙jd +
ℓjξz2
j
2λj
˙p2
p2
!
+ ρj1 + λj
2 + ℓj ˙ξzj
(27)
By designing the position loop virtual control rate as
αj = −µj1sj1 + ˙jd −
ℓjξz2
j
2λj
˙p2
p2 ,
(28)
where µj1 is the regularization parameter, it follows from (27) that
˙Vj1 ≤−µj1ξ
s2
j1
p2 −s2
j1
+ ρj1 + λj
2 + ℓjξsj2 + ℓj ˙ξzj.
To further design the stabilizing control law, let us consider candidate Lyapunov
functions given as Vj2 = Vj1 + 1
2s2
j2, whose derivatives satisfy the following:
˙Vj2 = ˙Vj1 + sj2 ˙sj2 = ˙Vj1 + sj2
uj + dj −˙αj

(29)
To eliminate the problematic singular term, we employ the following continuous
approximation. Note that
ℓj ˙ξzjsj2 = ℓj ˙ξzjsj2 ·
s2
j2 + δ2
j
s2
j2 + δ2
j
,
where δj > 0 is a small design parameter. This allows us to write the following:
ℓj ˙ξzj = ℓj ˙ξzj ·
sj2
s2
j2 + δ2
j
· sj2
The control law is thus designed as follows:
uj = −µj2sj2 −bdj + ˙αj −ℓjξ −ℓj ˙ξzj
sj2
s2
j2 + δ2
j
,
(30)
where µj2(j = x, y, z) is the regularization parameter and δj > 0 is a small positive constant
that prevents singularity when sj2 →0.
Remark 4. The continuous approximation
sj2
s2
j2+δ2
j ensures the following: (1) The control law remains
bounded for all sj2, including sj2 = 0; (2) When |sj2| ≫δj, the approximation
sj2
s2
j2+δ2
j ≈s−1
j2
closely matches the original design intent; (3) The approximation error ℓj ˙ξzj
δ2
j
s2
j2+δ2
j is uniformly
bounded and can be made arbitrarily small by choosing δj sufficiently small, while maintaining
control continuity.
https://doi.org/10.3390/electronics15020408

## Page 12

Electronics 2026, 15, 408
12 of 21
Theorem 2. Consider the quadrotor UAV position subsystem described by (6) with the prescribed-
time disturbance observer (8)–(12) and the position control law (19)–(30). Suppose the following
conditions hold:
1. The desired trajectory is bounded and twice differentiable;
2. The observer parameters satisfy α > 0, β > 0, 0 < γ < 1;
3. The controller parameter p0 > 1;
4. The prescribed time parameters satisfy T1 > 0, T2 > 0; and the approximation parameter
δj > 0.
Then, the position tracking error converges to a small neighborhood of the prescribed perfor-
mance bounds within the prescribed time, specifically: (i) the performance constraint |sj1(t)| < p(t)
is satisfied for all t ≥0, ensuring |zj(t)| < p(t)/ξ(t); and (ii) for t ≥T2, the system exhibits
exponential ultimate boundedness with |zj(t)| ≤p∞+ O(
q
Θj/µj), where the bound Θj depends
on disturbance observation error, control approximation error, and performance function derivative.
Remark 5. The term “arbitrary initial conditions” in this paper refers to a theoretical framework
where the control method can handle a wide range of initial states. In practical UAV applications,
the initial conditions are naturally constrained by physical limitations. Therefore, “arbitrary initial
conditions” should be interpreted as “high-redundancy initial conditions”.
Proof. Substituting the control law (30) into (29):
˙Vj2
≤−µj1ξ
s2
j1
p2−s2
j1 −µj2s2
j2 + ρj1 +
λj
2 + ℓj ˙ξzj
δ2
j
s2
j2+δ2
j + sj2 ˜dj
(31)
Using Young’s inequality on sj2 ˜dj:
sj2 ˜dj ≤
s2
j2
2ϵj
+
ϵj ˜d2
j
2
and noting that
δ2
j
s2
j2+δ2
j ≤1 and by Lemma 3(ii) |ℓj| ≤ℓj, we have the following:
ℓj ˙ξzj
δ2
j
s2
j2 + δ2
j
≤ℓj| ˙ξ||zj| ≤ρj2
for some constant ρj2 > 0 (since ˙ξ and zj remain bounded in the closed-loop system).
Therefore,
˙Vj2 ≤−µj1ξ
s2
j1
p2 −s2
j1
−
 
µj2 −1
2ϵj
!
s2
j2 + Θj,
(32)
where Θj = ρj1 + ρj2 +
λj
2 +
ϵjD2max
2
(using the bound from Theorem 1 on | ˜dj| ≤ε for
sufficiently large t).
By Lemma 3(i):
˙Vj2
≤−2µj1ξVj1 −

µj2 −
1
2ϵj

s2
j2 + Θj
≤−µjVj2 + Θj
(33)
where µj = min
n
2µj1ξmin, 2

µj2 −
1
2ϵj
o
> 0 (provided µj2 >
1
2ϵj , which can be satisfied
by design), and ξmin = ξ0 > 0 is the minimum value of ξ(t). By integrating both sides
of (33), we have the following:
https://doi.org/10.3390/electronics15020408

## Page 13

Electronics 2026, 15, 408
13 of 21
Vj2 ≤
 
Vj2(0) −Θj
µj
!
exp
−µjt
 + Θj
µj
(34)
By substituting the aforementioned expression into Equation (33), it can be inferred
that ˙Vj2 ≤0. Since
Vj2 = Vj1 + (1/2)sj22 = (1/2) ln

p2/
p2 −sj12 + 1/2sj22
≤Ae(−µjt) + B,
where A = Vj2(0) −
Θj
µj , B =
Θj
µj , then
ln
h
p2/

p2 −s2
j1
i
≤2Ae(−µjt) + 2B
p2/

p2 −s2
j1

≤e2Ae(−µjt)+2B
C(t)sj12 ≤(C(t) −1)p2
in which C(t) = e2Ae(−µjt)+2B. Therefore, sj12 ≤p2. In this case, prescribed performance
−p(t) < sj1 < p(t) holds, and the system states converge to a small neighborhood of the
origin.
Remark 6. (Clarification on Performance Satisfaction)
The proposed method achieves two distinct aspects:
(i) Prescribed-time performance constraint satisfaction: The barrier Lyapunov function guaran-
tees |sj1(t)| < p(t) for all t ≥0, where p(t) decreases from p0 to p∞within time T2. This ensures
the physical tracking error satisfies |zj(t)| < p(t)/ξ(t), achieving bounded tracking within the
prescribed time T2 regardless of initial conditions.
(ii) Exponential ultimate boundedness: The inequality ˙Vj2 ≤−µjVj2 + Θj (Equation (33))
yields exponential convergence to an ultimate bound limt→∞Vj2(t) ≤Θj/µj, rather than exact
convergence to zero. The bound Θj arises from three sources: (a) disturbance observation error
| ˜dj| ≤ε (Theorem 1), (b) continuous approximation error ρj2 from the term δ2
j /(s2
j2 + δ2
j ) (Equation
(30)), and (c) performance function derivative bound ρj1 (Lemma 3).
(iii) Engineering rationale for p∞> 0: Setting p∞= 0 would theoretically require infinite
control gains at t = T2, which is impractical given actuator saturation. The design choice p∞> 0
provides the following: (a) bounded control effort, (b) robustness to persistent disturbances and
modeling uncertainties, and (c) adjustable steady-state accuracy through parameter tuning (a3, δj,
ϵj, µj). The ultimate bound can be made arbitrarily small by appropriate parameter selection.
4.2. Design of Sliding Mode Controller for Prescribed-Time Attitude Loop
Considering the characteristics of the QUAV’s attitude dynamics, applying a
prescribed-time terminal sliding mode controller that is different from the controller
used for the position loop can be more effective for rapid and robust stabilization of
the attitude loop.
To design and analyze the controller, the errors in attitude tracking of a quadrotor
UAV are defined as follows:
zφ = φ −φd, zθ = θ −θd, zΨ = Ψ −Ψd,
(35)
https://doi.org/10.3390/electronics15020408

## Page 14

Electronics 2026, 15, 408
14 of 21
where [φd, θd, Ψd]T is the reference attitude input vector, and [φ, θ, Ψ]T is the actual output
attitude angle information. The derivatives of errors in (35) can be obtained by the following:
˙zφ = ˙φ −˙φd, ˙zθ = ˙θ −˙θd, ˙zΨ = ˙Ψ −˙Ψd
(36)
where
 ˙zφ, ˙zθ, ˙zΨ
T,
 ˙φd, ˙θd, ˙Ψd
T, and
 ˙φ, ˙θ, ˙Ψ
T represent the derivatives of

zφ, zθ, zΨ
T,
[φd, θd, Ψd]T, and [φ, θ, Ψ]T, respectively.
The prescribed-time non-singular terminal sliding mode surface for the attitude control
system is designed as [26]:
sk = ˙zk + b1 sign(zk)|zk|1−γ2 + b2 sign(zk)|zk|1+γ2(k = φ, θ, Ψ)
(37)
where the parameters satisfy the following:
b1 =
πη1/2
2
γ2T3β1/2
2

1
2
1−γ2
2 , b2 =
πβ1/2
2
γ2T3η1/2
2

1
2
1+ γ2
2 ,
γ2 ∈(0, 1), η2 > 0, β2 > 0.
Remark 7. The prescribed-time property is directly embedded in the sliding surface design
(Equation (37)) through the power-law coefficients b1 and b2, which are explicitly functions of
the prescribed time T3. Specifically, when the system reaches the sliding surface sk = 0, the
dynamics become the following:
˙zk + b1sign(zk)|zk|1−γ2 + b2sign(zk)|zk|1+γ2 = 0
The above formulation for the sliding mode surface structure, combined with the specific
parameter selection of b1 and b2, guarantees convergence from any point on the sliding surface to a
neighborhood of the origin within time T3, as proven in Theorem 3.
It can be derived that
˙sk = uk + dk −¨kd + ςk ˙zk,
(38)
where ςk = (1 −γ2)b1|zk|−γ2 + (1 + γ2)b2|zk|γ2.
To design the control law and guarantee stability, consider candidate Lyapunov functions
defined as Vk = 1
2s2
k, k = φ, θ, Ψ. The derivatives of these functions satisfy the following:
˙Vk = sk
uk + dk −¨kd + ςk ˙zk

(39)
Now, we are motivated to design the observer-based sliding mode controller as follows:
uk = Ij



−c1 sign(sk)|sk|1−γ3−
c2 sign(sk)|sk|1+γ3
−c3sk −bdk + ¨kd −ςk ˙zk



(40)
where the parameters satisfy the following:
c1 =
πη1/2
3
γ3T3β1/2
3

1
2
1−γ3
2 , c2 =
πβ1/2
3
γ3T3η1/2
3

1
2
1+ γ3
2 ,
c3 > 0, γ3 ∈(0, 1), η3 > 0, β3 > 0.
The stability property of the proposed attitude control law is demonstrated in the
following theorem.
https://doi.org/10.3390/electronics15020408

## Page 15

Electronics 2026, 15, 408
15 of 21
Theorem 3. Consider the quadrotor UAV attitude subsystem (35) and (36), with the prescribed-
time non-singular terminal sliding-mode surface (37) and the attitude control law (40). Suppose the
following conditions hold:
1. The desired attitude trajectories are bounded and differentiable;
2. The observer parameters satisfy α > 0, β > 0, 0 < γ < 1;
3. The sliding mode surface parameters satisfy γ2 ∈(0, 1), η2 > 0, β2 > 0, and the controller
parameters satisfy c3 > 0, γ3 ∈(0, 1), η3 > 0, β3 > 0.
4. The prescribed time parameters satisfy T1 > 0, T3 > 0.
Then the attitude tracking error vector converges to a small neighborhood of the origin within
the prescribed time, specifically: the sliding variable sk(t) reaches a neighborhood of zero within
time T3, and consequently zk(t) is ultimately bounded with O(
p
ϵkε2/c3) for t ≥T3, where ε is
the disturbance observation bound from Theorem 1.
Proof. Substituting (40) into (39) and using ˜dk = dk −ˆdk:
˙Vk = sk(−c1sign(sk)|sk|1−γ3 −c2sign(sk)|sk|1+γ3 −c3sk + ˜dk)
(41)
Using Young’s inequality on sk ˜dk:
sk ˜dk ≤s2
k
2ϵk
+ ϵk ˜d2
k
2
Therefore,
˙Vk
≤−c1|sk|2−γ3 −c2|sk|2+γ3 −

c3 −
1
2ϵk

s2
k + ϵkε2
2
≤−c1(2Vk)
2−γ3
2
−c2(2Vk)
2+γ3
2
−

c3 −
1
2ϵk

2Vk + ϵkε2
2 ,
(42)
where we used the observer bound | ˜dk| ≤ε from Theorem 1 for sufficiently large t.
For the appropriate choice of ϵk such that c3 >
1
2ϵk , the dominant terms yield the
following:
˙Vk ≤−
π
γ3T3
p
η3β3

η3V
1−γ3
2
k
+ β3V
1+ γ3
2
k

+ ϵkε2
2 .
(43)
According to Lemma 1, the system state vector reaches a small neighborhood of the
sliding mode surface within a prescribed time T3. Hence, the control system can converge
to a small neighborhood of the origin within prescribed time T = max{T1, T2, T3}.
Remark 8. The ultimate bounds in both position and attitude loops can be made arbitrarily small
by: (1) Increasing the observer gain a3 to reduce ε; (2) Reducing the approximation parameter δj
in the position controller; (3) Adjusting ϵj and ϵk to balance convergence rate and steady-state
accuracy. In practice, these parameters are tuned to achieve desired tracking performance while
maintaining control smoothness.
5. Numerical Experiments
To verify the effectiveness of the proposed control method, simulations are carried out
with designed parameters given in Table 1. Results show that the method in this paper can
solve the trajectory tracking problem under composite disturbances within a prescribed
time. As shown in Figure 2, the QUAV used in the simulation is able to track the desired
trajectory by utilizing the control method proposed in this paper. Figure 3 shows that the
position error converges to a small neighborhood of the origin within the user’s prescribed
time, and Figure 4 shows that the attitude error converges to a small neighborhood of
the origin within the prescribed time as well. It can be seen that the proposed method
https://doi.org/10.3390/electronics15020408

## Page 16

Electronics 2026, 15, 408
16 of 21
exhibits superior convergence accuracy when handling large initial deviations and strong
composite disturbances, and that the convergence time constraints and robust stability are
strictly satisfied. Figure 5 depicts the control inputs signals of position and altitude. The
applied disturbances are matched (directly added to control channels via Equation (1)),
time-varying (containing periodic sinusoidal components), and bounded with magnitude
| fi(t)| ≤0.2 for all channels. The disturbance model fi = 0.1 sin(0.01t) sin(0.1t) + 0.1 sin(i)
captures both slow-varying environmental effects (wind gusts with 0.01 Hz modulation)
and high-frequency oscillations (sensor noise at 0.1 Hz), representing realistic operational
conditions for small quadrotors.
Figure 2. Trajectory tracking performance.
Figure 3. Prescribed-time convergence curve of the position error.
https://doi.org/10.3390/electronics15020408

## Page 17

Electronics 2026, 15, 408
17 of 21
Figure 4. Prescribed-time convergence curve of the attitude error.
Figure 5. Control inputs performance.
https://doi.org/10.3390/electronics15020408

## Page 18

Electronics 2026, 15, 408
18 of 21
Table 1. Simulation parameters.
Parameters
Value
Simulation
m = 2, Ix = Iy = 1.24, Iz = 2.5,
Parameters
Kx = Ky = Kz = Kφ = Kθ = Kψ = 0.01
Disturbance
fi = 0.1 sin(0.01t) sin(0.1t) + 0.1 sin(i)
Type: Matched, time-varying, bounded
Magnitude: | fi(t)| ≤0.2 for all i
Reference signal
xd = 5 sin(t), yd = 5 cos(t), zd = t, φd = π/3
Initial state
x = −4, y = 8.5, z = −0.5,
φ = 0.1, θ = −0.2, ψ = 0.3
Prescribed time
T1 = 1, T2 = 3, T3 = 1
PPC function parameters
p0 = 1.1, p∞= 0.15, ξ0 = 0.001
Observer parameters
γ1 = 0.5, η1 = 0.1, β1 = 0.5, a3 = 5
Controller parameters
µj1 = 30, µj2 = 35, λj = 50, δj = 0.01,
γ2 = 0.3, η2 = 0.1, β2 = 2,
γ3 = 0.3, η3 = 6, β3 = 5, b3 = 20
5.1. Results Analysis
The actual position trajectories (x, y, z) closely follow their references (xd, yd, zd) after
the transient period, with steady-state errors remaining below the prescribed bounds.
Similarly, the attitude angles (φ, θ, ψ) track their desired values with errors converging to
small neighborhoods. These tracking accuracies are adequate for typical autonomous flight
missions such as waypoint navigation and trajectory following.
This paper conducts a comparative analysis of four different methods (results are
shown in Figures 6 and 7): PID control, terminal sliding mode control with extended state
observer (TSMC-ESO), combination of prescribed performance control with extended state
observer (PPC-ESO), and the method proposed in this paper (PTC-PPC-TSMC-ESO). It can
be observed that the PID controller is insufficient to control the system in the presence of
time-varying disturbances. The TSMC-ESO method exhibits suboptimal performance in
the position loop control, but it can converge quickly in the attitude loop; however, the use
of a sign function in the switching rate causes oscillations about the origin. The PPC-ESO
method performs well in position loop control, but in the attitude loop, the convergence
rate is unsatisfactory, and the states exhibit large fluctuations. Based on the comparison, the
proposed method, which combines PPC, PTC, TSMC, and ESO, can significantly mitigate
the shortcomings of the aforementioned methods, leading to substantial improvements in
QUAV control under disturbances.
Figure 6. Position tracking error curves of the four methods.
https://doi.org/10.3390/electronics15020408

## Page 19

Electronics 2026, 15, 408
19 of 21
Figure 7. Attitude tracking error curves of the four methods.
5.2. Limitations and Future Directions
Despite the theoretical contributions and promising simulation results, several limita-
tions of the proposed method should be acknowledged:
1. Need for systematic parameter tuning guidelines: The method involves the adjust-
ment of over a dozen parameters across the observer and controllers. Although effective
parameter sets have been demonstrated in simulation, systematic and efficient tuning
strategies for different quadrotor platforms and mission profiles require further study and
clear guidelines to facilitate practical deployment.
2. Higher real-time computational demand: The real-time computation of the dis-
turbance observer and the derivatives of the barrier Lyapunov function imposes greater
processing requirements compared to conventional PID controllers. Deployment on em-
bedded hardware with sufficient computing power is necessary to maintain control rates
above 100 Hz.
3. Dependence on model parameters: The control design relies on accurate model
parameters such as moments of inertia Ix, Iy, Iz and drag coefficients Ki. While the distur-
bance observer enhances robustness to parametric uncertainties to some extent, control
performance may still degrade when model errors are significant (e.g., exceeding ±20%).
Future research directions:
•
Experimental validation: Hardware-in-the-loop (HIL) testing and flight experiments
on physical quadrotor platforms to validate control performance under real-world
conditions, including sensor noise, actuator delays, and aerodynamic effects.
•
Adaptive parameter tuning: Development of online learning algorithms (e.g., rein-
forcement learning or adaptive control) to automatically adjust controller gains based
on flight conditions and disturbance characteristics.
•
Extension to multi-UAV systems: Application of the proposed framework to coopera-
tive control of heterogeneous multi-UAV formations with communication constraints,
as motivated by recent work on resilient distributed control [9].
•
Integration with perception systems: Combination of the proposed control with vision-
based state estimation and obstacle avoidance for fully autonomous navigation in
GPS-denied environments.
https://doi.org/10.3390/electronics15020408

## Page 20

Electronics 2026, 15, 408
20 of 21
These directions aim to bridge the gap between theoretical advances and prac-
tical deployment, ultimately enabling prescribed-performance control in real-world
UAV applications.
6. Conclusions
This article addresses the tracking control problem for QUAVs subject to unknown
disturbances and large initial-state deviations by proposing a control method that inte-
grates prescribed-performance control, prescribed-time control, a disturbance observer,
and prescribed-time nonsingular sliding-mode control. The proposed method achieves
prescribed-time satisfaction of performance constraints while ensuring exponential ulti-
mate boundedness in the presence of persistent disturbances. Specifically, the position
controller guarantees that tracking errors remain within prescribed bounds for all time,
and the attitude controller ensures rapid convergence to a small neighborhood of the origin
within prescribed time. A comparative analysis using simulations has been presented to
demonstrate that the proposed method can not only rigorously achieve the prescribed-time
convergence of position and attitude errors to small neighborhoods with the desired accu-
racy but also exhibit desirable performance under unknown disturbances and large initial
deviations, significantly improving the trajectory-tracking accuracy and mission reliability
of QUAVs.
Author Contributions: Conceptualization, T.X. and J.X.; methodology, T.X.; software, J.G.; validation,
J.C., D.S. and D.L.; formal analysis, J.C.; resources, T.X.; writing—original draft preparation, T.X.;
writing—review and editing, D.S.; visualization, J.G.; supervision, D.L.; project administration, D.S.
All authors have read and agreed to the published version of the manuscript.
Funding: The paper is supported by the National Key Laboratory of Micro-Spacecraft Rapid Design
and Intelligent Cluster [Funding Number: MS01240124] and National Natural Science Foundation of
China [Grant Numbers: 62403032].
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Written informed consent has been obtained from the authors to
publish this paper.
Data Availability Statement: The original contributions presented in this study are included in the
article. Further inquiries can be directed to the corresponding author.
Conflicts of Interest: The authors declare no conflicts of interest.
References
1.
Arafat, M.Y.; Alam, M.M.; Moh, S. Vision-Based Navigation Techniques for Unmanned Aerial Vehicles: Review and Challenges.
Drones 2023, 7, 89. [CrossRef]
2.
Mahony, R.; Kumar, V.; Corke, P. Multirotor aerial vehicles: Modeling, estimation, and control of quadrotor. IEEE Robot. Autom.
Mag. 2012, 19, 20–32. [CrossRef]
3.
Lee, T.; Leok, M.; McClamroch, N.H. Geometric tracking control of a quadrotor UAV on SE (3). In Proceedings of the 49th
IEEE Conference on Decision and Control (CDC), Atlanta, GA, USA, 15–17 December 2010; IEEE: Atlanta, GA, USA, 2010;
pp. 5420–5425.
4.
He, M.; Chen, H.; Han, W.; Deng, C.; Duan, H. Development status and key technologies of cooperative control of bird-inspired
UAV swarms. Acta Aeronaut. Astronaut. Sin. 2024, 45, 29946.
5.
Raffo, G.V.; Ortega, M.G.; Rubio, F.R. An integral predictive/nonlinear H∞control structure for a quadrotor helicopter. Automatica
2010, 46, 29–39. [CrossRef]
6.
Eltayeb, A.; Rahmat, M.F.; Basri, M.A.M.; Eltoum, M.M.; Mahmoud, M.S. Integral adaptive sliding mode control for quadcopter
UAV under variable payload and disturbance. IEEE Access 2022, 10, 94754–94764. [CrossRef]
7.
Cui, Y.; Chen, J.; Lin, H.; Yang, X.; Meng, M.Q.H. Cooperative Multi-AAV Path Planning for Discovering and Tracking Multiple
Radio-Tagged Targets. IEEE Trans. Syst. Man Cybern. Syst. 2025, 55, 2463–2475. [CrossRef]
https://doi.org/10.3390/electronics15020408

## Page 21

Electronics 2026, 15, 408
21 of 21
8.
Xu, G.; Xia, Y.; Zhai, D.H.; Lyu, W. Adaptive Finite-Time Attitude Tracking Control of Quadrotor Under Actuator Faults and
External Disturbances with Guaranteed Performance. Int. J. Adapt. Control Signal Process. 2022, 36, 2662–2676. [CrossRef]
9.
Liu, Y.; Dong, X.; Ren, Z.; Liu, J. Secure Formation Control for Resilient Multi-Agent Cyber-Physical Systems Under DoS Attacks
and Faults. Int. J. Robust Nonlinear Control 2023, 33, 3607–3626. [CrossRef]
10.
Polyakov, A. Nonlinear feedback design for fixed-time stabilization of linear control systems. IEEE Trans. Autom. Control 2011,
57, 2106–2110. [CrossRef]
11.
Wang, T.; Ning, W.; Sun, Z.; Xia, Y. Prescribed-Time Trajectory Tracking Control for Quadrotor Without Velocity Measurement.
IEEE/ASME Trans. Mechatron. 2025, 30, 5940–5951. [CrossRef]
12.
Liu, H.; Huang, S.; Tu, H. Quadrotor sliding mode control based on predefined time. J. Beijing Univ. Aeronaut. Astronaut. 2022,
50, 1665–1674.
13.
Yang, W. Development trend of navigation guidance and control technology for new generation aircraft. Acta Aeronaut. Astronaut.
Sin. 2024, 45, 529720.
14.
Wu, Y.; Hu, L.; Liu, L.; Zhang, Y.; Zhang, Y. Finite time prescribed performance control for stochastic systems with asymmetric
error constraint and actuator faults. Commun. Nonlinear Sci. Numer. Simul. 2024, 139, 108290. [CrossRef]
15.
Zhang, L.; Deng, C.; Che, W.W. Adaptive Backstepping Control for Nonlinear Interconnected Systems with Prespecified-
Performance-Driven Output Triggering. Automatica 2023, 154, 111063. [CrossRef]
16.
Zhao, Z.; Xiao, L.; Jiang, B.; Cao, D. Fast nonsingular terminal sliding mode trajectory tracking control of a quadrotor UAV based
on extended state observers. Control Decis. 2022, 37, 2201–2210.
17.
Wu, Y.; Zheng, B.; Li, H. Attitude controller for quadrotor via active disturbance rejection control and sliding mode control.
Electron. Opt. Control 2022, 29, 93–98.
18.
Labbadi, M.; Cherkaoui, M. Adaptive fractional-order nonsingular fast terminal sliding mode based robust tracking control of
quadrotor UAV with Gaussian random disturbances and uncertainties. IEEE Trans. Aerosp. Electron. Syst. 2021, 57, 2265–2277.
[CrossRef]
19.
Ding, X.; Jin, X. Research progress of rotorcraft UAV interactive manipulation dynamic modeling. Acta Aeronaut. Astronaut. Sin.
2024, 43, 527388.
20.
Liao, J.; Gao, X.; Yan, S.; Zhou, S.; Wang, D.; Kang, Y. Formation reconfiguration control of UAV swarm based on MPC-PIO.
J. Beijing Univ. Aeronaut. Astronaut. 2022, 50, 1541–1550.
21.
Cao, P.; Gan, Y.; Dai, X. Finite-time disturbance observer for robotic manipulators. Sensors 2019, 19, 1943. [CrossRef]
22.
Wang, J.; Zhao, L.; Yu, L. Adaptive terminal sliding mode control for magnetic levitation systems with enhanced disturbance
compensation. IEEE Trans. Ind. Electron. 2020, 68, 756–766. [CrossRef]
23.
Liu, W.; Chen, M.; Shi, P. Fixed-Time Disturbance Observer-Based Control for Quadcopter Suspension Transportation System.
IEEE Trans. Circuits Syst. I Regul. Pap. 2022, 69, 4632–4642. [CrossRef]
24.
Jia, T.; Yan, H.; Zhang, H.; Li, H.; Zhang, Y. Adaptive anti-disturbance performance guaranteed formation tracking control for
quadrotor UAVs via aperiodic signal updating. IEEE Trans. Syst. Man Cybern. Syst. 2024, 54, 5212–5223. [CrossRef]
25.
Bouabdallah, S.; Siegwart, R. Backstepping and sliding-mode techniques applied to an indoor micro quadrotor. In Proceedings of
the 2005 IEEE International Conference on Robotics and Automation, Barcelona, Spain, 18–22 April 2005; IEEE: Barcelona, Spain,
2005; pp. 2247–2252.
26.
Yao, Q.; Li, Q.; Huang, M.; Jahanshahi, H. Predefined-time trajectory tracking control of free-flying space manipulator subject to
uncertainties and disturbances. Robot. Auton. Syst. 2024, 177, 104699. [CrossRef]
27.
Liu, K.; Wang, R.; Zheng, S.; Dong, S.; Sun, G. Fixed-time disturbance observer-based robust fault-tolerant tracking control for
uncertain quadrotor UAV subject to input delay. Nonlinear Dyn. 2022, 107, 2363–2390. [CrossRef]
28.
Liu, C. Research on Adaptive Tracking Control of a Climbing Robot for Wooden Columns. Ph.D. Thesis, Shandong Jianzhu
University, Jinan, China, 2020.
29.
Yin, C.; Wu, Q.; Yang, S.; Zhou, C. Guaranteed performance predefined time Control for manipulator with arbitrary initial state.
Modul. Mach. Tool Autom. Manuf. Tech. 2025, 2025, 103–108, 113.
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.
https://doi.org/10.3390/electronics15020408
