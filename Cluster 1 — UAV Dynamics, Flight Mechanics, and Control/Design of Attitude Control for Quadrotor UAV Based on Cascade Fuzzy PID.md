# Design of Attitude Control for Quadrotor UAV Based on Cascade Fuzzy PID.pdf

## Page 1

Theory and Practice of Science and Technology
2025, VOL. 6, NO. 7, 100-104
DOI: 10.47297/taposatWSP2633-456920.20250607
Design of Attitude Control for Quadrotor UAV Based on Cascade Fuzzy PID
Deng Xin
Dundee International Institute of Central South University, Changsha, Hunan, 410083, China
ABSTRACT
The quadrotor unmanned aerial vehicle's attitude control algorithm was fine-tuned, and a cascade fuzzy PID self-tuning 
algorithm was developed, aiming to stabilise the unmanned aerial vehicle's posture during flight through traditional control 
method analysis. Initially, a complex mathematical representation of the quadrotor unmanned aerial vehicle was created, which 
was then linearised to derive the transfer functions for each channel. Subsequently, a design of a fuzzy controller was developed. 
Drawing on specialised knowledge, data adjustment, and enhancements to the fuzzy controller's rule table, the engineered 
fuzzy controller was integrated alongside the cascade PID controller's angular velocity inner loop. Ultimately, by comparing 
simulations of the conventional cascade PID controller with the cascade fuzzy PID controller via MATLAB-Simulink toolkit, and to 
evaluate the cascade fuzzy PID controller's interference resistance, interference signals were incorporated into the simulation. 
Results from the simulation experiments indicate that the enhanced cascade fuzzy PID outperforms the cascade PID in aspects 
of computation duration, complexity, and tracking inaccuracies. This suggests that the cascade fuzzy PID can improve the 
dynamic efficiency of the quadrotor unmanned aerial vehicle, thus fulfilling its stability needs throughout the mission.
KEYWORDS
Quadrotor unmanned aerial vehicle; Attitude control; Fuzzy control; Cascade PID; Parameter self-tuning
1　Introduction
A quadrotor unmanned aerial vehicle features multiple variables, minimal activation, and robust interconnection. This 
entity encompasses various factors and exhibits a heightened sensitivity to shifts in the environment. Consequently, 
meticulous management of the UAV's directional steadiness is essential. Presently, a variety of contemporary control 
theory-driven control techniques are utilized for managing the orientation of quadrotor UAVs. These include the neural 
network PID algorithm (referenced in), the cascade linear active disturbance rejection controller made up of a linear 
differential controller, a linear extended state observer, and a linear error control law (cited in), all of which are adept at 
managing the UAV's attitude stability. Reference proposed an active disturbance rejection controller optimised by an 
improved dung beetle optimisation algorithm. Reference] introduced the MPC (model predictive control) method into the 
height and attitude control loops of the rotor controller and designed a model correction MPC and PID hybrid control 
algorithm, which improves the dynamic characteristics of the transition mode through iterative optimization and 
compares multiple algorithms. However, most of these control methods are very complex, requiring many floating-point 
and matrix operations, and have high requirements for processors. The UAV is an underactuated system by nature, and 
these control methods make the system even more complex.
Following the refinement of the conventional cascade PID control algorithm, an advanced cascade fuzzy PID controller 
was created to enhance the stability of the unmanned aerial vehicle's flight orientation. Positioning the fuzzy controller 
within the drone's inner loop enhances its stability in attitude and reduces interference. Concurrently, adjustments and 
enhancements were made to the fuzzy rules in alignment with these rules. Following this, MATLAB was utilized to 
perform control variable simulation tests on both the refined fuzzy control technique and the conventional cascade PID 
control approach, with a comparison of the simulation outcomes to confirm the superior stability of this method. This 
diminishes the likelihood of crashes and collisions due to unstable positioning, facilitating the drone's attainment of 
steady and secure flight.
2　Modelling
2.1　Coordinate system
For a precise depiction of the quadrotor UAVs' movement, establishing a coordinate system is the initial step. This 
design incorporates two distinct coordinate systems: the ground cartesian (inertial) and the body coordinate systems. In 
the inertial coordinate framework, the starting point O is set at a specific ground point, with the X-axis moving northward, 
the Y-axis eastward, and the Z-axis ascending in parallel, creating a right-handed coordinate system. The o-xyz body 
coordinate system, distinct from the ground system and linked to the quadrotor, enables it to move in unison with the 
quadrotor, recording its movements and directions. The starting point O aligns with the quadrotor UAV's mass center, 
while the x-axis runs parallel to the body's longitudinal axis and the nose is oriented positively. The y-axis runs parallel to 
the body's right side, and the z-axis stands perpendicular to the body's plane downwards. The terrestrial system remains

## Page 2

Theory and Practice of Science and Technology
largely unchanged, in contrast to the body system's dynamic nature, which varies as the quadrotor moves through the air. 
Based on the understanding of the orientation and position, the transformation between the two coordinate systems is 
described by Euler angles (roll angleφ, pitch angle θ, yaw angle ψ). The transformation matrix R is as follows:
R = 
⎡
⎣
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢⎢⎢⎢⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎤
⎦
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥⎥⎥⎥⎥
⎥
⎥
⎥
⎥
⎥
⎥
cosψcosθ
cosψsinθsinϕ - sinψcosϕ
cosψsinθcosϕ + sinψcosϕ
sinψcosθ
sinψsinθsinϕ + cosψcosϕ
sinψsinθcosϕ - cosψsinϕ
-sinθ
cosψsinθ
cosθcosϕ
2.2　Kinematic model
2.2.1　Three setps
1) Set the quadrotor UAV as an axisymmetric rigid body. 2) Set the centre of gravity of the quadrotor unmanned aerial 
vehicle to coincide with the geometric center of the unmanned aerial vehicle. 3) Set the air resistance experienced by the 
unmanned aerial vehicle during flight is ignored, and the gravitational force does not change during flight. The motion of 
the UAV during flight can be regarded as the superposition of translation and rotation.
2.2.2　According to the newton-euler equations, the translational kinematic equation of the quadrotor 
unmanned aerial vehicle can be obtained
m ξ = Fg + R Ft
..
2.2.3　Rotational dynamics
Jω+ ω × Jω = τ + τg
Where J = diag(Jx, Jy, Jz ) is the moment of inertia matrix, ω = [p,q r]
T is the angular velocity vector, τ =[U1,U2, U3]
T is the 
control moment, and τgis gyroscopic torque.
The drone control input is defined as:
⎧
⎨
⎩
⎪
⎪
⎪
⎪⎪⎪⎪⎪⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪⎪⎪⎪⎪
⎪
⎪
⎪
U1 = b(Ω2
1 + Ω2
2 + Ω2
3 + Ω2
4 )
U2 = bl(Ω2
2 −Ω2
4 )
U3 = bl(Ω2
3 −Ω2
1 )
U4 = d(Ω2
1 −Ω2
2 + Ω2
3 −Ω2
4 )
Where l is the arm length and d is anti-torsional stiffness.
2.2.4　Kinematic model
The relationship between the attitude angles and angular velocities is described by the kinematic equation:
⎡
⎣
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢⎢⎢⎢⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢⎤
⎦
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥⎥⎥⎥⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
ϕ
θ
ψ
= 
⎡
⎣
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢⎢⎢⎢⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎤
⎦
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥⎥⎥⎥⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
1
sinϕtanθ
cosϕtanθ
0
cosϕ
-sinϕ
0
sinϕ cosθ
cosϕ cosθ
⎡
⎣
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢⎢⎢⎢⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢⎤
⎦
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥⎥⎥⎥⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
p
q
r
2.2.5　Linearization model
Small perturbation linearization near the hovering equilibrium point. a simplified linearised model can be obtained by 
assuming that the attitude angles and angular velocity are small, and the corresponding transfer function can be 
simplified as follows:
⎧
⎨
⎩
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪⎪⎪⎪⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪⎪⎪⎪⎪
⎪
⎪
⎪
⎪
⎪
⎪
Gϕ( )s = Φ(s)
U2 (s) = 1
Jxs2
Gθ( )s = Θ(s)
U3 (s) = 1
Jys2
Gψ( )s = Ψ(s)
U4 (s) = 1
Jzs2
3　Controller design
This design primarily comprises the series PID controller and the fuzzy controller. Comprising two interlinked PID 
controllers, the series PID controller features an inner loop for attitude control, regulating the unmanned aerial vehicle's 
101

## Page 3

Deng Xin
angular speed, and an outer loop for controlling the quadcopter UAV's flight angle. The primary components of the fuzzy 
controller are the angular velocity error e and the error rate change ec. The fuzzy controller also manages the trio of 
parameters: Kp, Ki, and Kd. The design phase of the controller adheres to the previously stated core principles.
3.1　Structure of the cascade PID controller
Outer loop controller (angle control):
uout = Kp,oute∠+ Ki,out∫e∠dt + Kd,out deω
dt
Inner loop controller (angular velocity control):
uin = Kp,ineω + Ki,in∫eωdt + Kd,in deω
dt
Where e∠ is angle error and eωis Angular velocity error.
3.2　Design of fuzzy controller
To improve the ability of the cascade PID controller to adapt, which is to say, to adjust itself to changing conditions, a 
fuzzy controller is added into the inner loop. This fuzzy controller, as it happens, takes in two main inputs: one is the 
angular velocity error, which we can call e, and the other is the rate of change of this error, which is referred to as ec. Now, 
based on these inputs, the fuzzy controller will produce an output, which is not just any output, but rather the amount by 
which the PID parameters should be adjusted, specifically ΔKp, ΔKi, and ΔKd. In essence, it is about modifying these 
parameters in real time, which means that adjustments happen as conditions change, which is, of course, quite crucial for 
maintaining effective control. This whole process, with its various components, aims to ensure that the controller remains 
responsive to the dynamics of the system it is meant to control, thereby enhancing overall performance.
The fuzzy sets, which are to be considered for the input variables, are defined in a certain way that includes categories 
such as NB, which stands for negative large, and NM, which means negative medium, and there is also NS for negative 
small. Then, we have ZO, representing zero, and moving on, PS indicates positive small, PM signifies positive medium, and 
finally, PB stands for positive large. The error, which is denoted as e, is confined within the range of values from negative 
three to positive three, and similarly, the rate at which this error changes, labelled ec, also lies within the same interval [−3,
3]. The outputs are ΔKp, ΔKi, and ΔKd, which are respectively defined in the domain [−0.3,0.3], [−0.06,0.06], and [−3,3]. 
Based on expert experience and system characteristics, fuzzy control rules are formulated. Taking ΔKp as an example, the 
fuzzy rule table is as follows:
Similarly, a fuzzy rule table for ΔKi and ΔKd can be established.
4　Simulation analysis
4.1　Simulation environment and parameter settings
A four-rotor unmanned aerial vehicle attitude control simulation system was built in the MATLAB/Simulink 
environment. The simulation parameters are set as follows: mass of the four-rotor unmanned aerial vehicle: m = 2.0 kg, 
length of the rotor arm: l = 0.2 m, rotational inertia: jx = jy = 1.25 × 10⁻² kg·m², jz = 2.5 × 10⁻² kg·m², lift coefficient: b = 3.13 
× 10⁻⁵ n·s², anti-torque coefficient: d = 7.5 × 10⁻⁷ n·m·s², simulation time: 10 s, sampling time: 0.01 s.
The initial parameters of the cascade PID controller were obtained by the Ziegler-Nichols method:
Table 1　Improved fuzzy rule table
eω ec
NB
NM
NS
ZO
PS
PM
PB
NB
PB
PB
PM
PM
PS
PS
ZO
NM
PB
PB
PM
PM
PS
ZO
ZO
NS
PM
PM
PM
PS
ZO
NS
NM
ZO
PS
PS
ZO
NS
NS
NM
NM
PS
PS
PS
ZO
NS
NS
NM
NM
PM
ZO
ZO
NS
NM
NM
NM
NB
PB
ZO
NS
NS
NM
NM
NB
NB
Table 2　Initial parameters using the Ziegler-Nichols method
Parameters
Outer loop
Inner loop
Kp
4.5
1.5
Ki
0.5
0.1
Kd
2.0
0.5
102

## Page 4

Theory and Practice of Science and Technology
4.2　Step response comparison
(1) Faster response speed: The rise time has decreased from 0.45 seconds to 0.35 seconds, an increase of 22.2%.
(2) Smaller overshoot: The overshoot has reduced from 16.0% to 5.0%, a decrease of 68.8%.
(3)Shorter stabilisation time: The time to reach the steady state value is approximately 1.5 seconds, while the 
traditional method requires 2.5 seconds.
4.3　Analysis of anti-interference performance
To test the anti-interference capability of the controller, an external disturbance was applied at t = 5s, and the response 
and recovery of the system were observed.
Disturbance suppression ability: The maximum deviation of the fuzzy cascade PID is 0.119 rad, while that of the 
traditional cascade PID is 0.238 rad. The anti-interference performance has improved by 50.0%.
Recovery speed: The fuzzy cascade PID can return to the steady state within 1.5s, while the traditional method requires 
approximately 2.5s.
Steady-state accuracy: Both methods can eventually reach the expected value, but the fluctuations of the fuzzy 
cascade PID are smaller.
4.4　Tracking performance
Tracking Accuracy: The root mean square error (RMSE) of the fuzzy cascade PID is 0.0234 rad, while that of the 
traditional method is 0.0712 rad, indicating an accuracy improvement of 67.2%.
Phase Delay: The phase lag of the fuzzy cascade PID is significantly less than that of the traditional method, resulting in 
a faster dynamic response.
Amplitude Maintenance: The fuzzy cascade PID can better maintain the amplitude of the desired trajectory, with less 
attenuation.
5　Conclusion
A prototype of the quadrotor unmanned aerial vehicle was created, a cascade PID controller was developed, and its 
efficiency was enhanced, drawing on the vehicle's multi-input and underactuated features. By integrating a fuzzy 
Figure 1　Comparison of Anti-interference Performance
Figure 2　Comparison of tracking and error
103

## Page 5

Deng Xin
controller into the inner loop, a fuzzy self-tuning controller was created. The traditional fuzzy rules underwent correction 
and enhancement based on the compilation guidelines of fuzzy rules. A simulation analysis was performed using a 
Simulink control system, which was then compared and examined alongside the cascade PID control system and the 
cascade fuzzy PID control system to assess disturbance rejection. Analytical simulaions of this control mechanism reveal 
that the unmanned aerial vehicle, equipped with an enhanced cascade fuzzy PID control system, exhibits greater stability 
in attitude control, minimal overshoot in attitude angles, and a reduced stabilization duration. In contrast to the cascade 
PID control system, this system offers a more effective control in every aspect and greater adaptability.
Additionally, the enhanced system's resilience to different external disruptions and fluctuating flight scenarios has 
been confirmed across various testing situations. The findings reveal an improvement in both the stability and the 
accuracy of following preferred flight trajectories. This system maintains a low response time, even under difficult 
conditions, underscoring its efficiency in practical scenarios. Subsequent efforts will concentrate on incorporating 
sophisticated machine learning techniques to enhance real-time control parameter optimization, aiming for increased 
adaptability and efficiency in varied operational scenarios.
6　Discussion
During the process of conducting research, it was noted that there were many limitations and restrictions that were 
imposed when it came to the modelling of the unmanned aerial vehicle, commonly referred to as a UAV. There were 
indeed several factors that could potentially influence the stability of the posture of the UAV, but these factors were not 
analysed in a deep or thorough manner. It is quite possible that in future studies or research endeavours, these relevant 
influencing factors can be included for further analysis, which could potentially lead to achieving better control results. 
This idea of including more factors seems reasonable, as it might help improve understanding and effectiveness. 
However, the previous research did not delve deeply enough into these aspects, which may have led to some gaps in the 
findings. Thus, one might say that a more comprehensive approach in future explorations could get better outcomes. This 
consideration is important, and it may open new avenues for research that could be beneficial in the long run.
References
[1] Cukdar, I., Yigit, T., & Celik, H. Balance control of brushless direct current motor driven two-rotor UAV. Applied Sciences, 2024, 14(10), 4059.
[2] Xu G, Zhou M. Modified adaptive flight control of quadrotor based on single neuron PID; proceedings of the 2013 IEEE Third International 
Conference on Information Science and Technology (ICIST), F 23-25 March 2013, 2013.
[3] Zhang Y, Chen Z, Zhang X, et al. Tandem-level linear self-anti-disturbance control of a dual-rotor UAV. Journal of Central South University 
(Natural Science Edition), 2019, 50(3): 564-71.
[4] Le Q, Hou S and Hou Y. Self-tuning of parameters for quadrotor unmanned aerial vehicle based on improved DBO. Information Technology 
and Informatization, 2025, (1): 175-178.
[5] D K, A M and B A. Attitude Optimal Backstepping Controller Based Quaternion for a UAV . Mathematical Problems in Engineering, 2016, 2016: 
1-11.
[6] N. Wanore Madebo, C. Merga Abdissa and L. Negash Lemma, "Enhanced Trajectory Control of Quadrotor UAV Using Fuzzy PID Based Recurrent 
Neural Network Controller," in IEEE Access, vol. 12, pp. 190454-190469, 2024.
[7] He, Z., Gao, W., He, X., Wang, M., Liu, Y., Song, Y., & An, Z. Fuzzy intelligent control method for improving flight attitude stability of plant 
protection quadrotor UAV. International Journal of Agricultural and Biological Engineering, 2019, 12(6), 110-115.
[8] K. Jia, S. Lin, Y. Du, C. Zou and M. Lu, "Research on Route Tracking Controller of Quadrotor UAV Based on Fuzzy Logic and RBF Neural Network," 
in IEEE Access, vol. 11, pp. 111433-111447, 2023.
[9] Melo, A. G., Andrade, F. A., Guedes, I. P., Carvalho, G. F., Zachi, A. R. L., & Pinto, M. F. Fuzzy gain-scheduling PID for UAV position and altitude 
controllers,pp.2173. 2022.
[10] Dong, J., & He, B. Novel fuzzy PID-type iterative learning control for quadrotor UAV.[OL]. 2019. https://doi-org-s-225.libdb.csu.edu.cn/10.3390/
s19010024.
[11] Andrade, F. A. A., Guedes, I. P., Carvalho, G. F., Zachi, A. R. L., Haddad, D. B., Almeida, L. F., Pinto, M. F. Unmanned aerial vehicles motion control 
with fuzzy tuning of cascaded-PID gains. [OL]. 2022. https://doi-org-s-225.libdb.csu.edu.cn/10.3390/machines10010012.
[12] Zhang Ze-jing, Zhang Shu-guang, Liu Xu, et al. Safety target level prediction method for unmanned aircraft systems. Journal of 
Aerodynamics, 2018, 33(4): 1017-24.
[13] Chen Long-sheng, Ning Xiao-ming. Nonlinear PI tandem attitude control for quadrotor UAV with preset performance. Journal of Applied 
Sciences, 2019, 37(1): 137-50.
[14] Xiamen University, 2018. Li Jia-hao. Improvement of self-turbulence control and its application on quadrotor UAV; [D]. Xiamen University, 
2018.
104
