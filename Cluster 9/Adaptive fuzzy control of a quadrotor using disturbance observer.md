# Adaptive fuzzy control of a quadrotor using disturbance observer.pdf

## Page 1

University of Groningen
Adaptive fuzzy control of a quadrotor using disturbance observer
Li, Chuang; Wang, Yujia; Yang, Xuebo
Published in:
Aerospace science and technology
DOI:
10.1016/j.ast.2022.107784
IMPORTANT NOTE: You are advised to consult the publisher's version (publisher's PDF) if you wish to cite from
it. Please check the document version below.
Document Version
Publisher's PDF, also known as Version of record
Publication date:
2022
Link to publication in University of Groningen/UMCG research database
Citation for published version (APA):
Li, C., Wang, Y., & Yang, X. (2022). Adaptive fuzzy control of a quadrotor using disturbance observer.
Aerospace science and technology, 128, Article 107784. https://doi.org/10.1016/j.ast.2022.107784
Copyright
Other than for strictly personal use, it is not permitted to download or to forward/distribute the text or part of it without the consent of the
author(s) and/or copyright holder(s), unless the work is under an open content license (like Creative Commons).
The publication may also be distributed here under the terms of Article 25fa of the Dutch Copyright Act, indicated by the “Taverne” license.
More information can be found on the University of Groningen website: https://www.rug.nl/library/open-access/self-archiving-pure/taverne-
amendment.
Take-down policy
If you believe that this document breaches copyright please contact us providing details, and we will remove access to the work immediately
and investigate your claim.
Downloaded from the University of Groningen/UMCG research database (Pure): http://www.rug.nl/research/portal. For technical reasons the
number of authors shown on this cover page is limited to 10 maximum.
Download date: 30-12-2024

## Page 2

Aerospace Science and Technology 128 (2022) 107784
Contents lists available at ScienceDirect
Aerospace Science and Technology
www.elsevier.com/locate/aescte
Adaptive fuzzy control of a quadrotor using disturbance observer ✩
Chuang Li a,b,∗, Yujia Wang c, Xuebo Yang c
a The College of Engineering, Bohai University, Jinzhou 121013, Liaoning, China
b Department of Biomedical Engineering, University of Groningen and University Medical Centre Groningen, 9713 GZ Groningen, the Netherlands
c The Research Institute of Intelligent Control and Systems, School of Astronautics, Harbin Institute of Technology, Harbin 150001, China
a r t i c l e 
i n f o
a b s t r a c t
Article history:
Received 22 March 2019
Received in revised form 1 November 2021
Accepted 23 July 2022
Available online 28 July 2022
Communicated by Roberto Sabatini
Keywords:
Adaptive control
Fuzzy logic system
Disturbance observer
Quadrotor
In this paper, an adaptive fuzzy tracking control scheme by combining Lyapunov stability theory and 
backstepping technique is proposed for a quadrotor unmanned aerial vehicle. First, a fuzzy logic system 
is used to approximate the unmodeled dynamics of the quadrotor system. Second, command ﬁltering is 
utilized to compute the derivatives of the virtual control signals to avoid the complex analytic derivation 
of these derivatives. Third, a nonlinear disturbance observer is applied to compensate for external 
disturbance and approximation error of the fuzzy logic system. Lyapunov stability analysis shows that 
the quadrotor system can be stabilized by the proposed controller with high control accuracy. Finally, the 
experimental results are given to verify the effectiveness of the proposed control strategy.
© 2022 Elsevier Masson SAS. All rights reserved.
1. Introduction
Very recently, unmanned aerial vehicles (UAVs) have been 
widely used in military and civil ﬁelds. For example, military 
strikes, aerial photography, power line inspection, and forest ﬁre 
prevention [1–4]. Therefore, some research groups have done cor-
responding researches on UAVs. The quadrotor is a type of UAV 
that can do aerial hover, low-altitude, low-speed, heading remain 
unchanged, as well as perform tasks in a conﬁned space. These 
superior features are not available for other UAVs. However, the 
quadrotor control system has the characteristics of nonlinearity, 
uncertainty, underactuated with strong coupling. Moreover, the ex-
ternal disturbance also increases the diﬃculty of control. Therefore, 
the design of the quadrotor controller is very challenging.
To guarantee that a quadrotor UAV tracks ideal trajectory 
within a small tracking error, the attitude loop and the position 
loop need to be precisely controlled, and then the high preci-
sion control of the six degrees of freedom of the quadrotor can 
be achieved. Among existing literatures, the Proportional-Integer-
Derivative (PID) controller [5–8] has been widely used in UAVs 
due to its simple control structure. In [5], the PID controller has 
been used to regulate the posture (position and orientation) of the 
✩This research has received funding from China Scholarship Council (CSC No. 
201908210341).
* Corresponding author at: The College of Engineering, Bohai University, Jinzhou 
121013, Liaoning, China.
E-mail addresses: seven777lee@163.com (C. Li), wangyujia542@163.com
(Y. Wang), xueboyang@hit.edu.cn (X. Yang).
quadrotor. In [6], the authors have proposed a new model design 
method for a quadrotor, which has been further controlled by a 
PID controller. In [7], the authors have proposed two algorithms to 
adjust the gain of PID controller, and then compared the superior-
ity of the two algorithms. In [8], the authors have proposed a PID 
control method to restrain constant interference for the formation 
ﬂight of UAVs.
Compared with classical control methods, modern control 
methods have received much attention in recent decades. A large 
number of modern control methods have been proposed. For a 
nonlinear, strongly coupled, multi-input, multi-output quadrotor 
system with unmodeled dynamics, a robust controller combining 
backstepping with extended Kalman Bucy ﬁlter [9] has been pro-
posed to control the smooth ﬂight of the quadrotor. In [10–15], 
a control method based on sliding mode technology has been 
presented to solve the problem of model uncertainty, external dis-
turbance, actuator failure, and time-varying load in a quadrotor 
control system. In [16,17], for the problem of uncertain distur-
bances in the quadrotor system, the authors have been presented 
an error compensation mechanism to enhance the robustness of 
the system. With the rapid development of intelligent control, 
intelligent control algorithms have also been widely applied to 
various systems. Adaptive fuzzy [18] and adaptive neural network 
[19] control algorithms have been presented to control a 3-DOF 
helicopter system with model uncertainty, actuator deadzone, and 
state delay. In [20], the conventional PID controller and fuzzy logic 
system have been combined to construct a fuzzy self-tuning PID 
control algorithm to achieve precise control of the ﬂight height of 
the quadrotor.
https://doi.org/10.1016/j.ast.2022.107784
1270-9638/© 2022 Elsevier Masson SAS. All rights reserved.

## Page 3

C. Li, Y. Wang and X. Yang
Aerospace Science and Technology 128 (2022) 107784
Most of the control methods mentioned above improve the 
ﬂight performance of the quadrotor to some extent. However, there 
are still some problems that should be solved. Linear control meth-
ods are commonly used to control a quadrotor, such as PID or LQR. 
Although linear control methods have been proven to perform well 
in ﬂight control of the quadrotor, the effectiveness of linear con-
trol methods can only be guaranteed within a limited range of 
operating conditions. For sliding mode control, it has the merits 
of perfect robustness and better control performance, however, in 
the process of using sliding mode control, because of the contin-
uous switching logic, there would be chattering, which may affect 
the control accuracy of the quadrotor. In [21], the authors have 
realized that the fuzzy logic system can be used to approximate 
the unmodeled dynamics in the system. In [22,23], a ﬁnite-time 
disturbance observer has been deployed to deal with the uncer-
tainty in the system of a surface vehicle. In addition, a new type 
of disturbance observer has been designed for a quadrotor in [24], 
which has solved diﬃcult problems of high-accuracy control for 
the quadrotor UAV subjected to external disturbance force and un-
known disturbance torque.
Inspired by these research results, this paper proposes an adap-
tive control method based on fuzzy logic system and disturbance 
observer for a quadrotor system, and the main contributions of this 
paper are listed as follows:
(a) The unmodeled dynamics presented in the quadrotor system 
are approximated by the fuzzy logic system, and the external 
compounded disturbance is estimated by a disturbance ob-
server.
(b) The application of command ﬁltering and error compensa-
tion mechanism further improves the tracking accuracy of the 
quadrotor, and the conservativeness of the controller is re-
duced and the robustness of the controller is enhanced.
(c) Compared with traditional PID control, the proposed method 
can achieve full control of the six degrees of freedom of the 
quadrotor, also, can obtain smaller tracking error.
The remainder of this paper is organized as follows: Section 2
introduces the mathematical model of the quadrotor and the fuzzy 
logic system. An adaptive controller based on the fuzzy logic sys-
tem with disturbance observer is designed and the stability analy-
sis of the closed-loop system is given in Section 3. Finally, the ex-
perimental results and conclusions are demonstrated in Sections 4
and 5, respectively.
2. Problem statement
2.1. Mathematical model of quadrotor
The research platform shown in Fig. 1 is a quadrotor UAV by 
Quanser Innovate Educate Inc. The four brushless motors are sym-
metrically mounted on the frame, the No. 1 and No. 2 motors ro-
tate counterclockwise, and the No. 3 and No. 4 motors rotate clock-
wise. Furthermore, motion control of the quadrotor is achieved by 
adjusting the rotation speeds of the four motors. Fi {O I XI Y I Z I}
is the Earth-ﬁxed inertial frame, and Fb {O B XB Y B Z B} indicates 
the body-ﬁxed frame with the origin O B, which is the center of 
mass of the quadrotor UAV. The thrust Fk of each motor is gener-
ated by the following a ﬁrst-order linear transfer function:
Fk = K
B w
s + B w υk,
(1)
where k = 1, 2, 3, 4, K denotes a positive gain, B w represents 
the bandwidth of each brushless motor, and the input PWM of the 
Fig. 1. Structure of a quadrotor UAV.
motor is indicated by υk. The total force, torque of the pitch axis, 
roll axis, and yaw axis can be written as follows:
⎧
⎪⎪⎪⎪⎪⎨
⎪⎪⎪⎪⎪⎩
F = F1 + F2 + F3 + F4
τθ = d(F1 −F2)
τϕ = d(F3 −F4)
τψ = τ1 + τ2 −τ3 −τ4
,
(2)
where F represents the total force, and τθ , τϕ, and τψ are the 
torque of the pitch axis, roll axis, and yaw axis, respectively. d indi-
cates the distance from the center O B of the frame to each motor. 
τk is torque produced by rotating of motor, and its relationship 
with thrust Fk is τk = Ko Fk, and Ko is a constant.
In addition, according to Eq. (1), it can be assumed that Fk ≈
Kυk. Therefore, Eq. (2) can be written as:
⎧
⎪⎪⎪⎪⎪⎨
⎪⎪⎪⎪⎪⎩
F = K(υ1 + υ2 + υ3 + υ4)
τθ = Kd(υ1 −υ2)
τϕ = Kd(υ3 −υ4)
τψ = K Ko(υ1 + υ2 −υ3 −υ4)
.
(3)
Further, by applying small angle approximation, the attitude dy-
namics and the position dynamics are expressed in the body-ﬁxed 
frame and the inertial frame, respectively. They are given as fol-
lows [25]:
⎧
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎩
J y ¨θ = τθ + ( J z −Jx) ˙ϕ ˙ψ −J T ˙ϕω + fθ() + dθ(t)
Jx ¨ϕ = τϕ + ( J y −J z) ˙θ ˙ψ −J T ˙θω + fϕ() + dϕ(t)
J z ¨ψ = τψ + ( Jx −J y) ˙θ ˙ϕ + fψ() + dψ(t)
m¨x = F(cosϕ sinθ cosψ + sinϕ sinψ) + fx(x, ˙x) + dx(t)
m¨y = F(cosϕ sinθ sinψ −sinϕ cosψ) + f y(y, ˙y) + dy(t)
m¨z = F(cosϕ cosθ) −mg + fz(z, ˙z) + dz(t)
,
(4)
where θ, ϕ, and ψ indicate the pitch, roll, and yaw Euler angles 
of the quadrotor UAV. x, y, and z represent the coordinates of the 
quadrotor’s center of mass in the Earth-ﬁxed inertial frame. Jx, J y, 
and J z denote the moments of inertia along x, y, and z directions, 
respectively. J T represents the moment of inertia of each motor 
and  = [θ ˙θ ϕ ˙ϕ ψ ˙ψ]T is the state vector of the quadrotor. m de-
notes the total mass of the quadrotor, and g is the gravitational 
acceleration. ω = −ω1 −ω2 + ω3 + ω4, and ωk indicates the an-
gular speed of each motor. In addition, fθ , fϕ, fψ , fx, f y, and fz
represent the uncertainty of dynamic modeling of position and at-
titude due to installation errors, gyroscope errors, etc. dθ , dϕ, dψ, 
2

## Page 4

C. Li, Y. Wang and X. Yang
Aerospace Science and Technology 128 (2022) 107784
dx, dy, and dz indicate the time-dependent external disturbance 
which can be largely attributed to the exogenous effects, such as 
wind gusts or other environmental factors.
The desired attitude reference signal 	d = [θd ϕd ψd]T and the 
desired position reference signal Xd = [xd yd zd]T are given. The 
control objective is to design a control method such that the at-
titude and position of the quadrotor can asymptotically track the 
reference signal with a very small error.
In order to facilitate the establishment of the dynamic model 
for the quadrotor and to satisfy the implementation of the control 
algorithm, the following assumptions are given.
Assumption 1. The structure of the quadrotor is a symmetrical 
rigid body.
Assumption 2. The desired attitude reference signal and the de-
sired position reference signal are continuous, ﬁrst order differen-
tiable and bounded.
Assumption 3. The external disturbance d(t) = [dθ dϕ dψ dx dy dz]T
has ﬁnite energy. The external disturbances function d(t) and its 
ﬁrst-order derivative ˙d(t) are continuous functions, and ∥d(t)∥≤
dM, where dM is an unknown positive constant.
Lemma 1. [26]. Deﬁning a continuous and differentiable bounded func-
tion 
(x), ∀(t) ∈[t0, t1], if 
(x) satisﬁes 
(x)| ≤π, where π is the 
positive constant, and ˙
(x) is bounded.
Lemma 2. [26]. Given a continuous and positive deﬁnite Lyapunov 
function V (x), and there is bounded initial conditions, which satisﬁes 
π1(||x||) ≤V (x) ≤π2(||x||) such that ˙V (x) ≤−c1V (x) +c2, where π1, 
π2: Rn →R are class functions, and c1 and c2 are positive constants, 
then the solution x(t) is ultimately uniformly bounded.
2.2. Fuzzy logic system
The fuzzy logic system [27] contains the knowledge base, the 
fuzziﬁer, the fuzzy inference engine and the defuzziﬁer parts. If-
then rules form a knowledge base. Ri: If x1 is F i
1 and ... and xn
is F i
n then y is Bi, where x = [x1, x2,..., xn] ∈Rn, and y ∈R. x and 
y correspond to the input and output of the fuzzy logic system, 
F i
1, F i
2, ..., F i
n and Bi are fuzzy sets in ℜ. By applying the form 
of singleton fuzziﬁcation, the product inference, and the center-
average defuzziﬁcation, the following fuzzy logic system exists:
y(x) =
N
i=1
ωi
n
j=1
μF l
j(x j)
N
i=1

n
j=1
μF l
j(x j)
	,
(5)
where N indicates the number of if-then rules, μBi(ωi) is the 
fuzzy membership function.
Deﬁne si(xi) =
n

j=1
μF l
j(x j)/ 
N

i=1
⎡
⎣
n

j=1
μF l
j(x j)
⎤
⎦, S(X) =

s1(x), ...,
sn(x)
T and W = [ω1,...,ωn]T , the fuzzy logic system can be ex-
pressed by:
y = W T S(X).
(6)
If any membership is selected as Gaussian functions, there will 
be the following Lemma 3 set up.
Fig. 2. Control scheme of quadrotor.
Lemma 3. [28]. For a continuous function f (x) deﬁned on a compact set 
ω, deﬁne a desired precision function |σ(X)| ≤¯σ , then, the fuzzy logic 
system Eq. (6) satisﬁes sup
x∈
 f (x) −W T S(X)
 ≤¯σ .
Remark 1. It should be noted that Lemma 3 is very important for 
the following controller design process. An arbitrary real continu-
ous function f (x) can be linearly composed of the basis function 
vector S(X) and a bounded error function σ(X), which means that 
f (x) = W T S(X) + σ(X), where 0 < ST S ≤1.
3. Control design and stability analysis
In this section, an adaptive control method based on the fuzzy 
logic system with disturbance observer is proposed, and then the 
six degrees of freedom of the quadrotor is precisely controlled. The 
block diagram of the entire control system is shown in Fig. 2.
3.1. Attitude controller design
For facilitating the design of the attitude controller of the 
quadrotor, the coordinate transformation is given by:
⎧
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎩
	1 = θ, 	2 = ϕ, 	3 = ψ
	d1 = θd, 	d2 = ϕd, 	d3 = ψd
g1 = 1/ J y, g2 = 1/ Jx, g3 = 1/ J z
τ1 = τθ, τ2 = τϕ, τ3 = τψ
G1 = [( J z −Jx) ˙ϕ ˙ψ −J T ˙ϕω]/ J y
G2 = [( J y −J z) ˙θ ˙ψ −J T ˙θω]/ Jx
G3 = [( Jx −J y) ˙θ ˙ϕ]/ J z
f1 = fθ/ J y, f2 = fϕ/ Jx, f3 = fψ/ J z
d1 = dθ/ J y, d2 = dϕ/ Jx, d3 = dψ/ J z
.
(7)
Furthermore, the attitude dynamics in Eq. (4) can be written as 
follows:
¨	i = giτi + Gi + fi + di,
i = 1, 2, 3.
(8)
Backstepping technology will be used during the design of 
the quadrotor’s attitude controller. Therefore, the virtual controller 
needs to be derived, and in the process of derivation, it will in-
troduce extra signal noise to the controller, which will affect the 
control of the quadrotor. So the command ﬁltering technique is 
used to solve this problem, and a command ﬁltering [29] is de-
ﬁned as follows:
 ˙ηi1 = ϖiη2
˙ηi2 = −2ςiϖiηi2 −ϖi(ηi1 −αi) ,
(9)
3

## Page 5

C. Li, Y. Wang and X. Yang
Aerospace Science and Technology 128 (2022) 107784
where ηi1(0) = αi (0), ηi2(0) = 0, ϖi > 0, ςi ∈(0, 1], and αi =
−ki1ei1 + ˙	di represents virtual control, which is used to design 
the controller according to backstepping technology.
Deﬁne attitude tracking error as follows:
ei1 = 	i −	di,
(10)
ei2 = ˙	i −αi.o,
(11)
where αi.o = ηi1 represents the output of the command ﬁltering, 
and the input of the command ﬁltering is virtual control αi.
Remark 2. The use of the command ﬁltering will bring a small ﬁl-
ter error. Hence, an error compensation mechanism is introduced 
such that the tracking error can be further reduced.
An auxiliary system is given [30] as follows:
⎧
⎨
⎩
˙ζi1 = −ki1ζi1 + ζi2 + (αi.o −αi)
˙ζi2 = −ki2ζi2 −ζi1
,
(12)
where ki1 and ki2 represent the positive controller parameters to 
be designed, ζi1 represents the error compensation signal, and 
||ζi1|| is bounded [30].
Deﬁne the quadrotor attitude compensation tracking errors:
vi1 = ei1 −ζi1,
(13)
vi2 = ei2 −ζi2.
(14)
The time derivative of Eqs. (13) and (14) are given as follows:
˙vi1 = vi2 −ki1vi1,
(15)
˙vi2 = giτi + Gi + fi + di −˙αi.o + ki2ζi2 + ζi.
(16)
By applying fuzzy logic system, Eq. (16) can be written:
˙vi2 =giτi + Gi + W T
i Si(X) + σi(X)
+ di −˙αi.o + ki2ζi2 + ζi.
(17)
Deﬁne the following compounded disturbance as:
Di = σi(X) + di,
(18)
where the compounded disturbance Di is unknown because the 
external disturbances and the fuzzy logic system errors are un-
known. However, |˙di| ≤¯di can be obtained from Assumption 3 and 
Lemma 1. Additionally, based on the approximation theory [31] of 
fuzzy logic system, the unknown approximation error σi(X) satis-
ﬁes | ˙σi(X)| ≤¯σi. Therefore, the following inequality is established:
| ˙Di| ≤ρi,
(19)
where ρi is an unknown positive constant.
In order to eliminate the compounded disturbance for the at-
titude of the quadrotor system, a nonlinear disturbance observer 
will be utilized [32].
Consider an auxiliary system as follows:
Zi = Di −li ˙	i,
(20)
where li is a positive design parameter. Furthermore, using Eqs. (8)
and (18), the derivative of Zi concerning time can be obtained:
˙Zi = ˙Di −li ¨	i = ˙Di −li(giτi + Gi + W T
i Si(X) + Di).
(21)
In order to estimate the compounded disturbance in the 
quadrotor system, the auxiliary variable Zi should be estimated:
˙ˆZi = −li(giτi + Gi + ˆW T
i Si(X) + ˆDi).
(22)
Using Eq. (20), we have:
ˆDi = ˆZi + li ˙	i.
(23)
From Eqs. (20) and (23), one has:
˜Zi = Zi −ˆZi = Di −ˆDi = ˜Di.
(24)
Using Eqs. (21) and (22), the derivative of Eq. (24) can be ob-
tained:
˙˜Di = ˙Di −li( ˜W T
i Si(X) + ˜Di).
(25)
Then, the adaptive law and the attitude controller of the 
quadrotor system can be designed, as follows:
˙ˆ
Wi = i(Si(X)vi2 −δi ˆWi),
(26)
τi = 1
gi
(−ki2ei2 −ei1 −1
2 vi2 + ˙αi.o −Gi −ˆW T
i S(X)−ˆDi),
(27)
where i represents a positive deﬁnite matrix, and δi represents a 
positive constant.
3.2. Position controller design
Before designing the position controller, the coordinate trans-
formation is performed on the translational dynamics of the 
quadrotor dynamics equation:
⎧
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎩
X4 = x, X5 = y, X6 = z
Xd4 = xd, Xd5 = yd, Xd6 = zd
u4 = F
m(cosϕ sinθ cosψ + sinϕ sinψ)
u5 = F
m(cosϕ sinθ sinψ −sinϕ cosψ)
u6 = F
m(cosϕ cosθ) −g
f4 = fx/m, f5 = f y/m, f6 = fz/m
d4 = dx/m, d5 = dy/m, d6 = dz/m
.
(28)
Therefore, the translational dynamics of Eq. (4) can be written, as 
follows:
¨Xi = ui + fi + di
i = 4, 5, 6.
(29)
The design process of adaptive law and position controller is 
similar to the attitude controller design, as follows:
˙ˆ
Wi = i(Si(X)vi2 −δi ˆWi),
(30)
ui = −ki2ei2 −ei1 −1
2 vi2 + ˙αi.o −ˆW T
i S(X) −ˆDi,
(31)
where i = 4, 5, 6.
3.3. Stability analysis
Theorem 1. Consider the quadrotor closed-loop system Eq. (4), the con-
trollers Eqs. (27) and (31), and the adaptive laws Eqs. (26) and (30) are 
constructed. Furthermore, the fuzzy logic system and the disturbance ob-
server are utilized to construct the controller of the closed-loop control 
system. Additionally, the initial conditions of the quadrotor system are 
given. Therefore, the tracking error of the quadrotor system and all signal 
in closed-loop system can be guaranteed to be bounded.
4

## Page 6

C. Li, Y. Wang and X. Yang
Aerospace Science and Technology 128 (2022) 107784
Proof of Theorem 1. Consider a Lyapunov candidate function as:
V i1 = 1
2 v2
i1,
(32)
where i = 1, 2, 3, 4, 5, 6, and the derivative of V i1 can be ob-
tained from Eq. (15), as follows:
˙V i1 = vi1(vi2 −ki1vi1)
= vi1vi2 −ki1v2
i1.
(33)
Choose another a Lyapunov candidate function as:
V i2 = V i1 + 1
2 v2
i2 + 1
2
˜D2
i + 1
2
˜W T
i −1
i
˜Wi.
(34)
The derivative V i2 is given by:
˙V i2 = ˙V i1 + vi2 ˙vi2 + ˜Di ˙˜Di −˜W T
i −1
i
˙ˆW .
(35)
By applying Eqs. (17), (18), (25) and (33), one has:
˙V i2 =vi1vi2 −ki1v2
i1 + vi2(giτi + Gi + W T
i Si(X)
+ Di −˙αi.o + ki2ζi2 + ζi) + ˜Di( ˙Di
−li( ˜W T
i Si(X) + ˜Di)) −˜W T
i −1
i
˙ˆ
Wi.
(36)
Then, substitute Eqs. (27) and (31) into Eq. (36) leads to:
˙V i2 =vi1vi2 −ki1v2
i1 + vi2(−ki2vi2 −vi1 + ˜W T
i Si(X)
+ ˜Di −1
2 vi2) + ˜Di( ˙Di −li( ˜W T
i Si(X) + ˜Di))
−˜W T
i −1
i
˙ˆ
Wi.
(37)
Using the Young inequality and Eq. (19), then the following in-
equalities exist:
vi2 ˜Di ≤1
2 v2
i2 + 1
2
˜D2
i ,
(38)
˜Di ˙Di ≤1
2
˜D2
i + 1
2
˙D2
i ≤1
2
˜D2
i + 1
2ρ2
i ,
(39)
−li ˜Di ˜Wi Si(X) ≤1
2li ˜D2
i +1
2li|| ˜Wi||2.
(40)
Using Eqs. (38), (39), and (40), Eq. (37) can be written, as fol-
lows:
˙V i2 ≤−ki1v2
i1 −ki2v2
i2 + vi2 ˜W T
i Si(X) + 1
2
˜D2
i + 1
2
˜D2
i
+ 1
2ρ2
i + 1
2li ˜D2
i +1
2li|| ˜Wi||2 −li ˜D2
i −˜W T
i −1
i
˙ˆ
Wi.
(41)
Substituting Eqs. (26) and (30) into Eq. (41) leads to:
˙V i2 ≤−ki1v2
i1 −ki2v2
i2 + vi2 ˜W T
i Si(X) −(1
2li −1) ˜D2
i
+ 1
2ρ2
i +1
2li|| ˜Wi||2 −˜W T
i −1
i
(i(Si(X)vi2 −δi ˆWi)). (42)
Furthermore, the following inequality exists:
˜W T
i δi ˆWi ≤−1
2δi|| ˜Wi||2 + 1
2δi||Wi||2.
(43)
Substituting Eq. (43) into Eq. (42) leads to:
˙V i2 ≤−ki1v2
i1 −ki2v2
i2 −(1
2li −1) ˜D2
i + 1
2ρ2
i
−1
2(δi −li)|| ˜Wi||2 + 1
2δi||Wi||2
≤−aiV i2 + bi,
(44)
Fig. 3. The overall architecture of QBall 2.
where ai = min{2ki1, 2ki2, li −2, δi −li} and bi = 1
2ρ2
i + 1
2δi||Wi||2.
In order to ensure the stability of the quadrotor closed-loop 
system, the design parameters LI and δi should satisfy li > 2
and δi > li. In addition, all signals of the closed-loop system are 
bounded based on Lemma 2.
The proof is completed here.
Furthermore, the desired position reference signal xd, yd, and 
zd, and desired yaw angle ψd are given according to the actual 
mission requirements. Since the quadrotor system is underactu-
ated and strongly coupled, the position loop information is used 
to calculate the attitude loop information θd and ϕd, and at the 
same time calculate the total lift force, the speciﬁc expression is as 
follows [33]:
θd = arctan(u4 cosψd + u5 sinψd
u6 + g
),
(45)
ϕd = arcsin( u4 sinψd −u5 cosψd

u2
4 + u2
5 + (u6 + g)2
),
(46)
F = m

u2
4 + u2
5 + (u6 + g)2.
(47)
Remark 3. The control method proposed in this paper can theoret-
ically compensate the uncertainty of the quadrotor system model 
and eliminate the compounded disturbance, but the disturbance 
observer designed in this paper is more suitable for continuous 
disturbance due to it taking a certain time to estimate the distur-
bance. Then, for the instantaneous disturbance, it is diﬃcult to be 
estimated and eliminated. In addition, sensor noise can also have a 
certain negative impact on the ﬂight performance of the quadrotor.
4. Experimental results
In order to verify the control method proposed in this paper, 
the QBall 2 experimental tested is used, and the entire experimen-
tal tested system is shown in Fig. 3. In addition to a quadrotor in 
this experimental tested, there is also a subsystem for measuring 
the attitude and position of the quadrotor indoors called OptiTrack, 
which consists of 24 cameras installed indoors. Other than that, 
the Quanser’s on-board avionics data acquisition card which is a 
high-resolution inertial measurement unit, and a wireless Gum-
stix DuoVero embedded computer are used to measure on-board 
sensors and drive the motors. QUARC, Quanser’s real-time con-
trol software is applied, which can be seamlessly connected with 
MATLAB Simulink. Therefore, we can build the controller in the 
Simulink with QUARC, and then download, compile, generate code 
and execute the controller on-board QBall 2 quadrotor [34].
5

## Page 7

C. Li, Y. Wang and X. Yang
Aerospace Science and Technology 128 (2022) 107784
Table 1
Parameters of the quadrotor.
Parameter
Value
Parameter
Value
K
120 N
Jx
0.03 kg · m2
K0
0.033 m
J y
0.03 kg · m2
d
0.2 m
J z
0.04 kg · m2
B w
15 rad/sec
J T
154 × 10−7 kg · m2
m
1.8 kg
g
9.81 m/s2
Table 2
Gains of the quadrotor.
Gain
i = 1
i = 2
i = 3
i = 4
i = 5
i = 6
ki1
3
3
2.7
0.18
0.18
0.17
ki2
0.22
0.22
0.37
0.04
0.04
0.08
i
12I5×5
12I5×5
13I5×5
9I5×5
9I5×5
10I5×5
δi
10
10
8
8
8
10
li
2.8
2.8
2.9
2.6
2.6
2.5
ϖi
70
70
60
70
70
60
ςi
0.3
0.3
0.3
0.3
0.3
0.3
In this experimental environment, in order to improve the 
safety of the experiment, a safety rope is used to prevent injury 
to the experimenter and damage to the experimental equipment. 
Additionally, an electric fan is used which can provide wind as an 
external disturbance, and the wind speed is about 4 m/s. There-
fore, the corresponding external disturbance force and disturbance 
torque caused by wind will act on the QBall 2 quadrotor.
The initial conditions are: || ˆW1|| = || ˆW2|| = || ˆW3|| = || ˆW4|| =
|| ˆW5|| = || ˆW6|| = 0. In the fuzzy logic system, the basis function 
vectors S1(X), S2(X), S3(X), S4(X), S5(X), and S6(X) use 5 nodes, 
and the center values μ1, μ2, μ3, μ4, μ5, and μ6 are evenly dis-
tributed between [-1, 1], and the width values ℓ1 = 1.2, ℓ2 = 1.2, 
ℓ3 = 1.2, ℓ4 = 1.5, ℓ5 = 1.5, and ℓ6 = 1.5.
The parameters of the experimental equipment and the param-
eters of the controller are shown in Table 1 and Table 2, respec-
tively.
Remark 4. In order to make QBall 2 quadrotor system stable, the 
parameters of controller should be selected in strict accordance 
with the requirements of the controller design. In addition, the pa-
rameters of the controller are also related to the uncertainty of the 
quadrotor system and external disturbances. Therefore, we further 
adjust the parameters of the controller based on the experimental 
results.
Remark 5. In Table 2, i = 1, 2, 3 represents the parameters used in 
the design of the attitude controller, and i = 4, 5, 6 indicates the 
parameters used in the design of the position control controller.
Remark 6. In the following experimental process, the unit of the 
position of QBall 2 quadrotor is meter, and the unit of the attitude 
angle of the quadrotor is radian. Additionally, the initial position 
and the initial yaw angle of QBall 2 quadrotor are slightly different 
due to the placement of the experimenter during each experiment.
4.1. Experiment: set-point tracking
In the ﬁrst set of experiments, the control method pro-
posed in this paper is ﬁrst used to make the quadrotor ﬂy to 
a ﬁxed point for hovering. The coordinates of the hover point 
are Xd = [0 0 1]T and the desired yaw angle is ψd = 0. The 
initial position and initial attitude of the quadrotor are X0 =
Fig. 4. Position of the quadrotor in the XI -axis direction.
Fig. 5. Position of the quadrotor in the Y I -axis direction.
Fig. 6. Position of the quadrotor in the Z I -axis direction.
[0.029 0.015 0.300]T and 	0 = [0 0 
−0.035]T , respectively. 
Since the center height of the quadrotor is 0.3 m, the ini-
tial position of the takeoff height is 0.3 m. Second, in order 
to illustrate the advantages of the proposed method, the con-
ventional PID controller is used for the quadrotor with initial 
position X0 = [0.024 0.005 0.300]T
and initial attitude 	0 =
[0 0 −0.050]T , respectively.
Fig. 12 and Fig. 17 show the control inputs under the control 
method proposed in this paper and the conventional PID control 
method, respectively. Additionally, it can be seen from xaf c, yaf c, 
and zaf c in Figs. 4–6 that the quadrotor can hover perfectly at a 
given reference position. Further, from Figs. 7–9, the tracking of 
the attitude angle of the quadrotor can be obtained, and Fig. 10 di-
rectly reﬂects the tracking error of the attitude angle, furthermore, 
from the tracking error of the attitude angle, the perfect tracking 
effect of the attitude angle of the quadrotor can also be seen. Addi-
tionally, in this set of experiments, Fig. 11 shows the two norms of 
6

## Page 8

C. Li, Y. Wang and X. Yang
Aerospace Science and Technology 128 (2022) 107784
Fig. 7. Pitch angle tracking with the proposed controller.
Fig. 8. Roll angle tracking with the proposed controller.
Fig. 9. Yaw angle tracking with the proposed controller.
Fig. 10. Attitude angle tracking error with the proposed controller.
Fig. 11. Responses of || ˆW1||, || ˆW2||, || ˆW3||, || ˆW4||, || ˆW5||, and || ˆW6||. (For interpre-
tation of the colors in the ﬁgure(s), the reader is referred to the web version of this 
article.)
Fig. 12. Control input with the proposed controller.
Fig. 13. Pitch angle tracking with the PID controller.
Fig. 14. Roll angle tracking with the PID controller.
7

## Page 9

C. Li, Y. Wang and X. Yang
Aerospace Science and Technology 128 (2022) 107784
Fig. 15. Yaw angle tracking with the PID controller.
Fig. 16. Attitude angle tracking error with the PID controller.
Fig. 17. Control input with the PID controller.
the weight vector under the control method proposed in this pa-
per. However, when testing the quadrotor using the traditional PID 
control algorithm, we can obtain from the xpid, ypid, and zpid in 
Figs. 4–6 that the quadrotor has a large ﬂuctuation near the given 
reference point. Besides, Figs. 13–16 also show that the attitude 
tracking effect of the quadrotor is not ideal under the traditional 
PID control algorithm.
4.2. Experiment: trajectory tracking
Similar to the ﬁrst set of experiments, the second set of experi-
ments also used the control algorithm proposed in this article and 
the traditional PID control algorithm to test the quadrotor. How-
ever, the difference is that the quadrotor is required to track a 
trajectory. The expression of this trajectory is Xd = [xd
yd
1]T , 
where xd2 + yd2 = 0.25, and the desired yaw angle is ψd = 0. 
The initial position and initial attitude of the quadrotor when 
Fig. 18. Trajectory tracking result of quadrotor.
Fig. 19. Pitch angle tracking with the proposed controller.
Fig. 20. Roll angle tracking with the proposed controller.
using the control algorithm proposed in this paper are X0 =
[0.033 0.010 0.300]T and 	0 = [0 0 
−0.020]T , respectively, 
and the initial positions of the quadrotor when using the con-
ventional PID control algorithm are X0 = [0.022 0 0.300]T and 
	0 = [0 0 −0.005]T , respectively.
Fig. 24 and Fig. 29 show the control inputs under the control 
algorithm proposed in this paper and the traditional PID control 
algorithm. In Fig. 18, compared with the tracking effects of the 
two control algorithms, we can clearly see that the tracking per-
formance under the control algorithm proposed in this paper is 
8

## Page 10

C. Li, Y. Wang and X. Yang
Aerospace Science and Technology 128 (2022) 107784
Fig. 21. Yaw angle tracking with the proposed controller.
Fig. 22. Attitude angle tracking error with the proposed controller.
Fig. 23. Responses of || ˆW1||, || ˆW2||, || ˆW3||, || ˆW4||, || ˆW5||, and || ˆW6||. (For inter-
pretation of the colors in the ﬁgure(s), the reader is referred to the web version of 
this article.)
Fig. 24. Control input with the proposed controller.
Fig. 25. Pitch angle tracking with the PID controller.
Fig. 26. Roll angle tracking with the PID controller.
Fig. 27. Yaw angle tracking with the PID controller.
Fig. 28. Attitude angle tracking error with the PID controller.
9

## Page 11

C. Li, Y. Wang and X. Yang
Aerospace Science and Technology 128 (2022) 107784
Fig. 29. Control input with the PID controller.
better, while the quadrotor tracking effect using the PID control 
algorithm is not ideal. Further, the attitude angle tracking effect 
of the quadrotor under the two control algorithms can be seen 
from Figs. 19–21 and Figs. 25–27. Additionally, in this set of exper-
iments, Fig. 23 indicates the two norms of the weight vector under 
the control method proposed in this paper. By analyzing Fig. 22
and Fig. 28, we can get the attitude angle tracking performance of 
the quadrotor under the control algorithm proposed in this paper 
is satisfactory. However, the PID control algorithm does not make 
the attitude of the quadrotor have good tracking performance, es-
pecially the yaw angle.
Through the analysis and discussion of the above two sets 
of experiments and comparative experiments, whether the ﬁxed-
point hover or the tracking of the trajectory. The tracking per-
formance is relatively worse when the traditional PID control al-
gorithm is used because the PID controller cannot alleviate the 
inﬂuence of the uncertainty of the quadrotor system model and 
external interference. However, the quadrotor has perfect ﬂight 
performance and high-precision tracking performance by using the 
control method proposed in this paper when the system model of 
the quadrotor is uncertain and subject to external interference.
5. Conclusions
In the paper, an adaptive backstepping control scheme based 
on a fuzzy logic system, command ﬁltering, and disturbance ob-
server is proposed for a quadrotor UAV. In our method, the fuzzy 
logic system is used to compensate for uncertainty in the trans-
lational dynamics and the rotational dynamics of the quadrotor. 
Furthermore, we utilize a disturbance observer to approximate the 
external disturbances in the position loop and the attitude loop 
and error caused by using the fuzzy logic system. Finally, the pro-
posed control strategy can guarantee the accuracy of the quadrotor 
full (including translational and rotational) control, and the track-
ing errors of the position loop and the attitude loop are stabilized. 
Our future work is to extend this method to the formation con-
trol of multiple UAVs. In addition, control problems for UAVs with 
actuator or sensor failure will also be considered and studied.
Declaration of competing interest
We declare that we have no ﬁnancial and personal relationships 
with other people or organizations that can inappropriately inﬂu-
ence our work, there is no professional or other personal interest 
of any nature or kind in any product, service and/or company that 
could be construed as inﬂuencing the position presented in, or the 
review of, the manuscript entitled.
References
[1] T. Coffey, J.A. Montgomery, The emergence of mini UAVs for military applica-
tions, Mil. Technol. 28 (2004) 28–37.
[2] A. Gurtner, D.G. Greer, R. Glassock, L. Mejias, R.A. Walker, W.W. Boles, Investi-
gation of ﬁsh-eye lenses for small-UAV aerial photography, IEEE Trans. Geosci. 
Remote Sens. 47 (3) (2009) 709–721.
[3] X.B. Chen, M.A. Yu-Lin, X.U. Zu-Jian, Research on transmission-lines-cruising 
technology with the unmanned aerial vehicle, South. Power Syst. Technol. 2 (6) 
(2008) 59–61.
[4] K. Nonami, Prospect and recent research & development for civil use au-
tonomous unmanned aircraft as UAV and MAV, J. Syst. Des. Dyn. 1 (2) (2007) 
120–128.
[5] J. Li, Y. Li, Dynamic analysis and PID control for a quadrotor, in: 2011 IEEE 
International Conference on Mechatronics and Automation, 2011, pp. 573–578.
[6] A.L. Salih, M. Moghavvemi, H.A.F. Mohamed, K.S. Gaeid, Modelling and PID con-
troller design for a quadrotor unmanned air vehicle, in: 2010 IEEE International 
Conference on Automation, Quality and Testing, Robotics (AQTR), vol. 1, 2010, 
pp. 1–5.
[7] J. Kim, S.A. Wilkerson, S.A. Gadsden, Comparison of gradient methods for gain 
tuning of a PD controller applied on a quadrotor system, in: Unmanned Sys-
tems Technology XVIII, 2016, p. 98370V.
[8] R.T.Y. Thien, K. Yoonsoo, Decentralized formation ﬂight via PID and integral 
sliding mode control, Aerosp. Sci. Technol. 81 (2018) 322–332.
[9] R. Babaei, A.F. Ehyaei, Robust backstepping control of a quadrotor UAV using 
extended Kalman Bucy ﬁlter, Int. J. Mechatron. Electr. Comput. Technol. 5 (16) 
(2015) 2276–2291.
[10] Z. Jia, J. Yu, Y. Mei, Y. Chen, Y. Shen, X. Ai, Integral backstepping sliding mode 
control for quadrotor helicopter under external uncertain disturbances, Aerosp. 
Sci. Technol. 68 (2017) 299–307.
[11] B. Mu, K. Zhang, Y. Shi, Integral sliding mode ﬂight controller design for a 
quadrotor and the application in a heterogeneous multi-agent system, IEEE 
Trans. Ind. Electron. 64 (12) (2017) 9389–9398.
[12] X. Wang, S. Sun, E.-J. van Kampen, Q. Chu, Quadrotor fault tolerant incremental 
sliding mode control driven by sliding mode disturbance observers, Aerosp. Sci. 
Technol. 87 (2019) 417–430.
[13] M. Vahdanipour, M. Khodabandeh, Adaptive fractional order sliding mode con-
trol for a quadrotor with a varying load, Aerosp. Sci. Technol. 86 (2019) 
737–747.
[14] N. Wang, Q. Deng, G. Xie, X. Pan, Hybrid ﬁnite-time trajectory tracking control 
of a quadrotor, ISA Trans. 90 (2019) 278–286.
[15] N. Wang, S.-F. Su, M. Han, W.-H. Chen, Backpropagating constraints-based tra-
jectory tracking control of a quadrotor with constrained actuator dynamics 
and complex unknowns, IEEE Trans. Syst. Man Cybern. Syst. 49 (7) (2018) 
1322–1337.
[16] Y. Zhang, Z. Chen, X. Zhang, Q. Sun, M. Sun, A novel control scheme for quadro-
tor uav based upon active disturbance rejection control, Aerosp. Sci. Technol. 79 
(2018) 601–609.
[17] J. Zhang, D. Gu, Z. Ren, B. Wen, Robust trajectory tracking controller for quadro-
tor helicopter based on a novel composite control scheme, Aerosp. Sci. Technol. 
85 (2019) 199–215.
[18] C. Li, X. Yang, B. Xiao, Adaptive attitude tracking control of a 3-degrees-of-
freedom experimental helicopter with actuator dead-zone, Proc. Inst. Mech. 
Eng., Part I, J. Syst. Control Eng. 233 (1) (2019) 91–99.
[19] Y. Chen, X. Yang, X. Zheng, Adaptive neural control of a 3-DOF helicopter with 
unknown time delay, Neurocomputing 307 (2018) 98–105.
[20] Fahmizal, A. Surriani, M. Budiyanto, M. Arroﬁq, Altitude control of quadrotor 
using fuzzy self tuning PID controller, in: International Conference on Instru-
mentation, Control, and Automation, 2017, pp. 67–72.
[21] X. Zhao, X. Zheng, B. Niu, L. Liu, Adaptive tracking control for a class of uncer-
tain switched nonlinear systems, Automatica 52 (2015) 185–191.
[22] N. Wang, G. Xie, X. Pan, S.-F. Su, Full-state regulation control of asymmet-
ric underactuated surface vehicles, IEEE Trans. Ind. Electron. 66 (11) (2019) 
8741–8750.
[23] N. Wang, S.-F. Su, X. Pan, X. Yu, G. Xie, Yaw-guided trajectory tracking control 
of an asymmetric underactuated surface vehicle, IEEE Trans. Ind. Inform. 15 (6) 
(2018) 3502–3513.
[24] B. Xiao, S. Yin, A new disturbance attenuation control scheme for quadrotor 
unmanned aerial vehicles, IEEE Trans. Ind. Inform. 13 (6) (2017) 2922–2932.
[25] Y. Zhang, A. Chamseddine, Fault tolerant ﬂight control techniques with appli-
cation to a quadrotor UAV testbed, in: Automatic Flight Control Systems-Latest 
Developments, vol. 5, 2012, pp. 119–150.
[26] Z. Li, C.Y. Su, L. Wang, Z. Chen, T. Chai, Nonlinear disturbance observer-based 
control design for a robotic exoskeleton incorporating fuzzy approximation, 
IEEE Trans. Ind. Electron. 62 (9) (2015) 5763–5775.
[27] C.L.P. Chen, C.E. Ren, T. Du, Fuzzy observed-based adaptive consensus track-
ing control for second-order multiagent systems with heterogeneous nonlinear 
dynamics, IEEE Trans. Fuzzy Syst. 24 (4) (2016) 906–915.
[28] L.X. Wang, J.M. Mendel, Fuzzy basis functions, universal approximation, and 
orthogonal least-squares learning, IEEE Trans. Neural Netw. 3 (5) (1992) 
807–814.
10

## Page 12

C. Li, Y. Wang and X. Yang
Aerospace Science and Technology 128 (2022) 107784
[29] J. Yu, P. Shi, W. Dong, H. Yu, Observer and command-ﬁlter-based adaptive fuzzy 
output feedback control of uncertain nonlinear systems, IEEE Trans. Ind. Elec-
tron. 62 (9) (2015) 5962–5970.
[30] W. Dong, J.A. Farrell, M.M. Polycarpou, M. Sharma, Command ﬁltered adaptive 
backstepping, in: American Control Conference, 2010, pp. 105–110.
[31] R. Li, M. Chen, Q. Wu, Adaptive neural tracking control for uncertain nonlinear 
systems with input and output constraints using disturbance observer, Neuro-
computing 235 (2016) 27–37.
[32] L. Zhang, Z. Li, C. Yang, Adaptive neural network based variable stiffness con-
trol of uncertain robotic systems using disturbance observer, IEEE Trans. Ind. 
Electron. 64 (3) (2016) 2236–2245.
[33] Z. Zuo, C. Wang, Adaptive trajectory tracking control of output constrained 
multi-rotors systems, IET Control Theory Appl. 8 (13) (2014) 1163–1174.
[34] Qball 2 reference manual, Quanser Consulting Inc.
11
