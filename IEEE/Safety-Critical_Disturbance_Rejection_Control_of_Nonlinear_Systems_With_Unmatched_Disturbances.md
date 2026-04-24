# Safety-Critical_Disturbance_Rejection_Control_of_Nonlinear_Systems_With_Unmatched_Disturbances.pdf

## Page 1

2722
IEEE TRANSACTIONS ON AUTOMATIC CONTROL, VOL. 70, NO. 4, APRIL 2025
Safety-Critical Disturbance Rejection Control of Nonlinear Systems With
Unmatched Disturbances
Xinming Wang
, Student Member, IEEE, Jun Yang
, Fellow, IEEE, Cunjia Liu
, Senior Member, IEEE,
Yunda Yan
, Member, IEEE, and Shihua Li
, Fellow, IEEE
Abstract—Safety-critical control is signiﬁcant for autonomous
system applications where safety is an utmost concern. Control-
barrier-function (CBF)-based control has shown its promising po-
tential and power in delivering formal safe property of dynamic
nonlinear systems. The presence of disturbances, whether from
matched or unmatched channels, negatively impacts CBF-based
control, leading to violations of formal safety guarantees and de-
graded control performance. In this article, a new safety-critical
disturbance rejection control approach is proposed for nonlinear
systems subject to unmatched disturbances. Owing to the natu-
rally intractable mismatching condition, the disturbances and their
high order derivatives could generate considerable negative im-
pacts on not only the high order CBF but also the control Lyapunov
function. To this end, an observer-based disturbance rejection
CBF is proposed, delivering a new robust adaptive mechanism
to deal with the disturbances. It is shown that by fully exploiting
the disturbance estimates and adequately quantifying the impacts
of estimation errors, the proposed approach provides attractive
properties like formal robust safety guarantee and nominal control
performance recovery under unmatched disturbances. Simulation
results of path following of a drone suffering wind disturbances
verify the beneﬁts of the proposed solution in collision avoidance
and retaining nominal safety performance.
Index Terms—Control-barrier-function (CBF), disturbance ob-
server, disturbance rejection, safety-critical control, unmatched
disturbance.
I. INTRODUCTION
Safety guarantee has become a high priority for autonomous systems
in complex environments, e.g., autonomous vehicles and intelligent
robotics [1], [2], [3], [4]. Among the control approaches maintaining
mission-based safety constraints, control-barrier-function (CBF)-based
control has emerged as a popular and effective tool for formal safety
guarantee by virtue of a forward invariant set [5]. Due to its promis-
ing capability in describing complex nonlinear constraints and less
computational resources in implementation, CBF-based control has
made considerable progress in both theory investigation [6], [7], [8]
and applicable case studies [9], [10], [11].
One of the obstacles in early CBF research is the need for precisely
known system dynamics, which is usually unattainable due to external
Received 23 August 2024; accepted 2 November 2024. Date of pub-
lication 11 November 2024; date of current version 31 March 2025.
This work was supported by the National Natural Science Foundation
of China under Grant 62025302. Recommended by Associate Editor T.
Liu. (Corresponding author: Jun Yang.)
Xinming Wang and Shihua Li are with the Key Laboratory of
Measurement and Control of CSE, Ministry of Education, School
of Automation, Southeast University, Nanjing 210096, China (e-mail:
wxm_seu@seu.edu.cn; lsh@seu.edu.cn).
Jun Yang and Cunjia Liu are with the Department of Aeronautical and
Automotive Engineering, Loughborough University, LE11 3TU Lough-
borough, U.K. (e-mail: j.yang3@lboro.ac.uk; c.liu5@lboro.ac.uk).
Yunda Yan is with the Department of Computer Science, Univer-
sity College London, WC1E 6BT London, U.K. (e-mail: yunda.yan
@ucl.ac.uk).
Digital Object Identiﬁer 10.1109/TAC.2024.3496572
disturbances [6], [8], [12]. Clearly, ignoring the impacts of disturbances
will inﬂuence the desired control performances and even degrade the
formal guarantee of safety speciﬁcation [13]. To address this issue,
one possible treatment is to follow the philosophy of robust control
theory, i.e., designing a controller such that the formal safety property
is ensured even in the presence of worst-case disturbances. Toward this
end, a robust CBF method is proposed in [7], where the system states are
guaranteed to stay in a subset of the predeﬁned safety set. This evident
idea is also utilised to solve the robust safety-critical control problem of
a generic dynamic robotic system with bounded uncertainties in [14].
Moreover, inspired by the input-to-state stability (ISS) [15] in nonlinear
systems, the notion of input-to-state safety (ISSf) [16] is constructed
based on the upper bounds of external disturbances; then an ISSf-based
CBF is designed to render the system be safe within a larger invariant
set compared with original one. It should be highlighted that taking
the worst case of external disturbances into consideration attains strict
safety constraints. However, this approach usually generates overly
conservatism results in safety guarantee, which typically comes at the
expense of sacriﬁcing the control performance.
Disturbance observer-based control (DOBC) provides an alternative
tool to disturbance rejection of nonlinear dynamic systems subject
to disturbances [17]. By estimating and compensating for the distur-
bances, DOBC exhibits promising properties like strong disturbance
rejectioncapabilityandnominalcontrolperformancerecovery[18].Re-
cently,therehavebeensomepreliminaryworks[19],[20],[21]focusing
on the development of robust safety-critical control using disturbance
observer-assisted CBF. To be speciﬁc, by introducing the estimate of
lumped disturbance into the dynamics of CBF, a modiﬁed CBF-based
control approach is designed to enhance the robustness of the safety
guarantee in [19]. Based on the concept of ISSfs, a tunable disturbance
observer-based CBF is proposed in [20], where a new control parameter
is introduced to quantify the impacts caused by the estimation error.
The safety-critical control of sampled-data system with time-varying
disturbance is investigated where the nonlinear disturbance observer is
employed in [21]. Instead of using disturbance observer (DO), a new
robust CBF design is proposed for a disturbed system with only output
measurement based on the extended state observer in [22]. In [23],
when disturbances arise from a dynamically changing environment, an
alternative method, i.e., the environmentally robust CBF, is developed,
taking into account the upper bounds of the estimated environmental
state error.
Despite the enhanced robustness of safety guarantees using observer-
based CBFs as demonstrated in [19], [20], [21], [22], and [23], it is
important to note that these methods are limited to a class of CBFs with
matched disturbances (i.e., disturbances that affect safety speciﬁcations
throughthesamechannelasthecontrolinput).Ithasbeenshownthatthe
existence of unmatched disturbances would also generate adverse im-
pacts on system dynamics, which will signiﬁcantly degrade the control
performance [24], [25]. Taking the path following of drone under winds
as an example, the wind disturbance and its derivative will generate
undesirable impacts on system dynamics via a different channel from
the control input [26]. This naturally intractable mismatching condition
poses great challenges for CBF-based control design as the disturbances
inﬂuence the dynamics of candidate CBFs from both matched and
unmatched channels. Towards this issue, Takano and Yamakita [27]
1558-2523 © 2024 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:35:01 UTC from IEEE Xplore.  Restrictions apply.

## Page 2

IEEE TRANSACTIONS ON AUTOMATIC CONTROL, VOL. 70, NO. 4, APRIL 2025
2723
explored robust CBF design based on Gaussian process regression for
disturbed nonlinear systems, focusing on cases where the input relative
degree (IRD) and the disturbance relative degree (DRD) differ by one.
Here, IRD (DRD) is deﬁned by taking the safety speciﬁcation as the
interested output. This issue is further investigated in [28] by using
disturbance observers. With the help of the disturbance observer, a
preliminary result is developed for a class of single-input-single-output
lower triangular nonlinear system by constructing an estimation error-
based CBF in [29]. However, the analysis in [29] is restricted to a
simpliﬁed scenario that considers only a single external disturbance
and a speciﬁc system dynamic model. It should be highlighted that
there are few works addressing the safety-critical control for a class
of generalized nonlinear systems with disturbances, particularly when
DRD ≤IRD.
In this article, we propose a new safety-critical disturbance rejection
control approach for a class of nonlinear systems with unmatched
disturbances. To address the undesirable inﬂuences of unmatched
disturbances on safety speciﬁcation, disturbance observers are ﬁrst
introduced to obtain the estimates of disturbances and their high order
derivatives. To mitigate the conservativeness arising from quantifying
the estimation errors of high order disturbance derivatives, a new
estimation error quantiﬁcation mechanism is proposed by introducing
a set of saturated disturbance estimates and their saturated estimation
error bounds. Then, inspired by the design of high order CBF in [12], a
disturbance rejection control barrier function (DRCBF) is constructed
by fully exploiting the saturated estimates and their error bounds in
each order derivatives of the DRCBF. Built upon the DRCBF, an
optimization-basedcontrolpolicyisproposedtoachievethestrictsafety
task and satisfactory control performance with the support of input-
to-state stable control Lyapunov function (ISS-CLF) [30]. A rigorous
analysis of robust safety guarantee is established. The effectiveness of
the proposed approach is veriﬁed by a practical example of drone path
following under wind disturbances. The simulation results show that
the proposed control approach exhibits strict safety guarantee as well
as nominal safety performance recovery.
Notations: The sets of real numbers, nonnegative real numbers and
nonnegative integers are denoted as R, R+, and N. For i, j ∈N satis-
fying j ≤k, deﬁne Nj:k ≜{j, j + 1, . . . , k} as a subset of N. Deﬁne
diag(a1, . . . , an) as the diagonal matrix constructed from the vector
a = [a1, . . . , an]T . For a given matrix A or a vector x, deﬁne the |A|
or |x| as the corresponding matrix or vector with their element-wise
absolute values. For any vectors x, y ∈Rn, x ≤y corresponds to the
element-wise inequality between vectors x and y, i.e., xi ≤yi, i ∈
N1:n. Denote ∥x∥as the 2-norm of vector x. The saturation function
satM(x), x ∈R with M > 0 is deﬁned as satM(x) = x, if |x| < M,
and satM(x) = Msign(x), if |x| ≥M.
II. PRELIMINARIES AND MOTIVATION
In this section, we ﬁrst cover the basic safety control design using
CBF for nonlinear systems without disturbances. Then, the notions
of IRD and DRD with respect to safety speciﬁcations are introduced.
Finally, a drone path following with wind disturbances is presented
to highlight the challenges of ensuring safety with unmatched distur-
bances.
A. Safety Control With CBF
Consider the following afﬁne nonlinear system:
˙x = f(x) + g(x)u
(1)
where x ∈X ⊆Rn, u ∈Rm, X is denoted as the admissible compact
set for state. The nonlinear functions f : Rn →Rn, g : Rn →Rn×m
in (1) are known locally Lipschitz functions. In the notion of CBF, a
continuously differentiable function b : Rn →R is used to formulate
the safety speciﬁcation. Deﬁne C0 as the 0-superlevel set of b(x)
C0 = {x ∈Rn : b(x) ≥0}
(2)
Fig. 1.
Illustration of concept of CBF and the safety-critical path fol-
lowing of drone with wind disturbances. (a) Under the control action
from KCBF, the trajectory x(t) ∈C0 ∀t ≥0, if x(0) ∈C0. (b) In the
presence of wind disturbances, the conventional controller may lead to
collisions.
and ∂C0 ≜{x ∈Rn : b(x) = 0} is the boundary, and Int(C0) ≜
{x ∈Rn : b(x) > 0} is the nonempty interior. The system (1) is safe
with respect to the set C0, if there exists a control action u renders
the set C0 forward invariant, i.e., for each initial state x(0) ∈C0,
x(t) ∈C0 ∀t > 0. Then, the CBF is deﬁned as follows.
Deﬁnition 1 ([5]): Considering the system (1), a continuously dif-
ferentiable function b : Rn →R is a CBF, if there exists a positive
constant k0 subject to
sup
u∈Rm

Lfb(x) + Lgb(x)u + k0b(x)

≥0 ∀x ∈X
(3)
where Lf and Lg are standard Lie derivatives along f(x) and g(x).
Given a valid CBF b(x), if the initial states of system satisfy
x(0) ∈C0, then any Lipschitz continuous controller u(x) belonging
to KCBF ≜{u ∈Rm|Lfb(x) + Lgb(x)u ≥−k0b(x)} renders the
system (1) safe. The typical trajectory of system (1) satisfying (3) is
presented in Fig. 1(a).
B. System With Unmatched Disturbances
The considered nonlinear system (1) subject to external disturbances
d can be expressed as follows:
˙x = f(x) + g(x)u + d
(4)
where d = [d1, d2, . . . , dn]T are external disturbances. Deﬁne the
smooth function h : Rn →R as an output characterizing safety spec-
iﬁcation of system (4). When dealing with unmatched disturbances
like system (4), it is generally infeasible to completely reject their
effects [31]. However, it is possible to remove the inﬂuence of dis-
turbances from the h(x) [25]. Without loss of generality, it is supposed
that the equilibrium x0 of the system (4) without the disturbances is
the origin. The IRD to h(x) is deﬁned as follows.
Deﬁnition 2 ([31]): The relative degree from the control inputs
to the output h(x) is rI at the equilibrium x0 if LgjLk
f = 0 (j ∈
N1:m) for all k < rI −1 for all x in a neighborhood of x0, the
vector A(x) = [Lg1LrI−1
f
, Lg2LrI−1
f
, . . . , LgmLrI−1
f
]T has at least
one nonzero element. Here, gj is the jth row vector of g(x).
Similarly, the DRD to h(x) at x0 can be deﬁned as rD. It should
be noted that the CBF introduced above is an artiﬁcial output deﬁned
to characterise the safety speciﬁcation [32]. Thus, the CBF design
for the disturbed system (4) should account for the relationships be-
tween IRD and DRD. The following example illustrates this point
further.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:35:01 UTC from IEEE Xplore.  Restrictions apply.

## Page 3

2724
IEEE TRANSACTIONS ON AUTOMATIC CONTROL, VOL. 70, NO. 4, APRIL 2025
C. Motivating Example: Path Following of Drone
Consider the collision–avoidance path following of drone in the
horizontal plane as illustrated by Fig. 1(b), where (xs
p, ys
p) and (xf
p, yf
p)
are the start and end path points, respectively. In Fig. 1(b), the desired
path is shown as a red solid line. The standard safety-critical path,
generated by a conventional CBF-CLF-based controller, is the gray
dashed line. The robust safety-critical path, accounting for obstacles
and winds, is represented by a blue solid line.
The kinematics of the drone can be expressed as follows [33]:
˙px = Va cos ψ + dx, ˙py = Va sin ψ + dy
˙ψ = uψ
(5)
where px and py are the position of drone in the inertial frame, Va
represents its airspeed, ψ is the heading angle, uψ is the equivalent
control input driving the direction of drone, and dx and dy are the wind
disturbances. In this case, the drone is required to follow a desired path
while keeping a safe distance from some obstacles Oi, i ∈N. Despite
the path following task, the safety concern of obstacles is the high
priority of the mission. We can use the candidate CBFs bi(px, py) =
(px −xo,i)2 + (py −yo,i)2 −R2
o,i to interpret such safety speciﬁca-
tions, where xo,i, yo,i is the ith position of obstacle’s center and Ro,i is
its radius. To achieve the critical safety task, a control policy should be
designed to maintain the positiveness of bi(px(t), py(t)) ∀t > 0 when
bi(px(0), py(0)) ≥0 in the sense of CBF-based safety control. Then,
its time derivatives along the system (5) are
˙bi(px, py) = 2Va[(px −xo,i) cos ψ + (py −yo,i) sin ψ]
+ 2(px −xo,i)dx + 2(py −yo,i)dy
¨bi(px, py) = 2V 2
a + 2d2
x + 2d2
y + 2(px −xo,i) ˙dx + 2(py −yo,i)
˙dy + 2Va[(py −yo,i) cos ψ −(px −xo,i) sin ψ]uψ
+ 4Va(dx cos ψ + dy sin ψ).
(6)
Following from (6), it is evident that the DRD rD to bi(px, py) is less
than the IRD rI. This indicates that the wind disturbances dx, dy, and
their derivatives not only pollute the bi(px, py) via matched channel
but also alter its behavior from the unmatched channel, which can not
be solved by the current CBF-based control approaches. Especially, the
existences of 2(px −xo,i)dx and 2(py −yo,i)dy increase the difﬁculty
in design and analysis of robust CBF. This motivates us to design a new
CBF to actively reject the impacts on safety performance caused by
unmatched disturbances.
III. ROBUST SAFETY CONTROL DESIGN WITH UNMATCHED
DISTURBANCES
In this section, we will show the proposed robust safety control
solution under unmatched disturbances. Denote the b(x) as the can-
didate safe function for disturbed nonlinear system (4). To reduce the
complexity in analysis, we assume the external disturbances do not
change the control relative degree r ∈N of b(x), and suppose the high
order derivatives of b(x) can be expressed as follows:
b(i)(x) = αi(x) + βi(x, d, ˙d, . . . , d(i−1)), i ∈N1:r−1
b(r)(x) = αr(x) + βu(x)u + βr(x, d, ˙d, . . . , d(r−1))
(7)
where αi : Rn →R, βi : Rn × ¯Di−1 →R, in which ¯Di−1 ≜D0 ×
D1 × · · · × Di−1, and βu : Rn →Rm is a 1 × m raw vector satisfying
βu(x) ̸= 0 ∀x ∈X. The sets Di, i ∈N0:r−1 are denoted as the com-
pact sets of external disturbance vector d and their derivatives d(i). It
is important to mention that a large number of nonlinear systems meet
the condition stated in (7), e.g., the single-input-single-output lower
triangular nonlinear systems.
The external disturbances di considered in this article are assumed
to satisfy the following assumption.
Assumption 1: The disturbances di, i ∈N1:n are differentiable and
there exists a set of known positive real numbers δi,j ∈R+, j ∈N0:n
that |d(j)
i (t)| ≤δi,j ∀t ≥0.
Remark 1: The disturbances considered in this study encompass
most of the common types that occur in various systems, such as
constant, sinusoidal, and polynomial signals.
The nonlinear functions βi(x, d, ˙d, . . . , d(i−1)), i ∈N1:r are also
supposed to satisfy the following assumption.
Assumption 2: There exist known strictly increasing positive func-
tions γi(x) and ˜γi(y), i ∈N1:r such that for all x ∈X, yj, ˆyj ∈
¯Dj, j ∈N0:i−1, the following inequalities hold:
|βi(x, y0, . . . , yj−1) −βi(x, ˆy0, . . . , ˆyj−1)| ≤γi(x)˜γi([˜yT
0
˜yT
1 , . . . , ˜yT
j−1]T )
(8)
where ˜yj = yj −ˆyj.
Remark 2: Due to the wide range of mission-based safety
speciﬁcations described by b(x), exhibiting a uniform formulation of
βi(x, d, ˙d, . . . , d(i−1)) is a difﬁcult task. To reduce the complexity
and present the key idea of rejecting unmatched disturbances,
the above Assumption is made. Actually, the nonlinear functions
βi(x, d, ˙d, . . . , d(i−1)) satisfying Assumption 2 enclose a large
set of possible nonlinear functions of disturbances, e.g., d2
1 and
d1d2. For d2
1, it is obtained that d2
1 −ˆd2
1 = (d1 + ˆd1)(d1 −ˆd1) ≤
2 max{ ¯d1, | ˆd1|}|d1 −ˆd1|; for d1d2, it is obtained that d1d2 −ˆd1 ˆd2 =
d1d2−d1 ˆd2+d1 ˆd2−ˆd1 ˆd2 ≤2 max{ ¯d1, | ˆd2|}

(d1−ˆd1)2+(d2−ˆd2)2.
In the following, we will ﬁrst introduce the design of disturbance
observers and the corresponding quantiﬁcation mechanism of the esti-
mation errors. With those in mind, the proposed DRCBF is designed
under unmatched disturbances. Finally, an optimization-based robust
control policy is formulated by integrating with the technique of ISS-
CLF.
A. Disturbance Observer Design and Estimation Error
Quantiﬁcation
Considering the system (4), the disturbance observers employed
from [34] are constructed as follows:
˙ξi = A(ξi + Lixi) −Li[fi(x) + gi(x, u) + C(ξi + Lixi)]
ˆwi = ξi + Lixi
(9)
where fi(x), gi(x, u) are the ith component of f(x) and g(x)u,
ξi ∈Rn is the auxiliary state, A =

0
In−1
0
0

, C = [1, 0, . . . , 0], and
Li ∈Rn×1 is the parameter vector to be designed.
Denote ˆwi = [ ˆwi,0, ˆwi,1, . . . , ˆwi,n−1]T as the estimate vector of
disturbance di and its time-derivatives, and deﬁne the estimation error
ei = wi −ˆwi, where wi ≜[di, ˙di, . . . , d(n−1)
i
]T . Combining (4) and
(9), its dynamics is expressed as
˙ei = ¯
Aiei + σi
(10)
where ¯
Ai = A −LiC and σi = [0, 0, . . . , d(n)
i
]T . By selecting a
proper gain matrix Li, the ¯
Ai is Hurwitz. Then, the system (10) is
input-to-state stable with respect to the σi under Assumption 1.
Assuming the ¯
Ai has n independent eigenvalues λi,j, j ∈N1:n,
there exists an invertible matrix P i such that P −1
i
¯
AiP i = Λi with
Λi ≜diag(λi,1, . . . , λi,n). Moreover, by setting zero initial condition
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:35:01 UTC from IEEE Xplore.  Restrictions apply.

## Page 4

IEEE TRANSACTIONS ON AUTOMATIC CONTROL, VOL. 70, NO. 4, APRIL 2025
2725
of ˆwi(0) and considering Assumption 1, its solution can be overesti-
mated by the following estimation error bound εi(t):
|ei(t)| ≤|e
¯
Aitei(0) +
 t
0
e
¯
Ai(t−τ)σi(τ)dτ|
≤|P ieΛitP −1
i |¯δi(0) + |P i|
 t
0
|eΛi(t−τ)|dτ|P −1
i |¯δi,σ
= |P ieΛitP −1
i |¯δi(0) −|P i||Λ−1
i eΛit||P −1
i |¯δi,σ
+ |P i||Λ−1
i ||P −1
i |¯δi,σ
≜εi(t)
(11)
where ¯δi(0) = [δi,0, δi,1, . . . , δi,n−1]T and ¯δi,σ = [0, . . . , δi,n]T . It
should be noted that the error quantiﬁcation proposed in (11) will
unavoidably experience a dramatic change in the transient phase since
the high order derivatives of the disturbance di are required to be
estimated. To address this issue, the following new error quantiﬁcation
mechanism is proposed. Based on Assumption 1, we ﬁrst deﬁne the
following saturated disturbance estimates:
ˆwsat
i,j = satδi,j( ˆwi,j)
(12)
where i ∈N1:n, j ∈N0:n−1. With (11) in mind, we further deﬁne the
following saturated estimation error bounds:
εsat
i,j = sat2δi,j(εi,j)
(13)
where εi,j is the corresponding component of the error bound vector
εi. The following theorem is concluded to show the elegant properties
of the proposed error quantiﬁcation approach.
Theorem 1: Under Assumption 1, if the ¯
Ai is Hurwitz with n
independent eigenvalues, then the errors between d(j)
i , i ∈N1:n, j ∈
N0:n−1 and the saturated estimates ˆwsat
i,j satisfy |d(j)
i
−ˆwsat
i,j | ≤εsat
i,j .
Proof: In the following, we will demonstrate that the saturated
estimation error bound (13) is able to quantify the difference between
d(j)
i
and the saturated estimates ˆwsat
i,j .
Under Assumption 1, it is clear that |d(j)
i
−ˆwsat
i,j | ≤2δi,j. If |ei,j| >
2δi,j, due to the fact that εi,j ≥ei,j, it is obtained that εsat
i,j = 2δi,j.
Then, we have |d(j)
i
−ˆwsat
i,j | ≤εsat
i,j when |ei,j| > 2δi,j.
If |ei,j| ≤2δi,j, it is clear that |d(j)
i
−ˆwi,j| ≤2δi,j. Since the dis-
turbance di and its derivatives satisfy Assumption 1, it is obtained that
| ˆwi,j| ≤δi,j, which means ˆwi,j = ˆwsat
i,j . Then, the following inequality
holds:
|d(j)
i
−ˆwsat
i,j | = |d(j)
i
−ˆwi,j| ≤εsat
i,j .
(14)
Therefore, the value of |d(j)
i
−ˆwsat
i,j | is less than the saturated error
bound εsat
i,j whose maximum value is not greater than 2δi,j. This
completes the proof.
■
From the above analysis, the saturated bound (13) is able to quantify
the impacts caused by estimation error |d(j)
i
−ˆwsat
i,j |. Specially, its
transient value is no more than twice the bound of disturbance, and
the steady value can be adjusted by choosing the observer parameter
matrix Li. In the next section, the saturated estimates ˆwsat
i,j will be used
to compensate for the impacts to safety caused by the disturbances, and
the εsat
i,j will be used to quantify the errors between d(j)
i
and ˆwsat
i,j .
Remark 3: Based on the above analysis, the proposed disturbance
observer can accurately estimate a wide range of disturbances with
sufﬁciently small estimation errors. However, it should be highlighted
that if the disturbance d can be described by a known exogenous
system as proposed in [34], then the estimation error will exponentially
converge to zero.
B. Disturbance Rejection CBF Design
Now, we are able to show the proposed robust safety control ap-
proach. Let η0(x) = b(x) and deﬁne a series of disturbance-dependent
auxiliary functions for ∀i ∈N2:r−1
η1(x, d) =
 d
dt + p1

η0(x)
ηi(x, d, . . . , d(i−1)) =
 d
dt + pi

ηi−1(x, d, . . . , d(i−2))
ηr(x, u, d, . . . , d(r−1)) =
 d
dt + pr

ηr−1(x, d, . . . , d(r−2))
(15)
with positive constants pj, j ∈N1:r, and following 0-superlevel sets
Ci ≜{(x, d, . . . , d(i−1)) ∈Rn × ¯Di−1 : ηi ≥0, i ∈N1:r−1}.
(16)
From (7) and (15), ηi(x, d, . . . , d(i−1)) can be expressed as
ηi(x, . . . , d(i−1)) =
i

j=1
kj[αj(x) + βj(x, . . . , d(i−1))] + k0b(x)
(17)
where kj, j ∈N0:i
are the parameters
of polynomial
kjsi +
kj−1si−1 + . . . + k1s + k0 with negative eigenvalues −p1, . . . , −pi.
Deﬁning the estimation vectors ˆd
(i)
sat = [ ˆwsat
1,i , ˆwsat
2,i , . . . , ˆwsat
n,i]T from
(12), it is obtained that
ηi =
i

j=1
kjαj(x) +
i

j=1
kjβj(x, ˆdsat, . . . , ˆd
(j−1)
sat
) + k0b(x)
+
i

j=1
kj[βj(x, d, . . . , d(j−1)) −βj(x, ˆdsat, . . . , ˆd
(j−1)
sat
)].
(18)
Deﬁne ϖj = [εsat
1,0, . . . , εsat
1,j−1, . . . , εsat
n,0, . . . , εsat
n,j−1]T . Based on the
Theorem 1 and Assumption 2, the following estimates hold:
ηi ≥
i

j=1
kjαj(x) +
i

j=1
kjβj(x, ˆdsat, . . . , ˆd
(j−1)
sat
) + k0b(x)
−
i

j=1
kjγj(x)˜γj(ϖj)
= ηi(x, ˆdsat, . . . , ˆd
(i−1)
sat
) −μi(x, ϖ1, . . . , ϖi)
(19)
where μi(x, ϖ1, . . . , ϖi) = 	i
j=1 kjγj(x)˜γj(ϖj). Then, we can
conclude the following DRCBF.
Deﬁnition 3: Consider the system (4) and the disturbance observers
(9) with Assumption 1, and the sets Ci (16). A continuously differen-
tiable function b : Rn →R in (7) is a DRCBF of relative degree r, if
there exist positive constants kj, j ∈N1:r deﬁned in (17), subject to
sup
u∈Rm

r

j=1
kj[αj + βj(x, . . . , ˆd
(j−1)
sat
)] + k0b(x) + βuu



ηr(x,u,ˆdsat,...,ˆd(r−1)
sat
)

≥μr(x, ϖ1, . . . , ϖr)
(20)
for all (x, d, . . . , d(r−2)) ∈¯
C ≜r−1
i=0 Ci.
Theorem 2: Given a DRCBF and well-designed disturbance
observers (9), if the initial values of ηi(x, ˆdsat, . . . , ˆd
(i−1)
sat
) −
μi(x, ϖ1, . . . , ϖi), i ∈N0:r−1 are positive, then any Lipschitz
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:35:01 UTC from IEEE Xplore.  Restrictions apply.

## Page 5

2726
IEEE TRANSACTIONS ON AUTOMATIC CONTROL, VOL. 70, NO. 4, APRIL 2025
Fig. 2.
Control block of the disturbance rejection CBF-based safety-
critical control.
continuous controller u(t, x, ˆdsat, . . . , ˆd
(r−1)
sat
) ∈KDRCBF ≜{u ∈
Rm| 	r
j=1 kj[αj(x) + βj(x, ˆdsat, . . . , ˆd
(j−1)
sat
)]+ k0b(x)+βu(x)u
≥μr(x, ϖ1, . . . , ϖr)} renders the set ¯
C forward invariant for the
disturbed system (4).
Proof: First, since ηi(x(0), ˆdsat(0), . . . , ˆd
(i−1)
sat
(0)) −μi(x(0),
ϖ1(0), . . . , ϖi(0)), i ∈N1:r−1 are positive, it can be obtained
from
(19)
that
ηi(x(0), . . . , d(i−1)(0)) ≥0,
i.e.,
[xT (0), . . . ,
d(i−1)T ]T ∈Ci. Since there exists a Lipschitz continuous controller
u(t, x, ˆdsat, . . . , ˆd
(r−1)
sat
) ∈KDRCBF, it can be obtained that ηr(x, u,
. . . , d(r−1)) ≥ηr(x, u, . . . , ˆd
(r−1)
sat
)−μr(x, ϖ1, . . . , ϖr)≥0. From
(15), we have ˙ηr−1(x . . . , d(r−2)) = −prηr−1(x, d, . . . , d(r−2)) +
ηr(x, u, d, . . . , d(r−1)) such that the set Cr−1 is forward invariant.
Then, the forward invariance of Cr−2 can also be guaranteed for that
of Cr−1 and [xT (0), dT (0), . . . , d(r−3)T (0)]T ∈Cr−2. Therefore,
following a recursive analysis from the forward invariance of Cr−1
to that of C0, the forward invariant property of set ¯
C can be achieved
such that the strict safety constraint is guaranteed. This completes the
proof.
■
C. Optimization-Based Robust Safety Control With DRCBF
Based on the results of Theorem 2, the robust safety speciﬁcation
described by ¯
C can be guaranteed via a Lipschitz continuous controller
u(t, x, ˆdsat, . . . , ˆd
(r−1)
sat
) ∈KDRCBF. In order to achieve the safety
and stability tasks simultaneously, one possible way is to construct a
quadratic programming (QP) by combining the proposed DRCBF and
a well-designed CLF for the control task. In this article, the ISS-CLF
proposed in [30] is used. Suppose there is a positive deﬁnite function
V : Rn →R+ for the control objective of the disturbed system (4),
then the following DRCBF-based quadratic program (DRCBF QP) is
designed
arg min
(u,δ)∈Rm×R
1
2uT u + m
2 δ2,
DRCBF QP
s.t. ϕ0(x, . . . , ˆd
(r−1)
sat
) + ϕ1(x)u −μr(x, . . . , ϖr) ≥0
φ0(x, ˆd) + φ1(x)u + 1
ϵ ∥∂V (x)
∂x
∥2 ≤−cV + δ
(21)
where ϕ0 = 	r
j=1 kj[αj(x) + βj(x, . . . , ˆd
(j−1)
sat
)] + k0b(x), ϕ1 =
βu(x), and φ0 = LfV (x) + ∂V (x)
∂x
ˆd, φ1 = LgV (x), c, ϵ are positive
constants to be selected. A slack variable δ is introduced to make
the above optimization problem feasible, and m > 0 is the weight of
the cost function to regulate the amplitude of δ. The schematic block
of the proposed robust safety-critical control approach is presented in
Fig. 2.
In the following, we will show that a Lipschitz continuous controller
can be obtained by solving the DRCBF QP.
Theorem 3: Suppose the functions φ0(x, ˆd) + 1
ϵ ∥∂V (x)
∂x ∥2, φ1(x),
αi(x), βi(x, d, . . . , d(i−1)), βu(x), γi(x), and ˜γi(ϖ), i ∈N1:r are
all locally Lipschitz continuous in state x and continuous in t. Then,
the solution of DRCBF-QP is locally Lipschitz continuous in x and
continuous in t.
The Lipschitz continuity analysis can be discussed following the
results in [5] and [13]. For the sake of completeness of this article, the
proof is given in the Appendix.
IV. APPLICATION TO PATH FOLLOWING OF DRONE WITH WIND
DISTURBANCES
In this section, we consider a surveillance task for drone within a
speciﬁed safety region, which demands close-range observation of an
interesting area and collision avoidance from the region borders. To
this end, a periodic patrol path is designed as the desired path, which is
given by
pc
x(θ) = 10θ −220, pc
y(θ) = −50 sin(0.25θ)
(22)
where θ ∈[θ, ¯θ] is the path parameter, and θ, ¯θ represent its minimum
and maximum, respectively. By augmenting a virtual control uθ to
adjust the dynamics of path parameter θ, it is obtained that
˙px = Va cos ψ + dx, ˙py = Va sin ψ + dy, ˙ψ = uψ
˙θ1 = θ2, ˙θ2 = uθ
(23)
where θ1 = θ and θ2 = ˙θ. We assume there exist known positive
constants δi,0, δi,1, and δi,2 satisfying |di(t)| ≤δi,0, | ˙di(t)| ≤δi,1 and
| ¨di(t)| ≤δi,2, i = {x, y}. Based on the disturbance observer (9), the
following disturbance observers are constructed:
˙ξx,0 = ξx,1 + l2px −l1(Va cos ψ + ξx,0 + l1px)
˙ξx,1 = −l2(Va cos ψ + ξx,0 + l1px)
˙ξy,0 = ξy,1 + l2py −l1(Va sin ψ + ξy,0 + l1py)
˙ξy,1 = −l2(Va sin ψ + ξy,0 + l1py)
(24)
where ˆwx,0 = ξx,0 + l1px, ˆwy,0 = ξy,0 + l1py, ˆwx,1 = ξx,1 + l2px,
and ˆwy,1 = ξy,1 + l2py are the winds and their derivative estimates,
and l1 and l2 are observer parameters to be designed. Following the
proposed estimation error quantiﬁcation mechanism (12) and (13), we
denote ˆwsat
x,0, ˆwsat
y,0, ˆwsat
x,1, ˆwsat
y,1 and εsat
x,0, εsat
y,0, εsat
x,1, εsat
y,1 as the saturated
estimates and proposed error bounds, respectively.
A. ISS-CLF-Based Path Following Controller Design
Deﬁning the path following errors as z1 = px −pc
x, z2 =
Va cos ψ −∂pcx
∂θ θ2, z3 = py −pc
y and z4 = Va sin ψ −
∂pcy
∂θ θ2, the
tracking error dynamics is expressed as follows:
˙z1 = z2 + dx
˙z2 = −Va sin ψuψ −∂pc
x
∂θ uθ −∂2pc
x
∂θ2 θ2
2 + ˙dx
˙z3 = z4 + dy
˙z4 = Va cos ψuψ −∂pc
y
∂θ uθ −∂2pc
y
∂θ2 θ2
2 + ˙dy.
(25)
With the help of disturbance estimates, we deﬁne ˆ
Z = [z1, z2 +
ˆwx,0, z3, z4 + ˆwy,0]T , then it is obtained that
˙ˆ
Z = A ˆ
Z + ˆ
F + F ε + BGv
(26)
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:35:01 UTC from IEEE Xplore.  Restrictions apply.

## Page 6

IEEE TRANSACTIONS ON AUTOMATIC CONTROL, VOL. 70, NO. 4, APRIL 2025
2727
Fig. 3.
Path proﬁles of drone under the baseline, the DRCBF and the robust path following controllers in the presence of wind disturbances.
with
A =
⎡
⎢⎢⎢⎣
0
1
0
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
0
⎤
⎥⎥⎥⎦, B =
⎡
⎢⎢⎢⎣
0
0
1
0
0
0
0
1
⎤
⎥⎥⎥⎦, G =

−Va sin ψ
−∂pcx
∂θ
Va cos ψ
−
∂pcy
∂θ

(27)
where
v = [uψ, uθ]T ,
ˆ
F = [0, −∂2pcx
∂θ2 θ2
2 + ˆwx,1, 0, −∂2pcx
∂θ2 θ2
2 +
ˆwy,1]T , and F ε = [εx,0, l1εx,0, εy,0, l1εy,0]T is the estimation error
vector.
Based on the works in [30] and [35], we can deﬁne V = ˆ
Z
T P ˆ
Z
as the ISS-CLF for error system (26), where the symmetric positive
deﬁnite matrix P can be determined by solving the Riccati equation
AT P + P A −2P BBT P + Q = 0 with a positive deﬁnite matrix
Q. Then, the path following controller with disturbance estimates is
formulated as the following QP:
arg min
v∈R2
1
2vT v,
Path following QP
s.t.
φ0( ˆ
Z, ˆ
wx, ˆ
wy) + φ1( ˆ
Z)v + 1
ϵ ∥2 ˆ
Z
T P ∥2 ≤−cV
(28)
where φ0( ˆ
Z, ˆ
wx, ˆ
wy)= ˆ
Z
T (AT P + P A) ˆ
Z+2 ˆ
Z
T P ˆ
F and φ1( ˆ
Z)
= 2 ˆ
Z
T P BG, and ˆ
wx = [ ˆwx,0, ˆwx,1]T , ˆ
wy = [ ˆwy,0, ˆwy,1]T .
B. Safety-Critical Path Following Controller Design
Inthis scenario,thesafetyregionisconsideredas−xb ≤x ≤xb and
−yb ≤y ≤yb with xb = 230, yb = 40, and the collision avoidance
speciﬁcations are interpreted by the following two pair sharing con-
trol barrier functions [6] as bx,1(px) = xb + px, bx,2(px) = xb −px,
by,1(py) = yb + py and by,2(py) = yb −py. Based on the proposed
DRCBF in (21) and the ISS-CLF-based controller in (28), the proposed
robust safety-critical path following controller is formulated as the
following QP problem:
arg min
(v,δ)∈R2×R
1
2vT v + m
2 δ2,
DRCBF Path Following
s.t. ϕ0
x,i(ψ, ˆ
wsat
x ) + ϕ1
x,i(ψ)v −μx(εsat
x ) ≥0
ϕ0
y,i(ψ, ˆ
wsat
y ) + ϕ1
y,i(ψ)v −μy(εsat
y ) ≥0, i ∈N1:2
φ0( ˆ
Z, ˆ
wx, ˆ
wy) + φ1( ˆ
Z)v + 1
ϵ ∥2 ˆ
Z
T P ∥2 ≤−cV + δ (29)
Fig. 4.
Control input curves of drone under DRCBF path following
controller: (a) control inputs uθ and uψ; (b) slack variable δ.
with
ϕ0
x,1 = k1Va cos ψ + k0bx,1 + k1 ˆwsat
x,0 + ˆwsat
x,1
ϕ0
x,2 = −k1Va cos ψ + k0bx,2 −k1 ˆwsat
x,0 −ˆwsat
x,1
ϕ0
y,1 = k1Va sin ψ + k0by,1 + k1 ˆwsat
y,0 + ˆwsat
y,1
ϕ0
y,2 = −k1Va sin ψ + k0by,2 −k1 ˆwsat
y,0 −ˆwsat
y,1
μx = k1εsat
x,0 + εsat
x,1 , μy = k1εsat
y,0 + εsat
y,1
(30)
where εsat
x
= [εsat
x,0, εsat
x,1]T , εsat
y
= [εsat
y,0, εsat
y,1]T , ϕ1
x,1 = [−Va sin ψ,
0], ϕ1
x,2 = −ϕ1
x,1, ϕ1
y,1 = [Va cos ψ, 0], ϕ1
y,2 = ϕ1
y,1, and k0 and k1
are parameters to be designed for the DRCBF.
C. Simulation Results
The initial states of drone are px(0) = −220 m, py(0) = 0 m,
ψ(0) = −π
60 rad, and the initial conditions of θ are θ(0) =
π
16, ˙θ(0) =
0.1. The airspeed of drone is Va = 15m/s. The external winds dx and
dy are set as dx = 3.5 cos(0.5t) m/s and dy = 6 cos(0.5t) m/s. The
observer parameters are set as l1 = 100 and l2 = 2400 and the bounds
of external wind disturbances are assumed as δx,0 = 4, δy,0 = 7,
δx,1 = 3, δy,1 = 4.5, and δx,2 = 2, δy,2 = 3. The disturbances are
introduced to the system at the start and removed once x(t) ≥0.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:35:01 UTC from IEEE Xplore.  Restrictions apply.

## Page 7

2728
IEEE TRANSACTIONS ON AUTOMATIC CONTROL, VOL. 70, NO. 4, APRIL 2025
Fig. 5.
Trajectories of CBFs under DRCBF path following controller:
(a) CBFs in X-axis; (b) CBFs in Y -axis.
The control parameters are selected as Q = diag([4, 1, 1, 1]T), ϵ = 1,
c = 5, m = 0.01 and k0 = 16, k1 = 8.
In the following, to further exhibit its safety robustness against
unmatched disturbances and the feature of performance recovery, the
proposed controller is compared with the baseline CLF-CBF-based
controller without disturbance consideration proposed in [5] and the
robust CLF-CBF-based one using the conservative overapproximate
bounds of external disturbances proposed in [14]. The robust safety
controller with worst-case disturbances is designed as follows:
arg min
(v,δ)∈R2×R
1
2vT v + m
2 δ2,
Robust Path Following
s.t. ¯ϕ0
x,i(ψ) + ϕ1
x,i(ψ)v −ςx(ψ, δx,0, δx,1) ≥0
¯ϕ0
y,i(ψ) + ϕ1
y,i(ψ)v −ςy(ψ, δy,0, δy,1) ≥0, i ∈N1:2
ψ0(Z) + ψ1(Z)v + |2ZT P F δ| ≤−cV + δ
(31)
with
¯ϕ0
x,1 = k1Va cos ψ + k0bx,1, ¯ϕ0
x,2 = −k1Va cos ψ + k0bx,2
¯ϕ0
y,1 = k1Va sin ψ + k0by,1, ¯ϕ0
y,2 = −k1Va sin ψ + k0by,2
ςx = k1δx,0 + δx,1, ςy = k1δy,0 + δy,1
ψ0 = ZT (AT P + P A)Z + 2ZT P F
(32)
where Z = [z1, z2, z3, z4]T , F = [0, −∂2pcx
∂θ2 θ2
2, 0, −∂2pcx
∂θ2 θ2
2]T , and
ψ1(Z) = 2ZT P BG and F δ = [δx,0, δx,1, δy,0, δy,1]T .
The path following results under different controllers are shown
in Fig. 3, where we present the path following performances in the
horizontal plane with wind disturbances. It can be seen that the baseline
controller can not prevent drone from crossing the safety boundary
when there exists external wind disturbances. It is worth pointing out
that the proposed approach achieves a strict safety guarantee as well as
the nominal control performance, regardless of the presence of distur-
bances. In contrast, the robust approach results in overly conservative
safety performances as the drone is approaching the boundary due to
the use of worst-case disturbances. In Fig. 4, the trajectories of control
inputs uψ and uθ, and slack variable δ are shown, where the slack
variable keeps in a relatively small value when there is no conﬂict
between the safety and stability tasks. The trajectories of bxi(px) and
byi(py) presented in Fig. 5 indicate that the safety speciﬁcations are
achieved. Meanwhile, the disturbances and their estimates are shown
in Fig. 6, which demonstrates that the proposed error quantiﬁcation
mechanism achieves accurate and less conservative over-estimation
performances.
Fig. 6.
Estimation error quantiﬁcation performance of the wind dis-
turbances: (a) estimation errors of wx; (b) estimation errors of wy;
(c) estimation errors of ˙wx; (d) estimation errors of ˙wy.
V. CONCLUSION
In this article, inspired by the collision avoidance path following
of drone with wind disturbances, where the winds directly impact
the dynamics of CBF from the different channels of control input, a
disturbance observer-based DRCBF has been developed for a class
of nonlinear systems with unmatched disturbances. To achieve strict
safety speciﬁcations and satisfactory control performances under un-
matched disturbances, an optimization-based control scheme has been
proposed based on the techniques of DRCBF and ISS-CLF. It has
been demonstrated via the path following of drone that the proposed
method achieves the prescribed safety speciﬁcation without sacriﬁcing
the nominal control performances.
APPENDIX
Proof: We ﬁrst consider the solution of the proposed optimisation
program. The Lagrangian function of DRCBF QP is illustrated as
follows:
L = 1
2uT u + m
2 δ2 + λ1[a1(x)u + b1(x, ˆdsat, . . . , ˆd
(r−1)
sat
ϖ1, . . . , ϖr)] + λ2[a2(x)u −δ + b2(x, ˆd)]
(33)
where a1(x)=−ϕ1(x), b1(x, . . . , ˆd
(r−1)
sat
, . . . , ϖr)=−ϕ0(x, ˆdsat,
. . . , ˆd
(r−1)
sat
) + μr(x, ϖ1, . . . , ϖr),
a2(x) = φ1(x),
b2(x, ˆd) =
φ0(x, ˆd) + 1
ϵ ∥∂V (x)
∂x ∥2 + cV (x),
and
λi, i = {1, 2}
are
scalar
Lagrange multipliers. For brevity, the arguments of ai, bi, i ∈N1:2
are omitted. By applying the Karush–Kuhn–Tucker condition in [36],
the explicit control laws can be obtained under four cases where
different constraints are active.
Case 1: Both the safety and stability constraints are inactive (λ1 = 0,
λ2 = 0). Then, the solution of the optimization program is given by
u = 0, δ = 0.
(34)
The
region
in
which
the
above
solution
applies
is
Ω1 :=
{(t, x, ˆd, ˆdsat, . . . , ˆd
(r−1)
sat
) ∈R+ × X × Rn × ¯Dr−1 : b1 ≤0, b2 ≤
0}.
Case 2: Only the safety constraint is active (λ1 ≥0, λ2 = 0), and
the solution is given by
u = −
b1
∥a1∥2 aT
1 , δ = 0
(35)
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:35:01 UTC from IEEE Xplore.  Restrictions apply.

## Page 8

IEEE TRANSACTIONS ON AUTOMATIC CONTROL, VOL. 70, NO. 4, APRIL 2025
2729
where the solution applies is Ω2 := {(t, x, ˆd, ˆdsat, . . . , ˆd
(r−1)
sat
) ∈
R+ × X × Rn × ¯Dr−1 : b1 ≥0, b2 ≤
a2b1
∥a1∥2 aT
1 }.
Case 3: Only the stability constraint is active, while the safety
constraint is inactive (λ1 = 0, λ2 ≥0). The relative optimal solution is
u = −
mb2
1 + m∥a2∥2 aT
2 , δ =
b2
1 + m∥a2∥2 .
(36)
The above solution holds in Ω3 := {(t, x, ˆd, ˆdsat, . . . , ˆd
(r−1)
sat
) ∈
R+ × X × Rn × ¯Dr−1 : b1 ≤
ma1b2
1+m∥a2∥2 aT
2 , b2 ≥0}.
Case 4: Both the safety and stability constraints are active (λ1 ≥0,
λ2 ≥0), and we can obtain the following solution:
u = −[(∥a2∥2 + 1/m)b1 −a1aT
2 b2]aT
1 −(∥a1∥2b2 −a2aT
1 b1)aT
2
∥a1∥2(∥a2∥2 + 1/m) −∥a1aT
2 ∥2
δ =
∥a1∥2b2 −a2aT
1 b1
m∥a1∥2(∥a2∥2 + 1/m) −m∥a1aT
2 ∥2
(37)
where the solution applies is Ω4 := {(t, x, ˆd, ˆdsat, . . . , ˆd
(r−1)
sat
) ∈
R+ × X × Rn × ¯Dr−1 : b2 ≥
a2b1
∥a1∥2 aT
1 , b1 ≥
a1b2
∥a2∥2+1/maT
2 , b1 >
0, b2 > 0}.
It can be veriﬁed that the functions a0, a1, b1, and b2 are all
locally Lipschitz continuous functions x and continuous in t, since
the functions φ0 + 1
ϵ ∥∂V (x)
∂x ∥2, φ1, αi, βu, γi, and ˜γi are all locally
Lipschitz continuous in state x and continuous in t. Due to the fact
that βu(x) ̸= 0, then following a similar analysis proceed in [5] and
[13], the proposed control law is locally Lipschitz continuous in x and
continuous in t. This completes the proof.
■
REFERENCES
[1] U. Ozguner, C. Stiller, and K. Redmill, “Systems for safety and au-
tonomous behavior in cars: The darpa grand challenge experience,” Proc.
IEEE, vol. 95, no. 2, pp. 397–412, Feb. 2007.
[2] A. D. Ames, J. W. Grizzle, and P. Tabuada, “Control barrier function based
quadratic programs with application to adaptive cruise control,” in Proc.
IEEE Conf. Decis. Control, 2014, pp. 6271–6278.
[3] L. Wang, A. D. Ames, and M. Egerstedt, “Safety barrier certiﬁcates for
collisions-free multirobot systems,” IEEE Trans. Robot., vol. 33, no. 3,
pp. 661–674, Jun. 2017.
[4] A. M. Zanchettin, N. M. Ceriani, P. Rocco, H. Ding, and B. Matthias,
“Safety in human-robot collaborative manufacturing environments: Met-
ricsandcontrol,”IEEETrans.Autom.Sci.Eng.,vol.13,no.2,pp. 882–893,
Apr. 2015.
[5] A. D. Ames, X. Xu, J. W. Grizzle, and P. Tabuada, “Control barrier function
based quadratic programs for safety critical systems,” IEEE Trans. Autom.
Control, vol. 62, no. 8, pp. 3861–3876, Aug. 2017.
[6] X. Xu, “Constrained control of input-output linearizable systems using
control sharing barrier functions,” Automatica, vol. 87, pp. 195–201, 2018.
[7] M.Jankovic,“Robustcontrolbarrierfunctionsforconstrainedstabilization
of nonlinear systems,” Automatica, vol. 96, pp. 359–367, 2018.
[8] W. Xiao and C. Belta, “High order control barrier functions,” IEEE Trans.
Autom. Control, vol. 67, no. 7, pp. 3655–3662, Jul. 2022.
[9] S.-C. Hsu, X. Xu, and A. D. Ames, “Control barrier function based
quadratic programs with application to bipedal robotic walking,” in Proc.
Amer. Control Conf., 2015, pp. 4542–4548.
[10] A. D. Ames et al., “Control barrier functions: Theory and applications,”
in Proc. Eur. Control Conf., 2019, pp. 3420–3431.
[11] W. Xiao, C. G. Cassandras, and C. A. Belta, “Bridging the gap between
optimal trajectory planning and safety-critical control with applications to
autonomous vehicles,” Automatica, vol. 129, 2021, Art. no. 109592.
[12] Q. Nguyen and K. Sreenath, “Exponential control barrier functions for
enforcing high relative-degree safety-critical constraints,” in Proc. Amer.
Control Conf., 2016, pp. 322–328.
[13] X. Xu, P. Tabuada, J. W. Grizzle, and A. D. Ames, “Robustness of control
barrier functions for safety critical control,” IFAC-PapersOnLine, vol. 48,
no. 27, pp. 54–61, 2015.
[14] Q. Nguyen and K. Sreenath, “Robust safety-critical control for dynamic
robotics,” IEEE Trans. Autom. Control, vol. 67, no. 3, pp. 1073–1088,
Mar. 2021.
[15] E. D. Sontag and Y. Wang, “On characterizations of the input-to-state
stability property,” Syst. Control Lett., vol. 24, no. 5, pp. 351–359, 1995.
[16] A. Alan, A. J. Taylor, C. R. He, G. Orosz, and A. D. Ames, “Safe controller
synthesis with tunable input-to-state safe control barrier functions,” IEEE
Contr. Syst. Lett., vol. 6, pp. 908–913, Jun. 2021.
[17] W.-H. Chen, D. J. Ballance, P. J. Gawthrop, and J. O’Reilly, “A nonlinear
disturbanceobserverforroboticmanipulators,”IEEETrans.Ind.Electron.,
vol. 47, no. 4, pp. 932–938, Aug. 2000.
[18] W.-H. Chen, J. Yang, L. Guo, and S. Li, “Disturbance-observer-based
control and related methods—An overview,” IEEE Trans. Ind. Electron.,
vol. 63, no. 2, pp. 1083–1095, Feb. 2015.
[19] E. Da¸s and R. M. Murray, “Robust safe control synthesis with disturbance
observer-based control barrier functions,” in Proc. Conf. Decis. Control,
2022, pp. 5566–5573.
[20] A. Alan, T. G. Molnar, E. Das, A. D. Ames, and G. Orosz, “Disturbance
observers for robust safety-critical control with control barrier functions,”
IEEE Contr. Syst. Lett., vol. 7, pp. 1123–1128, Dec. 2022.
[21] J. Sun, J. Yang, and Z. Zeng, “Safety-critical control with control barrier
function based on disturbance observer,” IEEE Trans. Autom. Control,
vol. 69, no. 7, pp. 4750–4756, Jul. 2024.
[22] J. Chen, Z. Gao, and Q. Lin, “Robust control barrier functions for safe
control under uncertainty using extended state observer and output mea-
surement,” in Proc. IEEE Conf. Decis. Control, 2023, pp. 8477–8482.
[23] V. Hamdipoor, N. Meskin, and C. G. Cassandras, “Safe control synthesis
using environmentally robust control barrier functions,” Eur. J. Control,
vol. 74, 2023, Art. no. 100840.
[24] S. Li, J. Yang, W.-H. Chen, and X. Chen, “Generalized extended state
observer based control for systems with mismatched uncertainties,” IEEE
Trans. Ind. Electron., vol. 59, no. 12, pp. 4792–4802, Dec. 2012.
[25] J. Yang, W.-H. Chen, and S. Li, “Nonlinear disturbance observer-based
robust control for systems with mismatched disturbances/uncertainties,”
IET Control Theory Appl., vol. 5, no. 18, pp. 2053–2062, 2011.
[26] J. Yang, C. Liu, M. Coombes, Y. Yan, and W.-H. Chen, “Optimal path
following for small ﬁxed-wing UAVs under wind disturbances,” IEEE
Trans. Control Syst. Technol., vol. 29, no. 3, pp. 996–1008, May 2021.
[27] R. Takano and M. Yamakita, “Robust control barrier function for systems
affected by a class of mismatched disturbances,” SICE J. Control, Meas.,
Syst. Integr., vol. 13, no. 4, pp. 165–172, 2020.
[28] E. Das and J. W. Burdick, “Robust control barrier functions us-
ing uncertainty estimation with application to mobile robots,” 2024,
arXiv:2401.01881.
[29] Y. Wang and X. Xu, “Disturbance observer-based robust control barrier
functions,” in Proc. Amer. Control Conf., 2023, pp. 3681–3687.
[30] M. H. Cohen and C. Belta, “Modular adaptive safety-critical control,” in
Proc. Amer. Control Conf., 2023, pp. 2969–2974.
[31] A. Isidori, Nonlinear Control Systems. Berlin, Germany: Springer, 1995.
[32] M. Krstic, “Inverse optimal safety ﬁlters,” IEEE Trans. Autom. Control,
vol. 69, no. 1, pp. 16–31, Jan. 2024.
[33] R. W. Beard and T. W. McLain, Small Unmanned Aircraft: Theory and
Practice. Princeton, NJ, USA: Princeton Univ. Press, 2012.
[34] L.GuoandW.-H.Chen,“Disturbanceattenuationandrejectionforsystems
with nonlinearity via DOBC approach,” Int. J. Robust Nonlinear Control,
vol. 15, no. 3, pp. 109–125, 2005.
[35] A. D. Ames, K. Galloway, K. Sreenath, and J. W. Grizzle, “Rapidly
exponentially stabilizing control Lyapunov functions and hybrid zero
dynamics,” IEEE Trans. Autom. Control, vol. 59, no. 4, pp. 876–891,
Apr. 2014.
[36] S. Boyd, S. P. Boyd, and L. Vandenberghe, Convex Optimization. Cam-
bridge, U.K.: Cambridge Univ. Press, 2004.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:35:01 UTC from IEEE Xplore.  Restrictions apply.
