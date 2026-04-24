# Fixed-time tracking control of quadrotor UAVs based on disturbance observer and sliding mode.pdf

## Page 1

International Journal of Systems Science
ISSN: 0020-7721 (Print) 1464-5319 (Online) Journal homepage: www.tandfonline.com/journals/tsys20
Fixed-time tracking control of quadrotor UAVs
based on disturbance observer and sliding mode
Yulin Gai, Ming Chen, Huanqing Wang, Libing Wu & Kaixiang Peng
To cite this article: Yulin Gai, Ming Chen, Huanqing Wang, Libing Wu & Kaixiang Peng
(2026) Fixed-time tracking control of quadrotor UAVs based on disturbance observer
and sliding mode, International Journal of Systems Science, 57:3, 647-667, DOI:
10.1080/00207721.2025.2505714
To link to this article:  https://doi.org/10.1080/00207721.2025.2505714
Published online: 21 May 2025.
Submit your article to this journal 
Article views: 211
View related articles 
View Crossmark data
Citing articles: 4 View citing articles 
Full Terms & Conditions of access and use can be found at
https://www.tandfonline.com/action/journalInformation?journalCode=tsys20

## Page 2

INTERNATIONAL JOURNAL OF SYSTEMS SCIENCE
2026, VOL. 57, NO. 3, 647–667
https://doi.org/10.1080/00207721.2025.2505714
Fixed-time tracking control of quadrotor UAVs based on disturbance observer
and sliding mode
Yulin Gaia, Ming Chena, Huanqing Wangb, Libing Wuc and Kaixiang Pengd
aSchool of Electronic and Information Engineering, University of Science and Technology Liaoning, Anshan, People’s Republic of China ;
bCollege of Mathematical Sciences, Bohai University, Jinzhou, People’s Republic of China; cSchool of Science, University of Science and
Technology Liaoning, Anshan, People’s Republic of China; dSchool of Automation, University of Science and Technology Beijing, Beijing,
People’s Republic of China
ABSTRACT
A fixed-time sliding mode controller is investigated for a quadrotor Unmanned Aerial Vehicle(UAV)
with external disturbances. In order to improve the tracking performance, a double closed-loop
control structure is introduced effectively, which is divided into an inner loop and an outer loop. Fur-
thermore, non-singular terminal sliding mode (NTSM) control is used in the inner loop and the outer
loop based on a fast variable power reaching law, respectively. Additionally, the fixed-time stability
of the UAV system is proven by using Lyapunov stability theory. The proposed method’s validity
and feasibility are verified through both numerical simulation and experiment simulation. In the
numerical simulation, the performance of different sliding surfaces and reaching laws are compared,
which demonstrates the controller effectiveness. Experimental results further verify the robustness
and tracking performance of the controlled system.
ARTICLE HISTORY
Received 5 January 2024
Accepted 3 May 2025
KEYWORDS
Quadrotor UAVs; ﬁxed-time
control; sliding mode control;
fast variable power reaching
law
1. Introduction
In recent years, UAVs have become increasingly
important in today’s society and are widely utilised in
diverse fields such as agriculture, construction, logis-
tics, and rescue operations (Saleh & Hamoud, 2021;
Yang et al., 2020). Quadrotor UAVs are unmanned
aerial vehicles designed for vertical take-off and land-
ing with novel appearance and superior performance.
Compared to fixed-wing UAVs, quadrotors offer sev-
eral advantages including greater maneuverability,
high sensitivity, flexible operation and superior hover-
ing capability, as well as efficient vertical take-off and
landing (Mechali, Xu, et al., 2022). However, quadrotor
UAVs are a typical class of strongly coupled, under-
driven nonlinear systems which are greatly affected
by external disturbances. So, it is quite challenging to
design some effective controllers for these UAVs.
In the pursuit of continuously improving the flight
capability, intelligence level and safety of quadro-
tor UAVs, it is urgent to design their effective con-
trollers, which has important theoretical significance
CONTACT Ming Chen
cm8061@sina.com
School of Electronic and Information Engineering, University of Science and Technology Liaoning, Anshan,
Liaoning, People’s Republic of China
and practical value. Up to now, many mature meth-
ods have been developed including adaptive control
(Dydek et al., 2012; Jafarnejadsani et al., 2017), neu-
ral network control (K. Liu et al., 2021), backstep-
ping method (Hassani et al., 2021) and so on. In
Tang et al. (2021), a new finite-time fault-tolerant
controller is constructed for quadrotor UAVs attitude
tracking with actuator faults. Quadrotor state track-
ing is achieved by reinforcement learning techniques
in Hwangbo et al. (2017). By contrast, sliding mode
control (SMC) has become one of the most effective
means to deal with quadrotor UAVs tracking, because
it has strong robustness and excellent interference sup-
pression ability in dealing with high-order coupling
systems (Feng & Yu, 2014; Kamal et al., 2016; Moulay
et al., 2022) by altering the system structure or param-
eters and analyzing the errors based on the changes in
system state (Jiang et al., 2020; Labbadi et al., 2022;
Zhao et al., 2019). Similarly, when SMC is compared
with another non-linear control strategy such as com-
puted torque control (CTC), simulation results show
© 2025 Informa UK Limited, trading as Taylor & Francis Group

## Page 3

648
Y. GAI ET AL.
that SMC outperforms CTC in terms of tracking accu-
racy and robustness (ul Islam et al., 2014). In addi-
tion, an online adaptive scheme based on the SMC
method is proposed in B. Wang and Zhang (2017),
which not only adjusts the control gains of advanced
SMC modules seamlessly, but also reconfigures the dis-
tribution of control signals to mitigate the influence of
virtual control errors. In Mallavalli and Fekih (2020),
the authors come up with an adaptive fuzzy state
observer for quadrotor actuator fault situations, and
exploit an integrated terminal sliding mode controller.
All these methods achieve satisfactory tracking results
in numerical simulations.
However, the intricate combination of the above
algorithms and SMC greatly increases the complex-
ity of the design on the quadrotor UAV systems. In
addition, the quadrotor UAVs are strongly coupled
and underactuated, which is particularly detrimen-
tal to their application. Therefore, it is more practical
and urgent to find some SMC methods suitable for
practical use of the quadrotor UAVs.
In Raj et al. (2018), for a nonlinear high-order
flight system of fighter roll coupled maneuver, a SMC
method are designed with discontinuous law and a
super torsion continuous control law. For the ultra-
sonic glide vehicle, a new active adaptive law is added
to a continuous nonsingular terminal SMC (NTSMC),
which reduces the convergence error and chattering
in Guo et al. (2023). The NTSMC method is utilised
to achieve finite-time trajectory tracking for flexible
joint manipulators in Hong et al. (2023) and Goel
and Mobayen (2021), for the ship disturbed by ocean
currents in Cao et al. (2022), respectively. It is obvi-
ous that NTSMC is widely used in various fields, and
the method solves the singularity problem of tradi-
tional SMC. Simultaneously, in the related research of
quadrotors, Ghadiri et al. (2021) proposes an adap-
tive NTSMC approach to make the tracking achieve
finite-time stability in the quadrotor UAVs systems.
In addition, in SMC design, it is a crucial consid-
eration to improve the rate at which states conver-
gence to the sliding mode surface. The fast NTSMC
(FNTSMC) provides a dependable solution to address
the convergence rate issue. By employing an adap-
tive FNTSMC nonlinear tracking differentiator based
on a hyperbolic tangent, finite-time convergence to
the sliding mode surface is guaranteed. This improves
the system’s anti-interference ability, as mentioned
in Huang and Yang (2022). Three different forms of
adaptive FNTSMC schemes form are developed in
Lian et al. (2022), Mobayen, El-Sousy, et al. (2023), and
Lian et al. (2021), which guarantee the accurate atti-
tude tracking performance for the quadrotors. It can-
not be denied that it is very effective to slightly change
the form of the traditional sliding surface in this way
for the FNTSMC in Mobayen, Bayat, et al. (2023).
Simultaneously, the introduction of a reaching law
during the approach to the sliding surface allows for
controlled convergence rates towards the sliding sur-
face. The TSMC problem is discussed in W. W. Zhang
and Wang (2012) with the help of an example, in which
an exponential reaching law is utilised that ensures the
exponential convergence rate when the system states
are distant from the sliding mode surface. However,
when the system states approach the sliding surface,
the convergence rate does not decrease, resulting in
chattering oscillations. A dual power reaching law is
proposed by Kang et al. (2020), which accelerates con-
vergence rates when the system states are far from the
sliding mode surface and decelerates them when the
states are close to the surface. A fast reaching law based
on TSM and a nonlinear continuous terminal slid-
ing manifold are introduced in Mechali et al. (2021).
And the two reaching laws restrict each other, which
ensures that systems can reach the equilibrium point
quickly and smoothly. According to the above litera-
ture, it is necessary to design an appropriate reaching
law and combine the FNTSMC to make up for the
defect of slow convergence rate in the existing SMC. In
this paper, the adoption of a fast variable power reach-
ing law facilitates the smooth entry of system states
into the sliding mode surface.
It can be observed that the theory of finite-time
convergence of states to the sliding mode surface is
widely discussed and considered a prominent research
topic in recent years. In addition, fixed-time conver-
gence is more strict than finite-time for multiple-input
multiple-output systems, since it not only requires the
errors to converge in finite time, but also keeps the
errors within a certain range in each time interval
(Sui et al., 2022; Y.-C. Zhang et al., 2023). For exam-
ple, sliding mode control method is used to make
an underactuated nonlinear system converge in fixed
time (S. Liu et al., 2022). However, the research theory
of related fixed-time convergence is relatively lacking
in the field of quadrotor UAVs. The quadrotor UAV
system in Chen et al. (2022) only achieves fixed-time
convergence in the trajectory tracking of fractional

## Page 4

INTERNATIONAL JOURNAL OF SYSTEMS SCIENCE
649
sliding mode surface. Only by the above theory, The
FNTSMC and the fast variable power reaching law
alone are insufficient to achieve fixed-time conver-
gence. Additionally, the theoretical derivation lacks
proper handling of disturbances. For the processing
of disturbances, on the basis of NTSMC fault-tolerant
control, a disturbance observer is added to deal with
disturbances and make the quadrotor UAV systems
converge in finite time in F. Wang et al. (2022) and
Mechali, Xu, et al. (2021), and it can be seen that
the observer is an superexcellent way to estimate the
disturbances. This paper draws inspiration from the
aforementioned research and utilises a disturbance
observer to estimate disturbances. Moreover, to ensure
fixed-time convergence of quadrotor states to the slid-
ing surface, a fixed-time sliding mode controller is
constructed by combining the FNTSMC and the fast
variable power reaching law.
In dynamic and uncertain external disturbance
environments, precise trajectory tracking for quadro-
tors faces significant challenges. Therefore, conver-
gence rate becomes a critical factor. Rapid convergence
rate may lead to high-frequency chattering or jitter,
while slower convergence rate can result in delayed
system response, which may fail to meet real-time con-
trol requirements. Addressing this challenge, the main
advantage of this paper is:
(i) A FNTSMC method is proposed which enables
quadrotor UAVs to achieve attitude and trajec-
tory tracking within a fixed time, which ensures
that the state converges to the sliding mode sur-
face within a fixed time, overcomes the challenges
of traditional methods that rely on indefinite con-
vergence or require additional assumptions about
state controllability.
(ii) By integrating a disturbance observer, the sys-
tem disturbance rejection capability and robust-
ness are significantly enhanced. In the meantime,
operators are provided with real-time visibility of
disturbances affecting the system.
(iii) A fast variable power reaching law is proposed,
which provides an appropriate controller based
on the value of error. Compared to [30] and [31],
it significantly enhances the flexibility and adapt-
ability of sliding mode control and reduces chat-
tering.
The rest of the paper will be arranged: Section 3
describes the system model, presents the quadrotor
UAV tracking problem, and outlines the necessary
preliminary arguments. Section 4 introduces the pro-
posed control method. In the following section, the
controller is applied to both numerical simulations and
physical experiments, demonstrating improved track-
ing performance. The paper is concluded with a sum-
mary of the proposed method, as well as a discussion of
its limitations and possible future research directions.
2. System description
2.1. Quadrotor UAV model
Figure 1 illustrates the nonlinear rigid body model of
a quadrotor. A motor is installed at the end of the
arm of the ‘x’-shaped frame, and the propeller is fixed
on the motor rotor. Before establishing the quadro-
tor model, two 3D coordinate systems are constructed.
One is the body coordinate system, which takes the
nose direction of the quadrotor UAV as the reference,
and x-axis, y-axis and z-axis point to the right, front
and upward of the nose of the quadrotor UAV, respec-
tively. The origin of the body coordinate system always
coincides with the central position of the quadrotor
UAV, and the coordinate axis also changes with the
movement of the quadrotor UAV. The second coor-
dinate system is based on the earth’s reference with
the x-axis pointing towards the east, y-axis pointing
towards north and z-axis pointing towards the sky.
No matter how the quadrotor UAV moves, the earth
coordinate system remains unchanged. Even with the
movement of the quadrotor UAV, the earth coordinate
system remains constant. The Euler angle [φ, θ, ψ]T
expresses the vector resulting from the combination
of the solid union between the earth coordinate sys-
tem and the body coordinate system, which is used to
describe the attitude change of the quadrotor UAVs.
ω = [p, q, r]T denotes the body rotation angular veloc-
ity of the quadrotor UAV. The rotation sequence of
ZYX(Yaw-Pitch-Roll) is selected in this paper. So, the
relationship between the attitude derivative and the
rotational angular velocity of the body is as follows
ω = ˙ψRxRye3 + ˙θRxe2 + ˙φe1
(1)

## Page 5

650
Y. GAI ET AL.
Figure 1. Illustration of Quadrotor UAV.
where
Rx =
⎡
⎣
1
0
0
0
Cφ
Sφ
0
−Sφ
Cφ
⎤
⎦
represents the projection matrix of the body coordi-
nate system rotate about the x-axis,
Ry =
⎡
⎣
Cθ
0
−Sθ
0
1
0
Sθ
0
Cθ
⎤
⎦,
e1 = [1, 0, 0]T, e2 = [0, 1, 0]T, e3 = [0, 0, 1]T, S(·),
C(·) denote sin(·), cos(·). Based on this, the four
motors are represented as M1, M2, M3, M4, and M2 and
M4 rotate in a anti-clockwise direction with angular
velocities ω2 and ω4.
Assumption 2.1: The moment of inertia and mass of
the quadrotor are unchanged.
Assumption 2.2: The influence of the motor gyro
torque on the quadrotor UAV is ignored, and the quadro-
tor only receives the influence of the propeller lift, gravity,
and torque.
Based on Assumptions 2.1 and 2.2, the kinematics
and dynamics functions of the quadrotor UAV can be
written as follows Cui et al. (2021)
⎧
⎪⎪⎪⎪⎪⎨
⎪⎪⎪⎪⎪⎩
˙
V = 1
m(mge3 + FR()e3 −ktV + df )
˙P = V
˙
ω =J−1(−ω × Jω + τ + dτ −krω)
˙
 = W()ω
(2)
where P = [x, y, z]T∈R3 is used to represent the dis-
placement of the quadrotor UAV, and x, y, z are the
coordinates of the origin of the body coordinate system
on the earth coordinate system. V = [˙x, ˙y, ˙z]T∈R3,
˙x, ˙y, ˙z indicate the velocity of the quadrotor UAV in
different directions. m represents the mass of the
quadrotor and g is is the gravity coefficient, kt and kr
is resistance coefficient, J = diag[Jxx, Jyy, Jzz] ∈R3×3,
Jxx, Jyy, Jzz denote the moment of inertia, respec-
tively.  = [φ, θ, ψ]T∈R3 is the euler angle used
to represent the attitude of the quadrotor UAV.
df = [dx,dy, dz]T∈R3 and dτ = [dp, dq, dr]T∈R3 are
the system disturbance and parameter uncertainties.
R() ∈R3×3 is a rotation matrix, which represents
the conversion from the body coordinate system
to the earth coordinate system, can be denoted as
R() = RT
z RT
y RT
x , where
Rz =
⎡
⎣
Cψ
Sψ
0
−Sψ
Cψ
0
0
0
1
⎤
⎦.
W() is the matrix calculated by rotation kinematics,
and expressed as
W() =
⎡
⎢⎢⎣
1
SφTθ
CφTθ
0
Cφ
−Sφ
0
Sφ
Cθ
Cφ
Cθ
⎤
⎥⎥⎦
where T(·) denotes tan(·). The motor drives the pro-
peller to rotate, which results in a vertical body upward
lift and a torque in the same direction of rotation.
The lift forces generated by the four motors are F1,
F2, F3, F4, respectively. And the combined force is
F = F1 + F2 + F3 + F4. The total torque of the motor
can be divided into x-axis direction, y-axis direc-
tion and z-axis direction, and is expressed as τ =
[τp, τq, τr]T∈R3. The relationship between lift, torque
and propeller speed can be expressed as
⎡
⎢⎢⎣
F
τp
τq
τr
⎤
⎥⎥⎦=
⎡
⎢⎢⎣
kt
kt
kt
kt
−ktl1
ktl1
ktl1
−ktl1
ktl2
ktl2
−ktl2
−ktl2
kq
−kq
kq
−kq
⎤
⎥⎥⎦
⎡
⎢⎢⎣
ω2
1
ω2
2
ω2
3
ω2
4
⎤
⎥⎥⎦
where kq is the lift coefficient, and the resistance coef-
ficient kt reflects the throttle input of the motor; l1 and
l2 are constant length parameters for the wheelbase
dimensions of the drone arm. The speed of a single
motor is ωi, i = 1, 2, 3, 4. The reasonable PWM wave

## Page 6

INTERNATIONAL JOURNAL OF SYSTEMS SCIENCE
651
is calculated by the electric modulation, and the corre-
sponding speed is generated by issuing the instructions
to the motor.
From (2), the following state equations are obtained
⎧
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎩
˙x1 = 1
m[(Cx10Cx12Sx11 + Sx10Sx12)u1
−ktx1 + dx]
˙x2 = 1
m[(Cx10Sx11Sx12 −Cx12Sx10)u1
−ktx2 + dy]
˙x3 = 1
m[(Cx11Cx10)u1 −mg −ktx3 + dz]
˙x4 = x1
˙x5 = x2
˙x6 = x3
˙x7 = 1
Ixx
[−krx7 −x8x9(Izz −Iyy) + u2 + dp]
˙x8 = 1
Iyy
[−krx8 −x7x9(Ixx −Izz) + u3 + dq]
˙x9 = 1
Izz
[−krx9 −x7x8(Iyy −Ixx) + u4 + dr]
˙x10 = x7 + x8Sx10Tx11 + x9Cx10Tx11
˙x11 = x8Cx10 −x9Sx10
˙x12 =
1
Cx11
[x8Sx10 + x9Cx10]
(3)
where
[x1, x2, . . . , x12]T = [˙x, ˙y, ˙z, x, y, z, p, q, r, φ,
θ, ψ]T, u = [u1, u2, u3, u4]T = [F, τp, τq, τr]T.
The main objective is to develop a fixed-time sliding
mode controller for (3) that ensures precise trajec-
tory tracking within a fixed time. This approach com-
bines fast variable power reaching law with FTSMC
and incorporates a disturbance observer to enhance
robustness and accuracy. By integrating these meth-
ods, the proposed strategy aims to improve perfor-
mance and reliability in dynamic and uncertain envi-
ronments.
2.2. Mathematical preparation
Lemma 2.1 (Cui et al., 2023): Consider a nonlinear
system ˙x(t) = f (x(t)), the existence of a function V(x)
such that
˙V(x(t)) ≤−αV
m
n (x(t)) −βV
p
q (x(t)) + ϵ
(4)
where α > 0, β > 0, q>p>0, m>n>0, ϵ > 0. Then,
the origin of the nonlinear system is actual fixed-time
stable, and the settling time is
T ≤
1
α
m
n −1
 +
1
β(2
p
q −1)(1 −p
q)
(5)
Lemma 2.2 (Eliker & Zhang, 2020): Suppose ai >
0, i = 1, 2, . . . , n and 0<m<2, the following inequal-
ity is satisfied
(a2
1 + · · · + a2
n)m ≤(am
1 + · · · + am
n )2
(6)
3. Contoller design
It is challenging due to its underactuated nature
to control the quadrotor UAV model effectively. In
our design, a double closed-loop control scheme is
adopted, as shown in Figure 2. The expected output
is Pd = [xd, yd, zd]T, and the inner loop control output
XI = [x6, x10, x11, x12]T. The outer loop control output
Xo = [x4, x5]T. The expected output of x4, x5, x6, x12
are xd, yd, zd, x12d, and the expected output of φd and
θd are computed by the outer loop controller.
3.1. Inner loop
The state vector of the inner loop is
¯x = [¯x1, ¯x2, ¯x3, ¯x4, ¯x5, ¯x6, ¯x7, ¯x8]T
= [x3, x6, x7, x8, x9, x10, x11, x12]T
= [˙z, z, p, q, r, φ, θ, ψ]T
The inner loop dynamic system can be obtained
˙¯x = f1(¯x) + f2(¯x)u + ¯dI
(7)
XI = [¯x2, ¯x6, ¯x7, ¯x8]T
(8)
f1(¯x) =
⎡
⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎣
1
m[−mg −kt¯x1]
¯x1
1
Ixx
[−kr¯x3 −¯x4¯x5(Izz −Iyy)]
1
Iyy
[−kr¯x4 −¯x3¯x5(Ixx −Izz)]
1
Izz
[−kr¯x5 −¯x3¯x4(Iyy −Ixx)]
¯x3 + ¯x4S¯x6T¯x7 + ¯x5C¯x6T¯x7
¯x4C¯x6 −¯x5S¯x6
1
C¯x7
[¯x4S¯x6 + ¯x5C¯x6]
⎤
⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎦
(9)

## Page 7

652
Y. GAI ET AL.
Figure 2. Block diagram of control scheme.
f2(x) =
⎡
⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎣
1
mC¯x6C¯x7
0
0
0
0
0
0
0
0
1
Ixx
0
0
0
0
1
Iyy
0
0
0
0
1
Izz
0
0
0
0
0
0
0
0
0
0
0
0
⎤
⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎦
(10)
¯dI =
⎡
⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎣
dz
m
0
1
Ixx
dp
1
Iyy
dq
1
Izz dr
0
0
0
⎤
⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎦
(11)
From (3) and (8), we obtain
˙XI =
⎡
⎢⎢⎢⎣
¯x1
¯x3 + ¯x4S¯x6T¯x7 + ¯x5C¯x6T¯x7
¯x4C¯x6 −¯x5S¯x6
1
C¯x7 [¯x4S¯x6 + ¯x5C¯x6]
⎤
⎥⎥⎥⎦
= ϒ(¯x)
(12)
Taking the derivative of (12) to get
¨XI =
⎡
⎢⎢⎣
¨x6
¨x10
¨x11
¨x12
⎤
⎥⎥⎦= J(¯x) (f1(¯x) + f2(¯x)u) + dI
(13)
where
J(¯x) = ∂ϒ(¯x)
∂¯x
=
⎡
⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎣
1
0
0
0
0
0
0
0
0
1
0
0
0
S¯x6T¯x7
C¯x6
S¯x6
C¯x7
0
C¯x6T¯x7
−S¯x6
C¯x6
C¯x7
0
κ1
κ2
κ3
0
¯x4 sin ¯x6 + ¯x5 cos ¯x6
cos2 ¯x7
0
κ4
0
0
0
0
⎤
⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎦
T
(14)
with
κ1 = ¯x4C¯x6T¯x7 −¯x5S¯x6T¯x7,
κ2 = −¯x4S¯x6
−¯x5C¯x6, κ3 =
1
C¯x7 [¯x4C¯x6 −¯x5S¯x6], κ4 = Sx7
C2
¯x7
[¯x4S¯x6 +
¯x5C¯x6], dI = [di,1, di,2, di,3, di,4]T = J(¯x)¯dI. Define the
inner loop control output XId = [x6d, x10d, x11d, x12d]T
= [zd, φd, θd, ψd]T.
Remark 3.1: The four actual inputs of the quadro-
tor are designed in the inner loop, which allows the
inner loop control system to focus on fast response and
stability, while the outer loop focuses on higher level
trajectory adjustment. Secondly, this design can bal-
ance the control needs of the two links, which helps to
achieve a more refined and effective control strategy.
Now, we define

ei1 = XI −XId
ei2 = ˙XI −˙XId
(15)
where
ei1 = [ei1,1, ei1,2, ei1,3, ei1,4]T, ei2 = [ei2,1, ei2,2,
ei2,3, ei2,4]T.
Thereafter, (15) can be re-expressed as
⎧
⎪⎨
⎪⎩
˙ei1 = ei2 = ϒ(¯x) −˙XId
˙ei2 = ¨XI −¨XId
= J(¯x) (f1(¯x) + f2(¯x)u) + dI −¨XId
(16)

## Page 8

INTERNATIONAL JOURNAL OF SYSTEMS SCIENCE
653
Firstly, suppose
m =
⎡
⎢⎢⎢⎣
m1
m2
...
mn
⎤
⎥⎥⎥⎦∈Rn,
in order to avoid taking an even root of a negative
number, we define
sig(m)k = [|m1|ksign(m1), |m2|ksign(m2), . . . ,
|mn|ksign(mn)]T
(17)
where k>0. Next, a sliding mode surface can be
selected as
SI = ei1 + k1sig(ei1)a1 + k2sig(ei2)a2
(18)
where SI = [si1, si2, si3, si4]T, k1 > 0, k2 > 0, a1, a2 are
the ratios of two positive odd numbers, and 1 < a2 <
a1 < 2.
Remark 3.2: (1) The parameters a1 and a2 in the
sliding surface are chosen as the ratio of two posi-
tive odd numbers. This is to ensure that the partial
derivatives of the sliding surface are positive in the sub-
sequent process. Specifically, since 1 −a1 is the differ-
ence between a ratio of even and odd numbers. When
calculating the partial derivatives, this results in an
even power operation, which guarantees that the out-
come is positive, thus ensuring the positive of the par-
tial derivatives. 2)The fixed-time stability of the sliding
surface is indirectly related to the power difference of
two orders between ei1 and ei2, as will be reflected in
the subsequent proof. For example, the power differ-
ence between ei1 and sig(ei2)a2 ensures the conver-
gence time when the error is small, while the power
difference between sig(ei1)a1 and sig(ei2)a2 ensures the
convergence time when the error is large. In contrast,
the linear sliding mode surface can hardly guarantee
the convergence time (W. W. Zhang & Wang, 2012).
In conclusion, the sliding surface design proposed is
reasonable.
Taking the derivative of (18), we can get
˙SI = ei2 + k1a1diag(sig(ei1))a1−1)ei2
+ k2a2diag(sig(ei2)a2−1)(J(¯x)(f1(¯x)+
+ f2(¯x)u) + dI −¨XId)
(19)
To achieve faster and smoother entry of the system
states into the sliding mode surface, a novel approach is
employed by utilising a new fast variable power reach-
ing law. This reaching law combines the advantages
of both the fast power reaching law and the double
power reaching law. This reaching law formulation
helps to expedite the system’s convergence to the slid-
ing mode while ensuring a smooth transition. By com-
bining these reaching laws, the control system achieves
improved performance and reduces chattering. The
reaching law is made up of
˙SI = −ξ1sig(SI)γ1 −ξ2sig(SI)γ2 −ξ3sig(SI)γ3
(20)
where ξ1 > 0, ξ2 > 0, ξ3 > 0, γ1 > 1, 0 < γ2 < 1, and
γ3 is given by
γ3 =

1,
∥SI∥≥1
,
∥SI∥< 1
,
0 <  < 1.
It should be noted that (19) represents the derivative of
the sliding surface which provides the information on
the evolution of the sliding surface condition and the
manifestation of its convergence rate. In contrast, the
dynamics in (20) represent the desired convergence
rate of the state to the sliding surface, and it describes
the fundamental dynamics after control is applied. The
objective is to evolve the dynamics in (19) to the con-
vergence rate described in (20) through the design of
the control law.
Remark 3.3: As shown in Figure 3, the response speed
of the system can be accelerated by increasing ξ2 and
γ2 in different conditions away from the sliding mode
surface and close to it. Adjusting ξ1 and γ1 when near
the sliding mode surface can adjust the response speed
of the system. And at the same time, the introduction
of ξ3 and γ3 also makes the system more flexible. For
the quadrotor system, since the error and the control
moment are not linear, it is more necessary to adjust
the convergence speed of different error intervals. Fur-
thermore, compared to the sign reaching law and non-
linear sign reaching law, such as ˙s = −k1sign(s)α −
k2sign(s)β (Mechali, Xu, et al., 2022), the fast vari-
able power reaching law is continuous and control-
lable, which significantly reduces chattering during the
sliding mode process. This help the quadrotor system
to transition to the sliding mode surface faster and
smoother.

## Page 9

654
Y. GAI ET AL.
Figure 3. Control input of Example 4.2.
Since the states can be observed or calculated, a
disturbance observer is established
˙ZI = −kIb ˆdI + kIbJ(¯x)(f1(¯x) + f2(¯x)u)
(21)
where kIb > 0, ˆdI = [ˆdi,1, ˆdi,2, ˆdi,3, ˆdi,4]T. Then, dI can
be estimated as
ˆdI = J−1(¯x) (kIbϒ(¯x) + ZI)
(22)
The disturbance estimated by the observer can be
approximately equal to the actual disturbance dI, and
the specific proof is given in R. Wang et al. (2021).
The inner loop control laws is designed as
u = ui,1 + ui,2
(23)
ui,1 = −f−1
2 (¯x)J−1(¯x)(ˆdI + J(¯x)f1(¯x)
−¨XId + k−1
2 a−1
2 (sig(ei2)2−a2
+ k1a1diag(sig(ei1)a1−1)sig(ei2)2−a2))
(24)
ui,2 = −f−1
2 (¯x)J−1(¯x)(ξ1sig(SI)γ1
+ ξ2sig(SI)γ2 + ξ3sig(SI)γ3)
(25)
where ui,1 is equivalent control, ui,2 is manifold con-
trol.
Theorem 3.1: For the quadrotor inner loop system (7)
under Assumptions (2.1)–(2.2), when the reaching
law (20)) and control laws (23))–(25)) are used, the
tracking error finally approaches the small neighbour-
hood around the origin in fixed time, and the upper
bound of the fixed time is
Ti ≤Ti,0 +
1
2
γ1+1
2 ξ1λ1 min

γ1+1
2
−1

+
1
2
γ ∗+1
2 ξ∗λ1 min(2
γ ∗+1
2
−1)(1 −2
γ ∗+1
2 )
(26)
where
2
γ ∗+1
2 ξ∗V
γ ∗+1
2
1
= max(2
γ2+1
2 ξ2V
γ2+1
2
1
, 2
γ3+1
2 ξ3
V
γ3+1
2
1
), Ti,0 will be described later.
Proof: Selecting the following Lyapunov candidate
function
V1 = 1
2ST
I SI
(27)
Taking the derivative of (27) gets
˙V1 = ST
I (ei2 + k1a1diag(sig(ei1)a1−1)ei2
+ k2a2diag(sig(ei2)a2−1)J(¯x)(f1(¯x)
+ f2(¯x)u) + dI −¨XId)
(28)
Plugging (23) and (24) into (28), we obtain
˙V1 = ST
I

k1a1diag(sig(ei1)a1−1)ei2
+k2a2diag(sig(ei2)a2−1)
J(¯x)(f1(¯x) + f2(¯x)(−f−1
2 (¯x)J−1(¯x)(J(¯x)f1( ¯x)
+ k−1
2 a−1
2 (k1a1diag(sig(ei1)a1−1)sig(ei2)2−a2
+ sig(ei2)2−a2) + ¨XId −ˆdI) + ui,2) + ei2
+dI −¨XId

(29)
Then, through a simple computation, one has
˙V1 = ST
I (k2a2diag(sig(ei2)a2−1)(J(¯x)f2(¯x)ui,2)) (30)
Substituting (25) into (30) results in
˙V1 = −ST
I (k2a2diag(sig(ei2)a2−1)(ξ1sig(SI)γ1
+ ξ2sig(SI)γ2 + ξ3sig(SI)γ3))
(31)
Then (31) can be converted into the following the form
˙V1 = −k2a2ξ1(sig(ei2)a2−1)Tsig(SI)γ1+1
−k2a2ξ2(sig(ei2)a2−1)Tsig(SI)γ2+1
−k2a2ξ3(sig(ei2)a2−1)Tsig(SI)γ3+1
(32)
Next, in view of diag(ei2), two different cases are dis-
cussed. (1) When diag(ei2) is a full rank matrix, we

## Page 10

INTERNATIONAL JOURNAL OF SYSTEMS SCIENCE
655
make
k2a2diag(sig(ei2)a2−1) = ϱ1 = diag[ϱ1,1, ϱ1,2,
ϱ1,3, ϱ1,4, ]T, and λ1 min is the minimum eigenvalue of
ϱ1.
■
Through systematic derivation and analysis, the
equivalent control term has been effectively eliminated
in the design of the sliding mode control law, leav-
ing only the switching term that dominates the control
strategy. This indicates that the reaching law (20) plays
a central role in this control strategy, ensuring that
the system state approaches the sliding surface at the
desired rate. According to Lemma 2.2, (32) is reduced
to
˙V1 ≤−ξ1∥ϱ1∥· ||SI||
γ1+1
2
−ξ2∥ϱ1∥· ∥SI∥
γ2+1
2
−ξ3∥ϱ1∥· ∥SI∥
γ3+1
2
(33)
After a simple transformation, (34) is obtained
˙V1 ≤−2
γ1+1
2 ξ1λ1 minV
γ1+1
2
1
−2
γ ∗+1
2 ξ∗λ1 minV
γ ∗+1
2
1
(34)
where
2
γ ∗+1
2 ξ∗V
γ ∗+1
2
1
= max(2
γ2+1
2 ξ2V
γ2+1
2
1
, 2
γ3+1
2 ξ3
V
γ3+1
2
1
). Thus, the state fixed-time arrival at the sliding
surface can be achieved when diag(ei2) is a full rank
matrix.
(2) When diag(ei2) is a rank-deficient matrix, there
exists at least one j ∈{1, 2, 3, 4} such that ei2,j = 0,
which may hinder the reachability of NTSM. We will
show that ei2,j = 0
is not an attractor in reaching
phase. Substituting the (23) into ˙ei2 yields
˙ei2 = k−1
2 a−1
2
sig(ei2)2−a1 −ξ1 sig(SI)γ1
+ k2a2 diag(sig(ea1−1
i1
)) sig(ei2)2−a
−ξ2 sig(SI)γ2 −ξ3 sig(SI)γ3
(35)
In the case of ei2,j = 0 and ei1,j ̸= 0, we have
¨ei1,j = −
3

k=1
ξk sig(ei1,j + k1 sig(ei1,j)a1)γk ̸= 0 (36)
It shows that ei2,j = 0 is not an attractor (Feng
& Man, 2002; Yu et al., 2005). Therefore, the fixed-time
stability is still guaranteed. This implies that around
ei2,j = 0, there is a neighbourhood where, for a small
ϱ1,j > 0, if |ei2,j| < ϱ1,j. In addition, compared to the
design where sign(si) is chosen in the reaching law
(Mechali, Xu, et al., 2022; W. W. Zhang & Wang, 2012),
the ˙ei2,j is manifold type rather than switching type,
which reduces chattering.
When the system states reaches the sliding mode
surface
ei2 = −
 1
k2
 1
a2 sig (ei1)
1
a2 −
k1
k2
 1
a2 sig(ei1)
a1
a2
(37)
Thereby, the following Lyapunov function is selected
V0 = 1
2eT
i1ei1
(38)
The time derivative of (38) is
˙V0 = −
 1
k2
 1
a2 ||ei1||
1+a2
a2 −
k1
k2
 1
a2 ||ei1||
a1+a2
a2
(39)
According to Lemma 2.2, (39) is further written as
˙V0 ≤−α0V
1+a2
2a2
0
−β0V
a1+a2
2a2
0
(40)
where α0 = 2
1+a2
2a2 k
−1
a2
2
, β0 = 2
a1+a2
2a2 (k1
k2 )
1
a2 . So, the
convergence time of the inner sliding mode phase
is Ti,0 ≤
2a2
α0(a1−a2) +
2a2
β0(a2−1). Then, according to
Lemma 2.1 and (37)–(39), the fixed time for conver-
gence is computed as
Ti ≤Ti,0 +
1
2
γ1+1
2 ξ1λ1 min

γ1+1
2
−1

+
1
2
γ ∗+1
2 ξ∗λ1 min(2
γ ∗+1
2
−1)(1 −2
γ ∗+1
2 )
(41)
Figure 4 shows the phase plane of the sliding mode
process, where j ∈{1, 2, 3, 4}. When the state is in the
first or third quadrant, it will move to the second or
fourth quadrant, respectively. Even when ei2,j = 0, the
motion speed of ei2,j will differ depending on the sign
of ei1,j. The convergence rate of the sliding mode pro-
cess before reaching the sliding surface is determined
by the variable power reaching law, which ensures
fixed-time convergence while allowing the conver-
gence rate to be adjustable based on the error. After
reaching the sliding surface, the inner loop error fixed-
time converges to a region close to zero along the
sliding surface.

## Page 11

656
Y. GAI ET AL.
Figure 4. Phase plane of sliding mode process.
3.2. Outer loop
The outer loop dynamics can be described as
˙Xo1 =
˙˘x1
˙˘x2

= 1
m
(Cx10Cx12Sx11 + Sx10Sx12)u1 −kt˘x1
(Cx10Sx11Sx12 −Cx12Sx10)u1 −kt˘x2

+ 1
m
dx
dy

= u1
m
Cx12
Sx12
Sx12
−Cx12
 Cx10Sx11
Sx10

+ 1
m
dx
dy

−kt
m
˘x1
˘x2

= ϕ(x12)uo + ¯do + λXo1
(42)
˙Xo2 =
˙˘x3
˙˘x4

=
˘x1
˘x2

(43)
where [˘x1, ˘x2, ˘x3, ˘x4]T = [x1, x2, x4, x5]T = [˙x, ˙y, x, y]T,
ϕ(x12) = u1
m
 Cx12
Sx12
Sx12 −Cx12

, ¯do = 1
m[dx, dy]T, λ = −kt
m,
Xo1 = [˘x1, ˘x2]T, Xo2 = [˘x3, ˘x4]T. Selecting the virtual
control law uo = [˘u1, ˘u2]T =

cos x10 sin x11
sin x10

. Assume
that the inner loop runs faster than the outer loop, and
redefine
˘u = [˘u1, ˘u2]T
(44)
Xo2 = [˘x3, ˘x4]T
(45)
Xod = [x4d, x5d]T = [xd, yd]T
(46)
And we define

eo1 = Xo2 −Xod
eo2 = Xo1 −˙Xod
(47)
Then, (47) can be re-expressed as
⎧
⎪⎨
⎪⎩
˙eo1 = eo2 = Xo1 −˙Xod
˙eo2 = ˙Xo1 −¨Xod
= ϕ(x12)uo + ¯do + λXo1 −¨Xod
(48)
Next, the sliding mode surface can be selected as
So = eo1 + ˘k1sig(eo1)˘a1 + ˘k2sig(eo2)˘a2
(49)
with So = [so1, so2, so3]T, ˘k1 > 0, ˘k2 > 0, ˘a1, ˘a2 are the
ratios of two positive odd numbers, and 1 < ˘a2 <
˘a1 < 2.
Taking the derivative of (49), we can get
˙So = eo2 + ˘k1˘a1diag(eo1)˘a1−1eo2 + ˘k2˘a2diag(eo2)˘a2−1
(ϕ(x12)uo + ¯do + λXo1 −¨Xod)
(50)
The reaching law is made up of
˙So = −˘ξ1sig(So) ˘γ1 −˘ξ2sig(So) ˘γ2 −˘ξ3sig(So) ˘γ3 (51)
where ˘ξ1 > 0, ˘ξ2 > 0, ˘ξ3 > 0, ˘γ1 > 1, 0 < ˘γ2 < 1, and
˘γ3 is given by
˘γ3 =

1,
∥So∥≥1
˘,
∥So∥< 1
,
0 < ˘ < 1.
Similarly, a disturbance observer is established by
˙Zo = −kob ˆdo + kob(λXo1 + ϕuo)
(52)
where kob > 0, ˆdo = [ˆdo,1, ˆdo,2]T. Then, from (52), one
has
ˆdo = kobXo1 + Zo
(53)
The outer loop control laws is designed as
uo = ˘u1 + ˘u2
(54)
˘u1 = −ϕ−1(λXo1 −¨Xod + ˆdo + ˘k−1
2 ˘a−1
2
(sig(eo2)2−a′
2 + ˘k1˘a1diag(sig(eo1)a′
1−1)
sig (eo2)2−a′
2))
(55)
˘u2 = −ϕ−1(˘ξ1sig(So) ˘γ1 + ˘ξ2sig(So) ˘γ2
+ ˘ξ3sig(So) ˘γ3)
(56)

## Page 12

INTERNATIONAL JOURNAL OF SYSTEMS SCIENCE
657
where ˘u1 is equivalent control, ˘u2 is manifold control.
Theorem 3.2: For the quadrotor outer loop sys-
tem (42), when the reaching law (51) and control
laws (54)–(56) are used, then the tracking error finally
approaches the small neighbourhood around the origin
in fixed time, and the upper bound of the fixed time is
To ≤To,0 +
1
2
˘γ1+1
2
˘ξ1˘λ1 min

˘γ1+1
2
−1

+
1
2
˘γ ∗+1
2
˘ξ∗˘λ1 min(2
˘γ ∗+1
2
−1)(1 −2
˘γ ∗+1
2 )
Proof: Selecting the following Lyapunov candidate
function
V2 = 1
2ST
o So
(57)
Taking the derivative of (57) to get
˙V2 = ST
o (eo2 + ˘k1˘a1diag(sig(eo1)˘a1−1)eo2
+ ˘k2˘a2diag(sig(eo2)˘a2−1)(ϕ(x12)uo
+ ¯do + λXo1 −¨Xod))
(58)
Plugging (54) and (55) into (58), we obtain
˙V2 = ST
o (eo2 + ˘k1˘a2diag(sig(eo1)˘a2−1)eo2
+ ˘k2˘a2diag(sig(eo2)˘a2−1)
(ϕ(x12)((−ϕ−1(x12)(λXo1
+ ˆdo −¨Xod + ˘k−1
2 ˘a−1
2 (sig (eo2)2−˘a2
+ ˘k1˘a1diag(sig(eo1)a′
1−1)sig (eo2)2−˘a2))) + ˘u2)
+ ¯do + λXo1 −¨Xod))
(59)
Furthermore, through a simple computation, one has
˙V2 = ST
o (˘k2˘a2diag(sig(eo2)˘a2−1)(ϕ(x12)˘u2))
(60)
Substituting (56) into (60) results in
˙V2 = ST
o (˘k2˘a2diag(sig(eo2)˘a2−1)(ϕ(x12)(−ϕ−1(x12)
(˘ξ1sig(So) ˘γ1 + ˘ξ2sig(So) ˘γ2 + ˘ξ3sig(So) ˘γ3))))
(61)
Afterward (61) can be converted into
˙V2 = −˘k2˘a2˘ξ1(sig(eo2)˘a2−1)Tsig(So) ˘γ1+1
−˘k2˘a2˘ξ2(sig(eo2)˘a2−1)Tsig(So) ˘γ2+1
−˘k2˘a2˘ξ3(sig(eo2)˘a2−1)Tsig(So) ˘γ3+1
(62)
We make ˘k2˘a2diag(sig(eo2)˘a2−1) = ˘ϱ1, ˘λ1 min is the
minimum eigenvalue of ˘ϱ1. According to Lemma 2.2,
˙V2 is rewritten as
˙V2 = −˘ξ1∥˘ϱ1∥· ∥So∥
˘γ1+1
2
−˘ξ2∥˘ϱ1∥· ∥So∥
˘γ2+1
2
−˘ξ3∥˘ϱ1∥· ∥So∥
˘γ3+1
2
(63)
Consequently, we get
˙V2 ≤−2
˘γ1+1
2
˘ξ1˘λ1 minV
˘γ1+1
2
2
−2˘λ1 min · 2
˘γ ∗+1
2
˘ξ∗V
˘γ ∗+1
2
2
(64)
where 2
˘γ ∗+1
2
˘ξ∗V
˘γ ∗+1
2
2
= max(2
γ2+1
2
˘ξ2V
γ2+1
2
1
, 2
γ3+1
2
˘ξ3
V
γ3+1
2
1
). When the system state reaches the slid-
ing mode surface, same thing as (37)–(39), the
convergence time of the outer sliding mode phase
is To,0 ≤
2˘a2
˘α0(˘a1−˘a2) +
2˘a2
˘β0(˘a2−1), where ˘α0 = 2
1+˘a2
2˘a2 k
−1
˘a2
2
,
β0 = 2
˘a1+˘a2
2˘a2 (
˘k1
k2 )
1
˘a2 . Then, according to Lemma 2.1, the
following equality is true.
To ≤To,0 +
1
2
˘γ1+1
2
˘ξ1˘λ1 min

˘γ1+1
2
−1

+
1
2
˘γ ∗+1
2
˘ξ∗˘λ1 min(2
˘γ ∗+1
2
−1)(1 −2
˘γ ∗+1
2 )
(65)
Thus, Theorems 3.1–3.2 are proved. In conclusion, in
traditional underactuated system control, the conver-
gence of uncontrollable states is often addressed by
controlling the controllable states without considering
the convergence time of the uncontrollable states. The-
orems 3.1–3.2 avoids this issue by ensuring fixed-time
convergence and guaranteeing stable tracking perfor-
mance. Additionally, the disturbance observer not only
enhances robustness but also provides real-time feed-
back on disturbances, enabling operators to monitor
and adjust system behaviour, which further improves
both stability and practical usability.
■
4. Numerical simulation and experiment
simulation
In order to demonstrate the effectiveness of the devel-
oped method, numerical simulation and experiment
are carried out, respectively.

## Page 13

658
Y. GAI ET AL.
Table 1. System parameters.
Parameter
Description
Value
Unit
m
Mass
2.6
kg
Jx
Rotational Inertia
0.0291
kg · m2
Jy
Rotational Inertia
0.0291
kg · m2
Jz
Rotational Inertia
0.0467
kg · m2
kr
Drag Coeﬃcient
0.006
N · m/s
kt
Drag Coeﬃcient
0.006
N · m/s
d
Lift Coeﬃcient
0.0048
N · m/rad2
l
Distance
0.225
m
4.1. Numerical simulation
A numerical simulation is conducted in this paper by
using the Runge-Kutta method within the MATLAB
environment. The fixed time step is set to 0.004 s. And
the system parameters are given in Table 1.
In addition, the design parameters of the outer loop
controller are selected as: ξ1 = 1.055, ξ2 = 5.117, ξ3 =
0.098, γ1 = 1.2, γ2 = 0.99, γ3 = 0.99, k1 = 4.271,
k2 = 6.275, a1 = 137/125, a2 = 133/125.
And
the
design parameters of the inner loop controller are
selected
as
follows:
˘ξ1 = 2.07, ˘ξ2 = 0.0215, ˘ξ3 =
0.079, ˘γ1 = 1.01, ˘γ2 = 0.39, ˘γ3 = 0.99, ˘k1 = 4, ˘k2
= 4, ˘a1 = 195/101, ˘a2 = 1843/999. Since there is no
need to have too much requirement on yaw angle
when tracking the expected signal of the trajectory,
the expected signal of the yaw angle is always 0 in
the simulation. The drone is required to draw an ‘8’
shape track in the air at a fixed height of 1 meter, then
the expected trajectory is mathematically expressed as
[xd, yd, zd, ψd]=[sin(0.09t), sin(0.18t), 1, 0]T. To com-
pare our proposed method with those from other
literatures, the control methods from W. W. Zhang
and Wang (2012) and Kang et al. (2020) are applied
to the model used in this study by using the dou-
ble closed-loop solving approach and disturbance
observer described in this paper. The controller
form of exponential reaching law in W. W. Zhang
and Wang (2012) is as follows.
Si,[30] = ei1 + sig(ei2)1.66
ui,[30] = f−1
2 (¯x)J−1(¯x)( ¨XId −ˆdI −J(¯x)f1(¯x)
−0.6sig(ei2)0.44 −10Si,[30]
−0.015sgn

Si,[30]

)
The controller form of linear sliding mode surface
combined with dual power reaching law in Kang
et al. (2020) is
Si,[31] = ei1 + ei2
Figure 5. Trajectory tracking graph of the quadrotor.
ui,[31] = f−1
2 (¯x)J−1(¯x)( ¨XId −ˆdI −J(¯x)f1(¯x)
−sig(ei2) −1.5sig

So,[31]
0.75
−0.8sig

So,[31]
0.8
The above parameters are all referenced from the
original literature to ensure fairness and consis-
tency in the comparison. In addition, in order to
show the diversity of disturbances, the disturbance is
set to df = [e−(t−10)2 −2 e−(t−50)2 + e−(t−70)2
10
, e−t +
e−(t−50)2
50
, 0.05 sin(t/100)]T,
dτ = [0.03 sin(t), 0.03, 2
(sin(t/100))]T. In theory, the control law is large
enough to make the system stable, but it is not prac-
tical. To avoid this input saturation, the maximum
acceleration set in the vertical earth coordinate sys-
tem is 4, and the maximum torque calculated in radi-
ans is 0.18. Figure 5 depicts the tracking results by
using 3D space representation. And Figure 6 shows
the tracking performance of the proposed algorithm
compared with the methods selected from literatures
(Kang et al., 2020; W. W. Zhang & Wang, 2012). It is
easy to find that the simple exponential reaching law
is difficult to control the convergence speed, so the
tracking effect in the quadrotor system has a small
amplitude of chattering. Especially in the y-axis and
z-axis directions, the linear sliding surface in Kang
et al. (2020) results in slower tracking speed. At the
same time, the fast variable power reaching law and the
dual power reaching law in this paper can ensure that
the quadrotor system has good tracking performance.
The control inputs in Figure 7 shows that the buffeting

## Page 14

INTERNATIONAL JOURNAL OF SYSTEMS SCIENCE
659
Figure 6. Position tracking performance.
Figure 7. Control input.

## Page 15

660
Y. GAI ET AL.
Figure 8. Attitude response trajectory.
Figure 9. Disturbance and disturbance observer of outer loop.
input in this paper is smaller than the other two meth-
ods. This advantage is due to the adjustable conver-
gence speed when the error is near the sliding surface
in fast variable power reaching law, which makes the
control input of the calculation with small error more
reasonable and reduces the input buffeting. In contrast,
the method in W. W. Zhang and Wang (2012) uses
a switching-type reaching law (sign function), which
leads to higher chattering due to the abrupt switching
nature of the control inputs as the system approaches

## Page 16

INTERNATIONAL JOURNAL OF SYSTEMS SCIENCE
661
Figure 10. Disturbance and disturbance observer of inner loop.
Figure 11. Experimental platform.
the sliding surface. Figure 8 shows the change of the
attitude information of the quadrotor, while Figures 9
and 10 only show the observed disturbance value and
the actual given value in this paper. Thus, the suggested
control approach can attain satisfactory tracking per-
formance.
4.2. Example simulation
To further confirm the efficacy of the proposed design
approach, the inner loop attitude control is taken as an
example. Its application to an actual physical platform
is demonstrated – the quadrotor experimental plat-
form of Beijing Links Tech Co., Ltd from Figure 11
Our experimental platform is technically limited and
can only verify the tracking effect of the attitude loop.
In the attitude of the inner loop, the value of the con-
troller u1 is given as a fixed value, and the z-axis
does not participate in the matrix operation, only the
information about the Euler Angle and the controller
torque participate in the operation. And the first 10 s
for the preparation phase, the system from 10 s to
run. Since the parameters have been validated through
numerical simulation, the experimental parameters
are selected to match those from the simulation before
being applied to the actual system.
Example 4.1: The objective of this experiment is
to evaluate the performance of the fixed-time con-
troller in terms of its ability to achieve fixed-time
convergence of the tracking error. To achieve this,
the air blower is turned off, isolating the quadro-
tor from external airflow disturbances. This setup
allowed for a focussed assessment of the fixed-time
controller’s ability to ensure that the tracking error
converges to zero within a fixed time, even in the pres-
ence of uncertainty of parameters. The expected out-
put is [φd, θd, ψd]T = [0.23 sin
πt
3

, 0.3 cos
πt
5

, 0]T.
Figures 12–14 demonstrate the actual tracking effect.

## Page 17

662
Y. GAI ET AL.
Figure 12. Actual system attitude tracking of Example 4.1.
Figure 13. Actual system control input of Example 4.1.
The quadrotor system is very sensitive to the con-
troller. It can be seen from Figure 12 that the three
attitude angles of the quadrotor are well tracked to
the expected output, similar to the results shown in
Figure 6. In practice, an attitude tracking error of less
than 0.05 rad is considered reasonable. In Figure 13,
the controller fluctuates within an acceptable small
range. From Figure 14, we can see the uncertainty of
parameters observed by the disturbance observer for
the actual state output.

## Page 18

INTERNATIONAL JOURNAL OF SYSTEMS SCIENCE
663
Figure 14. Disturbance observer of Example 4.1.
Figure 15. Actual system attitude tracking of Example 4.2.
Example 4.2: In order to further demonstrate the
immunity of sliding mode control and disturbance
observer, the expected output is re-selected as
[φd, θd, ψd]T = [0, 0, 0]T. As shown in Figure 15,
within five seconds, the quadrotor reaches a stable
state. At around 16 s, 24 s, 27 s, 32 s, and 37 s, the
quadrotor is subjected to external disturbances gen-
erated by an air blower, which is directed at different
faces of the quadrotor. Although the exact magni-
tude of these disturbances is not directly measured,

## Page 19

664
Y. GAI ET AL.
Figure 16. Disturbance observer of Example 4.2.
Figure 17. Actual system control input of Example 4.2.
their impact is estimated by the disturbance observer,
which compensates for the disturbances in real-time.
This is illustrated in Figure 16, where the values
observed by the disturbance observer closely resemble
the compensation effect shown in the numerical simu-
lation, indicating accurate disturbance compensation.

## Page 20

INTERNATIONAL JOURNAL OF SYSTEMS SCIENCE
665
Furthermore, the control input, shown in Figure 17,
adjusts accordingly to stabilise the system after each
disturbance.
5. Conclusion
This study focuses on addressing the fixed-time track-
ing control challenge for quadrotor UAVs. The intro-
duction of NTSM mode control with a fast variable
power reaching law aims to tackle the complex tra-
jectory and attitude tracking issues in quadrotor UAV
systems. Simulation results confirm the feasibility of
trajectory tracking, while experimental validation sup-
ports the feasibility of attitude tracking. Compared to
previous algorithms, the proposed sliding mode con-
trol demonstrates a significant improvement in reduc-
ing chattering. Next work will concentrate on refining
the sliding mode controller to acquire better perfor-
mance.
Disclosure statement
The authors state that they have no known competing financial
interests or personal relationships that could have influenced
the findings presented in this paper.
Funding
This work was supported in part by the National Natural Sci-
ence Foundation of China under Grant U21A20483, 61873024,
62173046 and 61773072 and LiaoNing Revitalization Talents
Program under Grant XLYC2402002.
Data availability statement
No data was utilised in the research mentioned in the article.
References
Cao, G., Li, Z., Yang, Y., & Zhang, W. (2022). Barrier function-
based adaptive fast non-singular terminal sliding mode
tracking control for marine vessels. Ocean Engineering, 266,
Article
112851.
https://doi.org/10.1016/j.oceaneng.2022.
112851
Chen, D., Zhang, J., & Li, Z. (2022). A novel fixed-time tra-
jectory tracking strategy of unmanned surface vessel based
on the fractional sliding mode control method. Electronics,
11(5), 726. https://doi.org/10.3390/electronics11050726
Cui, L., Zhang, R., Yang, H., & Zuo, Z. (2021). Adaptive super-
twisting trajectory tracking control for an unmanned aerial
vehicle under gust winds. Aerospace Science and Technol-
ogy, 115, Article 106833. https://doi.org/10.1016/j.ast.2021.
106833
Cui, L., Zhou, Q., & Huang, D. (2023). Fixed-time dis-
turbance observer based distributed cooperative contain-
ment control with fixed-time anti-saturation compensator
for mult-unmanned aerial vehicles. International Journal
of Robust and Nonlinear Control, 33(17), 10584–10605.
https://doi.org/10.1002/rnc.v33.17
Dydek, Z. T., Annaswamy, A. M., & Lavretsky, E. (2012).
Adaptive control of quadrotor UAVs: A design trade study
with flight evaluations. IEEE Transactions on Control Sys-
tems Technology, 21(4), 1400–1406. https://doi.org/10.1109/
TCST.2012.2200104
Eliker, K., & Zhang, W. (2020). Finite-time adaptive integral
backstepping fast terminal sliding mode control application
on quadrotor UAV. International Journal of Control, Automa-
tion and Systems, 18(2), 415–430. https://doi.org/10.1007/
s12555-019-0116-3
Feng, Y., Han, F., & Yu, X. (2014). Chattering free full-
order sliding-mode control. Automatica, 50(4), 1310–1314.
https://doi.org/10.1016/j.automatica.2014.01.004
Feng, Y., Yu, X., & Man, Z. (2002). Non-singular terminal slid-
ing mode control of rigid manipulators. Automatica, 38(12),
2159–2167. https://doi.org/10.1016/S0005-1098(02)00147-4
Ghadiri, H., Emami, M., & Khodadadi, H. (2021). Adap-
tive super-twisting non-singular terminal sliding mode con-
trol for tracking of quadrotor with bounded disturbances.
Aerospace Science and Technology, 112, Article 106616.
https://doi.org/10.1016/j.ast.2021.106616
Goel, A., & Mobayen, S. (2021). Adaptive nonsingular
proportional–integral–derivative-type
terminal
sliding
mode tracker based on rapid reaching law for nonlin-
ear systems. Journal of Vibration and Control, 27(23-24),
2669–2685. https://doi.org/10.1177/1077546320964287
Guo, R., Ding, Y., & Yue, X. (2023). Active adaptive continu-
ous nonsingular terminal sliding mode controller for hyper-
sonic vehicle. Aerospace Science and Technology, 137, Article
108279. https://doi.org/10.1016/j.ast.2023.108279
Hassani, H., Mansouri, A., & Ahaitouf, A. (2021). Robust
autonomous flight for quadrotor UAV based on adaptive
nonsingular fast terminal sliding mode control. Interna-
tional Journal of Dynamics and Control, 9(2), 619–635.
https://doi.org/10.1007/s40435-020-00666-3
Hong, M., Gu, X., Liu, L., & Guo, Y. (2023). Finite time extended
state observer based nonsingular fast terminal sliding mode
control of flexible-joint manipulators with unknown dis-
turbance. Journal of the Franklin Institute, 360(1), 18–37.
https://doi.org/10.1016/j.jfranklin.2022.10.028
Huang, S., & Yang, Y. (2022). Adaptive neural-network-
based nonsingular fast terminal sliding mode control for
a quadrotor with dynamic uncertainty. Drones, 6(8), 206.
https://doi.org/10.3390/drones6080206
Hwangbo, J., Sa, I., Siegwart, R., & Hutter, M. (2017). Control
of a quadrotor with reinforcement learning. IEEE Robotics
and Automation Letters, 2(4), 2096–2103. https://doi.org/10.
1109/LRA.2017.2720851
Jafarnejadsani, H., Sun, D., Lee, H., & Hovakimyan, N. (2017).
Optimized L 1 adaptive controller for trajectory track-
ing of an indoor quadrotor. Journal of Guidance, Control,

## Page 21

666
Y. GAI ET AL.
and Dynamics, 40(6), 1415–1427. https://doi.org/10.2514/1.
G000566
Jiang, B., Karimi, H. R., Yang, S., Gao, C., & Kao, Y.
(2020). Observer-based adaptive sliding mode control
for nonlinear stochastic Markov jump systems via T–S
fuzzy modeling: Applications to robot arm model. IEEE
Transactions on Industrial Electronics, 68(1), 466–477.
https://doi.org/10.1109/TIE.41
Kamal, S., Moreno, J. A., Chalanga, A., Bandyopadhyay, B., &
Fridman, L. M. (2016). Continuous terminal sliding-mode
controller. Automatica, 69, 308–314. https://doi.org/10.
1016/j.automatica.2016.02.001
Kang, Z., Yu, H., & Li, C. (2020). Variable-parameter
double-power reaching law sliding mode control method.
Automatika, 61(3), 345–351. https://doi.org/10.1080/0005
1144.2020.1757965
Labbadi, M., Muñoz-Vázquez, A.J., Djemai, M., Boukal, Y.,
Zerrougui, M., & Cherkaoui, M. (2022). Fractional-order
nonsingular terminal sliding mode controller for a quadro-
tor with disturbances. Applied Mathematical Modelling, 111,
753–776. https://doi.org/10.1016/j.apm.2022.07.016
Lian, S., Meng, W., Lin, Z., Shao, K., Zheng, J., Li, H.,
& Lu, R. (2021). Adaptive attitude control of a quadro-
tor using fast nonsingular terminal sliding mode. IEEE
Transactions on Industrial Electronics, 69(2), 1597–1607.
https://doi.org/10.1109/TIE.2021.3057015
Lian, S., Meng, W., Shao, K., Zheng, J., Zhu, S., & Li, H. (2022).
Full attitude control of a quadrotor using fast nonsingular
terminal sliding mode with angular velocity planning. IEEE
Transactions on Industrial Electronics, 70(4), 3975–3984.
https://doi.org/10.1109/TIE.2022.3176314
Liu, S., Niu, B., Zong, G., Zhao, X., & Xu, N. (2022). Adaptive
fixed-time hierarchical sliding mode control for switched
under-actuated systems with dead-zone constraints via
event-triggered strategy. Applied Mathematics and Compu-
tation, 435, Article 127441. https://doi.org/10.1016/j.amc.
2022.127441
Liu, K., Wang, R., Wang, X., & Wang, X. (2021). Anti-saturation
adaptive finite-time neural network based fault-tolerant
tracking control for a quadrotor UAV with external dis-
turbances. Aerospace Science and Technology, 115, Article
106790. https://doi.org/10.1016/j.ast.2021.106790
Mallavalli, S., & Fekih, A. (2020). A fault tolerant tracking con-
trol for a quadrotor UAV subject to simultaneous actuator
faults and exogenous disturbances. International Journal of
Control, 93(3), 655–668. https://doi.org/10.1080/00207179.
2018.1484173
Mechali, O., Iqbal, J., Xie, X., Xu, L., Senouci, A., & Kaya-
can, E. (2021). Robust finite-time trajectory tracking con-
trol of quadrotor aircraft via terminal sliding mode-based
active antidisturbance approach: A PIL experiment. Inter-
national Journal of Aerospace Engineering, 2021, 1–28.
https://doi.org/10.1155/2021/5522379
Mechali, O., Xu, L., Huang, Y., et al. (2021). Observer-
based fixed-time continuous nonsingular terminal sliding
mode control of quadrotor aircraft under uncertainties and
disturbances for robust trajectory tracking: Theory and
experiment. Control Engineering Practice, 111, Article 104
806.
Mechali, O., Xu, L., Xie, X., & Iqbal, J. (2022). Fixed-time
nonlinear homogeneous sliding mode approach for robust
tracking control of multirotor aircraft: Experimental vali-
dation. Journal of the Franklin Institute, 359(5), 1971–2029.
https://doi.org/10.1016/j.jfranklin.2022.01.010
Mechali, O., Xu, L., Xie, X., & Iqbal, J. (2022). Theory and
practice for autonomous formation flight of quadrotors
via distributed robust sliding mode control protocol with
fixed-time stability guarantee. Control Engineering Practice,
123, Article 105150. https://doi.org/10.1016/j.conengprac.
2022.105150
Mobayen, S., Bayat, F., Din, S. ud, & Vu, M. T. (2023). Barrier
function-based adaptive nonsingular terminal sliding mode
control technique for a class of disturbed nonlinear systems.
ISA Transactions, 134, 481–496. https://doi.org/10.1016/j.
isatra.2022.08.006
Mobayen, S., El-Sousy, F. F.M., Alattas, K. A, Mofid, O., Fekih,
A., & Rojsiraphisal, T. (2023). Adaptive fast-reaching non-
singular terminal sliding mode tracking control for quadro-
tor UAVs subject to model uncertainties and external dis-
turbances. Ain Shams Engineering Journal, 14(8), Article
102059. https://doi.org/10.1016/j.asej.2022.102059
Moulay, E., Léchappé, V., Bernuau, E., Defoort, M., & Plestan,
F. (2022). Fixed-time sliding mode control with mis-
matched disturbances. Automatica, 136, Article 110009.
https://doi.org/10.1016/j.automatica.2021.110009
Raj, K., Muthukumar, V., Singh, S. N., & Lee, K. W. (2018).
Finite-time sliding mode and super-twisting control of
fighter aircraft. Aerospace Science and Technology, 82–83,
487–498. https://doi.org/10.1016/j.ast.2018.09.028
Saleh, A. M., & Hamoud, T. (2021). Mapping and 3D modelling
using quadrotor drone and GIS software. Journal of Big Data,
8(1), 1–12. https://doi.org/10.1186/s40537-020-00387-6
Sui, S., Chen, C. L. P., & Tong, S. (2022). A novel full
errors fixed-time control for constraint nonlinear systems.
IEEE Transactions on Automatic Control, 68(4), 2568–2575.
https://doi.org/10.1109/TAC.2022.3200962
Tang, P., Lin, D., Zheng, D., Fan, S., & Ye, J. (2020). Observer
based finite-time fault tolerant quadrotor attitude con-
trol with actuator faults. Aerospace Science and Technology,
104, Article 105968. https://doi.org/10.1016/j.ast.2020.105
968
ul Islam, R., Iqbal, J., & Khan, Q. (2014). Design and com-
parison of two control strategies for multi-DOF articulated
robotic arm manipulator. Journal of Control Engineering and
Applied Informatics, 16(2), 28–39.
Wang, F., Ma, Z., Gao, H., Zhou, C., & Hua, C. (2022).
Disturbance observer-based nonsingular fast terminal slid-
ing mode fault tolerant control of a quadrotor UAV with
external disturbances and actuator faults. International Jour-
nal of Control, Automation and Systems, 20(4), 1122–1130.
https://doi.org/10.1007/s12555-020-0773-2
Wang, R., Sun, Q., Sun, C., Zhang, H., Gui, Y., & Wang, P.
(2021). Vehicle-vehicle energy interaction converter of elec-
tric vehicles: A disturbance observer based sliding mode

## Page 22

INTERNATIONAL JOURNAL OF SYSTEMS SCIENCE
667
control algorithm. IEEE Transactions on VehicularTechnology,
70(10),
9910–9921.
https://doi.org/10.1109/TVT.2021.
3105433
Wang, B., & Zhang, Y. (2017). An adaptive fault-tolerant
sliding mode control allocation scheme for multirotor
helicopter subject to simultaneous actuator faults. IEEE
Transactions on Industrial Electronics, 65(5), 4227–4236.
https://doi.org/10.1109/TIE.41
Yang, L., Li, B., Li, W., Brand, H., Jiang, B., & Xiao, J.
(2020). Concrete defects inspection and 3D mapping using
CityFlyer quadrotor robot. IEEE/CAA Journal of Automat-
ica Sinica, 7(4), 991–1002. https://doi.org/10.1109/JAS.2020.
1003234
Yu, S., Yu, X., Shirinzadeh, B., & Man, Z. (2005). Con-
tinuous finite-time control for robotic manipulators with
terminal sliding mode. Automatica, 41(11), 1957–1964.
https://doi.org/10.1016/j.automatica.2005.07.001
Zhang, Y.-C., Ma, M.-C., Yang, X.-Y., & Song, S.-M. (2023).
Disturbance-observer-based fixed-time control for 6-DOF
spacecraft rendezvous and docking operations under full-
state constraints. Acta Astronautica, 205, 225–238. https://
doi.org/10.1016/j.actaastro.2023.02.005
Zhang, W. W., & Wang, J. (2012). Nonsingular terminal sliding
model control based on exponential reaching law. Control
and Decision, 27(6), 909–913.
Zhao, Z., Li, C., Yang, J., & Li, S. (2019). Output feedback
continuous terminal sliding mode guidance law for missile-
target interception with autopilot dynamics. Aerospace Sci-
ence and Technology, 86, 256–267. https://doi.org/10.1016/
j.ast.2019.01.012
