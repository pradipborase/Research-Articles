# Robust Attitude Control of Nonlinear UAV Dynamics with LFT Models and H∞ Performance.pdf

## Page 1

Robust Attitude Control of Nonlinear UAV
Dynamics with LFT Models and H∞Performance
Tanay Kumar
Raktim Bhattacharya
Aerospace Engineering, Texas A&M University,
College Station, TX, 77843-3141.
Abstract—Attitude stabilization of unmanned aerial vehicles
in uncertain environments presents significant challenges due
to nonlinear dynamics, parameter variations, and sensor lim-
itations. This paper presents a comparative study of H∞and
classical PID controllers for multi-rotor attitude regulation in
the presence of wind disturbances and gyroscope noise. The
flight dynamics are modeled using a linear parameter-varying
(LPV) framework, where nonlinearities and parameter varia-
tions are systematically represented as structured uncertainties
within a linear fractional transformation formulation. A robust
controller based on H∞formulation is designed using only gyro-
scope measurements to ensure guaranteed performance bounds.
Nonlinear simulation results demonstrate the effectiveness of the
robust controllers compared to classical PID control, showing
significant improvement in attitude regulation under severe
wind disturbances.
Keywords—LFT Modeling, LPV Systems, H∞Optimal Con-
trol, Flight Control.
I. INTRODUCTION
Unmanned Aerial Vehicles (UAVs) have seen rapid adop-
tion across diverse sectors, driving increased demands for
robust control systems. Complex missions involving urban
navigation, multi-agent coordination, and beyond-visual-line-
of-sight operations present challenges that conventional con-
trol approaches struggle to address. These applications face
significant disturbances, including atmospheric turbulence,
wind gradients, mass distribution variations, sensor impreci-
sion, and model uncertainties. Robust control methodologies
are therefore essential to maintain stability and performance
under such perturbations. Recent statistical analyses confirm
this need, showing increased incidents related to control
system failures in UAV operations [1].
Linear controllers remain predominant in practical im-
plementations due to their analytical tractability and com-
putational efficiency. Proportional-Integral-Derivative (PID)
control structures, particularly in cascaded configurations, are
extensively deployed in industry [2]; however, their single-
input-single-output (SISO) formulation inherently neglects
multi-axis coupling effects and relies on heuristic tuning pro-
cedures, rendering them susceptible to parametric uncertain-
Graduate Student, ktanay@tamu.edu
Professor, raktim@tamu.edu
ties and exogenous disturbances [3], [4]. Gain scheduling par-
tially compensates for nonlinearities by adapting controller
parameters across the operational envelope, yet this approach
provides only incremental improvements in robustness while
necessitating extensive empirical calibration [5], [6].
Linear Quadratic Regulators (LQR) provide a mathemati-
cally optimal control framework that minimizes a quadratic
cost function, balancing state regulation performance against
control effort. Despite their theoretical optimality, LQR
implementations suffer from two critical limitations: they
require full state feedback, necessitating state estimation
in practical applications, and they lack inherent robustness
guarantees against parametric uncertainties. When system
dynamics deviate from the nominal model – a common
occurrence in aerial vehicles due to aerodynamic effects and
mass distribution changes – LQR performance deteriorates
significantly. Additionally, the state estimation typically relies
on Kalman filtering, which achieves optimality only under
Gaussian noise assumptions. Furthermore, LQR controllers
commonly exhibit longer response times than their PID
counterparts, despite their theoretical optimality properties
[7].
Nonlinear control methodologies have been proposed
to address the limitations above. Backstepping techniques,
founded on recursive Lyapunov stability theory, offer en-
hanced robustness to matched uncertainties. However, their
implementation yields controllers of elevated structural com-
plexity with substantial computational overhead and pa-
rameter sensitivity, thus imposing practical constraints on
real-time applications [6]. Feedback linearization approaches
transform nonlinear dynamics into equivalent linear systems
via nonlinear state transformations and control laws. Yet,
these methods exhibit pronounced sensitivity to modeling er-
rors and measurement noise, consequently compromising ro-
bustness margins [6]. Adaptive control frameworks facilitate
online parameter estimation and controller reconfiguration to
mitigate parametric uncertainties. Nevertheless, several chal-
lenges persist, including parameter convergence rates under
time-varying conditions, susceptibility to measurement noise,
and analytical complexity in establishing uniform stability
guarantees. While these nonlinear methodologies demon-
arXiv:2510.00208v2  [eess.SY]  12 Mar 2026

## Page 2

strate theoretical superiority over linear control architectures
under nominal conditions, they frequently encounter imple-
mentation barriers on resource-constrained UAV platforms
and lack rigorous performance guarantees under structured
uncertainties and bounded disturbances.
These limitations have motivated the development of ro-
bust control frameworks, particularly H∞control [8], which
provides rigorous stability guarantees under bounded pa-
rameter variations by representing system uncertainties as
norm-bounded operators and minimizing worst-case induced
norms without requiring precise disturbance characterization.
These methodologies have gained significant traction across
aerospace applications, with recent literature demonstrating
their effectiveness for tailsitter UAVs under severe turbulence
[9], helicopter control with certified performance bounds
[10], and resource-constrained implementations that sub-
stantially outperform traditional PID architectures despite
computational limitations [11].
A key advantage of robust control frameworks lies in
their compatibility with Linear Parameter-Varying (LPV)
modeling, which enables exact representation of nonlinear
dynamics without local linearization or approximation [12].
The rotational dynamics of multi-rotors contain trigonomet-
ric and rational expressions that can be modeled precisely
using static nonlinear operators, which are then treated as
structured, bounded uncertainty blocks within the Linear
Fractional Transformation (LFT) formalism. This represen-
tation maintains the full fidelity of the nonlinear dynamics
while enabling systematic controller synthesis via the H∞
technique.
The LPV-LFT approach effectively bridges the gap be-
tween high-fidelity dynamic modeling and tractable robust
control design by encapsulating nonlinearities as parameter-
dependent terms around a linear time-invariant core. This
framework embeds parameter variations directly into the
synthesis process rather than treating them as afterthoughts,
offering formal robustness guarantees against structured un-
certainties. The resulting controllers maintain stability and
performance across the entire operating envelope without re-
quiring gain scheduling or extensive empirical tuning, making
them particularly suitable for autonomous systems operating
in uncertain environments.
The effectiveness of LFT-based modeling has been demon-
strated across aerospace applications, including NASA’s sta-
bility margin assessments [13] and ESA’s spacecraft attitude
control [14]. LPV approaches extend beyond gain scheduling
by embedding parameter variations into control design, offer-
ing formal robustness guarantees [15], [16]. While synthesis
methods typically use linear matrix inequalities [17], [18],
challenges remain in representing nonlinear dependencies, of-
ten requiring probabilistic solutions [19], [20]. Nevertheless,
LPV-LFT approaches have achieved success in applications
from reconfigurable flight control to polynomially parameter-
ized stability analysis [21], [22], [23], [24], motivating this
work’s robust control framework for aerospace systems.
A. New Contributions
This paper addresses significant challenges in robust multi-
rotor stabilization by advancing the application of structured
uncertainty frameworks to nonlinear multi-rotor flight dy-
namics. The contributions of this work are threefold:
1) We establish a systematic framework for representing
multi-rotor nonlinear dynamics within the LFT formal-
ism, enabling rigorous treatment of trigonometric non-
linearities and parameter-dependent terms as structured
uncertainties.
2) We develop and validate robust control synthesis tech-
niques that utilize H∞methodology for attitude stabi-
lization under significant external disturbances, utiliz-
ing only gyroscope measurements with explicit char-
acterization of state-dependent sensor noise.
3) We provide a comprehensive comparative analysis be-
tween classical PID and robust control approaches,
quantifying performance improvements regarding dis-
turbance rejection capabilities and control effort opti-
mization under wind turbulence conditions representa-
tive of practical operating environments.
This work studies the nonlinear flight dynamics of a mul-
tirotor aerial vehicle within a structured uncertainty frame-
work. The equations of motion considered in this paper
correspond to the standard nonlinear rigid-body dynamics
commonly used for generic UAV platforms. The formulation
is not specific to any particular vehicle configuration and it
represents a general multirotor model. The numerical param-
eter values used in simulations correspond to a representative
vehicle for evaluation. Building on this modeling framework,
this work advances the application of structured uncertainty
frameworks in UAV control by integrating LPV-LFT model-
ing with robust synthesis techniques. Unlike approaches that
rely on linearization approximations, our methodology pre-
cisely captures system nonlinearities while incorporating re-
alistic sensor limitations. The proposed framework addresses
fundamental challenges in existing multi-rotor controllers by
providing formal robustness guarantees against parametric
uncertainties and exogenous disturbances, thereby bridging
theoretical control design with practical implementation con-
straints.
II. LPV MODELING OF MULTI-ROTOR SYSTEMS
A. Dynamics
We consider the classical multi-rotor UAV dynamics de-
rived from the Newton-Euler equations. Since this work
focuses on robust stabilization, the analysis is restricted to
the rotational dynamics of the vehicle, while the translational
motion is omitted. The nonlinear equations of motion for the

## Page 3

rotational dynamics of a multi-rotor UAV are given in [9]
with ZYX Euler sequence:


˙ϕ
˙θ
˙ψ

=


1
sin ϕ tan θ
cos ϕ tan θ
0
cos ϕ
−sin ϕ
0
sin ϕ sec θ
cos ϕ sec θ




p
q
r

,
(1)


˙p
˙q
˙r

=


Iy−Iz
Ix
rq + L
Ix
Iz−Ix
Iy
pr + M
Iy
Ix−Iy
Iz
pq + L
Iz

,
(2)
where

ϕ
θ
ψ
⊤are Euler angles,

p
q
r
⊤are an-
gular rates in the body frame, blkdiag(Ix, Iy, Iz) is the
inertia matrix, and

L
M
N
⊤are the roll, pitch, and
yaw moments generated by the propellers.
The nonlinearities in Eqn. (1)-(2) arise from trigonometric
and state-dependent product terms. To streamline the robust
controller synthesis, these dynamics are expressed in LPV
form as


˙ϕ
˙θ
˙ψ
˙p
˙q
˙r


= J


0
0
0
1
ρ1ρ3
ρ4
ρ2ρ3
ρ4
0
0
0
0
ρ2
−ρ1
0
0
0
0
ρ1
ρ4
ρ2
ρ4
0
0
0
0
ρ7
2
ρ6
2
0
0
0
ρ7
2
0
ρ7
2
0
0
0
ρ6
2
ρ5
2
0




ϕ
θ
ψ
p
q
r


+


0
0
0
0
0
0
0
0
0
1
Ix
0
0
0
1
Iy
0
0
0
1
Iz




L
M
N

,
(3)
where the parameters are defined as


ρ1
ρ2
ρ3
ρ4

=


sin ϕ
cos ϕ
sin θ
cos θ

,


ρ5
ρ6
ρ7


=


p
q
r

,
(4)
and J = blkdiag(I3×3, Iy−Iz
Ix
, Iz−Ix
Iy
, Ix−Iy
Iz
) is the inertia
multiplier matrix. The formulation is linear in the states but
nonlinear in the parameter set ρ. The parameters are bounded
by trigonometric identities and actuator constraints, i.e., ρ ∈
[ρmin, ρmax].
B. Measurement Model and Sensor Noise
In practice, the onboard IMU sensors provide only an-
gle rate measurements. Therefore, we consider only the
gyroscopic sensor measurements in the robust controller
synthesis. Accordingly, the measurement model is
ym =


0
0
0
1
0
0
0
0
0
0
1
0
0
0
0
0
0
1




ϕ
θ
ψ
p
q
r


+ ν,
(5)
where ν represents the noise of the gyroscopic sensor.
While the measurement model is linear, practical IMU
noise exhibits frequency-dependent characteristics due to
internal sensor dynamics and filtering components. This be-
comes particularly problematic during aggressive maneuvers,
where signal and noise frequency content overlap substan-
tially. To accurately capture these effects within our robust
control framework, sensor noise is shaped by frequency-
dependent weights, which characterize the spectral distribu-
tion of measurement noise.
ν = blkdiag(Wϕ(jω), Wθ(jω), Wψ(jω))¯ν
(6)
where ¯ν is unit-norm exogenous noise, and Wϕ,θ,ψ(jω) are
frequency-dependent weighting functions, typically modeled
using the sensor noise characteristics provided by the manu-
facturer.
C. Robust Control Problem as an LFT Interconnection
The multi-rotor dynamics in Eqn. (3), together with the
measurement model in Eqn. (5)-(6), can be expressed in the
LPV state-space form
˙x = A(ρ)x + Bu(ρ)u + Bww,
(7a)
ym = Cy(ρ)x + Du(ρ) + Dww,
(7b)
z = Czx + Dzu,
(7c)
where x is the state vector, ym is the measured output, and
w is the exogenous input that includes sensor noise and
disturbance. z represents the regulated outputs that need to
be minimized, which in our case is the attitude error and
actuator efforts. The vector ρ represents the LPV parameters
given in (4). The system matrices are nonlinear functions of
ρ.
The control objective is to design an output-feedback con-
troller K that regulates z based on the available measurement
ym, while ensuring robust stability and performance against
parameter variations ρ and exogenous disturbances w. This
is achieved by embedding the system into the generalized
interconnection shown in Fig. 1, where weighting functions
Wr,d,u,n map the physical design specifications into the H∞
framework.
These weights shape the frequency response and capture
actuator bandwidth limits, noise spectra, and disturbance
rejection requirements that are not directly visible in the
raw signals. Moreover, the exogenous inputs are normalized

## Page 4

as unit-norm bounded, ensuring that the H∞optimization
problems remain well-posed, with performance guarantees
scaling proportionally with disturbance magnitudes.
Wr
K
P
Σ
Wn
Wd
Wu
˜n
˜r
˜u
˜d
u
y
n
+
+
Figure 1: System interconnection for designing and
implementing proposed controllers.
Formally, the objective is to define a tunable state space
model of the controller to minimize
∥z∥2 = ∥Tw→z(s)∥H∞,
(8)
where Tw→z is the closed-loop transfer matrix from w
to z. The H∞objective ensures attenuation of worst-case
disturbances, while accounting for structured uncertainties in
ρ.
To synthesize the controller, the nonlinear parameter de-
pendence in Eqn. (7) is expressed as an LFT interconnection
(Fig. 2) by treating the ρ terms as structured uncertainty
blocks. In MATLAB’s Robust Control Toolbox, this is imple-
mented by declaring ρ as ureal objects, automatically con-
structing the uncertainty blocks for LFT-based analysis. The
controller K is then synthesized using hinfstruct(...)
or hinfsyn(...).
blkdiag(ρ1In1, ..., ρ7In7)
P
K
w
˜u
˜z
˜ym
Figure 2: LFT interconnection for designing robust
controllers.
A key technical challenge in the LFT formulation is that
the nominal plant contains poles at the origin, a characteris-
tic feature of multi-rotor dynamics due to their free-body
rotational modes. These poles violate the well-posedness
conditions required for standard H∞optimization. To address
this issue, we implement stability augmentation through min-
imal viscous aerodynamic/motor damping terms that shift the
poles slightly into the left-half plane. This modification has
a negligible effect on the physical fidelity of the model but
renders the optimization problem mathematically tractable.
III. SIMULATION RESULTS
A. Design Parameters
For robust control synthesis, the physical parameters of
the multi-rotor are summarized in Table I, and the parameter
bounds ρ in Eqn. (4) are determined by the operational
envelope and actuator constraints, as listed in Table II.
Table I: Physical parameters of the multi-rotor
Parameter
mass
Ix
Iy
Iz
Value
10 kg
0.25 kg·m2
0.2 kg·m2
0.1 kg·m2
Table II: Parameter bounds
Parameter
ρ1
ρ2
ρ3
ρ4
ρ5
ρ6
ρ7
ρmin
-1
0
-1
0
-1.5 r/s
-1.5 r/s
-1.5 r/s
ρmax
1
1
1
1
1.5 r/s
1.5 r/s
1.5 r/s
The plant is augmented by incorporating actuator dynamics
and weighting functions to map the physical design require-
ments into the H∞framework. The actuators are modeled
as first-order systems, and constant weighting functions are
employed. This choice simplifies the synthesis problem by
avoiding additional dynamics in the augmented plant while
capturing the relative importance of different performance
channels. The constant weights act as scaling factors that
normalize these channels, ensuring each contributes appro-
priately to the overall performance index. This augmentation
yields the standard interconnection structure shown in Fig.
1, ensuring that performance constraints are explicitly repre-
sented in the closed-loop problem.
The
controller
is
synthesized
using
MATLAB’s
hinfsyn(...), which formulates the uncertain blocks
as an upper LFT and minimizes the H∞norm of the
augmented system. The resulting controller has nine states,
corresponding to the three disturbance channels, three sensor
noise channels, and three actuator effort channels that are
jointly minimized in the performance objective. In contrast,
the cascaded SISO PID controller uses two states per axis,
for a total of six states.
The closed-loop performance achieved by the H∞con-
troller is quantified by the norm γ0 = 0.25. This indicates that
the worst-case amplification from disturbances and sensor
noise to the regulated outputs is bounded by γ0 in the in-
duced L2 sense, providing strong robustness and disturbance
attenuation guarantees.
B. Simulation Setup
Multi-rotor missions are particularly sensitive during take-
off, hover, and landing, as these phases are heavily affected
by unmodeled dynamics such as ground effects and wind
gusts. This makes crucial tasks, including VTOL and pay-
load delivery in a constrained environment, challenging. To

## Page 5

emulate these conditions, we consider a simulation in which
a multi-rotor UAV is tasked with hovering at an altitude of
10 m in the presence of strong winds.
The exogenous input vector is considered as
w(t) = [τϕ(t)
τθ(t)
τψ(t)
np
nq
nr]⊤
(9)
where τϕ,θ,ψ(t) denote disturbance torques induced by wind
gusts along the respective axes, and np,q,r(t) represent sensor
noise in gyroscopic measurements.
For validation, a nonlinear Simulink model of the complete
system is employed. In Simulink, a three-axis gyroscope
block with an SNR of 35 dB is used, representative of
commercially available MEMS IMUs. Wind disturbances are
modeled using the Dryden turbulence model, consistent with
military specifications to simulate gust velocities up to 15
m/s, corresponding to worst-case operational conditions.
For baseline comparison, a cascaded SISO PID controller
is implemented for each axis, owing to its popularity. The
gains are tuned using MATLAB’s autotune feature to en-
sure best-case PID performance. This autotuner works by
performing a frequency-response estimation experiment to
identify the system dynamics, and then calculating PID gains
based on desired performance metrics. The H∞controller is
evaluated against this benchmark.
C. Results and Discussions
The disturbance moments generated by the Dryden turbu-
lence model are shown in Fig. 3. The Dryden turbulence
model produces disturbance moments up to 0.65 N-m in
roll and pitch, corresponding to moderate-to-severe gust
conditions. This replicates practical scenarios such as payload
delivery in urban areas subject to wind shear or missions in
hilly terrain with strong localized turbulence.
=? (N-m)
-0.4
-0.2
0
0.2
0.4
0.6
=3 (N-m)
-0.3
-0.2
-0.1
0
0.1
0.2
0.3
0
10
20
30
40
50
60
=A (N-m)
-0.1
-0.05
0
0.05
0.1
Figure 3: Disturbance moments generated by wind gust and
turbulence
The closed-loop attitude trajectories under PID and H∞
controllers are presented in Fig. 4-5. Since it is a regulation
problem, the controllers reject disturbances and drive the
states to zero using only gyroscope measurements. The
results demonstrate that the robust controller achieve sig-
nificantly superior performance compared to the PID con-
troller, showing improved resilience against disturbances,
uncertainties, and measurement noise. In all cases, the errors
remain bounded, validating the robustness of the proposed
controllers against dynamic and measurement uncertainties.
?°
-10
0
10
20
30
Desired
PID
H1
3°
-10
0
10
Time (sec)
0
10
20
30
40
50
60
A°
-10
0
10
Figure 4: Euler angles (attitude) of the multi-rotor
p °/sec
-40
-20
0
20
40
Desired
PID
H1
q °/sec
-20
-10
0
10
20
Time (sec)
0
10
20
30
40
50
60
r °/sec
-20
0
20
40
Figure 5: Rotational rates of the multi-rotor
The Euler angle deviations’ peak and root mean square
error (RMSE) values are summarized in Table III. The
PID controller exhibits large deviations, with a peak error
exceeding 30◦, whereas the H∞controller reduces the error
by nearly an order of magnitude.
Table III: Errors in multi-rotor attitude using different
controllers
PID
H∞
Peak magnitude
30.54◦
7.12◦
RMSE
5.67◦
1.35◦
The control inputs required to achieve the desired states
are shown in Fig. 6. The H∞controller achieves lower
tracking errors without exerting aggressive or high-magnitude
actuator efforts. Additionally, the actuator model in the sim-
ulation ensures that the controller does not exceed actuator

## Page 6

bandwidths. Therefore, the H∞controller exhibits overall
improved performance relative to the PID controller as it
regulates the states effectively with less actuator exertion.
L (N-m)
-0.5
0
0.5
PID
H1
M (N-m)
-0.2
0
0.2
Time (sec)
0
10
20
30
40
50
60
N (N-m)
-0.1
0
0.1
Figure 6: Control Inputs
We also verified that the LPV parameters ρ(t) remain
within the assumed bounds under closed-loop operation.
Since roll and pitch are constrained to ϕ, θ ∈[ −π
2 , π
2 ],
the trigonometric scheduling terms (e.g., sin (.), cos (.)) are
naturally bounded in [−1, 1]. The states p, q, r (corresponding
to ρ5-ρ7) remain within the prescribed limits (±1.5π rad)
throughout the simulations, as confirmed by the state trajec-
tories shown in Fig. 5. No violations of the ρ bounds were
observed for the H∞controller.
IV. CONCLUSIONS
This paper presents a robust multi-rotor UAV attitude
stabilization control framework that systematically captures
nonlinear dynamics within the Linear Fractional Transfor-
mation (LFT) framework. The proposed H∞methodology
preserves full dynamic fidelity in the controller synthesis by
treating trigonometric nonlinearities and parameter variations
as structured uncertainties rather than linearization approxi-
mations. The approach utilizes only gyroscope measurements
and provides stability guarantees.
Simulation results under realistic conditions demonstrate
substantial performance improvements over classical PID
control, with significant reductions in peak attitude errors
and RMSE values under severe wind disturbances generated
by the Dryden turbulence model. These improvements are
achieved while maintaining lower actuator effort and oper-
ating with realistic gyroscope noise representative of com-
mercial MEMS IMUs. The validation confirms the practical
applicability of H∞theory for multi-rotor attitude control
in challenging missions such as urban navigation, VTOL
operations, and payload delivery in gusty environments.
REFERENCES
[1] B. Grindley, K. Phillips, K. J. Parnell, T. Cherrett, J. Scanlan, and K. L.
Plant, “Over a decade of uav incidents: A human factors analysis of
causal factors,” Applied Ergonomics, vol. 121, p. 104355, 2024.
[2] I. Lopez-Sanchez and J. Moreno-Valenzuela, “Pid control of quadrotor
uavs: A survey,” Annual Reviews in Control, vol. 56, p. 100900, 2023.
[3] C. Kasnako˘glu, “Investigation of multi-input multi-output robust con-
trol methods to handle parametric uncertainties in autopilot design,”
PloS one, vol. 11, no. 10, p. e0165017, 2016.
[4] B. Kada and Y. Ghazzawi, “Robust pid controller design for an
uav flight control system,” in Proceedings of the World congress on
Engineering and Computer Science, vol. 2, no. 1-6, 2011, pp. 1–6.
[5] A. G. Melo, F. A. Andrade, I. P. Guedes, G. F. Carvalho, A. R. Zachi,
and M. F. Pinto, “Fuzzy gain-scheduling pid for uav position and
altitude controllers,” Sensors, vol. 22, no. 6, p. 2173, 2022.
[6] N. Abbas, Z. Abbas, S. Zafar, N. Ahmad, X. Liu, S. S. Khan, E. D.
Foster, and S. Larkin, “Survey of advanced nonlinear control strategies
for uavs: Integration of sensors and hybrid techniques,” Sensors,
vol. 24, no. 11, p. 3286, 2024.
[7] A. S. Elkhatem and S. N. Engin, “Robust lqr and lqr-pi control strate-
gies based on adaptive weighting matrix selection for a uav position
and attitude tracking control,” Alexandria Engineering Journal, vol. 61,
no. 8, pp. 6275–6292, 2022.
[8] K. Zhou and J. C. Doyle, Essentials of robust control.
Prentice hall
Upper Saddle River, NJ, 1998, vol. 104.
[9] T. Kumar, M. Kothari, and R. Bhattacharya, “H∞robust control of a
quadrotor biplane tailsitter uav,” in AIAA SCITECH 2024 Forum, 2024,
p. 0318.
[10] J. Gadewadikar, F. Lewis, K. Subbarao, and B. M. Chen, “Structured
mathcalH∞command and control-loop design for unmanned heli-
copters,” Journal of guidance, control, and dynamics, vol. 31, no. 4,
pp. 1093–1102, 2008.
[11] R. Bautista-Quintero and M. J. Pont, “Implementation of h-infinity
control algorithms for sensor-constrained mechatronic systems using
low-cost microcontrollers,” IEEE Transactions on Industrial Informat-
ics, vol. 4, no. 3, pp. 175–184, 2008.
[12] T. Kumar and R. Bhattacharya, “Sparse actuation for lpv systems with
full-state feedback in H2/H∞framework,” in 2025 American Control
Conference (ACC).
IEEE, 2025, pp. 5004–5009.
[13] J.-Y. Shin and C. Belcastro, “Robustness analysis and reliable flight
regime estimation of an integrated resilient control system for a trans-
port aircraft,” in AIAA Guidance, Navigation and Control Conference
and Exhibit, 2008, p. 6656.
[14] E. Di Sotto, N. Paulino, and S. Salehi, “Integrated validation and
verification framework for autonomous rendezvous systems,” IFAC
Proceedings Volumes, vol. 43, no. 15, pp. 315–320, 2010.
[15] J. S. Shamma and M. Athans, “Analysis of gain scheduled control for
nonlinear plants,” IEEE Transactions on Automatic Control, vol. 35,
no. 8, pp. 898–907, 1990.
[16] J. S. Shamma, “An overview of lpv systems,” Control of linear
parameter varying systems with applications, pp. 3–26, 2012.
[17] L. El Ghaoui and S.-l. Niculescu, Advances in Linear Matrix Inequality
Methods in Control.
SIAM, 2000.
[18] J. W. Helton and V. Vinnikov, “Linear matrix inequality representation
of sets,” Communications on Pure and Applied Mathematics: A Journal
Issued by the Courant Institute of Mathematical Sciences, vol. 60,
no. 5, pp. 654–674, 2007.
[19] R. Tempo, G. Calafiore, F. Dabbene et al., Randomized algorithms for
analysis and control of uncertain systems: with applications. Springer,
2013, vol. 7.
[20] Y. Fujisaki, F. Dabbene, and R. Tempo, “Probabilistic design of lpv
control systems,” Automatica, vol. 39, no. 8, pp. 1323–1337, 2003.
[21] S. Ganguli, A. Marcos, and G. Balas, “Reconfigurable lpv control
design for boeing 747-100/200 longitudinal axis,” in Proceedings of the
2002 American control conference (IEEE cat. no. CH37301), vol. 5.
IEEE, 2002, pp. 3612–3617.
[22] G. J. Balas, “Linear, parameter-varying control and its application to
aerospace systems,” in ICAS congress proceedings, 2002, pp. 541–1.
[23] W. Gilbert, D. Henrion, J. Bernussou, and D. Boyer, “Polynomial lpv
synthesis applied to turbofan engines,” Control engineering practice,
vol. 18, no. 9, pp. 1077–1083, 2010.
[24] A. Marcos and S. Bennani, “Lpv modeling, analysis and design
in space systems: Rationale, objectives and limitations,” in AIAA
guidance, navigation, and control conference, 2009, p. 5633.
