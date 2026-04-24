# NN-MPC An Adaptive Neural Network-Based Nonlinear Model Predictive Control Method for Robust Trajectory Tracking of Quadrotors.pdf

## Page 1

10966
IEEE ROBOTICS AND AUTOMATION LETTERS, VOL. 10, NO. 10, OCTOBER 2025
ANN-MPC: An Adaptive Neural Network-Based
Nonlinear Model Predictive Control Method for
Robust Trajectory Tracking of Quadrotors
Chuixu Kong
, Bin Wang
, Liang He
, Qinglong Jiang
, and Chang Liu
Abstract—Quadrotor systems, despite their extensive deploy-
ment in diverse application domains, face substantial performance
degradation due to three predominant factors: unmodeled aero-
dynamic phenomena, persistent wind disturbances, and unantici-
pated payload variations. These challenges collectively compromise
precise trajectory tracking in dynamic environments. To address
these limitations, this study introduces an integrated control ar-
chitecture combining 1) an adaptive neural network disturbance
observer (ANNDO) with guaranteed Lyapunov stability through
carefully designed adaptive laws, and 2) a modiﬁed model predic-
tive control (MPC) scheme enhanced with real-time disturbance
compensation. The proposed framework demonstrates substantial
performanceimprovements,achievingover80%trackingaccuracy
enhancement in numerical simulations during agile ﬂight, and
over 50% improvement in physical experiments involving complex
disturbance rejection, compared with baseline MPC.
Index Terms—Adaptive neural network control, model predi-
ctive control, disturbance rejection.
I. INTRODUCTION
A. Motivation
T
HE proliferation of quadrotor systems in mission-critical
domains, including time-sensitive logistics operations [1],
[2] and safety-contingent emergency response missions [3], has
been propelled by recent advancements in embedded avionics
and fusion perception. Ensuring high-precision trajectory track-
ing under disturbances is essential for quadrotors to maintain
safe and high-performance ﬂight in complex environments.
Received 27 March 2025; accepted 25 August 2025. Date of publication
8 September 2025; date of current version 15 September 2025. This article
was recommended for publication by Associate Editor U-X. Tan and Editor L.
Pallottino upon evaluation of the reviewers’ comments. (Corresponding author:
Chang Liu.)
Chuixu Kong and Bin Wang are with Aerospace Information Research In-
stitute, Chinese Academy of Sciences, Beijing 100094, China, also with the
School of Electronic, Electrical and Communication Engineering, University
of Chinese Academy of Sciences, Beijing 100049, China, and also with the
National Key Laboratory of Intelligent Collaborative Perception and Analytic
Cognition, Beijing 100124, China (e-mail: kongchuixu23@mails.ucas.ac.cn;
wangbin22@mails.ucas.ac.cn).
Liang He is with the National Key Laboratory of Intelligent Collaborative
Perception and Analytic Cognition, Beijing 100124, China (e-mail: heliang
09@nudt.edu.cn).
Qinglong Jiang is with Shen Yuan Honors College of Beihang University,
Beijing 100191, China (e-mail: 21231075@buaa.edu.cn).
Chang Liu is with Aerospace Information Research Institute, Chinese
Academy of Sciences, Beijing 100094, China (e-mail: cliu@aircas.ac.cn).
Video: https://youtu.be/VZgPOiFOnPM.
Digital Object Identiﬁer 10.1109/LRA.2025.3607272
Traditional control methods, such as PID and LQR, are widely
used due to their simplicity and ease of implementation [4].
However, their performance markedly deteriorates when ad-
dressing highly nonlinear dynamics inherent in aerial systems.
Research demonstrates that MPC effectively addresses the non-
linear coupling effects of quadrotors through receding horizon
optimization with explicit constraint handling [5], [6]. Never-
theless, MPC’s dependence on ﬁrst-principles models limits its
practical applicability, as uncertainties and disturbances com-
monly cause these models to become inaccurate or unreliable.
Neural networks can universally approximate any contin-
uous and bounded function on a compact set [7], such as
modeling disturbances on a quadrotor [8]. However, traditional
learning-based approaches struggle to quickly adapt to sudden
disturbances with limited data, which motivates us to explore
the use of the adaptive neural network (ANN). To address
this, we propose the ANNDO that adaptively compensates for
disturbances within the MPC framework, enabling reliable and
precise quadrotor control. The main contributions of this article
can be summarized as follows:
1) An adaptive neural network disturbance observer is pro-
posed to estimate disturbances, and the Lyapunov tech-
nique is employed to guarantee convergence of the
estimation error.
2) Within the MPC framework, disturbance estimates are
integrated into the predictive model, resulting in an
ANNDO-enhanced MPC algorithm (ANN-MPC) that
achieves robust trajectory tracking for quadrotors.
3) The effectiveness of our proposed approach is validated
through extensive simulations and physical experiments.
B. Related Works
Trajectorytrackingforquadrotorhasemergedasacriticalarea
of research, with extensive taxonomies provided in[4], [9]. Early
approaches primarily relied on linearized controllers based on
small-angle assumptions, which constrained their applicability
toquasi-statichoveringandlow-accelerationmaneuvers[10].To
overcome these limitations, nonlinear model predictive control
has been extensively investigated due to its capability to generate
optimal control inputs while simultaneously accounting for sys-
tem constraints and future states. Empirical studies have demon-
strated its superior performance in agile trajectory tracking [5],
[6]. Nevertheless, its effectiveness is inherently dependent on
2377-3766 © 2025 IEEE. All rights reserved, including rights for text and data mining, and training of artiﬁcial intelligence and similar technologies.
Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 10:43:05 UTC from IEEE Xplore.  Restrictions apply.

## Page 2

KONG et al.: ANN-MPC: AN ADAPTIVE NEURAL NETWORK-BASED NONLINEAR MODEL PREDICTIVE CONTROL METHOD
10967
accurate system modeling, rendering it susceptible to model
uncertainties and external disturbances, such as wind perturba-
tions [10]. These vulnerabilities present substantial challenges
for real-world deployment, particularly in dynamically varying
environments.
Various enhancement strategies have been developed to im-
prove MPC’s robustness against disturbances and model un-
certainties. One widely adopted approach involves integrating
disturbance observers to estimate and compensate for perturba-
tionsinrealtime.Techniquessuchasactivedisturbancerejection
control (ADRC) [11], [12] have been extensively explored in
this context. The extended state observer (ESO) is a key part
of the ADRC, which treats internal unknown dynamics and
external perturbations as the total perturbations of the extended
state and estimates the total perturbations in real time [13].
Chen et al. [14] incorporated ESO within an MPC framework,
leading to improved tracking accuracy by mitigating the impact
of external disturbances.
Beyond disturbance observers, adaptive control has been
increasingly integrated with other control frameworks to ad-
dress uncertainties and enhance performance. In particular, L1
adaptive control has been integrated into MPC to enhance its
robustness, primarily targeting the compensation of matched
uncertainties [15], [16], [17]. However, these approaches are
inherently limited when it comes to handling unmatched uncer-
tainties, such as external forces projected onto the body-frame xy
plane, which can signiﬁcantly impair ﬂight stability and tracking
accuracy To address this issue, Chee et al. [18] introduced the
KNODE-MPC-L1-Int framework, which synergistically com-
bines KNODE for system modeling, L1 adaptive control for
residual disturbance compensation, and MPC for trajectory
optimization. This integrated approach has demonstrated no-
table improvements in robustness across varying environmental
conditions.
Recent advancements in data-driven methodologies have fur-
thercontributedtoMPC’sresilienceagainstmodeluncertainties.
Machine learning methods have made signiﬁcant contributions
to the approximation of dynamic residuals and the estimation
of unknown disturbances [8], [19], [20], [21], [22], [23], [24],
[25]. Gaussian process regression (GPR) has been successfully
applied to capture unknown aerodynamic disturbances, resulting
in enhanced MPC-based tracking accuracy [20]. Despite these
advancements, the efﬁcacy of machine learning-based models
remains constrained by their reliance on extensive training data.
Their generalization capability, particularly in unseen or dynam-
ically shifting environments, remains an open challenge.
To mitigate the reliance of machine learning-based models
on extensive precollected training datasets, ANN has been in-
troduced as an alternative approach to real-time disturbance
estimation [7], [26], [27], [28], [29]. By integrating the strong
nonlinear approximation capability of neural networks with
adaptive parameter adjustment, ANN can dynamically model
complex disturbances and continuously reﬁne their predictions
based on real-time ﬂight data [7]. However, despite these ad-
vantages, ensuring the boundedness of ANN weights remains a
critical challenge [28], particularly when integrated with MPC.
Stability concerns, alongside the computational overhead as-
sociated with real-time parameter updates, must be carefully
Fig. 1.
Diagram of the quadrotor model with the world and body frames and
propeller numbering convention.
addressed to ensure reliable deployment in practical quadrotor
applications.
II. PRELIMINARY AND MODEL
A. Notation
1) Kinetic Expression: As illustrated in Fig. 1, we deﬁne the
world coordinate system W and the body-ﬁxed frame B using
the orthonormal basis {xW , yW , zW } and {xb, yb, zb}. The
body-ﬁxed coordinate system is established at the center of mass
of the quadrotor.
2) Neural Network Formulation: Consider a scalar input ν ∈
R and a function ϕ : R →R which can be approximated by the
following linear model:
ϕ(ν) = W T h(ν) + ε,
(1)
where h(ν) = [h1(ν), h2(ν), . . . , hn(ν)]T ∈Rn represents the
vector of outputs from the hidden layer, W ∈Rn denotes the
weight vector connecting the hidden units to the output, and ε ∈
R is the approximation error term. In this study, the Gaussian ra-
dialbasisfunctionneuralnetwork(RBFNN)isadoptedastheac-
tivation function, deﬁned by hi(ν) = exp(−∥ν −μi∥2/σ2) ∈
R, for i = 1, 2, . . . , n, where the parameter σ ∈R controls the
spread of each basis function, and μi ∈R speciﬁes the center
position of the i-th Gaussian function.
Assumption 1: The approximation error ε is bounded in mag-
nitude by an unknown constant ψ ∈R, such that |ε| ≤ψ.
B. Quadrotor Dynamics
The quadrotor dynamics can be modeled as:
˙x =
⎡
⎢⎢⎢⎣
˙p
˙q
˙v
˙ω
⎤
⎥⎥⎥⎦=
⎡
⎢⎢⎢⎢⎢⎢⎣
v
1
2q ⊗

0
ω
	
(1/m)(RW
B (q)T + df) + gW
J−1 (τ −ω × Jω + dτ)
⎤
⎥⎥⎥⎥⎥⎥⎦
,
(2)
where p ∈R3 denotes the position, and v ∈R3 represents the
linear velocity in the world frame. The unit quaternion q =
[qw, qx, qy, qz]T represents the orientation of the body frame
relative to the world frame. Furthermore, the angular velocity
ω = [ωx, ωy, ωz]T ∈R3 is expressed in the body frame. Here,
the scalar m denotes the mass, and J = diag(Jx, Jy, Jz) is the
constant inertia matrix. The gravitational acceleration vector is
deﬁned as gW = [0, 0, −9.81]T m/s2.The terms df ∈R3 and
dτ ∈R3 denote the external disturbance force and torque acting
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 10:43:05 UTC from IEEE Xplore.  Restrictions apply.

## Page 3

10968
IEEE ROBOTICS AND AUTOMATION LETTERS, VOL. 10, NO. 10, OCTOBER 2025
Fig. 2.
The ﬁgure illustrates the integration of an adaptive neural network
disturbance observer with model predictive control under disturbances. It de-
scribes the ﬂow of data and control signals between these modules, highlighting
the adaptive updating of the neural network weights, which enables precise and
robust ﬂight control despite disturbances.
on the quadrotor, resulting from aerodynamic drag, wind gusts,
and other environmental inﬂuences.
The operator ⊗denotes quaternion multiplication, which is
explicitly deﬁned as:
q ⊗

0
ω
	
=
⎡
⎢⎢⎢⎣
0
−ωx
−ωy
−ωz
ωx
0
ωz
−ωy
ωy
−ωz
0
ωx
ωz
ωy
−ωx
0
⎤
⎥⎥⎥⎦q.
(3)
The rotation matrix from the body frame to the world frame,
RW
B (q) ∈SO(3), is given by
RW
B (q) =
⎡
⎢⎣
1 −2q2
y −2q2
z
2(qxqy −qwqz)
2(qwqy + qxqz)
2(qxqy + qwqz)
1 −2q2
x −2q2
z
2(qyqz −qwqx)
2(qxqz −qwqy)
2(qwqx + qyqz)
1 −2q2
x −2q2
y
⎤
⎥⎦. (4)
The collective thrust T and torque vector τ in the body frame
are computed as
T =
⎡
⎢⎣
0
0

3
i=0 Ti
⎤
⎥⎦,
τ =
⎡
⎢⎣
ly(−T0 −T1 + T2 + T3)
lx(−T0 + T1 + T2 −T3)
cτ(−T0 + T1 −T2 + T3)
⎤
⎥⎦,
(5)
where lx, ly denote the effective distances from the center of
mass to each rotor along the body axes, and cτ is the torque
coefﬁcient relating the thrust to yaw torque. The individual rotor
thrusts u = [T0, T1, T2, T3]T ∈R4 are the control inputs.
Finally, the discrete-time state-space propagation using the
explicit 4th-order Runge-Kutta (RK4) method is given by
xk+1 = fRK4(xk, uk).
(6)
III. DESIGN OF ANN-MPC ALGORITHM
This section presents an ANN-MPC algorithm. First, the
ANNDO is designed to estimate the total disturbance. Then,
the MPC is developed to track the desired trajectory while
compensating for the total disturbance. The structure of the
integrated controller and observer is shown in Fig. 2.
A. ANNDO Design
Considerthereducedstatevectorz = vW ∈R3,representing
the world-frame velocity. Its dynamical evolution captures both
nominal and uncertain system behaviors through the following
differential equation:
˙z = f(.) + (1/m)df,
(7)
where f(.) is the nominal dynamics:
f(.) = (1/m)RW
B (q)T + gW .
(8)
The observer of z is designed as:
˙ˆz = f(.) + (1/m) ˆ
df + Ase,
(9)
where the estimation error is deﬁned by e = ˆz −z ∈R3, with
As ∈R3×3 being the observer gain matrix, and ˆz ∈R3 the
observer state.
Subtracting (7) from (9) yields the following error dynamics:
˙e = −Ase + (1/m)

ˆ
df −df

.
(10)
For analytical convenience, the three-dimensional distur-
bance vector df = [dx, dy, dz]T ∈R3 is decomposed into its
scalar components dx, dy, dz ∈R. Each component is treated
independently, allowing the error dynamics to be analyzed on a
scalarbasis.Speciﬁcally,letd ∈{dx, dy, dz}denoteanarbitrary
scalar disturbance component, and correspondingly let ˆd be
its estimate. The scalar form of the error dynamics for each
component e ∈R is then expressed as
˙e = −ase + (1/m)( ˆd −d),
(11)
where as > 0 is the scalar gain associated with the correspond-
ing diagonal entry of the gain matrix As.
According to (1), the true disturbance d = W T h(e) + ε is
approximated by the neural network, and its estimate is given
by
ˆd = ˆ
W
T h(e),
(12)
where ˆ
W denotes the estimate of the optimal weight vector
W .The scalar error dynamics can now be expressed in terms of
weight estimation error ˜
W = ˆ
W −W :
˙e = −ase + (1/m)

˜
W
T h(e) −ε

.
(13)
The adaptive update law is designed as
˙ˆW = −(1/m)γe Φ h(e),
(14)
where γ ∈R is a positive adaptation gain and Φ ∈R is a positive
weight gain.
Theorem 1: Consider the closed-loop system described by
equations (7)–(13) with the adaptive law (14). Assume that
Assumption1strictlyholdsandthematrixAs ispositivedeﬁnite.
The observer estimation error e and the parameter estimation
error ˜
W are uniformly ultimately bounded (UUB).
Proof: Consider the Lyapunov function candidate
V = 1
2eT Φe + 1
2γ
˜
W
T ˜
W ,
(15)
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 10:43:05 UTC from IEEE Xplore.  Restrictions apply.

## Page 4

KONG et al.: ANN-MPC: AN ADAPTIVE NEURAL NETWORK-BASED NONLINEAR MODEL PREDICTIVE CONTROL METHOD
10969
where Φ satisﬁes the equation aT
s Φ + Φas = −Q, with Q =
QT > 0 ∈R.
Taking derivative of V along the trajectories yields, and
substituting ˙e and ˙ˆW , yielding
˙V = −1
2eT Qe + (1/m)

eT Φ ˜
W
T h(e) + eT Φε −˜
W
T eΦh(e)

.
(16)
Note that eT Φ ˜
W
T h(e) and ˜
W
T eΦh(e) are equal scalars
and thus exactly cancel each other in the Lyapunov derivative,
yielding
˙V = −1
2eT Qe + (1/m)eT Φε.
(17)
Since Q > 0, the ﬁrst term is negative deﬁnite. According to
Assumption 1, the second term is bounded by |(1/m)eT Φε| ≤
(1/m)∥e∥∥Φ∥∥ψ∥.
Since the Lyapunov function accounts for both the estimation
error e and the parameter error ˜
W , and ˙V is negative semi-
deﬁnite outside a compact set due to bounded approximation
error ε, standard Lyapunov theory ensures e is UUB.
Furthermore, the adaptation law
˙ˆW = −(1/m)γe Φ h(e),
driven by bounded e and bounded basis functions h(e), ensures
that ˜
W is also UUB.
Thus, both the observer error and weight estimation error re-
main bounded, guaranteeing closed-loop stability and parameter
convergence within a bounded neighborhood. This completes
the proof.
Note: The proposed observer framework is theoretically ca-
pable of estimating both disturbance forces and torques. In
this work, we focus on estimating and compensating for the
disturbance forces. However, the disturbance torque estimation
capability can be systematically realized by reformulating the
nominal translational dynamics in equation (7) into correspond-
ing rotational dynamics equations.
B. ANN-MPC Design
To achieve robust quadrotor trajectory tracking under distur-
bances, the MPC incorporating disturbance estimates from the
ANNDO is proposed. We summarize the proposed method in
Algorithm 1.
During each iteration of solving the MPC problem, the es-
timated disturbance force ˆ
dk is assumed to remain constant
along the prediction horizon. The nonlinear trajectory tracking
problem is formulated as a quadratic optimization minimizing
the weighted sum of state and control tracking errors over a
discrete horizon T with N steps:
min
u
ΔxT
NQΔxN +
N−1

k=0

ΔxT
k QΔxk + ΔuT
k RΔuk

s.t. xk+1 = fRK4(xk, uk),
x0 = xinit, uk ∈U, xk ∈X, xN ∈XN,
(18)
where Δxk = xk −xk,r and Δuk = uk −uk,r denote the
tracking errors relative to the reference trajectory. The weighting
matrices Q ≥0 and R > 0 penalize tracking deviations and
Algorithm 1: ANN-MPC Algorithm.
Input: State measurements xk, reference trajectory xk,r
Output: Control command u∗
k(0)
1:
Initialize: u∗
k ←0, ˆdk ←0, ˆ
W ←0, x0 given
2:
for each time step k do
3:
Update the ANNDO weights ˆ
W using (14)
4:
Compute disturbance estimate ˆdk using (12)
5:
Build prediction model by (6)
6:
Apply xk to solve (18) and obtain the optimal
control sequence
u∗
k = {u∗
k(0), u∗
k(1), . . . , u∗
k(N −1)}
7:
Apply the ﬁrst control input u∗
k(0) to the system
8:
end for
control effort, respectively. The sets U, X, and XN represent
admissible input, state, and terminal constraint sets, respectively.
This optimization problem is solved online using a real-time
sequential quadratic programming (SQP) method [30] imple-
mented with the ACADO toolkit [31]. The proof of the recursive
feasibilityoftheproposedMPCandthestabilityofthecombined
system is provided based on the work in [32].
IV. EXPERIMENTS AND RESULTS
During testing, we address the following questions:
1) What is the disturbance estimation performance of
ANNDO?
2) How much does ANN-MPC tracking performance im-
prove in the presence of gusts, unknown loads, and aero-
dynamic drag?
3) Can simulation-based tracking improvements be validated
through ﬂight tests?
Weaddressthesequestionsthroughaseriesofsimulationsand
physical tests, incorporating signiﬁcant disturbances, and fur-
ther illustrate the algorithm’s robustness with the corresponding
video.
To validate the effectiveness of the proposed method,
we conduct comparative studies against four benchmark ap-
proaches: MPC, Gaussian Process Regression-based MPC
(GP-MPC) [20], Extended State Observer-based MPC (ESO-
MPC) [14], and L1 Adaptive Control-integrated MPC (L1-
MPC-Int) [18]. All approaches use the same MPC parameters as
ANN-MPC,ensuringafaircomparison.Performanceisassessed
by comparing the root-mean-square error (RMSE) between the
quadrotor’s position and the desired trajectory.
A. Simulation Setup
WeemploythePython-basedsimulationframeworkfrom [20]
for preliminaryvalidationof theproposedalgorithm. Thesystem
dynamics are numerically integrated using a 4th-order explicit
Runge-Kutta method with a ﬁxed time step of 0.5 ms. The
simulation environment assumes precise quadrotor odometry,
accurate tracking of the commanded single-rotor thrusts, and
instantaneous computation of the MPC. The simulator also
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 10:43:05 UTC from IEEE Xplore.  Restrictions apply.

## Page 5

10970
IEEE ROBOTICS AND AUTOMATION LETTERS, VOL. 10, NO. 10, OCTOBER 2025
TABLE I
COMPARISON OF ACCELERATED CIRCULAR TRAJECTORY TRACKING
PERFORMANCE AT DIFFERENT PEAK VELOCITIES IN SIMULATION
Fig. 3.
Thrust commands of proposed method during accelerated circular
trajectory with a peak velocity of 10 m/s in simulation test.
Fig. 4.
Comparison of disturbance estimated by ANNDO and real disturbance.
accounts for rotor and airframe aerodynamic drag effects. We
designed a set of experiments as follows:
1) Agile Flight Capability Test in Simulation: Tracking per-
formance of ANN-MPC was compared and analyzed against
several other controllers under aggressive ﬂight trajectories. The
effect of increasing speed on tracking accuracy was simulated
on circular trajectories with a radius of 5 m, where peak speeds
variedbetween2and12m/s.Inthesecases,themass,inertia,and
rotor arm lengths of the quadrotors were perfectly known. These
experiments provide insights into the maximum performance
achievable by each method in the presence of an unmodeled
resistance model.
As shown in Table I, each row represents the cumulative
positional tracking error at a given peak speed. As ﬂight speed
Fig. 5.
Tracking performance comparison.
Fig. 6.
Thrust commands of proposed method during accelerated circular
trajectory with a peak velocity of 10 m/s in physical test.
increases, the proposed ANN-MPC maintains accurate trajec-
tory tracking, with signiﬁcantly higher accuracy compared to
other methods. This demonstrates that ANN-MPC effectively
compensatesforunmodeledresistance,enablingagileﬂight.The
simulation results in Fig. 3 demonstrate that the proposed ANN-
MPC algorithm generates smooth thrust commands within all
motors’ saturation limits while exhibiting rapid, stable response
characteristics, thereby verifying its theoretical feasibility.
2) Disturbance Estimate Capability Test: To validate the ex-
ternal disturbance estimation capability of ANNDO, f total(t) =
[sin(ωt), 1, 0]T + ϵ(t)
is
designed
to
model
unknown
disturbance, where ω is the angular frequency of the periodic dis-
turbance component, and ϵ(t) = N(0, σ2(t)) · [1, 1, 1]T ∈R3
denotes a noise disturbance modeled by a zero-mean Gaussian
distribution.
The comparison between the actual disturbance and the dis-
turbance estimated by the ANNDO is shown in Fig. 4. The
results indicate that the estimated disturbance converges rapidly
and exhibits excellent tracking performance, validating the ef-
fectiveness of the proposed ANNDO in accurately estimating
disturbances.
B. Physical Experiments Setup
Physical experiments were carried out using a custom-built
quadrotor with a total mass of 250 g. The vehicle was equipped
with a propulsion system comprising four Smoox 1404 brush-
less motors paired with 6045 three-bladed propellers, yielding
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 10:43:05 UTC from IEEE Xplore.  Restrictions apply.

## Page 6

KONG et al.: ANN-MPC: AN ADAPTIVE NEURAL NETWORK-BASED NONLINEAR MODEL PREDICTIVE CONTROL METHOD
10971
Fig. 7.
The results of the hovering with unknown load experiment. Left: Experimental setup for hovering with an unknown load, using a 90 g battery as the
suspended load. Center: Tracking error during hovering with the load. Right: Real-time disturbance estimation using ANNDO.
Fig. 8.
The results of the hovering anti-wind disturbance experiment: Left: Experimental setup for hovering in wind. Center: Tracking error during wind hover.
Right: Comparison of disturbance estimation between ANN-MPC and L1-MPC-Int.
a maximum thrust-to-weight ratio of 4:1 to ensure adequate
maneuverability.Thequadrotor’sembeddedsystemisbasedona
custom-designed ﬂight controller board running PX4 ﬁrmware,
employing the STM32H743 microcontroller.
The localization is achieved using an OptiTrack motion cap-
ture system with 46 infrared cameras, providing high-precision
full-state estimation, including position, velocity, attitude, and
angular velocity, within a 20 × 10 × 10 m3 experimental
space. The proposed algorithm operates at 50 Hz on a laptop
equipped with an Intel i7 processor, implementing a prediction
horizon of N = 20. Control commands, including collective
thrust and desired body rates, are transmitted to the quadrotor
via an LR24 wireless module, while the onboard PID controller
handles low-level command tracking. The software architecture
is based on the Robot Operating System (ROS). To evaluate the
practical effectiveness of the proposed algorithm, we conducted
the following tests:
1) Agile Flight Capability Test in Physical Flight: Perfor-
mance comparison of various algorithms was conducted during
the tracking of an accelerated circular trajectory. The experi-
mental conﬁguration mirrored that of Simulation Experiment 1,
featuring a circular path with a radius of 4 meters, while the peak
velocity progressively increased from 2 m/s to 10 m/s.
As shown in Fig. 5, the tracking accuracy of ANN-MPC is
signiﬁcantly improved by over 60% compared to the nominal
MPC, demonstrating that the ANN-MPC method effectively
compensatesforunmodeledaerodynamicdragresiduals,outper-
forming other disturbance compensation strategies. The thrust
commands in the physical test are shown in Fig. 6. The results
are highly consistent with the simulation results, which further
veriﬁes the feasibility and effectiveness of the proposed algo-
rithm deployed in the real world.
2) Robustness to Mass Mismatch in Physical Flight: To val-
idate the robustness of the proposed algorithm in the presence
of unknown loads, we added a 90 g payload to the quadro-
tor to simulate model uncertainties. As shown in Fig. 7, the
GP-MPC and MPC methods exhibit signiﬁcant oscillations and
large steady-state errors under mass mismatch. In contrast, the
ANN-MPC method enhances steady-state accuracy to within
3 cm, reducing the error by approximately 24 cm compared
to the MPC, representing an 88.89% relative improvement.
This demonstrates that the ANN-MPC method can quickly
adapt to mass mismatch and signiﬁcantly enhance system
stability.
In addition, this experiment primarily validates the estimation
and compensation of matched disturbances along the Z-axis
of the quadrotor. Notably, during ﬂight, as the battery voltage
decays, the ANN method promptly detects and effectively com-
pensates for disturbances caused by changes in voltage. These
results highlight the exceptional robustness and adaptability of
the ANN-MPC in dynamic environments.
3) Robustness to Wind Disturbance During Hovering: We
further validated the robustness of the proposed algorithm
through hover ﬂight in windy conditions. The wind, generated
by an industrial fan, directly impacted the Y-axis of the quadro-
tor during hover, with the maximum wind speed at the hover
position reaching approximately 12 m/s, equivalent to a force 5
wind on the Beaufort scale.
Fig. 8 shows a comparison of the real-time total error for
various methods. Compared to the uncompensated MPC and
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 10:43:05 UTC from IEEE Xplore.  Restrictions apply.

## Page 7

10972
IEEE ROBOTICS AND AUTOMATION LETTERS, VOL. 10, NO. 10, OCTOBER 2025
Fig. 9.
Violin plot of position tracking RMSE distributions from complex
disturbance ﬂight experiments, comparing the performance of different methods.
the GP-MPC method, the steady-state error of the ANN-MPC
method was reduced by approximately 25 cm. This indicates that
the ANN-MPC method can effectively estimate and compensate
for time-varying external disturbances. Compared to the L1-
MPC-Int method, the ANN-MPC not only accurately estimates
the disturbance but also produces very low disturbance noise,
demonstrating excellent estimation accuracy. Furthermore, the
ANN-MPC method requires no additional ﬁltering and can be
directly integrated with the dynamic equations of the quadrotor,
enhancing its robustness.
4) Robustness to Complex Disturbances: In order to assess
the robustness of the proposed method under more complex con-
ditions, various disturbances were introduced, including gusts,
unknownloads, andunmodeledaerodynamiceffects. Thetaskof
the quadcopter is to ﬂy along a circular trajectory with a radius
of 3 meters at a speed of 2 m/s. Throughout the experiment,
three industrial fans generated a wind ﬁeld within a radius of 3
meters, producing a maximum wind speed of 12 m/s. In addition,
a 90 g mass is attached to simulate the effects of unknown load
interference.
Each method was tested in ﬁve ﬂight experiments, and the
RMSE distribution of position tracking is summarized in Fig. 9.
The results indicate that, in the presence of complex distur-
bances, the proposed method exhibits the lowest concentration
of error distribution, with tracking performance at least 50%
better than MPC and at least 15% better than L1-MPC-Int.
This demonstrates that the ANN-MPC method has exceptional
adaptability to complex and unmodeled external disturbances,
such as gusts and load variations.
5) Outdoor Experiments: As demonstrated in Fig. 10, the
quadrotors successfully tracked an accelerated 3D lemniscate
trajectory under outdoor windy conditions with wind speeds of
approximately 5 m/s, and the corresponding tracking perfor-
mance is presented in Fig. 11. Under positioning discrepancies
conditions, the ANN-MPC achieved an RMSE less than 15 cm,
representing an improvement exceeding 60% compared to the
baseline MPC. Notably, while the RMSE demonstrated an in-
creasing trend with higher ﬂight speeds and more aggressive
trajectories along the green segment, the overall tracking error
of ANN-MPC remained at a low level. These results conﬁrm
the adaptability and robustness of ANN-MPC in challenging
outdoor wind environments.
Fig. 10.
Experimental scene in outdoor environments under strong wind
conditions.
Fig. 11.
Comparison of quadrotor tracking performance under different con-
trol methods:(a)MPC, RMSE = 0.4112 m; (b)ANN-MPC, RMSE = 0.1495 m.
V. CONCLUSION
This letter proposes an ANN-MPC algorithm for robust tra-
jectory tracking of quadrotors under disturbance conditions.
First, ANNDO is designed for real-time disturbance estimation,
ensuring convergence of the estimation error using Lyapunov-
based methods. Subsequently, the disturbance estimated by
ANNDO is integrated into the predictive model to construct
an observer-based MPC. The efﬁcacy and practicality of the
approach have been thoroughly validated through both simu-
lation studies and real-world ﬂight experiments. Future work
will extend the adaptation framework to rotational dynamics
and investigate disturbance prediction models using historical
estimation data, potentially enhancing MPC prediction accuracy
for aggressive maneuvers.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 10:43:05 UTC from IEEE Xplore.  Restrictions apply.

## Page 8

KONG et al.: ANN-MPC: AN ADAPTIVE NEURAL NETWORK-BASED NONLINEAR MODEL PREDICTIVE CONTROL METHOD
10973
REFERENCES
[1] H. Li, H. Wang, C. Feng, F. Gao, B. Zhou, and S. Shen, “AutoTrans: A
complete planning and control framework for autonomous UAV payload
transportation,” IEEE Robot. Automat. Lett., vol. 8, no. 10, pp. 6859–6866,
Oct. 2023.
[2] G. Loianno and D. Scaramuzza, “Special issue on future challenges and
opportunities in vision-based drone navigation,” J. Field Robot., vol. 37,
no. 4, pp. 495–496, Jun. 2020.
[3] B. Tang et al., “Bubble Explorer: Fast UAV exploration in large-scale
and cluttered 3D-environments using occlusion-free spheres,” in Proc.
IEEE/RSJ Int. Conf. Intell. Robots Syst., 2023, pp. 1118–1125.
[4] T.P.NascimentoandM.Saska,“Positionandattitudecontrolofmulti-rotor
aerial vehicles: A survey,” Annu. Rev. Control, vol. 48, pp. 129–146, 2019.
[5] D. Wang, Q. Pan, Y. Shi, J. Hu, and C. Zhao, “Efﬁcient nonlinear model
predictive control for quadrotor trajectory tracking: Algorithms and exper-
iment,” IEEE Trans. Cybern., vol. 51, no. 10, pp. 5057–5068, Oct. 2021.
[6] M. Greeff and A. P. Schoellig, “Flatness-based model predictive control for
quadrotor trajectory tracking,” in Proc. IEEE/RSJ Int. Conf. Intell. Robots
Syst., 2018, pp. 6740–6745.
[7] G. Yu, J. Reis, and C. Silvestre, “Quadrotor neural network adaptive
control: Design and experimental validation,” IEEE Robot. Automat. Lett.,
vol. 8, no. 5, pp. 2574–2581, May 2023.
[8] M. O’Connell et al., “Neural-ﬂy enables rapid learning for agile ﬂight in
strong winds,” Sci. Robot., vol. 7, no. 66, 2022, Art. no. eabm6597.
[9] H. Lee and H. J. Kim, “Trajectory tracking control of multirotors from
modelling to experiments: A survey,” Int. J. Control, Automat. Syst.,
vol. 15, no. 1, pp. 281–292, 2017.
[10] S. Sun, A. Romero, P. Foehn, E. Kaufmann, and D. Scaramuzza, “A com-
parative study of nonlinear MPC and differential-ﬂatness-based control for
quadrotor agile ﬂight,” IEEE Trans. Robot., vol. 38, no. 6, pp. 3357–3373,
Dec. 2022.
[11] J. Han, “From PID to active disturbance rejection control,” IEEE Trans.
Ind. Electron., vol. 56, no. 3, pp. 900–906, Mar. 2009.
[12] Z. Gao, “Scaling and bandwidth-parameterization based controller tun-
ing,” in Proc. Amer. Control Conf., Denver, CO, USA, 2003, pp. 4989–
4996, doi: 10.1109/ACC.2003.1242516.
[13] G. Tang, W. Xue, X. Huang, and K. Song, “On error-driven nonlinear ESO
based control design with application to air–fuel ratio control of engines,”
Control Eng. Pract., vol. 143, 2024, Art. no. 105808.
[14] C. Chen, X. Zhang, and X. Peng, “Trajectory tracking control of four-rotor
UAV based on nonlinear extended state observer and model predictive
control in wind disturbance environment,” J. Phys., Conf. Ser., vol. 2764,
no. 1, 2024, Art. no. 012075.
[15] D. Hanover, P. Foehn, S. Sun, E. Kaufmann, and D. Scaramuzza, “Perfor-
mance, precision, and payloads: Adaptive nonlinear MPC for quadrotors,”
IEEE Robot. Automat. Lett., vol. 7, no. 2, pp. 690–697, Apr. 2022.
[16] K. Pereida and A. P. Schoellig, “Adaptive model predictive control
for high-accuracy trajectory tracking in changing conditions,” in Proc.
IEEE/RSJ Int. Conf. Intell. Robots Syst., 2018, pp. 7831–7837.
[17] J.Pravitra,K.A.Ackerman,C.Cao,N.Hovakimyan,andE.A.Theodorou,
“L1-Adaptive MPPI architecture for robust and agile control of multiro-
tors,”inProc.IEEE/RSJInt.Conf.Intell.RobotsSyst.,2020,pp.7661–766.
[18] K. Y. Chee, T. C. Silva, M. A. Hsieh, and G. J. Pappas, “Enhancing
sample efﬁciency and uncertainty compensation in learning-based model
predictive control for aerial robots,” in Proc. IEEE/RSJ Int. Conf. Intell.
Robots Syst., 2023, pp. 9435–9441.
[19] J. Kabzan, L. Hewing, A. Liniger, and M. N. Zeilinger, “Learning-based
model predictive control for autonomous racing,” IEEE Robot. Automat.
Lett., vol. 4, no. 4, pp. 3363–3370, Oct. 2019.
[20] G. Torrente, E. Kaufmann, P. Foehn, and D. Scaramuzza, “Data-driven
MPC for quadrotors,” IEEE Robot. Automat. Lett., vol. 6, no. 2, pp. 3769–
3776, Apr. 2021, doi: 10.1109/LRA.2021.3061307.
[21] T. Salzmann, E. Kaufmann, J. Arrizabalaga, M. Pavone, D. Scaramuzza,
and M. Ryll, “Real-time neural MPC: Deep learning model predictive
control for quadrotors and agile robotic platforms,” IEEE Robot. Automat.
Lett., vol. 8, no. 4, pp. 2397–2404, Apr. 2023.
[22] K.Huang,R.Rana,A.Spitzer,G.Shi,andB.Boots,“DATT:Deepadaptive
trajectory tracking for quadrotor control,” 2023.
[23] K. Y. Chee, T. Z. Jiahao, and M. A. Hsieh, “KNODE-MPC: A knowledge-
based data-driven predictive control framework for aerial robots,” IEEE
Robot. Automat. Lett., vol. 7, no. 2, pp. 2819–2826, Apr. 2022.
[24] A. Saviolo, G. Li, and G. Loianno, “Physics-inspired temporal learning
of quadrotor dynamics for accurate model predictive trajectory tracking,”
IEEE Robot. Automat. Lett., vol. 7, no. 4, pp. 10256–10263, Oct. 2022.
[25] R. Yang, L. Zheng, J. Pan, and H. Cheng, “Learning-based predictive path
following control for nonlinear systems under uncertain disturbances,”
IEEE Robot. Automat. Lett., vol. 6, no. 2, pp. 2854–2861, Apr. 2021.
[26] Y. Ouyang, L. Xue, L. Dong, and C. Sun, “Neural network-based
ﬁnite-time distributed formation-containment control of two-layer quadro-
tor UAVs,” IEEE Trans. Syst., Man, Cybern. Syst., vol. 52, no. 8,
pp. 4836–4848, Aug. 2022.
[27] Q. Xu, Z. Wang, and Z. Zhen, “Adaptive neural network ﬁnite time
control for quadrotor UAV with unknown input saturation,” Nonlinear
Dyn., vol. 98, no. 3, pp. 1973–1998, 2019.
[28] M. Wei, L. Zheng, H. Li, and H. Cheng, “Adaptive neural network-
based model path-following contouring control for quadrotor under di-
versely uncertain disturbances,” IEEE Robot. Automat. Lett., vol. 9, no. 4,
pp. 3751–3758, Apr. 2024.
[29] Y. Zou and Z. Zheng, “A robust adaptive RBFNN augmenting backstep-
ping control approach for a model-scaled helicopter,” IEEE Trans. Control
Syst. Technol., vol. 23, no. 6, pp. 2344–2352, Nov. 2015.
[30] M. Diehl, H. Bock, H. Diedam, and P. -B. Wieber, “Fast direct multiple
shooting algorithms for optimal robot control,” in Fast Motions in Biome-
chanics and Robotics: Optimization and Feedback Control, M. Diehl and
K. Mombaur, Eds. Berlin, Heidelberg: Springer, 2006, pp. 65–93.
[31] B. Houska, H. J. Ferreau, and M. Diehl, “ACADO toolkit—An open-
source framework for automatic control and dynamic optimization,” Op-
timal Control Appl. Methods, vol. 32, no. 3, pp. 298–312, 2011.
[32] L.Xuetal.,“Fixed-timedisturbanceobserver-basedMPCrobusttrajectory
tracking control of quadrotor,” IEEE/ASME Trans. Mechatron., Dec. 2024,
doi: 10.1109/TMECH.2024.3503062.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 10:43:05 UTC from IEEE Xplore.  Restrictions apply.
