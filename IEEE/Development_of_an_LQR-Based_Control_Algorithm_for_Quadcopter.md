# Development_of_an_LQR-Based_Control_Algorithm_for_Quadcopter.pdf

## Page 1

Development of an LQR-Based Control Algorithm 
for Quadcopter      
Aizaz Ali Khan  
Dept. of Robotic and Mechatronics 
School of Engineering and      
Digital Science(SEDS)      
Nazarbayev University      
Astana, Kazakhstan     
aizazali.khan@nu.edu.kz 
Syuhei Kurokawa  
Dept. of Mechanical Engineering, 
Kyushu University, Nishi-ku, 
Fukuoka 819-0395, Japan 
kurobe-@mech.kyushu-u.ac.jp 
Ton Duc Do  
Dept. of Robotic and Mechatronics 
School of Engineering and 
  Digital Science (SEDS) 
Nazarbayev University   
  Astana, Kazakhstan   
 doduc.ton@nu.edu.kz 
Md. Hazrat Ali*  
Dept. of Mechanical and Aerospace Engineering 
School of Engineering and   
 Digital Science (SEDS) 
Nazarbayev University      
Astana, Kazakhstan      
*md.ali@nu.edu.kz
Abstract— The increasing use of unmanned aerial vehicles 
(UAVs) necessitates the development of more sophisticated 
control algorithms to enhance the performance of rotary-wing 
UAVs. This article discusses the implementation of a linear 
quadratic regulator (LQR) controller as a control technique for 
the flight controller of the Qdrone1, developed by Quanser. 
While LQR analysis is well-known, our approach distinguishes 
itself through the integration of an advanced six-camera system 
to establish an exceptionally accurate reference point for the 
drone. This innovative use of the OptiTrack system for precise 
position tracking feeds into the control algorithm, significantly 
enhancing the accuracy and stability of the UAV. The LQR 
controller 
is 
evaluated 
in 
real-time 
using 
the 
MATLAB/Simulink environment, including control loops for 
altitude, position, and attitude. The primary objective is to 
develop an optimal controller for effectively regulating the 
drone's motion while maintaining the utmost stability and 
accuracy. Using its dynamic model, a MATLAB Simulink 
algorithm is developed to control the quadrotor. This work 
further demonstrates the creation and verification of a 
simulation model for Qdrone1. The correctness of the model is 
evaluated by comparing its simulated outcomes with data 
obtained from flight testing. The flight data and simulation 
results show the model's reliability. The main goal of this 
research is to develop a precise dynamic model and LQR 
controller for Qdrone1, allowing for the comprehensive 
evaluation of this specific UAV configuration. 
Keywords—Quadcopter, 
Flight 
controller, 
Model-based 
design, Linear quadratic regulator (LQR) controller, Modelling. 
I. 
INTRODUCTION 
Unmanned aerial vehicles (UAVs) have been significantly 
contributing to many civilian applications over the last several 
decades. Specifically, rotary-wing UAVs have been used in 
many applications, and shortly, corporations intend to expand 
their utilization further. Agricultural operations extensively 
use UAVs for tasks such as field mapping, plant stress 
detection, and chemical spraying. In some circumstances, 
drones are already ensuring optimal performance from 
outdated equipment, resulting in a significant decrease in 
operating times [1]. Recently UAVs have been used for aerial 
surveillance and surveying purposes. These drones may be 
fitted with remote sensing cameras to identify water sources 
in arid regions or locate water leaks in underground pipes [2]. 
Additionally, some are used to gather data from areas 
impacted by natural calamities. Within a decade UAVs might 
be extensively used for delivery purposes, taking advantage of 
the vertical dimension [3]. This would result in a significant 
reduction in delivery times and less congested streets. 
Flight controllers for UAVs play a critical role in ensuring 
optimal flying performance and exceptional stability for these 
aircraft [4]. Specifically, rotary-wing UAVs possess inherent 
static 
and 
dynamic 
instability, 
necessitating 
the 
implementation of precise control algorithms to ensure stable 
flight and execute maneuvers. Many flight controllers in 
commercial rotary-wing UAVs use a proportional-integrative-
derivative (PID) control algorithm, which can be readily 
adjusted and executed on a microcontroller [5]. PID control is 
effective in ensuring flight stability. However, the growing 
demand for UAVs has prompted several academics to devise 
and evaluate more sophisticated control systems. Capello et 
al. introduced an L1 adaptive controller as the autopilot for the 
inner loop of a fixed-wing UAV [6]. Kyaw and Gavrilov used 
the L1 adaptive controller to manage the attitude control of a 
quadcopter. They also presented a straightforward method for 
designing the controller. Model predictive control (MPC) has 
mostly been evaluated using simulation models [7]. This 
control technique demonstrates the benefit of not relying on 
model parameters, making it particularly efficient in 
addressing nonlinearities and uncertainties in the model. Islam 
et al. conducted a successful simulation-based experiment to 
investigate the effectiveness of a linear Model Predictive 
Control (MPC) system for trajectory control of a quadcopter 
UAV [8]. Suhail highlighted the adoption of a unique control 
strategy termed active disturbance response (ADR) [9] 
because of the quadcopter's susceptibility to disturbances and 
the significant nonlinear effects it experiences. The results 
presented in the research show that the ADR has a superior 
capacity to respond quickly to disturbances compared to a PID 
controller [10]. Additionally, neural network (NN) methods 
have been suggested for constructing the flight controller's 
inner loop [11]. A simulation tool was developed to create a 
model-based controller using a radial basis function neural 
network trained with the minimum resource allocating 
2024 IEEE 12th Conference on Systems, Process & Control (ICSPC), 7 December 2024, Malacca, Malaysia
979-8-3503-9139-8/24/$31.00 ©2024 IEEE
142
2024 IEEE 12th Conference on Systems, Process & Control (ICSPC) | 979-8-3503-9139-8/24/$31.00 ©2024 IEEE | DOI: 10.1109/ICSPC63060.2024.10862615
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:38:32 UTC from IEEE Xplore.  Restrictions apply.

## Page 2

network (MRAN) algorithm [12], offering an accurate 
representation of quadcopter attitude dynamics [13]. 
This study presents a novel approach by integrating an 
advanced six-camera OptiTrack system for exceptionally 
accurate reference point establishment and precise position 
tracking for the Qdrone1. This innovative integration 
significantly enhances the LQR controller's accuracy and 
stability. The LQR-based controller with integrative action 
was designed using MATLAB/Simulink software, tailored to 
Qdrone's specific characteristics. The controller's responses 
were tested with control inputs and reference trajectories, 
demonstrating superior performance. This unique integration 
and 
real-time 
evaluation 
in 
a 
MATLAB/Simulink 
environment set this work apart from existing control 
techniques. 
II.
MATHEMATICAL MODEL OF QUADCOPTER
This section outlines the creation of a mathematical model for 
the quadcopter that considers non-linear factors. Before 
constructing the model, the following assumptions are made: 
•
The quadcopter is classified as a rigid body, which
implies that any vibrations or deformations that occur
during flight are disregarded.
•
The motor's thrust is unaffected by external influences
such as variations in air density, temperature, and
altitude [15].
•
An Inertial Reference Frame ⃗: 
⃗, 	
⃗, 
⃗ Is a
coordinate system anchored to the Earth that usually
places its starting point at ground level.
•
The Body Reference Frame⃗: 
⃗, 	
⃗, 
⃗ Is defined with
its origin located at the center of gravity (COG) of the
quadrotor.
•
The origin of the Horizon Reference Frame ⃗: 0, 0, ℎ
⃗
is the quadrotor's mass center, and its axes are oriented
in the direction of the horizon, or the nearby vertical and
horizontal planes shown in Fig 1.
Fig. 1. North-east-down (NED) reference system [12]. 
A. Nonlinear Dynamic Equation of Quadcopter using 
Euler's equation 
The motion of the quadcopter is described in both the body 
and inertial frames. In the inertial frame, the quadcopter's 
position and velocity are represented as x=(x, y, z)T and  
˙, ˙, ˙ Respectively. In the body frame, the velocity is
represented as   , ,  . we define the roll, pitch, and
yaw angles in the body frame as ! = (ϕ, θ, ψ)T, The vector. 
Ω  ϕ˙ , θ˙, ψ˙ & represents the angular rates [14]. It is crucial
to comprehend that the angular velocity vector Ω is not equal 
to the angular velocity. !˙ . The angular velocity is a vector 
that specifies the rotational direction, whereas ' ( represents
the rate of change of the yaw, pitch, and roll in an inertial 
frame the relation is given as: [16]. 
)  *
+
,
-
.  /
1
0
12'
0
34
243'
0
124
343'
5 6
4
'(
7(
(
8  
(1) 
Ω  9!˙  , 9 ∈ℝ
<
The quadrotor's location and rotation vector can be 
represented as = = [> !] ?. The vector is defined as [   ϕ 
' 7] ?. The linear and angular velocities are represented by 
the vector V = [A Ω] ?, where A represents the linear velocities 
in the , , and  directions, and Ω represents the angular 
velocities around the +, ,, and - axes  = [A Ω] ? = [   
+ , -] ?. The translational motion is determined by the 
positional state variables. BC⃗ in the inertial frame and the
positional state variables BD⃗. In the body frame. R is Rotation
matrices in eq (3): 
 *



.
C⃗
 E *



.
D⃗
(2) 
E    /
3'37
242'37 1 3427
342'37 F 2427
3'27
242'27 F 3427
342'27 1 2437
12'
243'
343'
5 
(3) 
In equation (3) sin(τ) is replaced with sτ and cos(τ) is replaced 
with cτ where τ = ',4, 7. 
The quadrotor's translational and rotational kinetic energy is 
determined by the following equations [16]: 
?GHIJK  1
2 MN˙ N˙
?HOG  1
2 Ω˙ PΩ˙
and P  diag PU
PV
PU ∈ℝ
<
  matrix represents the
inertia of the quadrotor in the body-fixed frame, which is a 
result of its symmetry. The quadrotor's Euler-Lagrange 
equation is provided [17]: 
W
WX Y
Z[
Z\
. ^ 1
Z[
Z\   _`
ab                                (4)
F represents the external force applied to the quadrotor. τ 
represents the generalized moments around the UAV. 
The equation for force is given by `  `c F `X  and a 
ad
ae
af  where `c  is the force of translational
movement created by propellers and `X  is the drag forces
acting on the quadrotor along ,	,
 vectors, g  ∑Xi
j
 g
and `c  gElm .
`c  g /
342'37 F 2427
342'27 1 2437
343'
5 
(5) 
`X  6
1noU
0
0
0
1noV
0
0
0
1nop
8 >˙ 
(6) 
where noU, noV, nop are drag coefficients, now putting F in
equation (5). 
                   M /
q
q
q
5   g /
342'37 F 2427
342'27 1 2437
343'
5 F
                6
1noU
0
0
0
1noV
0
0
0
1nop
8 >( 1 Mr /
0
0
1
5 
(7) 
2024 IEEE 12th Conference on Systems, Process & Control (ICSPC), 7 December 2024, Malacca, Malaysia
143
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:38:32 UTC from IEEE Xplore.  Restrictions apply.

## Page 3

M
..  (342'37 F 2427)u 1 noU˙
(8) 
M¨  (342'27 1 2437)u 1 nwV˙
(9) 
M¨  (343')u 1 Mr 1 nop
.
(10) 
Whereas 
.., 
..  and 
..  represent linear accelerations in the 
horizon 
frame. 
The 
Euler 
equation, 9  PΩ˙ F Ω <
PΩ   yields the following three angular motion equations [12]: 
PΩ(  Ω < PΩ F x JH(Ω < e
)Ω{ F a
j
{i
(11) 
6
|U
0
0
0
|V
0
0
0
|
8 6
4
..
'
..
7q
8  }
'
.
7(~|p 1 |V•
4(7((|U 1 |p)
'(4(~|V 1 |U•
€ F 6
P•'(Ω•
1P•4(Ω•
0
8 F /
ad
ae
af
5 (12)
4
..
 '˙7˙‚ƒ 1 ‚	ƒ'˙ΩH F „du	
(13) 
'
..
 4˙7˙‚… 1 ‚	…7˙Ω• F „eu
(14) 
7¨  4˙'˙‚† F uj
(15) 
Where, ‚ƒ  (|V 1 |p)/|U , ‚	ƒ 
ˆ‰
ˆŠ   , ‚…  (|p 1 |U)/|V
, ‚…  |•/|V  , ‚†  (|U 1 |V)/|p  , „d  „/|U  , „e  „/|V
and „f  „/|p with „ representing the length, Ωr denotes rotor
inertia  Ωr = ω2 + ω4 − ω1 − ω3. 
III. LINEARIZATION OF THE QUADCOPTER MODEL
When the sets of equations specified in Equations (8)-(10) 
and (13)-(15) are examined, it contains nonlinear 
expressions. These equation sets need to be linearized since 
this research will use linear control approaches. The 
equilibrium point for linearization was identified as the 
quadcopter's hover position, with the position vector 
represented as +     and the velocity vector as ‹ 
0 0 0. Consider the equation to be linearized [17].
      Y′′(t) = f (Y(t), Y'(t), U(t), U'(t)) 
The procedure for linearizing this equation is as follows: 
•
We calculate the partial derivatives with respect to its
different variables and we evaluate these derivatives at
the equilibrium point considered.
•
We write the expansion limited to order 1 of the function
f, neglecting the higher order terms to reduce the
function f to its linear part only.
•
We write from our initial equation, the equation of the
resulting behavior, namely:
Y"(t)  
•o
•• |•’,’,“’,’ ∗ (Y(t)-Y0) F 
•o
•–— |•’,’,“’,’  ∗ (Y′(t)-0) 
F
•o
•“ |•’,’,“’,’∗ (U(t)-U0)F 
•o
•š— |•’,’,“’,’  ∗ (U′(t)-0).      (16)
 In the small angle’s approximation, the cosine values are an 
approximation. By applying the first-order Taylor expansion 
to the Dynamic Equation at the equilibrium point, we get the 
linear model of the quadrotor. 

..  r' 
(17) 

..  14r 
(18) 
M
..  T
(19) 
4
..
 ud
|U
(20) 
'
..
 ue
|V
(21) 
7¨  uf
|p
(22) 
IV. DEVELOPMENT OF LQR ALGORITHM FOR
QUADCOPTER 
The linear quadratic regulator is an optimum linear control 
approach that conducts optimization over system dynamics 
using feedback from all states. First it is necessary to model 
the system that is to be controlled in the following state space 
equations [18]: 
˙  œ F  
(23) 
  • F ž 
(24) 
(Ÿ)  1n(Ÿ) 
(25) 
K is optimized using the cost function in LQR controller 
design: 
P  ∫’
¡ (¢ F E)£Ÿ
(26) 
In Equation (25), Q represents the weight matrix and R 
represents the control matrix. The determination of the 
optimum coefficient is performed in the following manner 
[19]. 
 The state variables and inputs for height in this system are as 
follows: 
p   (, p  ? 1 Mr 
(27)
The state-space representation is given by the following 
equation: 
p˙  _0
1
0
0b p F ¤ 0
1/M¥ p
(28) 
p  1   0p
(29) 
Position Updates in the x and y coordinates of the quadcopter 
also impact the rotation around the longitudinal and lateral 
axes in the reference frame of the quadcopter. The 
modifications may be expressed in the following manner for 
the transnational Equation:   
¨W  ?
M (cos 4sin ')
¨W  ?
M (1sin 4)
¨W  ?
M (cos 4cos ')⎭
⎪
⎬
⎪
⎫
 
'W  atan ¤
¨W
¨W F r¥
4W  atan ¤1¨Wcos '
¨W F r ¥
        (30) 
State-space representation for reference position control in 
the X-Y axis is: 
¯°±   D²   
..  D²  
.., U  ', V  ³
(31) 
¯°±  x  y
˙¯°±  }
0  0  1  0
0  0  0  1
0  0  0  0
0  0  0  0
€ }


(
(
€ F }
  0   0
  0   0
  0   r
1r 0
€ ¯°±
(32) 
¯°±  1 1p
(33) 
The state variable and inputs for the altitude Controller are 
expressed as: 
¶·X  4W  4(   'W  '  ˙ 7  7˙, e  ae
(34) 
, d  ad, f  af
·X  4W  'W  7  
2024 IEEE 12th Conference on Systems, Process & Control (ICSPC), 7 December 2024, Malacca, Malaysia
144
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:38:32 UTC from IEEE Xplore.  Restrictions apply.

## Page 4

˙·X 
⎣
⎢
⎢
⎢
⎢
⎡0  0  0  1  0  0
0  0  0  0  1  0
0  0  0  0  0  1
0  0  0  0  0  0
0  0  0  0  0  0
 0  0  0  0  0  0 ⎦
⎥
⎥
⎥
⎥
⎤
 
⎣
⎢
⎢
⎢
⎢
⎡



(
(
(⎦
⎥
⎥
⎥
⎥
⎤
F
⎣
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎡   0   0   0  
 0   0   0
0   0   0
 1
|U
   0   0
 0   1
|V
   0
 0   0     1
|p
 ⎦
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎤
·X
(35) 
·X  1 1p
(36) 
The Q and R matrices for each controller were adjusted 
according to these linear models. This approach offers a more 
straightforward method for the tuning process since the linear 
equations are largely independent of each other. This means 
that the adjustment of the specified matrices may be made 
without worrying about how it would impact the stability of 
other states, unless in the case of a cascaded situation. 
Qz = [0.03 0; 0 0.05]. 
Rz = .0002. 
Qpos=diag ([0.1 0.1 0.001 0.001]). 
Rpos=diag ([1 1]). 
Qatt=diag ([20 17 .15 .05 .05 .09]). 
Ratt=diag ([1 1 1]). 
In this procedure, the most optimal gain matrix K is 
determined using MATLAB for the linear model and then 
validated on the non-linear model in Simulink. 
The controller is designed according to the altitude, position, 
and attitude loop structure, as shown in Fig 2. 
  
Fig. 2. The altitude, position, and attitude loop structure used for the LQR 
      controller. 
The LQR controller requires determining the Q and R matrix, 
which can be done through trial and error, and 18 coefficients, 
which govern the quadcopter's x, y, and z locations, without 
using time-consuming optimization procedures like GA. 
V. EXPERIMENTAL SETUP 
A. Hardware 
The experiments are carried out inside a 5.5x3.5 square 
meter area that is surrounded by a safety net shown in Fig 4a. 
As seen in Fig 4b, a total of six cameras are positioned at the 
corners and edges of the workplace. These cameras are linked 
to a computer via wires. OptiTrack utilizes cameras to 
ascertain the precise position and orientation of the UAV. The 
current UAV in use is a Qdrone1, which is produced by 
Quanser, Canada. As per the manufacturer's prescribed plan, 
five markers were affixed on the Qdrone1, as shown in Fig 3. 
B. Real-time Communication and Localization 
The vehicles and computers communicate via a router 
and wireless Wi-Fi connection, providing a unique IP address 
for the computer, drone, and robot. MATLAB Simulink and 
QUARC blocks facilitate vehicle management.  
Fig. 3.  QUANSER Qdrone1. 
C. Experimental procedure 
Fig 5 illustrates the steps of the operation technique 
involving the OptiTrack system detecting the quadcopter's 
location, which is sent to the Mission Server. The server 
computers and transmits the position to the Stabilizer. The 
drone tracks the specified location.Qdrone1 lands after 
receiving instructions. 
Fig. 4(a). Enclosed workspace with a safety net and rubber floor. 
 Fig. 4(b). Communication scheme[12]. 
2024 IEEE 12th Conference on Systems, Process & Control (ICSPC), 7 December 2024, Malacca, Malaysia
145
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:38:32 UTC from IEEE Xplore.  Restrictions apply.

## Page 5

D. MATLAB Simulink 
A Wi-Fi connection and router enable communication 
between the onboard CPU of Qdrone1 and the ground station 
(PC). The control algorithm and mission server are 
implemented using MATLAB. Table 1 presents the precise 
technical details of Qdrone1. When comparing Qdrone1 
dynamics to other quadrotors, the key difference in modeling 
is that the lengths of ¾E¿„„ and ¾pÀŸ3ℎ are not equal. 
TABLE Ⅰ. Description of quadcopter parameter. 
Symbol 
Description 
Value 
Units 
J 
Roll Moment of Inertia 
0.01 
kg*m2 
J 
Pitch Moment of Inertia 
0.082 
kg*m2 
J 
Yaw Moment of Inertia 
0.015 
kg*m2 
b 
Maximum commanded thrust force 
5.11 
N 
d 
Normalized yaw torque constant 
0.048 
Nm 
M 
Total mass of the quadcopter 
1.121 
kg 
g 
Gravitational constant 
9.81 
m/s2 
L_E¿„„ 
Roll motor-to-motor distance 
0.213 
m 
L_B-ÀŸ3ℎ 
Pitch motor-to-motor distance 
0.175 
m 
Fig. 5. Operation procedure flowchart [12]. 
VI. RESULT AND VALIDATION
The drone's position tracking experiments revealed that 
a Linear Quadratic Regulator (LQR) controller provided the 
best stable control in the x, y, and yaw axes, as measured by 
root mean square error (RMSE) and peak-to-peak (P2P) data 
shown in Fig 6(a)-6(d). The LQR controller strikes a balance 
between control effort and system performance by 
minimizing a cost function that penalizes departures from the 
intended trajectory and excessive control inputs. This 
provides accurate tracking performance with minimum 
variance. 
A. Stability of Each Axis: 
The drone's position tracking tests showed that an over 
LQR controller achieved the most stable behavior for x, y, 
and yaw position control. This controller, designed to balance 
control effort and system performance, minimizes deviations 
from the target trajectory and excessive control inputs. The 
quadrotor's precise and effective tracking performance 
ensures the drone accurately follows the target route with 
little deviation shown in Table Ⅱ, demonstrating the 
effectiveness of this controller in drone position tracking. 
Yaw Axis refers to the horizontal axis around which an object 
rotates or moves. The LQR controller stabilizes the yaw axis, 
controlling rotational movement around the vertical axis, by 
making differential thrust changes.  
TABLE ⅠⅠ. Numerical Results 
Metric 
x-axis 
(m) 
y-axis 
(m) 
z-axis 
(m) 
Yaw 
(rad) 
RMSE 
0.04 
0.05 
0.001 
0.01 
 (P2P) 
0.10 
0.12 
0.01 
0.02 
Total Accuracy (%) 
98 
97 
98 
97 
Accumulated Error 
0.07 
0.08 
0.001 
0.005 
Fig.6(a). Z Position vs. time (Position control test, LQR) 
Fig.6(b). Y Position vs. time (Position control test, LQR) 
Fig.6(c). X Position vs. time (Position control test, LQR) 
B. Controller Action 
The LQR controller iteratively computes optimal control 
inputs based on the quadrotor's current state and the planned 
trajectory, considering variables like location, velocity, 
direction, and angular velocity. It solves the Riccati equation 
and applies the feedback gain matrix to address system 
discrepancies. The LQR controller minimizes a quadratic 
cost function to determine the optimum control law, 
2024 IEEE 12th Conference on Systems, Process & Control (ICSPC), 7 December 2024, Malacca, Malaysia
146
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:38:32 UTC from IEEE Xplore.  Restrictions apply.

## Page 6

balancing performance and energy efficiency. It dynamically 
adjusts motor thrusts to realign the quadrotor with the target 
route, minimizing overshooting shown in Fig 7(a),7(b). 
Fig.6(d). Yaw rotation vs. time (Position control test, LQR) 
Fig.7(a)Unsaturated Z(axis)and X(axis) controller commands vs. time 
(LQR)  
Fig.7(b)Unsaturated Y(axis)and Yaw(axis) controller commands vs. time 
(LQR) 
VII. CONCLUSION AND FUTURE WORK
      In this work, the construction and verification of a 
simulation model for the Qdrone1 quadcopter have been 
shown by comparing the results of the simulation with actual 
data collected in the real world. Although the system 
dynamics are extremely nonlinear and interrelated, the model 
is nevertheless useful for developing a control algorithm 
utilizing a model-based approach. The experimental 
approach for determining physical parameters is thoroughly 
explained, demonstrating that the quadcopter's dynamics can 
be precisely calculated using Newton's and Euler's equations, 
even without including wind disturbances and other nonlinear 
factors. Although the model may show discrepancies when 
instructions change rapidly and significantly, it consistently 
and properly predicts the time it takes for something to rise 
and effectively generates the necessary control settings. 
     Future endeavors will prioritize the incorporation of a 
Disturbance Observer (DOB) to augment the precision of the 
model by considering external disturbances such as wind and 
unexpected changes in the payload. In addition, the study will 
focus on enhancing control algorithms to maximize the 
quadcopter's maneuverability and stability in different 
situations, 
guaranteeing 
consistent 
and 
dependable 
performance in real-world uses. This work establishes a 
strong basis for future progress in UAV operations, 
emphasizing the effectiveness of the LQR controller in 
preserving stability and accuracy, thereby improving the 
resilience and reliability of quadcopter control algorithms. 
ACKNOWLEDGEMENT 
This research is funded in part by the Nazarbayev University, 
Kazakhstan under Collaborative Research Program Grant 
No. 11022021CRP1509. 
REFERENCES 
[1] A. J. Abougarair, H. Almgallesh, and N. A. A. Shashoa, "Dynamics 
and Optimal Control of Quadcopter," 2024 IEEE 4th International 
Maghreb Meeting of the Conference on Sciences and Techniques of 
Automatic Control and Computer Engineering (MI-STA), Tripoli, 
Libya, pp. 136-141,2024. 
[2] S. M. Nashit Arshad, Y. Ayaz, S. Ali, K. F. Iqbal and N. Naseer, 
"Modeling and Control of Liquid Carrying Aerial Vehicle's Endurance 
and Performance Based on LQR And PID Control Strategies," 2023 
7th International Multi-Topic ICT Conference (IMTIC), Jamshoro, 
Pakistan, pp. 1-6, 2023. 
[3] B. E. Schafer, D. Picchi, T. Engelhardt, and D. Abel, “Multicopter 
unmanned aerial vehicle for automated inspection of wind turbines,” in 
2016 24th Mediterranean Conference on Control and Automation 
(MED), IEEE, pp. 244–249, Jun. 2016. 
[4] M. Stokkeland, K. Klausen, and T. A. Johansen, “Autonomous visual 
navigation of Unmanned Aerial Vehicle for wind turbine inspection,” 
in 2015 International Conference on Unmanned Aircraft Systems 
(ICUAS), IEEE, pp. 998–1007, Jun. 2015. 
[5] Oktaf Agni Dhewa, Fatchul Arifin, Ardy Seto Priyambodo, Anggun 
Winursito, & Yasir Mohd. Mustafa. (2024). Attitude UAV Stability 
Control Using Linear Quadratic Regulator-Neural Network (LQR-
NN). IIUM Engineering Journal, 25(2), 2024. 
[6] J. Farrell, M. Sharma, and M. Polycarpou, “Backstepping-Based Flight 
Control with Adaptive Function Approximation,” Journal of Guidance, 
Control, and Dynamics, vol. 28, no. 6, pp. 1089–1102, Nov. 2005. 
[7] Z. Zuo and C. Wang, “Adaptive trajectory tracking control of output 
constrained multi‐rotors systems,” IET Control Theory & Applications, 
vol. 8, no. 13, pp. 1163–1174, Sep. 2014. 
[8] J. Spencer, J. Lee, J. A. Paredes, A. Goel, and D. Bernstein, “An 
Adaptive PID Autotuner for Multicopters with Experimental Results,” 
in 2022 International Conference on Robotics and Automation (ICRA), 
IEEE, pp. 7846–7853, May 2022.  
[9] Z. T. Dydek, A. M. Annaswamy, and E. Lavretsky, “Adaptive Control 
of Quadrotor UAVs: A Design Trade Study With Flight Evaluations,” 
IEEE Transactions on Control Systems Technology, vol. 21, no. 4, pp. 
1400–1406, Jul. 2013. 
[10] Y. Jing et al., “PX4 Simulation Results of a Quadcopter with a 
Disturbance-Observer-Based and PSO-Optimized Sliding Mode 
Surface Controller,” Drones, vol. 6, no. 9, p. 261, Sep. 2022. 
[11] A. R. Dooraki and D.-J. Lee, “Reinforcement learning based flight 
controller capable of controlling a quadcopter with four, three and two 
working motors,” in 2020 20th International Conference on Control, 
Automation, and Systems (ICCAS), IEEE, pp. 161–166, Oct. 2020. 
[12] A. Tassanbi, A. Iskakov, T. Do, and Md. Ali, "Interactive Real-time 
Leader Follower Control System for UAV and UGV," in Proc. IEEE 
Int. Conf. on Electrical, Computer and Communication Technologies 
(ICECCME), Dec. 2022. 
[13] A. T. KARAŞAHİN, “Genetically Tuned Linear Quadratic Regulator 
for Trajectory Tracking of a Quadrotor,” Academic Platform Journal 
of Engineering and Smart Systems, vol. 12, no. 1, pp. 37–46, Jan. 2024. 
[14] M. S. Can and H. Ercan, “Real-time tuning of PID controller based on 
optimization algorithms for a quadrotor,” Aircraft Engineering and 
Aerospace Technology, vol. 94, no. 3, pp. 418–430, Feb. 2022. 
[15] I. Siti, M. Mjahed, H. Ayad, and A. El Kari, “New Trajectory Tracking 
Approach for a Quadcopter Using Genetic Algorithm and Reference 
Model Methods,” Applied Sciences, vol. 9, no. 9, p. 1780, Apr. 2019. 
[16] M. N. Shauqee, P. Rajendran, and N. M. Suhadis, “Proportional Double 
Derivative Linear Quadratic Regulator Controller Using Improvised 
Grey Wolf Optimization Technique to Control Quadcopter,” Applied 
Sciences, vol. 11, no. 6, p. 2699, Mar. 2021. 
[17] A. T. KARAŞAHİN, “Genetically Tuned Linear Quadratic Regulator 
for Trajectory Tracking of a Quadrotor,” Academic Platform Journal 
of Engineering and Smart Systems, vol. 12, no. 1, pp. 37–46, Jan. 2024.  
[18] L. Martins, C. Cardeira, and P. Oliveira, “Linear Quadratic Regulator 
for Trajectory Tracking of a Quadrotor,” IFAC-PapersOnLine, vol. 52, 
no. 12, pp. 176–181, 2019.  
[19] R. Mahony, V. Kumar, and P. Corke, “Multirotor Aerial Vehicles: 
Modeling, Estimation, and Control of Quadrotor,” IEEE Robot Autom 
Mag, vol. 19, no. 3, pp. 20–32, Sep. 2012.  
2024 IEEE 12th Conference on Systems, Process & Control (ICSPC), 7 December 2024, Malacca, Malaysia
147
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:38:32 UTC from IEEE Xplore.  Restrictions apply.
