# LGVINS LiDAR-GPS-Visual and Inertial System Based Multi-Sensor Fusion for Smooth and Reliable UAV State Estimation.pdf

## Page 1

3976
IEEE TRANSACTIONS ON INTELLIGENT VEHICLES, VOL. 10, NO. 7, JULY 2025
LGVINS: LiDAR-GPS-Visual and Inertial System
Based Multi-Sensor Fusion for Smooth and Reliable
UAV State Estimation
Mahammad Irfan
, Graduate Student Member, IEEE, Sagar Dalai
, Graduate Student Member, IEEE, Petar Trslic,
Matheus C. Santos
, Member, IEEE, James Riordan, and Gerard Dooly
, Member, IEEE
Abstract—With the development of Autonomous Unmanned
Aerial Vehicle’s (UAV’s), Precise state estimation is a fundamental
aspect of autonomous ﬂight and plays a critical role in enabling
robots specially in GPS denied environment to operate safely,
reliably, and effectively across a wide range of applications and
operational scenarios. In this paper, we propose a tightly-coupled
multi-sensor ﬁltering framework for robust UAV/UGV state es-
timation, which integrates data from an Inertial Measurement
Unit (IMU), a stereo camera, GPS, and 3D range measurements
from two Light Detection and Ranging (LiDAR) sensors. The
proposed LGVINS system signiﬁcantly improves the accuracy and
robustness of state estimation in both structured and unstructured
outdoor environments, such as bridge inspections, open ﬁelds,
urban city and areas near buildings. It also improves positioning
accuracy in scenarios with or without GPS signals. The goal is to
exploit the fact that these sensor modalities have mutually exclusive
strengths, the visual, inertial and the Lidar sensor techniques are
implemented to compensate for the robots state estimate errors in
multiple outdoor challenging environment. It effectively reduces
long-term trajectory drift and ensures smooth, continuous state
estimation, regardless of GPS satellite availability. We demonstrate
and evaluate the LGVINS approach on public dataset as well as
our own dataset collected from the proposed hardware integration
on UAV, deployed on computationally-constrained systems. This
demonstrates that the proposed system achieves higher accuracy
and robustness in state estimation across various environments
compared to currently available methods.
Index
Terms—Intelligent
UAV/UGV,
LiDAR-visual-inertial
odometry, multi-sensor fusion, ROS, state-estimation.
Received 30 June 2024; revised 8 September 2024; accepted 18 September
2024. Date of publication 27 September 2024; date of current version 17 October
2025. This work was supported in part by the European Commission’s Horizon
2020 Project RAPID under Grant 861211, and in part by the Enterprise Ireland’s
Disruptive Technologies Innovation Fund (DTIF) Project GUARD under Grant
DT2020 0286B. (Corresponding author: Mahammad Irfan.)
Mahammad Irfan and Sagar Dalai are with the CRIS Research Group, De-
partment of Electronic and Computer Engineering, University of Limerick, V94
T9PX Limerick, Ireland (e-mail: mahammad.irfan@ul.ie).
PetarTrslic,MatheusC.Santos,andGerardDoolyarewiththeCRISResearch
Group and Department of School of Engineering, University of Limerick, V94
T9PX Limerick, Ireland.
James Riordan is with the ALMADA Research Centre, School of Computing,
Engineering and Physical Science, University of the West of Scotland, G72 0LH
Glasgow, U.K..
Color versions of one or more ﬁgures in this article are available at
https://doi.org/10.1109/TIV.2024.3469551.
Digital Object Identiﬁer 10.1109/TIV.2024.3469551
I. INTRODUCTION
T
HE ﬁeld of Autonomous and Intelligent Unmanned Aerial
Vehicle (UAV) has grown tremendously over the past few
years, as they have potential to explore unknown environments
and perform challenging tasks thereby reducing the need for
human intervention [1]. UAV ﬂight control is primarily de-
pendent on GPS and some use-cases where GPS robustness is
low, there are safety concerns. For example, in the application
of autonomous bridge inspection, GPS signal under or close
to the bridge suffers from low signal strength and multi-path
interference. An accurate localization and stable odometry po-
sition can be crucial in these GPS-denied use cases to provide
robust autonomous UAV navigation and control. Navigation and
control are difﬁcult in close quarter surveys close to infrastruc-
ture, however other perception payloads such as LiDAR and
stereo-camera can aid with localizing position and automatically
building up a surrounding map. These systems provide scene
perception for vehicle understanding, learning, and ultimately
interacting with the surrounding. For autonomous drones, 3D
perception of the environment with fusing data from several
sensors is a crucial task, which can be used to achieve an
improved localization in an obstacle-rich environment [2].
In the autonomous UAV navigation, localization and state
estimation task, an accurate GPS-RTK position is always nec-
essary during outdoor applications. One of the challenges is the
safe navigation in law GPS environment which requires a robust
UAV pose state estimation to rely on highly dynamic responses.
However, an autonomous UAV localization and pose estimation
in a complex scenario using a vision-based SLAM operation
cannot easily be solved due to error and uncertainties in onboard
sensors, resulting in inaccurate localization [3]. These sensors
when used individually are not accurate enough to produce
precision drone position estimation. In order to solve these
challenges, an optimized multi sensor fusion approach is imple-
mented with SLAM which ultimately minimizes single sensor
errors but also maximizes the UAV pose and localization by
fusing the information from multiple sensors and pass it through
a Kalman ﬁlter [4]. This will provide the level of integrity and
redundancy that a multi sensor fusion SLAM system requires
during autonomous UAV operation. Recent research, however,
has focused on integrating camera-LiDAR multi-sensor fusion
into SLAM systems [5]. The sensors such as LiDAR and stereo
© 2024 The Authors. This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see
https://creativecommons.org/licenses/by-nc-nd/4.0/

## Page 2

IRFAN et al.: LGVINS: LiDAR-GPS-VISUAL AND INERTIAL SYSTEM BASED MULTI-SENSOR FUSION FOR SMOOTH
3977
TABLE I
SUMMARY OF EXISTING MULTI SENSOR FUSION METHODS
cameras provide limited information by themselves, but when
combined creates a system resembling an eye, differentiating
colors, features and an accurate drone position and orientation.
The key contribution of this proposed paper lies in address-
ing the challenges associated with UAV/UGV state estimation.
Based on our knowledge, this study is among the ﬁrst to establish
a consistent and tightly-integrated multi sensor fusion, designed
to efﬁciently fuse commonly used sensors by addressing chal-
lenges like processing complexity, sensor synchronization is-
sues, and intra-sensor calibration. Although this article builds
on the ideas from previous studies [6], [7] and [8], it intro-
duces several distinct contributions and novelty as discussed in
Table I. Speciﬁcally, LGVINS utilizes the tightly coupled ﬁlter-
ing framework, allowing for the seamless high-frequency fusion
of multiple sensors regardless of their timing or delay within a
uniﬁed continuous-time structure. Beneﬁting from this, multiple
sensors can be easily fused into the framework as new factors.
Furthermore, this paper provides a novel fusion technique which
automatically includes/excludes GPS position to accurately fuse
true GPS position into state estimation as per the available
satellite signal that is robust to various challenging scenario.
Proposed LGVINS has added a new Lidar fusion technique,
embedding it within the existing VINS framework to facilitate
multi-LiDAR fusion. The system adopts the direct alignment
method [9] in place of other like LOAM feature extraction,
enhancing both the efﬁciency and consistency of updates.
The proposed method builds upon and enhances the VINS
and VINSFUSION [10] [4] models. We demonstrated a fusion
system which quickly and accurately determines the orientation
and position of the vehicle in order to give better state estimation
during close infrastructure inspection such as bridge survey
operation, near the high-rise buildings or cluttered environment.
Our proposed approach architecture is represented in the Figs. 2
and 1 depicts the proposed LGVINS with its trajectory plot-
ted on google map, indicating a strong alignment with RTK
ground truth data obtained using our handheld UAV integrated
with proposed multiple sensors at the University of Limerick
campus living bridge area. The Fig. 1 also shows the GPS signal
drifts near the high-rise buildings, however LGVINS trajectory
remains reliable and smooth. Hence, the developed system can
allow to the successful execution of unmanned ﬂight close to
target, allowing the drone to navigate in a GPS obstructed or
GPS denied environment.
Fig. 1.
Top view of Google maps plot of the proposed LGVINS global
estimated result with trajectory aligned well with the ground truth obtained
at UL living bridge area.
Fig. 2.
Depicts the proposed LGVINS architecture.
This paper excels in addressing state estimation challenges.
The algorithms presented have the capability to autonomously
choose relevant sensor data, thereby improving positioning ac-
curacy in situations with or without GPS signals. Furthermore,
in the absence of GPS, it can leverage Stereo-inertial or Lidar-
intertial odometry outcomes to ensure global positioning.
The key contributions of our work can be outlined as follows:

## Page 3

3978
IEEE TRANSACTIONS ON INTELLIGENT VEHICLES, VOL. 10, NO. 7, JULY 2025
r Proposed method leverages a tightly integrated multi-
sensor fusion framework comprising a VGA stereo camera,
two 3D LiDAR sensors, a 9 DOF IMU, and GPS-RTK
network optimization to achieve highly accurate trajectory
state estimation validated and tested both in UAV and UGV
platform.
r AcquisitionofchallengingdatasetsusingcommercialUAV
with in-house integrated and calibrated sensor hardware
platform.
r The performance and effectiveness of the proposed Stereo-
Visual-LiDAR fusion framework are validated through
experimental evaluations which achieve high efﬁciency,
robustness, consistency and accuracy in many challenging
scenarios.
r Validation demonstrates, drift-free 6-DoF global estima-
tions in environments such as beneath bridges and other
areas where GNSS signals are frequently lost for extended
periods without loop closure. The developed algorithm
automatically includes/excludes GPS position as per the
available satellite signal.
This paper is organized as follows Section II reviews the
relevant work. Section III describes the LGVINS Methodol-
ogy. Section IV describes Hardware and Experimental Setup.
Section V describes the Experiments and Results. Finally,
Section VI reports the conclusions and outlines future work.
II. RELATED WORK
Over the past few years, several UAV SLAM navigation
techniques in challenging environment have been proposed [11].
3D LiDAR based and Visual SLAM algorithms have their own
beneﬁts and disadvantages. Visual SLAM systems often use a
monocular or stereo camera in order to determine the camera
motion. Open-source vision-inertial slam, are sensor cost efﬁ-
cient and perform well in many scenarios, but the vision-based
approaches become unreliable in poor light and sensitive to
illumination change which results prone to errors and an in-
accurate odometry localization. However, SLAM when used
with RGB-D based cameras are sensitive to sunlight as it has
an inbuilt IR sensor. Therefore, these sensors are only useful
in indoor applications. Furthermore, the performance of these
SLAM algorithms is often challenging, especially in long-range
large-scale SLAM applications like a bridge inspection or out-
door open ﬁeld operation during a sunny and dark day time [12].
During the past few years, different open-source SLAM algo-
rithms has been introduced for the robotics research community
based on sensors used such as monocular, stereo, event cameras,
RGB-D, and when integrated them with an internal/external
IMU measurements known as visual-inertial odometry (VIO)
based SLAM approach. These techniques are mostly feature
based indirect and photometric or direct methods, However
VIO methods can be categorized into semi dense, dense, sparse
etc. Nowadays, LiDAR and RADAR sensors-based SLAM ap-
proaches are mostly implemented in autonomous cars [13].
Other research approaches have been conducted in aerial vehi-
cles with 3D/2D LiDAR based SLAM such as FASTLIO2, LIO-
SAM, LeGO-LOAM etc. [14]. Multi-sensor fusion technique
with combination of stereo and Lidar odometry is a new widely
researched topic in the robotics community. Recent research
shows low-cost consumers grade sensors may also be viable in
autonomous vehicles for multi-sensor fusion and internet of ve-
hicle communication etc. [15]. An ArUco marker-based SLAM
algorithm has also been introduced in an indoor UAV navigation
for path detection, guidance and an improved odometry fusion
using a stereo camera [16]. An improved fusion odometry results
in robust localization which help the UAVs to navigate in GPS
denied environments and help to achieve an Optimus control,
obstacle avoidance and path planning [17].
The implementation of a sensor-fusion approach for state
estimation has proven its effectiveness and robustness, with
abundant literature supporting this assertion. Although there
is a rich literature on the proposed topic however, our focus
lies in the integration of compact sensors like cameras, IMUs,
Lidar and GPS receivers, aiming to achieve precise estimation
of state in challenging environments. While systems equipped
with any number of sensor modalities boast advantages in terms
of robustness, accuracy, and versatility, their development has
been limited. This is largely due to the complexities involved
in processing large-scale computations and managing sensor
data that may be asynchronous, delayed, or both. Effective
management of asynchronous and delayed sensor measurements
is crucial in multi-sensor systems. This functionality allows the
system to ﬂexibly integrate in any number of sensors, whether
they are homogeneous or heterogeneous, accurately model the
measurements, and retain all available data without unnecessary
loss. Table I provides a summary of the relevant literature. The
fusion of VI system with a tightly coupled, is classiﬁed by
graph/optimization-based methods, learning-based approaches,
or ﬁlter-based methodologies.
A. Graph Based Approaches
Optimization methods are classiﬁed into two parts: the
back/front end. The front end handles map construction through
image processing, while the back end aim into pose optimiza-
tion. Graph-based formulations excel at handling delayed mea-
surements because they can maintain a complete or partially
obtained measurements. This capability enables delayed states
to be seamlessly incorporated into the optimization problem.
The latest VINS-Fusion [4] uses a pose graph to loosely combine
VINS which tightly integrates IMU and camera data with other
global sensors like GNSS, magnetometers, and barometers,
under the assumption that all sensors are perfectly synchronized.
OKVIS [24], an open keyframe-based visual inertial SLAM sys-
tem, introduced bundle adjustment along with keyframe-based
sliding window nonlinear optimization, marking a signiﬁcant
advancement in VO technology
Lvio-fusion [22] tightly integrates IMU, camera, and LiDAR
for trajectory estimation, while incorporating GNSS data in
a pose graph with a looser coupling. VINS-Mono [7] incor-
porates loop-closure constraints into both local sliding win-
dow and global pose graph optimization. It also incorporates
efﬁcient IMU pre-integration with bias correction, online ex-
trinsic calibration, and the capability for relocalization. The

## Page 4

IRFAN et al.: LGVINS: LiDAR-GPS-VISUAL AND INERTIAL SYSTEM BASED MULTI-SENSOR FUSION FOR SMOOTH
3979
VINS-Mono [7] framework integrates loop closure technique
into both pose graph and sliding window method. It also includes
highly desired preinegrated IMU with correct biases, live cali-
brated offset parameters, and the capability for relocalization.
Furthermore, VIRAL SLAM [23]merges IMU and stereo
camera data with multiple UWBs and LiDARs by aligning
all sensor measurements with the base LiDAR measurement
time. This process entails interpolating IMU and UWB data,
aligning non-base LiDAR point clouds with the base LiDAR
measurement time, and choosing camera measurements that are
closest in time while disregarding the rest. Through synchroniz-
ing sensors via independent state creation regardless of sensor
measurement timings, VIRAL-Fusion [23] uses interpolating
states to accommodate UWB measurements, and producing syn-
thetic measurements at the state timestamp using measurement
interpolation. GR-FUSION [2] tightly integrates visual, inertial,
LiDAR, and gps data to ﬁnd the true odometry position of a
robot. It leverages LiDAR data and scenes from object to extract
depth information of visual features and improve their quality.
Moreover, it chooses both stereo-point cloud from lidar-camera
for tracking and integrates all the sensors in a coupled manner
to optimize the robot’s current state.
B. Learning Based Approaches
In recent times, there has been a growing research in us-
ing deep neural networks to learn and predict robots states.
Learning-based methods offer the advantage of automatically
learning features rather than relying on hand-crafted ones.
These attributes empower deep learning-based approaches to
achieve greater robustness, particularly in scenarios where im-
ages exhibit variations in lighting or textures. These method-
ologies comprise probabilistic methods, statistical approaches,
knowledge-based techniques (including fuzzy logic and possi-
bility theory), interval analysis methods, and evidential reason-
ing methods. LO-Net [25] explores learning LIDAR odometry
by utilizing geometric evaluation based motion identiﬁcation
and integrating pose correction similar to deep simultaneous
localizationandmapping(SLAM)techniques.Itsaccuracycom-
parable to traditional approaches has been demonstrated through
experimentation.
Lvio-Fusion [22] is a tightly integrated SLAM framework that
utilizes 3D LiDAR, stereo camera, IMU, and GPS. It employs
factor graph optimization to fuse sensor data and incorporates a
lightweight deep reinforcement learning algorithm for adaptive
adjustment of sensor model weights. Posenet [26] is the pio-
neering study to employ convolutional neural networks (CNNs)
for the regression of pose from 2D images. Additional improve-
ments to PoseNet technique by integrating convolutional neural
networks (CNNs) with long short-term memories (LSTMs) to
enhance feature correlation [27]. MS-Transformer [28] repre-
sents a recent advancement in relocalization utilizing a trans-
former architecture, yielding sota results. Nonetheless, deep
learning approaches suffer from the drawback of requiring ex-
tensive training data and signiﬁcant computational resources.
Hence, traditional fusion approaches are deemed more practical
for drone applications.
C. Filtered Based Approaches
The tightly-coupled approach utilizes raw input data from
the sensors to collectively establish states. The MSCKF [29]
is an impressive ﬁlter-based state estimator that leverages the
camera poses and geometric constraints to effectively utilize
and optimize a robot’s state. The state estimation relies on
multiple past camera poses, while maintaining tracking of the
geometric parameter of camera features across multiple images.
Filter-based techniques continue to be ideal over graph-based
systems due to their effectiveness, which is essential for han-
dling computationally intensive multi-sensor fusion systems.
Moreover, in order to maintain asynchronous and delayed sensor
measurements is challenging, as ﬁlters usually maintain only
the most information and a brief historical record of stochastic
poses. Recent studies show that it can be feasible to study odom-
etry estimation from imu data using recurrent neural networks,
thereby enabling advanced deep VIO estimation techniques.
DeepVIO [30] recently introduced a fusion network speciﬁcally
designed to integrate vo and vio features. This function is trained
using a specialized function.
Furthermore, Robust Visual-Inertial Odometry (ROVIO) [31]
utilizes patch-based direct photometry use to updates via an
iterated ekf. Some initially introduced ﬁltering approaches, such
as those by [21]and [32], which fused cameras, IMU, wheel,
and LiDAR data using an EKF. [19], which combined GPS,
IMU, wheel, and LiDAR data with an unscented Kalman ﬁl-
ter (UKF), and [33], which integrated IMU, camera, GNSS,
wheel, and symbolic road map data with a particle ﬁlter (PF),
sensor measurements were assumed to be synchronized and
time-ordered. This assumption can introduce unmodeled errors
into the estimator when it does not hold. MSF-EKF [34] is
one of the pioneering works that addresses asynchronous and
delayed sensor measurements by integrating generic relative and
absolute values from inertial sensor, visual parameter, GPS, and
pressure sensor within an EKF framework. MSF-EKF addresses
asynchronicity by forward-predicting the current state from the
queried state when a delayed measurement is received, hence re-
quires subsequent measurement updates to be re-executed. Sim-
ilarly [20] introduced approaches dealing with asynchronous
and delayed sensor measurements, which fused IMU, camera,
GNSS, and UWB in iterated EKF.
D. Different Sensor Modalities Uses VINS Framework
A GPS sensor offers direct absolute position data, though its
accuracy heavily relies on environmental conditions and access
to external correction data. Consequently, many researchers
have explored integrating GPS with VINS to achieve locally
precise and globally accurate localization. Numerous studies
have examined the fusion of GPS with VINS through graph
formulations, employing both loosely-coupled [4], [35] and
tightly-coupled [36], [36], [37] approaches. Yet, GPS mea-
surements frequently occur intermittently and asynchronously
with respect to other sensors, complicating the design of the
graph construction process. Recent studies have concentrated
on integrating lower-level GNSS measurements, such as GNSS

## Page 5

3980
IEEE TRANSACTIONS ON INTELLIGENT VEHICLES, VOL. 10, NO. 7, JULY 2025
TABLE II
SENSOR CONFIGURATION
satellite signals, with VINS, as demonstrated by [6], [18], [38],
[39]and [40].
WhenwetalkaboutLidaronlycase,theseeffortsshowcaseen-
hanced robustness in scenarios with limited ﬁeld of view (FOV)
and improved localization accuracy. LiDAR is commonly inte-
grated with VINS because its measurements remain unaffected
by lighting conditions and it offers direct depth information.
This capability can address the limitations of cameras in various
scenarios, such as navigating in a sunny day, dark caves or
encountering featureless walls. Loosely coupled systems have
aimed to resolve the degeneracy problems inherent in indepen-
dent camera and LiDAR odometry algorithms. For instance,
LiDAR (combined with IMU) odometry is integrated with VINS
in a graph formulation, treating them as separate sub-systems to
enhance robustness [41]. Numerous research has employed ﬁl-
tering frameworks to develop tightly coupled systems, resulting
in improved estimate consistency and accuracy. MSCKF-based
designs,pioneeredby[29],havegainedpopularityandhavebeen
successfully implemented in various studies, including those
by [18], [40] and [14]. Likewise, the error state iterated Kalman
ﬁlter (ESIKF) is utilized while fusing LiDAR without extracting
the features (a.k.a. direct method) was also studied by [42].
III. METHODOLOGY
In this section, we discuss an in-depth explanation of the
LGVINS multi sensor fusion framework and demonstrate how
the each sensor modules are integrated. The system is based on
modiﬁed version of VINS system [7], [8].
A. Data-Preprocessing
The architecture of the proposed method is shown in Fig. 2.
The measurement frequency for each sensor is described in
Table II. The sampling rates of different sensors differ, like a
GPS at 50 Hz, camera at 15 Hz and a LiDAR at 20 Hz, making
their measurements generally asynchronous without hardware
synchronization. Hence, this leads difﬁculties in constructing
theirmeasurementmodels,asthecorrespondingIMUposestates
are unavailable at the exact measurement times can be seen in
(1). A basic strategy is to integrate IMU poses into the state
at the sampling time of each sensor, but this would increase
the state size and lead to a substantial computational burden. In
comparison, We use linear interpolation method given by [40]
of the bounding clones to estimate the IMU pose at the mea-
surement time to calculate 3D position increments of the robot,
which signiﬁcantly reduces computational overhead compared
to continuously adding clones to the state with each incoming
LiDAR measurement. We use the 1st-order linear interpolation
to handle asynchronous and delayed measurements. For the
time synchronization, We use ROS timestamps subscribe from
dji-osdk and integrated Livox Lidar sensor nodes. In addition,
The extrinsic parameters of stereo cameras and camera-IMU,
Lidar-IMU are calibrated ofﬂine by using the Kalibr tools [43]
and [44]. The extrinsic calibrated sensor parameters for public
dataset Kaist is obtained from [45].
B. Lgvins State Estimation
In this section, we reframe the state estimation issue within a
probabilistic ﬁlter graph methodology. Considering INS as the
pivotal component of the system, the proposed LGVINS propa-
gates UAV state estimation using IMU as primary measurements
and efﬁcient ﬁltering techniques.
It integrates multi-modal measurements from various adopted
sensors like cameras, LiDARs, IMU and GPS receivers for
accurate odometry updates, which is shown in the Fig. 2, With
reference to the VINS based MSCKF approach [8], [29]. The
integrated imu navigation state estimation vector xIk and xkk is
the sum of all the obtained IMU poses in the global frame G:
xk = (xIk, xNk )
(1)
xIK = (Ik
E R,E pIk,E vIk, Fg, Fa)
(2)
xNk = (Ik−1
E
R,E pIk−1, . . . , Ik−n
E
R EpIk−n)
(3)
Where Ik
E R is known as unit quaternion in JPL for rotation
matrix D
C R corresponding to C,D. D
C p and D
C v is position, linear
velocity corresponding to C and D respectively. Fg is gyroscope
bias and Fa is accelerometer bias. Further we have taken x =
x ⊞¯x, Here x is state estimation, ¯x known as obtained error
state, and x is known as true state.
Now, we will discuss each sensor modality and the proposed
LGVINS approach for updating and propagating the state esti-
mation corresponding to their measurements.

## Page 6

IRFAN et al.: LGVINS: LiDAR-GPS-VISUAL AND INERTIAL SYSTEM BASED MULTI-SENSOR FUSION FOR SMOOTH
3981
C. IMU Kinematic Model
The state estimation evolves over time by incorporating
high-rate IMU measurements, which typically denote angular
velocity ωv and local linear acceleration av:
ωvk = ωk + Fg + ng
(4)
avk = ak + Ik
E R
Eg + Fa + na
(5)
Here, ωk and ak is the true local angular velocity and linear
acceleration at time tk, respectively. Fg and Fa denote the bias
for the accelerometer and gyroscope.
Eg ≃[0 0 9.81]T represents the gravity as global, while na
and ng denote zero-mean Gaussian noises. The resultant mea-
surements are utilized to propagate the state estimation and
covariance from time tk to tk+1, following the standard inertial
kinematic model with zero noise assumption [46]:
ˆxIk+1|k = f(ˆxIk|k avk, ωvk, 0, 0)
(6)
PIk+1|k = ϑI(tk+1, tk) PIk|kϑI(tk+1, tk) ⊺+ JkQdJ⊺
k
(7)
where, Ik+1|k=IC|D
Furthermore, ˆxIC|D is the estimate at time tC which is ob-
tained by the processing its measurements in time tD.ϑ, J and
Q are the state transition matrix, Jacobian’s of f(.) w.r.t noise
vector and discrete noise covariance respectively which is found
from [47].
D. Camera Measurement Model
Let’s consider a scenario where a 3D feature is identiﬁed in
a random camera image at time tk. Its uv measurement, rep-
resenting the pixel coordinates on the image plane, is obtained
from [8]:
zC = hC (xk) + nC
(8)
= hd

hρ

ht(EpF , Ck
E R EpCk

, xCI) + nC
(9)
Here, xCI denotes the camera’s intrinsic parameters encom-
passing focal length and distortion parameters, nC represents
the zero-mean white Gaussian noise, zn denoted by undistorted
uv measured in normalized form, EpF is called as feature pose
in global, (Ck
E R EpCk) is the latest stereo visual pose obtained
the global frame. In above expression, we break down the
measurement function into several concatenated functions, each
representing distinct operations that transform the states into raw
UV measurements on the image plane. Each parameters (i.e.
hd, hρ, ht) is elaborated on next:
Projection Coefﬁcients (hp): The standard pinhole cam-
era model is utilized to project a 3D point,
CKpF =
[Ck
x
Ck y
Ck z]T onto the normalized image plane assuming
a unit depth:
zn = hρ(CKpF ) =
Ckx/Ckz
Cky/Ckz

(10)
Distortion Coefﬁcient (hd): To obtain the normalized coordi-
nates zn = [xn yn]T of a 3D feature projected onto the image
plane, a distortion model tailored to the speciﬁc camera lens type
is employed. Our LGVINS equipped drone uses VGA 640x480
resolution results grey scale images via ROS which we map to
the normalized coordinates into the raw pixel coordinates. In
regards with above circumstances, we chose hd with the camera
model:

u
v

:= zC = hd (zn, xCI) =

fxx + cx
fyy + cy

(11)
Where,
x = xn

1 + k1r2 + k2r4
+ 2p1xnyn + p2(r2 + 2x2
n)
(12)
y = yn

1 + k1r2 + k2r4
+ p1

r2 + 2y2
n

+ 2p2xnyn
(13)
r2 = x2
n + y2
n
(14)
xCI = (fx, fy, cx, cy, k1, k2, p1, p2)
(15)
intrinsic parameter xCI is obtained from [48]
Transformation of Euclidean (ht): To convert the 3D feature
position from the frame E coordinate system to the current
camera frame ck, we apply a 6DOF rigid-body Euclidean trans-
formation, which accounts for the current camera pose:
CkpF = ht

EpF , Ck
E R, EpCK

(16)
= Ck
E R(EpF −EpCk)
(17)
The camera pose (Ck
E R, EpCK) is described using the camera
extrinsic xCE = (C
I R, CpI) and the IMU pose (Ik
E R, EpIK):
Ck
E R = C
I RIk
E R
(18)
EpCK = EpIK + E
IkRIpC
(19)
MSCKF Update: For the MSCKF update [29], we linearize
the measurement function from the (4) at current state estimate
ˆxkandE ˆpF to obtain the following residual:
˜zC := zC −hC
	xk, EˆpF

(20)
≈HC ˜xk + HF
E˜pF + nC
(21)
Here HCk and HF represent the Jacobian matrix of the
function hc (·) corresponding to the current state estimate ˆxk
and other is estimated position for feature E ˆpF respectively.
z′C = H′Cxk + n′C
(22)
Next, we apply measurement compression following the
method outlined by [49]. This step signiﬁcantly reduces com-
putational complexity before the EKF update.
E. LiDAR
LGVINSutilizes anadaptationof thedirect alignment method
from [9] rather than extracting other like LOAM features. This

## Page 7

3982
IEEE TRANSACTIONS ON INTELLIGENT VEHICLES, VOL. 10, NO. 7, JULY 2025
approach enhances the efﬁciency and consistency of the up-
date process and introduces a mapping functionality. LiDAR
generates 3D point clouds representing the navigation environ-
ment. At time tk, a new point cloud is captured in the LiDAR
frame L.
Each point LkpF is transformed to the local map frame
M, where we then identify several neighboring points,Mpni =

xni
yni
zni
T
, i ∈1, ..., m. We calculate the plane M  =

a
b
c
T
, where the neighboring points are located as fol-
lows:
Am×3
⎧
⎪
⎨
⎪
⎩
⎡
⎢⎣
xn1
yn1
zn1
...
...
...
xnm
ynm
znm
⎤
⎥⎦
⎡
⎣
a
b
c
⎤
⎦= bm×1
⎧
⎪
⎨
⎪
⎩
⎡
⎢⎣
1
...
1
⎤
⎥⎦
(23)
The linear least-square solution is determined by M  =
(A⊺A)−1A⊺b. Upon ﬁnding the plane...M , we deﬁne the
following measurement for all planar points, encompassing
LkpF and Mpni :
zL :=
⎡
⎢⎢⎢⎣
0
...
0
0
⎤
⎥⎥⎥⎦= hL (xk) =
⎡
⎢⎢⎢⎣
MΠ⊤pn1 −1
...
MΠ⊤pnm −1
MΠ⊤pF −1
⎤
⎥⎥⎥⎦
(24)
The computation of MpF involves transforming LkpF into
the map frame utilizing the IMU-LiDAR extrinsic calibration
xL = (L
I R, LpI), the IMU pose (Ik
E R, EpIk), and the map pose
(M
E R, EpM):
MpF = M
E R
EpIk + E
IkR
IpL + I
LRLkpF

−EpM

(25)
For the EKF update, we linearize (24) and obtain the subse-
quent residual:
˜zL =
⎡
⎢⎢⎢⎣
−M ˆΠ⊤ˆpn1 + 1
...
−M ˆΠ⊤ˆpnm + 1
−M ˆΠ⊤ˆpF + 1
⎤
⎥⎥⎥⎦
(26)
≈HLxk + H M  + nL
(27)
where HL and H are the Jacobian matrix of HL (·) in respect
to the state xk and the plane M ; nL is noise as zero-mean
Gaussian. Now we possess subsequent measurement model,
which relies solely on the state and is prepared for the EKF
update:
z′L = H′Lxk + n′L
(28)
Please note that we also apply measurement compression
similarly to MSCKF-based VINS to enhance efﬁciency even
further.
F. GPS
A GPS receiver provide UAV position in a geodetic coordinate
frame. These information are commonly converted to a local
ENU or NED frame E for GPS based robot navigation purposes.
For instance, this conversion can be accomplished by designat-
ing the initial measurement location as the reference point or
by employing a base station. At time tk, a GNSS measurement
ZG represents the global position of the receiver EpGk. This
aspect can be represented using the IMU pose (Ik
E R, EpIk) and
the extrinsic calibration IpG:
zG = hG(xk) = EpGk + nG
(29)
= EpIk + IE
k RIpG + nG
(30)
where nG represents white Gaussian noise. Next, we linearize
this measurement for the EKF update:
zG := zG −hG(ˆxk) ≈HGˆxk + nG
(31)
Here HG represent hG (·) of the Jacobian matrix correspond-
ing to xk.
Considering that the measurement contains information about
the pose of sensor, Therefore it can be written as (X
E R, EpX),
We represent the measurement by incorporating the IMU
pose (Ik
E R, EpIk) and the corresponding extrinsic calibration
(X
I R, XpI):
zX :=
 Xk
E θ
EpXk

= hX(xk) =

log(X
I RIk
E R)
EpIk + IE
k RIpX

+ nX
(32)
Here nx denotes the zero-mean Gaussian noise. Finally, we
again linearize this global-pose measurement for the EKF up-
date:
zX := zX −hX(ˆxk) ≈HXxk + nX
(33)
Here Hx denotes the Jacobian matrix.
G. Coordinate Frames Navigation
The UAV’s state estimate requires translation of GPS data
by its body frame and correspond coordinate frame. The sensor
frame is connected to the sensors, acting as the local reference
frame where the sensor’s readings are reported. The LGVINS
typically includes sensor frame like IMU frame B, camera as
C, GPS as G and Lidar frame as L. We designate the IMU
frame as the target frame for estimation, referred to as the
LGVINS body frame, as shown in Fig. 3. To integrate GPS
coordinates, which are ECEF (Earth-Centered, Earth-Fixed)
frame, and navigation solution needs to be changed into the NED
(North-East-Down) coordinate system or ENU (East-North-Up)
frames. ECEF (Earth-Centered, Earth-Fixed) one of the Carte-
sian coordinate system that remains ﬁxed relative to the Earth,
centered at its center of mass.
The x-y plane is aligned with the equatorial plane of earth,
where x-axis points towards prime meridian. Furthermore, z-
axis is perpendicular to the equatorial plane, directed towards ge-
ographic North Pole and y-axis is oriented to maintain in ECEF
frame as right-hand coordinated. Here, we utilize the WGS84
realization from ECEF coordinated frame, depicted Fig. 3. To
establish a connection between the local and global ECEF frame,
and a semi-global called ENU (East-North-Up) is introduced. In
this study, we utilized ENU coordinate systems, adhering to the

## Page 8

IRFAN et al.: LGVINS: LiDAR-GPS-VISUAL AND INERTIAL SYSTEM BASED MULTI-SENSOR FUSION FOR SMOOTH
3983
Fig. 3.
An illustration of the local world, ECEF and ENU frames w.r.t UAV
and sensor body frame. Here N denotes ENU frame, E is the ECEF frame, W for
world frame, B is the IMU frame, G denotes the GPS frame, C for the camera
frame and L for the lidar frame.
ISO8855standardcommonlyusedintheautomotiveindustry.In
the ENU reference frame, the x-axis is oriented east, the y-axis
is oriented north, and the z-axis is oriented upward. An ENU
frame with a unique origin can be created for any point in the
ECEF frame. It is important to note that the alignment of the
frame ENU by z-axis corresponds to the direction of gravity. In
terms of time frames, GNSS data is documented in the GNSS
time system (such as GPS time), whereas VI measurements are
timestamped using the local time system. We proceed with the
assumption that these two time systems are pre-synchronized
and equivalent for the purposes of this research..
The following equation describes the conversion from the
ECEF frame to the ENU frame, aligning the local coordinate
system with the east, north, and up directions relative to the
observer:
⎡
⎣
xn
yn
zn
⎤
⎦=
⎡
⎣
cos λ
−sin λ
0
−sin Φ sin λ −sin Φ cos λ −cos Φ
cos Φ sin λ
cos Φ cos λ
−sin Φ
⎤
⎦
⎡
⎣
xe −x0
ye −y0
ze −z0
⎤
⎦
(34)
Where, λ is the longitude and Φ is called as the latitude origin
of frame.
IV. EXPERIMENTAL SETUP
To evaluate the performance of the proposed LGVINS fusion
algorithm, we ﬁrst tested with KAIST URBAN [45] public
dataset as well as our own dataset collected using integrated
UAV platform, as depicted in Fig. 4. The UAV is outﬁtted with a
range of onboard sensors that have been calibrated before being
used. The integrated sensors such as front facing stereo camera
with dual VGA 640x480 resolution publishes at 15 Hz along
withaGPS/RTKreceiverwhichpublishesat50Hz.Thisreceiver
connects to a differential station via Ethernet, providing both raw
GPS observations and RTK ground truth data. Additionally, we
integrated a 9-axis 400 Hz IMU module from a DJI drone onto
the front facing stereo to align the vision by the ENU coordinate
system of GPS. Two Livox M360 3D LiDAR’s are connected in
front and downward facing in order to acquire maximum number
of 3D points. Each of the LiDAR’s ROS pointcloud is obtained
Fig. 4.
LGVINS hardware integration setup on a UAV, SBC is a single board
onboard computer based on Nvidia NX, front stereo camera which is VGA
640x480 with 15 Hz, IMU and GPS/RTK are dji onboard sensors and two Livox
M360 3D LiDAR’s.
at 20Hz frequency. Table II. shows each hardware conﬁguration
used in the LGVINS UAV.
Moreover, to coordinate and multiple sensor synchronization,
data collection, we utilize ROS (Robot Operating System). ROS
is an open-source robotics solution tool [50] that facilitates
message-passing between processes and provides synchroniza-
tion utilities. All our datasets have been obtained using an
onboardcomputerbasedonNvidiaJetsonwithGPUsupportem-
bedded in the proposed UAV platform can be seen in the Fig. 4.
The corresponding dataset will be made available public for
the community. Three different dataset in rosbag format, which
can be accessed through https://github.com/mahammadirfan/
LGVINSLGVINS. This repository provide signiﬁcant insights
into the system’s performance and function as an important
resource for ongoing analysis,updates and research.
The ofﬂine calibration of this system comprises three com-
ponents: estimation of camera’s extrinsic/intrinsic parameters
and determination of IMU-camera exxtrinsic offset parameters,
for which we utilize the well-known Kalibr calibration tool-
box method [43] to estimate both the intrinsic and extrinsic
parameters of the stereo camera. Lastly, 3D LiDAR-IMU offset
calibration, we use latest popular toolbox LI-Init by [44] which
serves as a real-time initialization method for LiDAR-inertial
systems. This calibrates the temporal offset and extrinsic pa-
rameter between LiDARs and IMUs. To check the robustness
of the algorithm under different circumstances, we collected
multiple datasets in three scenario including both Handheld and
inﬂightUAVdataset.ThedatasetsarereferredasULCarBridge,
UL living bridge (Handheld UAV), UL Car Parking. Fig. 5.
represents the experimental environment in different scenario
during the data collection and the information of the dataset
used is presented in Table III. The results presented in this paper
were performed at the University of Limerick Campus of the
CRIS Lab research group.
V. RESULTS AND DISCUSSION
We perform and analyse the proposed LGVINS with pub-
lic and our real-world experiment datasets to verify the per-
formance. In this section, we conduct a comparison be-
tween LGVINS with the open-source algorithms such as
FASTLIO2 [9], VINS-FUSION with GPS [6], VINS-FUSION

## Page 9

3984
IEEE TRANSACTIONS ON INTELLIGENT VEHICLES, VOL. 10, NO. 7, JULY 2025
TABLE III
DATASET DETAILS
Fig. 5.
The experimental environment in different scenario during the data
collection.
without GPS [7] and Lvio-Fusion [22] to demonstrate its ef-
fectiveness. Furthermore, we perform in detail comparison of
LGVINS algorithm with its different sensor combination. We
only fuse the GPS position when it is in good health, by sub-
scribing to the DJI ROS SDK, we can monitor the number of
available GPS satellites during the ﬂight. Therefore, we have set
a minimum threshold of 11 satellite signals to ensure good GPS
health. LGVINS automatically use GPS position as per window
limit in order to fuse only optimum true position from GPS.
All the experiments have been performed without loop clo-
sure scenario to validate the proposed LGVINS global consis-
tency. All experiments in this section were performed using
a laptop equipped with an Intel Core(TM) i7-10750H CPU
@ 2.60 GHz processor running at 3.7 GHz and 32 GB of
RAM. We conducted a thorough numerical analysis to show-
case the consistency of proposed system and evaluated a de-
tailed comparison with four state-of-the-art methods: VINS-
FUSION (Stereo-inertial) [7] Fast-LIO2 [9], VINSFUSION
(Stereo-inertial-gps) [7] and Lvio-Fusion [22]. Additionally, we
opted exclusively for methods with open-source code availabil-
ity and are compatible with our developed LGVINS hardware
platform.
A. Evaluation Metrics
The mean error of the proposed multi-sensor fusion system is
a crucial validation metric which will validate the LGVINS state
Fig. 6.
The scenario of UL car bridge dataset. Panels (a) and (b) represent to
the datasets 3D point cloud map and google map, while panels (c) and (d) are
the bridge view from UAV.
estimation trajectory and poses to their actual positions as ob-
tained from the ground truth data RTK. The metric is considered
as the important indicator of the precision and accuracy of the
system. The most common formula such as RMSE are used to
calculate systems mean error. RMSE can be computed by taking
the root mean square and squared mean difference between the
estimated and ground truth values. This gives the metric which
represents the average magnitude of the error correspond to the
position estimate and the reference RTK position. The formula
for RMSE calculation is:
RMSE =



 1
n
n

i=1
(yi −ˆyi)2
(35)
where;
r yi is the actual value,
r n is the no. of observations,
r ˆyi is the predicted value,
r  represents the summation over all observations.
We utilize Absolute Pose Error (APE) as our accuracy metric
given by evo [51]. APE measures accuracy by directly compar-
ing the corresponding poses of the robot state trajectory and the
ground truth at identical timestamps. Then the whole trajectory
is uniﬁed for analysis, which is helpful for assessing the global
consistency of UAV trajectory.
B. UL car Bridge Dataset
The experiment takes place at the university of limerick car
bridge, ﬂying the drone under and above of the bridge envi-
ronment is displayed in the Fig. 6. The reference for LGVINS
is collected by RTK. The UAV ﬂight was done manually by
a trained pilot. We have performed this experiment without

## Page 10

IRFAN et al.: LGVINS: LiDAR-GPS-VISUAL AND INERTIAL SYSTEM BASED MULTI-SENSOR FUSION FOR SMOOTH
3985
TABLE IV
SUMMARY OF FINDINGS FROM ACCURACY EVALUATION ON UL CAR BRIDGE DATASET IN METERS
Fig. 7.
Trajectory plots of various methods on UAV car bridge dataset.
loop closing condition to validate the global consistency of
the LGVINS. The dataset environment involve acute ambient
illumination changes, agile movements and GPS degraded, as
depicted in Fig. 8, which are challenges for the VIO and LO
methods, where proposed LGVINS fusion method performed
well as compare with other SOTA methods. During the ex-
periment, most satellites consistently maintain a strong signal
lock, ensuring that the RTK status remains ﬁxed throughout
the entire route. However, while ﬂying under the bridge GPS
satellite number reached minimum to (11) satellite signal which
resulted in unstable GPS signal in challenging environment.
The proposed LGVINS fuses GPS position only if it is in good
health condition (enough satellite signal), otherwise LGVINS
deselect GPS position while only fuses other sensor combination
for state estimation. This experiment test the global consistency
of proposed LGVINS, in a challenging unstable and noisy gps
signal under the bridge environment, affecting the local UAV
state and smoothness of the trajectory. Figs. 7 and 8 represents
the LGVINS obtained trajectories along with other methods,
Table IV lists the RMSE of each method. This experiment
demonstrates that our system can achieve global consistency to
eliminate single sensor drifts while maintaining local smooth-
ness even under noisy GPS conditions.
Fig. 8 depicts the trajectory error plots and comparison gen-
erated by each methods. Trajectory error for vinsfusion [7] with
stereo-inertial is much more as compare to others. Vinsfusion
with no GPS [7] performs poorly because estimating UAV
pose solely through visual odometry is difﬁcult in challenging
environment like bridge inspection case and the motion of the
UAV also had an impact, as the drone occasionally underwent
almost purely rotational movements which can be seen in the
Fig. 7 Fastlio2 [9] was also resulting in signiﬁcant trajectory
drifts compare to ground truth as it only based with lidar-inertial
odometry. In contrast, LGVINS consisting of all the sensors
achieved the best performance.
When compare the LGVINS sensor combination, LGVINS
(Lidar+Imu+Stereo+GPS) performs well in bridge case sce-
nario. However, LGVINS (Lidar+Imu+GPS) and LGVINS (Li-
dar+Imu) comes in second and third place showing RMSE error
of 0.66 and 1.12 respectively. Hence, LGVINS with GPS fusion
perform the best in compare without GPS sensor combination.
Table IV provides a detailed evaluation of the translational
APE using the RMSE. The performance metric highlights the
percentage improvement in APE compared to other methods.
Table III. shows that proposed LGVINS outperforms all other
in UL car bridge dataset. Figs. 9 and 10 represents the absolute
positionerrorofx,y,zandroll,pitch,yawshowingplotsofvarious
methods on UAV car bridge dataset. Fig. 11 is the estimated
trajectory plot of the UAV car bridge dataset aligned well with
Google map. Fig. 12 depicts Box plot of overall RPE of the
seven strategies of UAV car bridge dataset showing LGVINS
performed well compared with other SOTA methods.
C. Handheld UAV Living Bridge Dataset
In this experiment, we utilized the same UAV custom-
designed sensor suite to showcase the capabilities of our frame-
work. The RTK position is treated as ground truth while with
good GPS signal recorded throughout the experiment. The
dataset has been collected using handheld UAV method while
walking around outdoor which encompass environments with
image degradation and structure-less surroundings, dynamic tar-
gets and unstable features which is challenging for vision-based
and lidar-based methods.
The experiment has been performed without loop closure
scenario to validate the consistency of the proposed LGVINS
approach and compared with RTK as reference data. Fig. 13
shows an overview of the environment. This experiment was
conducted in handheld UAV mode to eliminate the noise gen-
erated during ﬂight missions and validate the performance of
the proposed LGVINS in such scenarios. We performed state
estimation using LGVINS different sensor combinations as well

## Page 11

3986
IEEE TRANSACTIONS ON INTELLIGENT VEHICLES, VOL. 10, NO. 7, JULY 2025
Fig. 8.
Trajectory error plot for each method. Here, reference, L,I,S and G denotes RTK, lidar, IMU, stereo and GPS respectively.
Fig. 9.
Absolute position error of x,y,z axis showing plots of various methods
on UAV car bridge dataset.
Fig. 10.
Absolute position error of roll,yaw,pitch showing plots of various
methods on UAV car bridge dataset.
as other SOTA like VINSFUSION [7] and FASTLIO2 [9].
The plot shown in Fig. 14 trajectory obtained using different
methods, and the trajectory error comparison of various methods
is shown in Fig. 18. Table V illustrates the RMSE values for
the experiment of each method. Figs. 15 and 16 represents the
absolute position error of x,y,z and roll,pitch,yaw showing plots
of various methods on handheld UAV living bridge dataset.
It can be observed from the dataset experiment, signiﬁcant
position drifts were observed in the stereo-imu only scenario.
Fig. 11.
Estimated trajectory of the UAV car bridge dataset aligned well with
Google map.
Fig. 12.
Box plot of overall APE of the seven strategies of UAV car bridge
dataset.
However, the accuracy improved substantially with the assis-
tance of the Lidar or GPS or combination of all. VINS-Fusion’s
error plot continues to rise due to accumulated drift, whereas
LGVINS maintains a constant and smooth trajectory approach.
VINSFUSION [7] and Fast-LIO2 [9] do not accurately align
with the ground truth, whereas LGVINS demonstrated strong
performance across all three combinations.

## Page 12

IRFAN et al.: LGVINS: LiDAR-GPS-VISUAL AND INERTIAL SYSTEM BASED MULTI-SENSOR FUSION FOR SMOOTH
3987
TABLE V
SUMMARY OF FINDINGS FROM ACCURACY EVALUATION ON HANDHELD UAV LIVING BRIDGE DATASET IN METERS
Fig. 13.
The environments of the collected Handheld UAV dataset. Panels (a)
and (b) represent the datasets 3D point cloud map and google map, while panels
(c) and (d) are the drone view.
Fig. 14.
Trajectory plots of various methods on handheld UAV living bridge
dataset.
The experiment performed in varying illumination and
structure-less environment, presenting challenges for tracking
multiple visual features and matching geometric features. Nev-
ertheless, LGVINS method continue to perform well, as they
Fig. 15.
Relative position error of x,y,z axis showing plots of various methods
on handheld UAV living bridge dataset.
Fig. 16.
Relative position error of roll,yaw,pitch showing plots of various
methods on handheld UAV living bridge dataset.
Fig. 17.
Box plot of overall APE of the six strategies of handheld UAV living
bridge dataset.

## Page 13

3988
IEEE TRANSACTIONS ON INTELLIGENT VEHICLES, VOL. 10, NO. 7, JULY 2025
Fig. 18.
Trajectory error of various methods on handheld UAV living bridge dataset.
Fig. 19.
The scenario of the UL car parking collected dataset. Panels (a) and
(b) represent the 3D point cloud map and google map, while panels (c) and (d)
are the drone view.
effectively fuse data from camera, IMU, GPS and 3D LiDAR
or combination of any. The RMSE values of each LGVINS
combination are less compare to all the SOTA methods which is
displayed in the table. V. The trajectories displayed in Figs. 14
and 18 illustrate that following dataset, the trajectory obtained
by LGVINS(LSIG), LGVINS(SIG) and LGVINS(LSI) show
a signiﬁcant advantage over those produced by the VINSFU-
SION [7] and Fast-LIO2 [9] methods. These results suggest that
the LGVINS method improves UAV state estimation accuracy
compared to alternative algorithms and shows greater robustness
due to its capabilities. Fig. 17 shows that proposed method
outperforms all other in Handheld UAV living bridge dataset.
D. Car Parking Dataset
The car parking dataset environment includes open-air, tree-
shadowedenvironmentandacuteambientilluminationchanging
scenariocanbeseentheFig.19.Inthisexperiment,Evaluationof
the LGVINS approach has been conducted in an large-scale out-
door, open-air environment. The experiment has been performed
without loop closure condition to validate the consistency of
proposed LGVINS. In this car parking dataset, the UAV navigate
in a vast, open lawn with mostly few trees visible in the distance
with very bright and sunny environment, which is challenging
for stereo based approaches and most odometry fails and cannot
Fig. 20.
Trajectory plots of various methods on car parking dataset.
be effectively addressed by vision-based or LiDAR-based meth-
ods individually. Furthermore, While ﬂying above the parking
area, Most of the features detected by the LiDAR sensor were
located at ground level, leading to degraded motion estimation.
Therefore, it can be observe from the obtained trajectory plot
with respect to the ground truth RTK, FASTLO2 [9] produces a
signiﬁcant high errors due to Lidar degradation.
Similarly, VINSFUSION (stereo-inertial) performs worst as
compare to all others whereas noticeable position drifts oc-
curred in the VINSFUSION (stereo-imu-GPS) scenario. Ad-
ditionally, we observed that in the car parking open lawn
dataset, the features extracted from LiDAR were noticeably
sparse, resulting in reduced performance of the Lidar based
algorithms like FASTLIO2 [9]. Incontrast, proposed LGVINS
uses stereo,imu,Lidars and GPS, hence producing an improved
UAV state estimation and smooth trajectory in all challenging
scenarios. In all four sensor combination LGVINS performs
better and produces smooth trajectory state as compare to VINS-
FUSION [7] and FASTLIO2 [9] can be seen in the Fig. 20
and box plot in Fig. 23 and Table VI illustrate RMSE for
each method. We have compared all the sensor combination for

## Page 14

IRFAN et al.: LGVINS: LiDAR-GPS-VISUAL AND INERTIAL SYSTEM BASED MULTI-SENSOR FUSION FOR SMOOTH
3989
Fig. 21.
Trajectory Error plots of various methods on car parking dataset.
TABLE VI
SUMMARY OF FINDINGS FROM ACCURACY EVALUATION ON UAV CAR PARKING DATASET IN METERS
Fig. 22.
Absolute position error of roll, yaw, pitch showing plots of various
methods on car parking dataset.
Fig. 23.
Box plot of overall RPE of the seven strategies of car parking dataset.
LGVINSmethods,andfoundthatwiththecombinationoffusing
all sensor state, the accuracy improves in LGVINS hence the
estimated global pose produces smooth and consistent UAV state
estimation. Figs. 22 and 21 represents the absolute position error
TABLE VII
SUMMARY OF FINDINGS FROM ACCURACY EVALUATION ON KAIST URBAN
DATASET IN METERS
of roll,pitch,yaw and trajectory error showing plots of various
methods on car parking dataset respectively. Fig. 23 shows that
our method outperforms all other in UL car parking dataset.
E. KAIST Urban Dataset
The dataset [45] has been collected using a ground vehicle
in highly complex downtown environment including metropolis
areas, complex buildings and residential areas with movable fea-
tures. The presence of moving vehicles and pedestrians further
complicates the state estimation, making multi-sensor fusion
and global constraints even more critical. The device of kaist
urban dataset sensor includes a 100 Hz Xsens MTi-300 IMU,
two 10 Hz Pointgrey Flea3 stereo camera, two 10 Hz Velodyne
VLP-16 channel LiDARs. Kaist Urban Sequence 39 which is
the largest and most complex dataset (11 km) is used to evaluate
the proposed LGVINS.
The results of APE is summarize in Table VII. The efﬁciency
of the proposed approach is ultimately demonstrated by a nu-
merical study, using mean and RMSE. Based on different com-
bination of sensors are tested along with SOTA and the resulting
error trajectories of each algorithm are shown in Fig. 24. Fig. 26
depicts the obtained APE trajectory of proposed LGVINS in
kaist urban dataset. Overall, Fastlio2 (Lidars+IMU) and Vinsfu-
sion (stereo+IMU) showed scale issue and combining additional

## Page 15

3990
IEEE TRANSACTIONS ON INTELLIGENT VEHICLES, VOL. 10, NO. 7, JULY 2025
Fig. 24.
Trajectory error plot for each method on KAIST urban dataset. Here L,I,S and G denotes Lidar, IMU, stereo and GPS respectively.
Fig. 25.
The scenario of KAIST urban dataset. Panels (a) and (b) represent
to the datasets platform and google map, while panels (c) and (d) are the view
from KAIST sensor.
sensor was able to solve the problem. Note that Fastlio2 can fuse
only one LiDAR sensor which showed poor performance on the
KAIST dataset due to its limited overlapping points between the
LiDAR scans. The key issue for poor performance is likely the
lack of overlapping point clouds between the map and the new
scan, resulting in a poorly deﬁned ICP problem. The Vinsfusion
methods using stereo-inertial only initialized successfully, but
their performances were largely drifted by the dynamic objects
present in Kaist seq 39. (see an exemplary case in Fig. 25.
VINS-Fusion with adding a GPS sensor combination and Lvio-
Fusion using all sensors failed to provide consistent estimates
on kaist datasets, even when GPS global position was available,
due to their loosely coupled approach. This occurs because the
Fig. 26.
Proposed LGVINS on KAIST urban dataset.
VIO sub-system of VINS-Fusion and the LIO sub-system of
Lvio-Fusion (stereo+Lidar+IMU+GPS) struggled with initial-
ization and dynamic objects present in kaist dataset, which led
to inconsistent odometry data being fed into the pose graph. This
caused global estimation to become highly unreliable, ultimately
resulting in worse performance than relying solely on GPS data.
In contrast, proposed LGVINS-Fusion integrated GPS data with
other sensors in a tightly coupled manner, enabling the state
estimation to effectively limit its drift, resulting in globally
accurate and locally precise performance.
VI. CONCLUSION
The multi sensor fusion algorithms to improve the UAV/UGV
state estimation have been proposed in this work. The accu-
racy and effectiveness of the proposed LGVINS were validated
through real-world experiments and public dataset, which in-
cluded challenging dataset collection using our UAV equipped

## Page 16

IRFAN et al.: LGVINS: LiDAR-GPS-VISUAL AND INERTIAL SYSTEM BASED MULTI-SENSOR FUSION FOR SMOOTH
3991
with an integrated hardware platform across a range of scenar-
ios. Experiments have demonstrated that the proposed fusion
technique can optimize UAV state estimation, resulting in an
improved, robust and accurate state in GPS degraded environ-
ment under multiple use case. The aiding of an GPS along with
onboard IMU fused with stereo/LiDAR odometry data can min-
imize growing GPS errors and can bridge even long GPS signal
outages. Experiments conducted across diverse environments
show that the proposed LGVINS method consistently outper-
forms other methods such as VINSFUSION (stereo-inertial,
VINSFUSION (stereo-inertial-GPS) and FastLIO2, algorithms
and achieve high state estimation accuracy and robustness in
challenging environments, including those with bridge case,
open air or poor lighting or no structure. Furthermore, Proposed
LGVINS demonstrated and evaluated on KAIST Urban chal-
lenging dataset which outperform SOTA methods.
Future work could investigate using even larger, more di-
verse dataset adding sensors like radar sensor. However, the
accuracy of IMU-based odometry can degrade over time due
to the accumulation of errors. In contrast, radar sensors are
emerging as a promising alternative for state estimation and
SLAM (Simultaneous Localization and Mapping) because of
their robustness against adverse ambient illumination condition
and complex environmental structures. Despite this potential,
the challenge of identifying reliable RADAR/LiDAR sensors
remains an unresolved issue. Therefore, we would like to inves-
tigate LGVINS by adding more sensors in future.
REFERENCES
[1] C. Cadena et al., “Past, present, and future of simultaneous localization and
mapping: Toward the robust-perception age,” IEEE Trans. Robot., vol. 32,
no. 6, pp. 1309–1332, Dec. 2016.
[2] T. Wang, Y. Su, S. Shao, C. Yao, and Z. Wang, “GR-Fusion: Multi-sensor
fusion slam for ground robots with high robustness and low drift,” in Proc.
IEEE/RSJ Int. Conf. Intell. Robots Syst., 2021, pp. 5440–5447.
[3] S. Dorafshan and M. Maguire, “Bridge inspection: Human performance,
unmanned aerial systems and automation,” J. Civil Struct. Health Monit.,
vol. 8, pp. 443–476, 2018.
[4] T. Qin, J. Pan, S. Cao, and S. Shen, “A general optimization-based
framework for local odometry estimation with multiple sensors,” 2019,
arXiv:1901.03638.
[5] M. Rossi, P. Trsli´c, S. Sivˇcev, J. Riordan, D. Toal, and G. Dooly, “Real-time
underwater stereofusion,” Sensors, vol. 18, no. 11, 2018, Art. no. 3936.
[6] S.Cao,X.Lu,andS.Shen,“GVINS:TightlycoupledGNSS-visual-inertial
fusion for smooth and consistent state estimation,” IEEE Trans. Robot.,
vol. 38, no. 4, pp. 2004–2021, Aug. 2022.
[7] T. Qin, P. Li, and S. Shen, “VINS-Mono: A robust and versatile monoc-
ular visual-inertial state estimator,” IEEE Trans. Robot., vol. 34, no. 4,
pp. 1004–1020, Aug. 2018.
[8] P. Geneva, K. Eckenhoff, W. Lee, Y. Yang, and G. Huang, “OpenVINS: A
research platform for visual-inertial estimation,” in Proc. IEEE Int. Conf.
Robot. Automat., 2020, pp. 4666–4672.
[9] W. Xu, Y. Cai, D. He, J. Lin, and F. Zhang, “FAST-LIO2: Fast di-
rect LiDAR-inertial odometry,” IEEE Trans. Robot., vol. 38, no. 4,
pp. 2053–2073, Aug. 2022.
[10] G. Huang, “Visual-inertial navigation: A concise review,” in Proc. Int.
Conf. Robot. Automat., 2019, pp. 9572–9582.
[11] K. Ebadi et al., “Present and future of SLAM in extreme environments:
The DARPA SubT challenge,” IEEE Trans. Robot., vol. 40, pp. 936–959,
2024.
[12] A. R. Sahili et al., “A survey of visual SLAM methods,” IEEE Access,
vol. 11, pp. 139643–139677, 2023.
[13] N. J. Abu-Alrub and N. A. Rawashdeh, “Radar odometry for autonomous
ground vehicles: A survey of methods and datasets,” IEEE Trans. Intell.
Veh., vol. 9, no. 3, pp. 4275–4291, Mar. 2024.
[14] D. Lee, M. Jung, W. Yang, and A. Kim, “LiDAR odometry survey: Recent
advancements and remaining challenges,” Intell. Serv. Robot., vol. 17,
pp. 95–118, 2024.
[15] M. Irfan, K. Kishore, and V. A. Chhabra, “Smart vehicle management
system using Internet of Vehicles (IoV),” in Proc. Int. Conf. Adv. Comput.
Appl., 2022, pp. 73–83.
[16] M. Irfan, S. Dalai, K. Kishore, S. Singh, and S. A. Akbar, “Vision-based
guidance and navigation for autonomous MAV in indoor environment,” in
Proc. 11th Int. Conf. Comput., Commun. Netw. Technol., 2020, pp. 1–5.
[17] S. Singh et al., “CACLA-based local path planner for drones navigating
unknown indoor corridors,” IEEE Intell. Syst., vol. 37, no. 5, pp. 32–41,
Sep./Oct. 2022.
[18] W. Lee, P. Geneva, Y. Yang, and G. Huang, “Tightly-coupled GNSS-aided
visual-inertial localization,” in Proc. Int. Conf. Robot. Automat., 2022,
pp. 9484–9491.
[19] X. Meng, H. Wang, and B. Liu, “A robust vehicle localization approach
based on GNSS/IMU/DMI/LiDAR sensor fusion for autonomous vehi-
cles,” Sensors, vol. 17, no. 9, 2017, Art. no. 2140.
[20] K. Hausman, S. Weiss, R. Brockers, L. Matthies, and G. S. Sukhatme,
“Self-calibrating multi-sensor fusion with probabilistic measurement val-
idation for seamless sensor switching on a UAV,” in Proc. IEEE Int. Conf.
Robot. Automat., 2016, pp. 4289–4296.
[21] V. Kubelka, L. Oswald, F. Pomerleau, F. Colas, T. Svoboda, and
M. Reinstein, “Robust data fusion of multimodal sensory informa-
tion for mobile robots,” J. Field Robot., vol. 32, no. 4, pp. 447–473,
2015.
[22] Y. Jia et al., “Lvio-fusion: A self-adaptive multi-sensor fusion SLAM
framework using actor-critic method,” in Proc. IEEE/RSJ Int. Conf. Intell.
Robots Syst., 2021, pp. 286–293.
[23] T.-M. Nguyen, S. Yuan, M. Cao, T. H. Nguyen, and L. Xie, “Vi-
ral SLAM: Tightly coupled camera-IMU-UWB-LiDAR SLAM,” 2021,
arXiv:2105.03296.
[24] S. Leutenegger, A. Forster, P. Furgale, P. Gohl, and S. Lynen, “OKVIS:
Open keyframe-based visual-inertial SLAM (RoS version),” 2016.
[25] Q. Li et al., “LO-Net: Deep real-time LiDAR odometry,” in Proc.
IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2019, pp. 8473–8482.
[26] A.Kendall,M.Grimes,andR.Cipolla,“PoseNet:Aconvolutionalnetwork
for real-time 6-DoF camera relocalization,” in Proc. IEEE Int. Conf.
Comput. Vis., 2015, pp. 2938–2946.
[27] A. Sherstinsky, “Fundamentals of recurrent neural network (RNN) and
long short-term memory (LSTM) network,” Physica D: Nonlinear Phe-
nomena, vol. 404, 2020, Art. no. 132306.
[28] Q. Jia, G. Luo, Q. Yuan, J. Li, C. Shao, and Z. Chen, “MS-transformer:
Masked and sparse transformer for point cloud registration,” in Proc. IEEE
Int. Conf. Syst., Man, Cybern., 2023, pp. 1375–1381.
[29] A. I. Mourikis and S. I. Roumeliotis, “A multi-state constraint Kalman
ﬁlter for vision-aided inertial navigation,” in Proc. 2007 IEEE Int. Conf.
Robot. Automat., 2007, pp. 3565–3572.
[30] L. Han, Y. Lin, G. Du, and S. Lian, “Deepvio: Self-supervised deep learn-
ing of monocular visual inertial odometry using 3D geometric constraints,”
in Proc. IEEE/RSJ Int. Conf. Intell. Robots Syst., 2019, pp. 6906–6913.
[31] M. Bloesch, S. Omari, M. Hutter, and R. Siegwart, “Robust visual inertial
odometry using a direct EKF-based approach,” in Proc. IEEE/RSJ Int.
Conf. Intell. robots Syst., 2015, pp. 298–304.
[32] J. Simanek, V. Kubelka, and M. Reinstein, “Improving multi-modal data
fusion by anomaly detection,” Auton. Robots, vol. 39, no. 2, pp. 139–154,
2015.
[33] J. K. Suhr, J. Jang, D. Min, and H. G. Jung, “Sensor fusion-based low-cost
vehicle localization system for complex urban environments,” IEEE Trans.
Intell. Transp. Syst., vol. 18, no. 5, pp. 1078–1086, May 2017.
[34] S. Lynen, M. W. Achtelik, S. Weiss, M. Chli, and R. Siegwart, “A robust
and modular multi-sensor fusion approach applied to MAV navigation,”
in Proc. IEEE/RSJ Int. Conf. Intell. Robots Syst., 2013, pp. 3923–3929.
[35] C. Merfels and C. Stachniss, “Pose fusion with chain pose graphs for
automated driving,” in Proc. IEEE/RSJ Int. Conf. Intell. Robots Syst., 2016,
pp. 3116–3123.
[36] R.Mascaro,L.Teixeira,T.Hinzmann,R.Siegwart,andM.Chli,“GOMSF:
Graph-optimization based multi-sensor fusion for robust UAV pose esti-
mation,” in Proc. IEEE Int. Conf. Robot. Automat., 2018, pp. 1421–1428.
[37] S. Han, F. Deng, T. Li, and H. Pei, “Tightly coupled optimization-based
GPS-visual-inertial odometry with online calibration and initialization,”
2022, arXiv:2203.02677.
[38] B. Dong and K. Zhang, “A tightly coupled visual-inertial GNSS state
estimator based on point-line feature,” Sensors, vol. 22, no. 9, 2022,
Art. no. 3391.

## Page 17

3992
IEEE TRANSACTIONS ON INTELLIGENT VEHICLES, VOL. 10, NO. 7, JULY 2025
[39] J. Liu, W. Gao, and Z. Hu, “Optimization-based visual-inertial SLAM
tightly coupled with raw GNSS measurements,” in Proc. IEEE Int. Conf.
Robot. Automat., 2021, pp. 11612–11618.
[40] W. Lee, P. Geneva, C. Chen, and G. Huang, “Mins: Efﬁcient and robust
multisensor-aided inertial navigation system,” 2023, arXiv:2309.15390.
[41] S. Zhao, H. Zhang, P. Wang, L. Nogueira, and S. Scherer, “Super
odometry: IMU-centric LiDAR-visual-inertial estimator for challenging
environments,” in Proc. IEEE/RSJ Int. Conf. Intell. Robots Syst., 2021,
pp. 8729–8736.
[42] J. Lin and F. Zhang, “R 3 live: A robust, real-time, RGB-colored, LiDAR-
inertial-visual tightly-coupled state estimation and mapping package,” in
Proc. Int. Conf. Robot. Automat., 2022, pp. 10672–10678.
[43] J.Rehder,J.Nikolic,T.Schneider,T.Hinzmann,andR.Siegwart,“Extend-
ing Kalibr: Calibrating the extrinsics of multiple IMUs and of individual
axes,” in Proc. IEEE Int. Conf. Robot. Automat., 2016, pp. 4304–4311.
[44] F. Zhu, Y. Ren, and F. Zhang, “Robust real-time LiDAR-inertial initializa-
tion,” in Proc. IEEE/RSJ Int. Conf. Intell. Robots Syst., 2022, pp. 3948–
3955.
[45] J. Jeong, Y. Cho, Y.-S. Shin, H. Roh, and A. Kim, “Complex urban dataset
with multi-level sensors from highly diverse urban environments,” Int. J.
Robot. Res., vol. 38, no. 6, pp. 642–657, 2019.
[46] N. Trawny and S. I. Roumeliotis, “Indirect Kalman ﬁlter for 3D attitude
estimation,” Dept. Comput. Sci. & Eng., Univ. Minnesota, Minneapolis,
MN, USA, Tech. Rep. 2005-002, 2005.
[47] J. A. Hesch, D. G. Kottas, S. L. Bowman, and S. I. Roumeliotis,
“Observability-constrained vision-aided inertial navigation,” Dept. of
Comput. Sci. & Eng., MARS Lab, Univ. of Minnesota, Minneapolis, MN,
USA, Tech. Rep. 2012-001, 2012.
[48] J. Kannala and S. S. Brandt, “A generic camera model and calibration
method for conventional, wide-angle, and ﬁsh-eye lenses,” IEEE Trans.
Pattern Anal. Mach. Intell., vol. 28, no. 8, pp. 1335–1340, Aug. 2006.
[49] G. H. Golub and C. F. Van Loan, Matrix Computations. Baltimore, MD,
USA: Johns Hopkins Univ. Press, 2013.
[50] A. Koubâa et al. Robot Operating System (ROS), vol. 1. Berlin, Germany:
Springer, 2017.
[51] M. Grupp, “EVO: Python package for the evaluation of odometry and
SLAM,” 2017. [Online]. Available: https://github.com/MichaelGrupp/evo
Mahammad Irfan (Graduate Student Member,
IEEE) received Bachelor of Technology degree in
electrical and electronics engineering from S’O’A
University, Bhubaneswar, Odisha, in 2015, India,
and the Master of Technology degree in electronics
engineering from the Punjab Technical University,
Punjab,India,in2018.Heiscurrentlyworkingtoward
Ph.D. degree in electronics and computer engineering
with the University of Limerick, Limerick, Ireland.
He is also a Member with the Centre for Robotics
and Intelligent Systems (CRIS). His research interests
include SLAM system, UAV State Estimation, Sensor Fusion, and autonomous
UAV navigation and perceptiom.
Sagar Dalai (Graduate Student Member, IEEE) is
currently working toward the Ph.D. degree with
the Centre of Robotics and Intelligent Systems
(CRIS) Group, University of Limerick, Limer-
ick, Ireland. He received the Bachelor of Tech-
nology
degree
in
electronics
and
telecommu-
nication
from
the
Biju
Patnaik
University
of
Technology (BPUT), Odisha, India. His research in-
terests include hyperspectral image processing, si-
multaneous localization and mapping (SLAM), and
path planning algorithms, leveraging advanced imag-
ing, AI techniques to enhance environmental monitoring, and autonomous
systems.
Petar Trslic received the B.Sc. and M.Sc. degrees
in mechanical engineering from the University of
Zagreb, Zagreb, Croatia, and the Ph.D. degree from
the University of Limerick (UL), Limerick, Ireland,
in March 2020. He is currently a Postdoctoral Re-
searcher with CRIS, UL. During the Ph.D. degree,
he was working on the development of advanced
monitoring, control systems and onboard robotics
for the automation of MRE inspection, repair, and
maintenance.
Matheus C. Santos (Member, IEEE) received the
bachelor’s degree in computer engineering and the
master’s degree in electrical engineering from the
Federal University of Sergipe (UFS), State of Sergipe,
Brazil, in 2019 and 2021, respectively. He is currently
working toward the Ph.D. degree in electrical engi-
neering with the University of Limerick. He is also
a member of the Centre of Robotics and Intelligent
Systems (CRIS) and the Robotics Research Group
(GPR), UFS.
James Riordan received the B.Eng. degree in elec-
tronic engineering specialising in aircraft simulation
systems, and the Ph.D. degree in real-time processing
of acoustic signals from the University of Limerick,
Limerick, Ireland, respectively. He is currently a Full
Professor with the University of the West of Scot-
land, Glasgow, U.K., where he is also the Director
with Drone Systems Laboratory. He is a Principal
Investigator of multiple research projects funded by
the European Commission and U.K. Research and
Innovation. His research interests include artiﬁcial
intelligence, computer vision, and sensing methods to extend the safe and
sustainable application of autonomous vehicles in land, air, and sea.
Gerard Dooly (Member, IEEE) received the B.Eng.
degree from the Electronic and Computer Engineer-
ing Department, University of Limerick (UL), Lim-
erick, Ireland, in 2003, and the Ph.D. degree from
the Optical Fibre Sensors Research Centre, UL, in
2008, based on the topic “An Optical Fibre Sensor
for the Measurement of Hazardous Emissions from
LandTransportVehicles,”.Hehasworkedextensively
in ﬁeld robotics with UL for more than ten years.
His research interests include real-time 3-D recon-
struction, machine vision, machine learning, optical
ﬁbre sensors, subsea structural health monitoring, teleoperation, and automated
docking and intervention. He is involved in robotics for harsh environments
in offshore setting and is developing systems to address beyond visual line of
sight operations for UAS. He is also focused on the design and development of
robotics and has engaged in numerous ﬁeld operations and survey missions both
in Ireland and on the continent. Some of his recent offshore operations involved
environmentalsensing,anti-minecountermeasureOPS,remoteUASforincident
response, archaeological survey, and hybrid long range UAS technologies.
