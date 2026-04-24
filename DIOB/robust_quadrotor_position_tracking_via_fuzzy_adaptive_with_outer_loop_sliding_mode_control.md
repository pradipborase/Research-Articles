# robust_quadrotor_position_tracking_via_fuzzy_adaptive_with_outer_loop_sliding_mode_control.pdf

## Page 1

Robust Quadrotor Position Tracking via Fuzzy
Adaptive with Outer-Loop Sliding Mode Control
Sotirios Spanogianopoulos 
University of Portsmouth
Mostafa Jalalnezhad 
Kharazmi University
Research Article
Keywords: UAV, Deep reinforcement learning, Robotic control, CoppeliaSim, Deep deterministic policy
gradient
Posted Date: January 14th, 2026
DOI: https://doi.org/10.21203/rs.3.rs-8394499/v1
License:   This work is licensed under a Creative Commons Attribution 4.0 International License.  
Read Full License
Additional Declarations: No competing interests reported.

## Page 2

1 
 
Robust Quadrotor Position Tracking via Fuzzy Adaptive with Outer-Loop Sliding Mode Control 
 
Sotirios Spanogianopoulos*  
University of Portsmouth, School of Electrical and Mechanical Engineering, PO1 3DJ, Portsmouth, UK 
sotiris.spanogianopoulos@gmail.com  
  
Mostafa Jalalnezhad 
Kharazmi University, Department of Mechanical Engineering, Tehran 15614, Iran, 
 mostafajalalneghad@yahoo.com, mostafajalalnezh@khu.ac.ir, RCID: https://orcid.org/0000-0002-6304-9894 
 
 
*Corresponding Author Email: sotiris.spanogianopoulos@gmail.com  
 
Abstract: 
The present research introduces an integrated and computationally efficient control and optimization framework aimed at enhancing the 
robustness, adaptability, and real-time efficiency of unmanned aerial vehicle (UAV) operations in complex, uncertain, and dynamically 
changing environments. The proposed hybrid system combines an Adaptive Fuzzy Feedback Linearization Controller (AFFLC) with an 
outer-loop Sliding-Mode Controller (SMC) and a Late Acceptance Hill-Climbing (LAHC) path-planning optimizer, building a two-layer 
intelligent structure capable of handling both nonlinear flight dynamics and global trajectory optimization. The innovation of the research lies 
in the formulation of a fuzzy adaptive law that modulates internal control gains according to instantaneous tracking error and its derivative, 
ensuring smooth and rapid responses while effectively mitigating chattering without relying on disturbance observers or heavy parameter 
tuning. The importance of this study stems from the growing demand for lightweight, low-complexity algorithms that can sustain stable 
performance under severe operational conditions—such as payload uncertainty, wind disturbance, and limited onboard computational power—
where conventional control and meta-heuristic methods often fail. The objectives include designing a dual-loop AFFLC–SMC system for 
robust stabilization, deriving Lyapunov-based guarantees of global boundedness and convergence, and integrating a LAHC-based global route 
optimizer minimizing the combined cost of distance, energy consumption, and threat exposure. Quantitative and qualitative analyses confirm 
that the proposed approach achieves the smallest tracking error, negligible steady-state deviation, and fastest dynamic recovery. Specifically, 
the AFFLC suppresses rotor chattering by over 70 % and reduces total convergence time by ≈ 35 % compared with conventional adaptive and 
sliding-mode controllers, while the LAHC algorithm yields the lowest path cost and execution time across all benchmark scenarios, stabilizing 
within ≈ 100 iterations—far faster than GWO, SOS, SA, and HGWO-MSOS optimizers. The associated tables and figures demonstrate that 
the adaptive-gain surface produces nonlinear stabilization behavior, effectively balancing transient acceleration and steady-state smoothness, 
while the 3D simulation results highlight the planner’s capability in maintaining safe, energy-efficient navigation even in densely constrained, 
multi-obstacle environments. Collectively, the integrated AFFLC–SMC + LAHC framework offers a lightweight, high-precision, and 
computationally scalable solution readily applicable to real-time UAV flight missions, emphasizing a practical step toward intelligent 
autonomous aerial systems for industrial, security, and environmental applications. 
 
Keywords: UAV, Deep reinforcement learning, Robotic control, CoppeliaSim, Deep deterministic policy gradient. 
 
1. 
Introduction 
Quadrotor position control remains a canonical yet challenging benchmark due to tight actuator limits, strong nonlinear couplings, and 
susceptibility to modeling errors, payload variations, and wind disturbances [1]–[4]. Conventional single-loop designs struggle to reconcile 
fast inner-loop attitude stabilization with accurate outer-loop trajectory tracking, especially under uncertainties and chattering-prone switching 
actions [5], [6]. This paper targets a dual-loop architecture that explicitly separates fast attitude/force generation from slower position 
regulation to achieve high-precision, robust 3D tracking. 
The practical motivation is twofold: ensuring reliability in mission-critical tasks (inspection, SAR, logistics) and keeping computational burden 
compatible with on-board processors [7]–[9]. Real UAV deployments demand controllers that withstand abrupt mass changes, actuator 
saturation, and sensor noise without re-tuning [10], [11]. Our design emphasizes robustness, low computational overhead, and smooth control 
signals suitable for embedded implementation. 
Prior linear approaches such as PID/LQR/LQT offer simplicity and good local behavior but degrade under large excursions and parametric 
drift typical of outdoor flights [12]–[15]. They also require frequent gain re-scheduling and provide limited guarantees against matched 
uncertainties [16]. Consequently, nonlinear and intelligent methods have been widely explored to overcome these limits. 
Sliding Mode Control (SMC) is a popular nonlinear strategy due to its intrinsic robustness to matched disturbances and model errors [17]–
[19]. However, its high-frequency switching induces chattering that excites unmodeled dynamics, amplifies actuator wear, and violates 
feasibility under tight bandwidth constraints [20], [21]. Fractional-order and higher-order SMC variants alleviate chattering but increase design 
and computational complexity [22], [23]. 
Adaptive backstepping and model reference adaptive control (MRAC) improve robustness to parametric uncertainties with Lyapunov-based 
adaptation [24], [25]. Yet, their performance hinges on correct regressor structures and often assumes slowly varying parameters, which may 
not hold during payload pickup/drop events [26]. Moreover, pure adaptive schemes can exhibit sluggish transients or peaking without 
additional damping mechanisms [27]. 
Disturbance observers (DO/ESO/ADRC) estimate lumped uncertainties effectively and have seen success in UAVs [28]–[30]. Still, observer 
bandwidth selection trades off noise amplification versus tracking accuracy, and poorly tuned observers can destabilize inner loops or increase 
control effort [31]. In addition, DO-centric solutions typically require careful plant/actuator modeling around the operating point [32]. 
Fuzzy and neural methods—FLC, ANFIS, RBF/NN—learn complex mappings and compensate unmodeled dynamics [33]–[36]. They reduce 
reliance on exact models but may suffer from over-parameterization, require large training sets, or lack guaranteed stability unless embedded 
in Lyapunov-consistent adaptation laws [37], [38]. Meta-heuristic gain tuning (PSO/GA/GWO/BOA) improves performance but raises off-
line complexity and transferability concerns [39], [40].

## Page 3

2 
 
Recent hybrid strategies combine robust nonlinear control with intelligence to exploit complementary strengths. Examples include SMC+FLC, 
backstepping+NN, ADRC+FLC, and MPC+learned disturbance models [41]–[44]. While promising, many hybrids either retain chattering, 
incur heavy computation, or provide incomplete stability proofs for the fully coupled 6-DOF quadrotor. 
This paper proposes a dual-loop controller that integrates an inner-loop Fuzzy Adaptive Feedback Linearization Controller (AFFLC) with an 
outer-loop Sliding Mode Controller (SMC). The inner loop employs feedback linearization to cancel structured nonlinearities and uses a 
Lyapunov-consistent fuzzy adaptive law to estimate uncertain parameters (e.g., mass/payload) and tune adaptive gains online, thereby 
maintaining smooth actuation and fast convergence [45]. The outer loop uses SMC only at the trajectory level, where its switching activity is 
significantly attenuated by the inner loop, thereby mitigating chattering at the propeller level. 
The key novelty is the asymmetric fuzzy adaptation mapping from the output error Z to the adaptive gain γ, designed so that γ increases 
nonlinearly with |Z| but remains small near the origin to avoid overdrive and residual chatter. The mapping is realized via Gaussian input 
membership functions (NB, NS, Z, PS, PB) and non-symmetric output sets (S, M, B), yielding fast transient compensation when errors surge 
(e.g., load changes) while preserving smooth steady-state behavior [46]. This mechanism closes a known gap between fast adaptation and low 
control ripple in UAV applications. 
Recent investigations have explored numerous intelligent control and optimization strategies for UAVs and robotic systems to enhance 
robustness, adaptability, and computational efficiency. For example, a low-complexity energy-efficient aerial communication platform was 
presented in [47], which improved power utilization but lacked adaptive nonlinear compensation. A comprehensive review on dynamic 
path-planning algorithms was conducted in [48], demonstrating critical trade-offs between convergence speed and parameter sensitivity. Other 
studies [49, 50] identified performance variation under uncertainty for rule-based methods, recommending hybrid meta-heuristics for greater 
real-time stability. 
In the field of intelligent control, [51] proposed a Quadrotor Position Controller integrating fuzzy adaptive feedback linearization with 
sliding-mode control, achieving strong disturbance rejection yet suffering from residual chattering. Further developments in [52] introduced 
intelligent vibration control of composite plates using optimized sliding-mode-based algorithms, providing excellent energy damping through 
nonlinear optimization. The adaptive backstepping formulation presented in [53] demonstrated global stability for underwater manipulators 
through Lyapunov–Krasovskii theory and shares conceptual similarity with the adaptive law employed in the present study. Likewise, [54] 
combined fuzzy estimation and SMC control to enhance tracking precision for aerial platforms, but without considering time-varying 
aerodynamic coefficients. 
Other recent works, such as [55, 56], examined neural-network-based and multi-objective heuristic frameworks for UAVs and mobile robots. 
These approaches improved environmental awareness but incurred high computational costs, limiting suitability for embedded processors. 
The comprehensive surveys in [57, 58] also underscored the need for algorithms that balance fast convergence with low complexity. 
In contrast, the current research introduces a hybrid AFFLC–SMC control structure and a Late Acceptance Hill Climbing (LAHC) optimization 
mechanism that achieve rapid convergence, reduced chattering, and robust adaptability to dynamic load variations—offering a computationally 
lighter yet more stable alternative to prior deep-learning-based or heavy meta-heuristic solutions reported in [47–58]. 
Unlike DO/ESO-based designs, the proposed method avoids explicit high-bandwidth observers, reducing noise amplification and parameter 
tuning burdens. Compared with fractional/higher-order SMC, it achieves chattering suppression through inner-loop linearization and fuzzy 
adaptation rather than higher-order switching dynamics, thus lowering computational complexity. Relative to pure adaptive 
backstepping/MRAC, it provides stronger transient damping and less peaking due to the SMC outer loop and the gain-scheduled fuzzy law. 
The contributions are fourfold: (i) a rigorously analyzed dual-loop architecture with inner AFFLC and outer SMC that preserves fast 
attitude/force dynamics while ensuring robust trajectory tracking; (ii) a Lyapunov-certified fuzzy adaptive law with asymmetric gain shaping 
that accelerates convergence during large deviations yet minimizes steady-state chattering; (iii) a provable stability framework using composite 
Lyapunov functions (and Lyapunov–Krasovskii tools for bounded delays) guaranteeing ultimate boundedness under matched uncertainties 
and time-varying payloads; (iv) a comprehensive benchmark against classical (PID/LQR/LQT), robust (SMC/FRSMC/H∞), adaptive 
(MRAC/backstepping), observer-based (ADRC/ESO), and intelligent (FLC/ANFIS/NN) baselines across two scenarios (nominal and 
uncertain load). 
Methodologically, our approach differs from at least twenty representative prior studies spanning: PID/LQR/LQT tracking [12]–[15]; classical 
SMC and high-order variants [17]–[23]; adaptive backstepping/MRAC [24]–[27]; ADRC/ESO/DO-based designs [28]–[32]; fuzzy and neuro-
fuzzy controllers with meta-heuristic tuning [33]–[40]; and hybrid robust–intelligent controllers [41]–[44]. In contrast to these, our inner-loop 
linearization with fuzzy Lyapunov adaptation directly conditions the effective control gain on real-time error magnitudes, which demonstrably 
suppresses rotor-speed oscillations and reduces control effort under disturbances. 
The resulting closed-loop system achieves: (a) near-perfect 3D trajectory tracking without payload and with unknown payload 
application/removal; (b) substantially reduced rotor-speed ripple versus SMC and classical FLC, faster and smoother mass/payload estimation 
compared with AFLC variants; and (d) improved damping in roll–pitch angles during transients. These behaviors arise from the designed 
synergy: outer-loop sliding variables drive tracking, while inner-loop fuzzy adaptation maintains smooth, adequately damped actuation. 
The significance for practice is that the controller attains robust performance with modest computational cost and minimal parameterization, 
easing porting to embedded autopilots. The avoidance of high-bandwidth observers and higher-order sliding surfaces lowers noise sensitivity 
and actuator wear, extending hardware longevity. Moreover, the structured rule base (with a small number of interpretable membership 
functions) facilitates implementation transparency and certification. 
This paper positions a low-complexity yet theoretically grounded dual-loop controller that advances the state of the art in quadrotor position 
control by unifying feedback linearization, Lyapunov-consistent fuzzy adaptation, and sliding-mode robustness. The proposed method bridges 
the gap between chattering suppression and fast uncertainty compensation, while offering formal stability assurances and favorable embedded 
feasibility. The remainder of the paper details the system modeling, controller synthesis, stability proofs, and simulation studies versus the 
aforementioned baselines 
2. 
Quadrotor Dynamic Model - Paraphrased Version 
In this section, the mathematical model of a quadrotor is formulated based on Newton-Euler equations for a rigid body in three-dimensional 
space [8]. The purpose of this formulation is to obtain a relatively accurate and flexible system representation that can effectively describe the 
behavior and control of a quadrotor. This model ensures reliable simulation results and a robust foundation for subsequent control system 
design. 
Let the state vector of the quadrotor be defined as: 
𝐱= [ݔ
ݕ
ݖ
߶
ߠ
߰]் 
(1) 
where ݔ, ݕ, ݖ represent the vehicle's position in the earth (inertial) frame, and ߶, ߠ, ߰ denote the roll, pitch, and yaw Euler angles, respectively.

## Page 4

3 
 
The linear and angular velocity vectors in the body frame are expressed as: 
ܞ஻= [ݑ
ݒ]், ܟ஻= [݌ݍݎ]் 
(2) 
The linear and angular velocities in the inertial frame are then related to those in the body frame through the following transformation matrices: 
ܞ
ܟ= ܀ܞ஻
܂ܟ஻
 
(3) 
where R and T are the rotation matrices for linear and angular motion transformations, respectively. 
They are defined as: 
܀= [
ܿ(߶)ܿ(߰)
ݏ(߶)ݏ(ߠ)ܿ(߰) −ܿ(߶)ݏ(߰)
ܿ(߶)ݏ(ߠ)ܿ(߰) + ݏ(߶)ݏ(߰)
ܿ(߶)ݏ(߰)
ݏ(߶)ݏ(ߠ)ݏ(߰) + ܿ(߶)ܿ(߰)
ܿ(߶)ݏ(ߠ)ݏ(߰) −ݏ(߶)ܿ(߰)
−ݏ(ߠ)
ݏ(߶)ܿ(ߠ)
ܿ(߶)ܿ(ߠ)
]
܂= [
1
ݏ(߶)ݐ(ߠ)
ܿ(߶)ݐ(ߠ)
0
ܿ(߶)
−ݏ(߶)
0
ݏ(߶)/ܿ(ߠ)
ܿ(߶)/ܿ(ߠ)
]
 
(4) 
where ݏ(), ܿ(), ݐ() represent sin⁡(), cos⁡(), tan⁡(), respectively. 
The translational kinematics are thus written as: 
ݔ˙ = ݓ[ݏ(߶)ݏ(߰) + ܿ(߶)ܿ(߰)ݏ(ߠ)] −ݒ[ܿ(߶)ݏ(߰) −ݏ(߶)ݏ(ߠ)ܿ(߰)] + ݑ[ܿ(ߠ)ܿ(߰)]
ݕ˙ = ݓ[−ݏ(߶)ܿ(߰) + ܿ(߶)ݏ(߰)ݏ(ߠ)] + ݒ[ܿ(߶)ܿ(߰) + ݏ(߶)ݏ(߰)ݏ(ߠ)] + ݑ[ܿ(ߠ)ݏ(߰)]
ݖ˙ = ݓ[ܿ(߶)ܿ(ߠ)] −ݑ[ݏ(ߠ)]
 
(5) 
and the angular kinematics are: 
߶˙ = ݌+ ݎ[ܿ(߶)ݐ(ߠ)] + ݍ[ݏ(߶)ݐ(ߠ)]
ߠ˙ = ݍ[ܿ(߶)] −ݎ[ݏ(߶)]
 
߰˙ = ݎ[ܿ(߶)] + ݍ[ݏ(߶)]
ܿ(ߠ)
 
(6) 
3. 
Dynamic Equations 
By applying the Newton-Euler laws for translational and rotational motion, one obtains: 
݉(ܟ஻× ܞ஻+ ܞ˙஻)⁡= ܎஻
۷ܟ˙ ஻+ ܟ஻× (۷ܟ஻)⁡= ܕ஻
 
(7) 
Where ܎஻= [݂௫, ݂௬, ݂௭]
் is the total force vector, ܕ஻= [݉௫, ݉௬, ݉௭]
் is the torque vector, ݉ is the vehicle mass, and ۷ is the diagonal inertia 
matrix: 
۷ = [
ܫ௫
0
0
0
ܫ௬
0
0
0
ܫ௭
] 
(8) 
Hence, the complete translational dynamics are: 
݂௫= ݉(ݑ˙ + ݍݓ−ݎݒ)
݂௬= ݉(ݒ˙ + ݎݑ−݌ݓ)
݂௭= ݉(ݓ˙ + ݌ݒ−ݍݑ)
 
(9) 
and the rotational dynamics are: 
݉௫= ܫ௫݌˙ −ݍݎ(ܫ௬−ܫ௭)
݉௬= ܫ௬ݍ˙ −݌ݎ(ܫ௭−ܫ௫)
݉௭= ܫ௭ݎ˙ −݌ݍ(ܫ௫−ܫ௬)
 
(10) 
The primary external forces acting on the quadrotor are: 
܎஻= ்ܴ݉݃݁ˆ௭−݂௧݁ˆ3 + ܎௪ 
(11) 
where 
்ܴ݉݃݁ˆ௭ : gravitational force in body coordinates, 
݂௧ : total thrust, 
܎௪= [݂௪௫, ݂௪௬, ݂௪௭]
் : aerodynamic drag or wind disturbances. 
The external moments in the body frame are given as: 
ܕ஻= ߬஻−݃௔+ ߬௪ 
(12) 
where 
߬஻= [߬௫, ߬௬, ߬௭]
் : control torques induced by motor thrust differences, ݃௔ : gyroscopic moments, ߬௪ : aerodynamic disturbances. 
The aggregated gyroscopic term is: 
݃௔= ∑ 
4
௜=1
ܬ௣(ܟ஻∧݁ˆ3)(−1)௜+1Ω௜ 
(13) 
The control inputs for a quadrotor consist of four rotor angular velocities Ω1, Ω2, Ω3,Ω4. 
Let ܾ denote the thrust coefficient and ݀ the drag coefficient; ݈ is the arm length from the center to each rotor. 
The generated forces and moments are: 
߬௫= ܾ݈(Ω3
2 −Ω1
2)
߬௬= ܾ݈(Ω4
2 −Ω2
2)
߬௭= ݀(Ω2
2 + Ω4
2 −Ω1
2 −Ω3
2)
 
(14) 
Accordingly, the complete translational model becomes: 
−݉݃ݏ(ߠ) + ݂௪௫= ݉(ݑ˙ + ݍݓ−ݎݒ)
݉݃ܿ(ߠ)ݏ(߶) + ݂௪௬= ݉(ݒ˙ −݌ݓ+ ݎݑ)
݉݃ܿ(ߠ)ܿ(߶) + ݂௪௭−݂௧= ݉(ݓ˙ + ݌ݒ−ݍݑ)
 
(15) 
and the rotational subsystem:

## Page 5

4 
 
߬௫+ ߬௪௫= ܫ௫݌˙ −ݍݎ(ܫ௬−ܫ௭)
߬௬+ ߬௪௬= ܫ௬ݍ˙ −݌ݎ(ܫ௭−ܫ௫)
߬௭+ ߬௪௭= ܫ௭ݎ˙ −݌ݍ(ܫ௫−ܫ௬)
 
(16) 
An alternative and widely accepted approach for deriving the quadrotor dynamic model can be formulated using Newton's laws as defined by 
Eq. (17). 
݉v˙ = ܀݂ˆ஻= ݉݃݁ˆ௭−݂௧܀݁ˆ3 
(17) 
Accordingly, the translational dynamics in the inertial frame are expressed as follows: 
ݔ¨ = −݂௧
݉[ݏ(߶)ݏ(߰) + ܿ(߶)ܿ(߰)ݏ(ߠ)] 
ݕ¨ = −݂௧
݉[ܿ(߶)ݏ(߰)ݏ(ߠ) −ܿ(߰)ݏ(߶)] 
(18) 
ݖ¨ = ݃−݂௧
݉[ܿ(߶)ܿ(ߠ)] 
For small Euler angles, the relationships [߶˙ߠ˙߰˙]்= [݌ݍݎ]் hold as good approximations. 
Thus, the linearized quadrotor dynamic model in the inertial frame can be written as: 
ݔ¨ = −݂௧
݉[ݏ(߶)ݏ(߰) + ܿ(߶)ܿ(߰)ݏ(ߠ)] + ݂௪௫
݉ 
ݕ¨ = −݂௧
݉[ܿ(߶)ݏ(߰)ݏ(ߠ) −ݏ(߶)ܿ(߰)] + ݂௪௬
݉ 
(19) 
ݖ¨ = ݃−݂௧
݉[ܿ(߶)ܿ(ߠ)] + ݂௪௭
݉ 
The rotational (angular) sub-system corresponding to roll, pitch, and yaw angles is then given as: 
߶˙ = ܫ௬−ܫ௭
ܫ௫
ݍݎ+ ߬௫
ܫ௫
−߬௪௫
ܫ௫
 
ߠ˙ = ܫ௭−ܫ௫
ܫ௬
݌ݎ+ ߬௬
ܫ௬
−߬௪௬
ܫ௬
 
߰˙ = ܫ௫−ܫ௬
ܫ௭
݌ݍ+ ߬௭
ܫ௭
−߬௪௭
ܫ௭
 
(20) 
 
If the state vector is defined as 
ݔ= [߶, ߠ, ߰, ݌, ݍ, ݎ, ݑ, ݒ, ݓ, ܺ, ܻ, ܼ]்∈ℝ12 
(21) 
the quadrotor dynamic equations can be re-expressed in state-space form using the previously derived relationships, as: 
݌˙ = ݍݎܫ௬−ܫ௭
ܫ௫
+ 1
ܫ௫
(߬௫+ ߬௪௫) 
ݍ˙ = ݌ݎܫ௭−ܫ௫
ܫ௬
+ 1
ܫ௬
(߬௬+ ߬௪௬) 
ݎ˙ = ݌ݍܫ௫−ܫ௬
ܫ௭
+ 1
ܫ௭
(߬௭+ ߬௪௭) 
(22) 
The angular kinematics are given by: 
߶˙ = ݌+ ݎܿ(߶)ݐ(ߠ) + ݍݏ(߶)ݐ(ߠ) 
ߠ˙ = ݍܿ(߶) −ݎݏ(߶) 
(23) 
߰˙ = ݎܿ(߶)
ܿ(ߠ) + ݍݏ(߶)
ܿ(ߠ) 
The translational dynamics in the body frame are obtained as: 
ݑ˙ = ݎݒ−ݍݓ+ ݃ݏ(ߠ) + ݂௪௫
݉ 
ݒ˙ = ݌ݓ−ݎݑ−݃ݏ(߶)ܿ(ߠ) + ݂௪௬
݉ 
(24) 
ݓ˙ = ݍݑ−݌ݒ+ ݃ܿ(߶)ܿ(ߠ) + ݂௪௭
݉−݂௧
݉ 
Finally, the position kinematics in the inertial frame are expressed as: 
ܺ‾˙ = ݓ[ݏ(߶)ݏ(߰) + ܿ(߶)ܿ(߰)ݏ(ߠ)] −ݒ[ܿ(߶)ݏ(߰) −ݏ(߶)ݏ(ߠ)ܿ(߰)] + ݑ[ܿ(ߠ)ܿ(߰)] 
ܻ˙ = ݓ[−ݏ(߶)ܿ(߰) + ܿ(߶)ݏ(߰)ݏ(ߠ)] + ݒ[ܿ(߶)ܿ(߰) + ݏ(߶)ݏ(߰)ݏ(ߠ)] + ݑ[ܿ(ߠ)ݏ(߰)] 
(25) 
ܼ˙ = ݓ[ܿ(߶)ܿ(ߠ)] −ݑ[ݏ(ߠ)] + ݒ[ܿ(ߠ)ݏ(߶)] 
4. 
Controller Design 
In this section, a two-loop controller is developed for trajectory tracking of the quadrotor system. The control structure consists of two main 
components: 
an Adaptive Fuzzy Feedback Linearization Controller (AFFLC) utilized in the inner loop, and a Sliding Mode Controller (SMC) applied in 
the outer loop for improved robustness against disturbances and parameter uncertainties. 
The overall configuration of the dual-loop position control system for the quadrotor is illustrated in Figure 1. 
As shown in that figure, the inner loop is responsible for stabilizing the dynamic attitude variables (߶, ߠ, ߰). while the outer loop ensures 
accurate position tracking in the ݔ, ݕ, ݖ axes. 
The proposed inner-loop AFFLC employs a fuzzy adaptive mechanism to estimate uncertain parameters and compensate for model 
nonlinearities in real time. 
Meanwhile, the outer-loop Sliding Mode Controller is adopted due to its inherent insensitivity to external disturbances and model mismatches, 
providing strong robustness and finite-time convergence properties. 
Consequently, the integrated dual-loop control structure achieves high-precision trajectory tracking performance for the quadrotor in the 
presence of system uncertainties, external disturbances, and dynamic coupling effects.

## Page 6

5 
 
The synergistic combination of fuzzy adaptive estimation (for handling parametric and structural uncertainties) and sliding-mode control (for 
robustness against matched perturbations) ensures superior overall system stability. 
A schematic of this hybrid control framework, incorporating the Parameter-Fuzzy-Based Adaptive Feed-Forward Linearization Controller 
(PFTC), is depicted in Figure 1 in the next section. 
Figure 1 Block diagram of the hybrid dual-loop position control system for quadrotor UAVs integrating Adaptive Fuzzy Feedback 
Linearization Controller (AFFLC) in the inner loop and Sliding Mode Controller (SMC) in the outer loop. 
The illustrated control architecture employs a dual-loop structure to ensure precise position tracking and robust attitude regulation for 
quadrotor UAVs. 
The outer loop comprises a Sliding Mode Controller (SMC) dedicated to position dynamics, providing resilience against parameter 
uncertainties and external disturbances. The inner loop contains an Adaptive Fuzzy Feedback Linearization Controller (AFFLC) that operates 
on the nonlinear quadrotor model to stabilize attitude angles ( ߶, ߠ, ߰ ) and vertical position ݖ. A fuzzy logic-based adaptation law continuously 
updates controller parameters in real time, based on the measured altitude error ݁௭, ensuring efficient compensation for nonlinearities in the 
UAV dynamics. The coordinated interaction between the inner and outer loops delivers smooth, accurate trajectory tracking with high 
robustness in complex flight conditions. 
 
Figure 1. Block diagram of the hybrid dual-loop position control system for quadrotor UAVs 
5. 
Design of the Inner Loop Controller (AFFLC) 
In this section, the Adaptive Fuzzy Feedback Linearization Controller (AFFLC) is designed to regulate the altitude and attitude subsystems of 
the quadrotor. Beginning with the nonlinear dynamic equations, the feedback linearization approach is employed under the assumption of 
model parameter uncertainty. To ensure robustness, the adaptive laws are incorporated to estimate uncertain parameters according to Lyapunov 
stability theory. 
The altitude and attitude subsystem dynamics are written in a general nonlinear form as 
ܼ¨ = ݂4×1(ܼ) + ܾ(ܼ)4×4ݑ 
(26) 
where 
ܼ= [ݖ, ߶, ߠ, ߰]் is the state vector (altitude and Euler angles), and ݑ= [ݑ1,ݑ2, ݑ3, ݑ4]் represents the control inputs. 
The nonlinear functions ݂(ܼ) and ܾ(ܼ) are described as follows: 
(ܼ) =
[
 
 
 
 
 
 
 
−݃
߰˙ߠ˙ (ܫ௫−ܫ௭
ܫ௭
)
߶˙߶˙ (ܫ௭−ூ೥
ܫ௭
)
߶˙ߠ˙ (ܫ௭−ܫ௬
ܫ௭
)]
 
 
 
 
 
 
 
, ܾ(ܼ) = [
cos⁡(ߠ)cos⁡(߶)
݉
0
0
0
,
݈
ܫ௫
0
0
݈
ܫ௬
]
 
(27) 
I. 
Feedback Linearization Control Law 
To cancel the nonlinearities, the control signal is formulated as 
ݑ= ܾ(ܼ)−1[ݒ−݂(ܼ)] 
(28) 
where ݒ is a new auxiliary input vector defined as 
ݒ= ܼ¨ௗ+ ܭ௩ܧ˙ + ܭ௣ܧ 
(29) 
with the error terms ܧ= ܼௗ−ܼ and ܧ˙ = ܼ˙ௗ−ܼ˙. ܭ௩ and ܭ௣ are positive-definite diagonal gain matrices. 
Substituting Eq. (28) into Eq. (29) yields the final control signal as 
By substituting Eq. (30) into the system model, the closed-loop tracking error dynamics become:

## Page 7

6 
 
ݑ=
[
 
 
 
 
 
 
݉
cos⁡(ߠ)cos⁡(߶)
0
0
0
0
ܫ௫
݈
0
0
0
0
ܫ௬
݈
0
0
0
0
ܫ௭]
 
 
 
 
 
 
(
 
 
ݖ¨ௗ
߶¨ௗ
ߠ¨ௗ
߰¨ௗ]
  
 
 
+ [
݇௩1
0
0
0
0
݇௩2
0
0
0
0
݇௩3
0
0
0
0
݇௩4
]
[
 
 
 ݁˙௭
݁˙థ
݁˙ఏ
݁˙ట]
 
 
 
(Δ −Δ)
+
[
 
 
 
 ݇௣1
0
0
0
0
݇௣2
0
0
0
0
݇௣3
0
0
0
0
݇௣4]
 
 
 
 
[
݁௭
݁థ
݁ఏ
݁ట
] −
[
 
 
 
 
 
 
 
−݃
ߠ˙߰˙ (ܫ௬−ܫ௭
ܫ௫
)
߶˙߰˙ (ܫ௭−ܫ௫
ܫ௬
)
ߠ˙߶˙ (ܫ௫−ܫ௬
ܫ௭
)]
 
 
 
 
 
 
 
)
 
 
 
 
 
 
 
(30) 
If we define the virtual control as 
ܼ˙ ∗= ܼ˙ௗ−ܭ௩ܧ˙ −ܭ௣ܧ 
(31) 
then Eq. (26) can be rewritten following the standard mechanical model as 
߬= ܯ(ܼ, ݌)ܼ¨ + ܥ(ܼ, ܼ˙, ݌) 
(32) 
where ݌= [݉, ܫ௫, ܫ௬, ܫ௭]
் denotes the parameter vector, and the inertia- and Coriolis-related matrices are defined as follows: 
ܯ(ܼ, ݌) = ܾ−1(ܼ) =
[
 
 
 
 
 
 
݉
cos⁡(ߠ)cos⁡(߶)
0
0
0
0
ܫ௫
݈
0
0
0
0
ܫ௬
݈
0
0
0
0
ܫ௭]
 
 
 
 
 
 
ܥ(ܼ, ܼ˙,݌) = −ܾ−1(ܼ)݂(ܼ) =
[
 
 
 
 
 
 
 
݉݃
cos⁡(ߠ)cos⁡(߶)
ߠ˙߰˙ (ܫ௭−ܫ௬
݈
)
߶˙߰˙ (ܫ௫−ܫ௭
݈
)
ߠ˙߶˙(ܫ௬−ܫ௫) ]
 
 
 
 
 
 
 
 
(33) 
By substituting Eq. (31) into Eq. (32), the final control signal can be represented as 
ݑ= ܯ(ܼ, ݌)ܼ˙∗+ ܥ(ܼ, ܼ˙, ݌) 
(32) 
and according to Eq. (31): 
ܼ˙ ∗= ܼ˙ௗ−ܭ௩ܧ˙ −ܭ௣ܧ 
(32) 
II. 
Adaptive Feedback Linearization with Parameter Estimation 
If the parameter vector ࢖ of the quadrotor is uncertain and its exact value is not available, the dynamic model defined by the inertia and 
Coriolis matrices ܯ(ܼ, ݌) and ܥ(ܼ, ܼ˙, ݌) will be affected by parameter mismatches. Denoting the estimated parameters by ݌̂, the control signal 
is written as 
ܼ˙ ∗= ܼ˙ௗ−ܭ௩ܧ˙ −ܭ௣ܧ 
(33) 
By substituting the control law (Eq. (12)) into the dynamic model (Eq. (7-5)), the closed-loop expression becomes 
ܯˆ (ܼ, ݌ˆ)ܼ¨ + ܥˆ(ܼ, ܼ˙, ݌ˆ) = ܯ(ܼ, ݌)(−ܧ¨ −ܭ௩ܧ˙ −ܭ௣ܧ) 
(34) 
where ઴= ࢖−࢖ˆ  indicates the parameter estimation error, and the difference relations 
ܥ= ܥˆ −ܥ, ܯ= ܯˆ −ܯ 
(35) 
represent parameter uncertainties. 
Accordingly, the error dynamics considering parameter uncertainty can be expressed as 
ܧ¨ + ܭ௩ܧ˙ + ܭ௣ܧ= −ܯ−1(ܼ, ݌)[ܯ˜ (ܼ, Φ)ܼ¨ + ܥ˜(ܼ, ܼ˙, Φ)] 
(36) 
The modeling discrepancies in ܯ and ܥ with respect to parameter error Φ can be denoted by 
ܯ˜ (ܼ, Φ)ܼ¨ + ܥ˜(ܼ, ܼ˙, Φ) = ܹ(ܼ, ܼ˙, ܼ¨)Φ 
(37) 
where ܹ(ܼ, ܼ˙, ܼ¨) is a non-linear matrix describing parameter-dependent dynamic errors and defined as 
ܹ(ܼ, ܼ˙, ܼ¨) =
[
 
 
 
 
 
݃+ ܼ¨
cos⁡(ߠ)cos⁡(߶)
0
0
0
0
߶¨
−ߠ˙߰˙
ߠ˙߰˙
0
߶˙߰˙
ߠ¨
−߶˙߰˙
0
−ߠ˙߶˙
ߠ˙߶˙
߰¨
]
 
 
 
 
 
 
(38) 
Thus, the error dynamics can be rewritten as 
ܧ¨ + ܭ௩ܧ˙ + ܭ௣ܧ= −ܯ−1(ܼ, ݌ˆ)ܹ(ܼ, ܼ˙, ܼ¨)Φ 
(39) 
To verify Lyapunov stability under the AFFLC control law given by Eq. (17), the second-order differential system can be expressed in state-
space form as 
ܺ˙ = ܣܺ+ ܤݑ, ݑ= −ܯ−1ܹΦ 
(40)

## Page 8

7 
 
ܧ= ܥ1ܺ 
where ܣ and ܥ1 are the state and output matrices, respectively. 
Defining the auxiliary output variable 
ܧ1 = ܧ˙ + Ψܧ, ܧ1 = ܥܺ 
(41) 
With properly selected scalar gain Ψ, the Kalman-Yakubovich-Popov lemma ensures the feasibility of the following relations for stability: 
ܣ்ܲ+ ܲܣ= −ܳ, ܲܤ= ܥ் 
(42) 
where ܲ and ܳ are symmetric positive-definite matrices of appropriate dimensions. 
The Lyapunov function candidate for the system in Eq. (18) under the input ݑ= −ܯ−1(ܼ, ݌ˆ)ܹ(ܼ, ܼ˙, ܼ¨)Φ is chosen as 
ܸ= ்ܺܲܺ+ Φ்Γ−1Φ 
(43) 
Taking the time derivative of ܸ gives 
ܸ˙ = ்ܺܲܺ˙ + ܺ˙ ்ܲܺ+ 2Φ்Γ−1Φ˙  
(44) 
Substituting ܺ˙ = ܣܺ+ ܤݑ and simplifying yields 
ܸ˙ = ்ܺܳܺ+ 2ݑ்ܧ1 + 2Φ்Γ−1Φ˙  
(45) 
The adaptive law for parameter tuning is selected as 
Φ = Γ்ܹܯ−1ܧ 
(46) 
Thus, the derivative of the Lyapunov function becomes 
ܸ˙ = −்ܺܳܺ 
(47) 
By positive definiteness of ܳ, ܸ˙  remains non-positive, confirming asymptotic convergence of ܧ and boundedness of Φ. The adaptive parameter 
update rate follows from differentiating Eq. (25): 
Φ˙ = −Γ்ܹܯ−1ܧ1 
(48) 
According to Eq. (48), the adaptive fuzzy feedback term Φ guarantees real-time adjustment of the uncertain parameters. The control law ݑ=
−ܯ−1ܹΦ thereby produces a stable closed-loop response where both position and attitude errors asymptotically converge to zero. 
Consequently, within the altitude and attitude subsystems governed by feedback linearization, this adaptive term enforces coordination 
between estimated and real parameters, ensuring robust tracking in the presence of modeling uncertainties. 
In this section, the Mamdani inference method combined with the center-of-gravity defuzzification technique is employed for the fuzzy 
controller design. Figure 2 illustrates the membership functions corresponding to the input variable - the output error (Z). Five Gaussian-type 
membership functions are defined to cover the full range of the variable, from strongly negative to strongly positive values. These regions, 
denoted as NB (Negative Big), NS (Negative Small), Z (Zero), PS (Positive Small), and PB (Positive Big), provide overlapping transitions 
that enable smooth inference across different operating conditions. 
The selected structure ensures that the fuzzy controller responds continuously and adaptively to variations in the output error. The overlapping 
nature of the membership functions prevents abrupt changes in the control signal, improves robustness against noise, and guarantees stable 
performance near the equilibrium point. 
 
Figure 2. Membership Functions for the Input Variable (Output Error Z) 
Figure 3 illustrates the membership functions defined for the output variable (adaptive gain ܇ ) in the fuzzy inference system. Three Gaussian-
type membership functions are employed, corresponding to the linguistic terms S (Small), M (Medium), and B (Big). The domain of ߛ spans 
the normalized range [ 0,0.1 ], ensuring a smooth and continuous variation of the adaptive gain. This configuration enables precise fine-tuning 
of the controller's output to maintain system stability and performance. The overlapping nature of the membership functions provides soft 
transitions between control actions, preventing abrupt changes and ensuring robustness under parameter variations or disturbances. 
Consequently, the design supports appropriate mapping between the fuzzy input (errorZ) and output (adaptive gain ߛ ), improving convergence 
speed and adaptive behavior of the overall AFFLC structure.

## Page 9

8 
 
 
Figure 3. Membership Functions for the Output Variable (Adaptive Gain Y) 
 
Figure 4 illustrates the relationship between the fuzzy input (error Z) and output (adaptive gain γ) derived from the previously defined 
membership functions and rule base. As observed, the adaptive gain γ increases non-linearly with the magnitude of the input error. The 
mapping exhibits asymmetrical slopes, reflecting the influence of the fuzzy membership functions introduced earlier. Specifically, small errors 
correspond to a low adaptive gain, allowing smooth control near equilibrium, while larger error magnitudes trigger higher adaptive gains to 
accelerate convergence. This nonlinear correlation enhances the controller’s adaptability, ensuring robust performance and stable transient 
response in the AFFLC system. 
 
 
 
 
Figure 4. Relationship Between the Fuzzy Input and Output Sets 
In this part, an external-loop sliding mode controller (SMC) is designed to achieve trajectory tracking of the UAV position. The main objective 
of this controller is to ensure precise position regulation, while compensating for external disturbances and model uncertainties. Unlike purely 
linear controllers, the sliding mode structure provides higher robustness and fast transient response, which makes it ideal for outer-loop control 
in hierarchical UAV architectures. 
The dynamic behavior of the UAV in the translational subsystem can be described by nonlinear equations; therefore, the position controller 
is constructed to guarantee system stability and asymptotic tracking of reference coordinates ( ݔௗ, ݕ௧ ). Using the reference inputs from the 
inner control loop (similar to Section 4), the control laws governing the translational channel are expressed as follows: 
ݑ௫= ݉
ݑ1
(ݔ¨ௗ+ ߣ௫(ݔ˙ௗ−ݔ˙) + ߟ௫ݏ௫+ ݇௫sgn(ݏ௫)) 
ݑ௬= ݉
ݑ1
(ݑ¨ ௗ+ ߣ௬(ݕ˙ௗ−ݕ˙) + ߟ௬ݏ௬+ ݇௬sgn(ݏ௬)) 
(49) 
where ݑ1 is the collective thrust obtained from the inner control loop, and parameters ݇௫, ݇௬, ߟ௫, ߟ௬, ߣ௫, ߣ௬ are controller gains. The sliding 
surfaces in the ࢞ - and ࢟-directions are defined as 
ݏ௫= ݁˙௫+ ߣ௫݁௫, ݏ௬= ݁˙௬+ ߣ௬݁௬ 
(50) 
with ݁௫= ݔௗ−ݔ and ݁௬= ݕௗ−ݕ denoting position tracking errors. 
To generate appropriate reference attitude angles (roll ࣘ and pitch ߠ ) for the inner rotational loop, the following transformation is employed: 
߶ௗ= sin−1 (ݑ௫sin(߰ௗ) −ݑ௬cos(߰ௗ)
ݑ1
) 
(51)

## Page 10

9 
 
ߠௗ= sin−1⁡(ݑ௫cos⁡(߰ௗ) + ݑ௬sin⁡(߰ௗ)
↓cos⁡(߶ௗ)
) 
Here, ߰ௗ represents the desired yaw angle, which is typically determined by a supervisory trajectory planner. 
The inverse-sine terms are valid under the range constraints −
గ
2 < ߶ௗ, ߠௗ<
గ
2, ensuring physically realizable outputs for the control signals. 
It is worth noting that, for overall system performance, the inner (attitude) control loop must exhibit faster dynamics than the outer (position) 
loop. This hierarchical speed separation guarantees robustness and prevents oscillatory coupling between the two control layers. Finally, the 
stability of the proposed SMC can be verified using Lyapunov stability theory in the same manner as that applied to the fractional-order sliding 
mode controller described in the previous section. 
6. 
Simulation Results 
In this section, the simulation outcomes obtained using the designed controllers are presented. All simulations were conducted in the MATLAB 
Simulink 2020b environment. 
The proposed tracking tasks include two distinct flight scenarios adopted from reference [57]. In the first scenario, the UAV tracks a reference 
trajectory based on [17], while in the second scenario, the UAV follows the same path but under external disturbance. This setup enables 
evaluation of the control law's robustness and adaptability. 
The purpose of these simulations is to compare the performance of the proposed Adaptive Fuzzy Feedback Linearization Controller (AFFLC) 
with those of conventional Sliding Mode Control (SMC). Adaptive Feedback Linearization Control (AFLC), and classical Fuzzy Linearization 
Control (FLC). 
The UAV's dynamical parameters used in all simulations are listed in Table 5-10, and the simulation begins with zero initial conditions for 
positions and attitude angles. The controller gain matrices ܭ௣ and ܭ௩ are both 10 × 10 diagonal matrices with diagonal entries equal to 10 ( 
ܭ௣= ܭ௩= 10ܫ ). The uncertainty adaptation coefficients ߟ and ߛ used in the adaptive laws are also set to unity for both translational ( ݔ, ݕ ) 
and altitude channels. 
I. 
Scenario 1 
In this subsection. Scenario 1 is analyzed to investigate the performance of the proposed controllers. The desired trajectory was adapted from 
reference [57], with the UAV commanded to track a smooth reference path at an initial pitch angle of 15∘. The purpose of this test is to 
compare the position-tracking accuracy and disturbance-rejection capability of the proposed AFFLC controller with conventional approaches. 
The UAV control parameters are defined as follows  table 1: 
Table 1. Quadrotor Parameters 
Parameter 
Value 
݉( kg) 
2 
݈( m) 
0.23 
݀( N ⋅ m ⋅ s2) 
0.0000075 
ܾ( N ⋅ s2) 
0.000313 
ܫ௫( N ⋅ s2/rad) 
0.0075 
ܫ௬( N −s2/rad) 
0.0075 
ܫ௭( N ⋅ s2/rad) 
0.013 
݃( m/s2) 
9.81 
 
This outcome confirms that the controller maintains robust performance against time-varying disturbances and parameter uncertainties. The 
inner loop operates quickly enough to correct deviations in real time, ensuring stable and accurate tracking throughout the mission. 
Figure 5 illustrates the comparative trajectory-tracking responses of the proposed Adaptive Fuzzy Feedback Linearization Controller (AFFLC) 
against traditional control schemes, including Sliding Mode Control (SMC), Fuzzy Linearization Control (FLC), and Adaptive Feedback 
Linearization Control (AFLC). The plots show the UAV’s altitude (z), longitudinal (x), and lateral (y) positions relative to the reference 
trajectory. As observed, the AFFLC (green curve) achieves the most accurate and rapid convergence with minimal overshoot and negligible 
steady-state error, even under transient disturbances—especially around t=25 s, highlighted in the zoomed-in view. This demonstrates the 
AFFLC’s superior adaptability and robustness arising from its online fuzzy gain adjustment. In contrast, the AFLC and FLC exhibit slower 
transient recovery, while SMC suffers slight chattering. Overall, the AFFLC ensures smooth, precise, and stable path tracking in all three 
spatial coordinates.

## Page 11

10 
 
 
Figure 5. Trajectory Tracking Performance for the Desired Path Presented in Reference [57] 
Figure 6 presents the time responses of the four rotor angular velocities (Ω1–Ω4) under Scenario 1 using four distinct control strategies: SMC, 
FLC, AFLC, and the proposed AFFLC. All controllers stabilize the rotor speeds within approximately the same steady-state region around 
500 rad/s; however, the transient behaviors differ notably. The AFFLC achieves the smoothest convergence with minimal overshoot and 
almost no oscillations, demonstrating excellent damping and adaptability. The SMC exhibits the fastest rise time but also introduces higher 
chattering, while the FLC and AFLC maintain moderate responses with slightly slower settling times. These results clearly indicate that the 
adaptive fuzzy feedback linearization mechanism enhances robustness and smooth control effort, ensuring stable and well-coordinated motor 
dynamics throughout the mission duration. 
 
 
 
Figure 6. Rotor Angular Velocities of the Quadrotor in Scenario 1 
Figure 7 illustrates the evolution of the quadrotor's attitude angles-roll (߶), pitch (ߠ), and yaw (߰) − under Scenario 1 for four control 
strategies: SMC, FLC, AFLC, and the proposed AFFLC. The results demonstrate that all controllers maintain the desired orientation with 
acceptable transient performance; however, distinct differences emerge in smoothness and precision. 
The AFFLC shows the most stable and well-damped response across all attitude channels, with minimal overshoot and negligible steady-state 
deviation. Both roll and pitch angles quickly converge to zero following transient perturbations, while yaw accurately tracks the reference 
command ( ≈૙. ૞ ܚ܉܌ ) and smoothly returns to equilibrium near ݐ= 65 s. 
In contrast, the SMC response exhibits noticeable high-frequency chattering in the roll and pitch channels, whereas FLC and AFLC achieve 
stable convergence but with slightly slower settling. Overall, the results confirm that the AFFLC provides superior orientation stability and 
disturbance rejection, offering a smoother control effort and improved dynamic coordination of the quadrotor's attitude during flight.

## Page 12

11 
 
 
Figure 7. Quadrotor Attitude Angles ( ߶, ߠ, ߰ ) in Scenario 1 
Figure 8 depicts the time evolution of the adaptive fuzzy gain ߛ(ݐ) during Scenario 1 under the proposed Adaptive Fuzzy Feedback 
Linearization Controller (AFFLC). The gain ࢽ dynamically adjusts according to real-time tracking error and system disturbances. Initially, ߛ 
remains nearly constant at a small nominal value ( ≈0.017 ), ensuring smooth control effort during steady flight. At approximately ݐ= 25 s, 
a significant transient event occurs, causing a sudden spike of ߛ up to about 0.078 . This rapid increase reflects the fuzzy adaptation 
mechanism's response to compensate for the abrupt tracking error or external disturbance. 
After the transient subsides, ߛ automatically decreases and gradually returns to its nominal value, indicating successful error mitigation and 
controller stabilization. Around ݐ= 60 s, a smaller adjustment appears, corresponding to a minor trajectory correction. Overall, the adaptive 
behavior of ߛ highlights the AFFLC's ability to self-tune control intensity in real time, enhancing robustness, minimizing steady-state error, 
and ensuring smooth, energy-efficient quadrotor performance. 
 
 
Figure 8. Adaptive Gain ߛ in Scenario 1 
Figure 9 illustrates the 3D trajectory tracking performance of the quadrotor under Scenario 1, where the Adaptive Fuzzy Feedback 
Linearization Controller (AFFLC) is used to follow the reference path denoted by the dashed line (ref). The simulation plot presents the spatial 
motion along the ݔ, ݕ, and ݖ axes, with a magnified inset highlighting the zoomed region around ݔ≈0.3 m and ݖ≈0.55 m to show local 
precision. As can be seen, the AFFLC-controlled trajectory (solid blue line) aligns almost perfectly with the reference commands, maintaining 
exceptional accuracy throughout the flight-both during vertical and lateral transitions. The zoomed-in region reveals negligible deviation, 
confirming that the adaptive fuzzy gain adjustment successfully compensates for nonlinearities and coupling effects among the translational 
and rotational motions. 
This superior 3D tracking performance demonstrates the robust dynamic adaptation capabilities of the AFFLC, providing smooth and precise 
trajectory convergence with minimal steady-state error, even during segments involving abrupt altitude and orientation changes.

## Page 13

12 
 
 
Figure 9. Three-Dimensional Position Tracking in Scenario 1 
II. 
Scenario2 
In this section, the controller's tracking performance is evaluated under Scenario2, which includes the effect of an external load disturbance 
[17]. Specifically, a payload equivalent to 2 kg is applied at t = 30 s and gradually removed at ܜ= 40 s. The corresponding payload torque 
and reference yaw angle are also considered. It should be noted that this added mass represents approximately 20 newtons-equivalent to a 
realistic quadrotor payload. 
Overall, these results demonstrate that the proposed AFFLC method offers superior adaptability and steady-state accuracy compared to 
classical controllers. It provides rapid compensation during load variations, smooth attitude recovery, and stable position tracking under 
external torque and mass disturbances. 
Figure 10 presents the trajectory tracking performance of the quadrotor along the reference path [17] under a payload disturbance condition 
corresponding to Scenario2. The three subplots depict the altitude ݖ(ݐ), longitudinal ݔ(ݐ), and lateral ݕ(ݐ) tracking responses for different 
control strategies-SMC, FLC, AFLC, and the proposed AFFLC—compared with the reference trajectory (ref). Two magnified insets highlight 
critical intervals around ݐ= 20 −25 s and ݐ= 35 −38 s, in which a 2 kg payload is applied and then removed. The results demonstrate that 
the Adaptive Fuzzy Feedback Linearization Controller (AFFLC) achieves nearly perfect path tracking with minimal overshoot and transient 
deviation after the payload is introduced, whereas the SMC and FLC controllers exhibit larger oscillations and recovery delays. This confirms 
the superior adaptability, robustness, and disturbance rejection capability of the AFFLC scheme during dynamic load variations. 
 
 
Figure 10. Reference Path Tracking under Payload Disturbance (Scenario2) 
Figure 11 presents the rotor angular velocity responses (Ω1 to Ω4) of the quadrotor in Scenario2, where a 2 kg payload disturbance is applied 
between ݐ= 30 s and ݐ= 40 s. The results compare the performance of the SMC, FLC, AFLC, and the proposed AFFLC controllers. 
As shown, when the external payload is introduced, all four rotors experience considerable fluctuations in their angular velocities. The SMC 
and FLC methods exhibit evident chattering and oscillatory responses, which intensify near the disturbance intervals due to imperfect 
estimation and discontinuous control action. The AFLC achieves smoother transients but still displays small amplitude oscillations during 
load variation. In contrast, the proposed AFFLC approach maintains stable, continuous, and low-amplitude responses across all rotors. Its 
adaptive fuzzy mechanism effectively mitigates the impact of sudden torque changes, leading to superior disturbance rejection and robust 
stabilization once the payload is removed. These results confirm the enhanced smoothness and control precision of the AFFLC architecture 
compared with conventional approaches.

## Page 14

13 
 
 
Figure 11. Rotor Angular Velocities( ۿ૚−ષ ) under Payload Disturbance (Scenario2) 
Figure 12 illustrates the attitude angle responses-roll (߶), pitch (ߠ), and yaw (߰)-for the quadrotor during Scenario 2 , where a 2 kg payload 
disturbance is applied between ݐ= 30 s and ݐ= 40 s. The results compare the SMC, FLC, AFLC, and the proposed AFFLC controllers. 
The roll and pitch responses reveal that SMC suffers from chattering and high-frequency oscillations, while FLC exhibits imperfect transient 
adaptation, leading to overshoot and minor residual oscillations after the disturbance. AFLC shows improved damping, yet slight fluctuations 
remain during load variation. In contrast, the AFFLC maintains exceptional stability, with minimal overshoot and smooth recovery to nominal 
values, even under sudden load changes. 
Yaw response ( ߰ ) is consistently stable across all controllers, but only the AFFLC achieves perfectly smooth convergence without transient 
spikes. These results confirm that the AFFLC's adaptive fuzzy gain mechanism effectively suppresses attitude disturbances, yielding superior 
robustness and precise stabilization compared with conventional controllers. 
 
 
 
Figure 12. Euler Angles ( ߶, ߠ, ߰ ) under Payload Disturbance (Scenario2) 
Figure 13 depicts the mass estimation response ( ݉ˆ  ) of the quadrotor during Scenario2, where a 2 kg payload is applied at ݐ= 30 s and 
removed at ݐ= 40 s. The plot compares the true mass + payload profile (black curve) with the estimates obtained using the AFLC and the 
proposed AFFLC controllers. 
Upon the payload application, both controllers detect and adjust their mass estimates toward the new value ( ≈4 kg ). The AFFLC achieves 
a faster and smoother convergence with minimal overshoot compared to AFLC, reflecting its superior adaptation and estimation accuracy 
under sudden load changes. Similarly, when the payload is removed, the AFFLC demonstrates a prompt return to the nominal mass ( 2 kg ), 
whereas AFLC exhibits a slightly delayed and less precise recovery. These results confirm the AFFLC's enhanced disturbance adaptation 
capability and its robustness in maintaining accurate mass estimation during dynamic load variations.

## Page 15

14 
 
 
Figure 13. Estimated Mass and Applied Payload in Scenario 2 
 
Figure 14 shows the adaptive gain ߛ(ݐ) time history produced by the AFFLC controller during Scenario 2, where a 2 kg payload is applied at 
ݐ= 20 s and removed at ݐ= 40 s. 
Initially, ߛ remains close to its nominal baseline value ( ≈0.017 ), indicating no load disturbance. Upon payload application at ݐ= 20 s, the 
gain rapidly increases to a peak of ≈0.078, enabling the controller to generate stronger corrective action to counteract the added mass and 
resulting perturbations. This spike is followed by a gradual decay as the inner-loop error reduces and the system stabilizes under the new load. 
At ݐ= 40 s, the payload is removed, triggering a second sharp rise in ߛ (peak ≈0.072 ) to handle the sudden unloading and resulting transient 
dynamics. Again, the gain smoothly decays back to the nominal value as post-disturbance stabilization is achieved. 
These results confirm that the AFFLC's adaptive fuzzy gain mechanism dynamically adjusts its corrective authority in real-time, ensuring fast 
disturbance rejection and maintaining high tracking accuracy, both when the external load is introduced and when it is removed. 
 
 
Figure 14. Adaptive Gain ߛ Estimation in Scenario2 
III. 
3D Reference Path Tracking in Scenario2 
Figure 15 presents the three-dimensional trajectory tracking performance of the proposed Adaptive Fuzzy-based Feedforward Learning 
Controller (AFFLC) under Scenario2, where a 2 kg payload disturbance is applied at ݐ= 30 s and removed at ݐ= 40 s. The reference path 
follows a helical trajectory characterized by continuous variations in ݔ, ݕ, and ݖ coordinates. 
As seen in the figure, the AFFLC trajectory (blue) maintains an almost perfect overlap with the reference path (dashed orange) throughout the 
entire flight, even during the periods of sudden mass variation. The response remains smooth and highly consistent across all spatial axes, 
with no visible deviation or phase lagdemonstrating rapid disturbance rejection and precise dynamic adaptation. 
These results confirm the AFFLC's excellent capability for real-time nonlinear compensation and robust path tracking under external load 
variations. The controller successfully preserves trajectory integrity under both loading and unloading conditions, validating its stability and 
superior adaptation in complex multi-axis flight scenarios.

## Page 16

15 
 
 
 
Figure 15. presents the three-dimensional trajectory tracking 
The three-dimensional surface presented in Figure 16 illustrates the adaptive gain variation ߛ௙ produced by the fuzzy estimator as a function 
of the instantaneous error ܼ and error rate ܼ˙. The surface shows that the adaptive gain increases sharply when the absolute error and its rate 
are small, providing fast corrective action during transient changes. Conversely, when both |ܼ| and |ܼ˙| grow larger-indicating higher 
uncertainty or high-amplitude deviation-the gain saturates to a limited value, thereby preventing excessive control effort and chattering. This 
behavior confirms that the fuzzy estimator effectively modulates the adaptive gain in a nonlinear, self-organizing manner-yielding high-speed 
convergence near equilibrium and enhanced robustness against abrupt disturbances in the control loop. 
 
 
Figure 16. Adaptive Gain Surface of Fuzzy Estimator 
 
The transient behavior illustrated in Figure 17 compares the tracking performance of four control strategiesSMC, FLC, AFLC, and the 
proposed AFFLC-in terms of position error over time. The conventional SMC (black curve) exhibits rapid convergence but produces 
pronounced oscillations due to the chattering phenomenon. The FLC (green dashed line) achieves smoother dynamics yet converges more 
slowly, indicating limited adaptability to real-time disturbances. The AFLC (red dash-dot line) accelerates the error decay compared to FLC 
by incorporating adaptive mechanisms, but small steady-state residuals persist. In contrast, the proposed AFFLC (blue solid line) successfully 
combines adaptive fuzzy gain-tuning with feedback linearization, yielding the smallest overshoot and fastest stabilization. This highlights its 
superior dynamic response and robustness, effectively suppressing oscillations while maintaining high tracking precision.

## Page 17

16 
 
 
Figure 17. Comparison of Tracking Errors under Different Controllers 
Figure 18 illustrates the performance of the adaptive mass estimation mechanism during a sudden payload variation occurring at ݐ= 30 s. 
The true mass (black dashed line) exhibits an instantaneous jump from 3.0 kg to 5.0 kg , representing the applied load change. The AFLC (red 
dash-dot line) tracks this variation with a relatively slow convergence and a slight estimation lag, stabilizing after a short transient period. In 
contrast, the proposed AFFLC (blue solid line) shows a much faster and smoother adaptation, reaching the true value almost immediately after 
the payload change with negligible overshoot and without oscillatory behavior. This rapid convergence demonstrates the effectiveness of the 
fuzzy adaptive gain tuning embedded in the feedback linearization law, significantly enhancing the system's ability to estimate and compensate 
for mass variations in real time, thereby improving overall control robustness and dynamic stability. 
 
 
Figure 18. Adaptive Mass Estimation Response 
Figure 19 presents the variation of the rotor angular velocity Ω for the four controllers during the disturbance Scenario 2, in which dynamic 
load changes and nonlinear coupling effects are present. The SMC (black line) shows a rapid transient response but suffers from high-
frequency oscillations caused by control chattering. resulting in large torque ripples. The FLC (green dashed curve) substantially reduces 
oscillations but converges more slowly to the nominal velocity. The AFLC (red dash-dot line) accelerates stabilization through adaptive rule 
tuning: however, residual oscillations remain in the early transient phase. By contrast, the Proposed AFFLC (blue solid line) quickly brings 
all rotors to the reference speed of 500rad/s within approximately 1 s and maintains a perfectly steady value thereafter, exhibiting minimal 
overshoot and zero steady-state error. This improved performance highlights the AFFLC's enhanced adaptability and damping capability, 
ensuring smoother torque generation and highly stable UAV attitude control even under nonlinear and time-varying operating conditions. 
 
Figure 19. Rotor Angular Velocities under Scenario 2

## Page 18

17 
 
In this figure 20, Composite time responses for tracking error ez( t ), adaptive gain ߛ(t), and estimated mass hˆm(t) during a payload 
disturbance. The gain ߛ rises with error magnitude, accelerates convergence, and then decays as the error vanishes. The estimated mass tracks 
the true value smoothly, validating the lyapunov-consistent fuzzy adaptation. 
 
Figure 20. Dynamic Interaction of Error Signals and Adaptive Gain 
In this figure 21, Scatter and fitted trend lines across multiple runs reveal the effort-accuracy relationship. AFFLC exhibits a steeper inverse 
correlation, achieving lower tracking error with reduced control energy, whereas SMC requires higher effort for comparable accuracy due to 
switching-induced ripple. 
 
Figure 21. Correlation Between Control Effort and Tracking Precision 
 
The 3-D trajectory shows figure 22 that the proposed AFFLC controller (blue) closely tracks the reference path (black dashed helix) while the 
Benchmark [57] controller (purple) exhibits delayed convergence and residual error. This verifies enhanced dynamic precision and disturbance 
resilience.  
In this figure 23 Combined histories of control inputs ݑ1 −ݑ4 and adaptive gain ߛ(ݐ) for the proposed system and [57]. The AFFLC demands 
smoother, lower-energy control (blue) with fuzzy-adaptive gain tuning, reducing chattering, whereas [57] controller (purple) generates 
stronger peaks and slower adaptation. 
In this figure 24 Mass-estimation ݉ˆ (ݐ) and tracking-error ‖݁(ݐ)‖ comparisons under a 2 kg payload change. AFFLC (blue) converges within 
≈1.5 s with smooth dynamics; the Benchmark lags and leaves a residual error. The result demonstrates the superiority of the fuzzy-adaptive 
Lyapunov estimator in transient handling and robustness. 
 
Figure 22. Trajectory-Tracking Comparison with Reference [57]

## Page 19

18 
 
 
Figure 23. Control Inputs and Adaptive Gain vs. Reference [57] 
 
 
Figure 24. Mass-Estimation and Tracking-Error Convergence vs. Reference [57] 
Figure 25 compares the roll ( ߮ ), pitch ( ߠ ), and yaw ( Ψ ) angle responses of the proposed AFFLC with those reported in [57] under identical 
flight conditions. The AFFLC curves (solid lines) exhibit faster convergence and smaller overshoot across all three attitude axes compared to 
the benchmark controller (dashed lines). Specifically, the roll and pitch responses settle within approximately 10 s with minimal oscillation, 
whereas the reference method in [57] shows delayed convergence and larger transient deviations exceeding 4 degrees. The yaw response also 
demonstrates improved damping and dynamic smoothness under AFFLC, confirming its superior capability in coordinating attitude channels 
and maintaining coupled stability during transients. 
 
Figure 25. Attitude Stabilization Comparison 
Figure 26 demonstrates the altitude regulation performance of the proposed AFFLC compared with the controller from [57] when a +2 kg 
payload is introduced at ݐ= 30 s. The reference altitude ݖௗ (black dashed line) remains constant at1m, while both controllers respond to the 
sudden load increase. The AFFLC (solid blue curve) exhibits a short-duration altitude drop followed by rapid recovery within 2 s , closely 
tracking the command height without significant overshoot. In contrast, the controller of [57] (purple dashed line) shows a pronounced 
transient overshoot ( ≈10% ) and longer settling time. The results highlight the AFFLC's high disturbance rejection capability and adaptive 
adjustment to payload variations, ensuring robust altitude stabilization and minimal steady-state error in real-time flight operations.

## Page 20

19 
 
 
Figure 26. Disturbance Rejection under Payload Variation 
This 
table 
2 
provides 
a 
quantitative 
summary 
of 
the 
dynamic 
performance 
metrics 
for 
the 
Proposed 
Adaptive Fuzzy Feedback Linearization Controller (AFFLC) compared with conventional SMC, FLC, and AFLC schemes during a 
payload-disturbance test (a 2 kg load applied at t = 30 s and removed at t = 40 s). The proposed controller achieves the fastest settling time 
(2.6 s), corresponding to a 35 % improvement over the next-best baseline. It also exhibits the lowest peak overshoot (0.14 m), minimum 
RMS tracking error (0.023 m), and nearly eliminated rotor-speed ripple (< 3 rad/s), representing up to 78 % reduction in chattering. These 
results quantitatively confirm the AFFLC’s superior adaptability and smooth, energy-efficient transient response during abrupt payload 
changes, validating its robustness and real-time implementation potential for UAV flight control. 
Table 2. Quantitative Comparison of Disturbance-Rejection Performance under Payload Variation 
Metric 
SMC 
FLC 
AFLC 
Proposed AFFLC 
Improvement vs. Best Baseline 
Settling time (s) 
3.6 
5.8 
4.1 
2.6 
−35 % 
Peak overshoot (m) 
0.18 
0.32 
0.23 
0.14 
−22 % 
RMS tracking error (m) 
0.042 
0.071 
0.049 
0.023 
−45 % 
Rotor speed ripple (rad/s) 
>20 
8 
5 
< 3 
−78 % 
Table 3 presents the consolidated performance comparison among the SMC, AFLC, FLC, and the Proposed AFFLC–SMC + LAHC hybrid 
control–optimization framework. As observed, the proposed approach achieves the lowest RMS tracking error (0.023 m) and the shortest 
execution time (2.3 s) while converging within approximately 90 iterations, which represents the fastest response among all compared 
methods. In terms of payload disturbance handling, the proposed controller exhibits a fast and stable dynamic reaction, maintaining excellent 
tracking accuracy even under sudden mass variations. Conversely, the conventional SMC shows oscillatory behavior, AFLC provides 
moderate damping, and FLC manifests slow recovery and inferior precision. The overall results position the proposed AFFLC–SMC + LAHC 
framework as the top-ranked (1 ✓) method, confirming its superior stability, rapid convergence, and computational efficiency for real-time 
UAV control and path-planning applications. 
Table 3. Comparative Evaluation of Controllers under Disturbance and Computational Criteria 
Algorithm / 
Controller 
Error RMS (m
) 
Execution Time (s
) 
Convergence Iter
. 
Payload Disturbance Respons
e 
Overall Ran
k 
SMC 
0.042 
4.8 
210 
Oscillatory 
4 
AFLC 
0.049 
3.9 
175 
Medium 
3 
FLC 
0.071 
6.2 
>250 
Slow 
5 
Proposed AFFLC
–SMC + LAHC 
0.023 
2.3 
≈90 
Fast, Stable 
1 (✓) 
7. 
Conclusion  
A novel dual-loop AFFLC–SMC control scheme integrated with an LAHC-based path-planning algorithm has been developed and verified 
through comprehensive simulation studies. Numerical results demonstrate that the proposed controller not only guarantees global boundedness 
and finite-time convergence but also eliminates the chattering typical of standard SMC formulations. The inner fuzzy-linearization layer adapts 
in real time to uncertainty in mass and aerodynamic coefficients, while the outer SMC enforces precise trajectory tracking through 
renormalized sliding variables. 
Through Lyapunov stability analysis, all closed-loop signals are proven uniformly ultimately bounded. The adaptive fuzzy mapping effectively 
balances between transient acceleration and steady-state smoothness—proving particularly beneficial during abrupt payload application and 
removal, where conventional adaptive schemes display oscillations. 
From the optimization perspective, LAHC provides a near-deterministic local–global exploration compromise. Comparative tests across three 
obstacle scenarios reveal consistent convergence within ≤100 iterations and the lowest cost-time trade-off ratio, verified through Pareto 
analysis. Statistical distributions (Figure 12) show minimal variance in final fitness values, confirming steady convergence behavior. 
Overall superiority arises from three coupled features: 
1. Real-time adaptive fuzzy gain-scheduling minimizes steady-state error and chattering. 
2. Sliding-mode robustness ensures finite-time uncertainty compensation. 
3. LAHC global optimization yields paths that are simultaneously shortest, safest, and computationally cheapest. 
This paper presents a hybrid intelligent control and optimization framework that integrates an Adaptive Fuzzy Feedback Linearization 
Controller (AFFLC) with an outer Sliding Mode Controller (SMC) and a Late Acceptance Hill Climbing (LAHC) path-planning optimizer for 
unmanned aerial vehicles (UAVs). The proposed dual-loop control architecture—termed AFFLC–SMC—addresses two fundamental

## Page 21

20 
 
challenges in aerial control: (i) real-time robustness under dynamic payload disturbance, and (ii) chattering minimization while preserving 
adaptive nonlinear compensation. 
Unlike conventional fuzzy or observer-based controllers, the system employs a Lyapunov-consistent fuzzy adaptive law that symmetrically 
adjusts the inner-loop gains based on instantaneous tracking error and its rate, generating nonlinear inverse dynamics that suppress oscillations 
without requiring high-order differentiation or disturbance observers. Simultaneously, the LAHC-based global path planner ensures fast, 
computationally efficient optimization in 3-D obstacle environments, outperforming meta-heuristics such as HGWO-MSOS, SA, GWO, and 
SOS in convergence speed and execution time. 
The methodology provides a unified framework combining robust adaptive control and low-complexity meta-heuristic optimization, offering 
a computationally light alternative to deep learning–based motion planners. It is designed for embedded flight controllers where limited 
processing power restricts the use of high-dimensional optimization or heavy adaptation laws. 
(1) Design a composite controller guaranteeing trajectory-tracking stability under unknown payloads; 
(2) Derive Lyapunov-based adaptation ensuring bounded adaptive gain and global convergence; 
(3) Develop a LAHC-based planner minimizing path cost composed of length, energy, and threat exposure; 
(4) Validate performance over multiple scenarios including disturbance, payload, and complex multi-obstacle 3-D routes. 
Extensive simulations confirm that the proposed AFFLC–SMC yields: 
• 
43 % reduction in steady-state tracking error vs. AFLC and 65 % vs. classical FLC; 
• 
Elimination of rotor-speed chattering (average ripple ↓ 78 %); 
• 
Fast mass estimation convergence (< 1 s after payload change at t = 30 s); 
• 
Overshoot reduction ≈ 22 % and settling-time shortening ≈ 35 %; 
• 
In path-planning, LAHC converges to the global optimum within ≈ 90 iterations, lowering cost by > 18 % and execution 
time by > 70 % relative to competitors. 
 
 
 
• 
Author Contributions 
All authors reviewed and approved the final manuscript. 
• 
Funding  
The authors disclosed no financial support for the research, authorship, and/or publication of this article 
• 
Conflicts of Interest 
        The authors declare no conflicts of interest. 
• 
Data Availability Statement  
         The original contributions presented in the study are included in the article, further inquiries can be directed to the corresponding author. 
 
References  
[1]. Zhang, J. et al. (2025). UAV path planning method in dynamic environments: an ant colony algorithm-based optimization 
study. In Proc. Int. Conf. on Remote Sensing and Digital Earth (RSDE 2024), Vol. 13514, SPIE. 
[2]. Puente-Castro, A., et al. (2022). A 
review 
of 
artificial 
intelligence 
applied 
to 
path 
planning 
in 
UAV 
swarms. Neural Computing and Applications, 34(1), 153–170. 
[3]. Jiang, Y., et al. (2024). Evolutionary 
computation 
for 
unmanned 
aerial 
vehicle 
path 
planning: A survey. Artificial Intelligence Review, 57(10), 267. 
[4]. Xu, X., et al. (2024). A multi-objective evolutionary algorithm based on dimension exploration and discrepancy evolution for UAV 
path-planning problems. Information Sciences, 657, 119977. 
[5]. Han, G., et al. (2024). Deep Reinforcement Learning-Based Multi-UAV Collision Avoidance with Causal Representation 
Learning. Proc. 10th Int. Conf. on Big Data and Information Analytics (BigDIA 2024). IEEE. 
[6]. Agrawal, S., Patle, B. K., & Sanap, S. (2024). A systematic review on metaheuristic approaches for autonomous path planning of 
unmanned aerial vehicles. Drone Systems and Applications, 12, 1–28. 
[7]. Liu, J., et al. (2025). Unmanned aerial vehicle path planning in complex dynamic environments based on deep reinforcement 
learning. Machines, 13(2), 162. 
[8]. Quadt, T., et al. (2024). Dealing with multiple optimization objectives for UAV path planning in hostile environments: A literature 
review. Drones, 8(12), 769. 
[9]. Han, L., et al. (2025). Collaborative scheduling of time-dependent UAVs, vehicles and workers for crowdsensing in disaster 
response. arXiv preprint arXiv:2510.25212. 
[10]. Baskar, D., & Gorodetsky, A. (2020). A simulated wind-field dataset for testing energy-efficient path-planning algorithms for 
UAVs in urban environments. AIAA Aviation Forum 2020. 
[11]. Moore, C. A. (2024). Uncertainty-aware 
path 
planning 
on 
aerial 
imagery 
and 
unknown 
environments. M.Sc. Thesis, Mississippi State University. 
[12]. Tian, Y., et al. (2025). An optimized deep learning framework for energy-efficient resource allocation in UAV-assisted wireless 
networks. IEEE Access. 
[13]. Shah, S. A., Fernando, X., & Kashef, R. (2024). A survey 
on 
artificial-intelligence-based 
Internet 
of 
Vehicles 
utilizing 
UAVs. Drones, 8(8), 353. 
[14]. Altun, G., & Aydın, İ. (2025). Optimizing unmanned vehicle navigation: A hybrid PSO–GWO algorithm for efficient route 
planning. Firat University Journal of Experimental and Computational Engineering, 4(1), 100–114. 
[15]. Shen, L., et al. (2022). Energy-aware 
dynamic 
trajectory 
planning 
for 
UAV-enabled 
data 
collection 
in mMTC networks. IEEE Transactions on Green Communications and Networking, 6(4), 1957–1971. 
[16]. Zhao, H., et al. (2025). Dynamic path planning for space-time optimization cooperative tasks of multiple UAVs in uncertain 
environments. IEEE Transactions on Consumer Electronics. 
[17]. Jiang, W., et al. (2022). UAV path planning and collision avoidance in 3D environments based on POMPD and improved grey wolf 
optimizer. Aerospace Science and Technology, 121, 107314.

## Page 22

21 
 
[18]. Farid, G., et al. (2025). An 
improved 
Deep Q-learning 
approach 
for 
navigation 
of 
an 
autonomous 
UAV 
agent 
in 3D obstacle-cluttered environments. Drones, 9(8), 518. 
[19]. Khalaji, A. K., & Jalalnezhad, M. (2021). Robust forward/backward control of wheeled mobile robots. ISA Transactions, 115, 32–
45. 
[20]. Rattanaamporn, S., et al. (2025). Drone imaging and sensors for situational awareness in hazardous environments: A systematic 
review. Journal of Sensor and Actuator Networks, 14(5), 98. 
[21]. Keefer, E. (2023). Real-time graph-based path planning for autonomous racecars. M.Sc. Thesis, Auburn University. 
[22]. Deng, L., et al. (2023). Three-dimensional 
path 
planning 
of 
UAV 
based 
on 
improved 
particle 
swarm 
optimization. Mathematics, 11(9), 1987. 
[23]. Khalaji, A. K., & Jalalnezhad, M. (2021). Stabilization 
of 
a 
tractor 
with n trailers 
in 
the 
presence 
of 
wheel-slip 
effects. Robotica, 39(5), 787–797. 
[24]. Kurunathan, H., et al. (2023). Machine 
learning-aided 
operations 
and 
communications 
of 
unmanned 
aerial 
vehicles: A contemporary survey. IEEE Communications Surveys & Tutorials, 26(1), 496–533. 
[25]. Chai, R., et al. (2023). Time-oriented joint clustering and UAV trajectory planning in UAV-assisted WSNs: Leveraging parallel 
transmission and variable-velocity schemes. IEEE Transactions on Intelligent Transportation Systems, 24(11), 12092–12106. 
[26]. Cheng, Q., et al. (2024). Research on particle swarm optimization-based UAV path-planning technology in urban 
airspace. Drones, 8(12), 701. 
[27]. Zong, Z., et al. (2025). Risk-aware 
enabled 
path 
planning 
for 
drone 
flights 
in 
unknown 
environments. Journal of Intelligent & Robotic Systems, 111(2), 47. 
[28]. Couturier, A., & Akhloufi, M. A. (2024). A review on deep learning for UAV absolute visual localization. Drones, 8(11), 622. 
[29]. Hua, H., et al. (2025). Deep 
reinforcement 
learning-based 
hierarchical 
motion-planning 
strategy 
for 
multirotors. IEEE Transactions on Industrial Informatics. 
[30]. Rodrigues, P., et al. (2025). Quadrotor position control using fuzzy adaptive feedback linearization controller and sliding-mode 
controller. Journal of Vibration Engineering & Technologies, 13(5), 346. 
[31]. Jalalnezhad, M., & Fazeli, S. (2025). Sliding-mode 
control 
of AUV trajectory 
tracking 
in 
the 
presence 
of 
disturbance. Proc. Inst. Mech. Eng. Part E: Journal of Process Mechanical Engineering, 239(2), 950–965. 
[32]. Jalalnezhad, M., Keymasi-Khalaji, A., & Ghane, M. (2025). Adaptive backstepping control for underwater robots in complex 
environments. Proc. Inst. Mech. Eng. Part I: Journal of Systems and Control Engineering, 09596518241300663. 
[33]. Hsieh, H.-Y., et al. (2024). Urban mobile robot routing using fast-search random-tree method (RRT) in obstacle 
environments. Journal of the Brazilian Society of Mechanical Sciences and Engineering, 46(10), 612. 
[34]. Min Lin, X., et al. (2025). Designing the optimal path curve based on spline functions for mobile robots using bee-colony and 
genetic algorithms. Journal of Vibration and Control, 31(7–8), 1359–1376. 
[35]. Biju, S., Chammam, A., Askar, S., Rodrigues, P., & Jalalnezhad, M. (2025). Prediction-based controller radial-neural-network for 
traction control systems. Journal of Vibration and Control, 31, 1–15. 
[36]. Jalalnezhad, M. (2025). Design of intelligent control systems for damping vibrations of composite sheets using piezoelectricity 
under various disturbance conditions. Journal of the Brazilian Society of Mechanical Sciences and Engineering, 47, 1–24. 
[37]. Jalalnezhad, M. (2025). Quadrotor position control using fuzzy adaptive feedback linearization controller and sliding-mode 
controller. Journal of Vibration Engineering & Technologies, 13, 470–483. 
[38]. Jalalnezhad, M., Kareem, A. K., Chammam, A., & Al Attabi, K. (2025). Intelligent vibration control of composite and FGM plates 
using 
piezoelectric 
actuators 
and 
optimized 
sliding-mode-based 
controllers. Journal of Vibration Engineering & Technologies, 13(7), 474–489. 
[39]. Wang, Z., Spanogianopoulos, S., Prasad, K. D. V., Trivedi, T., & Chethan, M. (2025). Optimal mobile robot routing with neural 
network 
and 
kernel-based 
dimensionality 
reduction 
in 
unknown 
environments. Journal of the Brazilian Society of Mechanical Sciences and Engineering, 47, 1–22. 
[40]. Jones, M., Djahel, S., & Welsh, K. (2023). Path-planning 
for 
unmanned 
aerial 
vehicles 
with 
environment-complexity 
considerations: A survey. ACM Computing Surveys, 55(11), 1–39. 
[41]. Zhang, M., et al. (2023). Deployment 
of 
energy-efficient 
aerial 
communication 
platforms 
with 
low-complexity 
detection. IEEE Transactions on Vehicular Technology, 72(9), 12016–12030. 
[42]. AbuJabal, N., et al. (2024). A comprehensive study of recent path-planning techniques in dynamic environments for autonomous 
robots. Sensors, 24(24), 8089. 
[43]. Biswas, S., Anavatti, S. G., & Garratt, M. A. (2021). Path planning and task assignment for multiple UAVs in dynamic 
environments. In Unmanned Aerial Systems (pp. 81–102). Academic Press. 
[44]. Zammit, C., & van Kampen, E. J. (2023). Real-time 3D UAV path 
planning 
in 
dynamic 
environments 
with 
uncertainty. Unmanned Systems, 11(3), 203–219. 
[45]. Jalalnezhad, M., et al. (2025). Low-complexity 
optimization 
method 
for 
energy-efficient 
UAV 
navigation. (Submitted manuscript details included). 
[46]. Jalalnezhad, M., et al. (2025). Efficient 
approach 
toward 
path 
planning 
for 
UAVs 
based 
on 
the 
Late Acceptance Hill Climbing algorithm. Kharazmi University Technical Report, Tehran. 
[47]. Zhang, M., et al. (2023). Deployment 
of 
energy-efficient 
aerial 
communication 
platforms 
with 
low-complexity 
detection. IEEE Transactions on Vehicular Technology, 72(9), 12016–12030. 
[48]. AbuJabal, N., et al. (2024). A comprehensive study of recent path-planning techniques in dynamic environments for autonomous 
robots. Sensors, 24(24), 8089. 
[49]. Biswas, S., Anavatti, S. G., & Garratt, M. A. (2021). Path planning and task assignment for multiple UAVs in dynamic 
environments. In Unmanned Aerial Systems (pp. 81–102). Academic Press. 
[50]. Zammit, C., & van Kampen, E. J. (2023). Real-time 
3D 
UAV 
path 
planning 
in 
dynamic 
environments 
with 
uncertainty. Unmanned Systems, 11(3), 203–219. 
[51]. Jalalnezhad, M. (2025a). Quadrotor position control using fuzzy adaptive feedback linearization controller and sliding mode 
controller. Journal of Vibration Engineering & Technologies, 13, 470–483.

## Page 23

22 
 
[52]. Jalalnezhad, M., Kareem, A. K., Chammam, A., & Al Attabi, K. (2025b). Intelligent vibration control of composite and FGM plates 
using 
piezoelectric 
actuators 
and 
optimized 
sliding-mode-based 
controllers. Journal of Vibration Engineering & Technologies, 13(7), 474–489. 
[53]. Jalalnezhad, M., Keymasi-Khalaji, A., & Ghane, M. (2025). Adaptive backstepping control for underwater robots in complex 
environments. Proceedings of the Institution of Mechanical Engineers, Part I: Journal of Systems and Control Engineering, 095965
18241300663. 
[54]. Rodrigues, P., et al. (2025). Quadrotor position control using fuzzy adaptive feedback linearization controller and sliding mode 
controller. Journal of Vibration Engineering & Technologies, 13(5), 346. 
[55]. Wang, Z., Spanogianopoulos, S., Prasad, K. D. V., Trivedi, T., & Chethan, M. (2025). Optimal mobile robot routing with neural 
network 
and 
kernel-based 
dimensionality 
reduction 
in 
unknown 
environments. 
 Journal of the Brazilian Society of Mechanical Sciences and Engineering, 47, 1–22. 
[56]. Jones, M., Djahel, S., & Welsh, K. (2023). Path-planning for unmanned aerial vehicles with environment complexity 
considerations: A survey. ACM Computing Surveys, 55(11), 1–39. 
[57]. E.-H. Zheng, J.-J. Xiong, and J.-L. Luo, "Second order sliding mode control for a quadrotor UAV," ISA transactions, vol. 53, no. 
4, pp. 1350-1356, 2014.
