# a_multi_stage_optimized_adaptive_control_framework_for_quadcopter_trajectory_tracking_under_wind_disturbances_and_payload_variations.pdf

## Page 1

A Multi-Stage Optimized Adaptive Control
Framework for Quadcopter Trajectory Tracking
Under Wind Disturbances and Payload Variations
Osama A. Nagee 
King Fahd University of Petroleum & Minerals
Muhammad Faizan Mysorewala 
King Fahd University of Petroleum & Minerals https://orcid.org/0000-0001-8909-8937
Research Article
Keywords: Quadcopter trajectory tracking, Wind disturbances, Payload variations, Fuzzy-PID, LADRC,
Particle swarm optimization
Posted Date: March 6th, 2026
DOI: https://doi.org/10.21203/rs.3.rs-9042352/v1
License:   This work is licensed under a Creative Commons Attribution 4.0 International License.  
Read Full License
Additional Declarations: The authors declare no competing interests.

## Page 2

1 
 
Osama A. Nagee1, Muhammad Faizan Mysorewala1, 2, 3  
1Control and Instrumentation Engineering Department, King Fahd University of 
Petroleum & Minerals (KFUPM), Dhahran 31261, Saudi Arabia 
2Interdisciplinary Research Center for Smart Mobility and Logistics, King Fahd 
University of Petroleum & Minerals, Dhahran 31261, Saudi Arabia 
3Interdisciplinary Research Center (IRC) for Intelligent Manufacturing and Robotics, 
King Fahd University of Petroleum & Minerals, Saudi Arabia 
Emails: g202423680@kfupm.edu.sa , mysorewala@kfupm.edu.sa 
A Multi-Stage Optimized Adaptive Control Framework for Quadcopter 
Trajectory Tracking Under Wind Disturbances and Payload Variations 
ABSTRACT 
This paper proposes a multi-stage control strategy for quadcopter trajectory tracking under wind 
disturbances and payload variations. The approach is built on a standard cascaded architecture, where the 
outer loop regulates horizontal position and generates attitude references, while the inner loop tracks the 
commanded attitudes. First, Particle Swarm Optimization (PSO) is implemented offline to tune baseline 
PID controllers for the outer-loop horizontal channels and inner-loop attitude channels using a tracking-
based objective function. Then, a supervisory fuzzy self-tuning mechanism is integrated within the inner 
loop to adapt the attitude PID gains online according to the tracking error and its rate, improving robustness 
against coupling effects and external disturbances. To ensure effective and bounded adaptation, a Genetic 
Algorithm (GA) is employed offline to optimize the fuzzy scaling factors. In addition, Linear Active 
Disturbance Rejection Control (LADRC) is assigned to the altitude channel to explicitly address payload-
induced thrust-to-weight mismatch by estimating and compensating for the total disturbance. 
MATLAB/Simulink simulations demonstrate improved trajectory tracking and disturbance rejection 
compared with the PSO-tuned fixed-gain baseline. Performance evaluation using the integral of time-
weighted absolute error (ITAE) confirms superior robustness under wind disturbance and payload 
variation scenarios while maintaining bounded control effort. 
KEYWORDS: 
Quadcopter trajectory tracking, Wind disturbances, Payload variations, Fuzzy-PID; LADRC, Particle 
swarm optimization 
1 INTRODUCTION 
In recent years, unmanned aerial vehicles (UAVs), especially quadcopters, have gained high attention due 
to their expanding range of applications [1–4]. They have been used in wide applications from aerial 
photography and precision agriculture to search and rescue and infrastructure inspection [3, 5]. The reason 
for their effectiveness lies in their ability to perform autonomous and precise trajectory tracking [6–9]. 
However, achieving this precision remains a significant control engineering challenge as it has a non-
linear systems behavior and cross-coupling between axes and under actuated configuration [2, 10]. For

## Page 3

2 
 
example, wind disturbance. Furthermore, quadcopters are highly sensitive to internal uncertainties, such 
as sudden payload variations, and external disturbance [4, 11, 12]. For example, wind disturbance can 
affect the stability of the system and degrade its performance [13]. The proportional-integral-derivative 
(PID) controller still the quadcopter flight control and the useful in tight spaces and missions' industry 
standard due to its direct implementation and intuitive tuning [2, 10, 14, 15]. However, the fixed-gain 
nature of conventional PID controllers is the main issue. Although it tuned for adequate performance at a 
specific operating point, it lacks the adaptability to maintain performance across the entire flight envelope 
or in the presence of the disturbances and uncertainties [12]. This often results in persistent tracking errors, 
oscillatory responses, and in some cases, instability [2]. Much research has been conducted in intelligent 
and adaptive control to address these limitations [10]. For instance, Fuzzy Logic Controller (FLC) offers 
a model-free approach to handle nonlinear systems and shows highly effective performance [2]. The self-
tuning Fuzzy-PID controller, where a fuzzy inference system adjusts the PID gains online based on the 
tracking error and its derivative (i.e., error and change-rate of error), has demonstrated superior 
performance over fixed-gain PID in several studies [2, 16–18]. Despite its advantages, the design of the 
fuzzy system itself including the membership functions and scaling factors often relies on trial-and-error 
or heuristic methods, which may not yield a globally optimal solution and can be time-consuming [2, 19]. 
This is where metaheuristic optimization algorithms provide a powerful solution. Particle Swarm 
Optimization (PSO) and Genetic Algorithms (GA) have been successfully applied to automate and 
optimize control parameters, avoiding local minima to find high performance solution [10, 20, 21]. While 
some research has explored using PSO for tuning Fuzzy-PID systems, a gap exists in developing a 
structured, hierarchical optimization framework that systematically combines the global search capability 
of these algorithms with the real-time adaptability of fuzzy logic.  
This paper proposes a multi-stage quadcopter control framework based on a standard cascaded 
architecture, where PSO is employed offline to tune the baseline PID controllers of the outer-loop 
horizontal position channels and the inner-loop attitude channels using a trajectory-tracking objective. In 
addition, a supervisory fuzzy self-tuning mechanism is integrated within the inner loop to adapt the attitude 
PID gains online according to the tracking error and its rate, thereby improving robustness against wind-
induced coupling and unmodeled dynamics while preserving the simplicity of the PID structure. 
Moreover, a GA-based optimization is implemented offline to tune the fuzzy scaling factors, ensuring 
bounded and effective gain adaptation without manual trial-and-error selection. To enhance vertical 
robustness, LADRC is assigned to the altitude channel with the primary objective of addressing payload 
variation, where the resulting thrust-to-weight mismatch is treated as a total disturbance and compensated 
online through disturbance estimation. Finally, comprehensive MATLAB/Simulink simulations under 
nominal conditions, wind disturbances, and payload variation are conducted, and the results supported by 
ITAE-based evaluation confirm superior tracking and robustness compared with the PSO-tuned fixed-
gain baseline. 
The remainder of this paper is organized as follows. Section 2 reviews related work. Section 3 presents 
the quadcopter model and the proposed multi-stage control design (PSO-tuned outer-loop horizontal and 
inner-loop PID, inner-loop fuzzy self-tuning with GA-optimized scaling factors, and LADRC altitude 
control for payload variation), along with the considered disturbance models. Section 4 reports the 
simulation results under nominal conditions, wind disturbance, and payload variation. Finally, Section 5 
concludes the paper and outlines future work.

## Page 4

3 
 
2 RELATED WORKS 
Recent quadcopter trajectory-tracking studies mainly improve robustness through optimized PID-based 
cascaded structures, intelligent self-tuning, and explicit disturbance rejection. Li et al. [1] designed a 
cascaded inner–outer controller where the outer position loop uses GA–PSO offline tuning to minimize 
ITAE, while the inner attitude loop employs LADRC with fuzzy online parameter adaptation. Under time-
varying wind with added Gaussian noise, their simulations reported lower ITAE and faster stabilization 
than PID–PID, PID–LADRC, and PID–Fuzzy LADRC; however, the PID gains remain offline-tuned and 
validation is largely limited to hovering/waypoint tasks rather than challenging 3D trajectories. Using a 
Newton–Euler model of a DJI Tello, Baharuddin et al. [2] proposed a Mamdani MIMO self-tuning fuzzy-
PID within a standard cascaded position–attitude architecture, updating 𝐾௣, 𝐾௜, and 𝐾ௗ online from the 
tracking error and error rate. MATLAB/Simulink results on several reference paths (circle, square, zigzag, 
spiral, and lemniscate) showed improved IAE/ISE/RMSE and faster tracking compared with fixed-gain 
PID, though disturbance effects were not considered. 
Beyond basic self-tuning, El Hamidi et al. [22] compared conventional PID, neural-based PID gain 
scheduling, and PSO-optimized fuzzy-PID, showing that improved back-propagation learning and PSO-
tuned scaling factors can accelerate convergence and enhance tracking performance. PID tuning has also 
been framed as a multi-objective optimization problem: Kouritem et al. [12] introduced MONLTA to tune 
six PID loops (altitude, roll, pitch, yaw, and x–y position) by minimizing metrics such as IAE and ITSE, 
outperforming GA-based tuning and nonlinear PID (NLPID) in simulation. 
For stronger robustness under uncertainty, many works employ nonlinear and sliding-mode–based 
designs. Madebo [23] presented a Lyapunov-stable neuro-fuzzy adaptive sliding-mode controller derived 
from a quaternion Newton–Euler model, where an ANN estimates the equivalent control term and fuzzy 
logic generates the switching term, improving tracking while reducing chattering relative to SMC and 
fuzzy-SMC. Similarly, Darwito et al. [24] integrated ANFIS with SMC to adapt the switching gain under 
changing conditions, achieving improved tracking over classical SMC in simulation. Fuzzy approaches 
have also been validated experimentally: Nguyen et al. [25] proposed a fuzzy-PD trajectory-tracking 
controller and demonstrated performance gains over conventional PD in both MATLAB/Simulink and 
real-time experiments on a QDron2 platform. 
Several studies explicitly address wind and external disturbances. Li et al. [15] combined fuzzy 
approximation of unmodeled dynamics with a nonlinear disturbance observer within a command-filtered 
backstepping framework, reducing derivative complexity and improving experimental precision and 
stability compared with PID. Along the same direction, Khatoon et al. [26] proposed a hybrid adaptive PD 
neuro-fuzzy controller that improved transient response, robustness, and disturbance rejection relative to 
PD, PID, and fuzzy controllers in simulation. From an implementation perspective, Noordin et al. [27] 
evaluated altitude control on a Parrot Mambo using PID, and adaptive PID (APID) with a fuzzy 
compensator (APIDFC); the second-order sliding-mode adaptation and fuzzy compensation reduced 
chattering and power consumption and achieved significantly lower ISE than PID in experiments. For 
higher-level intelligent robustness, Shirzadeh et al. [28] combined exponential sliding-mode control with 
a Type-2 fuzzy neural network, optimized via cuckoo search with Lyapunov-based adaptation laws, and 
reported superior tracking under uncertainties, disturbances, and actuator saturation compared with Type-
1 fuzzy neural and GA-tuned methods in simulation.

## Page 5

4 
 
 
Overall,  Table  1  indicates  that  existing  studies  often  improve  PID  tracking  without  explicit  wind 
evaluation [1], optimize controllers offline without structured online supervision [22], or rely on higher-
complexity nonlinear/SMC-based designs for robustness [28]. In contrast, this work retains a PID-
compatible cascaded architecture while integrating PSO-based global tuning, fuzzy online gain adaptation 
with GA-optimized scaling factors, and an LADRC disturbance-rejection layer to compensate lumped 
uncertainties (e.g., payload variations). This combination provides a systematic, yet practical workflow 
aimed at robust tracking of disturbed 3D trajectories.  
Table 1 Comparison of related works and the proposed approach (PID-, fuzzy-, and optimization-based quadcopter 
control) 
 
Ref. 
Method / 
Controller 
core 
Online 
adaptation 
Offline 
optimizatio
n 
Disturbance 
handling 
Validation 
Main 
strengths 
Main limitation / 
gap (why this work 
is needed) 
 
[1] 
Dual-loop: 
outer PID + 
inner 
LADRC 
with fuzzy 
augmentatio
n (cascaded)
 
Yes (fuzzy 
adaptation 
of LADRC 
parameters) 
Yes (GA-
PSO tunes 
PID gains 
via ITAE) 
Yes (time-varying 
wind + Gaussian 
noise) 
Simulations 
(mainly 
hover/step-
like 
references; 
baseline 
comparisons) 
Lower ITAE; 
faster 
stabilization; 
improved 
wind/disturban
ce rejection vs 
PID/PID–
LADRC 
baselines 
Tested on simple 
trajectories (no 
complex/aggressive 
3D paths) 
[22] 
Neural-PID 
vs PID vs 
PSO-
optimized 
Fuzzy PID 
Yes (NN 
schedules 
gains) 
Yes (PSO 
tunes 
scaling 
factors) 
Indirect (improves 
convergence; 
disturbance not 
central) 
Simulations 
Good 
comparative 
framework and 
improved 
convergence 
Does not focus on 
wind rejection and 
does not present a 
hierarchical tuning + 
supervision pipeline 
for cascaded 
quadcopter control. 
[23] 
Neuro-fuzzy 
adaptive 
SMC (ANN 
+ FLC) 
Yes 
(adaptive 
estimation) 
No (mainly 
adaptive 
laws) 
Yes (robust; 
chattering 
reduced) 
Simulations 
High 
robustness; 
reduced 
chattering; 
good tracking 
Higher complexity 
than PID-based 
designs; harder to 
tune/implement for 
practical PID-
centered pipelines. 
 
[24] 
ANFIS-SMC 
(ANFIS 
adapts SMC 
gain) 
Yes (gain 
adapts 
online) 
No explicit 
global 
optimizer 
Yes (robust to 
changes/disturban
ces) 
Simulations 
Improved 
tracking vs 
classical SMC 
SMC-based 
complexity and 
chattering 
considerations; not 
PID-compatible for 
easy implementation.
 
[25] 
Fuzzy-PD for 
quadcopter 
trajectory 
tracking 
Yes (rule-
based fuzzy 
action) 
No explicit 
global 
optimizer 
Not the main focus
Simulation + 
real-time 
experiments 
Experimental 
validation; 
improved over 
PD 
PD may suffer 
steady-state errors 
under persistent 
disturbances; no 
explicit wind

## Page 6

5 
 
robustness 
optimization. 
 
[15] 
Fuzzy 
approximatio
n + nonlinear 
disturbance 
observer 
(backstepping 
+ command 
filter) 
Yes 
(adaptive + 
observer) 
No (model-
based 
design) 
Yes (explicit 
wind/disturbance 
rejection) 
Experiments 
Strong 
disturbance 
handling and 
high precision 
More complex 
nonlinear 
framework; not a 
PID-based 
architecture with 
simple tuning and 
clear industry 
compatibility. 
 
[26] 
Hybrid 
adaptive PD 
neuro-fuzzy 
controller 
Yes 
(adaptive 
neuro-
fuzzy) 
Not 
emphasized 
Yes (targets 
disturbance 
rejection) 
Simulations 
Improved 
robustness and 
transient 
response 
Limited details on 
cascaded PID 
architecture and 
systematic global 
tuning for wind 
trajectories. 
 
[27] 
PID vs APID 
vs APID + 
fuzzy 
compensator 
(APIDFC) 
Yes (online 
gain 
adaptation 
+ fuzzy) 
No global 
optimizer 
Yes (disturbance 
rejection; 
chattering 
mitigation) 
Real 
experiments 
Practical 
implementatio
n; better ISE; 
lower 
power/chatteri
ng 
Focus on altitude 
control; does not 
provide a full 3D 
trajectory wind study 
with hierarchical 
optimization layers. 
 
[28] 
ESMC + 
Type-2 Fuzzy 
Neural 
Network + 
COA 
optimization 
Yes 
(Lyapunov-
based 
adaptation) 
Yes (COA 
optimizes 
parameters) 
Yes (uncertainty, 
disturbances, 
saturation) 
Simulations 
Very robust 
and accurate 
tracking 
High complexity; 
tuning and 
implementation 
burden; less aligned 
with PID-centered 
practical design. 
This 
work 
PSO-tuned 
cascaded PID 
(outer-loop 
horizontal + 
inner-loop 
attitude) + 
inner-loop 
supervisory 
fuzzy self-
tuning + GA-
optimized 
fuzzy scaling 
factors + 
LADRC 
altitude 
Yes (inner-
loop fuzzy 
adapts 
attitude PID 
gains 
online; 
LADRC/LE
SO 
estimates 
and 
compensate
s total 
disturbance 
in altitude). 
Yes (PSO 
for baseline 
PID gains 
in outer 
horizontal + 
inner 
attitude 
loops; GA 
for fuzzy 
scaling 
factors). 
Yes (explicit 
evaluation under 
wind disturbances 
and payload 
variation; LADRC 
provides altitude 
robustness to 
payload-induced 
uncertainty). 
MATLAB 3D 
trajectory 
simulations 
(nominal vs 
wind and 
payload 
variation) 
with ITAE-
based 
comparison 
PID-
compatible 
and 
implementable
; systematic 
baseline tuning 
+ bounded 
online 
adaptation; 
improved wind 
robustness 
through 
adaptive inner 
loop; payload-
robust altitude 
regulation via 
LADRC 
Validated in 
simulation; HIL/real-
time experimental 
validation and formal 
stability analysis of 
the overall cascaded 
structure remain as 
future work.

## Page 7

6 
 
3 METHODOLOGY  
3.1 Quadcopter Modeling  
 
This section presents the nonlinear dynamic model adopted for controller synthesis and simulation. 
A nonlinear formulation is preferred for aggressive maneuvers and for disturbance studies (e.g., 
wind), since these effects are not well captured by oversimplified linear models [29, 30]. 
3.1.1 Reference frames and attitude representation 
 
Two coordinate frames are considered: (i) an inertial/spatial frame {ܵ} fixed to the earth and (ii) a 
body-fixed frame {ܤ} attached to the quadcopter at its center of mass. The vehicle position in {ܵ} 
is denoted by ࣈ௕
௦= [ݔ  ݕ  ݖ]், and the attitude is parameterized by the Euler angles (߶, ߠ, ߰), 
representing roll, pitch, and yaw, respectively (Fig. 1). The rotation matrix ܴ௕
௦(߶, ߠ, ߰) maps 
vectors expressed in {ܤ} to {ܵ}. 
The attitude transformation is constructed via three successive elemental rotations about the body 
axes. The elemental rotation matrices are given by 
ܴ௫(߶) = ൥
1
0
0
0
cos ߶
−sin ߶
0
sin ߶
cos ߶
൩, ܴ௬(ߠ) = ൥
cos ߠ
0
sin ߠ
0
1
0
−sin ߠ
0
cos ߠ
൩, ܴ௭(߰) = ൥
cos ߰
−sin ߰
0
sin ߰
cos ߰
0
0
0
1
൩. 
 
Fig. 1 Inertial and body-fixed reference frames of the quadcopter and 
the Euler-angle convention [3]. 
ࣈ௕
௦

## Page 8

7 
 
Accordingly, the body-to-spatial rotation is 
ܴ௕
௦= ܴ௫(߶)ܴ௬(ߠ)ܴ௭(߰). 
   (1) 
For compactness, let ܿఈ= cos ߙ and ݏఈ= sin ߙ. Expanding (1) yields 
ܴ௕
௦= ቎
ܿటܿఏ
ܿటݏఏݏథ−ݏటܿథ
ܿటݏఏܿథ+ ݏటݏథ
ݏటܿఏ
ݏటݏఏݏథ+ ܿటܿథ
ݏటݏఏܿథ−ܿటݏథ
−ݏఏ
ܿఏݏథ
ܿఏܿథ
቏. 
 
(2) 
 
 
The body angular velocity of {ܤ} with respect to {ܵ}, expressed in the body frame, is denoted bݕ 
 ߱௕
௕,௦= [݌  ݍ  ݎ]்,where ݌, ݍ, and ݎ are the roll-, pitch-, and yaw-rate components. The Euler-angle 
rates ൣ߶̇  ߠ̇  ߰̇]் are related to  [݌  ݍ  ݎ]் through the standard kinematic mapping 
቎
߶̇
ߠ
߰̇
቏= ൦
1
sin ߶tan ߠ
cos ߶tan ߠ
0
cos ߶
−sin ߶
0
sin ߶
cos ߠ
cos ߶
cos ߠ
൪ቈ
݌
ݍ
ݎ
቉. 
(3) 
 
This relation is valid for the considered operating envelope (i.e., away from the Euler singularity 
at cos ߠ= 0). 
3.1.2 Modeling assumptions 
 
To ensure the model remains both manageable and physically realistic, the following simplifying 
assumptions are made [31]: 
(i) the quadcopter frame is assumed to be rigid; (ii) the structure is assumed to be symmetric; (iii) 
the center of mass coincides with the origin of the body-fixed frame; (iv) the propellers are treated 
as rigid components; and (v) thrust and drag forces are assumed to vary proportionally with the 
square of the propeller speed. 
Table 2 summarizes the symbols and parameters used throughout the quadcopter dynamic model 
and the proposed controller design. 
Table 2 Definitions of symbols and parameters used in the quadcopter dynamic model 
Parameter 
Definition 
߱௕
௕,௦ 
The angular velocity of the body frame with respect to the 
inertia frame expressed in the body frame

## Page 9

8 
 
ܬ௕,௕ 
The inertia of the body expressed in the body frame 
݉ 
Quadcopter mass 
݂௕,௕ 
The total applied force on the body expressed on the body 
frame 
߬௕,௕ 
The total applied torque on the body expressed in the body 
frame 
 
3.1.3 Newton–Euler dynamics 
 
The quadcopter rigid-body dynamics are derived using the Newton–Euler formulation, yielding 
coupled rotational and translational equations of motion (Eqs. (4)–(14)). This formulation is widely 
used for quadrotors and naturally accommodates disturbance terms when required [32, 33].  
The rotational motion of the rigid body expressed in {ܤ} is given by 
ܬ௕,௕߱̇ ௕
௕,௦= −߱௕
௕,௦× (ܬ௕,௕߱௕
௕,௦) + ߬௕,௕. 
(4) 
where ܬ௕,௕∈ℝଷ×ଷ is the inertia matrix, ߱௕
௕,௦= [݌  ݍ  ݎ]் is the body angular velocity, and ߬௕,௕ is 
the net control torque about the body axes. The cross-product term ߱௕
௕,௦× (ܬ௕,௕߱௕
௕,௦) captures the 
gyroscopic coupling between rotational axes. 
The translational motion of the center of mass in {ܵ} is given by 
݉ߦ̈௕
௦= ܴ௕
௦(ݐ) ݂௕,௕−݉݃ݖ̂௦. 
(5) 
where ݉ is the quadcopter mass, ݃ is the gravitational acceleration, and zො௦= [0  0  1]் is the unit 
vector along the inertial ݖ-axis. The vector ݂௕,௕ is the total applied thrust force expressed in {ܤ} 
(thrust acts along the body ݖ-axis). 
The quadcopter is controlled through four virtual inputs: the total thrust ݑଵ and the body torques 
(ݑଶ, ݑଷ, ݑସ). Consistent with the thrust direction, the total thrust force and torque vector are written 
as 
݂௕,௕= ൥
0
0
ݑଵ
൩, ߬௕,௕= ൥
ݑଶ
ݑଷ
ݑସ
൩. 
The total thrust is the sum of individual rotor thrusts, 
ݑଵ= ݇௙(Ωଶ
ଵ+ Ωଶ
ଶ+ Ωଶ
ଷ+ Ωଶ
ସ). 
(6) 
where Ω௜ is the ݅-th rotor angular speed and ݇௙ is the thrust coefficient.

## Page 10

9 
 
 
The roll, pitch, and yaw torques are produced by differential thrust (lever arm ݈) and rotor reaction 
torques (drag coefficient ݇௠) 
൥
ݑଶ
ݑଷ
ݑସ
൩= ൦
݈݇௙(Ωଶ
ସ−Ωଶ
ଶ)
݈݇௙(Ωଶ
ଷ−Ωଶ
ଵ)
݇௠(Ωଶ
ଶ−Ωଶ
ଵ+ Ωଶ
ସ−Ωଶ
ଷ)
൪. (7) 
Equation (7) shows that (i) roll and pitch torques arise from opposing-arm thrust differences, and 
(ii) yaw torque arises from the imbalance of rotor drag moments due to alternating rotation 
directions. 
Substituting (7) into (4) yields the compact rotational form 
ܬ௕,௕൥
݌̇
 ݍ̇
ݎ̇
൩= ൥
݈݂ସ−݈݂ଶ
݈݂ଷ−݈݂ଵ
߬ଶ−߬ଵ+ ߬ସ−߬ଷ
൩−ቈ
݌
ݍ
ݎ
቉× ቆܬ௕,௕ቈ
݌
ݍ
ݎ
቉ቇ. 
(8) 
where ݂௜= ݇௙Ω௜
ଶ is the thrust generated by rotor ݅, and ߬௜= ݇௠Ω௜
ଶ is the corresponding reaction 
(drag) torque. 
By substituting f௕,௕= [0  0  ݑଵ]் into (5) and expanding ܴ௕
௦, the inertial accelerations become 
ݔ̈ = ݑଵ
݉(cos ߶ௗsin ߠௗcos ߰+ sin ߶ௗsin ߰). 
(9) 
ݕ̈ = ݑଵ
݉(cos ߶ௗsin ߠௗsin ߰−sin ߶ௗcos ߰). 
(10)
ݖ̈ = −݃+ ݑଵ
݉(cos ߶ௗcos ߠ). 
(11) 
Equations (9)– (11) explicitly show that horizontal motion (ݔ, ݕ) is generated by tilting the vehicle 
(changing ߶ and ߠ), which redirects thrust into the horizontal plane, while altitude motion depends 
on the vertical thrust component cos ߶cos ߠ. 
Assuming a diagonal inertia matrix 
ܬ௕,௕= ቎
ܬ௫௫
0
0
0
ܬ௬௬
0
0
0
ܬ௭௭
቏. 
the rotational dynamics can be written explicitly as 
 
(12)

## Page 11

10 
 
݌̇ = ൬ܬ௬௬−ܬ௫௫
ܬ௫௫
൰ݍݎ+ ܬ௥
ܬ௫௫
ݍΩ + 1
ܬ௫௫
߬థ. 
 
ݍ̇ = ቆܬ௭௭−ܬ௫௫
ܬ௬௬
ቇ݌ݎ−ܬ௥
ܬ௬௬
݌Ω + 1
ܬ௬௬
߬ఏ. 
(13) 
ݎ̇ = ൬ܬ௫௫−ܬ௬௬
ܬ௭௭
൰݌ݍ+ 1
ܬ௭௭
߬ట. 
(14) 
Here, ߬థ, ߬ఏ, and ߬ట denote the roll, pitch, and yaw control torques about the body axes, ܬ௥ is the 
rotor rotational inertia, and Ω represents the net rotor-speed term that captures rotor gyroscopic 
effects according to the rotor rotation directions. The products ݍݎ, ݌ݎ, and ݌ݍ represent inertial 
coupling between the rotational axes. 
3.1.4 Control inputs and motor mixing (control allocation) 
 
The physical actuators are the four rotor speeds Ω௜, whereas the controller is formulated in terms 
of the virtual inputs [ݑଵ  ݑଶ  ݑଷ  ݑସ]். Therefore, a control-allocation step is required to map the 
desired thrust and torques to rotor-speed commands. Using thrust and drag relations ݂௜= ݇௙Ω௜
ଶ and 
߬௜= ݇௠Ω௜
ଶ, the motor mixing relationship can be written in matrix form as 
⎣
⎢
⎢
⎢
⎡Ωଵ
ଶ
Ωଶ
ଶ
Ωଷ
ଶ
Ωସ
ଶ⎦
⎥
⎥
⎥
⎤
= 
⎝
⎜
⎛
⎣
⎢
⎢
⎡݇௙
݇௙
݇௙
݇௙
0
−݇௙
0
݇௙
−݇௙
0
݇௙
0
−݇௠
݇௠
−݇௠
݇௠⎦
⎥
⎥
⎤
⎠
⎟
⎞
ିଵ
൦
ݑଵ
ݑଶ
ݑଷ
ݑସ
൪. 
(15) 
The mixing matrix is determined by the quadcopter geometry and rotor rotation directions [34]. 
When the matrix is invertible, a unique allocation exists for the commanded thrust–torque vector 
within actuator limits; in practice, saturation constraints are applied to ensure Ω௜ remain feasible. 
3.2 Proposed Control Design 
 
This section presents the proposed hierarchically optimized control strategy for quadcopter 
trajectory tracking. The overall architecture follows a nested inner–outer loop structure, where an 
outer position loop generates attitude references, and an inner attitude loop ensures fast stabilization 
and accurate tracking of these references [35]. Such a cascaded design is widely adopted for 
quadrotor control because it separates the slower translational dynamics from the faster rotational 
dynamics, improving stability and tuning practicality. Fig. 2 shows the standard nested control 
loops of quadcopter.

## Page 12

11 
 
3.2.1 Overview of the control design  
The proposed methodology is organized into four consecutive stages to ensure both nominal 
performance and robustness. 
 
Stage 1 (offline PSO-tuned baseline PID): Particle Swarm Optimization (PSO) is used to tune 
the baseline PID gains offline. PSO optimizes (i) the outer-loop horizontal position PID gains (for 
ݔ–ݕ regulation), which generate attitude references, and (ii) the inner-loop attitude PID gains, 
which track ߶ௗ, ߠௗ, and ߰ௗ. This stage establishes strong fixed-gain controllers that serve as a 
reliable starting point for subsequent robustness layers. 
Stage 2 (LADRC altitude loop): The vertical channel is strengthened using Linear Active 
Disturbance Rejection Control (LADRC). The altitude controller improves robustness to payload 
variations, which alters the effective mass and introduces thrust-to-weight mismatch. LADRC 
lumps payload-induced uncertainty, aerodynamic effects, and unmodeled couplings into a single 
“total disturbance,” estimates it online using a Linear Extended State Observer (LESO), and 
compensates for it directly in the thrust command. 
Stage 3 (online supervisory fuzzy self-tuning): Robustness of attitude regulation is enhanced by 
integrating a supervisory fuzzy self-tuning layer within the inner loop. The fuzzy system uses the 
attitude tracking error and its rate to generate bounded gain adjustments Δ𝐾௣, Δ𝐾௜, and Δ𝐾ௗ, 
thereby adapting the inner-loop PID gains online while preserving the overall cascaded structure. 
Fig. 2 Cascaded quadcopter control architecture: the outer position loop generating attitude commands for the inner 
attitude loop.

## Page 13

12 
 
Stage 4 (offline GA optimization of fuzzy scaling factors): A Genetic Algorithm (GA) is used 
offline to tune the fuzzy scaling factors that govern the amplitude of online gain adaptation. Each 
candidate scaling-factor set is evaluated via closed-loop simulation, and the scaling factors that 
yield the best tracking performance are selected while preventing overly aggressive gain variations. 
Fig. 4 illustrates the proposed hierarchical cascaded control architecture for the quadcopter, 
organized into a slower outer loop and a faster inner loop. The trajectory planner provides the 
desired position/velocity commands and the reference yaw angle (߰ௗ). In the outer loop, the 
horizontal position controller (PID) regulates the ݔݕ motion and produces the desired translational 
accelerations (ݔ̈ௗ, ݕ̈ௗ), which are mapped together with ߰ௗ into the desired roll and pitch angles 
(߶ௗ, ߠௗ). In parallel, the altitude channel is regulated by LADRC, where the controller and its 
extended state observer (ESO) estimate and compensate for the lumped disturbance acting on the 
vertical dynamics (e.g., modeling uncertainties, and payload-induced thrust-to-weight mismatch), 
ࡹ࢕࢚࢕࢘ 
ࡹ࢏࢚࢛࢞࢘ࢋ
ࡽ࢛ࢇࢊࢉ࢕࢖࢚ࢋ࢘
ࢊ࢟࢔ࢇ࢓࢏ࢉ
ࢀ࢘ࢇ࢐ࢋࢉ࢚࢕࢘࢟
࢖࢒ࢇ࢔࢔ࢋ࢘ 
ܴ௕
௦, ߱௕
௕,௦(߶, ߠ, ߰, ݌, ݍ, ݎ)ݐℎ݁ܽܿݐݑ݈ܽ ݋ݎ݅݁݊ݐܽݐ݅݋݊
ܽ݊݀ݐℎ݁ܽ݊݃ݑ݈ܽݎݒ݈݁݋ܿ݅ݐ݅݁ݏ
ߦ௕
௦, ߦ̇௕
௦ݐℎ݁ܽܿݐݑ݈ܽ݌݋ݏ݅ݐ݅݋݊
 ܽ݊݀ ݐℎ݁ ݈݅݊݁ܽݎ ݒ݈݁݋ܿ݅ݐ݅݁ݏ 
ݑଶିସ
ܴ௕
௦
ௗ(߶ௗ, ߠௗ, ߰ௗ)
           the desired orientation 
ݑଵ 
ݐℎݎݑݏݐ  
ݒ݁ܿݐ݋ݎ
Inner loop
faster
Outer loop 
slower
ࣱ௕,௕
ܪ௕
௦
ࣰ௕
௕,௦
߶ௗ= ݂ଵ(ݔ̈ௗ, ݕ̈ௗ, ߰ௗ)
ߠௗ= ݂ଶ(ݔ̈ௗ,  ݕ̈ௗ, ߰ௗ)
߰ௗ= ߰ௗ 
ݔ̈ௗ, ݕ̈ௗthe desired 
acceleration
PID's  
࡭࢚࢚࢏࢚࢛ࢊࢋ 
ࢉ࢕࢔࢚࢘࢕࢒࢒ࢋ࢘ 
ߦ௕
௦
ௗ௘௦, ߦ௕
௦̇
ௗ௘௦, ߰ௗ௘௦, ߰̇ ௗ௘௦
ݐℎ݁ ݀݁ݏ݅ݎ݁݀ 
݌݋ݏ݅ݐ݅݋݊ ܽ݊݀ ݈݅݊݁ܽݎ
ݒ݈݁݋ܿ݅ݐ݅݁ݏ with       
desired 
Yaw angle
ݐℎ݁ݎ݁quired 
torque 
to achieve the 
desired orientation
ݐℎ݁ݐ݋ݐ݈ܽܽ݌݌݈݅݁݀
 ݓݎ݁݊ܿℎ ݋݊ ݐℎ݁ ܾ݋݀ݕ
ݐℎ݁ݎ݈݁ܽݐ݅ݒ݁݌݋ݏ݁ܽ݊݀ݐℎ݁ݐݓ݅ݏݐ
 ܾ݁ݐݓ݁݁݊ ݐℎ݁ ܾ݋݀ݕ ܽ݊݀ ݐℎ݁ ݅݊݁ݎݐ݅ܽ 
݂ݎܽ݉݁ݏ.
PID's  
ࡴ࢕࢘࢏ࢠ࢕࢔࢚ࢇ࢒ 
ࢉ࢕࢔࢚࢘࢕࢒࢒ࢋ࢘ 
߰ௗ 
 
 
ܨݑݖݖݕ 
ܵݕݏݐ݁݉ 
ܮܣܦܴܥ 
ܣ݈ݐ݅ݐݑ݀݁
  ݀
݀ݐ 
݁ଶ
݁ଵ
ߙ௣∆݇௣, ߙ௜∆݇௜, ߙௗ∆݇ௗ
݁̇ଶ
Fig. 4 Integration of the supervisory fuzzy system with the inner PID control loop of the quadcopter  
and LADRC with the altitude control. 
 
PSO-based offline optimization of 
baseline PID gains by minimizing 
trajectory-tracking error over a 
complex 3D reference 
  
Design the supervisory 
Fuzzy system   
  
GA-based offline optimization 
of the supervisory fuzzy 
scaling factors using a different 
complex trajectory 
  
Design LADRC-based 
altitude controller 
(replacing the altitude PID)  
Fig. 3 Hierarchical control-design workflow: PSO-tuned baseline PID, supervisory 
fuzzy self-tuning, and GA-optimized scaling factors.

## Page 14

13 
 
 
yielding  a  robust  thrust-related  command  for  the  ݖ -motion.  The  resulting  attitude  reference 
Rௗ(߶ௗ, ߠௗ, ߰ௗ) is  then  tracked  by  the  inner-loop  attitude  PID  controller,  which  generates  the 
required body torques. A supervisory fuzzy adaptation layer enhances both the horizontal PID and 
the attitude PID by updating the gains ൫Δ݇௣, Δ݇௜, Δ݇ௗ൯ online based on the attitude error signals 
and their derivatives, improving responsiveness and robustness under disturbances. Finally, the 
motor mixer converts the total thrust ݑଵ and the body torques (ݑଶ, ݑଷ, ݑସ) into rotor commands that 
drive the quadcopter dynamics, closing the feedback loop using measured position, velocity, 
orientation, and angular rates. 
3.2.2 Algorithm 1 - Offline baseline PID synthesis via PSO  
 
In the first stage, baseline PID gains are obtained offline using Particle Swarm Optimization (PSO). 
The goal of this step is to establish a strong fixed gain starting point for both inner and outer loops 
before adding online adaptation. As illustrated in Fig. 5, the offline PSO procedure iteratively 
simulates the quadcopter model and minimizes the tracking-error indices (ITAE/ISE/MSE) to 
obtain the optimized baseline PID gains ൫𝐾௣଴, 𝐾௜଴, 𝐾ௗ଴൯. For each controlled channel, the PID law 
is written as: 
ݑ(ݐ) = 𝐾௣݁(ݐ) + 𝐾௜න݁(߬)ௗ݀߬+
௧
଴
𝐾ௗ݁̇(ݐ) 
(16) 
where ݁(ݐ) is the tracking error. 
To ensure that the tuned gains remain effective under strong nonlinear coupling, PSO evaluates 
candidate gain sets by simulating the quadcopter on a highly exciting reference trajectory 
(expanding spiral). This trajectory is intentionally selected to persistently excite both outer and 
inner loops, revealing coupling effects and reducing the risk of “overfitting” the gains to a mild 
maneuver.  
Regarding the cost function a multi-objective function is used to penalize error in complementary 
ways 
ITAE
= ෍ݐ௞⋅∥݁(݇) ∥ଵ
ே
௞ୀଵ
⋅߂ݐ,
ISE
= ෍∥݁(݇) ∥ଶ
ଶ
ே
௞ୀଵ
⋅߂ݐ,
MSE
= 1
ܰ෍∥݁(݇) ∥ଶ
ଶ
ே
௞ୀଵ
,

## Page 15

14 
 
 ܬ = ߙ ⋅ ITAE + ߚ ⋅ ISE + ߛ ⋅ MSE.  
(17) 
Where ITAE emphasizes long-duration residual errors. (encouraging fast settling), ISE penalizes 
large transient errors (reducing overshoot), and MSE reflects overall tracking accuracy.  
PSO iteratively updates particle positions (candidate gains) until convergence, yielding optimized 
baseline gains ൫𝐾௣଴, 𝐾௜଴, 𝐾ௗ଴൯ for use in the next stage.

## Page 16

15 
 
 
Start PSO Optimization 
Define Quadcopter Model & Cost 
Function 
Set PSO parameters: ܰ௣, MaxIter, ݓ, ܿଵ, ܿଶ, bounds of PID gains 
Initialize swarm: random particles ܠ௜(PID gain vectors) and velocities ܞ௜  
ݔ௜= [𝐾௣, 𝐾௜, 𝐾ௗ]outer ∪[𝐾௣, 𝐾௜, 𝐾ௗ]inner 
Evaluate Cost Function 
 ܬ௜= ߙௗܫܶܣܧ+ ߚௗܫܵܧ+ ߛௗܯܵܧ 
For each particle ݅= 1, … , ܰ௣: simulate 
model with gains ܠ௜ 
Output Optimized Baseline Gains 
ܾ݃݁ݏݐ= [𝐾௣଴, 𝐾௜଴, 𝐾ௗ଴]outer ∪[𝐾௣଴, 𝐾௜଴, 𝐾ௗ଴]inner 
Is ܬ௜< ܬ(ܘ܊܍ܛܜ௜)? 
Update personal best: ܘ܊܍ܛܜ௜←ܠ௜ 
Iter ≥ MaxIter or convergence? 
End PSO Optimization 
Yes 
No 
Initialize: ܘ܊܍ܛܜ࢏= ܠ࢏; evaluate ࡶ(ܘ܊܍ܛܜ࢏); 
set ܏܊܍ܛܜ= ܉ܚ܏ܕܑܖ࢏ࡶ(ܘ܊܍ܛܜ࢏) 
Is ܬ(ܘ܊܍ܛܜ௜) < ܬ(܏܊܍ܛܜ)? 
Update global best: ܏܊܍ܛܜ←ܘ܊܍ܛܜ௜ 
܃ܘ܌܉ܜ܍ܞ܍ܔܗ܋ܑܜܡ: ܞ࢏←࢝ܞ࢏+ ࢉ૚࢘૚(ܘ܊܍ܛܜ࢏−ܠ࢏) + ࢉ૛࢘૛(܏܊܍ܛܜ−ܠ࢏) 
Update position (PID gains): ܠ࢏←ܠ࢏+ ܞ࢏; Apply bounds to PID gains 
Iter = Iter + 1 
Yes 
No 
No 
yes 
Fig. 5 PSO flowchart (Algorithm 1) for offline tuning of the baseline 
PID gains .

## Page 17

16 
 
 
During  the  optimization  process,  quadcopter  was  given  a  3D  spiral  trajectory  with  slowly 
increasing radius to persistently excite both outer and inner loops: 
ݔௗ(ݐ)
= ܴ൫ݖ(ݐ)൯cos(߱ݐ)
ݕௗ(ݐ)
= ܴ൫ݖ(ݐ)൯sin(߱ݐ)
ݖௗ(ݐ)
= ݒ௭ݐ
 
with radius function 
ܴ(ݖ) = ܴ଴+ (ܴ௠௔௫−ܴ଴) ൬
ݖ
ℎ௧௢௧௔௟
൰
ଶ
. 
(18) 
 
with ߱, ߱௭ chosen to avoid resonance and actuator saturation. For each controlled axis, PSO 
searches 𝐾௣଴, 𝐾௜଴, 𝐾ௗ଴ within stability-preserving bounds using a cost. 
3.2.3 Design of the LADRC controller for altitude control 
 
To enhance altitude tracking under payload variation, thrust uncertainty, and aerodynamic effects, 
the altitude loop is designed using LADRC. The key idea is to lump all unknown terms (e.g., 
mass/thrust mismatch, drag/propwash, and tilt-induced coupling) into a single total disturbance and 
cancel it online using an observer, instead of relying on an accurate model. 
where ܷଵ is the total thrust, ݉ is the mass, and ݀௭(ݐ) represents unmodeled disturbances affecting 
the altitude channel (including model mismatch, aerodynamic effects, and payload-induced thrust-
to-weight changes). In this work, wind is assumed to have no vertical component, so vertical wind 
is not included in ݀௭(ݐ). 
݀௭(ݐ) is assumed bounded and piecewise continuously differentiable, i.e., 
∣݀௭(ݐ) ∣≤݀¯௭, ∣݀̇௭(ݐ) ∣≤݀̇¯
௭. 
 
which is a standard requirement for observer-based disturbance rejection. 
Since the attitude loop is significantly faster than the altitude loop, the altitude channel is rewritten 
in an LADRC-friendly second-order form [36]: 
ݖ̈ = ܾ଴ݑ+ ݂(ݐ),
(20) 
 
ݖ̈ = cos ߶cos ߠ
݉
ܷଵ−݃+ ݀௭(ݐ), 
(19)

## Page 18

17 
 
where ݑ: = ܷଵ , ܾ଴(ݐ) =
ୡ୭ୱ థୡ୭ୱ ఏ
௠
  when tilt compensation is enabled, and ݂(ݐ) denotes the total 
disturbance term that includes −݃ and all uncertainties (including ݀௭(ݐ)). 
To estimate and cancel ݂(ݐ) online, a third-order Linear Extended State Observer (LESO) is used, 
with states ݖ̂ଵ, ݖ̂ଶ, ݖ̂ଷ estimating ݖ, ݖ̇, ݂, respectively: 
ቐ
ݖ̂̇ଵ= ݖ̂ଶ+ ߚଵௗ(ݖ−ݖ̂ଵ)
ݖ̂̇ଶ= ݖ̂ଷ+ ܾ଴ௗݑ+ ߚଶௗ(ݖ−ݖ̂ଵ)
ݖ̂̇ଷ= ߚଷௗ(ݖ−ݖ̂ଵ)
 
(21-23) 
where ߚଵ, ߚଶ, ߚଷ are observer gains. With the disturbance estimate ݖ̂ଷ the LADRC control law 
combines a simple PD tracking term with disturbance cancellation: 
ݑ= ݑ଴−ݖ̂ଷ
ܾ଴
, ݑ଴= ݖ̈ௗ+ ݇௣ௗ(ݖௗ−ݖ̂ଵ) + ݇ௗௗ(ݖ̇ௗ−ݖ̂ଶ), 
(24) 
 
where ݖௗ is the altitude reference, and ݇௣, ݇ௗ set the desired second-order tracking dynamics. The 
term −ݖ̂ଷ/ܾ଴ actively compensates the lumped disturbance, making the altitude channel behave 
like a well-damped second-order system while rejecting disturbances online. For tuning, a 
bandwidth approach is adopted to keep the design repeatable. A controller bandwidth ߱௖ is selected 
based on the desired altitude response speed, then ݇௣= ߱௖
ଶ and ݇ௗ= 2߱௖ are used for a non-
oscillatory response. Next, an observer bandwidth ߱௢> ߱௖ is chosen (faster than the controller), 
and the LESO gains are set using standard pole placement (e.g., ߚଵ= 3߱௢, ߚଶ= 3߱௢
ଶ, ߚଷ= ߱௢
ଷ). 
Increasing ߱௢ improves disturbance rejection but can amplify noise measurement, so it is selected 
according to the sensor quality. Finally, the thrust command is saturated within actuator limits, and 
practical safeguards (e.g., limiting the disturbance estimate and avoiding aggressive steps) are 
applied to maintain robustness. 
Finally, several practical points are enforced to ensure robust operation on the quadcopter. Gravity 
can be handled either as part of ݂(ݐ) or via feedforward (adding ݉݃) to reduce the observer burden. 
Tilt compensation is recommended during aggressive maneuvers by updating ܾ଴(ݐ) =
ୡ୭ୱ థୡ୭ୱ ఏ
௠
, 
which prevents altitude loss when the vehicle tilts. In addition, thrust saturation is applied at the 
actuator level, and the LESO must use the saturated thrust value (the actually applied input) to

## Page 19

18 
 
avoid observer windup and biased disturbance estimation. Fig. 6 illustrates LADRC-based altitude 
control structure with ESO estimation and online disturbance compensation. 
3.2.4 Supervisory fuzzy self-tuning layer (online adaptation) 
 
Although the PSO-tuned PID provides good nominal performance, fixed gains can degrade under 
wind, and unmodeled dynamics. Therefore, a supervisory fuzzy self-tuning mechanism is added to 
adapt the PID gains online using error information as shown in Fig. 7. The fuzzy system takes as 
inputs the normalized tracking error and its rate ݁௡∈[−1,1] , ݁̇௡∈[−1,1] and produces gain 
adjustments  Δ𝐾௣, Δ𝐾௜, Δ𝐾ௗ where the updated gains are computed by: 
𝐾௣= 𝐾௣଴+ ߙ௣ௗΔ𝐾௣,
𝐾௜= 𝐾௜଴+ ߙ௜ௗΔ𝐾௜,
𝐾ௗ= 𝐾ௗ଴+ ߙௗௗΔ𝐾ௗ 
where ߙ௣, ߙ௜, ߙௗ are scaling factors that shape the aggressiveness of adaptation.  
A compact Mamdani-style design is adopted where five triangular membership functions (NB, NS, 
Z, PS, PB) are assigned to each input and output, and a 5×5 rule base (25 rules) is constructed from 
  
Supervisory Fuzzy
  
PID gains update 
݇௣= ݇௣଴+ ߙ௣∆݇௣ 
݇௜= ݇௜଴+ ߙ௜∆݇௜ 
݇ௗ= ݇ௗ଴+ ߙௗ∆݇ௗ 
  
Scaling Factors
݁̇(ݐ)
݁(ݐ)
ݑ(ݐ)
∆݇௣, ∆݇௜, ∆݇ௗ 
ߙ௣∆݇݌, ߙ௜∆݇݅, ߙௗ∆݇݀
݁(ݐ)
Fig. 7 Supervisory fuzzy self-tuning PID scheme with scaling 
factors updating ઢࡷ࢖, ઢࡷ࢏, and ઢࡷࢊ. 
ݍݑܽ݀ܿ݋݌ݐ݁ݎ 
݈ܽݐ݅ݐݑ݀݁  
݀ݕ݊ܽ݉݅ܿ 
1
ܾ଴
݇௣
݇ௗ
ܧݔݐ݁݊݀݁݀
State observer
  
  
ݖௗ
ݖ̂ଷ
ݖ̂ଶ
ݖ̂ଵ
ݖ௔
−
+
+
−
ݑ଴
ݑ  
Fig. 6 LADRC-based altitude control structure with ESO estimation and online disturbance compensation [35].

## Page 20

19 
 
 
standard  PID  tuning  intuition  (increase 𝐾௣ when  error  is  large,  increase 𝐾ௗ  when  oscillations 
appear,  limit 𝐾௜ when  overshoot  risk  is  high).  The  inference  and  aggregation  follow  min–max 
logic, and the outputs are defuzzified using the centroid method.  
This online tuning philosophy (updating 𝐾௣, 𝐾௜, 𝐾ௗ based on error and error rate within a cascaded 
quadrotor structure) consists of prior fuzzy-based quadrotor controllers that report improved 
tracking versus fixed PID.  
The input membership functions for the normalized attitude error (݁) is shown in Fig. 8, which uses 
five triangular membership functions {NB, NS, Z, PS, PB} showing the normalized range [-1, 1]. 
This provides comprehensive coverage of all possible error conditions from strongly negative to 
strongly positive.  
Where the input membership functions for the normalized change in error (ė) is illustrated in Fig. 
9 with the same membership functions of the error (NB, NS, Z, PS, PB) it is distributed uniformly 
across the normalized range [-1, 1], This ensures balanced sensitivity to both positive and negative 
rate errors in the fuzzy inference process. 
Fig. 10 depicts the output membership functions for the proportional gain adjustment (߂݇௣) which 
has the same membership functions of the input (NB, NS, Z, PS, PB). Where the distribution of 
these membership functions ensures rapid response for tracking errors. 
Similar to the membership functions of the proportional gain adjustment ( ߂𝐾௣), the output 
membership functions for the integral gain adjustment (߂݇௜), and derivative gain adjustment (߂݇ௗ), 
utilizing five triangular functions (NB, NS, Z, PS, PB) with a shorter range of  [-0.2, 0.2] as shown 
in Fig. 11 and 12 .this is the common way of the adjustment approach employed for both integral 
and derivative gains to prevent windup issues and noise amplification. 
(a) 
Fig. 8 Input membership functions for the normalized 
tracking error ࢋ. 
(b) 
Fig. 9 Input membership functions for the normalized 
change of error ࢋ̇.

## Page 21

20 
 
 
 
 
The following tables 3-5 illustrates a 5×5 fuzzy-rule tables for the supervisory fuzzy system. Each 
cell gives the linguistic output (NB, NS, Z, PS, PB) (negative/positive big or small, or zero). Where 
Table 3 maps (݁, ݁̇) to the change in proportional gain Δ𝐾௣, Table 4 to Δ𝐾௜, and Table 5 to Δ𝐾ௗ.  
For any pair (݁, ݁̇), the selected label indicates whether to strongly or weakly increase, decrease, 
or keep the corresponding gain near zero. 
Fig. 12 Output membership functions for derivative gain 
adjustment ઢࡷࢊ 
Fig. 11 Output membership functions for integral 
gain adjustment ઢࡷ࢏. 
Fig. 10 Output membership functions for proportional 
gain adjustment ઢࡷ࢖.

## Page 22

21 
 
 
Table 3 Fuzzy rule base for proportional gains update 
ઢࡷ࢖ (inputs: ࢋ, ࢋ̇). 
        
NB 
NS 
Z 
PS 
PB 
NB 
NB 
NB 
NS 
NS 
Z 
NS 
NB 
NS 
NS 
Z 
PS 
Z 
NS 
Z 
Z 
Z 
PS 
PS 
NS 
Z 
PS 
PS 
PB 
PB 
Z 
PS 
PS 
PB 
PB 
Table 4 Fuzzy rule base for integral gains update ઢࡷ࢏ 
(inputs: ࢋ, ࢋ̇). 
 
 
NB 
NS 
Z 
PS 
PB 
NB 
PB 
PS 
PS 
PS 
PB 
NS 
Z 
PS 
PS 
Z 
NS 
Z 
Z 
PS 
Z 
PS 
Z 
PS 
NS 
Z 
PS 
PS 
Z 
PB 
NB 
NB 
NS 
NS 
NB 
 
 
Table 5 Fuzzy rule base for derivative gain update ઢࡷࢊ(inputs: ࢋ, ࢋ̇). 
 
NB 
NS 
Z 
PS 
PB 
NB 
PB 
PS 
Z 
NS 
NB 
NS 
PB 
PS 
Z 
NS 
NB 
Z 
NS 
Z 
Z 
Z 
PS 
PS 
NB 
NS 
Z 
PS 
PB 
PB 
NS 
NS 
Z 
PS 
PB 
 
3.2.5 Algorithm2: Offline optimization of the scaling factors via (GA) 
 
After obtaining the baseline PID gains ൫𝐾௣଴, 𝐾௜଴, 𝐾ௗ଴൯ from the PSO stage, this step optimizes the 
scaling factors of the supervisory fuzzy self-tuning layer offline. In our implementation, each GA 
individual (chromosome) is defined as a 3-dimensional vector: 
ߙ= ൣߙ௣, ߙ௜, ߙௗ൧ 
where ߙ௣, ߙ௜, ߙௗ regulate how aggressively the fuzzy outputs Δ𝐾௣, Δ𝐾௜, Δ𝐾ௗ modify the baseline 
gains. For a candidate ߙ, the quadcopter is simulated along the same evaluation scenario used in 
the paper, while the online gains are updated according to 
𝐾௣= 𝐾௣଴+ ߙ௣ௗΔ𝐾௣, 𝐾௜= 𝐾௜଴+ ߙ௜ௗΔ𝐾௜, 𝐾ௗ= 𝐾ௗ଴+ ߙௗௗΔ𝐾ௗ. 
The fitness is computed as ܬ, where ܬ is the tracking cost defined in Eq. (23) (based on the error 
measures used in the paper, e.g., (ITAE/ISE/MSE). Therefore, each individual is evaluated by 
ࢋ̇ 
ࢋ 
ࢋ̇ 
ࢋ 
ࢋ̇ 
ࢋ

## Page 23

22 
 
 
running a full nonlinear simulation and computing  ܬ, and the GA searches for the scaling factors 
that minimize this cost. 
Algorithm 2 summarizes the adopted workflow. The GA is implemented with population size = 
30, maximum generations = 20, crossover probability = 0.8, mutation probability = 0.2, and elitism 
= 2 (best individuals are copied to the next generation). Tournament selection is used to form 
parents, Simulated Binary Crossover (SBX) is applied to generate offspring, and Polynomial 
Mutation is used to preserve diversity. The best solution at termination is selected and then fixed 
for all subsequent simulations to keep the comparisons consistent. 
ALGORITHM 2: Genetic Algorithm workflow was used to optimize the 
fuzzy scaling factors. 
Input: Population size ܰ, Maximum generations ܩ, Crossover rate ܲܿ, 
Mutation rate ܲ݉ 
Output: Optimized scaling factors [ߙ௣, ߙ௜, ߙௗ]  
1: Initialize: 
   - Population ܲ ← Generate random population of ܰ individuals 
   - Each individual = [ߙ௣, ߙ௜, ߙௗ] ∈[0, 30]ଷ (scaling factors bounds) 
   - Fitness function ܨ(݅݊݀݅ݒ݅݀ݑ݈ܽ) =  1 / (1 +  ܬ) where ܬ is cost from 
Eq. (17) 
 
2: for ݃݁݊݁ݎܽݐ݅݋݊ =  1 to G ݀݋ 
3:   Evaluate fitness for all individuals in ܲ using quadcopter simulation 
4:   Selection:  
       ܲܽݎ݁݊ݐݏ ← ܶ݋ݑݎ݊ܽ݉݁݊ݐ ݏ݈݁݁ܿݐ݅݋݊ (ܲ, ݐ݋ݑݎ݊ܽ݉݁݊ݐ_ݏ݅ݖ݁= 3) 
5:   Crossover: 
       for each parent pair in Parents do 
           if ݎܽ݊݀() < ܲ௖  then 
               ܱ݂݂ݏ݌ݎ݅݊݃ ←
 ܵ݅݉ݑ݈ܽݐ݁݀ ܤ݅݊ܽݎݕ ܥݎ݋ݏݏ݋ݒ݁ݎ(݌ܽݎ݁݊ݐ1, ݌ܽݎ݁݊ݐ2) 
           else 
               ܱ݂݂ݏ݌ݎ݅݊݃ ← ݌ܽݎ݁݊ݐ1, ݌ܽݎ݁݊ݐ2 
           end if 
       end for 
6:   Mutation: 
       for each offspring do 
           if ݎܽ݊݀() < ܲ௠ ݐℎ݁݊ 
             ݋݂݂ݏ݌ݎ݅݊݃ ← ܲ݋݈ݕ݊݋݈݉݅ܽ ܯݑݐܽݐ݅݋݊(݋݂݂ݏ݌ݎ݅݊݃, ߟ݉= 20) 
           end if 
       end for 
7: Replacement: ܲ ← (ܱ݂݂ݏ݌ݎ݅݊݃ ∪ ܧ݈݅ݐ݅ݏ݉(ܲ, ݐ݋݌ 10%)) 
8: end for 
9: Return best individual [ߙ௣, ߙ௜, ߙௗ] from final population

## Page 24

23

## Page 25

24 
 
3.3 Disturbance model 
 
To evaluate controller robustness under realistic operating conditions, the quadcopter translational 
dynamics are augmented with external wind disturbance. The translational dynamics can be written 
as 
݉ξ̈௕
௦= ܴ௕
௦݂௕,௕−݉݃ࢠො௦+ F௪(ݐ). 
(25) 
where ξ̈௕
௦= [ݔ  ݕ  ݖ]், ࢠො௦= [0  0  1]், and ܨ௪(ݐ) = ቎
ܨ௫(ݐ)
ܨ௬(ݐ)
ܨ௭(ݐ)
቏ 
denotes the wind-induced force disturbance expressed in the inertial frame {ܵ}. 
3.3.1 Wind disturbance model 
In this work, wind is modeled as the superposition of a deterministic horizontal gust and a stochastic 
turbulence term 
 
This structure follows common practice in quadrotor wind-environment modeling where the wind 
profile is decomposed into deterministic and stochastic components and deterministic vertical wind 
is often neglected for tractable analysis and simulation. 
1) Gust component (deterministic, time-limited) 
 
 
where ܣ௚ is a dimensionless amplitude, ݐ௚ and ܶ௚ define the gust start time and duration, and d௫௬ 
is a fixed horizontal direction vector (no deterministic vertical gust is applied). 
2)  Turbulence component (stochastic) 
 
where ܣ௧ controls turbulence intensity and the vertical component is set to zero. This is consistent 
with wind models that represent the stochastic component using Gaussian processes, for example, 
Bae and Kang [37] explicitly define the wind profile as a sum of deterministic and stochastic terms, 
noting that the stochastic wind follows a white Gaussian distribution (with Dryden spectral shaping 
in their study). 
F௪(ݐ) = Fgust(ݐ) + Fturb(ݐ). 
(26) 
Fgust(ݐ) = ൜ܣ௚݉݃d௫௬,
ݐ∈[ݐ௚, ݐ௚+ ܶ௚],
0,
otherwise,
. 
(27) 
Fturb(ݐ) = ܣ௧ௗ݉݃ௗ[ݓ௫    ݓ௬    0]், ݓ௫, ݓ௬∼ࣨ(0,1). 
(28)

## Page 26

25 
 
3.3.2 Payload-drop disturbance (abrupt mass variation) 
A payload-drop is modeled as an instantaneous switch in the total mass at time ݐௗ 
 
where ݉଴ is the nominal quadcopter mass and ݉௣ is the payload mass. This captures the sudden 
change in thrust-to-weight ratio that occurs in “mass-drop” missions and is known to degrade 
altitude tracking performance if the controller is not sufficiently robust or adaptive. In the proposed 
framework, this effect is explicitly handled by the LADRC altitude loop through online estimation 
and compensation of the lumped disturbance induced by the abrupt mass change. 
4 SIMULATION RESULTS  
To validate the proposed multi-stage control design, a set of MATLAB/Simulink simulations was 
conducted to evaluate tracking accuracy, robustness, and control effort under both nominal and 
disturbed conditions. The baseline controller is the PSO-tuned cascaded PID, where PSO optimizes 
the outer-loop horizontal PID controllers and the inner-loop attitude PID controllers. Then, 
robustness is enhanced by integrating a supervisory fuzzy self-tuning system within the inner loop, 
while the altitude channel is strengthened using LADRC to handle payload variations that cause 
mass/thrust mismatch. 
4.1 Simulation Setup Parameters 
 
The quadcopter physical and aerodynamic parameters used in the simulations are listed in the 
corresponding parameter Table 6. Using the same plant model for all controllers ensures that 
performance differences are due to the control strategies rather than modeling changes.  
Table 6 Quadcopter physical parameters used in the simulation model [3]. 
Parameters 
Description 
Value (units) 
݉ 
Mass 
1.12 ݇݃
ܫ௫௫ 
Moment of inertia (roll) 
0.0119݇݃. ݉ଶ 
ܫ௬௬ 
Moment of inertia (pitch)
0.0119 ݇݃. ݉ଶ 
ܫ௭௭ 
Moment of inertia (yaw) 
0.0223 ݇݃. ݉ଶ 
݈
Arm length
0.23 ݉
ܾ 
Thrust coefficient in ݂=
ܾௗΩଶ 
7.73 × 10ି଺ 
݀ 
Drag (torque) coefficient 
in ߬= ݀ௗΩଶ 
1.275 × 10ି଻ܰ݉ݏଶ 
݉(ݐ) = ൜݉଴+ ݉௣,
ݐ< ݐௗ,
݉଴,
ݐ≥ݐௗ,.  
(29)

## Page 27

26 
 
ܬ௥
Rotor inertia
8.5 × 10ିସ݇݃. ݉ଶ
݃ 
Gravity 
9.81 ݉· ݏ⁻² 
 
Next, the reference trajectory is defined using an expanding 3D spiral, where the radius increases 
with time (time-varying ݎ(ݐ)) to excite both translational and rotational dynamics and to reveal 
coupling effects during motion. Importantly, the same reference trajectory is applied to all 
compared controllers to guarantee a fair assessment. Table 7 illustrates spiral reference trajectory 
parameters which are related to Eq 18. 
Table 7 Spiral reference trajectory parameters used for excitation and tuning. 
Item 
Symbol / code variable 
Value 
Notes / definition 
Initial 
radius 
ܴ଴ 
1 m 
Spiral radius at ݖ= 0 
Maximum 
radius
ܴ୫ୟ୶ 
3.0 m 
Radius at ݖ= ℎ௧௢௧௔௟ 
Total 
height
ℎ௧௢௧௔௟ 
8.0 m 
Final altitude at the end of the spiral 
Angular 
speed
߱௧௢௧௔௟ 
2.5 rad/s 
Angular velocity in the ݔݕ-plane 
 
After defining the model and trajectory, the optimization and adaptation settings are specified. The 
PSO configuration table reports the swarm and iteration settings used to obtain the baseline PID 
gains. Table 8 shows the PSO configuration used for offline optimization of PID gains 
Table 8 PSO configuration used for offline optimization of PID gains. 
Item 
Value 
Notes 
Swarm size 
30 
Number of particles 
Max iterations
30
Optimization iterations
Inertia weight
0.1
Velocity inertia term
Cognitive coefficient
1.5
Pull toward personal best
Social coefficient
1.5
Pull toward global best
 
In addition to PSO, the GA configuration table reports the genetic parameters used to optimize the 
fuzzy scaling factors that regulate the strength of online gain adaptation inside the inner loop. 
Finally, the quantitative comparison is summarized using the ITAE metric, which reflects tracking 
performance while emphasizing persistent error over time. Table 9 depicts the GA configuration 
used for offline optimization of fuzzy scaling factors.

## Page 28

27 
 
Table 9 GA configuration used for offline optimization of fuzzy scaling factors. 
Item 
Value 
Notes 
Population size 
30 
Individuals per generation 
Max generations
20
Evolution iterations
Crossover probability
0.8
Applied per mating pair
Mutation probability
0.2
Applied per gene (dimension-wise)
Elitism
2
Best individuals copied to next generation
 
Table 10 The parameters of the disturbance model 
Model part 
Symbol or Expression 
Value 
Payload-drop time 
ݐௗ 
ݐௗ= 8ௗs 
Initial mass 
݉= ݉଴+ ݉௣ 
݉= 1.12 + 0.5 = 1.62ௗkg 
Post-drop mass 
݉= ݉଴ 
݉= 1.12ௗkg 
Gust window 
ݐ௚, Δݐ௚ 
ݐ௚= 15ௗs, Δݐ௚= 2ௗs 
Gust force 
ܨgust amplitude 
ܣ௚ 
1.0  
Turbulence force 
ܨturb amplitued 
ܣ௧ 
ܣ௧= 0.05 
Gust force vector  
݀௫௬ 
൥
1
0.5
0
൩ 
 
To make the robustness tests reproducible and to ensure a fair comparison between controllers, the 
external inputs used in the disturbance scenarios are fully specified and kept identical across all 
simulations. Table 10 summarizes the complete disturbance-model parameters used in this study, 
including the gust activation window, the turbulence contribution, and the payload-drop 
configuration (initial/post-drop mass and switching time). These parameters define the exact 
wind/payload profiles injected into the translational dynamics and are therefore the basis for 
interpreting the tracking deviations and control-effort changes reported in the subsequent results. 
Table 11 LADRC parameters 
Loop 
Symbol 
Value (rad/s) 
Controller bandwidth 
߱௖ 
3.0 
ESO (observer) bandwidth
߱௢
15.0

## Page 29

28 
 
 
For the vertical channel, LADRC tuning is expressed compactly in terms of the controller 
bandwidth and the observer (ESO) bandwidth. Table 11 lists the selected bandwidths used to 
compute the LADRC/LESO gains for altitude regulation, where the observer bandwidth is chosen 
higher than the controller bandwidth to enable fast estimation and compensation of the lumped 
disturbance (e.g., thrust-to-weight mismatch due to payload variation). Fixing these LADRC 
parameters across scenarios isolates the effect of the proposed multi-stage framework and supports 
consistent comparison under nominal and payload-varying conditions. 
4.2 Offline PSO Tuning of Cascaded PID Gains 
 
This subsection reports the outcome of the offline PSO tuning stage. Fig. 13 illustrates the PSO 
convergence behavior by plotting the best cost value (global best) versus iteration. The decreasing 
trend indicates that the swarm progressively improves the candidate solutions until it reaches a 
stable optimum, confirming convergence of the optimization process. For clarity in the manuscript, 
the y-axis should be interpreted as the best objective value, which represents the best-performing 
particle at each iteration. 
Fig. 13 PSO optimization progress (convergence) for the baseline PID parameters 
The resulting optimized gains are then reported in Table 12. These gains are used as the baseline 
controller for the nominal and disturbance tests presented next.

## Page 30

29 
 
Table 12 Optimized outer-loop (position) and inner loop PID gains obtained via PSO. 
Axis 
𝐾௣ 
𝐾௜ 
𝐾ௗ 
X 
16.90 
1.300 
6.50 
Y 
8.29 
0.877 
2.68 
Z 
- 
- 
- 
Roll (߶) 
18.20 
0.48 
0.75 
Pitch (ߠ) 
11.58 
0.75 
2.00 
Yaw (߰) 
6.83 
0.53 
1.06 
 
4.3 Nominal Trajectory Tracking with the PSO-Tuned PID (Disturbance-Free). 
 
After obtaining the baseline gains, the controller is first evaluated in a disturbance-free scenario to 
establish a reference level of performance. Under nominal conditions, the PSO-tuned cascaded PID 
achieves stable closed-loop behavior and successfully tracks the expanding spiral trajectory with 
bounded errors. The trajectory plot confirms that the vehicle follows the reference path without 
divergence, while the corresponding attitude and position responses show well-damped behavior 
and acceptable transient characteristics.  
The nominal 3D trajectory tracking obtained with the PSO optimized PID is shown in Fig. 14, and 
the corresponding attitude/position time responses and control effort (total thrust and body torques) 
are reported in Figs. 20 and 24, respectively. 
This nominal case is essential because it verifies that the PSO tuning yields a feasible and efficient 
baseline before introducing robustness layers. The next subsection then stresses the same controller 
under disturbances to reveal its limitations. 
 
4.4 Disturbance Sensitivity of the PSO-Tuned PID Controller. 
 
The key robustness test is performed by applying external disturbances and uncertainty effects 
during tracking. Although the baseline PSO-PID performs well in the nominal case, the disturbed 
scenario reveals a clear limitation: tracking accuracy deteriorates and the controller demands higher 
control effort to compensate for unmodeled effects. This degradation appears as larger deviations 
from the reference trajectory, increased oscillations in the state responses, and a noticeable increase 
in the control inputs.

## Page 31

30 
 
 
Under the applied horizontal wind disturbance, the resulting deviation in 3D trajectory tracking is 
visualized in Fig. 15, while the associated attitude/position responses and the increase in control 
inputs are presented in Figs. 21 and 25, highlighting the limitation of fixed-gain tuning in disturbed  
The elevated control activity under disturbance is not only a performance issue but also a practical 
concern, as it may push actuators closer to saturation and potentially accelerate wear. These 
observations motivate the need for an adaptive inner-loop enhancement, which is introduced in the 
next subsection through the supervisory fuzzy self-tuning mechanism. 
 
4.5 Nominal Tracking Improvement Using Fuzzy Self-Tuned Attitude Control. 
 
To improve performance beyond the fixed-gain baseline, the supervisory fuzzy self-tuning layer is 
integrated inside the inner-loop attitude controller. In the nominal case, this addition improves the 
closed-loop response by enabling the inner loop to adjust its gains according to the instantaneous 
tracking error and error rate. As a result, the attitude tracking becomes tighter, which directly 
improves horizontal tracking because the outer-loop commands are executed more accurately by 
the inner loop. 
Compared with the baseline PSO-PID, the fuzzy-augmented inner loop yields smaller deviations, 
improved transient regulation, and smoother compensation behavior. Importantly, this 
improvement is achieved without changing the overall cascaded structure; the enhancement is 
introduced through bounded online gain adaptation within the inner loop. 
For the disturbance-free case with the supervisory fuzzy self-tuning inner loop, the improved 3D 
trajectory tracking is shown in Fig. 16, with the corresponding attitude/position responses given in 
Fig. 22 and the resulting control inputs in Fig. 26. 
 
4.6 Superior Disturbance Rejection of the Fuzzy-PID Controller  
 
 The disturbance-rejection capability of the proposed controller is evaluated by introducing time-
varying wind forces in the horizontal axes, as shown in Fig. 31, which provides the disturbance 
signals applied in the ݔ and ݕ directions. Under this wind profile, the 3D trajectory in Fig. 17 shows 
that the GA-optimized fuzzy self-tuning PID maintains close tracking of the reference path, while 
avoiding the large deviations observed with the fixed-gain PSO-PID baseline under disturbance. 
This improvement is further clarified by the time-domain responses in Fig. 23, where the proposed 
controller achieves faster disturbance attenuation and smaller oscillations in the coupled channels, 
reflecting stronger closed-loop damping during wind excitation. In addition, the control effort in 
Fig. 27 remains bounded and structured, indicating that the controller rejects wind disturbances

## Page 32

31 
 
 
through  effective  compensation  rather  than  excessive  high-frequency  activity.  Overall,  the 
observed behavior is consistent with the controller architecture: the inner-loop fuzzy self-tuning 
adapts the attitude response online, improving the execution of outer-loop commands during wind-
induced coupling, while the altitude loop remains robust due to the disturbance-rejection 
mechanism. 
 
4.7 PSO optimized PID under payload variation 
 
To evaluate robustness against payload variation, the quadcopter mass is switched abruptly 
according to the payload-drop model defined in Section 3.3.2. This change directly alters the thrust-
to-weight ratio and disturbs the vertical channel, which then propagates to horizontal motion 
through attitude coupling. As a result, even though the PSO-PID controller remains well-behaved 
in the nominal case, its fixed gains cannot fully accommodate the sudden change in effective plant 
dynamics, leading to larger transient errors and slower recovery. 
This limitation is evident in the ITAE results in Table 13. Compared to the disturbance-free case, 
the baseline PSO-PID shows a clear increase in time-weighted error under payload variation, 
particularly in the channels most affected by coupling and required re-balancing after the mass 
change. This indicates that the fixed-gain baseline is sensitive to abrupt parameter variation, and 
motivates the use of an explicit robustness mechanism (disturbance estimation/cancellation in 
altitude) and adaptive inner-loop regulation. 
 
The impact of the payload change on the nominal (PSO-PID + LADRC) controller is illustrated 
by the 3D trajectory tracking in Fig. 18 (with the corresponding thrust/torque commands shown 
in Fig. 28), where the transient degradation becomes clear immediately after the mass variation. 
 
4.8 PSO-optimized PID with a self-tuning fuzzy under payload variation 
 
In this payload-variation scenario, the main purpose of integrating LADRC in the altitude channel 
is to explicitly address the mass/thrust mismatch caused by payload change. Instead of relying on 
a fixed model, LADRC treats the payload-induced change as part of the total disturbance, estimates 
it online via the observer, and compensates it directly in the altitude control action. This helps the 
quadcopter maintain vertical regulation after the mass switch, which also reduces the coupling-
driven degradation in horizontal tracking. 
The quantitative results in Table 13 support this behavior: under payload variation, the proposed 
controller achieves slightly lower ITAE than the baseline in key channels (e.g., improvements in

## Page 33

32 
 
 
ݔ, ݕ,  and ݖ),  indicating  better  recovery  after  the  mass  change,  while  maintaining  comparable 
performance in the remaining channels. Minor trade-offs may still appear in some attitude channels 
because the fuzzy inner loop prioritizes maintaining stability and bounded control under sudden 
dynamics change, but overall the controller preserves stable tracking without divergence and with 
consistent closed-loop behavior under payload variation.  
The imposed mass variation used in this scenario is summarized in Fig. 29, and the resulting 3D 
trajectory tracking and control inputs of the proposed controller are presented in Figs. 19 and 30, 
respectively, demonstrating stable recovery after the payload switch. 
Finally, the qualitative improvement is supported quantitatively by the ITAE comparison: in Table 
13, the wind-disturbance case leads to unbounded (inf) ITAE for the PSO-PID baseline (indicating 
loss of tracking / divergence in the simulation), whereas the proposed method achieves finite ITAE 
values across all controlled states, confirming stable tracking under wind excitation and payload 
variations. 
 
 
 
 
 
 
Fig. 14 3D trajectory tracking using the PSO-optimized PID 
controller (no external disturbance). 
Fig. 15 3D trajectory tracking using the PSO-optimized PID 
controller under external disturbance.

## Page 34

33 
 
 
Fig. 16  3D trajectory tracking using the GA-optimized fuzzy self-
tuning PID controller (no external disturbance). 
Fig. 17 3D trajectory tracking using the fuzzy self-tuning 
PID controller under external disturbance. 
Fig. 18 3D trajectory tracking using the nominal PSO-PID controller 
under payload variation. 
Fig. 19 3D trajectory tracking using the proposed controller under 
payload varation.

## Page 35

34 
 
 
 
 
Fig. 20 Attitude and position responses of the PSO-optimized PID controller (no 
external disturbance).

## Page 36

35 
 
 
 
 
Fig. 21 Attitude and position responses of the PSO-optimized PID controller under 
external wind disturbance.

## Page 37

36 
 
 
 
 
Fig. 22 Attitude and position responses of the fuzzy self-tuning PID controller 
(no external disturbance).

## Page 38

37 
 
 
 
 
Fig. 23 Attitude and position responses of the fuzzy self-tuning PID controller under 
external wind disturbance.

## Page 39

38 
 
 
 
 
 
 
 
Fig. 24 Control inputs (total thrust and body torques) of the PSO-optimized PID controller (no external 
disturbance). 
Fig. 25 Control inputs of the PSO-optimized PID controller under external disturbance.

## Page 40

39 
 
 
 
 
 
 
 
 
Fig. 26 Control inputs of the fuzzy self-tuning PID controller (no external disturbance). 
Fig. 27 Control inputs of the fuzzy self-tuning PID controller under external disturbance.

## Page 41

40 
 
 
 
 
 
 
 
 
 
 
 
Fig. 28 Control inputs of the nominal (PSO-PID + LADRC) controller under payload variation. 
Fig. 29 Mass variation plot (the right-hand vertical axis denotes the total mass )

## Page 42

41 
 
 
 
 
 
 
 
 
 
 
 
 
Fig. 30 Control inputs of the proposed controller under payload variations. 
Fig. 31 Wind disturbance signals in x and y directions.

## Page 43

42 
 
 
 
4.8 Overall Performance Summary Across All Scenarios (Wind Disturbance and Payload 
Variation) 
 
The simulation results consistently demonstrate the superior performance of the proposed 
controller compared with the baseline PSO-tuned PID in both robust scenarios. Under wind 
disturbances, the baseline controller exhibits clear performance degradation and, in some cases, 
loss of tracking (as reflected by the unbounded ITAE values), whereas the proposed approach 
preserves stable closed-loop behavior with bounded errors and finite ITAE across all controlled 
states. This improvement is mainly attributed to the inner-loop fuzzy self-tuning, which strengthens 
attitude regulation during wind-induced coupling and enables faster disturbance attenuation. 
Similarly, under payload variation, the proposed controller maintains better tracking consistency 
after the abrupt mass change, achieving lower time-weighted tracking errors and smoother recovery 
than the fixed-gain baseline. This superiority is primarily due to the integration of LADRC in the 
altitude channel, whose main purpose is to reject the payload-induced thrust-to-weight mismatch 
by estimating and compensating the resulting total disturbance online. Overall, across both 
scenarios, the proposed controller achieves a better balance between tracking accuracy, robustness, 
and bounded control effort, confirming its suitability for practical operation under realistic 
environmental and operational uncertainties. 
Table 13 ITAE performance indices of the compared controllers across all controlled states under nominal 
and disturbance scenarios. 
Senario 
Method 
ITAE Index 
࢞ 
࢟ 
ࢠ 
࢜࢞ 
࢜࢟ 
࢜ࢠ 
Nominal 
PSO-PID 
86.2451   77.3024    76.9866  205.8352  194.2742  36.3764  
PSO-PID 
+ Fuzzy-
GA
86.4329   77.6081    77.6993  204.8051  194.0006  42.9770  
Wind disturbance 
PSO-PID 
inf 
inf 
inf 
inf 
inf 
inf 
PSO-PID 
+ Fuzzy-
GA
89.6612 
77.7072 
80.6530
208.2203
195.7843
78.1287
Payload variation 
PSO-PID  
+ LADRC
87.3659   184.7569   4.8654   211.6365  470.3046  22.9615

## Page 44

Under review at the Arabian Journal for Science and Engineering, February 2026 
43 
 
PSO-PID 
+ Fuzzy-
GA + 
LADRC
86.8631   184.1567   4.6644   222.0227  469.0826  23.1966  
 
5 CONCLUSION 
This paper presented a multi-stage control strategy for quadcopter trajectory tracking based on a 
standard cascaded structure. First, Particle Swarm Optimization (PSO) was used to obtain a reliable 
baseline by tuning the PID controllers of the outer-loop horizontal position and the inner-loop 
attitude dynamics. Then, a supervisory fuzzy self-tuning mechanism was integrated within the 
inner loop to adapt the attitude PID gains online using the tracking error and its rate. To avoid 
arbitrary tuning of the adaptation strength, a Genetic Algorithm (GA) was implemented to optimize 
the fuzzy scaling factors offline. In addition, a Linear Active Disturbance Rejection Control 
(LADRC) scheme was assigned to the altitude channel, with the primary objective of handling 
payload variations that cause thrust-to-weight mismatch and degrade vertical tracking. 
The simulation results confirmed that the PSO-tuned cascaded PID achieved stable performance in 
nominal conditions and provided a consistent baseline. However, under wind disturbances and 
payload changes, the fixed-gain baseline showed clear performance degradation. In contrast, the 
proposed controller maintained stable tracking and bounded control actions across all tested 
scenarios. Under wind disturbance, the improvement was mainly linked to the inner-loop fuzzy 
supervision, which strengthened attitude regulation and reduced coupling-induced tracking 
deviations. Under payload variation, the altitude LADRC improved recovery after mass change by 
estimating and compensating the induced total disturbance. Overall, the proposed approach 
achieved a better balance between tracking accuracy and robustness, and the ITAE-based 
comparison supported the superiority of the proposed strategy across the evaluated cases. 
6 FUTURE WORK 
Future work will focus on extending the validation beyond simulation toward more realistic 
implementation conditions. First, the controller will be tested through hardware-in-the-loop (HIL) 
and real-time embedded deployment to evaluate computation time, discretization effects, and 
sensor noise sensitivity. Second, the robustness analysis will be expanded to include actuator 
saturation, propeller dynamics, and time-varying wind fields, as well as uncertainty in inertial 
parameters. In addition, statistical model checking (SMC) will be investigated to provide 
probabilistic robustness guarantees under stochastic uncertainties (e.g., turbulent wind and 
measurement noise). This will be achieved by defining formal performance properties (e.g., 
bounded tracking error and settling-time constraints) and estimating their satisfaction probability

## Page 45

44 
 
 
over  large  ensembles  of  randomized  simulations,  complementing  the  deterministic  stress-test 
scenarios used in this work. Third, the LADRC altitude design can be further improved by adaptive 
tuning of the nominal gain and observer bandwidth to maintain performance across wider payload 
ranges. Finally, additional practical extensions will be explored, such as fault-tolerant control 
allocation, energy-aware optimization of the control effort, and formal stability/robustness analysis 
of the overall cascaded structure with fuzzy adaptation and disturbance estimation. 
REFERENCES: 
 
1.  
Li, K., Bai, Y., Zhou, H.: Research on Quadrotor Control Based on Genetic Algorithm and 
Particle Swarm Optimization for PID Tuning and Fuzzy Control-Based Linear Active 
Disturbance 
Rejection 
Control. 
Electronics 
(Switzerland). 
13, 
(2024). 
https://doi.org/10.3390/electronics13224386 
2.  
Baharuddin, A., Mohd Basri, M.A.: Self-Tuning PID Controller for Quadcopter using Fuzzy 
Logic. International Journal of Robotics and Control Systems. 3, 728–748 (2023). 
https://doi.org/10.31763/ijrcs.v3i4.1127 
3.  
Le Nhu Ngoc Thanh, H., Hong, S.K.: Quadcopter robust adaptive second order sliding mode 
control based on PID sliding surface. IEEE Access. 6, 66850–66860 (2018). 
https://doi.org/10.1109/ACCESS.2018.2877795 
4.  
Elmokadem, T., Savkin, A. V.: Towards Fully Autonomous UAVs: A Survey. Sensors 2021, 
Vol. 21, Page 6223. 21, 6223 (2021). https://doi.org/10.3390/S21186223 
5.  
Mohsan, S.A.H., Othman, N.Q.H., Li, Y., Alsharif, M.H., Khan, M.A.: Unmanned aerial 
vehicles (UAVs): practical aspects, applications, open challenges, security issues, and future 
trends. 
Intelligent 
Service 
Robotics 
2023 
16:1. 
16, 
109–137 
(2023). 
https://doi.org/10.1007/S11370-022-00452-4 
6.  
Zuo, Z., Liu, C., Han, Q.-L., Song, J.: Unmanned Aerial Vehicles: Control Methods and 
Future Challenges. IEEE/CAA Journal of Automatica Sinica, 2022, Vol. 9, Issue 4, Pages: 
601-614. 9, 601–614 (2022). https://doi.org/10.1109/JAS.2022.105410 
7.  
Hanover, D., Foehn, P., Sun, S., Kaufmann, E., Scaramuzza, D.: Performance, Precision, 
and Payloads: Adaptive Nonlinear MPC for Quadrotors. IEEE Robot. Autom. Lett. 7, 690–
697 (2022). https://doi.org/10.1109/LRA.2021.3131690 
8.  
Chen, L., Liu, Z., Dang, Q., Zhao, W., Wang, G.: Robust trajectory tracking control for a 
quadrotor using recursive sliding mode control and nonlinear extended state observer. 
Aerosp. Sci. Technol. 128, (2022). https://doi.org/10.1016/J.AST.2022.107749

## Page 46

45 
 
 
9.   
Yan,  K.,  Zhang,  J.R.,  Ren,  H.P.:  Interval  Observer-based  Robust  Trajectory  Tracking 
Control for Quadrotor Unmanned Aerial Vehicle. International Journal of Control, 
Automation and Systems 2024 22:1. 22, 288–300 (2024). https://doi.org/10.1007/S12555-
022-0464-2 
10.  
Lopez-Sanchez I, Moreno-Valenzuela J. PID control of quadrotor UAVs: A survey. Annual 
Reviews in Control. 2023 Jan 1;56:100900. 
11.  
Shen, J., Wang, B., Chen, B.M., Bu, R., Jin, B.: Review on Wind Resistance for Quadrotor 
UAVs: Modeling and Controller Design. https://doi.org/10.1142/S2301385023310015. 11, 
5–15 (2022). https://doi.org/10.1142/S2301385023310015 
12.  
Kouritem, S.A., Mahmoud, M., Nahas, N., Abouheaf, M.I., Saleh, A.M.: A self-adjusting 
multi-objective control approach for quadrotors. Alexandria Engineering Journal. 76, 543–
556 (2023). https://doi.org/10.1016/j.aej.2023.06.050 
13.  
Azid, S.I., Kumar, K., Cirrincione, M., Fagiolini, A.: Wind gust estimation for precise quasi-
hovering 
control 
of 
quadrotor 
aircraft. 
Control 
Eng. 
Pract. 
116, 
(2021). 
https://www.sciencedirect.com/science/article/pii/S0967066121002070  
14.  
Wang, R., Shen, J.: Disturbance Observer and Adaptive Control for Disturbance Rejection 
of Quadrotor: A Survey. Actuators 2024, Vol. 13, Page 217. 13, 217 (2024). 
https://doi.org/10.3390/ACT13060217 
15.  
Li, C., Wang, Y., Yang, X.: Adaptive fuzzy control of a quadrotor using disturbance 
observer. Aerosp. Sci. Technol. 128, (2022). https://doi.org/10.1016/j.ast.2022.107784 
16.  
Park, D., Le, T.L., Quynh, N.V., Long, N.K., Hong, S.K.: Online Tuning of PID Controller 
Using a Multilayer Fuzzy Neural Network Design for Quadcopter Attitude Tracking 
Control. 
Front. 
Neurorobot. 
14, 
619350 
(2021). 
https://doi.org/10.3389/FNBOT.2020.619350 
17.  
Gedefaw, E.A., Abdissa, C.M., Lemma, L.N.: An improved trajectory tracking control of 
quadcopter using a novel Sliding Mode Control with Fuzzy PID Surface. PLoS One. 19, 
e0308997 (2024). https://doi.org/10.1371/JOURNAL.PONE.0308997 
18.  
Ufacık, H., Kececioglu, O.F.: Interval type-2 fuzzy PID cascade control of quadrotor based 
on non-dominated sorting genetic algorithm-II. The Aeronautical Journal. 129, 1924–1959 
(2025). https://doi.org/10.1017/AER.2024.162 
19.  
Zangeneh, M., Aghajari, · Ebrahim, Forouzanfar, · Mehdi: A survey: fuzzify parameters and 
membership function in electrical applications. Int. J. Dyn. Control. 8, 1040–1051 (2020). 
https://doi.org/10.1007/s40435-020-00622-1

## Page 47

46 
 
 
20.   Leal, I.S., Abeykoon, C., Perera, Y.S.: Design, simulation, analysis and optimization of pid 
and fuzzy based control systems for a quadcopter. Electronics (Switzerland). 10, (2021). 
https://doi.org/10.3390/electronics10182218 
21.  
Gad, A.G.: Particle Swarm Optimization Algorithm and Its Applications: A Systematic 
Review. Archives of Computational Methods in Engineering 2022 29:5. 29, 2531–2561 
(2022). https://doi.org/10.1007/S11831-021-09694-4 
22.  
El Hamidi, K., Mjahed, M., El Kari, A.E., Ayad, H.: Neural network and fuzzy-logic-based 
self-tuning PID control for quadcopter path tracking. Studies in Informatics and Control. 28, 
401–412 (2019). https://doi.org/10.24846/v28i4y201904 
23.  
Madebo, M.M.: Neuro-Fuzzy-Based Adaptive Sliding Mode Control of Quadrotor UAV in 
the Presence of Matched and Unmatched Uncertainties. IEEE Access. 12, 117745–117760 
(2024). https://doi.org/10.1109/ACCESS.2024.3447474 
24.  
Darwito, P.A., Indayu, N.: Adaptive Neuro-Fuzzy Inference System Based on Sliding Mode 
Control for Quadcopter Trajectory Tracking with the Presence of External Disturbance. 
Journal 
of 
Intelligent 
Systems 
and 
Control. 
2, 
33–46 
(2023). 
https://doi.org/10.56578/jisc020104 
25.  
Nguyen, A.T., Nguyen, N.H., Trinh, M.L.: Fuzzy PD control for a quadrotor with 
experimental 
results. 
Results 
in 
Control 
and 
Optimization. 
19, 
(2025). 
https://doi.org/10.1016/j.rico.2025.100568 
26.  
Khatoon, S., Nasiruddin, I., Shahid, M.: Design and Simulation of a Hybrid PD-ANFIS 
Controller for Attitude Tracking Control of a Quadrotor UAV. Arab. J. Sci. Eng. 42, 5211–
5229 (2017). https://doi.org/10.1007/s13369-017-2586-z 
27.  
Noordin, A., Mohd Basri, M.A., Mohamed, Z.: Real-Time Implementation of an Adaptive 
PID Controller for the Quadrotor MAV Embedded Flight Control System. Aerospace. 10, 
(2023). https://doi.org/10.3390/aerospace10010059 
28.  
Shirzadeh, M., Amirkhani, A., Tork, N., Taghavifar, H.: Trajectory tracking of a quadrotor 
using a robust adaptive type-2 fuzzy neural controller optimized by cuckoo algorithm. ISA 
Trans. 114, 171–190 (2021). https://doi.org/10.1016/j.isatra.2020.12.047 
29.  
Wu, Z., Cheng, S., Zhao, P., Gahlawat, A., Ackerman, K.A., Lakshmanan, A., Yang, C., 
Yu, J., Hovakimyan, N.: L1Quad: L1 Adaptive Augmentation of Geometric Control for 
Agile Quadrotors With Performance Guarantees. IEEE Transactions on Control Systems 
Technology. 33, 597–612 (2025). https://doi.org/10.1109/TCST.2024.3521182

## Page 48

47 
 
 
30.   Saviolo, A., Loianno, G.: Learning quadrotor dynamics for precise, safe, and agile flight 
control. 
Annu. 
Rev. 
Control. 
55, 
45–60 
(2023). 
https://doi.org/10.1016/J.ARCONTROL.2023.03.009 
31.  
Abera, N.B., Abdissa, C.M., Lemma, L.N.: An improved nonsingular adaptive super 
twisting sliding mode controller for quadcopter. PLoS One. 19, e0309098 (2024). 
https://doi.org/10.1371/journal.pone.0309098 
32.  
Mahony, R., Kumar, V., Corke, P.: Multirotor aerial vehicles: Modeling, estimation, and 
control 
of 
quadrotor. 
IEEE 
Robot. 
Autom. 
Mag. 
19, 
20–32 
(2012). 
https://doi.org/10.1109/MRA.2012.2206474 
33.  
Svacha, J., Paulos, J., Loianno, G., Kumar, V.: IMU-Based Inertia Estimation for a 
Quadrotor Using Newton-Euler Dynamics. IEEE Robot. Autom. Lett. 5, 3861–3867 (2020). 
https://doi.org/10.1109/LRA.2020.2976308 
34.  
Faessler, M., Falanga, D., Scaramuzza, D.: Thrust Mixing, Saturation, and Body-Rate 
Control for Accurate Aggressive Quadrotor Flight. IEEE Robot. Autom. Lett. 2, 476–482 
(2017). https://doi.org/10.1109/LRA.2016.2640362 
35.  
Lopez-Sanchez, I., Pérez-Alcocer, R., Moreno-Valenzuela, J.: Trajectory tracking double 
two-loop adaptive neural network control for a Quadrotor. J. Franklin Inst. 360, 3770–3799 
(2023). https://doi.org/10.1016/j.jfranklin.2023.01.029 
36.  
Herbst G, Madonski R. Active disturbance rejection control: From principles to practice. 
Springer; 2025. 
37.  
Bae, J.J., Kang, J.Y.: Quaternion-Based Robust Sliding-Mode Controller for Quadrotor 
Operation Under Wind Disturbance. Aerospace 2025, Vol. 12, Page 93. 12, 93 (2025). 
https://doi.org/10.3390/AEROSPACE12020093
