# Thesis.pdf

## Page 1

Geometric Disturbance Observer Based Nonlinear
Model Predictive Control and Trajectory Planning
in Safe Convex Corridors for UAVs
by
© Muhammad Adeel Ahsan
A thesis submitted to the School of Graduate Studies
in partial fulﬁlment of the requirements for the degree of
Masters of Engineering
Department of Mechanical Engineering
Memorial University of Newfoundland
May 2026
St. John’s, Newfoundland

## Page 2

Abstract
This thesis develops and validates an integrated framework for UAV autonomy in
complex environments, spanning disturbance-resilient control, trajectory planning in
obstacle-dense environments, and a hardware-in-the-loop (HITL) simulation platform
for validating planning and control algorithms.
The thesis consists of three main components.
First, a geometric disturbance
observer-based nonlinear model predictive control (NMPC) architecture is presented
for quadrotor trajectory tracking. The framework couples an extended-state extended
Kalman ﬁlter formulated on the SO(3) manifold with a disturbance-aware NMPC that
embeds six-degree-of-freedom disturbance estimates as time-varying inputs within the
prediction model, enabling proactive compensation within the receding-horizon opti-
mization. Second, a time-eﬃcient trajectory planning framework for ﬁxed-wing UAVs
combines greedy corridor generation along bidirectional rapidly-exploring random tree
path with diﬀerential-ﬂatness-based convex optimization. The approach constructs a
safe corridor of overlapping convex regions signiﬁcantly faster than workspace-wide
convex decomposition methods and formulates the complete planning problem as a
single convex quadratic program, guaranteeing collision-free and dynamically feasible
solutions without nonlinear reﬁnement. Third, a comprehensive hardware-in-the-loop
ii

## Page 3

testing framework is developed for the DJI M300 RTK platform, integrating the DJI
Manifold 2-G onboard computer with the ﬂight controller through the DJI Onboard
SDK and Robot Operating System.
Simulation results demonstrate that the geometric disturbance observer-based
NMPC achieves 60% reduction in position root mean square error compared to
baseline NMPC under periodic six-degree-of-freedom disturbances.
The proposed
trajectory planning framework achieves a 36% reduction in traversal time with a
17Ö computational speedup relative to the Graph of Convex Sets (GCS) planner
reﬁned with Kinodynamic Trajectory Optimization (KTO) as the baseline method,
and demonstrating a 99.4% success rate across 1,001 randomized scenarios.
The
hardware-in-the-loop simulation framework for the DJI M300 RTK drone success-
fully validates the implementations of proportional–integral–derivative (PID), linear
quadratic regulator (LQR), and model predictive control (MPC) algorithms.
To-
gether, these contributions form a complete pipeline for robust UAV control and
planning: from disturbance-resilient NMPC and convex optimization-based trajec-
tory planning to pre-ﬂight validation on real hardware, providing a foundation for
safer autonomous UAV operations in uncertain and obstacle-dense environments.
iii

## Page 4

Acknowledgements
First and foremost, I am deeply grateful to Allah, the Most Gracious and Most
Merciful, for His countless blessings, guidance, and strength throughout this academic
journey. Without His divine support and wisdom, this work would not have been
possible.
I owe my deepest gratitude to my family, especially my parents, whose unwavering
love and prayers have been the foundation of all my achievements. In particular, I
thank my mother, whose selﬂess dedication, endless encouragement, and countless
sacriﬁces have shaped who I am; words cannot express the depth of my appreciation.
I would also like to express my sincere and heartfelt gratitude to my supervisors,
especially Dr. Oscar De Silva and Dr. George Mann, for their exceptional guidance,
constant support, and invaluable mentorship throughout this research.
I extend my gratitude to all my friends, colleagues, and faculty members at Memo-
rial University who have contributed to my academic journey through their support
and discussions. Finally, I gratefully acknowledge that part of this work was sup-
ported by the National Research Council of Canada and the Natural Sciences and
Engineering Research Council of Canada.
iv

## Page 5

Co-authorship Statement
I, Muhammad Adeel Ahsan, hold a principal author status for all the manuscript
chapters (Chapters 3–5) in this thesis. However, each manuscript is co-authored by
my supervisors, whose contributions have facilitated the development of this work as
described below.
 Paper 1 in Chapter 3: Muhammad Adeel Ahsan, Oscar De Silva, George K.
I. Mann, Raymond G. Gosine, and Awantha Jayasiri, “Geometric Disturbance
Observer Based Nonlinear Model Predictive Control of a Quadrotor,” ASME
Letters in Dynamic Systems and Control, vol. 6, no. 1, 011010, Jan. 2026. I
was the primary author responsible for preparing the manuscript, conducting
all simulations, and obtaining the results. Authors 2–4 worked in a supervisory
capacity, contributing to methodology development, and reﬁnement of the pre-
sentation. Author 5 was an industry collaborator from the National Research
Council of Canada who met at a regular frequency to discuss the work and
provided valuable feedback on the practical aspects of this paper.
 Paper 2 in Chapter 4: Time-Eﬃcient Trajectory Planning for UAVs in Safe
Convex Corridors using Diﬀerential Flatness Constrained Convex Optimization.
I was the primary author responsible for preparing the manuscript, conducting
v

## Page 6

all simulations, and obtaining the results. My MEng supervisors serve as co-
authors who worked in a supervisory capacity, contributing to methodology
development, and reﬁnement of the presentation. This work has been submitted
to IEEE Access.
 Paper 3 in Chapter 5: Hardware-in-the-Loop Implementation and Validation
of Trajectory Control Algorithms for DJI M300 RTK using DJI OSDK and ROS.
I was the primary author responsible for preparing the manuscript, conducting
all simulations and hardware implementations, and obtaining the results. My
MEng supervisors serve as co-authors who worked in a supervisory capacity,
contributing to methodology development, and reﬁnement of the presentation.
This work is to be submitted to ASME Letters in Dynamic Systems and Control.
Muhammad Adeel Ahsan
Date:
vi

## Page 7

List of Abbreviations
UAV
Unmanned Aerial Vehicle
PID
Proportional-Integral-Derivative
NMPC
Nonlinear Model Predictive Control
ADRC
Active Disturbance Rejection Control
MPC
Model Predictive Control
DO
Disturbance Observer
DOF
Degrees of Freedom
6-DOF
Six Degrees of Freedom
SO(3)
Special Orthogonal Group (3D rotation matrices)
A*
A-Star Algorithm
PRM
Probabilistic Roadmap
RRT
Rapidly-exploring Random Tree
RRT*
Rapidly-exploring Random Tree Star
GCS
Graph of Convex Sets
IRIS
Iterative Regional Inﬂation by Semideﬁnite programming
vii

## Page 8

MICP
Mixed-Integer Convex Program
SITL
Software-in-the-Loop
HITL
Hardware-in-the-Loop
OSDK
Onboard Software Development Kit
ROS
Robot Operating System
ES-EKF
Extended-State Extended Kalman Filter
KTO
Kinodynamic Trajectory Optimization
RTK
Real-Time Kinematic
LQR
Linear Quadratic Regulator
RMSE
Root Mean Square Error
SMC
Sliding-Mode Control
ESO
Extended State Observer
UKF
Unscented Kalman Filter
3-DOF
Three Degrees of Freedom
IMU
Inertial Measurement Unit
EKF
Extended Kalman Filter
SLAM
Simultaneous Localization and Mapping
LVIO
Lidar-Visual-Inertial Odometry
PD
Proportional-Derivative
GeoJSON
Geographic JavaScript Object Notation
viii

## Page 9

NLP
Nonlinear Program
CHOMP
Covariant Hamiltonian Optimization for Motion Planning
STOMP
Stochastic Trajectory Optimization for Motion Planning
JSON
JavaScript Object Notation
IP
Ingress Protection (rating)
API
Application Programming Interface
CPU
Central Processing Unit
RAM
Random Access Memory
SSD
Solid State Drive
USB
Universal Serial Bus
ENU
East-North-Up (coordinate frame)
NED
North-East-Down (coordinate frame)
ix

## Page 10

Contents
List of Abbreviations
vii
List of Tables
xv
List of Figures
xvi
1
Introduction
1
1.1
Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1
1.2
Thesis Statement . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5
1.3
Objectives and Expected Contributions . . . . . . . . . . . . . . . . .
5
1.3.1
Geometric Disturbance-Observer-Based NMPC for Quadrotors
6
1.3.2
Diﬀerential-Flatness-Based Convex Trajectory Optimization
.
6
1.3.3
Hardware-in-the-Loop Implementation and Validation . . . . .
7
1.4
Organization of the Thesis . . . . . . . . . . . . . . . . . . . . . . . .
8
1.5
Bibliography . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9
2
Literature Review
15
2.1
Classical to Optimal Control Approaches . . . . . . . . . . . . . . . .
15
2.1.1
Learning-Based NMPC . . . . . . . . . . . . . . . . . . . . . .
18
x

## Page 11

2.2
Disturbance Observer-Based Control
. . . . . . . . . . . . . . . . . .
18
2.2.1
Deterministic Disturbance Observers . . . . . . . . . . . . . .
19
2.2.2
Integration with Model Predictive Control . . . . . . . . . . .
20
2.2.3
Stochastic Disturbance Observers . . . . . . . . . . . . . . . .
21
2.2.4
Geometric State Estimation and Control . . . . . . . . . . . .
22
2.3
Path Planning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
23
2.4
Trajectory Optimization . . . . . . . . . . . . . . . . . . . . . . . . .
25
2.5
Trajectory Optimization within Safe Corridors . . . . . . . . . . . . .
28
2.6
Hardware-in-the-Loop Testing and Validation
. . . . . . . . . . . . .
29
2.7
Bibliography . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
31
3
Geometric Disturbance Observer Based Nonlinear Model Predictive
Control of a Quadrotor
39
3.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
40
3.2
Methodology
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
43
3.2.1
Mathematical Model . . . . . . . . . . . . . . . . . . . . . . .
45
3.2.2
Reference Trajectory Generation
. . . . . . . . . . . . . . . .
46
3.2.2.1
Stage 1: Diﬀerential Flatness-Based Planning . . . .
46
3.2.2.2
Stage 2: NMPC-Based Trajectory Smoothing . . . .
48
3.2.3
Nonlinear Model Predictive Control . . . . . . . . . . . . . . .
48
3.2.4
Geometric Extended State Extended Kalman Filter . . . . . .
50
3.2.4.1
Sensor Inputs and Observer Structure
. . . . . . . .
50
3.2.4.2
Linear State Error Dynamics on Lie Groups . . . . .
51
3.2.4.3
Observer Propagation and Update
. . . . . . . . . .
53
xi

## Page 12

3.3
Results and Discussion . . . . . . . . . . . . . . . . . . . . . . . . . .
55
3.4
Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
62
3.5
Bibliography . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
63
4
Time-Eﬃcient Trajectory Planning for UAVs in Safe Convex Corri-
dors using Diﬀerential Flatness Constrained Convex Optimization
67
4.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
69
4.2
Related Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
73
4.3
Safe Connected Convex Corridor Generation . . . . . . . . . . . . . .
77
4.3.1
Geographic Data Processing and Obstacle Decomposition . . .
78
4.3.2
Collision-Free Path Generation via Bidirectional RRT . . . . .
79
4.3.3
Seed Point Selection
. . . . . . . . . . . . . . . . . . . . . . .
82
4.3.4
Separating Hyperplane Construction
. . . . . . . . . . . . . .
83
4.3.5
Convex Region Formation . . . . . . . . . . . . . . . . . . . .
84
4.4
Convexiﬁcation of Nonconvex Dynamical Constraints . . . . . . . . .
85
4.4.1
Diﬀerential Flatness
. . . . . . . . . . . . . . . . . . . . . . .
86
4.4.2
Derivatives of Flat Outputs
. . . . . . . . . . . . . . . . . . .
87
4.4.3
Phase Space Generation and Boundary Approximation . . . .
87
4.5
Trajectory Optimization . . . . . . . . . . . . . . . . . . . . . . . . .
89
4.5.1
B´ezier Control Point Parameterization
. . . . . . . . . . . . .
90
4.5.2
Initial Time Allocation . . . . . . . . . . . . . . . . . . . . . .
90
4.5.3
Corridor Containment
. . . . . . . . . . . . . . . . . . . . . .
91
4.5.4
Boundary Conditions . . . . . . . . . . . . . . . . . . . . . . .
91
4.5.5
Derivative Relations
. . . . . . . . . . . . . . . . . . . . . . .
91
xii

## Page 13

4.5.6
Inter-Segment Continuity
. . . . . . . . . . . . . . . . . . . .
92
4.5.7
Dynamic Feasibility Constraints . . . . . . . . . . . . . . . . .
93
4.5.8
Objective Function . . . . . . . . . . . . . . . . . . . . . . . .
93
4.5.9
Trajectory Reconstruction . . . . . . . . . . . . . . . . . . . .
94
4.6
Results and Discussion . . . . . . . . . . . . . . . . . . . . . . . . . .
94
4.6.1
Comparison with GCS + KTO Baseline
. . . . . . . . . . . .
94
4.6.2
Web App Based Trajectory Planning Simulator
. . . . . . . .
100
4.6.3
Monte Carlo Simulations . . . . . . . . . . . . . . . . . . . . .
104
4.7
Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
107
4.8
Bibliography . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
108
5
Hardware-in-the-Loop Implementation and Validation of Trajectory
Control Algorithms for DJI M300 RTK using DJI OSDK and ROS113
5.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
114
5.2
System Architecture
. . . . . . . . . . . . . . . . . . . . . . . . . . .
116
5.2.1
DJI M300 RTK Hardware Platform . . . . . . . . . . . . . . .
117
5.2.2
DJI Onboard SDK Integration . . . . . . . . . . . . . . . . . .
118
5.2.3
Onboard Computing Platform . . . . . . . . . . . . . . . . . .
119
5.2.4
ROS Framework and Communication . . . . . . . . . . . . . .
119
5.2.5
HITL Testing Environment
. . . . . . . . . . . . . . . . . . .
120
5.3
Methodology
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
121
5.3.1
System Dynamics Model . . . . . . . . . . . . . . . . . . . . .
121
5.3.2
Common Control Framework
. . . . . . . . . . . . . . . . . .
123
5.3.3
Controller Formulations
. . . . . . . . . . . . . . . . . . . . .
125
xiii

## Page 14

5.3.3.1
PID Controller . . . . . . . . . . . . . . . . . . . . .
125
5.3.3.2
Linear Quadratic Regulator (LQR) . . . . . . . . . .
125
5.3.3.3
Model Predictive Control (MPC) . . . . . . . . . . .
126
5.4
Results and Discussion . . . . . . . . . . . . . . . . . . . . . . . . . .
128
5.4.1
Experimental Setup . . . . . . . . . . . . . . . . . . . . . . . .
128
5.4.2
Circular Trajectory Performance . . . . . . . . . . . . . . . . .
130
5.4.3
Figure-8 Trajectory Performance
. . . . . . . . . . . . . . . .
130
5.4.4
Disturbance Analysis . . . . . . . . . . . . . . . . . . . . . . .
136
5.5
Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
138
5.6
Bibliography . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
139
6
Conclusion and Future Work
142
6.1
Summary of Contributions . . . . . . . . . . . . . . . . . . . . . . . .
142
6.1.1
Geometric Disturbance Observer-Based NMPC
. . . . . . . .
142
6.1.2
Time-Eﬃcient Trajectory Planning in Safe Convex Corridors .
143
6.1.3
Hardware-in-the-Loop Validation Framework . . . . . . . . . .
144
6.2
Publications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
144
6.3
Future Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
145
6.3.1
Extensions to Disturbance-Aware Predictive Control
. . . . .
145
6.3.2
Extensions to Convex Trajectory Planning Methods . . . . . .
146
6.3.3
Expansion of HITL Testing Capabilities
. . . . . . . . . . . .
146
xiv

## Page 15

List of Tables
3.1
Simulation Parameters. . . . . . . . . . . . . . . . . . . . . . . . . . .
56
3.2
Sinusoidal Disturbance Parameters. . . . . . . . . . . . . . . . . . . .
56
4.1
Parameter Ranges for Phase Space Generation . . . . . . . . . . . . .
89
4.2
Stage-wise timing comparison for proposed and baseline frameworks.
96
4.3
Path length and traversal time comparison. . . . . . . . . . . . . . . .
97
4.4
Online web simulator results summary. . . . . . . . . . . . . . . . . .
103
5.1
RMSE Performance Comparison.
. . . . . . . . . . . . . . . . . . . .
136
xv

## Page 16

List of Figures
2.1
Quadrotor coordinate system (plus-conﬁguration). . . . . . . . . . . .
16
3.1
ES-EKF Based NMPC Architecture.
. . . . . . . . . . . . . . . . . .
44
3.2
Original and Smoothed Trajectory.
. . . . . . . . . . . . . . . . . . .
57
3.3
Trajectory Tracking with and without ES-EKF. . . . . . . . . . . . .
59
3.4
True Disturbances vs. ES-EKF Estimation.
. . . . . . . . . . . . . .
60
3.5
Lissajous Trajectory Tracking Comparison. . . . . . . . . . . . . . . .
60
3.6
RMSE comparison with & without ES-EKF. . . . . . . . . . . . . . .
61
4.1
Proposed Trajectory Planning Pipeline. . . . . . . . . . . . . . . . . .
73
4.2
Mission Planning . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
78
4.3
Convex Decomposition . . . . . . . . . . . . . . . . . . . . . . . . . .
79
4.4
Convexiﬁcation of nonconvex obstacles mapped by the user. “Org”
denotes the original obstacle vector map, and “Conv” denotes the con-
vexiﬁed obstacle vector map. . . . . . . . . . . . . . . . . . . . . . . .
80
4.5
Bidirectional RRT Generated Path. . . . . . . . . . . . . . . . . . . .
82
4.6
Path Planning and Safe Connected Corridors. . . . . . . . . . . . . .
85
4.7
Phase Spaces and Convex Hulls. . . . . . . . . . . . . . . . . . . . . .
88
xvi

## Page 17

4.8
Comparison of proposed and baseline pipeline planning results. . . . .
95
4.9
Kinematics proﬁles for all three maps. Left column: proposed method;
right column: GCS+KTO baseline. . . . . . . . . . . . . . . . . . . .
96
4.10 B´ezier derivative control points - Proposed approach. . . . . . . . . .
99
4.11 Comparison of diﬀerent sampling methods for connected safe-corridor
generation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
100
4.12 Web Based Trajectory Planning Simulator . . . . . . . . . . . . . . .
101
4.13 Proposed pipeline results using online web app simulator on various
maps.
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
101
4.14 Map for MonteCarlo simulations with obstacles. . . . . . . . . . . . .
104
4.15 Stage time distributions for Monte Carlo simulations. . . . . . . . . .
105
4.16 Optimized paths by outcome (success vs.
failure) for Monte Carlo
simulations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
106
4.17 Traversal time and path length histograms for Monte Carlo simulations.107
5.1
Overall HITL Architecture.
. . . . . . . . . . . . . . . . . . . . . . .
117
5.2
HITL setup showing the connections between the DJI M300 RTK
drone, DJI Manifold 2-G onboard computer, OSDK Expansion Mod-
ule, and Windows laptop.
. . . . . . . . . . . . . . . . . . . . . . . .
121
5.3
Hardware-in-the-loop (HITL) setup. Left: Windows laptop running
the DJI Assistant 2 simulator. Right: monitor connected to the DJI
Manifold 2-G with ROS nodes running. . . . . . . . . . . . . . . . . .
122
5.4
Circular trajectory 3D Tracking and individual position responses. . .
131
5.5
Circular trajectory velocity responses. . . . . . . . . . . . . . . . . . .
131
xvii

## Page 18

5.6
Circular trajectory acceleration commands. . . . . . . . . . . . . . . .
132
5.7
Circular trajectory attitude angles.
. . . . . . . . . . . . . . . . . . .
132
5.8
Figure 8 trajectory 3D Tracking and individual position responses. . .
133
5.9
Figure-8 trajectory velocity tracking. . . . . . . . . . . . . . . . . . .
133
5.10 Figure-8 trajectory acceleration commands. . . . . . . . . . . . . . . .
134
5.11 Figure-8 trajectory attitude angles. . . . . . . . . . . . . . . . . . . .
134
5.12 DJI Smart Controller traces rendered during HITL execution.
. . . .
135
5.13 Setting wind disturbances in DJI Assistant 2 simulator. . . . . . . . .
136
5.14 Drone tilted to compensate for the added wind disturbance.
. . . . .
137
5.15 Tracking performance comparison under wind disturbances. . . . . . .
138
xviii

## Page 19

Chapter 1
Introduction
1.1
Motivation
Unmanned aerial vehicles (UAVs) are being deployed in an expanding range of appli-
cations, from package delivery and infrastructure inspection to surveillance, search-
and-rescue, and agriculture [1]. The successful application of UAVs in these domains
depends on overcoming several fundamental challenges.
Flight control algorithms
must handle external disturbances such as wind gusts, payload shifts, and aerody-
namic uncertainties, while also addressing the inherently nonlinear, underactuated
dynamics of UAVs. Simultaneously, trajectory planning algorithms must eﬃciently
navigate cluttered, obstacle-dense environments while satisfying the UAV’s dynamic
constraints and real-time computational limits. Finally, bridging the gap from theory
to practice demands validation on hardware platforms, ensuring that the control and
planning algorithms perform reliably on physical UAV hardware which incorporates
practical constraints including sensor noise, actuator limits, communication latencies,
1

## Page 20

and computational overhead.
The control of UAVs, particularly quadrotors, presents signiﬁcant challenges due
to their inherent underactuation, nonlinear dynamics, and susceptibility to exter-
nal disturbances such as wind gusts, payload variations, and aerodynamic eﬀects
[2, 3]. While classical control approaches such as Proportional-Integral-Derivative
(PID) control remain widely used due to their simplicity, they are fundamentally
limited in handling nonlinear dynamics and system constraints [4]. Advanced control
strategies including adaptive control [5] and sliding-mode control [6] improve robust-
ness but lack the ability to explicitly handle state and input constraints that are
critical for safe operation. Nonlinear Model Predictive Control (NMPC) addresses
these limitations by solving constrained optimal control problem at each sampling
instant while accounting for system nonlinearities [7]. However, the performance of
NMPC critically depends on model accuracy, and unmodeled disturbances can lead
to signiﬁcant tracking errors and potential instability.
To address model uncertainties and external disturbances, disturbance observer-
based control has emerged as a promising approach. Active Disturbance Rejection
Control (ADRC) employs extended state observers to estimate and compensate for
disturbances in real-time [8]. Recent work has integrated disturbance observers with
MPC for quadrotor control [9, 10, 11]. However, existing approaches suﬀer from fun-
damental limitations: they typically estimate only translational forces while ignoring
disturbance torques, rely on singularity-prone Euler angle representations, and cru-
cially, do not embed disturbance estimates directly into the MPC prediction model.
Instead, disturbance compensation is applied as feedforward terms after optimization,
preventing the controller from proactively anticipating disturbance eﬀects within the
2

## Page 21

receding-horizon framework. Furthermore, deterministic observers become unreliable
during aggressive maneuvers where nonlinear dynamics dominate. For quadrotors
whose orientation evolves on the SO(3) manifold, geometric observers oﬀer computa-
tional eﬃciency with singularity-free representation [12, 13]. Despite these individual
advances, no existing framework combines geometric state and six-degree-of-freedom
(DOF) disturbance estimation with disturbance-aware predictive control that embeds
disturbance estimates as time-varying inputs within the NMPC prediction model.
Beyond robust control, autonomous UAV operation requires eﬃcient trajectory
planning capabilities that simultaneously ensure collision avoidance, satisfy dynamic
feasibility constraints, and remain computationally tractable for real-time execu-
tion. Traditional path planning methods such as graph-search algorithms [14, 15]
and sampling-based planners [16, 17, 18] focus primarily on geometric collision avoid-
ance without explicitly considering dynamic feasibility, necessitating substantial post-
processing. Trajectory optimization methods [19, 20] directly formulate planning as
optimal control problems but result in nonconvex programs that are computationally
intensive and sensitive to initialization [21]. Recent advances in convex decomposi-
tion, particularly the Graph of Convex Sets (GCS) framework [22], decompose free
space into overlapping convex regions using Iterative Regional Inﬂation by Semidef-
inite programming (IRIS) [23] and formulate trajectory planning as mixed-integer
convex programs (MICP). While GCS can handle complex obstacle environments,
constructing global convex decompositions of large workspaces is computationally
expensive, and MICP solve times grow rapidly with the number of regions [24], lim-
iting real-time replanning capabilities. Moreover, most approaches separate obstacle
avoidance from dynamic constraint enforcement, requiring subsequent nonlinear re-
3

## Page 22

ﬁnement stages that compromise either computational eﬃciency or solution quality
[25].
Diﬀerential ﬂatness theory provides an elegant framework for trajectory param-
eterization in underactuated systems [26]. For diﬀerentially ﬂat systems, all states
and control inputs can be expressed as algebraic functions of ﬂat outputs and their
derivatives, enabling polynomial trajectory parameterization that signiﬁcantly sim-
pliﬁes optimization. This approach has proved successful for quadrotor applications,
such as minimum snap trajectory generation [27]. However, applications to ﬁxed-wing
UAVs remain limited, and existing ﬂatness-based methods either assume obstacle-free
environments or rely on precomputed safe corridors without addressing eﬃcient cor-
ridor generation. The fundamental challenge is to develop a uniﬁed framework that
combines time-eﬃcient corridor construction with convex trajectory optimization that
simultaneously enforces obstacle avoidance, dynamic feasibility, and higher-order con-
tinuity constraints without requiring subsequent nonconvex reﬁnement.
Finally, bridging the gap between theoretical control and planning algorithms
and practical deployment on commercial UAV platforms remains a critical chal-
lenge. While Software-in-the-Loop (SITL) simulations are useful during initial de-
velopment, they do not accurately represent hardware-speciﬁc constraints such as
computational limitations, communication latencies, and actual ﬂight controller in-
terfaces. Hardware-in-the-Loop (HITL) testing addresses these limitations by exe-
cuting actual ﬂight software on real embedded hardware while maintaining the safety
and repeatability of simulated environments [28]. However, despite extensive litera-
ture on UAV control, there remains limited documentation of complete and validated
HITL workﬂows for commercial DJI platforms that execute real onboard software
4

## Page 23

through standardized interfaces such as the DJI Onboard SDK (OSDK) using the
Robot Operating System (ROS). A comprehensive HITL framework that enables
systematic validation of control algorithms on commercial platforms prior to outdoor
ﬂight testing is essential for accelerating the transition from simulation to practical
deployment.
1.2
Thesis Statement
This thesis develops and validates an integrated framework for robust control un-
der disturbances and eﬃcient trajectory planning for unmanned aerial vehicles in
complex environments. It addresses three challenges: (1) robust trajectory-tracking
control under external disturbances using geometric disturbance-observer-based non-
linear model predictive control; (2) time-eﬃcient trajectory planning in obstacle-dense
environments using diﬀerential-ﬂatness-based convex optimization within safe convex
corridors; and (3) implementation and evaluation of trajectory-tracking controllers in
a hardware-in-the-loop simulation setup.
1.3
Objectives and Expected Contributions
The speciﬁc research objectives and expected contributions are organized according
to the three main technical challenges addressed in this work:
5

## Page 24

1.3.1
Geometric Disturbance-Observer-Based NMPC for Quadro-
tors
Objective: Develop a disturbance-aware nonlinear model predictive control frame-
work that integrates geometric state estimation with six-DOF disturbance estimation
and embeds disturbance estimates directly into the receding-horizon optimization for
proactive compensation.
Expected Contributions:
 A novel extended-state extended Kalman ﬁlter (ES-EKF) formulated on the
SO(3) manifold that provides singularity-free real-time estimates of all states
along with six-DOF disturbance forces and torques for quadrotors.
 A disturbance-aware NMPC formulation that treats disturbance estimates as
known, time-varying inputs within the prediction model, enabling proactive
compensation within the receding-horizon optimization rather than feedforward
correction after optimization.
 A uniﬁed framework combining diﬀerential-ﬂatness-based trajectory generation
with disturbance-aware NMPC that integrates feedforward and feedback control
for improved tracking performance under external perturbations.
1.3.2
Diﬀerential-Flatness-Based Convex Trajectory Optimiza-
tion
Objective: Develop a time-eﬃcient trajectory planning framework that combines
rapid corridor generation with convex trajectory optimization, exploiting diﬀerential
6

## Page 25

ﬂatness to simultaneously enforce obstacle avoidance, dynamic feasibility, and higher-
order continuity constraints within a single convex program.
Expected Contributions:
 A greedy corridor generation algorithm that constructs a connected sequence
of overlapping convex regions along a bidirectional RRT path, achieving signif-
icantly faster computation than workspace-wide IRIS-based convex decomposi-
tion [23] while ensuring complete start-to-goal connectivity.
 A convex trajectory optimization formulation for ﬁxed-wing UAVs that exploits
diﬀerential ﬂatness of the dynamical model [21] and also uniﬁes corridor con-
tainment and higher-order dynamic constraints within a single convex program,
eliminating the need for nonconvex reﬁnement stages.
 Comprehensive validation including comparative experiments against GCS+KTO
baseline, web-based simulator with real map integration, and Monte Carlo anal-
ysis demonstrating high success rates and computational eﬃciency.
1.3.3
Hardware-in-the-Loop Implementation and Validation
Objective: Develop and validate a HITL framework for DJI M300 RTK drone us-
ing DJI OSDK and ROS that enables systematic testing of planning and control
algorithms on real hardware within simulated environments using DJI Assistant 2
simulator prior to outdoor ﬂight testing.
Expected Contributions:
 A complete HITL framework integrating the DJI M300 RTK platform with DJI
7

## Page 26

Manifold 2-G onboard computer, DJI OSDK, and ROS Kinetic, enabling real-
time execution of position control algorithms on actual ﬂight hardware within
the DJI Assistant 2 simulator environment.
 Implementation and comparative evaluation of PID, LQR, and MPC in the HIL
setup using the DJI OSDK and the DJI Assistant 2 Simulator.
1.4
Organization of the Thesis
This thesis follows a manuscript format and is divided into six chapters. A brief
summary of the contents of each chapter is provided below:
Chapter 1 presents the motivation, thesis statement, research objectives, ex-
pected contributions, and structure of the thesis.
Chapter 2 provides a comprehensive review of the state-of-the-art in UAV con-
trol and trajectory planning. The chapter covers nonlinear model predictive control
approaches, diﬀerent disturbance observers and their integration with MPC, path
planning and trajectory optimization methods, convex decomposition strategies for
obstacle avoidance, and the limitations in available HITL architectures for commercial
DJI drones.
Chapter 3 presents the research work published in [29]. This chapter details the
ﬁrst major contribution: a geometric disturbance observer-based NMPC architecture
that couples an SO(3)-formulated ES-EKF with a disturbance-aware predictive con-
troller. It describes the continuous-time augmented model with explicit force and
torque disturbance states, the geometric ES-EKF that provides real-time six-DOF
disturbance estimates, the NMPC formulation that injects these estimates at each
8

## Page 27

sampling instant for proactive compensation, and the trajectory-tracking evaluations
under periodic six-DOF perturbations across multiple ﬂight conditions, compared to
a baseline NMPC without disturbance feedback.
Chapter 4 presents the second major contribution: a convex optimization-based
trajectory planning framework for ﬁxed-wing UAVs. The chapter describes the greedy
corridor generation algorithm along bidirectional RRT path, the convexiﬁcation of
dynamic constraints through diﬀerential ﬂatness and phase-space sampling of ﬂat
outputs and their derivatives, the uniﬁed B´ezier control-point-based convex optimiza-
tion formulation, comparison with the GCS+KTO baseline framework, a web-based
trajectory planning simulator, and Monte Carlo simulation results for the proposed
trajectory planning framework.
Chapter 5 presents the third contribution: a comprehensive HITL framework for
famous commercial and industrial drone DJI M300 RTK. The chapter describes the
system architecture integrating DJI M300 RTK, Manifold 2-G, OSDK, and ROS, the
implementation of PID, LQR, and MPC controllers, and a comparison on circular
and ﬁgure-8 trajectories within the DJI Assistant 2 simulator.
Chapter 6 concludes the thesis by summarizing the key contributions, result-
ing publications, discussing limitations of the proposed approaches, and outlining
directions for future research.
1.5
Bibliography
[1] Aggarwal, S., and Kumar, N., 2020, “Path planning techniques for unmanned
aerial vehicles: A review, solutions, and challenges,” Comput. Commun., 149,
9

## Page 28

pp. 270–299. doi:10.1016/j.comcom.2019.10.014.
[2] Mahony, R., Kumar, V., and Corke, P., 2012, “Multirotor aerial vehicles: Mod-
eling, estimation, and control of a quadrotor,” IEEE Robot. Autom. Mag., 19(3),
pp. 20–32. doi:10.1109/MRA.2012.2206474.
[3] Bouabdallah, S., Noth, A., and Siegwart, R., 2004, “PID vs LQ control
techniques applied to an indoor micro quadrotor,” Proc. IEEE/RSJ Int.
Conf. Intelligent Robots and Systems (IROS), Sendai, Japan, pp. 2451–2456.
doi:10.1109/IROS.2004.1389776.
[4] Ahsan, M. A., Khan, H. Z. I., Rajput, J., and Riaz, J., 2022, “Active disturbance
rejection control of a quadrotor: A comparative study,” Proc. 19th Int. Bhur-
ban Conf. Applied Sciences and Technology (IBCAST), Islamabad, Pakistan,
pp. 444–450. doi:10.1109/IBCAST54850.2022.9990161.
[5] Dydek, Z. T., Annaswamy, A. M., and Lavretsky, E., 2013, “Adaptive control of
quadrotor UAVs: A design trade study with ﬂight evaluations,” IEEE Trans.
Control Syst. Technol., 21(4), pp. 1400–1406. doi:10.1109/TCST.2012.2200104.
[6] Xu, R., and ¨Ozguner, U., 2006, “Sliding mode control of a quadrotor helicopter,”
Proc. 45th IEEE Conf. Decision and Control (CDC), San Diego, CA, USA,
pp. 4957–4962. doi:10.1109/CDC.2006.377588.
[7] Gomaa, M. A. K., De Silva, O., Mann, G. K. I., and Gosine, R. G., 2023, “Compu-
tationally eﬃcient stability-based nonlinear model predictive control design for
quadrotor aerial vehicles,” IEEE Trans. Control Syst. Technol., 31(2), pp. 615–
630. doi:10.1109/TCST.2022.3188399.
10

## Page 29

[8] Han, J., 2009, “From PID to active disturbance rejection control,” IEEE Trans.
Ind. Electron., 56(3), pp. 900–906. doi:10.1109/TIE.2008.2011621.
[9] Xu, L., Tian, B., Wang, C., Lu, J., Wang, D., Li, Z., and Zong, Q., 2024,
“Fixed-time disturbance observer–based MPC robust trajectory tracking con-
trol of quadrotor,” IEEE/ASME Trans. Mechatron., Early Access, pp. 1–11.
doi:10.1109/TMECH.2024.3503062.
[10] Derakhshan, R. E., Danesh, M., and Moosavi, H., 2024, “Disturbance observer–
based model predictive control of a coaxial octorotor with variable centre of
gravity,” IET Control Theory Appl., 18(6), pp. 764–783. doi:10.1049/cth2.12611.
[11] Chen, C., Zhang, X., and Peng, X., 2024, “Trajectory tracking control of four-
rotor UAV based on nonlinear extended state observer and model predictive con-
trol in wind disturbance environment,” J. Phys.: Conf. Ser., 2764(1), p. 012075.
doi:10.1088/1742-6596/2764/1/012075.
[12] He, D., Xu, W., and Zhang, F., 2021, “Kalman ﬁlters on diﬀerentiable mani-
folds,” arXiv:2102.03804.
[13] Barrau, A., and Bonnabel, S., 2017, “The invariant extended Kalman ﬁlter
as a stable observer,” IEEE Trans. Autom. Control, 62(4), pp. 1797–1812.
doi:10.1109/TAC.2016.2594085.
[14] Dijkstra, E. W., 1959, “A note on two problems in connexion with graphs,”
Numer. Math., 1(1), pp. 269–271. doi:10.1007/BF01386390.
11

## Page 30

[15] Hart, P. E., Nilsson, N. J., and Raphael, B., 1968, “A formal basis for the heuristic
determination of minimum cost paths,” IEEE Trans. Syst. Sci. Cybern., 4(2),
pp. 100–107. doi:10.1109/TSSC.1968.300136.
[16] Kavraki, L. E., Svestka, P., Latombe, J.-C., and Overmars, M. H., 1996, “Prob-
abilistic roadmaps for path planning in high-dimensional conﬁguration spaces,”
IEEE Trans. Robot. Autom., 12(4), pp. 566–580. doi:10.1109/70.508439.
[17] LaValle, S. M., and Kuﬀner, J. J., 2001, “Randomized kinodynamic planning,”
Int. J. Robot. Res., 20(5), pp. 378–400. doi:10.1177/02783640122067453.
[18] Karaman,
S.,
and
Frazzoli,
E.,
2011,
“Sampling-based
algorithms
for
optimal
motion
planning,”
Int.
J.
Robot.
Res.,
30(7),
pp.
846–894.
doi:10.1177/0278364911406761.
[19] Betts, J. T., 1998, “Survey of numerical methods for trajectory optimization,”
J. Guid. Control Dyn., 21(2), pp. 193–207. doi:10.2514/2.4231.
[20] Kelly,
M.,
2017,
“An
introduction
to
trajectory
optimization:
How
to
do
your
own
direct
collocation,”
SIAM Rev.,
59(4),
pp.
849–904.
doi:10.1137/16M1062569.
[21] Dugar, V., Choudhury, S., and Scherer, S., 2017, “A KITE in the Wind: A Kin-
odynamically Constrained Trajectory Library for Quadrotor Planning in Clut-
tered Environments,” Proc. IEEE Int. Conf. Robotics Autom. (ICRA), Singa-
pore, pp. 109–116. doi:10.1109/ICRA.2017.7989017.
12

## Page 31

[22] Marcucci, T., Umenberger, J., Parrilo, P. A., and Tedrake, R., 2023, “Mo-
tion planning around obstacles with convex optimization,” Sci. Robot., 8(84),
eadf7843. doi:10.1126/scirobotics.adf7843.
[23] Deits, R., and Tedrake, R., 2015, “Computing large convex regions of obstacle-
free space through semideﬁnite programming,” in Algorithmic Foundations of
Robotics XI, Springer, pp. 109–124. doi:10.1007/978-3-319-16595-0 7.
[24] Richards, A., and How, J. P., 2005, “Mixed-integer programming for control,”
Proc. American Control Conference (ACC), Portland, OR, USA, pp. 2676–2683.
doi:10.1109/ACC.2005.1470372.
[25] von Wrangel, D., and Tedrake, R., 2024, “Using graphs of convex sets
to guide nonconvex trajectory optimization,” Proc. IEEE/RSJ Int. Conf.
Intelligent Robots and Systems (IROS), Abu Dhabi, UAE, pp. 9863–9870.
doi:10.1109/IROS58592.2024.10802426.
[26] Fliess, M., L´evine, J., Martin, P., and Rouchon, P., 1995, “Flatness and defect of
non-linear systems: Introductory theory and examples,” Int. J. Control, 61(6),
pp. 1327–1361. doi:10.1080/00207179508921959.
[27] Mellinger, D., and Kumar, V., 2011, “Minimum snap trajectory generation and
control for quadrotors,” Proc. IEEE Int. Conf. Robotics Autom. (ICRA), Shang-
hai, China, pp. 2520–2525. doi:10.1109/ICRA.2011.5980409.
[28] DJI, “DJI Onboard SDK Documentation,” [Online]. Available:
https://
developer.dji.com/onboard-sdk/documentation/. Accessed: Oct. 19, 2025.
13

## Page 32

[29] Ahsan, M. A., De Silva, O., Mann, G. K. I., Gosine, R. G., and Jayasiri, A.,
2026, “Geometric disturbance observer based nonlinear model predictive control
of a quadrotor,” ASME Letters in Dynamic Systems and Control, 6(1), 011010.
doi:10.1115/1.4069922.
14

## Page 33

Chapter 2
Literature Review
This chapter provides a review of the state-of-the-art in UAV control and trajectory
planning, establishing the foundation for the technical contributions presented in
subsequent chapters. The review is organized into six main areas: nonlinear model
predictive control approaches for UAVs, disturbance observer design and estimation
techniques, integration of disturbance observers with model predictive control, path
planning methods, trajectory optimization techniques, trajectory optimization within
safe convex corridors, and development of HITL simulation framework for commercial
and industrial drones.
2.1
Classical to Optimal Control Approaches
Quadrotors present a formidable control challenge due to their underactuated dynam-
ics, inherent instability, and susceptibility to external disturbances. As six-degree-of-
freedom systems with only four independent control inputs (rotor thrusts), as shown
in Fig. 2.1, quadrotors must coordinate thrust and attitude to achieve desired trans-
15

## Page 34

lational motion, creating strong coupling between position and orientation dynamics.
This underactuation, combined with nonlinear dynamics and sensitivity to external
disturbances such as wind gusts and payload variations, demands control strategies
that can handle complex dynamics while maintaining stability and performance. The
evolution of quadrotor control has progressed from classical feedback approaches such
as PID control, through advanced robust control techniques including adaptive con-
trol and sliding-mode control, to sophisticated optimal control frameworks such as
MPC that explicitly account for system constraints and nonlinear dynamics.
ω1
ω2
ω3
ω4
z
f1
f2
f3
f4
y
x
N
E
D
Figure 2.1: Quadrotor coordinate system (plus-conﬁguration).
Classical control approaches exhibit fundamental limitations when applied to
quadrotor systems.
PID control, while simple to implement and tune, is funda-
mentally limited in handling the nonlinear dynamics inherent in quadrotor platforms
[2]. The underactuated nature of quadrotors, combined with their susceptibility to
external disturbances such as wind gusts and payload variations, further challenges
16

## Page 35

classical controllers. Advanced control strategies including adaptive control [3] and
sliding-mode control (SMC) [4] improve robustness through online parameter tuning
or discontinuous control terms, respectively. Adaptive control schemes adjust con-
troller parameters in real-time to compensate for model uncertainties and changing
dynamics [3]. Sliding-mode control introduces discontinuous switching terms that
drive the system state to a sliding surface, providing robustness to matched uncer-
tainties and disturbances [4]. However, both approaches lack the ability to explicitly
handle state and input constraints, which are essential for ensuring safe operation
within physical limits of the platform.
Nonlinear Model Predictive Control (NMPC) addresses these limitations by solv-
ing a ﬁnite-horizon optimal control problem at each sampling instant while explicitly
accounting for system nonlinearities and constraints [1]. At each time step, NMPC
predicts future system behavior over a prediction horizon using a nonlinear model,
optimizes a sequence of control inputs to minimize a cost function while satisfying
constraints, and applies only the ﬁrst control input before repeating the process at
the next time step. This receding-horizon strategy enables NMPC to handle time-
varying references and adapt to changing operating conditions.
Recent work has
demonstrated computationally eﬃcient NMPC implementations for quadrotors that
achieve real-time performance through stability-based formulations [1] using CasADi.
Geometric control formulations have further advanced NMPC for quadrotors by
formulating the control problem directly on the vehicle’s conﬁguration manifold, the
Special Euclidean group SE(3), which combines position and rotation. In particular,
Pereira et al. formulate NMPC on SE(3) for aggressive quadrotor maneuvers [5]. By
optimizing over the full pose on the manifold, this approach avoids the singularities of
17

## Page 36

Euler angles and the ambiguities of quaternions, demonstrating improved performance
for agile ﬂight [5].
2.1.1
Learning-Based NMPC
Despite these advances, the performance of NMPC critically depends on the accuracy
of its internal prediction model. Unmodeled dynamics and external disturbances, if
not accounted for, can lead to signiﬁcant performance degradation and even instabil-
ity. Standard NMPC formulations assume that the system model accurately captures
all relevant dynamics, but in practice, model uncertainties and time-varying external
disturbances introduce discrepancies between predicted and actual system behavior.
This model-plant mismatch degrades tracking performance and can even destabilize
the closed-loop system if not handled properly. Learning-based approaches have been
proposed to address model uncertainties by using data-driven techniques to improve
model accuracy [6].
These methods employ machine learning algorithms to learn
model corrections from observed data, potentially improving prediction accuracy.
However, learning-based approaches often require extensive training data to general-
ize eﬀectively and focus primarily on structural model errors rather than time-varying
external disturbances. Thus, while learning can improve a model gradually, it may
not fully solve the need for disturbance rejection in uncertain environments.
2.2
Disturbance Observer-Based Control
To address external disturbances and model uncertainties in real-time, disturbance
observer-based control has emerged as a direct and eﬀective approach. Rather than
18

## Page 37

attempting to learn or model all possible disturbances oﬄine, disturbance observers
estimate unknown forces and torques online and enable controllers to compensate for
them explicitly.
2.2.1
Deterministic Disturbance Observers
Active Disturbance Rejection Control (ADRC) represents a foundational approach
to disturbance estimation and compensation [7]. ADRC employs an extended state
observer (ESO) that augments the system state with an additional “extended state”
representing the lumped eﬀect of all disturbances and unmodeled dynamics. The
ESO estimates both the system states and this extended disturbance state in real-
time, enabling the controller to actively reject disturbances through feedforward com-
pensation. ADRC has demonstrated eﬀectiveness in quadrotor control applications,
providing improved disturbance rejection compared to classical PID control [2]. The
key advantage of ADRC is its model-free approach: by treating all unmodeled dy-
namics and disturbances as a single extended state, ADRC reduces the reliance on
accurate system models.
However, classical ADRC and similar deterministic observers have fundamental
limitations. They do not account for measurement noise characteristics or provide un-
certainty quantiﬁcation, which can limit estimation accuracy under noisy conditions.
More critically, ADRC’s linear feedback control law, while simple and robust, does
not optimize performance subject to constraints. For systems requiring constraint
satisfaction or optimal trajectory tracking, the deterministic observer-controller ar-
chitecture becomes insuﬃcient.
19

## Page 38

2.2.2
Integration with Model Predictive Control
To address the optimality and constraint-handling limitations of deterministic observer-
based control, recent work has integrated disturbance observers with nonlinear model
predictive control (NMPC). Several studies have explored this integration for quadro-
tor control. A ﬁxed-time disturbance observer-based MPC scheme has been proposed
for trajectory tracking under disturbances [14], employing a ﬁxed-time convergent
observer that guarantees disturbance estimation within a ﬁnite time bound. Another
study integrates an extended disturbance observer with MPC for a coaxial octorotor
with variable center of gravity [15], addressing the challenge of controlling a multiro-
tor with time-varying mass distribution. A wind-rejection ESO-MPC framework has
been presented for quadrotor control in wind environments [16], using a nonlinear
extended state observer to estimate wind-induced disturbances.
However, these deterministic observer-MPC approaches share critical limitations.
First, they typically estimate only translational forces while ignoring disturbance
torques, providing incomplete disturbance information for systems requiring full six-
DOF control. Second, most critically, none of these methods embeds the disturbance
estimates directly into the MPC prediction model as time-varying inputs. Instead,
disturbance compensation is applied as feedforward terms after optimization. This
prevents the optimizer from proactively anticipating disturbance eﬀects within the
receding-horizon framework. Third, these deterministic observers become particu-
larly unreliable during aggressive maneuvers where nonlinear dynamics dominate and
measurement noise increases.
20

## Page 39

2.2.3
Stochastic Disturbance Observers
For systems with signiﬁcant measurement noise or during aggressive maneuvers,
stochastic observers can oﬀer improved estimation performance by explicitly model-
ing process and measurement noise. Kalman ﬁlter variants, including the Unscented
Kalman Filter (UKF), have been applied to estimate aerodynamic forces and torques
acting on quadrotors [8].
The UKF uses a deterministic sampling technique, the
unscented transform, to propagate the mean and covariance through nonlinear dy-
namics without Jacobian linearization. By carefully selecting a set of sigma points
that capture the mean and covariance of the state distribution, the UKF propagates
these points through the nonlinear dynamics and reconstructs the predicted mean
and covariance.
Recent work has also explored federated UKF architectures formulated on Lie
group manifolds to improve fault tolerance and estimation accuracy [9]. These ap-
proaches augment the state with a three-degree-of-freedom (3-DOF) lumped external
force to mitigate accelerometer bias under IMU faults, demonstrating improved nav-
igation performance. However, the UKF is computationally expensive due to the
need to propagate multiple sigma points (typically 2n+1 for an n-dimensional state)
through the nonlinear dynamics at each time step, which can limit real-time applica-
bility for high-dimensional systems or fast sampling rates. Furthermore, this method
estimates only translational forces while ignoring disturbance torques, providing in-
complete disturbance information for complete six-DOF control.
21

## Page 40

2.2.4
Geometric State Estimation and Control
For systems whose states evolve on manifolds, such as quadrotors whose orientation
evolves on the SO(3) manifold, geometric observers can be employed for state esti-
mation in a way that respects the manifold structure. These observers avoid singular
parameterizations and can lead to simpler error dynamics. Invariant EKF is a prime
example, developed for systems with symmetries (such as Lie groups) [11]. Barrau and
Bonnabel showed that by exploiting the inherent symmetry in problems like attitude
estimation, one can design EKF-like observers whose error dynamics are independent
of the true state trajectory (they are autonomous). For attitude estimation on SO(3),
they also prove local asymptotic stability of the IEKF under standard conditions [11].
Geometric ﬁltering techniques have also been successfully used in robotics appli-
cations. For instance, for combined vision-inertial odometry where orientation is part
of the state, ﬁlters that operate directly on SO(3) avoid problems like gimbal lock
and have shown better consistency. Modern SLAM and odometry systems often in-
corporate such manifolds; for example, the LVI-SAM system for lidar-visual-inertial
mapping uses a smoothing framework on manifold representations to fuse sensors
eﬀectively [12]. Many other systems (FAST-LIO, ROVIO, etc.) also take advan-
tage of ﬁltering on Lie groups to maintain accuracy and stability during aggressive
motions. Recent theoretical work has generalized Kalman ﬁltering to any diﬀeren-
tiable manifold, laying a foundation for systematically deriving ﬁlters in arbitrary
state spaces [10]. The extension of invariant EKF to include disturbance states has
also been explored, with theoretical results establishing that an invariant EKF can
be augmented to estimate additive disturbances along with the system state while
22

## Page 41

preserving stability under certain conditions [13].
Despite these advances in geometric estimation, and the parallel development of
geometric control methods for systems on manifolds, no existing framework combines
a geometric observer that jointly estimates states and six-DOF disturbances with an
NMPC that embeds those disturbance estimates as time-varying inputs within the
prediction model.
2.3
Path Planning
Path planning for UAVs addresses the fundamental problem of ﬁnding collision-free
paths from start to goal conﬁgurations in environments with obstacles. Traditional
path planning methods focus primarily on geometric collision avoidance without ex-
plicitly considering dynamic feasibility, necessitating substantial post-processing to
generate feasible trajectories.
Graph-search algorithms represent classical approaches to path planning that op-
erate on discretized representations of the conﬁguration space. Dijkstra’s algorithm
[17] systematically explores the conﬁguration space by expanding nodes in order of
increasing cost from the start, guaranteeing optimal solutions within the discretized
domain. The A* algorithm [18] improves computational eﬃciency by incorporating
heuristic guidance toward the goal, reducing the number of nodes explored while
maintaining optimality guarantees when using admissible heuristics.
These algo-
rithms provide completeness and optimality guarantees within the discretized space,
making them reliable for ﬁnding solutions when they exist [19]. However, graph-
search methods suﬀer from several limitations. They produce piecewise-linear paths
23

## Page 42

that lack the smoothness required for UAV execution. Furthermore, they scale poorly
to high-dimensional conﬁguration spaces due to the curse of dimensionality.
Sampling-based planners address the scalability limitations of graph-search meth-
ods through probabilistic exploration of the conﬁguration space. Probabilistic Roadmaps
(PRM) [20] construct a roadmap by randomly sampling collision-free conﬁgurations
and connecting nearby samples with local paths, creating a graph that can be queried
for multiple planning problems. Rapidly-exploring Random Trees (RRT) [21] incre-
mentally build a tree structure by randomly sampling conﬁgurations and extending
the tree toward samples, providing single-query planning with probabilistic complete-
ness. The RRT-Connect variant [22] grows two trees from start and goal simulta-
neously, often achieving faster connection.
RRT* [23] extends RRT with asymp-
totic optimality by rewiring the tree to improve path quality as more samples are
added, providing paths that converge to optimal solutions as the number of sam-
ples approaches inﬁnity. These sampling-based methods oﬀer improved scalability to
high-dimensional spaces compared to graph-search approaches, making them practi-
cal for complex robotic systems. However, like graph-search methods, they generate
piecewise-linear paths with discontinuities in velocity and higher-order derivatives,
requiring nonlinear reﬁnement to achieve dynamic feasibility and smoothness.
Kinodynamic planning [24] addresses the dynamic feasibility limitation by aug-
menting the state space with velocity and higher-order derivatives, enabling the plan-
ner to directly generate dynamically feasible trajectories. By planning in the full
state space (position, velocity, and potentially acceleration), kinodynamic planners
can account for dynamic constraints during the search process. However, this comes
at signiﬁcantly higher computational complexity due to the increased dimensional-
24

## Page 43

ity of the search space. The curse of dimensionality becomes even more severe, and
the computational cost of collision checking and local steering increases substantially.
Furthermore, kinodynamic planning methods often struggle to ﬁnd solutions in clut-
tered environments where the dynamically feasible space is highly constrained.
2.4
Trajectory Optimization
Trajectory optimization methods directly formulate the planning problem as an op-
timal control problem over continuous state and control trajectories. Rather than
separating geometric planning from dynamic feasibility, trajectory optimization si-
multaneously optimizes trajectory while enforcing dynamic constraints.
However,
the resulting optimization problems are typically nonconvex, presenting challenges
for computational eﬃciency and solution quality.
Classical trajectory optimization approaches [25], such as direct collocation [26],
transcribe the continuous optimal control problem into ﬁnite-dimensional nonlinear
programs (NLPs).
While these formulations can explicitly enforce dynamic con-
straints, boundary conditions, and path constraints, the resulting problems are gener-
ally nonconvex due to nonlinear dynamics and obstacle avoidance constraints. Non-
convex NLPs are computationally intensive, requiring good initial guesses for conver-
gence and often converging to local minima [27].
To address convergence challenges, gradient-based trajectory optimization meth-
ods such as CHOMP (Covariant Hamiltonian Optimization for Motion Planning) [28]
iteratively reﬁne trajectories by optimizing smoothness and obstacle cost functionals.
However, these methods remain sensitive to initialization and often converge to local
25

## Page 44

minima. Stochastic approaches like STOMP (Stochastic Trajectory Optimization for
Motion Planning) [29] were developed to overcome such local-minima failures through
stochastic exploration, yet they introduce their own sensitivity to initialization and
noise scaling, imposing practical computational and reliability limits.
Sequential convex optimization [30] addresses nonconvexity through successive
convexiﬁcation, solving sequences of convex subproblems that linearize nonlinear dy-
namics around the current trajectory. While this improves convergence reliability
over gradient-based methods by exploiting the eﬃciency of convex optimization at
each iteration, it typically requires multiple iterations and does not guarantee global
optimality for the original nonconvex problem.
More generally, convex optimization formulations and techniques [31, 32] oﬀer an
attractive alternative by using tractable convex surrogates or relaxations with global
optimality guarantees. When a problem can be formulated convexly, interior-point
methods can ﬁnd the global optimum reliably and eﬃciently, independent of initializa-
tion. When the convexiﬁcation or relaxation is tight, the solution is almost-optimal
for the original problem. The key challenge is reformulating inherently nonconvex
trajectory planning problems into convex or approximately convex forms.
Diﬀerential ﬂatness theory provides a mathematical framework for trajectory pa-
rameterization that can facilitate convex trajectory optimization for certain under-
actuated systems [33]. For diﬀerentially ﬂat systems, all states and control inputs
can be expressed as algebraic functions of ﬂat outputs and their derivatives without
requiring integration. This property enables polynomial trajectory parameterization,
signiﬁcantly simplifying optimization by reducing decision variable dimensionality
and converting diﬀerential constraints into algebraic constraints.
26

## Page 45

This approach has proven successful in aerial robotics. For quadrotors, minimum-
snap trajectory generation [34] optimizes polynomial trajectories for smoothness while
satisfying boundary conditions. Since quadrotors are diﬀerentially ﬂat with position
and yaw as the ﬂat outputs, all states and control inputs can be computed alge-
braically from these outputs and their derivatives up to fourth order. Polynomial
trajectory representations based on B´ezier and B-spline parameterizations oﬀer use-
ful computational properties such as convex-hull containment and linear relationships
between trajectory derivatives [41, 39, 40], enabling the trajectory generation problem
to be formulated as a convex optimization.
While diﬀerential ﬂatness methods have been demonstrated primarily on quadro-
tors [34], applications to ﬁxed-wing UAVs are fewer. For ﬁxed-wing UAVs, existing
trajectory optimization approaches such as [27] formulate the problem as a noncon-
vex program, requiring nonlinear solvers that lack global convergence guarantees and
are sensitive to initialization. Furthermore, most ﬂatness-based methods either as-
sume obstacle-free environments or rely on precomputed safe corridors (e.g., [34]),
without addressing rapid corridor generation. The fundamental challenge is devel-
oping a uniﬁed framework that exploits diﬀerential ﬂatness to convexify dynamic
constraints while simultaneously handling obstacle avoidance through eﬃcient cor-
ridor construction, enabling convex trajectory optimization with global optimality
guarantees within the convexiﬁed problem formulation.
27

## Page 46

2.5
Trajectory Optimization within Safe Corridors
Convex decomposition strategies address the fundamental challenge of obstacle avoid-
ance in trajectory optimization, stemming from the nonconvex nature of obstacle-
cluttered environments. Recent advances in convex decomposition methods tackle
this challenge by partitioning the free space into overlapping convex regions. The
GCS framework, as presented in [35], represents a signiﬁcant advancement in this
direction. GCS decomposes the free space into overlapping convex regions using the
IRIS algorithm [36] and constructs a roadmap over these regions. This approach then
formulates the trajectory planning problem as a Mixed Integer Convex Programming
(MICP). By optimizing discrete region selections along with continuous trajectory
parameters, GCS often yields shorter trajectories and faster online solutions com-
pared to sampling-based methods. However, GCS faces two key limitations. First,
constructing a global convex decomposition of the entire workspace using IRIS is com-
putationally expensive, especially for large environments with dense obstacles. The
IRIS algorithm iteratively inﬂates convex regions while avoiding obstacles through
semideﬁnite programming, and applying this across the entire workspace requires
substantial computation. Second, MICP solve times grow with the number of regions
and binary decision variables [37].
This limitation restricts scalability and makes
real-time replanning challenging when environments or mission parameters change.
Additionally, the standard GCS approach can only incorporate velocity constraints
and generates piecewise-polynomial paths that may exhibit discontinuities in higher-
order derivatives. These discontinuities could potentially violate dynamic constraints.
To address the limitations of convex decomposition and trajectory optimization meth-
28

## Page 47

ods, recent work [38] proposes a hybrid pipeline that combines Global Convex Search
(GCS) with local nonlinear trajectory optimization stages. This approach leverages
GCS for global path planning, followed by local nonlinear reﬁnement to satisfy higher-
order dynamic constraints. The GCS stage handles obstacle avoidance through con-
vex decomposition and MICP, while the second nonlinear reﬁnement stage reﬁnes
the trajectory to ensure dynamic feasibility. While this hybrid approach improves
trajectory quality compared to GCS alone, it inherits the computational expense of
global IRIS-based workspace decomposition from GCS. Additionally, the nonconvex
reﬁnement stage eliminates global optimality guarantees. The separation of obstacle
avoidance and dynamic constraint enforcement into two stages compromises either
computational eﬃciency or solution quality.
Existing approaches trade oﬀsolution quality, computational eﬃciency, and opti-
mality guarantees. Methods with strong guarantees rely on workspace-wide convex
decompositions and MICP, while faster pipelines either decouple geometry from dy-
namics or introduce nonconvex reﬁnement that forfeits guarantees.
2.6
Hardware-in-the-Loop Testing and Validation
While theoretical development and simulation validation are essential steps in the
research process, bridging the gap to practical deployment on commercial UAV plat-
forms remains a critical challenge. Hardware-in-the-Loop (HITL) testing has emerged
as an indispensable methodology for validating planning and control algorithms un-
der realistic hardware constraints while maintaining the safety and repeatability of
simulated environments [47].
29

## Page 48

The progression from algorithm development to deployment typically follows a
multi-stage validation pipeline. Software-in-the-Loop (SITL) simulation represents
the initial development stage, where planning and control algorithms are tested in
purely simulated environments without physical hardware involvement [47]. However,
SITL simulations fail to capture hardware-speciﬁc constraints such as computational
limitations, communication latencies between components, timing jitter in real-time
operating systems, and the actual interfaces exposed by commercial ﬂight controllers
[42]. These discrepancies can lead to algorithms that perform well in SITL but fail
when deployed on actual hardware due to timing issues, communication delays, or
interface incompatibilities.
Hardware-in-the-Loop testing addresses these limitations by executing actual ﬂight
software on real embedded hardware while the vehicle dynamics and environment
remain simulated [42]. In a HITL setup, the onboard computer runs the actual plan-
ning and control algorithms, communicates with the ﬂight controller through physical
hardware interfaces with realistic timing and computational constraints, while the
ﬂight controller executes its internal stabilization loops and safety logic exactly as it
would during real ﬂight but receives simulated sensor inputs and commands simulated
actuators. This conﬁguration reveals issues that cannot be detected in SITL, such
as computational bottlenecks causing control loop delays, communication protocol
errors, and timing synchronization problems. Commercial drone companies routinely
emphasize HITL validation before outdoor ﬂight testing.
Despite these clear beneﬁts, the literature reveals limited documentation of com-
plete and validated HITL workﬂows for commercial DJI platforms. This gap has
persisted throughout the development of quadrotor control research, which primarily
30

## Page 49

validate algorithms through controlled ﬂight experiments on custom research plat-
forms and open autopilot stacks, rather than HITL evaluation [48, 49, 46, 45]. The
gap is particularly pronounced for commercial platforms such as the DJI Matrice
series (e.g. DJI M300 RTK), which are widely used in both research and industry
but remain sparsely documented compared with open-source autopilot stacks like
PX4 and ArduPilot that publish complete HITL procedures. Although DJI’s OSDK
provides programmatic access to DJI ﬂight controllers [42] and OSDK-ROS [44] in-
tegrates these controllers with the Robot Operating System [43], repeatable HITL
workﬂows combining these tools remain scarce in the published literature.
2.7
Bibliography
[1] Gomaa, M. A. K., De Silva, O., Mann, G. K. I., and Gosine, R. G., 2023, “Compu-
tationally eﬃcient stability-based nonlinear model predictive control design for
quadrotor aerial vehicles,” IEEE Trans. Control Syst. Technol., 31(2), pp. 615–
630. doi:10.1109/TCST.2022.3188399.
[2] Ahsan, M. A., Khan, H. Z. I., Rajput, J., and Riaz, J., 2022, “Active disturbance
rejection control of a quadrotor: A comparative study,” Proc. 19th Int. Bhur-
ban Conf. Applied Sciences and Technology (IBCAST), Islamabad, Pakistan,
pp. 444–450.
[3] Dydek, Z. T., Annaswamy, A. M., and Lavretsky, E., 2013, “Adaptive control of
quadrotor UAVs: A design trade study with ﬂight evaluations,” IEEE Trans.
Control Syst. Technol., 21(4), pp. 1400–1406. doi:10.1109/TCST.2012.2200104.
31

## Page 50

[4] Xu, R., and ¨Ozguner, U., 2006, “Sliding mode control of a quadrotor helicopter,”
Proc. 45th IEEE Conf. Decision and Control (CDC), San Diego, CA, USA,
pp. 4957–4962. doi:10.1109/CDC.2006.377588.
[5] Pereira, J. C., Leite, V. J. S., and Raﬀo, G. V., 2021, “Nonlinear model predictive
control on SE(3) for quadrotor aggressive maneuvers,” J. Intell. Robot. Syst.,
101(3), Art. 62. doi:10.1007/s10846-021-01310-8.
[6] Limon, D., Calliess, J., and Maciejowski, J. M., 2017, “Learning-based non-
linear model predictive control,” IFAC-PapersOnLine, 50(1), pp. 7769–7776.
doi:10.1016/j.ifacol.2017.08.1050.
[7] Han, J., 2009, “From PID to active disturbance rejection control,” IEEE Trans.
Ind. Electron., 56(3), pp. 900–906.
[8] McKinnon, C. D., and Schoellig, A. P., 2020, “Estimating and reacting to forces
and torques resulting from common aerodynamic disturbances acting on quadro-
tors,” Robotics Auton. Syst., 123, Art. 103314. doi:10.1016/j.robot.2019.103314.
[9] Sun, X., Lai, J., Lyu, P., Tian, H., and Shen, Y., 2024, “Fault-tolerant
navigation aided by dynamics model of quadrotors based on federated
UKF on Lie group manifold,” IEEE Sensors J., 24(21), pp. 34828–34842.
doi:10.1109/JSEN.2024.3436943.
[10] He, D., Xu, W., and Zhang, F., 2021, “Kalman ﬁlters on diﬀerentiable mani-
folds,” arXiv preprint arXiv:2102.03804.
32

## Page 51

[11] Barrau, A., and Bonnabel, S., 2017, “The invariant extended Kalman ﬁlter
as a stable observer,” IEEE Trans. Autom. Control, 62(4), pp. 1797–1812.
doi:10.1109/TAC.2016.2594085.
[12] Shan, T., Englot, B., Ratti, C., and Rus, D., 2021, “LVI-SAM: Tightly-
coupled lidar–visual–inertial odometry via smoothing and mapping,” Proc.
IEEE Int. Conf. Robotics Autom. (ICRA), Xi’an, China, pp. 5692–5698.
doi:10.1109/ICRA48506.2021.9561996.
[13] Coleman, K., Bai, H., and Taylor, C. N., 2021, “Extended invariant-EKF designs
for state and additive disturbance estimation,” Automatica, 125, Art. 109464.
doi:10.1016/j.automatica.2020.109464.
[14] Xu, L., Tian, B., Wang, C., Lu, J., Wang, D., Li, Z., and Zong, Q., 2025,
“Fixed-time disturbance observer–based MPC robust trajectory tracking control
of quadrotor,” IEEE/ASME Trans. Mechatron., pp. 1–11.
[15] Derakhshan, R. E., Danesh, M., and Moosavi, H., 2024, “Disturbance observer–
based model predictive control of a coaxial octorotor with variable centre of
gravity,” IET Control Theory Appl., 18(6), pp. 764–783. doi:10.1049/cth2.12611.
[16] Chen, C., Zhang, X., and Peng, X., 2024, “Trajectory tracking control of four-
rotor UAV based on nonlinear extended state observer and model predictive con-
trol in wind disturbance environment,” J. Phys.: Conf. Ser., 2764(1), p. 012075.
doi:10.1088/1742-6596/2764/1/012075.
[17] Dijkstra, E. W., 1959, “A note on two problems in connexion with graphs,”
Numer. Math., 1(1), pp. 269–271. doi:10.1007/BF01386390.
33

## Page 52

[18] Hart, P. E., Nilsson, N. J., and Raphael, B., 1968, “A formal basis for the heuristic
determination of minimum cost paths,” IEEE Trans. Syst. Sci. Cybern., 4(2),
pp. 100–107. doi:10.1109/TSSC.1968.300136.
[19] LaValle, S. M., 2006, Planning Algorithms, Cambridge University Press, Cam-
bridge, UK.
[20] Kavraki, L. E., Svestka, P., Latombe, J.-C., and Overmars, M. H., 1996, “Prob-
abilistic roadmaps for path planning in high-dimensional conﬁguration spaces,”
IEEE Trans. Robot. Autom., 12(4), pp. 566–580. doi:10.1109/70.508439.
[21] LaValle, S. M., and Kuﬀner, J. J., 2001, “Randomized kinodynamic planning,”
Int. J. Robot. Res., 20(5), pp. 378–400. doi:10.1177/027836490102000503.
[22] Kuﬀner, J. J., and LaValle, S. M., 2000, “RRT-Connect: An eﬃcient approach
to single-query path planning,” Proc. IEEE Int. Conf. Robotics Autom. (ICRA),
San Francisco, CA, USA, pp. 995–1001. doi:10.1109/ROBOT.2000.844730.
[23] Karaman,
S.,
and
Frazzoli,
E.,
2011,
“Sampling-based
algorithms
for
optimal
motion
planning,”
Int.
J.
Robot.
Res.,
30(7),
pp.
846–894.
doi:10.1177/0278364911406761.
[24] Donald, B. R., Xavier, P., Canny, J., and Reif, J., 1993, “Kinodynamic motion
planning,” J. ACM, 40(5), pp. 1048–1066. doi:10.1145/174147.174150.
[25] Betts, J. T., 1998, “Survey of numerical methods for trajectory optimization,”
J. Guid. Control Dyn., 21(2), pp. 193–207. doi:10.2514/2.4231.
34

## Page 53

[26] Kelly,
M.,
2017,
“An
introduction
to
trajectory
optimization:
How
to
do
your
own
direct
collocation,”
SIAM Rev.,
59(4),
pp.
849–904.
doi:10.1137/16M1062569.
[27] Dugar,
V.,
Choudhury,
S.,
and
Scherer,
S.,
2017,
“A
κITE
in
the
wind:
Smooth
trajectory
optimization
in
a
moving
reference
frame,”
Proc. IEEE Int. Conf. Robotics Autom. (ICRA), Singapore, pp. 109–116.
doi:10.1109/ICRA.2017.7989017.
[28] Ratliﬀ, N., Zucker, M., Bagnell, J. A., and Srinivasa, S., 2009, “CHOMP:
Gradient
optimization
techniques
for
eﬃcient
motion
planning,”
Proc.
IEEE Int. Conf. Robotics Autom. (ICRA), Kobe,
Japan,
pp. 489–494.
doi:10.1109/ROBOT.2009.5152817.
[29] Kalakrishnan, M., Chitta, S., Theodorou, E., Pastor, P., and Schaal, S.,
2011, “STOMP: Stochastic trajectory optimization for motion planning,” Proc.
IEEE Int. Conf. Robotics Autom. (ICRA), Shanghai, China, pp. 4569–4574.
doi:10.1109/ICRA.2011.5980280.
[30] Schulman, J., Ho, J., Lee, A., Awwal, I., Bradlow, H., and Abbeel, P., 2014, “Mo-
tion planning with sequential convex optimization and convex collision checking,”
Int. J. Robot. Res., 33(9), pp. 1251–1270. doi:10.1177/0278364914528132.
[31] Boyd, S., and Vandenberghe, L., 2004, Convex Optimization, Cambridge Uni-
versity Press, Cambridge, UK.
[32] Nesterov, Y., and Nemirovskii, A., 1994, Interior-Point Polynomial Algorithms
in Convex Programming, SIAM, Philadelphia, PA, USA.
35

## Page 54

[33] Fliess, M., L´evine, J., Martin, P., and Rouchon, P., 1995, “Flatness and defect of
non-linear systems: Introductory theory and examples,” Int. J. Control, 61(6),
pp. 1327–1361.
[34] Mellinger, D., and Kumar, V., 2011, “Minimum snap trajectory generation and
control for quadrotors,” Proc. IEEE Int. Conf. Robotics Autom. (ICRA), Shang-
hai, China, pp. 2520–2525. doi:10.1109/ICRA.2011.5980409.
[35] Marcucci, T., Umenberger, J., Parrilo, P. A., and Tedrake, R., 2023, “Mo-
tion planning around obstacles with convex optimization,” Sci. Robot., 8(84),
eadf7843.
[36] Deits, R., and Tedrake, R., 2015, “Computing large convex regions of obstacle-
free space through semideﬁnite programming,” Algorithmic Foundations of
Robotics XI, Springer, pp. 109–124. doi:10.1007/978-3-319-16595-0 7.
[37] Richards, A., and How, J. P., 2005, “Mixed-integer programming for control,”
Proc. American Control Conference (ACC), Portland, OR, USA, pp. 2676–2683.
doi:10.1109/ACC.2005.1470372.
[38] von Wrangel, D., and Tedrake, R., 2024, “Using graphs of convex sets
to guide nonconvex trajectory optimization,” Proc. IEEE/RSJ Int. Conf.
Intelligent Robots and Systems (IROS), Abu Dhabi, UAE, pp. 9863–9870.
doi:10.1109/IROS58592.2024.10802426.
[39] Farouki, R. T., 2012, “The Bernstein polynomial basis: A centennial retrospec-
tive,” Comput. Aided Geom. Des., 29(6), pp. 379–419.
36

## Page 55

[40] Piegl, L., and Tiller, W., 1997, The NURBS Book, 2nd ed., Springer, Berlin,
Germany.
[41] Richter, C., Bry, A., and Roy, N., 2016, “Polynomial trajectory planning for
aggressive quadrotor ﬂight in dense indoor environments,” in Robotics Research
(The 16th International Symposium ISRR, 2013), Springer Tracts in Advanced
Robotics, pp. 649–666. doi:10.1007/978-3-319-28872-7 37.
[42] DJI, 2020, “Onboard SDK (OSDK) documentation,” [Online]. Available: https:
//developer.dji.com/onboard-sdk/. Accessed: Jan. 12, 2026.
[43] Quigley, M., Conley, K., Gerkey, B., Faust, J., Foote, T., Leibs, J., Wheeler,
R., and Ng, A. Y., 2009, “ROS: An open-source robot operating system,” ICRA
Workshop on Open Source Software, Kobe, Japan.
[44] DJI, 2020, “OSDK-ROS: ROS wrapper for DJI Onboard SDK,” [Online]. Avail-
able:
https://github.com/dji-sdk/Onboard-SDK-ROS. Accessed:
Jan. 12,
2026.
[45] Kamel, M., Burri, M., and Siegwart, R., 2017, “Linear vs nonlinear MPC
for trajectory tracking applied to rotary wing micro aerial vehicles,” IFAC-
PapersOnLine, 50(1), pp. 3463–3469. doi:10.1016/j.ifacol.2017.08.849.
[46] Pounds, P., Mahony, R., and Corke, P., 2010, “Modelling and control
of a large quadrotor robot,”
Control Eng. Pract.,
18(7),
pp. 691–699.
doi:10.1016/j.conengprac.2010.02.008.
37

## Page 56

[47] Mahony, R., Kumar, V., and Corke, P., 2012, “Multirotor aerial vehicles: Mod-
eling, estimation, and control of quadrotor,” IEEE Robot. Autom. Mag., 19(3),
pp. 20–32. doi:10.1109/MRA.2012.2206474.
[48] Bouabdallah, S., Noth, A., and Siegwart, R., 2004, “PID vs LQ control tech-
niques applied to an indoor micro quadrotor,” Proc. IEEE/RSJ Int. Conf. In-
telligent Robots and Systems (IROS), Sendai, Japan, pp. 2451–2456.
[49] Hoﬀmann, G., Huang, H., Waslander, S., and Tomlin, C., 2007, “Quadrotor
helicopter ﬂight dynamics and control: Theory and experiment,” Proc. AIAA
Guidance, Navigation and Control Conf. and Exhibit, Hilton Head, SC, USA,
p. 6461. doi:10.2514/6.2007-6461.
38

## Page 57

Chapter 3
Geometric Disturbance Observer
Based Nonlinear Model Predictive
Control of a Quadrotor
This chapter has been published in the American Society of Mechanical Engineers (ASME)
Letters in Dynamic Systems and Control.
Abstract
This letter presents a geometric disturbance-observer (DO) based nonlinear model
predictive control (NMPC) architecture for quadrotor trajectory tracking. The pro-
posed approach couples a geometric extended-state extended Kalman ﬁlter (ES-EKF)
formulated on the SO(3) manifold with a disturbance-aware predictive controller.
By embedding explicit force and torque disturbance states into the continuous-time
model, the ES-EKF obtains real-time estimates of six-degree-of-freedom (DOF) per-
39

## Page 58

turbations. These disturbance estimates are injected as known parameters into the
NMPC’s prediction model at each sampling instant, enabling proactive compensation
within the receding-horizon optimization. Simulations are conducted on diﬀerent tra-
jectories with varied ﬂight conditions subjected to periodic six-DOF perturbations.
The proposed ES-EKF-NMPC framework reduces position root mean square error
(RMSE) by 60% on average compared to baseline NMPC without disturbance feed-
back. These results demonstrate that the proposed architecture oﬀers disturbance-
resilient control for under-actuated unmanned aerial vehicles (UAVs) while handling
constraints.
3.1
Introduction
Quadrotors have become indispensable for various applications due to their agility and
hovering capability. However, they remain highly susceptible to external disturbances
such as wind gusts and payload variations, which introduce unpredictable forces and
torques that degrade stability and tracking accuracy. Proportional-integral-derivative
(PID) control is a common choice for quadrotor control, but its simplistic nature lim-
its its eﬀectiveness in handling nonlinear errors related to the platform’s dynamics
[1]. Adaptive control [2] and sliding-mode control (SMC) [3] schemes improve ro-
bustness by tuning parameters online or adding discontinuous terms, respectively,
but are unable to handle constraints. Nonlinear model predictive control (NMPC)
addresses these limitations explicitly by solving a constrained optimal-control prob-
lem while considering the system’s nonlinear dynamics at each sampling instant [4].
However, the performance of standard NMPC is critically dependent on the accu-
40

## Page 59

racy of its internal model. Unmodeled dynamics and external disturbances, if not
accounted for, can lead to signiﬁcant performance degradation and even instability.
To address model uncertainties, learning-based approaches have been proposed [5].
However, these methods often require extensive training data to generalize and fo-
cus primarily on structural model errors rather than time-varying disturbances. For
handling unknown external forces and torques speciﬁcally, a more direct strategy is
to explicitly estimate and reject them in real-time.
One such approach for eﬀec-
tive disturbance compensation is Active Disturbance Rejection Control (ADRC) [6],
which employs an extended state observer (ESO) to estimate and compensate for
disturbances. While eﬀective [1], ADRC also lacks the ability to explicitly handle
constraints. To address this limitation, several studies have integrated a disturbance
observer (DO) with model predictive control (MPC). In [7], a ﬁxed-time DO-MPC
scheme is proposed for trajectory tracking of quadrotors under disturbances, but it
only estimates translational forces and relies on Euler angles in attitude dynamics.
Another study integrates an extended DO with MPC on a coaxial octorotor, but
the disturbance estimate is applied in a feed-forward step after the optimization and
therefore never enters the prediction model [8]. A wind-rejection ESO-MPC is pre-
sented in [9]; however, it uses a decoupled architecture with MPC for position control
and SMC for attitude control, where the ESO disturbance estimates are applied only
as feedforward terms and never embedded in the MPC prediction model. All these
approaches suﬀer from fundamental limitations: incomplete disturbance modeling
(forces only), singularity-prone attitude representations, and none embeds the dis-
turbance estimate directly into the MPC prediction model, preventing the optimizer
from anticipating its eﬀects. Moreover, the deterministic observers underlying these
41

## Page 60

schemes become particularly unreliable during aggressive maneuvers where nonlinear
dynamics dominate. For accurate estimation under such challenging conditions, ad-
vanced stochastic observers have emerged as promising alternatives. The unscented
Kalman ﬁlter (UKF) is used in [10] to estimate aerodynamic forces and torques, but
it is computationally expensive due to sigma-point propagation. More recently, [11]
presents a federated Lie-group UKF with a three-degree-of-freedom (3-DOF) lumped
external-force state to mitigate accelerometer bias under inertial measurement unit
(IMU) faults; however, it ignores disturbance torques. For quadrotors whose orien-
tation evolves on the SO(3) manifold, geometric observers oﬀer computational eﬃ-
ciency with singularity-free representation, critical during aggressive maneuvers [12].
Recent theoretical advances have provided convergence guarantees for invariant ex-
tended Kalman ﬁlter (EKF) on manifolds [13]. These manifold-based approaches have
also shown success in robotic simultaneous localization and mapping (SLAM) appli-
cations such as FAST-LIO, LVIO, and ROVIO [14]. Additionally, recent work has
explored geometric NMPC formulations for quadrotor control [15]. However, despite
the individual merits of geometric estimation and geometric control, to the best of
the authors’ knowledge, no existing framework [7, 8, 9] combines a geometric observer
that jointly estimates states and six-DOF disturbances, with an NMPC that embeds
those disturbance estimates as time-varying inputs within the prediction model.
To address this gap, we present an extended-state extended Kalman ﬁlter (ES-
EKF)-based NMPC framework that uniﬁes geometric state and six-DOF disturbance
estimation with disturbance-aware predictive control. Unlike classical ADRC, our
approach provides singularity-free estimation on manifolds and incorporates distur-
bance estimates directly into the receding-horizon optimization. We use a diﬀerential-
42

## Page 61

ﬂatness based trajectory planner that generates reference states and inputs for the
NMPC cost function, unifying feedforward and feedback control rather than relying on
feedback linearization [16]. We augment the continuous-time dynamics with explicit
force and torque disturbance states, which the ES-EKF then propagates, yielding real-
time estimates of all states and disturbances. The disturbance estimates are treated
as known, time-varying parameters in the NMPC’s receding-horizon optimization,
enabling the solver to compensate for disturbances while enforcing state and input
constraints. Simulation results demonstrate the framework’s eﬀective tracking per-
formance and disturbance rejection capabilities across various trajectory types under
periodic six-DOF disturbances. The main contributions of this paper are:
 A novel ES-EKF based NMPC framework for quadrotor trajectory tracking.
 A disturbance-aware predictive model in the NMPC that treats six-DOF dis-
turbance estimates as known, time-varying inputs, enabling proactive compen-
sation within the receding-horizon optimization for a quadrotor.
 An ES-EKF formulated on the SO(3) manifold, providing singularity-free real-
time estimates of all states along with disturbance forces and torques for a
quadrotor.
3.2
Methodology
This section details the design and integration of the main components of our geo-
metric disturbance-observer based predictive control architecture. In the ﬁrst step, a
diﬀerentially-ﬂat trajectory planner generates desired state and input proﬁles, which
43

## Page 62

are then smoothed to ensure dynamic feasibility, as indicated in Fig. 3.1, and then
passed to the disturbance-aware NMPC controller. The design details for the trajec-
tory generation are presented in Section 2.2. The NMPC and ES-EKF modules of
the proposed architecture are also indicated in Fig. 3.1, with design details presented
in Sections 2.3 and 2.4, respectively. The proposed geometric ES-EKF, operating
directly on the SO(3) manifold, provides singularity-free estimation of both states
and external disturbances for a forward prediction horizon. These estimates are then
injected into the NMPC augmented prediction model, enabling proactive disturbance
compensation in all six-DOF while respecting system constraints. The resulting op-
timal thrust command is applied directly, whereas the optimal attitude set-points
are forwarded to an inner-loop proportional-derivative (PD) controller that generates
the required body torques. Finally, the measurements are fed back to the ES-EKF,
closing the control loop.
Figure 3.1: ES-EKF Based NMPC Architecture.
44

## Page 63

3.2.1
Mathematical Model
We begin by formulating an augmented state-space model that incorporates both the
translational and rotational dynamics of the quadrotor along with external distur-
bance forces and torques as extended states. This augmented model is propagated
inside the geometric ES-EKF, while the NMPC treats the disturbance components
as measured (known) parameters. The augmented state vector x(t) is deﬁned as:
x(t) =

p(t)
v(t)
R(t)
ω(t)
fd(t)
τ d(t)
⊤
(3.1)
where p(t) ∈R3 is the position vector in the inertial frame; v(t) ∈R3 is the linear
velocity in the inertial frame; R(t) ∈SO(3) is the rotation matrix representing the
quadrotor’s orientation; ω(t) ∈R3 is the angular velocity expressed in the body-ﬁxed
frame; and fd(t), τ d(t) ∈R3 are the external disturbance force and torque vectors,
respectively, expressed in the inertial frame for consistency. The control input vector
u(t), which comprises the total thrust fb(t) generated by the four rotors and the
body-frame torque vector τ b(t) ∈R3 for attitude control, is deﬁned as:
u(t) =

fb(t)
τ b(t)
⊤
(3.2)
The nonlinear system dynamics ˙x(t) = f(x(t), u(t)) can be written as:


˙p
˙v
˙R
˙ω
˙fd
˙τ d


=


v
R fb
m¯e3 −g + fd
m
R[ω]×
I−1 τ b + R⊤τ d −ω × (Iω)

ηf
ητ


(3.3)
45

## Page 64

where m is the mass, g is the gravitational acceleration vector, I is the inertia matrix,
¯e3 = [0, 0, 1]T, and [·]× denotes the skew-symmetric matrix corresponding to the cross
product. The disturbance force fd and torque τ d terms are modeled as random walks
driven by zero-mean Gaussian noise processes ηf and ητ, respectively.
3.2.2
Reference Trajectory Generation
The reference trajectory sequence {(xr,i, ur,i)}N
i=0 is systematically generated through
a two-stage process designed to ensure dynamic feasibility. This approach leverages
the diﬀerential ﬂatness property of a quadrotor to generate an initial trajectory [17],
which is subsequently reﬁned through NMPC optimization. The resulting state and
input proﬁles serve as reference signals in the NMPC cost function.
3.2.2.1
Stage 1: Diﬀerential Flatness-Based Planning
Quadrotor dynamics are diﬀerentially ﬂat with ﬂat outputs σ = [ p, ψ ]⊤. Deﬁning
the state and control vectors as x = [p, v, R, ω]⊤and u = [fb, τ b]⊤, every component
of x and u can be recovered algebraically from any desired position trajectory pd(t)
and yaw trajectory ψd(t) and their derivatives up to the fourth order, without inte-
grating the diﬀerential equations [17]. We begin by calculating the resultant force
vector as:
αd = m¨pd + mg
(3.4)
The desired body z-axis direction is aligned with this force vector:
zB,d =
αd
∥αd∥
(3.5)
46

## Page 65

The complete attitude matrix Rd is constructed by deﬁning intermediate body frame
vectors. An intermediate vector xC(t) is chosen to align the body x-axis with the
horizontal tangent of the desired path:
xC(t) =
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
zW × ˙pd(t)
∥zW × ˙pd(t)∥
if ∥˙pd(t)∥> ε
[1, 0, 0]⊤
otherwise
(3.6)
where zW = [0, 0, 1]⊤is the world-up axis and ε > 0 is a small threshold that
prevents division by zero when the horizontal speed becomes negligible. The body
frame vectors are then constructed as:
yB,d =
zB,d × xC
∥zB,d × xC∥,
xB,d =
yB,d × zB,d
∥yB,d × zB,d∥
(3.7)
yielding the desired rotation matrix:
Rd = [xB,d, yB,d, zB,d]
(3.8)
The desired thrust magnitude is computed by projecting the force vector along the
body z-axis as fb,d = zT
B,dαd.
The desired angular velocity and acceleration are
computed using ﬁnite diﬀerences as:
ωd(t) = LogSO(3)(RT
d (t −∆t)Rd(t))
∆t
(3.9)
˙ωd(t) = ωd(t) −ωd(t −∆t)
∆t
(3.10)
Finally, the required body torques are computed using the rotational dynamics equa-
tion as:
τ b,d = I ˙ωd + ωd × (Iωd)
(3.11)
47

## Page 66

This completes the diﬀerential ﬂatness mapping from desired ﬂat outputs σ = [pd, ψd]T
to the full system states xd,i and control inputs ud,i. Various trajectory types can be
generated by specifying appropriate parametric functions for pd(t) and ψd(t).
3.2.2.2
Stage 2: NMPC-Based Trajectory Smoothing
The initial trajectory from diﬀerential ﬂatness may not satisfy all system constraints.
Therefore, a second stage applies NMPC with the full prediction horizon N = Tsim/∆t
to generate a dynamically feasible reference trajectory. This optimization process
solves the complete OCP formulation:
min
{xi,ui}
N−1
X
i=0
∥xi −xd,i∥2
Q + ∥ui −ud,i∥2
R + ∥xN −xd,N∥2
QN
(3.12)
subject to the disturbance-free system dynamics, initial conditions, and constraints,
where xd,i and ud,i are the initial trajectories from Stage 1. This two-stage approach
ensures that the ﬁnal reference trajectory {(xr,i, ur,i)}N
i=0 is dynamically feasible.
3.2.3
Nonlinear Model Predictive Control
We propose a disturbance-aware NMPC scheme for quadrotor trajectory control under
external perturbations. At each discrete time step k, the NMPC algorithm solves a
ﬁnite-horizon optimal control problem (OCP). The OCP computes the optimal total
thrust force fb and attitude set-points, including the desired roll angle ϕd, pitch angle
θd, and yaw rate ψr,d. This optimization process utilizes the current state estimate
ˆxk provided by the geometric ES-EKF, which includes real-time estimates of external
disturbance forces ˆfd,k and torques ˆτ d,k, and the pre-computed dynamically feasible
48

## Page 67

reference trajectory sequence {(xr,i, ur,i)}N
i=0:
min
{xk+i,uk+i}
N−1
X
i=0
xk+i −xr,i
2
Q +
uk+i −ur,i
2
R +
xk+N −xr,N
2
QN
(3.13)
s.t.
xk+i+1 = fk
xk+i, uk+i, ˆdk+i

,
i = 0:N −1,
xk+0 = ˆxk,
xmin ≤xk+i ≤xmax,
i = 1:N,
umin ≤uk+i ≤umax,
i = 0:N −1.
where both the state vectors xk+i and control vectors uk+i are optimization variables.
The state vector is xk =

pk
vk
Rk
ωk
⊤
.
The disturbance estimates ˆdk =
[ˆfd,k, ˆτ d,k ]⊤are supplied by the ES-EKF and are treated as known parameters held
constant over the prediction horizon. The control vector is uk =

fb,k
ϕd,k
θd,k
ψr,d,k
⊤
.
The dynamics function fk represents the ﬁrst-order Euler discretisation of the continuous-
time quadrotor dynamics over the sampling interval ∆t, and can be written as:
xk+1 = fk(xk, uk, ˆdk)
≈


pk + vk ∆t
vk + ∆t

Rk
fb,k
m ¯e3 −g +
ˆfd,k
m

Rk exp
[ωk]×∆t

ωk + ∆t I−1
τ b,k + R⊤
k ˆτ d,k −ωk×Iωk



.
(3.14)
The weighting matrices Q ≻0, R ≻0, QN ≻0 penalize state errors, control eﬀort,
and terminal state errors, respectively. Estimated disturbances ˆfd,k, ˆτ d,k are directly
incorporated in OCP (3.13), allowing NMPC to proactively compensate for them,
similar to ADRC [6] but within a constraint-aware optimal framework. This inte-
49

## Page 68

gration enables the controller to generate optimal state and control trajectories that
not only track the reference but also compensate for six-DOF force and torque dis-
turbances in real-time.
At each time step k, only the ﬁrst optimal control input
u⋆
k = [f ∗
b,k, ϕ∗
d,k, θ∗
d,k, ψ∗
r,d,k]⊤is applied. The optimal thrust f ∗
b,k is applied directly,
while attitude set-points ϕ∗
d,k, θ∗
d,k, ψ∗
r,d,k are passed to an inner-loop PD controller,
which computes the required body torques τ b to track these set-points as deﬁned in
Eq. (3.15), separating the position and attitude control:
τ b =


Kp,ϕ(ϕ∗
d,k −ϕ) + Kw,ϕ(pd −p)
Kp,θ(θ∗
d,k −θ) + Kw,θ(qd −q)
Kw,ψ(ψ∗
r,d,k −r)


(3.15)
where ϕ, θ are the current roll and pitch angles, p, q, r are the body angular rates,
pd, qd are the desired angular rates, and the PD gains are listed in Table 3.1. At
the next time step k + 1, the horizon shifts, new states ˆxk+1 and disturbance ˆdk+1
estimates are obtained, and the optimization (3.13) is repeated.
3.2.4
Geometric Extended State Extended Kalman Filter
3.2.4.1
Sensor Inputs and Observer Structure
At each sampling instant k, the ES–EKF receives pose measurements (yp,k, yR,k) from
a motion-capture system (e.g., OptiTrack or Vicon) and rotor-speed measurements
{Ωi,k}4
i=1 from the electronic speed controllers (ESCs). Thrust and body torques are
then reconstructed online from {Ωi,k}4
i=1 using standard motor-mixing (allocation)
algorithms [10]. In hardware, the ES–EKF reconstructs fb,k and τ b,k from {Ωi,k}4
i=1,
whereas in simulation we inject the commanded thrust and body torques directly.
50

## Page 69

3.2.4.2
Linear State Error Dynamics on Lie Groups
For EKF implementation, we ﬁrst linearize the system ˙x = f(x, u, w) and measure-
ment y = h(x, ν) dynamics around an equilibrium point. Using ﬁrst-order Taylor
expansion, we obtain the state-space matrices F, B, Gw, and H, resulting in the
linear approximation:
˙x = Fx + Bu + Gww,
(3.16)
y = Hx + ν.
(3.17)
where w =

νf
ντ
ηf
ητ
⊤
denotes the process noise, and ν =

νp
νR
⊤
is
the measurement noise. The state-estimate dynamics of the linear observer can be
written as:
˙ˆx = Fˆx + Bu + K(y −Hˆx).
(3.18)
For systems involving Lie groups, the state error can be deﬁned using the inverse
mapping ⊖as δx = x ⊖ˆx, and the error perturbation is deﬁned using the retraction
operation ⊕as x = ˆx⊕δx. Diﬀerent error formulations for observers on Lie groups can
be found in [18]. Now, deﬁning the linear error state as δx = x⊖ˆx and diﬀerentiating
it yields the following error state system:
δ ˙x = (F −KH)δx + Gww −Kν.
(3.19)
51

## Page 70

The error state vector δx = x ⊖ˆx, and the retraction operation x = ˆx ⊕δx expands
to:
δx =


δp
δv
δθ
δω
δfd
δτ d


=


p −ˆp
v −ˆv
LogSO(3)( ˆR⊤R)
ω −ˆω
fd −ˆfd
τ d −ˆτ d


,


p
v
R
ω
fd
τ d


=


ˆp + δp
ˆv + δv
ˆR ExpSO(3)(δθ)
ˆω + δω
ˆfd + δfd
ˆτ d + δτ d


.
(3.20)
Linearizing the continuous-time dynamics in Eq. (3.3) around the estimate ˆx yields
the error dynamics δ ˙x ≈F(ˆx, u)δx + Gww, where w includes process noise ηf, ητ.
The Jacobians F and Gw are derived considering the Lie group structure as:
F =


03×3
I3×3
03×3
03×3
03×3
03×3
03×3
03×3
−ˆR[a]×
03×3
1
m I3×3
03×3
03×3
03×3
[−ˆω]×
I3×3
03×3
03×3
03×3
03×3
I−1[ ˆR⊤ˆτ d]×
I−1∆(ˆω)
03×3
I−1 ˆR⊤
03×3
03×3
03×3
03×3
03×3
03×3
03×3
03×3
03×3
03×3
03×3
03×3


(3.21)
Gw =


03×1
03×3
03×3
03×3
1
m ˆR¯e3
03×3
03×3
03×3
03×1
03×3
03×3
03×3
03×1
I−1
03×3
03×3
03×1
03×3
I3×3
03×3
03×1
03×3
03×3
I3×3


.
(3.22)
52

## Page 71

where 0i×j and Ii×i are zero and identity matrices, a = fb
m¯e3, and ∆(ω) = [Iω]× −
[ω]×I. The process noise covariance matrix is Qw = diag
σ2
f, σ2
τ I3×3, σ2
fd I3×3, σ2
τd I3×3

.
Assuming measurements of position yp and orientation yR are available, corrupted
by measurement noise νp and νR, respectively, the measurement residual δy is formed
using the geometric error deﬁnition in Eq. (3.20) as:
δy =


yp −ˆp
LogSO(3)
 ˆR⊤yR



≈


I3×3
03×3
03×3
03×3
03×3
03×3
03×3
03×3
I3×3
03×3
03×3
03×3


|
{z
}
H
δx + ν.
(3.23)
where H is the measurement Jacobian. The measurement noise covariance matrix
is Rν = diag(σ2
pI3×3, σ2
RI3×3), where σp and σR represent the standard deviations
for position and orientation measurement noise, respectively.
The noise mapping
Jacobian which maps measurement noise to the error space is deﬁned as Gν = I6×6.
3.2.4.3
Observer Propagation and Update
Algorithm 1 presents the propagation and update procedure for the proposed ES–EKF.
The structure follows the standard EKF predict-update cycle, adapted for the Lie
group.
53

## Page 72

Algorithm 1 Observer Propagation and Update
Propagation:
dv ←ˆRn
fb,n
m ¯e3 −g +
ˆfd,n
m
dω ←I−1
ˆR⊤
n ˆτ d,n + τ b,n −ˆωn × (I ˆωn)

ˆp−
n+1 ←ˆpn + ˆvn ∆t + 1
2 dv ∆t2
ˆv−
n+1 ←ˆvn + dv ∆t
ˆω−
n+1 ←ˆωn + dω ∆t
ˆR−
n+1 ←ˆRn ExpSO(3)

ˆωn ∆t + 1
2 dω ∆t2
Orthogonalize via SVD: ˆR−
n+1 = UΣV⊤and set ˆR−
n+1 ←UV⊤
Set ˆf −
d,n+1 = ˆfd,n and ˆτ −
d,n+1 = ˆτ d,n
Form propagated state:
ˆx−
n+1 ←
h
ˆp−
n+1, ˆv−
n+1, ˆR−
n+1, ˆω−
n+1, ˆf −
d,n+1, ˆτ −
d,n+1
i⊤
Compute Φ ←I18×18 + F ∆t + 1
2 F2 ∆t2
Compute Gd ←Gw ∆t + 1
2 F Gw ∆t2
Set Qd ←Gd Qw G⊤
d
Predict covariance: P−
n+1 ←Φ Pn Φ⊤+ Qd
Update:
S ←H P−
n+1 H⊤+ Gν Rν G⊤
ν
K ←P−
n+1 H⊤S−1
δy ←
h
yp −ˆp−
n+1, LogSO(3)
( ˆR−
n+1)⊤yR
i⊤
δx ←K δy
Update state components:
ˆpn+1 = ˆp−
n+1 + δp,
ˆvn+1 = ˆv−
n+1 + δv
ˆRn+1 = ˆR−
n+1 ExpSO(3)(δθ),
ˆωn+1 = ˆω−
n+1 + δω
ˆfd,n+1 = ˆf −
d,n+1 + δfd,
ˆτ d,n+1 = ˆτ −
d,n+1 + δτ d
Correct covariance: Pn+1 ←P−
n+1 −K H P−
n+1
54

## Page 73

The resulting state estimates ˆxn+1, particularly the disturbance estimates ˆfd,n+1
and ˆτ d,n+1, are then fed into the NMPC formulation Eq. (3.13) at the next time step,
closing the loop and enabling disturbance compensation.
3.3
Results and Discussion
Numerical simulations are conducted in MATLAB to compare ES-EKF-NMPC with
standard NMPC [16] on diﬀerent trajectories under identical periodic disturbances.
The optimal control problem in Eq. (3.13) is formulated using the CasADi symbolic
framework [19], chosen for its eﬃciency in nonlinear optimization and compatibil-
ity with C++, Python, and MATLAB. We discretize the OCP via direct multi-
ple shooting [20], converting it into a nonlinear programming problem (NLP). Fi-
nally, the resulting NLP is solved using Interior Point Optimizer (IPOPT), which
is integrated with CasADi. Using the nonlinear model from Eq. (3.3) with predic-
tion horizon N = 25 and sampling time ∆t = 0.02 s, we set weighting matrices
Q = diag(10I6×6, 100I3×3, 10I3×3) and R = I4×4. Key simulation parameters, includ-
ing inertial parameters for the quadrotor, actuation limits, and control and estimation
parameters, are listed in Table 3.1. We evaluate the performance of the proposed
framework and baseline NMPC on circular and 8-shaped trajectories under diﬀerent
ﬂight conditions, such as constant angular velocity (CV) and angular acceleration
(CA). At ﬁrst, we validate each module: trajectory generation through diﬀerential
ﬂatness, trajectory smoothing by solving the OCP with full prediction window to
make it dynamically feasible, and tracking performance under nominal conditions.
The original and smoothed reference trajectories along with the actual trajectories
55

## Page 74

Table 3.1: Simulation Parameters.
Parameter
Symbol
Value
Mass
m
6.3 kg
Inertia
diag(0.333, 0.442, 0.580)
kg m2
Kinematic limits
vmax, amax, ωmax
23 m/s, 15 m/s2, 20◦/s
Actuation limits
Tmin:max, τmin:max
0–176.6 N; ±111.9 N m
Attitude bounds
ϕmax, θmax, ψmax
35◦, 35◦, 100◦
PD gains
Kp,ϕ:θ, Kw,ϕ:ψ
12.6, 16.1; 3.68, 4.79, 29.0
ES–EKF noise
σp, σR, σf, στ, σfd, στd
0.005, 0.0025
0.001, 0.001; 20, 5.4
are shown in Fig. 3.2. To evaluate the robustness of both frameworks, we introduce
periodic disturbance forces and torques of the form A sin(ωt), with the parameters
listed in Table 3.2. The lateral force components (±8 N) are approximately 13%
of the vehicle weight, while the vertical component (±23 N) is approximately 37%,
providing realistic gust-load conditions. Under identical disturbances from Table 3.2,
Table 3.2: Sinusoidal Disturbance Parameters.
Axis
Force fd(t)
Torque τ d(t)
Af [N]
ωf [rad/s]
ff [Hz]
Aτ [Nm]
ωτ [rad/s]
fτ [Hz]
x
8
0.2π
0.10
1
0.6π
0.30
y
8
0.2π
0.10
1
0.6π
0.30
z
23
0.2π
0.10
1
0.6π
0.30
56

## Page 75

0
10
20
30
-5
0
5
0
10
20
30
-5
0
5
0
10
20
30
0
2
4
6
0
10
20
30
-4
-2
0
2
4
0
10
20
30
-4
-2
0
2
4
0
10
20
30
0
0.1
0.2
0.3
0.4
0
10
20
30
-20
-15
-10
-5
0
0
10
20
30
-10
-5
0
5
10
0
10
20
30
0
200
400
600
800
0
10
20
30
Time (s)
-20
-10
0
10
20
0
10
20
30
Time (s)
-40
-20
0
20
0
10
20
30
Time (s)
0
10
20
30
40
Figure 3.2: Original and Smoothed Trajectory.
both controllers are evaluated on circular and 8-shape trajectories with increasing
altitude. The results demonstrate that the proposed framework achieves tighter ad-
herence to the commanded path compared to the baseline NMPC when disturbance
estimates are incorporated into the prediction model. Tracking errors for each axis
are plotted on the right-hand side of each ﬁgure.
For the circular trajectory, as
shown in Fig. 3.3a, the baseline NMPC yields RMSE values of (0.122, 0.233, 0.150)
m, while the disturbance-aware NMPC reduces them to (0.031, 0.035, 0.064) m, rep-
57

## Page 76

resenting improvements of 57–85%. Similarly, for the 8-shape trajectory depicted in
Fig. 3.3b, baseline NMPC produces RMSE values of (0.042, 0.060, 0.118) m on the
(x, y, z) axes, while the proposed approach reduces them to (0.019, 0.020, 0.037) m,
achieving 55–69% improvement. The true disturbances, alongside their ES-EKF es-
timates and ±3σ conﬁdence envelopes are shown in Fig. 3.4. The ES-EKF achieves
force RMSE values of (1.07, 1.09, 2.71) N and torque RMSE values of (0.30, 0.28, 0.31)
N·m across (x, y, z) axes, respectively. Over 98.91% of estimation errors, states and
disturbances, remain within the conﬁdence bounds, providing the NMPC with ac-
curate states and disturbances estimates for accurate tracking and proactive com-
pensation. To further validate robustness, we evaluate both ES-EKF and baseline
controllers on a Lissajous trajectory under increased disturbances. Force amplitudes
are increased to 12 N (x,y-axes) and 25 N (z-axis), with frequencies of 0.25 Hz (x,y)
and 0.15 Hz (z), while torque disturbances remain as speciﬁed in Table 3.2. As shown
in Fig. 3.5, the proposed framework reduces RMSE from (0.081, 0.085, 0.178) m to
(0.051, 0.051, 0.074) m across the x, y, and z axes, respectively, achieving 37–58%
improvement. Fig. 3.6 compares RMSE in position tracking, showing that the ES-
EKF-NMPC consistently reduces errors by 37%–85% as compared to standard NMPC
across all trajectory types. We then increase the pose measurement noise tenfold to
σp = 0.05 m and σR = 0.025 rad; the tracking RMSE for CA-Circle increases to 0.29 m
with ES-EKF-NMPC and 0.70 m with baseline NMPC, still representing a 58% reduc-
tion. In terms of computational eﬃciency, the geometric ES-EKF performs a single
state propagation and one SO(3) exponential per time step, rather than the 2n+1
sigma-point propagations required by a UKF [10, 13]. Although the inner-loop PD
control provides basic disturbance rejection, performance is signiﬁcantly enhanced
58

## Page 77

0
2
-4
Z (m)
3D Trajectory
4
4
-2
2
Start
0
X (m)
Y (m)
0
2
End
-2
4
-4
6
Reference
With ES-EKF
Without ES-EKF
0
0.2
0.4
0.6
Error X (m)
0
0.5
1
Error Y (m)
0
5
10
15
20
25
30
Time (s)
-0.2
0
0.2
0.4
Error Z (m)
(a) Circular Trajectory Tracking
-4
-2
Start
X (m)
0
3D Trajectory
2
End
0
1
-1
Y (m)
0
2
4
1
Z (m)
3
4
5
Reference
With ES-EKF
Without ES-EKF
-0.1
-0.05
0
0.05
0.1
Error X (m)
-0.4
-0.3
-0.2
-0.1
0
Error Y (m)
0
5
10
15
20
25
30
Time (s)
-0.2
0
0.2
0.4
Error Z (m)
(b) 8-Shape Trajectory Tracking
Figure 3.3: Trajectory Tracking with and without ES-EKF.
59

## Page 78

-10
-5
0
5
10
-10
-5
0
5
10
3  bounds
Actual
ES-EKF Estimate
-20
-10
0
10
20
0
10
20
30
Time (s)
-4
-2
0
2
x (N·m)
0
10
20
30
Time (s)
-4
-2
0
2
y (N·m)
0
10
20
30
Time (s)
-3
-2
-1
0
1
2
3
z (N·m)
Figure 3.4: True Disturbances vs. ES-EKF Estimation.
0
1
-5
2
3
4
Z (m)
5
End
X (m)
0
3D Trajectory
Start
Y (m)
3
2
5
1
0
-1
-2
-3
Reference
With ES-EKF
Without ES-EKF
-0.2
0
0.2
Error X (m)
-0.2
0
0.2
Error Y (m)
0
5
10
15
20
25
30
Time (s)
-0.2
0
0.2
0.4
0.6
Error Z (m)
Figure 3.5: Lissajous Trajectory Tracking Comparison.
60

## Page 79

0.080
0.046
0.072
0.055
0.103
0.303
0.139
0.154
0.141
0.213
0
0.05
0.1
0.15
0.2
0.25
0.3
0.35
RMSE (m)
With ES-EKF
Without ES-EKF
CA = constant acceleration
CV = constant velocity
Figure 3.6: RMSE comparison with & without ES-EKF.
with the proposed disturbance-aware NMPC framework. These results validate that
the proposed framework provides a robust and eﬀective solution for quadrotor trajec-
tory tracking control under signiﬁcant six-DOF external disturbances, outperforming
traditional methods in both accuracy and disturbance resilience.
Theoretical Stability Considerations
Although we do not provide a formal theoretical proof of closed-loop stability for the
combined ES-EKF-NMPC cascade, our design builds directly on three complemen-
tary, well-established results: (i) NMPC with a terminal cost and terminal set guar-
antees that the optimal value function decreases along closed-loop trajectories, thus
serving as a Lyapunov function [21, 22]; (ii) for systems on SO(3) with autonomous
61

## Page 80

invariant error dynamics, the invariant EKF achieves local asymptotic convergence
of the attitude error; its disturbance-augmented extension provides the same guaran-
tee for disturbance estimates [13, 23]; and (iii) under standard Lipschitz-continuity
and recursive-feasibility assumptions, and provided that both the controller and the
observer are input-to-state stable (ISS) with linear interconnection gains, a nonlinear
small-gain argument guarantees local asymptotic stability of the proposed framework
[24].
3.4
Conclusion
We have presented a disturbance-aware NMPC scheme integrated with a geomet-
ric extended-state EKF on SO(3), which directly incorporates six-DOF disturbance
estimates into the receding-horizon prediction model as known, time-varying in-
puts.
Numerical simulations on various trajectories under periodic six-DOF per-
turbations demonstrate 60% reduction on average in position RMSE compared to a
standard NMPC without disturbance feedback. These results validate the proposed
framework’s ability to achieve robust, constraint-aware trajectory tracking for under-
actuated quadrotors in the presence of external disturbances. Future work will include
deriving closed-loop stability proofs, investigating higher-order disturbance models,
and conducting hardware-in-the-loop as well as real-world ﬂight-test validation.
62

## Page 81

Acknowledgments
This work was supported in part by the National Research Council of Canada, in
part by the Natural Sciences and Engineering Research Council of Canada, and in
part by the Memorial University of Newfoundland.
3.5
Bibliography
[1] Ahsan, M. A., Khan, H. Z. I., Rajput, J., and Riaz, J., 2022, “Active disturbance
rejection control of a quadrotor: A comparative study,” Proc. 19th Int. Bhur-
ban Conf. Applied Sciences and Technology (IBCAST), Islamabad, Pakistan,
pp. 444–450.
[2] Dydek, Z. T., Annaswamy, A. M., and Lavretsky, E., 2013, “Adaptive control of
quadrotor UAVs: A design trade study with ﬂight evaluations,” IEEE Trans.
Control Syst. Technol., 21(4), pp. 1400–1406.
[3] Xu, R., and ¨Ozguner, U., 2006, “Sliding mode control of a quadrotor helicopter,”
Proc. 45th IEEE Conf. Decision and Control (CDC), San Diego, CA, USA,
pp. 4957–4962.
[4] Gomaa, M. A. K., De Silva, O., Mann, G. K. I., and Gosine, R. G., 2023, “Compu-
tationally eﬃcient stability-based nonlinear model predictive control design for
quadrotor aerial vehicles,” IEEE Trans. Control Syst. Technol., 31(2), pp. 615–
630.
63

## Page 82

[5] Limon, D., Calliess, J., and Maciejowski, J. M., 2017, “Learning-based nonlinear
model predictive control,” IFAC-PapersOnLine, 50(1), pp. 7769–7776.
[6] Han, J., 2009, “From PID to active disturbance rejection control,” IEEE Trans.
Ind. Electron., 56(3), pp. 900–906.
[7] Xu, L., Tian, B., Wang, C., Lu, J., Wang, D., Li, Z., and Zong, Q., 2025,
“Fixed-time disturbance observer–based MPC robust trajectory tracking control
of quadrotor,” IEEE/ASME Trans. Mechatron., pp. 1–11.
[8] Derakhshan, R. E., Danesh, M., and Moosavi, H., 2024, “Disturbance observer–
based model predictive control of a coaxial octorotor with variable centre of
gravity,” IET Control Theory Appl., 18(6), pp. 764–783.
[9] Chen, C., Zhang, X., and Peng, X., 2024, “Trajectory tracking control of four-
rotor UAV based on nonlinear extended state observer and model predictive con-
trol in wind disturbance environment,” J. Phys.: Conf. Ser., 2764(1), p. 012075.
[10] McKinnon, C. D., and Schoellig, A. P., 2020, “Estimating and reacting to forces
and torques resulting from common aerodynamic disturbances acting on quadro-
tors,” Robotics Auton. Syst., 123, p. 103314.
[11] Sun, X., Lai, J., Lyu, P., Tian, H., and Shen, Y., 2024, “Fault-tolerant navigation
aided by dynamics model of quadrotors based on federated UKF on Lie group
manifold,” IEEE Sensors J., 24(21), pp. 34828–34842.
[12] He, D., Xu, W., and Zhang, F., 2021, “Kalman ﬁlters on diﬀerentiable mani-
folds,” arXiv:2102.03804.
64

## Page 83

[13] Barrau, A., and Bonnabel, S., 2017, “The invariant extended Kalman ﬁlter as a
stable observer,” IEEE Trans. Autom. Control, 62(4), pp. 1797–1812.
[14] Shan, T., Englot, B., Ratti, C., and Rus, D., 2021, “LVI-SAM: Tightly-coupled
lidar–visual–inertial odometry via smoothing and mapping,” Proc. IEEE Int.
Conf. Robotics Autom., Xi’an, China, pp. 5692–5698.
[15] Pereira, J. C., Leite, V. J. S., and Raﬀo, G. V., 2021, “Nonlinear model predictive
control on SE(3) for quadrotor aggressive maneuvers,” J. Intell. Robot. Syst.,
101(3), p. 62.
[16] Kamel, M., Stastny, T., Alexis, K., and Siegwart, R., 2017, “Model predictive
control for trajectory tracking of unmanned aerial vehicles using Robot Operating
System,” in Robot Operating System (ROS): The Complete Reference (Volume
2), A. Koubaa, ed., Studies in Computational Intelligence, Vol. 707, Springer,
Cham, pp. 3–39.
[17] Mellinger, D., and Kumar, V., 2011, “Minimum snap trajectory generation and
control for quadrotors,” Proc. 2011 IEEE Int. Conf. Robotics Autom. (ICRA),
Shanghai, China, pp. 2520–2525.
[18] Sol`a, J., Deray, J., and Atchuthan, D., 2018, “A micro Lie theory for state
estimation in robotics,” arXiv:1812.01537.
[19] Andersson, J. A. E., Gillis, J., Horn, G., Rawlings, J. B., and Diehl, M., 2019,
“CasADi: A software framework for nonlinear optimization and optimal control,”
Math. Program. Comput., 11(1), pp. 1–36.
65

## Page 84

[20] Bock, H. G., and Plitt, K.-J., 1984, “A multiple shooting algorithm for direct
solution of optimal control problems,” IFAC Proc. Volumes, 17(2), pp. 1603–
1608.
[21] Chen, H., and Allg¨ower, F., 1998, “A quasi-inﬁnite horizon nonlinear model pre-
dictive control scheme with guaranteed stability,” Automatica, 34(10), pp. 1205–
1217.
[22] Mayne, D. Q., Rawlings, J. B., Rao, C. V., and Scokaert, P. O. M., 2000, “Con-
strained model predictive control: Stability and optimality,” Automatica, 36(6),
pp. 789–814.
[23] Coleman, K., Bai, H., and Taylor, C. N., 2021, “Extended invariant-EKF designs
for state and additive disturbance estimation,” Automatica, 125, p. 109464.
[24] Jiang, Z.-P., Mareels, I. M. Y., and Wang, Y., 1996, “A Lyapunov formulation of
the nonlinear small-gain theorem for interconnected ISS systems,” Automatica,
32(8), pp. 1211–1215.
66

## Page 85

Chapter 4
Time-Eﬃcient Trajectory Planning
for UAVs in Safe Convex Corridors
using Diﬀerential Flatness
Constrained Convex Optimization
This chapter has been submitted to IEEE Access Journal.
Abstract
This paper presents a convex optimization-based, time-eﬃcient trajectory-planning
framework for unmanned aerial vehicles (UAVs) operating in obstacle-dense environ-
ments. The pipeline begins with an obstacle map provided in GeoJSON format. Ob-
stacles are decomposed into convex polygons, and a bidirectional Rapidly-exploring
67

## Page 86

Random Tree (RRT) generates a coarse reference path from start to goal. Along this
path, seed selection and convex region generation are performed jointly, producing a
time-eﬃcient sequence of minimally overlapping convex regions. This forms a safe,
connected corridor without requiring a full convex decomposition of the workspace.
Dynamic feasibility is enforced via diﬀerential ﬂatness by expressing system states
and inputs in terms of ﬂat outputs and their derivatives. Admissible phase-space
sets for velocity, acceleration, and jerk are constructed, and convex-hull (polygonal)
approximations of these sets are imposed directly as constraints on the correspond-
ing B´ezier derivative control points. These constraints are combined with corridor
containment and continuity constraints, yielding a single convex program that pro-
duces collision-free, dynamically feasible trajectories without subsequent nonlinear
reﬁnement. We compare the proposed framework against a Graph of Convex Sets
(GCS) planner reﬁned with Kinodynamic Trajectory Optimization (KTO) on three
maps. Under identical constraints, the proposed method achieves approximately 36%
shorter traversal time with comparable path lengths and yields a mean computational
speedup of 17× relative to the baseline. The proposed framework generates ﬁxed-
degree B´ezier trajectories that are globally optimal with respect to the precomputed
corridor and the convexiﬁed dynamic bounds. We also develop an interactive, web-
based trajectory-planning simulator to demonstrate practicality for real-time UAV
operations. Finally, Monte Carlo experiments over 1,001 randomized start–goal con-
ﬁgurations validate robustness, achieving a 99.4% success rate.
68

## Page 87

4.1
Introduction
The proliferation of unmanned aerial vehicles (UAVs) across diverse applications, from
autonomous delivery and infrastructure inspection to surveillance and search-and-
rescue missions, has intensiﬁed the demand for robust, real-time trajectory planning
capabilities [1]. These applications require UAVs to navigate complex environments
with dense obstacles, restricted airspace, and no-ﬂy zones, while adhering to strin-
gent safety and performance constraints imposed by mission requirements, platform
dynamics, and ﬂight control systems. The fundamental challenge is to generate tra-
jectories that simultaneously ensure collision avoidance, satisfy dynamic feasibility
including higher-order derivative constraints, and remain computationally tractable
for online execution. Existing methods typically address only a subset of these re-
quirements, limiting their practical deployment in real-time scenarios for UAVs.
Current approaches to UAV trajectory planning exhibit three key limitations.
First, methods based on global convex decomposition suﬀer from computational scal-
ability issues.
The Graph of Convex Sets (GCS) framework [2] decomposes the
whole workspace into overlapping convex regions using Iterative Regional Inﬂation by
Semideﬁnite programming (IRIS) [3] and formulates trajectory planning as a mixed-
integer convex program (MICP). While GCS can handle complex obstacle environ-
ments, constructing a global convex decomposition of complete large workspaces is
computationally expensive. Furthermore, MICP solve times grow rapidly with the
number of regions and binary variables [4], making real-time replanning challenging
when environments or mission parameters change.
Second, most trajectory plan-
ning methods separate obstacle avoidance from dynamic constraint enforcement, ne-
69

## Page 88

cessitating subsequent reﬁnement stages that compromise computational eﬃciency
or solution quality. For instance, recent work [5] couples GCS with a subsequent
nonlinear optimization, using GCS for geometric path planning followed by local
nonlinear reﬁnement to satisfy higher-order dynamic constraints. While this hybrid
approach improves trajectory quality, the nonconvex reﬁnement stage eliminates con-
vexity guarantees and adds computational overhead. Conversely, diﬀerential-ﬂatness-
based methods [6] eﬃciently generate smooth, dynamically feasible trajectories via
convex optimization by exploiting the ﬂat structure of quadrotor dynamics. How-
ever, these methods have been demonstrated primarily on quadrotors and do not
address the time-eﬃcient generation of corridors within which trajectories are opti-
mized. For ﬁxed-wing UAVs, existing trajectory optimization approaches such as [7]
formulate the problem as a nonconvex program, requiring nonlinear solvers that lack
global convergence guarantees and are sensitive to initialization. Therefore, there re-
mains a need for a computationally eﬃcient corridor-generation method and a convex
trajectory-optimization framework that simultaneously enforces dynamics, continu-
ity, and obstacle-avoidance constraints. Third, comprehensive validation frameworks
that integrate real-world map data, end-to-end pipeline testing, and statistical ro-
bustness analysis remain limited in the literature [8], making it diﬃcult to assess
practical deployment readiness.
To address these limitations, we present an integrated trajectory planning frame-
work for ﬁxed wing UAVs that couples computationally eﬃcient corridor construction
with a uniﬁed convex optimization formulation. Rather than decomposing the entire
workspace, we construct a safe corridor represented by a connected sequence of over-
lapping convex regions, generated greedily along a bidirectional RRT reference path.
70

## Page 89

We exploit diﬀerential ﬂatness to convexify the dynamic constraints and cast the
complete planning problem, including obstacle avoidance, corridor containment, con-
tinuity, and higher order dynamic feasibility, as a single convex program. Speciﬁcally,
we ﬁrst compute a coarse collision free reference path using bidirectional Rapidly ex-
ploring Random Trees (RRT), and then greedily generate overlapping convex polygons
along this path to obtain an obstacle free corridor from start to goal. This corridor is
produced signiﬁcantly faster than Graph of Convex Sets (GCS) methods that rely on
workspace wide, IRIS based convex decomposition. We parameterize the trajectory
using Bezier curves [9] and leverage the diﬀerential ﬂatness property of the ﬁxed wing
model [7] to express all states and inputs as functions of the ﬂat outputs and their
derivatives. By sampling the admissible phase spaces for velocity, acceleration, and
jerk induced by the vehicle dynamics, we compute conservative polytopic inner ap-
proximations, enabling the dynamic constraints to be enforced as linear inequalities
on the Bezier control points. Corridor containment is enforced in the same man-
ner, yielding a single convex quadratic program whose solution is guaranteed to be
collision free and dynamically feasible without subsequent nonlinear reﬁnement. We
validate the framework through comparative experiments against a GCS plus KTO
baseline, demonstrating substantial computational speedups and reduced traversal
times with nearly identical path lengths. We also develop a web based simulator
that integrates real map layers, including buildings, parks, residences, and restricted
zones, to support practical mission planning. Finally, experiments across multiple
maps and Monte Carlo analysis over randomized start to goal pairs demonstrate sta-
tistical robustness, achieving a 99% success rate. Hence, the main contributions of
this work are:
71

## Page 90

 A time eﬃcient greedy corridor generation algorithm that constructs a con-
nected corridor of overlapping convex regions along a bidirectional RRT path,
achieving signiﬁcantly faster computation than workspace wide IRIS based con-
vex decomposition [2].
 A convex trajectory optimization formulation for ﬁxed wing UAVs that ex-
ploits the diﬀerential ﬂatness of the dynamical model [7] and uniﬁes corridor
containment with higher order dynamic constraints in a single convex program,
eliminating the need for nonconvex reﬁnement stages.
 An end to end validation framework that includes a web based simulator with
real map, zone, and obstacle integration for practical mission planning, and
Monte Carlo analysis demonstrating a 99% success rate and robustness across
varied scenarios.
The rest of the paper is organized as follows. Section 4.2 reviews related work. Sec-
tion 4.3 describes the construction of a safe corridor, represented by a connected
sequence of obstacle-free convex regions, from GeoJSON obstacle maps using a bidi-
rectional RRT reference path. Section 4.5 formulates the control-point-based con-
vex trajectory optimization using piecewise B´ezier parameterization, incorporating
corridor-containment constraints, endpoint boundary conditions, inter-segment con-
tinuity, and dynamic-feasibility constraints.
Section 4.6 reports the experimental
results, compares against the GCS+KTO baseline, and summarizes the web-based
simulator and Monte Carlo robustness analysis. Finally, Section 4.7 concludes the
paper and outlines directions for future work.
72

## Page 91

Mission Planning
on GeoJson
Obstacles Convex
Decomposition
Bi-direction RRT
based Path Planning
Set of Minimum
Overlapping Safe
Convex  Corridors
Generation along the
Path
UAV Dynamics
Convexification of
Phase Spaces of
Differentially Flat
Outputs and their
Derivatives
Convex
Trajectory
Optimization
Time Estimation to
Travel Through Each
Corridor
Figure 4.1: Proposed Trajectory Planning Pipeline.
4.2
Related Work
The trajectory planning problem for UAVs has been studied across multiple research
domains. Existing approaches can be grouped into path planning methods, convex de-
composition strategies, trajectory optimization techniques, diﬀerential ﬂatness-based
parameterization, and hybrid methods combining convex decomposition with nonlin-
ear optimization.
Traditional path planning methods focus on geometric collision avoidance without
explicitly considering dynamic feasibility. Graph-search algorithms such as Dijkstra’s
algorithm [10] and A* [11] operate on discretized conﬁguration spaces [12], guarantee-
ing solutions within the discretized domain but producing piecewise-linear paths that
lack smoothness and scale poorly to high-dimensional spaces. Sampling-based plan-
73

## Page 92

ners, including Probabilistic Roadmaps (PRM) [13] and Rapidly-exploring Random
Trees (RRT) [14, 15], oﬀer improved scalability through probabilistic exploration, with
RRT* [16] providing asymptotic optimality at increased computational cost. How-
ever, these methods generate paths requiring substantial post-processing to achieve
dynamic feasibility and smoothness. Kinodynamic planning [17] addresses this by
augmenting the state space with velocity and higher-order derivatives to directly gen-
erate dynamically feasible trajectories, though at signiﬁcantly higher computational
complexity.
Trajectory optimization methods directly formulate the planning problem as an
optimal control problem over continuous state and control trajectories. Classical ap-
proaches [18], such as direct collocation [19], transcribe the continuous optimal control
problem into ﬁnite-dimensional nonlinear programs (NLPs). While these formulations
can explicitly enforce dynamic constraints, the resulting optimization problems are
generally nonconvex and computationally intensive, requiring good initial guesses for
convergence [7]. To address convergence challenges, gradient-based trajectory opti-
mization methods such as CHOMP (Covariant Hamiltonian Optimization for Motion
Planning) [20] iteratively reﬁne trajectories by optimizing smoothness and obstacle
cost functionals. However, these methods remain sensitive to initialization and often
converge to local minima. Stochastic approaches like STOMP [21] were developed to
overcome such local-minima failures, yet they introduce their own sensitivity to ini-
tialization and noise scaling, imposing practical computational and reliability limits.
An alternative approach uses sequential convex optimization [22], which addresses
nonconvexity through successive convexiﬁcation by solving sequences of convex sub-
problems. While this improves convergence reliability over gradient-based methods, it
74

## Page 93

typically requires multiple iterations and may not guarantee global optimality. More
generally, convex optimization formulations and techniques [23, 24] use tractable con-
vex surrogates or relaxations with global optimality guarantees; when the relaxation
is tight, the solution is almost optimal for the original problem.
Diﬀerential ﬂatness theory provides a mathematical framework for trajectory pa-
rameterization that can simplify trajectory optimization in underactuated systems.
For diﬀerentially ﬂat systems, all states and control inputs can be expressed as al-
gebraic functions of ﬂat outputs and their derivatives [25]. This property enables
polynomial trajectory parameterization, signiﬁcantly simplifying optimization by re-
ducing decision variable dimensionality. This approach has proven successful in aerial
robotics [26]; for example, minimum-snap trajectory generation [6] optimizes poly-
nomial trajectories for smoothness while satisfying boundary conditions.
Polyno-
mial based curve parameterizations, such as B´ezier representation, oﬀer attractive
computational properties, including convex hull containment and linear relationships
between control points and trajectory derivatives [27, 9, 28], facilitating eﬃcient opti-
mization of smooth trajectories. While diﬀerential ﬂatness methods have been demon-
strated primarily on quadrotors [6], applications to ﬁxed-wing UAVs are fewer. For
ﬁxed-wing UAVs, existing trajectory optimization approaches such as [7] formulate
the problem as a nonconvex program, requiring nonlinear solvers that lack global con-
vergence guarantees and are sensitive to initialization. Furthermore, most ﬂatness-
based methods either assume obstacle-free environments or rely on precomputed safe
corridors (e.g., [6]), without addressing rapid corridor generation.
Convex decomposition strategies address the fundamental challenge of obstacle
avoidance in trajectory optimization, which stems from the nonconvex nature of
75

## Page 94

obstacle-cluttered environments. Recent advances in convex decomposition methods
address this by partitioning the free space into overlapping convex regions. The GCS
framework [2] represents a signiﬁcant advancement in this direction. GCS decom-
poses the free space into overlapping convex regions using IRIS [3] and constructs a
roadmap over these regions, formulating the trajectory planning problem as a MICP.
This approach optimizes discrete region selections together with continuous trajectory
parameters, often yielding shorter trajectories and faster online solutions compared
to sampling-based methods. However, GCS faces two key limitations. First, con-
structing a global convex decomposition of the entire workspace using IRIS is com-
putationally expensive, particularly for large environments with dense obstacles. The
IRIS algorithm iteratively inﬂates convex regions while avoiding obstacles through
semideﬁnite programming, and applying this across the entire workspace requires
substantial computation. Second, MICP solve times grow with the number of regions
and binary decision variables [4], limiting scalability and making real-time replan-
ning challenging when environments or mission parameters change.
Additionally,
the standard GCS approach can only incorporate velocity constraint, and generates
piecewise-polynomial paths that may exhibit discontinuities in higher-order deriva-
tives, potentially violating dynamic constraints.
To address the limitations of convex decomposition and trajectory optimization
methods, recent work [5] couples GCS with local nonlinear trajectory optimization
stages. This hybrid pipeline uses GCS for global path planning followed by local non-
linear reﬁnement to satisfy higher-order dynamic constraints. The GCS stage handles
obstacle avoidance through convex decomposition and MICP, while the second non-
linear reﬁnement stage reﬁnes the trajectory to satisfy dynamic feasibility. While
76

## Page 95

this hybrid approach improves trajectory quality compared to GCS alone, it inherits
the computational expense of global IRIS-based workspace decomposition from GCS.
Furthermore, the nonconvex reﬁnement stage also eliminates global optimality guar-
antees. The separation of obstacle avoidance and dynamic constraint enforcement
into two stages compromises either computational eﬃciency or solution quality.
Hence, existing approaches trade oﬀsolution quality, computational eﬃciency,
and optimality guarantees. Methods with strong guarantees rely on workspace-wide
convex decompositions and MICP, whereas faster pipelines either decouple geome-
try from dynamics or introduce nonconvex reﬁnement that forfeits guarantees. In
contrast, we build a single connected corridor by greedily placing overlapping con-
vex regions along a bidirectional-RRT path and use diﬀerential ﬂatness to convexify
ﬁxed-wing dynamics. The resulting convex program over B´ezier control points en-
forces corridor containment, continuity, and higher-order dynamic feasibility in one
solve, eliminating subsequent nonlinear reﬁnement while retaining global optimality
for the convexiﬁed problem given the precomputed corridor.
4.3
Safe Connected Convex Corridor Generation
This section presents the mathematical framework for constructing a connected con-
vex corridor from mission planning data provided in GeoJSON, a JSON based format
for geographic features. The input includes polygonal obstacle boundaries and start
and goal coordinates in latitude and longitude. These data then undergo coordinate
transformation, obstacle decomposition, path planning, and convex region construc-
tion.
77

## Page 96

Figure 4.2: Mission Planning
4.3.1
Geographic Data Processing and Obstacle Decomposi-
tion
The corridor generation begins with obstacle data provided in GeoJSON format us-
ing geographic coordinates. These coordinates are transformed to a local Cartesian
system using equirectangular projection, converting latitude-longitude pairs to x-y
coordinates while preserving local geometric relationships for subsequent processing.
The obstacles are initially mapped as polygons in GeoJSON format, which may be
nonconvex in shape, as shown in Fig. 4.2. Since the proposed pipeline operates on con-
vex obstacle representations, any nonconvex obstacle must ﬁrst be decomposed into
convex polygons. Hence, each obstacle is triangulated and then iteratively merged to
reduce the number of regions [29]. Speciﬁcally, adjacent triangles are merged when-
78

## Page 97

Figure 4.3: Convex Decomposition
ever their union remains convex, and the merging proceeds until no further convex
combinations are possible. Polygons that are fully contained within other polygons
are removed to avoid redundant regions. The resulting map with convexiﬁed obsta-
cles is shown in Fig. 4.3. This step is implemented in a generic manner and also
converts curved primitives (e.g., circles) into polygonal obstacles by sampling points
along the boundary and computing the convex hull. The convexiﬁcation process is
demonstrated across diverse obstacle vector maps in Fig. 4.4.
4.3.2
Collision-Free Path Generation via Bidirectional RRT
With convex obstacles and workspace boundaries established, we generate a collision-
free path connecting start ps and goal pg points using bidirectional RRT. Two trees
Ts and Tg expand alternately through multimodal sampling that balances exploration
79

## Page 98

(a) Case 1 org
(b) Case 1 conv
(c) Case 2 org
(d) Case 2 conv
(e) Case 3 org
(f) Case 3 conv
(g) Case 4 org
(h) Case 4 conv
(i) Case 5 org
(j) Case 5 conv
(k) Case 6 org
(l) Case 6 conv
Figure 4.4: Convexiﬁcation of nonconvex obstacles mapped by the user. “Org” de-
notes the original obstacle vector map, and “Conv” denotes the convexiﬁed obstacle
vector map.
80

## Page 99

with goal-directed search as:
pr =

















Uniform(Vopposite)
prob. 0.10,
ps + α(pg −ps) + ξ (clipped to W)
prob. 0.36,
Uniform(W)
prob. 0.54,
(4.1)
where α ∼Uniform(0, 1) provides start-goal interpolation, ξ ∼N(0, δ2I) introduces
controlled perturbation with identity matrix I, Vopposite denotes the vertex set of the
inactive tree, and W represents the workspace. The three modes respectively accel-
erate tree connection, apply goal-biased exploration, and ensure uniform workspace
coverage. For each sample pr, we identify the nearest vertex and extend the active
tree as:
pnear = arg
min
p∈Vactive∥p −pr∥2,
(4.2)
pnew = pnear + δ
pr −pnear
∥pr −pnear∥2
,
(4.3)
where δ denotes the step-size parameter and Vactive is the vertex set of the currently
expanding tree. The candidate is skipped if ∥pr−pnear∥2 is numerically negligible. The
edge (pnear, pnew) is accepted only if pnew lies outside all obstacles and the segment
(pnear, pnew) is collision-free. The algorithm terminates when the two trees can be
connected by selecting the nearest vertex in the opposite tree within distance 2δ and
verifying a collision-free connecting segment, yielding a path P = {p1, p2, . . . , pN}.
If bidirectional expansion fails, the planner reverts to unidirectional RRT from ps
toward pg. Finally, the path used for corridor construction is obtained by running
Dijkstra’s algorithm over the constructed roadmap graph. The resulting path for the
convexiﬁed obstacle vector map in Fig. 4.3 is shown in Fig. 4.5 and serves as the basis
81

## Page 100

Figure 4.5: Bidirectional RRT Generated Path.
for subsequent corridor construction.
4.3.3
Seed Point Selection
To generate a small number of regions for a connected corridor from start to goal
point, we employ a greedy seed-point selection algorithm along the planned path
P = {p1, . . . , pN}. Beginning with the start point p1 as the ﬁrst seed, we generate
a convex region L1 and traverse the path sequentially. When we encounter the ﬁrst
path point that lies outside the current region, we use it as the next seed point. This
process repeats until the goal is covered. Mathematically, for region Lk centered at
seed pik, the exit point is:
iexit = min{j > ik : pj /∈Lk}.
(4.4)
82

## Page 101

Now, the point piexit becomes seed pik+1 for the next region Lk+1. We determine how
far the new region extends along the path:
ifurthest = max{j ≥iexit : pj ∈Lk+1}.
(4.5)
When region generation succeeds, this procedure ensures that each path point is
covered by at least one region:
∀pi ∈P, ∃Lj : pi ∈Lj,
(4.6)
while generating new regions only when necessary along the path.
4.3.4
Separating Hyperplane Construction
For each seed point d ∈{pi1, pi2, . . . , piK}, we construct a convex region by generating
separating hyperplanes that exclude obstacles while expanding the feasible region
around the seed. To ensure numerical stability and uniform scaling, a scaling matrix
C = σI is introduced, where σ controls the region’s characteristic size. Obstacles are
processed iteratively by proximity to the seed point as:
O∗= arg min
O∈Orem min
v∈O ∥v −d∥2
(4.7)
where v represents vertices of obstacles. For the selected obstacle O∗= {v1, . . . , vm},
we ﬁnd the closest point on the obstacle boundary to the seed by transforming the
obstacle vertices to a normalized coordinate system via ˜vk = C−1(vk −d) and then
solving the following minimization problem:
min
˜x,w ∥˜x∥2
2
(4.8)
s.t. ˜x =
m
X
k=1
wk ˜vk,
m
X
k=1
wk = 1,
wk ≥0.
(4.9)
83

## Page 102

The solution ˜x∗corresponds to the closest point x∗= C ˜x∗+d in original coordinates.
This deﬁnes a separating hyperplane with normal vector and oﬀset:
a = 2 C−1C−T(x∗−d),
b = aTx∗.
(4.10)
The resulting halfspace aTx ≤b contains the seed-side free space and excludes the
obstacle. Any remaining obstacle Oj ∈Orem for which all vertices v ∈Oj satisfy
aTv ≥b lies entirely on the obstacle side and is excluded from further processing. This
iterative separation continues until all obstacles are processed, yielding hyperplanes
(A, b) that deﬁne an expanded convex region around seed d.
4.3.5
Convex Region Formation
The separating hyperplanes {(ai, bi)}m
i=1 deﬁne a convex region by intersecting half-
spaces:
L =
m
\
i=1
Hi,
Hi = {x ∈R2 : a⊤
i x ≤bi}.
(4.11)
We extract the vertices V (L) = {vj} from the half-space intersection and sort them
counter-clockwise about the seed d using angular coordinates θj = atan2(vj,y −
dy, vj,x −dx).
For robustness, we attempt region construction over a predeﬁned
set of scaling coeﬃcients σ (with C = σI), requiring the seed to lie within the result-
ing region (d ∈L) and at least three vertices (|V (L)| ≥3). If a candidate coeﬃcient
fails to produce a valid region, we retry with the next coeﬃcient until a valid region
is obtained. Combined with the greedy seed selection along the path, the resulting
regions form a collision-free convex corridor suitable for subsequent trajectory opti-
mization. The corridor of overlapping convex regions generated for the path obtained
in Fig. 4.5 is shown in Fig. 4.6.
84

## Page 103

Figure 4.6: Path Planning and Safe Connected Corridors.
4.4
Convexiﬁcation of Nonconvex Dynamical Con-
straints
We adapt a ﬁxed-wing UAV dynamic model from [7] under the coordinated-turn
assumption with zero sideslip.
The 7-dimensional state vector is deﬁned as X =

x, y, v, a, ψ, ϕ, ω
T
, and the control vector is U =

j, α
T
, where v is ground speed,
a = ˙v is tangential (along-track) acceleration, j = ˙a is tangential jerk, ψ is heading,
ϕ is bank angle, ω = ˙ϕ is bank rate, and α = ˙ω is bank angular acceleration. The
85

## Page 104

dynamics are:


˙x
˙y
˙v
˙a
˙ψ
˙ϕ
˙ω


=


v cos ψ
v sin ψ
a
j
g tan ϕ
v
ω
α


.
(4.12)
4.4.1
Diﬀerential Flatness
To establish diﬀerential ﬂatness, we choose the ﬂat outputs as xf = x and yf = y. All
states and controls can then be expressed in terms of these outputs and their time
derivatives (assuming v > 0):
x = xf,
y = yf,
v =
q
˙x 2
f + ˙y 2
f ,
ψ = atan2
˙yf, ˙xf

,
a = ˙xf ¨xf + ˙yf ¨yf
v
,
ϕ = arctan(η),
ω = ˙ϕ =
˙η
1 + η2,
(4.13)
where:
η = ˙xf ¨yf −˙yf ¨xf
g v
.
(4.14)
The jerk is the time derivative of a, deﬁned as:
j = ˙a = d
dt

˙xf ¨xf + ˙yf ¨yf
q
˙x2
f + ˙y2
f

,
(4.15)
and the bank angular acceleration is deﬁned as:
α = ˙ω.
(4.16)
86

## Page 105

4.4.2
Derivatives of Flat Outputs
The derivatives of the ﬂat outputs are used to construct admissible phase-space con-
straints. The ﬁrst derivatives (inertial velocity components) are:
˙xf = v cos ψ,
(4.17)
˙yf = v sin ψ.
(4.18)
The second derivatives (inertial acceleration components), which combine tangential
acceleration a = ˙v with the turn-induced lateral component governed by ϕ, are:
¨xf = a cos ψ −g sin ψ tan ϕ,
(4.19)
¨yf = a sin ψ + g cos ψ tan ϕ.
(4.20)
The third derivatives (inertial jerk components), which include the tangential jerk
j = ˙a and additional terms arising from the time variation of ψ and ϕ, are:
...x f = j cos ψ −a sin ψ · g tan ϕ
v
−g2 cos ψ tan2 ϕ
v
−g sin ψ sec2 ϕ · ω,
(4.21)
...y f = j sin ψ + a cos ψ · g tan ϕ
v
−g2 sin ψ tan2 ϕ
v
+ g cos ψ sec2 ϕ · ω.
(4.22)
4.4.3
Phase Space Generation and Boundary Approximation
The phase space for derivatives of the ﬂat outputs is generated by sampling v, ϕ, ψ,
ω, a, and j within predeﬁned ranges from Table 4.1. Using these sampled values,
we compute the derivatives of the ﬂat outputs using the relations from Sec. 4.4.2,
including velocity ( ˙xf, ˙yf), acceleration (¨xf, ¨yf), and jerk ( ...x f, ...y f). A simple convex
87

## Page 106

Figure 4.7: Phase Spaces and Convex Hulls.
relaxation of each nonlinear phase space boundary is obtained by computing the
convex hull of the sampled derivative points, as illustrated in Fig. 4.7. These convex
polygons can then be imposed as linear inequality constraints on derivatives of the
B´ezier control points during trajectory optimization. As an alternative, particularly
for nonconvex and irregularly shaped phase spaces, the IRIS algorithm [3] can be used
to compute large convex regions within the sampled phase-space boundary. Note that
the convex polygons corresponding to the phase spaces (¨xf, ¨yf) and ( ...x f, ...y f) bound
the inertial acceleration and jerk vectors. They limit the vector magnitude in the
inertial frame but do not directly enforce separate tangential and lateral bounds,
since the inertial components depend nonlinearly on ψ, ϕ, v, and ω. Consequently,
the resulting convex sets are typically less restrictive than bounds inferred from the
scalar limits a, j ∈[−1, 1] in Table 4.1.
88

## Page 107

Table 4.1: Parameter Ranges for Phase Space Generation
Parameter
Range
Units
Velocity (v)
0.5 to 50
m/s
Roll Angle (ϕ)
−15◦to 15◦
Degrees
Yaw Angle (ψ)
−180◦to 180◦
Degrees
Roll Rate (ω)
−15◦/s to 15◦/s
Degrees/second
Acceleration (a)
−1 to 1
m/s2
Jerk (j)
−1 to 1
m/s3
Note: These ranges were used to generate the phase space points.
4.5
Trajectory Optimization
The trajectory optimization stage computes a collision-free trajectory that lies within
the connected convex corridor, while satisfying boundary, continuity, and dynamic
feasibility constraints. The formulation is implemented in the Drake Mathematical
Program framework [30] and solved using the Clarabel solver. The decision variables
are the control points of piecewise B´ezier curves representing the vehicle position and
its time derivatives up to snap. This parameterization enables spatial containment to
be enforced through convex corridor constraints and enables derivative relationships
to be imposed through linear equality constraints.
89

## Page 108

4.5.1
B´ezier Control Point Parameterization
The trajectory within each corridor region is represented by a B´ezier curve of degree
n in R2. Let L denote the number of corridor regions. We introduce separate sets of
control points for position and for successive derivatives as:
x ∈RL×(n+1)×2,
v ∈RL×n×2,
a ∈RL×(n−1)×2,
j ∈RL×(n−2)×2,
s ∈RL×(n−3)×2,
where x denotes the position control points and v, a, j, and s denote the control
points for velocity, acceleration, jerk, and snap, respectively. These control points
constitute the optimization decision variables.
4.5.2
Initial Time Allocation
Although time does not explicitly appear in the convex formulation (since we ﬁx seg-
ment durations when optimizing), we need an initial guess for the timing T1, T2, . . . , TL
for each segment. Each segment i is assigned an initial traversal time Ti based on the
corridor path length di from the bidirectional RRT-generated path and the dynamic
limits. If di is suﬃcient for sustained cruise at Vmax, then time can be calculated
as Ti =
di
Vmax. If the segment is too short to reach Vmax, a trapezoidal or triangular
velocity proﬁle is computed using maximum allowable acceleration, deceleration, and
jerk. The mean velocity from this proﬁle deﬁnes Ti. The total initial trajectory time
is the sum of the segment times, scaled by a ﬁxed safety margin to ensure feasibility.
90

## Page 109

4.5.3
Corridor Containment
To ensure the trajectory remains inside the safe corridor (and thus avoids obstacles),
we impose containment constraints on the position B´ezier control points. Let the i-th
convex corridor be:
Li = {x ∈R2 | Aix ≤bi}.
(4.23)
Using the convex-hull property of B´ezier curves, enforcing all position control points
inside Li is suﬃcient to guarantee that the entire B´ezier segment lies in Li. Therefore,
each position control point x⟨0⟩
i,j satisﬁes:
Ai x⟨0⟩
i,j ≤bi,
j = 0, . . . , n.
(4.24)
4.5.4
Boundary Conditions
To ensure that the trajectory matches the speciﬁed initial and terminal conditions
for position and selected derivatives, we constrain the endpoint B´ezier control points.
For derivative order r, the constraints are imposed as:
x⟨r⟩
1, 0 = x⟨r⟩
start,
x⟨r⟩
L, n−r = x⟨r⟩
end,
(4.25)
where x⟨r⟩
i,k denotes the k-th control point of the r-th derivative curve for segment i.
4.5.5
Derivative Relations
Higher-order derivative control points are obtained from lower-order control points
through linear diﬀerence relations scaled by the segment duration Ti and the B´ezier
degree. Let segment i have degree n and duration Ti > 0, with position control points
91

## Page 110

{x⟨0⟩
i,0 , . . . , x⟨0⟩
i,n}. For derivative order r ∈{1, . . . , n}, we deﬁne the corresponding step
size as:
∆t(r)
i
=
Ti
n −r + 1.
(4.26)
Then, for any control-point index k ∈{0, . . . , n −r}, the derivative control points
satisfy:
x⟨r⟩
i,k =
1
∆t(r)
i
x⟨r−1⟩
i,k+1 −x⟨r−1⟩
i,k

.
(4.27)
These equalities are imposed directly in the optimization and preserve convexity since
they are linear in the decision variables.
4.5.6
Inter-Segment Continuity
We enforce continuity at the junctions of consecutive segments so that the piecewise
trajectory and its derivatives match across corridor boundaries. Let R denote the
highest derivative order enforced (with R ≤n−1). In this work we enforce continuity
up to snap (i.e., R = 4 for n ≥5). For segments i and i+1, continuity is imposed
by equating the endpoint control point of segment i to the startpoint control point of
segment i+1 for each derivative order:
x⟨r⟩
i, n−r = x⟨r⟩
i+1, 0,
r = 0, . . . , R.
(4.28)
Since the derivative control points x⟨r⟩
i,k are deﬁned with the segment duration Ti
through the derivative relations, these equalities enforce continuity in the physical
derivatives even when Ti varies across segments.
92

## Page 111

4.5.7
Dynamic Feasibility Constraints
The convex phase-space bounds obtained in Subsection 4.4.3 are used to constrain
the derivative control points for velocity, acceleration, and jerk. For derivative order
r ∈{1, 2, 3}, let
Pr = {y ∈R2 | Ary + br ≤0}
(4.29)
denote the convex polygon describing the admissible set in the inertial frame. Then,
for every segment i and every valid control-point index k, we enforce:
Ar x⟨r⟩
i,k + br ≤0,
∀i, k,
(4.30)
thereby bounding the inertial velocity (r = 1), acceleration (r = 2), and jerk (r =
3) vectors throughout the trajectory. Note that these constraints limit the inertial
derivative vectors and do not directly impose separate tangential and lateral bounds,
since the tangential/lateral decomposition depends nonlinearly on ψ, ϕ, v, and ω.
4.5.8
Objective Function
Since the exact B´ezier arc length is nonconvex [31], we minimize a convex surrogate
based on the squared distances between consecutive position control points.
Let
{x⟨0⟩
q }L(n+1)−1
q=0
denote the position control points obtained by stacking x⟨0⟩
i,j in segment
order (i.e., q = i(n + 1) + j with i = 0, . . . , L −1 and j = 0, . . . , n). The objective is
deﬁned as:
min
L(n+1)−2
X
q=0
x⟨0⟩
q+1 −x⟨0⟩
q

2
2 .
(4.31)
This quadratic objective is convex and encourages shorter, smoother trajectories with-
out introducing nonconvexity.
93

## Page 112

4.5.9
Trajectory Reconstruction
Once the optimization is solved, we obtain the optimal B´ezier control points for posi-
tion and its derivatives. The piecewise trajectory is then reconstructed by evaluating
each B´ezier segment. For derivative order r ∈{0, 1, 2, 3, 4}, the i-th segment is
B(r)
i (t) =
n−r
X
j=0
n −r
j

(1 −t) n−r−jt j x⟨r⟩
i,j ,
t ∈[0, 1],
(4.32)
where x⟨r⟩
i,j denotes the j-th control point of the r-th derivative curve for segment i.
Concatenating the L segments yields a global trajectory for each derivative order r,
with continuity guaranteed by the inter-segment constraints.
4.6
Results and Discussion
4.6.1
Comparison with GCS + KTO Baseline
We evaluate the proposed pipeline against a GCS planner reﬁned with KTO under
identical conditions and dynamic constraints. Both pipelines were executed on Google
Colab to ensure computational consistency. The baseline methodology generates IRIS
regions, constructs a connectivity graph, solves a shortest path problem within the
GCS, and reﬁnes the resulting trajectory using KTO with SNOPT solver [32]. In
contrast, the proposed approach generates a bidirectional RRT path, constructs a
minimal set of overlapping convex polygons along the path, and solves a single con-
vex program over B´ezier control points using the Clarabel solver. Both pipelines share
the same obstacle convex-decomposition step. For the proposed method, the B´ezier
curve degree is ﬁxed at 20 in all cases. For the baseline method, which uses KTO
94

## Page 113

200
400
600
800
1000
1200
100
200
300
400
500
600
700
800
900
1000
1100
Y (m)
0
200
400
600
800
1000
1200
1400
1600
X (m)
200
400
600
800
1000
Obstacles
Safe Convex Regions
RRT Tree
RRT Nodes
RRT Path
RRT Path Seed Points
Optimized Trajectory
Start
Goal
Bezier Control Points
200
400
600
800
200
400
600
800
1000
1200
(a) Proposed pipeline planning results.
0
200
400
600
800
1000
1200
0
200
400
600
800
1000
Y (m)
0
200
400
600
800
1000
1200
1400
1600
1800
X (m)
0
200
400
600
800
1000
Obstacles
Safe Regions
Region Connectivity
KTO Optimized Trajectory
GCS Path
Start
Goal
KTO Control Points
0
200
400
600
800
0
200
400
600
800
1000
1200
(b) Baseline pipeline planning results.
Figure 4.8: Comparison of proposed and baseline pipeline planning results.
with B-splines, we set the spline order to 5, for all cases. The proposed methodology
achieves planning times of 0.871 s, 0.826 s, and 0.755 s for Cases 1–3, respectively,
whereas the baseline requires 15.814 s, 20.648 s, and 6.422 s for the corresponding
cases, demonstrating a mean computational acceleration factor of 17× across all cases.
In the baseline, IRIS region generation plus graph construction accounts for most of
the runtime. While in the proposed pipeline, corridor generation is the dominant
stage, but much more computationally eﬃcient than IRIS, followed by RRT seeding
95

## Page 114

0
20
40
Time (s)
0
10
20
30
40
50
Airspeed (m/s)
Airspeed
0
20
40
Time (s)
0
2
4
6
8
Magnitude
Acceleration & Jerk
jaj (m/s2)
jjj (m/s3)
jaj limit
jjj limit
0
20
40
Time (s)
-15
-10
-5
0
5
10
15
Angle (/) / Rate (/ s!1)
Roll Angle & Rate
? (/)
_? (/ s!1)
(a) Case 1 - Proposed
0
50
100
Time (s)
0
10
20
30
40
50
Airspeed (m/s)
Airspeed
0
50
100
Time (s)
0
2
4
6
8
Magnitude
Acceleration & Jerk
jaj (m/s2)
jjj (m/s3)
jaj limit
jjj limit
0
50
100
Time (s)
-15
-10
-5
0
5
10
15
Angle (/) / Rate (/ s!1)
Roll Angle & Rate
? (/)
_? (/ s!1)
(b) Case 1 - Baseline
0
20
40
60
80
Time (s)
0
10
20
30
40
50
Airspeed (m/s)
Airspeed
0
20
40
60
80
Time (s)
0
2
4
6
8
Magnitude
Acceleration & Jerk
jaj (m/s2)
jjj (m/s3)
jaj limit
jjj limit
0
20
40
60
80
Time (s)
-15
-10
-5
0
5
10
15
Angle (/) / Rate (/ s!1)
Roll Angle & Rate
? (/)
_? (/ s!1)
(c) Case 2 - Proposed
0
50
100
Time (s)
0
10
20
30
40
50
Airspeed (m/s)
Airspeed
0
50
100
Time (s)
0
2
4
6
8
Magnitude
Acceleration & Jerk
jaj (m/s2)
jjj (m/s3)
jaj limit
jjj limit
0
50
100
Time (s)
-15
-10
-5
0
5
10
15
Angle (/) / Rate (/ s!1)
Roll Angle & Rate
? (/)
_? (/ s!1)
(d) Case 2 - Baseline
0
20
40
60
Time (s)
0
10
20
30
40
50
Airspeed (m/s)
Airspeed
0
20
40
60
Time (s)
0
2
4
6
8
Magnitude
Acceleration & Jerk
jaj (m/s2)
jjj (m/s3)
jaj limit
jjj limit
0
20
40
60
Time (s)
-15
-10
-5
0
5
10
15
Angle (/) / Rate (/ s!1)
Roll Angle & Rate
? (/)
_? (/ s!1)
(e) Case 3 - Proposed
0
20
40
60
80
Time (s)
0
10
20
30
40
50
Airspeed (m/s)
Airspeed
0
20
40
60
80
Time (s)
0
2
4
6
8
Magnitude
Acceleration & Jerk
jaj (m/s2)
jjj (m/s3)
jaj limit
jjj limit
0
20
40
60
80
Time (s)
-15
-10
-5
0
5
10
15
Angle (/) / Rate (/ s!1)
Roll Angle & Rate
? (/)
_? (/ s!1)
(f) Case 3 - Baseline
Figure 4.9: Kinematics proﬁles for all three maps. Left column: proposed method;
right column: GCS+KTO baseline.
Proposed Method
GCS + KTO Pipeline
Case
RRT Path
Corridors Generation
Trajectory Optimization
Total Time
IRIS Generation
Connection Graph
GCS
KTO
Total Time
Case 1
0.175
0.440
0.256
0.871
8.953
1.562
5.275
0.024
15.814
Case 2
0.163
0.520
0.143
0.826
9.673
2.175
8.740
0.060
20.648
Case 3
0.026
0.521
0.208
0.755
4.437
0.803
1.138
0.044
6.422
Table 4.2: Stage-wise timing comparison for proposed and baseline frameworks.
and the optimization. Detailed stage-wise computational runtime are presented in
Table. 4.2. The initial traversal time allocation is computed outside the optimization
using a physics-based estimate that respects dynamics with a safety margin, since
96

## Page 115

embedding time as a decision variable directly into the optimization would render the
trajectory optimization problem nonconvex. The outer loop then iteratively reduces
the corridor times and re-solves the optimization until no further reduction is feasi-
ble. Since the objective of the trajectory optimization is to minimize the path length,
the time is reduced to the extent where it gives the shortest path, rather than the
minimum possible time, as the fastest path may not be the shortest path. Now, for
fair comparison, we added an iteratively reﬁned upper time bound to the time cost
for the KTO step, which, if left unbounded, yields even larger traversal times. The
path lengths and traversal times for all three maps for both approaches are tabulated
in Table 4.3, showing an average traversal-time reduction of 36% relative to the base-
line. The optimization results for both frameworks are presented in Figs. 4.8a and
Proposed Method
GCS + KTO Pipeline
Case
Path Length (m)
Traversal Time (s)
Path Length (m)
Traversal Time (s)
Case 1
679.207
58.000
679.600
100.577
Case 2
1547.342
90.000
1512.430
133.000
Case 3
845.724
65.000
845.674
98.000
Table 4.3: Path length and traversal time comparison.
4.8b, which depict each environment with obstacles, safe corridors, and the ﬁnal tra-
jectories. Since Drake’s KinematicTrajectoryOptimization returns only the position
B-spline control points and derivative evaluations, and does not expose the control
points for velocity, acceleration, or jerk, we only plot the derivative control points for
97

## Page 116

the proposed framework. The proposed framework constrains the control points di-
rectly x, v, a, j, therefore the B´ezier trajectory for each derivative also remains inside
its corresponding convex hull as shown in Fig. 4.10. Both pipelines keep airspeed,
acceleration, jerk, roll angle and rate within bounds as shown in Fig. 4.9. As depicted
in the ﬁgures and Table 4.3, the proposed pipeline generates dynamically feasible and
globally optimal solution to the convex program within the constructed corridor, with
shorter traversal and computational times compared to the baseline pipeline, while
achieving nearly identical path lengths. In contrast, the baseline pipeline results in
longer traversal times and signiﬁcantly higher computational times.
Though the GCS+KTO framework is computationally expensive, GCS yields the
shortest path over the graph of convex sets. The proposed framework is computa-
tionally eﬃcient but does not guarantee the shortest path in the environment, since
the corridor of overlapping convex regions is restricted to the initial bidirectional
RRT path. Bidirectional RRT can be replaced with RRT*, which provides an asymp-
totically optimal path, but RRT* is more computationally expensive, as shown in
Fig. 4.11. Since we aim for time-eﬃcient corridor generation, we prefer bidirectional
RRT-based sampling. In our comparison studies (Table 4.3), given suﬃcient itera-
tions, the bidirectional RRT-based proposed pipeline results in path lengths that are
close to those obtained by the baseline method.
98

## Page 117

-40 -20
0
20
40
vx [m s!1]
-40
-20
0
20
40
vy [m s!1]
Velocity
Corridor
Trajectory
Control Pts
-2
0
2
ax [m s!2]
-2
-1
0
1
2
ay [m s!2]
Acceleration
-5
0
5
jx [m s!3]
-5
0
5
jy [m s!3]
Jerk
(a) Case 1
-40 -20
0
20
40
vx [m s!1]
-40
-20
0
20
40
vy [m s!1]
Velocity
Corridor
Trajectory
Control Pts
-2
0
2
ax [m s!2]
-2
-1
0
1
2
ay [m s!2]
Acceleration
-5
0
5
jx [m s!3]
-5
0
5
jy [m s!3]
Jerk
(b) Case 2
-40 -20
0
20
40
vx [m s!1]
-40
-20
0
20
40
vy [m s!1]
Velocity
Corridor
Trajectory
Control Pts
-2
0
2
ax [m s!2]
-2
-1
0
1
2
ay [m s!2]
Acceleration
-5
0
5
jx [m s!3]
-5
0
5
jy [m s!3]
Jerk
(c) Case 3
Figure 4.10: B´ezier derivative control points - Proposed approach.
99

## Page 118

28.530
27.316
7.881
10.515
16.850
5.240
0.839
1.666
2.256
0.615
0.683
0.547
Case 01
Case 02
Case 03
0
5
10
15
20
25
30
Time (s)
RRT*
IRIS
RRT
BiRRT
Figure 4.11: Comparison of diﬀerent sampling methods for connected safe-corridor
generation.
4.6.2
Web App Based Trajectory Planning Simulator
To demonstrate the practical applicability of the proposed convex trajectory opti-
mization framework, we implement a comprehensive web-app based online simulator
that currently operates on local hardware but can be deployed online. This simulator
provides an intuitive browser interface for mission planning and trajectory visualiza-
tion. The system architecture consists of a Next.js/React frontend coupled with a
FastAPI backend, enabling real-time trajectory planning with user-friendly interface.
The frontend interface utilizes Leaﬂet together with the leaflet-draw extension
and react-leaflet components to provide interactive map-based mission planning
100

## Page 119

Figure 4.12: Web Based Trajectory Planning Simulator
(a) Map - 01
(b) Map - 02
(c) Map - 03
(d) Map - 04
(e) Map - 05
(f) Map - 06
Figure 4.13: Proposed pipeline results using online web app simulator on various
maps.
101

## Page 120

capabilities. Geographic obstacle data are sourced from multiple providers: Open-
StreetMap, Esri World Imagery, and CartoDB basemaps for visualization, while Map-
Tiler vector tiles are decoded in-browser using Mapbox Vector Tile (MVT) format to
extract feature-speciﬁc polygonal obstacles including buildings, water bodies, parks,
and forested areas. It also allows user to deﬁne mission parameters by setting start
and goal waypoints directly on the map interface, manually drawing obstacle polygons
using the integrated drawing tools, or automatically importing geospatial features as
obstacles from MapTiler within a user-deﬁned area of concern (based on start and end
point). The backend implements the complete trajectory planning pipeline through
RESTful API endpoints using FastAPI framework. Obstacle convexiﬁcation utilizes
Shapely geometric operations for polygon decomposition and union operations. The
bidirectional RRT path generation and connected convex corridor construction algo-
rithms are implemented as described in Section 4.3, with user-conﬁgurable parameters
including RRT iteration count and step size fraction. The trajectory optimization
stage is implemented as described in Section 4.5 using CVXPY with Clarabel and
OSQP solvers for convex programming with an options menu in which user can set
the maximum bounds on velocity, acceleration and jerk, B´ezier degree and can also
override the per-corridor time calculated as mentioned in Subsection 4.5.2. In this sim-
ulator, simple bounds are implemented on the control points of derivaitves of B´ezier
curve, instead of convex phase-spaces derived in Subsection 4.4.3. The simulator pro-
vides comprehensive trajectory analysis including kinematic proﬁles, computation per
step and resulting path metrics, and its frontend user interface is shown in Fig. 4.12.
Using this simulator, we evaluate the proposed pipeline by importing obstacles with
the built-in segmentation module using MVT and by manually drawing polygons,
102

## Page 121

Table 4.4: Online web simulator results summary.
Case
Computation Time (ms)
Traversal Time (min:sec)
Path Length (m)
Map 01
4765
1:52
570
Map 02
683
2:05
1100
Map 03
686
0:57
332
Map 04
1189
1:11
448
Map 05
346
1:11
643
Map 06
784
1:06
256
squares, and circles. For these test cases, the B´ezier curve degree is set to 20, and
the derivative bounds are v ∈[−15, 15] m/s, a ∈[−5, 5] m/s2, and j ∈[−2, 2] m/s3.
Fig. 4.13 presents six distinct maps that combine obstacle sets obtained from the
built-in segmentation and from user-drawn annotations. In each map, obstacles are
shown in red, safe convex regions in green, the bidirectional RRT path as a dashed
blue curve, and the optimized trajectory in purple; the start and goal points are
marked in green and red, respectively. The computational time, traversal time and
the path length for each case is tabulated in Table. 4.4.
From these results it is
depicted that, the proposed pipeline is computationally eﬃcient for real-time trajec-
tory planning of UAVS in obstacle-dense environments. For longer trajectories, the
pipeline can be executed in successive segments as the UAV moves from one area to
the next. Since the corridor set is connected and continuity constraints are enforced
at segment interfaces, the concatenated trajectory remains dynamically feasible and
smooth while remaining computationally eﬃcient.
103

## Page 122

4.6.3
Monte Carlo Simulations
To evaluate robustness, we conducted a Monte Carlo analysis. A ﬁxed area of concern
was deﬁned by selecting start and end points on the map and by adding obstacles
using built-in segmentation module, which segments the houses and other buildings
as obstacles on the map, as shown in Fig. 4.14.
Figure 4.14: Map for MonteCarlo simulations with obstacles.
The segmented obstacles were convexiﬁed prior to planning. We then executed
1001 trials in which the start and goal positions were sampled uniformly at random
within the area of concern, with samples rejected if they fell inside any obstacle. The
planner was run with identical constraint parameters across all trials. Across 1001
trials, the planner succeeded in 995 and failed in 6, yielding a success rate of 99.40%.
The solver of record was CLARABEL in 995 trials and OSQP in 6 trials, which
104

## Page 123

has been implemented as a fallback solver in the online web simulator, but fallback
is considered as failure in this scenario. Fig. 4.15 summarizes stage-time dispersion
plots such as computational time for generating a bidirectional-RRT path, convex
corridor, and trajectory optimization for all Monte Carlo simulations, Fig. 4.17 shows
the traversal-time and path-length histograms, and Fig. 4.16 visualizes the optimized
trajectories for the Monte Carlo simulations.
The Monte Carlo runs show stable
BiRRT
Convex Regions
Optimization
0
0.5
1
1.5
2
2.5
3
3.5
4
4.5
Seconds
Figure 4.15: Stage time distributions for Monte Carlo simulations.
solve times across varied start and goal pairs. The few failures occurred in narrow
passages where corridor generation failed, or when the initial time allocation was too
tight, but those cases can be addressed by increasing the bidirectional RRT iterations,
reducing step size, and increasing the safety margin for initial physics-based time allo-
cation to account for tighter turns. Combined with the three-map comparison against
105

## Page 124

-52.74
-52.739
-52.738
-52.737
-52.736
-52.735
-52.734
-52.733
-52.732
-52.731
Longitude
47.5625
47.563
47.5635
47.564
47.5645
47.565
47.5655
47.566
Latitude
Success
Failure
Figure 4.16: Optimized paths by outcome (success vs.
failure) for Monte Carlo
simulations.
GCS+KTO, these results support the claim that proposed pipeline provides reliable
planning with lower computation and shorter traversal time while meeting dynamic
limits. The Monte Carlo analysis conﬁrms the robustness of proposed pipeline across
diﬀerent scenarios, with failures only in extreme cases that can be addressed through
parameter tuning. The web-based simulator further validates the framework’s readi-
ness for practical deployment, providing an intuitive interface for mission planning
and real-time trajectory visualization. These results demonstrate that the proposed
framework provides a practical solution for real-time UAV trajectory planning in
obstacle-dense environments, bridging the gap between theoretical optimization and
real-world implementation.
106

## Page 125

Traversal Time (s)
0
100
200
300
s
0
50
100
150
200
250
Count
Path Length (km)
0
0.2
0.4
0.6
0.8
km
0
20
40
60
80
100
120
140
160
180
Count
Figure 4.17: Traversal time and path length histograms for Monte Carlo simulations.
4.7
Conclusion
This work presented a time-eﬃcient, convex optimization–based trajectory planning
pipeline for UAVs operating in obstacle-dense environments. A collision-free corridor
is constructed by greedily generating a minimal sequence of overlapping convex re-
gions along a bidirectional RRT reference path, avoiding workspace-wide IRIS region
inﬂation. Given this connected corridor, the trajectory is parameterized using ﬁxed-
degree piecewise B´ezier curves, and derivative-consistency and continuity constraints
are enforced directly on B´ezier control points. Dynamic feasibility is incorporated
through diﬀerential-ﬂatness relations by convexifying the admissible phase spaces of
inertial velocity, acceleration, and jerk into polytopic sets, which are then imposed
as linear inequality constraints in a single convex program. Experimental evaluation
on three obstacle-rich maps showed that the proposed pipeline achieves substantially
107

## Page 126

lower compute time than a GCS+KTO baseline while producing comparable path
lengths. Under identical dynamic limits, the proposed method reduced traversal time
by 36% on average and achieved a mean computational speedup of 17×. Robustness
was further evaluated using 1,001 Monte Carlo trials over randomized start–goal pairs,
where the pipeline succeeded in 995 cases (99.4%), with the remaining failures pri-
marily occurring in narrow passages due to corridor-generation limitations or overly
tight initial time allocation. A web-based planning simulator was also developed to
demonstrate practical integration with map-based mission speciﬁcation and real-time
trajectory visualization. The proposed pipeline guarantees global optimality for the
convexiﬁed problem given a precomputed, traversable, connected corridor of convex
polygons and convexiﬁed dynamic phase-space bounds for a speciﬁed B´ezier degree,
while being more computationally eﬃcient than the baseline approach. Future work
will focus on three key extensions: embedding time optimization directly within the
convex program, developing convex formulations for separate lateral and tangential
acceleration constraints, and extending the framework to 3D ﬂight environments.
4.8
Bibliography
[1] S. Aggarwal and N. Kumar, “Path planning techniques for unmanned aerial
vehicles: A review, solutions, and challenges,” Computer Communications, vol.
149, pp. 270–299, 2020.
[2] T. Marcucci, M. Petersen, D. von Wrangel, and R. Tedrake, “Motion planning
around obstacles with convex optimization,” Science Robotics, vol. 8, no. 84,
eadf7843, 2023.
108

## Page 127

[3] R. Deits and R. Tedrake, “Computing large convex regions of obstacle-free space
through semideﬁnite programming,” in Algorithmic Foundations of Robotics XI
(Springer Tracts in Advanced Robotics, vol. 107), Springer, 2015, pp. 109–124.
[4] A. Richards and J. P. How, “Mixed-integer programming for control,” in Proc.
American Control Conference (ACC), 2005, pp. 2676–2683.
[5] D. von Wrangel and R. Tedrake, “Using Graphs of Convex Sets to Guide Noncon-
vex Trajectory Optimization,” in Proc. IEEE/RSJ Int. Conf. Intelligent Robots
and Systems (IROS), 2024, pp. 9863–9870.
[6] D. Mellinger and V. Kumar, “Minimum snap trajectory generation and control
for quadrotors,” in Proc. IEEE Int. Conf. Robotics and Automation (ICRA),
Shanghai, China, May 9–13, 2011, pp. 2520–2525.
[7] V. Dugar, S. Choudhury, and S. Scherer, “A KITE in the wind: Smooth trajec-
tory optimization in a moving reference frame,” in Proc. IEEE Int. Conf. Robotics
and Automation (ICRA), Singapore, May 29–June 3, 2017, pp. 109–116.
[8] M. R. Jones, S. Djahel, and K. Welsh, “Path-Planning for Unmanned Aerial
Vehicles with Environment Complexity Considerations: A Survey,” ACM Com-
puting Surveys, vol. 55, no. 11, Article 234, 39 pp., 2023.
[9] R. T. Farouki, “The Bernstein polynomial basis: A centennial retrospective,”
Computer Aided Geometric Design, vol. 29, no. 6, pp. 379–419, 2012.
[10] E. W. Dijkstra, “A note on two problems in connexion with graphs,” Numerische
Mathematik, vol. 1, no. 1, pp. 269–271, 1959.
109

## Page 128

[11] P. E. Hart, N. J. Nilsson, and B. Raphael, “A formal basis for the heuristic
determination of minimum cost paths,” IEEE Trans. Systems Science and Cy-
bernetics, vol. 4, no. 2, pp. 100–107, 1968.
[12] S. M. LaValle, Planning Algorithms. Cambridge, U.K.: Cambridge Univ. Press,
2006.
[13] L. E. Kavraki, P. Svestka, J.-C. Latombe, and M. H. Overmars, “Probabilistic
roadmaps for path planning in high-dimensional conﬁguration spaces,” IEEE
Trans. Robotics and Automation, vol. 12, no. 4, pp. 566–580, 1996.
[14] S. M. LaValle and J. J. Kuﬀner Jr., “Randomized kinodynamic planning,” Int.
J. Robotics Research, vol. 20, no. 5, pp. 378–400, 2001.
[15] J. J. Kuﬀner and S. M. LaValle, “RRT-Connect:
An eﬃcient approach to
single-query path planning,” in Proc. IEEE Int. Conf. Robotics and Automa-
tion (ICRA), San Francisco, CA, USA, 2000, pp. 995–1001.
[16] S. Karaman and E. Frazzoli, “Sampling-based algorithms for optimal motion
planning,” Int. J. Robotics Research, vol. 30, no. 7, pp. 846–894, 2011.
[17] B. R. Donald, J. Xavier, J. Canny, and J. Reif, “Kinodynamic motion planning,”
Journal of the ACM, vol. 40, no. 5, pp. 1048–1066, 1993.
[18] J. T. Betts, “Survey of numerical methods for trajectory optimization,” Journal
of Guidance, Control, and Dynamics, vol. 21, no. 2, pp. 193–207, 1998.
[19] M. P. Kelly, “An introduction to trajectory optimization: How to do your own
direct collocation,” SIAM Review, vol. 59, no. 4, pp. 849–904, 2017.
110

## Page 129

[20] M. Zucker, N. Ratliﬀ, A. Dragan, M. Pivtoraiko, M. Klingensmith, C. Dellin, J.
A. Bagnell, and S. Srinivasa, “CHOMP: Covariant Hamiltonian optimization for
motion planning,” Int. J. Robotics Research, vol. 32, nos. 9–10, pp. 1164–1193,
2013, doi: 10.1177/0278364913488805.
[21] M. Kalakrishnan, S. Chitta, E. Theodorou, P. Pastor, and S. Schaal, “STOMP:
Stochastic trajectory optimization for motion planning,” in Proc. IEEE Int.
Conf. Robotics and Automation (ICRA), Shanghai, China, May 9–13, 2011, pp.
4569–4574.
[22] J. Schulman et al., “Motion planning with sequential convex optimization
and convex collision checking,” Int. J. Robotics Research, vol. 33, no. 9, pp.
1251–1270, 2014.
[23] S. Boyd and L. Vandenberghe, Convex Optimization. Cambridge, U.K.: Cam-
bridge Univ. Press, 2004.
[24] Y. Nesterov and A. Nemirovskii, Interior-Point Polynomial Algorithms in Con-
vex Programming. Philadelphia, PA, USA: SIAM, 1994.
[25] M. Fliess, J. L´evine, P. Martin, and P. Rouchon, “Flatness and defect of nonlinear
systems: Introductory theory and examples,” International Journal of Control,
vol. 61, no. 6, pp. 1327–1361, 1995.
[26] R. Mahony, V. Kumar, and P. Corke, “Multirotor aerial vehicles: Modeling,
estimation, and control of quadrotors,” IEEE Robotics & Automation Magazine,
vol. 19, no. 3, pp. 20–32, 2012.
111

## Page 130

[27] C. Richter, A. Bry, and N. Roy, “Polynomial trajectory planning for aggressive
quadrotor ﬂight in dense indoor environments,” in Robotics Research: The 16th
International Symposium ISRR, Springer Tracts in Advanced Robotics, vol. 114,
Springer, 2016, pp. 649–666, doi: 10.1007/978-3-319-28872-7 37.
[28] L. Piegl and W. Tiller, The NURBS Book, 2nd ed. Berlin, Germany: Springer,
1997.
[29] M. de Berg, O. Cheong, M. van Kreveld, and M. Overmars, Computational
Geometry: Algorithms and Applications, 3rd ed. Berlin, Germany: Springer,
2008.
[30] R. Tedrake and the Drake Development Team, “Drake: Model-based design and
veriﬁcation for robotics,” 2019. [Online]. Available: https://drake.mit.edu
[31] J. Gravesen, “The length of B´ezier curves,” in Graphics Gems V, Academic
Press, 1995, pp. 199–205.
[32] P. E. Gill, W. Murray, and M. A. Saunders, “SNOPT: An SQP algorithm for
large-scale constrained optimization,” SIAM Review, vol. 47, no. 1, pp. 99–131,
2005.
112

## Page 131

Chapter 5
Hardware-in-the-Loop
Implementation and Validation of
Trajectory Control Algorithms for
DJI M300 RTK using DJI OSDK
and ROS
This chapter has been submitted to American Society of Mechanical Engineers (ASME)
Letters in Dynamic Systems and Control.
113

## Page 132

Abstract
This letter presents the development of a hardware-in-the-loop (HITL) simulation
framework for the DJI M300 RTK and the implementation and validation of tra-
jectory tracking controllers, including proportional–integral–derivative (PID), linear
quadratic regulator (LQR), and model predictive control (MPC). The framework in-
tegrates the DJI Onboard SDK (OSDK) with ROS Kinetic on the DJI Manifold 2-G
onboard computer, enabling real-time onboard execution of the control algorithms
and closed-loop HITL evaluation using the DJI Assistant 2 Simulator. Both LQR
and MPC are formulated using the same linear double-integrator dynamics, and all
three controllers share a common trajectory generation pipeline. Experimental val-
idation on circular and ﬁgure-eight trajectories demonstrates satisfactory tracking
performance for all three controllers. Observed performance diﬀerences are primarily
attributable to controller tuning rather than inherent algorithmic limitations. Wind-
disturbance tests further indicate robust tracking under moderate disturbances, with
noticeable degradation occurring only when attitude saturation limits are reached.
Overall, this work provides a validated HITL framework for deploying and evaluating
advanced trajectory planning and control algorithms on the DJI M300 RTK platform.
5.1
Introduction
Quadrotor unmanned aerial vehicles (UAVs) are widely used in research and commer-
cial applications due to their maneuverability, vertical takeoﬀand landing capability,
and ability to operate in constrained environments [1]. The intrinsic instability and
114

## Page 133

underactuation of quadrotors pose signiﬁcant challenges for robust control design,
implementation, and validation [2, 3]. These challenges have motivated the devel-
opment of control strategies ranging from classical proportional–integral–derivative
(PID) control to optimal and predictive methods such as linear quadratic regulator
(LQR) and model predictive control (MPC) [4, 5].
A major practical challenge is the implementation and validation of control al-
gorithms on commercial UAV platforms with onboard computing and proprietary
ﬂight control interfaces. Software in the loop (SITL) simulation is useful for early
development, but it often fails to capture hardware dependent eﬀects, including com-
putational limits, communication latency, message timing, and interface constraints
imposed by the ﬂight controller.
Hardware in the loop (HITL) testing mitigates
these limitations by executing the actual ﬂight software on embedded hardware while
preserving the safety and repeatability of a simulated environment.
HITL there-
fore enables algorithm validation under more realistic operating conditions prior to
ﬂight testing. Despite extensive literature on quadrotor control, publicly documented
end-to-end HITL workﬂows for DJI commercial platforms remain limited, particularly
those that execute onboard ROS nodes and interface with the ﬂight controller through
the DJI Onboard SDK (OSDK). Moreover, to the best of the authors’ knowledge, a
uniﬁed implementation and performance comparison of PID, LQR, and MPC on the
DJI Matrice 300 RTK (M300 RTK) using the DJI OSDK and the DJI Assistant 2
simulation environment has not been reported.
This paper presents the implementation and experimental validation of PID, LQR,
and MPC trajectory tracking controllers on the DJI M300 RTK in an HITL setup.
The HITL framework integrates the DJI Manifold 2-G onboard computer running
115

## Page 134

Ubuntu 16.04 and ROS Kinetic with the M300 RTK ﬂight controller through the
OSDK Expansion Module, enabling real-time execution of trajectory control algo-
rithms directly on the onboard embedded platform during simulation [6, 7].
The
framework employs a uniﬁed trajectory generation pipeline shared by all three con-
trollers, along with a common acceleration-to-attitude mapping interface. For the
model-based controllers, both LQR and MPC are formulated using the same linear
double-integrator dynamics. This design isolates algorithmic eﬀects from platform
and modeling variations, providing a fair basis for comparing performance under
identical conditions. Additionally, wind disturbances are injected in the DJI Assis-
tant 2 Simulator to assess robustness under external perturbations and to examine
the disturbance-rejection behavior of the inner-loop attitude stabilization. Hence, the
key contributions of this work are:
 Development and validation of a complete HITL framework for the DJI M300
RTK that executes onboard ROS nodes on the Manifold 2-G via the DJI OSDK
and closes the loop through the DJI Assistant 2 Simulator, enabling safe and
repeatable preﬂight testing on real embedded hardware.
 Implementation, validation, and performance comparison of PID, LQR, and
MPC trajectory-tracking controllers within a uniﬁed test framework.
5.2
System Architecture
The HITL testing framework integrates the DJI M300 RTK ﬂight controller, a DJI
Manifold 2-G companion computer running ROS, and the DJI Assistant 2 Simula-
116

## Page 135

tor to enable systematic evaluation of quadrotor trajectory-tracking controllers. This
section summarizes the hardware platform (M300 RTK airframe and Manifold 2-G),
the software architecture, and the communication interfaces used for repeatable con-
troller implementation and comparison. The overall HITL architecture is presented
in Fig. 5.1.
Figure 5.1: Overall HITL Architecture.
5.2.1
DJI M300 RTK Hardware Platform
The DJI Matrice 300 RTK serves as the primary aircraft platform for this work. The
M300 RTK supports long endurance operation (≈55 minutes), a maximum takeoﬀ
weight of 9 kg, and an IP45 ingress protection rating, enabling repeated experimental
117

## Page 136

trials under realistic operating conditions. The integrated RTK subsystem provides
centimeter-level positioning when RTK is enabled and ﬁxed, which is valuable for
quantitative trajectory-tracking evaluation. In addition, the platform includes re-
dundant sensors (e.g., multiple inertial and environmental sensors and dual RTK
antennas) to improve robustness during testing and actual missions. [8]
5.2.2
DJI Onboard SDK Integration
The DJI Onboard SDK (OSDK) provides the interface between the onboard compan-
ion computer and the M300 RTK ﬂight controller. The OSDK client running on the
companion computer (Manifold 2-G) receives telemetry and transmits ﬂight-control
setpoints, while the embedded ﬂight controller executes these commands through its
internal stabilization, safety checks, and mode management. The OSDK application
layer does not replace or bypass the inner-loop attitude stabilization implemented on
the ﬂight controller. [6]
OSDK ﬂight-control setpoints are selected through the Control API by conﬁguring
the control mode byte (joystick ﬂags), which speciﬁes the commanded quantity and
reference frame on each axis. For horizontal motion, the API supports roll/pitch
angle commands, roll/pitch angular-rate commands, horizontal velocity commands,
or horizontal position commands. The yaw channel supports angle or rate control,
while the vertical channel supports position, velocity, or thrust commands. These
modes can be issued using flightCtrl(CtrlData) with the appropriate ﬂags, or via
provided helper interfaces depending on the desired command structure. [9, 10]
In this work, all controllers share a common command interface implemented
118

## Page 137

through the OSDK ﬂight-control pipeline.
Speciﬁcally, the outer-loop controllers
generate commands that are mapped to roll and pitch angle setpoints, a yaw rate
setpoint, and a vertical position setpoint before being transmitted to the ﬂight con-
troller at each sampling instant.
The ﬂight controller then tracks these setpoints
using its internal attitude and altitude stabilization loops. [11]
5.2.3
Onboard Computing Platform
The onboard computing platform is the DJI Manifold 2 series. Two variants are avail-
able: the Manifold 2-C (Intel Core i7-8550U) and the Manifold 2-G (NVIDIA Jetson
TX2), both with 8 GB RAM and onboard storage. In this work, the Manifold 2-G is
used to execute the ROS-based controller nodes and supporting middleware in real
time [12]. The Manifold 2-G connects to the M300 RTK via the OSDK Expansion
Module, which provides a mechanical mounting interface and exposes OSDK con-
nectivity to the companion computer through standard ports and wiring harnesses.
In the presented conﬁguration, the Manifold hosts the controller nodes, trajectory
generation, and logging processes, while the ﬂight controller remains responsible for
low-level stabilization and safety. [13]
5.2.4
ROS Framework and Communication
The Robot Operating System (ROS) provides the middleware for the onboard soft-
ware architecture.
Each trajectory-tracking controller is implemented as an inde-
pendent ROS node, while sharing a common trajectory generator and a common
command-mapping interface to ensure consistent test conditions across controllers
119

## Page 138

[14]. State feedback is obtained through the OSDK-ROS telemetry interface, which
exposes ﬂight-controller telemetry as ROS topics under the dji osdk ros/ namespace
(e.g., attitude, velocity, local position, and height above takeoff).
These
telemetry topics provide the state estimates required by the outer-loop controllers
for tracking and evaluation. Control commands are produced by the controller node,
passed through a common acceleration-to-attitude and altitude command mapping
layer, and then forwarded through the OSDK ﬂight-control interface to the ﬂight
controller. [13]
5.2.5
HITL Testing Environment
The DJI Assistant 2 simulator is used as the HITL testing environment while the
actual onboard computer executes the ROS nodes in real time. In DJI’s architecture,
the aircraft simulator resides on the aircraft ﬂight controller and can be initialized
and visualized using DJI Assistant 2 over a USB connection. When the simulator is
enabled, the ﬂight controller produces simulated vehicle motion and outputs corre-
sponding simulated state information. [7]
In the proposed HITL setup, the companion computer continues to communicate
with the ﬂight controller via OSDK exactly as in real ﬂight. Importantly, the sim-
ulated state generated by the ﬂight controller’s simulator is streamed through the
same OSDK telemetry channel and is therefore accessible to the onboard ROS stack
through the same dji osdk ros/ telemetry topics used in outdoor operation. This
preserves the timing, message pathways, and command interfaces of the onboard
control stack while eliminating ﬂight risk. Additionally, the simulator’s environmen-
120

## Page 139

Figure 5.2: HITL setup showing the connections between the DJI M300 RTK drone,
DJI Manifold 2-G onboard computer, OSDK Expansion Module, and Windows lap-
top.
tal settings (e.g., wind speed conﬁgured during simulator initialization) are used to
inject repeatable external disturbances for robustness assessment under controlled
conditions. [7]
5.3
Methodology
This section presents the mathematical formulations of the control algorithms and
explains the comparison framework for performance evaluation.
5.3.1
System Dynamics Model
The dynamical model used for XY position tracking control is derived from the full
nonlinear translational dynamics of a quadrotor [15]. The translational motion equa-
121

## Page 140

Figure 5.3: Hardware-in-the-loop (HITL) setup. Left: Windows laptop running the
DJI Assistant 2 simulator. Right: monitor connected to the DJI Manifold 2-G with
ROS nodes running.
tions in the ENU frame are given by:


¨x
¨y
¨z


= fb
m


cos ψ sin θ cos ϕ + sin ψ sin ϕ
sin ψ sin θ cos ϕ −cos ψ sin ϕ
cos θ cos ϕ


−


0
0
g


(5.1)
where fb is the total thrust force, m is the quadrotor mass, g is the gravitational
acceleration, and ϕ, θ, and ψ denote the roll, pitch, and yaw angles, respectively.
To obtain a linear model suitable for horizontal position control, the dynamics are
linearized about a hover equilibrium under the assumptions of small roll and pitch
angles (|ϕ| ≪1 rad, |θ| ≪1 rad) with yaw held ﬁxed at ψ = 0, so that sin ϕ ≈ϕ,
cos ϕ ≈1, sin θ ≈θ, cos θ ≈1, and sin ϕ sin θ ≈0, while the thrust is taken to
approximately balance weight at hover (fb ≈mg). Aerodynamic drag and external
disturbances are neglected in this linearization. Applying these assumptions to (5.1),
122

## Page 141

the horizontal acceleration components simplify to:
¨x ≈gθ
(5.2)
¨y ≈−gϕ
(5.3)
Under the stated assumptions, the horizontal dynamics decouple into two independent
double integrators systems. The continuous-time dynamics for the horizontal plane
are:
¨x = ax,ENU,
¨y = ay,ENU
(5.4)
where ax,ENU = ¨x and ay,ENU = ¨y are the desired ENU-frame accelerations. Deﬁning
the state vector x = [x, y, vx, vy]T ∈R4 and control input u = [ax, ay]T ∈R2, the
discrete-time dynamics with sampling time ∆t are:
xk+1 = Axk + Buk
(5.5)
where the system matrices are derived from exact discretization of (5.4) as:
A =


1
0
∆t
0
0
1
0
∆t
0
0
1
0
0
0
0
1


,
B =


1
2∆t2
0
0
1
2∆t2
∆t
0
0
∆t


(5.6)
This model is used by both LQR and MPC controllers.
5.3.2
Common Control Framework
All three controllers share a common framework for transforming desired accelerations
to attitude commands. From (5.2) and (5.3), the relationship between ENU-frame
123

## Page 142

accelerations and attitude angles is ¨x ≈gθ and ¨y ≈−gϕ. The desired ENU-frame
accelerations are transformed to the body frame using the current yaw angle ψ as:


ax,body
ay,body

=


cos ψ
sin ψ
−sin ψ
cos ψ




ax,ENU
ay,ENU


(5.7)
The body-frame accelerations are then mapped to roll and pitch commands as:
θcmd = satθmax
ax,body
g

,
ϕcmd = satϕmax

−ay,body
g

(5.8)
where θmax and ϕmax are the maximum allowable pitch and roll angles, and the satu-
ration function sata(·) is deﬁned as:
sata(x) =

















a
if x > a
x
if −a ≤x ≤a
−a
if x < −a
(5.9)
For altitude control, the desired z position is sent directly as a setpoint to the DJI
ﬂight controller. Yaw control employs a proportional controller with angle wrapping
and can be deﬁned as:
˙ψcmd = sat ˙ψmax (Kyaw · wrap(ψref −ψ))
(5.10)
where Kyaw is the yaw proportional gain and ˙ψmax is the maximum yaw-rate limit.
The angle-wrapping function wrap(·) : R →[−π, π] is deﬁned as wrap(θ) = mod(θ +
π, 2π) −π.
124

## Page 143

5.3.3
Controller Formulations
5.3.3.1
PID Controller
The PID controller computes desired accelerations in the ENU frame based on posi-
tion and velocity errors. The control law is deﬁned as:
ades,ENU = Kpep + Kdev + KiI
(5.11)
where ep = pref −p is the position error vector in the XY plane, ev = vref −v is the
velocity error vector, and Kp, Kd, Ki are the proportional, derivative, and integral
gains. The integral term I accumulates position error with anti-windup saturation
as:
I(t + ∆t) = satImax(I(t) + ep∆t)
(5.12)
where Imax is the integrator saturation limit. The computed accelerations are then
transformed to attitude commands using the common framework described in (5.7)
and (5.8).
5.3.3.2
Linear Quadratic Regulator (LQR)
The LQR controller minimizes a quadratic cost function to achieve optimal linear
control. Using the system dynamics model from (5.5) and (5.6), the LQR gain matrix
K is computed by solving the Discrete Algebraic Riccati Equation (DARE) iteratively
as:
Si = R + BTXiB
(5.13)
Ki = S−1
i BTXiA
(5.14)
Xi+1 = AT(Xi −XiBKi)A + Q
(5.15)
125

## Page 144

where Xi is the solution matrix at iteration i, initialized as X0 = Q. The iteration
continues for a maximum of 200 iterations or until convergence (∥Xi+1 −Xi∥∞<
10−9). The weight matrices are:
Q = diag(Qpos, Qpos, Qvel, Qvel),
R = diag(Racc, Racc)
(5.16)
where Qpos penalizes position errors, Qvel penalizes velocity errors, and Racc penalizes
control eﬀort. The control law combines feedforward and feedback terms, and can be
written as:
u = aﬀ−K(x −xref)
(5.17)
where the feedforward acceleration is computed from the reference velocity using ﬁnite
diﬀerences:
aﬀ(t) = vref(t) −vref(t −∆t)
∆t
(5.18)
The computed accelerations are then transformed to attitude commands using (5.7)
and (5.8).
5.3.3.3
Model Predictive Control (MPC)
The MPC controller solves a ﬁnite-horizon optimal control problem at each time step
using the system dynamics model from (5.5) and (5.6). At each sampling instant,
given the current state x0, the MPC solves:
min
{uk}N−1
k=0
J =
N−1
X
k=0

(xk −xref,k)TQ(xk −xref,k) + uT
k Ruk

subject to
xk+1 = Axk + Buk,
k = 0, . . . , N −1
x0 = x(t)
uk ∈U,
k = 0, . . . , N −1
(5.19)
126

## Page 145

where N is the prediction horizon, and Q = diag(qpos, qpos, qvel, qvel) and R = diag(racc, racc)
are weight matrices. The constraint set U consists of roll and pitch angle limits. The
implementation computes prediction matrices that include the dynamics over the
horizon. Recursively applying the dynamics yields:
X = Sxx0 + SuU
(5.20)
where X = [xT
1 , . . . , xT
N]T ∈R4N contains predicted states, U = [uT
0 , . . . , uT
N−1]T ∈
R2N is the decision variable, and:
Sx =


A
A2
...
AN


∈R4N×4,
Su =


B
0
· · ·
0
AB
B
· · ·
0
...
...
...
...
AN−1B
AN−2B
· · ·
B


∈R4N×2N
(5.21)
Using these matrices, the cost function becomes:
J = 1
2UTHU + f TU
(5.22)
where H = ST
u ¯QSu + ¯R and f = ST
u ¯Q(Sxx0 −Xref), with ¯Q = diag(Q, . . . , Q) ∈
R4N×4N and ¯R = diag(R, . . . , R) ∈R2N×2N.
For each time step k, body-frame
accelerations are computed using the current yaw angle ψ:


ax,body,k
ay,body,k

=


cos ψ
sin ψ
−sin ψ
cos ψ




ux,k
uy,k


(5.23)
with constraints:
−gθmax ≤ax,body,k ≤gθmax,
−gϕmax ≤ay,body,k ≤gϕmax
(5.24)
127

## Page 146

The resulting constrained quadratic program is implemented in CasADi and solved
using IPOPT [16, 17]. After obtaining the optimal sequence U∗, only the ﬁrst control
action u∗
0 is applied along with the feedforward compensation as:
ucmd = aﬀ+ u∗
0
(5.25)
where aﬀ= dvref/dt. The commanded accelerations are then transformed to attitude
commands using (5.7) and (5.8).
5.4
Results and Discussion
This section presents experimental validation of the three control algorithms within
the HITL simulation framework. All controllers were evaluated on circular and ﬁgure-
8 trajectories, both maintaining constant altitude, to assess performance under vary-
ing curvature conditions. Experiments utilized the DJI Assistant 2 simulator with
ﬂight controller code executing on the DJI Manifold 2-G onboard computer with
Ubuntu 16.04 and ROS Kinetic. All simulation data were logged on the DJI Man-
ifold 2-G, which hosted the controller nodes, and were subsequently processed and
plotted in MATLAB.
5.4.1
Experimental Setup
A uniﬁed trajectory generator provides identical reference commands to all controllers
and generates both a circular and a ﬁgure-8 (lemniscate) path. The circular trajectory
is deﬁned by:
xref(t) = xc + r cos(ωt),
yref(t) = yc + r sin(ωt)
(5.26)
128

## Page 147

where xc, yc are the trajectory center coordinates (set to the initial vehicle position), r
is the radius parameter, and ω = v/r is the angular velocity. The reference velocities
commands can be calculated as:
vx,ref(t) = −rω sin(ωt),
vy,ref(t) = rω cos(ωt)
(5.27)
The ﬁgure-8 trajectory is deﬁned by:
xref(t) = xc + r sin(ωt),
yref(t) = yc + r sin(ωt) cos(ωt)
(5.28)
with corresponding reference velocities deﬁned as:
vx,ref(t) = rω cos(ωt),
vy,ref(t) = rω
cos2(ωt) −sin2(ωt)

(5.29)
Altitude control uses a constant proﬁle zref(t) = ztakeoﬀ+ h0, where ztakeoﬀis take-
oﬀaltitude and h0 is desired height above takeoﬀ.
Again, both LQR and MPC
controllers share identical linear dynamics models (5.5) and (5.6), ensuring perfor-
mance diﬀerences reﬂect algorithmic characteristics rather than model discrepancies.
Similarly, all controllers employ the same coordinate frame transformation (5.7) and
acceleration-to-angle mapping (5.8).
All controllers operate at 50 Hz (∆t = 0.02 s) with g = 9.8066 m/s2. Common
attitude limits are ϕmax = θmax = ±35◦, ˙ψmax = ±100◦/s, Kyaw = 1.2 s−1, and altitude
constraints of 0.5–50 m. The PID controller uses Kp = 0.6 s−2, Kd = 1.2 s−1, Ki =
0.05 s−3 with integrator limit Imax = 3.0 m·s. LQR employs weights Qpos = 2000,
Qvel = 1000, Racc = 1000. MPC uses prediction horizon N = 15 steps with weights
Qpos = 20000, Qvel = 6000, Racc = 1300, solver tolerance 10−4, and maximum 100
iterations. The circular trajectory has radius r = 30 m at constant speed v = 3 m/s
and base altitude h0 = 5 m, completing one loop. This provides constant curvature
129

## Page 148

for baseline assessment, while the ﬁgure-8 introduces varying curvature and direction
changes that challenge trajectory tracking capabilities.
5.4.2
Circular Trajectory Performance
Fig. 5.4 presents the 3D trajectory tracking and individual position components for
the circular trajectory. All controllers demonstrate reasonable tracking performance,
with LQR showing superior tracking accuracy compared to the others. Table 5.1
summarizes quantitative metrics. LQR achieves the lowest RMSE of 0.8716 meters,
which represents an 11.4% reduction compared to PID (0.9840 m) and a 20.9% reduc-
tion compared to MPC (1.1019 m). The Z position remains constant at the desired
altitude, demonstrating eﬀective altitude hold throughout the maneuver.
The corre-
sponding velocity responses for the circular trajectory tracking are shown in Fig. 5.5
and similarly, the acceleration responses are shown in Fig. 5.6.
Attitude responses
in Fig. 5.7 show all controllers maintain roll and pitch angles well within limits. Yaw
remains relatively constant under the yaw-hold strategy.
5.4.3
Figure-8 Trajectory Performance
The ﬁgure-8 trajectory presents increased challenges due to varying curvature and
direction reversals. Fig. 5.8 shows tracking performance with noticeably larger errors
compared to the circular case, particularly at the crossover point where curvature
changes rapidly. As shown in Table 5.1, RMSE values increase for all controllers:
LQR achieves 1.1425 m, a 3.4% reduction relative to PID (1.1826 m) and a 21.9%
reduction relative to MPC (1.4624 m).
130

## Page 149

-30
-20
-10
0
10
20
30
x (m)
-30
-20
-10
0
10
20
30
y (m)
3D Trajectory
-40
-20
0
20
40
x (m)
-40
-20
0
20
40
y (m)
10
20
30
40
50
60
Time (s)
0
1
2
3
4
5
z (m)
Reference
PID
LQR
MPC
Figure 5.4: Circular trajectory 3D Tracking and individual position responses.
0
20
40
60
Time (s)
-4
-3
-2
-1
0
1
2
3
4
vx (m/s)
0
20
40
60
Time (s)
-4
-3
-2
-1
0
1
2
3
4
5
6
vy (m/s)
0
20
40
60
Time (s)
-0.2
0
0.2
0.4
0.6
0.8
1
1.2
1.4
vz (m/s)
PID
LQR
MPC
Figure 5.5: Circular trajectory velocity responses.
131

## Page 150

0
10
20
30
40
50
60
Time (s)
-0.8
-0.6
-0.4
-0.2
0
0.2
0.4
0.6
ax (m/s2)
0
10
20
30
40
50
60
Time (s)
-2
-1
0
1
2
3
4
5
6
7
8
ay (m/s2)
PID
LQR
MPC
Figure 5.6: Circular trajectory acceleration commands.
0
20
40
60
Time (s)
-20
-10
0
10
20
30
3 (deg)
0
20
40
60
Time (s)
-30
-20
-10
0
10
20
? (deg)
Command
PID
LQR
MPC
Figure 5.7: Circular trajectory attitude angles.
132

## Page 151

-30
-20
-10
0
10
20
30
x (m)
-30
-20
-10
0
10
20
30
y (m)
3D Trajectory
-40
-20
0
20
40
x (m)
-20
-10
0
10
20
y (m)
10
20
30
40
50
60
Time (s)
0
1
2
3
4
5
z (m)
Reference
PID
LQR
MPC
Figure 5.8: Figure 8 trajectory 3D Tracking and individual position responses.
The corresponding velocity responses for the ﬁgure-8 trajectory tracking are shown
in Fig. 5.9 and similarly, the acceleration responses are shown in Fig. 5.10.
Finally,
0
20
40
60
Time (s)
-4
-3
-2
-1
0
1
2
3
4
5
6
vx (m/s)
0
20
40
60
Time (s)
-4
-3
-2
-1
0
1
2
3
4
5
6
vy (m/s)
0
20
40
60
Time (s)
-0.2
0
0.2
0.4
0.6
0.8
1
1.2
1.4
vz (m/s)
PID
LQR
MPC
Figure 5.9: Figure-8 trajectory velocity tracking.
133

## Page 152

0
10
20
30
40
50
60
Time (s)
-2
0
2
4
6
8
10
ax (m/s2)
0
10
20
30
40
50
60
Time (s)
-4
-2
0
2
4
6
8
10
ay (m/s2)
PID
LQR
MPC
Figure 5.10: Figure-8 trajectory acceleration commands.
0
20
40
60
Time (s)
-30
-20
-10
0
10
20
30
3 (deg)
0
20
40
60
Time (s)
-20
-10
0
10
20
30
? (deg)
Command
PID
LQR
MPC
Figure 5.11: Figure-8 trajectory attitude angles.
the attitude responses in Fig. 5.11 show all controllers maintain roll and pitch angles
well within limits, and the yaw angle remains relatively constant under the yaw-hold
strategy.
In HITL, while the simulation runs in DJI Assistant 2, the DJI Smart Controller
shows the drone’s path in real time, as shown in Fig. 5.12. The experimental results
134

## Page 153

(a) Figure-8 path.
(b) Circular path.
Figure 5.12: DJI Smart Controller traces rendered during HITL execution.
for nominal cases reveal that the better performance of one controller over another is
mainly a tuning issue rather than a fundamental algorithmic diﬀerence. As tabulated
in Table 5.1, LQR achieved the lowest tracking error because of its well-tuned gain
matrix K and explicit feedforward acceleration, which produced smooth commands.
MPC’s tracking gap came from formulation and tuning choices rather than the solver
or core algorithm. Similarly, the PID controller also has reasonable tracking perfor-
mance but is sensitive to gain selection, and diﬀerent tuning could change its relative
performance. It is worth noting that although the control model does not incorpo-
rate drag forces, but the DJI Assistant 2 HITL simulator does model drag eﬀects.
Despite this model-reality mismatch, the implemented control strategies still exhibit
satisfactory tracking performance, demonstrating robustness to unmodeled dynam-
ics.
The presented uniﬁed HITL framework enables fair, repeatable comparisons
under identical interfaces and can support implementation of modern model-based,
learning-based, or data-driven control frameworks in the HITL environment.
135

## Page 154

Table 5.1: RMSE Performance Comparison.
Controller
Circular (m)
Figure-8 (m)
PID
0.9840
1.1826
LQR
0.8716
1.1425
MPC
1.1019
1.4624
5.4.4
Disturbance Analysis
In this HITL setup, users can add wind in DJI Assistant 2 by entering three world–frame
components aligned with North, East, and Down, as shown in Fig. 5.13. When the
Figure 5.13: Setting wind disturbances in DJI Assistant 2 simulator.
drone is holding position, the inner stabilization loop in the ﬂight controller treats
this as a steady disturbance and tilts the drone (roll/pitch) into the wind to hold
position, as shown in Fig. 5.14. Hence, the outer-loop trajectory controllers (PID,
LQR, MPC) see little change until attitude authority becomes the bottleneck: the
136

## Page 155

Figure 5.14: Drone tilted to compensate for the added wind disturbance.
tilt needed for the path plus the tilt needed to reject wind must remain below the
platform limit that the ﬂight controller enforces. On the M300 RTK this limit is
about 30◦in P/Normal mode, while the OSDK horizontal angle mode accepts up to
±35◦but the ﬂight controller clips to the drone limits. In short, wind degrades track-
ing only when the required path curvature and the wind rejection together push the
commanded attitude into saturation; otherwise the inner loop cancels the bias and
outer–loop trajectory performance remains close to nominal. Fig. 5.15 shows circular
and ﬁgure-eight trajectories under 10 m/s and 15 m/s wind for all controllers. The
ﬁgure-eight is largely unaﬀected because inner-loop stabilization compensates for the
disturbance and the commanded attitudes stay below saturation. In contrast, the
circular trajectory exhibits degraded tracking in the turns where attitude saturates;
performance recovers once the controller exits saturation.
137

## Page 156

-30
-20
-10
0
10
20
30
x
-20
-15
-10
-5
0
5
10
15
20
y
2D Trajectory Comparison (XY)
(a) Figure-8 path.
-30
-20
-10
0
10
20
30
x
-30
-20
-10
0
10
20
30
y
2D Trajectory Comparison (XY)
LQR Nominal
PID Nominal
MPC Nominal
LQR 10 m/s
PID 10 m/s
MPC 10 m/s
LQR 15 m/s
PID 15 m/s
MPC 15 m/s
Reference
(b) Circular path.
Figure 5.15: Tracking performance comparison under wind disturbances.
5.5
Conclusion
This work presented a validated hardware-in-the-loop framework for the DJI M300
RTK. The framework combines the DJI Onboard SDK (OSDK) with ROS Kinetic
running on the DJI Manifold 2-G, allowing the trajectory controllers to run in real
time on the onboard computer while interfacing with the DJI Assistant 2 simulator
for closed-loop hardware-in-the-loop evaluation. Implementation and comparison of
PID, LQR, and MPC controllers within a uniﬁed pipeline demonstrated that observed
performance diﬀerences stem primarily from tuning choices rather than fundamental
algorithmic limitations. Wind-disturbance analysis revealed that inner-loop attitude
stabilization provides substantial robustness to external perturbations. The presented
HITL workﬂow provides a practical and repeatable path for validating trajectory
control algorithms on DJI commercial platforms prior to outdoor ﬂight testing. Future
work will focus on nonlinear MPC and real-ﬂight validation.
138

## Page 157

5.6
Bibliography
[1] R. Mahony, V. Kumar, and P. Corke, “Multirotor aerial vehicles: Modeling,
estimation, and control,” IEEE Robotics & Automation Magazine, vol. 19, no. 3,
pp. 20–32, Sep. 2012. doi: 10.1109/MRA.2012.2206474.
[2] S. Bouabdallah,
P. Murrieri,
and R. Siegwart,
“Design and control of
an indoor micro quadrotor,” in Proc. IEEE Int. Conf. Robotics and Au-
tomation (ICRA),
New
Orleans,
LA,
USA,
2004,
pp.
4393–4398.
doi:
10.1109/ROBOT.2004.1302409.
[3] G. M. Hoﬀmann, H. Huang, S. L. Waslander, and C. J. Tomlin, “Quadrotor
helicopter ﬂight dynamics and control: Theory and experiment,” in Proc. AIAA
Guidance, Navigation and Control Conf., Hilton Head, SC, USA, 2007, AIAA
Paper No. 2007-6461. doi: 10.2514/6.2007-6461.
[4] M. Kamel, T. Stastny, K. Alexis, and R. Siegwart, “Model predictive control
for trajectory tracking of unmanned aerial vehicles using Robot Operating Sys-
tem,” in Robot Operating System (ROS): The Complete Reference (Volume 2).
Springer, 2017, pp. 3–39. doi: 10.1007/978-3-319-54927-9 1.
[5] P. Pounds, R. Mahony, and P. Corke, “Modelling and control of a large quadrotor
robot,” Control Engineering Practice, vol. 18, no. 7, pp. 691–699, Jul. 2010. doi:
10.1016/j.conengprac.2010.02.008.
[6] DJI, “DJI Onboard SDK Documentation,” 2026. [Online]. Available: https:
//developer.dji.com/onboard-sdk/documentation. Accessed: Jan. 10, 2026.
139

## Page 158

[7] DJI, “DJI Assistant 2 (Enterprise Series) — Download Center,”
2026.
[Online].
Available:
https://www.dji.com/downloads/softwares/
dji-assistant-2-enterprise-series. Accessed: Jan. 10, 2026.
[8] DJI,
Matrice
300
RTK
User
Manual,
May
2020.
[Online].
Available:
https://dl.djicdn.com/downloads/matrice-300/20200507/M300_RTK_
User_Manual_EN.pdf. Accessed: Jan. 10, 2026.
[9] DJI,
“DJI::OSDK::Control
class
reference
—
Onboard
SDK
API
Reference,”
2026.
[Online].
Available:
https://developer.dji.com/
onboard-api-reference/classDJI_1_1OSDK_1_1Control.html.
Accessed:
Jan. 10, 2026.
[10] DJI, “dji control.hpp — Flight control API reference (Onboard SDK),” 2026.
[Online]. Available:
https://developer.dji.com/onboard-api-reference/
dji__control_8hpp_source.html. Accessed: Jan. 10, 2026.
[11] DJI, “Telemetry topics (Subscription and Broadcast) — Onboard SDK
API Reference,” 2026. [Online]. Available:
https://developer.dji.com/
onboard-api-reference/group__telem.html. Accessed: Jan. 10, 2026.
[12] DJI, “Manifold 2 — Speciﬁcations,” 2026. [Online]. Available: https://www.
dji.com/manifold-2/specs. Accessed: Jan. 10, 2026.
[13] DJI, “Onboard-SDK-ROS: Oﬃcial ROS packages for DJI Onboard SDK,”
2026. [Online]. Available:
https://github.com/dji-sdk/Onboard-SDK-ROS.
Accessed: Jan. 10, 2026.
140

## Page 159

[14] M. Quigley et al., “ROS: An open-source Robot Operating System,” in
ICRA Workshop on Open Source Software, Kobe, Japan, May 2009, pp. 1–6.
Available:
https://robotics.stanford.edu/~ang/papers/icraoss09-ROS.
pdf (Accessed: Jan. 10, 2026).
[15] M. A. Ahsan, H. Z. I. Khan, J. Rajput, and J. Riaz, 2022, “Active disturbance
rejection control of a quadrotor: A comparative study,” Proc. 19th Int. Bhur-
ban Conf. Applied Sciences and Technology (IBCAST), Islamabad, Pakistan,
pp. 444–450. doi: 10.1109/IBCAST54850.2022.9990161.
[16] J. A. E. Andersson, J. Gillis, G. Horn, J. B. Rawlings, and M. Diehl, “CasADi
— A software framework for nonlinear optimization and optimal control,”
Mathematical Programming Computation, vol. 11, no. 1, pp. 1–36, 2019. doi:
10.1007/s12532-018-0139-4.
[17] A. W¨achter and L. T. Biegler, “On the implementation of an interior-point ﬁl-
ter line-search algorithm for large-scale nonlinear programming,” Mathematical
Programming, vol. 106, no. 1, pp. 25–57, 2006. doi: 10.1007/s10107-004-0559-y.
141

## Page 160

Chapter 6
Conclusion and Future Work
This thesis addressed fundamental challenges in UAV trajectory planning and control
through three complementary contributions: a geometric disturbance observer-based
nonlinear model predictive control framework for robust trajectory tracking, a time-
eﬃcient convex trajectory optimization method for ﬁxed-wing UAVs in obstacle-dense
environments, and a comprehensive hardware-in-the-loop validation framework for
commercial UAV platforms.
6.1
Summary of Contributions
6.1.1
Geometric Disturbance Observer-Based NMPC
Chapter 3 presented a uniﬁed framework combining geometric state and six-DOF dis-
turbance estimation with disturbance-aware NMPC for quadrotor trajectory tracking.
The key innovation integrates an extended-state extended Kalman ﬁlter formulated
on the SO(3) manifold with an NMPC that embeds disturbance estimates as time-
142

## Page 161

varying inputs within the prediction model. Unlike existing approaches that apply
disturbance compensation as feedforward terms after optimization, this framework
embeds six-DOF disturbance estimates directly into the prediction model, enabling
proactive anticipation of disturbance eﬀects. Simulation results demonstrated an av-
erage 60% reduction in position RMSE compared to baseline NMPC, maintaining
58% reduction even under tenfold increases in measurement noise.
6.1.2
Time-Eﬃcient Trajectory Planning in Safe Convex Cor-
ridors
Chapter 4 addressed computational scalability limitations of global convex decompo-
sition methods through a framework combining time-eﬃcient corridor generation with
uniﬁed convex trajectory optimization. The corridor generation algorithm constructs
overlapping convex regions greedily along a bidirectional RRT reference path, achiev-
ing signiﬁcantly faster computation than workspace-wide IRIS-based methods. The
optimization formulation exploits diﬀerential ﬂatness to cast the complete trajectory
planning problem as a single convex quadratic program, guaranteeing collision-free
and dynamically feasible solutions without subsequent nonlinear reﬁnement. Experi-
mental validation demonstrated 36% reduction in traversal time with 17Ö computa-
tional speedup over Graph of Convex Sets baseline, and achieving 99.4% success rate
across 1,001 randomized scenarios.
143

## Page 162

6.1.3
Hardware-in-the-Loop Validation Framework
Chapter 5 presented a comprehensive HITL testing framework for the DJI M300 RTK
platform. The framework integrates the DJI Manifold 2-G onboard computer with the
M300 RTK ﬂight controller through the DJI Onboard SDK, enabling real-time execu-
tion of trajectory control algorithms within the DJI Assistant 2 simulator. Successful
implementation and validation of PID, LQR, and MPC controllers demonstrated the
framework’s capability to validate advanced control algorithms on commercial plat-
forms under realistic hardware constraints before outdoor deployment.
6.2
Publications
The work in this thesis resulted in the following publications:
 M. A. Ahsan, O. De Silva, G. K. I. Mann, R. G. Gosine, and A. Jayasiri,
“Geometric Disturbance Observer Based Nonlinear Model Predictive Control
of a Quadrotor,” ASME Letters in Dynamic Systems and Control, vol. 6, no.
1, p. 011010, January 2026. doi:10.1115/1.4069922.
 M. A. Ahsan, “Convex Trajectory Optimization for UAVs using Diﬀerential
Flatness and B´ezier Curves,” 33rd Annual Newfoundland Electrical and Com-
puter Engineering Conference (NECEC 2024), St. John’s, NL, Canada, Novem-
ber 14, 2024 (conference presentation).
 Time-Eﬃcient Trajectory Planning for UAVs in Safe Convex Corridors using
Diﬀerential Flatness Constrained Convex Optimization, has been submitted to
IEEE Access.
144

## Page 163

 Hardware-in-the-Loop Implementation and Validation of Trajectory Control Al-
gorithms for DJI M300 RTK using DJI OSDK and ROS, to be submitted to
ASME Letters in Dynamic Systems and Control.
6.3
Future Work
The research presented in this thesis has several potential future extensions. These
future developments aim to generalize the results and improve their practicality.
6.3.1
Extensions to Disturbance-Aware Predictive Control
 Develop a closed-loop stability proof for the proposed ES-EKF-based NMPC
architecture using input-to-state stability (ISS) theory or Lyapunov-based meth-
ods to establish formal convergence guarantees under bounded disturbances.
 Extend the disturbance modeling framework to incorporate higher-order distur-
bance models.
 Integrate the geometric disturbance observer-based NMPC controller into the
HITL framework developed in Chapter 5, enabling systematic validation of the
disturbance-aware control architecture on the DJI M300 RTK platform within
the DJI Assistant 2 simulator environment prior to ﬂight testing.
 Conduct ﬂight experiments using motion capture systems (e.g., OptiTrack) to
validate trajectory tracking performance under external disturbances and pay-
load variations, and compare experimental results against simulation predic-
tions.
145

## Page 164

6.3.2
Extensions to Convex Trajectory Planning Methods
 Reformulate the trajectory optimization problem to include time as a decision
variable within the convex program, enabling time-optimal trajectory genera-
tion while maintaining convexity through appropriate constraint reformulations.
 Develop convex approximations for lateral and tangential acceleration con-
straints derived from the ﬁxed-wing UAV dynamics and incorporate these con-
straints directly into the B´ezier control-point-based optimization framework.
 Extend the safe corridor generation and convex trajectory optimization frame-
work to three-dimensional environments.
 Incorporate dynamic obstacle avoidance capabilities into the trajectory plan-
ning formulation, enabling real-time replanning in environments with moving
obstacles.
6.3.3
Expansion of HITL Testing Capabilities
 Integrate the geometric disturbance observer-based NMPC controller from Chap-
ter 3 into the HITL framework, evaluating computational performance, real-
time feasibility, and tracking accuracy on the Manifold 2-G embedded platform
within the DJI Assistant 2 simulator.
 Investigate learning-based control approaches, for implementation within the
HITL framework, assessing their performance relative to model-based methods
under varying ﬂight conditions and disturbance proﬁles.
146

## Page 165

 Transition from HITL simulation to ﬂight testing on the DJI M300 RTK plat-
form, validating the complete integrated control and trajectory planning frame-
work under real-world operational conditions.
147
