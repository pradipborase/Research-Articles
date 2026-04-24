# Prescribed-Time_Robust_Synchronization_of_Networked_Heterogeneous_Euler-Lagrange_Systems.pdf

## Page 1

12160
IEEE TRANSACTIONS ON AUTOMATION SCIENCE AND ENGINEERING, VOL. 22, 2025
Prescribed-Time Robust Synchronization of
Networked Heterogeneous
Euler-Lagrange Systems
Gewei Zuo , Yaohang Xu, Mengmou Li , Member, IEEE, Lijun Zhu , Member, IEEE,
and Han Ding , Member, IEEE
Abstract— In this paper, we propose a prescribed-time synchro-
nization (PTS) algorithm for networked Euler-Lagrange systems
subjected to external disturbances. Notably, the system matrix
and the state of the leader agent are not accessible to all
agents. The algorithm consists of distributed prescribed-time
observers and local prescribed-time tracking controllers, dividing
the PTS problem into prescribed-time convergence of distributed
estimation errors and local tracking errors. Unlike most existing
prescribed-time control methods, which achieve prescribed-time
convergence by introducing specific time-varying gains and
adjusting feedback values, we establish a class of KT functions
and incorporate them into comparison functions to represent
time-varying gains. By analyzing the properties of class KT and
comparison functions, we ensure the prescribed-time convergence
of distributed estimation errors and local tracking errors, as well
as the uniform boundedness of internal signals in the closed-loop
systems. External disturbances are handled and dominated by
the time-varying gains that tend to infinity as time approaches
the prescribed time, while the control signal is still guaranteed
to be bounded. Finally, a numerical example and a practical
experiment demonstrate the effectiveness and innovation of the
algorithm.
Note to Practitioners—This paper aims to address the issue of
prescribed-time synchronization for networked Euler-Lagrange
systems. Existing research on asymptotic and finite-time conver-
gence reveals that the settling time for synchronization is signif-
icantly influenced by the system’s initial values and controller
parameters, making it challenging to be freely pre-designed.
In
contrast,
our
proposed
prescribed-time
synchronization
Received 14 October 2024; revised 3 January 2025; accepted 26 January
2025. Date of publication 11 February 2025; date of current version 16 April
2025. This article was recommended for publication by Associate Editor
H. Yan and Editor G. Fortino upon evaluation of the reviewers’ comments.
This work was supported in part by the National Natural Science Foundation
of China under Grant 62173155 and Grant 52188102; in part by the Program
for the Huazhong University of Science and Technology (HUST) Academic
Frontier Youth Team; and in part by the Taihu Lake Innovation Fund for
Future Technology, HUST. (Corresponding author: Lijun Zhu.)
Gewei Zuo and Yaohang Xu are with the School of Artificial Intelligence
and Automation, Huazhong University of Science and Technology, Wuhan
430072, China (e-mail: gwzuo@hust.edu.cn; yhxu@hust.edu.cn).
Mengmou
Li
is
with
the
Graduate
School
of
Advanced
Science
and Engineering, Hiroshima University, Higashihiroshima 739-0046, Japan
(e-mail: mmli.research@gmail.com).
Lijun Zhu is with the School of Artificial Intelligence and Automation
and the Key Laboratory of Imaging Processing and Intelligence Control,
Huazhong University of Science and Technology, Wuhan 430072, China
(e-mail: ljzhu@hust.edu.cn).
Han Ding is with the State Key Laboratory of Intelligent Manufacturing
Equipment and Technology, Huazhong University of Science and Technology,
Wuhan 430074, China (e-mail: dinghan@mail.hust.edu.cn).
Digital Object Identifier 10.1109/TASE.2025.3541052
algorithm ensures that all Euler-Lagrange systems achieve syn-
chronization within a prescribed time. The effectiveness of our
algorithm has been validated through numerical simulations and
physical experiments. In practical applications, our algorithm can
be utilized for cooperative control in robotic manipulators and
drones. Compared to traditional PD controllers, our proposed
algorithm not only offers the advantage of arbitrary settling
time configuration in cooperation but also ensures faster response
speeds and higher control accuracy, owing to the incorporation
of time-varying gains.
Index
Terms— Prescribed-time
synchronization,
Euler-
Lagrange systems, comparison functions, multi-agent systems.
I. INTRODUCTION
I
N RECENT years, synchronization (or consensus) of net-
worked Euler-Lagrange systems has received increasing
attention due to its great application potential in drone
swarms [1] and multi-robot systems [2], etc. Early studies [3],
[4], [5], [6], [7], [8] explored the asymptotic synchronization
of these systems, achieving synchronization errors approach-
ing zero as time extends infinitely.
Compared with the asymptotic stability theory, finite-time
control [9], [10] offers improved convergence performance
and enhanced disturbance rejection capabilities. Research
on finite-time synchronization of networked Euler-Lagrange
systems, as illustrated in [11] and [12], indicates that the
settling time has an upper bound that generally depends on
initial values and control parameters. Furthermore, studies
on fixed-time synchronization [13], [14] indicate that the
finite settling time is invariant with respect to initial values,
although control parameters still play a role. Practical fixed-
time synchronization, introduced in [15], ensures convergence
within a fixed time to a neighborhood of zero synchronization
error. According to [16] and [17], both finite-time and fixed-
time synchronization for multi-agent systems (MASs) are
impacted by external disturbances, making the upper bound
of the settling time uncomputable in advance. Alternatively,
if these disturbances do not alter the settling time, only prac-
tical fixed-time convergence is typically achieved, resulting
in convergence to a neighborhood of zero rather than exact
zero-error, as noted in [15] and [18]. Consequently, neither
the upper bound nor the precise settling time can be estimated
prior to system operation. Moreover, without disturbances,
determining settling time requires awareness of each agent’s
1558-3783 © 2025 IEEE. All rights reserved, including rights for text and data mining, and training of artificial intelligence
and similar technologies. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:38:30 UTC from IEEE Xplore.  Restrictions apply.

## Page 2

ZUO et al.: PRESCRIBED-TIME ROBUST SYNCHRONIZATION OF EULER-LAGRANGE SYSTEMS
12161
initial values [19]. Thus, these approaches may fall short
when specific settling time constraints are required, primarily
due to unforeseen disturbances and locality of agents’ initial
values [20].
As an extension of finite-time control, prescribed-time
control is introduced in [21], where the settling time is
prescribed as the name suggests and independent of initial
values and any other design parameters. Its application to
a single Euler-Lagrange system is discussed in [22], and
it has been further extended to various MASs. Examples
include linear MASs [23], single-integrator MASs [24], [25],
double-integrator MASs [26], chain-integrator MASs [27],
and strict-feedback MASs [28], [29]. Prescribed-time control
has also been applied to different forms of synchronization.
These include synchronization in the leaderless case [30],
the leader-follower case [31], containment control [32], and
formation control [33], among others. Notably, practical
prescribed-time consensus for chain-integrator MASs is pro-
posed in [29], in which fuzzy logic and the adaptive method
are adopted to handle dead-zone input and sensor faults.
Moreover, an event-triggered communication mechanism-
based prescribed-time consensus is proposed in [34], showing
that practical prescribed-time convergence still holds under
discrete-time communication.
Although prescribed-time control has been successfully
extended to various forms of MASs and synchronization
control types, the specific solution for prescribed-time syn-
chronization in networked Euler-Lagrange systems within
a leader-follower framework remains unexplored. This gap
in the literature motivates our study. Current studies on
prescribed-time control for MASs, as seen in [23], [24],
[25], [26], [27], [28], and [29], predominantly focus on
systems without external disturbances, neglecting the aspects
of robustness and disturbance rejection through prescribed-
time control. While some studies, like [29] and [34], propose
practical prescribed-time control with time-varying gains that
have finite upper bounds, these only ensure convergence to
a neighborhood of zero. Our approach diverges from tradi-
tional finite-time [11], [12] and fixed-time synchronization
methods [13], [14], which rely on fractional-power feed-
back. Instead, we accomplish prescribed-time convergence of
synchronization errors by implementing time-varying gains
that grow indefinitely. This ensures that the settling time is
independent of initial values and design parameters, provid-
ing uniform convergence across all agents. However, given
the complexity inherent to high-order nonlinear systems in
prescribed-time control, and the potential destabilization from
unbounded time-varying gains, particularly in the presence of
external disturbances, this task is challenging.
In this paper, we address the robust PTS problem for
networked Euler-Lagrange systems subjected to external
disturbances. The main features and contributions are summa-
rized as follows: (i) We develop distributed prescribed-time
observers for followers to estimate the leader system’s infor-
mation, including its state and system matrix. This allows
us to tackle the PTS problem by addressing prescribed-time
stabilization of both distributed estimation errors and local
tracking errors. Distributed controllers are then designed using
time-varying state transformations and sliding mode control.
(ii) Contrary to existing prescribed-time control methods that
rely on introducing specific time-varying gains, we construct
a class of KT functions and integrate them into a comparison
function. These are incorporated into the feedback loop as
time-varying gains. This approach is theoretically more gen-
eral, offering greater design flexibility and enabling various
forms of prescribed-time convergence. (iii) In the presence
of external disturbances, unbounded time-varying gains may
excessively amplify these disturbances, potentially causing
unbounded internal signals in closed-loop systems. To address
this, we propose sufficient conditions for combining the class
KT and comparison functions. These conditions ensure a
sufficient prescribed-time convergence rate, achieving not only
PTS but also guaranteeing the boundedness of all internal
signals in closed-loop MASs, thus mitigating the impact of
external disturbances on prescribed-time convergence.
The rest of the paper is organized as follows. Section II
gives the notations and problem formulation. Section III
constructs the KT and DT functions. The main results of the
proposed PTS algorithm are presented in Section IV. Numer-
ical and experimental results are performed in Section V.
Finally, Section VI concludes this paper.
II. NOTATIONS AND PROBLEM FORMULATION
A. Notations
R, R+, and Rn denote the set of real numbers, the set of
non-negative real numbers, and the n-dimensional Euclidean
space, respectively. Rn×m denotes the set of real matrices with
dimensions n by m. t0 denotes the initial time, T > 0 denotes
the prescribed time, and Tp denotes the time interval Tp =
{t : t0 ≤t < T + t0}. For a positive definite matrix A,
λA and ¯λA denote the minimum and maximum eigenvalues
of A, respectively. |A|2 = max{λ(A⊤A)} denotes the 2-norm
of a matrix A with λ(A⊤A) being the spectrum of A⊤A.
For a matrix s = [s1, · · · , sn] ∈Rn×n where si ∈Rn for
i = 1, · · · , n, vec(s) = [s⊤
1, · · · , s⊤
n ]⊤∈Rnn. For a Ck function
(i.e., k-times continuously differentiable) µ(t) : R →R,
dkµ(t)/dtk is its k-th derivative with respect to t.
B. Multi-Agent Systems
Consider a group of n-link robotic manipulators described
by the Euler-Lagrange dynamics, for i = 1, · · · , N,
˙qi = ri,
˙ri = M−1
i
(qi)(τi −di(t) −Ci(qi,ri)ri −Gi(qi))
(1)
where qi ∈Rn and ri ∈Rn are the vectors of generalized posi-
tion and velocity of the i-th robotic manipulator, respectively.
The symmetric and positive definite matrix Mi(qi) : Rn →
Rn×n is the inertia matrix, Ci(qi,ri) : Rn × Rn →Rn×n
is the matrix related to the Coriolis and centrifugal forces,
Gi(qi) : Rn →Rn is the gravitational torque, di(t) ∈Rn
denotes the external disturbance, and τi ∈Rn is the vector
of control forces. According to [35], some properties and
assumptions for system (1) are presented as follows.
Property 1: Mi(qi), Ci(qi,ri) and Gi(qi) in (1) satisfy the
following properties: kn In ≤Mi(qi) ≤k ¯n In, ∥Ci(qi,ri)∥≤
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:38:30 UTC from IEEE Xplore.  Restrictions apply.

## Page 3

12162
IEEE TRANSACTIONS ON AUTOMATION SCIENCE AND ENGINEERING, VOL. 22, 2025
kc∥ri∥, and ∥Gi(qi)∥≤kg for qi,ri ∈Rn and i = 1, · · · , N,
where kn, k ¯n, kc and kg are some positive constants.
Assumption 1: di(t) satisfies supt∈[t0,∞) ∥di(t)∥≤
¯di for
i = 1, · · · , N, where ¯di is a positive, finite constant that does
not need to be known.
We call the i-th robotic manipulator agent i. The reference
trajectory is generated by a system, labeled agent 0, and
described by
˙υ0 = S0υ0
(2)
where S0 ∈Rn×n is a constant matrix, and υ0 ∈Rn is the
desired trajectory to be tracked.
We first review some terminologies in graph theory to
describe the interaction among agents. Denote a directed graph
G = (V, E) with the node set V = {0, 1, · · · , N} and the
edge set E ⊆V × V. The existence of the edge (i, j) ∈E
indicates that agent j can obtain information from the i-th
agent. Denote the node set ¯V = {1, · · · , N} without node 0.
Agent j is called a neighbor of i if ( j, i) ∈E. The set of
neighbors of agent i is denoted by Ni = { j ∈V : ( j, i) ∈E}.
Denote by A = [ai j] ∈R(N+1)×(N+1) the weighted adjacency
matrix of G, where ai j > 0 if ( j, i) ∈E and ai j = 0, otherwise.
Self-edges are not allowed, i.e., aii = 0. The Laplacian matrix
of the graph is denoted as L = [li j] ∈R(N+1)×(N+1), where
lii = PN
j=0ai j, and li j = −ai j with i ̸= j.
For the MASs consisting of (1) and (2), we associate node
0 with system (2) and call it the leader. The other nodes are
associated with system (1) and are called followers. In this
paper, we assume S0 and υ0 are known only to the neighbors
of the leader system.
Assumption 2: The graph G contains a spanning tree with
node 0 as the root.
Remark 1: Let 1 = diag{a10, · · · , aN0}, then the Laplacian
L of G can be expressed as
L =
" PN
j=1a0 j −(a01, · · · , a0N)
−11N
H
#
.
As shown in [36], under Assumption 1, all elements of λ(H)
have positive real parts, and H satisfies H1N = 11N.
C. Problem Formulation
To the best of our knowledge, the prescribed-time control
for nonlinear systems is generally based on three approaches.
The time-varying state transformation method [21] con-
verts the prescribed-time convergence of original states into
a boundedness problem of the transformed variables. The
time-varying gain method [37] increases the control gain to
infinity as time approaches the prescribed time instance. The
last approach is essentially a finite-time control method, which
achieves prescribed-time stability through a fractional-power
state feedback and a suitable selection of control param-
eters [38]. This method has been successfully applied to
first-order systems and some canonical systems, while its
effectiveness has not been verified for nonlinear systems with
a relative degree greater than one. Moreover, this method
can only guarantee that the upper bound of settling time is
prescribed, while the actual settling time is also affected by
initial values and control parameters, leading to inconsistency
across agents. Therefore, in this paper, we adopt the first
two methods where a class of functions will be useful for
the time-varying state transformation and the prescribed-time
control later, and it is defined as follows.
Definition 1: A twice differentiable function µ : Tp →
[a0, ∞) is said to belong to the class KT if it is strictly
increasing with
dkµ(t)
dtk

t=t0 = ak,
lim
s→t0+T
dkµ(t)
dtk

t=s = ∞
for ∀k = 0, 1, 2, where ak is a positive constant possibly
related to T and there exist finite numbers wk > 0 and
ιk > 1 such that
µ(k)(t) ≤wk
µ(k−1)(t)
ιk,
∀t ∈Tp, k = 1, 2.
(3)
A function ϕ : Tp →(0, b] is said to belong to class DT , if it
is strictly decreasing with ϕ(t0) = b and limt→t0+T ϕ(t) =
0 where b is a positive constant possibly related to T .
Remark 2: A few examples of KT functions are µ(t) =
(T + t0 −t)−m, µ(t) = exp
(T + t0 −t)−1
and µ(t) =
ζ 1/(T +t0−t) with some constants ζ > 1 and m > 0.
A class of functions is defined as an extension to K∞
and KL functions (Definitions 4.2 and 4.3 in [39]) that have
different domains.
Definition 2: A function α : [0, ∞) →[a, ∞) is said to
belong to class Ke
∞if it is strictly increasing and α(0) =
a > 0. A
continuous function β : [0, c) × Tp →[0, ∞) is
said to belong to class KLT if, for each fixed s, the mapping
β(r, s) belongs to class K with respect to r and, for each
fixed r, the mapping β(r, s) is decreasing with respect to s
and β(r, s) →0 as s →t0 + T .
We then give the definition of prescribed-time convergence
as follows.
Definition 3 (Prescribed-Time Convergence): Consider the
system
˙x = f (x, d(t), t),
x(t0) = x0,
e = h(x, d(t), t)
where x ∈Rn is the state, d(t) : [t0, ∞) →Rnd is the external
input, e ∈Rp is the output, and x0 is the initial state at the
initial time t0. For a given T > 0, the system output is said
to achieve prescribed-time convergence (towards zero within
T ) if there exists a KLT function β such that, for any x0 and
any d(t),
∥x(t)∥≤β(∥¯x0∥, t), ∀t ∈Tp
where ∥¯x0∥=
q
∥x0∥2 + ∥d(t)∥2
[t0,∞).
This paper aims to propose a distributed control law in the
form of
˙Si = σS,i(P
j∈Niai j(Sj −Si), µ(t)),
˙υi = συ,i(P
j∈Niai j(υ j −υi), Si, µ(t)),
τi = στ,i(qi,ri, υi, ˙υi, µ(t)), i ∈¯V
(4)
with functions σS,i, συ,i, and στ,i to be designed and µ(t) ∈
KT . Since the state and matrix of the leader (2) are only
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:38:30 UTC from IEEE Xplore.  Restrictions apply.

## Page 4

ZUO et al.: PRESCRIBED-TIME ROBUST SYNCHRONIZATION OF EULER-LAGRANGE SYSTEMS
12163
accessible to a subset of followers via the communication
network, Si- and υi-dynamics in (4) are constructed for each
follower to obtain the estimation of the leader’s state υ0 and
matrix S0, respectively. Let ei = qi−v0 and e = [e⊤
1, · · · , e⊤
N]⊤.
Compared with the exponential synchronization in [36]
and fixed-time synchronization in [14], we introduce the
time-varying transformation for the prescribed-time stability
and thus µ(t) is introduced in (4). Then, the prescribed-time
synchronization problem is defined as follows.
Prescribed-Time Synchronization Problem: Given the sys-
tem composed of (1) and (2) that communicate through
directed graph G. For a prescribed time T > 0, design a
distributed control law of the form (4) such that, for all
bounded initial values, the synchronization error e of the
closed-loop system achieves prescribed-time convergence in
the sense of Definition 3 and all internal signals are bounded.
III. KT AND DT FUNCTIONS
In this section, we discuss the properties of KT and DT
functions and their involvement in the Lyapunov stability
analysis. We simplify µ(t) and ˙µ(t) to µ and ˙µ throughout this
paper if no confusion arises. For γ ∈K∞, the incorporation of
class KT and comparison functions is defined as γ (µ). Define
κι(γ (µ)) = exp
ι
R t
t0γ (µ(s))ds

, t ≥t0,
(5)
κι(γ (µ(ζ))) = exp
ι
R ζ
t0γ (µ(s))ds

, ζ ≥t0
(6)
where ι is a constant and γ ∈K∞. We then have the following
propositions and lemmas.
The proof of Proposition 1 is
straightforward and omitted here, while the other proofs are
listed the in appendix.
Proposition 1: Let µ ∈KT and γ ∈K∞. Then κ−1(γ (µ))
is a DT function satisfying κ−1(γ (µ)) < 1. If α ∈K∞or
α ∈Ke
∞, β(r, t) = α(r)κ−c(γ (µ)) for any c > 0 is a KLT
function.
Proposition 2: Let µ ∈KT with some ι1 and w1 satisfy-
ing (3). For some γ ∈K∞and any c1, c2 > 0, the function
(γ (µ))c1κ−c2(γ (µ)) belongs to class DT for t ∈Tp if the
function γ (s) satisfies
dγ (s)
ds
≤εw−1
1
c2
c1
s−ι1(γ (s))2
(7)
for
s
∈
[a0, ∞)
and
0
<
ε
<
1.
Moreover,
(γ (µ))c1κ−c2(γ (µ))
≤
ϵ1κ−(1−ε)c2(γ (µ))
where
ϵ1
=
(γ (a0))c1 and a0 = µ(t0).
Proposition 3: Let µ ∈KT with some ι1, ι2, w1 and
w2 satisfying (3). Define
¯γ (t) = ˙γ (µ(t)) + γ 2(µ(t)) + γ (µ(t)).
(8)
Suppose the conditions of Proposition 2 hold with γ (s) further
satisfying
d2γ (s)
ds2
+ dγ (s)
ds
w2wι2−1
1
sι1(ι2−1) ≤εcdγ (s)
ds
γ (s)
(9)
for s ∈[a0, ∞) and 0 < ε < 1. Then, for any c ≥2c2/c1,
¯γ (t)κ−c(γ (µ)) belongs to class DT for t ∈Tp. Moreover,
¯γ (t)κ−c(γ (µ)) ≤ϵ2κ−2(1−ε)c2
c1
(γ (µ)) where ϵ2 = ˙γ (µ(t0)) +
γ (a0) + (γ (a0))2.
Lemma 1: Let µ ∈KT and γ1, γ2 ∈K∞. Consider a system
˙x = f (x, d) where x ∈Rn and d ∈Rnd. If there exists a
positive definite function V (x) = x ⊤Px where P > 0 such
that its derivative along x-dynamics satisfies
˙V ≤−(c1γ1(µ(t)) −c2)V + c3κ−c1(γ2(µ))
(10)
for any positive numbers c1
>
0, c2, c3
∈
R and
γ1(s) −γ2(s)
<
0 for s
∈
[a0, ∞), then ∥x(t)∥
≤
α(∥x(t0)∥)κ−c1/2(γ1(µ)), where α is a Ke
∞function if c3 ̸= 0,
and otherwise a K∞function.
Lemma 2: Let µ ∈KT and γ ∈K∞. Consider a system
˙x = f (x, d) where x ∈Rn and d ∈Rnd. If there exists a
positive definite function V (x) = x ⊤Px where P > 0 such
that its derivative along x-dynamics satisfies
˙V ≤−c1γ (µ)V + c2γ (µ)
(11)
for some constants c1 > 0, c2 ∈R, then ∥x(t)∥≤α(∥x(t0)∥),
where α is a Ke
∞function.
Remark 3: There are many choices for γ (s) to satisfy
the conditions in Proposition 2 and 3. For example, for a
given µ ∈KT , any 0 < ε < 1, and c1, c2 > 0, one can find
m ≥max{ι1 −1, ι1(ι2 −1)}, k > c1mω1/(am+1−ι1
0
c2ε) and
c
>
max{2ωι2−1
1
ω2/(εkam−ι1(ι2−1)
0
), 2(m −1)/(kεam+1
0
)},
where
a0
=
µ(t0)
and
ιi,
ωi
are
given
in
Definition
1.
Let
γ (s)
=
ksm.
We
can
check
W
dγ (s)
ds
=
εω−1
1 c2c−1
1 s−ι1(γ (s))2ε−1ω1c1c−1
2 mk−1sι1−m−1
≤
εw−1
1
c2
c1 s−ι1(γ (s))2
and
d2γ (s)
ds2
+
dγ (s)
ds w2wι2−1
1
sι1(ι2−1)
=
k2m(m −1)s2m−2 + kmω2ωι2−1
1
sm−1+ι1(ι2−1) ≤εc dγ (s)
ds γ (s).
Thus, the conditions in Propositions 2 and 3 are satisfied.
Remark 4: The motivation behind Propositions 1 and 2
is to analyze the prescribed-time convergence of a nominal
system. Consider, for instance, the single-integrator system
described by ˙x = u, where x ∈R is the state and u ∈R
is the control input. Suppose the control input is given by
u = −cγ (µ)x, with c > 0 and µ ∈KT . Proposition 1
asserts that x achieves the prescribed-time convergence to
zero for any c > 0. To guarantee the boundedness of u,
it is necessary to demonstrate that γ (µ)κ−c(γ (µ)) < ∞.
Proposition 2 provides that this condition is met if γ (s)
satisfies dγ (s)
ds
< w−1
1 cs−ι1(γ (s))2. Additionally, Proposition 3
is employed to establish prescribed-time convergence in more
complex scenarios.
Remark 5: In this paper, both Propositions 2 and 3 are
integral to proving the prescribed-time convergence of relevant
states and the uniform boundedness of terms associated with
µ. Lemma 1 sets the conditions on the Lyapunov function nec-
essary for deriving prescribed-time convergence. Meanwhile,
Lemma 2 is utilized to validate the boundedness of the new
state after implementing time-varying state transformations
within the closed-loop system.
IV. MAIN RESULTS
In this section, we first establish distributed prescribed-time
observers to estimate the leader’s state υ0 and the system
matrix S0, which will be used to construct prescribed-time
synchronization
controllers.
Second,
we
design
local
prescribed-time
tracking
controllers
by
utilizing
the
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:38:30 UTC from IEEE Xplore.  Restrictions apply.

## Page 5

12164
IEEE TRANSACTIONS ON AUTOMATION SCIENCE AND ENGINEERING, VOL. 22, 2025
time-varying state transformation and sliding-mode control
method, and prove the prescribed-time convergence of the
synchronization errors.
A. Prescribed-Time Observer
We construct the distributed prescribed-time observers as
follows
˙Si = γs(µ(t))P
j∈Vai j(Sj −Si),
(12)
˙υi = Siυi + γυ(µ(t))P
j∈Vai j(υ j −υi), i ∈¯V
(13)
where γs, γυ are differentiable K∞functions to be designed
and µ is a KT function. We note γs(µ(t)) and γυ(µ(t)) are
KT functions.
In (12) and (13), Si and υi denote the i-th agents’ estima-
tions for the leader’s system matrix and state, respectively.
Let S =

S⊤
1, · · · , S⊤
N
⊤and υ =

υ⊤
1 , · · · , υ⊤
N
⊤. Denote
˜Si = Si −S0 and ˜υi = υi −υ0 as the i-th local estimation
errors for Si and vi, respectively. Let
˜S =
 ˜S
⊤
1, · · · , ˜S
⊤
N
⊤,
˜υ =

˜υ
⊤
1, · · · , ˜υ
⊤
N
⊤
(14)
as the extended estimation errors. Taking time derivative of ˜S
yields
˙˜S = −γυ(µ)(H ⊗In)S + γυ(µ)(1 ⊗In)(1N ⊗S0)
= −γυ(µ)(H ⊗In)S + γυ(µ)(11N) ⊗(InS0)
= −γυ(µ)(H ⊗In)S + γυ(µ)(H1N) ⊗(InS0)
= −γυ(µ)(H ⊗In)S + γυ(µ)(H ⊗In)(1N ⊗S0)
= −γs(µ)(H ⊗In) ˜S.
(15)
where we used 11N = H1N (see Remark 1). Similarly, taking
time derivative of ˜υ yields ˙˜υ = −γυ(µ)(H ⊗In) ˜υ + 3s ˜υ +
3˜s(1N ⊗υ0) where
3s = diag

S1, · · · , SN
	
, 3˜s = diag
 ˜S1, · · · , ˜SN
	
.
(16)
By Remark 1, there always exist positive matrices P and
Q such that −P(H ⊗In) −(H ⊗In)⊤P = −Q holds. Define
ζ = λQ ¯λ−1
P . Then, we have the following lemma.
Lemma 3: Consider the leader (2) and observers (12)-(13)
in a directed graph G
under Assumption 2. Suppose µ ∈KT , and γs, γυ satisfy
γυ(s) −γs(s) < 0, ∀s ∈[a0, ∞) with a0 = µ(t0). Then, ˜S(t)
and ˜υ(t) in (14) achieve prescribed-time convergence toward
zero within T + t0, i.e., there exist KLT functions βs and βυ
such that
∥˜S(t)∥≤βs(∥˜S(t0)∥, t) = αs(∥˜S(t0)∥)κ−ζ
2 (γs(µ)),
(17)
∥˜υ(t)∥≤βυ(∥˜υ(t0)∥, t) = αυ(∥˜υ(t0)∥)κ−ζ
2 (γυ(µ))
(18)
where αs
∈
K∞and αυ
∈
Ke
∞, and κ−ζ
2 (γs(µ)) and
κ−ζ
2 (γυ(µ)) are defined in the sense of (5). Moreover, S(t)
and υ(t) are bounded for t ∈Tp, i.e.,
∥S(t)∥≤¯s = βs(∥˜S(t0)∥, t0) + ∥1N ⊗S0∥,
(19)
∥υ(t)∥≤¯υ = βυ(∥˜υ(t0)∥, t0) + sup
t∈TP
∥1N ⊗υ0(t)∥,
(20)
where ¯s and ¯υ are some positive finite constants.
Proof: First, we rewrite (15) as
dvec( ˜S)
dt
= −γs(µ(t))(In ⊗H ⊗In)vec( ˜S).
(21)
Define
the
Lyapunov
candidate
functions
as
V ( ˜S)
=
vec( ˜S)⊤(In ⊗P)vec( ˜S) and U( ˜υ) =
˜υ⊤P ˜υ, where P ∈
RNn×Nn is a positive definite matrix.
Due to (21), ˙V ( ˜S) ≤−ζγs(µ(t))V ( ˜S). Invoking the com-
parison lemma yields V ( ˜S(t)) ≤κ−ζ(γs(µ))V ( ˜S(t0)), which
implies ∥vec( ˜S(t))∥≤¯λPλ−1
P ∥vec( ˜S(t0))∥κ−ζ/2(γs(µ)). Note
that ∥˜S∥= θ∥˜S∥F = θ∥vec( ˜S)∥for some 0 < ϑ < ∞, where
∥˜S∥F denotes the Frobenius norm of matrix ˜S. Therefore, (17)
holds with αs(∥˜S(t0)∥) = ¯λpλ−1
P ∥˜S(t0)∥.
Thus, the prescribed-time convergence is achieved for ˜S.
Noting that βs(∥˜S(t0)∥, t) is strictly decreasing with respect to
t, then ∥˜S(t)∥has an upper bound βs(∥˜S(t0)∥, t0) and tends
to zero as t →T +t0, that is limt→T +t0 Si(t) = S0, i ∈¯V . Due
to ˜S(t) = S(t)−1N ⊗S0, one has ∥S(t)∥≤∥˜S(t)∥+∥1N ⊗S0∥.
Therefore, Si(t) is bounded for t ∈Tp as in (19). The time
derivative of U( ˜υ) satisfies
˙U( ˜υ) = −γυ(µ(t)) ˜υ
⊤Q ˜υ + 2 ˜υ
⊤P(3s ˜υ + 3˜s ¯υ0)
≤−γυ(µ(t))λQ∥˜υ∥2 + 2 ˜υ
⊤P(3s ˜υ + 3˜s ¯υ0)
where ¯υ0 = 1N ⊗υ0(t).
Due
to
(17)
and
(19),
one
has
2 ˜υ⊤P3s ˜υ
≤
2 ¯3s∥P∥∥˜υ∥2
with
¯3s
=
supt∈Tp ∥3s(t)∥,
where
we
note ¯3s < ∞due to (19). Furthermore, 2 ˜υ⊤P3˜s(1N ⊗υ0) ≤
∥˜υ∥2
+
∥P∥2supt∈Tp ∥¯υ0(t)∥
2α2
s (∥˜S(t0)∥)κ−ζ(γs(µ)).
Therefore,
˙U satisfies
˙U( ˜υ) ≤−(ζγυ(µ(t)) −c)U( ˜υ) +
dκ−ζ(γs(µ)),
where
c
=
2 ¯3s∥P∥+ 1

λ−1
P
and
d = ∥P∥2supt∈Tp ∥¯υ0(t)∥
2α2
s (∥˜S(t0)∥).
Applying Lemma 1 with c1 = ζ, c2 = c, c3 = d,
γ1(µ) = γυ(µ) and κ−1(γ2(µ)) = κ−1(γs(µ)) leads to
∥˜υ(t)∥≤αυ( ˜υ(t0))κ−ζ/2(γυ(µ)), where αυ ∈Ke
∞can be
calculated according to the proof of Lemma 1. Therefore,
(18) as well as the prescribed-time convergence is achieved
for ˜υ. Since βυ(∥˜υ(t0)∥, t) is strictly decreasing for t ∈Tp,
then ˜υ(t) has an upper bound βυ(∥˜υ(t0)∥, t0). Due to ˜υ(t) =
υ(t)−1N ⊗υ0(t), one obtains ∥υ(t)∥≤∥˜υ(t)∥+∥1N ⊗υ0(t)∥.
Thus υ(t) is bounded for t ∈Tp as in (20). This completes
the proof.
Remark 6: Most results in the existing literature introduce
specific time-varying gains for the prescribed-time control,
such as µ(t) = (T/(T +t0−t))m with m ∈N+ in [21], µ(t) =
tan

π(t+t0)
2(T +t0)

+ 1 in [40], and µ(t) =
exp(c(T +t0))−1
exp(c(T +t0))−exp(c(t+t0))
with c ∈R+ in [41]. In this paper, we introduce a general
class of KT functions in Definition 1 and incorporate them
into K∞functions for the prescribed-time control in (12)
and (13). Then, we investigate the conditions for KT functions
to achieve the prescribed-time convergence in Lemma 3 and,
later on, establish a more general approach.
B. Controller Design and Prescribed-Time Stability Analysis
For i-th agent, we denote
ei =
 ei1
ei2

=
 qi −v0
ri −S0v0

, i ∈¯V
(22)
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:38:30 UTC from IEEE Xplore.  Restrictions apply.

## Page 6

ZUO et al.: PRESCRIBED-TIME ROBUST SYNCHRONIZATION OF EULER-LAGRANGE SYSTEMS
12165
as the real tracking error of the i-th follower towards the leader.
Note that ei may not be available for the i-th agent since
v0 and S0 are only known to the neighbors of the leader system.
Therefore, we denote
ˆei =
 ˆei1
ˆei2

=
 qi −vi
ri −˙vi

, i ∈¯V
(23)
as the local tracking error. Then, the relationship between ei
and ˆei is
ei = ˆei + ˜ei
(24)
where
˜ei =
 ˜vi
zi

=
 vi −v0
˙vi −S0v0

, i ∈¯V.
(25)
Therefore, PTS is achieved if the prescribed-time convergence
is achieved for ˆei and ˜ei. Lemma 3 shows that the prescribed-
time convergence is achieved for ˜v. The next lemma shows
that the prescribed-time convergence is achieved for z, where
z =

z⊤
1, · · · , z⊤
N
⊤=

( ˙υ1 −S0υ0)⊤, · · · , ( ˙υ N −S0υ0)⊤⊤.
Lemma 4: Suppose conditions of Lemma 3 hold, and the
functions γs, γυ satisfy (7) in Proposition 2 with c2/c1 ≤
ζ/2 and µ ∈KT . Then, the prescribed-time convergence is
achieved for z, i.e., there exists a KLT function ˜βz such that
∥z(t)∥≤˜βz(∥ϑz(t0)∥, t)) = αz(∥ϑz∥)κ−(1−ε)ζ
2
(γυ(µ))
(26)
where ϑz =

(vec( ˜S))⊤, ˜υ⊤⊤and αz ∈K∞. Moreover, there
exists a KLT function ˜βs such that
∥˙S(t)∥≤˜βs(∥˜S(t0)∥, t) = ˜αs(∥˜S(t0)∥)κ−(1−ε)ζ
2
(γs(µ))
(27)
where ˜αs ∈K∞.
Proof: Due to (12) and (13), ˙S and ˙υ can be described
as follows:
˙S = −γs(µ)(H ⊗In) ˜S,
(28)
˙υ = −γυ(µ)(H ⊗In) ˜υ + 3sυ
(29)
where
3s
is
given
in
(16).
Due
to
Lemma
3,
(17)
holds.
Note
that
(17)
and
(28)
imply
that
∥˙S∥
≤
∥H ⊗In∥˜αs(∥˜S(t0)∥)γs(µ)κ−ζ
2 (γs(µ)), then applying Propo-
sition 2 leads to (27) with ˜αs(∥˜S(t0)∥) = γs(µ(t0))∥H ⊗
In∥˜αs(∥˜S(t0)∥). Note that
z = ˙υ −3sυ + 3sυ −1N ⊗S0υ0
= ˙υ −3sυ + 3˜s(1N ⊗υ0) + 3s ˜υ
(30)
where 3s and 3˜s are given in (16). Note that (18) and (29)
imply
∥˙υ −3sυ∥≤αυ(∥˜υ(t0)∥)∥(H ⊗In)∥γυ(µ)κ−ζ
2 (γυ(µ)).
(31)
Since function γυ satisfies (7) with c1 = 1, c2 = ζ/2,
by Proposition 2, we obtain that γυ(µ(t))κ−ζ
2 (γυ(µ)) ≤
γυ(µ(t0))κ−(1−ε)ζ
2
(γυ(µ)). Due to (17), (18), (19), (30), (31),
and the fact γυ(s) −γs(s) < 0, one obtains (26) with some
αz ∈K∞.
Remark 7: There are many (in fact, an infinite number) of
γs and γυ functions satisfying conditions in both Lemma 3
and 4. For example, given µ(t) = 1/(T + t0 −t), one can
find ι1 = 2, ι2 = 3/2, w1 = 1, w2 = 2 in Definition 1.
γs and γυ can be chosen as γs(µ) = m1µ, γυ(µ) = m2µ
with m1, m2 being finite constants satisfying 2/ζ ≤c1/c2 <
m2 < m1. Since c2/c1 ≤ζ/2, we can check
dγs(s)
ds
=
m1 = ω−1
1
c2
c1 s−ι1(γs(s))2
c1
m1c2 ≤εω−1
1
c2
c1 s−ι1(γs(s))2 with ε =
c1/(c2m1). Similarly, we can choose γv(s) to satisfy Proposi-
tion 2, and Lemmas 3, 4. Note that when a different µ ∈KT
is used, it yields different ιk, ωk with k = 1, 2 and results in a
different group of γs and γυ, as shown in Proposition 2 and 3.
Combining Lemma 3 and 4 shows that the prescribed-time
convergence is achieved for ˜ei in (25), and it now suffices to
prove that the prescribed-time convergence is achieved for ˆei
defined in (23). To this end, we introduce time-varying state
transformation
ϖi1 = 0ϖ(µ)ˆei1,
(32)
ϖi2 = ˙ϖ 1i = ˙0ϖ(µ)ˆei1 + 0ϖ(µ)ˆei2
(33)
where 0ϖ(µ(t)) = γϖ(µ(t)) ˜K with γϖ being a twice-
differentiable K∞
function to be designed, and
˜K
=
diag
˜k1, · · · , ˜kn
	
∈Rn×n with ˜ki > 0 for i = 1, · · · , n.
˙0ϖ(µ(t)) ∈Rn×n is the time derivative of 0ϖ(µ(t)).
For i ∈¯V, the local prescribed-time tracking controllers are
designed as
ξi = ϖi2 + Kiϖi1,
(34)
τi = Ci(qi,ri)ri + Gi(qi)
+ Mi(qi)
−(ρi + 2In)ξi −ηi + S2
i υi

(35)
where Ki
∈
Rn×n, ρi
=
diag{ρi1, · · · , ρin}
∈
Rn×n
with ρi j > 0 for j = 1, · · · , n, and ηi =
¨0ϖ (µ)
02ϖ (µ)ϖi1 −
2
˙02
ϖ (µ)
03ϖ (µ)ϖi1 + 2
˙0ϖ (µ)
02ϖ (µ)ϖi2 +
Ki
0ϖ (µ)ϖi2, where ¨0ϖ(µ) ∈Rn×n
is the second-order derivative of 0ϖ(µ) with respect to t.
We note that (0ϖ(µ(t)))l is positive definite for l ∈N+ and
∀t ∈Tp, thus ηi can be computed for t ∈Tp. Then, we have
the following theorem.
Theorem 1: Consider
the
closed-loop
networked
Euler-Lagrange systems composed of (1)-(2), distributed
prescribed-time observers (12)-(13), and local prescribed-time
tracking
controllers
(35)
under
Property
1
and
Assumption
1,
2.
Suppose
the
distributed
prescribed-
time observers (12)-(13) are designed according to Lemma 3
and 4. Let Ki in (34) be arbitrarily given. Suppose the K∞
function γυ satisfies the conditions of Proposition 2 and 3
with c2/c1 ≤c ≤ζ/2, and the K∞function γϖ satisfies
d2γϖ (µ)
dµ2
≥0 and
dγϖ(s)
ds
/(s−ι1γ ιϖ
ϖ (s)) < ∞,
(36)
d2γϖ(s)
ds2
sι1 + dγϖ(s)
ds
sι1ι2

/(γ 2
ϖ(s)) < ∞
(37)
for ∀s ∈[a0, ∞) and 1 < ιϖ < 3/2. Then, the prescribed-time
synchronization problem is solved and all internal signals in
the closed-loop systems are bounded.
Proof: The proof will be divided into three parts. We first
show that ξi in (34) is bounded for t ∈Tp which will be
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:38:30 UTC from IEEE Xplore.  Restrictions apply.

## Page 7

12166
IEEE TRANSACTIONS ON AUTOMATION SCIENCE AND ENGINEERING, VOL. 22, 2025
used to prove that ϖi1 and ϖi2 are bounded. Then, we prove
that prescribed-time convergence is achieved for ei. Last, the
boundedness of the control signal is shown.
1) Boundedness of ξi: Taking the time derivative of ξi and
upon using τi in (35) yields
˙ξ i = ¨0ϖ(µ)ˆei1 + 2 ˙0ϖ(µ)ˆei2 + 0ϖ(µ)˙ˆei2 + Kiϖi2
= 0ϖ(µ)

M−1
i
(qi)
τi −di −Ci(qi,ri)ri
−Gi(qi)

−¨υi + ηi

= 0ϖ(µ)
−(ρi + 2In)ξi −ςi −M−1
i
(qi)di

(38)
where
ςi = ¨υi −S2
i υi.
(39)
Define the Lyapunov function candidate for ξi-dynamics
in (38) as Wi(ξi) =
1
2ξ ⊤
i ξi. Using (38) and (39), the time
derivative of Wi(ξi) is
˙W i(ξi) = ξ
⊤
i 0ϖ(µ)
−(ρi + 2In)ξi −ςi −M−1
i
(qi)di

.
(40)
By Property 1, Assumption 1 and Young’s inequality, one
has −ξ ⊤
i 0ϖ(µ)M−1
i
(qi)di ≤γϖ(µ)∥ξi∥∥˜K∥∥M−1
i
(qi)∥di∥≤
γϖ(µ)k−1
n
¯di ˜kmax∥ξi∥≤ξ ⊤
i 0ϖ(µ)ξi +γϖ(µ) ¯d2
i ˜k2
max/(4k2
n ˜kmin),
where ˜kmin = min{˜k1, · · · , ˜kn}, ˜kmax = max{˜k1, · · · , ˜kn} and
we used ∥˜K∥= ˜kmax.
Since 3sυ −1N ⊗S0υ0 = 3sυ −3s(1N ⊗υ0) + 3s(1N ⊗
υ0) −1N ⊗S0υ0 = 3s ˜υ + 3˜s(1N ⊗υ0). Then by (29), ¨υ can
be expressed as
¨υ = −˙γ υ(µ) ¯H ˜υ −γυ(µ) ¯H ˙˜υ + 3˙sυ + 3s ˙υ
= 8(µ) ˜υ −γυ(µ(t)) ¯H3˜s ¯υ0 + 3˙sυ + 32
sυ
(41)
where 8(µ)
=
−˙γ υ(µ) ¯H + γ 2
υ (µ) ¯H 2 −γυ(µ) ¯H3s −
γυ(µ)3s ¯H,
3˙s
=
diag{ ˙S1, · · · , ˙Sn},
¯H
=
H ⊗
In
and
¯υ0
=
1N ⊗υ0.
Upon
using
(17),
(18),
(19) and (20), the terms in (41) satisfy ∥8(µ) ˜υ∥
≤
ϵυ ¯γ υ(µ)κ−ζ
2 (γυ(µ)), γυ(µ(t)) ¯H3˜s ¯υ0 ≤ϵsγs(µ)κ−ζ
2 (γs(µ))
and 3˙sυ
≤
ϵ′
sγs(µ)κ−ζ
2 (γs(µ)), where
¯γ υ(t) is defined
in (8), ϵυ
= max{∥¯H∥, ∥¯H∥2, 2¯s∥¯H∥}αυ(∥˜υ(t0)∥), ϵs
=
∥¯H∥supt∈Tp ∥¯υ0(t)∥αs(∥˜S(t0)∥) and ϵ′
s = ¯υ∥¯H∥˜αs(∥˜S(t0)∥).
Let
ς
=
[ς ⊤
1 , · · · , ς ⊤
N]⊤
with
ςi
denoted
in
(39).
Using (41) and the above inequalities leads to ∥ς∥
≤
ϵυ ¯γ υ(t)κ−ζ
2 (γυ(µ))+(ϵs +ϵ′
s)γs(µ(t))κ−ζ
2 (γs(µ)). By Propo-
sition
3
with
c2/c1
≤
c
≤
ζ/2,
¯γ υ(t)κ−ζ
2 (γυ(µ))
and
γs(µ)κ−ζ
2 (γs(µ))
are
DT
functions.
Therefore,
ς
satisfies
∥ς∥≤βς(∥ϑz(t0)∥, t)
(42)
for some KLT functions βς, where ϑz is defined in 4.
Then by (42), ∥ς∥≤φ = βς(∥ϑz(t0)∥, where φ is some
positive constant. As a result, the bound of −ξ ⊤
i γϖ(µ(t))ςi is
calculated as
−ξ
⊤
i 0ϖ(µ)ςi ≤ξ
⊤
i 0ϖ(µ)ξi + γϖ(µ)∥φ∥2 ˜k2
max/(4˜kmin) (43)
where
we
used
the
fact
∥ςi∥
≤
∥ς∥.
By
(40)
and (43),
˙W i(ξi) satisfies
˙W i(ξi)
≤
−ξ ⊤
i 0ϖ(µ)ρiξi +
γϖ(µ)1i
≤
−ϱiγϖ(µ)Wi(ξi) + γϖ(µ)1i, where ϱi
=
2 min

ρi1 ˜k1, · · · , ρin ˜kn
	
and 1i
=
¯d2
i ˜k2
max/(4k2
n ˜kmin) +
∥φ∥2 ˜k2
max/(4˜kmin). Applying Lemma 2 gives
∥ξi(t)∥≤¯ξ i = αξi(∥ξi(t0)∥)
(44)
for some Ke
∞function αξi.
2) Prescribed-Time Convergence of ei: We first prove the
boundedness of ϖi1 and ϖi2. Define the Lyapunov candidate
function Ji(ϖi1) = ϖ ⊤
i1ϖi1. Taking the time derivative of
Ji(ϖi1) along (33) yields
˙J i(ϖi1) = 2ϖ
⊤
i1(−Kiϖi1 + ξi) ≤ci Ji(ϖi1) + ¯ξ 2
i
(45)
where ci = 2∥Ki∥+ 1 > 0, ¯ξ i is defined in (44) and we
used ˙ϖ i1 = ϖi2. For t ∈Tp, applying the comparison lemma
to (45) yields
Ji(ϖi1(t))
≤exp
ci(t −t0)

Ji(ϖi1(t0)) +
R t
t0 exp
ci(t −s)
¯ξ 2
i ds
≤exp
ci(t −t0)

(Ji(ϖi1(t0)) + ¯ξ 2
i c−1
i ) −¯ξ 2
i c−1
i
≤exp
ciT

(Ji(ϖi1(t0)) + ¯ξ 2
i c−1
i ).
(46)
Therefore, Ji(ϖi1(t)), and thus ϖi1(t), are bounded for t ∈Tp.
By (46), the upper bound ¯ϖ i1 of ϖi1(t) can be expressed as
∥ϖi1(t)∥≤¯ϖ i1 = exp
ωiT/2

(∥ϖi1(t0)∥+ ¯ξ ic
−1
2
i
).
Define ϖi = [ϖ ⊤
i1, ϖ ⊤
i2]⊤. By (32) and (33), we have ˆei =
ψ(µ)ϖi, where
ψ(µ) =

(1/γϖ(µ))
0
−( ˙γ ϖ(µ)/γ 2
ϖ(µ)) (1/γϖ(µ))

⊗˜K −1.
From (36), one has sups∈[a0,∞)
h
dγϖ (s)
ds
/(s−ι1γ ιϖ
ϖ (s))
i
= g1 <
∞. Since 1 < ιϖ < 3/2, there exists a 0 < p1 < 1/2 such
that ιϖ + p1 = 3/2. By (3) and (36), ˙γ ϖ(µ) satisfies
˙γ ϖ(µ) = dγϖ(µ)
dµ
˙µ
≤g1µ−ι1γ
3
2 −p1
ϖ
(µ) ˙µ ≤g1w1γ
3
2 −p1
ϖ
(µ)
(47)
where we used the facts that
dγϖ (µ)
dµ
≥
0 for µ
∈
[a0, ∞) due to γϖ
∈
K∞, and
˙µ(t)
>
0 for t
∈
Tp
since
µ(t)
is
strictly
increasing.
Define
9(µ)
=
∥ψ(µ)∥. Then by (47) and the fact ∥A ⊗B∥= ∥A∥∥B∥,
one
has
9(µ)
≤
˜k
−1
min
1/γϖ(µ) + ˙γ ϖ(µ)/γ 2
ϖ(µ)

≤
˜k
−1
min
(γϖ(µ))−1 + g1ω1(γϖ(µ))−1
2 −p1
= g′
1(γϖ(µ))−p1−1
2 ,
where
˜kmin
=
min{˜k1, · · · , ˜kn}
and
g′
=
(g1ω1 +
(γϖ(µ(t0))
1
2 −p1)˜k−1
min. Let ˆe = [ˆe⊤
1, · · · , ˆe⊤
N]⊤. Therefore, ˆe
satisfies
∥ˆe(t)∥≤∥ψ(µ)∥∥ϖ∥
≤9(µ(t)) ¯ϖ ≤ˆβe( ¯ϖ, t) = αϖ( ¯ϖ)γ
−p1−1
2
ϖ
(µ)
(48)
with some KLT function ˆβe, where
¯ϖ =
¯ϖ 1 + ¯ϖ 2 and
αϖ( ¯ϖ) = g′
1 ¯ϖ. Inequality (48) means that ˆei(t) is bounded
for t ∈Tp and converges to zero as t →t0 + T . Due to (24)
and Lemmas 3 and 4, using (48) and the fact γυ(s)−γs(s) < 0,
the bound of e is obtained as
∥e(t)∥≤βυ(∥˜υ(t0)∥, t) + ˜βz(∥ϑz(t0)∥, t)) + βe( ¯ϖ, t)
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:38:30 UTC from IEEE Xplore.  Restrictions apply.

## Page 8

ZUO et al.: PRESCRIBED-TIME ROBUST SYNCHRONIZATION OF EULER-LAGRANGE SYSTEMS
12167
≤αe(ϑe(t0)) max
n
γ
−p1−1
2
ϖ
(µ), κ−(1−ε)ζ/2(γυ(µ))
o
= βe(∥ϑe(t0)∥, t)
(49)
with some KLT function βe where ϑe = [vec( ˜S)⊤, ˜υ⊤, ¯ϖ ⊤]⊤.
The prescribed-time convergence is achieved for ei. In other
words, ei(t) is bounded for t
∈
Tp and converges to
zero as t
→
t0 + T . As a result, the prescribed-time
synchronization
between
leader
and
followers
is
achieved.
3) Boundedness of the Control Signal τi: By (37), we have
¨γ ϖ(µ)
=
d2γϖ (µ)
dµ2
˙µ(t) +
dγϖ (µ)
dµ
¨µ(t)
≤
d2γϖ (µ)
dµ2
w1µι1 +
dγϖ (µ)
dµ
w2wι1
1 µι1ι2
≤
¯w

d2γϖ (µ)
dµ2
µι1 + dγϖ (µ)
dµ
µι1ι2

≤
¯wg2γ 2
ϖ(µ)
for
some
finite
number
g2
>
0,
where
¯w
=
max

w1, w2wι1
1
	
. By (47), ηi
satisfies ∥ηi∥
≤
¯wg2 ¯ϖ i1 + 2(g1w1)2(γϖ(µ))−1 ¯ϖ i1 + 2g1w1(γϖ(µ))−1 ¯ϖ i2 +
∥Ki∥(γϖ(µ))−1 ¯ϖ i2 ≤( ¯wg2γϖ(a) + 2(g1w1)2 + 2g1w1 +
∥Ki∥) ¯ϖ i(γϖ(a0))−1, where we used the fact γϖ(µ) ≥γϖ(a0).
Note that ˙qi in (1) satisfies ∥˙qi∥≤∥ei∥+ ∥S0υ0∥≤
βe(∥re(t0)∥, t0) + ∥S0∥¯υ0. By (19) and (18), S2
i υi is also
bounded. Thus, we can conclude that τi, i = 1, · · · , N is
bounded.
Remark 8: Let µ(t) = (
1
T +t0−t )m1 and γϖ(µ) = µm2. As a
result, w1 = m1, ι1 = m1+1
m1 , w2 = m1+1, ι2 = m1+2
m1+1, dγϖ (µ)
dµ
=
m2µm2−1 and d2γϖ (µ)
dµ2
= m2(m2−1)µm2−2. Let us choose m1 >
0, m2 > 2(m1+1)/m1+2 and m1m2 > 2. Then, (36) and (37)
are satisfied.
Remark 9: For the closed-loop networked Euler-Lagrange
systems, there are three incorporations of class KT
and
comparison functions: γs(µ), γυ(µ), and γϖ(µ). The func-
tion γs(µ) primarily provides a prescribed-time convergence
gain
for
the
Si-dynamics.
Meanwhile,
γυ(µ)
offers
a
prescribed-time convergence gain for the υi-dynamics. The
function γϖ(µ) is directly fed back into the local controller,
furnishing a prescribed-time convergence gain for the local
tracking error ˆei. Due to the decomposition of the synchroniza-
tion error as described in (23), (24), and (25), as shown in (49),
the prescribed-time convergence of the synchronization error
ei is influenced by the three gains: γs(µ), γυ(µ), and γϖ(µ).
Specifically, the faster µ increases with respect to time within
Tp, or the faster γs(µ), γυ(µ), and γϖ(µ) increase with
respect to µ, the quicker the synchronization error converges
in prescribed time.
Remark 10: Adaptive fuzzy prescribed-time control [29]
and adaptive neural prescribed-time control [42] employ
approximations with fuzzy logic or ANNs within com-
pact sets, resulting in time-varying gains capped by upper
bounds, thus preventing unbounded growth. Consequently,
these controls achieve only practical prescribed-time con-
vergence. Furthermore, in contrast to robust finite-time
control [43] and robust fixed-time control [14], [15], our robust
prescribed-time synchronization purely utilizes time-varying
gains to counteract the impact of external disturbances on
convergence. It does not involve any compensation measures
within the controller, nor does it employ any disturbance
information.
V. SIMULATION AND EXPERIMENTAL RESULTS
A. Numerical Simulation
Consider a group of six robotic manipulators given by (1)
where qi = [qi1, qi2]⊤∈R2 and
Mi(qi) =
 θi1 + θi2 + 2θi3 cos(qi2) θi2 + θi3 cos(qi2)
θi2 + θi3 cos(qi2)
θi4

,
Ci(qi,ri) =
 −θi3 sin(qi2)ri1 −2θi3 sin(qi2)ri1
0
θi3 sin(qi2)ri2

,
Gi(qi) =
 θi5g cos(qi1) + θi6g cos(qi1 + qi2)
θi6g cos(qi1 + qi2)

where θi1 = 6kg · m2, θi2 = 0.8kg · m2, θi3 = 0.1kg · m2,
θi4 = 5.5kg · m2, θi5 = 0.1kg · m, θi6 = 0.1kg · m for
i = 1, · · · , 6, and g = 9.8m · s2. The external disturbance
is denoted as di = 12 ⊗δ(t), i = 1, · · · , 6, where δ(t) is
impulse noise with sparsity 0.01 and pulse peak 5.
The leader system is given by (2) with S0 = [0, −1; −1, 0]
and υ0(t0) = [0.5, 0.5]⊤. The information flow among all the
subsystems and the leader is described by the digraph as 0 →
1 →2 →3 →4 →5 →6, which contains a spanning tree
with node 0 as the root, and thus Assumption 2 is satisfied.
We select Q = I12 and then ζ = λQ ¯λ−1
P = 0.3406.
The prescribed-time function µ(t) is chosen as µ(t) =
(1/(T + t0 −t))2 with t0 = 0 and prescribed scalar T = 1s.
Thus, µ(t) satisfies Definition 1 with ι1 =
3
2, ι2 =
4
3,
w1 = 2 and w2 = 3. The observer gains in (12), (13)
are γs(µ) = 16µ, γυ(µ) = 14µ. We check γs(µ) >
γυ(µ), ω1
dγs(µ)
dµ µι1(γs(µ))−2
≤
(T + t0 −t)/8
≤
1/8,
ω1
dγυ(µ)
dµ µι1(γυ(µ))−2 ≤(T + t0 −t)/7 ≤1/7, d2γυ(µ)
dµ2 γυ(µ) +
dγυ(µ)
dµ w2wι2−1
1
µι1(ι2−1)
≤
0.27 dγυ(µ)
dµ γυ(µ), thus conditions
of Lemma 3 and 4 are satisfied. The time-varying state
transformation function γϖ(µ) in (32) is
˜K
=
I2 and
γϖ(µ)
=
µ2, and then
dγϖ (µ)
dµ
=
2µ,
d2γϖ (µ)
dµ2
=
2.
We check d2γϖ (µ)
dµ2
µι1(γϖ(µ))−3
2 = 2(γϖ(µ))−1
4 , d2γϖ (µ)
dµ2
µι1 +
dγϖ (µ)
dµ
µι1ι2 = 2µ
3
2 + 2µ3 ≤2γ 2
ϖ(µ), thus (36) and (37) are
satisfied.
The initial values are Si = [1, 1; 1, 1], υi = [0, 0]⊤, qi =
[0.5, 0.5]⊤, ri = [2, 2]⊤, i = 1, · · · , 6, and control parameters
are selected as ρi = 3I2, Ki = I2, i = 1, · · · , 6. The sampling
time for ordinary differential equation solvers tool is 5×10−5s.
The simulation results are presented in Fig. 1-4, demonstrating
that the distributed estimate errors, synchronization position
errors, and synchronization velocity errors remain bounded for
t ∈Tp and converge to zero as t →T + t0. Additionally, the
uniform boundedness of the control input τi is illustrated in
Fig. 4. Furthermore, we verify that the finite settling time is
independent of initial values and control parameters, as shown
in Fig. 5. Let ep = [e⊤
11, · · · , e⊤
N1]⊤and ev = [e⊤
12, · · · , e⊤
N2]⊤
be the position error and velocity error, where ei1 and ei2
are denoted in (22). The trajectories of ep and ev subject to
different prescribed times are shown in Fig. 6, demonstrating
the PTS algorithm’s robustness and its ability to be specified
a priori.
To
further
demonstrate
the
advantages
of
our
proposed PTS algorithm, a comparison with fixed-time
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:38:30 UTC from IEEE Xplore.  Restrictions apply.

## Page 9

12168
IEEE TRANSACTIONS ON AUTOMATION SCIENCE AND ENGINEERING, VOL. 22, 2025
Fig. 1.
The norm of distributed estimate errors ˜si and ˜υi for i = 1, · · · , 6.
Fig. 2.
Synchronization velocity errors ri −˙υ0, i = 1, · · · , 6.
Fig. 3.
Synchronization velocity errors ri −˙υ0, i = 1, · · · , 6.
synchronization from [13] and [14] is carried out. The
distributed
fixed-time
observers
and
local
fixed-time
tracking
controllers
are
designed
as
follows,
for
i
= 1, · · · , 6,
˙Si
= −c1χi −c2sigβ1(χi) −c3sigα1(χi),
˙υi
=
Siυi−
c1 ˜χi
−
c2sigβ1( ˜χi)
−
c3sigα1( ˜χi),
˜si = ˆei2 + γ1
sigα1(ˆei1) + sigβ1(ˆei1)

and τi = Ci(qi,ri)ri +
Gi(qi)
−
γ2Mi(qi)
sigα2(˜si)
+
sigβ2(˜si)

−
γ1Mi(qi)
(α1diag{|ˆei1|α1−1}ˆei2 + β1diag{|ˆei1|β1−1}ˆei2), where χi
=
P
j∈Ni(Si −Sj), ˜χi = P
j∈Ni(υi −υ j), ˆei1 and ˆei2 are denoted
in
(23),
sigβ1(χi)
=
[sign(χi1)|χi1|β1, sign(χi2)|χi2|β2]⊤
with similar variables represented in the same manner.
The design parameters are c1
=
8.4, c2
=
1, c3 =
1, α1
= α2
= 3, β1
= β2
= 3/5, γ1
= γ2
= 2.
Based on [13], [14], the upper bound of the settling-
time T
is T
≤
2
a1(α2−1) +
2
b1(1−β2)
=
2.94s, where
a1 = 2[(1+α2)/2](Nn)[(1−α2)/2]γ2 and b1 = 2[(1+β2)/2]γ2 with
N = 6 and n = 2 denoting the number of followers and the
dimension of the leader system, respectively.
Fig. 4.
The trajectories for the control input τi, i = 1, · · · , 6.
Fig. 5. Trajectories of q11−υ01 subject to different initial values and different
control parameters.
Fig. 6.
Trajectories of position error ep and velocity error ev subject to
different prescribed times T .
Fig. 7.
The trajectories of q11 under different control algorithms.
The sampling time for the ordinary differential equation
solver is 5 × 10−5s, and the total simulation time for our
PTS algorithm and the fixed-time synchronization algorithm
is 3s. The simulation results are given in Fig. 7-9. As shown
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:38:30 UTC from IEEE Xplore.  Restrictions apply.

## Page 10

ZUO et al.: PRESCRIBED-TIME ROBUST SYNCHRONIZATION OF EULER-LAGRANGE SYSTEMS
12169
Fig. 8.
Trajectories of torque input τ11 under different control algorithms
and initial values.
Fig. 9.
Energy cost under different control algorithms and initial values.
Fig. 10.
The robot image and model diagram of the 6-DOF manipulator.
in Fig. 7, the convergence accuracy of our proposed PTS
algorithm is better in the presence of external disturbances.
The first control torque τ11 of follower 1 under different
control schemes is displayed in Fig. 8, which demonstrates that
the amplitude of the control torque under the PTS algorithm is
lower. The energy cost EC =
R t
t0 ∥τ11(s)∥1ds by control torque
τ11 is shown in Fig. 9, indicating that under the same energy
measurement standard, the PTS algorithm requires less energy.
The trajectories of the other followers are similar and thus not
repeated here.
B. Real-Robot Experiment
To verify the effectiveness of the proposed algorithm from
the perspective of practical implementation, experimental stud-
ies are performed in this subsection using the 6-DOF industrial
manipulator shown in Fig.10.
In this experiment, we set two manipulators as the followers
and the communication graph is 0 →1 →2. The leader
Fig. 11.
The experimental and desired joint trajectories of the manipulators.
Fig. 12.
The experimental and desired joint angular velocity of the
manipulators.
Fig. 13.
The experimental torque outputs of the manipulators.
system in (2) is designed as S0 = [0, −0.04, −0.33, −0.6,
0.45, 0.1; 0.04, 0, −0.4, −0.56, −0.6, −0.3; 0.33, 0.4, 0,
−0.18, −0.06, 0.5; 0.6, 0.56, 0.18, 0, 0.1, −0.47; −0.45, 0.6,
0.06, −0.1, 0, 0.39; −0.1, 0.3, −0.5, 0.47, −0.39, 0] and
υ0(t0) = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2]⊤. By adjusting the values
of S0 and υ0(t0), the leader system can generate desired trajec-
tories for the manipulators to execute a place task as in [44].
The prescribed-time function µ(t) is chosen as µ(t) = (T +
t0)/(T +t0−t)+5 with t0 = 0 and prescribed-time scalar T =
8s. Thus, µ is a KT function in Definition 1 with ι1 = 2, ι2 =
3/2, ω1 = 1/(T + t0) and ω2 = 2(T + t0)−1/2. The observer
gains in (12) and (13) are γs(µ) = 5µ and γυ(µ) = 4µ.
We check γs(µ) > γυ(µ), ω1
dγs(µ)
dµ µι1(γs(µ))−2 = 1/(5(T +
t0)), ω1
dγυ(µ)
dµ µι1(γυ(µ))−2 = 1/(4(T + t0)),
d2γυ(µ)
dµ2 γυ(µ) +
dγυ(µ)
dµ w2wι2−1
1
µι1(ι2−1) ≤2−1(T + t0)−3/2 dγυ(µ)
dµ γυ(µ), and thus
conditions of Lemma 3 and 4 are satisfied.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:38:30 UTC from IEEE Xplore.  Restrictions apply.

## Page 11

12170
IEEE TRANSACTIONS ON AUTOMATION SCIENCE AND ENGINEERING, VOL. 22, 2025
Fig. 14.
The experimental and desired trajectories of the 6-th joint’s position
subject to different prescribed times T .
Fig. 15.
The experimental and desired trajectories of the 6-th joint’s velocity
subject to different prescribed times T .
Fig. 16.
The experimental and desired trajectories of the 6-th joint’s torque
subject to different prescribed times T .
The time-varying state transformation function γϖ(µ)
in (32) is given by
˜K
=
diag{8, 8, 10, 10, 5, 5} and
γϖ(µ)
=
µ2.
Then
dγϖ (µ)
dµ
=
2µ,
d2γϖ (µ)
dµ2
=
2.
We check d2γϖ (µ)
dµ2
µι1(γϖ(µ))−3
2 = 2(γϖ(µ))−1
2 , d2γϖ (µ)
dµ2
µι1 +
dγϖ (µ)
dµ
µι1ι2 = 2µ2 + 2µ4 ≤4γ 2
ϖ(µ), and thus (36) and (37)
are satisfied.
The initial values are Si = 16×6, υi = 06×1 for i = 1, 2,
and control parameters are selected as ρi = 4I6, ˜K = 5I6.
The sampling and communication frequency is 1000Hz.
As in [45], we also employ gain clipping as µ(t) =
min{T/(T + t0 −t) + 5, ξ} with ξ = 20 for the real-robot
experiment. This mitigates the instability issue caused by the
measurement noise but introduces a small synchronization
error. The experimental results are shown in Fig. 11-13 demon-
strating that the position and velocity of the two manipulators
achieve synchronization within T + t0 while the control input
remains bound.
Furthermore, we validate the robustness of the proposed
PTS algorithm, as shown in Fig. 14-16, by setting different
prescribed times T . These figures show that the finite settling
time can be specified a priori. Additionally, the PTS algorithm
demonstrates robustness to external disturbances by relying
solely on time-varying gains, without requiring any compen-
satory techniques.
VI. CONCLUSION
In this paper, the PTS problem of networked Euler-Lagrange
systems with external disturbances is addressed. We propose
a novel prescribed-time PTS algorithm comprising distributed
prescribed-time observers and local prescribed-time tracking
controllers. A distinct feature of our algorithm is that the
settling time of synchronization errors is independent of initial
values and design parameters. Additionally, we analyze the
properties of time-varying gains coupled with comparison
functions to derive prescribed-time convergence. Our results
require the leader to transmit its full state in the network.
It would be interesting to consider the case where the leader
can only transmit its partial state or output in the network, and
thus a more general observer is needed.
APPENDICES
Proof
of
Proposition
2:
Taking
the
time
derivative
of (γ (µ))c1κ−c2(γ (µ)) yields d

(γ (µ))c1κ−c2(γ (µ))

/dt =

c1(γ (µ))c1−1 dγ (µ)
dµ
˙µ −c2(γ (µ))c1+1
κ−c2(γ (µ))
≤
(ε −
1)c2(γ (µ))c1+1κ−c2(γ (µ)) < 0, where we used (3) and (7).
Therefore, (γ (µ))c1κ−c2(γ (µ)) is a decreasing function of
t for t ∈Tp. Note that (γ (µ))c1κ−c2(γ (µ)) can be further
expressed as
(γ (µ))c1κ−c2(γ (µ))
= (γ (a0))c1 exp
 
R t
t0
c1
dγ (s)
ds

s=µ(ζ) ˙µ(ζ)−c2γ 2(µ(ζ))
γ (µ(ζ))
dζ
!
≤(γ (a0))c1 exp
 
R t
t0
c1w1µι1(ζ) dγ (s)
ds

s=µ(ζ)−c2γ 2(µ(ζ))
γ (µ(ζ))
dζ
!
≤(γ (a0))c1κ−(1−ε)c2(γ (µ))
which means that (γ (µ))c1κ−c2(γ (µ)) tends to zero as t →
t0 + T . Therefore, (γ (µ))c1κ−c2(γ (µ)) is a DT function.
■
Proof of Proposition 3: Taking the time derivative of
˙γ (µ)κ−c(γ (µ)) yields
d[ ˙γ (µ)κ−c(γ (µ))]/dt
≤˙µκ−c(γ (µ))
d2γ (µ)
dµ2
+ dγ (µ)
dµ
w2 ˙µι2−1 −cdγ (µ)
dµ
γ (µ)

≤˙µκ−c(γ (µ))
d2γ (µ)
dµ2
+ dγ (µ)
dµ
w2wι2−1
1
µι1(ι2−1)
−cdγ (µ)
dµ
γ (µ)

≤˙µκ−c(γ (µ))(ε −1)cdγ (µ)
dµ
γ (µ) < 0
(50)
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:38:30 UTC from IEEE Xplore.  Restrictions apply.

## Page 12

ZUO et al.: PRESCRIBED-TIME ROBUST SYNCHRONIZATION OF EULER-LAGRANGE SYSTEMS
12171
where we used (9). Therefore, ˙γ (µ)κ−c(γ (µ)) is a decreasing
function of t for t ∈Tp. Note that ˙γ (µ)κ−c(γ (µ)) can be
further expressed as
˙γ (µ)κ−c(γ (µ))
≤a′ exp
 
R t
t0
d2γ (s)
ds2

s=µ(ζ) ˙µ(ζ)+ dγ (s)
ds

s=µ(ζ) ¨µ(ζ)
dγ (s)
ds

s=µ(ζ) ˙µ(ζ)
dζ
!
× exp
 
R t
t0
−cγ (µ(ζ)) dγ (s)
ds

s=µ(ζ) ˙µ(ζ))
dγ (s)
ds

s=µ(ζ) ˙µ(ζ)
dζ
!
≤a′exp
R t
t0 ˙µ(ζ)

d2γ (s)
ds2

s=µ(ζ)+ dγ (s)
ds

s=µ(ζ)w2( ˙µ(ζ))ι2−1
−cγ (µ(ζ))dγ (s)
ds

s=µ(ζ)

/
dγ (s)
ds

s=µ(ζ) ˙µ(ζ)

dζ

≤a′κ−(1−ε)c(γ (µ)).
where a′ = dγ (s)
ds
|s=µ(t0) ˙µ(t0).
By
Propositions
1
and
2,
and
c2/c1
≤
c/2,
we have
dγ (s)
ds
≤
εw−1
1
c
2µ−ι1γ 2(s) for s
∈
[a0, ∞),
then
γ 2(µ)κ−c(γ (µ))
are
DT
function
and
satisfies
γ 2(µ)κ−c(γ (µ))
≤
(γ (a0))2κ−(1−ε)c(γ (µ)).
We
also
note that
dγ (s)
ds
≤
εw−1
1 cµ−ι1γ 2(s) for s
∈
[a0, ∞).
Then
γ (µ)κ−c(γ (µ))
satisfies
γ (µ)κ−c(γ (µ))
≤
γ (a0)κ−(1−ε)c(γ (µ)).
■
Proof of Lemma 1: For t
∈
Tp, applying compari-
son lemma (Lemma 3.4 in [39]) to (10) yields V (t) ≤
κ−c1(γ1(µ)) exp
c2(t −t0)

V (t0) + c3
R t
t0

exp
c2(t −ζ) −
c1
R t
ζγ1(µ(s))ds

κ−c1(γ2(µ(ζ)))

dζ. The second term on the
right-hand side of V (t) satisfies
c3
R t
t0[exp
c2(t −ζ) −c1
R t
ζγ1(µ(s))ds

κ−c1(γ2(µ))]dζ
≤c4
R t
t0 exp
−c1
R t
ζγ1(µ(s))ds −c1
R ζ
t0 γ2(µ(s))ds

dζ
≤c4T κ−c1(γ1(µ))
(51)
with c4 = |c3| exp
|c2|T

where γ1(µ) −γ2(µ) < 0 is
used.
Using
the
inequality
(51)
yields
V (t)
≤
κ−c1(γ1(µ)) exp
c2(t −t0)

V (t0)
+
c4T κ−c1(γ1(µ))
≤
(c5V (t0) + c4T )κ−c1(γ1(µ)) where c5 = exp
c2T

. As a
result, ∥x(t)∥≤(λ−1
P (¯λPc5∥x(t0)∥2 + c4T ))
1
2 κ−c1
2 (γ1(µ)).
The proof is thus completed.
■
Proof of Lemma 2: Applying the comparison lemma to (11)
obtains
V (t) ≤exp
−c1
R t
t0γ (µ(ζ))dζ

V (t0)
+ c2
R t
t0 exp
−c1
R t
ζ γ (µ(s))ds

γ (µ(ζ))dζ.
(52)
The second term on the right-hand side of (52) becomes
c2
R t
t0 exp
−c1
R t
ζ γ (µ(s))ds

γ (µ(ζ))dζ
= c2κ−c1(γ (µ))
R t
t0 exp
c1
R ζ
t0 γ (µ(s))ds

γ (µ(ζ))dζ
= c2κ−c1(γ (µ))
R t
t0 exp
c1
R ζ
t0 γ (µ(s))ds

d
R ζ
t0 γ (µ(s))ds
= c2κ−c1(γ (µ))c−1
1 exp
c1
R ζ
t0γ (µ(s))ds
t
t0
= c2c−1
1 κ−c1(γ (µ))(κc1(γ (µ)) −1).
(53)
Substituting (53) into (52) yields V (t) ≤κ−c1(γ (µ))V (t0) +
c2c−1
1 (1
−
κ−c1(γ (µ))).
As
a
result,
∥x(t)∥
≤
q
λ−1
p ¯λp∥x(0)∥2 + λ−1
p |c2|c−1
1 . Thus, (11) holds.
REFERENCES
[1] W. Chen, J. Liu, and H. Guo, “Achieving robust and efficient consensus
for large-scale drone swarm,” IEEE Trans. Veh. Technol., vol. 69, no. 12,
pp. 15867–15879, Dec. 2020.
[2] E. Nuño, A. Loría, T. Hernández, M. Maghenem, and E. Panteley,
“Distributed consensus-formation of force-controlled nonholonomic
robots with time-varying delays,” Automatica, vol. 120, Oct. 2020,
Art. no. 109114.
[3] E. Nuno, R. Ortega, L. Basanez, and D. Hill, “Synchronization of
networks of nonidentical Euler–Lagrange systems with uncertain param-
eters and communication delays,” IEEE Trans. Autom. Control, vol. 56,
no. 4, pp. 935–941, Apr. 2011.
[4] X. Zhao, X. Zheng, C. Ma, and R. Li, “Distributed consensus of multiple
Euler–Lagrange systems networked by sampled-data information with
transmission delays and data packet dropouts,” IEEE Trans. Autom. Sci.
Eng., vol. 14, no. 3, pp. 1440–1450, Jul. 2017.
[5] L. Zhu, Z. Chen, and R. H. Middleton, “A general framework for
robust output synchronization of heterogeneous nonlinear networked
systems,” IEEE Trans. Autom. Control, vol. 61, no. 8, pp. 2092–2107,
Aug. 2016.
[6] C. Chen, X. Gao, H. Zhang, W. Zou, and Z. Xiang, “Sampled-data
connectivity-preserving consensus for multiple heterogeneous Euler–
Lagrange systems,” IEEE Trans. Autom. Sci. Eng., early access, Sep. 4,
2024, doi: 10.1109/TASE.2024.3450518.
[7] M. Long and H. Su, “Distributed reduced-order observer-based consen-
sus of multiple Euler–Lagrange systems over switching networks,” IEEE
Trans. Autom. Sci. Eng., vol. 22, pp. 53–61, 2025.
[8] M. Long and H. Su, “Robust consensus of multiple Euler–Lagrange
systems via a distributed reduced-order observer,” IEEE Trans. Control
Netw. Syst., vol. 11, no. 3, pp. 1667–1678, Sep. 2024.
[9] S. P. Bhat and D. S. Bernstein, “Continuous finite-time stabilization of
the translational and rotational double integrators,” IEEE Trans. Autom.
Control, vol. 43, no. 5, pp. 678–682, May 1998.
[10] A. Polyakov, D. Efimov, and W. Perruquetti, “Finite-time and fixed-time
stabilization: Implicit Lyapunov function approach,” Automatica, vol. 51,
pp. 332–340, Jan. 2015.
[11] J. Huang, C. Wen, W. Wang, and Y.-D. Song, “Adaptive finite-time con-
sensus control of a group of uncertain nonlinear mechanical systems,”
Automatica, vol. 51, pp. 292–301, Jan. 2015.
[12] M. Ghasemi and S. G. Nersesov, “Finite-time coordination in multiagent
systems using sliding mode control approach,” Automatica, vol. 50,
no. 4, pp. 1209–1216, 2014.
[13] T. Xu, Z. Duan, Z. Sun, and G. Chen, “Distributed fixed-time coordi-
nation control for networked multiple Euler–Lagrange systems,” IEEE
Trans. Cybern., vol. 52, no. 6, pp. 4611–4622, Jun. 2022.
[14] Y. Dong and Z. Chen, “Fixed-time synchronization of networked
uncertain Euler–Lagrange systems,” Automatica, vol. 146, Dec. 2022,
Art. no. 110571.
[15] J. Wang, Y. Li, Y. Wu, Z. Liu, K. Chen, and C. L. P. Chen, “Fixed-
time formation control for uncertain nonlinear multiagent systems with
time-varying actuator failures,” IEEE Trans. Fuzzy Syst., vol. 32, no. 4,
pp. 1965–1977, Apr. 2024.
[16] H. Wang, W. Yu, Z. Ding, and X. Yu, “Tracking consensus of general
nonlinear multiagent systems with external disturbances under directed
networks,” IEEE Trans. Autom. Control, vol. 64, no. 11, pp. 4772–4779,
Nov. 2019.
[17] Z. Zuo, B. Tian, M. Defoort, and Z. Ding, “Fixed-time consensus
tracking for multiagent systems with high-order integrator dynamics,”
IEEE Trans. Autom. Control, vol. 63, no. 2, pp. 563–570, Feb. 2018.
[18] J. Wang, C. Wang, Z. Liu, C. L. P. Chen, and C. Zhang, “Practical fixed-
time adaptive ERBFNNs event-triggered control for uncertain nonlinear
systems with dead-zone constraint,” IEEE Trans. Syst. Man, Cybern.
Syst., vol. 54, no. 1, pp. 342–351, Jan. 2024.
[19] Y. Zhao, Z. Duan, G. Wen, and G. Chen, “Distributed finite-time tracking
of multiple non-identical second-order nonlinear systems with settling
time estimation,” Automatica, vol. 64, no. 1, pp. 86–93, 2016.
[20] X. Jin, “Adaptive fixed-time control for MIMO nonlinear systems with
asymmetric output constraints using universal barrier functions,” IEEE
Trans. Autom. Control, vol. 64, no. 7, pp. 3046–3053, Jul. 2019.
[21] Y. Song, Y. Wang, J. Holloway, and M. Krstic, “Time-varying feedback
for regulation of normal-form nonlinear systems in prescribed finite
time,” Automatica, vol. 83, pp. 243–251, Sep. 2017.
[22] A. Shakouri and N. Assadian, “Prescribed-time control for perturbed
Euler–Lagrange systems with obstacle avoidance,” IEEE Trans. Autom.
Control, vol. 67, no. 7, pp. 3754–3761, Jul. 2022.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:38:30 UTC from IEEE Xplore.  Restrictions apply.

## Page 13

12172
IEEE TRANSACTIONS ON AUTOMATION SCIENCE AND ENGINEERING, VOL. 22, 2025
[23] C. Chen, Y. Han, S. Zhu, and Z. Zeng, “Prescribed-time coopera-
tive output regulation of heterogeneous multi-agent systems,” IEEE
Trans. Ind. Informat., vol. 20, no. 2, pp. 2432–2443, 2024, doi:
10.1109/TII.2023.3290989.
[24] X. Chen, H. Yu, and F. Hao, “Prescribed-time event-triggered bipartite
consensus of multiagent systems,” IEEE Trans. Cybern., vol. 52, no. 4,
pp. 2589–2598, Apr. 2022.
[25] Y. Ma, K. Zhang, and B. Jiang, “Practical prescribed-time active fault-
tolerant control for mixed-order heterogeneous multiagent systems: A
fully actuated system approach,” Automatica, vol. 166, Aug. 2024,
Art. no. 111721.
[26] Y. Ren, W. Zhou, Z. Li, L. Liu, and Y. Sun, “Prescribed-time consensus
tracking of multiagent systems with nonlinear dynamics satisfying time-
varying Lipschitz growth rates,” IEEE Trans. Cybern., vol. 53, no. 4,
pp. 2097–2109, Apr. 2023.
[27] Y. Wang and Y. Song, “Leader-following control of high-order multi-
agent systems under directed graphs: Pre-specified finite time approach,”
Automatica, vol. 87, pp. 113–120, Jan. 2018.
[28] Y. Gao, W. Zhou, B. Niu, Y. Kao, H. Wang, and N. Sun, “Distributed
prescribed-time consensus tracking for heterogeneous nonlinear multi-
agent systems under deception attacks and actuator faults,” IEEE Trans.
Autom. Sci. Eng., vol. 21, no. 4, pp. 6920–6929, Oct. 2024.
[29] J. Wang, J. Liu, Y. Li, C. L. P. Chen, Z. Liu, and F. Li, “Prescribed time
fuzzy adaptive consensus control for multiagent systems with dead-zone
input and sensor faults,” IEEE Trans. Autom. Sci. Eng., vol. 21, no. 3,
pp. 4016–4027, Jul. 2024.
[30] B. Ning, Q.-L. Han, and Z. Zuo, “Bipartite consensus tracking
for second-order multiagent systems: A time-varying function-based
preset-time approach,” IEEE Trans. Autom. Control, vol. 66, no. 6,
pp. 2739–2745, Jun. 2021.
[31] B. Cui, Y. Wang, K. Liu, and Y. Xia, “Sliding mode based prescribed-
time consensus tracking control of second-order multi-agent systems,”
Automatica, vol. 158, Dec. 2023, Art. no. 111296.
[32] Y. Wang, Y. Song, D. J. Hill, and M. Krstic, “Prescribed-time consensus
and containment control of networked multiagent systems,” IEEE Trans.
Cybern., vol. 49, no. 4, pp. 1138–1147, Apr. 2019.
[33] T.-F. Ding, M.-F. Ge, C. Xiong, Z.-W. Liu, and G. Ling, “Prescribed-time
formation tracking of second-order multi-agent networks with directed
graphs,” Automatica, vol. 152, Jun. 2023, Art. no. 110997.
[34] J. Wang, Q. Gong, K. Huang, Z. Liu, C. L. P. Chen, and J. Liu, “Event-
triggered prescribed settling time consensus compensation control for a
class of uncertain nonlinear systems with actuator failures,” IEEE Trans.
Neural Netw. Learn. Syst., pp. 1–11, 2021.
[35] M. Lu, L. Liu, and G. Feng, “Adaptive tracking control of uncertain
Euler–Lagrange systems subject to external disturbances,” Automatica,
vol. 104, pp. 207–219, Jun. 2019.
[36] H. Cai and J. Huang, “The leader-following consensus for multi-
ple uncertain Euler–Lagrange systems with an adaptive distributed
observer,” IEEE Trans. Autom. Control, vol. 61, no. 10, pp. 3152–3157,
Oct. 2016.
[37] C. Hua, P. Ning, and K. Li, “Adaptive prescribed-time control for a class
of uncertain nonlinear systems,” IEEE Trans. Autom. Control, vol. 61,
no. 17, pp. 6159–6166, Nov. 2021.
[38] E. Jiménez-Rodríguez, A. J. Muñoz-Vázquez, J. D. Sánchez-Torres,
M. Defoort, and A. G. Loukianov, “A Lyapunov-like characterization of
predefined-time stability,” IEEE Trans. Autom. Control, vol. 65, no. 11,
pp. 4922–4927, Nov. 2020.
[39] H.
K.
Khalil,
Nonlinear
Systems,
3rd
ed.,
Upper
Saddle
River,
NJ,
USA:
Prentice-Hall,
2002.
[Online].
Available:
https://cds.cern.ch/record/1173048
[40] H. Ye and Y. Song, “Prescribed-time tracking control of MIMO non-
linear systems with nonvanishing uncertainties,” IEEE Trans. Autom.
Control, vol. 68, no. 6, pp. 3664–3671, Jun. 2023.
[41] B. Zhou and Y. Shi, “Prescribed-time Stabilization of a class of nonlinear
systems by linear time-varying feedback,” IEEE Trans. Autom. Control,
vol. 66, no. 12, pp. 6123–6130, Dec. 2021.
[42] D. Zeng, Z. Liu, C. L. P. Chen, Y. Wang, Y. Zhang, and Z. Wu, “Adaptive
neural prescribed-time control of switched nonlinear systems with mode-
dependent average dwell time,” IEEE Trans. Syst. Man, Cybern. Syst.,
vol. 53, no. 12, pp. 7427–7440, Dec. 2023.
[43] R. Yang and L. Sun, “Finite-time robust control of a class of nonlinear
time-delay systems via Lyapunov functional method,” J. Franklin Inst.,
vol. 356, no. 3, pp. 1155–1176, Feb. 2019.
[44] A. Bertino, M. Bagheri, M. Krsti´c, and P. Naseradinmousavi, “Experi-
mental autonomous deep learning-based 3D path planning for a 7-DOF
robot manipulator,” in Proc. Dyn. Syst. Control Conf., vol. 59155,
2019.
[45] A. Bertino, P. Naseradinmousavi, and M. Krstic, “Design and experiment
of a prescribed-time trajectory tracking controller for a 7-DOF robot
manipulator,” J. Dyn. Syst., Meas., Control, vol. 144, no. 10, Oct. 2022,
Art. no. 101005.
Gewei Zuo received the M.E. degree in control
theory and engineering from Chongqing Univer-
sity, Chongqing, China, in 2022. He is currently
pursuing the Ph.D. degree in control science and
engineering with the School of Artificial Intelligence
and Automation, Huazhong University of Science
and Technology, Wuhan, Hubei, China. His research
interests include nonlinear system control theory,
distributed cooperative control, and distributed con-
vex optimization.
Yaohang Xu received the B.E. degree in automa-
tion from the Huazhong University of Science and
Technology, Wuhan, Hubei, China, in 2023, where
he is currently pursuing the M.E. degree in control
science and engineering with the School of Artificial
Intelligence and Automation. His research interests
include manipulator control and imitation learning
of robots.
Mengmou Li (Member, IEEE) received the B.S.
degree in physics from Zhejiang University, China,
in 2016, and the Ph.D. degree in electrical and
electronic engineering from The University of Hong
Kong in 2020. He held post-doctoral positions at
The Hong Kong University of Science and Technol-
ogy; the Control Group, University of Cambridge;
and Tokyo Institute of Technology, Japan. He was
a Specially Appointed Assistant Professor with
Tokyo Institute of Technology. He is currently a
Tenure-Track Associate Professor with the Graduate
School of Advanced Science and Engineering, Hiroshima University, Japan.
His research interests include optimization, robust control, and power systems.
Lijun Zhu (Member, IEEE) received the Ph.D.
degree in electrical engineering from the University
of Newcastle, Callaghan, Australia, in 2013. He is
currently a Professor with the School of Artificial
Intelligence and Automation, Huazhong University
of Science and Technology, Wuhan, China. Prior to
this, he was a Post-Doctoral Fellow with The Univer-
sity of Hong Kong and the University of Newcastle.
His research interests include power systems, multi-
agent systems, and nonlinear systems analysis and
control.
Han Ding (Member, IEEE) received the Ph.D.
degree
in
mechanical
engineering
from
the
Huazhong University of Science and Technology
(HUST), Wuhan, China, in 1989.
Supported
by
the
Alexander
von
Humboldt
Foundation,
he
was
a
Researcher
with
the
University
of
Stuttgart,
Stuttgart,
Germany,
from 1993 to 1994. He has been a Professor with
HUST since 1997. He was a “Cheung Kong” Chair
Professor
with
Shanghai
Jiao
Tong
University
from 2001 to 2006. His research interests include
intelligent manufacturing and robotic machining.
Dr. Ding was elected as a member of the Chinese Academy of Sciences in
2013.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:38:30 UTC from IEEE Xplore.  Restrictions apply.
