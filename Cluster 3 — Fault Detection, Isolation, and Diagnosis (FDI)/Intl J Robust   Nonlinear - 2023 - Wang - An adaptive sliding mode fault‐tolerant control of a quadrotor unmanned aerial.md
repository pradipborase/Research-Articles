# Intl J Robust   Nonlinear - 2023 - Wang - An adaptive sliding mode fault‐tolerant control of a quadrotor unmanned aerial.pdf

## Page 1

Received: 30 January 2022
Revised: 4 January 2023
Accepted: 31 January 2023
DOI: 10.1002/rnc.6631
R E S E A R C H A R T I C L E
An adaptive sliding mode fault-tolerant control
of a quadrotor unmanned aerial vehicle with actuator faults
and model uncertainties
Ban Wang1
Yanyan Shen2
Ni Li1
Youmin Zhang3
Zhenghong Gao1
1School of Aeronautics, Northwestern
Polytechnical University, Xi’an, Shaanxi,
China
2Department of Electrical and Computer
Engineering, Concordia University,
Montreal, Quebec, Canada
3Department of Mechanical, Industrial
and Aerospace Engineering, Concordia
University, Montreal, Quebec, Canada
Correspondence
Youmin Zhang, Department of
Mechanical, Industrial and Aerospace
Engineering, Concordia University,
Montreal, QC H3G 1M8, Canada.
Email: ymzhang@encs.concordia.ca
Funding information
National Natural Science Foundation of
China, Grant/Award Numbers: 62003266,
61833013, 62003272; Fundamental
Research Funds for the Central
Universities; Natural Sciences and
Engineering Research Council of Canada
Abstract
An adaptive sliding mode fault-tolerant control strategy is proposed for a
quadrotor unmanned aerial vehicle in this article to accommodate actuator
faults and model uncertainties. First, a new reaching law is proposed, with
which a sliding mode control (SMC) law is constructed. The proposed reaching
law is made up of a sliding variable and the distance between it and a desig-
nated boundary layer, and it can effectively suppress the unexpected control
chattering while preserving the necessary system tracking performance. Then,
an adaptive SMC scheme is proposed to further solve the fault and uncertainty
compensation problem. The proposed adaptation law helps to prevent overesti-
mation of the adaptive control parameters, as well as avoiding control chattering.
Finally, a number of comparative simulation tests are carried out to validate the
effectiveness and superiority of the proposed control strategy. The demonstrated
quantitative comparison results confirm its advantages.
K E Y W O R D S
actuator fault, adaptive sliding mode control, fault-tolerant control, model uncertainty,
quadrotor UAV
1
INTRODUCTION
Unmanned aerial vehicles (UAVs) have been increasingly popular and widely employed in the industrial and academic
communities in recent years, such as payload transportation,1,2 autonomous aerial refueling,3,4 monitoring and surveil-
lance,5,6 and last-mile delivery.7,8 Quadrotor UAVs have attracted a lot of attention among the various types of UAVs, due
to its ability to perform vertical takeoff and landing and low cost. In addition, many of these applications are deployed in
areas with high safety requirements. As a result, both academia and industry are paying more attention to the safety and
reliability of quadrotor UAVs.9-12 One way to retain high safety and reliability of quadrotor UAVs is to design fault-tolerant
control (FTC) systems.13 The increasing demands on high system performance, safety, and reliability have driven active
research on advanced FTC approaches for safety-critical systems.14-18
This is an open access article under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in any medium, provided the
original work is properly cited.
© 2023 The Authors. International Journal of Robust and Nonlinear Control published by John Wiley & Sons Ltd.
10182
wileyonlinelibrary.com/journal/rnc
Int J Robust Nonlinear Control. 2023;33:10182–10198.

## Page 2

WANG et al.
10183
An overview of the existing FTC strategies for quadrotor UAVs is presented in Reference 19. In general, the com-
monly used FTC strategies for quadrotor UAVs can be divided into two categories: passive and active FTC approaches.
In Reference 20, a sliding mode-based passive FTC scheme is designed for a quadrotor UAV to tolerate actuator faults
and model uncertainties. In Reference 21, both passive and active FTC methods are designed for a commercial quadrotor
under actuator faults based on sliding mode technique, and their advantages and disadvantages are investigated and com-
pared through analytical results. Essentially, passive FTC approaches use the inherent robustness of the designed control
algorithm to mitigate prescribed faults and they may sacrifice tracking control performance under fault-free conditions.
In contrast to passive FTC approaches, active FTC methods can reconfigure the controller in real time to compensate
for faults based on the fault information provided by the fault diagnosis unit. In Reference 22, by combining a recurrent
neural network-based fault estimation technique with a sliding mode feedback controller, an active FTC mechanism is
created for actuator fault accommodation. In Reference 23, to compensate for the loss of effectiveness actuator defect
caused by battery depletion, an active FTC approach based on linear parameter varying control technique is provided.
Although active FTC system can effectively compensate actuator faults, its performance heavily depends on the level of
accuracy of the estimated fault magnitude. The fault estimation error and delay may degrade the FTC performance. To
resolve this issue, many researchers focus on investigating adaptive FTC strategies in recent years. In Reference 24, to
compensate the actuator faults for a quadrotor UAV without the necessity for a fault estimation mechanism, a nonlinear
adaptive FTC approach is developed for altitude and attitude tracking. In Reference 25, the position and attitude tracking
control of a quadrotor UAV is built using an indirect neural network-based adaptive FTC method that can compensate
actuator faults and external disturbances. In Reference 26, an adaptive radial basis function neural network fuzzy sliding
mode control (SMC) scheme is built to accommodate actuator faults for a coaxial octorotor UAV. In Reference 27, an adap-
tive fuzzy backstepping FTC scheme is presented for a modified quadrotor UAV to achieve accommodation of actuator
faults. Despite the fact that the aforementioned control strategies are capable of achieving desired tracking performance
of quadrotor UAVs in the face of actuator faults, the issues of model uncertainties are not adequately investigated.
In addition, fault-tolerance capability is not the only factor to consider when it comes to ensuring the safety control of
quadrotor UAVs. When UAVs are deployed for practical applications, many uncertain factors often occur which may affect
their safety and reliability. One of the challenges for safety control of quadrotor UAVs is to deal with model uncertainties.
To enhance the quadrotor UAVs’ capability for tolerating certain level of model uncertainties, a number of control strate-
gies have been developed. In Reference 28, to manage the attitude and position of a quadrotor UAV while attenuating
parameter changes and uncertainties, a model-free-based terminal SMC technique is designed. In Reference 29, an adap-
tive fuzzy terminal SMC strategy is presented to overcome the quadrotor’s model uncertainties and provide a robust path
tracking performance. In Reference 30, a complementary control strategy based on approximate dynamic programming
is developed to improve the quadrotor UAV tracking performance under model uncertainties. It is worth noting that the
robust tracking control performance of the above mentioned control strategies can only be achieved under fault-free con-
ditions. To further ensure robustness of the developed control strategies, the uncertain factors including actuator faults
and model uncertainties need to be jointly considered.
In this sense, the developed control system for quadrotor UAVs is anticipated to tolerate the adverse impact produced
by actuator faults and model uncertainties for the sake of safety control of quadrotor UAVs. In Reference 31, to mitigate
actuator faults and model uncertainties for a quadrotor UAV, a dual adaptive FTC strategy is developed. In Reference 32,
an active FTC scheme is presented for a quadrotor UAV, in which the model uncertainty is compensated with adaptive
neural network mechanism, and actuator fault information is provided by a fault estimation unit and compensated in an
active way. In Reference 33, a sliding mode observer is designed to estimate the uncertainties induced by actuator faults
and unknown parameters and integrated with the feedback SMC to compensate the adverse effect of actuator faults. SMC
is well known for its robustness against the so-called matched uncertainties. It has been successfully applied in a variety
of fields.34,35 However, the robustness of conventional SMC can only be ensured by selecting a large discontinuous control
gain, which may lead to unanticipated control chattering.36 To solve this problem, a number of adaptive SMC approaches
for accommodating actuator faults and model uncertainties have been presented. In Reference 37, an adaptive SMC with
projection method is designed that ensures constrained estimations of uncertain inertial parameters for a quadrotor.
In Reference 38, for a class of nonlinear systems with actuator faults a multivariable SMC scheme with the aid of an
adaptive single-hidden-layer feedforward network is designed. As reported in Reference 39, a fractional order SMC with
adaptive fuzzy approximation technique is designed for the attitude system of a spacecraft subject to inertia uncertainty
and multiple type actuator faults. In Reference 40, to compensate actuator faults and uncertainties for high-speed trains,
an adaptive fault-tolerant SMC scheme is presented. In Reference 41, a continuous adaptive integral SMC strategy is built
for a space manipulator to achieve trajectory tracking control against actuator uncertainties.
 10991239, 2023, 17, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/rnc.6631 by Pradip Diwan Borase - Netaji Subhas University of Technology, Delhi,Delhi , Wiley Online Library on [07/04/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 3

10184
WANG et al.
Although substantial research studies have been done towards safety control of quadrotor UAVs, there still exist several
problems that need to be solved in order to enhance the safety and reliability of quadrotor UAVs: (1) most of the previous
works using SMC to deal with actuator faults and model uncertainties usually employ a constant discontinuous control
gain, which may lead to a conservative tracking performance in order to avoid control chattering; (2) when utilizing
adaptive SMC technique to mitigate actuator faults and model uncertainties, the discontinuous control component of
SMC is usually overused resulting in unanticipated control chattering; (3) because of the inherent tracking errors, if sliding
variable is used for constructing the adaptive schemes to mitigate actuator faults and uncertainties, it may not be able to
guarantee the convergence of adaptive control parameters.
In an effort to overcome the aforementioned challenges in achieving safety control of quadrotor UAVs, this article
proposes a unique adaptive sliding mode FTC strategy with a new reaching law to jointly compensate both actuator faults
and model uncertainties. The major contributions of this article can be summarized as follows:
(1) A new reaching law is proposed in this article, which can adapt to the variations of the distance between the sliding
variable and the designated boundary layer. It features that when the sliding variable is far away from the desired slid-
ing surface, a large discontinuous control gain is generated for a faster reaching time, and when the sliding variable
approaches to the desired sliding surface, the discontinuous control gain will gradually decrease to zero to suppress
control chattering.
(2) In the existing adaptive sliding mode FTC designs37,42 for quadrotor UAVs, the adaptation law is commonly con-
structed with sliding variable. Because of the inevitable tracking errors, it is possible that the adaptive control
parameters will not be able to converge. To address this issue, inspired by Xu et al.,43 this article proposes an
adaptation law that can prevent overestimation of adaptive control parameters and suppress control chattering.
(3) To achieve actuator fault tolerance, instead of merely adaptively changing the discontinuous control component
of SMC in contrast to the works in References 38 and 44, with the developed control strategy, the continuous and
discontinuous control components are both constructed with adaptive parameters. In this case, the utilization of the
discontinuous control component will be decreased, which can help to prevent control chattering.
The rest of this article is organized as follows. In Section 2, the modeling and system formulation of the researched
quadrotor UAV are presented. In Section 3, the detailed design procedures of the proposed adaptive FTC strategy are
explained. Then, the effectiveness of the proposed control strategy is validated and compared in Section 4 through a series
of simulation tests. Finally, Section 5 summarizes the general conclusions of this article.
2
PROBLEM FORMULATION
This section describes the mathematical modeling of the quadrotor UAV under consideration, as well as the corresponding
system formulation. Figure 1 depicts the researched quadrotor UAV, that is produced by Quanser. It is assembled with
four 10-inch propellers driven by brushless motors in a plus configuration. The motor #1 and #2 spin clockwise (CW),
while the motor #3 and #4 rotate counter-clockwise (CCW). The motors are connected to electric speed controllers that
receive commands from the flight controller in the form of pulse-width modulation (PWM) outputs. The generated thrust
of each individual propeller is varied to control the quadrotor UAV.
2.1
Modeling of quadrotor UAV
Two reference frames, the body-fixed reference frame and the earth-fixed reference frame, are first defined for the
purpose to determine the equations of motion of the quadrotor UAV. The center of gravity of the quadrotor UAV
is chosen as the origin of the body-fixed reference frame, whereas the takeoff point is chosen as the origin of the
earth-fixed reference frame. The axes of the body-fixed reference frame and the earth-fixed reference frame are rep-
resented by (ob, xb, yb, zb) and (oe, xe, ye, ze), respectively. Concentrating on the fault-tolerant attitude control of the
quadrotor UAV, the dynamic equations of motion of the quadrotor UAV are derived as follows using the Newton–Euler
formulation:
𝜏B = I ̇𝜔B + 𝜔B × I𝜔B,
(1)
 10991239, 2023, 17, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/rnc.6631 by Pradip Diwan Borase - Netaji Subhas University of Technology, Delhi,Delhi , Wiley Online Library on [07/04/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 4

WANG et al.
10185
F I G U R E 1
Illustration of the researched quadrotor UAV.
where I is a diagonal matrix denoting the quadrotor UAV’s moment of inertia that is defined as I = diag([Ixx, Iyy, Izz]). 𝜏B =
[𝜏x, 𝜏y, 𝜏z]T, and 𝜔B = [p, q, r]T represent the vector of resultant torques and the vector of angular velocities, respectively,
with respect to the body-fixed reference frame.
The resultant torques operating on the quadrotor UAV are composed of the propeller-generated torques (𝜏T) and the
rotational motion induced torques (𝜏f ), that can be formulated as follows:
𝜏B = 𝜏T + 𝜏f =
⎡
⎢
⎢
⎢⎣
𝜏𝜙
𝜏𝜃
𝜏𝜓
⎤
⎥
⎥
⎥⎦
+
⎡
⎢
⎢
⎢⎣
−kd1 ̇𝜙
−kd2 ̇𝜃
−kd3 ̇𝜓
⎤
⎥
⎥
⎥⎦
,
(2)
where 𝜏𝜙, 𝜏𝜃, 𝜏𝜓are the propeller-generated torques along xb-, yb-, and zb-axis, respectively. 𝜙, 𝜃, 𝜓are the roll, pitch, and
yaw angle of the quadrotor UAV, and kdi (i = 1, 2, 3) is the aerodynamic drag coefficient caused by rotational motion.
The relationship between the propeller-generated torques and the PWM inputs of the electric motors can be
formulated as per the illustrated configuration of the quadrotor UAV in Figure 1 as follows:
⎡
⎢
⎢
⎢⎣
𝜏𝜙
𝜏𝜃
𝜏𝜓
⎤
⎥
⎥
⎥⎦
=
⎡
⎢
⎢
⎢⎣
0
0
KuL
−KuL
KuL
−KuL
0
0
Ky
Ky
−Ky
−Ky
⎤
⎥
⎥
⎥⎦
⎡
⎢
⎢
⎢
⎢
⎢⎣
u1
u2
u3
u4
⎤
⎥
⎥
⎥
⎥
⎥⎦
,
(3)
where ui (i = 1, 2, 3, 4) is the PWM input of the ith motor whose range is [0, 0.05]. A command of 0 corresponds to zero
throttle, which will cause the motors to stop. A command of 0.05 corresponds to full throttle. Ku is the thrust gain related
to the propeller-generated force, Ky is the torque gain related to the reaction torque generated by the propellers, L is the
distance between the individual motor and center of gravity of the quadrotor UAV.
In this sense, substituting Equations (2) and (3) into Equation (1), one can obtain:
⎧
⎪
⎪
⎪
⎨
⎪
⎪
⎪⎩
̇p = (Iyy −Izz)qr
Ixx
+ KuL(u3 −u4)
Ixx
−kd1 ̇𝜙
Ixx
̇q = (Izz −Ixx)pr
Iyy
+ KuL(u1 −u2)
Iyy
−kd2 ̇𝜃
Iyy
̇r = (Ixx −Iyy)pq
Izz
+ Ky(u1 + u2 −u3 −u4)
Izz
−kd3 ̇𝜓
Izz
,
(4)
Furthermore, the following equations can be used to define the relationship between the angular velocities and the
Euler-angle rates:
⎡
⎢
⎢
⎢⎣
̇𝜙
̇𝜃
̇𝜓
⎤
⎥
⎥
⎥⎦
=
⎡
⎢
⎢
⎢⎣
1
sin 𝜙tan 𝜃
cos 𝜙tan 𝜃
0
cos 𝜙
−sin 𝜙
0
sin 𝜙∕cos 𝜃
cos 𝜙∕cos 𝜃
⎤
⎥
⎥
⎥⎦
⎡
⎢
⎢
⎢⎣
p
q
r
⎤
⎥
⎥
⎥⎦
= RE
B
⎡
⎢
⎢
⎢⎣
p
q
r
⎤
⎥
⎥
⎥⎦
,
(5)
where RE
B is a transformation matrix from the body-fixed reference frame to the earth-fixed reference frame.
 10991239, 2023, 17, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/rnc.6631 by Pradip Diwan Borase - Netaji Subhas University of Technology, Delhi,Delhi , Wiley Online Library on [07/04/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 5

10186
WANG et al.
Assume that the changes of the roll and pitch angles are small to facilitate the controller design. Under this
assumption, the transformation matrix RE
B will be close to an identity matrix, and the angular velocities (p, q, r) can be
simply replaced by the Euler-angle rates ( ̇𝜙, ̇𝜃, ̇𝜓). Note that, this assumption is only made for controller design. In this
situation, Equation (4) can be rewritten as follows:
⎧
⎪
⎪
⎪
⎨
⎪
⎪
⎪⎩
̈𝜙= (Iyy −Izz) ̇𝜃̇𝜓
Ixx
+ KuL(u3 −u4)
Ixx
−kd1 ̇𝜙
Ixx
̈𝜃= (Izz −Ixx) ̇𝜙̇𝜓
Iyy
+ KuL(u1 −u2)
Iyy
−kd2 ̇𝜃
Iyy
̈𝜓= (Ixx −Iyy) ̇𝜙̇𝜃
Izz
+ Ky(u1 + u2 −u3 −u4)
Izz
−kd3 ̇𝜓
Izz
.
(6)
2.2
System formulation
Consider a nonlinear quadrotor UAV system with actuator faults and model uncertainties as:
̇x(t) = f(x(t), t) + g(x(t), t)BuLc(t)u(t),
(7)
where x(t) ∈Rn is the state vector, u(t) ∈Rm is the control input vector. f(x(t), t) ∈Rn and g(x(t), t) ∈Rn×n represent
nonlinear functions with model uncertainties. Bu ∈Rn×m is the control efficiency matrix, which is made up of control
input coefficients. Lc(t) = diag([lc1(t), lc2(t), … , lcm(t)]) is a diagonal matrix that represents the level of remaining control
effectiveness of the actuators, where lci(t) (i = 1, 2, … , m) is a scalar satisfying 0 ≤lci(t) ≤1. If the ith actuator encounters
certain level of fault, then 0 ≤lci(t) < 1, otherwise, the ith actuator works well. In the subsequent sections, the notation
(t) is removed for convenience of expression. For example, u(t) is expressed as u.
In order to facilitate the fault-tolerant attitude control design for the quadrotor UAV, define the state vector of the
system as x = [𝜙, ̇𝜙, 𝜃, ̇𝜃, 𝜓, ̇𝜓]T. Thus, the quadrotor UAV system described in Equation (6) can be expressed as a general
integral-chain nonlinear system as follows using this state vector:
⎧
⎪
⎨
⎪⎩
̇x1i = x2i
̇x2i = (h1i + Δh1i)fi(x) + (h2i + Δh2i)x2i + gi𝜈i
𝜈i = BuiLcu,
(8)
where i = 1, 2, 3 represents the roll, pitch, and yaw subsystem, respectively, u = [u1, u2, u3, u4]T, x1i = [𝜙, 𝜃, 𝜓]T, x2i =
[ ̇𝜙, ̇𝜃, ̇𝜓]T. Δh1i and Δh2i represent the model uncertainties of the system induced by the uncertain moments of iner-
tia of the quadrotor UAV, which are bounded as |Δh1i| ≤Δ1 and |Δh2i| ≤Δ2. For the roll subsystem, f1(x) = ̇𝜃̇𝜓, h11 =
(Iyy −Izz)∕Ixx, h21 = −kd1∕Ixx, g1 = 1∕Ixx, Bu1 = [0, 0, KuL, −KuL]. For the pitch subsystem, f2(x) = ̇𝜙̇𝜓, h12 = (Izz −Ixx)∕Iyy,
h22 = −kd2∕Iyy, g2 = 1∕Iyy, Bu2 = [KuL, −KuL, 0, 0]. For the yaw subsystem, f3(x) = ̇𝜙̇𝜃, h13 = (Ixx −Iyy)∕Izz, h23 = −kd3∕Izz,
g3 = 1∕Izz, Bu3 = [Ky, Ky, −Ky, −Ky].
Remark 1. The diagonal matrix Lc is mainly used to model the investigated actuator faults. In the context of adaptive
FTC framework, the main priority is to compensate the fault and may not need to know the actual faulty level of the
actuators. Therefore, the unknown matrix Lc is not used in the developed control law and the following equation 𝜈i = Buiu
is employed to calculate the control law.
3
ADAPTIVE SLIDING MODE FTC STRATEGY
In this section, an adaptive sliding mode FTC strategy is designed to simultaneously compensate actuator faults and
model uncertainties for the investigated quadrotor UAV. Figure 2 depicts an overview of the proposed control strategy. To
achieve the desired attitude control performance, two issues need to be addressed. The first issue is to design a reaching
law-based SMC scheme that ensures the desired system tracking performance while minimizing control chattering under
 10991239, 2023, 17, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/rnc.6631 by Pradip Diwan Borase - Netaji Subhas University of Technology, Delhi,Delhi , Wiley Online Library on [07/04/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 6

WANG et al.
10187
F I G U R E 2
Overview of the proposed adaptive sliding mode FTC scheme.
nominal conditions. The second task is to investigate the adaptive control schemes in order to determine the adaptive
control parameters without overestimation and then to combine them with the developed control law for accommodation
of actuator faults and model uncertainties.
3.1
Design of reaching law-based SMC
In general, the SMC design typically consists of two steps. The initial step involves establishing a sliding surface on which
the system performance can be attained as expected. The second step is to construct an appropriate control law that will
push the sliding variable towards the designed sliding surface, ensuring that the system will satisfy the sliding mode
reaching requirement.
The desired time-varying system trajectory is denoted as xd
1i, and its derivative is assumed to be bounded. The corre-
sponding tracking error states can be described as xe
1i = x1i −xd
1i and xe
2i = x2i −̇xd
1i. With the defined tracking error states,
the integral sliding surface for the considered attitude control system of the quadrotor UAV is designed as:45
si = si0 + zi,
(9)
where si0 is the linear combination of the tracking error states which is formulated as si0 = cixe
1i + xe
2i, and zi includes the
integral term that is determined by Equation (10).
̇zi = −cixe
2i + kc2ixe
2i + kc1ixe
1i
zi(0) = −cixe
1i(t0) −xe
2i(t0),
(10)
where kc1i and kc2i denote the adjustable design parameters, and t0 represents the initial time instant.
Then, combining the above equations, the following equation can be obtained as:
si = si0 + zi
= cixe
1i + xe
2i −cixe
1i(t0) −xe
2i(t0) +
t
∫
t0
(−cixe
2i(𝜏) + kc2ixe
2i(𝜏))d𝜏+
t
∫
t0
xe
1i(𝜏)d𝜏
= cixe
1i + xe
2i −cixe
1i(t0) −xe
2i(t0) −cixe
1i + cixe
1i(t0) + kc2ixe
1i −kc2ixe
1i(t0) +
t
∫
t0
xe
1i(𝜏)d𝜏
= xe
2i + kc2ixe
1i + kc1i
t
∫
t0
xe
1i(𝜏)d𝜏−kc2ixe
1i(t0) −xe
2i(t0).
(11)
Following the construction of the sliding surface, the next step is to design a suitable control law for satisfying the
reaching requirement of the sliding mode. The conventional SMC law is usually made up of two control components,
namely the continuous control component and the discontinuous robust control component. However, a large discontin-
uous control gain will lead to the occurrence of control chattering even though it can increase the robustness of the SMC.
 10991239, 2023, 17, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/rnc.6631 by Pradip Diwan Borase - Netaji Subhas University of Technology, Delhi,Delhi , Wiley Online Library on [07/04/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 7

10188
WANG et al.
In order to address this problem, this article proposes a novel reaching law as follows:
̇si = −
kc3i
𝜂i + (1 + 1∕|si| −𝜂i)e−𝛼i|Δsi| sign(si),
(12)
where kc3i and 𝛼i are positive design parameters, 0 < 𝜂< 1, Δsi = si −Φisat(si), and
sat(si) =
{
sign(si)
if |si| > Φi
si∕Φi
if |si| ≤Φi
(13)
with Φi representing the defined boundary layer thickness.
Remark 2. As can be observed from the afore-defined variable Δsi, it represents the algebraic distance between the current
sliding variable and the designated boundary layer. Δsi is equal to zero when the sliding variable is inside the designated
boundary layer.
Remark 3. With the proposed reaching law, it can be observed from Equation (12) that if Δsi increases, the function
kc3i∕[𝜂i + (1 + 1∕|si| −𝜂i)e−𝛼i|Δsi|] will converge to the value of kc3i∕𝜂i, which is larger than kc3i. As can be seen, a large
discontinuous control gain is used for a faster reaching time if the sliding variable is far away from the specified sliding
surface where the tracking performance is unsatisfactory.
Remark 4. With the decrease of the variable |Δsi|, the function kc3i∕[𝜂i + (1 + 1∕|si| −𝜂i)e−𝛼i|Δsi|] will converge to
kc3i|si|∕(|si| + 1). When the sliding variable is driven onto the desired sliding surface si = 0 by the subsequent designed
control law, the discontinuous control gain will decrease to zero. In this sense, with the sliding variable approach-
ing the desired sliding surface, the discontinuous control gain will gradually decrease to zero to suppress control
chattering.
Based on the defined sliding surface in Equation (11), its time derivative can be calculated as:
̇si = ̇xe
2i + kc2ixe
2i + kc1ixe
1i.
(14)
By recalling the definition of xe
1i and xe
2i, substituting Equations (8) and (12) into Equation (14) leads to:
h1ifi(x) + h2ix2i + giBuiu −̈xd
1i + kc2ixe
2i + kc1ixe
1i = −
kc3i
𝜂i + (1 + 1∕|si| −𝜂i)e−𝛼i|Δsi| sign(si).
(15)
Therefore, by solving Equation (15), the corresponding control law can be designed as follows:
u = B+
uig−1
i
(̈xd
1i −kc1ixe
1i −kc2ixe
2i −h1ifi(x) −h2ix2i −k∗
c3isign(si)) ,
(16)
where B+
ui = BT
ui(BuiBT
ui)−1 and k∗
c3i = kc3i∕[𝜂i + (1 + 1∕|si| −𝜂i)e−𝛼i|Δsi|].
Furthermore, model uncertainties are common in quadrotor UAVs. They might compromise the tracking control
performance of quadrotor UAVs or possibly cause instability of the system. With this in mind, an adaptive control law is
developed to compensate model uncertainties as:
u = B+
uig−1
i
(
̈xd
1i −kc1ixe
1i −kc2ixe
2i −̂h1ifi(x) −̂h2ix2i −k∗
c3isign(si)
)
.
(17)
The corresponding adaptation laws for estimating the uncertain parameters are then designed in the following
manner:
̇̂h1i = 𝛾1ifi(x)Δsi
̇̂h2i = 𝛾2ix2iΔsi,
(18)
where 𝛾1i and 𝛾2i are positive parameters that control the adaptation rate.
 10991239, 2023, 17, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/rnc.6631 by Pradip Diwan Borase - Netaji Subhas University of Technology, Delhi,Delhi , Wiley Online Library on [07/04/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 8

WANG et al.
10189
Theorem 1. Consider an integral-chain nonlinear system in Equation (8) with model uncertainties, given the defined sliding
surface in Equation (11) and the proposed reaching law in Equation (12), an adaptive feedback control law is designed in
Equation (17) that is updated by Equation (18). Therefore, the desired sliding motion will be obtained and system tracking
performance can be ensured with the discontinuous control gain chosen as k∗
c3i = kc3i∕[𝜂i + (1 + 1∕|si| −𝜂i)e−𝛼i|Δsi|].
Proof. Consider the Lyapunov function as:
V1 =
3
∑
i=1
1
2
[
Δs2
i + 1
𝛾1i
(̂h1i −h1i)2 + 1
𝛾2i
(̂h2i −h2i)2
]
.
(19)
Then, considering the condition that Δsi ≠0, that is, the sliding variable is outside the boundary layer, and recalling
the control law in Equation (17) and the adaptation law in Equation (18), the time derivative of V1 can be calculated as:
̇V1 =
3
∑
i=1
[
ΔsiΔ̇si + 1
𝛾1i
(̂h1i −h1i) ̇̂h1i + 1
𝛾2i
(̂h2i −h2i) ̇̂h2i
]
=
3
∑
i=1
[
Δsi
(
h1ifi(x) + h2ix2i −̂h1ifi(x) −̂h2ix2i −k∗
c3isign(si)
)
+ 1
𝛾1i
(̂h1i −h1i) ̇̂h1i + 1
𝛾2i
(̂h2i −h2i) ̇̂h2i
]
=
3
∑
i=1
[(
̂h1i −h1i
) ( ̇̂h1i
𝛾1i
−fi(x)Δsi
)
+
(
̂h2i −h2i
) ( ̇̂h2i
𝛾2i
−x2iΔsi
)
−k∗
c3isign(si)Δsi
]
=
3
∑
i=1
[−k∗
c3i|Δsi|] < 0.
(20)
As a result, in the presence of certain level of model uncertainties with bounded Δ1 and Δ2, the system’s stability can
be guaranteed by using the developed control law and adaptation law with reasonable adaptation rate.
▪
3.2
Adaptive fault-tolerant SMC
Considering the occurrence of actuator faults in the quadrotor UAV, the diagonal matrix Lc, which measures the fault
severity of the actuators, is not an identity matrix. One way to achieve FTC purpose of compensating the negative effect of
actuator faults is to use a fault diagnosis unit to estimate the actual value of Lc and incorporate it with the developed control
law. In practice, however, there may be a significant time delay in obtaining the essential fault information. Moreover,
there may be fault estimation inaccuracies, which would have an impact on the relevant control performance. In this
section, an adaptive FTC technique is proposed for the studied quadrotor UAV to tolerate actuator faults without the need
for fault information.
Under this condition, Equation (8) can be rewritten as:
⎧
⎪
⎨
⎪⎩
̇x1i = x2i
̇x2i = (h1i + Δh1i)fi(x) + (h2i + Δh2i)x2i + gi(𝜈d
i + 𝜈e
i )
𝜈i = BuiIcu −Bui(Ic −Lc)u,
(21)
where Ic is an identity matrix with the same dimension as Lc, 𝜈i = 𝜈d
i + 𝜈e
i denotes the actual virtual control signal gen-
erated by the individual actuators under the actuator faulty condition, 𝜈d
i = BuiIcu represents the desired virtual control
signal derived from the developed control law without considering the actuator faults, 𝜈e
i = −Bui(Ic −Lc)u represents the
virtual control signal error due to the occurrence of actuator faults.
As can be observed from Equation (21), to mitigate the negative effects of virtual control signal error induced by
actuator faults while maintaining the desired system tracking control performance, one intuitive way is to adaptively
adjust the parameter gi. In this case, let gi𝜈e
i = ̃gi𝜈d
i , and Equation (21) can be reconstructed as follows:
̇x2i = (h1i + Δh1i)fi(x) + (h2i + Δh2i)x2i + (gi + ̃gi)𝜈d
i = (h1i + Δh1i)fi(x) + (h2i + Δh2i)x2i + ̂gi𝜈d
i ,
(22)
where ̂gi represents the estimation of gi, and ̃gi = ̂gi −gi denotes the estimation error.
 10991239, 2023, 17, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/rnc.6631 by Pradip Diwan Borase - Netaji Subhas University of Technology, Delhi,Delhi , Wiley Online Library on [07/04/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 9

10190
WANG et al.
Under this condition, instead of using gi for developing the feedback control law, the estimated parameter ̂gi
should be employed to compensate the actuator faults and maintain the original tracking control performance of
the closed-loop system. Moreover, recalling the developed control law in Equation (17), the parameters ̂h1i and
̂h2i need to be utilized in conjunction with ̂gi to develop the control law for compensation of actuator faults and
model uncertainties. Therefore, by denoting ̂Γi = ̂g−1
i
̂h1i, ̂Υi = ̂g−1
i
̂h2i, and ̂Ψi = ̂g−1
i , the feedback control law can be
developed as:
u = B+
ui ̂Ψi
(̈xd
1i −kc1ixe
1i −kc2ixe
2i −k∗
c3isign(si)) −B+
ui ̂Γifi(x) −B+
ui ̂Υix2i.
(23)
The corresponding adaptation laws for uncertain parameter estimation are designed as:
̇̂Γi = 𝜌1ifi(x)Δsi,
̇̂Υi = 𝜌2ix2iΔsi,
̇̂Ψi = 𝜌3i
(kc1ixe
1i + kc2ixe
2i −̈xd
1i + k∗
c3isign(si)) Δsi,
(24)
where 𝜌1i, 𝜌2i, and 𝜌3i are positive parameters for tuning the adaptation rate.
Remark 5. As can be seen from the developed feedback control law in Equation (23), rather than adaptively adjust-
ing the discontinuous control gain to compensate actuator faults, ̂Ψi and k∗
c3i are treaded together as the discontinuous
control gain and ̂Ψi is adaptively estimated. Since ̂Ψi is employed in both continuous and discontinuous control com-
ponents, both of them will contribute to compensate the actuator faults after fault occurrence. In this sense, the
utilization of the discontinuous control component will be decreased, which can contribute to preventing control
chattering.
Theorem 2. Consider an integral-chain nonlinear quadrotor UAV system in Equation (8) with actuator faults and model
uncertainties. Given the proposed reaching law in Equation (12), by utilizing the developed feedback control law in Equation
(23) and the adaptation law in Equation (24), the desired system tracking control performance can be achieved in spite of
actuator faults and model uncertainties.
Proof. A Lyapunov function is selected as:
V2 =
3
∑
i=1
1
2
[
Δs2
i +
1
𝜌1iΨi
̃Γ2
i +
1
𝜌2iΨi
̃Υ2
i +
1
𝜌3iΨi
̃Ψ
2
i
]
,
(25)
where ̃Γi = ̂Γi −Γi, ̃Υi = ̂Υi −Υi, and ̃Ψi = ̂Ψi −Ψi.
For simplicity of analysis, V2 is divided into four components as:
V2 = V21 + V22 + V23 + V24,
(26)
where V21 = ∑3
i=1Δs2
i ∕2, V22 = ∑3
i=1 ̃Γ2
i ∕(2𝜌1iΨi), V23 = ∑3
i=1 ̃Υ2
i ∕(2𝜌2iΨi), and V24 = ∑3
i=1 ̃Ψ
2
i ∕(2𝜌3iΨi).
First, recalling Equation (23), the time derivative of V21 is calculated as:
̇V21 =
3
∑
i=1
Δsi[ ̇xe
2i + kc2ixe
2i + kc1ixe
1i]
=
3
∑
i=1
Δsi[Ψ−1
i Γifi(x) + Ψ−1
i Υix2i + Ψ−1
i [ ̂Ψi(̈xd
1i −kc1ixe
1i −kc2ixe
2i −k∗
c3isign(si))
−̂Γifi(x) −̂Υix2i] −̈xd
1i + kc2ixe
2i + kc1ixe
1i]
=
3
∑
i=1
Δsi[Ψ−1
i fi(x)(Γi −̂Γi) + Ψ−1
i x2i(Υi −̂Υi) −k∗
c3isign(si)
+ (1 −Ψ−1
i
̂Ψi)(kc2ixe
2i + kc1ixe
1i −̈xd
1i + k∗
c3isign(si))].
(27)
 10991239, 2023, 17, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/rnc.6631 by Pradip Diwan Borase - Netaji Subhas University of Technology, Delhi,Delhi , Wiley Online Library on [07/04/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 10

WANG et al.
10191
Then, employing the adaptation law in Equation (24), one can obtain that:
̇V22 + ̇V23 + ̇V24 =
3
∑
i=1
[Ψ−1
i (̂Γi −Γi) ̇̂Γi∕𝜌1i + Ψ−1
i ( ̂Υi −Υi) ̇̂Υi∕𝜌2i + Ψ−1
i ( ̂Ψi −Ψi) ̇̂Ψi∕𝜌3i]
=
3
∑
i=1
[Ψ−1
i ( ̂Ψi −Ψi)(kc1ixe
1i + kc2ixe
2i −̈xd
1i + k∗
c3isign(si))Δsi
+ Ψ−1
i (̂Γi −Γi)fi(x)Δsi + Ψ−1
i ( ̂Υi −Υi)x2iΔsi].
(28)
Combining Equations (27) and (28) and considering the condition that Δsi ≠0, it gives:
̇V2 =
3
∑
i=1
Δsi[Ψ−1
i (Γi −̂Γi)fi(x) + Ψ−1
i (Υi −̂Υi)x2i + (1 −Ψ−1
i
̂Ψi)(kc2ixe
2i + kc1ixe
1i −̈xd
1i + k∗
c3isign(si)) −k∗
c3isign(si)
+ Ψ−1
i ( ̂Ψi −Ψi)(kc1ixe
1i + kc2ixe
2i −̈xd
1i + k∗
c3isign(si)) + Ψ−1
i (̂Γi −Γi)fi(x) + Ψ−1
i ( ̂Υi −Υi)x2i]
=
3
∑
i=1
Δsi[Ψ−1
i (Γi −̂Γi)fi(x) + Ψ−1
i (Υi −̂Υi)x2i + (1 −Ψ−1
i
̂Ψi)(kc2ixe
2i + kc1ixe
1i −̈xd
1i + k∗
c3isign(si)) −k∗
c3isign(si)
−(1 −Ψ−1
i
̂Ψi)(kc2ixe
2i + kc1ixe
1i −̈xd
1i + k∗
c3isign(si)) −Ψ−1
i (Γi −̂Γi)fi(x) −Ψ−1
i (Υi −̂Υi)x2i]
=
3
∑
i=1
Δsi[−k∗
c3isign(si)].
(29)
For the above equation, we have the following two conditions. If si > Φi, then sign(si) = 1, sat(si) = 1, and sign(si)Δsi =
Δsi = si −Φisat(si) = si −Φi > 0. In this case, we can get that sign(si)Δsi = Δsi = |Δsi|. If si < −Φi, then sign(si) = −1,
sat(si) = −1, and sign(si)Δsi = −Δsi = −(si −Φisat(si)) = −(si + Φi) > 0. In this case, we can obtain that sign(si)Δsi =
−Δsi = |Δsi|. Based on above analysis, we can get that no matter Δsi is positive or negative, we can always guarantee that
Δsisign(si) = |Δsi|. Therefore, Equation (29) can be rewritten as:
̇V2 =
3
∑
i=1
[−k∗
c3i|Δsi|] < 0.
(30)
As a result, under the influence of certain level of actuator faults and model uncertainties with bounded Δ1 and
Δ2, system stability can be maintained from any initial conditions by using the proposed adaptive control strategy with
reasonable adaptation rate.
▪
Remark 6. As per the definition of the designed variable Δsi, by employing this variable for constructing the adaptation
law in Equation (24), the adaptation will be ceased as long as the sliding variable is inside the defined boundary, which
can help to avoid overestimation of the discontinuous control gain. As a result, the proposed adaptive scheme can avoid
control chattering as compared to the existing adaptive SMC methods in the literature, in which it is difficult to guarantee
the adaptation convergence due to the use of sliding variable for adaptation law formulation and the inevitable tracking
errors.
4
SIMULATION RESULTS AND DISCUSSIONS
A series of simulation tests are undertaken to quantitatively examine the effectiveness of the proposed adaptive
fault-tolerant control method (PAFTC) for mitigating actuator faults and model uncertainties of the quadrotor
UAV. Table 1 lists the physical specifications of the quadrotor UAV under investigation. For the sake of compar-
ison and demonstrating the advantages of PAFTC, the performance of the SMC constructed with the proposed
reaching law (SMCRL) and a nominal adaptive SMC whose adaptation law is formulated with sliding variable
(NASMC)42 are investigated as well. The control parameters of PAFTC are set as follows: 𝜂1 = 0.1, 𝛼1 = 10, kc11 = 100,
kc21 = 20, kc31 = 1, Φ1 = 0.1, 𝜌11 = 𝜌21 = 𝜌31 = 1, ̂Γ1(0) = ̂Υ1(0) = 0, ̂Ψ1(0) = 0.03, 𝜂2 = 0.1, 𝛼2 = 10, kc12 = 100, kc22 = 20,
kc32 = 1, Φ2 = 0.1, 𝜌12 = 𝜌22 = 𝜌32 = 1, ̂Γ2(0) = ̂Υ2(0) = 0, ̂Ψ2(0) = 0.03, 𝜂3 = 0.1, 𝛼3 = 10, kc13 = 100, kc23 = 20, kc33 = 1,
 10991239, 2023, 17, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/rnc.6631 by Pradip Diwan Borase - Netaji Subhas University of Technology, Delhi,Delhi , Wiley Online Library on [07/04/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 11

10192
WANG et al.
TA B L E 1
Physical specifications of the researched quadrotor UAV.
Symbols
Interpretations
Values
I = diag([Ixx, Iyy, Izz])
Moment of inertia
I = diag([0.03, 0.03, 0.04]) kg ⋅m2
L
Distance between motor and center of gravity
0.2 m
Ku
Thrust gain
120 N
Ky
Torque gain
4 N ⋅m
Φ3 = 0.1, 𝜌13 = 𝜌23 = 𝜌33 = 1, ̂Γ3(0) = ̂Υ3(0) = 0, ̂Ψ3(0) = 0.04. The non-adaptive parameters of SMCRL and NASMC are
chosen the same as those of PAFTC. The following two scenarios are used to demonstrate the effectiveness of the proposed
control strategy. Furthermore, for the purpose of quantitatively evaluating the tracking performance of the demonstrated
control approaches, an index indicating the root mean squared error (RMSE) of the attitude tracking is specified as:
eRMSE =
√
√
√
√
√
√
1
t1 −t0
t1
∫
t0
|xd
1i −x1i|2d𝜏,
(31)
where [t0, t1] spans the entire time frame of the simulation test.
In Scenario 1, a 20% loss of control effectiveness fault is injected into actuator #1 at 10 s and actuator #4 at 20 s, the
uncertain parameters for drag forces are set to kdi = 0.2 (i = 1, 2, 3), and the model uncertainties for inertial moments
are set to ΔI = 0.5I and injected into the attitude system at 15 s. The detailed tracking performance of roll, pitch, and
yaw motions are demonstrated in Figure 3. After faults occurrence, the PAFTC can instantaneously change both the
discontinuous control gain as shown in Figure 3D and the adaptive control parameters as illustrated in Figure 4 to mitigate
the negative impact caused by actuator faults and retain the original system tracking performance. In addition, both
the compared SMCRL and NASMC can retain the appropriate system tracking performance as well. However, as shown
in Figure 5, the compared NASMC induces control chattering because of the employment of a sliding variable in the
adaptation law formulation. Figure 3 shows that the PAFTC developed in this article outperforms the compared SMCRL
and NASMC with less tracking errors and avoidance of control chattering. Moreover, both the PAFTC and SMCRL use the
same reaching law for SMC development, however, the PAFTC has less tracking errors than the SMCRL. This is because
in the PAFTC, the developed adaptation law is incorporated in both continuous and discontinuous control components of
SMC, which can contribute to compensating actuator faults without merely relying on the robustness of the discontinuous
control component of SMC.
In Scenario 2, a larger actuator fault with 35% loss of control effectiveness is injected into actuator #1 at 10 s and
actuator #4 at 20 s, respectively, to further test the effectiveness and capability of the proposed control method. More-
over, when compared to Scenario 1, the uncertain parameters for drag forces are adjusted with a bigger amplitude
and time-varying property. The uncertain parameters are set as kdi = 10 sin(0.2𝜋t) (i = 1, 2, 3), and the uncertain iner-
tial moments are the same as those in Scenario 1. The corresponding tracking performance of roll, pitch, and yaw
motions are demonstrated in Figure 6. Compared to Scenario 1, due to the increased severity of actuator faults and
model uncertainties, the compared SMCRL is more affected and exhibits large tracking errors. Nevertheless, under
this faulty and uncertain condition, although the compared NASMC can track the desired trajectory, it exhibits oscil-
latory tracking errors. As can be observed from Figure 8, the compared NASMC uses more control effort and induces
severe control chattering. In contrast, the PAFTC is still able to retain the necessary tracking performance with mod-
est tracking deviations. Figures 7 and 6D demonstrate the change of adaptive control parameters and discontinuous
control gain, which are bigger than those in Scenario 1 because of the increased severity of actuator faults and model
uncertainties.
Table 2 summarizes the performance indices related to the roll, pitch, and yaw tracking. Taking roll motion control
in Scenario 1 as an example, compared to SMCRL and NASMC, the PAFTC has improved the RMSE of roll angle from
0.1466◦and 0.1297◦to 0.0611◦with the enhancement rate of 58.32% and 52.89%, respectively. As per the performance
indices in Table 2, the PAFTC can ensure the desired tracking performance of the quadrotor UAV even under the unfa-
vorable conditions involving actuator faults, inertial moment variations, and time-varying drag forces. In addition, the
quantitative comparison results confirm the effectiveness and superiority of the PAFTC.
 10991239, 2023, 17, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/rnc.6631 by Pradip Diwan Borase - Netaji Subhas University of Technology, Delhi,Delhi , Wiley Online Library on [07/04/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 12

WANG et al.
10193
(A)
(B)
(C)
(D)
F I G U R E 3
Tracking performance of quadrotor UAV in Scenario 1. (A) Roll motion responses; (B) pitch motion responses; (C) yaw
motion responses; (D) change of discontinuous control gain.
(A)
(B)
(C)
(D)
F I G U R E 4
Change of adaptive control parameter and sliding variable of PAFTC in Scenario 1. (A) Roll motion related adaptive control
parameter; (B) pitch motion related adaptive control parameter; (C) yaw motion related adaptive control parameter; (D) change of sliding
variable.
 10991239, 2023, 17, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/rnc.6631 by Pradip Diwan Borase - Netaji Subhas University of Technology, Delhi,Delhi , Wiley Online Library on [07/04/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 13

10194
WANG et al.
(A)
(B)
(C)
F I G U R E 5
Control inputs of quadrotor UAV in Scenario 1. (A) control inputs with SMCRL; (B) control inputs with NASMC; (C)
control inputs with PAFTC.
(A)
(B)
(C)
(D)
F I G U R E 6
Tracking performance of quadrotor UAV in Scenario 2. (A) Roll motion responses; (B) pitch motion responses; (C) yaw
motion responses; (D) change of discontinuous control gain.
 10991239, 2023, 17, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/rnc.6631 by Pradip Diwan Borase - Netaji Subhas University of Technology, Delhi,Delhi , Wiley Online Library on [07/04/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 14

WANG et al.
10195
(A)
(B)
(C)
(D)
F I G U R E 7
Change of adaptive control parameter and sliding variable of PAFTC in Scenario 2. (A) Roll motion related adaptive control
parameter; (B) pitch motion related adaptive control parameter; (C) yaw motion related adaptive control parameter; (D) change of sliding
variable.
(A)
(B)
(C)
F I G U R E 8
Control inputs of quadrotor UAV in Scenario 2. (A) Control inputs with SMCRL; (B) control inputs with NASMC; (C)
control inputs with PAFTC.
 10991239, 2023, 17, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/rnc.6631 by Pradip Diwan Borase - Netaji Subhas University of Technology, Delhi,Delhi , Wiley Online Library on [07/04/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 15

10196
WANG et al.
TA B L E 2
Comparison of performance indices.
Scenario
SMCRL
NASMC
PAFTC
Enhancement rate
Scenario 1
RMSE of 𝜙
0.1466◦
0.1297◦
0.0611◦
58.32%&52.89%
RMSE of 𝜃
0.1558◦
0.1169◦
0.0603◦
61.29%&48.42%
RMSE of 𝜓
0.1110◦
0.0372◦
0.0349◦
68.56%&6.18%
Scenario 2
RMSE of 𝜙
0.8525◦
0.1784◦
0.0834◦
90.22%&53.25%
RMSE of 𝜃
1.1838◦
0.2750◦
0.0669◦
94.35%&75.67%
RMSE of 𝜓
0.1707◦
0.0443◦
0.0379◦
77.79%&14.45%
5
CONCLUSIONS
An adaptive sliding mode FTC strategy for a quadrotor UAV is proposed in this article to compensate both actuator faults
and model uncertainties. First, a new reaching law is proposed to achieve a fast reaching time while avoiding control
chattering. Based on the proposed reaching law, a baseline SMC law is developed, which can effectively suppress the unex-
pected control chattering. Then, to further address the problem of compensating actuator faults and model uncertainties,
an adaptive FTC scheme is proposed to mitigate the adverse impact of both actuator faults and model uncertainties. With
the aid of the proposed adaptation law, overestimation of the uncertain adaptive control parameters can be prevented.
Finally, the effectiveness and advantages of the proposed control strategy are demonstrated in a series of comparative
simulation tests, in which the quadrotor UAV is exposed to different level of actuator faults, inertial moment variations,
and time-varying drag forces.
CONFLICT OF INTEREST STATEMENT
The authors declare that there is no potential conflict of interest.
DATA AVAILABILITY STATEMENT
The data that support the findings of this study are available from the corresponding author upon reasonable request.
ORCID
Ban Wang
https://orcid.org/0000-0001-8002-1263
Youmin Zhang
https://orcid.org/0000-0002-9731-5943
REFERENCES
1. Chen T, Shan JJ, Liu HH. Cooperative transportation of a flexible payload using two quadrotors. J Guid Control Dyn. 2021;44(11):2099-2107.
2. Villa DK, Brandao AS, Sarcinelli-Filho M. A survey on load transportation using multirotor UAVs. J Intell Robot Syst. 2020;98(2):
267-296.
3. Dai X, Quan Q, Ren J, Cai KY. Iterative learning control and initial value estimation for probe–drogue autonomous aerial refueling of
UAVs. Aerosp Sci Technol. 2018;82:583-593.
4. Ren J, Quan Q, Ma H, Cai KY. Additive-state-decomposition-based station-keeping control for autonomous aerial refueling. Sci China Inf
Sci. 2021;64(11):1-3.
5. Yuan C, Zhang YM, Liu Z. A survey on technologies for automatic forest fire monitoring, detection, and fighting using unmanned aerial
vehicles and remote sensing techniques. Can J For Res. 2015;45(7):783-792.
6. Kim H, Mokdad L, Ben-Othman J. Designing UAV surveillance frameworks for smart city and extensive ocean with differential
perspectives. IEEE Commun Mag. 2018;56(4):98-104.
7. Ortiz S, Calafate CT, Cano JC, Manzoni P, Toh CK. A UAV-based content delivery architecture for rural areas and future smart cities. IEEE
Internet Comput. 2018;23(1):29-36.
8. Wang B, Zhang YM, Zhang W. Integrated path planning and trajectory tracking control for quadrotor UAVs with obstacle avoidance in
the presence of environmental and systematic uncertainties: theory and experiment. Aerosp Sci Technol. 2022;120:107277.
9. Zhao X, Zong Q, Tian B, Wang D, You M. Finite-time fault-tolerant formation control for multiquadrotor systems with actuator fault. Int
J Robust Nonlinear Control. 2018;28(17):5386-5405.
10. Shao X, Liu N, Liu J, Wang H. Model-assisted extended state observer and dynamic surface control–based trajectory tracking for quadrotors
via output-feedback mechanism. Int J Robust Nonlinear Control. 2018;28(6):2404-2423.
 10991239, 2023, 17, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/rnc.6631 by Pradip Diwan Borase - Netaji Subhas University of Technology, Delhi,Delhi , Wiley Online Library on [07/04/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 16

WANG et al.
10197
11. Zhao J, Ding X, Jiang B, Jiang G, Xie F. A novel control strategy for quadrotors with variable mass and external disturbance. Int J Robust
Nonlinear Control. 2021;31(17):8605-8631.
12. Tian B, Cui J, Lu H, Zuo Z, Zong Q. Adaptive finite-time attitude tracking of quadrotors with experiments and comparisons. IEEE Trans
Ind Electron. 2019;66(12):9428-9438.
13. Zhang YM, Jiang J. Bibliographical review on reconfigurable fault-tolerant control systems. Annu Rev Control. 2008;32(2):229-252.
14. Zhang YM, Luo D. Editorial of special issue on UAV autonomous, intelligent and safe control. Guid Navig Control. 2021;1(4):2102001.
15. Edwards C, Lombaerts T, Smaili H. Fault Tolerant Flight Control: A Benchmark Challenge. Springer-Verlag; 2010.
16. Chen L, Alwi H, Edwards C. Development and evaluation of an integral sliding mode fault-tolerant control scheme on the RECONFIGURE
benchmark. Int J Robust Nonlinear Control. 2019;29(16):5314-5340.
17. Alwi H, Edwards C, Stroosma O, Mulder J, Hamayun MT. Real-time implementation of an ISM fault-tolerant control scheme for LPV
plants. IEEE Trans Ind Electron. 2014;62(6):3896-3905.
18. Chen L, Edwards C, Alwi H, Sato M. Flight evaluation of a sliding mode online control allocation scheme for fault tolerant control.
Automatica. 2020;114:108829.
19. Zhang YM, Chamseddine A, Rabbath CA, et al. Development of advanced FDD and FTC techniques with application to an unmanned
quadrotor helicopter testbed. J Frankl Inst. 2013;350(9):2396-2422.
20. Merheb AR, Noura H, Bateman F. Design of passive fault-tolerant controllers of a quadrotor based on sliding mode theory. Int J Appl Math
Comput Sci. 2015;25(3):561-576.
21. Li T, Zhang YM, Gordon BW. Passive and active nonlinear fault-tolerant control of a quadrotor unmanned aerial vehicle based on the
sliding mode control technique. Proc Inst Mech Eng I J Syst Control Eng. 2013;227(1):12-23.
22. Wang B, Shen YY, Zhang YM. Active fault-tolerant control for a quadrotor helicopter against actuator faults and model uncertainties.
Aerosp Sci Technol. 2020;99:105745.
23. Liu Z, Yuan C, Zhang YM. Active fault-tolerant control of unmanned quadrotor helicopter using linear parameter varying technique.
J Intell Robot Syst. 2017;88(2-4):415.
24. Avram RC, Zhang X, Muse J. Nonlinear adaptive fault-tolerant quadrotor altitude and attitude tracking with multiple actuator faults. IEEE
Trans Control Syst Technol. 2017;26(2):701-707.
25. Song Y, He L, Zhang D, Qian J, Fu J. Neuroadaptive fault-tolerant control of quadrotor UAVs: a more affordable solution. IEEE Trans
Neural Netw Learn Syst. 2018;30(7):1975-1983.
26. Zeghlache S, Mekki H, Bouguerra A, Djerioui A. Actuator fault tolerant control using adaptive RBFNN fuzzy sliding mode controller for
coaxial octorotor UAV. ISA Trans. 2018;80:267-278.
27. Zeghlache S, Djerioui A, Benyettou L, Benslimane T, Mekki H, Bouguerra A. Fault tolerant control for modified quadrotor via adaptive
type-2 fuzzy backstepping subject to actuator faults. ISA Trans. 2019;95:330-345.
28. Wang H, Ye X, Tian Y, Zheng G, Christov N. Model-free–based terminal SMC of quadrotor attitude and position. IEEE Trans Aerosp
Electron Syst. 2016;52(5):2519-2528.
29. Nekoukar V, Dehkordi NM. Robust path tracking of a quadrotor using adaptive fuzzy terminal sliding mode control. Control Eng Pract.
2021;110:104763.
30. Guo Y, Chen G, Zhao T. Learning-based collision-free coordination for a team of uncertain quadrotor UAVs. Aerosp Sci Technol.
2021;119:107127.
31. Wang B, Yu X, Mu L, Zhang YM. A dual adaptive fault-tolerant control for a quadrotor helicopter against actuator faults and model
uncertainties without overestimation. Aerosp Sci Technol. 2020;99:105744.
32. Zhong Y, Liu Z, Zhang YM, Zhang W, Zuo J. Active fault-tolerant tracking control of a quadrotor with model uncertainties and actuator
faults. Front Inf Technol Electron Eng. 2019;20(1):95-106.
33. Chen FY, Zhang K, Wang Z, Tao G, Jiang B. Trajectory tracking of a quadrotor with unknown parameters and its fault-tolerant control via
sliding mode fault observer. Proc Inst Mech Eng I J Syst Control Eng. 2015;229(4):279-292.
34. Alwi H, Edwards C. Sliding mode fault-tolerant control of an octorotor using linear parameter varying-based schemes. IET Control Theory
Appl. 2015;9(4):618-636.
35. Hamayun MT, Edwards C, Alwi H. Design and analysis of an integral sliding mode fault-tolerant control scheme. IEEE Trans Autom
Control. 2011;57(7):1783-1789.
36. Zhang X, Sun L, Zhao K, Sun L. Nonlinear speed control for PMSM system using sliding-mode control and disturbance compensation
techniques. IEEE Trans Power Electron. 2012;28(3):1358-1365.
37. Zou Y. Nonlinear robust adaptive hierarchical sliding mode control approach for quadrotors. Int J Robust Nonlinear Control.
2017;27(6):925-941.
38. Guo K, Lyu S, Yu X, Qiao J, Guo L, Zhang YM. Fault-tolerant control design for a class of nonlinear systems with actuator malfunctions.
Int J Robust Nonlinear Control. 2022;32(5):2828-2844.
39. Qian M, Shi Y, Gao Z, Zhang X. Integrated fault tolerant tracking control for rigid spacecraft using fractional order sliding mode technique.
J Frankl Inst. 2020;357(15):10557-10583.
40. Mao Z, Yan XG, Jiang B, Chen M. Adaptive fault-tolerant sliding-mode control for high-speed trains with actuator faults and uncertainties.
IEEE Trans Intell Transp Syst. 2019;21(6):2449-2460.
41. Jia S, Shan JJ. Continuous integral sliding mode control for space manipulator with actuator uncertainties. Aerosp Sci Technol.
2020;106:106192.
 10991239, 2023, 17, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/rnc.6631 by Pradip Diwan Borase - Netaji Subhas University of Technology, Delhi,Delhi , Wiley Online Library on [07/04/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 17

10198
WANG et al.
42. L’afflitto A, Anderson RB, Mohammadi K. An introduction to nonlinear robust control for unmanned quadrotor aircraft: How to design
control algorithms for quadrotors using sliding mode control and adaptive control techniques. IEEE Control Syst Mag. 2018;38(3):102-121.
43. Xu JX, Jia QW, Lee TH. On the design of a nonlinear adaptive variable structure derivative estimator. IEEE Trans Autom Control.
2000;45(5):1028-1033.
44. Li P, Yu X, Zhang YM, Peng X. Adaptive multivariable integral TSMC of a hypersonic gliding vehicle with actuator faults and model
uncertainties. IEEE/ASME Trans Mechatron. 2017;22(6):2723-2735.
45. Utkin V, Shi J. Integral sliding mode in systems operating under uncertainty conditions. Proceedings of the 35th Conference on Decision
and Control; 1996:4591–4596.
How to cite this article: Wang B, Shen Y, Li N, Zhang Y, Gao Z. An adaptive sliding mode fault-tolerant control
of a quadrotor unmanned aerial vehicle with actuator faults and model uncertainties. Int J Robust Nonlinear
Control. 2023;33(17):10182-10198. doi: 10.1002/rnc.6631
 10991239, 2023, 17, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/rnc.6631 by Pradip Diwan Borase - Netaji Subhas University of Technology, Delhi,Delhi , Wiley Online Library on [07/04/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
