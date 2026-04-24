# Design and Implementation of a High-Precision Wind-Estimation UAV with Onboard Sensors.pdf

## Page 1

Contents lists available at ScienceDirect
Measurement
journal homepage: www.elsevier.com/locate/measurement
 
Design and implementation of a high-precision wind-estimation UAV with 
onboard sensors
Haowen Yu a
, Na Fan c
, Xing Liu d
, Ximin Lyu a,b,e
,∗
a School of Intelligent Systems Engineering, Sun Yat-sen University, Guangdong, China
b The Research Institute of Multiple Agents and Embodied Intelligence, Peng Cheng Laboratory, Guangdong, China
c Department of Computer Science and Engineering, The Hong Kong University of Science and Technology, Hong Kong, China
d Shenzhen ZEEY Technology Co., Ltd., Guangdong, China
e Differential Robotics Technology Co., Ltd., Zhejiang, China
A R T I C L E  I N F O
Keywords:
Wind estimation
UAV
Disturbance observer
 
A B S T R A C T
Accurate real-time wind vector estimation is essential for enhancing the safety, navigation accuracy, and energy 
efficiency of unmanned aerial vehicles (UAVs). Traditional approaches rely on external sensors or simplify 
vehicle dynamics, which limits their applicability during agile flight or in resource-constrained platforms. 
This paper proposes a real-time wind estimation method based solely on onboard sensors. The approach first 
estimates external aerodynamic forces using a disturbance observer (DOB), and then maps these forces to 
wind vectors using a thin-plate spline (TPS) model. A custom-designed wind barrel mounted on the UAV 
enhances aerodynamic sensitivity, further improving estimation accuracy. The system is validated through 
comprehensive experiments in wind tunnels, indoor and outdoor flights. Experimental results demonstrate that 
the proposed method achieves consistently high-accuracy wind estimation across controlled and real-world 
conditions, with speed RMSEs as low as 0.06 m∕s in wind tunnel tests, 0.22 m∕s during outdoor hover, and 
below 0.38 m∕s in indoor and outdoor dynamic flights, and direction RMSEs under 7.3◦ across all scenarios, 
outperforming existing baselines. Moreover, the method provides vertical wind estimates – unavailable in 
baselines – with RMSEs below 0.17 m∕s even during fast indoor translations.
1. Introduction
Accurate real-time wind vector measurements, including wind speed 
and direction, are essential for unmanned aerial vehicle (UAV) opera-
tions. These measurements offer three key benefits. First, they improve 
flight safety and stability by compensating for wind disturbances, espe-
cially in strong winds [1]. Second, they enhance navigation precision 
by correcting wind-induced drift, thus supporting accurate trajectory 
tracking [2]. Third, they optimize energy use and flight endurance 
via wind-aware path planning and power management, maximizing 
operational range and flight time [3]. However, existing wind estima-
tion methods often struggle to deliver high accuracy across a wide 
measurement range without compromising flight safety or onboard 
computational efficiency, especially in dynamic flight.
Traditional high-precision wind measurement methods rely on ex-
pensive or heavy external devices, e.g., ground anemometers, weather 
balloons, and weather radars. Ground anemometers provide only point 
measurements [4]. Weather balloons are costly and subject to uncer-
tainties due to spatial drift [5]. Weather radar lacks sufficient resolution 
∗Corresponding author.
E-mail addresses: yuhw7@mail2.sysu.edu.cn (H. Yu), nfanaa@connect.ust.hk (N. Fan), liuxing@zeeytech.com (X. Liu), lvxm6@mail.sysu.edu.cn (X. Lyu).
for fine-scale wind measurements near operational aircraft [6]. Mount-
ing wind sensors directly on UAVs can provide localized wind mea-
surements, but typically increases power consumption and enlarges the 
UAV’s geometry, which may negatively affect obstacle avoidance capa-
bility. To address these challenges, researchers have explored methods 
that use only onboard sensors to estimate wind [7,8]. These methods 
typically infer wind from attitude changes and are based on quasi-static 
assumptions, neglecting full UAV dynamics. As a result, their accuracy 
degrades during dynamic flight maneuvers.
To address these limitations, we propose a method that lever-
ages only onboard sensors to estimate wind vectors, enabling accurate 
measurements during both static and dynamic flight. This approach 
eliminates the need for additional dedicated measurement instruments, 
thereby reducing dead weight and complexity while enhancing safety 
and endurance.
Our proposed method adopts a two-stage structure. The front-end 
employs a disturbance observer (DOB) [9,10] to estimate external 
forces acting on the vehicle. The DOB provides high-frequency force 
https://doi.org/10.1016/j.measurement.2025.119882
Received 29 August 2025; Received in revised form 24 November 2025; Accepted 25 November 2025
Measurement 260 (2026) 119882 
Available online 26 November 2025 
0263-2241/© 2025 Elsevier Ltd. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

## Page 2

H. Yu et al.
Fig. 1.  Wind estimation experiments in diverse environments: (a) Indoor dynamic flight in still-air conditions; (b) Outdoor hover and dynamic flight in natural, 
time-varying winds.
estimates without relying on quasi-static assumptions, enabling wind 
estimation during dynamic flight. The back-end maps these estimated 
forces to wind vectors using a hybrid model pre-fitted on wind tunnel 
data: a thin-plate spline (TPS) [11] for horizontal and a regression 
model for vertical components. The TPS model’s minimum bending 
energy property ensures smooth and accurate force-to-wind mapping 
over a wide range. To further enhance wind sensitivity and estimation 
accuracy, we incorporated a custom-designed wind barrel.
We evaluated the proposed wind estimation system across a variety 
of scenarios, including controlled wind tunnel tests, indoor flights, 
and outdoor hover and dynamic flight tests (see Fig. 1). Experimental 
results demonstrate that the proposed method consistently achieves 
high-accuracy wind estimation and outperforms baselines across all 
scenarios. In wind tunnel tests, speed and direction RMSEs reached 
0.06 m∕s and 3.6◦ at a ground-truth wind speed of 10 m∕s. During 
outdoor hover, RMSEs were 0.22 m∕s and 3.3◦, strongly correlated 
with the ground truth (correlation coefficient 𝑟> 0.9). In indoor 
dynamic flights, horizontal wind speed RMSE remained below 0.38 m∕s
and direction RMSE below 7.3◦. For the vertical component, where 
the ground-truth wind speed was 0 m∕s, the method achieved RMSEs 
under 0.17 m∕s. Even in outdoor dynamic flights with varying natural 
wind, the method achieved RMSEs of 0.29 m∕s for speed and 6.0◦ for 
direction in circular flights, consistently surpassing the baselines during 
unconstrained trajectories.
Our contributions are summarized as follows:
1. DOB-based wind vector estimation algorithm: We propose a 
real-time wind vector estimation method based on DOB, which 
relies solely on onboard sensors. The approach achieves high-
precision wind speed and direction estimation without exter-
nal sensors, and remains effective even during dynamic UAV 
maneuvers.
2. Improved estimation accuracy and extended measurement 
range: The DOB enables accurate external force estimation over 
a wide range. The TPS model provides smooth and accurate 
mapping from force to wind. The custom-designed wind barrel 
increases aerodynamic sensitivity, further enhancing estimation 
performance.
3. Comprehensive experimental validation: Extensive experi-
ments, including wind tunnel tests, outdoor hover trials, and 
both indoor and outdoor dynamic flights, validate the method’s 
reliability and performance in static and dynamic scenarios (see 
Section 5).
The remainder of this paper is organized as follows: Section 2 
provides an overview of related work. Section 3 introduces the de-
fined coordinate frames and the UAV dynamics. Section 4 presents 
the principle and framework of the proposed wind estimation system, 
including the DOB formulation (Section 4.2.1), the wind barrel design 
and validation (Section 4.2.2), and the force-to-wind mapping model 
(Section 4.3). Experimental results are presented in Section 5. Finally, 
Section 6 concludes the paper and introduces future work.
2. Related work
Pioneering UAV wind measurements used fixed-wing aircraft with 
Pitot tubes to infer airspeed  [12,13]. However, Pitot tubes require 
prior knowledge of airflow direction and precise alignment [14], and 
their accuracy degrades at low airspeeds [15]. Furthermore, fixed-
wing UAVs cannot hover, which restricts in-situ wind sensing at a 
fixed location. Multirotors have attracted increasing interest for wind 
sensing due to their hovering and maneuvering capabilities. Some 
studies have integrated conventional wind sensors, such as ultrasonic 
anemometers [16] and multi-hole pressure probes [17]. However, these 
sensors are often bulky and heavy, reducing UAV maneuverability, 
stability, and flight duration [18]. For instance, mounting a commercial 
ultrasonic anemometer such as the Sniffer4D Mini 2 [19] on a DJI M300 
adds 780 g of mass and requires 12 W of continuous power. To avoid 
rotor wash, it must be mounted on a mast of approximately 0.37 m 
above the rotor plane, significantly increasing the vehicle’s vertical 
extent. Others have developed specialized sensors (whiskers [20,21], 
microphones [22], hot-wire sensors [23], surface wind sensors [24]).
Model-based approaches estimate wind indirectly from UAV mo-
tion states (e.g., attitude, velocity) and aerodynamic interactions [7,25,
26]. However, they are typically limited to steady or near-hover flight 
and cannot estimate vertical wind components. Extensions for 3D wind 
estimation in constant-velocity flight exist [8,27], but they still struggle 
during rapid maneuvers and with uncertain aerodynamics. Kalman 
Filter (KF)-based estimators are widely used to improve robustness by 
explicitly modeling process and measurement uncertainties [28–30]. 
However, their accuracy strongly depends on the fidelity of the UAV 
dynamics and wind interaction models, and consequently, their per-
formance is often degraded by real-world model imperfections [31].
Learning-based methods [23,32–34] offer data-driven alternatives 
by mapping UAV sensor data (e.g., IMU, GPS) directly to wind vec-
tors. They leverage the nonlinear approximation capabilities of neural 
networks to capture complex relationships, but often require large-
scale training data and exhibit poor generalization across sensors and 
platforms.
Disturbance Observer (DOB)-based methods have recently
emerged as promising alternatives. They estimate external disturbance 
forces on the UAV and map them to wind vectors using aerodynamic 
models calibrated from flight data. Lyu et al. [10] demonstrated that 
DOB-based control improves wind disturbance rejection in VTOL UAVs. 
Building on this, Yu et al. [35] proposed a DOB-based wind estimation 
method using onboard sensors (IMU, GPS) to achieve real-time 3D wind 
vector estimation.
Measurement 260 (2026) 119882 
2

## Page 3

H. Yu et al.
Fig. 2.  UAV platform with a custom wind barrel mounted beneath to enhance wind estimation. Three coordinate frames are defined: inertial (𝐼), body (𝐵), 
and intermediate (𝐶).
Despite these advances, existing approaches remain limited in terms 
of accuracy, capability for 3D wind estimation, robustness under dy-
namic flight conditions, data efficiency, and adaptability across sensor 
suites and platforms. Our approach addresses these gaps by enabling ac-
curate and reliable 3D wind estimation across diverse flight conditions, 
even during Beyond estimation, robust wind-aware control is critical 
for safe UAV operation. Recent advances in safety-guaranteed and fault-
tolerant control – e.g., Yu et al. [36] on fault-tolerant cooperative 
control and Yu et al. [37] on performance-guaranteed safety control 
– highlight the growing emphasis on resilience under environmental 
disturbances (including wind). While our work focuses on estimation, 
its high-fidelity wind output can serve as a key enabler for such control 
frameworks, closing the loop from perception to robust action.
3. Preliminaries
3.1. Coordinate systems
To describe the UAV’s motion and wind estimation process, three 
coordinate frames are introduced (see Fig. 2): the Earth-fixed inertial 
frame 𝐼 with axes (𝒙𝐼, 𝒚𝐼, 𝒛𝐼); the body frame 𝐵 with origin 𝒐𝑏 at 
the UAV’s center of gravity and axes (𝒙𝐵, 𝒚𝐵, 𝒛𝐵); and the intermediate 
frame 𝐶 with axes (𝒙𝐶, 𝒚𝐶, 𝒛𝐶), obtained by rotating 𝐼 about its 
𝒛𝐼-axis by the desired yaw angle 𝜓𝑑.
3.2. UAV dynamics
The UAV’s dynamics are described by [38]: 
𝑚̈𝒑= −𝑢𝑓𝑹𝒆3 + 𝑚𝑔0𝒆3 + 𝒇𝑒,
𝑱̈𝜼= −C(𝜼, ̇𝜼) ̇𝜼+ 𝒖𝜏+ 𝝉𝑒.
(1)
where 𝑚 is the UAV’s mass; 𝑔0 is the gravitational acceleration; 𝒑=
[𝑝𝑥, 𝑝𝑦, 𝑝𝑧]⊤ is the position of 𝒐𝑏 represented in 𝐼; 𝒆3 = [0, 0, 1]⊤ is the 
unit vector along 𝒛𝐼; 𝑹∈𝑆𝑂(3) is the rotation matrix that transforms 
vectors from 𝐵 to 𝐼; 𝒇𝑒= [𝑓𝑒𝑥, 𝑓𝑒𝑦, 𝑓𝑒𝑧]⊤ is the total external force 
in 𝐼; 𝜼= [𝜙, 𝜃, 𝜓]⊤ represents the UAV’s attitude (e.g., roll, pitch, and 
yaw angles); 𝑱∈R3×3 is the UAV’s moment of inertia in 𝐵; 𝝉𝑒∈R3
is the total external torque in 𝐵; C(𝜼, ̇𝜼) is the Coriolis matrix; 𝑢𝑓∈R
and 𝒖𝝉∈R3 are the total thrust and torque control inputs generated by 
the four rotors [39].
Fig. 3 illustrates the relationship between the thrust and normalized 
RPM of each rotor. The relationship between 𝑢𝑓 and normalized RPM 
can be approximated using a quadratic polynomial [40]. For our UAV 
platform, the fitted mapping is: 
𝑢𝑓=
4
∑
𝑖=1
(207𝛺2
𝑖+ 11.34𝛺𝑖+ 0.01315),
(2)
Fig. 3. ‘Revolution-Thrust’ curve for each motor.
where 𝛺𝑖 is the normalized RPM of the 𝑖th rotor (actual RPM divided 
by the maximum RPM). Note that while the full control input of the 
quadrotor includes both thrust 𝑢𝑓 and 𝒖𝜏, only 𝑢𝑓 is required for 
the subsequent wind estimation process (see Section 4.2.1). Therefore, 
we provide only the thrust–RPM relationship here. The coefficients in 
Eq. (2) were obtained via static thrust-stand calibration: each motor 
was mounted on a load cell, and thrust was measured across 10 evenly 
spaced RPM levels from 0 to 3650 RPM. The normalized speed is 
computed as 𝛺𝑖= RPM𝑖× 1.047 × 10−4, yielding a calibration range 
of 𝛺∈[0, 0.38].
4. Methodology
Section 4.1 presents a system overview, outlining data flow and 
module functions. Section 4.2 details Stage I, which estimates external 
force via DOB (Section 4.2.1) and improves aerodynamic sensitivity 
using a custom wind barrel (Section 4.2.2). Section 4.3 describes Stage 
II, covering training data acquisition (Section 4.3.1), modeling using 
TPS and polynomial regression (Section 4.3.2), and real-time filtering 
(Section 4.3.3).
4.1. Wind estimation system overview
Our wind estimation system adopts a two-stage structure, as illus-
trated in Fig. 4:
Stage I: External Force Estimation (Fig. 4(a)): External aero-
dynamic forces 𝒇𝑒 induced by ambient airflow are estimated by a 
disturbance observer (DOB). The DOB computes ̂𝒇
𝐼
𝑒 in the inertial frame 
𝐼 using measured thrust 𝑢𝑓, acceleration ̈𝒑, and attitude 𝜼 as inputs. 
Measurement 260 (2026) 119882 
3

## Page 4

H. Yu et al.
Fig. 4.  System Overview: (a) DOB-based external force estimation. (b) Force-to-wind mapping and wind inference.
̂𝒇
𝐼
𝑒 are then transformed into the intermediate frame 𝐶 to obtain ̂𝒇
𝐶
𝑒
for subsequent wind estimation.
Stage II: Force-to-Wind Mapping (Fig. 4(b)): The horizontal force 
components ( ̂𝑓𝐶
𝑒𝑥, ̂𝑓𝐶
𝑒𝑦) are used to compute the wind direction 𝜗𝑟, which 
is the same as the direction of the force. The horizontal wind speed ̂𝑉𝐶
ℎ
is then obtained from these components using a TPS model, while the 
vertical force ̂𝑓𝐶
𝑒𝑧 is converted to vertical wind speed ̂𝑉𝐶
𝑣 via polynomial 
regression. These components form the relative air velocity ̂𝑨
𝐶
𝑟, which 
is then transformed into the inertial frame 𝐼 as ̂𝑨
𝐼
𝑟. Finally, the true 
wind vector ̂𝑨
𝐼
𝑤 is obtained by subtracting the UAV’s velocity ̇𝒑 from 
̂𝑨
𝐼
𝑟.
4.2. Stage I: DOB-based external force estimation
4.2.1. DOB formulation
We use a DOB to estimate the external disturbances caused by air-
flow in real time. Our approach extends the work of Yüksel et al. [41]. 
The UAV’s configuration is described by 𝜣= [𝒑⊤, 𝜼⊤]⊤, then we write 
(1) in a compact form: 
𝒅𝒆= ̈𝜣+ ̇𝜣+ 𝝁+ 𝒈,
(3)
where 
=
[𝑚𝐈3
𝟎3×3
𝟎3×3
𝐉
]
,
=
[𝟎3×3
𝟎3×3
𝟎3×3
C
]
,
=
[𝐑𝒆3
𝟎3×3
𝟎3×3
−𝐈3
]
,
𝒈=
[−𝑚𝑔0𝒆3
𝟎3×1
]
.
(4)
Here, 𝒅𝒆= [𝒇⊤
𝒆, 𝝉⊤
𝒆]⊤ is the external wrench applied to the UAV; 𝐈3 ∈
R3×3 is the identity matrix; 𝝁= [𝑢𝑓, 𝒖𝝉⊤]⊤∈R4×1 is the control input 
of total thrust and torque.
Following the formulation in [9], the DOB is described by: 
̇̂𝒅𝒆= 𝑳(𝜣, ̇𝜣) (𝒅𝑒−̂𝒅𝑒
) ,
(5)
where 𝒅𝑒 is the actual wrench as defined in (3); ̂𝒅𝑒 is the estimated 
external wrench; and 𝑳(𝜣, ̇𝜣) ∈R6×6 is a gain matrix. Since we do not 
assume any specific model for the external wrench and have no prior 
information about its time derivative [9,41], we assume: 
̇𝒅𝑒= 𝟎.
(6)
Define the observation error 𝒆 as the difference between the actual 
external wrench 𝒅𝒆 and its estimate ̂𝒅𝑒: 
𝒆= 𝒅𝑒−̂𝒅𝑒.
(7)
Taking the derivative of (7) and substituting from (5), we obtain: 
̇𝒆= −𝑳(𝜣, ̇𝜣)𝒆.
(8)
The convergence of the observer error depends on the gain matrix 
𝑳(𝜣, ̇𝜣).
To enable axis-wise tuning of convergence rates, we follow the 
design proposed in [41] and define the gain matrix as: 
𝑳(𝜣, ̇𝜣) = 𝑲𝐼−1,
(9)
where 𝑲𝐼∈R6×6 is a diagonal gain matrix with positive elements, 
allowing independent tuning of observer gains for each axis.
Proposition 1.  Consider the wrench estimator defined by (5). If the gain 
matrix is structured as (9), then the estimated external wrench ̂𝒅𝑒 converges 
asymptotically to the actual external wrench 𝒅𝒆, i.e., ̂𝒅𝑒→𝒅𝒆.
Proof.  We consider the Lyapunov function candidate: 
𝑽(𝒆, 𝜣) = 𝒆⊤𝒆,
(10)
is positive definite. Considering (8) and (9), we can write: 
𝑑𝑽(𝒆, 𝜣)
𝑑𝑡
= −2𝒆⊤𝑲𝐼−1𝒆+ 𝒆⊤̇𝒆
= 𝒆⊤(−2𝑲𝐼−1 + ̇)𝒆,
(11)
since  is constant (mass and inertia are time-invariant), we have: 
̇= 𝟎6×6.
(12)
Substituting into (11) yields: 
𝑑𝑽(𝒆, 𝜣)
𝑑𝑡
= 𝒆⊤(−2𝑲𝐼−1)𝒆,
(13)
since  a positive-definite matrix and 𝑲𝐼 is a diagonal matrix with 
positive elements, the matrix −2𝑲𝐼−1 is negative definite. Thus, 
𝑑𝑽
𝑑𝑡
≤0, which ensures Lyapunov stability. It follows that the ob-
servation error 𝒆(𝑡) asymptotically converges to zero, completing the 
proof. □
Consequently, by substituting (9) into (5), we obtain the observer 
formulation: 
̇̂𝒅𝒆= −𝑲𝐼−1 ̂𝒅𝑒+ 𝑲𝐼−1(̈𝜣+ ̇𝜣+ 𝝁+ 𝒈).
(14)
Through wind tunnel analysis, we found that while the external 
force 𝒇𝑒 exhibits a one-to-one mapping to wind velocity 𝑉𝑤 (Sec-
tion 4.3), the external torque 𝝉𝑒 does not: the same torque magni-
tude and direction can correspond to multiple different wind condi-
tions, making torque unsuitable for unambiguous wind reconstruction. 
Measurement 260 (2026) 119882 
4

## Page 5

H. Yu et al.
Hence, for the purpose of wind velocity estimation, we extract and 
discretize the estimated forces part from (14). This yields the following 
discrete-time representation of the force estimator: 
̂𝒇𝑒(𝑘+ 1) =
(
𝑰3 −𝛿𝑡
2𝑚𝑲𝐼
)
̂𝒇𝑒(𝑘)
+ 𝛿𝑡
2𝑚𝑲𝐼
(𝑚̈𝒑−𝒈+ 𝑢𝑓𝒛𝐵
) ,
(15)
where 𝛿𝑡 is the time step; 𝒛𝐵 is the third column of 𝑹, representing the 
body-frame 𝑧-axis in 𝐼; ̂𝒇𝑒 is the estimated external force in 𝐼. The 
resulting ̂𝒇𝑒 is transformed into 𝐶 to yield: 
̂𝒇
𝐶
𝑒= [ ̂𝑓𝐶
𝑒𝑥, ̂𝑓𝐶
𝑒𝑦, ̂𝑓𝐶
𝑒𝑧]⊤.
(16)
4.2.2. Wind barrel aerodynamic design and validation
To improve wind sensitivity, especially under low-speed conditions, 
increasing aerodynamic drag is essential to amplify the system’s mea-
surable airflow response. To this end, we explored the effect of barrel 
surface texture and developed a customized design that enhances drag. 
We evaluated three barrel surface designs, illustrated in Fig. 5(a):
- Design A: cross-lattice texture with large grooves (6 mm × 6 mm ×
13 mm);
- Design B [42]: smooth surface;
- Design C (ours): same lattice pattern as A but with shallower grooves 
(6 mm × 6 mm × 1.5 mm).
All three designs share identical geometry and cross-sectional area, 
isolating surface structure as the only variable.
CFD simulations (Fig. 5(b)) reveal distinct wake structures and 
drag coefficients. A produces the most symmetric and narrow wake, 
indicating smooth flow with minimal separation and thus the low-
est drag coefficient (𝐶𝑑= 0.97). In contrast, B exhibits pronounced 
vortex shedding and a significantly wider wake, reflecting stronger 
flow separation and a higher drag coefficient (𝐶𝑑= 1.30). C shows 
even more intense vortex shedding than B, indicating further increased 
flow separation, resulting in the highest drag coefficient (𝐶𝑑= 1.47). 
These findings confirm that C most effectively increases aerodynamic 
drag under low-speed flow, making it well-suited for force-based wind 
sensing.
To experimentally validate the CFD results, we conducted wind 
tunnel tests using a suspended crossbar setup, as shown in Fig. 5(c). 
The crossbar was mounted horizontally and positioned perpendicular 
to the incoming wind (red arrow), with two different wind barrel 
designs installed at its ends (e.g., A vs. B, A vs. C, B vs. C), enabling 
direct comparison of their aerodynamic performance under identical 
conditions.
The drag force on each barrel is given by 
𝐹𝑑= 1
2𝜌𝑣2𝐴𝐶𝑑,
(17)
where 𝐹𝑑 is the drag force, 𝜌 the air density, 𝑣 the wind speed, 𝐴 the 
cross-sectional area, and 𝐶𝑑 the drag coefficient. Since 𝐴 is fixed across 
designs, differences in 𝐹𝑑 stem solely from 𝐶𝑑. This imbalance generates 
a torque that causes the crossbar to rotate, with the higher-drag side 
moving downwind.
In Fig. 5(c), the yellow arrow indicates this rotation. In the A–
B comparison, the crossbar rotated such that B moved downwind, 
suggesting B generated more drag than A. In tests involving C, the 
crossbar consistently rotated with C moving downwind, indicating it 
produced more drag than both A and B. These experimental obser-
vations confirm the CFD results, which identified C as having the 
highest 𝐶𝑑, validating its advantage in boosting aerodynamic force and 
improving the signal-to-noise ratio (SNR) in wind sensing.
Fig. 5.  Three wind barrel designs and their evaluation. (a) Surface textures 
of each design. (b) CFD simulation results showing airflow and wake patterns. 
(c) Wind tunnel test showing crossbar rotation due to drag differences.
4.3. Stage II: Force-to-wind mapping
4.3.1. Wind tunnel data collection
A dedicated dataset was collected in a controlled wind tunnel 
environment to train the force-to-wind mapping model. The UAV was 
commanded to hover under steady laminar airflow with onboard sensor 
data recorded continuously at 50 Hz.
Horizontal wind data. To characterize the UAV’s aerodynamic response 
under various horizontal wind conditions, yaw-sweep data were col-
lected at wind speeds ranging from 0 to 8 m∕s, in 1 m∕s increments. At 
each wind speed 𝑉𝑤, the UAV maintained a stable hover and was slowly 
rotated about its yaw axis. The yaw angle 𝜓 was incremented by 10◦
every 20 s, completing a full 360◦ sweep per speed level.
The horizontal force vector is characterized by its magnitude and 
direction in 𝐶: 
̂𝑓𝐶
ℎ=
√
( ̂𝑓𝐶
𝑒𝑥)2 + ( ̂𝑓𝐶
𝑒𝑦)2,
̂𝜗𝐶
𝑓= arctan 2( ̂𝑓𝐶
𝑒𝑥, ̂𝑓𝐶
𝑒𝑦),
(18)
where ̂𝑓𝐶
ℎ and ̂𝜗𝐶
𝑓 are the magnitude and direction of the estimated 
horizontal external force.
Fig. 6(a) visualizes the collected horizontal data in polar coordi-
nates: radial distance represents ̂𝑓𝐶
ℎ, angle denotes ̂𝜗𝐶
𝑓, and the color 
Measurement 260 (2026) 119882 
5

## Page 6

H. Yu et al.
Fig. 6.  Horizontal force–wind mapping using TPS regression. (a) Training data distribution. (b) Fitted TPS surface.
gradient encodes the corresponding wind speed. The non-circular dis-
tribution of points shows the UAV’s anisotropic aerodynamic response 
across different flow directions, showing that the same wind speed may 
produce different force magnitudes depending on orientation.
Vertical wind data. Unlike the horizontal direction, vertical wind can-
not be easily generated in the wind tunnel, thus we use UAV vertical 
motion to simulate equivalent vertical airflow.
To generate an equivalent vertical airflow, the UAV was com-
manded to perform controlled vertical ascents and descents along 𝒛𝐼
in still air. The UAV was commanded to ascend or descend at constant 
vertical speeds ranging from 0 to 5 m∕s, increasing in 1 m∕s increments. 
At each speed level, the motion was sustained for 20 s. This proce-
dure effectively induces an aerodynamic equivalent of vertical wind, 
enabling construction of the vertical force–wind model in the absence 
of actual environmental airflow.
4.3.2. Force-to-wind mapping
To estimate wind velocity from onboard force measurements, we 
construct a data-driven pipeline that maps estimated external forces 
to wind components. Horizontal wind speed ̂𝑉𝐶
ℎ is obtained by fitting 
a thin-plate spline model to ( ̂𝑓𝐶
𝑒𝑥, ̂𝑓𝐶
𝑒𝑦), while vertical wind speed ̂𝑉𝐶
𝑣
is estimated via polynomial regression on ̂𝑓𝐶
𝑒𝑧. The full wind vector 
is finally reconstructed in the inertial frame using ̂𝑉𝐶
ℎ, ̂𝑉𝐶
𝑣, and the 
estimated direction ̂𝜗𝐶
𝑓.
TPS regression of horizontal wind speed. The mapping between hori-
zontal external force and airflow is modeled using a TPS regression 
method [11].
The horizontal force vector, represented in polar form as ( ̂𝑓𝐶
ℎ, ̂𝜗𝐶
𝑓), 
is first converted into Cartesian coordinates: 
𝑚= ̂𝑓𝐶
ℎcos ̂𝜗𝐶
𝑓,
𝑛= ̂𝑓𝐶
ℎsin ̂𝜗𝐶
𝑓.
(19)
Using input (𝑚, 𝑛), we trained a TPS model 𝑍(⋅) to predict the 
corresponding horizontal wind speed ̂𝑉𝐶
ℎ: 
̂𝑉𝐶
ℎ= 𝑍(𝑚, 𝑛) = 𝑍
(
̂𝑓𝐶
ℎcos ̂𝜗𝐶
𝑓, ̂𝑓𝐶
ℎsin ̂𝜗𝐶
𝑓
)
.
(20)
The TPS function takes the following form: 
𝑍(𝑚, 𝑛) =
𝑁
∑
𝑖=1
𝑐𝑖𝜙(|(𝑚, 𝑛) −(𝑚𝑖, 𝑛𝑖)|) + 𝑎0 + 𝑎1𝑚+ 𝑎2𝑛,
(21)
where 𝜙(𝑟) = 𝑟2 log 𝑟 is the radial basis function, and (𝑚𝑖, 𝑛𝑖) is the 𝑖th 
training input. The parameters 𝑐𝑖, 𝑎0, 𝑎1, and 𝑎2 are fitted by minimizing 
the regularized loss: 
min
𝑎0,𝑎1,𝑎2,𝑐𝑖
{ 𝑁
∑
𝑖=1
(
𝑉𝐶
ℎ,𝑖−𝑍(𝑚𝑖, 𝑛𝑖)
)2
+ 𝜆𝐽(𝑍)
}
,
(22)
where 𝑉𝐶
ℎ,𝑖 is the measured horizontal wind speed in 𝐶 for the 𝑖th 
sample, 𝜆≥0 is a regularization parameter, and 𝐽(𝑍) is a roughness 
penalty term controlling surface curvature. Further details on TPS 
modeling and regularization can be found in [11].
Fig. 6(b) shows the fitted TPS surface mapping inputs (𝑚, 𝑛) to hori-
zontal wind speed ̂𝑉𝐶
ℎ. The TPS formulation effectively balances fidelity 
to the training data and smoothness through the regularization term in 
(22), allowing the model to capture localized variations in aerodynamic 
response while suppressing high-frequency noise. This regularization 
ensures that the learned force-to-wind relationship faithfully represents 
underlying physical characteristics without overfitting.
Polynomial regression of vertical wind speed. To estimate vertical wind 
speed ̂𝑉𝐶
𝑣, a simple polynomial regression model was fitted to relate 
the estimated vertical external force ̂𝑓𝐶
𝑒𝑧 to ̂𝑉𝐶
𝑣: 
̂𝑉𝐶
𝑣=
𝐾
∑
𝑘=1
𝑐𝑘⋅( ̂𝑓𝐶
𝑒𝑧)𝑘,
(23)
where 𝐾 is the polynomial degree, and 𝑐𝑘 are the regression coefficients 
obtained during training.
Wind vector reconstruction. The estimated values ̂𝜗𝐶
𝑓, ̂𝑉𝐶
ℎ, and ̂𝑉𝐶
𝑣 from 
(18), (20), and (23), are used to construct the relative air velocity ̂𝑨
𝐶
𝑟
in 𝐶: 
̂𝑨
𝐶
𝑟=
⎡
⎢
⎢
⎢⎣
̂𝑉𝐶
ℎcos ̂𝜗𝐶
𝑓
̂𝑉𝐶
ℎsin ̂𝜗𝐶
𝑓
̂𝑉𝐶
𝑣
⎤
⎥
⎥
⎥⎦
,
(24)
This vector is then rotated into 𝐼 as ̂𝑨
𝐼
𝑟 via: 
̂𝑨
𝐼
𝑟= 𝐑𝐼𝐶̂𝑨
𝐶
𝑟,
(25)
where 𝐑𝐼𝐶 is the rotation matrix from 𝐶 to 𝐼.
According to the wind triangle principle, the true wind velocity ̂𝑨
𝐼
𝑤
in 𝐼 is computed by subtracting the UAV’s ground velocity ̇𝒑 from the 
air-relative velocity ̂𝑨
𝐼
𝑟: 
̂𝑨
𝐼
𝑤= ̂𝑨
𝐼
𝑟−̇𝒑.
(26)
Given the wind vector ̂𝑨
𝐼
𝑤= [ ̂𝐴𝑤𝑥, ̂𝐴𝑤𝑦, ̂𝐴𝑤𝑧]⊤ in 𝐼, the horizontal 
wind direction ̂𝜗𝐼
ℎ, speed ̂𝑉𝐼
ℎ, and vertical speed ̂𝑉𝐼
𝑣 are computed as: 
̂𝜗𝐼
ℎ= arctan 2( ̂𝐴𝑤𝑦, ̂𝐴𝑤𝑥) + 𝜋,
̂𝑉𝐼
ℎ=
√
̂𝐴2
𝑤𝑥+ ̂𝐴2
𝑤𝑦,
̂𝑉𝐼
𝑣= ̂𝐴𝑤𝑧,
(27)
where the additional 𝜋 compensates for the 180◦ offset between the 
force orientation and the true wind direction. A positive value of ̂𝑉𝐼
𝑣
indicates upward airflow, while a negative value indicates downward 
airflow along 𝒛𝐼. This completes the reconstruction of the full wind 
velocity in 𝐼.
Measurement 260 (2026) 119882 
6

## Page 7

H. Yu et al.
Fig. 7.  Comparison of wind estimation using unfiltered, static-filtered, and 
dynamic-filtered methods. The dynamic filter effectively reduces noise and 
remains responsive.
4.3.3. Dynamic filtering for wind estimate refinement
Although the wind vector is reconstructed via force-to-wind map-
ping, it remains sensitive to high-frequency noise, primarily due to 
sensor noise and numerical differentiation in DOB estimation. There-
fore, we apply temporal filtering to refine the signal quality. According 
to [43], the DOB maintains accurate gain up to approximately 0.5 Hz, 
sufficient for low-altitude wind monitoring tasks where rapid response 
is less critical. To enhance real-time usability, we apply a dynamic 
post-processing filter. This filter uses gain scheduling to suppress high-
frequency noise while preserving temporal responsiveness. Specifically, 
the filter gain adapts to the estimated wind speed: higher gains are 
applied under low-speed conditions to improve the SNR, while lower 
gains are used at higher speeds to minimize phase lag.
Fig. 7 compares three approaches: unfiltered wind estimation, con-
ventional static filtering, and the proposed dynamic filter. The proposed 
dynamic filter (blue curve) effectively suppresses high-frequency noise 
without introducing noticeable delay. At a wind speed of 10 m∕s, it 
reduces lag by 3.4 s compared to static filtering, as highlighted by the 
black arrow. Meanwhile, it maintains close temporal alignment with 
the unfiltered signal while offering substantial noise suppression. These 
results confirm that dynamic filtering improves both the clarity and 
timeliness of wind estimates, making them more suitable for practical 
applications.
5. Experiment and results
5.1. Hardware platform
The DJI Matrice 300 UAV (see Fig. 2) was used as the experimen-
tal platform. To improve wind sensitivity and estimation accuracy, a 
custom wind barrel was mounted beneath the UAV. The wind barrel 
is a cylindrical structure with an inner diameter of 105 mm, outer 
diameter of 106.5 mm, height of 150 mm, and mass of 105 g. The barrel 
is installed in an underslung configuration to enhance aerodynamic 
response without increasing the vehicle’s geometric. The performance 
of the wind barrel is described in Section 4.2.2. The modified UAV is 
capable of reaching a maximum flight speed of 15 m∕s.
5.2. Validation of DOB-based force estimation
To validate the performance of the DOB-based external force esti-
mation, we conducted static experiments using a tensiometer. Ground-
truth (GT) forces of 4.89 N, 9.78 N, and 12.71 N were sequentially applied 
along the 𝒙𝐼, 𝒚𝐼, and 𝒛𝐼 axes. Table 1 summarizes the mean (𝑒𝜇) and 
standard deviation (SD) (𝑒𝜎) of DOB force estimation errors for each 
axis and force magnitude. For the 𝒙𝐼-axis, 𝑒𝜇 remained small, ranging 
Table 1
 The mean (𝑒𝜇) and SD (𝑒𝜎) of DOB-estimated force errors under different 
ground-truth force magnitudes applied along the 𝒙𝐼, 𝒚𝐼, and 𝒛𝐼 axes. 
 GT Force (N)
4.89
9.78
12.71
 Axis
𝑒𝜇 (N)
𝑒𝜎 (N)
𝑒𝜇 (N)
𝑒𝜎 (N)
𝑒𝜇 (N)
𝑒𝜎 (N) 
 𝒙𝐼-direction
−0.27
0.09
−0.25
0.10
−0.20
0.07  
 𝒚𝐼-direction
−0.72
0.16
−0.71
0.15
−0.73
0.13  
 𝒛𝐼-direction
−1.88
0.33
−1.85
0.22
−1.87
0.19  
from −0.27 N to −0.20 N, with a low 𝑒𝜎 between 0.07 N and 0.10 N. For 
the 𝒚𝐼-axis, the DOB also exhibited a consistent negative bias of around 
0.72 N, with 𝑒𝜎 ranging from 0.13 N to 0.16 N. The 𝒛𝐼-axis demonstrated 
the largest 𝑒𝜇, consistently around −1.87 N. Despite the larger bias, the 
𝑒𝜎 decreased as the applied force increased, from 0.33 N at 4.89 N to 
0.19 N at 12.71 N, indicating improved stability under stronger forces.
The estimation errors were primarily due to sensor noise. Across 
all axes and force magnitudes, the low 𝑒𝜎 indicates consistent and 
reliable DOB outputs. Although a systematic bias exists in 𝑒𝜇, it does not 
compromise wind estimation accuracy. This is because there exists a 
one-to-one mapping between the external force 𝒇𝐶
𝑒 and the wind vector 
̂𝑨
𝐼
𝑤. As long as the DOB consistently estimates 𝒇𝐶
𝑒 as ̂𝒇
𝐶
𝑒, the system 
can learn a reliable mapping from ̂𝒇
𝐶
𝑒 to ̂𝑨
𝐼
𝑤. The small 𝑒𝜎 ensures that 
this mapping remains stable and accurate despite the bias. Therefore, 
the proposed DOB-based force estimation is robust to sensor noise and 
adaptable to different UAV platforms via parameter tuning.
5.3. Wind estimation: Experimental setup
To systematically evaluate our wind estimation method, we conduct 
experiments in a wind tunnel, indoor space, and outdoor environment.
Ground-truth wind measurement. In wind-tunnel experiments, the hori-
zontal flow was set and controlled by the tunnel, while vertical wind 
components were not measured. Indoor experiments assumed still air, 
with a ground-truth wind speed of 0 m∕s and direction of 0◦ (equiv-
alently 360◦). For outdoor experiments, a 2D ultrasonic anemometer 
placed 6 m from the UAV and sampled at 0.3 Hz provided horizontal 
wind GT. Vertical wind estimation was evaluated only indoors due to 
the lack of reliable vertical sensing for the wind-tunnel and outdoor 
setups.
Baselines. We compared the proposed method with a regularized poly-
nomial regression method (Yu et al. [35]) and a learning-based method 
(Zimmerman et al. [32]). Both baselines were re-implemented on our 
UAV platform using consistent sensor configurations. Since these base-
lines estimate only horizontal wind, comparisons were limited to hor-
izontal wind estimation. The learning-based method was trained using 
150,000 samples with 11 input features, including motor speed (𝛺), 
attitude (𝜼), and acceleration (̈𝒑). In contrast, our TPS model used 
only 289 averaged samples with inputs (𝑚, 𝑛) and 𝑉𝐶
ℎ as defined in 
Section 4.3.
Evaluation metrics. Wind estimation performance was quantified using 
two primary metrics: root-mean-square error (RMSE) and the Pearson 
correlation coefficient (𝑟), evaluated for both wind speed and direction 
relative to ground truth. RMSE reflects absolute estimation accuracy, 
while 𝑟 captures the linear correlation between estimated and true 
values. Additionally, the mean and standard deviation (SD) of RMSE 
across multiple samples were computed to assess average performance 
and consistency.
5.4. Wind estimation: Wind tunnel validation
Wind tunnel experiments with controlled horizontal winds were 
conducted to assess the accuracy, robustness, and generalization of the 
proposed method. The wind speed was gradually increased from 0 m∕s
Measurement 260 (2026) 119882 
7

## Page 8

H. Yu et al.
Fig. 8.  Wind tunnel validation: RMSE (solid lines) and SD (shaded areas) of estimated horizontal wind speed and direction over ground-truth wind speeds from 
0 to 10 m∕s.
Table 2
 Wind tunnel validation: RMSE of estimated wind speed 𝜀𝑣 (m∕s) and direction 𝜀𝜃 (◦) at selected ground-truth wind speeds. 
 GT wind speed (m∕s)
0
1
5
9
10
 Method
𝜀𝑣 (m∕s)
𝜀𝜃 (◦)
𝜀𝑣 (m∕s)
𝜀𝜃 (◦)
𝜀𝑣 (m∕s)
𝜀𝜃 (◦)
𝜀𝑣 (m∕s)
𝜀𝜃 (◦)
𝜀𝑣 (m∕s)
𝜀𝜃 (◦) 
 [32]
0.62
13.2
0.44
12.6
0.17
9.4
0.16
8.9
0.17
7.8  
 [35]
0.48
11.0
0.39
8.4
0.15
5.1
0.15
5.0
0.17
5.1  
 Proposed
0.32
9.8
0.17
7.6
0.08
5.0
0.06
3.7
0.06
3.6  
to 10 m∕s in 1 m∕s increments. At each speed level, the UAV was held 
stationary at a fixed angle to the wind for 20 s. The test data at 9 m∕s
and 10 m∕s beyond the training range of 0 m∕s to 8 m∕s were used to 
assess model extrapolation.
Fig. 8 shows the RMSE and SD of estimated horizontal wind speed 
and direction across wind speeds from 0 to 10 m∕s. The white region 
indicates interpolation within the training range (0–8 m∕s), while the 
gray area denotes extrapolation (9–10 m∕s). For wind speed (top panel), 
all methods exhibited decreasing RMSE and SD with increasing wind 
speed, stabilizing above 3 m∕s. This trend reflects changes in SNR: at 
low speeds, weaker aerodynamic forces reduce SNR, amplifying sensor 
noise; at higher speeds, SNR improves, reducing estimation errors. For 
wind direction (bottom panel), the proposed method and Yu et al. [35] 
achieved comparable RMSE across the full range. Overall, the proposed 
method consistently achieved the lowest RMSE and SD, outperforming 
all baselines in both interpolation and extrapolation regimes.
Table 2 reports the RMSE of each method at selected wind speeds. 
The proposed method consistently achieves the lowest estimation error 
across all tested wind speeds, with up to 65 % reduction in speed 
RMSE and 54 % reduction in direction RMSE compared to the strongest 
baseline. Notably, even at the highest speed (10 m∕s) – beyond the 
training range – the proposed method maintains superior accuracy, 
confirming robust extrapolation capability.
Compared to the global polynomial fit in Yu et al. [35], our TPS 
model better preserves force-to-wind mapping features, improving ac-
curacy. The end-to-end learning model in Zimmerman et al. [32] 
directly maps sensor data to wind estimates but performs worse in 
our setup—likely due to the lack of physical constraints, which makes 
it prone to overfitting and less physically consistent. In contrast, our 
method explicitly incorporates the physical relationship between wind 
and aerodynamic force, enhancing interpretability and consistency. 
Overall, the proposed method demonstrates superior performance and 
generalization under controlled laminar flow.
5.5. Wind estimation: Field validation
5.5.1. Outdoor hover
To assess estimation accuracy under static, real-world conditions, an 
outdoor hovering experiment was conducted, with results summarized 
in Fig. 9.
As shown in Fig. 9(a), the proposed method (blue) closely matches 
the ground truth (cyan), outperforming both Zimmerman et al. [32] 
(brownish red) and Yu et al. [35] (yellow). The proposed method 
achieved a wind speed RMSE of 0.22 m∕s, representing relative im-
provements of 41 % and 27 % compared to Zimmerman et al. [32] 
(0.37 m∕s) and Yu et al. [35] (0.30 m∕s), respectively. The wind speed 
error distributions (Fig. 9(b), left) demonstrate the proposed method’s 
superior performance with a sharp, zero-centered peak, in contrast to 
the wider error ranges of the other methods. 𝑟 between estimated and 
ground-truth wind speeds (Fig. 9(c)) was 0.94 for the proposed method, 
surpassing Zimmerman et al. [32] (𝑟= 0.75) and Yu et al. [35] (𝑟=
0.83). Fig. 9(d) illustrates the estimated wind direction during hover. 
The proposed method achieved an RMSE of 3.3◦, which is 52 % lower 
than Zimmerman et al. [32] (6.9◦) and 13 % lower than Yu et al. [35] 
(3.8◦). Fig. 9(e) presents the distribution of wind direction estimation 
errors. As illustrated in Fig. 9(f), the proposed method achieved 𝑟=
0.93, outperforming Zimmerman et al. [32] (𝑟= 0.87) and Yu et al. [35] 
(𝑟= 0.91).
In summary, the proposed approach demonstrates superior accuracy 
in wind vector estimation under static outdoor conditions, exhibiting 
both low estimation error and high consistency with ground truth.
5.5.2. Indoor dynamic flight
To assess wind estimation performance in still air, two indoor 
flight patterns were tested: (1) a horizontal figure-eight for low-speed, 
continuously changing headings, and (2) a fast lateral translation for 
high-speed motion along all principal axes.
Horizontal figure-eight flight. To evaluate performance during low-speed 
maneuvers with varying headings, the UAV followed a horizontal 
figure-eight trajectory.
Fig. 10(a) shows the UAV’s horizontal speed 𝑉𝑥𝑦, estimated hori-
zontal wind speeds ̂𝑉𝐼
ℎ from Zimmerman et al. [32], Yu et al. [35], 
and the proposed method, along with the proposed method’s vertical 
wind speed estimate ̂𝑉𝐼
𝑧. The proposed method produced horizontal 
wind estimates closest to the zero-wind ground truth, with reduced 
bias and fluctuations, and uniquely provided vertical wind estimation. 
Fig. 10(b) shows the estimated horizontal wind direction ̂𝜗𝐼
ℎ, where 
the proposed method exhibited the lowest deviation. Quantitatively 
(Fig. 10(c)), the proposed method’s horizontal wind speed RMSE was 
0.35 m∕s, 48 % lower than Zimmerman et al. [32] (0.67 m∕s) and 15 %
lower than Yu et al. [35] (0.41 m∕s). Its vertical wind speed RMSE was 
0.1 m∕s. For horizontal wind direction, the RMSE was 7.1◦, 42 % lower 
than Zimmerman et al. [32] (12.2◦) and 3 % lower than Yu et al. [35] 
(7.3◦).
Errors were mainly due to thrust modeling inaccuracies during 
dynamic flight, particularly from variations in propeller advance ratio 
affecting aerodynamic thrust [44].
Measurement 260 (2026) 119882 
8

## Page 9

H. Yu et al.
Fig. 9.  Outdoor hover. (a) Wind speed estimates over time. (b) Estimated wind speed error distribution. (c) Correlation between GT speed and estimated speed. 
(d) Wind direction estimates over time. (e) Estimated wind direction error distribution. (f) Correlation between GT direction and estimated direction.
Fig. 10.  Indoor dynamic flight: horizontal figure-eight pattern. (a) Horizontal 
UAV speed 𝑉𝑥𝑦, estimated wind speeds ̂𝑉𝐼
ℎ (horizontal) and ̂𝑉𝐼
𝑣 (vertical). 
(b) Estimated horizontal wind direction ̂𝜗𝐼
ℎ. (c) RMSE of wind speeds and 
horizontal wind direction (vertical wind speed RMSE shown only for the 
proposed method).
Fast lateral translation flight. To assess performance during rapid trans-
lations along 𝒙𝐼, 𝒚𝐼, and 𝒛𝐼 axes, the UAV executed acceleration–
deceleration maneuvers along each axis to cover both horizontal and 
vertical motions.
Fig. 11(a) shows the UAV’s translational speeds along each axis. 
Fig. 11(b) presents horizontal wind speed estimates ̂𝑉𝐼
ℎ from all three 
methods and vertical wind speed ̂𝑉𝐼
𝑣 from the proposed method. Fig. 
11(c) shows estimated wind direction ̂𝜗ℎ, and Fig. 11(d) summarizes 
RMSEs.
For horizontal wind speed, the proposed method achieved an RMSE 
of 0.38 m∕s, 34 % lower than Zimmerman et al. [32] (0.58 m∕s) and 7 %
lower than Yu et al. [35] (0.41 m∕s). For wind direction, the RMSE was 
7.3◦, 40 % lower than Zimmerman et al. [32] (12.2◦) and 6 % lower than 
Yu et al. [35] (7.8◦). The proposed method’s vertical wind speed RMSE 
was 0.17 m∕s, with additional errors from rotor-induced downwash in 
the confined indoor space.
In summary. Across both experiments, the proposed method consis-
tently outperformed the other two, achieving the lowest RMSE in 
horizontal wind speed and direction, while maintaining low vertical 
wind error in dynamic indoor flight.
5.5.3. Outdoor dynamic flight
To evaluate wind estimation performance under realistic, time-
varying conditions, outdoor dynamic flight experiments were con-
ducted in the presence of the natural wind.
Circular flight. The UAV followed circular trajectories to induce vary-
ing airflow across all axes.
Fig. 12 shows the estimated horizontal wind speed ̂𝑉𝐼
ℎ and direction 
̂𝜗𝐼
ℎ along with ground truth from the ultrasonic anemometer. The pro-
posed method achieved the highest accuracy, while baselines exhibited 
larger deviations.
Corresponding RMSE and Pearson correlation coefficient (𝑟) are 
summarized in Table 3. For wind speed estimation, Zimmerman et al.
[32] reported an RMSE of 0.55 m∕s with 𝑟= 82 %. Yu et al. [35] 
improved these results to 0.49 m∕s and 85 %. The proposed method 
further reduced the error to 0.29 m∕s with 𝑟= 93 %, representing RMSE 
reductions of 47 % and 41 % compared to Zimmerman et al. [32] and 
Yu et al. [35], respectively. For wind direction estimation, Zimmer-
man et al. [32] reported an RMSE of 14.7◦ with 𝑟= 76 %. Yu et al. [35] 
improved the estimation with a lower RMSE of 6.4◦ and a higher 𝑟
of 83 %. The proposed method achieved the lowest RMSE (6.0◦) with 
𝑟= 85 %, corresponding to a further 59 % over Zimmerman et al. [32] 
and 6 % reduction over Yu et al. [35]. Overall, the proposed method 
consistently outperformed the baselines in horizontal wind estimation, 
achieving both the highest accuracy and the strongest correlation with 
ground truth.
Measurement 260 (2026) 119882 
9

## Page 10

H. Yu et al.
Fig. 11.  Indoor dynamic flight: fast lateral translation. (a) UAV speeds along 𝒙𝐼, 𝒚𝐼, and 𝒛𝐼. (b) Estimated wind speeds ̂𝑉𝐼
ℎ (proposed) and ̂𝑉𝐼
𝑣. (c) Estimated 
horizontal wind direction ̂𝜗𝐼
ℎ. (d) RMSE of wind speeds and horizontal wind direction across all methods.
Fig. 12.  Outdoor dynamic flight: circular pattern. (a) Estimated horizontal wind speed ̂𝑉𝐼
ℎ vs. ground truth. (b) Estimated horizontal wind direction ̂𝜗𝐼
ℎ vs. ground 
truth.
Table 3
 Outdoor dynamic flight: RMSE and Pearson correlation (𝑟) of estimated wind 
speed and direction. 
 
Wind speed (m∕s)
Wind direction (◦)
 Method
RMSE ↓
𝑟 (%) ↑
RMSE ↓
𝑟 (%) ↑
 Zimmerman et al. [32]
0.55
82
14.7
76
 
 Yu et al. [35]
0.49
85
6.4
83
 
 Proposed
0.29
93
6.0
85
 
Table 4
 Outdoor dynamic flight: extended free flights. RMSE of estimated wind speed 
𝜀𝑣 (m∕s) and direction 𝜀𝜃 (◦) for multiple trials of hover and dynamic flights. 
 Method
Zimmerman et al. [32]
Yu et al. [35]
Proposed
 Flights
𝜀𝑣 (m∕s)
𝜀𝜃 (◦)
𝜀𝑣 (m∕s)
𝜀𝜃 (◦)
𝜀𝑣 (m∕s)
𝜀𝜃 (◦) 
 Trial 1 (Hover)
0.58
8.7
0.35
7.0
0.28
6.9  
 Trial 2 (Hover)
0.40
6.9
0.27
5.5
0.23
5.4  
 Trial 3 (Dynamic)
0.70
11.8
0.50
10.1
0.46
8.9  
 Trial 4 (Dynamic)
0.54
13.1
0.44
11.4
0.42
10.5  
 Trial 5 (Dynamic)
0.70
13.5
0.48
7.9
0.37
7.1  
Extended free flights. To further assess performance in less constrained 
scenarios, extended outdoor free-flight tests were conducted in nat-
urally varying wind, including both hover and dynamic maneuvers. 
The UAV flew 5 m–10 m from the ultrasonic anemometer following 
unconstrained trajectories. Five trials, each lasting up to 6 minutes, 
were recorded. Trials 1–2 (Hover), conducted under the same setup 
as Section 5.5.1, were used as reference under steady conditions for 
comparison with dynamic trials. Trials 3–5 (Dynamic) involved free 
flights with heading and velocity changes.
Table 4 reports the RMSE of estimated wind speed 𝜀𝑣 and direction 
𝜀𝜃 for each trial and method. Hover trials exhibited relatively low errors 
for all methods, with the proposed method achieving the smallest RMSE 
in both wind speed and direction estimation. Dynamic trials showed 
higher errors. These discrepancies may partly result from spatial vari-
ations in the wind field rather than from algorithmic degradation. 
Because the ultrasonic anemometer assumes a uniform wind field, the 
moving UAV can traverse regions with wind conditions different from 
those measured by the anemometer, leading to mismatches between the 
estimated and ground-truth values. Across all five trials, the proposed 
method consistently yielded the smallest RMSE, demonstrating that 
our method maintains high precision and robustness even in dynamic, 
unstructured outdoor flight scenarios.
6. Conclusion and future work
In this work, we proposed a high-precision, wide-range wind estima-
tion method relying solely on UAV onboard sensors. The system com-
bines a DOB for external force estimation with a combination of TPS 
and polynomial regression models to map aerodynamic forces to wind 
vectors, eliminating the need for dedicated wind-sensing hardware. 
A custom-designed wind barrel enhances aerodynamic sensitivity, as 
confirmed by CFD and wind tunnel analyses.
The proposed method was extensively validated through wind tun-
nel, indoor, and outdoor flight experiments. In controlled wind tunnel 
tests up to 10 m∕s, it demonstrated RMSEs as low as 0.06 m∕s for speed 
and 3.6◦ for direction under laminar airflow. Outdoor experiments 
confirmed accurate horizontal wind estimation, achieving RMSEs of 
0.29 m∕s and 6.0◦ for speed and direction, respectively, with strong 
correlation to ground-truth trends. Indoor dynamic trials further veri-
fied robust performance under varying maneuvers, providing reliable 
horizontal wind estimates and uniquely enabling vertical wind esti-
mation with RMSEs below 0.17 m∕s, which is not provided by prior 
baselines. These results demonstrate the feasibility, robustness, and 
broad applicability of the proposed method.
Measurement 260 (2026) 119882 
10

## Page 11

H. Yu et al.
Future work will explore (i) direct aerodynamic force-to-wind map-
ping to reduce dependence on wind tunnel calibration and enable fully 
calibration-free deployment, and (ii) validation against true vertical 
wind sources (e.g., 3D wind facilities) to further strengthen verti-
cal wind estimation capability. Furthermore, integrating the proposed 
wind estimator with performance-guaranteed safety controllers [37] 
or cooperative fault-tolerant architectures [36] could significantly en-
hance UAV robustness in extreme wind events—e.g., gust rejection 
during formation flight or safe landing under sensor degradation.
CRediT authorship contribution statement
Haowen Yu: Writing – original draft, Validation, Software, Method-
ology, Investigation. Na Fan: Writing – review & editing, Validation. 
Xing Liu: Resources, Data curation. Ximin Lyu: Writing – review & 
editing, Supervision, Methodology, Investigation, Funding acquisition, 
Formal analysis, Conceptualization.
Declaration of competing interest
The authors declare that they have no known competing finan-
cial interests or personal relationships that could have appeared to 
influence the work reported in this paper.
Acknowledgments
This research was supported by the National Natural Science Foun-
dation of China[http://dx.doi.org/10.13039/501100001809] (Grant 
No. 62303495), and Young Talent Support Project of Guangzhou Asso-
ciation for Science and Technology, China (Project No. QT-2025-004).
Data availability
The authors do not have permission to share data.
References
[1] K. Guo, J. Jia, X. Yu, L. Guo, L. Xie, Multiple observers based anti-disturbance 
control for a quadrotor UAV against payload and wind disturbances, Control 
Eng. Pract. 102 (2020) 104560, http://dx.doi.org/10.1016/j.conengprac.2020.
104560.
[2] M. O’Connell, G. Shi, X. Shi, K. Azizzadenesheli, A. Anandkumar, Y. Yue, S. 
Chung, Neural-Fly enables rapid learning for agile flight in strong winds, Sci. 
Robot. 7 (66) (2022) http://dx.doi.org/10.1126/SCIROBOTICS.ABM6597.
[3] Y. Duan, F. Achermann, J. Lim, R. Siegwart, Energy-optimized planning in 
non-uniform wind fields with fixed-wing aerial vehicles, in: 2024 IEEE/RSJ 
International Conference on Intelligent Robots and Systems, IROS, IEEE, 2024, 
pp. 3116–3122.
[4] J. jia Jiang, W. jie Dang, F. jie Duan, X. quan Wang, X. Fu, C. yue Li, Z. bo Sun, 
H. Liu, L. ran Bu, An accurate ultrasonic wind speed and direction measuring 
method by combining time-difference and phase-difference measurement using 
coded pulses combination, Appl. Acoust. 159 (2020) 107093, http://dx.doi.org/
10.1016/j.apacoust.2019.107093.
[5] E.I.F. de Bruijn, F.C. Bosveld, S. de Haan, B.G. Heusinkveld, Measuring low-
altitude winds with a hot-air balloon and their validation with cabauw tower 
observations, J. Atmos. Ocean. Technol. 37 (2) (2020) 263–277, http://dx.doi.
org/10.1175/JTECH-D-19-0043.1.
[6] M.B. Yeary, B.L. Cheong, J.M. Kurdzo, T. Yu, R.D. Palmer, A brief overview of 
weather radar technologies and instrumentation, IEEE Instrum. Meas. Mag. 17 
(5) (2014) 10–15, http://dx.doi.org/10.1109/MIM.2014.6912194.
[7] R.T. Palomaki, N.T. Rose, M. van den Bossche, T.J. Sherman, S.F.D. Wekker, 
Wind estimation in the lower atmosphere using multirotor aircraft, J. Atmos. 
Ocean. Technol. 34 (5) (2017) 1183–1191, http://dx.doi.org/10.1175/JTECH-D-
16-0177.1.
[8] K. Meier, R. Hann, J. Skaloud, A. Garreau, Wind estimation with mul-
tirotor UAVs, Atmosphere 13 (4) (2022) 551, http://dx.doi.org/10.3390/
atmos13040551.
[9] W. Chen, D.J. Ballance, P.J. Gawthrop, J. O’Reilly, A nonlinear disturbance 
observer for robotic manipulators, IEEE Trans. Ind. Electron. 47 (4) (2000) 
932–938, http://dx.doi.org/10.1109/41.857974.
[10] X. Lyu, J. Zhou, H. Gu, Z. Li, S. Shen, F. Zhang, Disturbance observer based 
hovering control of quadrotor tail-sitter VTOL UAVs using H∞ synthesis, IEEE 
Robot. Autom. Lett. 3 (4) (2018) 2910–2917, http://dx.doi.org/10.1109/LRA.
2018.2847405.
[11] S.N. Wood, Thin plate regression splines, J. R. Stat. Soc. Ser. B Stat. Methodol. 
65 (1) (2003) 95–114, http://dx.doi.org/10.1111/1467-9868.00374.
[12] M. Kumon, I. Mizumoto, Z. Iwai, M. Nagata, Wind estimation by unmanned air 
vehicle with delta wing, in: Proc. IEEE Int. Conf. on Robotics and Automation, 
ICRA, 2005, pp. 1896–1901, http://dx.doi.org/10.1109/ROBOT.2005.1570390.
[13] A. Wenz, T.A. Johansen, Moving horizon estimation of air data parameters 
for UAVs, IEEE Trans. Aerosp. Electron. Syst. 56 (3) (2020) 2101–2121, http:
//dx.doi.org/10.1109/TAES.2019.2946677.
[14] T.A. Johansen, A. Cristofaro, K. Sørensen, J.M. Hansen, T.I. Fossen, On estimation 
of wind velocity, angle-of-attack and sideslip angle of small UAVs using standard 
sensors, in: Proc. Int. Conf. Unmanned Aircraft Systems, ICUAS, 2015, pp. 
510–519, http://dx.doi.org/10.1109/ICUAS.2015.7152330.
[15] I.d. Buscarini, A.C. Barsaglini, P.J.S. Jabardo, N.M. Taira, G. Nader, Impact 
of pitot tube calibration on the uncertainty of water flow rate measurement, 
J. Phys.: Conf. Ser. 648 (2015) 012005, http://dx.doi.org/10.1088/1742-6596/
648/1/012005.
[16] D. Hollenbeck, G. Nunez, L.E. Christensen, Y. Chen, Wind measurement and 
estimation with small unmanned aerial systems (suas) using on-board mini 
ultrasonic anemometers, in: Proc. Int. Conf. Unmanned Aircraft Systems, ICUAS, 
2018, pp. 285–292, http://dx.doi.org/10.1109/ICUAS.2018.8453418.
[17] S. Prudden, A. Fisher, M. Marino, A. Mohamed, S. Watkins, G. Wild, Measuring 
wind with small unmanned aircraft systems, J. Wind Eng. Ind. Aerodyn. 176 
(2018) 197–210, http://dx.doi.org/10.1016/j.jweia.2018.03.029.
[18] Z. Li, O. Pu, Y. Pan, B. Huang, Z. Zhao, H. Wu, A study on measuring the 
wind field in the air using a multi-rotor UAV mounted with an anemometer, 
Bound.-Layer Meteorol. 188 (1) (2023) 1–27.
[19] SoarAbility Technology, Sniffer4D Mini 2 Modular Meteorological Payload for 
UAV, 2025, URL https://www.soarability.tech/uav_met, (Accessed: 2025-11-19).
[20] S. Kim, R. Kubicek, A. Paris, A. Tagliabue, J.P. How, S. Bergbreiter, A whisker-
inspired fin sensor for multi-directional airflow sensing, in: Proc. IEEE/RSJ Int. 
Conf. on Intelligent Robots and Systems, IROS, 2020, pp. 1330–1337, http:
//dx.doi.org/10.1109/IROS45743.2020.9341723.
[21] A. Tagliabue, J.P. How, Airflow-inertial odometry for resilient state estimation on 
multirotors, in: 2021 IEEE International Conference on Robotics and Automation, 
ICRA, IEEE, 2021, pp. 5736–5743.
[22] M. Makaveev, M. Snellen, E.J.J. Smeur, Microphones as airspeed sensors for 
unmanned aerial vehicles, Sensors 23 (5) (2023) 2463, http://dx.doi.org/10.
3390/S23052463.
[23] N. Simon, A.Z. Ren, A. Piqué, D. Snyder, D. Barretto, M. Hultmark, A. Majumdar, 
FlowDrone: Wind estimation and gust rejection on UAVs using fast-response hot-
wire flow sensors, in: Proc. IEEE Int. Conf. on Robotics and Automation, ICRA, 
2023, pp. 5393–5399, http://dx.doi.org/10.1109/ICRA48891.2023.10160454.
[24] Z. Wang, A. Giaralis, S. Daniels, M. He, A. Margnelli, C. Jagadeesh, Enhancing 
accuracy of surface wind sensors in wind tunnel testing: A physics-guided 
neural network calibration approach, Measurement 234 (2024) 114812, http:
//dx.doi.org/10.1016/j.measurement.2024.114812.
[25] P.P. Neumann, M. Bartholmai, Real-time wind estimation on a micro unmanned 
aerial vehicle using its inertial measurement unit, Sens. Actuators A Phys. 235 
(2015) 300–310, http://dx.doi.org/10.1016/j.sna.2015.09.036.
[26] J. Gonzalez-Rocha, C.A. Woolsey, C. Sultan, S. de Wekker, N. Rose, Measuring 
atmospheric winds from quadrotor motion, in: Proc. AIAA Atmos. Flight Mech. 
Conf., AFM, 2017, p. 1189, http://dx.doi.org/10.2514/6.2017-1189.
[27] J. Gonzalez-Rocha, C.A. Woolsey, C. Sultan, S.F.D. Wekker, Model-based wind 
profiling in the lower atmosphere with multirotor UAS, in: Proc. AIAA SciTech 
Forum, 2019, p. 1598, http://dx.doi.org/10.2514/6.2019-1598.
[28] Z. Xing, Y. Zhang, C. Su, Y. Qu, Z. Yu, Kalman filter-based wind estimation for 
forest fire monitoring with a quadrotor UAV, in: Proc. IEEE Conf. on Control 
Technology and Applications, CCTA, 2019, pp. 783–788, http://dx.doi.org/10.
1109/CCTA.2019.8920637.
[29] C. Hajiyev, D. Cilden-Guler, U. Hacizade, Two-stage Kalman filter for fault 
tolerant estimation of wind speed and UAV flight parameters, Meas. Sci. Rev. 
20 (1) (2020) 35–42, http://dx.doi.org/10.2478/msr-2020-0005.
[30] A. Tagliabue, A. Paris, S. Kim, R. Kubicek, S. Bergbreiter, J.P. How, Touch the 
wind: Simultaneous airflow, drag and interaction sensing on a multirotor, in: 
Proc. IEEE/RSJ Int. Conf. on Intelligent Robots and Systems, IROS, 2020, pp. 
1645–1652, http://dx.doi.org/10.1109/IROS45743.2020.9341797.
[31] G. Perozzi, D.V. Efimov, J. Biannic, L. Planckaert, Using a quadrotor as wind 
sensor: time-varying parameter estimation algorithms, Internat. J. Control 95 (1) 
(2020) 126–137, http://dx.doi.org/10.1080/00207179.2020.1780324.
[32] S. Zimmerman, M. Yeremi, R. Nagamune, S. Rogak, Wind estimation by multi-
rotor dynamic state measurement and machine learning models, Measurement 
198 (2022) 111331, http://dx.doi.org/10.1016/j.measurement.2022.111331.
[33] S. Allison, H. Bai, B. Jayaraman, Estimating wind velocity with a neural network 
using quadcopter trajectories, in: Proc. AIAA SciTech Forum, 2019, p. 1596, 
http://dx.doi.org/10.2514/6.2019-1596.
Measurement 260 (2026) 119882 
11

## Page 12

H. Yu et al.
[34] A.S. Marton, A.R. Fioravanti, J.R. Azinheira, E.C. de Paiva, Hybrid model-based 
and data-driven wind velocity estimator for an autonomous robotic airship, J. 
Braz. Soc. Mech. Sci. Eng. 42 (2020) 1–11, http://dx.doi.org/10.1007/s40430-
020-2215-8.
[35] H. Yu, X. Liang, X. Lyu, DOB-based wind estimation of a UAV using its onboard 
sensor, in: Proc. IEEE/RSJ Int. Conf. on Intelligent Robots and Systems, IROS, 
2024, pp. 8126–8133, http://dx.doi.org/10.1109/IROS58592.2024.10801906.
[36] Z. Yu, Y. Zhang, B. Jiang, C.-Y. Su, Fault-Tolerant Cooperative Control of 
Unmanned Aerial Vehicles, Springer, 2024.
[37] Z. Yu, M. Li, Y. Zhang, B. Jiang, A review on safety control of unmanned 
aerial vehicles with guaranteed performance requirements, Prog. Aerosp. Sci. 
158 (2025) 101144.
[38] B.J. Emran, H. Najjaran, A review of quadrotor: An underactuated mechanical 
system, Annu. Rev. Control. 46 (2018) 165–180, http://dx.doi.org/10.1016/J.
ARCONTROL.2018.10.009.
[39] T. Tomic, C. Ott, S. Haddadin, External wrench estimation, collision detec-
tion, and reflex reaction for flying robots, IEEE Trans. Robot. 33 (6) (2017) 
1467–1482, http://dx.doi.org/10.1109/TRO.2017.2750703.
[40] R.W. Deters, G.K.A. Krishnan, M.S. Selig, Reynolds number effects on the 
performance of small-scale propellers, in: Proc. AIAA Appl. Aerodyn. Conf., 2014, 
p. 2151, http://dx.doi.org/10.2514/6.2014-2151.
[41] B. Yuksel, C. Secchi, H.H. Bülthoff, A. Franchi, A nonlinear force observer for 
quadrotors and application to physical interactive tasks, in: Proc. IEEE/ASME 
Int. Conf. on Advanced Intelligent Mechatronics, AIM, 2014, pp. 433–440, http:
//dx.doi.org/10.1109/AIM.2014.6878116.
[42] S. Wornom, H. Ouvrard, M.V. Salvetti, B. Koobus, A. Dervieux, Variational 
multiscale large-eddy simulations of the flow past a circular cylinder: Reynolds 
number effects, Comput. & Fluids 47 (1) (2011) 44–50.
[43] M. Zheng, X. Lyu, X. Liang, F. Zhang, A generalized design method for learning-
based disturbance observer, IEEE/ASME Trans. Mechatron. 26 (1) (2020) 45–54, 
http://dx.doi.org/10.1109/TMECH.2020.2999340.
[44] J. Brandt, M. Selig, Propeller performance data at low reynolds numbers, in: 
AIAA Aerosp. Sci. Meeting, 2011, p. 1255, http://dx.doi.org/10.2514/6.2011-
1255.
Measurement 260 (2026) 119882 
12
