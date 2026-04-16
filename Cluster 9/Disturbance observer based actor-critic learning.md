# Disturbance observer based actor-critic learning.pdf

## Page 1

Disturbance observer based actor-critic learning
control for uncertain nonlinear systems
Xianglong LIANG a, Zhikai YAO b, Yaowen GE a, Jianyong YAO a,*
a School of Mechanical Engineering, Nanjing University of Science and Technology, Nanjing 210094, China
b College of Artiﬁcial Intelligence, Nanjing University of Post and Telecommunication, Nanjing 210023, China
Received 8 October 2022; revised 3 December 2022; accepted 17 January 2023
Available online 27 June 2023
KEYWORDS
Actor-critic structure;
Composite adaptation;
Disturbance observer;
Robot manipulator;
Uncertain nonlinear system
Abstract
This paper investigates the disturbance observer based actor-critic learning control for a
class of uncertain nonlinear systems in the presence of unmodeled dynamics and time-varying dis-
turbances. The proposed control algorithm integrates a ﬁlter-based design method with actor-critic
learning architecture and disturbance observer to circumvent the unmodeled dynamic and the time-
varying disturbance. To be speciﬁc, the actor network is employed to estimate the unknown system
dynamic, the critic network is developed to evaluate the control performance, and the disturbance
observer is leveraged to provide efﬁcient estimation of the compounded disturbance which includes
the time-varying disturbance and the actor-critic network approximation error. Consequently, high-
gain feedback is avoided and the improved tracking performance can be expected. Moreover, a
composite weight adaptation law for actor network is constructed by utilizing two types of signals,
the cost function and the modeling error. Eventually, theoretical analysis demonstrates that the
developed controller can guarantee bounded stability. Extensive simulations and experiments on
a robot manipulator are implemented to validate the performance of the resulted control strategy.
 2023 Production and hosting by Elsevier Ltd. on behalf of Chinese Society of Aeronautics and
Astronautics. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/
licenses/by-nc-nd/4.0/).
1. Introduction
Owing to its signiﬁcance, both from a practical and a theoret-
ical perspective, the control design of uncertain nonlinear sys-
tems has been a major research topic over the past decades.1–4
Some remarkable control approaches can be found in Refs. 5–
7, including backstepping control, adaptive control, and
observer-based nonlinear control, to name a few. Among
them, adaptive control is an effective approach to address
unknown parameters, and hereafter, its combination with
backstepping technique plays an important role in the control
of nonlinear systems. However, all these aforementioned meth-
ods cannot be directly applied to the nonlinear systems con-
taining
completely
unknown
dynamic
structure,
which
hinders their widespread application.
In recent years, scholars have observed that Neural Net-
work (NN) displays excellent ability in dealing with unknown
nonlinearity due to its universal function approximation prop-
erties, and substantial control problems have been addressed
by utilizing the NN.8–10 For instance, in Ref. 11, an adaptive
neural tracking control problem was investigated for strict
feedback nonlinear systems with unmodeled dynamics. By
introducing robust control and disturbance observer tech-
niques, the authors in Refs. 12–13 presented robust adaptive
neural control and disturbance observer based adaptive neural
* Corresponding author.
E-mail address: jerryyao.buaa@gmail.com (J. YAO).
Chinese Journal of Aeronautics, (2023), 36(11): 271–280
Chinese Society of Aeronautics and Astronautics
& Beihang University
Chinese Journal of Aeronautics
cja@buaa.edu.cn
www.sciencedirect.com
https://doi.org/10.1016/j.cja.2023.06.028
1000-9361  2023 Production and hosting by Elsevier Ltd. on behalf of Chinese Society of Aeronautics and Astronautics.
This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by-nc-nd/4.0/).

## Page 2

control, which can handle both unmodeled dynamics and time-
varying disturbances. Different from the traditional NN-based
control, an advanced neural learning control strategy is further
developed according to actor-critic learning architecture.14,15
To be speciﬁc, the actor-critic learning architecture consists
of two networks: an actor network and a critic network. The
actor network is leveraged to approximate an unknown func-
tion and generate action or control signal, while the critic net-
work is leveraged to evaluate the control performance in the
actor-critic learning architecture. The actor-critic learning
architecture with a generalized learning structure can be easily
applied to control other nonlinear systems.
Enlightened by the philosophy in Ref. 15, extensive control
approaches were studied by integrating the actor-critic learn-
ing architecture with traditional control approaches for
unknown nonlinear systems. In Refs. 16–18, the actor-critic
architecture has been successfully applied to estimate the
unknown nonlinearity online and achieved satisfactory results,
yet they ignore the negative inﬂuence of time-varying unknown
disturbances on control performance. However, for the practi-
cal systems (e.g., vehicular systems, robot manipulators and
unmanned aerial vehicles19–21), the time-varying perturbations
always exist. The appearance of time-varying disturbance
could generate some unexpected results, such as degrading
the control performance and leading to system divergence,
and it is difﬁcult to circumvent the inﬂuence of the time-
varying disturbances with actor-critic learning control alone.
Moreover, the approximation inaccuracy caused by actor-
critic learning also inﬂuences the tracking performance. In this
regard, the above-mentioned factors facilitate the combination
of the actor-critic control and robust control or disturbance
observer based control. In Ref. 22, the actor-critic structure
is used to estimate the modeling uncertainties that exist in a
small unmanned helicopter, and a discontinuous sliding model
based robust component is introduced to eliminate the inﬂu-
ence of the approximation error of actor network and
unknown disturbance. To overcome the discontinuities of con-
trol input, a prescribed performance fault-tolerant control
approach is developed in Ref.23 by integrating the actor-
critic learning scheme with a Robust Integral of the Sign of
Error (RISE) feedback term, which requires less system infor-
mation and achieves the asymptotic stability. However, large
feedback gains are required to resist unknown disturbances
in robust control, which will reduce the stability margin, even
stimulate high-frequency dynamics, and then result in system
instability. Inspired by the feedforward design, disturbance
observer based control24–27 can be used to estimate the impact
of disturbance and further used for compensation. In Refs.
28,29, a reinforcement learning based controller integrated
with disturbance observer is established to reject the real-
time external disturbance, which can guarantee the robust sta-
bility and the nominal performance even for the uncertain
plant, and obtain satisfactory results in the numerical simula-
tion. However, both of them merely focus on the regulation
control problem.
Inspired by the aforementioned challenges, a disturbance
observer based actor-critic learning control is developed for
a class of uncertain nonlinear systems in the presence of
unknown dynamic and time-varying disturbance. To cope with
the unknown dynamic, the actor-critic learning architecture is
developed to provide the feedforward compensation by
approximating unknown nonlinearity. Considering the effect
of the time-varying disturbance and actor-critic network
approximation error on tracking performance, the actor-
critic learning algorithm is combined with the disturbance
observer to circumvent the effects of the above factors. In
addition, a composite weight adaptation law for actor network
is constructed by utilizing two types of signals, the cost func-
tion and the modeling error. Consequently, high-gain feedback
is avoided and the improved tracking performance can be
achieved. Eventually, extensive simulations and experiments
on a robot manipulator are implemented to validate the per-
formance of the resulted control strategy.
The key contributions of this paper are listed as follows:
(1) An actor-critic learning architecture is developed to esti-
mate the unknown system dynamic online, which
requires less model information and improves the
robustness to unmodeled dynamic effectively.
(2) A disturbance observer is effectively combined to com-
pensate for the time-varying disturbance and actor-
critic network approximation error, which avoids high-
gain
feedback
and
achieves
improved
tracking
performance.
To the best of our knowledge, few studies have integrated
actor-critic learning architecture with disturbance observer
for tracking control of uncertain nonlinear systems with
unmodeled dynamic and time-varying unknown disturbance.
The remainder of this paper is organized as follows. The
problem description is provided in Section 2. Section 3 states
the disturbance observer based actor-critic learning control
scheme and system stability analysis. Simulation and experi-
mental studies on a single-link robot are provided in Section 4,
and conclusions are drawn in Section 5.
2. Problem description
Consider a class of the nth-order Multiple Input Multiple Out-
put (MIMO) nonlinear systems with the following form:
_xi ¼ xiþ1i ¼ 1; 2;    ; n  1
_xn ¼ gðxÞu þ fðxÞ þ dðtÞ
yðtÞ ¼ x1
8
>
<
>
:
ð1Þ
where x ¼ ½xT
1 ; xT
2 ;    ; xT
n 
T 2 Rmn denotes the system state
vector with xi 2 Rm, which is assumed to be available for mea-
surement; u 2 Rm is the control input; y 2 Rm is the system
output; f 2 Rm is the unknown smooth nonlinear function,
gðxÞ 2 Rm is the known nonzero function, and dðtÞ 2 Rm is
the time-varying disturbance.
The main control objective of this study is to propose a dis-
turbance observer based actor-critic learning control strategy
to achieve high tracking accuracy with unmodeled dynamic
and time-varying unknown disturbance. To facilitate the pre-
sentation,
some
related
assumptions
and
lemmas
are
necessary.
Assumption 1. The reference trajectory yrðtÞ 2 Rm and its n-
derivative yðnÞ
r
are available, smooth, and bounded.
Assumption 2. The time-varying disturbance dðtÞ and its ﬁrst
derivative are bounded, which satisfy kdk 6 dm; k_dk 6 d

m.
272
X. LIANG et al.

## Page 3

Lemma 1. The NN universal approximation property indi-
cates that a continuous function U : S ! RN1 (S is a compact
set) can be approximated as
UðxÞ ¼ WTuðxÞ þ eðxÞ
ð2Þ
where x 2 RN2 is the input vector, W 2 RN3N1 is the ideal
weight matrix, and N1, N2 and N3 are numbers of neurons in
the output, input, and hidden layer, respectively. uðxÞ 2 RN3
is the nonlinear activation function. According to Ref. 22,
the ideal NN weights, nonlinear activation function and
approximation
error
are
assumed
to
be
bounded
by
kWk 6 Wm,kuk 6 um; k _uk 6 u

m,kek 6 em; k_ek 6 e

m.
3. Main results
In this scenario, the disturbance observer based actor-critic
learning control strategy for uncertain nonlinear system Eq.
(1) will be presented. First, we provide the backstepping con-
troller design based on a ﬁlter-based design approach. Then,
we design the actor-critic network to deal with the unknown
nonlinear dynamic, where the critic network is leveraged to
evaluate the control performance while the actor network is
leveraged to approximate the unknown function. The architec-
ture of the developed control scheme is depicted as Fig. 1.
3.1. Controller design
To quantify the aforementioned control objective, the tracking
error z1 2 Rm is deﬁned as z1 ¼ y  yr, and the following ﬁl-
tered tracking errors are introduced to facilitate the controller
design
z2 ¼ _z1 þ k1z1
i ¼ 3; 4;    ; n
zi ¼ _zi1 þ ki1zi1
8
<
:
ð3Þ
where k1; k2;    ; kn1 2 R denote positive control gains. By
substituting Eq. (1) into Eq. (3), the dynamic of ﬁltered track-
ing error zn can be written as
_zn ¼ gðxÞu þ fðxÞ þ d  yðnÞ
r
þ k1zðn1Þ
1
þk2zðn2Þ
2
þ    þ kn1zð1Þ
n1
¼ gðxÞu þ fðxÞ þ d  yðnÞ
r
þ k

z
ð4Þ
where k

¼ ½k1; k2;    ; kn1, z ¼ ½zðn1Þ
1
; zðn2Þ
2
;    ; zð1Þ
n1, and the
unknown nonlinear function fðxÞ can be approximated by an
NN-based actor network
fðxaÞ ¼ WT
a uðxaÞ þ ea
ð5Þ
where xa ¼ ½xT
1 ; xT
2 ;    ; xT
n 
T denotes the input vector, Wa
denotes the weight vector of actor network and ea denotes
the actor network function reconstruction inaccuracy, which
satisﬁes keak 6 eam and k_eak 6 e

am. Deﬁning f ¼ ea þ d, the
expression in Eq. (4) can be further expressed as
_zn ¼ gðxÞu þ ^Wa
Tua  W
 T
a ua þ f  yðnÞ
r
þ kz
ð6Þ
where W

a ¼ ^Wa  Wa and ^Wa is the estimate of Wa, which
will be introduced later.
Generally, time-varying external disturbances can be esti-
mated by using model-based disturbance observers.30 Herein,
the time-varying external disturbance and the residual function
reconstruction inaccuracy of the actor network are integrated
as f. The adaptive neural disturbance observer for estimating
the lumped disturbance f is designed by using neural network
approximation
_h ¼ aðh þ axnÞ  að ^WT
a ua þ gðxÞuÞ
bf ¼ h þ axn
(
ð7Þ
where h 2 Rn is an internal state and a 2 R is a positive con-
stant. Therefore, the control input u can be given by
u ¼ g1ðxÞðyðnÞ
r
 kz  knzn  ^WT
a ua  bfÞ
ð8Þ
where kn 2 R denotes a positive control gain. Substituting Eq.
(8) into Eq. (6), the dynamics of ﬁltered error zn can be rewrit-
ten as
_zn ¼ knzn  W
 T
a ua þ f

ð9Þ
Fig. 1
Structure of disturbance observer based actor-critic learning control strategy.
Disturbance observer based actor-critic learning control
273

## Page 4

with f

¼ f  bf and
_~f ¼ a f

þaW
 T
a ua þ _f
ð10Þ
Remark 1. Apart from external disturbance, the residual
function reconstruction inaccuracy of actor network is esti-
mated by designing adaptive neural disturbance observer,
which is different from conventional disturbance observers.30
The performance and robustness of the control plant can be
greatly improved by utilizing the adaptive neural disturbance
observer for disturbance compensation.
3.2. Critic network design
The critic network is utilized to provide the evaluation func-
tion for the current strategy, which can test the performance
of the current policy and generate rewards/punishments as
the feedback for adaptive learning. Therefore, we introduce
the inﬁnite horizon performance index function as follows:
VðtÞ ¼
Z 1
t
exp½cðs  tÞrðsÞds
ð11Þ
where c > 0 represents a discount factor, which can guarantee
the boundedness of the cost function even if the reference tra-
jectory does not converge to zero, and rðtÞ represents an
instantaneous cost function
rðtÞ ¼ zT
1 Qz1 þ uTRu
ð12Þ
where Q 2 Rmm and R 2 Rmm are the weighting matrices for
the lumped tracking error z1 and control input u, respectively.
To achieve optimal control, the cost-to-go function is sup-
posed to be minimized. Given that it is difﬁcult to obtain the
cost-to-go function, an NN-based critic network is introduced
VðxcÞ ¼ WT
c uðxcÞ þ ec
ð13Þ
where xc ¼ z1 denotes the input vector, Wc denotes the weight
vector of critic network and ec denotes the critic network func-
tion reconstruction inaccuracy, which satisﬁes keck 6 ecm and
k_eck 6 e

cm. And the cost-to-go function can be approximated by
bVðxcÞ ¼ ^WT
c uðxcÞ
where ^Wc is the estimate of Wc.
The weight vector c
Wc is selected to minimize the objection
function Ec ¼ 0:5eT
c ec, and according to Eq. (11) and Eq. (12),
the prediction error ecðÞ can be expressed as
ec ¼ rðtÞ þ _^VðtÞ  c ^VðtÞ
ð15Þ
and the critic network weight parameters are updated by
the following update law:
_^Wc ¼ kc1ecðcuc þ ruc _xcÞ  kc2c
Wc
¼ kc1ðr þ c
WT
c KÞK  kc2c
Wc
ð16Þ
where kc1; kc2 are positive parameters and K ¼ cuc þ ruc _xc.
3.3. Actor network design
The actor network is leveraged to estimate the unknown
function fðxÞ that exists in Eq. (4), which can generate the
appropriate control policy by gradually accumulating the sys-
tem experience. The approximation of fðxÞ is designed as
follows:
^fðxaÞ ¼ ^WT
a uðxaÞ
ð17Þ
Deﬁne a prediction error eaðÞ as
ea ¼ KVð ^V  VdÞ þ ^WT
a ua
ð18Þ
where KV 2 Rm is the positive design parameter and Vd ¼ 0
is the ideal value of cost-to-go. The weight vector c
Wa is
selected to minimize the objection function Ea ¼ 0:5eT
a ea and
the actor network weight parameters are updated by the fol-
lowing update law:
_^Wa ¼ ka1uaðKV ^V þ ^WT
a uaÞ  ka2c
Wa
ð19Þ
with positive parameters ka1 and ka2. To further improve the
convergence of the estimated weights c
Wa and the function
approximation precision of actor network, another prediction
error x

n, named modeling error,24 is deﬁned as x

n ¼ bxn  xn, in
which x
^
n can be obtained by constructing the following serial-
parallel estimation model 31:
_^xi1 ¼ bxii ¼ 1; 2;    ; n  1
_^xn ¼ gðxÞu þ ^WT
a ua þ bf  bx

n
(
ð20Þ
and the dynamic equation x

n is written as
_~xn ¼ bx

n  W
 T
a ua  f

ð21Þ
in which b 2 R is a positive constant.
Therefore,
the
actor
network
weight
parameters
are
adjusted by the following composite update law:
_^Wa ¼ ka1uaðKV ^V þ ^WT
a uaÞ  ka2c
Wa  ka3uax
T
n
ð22Þ
where ka3 is a positive parameter.
Remark 2. Different from the traditional action network
weights updating,18,22,23 a composite weight adaptation law
for actor network is constructed by using both prediction error
ea and modeling error x

n, which ensures that the estimated
weights c
Wa converge better to unknown weights Wa and the
more precise approximation of the nonlinear function is
achieved.32
3.4. Stability analysis
Theorem 1. In consideration of the nonlinear system Eq. (1) in
the presence of unmodeled dynamic and time-varying distur-
bance, if the control input Eq. (8), the critic network weight
adaptive law Eq. (16), the actor network weight adaptive law
Eq. (22) and the adaptive neural disturbance observer Eq. (7)
are designed, then all system signals are bounded. Proof details
are given in Appendix A.
274
X. LIANG et al.

## Page 5

4. Simulation and experiments
4.1. Simulation
To substantiate the feasibility and effectiveness of the devel-
oped control strategy, we consider a two-degree-of-freedom
robot manipulator (see Ref. 32) with the following dynamic
equation:
MðqÞ€q þ Cðq; _qÞ_q þ Fð_qÞ þ sd ¼ s
ð23Þ
where q; _q; €q denote the position, velocity, and acceleration,
respectively,
MðqÞ
is
the
inertia
matrix,
Cðq; _qÞ
is
the
centripetal-Coriolis matrix, Fð_qÞ is the friction, sd is the exter-
nal disturbance, and s is the control input.
The matrix MðqÞ; Cðq; _qÞ; Fð_qÞ and sd are given as follows:
MðqÞ ¼
p1 þ 2p3 cosðq2Þ
p2 þ p3 cosðq2Þ
p2 þ p3 cosðq2Þ
p2


Cðq; _qÞ ¼
p3 sinðq2Þ _q2
p3 sinðq2Þð _q1 þ _q2Þ
p3 sinðq2Þ _q1
0


Fð_qÞ ¼
fd1
0
0
fd2


_q1
_q2


; sd ¼
sd1
sd2


where
p1 ¼ 3:473 kg  m2,
p2 ¼ 0:196 kg  m2,
p3 ¼ 0:242 kg  m2,
fd1 ¼ 5:3 N  m  s,
fd2 ¼ 1:1 N  m  s,
sd1 ¼ 3 sinðtÞ and sd2 ¼ 0:2 sinðtÞ.
Then the dynamics in Eq. (23) can be transformed into the
state-space equation considered in this paper, i.e.,
_x1 ¼ x2
_x2 ¼ gðxÞu þ fðxÞ þ dðtÞ

ð24Þ
with
x1 ¼ q1; q2
½
T; x2 ¼ _q1; _q2
½
T; gðxÞ ¼ M1ðx1Þ,
u ¼ s,
fðxÞ ¼ M1½Cðx1; x2Þx2 þ Fðx2Þ and dðtÞ ¼ M1sd.
The following two control strategies are compared to vali-
date the effectiveness of the proposed approach:
Controller 1. This is the proposed controller or more specif-
ically, actor-critic learning control integrated with disturbance
observer. The control parameters are chosen as k1 ¼ 30,
k2 ¼ 10, a ¼ 20, b ¼ 100, kc1 ¼ 2, kc2 ¼ 0:1, ka1 ¼ 20, ka2 ¼ 1
and ka3 ¼ 5. The initial weights of actor-critic networks are
chosen as c
Wa ¼ zerosð10; 4Þ and c
Wc ¼ zerosð10; 2Þ. The dis-
count factor is chosen as c ¼ 0:1, the positive matrices Q and
R in the cost function are selected as Q ¼ diagð½50 200Þ and
R ¼ diagð½0:1 0:1Þ, respectively.
Controller 2. This is the actor-critic learning control
approach without disturbance feedforward compensation. To
ensure fair comparison, the selected control parameters are
consistent with Controller 1.
The reference trajectories of two joints are chosen as
yr1 ¼ 0:6 sinð3:14tÞ  ½1  expðtÞ
and
yr2 ¼ 0:8 sinð3:14tÞ
½1  expðtÞ. The simulation results are depicted as Figs. 2-
6. As depicted in Fig. 2 and Fig. 3, the integrated Controller
1 controller can follow the reference signal well and achieve
the best tracking performance in aspects of convergence speed
and steady tracking error since the disturbance observer is
introduced. In comparison of the last 20 s, the maximum
amplitude of steady tracking error Mz1 ¼ ½0:0009; 0:0058 rad
under Controller 1, while the maximum amplitude of steady
tracking error Mz1 ¼ ½0:0021; 0:0103 rad under Controller 2.
The results in Figs. 4 and 5 depict the compound estimation
of f þ d, and it can be found that the composite estimation
architecture established by actor-critic learning and distur-
bance observer can well approximate the unmodeled dynamic
and time-varying disturbance in comparison of the estimation
architecture only with actor-critic learning. This phenomenon
Fig. 2
Tracking performance with proposed controller Con-
troller 1.
Fig. 3
Tracking errors for Joints 1 and 2 under Controller 1 and
Controller 2.
Fig. 4
Compound estimation
f þ d
ð
Þ 1½  for Joint 1 under
Controller 1 and Controller 2.
Disturbance observer based actor-critic learning control
275

## Page 6

explains that the accurate feedforward compensation can
result in higher tracking accuracy. Eventually, the control
inputs are shown in Fig. 6, which are regular and bounded.
4.2. Experiments
To further substantiate the priority of the developed control
strategy, an experiment was conducted on a single-degree-of-
freedom robot manipulator platform shown in Fig. 7. The test
rig includes a bench case, a motor actuator (consisting of a DC
motor Kollmorgen DH063A, an electrical driver Kollmorgen
ServoStar 620, a rotary encoder Heidenhain ERN180, and a
revolute joint), a link, a payload and a control module. The
control module consists of a real-time control software com-
posed of an Advantech PCI-1723 and a Heidenhain IK-220
counter card, and a monitoring software. The sampling time
is 0.5 ms.
The dynamic of single-degree-of-freedom robot manipula-
tor can also be written as the state-space form shown in Eq.
(24)
with
x1 ¼ q; x2 ¼ _q; x ¼ ½x1; x2T,
gðxÞ ¼ J1,
u ¼ s,
fðxÞ ¼ J1½Fð _qÞ þ GðqÞ and dðtÞ ¼ J1sd, where q; _q denote
the position and velocity, respectively, Fð _qÞ is the unknown
friction, GðqÞ is the unknown gravity, sd is the external distur-
bance, s is the control input, and J ¼ Jr þ Jl þ Jp is the total
moment of inertia with the joint moment of inertia Jr, the link
moment of inertia Jl ¼ mlL2=3 and the payload moment of
inertia Jp ¼ mpL2. The system parameters are provided as
Jr ¼ 0:3 kg  m2, L ¼ 0:5 m, ml ¼ 0:5 kg and mp ¼ 0  1 kg.
Likewise, the aforementioned two controllers are still uti-
lized to test in the experiments. The reference signal is chosen
as yr ¼ 10½1  cosð3:14tÞ  ½1  expðtÞ, the control parame-
ters are chosen as k1 ¼ 150, k2 ¼ 50, a ¼ 10, b ¼ 50, kc1 ¼ 2,
kc2 ¼ 0:5, ka1 ¼ 20, ka2 ¼ 2 and ka3 ¼ 5. The initial weights
of
actor-critic
networks
are
chosen
as
c
Wa ¼ zerosð10; 2Þ; ^Wc ¼ zerosð10; 1Þ. The discount factor is
chosen as c ¼ 0:1, and the positive matrices Q and R in the cost
function are selected as Q ¼ ½50 and R ¼ ½1, respectively. In
this scenario, the control performance with different payloads
mp ¼ 0 kg, mp ¼ 0:5 kg and mp ¼ 1 kg is tested, respectively.
Furthermore, to quantitatively evaluate the tracking perfor-
mance of the aforementioned controllers, three performance
indices (i.e., the maximum Mz, average l, and standard devia-
tion r) in Ref. 33 are introduced.
Case 1. The compared two controllers are tested under no-
load condition with mp ¼ 0 kg. The tracking errors and the
performance indices (during the last 20 s) of the two
controllers are presented in Fig. 8. From these results, it can
be observed that the tracking performance of Controller 1 is
improved compared with that of Controller 2 since the
disturbance observer is integrated with actor-critic learning
control, and the result of compound estimation ^f þ ^d acquired
by action network and disturbance observer is depicted in
Fig. 9.
Fig. 5
Compound estimation
f þ d
ð
Þ 2½  for Joint 2 under
Controller 1 and Controller 2.
Fig. 6
Control inputs of two joints under Controller 1 and
Controller 2.
Fig. 7
A single-degree-of-freedom robot manipulator platform.
276
X. LIANG et al.

## Page 7

Case 2. The compared two controllers are tested under light
load condition with mp ¼ 0:5 kg. The tracking errors and the
performance indices are shown in Fig. 10. It can be seen that
the performance of Controller 1 still outperforms that of Con-
troller 2. In comparison with the no-load condition, Mz of
Controller 1 changed very little, and only increased by 1:6%,
while that of Controller 2 increased by about two times, and
this phenomenon illustrates that the actor-critic learning con-
trol alone is not enough to compensate for the impact of load
change on the system. In addition, the result of compound esti-
mation is depicted in Fig. 11. Compared with Fig. 9, it can be
observed that as the payload becomes larger, the proposed
composite estimation scheme can well adapt to the change of
system uncertainty, which further illustrates that Controller 1
can effectively compensate for the inﬂuence of load change.
Case 3. The compared two controllers are tested under heavy
load condition with mp ¼ 1 kg. The tracking errors and the
performance indices are shown in Fig. 12. Likewise, the perfor-
mance of Controller 1 still outperforms that of Controller 2,
and compared with the no-load condition, Mz of Controller
1 increased by 5:5%, while that of Controller 2 increased by
about 2.3 times, which further illustrates that Controller 1
can effectively compensate for the impact of load change on
the system. The result of compound estimation is depicted in
Fig. 13. Compared with Fig. 9, it can be observed that as the
payload becomes larger, Controller 1 can still well adapt to
the change of system uncertainty.
Fig. 8
System tracking errors of Controller 1 and Controller 2
under no-load condition with mp ¼ 0 kg.
Fig. 9
Compound estimation of ^f þ ^d of Controller 1 under no-
load condition with mp ¼ 0 kg.
Fig. 10
System tracking errors of Controller 1 and Controller 2
under light load condition with mp ¼ 0:5 kg.
Fig. 11
Compound estimation of ^f þ ^d of Controller 1 under
light load condition with mp ¼ 0:5 kg.
Fig. 12
System tracking errors of Controller 1 and Controller 2
under heavy load condition with mp ¼ 1 kg.
Fig. 13
Compound estimation of ^f þ ^d of Controller 1 under
heavy load condition with mp ¼ 1 kg.
Disturbance observer based actor-critic learning control
277

## Page 8

In order to more intuitively observe the impact of load
change on the tracking performance of controllers Controller
1 and Controller 2, Mz of the two controllers under different
payloads are collected together, as shown in Fig. 14. It is evi-
dent that Controller 1 can effectively compensate for the
impact of load change on the system and maintain its tracking
performance, while the tracking performance of Controller 2
gradually deteriorates with the increase of payload. To this
end, the proposed controller Controller 1 is robust to
unknown uncertainties and the improved tracking perfor-
mance can be achieved.
5. Conclusions
In this paper, the disturbance observer based actor-critic learn-
ing control is investigated for a class of nonlinear systems in
the presence of unknown dynamic and time-varying distur-
bance. A composite weight adaptation law for actor network
is constructed by both cost function and modeling error, and
a disturbance observer component is combined to compensate
for the residual functional reconstruction inaccuracy caused by
the actor network and the time-varying disturbance. Extensive
simulations and experiments on a robot manipulator present
that using the developed disturbance observer based actor-
critic learning control strategy can effectively circumvent the
inﬂuence of unknown system dynamic and time-varying distur-
bance, and higher tracking accuracy can be achieved. Consid-
ering that the full state information is required in the
implementation of the developed control strategy, we will
explore an output feedback control approach for uncertain
nonlinear systems in the future.
Declaration of Competing Interest
The authors declare that they have no known competing
ﬁnancial interests or personal relationships that could have
appeared to inﬂuence the work reported in this paper.
Acknowledgements
This work was supported by the National Key R&D Program
of China (No. 2021YFB2011300), the National Natural
Science Foundation of China (No. 52075262).
Appendix A. Proof of Theorem 1. Consider the following
Lyapunov candidate function:
L ¼ L1 þ L2 þ L3 þ L4 þ L5
ðA1Þ
where
L1 ¼
X
n
i¼1
1
2 zT
i zi; L2 ¼ 1
2 f
T f

; L3 ¼ 1
2 trðW
 T
c W

cÞ;
L4 ¼ 1
2 trðW
 T
a W

aÞ; L5 ¼ 1
2 x
T
nx

n
ðA2Þ
Using Eq. (3) and Eq. (9), the derivative of L1 can be
expressed as
_L1 ¼ k1zT
1 z1 þ zT
1 z2  k2zT
2 z2 þ zT
2 z3 þ     kn1zT
n1zn1
þ zT
n1zn  knzT
n zn þ zT
n ðW
 T
a ua þ f

Þ
 k1kz1k2 þ 1
2 kz1k2 þ 1
2 kz2k2  k2kz2k2
þ 1
2 kz2k2 þ 1
2 kz3k2 þ     kn1kzn1k2
þ 1
2 kzn1k2 þ 1
2 kznk2  knkznk2 þ kznk2
þ 1
2 k f

k2 þ 1
2 kW

ak2kuak2
ðA3Þ
Using Eq. (10), the derivative of L2 can be expressed as
_L2 ¼ af

T f

þaf

TW
 T
a ua þ f

T_f
6 ak f

k2 þ 1
2 ak f

k2 þ 1
2 akW

ak2kuak2
þ 1
2 k f

k2 þ 1
2 k_fk
2
6  1
2 ða  1Þk f

k2 þ 1
2 akW

ak2kuak2 þ 1
2 k_fk
2
ðA4Þ
Using Eq. (13) and Eq. (16), the derivative of L3 can be
expressed as.
_L3 ¼ kc1W
 T
c ðrðtÞ þ c
WT
c KÞK  kc2W
 T
c c
Wc
¼ kc1W
 T
c ðc
WT
c K þ ec þ c
WT
c KÞK  kc2W
 T
c Wc þ W

c


6  1
2 kc1kmin KKT


þ kc2


W
 T
c W

c þ kc1
2 2T
c 2c þ kc2
2 WT
c Wc
(A5)
where ec ¼ cec  _ec, which is bounded, i.e., keck 6 ecm.
Using Eq. (22), the derivative of L4 can be expressed as
_L4 ¼ ka1W
 T
a uaðKVc
WT
c uc þ c
WT
a uaÞ  ka2W
 T
a c
Wa
ka3W
 T
a ux
T
n
¼ ka1W
 T
a uaW
 T
a ua  ka1W
 T
a uaðWT
a ua þ KVc
WT
c ucÞ
ka2W
 T
a ðWa þ W

aÞ  ka3W
 T
a uax
T
n
6  1
2 ðka1kminðuauT
a Þ þ ka2  ka3kuak2ÞW
 T
a W

a
þka1kWak2kuak2 þ 2ka1KT
VKVkuck2W
 T
c W

c
þ2ka1KT
VKVkWck2kuck2 þ ka2
2 WT
a Wa þ ka3
2 kx

nk
2
ðA6Þ
Using Eq. (21), the derivative of L5 can be expressed as
_L5 ¼ x
T
n ðbx

n  W
 T
a ua  f

Þ  ðb  1Þkx

nk2 þ 1
2 k f

k2 þ 1
2 kW

ak2kuak2 ðA7Þ
Then combining Eqs. (A3)–(A7), the ﬁrst derivative of L
can be written as
_L 6 ðk1  0:5Þkz1k2  ðki  1Þkzik2      ðkn  1:5Þkznk2
 1
2 ðkc1kminðKKTÞ þ kc2  4ka1KT
VKVkuck2ÞkW

ck2
 1
2 ðka1kminðuauT
a Þ  ðka3 þ a þ 2Þkuak2 þ ka2ÞkW

ak2
 1
2 ða  3Þk f

k2  1
2 ð2b  ka3  2Þkx

nk
2 þ q1
6 q0L þ q1
ðA8Þ
Fig. 14
Mz of two controllers under different payloads.
278
X. LIANG et al.

## Page 9

where
q0 ¼ minf2ðk1  0:5Þ; 2ðk2  1Þ;    ; 2ðkn  1:5Þ; a  3; 2b
ka3  2; kc1kminðKKTÞ þ kc2  4ka1KT
VKVkuck2;
ka1kminðuauT
a Þ  ðka3 þ a þ 2Þkuak2 þ ka2g
q1 ¼ 0:5ðkc12
cm þ e
2
am þ d

2
mÞ þ e2
am þ d2
m þ ð2ka1KT
VKVkucmk2
þ0:5kc2ÞkWcmk2 þ ð0:5ka2 þ ka1kuamk2ÞkWamk2
To ensure q0 > 0, the following conditions must be fulﬁlled:
k1 > 0:5; k2 > 1;    ; kn > 1:5
a > 3; 2b  ka3  2 > 0
kc1kminðKKTÞ þ kc2  4ka1KT
VKVkuck2 > 0
ka1kminðuauT
a Þ þ ka2  ðka3 þ a þ 2Þkuak2 > 0
ðA9Þ
Solving the aforementioned differential inequality Eq. (A8),
we have
LðtÞ 6 ðLð0Þ  q1
q0
Þ expðq0tÞ þ q1
q0
6 Lð0Þ þ q1
q0
ðA100Þ
Consequently, all system signals are bounded according to
the deﬁnition of L in Eq. (A1).
References
1. Han SS, Jiao ZX, Wang CW, et al. Fuzzy robust nonlinear control
approach for electro-hydraulic ﬂight motion simulator. Chin J
Aeronaut 2015;28(1):294–304.
2. Yao JY, Deng WX. Active disturbance rejection adaptive control
of uncertain nonlinear systems: Theory and application. Nonlinear
Dyn 2017;89(3):1611–24.
3. Deng WX, Yao JY, Ma DW. Time-varying input delay compen-
sation for nonlinear systems with additive disturbance: An output
feedback approach. Int J Robust Nonlinear Control 2018;28
(1):31–52.
4. Lu Y. Disturbance observer-based backstepping control for
hypersonic ﬂight vehicles without use of measured ﬂight path
angle. Chin J Aeronaut 2021;34(2):396–406.
5. Yao JY, Jiao ZX, Ma DW. Extended-state-observer-based output
feedback nonlinear robust control of hydraulic systems with
backstepping. IEEE Trans Ind Electron 2014;61(11):6285–93.
6. Chen M, Ge SS, Ren BB. Adaptive tracking control of uncertain
MIMO nonlinear systems with input constraints. Automatica
2011;47(3):452–65.
7. Wu XQ, Xu KX, He XX. Disturbance-observer-based nonlinear
control for overhead cranes subject to uncertain disturbances.
Mech Syst Signal Process 2020;139 106631.
8. Bu XW, Wu XY, Ma Z, et al. Novel adaptive neural control of
ﬂexible air-breathing hypersonic vehicles based on sliding mode
differentiator. Chin J Aeronaut 2015;28(4):1209–16.
9. Ouyang YC, Dong L, Xue L, et al. Adaptive control based on
neural networks for an uncertain 2-DOF helicopter system with
input deadzone and output constraints. IEEE/CAA J Autom Sin
2019;6(3):807–15.
10. Ma L, Xu N, Zhao XD, et al. Small-gain technique-based adaptive
neural output-feedback fault-tolerant control of switched nonlin-
ear systems with unmodeled dynamics. IEEE Trans Syst Man
Cybern 2021;51(11):7051–62.
11. Zhang T, Ge SS, Hang CC. Adaptive neural network control for
strict-feedback nonlinear systems using backstepping design.
Automatica 2000;36(12):1835–46.
12. Yao ZK, Yao JY, Sun WC. Adaptive RISE control of hydraulic
systems with multilayer neural-networks. IEEE Trans Ind Electron
2019;66(11):8638–47.
13. Wang XJ, Yin XH, Wu QH, et al. Disturbance observer based
adaptive neural control of uncertain MIMO nonlinear systems
with unmodeled dynamics. Neurocomputing 2018;313:247–58.
14. Sutton RS, Barto AGReinforcement learning: An introduction. 2nd
ed. Cambridge: MIT Press; 2018. p. 331–2.
15. Widrow B, Gupta NK, Maitra S. Punish/reward: Learning with a
critic in adaptive threshold systems. IEEE Trans Syst Man Cybern
1973;3(5):455–65.
16. Cui RX, Yang CG, Li Y, et al. Adaptive neural network control of
AUVs with control input nonlinearities using reinforcement
learning. IEEE Trans Syst Man Cybern 2017;47(6):1019–29.
17. Guo XX, Yan WS, Cui RX. Event-triggered reinforcement
learning-based adaptive tracking control for completely unknown
continuous-time nonlinear systems. IEEE Trans Cybern 2020;50
(7):3231–42.
18. He W, Gao HJ, Zhou C, et al. Reinforcement learning control of a
ﬂexible two-link manipulator: an experimental investigation. IEEE
Trans Syst Man Cybern 2021;51(12):7326–36.
19. Yang J, Su JY, Li SH, et al. High-order mismatched disturbance
compensation for motion control systems via a continuous
dynamic sliding-mode approach. IEEE Trans Ind Inform 2014;10
(1):604–14.
20. Razmjooei H, Shaﬁei MH, Palli G, et al. Non-linear ﬁnite-time
tracking control of uncertain robotic manipulators using time-
varying disturbance observer-based sliding mode method. J Intell
Rob Syst 2022;104(2):1–13.
21. Liang YQ, Dong Q, Zhao YJ. Adaptive leader-follower formation
control for swarms of unmanned aerial vehicles with motion
constraints and unknown disturbances. Chin J Aeronaut 2020;33
(11):2972–88.
22. Xian B, Zhang X, Zhang HN, et al. Robust adaptive control for a
small unmanned helicopter using reinforcement learning. IEEE
Trans Neural Netw Learn Syst 2022;33(12):7589–97.
23. Wang XR, Wang QL, Sun CY. Prescribed performance fault-
tolerant control for uncertain nonlinear MIMO system using
actor–critic learning structure. IEEE Trans Neural Netw Learn
Syst 2022;33(9):4479–90.
24. Xu B, Sun FC, Pan YP, et al. Disturbance observer based
composite learning fuzzy control of nonlinear systems with
unknown dead zone. IEEE Trans Syst Man Cybern 2017;47
(8):1854–62.
25. Jing YH, Yang GH. Fuzzy adaptive quantized fault-tolerant
control of strict-feedback nonlinear systems with mismatched
external disturbances. IEEE Trans Syst Man Cybern 2020;50
(9):3424–34.
26. Zhang R, Xu B, Shi P. Output feedback control of micromechan-
ical gyroscopes using neural networks and disturbance observer.
IEEE Trans Neural Netw Learn Syst 2022;33(3):962–72.
27. Min HF, Xu SY, Fei SM, et al. Observer-based NN control for
nonlinear systems with full-state constraints and external distur-
bances. IEEE Trans Neural Netw Learn Syst 2022;33(9):4322–31.
28. Ran MP, Li JC, Xie LH. Reinforcement-learning-based distur-
bance rejection control for uncertain nonlinear systems. IEEE
Trans Cybern 2022;52(9):9621–33.
29. Kim JW, Shim H, Yang I. On improving the robustness of
reinforcement learning-based controllers using disturbance obser-
ver. 2019 IEEE 58th conference on decision and control (CDC).
Piscataway: IEEE Press; 2020. p. 847-52.
30. Chen WH, Yang J, Guo L, et al. Disturbance-observer-based
control and related methods—an overview. IEEE Trans Ind
Electron 2015;63(2):1083–95.
Disturbance observer based actor-critic learning control
279

## Page 10

31. Xu B, Shi ZK, Yang CG, et al. Composite neural dynamic surface
control of a class of uncertain nonlinear systems in strict-feedback
form. IEEE Trans Cybern 2014;44(12):2626–34.
32. Hojati M, Gazor S. Hybrid adaptive fuzzy identiﬁcation and
control of nonlinear systems. IEEE Trans Fuzzy Syst 2002;10
(2):198–210.
33. Yao ZK, Liang XL, Zhao QT, et al. Adaptive disturbance
observer-based control of hydraulic systems with asymptotic
stability. Appl Math Model 2022;105:226–42.
280
X. LIANG et al.
