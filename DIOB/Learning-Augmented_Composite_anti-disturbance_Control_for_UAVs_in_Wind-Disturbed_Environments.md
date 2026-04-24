# Learning-Augmented_Composite_anti-disturbance_Control_for_UAVs_in_Wind-Disturbed_Environments.pdf

## Page 1

Learning-Augmented Composite anti-disturbance Control for UAVs in
Wind-Disturbed Environments
Yixin Hu1, Li Fan2, Chao Xu3
Abstract— This study introduces a control framework de-
signed to improve the disturbance rejection capability of
unmanned aerial vehicles (UAVs) by integrating learning-
augmented disturbance estimation into the conventional com-
posite hierarchical anti-disturbance control (CHADC) archi-
tecture. A sensorless freestream velocity estimation scheme is
developed to enable real-time freestream velocity estimation
without requiring additional hardware. Leveraging this estima-
tion, Gaussian Process Regression (GPR) is employed to accu-
rately model and integrate with model predictive control (MPC)
to compensate for wind-induced external forces. Furthermore,
an SO(3)-based backstepping attitude controller is designed,
incorporating a nonlinear disturbance observer (NDO) to ac-
tively compensate for external moment disturbances. Rigorous
Lyapunov analysis guarantees the bounded convergence of both
attitude and estimation errors, ensuring robust performance in
the presence of external disturbances. The effectiveness of the
proposed method is validated through high-fidelity simulations
and real-world flight experiments conducted on a medium-sized
tail-sitter UAV. The experimental results demonstrate significant
improvements in robustness under complex operating condi-
tions.
I. INTRODUCTION
Recently, unmanned aerial vehicles (UAVs) have under-
gone significant advancements due to their promising appli-
cations across various industries, including agriculture [1],
logistics [2], and surveillance [3], [4]. However, ensuring
the safe and precise flight of UAVs in wind-disturbed en-
vironments remains a challenging task. The accurate esti-
mation of wind-induced external disturbances, along with
the development of a robust control strategy, is essential for
enhancing trajectory tracking performance in the presence
of such disturbances. The wind-induced disturbances are
typically modeled as functions of aerodynamic coefficients
and freestream velocity. Although wind tunnel experiments
can provide accurate measurements of these coefficients,
they often involve significant experimental costs. Similarly,
freestream velocity can be obtained using onboard sensors
such as pitot tubes, but high-precision measurements also
require expensive instrumentation.
* This research was supported by the Intelligent Aerospace System
Leading Innovation Team Program (Grant No. 2022R01003) and the
Lingyan Research Project (Grant No. 2024C01171) of Zhejiang Province.
(Corresponding authors: Li Fan; Chao Xu.)
1Yixin Hu is with the College of Control Science and Engineering, Zhe-
jiang University, Hangzhou 310027, China, 12332055@zju.edu.cn
2Li Fan is with the Huzhou Institute of Zhejiang University, Huzhou
313000, China, and also with Zhejiang University, Hangzhou 310027, China,
fanli77@zju.edu.cn
3Chao Xu is with the Institute of Cyber-Systems and Control, College of
Control Science and Engineering, Zhejiang University, Hangzhou 310027,
China, and also with Huzhou Institute of Zhejiang University, Huzhou
313000, China cxu@zju.edu.cn
Fortunately, significant advances in intelligent control
strategies have enabled high-precision maneuverability and
safety control in a wide range of mission conditions. On
the one hand, traditional robust control methods remain
foundational approaches for disturbance rejection in UAVs.
Representative techniques include model predictive control
(MPC) [5], incremental nonlinear dynamic inversion control
(INDI) [6], sliding mode control (SMC) [7], and backstep-
ping control [8]. These methods are well-regarded for their
theoretical rigor and demonstrated capability to maintain
stability under model uncertainties and external disturbances.
Although these controllers demonstrate notable performance
in theory, their practical application to UAVs is often con-
strained by the need for accurate dynamic models and ideal-
ized assumptions about external disturbances. In addition, the
requirements for high-fidelity state measurements, complex
hardware setups, and significant computational resources
further limit their deployment in real-world scenarios. For
instance, the optical encoder-based motor speed feedback
used in INDI [6] is impractical for most UAVs.
On the other hand, disturbance estimation and compensa-
tion–based control strategies provide an alternative approach
by explicitly identifying external disturbances and compen-
sating for residual dynamics within the control loop. The
core of this strategy involves developing a rapid-response,
high-precision observer, thereby enabling the controller to
maintain robustness under conditions of model uncertainty
and external disturbances. Various disturbance observation
strategies have been proposed to enhance UAV robustness
under external disturbances. In [9], an H∞disturbance
observer is developed to improve hovering accuracy un-
der crosswind conditions. However, reliance on linearized
frequency-domain models limits its effectiveness in highly
nonlinear or dynamic environments. To address aerody-
namic disturbances more directly, a model-based observer
is introduced targeting drag force compensation in [10],
while a wind speed observer leveraging known disturbance
characteristics to improve trajectory tracking is designed in
[11]. Additionally, cascade control frameworks with dual-
loop nonlinear disturbance observers (NDOs) are employed
to mitigate complex disturbances such as actuator faults [12],
[13] and ground effects [14], [15].
Building upon this foundation, the composite hierarchi-
cal anti-disturbance control (CHADC) proposed in [16],
[17] represents a structured approach to simultaneously ad-
dress multiple disturbances. By integrating a robust baseline
controller and a disturbance observer (DO), the CHADC
achieves robust performance and accurate disturbance es-
This article has been accepted for publication in IEEE Transactions on Aerospace and Electronic Systems. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TAES.2026.3657729
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 13:00:03 UTC from IEEE Xplore.  Restrictions apply.

## Page 2

timation [10], [18]. This hierarchical architecture enables
modularity and a clear separation of control and estimation
tasks, making it particularly suitable for complex aerial
systems operating in uncertain environments.
However, while CHADC provides a principled framework
for multi-disturbance handling, its performance still depends
on accurate modeling and rapid-response observer design. To
further improve adaptability and generalization under diverse
and time-varying conditions, recent advances in machine
learning offer promising approaches to improve traditional
CHADC architectures. Specifically, the emergence of the
EVOLVER framework proposed in [19], the meta-model ap-
proaches in [20], [21], and the reinforcement learning method
in [22] have allowed improved prediction of disturbances.
At the same time, Gaussian Process Regression (GPR)
offers several advantages over these methods, including
its non-parametric flexibility without requiring partial prior
knowledge of disturbance structures, inherent probabilistic
uncertainty quantification for robust and cautious predictions,
and superior data efficiency in limited-sample scenarios [23].
While these methods demonstrate outstanding performance
in disturbance estimation, their full potential could be further
realized if carefully integrated into a comprehensive con-
trol framework. To fully leverage such observers, previous
studies have explored learning-based disturbance estimation
in the contexts of survival intelligence and safety [24],
immunity [25], and green control technologies for unmanned
systems [26]. However, integrating such learning-based ob-
servers into the CHADC framework and applying them to
significant wind-disturbance rejection remains a challeng-
ing task. Therefore, inspired by the CHADC architecture
and data-driven techniques, this study proposes a learning-
augmented composite anti-disturbance control framework for
large-mass UAVs operating in wind-disturbed environments.
To validate the proposed framework, a custom-built tail-
sitter UAV with a wingspan of 1.625 m, shown in Fig. 1, is
employed. Tail-sitter UAVs offer an effective compromise
between quadrotors and fixed-wing aircraft by combining
VTOL capabilities with high aerodynamic efficiency, while
avoiding the mechanical complexity of tilting mechanisms
[27]. However, this configuration also introduces distinct
control challenges. During vertical flight, the large frontal
area significantly increases the sensitivity of the platform
to wind disturbances. Moreover, the 16 kg aircraft, equipped
with 21-inch propellers, experiences notable acceleration and
angular velocity noise due to strong thrust generation. These
factors complicate the task of maintaining high-precision
control under wind-disturbed conditions.
Rather than being a limitation, these disturbance-prone
characteristics make the tail-sitter UAV an ideal platform
for evaluating the effectiveness of advanced anti-disturbance
control strategies. The inherent dynamic complexity of this
system, combined with environmental uncertainty, provides
a realistic and rigorous experimental setting that is particu-
larly suitable for evaluating the proposed learning-augmented
composite control framework in practical applications.
The main contributions of this work are summarized as
Wingspan:1.625 m
0.552 m
Height:1.05 m
0.765 m
Fig. 1: The discussed tail-sitter UAV and the comparison of
acceleration noise.
follows:
• This study introduces an integration of learning-
augmented disturbance estimation into the CHADC
framework. An attitude-based freestream velocity esti-
mation scheme is developed to infer aerodynamic con-
ditions in real time without requiring additional onboard
sensors. By utilizing the estimated freestream velocity,
the GP-MPC framework is integrated with hierarchi-
cal anti-disturbance control to accurately model and
compensate for external wind disturbances, enabling
robust and precise trajectory tracking under complex
aerodynamic conditions.
• An SO(3)-based backstepping attitude controller is de-
veloped, augmented with an NDO to actively compen-
sate for external moment disturbances. The Lyapunov-
based stability analysis rigorously demonstrates that
both the attitude tracking error and the disturbance
estimation error asymptotically converge to a bounded
region, thereby ensuring fast and robust attitude regu-
lation even under aggressive and highly dynamic flight
conditions.
• The proposed control framework is implemented on
a medium-sized tail-sitter UAV with significant mass
and subjected to strong external disturbances. The per-
formance is validated through high-fidelity simulations
and real-world flight experiments, including challeng-
ing scenarios involving substantial propeller-induced
airflow. The results indicate that, in both simulations
and real-world flight experiments, the proposed method
achieves superior trajectory tracking performance com-
pared to baseline controllers, with more than a 15%
improvement in the root mean square error (RMSE)
and a maximum reduction in tracking error exceeding
30%. Furthermore, the estimated disturbances not only
enable more accurate identification of disturbances but
also substantially reduce the estimation delay relative to
This article has been accepted for publication in IEEE Transactions on Aerospace and Electronic Systems. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TAES.2026.3657729
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 13:00:03 UTC from IEEE Xplore.  Restrictions apply.

## Page 3

the baseline approach. The results demonstrate the ro-
bustness and effectiveness of the method under realistic
operating conditions.
The remainder of this paper is organized as follows.
Section II introduces the preliminaries, including the fun-
damentals of GPR and the modeling of UAV dynamics.
The proposed control architecture is detailed in Section III.
Experimental validation is presented in Section IV, followed
by concluding remarks in Section V.
II. METHODOLOGY
A. Notation
Throughout this study, the map (·)× defines the skew-
symmetric operator of a vector x =
 x1
x2
x3
T as
x× =


0
−x3
−x2
x3
0
x1
−x2
x1
0

.
(1)
Conversely, the vee-map (·)∨is defined as the inverse of
the hat map: (x×)∨= x. The operator ∥·∥denotes the
standard Euclidean norm for vectors or the corresponding
induced norm for matrices. While tr (·) represents the trace
of a matrix, λm (·) and λM (·) denote the minimum and
maximum eigenvalues of a matrix, respectively.
B. Gaussian process regression
GPR is a nonparametric, probabilistic modeling frame-
work that offers a mathematically rigorous and flexible
approach for learning unknown functions. Owing to its
ability to model complex system dynamics and quantify
predictive uncertainty, this paper employs GPR to model the
residual dynamics in wind-disturbed environments, which are
challenging to capture using first-principles models alone.
Consider the case where the input x ∈Rn and the
corresponding noisy observations y ∈R are assumed to
follow an unknown underlying relationship,
yi = f(xi) + ϵi,
ϵi ∼N(0, σ2
n),
(2)
where f(·) represents the unknown, possibly nonlinear
function, and ϵi denotes an independent Gaussian noise
process. The fundamental concept of GPR is to treat the
unknown function f as a Gaussian process (GP), f(·) ∼
GP(µ(·), k(·, ·)), which is fully specified by its mean func-
tion µ(·) and covariance function k(·, ·), defined as,
(
µ(x) = E[f(x)],
k(x, x′) = E[(f(x) −µ(x))(f(x′) −µ(x′))].
(3)
By learning from historical observations D = {(xi, yi)}n
i=1,
GPR can provide both point estimates of disturbance forces
and the associated variance. Since no prior knowledge is
available for the wind disturbance, a zero mean function
µ(x) = 0, combined with a squared-exponential (SE) covari-
ance function, is commonly chosen for the smooth estimation
of f(·),
k(x, x′) = σ2
f exp

−1
2(x −x′)⊤Λ−1(x −x′)

,
(4)
where σ2
f is the signal variance and Λ determines the
smoothness of f(·) with respect to x.
Once the GP prior is defined, the joint distribution of the
observed data y and the predicted function values f(x∗) at
a test point x∗is given by,

y
f(x∗)

∼N

0,
K(X, X) + σ2
nI
K(X, x∗)
K(x∗, X)
k(x∗, x∗)

,
(5)
where X = [x1, . . . , xn]⊤and y = [y1, . . . , yn]⊤denote
the training inputs. K ∈Rn×n is the kernel matrix with
elements Kij = k(xi, xj). The kernel vector for the test
point x∗is defined as k∗= [k(x1, x∗), . . . , k(xn, x∗)]⊤
and k∗∗= k(x∗, x∗). Consequently, given the training data,
the posterior predictive distribution of the residual dynamics
f(x∗) is Gaussian and is characterized by,
(
µg(x∗) = E[f(x∗) | D] = k⊤
∗(K + σ2
nI)−1y,
σ2
g(x∗) = Var[f(x∗) | D] = k∗∗−k⊤
∗(K + σ2
nI)−1k∗.
(6)
To enable accurate and reliable disturbance estimation,
the hyperparameters θ
= {σ2
f, σ2
n, l} are optimized by
maximizing the log marginal likelihood of the training data,
log p(y|X, θ) = −1
2y⊤K−1
y y −1
2 log |Ky| −n
2 log(2π),
(7)
where Ky = K(X, X)+σ2
nI is the regularized kernel matrix.
Remark 1. To avoid high-dimensional matrix operations, two
independent GPs are trained separately for each dimension of
the wind disturbance. Building upon the function estimates
µg(x∗) and associated uncertainty quantification σ2
g(x∗),
GPR enables the construction of accurate, uncertainty-aware
residual dynamic models. These models are essential for
constructing precise and comprehensive dynamic models
in the presence of model uncertainties, thereby facilitating
reliable control performance.
C. Dynamics of Tail-sitter
Two related coordinate system are defined in Fig. 2.
The inertial frame {xI, yI, zI} is fixed on the ground and
points north, east, and downward. The body-fixed frame
{xB, yB, zB} is fixed at the center of mass and points toward
the heading, left, and upward directions of the vehicle. The
kinematic and dynamic model of the tail-sitter considering
disturbances can be expressed as follows,







˙p = v,
˙v = aT Re3 −ge3 + Rdf,
˙R = Rω×,
J ˙ω = −ω×Jω + M + dτ,
(8)
where J denote the inertia of the vehicle, p and v are the
position and velocity of the vehicle in the inertial frame,
respectively. ω represents the angular velocity in the body-
fixed frame, and R denotes the rotation matrix from the
body-fixed frame to the inertial frame. aT and M represent
the total acceleration and moments generated by the motors,
while df and dτ denote the unmodeled force and moment
in the body-fixed frame, respectively.
This article has been accepted for publication in IEEE Transactions on Aerospace and Electronic Systems. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TAES.2026.3657729
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 13:00:03 UTC from IEEE Xplore.  Restrictions apply.

## Page 4

III. CONTROL ARCHITECTURE
In this section, the overall anti-disturbance control archi-
tecture is detailed, as illustrated in Fig. 2. Recognizing that
changes in the translational loop are driven by adjustments
in the rotational loop, the control scheme employs a cas-
caded structure in which the rotational loop operates at a
significantly higher update frequency than the translational
loop. Building upon the concept of CHADC, both learning-
augmented and NDOs are incorporated into the transla-
tional and rotational control loops. Specifically, the GP-
MPC framework, augmented by an attitude-based freestream
velocity estimator, enables the system to accurately infer
aerodynamic conditions in real time and compensate for
wind-induced external forces through data-driven method.
In the inner loop, a singularity-free SO(3) backstepping
controller is integrated with an NDO to achieve smooth and
robust attitude tracking under moment disturbances.
A. Translational Control Loop
The objective of translational control is to generate the
control vector u = [aT , qw, qx, qy, qz]T to track the desired
trajectory xref =

xref, yref, zref, vref
x , vref
y , vref
z
T. In this
study, MPC is employed as the baseline controller to stabilize
the translational dynamics in Eq. (8) through the quadratic
optimal control problem formulated as follows,
min
uk
N−1
X
k=0
xk −xref
k
2
Q +
N−1
X
k=0
uk −uref
k
2
W
+
N−1
X
k=0
∥uk∥2
Wu +
N−1
X
k=1
∥˜uk∥2
S +
xN −xref
N
2
P (9)
s.t.
xk+1 = fd(xk, uk) + d(xk, uk),
k ∈[0, N −1],
umin ≤uk ≤umax,
k ∈[0, N −1],
where terminal state reference is given by xref
N
and ˜uk =
uk −uk−1 is introduced to discourage sudden variations
in control inputs, which may otherwise lead to undesirable
performance. The matrices Q, W, Wu, S and P are the
corresponding diagonal weight matrices, while umin and
umax denote the lower and upper limits on the control inputs.
The overall dynamics of the vehicle consist of a discrete-time
nominal model and a residual model. The nominal model
fd is obtained by discretizing the continuous-time dynamics
using numerical integration techniques, such as the fourth-
order Runge–Kutta (RK4) method. The residual term d,
learned through GPR, accounts for both internal and external
disturbances not captured by the nominal model. It represents
the discrepancy between the actual system dynamics and the
nominal model, and is formulated as follows,
d (xk, uk) = [0, 0, 0, adx, ady, adz]⊤,
(10)
where adx, ady, adz denote the disturbance accelerations in
the inertial frame.
Remark 2. Given the unique aerodynamic characteristics of
the tail-sitter UAV, particularly the large frontal area during
VTOL, the system is especially susceptible to varying wind
disturbances. These effects are challenging to model explic-
itly using traditional approaches. The learned GP models,
by leveraging data-driven nonparametric regression, offer a
flexible way to represent the residual dynamic behavior of
the tail-sitter UAV under varying flight conditions. Rather
than capturing the complete vehicle dynamics, learning only
the residual dynamics greatly simplifies the learning problem
while still capturing the critical unmodeled effects. The
resulting residual estimates can then be incorporated into
the GP–MPC framework to provide compensation in real
time, which helps enhance control robustness for tail–sitter
platforms operating in challenging environments [28], [29].
B. GP-Based Disturbance Regression
The GP-MPC frameworks presented in [26], [30], [31]
are primarily developed under wind-free conditions, with
the objective of improving trajectory tracking accuracy by
learning residual dynamics induced by aerodynamic drag
rather than wind-induced disturbances. In these studies,
ground speed is typically equated with freestream veloc-
ity, and residual forces resulting from aerodynamic drag
are modeled using GPR as a function of ground velocity.
However, the approximation of freestream velocity by ground
speed becomes invalid under strong wind disturbances during
hovering. This discrepancy leads to significant modeling
errors in the aforementioned GP-MPC frameworks trained
under wind-free conditions, limiting their effectiveness in
wind-affected scenarios.
To address this limitation without requiring additional
sensors, inspired by previous work [32], [33], we propose a
sensorless freestream velocity estimation method that utilizes
only onboard measurements. A longitudinal wind disturbance
acting on the hovering vehicle enables the derivation of the
following relation from equilibrium force analysis,
mg tan θ = 1
2cDρA ∥v∞∥2 ,
(11)
where A denotes the reference area, cD is the drag coeffi-
cient, ρ presents the air density and g is the gravitational
acceleration. A similar equilibrium analysis can be extended
to the case of lateral wind disturbances. Modest simplifi-
cations yield the following approximation of the freestream
velocity vector,
v∞=


hx(θ)
hy(ϕ)
0

,
(12)
where hx(θ) and hy(ϕ) are functions of the pitch angle
θ and roll angle ϕ, respectively, derived from the corre-
sponding equilibrium conditions. To identify the functional
relationship between tilt angles and freestream velocity, the
vehicle is maintained in steady flight across a range of ground
speeds, while the corresponding tilt angles are recorded.
Under wind-free conditions, ground speed serves as an
approximation of freestream velocity. The maneuvers are
performed independently along the longitudinal and lateral
This article has been accepted for publication in IEEE Transactions on Aerospace and Electronic Systems. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TAES.2026.3657729
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 13:00:03 UTC from IEEE Xplore.  Restrictions apply.

## Page 5

Mavlink
FAST-LIO
Safety 
Catcher 
Tail-sitter 
Plant
EKF
Rotational Controller
SO(3) Based 
Backstrpping 
Controller
Disturbance 
Observation
Rotational Loop
PX4 SITL
Reference 
Trajectory
GPR
Translational Controller
Quaternion Based 
MPC
Freestream 
Estimation
Flatness
Translational Loop
Onboard PC
IMU
Autopilot
B
x
B
y
Bz
Body
Ix
Iy
Iz
World
Rotational Controller
SO(3) Based 
Backstrpping 
Controller
Disturbance 
Observation
Mavlink
Fig. 2: Coordinate system and cascaded control architecture for simulation and real-world experiments. Reference trajectories
and translational loop are computed on the onboard PC and mapped via the flatness module (blue block); the rotational loop
and vehicle dynamics are simulated in the virtual environment (green block); in real-world experiments, the rotational loop
runs on the autopilot and interacts with the physical vehicle (red block); external positioning and safety systems (purple
block) support the experiments.
axes, with successive performed runs in opposite directions
by reversing the heading, to reduce potential bias.
Subsequently, the estimated freestream velocity and the
corresponding disturbance forces in the body frame are used
as training data D = {(Bv∞,i, Bdi)}N
i=1 for GPR, where Bd
is computed based on the sampling interval and the difference
between the measured velocity and the predicted velocity at
the next time step, as follows,
Bdk = Bv∞,k+1 −Bˆv∞,k+1
∆t
.
(13)
Remark 3. In some previous studies [34], [35], the difference
between the actual control output and the nominal control
command is treated as the external disturbance. However, the
tail-sitter UAV considered in this study exhibits significantly
higher acceleration measurement noise compared to typical
small quadrotor platforms, which may lead to inaccurate
estimation of the true external disturbance. Since the train-
ing data are obtained from real flight experiments, where
estimated disturbances naturally include contributions from
both external disturbances and internal disturbances, such as
deviations in rotational inertia. Consequently, the GPR learns
to predict the total disturbance affecting the system.
C. Differential Flatness
Given the desired attitude and thrust from the GP-MPC
framework, the differential flatness module computes the
corresponding angular velocity and acceleration for the ro-
tational loops. The desired thrust force vector in the inertial
frame is computed as Fd = Rd [0, 0, aT ]T, where Rd
denotes the desired attitude rotation matrix. The matrix Rd is
obtained by converting the quaternion contained in the MPC
control input vector u, as defined in Section III-A.
The desired angular velocity can be obtained by computing
the time derivative of ¯Fd =
Fd
||Fd|| in the inertial frame [36],





˙¯Fd = d
dt
¯Fd

rel + ωd × ¯Fd = ωd × ¯Fd,
ωdxy = ¯Fd × ˙¯Fd,
ωdz = ˙ψd,
(14)
The condition d
¯Fd

rel /dt = 0 always holds because ¯Fd
remains constant along the body-fixed axis zb.
Differentiating Eq. (14) yields the desired angular accel-
eration,
(
˙ωdxy = ˙¯Fd × ˙¯Fd + ¯Fd × ¨¯Fd,
˙ωdz = ¨ψd,
(15)
where ˙¯Fd and ¨¯Fd are obtained by numerical differentiation.
D. Rotational Control Loop
The objective of the rotational loop is to track the de-
sired attitude commands Rd. A singularity-free SO(3)-
based backstepping attitude controller is proposed in this
section, augmented with an NDO to compensate for moment
disturbances. First, the attitude and angular velocity errors
are defined as follows,
eR = 1
2
RT
d R −RTRd
∨, eω = ω −RTRdωd.
(16)
This article has been accepted for publication in IEEE Transactions on Aerospace and Electronic Systems. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TAES.2026.3657729
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 13:00:03 UTC from IEEE Xplore.  Restrictions apply.

## Page 6

Taking the derivative of Eq. (16) yields,



˙eR = 1
2
tr
RTRd

I −RTRd

eω = C
RT
d R

eω,
˙eω = ˙ω + ω×RTRdωd −RTRd ˙ωd,
(17)
where
C
RT
d R
 ≤1 is established for any RT
d R ∈
SO(3) [37].
According to the aforementioned attitude error dynamics,
the SO(3)-based backstepping attitude control scheme is
proposed as follows. Consider the following function,
V1 = 1
2eT
ReR.
(18)
Taking the derivative of Eq. (18) yields,
˙V1 = eT
R ˙eR = eT
RC
RT
d R

eω.
(19)
Define σ = eω −ϖ and C = C
RT
d R

for convenience,
where ϖ = −C−1c1eR, and c1 is the diagonal positive gain
matrix. Eq. (19) can be rewritten as,
˙V1 = eT
RC (σ + ϖ) = eT
RCσ −eT
Rc1eR.
(20)
Subsequently, consider the following quadratic form,
V2 = V1 + 1
2σTJσ.
(21)
Taking the derivative of Eq. (21) yields,
˙V2 = ˙V1 + σTJ ˙σ
= eT
RCσ −eT
Rc1eR + σTJ˙eω −σTJ ˙ϖ
= eT
RCσ −eT
Rc1eR −σTJ ˙ϖ −σTω×Jω+
σT 
M + dτ + J
ˆωRTRdωd −RTRd ˙ωd

.
(22)
Therefore, the controller for the rotational loop is designed
as,
M = −J
ˆωRTRdωd −RTRd ˙ωd

−ˆdτ
+ ω×Jω + J ˙ϖ −CeR −c2Jσ,
(23)
where c2 is a diagonal positive gain matrix. By substituting
Eq. (23) into Eq. (22), the following reformulation can be
obtained,
˙V2 = −eT
Rc1eR −σTc2Jz + σT˜dτ,
(24)
where ˜dτ = dτ −ˆdτ. Here, ˆdτ represents the estimation of
the unmodeled disturbance moment dτ , which is obtained
through a designed NDO.
Similar to the design principle of a state observer, the
NDO estimates the external moments acting on the vehicle
by introducing an auxiliary variable ς. By incorporating the
rotational dynamics described in Eq. (8), the rotational NDO
is designed as follows,



J ˙ω = −ω × Jω + M + dτ,
˙ς = −Lm (ς + LmJω) + Lm (−M + ω × Jω) ,
ˆdτ = ς + LmJω,
(25)
where Lm denotes the positive diagonal observer gain ma-
trix. Defining the estimation error ˜dτ
= dτ −ˆdτ, the
resulting error dynamics from Eq. (25) are given by,
˙˜dτ = ˙dτ −˙ˆdτ
= ˙dτ −(˙ς + LmJ ˙ω)
= ˙dτ −Lm (−ω × Jω + M + dτ) −˙ς
= ˙dτ −Lm˜dτ,
(26)
where the dynamics performance can be adjusted by appro-
priate selection of the gain matrix Lm.
E. Closed-loop stability analysis of the rotational loop
Due to the modular nature of the cascaded architecture,
the stability analysis of the rotational loop can be conducted
independently of the translational loop.
Assumption 1. The time derivative of the disturbance torque
is bounded, i.e.,
 ˙dτ
 ≤¯dτ,
where ¯dτ denotes a positive constant.
Remark 4. Wind-induced disturbances can generally be de-
composed into a low-frequency component and a set of high-
frequency components. For the tail-sitter UAV considered
in this study, the significant mass and rotational inertia
cause its dynamics to inherently behave as a low-pass
filter. This attenuates most high-frequency components and
leaves a residual low-frequency component that is smooth
and bounded. Therefore, the assumption
 ˙dτ
 ≤
¯dτ is
reasonable [6].
Theorem 1. Consider Assumption 1 and the rotational
dynamics given in Eq. (8). If the SO(3)-based backstepping
rotational controller in Eq. (23) is applied in conjunction
with the NDO in Eq. (25), then the resulting rotational
closed-loop system is stable. Moreover, the attitude tracking
errors converge to an arbitrarily small residual set.
Proof. Considering the following Lyapunov function,
V3 = V2 + 1
2
˜dT
τ ˜dτ.
(27)
The derivative of V3 can be obtained by considering Eqs. (24)
and (26)
˙V3
(24)
= −eT
Rc1eR −σTc2Jσ + σT 
dτ −ˆdτ

+ ˜dT
τ ˙˜dτ
(26)
= −eT
Rc1eR −σTc2Jσ + σT˜dτ + ˜dT
τ ˙dτ −˜dT
τ Lm˜dτ.
(28)
By virtue of Young’s inequality,
σT˜dτ ≤
1
2ε1
σTσ+ε1
2
˜dT
τ ˜dτ, ˜dT
τ ˙dτ ≤
1
2ε2
˜dT
τ ˜dτ+ε2
2
 ˙dτ

2
,
(29)
we can obtain that,
˙V3 ≤−eT
Rc1eR −σTc2Jσ −˜dT
τ Lm˜dτ
+ 1
2ε1
σTσ + ε1ε2 + 2
2ε2
˜dT
τ ˜dτ + ε2
2
 ˙dτ

2
,
(30)
This article has been accepted for publication in IEEE Transactions on Aerospace and Electronic Systems. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TAES.2026.3657729
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 13:00:03 UTC from IEEE Xplore.  Restrictions apply.

## Page 7

where ε1 and ε2 are arbitrary positive constants. Given that,





−eT
Rc1eR ≤−λmin(c1) eT
ReR
−σTc2Jσ ≤−λmin(c2J) σTσ
−˜dT
τ Lm˜dτ ≤−λmin(Lm) ˜dT
τ ˜dτ
,
(31)
Eq. (30) can thereby be rewritten as,
˙V3 ≤−λmin(c1) eT
ReR +
 1
2ε1
−λmin(c2J)

σTσ
+
ε1ε2 + 2
2ε2
−λmin(Lm)

˜dT
τ ˜dτ + ε2
2
 ˙dτ

2
≤−λmin(c1) eT
ReR −
λmin(c2J) −
1
2ε1
λmax(J)
σTJσ
−

λmin(Lm) −ε1ε2 + 2
2ε2

˜dT
τ ˜dτ + ε2
2
 ˙dτ

2
≤−κ1eT
ReR −κ2σTJσ −κ3˜dT
τ ˜dτ + ε2
2
¯d2
τ,
(32)
where κ1 = λmin(c1), κ2 =
λmin(c2J)−
1
2ε1
λmax(J)
and κ3 =

λmin(Lm) −ε1ε2+2
2ε2

. The conditions κ1, κ2, κ3 > 0 can
be guaranteed by appropriate selection of ε1, ε2 and the gain
matrix Lm.
By defining δ1 = min {κ1, κ2, κ3} and δ2 =
ε2
2 ¯d2
τ, we
can obtain,
˙V3 ≤−δ1V3 + δ2,
(33)
which implies that,
0 ≤V3 (t) ≤e−δ1t

V3 (0) −δ2
δ1

+ δ2
δ1
.
(34)
And the attitude tracking error is bounded by,
lim
t→∞
∥eR∥≤
q
2δ2
δ1 .
(35)
Therefore, the rotational tracking errors and observer es-
timation errors are globally uniformly ultimately bounded,
converging to a residual set determined by κ1, κ2, κ3, ¯d2
τ,
and Lm. This completes the proof.
Remark 5. Given the physical constraints of real actuators,
the residual set cannot be completely eliminated. Therefore,
the controller parameters must be carefully tuned to achieve
an optimal balance among stability, responsiveness, and
accuracy in practical implementations.
IV. EXPERIMENTAL RESULTS
In this section, simulations and real-world experiments
are conducted to evaluate the effectiveness of the proposed
method.
A. Experiments in Simulation
The simulation is conducted within a software-in-the-loop
(SITL) framework built upon the PX4 firmware and ROS,
utilizing the Gazebo simulation platform for high-fidelity
physics simulation. MPC optimization problems are solved
using the OSQP solver. To improve simulation realism,
computational fluid dynamics (CFD) data and experimen-
tally identified motor dynamics are integrated into the PX4
framework. For both GP training and freestream velocity
estimation modeling, the vehicle performs uniform maneu-
vers in the longitudinal and lateral directions. The resulting
estimation model, which maps freestream velocities v∞to
tilt angles, is illustrated in Fig. 3. The actual freestream
velocities, together with the inferred external disturbances,
are subsequently employed to train the GP model, as depicted
in Fig. 4.
-0.5
0
0.5
-8
-6
-4
-2
0
2
4
6
8
-0.6
-0.4
-0.2
0
0.2
0.4
0.6
-15
-10
-5
0
5
10
15
Fig. 3: The freestream velocity as a function of attitude in
simulation.
-10
-5
0
5
10
-5
0
5
-15
-10
-5
0
5
10
15
-5
0
5
Fig. 4: External disturbances and freestream velocities for
GP training in simulation.
All modules are executed on an HP OMEN8 Plus laptop
equipped with an Intel Core i7-12700H processor and 16 GB
of RAM. The SITL framework is employed primarily to fa-
cilitate the tuning of control parameters and to systematically
evaluate performance across a wide range of wind conditions
that are difficult to replicate in real-world environments.
Wind disturbances in the simulation are generated using
the following function, designed to reproduce realistic wind
profiles with high fidelity,
vw = υ

sin4
4πt
T

+ cos3
πt
T

+ sin2
2πt
T

+ sin
2πt
T
 
,
(36)
This article has been accepted for publication in IEEE Transactions on Aerospace and Electronic Systems. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TAES.2026.3657729
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 13:00:03 UTC from IEEE Xplore.  Restrictions apply.

## Page 8

where υ denotes the mean wind speed vector and T repre-
sents the time period.
To evaluate the effectiveness of the proposed control strat-
egy, a simulation is conducted under a hovering scenario with
aforementioned external wind disturbances. For comparison,
three controllers are implemented under identical conditions:
(i) a conventional cascaded PID controller, (ii) a baseline
MPC without GPR, and (iii) the dual-loop observer (DLO)-
based controller introduced in [12]. The related parameters
for simulation and real-world are selected as the same, which
are summarized in Table I.
TABLE I: Control parameters for simulation and real-world.
Controller
Control Gains
PID
Kp = diag[3, 3, 3.5],
Kpi = diag[0.1, 0.1, 0.1],
Kv = diag[2, 2, 2],
Kvi = diag[0.05, 0.05, 0.05],
KR = diag[3, 3, 1.5],
Kω = diag[0.27, 0.27, 0.4]
DLO
L1 = diag[4, 4, 4],
L2 = diag[0.3, 0.3, 0.3]
MPC
Q = diag[470, 470, 500],
P = diag[470, 470, 500],
R = diag[850, 850, 850, 850],
Ru = diag[0.5, 100, 100, 100, 100],
S = diag[0.5, 80, 80, 80, 80]
Proposed
c1 = diag[3.5, 3.5, 4.5],
c2 = diag[0.35, 0.55, 0.85],
Lm = diag[0.3, 0.3, 0.3]
Fig. 5 presents the hovering performance under wind
disturbance for all controllers. Visually, the proposed method
demonstrates significantly smoother trajectory and reduced
positional errors compared to the other methods. To quan-
titatively assess the performance, RMSE between the actual
and desired positions is calculated as,
RMSE =
v
u
u
t 1
n
n
X
i=1
∥pi −pd,i∥2.
(37)
The computed RMSE values and maximum absolute position
errors for each controller are summarized in Table III. The
results indicate that the proposed method achieves superior
overall performance across all three dimensions. Specifically,
the proposed method yields the lowest RMSE values in the
x, y, and z directions, measuring 0.1270 m, 0.1155 m, and
0.0320 m, respectively. These values represent reductions of
45.2 %, 35.9 %, and 76.4 % compared to the cascade PID
controller, and improvements of 17.0 %, 17.3 %, and 19.4
% relative to the DLO controller, respectively. Regarding
the maximum absolute position errors, the proposed method
also achieves the smallest error of 0.444 m, corresponding
to improvements of 46.1 % and 19.7 % over the PID
and DLO controllers, respectively. Further insights can be
derived from the disturbance estimation results presented in
Fig. 6. The proposed method demonstrates not only more
accurate disturbance identification but also a significantly
reduced estimation delay compared to the DLO-based ap-
proach. To validate this observation, three representative
peak-disturbance events in Fig. 6 are selected to compare
TABLE II: Comparison of disturbance estimation delay
(Unit: s).
Controller
Peak 1
Peak 2
Peak 3
Average
DLO
1.83
1.37
1.62
1.61
Proposed
0.15
0.23
0.12
0.25
Improvement
1.68
1.14
1.50
1.36
the estimation performance of the proposed method with that
of the DLO. The measured delays in these peak regions are
summarized in Table II and highlighted by the green shaded
areas in Fig. 6, clearly illustrating the reduction in estimation
delay achieved by the proposed approach. This enhanced
performance can be primarily attributed to the proposed
attitude-based freestream velocity estimation strategy. Since
the attitude control loop constitutes the inner loop of the
cascaded control architecture and operates at a significantly
higher frequency, it enables faster dynamic responses and,
consequently, more timely estimation of external distur-
bances. This high-rate inner loop constitutes the foundation
of the proposed attitude-based freestream velocity estimator,
providing lower delay and faster response than translational
velocity-based methods such as the DLO. Furthermore, the
integration of an SO(3)-based backstepping controller with
an NDO ensures high-precision attitude tracking, which is
critical for the accuracy of freestream velocity estimation.
This design significantly improves the fidelity of disturbance
compensation and enhances the overall robustness and track-
ing performance under complex aerodynamic conditions.
0
10
20
30
40
50
60
70
80
90
100
-0.5
0
0.5
1
X (m)
Position SP
MPC
DLO
Cascade PID
GP-MPC
0
10
20
30
40
50
60
70
80
90
100
-0.5
0
0.5
Y (m)
0
10
20
30
40
50
60
70
80
90
100
Time (s)
3.2
3.4
3.6
3.8
Z (m)
Fig. 5: Hovering performance in the presence of wind
disturbances.
TABLE III: RMSE and maximum error (UNIT: m).
Controller
Max
RMSE(x)
RMSE(y)
RMSE(z)
MPC
0.652
0.1937
0.1563
0.0334
DLO
0.553
0.1530
0.1396
0.0397
Cascade PID
0.824
0.2319
0.1801
0.1355
GP-MPC
0.444
0.1270
0.1155
0.0320
This article has been accepted for publication in IEEE Transactions on Aerospace and Electronic Systems. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TAES.2026.3657729
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 13:00:03 UTC from IEEE Xplore.  Restrictions apply.

## Page 9

0
10
20
30
40
50
60
70
80
90
100
-20
0
20
40
60
Real Drag
DLO
Proposed
 3
0
10
20
30
40
50
60
70
80
90
100
Time (s)
0
10
20
30
40
Fig. 6: True and estimated wind disturbance forces.
B. Experiments in the Real World
In real-world model training, the vehicle executed identical
uniform maneuvers in both longitudinal and lateral directions
as in the simulation. To ensure accurate state estimation,
real-time kinematic (RTK) positioning is employed for high-
precision localization. The recorded flight data are processed
using the same pipeline as in the simulation to extract body-
frame freestream velocities and corresponding external dis-
turbances, which are subsequently used to train both the GP
model and the freestream velocity estimator. The resulting
models are presented in Fig. 7 and Fig. 8, respectively.
-0.4
-0.2
0
0.2
0.4
-10
-8
-6
-4
-2
0
2
4
6
8
-0.2
-0.1
0
0.1
0.2
0.3
-10
-8
-6
-4
-2
0
2
4
6
8
10
Fig. 7: The freestream velocity as a function of attitude in
real-world experiments.
Given the relatively large size and mass of the tail-sitter
UAV tested in this study, small-scale fans are insufficient to
generate disturbances significant enough to affect its flight
dynamics. To address this limitation, a UAV propulsion test
stand equipped with a 49-inch high-thrust propeller is em-
ployed to generate controllable and repeatable external dis-
turbances, as illustrated in Fig. 9. The high-speed propeller
wake introduced significant external wind up to 6.1 m/s,
enabling a meaningful evaluation of the disturbance rejection
capabilities. For safety considerations, the UAV is suspended
under a safety catcher system using a high-strength harness to
-6
-4
-2
0
2
4
-5
0
5
-6
-4
-2
0
2
4
6
-5
0
5
Fig. 8: External disturbances and freestream velocities for
GP training in real-world experiments.
prevent accidental falls. Due to the limited yaw authority of
the vehicle, the heading is fixed throughout the experiments
to ensure safe operation. Under this fixed-heading condition,
disturbance responses are independently examined along the
x and y axes. This experimental configuration provides a
safe testing environment while preserving sufficient transla-
tional degrees of freedom to effectively evaluate disturbance
rejection performance.
All modules are executed on an Intel NUC onboard
computer equipped with an i7 processor operating at 4.2
GHz and 16 GB of RAM, ensuring adequate computational
resources. A CUAV V5+ autopilot manages low-level control
and sensor data fusion, while FAST-LIO [38] is utilized for
localization.
Fig. 9: The real-world experimental setup.
In the experiment, the tail-sitter UAV is commanded to
take off from the origin, hover at the position (0, 0, 1 m)
This article has been accepted for publication in IEEE Transactions on Aerospace and Electronic Systems. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TAES.2026.3657729
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 13:00:03 UTC from IEEE Xplore.  Restrictions apply.

## Page 10

0
0.2
0.4
0.6
0.4
Z (m)
0.8
0.5
1
0.2
Y (m)
0
0
X (m)
-0.2
-0.5
-0.4
-1
Reference
PID
DLO
MPC
PID in wind
DLO in wind
MPC in wind
Proposed in wind
(a) 3D view of tracking in x direction
0
5
10
15
20
25
30
35
40
-1
-0.5
0
0.5
X (m)
0
5
10
15
20
25
30
35
40
-0.5
0
0.5
Y (m)
0
5
10
15
20
25
30
35
40
Time (s)
0
0.5
1
Z (m)
(b) Tracking performance in x direction
0
5
10
15
20
25
30
35
40
-0.2
0
0.2
0.4
X (m)
0
5
10
15
20
25
30
35
40
-0.2
0
0.2
Y (m)
0
5
10
15
20
25
30
35
40
Time (s)
-0.2
0
0.2
Z (m)
(c) Tracking error in x direction
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
10
15
0
5
10
15
20
25
30
35
40
Time (s)
-1
0
1
2
(d) External force estimation in x direction
Fig. 10: The 3D trajectory, tracking performance, error, and
disturbance estimation in the x direction.
0
0.5
1
0.2
0.4
Z (m)
0.6
0.5
X (m)
0.8
Y (m)
0
1
0
-0.5
-0.5
Reference
PID
DLO
MPC
PID in wind
DLO in wind
MPC in wind
Proposed in wind
(a) 3D view of tracking in y direction
0
5
10
15
20
25
30
35
40
-0.5
0
0.5
X (m)
0
5
10
15
20
25
30
35
40
-0.5
0
0.5
1
Y (m)
0
5
10
15
20
25
30
35
40
Time (s)
0
0.5
1
Z (m)
(b) Tracking performance in y direction
0
5
10
15
20
25
30
35
40
-0.2
0
0.2
X (m)
0
5
10
15
20
25
30
35
40
-0.5
0
0.5
Y (m)
0
5
10
15
20
25
30
35
40
Time (s)
-0.1
0
0.1
Z (m)
(c) Tracking error in y direction
0
5
10
15
20
25
30
35
40
-3
-2
-1
0
1
2
0
5
10
15
20
25
30
35
40
Time (s)
-15
-10
-5
0
(d) External force estimation in y direction
Fig. 11: The 3D trajectory, tracking performance, error, and
disturbance estimation in the y direction.
This article has been accepted for publication in IEEE Transactions on Aerospace and Electronic Systems. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TAES.2026.3657729
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 13:00:03 UTC from IEEE Xplore.  Restrictions apply.

## Page 11

for 5 s, and then begin tracking the desired circular trajec-
tory. Two experiments, one with and one without external
disturbances, are conducted using different controllers for
comparative analysis. The experimental results are presented
in Fig. 10, while the corresponding RMSE values and
maximum absolute tracking errors for each controller are
summarized in Table IV. The experiment without external
disturbances is designed to evaluate the inherent tracking per-
formance of the baseline controllers. By employing baseline
controllers in the absence of external forces, the potential in-
fluence of the safety catcher on subsequent disturbance rejec-
tion experiments can be effectively isolated. As demonstrated
by both Fig. 10 and the quantitative results in Table IV,
the tracking performance of all baseline controllers remains
largely consistent under wind-free conditions. Although the
safety catcher may exert a minor influence on vehicle dynam-
ics, its impact is effectively controlled through the variable
isolation strategy, ensuring that it does not confound the
interpretation of disturbance-related effects.
By comparing the experimental results with and without
external wind disturbances, it is evident that the presence
of wind significantly degrades the trajectory tracking perfor-
mance of the vehicle. According to the estimation results
illustrated in Fig. 10d, the estimated maximum external
disturbance force exceeds 10 N, indicating a substantial
challenge to the rejection of disturbances in the control task.
All controllers exhibit an increase in RMSE exceeding 9 cm,
and the maximum tracking errors at least triple compared
to the disturbance-free condition. As illustrated by the 3D
trajectories in Fig. 10a, deviation during the take-off phase
becomes particularly pronounced under wind disturbances.
Despite the presence of significant external disturbances,
the proposed controller demonstrates superior tracking per-
formance. Specifically, in the x-axis direction, the proposed
method achieves an 18.17 % improvement in tracking ac-
curacy and a 10.75 % reduction in maximum tracking error
compared to the DLO controller, highlighting the advantage
of the proposed method. While the inner-loop attitude con-
troller ensures a rapid response to attitude commands, the
GPR component accurately estimates external disturbances
in real time.
In contrast, the disturbance estimation provided by the
DLO consistently exhibits a noticeable delay, which par-
tially explains its inferior tracking performance. The close
coordination between rapid attitude regulation and precise
disturbance compensation contributes significantly to the
robustness and precision of the proposed method under
challenging flight conditions.
In the y direction, the influence of external wind distur-
bances remained significant, and a similar degradation trend
is observed under external wind disturbances. As detailed
in Table V, all compared controllers exhibited a substantial
increase in RMSE, with values exceeding 10 cm. Further-
more, the maximum tracking errors demonstrated a consid-
erable escalation, exceeding three times those observed under
disturbance-free conditions. Thus, the external wind exerts a
pronounced effect on lateral trajectory tracking, particularly
TABLE IV: RMSE and maximum error in x direction (unit:
m).
Controller
Max
RMSE-x
RMSE-y
RMSE-z
PID
0.0831
0.0403
0.0576
0.0348
MPC
0.0935
0.0344
0.0532
0.0441
DLO
0.0706
0.0259
0.0337
0.0377
PID (wind)
0.5034
0.1698
0.0752
0.0336
MPC (wind)
0.4445
0.1390
0.0706
0.0396
DLO (wind)
0.2419
0.1112
0.0731
0.0440
Proposed (wind)
0.2159
0.0910
0.0550
0.0365
TABLE V: RMSE and maximum error in y direction (unit:
m).
Controller
Max
RMSE-x
RMSE-y
RMSE-z
PID
0.0945
0.0324
0.0392
0.0177
MPC
0.0712
0.0293
0.0298
0.0179
DLO
0.0829
0.0230
0.0264
0.0179
PID (wind)
0.5331
0.0699
0.1523
0.0431
MPC (wind)
0.4091
0.0651
0.1374
0.0262
DLO (wind)
0.3206
0.0616
0.1183
0.0258
Proposed (wind)
0.2678
0.0513
0.0951
0.0247
during take-off phases, as illustrated in Fig. 11a.
Despite the challenging conditions, the proposed controller
exhibited superior tracking performance compared to other
methods. Relative to the DLO controller, it reduced the
RMSE by 19.61 % and decreased the maximum tracking
error by 34.54 % in the y direction. The superior performance
highlights the efficacy of the proposed approach in rejecting
lateral disturbance. In contrast to simpler feedback designs,
the proposed method, combined with real-time disturbance
estimation, enabled the controller to actively adapt to varying
disturbances. The enhancement in lateral regulation is partic-
ularly crucial for maintaining overall tracking performance.
These results further demonstrate the robustness of the
proposed approach across multiple directional axes.
V. CONCLUSIONS
This study addresses the critical challenge of rejecting
external wind disturbances for UAVs, particularly for a
medium-scale tail-sitter during VTOL operations. A cas-
caded control architecture is proposed through the inte-
gration of learning-augmented disturbance estimation into
the classical CHADC framework. A sensorless freestream
velocity estimation method based on attitude dynamics is
developed and embedded within a GPR model to enable real-
time and accurate disturbance estimation. Furthermore, an
SO(3)-based backstepping attitude controller is designed and
augmented with an NDO to actively compensate for external
moment disturbances, ensuring rapid and precise attitude
tracking. The effectiveness of the proposed control scheme
is validated through both high-fidelity simulations and real-
world experiments, demonstrating superior trajectory track-
ing performance and robust disturbance rejection capability
This article has been accepted for publication in IEEE Transactions on Aerospace and Electronic Systems. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TAES.2026.3657729
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 13:00:03 UTC from IEEE Xplore.  Restrictions apply.

## Page 12

under complex aerodynamic conditions. Future work will fo-
cus on incorporating online adaptive GPR to further improve
learning efficiency and adaptability in dynamically changing
environments.
REFERENCES
[1] A. Divazi, R. Askari, and E. Roohi, “Experimental and numerical
investigation on the spraying performance of an agricultural unmanned
aerial vehicle,” Aerospace Science and Technology, vol. 160, pp.
110 083–110 102, 2025.
[2] S. Li, H. Zhang, J. Yi, and H. Liu, “A bi-level planning approach of
logistics unmanned aerial vehicle route network,” Aerospace Science
and Technology, vol. 141, pp. 108 572–108 584, 2023.
[3] H. Bai, S. Mei, and J. Dong, “Hierarchical temporal sequence conver-
gence in prescribed-time control for quadrotor UAVs under unknown
dynamic disturbances,” Aerospace Science and Technology, vol. 148,
pp. 109 094–109 106, 2024.
[4] X. Peng, G. Su, and R. Sengupta, “An autonomous unmanned aerial
vehicle exploration platform with a hierarchical control method for
post-disaster infrastructures,” IET Cyber-Systems and Robotics, vol. 6,
no. 1, p. e12107, 2024.
[5] W. Tian, L. Liu, X. Zhang, J. Shao, and J. Ge, “Adaptive hierarchical
energy management strategy for fuel cell/battery hybrid electric uavs,”
Aerospace Science and Technology, vol. 146, pp. 108 938–108 949,
2024.
[6] E. Tal and S. Karaman, “Global incremental flight control for agile
maneuvering of a tailsitter flying wing,” Journal of Guidance, Control,
and Dynamics, vol. 45, no. 12, pp. 2332–2349, 2022.
[7] M. Khodaverdian, S. Hajshirmohamadi, A. Hakobyan, and S. Ijaz,
“Predictor-based constrained fixed-time sliding mode control of multi-
uav formation flight,” Aerospace Science and Technology, vol. 148, pp.
109 113–109 134, 2024.
[8] Y. Wang and J. Hu, “Robust control for a quadrotor aircraft with small
overshoot and high-precision position tracking performance,” Journal
of the Franklin Institute, vol. 357, no. 18, pp. 13 386–13 409, 2020.
[9] X. Lyu, J. Zhou, H. Gu, Z. Li, S. Shen, and F. Zhang, “Disturbance
observer based hovering control of quadrotor tail-sitter vtol UAVs
using H∞synthesis,” IEEE Robotics and Automation Letters, vol. 3,
no. 4, pp. 2910–2917, 2018.
[10] J. Jia, K. Guo, X. Yu, L. Guo, and L. Xie, “Agile flight control under
multiple disturbances for quadrotor: Algorithms and evaluation,” IEEE
Transactions on Aerospace and Electronic Systems, vol. 58, no. 4, pp.
3049–3062, 2022.
[11] J. Jia, K. Guo, X. Yu, W. Zhao, and L. Guo, “Accurate high-
maneuvering trajectory tracking for quadrotors: A drag utilization
method,” IEEE Robotics and Automation Letters, vol. 7, no. 3, pp.
6966–6973, 2022.
[12] X. Yu, X. Zhou, K. Guo, J. Jia, L. Guo, and Y. Zhang, “Safety
flight control for a quadrotor UAV using differential flatness and dual-
loop observers,” IEEE Transactions on Industrial Electronics, vol. 69,
no. 12, pp. 13 326–13 336, 2021.
[13] J. Zhang, D. Gu, Z. Ren, and B. Wen, “Robust trajectory tracking
controller for quadrotor helicopter based on a novel composite control
scheme,” Aerospace Science and Technology, vol. 85, pp. 199–215,
2019.
[14] H. Hua, Y. Fang, X. Zhang, and B. Lu, “A novel robust observer-
based nonlinear trajectory tracking control strategy for quadrotors,”
IEEE Transactions on Control Systems Technology, vol. 29, no. 5, pp.
1952–1963, 2020.
[15] K. Guo, W. Zhang, Y. Zhu, J. Jia, X. Yu, and Y. Zhang, “Safety control
for quadrotor UAV against ground effect and blade damage,” IEEE
Transactions on Industrial Electronics, vol. 69, no. 12, pp. 13 373–
13 383, 2022.
[16] L. Guo and W.-H. Chen, “Disturbance attenuation and rejection for
systems with nonlinearity via dobc approach,” International Journal of
Robust and Nonlinear Control: IFAC-Affiliated Journal, vol. 15, no. 3,
pp. 109–125, 2005.
[17] L. Guo and S. Cao, “Anti-disturbance control theory for systems with
multiple disturbances: A survey,” ISA Transactions, vol. 53, no. 4, pp.
846–849, 2014.
[18] Y. Chen, J. Liang, Y. Wu, Z. Miao, H. Zhang, and Y. Wang,
“Adaptive sliding-mode disturbance observer-based finite-time control
for unmanned aerial manipulator with prescribed performance,” IEEE
Transactions on Cybernetics, vol. 53, no. 5, pp. 3263–3276, 2022.
[19] J. Jia, W. Zhang, K. Guo, J. Wang, X. Yu, Y. Shi, and L. Guo, “Evolver:
Online learning and prediction of disturbances for robot control,” IEEE
Transactions on Robotics, vol. 40, pp. 382–402, 2023.
[20] Y. Yang, Z. Bao, J. Qiao, Y. Zhu, and L. Guo, “Refined metamodel
disturbance observer-based control for coarse pointing assembly under
constraints,” Guidance, Navigation and Control, vol. 4, no. 04, p.
2450017, 2024.
[21] M. O’Connell, G. Shi, X. Shi, K. Azizzadenesheli, A. Anandkumar,
Y. Yue, and S.-J. Chung, “Neural-fly enables rapid learning for agile
flight in strong winds,” Science Robotics, vol. 7, no. 66, p. eabm6597,
2022.
[22] Y. Wang and D. Boyle, “Constrained reinforcement learning using
distributional representation for trustworthy quadrotor UAV tracking
control,” IEEE Transactions on Automation Science and Engineering,
vol. 22, pp. 5877–5894, 2024.
[23] Y. Wei, S. Lyu, W. Li, X. Yu, Z. Wang, and L. Guo, “Contact force
estimation of robot manipulators with imperfect dynamic model: On
gaussian process adaptive disturbance kalman filter,” IEEE Transac-
tions on Automation Science and Engineering, vol. 21, no. 3, pp. 3524–
3537, 2023.
[24] C. Gall and N. Bezzo, “Gaussian process-based interpretable runtime
adaptation for safe autonomous systems operations in unstructured
environments,” in 2021 IEEE/RSJ International Conference on Intel-
ligent Robots and Systems (IROS).
IEEE, 2021, pp. 123–129.
[25] H. Li, X. Li, Z. Zhang, C. Hu, F. Dunkin, and S. S. Ge, “Esuav-
ni: Endogenous security framework for uav perception system based
on neural immunity,” IEEE Transactions on Industrial Informatics,
vol. 20, no. 1, pp. 732–743, 2023.
[26] G. Kulathunga, H. Hamed, and A. Klimchik, “Residual dynamics
learning for trajectory tracking for multi-rotor aerial vehicles,” Sci-
entific Reports, vol. 14, no. 1, pp. 1858–1873, 2024.
[27] Z. Cheng and H. Pei, “A corridor-based flight mode transition strategy
for agile ducted-fan tail-sitter UAV: Altitude-hold transition,” Chinese
Journal of Aeronautics, vol. 36, no. 9, pp. 330–345, 2023.
[28] M. Mehndiratta and E. Kayacan, “Gaussian process-based learning
control of aerial robots for precise visualization of geological out-
crops,” in 2020 European control conference (ECC).
IEEE, 2020,
pp. 10–16.
[29] G. Cao, E. M.-K. Lai, and F. Alam, “Gaussian process model pre-
dictive control of an unmanned quadrotor,” Journal of Intelligent &
Robotic Systems, vol. 88, no. 1, pp. 147–162, 2017.
[30] P. Antal, T. P´eni, and R. T´oth, “Backflipping with miniature quad-
copters by Gaussian-Process-Based control and planning,” IEEE
Transactions on Control Systems Technology, vol. 32, no. 1, pp. 3–14,
2023.
[31] G. Torrente, E. Kaufmann, P. F¨ohn, and D. Scaramuzza, “Data-driven
mpc for quadrotors,” IEEE Robotics and Automation Letters, vol. 6,
no. 2, pp. 3769–3776, 2021.
[32] Y. Demitrit, S. Verling, T. Stastny, A. Melzer, and R. Siegwart,
“Model-based wind estimation for a hovering vtol tailsitter UAV,”
in 2017 IEEE International Conference on Robotics and Automation
(ICRA).
IEEE, 2017, pp. 3945–3952.
[33] T. Wetz, N. Wildmann, and F. Beyrich, “Distributed wind mea-
surements with multiple quadrotor unmanned aerial vehicles in the
atmospheric boundary layer,” Atmospheric Measurement Techniques,
vol. 14, no. 5, pp. 3795–3814, 2021.
[34] A. Buelta, A. Olivares, E. Staffetti, W. Aftab, and L. Mihaylova,
“A Gaussian process iterative learning control for aircraft trajectory
tracking,” IEEE Transactions on Aerospace and Electronic Systems,
vol. 57, no. 6, pp. 3962–3973, 2021.
[35] M. Wei, L. Zheng, Y. Wu, H. Liu, and H. Cheng, “Safe learning-
based control for multiple UAVs under uncertain disturbances,” IEEE
Transactions on Automation Science and Engineering, vol. 21, no. 4,
pp. 7349–7362, 2023.
[36] M. Cutler and J. P. How, “Analysis and control of a variable-pitch
quadrotor for agile flight,” Journal of Dynamic Systems, Measurement,
and Control, vol. 137, no. 10, pp. 101 002–101 017, 2015.
[37] T. Lee, M. Leok, and N. H. McClamroch, “Control of complex
maneuvers for a quadrotor UAV using geometric methods on SE (3),”
arXiv preprint arXiv:1003.2005, 2010.
[38] W. Xu, Y. Cai, D. He, J. Lin, and F. Zhang, “Fast-LIO2: Fast direct
lidar-inertial odometry,” IEEE Transactions on Robotics, vol. 38, no. 4,
pp. 2053–2073, 2022.
This article has been accepted for publication in IEEE Transactions on Aerospace and Electronic Systems. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TAES.2026.3657729
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 13:00:03 UTC from IEEE Xplore.  Restrictions apply.
