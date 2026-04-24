# machines-14-00277.pdf

## Page 1

Academic Editor: Tao Li
Received: 20 January 2026
Revised: 26 February 2026
Accepted: 27 February 2026
Published: 2 March 2026
Copyright: © 2026 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license.
Article
Robust Vehicular Dynamics and Sliding Mode Control of
Multi-Rotor UAVs in Harsh Wind Fields
Umar Farid 1
, Bilal Khan 2,3
and Zahid Ullah 4,*
1
Department of Electrical Engineering, COMSATS University Islamabad, Abbottabad Campus,
Abbottabad 22060, Pakistan
2
Control and Instrumentation Engineering Department, King Fahd University of Petroleum and Minerals
(KFUPM), Dhahran 31261, Saudi Arabia
3
Center for Sustainable Energy Systems (IRC-SES), King Fahd University of Petroleum and Minerals (KFUPM),
Dhahran 31261, Saudi Arabia
4
Dipartimento di Elettronica, Informazione e Bioingegneria, Politecnico di Milano, 20133 Milan, Italy
*
Correspondence: zahid.ullah@polimi.it
Abstract
A crucial problem for autonomous aerial operations is to provide dependable and strong
control of unmanned aerial vehicles (UAVs) in adverse environmental circumstances. The
current paper provides an extensive analysis of the vehicle dynamics and control of drones
in strong wind fields with altitude-dependent wind shear, wind gusts, and turbulence. A
comparative evaluation of sliding mode control (SMC), linear quadratic regulator (LQR),
model predictive control (MPC), adaptive constrained adaptive linear control (ACALC),
and higher-order control barrier function (HOCBF)-based control in the context of trajectory
tracking performance, control effort, and robustness is carried out. Simulation outcomes
show that SMC exhibits superior robustness to sudden wind disturbances and the most
consistent tracking accuracy under stochastic variations; HOCBF and ACALC provide
comparable high precision with added constraint enforcement and adaptive capability,
respectively; MPC has smooth control and minimal energy consumption; and LQR has a
high level of computational efficiency with significantly tolerable tracking performance.
Monte Carlo calculations are conducted to measure tracking errors and control energy
under the stochastic wind variations, and the capability of the proposed control strategies
to remain resilient in uncertain conditions is brought to light. The results provide useful
information about the architecture of effective controllers used in UAVs during severe
weather conditions and underline the compromises between the accuracy of tracking,
the control effort, and the energy consumption. The suggested framework offers an
effective and scalable system suitable for reliable autonomous drone activity in complicated
reality settings.
Keywords: unmanned aerial vehicle; robust control; vehicular dynamics; harsh wind
disturbances; trajectory tracking; sliding mode control
1. Introduction
UAVs have been under rapid development in civic as well as defense sectors because
they are extremely fast, cost-efficient, and function in hazardous and inaccessible areas.
Common uses of autonomous UAV programs include aerial surveillance, environmental
surveillance, disaster recovery, precision farming, package delivery, and more, and the
high robustness and reliability of autonomous UAV programs are becoming essential. But
Machines 2026, 14, 277
https://doi.org/10.3390/machines14030277

## Page 2

Machines 2026, 14, 277
2 of 24
environmental perturbations have a great influence on the operation of UAVs; mostly,
wind gusts, turbulence, and wind shear pose major challenges to the vehicle dynamics and
control-design methodology.
Multi-rotor UAVs are highly nonlinear, lightweight, and underactuated, as far as
control is concerned. They are highly sensitive to external aerodynamic disturbances,
especially due to their low inertia and a high ratio of thrust to weight. When they develop
in severe wind conditions, the deviations can be significant in the motion, there can be
oscillatory movement, more effort in controlling, and a decrease in flight endurance. This is
further complicated by wind shear, which is variation in wind velocity that depends on the
altitude and creates spatially varying uncertainties, which cannot be easily counteracted by
traditional control strategies.
LQR and proportional-integral-derivative control (PID) are the classical control meth-
ods that are widely implemented in UAV stabilization and trajectory tracking because of
their simplicity and the fact that no special tools are required for implementation [1,2].
Although these techniques prove to be satisfactorily effective at nominal conditions of oper-
ation, they become considerably weaker when there are strong disturbances and model
uncertainties. As a result, UAVs spaced using linear controllers can have less tracking
precision or even instability with operation in turbulent wind fields [3].
In an effort to eliminate these shortcomings in tandem with a deeper insight into
optimal solutions of nonlinear control, enhanced nonlinear control methods have been
explored in depth. It is especially appealing that SMC is designed in such a way that
it can withstand matched disturbances and parametric uncertainties [4]. A number of
experiments have shown that SMC is effective in cases of UAVs in wind turbulence and
changes in the payload [5]. Nonetheless, traditional SMC is characterized by chattering
effects, implying stimulation of unconstrained dynamics and wear and tear of actuators,
leading to a decrease in energy efficiency [4].
MPC has become a strong alternative with its capability to provide a clear represen-
tation of system limitations and optimize control responses in the view of a prediction
horizon [6]. The UAV controllers configured through MPC have demonstrated good per-
formance in trajectory tracking, obstacle avoidance, and disturbance rejection [7]. How-
ever, the strength of MPC to withstand extreme and stochastic wind turbulence and the
computational viability of MPC to be implemented in real time have not been explored
through research.
Beyond tracking accuracy and stability, energy efficiency is a critical performance
metric for battery-powered UAVs. Harsh wind conditions often lead to aggressive control
actions, resulting in increased power consumption and reduced flight endurance. Despite
its practical importance, energy-sensitive evaluation is often overlooked in UAV control
studies, where the emphasis is primarily placed on minimizing tracking error [8]. Further-
more, most existing works rely on deterministic disturbance scenarios, whereas real-world
wind fields are inherently stochastic.
Driven by these problems, this paper aims to provide a detailed comparative analysis
of robust control of UAVs in severe wind conditions. SMC, LQR, and MPC are compared in
a single simulation scenario with gusts, turbulence, wind shear depending on the altitude,
and stochastic disturbances. The evaluation of performance is based on the accuracy
of tracking trajectory, robustness, control effort, and energy consumption with a solid
background of Monte Carlo simulations.
Although a complete 6-DOF Newton–Euler model has been used to characterize
rotational coupling and aerodynamic torque perturbation, the current study utilities the
hierarchical modeling representation, which is common in the quadrotor trajectory-tracking
literature. The paper is based on the assumption that a fast inner-loop attitude controller
https://doi.org/10.3390/machines14030277

## Page 3

Machines 2026, 14, 277
3 of 24
can provide the thrust vector as an effective acceleration command on the inertial frame
by decoupling the position dynamics to a two-integrator form with equal wind distur-
bances. This enables a focused, fair comparison of outer-loop controllers (SMC, LQR,
MPC) on disturbance rejection, energy efficiency, and robustness metrics under identical
stochastic wind profiles. The primary contribution of this study is: Extensions to coupled
6-DOF effects are noted as valuable future work, particularly for aggressive maneuvers or
extreme turbulence.
The primary aim of this paper is to provide a systematic, unified comparative analysis
of SMC, LQR, and MPC for multi-rotor UAV trajectory tracking under identical harsh wind
conditions. Through realistic composite interruptive disturbance modeling and Monte
Carlo statistics analysis, we process not only tracking precision and robustness but also
control productivity together with energy taxation, which provides obvious trade-off un-
derstanding about operational controller choice in inauspicious settings. While individual
controllers have been studied, such a multi-metric, statistically rigorous benchmark under
the same challenging stochastic wind profile is largely absent in the literature. Results
are simulation-based to establish baseline performance before real-platform deployment;
experimental validation is discussed as future work.
To permit such a fair comparison, we construct a high-fidelity wind model, based
upon: (i) power-law altitude-dependent shear, (ii) Dryden continuous turbulence with
natural scales of intensity and length scales, and (iii) randomly killed deterministic gusts.
This testbed is more representative of actual low-altitude wind fields in the real world than
a lot of the previous models and is the basis of our evaluations.
More recent developments have proposed more advanced disturbance rejection and
constrained control in UAVs and their associated systems, such as learning-based on finite-
times/fixed-time [9], adaptive critic designs [10], path-following through fuzzy disturbance
observers [11], and safety-certified through control barrier function formation control [12].
Although such methods also demonstrate promise to perform uncertainty, constraint, and
multi-agent coordination tasks, they are often significantly better at performing these tasks
in particular cases (e.g., faster convergence, or safety in hypersonic aircraft), but they are also
much more commonly applied to different problem domains, such as elliptical encircling,
formation flying, or hypersonic aircraft attitude control. A more direct integration or
comparison would demand more specific extensions than the capability at the current
paper to expect in the study under severe wind of a UAV-trajectory situation, though
they would inspire future hybrid development to harness the strengths of SMC and the
adaptive/learning features to their benefit.
The rest of the paper is organized as follows: Section 2 explains the literature review
and identifies the research gaps; Section 3 explains the detailed vehicular dynamic and
problem formulation. Detailed controller design and stability analysis are explained in
Section 4. Section 5 presents the detailed simulation of the paper, and Section 6 gives
concluding remarks and future directions.
2. Literature Review
Early research on UAV control primarily focused on linearized models and classi-
cal controllers. LQR-based approaches were proposed for multi rotor stabilization and
trajectory tracking, demonstrating acceptable performance under mild disturbances [13].
However, these methods rely on near-hover assumptions and offer limited robustness
against strong environmental uncertainties.
Robust control techniques, particularly SMC, have been extensively studied for UAV
applications. In [14], SMC can effectively reject wind disturbances and model uncertain-
ties. Advanced variants such as higher-order and adaptive SMC have been proposed
https://doi.org/10.3390/machines14030277

## Page 4

Machines 2026, 14, 277
4 of 24
to mitigate chattering effects [15]. Despite these advancements, a fundamental trade-off
between robustness and smooth control action persists, especially under highly turbulent
wind conditions.
In recent years MPC has received much attention. Some of the projects have used
MPC in UAV trajectory tracking challenges and in disturbance rejection issues [16]. In [17],
MPC was demonstrated to be better than PID and LQR controllers in restricted conditions.
Nevertheless, in the majority of MPC-studies, it is discovered that simplified wind models,
or deterministic models, are employed, which fail to explicitly take into consideration wind
shear or stochastic turbulence. Moreover, the strength and computational efficiency in
severe disturbances are not addressed well.
There is a considerable variation of wind modelling fidelity in the literature. Whereas
in some studies the wind disturbances are constant or sinusoidal [18], in others they are
stochastic gust models [19]. Nonetheless, the altitude-dependent wind shear, especially
when considering low altitude UAV operations, has been given rather a low consideration.
Energy consumption analysis is yet another field that is not fully explored. Though
some of the works have explored the use of energy-efficient UAV control mechanisms,
they are usually ignoring severe environmental perturbations or only consider trajectory
optimization instead of closed-loop strength.
Monte Carlo-based robustness assessment has been utilised in few UAV research and
is mainly used to analyze parameter uncertainty [20]. It has limited application to stochastic
wind disturbance evaluation and controllers comparison. Moreover, a unified comparative
analysis of SMC, LQR, and MPC under identical harsh wind conditions, including energy
efficiency metrics, is largely absent from the existing literature.
Despite significant progress in UAV control under disturbance-prone environments,
several critical research gaps remain. First, existing studies predominantly investigate
individual control strategies in isolation, resulting in a lack of unified and fair compar-
ative analyses of classical optimal control (LQR), robust nonlinear control (SMC), and
optimization-based control (MPC) under identical harsh wind conditions. Second, most
wind disturbance models employed in the literature are either deterministic or spatially
uniform, thereby neglecting altitude-dependent wind shear effects that are particularly
relevant for low-altitude UAV operations in urban and complex terrains. Third, although
robustness and accuracy of trajectory tracking are commonly cited, the energetic cost of
disturbance rejection is also rarely quantified despite its paramount importance to the UAV
battery-powered endurance and mission sustainability. Moreover, the fact that real whirl-
wind fields are stochastic is frequently ignored, and data on Monte Carlo-based robustness
assessment frameworks is not widely adopted, which could give a statistically significant
view of controller reliability. Finally, a coherent performance assessment framework in
which robustness, tracking performance, control effort, and energy efficiency are collec-
tively evaluated does not exist often, restricting the usefulness of the currently known
control solutions to the deployment of UAVs into harsh environments.
In parallel, emerging works have explored advanced nonlinear and learning-based
strategies for improved disturbance rejection and constrained UAV/multi-agent control.
Finite-time learning-based optimal control has been applied to elliptical encircling tasks for
UAVs with prescribed constraints, integrating reinforcement learning approximations to
handle uncertainties [21] Fixed-time collision-free coordination for multi-UAV [22] ensures
convergence independent of initial conditions while avoiding collisions. Adaptive critic
methods without back stepping have been developed for attitude control under large
uncertainties in hypersonic morphing vehicles [23], and concurrent-learning adaptive
critics address multi-robot formation under safety constraints [24]. Fuzzy-based quantized
observers enable efficient path-following for consumer UAVs in logistics under disturbance
https://doi.org/10.3390/machines14030277

## Page 5

Machines 2026, 14, 277
5 of 24
constraints [25], while high-order control barrier functions provide safety-certified optimal
formation for nonlinear multi-agents [26]. State-constrained adaptive fuzzy exact tracking
has also been enhanced for general strict-feedback nonlinear systems [27].
These developments highlight the trend toward adaptive, finite/fixed-time, and safety-
aware control with learning components for better robustness and performance guarantees.
However, most focus on formation, encircling, or attitude problems rather than single
quadrotor position trajectory tracking in stochastic wind shear and gusts. Moreover, com-
prehensive energy consumption and Monte Carlo robustness evaluations under identical
harsh wind profiles remain limited in these works. The current paper therefore fills this gap
because it brings on the same platform a comparative baseline of existing robust and best
approaches, which will lead to the ultimate incorporating of such advanced techniques.
In general, the key contributions of this paper are as follows:
•
Development of a realistic harsh wind model incorporating gusts, turbulence, and
altitude-dependent wind shear;
•
Systematic comparison of SMC, LQR, and MPC for UAV vehicular dynamics under
identical disturbance conditions;
•
Monte Carlo-based robustness analysis for statistically meaningful performance evaluation.
3. Vehicular Dynamics and Problem Formulation
3.1. UAV Translational Dynamics
Consider a quadrotor UAV operating in a three-dimensional inertial frame
FI = {OI, xI, yI, zI}. The translational motion of the UAV center of mass is described
by the following second-order nonlinear dynamics:
m ¨p(t) = u(t) + fw(p, t).
(1)
In (1), f p(t) = [x(t), y(t), z(t)]⊤∈R3 denotes the position vector of the UAV, m ∈R+
is the mass, f u(t) ∈R3 represents the collective thrust vector expressed in the inertial frame,
and fw(p, t) denotes the resultant aerodynamic disturbance force induced by wind effects.
This modeling choice is standard in the UAV control literature for position/trajectory
tracking under wind disturbances, as it isolates outer-loop performance while relying on
proven inner-loop attitude stabilization. Wind-induced attitude perturbations are assumed
to be rejected by the inner loop; residual coupling effects are secondary for the moderate
wind intensities.
It is a standard modeling choice to represent the translational dynamics in the form
of a double-integrator, used in the literature of quadrotor UAV control. It supposes a
hierarchical control system with a fast inner-loop attitude controller of the thrust vector,
making it virtually an acceleration command in the inertial frame, uncoupling the position
dynamics with the nonlinear attitude coupling. This simplification can effectively compare
(outer-loop) position controllers (SMC, LQR, MPC) on disturbance rejection and energy
quantities without generating loss of generality when tracking a trajectory in the wind,
while maintaining the model control oriented and manageable. Equation (1) explains
the fundamental Newton–Euler translational dynamics, where the UAV acceleration is
governed by the applied thrust and external wind-induced forces.
3.2. State-Space Representation
Define the system state vector as
x(t) =
"
p(t)
˙p(t)
#
∈R6.
(2)
https://doi.org/10.3390/machines14030277

## Page 6

Machines 2026, 14, 277
6 of 24
Then, the translational dynamics can be rewritten in first-order state-space form as
˙x(t) =
"
03×3
I3×3
03×3
03×3
#
|
{z
}
A
x(t) +
"
03×3
1
mI3×3
#
|
{z
}
B
u(t) + d(p, t).
(3)
In (3), d(p, t) = [0⊤
3×1 f ⊤
w (p, t)/m]⊤denotes the matched disturbance vector.
UAV translational dynamics in a linear time-invariant (LTI) structure, additive
matched disturbance form, which is critical to coherent comparison of controllers is ex-
plained in (3).
Remark 1. The linear double-integrator structure in state-space form facilitates direct application
and comparison of linear (LQR), predictive (MPC), and robust nonlinear (SMC) methods on the
same matched-disturbance channel, consistent with common UAV position control practices.
3.3. Harsh Wind and Wind Shear Modeling
3.3.1. Wind Decomposition
The total wind disturbance is modeled as a superposition of mean wind, gust, turbu-
lence, and altitude-dependent shear components:
vw(p, t) = vm + vg(t) + vt(t) + vs(z).
(4)
In (4), vm denotes the steady mean wind, vg(t) represents deterministic gusts, vt(t)
models stochastic turbulence, and vs(z) captures vertical wind shear.
This decomposition gives the true behavior of the atmosphere, and each element of
disturbance is analyzed separately.
3.3.2. Stochastic Turbulence and Gust Parameters
The stochastic turbulence component vt(t) is generated using the Dryden continuous
turbulence model [28] This model approximates the power spectral densities for longitudi-
nal, lateral, and vertical components with turbulence intensity σt = 1.5–3.0 m/s (light-to-
moderate turbulence) and length scales Lt = 50–150 m (adjusted for low-altitude quadrotor
relevance). Deterministic gusts vg(t) are superimposed as discrete pulses (1-cosine or ex-
ponential shapes) with peak amplitudes up to 5–8 m/s, occurring at irregular intervals and
randomized per Monte Carlo run. These parameters produce realistic deviations consistent
with observed UAV behavior in gusty urban/coastal environments.
3.3.3. Altitude-Dependent Wind Shear
The wind shear component is defined as
vs(z) = ks
 z
z0
α
.
(5)
In (5), ks ∈R3 is the shear intensity vector, z0 is a reference altitude, and α > 0 is the
shear exponent.
The non-linear way of the wind velocity increasing with the altitude, which is regarded
as typical of the low-altitude atmospheric boundary layer, is explained in (5).
3.3.4. Physical Motivation and Justification of Components
The composite model reflects realistic low-altitude atmospheric boundary layer (ABL)
physics relevant to UAV operations (urban, coastal, and disaster zones). Altitude-dependent
wind shear (power-law form, (5)) arises from surface friction and terrain effects, causing
wind speed to increase with height; typical shear exponent α ≈0.1–0.3 over land, higher in
https://doi.org/10.3390/machines14030277

## Page 7

Machines 2026, 14, 277
7 of 24
complex terrain. Dryden turbulence is continuous, Gaussian, stationary random turbulence
in the form of rational power spectral densities, which are easy to simulate (white noise
filtering); common values: turbulence intensity, σ t = 1.530 m/s (light-moderate); length
scales, L t = 50,150 m low-altitude quadrotor. The sudden bursts (peaks 5 to 8 m/s) used in
the deterministic gusts (1-cosine/exponential) model are typical of the real world. Linear
drag = 0.5 v 0.5 kg/s in nominal conditions. The combined effect of density, area, and coef-
ficient is contained in the nominal force that is approximated by the linear drag = 0.5 c d v
0.5 kg/s per corridor of aerodynamic force = F w 0.5 kg/s: c d v 0.5 kg/s kg/s is the
drag coefficient and v w is the wing coordinate velocity. This allows matched-disturbance
analysis but will result in realistic deviations (meters in 510 m/s gusts).
3.3.5. Aerodynamic Disturbance Force
The wind-induced disturbance force is approximated as
fw(p, t) = cd vw(p, t).
(6)
In (6), cd > 0 is an equivalent drag coefficient. This linear relationship represents
a first-order approximation of the aerodynamic drag force commonly used in quadrotor
UAV control and disturbance rejection [29]. In full generality, aerodynamic drag follows
the quadratic law fw ≈1
2ρcdA∥vw∥vw, where ρ is air density, cd is the dimensionless drag
coefficient, and A is the effective projected frontal area. However, for moderate wind
speeds and control-oriented modeling, the linear form fw = cdvw is widely adopted as an
equivalent matched disturbance. The lumped parameter cd encapsulates the combined
effects of 1
2ρcdA (with militarization around nominal conditions). The value of cd can be
estimated via wind-tunnel tests, flight data identification, or geometry-based calculation
(typical range for small quadrotor: cd ≈0.5–2.0 kg/s depending on size and attitude).
In our simulations, cd is tuned to produce realistic force magnitudes leading to position
deviations of several meters in gusts of 5 to 10 m/s, consistent with reported wind effects.
This representation of the affine disturbance is largely used in the robust control
analysis and guarantees the correspondence of the disturbance to the control input.
Remark 2. The disturbance fw(p, t) enters the system through the same channel as the control
input, satisfying the matched disturbance condition required for sliding mode robustness analysis.
3.4. Wind-Induced Torque Disturbances via Blade Flapping
In full 6-DOF modeling, wind induces attitude torques primarily through blade
flapping: advancing/retreating blades experience differential inflow, tilting the rotor plane
and misalignment thrust. The flapping angle β satisfies a first-order dynamic equation
(simplified Pitt-Peters inflow model):
τβ ˙β + β = θ0
2 + 8
3π
vw sin ψ
ΩR
,
where τβ is flapping time constant, θ0 collective pitch, vw horizontal wind, ψ azimuth, and
ΩR tip speed. This generates hub moments Mx, My ∝β and thrust deflection, entering as
additive attitude disturbances τw.
While the present outer-loop focus assumes inner-loop rejection, future extensions
will integrate these torques into a full Newton–Euler 6-DOF model to evaluate coupled
robustness, especially attitude excursions under extreme gusts.
https://doi.org/10.3390/machines14030277

## Page 8

Machines 2026, 14, 277
8 of 24
3.5. Trajectory Tracking Error Dynamics
Let pd(t) be a smooth reference trajectory with bounded derivatives. Define the
tracking error as
e(t) = p(t) −pd(t).
(7)
Differentiating twice yields the error dynamics
¨e(t) = 1
mu(t) + 1
m fw(p, t) −¨pd(t).
(8)
Equation (8) forms the basis for controller synthesis and robustness analysis.
3.6. Disturbance Boundedness Assumption
Assumption 1. The wind disturbance force fw(p, t) is bounded such that
∥fw(p, t)∥≤¯fw,
∀t ≥0.
(9)
In (9), ¯fw > 0 is a known constant.
This is a physically acceptable assumption that is required to provide strong guarantees
of stability.
3.7. Fundamental Stability Property
Lemma 1. The uncontrolled error dynamics in (8) are unstable in the presence of nonzero
wind disturbances.
Proof. Setting u(t) = 0 yields ¨e(t) = fw/m −¨pd(t), which results in unbounded error
growth for persistent disturbances.
3.8. Control Objective
The control objective is to design u(t) such that:
lim
t→∞e(t) = 0,
lim
t→∞˙e(t) = 0,
(10)
while minimizing control power and making it resistant to stochastic wind disturbances.
Theorem 1. Under bounded wind disturbances and appropriately designed control inputs, the
closed-loop error dynamics are uniformly ultimately bounded.
Proof. The proof follows from Lyapunov stability theory and is controller-specific; detailed
derivations are provided in subsequent sections for SMC, LQR, and MPC.
Corollary 1. The UAV trajectory tracking performance remains robust under stochastic wind shear
if the disturbance bound is satisfied.
Remark 3. The above modelling framework enables a fair and rigorous comparison of optimal,
robust, and predictive controllers under identical harsh wind conditions.
4. Controller Design and Stability Analysis
This section presents the design of three representative control strategies (SMC, LQR,
and MPC) for robust UAV trajectory tracking under harsh wind environments. The con-
trollers are developed within the unified modelling framework introduced in Section 2 to
ensure a fair and meaningful comparison.
https://doi.org/10.3390/machines14030277

## Page 9

Machines 2026, 14, 277
9 of 24
4.1. Sliding Mode Control
4.1.1. Sliding Surface Design
Define the sliding surface as
s(t) = ˙e(t) + Λe(t).
(11)
In (11), Λ ∈R3×3 is a positive definite diagonal matrix.
The sliding surface enforces first-order error dynamics once the system reaches the
sliding manifold, ensuring exponential convergence of the tracking error.
4.1.2. SMC Control Law
The SMC input is designed as
uSMC = m( ¨pd −Λ ˙e) −Ks tanh(s),
(12)
where Ks ∈R3×3 is a positive definite gain matrix.
The hyperbolic tangent function tanh(s) (component-wise) replaces the discontinuous
sgn(s) to introduce a smooth approximation within a boundary layer around the sliding
surface. This mitigates chattering by providing a continuous control signal that transitions
gradually from −Ks to Ks as ∥s∥increases. The effective boundary layer thickness is implic-
itly controlled by the argument scaling (here, direct tanh(s) corresponds to δ = 1). Smaller
effective δ yields sharper transitions (better robustness, smaller residual error) but risks
residual oscillations; larger δ ensures smoother control at the cost of wider boundary layer
and larger steady-state bounds under persistent disturbances. The smoothing parameter is
typically selected empirically or such that the layer encompasses realistic tracking errors
(e.g., δ ≈0.1–1.0 in normalized units). In our implementation, the direct tanh(s) form was
chosen after preliminary tuning to achieve sub-0.5 m steady-state error under the simulated
wind profiles while eliminating observable chattering. More advanced adaptive boundary
layers could further optimize this trade-off.
The former term of the expression signifies the equivalent control that cancels the
nominal dynamics, whereas the latter term imposes the robustness against the wind
disturbances. Chattering is reduced by the hyperbolic tangent function.
Remark: The design inherently counters bounded matched disturbances via the robust
term without explicit estimation/feedforward, as the gain Ks > ¯fwI ensures boundedness
(Theorem 2). While disturbance observers could reduce gain/chattering in hybrids, pure
SMC avoids estimation errors in stochastic wind and maintains simplicity, aligning with
our baseline comparison focus. Feedforward/estimation is more relevant for LQR/MPC
extensions and noted as future work.
4.1.3. Stability Analysis
Theorem 2. Under Assumption 2, the closed-loop error dynamics under SMC are globally uni-
formly ultimately bounded.
Proof. Consider the Lyapunov candidate function
V = 1
2s⊤s.
(13)
Differentiating yields
˙V = s⊤
 1
m fw −Ks tanh(s)

.
(14)
https://doi.org/10.3390/machines14030277

## Page 10

Machines 2026, 14, 277
10 of 24
Since ∥fw∥≤¯fw, choosing Ks > ¯fwI ensures ˙V < 0 outside a compact set, guaranteeing
ultimate boundedness.
Remark 4. The use of tanh(·) instead of sgn(·) modifies the ideal sliding mode to the behavior of
the boundary layer. While Theorem 2 guarantees global uniform ultimate boundedness (with a bound
depending on ¯fw/λmin(Ks) and smoothing scale), the residual set size increases slightly compared
to discontinuous SMC. This is an acceptable compromise for practical UAV implementation, as
validated by low RMS errors in Monte Carlo simulations (Section 5).
4.2. Linear Quadratic Regulator
4.2.1. LQR Problem Formulation
Consider the linearized state-space model
˙x = Ax + Bu.
(15)
The LQR controller minimises the quadratic cost function
J =
Z ∞
0

x⊤Qx + u⊤Ru

dt,
(16)
where Q ⪰0 and R ≻0.
The cost function penalizes state deviation and control energy, yielding an optimal
feedback law for nominal conditions.
4.2.2. LQR Control Law
The optimal control input is
uLQR = −KLQRx,
KLQR = R−1B⊤P,
(17)
where P is the solution to the algebraic Riccati equation.
4.2.3. Stability Property
Lemma 2. In the absence of disturbances, the LQR-controlled system is asymptotically stable.
Proof. The Riccati-based gain KLQR ensures that A −BKLQR is Hurwitz.
Remark 5. Although LQR ensures optimal energy usage under nominal conditions, it lacks
robustness against strong stochastic wind disturbances, as confirmed by simulation results.
4.3. Model Predictive Control
4.3.1. MPC Optimization Problem
At each sampling instant, MPC solves
min
u
Np
∑
k=0

∥xk −xd∥2
Q + ∥uk∥2
R

,
(18)
subject to
xk+1 = Adxk + Bduk,
∥uk∥∞≤umax.
(19)
MPC predicts future system behavior and optimizes control actions while respecting
physical constraints.
https://doi.org/10.3390/machines14030277

## Page 11

Machines 2026, 14, 277
11 of 24
4.3.2. Recursive Feasibility
Lemma 3. If the MPC optimization problem is feasible at time k, it remains feasible at time k + 1
under bounded disturbances.
Proof. The receding horizon structure ensures constraint satisfaction by shifting the optimal
solution forward in time.
4.3.3. Closed-Loop Stability
Theorem 3. Under bounded wind disturbances, the MPC-controlled UAV achieves practical
stability around the reference trajectory.
Proof. Using the optimal cost as a Lyapunov candidate, it can be shown that the cost
decreases monotonically outside a bounded invariant set.
Remark 6. MPC achieves a favourable trade-off between robustness, tracking accuracy, and energy
efficiency but incurs higher computational complexity.
4.4. High-Order Control Barrier Function (HOCBF) Controller
Consider the UAV translational dynamics:
˙x = v,
m ˙v = u + d(t),
(20)
where x ∈R3 is the position, v ∈R3 is the velocity, u ∈R3 is the control input, d(t) is a
bounded disturbance, and m is the mass of the UAV. In compact form:
˙X = f (X) + g(X)u,
X =
"
x
v
#
.
(21)
4.4.1. Safety Constraint Formulation
Define a safety function h(x) ≥0 to enforce trajectory tracking within a safe radius r:
h(x) = ∥x −xd∥2 −r2,
C = {x ∈R3 : h(x) ≥0}.
(22)
The system has relative degree 2 with respect to h(x):
˙h = 2(x −xd)⊤v,
(23)
¨h = 2(v −˙xd)⊤v + 2(x −xd)⊤˙v.
(24)
4.4.2. High-Order Barrier Construction
Introduce auxiliary variables:
ψ1 = ˙h + α1h,
(25)
ψ2 = ˙ψ1 + α0ψ1,
(26)
with α0, α1 > 0. The HOCBF condition is:
ψ2 ≥0.
(27)
4.4.3. Control Formulation via Quadratic Program
The admissible control set:
Usa f e =
n
u ∈R3 : L2
f h + LgL f h u + α1 ˙h + α0h ≥0
o
,
(28)
https://doi.org/10.3390/machines14030277

## Page 12

Machines 2026, 14, 277
12 of 24
and the safety-filtered control is obtained by:
u∗= arg min
u∈Usa f e
∥u −unom∥2,
(29)
where unom is the nominal controller (e.g., SMC).
4.4.4. Stability Analysis
Theorem 4. If ψ2 ≥0 for all t ≥0, then the set C is forward invariant, i.e.,
x(0) ∈C =⇒x(t) ∈C,
∀t ≥0.
(30)
Remark 7. The HOCBF guarantees that safety constraints are never violated while minimally
altering the nominal controller. Robustness and trajectory tracking performance are preserved.
4.5. Adaptive Critic Attitude Learning Control (ACALC)
4.5.1. Error Dynamics and Sliding Surface
Define the tracking errors:
e = x −xd,
˙e = v −˙xd
(31)
and the sliding surface:
s = ˙e + Λe,
Λ > 0.
(32)
4.5.2. Performance Index
The infinite-horizon cost function:
J =
Z ∞
0
e⊤Qe + u⊤Ru

dt,
Q > 0, R > 0.
(33)
4.5.3. Actor–Critic Structure
Critic Network:
Approximates the value function:
ˆV(ξ) = W⊤
c Φ(ξ),
ξ =
"
e
˙e
#
,
(34)
where Φ(ξ) is the basis function vector and Wc are the critic weights.
Actor Network:
Generates control:
u = uSMC + W⊤
a Φ(ξ),
uSMC = m( ¨xd −Λ ˙e) −K tanh
 s
ϕ

,
(35)
where Wa are actor weights.
4.5.4. Adaptive Laws
Critic and actor weight updates:
˙Wc = −αcδΦ(ξ),
(36)
˙Wa = −αaδΦ(ξ),
(37)
https://doi.org/10.3390/machines14030277

## Page 13

Machines 2026, 14, 277
13 of 24
where δ is the temporal difference error:
δ = ξ⊤Qξ + u⊤Ru + ˆV(ξk+1) −ˆV(ξk),
αc, αa > 0.
(38)
4.5.5. Lyapunov Stability Analysis
Consider the composite Lyapunov candidate:
V = 1
2s⊤s + 1
2αc
˜W⊤
c
˜Wc +
1
2αa
˜W⊤
a ˜Wa,
(39)
where ˜Wc = Wc −W∗
c , ˜Wa = Wa −W∗
a are weight estimation errors.
Lemma 4. Under bounded approximation errors, the Lyapunov derivative satisfies:
˙V ≤−s⊤Ks ≤0.
(40)
Remark 8. Hence, the sliding surface s →0, which implies e →0, ensuring asymptotic tracking
while the actor–critic weights converge to bounded values.
4.6. Comparative Control Insights
The comparative evaluation encompasses five controllers implemented on the iden-
tical nonlinear state-space model of the system: LQR with infinite-horizon Riccati based
gains for quadratic cost minimization, MPC employing receding-horizon quadratic opti-
mization with a finite prediction horizon, SMC leveraging its inherent matched-uncertainty
robustness via discontinuous switching, ACALC, which incorporates online adaptation and
explicit constraint handling for enhanced flexibility under uncertainty, and HOCBF based
control, enforcing forward invariance of high-relative-degree safety sets while permitting
aggressive nominal tracking.
For fairness, no explicit disturbance observers, feedforward compensation, or addi-
tional estimation modules are incorporated in LQR, MPC, ACALC, or HOCBF, preserving
their baseline formulations and avoiding estimation-induced risks in turbulent wind con-
ditions. SMC exploits its structural robustness to matched disturbances directly without
augmentation. While observers or adaptive estimators could improve nominal performance
in LQR, MPC, ACALC, and HOCBF, they introduce complexity and potential sensitivity to
noise or model mismatch in harsh environments.
Corollary 2. Under identical severe wind disturbances, SMC delivers the strongest robustness and
most consistent tracking accuracy across stochastic variations, as evidenced by the tightest Monte
Carlo dispersion and lowest mean RMS error. HOCBF and ACALC provide comparable steady-state
precision with added constraint-awareness and adaptability, respectively, outperforming classical
methods in structured uncertainty. MPC offers the most favorable long-term energy-tracking
trade-off through predictive optimization but exhibits greater sensitivity to unmodelled dynamics;
LQR achieves the lowest computational burden yet the weakest disturbance rejection among the set.
Remark 9. This corollary is substantiated by deterministic trajectory-tracking comparisons
(Section 4), Monte Carlo robustness analysis under parametric uncertainties, measurement noise,
and wind variations (Section 5), as well as control-effort and energy-consumption metrics, collec-
tively highlighting SMC’s superior reliability in demanding, uncertain operating regimes.
5. Results and Discussion
This section presents detailed simulation results evaluating the performance of SMC,
LQR, MPC, HOCBF, and ACALC for quadrotor UAV trajectory tracking under harsh wind
https://doi.org/10.3390/machines14030277

## Page 14

Machines 2026, 14, 277
14 of 24
disturbances. The simulations utilise the translational dynamics model given in (1) with
a UAV mass m = 10 kg. The reference trajectory is a smooth circular curve given on the
xy plane at a constant altitude. The wind perturbation is based on the composite model
in (4) of the wind model, and it includes mean wind, deterministic gusts, turbulence, and
shear based on altitude as represented in (5) of shear. All of the controllers are set to
similar nominal performance. Performance can be measured based on trajectory fidelity,
tracking error, and control effort (in the case of SMC), and statistical robustness using
Monte Carlo analysis.
The wind disturbance profile employed over the course of the simulations is shown in
Figure 1. This dynamic model of harsh wind results in an irregular but fixed frequency of
high turbulence that is caused by steady mean wind, intermittent and deterministic gusts,
and high-frequency stochastic turbulence with an irregular increase or decrease of the wind
speed. The gust peaks are prominent at the intervals of about 2 s, 6 s, 11 s, 15 s, 19 s, and
23 s, which are supposed to represent realistic low-altitude atmospheric conditions that
may be observed in the urban environment, coastal area, or rough terrain. The character of
this disturbance, which is non-stationary and constrained but random, poses enormous
challenges to the disturbance rejection property of either controller, but is in line with the
constrained nature of the disturbance.
The stochastic wind variations in the 100 Monte Carlo runs were generated using the
Dryden turbulence model with parameters as detailed in Section 3.3 (turbulence intensity
σt = 2.0 m/s nominal, length scale Lt = 100 m, randomized seeds), combined with
randomized deterministic gust timings and amplitudes (peak 6–8 m/s). This setup ensures
a statistically meaningful evaluation of robustness under varying but bounded harsh
wind conditions.
Simulation Setup and Controller Parameters
The UAV mass was set to m = 10 kg, and the reference trajectory is a smooth circular
path in the xy-plane at constant altitude z = 10 m (radius 5 m, angular speed 0.2 rad/s).
The simulation time step was Ts = 0.01 s.
The composite wind disturbance parameters are as follows:
•
Turbulence intensity: σt = 2.0 m/s (Dryden model, length scale Lt = 100 m);
•
Gust peaks: randomised 6–8 m/s (1-cosine shape, irregular intervals);
•
Shear: exponent α = 0.2, reference altitude z0 = 10 m, shear vector ks = [3, 2, 1]⊤m/s;
•
Drag coefficient: cd = 1.2 kg/s (tuned for realistic deviations of several meters
in gusts).
All numerical simulations were implemented and executed in Python 3 using the free
tier of Google Colab (cloud-based Jupyter environment, accessed during 2025–2026).
The main software libraries utilised were:
•
numpy and scipy for numerical computations, matrix operations, and integration,
•
matplotlib for generating all figures (trajectories, tracking errors, wind profiles,
control signals, Monte Carlo statistics),
•
osqp (Operator Splitting Quadratic Program solver) via its official Python interface
to solve the constrained quadratic programs arising in the MPC formulation at each
time step.
The MPC controller was implemented by directly formulating the sparse equality- and
inequality-constrained quadratic program and passing it to the OSQP solver; no commercial
solvers or high-level modelling layers were employed.
No GPU or TPU acceleration was used. The complete set of 100 Monte Carlo runs
typically completed in 30 to 60 min, confirming practical feasibility even on modest
https://doi.org/10.3390/machines14030277

## Page 15

Machines 2026, 14, 277
15 of 24
cloud resources. The code is modular and can be reproduced locally or in any standard
Python environment.
Controller-specific parameters are summarized in Table 1:
Table 1. Key tuning parameters and implementation details of the controllers.
Parameter
Value
Description
Common
Simulation time step Ts
0.01 s
Numerical integration step
Monte Carlo runs
100
Randomized wind/initial-
condition trials
SMC
Λ (diag.)
diag(2,2,2)
Sliding surface gains
Ks (diag.)
diag(15,15,15)
Switching gain (>
¯fw ≈
12 N)
Boundary layer
tanh(s)
Chattering reduction
LQR
State weighting Q
diag(100,100,100,10,10,10)
Position states heavily pe-
nalized
Control weighting R
diag(0.1,0.1,0.1)
Moderate control penalty
Riccati solution
care() or lqr()
Continuous-time infinite
horizon
MPC
Prediction horizon Np
20
2 s at Ts = 0.1 s
Control horizon Nc
5
Reduced for computation
MPC sampling time
0.1 s
Outer-loop update
State weighting Q
diag(50,50,50,5,5,5)
Tracking penalty
Control weighting R
diag(0.05,0.05,0.05)
Energy-efficient penalty
Input constraints
∥u∥∞≤1.5 mg
Thrust limit
ACALC
Nominal gain K
LQR-based
Baseline feedback
Adaptation gain Γ
diag(1.2,1.2,1.2)
Parameter adaptation rate
Projection bound ˆθmax
1.5 × nominal
Prevents drift
Constraint parameter ϵ
0.05
Soft constraint margin
Filtering time constant τ
0.08 s
Adaptation filter
HOCBF
Relative degree r
2 or 3
CBF order (position →thrust)
Class-K functions
α1(s) = 3s, α2(s) = 5s1/2, α3(s) = 4s1/3
Higher-order decay rates
Safety margin γ
0.1–0.3
Forward invariance margin
QP objective
min ∥u −unom∥2
Subject to HOCBF constraints
Softening parameter δ
0.02
Slack penalty
Nominal law
LQR/feedback linearization
When safety permits
These values were tuned iteratively via simulation trials to achieve comparable nom-
inal (no-wind) tracking performance (sub-0.2 m steady-state error) while highlighting
disturbance-rejection differences. For LQR and MPC, Q prioritises position over velocity;
for SMC, gains ensure ˙V < 0 outside a small boundary set.
Figure 1 further illustrates the two-dimensional wind velocity components (vw,x, vw,y,
vw,z) when altitude-dependent wind shear is explicitly included. The directional and
temporally varying nature of the field, with magnitudes reaching ±6 m/s and pronounced
high-frequency content, highlights the spatial complexity introduced by the shear term
vs(z) = ks(z/z0)α, which is particularly relevant for low-altitude operations.
https://doi.org/10.3390/machines14030277

## Page 16

Machines 2026, 14, 277
16 of 24
Figure 1. Harsh wind profile combining mean wind, deterministic gusts, and stochastic turbulence.
The comparison of the performance of the closed-loop tracking of the trajectory in the
xy-plane under harsh wind disturbances is shown in Figure 2: LQR, MPC, SMC, ACALC,
and HOCBF against the prescribed reference path. The reference trajectory forms a smooth
closed curve incorporating a full circular arc and a localized deviation in the upper region.
Notably, the SMC trajectory exhibits the tightest adherence to the reference throughout
the entire maneuver, displaying virtually imperceptible deviation even in regions of high
curvature and abrupt directional change. The HOCBF and ACALC are just slightly behind
SMC with only small lateral shifts; however, LQR is also competitive but slightly inaccurate
in transient areas. However, markedly and notably, the MPC depicts large and sustained
deviations, such as a strong undershoot on the lower arc and erroneous inward loop in
the upper-right quadrant, in comparison with its comparative weakness in reflecting fast
varying nonlinear dynamics. It is a visual comparison that indicates the high path-following
strength and precision of SMC in experimental conditions is better than the classical as well
as sophisticated constrained formulations.
The corresponding Euclidean position tracking error ∥e(t)∥= ∥p(t) −pd(t)∥is
presented in Figure 3. Each of the schemes starts with the same large initial error of about
2.8 m since there is position offset imposed. The highest convergence is the quickest and
most decisive; the error is less than 0.01 m after some 1.8 s and virtually zero thereafter with
no tangible oscillations and rebound visible. The settling of both HOCBF and ACALC is
also relatively fast (approximately of the order of 2.0 to 2.2 s), although with slightly higher
transient overshoot than in the case of SMC. LQR is acceptable, with slower converging,
and MPC is the worst, leaving the error above 0.2 m until approximately 7 s and showing
sustained low-frequency oscillations (0.1 to 0.3 m) during the steady state. These findings
offer solid quantitative support indicating that sliding mode control offers the greatest
disturbance rejection as well as the maximum amount of steady-state accuracy of any of
the considered procedures.
https://doi.org/10.3390/machines14030277

## Page 17

Machines 2026, 14, 277
17 of 24
Figure 2. Two-dimensional wind velocity components incorporating altitude-dependent shear.
Figure 3. Comparative xy-plane trajectory tracking performance under harsh wind disturbances.
Figure 4 compares the instantaneous control effort ∥u(t)∥across all control strategies.
All controllers exhibit an initial high-effort transient to correct the starting position error.
Thereafter, SMC produces the highest peak efforts (up to ∼18 N) during gust encounters
due to its aggressive switching action, although the use of tanh(·) significantly reduces
chattering. MPC maintains the smoothest and generally lowest control profile after the
transient phase, benefiting from explicit constraint handling and energy-aware cost mini-
mization. LQR settles to moderate effort levels but remains more responsive to turbulence
than MPC, HOCBF, and ACALC.
https://doi.org/10.3390/machines14030277

## Page 18

Machines 2026, 14, 277
18 of 24
Figure 4. Control effort comparison of all controllers.
The evolution of the sliding surface norm ∥s(t)∥= ∥˙e(t) + Λe(t)∥for the SMC
controller is shown in Figure 5. The surface converges exponentially from an initial
value of approximately 17 to near zero within 4 to 5 s. After reaching the sliding mani-
fold, residual oscillations remain bounded below 0.5 despite ongoing wind disturbances,
confirming effective reaching and sliding phase behavior with the chosen gain Ks and
smooth approximation.
Figure 5. Sliding surface convergence plot of SMC.
Figure 6 summarizes the root-mean-square (RMS) tracking error over the full sim-
ulation duration, offering a compact metric of overall performance. SMC achieves the
lowest RMS value of 0.368 m, marginally outperforming HOCBF (0.368 m) and ACALC
(0.373 m), while clearly surpassing LQR (0.405 m) and decisively outperforming MPC
https://doi.org/10.3390/machines14030277

## Page 19

Machines 2026, 14, 277
19 of 24
(0.814 m). The near-identical RMS performance of SMC and HOCBF reflects their shared
strength in steady-state accuracy. However, SMC’s advantage becomes evident when
considering its faster transient convergence and absence of residual oscillations observed
in the time-domain plots. These quantitative results confirm that sliding mode control
provides the best cumulative tracking fidelity among the compared approaches, delivering
sub-40 cm RMS error in a demanding nonlinear trajectory-following task while maintaining
robustness against initial condition uncertainty and path curvature variations. The bar chart
thereby substantiates the adoption of SMC as the benchmark for high-precision trajectory
tracking under the studied conditions.
Figure 6. Bar plot for comparison between all controllers.
The evolution of the sliding surface norm ∥s(t)∥= ∥˙e(t) + Λe(t)∥for the SMC
controller is shown in Figure 7. The surface converges exponentially from an initial
value of approximately 17 to near zero within 4 to 5 s. After reaching the sliding mani-
fold, residual oscillations remain bounded below 0.5 despite ongoing wind disturbances,
confirming effective reaching and sliding phase behavior with the chosen gain Ks and
smooth approximation.
To quantify statistical robustness under stochastic wind variations, 100 Monte Carlo
runs were performed with randomized realizations of the turbulence and gust components.
The resulting distribution of root-mean-square (RMS) tracking error is summarized in
Figure 8. Each data point represents the RMS error achieved in a single trial, with horizontal
lines indicating the mean value for the respective controller. The sliding mode controller
(SMC) exhibits the lowest mean RMS error (≈0.368 m) and the smallest dispersion, with
all trials tightly clustered around 0.36–0.37 m, demonstrating exceptional consistency and
insensitivity to disturbances. In contrast, MPC displays the highest mean (≈0.814 m) and
widest spread (0.78–0.82 m), indicating pronounced vulnerability to uncertainty. LQR
shows moderate performance (mean ≈0.405 m) with limited variability, while ACALCLC
and HOCBF achieve mean values very close to SMC (≈0.373 m and ≈0.368 m, respectively)
yet exhibit slightly broader scatter. These results quantitatively confirm that SMC provides
the highest robustness and most reliable sub-40 cm tracking accuracy under stochastic
perturbations, outperforming both classical and advanced constrained control strategies in
terms of mean performance and variability.
https://doi.org/10.3390/machines14030277

## Page 20

Machines 2026, 14, 277
20 of 24
Figure 7. Evolution of the sliding surface norm ∥s(t)∥for the SMC controller.
Figure 8.
Monte Carlo analysis of root-mean-square (RMS) tracking error under stochastic
wind variations.
6. Conclusions
This study presented a comprehensive framework for robust trajectory tracking con-
trol of multi-rotor UAVs operating in harsh wind environments characterized by gusts,
turbulence, and altitude-dependent wind shear. A realistic wind disturbance model was
developed and integrated into the nonlinear translational dynamics of a quadrotor UAV, en-
abling a rigorous and fair comparative evaluation of three representative control strategies:
SMC, LQR, MPC, HOCBF, and ACALC.
The performance trade-offs were clear in simulation results with huge support pro-
vided by Monte Carlo analysis during the stochastic wind variations. Even in extreme
cases of gusts and directional uncertainties caused by shear, the root-mean-square error
distributions were lowest (median of 0.5 m in 100 trials), the sliding surface convergence
was rapid, and nearly zero steady-state tracking errors (less than 0.5 in nominal cases)
were obtained. This confirms the ultimate boundedness guarantees of the theoretical ap-
proach based on Lyapunov analysis and highlights the usefulness of SMC in the rejection
https://doi.org/10.3390/machines14030277

## Page 21

Machines 2026, 14, 277
21 of 24
of matched disturbances. ACALC and HOCBF achieve tracking performance very close to
SMC in terms of mean and variance of RMS errors (Figure 8) while additionally providing
online adaptation (ACALC) and explicit forward-invariance guarantees via higher-order
barrier constraints (HOCBF), offering structured robustness enhancements over classical
linear designs. However, in controlled experiments, MPC provided the most control effort
and optimal energy consumption in terms of constrained receding-horizon optimization,
so it is especially appropriate to battery-constrained missions, but significantly increased
tracking errors during extreme stochasticity conditions. LQR was not only simpler to
compute but also featured the worst disturbance rejection and larger deviations and higher
variance of Monte Carlo statistics.
Although the results of the simulation indicate the evident performance trade-offs
between SMC, LQR, MPC, HOCBF, and ACALC when operating in severe wind conditions,
the implementation in the embedded system opens up new issues that determine the choice
of the controllers.
The main constraint of MPC in the case of MPC is its high computational load in the
form of repeated on-line optimization of a prediction horizon. The run time of the quadratic
program at the high frequencies (50–100 Hz) may surpass the low-power embedded
processor, introducing delays or low horizons. More recent approximations allow it to
be run in real time on limited-capability hardware or on companion computers. Such
optimizations would most likely be needed in deployment, which is why our linear-time-
invariant MPC formulation has already made the computation more simple.
SMC offers excellent robustness with low computational cost, making it highly suit-
able for embedded systems. However, in digital implementations with finite sampling,
the discontinuous sign function can induce chattering. Our use of tanh(·) significantly
mitigates this, as shown by smooth control effort (Figure 6) and bounded residual sliding
motion (Figure 7). Further enhancements (higher-order SMC, adaptive boundary layers)
could minimise residual effects.
LQR is computationally lightest (static gain multiplication), ideal for basic micro
controllers. Its main drawback is sensitivity to model uncertainties and disturbances, as
seen in higher variance in Monte Carlo results (Figure 8). Gain scheduling or robust variants
can improve resilience.
ACALC and HOCBF maintain low-to-moderate computational complexity similar to
LQR/SMC while incorporating adaptation and safety constraints, making them attractive
for resource-constrained platforms requiring both robustness and formal guarantees.
In short, LQR is simple in controlled settings, SMC is robust with controllable chat-
tering, and MPC is at the best of tracking, energy use, and constraint trade-off, but needs
computational optimizations to be able to run on embedded systems. Our structure facili-
tates mission specialization or crossbreeding. These trade-offs still have to be empirically
determined through experimental validation using hardware-in-the-loop (HIL) testing and
outdoor flights.
A key limitation is the simulation-only nature of results, despite high-fidelity stochastic
wind and Monte Carlo rigor. Simulations enable controlled, repeatable comparison but omit
real effects: actuator saturation/dynamics, sensor noise, measurement delays, propeller
efficiency loss in turbulence, and embedded computation constraints. To bridge this
gap, future work includes: (i) HIL testing, to assess sampling-induced chattering (SMC)
and optimization delays (MPC); (ii) wind-tunnel experiments for controlled gust/shear
validation; and (iii) outdoor flights in natural gusty conditions to quantify real deviations,
energy use, and robustness rankings. These steps will empirically confirm simulation
trade-offs and guide deployment.
https://doi.org/10.3390/machines14030277

## Page 22

Machines 2026, 14, 277
22 of 24
This research puts forth several opportunities in the future of the proposed framework
as a path to the interim deployment and optimal performance of this scheme. First, one
will have to test the experiment on a real physical platform, the quadrotor. Although high-
fidelity simulations were discovered to be realistic to model the effect of the wind, other real-
world effects, such as actuator dynamics, sensor noise, measurement delays, and turbulence-
induced propeller inefficiency, might pose some concerns. The rankings of robustness
obtained would be confirmed by HIL prototyping and experiments in controlled wind
tunnels or in gusty wind field environments, and any implementation-related limitations
(i.e., chattering in SMC when finite rate sampling) would be uncovered.
Second, hybrid control frameworks may leverage the strengths of the reviewed ap-
proaches. As an example, a hybrid controller combining the disturbance rejection that
is part of SMC and the constraint-handling and constraint-energy optimization of MPC,
perhaps with SMC used as an inner-loop disturbance observing or inner-loop compensating
controller, could be highly capable of providing controllers that are sub-meter accurate,
consume less energy, and ensure constraints are met. Residual chattering reduction and
adaptive variants, including gain-scheduled and neural-enhanced sliding mode surfaces,
might also reduce residual chattering without reducing robustness.
Third, more complicated atmospheric dynamics can be modelled by extensions of
the wind model, e.g., spatially correlated turbulence wake vertices of nearby structures
or downbursts applicable to the operations of urban canyons. Proactive disturbance
compensation would be provided by the integration of real-time wind estimation, which
would potentially bridge the gap between simulation and field performance.
Finally, multi-UAV coordination and higher-level mission planning under wind un-
certainty represent important next steps. Extending the framework to formation control,
collision avoidance, or persistent coverage missions while accounting for wind shear gradi-
ents across a swarm would enhance applicability to large-scale autonomous operations.
Energy-aware path re-planning that explicitly minimises integrated control effort over long
horizons, possibly using reinforcement learning to approximate optimal policies under
stochastic wind, also merits investigation.
These extensions would further bridge the gap between theoretical robustness guaran-
tees and deployable solutions for UAVs in extreme environmental conditions.
Author Contributions: U.F.: conceptualisation, validation, methodology, and writing original draft.
B.K.: supervision, conceptualisation, formal analysis, and writing original draft. Z.U.: formal analysis,
visualisation, project administration, and reviewing original draft. All authors have read and agreed
to the published version of the manuscript.
Funding: This research received no external funding.
Informed Consent Statement: Not applicable.
Data Availability Statement: The original contributions presented in this study are included in the
article. Further inquiries can be directed to the corresponding author.
Conflicts of Interest: The authors declare no conflicts of interest.
Abbreviations and Nomenclature
The following abbreviations and symbols are used in this manuscript:
Abbreviation/Symbol
Description
A, B
State-space system matrices
Ad, Bd
Discrete-time system matrices
cd
Aerodynamic drag coefficient
https://doi.org/10.3390/machines14030277

## Page 23

Machines 2026, 14, 277
23 of 24
DOF
Degrees of freedom
d
Matched disturbance vector
e
Position tracking error vector
˙e
Velocity tracking error vector
FI
Inertial reference frame
fw
Wind-induced aerodynamic disturbance force
¯fw
Upper bound on wind disturbance magnitude
J
Quadratic performance cost function
Ks
Sliding mode control gain matrix
LQR
Linear quadratic regulator
LTI
Linear time-invariant
m
Mass of the UAV (kg)
MPC
Model predictive control
Np
MPC prediction horizon length
PID
Proportional–integral–derivative
p = [x, y, z]⊤
UAV position vector in inertial frame (m)
pd
Desired reference trajectory
Q, R
State and control weighting matrices
˙p
UAV velocity vector (m/s)
¨p
UAV acceleration vector (m/s2)
SMC
Sliding mode control
s
Sliding surface vector
umax
Maximum admissible control input
UAV
Unmanned aerial vehicle
u
Control input (thrust force vector)
V
Lyapunov candidate function
vg
Wind gust component
vm
Mean wind component
vs
Wind shear component
vt
Turbulence component
vw
Wind velocity vector (m/s)
x
State vector [p⊤˙p⊤]⊤
α
Wind shear exponent
Λ
Sliding surface gain matrix
∥· ∥
Euclidean norm
∥· ∥∞
Infinity norm
z
Altitude of UAV (m)
References
1.
Djizi, Hamza, and Zoubir Zahzouh.
Comparative Study of PID, PD, LQR, and LQR-PD Regulators for Quadro-
tor Stabilization and Trajectory Tracking.
2023.
Available online:
https://d1wqtxts1xzle7.cloudfront.net/110837762/
latest-libre.pdf?1706203901=&response-content-disposition=inline%3B+filename%3DComparative_Study_of_PID_PD_LQR_and
_LQR.pdf&Expires=1772275857&Signature=K-9vakVh-CflnKZwC4Rs6bk3YG3S0g4vv2hJ6Oulf-yfZkio3PRXdI5lSiI dfySIDyk1w
T7PCe1KFjHQGYjqz-pDxRKEUUo kxU2cF4YjenVjaA6I8w2CU8JhGRgo zzRUL4psnxnnujwTk-gZQF2AxED2KT0eEGOzdJJAQ67
8gs0LqKcpmqSMhhCRg36PXgEM-EU8X9zfXbVmZimv9w6mcfCvoOLOQu4qsQfl4iDzEvRy7z1C5PgaP7i1yUIVEhTVTCJbPN5x
ZPk6ssaoiKHuRCx3HvbPDRT8ev NGurZk NDg BirLlZvkOnXmThLI-Be2eLX7uVY0ZCoivMUSg__&Key-Pair-Id=APKAJLOHF5
GGSLRBV4ZA (accessed on 19 January 2026).
2.
Saleem, O.; Kazim, M.; Iqbal, J. Robust Position Control of VTOL UAVs Using a Linear Quadratic Rate-Varying Integral Tracker:
Design and Validation. Drones 2025, 9, 73. [CrossRef]
3.
Kalaitzakis, M.; Vitzilaios, N. UAS Control under GNSS Degraded and Windy Conditions. Robotics 2023, 12, 123. [CrossRef]
4.
Uppal, A.A.; Azam, M.R.; Iqbal, J. Sliding mode control in dynamic systems. Electronics 2023, 12, 2970. [CrossRef]
5.
Gomiero, S.; Von Ellenrieder, K.D. Modeling and Sliding Mode Control of a Heavy-lift Quadrotor with a Cable-suspended
Payload under Wind Disturbances. IEEE Trans. Autom. Sci. Eng. 2025, 23, 3065–3082. [CrossRef]
https://doi.org/10.3390/machines14030277

## Page 24

Machines 2026, 14, 277
24 of 24
6.
Panjavarnam, K.; Ismail, Z.H.; Tang, C.H.H.; Sekiguchi, K.; Casas, G.G. Model Predictive Control for Autonomous UAV Landings:
A Comprehensive Review of Strategies, Applications and Challenges. J. Eng. 2025, 2025, e70085. [CrossRef]
7.
Farid, U.; Khan, B.; Ali, S.M.; Ullah, Z. A Digital Twin Model for UAV Control to Lift Irregular-Shaped Payloads Using Robust
Model Predictive Control. Machines 2025, 13, 1069. [CrossRef]
8.
Saxena, R.R.; Pal, J.; Iyengar, S.; Chhaglani, B.; Ghosh, A.; Padmanabhan, V.N.; Venkata, P.T. Holistic Energy Awareness and
Robustness for Intelligent Drones. ACM Trans. Sens. Netw. 2024, 20, 1–31. [CrossRef]
9.
Meng, B.; Zhang, K.; Jiang, B. Fixed-time optimal fault-tolerant formation control with prescribed performance for fixed-wing
UAVs under dual faults. IEEE Trans. Signal Inf. Process. Over Netw. 2023, 9, 875–887. [CrossRef]
10.
Song, X.; Wu, C.; Song, S.; Shi, H.; Zhu, J. Human-in-the-loop adaptive formation control for constrained multi-QUAVs: A
self-triggered predefined-time strategy. Sci. China Technol. Sci. 2025, 68, 2220404. [CrossRef]
11.
Kong, L.; Liu, Z.; Zhao, Z.; Lam, H.K. Observer-based fuzzy tracking control for an unmanned aerial vehicle with communication
constraints. IEEE Trans. Fuzzy Syst. 2024, 32, 3368–3380. [CrossRef]
12.
Wang, S.; Wen, S. Safe control against uncertainty: A comprehensive review of control barrier function strategies. IEEE Syst. Man
Cybern. Mag. 2025, 11, 34–47. [CrossRef]
13.
Chen, S.; Zhu, X.; Fang, Y.; Zhan, Y.; Han, D.; Qiu, Y.; Sun, Y. A Hierarchical PSMC–LQR Control Framework for Accurate
Quadrotor Trajectory Tracking. Sensors 2025, 25, 7032. [CrossRef] [PubMed]
14.
Alhassan, A.B.; Shehu, M.A.; Gali, V. Disturbance observer-based super-twisting smc for variable speed wind energy conversion
system under parametric uncertainties. IEEE Access 2025, 13, 11003–11020. [CrossRef]
15.
Shtessel, Y.; Plestan, F.; Edwards, C.; Levant, A. Adaptive sliding mode and higher order sliding-mode control techniques
with applications: A survey. In Sliding-Mode Control and Variable-Structure Systems: The State of the Art; Springer International
Publishing: Cham, Switzerland, 2023; pp. 267–305.
16.
Xu, Z.; Fan, L.; Qiu, W.; Wen, G.; He, Y. A robust disturbance-rejection controller using model predictive control for quadrotor
UAV in tracking aggressive trajectory. Drones 2023, 7, 557. [CrossRef]
17.
Garg, B.; Kubal, P.C.; Sahoo, S.R Energy-Efficient Controllers for Quadcopters: A Comparative Study of PID, LQR, and MPC. In
International Mechanical Engineering Congress and Exposition-India; American Society of Mechanical Engineers: New York, NY, USA,
2025; Volume 89169, p. V004T09A019.
18.
Chen, P.; Zhang, G.; Li, J.; Chang, Z.; Yan, Q. Path-following control of small fixed-wing UAVs under wind disturbance. Drones
2023, 7, 253. [CrossRef]
19.
Lu, Z.; Tang, Y.; Li, L.; Su, R.; Jiang, Z.; Watson, S.; Weightman, A. Model-Based Analysis of UAV Accurate Landing in Stochastic
Turbulent Environments. In Proceedings of the International Micro Air Vehicles, Conference and Competitions, Puebla, Mexico,
3–7 November 2025.
20.
Vedrtnam, A.; Negi, H.; Kalauni, K. Materials and energy-centric life cycle assessment for drones: A review. J. Compos. Sci. 2025,
9, 169. [CrossRef]
21.
Shao, X.; Zhang, F.; Liu, J.; Zhang, Q. Finite-Time Learning-Based Optimal Elliptical Encircling Control for UAVs with Prescribed
Constraints. IEEE Trans. Intell. Transp. Syst. 2025, 26, 7065–7080. [CrossRef]
22.
Miao, Q.; Zhang, K.; Jiang, B. Fixed-time collision-free fault-tolerant formation control of multi-UAVs under actuator faults. IEEE
Trans. Cybern. 2024, 54, 3679–3691. [CrossRef]
23.
Li, S.; Shao, X.; Wang, H.; Liu, J.; Zhang, Q. Adaptive Critic Attitude Learning Control for Hypersonic Morphing Vehicles without
Backstepping. IEEE Trans. Aerosp. Electron. Syst. 2025, 61, 8787–8803. [CrossRef]
24.
Cheng, Y.; Shao, X.; Li, J.; Liu, J.; Zhang, Q. Concurrent Learning-Based Adaptive Critic Formation for Multi-robots under Safety
Constraints. IEEE Internet Things J. 2024, 12, 7610–7621. [CrossRef]
25.
Shao, X.; Du, J.; Xia, Y.; Zhang, Z.; Hou, X.; Debbah, M. Efficient Path-Following for Urban Logistics: A Fuzzy Control Strategy
for Consumer UAVs under Disturbance Constraints. IEEE Trans. Consum. Electron. 2025, 71, 7117–7128. [CrossRef]
26.
Li, X.; Cheng, Y.; Shao, X.; Liu, J.; Zhang, Q. Safety-Certified Optimal Formation Control for Nonline-ar Multi-Agents via
High-Order Control Barrier Function. IEEE Internet Things J. 2025, 12, 24586–24598. [CrossRef]
27.
Lü, S.; Shen, H. Adaptive fuzzy asymptotic tracking control of uncertain nonlinear systems with full state constraints. IEEE Trans.
Fuzzy Syst. 2024, 32, 2750–2761. [CrossRef]
28.
Gomaa, M.M.; Sabatini, R.; Gardi, A. AAM and UAS collision avoidance in the presence of wind and wake turbulence. In
Proceedings of the 2023 IEEE Aerospace Conference, IEEE, Big Sky, MT, USA, 4–11 March 2023; pp. 1–10.
29.
Wang, B.; Yan, Y.; Xiong, X.; Han, Q.; Li, Z. Attitude Control of Small Fixed– Wing UAV Based on Sliding Mode and Linear Active
Disturbance Rejection Control. Drones 2024, 8, 318. [CrossRef]
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.
https://doi.org/10.3390/machines14030277
