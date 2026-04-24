# machines-14-00078-v2.pdf

## Page 1

Academic Editor: Dan Zhang
Received: 8 December 2025
Revised: 31 December 2025
Accepted: 4 January 2026
Published: 8 January 2026
Copyright: © 2026 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license.
Article
Trajectory Tracking Control of a Six-Axis Robotic Manipulator
Based on an Extended Kalman Filter-Based State Observer
Jianxuan Liu, Tao Chen, Zhen Dou, Xiaojuan Li *
and Xiangjun Zou
School of Mechanical Engineering, Xinjiang University, Urumqi 830047, China; 107552204232@stu.xju.edu.cn (J.L.);
107556523226@stu.xju.edu.cn (T.C.); 107552404243@stu.xju.edu.cn (Z.D.); xjzou1@163.com (X.Z.)
* Correspondence: lxj_xj903@163.com
Abstract
To achieve high-precision trajectory tracking for multi-joint robotic manipulators in the
presence of model uncertainties, external disturbances, and strong coupling effects, this
paper proposes a nonsingular fast terminal sliding mode control (NFTSMC) scheme incor-
porating an extended Kalman filter-based disturbance observer. First, the Kalman filter is
combined with an extended state observer to perform the real-time observation of both
internal and external disturbances in the system, accurately estimating system uncertainty
and external disturbances. This approach reduces noise interference while significantly
improving the correction accuracy of position and tracking errors. Second, an improved
nonsingular fast terminal sliding mode controller with an optimized convergence law is
introduced to ensure stability during the tracking process, effectively mitigate oscillation
phenomena, and accelerate the system’s convergence speed. Finally, the convergence
of the proposed method is analyzed by constructing an appropriate Lyapunov function.
Simulation and experimental results strongly validate the superior performance of the pro-
posed control strategy, demonstrating that the system can achieve high-precision trajectory
tracking under the complex coupled effects of a six-axis robotic manipulator, and exhibits
significant advantages in terms of accuracy and robustness.
Keywords: robotic manipulator; non-singular fast terminal sliding mode control; extended
state observer; kalman filter; trajectory tracking
1. Introduction
In recent years, the widespread adoption of robots has significantly increased the
demands on robot control performance. Among the various research topics, trajectory
tracking for robotic manipulators has consistently been a core research focus. The ability of
robotic manipulators to precisely follow predefined joint trajectories is crucial for executing
complex tasks. To satisfy diverse performance requirements, numerous advanced control
strategies have been proposed [1–3], including PID control [4–6], sliding mode control [7–9],
fuzzy control [10,11], neural network control [12,13], adaptive control [14,15], and robust
control [16,17]. However, owing to the highly nonlinear dynamics of robotic manipulators,
along with model uncertainties, strong coupling effects, unknown external disturbances,
and measurement noise, achieving accurate and fast trajectory tracking remains a significant
challenge. Therefore, developing effective and robust trajectory tracking control methods
remains an urgent and important research direction.
Sliding mode control (SMC), as a control method, has the advantages of strong ro-
bustness, fast response, high accuracy, and simple design. Nevertheless, for robots with
Machines 2026, 14, 78
https://doi.org/10.3390/machines14010078

## Page 2

Machines 2026, 14, 78
2 of 18
parameter uncertainties and disturbances, SMC suffers from certain drawbacks, including
overshoot problems, challenges in sliding surface design, and the possibility of induc-
ing high-frequency oscillations. In particular, achieving the fast tracking of the desired
trajectory while simultaneously avoiding chattering caused by system uncertainties and dis-
turbances remains a challenge. To address these issues, researchers have proposed various
methods. References [18,19] proposed control strategies achieving fixed-time convergence,
with settling time independent of initial conditions, representing a class of fast and robust
control methods. Reference [20] proposed an adaptive nonsingular fast terminal sliding
mode control with model feedforward compensation, achieving fast convergence and
improved trajectory tracking under high-speed variable loads. Reference [21] combined
adaptive sliding mode control with NFTSMC for agricultural quadrotor UAVs, adjust-
ing parameters to handle system uncertainties and variations. Reference [22] introduced
a fractional-order sliding mode control based on a nonlinear ESO for photoelectric tracking
systems, providing faster response and enhanced control performance. Reference [23]
developed a PFTO-ABSTC method for deep-sea hydraulic manipulators, using adaptive
parameter estimation and disturbance observation to suppress chattering and improve
tracking precision. Reference [24] proposed an extended desired trajectory control strategy
combined with a predefined-time sliding mode controller, using an improved non-singular
fast sliding mode surface and a state observer to achieve convergence of angle tracking error
within a specified time. Reference [25] proposed a time-delay sliding mode control using
the previous sampling sliding variable to achieve fast convergence, minimal steady-state
error, and robustness to unknown dynamics and payloads. Reference [26] designed sliding
surfaces using error-shifting and barrier functions to achieve finite-time convergence under
system uncertainties, input dead zone, and external disturbances.
In addition to sliding mode control, numerous other methods have been developed to
handle system uncertainties and disturbances. Reference [27] introduced an observer with
adaptive switching gain, which enhances disturbance rejection ability and reduces servo
error. Reference [28] proposed a robust active learning (RAL) control method combining
Koopman modeling, active learning, and ESO-assisted tracking for efficient learning and
accurate trajectory tracking under unknown disturbances. Reference [29] developed a new
extended state observer with filtering capability to estimate lumped system uncertainties
and external disturbances. Reference [30] proposed a novel logarithmic power sliding mode
reaching law, combined with a fast terminal sliding mode surface, to design a finite-time
trajectory tracking controller.
Other advanced approaches have also been investigated. In Reference [31], an indirect
adaptive control using neural networks and DEKF was proposed for wheeled mobile
robots, improving tracking accuracy and computational efficiency under uncertainties.
Reference [32] combined a Dual-GRU Kalman Net estimator with an adaptive ESO and
nonsingular terminal sliding mode controller for robust tracking and faster, more accurate
convergence. In Reference [33], EKF was applied to attitude estimation of quadrotor
UAVs, demonstrating robust and accurate performance despite unpredictable external
disturbances and measurement noise.
Inspired by these methods, this paper proposes a comprehensive control strategy for
robotic systems subject to model uncertainties and external disturbances. The proposed ap-
proach integrates extended state observer (ESO) control, Kalman filtering, and nonsingular
fast terminal sliding mode control (NFTSMC) to enhance system robustness and control
accuracy. The main contributions of this paper can be summarized as follows: The main
contributions of this paper can be summarized as follows:
(1) An EKF–ESO integrated disturbance observation structure is proposed by incor-
porating an extended Kalman filter into the ESO framework. This approach preserves
https://doi.org/10.3390/machines14010078

## Page 3

Machines 2026, 14, 78
3 of 18
fast disturbance estimation capability while effectively suppressing measurement noise,
thereby significantly improving the accuracy and robustness of uncertainty and external
disturbance estimation.
(2) An improved nonsingular fast terminal sliding mode reaching law is developed. By
introducing a switching structure that combines nonlinear adaptive gains with a saturation
function, finite-time convergence is maintained while chattering caused by high-frequency
switching is effectively mitigated, resulting in smoother control inputs and improved
practical implementability for robotic manipulators.
(3) A unified control framework with deep integration of the observer and controller
is established. Through the coordinated design of the EKF–ESO and NFTSMC, a compre-
hensive optimization of trajectory tracking accuracy, convergence speed, and control input
smoothness is achieved.
2. Problem Description and Preliminaries
2.1. Interaction Force Control of Industrial Robots
Based on Lagrange dynamics analysis, the 6-DOF robot dynamics is represented as:
M(q)
..q + C(q,
.q)
.q + G(q) = τ + τd
(1)
where q,
.q,
..q ∈R6×1 denote the angle, velocity and acceleration of the robot, respectively.
M(q) ∈R6×6 denotes the positive definite inertia matrix of the system, C(q,
.q) ∈R6×6
denotes the Coriolis force and centrifugal force matrix, G(q) ∈R6×1 denotes the joint
gravity matrix. τ ∈R6×1 denotes the control input joint torque; and τd ∈R6×1 denotes the
external unknown disturbance matrix.
In the actual modeling process, due to unknown uncertainties in the mathematical
model of the robotic manipulator, M(q), C(q,
.q), G(q) are usually inaccurate. Therefore, it
can be expressed as:





M(q) = M0(q) + ∆M(q)
C(q,
.q) = C0(q,
.q) + ∆C(q,
.q)
G(q) = C0(q) + ∆C(q)
(2)
where M0(q),C0(q,
.q), G0(q) represent the nominal components of the parameters, while
∆M(q), ∆C(q,
.q), ∆G(q) denote the respective uncertain deviations from these nominal values.
Substituting Equation (2) into Equation (1), the dynamic model is reformulated as:
(M0(q) + ∆M(q))
..q + (C0(q,
.q) + ∆C(q,
.q))
.q + (C0(q) + ∆C(q)) = τ + τd
(3)
Define the total uncertainty part due to modeling errors and external disturbances as:
d(q,
.q,
..q) = τd −∆M(q)
..q −∆C(q,
.q)
.q −∆C(q). Thus, the dynamic model can be written as:
M0(q)
..q + C0(q,
.q)
.q + C0(q) = τ + d(q,
.q,
..q)
(4)
2.2. Related Properties and Lemmas
Property 1. Inertia M(q) is a symmetric positive definite matrix, and there exist positive num-
bers m1 and m2 that satisfy:
m1 ∥ς ∥2≤ςTM(q)ς ≤m2 ∥ς ∥2
(5)
Property 2. M(q) −2C(q,
.q) is a skew-symmetric matrix and satisfies:
ϖT(M(q) −2C(q,
.q))ϖ = 0
(6)
https://doi.org/10.3390/machines14010078

## Page 4

Machines 2026, 14, 78
4 of 18
Assumption 1. The lumped disturbance, including modeling uncertainties and external distur-
bances, is assumed to be bounded, ∥d∥(t) ≤dmax where dmax is a positive constant.
3. Proposed Control Design
3.1. Extended Kalman Filter State Observer Design
Define joint angle error, angular velocity error, and angular acceleration error,
respectively, as:
e = qd −q
.e =
.qd −
.q
..e =
..qd −
..q
(7)
where qd,
.qd,
..qd represent the desired displacement, angular velocity, and angular accelera-
tion of each joint, respectively. Assume they are known differentiable signals. The error
vectors are defined as:
.e = (
.e1,
.e2, . . . ,
.en)T ∈Rn
eα = (eα
1, eα
2, . . . , eα
n)T ∈Rn
|e|α = (|e1|α, |e2|α, . . . , |en|α)T ∈Rn
(8)
Combining with the system dynamics model (1), it can be written as:
.x(t) = f (x(t), u(t), t)
(9)
At time k, the measurement equation consists of the base joint angle position and the
end-effector rotation angle. Therefore, the measurement equation at time k is:
y(k) = Hx(k) + µ(k)
(10)
where H is the measurement matrix, and µ(k) denotes Gaussian white noise. Using the
difference equation representation, the state prediction equation with measurement noise
can be expressed. After the filtering prediction and update, the recursive formula is
obtained. The prediction equation can be expressed as:
ˆx−
k = f ( ˆxk−1, uk−1, tk−1)
P−
k−1 = AkPk−1AT
k + Qk
(11)
where ˆx−
k denotes the predicted state estimate at time k, P−
k−1 denotes the prediction error
covariance matrix, Ak is the Jacobian matrix, and Qk is the process noise covariance.
The Jacobian matrix Ak is expressed as:
Ak = ∂f ( ˆxk−1, uk−1, tk−1)
∂ˆxk−1
(12)
The update equation can be expressed as:
ˆxk = ˆx−
k + Kk(yk −Hk ˆx−
k )
Pk = (I −KkHk)P−
k
(13)
where yk is the observed value at time k, Hk is the observation matrix, Kk is the Kalman
gain, and I is a 6 × 6 identity matrix. The Kalman gain is expressed as:
Kk = P−
k HT
k (HkP−
k HT
k + Rk)
−1
(14)
https://doi.org/10.3390/machines14010078

## Page 5

Machines 2026, 14, 78
5 of 18
Considering system uncertainties and external disturbances, by selecting the state vari-
ables x1 = q and x2 =
.q, the dynamic equations shown in the formula can be transformed
into state-space form as follows:





.x1 = x2
.x2 = M−1
0 (τ −C0
.q −G0) + M−1
0 d
y = x1
(15)
Define observation error as ϑ = zi −xi. Based on this, the extended state space
observer is established as:









ϑ1 = zi1 −y1
.zi1 = zi2 −βi1ϑ1
.zi2 = zi3 −βi2e2fal(ϑ1, α1, δ) + M−1
d τ
.zi3 = −βi3fal(ϑ2, α2, δ)
(16)
where βi1, βi2, βi3 are all constant matrices, represents the observer gain; the observer
output zi1 is an estimate of the system’s joint angle q; zi2 is an estimate of the system’s joint
angular velocity
.q; zi3 is an estimate of the system’s total disturbance d, and zi3 is used to
compensate for disturbances. f al(ϑ, α, δ) is the nonlinear function defined as:
f al(ϑ, α, δ) =
(
ϑ
δ1−α
|ϑ| ⩽δ
|ϑ|α sign(ϑ)
|ϑ| > δ
(17)
According to Equations (15) and (16), the observation error is given by:











.
ϑ1 =
.zi1 −
.xi1 = ϑ2 −βi1ϑ1
.
ϑ2 =
.zi2 −
.xi2 = ϑ3 −βi2 f al(ϑ1, α1, δ)
.
ϑ3 =
.zi3 −
.xi3
= −βi3 f al(ϑ2, α2, δ) −(M−1
0 (τ −C0
.q −G0))
′
(18)
where α, δ are positive constants. The function f al(ϑ, α, δ) is a nonlinear gain function.
This ensures that the extended state observer (ESO) maintains bounded estimation
errors even when unmodeled dynamics and disturbances exist. By combining the EKF
Equation (14) and ESO equations, the following can be obtained:
ˆϑ = ˆϑ−+ K(y −H ˆϑ−)
(19)
P = (I −KH)P−
(20)
K = P−HT(HP−HT + R)
−1
(21)
Assumption 2. It is assumed that the measurement errors of the robot joint sensors are bounded.
For the i joint, the sensor error ei(t) satisfies: |ei(t)| ≤emax.
3.2. Stability Analysis
Let w = (M−1
0 (τ −C0
.q −G0))
′, and assume ∥w∥≤r. The observer state-space
equation can be expressed as:
.
ϑ = Aϑ + B
(22)
where
.
ϑ =


.
ϑ1
.
ϑ2
ϑ3

, ϑ =


ϑ1
ϑ2
ϑ3

, A1 =


−βi1
1
0
0
0
1
0
0
0

B1 =


0
−βi2fal(ϑ1, α1, δ)
−βi3fal(ϑ2, α2, δ) −w

.
https://doi.org/10.3390/machines14010078

## Page 6

Machines 2026, 14, 78
6 of 18
Case A: When |ϑ| ⩽δ
f al(ϑ, α, δ) =
ϑ
δ1−α
(23)
and the error dynamics can be rewritten as:
.
ϑ = A1ϑ + B1w
(24)
where A1 =


−βi1
γ1−θ
1
0
−βi2
γ1−θ
0
1
−βi3
γ1−θ
0
0

, B1 =


0
0
−1

and the characteristic equation is:
λ3 + h1λ2 + h2λ + h3 = 0
(25)
where h1, h2, h3 are all positive numbers, which indicates that the eigenvalues of matrix
A1 are all negative real parts. According to the Routh-Hurwitz stability criterion, it can be
concluded that all eigenvalues of A1 have negative real parts. This implies that the ESO
error eventually converges to zero and remains stable.
Case B: When |ϑ| > δ
fal(ϑ, α, δ) = |ϑ|αsign(ϑ)
(26)
Consider the following Lyapunov candidate function:
V1 =
.
ϑβTM(q)βϑ
(27)
Since the inertia matrix M(q) is positive definite, taking the derivative of the above
expression yields:
.
V1
=
.
ϑ
T .
β
T
M(q)βϑ + ϑTβTM(q)βϑ + ϑTβTM(q)β
.
ϑ
= −ϑT(β −βTM(q)β + βT)ϑ ≤−ϑT(β −c ∥ς∗∥2 +βT)ϑ
(28)
Constructing the inequality:
β −c ∥ζ∗∥2 +βT ≥Y
(29)
where Y > 0 is a symmetric positive definite matrix. Therefore, there exists Y∗> 0,
such that:
.
V1 ≤−ϑTY∗ϑ < 0
(30)
Selecting an appropriate observer gain matrix β ensures
.
V1 ≤0, which implies that
the error in ESO eventually converges and remains stable.
Case C: From Equations (20) and (21),
Kk+1 = P−
k+1HT(HP−
k+1HT + R)
−1
(31)
Pk+1 = (I −Kk+1H)P−
k+1
(32)
Substituting the estimated state into it:
∆= ˆz −z
(33)
https://doi.org/10.3390/machines14010078

## Page 7

Machines 2026, 14, 78
7 of 18
Substitute the update equation of the error covariance matrix into the definition of the
state estimation error:
Pk+1 = (l −Kk+1H)P−
k+1 = (l −Kk+1(H ˆz−+ ∆))P−
k+1 = P−
k+1 −Kk+1H ˆz−P−
k+1 −Kk+1∆P−
k+1
(34)
By substituting the Kalman gain, we obtain:
Pk+1 = P−
k+1 −P−
k+1HT(HP−
k+1HT + R)
−1H ˆz−P−
k+1 −P−
k+1HT(HP−
k+1HT + R)
−1∆P−
k+1
(35)
Because (HP−
k+1HT + R)−1 is a positive definite matrix, it can be concluded that:
I −P−
k+1HT(HP−
k+1HT + R)
−1 ≤0
(36)
Thus the error covariance matrix sequence Pk converges.
4. Design of the Sliding Mode Controller
4.1. Design of the Sliding Surface
Define the sliding mode surface:
s = e + p1Γ(e) + p2Γ(
.e) + p3
.e
(37)
where p1, p2, p3, r1, r2 are positive constants. Define:
Γ(e) = sign(e)|e|r1
(38)
Γ(
.e) = sign(
.e)
 .e
r2
(39)
The sign function is the following discontinuous function:
sign(s) =







1
s > 0
0
s = 0
−1
s < 0
(40)
The time derivative of the sliding surface is obtained as:
.s
=
.e + p1r1sign(e)|e|r1−1 .e + p2r2sign(
.e)
 .e
r2−1..e + p3
..e
= (1 + p1r1sign(e)|e|r1−1)
.e +

p2r2sign(
.e)
 .e
r2−1 + p3
..e
(41)
Using the tracking error, we obtain:
.s
= (1 + p1r1sign(e)|e|r1−1)
.e
+

p2r2sign(
.e)
 .e
r2−1 + p3
..qd −M−1
0 (q)
τ + d −C0(q,
.q)
.q −G0(q)

(42)
Define φ = 1 + p1r1sign(e)|e|r1−1, ψ = p2r2sign(
.e)
 .e
r2−1 + p3, According to the
definition of the sign function, it can be seen that φ ≥0, ψ ≥0. Therefore, Equation (40)
can be simplified as:
.s = φ
.e + ψ
..qd −ψ(M−1
0 (q)(τ + d −C0(q,
.q)
.q −G0(q)))
(43)
The traditional approaching law control method enables the system state trajectory to
move towards the designed sliding mode surface, thereby achieving convergence of the
sliding mode. However, in some cases, it may result in excessively high convergence speed,
causing system oscillations, or excessively low speed, leading to a slow response. In order
https://doi.org/10.3390/machines14010078

## Page 8

Machines 2026, 14, 78
8 of 18
to solve this problem, a nonlinear approaching law control method is adopted to adjust the
convergence speed adaptively. Therefore, a new sliding mode approaching law is proposed
in this paper.
.s = −
etanh(ϵs)
η + (1 −η)e−s εsign(s) −ks
(44)
Among them, ε, k and ϵ are constant matrices. When s increases, the approximate linear
interval range decreases, and the hyperbolic tangent function tends to saturation when s is
small. The introduction of the nonlinear term, by increasing the slope of the sliding mode
function, can reduce system oscillations, improve stability, or enhance response speed.
By adopting the concept of equivalent control to derive the control input, in order to
ensure that the system state remains on the sliding surface, let
.s = 0 in Equation (43), then
the equivalent control torque can be obtained as:
τeq = M0(q)
..qd + M0(q)ψ−1φ
.e + C0(q,
.q)
.q + G0(q) −d
(45)
Considering disturbances and uncertainties, in order to ensure that the system state
does not leave the sliding surface, the switching control law is designed as:
τsw = M0(q)ψ−1
 
εetanh(ϵs)sign(s)
η + (1 −η)e−s + ks
!
(46)
Therefore, the total control law of the system is:
τold
= τeq + τsw
= M0(q)
..qd + M0(q)ψ−1φ
.e + C0(q,
.q)
.q
+G0(q) −d + M0(q)ψ−1

εetanh(ϵs)sign(s)
η+(1−η)e−s
+ ks

= M0(q)
..qd + C0(q,
.q)
.q + G0(q) −d + M0(q)ψ−1

εetanh(ϵs)sign(s)
η+(1−η)e−s
+ ks + φ
.e

(47)
Note 1: Compared with the sign function, the advantage of the saturation function in
eliminating chattering lies in its smoothness, adjustable range, and ability to suppress noise.
Therefore, in order to further reduce chattering, the sign function sign(s) in Equation (47)
is replaced by the saturation function sat(s), whose expression is:
sat(s) =







1
s > δ
s/δ
|s| = δ
−1
s < −δ
(48)
The parameter δ > 0 is called the boundary layer. Within the boundary layer, linear
feedback control is applied, while outside the boundary layer, switching control is adopted.
By replacing the sign function with the saturation function, the improved non-singular fast
terminal sliding mode control law with the reaching law is given as follows:
τ = M0(q)ψ−1
 
εetanh(ϵs)sat(s)
η + (1 −η)e−s + ks + φ
.e
!
+ M0(q)
..qd + C0(q,
.q)
.q + G0(q) −d
(49)
Note 2: It should be noted that the parameters ε and k directly affect the convergence speed.
Choosing a smaller ε and a larger k will achieve a faster convergence speed.
https://doi.org/10.3390/machines14010078

## Page 9

Machines 2026, 14, 78
9 of 18
4.2. Analysis of System Stability
To analyze the convergence of the system, Lyapunov stability theory is employed.
First, construct the positive definite Lyapunov function V:
V2 = 1
2sTMs
(50)
V2 ≥1
2χmin ∥s ∥2= 1
2χmin
n
∑
i=1
s2
i
(51)
V2 ≤1
2χmax ∥s ∥2= 1
2χmax ∥s ∥T∥s ∥≤1
2χmaxµ ∥s ∥2
(52)
where χmin, χmax, µ are small positive numbers, so it can be shown that V2 is positive
definite and decreasing. Taking the derivative with respect to time:
.
V2 = 1
2sT
.
M0s + sTM0
.s = sTM0
.s + 1
2sT .
M0s = sTM0
.s + 1
2sT(
.
M0 −2C0)s + sTC0s
(53)
From Property 1 and Property 2:
.
V2 = sTM0
.s + sTC0s
(54)
Substituting Equation (43) into Equation (54) yields:
.s = φ
.e + ψ
..qd −ψ(M−1
0 (q)(τ + d −C0(q,
.q)
.q −G0(q)))
(55)
According to the Lyapunov stability theorem, V2 ≥0,
.
V2 ≤0, and hence it can be
proven that all parameters of V2 are bounded. It should be noted that the Lyapunov analysis
presented above is mainly intended to guarantee the stability of the closed-loop system
and the finite-time convergence of the tracking error in the sense of sliding mode control.
Due to the introduction of saturation functions and nonlinear reaching laws for chattering
suppression and practical implementation, deriving a strict analytical upper bound on
the convergence time would require additional conservative assumptions, which are not
pursued in this work.
5. Simulation and Experimental Analysis
In this section, to verify the effectiveness of the proposed control strategy, numeri-
cal simulations are conducted based on a six-degree-of-freedom robotic manipulator. To
demonstrate the superiority of the proposed scheme, NFTMC, ESONFTMC, and EKFESON-
FTMC are, respectively, used to control the trajectory tracking of the collaborative robot,
and the control performance is analyzed and compared. To ensure the accuracy of the
simulations, the basic parameters, external disturbances, and desired trajectories are all set
identically. The main parameters are listed in Table 1.
Table 1. Main Parameters.
Parameters
Value
Parameters
Value
p1
1.5
k
1000
p2
2.5
ϵ
1
p3
2
α1
0.5
r1
1.8
α2
0.1
r2
1.2
δ
0.01
ε
0.01
η
0.5
https://doi.org/10.3390/machines14010078

## Page 10

Machines 2026, 14, 78
10 of 18
The observer gains β1, β2, and β3 were selected according to the bandwidth-based
tuning principle commonly adopted in ESO design. Specifically, the observer bandwidth
ω0 was first determined based on a trade-off between estimation speed and noise sensitivity.
The gains were then chosen as β1 = 3ω0, β2 = 3ω2
0, and β3 = ω3
0, ensuring fast convergence
of the estimation error while avoiding excessive noise amplification.
In this work, ω0 was selected as 8 rad/s based on empirical tuning and preliminary
simulation tests, resulting in β1 = 24, β2 = 192, and β3 = 512.
The initial positions and velocities are chosen as [0; 0; 0; 0; 0; 0], and the external distur-
bances and desired trajectories are assumed as follows:
d =


d1
d2
d3
d4
d5
d6


=


sin(t) + exp(−10t)
0.4 sin(πt)
sin(t) + exp(−10t)
0.2 sin(2πt)
sin(t) + exp(−10t)
0.4 sin(2πt)


qd =


qd1
qd2
qd3
qd4
qd5
qd6


=


sin(t)
sin(t)
sin(t)
sin(t)
sin(t)
sin(t)


5.1. Analysis of the Control Strategy
The three control strategies share the same sliding surface, all using the s = e +
p1Γ(e) + p2Γ(
.e) + p3
.e proposed in this paper. The reaching laws and control laws of the
three control strategies are as follows:
Case 1: NFTSMC
Reaching Law:
.s = −εsign(s) −ks
Control Law: τ = M0(q)
..qd + ψ−1εsign(s) + ks + φ
.e
 + C0(q,
.q)
.q + G0(q) −d
Where φ = 1 + p1r1sign(e)|e|r1−1, ψ = p2r2sign(
.e)

.e|r2−1 + p3 .
Case 2: NFTSMC with Improved Reaching Law Based on ESO (E-NFTSMC)
Reaching Law:
.s = −
etanh(ϵs)
n+(1−n)e−s εsign(s) −ks
Control Law: τ = M0(q)

..qd + ψ−1

εetanh(ϵs)sat(s)
η+(1−η)e−s + ks + φ
.e

+ C0(q,
.q)
.q + G0(q) −d
Where φ = 1 + p1r1sign(qd −z1)|qd −z1|r1−1, ψ = p2r2sign(
.qd −z2)

.qd −z2|r2−1 + p3.
Case 3: The Control Strategy Proposed in This Paper (E-E-NFTSMC)
Reaching Law:
.s = −
etanh(ϵs)
n+(1−n)e−s εsign(s) −ks
Control Law: τ = M0(q)

..qd + ψ−1

εetanh(ϵs)sat(s)
η+(1−η)e−s + ks + φ
.e

+ C0(q,
.q)
.q + G0(q) −d
Where φ = 1 + p1r1sign(qd −ˆz1)|qd −ˆz1|r1−1, ψ = p2r2sign(
.qd −ˆz2)

.qd −ˆz2|r2−1 + p3.
5.2. Analysis of Simulation Results
To verify the effectiveness and feasibility of the proposed control scheme, a control
model is built in Simulink. In this paper, a six-axis robotic manipulator is used as the
control object, with its structure shown in Figure 1. The simulation duration is set to 10 s,
and the position tracking trajectory results are shown in Figure 2.
From the joint trajectory tracking curves shown in Figure 2a,b, it can be observed that
all control schemes for axes 1 and 2 are able to track the desired trajectory, but the tracking
error of the E-E-NFTSMC control strategy is the smallest. From Figure 2c–f, it can be
seen that, due to external disturbances and coupling effects, the NFTSMC and E-NFTSMC
control strategies show poor tracking performance on axes 3–6, and even fail to track the
https://doi.org/10.3390/machines14010078

## Page 11

Machines 2026, 14, 78
11 of 18
desired trajectory. In contrast, the E-E-NFTSMC control strategy proposed in this paper
can still track the trajectory well, and the tracking performance is the most satisfactory.
Figure 1. Structure of a six-axis robotic manipulator.
(a)
(b) 
(c)
(d) 
(e)
(f) 
Figure 2. Joint position tracking trajectory. (a) position tracking trajectory of joint 1. (b) position
tracking trajectory of joint 2. (c) position tracking trajectory of joint 3. (d) position tracking trajectory
of joint 4. (e) position tracking trajectory of joint 5. (f) position tracking trajectory of joint 6.
https://doi.org/10.3390/machines14010078

## Page 12

Machines 2026, 14, 78
12 of 18
From the convergence curves of the control torque inputs in Figure 3, it can be observed
that under the influence of disturbances, the torque remains relatively stable with the
proposed control algorithm, while the other two methods still exhibit large fluctuations.
The maximum torques of the three methods used in the simulation are −1809.7 N·m,
−477.2 N·m and −111.8 N·m, respectively, which further demonstrates the superiority of
the proposed method from the data.
 
 
(a) 
(b) 
 
 
(c) 
(d) 
 
 
(e) 
(f) 
Figure 3. Joint Torques. (a) control torque of joint 1. (b) control torque of joint 2. (c) control torque of
joint 3. (d) control torque of joint 4. (e) control torque of joint 5. (f) control torque of joint 6.
Compared with the conventional NFTSMC, the proposed E-E-NFTSMC reduces the
RMS value of the control torque from approximately 520 N·m to a negligible level, cor-
responding to a reduction of about 99.9%. In comparison with the E-NFTSMC, the pro-
posed E-E-NFTSMC decreases the peak RMS torque from approximately 11,500 N·m
to about 575 N·m, achieving a reduction of around 95%, which significantly improves
control smoothness.
https://doi.org/10.3390/machines14010078

## Page 13

Machines 2026, 14, 78
13 of 18
From the joint trajectory tracking error curves shown in Figure 4, it can be seen that
the control method proposed in this paper has a faster convergence speed compared with
the other two methods. To further evaluate the convergence rate quantitatively, the settling
time is defined as the time required for the tracking error to enter and remain within
a small neighborhood around zero (±5% of the steady-state value). As observed from
Figure 4, the proposed E-E-NFTSMC consistently exhibits the shortest settling time among
the three control strategies for all joints. This confirms that, although an explicit theoretical
upper bound is not derived, the proposed method achieves significantly faster convergence
in practice. Under the optimization of the proposed control strategy, the trajectory tracking
error quickly converges to zero, and the error fluctuations are relatively small.
 
 
(a) 
(b) 
 
 
(c) 
(d) 
 
 
(e) 
(f) 
Figure 4. Joint position tracking error. (a) position tracking error of joint 1. (b) position tracking
error of joint 2. (c) position tracking error of joint 3. (d) position tracking error of joint 4. (e) position
tracking error of joint 5. (f) position tracking error of joint 6.
https://doi.org/10.3390/machines14010078

## Page 14

Machines 2026, 14, 78
14 of 18
Based on the error of the six-axis robotic manipulator, the error bar chart of the six axes
is obtained as shown in Figure 5, and the average error is shown in Table 2. Through
the error comparison chart, it can be more intuitively observed that the errors of the
method proposed in this paper are all around zero, while the other two methods have large
fluctuations, especially in axes 4, 5, and 6, where there are large errors due to coupling
effects. The proposed method effectively solves this problem.
Figure 5. Comparison of errors.
Table 2. Average errors.
Joint
Average Error
NFTSMC
E-NFTSMC
E-E-NFTSMC
Joint 1
0.03289
0.03240
0.00472
Joint 2
0.05439
0.02712
0.00104
Joint 3
0.07719
0.02415
0.00504
Joint 4
1.04326
0.33578
0.01413
Joint 5
2.36878
1.21736
0.01343
Joint 6
18.10548
10.53078
0.03969
From Figure 5 and Table 2, it can be seen that, compared with the conventional
NFTSMC, the E-E-NFTSMC improves the average error by approximately 1.49%, 50.14%,
68.71%, 67.82%, 48.61%, and 41.84%, respectively; compared with the conventional
NFTSMC, the E-E-NFTSMC improves the average error by approximately 85.65%, 98.09%,
93.47%, 98.65%, 99.43%, and 99.78%, respectively. The comparative analysis indicates that
the proposed control method can not only significantly enhance trajectory tracking accuracy
but also substantially shorten the system’s response adjustment time. This validates that the
method can effectively reduce steady-state error, thereby improving both control precision
and robustness.
To observe the effect of the proposed observer in coping with disturbances, joints
4 and 5, which are most severely affected by coupling, were selected as examples, and
the observation trajectories of the two observers were compared. The results are shown
in Figure 6.
The results show that the conventional observer struggles significantly under strong
coupling, exhibiting large trajectory fluctuations and substantial deviations, making it
difficult to track the trajectory accurately. In contrast, the improved observer, with pre-
cise disturbance identification and a rapid compensation mechanism, produces smooth
trajectories that closely follow the desired path.
https://doi.org/10.3390/machines14010078

## Page 15

Machines 2026, 14, 78
15 of 18
 
(a) 
(b) 
Figure 6. Observation Trajectories. (a) Joint 4 Observation Trajectory; (b) Joint 5 Observation Trajectory.
5.3. Experiments and Analysis
To further verify superiority of the designed controller, experiments were conducted on
the ROCR6 robotic manipulator to compare the proposed control strategy with other control
strategies used in the simulations. The experimental procedure is shown in Figure 7. The
experimental platform consists of a 6-DOF robotic manipulator, drive boards, an integrated
controller, a computer, and MATLAB 2022b for data processing. The manipulator’s joints
communicate with the controller to exchange commands and state feedback. Control
signals generated in MATLAB are transmitted via the computer to the controller, enabling
precise trajectory tracking.
Figure 7. Experimental Procedure Diagram.
A periodic desired trajectory was set for tracking. When the ROCR6 was configured in
torque control mode, the robotic manipulator experienced some deflection due to gravity.
However, under the action of the controller, the actual trajectory was able to follow the
desired trajectory accurately.
From the tracking performance analysis, all joints in Figure 8 are able to accurately
follow the desired trajectory. Regarding the tracking error, the robotic manipulator’s joint
errors remain stable within the range of [−0.4, 0.4], and the joint torques in Figure 8 stay
within [−60, 50] with relatively small fluctuations. As shown in Figure 8, the tracking
errors of the six joints differ. Joints 3 and 4 exhibit the largest errors because they bear
higher inertial loads and are more sensitive to disturbances, unmodeled dynamics, as well
as nonlinear effects such as friction, backlash, and joint coupling. Joints 1 and 2, located
near the base, have smaller inertial loads but may be affected by motion errors transmitted
from the base, resulting in moderate errors. Joints 5 and 6, near the end effector, experience
smaller loads and require lower control torques, leading to weaker error amplification and
the best tracking performance.
https://doi.org/10.3390/machines14010078

## Page 16

Machines 2026, 14, 78
16 of 18
 
 
(a)  
(b)  
(c) 
Figure 8. Experimental Analysis. (a) Joint Trajectory Tracking. (b) Joint Errors. (c) Joint Torques.
These results indicate that the proposed control strategy can maintain tracking er-
rors within a small range during trajectory tracking, demonstrating that the strategy can
achieve rapid convergence within a limited time and ensure high-precision trajectory
tracking of the robotic manipulator. Figure 9 shows the process diagram of the trajectory
tracking procedure.
 
 
 
 
Figure 9. Experimental Process Diagram.
During the experiments, it was observed that without filtering, the robotic manipulator
exhibited varying degrees of vibration due to external disturbances and coupling effects, re-
sulting in poor trajectory tracking performance. After introducing the filtering module, the
robotic manipulator was able to effectively control the current, thereby reducing vibrations.
Both the simulation and hardware experiment results demonstrate that the proposed
control scheme exhibits excellent trajectory tracking performance and rapid convergence.
The control strategy meets the requirements for both precision and stability in robotic
manipulator control and can effectively handle complex issues such as system nonlinearity,
strong coupling, and external disturbances.
6. Conclusions
For a six-degree-of-freedom robotic manipulator subject to external disturbances, un-
known system uncertainties, and coupling effects, an improved non-singular fast terminal
sliding mode controller based on an extended Kalman filter (EKF) state observer is pro-
posed. This controller can drive the tracking error to converge to zero within a finite time
while effectively reducing torque chattering. The newly designed observer, composed
of the improved Kalman filter and the extended state observer, can rapidly converge the
estimation error to a bounded range and eventually stabilize near zero, thereby enhancing
the system’s robustness to high-frequency disturbances. By designing a new reaching law
https://doi.org/10.3390/machines14010078

## Page 17

Machines 2026, 14, 78
17 of 18
to update the switching gain of the sliding function, the chattering problem is further miti-
gated, improving overall controller performance. To achieve finite-time convergence of the
tracking error, these techniques are combined with the non-singular fast terminal sliding
mode control, and the finite-time convergence property of the algorithm is proven using
a Lyapunov function. Finally, the proposed method is applied to numerical simulations
and experiments on a six-degree-of-freedom robotic manipulator, and the results validate
the feasibility and superiority of the approach. In future work, trajectory planning methods
will be investigated in conjunction with the proposed robust trajectory tracking controller to
achieve a systematic integration of smooth motion planning and robust finite-time tracking
control under complex operating conditions, thereby further improving motion smoothness
and overall control performance in practical robotic applications.
Author Contributions: Conceptualization, J.L. and T.C.; methodology, J.L.; software, J.L.; validation,
J.L., T.C. and Z.D.; formal analysis, J.L.; investigation, Z.D.; resources, X.L.; data curation, T.C.;
writing—original draft preparation, J.L.; writing—review and editing, X.Z. and X.L.; visualization,
J.L.; supervision, X.L.; project administration, X.Z. and X.L.; funding acquisition, X.L. All authors
have read and agreed to the published version of the manuscript.
Funding: This research was funded by the National Natural Science Foundation of China project
(52265003); The Tianshan Talents-Young Cedar Youth Top Talent Project of the Xinjiang Uygur
Autonomous Region (20227SYCCX0061) and the Xinjiang Uygur Autonomous Region Postgraduate
Research Innovation Project, grant number (XJ2025G042).
Data Availability Statement: Data are contained within the article.
Conflicts of Interest: The authors declare no conflicts of interest.
References
1.
Shojaei, K.; Kazemy, A.; Chatraei, A. An observer-based neural adaptive PID2 controller for robot manipulators including motor
dynamics with a prescribed performance. IEEE/ASME Trans. Mechatron. 2020, 26, 1689–1699. [CrossRef]
2.
Tinoco, V.; Silva, M.F.; Santos, F.N.; Morais, R.; Magalhães, S.A.; Oliveira, P.M. A review of advanced controller methodologies for
robotic manipulators. Int. J. Dyn. Control 2025, 13, 36. [CrossRef]
3.
Xuan, Q.N.; Cong, C.N.; Ba, N.N. Robust adaptive trajectory tracking sliding mode control for industrial robot manipulator using
fuzzy neural network. J. Robot. Control (JRC) 2024, 5, 490–499. [CrossRef]
4.
Ata¸slar-Ayyıldız, B. Robust trajectory tracking control for serial robotic manipulators using fractional order-based PTID controller.
Fractal Fract. 2023, 7, 250. [CrossRef]
5.
Azeez, M.I.; Atia, K.R. Modeling of PID controlled 3DOF robotic manipulator using Lyapunov function for enhancing trajectory
tracking and robustness exploiting Golden Jackal algorithm. ISA Trans. 2024, 145, 190–204. [CrossRef]
6.
Zhang, Q.; Mu, M.; Ji, H.; Wang, Q.; Wang, X. An adaptive type-2 fuzzy sliding mode tracking controller for a robotic manipulator.
Electron. Res. Arch. 2023, 31, 3791–3813. [CrossRef]
7.
Aydın, M. Real-time sliding mode and moving sliding mode control of 3-dof linear parallel robot. Machines 2025, 13, 190.
[CrossRef]
8.
Park, J.M.; Kwon, W.; Park, P.G. An improved adaptive sliding mode control based on time-delay control for robot manipulators.
IEEE Trans. Ind. Electron. 2022, 70, 10363–10373. [CrossRef]
9.
Wang, Z.; Mei, L.; Ma, X. A novel generalized sliding mode controller for uncertain robot manipulators based on motion
constraints. Mech. Sci. 2024, 15, 55–62. [CrossRef]
10.
Qu, J.; Zhang, Z.; Li, H.; Li, M.; Xi, X.; Zhang, R. Design and experiments of a two-stage fuzzy controller for the off-center
steer-by-wire system of an agricultural mobile robot. Machines 2023, 11, 314. [CrossRef]
11.
Zhang, X.; Wang, R. Non-singular fast terminal sliding mode control of robotic manipulator with prescribed performance. J. Eng.
Appl. Sci. 2024, 71, 217. [CrossRef]
12.
Xu, K.; Wang, Z. The design of a neural network-based adaptive control method for robotic arm trajectory tracking. Neural
Comput. Appl. 2023, 35, 8785–8795. [CrossRef]
13.
Du, B.; Zhu, D.; Pan, Y. Fuzzy super-twisting second order sliding mode trajectory tracking control for robotic manipulator.
J. Syst. Simul. 2022, 34, 1343–1352.
https://doi.org/10.3390/machines14010078

## Page 18

Machines 2026, 14, 78
18 of 18
14.
Shan, H.; Jiang, Y.; Zhu, Y.; Liang, H.; Wang, S. Fixed-time self-triggered fuzzy adaptive control of N-link robotic manipulators.
Fuzzy Sets Syst. 2025, 498, 109134. [CrossRef]
15.
Li, L.; Qiang, J.; Xia, Y.; Cao, W. Adaptive dual closed-loop trajectory tracking control for a wheeled mobile robot on rough
ground. Nonlinear Dyn. 2025, 113, 2411–2425. [CrossRef]
16.
Zhou, S.; Shen, C.; Xia, Y.; Chen, Z.; Zhu, S. Adaptive robust control design for underwater multi-DoF hydraulic manipulator.
Ocean. Eng. 2022, 248, 110822. [CrossRef]
17.
Song, G.I.; Park, H.Y.; Kim, J.H. The H∞Robust Stability and Performance Conditions for Uncertain Robot Manipulators.
IEEE/CAA J. Autom. Sin. 2025, 12, 270–272. [CrossRef]
18.
Wang, C.; Tnunay, H.; Zuo, Z.; Lennox, B.; Ding, Z. Fixed-time formation control of multirobot systems: Design and experiments.
IEEE Trans. Ind. Electron. 2018, 66, 6292–6301. [CrossRef]
19.
Ning, B.; Han, Q.L. Prescribed finite-time consensus tracking for multiagent systems with nonholonomic chained-form dynamics.
IEEE Trans. Autom. Control 2018, 64, 1686–1693. [CrossRef]
20.
Hu, S.; Wan, Y.; Liang, X. Adaptive nonsingular fast terminal sliding mode trajectory tracking control for robotic manipulators
with model feedforward compensation. Nonlinear Dyn. 2025, 113, 16893–16911. [CrossRef]
21.
Cruz-Ortiz, D.; Chairez, I.; Poznyak, A. Non-singular terminal sliding-mode control for a manipulator robot using a barrier
Lyapunov function. ISA Trans. 2022, 121, 268–283. [CrossRef] [PubMed]
22.
Zhou, X.; Li, X. Trajectory tracking control for electro-optical tracking system using ESO based fractional-order sliding mode
control. IEEE Access 2021, 9, 45891–45902. [CrossRef]
23.
Chen, G.; Wu, W.; Yang, C.; Hu, H.; Zhang, J.; Shi, J.; Wu, C.; Ma, Y. Practical Finite-Time Observer-Based Adaptive Backstepping
Super-Twisting Sliding Mode Control for Deep-Sea Hydraulic Manipulator. In IEEE Transactions on Industrial Electronics; IEEE:
Piscataway, NJ, USA, 2025.
24.
Yin, C.W.; Ding, Y.P.; Sun, H.J. Nonsingular fast predefined time convergence sliding mode control for construction robot. ISA
Trans. 2025, 161, 109–121. [CrossRef] [PubMed]
25.
Yang, J.; Wang, Y.; Wang, T.; Hu, Z.; Yang, X.; Rodriguez-Andina, J.J. Time-delay sliding mode control for trajectory tracking of
robot manipulators. IEEE Trans. Ind. Electron. 2024, 71, 13083–13091. [CrossRef]
26.
Zhang, Y.; Kong, L.; Zhang, S.; Yu, X.; Liu, Y. Improved sliding mode control for a robotic manipulator with input deadzone and
deferred constraint. IEEE Trans. Syst. Man Cybern. Syst. 2023, 53, 7814–7826. [CrossRef]
27.
Tian, D.; Xu, R.; Sariyildiz, E.; Gao, H. An adaptive switching-gain sliding-mode-assisted disturbance observer for high-precision
servo control. IEEE Trans. Ind. Electron. 2021, 69, 1762–1772. [CrossRef]
28.
Lyu, S.; Lang, X.; Wang, D. Koopman-based robust learning control with extended state observer. In IEEE Robotics and Automation
Letters; IEEE: Piscataway, NJ, USA, 2025.
29.
Xu, Z.; Yang, X.; Zhou, S.; Zhang, W.; Zhang, W.; Yang, S.; Liu, P.X. Extended state observer based adaptive backstepping
nonsingular fast terminal sliding-mode control for robotic manipulators with uncertainties. Int. J. Control. Autom. Syst. 2022, 20,
2972–2982. [CrossRef]
30.
Silaa, M.Y.; Bencherif, A.; Barambones, O. Indirect adaptive control using neural network and discrete extended kalman filter for
wheeled mobile robot. Actuators 2024, 13, 51. [CrossRef]
31.
Hartley, R.; Ghaffari, M.; Eustice, R.M.; Grizzle, J.W. Contact-aided invariant extended Kalman filtering for robot state estimation.
Int. J. Robot. Res. 2020, 39, 402–430. [CrossRef]
32.
Zhang, C.; Mao, J.; Qin, Q.; Wu, A.; Zhang, X.; Zheng, J. Vision-based trajectory tracking control for wheeled mobile robots using
DG-KalmanNet and nonsingular terminal sliding mode control: C. Zhang et al. Nonlinear Dyn. 2025, 113, 33687–33719. [CrossRef]
33.
Li, L.; Cao, W.; Yang, H.; Geng, Q. Trajectory tracking control for a wheel mobile robot on rough and uneven ground. Mechatronics
2022, 83, 102741. [CrossRef]
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.
https://doi.org/10.3390/machines14010078
