# On_Compensation_Function_Observer-Based_Active_Disturbance_Rejection_Control_for_MIMO_Uncertain_Systems_and_Its_Application_to_2-DOF_Helicopter_System.pdf

## Page 1

IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS
1
On Compensation Function Observer-Based
Active Disturbance Rejection Control for MIMO
Uncertain Systems and Its Application to 2-DOF
Helicopter System
Kaiwen Liu
, Sen Chen
, Member, IEEE, Zhi-Liang Zhao
, Member, IEEE,
and Wenchao Xue
, Member, IEEE
Abstract—This article investigates the control problem
for multiple-input multiple-output systems with nonlinear
uncertainties. By introducing a prediction-correction mech-
anism, a new compensation function observer (CFO) is
constructed to enhance the estimation accuracy of the total
disturbance. Subsequently, the CFO-based active distur-
bance rejection control (CADRC) is designed to mitigate
the total disturbances and attain the desired control perfor-
mance. Based on an inductive decoupling-based Lyapunov
method, this article rigorously establishes the closed-loop
stability of the CADRC under a broad class of nonlin-
ear state-dependent uncertainties. Moreover, a comparative
frequency-domain analysis quantitatively reveals the supe-
rior disturbance estimation and rejection capabilities of the
CADRC. Finally, the proposed CADRC is implemented on
a Quanser two-degree-of-freedom helicopter system sub-
ject to additional digital uncertainties, and the experimental
results demonstrate its clear superiority over the conven-
tional ADRC.
Index
Terms—Active
disturbance
rejection
control
(ADRC), compensation function observer (CFO), multiple-
input multiple-output system (MIMO), uncertain system.
Received 25 August 2025; revised 10 November 2025 and 15 De-
cember 2025; accepted 25 December 2025. This work was supported
in part by the National Natural Science Foundation of China under
Grant 62473344 and Grant 92471204; in part by the Natural Science
Basic Research Program of Shaanxi under Grant 2025JC-YBQN-035;
and in part by the Ministry of Education’s Industry School Cooperation
Collaborative Education Project under Grant 240704701190619. (Cor-
responding author: Sen Chen.)
Kaiwen Liu and Sen Chen are with the School of Mathematics and
Statistics, Shaanxi Normal University, Xi’an 710119, China (e-mail:
lkw1895266@snnu.edu.cn; chensen14@mails.ucas.ac.cn).
Zhi-Liang Zhao is with the School of Electrical and Control Engi-
neering, North University of China, Taiyuan 030051, China (e-mail:
20240016@nuc.edu.cn).
Wenchao Xue is with the State Key Laboratory of Mathematical
Sciences, Academy of Mathematics and Systems Science, Chinese
Academy of Sciences, Beijing 100190, China, and also with the School
of Mathematical Sciences, University of Chinese Academy of Sciences,
Beijing 100049, China (e-mail: wenchaoxue@amss.ac.cn).
Digital Object Identiﬁer 10.1109/TIE.2026.3651375
I. INTRODUCTION
S
INCE uncertainties are ubiquitous in physical systems, it is
one of the fundamental issues in the control ﬁeld to tackle
these uncertainties [1]. To preserve the normal system operation
in the presence of various uncertainties, abundant control strate-
gies have been proposed and developed, such as proportional-
integral-derivative (PID) control [2], active disturbance rejec-
tion control (ADRC) [3], [4], disturbance observer-based con-
trol [5], [6], generalized proportional integral observer-based
control [7], [8], embedded model control [9], [10], model pre-
dictive control [11], ﬁnite-time control [12], [13], predeﬁned-
time control [14], etc. Among these methods, ADRC has at-
tracted considerable attention across academia and industry due
to its profound theoretical foundation and exceptional practical
performance.
The core principle of ADRC lies in constructing an extended
state observer (ESO) to actively estimate the total disturbance
[15], which is subsequently compensated for within the closed-
loop system. By formulating disturbances in a generalized
framework and leveraging the strong estimation capability of
the ESO, ADRC can effectively cope with a wide range of
uncertainties and achieve satisfactory closed-loop performance.
To date, ADRC has found successful application in a variety of
industrial systems, such as PMSM system [16], power system
[17], robotic system [18], motion system [19], magnetic levita-
tion system [20], etc. Owing to the pivotal role of ESO, substan-
tial research has focused on enhancing its estimation accuracy
and improving its overall performance [21], [22], [23], [24],
[25], [26], [27]. Recently, Qi et al. [28] pointed out the limita-
tions of the traditional ESO, such as nonderivative structure and
insufﬁcient usage of information. To tackle these limitations,
they ﬁrst proposed a novel third order compensation function
observer (CFO) for a class of second order uncertain systems. In
the design framework of CFO, the derivative form, measurable
innovation, and an explicit compensator are adopted to enhance
the estimation performance, which has been validated through
both theoretical analysis and experimental studies.
1557-9948 © 2026 IEEE. All rights reserved, including rights for text and data mining, and training of artiﬁcial intelligence and similar technologies.
Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html
for more information.
This article has been accepted for inclusion in a future issue of this journal. Content is final as presented, with the exception of pagination. 
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 12:52:47 UTC from IEEE Xplore.  Restrictions apply.

## Page 2

2
IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS
In the development of CFO, several notable advances have
been made. The reference [29] developed a general design of
the CFO for a class of nth order single-input single-output
(SISO) uncertain systems, and demonstrated its advantages in
the disturbance estimation accuracy and estimable bandwidth.
Wang et al. [30] investigated the application of CFO in PMSM
system, and highlighted the merits of the CFO-based ADRC
in disturbance rejection capability. The reference [31] explored
the implementation of CFO in the quadrotor UAV system, and
effectively addressed the dependence on modeling accuracy
in traditional backstepping control. Nevertheless, the general
design of the CFO-based ADRC (CADRC) for multiple-input
multiple-output (MIMO) uncertain system remains unexplored.
Furthermore, the inherent complexity of parameter design in
traditional CFO structures requires further investigation and
simpliﬁcation.
As for the theoretical foundations of the CFO, the existing
studies remain incomplete and warrant further development.
Under the assumption that the total disturbance is a (n +
1)th order inﬁnitesimal function, the reference [29] rigorously
proved the convergence of the (n + 1)th order CFO for a class
of nth order SISO uncertain systems. However, in practical
scenarios, the total disturbance often depends on the system
states [15], which makes it challenging to precisely analyze the
estimation performance of CFO by existing methods [28], [29].
Moreover, as reported in [29], the closed-loop stability of the
CADRC remains unresolved, which calls for further investiga-
tion to ensure its reliable application. The main difﬁculties in the
theoretical analysis of CADRC under nonlinear uncertainties
can be summarized as the following two points.
(D1) Since the uncertainties are nonlinearly dependent on the
system states, it is sometimes unreasonable to directly assume
that the uncertainties and their derivatives are bounded. More-
over, the strong cross-channel coupling exists in the MIMO
systems, where the uncertainty in any single channel is affected
by all states of the control system. Therefore, it is challenging
to characterize and prove the scope of uncertainties that the
CADRC can effectively suppress.
(D2) Due to the complex coupling effect between the control
system and the observer system, it is insufﬁcient to conduct a
standalone convergence analysis of CFO, such as [28], [29].
How to comprehensively analyze the closed-loop transient per-
formance of CADRC under nonlinear state-dependent uncer-
tainties remains a signiﬁcant theoretical hurdle.
To address the aforementioned issues, this article is devoted
to the design and theoretical analysis of CADRC for a class
of MIMO systems with nonlinear uncertainties. Furthermore,
the proposed CADRC is applied to a Quanser two-degree-
of-freedom (2-DOF) helicopter system with additional digital
uncertainties. The key contribution is outlined as follows.
1) A new CADRC is proposed for a class of MIMO un-
certain systems. In the proposed design, the prediction-
correction mechanism is introduced to enhance the es-
timation accuracy of the total disturbances. Moreover,
by investigating the estimation errors of the CFO, a
single-parameter-tuning strategy is devised to simplify the
parameter design.
2) The closed-loop stability of the CADRC-based MIMO
system is rigorously investigated in the presence of a
broad class of nonlinear state-dependent uncertainties.
Moreover, it is shown that the tracking and estimation
errors can converge to the desired bound by increasing
the bandwidth of CFO.
3) The transfer functions from the total disturbance to both
its estimation error and the controlled output are explicitly
derived. Then, the frequency response analysis of these
transfer functions quantitatively reveals the superiority
of CADRC in both disturbance estimation and rejection
capabilities.
The remainder of this article is structured as follows. Sec-
tion II provides the problem formulation. Section III presents
the design of the ADRC with a single-parameter-tuning CFO.
The performance analyses in both time domain and frequency
domain are provided in Section IV. The experiments are dis-
cussed in Section V. Section VI concludes the article.
II. PROBLEM FORMULATION
Consider
the
following
multiple-input
multiple-output
(MIMO) nonlinear uncertain system
⎧
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎨
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎩
˙xi1(t) = xi2(t),
...
˙xi(n−1)(t) = xin(t),
˙xin(t) = δi(x(t), t) + di(t) +
m

j=1
bij(t)uj(t),
yi(t) = Cxi(t) = xi1(t),
t ⩾t0,
i = 1, 2, . . . , m,
(1)
where
x(t) = [x⊤
1 (t), . . . , x⊤
m(t)]⊤∈Rnm,
xi(t) =
[xi1(t), . . . , xin(t)]⊤∈Rn
represent
the
state
vector,
uj(t) ∈R represents the control input, yi(t) ∈R represents
the controlled output, di(t) ∈R represents the time-varying
external
disturbances,
and
δi(x(t), t) ∈R
represents
the
coupled internal uncertainties. Additionally, the known control
input gain matrix Bu(t) = [bij(t)]m×m ∈Rm×m is invertible,
and the output matrix is deﬁned as C = [1, 0, . . . , 0] ∈R1×n.
Remark 1: It is worth emphasizing that each internal uncer-
tainty δi(x(t), t) is a nonlinear function of the entire state vector
x(t), resulting in strong cross-channel coupling.
The
control
target
is
to
design
the
control
input
u(t) ≜[u1(t), . . . , um(t)]⊤∈Rm
such
that
the
output
y(t) ≜[y1(t), . . . , ym(t)]⊤∈Rm
tracks a given reference
signal
r(t) ≜[r1(t), . . . , rm(t)]⊤∈Rm.
Additionally,
the
following assumptions are presented regarding the unknown
nonlinear functions δi(·), di(·), and the reference signal ri(t),
i ∈m.
Assumption 1: The function δi(·) ∈Cn+1 (Rnm × R, R).
Furthermore, there exists a function ϕ(·) ∈C (Rnm, [0, +∞))
such that for any integers ix ⩾0, it ⩾0, and ix + it ⩽n + 1
sup
t⩾t0

∂ix+itδi
∂xix∂tit
 ⩽ϕ(x),
∀x ∈Rnm.
(2)
This article has been accepted for inclusion in a future issue of this journal. Content is final as presented, with the exception of pagination. 
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 12:52:47 UTC from IEEE Xplore.  Restrictions apply.

## Page 3

LIU et al.: ON COMPENSATION FUNCTION OBSERVER-BASED ACTIVE DISTURBANCE REJECTION CONTROL
3
Assumption 2: [5], [24] The function di(·) ∈Cn+1(R, R).
Furthermore, there exists a positive constant Nd such that
sup
t⩾t0
d(n+1)
i
(t)
 ⩽Nd.
(3)
Remark 2: Under Assumption 1, the nonlinear function
δi(x, t) and its partial derivatives (∂ix+itδi/∂xix∂tit) are uni-
formly bounded by a continuous function ϕ(x), which covers
a broad class of uncertainties. For Assumption 2, the bounded-
ness of the (n + 1)th order derivative of the nonlinear function
di(t) is required. Additionally, if di(t) is a discontinuous func-
tion with the ﬁrst class of discontinuous points, the stability can
still be established in a piecewise manner, as shown in [32].
Assumption 3: [5], [15] The function ri(·) ∈C2n+1 (R, R).
Furthermore, there exists a positive constant Nr such that
sup
t⩾t0

|ri(t)| ,
r(1)
i (t)
 , . . . ,
r(2n+1)
i
(t)

	
⩽Nr.
(4)
From Assumption 3, the reference signal r(t) and its deriva-
tives up to (2n + 1) order are assumed to be bounded, which
are typical in practical engineering scenarios.
III. DESIGN OF CADRC
In this section, the CFO-based ADRC is designed for the
MIMO system (1). First, a single-parameter-tuning CFO is
designed to estimate the total disturbance for each channel indi-
vidually. Then, based on these estimations, the overall feedback
controller is constructed. Let gi (x(t), t) ≜δi(x(t), t) + di(t)
denote the total disturbance, and let u∗
i (t) ≜m
j=1 bij(t)uj(t)
be the virtual input, for i = 1, 2, . . . , m.
From the system (1), the state vector xi(t) is governed by the
following equation:
˙xi(t) = Axi(t) + B (gi(x(t), t) + u∗
i (t))
(5)
where
the
matrices
A
and
B
are
deﬁned
as
A =

 0(n−1)×1
I(n−1)×(n−1)
01×1
01×(n−1)

∈Rn×n, B =

01×(n−1) 1 T ∈Rn.
Then, a single-parameter-tuning CFO is designed to esti-
mate the total disturbance gi (x(t), t) through the following
steps. In addition, deﬁne the extended state vector as xie(t) =
[xi1, . . . , xi(n+1)]⊤≜

x⊤
i (t) gi (x(t), t)
⊤∈Rn+1.
Step 1 (Prediction): To begin with, we provide a preliminary
estimation for the total disturbance xi(n+1)(t)
 ˙ˆxi(t) = Aˆxi(t) + B

zi(t) + L⊤
1 (xi(t) −ˆxi(t)) + u∗
i (t)

,
˙zi(t) = L⊤
2 (xi(t) −ˆxi(t))
(6)
where ˆxi(t) = [ˆxi1(t), . . . , ˆxin(t)]⊤∈Rn is the estimation of
xi(t), zi(t) ∈R is preliminary estimation of xi(n+1)(t), and
L1 = [l11, . . . , l1n]⊤∈Rn, L2 = [l21, . . . , l2n]⊤∈Rn are the
parameter vectors to be designed.
Step 2 (Correction): Then, to enhance the estimation accu-
racy of the total disturbance, the preliminary estimation zi(t)
is reﬁned by estimation errors (xi(t) −ˆxi(t)). The actual es-
timation of the total disturbance is obtained by the following
equation:
ˆxi(n+1)(t) = zi(t) + L⊤
1 (xi(t) −ˆxi(t))
(7)
Fig. 1.
Block diagram of the proposed CADRC scheme for each
channel.
where ˆxi(n+1)(t) ∈R represents the estimation of xi(n+1)(t).
Step 3 (Parameter Design): Next, to facilitate parameter
design, the estimation errors of CFO (6) and (7) are investigated.
By taking the derivative of ˆxi(n+1)(t), the CFO (6) and (7) can
be equivalently rewritten as follows:
˙ˆxie(t) = Aeˆxie(t) + Beu∗
i (t) + DeL⊤
e (xie(t) −ˆxie(t)) (8)
where ˆxie(t) = [ˆx⊤
i (t), ˆxi(n+1)(t)]⊤∈Rn+1, the parameter
vector
Le = [l21, l22 + l11, . . . , l2n + l1(n−1), l1n]⊤∈Rn+1,
and
the
matrices
Ae,
Be,
De
are
deﬁned
by
Ae =

 0n×1 In×n
01×1 01×n

∈R(n+1)×(n+1),
Be =

01×(n−1) 1 0 ⊤∈Rn+1,
De =

01×n 1 ⊤∈Rn+1.
Combining (5) and (8), we derive that the estimation errors
of CFO ei(t)
△= xie(t) −ˆxie(t) satisfy the following equation:
˙ei(t) =

Ae −DeL⊤
e

ei(t) + De ˙gi(x(t), t).
(9)
To ensure the stability of (9), the parameter vector Le is
designed to render the matrix

Ae −DeL⊤
e

Hurwitz. Specif-
ically, by using the bandwidth theory in [21], we design
sIn+1 −Ae + DeL⊤
e
 = sn+1 + l1nsn
+ · · · + (l11 + l22)s + l21 = (s + μ)n+1
(10)
where
μ > 0
is
viewed
as
the
bandwidth
of
CFO.
Then,
by
setting
L1 = [(1/2)ln, . . . , (1/2)l2, l1]⊤
and
L2 = [ln+1, (1/2)ln, . . . , (1/2)l2]⊤
with
lj = Cj
n+1μj,
j ∈n + 1, the parameters can be uniquely determined with
respect to the given bandwidth μ, leaving only one parameter
to be tuned. The general scheme of CFO is presented in Fig. 1.
Remark 3: According to the traditional CFO in [28], [29],
zi(t) serves as the compensation function. Unlike the previous
design, zi(t) is deﬁned as the integral of L⊤
2 (xi(t) −ˆxi(t)),
rather than the integral of λL⊤
1 (xi(t) −ˆxi(t)). Moreover, un-
der the proposed design (10), the parameter design of the CFO
is simpliﬁed to tuning a single bandwidth μ, which promotes
its industrial application.
Finally, based on (6) and (7), the CFO-based feedback con-
troller u(t) is designed as follows:

u∗
i (t) = r(n)
i
(t) −K⊤(xi(t) −¯ri(t)) −ˆxi(n+1)(t), i ∈m
u(t) = B−1
u (t)u∗(t) ≜B−1
u (t)[u∗
1(t), . . . , u∗
m(t)]⊤
(11)
This article has been accepted for inclusion in a future issue of this journal. Content is final as presented, with the exception of pagination. 
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 12:52:47 UTC from IEEE Xplore.  Restrictions apply.

## Page 4

4
IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS
where ¯ri(t) = [ri(t), r(1)
i (t), . . . , r(n−1)
i
(t)]⊤∈Rn, and the
control gain vector K = [k1, . . . , kn]⊤∈Rn is chosen to make
the matrix AK ≜A −BK⊤Hurwitz.
IV. PERFORMANCE ANALYSIS
A. Time-Domain Performance Analysis
In this section, the closed-loop stability of the CADRC is ana-
lyzed. The analysis unfolds in the following two steps: 1) estab-
lishing an equivalent realization of the CADRC; and 2) proving
the stability of the CADRC-based closed-loop system.
First, to establish a benchmark for the disturbance rejection
performance, we design the following ideal trajectory

˙x∗
i (t) = Ax∗
i (t) −BK⊤(x∗
i (t) −¯ri(t)) + Br(n)
i
(t),
y∗
i (t) = C⊤x∗
i (t),
t ⩾t0,
x∗
i (t0) = xi(t0)
(12)
where x∗
i (t) = [x∗
i1(t), . . . , x∗
in(t)]⊤∈Rn represents the ideal
state vector, and y∗
i (t) ∈R represents the ideal output, which
exponentially converges to the reference signal ri(t) at a rate
governed by the parameter vector K.
Then, an equivalent realization of the CADRC (6), (7), and
(11) is introduced to facilitate the theoretical analysis.
Lemma 1: For the system (5), an equivalent realization of the
CADRC (6), (7), and (11) is established as
⎧
⎪
⎨
⎪
⎩
˙ˆGi(t) = Ae ˆGi(t) + ˜LeC⊤
e

Gi(t) −ˆGi(t)

,
˜u∗
i (t) = r(n)
i
(t) −K⊤(xi(t) −¯ri(t)) −ˆgi1(t), i ∈m
˜u(t) = B−1
u (t)˜u∗(t) ≜B−1
u (t) [˜u∗
1(t), . . . , ˜u∗
m(t)]⊤
(13)
where
Ce =

1 01×n
⊤∈Rn+1,
the
parameter
vector
˜Le = [l1, . . . , ln+1]⊤∈Rn+1,
and
ˆGi(t) =
[ˆgi1(t), . . . , ˆgi(n+1)(t)]⊤∈Rn+1
is
the
estimation
of
Gi(t) = [gi(x(t), t), g(1)
i (x(t), t), . . . , g(n)
i
(x(t), t)]⊤∈Rn+1.
The proof of Lemma 1 is presented in Appendix A. Based on
the realization in (13), the following theorem demonstrates the
closed-loop performance of the CADRC-based MIMO system
under nonlinear state-dependent coupling uncertainties.
Theorem 1: Consider the CADRC-based closed-loop system
(1), (6), (7), and (11). Suppose that Assumptions 1–3 are satis-
ﬁed, and the matrix AK is Hurwitz. Then, there exist positive
constants ˜μ and ρj(1 ⩽j ⩽3) dependent on (ϕ(·), Nr, Nd),
such that if μ ∈[˜μ, +∞), then
sup
t⩾t0
∥xi(t) −x∗
i (t)∥⩽ρ1
lnμ
μ
(14)
sup
t⩾˜t
Gi(t) −ˆGi(t)
 ⩽ρ2

e−ρ3μ(t−˜t) + 1
μ

(15)
for
any
i ∈m,
where
the
constants
ρj(1 ⩽j ⩽3)
are
μ-independent, ˜t = t0 + 2nλφ2(lnμ/μ), and λφ2 is given in
(26) in Appendix B.
The proof of Theorem 1 is presented in Appendix B. As
shown in (14) and (15), Theorem 1 establishes the explicit and
tunable upper bounds for the tracking and estimation errors in
the CADRC-based closed-loop system. From (14), by selecting
a sufﬁciently large observer bandwidth μ, the tracking error
between the actual and ideal trajectories can be arbitrarily small
in the whole time domain. According (15), the estimation errors
can exponentially converge to the desired bound by increasing
the observer bandwidth μ.
Remark 4: As demonstrated in Theorem 1, the desired
closed-loop performance in the presence of nonlinear state-
dependent uncertainties can be attained by increasing μ. More-
over, the relationship between the closed-loop performance and
the controller parameters is explicitly depicted. The controller
gain K is selected to determine the ideal tracking performance,
and the observer bandwidth μ is increased to enhance the
disturbance rejection capability, which provides guidance for
practical engineering applications.
B. Frequency-Domain Performance Analysis
In this section, a frequency-domain performance analysis of
the proposed CADRC is presented.
First, we deﬁne Yi(s), Ri(s), Xi(n+1)(s), and ˆXi(n+1)(s) as
the Laplace transforms of the system output yi(t), the reference
signal ri(t), the total disturbance xi(n+1)(t), and its corre-
sponding estimation ˆxi(n+1)(t), respectively. Then, the transfer
functions from the total disturbance to both its estimation error
and the controlled output are explicitly derived, as presented in
Proposition 1.
Proposition 1: Consider the system (1) under two control
methods: 1) the CADRC (6)–(11); and 2) the LADRC [33].
Suppose zero initial condition, then

Xi(n+1)(s) −ˆXi(n+1),p(s) = L1,p(s)Xi(n+1)(s),
Yi,p(s) = L2,p(s)Xi(n+1)(s) + Ri(s),
p = a, b,
(16)
where the index p denotes the control method, and the transfer
functions L1,p(s) and L2,p(s) are deﬁned as
⎧
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎨
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎩
L1,a(s) =
sn+1
sn+1+n+1
p=1 lpsn+1−p ,
L2,a(s) =
sn+1
(sn+1+n+1
p=1 lpsn+1−p)(sn+n−1
p=0 kn−psn−1−p),
L1,b(s) =
sn+1+n
p=1 lpsn+1−p
sn+1+n+1
p=1 lpsn+1−p ,
L2,b(s) =
sn+1+n
p=1(lp+p−1
q=1 kn+1−qlp−q+kn+1−p)sn+1−p
(sn+1+n+1
p=1 lpsn+1−p)(sn+n−1
p=0 kn−psn−1−p) .
The proof of Proposition 1 is provided in Appendix C. By
analyzing the frequency response of L1,a(s) and L2,a(s) in (16),
the disturbance estimation and rejection capabilities of CADRC
are assessed. Furthermore, a comparative result between the
proposed CADRC and the traditional LADRC is established in
Proposition 2.
Proposition 2: Consider the system (1) under two control
methods: (a) the CADRC (6)–(11), and (b) the LADRC [33].
Suppose that the initial values are zero, and AK is Hurwitz.
Then, for any bandwidth μ > 0, the following relationships hold
lim
w→0 |L1,a(jw)| = 0,
lim
w→0 |L2,a(jw)| = 0
(17)
lim
w→0

L1,a(jw)
L1,b(jw)
 = 0,
lim
w→0

L2,a(jw)
L2,b(jw)
 = 0
(18)
where j represents the imaginary unit.
This article has been accepted for inclusion in a future issue of this journal. Content is final as presented, with the exception of pagination. 
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 12:52:47 UTC from IEEE Xplore.  Restrictions apply.

## Page 5

LIU et al.: ON COMPENSATION FUNCTION OBSERVER-BASED ACTIVE DISTURBANCE REJECTION CONTROL
5
Fig. 2.
Magnitude response curves of L1,a(s) and L1,b(s) under the
parameter conﬁguration (μ = 10).
Fig. 3.
Magnitude response curves of L2,a(s) and L2,b(s) under the
parameter conﬁguration (μ = 10, ωc = 10).
The proof of proposition 2 is provided in Appendix D.
According to (17), the CADRC exhibits reliable disturbance
estimation and rejection capabilities for low-frequency dis-
turbances. Moreover, as revealed by (18), in the same low-
frequency limit, the transfer functions L1,a(jw) and L2,a(jw)
approach zero more rapidly than those of LADRC, conﬁrming
the enhanced disturbance estimation and rejection capabilities.
To more intuitively illustrate the results of Proposition 2,
the magnitude response curves of L1,p(s) and L2,p(s) are pre-
sented under multiple parameter conﬁgurations. The parameters
of both CADRC and LADRC are conﬁgured as follows: the
system order n ranges from 1 to 6, and the controller gains
kj ≜Cn−j+1
n
ωn−j+1
c
(1 ⩽j ⩽n). Two distinct bandwidth sce-
narios are subsequently evaluated: (1) μ = 10, ωc = 10; (2) μ =
20, ωc = 5. As depicted in Figs. 2–5, the magnitude response
curves of CADRC are uniformly lower than the LADRC ones
at the same frequency, quantitatively demonstrating its superior
capability in disturbance estimation and rejection.
V. APPLICATION TO THE QUANSER 2-DOF
HELICOPTER SYSTEM
In this section, the experiments of a Quanser 2-DOF heli-
copter system are presented.
A diagram of the experimental setup is provided in Fig. 6.
The Quanser 2-DOF helicopter system comprises a helicopter
body equipped with a hardware-in-the-loop (HIL) control
board, a yoke, two dc motors (pitch and yaw), two corre-
sponding propellers, two encoders, and a slip ring. The pitch
and yaw encoders measure the actual pitch and yaw angles of
Fig. 4.
Magnitude response curves of L2,a(s) and L2,b(s) under the
parameter conﬁguration (μ = 20).
Fig. 5.
Magnitude response curves of L2,a(s) and L2,b(s) under the
parameter conﬁguration (μ = 20, ωc = 5).
Fig. 6.
Experimental setup of the quanser 2-DOF helicopter system.
the helicopter, respectively. Based on the implemented control
algorithm, the master computer calculates the control input
and sends it to the HIL control board. Subsequently, the HIL
control board drives the pitch and yaw dc motors to regulate the
corresponding angles. Additionally, the input voltages of both
motors are limited to [−24 V, 24 V] to protect the devices.
The mathematical model of the Quanser 2-DOF helicopter
system is formulated as follows [34]:
⎧
⎪
⎪
⎪
⎨
⎪
⎪
⎪
⎩

Ip + ml2
a
 ¨θ = −mgla cos θ −Dp ˙θ −ml2
a ˙φ2 sin θ cos θ
+Kpp (Vp + △Vp) + Kpy (Vy + △Vy) ,

Iy + ml2
a cos2 θ
 ¨φ = −Dy ˙φ + 2ml2
a ˙φ ˙θ sin θ cos θ
+Kyp (Vp + △Vp) + Kyy (Vy + △Vy) ,
(19)
This article has been accepted for inclusion in a future issue of this journal. Content is final as presented, with the exception of pagination. 
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 12:52:47 UTC from IEEE Xplore.  Restrictions apply.

## Page 6

6
IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS
TABLE I
MAIN PARAMETERS OF THE 2-DOF HELICOPTER SYSTEM
Parameter
Value
Parameter
Value
la
0.0071 m
Kpp
0.0012 Nm/V
Ip
0.0230 kg · m2
Kpy
0.0022 Nm/V
Iy
0.0210 kg · m2
Kyp
−0.0027 Nm/V
Dp
0.0071 N · s/m
Kyy
0.0024 Nm/V
Dy
0.0220 N · s/m
m
1.0760 kg
where θ(t) ∈R and φ(t) ∈R are the pitch angle and the yaw
angle, Vp(t) ∈R and Vy(t) ∈R represent the voltages for the
pitch and yaw motors, respectively. △Vp(t), △Vy(t) ∈R are the
designed digital uncertainties. The parameters la is the distance
from the helicopter’s mass center to the origin of the ﬁxed
fuselage frame, Ip and Iy represent the pitch and yaw moments
of inertia, Dp and Dy are the corresponding friction coefﬁ-
cients, Kpp, Kpy, Kyp, and Kyy are the torque-thrust gains, m
is gross mass of helicopter. Moreover, the nominal values of
{la, Ip, Iy, Dp, Dy, Kpp, Kpy, Kyp, Kyy, m} are summarized
in Table I.
Based on the measurements of the attitude angle vector
p(t) = [p1(t), p2(t)]⊤≜[θ(t), φ(t)]⊤, the control target is to
design the motor voltages V (t) ≜[Vp(t), Vy(t)]⊤such that
p(t) tracks the given reference signal r(t) = [r1(t), r2(t)]⊤≜
[30 deg, 30 deg]⊤.
Denote
b11 = (Kpp/Ip + ml2
a),
b12 = (Kpy/Ip
+
ml2
a),
g1(θ, ˙θ, φ, ˙φ, t)
=
(−mgla cos θ
−
Dp ˙θ
−
ml2
a ˙φ2 sin θ cos θ/Ip + ml2
a) + (Kpp△Vp + Kpy△Vy/Ip +
ml2
a),
b21(t)
=
(Kyp/Iy
+
ml2
a cos2 θ),
b22(t)
=
(Kyy/Iy
+
ml2
a cos2 θ),
g2(θ, ˙θ, φ, ˙φ, t)
=
(−Dy ˙φ
+
2ml2
a ˙φ ˙θ sin θ cos θ/Iy
+
ml2
a cos2 θ)
+
(Kyp△Vp
+
Kyy△Vy/Iy + ml2
a cos2 θ). Then, the proposed CADRC
(6), (7), and (11) is applied to the Quanser 2-DOF helicopter
with the parameters (k1 = 10, k2 = 20, μ = 12).
For comparative evaluation, the following traditional ADRC
(TADRC) is also considered in the experiments:
⎧
⎪
⎪
⎪
⎪
⎪
⎪
⎨
⎪
⎪
⎪
⎪
⎪
⎪
⎩
˙˜xi1(t) = ˜xi2(t) + 3˜μ(pi(t) −˜xi1(t)),
˙˜xi2(t) = ˜xi3(t) + 3˜μ2(pi(t) −˜xi1(t)),
˙˜xi3(t) = ˜μ3(pi(t) −˜xi1(t)),
i = 1, 2,
V ∗
i (t) = ¨ri(t) −˜k1(˜xi1(t) −ri(t))
−˜k2(˜xi2(t) −˙ri(t)) −˜xi3(t),
˜V (t) = B−1
v (t)[V ∗
1 (t), V ∗
2 (t)]⊤
(20)
where Bv(t) = (bij) ∈R2×2, and the controller parameters are
set to (˜k1 = 10, ˜k2 = 20, ˜μ = 12) for a fair comparison.
To further demonstrate the superiority of the proposed control
approach, we impose additional digital uncertainties △Vp(t)
and △Vy(t) in Experiments 1 and 2.
Experiment 1: In this experiment, the additional digital un-
certainties △Vp(t) and △Vy(t) are designed as sinusoidal sig-
nals combined with state-dependent nonlinearities
Case 1 : △Vp(t) = △Vy(t) = 2 sin(2t) + 0.6θ3 + 0.4φ2,
Case 2 : △Vp(t) = △Vy(t) = 4 sin(2t) + 0.6θ3 + 0.4φ2,
Fig. 7.
Control
performance
under
additional
digital
uncertainty
(case 1). (a) Pitch. (b) Yaw.
Fig. 8.
Control
performance
under
additional
digital
uncertainty
(case 2). (a) Pitch. (b) Yaw.
Case 3 : △Vp(t) = △Vy(t) = 8 sin(2t) + 0.6θ3 + 0.4φ2,
Case 4 : △Vp(t) = △Vy(t) = 8 sin(4t) + 0.6θ3 + 0.4φ2.
Experiment 2: In this experiment, the additional digital un-
certainties △Vp(t) and △Vy(t) are designed as step signals
combined with state-dependent nonlinearities
Case 5 : △Vp(t) = △Vy(t) =

5 + θ2 + φ, if sin(πt) ⩾0
−5 + 0.5φ2, if sin(πt) < 0 ,
Case 6 : △Vp(t) = △Vy(t) =

7.5 + θ2 + φ, if sin(πt) ⩾0
−7.5 + 0.5φ2, if sin(πt) < 0 ,
This article has been accepted for inclusion in a future issue of this journal. Content is final as presented, with the exception of pagination. 
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 12:52:47 UTC from IEEE Xplore.  Restrictions apply.

## Page 7

LIU et al.: ON COMPENSATION FUNCTION OBSERVER-BASED ACTIVE DISTURBANCE REJECTION CONTROL
7
Fig. 9.
Control
performance
under
additional
digital
uncertainty
(case 3). (a) Pitch. (b) Yaw.
Fig. 10.
Control performance under additional digital uncertainty
(case 4). (a) Pitch. (b) Yaw.
Case 7 : △Vp(t) = △Vy(t) =

10 + θ2 + φ, if sin(2πt) ⩾0
−10 + 0.5φ2, if sin(2πt) < 0.
During the experiments, a sampling interval of 0.001 s was
adopted, and the continuous-time controller was discretized via
the forward Euler method. The results of the experiments are
illustrated in Figs. 7–13. In addition, the integral of squared
error (ISE), integral of absolute error (IAE), root mean square
error (RMSE), and integral of squared control input (ISCI)
Fig. 11.
Control performance under additional digital uncertainty
(case 5). (a) Pitch. (b) Yaw.
Fig. 12.
Control performance under additional digital uncertainty
(case 6). (a) Pitch. (b) Yaw.
are provided as key quantitative performance indicators in Ta-
bles II–III.
As depicted in Figs. 7–13, the proposed CADRC delivers
consistently superior pitch and yaw tracking performance over
the traditional ADRC under all disturbance scenarios (Cases 1–
7). For pitch angle control, CADRC achieves markedly lower
ISE, IAE, and RMSE values compared to TADRC, with ISE
reductions ranging from 82.48% (Case 4) to 98.14% (Case 2),
IAE reductions from 58.52% (Case 4) to 86.31% (Case 2),
This article has been accepted for inclusion in a future issue of this journal. Content is final as presented, with the exception of pagination. 
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 12:52:47 UTC from IEEE Xplore.  Restrictions apply.

## Page 8

8
IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS
Fig. 13.
Control performance under additional digital uncertainty
(case 7). (a) Pitch. (b) Yaw.
TABLE II
PERFORMANCE INDICATORS OF PITCH ANGLE TRACKING
FOR CASES 1–7
Test Type
Method
ISE
IAE
RMSE
ISCI
Case 1
CADRC
0.1247
1.4906
0.0790
18013
TADRC
2.9863
6.9576
0.3864
17976
RATIO
4.18%
21.42%
20.45%
100.21%
Case 2
CADRC
0.1786
1.7116
0.0945
17999
TADRC
9.5771
12.5058
0.6920
17967
RATIO
1.86%
13.69%
13.66%
100.18%
Case 3
CADRC
0.5807
2.9765
0.1704
18019
TADRC
12.7338
14.5594
0.7979
17976
RATIO
4.56%
20.44%
21.36%
100.24%
Case 4
CADRC
3.0425
7.0006
0.3900
18052
TADRC
17.3676
16.8779
0.9319
18028
RATIO
17.52%
41.48%
41.85%
100.13%
Case 5
CADRC
0.9602
3.6218
0.2191
18056
TADRC
7.7053
11.7841
0.6207
18007
RATIO
12.46%
30.73%
35.30%
100.27%
Case 6
CADRC
1.0614
3.6165
0.2304
18042
TADRC
21.6500
19.5904
1.0404
18021
RATIO
4.90%
18.46%
22.15%
100.12%
Case 7
CADRC
2.8517
7.0881
0.3776
18001
TADRC
49.2088
28.9765
1.5686
18044
RATIO
5.80%
24.46%
24.08%
99.76%
and RMSE reductions from 58.15% (Case 4) to 86.34%
(Case 2). Similar advantages can be observed in yaw an-
gle tracking control, where CADRC consistently outperforms
TADRC, with ISE values reduced to only 3.19-36.10% of
TADRC’s values and RMSE reductions reaching up to 72.40%
(Case 4). Critically, these signiﬁcant accuracy improvements
are achieved with nearly identical ISCI values (ISCI ratios:
99.65%–102.00%), demonstrating CADRC’s efﬁcient distur-
bance rejection capability.
TABLE III
PERFORMANCE INDICATORS OF YAW ANGLE TRACKING
FOR CASES 1–7
Test Type
Method
ISE
IAE
RMSE
ISCI
Case 1
CADRC
0.1582
1.5011
0.0889
18013
TADRC
1.5123
4.9016
0.2750
18009
RATIO
10.46%
30.62%
32.33%
100.02%
Case 2
CADRC
0.4635
2.7180
0.1522
18013
TADRC
14.5296
15.3194
0.8524
18028
RATIO
3.19%
17.75%
17.85%
99.92%
Case 3
CADRC
1.0411
3.9038
0.2282
18103
TADRC
23.8514
19.7283
1.0921
18046
RATIO
4.36%
19.79%
20.90%
100.32%
Case 4
CADRC
9.1194
12.1800
0.6753
18084
TADRC
25.2625
20.3145
1.1239
18034
RATIO
36.10%
59.95%
60.09%
100.28%
Case 5
CADRC
1.0269
3.5973
0.2266
18126
TADRC
10.0258
13.4549
0.7080
18006
RATIO
10.24%
26.74%
32.01%
100.67%
Case 6
CADRC
3.0505
6.9116
0.3905
18388
TADRC
33.5781
24.4416
1.2957
18028
RATIO
9.09%
28.28%
30.14%
102.00%
Case 7
CADRC
5.2328
9.4609
0.5115
18006
TADRC
68.6547
34.7738
1.8528
18069
RATIO
7.62%
27.21%
27.60%
99.65%
VI. CONCLUSION
This article proposed a novel CFO-based ADRC for MIMO
nonlinear uncertain systems. By leveraging an inductive
decoupling-based Lyapunov method, the closed-loop stabil-
ity was rigorously established under a broad class of state-
dependent uncertainties. Moreover, a comparative frequency-
domain analysis quantitatively demonstrated the superior dis-
turbance estimation and rejection performance of the proposed
method. Finally, experiments on a Quanser 2-DOF helicopter
system conﬁrmed that the proposed method outperforms the
conventional ADRC.
In future work, we will focus on extending the CADRC
framework to heterogeneous MIMO systems and stochastic
SISO systems. Additionally, the improvement of the CFO struc-
ture to enhance robustness against measurement noise will be
investigated to further facilitate practical applications.
APPENDIX
A. Proof of Lemma 1
To
begin
with,
we
deﬁne
the
estimation
errors
of
(8)
and
(13)
as
ei(t) = xie(t) −ˆxie(t) ∈Rn+1
and
˜ei(t) = Gi(t) −ˆGi(t) ∈Rn+1,
respectively.
Denote
their
Laplace transforms as Ei(s) = [Ei,1(s), . . . , Ei,n+1(s)]⊤and
˜Ei(s) = [ ˜Ei,1(s), . . . , ˜Ei,n+1(s)]⊤. In addition, let Xi(n+1)(s),
ˆXi(n+1)(s), and ˜Xi(n+1)(s) denote the Laplace transforms of
the total disturbance gi(x(t), t), its estimations ˆxi(n+1)(t), and
ˆgi1(t), respectively.
Due to (5), (8), and (13), ei(t) and ˜ei(t) satisfy that
˙ei(t) = ALei(t)
+
De(˙gi (x(t), t)) , ˙˜ei(t)
=
A˜L˜ei(t)
+
De(g(n+1)
i
(x(t), t)) , where De = [01×n, 1]⊤, AL = Ae −
DeL⊤
e , and A˜L = Ae −˜LeC⊤
e .
By taking the Laplace transform of ei(t), it can be
obtained that Ei(s) = (sIn+1 −AL)−1 De(sXi(n+1)(s)),
This article has been accepted for inclusion in a future issue of this journal. Content is final as presented, with the exception of pagination. 
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 12:52:47 UTC from IEEE Xplore.  Restrictions apply.

## Page 9

LIU et al.: ON COMPENSATION FUNCTION OBSERVER-BASED ACTIVE DISTURBANCE REJECTION CONTROL
9
where
(sIn+1 −AL)−1 De = [1, s, . . . , sk−1, . . . , sn]ϱ,
and
ϱ = (1/sn+1 + l1sn + · · · + lns + ln+1). Then, we can further
obtain that Ei,n+1(s) = (sn+1/sn+1 + l1sn + · · · + lns +
ln+1)Xi(n+1)(s). By leveraging the equation Ei,n+1(s) =
Xi(n+1)(s) −ˆXi(n+1)(s), it can be deduced that
ˆXi(n+1)(s) =
l1sn+···+lns+ln+1
sn+1+l1sn+···+lns+ln+1 Xi(n+1)(s).
(21)
Similarly, by taking the Laplace transform of ˜ei(t), we obtain
that ˜Ei(s) = (sIn+1 −A˜L)−1De

sn+1Xi(n+1)(s)

, where
(sIn+1 −A˜L)−1De = [1, s + l1, . . . , sk−1 + l1sk−2 + · · · +
lk−1, . . . , sn + l1sn−1 + · · · + ln]ϱ, and ϱ = (1/sn+1 + l1sn +
· · · + lns + ln+1). Then, we can further deduce that
˜Xi(n+1)(s) =
l1sn+···+lns+ln+1
sn+1+l1sn+···+lns+ln+1 Xi(n+1)(s).
(22)
By Comparing (21) with (22), Lemma 1 is proved.
□
B. Proof of Theorem 1
The proof of Theorem 1 proceeds in the following ﬁve steps.
1) Step1:
The
Establishment
of
Closed-Loop
Error
System: Let the tracking and estimation errors be deﬁned as
Ei(t) = xi(t) −x∗
i (t) ∈Rn,
E(t) = [E⊤
1 (t), . . . , E⊤
m(t)]⊤∈
Rnm,
and
ξi(t) = T −1 
Gi(t) −ˆGi(t)

∈Rn+1,
ξ(t)
=
[ξ⊤
1 (t), . . . , ξ⊤
m(t)]⊤∈R(n+1)m,
respectively,
where
the
matrix T
△= diag

μ−n, . . . , μ−1, 1

∈R(n+1)×(n+1).
Based on (5), (12), and (13), the dynamics of (Ei(t), ξi(t))
for i ∈m are derived as follows:
 ˙Ei(t) = AKEi(t) + BC⊤
e Tξi(t),
˙ξi(t) = μAφξi(t) + DeΨi(E(t), ξ(t), t),
(23)
where Ce = [1, 01×n]⊤, De = [01×n, 1]⊤, Ψi(E(t), ξ(t), t) =
(dn+1fi/dtn+1),
and
the
matrices
AK ∈Rn×n,
Aφ ∈R(n+1)×(n+1) have the following form:
AK =
⎡
⎢⎢⎢⎣
0
1
· · ·
0
...
...
...
...
0
0
· · ·
1
−k1
−k2
· · ·
−kn
⎤
⎥⎥⎥⎦, Aφ=
⎡
⎢⎢⎢⎣
−C1
n+1
1
· · ·
0
...
...
...
...
−Cn
n+1
0
· · ·
1
−Cn+1
n+1
0
· · ·
0
⎤
⎥⎥⎥⎦.
2) Step2: The Analysis of the Coupling Effect Caused by
the Total Disturbances: To begin with, it can be noticed
that
(dn+1/dtn+1)gi(x(t), t) = (dn+1/dtn+1)δi(x(t), t) +
(dn+1/dtn+1)di(t), and C⊤
e T = μ−nCe, C⊤
e TAj
φDe = 0 for
0 ⩽j ⩽n −1. Subsequently, it will be proved that, for any
positive integer 1 ⩽k ⩽n + 1, there exist functions ϑlk(·) and
ϑlk,z(·) ∈C1(Rn × R, R) such that
dkδi
dtk = ϑlk(x, t)
+
k−1

z=0

Lk,z∈ϖ(k,z)
ϑLk,z(x, t)
⎡
⎣
m

p=1
z

q=0

C⊤
e Aq
φξp(t)
μn
 l(k)
p,q⎤
⎦μz
(24)
where
Lk,z = (l(k)
1,0 , . . . , l(k)
1,z , . . . , l(k)
m,0, . . . , l(k)
m,z) ∈Nmz+m
denotes the multi-index notation, and the index set ϖ(k, z)
is
deﬁned
as
ϖ(k, z) ≜{(l1,0, . . . , l1,z, . . . , lm,0, . . . ,
lm,z) ∈Nmz+m| 0 ⩽lp,q ⩽k, 1 ⩽p ⩽m, 0 ⩽q ⩽
z, z
q=1(q m
p=1 lp,q) = z}.
The proof proceeds by induction on the derivative order
k. For the case k = 1, it can be deduced that (dδi/dt) =
ϑl1(x(t), t) + m
p=1 ϑlp,0(x(t), t)μ−nC⊤
e ξp(t),
where
ϑlp,0(x, t) = (∂δi/∂xpn), p = 1, 2, . . . , m, and ϑl1(x(t), t) =
m
j=1(∂δi/∂xj) (AKxj(t)
+ Br(n)
j
(t) + BK⊤¯rj(t)) +
(∂δi/∂t).
Assuming that (24) holds for any positive integer k =
s (∀1 ⩽s ⩽n), it is obtained that (d(μ−nC⊤
e Aq
φξp(t))lp,q/
dt)
=
(lp,qμ)(μ−nC⊤
e Aq
φξ(t))lp,q−1(μ−nC⊤
e Aq+1
φ
ξp(t)),
(dϑLk,z(x, t)/dt)
=
m
j=1(∂ϑLk,z/∂xj)(AKxj(t)
+
Br(n)
j
(t) + BK⊤¯rj(t)) +
(∂ϑLk,z/∂t) + m
j=1(∂ϑLk,z/
∂xjn)C⊤
e Tξj(t). Then, we further verify that (24) holds for
k = s + 1.
Given the fact that the functions ϑlk(x, t), ϑLk,z(x, t)
in (24) are composed of ﬁnite products and sums of
(xp, x∗
p, r(i)
p , (∂ix+itδi/∂xix∂tit)) with 1 ⩽p ⩽m, 1 ⩽i ⩽
2n + 1, and 1 ⩽ix + it ⩽n + 1, along with Assumptions 1–3,
we can obtain that there exists a non-decreasing function Φ(·) so
that
supLk,z∈ϖ(k,z){|ϑlk(x(t), t)|, |ϑLk,z(x(t), t)|} ⩽Φ(ρe),
for any E(t) ∈{E ∈Rnm : ||E|| ⩽ρe}.
Finally, it is deduced that if ||E(t)|| ⩽ρe, ||ξ(t)|| ⩽
μrρξ (∀0 ≤r ≤n), then
|Ψi(E(t), ξ(t), t)| ⩽
r

j=0
Ni,r,jμj
(25)
where
Ni,r,0
=
Nd
+
Φ(ρe)
+
n−r
z=0

Ln+1,z∈ϖ(n+1,z) Φ(ρe)[!m
p=1
!z
q=0(||Aφ||qρξ)lp,q], Ni,r,j =

Ln+1,z∈ϖ(n+1,z) Φ(ρe)[!m
p=1
!z
q=0(||Aφ||qρξ)lp,q]
(1
⩽
j ⩽r, z = n + j −r).
3) Step3: The Boundedness Analysis of the Trajectories of
the Closed-Loop Error system: Since the matrices AK and
Aφ are Hurwitz, there exist unique positive deﬁnite matrices
QK and Qφ such that A⊤
KQK + QKAK = −In and A⊤
φ Qφ +
QφAφ = −In+1. Deﬁne the Lyapunov functions Vi1(t) =
E⊤
i (t)QKEi(t) and Vi2(t) = ξ⊤
i (t)Qφξi(t), i ∈m. Moreover,
it can be veriﬁed that
λk1||Ei(t)||2 ⩽Vi1(t) ⩽λk2||Ei(t)||2,
λφ1||ξi(t)||2 ⩽Vi2(t) ⩽λφ2||ξi(t)||2
(26)
where λk1 and λk2 represent the minimal and maximal eigen-
values of QK, λφ1 and λφ2 represent the minimal and maximal
eigenvalues of Qφ, respectively.
Then, it will be proved that there exists a positive con-
stant ˜μ > 1 such that (E1(t), . . . , Em(t), ξ1(t), . . . , ξm(t)) re-
mains in the invariant set: Ω
△= {(E1, . . . , Em, ξ1, . . . , ξm) ∈
R(2n+1)m : Vi1 ⩽ρk1, Vi2 ⩽ρφ1, i ∈m}, for any μ ⩾˜μ, where
ρk1, ρφ1 is deﬁned by ρ0
△= 2 max1⩽i⩽m{Fi(t0) −ˆFi(t0)} >
0, ρk1
△= (9λk2λφ2/λφ1)∥QK∥2ρ2
0, ρφ1
△= 2λφ2ρ2
0μ2n.
The proof consists of the following two steps.
(S1)
For
any
integer
1 ⩽i ⩽m,
suppose
that
there
exists
a
positive
constant
t∗
i ∈(t0, +∞)
such
that
Vi2(t∗
i ) = ρφ1, max1⩽j⩽m,
j̸=i
Vj2(t) ⩽ρφ1, max1⩽j⩽m Vj1(t) ⩽
ρk1, t ∈[t0, t∗
i ], which implies that (ρφ1/λφ2) ⩽||ξi(t∗
i )||2 ⩽
This article has been accepted for inclusion in a future issue of this journal. Content is final as presented, with the exception of pagination. 
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 12:52:47 UTC from IEEE Xplore.  Restrictions apply.

## Page 10

10
IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS
(ρφ1/λφ1), and ∥ξ(t∗
i )∥⩽μn
"
(2mλφ2ρ2
0/λφ1),
∥E(t∗
i )∥⩽
#
(mρk1/λk1).
Then,
according
to
(23)
and
(25),
the
deriva-
tive
of
Vi2(t∗
1)
satisﬁes
that
(dVi2(t∗
1)/dt)
=
−μ||ξi(t∗
1)||2
+
2(D⊤
e Qφξi(t∗
1))Ψi(E(t∗
1),
ξ(t∗
1),
t∗
1)
⩽
||ξ1(t∗
1)||(−
√
2ρ0μn+1
+
2∥Qφ∥(n
j=0 Ni,n,jμj)),
where
Ni,n,j(0 ⩽j ⩽n) are positive constants independent of μ.
Based on polynomial theory, there exists a positive constant
˜μi > 1 such that (dVi2(t∗
1)/dt) < 0.
(S2)
For
any
integer
1 ⩽i ⩽m,
suppose
that
there
exists a positive constant ˜ti ∈(t0, +∞) such that Vi1(˜ti) =
ρk1, max1⩽j⩽m Vj2(t) ⩽ρφ1, max1⩽j⩽m,
j̸=i
Vj1(t) ⩽ρk1, t ∈
[t0, ˜ti],
which
implies
that
(ρk1/λk2) ⩽||Ei(˜ti)||2 ⩽
(ρk1/λk1), and ||ξi(˜ti)||2 ⩽(ρφ1/λφ1).
Then, due to (23), the derivative of Vi1(˜t1) satisﬁes that
(dVi1(˜t1)/dt) = −||Ei(˜ti)||2 + 2E⊤
i (˜ti)QKBC⊤
e Tξi(˜ti) ⩽
∥Ei(˜ti)∥(2
√
2 −3)∥QK∥ρ0
#
λφ2/
#
λφ1)) < 0.
By deﬁning ˜μ = max1⩽j⩽m ˜μj, and combining (S1) and
(S2), we can deduce that (E1(t), . . . , Em(t), ξ1(t), . . . , ξm(t))
remains in the invariant set Ω for any μ ⩾˜μ and t ⩾t0. More-
over, we deﬁne ρ1,e =
#
ρk1/λk1 and ρ1,ξ =
#
ρφ1/λφ1.
4) Step4:
The
Further
Analysis
of
the
Upper
Bound
for
the
Estimation
Errors
ξ(t):
By
leveraging
(23),
we
get
that
(d
#
Vi2(t)/dt) ⩽−(μ/2λφ2)
#
Vi2(t) +
(||Qφ||/
#
λφ1)|Ψi(E(t), ξ(t), t)|.
Then,
based
on
Gronwall
inequality
and
(25),
the
bound
of
#
Vi2(t)
is
given
by
#
Vi2(t) ⩽(
#
2λφ2ρ0)μne−(μ/2λφ2)(t−t0) +
(||Qφ||/
#
λφ1)Ni,n,maxμn $ t
t0 e−(μ/2λφ2)(t−τ)dτ,
where
Ni,n,max
△= max0⩽j⩽n Ni,n,j,
and
Ni,n,j (0 ⩽j ⩽n)
are
positive constants independent of μ.
Let t1 = t0 + 2λφ2(lnμ/μ), and it can be derived that
||ξi(t)|| ⩽(
#
Vi2(t)/
#
λφ1) ⩽μn−1ρ∗
i1,
∀t ⩾t1,
where
ρ∗
i1
=

(
#
2λφ2ρ0/
#
λφ1)
+
(2Ni,n,max||Qφ||λφ2/λφ1).
Then,
we
can
obtain
that
∥ξ(t)∥=
#m
i=1 ||ξi(t)||2 ⩽
μn−1ρ∗
1,
∀t ⩾t1,
where
ρ∗
1 =
#m
i=1(ρ∗
i1)2.
In
conjunction with (25), we know that |Ψi(E(t), ξ(t), t)| ⩽
n−1
j=0 Ni,n−1,jμj,
∀t ⩾t1, where Ni.n−1,j (0 ⩽j ⩽n −1)
are independent positive constants of μ.
Furthermore,
according
to
(23)
and
Gronwall
inequality,
#
Vi2(t) has the following bound:
#
Vi2(t) ⩽
e−(μ/2λφ2)(t−t1)#
Vi2(t1)
+
$ t
t1 e−(μ/2λφ2)(t−τ)(||Qφ||/
#
λφ1)|Ψi(E(τ), ξ(τ), τ)|dτ,
∀t ⩾t1. Similar to before,
by deﬁning t2 = t0 + 4λφ2(lnμ/ μ), it can be concluded
that ||ξ(t)|| ⩽μn−2ρ∗
i2,
∀t ⩾t2, where ρ∗
i2 = ((
#
λφ2ρ∗
1/
#
λφ1)
+
(2Ni,n−1,max||Qφ||λφ2/λφ1)).
Next,
we
can
further obtain that ∥ξ(t)∥⩽μn−2ρ∗
2,
∀t ⩾t2, where ρ∗
2 =
#m
i=1(ρ∗
i2)2.
In conclusion, by deﬁning ˜t = t0 + 2nλφ2(lnμ/μ) and using
mathematical induction, we can prove that there exists a pos-
itive constant ρ∗
n such that ||ξ(t)|| ⩽ρ∗
n,
∀t ⩾˜t, where ρ∗
n is
independent of μ and limμ→+∞˜t = t0.
5) Step5:
The
Convergence
Analysis
of
the
Trajectories of Closed-Loop Error System: By leveraging
(25),
the
bound
for
Ψi(E(t), ξ(t), t)
is
given
by:
|Ψi(E(t), ξ(t), t)| ⩽πi (ρ1,e, ρ∗
n) ,
∀t ⩾˜t,
for
any
μ ⩾˜μ,
where πi(·) is a well-deﬁned function independent of μ. Then,
we deﬁne π (ρ1,e, ρ∗
n) = max1⩽i⩽m πi (ρ1,e, ρ∗
n).
By using the dynamics (23) and the Gronwall inequality,
it can be derived that
#
Vi2(t) ⩽e−(μ/2λφ2)(t−˜t)#
Vi2(˜t) +
$ t
˜t e−(μ/2λφ2)(t−τ)(||Qφ||/
#
λφ1)|Ψi(E(τ),
ξ(τ), τ)|dτ.
Then,
it
can
be
obtained
that
||Gi(t)
−
ˆGi(t)||
⩽
ρ2(e−ρ3μ(t−˜t) + (1/μ)), ∀t ⩾˜t, where ρ2 = max{(
#
λφ2ρ∗
n/
#
λφ1), (2||Qφ||λφ2π (ρ1,e, ρ∗
n)/
#
λφ1)}, ρ3 = (1/2λφ2).
Subsequently, we analyze the convergence of
#
Vi1(t). For
all t ⩾˜t, we can deduce that (d
#
Vi1(t)/dt) ⩽−(1/
2λk2)
#
Vi1(t)
+
(||QK||/√λk1)||ξi(t)||μ−n, ∀t ⩾˜t.
By
leveraging
Gronwall
inequality,
the
upper
bound
for
#
Vi1(t)
can
be
established
as:
#
Vi1(t)
⩽
e−(1/2λk2)(t−˜t)√λk2||Ei(˜t)||
+
(2λk2||QK||ρ∗
n/√λk1)(1/
μn), ∀t ⩾˜t.
Finally, from (23), it can be derived that ||Ei(t)|| ⩽
ρ∗
0(lnμ/μ),
∀t0 ⩽t ⩽˜t, where ρ∗
0 = 2n2λφ2((3
#
λk2λφ2/
#
λk1λφ1)||AK||||QK|| + (
#
2λφ2/
#
λφ1))ρ0. Then, we fur-
ther obtain that for any μ ⩾˜μ, and i ∈m, ||Ei(t)|| ⩽ρ1(lnμ/
μ), ∀t ⩾t0, where ρ1 = max{ρ∗
0, √λk2ρ∗
0 + (2λk2||QK||ρ∗
n/
√λk1)}.
□
C. Proof of Proposition 1
Taking Laplace transforms of (5) and (11), we derive
that
sXi(s) = AXi(s) + B(U ∗
i (s) + Xi(n+1)(s)),
U ∗
i (s) =
−K⊤Xi(s) + (sn + n−1
p=0 kn−psn−1−p)R(s) −ˆXi(n+1)(s),
and Yi(s) = C⊤Xi(s).
Then,
it
can
be
deduced
that
Yi(s)
=
C⊤(sIn −
AK)−1BD⊤
e (Xi(n+1)(s) −ˆXi(n+1)(s))
+
C⊤(sIn −
AK)−1B(sn
+
n−1
p=0 kn−psn−1−p)R(s),
where
(sIn −AK)−1B = [1, s, . . . , sn−1]⊤ι, and ι = (1/(sn +
n−1
p=0 kn−psn−1−p)).
In
conjunction
with
(21),
we
obtain
that
Yi(s)
=
Ri(s)
+
(sn+1/(sn+1
+
n+1
p=1 lpsn+1−p)(sn
+
n−1
p=0 kn−psn−1−p))Xi(n+1).
Furthermore,
we
denote
L1,a(s) = (sn+1/sn+1 + n+1
p=1 lpsn+1−p) and L2,a(s) =
(sn+1/(sn+1 + n+1
p=1 lpsn+1−p)(sn + n−1
p=0 kn−psn−1−p)).
Similar to the derivation of L1,a(s) and L2,a(s), the expres-
sions of L1,b(s) and L2,b(s) corresponding to LADRC can be
found in [33].
□
D. Proof of Proposition 2
From Proposition 1, the following equations are obtained:
⎧
⎪
⎪
⎨
⎪
⎪
⎩
lim
w→0 |L1,a(jw)| = 0,
lim
w→0 |L2,a(jw)| = 0,
L1,a(s)
L1,b(s) =
sn
sn+n
p=1 lpsn−p ,
L2,a(s)
L2,b(s) =
sn
sn+n
p=1(lp+p−1
q=1 kn+1−qlp−q+kn+1−p)sn−p .
(27)
Then,
it
follows
that
limw→0 |(L1,a(jw)/L1,b(jw))| = 0
and
limw→0 |(L2,a(jw)/L2,b(jw))| = 0,
thereby
verifying
Proposition 2.
□
This article has been accepted for inclusion in a future issue of this journal. Content is final as presented, with the exception of pagination. 
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 12:52:47 UTC from IEEE Xplore.  Restrictions apply.

## Page 11

LIU et al.: ON COMPENSATION FUNCTION OBSERVER-BASED ACTIVE DISTURBANCE REJECTION CONTROL
11
REFERENCES
[1] K. J. Åström and P. R. Kumar, “Control: A perspective,” Automatica,
vol. 50, no. 1, pp. 3–43, 2014.
[2] J. Chen, D. Ma, Y. Xu, and J. Chen, “Delay robustness of PID control
of second-order systems: Pseudoconcavity, exact delay margin, and
performance tradeoff,” IEEE Trans. Autom. Control, vol. 67, no. 3,
pp. 1194–1209, Mar. 2022.
[3] J. Han, “From PID to active disturbance rejection control,” IEEE Trans.
Ind. Electron., vol. 56, no. 3, pp. 900–906, Mar. 2009.
[4] Y. Cui, Z. Yin, P. Luo, D. Yuan, and J. Liu, “Linear active disturbance
rejection control of IPMSM based on quasi-proportional resonance and
disturbance differential compensation linear extended state observer,”
IEEE Trans. Ind. Electron., vol. 71, no. 10, pp. 11–91011924, Oct. 2024.
[5] S. Chen, Z. Chen, and Z.-L. Zhao, “Parameter selection and performance
analysis of linear disturbance observer based control for a class of
nonlinear uncertain systems,” IEEE Trans. Ind. Electron., vol. 70, no. 11,
pp. 11587–11597, Nov. 2023.
[6] Z. Li, C.-Y. Su, L. Wang, Z. Chen, and T. Chai, “Nonlinear disturbance
observer-based control design for a robotic exoskeleton incorporating
fuzzy approximation,” IEEE Trans. Ind. Electron., vol. 62, no. 9,
pp. 5763–5775, Sep. 2015.
[7] X. Dai, Y. Hu, D. Cui, and T. Chai, “A disturbance decoupling
generalized proportional-integral observer design for robust sensor fault
detection,” IEEE Trans. Ind. Electron., vol. 70, no. 6, pp. 6326–6336,
Jun. 2023.
[8] Y. Jiang, J. Yang, X. Wang, X. Lin, C. Chen, and S. Li, “Enhanced
optimal backlash compensation for transmission servo systems via a
reduced-order GPI observer: A switched control design,” IEEE Trans.
Ind. Electron., vol. 72, no. 10, pp. 10465–10475, Oct. 2025.
[9] L. M. Gallegos-Canales, A. Favela-Contreras, A. Ávila, and S. O.
MartÃnez-Chapa, “Embedded software implementation of the SISO
adaptive predictive control algorithm,” IEEE Trans. Ind. Electron.,
vol. 64, no. 9, pp. 7229–7238, Sep. 2017.
[10] M. Bin, D. Astolﬁ, and L. Marconi, “About robustness of control
systems embedding an internal model,” IEEE Trans. Autom. Control,
vol. 68, no. 3, pp. 1306–1320, Mar. 2023.
[11] I. Schimperna and L. Magni, “Robust offset-free constrained model
predictive control with long short-term memory networks,” IEEE Trans.
Autom. Control, vol. 69, no. 12, pp. 8172–8187, Dec. 2024.
[12] Z.-L. Zhao, Z.-P. Jiang, T. Liu, and T. Chai, “Global ﬁnite-time output-
feedback stabilization of nonlinear systems under relaxed conditions,”
IEEE Trans. Autom. Control, vol. 66, no. 9, pp. 4259–4266, Sep. 2021.
[13] W. M. Haddad and J. Lee, “Finite-time stabilization and optimal
feedback control for nonlinear discrete-time systems,” IEEE Trans.
Autom. Control, vol. 68, no. 3, pp. 1685–1691, Mar. 2023.
[14] J. Ni, S. Qian, J. Cao, W. Li, and F. Yang, “Predeﬁned-time consensus
tracking control for multiagent system with channel fading,” IEEE
Trans. Cybern., vol. 54, no. 8, pp. 4652–4665, Aug. 2024.
[15] Y. Huang and W. Xue, “Active disturbance rejection control: Method-
ology and theoretical analysis,” ISA Trans., vol. 53, no. 4, pp. 963–976,
2014.
[16] H. Cao, Y. Deng, Y. Zuo, X. Liu, J. Wang, and C. H. T. Lee, “A variable
structure ADRC for enhanced disturbance rejection and improved noise
suppression of PMSM speed system,” IEEE Trans. Ind. Electron.,
vol. 72, no. 5, pp. 4481–4495, May 2025.
[17] L. Sun, W. Xue, D. Li, H. Zhu, and Z-g Su, “Quantitative tuning of
active disturbance rejection controller for FOPTD model with applica-
tion to power plant control,” IEEE Trans. Ind. Electron., vol. 69, no. 1,
pp. 805–815, Jan. 2022.
[18] J. Zhao, Y. Zhang, H. Hou, Y. Yue, K. Meng, and Z. Yang, “Active
disturbance rejection control with backstepping for decoupling control
of hydraulic driven lower limb exoskeleton robot,” IEEE Trans. Ind.
Electron., vol. 72, no. 1, pp. 714–723, Jan. 2025.
[19] X. Shi, Y. Chen, and J. Huang, “Application of fractional-order active
disturbance rejection controller on linear motion system,” Control Eng.
Pract., vol. 81, pp. 207–214, Dec. 2018.
[20] W. Wei, W. Xue, and D. Li, “On disturbance rejection in magnetic
levitation,” Control Eng. Pract., vol. 82, pp. 24–35, Jan. 2019.
[21] Z. Gao, “Scaling and bandwidth-parameterization based controller tun-
ing,” in Proc. Am. Control Conf., vol. 6, 2003, pp. 4989–4996.
[22] Z.-L. Zhao and B.-Z. Guo, “A nonlinear extended state observer based
on fractional power functions,” Automatica, vol. 81, pp. 286–296, Jul.
2017.
[23] A. A. Godbole, J. P. Kolhe, and S. E. Talole, “Performance analysis of
generalized extended state observer in tackling sinusoidal disturbances,”
IEEE Trans. Control Syst. Technol., vol. 21, no. 6, pp. 2212–2223,
Nov. 2013.
[24] G. Tang, W. Xue, H. Peng, Z. Yang, and Y. Zhao, “Parallel multiple
extended state observers based ADRC with application to high-speed
precision motion stage,” IEEE Trans. Ind. Electron., vol. 71, no. 8,
pp. 9639–9648, Aug. 2024.
[25] H. Sun, R. Madonski, S. Li, Y. Zhang, and W. Xue, “Composite
control design for systems with uncertainties and noise using combined
extended state observer and kalman ﬁlter,” IEEE Trans. Ind. Electron.,
vol. 69, no. 4, pp. 4119–4128, Apr. 2022.
[26] Z. Pu, R. Yuan, J. Yi, and X. Tan, “A class of adaptive extended state
observers for nonlinear disturbed systems,” IEEE Trans. Ind. Electron.,
vol. 62, no. 9, pp. 5858–5869, Sep. 2015.
[27] X. Zhang, Y. Wang, W. Xue, and Y. Zhao, “Recursive projected ﬁlter
algorithm with binary-valued observations,” J. Syst. Sci. Complexity,
vol. 37, no. 5, pp. 1832–1860, 2024.
[28] G. Qi, X. Li, and Z. Chen, “Problems of extended state observer and
proposal of compensation function observer for unknown model and
application in UAV,” IEEE Trans. Syst., Man, Cybern.: Syst., vol. 52,
no. 5, pp. 2899–2910, May 2022.
[29] G. Qi, J. Hu, L. Li, and K. Li, “Integral compensation function observer
and its application to disturbance-rejection control of QUAV attitude,”
IEEE Trans. Cybern., vol. 54, no. 7, pp. 4088–4099, Jul. 2024.
[30] C. Wang, J. Yan, P. Heng, L. Shan, and X. Zhou, “Enhanced LADRC
for permanent magnet synchronous motor with compensation function
observer,” IEEE Trans. Emerg. Sel. Topics Power Electron., vol. 11,
no. 3, pp. 3424–3434, 2023.
[31] G. Qi, J. Deng, X. Li, and X. Yu, “Compensation function observer-
based model-compensation backstepping control and application in anti-
inference of quadrotor UAV,” Control Eng. Pract., vol. 140, 2023, Art.
no. 105633.
[32] W. Xue and Y. Huang, “Performance analysis of 2-DOF tracking
control for a class of nonlinear uncertain systems with discontinuous
disturbances,” Int. J. Robust Nonlinear Control, vol. 28, no. 4, pp. 1456–
1473, 2018.
[33] W. Tan and C. Fu, “Linear active disturbance-rejection control: Analysis
and tuning via IMC,” IEEE Trans. Ind. Electron., vol. 63, no. 4,
pp. 2350–2359, 2016.
[34] Z. Zhao, J. Zhang, Z. Liu, W. He, and K.-S. Hong, “Adaptive quantized
fault-tolerant control of a 2-DOF helicopter system with actuator fault
and unknown dead zone,” Automatica, vol. 148, 2023, Art. no. 110792.
Kaiwen Liu received the B.S. degree in statis-
tics in 2024 from the School of Mathematics
and Statistics, Shaanxi Normal University, Xi’an,
China, where he is currently working toward the
M.S. degree in applied mathematics.
His research interests include nonlinear sys-
tems and control and active disturbance rejec-
tion control.
This article has been accepted for inclusion in a future issue of this journal. Content is final as presented, with the exception of pagination. 
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 12:52:47 UTC from IEEE Xplore.  Restrictions apply.

## Page 12

12
IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS
Sen Chen (Member, IEEE) received the B.S.
degree in mathematics from Beihang Univer-
sity, Beijing, China, in 2014, and the Ph.D. de-
gree in operational research and cybernetics
from Academy of Mathematics and System Sci-
ences, Chinese Academy of Sciences, Beijing,
in 2019.
He is currently an Associate Professor with
the
School
of
Mathematics
and
Statistics,
Shaanxi Normal University, Xi’an, China. His
research interests include nonlinear system and
control, and reinforcement learning.
Zhi-Liang Zhao (Member, IEEE) received the
B.S. degree from Shaanxi Normal University,
Xi’an, China, in 2003, the M.S. degree from
Huazhong University of Science and Technol-
ogy, Wuhan, China, in 2007, and the Ph.D. de-
gree from the University of Science and Tech-
nology, Wuhan, in 2012, all in mathematics.
He is currently a Professor with the School of
Electrical and Control Engineering, North Uni-
versity of China, Taiyuan, China. His research
interests include nonlinear systems and control,
and active disturbance rejection control.
Wenchao Xue (Member, IEEE) received the
B.S.degree in applied mathematics from Nankai
University, Tianjin, China, in 2007, and the Ph.D.
degree in control theory from the Academy of
Mathematics and Systems Science (AMSS),
Chinese Academy of Sciences (CAS), Beijing,
China, in 2012.
He is currently a Professor with the Key Lab-
oratory of System and Control, AMSS, CAS.
His research interests include nonlinear uncer-
tain systems control, active disturbance rejec-
tion control, and nonlinear uncertain systems ﬁlter.
Dr. Xue also serves as an Associate Editor for the IFAC Journal of
Control Engineering Practice.
This article has been accepted for inclusion in a future issue of this journal. Content is final as presented, with the exception of pagination. 
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on March 15,2026 at 12:52:47 UTC from IEEE Xplore.  Restrictions apply.
