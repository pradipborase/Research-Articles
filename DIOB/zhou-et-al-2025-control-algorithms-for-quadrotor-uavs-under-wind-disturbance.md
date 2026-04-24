# zhou-et-al-2025-control-algorithms-for-quadrotor-uavs-under-wind-disturbance.pdf

## Page 1

Control Algorithms for Quadrotor UAVs
under Wind Disturbance
Le Zhou1; Chen Xu2; Fengnian Tian3; and Yijun Mao4
Abstract: As unmanned aerial vehicle (UAV) outdoor missions increase, low-altitude wind disturbances significantly affect flight per-
formance and demand stronger control robustness. Based on the quadrotor dynamic model considering wind disturbances developed in the
previous work, this study investigates the antidisturbance performance of proportional-integral-derivative control, sliding mode control
(SMC), and SMC based on the extended state observer (SMCESO) through simulations and experiments under both steady and sudden
wind conditions. The study considers both linear and nonlinear control strategies as well as passive- and active-disturbance rejection ap-
proaches. Results show that SMCESO achieves superior disturbance rejection under time-varying winds, though with larger angular fluc-
tuations than SMC at high wind speeds. A sensitivity analysis of key SMCESO parameters provides tuning guidance. Additionally, the
consistency of data results between simulation and experiment verifies the established dynamic model that accounts for wind disturbances.
DOI: 10.1061/JAEEEZ.ASENG-6505. © 2025 American Society of Civil Engineers.
Author keywords: Quadrotor; Attitude control; Wind disturbances; Extended state observer; Sliding-mode control.
Introduction
In recent years, outdoor flight missions of unmanned aerial vehicles
(UAVs) have gradually increased, while wind disturbances in low-
altitude environments significantly affect their flight performance
and place higher demands on control algorithms. Quadrotor UAVs,
in particular, have a wide range of applications due to their rela-
tively simple structure and high flexibility (Khadka, et al. 2020;
Atif et al. 2021; Dalwadi et al. 2023; Zeng et al. 2023; Jiang et al.
2024). The quadrotor UAV is a highly coupled system with six de-
grees of freedom, controlled by four inputs, making it a typical
underactuated system (Amin et al. 2016). Furthermore, due to their
small size and light weight, quadrotors are more sensitive to external
disturbances (Ariyibi and Tekinalp 2020). Therefore, it is neces-
sary to investigate the impact of wind disturbance on UAV control
algorithms to ensure their flight performance under unknown wind
conditions.
To enhance UAV performance against wind disturbances, re-
searchers have proposed various control methods. Studies on dis-
turbance rejection of UAVs can generally be classified into two
categories: passive resistance control and active resistance control.
Passive resistance control refers to a control system that calculates
the appropriate control inputs to counteract disturbances when they
significantly affect the position and attitude of UAVs. Meanwhile,
active resistance control involves controllers that can estimate and
compensate for disturbances in real time (Shen et al. 2022).
Dai et al. (2018) proposed a passive-disturbance controller for
UAVs based on acceleration feedback, which introduced angular and
linear acceleration feedback to improve the disturbance rejection ca-
pability of the system without changing the original controller struc-
ture. Xu et al. (2019) designed a dual-loop tracking control method to
counter wind disturbances. In the inner loop, finite-frequency H∞
control was used for attitude stabilization, and H∞loop shaping con-
trol combined with proportional-integral-derivative (PID) was em-
ployed to achieve the desired tracking performance in the presence
of wind disturbances. Xia et al. (2022) proposed a robust passive
fault-tolerant control strategy of UAVs in the presence of partial
propeller fault and external disturbance. A first-order filter based
dynamics estimator was introduced as the compensation mechanism.
Vahdanipour and Khodabandeh (2019) developed a fractional-order
sliding-mode controller based on a backstepping approach to mit-
igate wind disturbances and handle variations in load and moments
of inertia. The simulation results demonstrated that the use of
fractional-order sliding surfaces in the controller significantly en-
hanced trajectory tracking performance. Husain et al. (2024) pro-
posed an integral sliding-mode control (SMC) design based on a
barrier function (ISMCbf), which can effectively eliminate the chat-
tering phenomenon associated with the conventional ISMC and
does not require prior knowledge of the disturbance bounds or their
derivatives. However, while passive antidisturbance control is rela-
tively simple in principle and can ensure tracking accuracy, it tends
to cause significant lag and may lead to oscillations. The active anti-
disturbance control, on the other hand, though more complex in
structure, requires more parameter adjustments and demands higher
computational performance, has been widely used in the design of
quadrotor controllers in recent years due to its ability to estimate and
compensate for multisource disturbances, and thus achieves rapid
suppression of disturbances.
Xing et al. (2023) addressed both wind disturbances and sto-
chastic system noise by designing a two-stage particle filter for the
estimation of UAV states and wind conditions without additional
1Master’s Student, School of Aerospace Engineering, Huazhong Univ.
of Science and Technology, Wuhan 430074, People’s Republic of China.
Email: 1121942834@qq.com
2Associate Professor, School of Naval Architecture, Ocean and Energy
Power Engineering, Wuhan Univ. of Technology, Wuhan 430063, People’s
Republic of China. Email: chenxu@whut.edu.cn
3Assistant Professor, School of Aerospace Engineering, Huazhong
Univ. of Science and Technology, Wuhan 430074, People’s Republic of
China. Email: tianfengnian@hust.edu.cn
4Professor, School of Aerospace Engineering, Huazhong Univ. of Science
and Technology, Wuhan 430074, People’s Republic of China (corresponding
author). Email: maoyijun@hust.edu.cn
Note. This manuscript was submitted on April 8, 2025; approved on
September 17, 2025; published online on November 27, 2025. Discussion
period open until April 27, 2026; separate discussions must be submitted
for individual papers. This paper is part of the Journal of Aerospace En-
gineering, © ASCE, ISSN 0893-1321.
© ASCE
04025131-1
J. Aerosp. Eng.
 J. Aerosp. Eng., 2026, 39(2): 04025131 
 Downloaded from ascelibrary.org by Netaji subhas university of technology on 03/15/26. Copyright ASCE. For personal use only; all rights reserved.

## Page 2

wind sensors. The disturbances were attenuated by combining adap-
tive wind compensation with a nonsingular terminal sliding-mode
controller. Gremillion and Humbert (2016) used feedback control
by estimating force and torque induced accelerations from a redun-
dant, distributed array of accelerometers, effectively addressing
both actuator disturbances and exogenous wind gusts. Mofid et al.
(2021) developed a supertwisting terminal sliding-mode controller
to achieve finite-time attitude and position tracking of the quad-
rotor while considering input delays, model uncertainties, and wind
disturbances. However, the controller required a large number of
parameter adjustments and was selected using the trial-and-error
method. Labbadi et al. (2022) investigated the robust continuous
fractional-order nonlinear sliding-mode control scheme for a dis-
turbed uncertain quadrotor, and a fractional-order switching element
was employed to improve the dynamic response by substituting con-
ventional operators with fractional-order ones in the error dynamics.
Abbas et al. (2024) developed an adaptive integral sliding-mode con-
trol (AISMC) scheme, which can avoid overestimation of the sliding
gain under unknown prior knowledge of perturbations. Compar-
ative studies between AISMC, ISMC, and other control methods
demonstrate that the proposed method achieves superior tracking
performance and accuracy. Guo et al. (2020) proposed a multiple
observers-based antidisturbance control scheme for a quadrotor
UAV subjected to both cable-suspended payload disturbances and
wind disturbances. Experimental results under wind disturbance,
payload oscillating disturbance, and hybrid disturbances proved
the robustness and effectiveness of the proposed method compared
to the classical PID method. Li et al. (2022b) designed a composite
control strategy integrating nonsmooth control with a reduced-order
general proportional integral (GPI) observer. The feedback com-
ponent employed a nonsmooth controller, while the feedforward
component used the reduced-order GPI observer. Cai et al. (2024)
combined a sliding-mode controller with a fixed-time disturbance
observer to address UAV trajectory tracking under time-varying
wind disturbances, and numerical simulations and actual flight ex-
periments were performed to confirm the control strategy’s robust-
ness and effectiveness. Wang et al. (2019) designed a nonlinear
disturbance observer-based adaptive SMC strategy to simultane-
ously compensate for actuator faults, parametric uncertainties, and
external disturbances. By incorporating adaptive control parame-
ters in both the continuous and discontinuous control components,
this approach substantially alleviates the control chattering prob-
lem. Lotufo et al. (2019) proposed an attitude control method that
combined active-disturbance rejection control (ADRC) with em-
bedded model control This approach extended the validity of the
simplified controllable model and was also capable of handling
input disturbances that enter the system at multiple points.
Disturbance observation methods combined with model control
are widely used in active-disturbance rejection control. The main
observation techniques include the extended state observer (ESO),
uncertainty and disturbance estimator, generalized proportional inte-
gral observer, and so on. Chen et al. (2016) gave a systematic survey
on disturbance-observer-based control methods. The idea of ESO
originates from ADRC (Shen and Xu 2021); ESO expands the total
disturbances into a new state variable of the system and estimates the
state from the output of the system to achieve the estimation of the
total disturbances. The ESO is the core component of the ADRC
structure. Al-Dujaili et al. (2024) conducted a comparative study
between the linear extended state observer (LESO) and the non-
linear extended state observer (NESO), and the results showed that
the ADRC algorithm based on LESO outperformed the NESO-
based algorithm in both disturbance rejection capability and robust-
ness to parameter variations. Cai et al. (2019) designed a finite-time
convergent extended state observer to enhance the performance of
the ADRC controller. The chaotic gray wolf optimization algorithm
was developed to obtain the optimal parameters for quadrotor con-
trollers in trajectory tracking tasks subject to external disturbances.
Yang et al. (2018) investigated the attitude control of a quadrotor
under a wind field by using a double closed-loop control framework.
Active-disturbance control and PD control were used in the inner
and outer loops, respectively, with the wind disturbances estimated
by the inner-loop ESO. Zhao et al. (2019) investigated a double
closed-loop control strategy for a quadrotor that integrated the advan-
tages of ADRC and integral SMC. A nonlinear ESO was adopted in
the inner loop to estimate internal uncertain dynamics and external
wind disturbances in a timely manner. Wang et al. (2022) developed
an adaptive composite antidisturbance attitude controller aimed at
addressing the ground effect and propeller failure disturbances. The
controller, which combined ADRC with a disturbance observer based
on a nominal inverse model, was designed to estimate disturbances in
real time. Cui et al. (2021) adopted an adaptive supertwisting sliding-
mode control for a quadrotor UAV to track a desired trajectory under
gust winds. The gust winds were estimated using an adaptive super-
twisting ESO, with the ESO gains adjusted based on estimation
errors through an adaptive law. Wang et al. (2021) proposed a back-
stepping sliding-mode control algorithm based on a high-order
ESO. The tracking and estimation errors of the designed method
were proven to be arbitrarily small using the Lyapunov theory. Tang
et al. (2019) proposed a double power reaching law controller for
sliding-mode control based on an ESO. Simulation results indicated
that the proposed controller achieved a position optimization rate of
approximately 90% in wind conditions compared to SMC. How-
ever, an excessive disturbance observation load may induce a lag in
the ESO’s position output, undermining the real-time performance
of the UAV. Chen et al. (2022) designed a novel robust controller
using a NESO (Zhao and Guo 2017) and recursive sliding-mode
control. While the parameter design of the NESO did not rely on
information about unknown lumped disturbances, it increased the
complexity of the selection and modification process for algorithm
parameters. Hasan et al. (2023) designed an ADRC for a tricopter
UAV based on three types of extended state observers: the fractional-
order extended state observer, the NESO, and the supertwisting ex-
tended state observer. The performance differences among these
observers were evaluated through comparative analysis in terms of
robustness to parameter variations and disturbance rejection ca-
pability. Lv et al. (2019) proposed a model predictive control ap-
proach with an ESO for tracking control of a quadrotor under wind
disturbances. The ESO gain was optimized in real time to create an
extended state-based Kalman filter for noise management, and
feedback linearization was used to simplify the attitude system
while accounting for nonlinearities.
The aforementioned literature further illustrated the perfor-
mance advantages of the ESO in active wind disturbances. In most
cases, flight experiments under wind field disturbances are con-
ducted for the designed controller in real physical environments.
However, to the best of the authors’ knowledge, it is also necessary
to investigate the simulation study of control algorithms under
wind fields based on a relatively precise and reliable quadrotor
dynamic model and further compare the results with experimental
data to verify their accuracy and credibility. Simulation efficiently
examines wind effects on UAVs and assesses the controller’s
response, serving as a key guide for reducing risks and optimizing
real-world flight experiments. Furthermore, most previous studies
have overlooked a comprehensive investigation of UAV wind
disturbance rejection from multiple perspectives, including linear
versus nonlinear controllers and active versus passive control
strategies.
© ASCE
04025131-2
J. Aerosp. Eng.
 J. Aerosp. Eng., 2026, 39(2): 04025131 
 Downloaded from ascelibrary.org by Netaji subhas university of technology on 03/15/26. Copyright ASCE. For personal use only; all rights reserved.

## Page 3

In summary, based on the dynamic model considering wind dis-
turbances developed in Zhou (2025), the main contributions of this
work are as follows:
1. Simulation and experimental analyses were conducted on three
controllers—PID, SMC, and SMC based on the extended state
observer (SMCESO)—encompassing both linear and nonlinear
designs, as well as active and passive control strategies, to evalu-
ate and compare their antidisturbance performance under time-
varying wind conditions, including steady winds and sudden
gusts.
2. The comparative results highlight the superior performance of
the SMCESO controller as a composite active control strategy,
combining the robustness of SMC with the disturbance estima-
tion capability of ESO, enabling it to perform exceptionally well
in complex and uncertain environments. In addition, sensitivity
analysis of the key parameters in the SMCESO controller was
performed, providing guidance for parameter tuning and enhanc-
ing its practical applicability.
3. The comparison results between simulation and experiment fur-
ther verify the reliability of the established UAV dynamic model
with wind disturbances, which could help to guide the design of
flight control algorithms with stronger wind disturbance resis-
tance and robustness.
This paper is organized as follows: the UAV dynamic model, the
design of the SMCESO, and the sensitivity analysis of its key
parameters are given in the section titled “Dynamic Modeling and
Controller Design.” In the section titled “Simulation Analysis,” the
simulation results of the control algorithm under various time-
varying wind disturbances are presented. In the section titled
“Experimental Studies,” the platform experiments under the same
conditions are conducted. The section titled “Conclusion” draws
the main conclusions. The main framework is shown in Fig. 1.
Dynamic Modeling and Controller Design
Dynamic Modeling
The UAV used is an X-type quadrotor, and the coordinate systems
are shown in Fig. 2, where oexeyeze represents the inertial coordi-
nate system, it takes the center of the earth oe as the coordinate ori-
gin, oexe is in a certain direction in the horizontal plane, oeze is
perpendicular to the ground downward, and oeye is determined
by the right-hand rule; obxbybzb represents the body coordinate
system, with the origin in the center of the quadrotor, obxb is in
the middle of the propellers pointing to the forward flight, obzb is
perpendicular to the obxb pointing toward the bottom of the body,
and obyb is determined by the right-hand rule.
The vector expression of the dynamic model is
m¨p ¼ mge3 −Re
bðfe3 þ fDÞ
J ˙Ω ¼ ðJΩÞ × Ω þ ðτ þ τDÞ
ð1Þ
where m = mass of UAV; g = gravitational acceleration; p = UAV
position in inertial coordinate system; J = moment of inertia; R ¼
Re
b = transformation matrix from the body to the inertial coordinate
system; e3 = unit vector along the z direction in the inertial coor-
dinate system; Ω ¼ ½ p
q
r T = angular velocity vector; and f
and τ ¼ ½ τx
τy
τz T = resultant force and moment generated by
the four propellers of the UAV, respectively, and they are related to
the thrust of each motor through the following equation:
2
66664
f
τx
τy
τz
3
77775
¼
2
66666664
1
1
1
1
−
ﬃﬃ
2
p
2 l
ﬃﬃ
2
p
2 l
ﬃﬃ
2
p
2 l
−
ﬃﬃ
2
p
2 l
ﬃﬃ
2
p
2 l
−
ﬃﬃ
2
p
2 l
ﬃﬃ
2
p
2 l
−
ﬃﬃ
2
p
2 l
kτ
kτ
−kτ
−kτ
3
77777775
2
66664
T1
T2
T3
T4
3
77775
ð2Þ
Fig. 2. Quadrotor and the coordinate system.
Fig. 1. Framework of UAV wind-rejection control.
© ASCE
04025131-3
J. Aerosp. Eng.
 J. Aerosp. Eng., 2026, 39(2): 04025131 
 Downloaded from ascelibrary.org by Netaji subhas university of technology on 03/15/26. Copyright ASCE. For personal use only; all rights reserved.

## Page 4

where Ti = thrust of each propeller; subscript i ¼ 1 ∼4 = index
number of four propellers; and l = distance from the motor to the
center of the quadrotor; fD ¼ ½ fDH
0 T ¼ ½ fDx
fDy
0 T and
τD ¼ ½ τDx
τ Dy
τDz T are, respectively, the resultant drag and
drag moment of the UAV. The expressions of Ti, fDH, and τD
are as follows, and the detailed processes of formula derivation
and parameter calibration can be found in (Zhou 2025)
Ti ¼ 1.096 × 10−5ω2
i −4.441 × 10−4Vrzωi þ 2.659 × 10−3kVrhk2
fDH ¼ 7.5 × 10−5ωsum
Vrx
Vry

þ 7.3 × 10−3
V2rx
V2ry

τD ¼
2
64
τDx
τDy
τDz
3
75 ¼ 7.5 × 10−5dωsum
2
64
−Vry
Vrx
0
3
75 þ
ﬃﬃ
2
p
2 × 7.5 × 10−5l
×
2
64
0
0
Vrxð−ω1 þ ω2 þ ω3 −ω4Þ þ Vryðω1 −ω2 þ ω3 −ω4Þ
3
75
ð3Þ
where ωi = rotational angular speed of the individual propeller;
ωsum = sum of the four propeller rotational speeds; Vr ¼
½ Vrh
Vrz T ¼ ½ Vrx
Vry
Vrz T = relative wind speeds in body
coordinate system; and d = vertical distance from propeller plane to
UAV center. The first and second terms in fDH represent the pro-
peller drag and the fuselage drag, respectively.
Controller Design
In this research, a comparative simulation and experimental study
of the PID, SMC, and SMCESO controllers under time-varying
wind disturbances is presented. Specifically, the PID controller is
widely applied in engineering practice as a linear control method
(Lopez-Sanchez and Moreno-Valenzuela 2023). The SMC is val-
ued for its robustness to model errors, disturbances, and parameter
uncertainties, along with its ability to globally stabilize underactu-
ated systems. Moreover, SMCESO enhances traditional SMC by
incorporating an ESO to estimate and compensate for total disturb-
ances in real time. This section introduced the design of the
SMCESO controller; the design of PID and SMC controllers can
be referenced in Zheng et al. (2014) and Karahan and Kasnakoglu
(2019).
Extended State Observer
The extended state observer-based sliding-mode control is intro-
duced in this section, and the diagram of the proposed control
scheme is shown in Fig. 3. In this research, the attitude control
and altitude control of the quadrotor are mainly considered, and
the roll angle is taken as an example to design the controller. The
controller design for the pitch, yaw, and altitude channels is the
same. According to Eq. (1), the scalar expression of the roll angle
is expressed as
¨ϕðtÞ ¼
˙θðtÞ ˙ψðtÞðIyy −IzzÞ
Ixx
þ τDxðtÞ
Ixx
þ τxðtÞ
Ixx
ð4Þ
where the first two terms in the equation represent the total disturb-
ances consisting of the dynamic coupled part of the roll angle and
external disturbances, i.e., fϕ ¼ ð˙θ ˙ψðIyy −IzzÞÞ=Ixx þ ðτDx=IxxÞ,
and given that bϕ ¼ 1=Ixx, the aforementioned equation can be
rewritten as
¨ϕ ¼ fϕ þ bϕτx
ð5Þ
Define the state variables x1 ¼ ϕ, x2 ¼ ˙ϕ, x3 ¼ fϕ, and Eq. (5)
is expressed as
˙x1 ¼ x2
˙x2 ¼ x3 þ bϕτx
˙x3 ¼ ˙fϕ
y ¼ ϕ ¼ x1
ð6Þ
The extended state observer of Eq. (6) is designed as follows:
γϕ ¼ ˆx1 −ϕ ¼ ˆx1 −y
˙ˆx1 ¼ ˆx2 −α1
ε γϕ
˙ˆx2 ¼ ˆx3 −α2
ε2 γϕ þ bϕτx
˙ˆx3 ¼ −α3
ε3 γϕ
ð7Þ
where ˆx1, ˆx2, and ˆx3 = state variables of the ESO, and as t →∞,
the ˆx1 →x1, ˆx2 →x2, ˆx3 →fϕ, which means the state variables ˆxi
of the ESO track the state variables xi and fϕ of the original system.
The parameters ε, α1, α2, and α3 are positive real coefficients of the
ESO. The response speed of the ESO can be improved by reducing
the ε; however, an excessively small ε will result in oscillations in
a real system. The polynomial s3 þ α1s2 þ α2s þ α3 satisfies the
Hurwitz condition, where s is the Laplace operator.
The convergence of the extended state observer is proven as
follows.
The observation error equation is defined as
η ¼ ½ η1
η2
η3 T
ð8Þ
where η1 ¼ ðx1 −ˆx1Þ=ε2, η2 ¼ ðx2 −ˆx2Þ=ε, and η3 ¼ f −ˆx3. It
can be derived that
ε˙η1 ¼ ˙x1 −˙ˆx1
ε
¼ 1
ε

x2 −

ˆx2 þ α1
ε ðy −ˆx1Þ

¼ 1
ε

x2 −ˆx2 −α1
ε ðy −ˆx1Þ

¼ −α1
ε2 ðx1 −ˆx1Þ þ 1
ε ðx2 −ˆx2Þ ¼ −α1η1 þ η2
ð9Þ
ε˙η2 ¼ ε ˙x2 −˙ˆx2
ε
¼ bϕτx þ fϕ −

bϕτx þ ˆx3 þ α2
ε2 ðy −ˆx1Þ

¼ fϕ −ˆx3 −α2
ε2 ðy −ˆx1Þ ¼ −α2
ε2 ðx1 −ˆx1Þ þ ðfϕ −ˆx3Þ
¼ −α2η1 þ η3
ð10Þ
Fig. 3. Diagram of the proposed control scheme.
© ASCE
04025131-4
J. Aerosp. Eng.
 J. Aerosp. Eng., 2026, 39(2): 04025131 
 Downloaded from ascelibrary.org by Netaji subhas university of technology on 03/15/26. Copyright ASCE. For personal use only; all rights reserved.

## Page 5

ε˙η3 ¼ εð˙fϕ −˙ˆx3Þ ¼ ε

˙fϕ −α3
ε3 ðy −ˆx1Þ

¼ ε˙fϕ −α3
ε2 ðy −ˆx1Þ ¼ −α3η1 þ ε˙fϕ
ð11Þ
Then the state equation of the observation error can be written as
˙η ¼ 1
ε Aη þ B˙fϕ
ð12Þ
where
A ¼
2
64
−α1
1
0
−α2
0
1
−α3
0
0
3
75;
B ¼
2
64
0
0
1
3
75
The characteristic equation of matrix A is expressed as
λ3 þ α1λ2 þ α2λ þ α3 ¼ 0
ð13Þ
where matrix A is a Hurwitz matrix by choosing suitable param-
eters α1, α2, and α3.
For any given symmetric positive definite matrix Q, there exists
a symmetric positive definite matrix P satisfying the following Lya-
punov equation:
ATP þ PA þ Q ¼ 0
ð14Þ
Define the Lyapunov function of the extended state observer as
VE ¼ ηTPη
ð15Þ
The derivative of the aforementioned equation is
˙VE ¼ ˙ηTPη þ ηTP˙η
¼
1
ε Aη þ B˙fϕ
T
Pη þ ηTP
1
ε Aη þ B˙fϕ

¼ 1
ε ηTATPη þ ðB˙fϕÞTPη þ 1
ε ηTPAη þ ηTPB˙fϕ
¼ 1
ε ηTðATP þ PAÞη þ 2ηTPB˙fϕ
¼ −1
ε ηTQη þ 2ηTPB˙fϕ
ð16Þ
From Arindama (2021), there exists
˙V ≤−λminðQÞ
ε
kηk2 þ 2LkPBkkηk
ð17Þ
where j˙fϕj ≤L, λminðQÞ = minimum eigenvalue of Q.
Take the positive real number λ1 < λ2 < λ3 to make the follow-
ing equation valid:
jλI3 −Aj ¼
Y
3
i¼1
ðλ þ λiÞ ¼ 0
ð18Þ
where I3 = identity matrix. Thus, the eigenvalues of the matrix A
are different from each other, so there exists an invertible real ma-
trix R to satisfy the following equation:
A ¼ Rdiagf−λ1; −λ2; −λ3gR−1
ð19Þ
and the following equation is given that
exp
1
ε At

¼ Rdiag

exp
−λ1t
ε

; exp
−λ2t
ε

;
exp
−λ3t
ε

R−1
ð20Þ
Then, the solution to the observer error is obtained as
ηðtÞ ¼ exp
1
ε At

ηð0Þ þ
Z t
0
exp
1
ε Aðt −τÞ

Bfϕdτ
ð21Þ
As recommended by Arindama (2021), one has that
kηðtÞk ¼
				exp
1
ε At
				kηð0Þk þ L
Z t
0
				exp
1
ε Aðt −τÞ
				kBkdτ
≤kRkkR−1k

exp

−λ1t
ε

kηð0Þk
þ LkBk
Z t
0
exp

−λ1
ε ðt −τÞ

dτ

≤kRkkR−1k

exp

−λ1t
ε

kηð0Þk
þ ε
λ1
LkBk

1 −exp

−λ1t
ε

ð22Þ
where kBk ¼ 1, ηð0Þ represents the initial error. So there exists
M ∈Rþ, and the following equation can be satisfied as
lim
t→∞kηðtÞk ≤εLkRkkR−1kkBk
λ1
¼ εM
ð23Þ
which implies that the error of the extended observer is bounded,
and as ε →0þ, then limt→∞kηðtÞk →0, which means that the ob-
servation error gradually converges to zero. The relevant proof
method can be seen in Xiong et al. (2022) and Zhang et al. (2018).
Note that the derivative of the initial signal is often required be-
fore it is fed into the SMCESO controller. The tracking differen-
tiator is commonly employed to generate smooth transition signals
and their derivatives, which helps reduce initial errors and overshoot
in the system while avoiding the noise amplification introduced by
directly differentiating the initial signal numerically. A discrete dif-
ferentiator was adopted in the simulations of this study.
Sliding-Mode Controller
Take the roll angle as an example to design the sliding-mode con-
troller, and the error is defined as
eϕ ¼ ϕd −ϕ
ð24Þ
The sliding manifold of the SMC is designed as follows:
sϕ ¼ cϕeϕ þ ˙eϕ
ð25Þ
where the parameter cϕ is required to satisfy the Hurwitz condition,
i.e., cϕ > 0.
The exponential reaching law is employed, with the sign func-
tion replaced by the hyperbolic tangent function to reduce the chat-
tering phenomenon of the controller, as follows:
˙sϕ ¼ −kϕ tanh
sϕ
γϕ

−λϕsϕ
ð26Þ
where kϕ > 0, λϕ > 0, γϕ > 0. The parameter γϕ adjusts the slope
of the function and helps balance the convergence speed and the
response smoothness. Take kϕ > ¯dϕ, where ¯dϕ is an upper bound
of the perturbation. The sliding-mode controller is given as
© ASCE
04025131-5
J. Aerosp. Eng.
 J. Aerosp. Eng., 2026, 39(2): 04025131 
 Downloaded from ascelibrary.org by Netaji subhas university of technology on 03/15/26. Copyright ASCE. For personal use only; all rights reserved.

## Page 6

τx ¼ Ixx

cϕ ˙ϕd þ ¨ϕd −cϕ ˙ˆϕ −Iyy −Izz
Ixx
˙ˆθ ˙ˆψþkϕ tanh
ˆsϕ
γϕ

þ λϕˆsϕ

ð27Þ
where ˆsϕ ¼ cϕˆeϕ þ ˙ˆeϕ, ˆeϕ ¼ ϕd −ˆϕ, and ˙ˆeϕ ¼ ˙ϕd −˙ˆϕ; ˙ˆθ and ˙ˆψ =
estimated values based on ESO of ˙θ and ˙ψ, respectively. And rea-
sonable selection of controller parameters can make the closed-loop
system error close to zero.
Then the expression of the control input of roll angle is given as
τϕ ¼ τx −ˆx3
bϕ
ð28Þ
Lyapunov stability approach is used to prove and evaluate the
state convergence property of controller Eq. (27); the proof process
is presented as follows.
The Lyapunov function of the controller is taken as
Vs ¼ 1
2 s2
ϕ
ð29Þ
The derivative of the aforementioned equation is
˙VS ¼ sϕ˙sϕ ¼ sϕ

cϕ ˙ϕd þ ¨ϕd −cϕ ˙ϕ −
˙θ ˙ψðIyy −IzzÞ
Ixx
−τDx
Ixx
−τx
Ixx

¼ sϕ

−kϕ tanh
sϕ
γϕ

−λϕsϕ −τDx
Ixx

¼ −kϕsϕ tanh
sϕ
γϕ

−λϕs2
ϕ −τDx
Ixx
sϕ < 0;
sϕ ≠0
ð30Þ
It can be shown that Vs is positive definite and radially un-
bounded and ˙Vs is negative definite, which means that the system
has global asymptotic stability. Note that in the proof, the hyper-
bolic tangent function is treated as the sign function, and the system
is asymptotically stable in the absence of disturbances, whereas it
can be guaranteed to be stabilized in the presence of disturbances.
For more details on the Lyapunov-based proofs of the SMCESO
controller, please refer to Chen et al. (2022), Li et al. (2022a), and
Zhao et al. (2022).
In this research, the parameters of the SMCESO controller are
obtained through the empirical-tuning method. Initially, parameters
are selected based on SIMULINK simulations, where the prelimi-
nary choices are made when the altitude and attitude angle tracking
performance in response to step inputs is satisfactory. Subsequently,
the controller is implemented in a real UAV, with control commands
issued via a remote controller. The final parameters are determined
based on the actual attitude angle response curves to the given con-
trol commands, which are obtained as follows: α1 ¼ 3, α2 ¼ 3,
α3 ¼ 1, ε ¼ 0.1, cϕ ¼ cθ ¼ cψ ¼ 5, kϕ ¼ kθ ¼ kψ ¼ 1, λϕ ¼
λθ ¼ λψ ¼ 10, and γϕ ¼ γθ ¼ γψ ¼ 0.7 for the attitude channel
and parameters ch ¼ 15, kh ¼ 5, λh ¼ 8, and γh ¼ 0.5 for the al-
titude channel.
Parameter Sensitivity Analysis
For the SMCESO controller, there are four parameters related to
SMC: the sliding surface parameter c, the switching gain term k,
the exponential reaching term λ, and the scaling factor γ in the hy-
perbolic tangent function. The scaling factor γ is used to adjust the
smoothness of the tanh function. Since its variation range is rela-
tively small and can be easily determined, γ is fixed at 0.7 to reduce
the complexity of the sensitivity analysis and is therefore not included
in the analysis. Two parameters are associated with the ESO, namely,
ωa and ε, which jointly determine the observer bandwidth. In Eq. (7),
the coefficients α1, α2, and α3 are related to ωa as follows: α1 ¼
3ωa, α2 ¼ 3ω2a, and α3 ¼ ω3a. Therefore, once the value of ωa is
determined, the coefficients α1, α2, and α3 in Eq. (7) can be
uniquely specified.
In summary, five parameters, namely, c, k, λ, ωa, and ε, are se-
lected for the sensitivity analysis, with the roll channel serving as an
example. For simplicity in the subsequent discussion, the subscript
notation of the roll channel control parameters is omitted.
To conduct the analysis, the parameter ranges are first defined,
and uniform sampling is performed. The total number of sample
points is set to 150, and the ranges of the parameters are as follows:
c ∈½2; 10; k ∈½0.3; 5; λ ∈½5; 15; ωa ∈½0.5; 2; ε ∈½0.05; 0.15
ð31Þ
The distribution of the sampled points is shown in Fig. 4.
In Fig. 4, the five plots on the diagonal represent the distribu-
tion of each parameter within the specified range, where all histo-
grams appear approximately uniform. The off-diagonal plots show
scatter plots between pairs of different variables. Since no cross
correlation among parameters was specified, the scatter plots ap-
pear uncorrelated.
The objective function is defined as the sum of the squared er-
rors (SSE) between the model inputs and outputs, expressed as
SSE ¼
X
T
t¼t0
ðyt −ydtÞ2
ð32Þ
where ydt = model input, which is defined as the desired roll angle
of 10°; and yt = model output, which corresponds to the actual roll
angle tracking. The simulation time is set to t ¼ 10 s. After com-
pleting 150 simulation runs, statistical analyses were conducted to
quantify the influence of each parameter on the objective function.
Four indicators were selected for evaluation: namely, linear corre-
lation, standardized linear regression, rank correlation, and stand-
ardized rank regression (Rice 1994). The results are presented in
the tornado plot shown in Fig. 5 and summarized in Table 1.
In Fig. 5, the vertical axis represents the five key parameters,
arranged from top to bottom in order of their influence. Since four
evaluation indicators were adopted, the parameters are ranked ac-
cording to the first indicator, linear correlation. The horizontal axis
indicates the degree of influence of each variable on the output,
with longer bars corresponding to higher sensitivity. The direction
Fig. 4. Distribution of the sampled points.
© ASCE
04025131-6
J. Aerosp. Eng.
 J. Aerosp. Eng., 2026, 39(2): 04025131 
 Downloaded from ascelibrary.org by Netaji subhas university of technology on 03/15/26. Copyright ASCE. For personal use only; all rights reserved.

## Page 7

of the bars reflects whether the effect on the output is positive or
negative. Therefore, as shown in Fig. 5, the parameters ωa and ε
exhibit the highest sensitivity, followed by c and λ, while the sen-
sitivity of k is relatively low. This indicates that, for the SMCESO
controller, the parameters associated with the ESO are slightly
more sensitive than those related to the SMC.
For each parameter, parameters ωa and ε determine the obser-
vation speed and estimation accuracy of the ESO. A larger ωa or a
smaller ε increases the bandwidth of the ESO, resulting in faster
observation, improved disturbance estimation, and higher tracking
accuracy. However, an excessively high bandwidth also increases
sensitivity to noise and may even lead to system instability. The
sliding surface parameter c influences the system’s convergence rate
and dynamic characteristics. Increasing c accelerates the system re-
sponse but also places higher demands on the actuators. The switch-
ing gain k determines the system’s robustness against uncertainties
and disturbances. A higher k increases the reaching speed and dis-
turbance rejection capability but may also induce higher chattering.
The exponential reaching parameter λ is used to adjust the smooth-
ness and speed of the reaching process. A larger λ results in faster
exponential decay and quicker convergence.
In the tuning process of the SMCESO controller, it is generally
recommended to first adjust the ESO parameters to ensure accurate
observation. If the ESO exhibits slow tracking or excessive chat-
tering, the subsequent tuning of the SMC parameters may be ad-
versely affected. The SMC parameters can then be tuned to further
enhance system performance. During tuning, initial values for all
parameters are first determined to ensure system convergence. For
the ESO parameters, ωa can be fixed initially, typically around 1,
followed by adjusting ε to maximize bandwidth while keeping
noise within acceptable limits. This ensures fast estimation and
strong disturbance rejection capability of the ESO. For the SMC
parameters, tuning typically starts with a small value of c near its
initial value while keeping other parameters constant. As c is gradu-
ally increased, the convergence speed of the controller is observed.
For the parameters λ and k, the switching gain term k should exceed
the upper bound of the estimated disturbance. Generally, λ is in-
creased while k is decreased to achieve fast reaching while mitigat-
ing chattering. Finally, all parameters can be fine-tuned to further
optimize overall system performance.
Simulation Analysis
Simulation Setup
The simulation software used is MATLAB R2022a, with the fol-
lowing settings: the simulation time is set to t ¼ 10 s when no wind
disturbances are present and t ¼ 30 s when wind disturbances are
introduced. The fixed step size is set to 0.001 s, and the simulation
solver is ode4 (Runge-Kutta). Table 2 Shows the parameters of the
quadrotor UAV.
Simulation Results and Analyses
Simulation Results without Wind Disturbances
First, the command tracking performances of the three controllers are
verified under conditions without external wind disturbances. The
tracking targets are set as follows: the desired altitude zd ¼ 1 m
and the desired attitude angle ϕd ¼ θd ¼ ψd ¼ 10°, with the initial
altitude and attitude angle of the UAV set to 0 m and ½ 0
0
0  deg,
respectively. The simulation results are shown in Figs. 6 and 7.
Fig. 6 shows the tracking results of altitude and attitude angle; it
can be seen that all three controllers reached the desired values
within 2 s, demonstrating good tracking performance. For the roll
and pitch angles, at the initial stage of tracking, all three controllers
exhibit significant oscillations instead of directly moving toward
the desired angle. Instead, they undergo rapid oscillations in the
opposite direction before converging to the target. This phenome-
non may be attributed to the excessively large initial error and in-
sufficient control input at the beginning, which fails to provide
adequate support for attitude adjustment.
Fig. 7 shows the control inputs of altitude and attitude angles.
Due to the symmetrical structure of the quadrotor and the rotational
inertia Ixx ¼ Iyy set in the simulation, it is obvious that the control
inputs for roll and pitch angles shown in Figs. 7(b and c) are almost
the same. For roll and pitch angles, the maximum amplitudes of
chattering at the initial stage of PID, SMC, and SMCESO control
inputs are 0.353, 0.94, and 0.413 N·m, respectively. The results
show that (1) although both SMC and SMCESO use the hyperbolic
tangent function instead of the sign function to attenuate chattering
to some extent, their initial chattering is still higher compared to
PID. In particular, the chattering peak of the SMC controller is
nearly three times that of the PID controller. (2) Compared to the
Fig. 5. Sensitivity of different parameters to the model output.
Table 1. Evaluation indicators of five different parameters
Parameter
Linear
correlation
Ranked
correlation
Linear
standardized
regression
Ranked
standardized
regression
ωa
0.452
0.467
0.502
0.492
ε
−0.356
−0.215
−0.446
−0.315
c
0.317
0.385
0.303
0.372
λ
0.204
0.259
0.176
0.227
k
−0.037
0.058
−0.037
0.07
Table 2. Parameters of the quadrotor UAV
Parameter
Symbol
Value
UAV mass
m
1.1 kg
Gravitational acceleration
g
9.8 m=s2
Moment of inertia J
Ixx
0.0127 kg · m2
Iyy
0.0127 kg · m2
Izz
0.0238 kg · m2
Radius of UAV body
l
0.225 m
Vertical distance from propeller
plane to UAV center
d
0.05 m
© ASCE
04025131-7
J. Aerosp. Eng.
 J. Aerosp. Eng., 2026, 39(2): 04025131 
 Downloaded from ascelibrary.org by Netaji subhas university of technology on 03/15/26. Copyright ASCE. For personal use only; all rights reserved.

## Page 8

SMC controller, the SMCESO controller exhibits a substantial re-
duction in chattering at the beginning of the response, with its value
closer to that of the PID, due to the incorporation of the ESO.
The state estimation performance of the ESO in the SMCESO
controller for altitude and three attitude angles is shown in Fig. 8.
In each figure, the first subplot shows the comparison between the
estimated and actual values of the desired commands (desired alti-
tude and three desired attitude angles). The second subplot presents
the comparison of the derivatives of the desired commands, i.e., the
estimated and actual values of the vertical velocity and the three
angular velocities. The third subplot displays the disturbance esti-
mation by the ESO. It can be shown that in the initial stage, within
the first t ¼ 1 s after the command signal is given, there is a certain
deviation between the estimated and actual values, and then the es-
timated values quickly and accurately track the actual values, indi-
cating that the ESO performs well.
Fig. 6. Altitude and attitude angle tracking curves of quadrotor: (a) altitude; (b) roll angle; (c) pitch angle; and (d) yaw angle.
Fig. 7. Control inputs of quadrotor: (a) altitude; (b) roll angle; (c) pitch angle; and (d) yaw angle.
© ASCE
04025131-8
J. Aerosp. Eng.
 J. Aerosp. Eng., 2026, 39(2): 04025131 
 Downloaded from ascelibrary.org by Netaji subhas university of technology on 03/15/26. Copyright ASCE. For personal use only; all rights reserved.

## Page 9

Simulation Results with Wind Disturbances
For the simulation in this section and the experiments in the follow-
ing section considering wind disturbances, the wind sources are gen-
erated by electric fans, and the wind speed data required for the
simulation are collected using a hot-wire anemometer system,
as shown in Fig. 9. The hot-wire anemometry system is an instru-
ment used to measure fluid velocity, and the Hanghua CTA-04 hot-
wire anemometer was employed in this study. The sampling was
set to 10 s with a rate of 10,000 Hz, resulting in 1 × 105 data points
Fig. 8. State estimation of SMCESO without wind disturbances: (a) altitude; (b) roll angle; (c) pitch angle; and (d) yaw angle.
Fig. 9. Experiment: (a) wind speed measured by hot-wire anemometer system; (b) schematic diagram of the experiment; and (c) instantaneous wind
speed result.
© ASCE
04025131-9
J. Aerosp. Eng.
 J. Aerosp. Eng., 2026, 39(2): 04025131 
 Downloaded from ascelibrary.org by Netaji subhas university of technology on 03/15/26. Copyright ASCE. For personal use only; all rights reserved.

## Page 10

per set. The mean values of the collected wind speeds are 2.5, 5,
and 7.5 m=s, corresponding to the values of wind level 2–4, re-
spectively. The results in Table 3 show that the standard deviations
of the wind speed increase as the wind speed rises. For the time-
varying wind speed data at 7.5 m=s, a noticeable jump is observed
around 7 s. The performance of different controllers at this point
varies significantly. Meanwhile, the wind speed data collected
through the hot-wire system are highly accurate, allowing the sim-
ulation results to precisely display the wind disturbance rejection
performance of the controllers.
For the three controllers, simulations are performed at three
time-varying wind speeds as shown in Table 3. The wind speed
in the z direction of the ground coordinate system is fixed at
2.5 m=s, while the wind speeds in the x and y directions are 2.5,
5, and 7.5 m=s, respectively. The wind directions are along −ex,
−ey, and ez. The desired commands are as follows: the desired
height is 1 m, and the three attitude angles are ½ 0
0
0  deg. The
time-varying wind speeds shown in Fig. 9(c) are added at t ¼
10–20 s, and the wind speeds are zero at other times. The simula-
tion results are shown in Fig. 10.
Fig. 10 represents the altitude and attitude angle tracking curves
of the UAVunder different time-varying wind speeds, and the results
show that (1) for altitude tracking, the variations in horizontal wind
speed have little impact on altitude response, with the relative
tracking error remaining on the order of 10−2–10−3. (2) For roll
and pitch angles, the PID controller exhibits the largest angular er-
rors across all wind speeds, indicating that it is the most affected by
wind disturbances and has the weakest disturbance resistance, while
SMC significantly reduces angular tracking and exhibits smaller
fluctuations within t ¼ 10–20 s. For instance, at a wind speed of
7.5 m=s, as shown in Fig. 10(c), both PID and SMC exhibit similar
trends in pitch angle changes influenced by the wind speed varia-
tions shown in Fig. 9. However, the PID controller is consistently
more sensitive to fluctuations, as indicated by the large amplitude of
its angle curve. In contrast, SMC demonstrates greater stability, with
noticeably reduced angular error and fluctuation amplitude, result-
ing in an average pitch angle error around 9° for PID and 5° for
SMC. For the SMCESO controller, although the overall error is de-
creasing, its fluctuations are not as stable as those of the SMC. (3) In
terms of the performance of different controllers during wind gusts,
it can be observed in Figs. 10(c and d) that at t ¼ 17 s, there is a
significant jump in wind speed of 7.5 m=s that leads to different
responses for the three controllers. At this time, the PID exhibits
a notable abrupt change in angle, with a difference of approximately
4°, while the SMC also shows a sudden change, but it is relatively
minor, around 1°. SMCESO reduces the angular deviation in the
presence of wind disturbances; however, compared to the SMC con-
troller, it exhibits slightly larger angular fluctuations overall.
Moreover, the angle tracking performance of different control-
lers is quantitatively evaluated using three performance indicators:
the maximum value of the absolute tracking error (emax), the abso-
lute value of the average tracking error (eavg), and the standard
deviation of the tracking value (σ). The error expressions are given
by Eqs. (33)–(35)
Table 3. Results of wind speeds of electric fans
No.
Average
wind speed
(m=s)
Standard deviation
of wind speed
(m=s)
Wind level
1
2.503
1.075
Level 2
2
5.02
1.297
Level 3
3
7.506
1.519
Level 4
Fig. 10. Tracking results for different time-varying wind speeds of quadrotor: (a) altitude; (b) roll angle; (c) pitch angle; and (d) yaw angle.
© ASCE
04025131-10
J. Aerosp. Eng.
 J. Aerosp. Eng., 2026, 39(2): 04025131 
 Downloaded from ascelibrary.org by Netaji subhas university of technology on 03/15/26. Copyright ASCE. For personal use only; all rights reserved.

## Page 11

emax ¼ maxjyt −ydtj
ð33Þ
eavg ¼
PT
t¼T0ðjyt −ydtjÞ
T
ð34Þ
σ ¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
PT
t¼T0 ðjyt −ydtjÞ2
T
s
ð35Þ
where yt = actual value at time t; ydt = expected value; and T =
total time.
The results in Fig. 10 illustrate that wind disturbances have rel-
atively small effects on altitude and yaw angle; therefore, quanti-
tative analyses are performed only for the pitch and roll angles.
The indicators of the tracking results at t ¼ 10–20 s are shown in
Tables 4 and 5 and Fig. 11. The results show that (1) for all con-
trollers, the tracking errors increase with wind speeds; and (2) at the
same wind speed, the SMCESO controller exhibits the smallest
maximum and average errors, significantly lower than those of the
PID and SMC controllers. (3) Fig. 10 shows that the PID controller
exhibits more noticeable fluctuations under time-varying wind dis-
turbance, and further quantitative analyses reveal that the standard
deviations of the PID tracking results at various wind speeds are
much larger than those of SMC and SMCESO, while the difference
in standard deviations between SMC and SMCESO is relatively
small. (4) Comparing the SMC and SMCESO controllers, under
lower wind speed conditions (2.5 m=s), taking the roll angle shown
in Table 4 as an example, the results show that the standard
deviation of the roll angle for the SMC controller (0.092°) is nearly
twice that of the SMCESO controller (0.047°). As wind speed in-
creases to 5 m=s, the SMC controller still shows a larger standard
deviation (0.52° versus 0.404°), though the difference narrows. At
7.5 m=s, the standard deviation of the SMC controller increases
slightly to 0.611°, while that of the SMCESO controller rises sig-
nificantly to 1.01°, exceeding the SMC controller. These results
suggest that although the SMCESO controller significantly reduces
angular errors and improves wind disturbance rejection perfor-
mance, it may result in greater angular fluctuations than SMC under
high wind conditions, as indicated by the standard deviation.
Next, the causes of the increased fluctuations of SMCESO
under strong wind disturbances are analyzed. For traditional SMC,
the switching gain k should exceed the upper bound of the total
disturbance. As k increases, the amplitude of the switching control
action also grows, which leads to more pronounced chattering. For
SMCESO, the ESO can estimate and compensate for most disturb-
ances in real time, allowing the switching gain k to overcome only
the residual estimation error after ESO compensation. Consequently,
the switching gain k can be reduced, resulting in a smaller switch-
ing amplitude and effectively alleviating chattering. Under proper
design and tuning, SMCESO can therefore achieve superior con-
trol performance.
However, when the disturbance amplitude is large or varies rap-
idly (e.g., a wind speed of 7.5 m=s with stronger fluctuations), the
chattering in SMCESO may exceed that of the traditional SMC.
This could occur due to an insufficient ESO bandwidth, which hin-
ders its ability to promptly compensate for rapidly changing disturb-
ances, leading to increased estimation errors that may even surpass
Fig. 11. Tracking errors at different time-varying wind speeds: (a) roll angle; and (b) pitch angle.
Table 4. Performance indicators of roll angle with different wind
disturbances
Wind
speed Wz
(m=s)
Wind speeds
Wx and Wy (m=s)
Controller
emax
(degrees)
eavg
(degrees)
eσ
(degrees)
Wz ¼ 2.5 Wx ¼ 0, Wy ¼ −2.5
PID
1.403
0.765
0.247
SMC
0.58
0.32
0.092
SMCESO
0.228
0.023
0.047
Wx ¼ 0, Wy ¼ −5
PID
5.24
3.667
1.238
SMC
2.192
1.544
0.52
SMCESO
1.468
0.396
0.404
Wx ¼ 0, Wy ¼ −7.5
PID
12.129
9.526
1.466
SMC
5.47
4.23
0.611
SMCESO
3.8
1.75
1.01
Table 5. Performance indicators of pitch angle with different wind
disturbances
Wind
speed Wz
(m=s)
Wind speeds
Wx and Wy (m=s)
Controller
emax
(degrees)
eavg
(degrees)
eσ
(degrees)
Wz ¼ 2.5 Wx ¼ −2.5, Wy ¼ 0
PID
1.403
0.7656
0.247
SMC
0.557
0.3055
0.0886
SMCESO
0.22
0.022
0.046
Wx ¼ −5, Wy ¼ 0
PID
5.24
3.667
1.238
SMC
2.169
1.515
0.519
SMCESO
1.443
0.383
0.395
Wx ¼ −7.5, Wy ¼ 0
PID
12.127
9.525
1.466
SMC
5.9
4.48
0.683
SMCESO
3.942
1.751
1.045
© ASCE
04025131-11
J. Aerosp. Eng.
 J. Aerosp. Eng., 2026, 39(2): 04025131 
 Downloaded from ascelibrary.org by Netaji subhas university of technology on 03/15/26. Copyright ASCE. For personal use only; all rights reserved.

## Page 12

the original disturbance. On the other hand, if the ESO bandwidth is
too high, it becomes overly sensitive to measurement noise, amplify-
ing high-frequency noise and injecting it into the disturbance esti-
mate, which also degrades control quality. Therefore, for SMCESO
controllers, appropriate parameter tuning and coordinated design be-
tween ESO and SMC parameters are crucial for achieving optimal
control performance.
To address this issue, an adaptive ESO bandwidth can be em-
ployed to dynamically adjust the observer gain, balancing fast dis-
turbance compensation and noise robustness. Alternatively, ESO
can be combined with other disturbance observers to separately es-
timate and compensate disturbances of different frequencies, thereby
enhancing system robustness and control accuracy.
Taking the wind speed of 5 m=s as an example to compare the
control inputs of three controllers and observe the state estimation
effect of the SMCESO controller, Fig. 12 shows that (1) for the
control input of force, during the initial stage, the maximum oscil-
lation values of SMC and SMCESO are much larger, approximately
37 N, compared to 31 N for PID; and (2) for the control inputs of
moments in three directions, the frequency and amplitude of the os-
cillations of SMC and SMCESO are also significantly larger than
those of PID under wind disturbances. Specifically, the maximum
control input for PID is approximately 0.279 N·m, while both SMC
and SMCESO reach 0.357 N·m. This suggests that while SMCESO
has reduced the impact of wind disturbances, its effect on decreasing
the oscillation of SMC is not obvious.
Fig. 13 illustrates the estimation performance of the ESO for
altitude and the three attitude angles at a wind speed of 5 m=s.
The results show that (1) for altitude estimation, after an initial os-
cillation, the estimated value quickly tracks the actual altitude of
1 m and the required z-direction velocity. The initial oscillation
may be related to the ESO parameter settings, which can be further
optimized to balance the oscillation and the effects of estimation.
(2) For the three attitude angles, the ESO shows a quick response in
tracking the actual changes. The overall tracking performance is sat-
isfactory, although there is a small steady-state error between the
estimated and actual angles. For angular velocities, the actual veloc-
ities exhibit significant oscillation, while the estimated velocities
show reduced oscillation.
Experimental Studies
Introduction to Experimental Platforms
The experimental platform is shown in Fig. 14, which includes a
UAV, a test platform, a laptop (ground station), a ceiling fan, and
two electric fans. The test platform is connected to the UAV through
a spherical Cardan joint, allowing movement only in the three atti-
tude angles to ensure experimental safety. The ceiling fan, with a
diameter of 700 mm, provides a wind speed of 2.5 m=s in the ver-
tical direction. The hardware of the quadrotor is listed in Table 6.
Before starting the experiment, connect the UAV to the com-
puter via a USB cable to program the controller code. Then, use the
QGC software to calibrate the sensors of the UAV. The data logging
block is incorporated into the code, enabling automatic flight data
recording onto the UAV’s SD card, which can be retrieved and an-
alyzed on the computer after each experiment. The control algorithm
burned onto the UAV is identical to that used in the simulation, facili-
tating further comparisons between the simulation results and real
flight data.
Experimental Results and Analyses
Experimental Results without Wind Disturbances
At the beginning, the expected commands were given via a remote
controller to evaluate the tracking performance of the UAV without
Fig. 12. Control inputs of three controllers under a wind speed of 5 m=s: (a) altitude; (b) roll angle; (c) pitch angle; and (d) yaw angle.
© ASCE
04025131-12
J. Aerosp. Eng.
 J. Aerosp. Eng., 2026, 39(2): 04025131 
 Downloaded from ascelibrary.org by Netaji subhas university of technology on 03/15/26. Copyright ASCE. For personal use only; all rights reserved.

## Page 13

external wind disturbances. The tracking results for the PID, SMC,
and SMCESO controllers are shown in Figs. 15–17, respectively,
indicating that all three controllers performed well in tracking the
commands.
Experimental Results with Wind Disturbances
In the experiments, three sets of wind speeds are selected; the
z-direction wind speed is maintained at Wz ¼ 2.5 m=s, while the
horizontal wind speeds are set at Wh ¼ 2.5, 5, and 7.5 m=s, respec-
tively. The average wind speeds used in the experiment are the same
as those in the simulation. In the roll angle experiment, the direction
Fig. 13. State estimation of SMCESO under a wind speed of 5 m=s: (a) altitude; (b) roll angle; (c) pitch angle; and (d) yaw angle.
Fig. 14. Experimental platform of the quadrotor.
Table 6. System components of the quadrotor
Component
Brand
Flight controller
PIXHAWK 2.4.8
Frame
DJI F450
Motor
SUNNYSKY A2212 KV980
ESC
SkyWalker20A
Battery
LiPo 4000mAh-3S1P-11.1V-30C
Propeller
DJI 9450
Remote controller
MC6C-MINI
Receiver
MC6RE-V2
Other modules: buzzer, safety switch,
and vibration dampers
—
© ASCE
04025131-13
J. Aerosp. Eng.
 J. Aerosp. Eng., 2026, 39(2): 04025131 
 Downloaded from ascelibrary.org by Netaji subhas university of technology on 03/15/26. Copyright ASCE. For personal use only; all rights reserved.

## Page 14

of the horizontal wind speed is set as Wy ¼ −Wh and Wx ¼ 0,
whereas in the pitch angle experiment, it is set as Wx ¼ −Wh and
Wy ¼ 0. The desired roll angle and pitch angle are both set to 0°.
The fan is turned on at t ¼ 5 s during the experiments, and the wind
speed gradually increases at t ¼ 5–10 s, ultimately stabilizing. The
results of the experiments are shown in Fig. 18.
As shown in Fig. 18, the comparison of the tracking performances
of the three controllers reveals that (1) under all wind speed con-
ditions, the SMCESO controller exhibits the best wind disturbance
resistance, followed by the SMC, while the PID has the relatively
worst performance of antiwind disturbance, which is consistent with
the simulation results; and (2) as the wind speeds increase, the an-
gular deviations of all three controllers also increase. At the wind
speed of 2.5 m=s, the angular deviations of all three controllers
show almost no significant change compared to the no wind con-
dition (t ¼ 0–5 s), whereas the impacts of wind disturbances on the
UAV are more obvious at the wind speeds of 5 and 7.5 m=s. This
indicates that as wind speeds gradually increase, the differences in
Fig. 15. Command tracking results of PID controller: (a) roll angle; and (b) pitch angle.
Fig. 16. Command tracking results of SMC controller: (a) roll angle; and (b) pitch angle.
Fig. 17. Command tracking results of SMCESO controller: (a) roll angle; and (b) pitch angle.
© ASCE
04025131-14
J. Aerosp. Eng.
 J. Aerosp. Eng., 2026, 39(2): 04025131 
 Downloaded from ascelibrary.org by Netaji subhas university of technology on 03/15/26. Copyright ASCE. For personal use only; all rights reserved.

## Page 15

disturbance rejection performance among the three controllers be-
come more evident.
Comparing the performance indicators of the three controllers in
terms of roll and pitch angles under different wind disturbances
shown in Tables 7 and 8, respectively, it can be found that (1) under
all wind speed conditions, the average and maximum errors of PID
are larger than those of SMC and SMCESO controllers; and (2) ex-
cept at 2.5 m=s, the average and maximum errors of SMCESO are
smaller than those of SMC, while at 2.5 m=s, the errors of the SMC
and SMCESO controllers are similar and are both slightly lower
than those of PID. This indicates that at lower wind speeds, the wind
disturbance resistance of the three controllers does not differ sig-
nificantly; however, as the wind speed increases, the differences in
disturbance rejection performance become more pronounced, with
SMCESO consistently outperforming SMC, while PID shows rel-
atively poorer performance.
Table 9 shows the comparison of the three controllers. It can be
seen that each controller has different characteristics in terms of dis-
turbance rejection capability, computational complexity, and other
aspects. Therefore, suitable control methods can be selected for
practical applications based on specific engineering requirements.
The differences between the mean errors of the simulation and
experimental results under different wind disturbances are com-
pared in Table 10, where Wh represents the horizontal wind speed,
for the roll angle, Wh ¼ Wy; and for the pitch angle, Wh ¼ Wx.
E represents the difference of mean angular error between the sim-
ulation and the experiment, with the experimental results consis-
tently exceeding the simulation results. It shows that the differences
between the simulation and the experiment results for pitch angle
and roll angle of the PID, SMC, and SMCESO controllers do not
exceed 4°, indicating that the simulation and experimental results are
relatively consistent. Furthermore, it illustrates that the dynamic
model of the UAV considering the wind disturbances is closer to
the actual system and exhibits a high degree of reliability.
It is noted that due to differences in experimental conditions and
the simulation environment, the data results from the simulation
and experiments are not entirely identical. However, both the sim-
ulation and experimental results consistently demonstrate similar
performance trends for the three control algorithms: the SMCESO
controller exhibits the best wind disturbance rejection performance,
followed by the SMC, while the PID controller performs relatively
poorly.
Conclusions
Based on the UAV dynamic model that accounts for wind disturb-
ances established in previous work, this paper conducts a compara-
tive simulation analysis and experimental study of the antidisturbance
performances of three controllers under various time-varying wind
disturbances conditions: PID, SMC, and SMCESO control. The main
conclusions are as follows.
•
In real wind conditions, the uncertain inflow direction makes it
difficult to quantify wind effects on UAVs. The proposed quad-
rotor model addresses this by decomposing wind influence into
components parallel and perpendicular to the propeller. Compared
to vertical wind speed, horizontal wind speed has a negligible
Fig. 18. Tracking results of three controllers under different wind disturbances: (a) roll angle; and (b) pitch angle.
Table 7. Performance indicators of roll angle with different wind
disturbances
Wind
speed Wz
(m=s)
Wind speeds
Wx and Wy (m=s)
Controller
emax
(degrees)
eavg
(degrees)
Wz ¼ 2.5
Wx ¼ 0, Wy ¼ −2.5
PID
6.324
2.946
SMC
6.172
0.842
SMCESO
4.035
1.631
Wx ¼ 0, Wy ¼ −5
PID
13.269
5.918
SMC
12.721
4.151
SMCESO
4.580
0.621
Wx ¼ 0, Wy ¼ −7.5
PID
20.305
9.848
SMC
15.511
7.381
SMCESO
11.548
5.626
Table 8. Performance indicators of pitch angle with different wind
disturbances
Wind
speed Wz
(m=s)
Wind speeds
Wx and Wy (m=s)
Controller
emax
(degrees)
eavg
(degrees)
Wz ¼ 2.5
Wx ¼ −2.5, Wy ¼ 0
PID
6.052
2.345
SMC
5.578
1.131
SMCESO
5.473
1.258
Wx ¼ −5, Wy ¼ 0
PID
12.077
6.696
SMC
14.852
5.177
SMCESO
9.066
2.128
Wx ¼ −7.5, Wy ¼ 0
PID
23.215
11.797
SMC
17.374
7.207
SMCESO
11.828
3.510
© ASCE
04025131-15
J. Aerosp. Eng.
 J. Aerosp. Eng., 2026, 39(2): 04025131 
 Downloaded from ascelibrary.org by Netaji subhas university of technology on 03/15/26. Copyright ASCE. For personal use only; all rights reserved.

## Page 16

effect on the vertical thrust of the propeller. Meanwhile, the hori-
zontal wind speed primarily affects the drag moment, thereby
influencing the attitude angle of the quadrotor.
•
The variations in horizontal wind speed have minimal impact
on the altitude channel, and the relative altitude tracking errors
of the three controllers are in the range of 10−3 to 10−2. For pitch
and roll angles, as the wind speed increases, the angular tracking
errors of all controllers also increase. In addition, at higher wind
speeds, the angular differences among the controllers become
more significant. When the wind speed is low, e.g., 2.5 m=s, the
angular deviations of all three controllers are small, indicating
similar performance in disturbance resistance. However, at higher
wind speeds, e.g., 7.5 m=s, the angular deviations among the
controllers become more pronounced, highlighting clearer differ-
ences in their disturbance rejection capabilities.
•
At the same wind speed, the SMCESO controller achieves the
smallest maximum error and mean error. Both simulation and
experimental results at different time-varying wind disturbances
consistently show that the SMCESO controller, as an active anti-
disturbance controller, achieves optimal antidisturbance perfor-
mance by incorporating ESO to estimate the total disturbances
of the system in real time, followed by the SMC controller,
while the PID controller exhibits relatively poor disturbance re-
sistance performance. Additionally, the SMCESO controller has
a relatively low dependence on precise mathematical modeling,
enabling it to perform exceptionally well in complex systems
with unknown models.
•
The simulation results for pitch and roll angles under a sudden
wind disturbance of 7.5 m=s highlight the different characteris-
tics of the three controllers in disturbance rejection. The PID
controller is particularly sensitive to wind fluctuations, exhibit-
ing obvious angular variations of about 4° when the wind speed
changes. In contrast, the SMC shows better robustness, with no-
ticeably reduced angular error and a fluctuation of about 1°.
While the SMCESO significantly improves antidisturbance per-
formance, its angular fluctuations may exceed those of the SMC
controller under high wind speeds.
•
The antidisturbance experiments of the three controllers were
conducted using a physical test platform, including both linear
and nonlinear controllers, as well as active and passive control
strategies. Moreover, the consistency of data results between the
simulation and experiment further supports validation of the pro-
posed dynamic model and demonstrate its efficacy. This model
can be used for simulations to analyze the impacts of wind dis-
turbances on UAVs, further guiding the design of flight control
algorithms with stronger disturbance rejection and robustness.
•
UAVs may encounter compound disturbances such as winds,
payload variations, and sensor noise during actual flight, which
place higher demands on control performance. The introduction
of adaptive or intelligent control strategies, incorporating deep
neural networks and vision-language models, is expected to en-
hance their autonomous control capability and robustness in
complex environments.
Appendix. State-Space Representation
of the UAV Model
In Eq. (1), p ¼ ½ px
py
pz T denotes the displacement of the
quadrotor in the inertial frame, v ¼ ½ vx
vy
vz T denotes the
velocity of the quadrotor in the inertial frame, Θ ¼ ½ ϕ
θ
ψ T
denotes the Euler angles, ˙Θ ¼ ½ ˙ϕ
˙θ
˙ψ T denotes the rate of the
attitude change, and Ω ¼ ½ p
q
r T denotes the angular velocity
in the body frame.
The general form of the state-space equation for a nonlinear
system is
˙xðtÞ ¼ fðxðtÞ; uðtÞ; tÞ þ dðtÞ
ð36Þ
To establish the state-space equations of Eq. (1), the position,
velocity, attitude angles, and angular velocity are chosen as the state
variables
Table 10. Comparison of simulation and experimental results
Wind
speed Wz
(m=s)
Wind speeds
Wx and Wy
(m=s)
Controller
Eϕ
Eθ
Wz ¼ 2.5
Wh ¼ −2.5
PID
2.181
1.579
SMC
0.523
0.811
SMCESO
1.608
1.237
Wh ¼ −5
PID
2.251
3.029
SMC
2.607
3.661
SMCESO
0.225
1.745
Wh ¼ −7.5
PID
0.322
2.272
SMC
3.15
2.727
SMCESO
3.875
1.76
Table 9. Comparison of the three controllers
Controller
PID
SMC
SMCESO
Basic principle
Based on the idea of “eliminating error
through error correction”
Type of variable structure
control
Composite control system that combines
the robustness of SMC with the disturbance
estimation capability of ESO
Passive/active control strategy
Passive
Passive
Active
Linear/nonlinear controller
Linear
Nonlinear
Nonlinear
Parameter tuning
Simple
Moderately complex
Complex
Disturbance rejection
Low
Relatively high
High
Model dependency
Low
Medium
Low
Computational complexity
Low
Medium
High
Actuator demands
Low (output is continuous and smooth)
High (output has
high-frequency chattering)
Medium
Advantages
Simple structure and easy to implement
High robustness
Excellent performance in complex and
uncertain environments
Disadvantages
Limited performance for nonlinear and
complex systems
Chattering may occur
Requires tuning of many parameters
© ASCE
04025131-16
J. Aerosp. Eng.
 J. Aerosp. Eng., 2026, 39(2): 04025131 
 Downloaded from ascelibrary.org by Netaji subhas university of technology on 03/15/26. Copyright ASCE. For personal use only; all rights reserved.

## Page 17

x ¼ ½ px
py
pz
˙px
˙py
˙pz
ϕ
θ
ψ
˙ϕ
˙θ
˙ψ T
¼ ½ px
py
pz
vx
vy
vz
ϕ
θ
ψ
p
q
r T
ð37Þ
The control input u is defined as
u ¼ ½ f
τx
τ y
τ z T
ð38Þ
The disturbance d is defined as
d ¼ ½ fDx
fDy
τDx
τ Dy
τDz T
ð39Þ
Thus, the state equations of Eq. (1) can be expressed as
˙x1 ¼ x4
˙x2 ¼ x5
˙x3 ¼ x6
˙x4 ¼ −u1 −d1
m
ðcos ψ sin θ cos ϕ þ sin ψ sin ϕÞ
˙x5 ¼ −u1 −d2
m
ðsin ψ sin θ cos ϕ −cos ψ sin ϕÞ
˙x6 ¼ g −u1
m cos ϕ cos θ
˙x7 ¼ x10 ¼ p
˙x8 ¼ x11 ¼ q
˙x9 ¼ x12 ¼ r
˙x10 ¼ 1
Ixx
½ðu2 þ d3Þ þ x11x12ðIyy −IzzÞ
˙x11 ¼ 1
Iyy
½ðu3 þ d4Þ þ x10x12ðIzz −IxxÞ
˙x12 ¼ 1
Izz
½ðu4 þ d5Þ þ x10x11ðIxx −IyyÞ
ð40Þ
The output equations y can be written as
y ¼ x
ð41Þ
Data Availability Statement
Some or all data, models, or code that support the findings of this
study are available from the corresponding author upon reasonable
request.
Acknowledgments
This research has been supported by the National Natural Science
Foundation of China (No. 52076086).
Author Contributions
Le Zhou: Conceptualization; Formal analysis; Investigation; Meth-
odology; Software; Writing – original draft. Chen Xu: Conceptuali-
zation; Methodology; Supervision; Visualization; Writing – review
and editing. Fengnian Tian: Conceptualization; Methodology; Super-
vision; Validation; Writing – review and editing. Yijun Mao: Funding
acquisition; Investigation; Methodology; Supervision; Validation;
Writing – review and editing.
References
Abbas, S., S. Husain, S. Al-Wais, and A. Humaidi. 2024. “Adaptive integral
sliding mode controller (SMC) design for vehicle steer-by-wire system.”
SAE Int. J. Veh. Dyn. Stab. NVH 8 (3): 383–396. https://doi.org/10.4271
/10-08-03-0021.
Al-Dujaili, A., A. Hasan, A. Humaidi, and A. Al-Jodah. 2024. “Anti-
disturbance control design of Exoskeleton Knee robotic system for
rehabilitative care.” Heliyon 10 (9): e28911. https://doi.org/10.1016/j
.heliyon.2024.e28911.
Amin, R., A. Li, and S. Shamshirband. 2016. “A review of quadrotor UAV:
Control methodologies and performance evaluation.” Int. J. Autom.
Control 10 (2): 87–103. https://doi.org/10.1504/IJAAC.2016.076453.
Arindama. 2021. Introduction to matrix theory. Cham, Switzerland: Springer.
Ariyibi, S. O., and O. Tekinalp. 2020. “Quaternion-based nonlinear attitude
control of quadrotor formations carrying a slung load.” Aerosp. Sci.
Technol. 105 (Oct): 105995. https://doi.org/10.1016/j.ast.2020.105995.
Atif, M., R. Ahmad, W. Ahmad, L. Zhao, and J. J. P. C. Rodrigues. 2021.
“UAV-assisted wireless localization for search and rescue.” IEEE Syst. J.
15 (3): 3261–3272. https://doi.org/10.1109/JSYST.2020.3041573.
Cai, X., X. Zhu, and W. Yao. 2024. “Fixed-time trajectory tracking control
of a quadrotor UAV under time-varying wind disturbances: Theory and
experimental validation.” Meas. Sci. Technol. 35 (8): 086205. https://
doi.org/10.1088/1361-6501/ad4627.
Cai, Z., J. Lou, J. Zhao, K. Wu, N. Liu, and Y. Wang. 2019. “Quadrotor
trajectory tracking and obstacle avoidance by chaotic grey wolf
optimization-based active disturbance rejection control.” Mech. Syst.
Signal Process. 128 (Aug): 636–654. https://doi.org/10.1016/j.ymssp
.2019.03.035.
Chen, L., Z. Liu, Q. Dang, W. Zhao, and G. Wang. 2022. “Robust trajectory
tracking control for a quadrotor using recursive sliding mode control
and nonlinear extended state observer.” Aerosp. Sci. Technol. 128 (Sep):
107749. https://doi.org/10.1016/j.ast.2022.107749.
Chen, W., J. Yang, L. Guo, and S. Li. 2016. “Disturbance-observer-based
control and related methods—An overview.” IEEE Trans. Ind. Electron.
63 (2): 1083–1095. https://doi.org/10.1109/TIE.2015.2478397.
Cui, L., R. Zhang, H. Yang, and Z. Zuo. 2021. “Adaptive super-twisting
trajectory tracking control for an unmanned aerial vehicle under gust
winds.” Aerosp. Sci. Technol. 115 (Aug): 106833. https://doi.org/10
.1016/j.ast.2021.106833.
Dai, B., Y. He, G. Zhang, W. Xu, and D. Wang. 2018. “Acceleration feed-
back enhanced H∞control of unmanned aerial vehicle for wind disturb-
ance rejection.” In Proc., 2018 15th Int. Conf. on Control, Automation,
Robotics and Vision (ICARCV), 1045–1050. New York: IEEE. https://
doi.org/10.1109/ICARCV.2018.8581259.
Dalwadi, N., D. Deb, and S. Ozana. 2023. “Performance evaluation of
RW-quadrotor and Bi-quadrotor for payload delivery.” IET Intell.
Transp. Syst. 17 (11): 2221–2236. https://doi.org/10.1049/itr2.12403.
Gremillion, G. M., and J. S. Humbert. 2016. “Disturbance rejection with
distributed acceleration sensing for small unmanned aircraft systems.”
AIAA J. 53 (May): 1–14. https://doi.org/10.2514/1.J054408.
Guo, K., J. Jia, X. Yu, L. Guo, and L. Xie. 2020. “Multiple observers based
anti-disturbance control for a quadrotor UAV against payload and wind
disturbances.” Control Eng. Pract. 102 (Sep): 104560. https://doi.org
/10.1016/j.conengprac.2020.104560.
Hasan, A., A. Humaidi, A. Al-Obaidi, A. Azar, I. Ibraheem, A. Al-Dujaili,
A. Al-Mhdawi, and F. Abdulmajeed. 2023. “Fractional order extended
state observer enhances the performance of controlled tri-copter UAV
based on active disturbance rejection control.” In Mobile robot: Motion
control and path planning, 439–487. Cham, Switzerland: Springer.
https://doi.org/10.1007/978-3-031-26564-8_14.
Husain, S., A. Al-Dujaili, A. Jaber, A. Humaidi, and R. Al-Azzawi. 2024.
“Design of a robust controller based on barrier function for vehicle
steer-by-wire systems.” World Electr. Veh. J. 15 (1): 17–37. https://doi
.org/10.3390/wevj15010017.
Jiang, H., K. Chen, R. Chai, J. Yu, C. Guo, and Y. Xia. 2024. “Trajectory
planning and control of multiple quadcopters for Mars exploration.”
J. Aerosp. Eng. 37 (4): 04024038. https://doi.org/10.1061/JAEEEZ
.ASENG-5270.
© ASCE
04025131-17
J. Aerosp. Eng.
 J. Aerosp. Eng., 2026, 39(2): 04025131 
 Downloaded from ascelibrary.org by Netaji subhas university of technology on 03/15/26. Copyright ASCE. For personal use only; all rights reserved.

## Page 18

Karahan, M., and C. Kasnakoglu. 2019. “Modeling and simulation of quad-
rotor UAVusing PID controller.” In Proc., 2019 11th Int. Conf. on Elec-
tronics, Computers and Artificial Intelligence (ECAI), 1–4. New York:
IEEE. https://doi.org/10.1109/ECAI46879.2019.9042043.
Khadka, A., B. Fick, A. Afshar, M. Tavakoli, and J. Baqersad. 2020.
“Non-contact vibration monitoring of rotating wind turbines using a
semi-autonomous UAV.” Mech. Syst. Signal Process. 138 (Apr):
106446. https://doi.org/10.1016/j.ymssp.2019.106446.
Labbadi, M., K. Boudaraia, A. Elakkary, M. Djemai, and M. Cherkaoui.
2022. “A continuous nonlinear sliding mode control with fractional
operators for quadrotor UAV systems in the presence of disturbances.”
J. Aerosp. Eng. 35 (1): 04021122. https://doi.org/10.1061/(ASCE)AS
.1943-5525.0001375.
Li, B., W. Gong, Y. Yang, B. Xiao, and D. Ran. 2022a. “Appointed fixed time
observer-based sliding mode control for a quadrotor UAV under external
disturbances.” IEEE Trans. Aerosp. Electron. Syst. 58 (1): 290–303.
https://doi.org/10.1109/TAES.2021.3101562.
Li, S., Z. Sun, and M. A. Talpur. 2022b. “A finite time composite control
method for quadrotor UAV with wind disturbance rejection.” Comput.
Electr. Eng. 103 (Oct): 108299. https://doi.org/10.1016/j.compeleceng
.2022.108299.
Lopez-Sanchez, I., and J. Moreno-Valenzuela. 2023. “PID control of quad-
rotor UAVs: A survey.” Annu. Rev. Control 56 (Jan): 100900. https://doi
.org/10.1016/j.arcontrol.2023.100900.
Lotufo, M. A., L. Colangelo, C. Perez-Montenegro, E. Canuto, and
C. Novara. 2019. “UAV quadrotor attitude control: An ADRC-EMC
combined approach.” Control Eng. Pract. 84 (Mar): 13–22. https://doi
.org/10.1016/j.conengprac.2018.11.002.
Lv, T., Y. Yang, L. Chai, and Q. Li. 2019. “ESKF-based model predictive
control for a quadrotor subject to wind disturbances and measurement
noise.” In Proc., 2019 WRC Symp. on Advanced Robotics and Automa-
tion (WRC SARA), 260–265. New York: IEEE. https://doi.org/10.1109
/WRC-SARA.2019.8931803.
Mofid, O., S. Mobayen, C. Zhang, and B. Esakki. 2021. “Desired tracking
of delayed quadrotor UAV under model uncertainty and wind disturb-
ance using adaptive super-twisting terminal sliding mode control.”
ISA Trans. 123 (Apr): 455–471. https://doi.org/10.1016/j.isatra.2021
.06.002.
Rice, J. 1994. Mathematical statistics and data analysis. 3rd ed. Belmont,
CA: Duxbury Press.
Shen, J., B. Wang, B. Chen, R. Bu, and B. Jin. 2022. “Review on wind re-
sistance for quadrotor UAVs: Modeling and controller design.” Unmanned
Syst. 11 (1): 5–15. https://doi.org/10.1142/S2301385023310015.
Shen, S., and J. Xu. 2021. “Research progress in active disturbance rejec-
tion control of unmanned aerial vehicle.” [In Chinese.] J. Cent. South
Univ. 52 (4): 1197−1212. https://doi.org/10.11817/j.issn.1672-7207
.2021.04.016.
Tang, L., W. Lu, F. Gong, M. Yang, and G. Liu. 2019. “Double power
reaching law for sliding mode control of the quadrotor UAV based on
wind disturbance observation.” [In Chinese.] Flight Dyn. 37 (6): 27–33.
https://doi.org/10.13645/j.cnki.f.d.20190626.001.
Vahdanipour, M., and M. Khodabandeh. 2019. “Adaptive fractional order
sliding mode control for a quadrotor with a varying load.” Aerosp. Sci.
Technol. 86 (Mar): 737–747. https://doi.org/10.1016/j.ast.2019.01.053.
Wang, B., X. Yu, L. Mu, and Y. Zhang. 2019. “Disturbance observer-based
adaptive fault-tolerant control for a quadrotor helicopter subject to
parametric uncertainties and external disturbances.” Mech. Syst.
Signal Process. 120 (Apr): 727–743. https://doi.org/10.1016/j.ymssp
.2018.11.001.
Wang, H., N. Li, Y. Wang, and B. Su. 2021. “Backstepping sliding mode
trajectory tracking via extended state observer for quadrotors with wind
disturbance.” J. Control Autom. Syst. 19 (10): 3273–3284. https://doi
.org/10.1007/s12555-020-0673-5.
Wang, S., J. Chen, and X. He. 2022. “An adaptive composite disturbance
rejection for attitude control of the agricultural quadrotor UAV.” ISA
Trans. 129 (Oct): 564–579. https://doi.org/10.1016/j.isatra.2022.01.012.
Xia, K., W. Chung, and H. Son. 2022. “Dynamics estimator based robust
fault-tolerant control for VTOL UAVs trajectory tracking.” Mech. Syst.
Signal Process. 162 (Jan): 108062. https://doi.org/10.1016/j.ymssp
.2021.108062.
Xing, Z., Y. Zhang, and C.-Y. Su. 2023. “Active wind rejection control for a
quadrotor UAVagainst unknown winds.” IEEE Trans. Aerosp. Electron.
Syst. 59 (6): 8956–8968. https://doi.org/10.1109/TAES.2023.3315254.
Xiong, J., J. Pan, G. Chen, X. Zhang, and F. Ding. 2022. “Sliding mode
dual-channel disturbance rejection attitude control for a quadrotor.” IEEE
Trans. Ind. Electron. 69 (10): 10489–10499. https://doi.org/10.1109/TIE
.2021.3137600.
Xu, J., P. Shi, C.-C. Lim, C. Cai, and Y. Zou. 2019. “Reliable tracking
control for under-actuated quadrotors with wind disturbances.” IEEE
Trans. Syst. Man Cybern. Syst. 49 (10): 2059–2070. https://doi.org/10
.1109/TSMC.2017.2782662.
Yang, H., L. Cheng, Y. Xia, and Y. Yuan. 2018. “Active disturbance rejec-
tion attitude control for a dual closed-loop quadrotor under gust wind.”
IEEE Trans. Control Syst. Technol. 26 (4): 1400–1405. https://doi.org
/10.1109/TCST.2017.2710951.
Zeng, J., Z. Wu, M. D. Todd, and Z. Hu. 2023. “Bayes risk-based mission
planning of unmanned aerial vehicles for autonomous damage inspec-
tion.” Mech. Syst. Signal Process. 187 (Mar): 109958. https://doi.org
/10.1016/j.ymssp.2022.109958.
Zhang, J., Y. Shi, Z. Ren, and B. Wen. 2018. “Robust sliding mode control
for quadrotor UAV trajectory based on extended state observer.” [In
Chinese.] J. Chin. Inertial Technol. 26 (2): 247–254. https://doi.org/10
.13695/j.cnki.12-1222/o3.2018.02.017.
Zhao, L., L. Dai, Y. Xia, and P. Li. 2019. “Attitude control for quadrotors
subjected to wind disturbances via active disturbance rejection control
and integral sliding mode control.” Mech. Syst. Signal Process. 129 (Aug):
531–545. https://doi.org/10.1016/j.ymssp.2019.04.040.
Zhao, Z., and B. Guo. 2017. “A nonlinear extended state observer based on
fractional power functions.” Automatica 81 (July): 286–296. https://doi
.org/10.1016/j.automatica.2017.03.002.
Zhao, Z., L. Xiao, B. Jiang, and D. Cao. 2022. “Fast nonsingular terminal
sliding mode trajectory tracking control of a quadrotor UAV based
on extended state observers.” [In Chinese.] J. Control Decis. 37 (9):
2201–2210. https://doi.org/10.13195/j.kzyjc.2021.1819.
Zheng, E., J. Xiong, and J. Luo. 2014. “Second order sliding mode control
for a quadrotor UAV.” ISA Trans. 53 (4): 1350–1356. https://doi.org/10
.1016/j.isatra.2014.03.010.
Zhou, L. 2025. “Research on dynamic modeling and control algorithms of a
quadrotor UAV under wind disturbances.” [In Chinese.] Master’s thesis,
School of Aerospace Engineering, Huazhong Univ. of Science and
Technology.
© ASCE
04025131-18
J. Aerosp. Eng.
 J. Aerosp. Eng., 2026, 39(2): 04025131 
 Downloaded from ascelibrary.org by Netaji subhas university of technology on 03/15/26. Copyright ASCE. For personal use only; all rights reserved.
