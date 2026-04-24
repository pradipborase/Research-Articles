# Identifying Aerodynamics of Delta-Wing Drones for Model-Based Navigation A Comparative Study,.pdf

## Page 1

Received 16 May 2024, accepted 16 June 2024, date of publication 1 July 2024, date of current version 10 July 2024.
Digital Object Identifier 10.1109/ACCESS.2024.3421579
Identifying Aerodynamics of Delta-Wing
Drones for Model-Based Navigation:
A Comparative Study
PASQUALE LONGOBARDI
∗, AMAN SHARMA
∗, AND JAN SKALOUD
Laboratory of Cryospheric Sciences, Ecole Polytechnique Fédérale de Lausanne (EPFL), 1950 Sion, Switzerland
Corresponding author: Pasquale Longobardi (pasquale.longobardi@epfl.ch)
This work was supported in part by European Union’s Horizon 2020 Research and Innovation Program under the Marie Skłodowska-Curie
grant agreement No. 754354, and in part by Swiss Le Département fédéral de la défense, de la protection de la population et des sports
[Federal Department of Defence, Civil Protection and Sport (DDPS)] (Armasuisse) under Contract ARF00-009.
∗Pasquale Longobardi and Aman Sharma are co-first authors.
ABSTRACT This paper presents a comparative analysis of two methodologies for estimating unknown
parameters in a Vehicle Dynamic Model (VDM)-based sensor fusion framework for small drones. Focusing
on a delta-wing drone, we conduct open-air wind tunnel experiments to determine a functional aerodynamic
model. Subsequently, we compare two methodologies for unknown model parameters identification, one
based on linear regression on wind tunnel experimental data, and the other employing partial-update-
based estimators on recorded flight data. The performance of both parameter estimation approaches is
then evaluated in a VDM-based framework through three independent test flights. Our results highlight the
necessity of wind tunnel experiments for aerodynamic model formulation, while the data-driven method
proves useful to identify the parameters at a low cost. Furthermore, we demonstrate that both (flight)
data-driven and wind-tunnel experiment-based identified aerodynamics significantly enhance positioning
accuracy, particularly in the absence of satellite signals, when integrated with low-cost consumer-grade
MEMS inertial sensors.
INDEX TERMS
Aerodynamics, delta-wing drone, extended Kalman filter, model-based navigation,
observability Gramian, Schmidt-Kalman filter, wind-tunnel.
I. INTRODUCTION
A typical integrated navigation system [1], [2] on a drone
comprises the i) Global Navigation Satellite System (GNSS)
and ii) Inertial Navigation System (INS). Fusion of low-
frequency PVT1 data from GNSS with the high-frequency
PVA2 data from INS results in sufficient short and long-term
accuracy. However, during a GNSS outage, while vertical
positioning can be effectively secured using a barometer,
horizontal positioning accuracy is primarily dictated by the
quality of the Inertial Measurement Unit (IMU). For small
drones, with consumer-grade MEMS IMU, the position
uncertainty rapidly becomes nonviable after a minute of
GNSS denial [3]. In this study, we make use of a low-cost
The associate editor coordinating the review of this manuscript and
approving it for publication was Jiankang Zhang
.
1Position Velocity Time.
2Position Velocity Attitude.
IMU, present on a readily available open-source autopilot,
to motivate the benefits of model-based navigation over
conventional GNSS/INS fusion.
A. VEHICLE DYNAMIC MODEL BASED NAVIGATION
Lately, [3] proposed a so-called Vehicle Dynamic Model
(VDM) based navigation system, applicable to small drones,
in which a mathematical model of aerodynamic forces and
moments is used to fuse the sensors such as GNSS, IMU,
and barometer, via an Extended Kalman Filter (EKF). In this
framework, the aerodynamic model is used to carry out
the EKF-prediction step, whereas sensor measurements lead
to an EKF update. This is somewhat in contrast to the
conventional GNSS/INS fusion, wherein an IMU measure-
ment results in the EKF prediction while a GNSS-based
update is common in both approaches. Before [3], other
variants of VDM-based navigation [13], [14], [15], [16],
VOLUME 12, 2024
 2024 The Authors. This work is licensed under a Creative Commons Attribution 4.0 License.
For more information, see https://creativecommons.org/licenses/by/4.0/
91649

## Page 2

P. Longobardi et al.: Identifying Aerodynamics of Delta-Wing Drones for Model-Based Navigation
TABLE 1. Summary of related works in the context of VDM and positioning of presented research.
[17], [18] existed which either: i) overlooked the wind,
ii) excluded in-flight refinement of model-parameters,
iii) partially utilized VDM for navigation, iv) utilized VDM
with high-accuracy IMUs, or iv) limited the studies to
simulations. Thus, we base our model-based navigation
system on the architecture presented in [3]. Nevertheless, it is
important to note that while [3] focused on conventional-
fixed-wing drones (with three independent control surfaces),
our work analyses the employment of VDM on delta-wing
drones for autonomous navigation.
B. DELTA-WING DRONES
Delta-wing drones, often interchangeably labeled as flying
wings in literature, are tailless aircraft frequently char-
acterized by a blended-wing-body design, enabling the
fuselage to actively contribute to lift generation. This
characteristic grants them increased aerodynamic efficiency
compared to traditional aircraft configurations, making them
highly attractive for missions necessitating extended flight
autonomy. The absence of a rudder increases the complexity
of flight dynamics of these platforms, as both longitudinal
and lateral maneuvers exclusively rely on the deflection of
two control surfaces, known as elevons, situated on the wings.
Several studies [19], [20], [21], [22], [23] have examined
the aerodynamics of such platforms using different methods,
but they predominantly rely on existing benchmark model
formulations adapted from conventional aircraft configura-
tions. These formulations were not specifically tailored for
VDM-based navigation and as such have a large number
of parameters. Their direct employment within the VDM
framework leads to an undesired interdependence among
states and high computational cost [11].
C. RELATED WORKS
1) MODEL PARAMETERS DETERMINATION
The importance of reasonable prior knowledge of the model
parameters, used in the VDM-EKF framework, has been
accentuated in [9] and [24] for both a simulation and
a practical setting, asserting that insufficient knowledge
may lead to filter divergence due to numerical instabilities.
Consequently, a reliable aerodynamic characterization of the
employed platform is necessary to preclude such issues.
Throughout the literature, four main approaches for determin-
ing the numerical values of aerodynamic model parameters
are identified; they are listed in the following paragraphs.
Furthermore, a tabulated summary of some of the closest
approaches (in terms of usage of VDM for navigation) in
contrast to our study is presented in Table 1. In this table,
we broadly compare the different approaches in terms of
i) the used fixed-wing drone; ii) whether the studies propose
a functional model or not (for instance, using an existing
model structure); iii) whether the aerodynamic model is used
for VDM-based navigation; iv) whether the study presents
a comparison between different aerodynamic parameter
estimation techniques for VDM-based navigation. That being
said, it should be noted that (different) existing methods have
used different drones with different aerodynamic models and
parameter estimation techniques; thus, in our study, we have
focused on one delta-wing drone with an aerodynamic model,
common to the two approaches, used for identifying the
model parameters.
Semi-empirical methodologies employing the US Data
Compendium (DATCOM) have been adapted to flying wings
with unconventional design in [21], [22], and [23] to coarsely
identify model parameters values based on interpolation of
a vast array of aircraft data. However, this methodology has
rather low accuracy particularly when transitioning to small
drones characterized by sensibly different sizes and flight
speeds, and often requires further experimental validation.
Conventional wind tunnel (WT) testing is a well-
established method for aerodynamic assessments, but it
mainly offers static aerodynamic data. This limitation is
particularly problematic for highly agile tailless drones
operating in dynamic flight conditions and relying solely on
this method may not ensure the determination of an accurate
predictive model. Furthermore, they are often too expensive,
time-consuming, and laborious for small drones applications.
Numerical approaches such as CFD3 present the advan-
tage of not requiring external hardware to compute the plat-
form aerodynamic behavior. However, specific knowledge of
3Computational Fluid Dynamics.
91650
VOLUME 12, 2024

## Page 3

P. Longobardi et al.: Identifying Aerodynamics of Delta-Wing Drones for Model-Based Navigation
the drone geometry and of the operational flight boundary
conditions are required for such analysis, together with soft-
ware operator expertise. Furthermore, computational results
often require validation against experimental results [4].
System identification utilizing real-flight data offers a
compelling alternative to the aforementioned approaches,
bypassing the need for specialized facilities and complex
numerical flow modeling. However, its drawback lies in
limited aerodynamic observability, as it solely reflects flight
envelope data. Employing standard models found in the
literature for tailless drones, such as in [25], can result in the
development of interstate correlations and poor model-based
navigation performances [9].
Other approaches:Apart from the above approaches,
it appears that the study by [3] has utilized prior aerodynamic
knowledge of the conventional-fixed-wing drones, which was
then further refined in a long flight within the Bayesian
setting of the VDM-EKF framework. Another refinement
methodology [8] uses absolute attitude from photogrammet-
ric techniques in the same VDM-EKF framework. However,
both refinement techniques depend on a reasonable prior
knowledge of the vehicle aerodynamics that may not be
available for every drone. To address these concerns, [10]
proposed an experimental methodology based on open-air
wind tunnel (WT) testing, to determine an aerodynamic
model formulation suitable for model-based navigation.
Furthermore, a drone-independent method to identify the
model parameters from recorded-flight data has been pro-
posed in [9]. This data-driven approach uses three cascaded
linear estimators to identify a priori values of the unknown
model parameters via a combination of the partial-update
Schmidt Kalman Filter [26] and a heuristic based on the
observability Gramian [27]. This approach is referred to
as WMF and does not rely on prior knowledge of vehicle
aerodynamics; thus it strives to be an inexpensive substitute
for wind-tunnel experiments and CFD analysis for model-
based navigation [9].
2) VDM FOR DELTA-WING DRONES
In [28], the authors employ the aforementioned VDM-based
architecture [3] for a delta wing drone relying on a general
formulation of the drone aerodynamic model composed
of 44 parameters. However, no details about the origin
of the model are presented and the practical validation is
limited to only one flight. Following that, [5] proposed
another aerodynamic model with 23 parameters using the
D-optimal selection criterion for model selection, however,
the integration of this model within a VDM-EKF framework
was not explored further. Thereafter, [12] presented an
experimental methodology, based on step-wise regression to
model the aerodynamics and identify the unknown model
parameters using open-air-wind tunnel testing and a serial
robot. The selected model consists of 17 parameters that
are eventually incorporated into the VDM-based navigation
system and rigorously tested over multiple flights, resulting
in excellent mitigation of positioning inaccuracy during long
GNSS outages [10]. However, in the absence of a wind tunnel
facility, the identification of the unknown model parameters
remains a challenge.
3) OTHER APPROACHES TO GNSS DENIED NAVIGATION
The model-based frameworks in [7], [8], [11], [12], and [28]
have shown considerable improvement in positioning accu-
racy of a drone during GNSS outages; nevertheless, there
have also been other approaches that have striven to achieve
the same without using a VDM. For instance, in [29],
measurements from GNSS, IMU, compass, barometer, and
an airspeed sensor are fused through an EKF; however,
this fusion was tested for a single flight of a manned
glider while introducing a GNSS outage. On the other hand,
another approach referred to as relative navigation relies
on a front-end EKF for the estimation relative to the local
environment; in the back-end, a pose graph is optimized with
constraints from sensors such as camera/lidar to yield global
estimates. Such a framework has been employed in [30] for
a large fixed-wing drone. Yet, most of the existing works
on relative navigation are largely developed for multi-rotor
platforms [30]. Besides this, there are substantial challenges
in using vision-based sensors in case of homogeneous terrain
or foggy/low-visibility scenarios, while the integration of
emitting sensors as lidar or radar with a lightweight drone,
such as ours, would be impractical due to size, weight, and
power constraints. Due to these reasons, we focus on a
VDM-based system for autonomous navigation, in particular
for a delta-wing drone.
D. RESEARCH GAP
Most of the existing works [3], [4], [7], [8], [9], [24],
[31], [32], [33], [34] have focused on the aerodynamic
model of the conventional fixed-wing drone [35] for VDM-
based navigation, while there have been fewer contributions
for the delta-wing drones [10], [11], [12], [28]. Moreover,
according to previous studies [6], model parameters tend
to remain relatively constant, facilitating their estimation
and refinement through calibration flights, thus minimizing
design efforts [6], [7], [8]. Building on this approach, recent
work [28] extended the framework to delta-wing drones,
aiming to identify numerous unknown parameters in the
aerodynamic model. However, this extension was found to
suffer from over-parameterization [9], leading to overfitting
issues, as highlighted by subsequent studies [11]. To the
best of our knowledge, no prior work has addressed the
combined issue of model selection and validation on a
delta-wing drone, in a VDM-based framework, using both
wind tunnel and flight-data-based methods. Moreover, there
appears to be a gap of knowledge in the comparison of the
performance of the model parameters identified by the two
approaches in terms of cost, effectiveness, time, skill set, and
engineering requirements. Secondly, [9] has remarked that
the choice of IMU quality, for the flight-data-based method,
is an important factor affecting model-parameter estimation.
Although the authors [9] have presented preliminary results
VOLUME 12, 2024
91651

## Page 4

P. Longobardi et al.: Identifying Aerodynamics of Delta-Wing Drones for Model-Based Navigation
for the comparison of the two IMU types, they have also
clearly stated the need for a thorough statistical analysis.
As far as we can ascertain, there appears to be no other work
that has studied the impact of the identification and validation
of aerodynamics while using consumer-grade IMU, found in
readily available autopilots, for model-based navigation.
E. PROPOSITION
To address the above gap of knowledge: i) we manipulate
a delta-wing drone using a robotic arm in an open-air
wind tunnel to select an aerodynamic model and deduce
the numerical values of the corresponding model parameters
using step-wise regression [12]; ii) record the flight data
consisting of IMU, GNSS, control surface deflection, pro-
peller speed, airspeed using PX4 autopilot; iii) we use the
approach introduced in [9] to identify the values of unknown
parameters of the model-selected in step i; iv) we conduct
three field tests and simulate a 3-minute-long GNSS outage,
in a post-processing scenario, to evaluate the performance of
the model-parameters identified by wind-tunnel experiments
and flight-data-based method [9]; v) subsequently, we present
a statistical comparison of the two methods.
F. PAPER ORGANIZATION
The paper begins by providing relevant background on the
existing works related to VDM-based navigation in Sec. II.
Next, we present the experimental setup in Sec. III, followed
by the navigation results during GNSS outages in Sec. IV.
Lastly, a discussion on certain nuances is presented in Sec. V
and concluding remarks in Sec. VI.
II. BACKGROUND
A. NOTATIONS AND CONVENTIONS
1) REFERENCE FRAMES
A pictorial representation of the different frames used in this
paper is depicted in Fig. 1; with the nomenclature as follows:
i
Earth-centered-inertial frame (ECI).
e
Earth-centered earth-fixed frame (ECEF).
l
Local level navigation frame: North, East, and Down
(NED).
b
Body frame: forward, right, and down (FRD).
s
reference frame attached to the IMU.
w
wind reference frame.
A reader may refer to [2] and [6] for a more detailed
description of these reference frames.
2) MOTION VARIABLES
Cf2
f1
Rotation matrix from the reference frame f1 to f2
ωf3
f1f2
Angular velocity of the reference frame f2 with
respect to f1, expressed in f3
f3
f1f2
Angular velocity of the reference frame f2 with
respect to f1, expressed in f3, in skew-symmetric
matrix form.
 =


0
−ω3 ω2
ω3
0
−ω1
−ω2 ω1
0

with ω =


ω1
ω2
ω3


FIGURE 1. Reference frames. V represents (relative) airspeed vector.
qf2
f1
Quaternion representation of the rotation from
reference frame f1 to reference frame f2:
q = w + ix + jy + kz with
i2 = j2 = k2 = ijk = −1
{w, x, y, z} ∈R
q1 ⊗q2 Quaternion product of q1 and q2 [36].
re
Position of an object in the ECEF frame using
ellipsoidal coordinates parameterized by {φ, λ, h}
representing latitude, longitude, and height.
vl
Velocity of an object in the local-level frame.
D−1
Transformation matrix from Cartesian to ellipsoidal
coordinates [2], [6].
[ω]q
Quaternion representation of ω.
[ω]q = 0 + iω1 + jω2 + kω3
ff1
Specific force in the reference frame f1.
rf3
f1f2
Lever-arm between the origins of reference frames
f1 and f2, expressed in f3.
gf1
Gravity vector in the reference frame f1.
3) AERODYNAMIC VARIABLES
wl
Wind velocity in the local-level frame.
91652
VOLUME 12, 2024

## Page 5

P. Longobardi et al.: Identifying Aerodynamics of Delta-Wing Drones for Model-Based Navigation
α
Angle of attack.
β
Side slip angle.
V
Airspeed.
ωp
Drone’s propeller speed.
δℓ
Deflection of left control surface.
δr
Deflection of right control surface.
ρ
Air density.
J
Inertia tensor.
b
Wing span.
¯c
Mean aerodynamic chord.
S
Wing surface area.
m
Mass of the drone.
Dp
Diameter of the propeller.
J
Advance ratio.
B. VDM-BASED NAVIGATION SYSTEM
In this section, we briefly review the state-space formulation
of the VDM-based navigation system.
˙re = D−1vl
(1)
˙vl = gl + Cl
bfb −

2l
ie + l
el

vl
(2)
˙ql
b = 1
2ql
b ⊗
h
ωb
ib −(Cb
l )T 
ωl
ie + ωl
el
i
q
(3)
˙ωb
ib = (J)−1 
Mb −b
ib

Jωb
ib

(4)
˙xcoeff = 0
(5)
˙wl = 0
(6)
˙bf = 0
(7)
˙bω = 0
(8)
Here, fb
=
fF(A, xcoeff) and Mb
=
fM(A, xcoeff)
altogether represent the aerodynamic model of the drone.
Later, in Sec. IV-A1, a model is selected using step-
wise regression. Note that A denotes a set of aerodynamic
variables defined in Sec. II-A3; xcoeff ∈Rp denotes the
unknown model-parameters, specific to the operating drone.
Additionally, {bf , bω} denote accelerometer and gyroscope
errors, modeled here as a constant bias. The state-dynamics
defined by equations (1)-(8) alongside observation models of
GNSS, IMU, and barometric altimeter are implemented in a
sensor fusion framework utilizing an Extended Kalman Filter
(EKF). For more details, we refer the readers to [3] and [6].
C. WMF METHOD: FLIGHT-DATA BASED IDENTIFICATION
OF AERODYNAMICS
In [9], the authors propose a three-step procedure for
identifying aerodynamic model parameters, xcoeff, of fixed-
wing drones using sensor data: IMU, GNSS, autopilot control
commands and a pitot tube. Here, xcoeff = [cT
f
cT
m]T with
cf , cm denoting the parameters associated with forces and
moments respectively.
To execute this approach, the aforementioned sensor data
are collected in a calibration flight with sufficient maneuvers.
Subsequently, the following three estimators are sequentially
implemented to obtain the unknown model parameters.
The approach is briefly reviewed here for the sake of
completeness; for more details, we refer the reader to [9].
1) STEP-1: WIND ESTIMATION
The state dynamics for wind estimation are given by
wl
k+1
γk+1

=

wl
k
γk

+
νwk
νγk

(9)
with γ representing the pitot scale factor; {νwk, νγk} denoting
white noise. Meanwhile, the observation model is of the
following form:
zk = h(wl
k, γk) = dT Rb
lkwl
k + ukγk + νk,
(10)
with d
=
[ 1 0 0 ], u being the airspeed measured by
the pitot, z is the drone’s longitudinal velocity, obtained
as a result of post-processed sensor fusion (INS/GNSS);
and ν denotes measurement noise, modeled as white noise.
A Schmidt-Kalman filter [26], with selective update, based
on observability Gramian, is used for wind estimation.
2) STEP-2: MOMENT-PARAMETER ESTIMATION
After having estimated the wind, gyroscope measurements
are numerically differentiated using a higher-order differ-
entiator to obtain ˙ωb
ib. Subsequently, a linear system of the
following form is deduced:
zm = Hmcm + νm with
zm = 1
¯qS

J ˙ωb
ib + ωb
ib × Jωb
ib

(11)
where νm denotes white noise, ¯q = 1
2ρV 2; Hm is a function of
A, defined in equation (30) after model selection. A necessary
condition for this formulation to work is that the aerodynamic
model is a linear function of the unknown parameters. This
system is solved using partial-update-based recursive least
squares, where the update metric is based on the observability
grammian.
3) STEP-3: FORCE-PARAMETER ESTIMATION
After having estimated both the moments and the wind,
the following linear system is formulated to estimate the
unknown force parameters:
z′
f = Hf cf + νF with,
z′
f = zf −ωb
ib × ωb
ib × rb
bI
−
h
(J)−1 
Mb −ωb
ib × Ibωb
ib
i
× rb
bI
(12)
Here. νF denotes white noise and Hf is a function of A, later
defined in equation (31) after the force model is selected. It is
assumed that the aerodynamic model is a linear function of
the force model parameters and the system is solved in a way
similar to that of the moment estimator in Step 2.
As this method consists of following sequential estimators,
wind, moment and force, we shall refer to it as the WMF
method for brevity.
VOLUME 12, 2024
91653

## Page 6

P. Longobardi et al.: Identifying Aerodynamics of Delta-Wing Drones for Model-Based Navigation
D. WT METHOD: OPEN-AIR WIND-TUNNEL BASED
IDENTIFICATION OF AERODYNAMICS
In [12], the authors employ an alternative approach to
conventional wind tunnel testing that relies on an open-air
wind tunnel set-up. At the same time, a robotic arm is
employed for repositioning the drone and lowering the
experimental run-time compared to a traditional wind tunnel
setup. Such experiments provide the total aerodynamic force
fb and torque Mb acting on the test platform during different
testing scenarios. These quantities comprise the combined
effect of platform and propulsion system aerodynamics,
formulations of which are detailed in the following.
1) PLATFORM AERODYNAMICS
Following the traditional decomposition of longitudinal and
lateral dynamics, the aerodynamic behavior of the platform
can be characterized by a system of six equations. The
aerodynamic force is projected in the wind reference frame
and is broken down into components known as Drag (D),
Side force (Y), and Lift (L). The total aerodynamic moment
with respect to the platform’s center of gravity is expressed in
the drone body frame. The individual components are defined
as Roll moment (Mx), Pitch moment (My) and Yaw moment
(Mz). The selection of these reference frames is driven by
the linear interdependence exhibited by these force and
moment components concerning aerodynamic variables in
this particular configuration. This facilitates the formulation
of an aerodynamic model that is both simple and effective.
Furthermore, these force and moment components are made
dimensionless to render independence from flight conditions
and drone size:
CD = D
¯qS , CY = Y
¯qS , CL = L
¯qS
(13)
CMx = Mx
¯qSb, CMy = My
¯qS¯c, CMz = Mz
¯qSb
(14)
where CD, CY , CL, CMx, CMy, CMz take the name of
aerodynamic coefficients.
2) PROPULSION SYSTEM AERODYNAMICS
As outlined in [12], and consistent with prior findings detailed
in [37], the dynamics of the propulsion system can be broadly
defined through the ensuing thrust and torque equations
expressed within the body frame:
T b(J, ω) = CT0 · ρ · D4
p · ω2
p + CT1 · ρ · D4
p · J · ω2
p
(15)
Qb(J, ω) = CQ0 · ρ · D5
p · ω2
p + CQ1 · ρ · D5
p · J · ω2
p
(16)
where the advance ratio J is defined as:
J = V/ωp
(17)
3) AERODYNAMIC MODEL IDENTIFICATION
The data collected during open-air wind tunnel experiments
are used to determine candidate models for model-based
FIGURE 2. Concorde S delta wing drone (left), CAD model (right).
applications on a delta-wing drone. Notably, we propose
the use of step-wise regression to incrementally construct
the functional model leveraging the statistical significance
of the explanatory variables. Such variables belong to three
categories: i) flight variables α, β, ii) control variables δℓ, δr
and iii) dynamic variables ωb
ib. Addition (forward selection)
and removal (backward elimination) of explanatory variables
within the model is based on their statistical significance in
the form of the coefficient of determination R2 [38].
4) INTEGRATION IN THE DYNAMIC MODEL
Once the aerodynamic coefficients and propulsion dynamics
are determined, they are altogether integrated into the vehicle
dynamic model, see equations (2) and (4), as follows:
fb = 1
m0




T b
0
0

+ (Rw
b )T


¯qSCD
¯qSCY
¯qSCL




(18)
with Rw
b =


cos β
sin β 0
−sin β cos β 0
0
0
1




cos α 0 sin α
0
1
0
−sin α 0 cos α


and Mb =


¯qSbCMx + Qb
¯qS¯cCMy
¯qSbCMz


(19)
III. EXPERIMENTAL SETUP
A. DRONE AND AVIONICS
The delta-wing drone employed for this analysis is the
Concorde S, a custom-made platform developed at the
Swiss Federal Institute of Technology of Lausanne (EPFL)
which is shown in Figure 2. It is based on a commercially
available hobby flying wing, the Xeno electric, modified
to accommodate a larger payload bay and an upscaled
propulsion system.
The onboard avionics are detailed in Table 2.
Notably, the Pixhawk 4 autopilot contains two sets of
MEMS IMUs, a barometer and a magnetometer.
B. WIND-TUNNEL FACILITY
The experimental facility, situated in the Laboratory of
Intelligent Systems at EPFL, is depicted in Figure 3.
It comprises four parts: i) a Windshaper wind generator [39],
ii) a robotic arm that automatically adjusts the orientation
of a UAV with respect to the generated airflow, eliminating
the need for manual repositioning, iii) a 6-axis ATI4 load cell
4https://www.ati-ia.com/products/ft/sensors.aspx
91654
VOLUME 12, 2024

## Page 7

P. Longobardi et al.: Identifying Aerodynamics of Delta-Wing Drones for Model-Based Navigation
TABLE 2. Avionics on the Concorde S.
FIGURE 3. Experimental set-up.
to measure forces and torques and iv) OptiTrack,5 a motion
capture system used to follow and record the Concorde S
attitude trace.
C. FLIGHTS
The analysis presented in this comparative study relies on
four different flights performed utilizing the Concorde S
drone. Notably, one of the deployed flights is used as a
calibration dataset for the estimation of the aerodynamic
coefficients using the data-driven approach based on the
observability Gramian. The remaining flights provide a
testing dataset, allowing us to assess the performance of the
approaches compared in this study. To ensure the validity and
integrity of the solution, we rely on flight data characterized
by different dynamics and external conditions. On one hand,
manually controlled portions of the trajectory permit a variety
of maneuvers both in the longitudinal and lateral plane.
On the other hand, we use mission mode control to investigate
the impact of different flight conditions, dictated by the
external wind perturbation, on reproducible trajectories.
5https://optitrack.com/
TABLE 3. Summary of the flights. CF: calibration flight; TF: test flight.
FIGURE 4. Calibration and testing flights.
Figure 4 illustrates the flights utilized in this study with their
main characteristics summarised in Table 3.
D. REFERENCE TRAJECTORY
We deploy Concorde S, equipped with a dedicated pay-
load, described in Sec. III-A, for collecting IMU and
GNSS data during the mission. Throughout the mission,
a GNSS base station, with JAVAD Triumph-LS, a multi-
constellation/multi-frequency receiver, logs code and phase
signals for at least L1 and L2 on GPS and GLONASS.
This data is recorded at 10 Hz and is crucial for a precise
differential Post-Processed Kinematic (PPK) solution. This
data from the base station is combined with the data from
JAVAD-TR2S, which is mounted on the payload, using Iner-
tial Explorer version 8.5-9 by NovAtel Inc. (2020) to obtain
PPK solution: precise position and velocity information. This
information is then integrated with inertial data through
optimal smoothing using the INS/GNSS software POSProc
by Applanix Corporation, resulting in a reference trajectory.
This methodology has been adopted from [9].
E. EXPERIMENTAL METHODOLOGY
1) STEP-1: WIND-TUNNEL (WT) AERODYNAMICS
CHARACTERIZATION
The wind tunnel facility, described in Sec. III-B, is utilized
to understand the aerodynamic behavior of the drone under
different conditions and translate this understanding into
a model. To accomplish this, the load cell measurements
VOLUME 12, 2024
91655

## Page 8

P. Longobardi et al.: Identifying Aerodynamics of Delta-Wing Drones for Model-Based Navigation
FIGURE 5. Experimental workflow.
comprising forces and torques are recorded together with the
drone’s attitude while the robotic arm manipulates it. The
measured forces and moments include aerodynamics, gravity,
and inertia contributions. To recuperate the contribution of
aerodynamics from the rest, two types of experiments are
conducted: one without wind and another with controlled
airflow via the Windshaper. Cross-correlation is then used
to align and subtract the results of these two experiments,
revealing the specific aerodynamic data; this data is then used
to determine a functional model and the numerical values of
its parameters. This experimental workflow is illustrated in
Figure 5.
The above-obtained model is then integrated within
the VDM-EKF framework, with the initial values of the
unknown parameters, xcoeff, obtained using the two con-
sidered approaches. While the initial values are available
for the WT method, a calibration flight is utilized for
identifying these parameters for the WMF method (see
Step-2b below). Furthermore, this flight is reused for refining
the initial WT-based values (see Step-2a below) to account
for the differences between the laboratory and the real flight
conditions.
2) STEP-2A: ADAPTING WT-BASED PARAMETERS TO
REAL-FLIGHT
The numerical values of the aerodynamic model parame-
ters determined from the wind tunnel data via step-wise
regression do not represent the best estimate for model-based
navigation. This is mainly due to i) differences between
wind tunnel and real flight conditions and ii) different con-
figuration and boundary conditions among different flights.
Therefore, to account for such discrepancies, we follow
a two-phase procedure to fine-tune the model parameter
estimates. The first phase, named Coarse adjustment, relies
on the augmented state vector correction methodology of [3]
leveraging post-processed data from the reference trajectory
introduced in the previous section III-D. This phase permits
compensation of discrepancies between the wind tunnel
testing and real flight conditions. The second phase, named
Fine adjustment is common to the two methodologies and
will be detailed in Step 3.
FIGURE 6. WMF methodology: image courtesy [9]. IIR: infinite impulse
response, PVAT: position, velocity, attitude, time obtained from IMU/GNSS
fusion.
FIGURE 7. Schematics of the coefficient adjustment phases.
3) STEP-2B: IDENTIFYING PARAMETERS USING WMF
METHOD
The functional model obtained after Step-1 is used for
employing the WMF method (see Sec. II-C). This results
in the identification of the Coarse coefficients values of the
model. An illustration of this methodology is depicted in
Fig. 6.
4) STEP-3: IDENTIFYING FINAL MODEL PARAMETERS
VALUES FOR WT AND WMF METHODS
The two sets of model parameter values hence obtained
are then utilized as a priori estimates for the vehicle
dynamic model-based navigation (see Sec. II-B). During
the test flight, the Fine adjustment calibration phase is then
performed leveraging error state compensation using single-
point-positioning GNSS data as recorded on the onboard
autopilot. This phase accounts for a small variability of drone
properties (e.g. payload shift, accumulated wing damage)
among different flights.
Figure 7 provides schematics of the employed procedure.
To evaluate the performance of these approaches, we sim-
ulate a 3-minute-long GNSS outage in the three test flights
described in Fig. 4 and Table 3 and analyse the position-drift
of the two trajectories to draw relevant conclusions.
91656
VOLUME 12, 2024

## Page 9

P. Longobardi et al.: Identifying Aerodynamics of Delta-Wing Drones for Model-Based Navigation
FIGURE 8. Step-wise regression plots for wind tunnel experiments.
IV. RESULTS
Following the methodology formerly detailed in Sec. III-E,
we deduce an aerodynamic model structure of Concorde
S using step-wise regression applied on wind tunnel data.
Then, we identify the value of the aerodynamic coefficients
independently using WMF/WT methods and test them
separately in the VDM-EKF framework.
A. MODEL SELECTION
The chosen statistics for model construction using step-wise
regression is the coefficient of determination R2 ∈[0, 1].
Adding a regressor to the model causes an increase in the
R2 value proportional to the importance of the explanatory
variable within the model. The chosen stopping criterion is
when adding a new term in the model causes an increase
of R2 inferior to 0.01. Figure 8 illustrates the coefficient
of determination plots, hereby constructed using data from
open-air wind tunnel experiments, for the force and moment
equations. The information contained in these plots is
employed for model selection.
1) AERODYNAMIC MODEL
It is crucial to emphasize that selecting a model, based on the
maximization of the coefficient of determination, does not
inherently translate to enhanced predictive qualities of such
a model. Specifically, in the context of model-based navi-
gation, the indiscriminate inclusion of explanatory variables
may result in the development of correlations among them.
This potentially leads to detrimental effects on autonomous
navigation performance, as highlighted in [7] and [11]. After
testing several models, we chose the following formulation
that seems to be an optimal compromise achieving good
predicting capabilities with a minimal number of parameters:
CD = CD0 + CDα2α2
(20)
CY = CY0 + CYββ
(21)
CL = CL0 + CLαα
(22)
CMx = CMx0 + CMxδaδa
(23)
CMy = CMy0 + CMxδeδe
(24)
CMz = CMzββ
(25)
Due to the inherent separation of longitudinal and lateral
dynamics within the chosen set of equations, the elevons left
and right deflections denoted as δℓand δr, are combined and
subsequently remapped as symmetrical and asymmetrical
deflections. The symmetrical deflection acts in the longitu-
dinal plane and it is hence called elevator effect δe while the
asymmetrical deflection impacts the lateral dynamics and is
referred to as aileron effect δa.
δa
δe

= 1
2
1 −1
1 1
 δℓ
δr

(26)
Initially, the interaction term CMzδeδa was considered
due to its prominent correlation with yawing maneuvers,
as illustrated by the stepwise regression plots in Figure 8.
However, the observability of this variable was found to
be lacking in the recorded flight data. Figure 9 illustrates
the range of values exhibited by the variable during the
calibration flight (CF) in comparison to those observed during
wind tunnel experiments (WT). In this figure, the variation
range for the former is found to be significantly lower than
the latter. This means that a WT setup has substantially higher
persistence of excitation [40] as compared to non-acrobatic
flight with nominal autopilot stabilization. Furthermore and
as explained earlier, the inclusion of δa explanatory variable
causes (interstate) correlation with the rolling moment which
in turn hinders the usage of WMF methodology. To ensure
a fair comparison between both (WT vs WMF) approaches,
a common model structure was adopted, where parameters
are observable in both cases. Consequently, the parameter β,
whose range of values during the calibration flight (CF) and
wind-tunnel experiments (WT) is depicted in Figure 10, was
employed for the formulation of the ‘‘yawing model’’ CMz.
In contrast to Figure 9 the range of the explanatory variable
is comparable between both methods.
Consequently, including the propulsion system dynamics
(Eq. 15 and 16), the unknown model parameters for force and
torque characterization are:
cf =
CD0 CDα2 CY0 CYβ CL0 CLα CT0 CT1
T
(27)
cm =
CMx0 CMxδa CMy0 CMxδe CMzβ CQ0 CQ1
T
(28)
Combined, they form in the parameter state vector xcoeff in
Eq. 5.
xcoeff = [cT
f cT
m]T
(29)
VOLUME 12, 2024
91657

## Page 10

P. Longobardi et al.: Identifying Aerodynamics of Delta-Wing Drones for Model-Based Navigation
FIGURE 9. Range of the δeδa explanatory variable for real flight data (CF)
and wind-tunnel experimental data (WT).
FIGURE 10. Range of the β explanatory variable for real flight data (CF)
and wind-tunnel experimental data (WT).
2) WMF FORMULATION FOR THE CHOSEN MODEL
Based on the aerodynamic model above in Sec. IV-A1, the
matrix, Hm (see equation (11)), required for WMF method is
obtained as
Hm = Dm


1 δa
ρD5
pω2
p
¯qSb
ρD5
pVωp
¯qSb
0 0 0
0 0
0
0
1 δe 0
0 0
0
0
0 0 β


with Dm = diag(b, ¯c, b)
(30)
Similarly, the matrix, Hf (see equation (12)) is deduced as:
Hf = 1
m

A32 (Cw
b )T A36

with A32 =


ρD4
pω2
p ρD4
pVωp
0
0
0
0


and A36 =


1 α2 0 0 0 0
0 0 1 β 0 0
0 0 0 0 1 α


(31)
Once these matrices are deduced, the WMF method is
employed to obtain the unknown model parameters, which
are then utilized in the VDM-based navigation system.
TABLE 4. Pixhawk 4 IMU noise characteristics.
B. REFINEMENT OF AERODYNAMIC MODEL PARAMETERS
Once the model (Step 1) and the apriori estimates of the
model parameters (Step 2a-b), see equations (27)-(28), are
determined, all the components for implementing the EKF
are at hand. In this section, we detail some of the important
parameterization details of the filter.
The VDM-EKF framework needs to be initialized while
the drone is airborne [3]. For that, we employ the navigation
states (position, velocity, and attitude) and their covariance
from a standard INS/GNSS fusion result obtained from the
autopilot logs. All other states and their covariance are ini-
tialized through configuration files. When the aerodynamic
model parameters from WMF are utilised as a priori state
estimates, the initial covariance is set as a diagonal matrix
consisting of values equalling to the square of the standard
deviation (SD). The SD value of each parameter is set
to 5% of its magnitude. This value equals 0.1% in the
case of WT-based parameters. Although these values were
obtained as a result of empirical testing, the difference in
their magnitude demonstrates the confidence in their initial
estimates, which for the WT method is indeed larger than
WMF. The wind velocity is initialized with 0 and the SD for
horizontal wind is set to 1.3 m/s, whereas it is 2 cm/s for the
vertical. The biases of the accelerometer and gyroscope are
indeed slightly tricky to initialize as Pixhawk4 has two sets
of onboard IMUs, tabulated in Table. 4. The initial values of
the biases are set to 0 with SD close to the mean (slightly
bloated) of the two IMUs. It should be noted that the IMU
bias is 1−2 orders of magnitude higher than those used in [9].
C. COMPARISON OF FLIGHT-DATA-BASED AND
WIND-TUNNEL IDENTIFIED MODEL-PARAMETERS VALUES
After having selected the aerodynamic model, presented
in Sec. IV-A, we employ the VDM-EKF framework to
fuse the IMU, GNSS, barometer, and autopilot control
commands separately with each set of aerodynamic model
parameters: obtained by i) wind tunnel experiments (WT)
and ii) flight-data-based approach (WMF). The performance
of autonomous navigation utilizing these parameters is
subsequently evaluated in three test flights, namely TF-1,
TF-2, TF-3, each comprising a three-minute-long GNSS
outage. The planimetric view of the obtained trajectory, for
the three flights, is shown in Fig. 11, showcasing comparable
performance by both the sets of model parameters. Fur-
thermore, the horizontal positioning error of the VDM-EKF
framework is juxtaposed with the INS in Fig. 12(a)(c)(e),
showing the latter to be over 10 Km, whereas the former is
91658
VOLUME 12, 2024

## Page 11

P. Longobardi et al.: Identifying Aerodynamics of Delta-Wing Drones for Model-Based Navigation
less than 400 m for the chosen IMU type. That being said,
to better visualize the evolution of the errors of the VDM-
based approach, we zoom the above plots and present them
in Fig. 12(b)(d)(f). Across all the test flights, we find the
maximum error committed by the WMF ranging between
80 m and 380 m, whereas for WT between 60 m and 200 m.
D. COMPARISON TO INERTIAL COASTING
For a more nuanced understanding of the performance of the
two identification approaches, WT and WMF, we analyze the
error growth per minute associated with each approach and
compare it to the inertial coasting. The findings are presented
in Figure 13,14,15 in which we summarize performance
statistics specific to horizontal positioning error for 1,
2, and 3 minutes of GNSS outage respectively. In these
figures, we report the mean absolute error (MAE) and the
root mean squared error (RMSE). These metrics serve as
indicators of model accuracy and are valuable for evaluating
its performance. A lower RMSE signifies solutions that
consistently maintain proximity to the reference trajectory,
indicating a more robust navigation solution to GNSS outages
in a variety of scenarios. Such a metric has also been set
as a benchmark for positioning errors of SLAM6-based
systems [41]. Additionally, the maximum error value is
included to quantitatively measure the accumulated drift
during each GNSS outage interval. Note that in these graphs,
the cut-off is set to 200 m error, above which a beyond visual
line of sight (BVLOS) flight would be required. This shows
that even in case of long outages, employing VDM-based
navigation, regardless of the parameter identification method,
allows to not to reach BVLOS flight, potentially allowing a
safe return-to-home of the drone. On the contrary, for an INS,
the errors are at the order of kilometers, which is clearly a
BVLOS scenario.
While both the considered approaches exhibit excellent
performance as compared to the inertial coasting, it is
worth noting that for a one-minute-long GNSS outage, the
WT-based approach performs the best, capping the position
drift below 40 m for all the considered flights. That being
said, a global picture of the performance of the examined
methodologies, in terms of navigation accuracy, is presented
in Figure 16, depicting the average RMSE across the different
test flights. These results clearly show that the experimentally
inferred aerodynamic parameters consistently produce better
navigation results across different GNSS outage intervals.
On the other hand, the reported standard deviations also
indicate that, across various durations of GNSS outages,
there exists a higher variability in the navigation performance
of WMF-inferred parameters. These results are expected
because the experimental approach depends on accurate
equipment to gather aerodynamic data, while the accuracy of
the WMF methodology is constrained by the quality of the
MEMS grade IMUs on the onboard autopilot (in addition to
the existence of dynamic flight maneuvers). Further details
6Simultaneous Localisation and Mapping.
FIGURE 11. Comparison of trajectories obtained as a result of WT and
WMF based VDM-system.
regarding the limitations of both methodologies can be found
in Section. V-C
V. ADDITIONAL DISCUSSION
We throw light on some of the nuanced details that have not
been explicitly discussed so far.
A. NEED FOR A FUNCTIONAL MODEL
As highlighted in [9], the WMF method depends on the
choice of an aerodynamic model structure. In essence, the
VOLUME 12, 2024
91659

## Page 12

P. Longobardi et al.: Identifying Aerodynamics of Delta-Wing Drones for Model-Based Navigation
FIGURE 12. Evolution of horizontal positioning for 3 test flights
(a)(c)(e) and zoom (b)(d)(f) for the three approaches: WT vs WMF vs INS,.
FIGURE 13. Horizontal error for WT-VDM, WMF-VDM and inertial coasting
during 1 minute outage.
matrices, {Hm, Hf }, as defined in equations (11)-(12), are
functions of the explanatory variables detailed in Sec. II-D. In
[9], the aerodynamic model of [28] and [35] were employed
for identifying the unknown model parameters, Ci, for a
conventional and delta-wing drone respectively. Hence, the
knowledge of a model formulation is deemed essential;
furthermore, it is emphasized that this model should exhibit
FIGURE 14. Horizontal error for WT-VDM, WMF-VDM and inertial coasting
during 2 minute outage.
FIGURE 15. Horizontal error for WT-VDM, WMF-VDM and inertial coasting
during 3 minute outage.
linearity in terms of the model parameters [9]. This is indeed
an essential pre-requisite to retain the linear structure of the
system of equations (11)-(12).
Using open-air-wind-tunnel experiments (see Sec. IV-A),
we have selected an appropriate model respecting the above-
mentioned criteria. With the availability of a model, we have
employed the WMF methodology to identify the unknown
value of its parameters. During this process, we do not
need to exploit the knowledge of the numerical values
of these parameters from the wind tunnel experiments.
Henceforth, we have validated their correctness within
the VDM-EKF framework, obtaining excellent results in
autonomous navigation (see Sec. IV-C,IV-D) as compared
to inertial coasting. Therefore, this methodology validates
the applicability of an aerodynamic model in the context of
VDM-based navigation for delta-wing drones, with emphasis
on the identification of unknown values of model parameters
through the WMF method, once the appropriate model
structure is known (WT).
91660
VOLUME 12, 2024

## Page 13

P. Longobardi et al.: Identifying Aerodynamics of Delta-Wing Drones for Model-Based Navigation
FIGURE 16. Average RMS positioning error across the different test flights
for VDM-based navigation.
B. HOLISTIC COMPARISON: WMF VS WT FOR
MODEL-BASED NAVIGATION
Both the discussed approaches, WMF and WT, yield a
priori estimates of aerodynamic model parameters. When
incorporated within a model-based navigation system, these
estimations are found to be more effective than inertial
dead reckoning during GNSS outages (see Sec. IV-D).
Nevertheless, it is valuable to compare these two methods in
a holistic sense, taking into account factors such as cost, time,
and hardware requirements among others.
Characterized by simplicity, the WMF method follows a
minimalist design in terms of requirements. The algorithm
utilizes the data from GNSS, IMU, airspeed sensor, and
control commands (elevons, propeller speed) from the
autopilot, to obtain a priori parameter estimates. As these
data are readily available on almost any delta-wing drone,
employing this method is fairly simple and involves the
following three steps: i) a flight campaign, in which all the
sensor data are recorded; ii) executing the WMF offline to
obtain the unknown values of model parameters; iii) using the
obtained parameters as a priori estimates in the VDM-EKF
framework (for real-time/post-processed applications). Due
to these reasons, there is no requirement for any additional
hardware.
On the other hand, the WT method is expensive in terms
of the setup itself; the Windshaper and robotic arm itself
can cost hundreds of thousands of Euros. Additionally, the
time required to set up the facility is not insignificant; this
involves i) calibrating the motion-capture system, ii) finding a
proper zero-position of the robot, where the drone aligns with
the horizontal plane of the Windshaper; iii) manufacturing
the necessary parts to attach the drone to the load-cell and
then to the robot; iv) before manipulating the drone, all the
trajectories have to be verified at low-speeds to ensure that
there is no collision between the drone and the body of
the robot. Only after that, the drone can be allowed to be
manipulated by the robot. Nonetheless, each robot trajectory
has to be repeated two times, once in the presence of wind
TABLE 5. Summary of WT/WMF comparison over different qualitative
metrics.
and the other time without it. All these factors increase the
complexity in terms of the procedure and time required,
however, the autonomous positioning accuracy based on the
WT method is found to be better than the WMF approach.
For the tested trajectories, the former method outperforms the
latter by a factor of ∼2. We summarise these arguments in
Table 5.
C. LIMITATIONS
The WMF methodology relies heavily on the choice of
a functional aerodynamic model, which can pose chal-
lenges, as evidenced by the suboptimal performance of
the model employed for a delta-wing drone [9]. However,
leveraging an open-air WT facility allows the deduction of
a more precise functional model, subsequently enhancing
the effectiveness of the WMF methodology to identify the
unknown parameters independently. Furthermore, parameter
identification in WMF necessitates sufficient dynamical
behavior during real-flight scenarios to render unknown
parameters observable. While the previous study [9] encoun-
tered limitations due to the lack of manual control over
the drone, our utilization of a custom-made drone enabled
manual piloting and facilitated the execution of dynamic
maneuvers, thereby augmenting the observability of these
parameters. In addition to model dependency, the non-real-
time nature of WMF, requiring post-flight data processing,
is a notable constraint. However, once the identification
has been carried out, the results are applicable in real-
time settings. Besides these, reliance on measurements from
low-cost, lightweight sensors, such as Pitot tubes/pressure
sensors and IMUs, introduces inherent errors that can impact
estimation accuracy. Nonetheless, the VDM-EKF framework
refines these coarse estimates during flight [7].
For the WT methodology, addressing disparities between
experimental and real-flight conditions, notably secondary
aerodynamic effects like Reynolds number and propwash
effect [12], necessitates a two-phase calibration proce-
dure [10]. This procedure aims to adjust the numerical values
of model parameters accordingly. Nevertheless, it introduces
challenges in the tuning of the navigation filter and the
associated uncertainty regarding model parameters. Improper
tuning may lead to overfitting of real-flight data, par-
ticularly in the absence of excitation maneuvers, thereby
compromising navigation performance. That being said,
we have opted for empirical tuning of the navigation
VOLUME 12, 2024
91661

## Page 14

P. Longobardi et al.: Identifying Aerodynamics of Delta-Wing Drones for Model-Based Navigation
filter, ensuring consistent performance across various flight
dynamic conditions across different test flights. Besides
these, the WT facility has substantial cost and engineer-
ing overhead, however, the high accuracy underscores its
value.
D. SCALABILITY
On the aspect of scalability, the WMF methodology has
already been proven to be effective for different drones [9].
Our study further validates the scalability of this technique
on a custom-made delta-wing drone with a more suitable
aerodynamic model for VDM-based navigation and lower-
quality IMU. On the other hand, there have been works [11],
in which the aspects of portability of wind-tunnel-identified
parameters from one drone to another have been tested with
successful results. Nevertheless, it should be noted that, as of
now, such an approach has only been validated on two drones
sharing comparable geometry, size and weight.
VI. CONCLUSION
In conclusion, this comparative study demonstrates the
efficacy of two distinct methodologies in implementing a
model-based navigation system for a delta-wing drone. The
first approach (WT) utilizes open-air wind tunnel experimen-
tation to collect the data of interest, which are then used for
model selection and identification of unknown parameters
using step-wise regression. Meanwhile, the second approach
(WMF) utilizes flight data, logged by the autopilot, to identify
the unknown model parameters using a method based on
a partial-update Schmidt Kalman filter and observability
Gramian. Both methodologies yield a significant reduction,
of up to two orders of magnitude, in horizontal positioning
error during GNSS outages, in comparison to the traditional
kinematic navigation approach. This adds up to the studies
showing the merit of model-based navigation for small
drones by extending its applicability to delta-wing drones
or flying wing configurations. Our findings advocate for the
necessity of experimental analysis to determine the functional
model, with the acknowledgment that various approaches can
be employed for identifying numerical values of unknown
model parameters. Although experimental methods, like the
open-air wind tunnel used in this study, have the edge
in terms of general navigation performance, as manifested
by the reported error statistics across different flights for
different duration of GNSS denial, the WMF approach
offers substantial navigation improvements at virtually zero
additional cost, without requiring dedicated experimental
hardware.
ACKNOWLEDGMENT
The authors would like to express their sincere gratitude
to the Laboratory of Intelligent Systems (LIS) at EPFL
for providing access to their experimental facility and to
Dr. William Stewart in particular for helping in setting
up the experiments. Sincere thanks are also directed to
Dr. Iordan Doytchinov and Simon Reding for their help in the
experiment design and to Elie Chelly and Guillaume Bonneau
for their contribution to this study’s data collection.
REFERENCES
[1] M. Bryson and S. Sukkarieh, ‘‘UAV localization using inertial sensors and
satellite positioning systems,’’ in Handbook of Unmanned Aerial Vehicles,
K. P. Valavanis and G. J. Vachtsevanos, Eds., Dordrecht, The Netherlands:
Springer, 2015, pp. 433–460, doi: 10.1007/978-90-481-9707-1_3.
[2] P. D. Groves, Principles of GNSS, Inertial, and Multisensor Integrated
Navigation Systems. Norwood, MA, USA: Artech House, 2013.
[3] M. Khaghani and J. Skaloud, ‘‘Assessment of VDM-based autonomous
navigation of a UAV under operational conditions,’’ Robot. Auto. Syst.,
vol. 106, pp. 152–164, Aug. 2018.
[4] H. A. Mwenegoha, T. Moore, J. Pinchin, and M. Jabbal, ‘‘A model-
based tightly coupled architecture for low-cost unmanned aerial vehi-
cles for real-time applications,’’ IEEE Access, pp. 1–13, 2020, doi:
10.1109/ACCESS.2020.3038530.
[5] P. Longobardi, G. Laupré, and J. Skaloud, ‘‘Aerodynamic characterization
of a delta-wing UAV based on real flight data processing,’’ in Proc. IEEE
8th Int. Workshop Metrology Aerosp., Jun. 2021, pp. 69–74.
[6] M. Khaghani, Vehicle Dynamic Model Based Navigation for Small UAVs,
2018.
[7] G. Laupré, L. Pirlet, and J. Skaloud, ‘‘Reliable strategies for implementing
model-based navigation on fixed-wing drones,’’ J. Navigat., vol. 76,
nos. 4–5, pp. 413–431, Jul. 2023.
[8] G. Laupré and J. Skaloud, ‘‘Calibration of fixed-wing UAV aerodynamic
coefficients with photogrammetry for VDM-based navigation,’’ in Proc.
Int. Tech. Meeting Inst. Navigat., Feb. 2021, pp. 775–786.
[9] A. Sharma, G. F. Laupré, and J. Skaloud, ‘‘Identifying aerodynamics of
small fixed-wing drones using inertial measurements for model-based
navigation,’’ Navigation, J. Inst. Navigat., vol. 70, no. 4, pp. 1–23, 2023.
[10] P. Longobardi and J. Skaloud, ‘‘Aerodynamic modeling of a delta-wing
UAV for model-based navigation,’’ CEAS Aeronaut. J., vol. 15, no. 2,
pp. 283–301, Apr. 2024.
[11] P. Longobardi and J. Skaloud, ‘‘On the scalability of experimentally
determined aerodynamic model for model-based navigation on a delta-
wing UAV,’’ in Proc. IEEE 10th Int. Workshop Metrology Aerosp.,
Jun. 2023, pp. 19–24.
[12] P. Longobardi, G. Bonneau, and J. Skaloud, ‘‘Wind tunnel characterization
of a delta-wing UAV for-model-based navigation,’’ in Proc. Aerosp. Eur.
Conf. 10th EUCASS 9th CEAS Conf., 2023, pp. 1–23.
[13] M. Bryson and S. Sukkarieh, ‘‘Vehicle model aided inertial navigation for
a UAV using low-cost sensors,’’ in Proc. Australas. Conf. Robot. Automat.,
2004, pp. 1–9.
[14] P. Crocoll, J. Seibold, G. Scholz, and G. F. Trommer, ‘‘Model-aided
navigation for a quadrotor helicopter: A novel navigation system and first
experimental results,’’ Navigation, vol. 61, no. 4, pp. 253–271, Dec. 2014.
[15] P. Crocoll and G. F. Trommer, ‘‘Quadrotor inertial navigation aided
by a vehicle dynamics model with in-flight parameter estimation,’’ in
Proc. 27th Int. Tech. Meeting Satell. Division Inst. Navigat., Jan. 2014,
pp. 1784–1795.
[16] M. Koifman and I. Y. Bar-Itzhack, ‘‘Inertial navigation system aided by
aircraft dynamics,’’ IEEE Trans. Control Syst. Technol., vol. 7, no. 4,
pp. 487–493, Jul. 1999.
[17] K. Mueller, P. Crocoll, and G. F. Trommer, ‘‘Model-aided navigation
with wind estimation for robust quadrotor navigation,’’ in Proc. Int. Tech.
Meeting The Inst. Navigat., Feb. 2016, pp. 689–696.
[18] J. F. Vasconcelos, C. Silvestre, P. Oliveira, and B. Guerreiro, ‘‘Embedded
UAV model and LASER aiding techniques for inertial navigation
systems,’’ Control Eng. Pract., vol. 18, no. 3, pp. 262–278, Mar. 2010.
[19] N. Kumar, S. Saderla, and Y. Kim, ‘‘Aerodynamic characterisation of
delta wing unmanned aerial vehicle using non-gradient-based estimator,’’
Aeronaut. J., vol. 127, no. 1314, pp. 1435–1451, Aug. 2023.
[20] S. Saderla, R. Dhayalan, K. Singh, N. Kumar, and A. K. Ghosh,
‘‘Longitudinal and lateral aerodynamic characterisation of reflex wing
unmanned aerial vehicle from flight tests using maximum likelihood,
least square and neural Gauss Newton methods,’’ Aeronaut. J., vol. 123,
no. 1269, pp. 1807–1839, Nov. 2019.
[21] C. Bliamis, I. Zacharakis, P. Kaparos, and K. Yakinthos, ‘‘Aerodynamic
and stability analysis of a VTOL flying wing UAV,’’ in Proc. IOP Conf.
Ser., Mater. Sci. Eng., vol. 1024, 2021, p. 012039.
91662
VOLUME 12, 2024

## Page 15

P. Longobardi et al.: Identifying Aerodynamics of Delta-Wing Drones for Model-Based Navigation
[22] T. Dimopoulos, P. Panagiotou, and K. Yakinthos, ‘‘Stability study and
flight simulation of a blended-wing-body UAV,’’ in Proc. MATEC Web
Conf., vol. 304, 2019, p. 2013.
[23] S. Rezazadeh Movahhed and M. A. Hamed, ‘‘Calculating aerodynamic
coefficients of fixed wing aircrafts using datcom software with special
focus on rudderless flying-wing UAVs,’’ J. Aerosp. Sciece Technol., vol. 17,
pp. 60–71, Oct. 2024.
[24] G. Laupré and J. Skaloud, ‘‘On the self-calibration of aerodynamic
coefficients in vehicle dynamic model-based navigation,’’ Drones, vol. 4,
no. 3, p. 32, Jul. 2020.
[25] R. W. Beard and T. W. McLain, Small Unmanned Aircraft: Theory and
Practice. Princeton, NJ, USA: Princeton Univ. Press, 2012.
[26] K. M. Brink, ‘‘Partial-update schmidt–kalman filter,’’ J. Guid., Control,
Dyn., vol. 40, no. 9, pp. 2214–2228, 2017.
[27] C. Chen, Linear System Theory and Design. London, U.K.: Oxford Univ.
Press, 1999.
[28] G. Laupré, P. Longobardi, J. Skaloud, and J.-C. Charlaix, ‘‘Model
based navigation of delta-wing UAV-in-flight calibration and autonomous
performance,’’ Eur. J. Navigat., vol. 21, no. 1, pp. 22–30, 2021.
[29] S. Leutenegger and R. Y. Siegwart, ‘‘A low-cost and fail-safe inertial
navigation system for airplanes,’’ in Proc. IEEE Int. Conf. Robot. Autom.,
May 2012, pp. 612–618.
[30] G. Ellingson, K. Brink, and T. McLain, ‘‘Relative navigation of fixed-
wing aircraft in GPS-denied environments,’’ Navigation, vol. 67, no. 2,
pp. 255–273, Jun. 2020.
[31] H. A. Mwenegoha, T. Moore, J. Pinchin, and M. Jabbal, ‘‘Error
characteristics of a model-based integration approach for fixed-wing
unmanned aerial vehicles,’’ J. Navigat., vol. 74, no. 6, pp. 1353–1366,
Nov. 2021.
[32] H. A. Mwenegoha, T. Moore, J. Pinchin, and M. Jabbal, ‘‘Enhanced fixed
wing UAV navigation in extended GNSS outages using a vehicle dynamics
model and raw GNSS observables,’’ in Proc. 32nd Int. Tech. Meeting Satell.
Division Inst. Navigat., Oct. 2019, pp. 2552–2565.
[33] H. Mwenegoha, T. Moore, J. Pinchin, and M. Jabbal, ‘‘Model-based
autonomous navigation with moment of inertia estimation for unmanned
aerial vehicles,’’ Sensors, vol. 19, no. 11, p. 2467, May 2019.
[34] G. Laupré, M. Khaghani, and J. Skaloud, ‘‘Sensitivity to time delays in
VDM-based navigation,’’ Drones, vol. 3, no. 1, p. 11, Jan. 2019.
[35] G. J. Ducard, Nonlinear Aircraft Model. Cham, Switzerland: Springer,
2009.
[36] J.
Sola,
‘‘Quaternion
kinematics
for
the
error-state
KF,’’
2015,
arXiv:1711.02508.
[37] E. M. Coates, A. Wenz, K. Gryte, and T. A. Johansen, ‘‘Propulsion system
modeling for small fixed-wing UAVs,’’ in Proc. Int. Conf. Unmanned Aircr.
Syst. (ICUAS), Jun. 2019, pp. 748–757.
[38] V. Klein and E. Morelli, Aircraft System Identification: Theory and Prac-
tice. Chennai, India: American Institute of Aeronautics and Astronautics,
2006.
[39] F. Noca, G. Catry, N. Bosson, L. Bardazzi, S. Marquez, and A. Gros, ‘‘Wind
and weather facility for testing free-flying drones,’’ in Proc. AIAA Aviation
Forum, Jun. 2019, pp. 1–6.
[40] M. Green and J. B. Moore, ‘‘Persistence of excitation in linear systems,’’
Syst. Control Lett., vol. 7, no. 5, pp. 351–360, Sep. 1986.
[41] J. Sturm, N. Engelhard, F. Endres, W. Burgard, and D. Cremers, ‘‘A
benchmark for the evaluation of RGB-D SLAM systems,’’ in Proc.
IEEE/RSJ Int. Conf. Intell. Robots Syst., Oct. 2012, pp. 573–580.
PASQUALE LONGOBARDI received the M.S.
degree in microengineering (robotics and autono-
mous systems track), along with a minor in space
technologies from Ecole Polytechnique Fédérale
de Lausanne (EPFL), Switzerland, and the Ph.D.
degree in robotics from EPFL, in 2024. His
Ph.D. research concentrated on sensor fusion,
autonomous navigation, and the aerodynamic
characterization of UAVs for model-based naviga-
tion in GNSS-challenged environments.
AMAN SHARMA received the B.Tech degree
in electrical and electronics engineering from
the National Institute of Technology Goa, India,
in 2014, the dual master’s degree as part of
the European Union Erasmus Mundus Master
on Advanced Robotics from Ecole Centrale de
Nantes, France, and the University of Genoa,
Italy, in 2018. He is currently a Ph.D. candidate
with Ecole Polytechnique Fédérale de Lausanne
(EPFL) since 2019. He had a short industry
experience while serving as a Junior Manager with the Electrical Engineering
Department, JSW Jaigarh Port Ltd., India, from 2014 to 2016. He was a
Research Assistant with the University of Genoa, from 2018 to 2019. His
research has encompassed diverse areas, including bio-medical imaging,
autonomous vehicles, and motion cueing algorithms for virtual reality
gaming. Currently, his Ph.D. work focuses on identifying and integrating
aerodynamics with sensor measurements for model-based navigation. He is
an awardee of the prestigious European Union’s Horizon 2020 Marie Curie
fellowship.
JAN SKALOUD has been a Senior Research
Fellow and a Lecturer with Ecole Polytech-
nique Fédérale de Lausanne (EPFL), since 2008.
He holds several patents in the areas of estimation
and sensor integration, and distinctions in nav-
igation and mapping technologies from interna-
tional scientific societies and journals. He directs
research interests include satellite and inertial
navigation, sensor calibration, modern broadband
mapping, and monitoring techniques.
VOLUME 12, 2024
91663
