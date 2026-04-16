# Physics-Informed Machine Learning for UAV Control.pdf

## Page 1

Physics-Informed Machine Learning
for UAV Control
Carlos Alexander Osorio Quero
Computer Science Department.
Instituto Nacional de Astrof´ısica,
´Optica y Electr´onica (INAOE)
Puebla, Mexico
caoq@inaoep.mx
Jose Martinez-Carranza
Computer Science Department.
Instituto Nacional de Astrof´ısica
´Optica y Electr´onica (INAOE)
Puebla, Mexico
carranza@inaoep.mx
Abstract—The integration of Dynamic Mode Decomposition
(DMD) control with Physics-Informed Neural Networks (PINNs)
offers a novel approach to enhancing UAV quadcopter control
systems. This method leverages DMD techniques and PINNs to
solve the Riccati equation, which is essential for precise UAV
position estimation. By framing the UAV control problem within
physics-based constraints, the approach ensures that the learned
models adhere to the physical laws governing UAV dynamics.
Utilizing a comprehensive dataset—including UAV flight pa-
rameters such as position, velocity, and control inputs—DMD
extracts fundamental dynamic modes from the data, providing
a reduced-order representation that captures the dominant UAV
dynamics. This reduced representation is then incorporated into
the PINN framework to accurately solve the Riccati equation.
The combination of DMD and PINNs results in a robust control
strategy that significantly improves position estimation accuracy
and optimizes control performance. Real-time validation of this
method was conducted in a Unity-based physics simulation
environment, incorporating factors like gravity and perturbation
noise. The results demonstrate substantial improvements in
estimation accuracy and control stability compared to traditional
methods.
Index Terms—Dynamic Mode Decomposition (DMD), Physics-
Informed Neural Networks (PINNs), Unmanned Autonomous
Vehicle (UAV), Riccati equation, Deep Learning, drone trajectory.
I. INTRODUCTION
Unmanned Aerial Vehicles (UAVs) are increasingly vital
in diverse applications such as surveillance [1], mapping [2],
warehouse inspection [3], delivery services [4], and environ-
mental monitoring [5]. Achieving precise control and accu-
rate position estimation is crucial for effectively deploying
UAVs, particularly in highly complex and rapidly evolving
environments. State-of-the-art control strategies have been
developed to address these challenges, including Proportional-
Integral-Derivative (PID) control [6], Model Predictive Control
(MPC) [7], Deep Learning control [8], [9], genetic algo-
rithms [10] and Linear Quadratic Regulators (LQR) [11].
While these methods have shown success in specific scenarios,
they often struggle with real-time adaptability and robustness
in the presence of perturbations and noise.
Dynamic Mode Decomposition (DMD) [12] has emerged as
a powerful technique for capturing the essential dynamics of
complex systems through data-driven approaches. However,
DMD alone is insufficient to provide sufficient robustness
in highly dynamic and noisy environments, as it primarily
focuses on identifying dominant modes without explicitly
incorporating the underlying physical laws. This limitation can
lead to reduced UAV position estimation and control accuracy,
particularly in environmental perturbations such as wind or
other noise conditions. To overcome these limitations, this
paper introduces a novel approach that integrates DMD control
with Physics-Informed Neural Networks (PINNs) to enhance
UAV control systems [13]. The proposed method leverages
DMD techniques to extract critical dynamic modes from a
comprehensive dataset that includes UAV flight information
such as position, velocity, and control inputs. These modes
provide a reduced-order representation that captures the dom-
inant UAV dynamics. This representation is then used within
the PINN framework to solve the Riccati equation [14], [15]
with high accuracy, ensuring that the learned models conform
to the physical laws governing UAV dynamics [16].
Combining DMD and PINNs creates a robust control strat-
egy that provides accurate position estimations and enhances
control performance. This approach is efficient in environ-
ments with perturbations and noise, ensuring reliable UAV
operation under challenging conditions [17]. Experimental re-
sults validate the efficacy of the proposed method for real-time
UAV control in a simulated Unity environment. The method
demonstrates significant improvements in estimation accuracy
and control stability compared to traditional approaches.
This work marks a pivotal advancement in developing
intelligent, data-driven UAV control systems for a quadcopter,
opening new avenues for research in autonomous flight con-
trol. By integrating DMD and PINNs, we aim to develop
robust path trajectory solutions that can withstand environmen-
tal perturbations, providing a reliable and adaptable control
framework for UAVs. Therefore, in this work, we propose the
following:
• We proposed a DMD-PINN model for estimation the
position drone trajectory.
• Present a proposal to simulate drone trajectories for
979-8-3503-7754-5/24/$31.00 ©2024 IEEE
2024 21st International Conference on Electrical Engineering, Computing Science and Automatic Control (CCE) | 979-8-3503-7754-5/24/$31.00 ©2024 IEEE | DOI: 10.1109/CCE62852.2024.10770871
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:34:25 UTC from IEEE Xplore.  Restrictions apply.

## Page 2

training UAVs within a Unity environment, accounting
for various conditions that may affect the drone’s path.
II. DYNAMIC MODE DECOMPOSITION (DMD)
CONTROL FOR UAV
Dynamic Mode Decomposition (DMD) is a data-driven
technique used to decompose complex dynamical systems
into a set of dynamic modes, enabling a reduced-order rep-
resentation that captures the essential behavior of the system
(see Fig. 1). DMD has gained traction in UAV control due
to its ability to identify and isolate dominant patterns from
high-dimensional data, making it suitable for real-time control
applications [12].
A. State-Space Representation
For UAVs, the equations of state typically describe the evo-
lution of the system’s position and orientation over time [18].
The state vector xk can include position coordinates (x, y, z)
and Eular angles (ϕ, θ, ψ), representing roll, pitch and yaw
respectively. The continuos-time state-space model is given
by Eq.(1) [14].
xk+1 = Axk + Buk + wk
yk = Cxk + vk
(1)
where xk is the state vector at time step k, including position
(x, y, z) and orientation (roll, pitch, yaw), A is the system
matrix, B is the input matrix, uk is the control input vector, wk
is the process noise vector and vk measurement noise. DMD
is used to approximate the system dynamics by identifying the
matrix A and B from the collected flight data. The procedure
involves collecting snapshots of the state vector over time and
using these to compute the DMD modes. To control the UAV,
we solve the discrete algebraic Riccati equation (DARE) [19]
to obtain the optimal state feedback gains.
B. Solving the Riccati Equation
To achieve accurate position estimation, the discrete alge-
braic Riccati equation (DARE) is solved. The DARE is given
by Eq.(2):
X = AT XA −AT XB
R + BT XB
−1 BT XA + Q, (2)
where X is the solution to the Riccati equation (2), Q and
R are weighting matrices that penalize the state and control
input, respectively. The control law derived from solving the
Riccati equation Eq.(3):
uk = −
R + BT XB
−1 BT XAxk,
(3)
C. Limitations in the Presence of Noise
One of the significant challenges in using DMD control
for UAVs is its sensitivity to noise. Process noise wk(t)
and measurement noise vk can introduce inaccuracies in the
estimation of the system matrices A and B. This, in turn,
affects the accuracy of the reduced-order model and the
solution to the Riccati equation.
In the presence of noise, the estimated state ˆxk may deviate
from the true state xk, leading to suboptimal control inputs.
The effect of noise can be mitigated to some extent by
incorporating robust filtering techniques, such as the Kalman
filter [20], which can help improve state estimation by ac-
counting for noise in the measurements.
However, despite these techniques, noise remains a signifi-
cant limitation in achieving precise control. The integration
of PINNs with DMD aims to address this limitation by
incorporating physical constraints directly into the learning
process, ensuring that the model adheres to the underlying
physics of UAV dynamics even in noisy environments. This
integration enhances the robustness and accuracy of UAV
control, making it more reliable under various perturbations.
III. DYNAMIC MODE DECOMPOSITION (DMD)
WITH PHYSICS-INFORMED NEURONAL NETWORK
(PINNS)
Integrating DMD and PINNs offers a robust control strategy
that accurately estimates the UAV’s position and orientation,
even in noise and environmental perturbations. By minimizing
the composite loss function, the PINN framework ensures that
the estimated states conform to the physical laws of UAV
dynamics, resulting in improved accuracy and stability. The
training process involves adjusting the neural network param-
eters to minimize these loss functions, thereby enhancing the
overall performance of the control system (see Fig. 2).
For the process of integration DMD with PINN define the
following steps:
1) Data Acquisition and Preprocessing: A comprehensive
dataset comprising UAV flight information Xin, includ-
ing Euler angles (ϕ, θ, ψ), position coordinates (x, y, z),
and noisy observations . This dataset serves as the input
for the DMD process.
2) Dynamic Mode Decomposition (DMD): The input data
is processed using DMD to extract the system matrices
A
B
Q
R
representing the UAV dynamics and
control parameters. These matrices create a reduced-
order model that captures the dominant modes of the
UAV’s behavior.
3) Solving the Discrete Algebraic Riccati Equation
(DARE): The matrices obtained from DMD are used
to solve the discrete algebraic Riccati equation (DARE),
providing an initial state estimate ˆX1. The Riccati equa-
tion is given by Eq. (2)
4) Neural Network (NN) Refinement: The initial state
estimate ˆX1 is then refined using a Physics-Informed
Neural Network (PINN). The architecture consists of
fully connected layers with ReLU activation functions
between layers:
• Input Layer: The network takes as input system
matrices.
• First Layer: The flattened input passes through a
fully connected layer with 128 neurons, followed by
a ReLU activation.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:34:25 UTC from IEEE Xplore.  Restrictions apply.

## Page 3

Fig. 1: Process of integrating Dynamic Mode Decomposition (DMD) with control to solve the discrete algebraic Riccati
equation (DARE) for UAV position and orientation estimation.
Fig. 2: Process of integrating DMD with PINN for UAV position and orientation estimation. The sequence illustrates the
training process, including the loss function and neural network architecture.
• Second Layer: The output of the first hidden layer
is passed through another fully connected layer with
128 neurons, again followed by a ReLU activation.
• Output Layer: The output from the second hidden
layer is passed through a final fully connected
layer that outputs a vector reshaped into the desired
size of A (state dimension squared), producing an
estimated matrix
ˆ
Xk for the given system. This
matrix represents a control output in the form of
a transformation of the input matrices.
This neural network framework incorporates physical
laws and constraints directly into the learning process,
improving the accuracy of the state estimates. The
refinement process involves minimizing a composite loss
function, where the variable α=0.1 and β=0.05 used to
adjust the loss function:
L =
 ˆXk −ˆX1
+α
 ˆXk,0
+β
 ˆXk,0 −ˆXk,−1
 , (4)
• PDE Loss
 ˆXk −ˆX1
: Ensures that the neural
network solution adheres to the partial differential
equations governing the UAV dynamics.
• Initial Condition Loss α
 ˆXk,0
: Penalizes devi-
ations from the initial conditions.
• Boundary Condition Loss β
 ˆXk,0 −ˆXk,−1
: En-
sures continuity and smoothness in the state esti-
mates over time.
5) Control Law and Position Estimate: The refined state
estimate
ˆXk is used to update the control law. The
control law is given by:
ˆXk = AT A −AT B

R + BT ˆXinB
−1
BT A + Q
K =

R + BT ˆXinB
−1 
BT ˆXinA

(5)
This step involves computing the optimal control inputs
based on the refined state estimates to achieve accurate
UAV position and orientation control.
6) Output: The final output ˆXk consists of the estimated
position (ˆx, ˆy, ˆz) and Euler angles

ˆϕ, ˆθ, ˆψ

.
A. Training
The training process for the PINNs involves adjusting the
neural network parameters to minimize the composite loss
functions Eq. (4). By incorporating physical constraints and
leveraging the DMD-extracted dynamic modes, the PINNs
framework ensures robust and accurate UAV state estimations,
even in noise and environmental perturbations. For training,
we used the IMCIS [21] and Package Delivery UAV [22]
datasets. The network was trained for a maximum of 5000
iterations, with an early stopping criterion based on a network
error tolerance of 10−4. The Adam optimizer was utilized,
and the training duration ranged from 30 to 50 minutes. The
network configuration included three fully connected (Linear)
layers and two ReLU activation functions. The calculations
were executed using an NVIDIA GTX GeForce RTX 4060
graphics processing unit (GPU). For testing the model (for
example, we considered four different trajectory cases as
shown in Figure 3), we developed an environment in Unity that
includes a physics-based simulation incorporating factors such
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:34:25 UTC from IEEE Xplore.  Restrictions apply.

## Page 4

TABLE I: Comparison of UAV control performance metrics
for DMD,DMD-PINN,Multiple Linear Regressor (MLP),CNN
approaches. The metrics include RMSE, MAE, and R2.
The DMD-PINN approach shows improved performance with
lower RMSE and MAE values and a higher R2 value com-
pared to the DMD approach.
Method
RMSE
MAE
R2
MLR [25]
143.47
75.37
0.49
CNN [26]
89.63
37.31
0.42
DMD
20.58
16.55
0.58
PINN
8.92
7.35
0.37
as gravity and perturbation noise. The integration between the
control model and the simulation environment was achieved
using the UDP communication protocol (see Fig. 4).
IV. SIMULATION RESULTS
To evaluate the proposed neural network model, we trained
it using the IMCIS and Package Delivery UAV datasets,
specifically designed for a quadcopter UAV. To simulate real-
world outdoor conditions, the data was augmented with noise.
The model’s performance was tested in a Unity simulation
environment (see Fig. 4), using 200 trials. We compared its
results against DMD, CNN, and MLR models, as well as
the proposed PINNs, by calculating key performance metrics:
Root Mean Square Error (RMSE) [23], Mean Absolute Error
(MAE) [23], and the coefficient of determination (R2) [24].
The results indicated that the DMD-PINN model achieved
lower RMSE and MAE values and a higher R2 value, reflect-
ing more accurate and reliable trajectory control (see Table I).
The improvements observed when applying PINNs over the
simple DMD model are evident in these metrics. The testing
results, including position estimates (x, y, z) with added noise
for different cases, are presented in Figures 5.
V. DISCUSSION SIMULATION RESULTS
The integration of DMD with PINNs has substantially im-
proved UAV trajectory control, as demonstrated through both
quantitative and qualitative metrics. The DMD-PINN model
achieved significantly lower RMSE and MAE compared to
alternative models, including CNN, MLR, and the DMD-only
model (see Table I). These results underscore its superior ac-
curacy and reliability in controlling UAV trajectories. Further-
more, the DMD-PINN model exhibited closer alignment with
ground truth trajectories and demonstrated robust performance
across various test scenarios, indicating a substantial leap in
the model’s ability to handle noise and maintain precision
in dynamic environments. This blend of DMD with PINNs
suggests a robust methodology for improving the fidelity of
UAV control systems under diverse operational conditions.
VI. EMBEDDED SYSTEM FEASIBILITY
To deploy the PINN model on embedded systems for
drones, we focus on widely-used architectures like the Nvidia
Jetson Nano and the Raspberry Pi. The Nvidia Jetson Nano
is particularly well-suited for this application due to its GPU
acceleration, which makes it highly feasible for real-time tasks.
Conversely, while the Raspberry Pi is capable of running the
model, it may necessitate performance enhancements such
as reduced precision or optimized inference frameworks to
meet the stringent real-time control requirements. Although
the architecture is manageable on the Jetson Nano, achieving
real-time performance on the Raspberry Pi requires further
optimizations, particularly for control applications that neces-
sitate immediate feedback and adjustments.
VII. CONCLUSION
The combination of DMD with PINNs has significantly
improved UAV trajectory control, as demonstrated by the
superior performance indicators of the DMD-PINN model.
Achieving significantly lower RMSE and MAE values, and a
higher R2 score than the standalone DMD model, this hybrid
approach has proven its ability to provide more precise and
reliable trajectory estimations. Through various test cases, the
DMD-PINN model demonstrated its robustness in accurately
following ground truth trajectories with minimal deviation and
noise, especially under challenging conditions. This integration
not only improves the accuracy and efficiency of UAV control
systems but also establishes a framework to optimize UAV
performance across diverse operational scenarios.
REFERENCES
[1] Z. Zaheer, A. Usmani, E. Khan, and M. A. Qadeer, “Aerial surveillance
system using uav,” in 2016 Thirteenth International Conference on
Wireless and Optical Communications Networks., 2016, pp. 1–7.
[2] S. Rachmawati, A. Syah Putra, A. Priyatama, D. Parulian, D. Katarina,
M. Tri Habibie, M. Siahaan, E. Prawesti Ningrum, A. Medikano,
and V. Valentino, “Application of drone technology for mapping and
monitoring of corn agricultural land,” in 2021 International Conference
on ICT for Smart Society (ICISS), 2021, pp. 1–5.
[3] J. Martinez-Carranza and L. O. Rojas-Perez, “Warehouse inspection
using autonomous drones and spatial ai,” in Machine Learning for
Complex and Unmanned Systems.
CRC Press, 2024, pp. 259–276.
[4] B. Alkouz, B. Shahzaad, and A. Bouguettaya, “Service-based drone
delivery,” in 2021 IEEE 7th International Conference on Collaboration
and Internet Computing (CIC), 2021, pp. 68–76.
[5] R. Thomazella, J. E. Castanho, F. Dotto, O. R. J´unior, G. Rosa,
A. Marana, and J. Papa, “Environmental monitoring using drone images
and convolutional neural networks,” in IGARSS 2018 - 2018 IEEE
International Geoscience and Remote Sensing Symposium, 2018, pp.
8941–8944.
[6] M. E. Castro F´unez, A. F. B´aez Aponte, S. P. Triana, L. C. Ro-
driguez Barrios, D. V. Mu˜noz, and P. A. Mozuca Tamayo, “A pid-
controlled quadcopter system: The effect of parameters selection,”
in 2020 IX International Congress of Mechatronics Engineering and
Automation (CIIMA), 2020, pp. 1–6.
[7] A. Sahu, H. Kandath, and K. M. Krishna, “Model predictive control
based algorithm for multi-target tracking using a swarm of fixed wing
uavs,” in 2021 IEEE 17th International Conference on Automation
Science and Engineering (CASE), 2021, pp. 1255–1260.
[8] L. O. Rojas-Perez and J. Martinez-Carranza, “Deeppilot: A cnn for
autonomous drone racing,” Sensors, vol. 20, no. 16, p. 4524, 2020.
[9] L. O. Rojas Perez and J. Mart´ınez Carranza, “Autonomous drone racing
with an opponent: A first approach,” Computaci´on y Sistemas, vol. 24,
no. 3, pp. 1271–1279, 2020.
[10] A. Sonmez, E. Kocyigit, and E. Kugu, “Optimal path planning for
uavs using genetic algorithm,” in 2015 International Conference on
Unmanned Aircraft Systems (ICUAS), 2015, pp. 50–55.
[11] J. Velagi´c, N. Osmi´c, V. Klovo, and H. Laˇcevi´c, “Design of lqr controller
for 3d trajectory tracking of octocopter unmanned aerial vehicle,” in
2022 8th International Conference on Control, Decision and Information
Technologies (CoDIT), vol. 1, 2022, pp. 63–68.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:34:25 UTC from IEEE Xplore.  Restrictions apply.

## Page 5

Fig. 3: Reference drone trajectory used for evaluating the performance of DMD and PINN control methods.
Fig. 4: The proposed framework design outlines the interaction
between the PINN control system and the Unity environment,
facilitated through the UDP communication protocol.
[12] A.
Perrusqu´ıa,
W.
Guo,
B.
Fraser,
and
Z.
Wei,
“Uncovering
drone intentions using control physics informed machine learning,”
Communications Engineering, vol. 3, no. 1, p. 36, Feb 2024. [Online].
Available: https://doi.org/10.1038/s44172-024-00179-3
[13] W. Gu, S. Primatesta, and A. Rizzo, “Physics-informed neural
network
for
quadrotor
dynamical
modeling,”
Robotics
and
Autonomous Systems, vol. 171, p. 104569, 2024. [Online]. Available:
https://www.sciencedirect.com/science/article/pii/S0921889023002087
[14] A. A. Stoorvogel and A. J. Weeren, “The discrete time riccati equation
related to the h control problem,” in 1992 American Control Conference,
1992, pp. 1128–1132.
[15] M. Navabi and H. Mirzaei, “-d based nonlinear tracking control of
quadcopter,” in 2016 4th International Conference on Robotics and
Mechatronics (ICROM), 2016, pp. 331–336.
[16] T. K. Sheng and M. F. Rahmat, “Modeling and control of unmaned
aerial vehicles,” in 2023 IEEE 13th International Conference on Control
System, Computing and Engineering (ICCSCE), 2023, pp. 364–369.
[17] A. A. Zhilenkov and I. R. Epifantsev, “System of autonomous navigation
of the drone in difficult conditions of the forest trails,” in 2018 IEEE
Conference of Russian Young Researchers in Electrical and Electronic
Engineering (EIConRus), 2018, pp. 1036–1039.
[18] J. L. Proctor, S. L. Brunton, and J. N. Kutz, “Dynamic mode
decomposition with control,” SIAM Journal on Applied Dynamical
Systems, vol. 15, no. 1, pp. 142–161, 2016. [Online]. Available:
https://doi.org/10.1137/15M1013857
[19] G. Nedzhibov, “An improved approach for implementing dynamic
mode decomposition with control,” Computation, vol. 11, no. 10, 2023.
[Online]. Available: https://www.mdpi.com/2079-3197/11/10/201
[20] S. Alqahtani, S. Taylor, I. Riley, R. Gamble, and R. Mailler, “Predictive
path planning algorithm using kalman filters and mtl robustness,” in
2018 IEEE International Symposium on Safety, Security, and Rescue
Robotics (SSRR), 2018, pp. 1–7.
[21] M.
Street,
“Drone
identification
and
tracking,”
2021.
[Online].
Available: https://kaggle.com/competitions/icmcis-drone-tracking
[22] T. A. Rodrigues, J. Patrikar, A. Choudhry, J. Feldgoise, V. Arcot,
A. Gahlaut, and et al., “Data collected with package delivery quadcopter
drone,” https://doi.org/10.1184/R1/12683453.v1, 2020, dataset.
[23] P. Lu, M. Liu, X. Zhang, G. Zhu, Z. Li, and C.-Y. Su, “Neural
network based adaptive event-triggered control for quadrotor unmanned
aircraft robotics,” Machines, vol. 10, no. 8, 2022. [Online]. Available:
https://www.mdpi.com/2075-1702/10/8/617
[24] “Automatic obstacle avoidance of quadrotor uav via cnn-based learning,”
Neurocomputing, vol. 402, pp. 346–358, 2020.
[25] G.
K.
Uyanık
and
N.
G¨uler,
“A
study
on
multiple
linear
regression
analysis,”
Procedia
-
Social
and
Behavioral
Sciences,
vol.
106,
pp.
234–240,
2013,
4th
International
Conference on New Horizons in Education. [Online]. Available:
https://www.sciencedirect.com/science/article/pii/S1877042813046429
[26] Z.
Wang,
W.
Yang,
L.
Xiang,
X.
Wang,
Y.
Zhao,
Y.
Xiao,
P. Liu, Y. Liu, M. Banu, O. Zikanov, and L. Chen, “Multi-input
convolutional network for ultrafast simulation of field evolvement,”
Patterns,
vol.
3,
no.
6,
p.
100494,
2022.
[Online].
Available:
https://www.sciencedirect.com/science/article/pii/S2666389922000794
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:34:25 UTC from IEEE Xplore.  Restrictions apply.

## Page 6

(a)
(b)
(c)
(d)
Fig. 5: Trajectory estimation results from test cases comparing DMD-LQR and DMD-PINN approaches are presented for the
ground truth versus estimated trajectories in the x, y, and z coordinates. The cases are as follows: (a) Case 1: Trajectory in
Fig. 3a, (b) Case 2: Trajectory in Fig. 3b, (c) Case 3: Trajectory in Fig. 3c, and (d) Case 4: Trajectory in Fig. 3d.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:34:25 UTC from IEEE Xplore.  Restrictions apply.
