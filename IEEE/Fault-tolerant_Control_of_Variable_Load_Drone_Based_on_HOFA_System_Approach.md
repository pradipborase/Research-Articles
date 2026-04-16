# Fault-tolerant_Control_of_Variable_Load_Drone_Based_on_HOFA_System_Approach.pdf

## Page 1

Fault-tolerant Control of Variable Load Drone
Based on HOFA System Approach
1st Runze Wang
Department of Control Sciences and Engineering
Harbin Institute of Technology
Harbin, China
23B904007@stu.hit.edu.cn
3rd Linjie Li
Department of Control Sciences and Engineering
Harbin Institute of Technology
Harbin, China
23S136183@stu.hit.edu.cn
2nd Ruizhi Tong
Department of Control Sciences and Engineering
Harbin Institute of Technology
Harbin, China
23S104097@stu.hit.edu.cn
4th Yi Zeng*
Department of Control Sciences and Engineering
Harbin Institute of Technology
Harbin, China
yi.zeng@hit.edu.cn
Abstract—This paper proposes an integral sliding controller
based on second-order fully actuated system theory for the
control problem of variable load six rotor unmanned aerial
vehicles in the event of ﬂight faults, and an extended observer
with model information is used to estimate and compensate
for the fault signals which occur during the ﬂight. This paper
innovatively introduces virtual control variables to supplement
the system into a second-order six dimensional fully actuated
system, and designs an integral sliding mode controller using
a modiﬁed saturation function to achieve rapid stability of
unmanned aerial vehicles during the process of verying load.
In addition, the extended observer can also successfully estimate
and compensate for the loss of execution efﬁciency of the drone.
Index Terms—High-order Fully Actuated Systems, Various
Load Drones, Sliding Mode control, Fault-Tolerant Control
I. INTRODUCTION
A great number of unmanned aerial vehicles (UAVs) have
been successfully applied in many different ﬁelds. For example
transportation and agriculture over the last decade. They can
not only free people from repetive labor, but also complete
some dangerous works such as disaster recovery and moutain
mapping. Different works under various situation have put
forward diverse requirements for drones, including the ability
to carry various loads and cope with rotor fault events. The
controllers, as the core of UAVs, need to adopt advanced
methods with strong robustness and disturbance resistance
to deal with emerging problems. Numerous attitude con-
trol methods are proposed, considering the following control
approach: proportional-integral-derivative (PID) control [1],
linear-quadratic regulator (LQR) [2], model predictive control
(MPC) [3], and sliding mode control (SMC) [4], High-Order
Fully Actuated (HOFA) system theory [5], etc.
This work was supported in part by Harbin Institute of Technology, and
in part by the National Natural Science Foundation of China under Grant
62188101, 62303135,62033005, and 62320106001, and in part by the Natural
Science Foundation of Heilongjiang Province (ZD2021F001), and in part by
the Heilongjiang Touyan Team Program. (corresponding author: Yi Zeng)
The algorithms mentioned above have their own features.
H.Bolandi [1] combined a PID controller with a genetic
algorithm to implement the stability of quadcopters. In order
to make the system respond faster, M.R.Cohen [2] researched
optimal control for a quadcopter drone based on discrete-time
ﬁnite-horizon LQR, demonstrating superior performance com-
pared to traditional LQR controllers. Although MPC has difﬁ-
culties in tracking complex trajectories, M.Islam [3] designed
a MPC controller exploiting a linear modelfor prediction. The
results indicated its good dynamic performance and tracking
ability. To solve uncertainty and external disturbance problems
and improve the robustness of the system, Abro, G.E.M [4]
introduced a model-free one-dimensional fuzzy sliding mode
control (MFSDF-SMC) to control the attitude and position of
underactuated UAV.
In recent years, the Fully Actuated System (FAS) approach
[5] has attracted attention of the academia. This approach
exhibits excellent characteristics, as fully actuated systems are
commonly present in the real world, and many systems’ initial
mathematical models can be described as natural second-order
or higher-order fully actuated systems. This form of systems is
relatively simple and possesses full actuation characteristics,
which reduces the complexity of controller design [5]. Marko
Pranjic [6] successfully proved that this theory can be applied
to multi rotor systems and compared and analyzed the advan-
tages and disadvantages of traditional control and LQR. Lu
[7] proposed an improved HOFA method which divided the
system into two subsystems and displayed its effectiveness
in his work. Yan [8] combined this theory with disturbance
observer (DOB) and enabled a quadcopter affected by external
interference to stably track a designated trajectory. DOB was
also used by Li [9] to form a novel fault-tolerant control with
HOFA and the results illustrated that this controller was able
to deal with actuator faults.
Although dozens of papers have shown their researches on
HOFA and UAV system, there still are tons of cases which
deserved to be studied. Lots of works, it should be noted, still
7
2024 8th International Symposium on Computer Science and Intelligent Control (ISCSIC)
979-8-3503-8028-6/24/$31.00 ©2024 IEEE
DOI 10.1109/ISCSIC64297.2024.00011
2024 8th International Symposium on Computer Science and Intelligent Control (ISCSIC) | 979-8-3503-8028-6/24/$31.00 ©2024 IEEE | DOI: 10.1109/ISCSIC64297.2024.00011
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:37:07 UTC from IEEE Xplore.  Restrictions apply.

## Page 2

focus on traditional control methods ignoring model informa-
tion, because coupling and nonlinearity are considered as the
model uncertainty. Meanwhile, different application scenarios
have various functional requirements for drones, for example
extra load. This work focuses on in-depth research on fault-
tolerant algorithms for variable load unmanned aerial vehicles.
We propose an improved integral sliding mode controller
based on HOFA system theory to eliminate the impact of load
changes and add an model-based extended observer into the
controller to handle fault events. The results show that this
method has strong robustness, and can effectively handle the
load changes and fault events of drones during ﬂight.
II. HIGH-ORDER FULLY ACTUATED SYSTEM MODEL FOR
VARIABLE LOAD DRONE
According to the description in [10], we can obtain a general
model of rotor unmanned aerial vehicles (UAV) :



















¨x = −Kx
mb ˙x + cos φ sin θ cos ψ+sin φ sin ψ
mb
Fz
¨y = −Ky
mb ˙y + cos φ sin θ sin ψ−sin φ cos ψ
mb
Fz
¨z = −Kz
mb ˙z −g + cos φ cos θ
mb
Fz
¨φ = Iby−Ibz
Ibx
˙θ ˙ψ +
1
Ibx τφ
¨θ = Ibz−Ibx
Iby
˙φ ˙ψ +
1
Iby τθ
¨ψ = Ibx−Iby
Ibz
˙φ ˙θ +
1
Ibz τψ
,
(1)
where x, y and z are three components of drone position in
the ground coordinate system; φ, ψ and θ are the attitude
angle of drones. Therefore, ˙i and ¨i (i = x, y, z, φ, ψ, θ) mean
the ﬁrst and second derivatives of i. Meanwhile, Ibx, Iby and
Ibz represent the rotational inertia of the drone in three axial
directions; Kx, Ky and Kz are the air resistance coefﬁcients
in three directions; mb is the mass of UAV and Fz is the lift
force provided by rotors.
When adding additional loads to a drone, multiple factors
need to be considered, such as whether the connection between
drones and loads is rigid, and the impact of changes in
centroidal position on the system. In order to simplify the
model in this paper, we assume that the mass distribution of the
load is uniform and symmetrical; loads are rigidly connected
to UAV; after the drone carries goods, centroidal position of
goods is horizontally projected at the same position as the
drone’s center of mass. Let ms represent the mass of the load;
rs = [0, 0, zs]T represent the distance from the barycenter
location of the load to the coordinate origin in aircraft-body co-
ordinate frame, where zs represent the component of rs along
the z-axis in the body coordinate system; Is = [Isx, Isy, Isz]T
represents the moment of inertia for goods, where Isx, Isy, Isz
represents the components of Is on the three-axis direction,
and the mass of loaded drone system m can be obtained:
m = mb + ms.
(2)
The inertia of drone carrying cargo in three directions:



Ix = Ibx + Isx + msz2
s
Iy = Iby + Isy + msz2
s
Iz = Ibz + Isz
.
(3)
Ignoring the impact caused by changes in the centroid position,
a simpliﬁed model of the loaded UAV system can be obtained
as (4):

































¨x = −Kx
m ˙x + cos φ sin θ cos ψ+sin φ sin ψ
m
Fz
¨y = −Ky
m ˙y + cos φ sin θ sin ψ−sin φ cos ψ
m
Fz
¨z = −Kz
m ˙z −g + cos φ cos θ
m
Fz
¨φ = Iy−Iz
Ix
˙θ ˙ψ + τφ
Ix
¨θ = Iz−Ix
Iy
˙φ ˙ψ + τθ
Iy
¨ψ = Ix−Iy
Iz
˙φ ˙θ + τψ
Iz
m = mb + ms
Ix = Ibx + Isx + msz2
s
Iy = Iby + Isy + msz2
s
Iz = Ibz + Isz
.
(4)
According to Duan [11] [12], a second-order fully actuated
system (8) can be obtained:
E¨x = f(x, ˙x, t) + B(x, ˙x, t)u −v,
(5)
where the control distribution matrix satisﬁes the following
fully actuated conditions:
det B(x, x, t) ̸= 0, ∀x, ˙x ∈Rn, t ≥0.
(6)
When the system satisﬁes the fully actuated conditions, for
any given matrix A1, A0 ∈Rn×n, it can always be achieved
through the control law:
u = −B−1(·)[A1 ˙x + A0x + f(x, ˙x, t) −v].
(7)
Obtain the following linear steady-state closed-loop system:
E¨x + A1 ˙x + A0x = ν.
(8)
We deﬁne

















u1 = cos φd sin θd cos ψd+sin φd sin ψd
m+∆m
Fz
u2 = cos φd sin θd sin ψd−sin φd cos ψd
m+∆m
Fz
u3 = cos φd cos θd
m+∆m
Fz
u4 =
1
Ix τφ
u5 =
1
Iy τθ
u6 =
1
Iz τψ
.
(9)
Among them, ϕd, θd, φd represents the desired angle.
Subsequently, we can obtain:
E¨x = f(x, ˙x, t) + B(x, ˙x, t)u −v,
(10)
where E and B are both the identity matrices of I6×6
f(x, ˙x, t) = diag(−
K1
m+∆m ˙x, −
K2
m+∆m ˙y, −
K3
m+∆m ˙z,
Iy−Iz
Ix
˙θ ˙ψ, Iz−Ix
Iy
˙φ ˙ψ, Ix−Iy
Iz
˙φ ˙θ)
, (11)
v =
 0
0
g
0
0
0 T .
(12)
8
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:37:07 UTC from IEEE Xplore.  Restrictions apply.

## Page 3

III. SLIDING MODE CONTROL
The sliding mode control proposed in the last century is
a simple, feasible and effective control algorithm with strong
robustness. In this chapter, an improved integral sliding mode
controller based on the fully actuated system theory will be
proposed.
The error of state variables e1 and its ﬁrst derivative are
deﬁned as [13]:
e1 = x −xd.
(13)
e2 = ˙x −˙xd,
(14)
where x represents the state variable and xd is the expected
input for the state variable. Thus the general formula of the
integral sliding mode control can be given:
s = e2 + kpe1 + ki ∫t
0 e1dτ,
(15)
where kp and kiare two positive constants.
A nonlinear fuction H is introduced to replace the original
integral term, which can deal with integral saturation problem.
Meanwhile in order to reduce the overshoot, another positive
parameter kd is introduced. The new formula is as follows:
 s = kde2 + kpe1 + kiH −e2(0) −kpe1(0)
˙H = h(e)
,
(16)
where:
H(e) =



2β
π (1 −cos( π
2β e))
|e| < β
βe −π−2
π β2
e ≥β
−βe −π−2
π β2
e ≤−β
.
(17)
In the fomula above, β is a positive constant meaning switch
boundaries. Taking the derivative of H(e), we obtain a new
nonlinear function h:
h(e) =



β sin πρ
2β
|e| < β
β
e ≥β
−β
e ≤−β
.
(18)
Therefore, the derivative of fomula (16) above is obtained:
 ˙s = kd ˙e2 + kpe2 + kih(e)
˙H = h(e)
.
(19)
Combining (19) and HOFA model (10), we can obtain:
˙s = kd
f(x, ˙x, t) + B(x, ˙x, t)u −v −¨xd

+kpe2 + kih(e)
.
(20)
For the approach law, we adopt the traditional exponential
approach law here:
˙s = −εsigm(s) −ks
k ≥0, ε ≥0.
(21)
In the law, εsigm(s) is the constant speed reaching term, ks
is the exponential reaching term. Usually, k is designed to be
a large value, and ε is designed to be a small value. When the
system state is far from the sliding surface, the exponential
reaching term can make the system state quickly approach the
vicinity of the sliding surface. When the system state is close
to the sliding surface, the constant speed reaching term plays a
major role. At this time, the approaching speed is ε, ensuring
that the system state reaches the sliding surface at a relatively
small speed.
We deﬁne sigm(s) =

1
1−e−bs −0.5

, in which b represents
the convergence speed.
Combining (20) and (21), we can obtain:
kd
 f + Bu −v −¨xd

+ kpe2 + kih(e)
+εsigm(s) + ks = 0
.
(22)
Therefore, the control law for the integral sliding mode is
obtained:
u = 1
B (−f + v + ¨xd −kpe2
kd
−kih(e)
kd
−εsigm(s)
kd
−ks
kd
).
(23)
Next we proof the stability using Lyapunov function which
is given as follow:
V = 1
2s2.
(24)
˙V = s ˙s = s · (kd ˙e2 + kP e2 + kih(e)) =
s(kd(f + Bu −v −¨xd) + kpe2 + kih(e)) .
(25)
Substituting the expression for the control input u in (23),
we get:
˙V = kds(−εsigm(s) −ks) = −k1sεsigm(s) −k2s2.
(26)
In general, we set k1 and k2 to positive values, which means
that ˙V will be negative deﬁnite when the value of s is non-zero.
Therefore, it can be determined that the system is stabilized
globally.
IV. FAULT-TOLERANT OBSERVER DESIGN
Due to actuator malfunctions, such as propeller damage, the
execution efﬁciency may deviate either towards high or low
values. This aspect can be considered as disturbances in the
system, and compensation can be achieved by constructing
an observer for the system. A core component of the self-
disturbance rejection control is the Extended State Observer
(ESO), which effectively suppresses the inﬂuence of external
uncertainties on the system. The fundamental idea of this
approach is to introduce disturbances that affect the controlled
output into new state variables and suppress these distur-
bances. This process linearizes the system, transforming it into
a cascaded system, ultimately controlled using an integrator.



















¨x = −
K1
m+∆m ˙x + cos φ sin θ cos ψ+sin φ sin ψ
m+∆m
Fz + d1
¨y = −
K2
m+∆m ˙y + cos φ sin θ sin ψ−sin φ cos ψ
m+∆m
Fz + d2
¨z = −
K3
m+∆m ˙z −g + cos φ cos θ
m+∆m Fz + d3
¨φ = Iy−Iz
Ix
˙θ ˙ψ + 1
Ix τφ + d4
¨θ = Iz−Ix
Iy
˙φ ˙ψ + 1
Iy τθ + d5
¨ψ = Ix−Iy
Iz
˙φ ˙θ + 1
Iz τψ + d6
.
(27)
9
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:37:07 UTC from IEEE Xplore.  Restrictions apply.

## Page 4

In the context of n-order nonlinear time-varying systems,















˙x1 = x2
˙x2 = x3
...
˙xn = f (x1, x2, · · · , xn, w(t), t) + bu
y = x1
.
(28)
The expanded state of the system can be represented as
follows:





















˙x1 = x2
˙x2 = x3
...
˙xn = xn+1 + bu
˙xn+1 = f(t)
y = x1
.
(29)
The estimated values of the expanded system state variables
are designated as: Z =
z1
z2
· · ·
zn
zn+1
T, state
observer can be established as follows:





















e = z1 −y
˙z1 = z2 −β1e
˙z2 = z3 −β2fal
e, α1, δ

...
˙zn = zn+1 −βnfal
e, αn−1, δ

+ bu
˙zn+1 = −βn+1fal
e, αn, δ

.
(30)
The control gain is represented by b, the state-space expres-
sions for each control channel are as follows:





˙x1 = x2
˙x2 = f(x2 + 1) + bu + d
y = x1
.
(31)
The expanded state of the system can be represented as
follows:









x1 = x2
x2 = f(x2, t) + bu + x3
x3 = d(t)
y = x1
.
(32)
The estimated values of the expanded system state variables
are designated as: Z =
z1
z2
z3
T, state observer can be
established as follows:









e = z1 −y
z1 = z2 −β1g1(e)
z2 = z3 −β2g2(e) + 6u + f(x2, t)
z3 = −β3g3(e)
.
(33)
TABLE I
THE MODEL PARAMETER VALUES
Parameters
value
m
17kg
∆m
1kg
k1
0.001N/(s · m2)
k2
0.001N/(s · m2)
k3
0.003N/(s · m2)
Ix
0.2kg·m2
Iy
0.2kg·m2
Iz
0.37kg·m2
TABLE II
THE GAIN SELECTION OF THE ATTITUDE CONTROLLER
Parameters
x
y
z
ϕ
θ
φ
kd
2
2
2
0.5
0.5
0.5
kp
50
50
50
80
80
80
ki
80
80
80
100
100
40
k
10
10
10
10
10
10
ε
0.1
0.1
0.1
1
1
1
β
10
10
10
10
10
10
a
10
10
10
10
10
10
V. NUMERICAL EXAMPLE
A numerical example is conducted on the sine wave and
ramp signal response of the system to verify its effectiveness.
Table I and II show the values of the model parameters as
well as the controller respectively.
Fig. 1 and 2 respectively show the position information and
tracking error of the drone. From Fig. 2, we can see that it
can quickly converge after tracking y and z for 0.3 seconds.
When tracking x, the error approaches zero within 0.3 seconds
and ﬂuctuates around the zero scale line, with an up and down
error of less than 0.005 meters. The position error is controlled
within a small range, indicating that the designed controller
has good tracking performance and can reach the speciﬁed
position in a short time.
Fig. 1. The response of the position in x, y and z
Fig. 3 and 4 respectively show the expected attitude and
tracking attitude error of the drone. From Fig. 4., we can see
that the tracking attitude angle in φ, ϕ and θ converge quickly
within 0.5 seconds and there is no overshoot or oscillation.
10
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:37:07 UTC from IEEE Xplore.  Restrictions apply.

## Page 5

Fig. 2. The tracking error of the position in x, y and z
Moreover, the impact of adding a load on the tracking error
of the attitude angle is minimal, with a maximum error of no
more than 0.2 degrees. The attitude angle error is controlled
within a small range, indicating that the controller has high
control accuracy and good performance.
Fig. 3. The response of the angle in roll ϕ, pitch θ and yaw axes φ
Fig. 4. The tracking error of the angle in roll ϕ, pitch θ and yaw axes φ
VI. CONCLUSION
This article proposes an integral sliding mode controller
based on second-order fully actuated system theory for the
control problem of variable load unmanned aerial vehicles in
the event of ﬂight faults. An extended observer with model
information is used to estimate and compensate for the fault
signals. Finally, a numerical example is used to verify the
effectiveness of the method and the results indicate that the
controller offers the strong robustness and excellent dynamic
performance. In the future, more consideration will be given
to the actual mission requirements of the aircraft, and further
research on aircraft control based on the HOFA system method
will be carried out.
REFERENCES
[1] Bolandi H, Rezaei M, Mohsenipour R, et al. Attitude control of a
quadrotor with optimized PID controller[J]. 2013.
[2] Cohen M R, Abdulrahim K, Forbes J R. Finite-horizon LQR control
of quadrotors on SE2(3)[J]. IEEE Robotics and Automation Letters,
2020, 5(4): 5748-5755.
[3] Islam M, Okasha M, Idres M M. Dynamics and control of quadcopter
using linear model predictive control approach[C]//IOP conference se-
ries: materials science and engineering. IOP Publishing, 2017, 270(1):
012007.
[4] Abro G E M, Zulkiﬂi S A B M, Asirvadam V S, et al. Model-free-
based single-dimension fuzzy SMC design for underactuated quadrotor
UAV[C]//Actuators. MDPI, 2021, 10(8): 191.
[5] G.R.Duan. Pseudo-Linear System Approach to Aircraft Control - Part II:
Methods and Prospects [J]. Journal of Astronautics,2020,41(7): 839-849.
[6] Pranjic M, Pender A, Piljek P, et al. Fully Actuated Multirotor UAV
Control Design and Implementation[C]//2022 International Conference
on Electrical, Computer and Energy Technologies (ICECET). IEEE,
2022: 1-6.
[7] Lu S, Tsakalis K, Chen Y. Development and application of a novel high-
order fully actuated system approach-Part I: 3-DOF quadrotor control[J].
IEEE Control Systems Letters, 2022, 7: 1177-1182.
[8] Yan X, Yu L, Shao G, et al. Robust Trajectory Tracking Control for
Quadrotor UAV with External Disturbances via Fully Actuated System
Approach[C]//2023 2nd Conference on Fully Actuated System Theory
and Applications (CFASTA). IEEE, 2023: 783-787.
[9] Li M, Zhang K, Miao Q, et al. Adaptive Fault-Tolerant Control for
Attitude and Altitude Synchronization of Quadrotors Based on Fully-
Actuated System Approaches[C]//2023 2nd Conference on Fully Actu-
ated System Theory and Applications (CFASTA). IEEE, 2023: 480-485.
[10] Rajappa S, Ryll M, Bulthoff H H, et al. Modeling, control and
design optimization for a fully-actuated hexarotor aerial vehicle with
tilted propellers[C]//2015 IEEE international conference on robotics and
automation (ICRA). IEEE, 2015: 4006-4013.
[11] G.R.Duan. High-order system methods I: Fully actuated systems and
parametric design [J]. Acta Automatica Sinica,2020,46(7): 1333-1345.
[12] Zhao Q, Duan G R. Fully actuated system approach for 6DOF spacecraft
control based on extended state observer[J]. Journal of Systems Science
and Complexity, 2022, 35(2): 604-622.
[13] Chen G X, He Y B, Qiu G F, et al. Integral Sliding Mode Control
of Permanent Magnet Synchronous Linear Motor [J]. Modular Machine
Tool and Automatic Manufacturing Technique, 2023(10): 77-80.
11
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:37:07 UTC from IEEE Xplore.  Restrictions apply.
