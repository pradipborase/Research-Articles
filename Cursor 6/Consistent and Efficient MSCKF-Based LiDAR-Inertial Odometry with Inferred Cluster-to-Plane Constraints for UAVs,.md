# Consistent and Efficient MSCKF-Based LiDAR-Inertial Odometry with Inferred Cluster-to-Plane Constraints for UAVs,.pdf

## Page 1

Consistent and Efficient MSCKF-based LiDAR-Inertial Odometry with
Inferred Cluster-to-Plane Constraints for UAVs
Jinwen Zhu†∗, Xudong Zhao†∗, Fangcheng Zhu†, Jun Hu†, Shi Jin†, Yinian Mao†, Guoquan Huang‡
Abstract— Robust and accurate navigation is critical for
Unmanned Aerial Vehicles (UAVs) especially for those with
stringent Size, Weight, and Power (SWaP) constraints. However,
most state-of-the-art (SOTA) LiDAR-Inertial Odometry (LIO)
systems still suffer from estimation inconsistency and computa-
tional bottlenecks when deployed on such platforms. To address
these issues, this paper proposes a consistent and efficient
tightly-coupled LIO framework tailored for UAVs. Within
the efficient Multi-State Constraint Kalman Filter (MSCKF)
framework, we build coplanar constraints inferred from planar
features observed across a sliding window. By applying null-
space projection to sliding-window coplanar constraints, we
eliminate the direct dependency on feature parameters in the
state vector, thereby mitigating overconfidence and improving
consistency. More importantly, to further boost the efficiency,
we introduce a parallel voxel-based data association and a novel
compact cluster-to-plane measurement model. This compact
measurement model losslessly reduces observation dimensional-
ity and significantly accelerating the update process. Extensive
evaluations demonstrate that our method outperforms most
state-of-the-art (SOTA) approaches by providing a superior
balance of consistency and efficiency. It exhibits improved
robustness in degenerate scenarios, achieves the lowest memory
usage via its map-free nature, and runs in real-time on resource-
constrained embedded platforms (e.g., NVIDIA Jetson TX2).
I. INTRODUCTION
Robust, accurate, and efficient state estimation is prereq-
uisite for Unmanned Aerial Vehicles (UAVs), particularly
in safety-critical applications such as commercial drone
delivery [1]. Valued for its immunity to lighting variations
and precise ranging, LiDAR has become a primary sensor
for autonomous aerial navigation. While LiDAR provides
precise ranging, deploying LiDAR-Inertial Odometry (LIO)
on UAVs is challenged by stringent Size, Weight, and
Power (SWaP) constraints. Currently, the Error-State Iterated
Kalman Filter (ESIKF) framework (e.g., FAST-LIO2 [2],
Super-LIO [3]) dominates due to its impressive efficiency.
However, these methods fundamentally rely on a global
map treated as a fixed prior. This architecture theoretically
presents a critical limitation: inconsistency. By treating the
estimated map as a fixed prior with independent noise, these
approaches neglect the cross-correlations between the current
state and the map. This leads to “over-confidence”, where the
estimated uncertainty is significantly lower than the actual
error [4].
In contrast, the Multi-State Constraint Kalman Filter
(MSCKF) framework [5]—along with consistent treatments
∗Equal contribution.
†Meituan UAV, Beijing, China (e-mail: {zhaoxudong09, zhujinwen,
zhufangcheng, hujun11, jinshi02, maoyinian}@meituan.com).
‡Dept. of Mechanical Engineering, Computer and Information Sci-
ences, University of Delaware, Newark, DE (email: ghuang@udel.edu).
such as First-Estimate Jacobian (FEJ) [6], [7]—offers a con-
sistent alternative by exploiting relative constraints within a
sliding window. However, standard MSCKF implementations
such as LINS [8] still suffer from computational bottlenecks
due to the state vector growing with the window size and
the processing of massive LiDAR measurements.
To address these challenges, we propose a consistent
and efficient LIO system tailored for resource-constrained
platforms, e.g., UAVs. Our contributions are threefold:
• To ensure consistency, we propose a tightly-coupled
map-free MSCKF-based LIO. By marginalizing features
via null-space projection, we avoid the over-confidence
of ESIKF methods, yielding accurate and consistent
estimates.
• Aiming for computational efficiency, we design a paral-
lel, adaptive voxel-based data association coupled with
a novel, compact cluster-to-plane measurement model.
This formulation losslessly reduces the observation di-
mension by more than 85%, effectively resolving the
efficiency bottleneck of traditional LIO .
• We perform extensive validation in simulations and
real-world flights, showing that our method achieves
superior consistency compared to SOTA approaches
and real-time capability with extremely efficient memory
usage, even running on severely resource-constrained
computers (e.g., NVIDIA Jetson TX2).
The remainder of this paper is organized as follows:
After reviewing the related work, we present the system
formulation in Section III. Section IV details the proposed
parallelized voxelization and efficient MSCKF update with
inferred cluster-to-plane measurements. Extensive validation
through simulations and real-world experiments is provided
in Sections V and Section VI. Finally, Section VII concludes
the proposed framework and discusses the future work.
II. RELATED WORK
The field of LiDAR-Inertial Odometry (LIO) and SLAM
has witnessed a proliferation of high-performance systems
in recent years. These can be broadly categorized into
optimization-based and filtering-based approaches.
The optimization-based paradigm, which relies on it-
erative error minimization, includes seminal works like
LOAM [9]. LOAM pioneered real-time odometry through
efficient plane-edge feature matching. Building on this, LIO-
SAM [10] employs a factor graph to tightly fuse IMU
pre-integration with keyframe scan-matching for enhanced
robustness. More recently, SR-LIO [11] attempts to better
handle motion distortion via sweep reconstruction. Other

## Page 2

lightweight variations like CT-ICP [12] extend these concepts
to continuous-time trajectory estimation. FF-LINS [13] pro-
posed a frame-to-frame LiDAR-inertial state estimator under
factor graph optimization framework meanwhile maintaining
consistency.
Conversely, filtering-based methods sequentially update
the state estimate within a recursive framework, often pri-
oritizing computational efficiency. LINS [8] integrates IMU
and LiDAR data using an Iterated Extended Kalman Filter
(IEKF). The field was significantly advanced by the FAST-
LIO family [2], [14]–[16]: FAST-LIO [14] reformulated the
Kalman gain to depend on the measurement dimension, and
FAST-LIO2 [2] introduced the ikd-tree for efficient map
management. To further reduce computational load, Faster-
LIO [15] employs parallel sparse incremental voxels, and iG-
LIO [17] leverages an incremental GICP-based frontend to
accelerate the update process. VoxelMap [4] further improves
accuracy by using adaptive voxels to incrementally update
local map planes with uncertainty modeling.
However, a critical limitation of many high-performance
ESIKF systems (including [2], [4], [17], [18]) is their fail-
ure to maintain a theoretically correct uncertainty measure.
These methods typically treat the global map as a pre-built,
fixed reference with independent noise. This assumption
neglects the cross-correlations between the current state and
the map, leading to “over-confidence”, where the estimated
covariance fails to reflect the true error growth.
A recent line of work has focused explicitly on resolving
this inconsistency. Methods like MINS [19] and Puma-
LIO [20] achieve consistency by using null-space projection
to reformulate point-to-plane residuals as relative constraints
between frames, effectively removing the dependency on
a global map. The MSCKF framework, renowned for its
efficiency and consistency in visual-inertial odometry, has
also been adapted for LIO. LIC-FUSION [21] utilizes this
framework but relies on single-frame feature extraction,
leading to fragile result in sparse environments. Although
recent works like MSC-LIO [22] and BA-LINS [23] also
employ MSCKF for consistent estimation, their data as-
sociation typically involves expensive neighbor searches.
This process leads to a computational bottleneck in large-
scale environments, hindering their deployment on SWaP-
constrained platforms. Our work addresses this specific gap
by introducing an adaptive voxel-aided LIO with cluster-
to-plane measurement model under MSCKF framework that
ensures both consistency and extreme efficiency.
III. SYSTEM OVERVIEW
In this section, we briefly describe the problem formu-
lation within a sliding-window MSCKF framework, and
provide an overview of the proposed consistent and efficient
LIO system as shown in Fig. 1.
Within the efficient MSCKF framework [5], [7], IMU is
used to propagate the state estimates and covariance, and
LiDAR measurements are used for update. The state vector
of MSCKF framework includes n cloned IMU poses xCi
(i = 1, · · · , n) and the current IMU navigation states xI:
Framework Overview
IMU Data
LiDAR Points
State and Covariance 
Propagation
MSCKF Update 
& Marginalization
Points Undistortion 
& State Augmentation
Prior State
Multi-frame Data 
Association
Cluster to Plane 
Measurement Model
Residuals
Odometry
Fig. 1: System diagram of the proposed MSCKF-based LIO.
xT
k =
[︁
xT
C1
· · ·
xT
Cn
xT
Ik
]︁
(1)
=
[︁
xT
C1
· · ·
xT
Cn
GpT
Ik
GqT
Ik
GvT
Ik
bT
gk
bT
ak
]︁
where xT
Ci = [GqT
Ci,G pT
Ci], represents the rotation and
position corresponding to the i-th cloned IMU pose,
GpI,G qI,G vI are the position, rotation (unit quaternion)
and velocity of current IMU state expressed in the global
frame, and bg and ba are the gyroscope and accelerometer
biases, respectively.
When a new IMU reading is available, we use the ac-
celeration and angular velocity measurements to propagate
the IMU navigation state based on the inertial kinematic
model [24]:
xk = f(xk−1, am,k−1, ωm,k−1, nk−1)
(2)
where am, ωm is the measurement of acceleration and an-
gular velocity, n is noise of the IMU measurement, which
includes white Gaussian noise and random walk bias noise.
The state estimate propagates from k−1 to k is as follows:
ˆxk|k−1 = f(ˆxk−1|k−1, am,k−1, ωm,k−1, 0)
(3)
On the other hand, the covariance Pk|k−1 is propagated
based on the linearized IMU kinematic model of (2):
Pk|k−1 = Φk−1Pk−1|k−1Φ⊤
k−1 + Qk−1
(4)
where Φk−1 is the system Jacobian and Qk−1 is the discrete-
time noise covariance.
When a new LiDAR pointcloud measurement becomes
available, we utilize the IMU propagation to obtain the prior
state estimate. To perform the MSCKF-based sliding window
update, we clone the IMU pose xCi [see (1)] corresponding
to the current LiDAR time and augment the state and
covariance (i.e., stochastic cloning).
Given the substantial volume of LiDAR data, directly pro-
cessing raw points is computationally prohibitive. Therefore,
we pass the accumulated point clouds and the augmented
states to our proposed efficient state and covariance update
with our compact cluster-to-plan constraints inferred from
LiDAR measurements, as explained in next section.
IV. EFFICIENT MSCKF UPDATE WITH INFERRED
CLUSTER-TO-PLANE CONSTRAINTS
To achieve highly efficient state estimation on SWaP-
constrained UAVs, this section details our voxel-aided

## Page 3

MSCKF pipeline. We first aggregate multi-frame point
clouds in the sliding-window via parallel voxelization for
planar patch extraction (Section IV-A). Next, we derive
a lossless cluster-to-plane model to significantly compress
the observation dimensionality (Section IV-B). Finally, we
utilize MSCKF null-space projection to marginalize out these
features (Section IV-C). This formulation yields rigorous
geometric constraints while bypassing the need to maintain
feature states, guaranteeing both computational efficiency
and theoretical consistency.
A. Plane Patches in Voxels
Given a window of LiDAR cloud points, we first effi-
ciently and adaptively extract planes by leveraging voxels. It
is important to note that accurate plane fitting and tracking
is not our purpose, whereas we use these plane patches as
an intermediate step to help find proper point-on-plane mea-
surements to constrain motion. To this end, leveraging the
prior IMU/LiDAR pose estimates {GpLk, GRLk}, we first
transform the point cloud {Lkpi} of each frame {Lk} in the
window to the global frame {G}: Gpi = GpLk+GRLk
Lkpi.
Once all the LiDAR points of all the frames in the window
are transformed into the global frame, we partition them
into voxels with certain resolutions informed by operation
conditions; for example, a fixed resolution of 3m for high-
altitude flights was found to be reasonable in our case. For
fast retrieval, each i-th voxel is indexed by its integer grid
coordinates, denoted by Vi = (xidx, yidx, zidx). As a result,
each LiDAR frame at time k has a set of N associated
voxels (or voxel-map): Vk = {Vi, GPi, Ci, LkPi}N
i=1, where
LkPi is the point cloud of the i-th voxel and consists of
the n raw points LkPi = {Lkpj}n
j=1 from the frame k and
the corresponding transformed points into the global frame
GPi = {Gpj}n
j=1, along with the corresponding point cluster
Ci which is a 4 × 4 symmetric matrix defined as [25]:
Ci =
n
∑︂
j=1
[︃Gpj
1
]︃[︁GpT
j
1
]︁
=
[︃P
v
vT
n
]︃
∈S4×4
(5)
where P = ∑︁n
j=1
GpjGpT
j and v = ∑︁n
j=1
Gpj.
Now, for the voxel-map Vk at time k, we retrieve all the
frames in the current sliding window that contain the same
voxel Vi, and then aggregate the corresponding point clusters
Cℓfrom the matching voxels across frames: C′
i = Ci + Cℓ,
by leveraging the additive property of the point clusters [see
(5)]. For the aggregated cluster C′
i, we efficiently extract
planar features via adaptive plane fitting for the ensuing
construction of point-on-plane constraints.
Instead of probabilistic plane fitting (via least squares), we
efficiently extract planes by performing eigen-decomposition
of the 3 × 3 covariance matrix of 3D point cloud of the i-th
cluster C′
i of the voxel Vi [see (5)]:
cov(C′
i)
(5)= 1
nP −1
n2 vvT eig.
= U
⎡
⎣
λ1
0
0
0
λ2
0
0
0
λ3
⎤
⎦U⊤
(6)
where the eigenvalues λ1 ≥λ2 ≥λ3 and U contains the
three eigenvectors. Geometrically, a set of 3D points lying
on a plane would have uncertainty of a 2D ellipse (instead
of 3D ellipsoid) represented by their covariance. Therefore,
a point cluster is planar if the least eigenvalue λ3 is zero,
while practically we choose λ3 < τ · λ2, where τ is a
planar threshold that was set to 0.01 in our tests. The plane
parameters (i.e., closest point) can be determined from the
eigenvector corresponding to the smallest eigenvalue and the
centroid of the point cluster. In case where a voxel is non-
planar, we subdivide it into 8 sub-voxels, and this process is
recursively applied until the plane fitting is successful or the
maximum depth is reached.
We further accelerate the above voxelization-based plane
extraction with a dual-level (frame- and voxel-level) parallel
strategy. At the frame-level, per-frame voxelization is inde-
pendently processed for each frame, allowing for efficient
handling of individual cells. At the voxel-level, cluster aggre-
gation and plane fitting are performed simultaneously across
all voxels within the latest frame. This parallelism ensures
that the computational load scales linearly with the number
of voxels, instead of points.
B. Cluster-to-Plane Measurements
Once we have obtained all the planes in the global frame
Gp[i]
π , ∀i, from all the voxels of the current sliding window,
we then construct the following point-on-plane measure-
ments for each of the voxel points at the current frame:
z[i]
k,j =
Gp[i]T
π
∥Gp[i]
π ∥
(GpLk + G
LkRLkpj
⏞
⏟⏟
⏞
Gpj
) −∥Gp[i]
π ∥
(7)
=
[︄
Gp[i]
π /∥Gp[i]
π ∥
−∥Gp[i]
π ∥
]︄T
⏞
⏟⏟
⏞
π[i]T
[︃G
LkR
GpLk
0
1
]︃
⏞
⏟⏟
⏞
G
Lk T
[︃Lkpj
1
]︃
⏞⏟⏟⏞
Lk ¯pj
(8)
where the j-th 3D point in the IMU/LiDAR local frame at
the current time k, Lkpj, is transformed into the global frame
Gpj, and then projected onto the global voxel plane
Gp[i]
π .
If noise free, the above point-to-plane distance (residual) (8)
would be zero. However, due to measurement noise and
imperfect IMU/LiDAR poses, the point-on-plane uncertainty
(i.e., variance σ[i]2
k,j ) would be inevitable, which may be
derived from the plane fitting or found empirically, i.e.,
z[i]
k,j ∼N(0, σ[i]2
k,j ). To simplify the ensuing derivations, we
assume an isotropic unit variance.
Since there are typically many points from the same voxel
residing on the same plane π[i], processing all these point-
on-plane constraints (8), either in batch or sequential form,
could be a significant overtaking. To address this issue, we
compress the m point-on-plane measurements via (thin) QR
decomposition:
[︂
z[i]
k,1
· · ·
z[i]
k,m
]︂T
⏞
⏟⏟
⏞
z[i]
k
=
⎡
⎢⎣
Lk ¯pT
1
...
Lk ¯pT
m
⎤
⎥⎦
⏞
⏟⏟
⏞
¯
Pi
QR
= QiRi
G
LkTT π[i] + n[i]
(9)
⇒z′[i]
k := QT
i z[i]
k = Ri
G
LkTT π[i] + QT
i n[i]
(10)

## Page 4

where Ri is a 4 × 4 upper triangular matrix (thin QR).
However, employing (10) requires explicitly constructing
the stacked matrix ¯Pi ∈Rm×4 before QR decomposition,
incurring a memory footprint and dynamic allocation over-
head that grows linearly (O(m)) with the point count m.
Since m often reaches thousands in dense scans, repeating
this O(m) construction across voxels causes severe memory
consumption, detrimental to SWaP-constrained UAVs.
To resolve this, we leverage the compact point cluster ma-
trix Ci ∈S4×4 (5), naturally aggregated during voxel-wise
plane fitting. Using Ci, we replace the memory-intensive QR
decomposition with a Cholesky decomposition of a fixed
4 × 4 matrix. This entirely circumvents the O(m) matrix
construction, compressing the memory footprint to O(1).
Furthermore, it reduces the decomposition complexity from
O(m × 42) [26] to a strict O(1) (∼21 FLOPs), effectively
decoupling update efficiency from point density m.
Therefore, we take full advantage of the voxels built in
our system (see Section IV-A), and equivalently (in max-
imum likelihood estimation or MLE sense) transform the
m point-on-plane constraints into a single cluster-to-plane
measurement based on the following lemma:
Lemma 1: Performing EKF batch update with multiple
point-on-plane constraints (say j = 1, · · · , m) (8) associated
with the i-th plane patch π[i], is equivalent (up to noise
characterization) to update with the following one cluster-
to-plane measurement:
z′′[i]
k = L[i]T
k
G
LkTT π[i] + n′′[i]
k
(11)
where LkCi = L[i]
k L[i]T
k
is the Cholesky decomposition of
the local point cluster [see (5)].
Proof:
It is known that the (iterated) EKF update is
equivalent to Gauss-Newton method for maximum likelihood
estimation (MLE) [27]. Hence, we transform the m point-on-
plane measurements from the MLE perspective as follows:
min
xk,π[i]||xk −ˆxk|k−1||2
Pk|k−1 + ||z[i]
k ||2
=||xk −ˆxk|k−1||2
Pk|k−1 + π[i]T G
LkT
(︂
¯PT
i ¯Pi
)︂
G
LkTT π[i]
=||xk −ˆxk|k−1||2
Pk|k−1 + π[i]T G
LkT
(︂
LkCi
)︂
G
LkTT π[i]
Chol.
= ||xk −ˆxk|k−1||2
Pk|k−1 + π[i]T G
LkT
(︂
L[i]
k L[i]T
k
)︂
G
LkTT π[i]
=||xk −ˆxk|k−1||2
Pk|k−1 + || L[i]T
k
G
LkTT π[i]
⏞
⏟⏟
⏞
z′′[i]
k
||2
Clearly, in the sense of MLE, we can equivalently perform
EKF update with this inferred cluster-to-plain measurement
z[i]
k which is of dimension only 4 × 1, instead of the stacked
point-on-plane measurements of m × 1 where m is typically
in the hundreds or thousands.
C. MSCKF Update
With the inferred small-size cluster-to-plane measurements
z′′[i]
k
derived from (11), we proceed to update the sliding
window states. The linearized residual for this measurement,
corresponding to the planar feature π[i], can be expressed
as:
Fig. 2: Visualization of simulated indoor environment and
robot motion trajectory.
r[i]
k = 0 −z′′[i]
k ≃H[i]
x,k˜xk + H[i]
π,k ˜π[i]
k + n[i]
k
(12)
where H[i]
x,k and H[i]
π,k are the Jacobians with respect to
the sliding window states (poses) and the plane feature
parameters, respectively. A key characteristic of the MSCKF
framework is that feature parameters (planes) are not main-
tained in the state vector to ensure linear computational
complexity w.r.t the map size. However, the residual in (12)
explicitly depends on the feature error ˜π[i]
k . To eliminate this
dependency, we employ the null-space projection technique
similar to the MSCKF-based VIO [5]. We project (12) onto
the null-space of the plane measurement Jacobian H[i]
π,k (i.e.,
U⊤H[i]
π,k = 0), to create the feature-independent measure-
ments for EKF update:
U⊤r[i]
k = U⊤H[i]
x,k˜xk + U⊤H[i]
π,k ˜π[i]
k + U⊤n[i]
k
⇒r′[i]
k = H′[i]
x,k˜xk + n′[i]
k
(13)
This projected residual r′[i]
k
depends only on the state
vector errors ˜xk. By stacking these projected residuals from
all valid planar features extracted in the current sliding
window (Section IV-A), we perform a standard EKF update
to correct the poses and biases in the sliding window.
This formulation provides two significant advantages: 1)
Consistency: By marginalizing out features via null-space
projection, we correctly handle the uncertainty without over-
confident map assumptions. 2) Efficiency: The “cluster-to-
plane” model (11) reduces the measurement dimension via
projection (from m×1 to 4×1 for each plane feature). This
drastically reduces the cost of the null-space computation
and the final Kalman update.
V. MONTE-CARLO SIMULATIONS
To effectively validate the consistency and accuracy of the
proposed LIO, we perform Monte Carlo simulations. To this
end, we build an indoor environment using the open-source
simulation platform [28]. The simulation scene is visualized
in Fig. 2, and the simulation setup parameters are listed in
Table I.
We compare our proposed method with the SOTA base-
lines on the performance metrics including Absolute Pose Er-
ror (APE) (measured in percent for translation and in degrees
per meter for rotation) for accuracy and averaged Normal-
ized Estimation Error Squared (NEES) for consistency [29].
These baselines include the widely-adopted FAST-LIO2 [2]
and VoxelMap [4], iG-LIO [17] representing recent high-
efficiency LIO systems, Super-LIO [3], a recently proposed

## Page 5

TABLE I: Simulation setup parameters.
Parameter
Value
Parameter
Value
IMU Freq.(hz)
250
Traj. Length(m)
182
LiDAR Freq.(hz)
10
LiDAR Noise
0.03
Gyro Noise
0.005
Gyro Bias Init
0.01
Gyro Rand. Walk
4e-6
Acc Bias Init
0.1
Acc Noise
0.01
LiDAR Rings Num.
8
Acc Rand. Walk
2e-4
LiDAR Ver. Res.(◦)
3
Gravity
9.81
LiDAR Hor. Res.(◦)
0.25
TABLE II: Monte Carlo simulation results.
Method
Trans. Error (%)
Rot. Error (◦/m)
Avg. NEES
FAST-LIO2
0.51
0.0120
8.70 × 105
VoxelMap
0.22
0.0058
1.06 × 106
iG-LIO
0.38
0.0115
1.05 × 106
Super-LIO
0.50
0.0100
1.42 × 105
FF-LINS
0.20
0.0019
15.96
Ours
0.22
0.0012
6.70
LIO system published in 2026 achieving extreme compu-
tational speed, and FF-LINS [13] which is known as a
consistent LiDAR-inertial state estimator.
Totally 20 Monte Carlo simulations are conducted, where
the results are presented in Table II. From these results, it is
evident that while the proposed method achieves localization
accuracy comparable to SOTA baselines, it significantly
outperforms them in terms of average NEES (where the
ideal value is 6.0 in this test). Specifically, FAST-LIO2,
VoxelMap, iG-LIO, and Super-LIO exhibit severe over-
confidence, yielding extremely large NEES values because
they neglect the inherent map uncertainty and the cross-
correlations between states and the geometric features. In
contrast, FF-LINS, which employs an Factor Graph Opti-
mization (FGO)-based framework with frame-to-frame data
association, maintains a relatively better uncertainty envelope
with an average NEES of 15.96. However, our proposed
method achieves an average NEES of 6.7, which is the
closest to the ideal value among all tested methods. This
indicates that our MSCKF-based formulation maintains a
Fig. 3: Comparison of yaw estimation error and estimated
3-sigma bounds: (top) VoxelMap, (bottom) our method.
Fig. 4: The vehicle platform equipped with a down-facing
LiDAR and RTK-GPS (providing ground-truth).
generally correct order of magnitude for the covariance
estimate, providing the most realistic assessment of system
uncertainty.
To further verify the consistency, we visualize the yaw
error and 3σ bounds estimated by the compared methods, as
shown in Fig. 3. Our method demonstrates a realistic growth
in uncertainty that correctly envelopes the yaw error, consis-
tent with the inherent drift of odometry systems. Conversely,
VoxelMap produces over-confident bounds that do not reflect
the true error accumulation. Results for FAST-LIO2, iG-
LIO, and Super-LIO are omitted due to their similar over-
confidence issues. Since the consistent baseline FF-LINS
yields an uncertainty profile similar to ours, its curve is also
omitted to maintain the clarity of the comparison.
VI. REAL-WORLD EXPERIMENTS
Real-world validation was conducted using a hexacopter
equipped with a downward-facing Livox Avia LiDAR and
RTK-GPS for ground-truth (Fig. 4). Six sequences were
captured across sparse (seq1), forested (seq2-4, 6), and
urban (seq5) environments, as shown in Fig. 5. Following
VoxelMap [4] configurations, we used full point clouds with
3m voxels (3-layer octree) and a 10-frame sliding win-
dow. Performance, measured by length-normalized APE, was
benchmarked against FAST-LIO2 [2], iG-LIO [17], Super-
LIO [3], and FF-LINS [13] on an Intel i7-11700 PC (8
threads, 32GB RAM).
A. Accuracy and Consistency Evaluation
The quantitative results of the flight tests, including
translation errors (measured in percent) and rotation errors
(measured in degrees per meter), and average NEES, are
summarized in Table III.
1) Accuracy and Robustness Analysis: The results in
Table III highlight a fundamental distinction between the
compared frameworks in terms of robustness under en-
vironmental degeneracy. Notably, in seq1, the drone tra-
versed a large open square with sparse geometric features,
a typical degenerate scenario for LiDAR-based odometry. In
this environment, map-based methods (e.g., FAST-LIO2, iG-
LIO, Super-LIO) exhibit significant performance degrada-
tion. Since these methods treat the global map as a fixed
prior, even a minor initial drift during the feature-sparse
period causes subsequent scans to be “forcefully” matched
against an increasingly erroneous map. This creates a de-
structive feedback loop, leading to the tracking divergence

## Page 6

TABLE III: Accuracy and Consistency Comparison
Data
Len.(m)
FAST-LIO2
iG-LIO
Super-LIO
FF-LINS
Ours
Trans. / Rot.
NEES
Trans. / Rot.
NEES
Trans. / Rot.
NEES
Trans. / Rot.
NEES
Trans. / Rot.
NEES
seq1
424.60
×
×
×
×
21.173/0.0060
1.076×1010
3.8813/0.0030
6.197×103
1.1098/0.0087
4.131×103
seq2
506.40
0.4346/0.0020
7.279×106
0.5559/0.0012
2.654×108
0.5662/0.0014
1.201×107
0.2874/0.0014
6.050×102
0.6270/0.0013
9.072×102
seq3
480.75
1.5189/0.0037
4.547×107
0.5429/0.0012
4.795×108
0.6917/0.0026
4.210×107
0.1992/0.0012
2.757×102
0.5682/0.0014
5.860×102
seq4
498.01
0.5829/0.0020
1.620×107
0.4063/0.0017
4.022×108
0.2583/0.0028
9.461×106
0.3485/0.0022
7.159×102
0.7504/0.0019
7.057×102
seq5
551.50
0.5827/0.0046
7.826×107
0.2359/0.0013
5.786×107
0.2645/0.0020
4.892×106
0.4984/0.0014
2.211×102
0.5276/0.0014
2.637×102
seq6
588.57
1.9218/0.0152
9.353×107
0.1639/0.0012
2.818×107
0.2755/0.0022
5.263×106
0.1197/0.0013
6.713×102
0.4884/0.0019
4.606×102
× denotes that the method failed to complete the corresponding sequence due to excessive odometry drift.
Fig. 5: Different real-world flight trajectories and scenes.
of FAST-LIO2 and iG-LIO (×) and a substantial translation
error in Super-LIO (21.17%).
In contrast, our proposed MSCKF framework and the
consistent FF-LINS avoid this pitfall by not relying on a
drifting global map, thereby maintaining a acceptable trans-
lation error (3.88%). Our method successfully completes the
trajectory with the lowest translation error of 1.11%, demon-
strating superior robustness in such degenerate scenarios. In
feature-rich environments (seq2 to seq6), the localization
accuracy of our method is on par with SOTA algorithms,
with translation errors ranging between 0.4% and 0.7% and
rotation errors between 0.0013 and 0.0019◦/m.
2) Consistency Analysis: To quantitatively assess esti-
mation consistency, we compute the average NEES for
all methods, utilizing high-precision RTK-GPS as ground-
truth. The results are summarized in Table III. In real-
world aerial experiments, unmodeled factors such as extrinsic
calibration residuals, time-synchronization errors, and non-
Gaussian sensor noise inevitably cause NEES values to
deviate from the theoretical ideal. Nevertheless, our method
achieves NEES values on the order of 102 ∼103, which is
within the same magnitude as the consistent LIO framework,
FF-LINS. In sharp contrast, FAST-LIO2, iG-LIO, and Super-
LIO exhibit significantly inflated NEES values (106 ∼1010),
indicating severe over-confidence.
This orders-of-magnitude difference confirms that our
map-free MSCKF framework effectively mitigates covari-
TABLE IV: Time Consumption Comparison (ms)
Data
FAST-LIO2
iG-LIO
Super-LIO
FF-LINS
Ours
seq1
×
×
11.78
113.01
18.11
seq2
62.19
36.65
17.28
45.69
27.09
seq3
73.79
38.27
16.83
40.22
29.70
seq4
60.75
37.33
17.16
51.25
27.07
seq5
41.38
25.42
12.66
27.35
19.88
seq6
60.64
25.31
11.08
37.08
19.94
TABLE V: Memory Usage Comparison (MB)
Data
FAST-LIO2
iG-LIO
Super-LIO
FF-LINS
Ours
seq1
×
×
162.082
728.469
103.41
seq2
623.105
1009.05
245.621
570.152
124.58
seq3
1785.94
887.270
231.800
564.863
107.40
seq4
576.703
925.328
233.629
550.770
99.410
seq5
505.895
984.051
245.211
561.086
106.45
seq6
340.727
470.863
144.398
541.199
106.77
ance underestimation, providing a more realistic uncertainty
measure. Theoretical consistency is crucial for the physical
robustness of the estimator: it ensures that the filter correctly
weights the IMU-driven state prediction and the LiDAR-
derived observations. Unlike over-confident map-based filters
that “forcefully” align current scans to noisy or poten-
tially misaligned priors—thereby inducing spurious attitude
corrections and hindering gyroscope bias convergence—our
method maintains a proper covariance envelope. By avoiding
these erroneous updates, our framework ensures precise
orientation tracking and robustly suppresses cumulative drift
in roll and pitch, even throughout challenging, high-dynamic
aerial trajectories.
B. Computational Efficiency and Memory Usage Evaluation
We evaluate the computational efficiency and resource
consumption of the proposed method by comparing it against
SOTA baselines across various datasets.
1) Runtime Analysis: Table IV summarizes the average
processing time per scan. In terms of efficiency, our method
significantly outperforms iG-LIO and FF-LINS, achieving
a 2× to 3× speedup over FAST-LIO2. The performance
bottleneck for these baseline methods primarily stems from
a measurement dimensionality that is directly coupled with
point cloud density. FF-LINS, in particular, is further bur-
dened by the high computational overhead of its Factor
Graph Optimization (FGO) framework. In contrast, the effi-
ciency of our approach is rooted in parallel voxelization and
the compact cluster-to-plane measurement model. While the
computational load for existing systems scales linearly with
point volume during residual and Jacobian derivations, our

## Page 7

update operation is strictly bounded by the number of ex-
tracted planar features (typically in the hundreds), effectively
decoupling computational cost from raw point density.
We acknowledge that our runtime is slightly higher than
Super-LIO. This difference arises because Super-LIO em-
ploys the OctVox structure to enforce strict density control
(i.e., aggressive downsampling) and utilizes a heuristic-
guided KNN strategy (HKNN) to accelerate search [3].
However, such aggressive downsampling poses risks for
high-altitude UAV flights, where scanned ground points
are inherently sparse. In these scenarios, further discarding
points can lead to a loss of critical geometric constraints,
potentially increasing state estimation errors. Consequently,
our method prioritizes robustness by processing the full
input point cloud without downsampling to ensure a lossless
LIO system. Despite processing significantly more data, our
approach remains highly competitive and fully satisfies real-
time requirements, with an average processing time below
30 ms per frame—well below the 100 ms real-time threshold
(for 10Hz LiDAR).
Lastly, to demonstrate the computational efficiency of our
proposed method on severely resource-constrained edge plat-
forms, we also conducted evaluations on a legacy NVIDIA
Jetson TX2. Even on this limited onboard hardware, our sys-
tem achieves real-time performance, maintaining an average
processing time of 86.2 ms per frame.
2) Memory Usage Analysis: Memory usage is a crit-
ical constraint for onboard UAV processors with limited
resources. As shown in Table IV, our method achieves
the lowest memory usage among all compared methods,
consistently maintaining a stable usage of approximately 100
MB regardless of trajectory duration.
This superior efficiency stems from the combination of
our map-free architecture and a lightweight sliding window
representation. While FAST-LIO2, iG-LIO, and Super-LIO
rely on maintaining an explicit global map (e.g., ikd-tree or
voxel-map) that can consume between 200 MB and 1 GB,
our approach marginalizes out historical features via null-
space projection. Crucially, our method also significantly
outperforms the map-free FF-LINS in memory conservation.
Although FF-LINS avoids a global map, its sliding window
stores “keyframes” that are actually dense submaps con-
structed by aggregating multiple LiDAR scans. In contrast,
each entry in our sliding window is a single raw LiDAR
scan. Consequently, even with an identical window size, our
system maintains a much leaner memory profile than FF-
LINS, making it uniquely suited for SWaP-constrained aerial
platforms.
C. Ablation Study
To quantitatively evaluate the individual contributions of
the proposed voxel-based parallel acceleration strategy and
the cluster-to-plane measurement model, we conducted a
comprehensive ablation study. We designed three variants of
the system to analyze the time consumption of key modules:
• Ours: The complete proposed framework equipped with
seq1
seq2
seq3
seq4
seq5
seq6
0
20
40
60
80
100
Time consumption (ms)
Methods
Ours
Ours^
Ours*
Modules breakdown
Pre-process
Data Assoc
State Update
Others
Fig. 6: Module-level runtime breakdown of the ablation
variants across six evaluation sequences.
both the compact cluster-to-plane constraints and multi-
threaded voxelization and data association (8 threads).
• Ours∧: The proposed cluster-to-plane model imple-
mented in a single-threaded manner.
• Ours∗: Replaces the cluster-to-plane model with the
conventional point-to-plane model (processing all points
individually) while keeping multi-threading enabled.
We decomposed the average time consumption per frame
into three critical functional modules and a residual ’Others’
category. Specifically, the Pre-process module encompasses
prediction, point undistortion, and state augmentation; Data
Association involves voxelization and adaptive plane fit-
ting; and State Update comprises residual and Jacobian
calculation, null-space projection, and the MSCKF update.
Remaining auxiliary overheads are grouped into Others. The
detailed runtime breakdown across six diverse sequences is
illustrated in Fig. 6.
1) Impact of Parallel Strategy: The effectiveness of the
voxel-based parallel strategy is evident by comparing the
single-threaded groups (Ours∧) with their multi-threaded
counterparts (Ours). The Data Association part is computa-
tionally intensive due to the traversal of massive point clouds
and voxels. The single-threaded implementation (Ours∧)
often creates a bottleneck, pushing the total frame time
over 80 ms in complex scenarios, e.g., seq3 and seq4.
By leveraging 8-thread parallelism, the proposed method
(Ours) significantly reduces the time consumption of the
voxelization and plane-fitting modules by a factor ranging
from 4× to 6×, ensuring the system remains well within
real-time constraints.
2) Impact of Point-Cluster Measurement Model: By com-
paring Ours with Ours∗, we observe the efficiency gain
brought by the observation dimensionality reduction. As
shown in the State Update module of the bars in Fig. 6,
the traditional point-to-plane model (Ours∗) incurs a heavy
computational load during the EKF update because the
dimension of the residual vector scales linearly with the
number of valid points (typically more than thousands). To
quantify this, we calculated the average number of planar
features Npl and planar points Npt per frame across all
test data. The statistics reveal that the average Npt (11,835)
is approximately two orders of magnitude larger than the
average Npl (429). Consequently, the effective measurement
dimension is drastically reduced from Npt (in point-to-plane

## Page 8

mode) to 4 × Npl (in cluster-to-plane mode), achieving
a dimensionality reduction of over 85%. This compact
formulation significantly reduces the dimension of the Ja-
cobian matrix and the computational cost of the null-space
projection, resulting in a State Update speedup ranging
from 3× to 8× across different sequences. In particular,
the acceleration is most pronounced in seq1. This sequence
features structured environments with extensive large-area
planes (e.g., walls and floors), resulting in a high density
of points per planar feature. Consequently, our cluster-based
representation achieves the maximal degree of dimensional-
ity reduction in this scenario, thereby yielding the highest
computational gain.
VII. CONCLUSION AND FUTURE WORK
In this paper, we presented a consistent and efficient
LiDAR-Inertial Odometry system specifically tailored for
SWaP-constrained UAVs. By establishing multi-frame geo-
metric constraints within an MSCKF framework, our method
ensures theoretical estimator consistency, effectively address-
ing the over-confidence issue prevalent in ESIKF-based
approaches. Furthermore, we resolved the computational
bottleneck of traditional MSCKF by introducing a paral-
lel voxelization and data association and a novel lossless
cluster-to-plane measurement model, which drastically re-
duces observation dimensionality. Extensive validations in
both simulations and challenging real-world aerial scenarios
demonstrate that our approach achieves accuracy comparable
to SOTA methods while delivering superior performance in
terms of estimation consistency and computational efficiency.
For future work, our primary goal is to further boost
the algorithm’s efficiency to achieve super-real-time perfor-
mance, making it even more suitable for drone platforms with
limited computational power. This will involve exploring
techniques such as keyframe selection to reduce the sliding
window length. Additionally, we plan to enhance long-
term robustness by incorporating persistently tracked planar
features directly into the state vector, enabling more resilient
data association over extended trajectories.
REFERENCES
[1] Federal Aviation Administration, “Package delivery by drone (part
135),” https://www.faa.gov/uas/advanced operations/package del
ivery drone, accessed: September 5, 2025.
[2] W. Xu, Y. Cai, D. He, J. Lin, and F. Zhang, “Fast-lio2: Fast direct lidar-
inertial odometry,” IEEE Transactions on Robotics, vol. 38, no. 4, pp.
2053–2073, 2022.
[3] L. Wang, X. Zhang, C. Li, D. He, Y. Pan, and J. Yi, “Super-lio:
A robust and efficient lidar-inertial odometry system with a compact
mapping strategy,” IEEE Robotics and Automation Letters, vol. 11,
no. 3, pp. 2666–2673, 2026.
[4] C. Yuan, W. Xu, X. Liu, X. Hong, and F. Zhang, “Efficient and prob-
abilistic adaptive voxel mapping for accurate online lidar odometry,”
IEEE Robotics and Automation Letters, vol. 7, no. 3, pp. 8518–8525,
2022.
[5] A. I. Mourikis and S. I. Roumeliotis, “A multi-state constraint kalman
filter for vision-aided inertial navigation,” in Proceedings 2007 IEEE
International Conference on Robotics and Automation.
IEEE, 2007,
pp. 3565–3572.
[6] M. Li and A. I. Mourikis, “High-precision, consistent ekf-based visual-
inertial odometry,” The International Journal of Robotics Research,
vol. 32, no. 6, pp. 690–711, 2013.
[7] P. Geneva, K. Eckenhoff, W. Lee, Y. Yang, and G. Huang, “Openvins:
A research platform for visual-inertial estimation,” in 2020 IEEE
International Conference on Robotics and Automation (ICRA). IEEE,
2020, pp. 4666–4672.
[8] C. Qin, H. Ye, C. E. Pranata, J. Han, S. Zhang, and M. Liu, “Lins:
A lidar-inertial state estimator for robust and efficient navigation,”
in 2020 IEEE international conference on robotics and automation
(ICRA).
IEEE, 2020, pp. 8899–8906.
[9] J. Zhang, S. Singh et al., “Loam: Lidar odometry and mapping in
real-time.” in Robotics: Science and systems, vol. 2, no. 9.
Berkeley,
CA, 2014, pp. 1–9.
[10] T. Shan, B. Englot, D. Meyers, W. Wang, C. Ratti, and D. Rus,
“Lio-sam: Tightly-coupled lidar inertial odometry via smoothing and
mapping,” in 2020 IEEE/RSJ international conference on intelligent
robots and systems (IROS).
IEEE, 2020, pp. 5135–5142.
[11] Z. Yuan, F. Lang, T. Xu, and X. Yang, “Sr-lio: Lidar-inertial odometry
with sweep reconstruction,” in 2024 IEEE/RSJ International Confer-
ence on Intelligent Robots and Systems (IROS).
IEEE, 2024, pp.
7862–7869.
[12] P. Dellenbach, J.-E. Deschaud, B. Jacquet, and F. Goulette, “Ct-icp:
Real-time elastic lidar odometry with loop closure,” 2021.
[13] H. Tang, T. Zhang, X. Niu, L. Wang, L. Wei, and J. Liu, “Ff-lins:
A consistent frame-to-frame solid-state-lidar-inertial state estimator,”
IEEE Robotics and Automation Letters, vol. 8, no. 12, pp. 8525–8532,
2023.
[14] W. Xu and F. Zhang, “Fast-lio: A fast, robust lidar-inertial odometry
package by tightly-coupled iterated kalman filter,” IEEE Robotics and
Automation Letters, vol. 6, no. 2, pp. 3317–3324, 2021.
[15] C. Bai, T. Xiao, Y. Chen, H. Wang, F. Zhang, and X. Gao, “Faster-
lio: Lightweight tightly coupled lidar-inertial odometry using parallel
sparse incremental voxels,” IEEE Robotics and Automation Letters,
vol. 7, no. 2, pp. 4861–4868, 2022.
[16] F. Zhu, Y. Ren, L. Yin, F. Kong, Q. Liu, R. Xue, W. Liu, Y. Cai,
G. Lu, H. Li et al., “Swarm-lio2: Decentralized efficient lidar-inertial
odometry for aerial swarm systems,” IEEE Transactions on Robotics,
vol. 41, pp. 960–981, 2024.
[17] Z. Chen, Y. Xu, S. Yuan, and L. Xie, “ig-lio: An incremental gicp-
based tightly-coupled lidar-inertial odometry,” IEEE Robotics and
Automation Letters, vol. 9, no. 2, pp. 1883–1890, 2024.
[18] C. Bai, T. Xiao, Y. Chen, H. Wang, F. Zhang, and X. Gao, “Faster-
lio: Lightweight tightly coupled lidar-inertial odometry using parallel
sparse incremental voxels,” IEEE Robotics and Automation Letters,
vol. 7, no. 2, pp. 4861–4868, 2022.
[19] W. Lee, P. Geneva, C. Chen, and G. Huang, “Mins: Efficient and
robust multisensor-aided inertial navigation system,” arXiv preprint
arXiv:2309.15390, 2023.
[20] B. Jiang and S. Shen, “A lidar-inertial odometry with principled
uncertainty modeling,” in 2022 IEEE/RSJ International conference on
intelligent robots and systems (IROS). IEEE, 2022, pp. 13 292–13 299.
[21] X. Zuo, P. Geneva, W. Lee, Y. Liu, and G. Huang, “Lic-fusion: Lidar-
inertial-camera odometry,” in 2019 IEEE/RSJ International Confer-
ence on Intelligent Robots and Systems (IROS).
IEEE, 2019, pp.
5848–5854.
[22] T. Zhang, M. Yuan, L. Wei, H. Tang, and X. Niu, “Msc-lio: An msckf-
based lidar-inertial odometry with same-plane-point tracking,” arXiv
preprint arXiv:2407.07589, 2024.
[23] H. Tang, T. Zhang, L. Wang, M. Yuan, and X. Niu, “Ba-lins: A
frame-to-frame bundle adjustment for lidar-inertial navigation,” IEEE
Transactions on Intelligent Transportation Systems, 2025.
[24] N. Trawny and S. I. Roumeliotis, “Indirect kalman filter for 3d attitude
estimation,” University of Minnesota, Dept. of Comp. Sci. & Eng.,
Tech. Rep, vol. 2, p. 2005, 2005.
[25] Z. Liu, X. Liu, and F. Zhang, “Efficient and consistent bundle
adjustment on lidar point clouds,” IEEE Transactions on Robotics,
2023.
[26] D. Mori, Y. Yamamoto, and S.-L. Zhang, “Backward error analysis
of the allreduce algorithm for householder qr decomposition,” Japan
Journal of Industrial and Applied Mathematics, vol. 29, no. 1, pp.
111–130, 2012.
[27] B. M. Bell and F. W. Cathey, “The iterated kalman filter update as
a gauss-newton method,” IEEE Transactions on Automatic Control,
vol. 38, no. 2, pp. 294–297, 1993.
[28] P. Geneva, K. Eckenhoff, Y. Yang, and G. Huang, “Lips: Lidar-
inertial 3d plane slam,” in 2018 IEEE/RSJ International Conference
on Intelligent Robots and Systems (IROS).
IEEE, 2018, pp. 123–130.

## Page 9

[29] Y. Bar-Shalom, X.-R. Li et al., “Thiagalingam kirubarajan, estimation
with applications to tracking and navigation,” wiley Publishing, 2001.
