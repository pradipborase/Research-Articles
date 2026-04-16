# Robust_Cascaded_PID_Disturbance_Observer-Based_Control_of_an_Unmanned_Quadrotor_Aerial_Vehicle.pdf

## Page 1

Robust cascaded PID disturbance observer-based control of an unmanned
quadrotor aerial vehicle
Mohammed Hany
Mohamed Elsayd
Ayman El-Badawy
Mechatronics Engineering Department
Mechatronics Engineering Department
Mechatronics Engineering Department
German University in Cairo
German University in Cairo
German University in Cairo
mohammed.hany@student.guc.edu.eg
mohamed.ramadan@student.guc.edu.eg
ayman.elbadawy@guc.edu.eg
Abstract—A disturbance observer (DOB) is incorporated into
a cascaded PID control framework for a quadrotor unmanned
aerial vehicle (UAV) to improve trajectory tracking under ex-
ternal disturbances. While the cascaded PID structure offers
simplicity of implementation, it lacks robustness against time-
varying disturbances. To address this, the system is linearized at
selected operating points for DOB design, and the robust stability
of the Q-filter is verified using the small-gain theorem. Simulation
studies with trajectories subject to Dryden wind disturbances
demonstrate that the DOB-enhanced controller achieves superior
tracking accuracy compared to the conventional cascaded PID
controller achieving reductions in position standard deviation
of 26.47%, 39.5%, and 59.7% along the X, Y, and Z axes,
respectively.
Index Terms—UAV, Quadrotor, cascaded PID, disturbance
observer
I. INTRODUCTION
Unmanned Aerial Vehicles (UAVs) have attracted the at-
tention of many researchers for the past two decades. Ad-
vancements in micro-controllers, sensors and power storing
devices lead to the manufacturing of different types of UAVs
[1]. The multi-rotor quadcopter was chosen due to its easier
controllability and maneuverability, low price and portability
[2]. Quadrotors are widely used in different fields such as dis-
aster management, data collection Internet of Things(IOT) [3],
remote sensing, mapping [4], search and rescue, construction
and infrastructure inspection, precision agriculture, delivery of
goods and real-time monitoring of road traffic [5].
Unfortunately, UAVs represent an unstable coupled system,
thus, researchers are interested in designing control systems
that enable a UAV to follow a specified trajectory with
minimal tracking errors. These controllers include Feedback
Linearization Control [6], Sliding Mode Control (SMC) [7],
Backstepping control [8], PID control [9], Model Predictive
Control (MPC) [10], Linear Quadratic Regulator (LQR) [11],
Adaptive control [12] and H∞control [13].
Disturbance rejection is one of the most important goals
when designing control systems. There are two types of
disturbances: external disturbances caused by the environment
like wind disturbances and input signal fluctuations [14], and
internal disturbances caused by uncertainties like modeling
errors, parameter changes and sensor noise [15]. There are
many different techniques for disturbance rejection. One of
these techniques is using a disturbance observer (DOB).
Several papers were written using DOBs in UAV systems.
In [16] a time domain DOB-based controller is applied to a
quadrotor unmanned aerial vehicle, for [17] a linear dual DOB
is used for disturbance rejection for a quadrotor UAV, while
in [18] a DOB designed using the H∞synthesis techniques
is used for disturbance rejection for a hybrid VTOL UAV,
for [19] a finite-time disturbance observer combined with
a sliding mode controller is used for disturbance rejection
for a quadrotor UAV and in [20] a backstepping disturbance
observer based controller is designed for trajectory tracking
for a multi rotor UAV using two DOBs to estimate force and
torque disturbances.
Although DOB-based control has been explored using time-
domain and H∞techniques, existing literature validates these
methods against simplified disturbances (e.g., step or sinu-
soidal inputs). This work addresses a gap by evaluating
the DOB-Cascaded PID integration against the Dryden wind
turbulence model on a quadrotor UAV. The robust stability of
the chosen filter Q for the disturbance observer is assessed
using the small gain theorem. The results are then compared
to that of a normal cascaded PID controller.
The paper is organized as follows: section 2 is going to cover
the non-linear quadrotor model and the Dryden wind model,
section 3 is covering the design of the cascaded PID controller
used in the quadrotor system and the linearized model, section
4 is covering the design of the used disturbance observer,
section 5 will cover the simulations and results and section
6 is going to cover the conclusion of this paper.
II. DYNAMIC MODELING
A. Modeling the quadrotor dynamics
With the help of [21], the equations of motion were de-
rived for a quadrotor using Lagrange energy technique in the
Body-Fixed Axes. For the translational motion, the following
equations were derived:
m¨x = T cos ϕ sin θ −Ax ˙x
m¨y = −T sin ϕ −Ay ˙y
m¨z = T cos ϕ cos θ −mg −Az ˙z
(1)
where m is the mass of the quadrotor, g is the acceleration
due to gravity, ϕ, θ and ψ are the roll, pitch and yaw angles
respectively, Ax, Ay and Az represent the drag coefficients in
the X, Y and Z directions respectively and T represents the
2026 IEEE 23rd Mediterranean Electrotechnical Conference (MELECON)
979-8-3315-2684-9/26/$31.00 ©2026 IEEE
2026 IEEE 23rd Mediterranean Electrotechnical Conference (MELECON) | 979-8-3315-2684-9/26/$31.00 ©2026 IEEE | DOI: 10.1109/MELECON64486.2026.11418847
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 12:22:26 UTC from IEEE Xplore.  Restrictions apply.

## Page 2

thrust force which is represented by the following equation:
T = k(ω2
1 + ω2
2 + ω2
3 + ω2
4)
(2)
where k is the lift factor and ωi is the angular velocity of the
motor. For the rotational motion, the following equations were
derived:
J d2η
dt2 + C dη
dt = B
η =


ϕ
θ
ψ


B =


Lk(ω2
4 −ω2
2)
Lk(ω2
3 −ω2
1)
b(ω2
2 + ω2
4 −ω2
1 −ω2
3)


(3)
where L is the length of the quadrotor’s arm, b is the drag
factor, while C and J are 3×3 matrices that are shown in the
appendix.
B. Dryden wind modeling
In the used model, disturbances are modeled using the
Dryden wind model where the gust component of the wind
is modeled using the following transfer functions[22]:
Hu(s) = ud(s)
ηu(s) = σu
r
2Va
πLu
1
s + Va
Lu
Hv(s) = vd(s)
ηv(s) = σv
r
3Va
πLv
(s +
Va
√
3Lv )
(s + Va
Lv )2
Hw(s) = wd(s)
ηw(s) = σw
r
3Va
πLw
(s +
Va
√
3Lw )
(s + Va
Lw )2
vwx = ¯vwx + ud
vwy = ¯vwy + vd
vwz = ¯vwz + wd
(4)
where ud, vd and wd represent deviations from the mean
velocity, σu, σv and σw are turbulence intensities, Lu, Lv
and Lw are the turbulence scale lengths, Va is the mean wind
velocity, ηu, ηv and ηw represent zero-mean white gaussian
noise with a unity standard deviation, vwx, vwy and vwz
represent the wind velocities across the inertial axes and s
is the Laplace variable. The mean wind velocities are chosen
to be 0.5 m/s for X and Y and 0.3 m/s for Z.
III. CONTROLLER DESIGN
The overall system is shown in figure 1. It consists of 5
main parts: the motion profile which generates the reference
points, the drone model, the outer loop, the inner loop and the
disturbance observer. The cascaded PID controller was used
for controlling the quadrotor system due to its simplicity and
easier tuning in comparison to other non-linear techniques.
The control system consists of two loops: the outer loop and
the inner loop.
Fig. 1. Detailed overall control scheme with disturbance observer, ζ represents
external disturbances
A. Outer loop
The outer loop calculates the difference between the ref-
erence position and current position and multiplies each co-
ordinate by its respective PID controller. The resulting values
Xd, Yd and Zd, represent the desired accelerations in the X, Y
and Z directions respectively, are used to calculate the desired
pitch angle θd, the desired roll angle ϕd and the desired thrust
Ti using the following equations:
θd = tan−1(
Xd
Zd + g )
(5)
ϕd = tan−1(−Yd cos θd
Zd + g
)
(6)
Ti = m ∗
q
X2
d + Y 2
d + (Zd + g)2
(7)
The desired yaw angle ψd is assumed to be 0.
B. Inner loop
In the inner loop the difference between the desired angles
and the current angles is calculated and multiplied by PD
controllers to generate the desired angular accelerations ¨ϕ, ¨θ
and ¨ψ. The angular acceleration values are used to calculate
three torques in the roll, pitch and yaw directions using the
following equations:
τϕ = Ixx ¨ϕ
τθ = Iyy ¨θ
τψ = Izz ¨ψ
(8)
where Ixx, Iyy and Izz are the products of inertia about the
body frame’s inertial axes.
The calculated torques in combination with the desired thrust
Ti calculated in equation (7) are used to calculate the angular
2026 IEEE 23rd Mediterranean Electrotechnical Conference (MELECON)
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 12:22:26 UTC from IEEE Xplore.  Restrictions apply.

## Page 3

Fig. 2. Simplified model of the overall control scheme
speeds of the four motors using the following equations:
ω2
1 = Ti
4k −τθ
2kl −τψ
4b
ω2
2 = Ti
4k −τϕ
2kl + τψ
4b
ω2
3 = Ti
4k + τθ
2kl −τψ
4b
ω2
4 = Ti
4k + τϕ
2kl + τψ
4b
(9)
C. Linearized model of the quadrotor control system
In order to design the disturbance observer, a linearized
model of the gray box in figure 1 which represents the actual
plant P(s), which includes the outer loop, the inner loop and
the plant, is required to get the necessary transfer functions
of the nominal plant Pn(s). Figure 2 shows the simplified
quadrotor control system. In order to linearize the quadrotor
system, three operating points were chosen corresponding to
the UAV motion in each of the three axes with constant
velocity. The defined operating points were as follows:
[˜x, ˜y, ˜z] = [x0, y0, z0]
[˜˙x, ˜˙y, ˜˙z] = [vx, vy, vz]
[˜ϕ, ˜θ, ˜ψ] = [0, 0, 0]
[˜˙ϕ, ˜˙θ, ˜˙ψ] = [0, 0, 0]
(10)
where for each operating point two of the three values vx,
vy and vz are equal to zero while the third value is 5. The
linearization was done by the MATLAB Simulink Model
Linearizer app. For each operating point, the nominal plant
transfer function between one of the three positions (X, Y and
Z) and its corresponding desired acceleration (Xd, Yd and Zd)
that is produced by the PID controller in the outer loop of the
control system was computed to be:
Pn(s) =





X(s)
Xd(s)
=
0.06901s3+52.71s2+3438s+763.8
s5+764.3s4+3846s3+2600s2+408s
Y (s)
Yd(s)
=
0.06901s3+52.71s2+3438s+763.8
s5+764.3s4+3846s3+2600s2+408s
Z(s)
Zd(s)
=
1
s2+0.53s
(11)
IV. DISTURBANCE OBSERVER DESIGN
The disturbance observer is mainly concerned with predict-
ing the disturbances facing the system and then compensating
for it in the controller’s output. Figures 1 and 2 show the
DOB model where Ex, Ey and Ez represent the estimated
disturbances in the X, Y and Z directions respectively, Q(s)
represents the used filter and ζ represents the external distur-
bances. In order to design a disturbance observer two things
are needed:
• The inverse of the transfer function of the nominal plant
which was already computed in equation (11).
• A filter Q.
The chosen filter Q for the DOB should satisfy the following
requirements:
• Lims−>0Q = 1 so that at low frequencies Q(s) ≈1
which makes the estimated disturbances [Ex, Ey, Ez]
equal to the actual disturbances facing the system.
• The relative degree of Q should be more than or equal
to the relative degree of the nominal transfer function as
the nominal plant Pn(s) in equation (11) is linear time-
invariant system whose relative degree is more than 1,
so its inverse P −1
n (s) becomes an improper fraction that
needs to be multiplied by a transfer function that satisfies
this condition.
A filter that satisfies the previous requirements is able, at low
frequencies, to give an accurate estimation of the disturbances
facing the system and compensate for it in the controller’s out-
put. Consequently, a low pass filter is used and its bandwidth
is tuned to be as large as possible to reject disturbances with
lower frequencies. However, if the bandwidth is increased, the
plant might be affected by noise in the system. To help in
designing the used filter, the small gain theorem is used [23]
which guarantees the stability of the system with the added
filter if the following inequality is satisfied:
||Q(s)∆(s)||∞< 1
(12)
which can be rewritten as:
||Q(s)||∞<
1
||∆(s)||∞
(13)
where ∆(s) refers to the uncertainty between the nominal plant
and the actual plant. While this study primarily models ∆(s) as
a time delay, in practice, it also encompasses parametric uncer-
tainties such as mismatches in mass, inertia tensors, and aero-
dynamic drag or thrust coefficients. These parametric errors
would increase the magnitude of the uncertainty ||∆(s)||∞,
at higher frequencies. According to the small-gain theorem
(13), the presence of significant parametric mismatch would
lower the stability upper bound (the 1/∆curve), therefore
necessitating a more conservative Q-filter with a lower cutoff
frequency ωn to guarantee stability[24].
To evaluate the validity of this assumption, the behavior
of the transfer functions of the nominal plant calculated in
equation (11) is compared to that of the actual plant when
tracking a straight path in each axis.
2026 IEEE 23rd Mediterranean Electrotechnical Conference (MELECON)
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 12:22:26 UTC from IEEE Xplore.  Restrictions apply.

## Page 4

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
Time (s)
0
10
20
30
40
50
60
X (m)
Xreal
Xnominal
50
50.002
50.004
50.006
50.008
50.01
27.732
27.734
27.736
27.738
Fig. 3. Comparison of the linearized and real plant responses in the X-axis
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
Time (s)
0
10
20
30
40
50
60
Y (m)
Yreal
Ynominal
50
50.002
50.004
50.006
50.008
50.01
27.732
27.734
27.736
27.738
Fig. 4. Comparison of the linearized and real plant responses in the Y-axis.
As seen from figures 3, 4 and 5, the actual plant and the
nominal plant behave in a similar manner with only a time
delay between them. The time delay between the real plant
and the nominal plant in the X,Y and Z directions was found
to be 2.5, 2.5 and 1.4 milliseconds respectively.
If the nominal plant is given by the following transfer function:
Pn(s) = Bn(s)
An(s)
(14)
Then the actual plant will be given by the following transfer
function:
P(s) = e−sTd Bn(s)
An(s)
(15)
where Td refers to the time delay between the actual plant and
the nominal plant.
From equations (14) and (15) we get the following equation:
P(s) = e−sTdPn(s)
(16)
which can be rewritten as:
P(s) = Pn(s)(1 + ∆(s))
(17)
where:
∆(s) = e−sTd −1
(18)
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
Time (s)
0
10
20
30
40
50
60
Z (m)
Zreal
Znominal
50
50.002
50.004
50.006
50.008
50.01
27.726
27.728
27.73
27.732
Fig. 5. Comparison of the linearized and real plant responses in the Z-axis.
Combining inequality (13) and equation (18) gives us the
following inequality:
||Q(s)||∞<
1
||e−sTd −1||∞
(19)
The chosen filter is given by the following equation:
Q(s) =
ω2
n
(τs)2 + a(τs) + ω2n
(20)
where ωn represents the bandwidth of the filter while a and
τ are constants.
Choosing ωn to be 50 rad/s, a to be 1000 and τ to be
0.4, the selected bandwidth ωn limits the Q-filter’s gain
such that its magnitude, |Q(jω)|, never intersects or exceeds
the magnitude of the inverse uncertainty bound, |∆−1(jω)|,
to satisfy the inequality (13). Since the uncertainty ∆(jω)
dominated by unmodeled high-frequency dynamics and time
delays grows with frequency, the stability limit |∆−1(jω)|
drops significantly at higher frequencies. creating a stability
limit which decreases the bandwidth when subjected to higher
uncertainties, so according to the small gain theorem the robust
stability of the system should be guaranteed[23]. The bode
plots of Q(s) and ∆−1(s) are shown for X, Y and Z in figures
6, 7 and 8.
-200
0
200
400
Magnitude (dB)
10-1
100
101
102
103
104
105
-180
-90
0
90
180
270
Phase (deg)
1/delta
Qx
Frequency  (rad/s)
Fig. 6. Bode diagram of filter Qx and uncertainty ∆−1
x
-200
0
200
400
Magnitude (dB)
10-1
100
101
102
103
104
105
-180
-90
0
90
180
270
Phase (deg)
1/delta
Qy
Frequency  (rad/s)
Fig. 7. Bode diagram of filter Qy and uncertainty ∆−1
y
2026 IEEE 23rd Mediterranean Electrotechnical Conference (MELECON)
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 12:22:26 UTC from IEEE Xplore.  Restrictions apply.

## Page 5

-200
-100
0
100
200
300
Magnitude (dB)
10-1
100
101
102
103
104
105
-180
-90
0
90
180
270
Phase (deg)
1/delta
Qz
Frequency  (rad/s)
Fig. 8. Bode diagram of filter Qz and uncertainty ∆−1
z
TABLE I
SYSTEM CONSTANTS AND THEIR VALUES
Constant
Value
Constant
Value
Ax
0.25
l
0.225 m
Ay
0.25
m
0.468 kg
Az
0.25
σu
2.12 m/s
Ixx
0.004856 m4
σv
2.12 m/s
Iyy
0.004856 m4
σw
1.4 m/s
Izz
0.008801 m4
Lu
200 m
b
1.14 × 10−7
Lv
200 m
g
9.81 m/s2
Lw
50 m
k
2.98 × 10−6
Va
0.5 m/s
Fig. 10. Simulation results: Position error for the X direction
Fig. 9. Simulation results: UAV path
Fig. 11. Simulation results: Position error for the Y direction
Fig. 12. Simulation results: Position error for the Z direction
V. SIMULATION RESULTS
Simulations were conducted to compare the performance
of a quadrotor equipped with a disturbance observer (DOB)-
based controller against that of a conventional cascaded PID
controller. Disturbances were modeled using the Dryden wind
turbulence model. The constants employed in the quadrotor
model are listed in Table I. The PID values were chosen with
the help of the MATLAB PID Tuner App to optimal values
for rise time, settling time and overshoot. For the outer loop,
the chosen values for the PID controllers were 4, 0.04, 2.4
for X and Y, and 3, 0.04, 2 for Z. For the inner loop, the
chosen values for the PD controllers were 1 and 4.5. The
simulated trajectory is shown in figure 9. Tracking errors for
both controllers in the X, Y, and Z axes are compared in figures
10, 11, and 12, respectively.
The performance of the cascaded PID and DOB-based con-
trollers was evaluated using RMSE and standard deviation
metrics along the X, Y, and Z axes. The cascaded PID
controller exhibited RMSE values of 10.2, 11.9, and 14 cm
and standard deviations of 10.2, 11.9, and 13.4 cm, in the X,
Y, and Z directions, respectively. In comparison, the DOB-
based controller achieved lower RMSE values of 7.5, 7.3,
and 7.2 cm and standard deviations of 7.5, 7.2, and 5.4
cm. Overall, the DOB-based controller reduced RMSE by
26.47%, 38.66%, and 48.57% in the X, Y, and Z positions,
respectively. Corresponding standard deviation reductions of
26.47%, 39.5%, and 59.7% were observed.
VI. CONCLUSION
In this study, a disturbance observer–based control scheme
was developed for a quadrotor UAV, and its robust stability was
verified using the small-gain theorem. The proposed controller
2026 IEEE 23rd Mediterranean Electrotechnical Conference (MELECON)
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 12:22:26 UTC from IEEE Xplore.  Restrictions apply.

## Page 6

was evaluated against a conventional cascaded PID controller
through simulation scenarios in which the UAV was required
to track reference trajectories under continuous Dryden wind
disturbances. The results demonstrated that the disturbance
observer–augmented controller achieved superior stabilization
and trajectory tracking performance compared to the baseline
PID framework. Notably, the addition of the disturbance ob-
server significantly enhanced the effectiveness of the otherwise
simple cascaded PID architecture, highlighting its potential as
a practical and robust solution for UAV control.
REFERENCES
[1] S. Bouabdallah and R. Siegwart, “Backstepping and sliding-mode tech-
niques applied to an indoor micro quadrotor,” in Proceedings of the 2005
IEEE International Conference on Robotics and Automation, 2005, pp.
2247–2252.
[2] P. Garg, “Characterisation of fixed-wing versus multirotors uavs/drones,”
Journal of Geomatics, vol. 16, no. 2, pp. 152–159, 2022.
[3] B.
Alzahrani,
O.
S.
Oubbati,
A.
Barnawi,
M.
Atiquzzaman,
and D. Alghazzawi, “Uav assistance paradigm: State-of-the-art in
applications and challenges,” Journal of Network and Computer
Applications,
vol.
166,
p.
102706,
2020.
[Online].
Available:
https://www.sciencedirect.com/science/article/pii/S1084804520301806
[4] J. Everaerts et al., “The use of unmanned aerial vehicles (uavs) for
remote sensing and mapping,” The international archives of the pho-
togrammetry, remote sensing and spatial information sciences, vol. 37,
no. 2008, pp. 1187–1192, 2008.
[5] H. Shakhatreh, A. H. Sawalmeh, A. Al-Fuqaha, Z. Dou, E. Almaita,
I. Khalil, N. S. Othman, A. Khreishah, and M. Guizani, “Unmanned
aerial vehicles (uavs): A survey on civil applications and key research
challenges,” IEEE Access, vol. 7, pp. 48 572–48 634, 2019.
[6] J. Ghandour, S. Aberkane, and J.-C. Ponsart, “Feedback linearization
approach for standard and fault tolerant control: Application to a
quadrotor uav testbed,” vol. 570, no. 8, dec 2014, p. 082003. [Online].
Available: https://doi.org/10.1088/1742-6596/570/8/082003
[7] E.-H. Zheng, J.-J. Xiong, and J.-L. Luo, “Second order sliding mode
control for a quadrotor uav,” ISA Transactions, vol. 53, no. 4, pp. 1350–
1356, 2014, disturbance Estimation and Mitigation. [Online]. Available:
https://www.sciencedirect.com/science/article/pii/S0019057814000512
[8] R. Rashad, A. Aboudonia, and A. El-Badawy, “Backstepping trajectory
tracking control of a quadrotor with disturbance rejection,” in 2015
XXV International Conference on Information, Communication and
Automation Technologies (ICAT).
IEEE, 2015, pp. 1–7.
[9] V. Praveen and A. Pillai, “Modeling and simulation of quadcopter using
pid controller,” vol. 9, pp. 7151–7158, 01 2016.
[10] A. Prach and E. Kayacan, “An mpc-based position controller for a tilt-
rotor tricopter vtol uav,” Optimal control applications and methods,
vol. 39, no. 1, pp. 343–356, 2018.
[11] A. Ingabire and A. A. Sklyarov, “Control of longitudinal flight dynamics
of a fixedwing uav using lqr, lqg and nonlinear control,” in E3S Web of
Conferences, vol. 104.
EDP Sciences, 2019, p. 02001.
[12] A. Eltayeb Taha, M. Rahmat, and A. Basri, “Adaptive feedback lineariza-
tion controller for stabilization of quadrotor uav,” International Journal
of Integrated Engineering, vol. 12, 07 2020.
[13] N. T. Hegde, V. I. George, C. G. Nayak, and A. C. Vaz, “Application of
robust h-infinity controller in transition flight modeling of autonomous
vtol convertible quad tiltrotor uav,” International Journal of Intelligent
Unmanned Systems, vol. 9, no. 3, pp. 204–235, 01 2021. [Online].
Available: https://doi.org/10.1108/IJIUS-09-2020-0041
[14] G. C. Goodwin, S. F. Graebe, M. E. Salgado et al., Control system
design.
Prentice Hall Upper Saddle River, 2001, vol. 240.
[15] A. Wood and B. Wollenberg, Power generation, operation, and control,
01 2012.
[16] A. Aboudonia, R. Rashad, and A. El-Badawy, “Time domain disturbance
observer based control of a quadrotor unmanned aerial vehicle,” in
2015 XXV International Conference on Information, Communication
and Automation Technologies (ICAT).
IEEE, 2015, pp. 1–6.
[17] H. Wang and M. Chen, “Trajectory tracking control for an indoor
quadrotor uav based on the disturbance observer,” Transactions of the
Institute of Measurement and Control, vol. 38, 08 2015.
[18] X. Lyu, J. Zhou, H. Gu, Z. Li, S. Shen, and F. Zhang, “Disturbance
observer based hovering control of quadrotor tail-sitter vtol uavs using
H∞synthesis,” IEEE Robotics and Automation Letters, vol. 3, no. 4,
pp. 2910–2917, 2018.
[19] F. Wang, H. Gao, K. Wang, C. Zhou, Q. Zong, and C. Hua, “Disturbance
observer-based finite-time control design for a quadrotor uav with
external disturbance,” IEEE Transactions on Aerospace and Electronic
Systems, vol. 57, no. 2, pp. 834–847, 2021.
[20] A. Moeini, A. Lynch, and Q. Zhao, “A backstepping disturbance ob-
server control for multirotor uavs: theory and experiment,” International
Journal of Control, vol. 95, pp. 1–15, 05 2021.
[21] N. Muraleedharan, D. S. Cohen, V. V. Estrela, J. Hemanth, O. Saotome,
G. Nikolakopoulos, R. Sabatini, and L. Wackett, “Modelling and sim-
ulation of uav systems,” Imaging and Sensing for Unmanned Aircraft
Systems, vol. 1, pp. 101–121, 2020.
[22] S. Waslander and C. Wang, “Wind disturbance estimation and rejection
for quadrotor position control,” in AIAA Infotech@ Aerospace confer-
ence and AIAA unmanned... Unlimited conference, 2009, p. 1983.
[23] Z. P. Jiang, A. R. Teel, and L. Praly, “Small-gain theorem for iss systems
and applications,” Mathematics of Control, Signals and Systems, vol. 7,
pp. 95–120, 1994.
[24] C. Kempf and S. Kobayashi, “Disturbance observer and feedforward de-
sign for a high-speed direct-drive positioning table,” IEEE Transactions
on Control Systems Technology, vol. 7, no. 5, pp. 513–526, 1999.
VII. APPENDIX
The two matrices J and C are shown below where J
represents the inertia matrix while C represents centripetal
matrix:
J =


Ixx
0
−IxxSθ
0
IyyC2ϕ + IzzS2ϕ
(Iyy −Izz)CϕSϕCθ
−IxxSθ
(Iyy −Izz)CϕSϕCθ
J33


(21)
J33 = IxxS2θ + IyyS2ϕ2θ + IzzC2ϕC2θ
(22)
C =


C11
C12
C13
C21
C22
C23
C31
C32
C33


(23)
C11 = 0
(24)
C12 = (Iyy −Izz)( ˙θCϕSϕ + ˙ψS2ϕCθ)
+(Izz −Iyy) ˙ψC2ϕCθ −Ixx ˙ψCθ
(25)
C13 = (Izz −Iyy) ˙ψCϕSϕC2θ
(26)
C21 = (Izz −Iyy)( ˙θCϕSϕ + ˙ψSϕCθ)
+(Iyy −Izz) ˙ψC2ϕCθ + Ixx ˙ψCθ
(27)
C22 = (Izz −Iyy) ˙ϕCϕSϕ
(28)
C23 = −Ixx ˙ψSθCθ + Iyy ˙ψS2ϕSθCθ
+ Izz ˙ψC2ϕSθCθ
(29)
C31 = (Iyy −Izz) ˙ψC2θSϕCϕ −Ixx ˙θCθ
(30)
C32 = (Izz −Iyy)( ˙θCϕSϕSθ + ˙ϕS2ϕCθ)
+(Iyy −Izz) ˙ϕC2ϕCθ + Ixx ˙ψSθCθ
−Iyy ˙ψS2ϕSθCθ −Izz ˙ψC2ϕSθCθ
(31)
C33 =(Iyy −Izz) ˙ϕCϕSϕC2θ −Iyy ˙θS2ϕCθSθ
−Izz ˙θC2ϕCθSθ + Ixx ˙θCθSθ
(32)
2026 IEEE 23rd Mediterranean Electrotechnical Conference (MELECON)
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 12:22:26 UTC from IEEE Xplore.  Restrictions apply.
