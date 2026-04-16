# OpenVINS  A Research Platform for Visual-Inertial Estimation.pdf

## Page 1

OpenVINS: A Research Platform for Visual-Inertial Estimation
Patrick Geneva, Kevin Eckenhoff, Woosik Lee, Yulin Yang, and Guoquan Huang
Abstract— In this paper, we present an open platform, termed
OpenVINS, for visual-inertial estimation research for both the
academic community and practitioners from industry. The open
sourced codebase provides a foundation for researchers and
engineers to quickly start developing new capabilities for their
visual-inertial systems. This codebase has out of the box support
for commonly desired visual-inertial estimation features, which
include: (i) on-manifold sliding window Kalman ﬁlter, (ii)
online camera intrinsic and extrinsic calibration, (iii) camera
to inertial sensor time offset calibration, (iv) SLAM landmarks
with different representations and consistent First-Estimates
Jacobian (FEJ) treatments, (v) modular type system for state
management, (vi) extendable visual-inertial system simulator,
and (vii) extensive toolbox for algorithm evaluation. Moreover,
we have also focused on detailed documentation and theoretical
derivations to support rapid development and research, which
are greatly lacked in the current open sourced algorithms.
Finally, we perform comprehensive validation of the proposed
OpenVINS against state-of-the-art open sourced algorithms,
showing its competing estimation performance.
• Open source:
https://github.com/rpng/open_vins
• Documentation:
https://docs.openvins.com
I. INTRODUCTION
Autonomous robots and consumer-grade mobile devices
such as drones and smartphones are becoming ubiquitous,
in part due to a large increase in computing ability and
a simultaneous reduction in power consumption and cost.
To endow these robots and mobile devices with the ability
to perceive and understand their contextual locations within
local environments, which is desired in many different ap-
plications from mobile AR/VR to autonomous navigation,
visual-inertial navigation systems (VINS) are often used to
provide accurate motion estimates by fusing the data from
on-board camera and inertial sensors [1].
Developing a working VINS algorithm from scratch has
proven to be challenging, and in the robotics research
community, this has shown to be a signiﬁcant hurdle for
researchers due to the lack of VINS codebases that have
comprehensive documentation and detailed derivations for
which even users with little background can learn and extend
a current state-of-the-art work to address their problems at
hand. While there are several open sourced visual-inertial
codebases [2]–[8], they are not developed for extensibility
and lack proper documentation and evaluation tools, which,
This work was partially supported by the University of Delaware (UD)
College of Engineering, the NSF (IIS-1924897), the ARL (W911NF-19-
2-0226, JWS 10-051-003) the DTRA (HDTRA1-16-1-0039), and Google
ARCore. P. Geneva was also partially supported by the Delaware Space
Grant College and Fellowship Program (NASA Grant NNX15AI19H).
The
authors
are
with
the
Robot
Perception
and
Navigation
Group (RPNG), University of Delaware, Newark, DE 19716, USA.
{pgeneva,keck,woosik,yuyang,ghuang}@udel.edu
to our experience, are crucial for rapid development and
deep understanding, thus accelerating the VINS research and
development in the ﬁeld. Moreover, these systems have many
hard-coded assumptions or features that require an intricate
understanding of the codebases in order to adapt them to
the sensor systems at hand. This, along with inadequate
documentation and support, limits their wide adoption in
different applications.
To ﬁll the aforementioned void in the community and
to promote the VINS research in robotics and beyond, in
this paper, we present an extendable, open-sourced codebase
that is particularly designed for researchers and practitioners
with either limited or extensive background knowledge of
state estimation. We provide the necessary documentation,
tools, and theory for those who are even new to visual-
inertial estimation, and term this collection of utilities as
OpenVINS (OV). This codebase has been the foundation
of many of the recent visual-inertial estimation projects in
our group at the University of Delaware, which include
multi-camera VIO [9], multi-IMU VIO [10], visual-inertial
moving object tracking [11], Schmidt-based visual-inertial
SLAM [12], [13], point-plane and point-line visual-inertial
navigation [14], [15], among others [16]–[18]. We summa-
rize the key functionality of the different components in
OpenVINS as follows:
• ov core – Contains 2D image sparse visual feature
tracking; linear and Gauss-Newton feature triangulation
methods; visual-inertial simulator for arbitrary number
of cameras and frequencies; and fundamental manifold
math operations and utilities.
• ov eval – Contains trajectory alignment; plotting utili-
ties for trajectory accuracy and consistency evaluation;
Monte-Carlo evaluation of different accuracy metrics;
and utility for recording ROS topics to ﬁle.
• ov msckf – Contains the extendable modular Extended
Kalman Filter (EKF)-based sliding window visual-
inertial estimator with on-manifold type system for
ﬂexible state representation. Features include: First-
Estimates Jacobains (FEJ) [19]–[21], IMU-camera time
offset calibration [22], camera intrinsics and extrinsic
online calibration [23], standard MSCKF [24], and 3D
SLAM landmarks of different representations.
In what follows we describe our generalized modular
on-manifold EKF-based estimator which, in its simplest
form, estimates the current state of a camera-IMU pair. We
then introduce the implemented features that provide the
foundation for researchers to quickly build and extend on.
Note that what we present here is only a brief introduction
to the feature set and readers are referred to our thorough
documentation website. We also provide an evaluation of

## Page 2

the proposed EKF-based solution in simulations and then
on real-world datasets, clearly demonstrating its competing
performance against other open-sourced algorithms.
II. ON-MANIFOLD MODULAR EKF
The state vector of our visual-inertial system consists of
the current inertial navigation state, a set of c historical IMU
pose clones, a set of m environmental landmarks, and a set
of w cameras’ extrinsic and intrinsic parameters.
xk =
h
x⊤
I
x⊤
C
x⊤
M
x⊤
W
CtI
i⊤
(1)
xI =
h
Ik
G ¯q⊤
Gp⊤
Ik
Gv⊤
Ik
b⊤
ωk
b⊤
ak
i⊤
(2)
xC =
h
Ik−1
G
¯q⊤
Gp⊤
Ik−1
· · ·
Ik−c
G
¯q⊤
Gp⊤
Ik−c
i⊤
(3)
xM =
h
Gp⊤
f1
· · ·
Gp⊤
fm
i⊤
(4)
xW =
h
I
C1 ¯q⊤
C1p⊤
I
ζ⊤
0 · · ·
I
Cw ¯q⊤
Cwp⊤
I
ζ⊤
w
i⊤
(5)
where Ik
G ¯q is the unit quaternion parameterizing the rotation
R(Ik
G ¯q) = Ik
G R from the global frame of reference {G} to
the IMU local frame {Ik} at time k [25], bω and ba are
the gyroscope and accelerometer biases, and GvIk and GpIk
are the velocity and position of the IMU expressed in the
global frame, respectively. The inertial state xI lies on the
manifold deﬁned by the product of the unit quaternions H
with the vector space R12 (i.e. M = H × R12) and has 15
total degrees of freedom (DOF).
For vector variables, the “boxplus” and “boxminus” opera-
tions, which map elements to and from a given manifold [26],
equate to simple addition and subtraction of their vectors. For
quaternions, we deﬁne the quaternion boxplus operation as:
¯q1 ⊞δθ
∆=
"
δθ
2
1
#
⊗¯q1 ≃¯q2
(6)
Note that although we have deﬁned the orientations using
the left quaternion error, it is not limited to this and any on-
manifold representation in practice can be used (e.g., [27]).
The map of environmental landmarks xM contains global
3D positions only for simplicity, while in practice we offer
support for different representations (e.g. inverse MSCKF
[24], full inverse depth [28], and anchored 3D position [29]).
The calibration vector xW contains the camera intrinsics
ζ, consisting of focal length, camera center, and distortion
parameters, and the camera-IMU extrinsics, i.e., the spatial
transformation (relative pose) from the IMU to each camera.
Since we consider synchronized camera clocks but not for
IMU clock, we include a single time offset CtI between the
IMU and the camera clock in the calibration vector.
A. Propagation
The inertial state xI is propagated forward using incoming
IMU measurements of linear accelerations Iam and angular
velocities Iωm based on the following generic nonlinear
IMU kinematics propagating the state from timestep k −1
to k [30]:
xk = f(xk−1, Iam, Iωm, n)
(7)
where n contains the zero-mean white Gaussian noise of the
IMU measurements along with random walk bias noise. This
state estimate is evaluated at the current estimate:
ˆxk|k−1 = f(ˆxk−1|k−1, Iam, Iωm, 0)
(8)
where ˆ· denotes the estimated value and the subscript k|k−1
denotes the predicted estimate at time k given the mea-
surements up to time k −1. The state covariance matrix
is propagated typically by linearizing the nonlinear model at
the current estimate:
Pk|k−1 = Φk−1Pk−1|k−1Φ⊤
k−1 + Qk−1
(9)
where Φk−1 and Qk−1 are respectively the system Jacobian
and discrete noise covariance matrices [24]. The clones xC,
environmental features xM, and calibration xW states do not
evolve with time and thus the corresponding state Jacobian
entries are identity with zero propagation noise, thus allowing
for exploitation of the sparsity for computational savings.
B. On-Manifold Update
Consider the following nonlinear measurement function:
zm,k = h(xk) + nm,k
(10)
where we have the measurement noise nm,k ∼N(0, Rm,k).
For the standard EKF update, one linearizes the above
equation at the current state estimate. In our case, as in
the indirect EKF [25], we linearize (10) with respect to the
current zero-mean error state (i.e. ˜x = x ⊟ˆx ∼N(0, P)):
zm,k = h(ˆxk|k−1 ⊞˜xk|k−1) + nm,k
(11)
= h(ˆxk|k−1) + Hk˜xk|k−1 + nm,k
(12)
⇒˜zm,k = Hk˜xk|k−1 + nm,k
(13)
where Hk is the measurement Jacobian computed as follows:
Hk = ∂h(ˆxk|k−1 ⊞˜xk|k−1)
∂˜xk|k−1

˜xk|k−1=0
(14)
Using this linearized measurement model, we can now
perform the following standard EKF update to ensure the
updated states remain on-manifold:
ˆxk|k = ˆxk|k−1 ⊞Kk(zm,k −h(ˆxk|k−1))
(15)
Pk|k = Pk|k−1 −KkHkPk|k−1
(16)
Kk = Pk|k−1H⊤
k (HkPk|k−1H⊤
k + Rm,k)−1
(17)
III. OPENVINS RESEARCH PLATFORM
A. Type-based Index System
At the core of the OpenVINS library is the type-based
index system. Inspired by graph-based optimization frame-
works such as GTSAM [31], we abstract away from the user
the need to directly manipulate the covariance and instead
provide the tools to automatically manage the state and
its covariance. This offers many beneﬁts such as reduced
implementation time and being less prone to development
errors due to explicit state and covariance access.
Each state variable “type” has internally the location of
where it is in the error state which is automatically updated
during initialization, cloning, or marginalization operations
which affect variable ordering. A type is deﬁned by its

## Page 3

covariance location, its current estimate and its error state
size. The current value does not have to be a vector, but could
be a matrix in the case of an SO(3) rotation representation.
The error state for all types is a vector and thus a type will
need to deﬁne the boxplus mapping between its error state
and its manifold representation (i.e. the update function).
c l a s s
Type {
protected :
/ /
Current
b e s t
e s t i m a t e
Eigen : : MatrixXd
v a l u e ;
/ /
Index
of
error
s t a t e
in
covariance
i n t
i d = −1;
/ /
Dimension
of
error
s t a t e
i n t
s i z e = −1;
/ /
Vector
c o r r e c t i o n ,
how to
update
void
update ( const
Eigen : : VectorXd dx ) ;
};
One of the main advantages of this type system is that it
reduces the complexity of adding new features by allowing
the user to construct sparse Jacobians. Instead of constructing
a Jacobian for all state elements, the “sparse” Jacobian needs
to only include the state elements that the measurement is a
function of. This both saves computation in the cases where
a measurement is a function of only a few state elements
and allows for measurement functions to be state agnostic
as long as their involved state variables are present.
B. State Variable Initialization
Based on a set of linearized measurement equations (13),
we aim to optimally compute the initial estimate of a new
state variable and its covariance and correlations with the
existing state variables. As a motivating example, we here
describe how to initialize a new SLAM landmark
Gpf,
whose key logic can be used for any new state variable and
is generalized to any type within the codebase. As in [32] we
ﬁrst perform QR decomposition (e.g., using computationally
efﬁcient in-place Givens rotations) to separate the linear
system (13) into two subsystems: (i) one that depends on
the new state (i.e., Gpf), and (ii) the other that does not.
˜zm,k =
h
Hx
Hf
i "
˜xk
G˜pf
#
+ nm,k
(18)
⇒
"
˜zm1,k
˜zm2,k
#
=
"
Hx1
Hf1
Hx2
0
# "
˜xk
G˜pf
#
+
"
nf1
nf2
#
(19)
where nfi ∼N(0, Rfi), i ∈{1, 2}. Note that in the above
expression ˜zm1,k and ˜zm2,k are orthonormally transformed
measurement residuals, not the direct partitions of ˜zm,k. With
the top transformed linearized measurement residual ˜zm1,k
in (19), we now perform efﬁcient EKF update to initialize
the state estimate of Gˆpf and its covariance and correlations
to xk [see (15)], which will then be augmented to the current
state and covariance matrix.
Gˆpf = Gˆpf ⊞H−1
f1 ˜zm1,k
(20)
Pxf = −PkH⊤
x1H−⊤
f1
(21)
Pff = H−1
f1 (Hx1PkH⊤
x1 + Rf1)H−⊤
f1
(22)
It should be noted that a full-rank Hf1 is needed to perform
above initialization, which normally is the case if enough
measurements are collected (i.e., delayed initialization). Note
also that to utilize all available measurement information,
we also perform EKF update using the bottom measurement
residual ˜zm2,k in (19), which essentially is equivalent to the
Multi-State Constraint Kalman Filter (MSCKF) [24] update
with nullspace projection [33].
C. Landmark Update
We generalize the landmark measurement model as a
series of nested functions to encompass different feature
parameterizations such as 3D position and inverse depth and
so on. Assuming a visual feature that has been tracked over
the sliding window of stochastic clones [34], we can write
the visual-bearing measurements (i.e., pixel coordinates) as
the following series of nested functions:
zm,k = h(xk) + nm,k
(23)
= hd(zn,k, ζ) + nm,k
(24)
= hd(hp(Ckpf), ζ) + nm,k
(25)
= hd(hp(ht(Gpf, Ck
G R, GpCk)), ζ) + nm,k
(26)
where zm,k is the raw uv pixel coordinate; nm,k the raw pixel
noise and typically assumed to be zero-mean white Gaussian;
zn,k is the normalized undistorted uv measurement; Ckpf is
the landmark position in the current camera frame; Gpf is
the landmark position in the global frame and depending on
its representation may also be a function of state elements;
and {Ck
G R, GpCk} denotes the current camera pose (position
and orientation) in the global frame.
The measurement functions hd, hp, and ht correspond to
the intrinsic distortion, projection, and transformation func-
tions and the corresponding measurement Jacobians can be
computed through a simple chain rule. Note that we compute
the errors on the raw uv pixels to allow for calibration of the
camera intrinsics ζ and that the function hd can be changed
to support any camera model (e.g., radial-tangential and
equidistant). We refer readers to the documentation website
for the details of these measurement functions.
D. Online Calibration
We perform online spatiotemporal calibration of the
camera-IMU time offset and extrinsic transformation, and
camera
intrinsics.
Looking
at
the
landmark
measure-
ment (26), one can simply take the derivative with respect
to the desired variables that they wish to calibrate online. In
this case we will have additional Jacobians for the intrinsic ζ
in function hd and {C
I R, CpI} extrinsics that the global pose
{Ck
G R, GpCk} is a function of. For derivations and Jacobian
results, we refer the reader to our documentation.
We also co-estimate the time offset between the camera
and IMU, which can commonly exist in low-cost devices due
to sensor latency, clock skew, or data transmission delays.
Consider the time Ct as expressed in the camera clock is
related to the same instant represented in the IMU clock, It,
by a time offset CtI:
It = Ct + CtI
(27)
This offset is unknown and estimated online. We refer the
reader to [22] for further details.

## Page 4

E. Codebase Documentation
It is our belief that the documentation of this work in itself
is one of the main contributions to the research community.
Both researchers and practitioners with little background in
estimation may struggle to grasp the core theoretical concepts
and important implementation details when it comes to
visual-inertial estimation algorithms. To bridge this gap the
documentation of this codebase takes as much of a priority as
new features that could improve the estimation performance.
As compared to existing open sourced systems with limited
documentation, we focus on providing additional dedicated
derivation pages on how different parts of the code are
derived and interact. The in-code and page documentation
is automatically generated from the codebase using Doxygen
[35] which is then post-processed using m.css [36] to provide
high quality search functionality and mobile friendly layout.
This tight-coupling of our documentation and derivations
within the codebase also ensures that the documentation is
up to date and that developers can easily ﬁnd answers.
IV. VISUAL-INERTIAL SIMULATOR
We now detail how our simulator generates visual-inertial
measurements. We note that this simulator can be easily
extended to include other measurements besides the inertial
and visual-bearing measurements presented below.
A. B-Spline Interpolation
fSg
fig
fi-1g
fi+1g
fi+2g
u
u
u
Fig. 1: Illustrate the B-spline interpolation to a pose G
S T
which is bounded by four control poses.
At the center of the simulator is an SE(3) B-spline
which allows for the calculation of the pose, velocity, and
accelerations at any given timestep along a given trajectory.
We follow the work of Patron-Perez et al. [37] and Mueggler
et al. [38] in which given a series of temporally uniformly
distributed “control point” poses, the pose {S} at a given
timestep ts can be interpolated by:
G
S T(u(ts)) = G
i−1T A0 A1 A2
(28)
Aj = exp

Bj(u(t)) i−1+j
i+j
Ω

(29)
i−1
i
Ω= log

G
i−1T−1 G
i T

(30)
where Bj(u(t)) are our spline interpolation constants,
exp(·), log(·) are the SE(3) matrix exponential and log-
arithm, and the frame notations are shown in Figure 1.
Equation (28) can be interpreted as compounding the fraction
portions of the bounding poses to the ﬁrst pose G
i−1T. It
is then simple to take the time derivative to allow the
computation of the velocity and acceleration at any point.
The only needed input into the simulator is a pose trajectory
which we uniformly sample to construct control points for
the B-spline. This B-spline is then used to both generate
the inertial measurements while also providing the pose
information needed to generate visual-bearing measurements.
B. Inertial Measurements
To incorporate inertial measurements from an IMU sensor,
we can leverage the continuous nature and C2-continuity of
our cubic B-spline. To obtain the true measurements from
our SE(3) B-spline we can do the following:
Iω(t) = vee

G
I R(u(t))⊤G
I ˙R(u(t))

(31)
Ia(t) = G
I R(u(t))⊤G¨pI(u(t))
(32)
where vee(·) returns the vector portion of the skew-
symmetric matrix. These are then corrupted using the random
walk biases and corresponding white noises.
C. Visual-Bearing Measurement
After creating the B-spline trajectory we generate envi-
ronmental landmarks that can be later projected into the
synthetic camera frames. To generate these landmarks, we
increment along the spline at a ﬁxed interval and ensure that
all cameras see enough landmarks in the map. If there are not
enough landmarks in the given camera frame, we generate
new landmarks by sending out random rays from the camera
and assigning a random depth. Landmarks are then added to
the map so that they can be projected into future frames. We
generate landmarks’ visual measurements by projecting them
into the current frame. Projected landmarks are limited to
being within the ﬁeld of view, in front, and close in distance
to the camera. Pixel noise can be directly added to the true
pixel values.
V. BENCHMARKS
A. Simulation Results
With the proposed visual-inertial simulator, we evaluate
the proposed online calibration and the consistency of our
MSCKF estimator, which is implemented based on the First
Estimate Jacobians (FEJ)-EKF [20], [21]. In particular, the
system is run with a monocular camera, a window size
of 11, a maximum of 100 feature tracks per frame, and
a maximum of 50 SLAM landmarks kept in the state,1
along with VIO feature tracks that are processed by the
MSCKF update. The camera is simulated at 10Hz while
the IMU is simulated at 400Hz. We inject one pixel noise
and the IMU noise characteristics of an ADIS16448 MEMS
IMU. To simulate bad initial calibration values, we randomly
initialize the calibration values using the prior distribution
values of the estimator. This ensures that during Monte-Carlo
simulation we have both different measurement noises and
initial calibration values for each run.
As summarized in Table I, the average Absolute Trajec-
tory Error (ATE) and Normalized Estimation Error Squared
(NEES) for each different scenario shows that when perform-
ing online calibration, estimation accuracy does not degrade
if we are given the true calibration; while in the case that we
have bad initial guesses, the estimator remains consistent and
is able to estimate with reasonable accuracy. A representative
run with uncertainty bounds is shown in Figure 2. When
1This might be a little abuse of terminology. We use SLAM landmarks to
refer to the visual features that can be tracked beyond the current window
and will be kept in the state vector and marginalized out when they are lost.

## Page 5

Fig. 2: IMU pose errors and 3σ bounds for a representative
run of the proposed method with SLAM landmarks and
online calibration.
Fig. 3: Camera to IMU time offset error and 3σ bounds for
a representative run.
calibration is disabled and a bad initial guess is used, the
NEES becomes large due to not modeling the uncertainty
that these calibration parameters have, and in many cases
the estimate diverges. We also plot the ﬁrst ten and sixty
seconds of all calibration parameters of a representative run
in Figures 3 and 4, showing that these parameters rapidly
converge from their initially poor guesses.
B. Real-World Comparison
We evaluate the proposed visual-inertial FEJ-MSCKF esti-
mator with and without SLAM landmarks on the Vicon room
scenarios from the EurocMav dataset [39] which provides
both 20Hz stereo images, 200Hz ADIS16448 MEMS IMU
measurements, and optimized groundtruth trajectories. It
should be noted that we have recalculated the V1 01 easy
groundtruth due to the original having incorrect orientation
values and have provided this corrected groundtruth trajec-
TABLE I: Average ATE and NEES over twenty runs with
true or bad calibration, with and without online calibration.
ATE (deg)
ATE (m)
Ori. NEES
Pos. NEES
true w/ calib
0.212
0.134
2.203
1.880
true w/o calib
0.200
0.128
2.265
1.909
bad w/ calib
0.218
0.139
2.235
2.007
bad w/o calib
5.432
508.719
9.159
1045.174
tory to the community on our documentation website. All
methods were run with the conﬁguration ﬁles from their open
sourced repositories with each algorithm being run ten times
on each dataset to compensate for some randomness inherent
to the visual front-ends. In this benchmarking test, we eval-
uate the following state-of-the-art visual-inertial estimation
algorithms:
OKVIS [2] – Keyframe-based ﬁxed-lag smoother which
optimizes arbitrarily spaced keyframe poses connected
with inertial measurement factors and environmental land-
marks. A ﬁxed window size was enforced to ensure com-
putational feasibility with the focus on selective marginal-
ization to allow for problem sparsity.
VINS-Fusion VIO [3] – Extension of the original VINS-
Mono [40] sliding optimization-based method that lever-
ages IMU preintegration which is then loosely coupled
with a secondary pose-graph optimization. VINS-Fusion
extends the original codebase to support stereo cameras.
Basalt VIO [4] – Stereo keyframe-based ﬁx-lag smoother
with custom feature tracking frontend with focus on ex-
tracting relevant information from the VIO for later ofﬂine
visual-inertial mapping.
R-VIO [5] – Robocentric MSCKF-based algorithm which
estimates in a local frame and updates the global frame
through a composition step. The direction of gravity is
also estimated within the ﬁlter.
ROVIO [6] – We use the ROVIO implementation within
maplab [41], which is a monocular iterative EKF-based
approach that performs minimization on the direct image
intensity patches allowing for tracking of non-corner fea-
tures such as high gradient lines.
ICE-BA [7] – Stereo incremental bundle adjustment (BA)
method which optimizes both a local siding window and
global optimization problem in parallel. They exploited the
sparseness of their formulation and introduced a relative
marginalization procedure.
S-MSCKF [8] – An open sourced implementation of original
MSCKF [24] paper with stereo feature tracking and a
focus on high-speed motion scenarios.
Note that we evaluate only the VIO portion of these code-
bases (i.e., not the non-realtime backend pose graph thread
output of VINS-Fusion [3] and visual-inertial mapping of
Basalt [4]), as one could simply append a pose graph
optimizer after any of these odometry methods to improve
long-term accuracy.
Table II shows the average ATE of all methods for each
dataset. It is clear that the addition of SLAM landmarks in
our OpenVINS greatly reduces the drift in the monocular
case, while it has a smaller impact on the stereo performance;
and more importantly, OpenVINS is able to perform com-
petitively to other methods. We additionally compared the
Relative Pose Error (RPE) of all methods. Shown in Table
III, our monocular system clearly outperforms the current
open-sourced codebases, with our stereo system being able
to perform second to Basalt. While we did not evaluate per-
frame timing rigorously, we found that Basalt outperformed
all other algorithms, with our proposed method being limited
by the visual-frontend implementation from OpenCV [42].

## Page 6

Fig. 4: Camera intrinsic projection and distortion along with extrinsic orientation and positions parameters error and 3σ
bounds for a representative run. Note that we only plot the ﬁrst sixty seconds of the dataset.
TABLE II: Ten runs mean absolute trajectory error (ATE) for each algorithm in units of degree/meters. Note that V2 03
dataset is excluded due the inability for some algorithms to run on it.
V1 01 easy
V1 02 medium
V1 03 difﬁcult
V2 01 easy
V2 02 medium
Average
mono ov slam
0.699 / 0.058
1.675 / 0.076
2.542 / 0.063
0.773 / 0.124
1.538 / 0.074
1.445 / 0.079
mono ov vio
0.642 / 0.076
1.766 / 0.096
2.391 / 0.344
1.164 / 0.121
1.248 / 0.106
1.442 / 0.148
mono okvis
0.823 / 0.090
2.082 / 0.146
4.122 / 0.222
0.826 / 0.117
1.704 / 0.197
1.911 / 0.154
mono rovioli
2.249 / 0.153
1.635 / 0.131
3.253 / 0.158
1.455 / 0.106
1.678 / 0.153
2.054 / 0.140
mono rvio
0.994 / 0.094
2.288 / 0.129
1.757 / 0.147
1.735 / 0.144
1.690 / 0.233
1.693 / 0.149
mono vinsfusion vio
1.199 / 0.064
3.542 / 0.103
5.934 / 0.202
1.585 / 0.073
2.370 / 0.079
2.926 / 0.104
stereo ov slam
0.856 / 0.061
1.813 / 0.047
2.764 / 0.059
1.037 / 0.056
1.292 / 0.047
1.552 / 0.054
stereo ov vio
0.905 / 0.061
1.767 / 0.056
2.339 / 0.057
1.106 / 0.053
1.151 / 0.048
1.454 / 0.055
stereo basalt
0.654 / 0.035
2.067 / 0.059
2.017 / 0.085
0.981 / 0.046
0.888 / 0.059
1.321 / 0.057
stereo iceba
0.909 / 0.059
2.574 / 0.120
3.206 / 0.137
1.819 / 0.128
1.212 / 0.116
1.944 / 0.112
stereo okvis
0.603 / 0.039
1.963 / 0.079
4.117 / 0.122
0.834 / 0.075
1.201 / 0.092
1.744 / 0.081
stereo smsckf
1.108 / 0.086
2.147 / 0.121
3.918 / 0.198
1.181 / 0.083
2.142 / 0.164
2.099 / 0.130
stereo vinsfusion vio
1.073 / 0.054
2.695 / 0.089
3.643 / 0.132
2.499 / 0.071
2.006 / 0.074
2.383 / 0.084
TABLE III: Relative pose error (RPE) for different segment lengths for each algorithm variation over all datasets in units
of degree/meters. Note that V2 03 dataset is excluded due the inability for some algorithms to run on it.
8m
16m
24m
32m
40m
48m
mono ov slam
0.604 / 0.066
0.680 / 0.076
0.829 / 0.086
0.962 / 0.095
0.995 / 0.101
1.056 / 0.111
mono ov vio
0.721 / 0.083
0.832 / 0.093
1.057 / 0.104
1.204 / 0.108
1.216 / 0.113
1.283 / 0.143
mono okvis
0.605 / 0.089
0.768 / 0.131
0.912 / 0.167
1.007 / 0.191
1.076 / 0.202
1.212 / 0.225
mono rovioli
1.046 / 0.080
1.364 / 0.114
1.659 / 0.150
1.998 / 0.181
2.023 / 0.216
2.133 / 0.234
mono rvio
0.624 / 0.116
0.741 / 0.137
0.852 / 0.158
0.974 / 0.171
0.943 / 0.185
0.974 / 0.214
mono vinsfusion vio
0.785 / 0.063
1.040 / 0.081
1.453 / 0.109
1.703 / 0.121
1.750 / 0.134
1.762 / 0.143
stereo ov slam
0.617 / 0.060
0.711 / 0.074
0.892 / 0.079
1.040 / 0.086
1.057 / 0.085
1.252 / 0.089
stereo ov vio
0.651 / 0.060
0.726 / 0.068
0.909 / 0.075
1.065 / 0.085
1.080 / 0.084
1.274 / 0.093
stereo basalt
0.517 / 0.054
0.546 / 0.065
0.582 / 0.072
0.649 / 0.079
0.596 / 0.081
0.677 / 0.086
stereo iceba
0.849 / 0.079
1.071 / 0.102
1.279 / 0.122
1.446 / 0.123
1.549 / 0.136
1.876 / 0.160
stereo okvis
0.557 / 0.055
0.667 / 0.072
0.802 / 0.088
0.897 / 0.105
0.945 / 0.114
1.073 / 0.124
stereo smsckf
0.944 / 0.087
1.244 / 0.116
1.472 / 0.136
1.494 / 0.150
1.587 / 0.163
1.752 / 0.178
stereo vinsfusion vio
0.780 / 0.052
1.077 / 0.068
1.467 / 0.080
1.761 / 0.099
1.851 / 0.106
1.797 / 0.110
VI. CONCLUSION AND FUTURE WORK
In this paper we have presented our OpenVINS (OV)
system as a platform for the research community. At the core
we provide the visual processing frontend, full visual-inertial
simulator, and modular on-manifold EKF. In particular, we
have implemented the FEJ-based MSCKF with and without
SLAM landmarks and demonstrated the competing perfor-
mance of our estimator. We have heavily documented the
project to allow for researchers and practitioners to quickly
build on top of this work with minimal estimation theory
background. In the future we plan to expand our system
to provide a sliding window optimization-based estimator
leveraging our closed-form preintegration [43]. We are also
interested in integrating visual-inertial mapping and percep-
tion capabilities into OpenVINS.
REFERENCES
[1] G. Huang, “Visual-inertial navigation: A concise review,” in Proc.
International Conference on Robotics and Automation, Montreal,
Canada, May 2019.
[2] S. Leutenegger, S. Lynen, M. Bosse, R. Siegwart, and P. Furgale,
“Keyframe-based visual-inertial odometry using nonlinear optimiza-
tion,” International Journal of Robotics Research, vol. 34, no. 3, pp.
314–334, 2015.

## Page 7

[3] T. Qin, J. Pan, S. Cao, and S. Shen, “A general optimization-based
framework for local odometry estimation with multiple sensors,”
CoRR, vol. abs/1901.03638, 2019.
[4] V. C. Usenko, N. Demmel, D. Schubert, J. St¨uckler, and D. Cremers,
“Visual-inertial mapping with non-linear factor recovery,” CoRR, vol.
abs/1904.06504, 2019.
[5] Z. Huai and G. Huang, “Robocentric visual-inertial odometry,” Inter-
national Journal of Robotics Research, Apr. 2019.
[6] M. Bloesch, M. Burri, S. Omari, M. Hutter, and R. Siegwart, “Iterated
extended kalman ﬁlter based visual-inertial odometry using direct pho-
tometric feedback,” The International Journal of Robotics Research,
vol. 36, no. 10, pp. 1053–1072, 2017.
[7] H. Liu, M. Chen, G. Zhang, H. Bao, and Y. Bao, “Ice-ba: Incremental,
consistent and efﬁcient bundle adjustment for visual-inertial slam,” in
Proceedings of the IEEE Conference on Computer Vision and Pattern
Recognition, 2018, pp. 1974–1982.
[8] K. Sun, K. Mohta, B. Pfrommer, M. Watterson, S. Liu, Y. Mulgaonkar,
C. J. Taylor, and V. Kumar, “Robust stereo visual inertial odometry
for fast autonomous ﬂight,” IEEE Robotics and Automation Letters,
vol. 3, no. 2, pp. 965–972, April 2018.
[9] K. Eckenhoff, P. Geneva, J. Bloecker, and G. Huang, “Multi-camera
visual-inertial navigation with online intrinsic and extrinsic calibra-
tion,” in Proc. International Conference on Robotics and Automation,
Montreal, Canada, May 2019.
[10] K. Eckenhoff, P. Geneva, and G. Huang, “Sensor-failure-resilient
multi-imu visual-inertial navigation,” in Proc. International Confer-
ence on Robotics and Automation, Montreal, Canada, May 2019.
[11] K. Eckenhoff, Y. Yang, P. Geneva, and G. Huang, “Tightly-coupled
visual-inertial localization and 3D rigid-body target tracking,” IEEE
Robotics and Automation Letters (RA-L), vol. 4, no. 2, pp. 1541–1548,
2019.
[12] P. Geneva, K. Eckenhoff, and G. Huang, “A linear-complexity EKF for
visual-inertial navigation with loop closures,” in Proc. International
Conference on Robotics and Automation, Montreal, Canada, May
2019.
[13] P. Geneva, J. Maley, and G. Huang, “An efﬁcient schmidt-ekf for 3D
visual-inertial SLAM,” in Proc. Conference on Computer Vision and
Pattern Recognition (CVPR), Long Beach, CA, June 2019.
[14] Y. Yang, P. Geneva, X. Zuo, K. Eckenhoff, Y. Liu, and G. Huang,
“Tightly-coupled aided inertial navigation with point and plane fea-
tures,” in Proc. International Conference on Robotics and Automation,
Montreal, Canada, May 2019.
[15] Y. Yang, P. Geneva, K. Eckenhoff, and G. Huang, “Visual-inertial
odometry with point and line features,” Macau, China, Nov. 2019.
[16] X. Zuo, P. Geneva, W. Lee, Y. Liu, and G. Huang, “LIC-Fusion: Lidar-
inertial-camera odometry,” Macau, China, Nov. 2019.
[17] X. Zuo, P. Geneva, Y. Yang, W. Ye, Y. Liu, and G. Huang, “Visual-
inertial localization with prior lidar map constraints,” IEEE Robotics
and Automation Letters (RA-L), 2019.
[18] Y. Yang, P. Geneva, K. Eckenhoff, and G. Huang, “Degenerate motion
analysis for aided INS with online spatial and temporal calibration,”
IEEE Robotics and Automation Letters (RA-L), vol. 4, no. 2, pp. 2070–
2077, 2019.
[19] G. Huang, A. I. Mourikis, and S. I. Roumeliotis, “Analysis and
improvement of the consistency of extended Kalman ﬁlter-based
SLAM,” in Proc. of the IEEE International Conference on Robotics
and Automation, Pasadena, CA, May 19-23 2008, pp. 473–479.
[20] ——, “A ﬁrst-estimates Jacobian EKF for improving SLAM consis-
tency,” in Proc. of the 11th International Symposium on Experimental
Robotics, Athens, Greece, July 14–17, 2008.
[21] ——, “Observability-based rules for designing consistent EKF SLAM
estimators,” International Journal of Robotics Research, vol. 29, no. 5,
pp. 502–528, Apr. 2010.
[22] M. Li and A. I. Mourikis, “Online temporal calibration for Camera-
IMU systems: Theory and algorithms,” International Journal of
Robotics Research, vol. 33, no. 7, pp. 947–964, June 2014.
[23] M. Li, H. Yu, X. Zheng, and A. I. Mourikis, “High-ﬁdelity sensor
modeling and self-calibration in vision-aided inertial navigation,” in
IEEE International Conference on Robotics and Automation (ICRA),
May 2014, pp. 409–416.
[24] A. I. Mourikis and S. I. Roumeliotis, “A multi-state constraint Kalman
ﬁlter for vision-aided inertial navigation,” in Proceedings of the IEEE
International Conference on Robotics and Automation, Rome, Italy,
Apr. 10–14, 2007, pp. 3565–3572.
[25] N. Trawny and S. I. Roumeliotis, “Indirect Kalman ﬁlter for 3D
attitude estimation,” University of Minnesota, Dept. of Comp. Sci.
& Eng., Tech. Rep., Mar. 2005.
[26] C. Hertzberg, R. Wagner, U. Frese, and L. Schr¨oder, “Integrating
generic sensor fusion algorithms with sound state representations
through encapsulation of manifolds,” Information Fusion, vol. 14,
no. 1, pp. 57–77, 2013.
[27] K. Wu, T. Zhang, D. Su, S. Huang, and G. Dissanayake, “An
invariant-ekf vins algorithm for improving consistency,” in Proc. of the
IEEE/RSJ International Conference on Intelligent Robots and Systems,
Sept 2017, pp. 1578–1585.
[28] J. Civera, A. Davison, and J. Montiel, “Inverse depth parametrization
for monocular SLAM,” IEEE Transactions on Robotics, vol. 24, no. 5,
pp. 932–945, Oct. 2008.
[29] M. K. Paul, K. Wu, J. A. Hesch, E. D. Nerurkar, and S. I. Roumeliotis,
“A comparative analysis of tightly-coupled monocular, binocular, and
stereo VINS,” in Proc. of the IEEE International Conference on
Robotics and Automation, Singapore, July 2017, pp. 165–172.
[30] A. B. Chatﬁeld, Fundamentals of High Accuracy Inertial Navigation.
AIAA, 1997.
[31] F. Dellaert, “Factor graphs and gtsam: A hands-on introduction,”
Georgia Institute of Technology, Tech. Rep., 2012.
[32] M. Li, “Visual-inertial odometry on resource-constrained systems,”
Ph.D. dissertation, UC Riverside, 2014.
[33] Y. Yang, J. Maley, and G. Huang, “Null-space-based marginalization:
Analysis and algorithm,” in Proc. IEEE/RSJ International Conference
on Intelligent Robots and Systems, Vancouver, Canada, Sept. 24-28,
2017, pp. 6749–6755.
[34] S. I. Roumeliotis and J. W. Burdick, “Stochastic cloning: A generalized
framework for processing relative state measurements,” in Proceedings
of the IEEE International Conference on Robotics and Automation,
Washington, DC, May 11-15, 2002, pp. 1788–1795.
[35] D. Van Heesch, “Doxygen: Source code documentation generator
tool,” URL: http://www.doxygen.org, 2008.
[36] V. Vondruˇs, “m.css: A no-nonsense, no-javascript css framework
and pelican theme for content-oriented websites,” URL: https://mcss.
mosra.cz/, 2018.
[37] A. Patron-Perez, S. Lovegrove, and G. Sibley, “A spline-based tra-
jectory representation for sensor fusion and rolling shutter cameras,”
International Journal of Computer Vision, vol. 113, no. 3, pp. 208–
219, 2015.
[38] E.
Mueggler,
G.
Gallego,
H.
Rebecq,
and
D.
Scaramuzza,
“Continuous-time visual-inertial odometry for event cameras,” IEEE
Transactions on Robotics, pp. 1–16, 2018.
[39] M. Burri, J. Nikolic, P. Gohl, T. Schneider, J. Rehder, S. Omari, M. W.
Achtelik, and R. Siegwart, “The euroc micro aerial vehicle datasets,”
The International Journal of Robotics Research, vol. 35, no. 10, pp.
1157–1163, 2016.
[40] T. Qin, P. Li, and S. Shen, “VINS-Mono: A robust and versa-
tile monocular visual-inertial state estimator,” IEEE Transactions on
Robotics, vol. 34, no. 4, pp. 1004–1020, 2018.
[41] T. Schneider, M. Dymczyk, M. Fehr, K. Egger, S. Lynen, I. Gilitschen-
ski, and R. Siegwart, “Maplab: An open framework for research in
visual-inertial mapping and localization,” IEEE Robotics and Automa-
tion Letters, vol. 3, no. 3, pp. 1418–1425, July 2018.
[42] OpenCV Developers Team, “Open source computer vision (OpenCV)
library,” Available: http://opencv.org.
[43] K. Eckenhoff, P. Geneva, and G. Huang, “Closed-form preintegra-
tion methods for graph-based visual-inertial navigation,” International
Journal of Robotics Research, vol. 38, no. 5, pp. 563–586, 2019.
