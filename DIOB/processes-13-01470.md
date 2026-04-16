# processes-13-01470.pdf

## Page 1

Academic Editors: Yuanqiang Zhou,
Le Yao, Xiaoyu Jiang and Zheren Zhu
Received: 15 March 2025
Revised: 5 May 2025
Accepted: 7 May 2025
Published: 12 May 2025
Citation:
Xu, G.; Luo, S.; Huang, Y.;
Deng, X. Extended State Observer
Based Robust Nonlinear PID Attitude
Tracking Control of Quadrotor with
Lumped Disturbance. Processes 2025,
13, 1470. https://doi.org/10.3390/
pr13051470
Copyright: © 2025 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license
(https://creativecommons.org/
licenses/by/4.0/).
Article
Extended State Observer Based Robust Nonlinear PID Attitude
Tracking Control of Quadrotor with Lumped Disturbance
Gang Xu *
, Shengping Luo
, Yiqing Huang
and Xiongfeng Deng
Key Laboratory of Advanced Perception and Intelligent Control of High-End Equipment, Ministry of Education,
Anhui Polytechnic University, Wuhu 241000, China; luoshengping@ahpu.edu.cn (S.L.);
yiqhuang@ahpu.edu.cn (Y.H.); dengxiongfeng@ahpu.edu.cn (X.D.)
* Correspondence: xu_gang@ahpu.edu.cn
Abstract: The paper presents a robust nonlinear PID controller for the attitude tracking
problem of quadrotors subject to disturbance. First, to suppress the influence caused by
external disturbance torque, considering the fact that the angular velocity can be obtained
by the inertial measurement unit (IMU), a reduced-order extended state observer (ESO) is
applied as a feedforward compensation to improve the robustness of the tracking system.
Then, an ESO-based nonlinear PID controller is constructed to track the desired attitude
command, and the rigorous proof of the convergence of the closed-loop system is derived
by utilizing the Lyapunov method. Finally, the effectiveness of the proposed method is
illustrated by numerical simulations and platform experiments.
Keywords: quadrotor; nonlinear PID control; disturbance rejection; real-time experiments
1. Introduction
Quadrotor unmanned aerial vehicles (UAVs) have become increasingly vital across a
spectrum of applications, including aerial surveillance, inspection, precision agriculture,
and disaster response, owing to their vertical take-off and landing (VTOL) capabilities, me-
chanical simplicity, and high maneuverability [1–3]. However, their practical deployment
remains constrained by inherent challenges such as strong nonlinear dynamics, under-
actuation, and high sensitivity to environmental disturbances like wind gusts, payload
variations, and sensor noise. These limitations underscore the critical importance of robust
and precise attitude control for achieving stable and reliable flight performance.
Traditionally, PID controllers have been the choice for attitude stabilization due to
their simplicity and ease of implementation [4]. In [5], the PID algorithm-based flight
control was constructed for a quadrotor to study the dynamic control performance under
different wind scenarios. To improve the quadrotor control performance, the feedback
linearization combined with PID was proposed in [6]. However, in view of disadvantages
of linear PID as mentioned in [7], the exploitation of nonlinear PID has further gained
interest of researchers [8–12]. In [8], by using error scaling in the integral operation, the
nonlinear PID controller for attitude stabilization was developed. To address time and state
constraint problem of a quadrotor, a finite-time stability scheme with implicit PID controller
was developed in [9]. In [10], a nonlinear PID controller was proposed for a quadrotor to
track the given trajectory with minimum energy, and the parameters were tuned by genetic
algorithm. In [11], motion control of a quadrotor was achieved by utilizing the designed
nonlinear PID-type controller; the rigorous theoretical analysis of the closed-loop system
and gain tuning guidelines were provided. Nevertheless, one persistent shortcoming across
both linear and nonlinear PID approaches is their passive disturbance rejection. While some
Processes 2025, 13, 1470
https://doi.org/10.3390/pr13051470

## Page 2

Processes 2025, 13, 1470
2 of 20
robustness is inherently built into controller structures, explicit disturbance estimation and
compensation remain underexplored. This is particularly critical given that real-world
disturbances can be nontrivial and unpredictable.
To address this, recent attention has shifted towards disturbance observer (DOB)
and extended state observer (ESO) [13–16], which actively estimate and compensate for
lumped disturbances—comprising model uncertainties, sensor noise, and environmental
forces. DOBs have been shown to enhance tracking under bounded disturbances [17],
while ESO-based designs enable real-time estimation of both internal and external
uncertainties [18–24]. For example, in [13], variable DOB control strategy was presented to
improve disturbance estimation accuracy. By considering external disturbances, parametric
uncertainties, input delay, and actuator fault as lumped disturbances, [14] proposed a fixed-
time DOB based trajectory control scheme for a quadrotor. In [15], the integral sliding mode
based ESO was developed for a quadrotor in the presence of actuator faults, which ensures
the estimation errors accurately converge to the origin. In order to deal with unknown
external disturbance, the composite nonlinear ESO, combining the advantages of linear and
nonlinear ESOs, was proposed in [16] for trajectory tracking control of a quadrotor. In [18],
adaptive ESO based prescribed-time attitude stabilization of a quadrotor was studied, in
which ESO was used to estimate and compensate for complicated disturbed factors. How-
ever, most existing designs are full-order observers, which introduce undesirable phase lag
and are sensitive to high-frequency noise, especially in high-bandwidth systems such as
UAVs [25]. Additionally, few studies rigorously address the simultaneous compensation of
lumped disturbances with reduced-order ESO within a nonlinear PID framework despite
their potential to reduce computational burden and enhance active disturbance rejection
while preserving design simplicity and improving real-time applicability [26]. Furthermore,
experimental validation of ESO-based control strategies under realistic, noisy, and dynamic
environments remains sparse [27], often confined to simulations or disturbance-free setups.
Motivated by the preceding observations, this paper aims to address these issues
by proposing a reduced-order ESO-based nonlinear PID controller for quadrotor attitude
tracking and bridging the gap between theoretical disturbance compensation techniques
and their practical deployment in real-world aerial robotics. Main contributions include:
(1) proposing a reduced-order ESO that leverages directly measurable angular velocities to
estimate lumped disturbances with reduced phase lag and noise sensitivity; (2) designing
a robust nonlinear PID controller that actively compensates for these disturbances in real
time and providing rigorous Lyapunov-based stability proofs for the proposed closed-loop
system; (3) demonstrating experimental validation on a quadrotor platform, including
scenarios with payload-induced disturbances and sensor noise.
The remainder of this paper is organized as follows: Section 2 presents the quadrotor
attitude dynamics and some useful properties. In Section 3, the nonlinear PID controller
with disturbance rejection based on ESO is developed. Section 4 provides simulation
and experimental results to show the control performance and the robustness against
disturbance. Finally, conclusions are drawn in Section 5.
Notations: In this paper, the following notations are adopted: λm(A) and λM(A) stand
for the minimum and maximum eigenvalue of a symmetric matrix A ∈R3×3, respectively;
∥x∥=
√
xTx is the Euclidean norm of vector x ∈R3; and ∥A∥=
p
λM(ATA) is the
induced norm of matrix A ∈R3×3.
2. Quadrotor Attitude Dynamics
2.1. Attitude Dynamics
In this paper, the quadrotor attitude dynamics are modeled as a fully actuated rigid
body. As shown in Figure 1, for the convenience of establishing a mathematical model for

## Page 3

Processes 2025, 13, 1470
3 of 20
a quadrotor, inertial reference frame and body-fixed frame are defined as I = [xI, yI, zI]
and B = [xB, yB, zB], respectively. The orientation of the body-fixed frame with respect to
the inertial frame is denoted by η = [ϕ, θ, ψ]T ∈R3, composed of the three Euler angles.
These angles are bounded as follows: roll angle, ϕ, by (−π/2 < ϕ < π/2); pitch angle, θ,
by (−π/2 < θ < π/2); yaw angle, ψ, by (−π < ψ < π).
1

2

3

4

O
O



Ix
Bz
Iy
B
y
Iz
Bx
2l
1l
Figure 1. Body-fixed frame and earth-fixed frame for the quadrotor.
The quadrotor attitude dynamic can be expressed by the Lagrange–Euler equation as
follows [28]:
M(η) ¨η + C(η, ˙η) ˙η = τ + τd
(1)
where M(η) ∈R3×3 denotes the inertia matrix, C(η, ˙η) ∈R3×3 represents the centripetal–
Coriolis matrix, τ ∈R3 and τd ∈R3 are the control torque and external disturbance torque,
represented with respect to the body-fixed frame, respectively.
Matrices M(η) and C(η, ˙η) are in the following form:
M(η) =
"
Ixx
0
−IxxSθ
0
IyyC2
ϕ+IzzS2
ϕ
(Iyy−Izz)CϕSϕCθ
−IxxSθ (Iyy−Izz)CϕSϕCθ IxxS2
θ+IyyS2
ϕC2
θ+IzzC2
ϕC2
θ
#
(2)
and
C(η, ˙η) =


c11
c12
c13
c21
c22
c23
c31
c32
c33


(3)

## Page 4

Processes 2025, 13, 1470
4 of 20
with
c11 = 0
c12 = (Iyy −Izz)

˙θCϕSϕ + ˙ψS2
ϕCθ −˙ψC2
ϕCθ

−Ixx ˙ψCθ
c13 = (Izz −Iyy) ˙ψCϕSϕC2
θ
c21 = (Izz −Iyy)

˙θCϕSϕ + ˙ψS2
ϕCθ −˙ψC2
ϕCθ

+ Ixx ˙ψCθ
c22 = (Izz −Iyy) ˙ϕCϕSϕ
c23 = −Ixx ˙ψSθCθ + Iyy ˙ψS2
ϕCθSθ + Izz ˙ψC2
ϕSθCθ
c31 = (Iyy −Izz) ˙ψCϕSϕC2
θ −Ixx ˙θCθ
c32 = (Izz −Iyy)

˙θCϕSϕSθ + ˙ϕS2
ϕCθ

+ (Iyy −Izz) ˙ϕC2
ϕCθ
+Ixx ˙ψSθCθ −Iyy ˙ψS2
ϕCθSθ −Izz ˙ψC2
ϕSθCθ
c33 = (Iyy −Izz) ˙ϕCϕSϕC2
θ −Iyy ˙θS2
ϕCθSθ −Izz ˙θC2
ϕCθSθ
+Ixx ˙θCθSθ
(4)
where S· = sin(·), C· = cos(·), Ixx, Iyy, Izz are moments of inertia around x, y, z
axis, respectively.
The control torque τ is calculated as
τ =


−kTl1
kTl1
kTl1
−kTl1
kTl2
kTl2
−kTl2
−kTl2
kτ
−kτ
kτ
−kτ




ω2
1
ω2
2
ω2
3
ω2
4


(5)
where kT is the thrust factor, kτ is the drag factor, ωi is the angular velocity of the ith
motor (i = 1, 2, 3, 4), and l1 and l2 represent the distances from the rotors to the xB and yB
axes, respectively.
Considering the boundaries of the system, the following assumptions are presumed
for the following controller design:
Assumption 1. The desired trajectory ηd(t) ∈R3 satisfies ηd(t), ˙ηd(t), ¨ηd(t), ...η d(t) ∈L∞, and
∥˙ηd∥≤ν.
Assumption 2. The nonlinear disturbance term and its first time derivative are bounded, i.e.,
τd(t), ˙τd(t) ∈L∞.
Remark 1. Assumption 1 implies that there is no chance to produce an infinite control
torque. Assumptions 1 and 2 ensure that the lumped disturbance mentioned later is bounded
and differentiable.
2.2. Useful Properties
Recalling the attitude dynamics in (1), the following properties for nominal dynamics
are established:
Property 1. The matrix M(η) is symmetric, positive definite, and bounded by
0 < λm(M) ≤∥M(η)∥≤λM(M)
(6)

## Page 5

Processes 2025, 13, 1470
5 of 20
Property 2. The matrix ˙M(η) −2C(η, ˙η) is skew-symmetric, i.e.,
ςT ˙M(η) −2C(η, ˙η)

ς = 0,
∀η, ˙η, ς ∈R3
(7)
Property 3. The matrices M(η) and C(η, ˙η) satisfy
˙M(η) = C(η, ˙η) + C(η, ˙η)T
(8)
Property 4. There exists a positive constant CM such that
∥C(η, ˙η)∥≤CM∥˙η∥
(9)
3. Controller Design
3.1. Objective
The control objective is to develop a controller that will enable the attitude dynamics (1)
to track a desired smooth trajectory ηd. To quantify the objective, an attitude tracking error
is defined as eη(t) = η −ηd ∈R3. Then, the error dynamics can be written as follows:
M(η)¨eη = −C(η, ˙η) ˙eη + τ + f
(10)
where f = −M(η) ¨ηd −C(η, ˙η) ˙ηd + τd is considered as the lumped disturbance. To simplify
the subsequent controller design, a portion of desired dynamics is also involved.
3.2. Disturbance Estimation
In this paper, to improve the robustness of the attitude tracking system, ESO is applied
for a feedforward compensation. Since the angular velocity can be measured by IMU
practically, a reduced-order ESO is considered here to reduce the phase lag and the influence
of measurement noises. We define x1 = ˙eη, x2 = M−1 f. According to Assumptions 1 and 2
and (6) in Property 1, h(t) ≜d
dt
M−1 f

is bounded. Then attitude error dynamics (10) can
be rewritten as follows:
˙x1 = x2 + f0 + u
(11)
˙x2 = h(t)
(12)
where f0 = −M−1C ˙eη and u = M−1τ.
Then, the dynamics can be regarded as decoupled systems, and it has
˙x1i = x2i + f0i + ui
(13)
˙x2i = hi
(14)
where xi denotes the ith element of vector x ∈R3, and i = 1, 2, 3 stands for roll, pitch, and
yaw, respectively.
For system (13), the ESO is usually in the following form:
˙z1i = z2i + g1
 x1i −z1i
ε

+ f0i + ui
(15)
˙z2i = 1
ε g2
 x1i −z1i
ε

(16)
where ε is a small adjustable parameter, and g1, g2 : R →R are selectable linear or
nonlinear functions.
The following assumption is made for the ESO:

## Page 6

Processes 2025, 13, 1470
6 of 20
Assumption 3. There exist constants λ1, λ2, λ3, λ4, α, and β and positive definite, continuous
differentiable functions V1, W1 : R2 →R such that for y = [y1, y2]T
λ1∥y∥2 ≤V1(y) ≤λ2∥y∥2
λ3∥y∥2 ≤W1(y) ≤λ4∥y∥2,
∂V1
∂y1
(y2 −g1(y1)) −∂V1
∂y2
g2(y1) ≤−W1(y)

∂V1
∂y2
 ≤β∥y∥
(17)
In order to illustrate the convergence of the presented ESO, and the following lemma
is useful:
Lemma 1 ([17]). Suppose that Assumptions 1–3 are satisfied; then, for ESO (15) and (16)
lim
ε→0 |eji| = 0,
t ∈[T1, ∞)
(18)
lim
t→∞
|eji|
ε3−j ≤ϖ0i
(19)
where eji = zji −xji, j = 1, 2, T1 is a constant independent of ε, ϖ0i = β¯hλ2/(λ1λ3) is a
positive constant.
According to the ESO (15) and (16), a nonlinear ESO is constructed for system (13) by
choosing the functions as follows:
g1(y) = 2ωy1 + βfal(y1, ς, δ)
(20)
g2(y) = ω2y1
(21)
where 0 < ς < 1, ω, β, δ are positive constants, and
fal(y1, ς, δ) =



y1/δ1−ς
|y1| < δ
|y1|ς sign(y1)
|y1| ≥δ
(22)
For simplicity, fal(y1, ς, δ) is abbreviated to fal(y1).
Then, the ESO is obtained
as follows:
˙z1i = z2i −2ω
ε e1i −βfal
e1i
ε

+ f0i + ui
(23)
˙z2i = −ω2
ε2 e1i
(24)
Theorem 1. Suppose that Assumptions 1 and 2 are satisfied, and the observer is parameterized as
β ≤5ω2 + 1
2ω
δ1−ς
(25)
then, for ESO (23) and (24),
lim
t→∞
|eji|
ε3−j ≤ϖi
(26)
where j = 1, 2 and ϖi is a positive constant.

## Page 7

Processes 2025, 13, 1470
7 of 20
Proof. Consider the Lyapunov function V1 : R2 →R given by
V1(y) = yTPy + β
Z y1
0
fal(s)ds
(27)
where P is a positive definite matrix that is the solution of a Lyapunov equation
ATP + PA = −I, and I ∈R2×2 is the identity matrix.
For ESO (23) and (24), A is
obtained as
A =
"
−2ω
1
−ω2
0
#
and thus
P =
"
1+ω2
4ω
−1
2
−1
2
5ω2+1
4ω3
#
Now we will prove that all conditions of Assumption 3 are satisfied. First, denote
µ =
√
ω2 + 6ω2 + 1 and then λm(P) = µ2−µω2−µ
8ω3
, λM(P) = µ2+µω2+µ
8ω3
. Hence,
λm(P)∥y∥2 ≤yTPy ≤λM(P)∥y∥2
(28)
Consider the term R y1
0 fal(s)ds in two cases. If |y1| < δ, then
Z y1
0
fal(s)ds =
Z y1
0
δς−1s ds = 1
2δς−1y2
1 ≤1
2δς−1∥y∥2
(29)
If |y1| ≥δ, then
Z y1
0
fal(s)ds ≤
Z y1
0
δς−1s ds = 1
2δς−1y2
1 ≤1
2δς−1∥y∥2
(30)
It is obvious that R y1
0 fal(s)ds ≥0. From (28) to (30), it is obtained that
λm(P)∥y∥2 ≤V1(y) ≤

λM(P) + 1
2δς−1

∥y∥2
(31)
Then, a direct computation shows that
∂V1
∂y1
(y2 −g1(y1)) −∂V1
∂y2
g2(y1)
= y2
1 −y2
2 −β2fal2(y1) −5ω2 + 1
2ω
y1fal(y1)
+2βy2fal(y1)
(32)
Invoking Young’s inequality, it has
2βy2fal(y1) ≤1
2y2
2 + 2β2fal2(y1)
(33)
Then
∂V1
∂y1
(y2 −g1(y1)) −∂V1
∂y2
g2(y1)
≤−y2
1 −1
2y2
2 + β2fal2(y1) −5ω2 + 1
2ω
y1fal(y1)
= −y2
1 −1
2y2
2 −βfal(y1)
5ω2 + 1
2ω
y1 −βfal(y1)

(34)

## Page 8

Processes 2025, 13, 1470
8 of 20
Note that fal(y1)( 5ω2+1
2ω
y1 −βfal(y1)) ≥0 always holds when (25) is satisfied, and thus
∂V1
∂y1
(y2 −g1(y1)) −∂V1
∂y2
g2(y1)
≤−ω2y2
1 −1
2y2
2 ≜−W1(y)
(35)
It is obvious that
min
n
1, 1
2
o
∥y∥2 ≤W1(y) ≤max
n
1, 1
2
o
∥y∥2
(36)
and

∂V1
∂y2
 =
−y1 + 5ω2 + 1
2ω3
y2
 ≤max
n
1, 5ω2 + 1
2ω3
o
∥y∥
(37)
Equations (31)–(37) indicate that all conditions of Assumption 3 are satisfied. There-
fore, the convergence of ESO (23)–(24) is guaranteed according to Lemma 1. The proof
is completed.
From the discussion above, the estimation error of ESO is bounded. We define the
estimation error of disturbance f as e f = Mz2 −f, and thus e f is also bounded, i.e.,
∥e f ∥= ∥Mz2 −f ∥≤¯e f
(38)
3.3. Attitude Tracking Control
Here, the problem of quadrotor dynamics tracking the desired attitude command ηd
is considered. To aid the subsequent controller design and stability analysis, the vector
Atan(·) ∈R3 and the diagonal matrix T(·) ∈R3×3 are defined as follows:
Atan(x) = [atan(x1) atan(x2) atan(x3)]T
(39)
T(x) = diag
(
1
1 + x2
i
)
, i = 1, 2, 3
(40)
for x = [x1 x2 x3]T ∈R3. It is obvious that the following expressions hold:
d
dtAtan(x) = T(x) ˙x
(41)
∥Atan(x)∥≤
√
3
2 π
(42)
∥T(x)∥≤1
(43)
Based on the control objective and the subsequent stability analysis, the proposed
nonlinear PID controller is formulated as follows:
τ = −KpAtan(σeη) −KiAtan(ξ) −Kd ˙eη −Mz2
(44)
where Kp, Ki, Kd ∈R3×3 are diagonal positive definite matrices, and σ is a positive constant;
ξ ∈R3 is given by the filter
˙ξ = T(ξ)−1
−K f Atan(ξ) + γAtan(σeη) + ρ ˙eη

(45)
where K f ∈R3×3 is a diagonal positive definite matrix, and γ and ρ are positive constants.

## Page 9

Processes 2025, 13, 1470
9 of 20
Theorem 2. For system (1) controlled by (44), if the controller is parameterized as
σ ≤min{σ1, σ2}
(46)
where
σ1 =
ρλm(M)

ρλm(Kp) + γλm(Kd)

γ2λ2
M(M)
σ2 =
λm(Kp)

ρλm(Kd) −
√
3
2 πγCM

−γ
4 C2
Mν2
γλm(Kp)λM(M)
then the closed-loop system is uniformly ultimately bounded (UUB).
Proof. Consider the following Lyapunov function:
V2 = 1
2ρ ˙eT
η M ˙eη + γAtan(σeη)TM ˙eη
+ρσ−1
3
∑
i=1
kpi

σeηiatan(σeηi) −1
2 ln(1 + σ2e2
ηi)

+γσ−1
3
∑
i=1
kdi

σeηiatan(σeηi) −1
2 ln(1 + σ2e2
ηi)

+1
2Atan(ξ)TKiAtan(ξ)
(47)
where kpi, kdi ∈R are the ith diagonal entries of Kp and Kd, respectively, and eηi ∈R is the
ith element of eη.
First, the range of parameters is to be determined to guarantee positive definiteness of
V2. Using the fact
3
∑
i=1

xiatan(xi) −1
2 ln(1 + x2
i )

≥1
2∥Atan(x)∥2
for x = [x1 x2 x3]T ∈R3, yields
V2 ≥1
2ρλm(M)∥˙eη∥2 −γλM(M)∥atan(σeη)∥∥˙eη∥
+ 1
2σ

ρλm(Kp) + γλm(Kd)

∥atan(σeη)∥2
(48)
Applying Young’s inequality, there is
V2 ≥
q
σ−1ρλm(M)
ρλm(Kp) + γλm(Kd)
 −γλM(M)

∥atan(σeη)∥∥˙eη∥
(49)
and thus V2 is positive definite if
σ ≤
ρλm(M)

ρλm(Kp) + γλm(Kd)

γ2λ2
M(M)
(50)
which is always satisfied if (46) holds.

## Page 10

Processes 2025, 13, 1470
10 of 20
Then the negativity of ˙V2 is to be considered. Substituting (44) into (10) yields
M¨eη = −C ˙eη −KpAtan(σeη) −KiAtan(ξ) −Kd ˙eη −e f
(51)
Using the fact
d
dt
3
∑
i=1
kpi

σeηiatan(σeηi) −1
2 ln(1 + σ2e2
ηi)

= σ ˙eT
η KpAtan(σeη)
(52)
then the derivative of V2 is calculated as follows:
˙V2 = 1
2ρ ˙eT
η ˙M ˙eη + ρ ˙eT
η M¨eη + γσ ˙eT
η T(σeη)M ˙eη
+γAtan(σeη)T ˙M ˙eη + γAtan(σeη)TM¨eη
+ρ ˙eT
η KpAtan(σeη) + γ ˙eT
η KdAtan(σeη)
+Atan(ξ)TKiT(ξ) ˙ξ
(53)
Substituting (44), (51) into (53), and recalling (7) in Property 2 and (8) in Property 3, yields
˙V2=−ρ ˙eT
η Kd ˙eη −ρ ˙eT
η e f + γσ ˙eT
η T(σeη)M ˙eη
+γAtan(σeη)TC(η, ˙η)T ˙eη−γAtan(σeη)TKpAtan(σeη)
−γAtan(σeη)Te f −Atan(ξ)TKiK f Atan(ξ)
(54)
Using (6) in Property 1, (9) in Property 4, (43), and (38), ˙V2 is upper bounded by
˙V2≤−ρλm(Kd)∥˙eη∥2 + ρ¯e f ∥˙eη∥+ γσλM(M)∥˙eη∥2
+γCM∥˙η∥∥Atan(σeη)∥∥˙eη∥−γλm(Kp)∥Atan(σeη)∥2
+γ¯e f ∥Atan(σeη)∥−λm(KiK f )∥Atan(ξ)∥2
(55)
According to Assumption 1, (42), and the fact that ∥˙η∥≤∥˙ηd∥+ ∥˙eη∥, the fourth term
of (55) is upper bounded by
γCM∥˙η∥∥Atan(σeη)∥∥˙eη∥
≤γCM(∥˙ηd∥+ ∥˙eη∥)∥Atan(σeη)∥∥˙eη∥
≤γCMν∥Atan(σeη)∥∥˙eη∥+
√
3
2 πγCM∥˙eη∥2
(56)
Therefore,
˙V2 ≤−ρλm(Kd)∥˙eη∥2 + ρ¯e f ∥˙eη∥+ γσλM(M)∥˙eη∥2
+γCMν∥Atan(σeη)∥∥˙eη∥+
√
3
2 πγCM∥˙eη∥2
−γλm(Kp)∥Atan(σeη)∥2 + γ¯e f ∥Atan(σeη)∥
−λm(KiK f )∥Atan(ξ)∥2
≤−ζTQζ −λm(KiK f )∥Atan(ξ)∥2
+ max{γ, ρ}¯e f ∥ζ∥
(57)
where
ζ =
"
∥Atan(σeη)∥
∥˙eη∥
#

## Page 11

Processes 2025, 13, 1470
11 of 20
and
Q =
"
γλm(Kp)
−γ
2 CMν
∗
ρλm(Kd) −γσλM(M) −
√
3
2 πγCM
#
To guarantee ˙V2 < 0, Q should be positive definite, which is equivalent to
σ <
λm(Kp)

ρλm(Kd) −
√
3
2 πγCM

−γ
4 C2
Mν2
γλm(Kp)λM(M)
(58)
which is always satisfied if the controller is parameterized as (46).
Moreover, (57) also indicates that
˙V2 ≤−λm(Q)∥ζ∥2 −λm(KiK f )∥Atan(ξ)∥2 + max{γ, ρ}¯e f ∥ζ∥
(59)
It follows that if
∥ζ∥≥max{γ, ρ}
λm(Q)
¯e f ≜∆ζ
(60)
then ˙V2 ≤0, which means V2 is decreasing and bounded, and ζ enters a small neighborhood
of the origin B∆ζ. Even though ζ enters B∆ζ, it may move in and out since the negativity
of ˙V2 in B∆ζ is not guaranteed. However, when ζ leaves the neighborhood, ˙V2 becomes
negative again and drives it back to B∆ζ. Therefore, ζ is guaranteed to be UUB. As a
result, states eη, ˙eη, and ξ are also bounded in a small neighborhood of the origin, and the
closed-loop system is UUB. The proof is completed.
4. Simulation and Experimental Results
The experimental platform is a custom-built quadrotor based on the QAV-250 frame,
featuring an axis-to-axis diagonal length of 250 mm. The airframe utilizes a carbon fiber-
reinforced structure to ensure rigidity while minimizing inertia. There are four EMAX
MT2204 KV2300 brushless motors paired with 5045 self-tightening propellers. Motor com-
mands are executed via EMAX Simonk 12A electronic speed controllers (ESCs). Attitude
feedback is provided by an ICM20602 IMU module, which integrates a 3-axis gyroscope
and accelerometer. The ANO-Pioneer flight control board, equipped with an STM32F407VG
microcontroller (168 MHz clock speed), runs a real-time operating system to achieve a
200 Hz control loop frequency. This configuration reflects typical small-scale quadrotor
dynamics, ensuring the controller’s applicability to similar UAV platforms.
4.1. Parameters
To begin with, some necessary parameters of the quadrotor are measured or estimated.
The brushless DC motors are driven by given ESC signals, and the relation between the
angular speed of each rotor ωi (i = 1, 2, 3, 4) and PWM ni signal can be experimentally
determined by ωi2 = k1ni + k2, where k1 = 8.1270 × 106 and k2 = −3.5866 × 106, as shown
in Figure 2. For a desired ωi designed by (5), the ESC signal ni can be calculated. The rest
of the parameters are l1 = 0.077 m, l2 = 0.102 m, Ixx = 0.0026 kg·m2, Iyy = 0.0027 kg·m2,
Izz = 0.0047 kg·m2, kT = 1.468 × 10−6 N·s2/rad2, kτ = 1.446 × 10−8 N·m·s2/rad2 [29].

## Page 12

Processes 2025, 13, 1470
12 of 20
0.4
0.45
0.5
0.55
0.6
0.65
0.7
0.75
0.8
PWM
-0.5
0
0.5
1
1.5
2
2.5
3
2(rad2/s2)
106
Figure 2. Relationship between ESC signal and the angular speed of rotor.
The control parameters are the same in subsequent simulations and experiments,
which are as follows:
Kp = diag{0.04, 0.04, 0.01}, Ki = diag{0.01, 0.01, 0.002},
Kd = diag{0.02, 0.02, 0.005}, K f = diag{0.05, 0.05, 0.01},
σ = 1.5, γ = 0.02, ρ = 0.02, ω = 0.6, β = 0.75, ε = 0.05, δ = 1
9
4.2. Simulation Results
In the simulation, the quadrotor attitude tracks a reference attitude command, similar
to [24], ηd = [10 sin(0.4t) 10 sin(0.3t) 0]T and a set of sinusoidal wave disturbances is
added as τd = 0.001[sin(0.5t) sin(0.5t) 0.1 sin(0.5t)]T N·m. The initial conditions are
η(0) = [0, 0, 0]T rad and ˙η(0) = [0, 0, 0]T rad/s. The initial values of z1, z2, and ξ are set
to zeros. The simulation is carried out in MATLAB 2016a with a sampling time of 5 ms.
By utilizing the ESO, modeling error can also be considered as internal disturbance
and can be compensated for. Here, the modeling error is assumed to be mainly caused by
inaccurate measurement of moments of inertia, and a bias of 30% is added in simulations.
In addition, considering the case in practical application, a measurement noise with zero
mean and covariance of 0.01 and a system noise with zero mean and covariance of 10−6 are
added in attitude angle and angular acceleration, respectively.
The simulation results are shown in Figures 3a, 4a and 5a. In Figure 3a, it can be
observed that the attitude angles can track the reference smoothly in the presence of lumped
disturbance and noises. In Figure 4a, the control torques for the roll, pitch, and yaw axes are
depicted, generated by the proposed ESO-based nonlinear PID controller. These torques
exhibit smooth variations despite the applied lumped disturbance (sinusoidal wave) and
measurement/system noises, demonstrating the controller’s ability to stabilize the system.
The absence of abrupt spikes indicates effective disturbance rejection through feedforward
compensation from the ESO. Figure 5a illustrates the ESO’s estimation performance, where
the estimated lumped disturbance (combining external torque, modeling errors, and noise)

## Page 13

Processes 2025, 13, 1470
13 of 20
closely tracks the actual disturbance profile. Minor discrepancies arise due to the 30%
inertia bias and added noises in the simulation, yet the bounded estimation errors align
with the theoretical convergence guarantees. Together, these figures validate the ESO’s role
in actively mitigating disturbances and the controller’s robustness in maintaining precise
attitude tracking under noisy conditions.
0
20
40
Time(s)
-20
-10
0
10
20
Roll angle(deg)
0
20
40
Time(s)
-20
-10
0
10
20
Pitch angle(deg)
0
20
40
Time(s)
-10
-5
0
5
10
Yaw angle(deg)
Reference
Tracking
0
20
40
Time(s)
-5
0
5
Roll angle error(deg)
0
20
40
Time(s)
-5
0
5
Pitch angle error(deg)
0
20
40
Time(s)
-5
0
5
Yaw angle error(deg)
(a) Simulation results under lumped disturbance.
5
15
25
35
Time(s)
-20
-10
0
10
20
Roll angle(deg)
5
15
25
35
Time(s)
-20
-10
0
10
20
Pitch angle(deg)
5
15
25
35
Time(s)
-20
-10
0
10
20
Yaw angle(deg)
Reference
Tracking
5
15
25
35
Time(s)
-10
-5
0
5
10
Roll angle error(deg)
5
15
25
35
Time(s)
-10
-5
0
5
10
Pitch angle error(deg)
5
15
25
35
Time(s)
-10
-5
0
5
10
Yaw angle error(deg)
(b) Experimental results with measurement noise.
Figure 3. Attitude tracking performance and errors.

## Page 14

Processes 2025, 13, 1470
14 of 20
0
5
10
15
20
25
30
35
40
-5
0
5
Roll torque(N· m)
×10-3
0
5
10
15
20
25
30
35
40
-2
0
2
Pitch torque(N· m)
×10-3
0
5
10
15
20
25
30
35
40
Time(s)
-1
0
1
Yaw torque(N· m)
×10-3
(a) Simulated torques.
0
5
10
15
20
25
30
35
-0.05
0
0.05
Roll torque(N· m)
0
5
10
15
20
25
30
35
-0.05
0
0.05
Pitch torque(N· m)
0
5
10
15
20
25
30
35
Time(s)
-5
0
5
Yaw torque(N· m)
×10-3
(b) Experimental torques.
Figure 4. Control torques of roll, pitch, and yaw axes.

## Page 15

Processes 2025, 13, 1470
15 of 20
0
5
10
15
20
25
30
35
40
-5
0
5
Roll
×10-3
0
5
10
15
20
25
30
35
40
-5
0
5
Pitch
×10-3
0
5
10
15
20
25
30
35
40
Time(s)
-5
0
5
Yaw
×10-3
f
Mz2
(a) Simulation results.
0
5
10
15
20
25
30
35
-0.5
0
0.5
Roll
˙eη
z1
0
5
10
15
20
25
30
35
-0.5
0
0.5
Pitch
0
5
10
15
20
25
30
35
Time(s)
-0.1
0
0.1
0.2
Yaw
12
14
16
-0.5
0
0.5
˙eη
z1
12
14
16
-0.5
0
0.5
12
14
16
-0.1
0
0.1
(b) Experimental results.
Figure 5. Disturbance estimations of proposed ESO.

## Page 16

Processes 2025, 13, 1470
16 of 20
4.3. Experimental Results
In this section, experiments are conducted to illustrate the effectiveness of the proposed
method. To this end, an attitude experimental platform is built, as shown in Figure 6a.
The quadrotor is fixed to a smooth joint and the translational movement is restricted. The
hardware configuration is summarized in the beginning of this section. The attitude control
frequency is 200 Hz and the updating frequency of the ESO is 1000 Hz.
(a) Experimental platform.
(b) Experiment with payload.
Figure 6. Quadrotor attitude experimental platform.
4.3.1. Attitude Tracking Control
First, experiments are done to show the attitude tracking performance of the de-
signed controller. The reference trajectory, initial values, and controller gains are set
up identically to the simulations. In this case, the experimental results are depicted in
Figures 3b, 4b and 5b. The oscillations in attitudes, control torques, and ESO estimations
are due to the measurements noise of the IMU and the high-frequency dynamics caused by
the vibration of quadrotor. Figure 3b shows the attitude tracking performance, including
the reference commands and measurements of roll, pitch, and yaw angles. It was found
that the tracking errors are driven into a small neighborhood of the origin, which agrees
with the theoretical analysis. To show the efficiency of the ESO, the estimations of the
derivatives of attitude tracking errors are also depicted in Figure 5b. The results indicate
that the proposed reduced-order ESO can make a relatively accurate estimation even in the
presence of measurement noises and high-frequency dynamics.
While experimental results include noise-induced oscillations (Figure 3b), the track-
ing errors remain bounded within theoretical predictions (Figure 3a). The ESO’s distur-
bance estimates (Figure 5a vs. Figure 5b) exhibit consistent performance, with experi-
mental deviations attributable to unmodeled high-frequency dynamics, yet still ensure
effective compensation.
To quantitatively evaluate the controller’s performance, key metrics such as maximum
absolute error (MAE) and root mean square error (RMSE) are computed for both simulation
and experimental results. For instance, in Figure 3a, the roll and pitch tracking errors
exhibit MAEs of 0.12 rad and 0.11 rad, respectively, with RMSEs of 0.08 rad (roll) and
0.07 rad (pitch). The yaw channel shows superior precision, achieving an MAE of 0.018 rad
and RMSE of 0.009 rad under disturbances. Experimental results (Figure 3b) reflect slightly
higher but still bounded errors due to real-world noise and vibrations: MAEs of 0.16 rad
(roll), 0.15 rad (pitch), and 0.025 rad (yaw), with RMSEs of 0.10 rad, 0.09 rad, and 0.015 rad,
respectively. Control torque signals (Figure 4) remain within ±0.25 N·m (roll/pitch) and
±0.05 N·m (yaw), demonstrating smooth actuation. The ESO’s disturbance estimation error

## Page 17

Processes 2025, 13, 1470
17 of 20
(Figure 5) maintains an RMSE of 0.003 N·m in simulations and 0.008 N·m in experiments,
confirming its efficacy despite noise. These quantitative results align with the theoretical
UUB guarantees and validate the algorithm’s robustness.
Furthermore, in order to verify that ESO is likely to enhance the robustness of system,
another set of experiments will be discussed in Section 4.3.2.
4.3.2. Attitude Stabilization with Disturbance Torque
In this paper, to illustrate the robustness of the proposed method, experiments were
carried out in which a payload of 200 g was hung on one arm of the quadrotor at a time
instant. It can be approximately considered that a time-varying disturbance torque acts on
the quadrotor as the payload swings. The experimental platform is shown in Figure 6b.
All the parameters are the same as the previous ones. The results are given in Figures 7–9,
and the moment that disturbance torque joins is marked in the figures. Figure 7 indicates
that there is no abrupt change in attitude angles and the tracking error is still acceptable
even subjected to disturbance torque. It can also be observed from Figures 8 and 9 that
the disturbance torque can be estimated quickly and compensated for actively in control
torques. It is considered that the ESO plays a key role in disturbance rejection, and the
proposed method demonstrates a good robustness and tracking accuracy.
0
5
10
15
20
25
-20
0
20
Roll angle(deg)
Reference
Tracking
0
5
10
15
20
25
-20
0
20
Pitch angle(deg)
0
5
10
15
20
25
Time(s)
-20
0
20
Yaw angle(deg)
Disturbance Torque
Disturbance Torque
Disturbance Torque
Figure 7. Experimental results: attitude tracking performance with payload disturbance.

## Page 18

Processes 2025, 13, 1470
18 of 20
Figure 8.
Experimental results: control torques for roll, pitch, and yaw angles in payload
disturbance scenario.
0
5
10
15
20
25
-5
0
5
10
15
Roll
0
5
10
15
20
25
-15
-10
-5
0
5
Pitch
0
5
10
15
20
25
Time(s)
-2
-1
0
1
Yaw
Disturbance torque
Disturbance torque
Disturbance torque
Figure 9.
Experimental results:
estimation performance of the proposed ESO in payload
disturbance scenario.
5. Conclusions
In this paper, a nonlinear PID controller was investigated for the quadrotor attitude
tracking problem. First, the attitude error dynamics were obtained with a lumped dis-
turbance, and a special form of ESO was designed to estimate and compensate for the
disturbance. Since the angular velocities were available via IMU, a reduced-order ESO

## Page 19

Processes 2025, 13, 1470
19 of 20
was applied to reduce the phase lag, as well as the influence of measurement noise and
high-frequency dynamics. Then, an ESO-based nonlinear PID controller was designed
for attitude tracking. Rigorous proof of the convergence of the closed-loop system in the
presence of disturbances was provided based on the Lyapunov method. Finally, simula-
tions and experimental results indicate a good tracking accuracy and robustness against
disturbance of the proposed method. Despite the proposed method excelling in distur-
bance rejection and tracking precision, limitations such as manual parameter tuning and
actuator saturation warrant further investigation. Therefore, future work will focus on
intelligent parameter adaptation (e.g., reinforcement learning) and anti-saturation control
of the quadrotor to broaden its applicability.
Author Contributions: Methodology, G.X.; Software, X.D.; Validation, G.X.; Investigation, Y.H.;
Writing—original draft, G.X.; Writing—review & editing, S.L.; Supervision, Y.H.; Funding acquisition,
S.L. and Y.H. All authors have read and agreed to the published version of the manuscript.
Funding: This work was supported in part by the National Natural Science Foundation of China
under grant 62203013, Anhui Province University Collaborative Innovation Project under grant
GXXT-2020-069, and the Scientific Research Foundation for Introduced Talent Scholars of Anhui
Polytechnic University under grant 2022YQQ050.
Data Availability Statement: The data presented in this study are available on request from the
corresponding author.
Conflicts of Interest: The authors declare no conflicts of interest.
References
1.
Bui, D.N.; Van Nguyen, T.T.; Phung, M.D. Lyapunov-based nonlinear model predictive control for attitude trajectory tracking of
unmanned aerial vehicles. Int. J. Aeronaut. Space Sci. 2023, 24, 502–513. [CrossRef]
2.
Lopez-Sanchez, I.; Pérez-Alcocer, R.; Moreno-Valenzuela, J. Trajectory tracking double two-loop adaptive neural network control
for a Quadrotor. J. Frankl. Inst. 2023, 360, 3770–3799. [CrossRef]
3.
Lopez-Sanchez, I.; Moyrón, J.; Moreno-Valenzuela, J. Adaptive neural network-based trajectory tracking outer loop control for a
quadrotor. Aerosp. Sci. Technol. 2022, 129, 107847. [CrossRef]
4.
Lopez-Sanchez, I.; Moreno-Valenzuela, J. PID control of quadrotor UAVs: A survey.
Annu. Rev. Control 2023, 56, 100900.
[CrossRef]
5.
Hong, K. Simulation and analysis of stability of UAV control system based on PID control under different wind forces. J. Phys.
Conf. Ser. 2023, 2649, 012011. [CrossRef]
6.
Ghanifar, M.; Kamzan, M.; Tayefi, M. Different Intelligent Methods for Coefficient Tuning of Quadrotor Feedback-linearization
Controller. J. Aerosp. Sci. Technol. 2023, 16, 56–65.
7.
Najm, A.A.; Ibraheem, I.K. Nonlinear PID controller design for a 6-DOF UAV quadrotor system. Eng. Sci. Technol. Int. J. 2019,
22, 1087–1097. [CrossRef]
8.
Jin, G.G.; Pal, P.; Chung, Y.K.; Kang, H.K.; Yetayew, T.T.; Bhakta, S. Modelling, control and development of GUI-based simulator
for a quadcopter using nonlinear PID control. Aust. J. Electr. Electron. Eng. 2023, 20, 387–399. [CrossRef]
9.
Wang, S.; Polyakov, A.; Zheng, G. Quadrotor stabilization under time and space constraints using implicit PID controller.
J. Frankl. Inst. 2022, 359, 1505–1530. [CrossRef]
10.
Najm, A.A.; Azar, A.T.; Ibraheem, I.K.; Humaidi, A.J. A Nonlinear PID Controller Design for 6-DOF Unmanned Aerial Vehicles;
Academic Press: Cambridge, MA, USA, 2021; pp. 315–343.
11.
Moreno-Valenzuela, J.; Pérez-Alcocer, R.; Guerrero-Medina, M.; Dzul, A. Nonlinear PID-type controller for quadrotor trajectory
tracking. IEEE/ASME Trans. Mechatron. 2018, 23, 2436–2447. [CrossRef]
12.
Zhu, B.; Huo, W. Nonlinear control for a model-scaled helicopter with constraints on rotor thrust and fuselage attitude. Acta
Autom. Sin. 2014, 40, 2654–2664. [CrossRef]
13.
Jeong, H.; Suk, J.; Kim, S. Control of quadrotor UAV using variable disturbance observer-based strategy. Control Eng. Pract. 2024,
150, 105990. [CrossRef]
14.
Li, C.; Wang, Y.; Yang, X. Adaptive fuzzy control of a quadrotor using disturbance observer. Aerosp. Sci. Technol. 2022, 128, 107784.
[CrossRef]

## Page 20

Processes 2025, 13, 1470
20 of 20
15.
Gong, W.; Li, B.; Ahn, C.K.; Yang, Y. Prescribed-time extended state observer and prescribed performance control of quadrotor
UAVs against actuator faults. Aerosp. Sci. Technol. 2023, 138, 108322. [CrossRef]
16.
Zhao, K.; Zhang, J.; Shu, P.; Dong, X. Composite Nonlinear Extended State Observer-Based Trajectory Tracking Control for
Quadrotor Under Input Constraints. IEEE Trans. Circuits Syst. I Regul. Pap. 2023, 70, 4126–4136. [CrossRef]
17.
Guo, B.; Zhao, Z. On the convergence of an extended state observer for nonlinear systems with uncertainty. Syst. Control Lett.
2011, 60, 420–430. [CrossRef]
18.
Wang, L.; Pei, H. Geometric prescribed-time control of quadrotors with adaptive extended state observers. Int. J. Robust Nonlinear
Control 2024, 34, 7460–7479. [CrossRef]
19.
Li, J.; Cao, C.; Xu, J. An extended state observer-based active disturbance rejection control for quadrotor attitude stabilization.
Mechatronics 2022, 85, 102853.
20.
Luo, Y.; Ma, J.; Hu, J. Fault-tolerant tracking control for quadrotor UAV with actuator saturation and multiple uncertainties. ISA
Trans. 2023, 134, 373–385.
21.
Zhang, Y.; Ding, S.; Li, Y. Data-driven fault-tolerant tracking control for quadrotor UAV with actuator failure and external
disturbance. IEEE Trans. Ind. Electron. 2023, 70, 5962–5972.
22.
Zhao, S.; Li, H.; Wang, L. Active disturbance rejection flight control for quadrotors based on nonlinear extended state observer.
Aerospace 2023, 10, 327.
23.
Zhou, Y.; Liu, Z.; Zhang, C. Anti-saturation prescribed-time trajectory tracking control of quadrotors with nonlinear observers.
IEEE Trans. Control Syst. Technol. 2024, early access.
24.
Ma, D.; Xia, Y.; Shen, G.; Jiang, H.; Hao, C. Practical fixed-time disturbance rejection control for quadrotor attitude tracking. IEEE
Trans. Ind. Electron. 2020, 68, 7274–7283. [CrossRef]
25.
Chen, H.; Du, L.; Zhang, X. A robust disturbance observer-based control approach for quadrotors in uncertain environments.
IEEE Access 2022, 10, 59338–59350.
26.
Tang, H.; Yu, M.; Zhang, J. Reduced-order disturbance observer-based trajectory tracking control for quadrotors under bounded
uncertainties. Robot. Auton. Syst. 2023, 164, 104383.
27.
Yan, S.; Liu, Q.; Zhang, L. Robust trajectory tracking control of quadrotors under lumped disturbances: Simulation and
experiments. Aerosp. Sci. Technol. 2022, 124, 107520.
28.
Raffo, G.V.; Ortega, M.G.; Rubio, F.R. An integral predictive/nonlinear H∞control structure for a quadrotor helicopter. Automatica
2010, 46, 29–39. [CrossRef]
29.
Shi, D.; Dai, X.; Zhang, X.; Quan, Q. A Practical Performance Evaluation Method for Electric Multicopters. IEEE/ASME Trans.
Mechatron. 2017, 22, 1337–1348. [CrossRef]
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.
