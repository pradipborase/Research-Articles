# Enhanced_Quadrotor_Drone_Control_Integration_of_Backstepping_Method_with_Butterfly_Optimization_Algorithm.pdf

## Page 1

Enhanced Quadrotor Drone Control: Integration of
Backstepping Method with Butterfly Optimization
Algorithm
Najlae Jennan
Laboratory of Engineering, Systems and Applications
Sidi Mohamed Ben Abdellah University
Fez, Morocco
najlae.jennan@usmba.ac.ma
Wiam Darkaoui
Laboratory of Engineering, Systems and Applications
Sidi Mohamed Ben Abdellah University
Fez, Morocco
wiam.darkaoui@usmba.ac.ma
El Mehdi Mellouli
Laboratory of Engineering, Systems and Applications
Sidi Mohamed Ben Abdellah University
Fez, Morocco
mellouli elmehdi@hotmail.com
El Hanafi Arjdal
Laboratory of Materials, Signals, Systems and Physical Modeling
Faculty of Sciences, Ibn Zohr University
Agadir, Morocco
e.arjdal@uiz.ac.ma
Abstract—This paper presents a robust approach for control-
ling a quadrotor drone, using the backstepping control method
combined with the Butterfly Optimization Algorithm (BOA) to
optimize its parameters, thereby improving its stability, and
maneuverability. Barrier Lyapunov Functions are employed to
provide a rigorous stability analysis and guarantee safe operation
within defined constraints. The study begins with the identifica-
tion of the mathematical model that governs the dynamics of the
system. Subsequently, a backstepping controller is employed to
control the drone’s behavior. To further enhance the controller’s
performance, the BOA technique is employed to optimize the
parameters associated with the controller. To estimate the hidden
states of the quadrotor system, a trianguler observer is used. In
addition, Barrier Lyapunov is employed to verify the efficiency
of the suggested approach in maintaining safety and stability.
The simulation results demonstrate the efficacy of the suggested
strategy in comparison with traditional control techniques.
Index Terms—Backstepping control, barrier Lyapunov, butter-
fly optimization algorithm, drone quadrotor, triangular observer.
I. INTRODUCTION
The quadrotor drone has become a significant and versatile
technology, with applications in diverse fields including aerial
surveillance, search and rescue missions, and agriculture [1],
[2]. The key advantages of this technology are its agility,
and ability to maneuver in complex environments [3]–[5].
Although quadrotor drones offer a multitude of advantages,
they present significant control challenges due to their inherent
nonlinear and multi-input multi-output (MIMO) dynamics.
These systems are highly susceptible to external disturbances,
and are particularly liable to instability in the absence of
careful control [6], [7], [9], [10]. It is therefore imperative that
robust and precise control strategies are employed to guarantee
the stability, safety and performance of quadrotors in real-
world applications [11], [12], [15].
The existing literature proposes a number of control method-
ologies with the objective of enhancing the stability and per-
formance of quadrotor systems. The application of traditional
control techniques, such as proportional-integral-derivative
(PID) control, offering a degree of simplicity and ease of
implementation. However, these methods frequently prove
inadequate when confronted with the highly nonlinear and
dynamic characteristics of quadrotors [16]. To overcome these
limitations, more advanced strategies such as Sliding Mode
Control (SMC) [8], [17]–[19] and fuzzy logic technique [20]–
[23] have gained importance in the field of control theory
due to their ability to handle nonlinearities and uncertainties
more effectively. In particular, backstepping control has gained
considerable attention for quadrotor systems, this approach
involves dividing the system dynamics into manageable sub-
systems, thereby ensuring stability at each stage [24], [25].
The combination of backstepping with the Lyapunov approach
has traditionally been employed to guarantee system stability
and convergence to the desired trajectory [26], [27]. However,
recent developments have introduced alternative methodolo-
gies, such as the deployment of barrier Lyapunov functions,
which impose constraints on the system states to ensure they
remain within predefined limits [28], [29]. Furthermore, it is
notable that optimization algorithms have been extensively
applied in order to dynamically adjust controller parameters
in response to varying conditions and uncertainties. Among
these, the Particle Swarm Optimization (PSO) approach and
the Butterfly Optimization Algorithm (BOA), have demon-
strated considerable potential for enhancing the efficiency and
979-8-3315-3297-0/25/$31.00 ©2025 IEEE
2025 5th International Conference on Innovative Research in Applied Science, Engineering and Technology (IRASET) | 979-8-3315-3297-0/25/$31.00 ©2025 IEEE | DOI: 10.1109/IRASET64571.2025.11008299
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:37:11 UTC from IEEE Xplore.  Restrictions apply.

## Page 2

responsiveness of control systems [30], [31].
This paper advances the field of quadrotor drone control by
integrating Barrier Lyapunov functions into the backstepping
control system, ensuring rigorous stability and safety within
predefined constraints [24]. The study employs the BOA
to optimize the parameters of the backstepping controller,
thereby considerably improving the drone’s performance in
terms of stability, robustness, and maneuverability [31]. It is
acknowledged that not all states can be directly measured;
thus, a triangular observer is introduced to the control system
in order to estimate the hidden states [32]. The results of
simulations demonstrate that the proposed approach outper-
forms traditional control methods, offering superior control
performance and adaptability [33], [34].
The structure of this paper is as follows: The quadrotor drone’s
mathematical model is presented in Section 2. The design of
the proposed control system is the primary focus of Section
3. The suggested triangular observer is described in section 4.
The simulation results are shown in Section 5. A conclusion
summarizing the results and suggesting future directions is
provided in Section 6.
II. THE MATHEMATICAL MODEL OF THE DRONE
QUADROTOR
A particular focus is placed on adequately modeling the
multi-input multi-output (MIMO) nonlinear dynamics of the
quadrotor drone when developing its mathematical model. The
motion of the drone is described in terms of its translational
and rotational movements in three-dimensional space, which
are governed by Newton-Euler equations [35], [36]. These
equations of motion are divided into two principal compo-
nents: the first concerns translational dynamics, which control
the position of the drone in space, and the second pertains
to rotational dynamics, which determine the orientation (roll,
pitch, and yaw) of the drone [37], [38]. The model incorpo-
rates the effects of gravity, thrust from the four rotors, and
gyroscopic forces that arise from the angular motion of the
rotors [33].
Fig. 1: Model of the quadrotor drone
The mathematical representation of the quadrotor system is
expressed using Newton-Euler formalism as a set of non-linear
differential equations that describe both the translational and
rotational dynamics by a state vector w = [x y z ϕ θ ψ], in
the following form:
¨wi = hi(w, t)+li(w, t)×ui(w, t)+di(t)
; i = [1, 6] (1)
Where u represents the vector of control inputs and d is the
vector of external disturbances.
h and l are two vectors that represent the dynamics of the
system, where their expressions are defined in table I.
The mass of the quadrotor is indicated by m, the mo-
TABLE I: Expressions of the dynamics of the system
Coefficient
Expression
h1
h1 = −
kftx
m
˙x
h2
h2 = −
kfty
m
˙y
h3
h3 = −g −
kftz
m
˙z
h4
h4 = (Iy−Iz)
Ix
˙θ ˙ψ −JrΩ
Ix ˙θ −
kfax
Ix
˙ϕ2
h5
h5 = (Iz−Ix)
Iy
˙ϕ ˙ψ −JrΩ
Iy
˙ϕ −
kfay
Iy
˙θ2
h6
h6 = (Ix−Iy)
Iz
˙θ ˙ϕ −
kfaz
Iz
˙ψ2
l1
l1 = 1/m
l2
l2 = 1/m
l3
l3 = cos θ cos ϕ
m
l4
l4 = 1/Ix
l5
l5 = 1/Iy
l6
l6 = 1/Iz
ments of inertia are represented by (Ix, Iy, Iz). The terms
(kftx, kftx, kftz) correspond to the translational drag coef-
ficients, and (kfax, kfay, kfaz) represent the aerodynamic
friction coefficients that influence the rotational dynamics.
III. PROPOSED CONTROL STRATEGY
This section will introduce the proposed control strategy for
the quadrotor drone, whereby a combination of backstepping
control and barrier Lyapunov stability will be emphasized.
This control design incorporates the BOA approach to opti-
mize the parameters of the controller [24], [28], [31]. The
triangular observer is used to approximate the hidden states
within the system [32].
A. Backstepping controller based on barrier Lyapunov
This part introduces the backstepping control method as
the primary control strategy for the quadrotor drone. The
backstepping method is implemented by defining a series of
virtual control inputs for each state variable and gradually
designing control laws that guarantee system stability at each
stage of the process [24], [26].
In this study, the backstepping method is integrated with
Barrier Lyapunov Functions (BLFs) to guarantee that the sys-
tem’s states remain within the predefined stability boundaries,
enablingan accurate control performance, even in the presence
of external disturbances and system uncertainties [28], [29].
Defining wd as the vector of desired trajectories, we calculate
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:37:11 UTC from IEEE Xplore.  Restrictions apply.

## Page 3

Fig. 2: Diagram of control law developement
the tracking errors as well as their derivatives in the following
manner: (
e1i = wi −wdi
˙e1i = ˙wi −˙wdi
; i = [1, 6]
(2)
Subsequently, in order to analyse the system stability and to
derive the virtual control laws, the barrier Lyapunov functions
and their derivatives are defined in the following form :









V1i = 1
2 × log
k2
ai
k2ai −e2
1i
≥0
˙V1i = e1i × ˙e1i
k2ai −e2
1i
< 0
; i = [1, 6]
(3)
Where kai, i = [1, 6] is a positive coefficient. We assume that
the virtual control laws can be written as follows :
˙wi = fi(wi) = ˙wdi −ˆα1i ×e1i
; i = [1, 6] (4)
Where ˆα1i is the optimal value of α1i, i = [1, 6] using BOA
approach.
Then, according to (3) and (4), we obtain :
˙V1i ≤−ˆα1i × V1i < 0
; i = [1, 6]
(5)
The second step consists on defining new errors and their
derivatives, determined in the following form :
(
e2i = ˙wi −fi(wi)
˙e2i = ¨wi −˙fi(wi)
; i = [1, 6]
(6)
Subsequently, an additional Lyapunov function is defined in
order to evaluate the overall stability of the system and then
to derive the control laws for each state.









V2i = 1
2 × log
k2
ai
k2ai −e2
1i
+ 1
2 × log
k2
bi
k2
bi −e2
2i
≥0
˙V2i = e1i × ˙e1i
k2ai −e2
1i
+ e2i × ˙e2i
k2
bi −e2
2i
< 0
; i = [1, 6]
(7)
From (7), the following inequality is obtained :
˙V2i ≤−ˆα1i × V1i −ˆα2i × V2i < 0
; i = [1, 6]
(8)
Where ˆα1i and ˆα2i are the optimal values of α1i and α2i
respectively, i = [1, 6] using BOA approach. The control laws
can subsequently be formulated in the following manner:
ui(w, t) =l−1
i
(w, t) × [ ˙fi(wi) −hi(w, t) −ˆα1i × e1i
−ˆα2i × e2i]
; i = [1, 6]
(9)
Figure 2 illustrates the overall structure of control law deriva-
tion, summarizing the key equations and their interactions in
the controller design.
B. Butterfly Optimization Algorithm
This part introduces the BOA as the optimization technique
used to fine-tune the coefficients α1i and α2i of the backstep-
ping controller. It is particularly effective in handling complex
optimization problems due to its capacity to explore a vast
search space and to maintain a balance between the exploration
and exploitation phases [31].
The algorithm, based on two principal phases: global search
and local search, represents the butterflies as individuals within
a population, with their position in the search space corre-
sponding to a potential solution to the optimization problem
[31].
In this study, the BOA approach is employed to optimize two
critical parameters in the backstepping control design: α1i
and α2i, as they influence the stability and response speed
of the system, and therefore affect the efficacy of the control
performance. The use of BOA enables an efficient search for
the optimal values ˆα1i and ˆα2i, which minimize the tracking
errors and enhance the overall stability of the quadrotor drone.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:37:11 UTC from IEEE Xplore.  Restrictions apply.

## Page 4

(a) The response of the control law u1 achieved
(b) The response of the control law u2 achieved
(c) The response of the control law u3 achieved
(d) The response of the control law u4 achieved
(e) The response of the control law u5 achieved
(f) The response of the control law u6 achieved
Fig. 3: The evolutions of the control laws achieved using the proposed controller
IV. DESIGN OF THE TRIANGULAR OBSERVER
The triangular observer, intended to estimate the hidden
states of the quadrotor drone system, is presented in this
section. This observer operates on the basis of the state
feedback principle, whereby the known states of the system
are employed to estimate the unknown states in a recursive
manner [32], [39].
In this work, the triangular observer is employed to estimate
the states that are critical for the accurate functioning of the
control strategy, such as velocities. These estimated states
are employed in the control loop to improve the overall
performance of the controller [39].
Considering ˙ˆw as the vector of the approximated states using
the triangular observer, the observer errors are then defined in
the following form :
eoi = wi −ˆwi
; i = [1, 6]
(10)
The approximated states ˙ˆw can be written as follows :





˙ˆwi = ¨ˆwi + λ1i × sign(wi −ˆwi)
¨ˆwi = ˆhi( ˆw, t) + ˆli( ˆw, t) × ui( ˆw, t) + λ2i × sign( ˙˜wi −˙ˆwi)
; i = [1, 6]
(11)
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:37:11 UTC from IEEE Xplore.  Restrictions apply.

## Page 5

Where λ1 and λ2 are two vectors of positive coefficients, and
˜w represents the estimation vector, with :
˙˜wi = ˙ˆwi + λ1i × sign(wi −ˆwi)
; i = [1, 6]
(12)
V. SIMULATION RESULTS
This section presents a comparative analysis of the proposed
control strategy, alongside two other methods: The first is
the backstepping method using barrier Lyapunov without the
BOA, the second method involves the traditional backstepping
control based on the standard Lyapunov approach. The objec-
tive of the comparison is to evaluate the three methods in terms
of their tracking accuracy, ability to reject disturbances, and
overall system stability. Moreover, the analysis will focus on
the states observed by the triangular observer, demonstrating
the effectiveness of this approach in estimating the system’s
hidden states.
The first set of figures 3 illustrates the evolution of the control
inputs u1 to u6 generated by the proposed controller. Each
subfigure corresponds to one of the six control signals applied
to control the system states: Specifically, u1, u2 and u3 control
the translational motion in the x, y and z axes, respectively,
while u4, u5 and u6 govern the rotational motion around the
roll (ϕ), pitch (θ), and yaw (ψ) angles. These figures illustrate
how the proposed controller dynamically adjusts the control
inputs over time to ensure precise tracking of the desired state
trajectories while maintaining system stability.
Figure 3 illustrates the efficacy of the proposed controller in
minimizing control effort while guaranteeing system stability
and precision across all six states.
Figure 4 illustrates the evolution of the system states - includ-
ing the three translational positions (x, y, z) and the three
rotational angles (ϕ, θ, ψ). Each subfigure presents both the
desired trajectory and the actual trajectory achieved. The com-
parison highlights the tracking performance of the proposed
control strategy, compared to the backstepping controller with-
out BOA and the traditional Lyapunov-based backstepping
approach.
The figures of trajectories 4 demonstrate the superior perfor-
mance of the proposed controller using BOA approach, where
it achieves the fastest response and convergence to the desired
trajectories, followed by the method without BOA, which
shows a slightly slower response. The traditional Lyapunov-
based backstepping approach has the slowest convergence
time, underscoring the effectiveness of the proposed strategy
in improving system responsiveness.
Figure 5 presents the estimated states and observer errors for
the six states of the quadrotor system: the three translational
velocities ( ˙x, ˙y, ˙z) and the three angular velocities ( ˙ϕ, ˙θ,
˙ψ). Each subfigure illustrates three curves: the hidden state,
the estimated state obtained by the triangular observer and
the corresponding observer error ˙eoi, which represents the
difference between the actual and estimated values.
The efficacy of the triangular observer is clearly demonstrated
by its capacity to accurately estimate the hidden states of the
quadrotor system. The observer exhibits robust performance
by minimizing estimation errors.
VI. CONCLUSION
This paper proposes a control strategy combining backstep-
ping control with barrier Lyapunov stability for the purpose
of controlling a quadrotor drone. The objective of this method
was to ensure precise trajectory tracking while enhancing the
system’s robustness against external disturbances and miti-
gating uncertainties. The Butterfly Optimization Algorithm
(BOA) was employed in order to optimize the controller’s
key parameters of the backstepping controller. Furthermore, a
triangular observer was introduced to approximate the hidden
states of the system. The simulation results demonstrated the
efficacy of the proposed control strategy, exhibiting consider-
able enhancements in trajectory tracking precision and robust
behavior in the presence of external disturbances. Neverthe-
less, although the results are promising, there are still some
limitations to this work as the computational complexity of
the BOA approach, particularly in real-time applications, may
present a challenge for computing systems.
Further research could be directed towards the refinement of
the optimization methodology in order to reduce the compu-
tational requirements, and the application of the method to
experimental systems for real-world validation.
REFERENCES
[1] T. Huynh-The, Q.V. Pham, T.V. Nguyen, D.B.D. Costa and D.S. Kim,
”RF-UAVNet: High-Performance Convolutional Network for RF-Based
Drone Surveillance Systems” IEEE Access, vol. 10, pp. 49696-49707,
2022.
[2] M. Zhang, C. Xu, S. Li and C. Jiang, ”On the Security of an ECC-Based
Authentication Scheme for Internet of Drones” IEEE Systems Journal,
vol. 16, no. 4, pp. 6425-6428, 2022.
[3] A.V. Savkin and H. Huang, ”Navigation of a Network of Aerial Drones
for Monitoring a Frontier of a Moving Environmental Disaster Area”
IEEE Systems Journal, vol. 14, no. 4, pp. 4746-4749, 2020.
[4] C. Xu, X. Liao, J. Tan, H. Ye and H. Lu, ”Recent Research Progress of
Unmanned Aerial Vehicle Regulation Policies and Technologies in Urban
Low Altitude”IEEE Access, vol. 8, pp. 74175-74194, 2020.
[5] V.Hassija, et al. ”Fast, Reliable, and Secure Drone Communication: A
Comprehensive Survey” IEEE Communications Surveys & Tutorials, vol.
23, no. 4, pp. 2802-2832, 2021.
[6] M. Adil, M.A. Jan, Y. Liu, H. Abulkasim, A. Farouk and H. Song,
”A Systematic Survey: Security Threats to UAV-Aided IoT Applications,
Taxonomy, Current Challenges and Requirements With Future Research
Directions” IEEE Transactions on Intelligent Transportation Systems, vol.
24, no. 2, pp. 1437-1455, 2023.
[7] N.B.V. Le, H.D. Thai, C.W. Yoon, and J.H.Huh, ”Recent Development
of Drone Technology Software Engineering: A Systematic Survey” IEEE
Access, vol. 12, pp. 128729-128751, 2024.
[8] L. El Hajjami, E.M. Mellouli, V. ˇZuraulis and M. Berrada, ”A novel
robust adaptive neuro-sliding mode steering controller for autonomous
ground vehicles” Robot. and Auton. Syst., vol. 170, pp. 104557, 2023.
[9] E.A. Debas, A. Albuali and M.M.H. Rahman, ”Forensic Examination
of Drones: A Comprehensive Study of Frameworks, Challenges, and
Machine Learning Applications” IEEE Access, vol. 12, pp. 111505-
111522, 2024.
[10] L. El Hajjami, E.M. Mellouli, V. ˇZuraulis, M. Berrada and I. Boumhidi,
”A Robust Intelligent Controller for Autonomous Ground Vehicle Lon-
gitudinal Dynamics” Applied Sc., vol. 13, no. 1, 2023.
[11] X. Li, L. Shuang and Z. Ju, ”Robust controller design for trajectory
tracking of autonomous vehicle” International Journal of Vehicle Perfor-
mance, vol. 6, no. 4, pp. 381-398, 2020.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:37:11 UTC from IEEE Xplore.  Restrictions apply.

## Page 6

(a) The response of the position x achieved
(b) The response of the position y achieved
(c) The response of the altitude z achieved
(d) The response of the roll angle ϕ achieved
(e) The response of the pitch angle θ achieved
(f) The response of the yaw angle ψ achieved
Fig. 4: The evolutions of the trajectories achieved and the desired trajectories using the three methods
[12] E.M. Mellouli, S. Massou and I. Boumhidi, ”Optimal robust adaptive
fuzzy H inf tracking control without reaching phase for nonlinear system”
J. Control Sc. Eng., no. 1, 2013.
[13] A. Mohamed, J. Ren, A.M. Sharaf and M. EI-Gindy, ”Optimal path
planning for unmanned ground vehicles using potential field method and
optimal control method” International Journal of Vehicle Performance,
vol. 4, no. 1, pp. 1-14, 2017.
[14] A. Mohamed, M. El-Gindy and J. Ren, ”Advanced control techniques
for unmanned ground vehicle: literature survey” International Journal of
Vehicle Performance, vol. 4, no. 1, pp. 46-73, 2017.
[15] R. Naoual, E.M. Mellouli and I. Boumhidi, ”Adaptive fuzzy sliding
mode control for the two-link robot” in 9th International Conference on
Intelligent Systems: Theories and Applications, SITA 2014, pp. 1-6, 2014.
[16] O.J. Wan, S.J. Won, G.Y. Hee, H.S. Jae and L.S. Dae, ”Drone Hovering
using PID Control” The Journal of the Korea institute of electronic
communication sciences, vol. 13, no. 6, pp. 1269-1274, 2018.
[17] A. Mughees and I. Ahmad, ”Multi-Optimization of Novel Conditioned
Adaptive Barrier Function Integral Terminal SMC for Trajectory Tracking
of a Quadcopter System” IEEE Access, vol. 11, pp. 88359-88377, 2023.
[18] A. Moussa and E.M. Mellouli, ”A new adaptive second-order non-
singular terminal sliding mode lateral control combined with neural
networks for autonomous vehicle” International Journal of Vehicle Per-
formance, vol. 10, no. 1, pp. 50-72, 2023.
[19] L. El Hajjami, E.M. Mellouli, V. ˇZuraulis, M. Berrada and I. Boumhidi,
”Neural network optimization algorithm based non-singular fast termi-
nal sliding-mode control for an uncertain autonomous ground vehicle
subjected to disturbances” Proceedings of the Institution of Mechanical
Engineers, Part D: Journal of Automobile Engineering, vol. 238, no. 7,
pp. 1687–1697, 2024.
[20] N. Jennan and E.M. Mellouli, ”Direct optimal fuzzy logic adapted to
sliding mode for lateral autonomous vehicle control” International Journal
of Vehicle Performance, vol. 10, no. 3, pp. 349 - 372, 2024.
[21] E. Lee, C. Choi and P. Kim, ”Intelligent Handover Scheme for Drone
Using Fuzzy Inference Systems” IEEE Access, vol. 5, pp. 13712-13719,
2017.
[22] R. Alika, E.M. Mellouli and E.H. Tissir, ”A modified sliding mode
controller based on fuzzy logic to control the longitudinal dynamics of
the autonomous vehicle” Res. Eng., vol. 22, 2024.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:37:11 UTC from IEEE Xplore.  Restrictions apply.

## Page 7

(a) The response of the observed state ˙ˆx and the observer
error ˙eo1 achieved
(b) The response of the observed state ˙ˆy and the observer
error ˙eo2 achieved
(c) The response of the observed state ˙ˆz and the observer
error ˙eo3 achieved
(d) The response of the observed state ˙ˆϕ and the observer
error ˙eo4 achieved
(e) The response of the observed state ˙ˆθ and the observer
error ˙eo5 achieved
(f) The response of the observed state ˙ˆψ and the observer
error ˙eo6 achieved
Fig. 5: The evolutions of the hidden states, the estimated states and the observer errors using the triangular observer
[23] R. Alika, E.M. Mellouli and E.H. Tissir, ”Adaptive Higher-Order
Sliding Mode Control Based Fuzzy Logic T-S for Lateral Dynamics of
Autonomous Vehicles” in 12th International Conference on Information
and Communication Systems, ICICS 2021, pp. 358–363, 2021.
[24] A. Belmouhoub, S. Medjmadj, Y. Bouzid, S.H. Derrouaoui and M.
Guiatni, ”Enhanced backstepping control for an unconventional quadrotor
under external disturbances” The Aeronautical Journal, vol. 127, no. 1310,
pp. 627-650, 2023.
[25] A.K. Bhatia, J. Jiang, Z. Zhen, N. Ahmed and A. Rohra, ”Projection
Modification Based Robust Adaptive Backstepping Control for Multipur-
pose Quadcopter UAV” IEEE Access, vol. 7, pp. 154121-154130, 2019.
[26] Z. Wang, X. Liu, K. Liu, S. Li and H. Wang, ”Backstepping-Based Lya-
punov Function Construction Using Approximate Dynamic Programming
and Sum of Square Techniques” IEEE Transactions on Cybernetics, vol.
47, no. 10, pp. 3393-3403, 2017.
[27] F. Wang, Q. Zou and Q. Zong, ”Robust adaptive backstepping control for
an uncertain nonlinear system with input constraint based on Lyapunov
redesign” International Journal of Control, Automation and Systems, Vol.
15, pp. 212–225, 2017.
[28] H. Liu, B. Meng and X. Tian, ”Finite-Time Prescribed Performance
Trajectory Tracking Control for Underactuated Autonomous Underwater
Vehicles Based on a Tan-Type Barrier Lyapunov Function” IEEE Access,
vol. 10, pp. 53664-53675, 2022.
[29] C.D.C. Ancona, M.A. Estrada and L. Fridman, ”Barrier Function-Based
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:37:11 UTC from IEEE Xplore.  Restrictions apply.

## Page 8

Adaptive Lyapunov Redesign for Systems Without A Priori Bounded
Perturbations” IEEE Transactions on Automatic Control, vol. 67, no. 8,
pp. 3851-3862, 2022.
[30] L. Sheng, H. Li, Y. Qi, and M. Shi, ”Real Time Screening and Trajectory
Optimization of UAVs in Cluster Based on Improved Particle Swarm
Optimization Algorithm” IEEE Access, vol. 11, pp. 81838-81851, 2023.
[31] H. Mazaheri and S. Goli, ”UAV path planning based on butterfly op-
timization algorithm in three-dimensional space” Aerospace Knowledge
and Technology Journal, vol. 10, no. 2, pp. 189-210, 2021.
[32] M.A.R. Serrano, J.S. Salinas and E.A. Bricaire, ”Observer-Based Time-
Varying Backstepping Control for a Quadrotor Multi-Agent System”
Journal of Intelligent & Robotic Systems, vol. 93, pp. 135–150, 2019.
[33] N. Jennan and E.M. Mellouli, ”Robust control for a drone quadrotor
using fuzzy logic-based fast terminal sliding mode control” Journal of
the Brazilian Society of Mechanical Sciences and Engineering, vol. 46,
no. 7, pp. 349-372, 2024.
[34] N. Jennan, E.M. Mellouli and I. Boumhidi, ”Fixed-Time Sliding Mode
Control for a Drone Quadrotor” Lecture Notes in Networks and Systems,
pp. 539–545, 2024.
[35] S. Musa, ”Techniques for Quadcopter modeling and Design: A Review”
The Journal of Unmanned System Technology, vol. 5, no. 3, 2017.
[36] B.B.V.L. Deepak and P. Singh, ”A survey on design and development
of an unmanned aerial vehicle (quadcopter)” International Journal of
Intelligent Unmanned Systems, vol. 4, no. 2, 2016.
[37] F. Jiang, F. Pourpanah and Q. Hao, ”Design, Implementation, and
Evaluation of a Neural-Network-Based Quadcopter UAV System” IEEE
Transactions on Industrial Electronics, vol. 67, no. 3, pp. 2076-2085,
2020.
[38] N. Jennan and E.M. Mellouli, ”New optimal fast terminal sliding mode
control combined with neural networks for modelling and controlling a
drone quadrotor” International Journal of Automation and Control, vol.
17, no. 6, pp. 595–612, 2023.
[39] S.K. Kim and C.K. Ahn, ”Angular Velocity Observer-Based Quadcopter
Attitude Stabilization via Pole-Zero Cancellation Technique” IEEE Trans-
actions on Circuits and Systems II: Express Briefs, vol. 68, no. 7, pp.
2458-2462, 2021.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:37:11 UTC from IEEE Xplore.  Restrictions apply.
