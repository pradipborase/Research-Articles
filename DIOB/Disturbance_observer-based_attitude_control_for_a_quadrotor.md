# Disturbance_observer-based_attitude_control_for_a_quadrotor.pdf

## Page 1

Disturbance Observer-based Attitude Control for a 
Quadrotor  
 
Yongsheng Zhao, Yabo Cao, Yunsheng Fan 
School of Information Science and Technology 
Dalian Maritime University 
Dalian 116026, China 
yszhao@dlmu.edu.cn; caoyabo2011@foxmail.com; yunsheng@dlmu.edu.cn 
 
 
Abstract—This paper gives an disturbance observer-based 
attitude control method of a quadrotor Unmanned Aerial Vehicle 
(UAV) in the presence of large disturbance. Based on linear PID 
controller a disturbance observer is designed to estimate and 
compensate for the impact of internal/external disturbance 
simultaneously. After the disturbance observer is added, the 
attitude subsystem can overcome the strong coupling and 
external disturbance. Simulation results show that the controller 
is simple and effective which is able to ensure the stability of 
attitude and has strong robustness to disturbance. 
Keywords—QBall2 Quadrotor; Disturbance Observer; Attitude 
Control; PID Control 
I.  INTRODUCTION  
In recent years, because the quadrotor unmanned UAV has 
the characteristics of vertical take-off and landing, freedom to 
hover, simple structure, its application in the field of military, 
civil and scientific research is more and more widely. This 
trend is also partly due to the integration and application on 
UAV platforms of high performance processors, sensors and 
micro electro mechanical systems devices with lower and 
lower power consumption, which promote the development of 
quadrotor UAV [1]. To ensure that the quadrotor has good 
flying quality in a variety of flight conditions, good flight 
control is necessary in addition to good hardware equipment. 
So that reliable and stable flight control algorithm is very 
important. And for a quadrotor the attitude control is the basis 
which is one of the key technologies [2, 3]. As quadrotor is a 
strong coupling, multivariable, underactuated nonlinear system 
that has six degree of freedom ouputs and four inputs, its flight 
control also has received wide attention of researchers both at 
home and abroad. And at present all kinds of control 
algorithms are widely used in quadrotor attitude control, such 
as 
PID[4], 
LQR[5] 
linear 
control 
algorithm, 
feedback 
linearization[6], backstepping[7], sliding mode variable structure 
control[8] nonlinear control algorithm, and adaptive[9], H-
infinity control[10], fuzz control[11] and so on. Disturbance and 
uncertainty rejection is a key objective in flight control system 
design. Some of these control approach mentioned above 
generally achieve the goal of disturbance rejection via feedback 
regulation based on the tracking error between the measured 
outputs and their set points.  Thus, designed controllers cannot 
react directly and fast enough in the presence of strong 
disturbances relative to the feedforward control. However, 
quite often, the external disturbance cannot be directly 
measured or is too expensive to measure [12]. So an active 
disturbance-rejection controller for the flight control was given 
in [13] which designed an extended state observer to estimate 
and compensate for the impact of disturbance. However, the 
controller has too many parameters to adjust which is a little 
complicated. As one of the most effective and popular 
disturbance estimation techniques disturbances observer has 
attracted a lot of interest and disturbance observer-based 
control (DOBC) has received a great deal of attention which is 
applied in this paper. For the attitude stabilization problem of a 
quadrotor, a classical linear PID is used as the basic controller. 
And on this basis, the output of the PID controller is combined 
with a disturbance observer to estimate equivalent input 
disturbance in the system. With not join disturbance observer, a 
disturbance observer-based control is verified, tested the 
perturbation resistance of the system and robustness.  
II. DYNAMIC MODEL OF QBALL2 QUADROTOR 
A quadrotor is a highly nonlinear, strong coupling of 
multiple inputs multiple outputs of complex nonlinear systems. 
 
Fig. 1. The QBall2 quadrotor UAV . 
This work was supported in part by National Natural Science Foundation 
of China under Grant 51609033, Natural Science Foundation of Liaoning
Province under Grant 2015020022, and Fundamental Research Funds for the
Central Universities under Grant 3132016312. 
2017 4th International Conference on Information, Cybernetics
and Computational Social Systems (ICCSS)
978-1-5386-3257-4/17/$31.00 © 2017 IEEE
355
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 13:26:52 UTC from IEEE Xplore.  Restrictions apply.

## Page 2

This paper is studied based on QBall2 quadrotor as shown 
in Fig. 1. The body axes coordinate system and the earth 
coordinate system of QBall2 are denoted  (
)
, ,
x y z
 and 
(
)
, ,
X Y Z
 respectively. And the attitude of quadrotor is 
described using Euler angle. φ  is roll angle and θ  is pitch 
angle and ψ  is yaw angle, which are defined as the angles of 
rotation about the x, y and z axis, respectively. 
The mathematical model of QBall2 quadrotor is shown as 
(1) according to Newton-Euler formalism [14]. 
(
)
(
)
(
)
(
)
(
)
(
)
1
1
1
2
3
4
cos sin
cos
sin
sin
/
cos sin
sin
sin
cos
/
cos cos
/
/
/
/
y
z
x
z
x
y
x
y
z
x
U
m
y
U
m
z
U
m
g
U
I
I
d
I
U
I
I
d
I
U
I
I
d
I
φ
θ
ψ
φ
θ
ψ
φ
ψ
φ
θ
ψ
φ
ψ
φ
θ
φ
θψ
θ
φψ
ψ
φθ
Γ
Γ
Γ
=
+





= −
−






=
−








=
+
−
+






=
+
−
+






=
+
−
+













 (1) 
where m is the total mass of quadrotor; g is the acceleration of 
gravity; 
,
,
x
y
z
I
I
I are the moment of inertia about the x-axis, y-
axis, z-axis respectively. 
1
2
3
4
,
,
,
U U U U are the virtual control 
inputs of quadrotor and  
1
U
denotes the total lift of a 
quadrotors and 
2
3
4
,
,
U U U  denote roll, pitch, yaw moment 
respectively.  
The mathematical model of the quadrotor can be divided 
into position subsystem and attitude subsystem. This paper 
mainly studies the control problem of attitude angle under the 
condition of disturbance exists. And for the attitude subsystem 
in (1) 
=
,
,
d
d
d
d
φ
θ
ψ
Γ
Γ
Γ
Γ



 denotes attitude disturbance 
torque, on behalf of the airflow disturbance torque of quadrotor 
and they have no clear model information which belongs to the 
structural interference, but are slowly time-varying bounded 
signal. 
The thrust 
iT  and un-torque 
i
Q  generated by th
i
 rotor 
have the following approximate relationship with th
i
 motor’s 
control input signal 
iu  as shown in (2) 
,
, (
1,2,3,4)
i
t
i
i
y
i
T
K
u Q
K
u
i
s
s
ω
ω
ω
ω
=
=
=
+
+
  (2) 
where 
t
K  and 
y
K
 are positive gains which denote thrust 
coefficient and un-torque coefficient respectively. ω  is the 
motor bandwidth and 
iu  is the PWM control input of th
i
 
motor which is limited between 0-1. 
And the virtual control inputs of a quadrotor have the 
following relationship with the thrust and un-torque generated 
by rotors as shown in equation (3) where l is the distance 
between the center of a rotor and the quadrotor. 
(
)
(
)
4
1
2
1
2
3
1
2
4
1
2
3
4
i
i
U
T
U
T
T
l
U
T
T
l
U
Q
Q
Q
Q

=


=
−


=
−


=
−
+
−


                       (3) 
III. DISTURBACNCE OBSERVER-BASED ATTITUDE CONTROL 
DESIGN 
A. Disturbance Observer Design 
For roll angle subsystem shown in (4) 
(
)
2
x
y
z
I
I
I
U
d
d
φ
φ
φ
θψ
Γ
=
−
+
+
+



          (4) 
where part of the uncertainty of roll angle system model d φ
 is 
considered and is combined with disturbance torque d φ
Γ  as 
the total disturbance dφ  of roll angle as shown in (5). 
d
d
d
φ
φ
φ
Γ
=
+
                                 (5) 
So equation (4) can be rewritten in 
(
)
2
/
y
z
x
I
I
U
d
I
φ
φ
θψ


=
−
+
+




             (6) 
Then rewrite (6) in the form of affine nonlinear system 
1
2
( )
( )
( )
x
f x
g x u
g
x d
=
+
+
                 (7) 
So equation (6) can be rewritten in 
(
)
2
1
1
y
z
x
x
x
I
I
U
d
I
I
I
φ
θψ
φ
−
=
+
+


            (8) 
To estimate the disturbance, a nonlinear disturbance 
observer is depicted by the following equation. 
( )
( )
( )
( )
( )
( )
2
2
1
( )
ˆ
( )
z
l x g
x z
l x
g
x p x
f x
g
x u
d
z
p x
= −
−

+
+






=
+


       (9) 
And the nonlinear distance observer gain ( )
l x
  is 
determined by: 
( )
( )
p x
l x
x
∂
=
∂
                              (10) 
2017 4th International Conference on Information, Cybernetics
and Computational Social Systems (ICCSS)
978-1-5386-3257-4/17/$31.00 © 2017 IEEE
356
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 13:26:52 UTC from IEEE Xplore.  Restrictions apply.

## Page 3

So the disturbance observer of roll angle is show as 
equation (11). 
(
)
2
( )
/
( )
( )
/
ˆ
( )
( )
( )
x
y
z
x
z
l x
z I
l x
p x
I
I
U
I
d
z
p x
p x
l x
θψ
φ
= −
∗
−



∗
+
−
+




=
+

=
∗



      (11) 
The disturbance estimation error is defined as. 
ˆ
de
d
d
=
−
                                 (12) 
And assuming that disturbance is slowly time-varying 
signal. 
0
d =

                                      (13) 
So the derivative of (12) is 
ˆ
de
d
d
=
−


                                  (14) 
Combing (13) and (14): 
(
)
(
)
2
=0
( )
( )
( )
/
( ) [ ( )
]/
( )
d
x
y
z
x
e
z
p x
z
l x
l x
z I
l x
p x
I
I
U
I
l x
φ
θψ
φ
−
+
= −−
∗
=
∗
+
∗
+
−
+
−
∗







(15) 
Replacing φ by (8) 
(
)
(
)
(
)
(
)
2
2
2
2
( ) /
( )
( )
/
1
1
( )
= ( )
( ) /
( )
/
( )[
(
1
)
]/
( )
ˆ
= ( )
/
( )
/
( )
/
d
x
y
z
x
y
z
x
x
x
x
x
y
y
z
z
x
x
x
x
x
d
x
e
l x z I
l x
p x
I
I
U
I
I
I
l x
U
d
I
I
I
l x
z
p x
I
l x d
I
l x
I
I
I
I
U
I
l x
U
I
I
l x d I
l x d
I
l x e
I
θψ
θψ
θψ
θψ


=
+
+
−
+




−


−
+
+




+
−
+
−


−


+
−
+




−
= −





(16) 
Which implies that the disturbance estimation error will 
converge to zero as time goes to infinity if the observer gain  
( )
l x  is chosen such that system (16) is asymptotically stable. 
B. Controller Input Design 
For the basic attitude control, a PID controller is used for 
roll angle and pitch angle. Due to the weak control torque of 
yaw and usually not very strict for yaw, a PD controller is used 
for yaw angle control. The control signals combined with 
estimated disturbance are given to four motor as shown in 
equation (17). 
1
2
3
4
_
_
_
_
_
_
_
_
_
_
_
_
u
u
throttle
u
pitch
u
yaw
u
u
throttle
u
pitch
u
yaw
u
u
throttle
u
roll
u
yaw
u
u
throttle
u
roll
u
yaw
=
+
−


=
−
−

=
+
+


=
−
+

       (17) 
where u_throttle is throttle control signal; u_roll is roll angle 
control signal; u_pitch is pitch angle control signal; u_yaw is 
yaw angle control signal. 
IV. SIMULATION AND RESULTS 
The observer disturbance-based attitude control structure is 
as shown in Fig. 2. 
 
Fig. 2. The control system structure block diagram of QBall2. 
where 
,
,
d
d
d
φ θ ψ
 are desired attitude angle; d is the 
disturbance for the QBall2 quadrotor and ˆ
ˆ
ˆ
,
,
d
d
d
φ
θ
ψ  are the 
disturbance estimated by disturbance observer. And the model 
parameters of QBall2 quadrotor are shown in Table 1. 
TABLE I.  
MODEL PARAMETERS OF QBALL2 
Symbol 
Value 
m 
1.80kg 
l 
0.20m 
w 
15rad/s 
Ix, 
0.03kg*m^2 
Iy 
0.03kg*m^2 
Iz 
0.04kg*m^2 
Kt 
8.80N 
Ky 
0.40N 
g 
9.81m/(s^2) 
 
The simulation time is set to 100s, assuming that quadrotor 
take off first then desired attitude is given at 15s. And in the 
20s disturbance is given which is slowly time-varying 
2017 4th International Conference on Information, Cybernetics
and Computational Social Systems (ICCSS)
978-1-5386-3257-4/17/$31.00 © 2017 IEEE
357
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 13:26:52 UTC from IEEE Xplore.  Restrictions apply.

## Page 4

aerodynamic interference torque and some system uncertainty 
is included in as shown in equation (18). The observer gains 
( )
l x  are chosen as 
[
]
( )
0.1,0.1,1
l x =
 and disturbance are 
chosen as 
[
,
,
]
[0.1sin(0.1
)
0.1,0.1cos(0.1
)
0.1,
0.01sin(0.1
)
0.02]
d
d
d
d
t
t
t
φ
θ
ψ
π
π
π
=
=
+
+
+
  (18) 
The simulation results are shown in the following. 
0
10
20
30
40
50
60
70
80
90
100
0
1
2
3
4
5
6
7
8
9
t(s)
roll(degree)
 
 
RollDOBC
Roll
 
Fig. 3. Roll angle output. 
0
10
20
30
40
50
60
70
80
90
100
-0.1
-0.05
0
0.05
0.1
0.15
0.2
0.25
t(s)
PWM
 
 
RollDOBCControl
RollControl
 
Fig. 4. Roll angle control input signal. 
 
0
10
20
30
40
50
60
70
80
90
100
0
1
2
3
4
5
6
7
8
9
10
t(s)
pitch(degree)
 
 
PitchDOBC
Pitch
 
Fig. 5. Pitch angle output. 
0
10
20
30
40
50
60
70
80
90
100
-0.15
-0.1
-0.05
0
0.05
0.1
0.15
0.2
0.25
t(s)
PWM
 
 
PitchControlDOBC
PitchControl
 
Fig. 6. Pitch angle control input signal. 
0
10
20
30
40
50
60
70
80
90
100
0
1
2
3
4
5
6
7
8
t(s)
yaw(degree)
 
 
YawDOBC
Yaw
 
Fig. 7. Yaw angle output. 
2017 4th International Conference on Information, Cybernetics
and Computational Social Systems (ICCSS)
978-1-5386-3257-4/17/$31.00 © 2017 IEEE
358
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 13:26:52 UTC from IEEE Xplore.  Restrictions apply.

## Page 5

0
10
20
30
40
50
60
70
80
90
100
-0.06
-0.04
-0.02
0
0.02
0.04
0.06
t(s)
PWM
 
 
YawControlDOBC
YawControl
 
Fig. 8. Yaw angle control input signal. 
Fig. 3 to Fig. 8 show that disturbance observer-based 
attitude control has better robustness  and need nearly the same 
control input signal than traditional PID controller. 
0
10
20
30
40
50
60
70
80
90
100
-0.02
-0.01
0
0.01
0.02
0.03
0.04
0.05
0.06
t(s)
disturb(rad/s2)
 
 
Rolldisturb
Pitchdisturb
Yawdisturb
 
Fig. 9. Disturbacne observered by disturbance obeserver. 
Fig. 9 shows that the disturbance observer designed has a 
good performance to estimate the system disturbance. 
White noise is added to the attitude angles of quadrotor to 
represent internal disturbance which caused by sensors noise. 
0
10
20
30
40
50
60
70
80
90
100
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
9
t(s)
roll(degree)
 
 
RollDOBC
Roll
 
Fig. 10. Roll angle output with sensors noise. 
0
10
20
30
40
50
60
70
80
90
100
-2
0
2
4
6
8
10
12
t(s)
pitch(degree)
 
 
PitchDOBC
Pitch
 
Fig. 11. Pitch angle output with sensors noise. 
0
10
20
30
40
50
60
70
80
90
100
-2
0
2
4
6
8
10
t(s)
yaw(degree)
 
 
YawDOBC
Yaw
 
Fig. 12. Yaw anglewith sensors noise. 
2017 4th International Conference on Information, Cybernetics
and Computational Social Systems (ICCSS)
978-1-5386-3257-4/17/$31.00 © 2017 IEEE
359
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 13:26:52 UTC from IEEE Xplore.  Restrictions apply.

## Page 6

Fig.10. to Fig. 12. show that the disturbance observer-based 
attitude control can still has a good robustness in the case of the 
high frequency oscillation disturbance cause by the vibration of 
the quadrotor flight.. 
V. CONCLUSIONS 
For underactuated quadrotor a nonlinear disturbance 
observer is designed in this paper which make attitude 
subsystem fast track command signal, and overcome the 
aerodynamic disturbance torque and model parameter 
uncertainty. Theoretical analysis and simulation results show 
that the designed controller can improve the anti-interference 
ability of the flight control system, and disturbance observer-
based control method can enhance the robustness and does not 
need to change the existing controller structure only require the 
system to control input and system output to estimate the 
equivalent interference which is simple and convenient, has 
extensive adaptability.  
ACKNOWLEDGMENT 
This work is partially supported by National Natural 
Science Foundation (NNSF) of China under Grant 51609033, 
Natural Science Foundation of Liaoning Province under Grant 
2015020022, and Fundamental Research Funds for the Central 
Universities under Grant 3132016312. The authors also 
gratefully acknowledge the helpful comments and suggestions 
of the reviewers, which have improved the presentation. 
REFERENCES 
[1]  P. Daponte, L. De Vito, G. Mazzilli, F. Picariello, S. Rapuano, and M. 
Riccio, "Metrology for drone and drone for metrology: measurement 
systems on small civilian drones," in Metrology for Aerospace, 2015, 
pp. 306-311. 
[2]  J. Yue, Q. Zhang, and H. Zhu, Research Progress and Key Technologies 
of Micro Quad-Rotor UAVa, ElectronicsOptics & Control, 10, pp. 46-52, 
2010. 
[3]  H. Zheng, X. Qi, M. Xia, and H. Zhao, Survey of flight control 
technology for quad-rotor unmanned helicopter, Flight Dynamics, 04, pp. 
295-299, 2012. 
[4]  A. L. Salih, M. Moghavvemi, H. A. F. Mohamed, and K. S. Gaeid, 
"Modelling and PID controller design for a quadrotor unmanned air 
vehicle," in IEEE International Conference on Automation, Quality and 
Testing, Robotics, Cluj-Napoca, Romania, 2010, pp. 1-5. 
[5]  S. Bouabdallah, A. Noth, and R. Siegwart, "PID vs LQ control 
techniques applied to an indoor micro quadrotor," in IEEE/RSJ 
International Conference on Intelligent Robots and Systems, Sendai, 
Japan, 2004, pp. 2451-2456. 
[6]  E. Altug, J. P. Ostrowski, and R. Mahony, "Control of a quadrotor 
helicopter using visual feedback," in Proceedings of the 2002 IEEE 
International Conference on Robotics and Automation, Washington, DC, 
USA, 2002, pp. 72-77. 
[7] T. Madani, A. Benallegue, "Backstepping control for a quadrotor 
helicopter," in IEEE/RSJ International Conference on Intelligent Robots 
and Systems, Beijing, PEOPLES R CHINA, 2006, pp. 3255-3260. 
[8]  Z. Xu, SMC Based Wind Disturbance Rejection for Quad-Rotor UAVs, 
Electronics Optics & Control, 01, pp. 67-71, 2017. 
[9]  G. Antonelli, F. Arrichiello, and S. Chiaverini, "Adaptive trajectory 
tracking for quadrotor MAVs in presence of parameter uncertainties and 
external disturbances," in IEEE/ASME International Conference on 
Advanced Intelligent Mechatronics, Wollongong, Australia, 2013. 
[10] G. V. Raffo, M. G. Ortega, and F. R. Rubio, An integral 
predictive/nonlinear H(infinity) control structure for a quadrotor 
helicopter, AUTOMATICA, vol. 46, no. 1, pp. 29-39, 2010. 
[11] I. Ilhan, M. Karakose, "Type-2 Fuzzy Based Quadrotor Control 
Approach," in 9th Asian Control Conference (ASCC), Istanbul, 
TURKEY, 2013, pp. 1-6. 
[12] W. Chen, J. Yang, L. Guo, and S. Li, Disturbance-Observer-Based 
Control and Related Methods-An Overview, IEEE Transactions on 
Industrial Electronics, vol. 63, no. 2, pp. 1083-1095, 2016. 
[13] Y. Liu, S. Yang, and W. Wang, An active disturbance-rejection flight 
control method for quad-rotor unmanned aerial vehicles, Control Theory 
& Applications, 10, pp. 1351-1360, 2015. 
[14] S. Bouabdallah, R. Siegwart, "Full control of a quadrotor," in IEEE/RSJ 
International Conference on Intelligent Robots and Systems, San Diego, 
CA, 2007, pp. 153-158. 
[15] L. Yang, J. Liu, Disturbance observer-based robust trajectory tracking 
control for a quadrotor UAV, Flight Dynamics, vol. 33, no. 4, pp. 328-
333, 2015. 
[16] W. Chen, Disturbance observer based control for nonlinear systems, vol. 
9, no. 4, pp. 706 - 710, 2004. 
 
 
2017 4th International Conference on Information, Cybernetics
and Computational Social Systems (ICCSS)
978-1-5386-3257-4/17/$31.00 © 2017 IEEE
360
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 13:26:52 UTC from IEEE Xplore.  Restrictions apply.
