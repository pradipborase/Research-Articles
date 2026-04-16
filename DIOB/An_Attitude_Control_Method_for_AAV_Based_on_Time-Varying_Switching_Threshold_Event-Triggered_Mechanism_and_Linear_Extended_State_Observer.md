# An_Attitude_Control_Method_for_AAV_Based_on_Time-Varying_Switching_Threshold_Event-Triggered_Mechanism_and_Linear_Extended_State_Observer.pdf

## Page 1

5744
IEEE TRANSACTIONS ON AUTOMATION SCIENCE AND ENGINEERING, VOL. 23, 2026
An Attitude Control Method for AAV Based on
Time-Varying Switching Threshold Event-Triggered
Mechanism and Linear Extended State Observer
Xiangze Lin , Weili Fu , Junwen Tu , and Ju H. Park , Senior Member, IEEE
Abstract—To address the dual challenges of tracking accuracy
and resource eﬃciency for quadrotor autonomous aerial vehicle
(AAV) attitude control, an event-triggered based control strategy
combining backstepping sliding mode control (BSMC) with a
linear extended state observer (LESO) is proposed. With a
quadrotor AAV dynamic model established via Euler-Newton
equations, a BSMC which combines sliding mode control and
backstepping is proposed to guarantee stability of AAV and a
LESO is used for real-time compensation of total disturbances
to improve tracking accuracy. Moreover, a time-varying threshold
event-triggered (TVST) mechanism is also deliberately developed
to reduce controller update frequency while maintaining the
system performance. The proposed methed is an emulation one
which signiﬁcantly reduces the communication and computation
burden and avoid the unnecessary wear and tear of the actua-
tor. Simulations and experimental results demonstrate that the
proposed control strategy achieves an eﬀective balance between
tracking accuracy and resource conservation.
Note to Practitioners—In practical applications, the introduc-
tion of event-triggered mechanism (ETM) in AAV control to
conserve communication resources may come at the cost of
reduced tracking accuracy. The dual optimization problem of
control accuracy and resource conservation for quadrotor AAVs
is addressed through the proposal of a TVST ETM within
the the LESO based BSMC (LESO-BSMC) framework. The
designed method features diﬀerentiated controllers for various
triggering conditions, which not only ensures high-precision
trajectory tracking but also signiﬁcantly reduces communication
and computational loads. This approach achieves an eﬀective
balance between system performance and transmission resource
demands, consequently better satisfying practical operational
needs.
Index Terms—Quadrotor AAV, linear extended state observer,
backstepping sliding mode, attitude control, time-varying switch-
ing threshold.
Received 14 October 2025; revised 30 December 2025; accepted 25 Febru-
ary 2026. Date of publication 2 March 2026; date of current version 11 March
2026. This article was recommended for publication by Associate Editor Y.
Huang and Editor M. Dotoli upon evaluation of the reviewers’ comments.
This work was supported by the Natural Science Foundation of China under
Grant 62173185 and Grant 61773216. The work of Ju H. Park was supported
by the National Research Foundation of Korea (NRF) grant funded by
Korean Government (Ministry of Science and Information and Communica-
tions Technology) under Grant RS-2023-00208078. (Corresponding authors:
Xiangze Lin; Ju H. Park.)
Xiangze Lin, Weili Fu, and Junwen Tu are with the College of Artiﬁcial
Intelligence, Nanjing Agricultural University, Nanjing 210031, China (e-mail:
xzlin@njau.edu.cn).
Ju H. Park is with the Department of Electrical Engineering, Yeungnam
University, Gyeongsan 38541, South Korea (e-mail: jessie@ynu.ac.kr).
Digital Object Identiﬁer 10.1109/TASE.2026.3669624
I. INTRODUCTION
A
AVs have been widely applied in power line inspection
[1], resource exploration [2], military missions [3] and
other ﬁelds due to their simple structure, low manufacturing
cost and high maneuverability. As a result, research on the
stability and trajectory tracking of AAVs has become a focal
point in recent decades [4]. Quadrotors rely on attitude control
to complete ﬂight tasks including trajectory tracking and
stabilization [5]. Due to its nonlinearity, strong coupling, and
underactuated nature [6], the attitude control of drones faces
multiple challenges.
About quadrotor attitude control, a substantial body of
research has been accumulated. Multiple control design meth-
ods were developed, such as PID control [7] and linear
quadratic regulator control [8]. Nevertheless, the above-
mentioned traditional linear controllers can hardly meet the
requirements of high-precision control. To overcome the lim-
itations of linear methods, various nonlinear control strategies
were proposed, including adaptive control [9], [10], backstep-
ping control [11], [12], sliding mode control (SMC) [13],
[14], [15] and model predictive control [16], [17], as well
as safety control techniques [18], [19]. The aforementioned
methods demonstrate that SMC exhibits superior performance
characteristics and robustness for a speciﬁc class of nonlinear
tracking problems [20]. But the sign function inherent in the
SMC control process inevitably induces system chattering.
In [21], the chattering phenomenon in control inputs caused
by conventional SMC was eﬀectively eliminated through the
integration of backstepping with SMC. A hybrid control strat-
egy combining BSMC was proposed in [22] and the results
demonstrated that compared with conventional backstepping
methods, this BSMC strategy exhibited signiﬁcantly enhanced
robustness against parameter uncertainties of varying magni-
tudes. Nevertheless, system uncertainties can still signiﬁcantly
degrade the tracking accuracy of the aforementioned control
methods.
To enhance the system’s robustness and disturbance rejec-
tion performance, a novel control method was proposed
integrating a nonlinear extended state observer (NESO) with
a nonlinear feedback controller in [23]. In [24], LESO instead
of a NESO was employed for quadrotor attitude control,
while reducing the number of tuning parameters required for
the extended state observer (ESO). In [25], a novel SMC
based on an ESO was designed, which eﬀectively suppresses
1558-3783 © 2026 IEEE. All rights reserved, including rights for text and data mining, and training of artiﬁcial intelligence and
similar technologies. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 12:54:41 UTC from IEEE Xplore.  Restrictions apply.

## Page 2

LIN et al.: ATTITUDE CONTROL METHOD FOR AAV BASED ON TIME-VARYING SWITCHING THRESHOLD ETM
5745
chattering while maintaining robustness through a dual-path
strategy combining an adaptive switching term and disturbance
compensation. To address the issue that the conventional ESO
cannot accurately estimate system states and disturbances
within ﬁnite time due to its linear characteristics, a ﬁnite-
time ESO based on the homogeneity theorem was proposed
[26], then, a nonsingular terminal SMC strategy was designed
accordingly, which ensures precise estimation of states and
disturbances and guarantees global ﬁnite-time stability of the
closed-loop system. In summary, the aforementioned control
strategies are fundamentally designed to enhance both ﬂight
stability and disturbance rejection capabilities of quadrotor
AAV systems, but most are in a continuous-time framework.
So far, most quadrotor controllers operate based on
continuous-time signal mechanisms, which require high sig-
nal transmission frequencies and lead to signiﬁcant resource
wastage. Yet, limited battery life remains a primary constraint
for AAV [27]. It is imperative to design resource-eﬃcient
controllers that can conserve both communication and com-
putational resources while maintaining high control precision,
thereby reducing energy consumption during mission execu-
tion. Recently, ETM have been introduced to address this
challenge [28] [29], [30]. In [31], for nonlinear systems
with output constraints, three distinct ETM were designed: a
ﬁxed-threshold (FT) strategy, a relative-threshold (RT) strategy
and a switching-threshold (ST) strategy. It is veriﬁed that
the proposed RT strategy has better control performance
and can save more communication resources than a FT one
[32] and has been used in AAVs [33]. Moreover, compared
with the traditional RT strategy, the presented ST strategy
demonstrates superior capability in balancing system perfor-
mance and communication constraints [34], [35], [36]. But,
as well-known to all, FT mechanism is simple in structure
but lacks ﬂexibility, making it diﬃcult to dynamically adjust
the triggering frequency according to diﬀerent response phases
of the system; RT mechanism usually presents a varying
threshold for the triggering event such that can improve the
ﬂexibility and obtain better system performance, however
sudden jump of control input may occurs when the magnitude
of the control signal is excessively large, which makes it face
numerous concerns in practical applications; traditional ST
mechanism has the advantages of the ﬁrst two design strate-
gies in balancing the system performance and the network
constraints through integrating them together, yet, research on
ST mechanism is still in its early stages, and it is worth further
studying how to enhance its ﬂexibility and to improve system
performance.
Motivated by these preceding results, an emulation method
which includes there parts: a LESO, a BSMC and a TVST,
is proposed. The LESO is incorporated into the BSMC
framework to signiﬁcantly enhances the quadrotor’s distur-
bance rejection capability while maintaining tracking accuracy.
An TVST strategy is developed in an innovative way with
two distinct event-triggering modes which employ dedicated
controllers respectively, while incorporating exponential-decay
thresholds for progressive temporal adaptation. Compared with
traditional ST in [34], [37], RT in [38] and FT in [39]
approaches, the proposed TVST strategy shows its much more
ﬂexibility and provides a balance between the tracking error
Fig. 1. Schematic diagram of the quadrotor.
and inter-execution intervals which means Zeno behaviors [40]
can be excluded.
II. DYNAMIC MODEL
An inertial frame (Xe, Ye, Ze) and a body-ﬁxed frame
(Xb, Yb, Zb) with the origin at the center of mass of the
quadrotors as shown in Fig. 1, and the vehicle’s motion is
controlled by regulating the rotational speeds of its four rotors.
The quadrotor AAV possesses six degrees of freedom in spatial
motion, comprising three translational degrees of freedom and
three rotational degrees of freedom. Since the system has six
degrees of freedom but four independent motors for control
actuation are utilized, then it is a canonical underactuated
system where the control input dimension is strictly less than
the system’s full conﬁguration space dimension [41].
The dynamic model of the quadrotor are based on the
Newton-Euler derivation [42]. Let Ω= [φ, θ, ψ]T, ωb =
[p, q, r]T, where φ, θ and ψ denote the angle of roll,
pitch and yaw with respect to the inertia frame, p,q and r
represent angular velocity relative to the body-ﬁxed frame
[43], as established in [44], the conversion between inertial
frame velocity and body-ﬁxed velocity is
2
4
˙φ
˙θ
˙ψ
3
5 =
2
4
1
sin φ tan θ
cos φ tan θ
0
cos φ
−sin φ
0
sin φ sec θ
cos φ sec θ
3
5
2
4
p
q
r
3
5 .
(1)
For the quadrotor AAV, the propellers are suﬃciently
lightweight, thus the moment of inertia caused by the pro-
pellers is neglected [45], then, the attitude dynamics model
can be written as
8
ˆˆˆˆˆˆˆˆ<
ˆˆˆˆˆˆˆˆ:
˙φ = p + (q sin φ + r cos φ) tan θ,
˙θ = q cos φ−r sin φ,
˙ψ = (q sin φ + r cos φ) sec θ,
˙p = a1qr + d1u1 + ∆1,
˙q = a2pr + d2u2 + ∆2,
˙r = a3pq + d3u3 + ∆3,
(2)
where a1 = Jy−Jz
Jx , a2 = Jz−Jx
Jy , a3 = Jx−Jy
Jz , d1 =
l
Jx , d2 =
l
Jy , d3 =
1
Jz , Jx, Jy and Jz are the moments of inertia of the quadrotor
around x, y, z respectively, l represents the distance between
rotor and quadrotor centers, ∆1, ∆2 and ∆3 represent external
disturbance acting on the rotational motion of the quadrotor.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 12:54:41 UTC from IEEE Xplore.  Restrictions apply.

## Page 3

5746
IEEE TRANSACTIONS ON AUTOMATION SCIENCE AND ENGINEERING, VOL. 23, 2026
To ensure ﬂight safety and facilitate controller design, the
pitch and roll angles are assumed to undergo small vari-
ations [46], [47], [48], so that (˙φ ˙θ ˙ψ) ≈(p q r). Let
[x1, x2, x3, x4, x5, x6]T = [φ, ˙φ, θ, ˙θ, ψ, ˙ψ]T, the equation (2) can
be rewritten as 8
ˆˆˆˆˆˆˆˆ<
ˆˆˆˆˆˆˆˆ:
˙x1 = x2,
˙x2 = x4x6a1 + d1u1 + ∆1,
˙x3 = x4,
˙x4 = x2x6a2 + d2u2 + ∆2,
˙x5 = x6,
˙x6 = x2x4a3 + d3u3 + ∆3.
(3)
In this section, a mathematical model of the quadrotor
under external disturbances is established. During practical
control of quadrotor, the angular velocity variations are small,
making the coupling terms of the control channels small
enough in most cases, which can be eﬀectively estimated and
compensated via ESO [23]. However, most existing quadrotor
attitude control methods rely on continuous-time controllers
[21], [22], [23], [24]. Therefore, the present work proposes an
enhanced ETM with TVST that improves resource utilization
while guaranteeing system stability.
III. ATTITUDE CONTROLLER DESIGN
AND STABILITY ANALYSIS
In this section, a LESO-BSMC based attitude controller,
which integrates sliding mode control with backstepping con-
trol techniques while employing a LESO to achieve estimation
of composite unknown disturbances, is proposed ﬁrst. Then,
a novel TVST event-triggered strategy is presented to reduces
communication resource. Finally, stability analysis of the
closed-loop system is conducted and the exclusion of Zeno
behavior is conﬁrmed. The whole control scheme is illustrated
in Fig. 2.
A. LESO
Coupling eﬀects between attitude loops, model uncertainties
and external disturbances can be estimated and compensated
via an ESO. Here, a LESO is obtained by simplifying NESO
design. Although the LESO’s linear feedback is theoretically
weaker, its simplicity and practicality make this trade-oﬀ
worthwhile [49]. Hence, similar as that in [50], the LESO
can be designed as
8
ˆ<
ˆ:
˙ˆξ1 = ˆξ2 + β1(x1 −ˆξ1),
˙ˆξ2 = ˆξ3 + d1u1 + β2(x1 −ˆξ1),
˙ˆξ3 = β3(x1 −ˆξ1),
(4)
8
ˆ<
ˆ:
˙ˆξ4 = ˆξ5 + β4(x3 −ˆξ4),
˙ˆξ5 = ˆξ6 + d2u2 + β5(x3 −ˆξ4),
˙ˆξ6 = β6(x3 −ˆξ4),
(5)
8
ˆ<
ˆ:
˙ˆξ7 = ˆξ8 + β7(x5 −ˆξ7),
˙ˆξ8 = ˆξ9 + d3u3 + β8(x5 −ˆξ7),
˙ˆξ9 = β9(x5 −ˆξ7),
(6)
where ˆξi, i = 1, . . . , 9 are the states of LESO, βi, i = 1, . . . , 9
are the gains of LESO which are proper real constants.
Fig. 2. Quadrotor AAV control scheme.
When the parameters βi, i = 1, . . . , 9 are set and the system
is stabilized, then ˆξ3 ≈(x4x6a1 + ∆1), ˆξ6 ≈(x2x6a2 + ∆2)
and ˆξ9 ≈(x2x4a3 + ∆3) [51]. By virtue of the above LESOs,
the total disturbance of the system can be estimated and
compensated.
B. LESO-BSMC Controller Design
The control objective of attitude system is to ensure that
(φ, θ, ψ) tracks the desired attitude (φd, θd, ψd) by designing
control law U = (u1, u2, u3)T. Here, BSMC is purposed to
achieve precise AAV attitude motion control with enhanced
robustness against parameter uncertainties.
Let the desired roll angle φd = xd1, the tracking error is
e1 = xd1 −x1, ˙e1 = ˙xd1 −˙x1 = ˙xd1 −x2. Choose
V(e1) = 1
2e2
1,
(7)
then
˙V(e1) = e1˙e1 = e1(˙xd1 −x2).
(8)
To ensure negative semi-deﬁnite of ˙V(e1), the control ˆx2 =
˙xd1 + k1e1 is introduced, where k1 > 0. Then, the tracking
error
e2 = x2 −ˆx2 = x2 −k1e1 −˙xd1 = −k1e1 −˙e1.
(9)
Construct the sliding surface
S 1 = e2 = x2 −ˆx2 = x2 −k1e1 −˙xd1.
(10)
Combining equation (3) and equation (4) yields
˙x2 = x4x6a1 + d1u1 + ∆1 = ˆξ3 + d1u1.
(11)
Select an exponential convergence law [52], then
˙S 1 = −c1sign(S 1) −c2S 1 = ˙x2 −k1˙e1 −¨xd1
= ˆξ3 + d1u1 −¨xd1 −k1(−k1e1 −e2),
(12)
where c1, c2 are positive constant.
Thus, the roll angle controller can be obtained
u1 = 1
d1
k1˙e1 −ˆξ3 + ¨xd1 −c1S 1 −c2 sign(S 1)

= 1
d1
−k2
1e1 −ˆξ3 + ¨xd1 −(c1 + k1)S 1 −c2 sign(S 1)

.
(13)
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 12:54:41 UTC from IEEE Xplore.  Restrictions apply.

## Page 4

LIN et al.: ATTITUDE CONTROL METHOD FOR AAV BASED ON TIME-VARYING SWITCHING THRESHOLD ETM
5747
Similarly, the sliding surfaces and controllers for the pitch
angle and yaw angle can be obtained as follows
8
<
:
S 2 = e4 = x4 −k2e3 −˙xd2,
u2 = 1
d2
−k2
2e3 −ˆξ6 + ¨xd2 −(c3 + k2)S 2 −c4 sign(S 2)

,
8
<
:
S 3 = e6 = x6 −k3e5 −˙xd3,
u3 = 1
d3
−k2
3e5 −ˆξ9 + ¨xd3 −(c5 + k3)S 3 −c6 sign(S 3)

,
where c1, c2, c3, c4, c5, c6, k1, k2, k3 are the positive constant.
xd2, xd3 are the desired values for the pitch and yaw angles,
respectively, ˆξ6 and ˆξ9 are the compounded disturbance esti-
mates for the pitch and yaw angles, and e3 and e5 are the
tracking errors for the pitch and yaw angles.
C. TVST Event-Triggered Mechanism
Due to quadrotors’ limited computational power and
onboard energy, a new TVST event-triggered strategy is
proposed to alleviate the burden of processors for handling
increasing computational demands as missions grow more
complex. The TVST ETM is as follows
ui(t) = ωi(tk),
∀t ∈[ti,k, ti,k+1]
(14)
ωi(t) =
8
ˆˆˆˆˆˆ<
ˆˆˆˆˆˆ:
−(1 + δ1)
2
πui arctan
uiS i
ϵi

+2
π ¯mi arctan
 ¯miS i
ϵi

,
|ui| < Di,
ui −2
π ¯mi arctan
 ¯miS i
ϵi

,
|ui| ≥Di,
(15)
ti,k+1 =
8
ˆˆˆ<
ˆˆˆ:
inf
˚
t ∈R | |ωi(t) −ui(t)| ≥δi|ui| + mie−t
+γi} ,
|ui| < Di,
inf
˚
t ∈R | |ωi(t) −ui(t)| ≥αie−t + γi
	
,
|ui| ≥Di,
(16)
where Di is a parameter to be designed, 0 < ϵi < 1, γi >
0, mi > 0, αi > 0, ¯mi > mi/(1 −δi), ¯mi > αi are positive
numbers, ti,k+1 is the moment of controller update, and i =
1, 2, 3 corresponds to the three attitude angles respectively.
Remark 1: It should be pointed out that the TVST ETM
proposed here diﬀers from those in [34] and [39] by intro-
ducing a time-varying decreasing function to the switching
threshold mechanism, enabling continuous threshold ajustation
corresponding to system dynamics. It employs dual threshold
expressions based on |ui| relative to Di achieving both fast
tracking for large signals with decaying bounded measurement
errors and high precision for small input signals−a capability
challenging for most FT, RT and traditional ST mechanisms.
Moreover, compared with ST [34], RT [38] and FT [39], both
simulation and experimental results, which is presented as
follows in Section IV, conﬁrm that the proposed ETM achieves
a better balance between system performance and resource
consumption.
Remark 2: The proposed TVST ETM provides more ﬂex-
ibility in balancing the system performance and the network
constraints lies in the following facts: when the magnitude of
input signals is relatively big, the threshold strategy is set to
Fig. 3. Phase diagram.
be a time-varying decreasing one such that the measurement
errors gradually decrease but keep bounded to ensure certain
system performances; otherwise, when the control signal sat-
isﬁes that |ui| < Di, the time-varying relative-like threshold
strategy is adopted so that precise control can be obtained
when needed. Thus, it provides a balance between the tracking
error and inter-execution intervals, compared to the existing
FT, RT and traditional ST ones.
D. Stability Analysis of the Closed-Loop System
Main results of this paper are presented as below. The main
stability results of the closed-loop system are summarized in
the following Theorem. To enhance readability and highlight
the main conclusions of the paper, the detailed proof is
provided in Appendix.
Theorem 1: For quadrotor AAV attitude system (3), imple-
mentation of the event-triggered controllers (14), (15), (16)
combined with the LESO-BSMC attitude controller (13)
ensures that it is ultimately bounded. Moreover, Zeno behav-
iors are excluded for the ETM (14), (15), (16), that is, there
exists t∗
1 > 0 such that the set of execution time intervals
{t1,k+1 −t1,k}, ∀k ∈N+ has t∗
1 as its lower bound.
Proof: See it in Appendix A, please.
Remark 3: Based on the Lyapunov analysis, the system is
proven to be uniformly ultimately bounded. The size of the
ultimate bounded region including the equilibrium is closely
related to the parameter C, i.e., the set parameter ϵ1: the
smaller ϵ1 is, the smaller C becomes, and a smaller C yields
the fact that the system converges to a smaller set near the
equilibrium. It is also be illustrated by simulations as below,
Fig. 3 in next section.
IV. SIMULATION AND EXPERIMENTAL VALIDATIONS
Now, the eﬃcacy of the proposed approach is to be validated
by simulations and experiments.
A. Numerical Simulations
Numerical simulations for quadrotor AAV attitude angles
were conducted to validate the eﬀectiveness of the proposed
control method.
The parameters in (2) are as follows: Jx = Jy = 3.513 ×
103 kg·m2, Jz = 6.521×10−3 kg·m2, l = 0.3m. The parameters
of controllers in (13) are k1 = k2 = k3 = 5, c1 = c3 = c5 = 12,
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 12:54:41 UTC from IEEE Xplore.  Restrictions apply.

## Page 5

5748
IEEE TRANSACTIONS ON AUTOMATION SCIENCE AND ENGINEERING, VOL. 23, 2026
Fig. 4. Sine response tracking error of attitude angles.
TABLE I
ITAE AND RMS VALUES
c2 = c4 = c6 = 0.3, β1 = β4 = β7 = 150, β2 = β5 = β8 =
8000, β3 = β6 = β9 = 9000. In the TVST ETM (15) (16), the
parameters ϵ1 = ϵ2 = 0.00282, ϵ3 = 0.002, D1 = D2 = D3 =
0.05, δ1 = 0.01, δ2 = 0.008, δ3 = 0.0289, γ1 = γ2 = γ3 =
0.0001, m1 = m2 = 0.125, m3 = 0.132, α1 = α2 = α3 = 0.135,
¯m1 = ¯m2 = ¯m3 = 6π.
In Fig. 3, the impact of parameter C, i.e., ϵ1 on the the
adjustable ultimately bounded region including the equilibrium
are presented, which intuitively demonstrated what Remark 3
has stated.
Comparison of the sinusoidal tracking error curves among
ST [34], RT [38], FT [39], TVST methods and the time-
triggered method (NO ETC) are presented in Fig. 4, the ITAE
and RMS values for sinusoidal tracking are provided in Table I
and controller update frequency are presented in Fig. 5. From
Figs. 4 and 5 and Table I, it is not diﬃcult to see that the
proposed TVST control strategy in this paper can achieve the
balance between system performance such as superior tracking
precision and appropriate ITAE and RMS performance metrics
Fig. 5. Controller update situations of attitude angles.
Fig. 6. Triggering intervals of attitude angle controllers.
and the inter-execution intervals of triggering events than the
above-mentioned approaches.
The controller updateand triggering intervals are respec-
tively presented in Fig. 5 and 6. In Fig. 5, FT, RT and ST
event-triggered control update the controller 536, 456 and 460
times during the same period, respectively. The TVST event-
triggered control further reduces the updates to 344 times.
Compared with the TTC method, which has a sampling time
of 0.002 s and requires 5000 controller updates in 10 seconds,
all three event-triggered methods achieve over 90% reduction
in controller updates relative to TTC. The proposed method
achieves 35.8%, 24.6% and 25.2% reductions in controller
updates relative to ST, RT and FT methods respectively. Fig. 6
shows the triggering intervals of the attitude controllers with
t∗denotes the minimum event trigger intervals corresponding
to two selected time periods: 0-2s and 2-10s. Speciﬁcally, the
minimum interval of 0.002s appears in the 0-2s period. This is
attributed to the fact that during the initial tracking stage, the
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 12:54:41 UTC from IEEE Xplore.  Restrictions apply.

## Page 6

LIN et al.: ATTITUDE CONTROL METHOD FOR AAV BASED ON TIME-VARYING SWITCHING THRESHOLD ETM
5749
Fig. 7. 3D trajectory tracking.
Fig. 8. The overall experiment setup.
controller requires more frequent updates to minimize errors.
Once the system enters a stable state, such frequent updates
are no longer necessary. Taking TVST as an example, in the
stable period from 2-8s, the roll angle’s minimum event trigger
interval is 0.012s. The proposed controller avoids continuous
updates and Zeno behaviors, while compared with FT and
ST triggering, it signiﬁcantly increases the update frequency
and reduces resource usage. The 3D trajectory tracking perfor-
mance comparison among ST, RT, FT and TVST proposed in
this paper is presented in Fig. 7, which further demonstrates
the superiority of the proposed method.
B. Experimental Results
In addition to numerical simulation veriﬁcation, this study
conducted physical validation experiments of the proposed
control algorithm using a high-precision attitude control test
platform. The experimental platform consists of the follow-
ing components as shown in Fig. 8: aircraft fuselage, ﬂight
control equipment, a spherical-joint-based ﬁxed base, wireless
data transmission system, and host computer. The quadrotor
Fig. 9. Experimental comparison under step response.
Fig. 10. Experimental comparison under sine response.
aircraft is connected to the top of a vertical column via a
spherical joint, which enables 360◦attitude movement through
its omnidirectional characteristics. To reduce the load on the
spherical joint, a limiting device was designed to constrain the
aircraft’s horizontal tilt angle within 40◦.
The step response experiments compare the performance
of three control methods: ST [34], RT [38], FT [39], and
TVST proposed in this paper, as illustrated in Fig. 9. The
experimental results demonstrate that for all three attitude
angles, the TVST control method exhibits signiﬁcantly supe-
rior dynamic response speed compared to all FT, RT and
traditional ST methods. During steady-state operation, the
TVST method achieves minimal tracking error, demonstrating
optimal tracking precision.
To quantitatively evaluate the performance of the error
response, the ITAE (Integral of Time-weighted Absolute Error)
and RMS (Root Mean Square) values were calculated. Both
metrics serve as critical indicators for assessing error response
characteristics, with their speciﬁc numerical values presented
in Table II. This experiment addresses the delay compensa-
tion problem in physical sensors, where hardware sampling
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 12:54:41 UTC from IEEE Xplore.  Restrictions apply.

## Page 7

5750
IEEE TRANSACTIONS ON AUTOMATION SCIENCE AND ENGINEERING, VOL. 23, 2026
TABLE II
ITAE AND RMS VALUES
TABLE III
AVERAGE PWM DUTY CYCLE COMPARISON
frequency and signal transmission latency artiﬁcially amplify
the time weighting factor in conventional ITAE calculations,
thereby obscuring genuine dynamic performance diﬀerences.
To eliminate the impact of time span on evaluation metrics,
normalized ITAE computation is deﬁned as: ITAEnorm
=
1
T 2
R T
0 t|e(t)|dt. The TVST method demonstrates consistently
superior performance by maintaining the lowest tracking
error level throughout the sinusoidal excitation response, as
evidenced by the comparative error analysis presented in
Fig. 10. The experimental results demonstrate that the pro-
posed method achieves faster system convergence and more
stable long-term control performance.
Table III presents a comparative analysis of PWM duty
cycles for three attitude control modes. For clarity, only one
motor from each actuation pair is shown for each attitude
angle, including (a) Roll: motors 1 & 4 and 2 & 3 paired
for roll motion, (b) Pitch: motors 1 & 2 and 3 & 4 paired for
pitch motion, (c) Yaw: motors 1 & 3 and 2 & 4 cooperate for
yaw motion. For roll and pitch angles, the proposed LESO-
BSMC+TVST method achieves the lowest duty cycles, while
maintaining mid-range values for yaw control. The results
demonstrate that the TVST method optimally balances energy
eﬃciency (reduced PWM duty cycles) with ﬂight stability
(consistent tracking accuracy) across all attitude control axes.
V. CONCLUSION
To address the attitude stabilization and tracking control
problem for quadrotor AAVs under communication resource
constraints and external uncertainties, a TVST-based control
strategy integrating LESO and BSMC, which can solve the
dilemma to some extent, achieving a balance of better system
performance and relatively few resource consumption. Further
research on the TVST event-triggered control strategy about
the smoothness of control input and more appropriate trigger-
ing and switching rules are in our future work schedule.
APPENDIX
A. Proof of Theorem 1
Proof: First, stability analysis of the resultant closed-loop
system is presented and taking the control of roll angle into
account. It can be divided into two cases.
Case 1: |u1| < D1. The event-triggered condition guarantees
|ω1(t) −u1(t)| ≤δ1|u1| + m1e−t + γ1,
∀t ∈[t1,k, t1,k+1].
Since λ1(t) and λ2(t) are continuous time-varying functions
and satisfy |λ1(t)| ≤1, |λ2(t)| ≤1, then the control input
ω1(t) = (1 + λ1(t)δ1)u1(t) + λ2(t)m1e−t + λ2(t)γ1. Thus,
u1(t) =
ω1(t)
1 + λ1(t)δ1
−λ2(t)m1e−t + λ2(t)γ1
1 + λ1(t)δ1
.
Let
V2 = V(e1, S 1) = V(e1) + 1
2S 2
1,
(17)
then
˙V2 = −e1e2 −k1e2
1
+ S 1
h
ˆξ3 + d1u1 −¨xd1 −k1(−k1e1 −e2)
i
= −e1S 1 −k1e2
1
+ S 1

d1

ω1(t)
1 + λ1(t)δ1
−λ2(t)m1e−t + λ2(t)γ1
1 + λ1(t)δ1

+ ˆξ3 −¨xd1 −k1(−k1e1 −e2)

.
(18)
For ϵ1 > 0, −u1S 1 arctan

u1S 1
ϵ1

≤0. Hence,
ω1(t)S 1
1 + λ1(t)δ1
= −(1 + δ1)
1 + λ1(t)δ1
×
2
πu1S 1 arctan
u1S 1
ϵ1

+ 2
π ¯m1S 1 arctan
 ¯m1S 1
ϵ1
 
≤−(1 + δ1)
1 + δ1
×
2
πu1S 1 arctan
u1S 1
ϵ1

+ 2
π ¯m1S 1 arctan
 ¯m1S 1
ϵ1
 
= −2
πu1S 1 arctan
u1S 1
ϵ1

−2
π ¯m1S 1 arctan
 ¯m1S 1
ϵ1

,
ˇˇˇˇ−λ2(t)S 1m1e−t
1 + λ1(t)δ1
ˇˇˇˇ ≤
ˇˇˇˇ−λ2(t)S 1m1
1 + λ1(t)δ1
ˇˇˇˇ ≤
ˇˇˇˇ
S 1m1
1 −δ1
ˇˇˇˇ ,
ˇˇˇˇ−λ2(t)γ1S 1
1 + λ1(t)δ1
ˇˇˇˇ ≤
ˇˇˇˇ
γ1S 1
1 −δ1
ˇˇˇˇ .
(19)
Moreover, the arctangent function has the following properties
(see it in [53], equation (32)), when ε > 0,
0 ≤|β| −2
πβ arctan
β
ε

≤2
πε.
(20)
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 12:54:41 UTC from IEEE Xplore.  Restrictions apply.

## Page 8

LIN et al.: ATTITUDE CONTROL METHOD FOR AAV BASED ON TIME-VARYING SWITCHING THRESHOLD ETM
5751
For equation (19), constructing a function in the form of
equation (20). Then, equation (18) can be rewritten as
˙V2 ≤−e1S 1 −k1e2
1 −c1S 2
1 −c2S 1sign(S 1)
+ d1
4
πϵ1 −|S 1 ¯m1| +
ˇˇˇˇ
S 1m1
1 −δ1
ˇˇˇˇ +
ˇˇˇˇ
γ1S 1
1 −δ1
ˇˇˇˇ

≤−e1S 1 −k1e2
1 −c1S 2
1 −c2S 1sign(S 1)
+ d1
4
πϵ1 −|S 1 ¯m1| + |S 1 ¯m1| +
ˇˇˇˇ
γ1S 1
1 −δ1
ˇˇˇˇ

≤−e1S 1 −k1e2
1 −c1S 2
1 −

c2 −
γ1
1 −δ1

|S 1|
+ 4
πd1ϵ1,
(21)
where c2 −
γ1
1−δ1 > 0.
Let Q =
k1
1
2
1
2 c1

and e = (e1 S 1)T. Then,
eTQe = (e1 S 1)
k1
1
2
1
2 c1
 e1
S 1

= e1S 1 + k1e2
1 + c1S 2
1.
(22)
Thus, equation (21) can be rewritten as
˙V2 ≤−eTQe −

c2 −
γ1
1 −δ1

|S 1| + 4
πd1ϵ1 ≤−eTQe + 4
πd1ϵ1.
If k1c1 > 1
4 is satisﬁed, then Q is positive deﬁnite. Therefore,
eTQe ≥λmin(Q)eTe = 2λmin(Q)V2,
where λmin(Q) represents the minimum eigenvalue of Q.
Therefore,
˙V2 ≤−eTQe + 4
π d1ϵ1
= −2λmin (Q) V2 + C,
where C = 4
π d1ϵ1.
Case 2: |u1| ≥D1. The event-triggered condition guarantees
|ω1(t) −u1(t)| ≤α1e−t + γ1,
∀t ∈[t1,k, t1,k+1].
Let λ3(t) be continuous and satisﬁes |λ3(t)| ≤1, then the
control input u1(t) = ω1(t) −λ3(t)α1e−t −λ3(t)γ1. Substituting
it and (15) into equation (18), then
˙V2 = −e1e2 −k1e2
1
+ S 1
h
ˆξ3 + d1u1 −¨xd1 −k1(−k1e1 −e2)
i
= −e1S 1 −k1e2
1
+ S 1

d1
ω1(t) −λ3(t)α1e−t −λ3(t)γ1

+ ˆξ3 −¨xd1 −k1(−k1e1 −e2)

= −e1S 1 −k1e2
1 + S 1
h
−d1
2
π ¯m1 arctan
 ¯m1S 1
ϵ1

−d1λ3(t)α1e−t −d1λ3(t)γ1 −c1S 1 −c2sign(S 1)
i
≤−e1S 1 −k1e2
1 −c1S 2
1 −c2S 1sign(S 1)
−d1
2
π ¯m1S 1 arctan
 ¯m1S 1
ϵ1

+ d1|α1S 1| + d1|γ1S 1|
≤−e1S 1 −k1e2
1 −c1S 2
1 −(c2 −d1γ1)|S 1| + d1|α1S 1|
−d1
2
π ¯m1S 1 arctan
 ¯m1S 1
ϵ1

≤−e1S 1 −k1e2
1 −c1S 2
1 −(c2 −d1γ1)|S 1| + d1| ¯m1S 1|
−d1
2
π ¯m1S 1 arctan
 ¯m1S 1
ϵ1

,
(23)
where c2 −d1γ1 > 0.
Substituting equation (20) into the above equation, then
˙V2 ≤−e1S 1 −k1e2
1 −c1S 2
1 + 2
πd1ϵ1.
(24)
Substituting equation (22) into equation (24), then
˙V2 ≤−eTQe + 2
πd1ϵ1 = −2λmin (Q) V2 + C
2 .
From the above analysis, it can be concluded that, for the
roll angle control process, all variables of the system remain
bounded. Similarly, the proofs for the boundedness of variables
in the pitch angle system, yaw angle system follow analogous
procedures.
Now, exclusion of Zeno behaviours of the proposed TVST
event-triggered mechanism is presented as below.
Let e(t) = ω1(t) −u1(t). Then
d|e(t)|
dt
= d
dt (e · e)
1
2 = sign(e) · ˙e ≤| ˙ω1(t)|.
For |u1| < D1,
˙ω1(t) = −(1 + δ1)2
π

˙u1 arctan
u1S 1
ϵ1

+
u1
1 + (u1S 1/ϵ1)2
ϵ1
˙u1S 1 + u1 ˙S 1
 
−(1 + δ1)2
π
¯m2
1 ˙S 1
ϵ1
1
1 + ( ¯m1S 1/ϵ1)2 .
Since all variables in ˙ω1(t) are globally bounded, there must
exist a constant η > 0 such that | ˙ω1(t)| < η. For ∀k ∈N+,
when t = t1,k, e(t1,k) = 0. At the event triggering instant,
when |ω1(t) −u1(t)| = δ1|u1| + m1e−t + γ1, it follows that
limt→t1,k+1 e(t) = δ1|u1| + m1e−t1,k+1 + γ1. The integral of |˙e(t)|
over [t1,k, t1,k+1) satisﬁes
Z t1,k+1
t1,k
ˇˇ˙e(t)
ˇˇ dt ≤
ˇˇ ˙ω1(t)
ˇˇ(t1,k+1 −t1,k)
≤η(t1,k+1 −t1,k).
Because
Z t1,k+1
t1,k
|˙e(t)|dt =
lim
t→t1,k+1
ˇˇe(t) −e(t1,k)
ˇˇ
= δ1|u1| + m1e−t1,k+1 + γ1,
then
t1,k+1 −t1,k ≥δ1|u1| + m1e−t1,k+1 + γ1
η
≥γ1
η ,
∀k ∈N+.
For |u1| ≥D1, the derivative of ω1(t) is
˙ω1(t) = ˙u1 −2 ¯m2
1 ˙S 1
πϵ1
·
1
1 +

¯m1.S 1
ϵ1
2 .
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 12:54:41 UTC from IEEE Xplore.  Restrictions apply.

## Page 9

5752
IEEE TRANSACTIONS ON AUTOMATION SCIENCE AND ENGINEERING, VOL. 23, 2026
Since all variables in ˙ω1(t) are globally bounded, there must
exist a constant η > 0 such that | ˙ω1(t)| < η. For ∀k ∈N+,
when t = t1,k, e(t1,k) = 0. At the event triggering instant,
when |ω1(t) −u1(t)| = α1e−t + γ1, it follows that limt→t1,k e(t) =
α1e−t1,k+1 + γ1. The integral of |˙e(t)| over [t1,k, t1,k+1) satisﬁes
Z t1,k+1
t1,k
ˇˇ˙e(t)
ˇˇ dt ≤
ˇˇ ˙ω1(t)
ˇˇ(t1,k+1 −t1,k).
≤η(t1,k+1 −t1,k).
Because
Z t1,k+1
t1,k
|˙e(t)|dt =
lim
t→t1,k+1
ˇˇe(t) −e(t1,k)
ˇˇ = α1e−t1,k+1 + γ1,
then
t1,k+1 −t1,k ≥α1e−t1,k+1 + γ1
η
≥γ1
η ,
∀k ∈N+.
Thus, t∗
1 = γ1
η > 0 is the lower bound for the set of execution
time intervals {t1,k+1 −t1,k}, ∀k ∈N+. Similar to the above
proof process for the roll angle, Zeno behaviours of the event-
triggered controllers for the pitch angle and yaw angle can be
also excluded. Therefore, exclusion of Zeno behavior of the
proposed event-triggered mechanism is proved.
REFERENCES
[1]
L. F. Luque-Vega, B. Castillo-Toledo, A. Loukianov, and L. E. Gonzalez-
Jimenez, “Power line inspection via an unmanned aerial system based
on the quadrotor helicopter,” in Proc. MELECON - 17th IEEE Medit.
Electrotechnical Conf., Beirut, Lebanon, Apr. 2014, pp. 393–397.
[2]
X. Zou, Z. Liu, W. Zhao, and C. Zhang, “Optimal hovering control of a
tail-sitter via model-free fast terminal slide mode controller and cuckoo
search algorithm,” in Proc. Int. Conf. Unmanned Aircr. Syst. (ICUAS),
Jun. 2021, pp. 978–984.
[3]
M. A. Ma’sum et al., “Simulation of intelligent unmanned aerial vehicle
(UAV) for military surveillance,” in Proc. Int. Conf. Adv. Comput. Sci.
Inf. Syst. (ICACSIS), Sanur Bali, Indonesia, Sep. 2013, pp. 161–166.
[4]
A. Noordin, M. A. M. Basri, Z. Mohamed, and I. M. Lazim, “Adaptive
PID controller using sliding mode control approaches for quadrotor UAV
attitude and position stabilization,” Arabian J. for Sci. Eng., vol. 46,
no. 2, pp. 963–981, Jul. 2020.
[5]
D. Mihailescu-Stoica, R. Acuna, and J. Adamy, “High performance
adaptive attitude control of a quadrotor,” in Proc. 18th Eur. Control
Conf. (ECC), Jun. 2019, pp. 3462–3469.
[6]
M. Jafarinasab, S. Sirouspour, and E. Dyer, “Model-based motion control
of a robotic manipulator with a ﬂying multirotor base,” IEEE/ASME
Trans. Mechatronics, vol. 24, no. 5, pp. 2328–2340, Oct. 2019.
[7]
R. Mahony, V. Kumar, and P. Corke, “Multirotor aerial vehicles: Mod-
eling, estimation, and control of quadrotor,” IEEE Robot. Autom. Mag.,
vol. 19, no. 3, pp. 20–32, Sep. 2012.
[8]
H. Liu, D. Derawi, J. Kim, and Y. Zhong, “Robust optimal attitude
control of hexarotor robotic vehicles,” Nonlinear Dyn., vol. 74, no. 4,
pp. 1155–1168, Dec. 2013.
[9]
W. He, Z. Yan, C. Sun, and Y. Chen, “Adaptive neural network control
of a ﬂapping wing micro aerial vehicle with disturbance observer,” IEEE
Trans. Cybern., vol. 47, no. 10, pp. 3452–3465, Oct. 2017.
[10] D. Yao, Y. Wu, H. Ren, H. Li, and Y. Shi, “Event-based adaptive sliding-
mode containment control for multiple networked mechanical systems
with parameter uncertainties,” IEEE Trans. Autom. Sci. Eng., vol. 22,
pp. 264–275, 2025.
[11] H. Su, Z. Zhang, and W. Zhang, “Adaptive backstepping optimal
tracking control of interconnected robotic manipulator system based
on reinforcement learning,” IEEE Trans. Autom. Sci. Eng., vol. 22,
pp. 19555–19567, 2025, doi: 10.1109/TASE.2025.3596555.
[12] J. Wang, K. A. Alattas, Y. Bouteraa, O. Moﬁd, and S. Mobayen,
“Adaptive ﬁnite-time backstepping control tracker for quadrotor UAV
with model uncertainty and external disturbance,” Aerosp. Sci. Technol.,
vol. 133, Feb. 2023, Art. no. 108088.
[13] T. Huo, X. Li, L. Zhu, and K. Wang, “Finite-time sliding mode
adaptive control for unknown nonlinear beam system with neural
network disturbance observer,” IEEE Trans. Autom. Sci. Eng., vol. 22,
pp. 18281–18296, 2025, doi: 10.1109/TASE.2025.3586229.
[14] Y. Bi, F. Wang, P. Ding, T. Wang, and J. Qiu, “Multivariable adaptive
super-twisting sliding mode resilient control for uncertain nonlinear
CPSs against actuator and sensor attacks,” IEEE Trans. Autom. Sci. Eng.,
vol. 22, pp. 9039–9048, 2025.
[15] M. M. Fatemi and A. Akbarimajd, “Adaptive sliding mode control for
quadrotor UAVs under disturbances using multi-layer perceptron,” IEEE
Access, vol. 13, pp. 45518–45526, 2025.
[16] M. Wei, L. Zheng, Y. Wu, H. Liu, and H. Cheng, “Safe learning-based
control for multiple UAVs under uncertain disturbances,” IEEE Trans.
Autom. Sci. Eng., vol. 21, no. 4, pp. 7349–7362, Oct. 2024.
[17] Z. Li, Y. Guo, G. Wang, J. Sun, and K. You, “Informative trajectory
planning for air-ground cooperative monitoring of spatiotemporal ﬁelds,”
IEEE Trans. Autom. Sci. Eng., vol. 22, pp. 2627–2638, 2025.
[18] Z. Yu and B. Jiang, Fault-Tolerant Control of Unmanned Flight Vehicles:
Safety in Low-Altitude Economic Environments. Cham, Switzerland:
Springer, 2025, doi: 10.1007/978-981-96-9388-7.
[19] Z. Yu, M. Li, Y. Zhang, and B. Jiang, “A review on safety control of
unmanned aerial vehicles with guaranteed performance requirements,”
Prog. Aerosp. Sci., vol. 158, Oct. 2025, Art. no. 101144.
[20] A. Nasiri, S. K. Nguang, and A. Swain, “Adaptive sliding-mode control
for a class of MIMO nonlinear systems with uncertainties,” J. Franklin
Inst., vol. 351, no. 4, pp. 2048–2061, Jan. 2014.
[21] Z. Jia, J. Yu, Y. Mei, Y. Chen, Y. Shen, and X. Ai, “Integral backstepping
sliding mode control for quadrotor helicopter under external uncertain
disturbances,” Aerosp. Sci. Technol., vol. 68, pp. 299–307, Sep. 2017.
[22] F. Chen, R. Jiang, K. Zhang, B. Jiang, and G. Tao, “Robust backstepping
sliding-mode control and observer-based fault estimation for a quadrotor
UAV,” IEEE Trans. Ind. Electron., vol. 63, no. 8, pp. 5044–5056, Aug.
2016.
[23] K.
Zhao,
J.
Zhang,
D.
Ma,
and
Y.
Xia,
“Composite
dis-
turbance
rejection
attitude
control
for
quadrotor
with
unknown
disturbance,” IEEE Trans. Ind. Electron., vol. 67, no. 8, pp. 6894–6903,
Aug. 2020.
[24] Y. Zhang, Z. Chen, X. Zhang, Q. Sun, and M. Sun, “A novel control
scheme for quadrotor UAV based upon active disturbance rejection
control,” Aerosp. Sci. Technol., vol. 79, pp. 601–609, Aug. 2018.
[25] P. Song, Q. Yang, D. Li, G. Wen, Z. Zhang, and J. Peng, “Disturbance-
compensation-based predictive sliding mode control for aero-engine
networked systems with multiple uncertainties,” IEEE Trans. Autom.
Sci. Eng., vol. 22, pp. 276–292, 2025.
[26] H. Lu, J. Li, S. Li, S. Wang, and Y. Xiao, “Finite-time extended
state observer enhanced nonsingular terminal sliding mode control for
buck converters in the presence of disturbances: Design, analysis and
experiments,” Nonlinear Dyn., vol. 112, no. 9, pp. 7113–7127, Mar.
2024.
[27] H. V. Abeywickrama, B. A. Jayawickrama, Y. He, and E. Dutkiewicz,
“Comprehensive energy consumption model for unmanned aerial vehi-
cles, based on empirical studies of battery performance,” IEEE Access,
vol. 6, pp. 58383–58394, 2018, doi: 10.1109/ACCESS.2018.2875040.
[28] X. Wu, N. Zhao, S. Ding, H. Wang, and X. Zhao, “Distributed event-
triggered output-feedback time-varying formation fault-tolerant control
for nonlinear multi-agent systems,” IEEE Trans. Autom. Sci. Eng.,
vol. 22, pp. 3810–3821, 2024, doi: 10.1109/TASE.2024.3400325.
[29] H. Ren, L. Cao, H. Ma, and H. Li, “Dynamic event-triggered-based
fuzzy adaptive pinning control for multiagent systems with output
saturation,” IEEE Trans. Fuzzy Syst., vol. 33, no. 4, pp. 1277–1286,
Apr. 2025.
[30] L. Cao, Y. Pan, H. Liang, and C. K. Ahn, “Event-based adaptive
neural network control for large-scale systems with nonconstant control
gains and unknown measurement sensitivity,” IEEE Trans. Syst., Man,
Cybern., Syst., vol. 54, no. 11, pp. 7027–7038, Nov. 2024.
[31] L. Xing, C. Wen, Z. Liu, H. Su, and J. Cai, “Event-triggered adaptive
control for a class of uncertain nonlinear systems,” IEEE Trans. Autom.
Control, vol. 62, no. 4, pp. 2071–2076, Apr. 2017.
[32] S. Yue, N. Xu, L. Zhang, and N. Zhao, “Observer-based event-triggered
adaptive fuzzy hierarchical sliding mode fault-tolerant control for uncer-
tain under-actuated nonlinear systems,” Int. J. Fuzzy Syst., vol. 27, no. 4,
pp. 1303–1320, Jun. 2025, doi: 10.1007/s40815-024-01834-9.
[33] C. Wang, N. Yang, W. Li, and M. Liang, “Event-triggered ﬁnite-time
fuzzy tracking control for a time-varying state constrained quadrotor
system based on disturbance observer,” Aerosp. Sci. Technol., vol. 151,
Aug. 2024, Art. no. 109329.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 12:54:41 UTC from IEEE Xplore.  Restrictions apply.

## Page 10

LIN et al.: ATTITUDE CONTROL METHOD FOR AAV BASED ON TIME-VARYING SWITCHING THRESHOLD ETM
5753
[34] Y. Wu, M. Chen, H. Li, and M. Chadli, “Event-triggered-based
adaptive NN cooperative control of six-rotor UAVs with ﬁnite-time
prescribed performance,” IEEE Trans. Autom. Sci. Eng., vol. 21, no. 2,
pp. 1867–1877, Apr. 2024.
[35] T. Jia, L. Cao, P. Zhang, and Y. Pan, “Event-based singularity-free ﬁxed-
time fuzzy control for active suspension systems with displacement
constraint,” Neural Comput. Appl., vol. 35, no. 27, pp. 19751–19763,
Sep. 2023.
[36] X. Yang, J. Cao, H. Liu, C. Huang, and G. Xue, “Composite adap-
tive fuzzy bipartite consensus of fractional-order multiagent systems
with a switched event-triggered mechanism,” ISA Trans., vol. 148,
pp. 224–236, Feb. 2024.
[37] X. Wang, Y. Zhou, B. Luo, Y. Li, and T. Huang, “Event-triggered
neuro-adaptive ﬁxed-time control for nonlinear switched and constrained
systems: An initial condition-independent method,” IEEE Trans. Circuits
Syst. I, Reg. Papers, vol. 71, no. 5, pp. 2229–2239, May 2024.
[38] G. Cui, H. Xu, J. Yu, and H.-K. Lam, “Event-triggered distributed ﬁxed-
time adaptive attitude control with prescribed performance for multiple
QUAVs,” IEEE Trans. Autom. Sci. Eng., vol. 21, no. 3, pp. 4471–4481,
Jul. 2024.
[39] X. Wang, C. Hua, and Y. Qiu, “Event-triggered model-free adaptive
control for nonlinear multiagent systems under jamming attacks,” IEEE
Trans. Neural Netw. Learn. Syst., vol. 35, no. 10, pp. 14458–14466, Oct.
2024.
[40] K. H. Johansson, M. Egerstedt, J. Lygeros, and S. Sastry, “On the
regularization of Zeno hybrid automata,” Syst. Control Lett., vol. 38,
no. 3, pp. 141–150, Oct. 1999.
[41] G. E. M. Abro and A. M. Abdallah, “Digital twins and control theory:
A critical review on revolutionizing quadrotor UAVs,” IEEE Access,
vol. 12, pp. 43291–43307, 2024, doi: 10.1109/ACCESS.2024.3376589.
[42] A. R. Ahangar, A. Ohadi, and M. A. Khosravi, “A novel ﬁreﬁghter
quadrotor UAV with tilting rotors: Modeling and control,” Aerosp.
Sci. Technol., vol. 151, Aug. 2024, Art. no. 109248, doi: 10.1016/
j.ast.2024.109248.
[43] F. Li, Z. Liu, and B. Jiang, “Adaptive ﬁnite-time fuzzy fractional sliding
mode control for uncertain QUAV with actuator faults and slung load,”
IEEE Trans. Aerosp. Electron. Syst., vol. 61, no. 2, pp. 3046–3058, Apr.
2025.
[44] X. Zhao, L. He, X. Liu, K. Han, and J. Li, “A novel reinforcement learn-
ing framework for optimizing ﬁxed-wing UAV ﬂight control strategies,”
Aerosp. Sci. Technol., vol. 166, Nov. 2025, Art. no. 110512.
[45] J. Xiong and G. Zhang, “Global fast dynamic terminal sliding mode
control for a quadrotor UAV,” ISA Trans., vol. 66, pp. 233–240, Jan.
2017.
[46] B. Wang, X. Yu, L. Mu, and Y. Zhang, “Disturbance observer-based
adaptive fault-tolerant control for a quadrotor helicopter subject to
parametric uncertainties and external disturbances,” Mech. Syst. Signal
Process., vol. 120, pp. 727–743, Apr. 2019.
[47] D. Huang, T. Huang, N. Qin, Y. Li, and Y. Yang, “Finite-time control
for a UAV system based on ﬁnite-time disturbance observer,” Aerosp.
Sci. Technol., vol. 129, Oct. 2022, Art. no. 107825.
[48] B. Wang, Y. Zhang, and W. Zhang, “A composite adaptive fault-tolerant
attitude control for a quadrotor UAV with multiple uncertainties,” J. Syst.
Sci. Complex., vol. 35, no. 1, pp. 81–104, Feb. 2022.
[49] L. Liu, J. Fei, and X. Yang, “Adaptive interval type-2 fuzzy neural
network sliding mode control of nonlinear systems using improved
extended state observer,” Mathematics, vol. 11, no. 3, p. 605, Jan. 2023,
doi: 10.3390/math11030605.
[50] J. Pan, B. Shao, J. Xiong, and Q. Zhang, “Attitude control of quadrotor
UAVs based on adaptive sliding mode,” Int. J. Control, Autom. Syst.,
vol. 21, no. 8, pp. 2698–2707, Aug. 2023.
[51] Y. Du, P. Huang, Y. Cheng, Y. Fan, and Y. Yuan, “Fault tolerant control
of a quadrotor unmanned aerial vehicle based on active disturbance
rejection control and two-stage Kalman ﬁlter,” IEEE Access, vol. 11,
pp. 67556–67566, 2023.
[52] X. Zhang, B. Hou, and Y. Mei, “Deadbeat predictive current con-
trol of permanent-magnet synchronous motors with stator current and
disturbance observer,” IEEE Trans. Power Electron., vol. 32, no. 5,
pp. 3818–3834, May 2017.
[53] B. Chang, L. Long, Y. Cheng, Z. Shen, and Z. Wang, “Attitude track-
ing control of quadrotors under multiple event-triggered mechanism,”
J. Xi’an Jiaotong Univ., vol. 56, no. 3, pp. 206–214, 2022.
Xiangze Lin received the B.S. degree in applied
mathematics and the M.S. degree in automation
from Southeast University, Nanjing, China, in 2000
and 2006, respectively, and the Ph.D. degree in
automation from Nanjing University of Science
and Technology, Nanjing, in 2012. He is currently
a Professor with the College of Artiﬁcial Intelli-
gence, Nanjing Agricultural University, Nanjing. His
research interests include switched systems, non-
linear control with physical/cyber constraints, and
control applications in smart agriculture.
Weili Fu received the B.S. degree in electrical
engineering and automation from Sichuan Nor-
mal University, Chengdu, China, in 2020. She
is currently pursuing the M.S. degree with Nan-
jing Agricultural University, Nanjing, China. Her
research primarily focuses on UAV attitude control
algorithms.
Junwen Tu was born in Xinyang, China, in 2001. He
is currently pursuing the M.S. degree in electronic
information with the College of Artiﬁcial Intel-
ligence, Nanjing Agricultural University, Nanjing,
China. His research interests include sliding-mode
control and its applications in permanent magnet
synchronous motors.
Ju H. Park (Senior Member, IEEE) received the
Ph.D. degree in electronics and electrical engi-
neering from Pohang University of Science and
Technology (POSTECH), Republic of Korea, in
1997.
Following a Research Associate with the Engi-
neering Research Center (1997-2000), POSTECH,
he joined the Faculty of Yeungnam University,
where he currently holds the prestigious title of
Chunma Chair Professor. A proliﬁc scholar, he has
co-authored ﬁve inﬂuential monographs, including
Dynamic Systems With Time Delays: Stability and Control (Springer Nature,
2019). His scholarly impact is reﬂected in over 56 000 citations and an H-
index of 114. His research portfolio spans nonlinear dynamics, intelligent
systems, and artiﬁcial intelligence.
Prof. Park is a fellow of Korean Academy of Science and Technology
(KAST). He was recognized by Clarivate as a Highly Cited Researcher for
eight consecutive years, he achieved the rare distinction of being listed in three
separate ﬁelds engineering, computer science, and mathematics from 2019 to
2022. He currently serves as a Receiving Editor for Nonlinear Dynamics
(Springer-Nature) and also hold or has held editorial positions with several
leading international journals, including Artiﬁcial Intelligence Science and
Engineering, The Journal of The Franklin Institute, Applied Mathematics and
Computation, IET Control Theory and Applications, IEEE TRANSACTIONS
ON FUZZY SYSTEMS, IEEE TRANSACTIONS ON NEURAL NETWORKS AND
LEARNING SYSTEMS, and IEEE TRANSACTIONS ON CYBERNETICS.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 12:54:41 UTC from IEEE Xplore.  Restrictions apply.
