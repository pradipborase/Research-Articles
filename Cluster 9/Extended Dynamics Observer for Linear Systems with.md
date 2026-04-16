# Extended Dynamics Observer for Linear Systems with.pdf

## Page 1

See discussions, stats, and author profiles for this publication at: https://www.researchgate.net/publication/369368273
Extended Dynamics Observer for Linear Systems with Disturbance
Article  in  European Journal of Control · April 2023
DOI: 10.1016/j.ejcon.2023.100806
CITATIONS
9
READS
234
2 authors:
Hongyinping Feng
Shanxi University
56 PUBLICATIONS   834 CITATIONS   
SEE PROFILE
Bao-Zhu Guo
Chinese Academy of Sciences
375 PUBLICATIONS   12,296 CITATIONS   
SEE PROFILE
All content following this page was uploaded by Bao-Zhu Guo on 20 March 2023.
The user has requested enhancement of the downloaded file.

## Page 2

Extended Dynamics Observer for Linear Systems with
Disturbance∗
Hongyinping Fenga† and
Bao-Zhu Guob,c
aSchool of Mathematical Sciences, Shanxi University, Taiyuan, Shanxi, 030006, China
bSchool of Mathematics and Physics, North China Electric Power University, Beijing 102206, China
cKey Laboratory of System and Control, Academy of Mathematics and Systems Science,
Academia Sinica, Beijing, China
October 22, 2022
Abstract
This paper aims at designing observer for single-input-single-output (SISO) linear ﬁnite-
dimensional systems corrupted by general disturbances. A new observer, referred to as extended
dynamics observer (EDO), is proposed to estimate both state and disturbance simultaneously.
The only assumption for the observer design is that the plant with unknown disturbance is
observable. The disturbance is treated by combination of high-gain and internal model contained
in the extended dynamics. The main advantage of the developed method lies in the maximum
utilization of the prior information of the disturbance. The more accurate the prior disturbance
dynamics we have, the better performance the observer would be. The well-posedness of EDO
is established and the theoretical results are validated by numerical simulations.
Keywords:
Active disturbance rejection control, internal model principle, disturbance, ob-
server, system dynamics.
1
Introduction
The observer design is one of the important topics in modern control theory, which has various
applications in output feedback control, system monitoring, process identiﬁcation and fault detec-
tion, among many others. The tolerance of external disturbance and system uncertainty becomes
a major concern in observer design. Many methods for observer design have been developed for
uncertain systems. These include but not limited to the sliding mode observer [15], [20], the high-
gain observer [14], the unknown input observer [21],[8], the observer based approach in internal
model principle [18], and the adaptive observer [12], to name just a few. If the system state and
∗This work is supported by the National Natural Science Foundation of China, Nos. 62273217,12131008.
†Corresponding author. Email: fhyp@sxu.edu.cn.
1

## Page 3

the disturbance were estimated eﬀectively online, the control system with disturbance would be-
come almost known, which makes the feedback control design much easier. In particular, when
the disturbance lies in the control channel, the disturbance can be compensated by its estimation
directly. The observer design is therefore very important to the controller design, in particular to
the estimation/cancellation strategy in the active disturbance rejection control (ADRC) [7].
The extended state observer (ESO), as a key part of ADRC, can estimate both the disturbance
and system state simultaneously by using the high-gain technique.
Regarding the un-modeled
dynamics of system as a disturbance, ESO is similar with the high-gain observer [6, 4, 16, 5].
Actually, ESO is always working provided the derivative of the disturbance is bounded. However,
every coin has two sides.
On the one hand, the model free characteristic leads to the strong
robustness to the uncertainty and disturbance, and on the other hand, it may waste more or less
some useful prior information that we have already known about plant and disturbance. The waste
of the prior disturbance information also exists with varying degrees in other observers such as the
sliding mode observer [15] and the extended high-gain observer [3], [19]. Actually, in engineering
applications, we are not always completely ignorant of the disturbance. Some information like
smoothness, boundedness, particularly some dynamic information of the disturbance are available
sometimes. This prior information might be useful or even valuable for control purpose. A typical
example is the harmonic disturbance where the known frequencies are very useful in internal model
principle (IMP) which is an elegant approach to robust output regulation [9] yet are completely
wasted in ADRC. However, the disturbance in IMP is almost known. Precisely, the dynamics or
the dynamical structure of disturbance are required to be known in IMP, which blocks the general
disturbance out the door of IMP although there are a few extensions of IMP ([11], [10]). In one
word, there is still much room for improvement for both ADRC and IMP but has not been noticed
and emphasized at least in existing literature from the best of our knowledge.
In this paper, we propose a new idea to the observer design which can make maximum use of
the prior disturbance information. Our starting point for observer design is the suﬃcient utilization
of the prior disturbance dynamics. This enables us to develop a fundamental principle to design
observer via online measurement from the plant and prior information of the disturbance. We
believe that a good observer should possess not only the strong robustness to the disturbance but
also the ability to make suﬃcient use of all the valuable prior information of the disturbance. The
more the prior information is properly used, the better performance of the observer would be.
Even the prior information is insuﬃcient, the observer can still do its best. In this spirit, a new
observer, referred to as extend dynamics observer (EDO), is designed in this paper to estimate both
disturbance and system state simultaneously. The EDO inherits almost all the advantages from the
ESO like model free characteristic yet can properly utilize the prior information not only about the
control plant but also the disturbance. If all the prior dynamic information about the disturbance
is available, the EDO can achieve a zero steady-state error. The EDO takes advantages of the IMP
and ADRC and remedies the defect of each of them.
2

## Page 4

Consider the following SISO system:



˙x(t) = Ax(t) + Bd(t),
y(t) = Cx(t),
(1.1)
where A ∈Rn×n, C ∈R1×n, B ∈Rn, y(·) is the measurement and d(·) is the total disturbance.
In this paper, all the unknown signals are referred to as disturbances which may contain system
uncertainties and external disturbances, that is, the disturbance d(t) can be decomposed into d(t) =
d0(t)+f(x(t)), where the d0(·) is the external disturbance and f : Rn →R is an unknown function.
Since the estimation of the state and disturbance is a key issue in the feedback linearization ([7, 3]),
we focus only on the observer design in this paper for system (1.1).
The rest of the paper is organized as follows. In the next section, Section 2, we consider the
observability of system (1.1). Section 3 is devoted to the observer design. The proof of the main
results are presented in Section 4. In Section 5, we apply the proposed EDO to deal with the
high frequency disturbance. Numerical simulations are carried out in Section 7 to validate the
theoretical results, followed up by conclusions in Section 8.
Throughout the paper, n and m denote the positive integers and Rn denotes the n-dimensional
Euclidean space. The norm of Rn is denoted by ∥· ∥Rn.
The spectrum of operator or matrix
A is denoted by σ(A); the transpose of matrix A is represented by A⊤; Λmax(A) stands for the
maximal real part of eigenvalues of A. For simplicity, we denote C+ = {λ ∈C | Reλ ≥0} and
∥· ∥∞= ∥· ∥L∞[0,∞).
2
Observability
In this section, we consider observability for linear system with disturbance. Generally speaking,
not all continuous disturbances can be estimated eﬀectively in real time by a deterministic dynamic
system. For instance, if the disturbance is a sample path of the Wiener process, it is diﬀerentiable
for no time t ≥0. In this case, we do not have any dynamic information about the disturbance and
the estimation of such a disturbance via typical dynamic system observer seems impossible. Based
on this observation, we ﬁrst limit ourselves into an estimable signal space of the following:
W 1,∞(R+) =
n
f : (0, +∞) →R is locally integrable
 f, ˙f ∈L∞(0, +∞)
o
,
(2.1)
where the notation ˙f(·) can be regarded as the weak derivative of f(·) deﬁned by
Z +∞
0
˙f(x)φ(x)dx = −
Z +∞
0
f(x) ˙φ(x)dx,
∀φ ∈C∞
0 (0, ∞),
(2.2)
where C∞
0 (0, ∞) stands for the space of inﬁnitely diﬀerentiable functions with compact support in
(0, +∞). By [1, p.249], W 1,∞(R+) is a Banach space equipped with the norm
∥f∥W 1,∞(R+) = ∥f∥∞+ ∥˙f∥∞,
∀f ∈W 1,∞(R+).
(2.3)
3

## Page 5

Since the piecewise signal like
sT (t) =



et,
t ∈[0, T],
eT ,
t ≥T
(2.4)
belongs to W 1,∞(R+), the signal space W 1,∞(R+) is quite general and can include the harmonic
signals, bounded continuously diﬀerentiable periodic signals, piecewise polynomial signals, piecewise
exponential signals and their linear combinations.
Deﬁnition 1. Let A ∈Rn×n, B ∈Rn and C ∈R1×n. Suppose that Θ is a set of signals and we
know that d ∈Θ. System (1.1) is said to be observable for the signal set Θ, provided both the
initial state and the disturbance are distinguishable in the sense that: For any T > 0,
y(t) = 0 for a.e. t ∈[0, T] ⇒x(0) = 0 and d(t) = 0 for a.e. t ∈[0, T].
(2.5)
From Deﬁnition 1, we see that system (1.1) is observable for Θ, it must have naturally that the
(C, A) is an observable pair. However, Deﬁnition 1 is diﬀerent from the observability of (C, A) for
which the observability on some ﬁnite interval [0, T] implies the observability on entire [0, +∞).
Owing to the uncertainty of the disturbance, it is generally impossible to estimate the disturbance
on [T, +∞) by the information of output over [0, T].
Suppose that (C, A) is an observable pair. Then, system (1.1) is equivalent to its observability
canonical form with
A =


0
0
· · ·
0
a1
1
0
· · ·
0
a2
0
1
· · ·
0
a3
...
...
...
...
...
0
0
· · ·
1
an


,
B =


b1
b2
...
bn−1
bn


̸= 0, C = [0 0 · · · 0 1] ∈R1×n.
(2.6)
The following Lemma 2.1 characterizes the observability of system (1.1) for W 1,∞(R+).
Lemma 2.1. Suppose that (C, A) is an observable pair.
Then, system (1.1) is observable for
W 1,∞(R+) if and only if its observability canonical form (2.6) satisﬁes b2 = b3 = · · · = bn = 0 and
b1 ̸= 0.
By Lemma 2.1, when system (1.1) is observable for W 1,∞(R+), system (1.1) with the observ-
ability canonical form (2.6) satisﬁes the familiar form
y(n)(t) = a1y(t) + a2 ˙y(t) + · · · + any(n−1)(t) + b1d(t),
y(t) = xn(t).
(2.7)
From now on, we always assume without loss the generality the following Assumption 2.1.
Assumption 2.1. The pair (C, A) is observable and system (1.1) takes its observability canonical
form (2.6) with b1 = 1 and bi = 0, i = 2, 3, · · · , n.
4

## Page 6

3
Extended dynamics observer
In this section, we shall design an observer for system (1.1) with d ∈W 1,∞(R+). In many circum-
stances, d(·) is not completely unknown and may contain for instance some part that is generated
by (m + 1)-order diﬀerential equation of the following:
s(m+1)(t) = g0s(t) + g1 ˙s(t) + · · · + gms(m)(t),
gi ∈R, i = 0, 1, · · · , m,
(3.1)
which can be written, like in the internal model principle, as an exosystem with the matrix G and
its observation matrix E1 as follows:
G =


0
1
0
· · ·
0
0
0
1
· · ·
0
...
...
...
...
...
0
0
0
· · ·
1
g0
g1
g2
· · ·
gm


∈R(m+1)×(m+1),
E1 = [1 0 0 · · · 0].
(3.2)
It is evident that the pair (E1, G) is always observable. By [2], we deﬁne
Ω(G) =
n
E1v(t)
˙v(t) = Gv(t), v(0) ∈Rm+1, t ≥0
o
=
n
E1eGtv0
v0 ∈Rm+1, t ≥0
o
.
(3.3)
Then, Ω(G) ⊂W 1,∞(R+) as long as σ(G) ⊂iR and each eigenvalue of G is algebraically simple.
Remark 3.1. It should be pointed that the properly chosen (E1, G) is quite general for extracting
the useful dynamics of the total disturbance d(·). Actually, let (F, S) be an arbitrary observable
system with the state space Rm+1 and output space R. Deﬁne
Ω(S) =

Fv(t)| ˙v(t) = Sv(t), v(0) ∈Rm+1, t ≥0
	
.
(3.4)
Then all disturbance in Ω(S) with known S can be treated by the internal model principle. On the
other hand, it follows from [2] that Ω(S) is independent of F and
Ω(S)
= span

tnλ−keλtλ ∈σ(S), k = 1, · · · , nλ, t ≥0,
nλ is the algebraic multiplicity of λ as an eigenvalue of S} .
(3.5)
As a result, Ω(S) = Ω(G) provided that S is similar to G. When (F, S) is observable, there always
exists an invertible matrix P such that PSP −1 = G and E1 = FP −1. This implies that any useful
dynamic information of the general total disturbance can be extracted by our special form (E1, G)
deﬁned by (3.2).
Proposition 3.1. Let (E1, G) be given by (3.2) and Ω(G) be given by (3.3). Then, for any Q ∈
R1×(m+1) such that the pair (Q, G) is observable, it must have
Ω(G) =
n
Qv(t)
˙v(t) = Gv(t), ∀v(0) ∈Rm+1o
.
(3.6)
5

## Page 7

For any s ∈W 1,∞(R+), we denote by PGs the projection of s on Ω(G), that is,
PGs = arg
inf
g∈Ω(G) ∥s −g∥W 1,∞(R+),
∀s ∈W 1,∞(R+).
(3.7)
Since Ω(G) is a ﬁnite-dimensional subspace of the Banach space W 1,∞(R+), the PGs must exist
for any s ∈W 1,∞(R+) ([22, p.35]).
In order to make use of the disturbance dynamics, we ﬁrst need to write the disturbance
dynamically.
Lemma 3.1. Suppose that the matrix G deﬁned by (3.2) satisﬁes g0 = 0.
Let (Q, G) be an
observable pair with Q ∈R1×(m+1). Then, for any d ∈W 1,∞(R+), there exists a v0 ∈Rm+1 such
that





˙v(t) = Gv(t) + Bd
QBd
˙e(t),
v(0) = v0,
d(t) = Qv(t),
(3.8)
where Bd ∈Rm+1 is the eigenvector corresponding to the eigenvalue 0 of G, e = (I −PG)d and PG
is given by (3.7).
Given d ∈W 1,∞(R+), we want to ﬁnd a G by properly choosing gi, i = 0, 1, 2, · · · , m in
(3.2) such that the approximation error ∥(I −PG)d∥W 1,∞(R+) is as small as possible. The part
PGd ∈Ω(G) will be treated by the internal model principle through extended state observer, while
the remaining part ∥(I −PG)d∥W 1,∞(R+) will be dealt with by the high-gain technique. Since the
high-gain technique needs 0 ∈σ(G), we assume that g0 = 0 in Lemma 3.1. By Lemma 3.1, system
(1.1) can be written dynamically as











˙x(t) = Ax(t) + BQv(t),
˙v(t) = Gv(t) + Bd
QBd
˙e(t),
y(t) = Cx(t).
(3.9)
where e = (I −PG)d and PG is given by (3.7). As a result, the observer design of system (1.1) comes
down to the observer design of system (3.9). Hence, the EDO of system (1.1) with its canonical
form (2.6) can be designed as



˙ˆx(t) = [A + (Kωo + SE)C]ˆx(t) + BQˆv(t) −(Kωo + SE)y(t),
˙ˆv(t) = Gˆv(t) −ECˆx(t) + Ey(t),
(3.10)
where ωo denotes the positive tuning gain, E = [0 0 · · · 1]⊤∈Rm+1, Kωo ∈Rn is a vector such
that
Λmax(A + KωoC) = −ωo,
(3.11)
S ∈Rn×(m+1) and Q ∈R1×(m+1) are the solutions of the equations
(A + KωoC)S −SG = BQ,
CS = Pωo,
(3.12)
6

## Page 8

with Pωo ∈Rm+1 being a vector such that
Λmax(G + EPωo) = −ωo.
(3.13)
Let the observer errors be denoted by
˜x(t) = x(t) −ˆx(t) and ˜v(t) = v(t) −ˆv(t).
(3.14)
Then, the errors are governed by





˙˜x(t) = [A + (Kωo + SE)C]˜x(t) + BQ˜v(t),
˙˜v(t) = G˜v(t) −EC˜x(t) + Bd
QBd
˙e(t).
(3.15)
System (3.15) can be written as
d
dt(˜x(t), ˜v(t))⊤= A(˜x(t), ˜v(t))⊤+ B ˙e(t),
(3.16)
where
A =
"
A + (Kωo + SE)C
BQ
−EC
G
#
, B =
1
QBd

0
Bd

.
(3.17)
In terms of the solution S of the Sylvester equation of (3.12), we introduce the transformation
P =
"
In
S
0
Im+1
#
,
(3.18)
where In and Im+1 are the identity matrices on Rn and Rm+1, respectively. Thanks to the choice
of Kωo, E and S, a simple computation shows that
PAP−1 =
"
A + KωoC
0
−EC
G + EPωo
#
,
(3.19)
which, together with (3.11) and (3.13), implies that the system matrix A of the error system (3.15)
is Hurwitz. The equations (3.12) are very important in the observer design and their solvability is
guaranteed by Lemma 4.1 in Section 4.
We are now in a position to summarize an implementable design scheme:
• Choose K = [k1 −a1
k2 −a2
· · ·
kn −an]⊤and P = [p0
p1 −g1
· · ·
pm −gm] such
that the matrices A + KC and G + EP are Hurwitz. Let
Kωo = [k1ωn
o −a1 k2ωn−1
o
−a2
· · ·
knωo −an]⊤
(3.20)
and
Pωo = [p0ωm+1
o
p1ωm
o −g1
· · ·
pmωo −gm],
(3.21)
where ωo is a positive tuning parameter;
7

## Page 9

• Solve the equations (3.12) to obtain S ∈Rn×(m+1) and Q ∈R1×(m+1).
Thanks to the choices of P and Pωo, a straightforward computation shows that
λωo ∈σ(A + KωoC) if and only if λ ∈σ(A + KC).
(3.22)
Similarly, we also have
λωo ∈σ(G + EPωo) if and only if λ ∈σ(G + EP).
(3.23)
By (3.22) and (3.23), we can change Λmax(A + KωoC) and Λmax(G + EPωo) by adjusting the
gain constant ωo only. As a result, there is only one parameter that aﬀects the performance of
the observer. The mechanism of the observer design is based on the deep understanding about
the internal model principle and the high-gain technique. Since the high-gain observer and the
IMP-based observer have diﬀerent structures. The combination of two diﬀerent approaches is not
straightforward.
Now, we state our main result Theorem 3.1.
Theorem 3.1. In addition to the Assumption 2.1, suppose that the matrix G deﬁned by (3.2) is
diagonalizable, g0 = 0 and
σ(G) ⊂C+.
(3.24)
Then, the EDO (3.10) for system (1.1) is well-posed: For any d ∈W 1,∞(R+) and (ˆx(0), ˆv(0)) ∈
Rn × Rm+1, there exists a positive constant M1, independent of ωo, such that
lim
t→∞∥x(t) −ˆx(t)∥Rn ≤M1∥e∥W 1,∞(R+)
ωo
,
(3.25)
where e = (I −PG)d and PG is given by (3.7). In particular, there exists a positive constant M2,
independent of ωo, such that
lim
t→∞|d(t) −Qˆv(t)| ≤M2∥e∥W 1,∞(R+)
ωo
.
(3.26)
Remark 3.2. We claim that the results in Theorem 3.1 can be actually applied to any system
(1.1) that is observable for W 1,∞(R+). Actually, when system (1.1) is observable for W 1,∞(R+)
but the Assumption 2.1 is not satisﬁed, by Lemma 2.1, one can always convert system (1.1) into
the canonical form (2.6) for which the Assumption 2.1 is satisﬁed. Moreover, it follows from (3.8)
and (4.51) below that the derivative of the approximation error e(t) and its boundedness have been
used in the proof of the Theorem 3.1. Hence, we should deﬁne in (3.7) the best approximation PG
with the norm ∥· ∥W 1,∞(R+) instead of the conventional Hilbert space norm ∥· ∥L2(R+) although the
L2(R+) is complete and there exists a minimizer in dealing with the projection.
Remark 3.3. For any d ∈W 1,∞(R+) and any matrix G, the disturbance can be divided into two
parts:
d(t) = PGd + e with e = (I −PG)d,
(3.27)
8

## Page 10

where PGd is given by (3.7). It is seen from observer (3.10) that it depends only on any given
G satisfying (3.24) yet does not depend on the decomposition (3.27). The decomposition (3.27)
is reﬂected only on the observation errors (3.25) and (3.26). We can improve the accuracy of the
observer by proper choosing G and the choice of G depends on the prior information that we have
known about the disturbance.
By (3.25), the accuracy of the observer depends both on the best approximation of d(·) on
Ω(G) and the decay rate ωo. This implies that there are two ways to improve the accuracy of the
observer. First, choose the G so that Ω(G) is as large as possible to make the approximation error
∥e∥W 1,∞(R+) be as small as possible. Second, increase the gain ωo. The choice of G depends on the
prior information about the disturbance. The more accurate prior disturbance dynamics we have
known, the smaller the steady-state error of the observer (3.10) will be. In particular, if we have
known all the disturbance dynamics, i.e., we have known d ∈Ω(G), the steady-state error becomes
zero. Although the increasing of the gain ωo can improve the observer accuracy, ωo can not be,
however, arbitrary large in engineering applications. This is the reason we need at all possible to
make maximum use of known information of d(·) to reduce ω0.
Corollary 3.1. In addition to Assumption 2.1, suppose that the matrix G deﬁned by (3.2) satisﬁes
(3.24). Then, for any d ∈Ω(G) and (ˆx(0), ˆv(0)) ∈Rn × Rm+1, the EDO (3.10) for system (1.1)
satisﬁes
lim
t→∞eβt [∥x(t) −ˆx(t)∥Rn + |d(t) −Qˆv(t)|] = 0,
∀0 < β < ωo.
(3.28)
4
Proof of main results
In this section, we give proofs of the results stated in previous sections.
Proof of Lemma 2.1. Suppose that b1 ̸= 0 and b2 = b3 = · · · = bn = 0. Then, for any T > 0,
u(t) = 0 for a.e. t ∈[0, T] implies that

















˙x1(t) = a1xn(t) + b1d(t),
˙x2(t) = x1(t) + a2xn(t),
· · · · · · · · · · · · · · · · · · · · ·
˙xn(t) = xn−1(t) + anxn(t),
a.e. t ∈[0, T],
(4.1)
where x(t) = [x1(t)
x2(t)
· · ·
xn(t)]⊤.
If y(t) = xn(t) = 0 for a.e.
t ∈[0, T], (4.1) yields
xn(t) = xn−1(t) = · · · = x1(t) = 0, which implies that d(t) = 0 for a.e. t ∈[0, T] due to b1 ̸= 0.
Hence, system (1.1) is observable for W 1,∞(R+).
Conversely, suppose that system (1.1) is observable for W 1,∞(R+). We ﬁrst claim that bn = 0.
9

## Page 11

Otherwise, for any T > 0,

























˙x1(t) = a1xn(t) + b1d(t),
˙x2(t) = x1(t) + a2xn(t) + b2d(t),
· · · · · · · · · · · · · · · · · · · · ·
˙xn(t) = xn−1(t) + anxn(t) + bnd(t),
y(t) = xn(t) = 0,
a.e. t ∈[0, T]
(4.2)
implies that xn−1(t) + bnd(t) = 0 for a.e. t ∈[0, T] and hence system (4.2) turns out to be







˙x1(t) = −b1
bn
xn−1(t),
˙xj(t) = xj−1(t) −bj
bn
xn−1(t),
j = 2, · · · , n −1
(4.3)
for a.e. t ∈[0, T]. Since system (4.3) with the output xn−1(·) is always observable for any bj ∈R,
j = 1, 2, · · · , n, each non-zero solution of system (4.3) satisﬁes xn−1(t) = −bnd(t) ̸= 0 for a.e. t ∈
[0, T] and hence is the zero dynamics of the original system (4.2). This contradicts the observability
of system (1.1) and hence bn = 0. Similarly, we can obtain bn−1 = · · · = b2 = 0 by repeating the
same process. This completes the proof of the lemma due to B ̸= 0.
Proof of Proposition 3.1.
Since both (E1, G) and (Q, G) are observable pairs, there exist
invertible matrix P1 and P2 such that
E1P −1
1 , P1GP −1
1

= (Q0, G0) =
QP −1
2 , P2GP −1
2

,
(4.4)
where (Q0, G0) is the observability canonical form. As a result,
E1 = QP −1
2 P1,
G = P −1
1 P2GP −1
2 P1,
(4.5)
and hence
E1eGt = QP −1
2 P1e(P −1
1
P2GP −1
2
P1)t = QP −1
2 P1P −1
1 P2eGtP −1
2 P1 = QeGtP −1
2 P1.
(4.6)
This, together with (3.3), yields (3.6).
Proof of Lemma 3.1. Since (Q, G) is an observable pair and 0 ∈σ(G), it follows from the Hautus
test [17, p.15, Remark 1.5.2] that KerG ∩KerQ = {0}. This means QBd ̸= 0 by the fact GBd = 0
and Bd ̸= 0. The ﬁrst equation of (3.8) therefore makes sense. Since PGd ∈Ω(G), it can be written
dynamically as
˙v1(t) = Gv1(t),
(PGd)(t) = Qv1(t)
(4.7)
for some initial state. Since GBd = 0, by setting
v2(t) = d(t) −(PGd)(t)
QBd
Bd = e(t)
QBd
Bd,
t ≥0,
(4.8)
10

## Page 12

it has





˙v2(t) = Gv2(t) + Bd
QBd
˙e(t), v2(0) = e(0)
QBd
Bd,
e(t) = Qv2(t).
(4.9)
Since d ∈W 1,∞(R+), e ∈W 1,∞(R+) as well. As a result, e is diﬀerentiable almost everywhere for
[0, ∞) [1, p.280,Theorem 5]. Hence, ˙e in (4.9) makes sense. System (3.8) then follows from (4.7)
and (4.9) by letting v(t) = v1(t) + v2(t).
Before prove Theorem 3.1, we ﬁrst give a Lemma.
Lemma 4.1. Under the assumptions of Theorem 3.1, the equations (3.12) are always solvable.
Moreover, the following assertions are true:
(i) The pair (Q, G) is observable;
(ii) For any s ∈C+, there exist two positive constants CK and CA, independent of ωo and s,
such that
∥[s −(A + KωoC)]−1B∥Rn ≤CK
ωo
,
(4.10)
1
|QBd| =
1
|k1p0|ωn+m+1
o
(4.11)
and
∥C[s −(A + KωoC)]−1∥Rn ≤CA
ωno
;
(4.12)
(iii) For any s ∈C+, there exists a positive constant CG, independent of ωo and s, such that
∥[s −(G + EPωo)]−1E∥Rm+1 ≤
CG
ωm+1
o
,
∀s ∈C+;
(4.13)
(iv) If G is diagonalizable, then there exist two positive constants CS and CQ, independent of
ωo and s, such that
∥Sv∥Rn ≤CS∥v∥Rm+1ωm+n
o
,
∀v ∈Rm+1,
(4.14)
and
|Q[s −(G + EPωo)]−1Bd| ≤CQωm+n
o
,
∀s ∈C+.
(4.15)
Proof. Since A + KC is Hurwitz and by the choice of A, B, C and Kωo, a simple computation
shows that A + KωoC is Hurwitz as well. Since the matrix
A + KωoC =


0
0
· · ·
0
k1ωn
o
1
0
· · ·
0
k2ωn−1
o
0
1
· · ·
0
k3ωn−2
o
...
...
...
...
...
0
0
· · ·
1
knωo


(4.16)
is Hurwitz, (3.24) implies that
σ(A + KωoC) ∩σ(G) = ∅.
(4.17)
11

## Page 13

Moreover, a simple computation shows that
[λ −(A + KωoC)]−1B =
Kλ
ρA(λ, ωo),
λ ∈C+,
(4.18)
where
Kλ =


knλn−2ωo + · · · + k3λωn−2
o
+ k2ωn−1
o
−λn−1
knλn−3ωo + · · · + k3ωn−2
o
−λn−2
...
knωo −λ
−1


(4.19)
and
ρA(λ, ωo) = knλn−1ωo + · · · + k2λωn−1
o
+ k1ωn
o −λn.
(4.20)
Hence, the following transmission zeros condition holds:
C[λ −(A + KωoC)]−1B =
−1
ρA(λ, ωo),
∀λ ∈C+.
(4.21)
By [13], (4.17) and (4.21), the equations (3.12) are solvable.
(i). Suppose that Gh = λh and Qh = 0 with λ ∈σ(G). Then, the Sylvester equation in (3.12)
turns out to be (A + KωoC −λ)Sh = BQh = 0. By (4.17), we conclude that λ /∈σ(A + KωoC) and
hence A + KωoC −λ is invertible. As a result, Sh = 0 and CSh = Pωoh = 0. By [17, p. Remark
1.5.2], we have h = 0 provided (G, Pωo) is an observable pair. Using [17, p. Remark 1.5.2] again,
(Q, G) is an observable pair if we can prove so is for (G, Pωo). Actually, for any Gv = λv and
Pωov = 0 with λ ∈σ(G), we have (G + EPωo)v = Gv = λv. Since G + EP is Hurwitz, it follows
from (3.2) and (3.21) that G + EPωo is Hurwitz as well.
By (3.24) and the fact λ ∈σ(G), we obtain λ /∈σ(G+EPωo). Hence, (G+EPωo)v = λv implies
that v = 0. By [17, p. Remark 1.5.2], (G, Pωo) is an observable pair.
(ii). Since A + KωoC is Hurwitz, it follows from (4.16) that k1 ̸= 0. The (4.10) can thus be
obtained by (4.18), (4.19) and (4.20) easily. Since GBd = 0, it follows from (3.12) that
(A + KωoC)SBd = BQBd
(4.22)
and hence
PωoBd = CSBd = C(A + KωoC)−1BQBd.
(4.23)
By (3.2) and (3.21),
PωoBd = p0ωm+1
o
.
(4.24)
Since (Q, G) is an observable pair and GBd = 0, the Hautus test [17, p.15, Remark 1.5.2] implies
that QBd ̸= 0. We then combine (4.21), (4.24) and (4.23) to obtain p0ωm+1
o
̸= 0 and
1
QBd
= C(A + KωoC)−1B
PωoBd
=
1
k1p0ωn+m+1
o
,
(4.25)
12

## Page 14

which leads to (4.11). In view of (4.16), a straightforward computation shows that, for any s ∈C+,
C[s −(A + KωoC)]−1 =
−1
ρA(s, ωo)[1
s
· · ·
sn−1],
which, together with (4.20), leads to (4.12).
(iii). By a straightforward computation, it follows that
G + EPωo =


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
p0ωm+1
o
p1ωm
o
· · ·
pmωo


(4.26)
and hence
[s −(G + EPωo)]−1E =
−1
ρG(s, ωo)


1
s
...
sm


,
s ∈C+,
(4.27)
where
ρG(s, ωo) = p0ωm+1
o
+ p1ωm
o s + · · · + pmωosm −sm+1.
(4.28)
Since G + EPωo is Hurwitz, we have p0 ̸= 0 and so (4.13) follows from (4.27) and (4.28).
(iv). Since G is diagonalizable, for any v ∈Rm+1, there exists a sequence v0, v1, v2, · · · , vm such
that v = Pm
j=0 vjεj, where Gεj = λjεj with λj ∈σ(G), j = 0, 1, 2, · · · , m. By (3.12), (4.18) and
(4.21), we have
Sεj = (A + KωoC −λj)−1BQεj = −QεjKλj
ρA(λj, ωo)
(4.29)
and
Pωoεj
= CSεj = C(A + KωoC −λj)−1BQεj
=
Qεj
ρA(λj, ωo).
(4.30)
Consequently,
Qεj = PωoεjρA(λj, ωo),
j = 0, 1, · · · , m,
(4.31)
which, together with (4.29), gives
Sv =
m
X
j=0
vjSεj = −
m
X
j=0
vjPωoεjKλj.
(4.32)
Combining (4.19), (3.21) and (4.32), we obtain (4.14).
Taking (4.26) and (3.2) into account, a simple computation shows that
[s −(G + EPωo)]−1Bd =
1
ρG(s, ωo)


pmsm−1ωo + pm−1sm−2ω2
o + · · · + p1ωm
o −sm
−p0ωm+1
o
−p0ωm+1
o
s
...
−p0ωm+1
o
sm−1


(4.33)
13

## Page 15

for any s ∈C+. By (4.28) and the fact p0 ̸= 0, there exists a positive constant M1, independent of
ωo and s, such that
∥G[s −(G + EPωo)]−1Bd∥Rm+1 ≤M1∥G∥
(4.34)
for any s ∈C+. Consequently, it follows from (4.14), (4.12) and (4.34) that
|C[s −(A + KωoC)]−1SG[s −(G + EPωo)]−1Bd| ≤CSM1∥G∥CAωm
o .
(4.35)
Combining (3.21), (4.28) and (4.33), there exists a positive constant M2, independent of ωo and s,
such that
|Pωo[s −(G + EPωo)]−1Bd| ≤M2ωm
o ,
∀s ∈C+.
(4.36)
For any v ∈Rm+1, it follows from (3.12) and (4.21) that
Qv = Pωov −C(A + KωoC)−1SGv
C(A + KωoC)−1B
= −ρA(λ, ωo)[Pωov −C(A + KωoC)−1SGv].
(4.37)
As a result, there exists an M3, independent of ωo, such that
|Qv| = M3ωn
o
h
|Pωov| + |C(A + KωoC)−1SGv|
i
,
∀v ∈Rm+1,
(4.38)
which, together with (4.35) and (4.36), leads to (4.15).
Proof of Theorem 3.1.
Let the observer errors be (3.14). Then, they are governed by (3.15),
or equivalently its abstract form (3.16). Let
AS =
"
A + KωoC
0
−EC
G + EPωo
#
, BS =


SBd
QBd
Bd
QBd

.
(4.39)
A simple computation shows that
PAP−1 = AS and BS = PB,
(4.40)
where A, B are those in (3.16), P is that in (3.18), and the Sylvester equation in (3.12) was used.
For any s ∈C+, a simple computation shows that
P−1(s −AS)−1BS =
1
QBd

[s −(A + KωoC)]−1SBd + SJ(s)
−J(s)

,
(4.41)
where
J(s) = −[s −(G + EPωo)]−1Bd + [s −(G + EPωo)]−1EC[s −(A + KωoC)]−1SBd.
(4.42)
Since GBd = 0, it follows from (3.12) that
SBd = (A + KωoC)−1BQBd,
(4.43)
14

## Page 16

and hence
[s −(A + KωoC)]−1SBd
QBd
= (A + KωoC)−1[s −(A + KωoC)]−1B.
(4.44)
By Lemma 4.1, there exist two positive constants CK and CS such that

[s −(A + KωoC)]−1SBd
QBd

Rn ≤CK
ω2o
,
(4.45)
and
∥SJ(s)∥Rn
|QBd|
≤CS∥J(s)∥Rm+1ωm+n
o
ωn+m+1
o
= CS∥J(s)∥Rm+1
ωo
,
∀s ∈C+.
(4.46)
By (4.28), (4.33) and the fact p0 ̸= 0, there exists a CJ > 0 such that
∥J(s)∥Rm+1 < CJ,
∀s ∈C+.
(4.47)
Combining (4.46), (4.47), (4.42), (4.45), (4.41) and (4.11), we arrive at
∥P−1(s −AS)−1BS∥Rn ≤CA
ωo
,
∀s ∈C+,
(4.48)
where CA is a positive constant independent of ωo and s. Furthermore, it follows from (4.40) that
∥(s −A)−1B∥Rn = ∥P−1(s −AS)−1BS∥Rn ≤CA
ωo
(4.49)
for any s ∈C+. Since both A + KωoC and G + EPωo are Hurwitz and satisfy (3.23) and (3.22),
respectively, the matrix A is also Hurwitz. By (4.49), there exists an LB > 0, independent of ωo,
such that
∥eAtB∥Rn×Rm+1 ≤LBe−ωot,
t ≥0.
(4.50)
We solve (3.16) to obtain
∥(˜x(t), ˜v(t))∥Rn×Rm+1 =
eAt(˜x(0), ˜v(0))⊤+
Z t
0
eA(t−s)B ˙e(s)ds

Rn×Rm+1
≤LAe−ωotX0 + LB
Z t
0
e−ωo(t−s)∥˙e∥∞ds ≤LAe−ωotX0 + ∥e∥W 1,∞(R+)LB
ωo
,
(4.51)
where X0 = ∥(˜x(0), ˜v(0))∥Rn×Rm+1 and LA is a positive constant. This leads to (3.25) from (3.14).
Now, we prove (3.26). For any s ∈C+, it follows from (4.41) that
QP−1(s −AS)−1BS = −QJ(s)
QBd
,
Q = (0, Q).
(4.52)
By (4.13), (4.12) and (4.14), there exists an M4 > 0 such that
∥[s −(G + EPωo)]−1EC[s −(A + KωoC)]−1SBd∥Rm+1 ≤M4
ωo
,
∀s ∈C+.
(4.53)
By (4.38), (3.21), (4.12) and (4.14), there exists an M5 > 0 such that
|Qv| = M5ωn+m+1
o
∥v∥Rm+1,
∀v ∈Rm+1.
(4.54)
15

## Page 17

We combine (4.53) and (4.54) to obtain
Q[s −(G + EPωo)]−1EC[s −(A + KωoC)]−1SBd
 ≤M4M5ωn+m
o
,
∀s ∈C+,
which, together with (4.15), (4.42), (4.11) and (4.52), leads to
QP−1(s −AS)−1BS
 =

QJ(s)
|QBd|
 ≤M6
ωo
,
(4.55)
where M6 is a positive constant independent of ωo and s. Owing to (4.40), we arrive at
|Q(s −A)−1B| ≤M6
ωo
,
∀s ∈C+.
(4.56)
By (4.56) and the inverse Laplace transform, we obtain
lim
ωo→+∞|QeAtB|
=
1
2πi
lim
ωo→+∞lim
T→∞
Z γ+iT
γ−iT
estQ(s −A)−1Bds
=
1
2πi lim
T→∞
Z γ+iT
γ−iT
est
lim
ωo→+∞Q(s −A)−1Bds
=
1
2πi lim
T→∞
Z γ+iT
γ−iT
est0ds = 0,
t > 0,
(4.57)
where γ is a real number so that the contour path of the integration is in the region of convergence
of QeAtB. Since the largest real part of eigenvalue of A is −ωo, (4.57) implies that
|QeAtB| ≤LQe−ωot,
t ≥0,
(4.58)
where LQ is a positive constant which is independent of ωo. As a result, the solution of system
(3.15) satisﬁes
lim
t→∞|Q˜v(t)| = lim
t→∞
QeAt(˜x(0), ˜v(0))⊤ +
Q
Z t
0
eAsB ˙e(t −s)ds


≤lim
t→∞

Z t
0
LQe−ωos|˙e(t −s)|ds
 ≤LQ∥e∥W 1,∞(R+)
ωo
,
which, together with (3.14) and (3.8), leads to (3.26).
Proof of Corollary 3.1. Since d ∈Ω(G), e = (I −PG)d = 0. By Lemma 4.1, the pair (Q, G) is
observable. It follows from Proposition 3.1 that d(·) can be represented dynamically to be governed
by ˙v(t) = Gv(t), d(t) = Qv(t). Hence, the observer errors (3.14) are governed by
d
dt(˜x(t), ˜v(t))⊤= A(˜x(t), ˜v(t))⊤,
(4.59)
where the matrix A is given by (3.17). Noting that both A + KωoC and G + EPωo are Hurwitz, A
is Hurwitz as well due to the invertible transformation (3.19).
16

## Page 18

5
Application to high frequency disturbance
The main advantage of the observer (3.10) lies in that we give a new way to improve the accuracy
of the observer without increasing the high-gain ωo.
This is very useful when the disturbance
contains high-frequency signals.
If the disturbance d(·) contains the frequencies {α1, · · · , αN},
we can choose g1, g2, · · · , g2N+1 such that the matrix G given by (3.2) with m = 2N satisﬁes
σ(G) = {0, ±αji | j = 1, 2, · · · , N}. Thanks to the Vieta theorem, the choice of the parameters
g0, g1, g2, · · · , g2N+1 is easy and implementable. By (3.7), we have PGd ∈Ω(G) and it follows from
(3.25) that the steady-error of the observer (3.10) depends on the approximation error e = (I−PG)d
instead of the disturbance d(·) itself. Since the error e(·) never contains the frequencies {α1, · · · , αN}
anymore, the negative impact of the signals with frequencies {α1, · · · , αN} has been completely
eliminated by the extended dynamics determined by G.
Although we can design an observer for system (1.1) by the existing approaches such as the
high-gain and the sliding mode methods, the performance of the observer may not be satisfactory
provided the disturbance d(·) contains the high-frequency signals. This is because high-frequency
parts of the disturbance usually leads to large ∥˙d∥∞and the tuning gain of the observer can not
be arbitrarily large in practice.
Next, we will give an example to show the main advantage of the proposed approach by com-
paring with the extended high-gain observer in [3]. For simplicity and without loss of the generality,
we only consider system (1.1) with
A =
"
0
a1
1
a2
#
, B =
"
1
0
#
and C = [0 1],
(5.1)
where aj ∈R, j = 1, 2. Suppose that the disturbance contains the high-frequency α0, i.e.,
d(t) = d1(t) + d0(t),
d1 ∈W 1,∞[0, ∞),
d0(t) = a0 sin α0t + b0 cos α0t,
(5.2)
where a0 and b0 are unknown amplitudes, α0 may be very large.
Suppose that all the prior
knowledge about the disturbance we have known is that
ˆα0 ≈α0 where ˆα0 is known.
(5.3)
With the prior information (5.1) and (5.3), an extended dynamics observer of system (1.1) can be
designed easily by (3.10) with
G =


0
1
0
0
0
1
0
−ˆα2
0
0

.
(5.4)
By a simple computation, we have
∥d0 −PGd0∥W 1,∞[0,∞) ≤∥d0 −(a0 sin ˆα0t + b0 cos ˆα0t)∥W 1,∞[0,∞) ≤M0(α0 −ˆα0),
(5.5)
where M0 = max{α0, ˆα0}(|a0| + |b0|). Consequently, the error e(·) of d(·) on Ω(G) satisﬁes
∥e∥W 1,∞[0,∞) = ∥d −PGd∥W 1,∞[0,∞) ≤∥d1 −PGd1∥W 1,∞[0,∞) + M0(α0 −ˆα0),
(5.6)
17

## Page 19

By (3.25) and (5.6), the upper boundedness of the steady-error of the EDO is
M1∥d1 −PGd1∥W 1,∞[0,∞) + M0(α0 −ˆα0)
ωo
,
(5.7)
where M1 is a positive constant.
It is seen from (5.7) that the high-frequency signal d0(·) has almost no eﬀect on the steady-error
of the EDO, provided the prior information is accurate enough, i.e., |α0 −ˆα0| is suﬃciently small.
In particular, when α0 = ˆα0, the high-frequency signal d0(·) does not aﬀect the steady-error at
all. Thanks to our extended dynamics G in (5.4), we can improve the accuracy of EDO without
increasing the gain ωo. However, the situation become completely diﬀerent if we use the existing
high-gain observer, see for instant the observer in [3]. Actually, the steady-error of the high-gain
observer is M2∥˙d∥∞
ωo
, where M2 is a positive constant and ωo is the tuning gain.
Owing to the
high-frequency content d0 of the disturbance d(·) , ∥˙d∥∞can be very large. This implies that the
tuning gain ωo has to be much larger to ensure the accuracy of the high-gain observer. However,
the large tuning gain ωo may lead to poor transient response in practice.
6
Comparison with the extended state observer
If we choose specially G = 0, then the disturbance dynamics can not be used in the observer (3.10).
In this case, the EDO (3.10) will reduce to a high-gain observer automatically. For example, a
simple computation will show that the observer (3.10) for system (1.1) with setting (5.1) and
G = 0 is











˙ˆx1(t) = a1ˆx2(t) + β1β3ω3
oˆv(t) −[(β1 −β2β3)ω2
o −a1][y(t) −ˆx2(t)],
˙ˆx2(t) = ˆx1(t) + a2ˆx2(t) −[(β2 + β3)ωo −a2][y(t) −ˆx2(t)],
˙ˆv(t) = [y(t) −ˆx2(t)],
(6.1)
where β3 < 0 and the matrix
"
0
β1
1
β2
#
is Hurwitz. In order to make a comparison to ESO [4] and
the high-gain observer [3], we consider the canonical system



˙z(t) = A⊤z(t) + C⊤d(t),
y(t) = B⊤z(t),
z(t) = [z1(t)
z2(t)]⊤,
(6.2)
where A, B and C are still given by (5.1).
By virtue of the observer (6.1) and the invertible
transformation
UAU−1 = A⊤, UB = C⊤, CU−1 = B⊤,
U =
"
0
1
1
a2
#
,
(6.3)
18

## Page 20

the EDO of system (6.2) becomes















˙ˆz1(t) = ˆz2(t) −[(β2 + β3)ωo −a2][y(t) −ˆz1(t)],
˙ˆz2(t) = a1ˆz1(t) + a2ˆz2(t) + β1β3ω3
oˆv(t)
−[(β1 −β2β3)ω2
o + a2(β2 + β3)ωo −a2
2 −a1][y(t) −ˆz1(t)],
˙ˆv(t) = [y(t) −ˆz1(t)].
(6.4)
When a1 = a2 = 0, observer (6.4) is reduced to











˙ˆz1(t) = ˆz2(t) −(β2 + β3)ωo[y(t) −ˆz1(t)],
˙ˆz2(t) = β1β3ω3
oˆv(t) −(β1 −β2β3)ω2
o[y(t) −ˆz1(t)],
˙ˆv(t) = [y(t) −ˆz1(t)],
(6.5)
and at the same time, system (6.2) turns out to be the canonical form of ESO in [4] or high-gain
observer in [3]. In this case, the extended state observer or high-gain observer of system (6.2) is











˙ˆz1(t) = ˆz2(t) −γ1ωo[y(t) −ˆz1(t)],
˙ˆz2(t) = ˆv(t) −γ2ω2
o[y(t) −ˆz1(t)],
˙ˆv(t) = −γ3ω3
o[y(t) −ˆz1(t)],
(6.6)
where γ1, γ2 and γ3 are constants such that the following matrix:


−γ1
1
0
−γ2
0
1
−γ3
0
0

,
(6.7)
is Hurwitz. By proper choices of γ1, γ2 and γ3, the observers (6.6) and (6.5) are equivalent under an
invertible coordinate transformation. From this point, the proposed EDO with constant dynamic
G = 0 covers the ESO as a special case and improves the ESO to the general observable linear
system with input disturbance.
Remark 6.1. It follows from [3] that the conventional high-gain observer usually works for the
chain of n integrators only. However, by Remark 3.2, the observer (3.10) works well for system
(1.1) that is observable for W 1,∞(R+). In particular, the observer (3.10) with G = 0, as a new
high-gain observer, also works well for system (1.1) that is observable for W 1,∞(R+). Hence, we
actually propose a new high-gain observer that is is more general than the well-known high-gain
observer in [3].
7
Numerical simulations
In order to validate the proposed principle visually, we present some simulations for the EDO (3.10).
The ﬁnite diﬀerence scheme is adopted in discretization. The numerical results are programmed
19

## Page 21

in Matlab. The time step is taken as 0.001. Suppose that the plant is known and is given by
(5.1) with a1 = 2 and a2 = 1. Let (x1(0), x2(0)) = (0, 1) and let the initial state of the observer
be zero.
The disturbance is chosen as d(t) = sin t + sin α0t with α0 = 10.
Suppose we have
known that the disturbance contains the frequency α0 = 10. We must point out that “α0 = 10
is known” is just the known prior information rather than a required assumption. If this prior
information is available, we can use it to improve the accuracy eﬀectively. If it is unavailable, the
EDO can still work. Comparing with the conventional ESO, we actually give an additional way to
use the disturbance dynamics which can improve the observer accuracy. We will show this merit
by numerical simulations in this section.
Since we have known the prior dynamics “α0 = 10”, the extended dynamics matrix G of the
observer (3.10) is chosen as (5.4) with ˆα0 = α0 = 10. The tuning gain is chosen as ωo = 20.
Compared with the simulations in [3], the frequency of disturbance here is much larger but the
tuning gain ωo is relatively small. The error of EDO and the disturbance estimation are plotted in
Figure 1. If we choose G = 0, EDO is reduced to the high-gain observer (6.1), which is equivalent to
the conventional ESO by Section 6. The counterparts for the observer (6.1) with the same tuning
gain ωo = 20 are plotted in Figure 2.
Since the observer gain ωo is relatively small and the prior information “α0 = 10 is known” is
wasted, the error of estimation is not satisfactory for the ESO (or equivalently, the high-gain ob-
server). However, the accuracy of EDO can be improved signiﬁcantly by using the prior information
“α0 = 10”. We increase the tuning gain of the ESO in Figure 3 by choosing ωo = 100. However,
the steady-state error is still not satisfactory. Worse of all, a serious “peaking phenomenon” takes
place during the transient time. Therefore, improving the accuracy of ESO by increasing the tuning
gain only is not feasible. The EDO gives a way to reach the high observer accuracy with relatively
small tuning gain ωo by using the prior information “α0 = 10 is known”. This implies that the
EDO can tolerate more measuring noise than the ESO due to the small tuning gain ωo.
0
0.5
1
1.5
2
2.5
3
3.5
4
4.5
t
-0.4
-0.2
0
0.2
0.4
0.6
0.8
1
(a) Error of state estimation
0
1
2
3
4
5
6
7
t
-10
-5
0
5
10
15
20
(b) d(·) and its estimation
Figure 1: Estimation error of extended dynamics observer (3.10).
20

## Page 22

0
1
2
3
4
5
6
t
-0.4
-0.2
0
0.2
0.4
0.6
0.8
1
(a) Error of state estimation
0
1
2
3
4
5
6
7
t
-6
-4
-2
0
2
4
6
8
(b) d(·) and its estimation
Figure 2: Estimation error of high-gain observer (6.1).
0
1
2
3
4
5
6
t
-0.4
-0.2
0
0.2
0.4
0.6
0.8
1
(a) Error of state estimation
0
1
2
3
4
5
6
7
t
-10
-5
0
5
10
15
20
25
30
(b) d(·) and its estimation
Figure 3: Estimation error of high-gain observer (6.1) with ωo = 100.
8
Conclusions
In this paper, a novel dynamics compensation approach is developed to estimate state of linear
systems with disturbance. An extended dynamic observer (EDO) is designed, in terms of both the
prior information and the online measurement information, to estimate both the disturbance and
the system state simultaneously. The EDO takes almost all advantages from ESO and observer-
based IMP. More speciﬁcally, it possesses strong robustness to the system and disturbance, as the
ESO in ADRC, and at the same time, it proposes a feasible way to maximum utilize the prior infor-
mation of the disturbance and the control plant. When there is no information about disturbance
dynamics, the EDO is reduced automatically to an extension of ESO in ADRC which has been
applied successfully to many engineering problems. Hence, the proposed EDO is quite general and
can cover the high-gain observer and the IMP-based observer as special cases. Comparing with the
21

## Page 23

existing approaches such as ADRC and IMP, the proposed approach can improve the performance
with relatively small tuning gain when the disturbance contains high-frequency signal. Therefore,
the EDO makes up for the defects of the high-gain observer and the IMP-based observer. Since
both of them have diﬀerent structures, the design of EDO is our main contribution.
We just present a fundamental principle for the observer design. The technical tunings such as
shaping the transient response are still required in engineering applications. From the theoretical
point of view, this paper gives a systematic way to utilize the prior disturbance dynamics. The
future works are the online computations of the disturbance dynamics by the measurements.
References
[1] L.C. Evans, Partial diﬀerential equations, Vol. 19 of Graduate studies in mathematics, American
mathematical society, 1997.
[2] H. Feng and Y. Qian, A linear diﬀerentiator based on the extended dynamics approach, IEEE
Transactions on Automatic Control, to in press. 10.1109/TAC.2022.3183960.
[3] L.B. Freidovich and H.K. Khalil, Performance recovery of feedback-linearization-based designs,
IEEE Trans. Automat. Control, 53(2008), 2324-2334.
[4] Z. Gao, Scaling and bandwith-parameterization based controller tuning, American Control Con-
ference, 2003, 4989-4996.
[5] B.Z. Guo and Z.L.Zhao, On the convergence of extended state observer for nonlinear systems
with uncertainty, Systems Control Lett., 60(2011), 420-430.
[6] B.Z. Guo and Z.L. Zhao, Active Disturbance Rejection Control for Nonlinear Systems: An
Introduction, John Wiley & Sons Inc., New York, 2016.
[7] J. Han, From PID to Active Disturbance Rejection Control, IEEE Trans. Ind. Electron.,
56(2009), 900-906.
[8] M. Hou and P.C. Muller, Design of observers for linear systems with unknown inputs, IEEE
Tans. Automat. Contr., vol. 37, pp. 871-874, 1992.
[9] J. Huang, Nonlinear Output Regulation: Theory and Applications, SIAM, Philadelphia, 2004.
[10] L. Liu, Z. Chen and J. Huang, Parameter convergence and minimal internal model with an
adaptive output regulation problem. Automatica, (2009)45, 1306-1311.
[11] R. Marino and P. Tomei, Disturbance cancellation for linear systems by adaptive internal
model, Automatica, 49(2013), 1494-1500.
[12] R. Marino and P. Tomei, Hybrid adaptive muti-sinusoidal disturbance cancellation, IEEE
Trans. Automat. Control, 62(2017), 4023-4030.
22

## Page 24

[13] V. Natarajan, D.S. Gilliam, and G. Weiss. The state feedback regulator problem for regular
linear systems, IEEE Trans. Automat. Control, 59(2014), 2708-2723.
[14] I.R. Petersen and C. V. Hollot, High gain observers applied to problems in the stabilization of
uncertain linear systems, disturbance attenuation and N∞optimiration, Int. J. Adapt. Conlrol
Signal Proc., 2(1988), 347-369.
[15] S.K. Spurgeon, Sliding mode observers: a survey, International Journal of Systems Science,
39(2008), 751-764.
[16] S. Shao and Z. Gao, On the conditions of exponential stability in active disturbance rejection
control based on singular perturbation analysis, Internat. J. Control, 90(2017), 2085-2097.
[17] M. Tucsnak and G. Weiss, Observation and Control for Operator Semigroups, Birkh¨auser,
Basel, 2009.
[18] J. Trumpf, H.L. Trentelman and J.C. Willems, Internal model principles for observers, IEEE
Trans. Automat. Control, 59(2014), 1737-1749.
[19] Y. Wu, A. Isidori, R.Lu, H. Khalil, Performance recovery of dynamic feedback-linearization
methods for multivariable nonlinear systems, IEEE Trans. Automat. Control, 65(2020), 1365-
1380.
[20] Y. Xiong and M. Saif, Sliding mode observer for nonlinear uncertain systems, IEEE Trans.
Autom. Control, 46(2001), 2012-2017.
[21] F. Yang and R.W. Wilde, Observers for linear systems with unknown inputs, IEEE Trans.
Autom. Control, 33(1988), 677-681.
[22] G.Q. Zhang and Y.Q. Lin, Lectures on Functgional Analysis, Beijing University Press, 1997
(in Chinese).
23
View publication stats
