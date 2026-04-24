# FAST-LIVO2 Fast, Direct LiDAR-Inertial-Visual Odometry.pdf

## Page 1

1
FAST-LIVO2: Fast, Direct LiDAR-Inertial-Visual
Odometry
Chunran Zheng1, Wei Xu1, Zuhao Zou1, Tong Hua1, Chongjian Yuan1, Dongjiao He1, Bingyang Zhou1, Zheng
Liu1, Jiarong Lin1, Fangcheng Zhu1, Yunfan Ren1, Rong Wang2, Fanle Meng2, Fu Zhang1†
Fig. 1: FAST-LIVO2 mapping results generated in real time. (a)-(c) showcase airborne mapping, (d) represents a retail street
collected with a handheld device, and (e) demonstrates an experiment where a UAV carrying a LiDAR, camera and inertial
sensor perform real-time state estimation (i.e., FAST-LIVO2), trajectory planning, and tracking control all on its onboard
computer. In (d)-(e), blue lines represent the computed trajectory. In (e1)-(e4), white points indicate the LiDAR scan at that
moment, and colored lines depict the planned trajectory. (e1) and (e4) mark areas of LiDAR degeneration. (e2) and (e3) show
obstacle avoidance. (e5) and (e6) depict the camera first-person view from indoor to outdoor, highlighting large illumination
variation from sudden overexposure to normal (see our accompanying video on YouTube: youtu.be/aSAwVqR22mo).
Abstract—This paper proposes FAST-LIVO2: a fast, direct
LiDAR-inertial-visual odometry framework to achieve accurate
and robust state estimation in Simultaneous Localization and
Mapping (SLAM) tasks and provide great potential in real-
time, onboard robotic applications. FAST-LIVO2 fuses the IMU,
LiDAR and image measurements, efficiently through an error-
state iterated kalman filter (ESIKF). To address the dimension
mismatch between the heterogeneous LiDAR and image measure-
†Corresponding author (email: fuzhang@hku.hk)
1Mechatronics and Robotic Systems (MaRS) Laboratory, Department of
Mechanical Engineering, University of Hong Kong, Hong Kong SAR, China.
2Information Science Academy of China Electronics Technology Group
Corporation
ments, we use a sequential update strategy in the Kalman filter.
To enhance the efficiency, we use direct methods for both the
visual and LiDAR fusion, where the LiDAR module registers raw
points without extracting edge or plane features and the visual
module minimizes direct photometric errors without extracting
ORB or FAST corner features. The fusion of both visual and
LiDAR measurements is based on a single unified voxel map
where the LiDAR module constructs the geometric structure for
registering new LiDAR scans and the visual module attaches
image patches to the LiDAR points (i.e., visual map points)
enabling new image alignment. To enhance the accuracy of image
alignment, we use plane priors from the LiDAR points in the
voxel map (and even refine the plane prior in the alignment
process) and update the reference patch dynamically after new
arXiv:2408.14035v2  [cs.RO]  28 Aug 2024

## Page 2

2
images are aligned. Furthermore, to enhance the robustness
of image alignment, FAST-LIVO2 employs an on-demanding
raycast operation and estimates the image exposure time in real
time. We conduct extensive experiments on both benchmark
and private datasets, demonstrating that our proposed system
significantly outperforms other state-of-the-art odometry systems
in terms of accuracy, robustness, and computation efficiency.
Moreover, the effectiveness of key modules in the system is also
validated. Lastly, we detail three applications of FAST-LIVO2:
UAV onboard navigation demonstrating the system’s computation
efficiency for real-time onboard navigation, airborne mapping
showcasing the system’s mapping accuracy, and 3D model ren-
dering (mesh-based and NeRF-based) underscoring the suitability
of our reconstructed dense map for subsequent rendering tasks.
We open source our code, dataset and application of this work
on GitHub1 to benefit the robotics community.
Index
Terms—Simultaneous
Localization
and
Mapping
(SLAM), Sensor Fusion, 3D Reconstruction, Aerial Navigation.
I. INTRODUCTION
I
N recent years, simultaneous localization and mapping
(SLAM) technology has seen significant advancements,
particularly in real-time 3D reconstruction and localization in
unknown environments. Due to its ability to estimate poses
and reconstruct maps in real time, SLAM has become indis-
pensable for various robot navigation tasks. The localization
process delivers crucial state feedback for the robot’s onboard
controllers, while the dense 3D map provides key environmen-
tal information, such as free spaces and obstacles, essential
for effective trajectory planning. A colored map also carries
substantial semantic information, enabling a vivid representa-
tion of the real world that opens up vast potential applications,
such as virtual and augmented reality, 3D modeling, and robot-
human interactions.
Currently, several SLAM frameworks have been success-
fully implemented with single-measurement sensors, primar-
ily cameras [1]–[4] or LiDAR [5]–[7]. Although visual and
LiDAR SLAM have shown promise in their own domains,
each has inherent limitations that constrain their performance
in various scenarios.
Visual SLAM, leveraging cost-effective CMOS sensors and
lenses, is capable of establishing accurate data associations,
thereby achieving a certain level of localization accuracy. The
abundance of color information further enriches the semantic
perception. Further leveraging this enhanced scene comprehen-
sion, deep learning methods are employed for robust feature
extraction and dynamic object filtering. However, the lack
of direct depth measurement in visual SLAM necessitates
concurrent optimization of map points via operations such as
triangulation or depth filtering, which introduces significant
computational overhead that often limits map accuracy and
density. Visual SLAM also encounters numerous other lim-
itations, such as varying measurement noise across different
scales, sensitivity to illumination changes, and the impact of
texture-less environments on data association.
LiDAR SLAM, utilizing LiDAR sensors, obtains precise
depth measurements directly, offering superior precision and
efficiency in localization and mapping tasks compared with
1https://github.com/hku-mars/FAST-LIVO2
visual SLAM. Despite these strengths, LiDAR SLAM exhibits
several significant shortcomings. On one hand, the point cloud
maps it reconstructs, albeit detailed, lack color information,
thereby reducing their information scale. On the other hand,
LiDAR SLAM performance tends to deteriorate in environ-
ments presenting insufficient geometric constraints, such as
narrow tunnels, a single and extended wall, etc.
As the demand to operate intelligent robots in the real world
grows, especially in environments that often lack structure or
texture, it is becoming clear that existing systems relying on
a single sensor cannot provide the accurate and robust pose
estimation as required. To address this issue, the fusion of
commonly-used sensors such as LiDAR, camera, and IMU is
gaining increasing attention. This strategy not only combines
the strengths of these sensors to provide enhanced pose
estimation, but also aids in the construction of accurate, dense,
and colored point cloud maps, even in environments where the
performance of individual sensors degenerate.
Efficient
and
accurate
LiDAR-inertial-visual
odometry
(LIVO) and mapping are still challenging problems: 1) The
entire LIVO system is tasked with processing LiDAR mea-
surements, consisting of hundreds to thousands of points per
second, as well as high-rate, high-resolution images. The
challenge of fully utilizing such a vast amount of data, partic-
ularly with limited onboard resources, necessitates exceptional
computational efficiency; 2) Many existing systems typically
incorporate a LiDAR-Inertial Odometry (LIO) subsystem and
a Visual-Inertial Odometry (VIO) subsystem, each necessitat-
ing the extraction of features from visual and LiDAR data
respectively to reduce computational load. In environments
that lack structure or texture, this extraction process often
results in limited feature points. Furthermore, to optimize
feature extraction, extensive engineering adaptations are es-
sential to accommodate the variability in LiDAR scanning
patterns and point densities; 3) To reduce computational
demands and achieve tighter integration between camera and
LiDAR measurements, a unified map is essential to man-
age sparse points and the observed high-resolution image
measurements simultaneously. However, designing and main-
taining such maps are particularly challenging considering
the heterogeneous measurements of LiDAR and cameras; 4)
To ensure the accuracy of the reconstructed colored point
cloud, pose estimation needs to achieve pixel-level accuracy.
Meeting this standard presents considerable challenges: proper
hardware synchronization, rigorous pre-calibration of extrinsic
parameters between LiDAR and cameras, precise recovery of
exposure time, and a fusion strategy capable of reaching pixel-
level accuracy in real time.
Motivated by these issues, we propose FAST-LIVO2, a
high-efficiency LIVO system that tightly integrates LiDAR,
image and IMU measurements through a sequentially updated
error-state iterated Kalman filter (ESIKF). With the prior from
IMU propagation, the system state is updated sequentially,
first by the LiDAR measurements and then by the image
measurements, both utilizing direct methods based on a single
unified voxel map. Specifically, in the LiDAR update, the
system registers raw points to the map to construct and update
its geometric structure, and in the visual update, the system

## Page 3

3
reuses LiDAR map points as the visual map points directly
without extracting, triangulating, or optimizing any visual
features from images. The chosen visual map points in the
map are attached with reference image patches previously
observed and then projected to the current image to align
its pose by minimizing the direct photometric errors (i.e.,
sparse image alignment). To improve the accuracy in the image
alignment, FAST-LIVO2 dynamically updates the reference
patches and uses the plane priors obtained from LiDAR
points. For improved computation efficiency, FAST-LIVO2
uses LiDAR points to identify visual map points visible from
the current image and conduct an on-demanding voxel raycast
in case of no LiDAR points. FAST-LIVO2 also estimates the
exposure time in real time to handle illumination variation.
FAST-LIVO2 is developed based on FAST-LIVO first pro-
posed in our previous work [8]. The new contributions com-
pared to FAST-LIVO are listed below:
1) We propose an efficient ESIKF framework with sequen-
tial update to address the dimension mismatch between
LiDAR and visual measurements, improving the robust-
ness of FAST-LIVO that uses asynchronous updates.
2) We use (and even refine) plane priors from LiDAR
points for improved accuracy. In contrast, FAST-LIVO
assumes all pixels in a patch share the same depth, a
wild assumption significantly reducing the accuracy of
affine warping in image alignment.
3) We propose a reference patch update strategy to improve
the accuracy of image alignment, by selecting high-
quality, inlier reference patches that have large parallax
and sufficient texture details. FAST-LIVO selects the
reference patch based on proximity to the current view,
often resulting in low-quality reference patches degrading
the accuracy.
4) We conduct online exposure time estimation for handling
environment illumination variation. FAST-LIVO did not
address this issue, leading to poor convergence in image
alignment under significant lighting changes.
5) We propose on-demand voxel raycasting to enhance the
system robustness in the absence of LiDAR point mea-
surements caused by LiDAR close proximity blind zones,
an issue not considered in FAST-LIVO.
Each of the above contributions are evaluated in com-
prehensive ablation studies to verify their effectiveness. We
implement the proposed system as practical open software,
meticulously optimized for real-time operation on both Intel
and ARM processors. The system is versatile, supporting
multi-line spinning LiDARs, emerging solid-state LiDARs
with unconventional scanning patterns, as well as both pinhole
cameras and various fisheye cameras.
Besides, we conduct extensive experiments on 25 sequences
of public datasets (i.e., Hilti and NTU-VIRAL datasets),
alongside various representative private datasets, enabling a
comparison with other state-of-the-art SLAM systems (e.g.,
R3LIVE, LVI-SAM, FAST-LIO2, etc). Both qualitative and
quantitative results demonstrate that our proposed system
significantly outpaces other counterparts in terms of accuracy
and robustness at a reduced computation cost.
Taking a step further to underline the real-world applicabil-
ity and versatility of our system, we deploy three distinctive
applications. Firstly, fully onboard autonomous UAV naviga-
tion, demonstrating the system’s real-time capabilities, marks
a pioneering instance of employing a LiDAR-inertial-visual
system for real-world autonomous UAV flights. Secondly,
airborne mapping showcases the system’s pixel-level precision
under structure-less environments in practical use. Lastly, the
high-quality generation of mesh, texturing, and NeRF models
underscores the system’s suitability for rendering tasks. We
make our code and dataset available on GitHub.
II. RELATED WORKS
A. Direct Methods
Direct methods stand out as a prominent approach for fast
pose estimation in both visual and LiDAR SLAM. Unlike
feature-based methods [5, 6, 9, 10] which necessitate the
extraction of salient feature points (e.g., corners and edge
pixels in images; plane and edge points in LiDAR scans)
and the generation of robust descriptors for matching, direct
methods directly leverage raw measurements to optimize the
sensor pose [11] by minimizing an error function based on
photometric error or point-to-plane residuals, e.g., [3, 12]–
[14]. By eliminating the time-consuming feature extraction and
matching, direct methods offer fast pose estimation. Nonethe-
less, the absence of feature matching requires fairly accurate
state prior estimation to avoid local minima.
Direct methods in visual SLAM can be broadly categorized
into dense direct, semi-dense direct, and sparse direct methods.
Dense direct methods, predominantly adopted for RGB-D
cameras with full depth measurements as exemplified by [15]–
[17], apply image-to-model alignment for pose estimation. In
contrast, semi-dense direct methods [3, 18] implement direct
image alignment by capitalizing on pixels with significant
gray-level gradients for estimation. Sparse direct methods
[2, 12] focus on delivering accurate state estimation through
only a few well-selected raw patches, thus further diminishing
the computational burden in comparison to both dense and
semi-dense direct methods.
Unlike direct visual SLAM methods, direct LiDAR SLAM
systems [13, 14, 19, 20] do not distinguish between dense and
sparse approaches and commonly use spatially-downsampled
or temporally-downsampled raw points in each scan to con-
struct constraints for pose optimization.
In our work, we harness the principles of the direct method
for both LiDAR and visual modules. The LiDAR module of
our system is adapted from VoxelMap [14], and the visual
model is based on a variant of sparse direct method [12].
While drawing inspiration from sparse direct image alignment
in [12], our visual module differs by re-utilizing the LiDAR
points as visual map points, thus mitigating the intensive
backend computations (i.e., feature alignment, sliding window
optimization and/or depth filtering).
B. LiDAR-visual(-inertial) SLAM
The incorporation of multiple sensors in LiDAR-visual-
inertial SLAM equips the system with the capability to han-
dle a wide range of challenging environments, particularly

## Page 4

4
when one sensor experiences failure or partial degeneration.
Motivated by this, the research community has seen the
emergence of various LiDAR-visual-inertial SLAM systems.
Existing methods can generally be divided into two categories:
loosely coupled and tightly coupled. The classification can be
determined from two perspectives: the state estimation level
and the raw measurement level. At the state estimation level,
the key is whether the estimate from one sensor serves as an
optimization objective in another sensor’s model. At the raw
measurement level, it involves whether raw data from different
sensors are combined.
Zhang et al. propose a LiDAR-Visual-Inertial SLAM system
[21] that is loosely coupled at the state estimation level. In
this system, VIO subsystem only provides the initial pose
for the scan registration in LIO subsystem, instead of being
optimized jointly with the scan registration. VIL-SLAM [22]
employs a similar loosely-coupled method, not utilizing joint
optimization of LiDAR, camera, and IMU measurements.
Some systems (e.g., DEMO [23], LIMO [24], CamVox [25],
[26]) use 3D LiDAR points to provide depth measurements
for the visual module [1, 4, 27]. While these systems exhibit
measurement-level tight coupling, they remain loosely-coupled
in state estimation, primarily due to the absence of constraints
directly derived from LiDAR measurements at state estima-
tion. Another issue arises as 3D LiDAR points do not have
a one-to-one correspondence with 2D image feature points
and/or lines due to mismatched resolutions. This mismatch
requires interpolation in depth association, introducing po-
tential errors. To address this, DVL-SLAM [28] employs a
direct method for visual tracking, wherein the LiDAR points
are directly projected into the image to ascertain the depth of
corresponding pixel positions.
The works mentioned above have not achieved tight cou-
pling at the state estimation level. In pursuit of higher accuracy
and robustness, many recent studies have emerged that jointly
optimize sensor data in a tightly-coupled manner. To name a
few, LIC-Fusion [29] tightly fuses IMU measurements, sparse
visual features, and LiDAR plane and edge features based on
the MSCKF [30] framework. The subsequent LIC-Fusion2.0
[31] enhances LiDAR pose estimation by implementing plane-
feature tracking within a sliding window. VILENS [32] offers
a joint optimization of visual, LiDAR, and inertial data through
a unified factor graph, relying on fixed lag smoothing. R2LIVE
[33] tightly fuses the LiDAR, camera and IMU measurements
in an on-manifold iterated Kalman filter [34]. For the VIO
subsystem in R2LIVE, a sliding window optimization is used
to triangulate the locations of visual features in the map.
Several systems achieve complete tight coupling at both
the measurement and state estimation levels. LVI-SAM [35]
fuses the LiDAR, visual and inertial sensors in a tightly-
coupled smoothing and mapping framework, which is built
atop a factor graph. The VIO subsystem performs visual
feature tracking and extracts feature depth using LiDAR scans.
R3LIVE [36] constructs the geometric structure of the global
map by LIO and renders map texture by VIO. These two
subsystems estimate the system state jointly by fusing their
respective LiDAR or visual data with IMUs. The advanced
version, R3LIVE++ [37], estimates exposure time in real
time and conducts photometric calibration in advance [38],
which enables the system to recover the radiance of map
points. Unlike most previously mentioned LiDAR-inertial-
visual systems that rely on feature-based methods for both
LIO and VIO subsystems, R3LIVE series [36, 37] adopt direct
methods for both without feature extraction, enabling them to
capture subtle environmental features even in texture-less or
structure-less scenarios.
Our system also jointly estimates the state using LiDAR,
image and IMU data, and maintains a tightly-coupled voxel
map at the measurement level. Furtheremore, our system uses
direct methods, harnessing raw LiDAR points for LiDAR
scan registration and employing raw image patches for visual
tracking. The key difference between our system and R3LIVE
(or R3LIVE++) is that R3LIVE (and R3LIVE++) operate at
an individual pixel level in the VIO, while our system operates
at image patch levels. This difference bestows our system
with marked advantages. Firstly, in terms of robustness, our
methodology uses a simplified, one-step frame-to-map sparse
image alignment for pose estimation, mitigating the heavy
reliance on an accurate initial state that is has to be obtained
by a frame-to-frame optical flow in R3LIVEs. Consequently,
our system simplifies and improves upon the two-stage frame-
to-frame and frame-to-map operations in R3LIVE. Secondly,
from a computational standpoint, the VIO in R3LIVE pre-
dominantly employs a dense direct method which is computa-
tionally expensive, necessitating extensive points for residual
construction and rendering. In contrast, our sparse direct
method provides enhanced computational efficiency. Lastly,
our system exploits information at the resolution of raw image
patches, whereas R3LIVE is capped at the resolution of its
point map.
The visual module of our system is most similar to DV-
LOAM [39], SDV-LOAM [40] and LVIO-Fusion [41], which
projects LiDAR points attached with patches into a new image
and tracks the image by minimizing the direct photometric
error. However, they have several key differences, such as the
use of separate maps for vision and LiDAR, reliance on the
assumption of constant depth in patch warping in the visual
module, loosely-coupling at the state estimation level, and two
stages of frame-to-frame and frame-to-keyframes for image
alignment. In contrast, our system tightly integrates frame-
to-map image alignment, LiDAR scan registration, and IMU
measurements in an iterated Kalman filter. Besides, thanks to
the single unified map for both LiDAR and visual modules,
our system can directly employ the plane priors provided by
the LiDAR points to accelerate the image alignment.
III. SYSTEM OVERVIEW
The overview of our system is shown in Fig. 2, which
contains four sections: ESIKF (Section IV), Local Mapping
(Section V), LiDAR Measurement Model (Section VI), and
Visual Measurement Model (Section VII).
The asynchronously-sampled LiDAR points are first re-
combined into scans at the camera’s sampling time through
scan recombination. Then, we tightly couple the LiDAR,
image and inertial measurements via an ESIKF with sequential

## Page 5

5
Fig. 2: System overview of FAST-LIVO2.
TABLE I: Some Important Notations
Notations
Explanation
⊞/ ⊟
The encapsulated “boxplus” and
“boxminus” operations on the state manifold
G(·)
A vector (·) in global world frame
C(·)
A vector (·) in camera frame
ITL
The extrinsic of LiDAR frame w.r.t. IMU frame
CTI
The extrinsic of IMU frame w.r.t. camera frame
GTI
The pose of IMU frame at time k w.r.t. the global frame
x, bx, ¯x
The ground-truth, predicted and updated estimation of x
bxκ
The κ-th update of x
δx
The error state between ground-truth x and its estimation
state update, where the system state is updated sequentially,
first by the LiDAR measurements and then by the image
measurements, both utilizing direct methods based on a single
unified voxel map (Section IV). To construct the LiDAR
measurement model in the ESIKF update (Section VI), we
compute the frame-to-map point-to-plane residual. To establish
visual measurement model (Section VII), we extract the visual
map points within the current FoV from the map, making use
of visible voxel query and on-demand raycasting; after the
extraction, we identify and discard outlier visual map points
(e.g., points that are occluded or exhibit depth discontinuity);
we then compute frame-to-map image photometric errors for
visual update.
The local map for both visual and LiDAR updates is a voxel-
map structure (Section V): the LiDAR points construct and
update the map’s geometric structure, while the visual images
append image patches to selected map points (i.e., visual map
points) and update reference patches dynamically. The updated
reference patches have their normal vectors further refined in
a separate thread.
IV. ERROR-STATE ITERATED KALMAN FILTER WITH
SEQUENTIAL STATE UPDATE
This section outlines the system’s architecture, based on
the sequentially-updated Error-State Iterated Kalman Filter
(ESIKF) framework.
A. Notations and State Transition Model
In our system, we assume the time offsets among the three
sensors (LiDAR, IMU and camera) are known, which can be
calibrated or synchronized in advance. We take IMU frame
(denoted as I) as the body frame and the first body frame as
Camera
IMU
LiDAR 
points
Time
tk-1
tk
Forward propagation
Backward propagation
10~50Hz
100~250Hz
100~500kHz
Fig. 3: Illustration of scan recombination, forward propagation
and backward propagation applied to input data.
the global frame (denoted as G). Besides, we assume that the
three sensors are rigidly attached and the extrinsic, defined in
Table I, are pre-calibrated. Then, the discrete state transition
model at the i-th IMU measurement is:
xi+1 = xi ⊞(∆tf (xi, ui, wi))
(1)
where ∆t is the IMU sample period, the state x, input u,
process noise w, and function f are defined as follows:
M ≜SO(3) × R16, dim(M) = 19
x ≜
GRT
I
GpT
I
GvT
I
bT
g
bT
a
GgT
τ
T ∈M
u ≜

ωT
m
aT
m
T , w ≜
h
nT
g
nT
a
nT
bg
nT
ba
nτ
iT
f(x, u, w) =


ωm −bg −ng
GvI + 1
2(GRI (am −ba −na) + Gg)∆t
GRI (am −ba −na) + Gg
nbg
nba
03×1
nτ


(2)
where
GRI,
GpI, and
GvI respectively denote the IMU
attitude, position, and velocity in the global frame, Gg is the
gravity vector in the global frame, τ is the inverse camera
exposure time relative to the first frame, nτ is the Gaussian
noise that models τ as a random walk, ωm and am are the
raw IMU measurements, ng and na are measurement noises
in ωm and am, ba and bg are IMU bias, which are modeled
as random walk driven by Gaussian noise nbg and nba,
respectively.

## Page 6

6
Algorithm 1: Sequential State Update
1 Scan recombination to synchronize LiDAR and image
data at the camera rate;
2 Forward propagation to obtain state prediction bx and
its covariance bP;
3 Backward propagation for LiDAR points motion
compensation;
4 // Point-to-plane LiDAR update
5 κ = −1, bxκ=0 = bx;
6 repeat
7
κ = κ + 1;
8
Compute residual zκ
l and Jacobin Hκ
l ;
9
Compute the state update bxκ+1;
10 until ∥bxκ+1 ⊟bxκ∥< ϵ;
11 bx = bxκ+1, bP = (I −KH) bP;
12 // Sparse direct visual update
13 level = −1;
14 repeat
15
κ = −1, bxκ=0 = bx;
16
level = level + 1;
17
repeat
18
κ = κ + 1;
19
Compute residual zκ
c and Jacobin Hκ
c ;
20
Compute the state update bxκ+1;
21
until ∥bxκ+1 ⊟bxκ∥< ϵ;
22
bx = bxκ+1;
23 until level >= 2;
24 ¯x = bxκ+1; ¯P = (I −KH) bP.
B. Scan Recombination
We employ the scan recombination to segment the high-
frequency, sequentially-sampled LiDAR raw points into dis-
tinct LiDAR scans at the camera sampling moments, as
depicted in Fig. 3. This ensures both camera and LiDAR data
are synchronized at the same frequency (e.g., 10 Hz), allowing
for update of state at the same time.
C. Propagation
In the ESIKF framework, the state and covariance are
propagated from time tk−1, when the last LiDAR scan and
image frame are received, to time tk, when the current LiDAR
scan and image frame are received. This forward propagation
predicts the state at each IMU input ui during tk−1 and tk,
by setting the process noise wi in (1) to zero. Denote the
propagated state as bx and covariance as bP, which will serve as
a prior distribution for the subsequent update in Section IV-D.
Moreover, to compensate for motion distortion, we conduct a
backward propagation as in [42], ensuring points in a LiDAR
scan are “measured” at the scan-end time tk. Note that for
notation simplification, we omit the subscript k in all state
vectors.
D. Sequential Update
The IMU propagated state bx and covariance bP impose a
prior distribution for x, the system state at time tk, as follows:
x ⊟bx ∼N(0, bP)
(3)
We denote the above prior distribution as p(x) and the
measurement models for the LiDAR and camera as:
yl
yc

=
hl(x, vl)
hc(x, vc)

(4)
where vl ∼N(0, Σvl) and vc ∼N(0, Σvc) respectively
denote the measurement noises for the LiDAR and camera.
A standard ESIKF [43] would update the state x using
all the current measurements, including both LiDAR mea-
surement yl and image measurements yc. However, LiDAR
and image measurements are two different sensing modalities,
whose data dimensions do not match. Furthermore, the fusion
of image measurement may be performed at various levels of
the image pyramid. To address the dimension mismatch and
give more flexibility for each module, we propose a sequential
update strategy. This strategy is theoretically equivalent to the
standard update using all measurements, assuming statistical
independence of LiDAR measurements yl and image measure-
ments yc given the state vector x (i.e., measurements corrupted
by statistically independent noise).
To introduce the sequential update, we rewrite the total
conditional distribution for the current state x as:
p(x|yl, yc) ∝p(x, yl, yc) = p(yc |x, yl)p(x, yl)
= p(yc |x) p(yl |x)p(x)
|
{z
}
∝p(x|yl)
(5)
Equation (5) implies that the total conditional distribution
p(x | yl, yc) can be obtained by two sequential Bayesian
updates. The first step fuses only the LiDAR measurement
yl with the IMU-propagated prior distribution p(x) to obtain
the distribution p(x|yl):
p(x|yl) ∝p(yl |x)p(x)
(6)
The second step then fuses the camera measurement yc with
p(x|yl) to obtain the final posterior distribution of x:
p(x|yl, yc) ∝p(yc |x)p(x|yl)
(7)
Interestingly, the two fusion in (6) and (7) follow the same
form:
q(x|y) ∝q(y|x)q(x)
(8)
To conduct the fusion in (8) for either LiDAR or image
measurements, we detail the prior distribution q(x) and mea-
surement model q(y|x) as follows. For the prior distribution
q(x), denote it as x = bx⊞δx with δx ∼N(0, bP). In case of
the LiDAR update (i.e., the first step), (bx, bP) is the state and
covariance obtained from the propagation step. In case of the
visual update (i.e., the second step), (bx, bP) is the converged
state and covariance obtained from the LiDAR update.
To obtain the measurement model distribution q(y | x),
denote state estimated at the κ-th iteration as bxκ, where
bx0 = bx. Approximating the measurement model (4) (either the
LiDAR or camera measurement) through its first-order Taylor
expansion made at bxκ leads to:
y|x ≃h(bxκ, 0)
|
{z
}
zκ
+Hκδxκ + Lκ v
(9)
q(y|x) ≃N(h(bxκ, 0) + Hκδxκ, R)
(10)

## Page 7

7
where δxκ = x ⊟bxκ, zκ is the residual, Lκ v ∼N(0, R) is
the lumped measurement noise, Hκ and Lκ are the Jacobian
matrixes of h(bxκ ⊞δxκ, v) with respect to δxκ and v,
evaluated at zero, respectively.
Then, substituting the prior distribution q(x) and the mea-
surement distribution q(y | x) in (10) into the posterior dis-
tribution (8) and performing maximum likelihood estimation
(MLE), we can obtain the maximum a-posterior estimation
(MAP) of δxκ (and hence xκ) from the standard update step
in the ESIKF framework [43]:
K =

(Hκ)T R−1Hκ + bP−1−1
(Hκ)T R−1,
bxκ+1 = bxκ⊞(−Kzκ −(I −KHκ) (bxκ⊟bx))
(11)
The converged state and covariance matrix then makes the
mean and covariance of the posterior distribution q(x|y).
Kalman filter with sequential update has been investigated
in the literature, such as in [44, 45]. This paper adopts
this approach for ESIKF for LiDAR and camera systems.
The implementation of the ESIKF with sequential update
is detailed in Algorithm 1. In the first step (Line 6-10),
the error state is updated from the LiDAR measurements
(Section VI-A) iteratively until convergence. The converged
state and covariance estimates, denoted again as bx and bP, are
used to update the geometry of the map (Section V-B), and
subsequently refined in the second step visual update (Line
13 - 23) on each level of the image pyramid (Section VII-B)
until convergence. The optimal state and covariance, denoted
as ¯x and ¯P, are employed for propagating incoming IMU
measurements (Section IV-C) and update the visual structures
of the map (Section V-D and V-E).
V. LOCAL MAPPING
A. Map Structure
Our map employs an adaptive voxel structure presented in
[14], which is organized by a Hash table and an octree for
each Hash entry (Fig. 2). The hash table manages root voxels,
each with a fixed dimension of 0.5 × 0.5 × 0.5 meters. Each
root voxel encapsulates an octree structure to further organize
leaf voxels of varying sizes. A leaf voxel represents a local
plane and stores a plane feature (i.e., plane center, normal
vector, and uncertainty) along with a set of LiDAR raw points
situated on this plane. Some of these points are attached with
three-level image patches (8 × 8 patch size), which we refer
to as visual map points. Converged visual map points are only
attached with reference patches, while non-converged ones are
attached with reference patches and other visible patches (see
Section V-E). The varying size of the leaf voxel allows it to
represent local planes of different scales, thus being adaptable
to environments with different structure [14].
To prevent the size of the map from going unbound, we
keep only a local map within a large local region of length
L around the LiDAR’s current position, as illustrated in a 2D
example in Fig. 4. Initially, the map is a cube centered at the
LiDAR’s starting position p0. The LiDAR’s detection area is
visualized as a sphere centered at its current position, with
its radius defined by the LiDAR’s detection range. When the
LiDAR moves to a new position p1 where the detection area
touches the boundaries of the map, we move the map away
from the boundaries by a distance d. As the map moves, the
memory containing the area moved out of the local map will
be reset to store new areas moved in the local map. This
ring-buffer approach ensures that our local map is maintained
within a fixed size of memory. The implementation of the ring-
buffer Hash map is detailed in [46]. The map move check is
performed after each ESIKF update step.
C
B
p0
r
L
p1
B
C
Memory
A
d
d
p0
r
r
A
(a) Initial map
(b) Move the map
(c) Reset the memory
Local voxel map
Fig. 4: 2D demonstration of local map slide. In (a), the grey
rectangle is the initial map region with length L. The red circle
is the initial detection area centered at p0. In (b), the detection
area moves to a new position p1 where the map boundaries
are touched. The map region is moved to a new position (blue
rectangle) by distance d. In (c), the memory space B remains
unchanged. The memory space A storing the green area is
reset for the blue area C in (b).
B. Geometry Construction and Update
The geometry of the map is constructed and updated from
LiDAR point measurements. Specifically, after the LiDAR
update in ESIKF (Section IV), we register all points from the
LiDAR scan to the global frame. For each registered LiDAR
point, we determine its located root voxel in the Hash map. If
the voxel does not exist, we initialize the voxel with the new
point and index it into the Hash map. If the determined voxel
already exists in the map, we append the point to the existing
voxel. After all points in a scan are distributed, we conduct
geometry construction and update as follows.
For newly-created voxels, we determine if all the contained
points lie on a plane based on the singular value decomposi-
tion. If so, we calculate the center point q = ¯p, plane normal
n, and the covariance matrix of (q, n), denoted as Σn,q, of
the plane. Σn,q is used to characterize the plane uncertainty,
which arises from both pose estimation uncertainty and the
point measurement noise. The detailed plane criteria and
calculation of the plane parameters and uncertainties can be
referred to our previous work [14]. If the contained points do
not lie on a plane, the voxel is continuously subdivided into
eight smaller octants until either the points in the sub-voxel
are determined to form a plane or the maximum layer (eg., 3)
is reached. In the latter case, the points in the leaf voxel will
be discarded. As a result, the map only contains voxels (either
root or sub) identified as planes.
For existing voxels that have new points appended, we
assess if the new points still form a plane with the existing
points in the root voxel or sub-voxel. If not, we conduct
voxel sub-division as above. If yes, we update the plane’s
parameters (q,n) and covariance Σn,q as above too. Once
the plane parameters converge (see [14]), the plane will be

## Page 8

8
considered as mature and new points on this plane will be
discarded. Moreover, mature planes will have their estimated
plane parameters (q,n) and covariance Σn,q fixed.
LiDAR points on planes (either in the root voxel or sub-
voxel) will be used for generating visual map points in the
subsequent section. For mature planes, 50 most recent LiDAR
points are candidates for visual map point generation, while
for unmature planes, all LiDAR points are the candidates. The
visual map point generation process will identify some of these
candidate points as visual map points and attach them with
image patches for image alignment.
C. Visual Map Point Generation and Update
To generate and update visual map points, we select the
candidate LiDAR points in the map that (1) are visible
from the current frame (detailed in Section VII-A), and (2)
exhibit significant gray-level gradients in the current image.
We project these candidate points, after the visual update
(Section IV-D), onto the current image and retain the candidate
point with the smallest depth for the local plane in each voxel.
Then, we divide the current image into uniform grid cells each
with 30 × 30 pixels. If a grid cell does not contain any visual
map point projected here, we generate a new visual map point
using the candidate point with the highest gray-level gradient
and associate it with the current image patch, estimated current
state (i.e., frame pose and exposure time), and the plane normal
calculated from the LiDAR points as in the previous section.
The patch attached to the visual map points has three layers of
the same size (e.g., 11×11 pixels), each layer is half sampled
from the previous layer, forming a patch pyramid. If a grid
cell contains visual map points projected here, we add new
patch (all three layers of pyramid) to the existing visual map
point if (1) more than 20 frames have passed since its last
patch addition, or (2) its pixel position in the current frame
deviates by more than 40 pixels from its position at the last
patch addition. As a result, the map points will likely have
effective patches with uniformly distributed viewing angles.
Along with the patch pyramid, we also attach the estimated
current state (i.e.,pose and exposure time to the map point.
D. Reference Patch Update
A visual map point could have more than one patch due to
the addition of new patches. We need to choose one reference
patch for image alignment in the visual update. In detail,
we score each patch f based on photometric similarity and
viewing angle as follows:
NCC(f, g) =
P
x,y[f(x, y) −¯f][g(x, y) −¯g]
qP
x,y[f(x, y) −¯f]2 P
x,y[g(x, y) −¯g]2
c = n · p
∥p∥,
ω1 =
1
1 + etr(Σn)
(12)
S = (1 −ω1) · 1
n
n
X
i=1
NCC(f, gi) + ω1 · c
where NCC(f, g) represents the Normalized Cross-Correlation
(NCC) used to measure the similarity between patch f and g
at the 0-th pyramid level (the level with the highest resolution)
of both patch, with mean subtraction applied to both patches,
c denotes the cosine similarity between the normal vector
n and view direction p/∥p∥of patch f under evaluation.
When the patch is directly facing the plane where the map
point is located, the value of c is 1. The overall score S is
calculated by summing the weighted NCC and c, where the
former represents the average similarity between the patch f
under evaluation and all other patches gi and tr(Σn) represents
the trace of the covariance matrix of the normal vector.
Among all the patches attached to a visual map point,
the one with the highest score is updated as the reference
patch. The above scoring mechanism tends to choose reference
patches whose (1) appearance is similar (in terms of NCC) to
most of the rest of the patches, a technique used by MVS
[47] to avoid patches on dynamic objects; (2) view direction
is orthogonal to the plane, thereby maintaining texture details
at a high resolution. In contrast, the reference patches update
strategy in our previous work FAST-LIVO [8] and prior arts [4]
directly select the patch with the smallest view direction dif-
ference from the current frame, causing the selected reference
patch to be very close to the current frame, hence imposing
weak constraints on the current pose update.
Fig. 5: (a) Affine warping between reference patches and target
patches. (b) Any normal Irn ∈S2 lying on the normalized
sphere is first projected into a point M ∈R3 on the plane
Irp
T M = 1, and then projected to a point m ∈R2 on the
x-y plane. This transformation thereby converts a perturbation
δn on the sphere into a perturbation δm in x-y plane.
E. Normal Refine
Each visual map point is assumed to lie on a small local
plane. Existing works [2, 4, 8] assumed that all pixels in a
patch have the same depth, a wild assumption that does not
hold in general. We use plane parameters computed from the
LiDAR points as detailed in Section V-B to achieve greater
accuracy. This plane normal is crucial for performing affine
warping for image alignment in the visual update process. To
further enhance the accuracy of the affine warping, the plane
normal could be further refined from the patches attached to
the visual map point. Specifically, we refine the plane normal
in the reference patch by minimizing the photometric error
with respect to the other patches attached to the visual map
point.
1) Affine warping: Affine warping is used to transform
patch pixels from the reference frame (i.e., the source patch)
to patch pixels in the rest of the frames (i.e., the target patch),
illustrated in Fig. 5(a). Let uj
r be the j-th pixel coordinates
in the source patch and uj
i be the j-th pixel coordinates in

## Page 9

9
the i-th target patch. Assuming all pixels in the patch lie in
a local plane with normal Irn and visual map point position
Irp (which corresponds to the center pixel for both source and
target patches), both represented in the source patch frame, we
have:
uj
i = Ai
ruj
r
Ai
r = P(IiRIr + IitIr
1
IrnT · Irp
IrnT )P−1
(13)
where Ai
r represents the affine warping matrix that transforms
the pixel coordinates from the source (or reference) patch
to the i-th target patch, IiRIr and IitIr denote the relative
pose of the reference frame Ir w.r.t. the target frame Ii.
To use fisheye images directly without rectifying them to
pinhole images, we implement projection matrix P and back
projection matrix P−1 based on different camera models (e.g.,
P is the camera intrinsic matrix for the pinhole camera model).
2) Normal Optimization: To refine the plane normal Irn,
we minimize photometric errors between the reference patch
and other image patches at the 0-th pyramid level (i.e., the
highest-resolution level):
Irn∗= arg min
Ir n∈S2
X
i∈S
N2
X
j=1
τiIi(Ai
ruj
r) −τrIr(uj
r)

2
(14)
where N is the path size, τr and τi are the inverse exposure
times of the reference frame and the i-th target frame, respec-
tively. Ir(uj
r) denote j-th patch pixel in the reference frame,
Ii(Ai
ruj
r) denotes the j-th path pixel in the i-th target frame,
and S is the set of all target frames.
3) Optimization Variable Transformation: To enhance the
computational efficiency, we reparameterize the least squares
problem in (14). Note that the optimization variable
Irn
only appeared in M ≜
1
IrnT · Irp
Irn ∈R3 in (13), the
optimization over Irn can be conducted over M. Moreover,
the vector M is subject to constraint Irp · M = 1, meaning
that M can be parameterized as follows:
M =


Mx
My
1
Irpz
−
Irpx
Irpz
Mx −
Irpy
Irpz
My

= Bm + b
B =


1
0
0
1
−
Irpx
Irpz
−
Irpy
Irpz

, b =


0
0
1
Irpz

, m =
Mx
My

∈R2
(15)
where Irpz ̸= 0 since no such reference patch could be chosen
for the visual map point. The relation among Irn, M, and m
are shown in Fig. 5 (b).
Finally, the optimization in (14) is conducted over the vector
m ∈R2 without any constraints. This optimization can be
performed in a separate thread to avoid blocking the main
odometry thread. The optimized parameter m∗can then be
used to recover the optimal normal vector Irn∗:
Irn∗=
M∗
∥M∗∥, M∗= Bm∗+ b
(16)
Once the plane normal converges, the reference patch and
normal vector for this visual map point are fixed without
further refinement, and all other patches are deleted.
VI. LIDAR MEASUREMENT MODEL
This section details the LiDAR measurement model yl =
hl(x, vl) used in the LiDAR update of ESIKF in Section IV-D.
A. Point-to-plane LiDAR Measurement Model
After obtaining the undistorted points {Lpj} in a scan, we
project them to the global frame using the estimated state bxκ
at the κ-th iteration of LiDAR update:
Gbpκ
j = G bTκ
I
ITL
Lpj
(17)
We then identify the root or sub voxel where Gbpκ
j lies in the
Hash map. If no voxel is found or the voxel does not contain
a plane, the point is discarded. Otherwise, we use the plane in
the voxel to establish a measurement equation for the LiDAR
point. Specifically, we assume the true LiDAR point Lpgt
j ,
given the accurate LiDAR pose GTI, should lie on the plane
with normal ngt
j and center point qgt
j in the voxel. i.e.,
0 = (ngt
j )T (GTI
ITL
Lpgt
j −qgt
j )
(18)
Since the ground-true point Lpgt
j
is measured as Lpj with
ranging and bearing noises δLpj, we have Lpgt
j
= Lpj −
δLpj. Likewise, the plane parameters (ngt
j , qgt
j ) are estimated
as (nj, qj) with covariance Σn,q (Section V-B), so we have:
ngt
j = nj ⊟δnj, qgt
j = qj −δqj. Therefore,
0
|{z}
yl
= (nj ⊟δnj)T (GTI
ITL(Lpj −δLpj) −(qj −δqj))
|
{z
}
hl(x,vl)
(19)
where the measurement noise vl = (δLpj, δnj, δqj) consist-
ing of the noise associated with the LiDAR point, the normal
vector, and the plane center respectively.
B. LiDAR Measurement Noise with Beam Divergence
The uncertainty of a LiDAR point δLpj in the local
LiDAR frame is decomposed into two components in [14],
the ranging uncertainty δd caused by laser time of flight
(TOF), and the bearing direction uncertainty δω originated
from encoders. Besides these uncertainties, we also consider
uncertainties caused by the laser beam divergence angle θ,
as illustrated in Fig. 6. As the angle φ between the bearing
direction and normal vector increases, the ranging uncertainty
of the LiDAR point increases significantly, while the bearing
direction uncertainty remains unaffected. The δd due to the
laser beam divergence angle can be modeled as:
δd = L2 −L1 = d

cos φ
cos(θ + φ) −
cos φ
cos(θ −φ)

(20)
Considering δd influenced by TOF and laser beam divergence,
when our system selects more points from the ground or walls
(see Fig. 6 (c, d)), it achieves a more precise pose estimation
than that not considering such effect.

## Page 10

10
Fig. 6:
(a) and (b) respectively illustrate the 3D and side
cross-sectional views of the LiDAR point uncertainty model
considering the laser beam divergence angle θ. The red contour
outlines the area that a laser beam spreads. (c) and (d) color the
points in a scan by the point location uncertainty. Compared
to (c), (d) further takes into account the ranging uncertainty
δd resulting from the beam divergence angle. This leads to a
higher uncertainty for ground points due to the large spread
area of laser beams.
X
Y
Z
dmin
dmax
World Frame
Sampled points
Sampled pixels
Occupied image grids
Voxel with visual map points
Unselected Voxel
Voxel with LiDAR
but without visual points
points
Fig. 7: The illustration of on-demand voxel raycasting.
VII. VISUAL MEASUREMENT MODEL
This section details the visual measurement model yc =
hc(x, vc) used in the visual update of ESIKF in Section IV-D.
A. Visual Map Point Selection
To perform sparse image alignment in the visual update,
we begin by selecting appropriate visual map points. We
first extract the set of map points (termed as visual submap)
that is visible in the current camera FoV, using voxel and
raycasting queries. Then, the visual map points from this
submap are selected and outliers are rejected. This process
yields a refined set of visual map points ready for constructing
visual photometric errors in the visual measurement model.
1) Visible Voxel Query: Identifying map voxels within the
current frame FoV is challenging due to the large number
of voxels in the map. To address this issue, we poll the
Visual map points
Current LiDAR scan points
Occluded visual map points
Depth discontinuous visual 
map points
(a)
(b)
Surface
Camera
Fig. 8: Outlier rejection. (a) shows the diagrammatic drawing
of occluded and depth-discontinuous visual map points. (b)
shows the effect of outlier rejection in real scenes. The red
dots are the rejected visual map points, and the green dots are
the accepted visual map points.
voxels hit by LiDAR points in the current scan. This can
be done efficiently by inquiring the voxel Hash table using
the measured point position. If the camera FoV is largely
overlapped with the LiDAR FoV, map points in the camera
FoV likely lie in these voxels as well. We also poll voxels
hit by map points identified visible (through the same voxel
query and raycasting) in the previous image frame, assuming
that two consecutive image frames have large FoV overlaps.
Finally, the current visual submap can be obtained as map
points contained in these two types of voxels followed by a
FoV check.
2) Raycasting on Demand:
In most cases, the visual
submap can be obtained through the voxel queries above.
However, a LiDAR sensor could return no points when it is
too close to an object (known as the close proximity blind
zones). Also, the camera FoV may not be completely covered
by the LiDAR FoV. To recall more visual map points in these
cases, we employ a raycasting strategy as illustrated in Fig.
7. We divide the image into uniform grid cells, each with
30 × 30 pixels, and project the visual map points obtained
from the voxel query onto the grid cells. For each image grid
cell that is not occupied by these visual map points, a ray is
cast backward along the central pixel, where sample points
are uniformly distributed along the ray in the depth direction
from dmin to dmax. In order to reduce computation load, the
positions of sample points on each ray in the camera body
frame are pre-computed. For each sampled point, we evaluate
the corresponding voxel’s status: if the voxel contains map
points that lie in this grid cell after projection, we incorporate
these map points into the visual submap and cease for this ray.
Otherwise, we continue to the next sample point on the ray
until reaching the maximum depth dmax. After processing all
the unoccupied image grid cells through raycasting, we obtain
a set of visual map points that distribute among the whole
image.
3) Outlier Rejection: After voxel query and raycasting,
we obtain all visual map points in the current frame FoV.
However, these visual map points could be occluded in the
current frame, have discontinuous depth, have their reference
patch taken at large view angles, or have large view angles
in the current frame, all of which can severely degrade image
alignment accuracy. To address the first issue, we project all

## Page 11

11
the visual map points in the submap into the current frame
using the pose after the LiDAR update and keep the lowest-
depth points in each grid cell of 30 × 30 pixels. To address
the second issue, we project the LiDAR points in the current
LiDAR scan to the current frame producing a depth map. By
comparing the depth of visual map points with their 9 × 9
neighbor in the depth map, we determine their occlusion and
depth variation. Occluded and depth-discontinuous map points
are rejected (see Fig. 8). To address the third and fourth issue,
we remove points where the view angle (i.e., the angle between
normal vector and direction from the visual map point to the
patch optical center) of the reference patch or current patch
is too large (e.g. over 80°). The remaining visual map points
will be used to align the current image.
B. Sparse-Direct Visual Measurement Model
The visual map points {Gpi} extracted above are used
to construct the visual measurement model. The underlying
principle is that, when transforming the map point Gpi to
the current image Ik(·) with the ground-truth state (i.e., pose)
xk, the photometric error between the reference patch and the
current patch should be zero:
0 = τkIgt
k (π(CTI(GTI)−1Gpi)
|
{z
}
ui
+∆u)
−τrIgt
r (π(CrTG
Gpi)
|
{z
}
u′
i
+Ar
i ∆u)
(21)
where π(·) is the common camera projection model (i.e.,
Pinhole, MEI, ATAN, Scaramuzza, Equidistant), CrTG is the
pose of the global frame G w.r.t. reference frame Cr, which
has been estimated when receiving and fusing the reference
frame, Ar
i is the affine warping matrix that transforms pixels
from the i-th current patch to the reference patch, ∆u is
the relative pixel position to the center ui within the current
patch, Igt
k , Igt
r
denote the ground-true pixel values of the
reference and current frames, respectively. They are measured
as the actual image pixel values Ik, Ir with measurement noise
vc = (δIk, δIr), which originate from various sources (e.g.,
shot noise and the Analog-to-Digital Converter (ADC) noise
of the camera CMOS). Hence,
0
|{z}
yc
= τk(Ik(ui+∆u)−δIk)−τr(Ir(u′
i+Ar
i ∆u)−δIr)
|
{z
}
hc(x,vc)
(22)
To enhance computational efficiency, we employ an inverse
compositional formulation [4, 48], where the pose incremental
δT ∈R6 parameterizing GTI =G bTκ
I Exp(δT) in ui (see
(21)), is moved from ui to u′
i as follows:
ui = π(CTI(G bTκ
I )−1Gpi)
u′
i = π(CrTG Exp(δT)Gpi)
(23)
Given that u′
i in the reference frame remains unchanged during
each iteration, we only require a one-time computation of the
Jacobian matrices w.r.t. δT, rather than re-calculating them
for every iteration.
To estimate the inverse exposure time τk from the mea-
surement equation (22), we fix the initial inverse exposure
time τ0 = 1 to eliminate the degeneration of equation (22)
when all inverse exposure time are zeros. The estimated
inverse exposure times of subsequent frames are therefore the
exposure time relative to the first frame.
The equation (22) is used in the visual update step across
three levels (see Algorithm 1); the visual update starts from
the coarsest level, after the convergence of a level, it proceeds
to the next finer level. The estimated state is then used to
generate visual map points (Section V-C) and update reference
patch (Section V-D).
VIII. DATASETS FOR EVALUATION
In this section, we introduce datasets for performance eval-
uation, including public datasets NTU-VIRAL [49], Hilti’22
[50], Hilti’23 [51], and MARS-LVIG [52], as well as our self-
collected FAST-LIVO2 private dataset. Specifically, the NTU-
VIRAL and Hilti datasets are used to conduct a quantitative
benchmark comparison of our system against other state-of-
the-art (SOTA) SLAM systems (Section IX-B). The FAST-
LIVO2 private dataset is primarily used to evaluate our system
across various extremely challenging scenarios (Section IX-C),
to demonstrate its capability for high-precision mapping (Sec-
tion IX-D), and to validate the functionality of the individual
modules within our system (Sections I-A through I-D in the
Supplementary Material [53]). MARS-LVIG dataset is em-
ployed for application demonstrations (Section X) and ablation
study (Section I-E in the Supplementary Material [53]).
A. NTU-VIRAL, Hilti and MARS-LVIG Dataset
The NTU-VIRAL dataset, collected at the Nanyang Techno-
logical University campus using an aerial platform, presents
diverse scenarios embodying unique aerial operational chal-
lenges. Specifically, the “sbs” sequences can only provide
noisy visual features from distant objects. The “nya” sequences
present challenges to LiDAR SLAM due to semi-transparent
surfaces and to visual SLAM owing to intricate flight dynamics
and low lighting conditions. The dataset is equipped with a
16-channel OS1 gen13 LiDAR sampled at 10 Hz and with a
built-in IMU at 100 Hz, and two synchronized pinhole cameras
triggered at 10 Hz. The left camera is used for evaluation.
The Hilti’22 and Hilti’23 datasets, collected by handheld
and robot devices, encompass indoor and outdoor sequences
from environments like construction sites, offices, labs and
parking areas. These sequences introduce numerous challenges
from long corridors, basements, and stairs, with textureless
features, varying illumination conditions, and insufficient Li-
DAR plane constraints. Handheld sequences use a Hesai
PandarXT-324 LiDAR at 10 Hz, five wide-angle cameras at 40
Hz, which is downsampled into 10 Hz, and an external Bosch
BMI085 IMU at 400 Hz. Meanwhile, the robot-mounted
sequences feature a Robosense BPearl5 LiDAR at 10 Hz, eight
omnidirectional cameras at 10 Hz, and an Xsens MTi-670
IMU at 200 Hz. In both cases, the front-facing camera is used
3https://ouster.com/products/os1-lidar-sensor
4https://www.hesaitech.com/product/xt32/
5https://www.robosense.ai/en/rslidar/RS-Bpearl

## Page 12

12
for all systems under evaluation. Millimeter-accurate ground
truth, obtained through a motion capture system (MoCap) or a
Total Station [54], is provided for each sequence. Note that the
ground truth of the Hilti datasets is not open-source; therefore,
algorithmic results on these datasets are evaluated via the Hilti
official website. Since “Site 3” in Hilti’23 does not provide
in-depth analysis plots (e.g., RMSE), we exclude these four
sequences, but our scoring results for these sequences can still
be found on their official website6. NTU-VIRAL and Hilti
contribute a total of 25 sequences.
The MARS-LVIG dataset provides high-altitude, ground-
facing mapping data that encompasses diverse unstructured
terrains such as jungles, mountains, and islands. The dataset
was collected via a DJI M300 RTK quadrotor, which is
equipped with a Livox Avia7 LiDAR (with built-in BMI088
IMU) and a high-resolution global-shutter camera, both trig-
gered at 10 Hz. This is notably distinct from the aforemen-
tioned NTU-VIRAL and Hilti datasets, which use 752 × 480
grayscale images, while the MARS dataset employs 2448 ×
2048 RGB images, thereby facilitating the generation of
clear, dense colored point clouds. Therefore, we leverage this
public dataset to validate our capabilities in high-altitude aerial
mapping applications.
Build-in IMU
LiDAR
Camera
Battery
STM32
On-board 
PC
(a)
Sychn 
Timers
Pulse signal 1
STM32
1 Hz
10 Hz
USB 
Serial
Synthetic 
GPRMC
On-board PC
10 Hz Point Cloud 
and RGB image
(b)
Livox Avia
Camera
Pulse signal 2
Fig. 9: Our platform with hardware synchronization for data
acquisition. (a) our handheld platform, (b) the hardware syn-
chronization scheme.
B. FAST-LIVO2 Private Dataset
To validate the system’s performance under more extreme
conditions (e.g., LiDAR degeneration, low illumination, dras-
tic exposure changes, and cases of no LiDAR measurements),
we make a new dataset named FAST-LIVO2 private dataset.
The dataset, hardware device, and hardware synchronization
scheme are released with the codes of this work to facilitate
the reproduction of our work.
1) Platform: Our data collection platform, illustrated in
Fig. 9, is equipped with an industrial camera (MV-CA013-
21UC), a Livox Avia LiDAR, and a DJI manifold-2c (Intel i7-
8550u CPU and 8 GB RAM) as onboard computers. The cam-
era FoV is 70.6◦×68.5◦and the LiDAR FoV is 70.4◦×77.2◦.
All sensors are hard synchronized with a 10 Hz trigger signal,
generated by STM32 synchronized timers.
2) Sequence Description: As summarized in Table S1 in
the Supplementary Material [53], FAST-LIVO2 private dataset
comprises 20 sequences across various scenes (e.g., campus
6https://hilti-challenge.com/leader-board-2022.html, https://hilti-challenge.
com/leader-board-2023.html
7https://www.livoxtech.com/avia
buildings, corridors, basements, mining tunnel, etc.) charac-
terized by structure-less, cluttered, dim, variable-lighting, and
weakly textured environments, with a total duration of 66.9
min. Most sequences exhibit visual and/or LiDAR degenera-
tion, such as facing a single and/or texture-less plane, travers-
ing an extremely narrow and/or dark tunnel, and experiencing
varying light conditions from indoor to outdoor (see Fig. S7
in the Supplementary Material [53]). To guarantee enhanced
synchronous data collection between the camera and LiDAR,
we configure the camera with fixed exposure time but auto-
gain mode in most scenarios. For the remaining sequences with
auto-exposure, we record their ground truth exposure times. In
all sequences, the platform returns to the starting point, which
enables the drift evaluation.
IX. EXPERIMENT RESULTS
In this section, we conduct extensive experiments to evaluate
our proposed system.
A. Implementation and System Configurations
We implemented the proposed FAST-LIVO2 system in
C++ and Robots Operating System (ROS). In the default
configuration, the exposure time estimation is enabled, while
normal vector refinement is turned off. LiDAR points in a scan
are downsampled temporally at a 1:3 ratio. The root voxel size
for the voxel map is set at 0.5 m, and the maximum layer of
the internal octree is 3. The image patch size is 8 × 8 for
image alignment and 11 × 11 for normal refinement. Within
the sequential ESIKF settings, for all the experiments, the
camera photometric noise is set to a constant value of 100.
The LiDAR depth error and bearing angle error are adjusted
to 0.02 m and 0.05° for Livox Avia LiDAR and OS1-16,
0.001 m and 0.001° for PandarXT-32, 0.008 m and 0.01° for
Robosense BPearl LiDAR. The laser beam divergence angle
is set at 0.15° for Livox Avia LiDAR and OS1-16, and at
0.001° for the PandarXT-32 and Robosense BPearl LiDAR.
Our system uses the same parameters in all sequences of all
datasets with the same sensor setup. The computation platform
for all experiments is a desktop PC equipped with an Intel i7-
10700K CPU and 32 GB RAM. For FAST-LIVO2, we also test
it on an ARM processor that is commonly used in embedded
systems with reduced power and cost. The ARM platform is
RB58. with a Qualcomm Kryo585 CPU and 8 GB RAM. We
refer to the implementation of FAST-LIVO2 on the ARM-
based platform as “FAST-LIVO2 (ARM)”.
B. Benchmark Experiments
In this experiment, we conduct quantitative evaluations on
25 sequences from the NTU-VIRAL, Hilti’22, and 23 open
datasets. Our approach is benchmarked against several state-
of-the-art open-source odometry systems, including R3LIVE
[36], a dense direct LiDAR-inertial-visual odometry system;
FAST-LIO2 [13], a direct LiDAR-inertial odometry system;
8https://www.adlinktech.com/Products/Computer on Modules/SMARC/
LEC-RB5?lang=en

## Page 13

13
TABLE II: Absolute translational errors (RMSE, meters) in sequences
Dataset
Sequence
SDV-
LOAM
Our
LIO
FAST-
LIO2
R3LIVE
LVI-
SAM
FAST-
LIVO
Ours
(w/o expo)
Ours
(w normal)
Ours
(w/o update)
Ours
Hilti’22
Construction Ground
25.121
0.011
0.013
0.021
×
0.022
0.011
0.008
0.015
0.010
Construction Multilevel
12.561
0.031
0.044
0.024
×
0.052
0.021
0.018
0.025
0.020
Construction Stairs
9.212
0.221
0.320
0.784
9.142
0.241
0.049
0.027
0.151
0.016
Long Corridor
19.531
0.061
0.064
0.061
6.312
0.065
0.069
0.059
0.071
0.067
Cupola
9.321
0.221
0.250
2.142
×
0.182
0.161
0.122
0.179
0.121
Lower Gallery
11.232
0.014
0.024
0.008
2.281
0.022
0.010
0.008
0.010
0.007
Attic to Upper Gallery
4.551
0.223
0.720
2.412
×
0.621
0.101
0.077
0.221
0.069
Outside Building
2.622
0.030
0.028
0.029
0.952
0.052
0.042
0.033
0.050
0.035
Hilti’23
Floor 0
4.621
0.028
0.031
0.018
×
0.021
0.025
0.023
0.023
0.022
Floor 1
7.951
0.025
0.031
0.024
8.682
0.022
0.024
0.022
0.031
0.023
Floor 2
7.912
0.041
0.083
0.046
×
0.048
0.023
0.021
0.051
0.022
Basement
6.151
0.021
0.038
0.024
×
0.035
0.020
0.018
0.018
0.016
Stairs
9.032
0.110
0.170
0.110
3.584
0.152
0.025
0.020
0.132
0.018
Parking 3x floors down
19.952
0.162
0.320
0.462
×
0.356
0.035
0.022
0.112
0.032
Large room
16.781
0.121
0.028
0.035
0.563
0.031
0.033
0.027
0.118
0.026
Large room (dark)
15.012
0.051
0.040
0.059
×
0.053
0.049
0.051
0.058
0.046
NTU VIRAL
eee 01
0.301
0.122
0.212
0.072
3.901
0.191
0.069
0.066
0.109
0.068
eee 02
1.842
0.131
0.172
0.059
0.182
0.132
0.051
0.055
0.112
0.051
eee 03
0.301
0.124
0.213
0.078
0.287
0.192
0.068
0.070
0.099
0.068
nya 01
0.202
0.084
0.141
0.080
0.205
0.121
0.075
0.078
0.106
0.073
nya 02
0.214
0.153
0.212
0.084
1.296
0.182
0.076
0.081
0.118
0.075
nya 03
0.251
0.082
0.133
0.079
0.176
0.112
0.060
0.060
0.092
0.059
sbs 01
0.212
0.112
0.184
0.075
0.254
0.253
0.064
0.063
0.098
0.062
sbs 02
0.233
0.123
0.161
0.076
0.221
0.134
0.062
0.048
0.116
0.061
sbs 03
0.281
0.122
0.142
0.070
0.309
0.132
0.061
0.047
0.119
0.060
Average
7.416
0.097
0.151
0.278
1.928
0.137
0.051
0.044
0.089
0.045
× denotes the system totally failed.
SDV-LOAM [40], a semi-direct LiDAR-visual odometry sys-
tem; LVI-SAM [35], a feature-based LiDAR-inertial-visual
SLAM system; and our previous work FAST-LIVO [8].
These systems are downloaded from their respective GitHub
repositories. For FAST-LIO2, FAST-LIVO, and LVI-SAM, we
use the recommended settings for indoor and outdoor scenes
equipped with multi-line LiDAR sensors. For R3LIVE, we
adapt the system to work with fisheye camera models and
multi-line LiDARs equipped with external IMUs (the default
configuration only supports internal IMUs). We disable the
real-time optimization of the camera intrinsic and the extrinsic
CTI due to adverse optimization caused by insufficient IMU
excitation in the datasets. Other parameters, including the
window size and pyramid level for optical flow tracking, the
resolution for downsampling the point cloud of the current
scan and the global map, are fine-tuned to achieve optimal
performance. Since only the vision module of SDV-LOAM
is open-sourced, we integrate it with LeGO-LOAM [7] in a
loosely coupled manner, following the methodology described
in the original paper [40]. This enhanced system continues
to refine poses obtained from the vision module and we also
open this implementation on GitHub9. Given that all compared
systems are odometry without loop closure, except for LVI-
SAM, we remove the loop-closure module of LVI-SAM to
ensure a fair comparison. Additionally, we conduct an ablation
study on the exposure time estimation module, the normal
refine module, and the reference patch update strategy. The
default FAST-LIVO2 has real-time exposure estimation and
reference patch update, but no normal refinement.
9https://github.com/xuankuzcr/SDV-LOAM reimplementation
The results of all methods are shown in Table II. It is seen
that our method achieves the highest overall accuracy across
all sequences with an average RMSE of 0.044 m, which is
three times more accurate than the second-place FAST-LIVO
at 0.137 m. Our system delivers the best results in most
sequences, except for ”Outside Building” and ”Large Room
(dark)”, where our system exhibits a slightly (millimeter-level)
higher error compared to the LiDAR-inertial only odometry
FAST-LIO2. This discrepancy can be attributed to the rich
structural features but poor lighting conditions of these se-
quences, resulting in dim and blurred images. Consequently,
fusing these low-quality images does not enhance odome-
try accuracy. Excluding these two sequences, our method,
which leverages tightly-coupled LiDAR, inertial, and visual
information, outperforms FAST-LIO2, our LIO subsystem,
and the LiDAR-visual only odometry, SDV-LOAM, signifi-
cantly. Notably, SDV-LOAM performs particularly poorly on
the Hilti datasets due to its lack of tight integration with
IMU measurements, leading to drift in the LO subsystem.
Additionally, the loose coupling between LiDAR and visual
observations, along with poor initial values for VO, often
results in local optima or even negative optimization. Our
LIO subsystem generally surpasses FAST-LIO2 due to our
more accurate noise modeling for each LiDAR point. In a
few sequences where FAST-LIO2 outperforms slightly, the
differences are minimal, at the millimeter level, and negligible.
Moreover, our system’s accuracy significantly exceeds that of
other tightly coupled LiDAR-inertial-visual systems across all
sequences. Among them, LVI-SAM fails in nine sequences
primarily due to its feature-based LIO and VIO subsystems

## Page 14

14
not fully utilizing raw measurements, which degrades its
robustness in environments with subtle geometric or texture
features. R3LIVE generally performs well, but struggles in
“Construction Stairs”, “Cupola”, and “Attic to Upper Gallery”
sequences, where its performance is even worse than FAST-
LIO2. This is because intense rotations at structure-less stair-
cases result in inadequate pose priors, causing local optima
when aligning colored map points with the current frame, and
ultimately leading to negative optimization. FAST-LIVO and
FAST-LIVO2 overcome such challenges in these sequences
by the patch-based image alignments. Additionally, situations
where the sensors are close to walls in these sequences high-
light the effectiveness of raycasting in FAST-LIVO2, with the
mapping results in these large-scale scenes shown in Fig. S8
in the Supplementary Material [53]. On the other hand, FAST-
LIVO is outperformed by R3LIVE and FAST-LIVO2 on the
NTU-VIRAL dataset, especially in unstructured scenes like
“nya” sequences, where the effects of affine warping based
on constant depth assumptions are inaccurate. In contrast,
the pixel-level alignment of R3LIVE and the plane prior (or
refinement) of FAST-LIVO2 do not encounter such issues.
Comparing the different variants of FAST-LIVO2, we ob-
serve that the average accuracy without real-time exposure
time estimation decreases by 6 mm compared to the default,
as the exposure time estimation can actively compensate
illumination changes in the environment. On the other hand,
the average accuracy without the reference patch update de-
creases by 44 mm compared to the default, as the reference
patch update strategy effectively selects patches with higher
resolution and avoids selecting outlier patches. Finally, the
normal refinement increases the average accuracy by 1 mm,
and the accuracy improvement is not consistent in all se-
quences. The limited improvement is mainly because normal
vector refinement yields positive optimization only in simple
structured scenes with nice image observations. In the NTU-
VIRAL dataset, images from the “eee” and “nya” sequences
are extremely dim and blurry, where negative optimization
is particularly severe. To further study the effectiveness of
the different modules, including exposure time estimation,
affine warping, reference patch update, normal convergence,
on-demand raycasting, and ESIKF sequential update, we con-
ducted a thorough study on our private dataset and MARS-
LVIG dataset. The results are presented in Section I (System
Module Validation) in the Supplementary Material [53] due to
the space limit. As confirmed in the results, our system can
achieve robust and accurate pose estimation in both structured
and unstructured environments, under severe light variations,
in remarkably large-scale scenarios with long-term, high-speed
data collection, and even in extremely narrow spaces with few
LiDAR measurements.
C. LiDAR Degenerated and Visually Challenging Environ-
ments
In this experiment, we evaluate the robustness of our system
under environments experiencing LiDAR degeneration and/or
visual challenges, comparing it with the qualitative mapping
results of FAST-LIVO and R3LIVE in 8 sequences as shown
in Fig. 10 and 11. Fig. 10 showcases LiDAR degeneration
sequences where the LiDAR is facing a big wall while moving
along the wall from one side to the other. Due to the absence
of geometrical constraints since only one wall plane is being
observed by the LiDAR, LIO methods would fail. It’s worth
mentioning that the “HIT Graffiti Wall” sequence spans nearly
800 meters with LiDAR continuously facing the wall, leading
to considerable degeneration. In all sequences, FAST-LIVO2
distinctly showcases its robustness against even long-term
degeneration and its capability to deliver high-precision col-
ored point maps. In contrast, FAST-LIVO managed to obtain
the geometric structure but with completely blurred texture.
R3LIVE struggles with both geometric structure and texture
clarity. Fig. 11 showcases tests in more complicated scenarios
where LiDAR and/or camera both degenerate occasionally.
The degeneration directions are indicated by respective arrows.
“HKU Cultural Center” (Fig. 11 (a)) showcases the mapping
results of FAST-LIVO2, R3LIVE, and FAST-LIVO. As can
be seen, R3LIVE and FAST-LIVO have distorted point maps,
blurred textures, and drifts exceeding 1 m. In contrast, FAST-
LIVO2 successfully returns to the starting point, achieving an
impressive end-to-end error of less than 0.01 m, while achiev-
ing a consistent point map with clear textures. “CBD Building
03” (Fig. 11 (b)) and “Mining Tunnel” (Fig. 11 (c)) display
only FAST-LIVO2 results, as R3LIVE and FAST-LIVO failed.
In Fig. 11 (b), the blue arrow represents movement towards a
pure black screen, indicating concurrent LiDAR and camera
degeneration. In Fig. 11 (c1) and (c2), the red points represent
the LiDAR scan at that location, illustrating the areas of
LiDAR degeneration due to the single plane being observed.
Furthermore, the “Mining Tunnel” exhibits very dim lighting
throughout the whole sequence, coupled with frequent visual
and LiDAR degeneration. Despite of these challenges, FAST-
LIVO2 still returns to the starting point with an end-to-end
error of less than 0.01 m in both sequences.
D. High-precision Mapping
In this experiment, we validate the high-precision map-
ping capabilities of our system. To explore the mapping
accuracy across different algorithms and ensure fairness, we
compare our system with FAST-LIO2, R3LIVE, and FAST-
LIVO in scenes characterized by rich texture and structured
environments. We take the sequences “SYSU 01”, “HKU
Landmark” and “CBD Building 01” as examples. Fig. S9 in
the Supplementary Material [53] shows the colored point maps
of these sequences reconstructed in real time. We can clearly
observe that the point maps generated by FAST-LIVO2 retain
the finest details among all the systems, the enlarged views of
the colored point maps are akin to those in the actual RGB
image. In the “SYSU 01” sequence, our algorithm produces
fewer white noise dots on the signboard because we normalize
the image colors to a reasonable exposure time using the
recovered exposure time before coloring, resulting in rarely
overexposed colored point maps. The reconstruction of the
human and motorcycle in “CBD Building 01” also exemplifies
our ability to rebuild the details of unstructured objects. In all
sequences, the estimated final position returns to the starting

## Page 15

15
Fig. 10: The mapping results generated in real time in LiDAR degenerated scenes. The point clouds from top to bottom
correspond to “Bright Screen Wall”, “Black Screen Wall”, “HIT Graffiti Wall” (the third and fourth rows), “Banner Wall”,
“HKU Lecture Center”, respectively, showing the comparison of colored point cloud constructed FAST-LIVO2, FAST-LIVO
or R3LIVE (see more details on YouTube: youtu.be/aSAwVqR22mo).
point with an end-to-end error of less than 0.01 m. We also
tested FAST-LIVO2 in the remaining sequences of the prviate
dataset, with mapping results shown in Fig. S10-S13 in the
Supplementary Material [53].
E. Run Time Analysis
In this section, we evaluate the average computational time
per LiDAR scan and image frame of our proposed system,
tested on a desktop PC equipped with an Intel i7-10700K
CPU and 32 GB RAM. Our evaluations span public datasets
including Hilti’22, Hilti’23, and NTU-VIRAL, and our private
dataset. As shown in Table III, our system exhibits the lowest
processing time across all sequences. The average computation
time consumption on an Intel i7 processor is only 30.03 ms
(17.13 ms per LiDAR scan and 12.90 ms per image frame),
fulfilling real-time operation at 10 Hz. Besides, our system can
even operate in real time on ARM processors with an average
processing time per frame of just 78.44 ms. LVI-SAM’s
LiDAR and visual feature extraction modules in LIO and
VIO are time-consuming. In addition to the time consumed
by LIO and VIO, LVI-SAM integrates IMU pre-integration
constraints, visual odometry constraints, and LiDAR odometry
constraints within a factor graph, further increasing the overall
processing time. For R3LIVE, although also employing a
direct method, its pixel-wise image alignment necessitates the
use of a large number of visual map points. In contrast, our
approach uses sparse points with reference patches, enabling
efficient alignment. Additionally, R3LIVE maintains a colored
map that undergoes Bayesian updating, significantly increasing
the computational load as the map resolution increases. For
FAST-LIO2, the average processing time per frame (Table S3
in the Supplementary Material [53] due to space constraints)
is approximately 10.35 ms less than FAST-LIVO2 due to not
processing additional image measurements.
FAST-LIVO2 also shows noticeable improvements over the
predecessor FAST-LIVO. The primary enhancement stems
from our application of inverse compositional formulation in
the sparse image alignment. Employing affine warping based
on the plane prior from LiDAR points further enhances the
convergence efficiency of our method. Consequently, FAST-
LIVO2 reduces the number of iterations per pyramid level
from 10 to 3, while still achieving superior accuracy.
X. APPLICATIONS
To showcase the superior performance and versatility of
FAST-LIVO2 in real-world applications, we develop multiple

## Page 16

16
Fig. 11: The mapping results generated in real time in complex LiDAR degenerated and visually challenging scenes. (a), (b),
and (c) correspond to “HKU Cultural Center”, “CBD Building 03”, and “Mining Tunnel”, respectively. Different colored arrows
indicate the directions of degeneration caused by different sensors (see more details on YouTube: youtu.be/aSAwVqR22mo).

## Page 17

17
TABLE III: Processing time (ms) per LiDAR and image frame
Dataset
R3LIVE
LVI-
SAM
FAST-
LIVO
FAST-LIVO2
(LiDAR / Image)
FAST-LIVO2
(ARM)
Hilti’22
Construction Ground
105.03
×
52.33
36.52 (20.44 / 15.05)
96.12
Construction Multilevel
112.13
×
56.12
38.77 (21.38 / 17.39)
95.38
Construction Stairs
125.41
138.47 51.34
39.33 (24.32 / 15.01)
98.43
Long Corridor
120.42
109.97 48.68
41.42 (26.21 / 15.21)
94.33
Cupola
151.52
×
59.42
43.54 (26.53 / 17.01)
98.12
Lower Gallery
119.74
131.37 51.15
41.11 (25.69 / 15.42)
92.13
Attic to Upper Gallery
144.39
×
58.61
44.21 (27.12 / 17.09)
91.15
Outside Building
105.17
107.92 44.25
33.82 (18.91 / 14.91)
85.43
Hilti’23
Floor 0
117.01
×
52.23
42.22 (25.13 / 17.09)
92.24
Floor 1
106.11
106.98 50.14
43.12 (27.43 / 15.69)
93.52
Floor 2
154.65
×
53.24
41.78 (26.12 / 15.66)
94.43
Basement
118.21
×
48.23
39.65 (24.53 / 15.12)
93.42
Stairs
122.94
114.29 48.55
38.42 (22.64 / 15.78)
95.53
Parking 3x floors down
142.43
×
51.89
43.62 (26.99 / 16.63)
94.22
Large room
125.78
182.18 55.23
43.23 (26.43 / 16.80)
93.28
Large room (dark)
131.31
×
51.46
44.21 (29.12 / 15.09)
92.29
NTU VIRAL
eee 01
105.89
113.61 38.22
31.45 (17.24 / 14.21)
78.03
eee 02
112.27
119.19 39.43
30.24 (16.23 / 14.01)
79.22
eee 03
108.11
108.77 37.53
29.44 (16.12 / 13.32)
77.43
nya 01
122.73
124.54 39.66
34.52 (18.14 / 16.38)
79.44
nya 02
111.96
117.18 35.11
32.23 (17.33 / 14.90)
80.52
nya 03
115.96
111.24 38.42
33.42 (18.12 / 15.30)
78.95
sbs 01
112.77
115.67 39.23
31.92 (14.68 / 17.24)
78.32
sbs 02
113.01
110.37 35.39
32.56 (17.62 / 14.94)
72.43
sbs 03
119.91
120.73 37.41
33.62 (18.02 / 15.60)
75.56
Private Dataset
Retail Street
85.32
70.23
31.22
19.44 (10.42 / 9.02)
64.12
CBD Building 01
79.22
65.32
29.14
18.22 (10.32 / 7.90)
62.33
CBD Building 02
×
×
×
21.53 (11.50 / 10.03)
69.98
CBD Building 03
×
×
×
21.89 (11.98 / 9.91)
69.92
HKU Landmark
75.43
68.77
28.33
17.42 (10.12 / 7.30)
63.21
HKU Lecture Center
70.42
×
31.45
18.12 (10.99 / 7.13)
62.88
HKU Centennial Garden 74.33
70.12
33.46
19.22 (10.80 / 8.42)
64.52
HKU Cultural Center
102.34
×
35.62
21.43 (11.42 / 10.01)
72.43
HKU Main Building
75.62
×
30.21
19.43 (10.33 / 9.10)
65.31
HKUST Red Sculpture
84.22
90.13
32.43
20.14 (11.12 / 9.02)
65.42
HIT Graffiti Wall
112.56
×
39.98
21.71 (10.55 / 11.16)
68.99
Banner Wall
74.13
×
30.22
19.32 (10.01 / 9.31)
63.43
Bright Screen Wall
73.23
×
28.43
18.22 (9.92 / 8.30)
61.21
Black Screen Wall
71.42
×
27.66
17.99 (9.10 / 8.89)
60.91
Office Building Wall
×
×
×
19.42 (10.11 / 9.31)
62.33
Narrow Corridor
×
×
×
18.44 (8.32 / 10.12)
61.42
Long Corridor
×
×
×
19.53 (10.43 / 9.10)
62.55
Mining Tunnel
×
×
×
29.43 (15.42 / 14.01)
79.32
SYSU 01
112.66
88.95
32.23
23.65 (12.51 / 11.14)
77.43
SYSU 02
110.12
×
32.12
22.63 (11.82 / 10.81)
72.31
Average
108.36
108.45 41.43
30.03 (17.13 / 12.90)
78.44
× denotes the system totally failed.
solutions, including fully onboard autonomous UAV naviga-
tion, airborne mapping, textured mesh generation, and 3D
Gaussian splatting reconstruction for 3D scene representation.
A. Fully Onboard Autonomous UAV Navigation
Given the high precision and robust localization perfor-
mance of FAST-LIVO2, along with its real-time capabilities,
we conduct closed-loop autonomous UAV flights.
1) System Configurations:
The hardware and software
setup are illustrated in Fig. 12. For hardware, we use a
NUC (Intel i7-1360P CPU and 32 GB RAM) as the onboard
computer. In terms of software, the localization component is
powered by FAST-LIVO2, which provides position feedback
at 10Hz. The localizationr result is fed to the flight controller
to achieve 200Hz feedback on position, velocity, and attitude.
FAST-LIVO2
Trajectory 
Planner
MPC 
Controller
Angular Velocity
Controller
Extended 
Kalman filter
Mixer
Dense point cloud
Position estimate
Trajectory 
commands
Desired angular 
velocity
Desired thrust
Point cloud & IMU
(10 Hz & 200 Hz, LiDAR)
Image (10 Hz)
Motor
PWM
Position, velocity, 
attitude feedback
(200 Hz)
IMU (200 Hz, 
filght control) 
Desired 
moments
Angular 
velocity 
feedback
Flight controller
Onboard computer
Position feedback 
(10 Hz)
Battery
STM32
Build-in 
IMU
LiDAR
Camera
On-board 
PC
Fig. 12: Fully onboard UAV navigation algorithm flowchart.
Fig. 13: (a) and (b) are the enlarged point maps of the “Woods”
and “Narrow Opening” experiments, respectively. The red
points in (a1), (a3), and (b4) represent the current scan. (a2)
and (a4) represent the first-person view at the corresponding
locations. (b1), (b2), and (b3) depict the third-person view (see
more details on YouTube: youtu.be/aSAwVqR22mo).
Besides localization, FAST-LIVO2 supplies a dense registered
point cloud to the planning module, the Bubble planner [55],
which plans a smooth trajectory that is then tracked by an
on-manifold Model Predictive Control (MPC) [56]. The MPC
calculates the desired angular rates and thrust, which are
tracked by respective low-level angular rate controllers running
on the flight controller. Importantly, the MPC, Planner, and
FAST-LIVO2 all operate on the onboard computer in real time.
2) UAV Autonomous Navigation: We conduct 4 fully on-
board autonomous UAV navigation experiments, “Basement”,
“Woods”, “Narrow Opening”, and “SYSU Campus” (Ta-
ble S2 in the Supplementary Material [53]). “Basement” and
“Woods” experiments are fully autonomous flights incorpo-
rating all planning, MPC, and FAST-LIVO2 modules, while
“Narrow Opening” and “SYSU Campus” are manual flights

## Page 18

18
with only MPC and FAST-LIVO2 (without the planning com-
ponent). As can be seen, “Basement” and “Woods” showcase
the UAV’s successful autonomous navigation and obstacle
avoidance. In “Narrow Opening”, the UAV is commanded to
fly close proximity to a wall leading to few LiDAR points
measurements. Nevertheless, the raycasting module recalls a
greater number of visual map points, providing abundant con-
straints for localization, which allows for stable localization.
Moreover, “Basement” and “Narrow Opening” experience
LiDAR degeneration, observing only a single wall (see Fig. 1
(e1) and (e4), Fig. 13 (b1-b4)), along with significant exposure
variations (see Fig. 1 (e5-e6)). Despite these challenges, our
UAV system performed exceptionally well. “Woods” involves
the UAV moving at high speeds up to 3 m/s, demanding
rapid response from the entire UAV system (see Fig. 13 (a1-
a4)). “SYSU Campus”, a non-degenerated scene, primarily
demonstrates the onboard high-precision mapping capabilities
(see Fig. S14 in the Supplementary Material [53]). Finally, it
is worth mentioning that in all these four UAV flights, severe
lighting variation occurred. FAST-LIVO2 is able to estimate
exposure time that closely follows the ground-truth values (see
Fig. S15 in the Supplementary Material [53]).
Regarding onboard computational time, the need to run
MPC (at 100 Hz) and Planning (at 10 Hz) on the onboard
computer consumes computational resources and memory,
limiting the computation resources available to FAST-LIVO2.
Despite of the concurrent execution of control and planning,
as illustrated in Fig. 14, the average onboard processing
time per LiDAR scan and image frame for FAST-LIVO2,
approximately 53.47 ms, is still well below the frame period
100 ms. The average processing times for planning and MPC
are 8.43 ms and 18.5 ms, respectively. The total average
processing time of 80.4 ms meets very well the real-time
requirements for onboard operations.
FAST-LIVO2 
  Planning 
MPC(10 times) 
Total time
0
20
40
60
80
Time (ms)
Onboard UAV Experiment Time Cost
Fig. 14: The processing time of each module and in total in
UAV autonomous navigation experiments across “Basement”,
“Woods”, “Narrow Opening”, and “SYSU Campus”. The MPC
executes at 100 Hz while planning and FAST-LIVO2 execute
at 10 Hz, so its computation time is counted for 10 times.
B. Airborne Mapping
Airborne mapping represents a crucial task in surveying and
mapping applications. To evaluate the suitability of FAST-
LIVO2 for this application, we conduct an aerial mapping
experiment using the public dataset MARS-LVIG [52] whose
hardware configuration is detailed in Section VIII-A. We
evaluate the two sequences “HKairport01” and “HKisland01”,
Fig. 15: (a) and (b) are the mesh and texture mapping of “CBD
Building 01”, respectively. (c) is the texture mapping of “Retail
Street”, with (c1) and (c2) showing local details.
whose real-time mapping results are illustrated in Fig. 1 (a-
c), with (a) and (c) corresponding to “HKisland01”, and
(b) depicting “HKairport01”. The results demonstrate the
effectiveness of FAST-LIVO2 in unstructured environments
such as forests and islands. The system successfully captures
many fine structures and sharp coloring effects, including
buildings, lane marks on roads, road curbs, tree crowns, and
rocks, all of which are clearly visible. The APE (RMSE) for
these sequences are 0.64 m and 0.27 m for FAST-LIVO2,
respectively, compared to 2.76 m and 0.52 m for R3LIVE.
The average processing times on the desktop PC (Section
IX-A), are approximately 25.2 ms and 21.8 ms, respectively,
compared to 110.5 ms and 100.2 ms for R3LIVE.
C. Supporting 3D Scene Applications: Mesh Generation, Tex-
ture, and Gaussian Splatting
Leveraging the high-precision sensor localization and dense
3D colored point map obtained from FAST-LIVO2, we de-
velop software applications for rendering pipelines including
meshing and texturing, as well as emerging NeRF-like ren-
dering pipeline such as 3D Gaussian Splatting (3DGS). For
meshing, we employ VDBFusion [57] based on the Truncated
Signed Distance Function (TSDF) in “CBD Building 01”,
shown in Fig. 15 (a). The sharp edges on the columns and the
distinct structure of the roof are clearly visible, demonstrating
the high quality of the mesh. This level of detail is achieved
due to the high density of FAST-LIVO2’s point clouds and
the exceptional accuracy of structural reconstruction. After
mesh construction, we use OpenMVS [58] to perform texture
mapping using the estimated camera poses in “CBD Building
01” and “Retail Street”, shown in Fig. 15 (b-c). In Fig. 15
(c1-c2), the texture images applied on the triangular facets are
seamless and accurately aligned, resulting in a highly clear
and precise texture mapping. This is attributed to pixel-level
image alignment achieved by FAST-LIVO2.
The dense color point clouds from FAST-LIVO2 can also
directly serve as the input of 3DGS. We conduct tests on
the sequence “CBD Building 01” utilizing 300 frames out

## Page 19

19
Fig. 16: Comparison of ground-truth image, COLMAP+3DGS, and FAST-LIVO2+3DGS in terms of render details, computa-
tional time (time for generating point clouds and estimating poses + training time), and PSNR for a random frame in “CBD
Building 01” (see more details on YouTube: youtu.be/aSAwVqR22mo).
of a total of 1,180 images. The results are shown in Fig. 16.
Compared to COLMAP [59], our method significantly reduces
the time required to obtain dense point clouds and poses
from 9 hours to 21 s. However, the training time increases
from 10 min and 59 s to 15 min and 30 s. This increase is
attributed to the denser point clouds (downsampled to 5 cm),
which introduce more parameters to optimize. Nonetheless, the
increased density and precision of our point clouds result in a
slightly higher Peak Signal-to-Noise Ratio (PSNR) compared
to the PSNR obtained from COLMAP inputs.
XI. CONCLUSION AND FUTURE WORK
This paper proposed FAST-LIVO2, a direct LIVO frame-
work achieving fast, accurate, and robust state estimation while
reconstructing the map on the fly. FAST-LIVO2 can achieve
high localization accuracy while being robust to severe LiDAR
and/or visual degeneration.
The gain in speed is attributed to the use of raw LiDAR,
inertial, and camera measurements within an efficient ESIKF
framework with sequential update. In the image update, an
inverse compositional formulation along with a sparse patch-
based image alignment is further adopted to boost the effi-
ciency. The gain in accuracy is attributed to the use (and
even refine) of plane priors from LiDAR points to enhance
accuracy of image alignment. Besides, a single unified voxel
map is used to manage simultaneously the map points and the
observed high-resolution image measurements. The voxel map
structure, which supports geometry construction and update,
visual map point generation and update, and reference patch
update, is developed and validated. The gain in robustness is
due to real-time estimation of exposure time, which effectively
handles environment illumination variation, and on-demand
voxel raycasting to cope with LiDARs’ close proximity blind
zones. The efficiency and accuracy of FAST-LIVO2 were
evaluated on extensive public datasets, while the robustness
and effectiveness of each system module were evaluated on
private dataset. The applications of FAST-LIVO2 in real-world
robotics applications, such as UAV navigation, 3D mapping,
and model rendering, were also demonstrated.
As an odometry, FAST-LIVO2 may have drifts over long
distances. In the future, we could integrate loop closure and
the sliding window optimization into FAST-LIVO2 to mitigate
this long-term drift. Moreover, the accurate and dense colored
point maps could be used to extract semantic information for
object-level semantic mapping.
REFERENCES
[1] R. Mur-Artal and J. D. Tard´os, “Orb-slam2: An open-source slam
system for monocular, stereo, and rgb-d cameras,” IEEE transactions
on robotics, vol. 33, no. 5, pp. 1255–1262, 2017.
[2] J. Engel, V. Koltun, and D. Cremers, “Direct sparse odometry,” IEEE
transactions on pattern analysis and machine intelligence, vol. 40, no. 3,
pp. 611–625, 2017.
[3] J. Engel, T. Sch¨ops, and D. Cremers, “Lsd-slam: Large-scale direct
monocular slam,” in European conference on computer vision. Springer,
2014, pp. 834–849.
[4] C. Forster, Z. Zhang, M. Gassner, M. Werlberger, and D. Scaramuzza,
“Svo: Semidirect visual odometry for monocular and multicamera sys-
tems,” IEEE Transactions on Robotics, vol. 33, no. 2, pp. 249–265,
2016.
[5] J. Zhang and S. Singh, “Loam: Lidar odometry and mapping in real-
time.” in Robotics: Science and Systems, vol. 2, no. 9, 2014.
[6] J. Lin and F. Zhang, “Loam livox: A fast, robust, high-precision lidar
odometry and mapping package for lidars of small fov,” in 2020 IEEE
International Conference on Robotics and Automation (ICRA).
IEEE,
2020, pp. 3126–3131.
[7] T. Shan and B. Englot, “Lego-loam: Lightweight and ground-optimized
lidar odometry and mapping on variable terrain,” in 2018 IEEE/RSJ
International Conference on Intelligent Robots and Systems (IROS).
IEEE, 2018, pp. 4758–4765.
[8] C. Zheng, Q. Zhu, W. Xu, X. Liu, Q. Guo, and F. Zhang, “Fast-livo: Fast
and tightly-coupled sparse-direct lidar-inertial-visual odometry,” in 2022
IEEE/RSJ International Conference on Intelligent Robots and Systems
(IROS).
IEEE, 2022, pp. 4003–4009.
[9] T. Qin, P. Li, and S. Shen, “Vins-mono: A robust and versatile monocular
visual-inertial state estimator,” IEEE Transactions on Robotics, vol. 34,
no. 4, pp. 1004–1020, 2018.
[10] R. Mur-Artal, J. M. M. Montiel, and J. D. Tardos, “Orb-slam: a versatile
and accurate monocular slam system,” IEEE transactions on robotics,
vol. 31, no. 5, pp. 1147–1163, 2015.
[11] M.Irani and P.Anandan, “All about direct methods,” in Proc. Workshop
Vis. Algorithms, Theory Pract, 1999, pp. 267–277.
[12] C. Forster, M. Pizzoli, and D. Scaramuzza, “Svo: Fast semi-direct
monocular visual odometry,” in 2014 IEEE international conference on
robotics and automation (ICRA).
IEEE, 2014, pp. 15–22.
[13] W. Xu, Y. Cai, D. He, J. Lin, and F. Zhang, “Fast-lio2: Fast direct lidar-
inertial odometry,” IEEE Transactions on Robotics, pp. 1–21, 2022.
[14] C. Yuan, W. Xu, X. Liu, X. Hong, and F. Zhang, “Efficient and
probabilistic adaptive voxel mapping for accurate online lidar odometry,”
IEEE Robotics and Automation Letters, vol. 7, no. 3, pp. 8518–8525,
2022.

## Page 20

20
[15] M. Meilland, A. I. Comport, and P. Rives, “Real-time dense visual
tracking under large lighting variations,” in British Machine Vision
Conference.
British Machine Vision Association, 2011, pp. 45–1.
[16] T. Tykk¨al¨a, C. Audras, and A. I. Comport, “Direct iterative closest point
for real-time visual odometry,” in 2011 IEEE International Conference
on Computer Vision Workshops (ICCV Workshops).
IEEE, 2011, pp.
2050–2056.
[17] C. Kerl, J. Sturm, and D. Cremers, “Robust odometry estimation for
rgb-d cameras,” in 2013 IEEE international conference on robotics and
automation.
IEEE, 2013, pp. 3748–3754.
[18] J. Engel, J. Sturm, and D. Cremers, “Semi-dense visual odometry for a
monocular camera,” in Proceedings of the IEEE international conference
on computer vision, 2013, pp. 1449–1456.
[19] K. Chen, R. Nemiroff, and B. T. Lopez, “Direct lidar-inertial odometry:
Lightweight lio with continuous-time motion correction,” in 2023 IEEE
International Conference on Robotics and Automation (ICRA).
IEEE,
2023, pp. 3983–3989.
[20] Z. Wang, L. Zhang, Y. Shen, and Y. Zhou, “D-liom: Tightly-coupled
direct lidar-inertial odometry and mapping,” IEEE Transactions on
Multimedia, 2022.
[21] J. Zhang and S. Singh, “Laser–visual–inertial odometry and mapping
with high robustness and low drift,” Journal of field robotics, vol. 35,
no. 8, pp. 1242–1264, 2018.
[22] W. Shao, S. Vijayarangan, C. Li, and G. Kantor, “Stereo visual inertial
lidar simultaneous localization and mapping,” in 2019 IEEE/RSJ Inter-
national Conference on Intelligent Robots and Systems (IROS).
IEEE,
2019, pp. 370–377.
[23] J. Zhang, M. Kaess, and S. Singh, “A real-time method for depth
enhanced visual odometry,” Autonomous Robots, vol. 41, pp. 31–43,
2017.
[24] J. Graeter, A. Wilczynski, and M. Lauer, “Limo: Lidar-monocular visual
odometry,” in 2018 IEEE/RSJ international conference on intelligent
robots and systems (IROS).
IEEE, 2018, pp. 7872–7879.
[25] Y. Zhu, C. Zheng, C. Yuan, X. Huang, and X. Hong, “Camvox: A
low-cost and accurate lidar-assisted visual slam system,” in 2021 IEEE
International Conference on Robotics and Automation (ICRA).
IEEE,
2021, pp. 5049–5055.
[26] S.-S. Huang, Z.-Y. Ma, T.-J. Mu, H. Fu, and S.-M. Hu, “Lidar-
monocular visual odometry using point and line features,” in 2020 IEEE
International Conference on Robotics and Automation (ICRA).
IEEE,
2020, pp. 1091–1097.
[27] C. Campos, R. Elvira, J. J. G. Rodr´ıguez, J. M. Montiel, and J. D.
Tard´os, “Orb-slam3: An accurate open-source library for visual, visual–
inertial, and multimap slam,” IEEE Transactions on Robotics, vol. 37,
no. 6, pp. 1874–1890, 2021.
[28] Y.-S. Shin, Y. S. Park, and A. Kim, “Dvl-slam: Sparse depth enhanced
direct visual-lidar slam,” Autonomous Robots, vol. 44, no. 2, pp. 115–
130, 2020.
[29] X. Zuo, P. Geneva, W. Lee, Y. Liu, and G. Huang, “Lic-fusion: Lidar-
inertial-camera odometry,” in 2019 IEEE/RSJ International Conference
on Intelligent Robots and Systems (IROS), 2019, pp. 5848–5854.
[30] K. Sun, K. Mohta, B. Pfrommer, M. Watterson, S. Liu, Y. Mulgaonkar,
C. J. Taylor, and V. Kumar, “Robust stereo visual inertial odometry for
fast autonomous flight,” IEEE Robotics and Automation Letters, vol. 3,
no. 2, pp. 965–972, 2018.
[31] X. Zuo, Y. Yang, P. Geneva, J. Lv, Y. Liu, G. Huang, and M. Pollefeys,
“Lic-fusion 2.0: Lidar-inertial-camera odometry with sliding-window
plane-feature tracking,” in 2020 IEEE/RSJ International Conference on
Intelligent Robots and Systems (IROS).
IEEE, 2020, pp. 5112–5119.
[32] D. Wisth, M. Camurri, S. Das, and M. Fallon, “Unified multi-modal
landmark tracking for tightly coupled lidar-visual-inertial odometry,”
IEEE Robotics and Automation Letters, vol. 6, no. 2, pp. 1004–1011,
2021.
[33] J. Lin, C. Zheng, W. Xu, and F. Zhang, “R2live: A robust, real-time,
lidar-inertial-visual tightly-coupled state estimator and mapping,” IEEE
Robotics and Automation Letters, vol. 6, no. 4, pp. 7469–7476, 2021.
[34] C. F. W. Bell B.M., “The iterated kalman filter update as a gauss-newton
method,” Automatic Control IEEE Transactions, vol. 38, no. 2, pp. 294–
297, 1993.
[35] T. Shan, B. Englot, C. Ratti, and D. Rus, “Lvi-sam: Tightly-coupled
lidar-visual-inertial odometry via smoothing and mapping,” in 2021
IEEE international conference on robotics and automation (ICRA).
IEEE, 2021, pp. 5692–5698.
[36] J. Lin and F. Zhang, “R 3 live: A robust, real-time, rgb-colored, lidar-
inertial-visual tightly-coupled state estimation and mapping package,”
in 2022 International Conference on Robotics and Automation (ICRA).
IEEE, 2022, pp. 10 672–10 678.
[37] ——, “R 3 live++: A robust, real-time, radiance reconstruction pack-
age with a tightly-coupled lidar-inertial-visual state estimator,” arXiv
preprint arXiv:2209.03666, 2022.
[38] J. Engel, V. Usenko, and D. Cremers, “A photometrically cali-
brated benchmark for monocular visual odometry,” arXiv preprint
arXiv:1607.02555, 2016.
[39] W. Wang, J. Liu, C. Wang, B. Luo, and C. Zhang, “Dv-loam: Direct
visual lidar odometry and mapping,” Remote Sensing, vol. 13, no. 16,
p. 3340, 2021.
[40] Z. Yuan, Q. Wang, K. Cheng, T. Hao, and X. Yang, “Sdv-loam:
Semi-direct visual-lidar odometry and mapping,” IEEE Transactions on
Pattern Analysis and Machine Intelligence, 2023.
[41] H. Zhang, L. Du, S. Bao, J. Yuan, and S. Ma, “Lvio-fusion:tightly-
coupled lidar-visual-inertial odometry and mapping in degenerate envi-
ronments,” IEEE Robotics and Automation Letters, vol. 9, no. 4, pp.
3783–3790, 2024.
[42] W. Xu and F. Zhang, “Fast-lio: A fast, robust lidar-inertial odometry
package by tightly-coupled iterated kalman filter,” IEEE Robotics and
Automation Letters, pp. 1–1, 2021.
[43] D. He, W. Xu, and F. Zhang, “Symbolic representation and toolkit de-
velopment of iterated error-state extended kalman filters on manifolds,”
IEEE Transactions on Industrial Electronics, 2023.
[44] D. Willner, C.-B. Chang, and K.-P. Dunn, “Kalman filter algorithms
for a multi-sensor system,” in 1976 IEEE conference on decision and
control including the 15th symposium on adaptive processes.
IEEE,
1976, pp. 570–574.
[45] J. Ma and S. Sun, “Globally optimal distributed and sequential state fu-
sion filters for multi-sensor systems with correlated noises,” Information
Fusion, p. 101885, 2023.
[46] Y. Ren, Y. Cai, F. Zhu, S. Liang, and F. Zhang, “Rog-map: An efficient
robocentric occupancy grid map for large-scene and high-resolution
lidar-based motion planning,” arXiv preprint arXiv:2302.14819, 2023.
[47] R. M. Stereopsis, “Accurate, dense, and robust multiview stereopsis,”
IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE IN-
TELLIGENCE, vol. 32, no. 8, 2010.
[48] S. Baker and I. Matthews, “Lucas-kanade 20 years on: A unifying
framework,” International journal of computer vision, vol. 56, pp. 221–
255, 2004.
[49] T.-M. Nguyen, S. Yuan, M. Cao, Y. Lyu, T. H. Nguyen, and L. Xie,
“Ntu viral: A visual-inertial-ranging-lidar dataset, from an aerial vehicle
viewpoint,” The International Journal of Robotics Research, vol. 41,
no. 3, pp. 270–280, 2022.
[50] M. Helmberger, K. Morin, B. Berner, N. Kumar, G. Cioffi, and
D. Scaramuzza, “The hilti slam challenge dataset,” IEEE Robotics and
Automation Letters, vol. 7, no. 3, pp. 7518–7525, 2022.
[51] L. Zhang, M. Helmberger, L. F. T. Fu, D. Wisth, M. Camurri, D. Scara-
muzza, and M. Fallon, “Hilti-oxford dataset: A millimeter-accurate
benchmark for simultaneous localization and mapping,” IEEE Robotics
and Automation Letters, vol. 8, no. 1, pp. 408–415, 2022.
[52] H. Li, Y. Zou, N. Chen, J. Lin, X. Liu, W. Xu, C. Zheng, R. Li, D. He,
F. Kong, et al., “Mars-lvig dataset: A multi-sensor aerial robots slam
dataset for lidar-visual-inertial-gnss fusion,” The International Journal
of Robotics Research, p. 02783649241227968, 2024.
[53] “Supplementary material: Fast-livo2: Fast, direct lidar-inertial-visual
odometry,” available online: https://github.com/hku-mars/FAST-LIVO2/
blob/main/Supplementary/LIVO2 supplementary.pdf.
[54] C. Klug, C. Arth, D. Schmalstieg, and T. Gloor, “Measurement uncer-
tainty analysis of a robotic total station simulation,” in IECON 2018-44th
Annual Conference of the IEEE Industrial Electronics Society.
IEEE,
2018, pp. 2576–2582.
[55] Y. Ren, F. Zhu, W. Liu, Z. Wang, Y. Lin, F. Gao, and F. Zhang,
“Bubble planner: Planning high-speed smooth quadrotor trajectories
using receding corridors,” in 2022 IEEE/RSJ International Conference
on Intelligent Robots and Systems (IROS). IEEE, 2022, pp. 6332–6339.
[56] G. Lu, W. Xu, and F. Zhang, “On-manifold model predictive control for
trajectory tracking on robotic systems,” IEEE Transactions on Industrial
Electronics, vol. 70, no. 9, pp. 9192–9202, 2022.
[57] I. Vizzo, T. Guadagnino, J. Behley, and C. Stachniss, “Vdbfusion:
Flexible and efficient tsdf integration of range sensor data,” Sensors,
vol. 22, no. 3, 2022. [Online]. Available: https://www.mdpi.com/
1424-8220/22/3/1296
[58] D. Cernea, “Openmvs: multi-view stereo reconstruction library. 2020,”
URL: https://cdcseacave. github. io/openMVS, vol. 5, no. 6, p. 7, 2020.
[59] J. L. Sch¨onberger and J.-M. Frahm, “Structure-from-motion revisited,”
in 2016 IEEE Conference on Computer Vision and Pattern Recognition
(CVPR), 2016, pp. 4104–4113.

## Page 21

1
Supplementary Material for FAST-LIVO2: Fast, Direct LiDAR-Inertial-Visual Odometry
I. SYSTEM MODULE VALIDATION
In this section, we validate the key modules of our system, including the affine warping, normal refinement, reference patch
update, on-demanding raycasting query, exposure time estimation, and ESIKF sequential update utilizing the FAST-LIVO2
private dataset and MARS-LVIG dataset.
A. Evaluation of Affine Warping
In this experiment, we aim to comprehensively evaluate the various affine warping effects based on the constant depth
assumption (a common technique utilized in semi-dense methods), the plane prior from point clouds, and the refined plane
normal of our proposed system (denoted as “Constant depth”, “Plane prior”, and “Plane normal refined“, respectively). To
achieve this, we compare the mapping results and drift metrics of the three methods on “CBD Building 02” and “Office
Building Wall”. As depicted in Fig. S2, “Plane normal refined” delivers the most clear and accurate mapping results and the
next best is “Plane prior”. Notably, “Plane normal refined” renders text and patterns on the ground and walls, as well as lane
markings, with remarkable clarity. Moreover, the drift associated with “Plane prior” and “Plane normal refined” remains below
0.01 m, whereas “Constant depth” does not return to the starting position, experiencing a drift of 0.22 m. Such results confirm
the enhanced performance of affine warping based on the plane prior and enhancements by the plane normal refinement.
Besides, we compare warped projection effects based on “Constant depth” and “Plane prior” on the sequence “CBD Building
02” and “Office Building Wall”. We randomly select several image frames from these two sequences for the qualitative analysis.
For each frame, we project the reference patches attached to the visual map points visible in the frame onto a blank image of
the current frame. This process yields a novel RGB image. If the affine warping and pose estimation are both performed well,
areas with patch projections will produce a seamless and minimally distorted appearance, closely resembling the raw RGB
image. The comparison of warped patches is presented in Fig. S1. The results indicate that the pose accuracy and warped
performance under “Plane prior” significantly outperform those under “Constant depth” .
Fig. S1: (a) and (c) depict the warped patches derived from the constant depth assumption, while (b) and (d) represent those
based on the plane prior.
B. Evaluation of Reference Patch Update and Normal Convergence
In this experiment, we validate the effects of the reference patch update strategy and normal convergence on “HIT Graffiti
Wall” and “HKU Centennial Garden”. As shown in Fig. S3, (a) and (b) are the reconstructed point clouds of these two
sequences. On the right, for each region from A to H, we respectively present five patch observations captured at different
poses, each with a patch size of 40 × 40 pixels for visualization. These patches are observed in camera frames located at
corresponding numbers on the left. As can be seen, our reference path update strategy tends to choose a high-resolution
reference patch that faces the plane along its normal. It is also noticed that, despite of visual map points and patches generated
at non-planar locations (e.g., tree leaves, trunk, and a lamp stand), the overall mapping quality is still high.
We also evaluate the convergence of our proposed normal estimation across patches in regions A to H. Each patch is in the
size of 11×11 pixels. The initial normal vector is estimated from the LiDAR points. The convergence curves, which represent
the angle change between the initial and optimized normal vectors at each iteration number, are shown in Fig. S3. Regions
A, C, D, and E are structured areas, whereas regions B, F, G, and H are unstructured ones. It can be observed that normal
vectors for structured areas converge faster (within 6 iterations) with small normal refinement (2 to 4 degrees) because the
initial normal provided by point clouds is relatively accurate. In unstructured areas, such as shrubs and tree leaves (i.e., B and
F), the normal refinement is significant (up to 9 degrees) and requires 9 iterations to converge. Overall, normal refinement
across these 8 regions demonstrates good convergence properties.

## Page 22

2
Fig. S2: (a) and (b) are FAST-LIVO2 default mapping results in “CBD Building 02” and “Office Building Wall”, respectively.
(a1, b1), (a2, b2), (a3, b3) are enlarged views of the point clouds using “Plane normal refined”, “Plane prior”, and “Constant
depth”, respectively.
Iteration Number
Angle Change (Degrees)
Normal Convergence Across Different Visual Map Points (A to H)
A
B
C
D
E
F
G
H
(c)
Fig. S3: The illustration of reference patch update. (a) and (b) are the reconstructed point clouds of sequences “HIT Graffiti
Wall” and “HKU Centennial Garden”, respectively. Regions A to H encompass both structured and unstructured areas in the
scene. On the right, the 40 × 40 image patches illustrate various observations for the same region, with numbers indicating
the corresponding camera frame on the left. The reference patch for each region is highlighted by a red box. (c) shows the
convergence of patch normal across regions A to H.

## Page 23

3
(a)
1.9m
`
(b) Weakly textured wall
Fig. S4: The illustration of on-demand raycasting and voxel query. (a) displays a top-down view of the reconstructed point
cloud for “Narrow Corridor”, with a corridor width of 1.9 m. In (a), the blue line indicates the trajectory and the yellow arrows
represent the direction of movement. The LiDAR camera sensor suite is turned to face a wall on the left side at the location
contained in the dashed box. (b) shows the camera image during the turn, having dim lighting conditions and very few LiDAR
points. In (b), blue dots represent points acquired from raycasting, yellow dots indicate points from voxel query, and red dots
are points in the LiDAR scan.
Ground Truth 
Estimated
Retail Street
HKU Centennial Garden
HKU Cultural Center
HKU Main Building
Exposure Time (ms)
Fig. S5: Comparison of estimated exposure time versus ground truth exposure time in “Retail Street”, “HKU Centennial
Garden”, “HKU Cultural Center”, and “HKU Main Building”.
C. Evaluation of On-demand Raycasting
In this experiment, we assess the performance of the on-demand raycasting module under extreme conditions where the
current and recent LiDAR scans have few or even no points due to LiDARs’ close proximity blind zone1. We use the sequence
“Narrow Corridor” for an in-depth analysis illustrated in Fig. S4. In this sequence, we traverse an extremely narrow tunnel,
approximately 1.9 m in width, and turn to face the weakly textured wall on one side. Due to the limited points in the LiDAR
scans when facing the wall, we can only acquire few visual map points through voxel query (yellow dots in Fig. S4 (b)). In
this case, raycasting offers sufficient visual constraints to mitigate degeneration (blue dots in Fig. S4 (b)). The visualization
results demonstrate that the on-demand raycasting module works well under challenging conditions with few points in LiDAR
scans.
D. Evaluation of Exposure Time Estimation
In this experiment, we validate the exposure time estimation module in two parts: 1) For the sequence with fixed exposure
and gain, we multiply each pixel of the received raw image by an exposure factor that changes sinusoidally over time. We
verify the effectiveness of our estimation by comparing the estimated exposure times against the sinusoidal function applied.
2) For sequences with auto-exposure and either fixed or auto-gain settings, we evaluate the accuracy of our estimated exposure
times by comparing them with the ground truth values retrieved from the camera’s API.
In part one, we test on the sequence “Retail Street”, applying an exposure factor to images with fixed exposure and gain. As
shown in Fig. S5, the estimated relative inverse exposure time matches the true values very well, evidencing the convergence of
our exposure estimation in synthetic conditions. In part two, we use the sequences “HKU Centennial Garden”, “HKU Cultural
Garden” and “HKU Main Building”, which have significant exposure time changes, for testing. We scale the estimated relative
exposure times by the first frame to recover the actual exposure time (ms) of each frame. As shown in Fig. S5, the estimated
exposure time follows closely the ground-truth values, which validates the effectiveness of our exposure time estimation module.
The occasional mismatches are possibly due to the unmodeled response function and vignetting factor [38].
1https://www.livoxtech.com/avia/specs

## Page 24

4
E. Evaluation of ESIKF Sequential Update
In this experiment, we evaluate different ESIKF update strategies for LiDAR and camera states. We compare asynchronous
versus synchronous updates, as well as standard versus sequential updates. Specifically, we assess three strategies: “asynchronous
(standard update)”, where the camera and LiDAR states are updated at their respective sampling times without scan
recombination; “synchronous (standard update)”, where LiDAR scans are recombined to sync with camera images and the
state is updated with both LiDAR and camera measurements within a standard ESIKF; and “synchronous (sequential update)”,
where the LiDAR and camera are synced but the state is first updated by LiDAR measurements and then updated by camera
measurements. These strategies are evaluated in terms of accuracy, robustness, and efficiency using the “AMvalley03” sequence
of the MARS-LVIG dataset. We select this sequence for several key reasons:
(1) This sequence includes slopes that lead to both LiDAR and visual degenerations, making it a challenging test case.
(2) This sequence represents an extremely large-scale scenario (approximately 901 m×500 m×130 m) with long-term and
high-speed data collection (covering 600 s at a speed of 12 m/s), where pose deviations are prone to occur (due to the
long-term and high-speed conditions), and even slight drifts can cause significant blurring in the colored point clouds (due
to the large scale), leading to more pronounced comparative results.
(3) This sequence provides the RTK ground truth data, allowing for more accurate quantitative comparisons.
We compare the qualitative mapping results, quantitative APE, and the average processing time of the three update strategies.
The experimental configuration is as follows: LiDAR updates involve up to 5 iterations, visual updates use a three-level pyramid
with up to 5 iterations per level and no more than 3 iterations per level when the camera and LiDAR are updated simultaneously
in a standard ESIKF, and the scale normalization factor (from visual photometric error to LiDAR point-to-plane distance) for
the “synchronous (standard update)” is set to 0.0032, which has been meticulously tuned for optimal performance.
Fig. S6, (a-c) present the reconstructed colored point clouds for this sequence. It is evident that the “synchronous (sequential
update)” strategy produces accurate mapping results, particularly in the areas highlighted by the blue and orange boxes, where
the mountain roads are reconstructed without any layering. In contrast, the other two strategies exhibit misalignments in
these areas, although the “synchronous (standard update)” performs slightly better than the “asynchronous (standard update)”.
The superior performance of the “synchronous (sequential update)” strategy is mainly attributed to its robustness in handling
significant LiDAR and visual degenerations, as seen in the white box (c3). This area features a large, textureless slope, and the
UAV passes over it at a high speed, heavily relying on a strong prior. The other two methods, which rely solely on the IMU
prior, struggle to compute a relatively accurate image gradient descent direction, leading to significant linearization errors.
The APE (RMSE) metrics for the “AMvalley03” sequence are 3.12 m, 2.45 m, and 0.68 m for the “asynchronous (standard
update)”, “synchronous (standard update)”, and “synchronous (sequential update)”, respectively. The average processing times
on a desktop PC (Section IX-A) are approximately 27.6 ms, 49.9 ms, and 23.1 ms. Our proposed “synchronous (sequential
update)” achieves the highest efficiency and accuracy, while the “asynchronous (standard update)” has the lowest accuracy. The
“synchronous (standard update)” is the most time-consuming, primarily because it requires fusing all LiDAR measurements at
each level of the image pyramid.
Overall, our proposed “synchronous (sequential update)” offers superior accuracy and efficiency, while the “asynchronous
(standard update)” has the lowest accuracy, and the “synchronous (standard update)” is the most time-consuming.
Fig. S6: (a), (b), and (c) are the mapping results in “AMvalley03” for the “asynchronous (standard update)”, “synchronous
(standard update)”, and “synchronous (sequential update)” strategies, respectively. (a1, b1, c1) and (a2, b2, c2) are enlarged
views of the point clouds for different update strategies. The blue line represents the UAV’s flight path, and the red points in
(c3) indicate the LiDAR scan at that moment.

## Page 25

5
II. ADDITIONAL INFORMATION
TABLE S1: Overview of FAST-LIVO2 Private Dataset
Sequence
Duration
(minute:second)
Sensor
Degeneration
Return
Origin1
Exposure /
Gain Mode
Exposure
Time2
Close Surface
Distance3
Scene
Characteristics
Retail Street
2 min : 15 sec
—
✓
Fixed / Fixed
Outdoor
CBD Building 01
1 min : 58 sec
—
✓
Fixed / Auto
Outdoor
CBD Building 02
3 min : 54 sec
LiDAR
✓
Auto / Fixed
✓
Outdoor
CBD Building 03
5 min : 01 sec
Camera, LiDAR
✓
Auto / Fixed
✓
Outdoor, Textureless
HKU Landmark
1 min : 31 sec
—
✓
Auto / Fixed
✓
Outdoor
HKU Lecture Center
1 min : 17 sec
LiDAR
✓
Auto / Fixed
✓
Indoor
HKU Centennial Garden
1 min : 32 sec
LiDAR
✓
Auto / Fixed
✓
Outdoor
HKU Cultural Center
4 min : 01 sec
LiDAR
✓
Auto / Fixed
✓
Outdoor
HKU Main Building
1 min : 36 sec
Camera, LiDAR
✓
Auto / Auto
✓
Out(In)door4, Textureless
HKUST Red Sculpture
2 min : 10 sec
—
✓
Fixed / Auto
Outdoor, Cluttered
HIT Graffiti Wall
8 min : 57 sec
LiDAR
✓
Fixed / Auto
Outdoor
Banner Wall
1 min : 40 sec
LiDAR
✓
Fixed / Auto
Indoor, Dim
Bright Screen Wall
1 min : 18 sec
LiDAR
✓
Fixed / Auto
Indoor
Black Screen Wall
0 min : 56 sec
Camera, LiDAR
✓
Fixed / Auto
Indoor, Textureless
Office Building Wall
1 min : 9 sec
LiDAR
✓
Fixed / Auto
✓
Outdoor
Narrow Corridor
1 min : 1 sec
Camera, LiDAR
✓
Fixed / Auto
✓
Indoor, Dim, Textureless
Long Corridor
1 min : 35 sec
LiDAR
✓
Fixed / Auto
✓
Indoor, Dim
Mining Tunnel
15 min : 49 sec
Camera, LiDAR
✓
Fixed / Auto
Indoor, Dim, Textureless
SYSU 01
4 min : 40 sec
—
✓
Auto / Auto
Outdoor, Light5
SYSU 02
4 min : 30 sec
Camera, LiDAR
✓
Auto / Auto
Out(In)door, Light
Total
66 min : 50 sec
Camera, LiDAR
✓
Auto (Fixed) / Auto (Fixed)
✓
✓
Out(In)door, Light,
Dim, Textureless
1 Sequences are collected by traveling in a loop, starting and ending at the same position.
2 Sequences with ground truth camera exposure time read from camera’s API.
3 Sequences exist where LiDAR captures no/limited point clouds due to close proximity blind zones.
4 Sequences include the process of moving from indoor to outdoor environments.
5 Sequences characterized by significant lighting variations.
TABLE S2: Overview of UAV Autonomous Navigation Experiments
Experiment
Flight Duration
(minute:second)
Flight
Mode6
Sensor
Degeneration
Return
origin
Exposure /
Gain Mode
Exposure
Time
Close Proximity
to Obstacles
Scene
Characteristics
Basement
5 min
Autonomous
Camera, LiDAR
✓
Auto / Auto
✓
Out(In)door, Light
Narrow Opening
2 min:32 sec
Manual
Camera, LiDAR
✓
Auto / Auto
✓
✓
Out(In)door, Light
SYSU Campus
3 min:6 sec
Manual
—
✓
Auto / Auto
Outdoor, Light
Woods
2 min:49 sec
Autonomous
Camera
✓
Auto / Fixed
✓
Outdoor, Cluttered
6 In autonomous mode, FAST-LIVO2, planning, and MPC modules are all running. In manual mode, FAST-LIVO2 and MPC are running while planning
is disabled.
TABLE S3: Average processing time per frame for FAST-LIO2 across different datasets
Hilti’22 & Hilti’23
Processing Time (ms)
NTU VIRAL
Processing Time (ms)
Private Dataset
Processing Time (ms)
Construction Ground
24.32
eee 01
17.63
Retail Street
10.23
Construction Multilevel
23.21
eee 02
17.33
CBD Building 01
10.40
Construction Stairs
×
eee 03
15.32
CBD Building 02
×
Long Corridor
28.43
nya 01
19.99
CBD Building 03
×
Cupola
×
nya 02
18.62
HKU Landmark
11.62
Lower Gallery
24.49
nya 03
19.32
HKU Lecture Center
×
Attic to Upper Gallery
×
nya 04
15.71
HKU Centennial Garden
×
Outside Building
18.67
sbs 02
16.10
HKU Cultural Center
×
Floor 0
27.34
sbs 03
17.71
HKU Main Building
×
Floor 1
27.12
HKUST Red Sculpture
10.98
Floor 2
25.22
HIT Graffiti Wall
×
Basement
22.31
Banner Wall
×
Stairs
20.91
Bright Screen Wall
×
Parking 3x floors down
×
Black Screen Wall
×
Large room
29.26
Office Building Wall
×
Large room (dark)
28.20
Narrow Corridor
×
Long Corridor
×
Mining Tunnel
×
SYSU 01
11.21
SYSU 02
×
Overall Average
19.68
7 × denotes the system totally failed.

## Page 26

6
Fig. S7: Challenging environments captured in the FAST-LIVO2 private dataset.
Fig. S8: The real-time mapping results of FAST-LIVO2 in the Hilti’22 dataset. (a) “Attic to Upper Gallery”, (b) “Cupola”, (c)
“Lower Gallery”, and (d) “Construction Stairs”. The point clouds in (a-c) are colored by intensity, while (d) is colored using
grayscale images.

## Page 27

7
Fig. S9: The real-time mapping results generated online in rich texture and structured scenes. The point clouds from left to
right correspond to “HKU Landmark”, “SYSU 01” and ”CBD Building 01”, respectively, showing the comparison of colored
point cloud accuracy among FAST-LIVO2, FAST-LIVO, R3LIVE, and FAST-LIO2.
Fig. S10: The real-time mapping results of FAST-LIVO2 in “HKU Main Building”, containing aggressive motions, indoor-to-
outdoor, outdoor-to-indoor, and a weakly textured wall.

## Page 28

8
Fig. S11: The real-time mapping results of FAST-LIVO2 in “SYSU 02”. (a) birdview of the colored point map, (b) drastic
lighting changes from indoor to outdoor facing the sun, (c) closeup view of details.
Fig. S12: The real-time mapping results of FAST-LIVO2 in “Long Corridor”. (a) birdview of the colored point map, (b) closeup
view of details, (c) LiDAR facing a single wall causing LiDAR degeneration.

## Page 29

9
Fig. S13: The real-time mapping results of FAST-LIVO2 in rich texture and structured scenes. (a) “HKUST Red Sculpture”,
(b) “CBD Building 01”.
Fig. S14: (a) is the enlarged point cloud image of the “SYSU Campus” experiment. (a1), (a2), and (a3) represent the third-person
view at the corresponding locations.

## Page 30

10
Basement
Narrow Opening
SYSU Campus
Woods
Ground truth 
Estimated
Exposure Time (ms)
Fig. S15: Comparison of estimated exposure time versus the ground truth exposure time in “Basement”, “Narrow Opening”,
“SYSU Campus”, and “Woods”.
