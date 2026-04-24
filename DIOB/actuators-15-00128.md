# actuators-15-00128.pdf

## Page 1

Academic Editor: João Falcão
Carneiro
Received: 15 January 2026
Revised: 12 February 2026
Accepted: 17 February 2026
Published: 19 February 2026
Copyright: © 2026 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license.
Article
Adaptive Sliding Mode Control Based on a Peak-Suppression
Extended State Observer for Angle Tracking in
Steer-by-Wire Systems
Guoqing Geng 1,*
, Debang Sun 1
, Jiantao Ma 1
and Haoran Li 2
1
School of Automotive and Traffic Engineering, Jiangsu University, Zhenjiang 212013, China
2
School of Engineering Informatics and Applied Sciences, Northern Arizona University,
Flagstaff, AZ 86011, USA
*
Correspondence: ggq@ujs.edu.cn
Abstract
To address the degradation of angle tracking performance in steer-by-wire (SBW) sys-
tems caused by external disturbances and parameter uncertainties, this paper proposes
a composite control strategy integrating adaptive sliding mode control (ASMC) and a
peak-suppression extended state observer (PSESO). Firstly, a novel sliding mode reaching
law is designed, which incorporates a dynamic adaptive gain function to achieve real-time
adjustment of the control gain. This approach accelerates the reaching speed while effec-
tively mitigating chattering. Secondly, to enhance the disturbance rejection capability of the
system, a PSESO is developed to estimate the lumped disturbance in the SBW system in
real time. By dynamically adjusting the observer bandwidth, the peak phenomenon in state
estimation is suppressed, thereby avoiding saturation of the control signal. The disturbance
estimate from the PSESO is then fed forward as a compensation term into the adaptive
sliding mode (ASM) controller, forming a composite ASMC+PSESO controller that enables
active compensation and suppression of disturbances. Finally, the proposed composite
control strategy is validated through both simulations and experiments. Experimental
results demonstrate that under sinusoidal signal tracking conditions, the proposed method
reduces the maximum tracking error, the mean absolute error, and the integral absolute
error by 64.4%, 74.2%, and 73.1%, respectively, compared to traditional sliding mode con-
trol (TSMC). These results fully underscore its superiority in angle tracking control and
disturbance rejection for SBW systems.
Keywords: steer-by-wire; adaptive sliding mode control; extended state observer; angle
tracking; disturbance rejection
1. Introduction
With the rapid advancement of automotive technology, the steer-by-wire (SBW) sys-
tem, serving as a critical actuator for advanced driver-assistance systems (ADAS), has
emerged as an important research topic in the field of automotive engineering [1–3]. Unlike
conventional mechanical steering systems, the SBW system eliminates the intermediate
shaft and achieves complete mechanical decoupling between the upper and lower mod-
ules, enabling steering functionality via drive signals transmitted through communication
buses. This architecture fundamentally enhances the design flexibility and versatility of
the vehicle steering system, which not only contributes to improved handling stability and
Actuators 2026, 15, 128
https://doi.org/10.3390/act15020128

## Page 2

Actuators 2026, 15, 128
2 of 21
active safety, but also provides essential underlying support for high-precision trajectory
tracking in autonomous driving applications [4,5].
However, due to the absence of a mechanical linkage for direct coupling in SBW
systems, the angular displacement output of the steering actuator entirely relies on the
precise regulation of control algorithms [6]. High-precision tracking control of the front-
wheel steering angle is crucial for achieving superior steering performance. Its accuracy
directly determines the vehicle’s path-following capability and driving stability, particularly
under extreme operating conditions such as high-speed maneuvers, steering on low friction
coefficient road surfaces, and emergency obstacle avoidance [7]. Nevertheless, SBW systems
are susceptible to various uncertainties during the control process, including variations
in motor parameters, unmodeled dynamics, and changes in tire self-aligning torque [8].
These disturbance factors are mutually coupled, resulting in a system that exhibits strong
nonlinearity and significant disturbance characteristics, thereby constituting a complex
uncertain system. These compounded uncertainties can substantially degrade the tracking
accuracy of the front-wheel angle and the robustness of the system, potentially even
leading to instability [9,10]. Therefore, investigating and designing a control strategy with
strong disturbance rejection capabilities is of great importance for enhancing the overall
performance of SBW systems.
To address the aforementioned challenges, numerous control strategies have been
proposed by researchers, such as proportional-integral-derivative (PID) control [11,12],
model predictive control (MPC) [8,13], and sliding mode control (SMC) [14,15]. PID control
has been widely adopted in early control systems owing to its simple structure and ease of
parameter tuning. However, limited by its linear control architecture, this method struggles
to effectively handle the strong nonlinear characteristics of the system, particularly under
extreme operating conditions where tracking errors increase significantly. MPC exhibits
notable advantages in dealing with multivariable and nonlinear constraints. Nevertheless,
its performance heavily relies on the accuracy of the system model. Furthermore, the
substantial computational burden of MPC makes it difficult to meet the stringent require-
ments of real-time vehicle control. As a powerful robust control methodology, SMC was
established in the seminal works of Utkin et al. [16,17]. In comparison with other control
methods, SMC offers prominent advantages such as low dependence on model accuracy,
strong robustness, and ease of engineering implementation [18]. As a result, SMC has
become an important control methodology in SBW systems.
However, traditional sliding mode control (TSMC) also suffers from inherent limi-
tations. The discontinuous term in its control law can induce high-frequency chattering,
which not only reduces control precision but may also excite harmful mechanical vibrations,
thereby accelerating actuator wear [19]. To improve its control performance, scholars have
proposed various enhancement strategies, such as sliding mode reaching laws [20–23],
higher-order SMC [24], and terminal SMC [25]. Among these, the reaching law approach de-
signs an independent differential equation for the system’s reaching mode, directly shaping
the convergence process of the state trajectory, which effectively suppresses chattering [26].
Rohith [20] proposed a fractional-power reaching law that introduces a fractional-order
proportional term. Experimental results demonstrated that this method effectively reduces
chattering while maintaining reaching time and robustness comparable to conventional
reaching laws. Kim et al. [21] introduced a nonlinear exponential gain term related to the
sliding surface into the traditional exponential reaching law and replaced the sign function
with a saturation function to limit control input, though at the expense of convergence speed.
Xu et al. [22] developed a composite sliding mode reaching law incorporating a terminal
attractor and an adaptive function. Experimental results indicated improved dynamic
performance, albeit with increased algorithmic complexity. Zhang et al. [23] proposed
https://doi.org/10.3390/act15020128

## Page 3

Actuators 2026, 15, 128
3 of 21
an exponential function-based reaching law that effectively suppresses high-frequency
chattering. However, under extreme operating conditions, the controller’s performance
degrades, requiring parameter retuning.
The aforementioned improved SMC methods can enhance the dynamic characteristics
of the system to some extent. However, when dealing with rapidly varying and high-
amplitude compound disturbances, maintaining robustness often requires the use of large
switching gains, which may exacerbate chattering and even lead to system instability [27].
Disturbance estimation and compensation, as a means to enhance robustness, has a long
history in control theory. Early concepts like the disturbance observer (DOB) [28] laid
the groundwork. The extended state observer (ESO), a pivotal advancement formalized
by Han [29] within the active disturbance rejection control (ADRC) framework, provides
a model-free approach to estimate and cancel ‘total disturbance’. Integrating an ESO
with SMC has been recognized as an effective solution to this issue [30]. Without relying
on an accurate system model, the ESO can estimate the lumped disturbances in real
time and feed the estimated values back into the control law for compensation, thereby
enabling robust performance with relatively lower gains [31]. In recent years, ESO has been
widely applied in various control fields such as robotic systems, SBW systems, and motor
servo control due to its advantages. For instance, Zhao et al. [32] designed a nonlinear
prescribed-time ESO to estimate both the states and disturbances of a robotic system, which
achieves theoretical preset-time convergence, though its complex structure increases the
computational burden. Sun et al. [33] developed an ESO to observe the states and lumped
disturbances in permanent magnet synchronous motors (PMSM), while Sun et al. [34]
applied an ESO to estimate aperiodic disturbances in an SBW system and updated the
control law in real time, thereby improving steering angle tracking accuracy. However,
when there is a discrepancy between the initial state of the ESO and the actual initial
operating state of the system, significant transient estimation errors may occur during
the initial phase, leading to a peak phenomenon in the observed values. If such peak
values are compensated into the control system, they may exceed the physical limits of the
actuator and cause undesirable impacts. To improve disturbance estimation performance,
methods such as the uncertainty and disturbance estimator (UDE) and cascaded high-
gain observers (CHO) have been proposed. UDE actively estimates and compensates
for matched or mismatched disturbances by incorporating a filter into the control law,
effectively suppressing high-frequency disturbances and enhancing robustness [35,36].
However, UDEs are also susceptible to the initial peaking phenomenon. CHOs employ
multiple layers of observers to progressively estimate states and disturbances, which
can theoretically achieve peaking reduction through distributed gains [37]. Nevertheless,
this architecture increases the observer order and computational complexity. In the field
of soft robotics, Shao et al. [38] achieved high-precision and robust trajectory tracking
control by integrating an adaptive fractional-order sliding mode controller with a nonlinear
disturbance observer. However, the core focus of their method lies in enhancing the
dynamic regulation capability of the controller. In SBW systems, existing research has
often paid insufficient attention to the initial estimation peak phenomenon of observers.
Therefore, this paper proposes a peak-suppression ESO (PSESO), which dynamically adjusts
the observer bandwidth to effectively suppress the initial peak phenomenon, further
enhancing the control performance.
Based on the above analysis, this paper proposes a composite control strategy inte-
grating adaptive sliding mode control (ASMC) with a PSESO for angle tracking control
of SBW systems. Notably, compared with MPC [8], which requires online solution of
optimization problems, and high-order SMC [24], which often involves complex structures
and high-order state derivatives, the ASMC + PSESO composite strategy proposed in this
https://doi.org/10.3390/act15020128

## Page 4

Actuators 2026, 15, 128
4 of 21
paper features control laws and observers composed of explicit algebraic operations and
differential equation updates. With a well-defined structure and no iterative optimization
loops, it not only ensures high precision and strong robustness but also inherently features
lower computational complexity, making it more suitable for real-time critical automotive
embedded systems. The main contributions of this work are summarized as follows:
(1) A novel sliding mode reaching law is proposed. This reaching law incorporates a
dynamic adaptive gain function to achieve self-adjusting control gains based on the system
states, and utilizes a segmented function to replace the traditional switching term, thereby
accelerating convergence while effectively suppressing chattering.
(2) A PSESO is designed to estimate the lumped disturbances in real time. Through
a feedforward compensation mechanism, the angle tracking accuracy of the SBW system
is significantly improved. Moreover, a time-varying bandwidth strategy is introduced in
the PSESO to suppress the initial peak phenomenon in observation, further enhancing the
control performance.
The remainder of this paper is organized as follows. Section 2 establishes the math-
ematical model of the SBW system. Section 3 presents the design of the sliding mode
controller based on the proposed adaptive sliding mode reaching law (ASMRL). Section 4
describes the design procedure of the PSESO and develops the composite controller com-
bining ASMC and PSESO. Simulation and experimental results along with corresponding
analysis are provided in Section 5. Finally, Section 6 concludes the paper.
2. Structure and Mathematical Model of the SBW System
2.1. Architecture and Operating Principle of the SBW System
A schematic diagram of the SBW system structure is shown in Figure 1. The system
primarily consists of three core modules: the steering wheel unit, the steering actuator
unit, and the electronic control unit (ECU). Upon receiving a steering angle command from
either the driver or an autonomous driving system, the ECU processes the instruction based
on its embedded control strategy and generates corresponding motor drive signals. These
signals are transmitted via the controller area network (CAN) to the steering actuator unit,
which precisely controls the wheel steering angle through the drive motor.
Figure 1. Schematic diagram of the SBW system structure.
2.2. Mathematical Modeling of the SBW System
The mathematical model of the steering system is established as follows: [34]
J
..
δ f + B
.
δ f + Tf + Ta = κθTe
(1)
https://doi.org/10.3390/act15020128

## Page 5

Actuators 2026, 15, 128
5 of 21
where J represents the equivalent moment of inertia of the system, B denotes the equivalent
damping coefficient, κθ is the transmission ratio of the steering system, Tf signifies the
friction torque inherent in the steering system, δf indicates the steering angle, and Te refers
to the output torque of the steering motor.
Assuming uniform tire pressure distribution and a small slip angle (<4◦), the self-
aligning torque Ta can be described as: [39,40]
(
Ta = (lp + lc)Fy f
Fy f = −Cr f (β +
ωl f
V −δf )
(2)
where lp denotes the pneumatic trail, representing the distance between the tire center of
pressure and the point of application of the lateral force; lc indicates the mechanical trail,
defined as the distance from the tire center of pressure to the tire rotation point on the
ground due to the caster angle; Fyf is the lateral force of the front tire; Crf represents the
cornering stiffness of the front tire; β refers to the sideslip angle at the center of mass; ω
denotes the yaw rate; lf is the distance from the front axle to the center of mass; and V
indicates the longitudinal vehicle velocity.
The friction torque Tf can be expressed as:
Tf = Fωsgn(
.
δ f )
(3)
where Fω denotes the coulomb friction constant.
This paper employs a PMSM as the steering actuator. The electromagnetic torque
equation of the PMSM is expressed as follows:
Te = 3
2 Pnψf iq
(4)
where Pn denotes the number of pole pairs, iq represents the q-axis stator current, and ψf
signifies the permanent magnet flux linkage.
Let fd = Tf + Ta; then, Equation (1) can be rewritten as:
J
..
δ f + B
.
δ f + fd = κθTe
(5)
In practice, factors such as component aging, thermal expansion and contraction, and
continuous vibration may cause parameter variations. However, the magnitude of such
variations remains confined within a deterministic bound. The uncertainties associated
with the parameters of the SBW system can be described as follows: [10]





|J −J0| < ∆J
|B −B0| < ∆B
ψf −ψf0
 < ∆ψf
(6)
where J0, B0, and ψf0 denote the nominal values of the system parameters.
By combining Equations (4) and (5) and explicitly introducing parameter perturbation
terms, we obtain the mathematical model of the SBW system that accounts for parameter
uncertainties as:
..
δ f = (P + ∆P)iq −(Q + ∆Q)
.
δ f −(R + ∆R) fd
(7)
P =
3κθPnψf
2J
, Q = B
J , R = 1
J
(8)
where ∆J, ∆B, and ∆R represent the variations in the system parameters.
https://doi.org/10.3390/act15020128

## Page 6

Actuators 2026, 15, 128
6 of 21
Two disturbances, d1 and d2, are introduced to represent the system uncertainties,
which can be expressed as follows:
(
d1 = P(iq −i∗
q) −Q
.
δ f −R fd
d2 = ∆Piq −∆Q
.
δ f −∆R fd
(9)
Finally, Equation (7) can be rewritten as:
..
δ f = Pi∗
q + d1 + d2
(10)
Equation (10) represents a comprehensive model of the SBW system incorporating all
system uncertainties, where d1 accounts for time-varying unknown disturbances such as
external interference, friction torque, and current tracking deviations, while d2 represents
perturbations induced by variations in system parameters. In this paper, the disturbances
d1 and d2 are aggregated into a lumped disturbance, denoted as d, such that d = d1 + d2.
Assumption 1. The lumped disturbance d satisfies |d|≤D1, and its time derivative is bounded
by

.
d
 ≤D2 , where D1 and D2 are unknown positive constants.
3. Controller Design
This section begins with an analysis of the conventional sliding mode reaching law. To
address its limitations, a novel sliding mode reaching law is designed. Using Lyapunov
stability theory, the finite-time stability of the system states under this reaching law is
rigorously proven. Simulation results are provided to demonstrate its comprehensive
performance. Finally, based on the proposed reaching law, a sliding mode controller with
disturbance rejection capability is developed for angle tracking in the SBW system.
3.1. Analysis of the Traditional Exponential Reaching Law (TERL)
Among conventional reaching laws, TERL exhibits a significantly faster convergence
rate. The TERL can be expressed as:
.s = −εsgn(s) −ks
(11)
where ε and k are positive constants, s denotes the sliding surface function. The constant
rate term εsgn(s) ensures that when s approaches zero, the reaching speed remains at ε
rather than zero, thereby guaranteeing that the system states reach the sliding manifold
within a finite time.
When s > 0, the following expression can be derived from Equation (11):
.s = −ε −ks
(12)
Solving Equation (12) yields:
s(t) = [s(0) + ε
k]e−λt −ε
k
(13)
where s(0) denotes the initial condition of the sliding surface.
The time ta required to reach the sliding surface can be determined from Equation (13) as:
ta = 1
k
n
ln[s(0) + ε
k] −ln ε
k
o
(14)
As evidenced by Equation (14), the response speed and steady-state accuracy of the
TERL heavily depend on the coordinated design of parameters k and ε. It is noteworthy
https://doi.org/10.3390/act15020128

## Page 7

Actuators 2026, 15, 128
7 of 21
that due to the presence of the discontinuous function sgn(s), although increasing ε can
reduce the reaching time, an excessively high gain will excite high-frequency switching
when s approaches zero, thereby amplifying chattering and compromising the stability
of the overall control system. Furthermore, the convergence rate of the linear term ks is
constrained by its linear growth characteristic, preventing nonlinear acceleration. Moreover,
since all adjustable parameters are fixed gains, the TERL lacks adaptability to varying
external conditions. To address the above limitations of the TERL, this paper proposes an
adaptive sliding mode reaching law (ASMRL).
3.2. Design of ASMRL
The proposed ASMRL incorporates a dynamic gain term and a power term, which
substantially resolves the inherent conflict between chattering suppression and convergence
rate associated with fixed gains. The specific design process is elaborated as follows.
(1) An adaptive gain function f(s, x) is introduced into the constant rate reaching term,
The function is designed as follows:



f (s, x) =
λ
ε+(1−ε)e−δ(|s|+γ|x|)
lim
t→∞|x| = 0, λ > 0, 0 < ε < 1, γ > 0
(15)
where x represents the state variable of the system, and λ, ε, and γ are tuning parameters.
By incorporating the system state x, the function f(s, x) enables the control gain to
adapt in real time based on the system dynamics, thereby enhancing robustness against
uncertainties. When the system is far from the sliding surface, both s and x are large,
yielding f(s, x) ≈λ/ε > λ. This elevated gain provides robust control authority to ensure
rapid convergence during transient maneuvers, such as emergency steering, thereby en-
hancing the vehicle’s transient stability and response speed. As the system approaches the
equilibrium point, s and x become small, leading to f(s, x) ≈λ, which reduces the reach-
ing speed. The attenuation of the control gain suppresses the high-frequency chattering
inherent to the discontinuous switching in SMC. This suppression minimizes undesirable
mechanical vibrations in SBW actuators, leading to reduced component wear. Therefore,
the introduction of the adaptive gain function shortens the reaching time during large
deviations while simultaneously reducing high-frequency chattering.
(2) A piecewise function is defined as follows:
G(s) =
(
sgn(s), |s| ≥σ
tanh(µs), |s| > σ
(16)
where µ = 2π/σ, σ > 0 represents the thickness of the boundary layer.
The function G(s) is employed to replace the signum function sgn(s) in the exponential
reaching term. Outside the boundary layer (|s| ≥σ), the signum function is retained to
enable the system states to approach the sliding surface at the maximum rate. Inside the
boundary layer (|s| < σ), the smooth hyperbolic tangent function is adopted to replace
the discontinuous switching term, which effectively reduces the high-frequency chattering
near the equilibrium point caused by the switching behavior in TSMC. Moreover, owing
to its smoothness, this function inherently filters out high-frequency noise in disturbance
rejection, preventing the amplification of disturbances and thereby further enhancing
the robustness of the overall control system. Therefore, compared with SMC laws using
only tanh(s) or only sgn(s), the introduction of the piecewise function further shortens the
reaching time while effectively mitigating chattering.
(3) A power function term |x|η is introduced, where η is a design parameter to be
determined and satisfies η > 0. When the system state is far from the sliding surface,
https://doi.org/10.3390/act15020128

## Page 8

Actuators 2026, 15, 128
8 of 21
the power term provides stronger nonlinear convergence rates, overcoming the speed
limitation of traditional linear terms. As the system state approaches the sliding surface, the
influence of the power term diminishes, leading to reduced reaching speed and chattering,
and ultimately converging to zero. Thus, chattering is suppressed without sacrificing the
reaching speed.
Finally, the ASMRL is proposed as follows:
.s = −f (s, x)G(s) −k|x|ηs
(17)
where η > 0, k > 0.
To verify the stability of the proposed ASMRL, consider the actual reaching dynamics
in the presence of d:
.s = −f (s, x)G(s) −k|x|ηs + d
(18)
A Lyapunov function candidate is chosen as V = s2/2. Its time derivative along the
system trajectories is:
.
V = s
.s = −s f (s, x)G(s) −k|x|ηs2 + sd
(19)
When |s| ≥σ, G(s) = sgn(s), so −sf(s, x)sgn(s) = −f(s, x)|s|, from the definition
of the adaptive gain function in (15), it follows that f(s, x) ≥λ. Substituting this bound
and applying the disturbance bound |d| ≤D1, we obtain
.
V ≤−λ|s| −k|x|ηs2 + |s|D1. By
selecting λ > D1,
.
V ≤0 holds. When |s| < σ, G(s) = tanh(µs) and f(s, x) = λ. Using the
inequality tanh(µs) ≥µ2s2/(1 + µσ), which holds for |s| < σ, and again invoking the
disturbance bound, leads to
.
V ≤−λ µ2s2
1 + µσ −k|x|ηs2 + |s|D1
(20)
Since |s| < σ, the term |s|D1 can be conservatively bounded as |s|D1 < (D/σ)s2.
Consequently,
.
V ≤−(λ
µ2
1 + µσ −D1
σ ) −k|x|ηs2
(21)
To maintain
.
V ≤0,the parameters must satisfy λµ2/(1+µσ) > D1/σ. Therefore, for all
s ̸= 0,
.
V ≤0, and
.
V = 0 if and only if s = 0. The proposed ASMRL satisfies the sliding mode
reaching condition in the presence of bounded disturbances and parameter uncertainties.
To evaluate the performance of the ASMRL, the state equation of a controllable system
is given as follows:
..
θ(t) = −f (θ, t) + hu(t) + d(t)
(22)
where θ represents the angular signal, f (θ, t) = 25
.
θ, u(t) is the control input, d(t) = 15sin(πt)
denotes the external disturbance, and h = 133 is the system gain.
The desired angular signal θd is set to sin(t), and the control error is defined as
e = θd −θ. The sliding surface function is selected as follows:
s =
.e + ce
(23)
where c is the sliding surface coefficient, satisfying c > 0.
By integrating Equations (17), (22) and (23), the ASMRL-based sliding mode controller
can be synthesized as follows:
u = 1
h( f (s, x)G(s) + k|x|ηs + c
.e +
..
θd + f (θ, t))
(24)
https://doi.org/10.3390/act15020128

## Page 9

Actuators 2026, 15, 128
9 of 21
A simulation model of the corresponding system was developed using MAT-
LAB/Simulink (R2024b) to compare the control performance between the TERL and the
proposed ASMRL. The control parameters were configured as follows: c = 25, λ = 70, k = 15,
ε = 0.3, δ = 2, η = 1.6, γ = 5, σ = 0.2. The initial state of the controlled system was set to
x = [x1, x2] = [−2, −2]. The simulation results are shown in Figure 2.
 
 
(a) 
(b) 
 
 
(c) 
(d) 
Figure 2. Comparison of the control performance: (a) tracking performance; (b) tracking error;
(c) performance during the reaching phase; (d) control signal.
As observed from Figure 2a,b, when the initial state of the system significantly deviates
from the given reference signal and in the presence of external disturbances, the proposed
ASMRL achieves faster tracking of the reference signal and exhibits a smaller steady-state
error compared to the TERL. Figure 2c demonstrates that the ASMRL effectively shortens
the reaching time. Furthermore, it can be seen from Figure 2d that the control signal
generated by the ASMRL is smoother, effectively suppressing chattering. Therefore, the
proposed ASMRL successfully resolves the inherent conflict between reaching speed and
chattering in the system.
3.3. Design of an Angle Tracking Controller Based on ASMC
The tracking error for the front-wheel steering angle is defined as follows:
eδ = δ∗
f −δf
(25)
where δ∗
f denotes the reference steering angle and δf represents the actual steering angle.
https://doi.org/10.3390/act15020128

## Page 10

Actuators 2026, 15, 128
10 of 21
The first and second derivatives of the front wheel steering angle tracking error are
given as follows:
.eδ =
.
δ
∗
f −
.
δ f
(26)
..eδ =
..
δ
∗
f −
..
δ f
(27)
Combining Equations (10) and (27), it can be concluded that:
..eδ =
..
δ
∗
f −Pi∗
q −d
(28)
The design of the ASMC involves two key steps: the construction of an appropriate
sliding surface, followed by the formulation of the control output utilizing the designed
sliding mode reaching law.
The sliding surface function is designed as:
s = ceδ +
.eδ
(29)
The time derivative of the sliding surface function is given by:
.s = c
.eδ +
..eδ
(30)
Combining the ASMRL (17) with Equations (28) and (30), the control output of the
ASMC-based angle tracking controller for the SBW system can be obtained as:
i∗
q = 1
P(c
.eδ +
..
δ f −d + f (s, x)G(s) + k|x|ηs)
(31)
Figure 3 shows the block diagram of the proposed adaptive sliding mode (ASM) controller.
 
Figure 3. Block diagram of the proposed ASM controller structure.
Compared with the traditional sliding mode controller, the proposed method can
reduce system chattering and improve the dynamic performance of the SBW system.
However, the presence of lumped disturbance d in (31) may introduce deviations in the
control signal. This implies that a larger control gain must be selected to compensate for
these deviations, which in turn exacerbates system chattering and may compromise the
steering angle tracking accuracy of the SBW system. Therefore, further improvements to
the controller will be presented in the next section.
4. Design of an ASMC and PSESO Integrated Controller
As mentioned earlier, the presence of unknown disturbances and parametric uncer-
tainties may lead to degradation in control performance. In this section, a PSESO is further
https://doi.org/10.3390/act15020128

## Page 11

Actuators 2026, 15, 128
11 of 21
constructed to estimate these unknown disturbances and parametric uncertainties. The esti-
mated values are then incorporated as a feedforward compensation term into Equation (31),
thereby enhancing the angle tracking accuracy of the SBW system.
4.1. Analysis of ESO
As presented in Section 2.2, the lumped disturbance d is expressed as d =d1 + d2. The
system dynamics (10) can be rewritten as:
..
δ f = Pi∗
q + d
(32)
Based on assumption 1, the lumped disturbance d is extended as an additional state
variable x3, while the system control input and output are the q-axis current i∗
q and the
front-wheel steering angle δf, respectively. Let x1 = δf , x2 =
.
δ f , x3 = d, then Equation (32)
can be rewritten as the following extended system:





.x1 = x2
.x2 = Pi∗
q + d
.x3 =
.
d
(33)
Based on Equation (33), an ESO is constructed as follows:





.z1 = ˆx2 −β1(z1 −x1)
.z2 = ˆx3 + Pi∗
q −β2(z1 −x1)
.z3 = −β3(z1 −x1)
(34)
where zi (i = 1, 2, 3) are the estimated values of xi. β1, β2, and β3 are the observer gains to
be designed.
Let ei = zi −xi (i = 1, 2, 3), which represents the estimation error of the ESO. The
vector differential equation of the estimation error system can be expressed as:
.ei = Aeei + L
(35)
where ei =


e1
e2
e3

, Ae =


−β1
1
0
−β2
0
1
−β3
0
0

is a Hurwitz matrix, L =


0
0
.
d

.
The characteristic polynomial can be derived from Equation (35) as follows:
f (λ) = λ3 + β1λ2 + β2λ + β3 = (λ + ω0)3
(36)
where ω0 denotes the bandwidth of the ESO. The gains of the ESO (34) are designed as
β1 = 3ω0, β2 = 3ω2
0, β3 = ω3
0.
However, if the initial estimates of the ESO (34) significantly deviate from the actual
initial states of the system, the high gains may induce a large and rapid peak in the
estimation. This peak, when directly applied to the control system, may lead to control
signal saturation and cause undesired actuator stress.
4.2. Design of PSESO
To address the issue mentioned above, a PSESO is constructed based on (34) as follows:





.
ˆx1 = ˆx2 −τ1( ˆx1 −x1)
.
ˆx2 = ˆx3 + Pi∗
q −τ2( ˆx1 −x1)
.
ˆx3 = −τ3( ˆx1 −x1)
(37)
https://doi.org/10.3390/act15020128

## Page 12

Actuators 2026, 15, 128
12 of 21
where ˆxi (i = 1, 2, 3) represent the estimated state values. The time-varying gains τi
are expressed as τ1 = 3ϖ(t), τ2 = 3ϖ2(t), τ3 = ϖ3(t), respectively. The time-varying
bandwidth ϖ(t) is generated by a second-order Butterworth filter [41], with Equation (38)
serving as its input signal. The switching instant was determined through extensive
simulation studies, ensuring that the transition is completed within the typical dynamic
response period of the SBW system. The Butterworth filter is chosen for its maximally
flat magnitude response in the passband, ensuring a smooth transition of the bandwidth
during the switching phase and avoiding additional observation noise or oscillation due to
abrupt bandwidth changes.
ω0(t) =
(
ω∗
0, t ≤0.3s
3ω∗
0, t > 0.3s
(38)
where ω∗
0 are parameters to be designed.
As indicated in Equation (38), during the initial phase (t ≤0.3s), ω0(t) remains rela-
tively small. After a certain period (t > 0.3s), it gradually increases until it converges to
3ω∗
0.This approach reduces the estimation peak caused by high gains without compromis-
ing observation accuracy.
Theoretically, the bandwidth of the ESO determines its trade-off between disturbance
tracking speed and high-frequency noise suppression. A higher bandwidth results in faster
disturbance estimation and reduced steady-state phase lag, but also amplifies measurement
noise. After careful consideration, selecting ω0* = 50 achieves a favorable compromise
between suppressing the initial peak and maintaining satisfactory estimation accuracy.
To verify the stability of the PSESO, the error vector of the PSESO is first defined
as follows:
Γ = [ρ1, ρ2, ρ3]T = [ ˆx1 −x1, ˆx2 −x2, ˆx3 −x3]T
(39)
Combining Equations (33) and (37) yields:
.
Γ = BeΓ + H
(40)
where Be =


−τ1
1
0
−τ2
0
1
−τ3
0
0

is a Hurwitz matrix, H =


0
0
.
d

.
From Equation (40), it can be obtained that:
Γ =
Z t
t0
e(t−υ)Be H(υ)dυ + e(t−t0)BeΓ(t0)
(41)
where t ≥t0, with t0 being the initial time. The term e(t−t0)Be satisfies the following relationship:
e(t−t0)Be
 ≤ζe−ρ(t−t0)
(42)
where ζ > 0, ρ = nmin|Reκ(Be)| = nω∗
0, n is a constant lying between 0 and 1. Then, the
following relationship holds for Equation (41), which serves as the stability condition for
the PSESO:
∥Γ∥≤
ζ
nω∗
0
sup
t0≤υ≤t
∥H(υ)∥+ ζe−nω∗
0(t−t0)∥Γ(t0)∥
(43)
Based on the assumptions in the preceding text,
.
d is bounded. Consequently, the initial
estimation error ∥Γ(t0)∥of the PSESO is bounded, and thus the term ζe−nω∗
0(t−t0)∥Γ(t0)∥
will eventually converge to zero. Moreover, the upper bound of ∥H(υ)∥is a small positive
constant. Therefore, the convergence speed of ∥Γ∥primarily depends on the adjustment of
https://doi.org/10.3390/act15020128

## Page 13

Actuators 2026, 15, 128
13 of 21
the parameter ω∗
0. A larger value of ω∗
0 leads to a shorter convergence time to zero and a
smaller steady-state error. Based on the above analysis, the disturbance estimation error of
the PSESO is bounded, indicating that the system achieves finite-time stability.
To validate the performance of the PSESO, consider the following plant:





.x1 = x2
.x2 = h0u0(t) + d0(t)
.x3 =
.
d0(t)
(44)
where h0 = 2 is the control input gain, u0(t) = 0.8sin(2πt) is the control input, and
d0(t) = 2 + 1.2sin(t) represents the external disturbance.
A corresponding simulation model was developed using MATLAB/Simulink, and a
comparison was conducted with a traditional extended state observer (TESO) employing
fixed bandwidth. The initial states of the plant were set to x1(0) = 0.5, x2(0) = x3(0) = 0, while
the initial states of both observers were set to zero to create an initial deviation. Figure 4
shows the comparative simulation results of the PSESO and the TESO. As observed in
Figure 4a,b, when the initial values of the observers deviate significantly from the actual
initial states of the system, the PSESO effectively suppresses the peak phenomenon and ex-
hibits a faster response speed, thereby avoiding control signal saturation and demonstrating
greater suitability for SBW systems.
 
 
(a) 
(b) 
Figure 4. Performance comparison between PSESO and TESO: (a) disturbance estimation; (b) estima-
tion error.
4.3. PSESO-Based Composite Controller
Combining the ASMRL with the PSESO, the proposed angle tracking controller for
the SBW system can be constructed as follows:
i∗
q = 1
P(c
.eδ +
..
δ f −ˆx3 + f (s, x)G(s) + k|x|ηs)
(45)
where ˆx3 is the estimated value of d provided by the PSESO.
Figure 5 presents the control block diagram of the proposed PSESO-based ASM
controller designed for angle tracking control in the SBW system.
https://doi.org/10.3390/act15020128

## Page 14

Actuators 2026, 15, 128
14 of 21
 
Figure 5. Block diagram of the proposed PSESO-based ASM controller architecture.
5. Simulation and Experimental Validation
To further validate the effectiveness of the proposed composite control algorithm for
angle tracking control in the SBW system, comparative analyses are conducted in both
simulation environments and an SBW hardware-in-the-loop (HIL) test bench. The proposed
PSESO-based ASM controller is compared with both the standard ASM controller and a
traditional sliding mode controller. The control performance is comprehensively evaluated
using multiple performance metrics.
5.1. Simulation Validation
The controller parameters were initially set based on the system model and empirical
guidelines. They were then adjusted and optimized through simulations, guided by key
performance metrics as detailed later in this section. The final controller parameters were
configured as follows: c = 20, λ = 30, k = 12, ε = 0.2, δ = 2, η = 1.6, γ = 5, σ = 0.2, ω∗
0 = 50. The
relevant parameters of the SBW system are listed in Table 1. Three controllers, namely the
proposed method (ASMC + PSESO), the standard ASMC, and the TSMC, were tested under
identical simulation environments and system parameters to ensure a fair comparison.
All controller parameters were repeatedly optimized and tuned through experimentation
to guarantee optimal performance. To comprehensively evaluate the superiority of the
proposed method for angle tracking control in the SBW system, simulations were conducted
under two typical test conditions.
Table 1. Parameters of the SBW system.
Parameters
Symbol
Value
Equivalent moment of inertia
J
3.6 kg·m2
Equivalent damping coefficient
B
12.9 Nms/rad
Transmission ratio
κθ
18
Pneumatic trail
lp
0.028 m
Mechanical trail
lc
0.04 m
Number of motor pole pairs
Pn
4
Permanent magnet flux linkage
ψf
0.05 Wb
Vehicle velocity
V
20 m/s
Distance from front axle to center of gravity
lf
1.12m
To provide a more intuitive comparison of the control performance of the three meth-
ods, this study further employed quantitative analysis. Specific performance evalua-
tion metrics included the maximum error (MAX = max(|eδ|), the mean absolute error
https://doi.org/10.3390/act15020128

## Page 15

Actuators 2026, 15, 128
15 of 21
(MAE = 1
n
n
∑
i=1
|eδ(i)|), where n denotes the number of samples), the integral of absolute error
(IAE = R t
0 |eδ(τ)|dτ), and the rise time (RT, defined as the time required for the step response
to increase from 10% to 90% of its steady-state value).
Case 1: sinusoidal signal. To validate the tracking performance of the proposed
method under continuously varying steering angle commands, a sinusoidal signal was
employed as the desired angle reference, set as δ∗
f = 0.4 sin t. The simulation time was set
to 30 s. Figure 6 shows the simulation results under the sinusoidal reference.
 
 
 
(a) 
(b) 
(c) 
Figure 6. Simulation results under sinusoidal signal: (a) angle tracking curve; (b) tracking error curve;
(c) motor torque curve.
As observed in Figure 6a, all three controllers exhibit certain overshoot at the peak
values. Among them, the ASMC + PSESO controller achieves the highest tracking accuracy
and stability. The ASMC controller, lacking disturbance estimation and compensation,
performs slightly worse than ASMC + PSESO but still outperforms the TSMC, further
verifying the effectiveness of the proposed ASMRL.
From Figure 6b, it can be seen that the composite ASMC + PSESO method yields
the smallest tracking error with minimal fluctuation. The ASMC method ranks second,
while the TSMC shows significantly larger errors, indicating its inferior performance under
continuously varying steering conditions.
As illustrated in Figure 6c, the torque output of ASMC + PSESO is smooth with
negligible chattering, which is beneficial for practical actuator application. In contrast, the
TSMC exhibits noticeable chattering. This demonstrates the strong disturbance rejection
and control stability of the proposed method.
Figure 7 and Table 2 summarize the tracking error metrics of the three control methods.
Compared to ASMC and TSMC, the ASMC + PSESO approach achieves smaller values in
MAX, MAE, and IAE. Specifically, the MAE of ASMC + PSESO is reduced by 53.8% and
73.1%, and the IAE is reduced by 54.4% and 73.5%, respectively, confirming the superiority
of the proposed method.
Table 2. Tracking error metrics under sinusoidal signal.
Controllers
MAX
MAE
IAE
ASMC + PSESO
0.0041
0.0018
5.35
ASMC
0.0061
0.0039
11.72
TSMC
0.0124
0.0067
20.17
https://doi.org/10.3390/act15020128

## Page 16

Actuators 2026, 15, 128
16 of 21
 
Figure 7. Comparison of tracking error metrics under sinusoidal signal.
The above simulation results indicate that the proposed method can achieve high-
precision tracking of steering commands with excellent anti-interference performance,
making it more suitable for SBW systems.
Case 2: step signal. The step signal simulates sudden steering commands issued by the
driver or autonomous driving system in scenarios such as emergency obstacle avoidance
and rapid lane changes. A step signal with an amplitude of 0.4 rad was used to evaluate
the transient tracking performance of the proposed method. The simulation time was set to
15 s. Figure 8 shows the simulation results under the step signal.
 
 
 
(a) 
(b) 
(c) 
Figure 8. Simulation results under step signal: (a) Angle tracking curve; (b) Tracking error curve;
(c) Motor torque curve.
As observed in Figure 8a,b, compared to ASMC and TSMC, the ASMC + PSESO
method tracks the reference value more rapidly and smoothly with almost no overshoot. In
contrast, due to the lack of disturbance compensation, both ASMC and TSMC exhibit minor
fluctuations near the steady-state value. These results demonstrate the strong disturbance
rejection and fast response of the proposed method.
From Figure 8c, it can be seen that in the presence of disturbances, the torque output
of ASMC+PSESO remains smoother, further confirming its anti-interference capability. Ad-
ditionally, while significant chattering is observed in TSMC, the ASMC + PSESO approach
maintains excellent control smoothness.
Figure 9 and Table 3 provide a comparison of the tracking error metrics for the three
control methods. Compared to ASMC and TSMC, the proposed method reduces the rise
time by 52.9% and 63.6%, the MAE by 81.5% and 86%, and the IAE by 61.2% and 70.9%,
respectively. These results validate the outstanding performance of the proposed method
in tracking step-type steering angle commands.
https://doi.org/10.3390/act15020128

## Page 17

Actuators 2026, 15, 128
17 of 21
 
Figure 9. Comparison of tracking error metrics under step signal.
Table 3. Tracking error metrics under step signal.
Controllers
RT
MAE
IAE
ASMC + PSESO
0.08
0.0017
5.22
ASMC
0.17
0.0092
13.78
TSMC
0.22
0.0122
28.39
In summary, the proposed PSESO-based ASM controller exhibits superior control
performance and achieves high-precision angle tracking in the SBW system.
5.2. Experimental Validation
To further validate the effectiveness of the proposed method, a HIL test bench for
the SBW system was developed, and relevant tests were conducted. The configured SBW
HIL test bench, as shown in Figure 10, primarily consists of an operation console, an
SBW actuator, a power distribution cabinet, a prototype control system, and a software
platform. The operation console comprises an upper computer equipped with a 13th Gen
Intel Core i7-13700KF processor (3.4 GHz), 32 GB of baseband RAM, and an NVIDIA
GeForce RTX 4070 graphics card. This setup provides substantial computational power
for algorithm development, real-time simulation interfacing, and data visualization. The
prototype control system is implemented based on rapid control prototyping (RCP). The
RCP hardware is built around a dedicated microprocessor and its peripheral circuitry,
housed in a dedicated enclosure. It features multiple analog-to-digital (A/D) and digital
input/output (I/O) channels to interface with sensors and actuators. The system sampling
frequency is set to 1 kHz. The power distribution cabinet supplies energy to the entire HIL
test bench. A servo-electric cylinder is used to simulate the steering resistance torque. The
HIL test bench adopts a modular design, allowing each module to operate independently
or be flexibly integrated, with real-time adjustment and monitoring of key parameters.
Various sensors are integrated into the test bench for real-time data acquisition of relevant
parameters. The steering angle is measured by a 17-bit photoelectric encoder, which
provides high-precision angular position feedback. Communication between modules is
achieved via CAN bus.
A serpentine path steering test was carried out on the HIL test bench to simulate
repeated obstacle avoidance scenarios in real vehicle operation. A sinusoidal signal was
used as the desired angle command. The parameters of the SBW system and the controllers
remained the same as those in the simulation. The test duration was 30 s. Figure 11 shows
the comparative control performance under the serpentine path.
https://doi.org/10.3390/act15020128

## Page 18

Actuators 2026, 15, 128
18 of 21
 
Figure 10. HIL test bench of the SBW system.
 
 
 
(a) 
(b) 
(c) 
Figure 11. Experimental results of angle tracking under serpentine path: (a) tracking curve; (b) Track-
ing error curve; (c) motor torque curve.
As observed in Figure 11a,b, the angle tracking accuracy of ASMC + PSESO is sig-
nificantly higher than that of ASMC and TSMC, and it reaches the steady state more
quickly. Compared with TSMC, ASMC reduces the tracking error, further verifying the
control performance of the proposed ASMRL. Meanwhile, the presence of disturbances
leads to a decrease in tracking accuracy. Thanks to the integration of PSESO, the control
system is compensated effectively. From Figure 11c, it can be seen that ASMC + PSESO
achieves lower torque fluctuation compared to the other two methods, effectively reducing
chattering. The experimental results demonstrate that the proposed method significantly
improves the dynamic performance of the SBW system.
The MAX, MAE, and IAE values of the tracking errors were further calculated, and
the results are summarized in Table 4. A bar chart based on these results is shown in
Figure 12. It can be observed that all three error metrics of ASMC + PSESO are superior
to those of ASMC and TSMC. Specifically, the proposed ASMC + PSESO method reduces
the MAX by 40.3% and 64.4%, the MAE by 53.4% and 74.2%, and the IAE by 52.9% and
73.1%, respectively. The experimental results confirm that the proposed PSESO-based
ASM controller exhibits excellent control performance and further enhances the dynamic
characteristics of the SBW system.
https://doi.org/10.3390/act15020128

## Page 19

Actuators 2026, 15, 128
19 of 21
Table 4. Tracking error metrics under serpentine path.
Controllers
MAX
MAE
IAE
ASMC + PSESO
0.0225
0.0041
12.47
ASMC
0.0377
0.0088
26.46
TSMC
0.0632
0.0159
46.28
 
Figure 12. Comparison of tracking error metrics under serpentine path.
6. Conclusions
To address the angle tracking control problem of SBW systems under external dis-
turbances and parameter uncertainties, this paper proposed a composite control strategy
integrating adaptive ASMC with a PSESO. To overcome the inherent conflict between chat-
tering and reaching speed in TSMC, a novel ASMRL was designed. By incorporating an
adaptive gain function and a piecewise function, the ASMRL enhances the response speed
of the control system and reduces chattering. Furthermore, a PSESO with time-varying
bandwidth design was proposed to accurately estimate the lumped disturbance while
suppressing the initial peak phenomenon. A feedforward compensation mechanism was in-
troduced to further improve the angle tracking accuracy. Simulation and HIL experimental
results demonstrate that the proposed method outperforms TSMC in both tracking accuracy
and disturbance rejection capability. It effectively reduces steady-state error and chattering
amplitude, thereby significantly improving the angle tracking performance of the SBW
system. These improvements contribute to enhanced path-following capability and driving
stability, which are critical for vehicle safety. In future work, a systematic comparative
evaluation will be performed against representative UDE and CHO, to further validate
the superiority of the proposed PSESO in terms of peak suppression and computational
efficiency. Moreover, extensions to integrated vehicle control systems and fault-tolerant
control in the presence of sensor or actuator faults will be explored to improve the practical
applicability and functional safety of the proposed control scheme.
Author Contributions: Conceptualization, G.G.; Methodology, G.G. and D.S.; software, J.M.; valida-
tion, G.G., D.S., J.M. and H.L.; formal analysis, D.S.; investigation, G.G. and D.S.; resources, G.G.;
data curation, D.S. and J.M.; writing—original draft, D.S.; writing—review and editing, D.S., J.M.
and H.L.; visualization, D.S. and H.L.; supervision, G.G. All authors have read and agreed to the
published version of the manuscript.
Funding: This research received no external funding.
Data Availability Statement: The original contributions presented in this study are included in the
article. Further inquiries can be directed to the corresponding author.
https://doi.org/10.3390/act15020128

## Page 20

Actuators 2026, 15, 128
20 of 21
Acknowledgments: We would like to express their sincere gratitude to the Laboratory of Jiangsu
University for providing an excellent research environment and advanced facilities. Special thanks
are extended to Guoqing Geng for his insightful guidance and critical discussion throughout this
study, which were instrumental in the completion of this work.
Conflicts of Interest: The authors declare no conflicts of interest.
References
1.
Yang, C.; Gao, Y.; Wang, W.; Zhang, Y.; Li, Y.; Wang, X.; Zhao, X. A Synergistic Predictive Fusion Control Method and Application
for Steering Feel Feedback of Steer-by-Wire System. IEEE Trans. Transp. Electrific. 2023, 9, 293–310. [CrossRef]
2.
Zhou, X.; Liu, J.; Wang, C.; Xu, K.; Zhao, W. Tracking and Synchronization Control of the 4WISBW System Considering Uncertain
Network Communication Delay. IEEE Trans. Ind. Inf. 2025, 21, 8913–8924. [CrossRef]
3.
Wang, Y.; Liu, Y.; Wang, Y.; Chai, T. Neural Output Feedback Control of Automobile Steer-by-Wire System With Predefined
Performance and Composite Learning. IEEE Trans. Veh. Technol. 2023, 72, 5906–5921. [CrossRef]
4.
Yang, H.; Liu, W.; Chen, L.; Yu, F. An Adaptive Hierarchical Control Approach of Vehicle Handling Stability Improvement Based
on Steer-by-Wire Systems. Mechatronics 2021, 77, 102583. [CrossRef]
5.
Zou, S.; Zhao, W.; Wang, C.; Liang, W.; Chen, F. Tracking and Synchronization Control Strategy of Vehicle Dual-Motor Steer-by-
Wire System via Active Disturbance Rejection Control. IEEE/ASME Trans. Mechatron. 2023, 28, 92–103. [CrossRef]
6.
Wu, X.; Zhang, M.; Xu, M. Active Tracking Control for Steer-by-Wire System With Disturbance Observer. IEEE Trans. Veh. Technol.
2019, 68, 5483–5493. [CrossRef]
7.
Sun, Z.; Zheng, J.; Man, Z.; Wang, H. Robust Control of a Vehicle Steer-by-Wire System Using Adaptive Sliding Mode. IEEE Trans.
Ind. Electron. 2015, 63, 2251–2262. [CrossRef]
8.
Xu, Z.; Shi, Q.; Wei, Y.; Wang, M.; Guo, C.; He, L. A Predictive Sliding Control Algorithm and Application to Angle Following of
Steer-by-Wire. IEEE Trans. Syst. Man Cybern Syst. 2025, 55, 2670–2680. [CrossRef]
9.
Xu, K.; Liang, W.; Zhao, W.; Wang, C.; Zou, S.; Zhou, X. Vehicle Stability and Synchronization Control of Dual-Motor Steer-by-Wire
System Considering Multiple Uncertainties. IEEE Trans. Transp. Electrific. 2024, 10, 3092–3104. [CrossRef]
10.
Gao, Y.; Wang, W.; Yang, C.; Zhang, Y.; Qie, T.; Ma, T. A New Reaching Law for Anti-Disturbance Sliding Mode Control of
Steer-by-Wire System. IEEE Trans. Veh. Technol. 2024, 74, 4064–4075. [CrossRef]
11.
Jin, K.; Xiao, P.; Yang, D.; Fang, Z.; Zhang, R.; Yang, A. Research on Steering-by-Wire System Motor Control Based on an Improved
Sparrow Search Proportional–Integral–Derivative Algorithm. Electronics 2024, 13, 4553. [CrossRef]
12.
Guo, C.-C.; Wu, C.-S.; He, D.-G. Adaptive Fractional Order PID Controller for Angle Tracking in Steer-By-Wire System. J. Chin.
Soc. Mech. Eng. 2024, 45, 177–186.
13.
He, L.; Xu, Z.; Guo, C.; Huang, C.; Zheng, X.; Shi, Q. A Model Predictive Backstepping Control Approach for Angle Tracking of
Steer-by-Wire System. Automot. Innov. 2024, 7, 613–626. [CrossRef]
14.
Zou, S.; Zhao, W.; Wang, C. Tracking and Synchronization Control Strategy of Vehicle Dual-Motor Steer-by-Wire System via
Super-Twisting SOSMC and MDCS. Mech. Syst. Signal Process. 2023, 183, 109638. [CrossRef]
15.
Yang, J.; Yu, Y.; Zeng, D.; Hu, Y.; Liu, J.; Liu, K.; Carbone, G.; Luo, S.; Zhu, X. An Adaptive Sliding Mode Fault-Tolerant Control of
Variable Speed Reaching Law for Steer-by-Wire Systems. Sci. Rep. 2025, 15, 12846. [CrossRef]
16.
Utkin, V. Variable Structure Systems with Sliding Modes. IEEE Trans. Automat. Contr. 1977, 22, 212–222. [CrossRef]
17.
Utkin, V.I. Sliding Mode Control Design Principles and Applications to Electric Drives. IEEE Trans. Ind. Electron. 1993, 40, 23–36.
[CrossRef]
18.
Rodriguez, J.; Lechappe, V.; Chesne, S. New Methodology for Adaptive Sliding Mode Control with Self-Tuning Threshold Based
on Chattering Detection. Mech. Syst. Signal Process. 2025, 235, 112854. [CrossRef]
19.
Li, B.; Gao, X.; Huang, H.; Yang, H. Improved Adaptive Twisting Sliding Mode Control for Trajectory Tracking of an AUV Subject
to Uncertainties. Ocean Eng. 2024, 297, 116204. [CrossRef]
20.
Rohith, G. Fractional Power Rate Reaching Law for Augmented Sliding Mode Performance. J. Frankl. Inst. 2021, 358, 856–876.
[CrossRef]
21.
Kim, J.; Choi, S.; Yun, D. Supercritical Sliding-Mode Control for Position Tracking of PMSM With Disturbance Rejection. IEEE
Trans. Power Electron. 2025, 41, 13–24. [CrossRef]
22.
Xu, Y.; Zhang, B.; Deng, Y.; Kang, Y.; Liu, X.; Cao, H. Robust Speed Control Strategy of PMSMs Using Improved Sliding-Mode
Controller With New Reaching Law and Variable-Parameter Generalized Super-Twisting Observer. IEEE Trans. Power Electron.
2025, 40, 16548–16559. [CrossRef]
23.
Zhang, Z.; Yang, X.; Wang, W.; Chen, K.; Cheung, N.C.; Pan, J. Enhanced Sliding Mode Control for PMSM Speed Drive Systems
Using a Novel Adaptive Sliding Mode Reaching Law Based on Exponential Function. IEEE Trans. Ind. Electron. 2024, 71,
11978–11988. [CrossRef]
https://doi.org/10.3390/act15020128

## Page 21

Actuators 2026, 15, 128
21 of 21
24.
Chughtai, M.R.; Ahmad, I.; Mughees, A.; Iqbal, M.; Almakhles, D.; Abdelrahim, M. Third-Order Sliding Mode Control for
Trajectory Tracking of Quadcopters Using Particle Swarm Optimization. Drones 2025, 9, 172. [CrossRef]
25.
Li, J.; Shang, Z.; Li, R.; Cui, B. Adaptive Sliding Mode Path Tracking Control of Unmanned Rice Transplanter. Agriculture 2022,
12, 1225. [CrossRef]
26.
Gao, W.; Hung, J.C. Variable Structure Control of Nonlinear Systems: A New Approach. IEEE Trans. Ind. Electron. 1993, 40, 45–55.
[CrossRef]
27.
Shen, X.; Liu, J.; Liu, G.; Zhang, J.; Leon, J.I.; Wu, L.; Franquelo, L.G. Finite-Time Sliding Mode Control for NPC Converters With
Enhanced Disturbance Compensation. IEEE Trans. Circuits Syst. I 2025, 72, 1822–1831. [CrossRef]
28.
Ohnishi, K.; Shibata, M.; Murakami, T. Motion Control for Advanced Mechatronics. IEEE/ASME Trans. Mechatron. 2002, 1, 56–67.
[CrossRef]
29.
Han, J. From PID to Active Disturbance Rejection Control. IEEE Trans. Ind. Electron. 2009, 56, 900–906. [CrossRef]
30.
Li, S.; Lu, H.; Li, J.; Zheng, T.; He, Y. Fractional-Order Sliding Mode Controller Based on ESO for a Buck Converter With
Mismatched Disturbances: Design and Experiments. IEEE Trans. Ind. Electron. 2025, 72, 8451–8462. [CrossRef]
31.
Ren, B.; Fang, S.; Song, Z.; Xu, Q.; Wang, J.; Meng, Y. Low-Pass Sliding Mode Control for Arc Motor Based on Adaptive Reaching
Law. IEEE J. Emerg. Sel. Top. Power Electron. 2025, 13, 5911–5921. [CrossRef]
32.
Zhao, X.; Wang, Z.; Zhang, H.; Yan, H. Hierarchical Prescribed-Time ESO-Based Fault-Tolerant Controller Synthesis for Error-
Constrained Coordination of Networked Robotic Systems. Nonlinear Dyn. 2025, 113, 3593–3609. [CrossRef]
33.
Sun, H.; Zhang, X.; Liu, X.; Su, H. Adaptive Robust Sensorless Control for PMSM Based on Improved Back EMF Observer and
Extended State Observer. IEEE Trans. Ind. Electron. 2024, 71, 16635–16643. [CrossRef]
34.
Sun, H.; Wang, C.; Zhao, W. Compound Disturbance Suppression Strategy for Steer-by-Wire System With Permanent Magnet
Synchronous Motor. IEEE Trans. Transp. Electrific. 2025, 11, 4482–4493. [CrossRef]
35.
Ren, J.; Ye, Y.; Xu, G.; Zhao, Q.; Zhu, M. Uncertainty-and-Disturbance-Estimator-Based Current Control Scheme for PMSM Drives
With a Simple Parameter Tuning Algorithm. IEEE Trans. Power Electron. 2017, 32, 5712–5722. [CrossRef]
36.
Lu, Q.; Ren, B.; Parameswaran, S. Uncertainty and Disturbance Estimator-Based Global Trajectory Tracking Control for a
Quadrotor. IEEE/ASME Trans. Mechatron. 2020, 25, 1519–1530. [CrossRef]
37.
Wang, H.; Wen, G.; Xue, W.; Fan, Z.; Zhang, F. Peak-Free Feedback-Cascaded Generalized Extended High-Gain Observer: A
Multisaturation Approach. IEEE Trans. Syst. Man Cybern Syst. 2025, 55, 9669–9680. [CrossRef]
38.
Shao, X.; Xu, L.; Sun, G.; Yao, W.; Wu, L.; Della Santina, C. Self-Attention Enhanced Dynamics Learning and Adaptive Fractional-
Order Control for Continuum Soft Robots With System Uncertainties. IEEE Trans. Automat. Sci. Eng. 2025, 22, 18694–18708.
[CrossRef]
39.
He, L.; Guo, C.; Xu, Z.; Huang, C.; Wei, Y.; Shi, Q. Particle-Swarm Backstepping Control for Angle Tracking of Electric Motor
Steer-by-Wire System. IEEE Trans. Transp. Electrific. 2023, 9, 2038–2047. [CrossRef]
40.
Huang, C.; Naghdy, F.; Du, H. Sliding Mode Predictive Tracking Control for Uncertain Steer-by-Wire System. Control Eng. Pract.
2019, 85, 194–205. [CrossRef]
41.
Pu, Z.; Yuan, R.; Yi, J.; Tan, X. A Class of Adaptive Extended State Observers for Nonlinear Disturbed Systems. IEEE Trans. Ind.
Electron. 2015, 62, 5858–5869. [CrossRef]
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.
https://doi.org/10.3390/act15020128
