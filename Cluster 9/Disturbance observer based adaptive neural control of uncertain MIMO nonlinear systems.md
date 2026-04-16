# Disturbance observer based adaptive neural control of uncertain MIMO nonlinear systems.pdf

## Page 1

Communicated by Dr. Yuan Yuan
Accepted Manuscript
Disturbance observer based adaptive neural control of uncertain
MIMO nonlinear systems with unmodeled dynamics
Xinjun Wang, Xinghui Yin, Qinghui Wu, Fanqi Meng
PII:
S0925-2312(18)30767-7
DOI:
10.1016/j.neucom.2018.06.031
Reference:
NEUCOM 19709
To appear in:
Neurocomputing
Received date:
24 January 2018
Revised date:
17 May 2018
Accepted date:
20 June 2018
Please cite this article as: Xinjun Wang, Xinghui Yin, Qinghui Wu, Fanqi Meng, Disturbance observer
based adaptive neural control of uncertain MIMO nonlinear systems with unmodeled dynamics, Neu-
rocomputing (2018), doi: 10.1016/j.neucom.2018.06.031
This is a PDF ﬁle of an unedited manuscript that has been accepted for publication. As a service
to our customers we are providing this early version of the manuscript. The manuscript will undergo
copyediting, typesetting, and review of the resulting proof before it is published in its ﬁnal form. Please
note that during the production process errors may be discovered which could affect the content, and
all legal disclaimers that apply to the journal pertain.

## Page 2

ACCEPTED MANUSCRIPT
ACCEPTED MANUSCRIPT
Disturbance observer based adaptive neural control of uncertain MIMO nonlinear systems
with unmodeled dynamics
Xinjun Wanga,∗, Xinghui Yina, Qinghui Wub, Fanqi Menga,c
aCollege of Computer and Information, Hohai University, Nanjing 211100, China
bCollege of Engineering, Bohai University, Jinzhou 121013, China
cCollege of Mathematics and Statistics, Yancheng Teachers University, Yancheng 224002, China
Abstract
This paper investigates the disturbance observer-based adaptive neural tracking control of a class of multiple-input multiple-output
(MIMO) systems in the presence of unmodeled dynamics, system uncertainties, time varying disturbance and input dead-zone. An
adaptive neural control method combined with backstepping technique and the radial basis function neural networks (RBFNNs) is
proposed for the systems under consideration. In recursive backstepping designs, neural network (NN) is employed for uncertainty
approximation. The disturbance observer is developed to provide eﬃcient learning of the compounded disturbance which includes
the eﬀect of time varying disturbance, neural network approximation error. It is shown that by using Lyapunov methods, the
developed control scheme can ensure semi-globally uniformly ultimately bounded (SGUUB) of all signals within the closed-loop
systems. Simulation results are presented to illustrate the validity of the approach. This paper is novel at least in the two aspects: (1)
disturbance observer based tracking control method is developed for MIMO nonlinear systems with unmodeled dynamics and (2)
the strong coupled terms is considered in this paper where the interconnections are functions of all states, which is a more general
form than existing related results.
Keywords: Adaptive backstepping control, Disturbance observer, Unmodeled dynamics, Input dead-zone, Radial basis function
neural networks(RBFNNs)
1. Introduction
The problem of nonlinear is commonly resides in almost
all real systems since many systems cannot be simpliﬁed into
a linear model. Therefore, tremendous attention has paid on
the control design of nonlinear systems during the past few
decades.
A variety of remarkable control approaches have
been presented in the literature, including adaptive control[1–
3], fuzzy control [4–6], fault tolerant control [7, 8] and intelli-
gent control [9–11]. Among them, the adaptive backstepping
technique as an eﬀective control approach has undergone rapid
development and played an important role in the control of non-
linear systems [1–3]. For a class of complex nonlinear systems
with unknown functions, many control schemes were explored
by combining adaptive control and functional approximators.
It is konwn that neural networks and fuzzy-logic systems are
proved to be eﬀective approaches for controlling the highly un-
certain nonlinear systems [12–23]. In general, neural networks
or fuzzy systems are employed to estimate uncertain continuous
nonlinear functions, to list a few, in [24, 25], the adaptive con-
trol based neural networks was developed for nonlinear systems
with unknown virtual control coeﬃcient functions.
In [26],
an eﬀective neural network control is developed for Bimanual
∗Corresponding author
Email addresses: wangxinjun1991@gmail.com (Xinjun Wang ),
xhyin@hhu.edu.cn (Xinghui Yin ), wqh_bhu@163.com (Qinghui Wu ),
fqmeng@hhu.edu.cn (Fanqi Meng )
Robots systems with unknown uncertainties. In [20, 27], the
research is extended to multiinput multioutput (MIMO) nonlin-
ear systems. Alternatively, many researchers have been actively
working on the fuzzy systems-based control design of uncertain
nonlinear systems containing unknown functions [4, 28–31].
Input dead-zone problem exists in many real systems, their
existences frequently deteriorates control performances and
even result in the instability of the system. Therefore, the con-
sideration on the control of nonlinear systems aﬀected by input
dead-zone has accepted increasing attention, and a variety of ef-
fective control methods have been proposed in [32–36]. In [33],
the robust adaptive control is presented for a class of uncertain
pure-feedback nonlinear systems with actuator dead-zones by
using fuzzy methods. A class of nonlinear uncertain systems
with dead-zone has been solved in the work [34], and the ba-
sic idea was to treat dead-zone as disturbance in a same way.
Moreover, the author in [35] solved the chattering problems by
proposing a smooth adaptive dead-zone inverse algorithm and
a diﬀerent adaptive compensation scheme for unknown dead-
zone is derived in [36]. However, it is observed that the unmod-
eled dynamics is not seriously considered based on the afore-
mentioned results.
On the other hand, the unmodeled dynamics and unknown
external disturbance often exist in actual engineering, since
the practical systems are almost impossible to describe precise
mathematical models. Therefore, the consideration on the con-
trol of nonlinear systems with unmodeled dynamics has gained
1

## Page 3

ACCEPTED MANUSCRIPT
ACCEPTED MANUSCRIPT
increasing attention, and a great number of valuable control al-
gorithms have been presented in [22, 23, 37–41]. In [22], an
adaptive neural output-feedback control method was presented
for a class of nonlower triangular nonlinear systems with un-
modeled dynamics. In [23], an adaptive neural tracking con-
trol problem was considered for a class of nonlower triangular
nonlinear systems with unmodeled dynamics. By introducing
modiﬁed dynamic signal, the authors in [39] proposed the ro-
bust adaptive control to deal with the unmodeled dynamics. In
[42], an adaptive decentralized control method was proposed
for strong interconnected nonlinear systems with unmodeled
dynamics using backstepping technique. Recently, the corre-
sponding researches have been extended to interconnected non-
linear systems with unmodeled dynamics. The work in [41, 43]
proposed a fuzzy decentralized control approach based observer
for interconnected systems with unmodeled dynamics. How-
ever, the interconnection terms in [41, 43] are only the func-
tions of each subsystem, cannot be practical. Therefore, it is
a meaningful research topic to design an adaptive backstep-
ping control approach for nonlinear systems with unmodeled
dynamics where the interconnection terms are functions of all
states. Meanwhile, some signiﬁcant achievements focusing on
problems of external disturbances have also been reported in
the literature [44–49]. In [44], the disturbance observer based
sliding model control is designed for vehicular radar system. In
[45], disturbance observer based adaptive output feedback con-
trol is proposed for strict-feedback systems with time-varying
disturbance. In [46], the the optimal control problem is in-
vestigated based the disturbance-observer for a class of delta-
domain networked control systems. In [48], the dynamic sur-
face design with disturbance observer is provided for the trans-
port aircraft. In [49], the composite control problem is consid-
ered based the disturbance-observer for a class of delta domain
linear quadratic game with both matched and unmatched dis-
turbances. As a matter of fact, many control issues of MIMO
uncertain nonlinear systems are still a challenging task, and en-
hance the design diﬃculty due to the existence of input dead-
zone, unmodeled dynamics, system uncertainty, and external
unknown disturbances, which needs to be further studied.
With the statements above, in this paper, the disturbance
observer-based adaptive neural tracking control is developed
for a class of MIMO systems in the presence of unmodeled
dynamics, system uncertainties, time varying disturbance and
input dead-zone. Compared with the existing results, the main
contributions are summarised as follows:
(1) Compared with the existing works on the control of non-
linear systems with unmodeled dynamics which mainly con-
sidered the stabilized control, e.g., [50, 51], while in this paper,
disturbance observer based tracking control method is devel-
oped for MIMO nonlinear systems with unmodeled dynamics,
(2) the strong coupled terms are considered in this paper where
the interconnections are functions of all states, which is in a
more general form than existing related results [41, 43], (3) the
coupler design between the RBFNNs and disturbance observer
is considered in this paper, which improves the functional ap-
proximation capability and disturbance compensation ability by
comparing with the existing works [44].
The rest of the paper is organised as follows: The dynamic
model of n-order uncertain nonlinear systems with input dead-
zone is presented in Section 2.
An adaptive RBFNN con-
trol strategy combined disturbance observer with backstepping
method is presented in Section 3. Simulation results are pro-
vided in Section 4. Section 5 presents the conclusions of this
paper.
2. Problem formulation and preliminaries
Consider a class of nonlinear MIMO continuous time strict-
feedback systems with subsystems subject to unknown dead-
zone described by the following diﬀerential equations:

˙zi = qi(zi, xi),
˙xi j = gi j(¯xi j)xi j+1 + fi j(X) + ∆i j(xi, zi, t) + di j(t),
˙xini = giniui(vi) + fini(X) + ∆ini(xi, zi, t) + dini(t),
yi = xi1,
(1)
where i = 1, 2, . . . , N;
j = 1, . . . , ni −1; xi
=
¯xini
=
[xi1, . . . , xini]T
∈Rni and X = [¯xT
1 , . . . , ¯xT
N]T stand for the
state of the ith subsystem and overall system, respectively,
¯xi j = [xi1, . . . , xi j]T ∈Rj; yi ∈R stands for the output in the
ith subsystem; zi is unmodeled dynamics; gi j(·) and fij(·) repre-
sent the unknown nonlinear functions; ∆i j(·) denotes the system
dynamic uncertainties; and ∆i j(·) and qi(·) are assumed to be
uncertain Lipschitz continuous functions; di j(t) stands for the
unknown external disturbance; ui ∈R is the control input in the
i-th subsystem, and the output of the unknown dead-zone which
is described by
ui = G(vi(t)) =

gr(vi),
if vi(t) ≥dr
0,
if dl ≤vi(t) ≤dr
gl(vi),
if vi(t) ≤dl
(2)
where vi is the input of dead zone, dr and dl are the unknown
constants, and dr > 0, dl < 0.
For uncertain MIMO nonlinear system (1) the objective of
this paper is to design an adaptive tracking controller such that
the output y tracks a target signal yr within a bounded error and
all the signals are bounded under the existence of system uncer-
tainties, input dead zone and unknown external disturbances.
According to the analysis in [35], the solution of the system
(2) can be transformed into
ui = G(vi(t)) = civi(t) + ιi(vi)
(3)
where ci is the positive constant, ιi(vi) is bounded and satisfying
|ιi(vi)| ≤¯ιi, ¯ιi is unknown positive constant.
Assumption 1. [45] The target signal and its time derivatives
up to the nth order are continuous and uniformly bounded.
There exists a positive constant Yi0 satisfy |yri(t)| ≤Yi0 for all
t ≥0, i = 1, . . . , N.
Assumption 2. [52] The unknown external disturbance Di(t) =
[di1(t), . . . , dini(t)]T is bounded and satisﬁes
di j(t)
 ≤ρi j, where
ρi j > 0 is unknown, i = 1, 2, . . . , N, j = 1, 2, . . . , ni.
2

## Page 4

ACCEPTED MANUSCRIPT
ACCEPTED MANUSCRIPT
Assumption 3. [4] The functions gij(·) are known, and there
exists a positive constant g0 satisfying
0 < g0 ≤
gij(·)
 < ∞
(4)
Assumption 4. [41, 53] For the dynamic uncertainties ∆i j,
there are unknown nonnegative smooth functions ϕij1(·) and
ϕi j2(·) which satisﬁes
∆ij
 ≤ϕij1(
(¯xij)
) + ϕi j2(|zi|)
(5)
Remark 1. Assumption 4 relaxes the restriction in the existing
results [41, 53], in which ϕij1(·) and ϕij2(·) are not required to
be known in this paper.
Deﬁnition 1. [53] If a continuous function ζ : [0, a) →[0, ∞)
is strictly increasing and ζ(0) = 0, then the function ζ is called
K function. If a = ∞and r →∞, ζ(r) →∞, then ζ is called
K∞function.
Assumption 5. [41, 51] The unmodeled dynamics in (1) is ex-
ponentially input-to-state practically stable (exp-ISpS); that is,
for the system ˙zi = q(zi, xi), there exists an exp-ISpS Lyapunov
function Vi(zi) such that
αi1(|zi|) ≤Vi(zi) ≤αi2(|zi|)
∂Vi(zi)
∂zi
qi(zi, xi) ≤−ciVi(zi) + µi(|xi|) + di
(6)
where αi1, αi2, and µi are of class K∞-functions and ci and di
are known positive constants.
Lemma 1. [38] If Vi is an exp-ISpS Lyapunov function for a
control system, then, for any constants ¯ci in (0, ci0), any initial
condition xi0 = xi0(0), and any function ¯µ(xi1) ≥µ(|xi1|), there
exists a ﬁnite time Ti0 = Ti0(¯ci, ri0, zi0), a nonnegative function
Di(t) deﬁned for all t ≥0, and a signal described by
˙ri = −¯ciri + ¯µi(|xi1|) + di, ri(0) = ri0,
(7)
such that Di(t) = 0 for all t ≥Ti0,
Vi(zi(t)) ≤ri(t) + Di(t)
(8)
for all t ≥0. Takes ¯µi(xi1) = x2
i1µi0(x2
i1), where ¯µi0(·) is a non-
negative smooth function, and µi0 is a nonnegative smooth func-
tion. The dynamical ri can be rewritten as
˙ri = −¯ciri + x2
i1µi0(x2
i1) + di, ri(0) = ri0
(9)
Lemma 2. [13] The following inequality holds for any ϵ > 0
and for any η ∈R
0 ≤|η| −ηtanh
η
ϵ

≤κϵ
(10)
where κ is a constant satisfying κ = e−(κ+1), i.e., κ ≈0.2785.
Lemma 3. [54] Consider the set Ωzi1 deﬁned by Ωzi1
:=
{zi1||zi1| < 0.8814τi}. Then, for any zi1 < Ωzi1, the inequality

1 −2tanh2(zi1/τi)

≤0 is satisﬁed.
Lemma 4. [14] The radial basis function has the following
form :
hi jq(Zi) = exp

−(Zi −µi jq)T(Zi −µi jq)
η2
i
, q = 1, . . . .li j
(11)
where ηi is the width of the Gaussian function, and µi jq =
[µi j1, µi j2, . . . , µi jlij]T is the center vector. A continuous nonlin-
ear function fi j(Zi) can be approximated by an ideal RBF neural
network on a compact set Zi ∈ΩZi ⊂Rq with the neural node
number li j > 1. For any ξi j > 0, the following inequality holds:
sup
Zi∈Ω
 fi j(Zi) −WT
i jHi j(Zi)
 ≤ξi j
(12)
where Hi j(Zi) = [hi j1(Zi), . . . , hi jli j(Zi)]T is the basis function
vector, Wi j = [wi j1, . . . , wi jli j]T is the ideal constant weight vec-
tor. In this paper, we directly estimate the norm of Wi j instead
of themselves, so the θi j can be expressed as
Wi j
2 = θi j , ˆθi j is
the estimate of θi j, ˜θi j = θi j −ˆθi j is the estimate error.
Remark 2. In general, it should be emphasized that the selec-
tion of the centers and widths of RBF has a great inﬂuence
on the performance of the designed controller. According to
[55, 56], (1) increasing the NN node number l will help to re-
duce the inherent NN approximation error ξ; (2) the centers µij
evenly cover the NN approximation domain; (3) the widths ηi
of RBFs are calculated by using the formula η =
√
2dmax/
√
l
where dmax is the maximal Euclid distance of the approxima-
tion domain. More details on selecting these parameters can be
found in [55, 56].
3. Adaptive control design via disturbance observer
An adaptive RBFNN control strategy combined disturbance
observer with backstepping method is presented in this section.
Firstly, the following change of coordinate is deﬁned:
Step 1: Firstly, the following change of coordinate is deﬁned
for the ﬁrst subsystem:
zi,1 = xi1 −yri
(13)
zi,2 = xi2 −αi1
(14)
Under the coordinate transformation (13) and (14), the time
derivative of zi1 is given by
˙zi1 =˙xi1 −˙yri
=gi1(αi1 + zi2) + fi1 + ∆i1
xi, zi, t + di1 −˙yri
(15)
Consider a Lyapunov function candidate as
Vi1 = 1
2z2
i1 + ri
λi0
+
1
2ri1
˜θ2
i1 + 1
2
˜D2
i1
(16)
where ri1 > 0 is a design parameter, ˜Di1 = Di1 −ˆDi1 is the
estimate error of disturbance. By Assumption 4 and Lemma 1,
3

## Page 5

ACCEPTED MANUSCRIPT
ACCEPTED MANUSCRIPT
the derivative of Vi1 is given by
˙Vi1 = zi1˙zi1 + 1
λi0
˙ri −1
ri1
˜θi1˙ˆθi1 + ˜Di1 ˙˜Di1
= zi1

gi1(αi1 + zi2) + fi1(X) + ∆i1 + di1 −˙yri

+ 1
λi0
˙ri −1
ri1
˜θi1˙ˆθi1 + ˜Di1 ˙˜Di1
≤zi1

gi1αi1 + gi1zi2 + fi1(X) + di1 −˙yri + x2
i1µ0(x2
i1)
λi0zi1

+ |zi1| |∆i1| + di0
λi0
−¯ci
λi0
ri −1
ri1
˜θi1˙ˆθi1 + ˜Di1 ˙˜Di1
≤zi1

gi1αi1 + gi1zi2 + fi1(X) + di1 −˙yri + x2
i1µ0(x2
i1)
λi0zi1

+ |zi1| ϕi11(|xi1|) + |zi1| ϕi12(|zi|) + di0
λi0
−¯ci
λi0
ri
−1
ri1
˜θi1˙ˆθi1 + ˜Di1 ˙˜Di1
(17)
By using Lemma 2, the following inequality holds:
|zi1| ϕi11(|xi1|) ≤zi1ϕi11(|xi1|)tanh
 zi1ϕi11(|xi1|)
ϵi11
!
+ ϵ′
i11
≤zi1 ˆϕi11(xi1) + ϵ′
i11
(18)
where ˆϕi11(xi1) = ϕi11(|xi1|)tanh
 zi1ϕi11(|xi1|)
ϵi11

is a smooth func-
tion.
Similar to the derivations in [38], we have
|zi1| ϕi12(|zi|) ≤|zi1| ϕi12 ◦α−1
1 (2ri) + 1
4z2
i1 + hi1(t)
≤|zi1| ¯ϕi12(ri) + 1
4z2
i1 + hi1(t)
≤zi1 ¯ϕi12(ri)tanh
 zi1 ¯ϕ12(ri)
ϵi12
!
+ ϵ′
i12 + 1
4z2
i1 + hi1(t)
≤zi1 ˆϕi12(ri) + ϵ′
i12 + 1
4z2
i1 + hi1(t)
(19)
where ϕi12 ◦α−1
i1 (2ri) = ϕi12[α−1
i1 (2ri)], ¯ϕi12(ri) = ϕi12 ◦α−1
i1 (2ri),
ˆϕi12(ri) = ¯ϕi12(ri)tanh
 zi1 ¯ϕi12(ri)
ϵi12

, hi1(t) = (ϕi12 ◦α−1
i1 (2Di(t)))2,
ϕi12 ◦α−1
i1 (2Di(t)) = ϕi12[α−1
i1 (2Di(t))] are smooth function.
Since the term
x2
i1µ0(x2
i1)
λi0zi1
in (17) is discontinuous at zi1 = 0, we
introduce a hyperbolic tangent function tanh2  zi1
τi

, and substi-
tuting (18) and (19) into (17) results in
˙V1 ≤zi1

gi1αi1 + gi1zi2 + ˆfi1(Zi1)

+ zi1di1 + di0
λi0
−¯ci
λi0
ri
+
 
1 −2tanh2
 zi1
τi
!! x2
i1µ0(x2
i1)
λi0
−1
ri1
˜θi1˙ˆθi1
+ ˜Di1 ˙˜Di1 +
2
X
k=1
ϵ′
i1k + hi1(t)
(20)
where τi is a given positive constant and unknown nonlinear
function ˆfi1(Zi1) deﬁned as
ˆfi1(Zi1) = fi1(X) −˙yri + ˆϕi11(xi1) + ˆϕi12(ri) + 1
4zi1
+ 2
zi1
tanh2
 zi1
τi
! x2
i1µi0(x2
i1)
λi0
,
Zi1 = [xi1, r]T ∈ΩZi1 ⊂R2.
(21)
Additionally, the remaining term

1 −2tanh2  zi1
τi
 x2
i1µ0(x2
i1)
λi0
in
(20) will be dealt with at the end of this section. By employing
an RBFNN WT
i1Hi1(Zi1) to approximate ˆfi1(Zi1), the following
equation can be obtained
ˆfi1(Zi1) = WT
i1Hi1(Zi1) + ξi1
(22)
where ξi1 is the approximation error. Since there exists RBFNN
approximation errors to be suppressed, and external time-
varying disturbance to be compensated, we need to design a
disturbance observer.
Then, deﬁne the disturbance observer
variable as
Di1 = di1 + ξi1
(23)
Considering Assumption 2 and the RBFNN approximation the-
ory, we have
 ˙Di1
 ≤ρi1, where ρi1 > 0 is an unknown con-
stant. Deﬁne the auxiliary variable as
Ξi1 = Di1 −ci1zi1
(24)
By using (24), we can obtain the estimate of disturbance Di1 as
follows:
ˆDi1 = ˆΞi1 + ci1zi1
(25)
The following equation is proposed based on (24) to estimate
Ξi1:
˙ˆΞi1 = −ci1
ˆθi1HT
i1Hi1 + zi2 + αi1 + ˆDi1

(26)
Calculating the derivative of the estimate error of disturbance
˜Di1 as follows:
˙˜Di1 = ˙Di1 −ci1
 ˜Di1 −˜θi1HT
i1Hi1

(27)
Then, the virtual control input and adaption laws shall be de-
signed as
αi1 = g−1
i1
−ki1zi1 −zi1
2γ2
i1
ˆθi1HT
i1Hi1 −ˆDi1 −zi1
2 + ˙yri

(28)
˙ˆθi1 = ri1

1
2γ2
i1
HT
i1Hi1z2
i1 −σi1ˆθi1

(29)
4

## Page 6

ACCEPTED MANUSCRIPT
ACCEPTED MANUSCRIPT
where σi1 is the positive design parameters. Substituting (21)-
(29) in to (20) results in
˙Vi1 ≤−ki1z2
i1 + σi1˜θi1ˆθi1
|   {z   }
I
+gi1zi1zi2
+ zi1 ˜Di1 + ˜Di1 ˙Di1 + ci1 ˜Di1˜θi1HT
i1Hi1
|                                       {z                                       }
II
−ci1 ˜D2
i1
+
 
1 −2tanh2
 zi1
τi
!! x2
i1µ0(x2
i1)
λi0
+ di0
λi0
−¯ci
λi0
ri
+
2
X
k=1
ϵ′
i1k + hi1(t) + γ2
i1
2 −z2
i1
2
(30)
The following inequalities hold
(I) :σi1˜θi1ˆθi1 ≤−σi1˜θ2
i1
2
+ σi1θ2
i1
2
(31)
(II) :zi1 ˜Di1 ≤z2
i1
2 +
˜D2
i1
2
˜Di1 ˙Di1 ≤
˜D2
i1
2
+ ρ2
i1
2
ci1 ˜Di1˜θi1HT
i1Hi1 ≤
˜D2
i1
2
+ µ2
i1c2
i1˜θ2
i1
2
(32)
Based on (31) and (32), Eq. (30) satisﬁes the following inequal-
ity
˙Vi1 ≤−ki1z2
i1 −σi1 −µ2
i1c2
i1
2
˜θ2
i1 + gi1zi1zi2 −(ci1 −1.5) ˜D2
i1
+
 
1 −2tanh2
 zi1
τi
!! x2
i1µ0(x2
i1)
λi0
+ di0
λi0
−¯ci
λi0
ri
+
2
X
k=1
ϵ′
i1k + hi1(t) + ρ2
i1
2 + γ2
i1
2 + σi1θ2
i1
2
(33)
Step j ( j = 2, . . . , ni −1) : The following change of coordi-
nate is deﬁned:
zi j = xi j −αi(j−1), j = 2, . . . , ni −1
(34)
Consider a Lyapnov function candidate as
Vi j = 1
2z2
ij +
1
2rij
˜θ2
ij + 1
2
˜D2
i j
(35)
Diﬀerentiating (35) results in
˙Vi j = zij

gij(αij + zi( j+1)) + fi j(X) + ∆ij + dij −˙αi(j−1)

−1
rij
˜θij˙ˆθi j + ˜Di j ˙˜Dij
(36)
where
˙αi( j−1) =
j−1
X
k=1
(∂αi( j−1)
∂xik

gikxi,(k+1) + fik(X) + ∆ik + dik
)
+
j−1
X
k=1
∂αi(j−1)
∂ˆθik
˙ˆθik + ∂αi( j−1)
∂ri
˙ri
(37)
Then, ˙Vi j can be rewritten as
˙Vi j ≤zi j

gi j(αi j + zi( j+1)) −
j−1
X
k=1
∂αi,( j−1)
∂xik
gikxi,(k+1) + fij(X)
−
j−1
X
k=1
∂αi(j−1)
∂xik
fik(X) −
j−1
X
k=1
∂αi( j−1)
∂xik
dik
+
j−1
X
k=1
∂αi(j−1)
∂ˆθik
˙ˆθik + ∂αi( j−1)
∂ri
˙ri

+
zi j ¯∆i j
 + zi jdi j
−1
ri j
˜θi j˙ˆθi j + ˜Di j ˙˜Di j
(38)
where ¯∆i j = ∆i j −P j−1
k=1
∂αi( j−1)
∂xik ∆ik.
By using the similar estimation methods in Step 1, one has
zi j ¯∆i j
 ≤
zi j


∆i j
 +
j−1
X
k=1

∂αi,(j−1)
∂xik
 |∆ik|

≤
zi j

ϕi j1(¯xi j) +
j−1
X
k=1

∂αi(j−1)
∂xik
 ϕik1(¯xi j)

+
zi j

ϕi j2(|zi|) +
j−1
X
k=1

∂αi( j−1)
∂xik
 ϕik2(|zi|)

(39)
Similar to (18) and (19), we can obtain
zi j

ϕi j1

¯xi j

+
j−1
X
k=1

∂αi( j−1)
∂xik
 ϕik1(¯xi j)

≤zi j ˆϕi j1

¯xi j

+ ϵ′
i j1
(40)
zi j

ϕi j2(|zi|) +
j−1
X
k=1

∂αi(j−1)
∂xik
 ϕik2(|zi|)

≤zi j ˆϕi j2

¯xi j, ri

+
z2
i j
4
1 +
j−1
X
k=1
 ∂αi(j−1)
∂xik
!2
+ ϵ′
i j2 + hi j(t)
(41)
where
ˆϕi j1

¯xi j

=

ϕi j1

¯xi j

+ P j−1
k=1

∂αi,( j−1)
∂xik
 ϕik1

¯xi j

tanh

zi j

ϕi j1 + P j−1
k=1
∂αi(j−1)/∂xik
 ϕi j1

/ϵi j1

,
ˆϕi j2

¯xi j, ri

=
¯ϕi j2

¯xi j, ri

tanh

zi j ¯ϕi j2

¯xi j, ri

/ϵi j2

,
¯ϕi j2

¯xi j, ri

=
ϕi j2 ◦α−1
i1 (2ri) + P j−1
k=1
∂αi(j−1)/∂xik
 ϕi j2 ◦α−1
i1 (2ri),
and
hi j(t) = P j
k=1(ϕi j2 ◦α−1
i1 (2Di(t)))2, noting that hi j(t) ≥0 for all
t ≥0. Substituting (40) and (41) into (38) yields
˙Vi j ≤zi j

gi j(αi j + zi( j+1)) + ˆfi j(Zi j)

+ zi jdi j
−1
ri j
˜θi j˙ˆθi j + ˜Di j ˙˜Di j +
2
X
k=1
ϵ′
i jk + hi j(t)
(42)
5

## Page 7

ACCEPTED MANUSCRIPT
ACCEPTED MANUSCRIPT
where
ˆfi j(Zi j) =fi j(X) −
j−1
X
k=1
∂αi,(j−1)
∂xik
gikxi,(k+1) −
j−1
X
k=1
∂αi,( j−1)
∂xik
fik(X)
−
j−1
X
k=1
∂αi(j−1)
∂xik
dik +
j−1
X
k=1
∂αi( j−1)
∂ˆθik
˙ˆθik + ∂αi(j−1)
∂ri
˙ri
+ ˆϕij1

¯xij

+ ˆϕij2

¯xij, ri

+
z2
ij
4
1 +
j−1
X
k=1
 ∂αi(j−1)
∂xik
!2
Zij = [¯xij, ¯ˆθi(j−1), r]T ∈ΩZi j ⊂R2 j.
(43)
By employing an RBFNN WT
i jHij(Zij) to approximate ˆfi j(Zi j),
the following equation can be obtained
ˆfi j(Zi j) = WT
ijHi j(Zij) + ξij
(44)
Deﬁne the following disturbance observer:

Di j = dij + ξij
ˆDi j = ˆΞij + cijzi j
˙ˆΞi j = −ci j
ˆθi jHT
ijHij + gij(zi( j+1) + αij) + ˆDi j

˙˜Di j = ˙Dij −cij
 ˜Dij −˜θi jHT
ijHij

(45)
where ˜Dij = Dij −ˆDij is the estimate error of disturbance,
˙Di j ≤ρij, ρij > 0 is an unknown constant, Ξij is the auxiliary
variable. Then, the virtual control input and adaption laws shall
be designed as
αij = g−1
ij
−kijzij −zij
2γ2
i j
ˆθijHT
ijHij −ˆDij −zij
2 + gi(j−1)zi(j−1)

(46)
˙ˆθi j = rij

1
2γ2
ij
HT
ijHijz2
ij −σijˆθij

(47)
Substituting (43)-(47) in to (42) results in
˙Vi j ≤−ki jz2
i j + σij˜θijˆθi j
|   {z   }
III
+gijzi jzi( j+1)
+ zij ˜Dij + ˜Di j ˙Di j + cij ˜Dij˜θi jHT
ijHij
|                                      {z                                      }
IV
−cij ˜D2
ij
+
2
X
k=1
ϵ′
ijk + hij(t) +
γ2
i j
2 −
z2
ij
2 −gi(j−1)zi(j−1)zij
(48)
Similar to (31) and (32), the following inequalities hold
(III) :σij˜θi jˆθi j ≤−
σij˜θ2
i j
2
+
σi jθ2
ij
2
(49)
(IV) :zij ˜Dij ≤
z2
ij
2 +
˜D2
ij
2
˜Dij ˙Dij ≤
˜D2
ij
2 +
ρ2
i j
2
cij ˜Dij˜θi jHT
ijHi j ≤
˜D2
i j
2 +
µ2
i jc2
ij˜θ2
ij
2
(50)
Based on (49) and (50), Eq. (48) satisﬁes the following inequal-
ity
˙Vi j ≤−ki jz2
i j −
σi j −µ2
i jc2
i j
2
˜θ2
i j −(ci j −1.5) ˜D2
i j
+ gi jzi jzi(j+1) +
2
X
k=1
ϵ′
i jk + hi j(t) +
ρ2
i j
2 +
γ2
i j
2
+
σi jθ2
i j
2
−gi(j−1)zi(j−1)zi j
(51)
Step ni: The actual control law vi is designed in ni step.
Based on the coordination transformation zini = xini −αi(ni−1),
the derivative of ˙zini is
˙zini = giniui(vi) + fini(X) + ∆ini + di j −˙αi(ni−1)
= ginicivi + giniιi(vi) + fini(X) + ∆ini + di j −˙αi(ni−1)
(52)
where ˙αi(ni−1) is deﬁned in (37) with j = ni. Choose a Lyapnov
function as
Vini = 1
2z2
ini +
ci
2rini
˜θ2
ini + 1
2
˜D2
ini
(53)
Then, the time derivative of Vini is
˙Vini ≤zini

ginicivi + giniιi(vi) −
ni−1
X
k=1
∂αi(ni−1)
∂xik
gikxi,(k+1)
+ fini(X) −
ni−1
X
k=1
∂αi(ni−1)
∂xik
fik(X) −
ni−1
X
k=1
∂αi(ni−1)
∂xik
dik
+
ni−1
X
k=1
∂αi(ni−1)
∂ˆθik
˙ˆθik + ∂αi(ni−1)
∂ri
˙ri

+
zini ¯∆ini
 + zinidini
−ci
rini
˜θini ˙ˆθini + ˜Dini ˙˜Dini
(54)
where ¯∆ini = ∆ini −Pni−1
k=1
∂αi(ni−1)
∂xik ∆ik.
Then, following the process from (39) to (42) outlined at step
j, we can obtain the results below.
zini ¯∆ini
 ≤zini ˆϕini1
¯xini
 + zinini ˆϕini2
¯xini, ri

+
z2
ini
4
1 +
ni−1
X
k=1
 ∂αi(ni−1)
∂xik
!2
+ ϵ′
ini1 + ϵ′
ini2 + hini(t)
(55)
where ˆϕini1
¯xini
, ˆϕini2
¯xini, ri
, hini(t) have been speciﬁed in (40)
and (41) with j = ni. Substituting (55) into (54) yields
˙Vini ≤zini

gini(αi j + zi(j+1)) + ˆfini(Zini)

+ zinidini
−1
rini
˜θini ˙ˆθini + ˜Dini ˙˜Dini +
2
X
k=1
ϵ′
inik + hini(t)
(56)
6

## Page 8

ACCEPTED MANUSCRIPT
ACCEPTED MANUSCRIPT
where
ˆfini(Zini) = fini(X) −
ni−1
X
k=1
∂αi(ni−1)
∂xik
gikxi(k+1) −
ni−1
X
k=1
∂αi(ni−1)
∂xik
fik(X)
−
ni−1
X
k=1
∂αi(ni−1)
∂xik
dik +
ni−1
X
k=1
∂αi(ni−1)
∂ˆθik
˙ˆθik + ∂αi( j−1)
∂ri
˙ri
+ ˆϕini1
¯xini
 + ˆϕini2
¯xini, ri
 +
z2
ini
4
1 +
ni−1
X
k=1
 ∂αi(ni−1)
∂xik
!2
Zini = [¯xini, ¯ˆθi(ni−1), r]T ∈ΩZini ⊂R2ni.
(57)
By employing an RBFNN WT
iniHini(Zini) to approximate
ˆfini(Zini), the following equation can be obtained
ˆfini(Zini) = WT
iniHini(Zini) + ξini
(58)
Deﬁne the following disturbance observer:

Dini = dini + ξini
ˆDini = ˆΞini + cinizini
˙ˆΞini = −cini
ˆθiniHT
iniHini + giniui + ˆDini

˙˜Dini = ˙Dini −cini
 ˜Dini −˜θiniHT
iniHini

(59)
where ˜Dini = Dini −ˆDini is the estimate error of disturbance,
˙Dini ≤ρini, ρini > 0 is an unknown constant, Ξini is the auxiliary
variable. Then, the virtual control input and adaption laws shall
be designed as
vi = g−1
ini

−kinizini −zini
2γ2
ini
ˆθiniHT
iniHini −c−1
i
ˆDini
−c−1
i zini + c−1
i gi(ni−1)zi(ni−1)

(60)
˙ˆθini = rini

1
2γ2
ini
HT
iniHiniz2
ini −σini ˆθini

(61)
Substituting (57)-(61) in to (56) results in
˙Vini ≤−kiniciz2
ini + ciσini ˜θini ˆθini
|        {z        }
V
+ zini ˜Dini + ˜Dini ˙Dini + cini ˜Dini ˜θiniHT
iniHini
|                                             {z                                             }
VI
−cini ˜D2
ini
+
2
X
k=1
ϵ′
inik + hini(t) +
γ2
ini
2 −z2
ini + ziniginiιi(vi)
|       {z       }
VII
−gi(ni−1)zi(ni−1)zini
(62)
Similar to (49) and (50), the following inequalities hold
(V) :ciσini ˜θini ˆθini ≤−
ciσini ˜θ2
ini
2
+
ciσiniθ2
ini
2
(63)
(VI) :zini ˜Dini ≤
z2
ini
2 +
˜D2
ini
2
˜Dini ˙Dini ≤
˜D2
ini
2
+
ρ2
ini
2
cini ˜Dini ˜θiniHT
iniHini ≤
˜D2
ini
2
+
µ2
inic2
ini ˜θ2
ini
2
(64)
(VII) :ziniginiιi(vi) ≤
z2
ini
2 + ¯gini¯ιi(vi)2
2
(65)
Based on (63)-(65), one has
˙Vini ≤−kiniciz2
ini −
ciσini −µ2
inic2
ini
2
˜θ2
ini −(cini −1.5) ˜D2
ini
+
2
X
k=1
ϵ′
inik + hini(t) +
ρ2
ini
2 +
γ2
ini
2
+
ciσiniθ2
ini
2
−gi(ni−1)zi(ni−1)zini + ¯gini¯ιi(vi)2
2
(66)
At current stage, a Lyapunov function is selected for the overall
systems as
V =
N
X
i=1
ni
X
j=1
Vi j
=
N
X
i=1
 ni
X
j=1
z2
i j
2 +
ni−1
X
j=1
˜θ2
i j
2ri j
+
ni
X
j=1
˜D2
i j
2 + ri
λi0
+
ci˜θ2
ini
2rini

(67)
By the inequalities (33), (51) and (66), we get
˙V ≤
N
X
i=1
(
−ki1z2
i1 −σi1 −µ2
i1c2
i1
2
˜θ2
i1 + gi1zi1zi2
−(ci1 −1.5) ˜D2
i1 +
 
1 −2tanh2
 zi1
τi
!! x2
i1µ0(x2
i1)
λi0
+ di0
λi0
−¯ci
λi0
ri +
2
X
k=1
ϵ′
i1k + hi1(t) + ρ2
i1
2 + γ2
i1
2 + σi1θ2
i1
2
)
+
N
X
i=1
ni−1
X
j=2
(
−ki jz2
i j −
σi j −µ2
i jc2
i j
2
˜θ2
i j −(ci j −1.5) ˜D2
i j
+ gi jzi jzi( j+1) +
2
X
k=1
ϵ′
i jk + hi j(t) +
ρ2
i j
2 +
γ2
i j
2
+
σi jθ2
i j
2
−gi(j−1)zi(j−1)zi j
)
+
N
X
i=1
(
−kiniciz2
ini
−
ciσini −µ2
inic2
ini
2
˜θ2
ini −(cini −1.5) ˜D2
ini
+
2
X
k=1
ϵ′
inik + hini(t) +
ρ2
ini
2 +
γ2
ini
2
+
σiniθ2
ini
2
−gi(ni−1)zi(ni−1)zini + ¯gini¯ιi(vi)2
2
)
(68)
7

## Page 9

ACCEPTED MANUSCRIPT
ACCEPTED MANUSCRIPT
Next, by rearranging the sequence, one has
˙V ≤
N
X
i=1
( ni−1
X
j=1
−ki jz2
ij −kiniciz2
ini −¯ci
λi0
ri −
ni−1
X
j=1
σi j −µ2
ijc2
i j
2
˜θ2
i j
−
ciσini −µ2
inic2
ini
2
˜θ2
ini −
ni
X
j=1
(cij −1.5) ˜D2
ij +
ni
X
j=1
S ij
+
 
1 −2tanh2
 zi1
τi
!! x2
i1µ0(x2
i1)
λi0
+ di0
λi0
+ ¯gini¯ιi(vi)2
2
)
(69)
Theorem 1. Consider the nonlinear system (1) with the con-
trollers (60) and adaptive update laws (29), (47), (61). The non-
linear disturbance observers are proposed as (25), (45), (59).
For 1 ≤i ≤N, 1 ≤j ≤ni, assume that all the unknown non-
linear functions ˆfi, j(Z) are approximated by neural networks in
the sense that the approximation error ξi,j is bounded. Then, for
bounded initial conditions, under the developed control laws
(60), all signals of the closed-loop system are bounded and the
target signal can be tracked within a small bounded error.
Proof. Let
ρ = min

2ki j, ¯ci, rij(σij −µ2
ijc2
ij), 2(cij −1.5), 2kinici,
rini(ciσini −µ2
inic2
ini), 1 ≤i ≤N, 1 ≤j ≤ni −1

(70)
and
ς0 =
N
X
i=1
ni
X
j=1
S ij + di0
λi0
+ ¯gini¯ιi(vi)2
2
(71)
such that (69) is rewritten as
˙V ≤−ρV + ς0
+
N
X
i=1
 
1 −2tanh2
 zi1
τi
!! x2
i1µ0(x2
i1)
λi0
, t ≥0.
(72)
It is noted that the last term

1 −2tanh2  zi1
τi
 x2
i1µ0(x2
i1)
λi0
in (72)
may be positive or negative which depends on the size of zi1.
Therefore, the following two cases should be considered based
(72).
Case 1: zi1 ∈Ωzi1 = {zi1||zi1| < 0.8814τi} for any positive
constant τi.
By using Assumption 4 and Lemma 1, µ0(x2
i1)
is a non-negative smooth function,

1 −2tanh2  zi1
τi
 x2
i1µ0(x2
i1)
λi0
is
bounded, there exists a positive constant µi0 > 0, such that

1 −2tanh2  zi1
τi
 x2
i1µ0(x2
i1)
λi0
≤µi0. From (72), we have
˙V ≤−ρV + b0
(73)
where b0 = ς0 + PN
i=1 µi0. Furthermore, (73) satisﬁes
V(t) ≤
 
V(0) −b0
ρ
!
e−ρt + b0
ρ , t ≥0.
(74)
Case 2: zi1 < Ωzi1. By using Lemma 3 and the fact that
x2
i1µi0(x2
i1)
λi0
≥0, we can obtain
 
1 −2tanh2
 zi1
τi
!! x2
i1µ0(x2
i1)
λi0
≤0
(75)
Therefore, (72) is simpliﬁed as
˙V ≤−ρV + ς0
(76)
Furthermore, (76) satisﬁes
V(t) ≤
 
V(0) −ς0
ρ
!
e−ρt + ς0
ρ , t ≥0.
(77)
Consider (74) and (77), we obtain
V(t) ≤
 
V(0) −b0
ρ
!
e−ρt + b0
ρ , t ≥0.
(78)
1) From (78), according to the boundedness theorem (e.g.,[57]),
we have that all zi and ˆθi(i = 1, . . . , n) are uniformly ultimately
bounded. Since zi1 = xi1 −yri and yri are bounded, we have that
xi1 is bounded. From zi j = xi j −αi( j−1), j = 1, . . . , ni, and the
virtual control laws (28), (46), we have that xi j, j = 2, . . . , ni
remain bounded. Using (60) we conclude that control vi is also
bounded. Thus, all the signals in the closed-loop system remain
bounded.
2) From (78), we have
N
X
i=1
1
2z2
i ≤
 
V(0) −b0
ρ
!
e−ρt + b0
ρ < V(0)e−ρt + b0
ρ
(79)
that is
N
X
i=1
z2
i < 2V(0)e−ρt + 2b0
ρ
(80)
In particular, we have
lim
t→∞|zi1| = lim
t→∞|yi(t) −yri(t)| ≤
s
2b0
ρ
(81)
which implies that the system output is ensured to converge to
a small bounded error. The proof is completed here.
Table 1
Initial values for example 1
x1,1(0) = 1
x1,2(0) = −1
x2,1(0) = 0.5
x2,2(0) = −0.5
ˆθ1,1(0) = 0.01
ˆθ1,2(0) = 0.1
ˆθ2,1(0) = 0.01
ˆθ2,2(0) = 0.1
α1,1 = 0.01
α1,2 = 0.02
α2,1 = 0.01
α2,2 = 0.02
8

## Page 10

ACCEPTED MANUSCRIPT
ACCEPTED MANUSCRIPT
Table 2
Controller parameters for example 1
k11 = 22
k12 = 40
k21 = 22
k22 = 40
c11 = 5
c12 = 5
c21 = 5
c22 = 5
γ11 = 8
γ12 = 10
γ21 = 8
γ22 = 10
σ11 = 0.02
σ12 = 0.03
σ21 = 0.02
σ22 = 0.03
r11 = 20
r12 = 50
r21 = 20
r22 = 45
Table 3
Initial values for example 2
x1,1(0) = 1
x1,2(0) = −1
x2,1(0) = 0.5
x2,2(0) = −0.5
x3,1(0) = 0.5
x3,2(0) = 1
ˆθ1,1(0) = 0.01
ˆθ1,2(0) = 0.1
ˆθ2,1(0) = 0.01
ˆθ2,2(0) = 0.1
ˆθ3,1(0) = 0.01
ˆθ3,2(0) = 0.1
α1,1 = 0.01
α1,2 = 0.02
α2,1 = 0.01
α2,2 = 0.02
α3,1 = 0.01
α3,2 = 0.02
4. Simulation studies
In this section, two simulation examples are presented to
show the eﬀectiveness of the developed method.
Example 1: Consider the following MIMO systems com-
posed of three subsystems with input dead-zone:

˙z1 = −z1 + x2
11 + 0.5
˙x11 = f11(·) + g11(·)x12 + d11(t)
˙x12 = f12(·) + g12(·)u1(v1) + d12(t)
˙z2 = −z2 + x2
21 + 0.5
˙x21 = f21(·) + g21(·)x22 + d21(t)
˙x22 = f22(·) + g22(·)u2(v2) + d22(t)
y1 = x11, y2 = x21
(82)
where the external disturbances are chosen as
D1(t) =
"0.2sin(t) + sin(1.5t)
0.1sin(t)
#
D2(t) =
"0.3sin(t) + sin(1.2t)
0.1sin(t)
#
(83)
where fi1(·) = 0, gi1(·) = 1, i = 1, 2, g12(·) = 1, f12(·) =
20sinx11 −8sinx11cosx11 + 8sinx21cos21, g22(·) = 0.7, f22(·) =
20sinx21 −10.6sinx21cosx21 + 5.3sinx11cosx11, ui, i = 1, 2, are
the actual inputs of the MIMO systems. The outputs of the
Table 4
Controller parameters for example 2
k11 = 17
k12 = 50
k21 = 25
k22 = 50
k31 = 26
k32 = 50
c11 = 3
c12 = 3
c21 = 0.05
c22 = 0.05
c31 = 0.01
c32 = 0.01
γ11 = 1
γ12 = 1
γ21 = 5
γ22 = 5
γ31 = 4
γ32 = 4
σ11 = 0.8
σ12 = 0.8
σ21 = 0.08
σ22 = 0.08
σ31 = 0.5
σ32 = 0.5
r11 = 8
r12 = 8
r21 = 8
r22 = 10
r31 = 10
r32 = 10
ρ11 = 20
ρ12 = 50
ρ21 = 20
ρ22 = 48
ρ31 = 18
ρ32 = 52
dead- zone actuators ui, i = 1, 2, are described as
ui = G(vi(t)) =

(1 −0.2sin(vi)(vi −1)), vi(t) ≥1
0, −0.5 ≤vi(t) ≤1
(0.8 −0.1cos(vi))(vi + 0.5), vi(t) ≤−0.5
(84)
The desired output is assumed to be

y1d = 0.5sin2πt
y2d = 0.8sinπt
(85)
The initial values and the design parameters are shown in Ta-
ble 1 and Table 2, respectively. Neural networks WT
i1Hi1(Zi1)
contains 11 nodes (i.e., li1=11), with centers Cl(l = 1, . . . , li1)
evenly spaced in [−10, 10] × [−10, 10], and widths bl = 1(l =
1, . . . , li1). Neural networks WT
i2Hi2(Zi2) contains 21 nodes (i.e.,
li2=21), with centers Cl(l = 1, . . . , li2) evenly spaced in [-
20,20]×[-20,20]×[-20,20]×[-20,20] and widths bl = 1.5(l =
1, . . . , li2).
The simulation ﬁgures are listed in Figs. 1-6. Fig. 1 demon-
strate that x11, x21 tracks their references eﬀectively and track-
ing errors are shown in Fig. 2. The control inputs u are shown in
Fig. 3. The disturbance estimate result is in Figs. 4-5. Figs. 4-
5 indicate that the proposed disturbance observer can estimate
external disturbance within a small bounded error. The adap-
tive parameters θi i = 1, 2 are shown in Fig. 6, respectively.
From the above-mentioned simulation ﬁgures, we can see that
the proposed approach in this paper provides good transient per-
formance and the tracking error is as good as desired, while all
the signals of the closed-loop system are bounded.
0
5
10
15
20
−1
0
1
2
time/s
x11, yr1
 
 
x11
yr1
0
5
10
15
20
−1
0
1
2
time/s
x21, yr2
 
 
x21
yr2
Fig. 1. Trajectories of the outputs xi1, the reference signals yri, i = 1, 2.
Example 2: Consider the model of three-axis ship-mounted
satellite tracking antenna systems [58]:

5.7¨q1 + 16.2˙q1 −5.7˙q2 ˙q3cosq2 + 7.2˙q3sinq2 = u1
38.6¨q2 + 33.1˙q2 + 5.2˙q1 ˙q3cosq2 + 25.4˙q2
3sinq2cosq2 = u2
54.7¨q3 + 78.3˙q3 −14.1˙q2 ˙q3sinq2cosq2 −1.4˙q1 ˙q2cosq2 = u3
(86)
where q = [q1, q2, q3]T are pitch, roll, and yaw angle respec-
tively, u denotes the control input. In addition, there always
9

## Page 11

ACCEPTED MANUSCRIPT
ACCEPTED MANUSCRIPT
0
5
10
15
20
−0.5
0
0.5
time/s
Tracking error
 
 
x11−yr1
0
5
10
15
20
−1
−0.5
0
0.5
time/s
Tracking error
 
 
x21−yr2
Fig. 2. The tracking errors xi1 −yri, i = 1, 2.
0
5
10
15
20
−20
−10
0
10
20
time/s
v1
 
 
v1
0
5
10
15
20
−20
−10
0
10
20
time/s
u1
 
 
u1
0
5
10
15
20
−10
−5
0
5
10
time/s
v2
 
 
v2
0
5
10
15
20
−100
−50
0
50
time/s
u2
 
 
u2
Fig. 3. Trajectories of the output ui and input vi, i = 1, 2 of dead-zone.
0
5
10
15
20
−5
0
5
10
time/s
Disturbance
 
 
ˆD 11
D 11
0
5
10
15
20
−20
−10
0
10
20
time/s
Disturbance
 
 
ˆD 12
D 12
0
5
10
15
20
−10
−5
0
5
time/s
Disturbance error
 
 
D 11 −ˆD11
0
5
10
15
20
−1
−0.5
0
0.5
1
time/s
Disturbance error
 
 
D 12 −ˆD12
Fig. 4. Disturbance estimate for D1 under the proposed control strat-
egy.
0
5
10
15
20
−2
0
2
4
time/s
Disturbance
 
 
ˆD 21
D 21
0
5
10
15
20
−20
−10
0
10
time/s
Disturbance
 
 
ˆD 22
D 22
0
5
10
15
20
−10
−5
0
5
time/s
Disturbance error
 
 
D 21 −ˆD21
0
5
10
15
20
−0.5
0
0.5
1
time/s
Disturbance error
 
 
D 22 −ˆD22
Fig. 5. Disturbance estimate for D2 under the proposed control strat-
egy.
0
5
10
15
20
0
0.1
0.2
0.3
0.4
time/s
ˆθ11
 
 
ˆθ11
0
5
10
15
20
0
5
10
15
time/s
ˆθ12
 
 
ˆθ12
0
5
10
15
20
0
0.02
0.04
0.06
0.08
0.1
time/s
ˆθ21
 
 
ˆθ21
0
5
10
15
20
0
2
4
6
8
10
time/s
ˆθ22
 
 
ˆθ22
Fig. 6. Trajectories of adaptive laws ˆθ1, ˆθ2.
0
5
10
15
20
−2
0
2
time/s
x11, yr1
 
 
x11
yr1
0
5
10
15
20
−1
0
1
time/s
x21, yr2
 
 
x21
yr2
0
5
10
15
20
−2
0
2
time/s
x31, yr3
 
 
x31
yr3
Fig. 7. Trajectories of the outputs xi1, the reference signals yri, i =
1, 2, 3 for Example 2.
0
5
10
15
20
−0.5
0
0.5
time/s
Tracking error
 
 
x11−yr1
0
5
10
15
20
−0.5
0
0.5
time/s
Tracking error
 
 
x21−yr2
0
5
10
15
20
−0.5
0
0.5
time/s
Tracking error
 
 
x31−yr3
Fig. 8. The tracking errors xi1 −yri, i = 1, 2, 3 for Example 2.
0
5
10
15
20
−100
0
100
time/s
v1
 
 
v1
0
5
10
15
20
−500
0
500
time/s
u1
 
 
u1
0
5
10
15
20
−50
0
50
time/s
v2
 
 
v2
0
5
10
15
20
−100
0
100
time/s
u2
 
 
u2
0
5
10
15
20
−10
0
10
time/s
v3
 
 
v3
0
5
10
15
20
−100
0
100
time/s
u3
 
 
u3
Fig. 9. Trajectories of the output ui and input vi, i = 1, 2, 3 of dead-
zone for Example 2.
10

## Page 12

ACCEPTED MANUSCRIPT
ACCEPTED MANUSCRIPT
0
5
10
15
20
−5
0
5
time/s
Disturbance
 
 
ˆD 11
D 11
0
5
10
15
20
−0.2
0
0.2
time/s
Disturbance
 
 
ˆD 12
D 12
0
5
10
15
20
−0.2
0
0.2
time/s
Disturbance
 
 
ˆD 21
D 21
0
5
10
15
20
−0.5
0
0.5
time/s
Disturbance
 
 
ˆD 22
D 22
0
5
10
15
20
−0.2
0
0.2
time/s
Disturbance
 
 
ˆD 31
D 31
0
5
10
15
20
−0.2
0
0.2
time/s
Disturbance
 
 
ˆD 32
D 32
Fig. 10. Disturbance estimate ˆD1, ˆD2, ˆD3 under the proposed control
strategy for Example 2.
0
5
10
15
20
−5
0
5
time/s
Disturbance error
 
 
D 11 −ˆD11
0
5
10
15
20
−0.2
0
0.2
time/s
Disturbance error
 
 
D 12 −ˆD12
0
5
10
15
20
−0.2
0
0.2
time/s
Disturbance error
 
 
D21 −ˆD21
0
5
10
15
20
−0.2
0
0.2
time/s
Disturbance error
 
 
D22 −ˆD22
0
5
10
15
20
−0.2
0
0.2
time/s
Disturbance error
 
 
D31 −ˆD31
0
5
10
15
20
−0.2
0
0.2
time/s
Disturbance error
 
 
D32 −ˆD32
Fig. 11. Disturbance estimate error under the proposed control strategy
for Example 2.
0
5
10
15
20
0
0.5
1
time/s
ˆθ11
 
 
ˆθ11
0
5
10
15
20
0
20
40
time/s
ˆθ12
 
 
ˆθ12
0
5
10
15
20
0
0.5
time/s
ˆθ21
 
 
ˆθ21
0
5
10
15
20
0
2
4
time/s
ˆθ22
 
 
ˆθ22
0
5
10
15
20
0
0.02
0.04
time/s
ˆθ31
 
 
ˆθ31
0
5
10
15
20
0
2
4
time/s
ˆθ32
 
 
ˆθ32
Fig. 12. Trajectories of adaptive laws ˆθ1, ˆθ2, ˆθ3 for Example 2.
0
5
10
15
20
−2
0
2
time/s
x11, yr1
 
 
x11
yr1
0
5
10
15
20
−1
0
1
time/s
x21, yr2
 
 
x21
yr2
0
5
10
15
20
−2
0
2
time/s
x31, yr3
 
 
x31
yr3
Fig. 13. Trajectory of xi1, yri, i = 1, 2, 3 using controller u∗in [44] for
Example 2.
0
5
10
15
20
−0.5
0
0.5
time/s
Tracking error
 
 
x11−yr1
0
5
10
15
20
−0.5
0
0.5
time/s
Tracking error
 
 
x21−yr2
0
5
10
15
20
−0.5
0
0.5
time/s
Tracking error
 
 
x31−yr3
Fig. 14. The tracking errors xi1 −yri, i = 1, 2, 3 using controller u∗in
[44] for Example 2.
exists external time-varying disturbances and system uncertain-
ties. The unknown input dead-zone in actuator is another prob-
lem which may be encountered, all of these factors bring out
model uncertainties and diﬃculties in control of ship-mounted
satellite tracking system.
In order to evaluate the proposed
method, we must ﬁrst change the ship-mounted satellite model
(86) into the shape of (1), that is

˙z1 = −z1 + 0.5x2
11 + 0.5
˙x11 = x12
˙x12 = x22x32cosx21 −2.84x12 −1.26x32sinx21 + 0.18u1
˙z2 = −z2 + 0.5x2
21 + 0.5
˙x21 = x22
˙x22 = −0.86x22 −0.13x12x32cosx21 −0.33x2
32sin2x21 + 0.03u2
˙z3 = −z3 + 0.5x2
31 + 0.5
˙x31 = x32
˙x32 = 0.13x22x32sin2x21 + 0.03x12x22cosx21 −1.43x32 + 0.02u3
y1 = x11, y2 = x21, y3 = x31
(87)
where x1 = [q1, ˙q1]T, x2 = [q2, ˙q2]T, x3 = [q3, ˙q3]T and the
external disturbances are chosen as
D1(t) =
"0.2sin(t) + sin(1.5t)
0.1sin(t)
#
D2(t) =
"0.1sin(0.01t) + 0.2cos(0.01t)
0.13sin(t) + 0.05sin(0.2t)
#
D3(t) =
"0.11cos(t) + 0.21sin(0.3t)
0.12sin(t) + 0.03sin(0.2t)
#
(88)
We choose the desired output

y1d = 0.3sin(t) + sin(1.5t)
y2d = 0.2sin(t) + sin(1.2t)
y3d = sinπt + cosπt
(89)
The initial values and the design parameters are shown in Table
3 and Table 4, respectively. The simulation ﬁgures are listed
in Figs. 7-12. Fig. 7 demonstrates that x11, x21, x31 tracks
their references eﬀectively and tracking errors are shown in Fig.
11

## Page 13

ACCEPTED MANUSCRIPT
ACCEPTED MANUSCRIPT
8. The control inputs u are shown in Fig. 9. The disturbance
estimate result is in Fig. 10. Fig. 11 indicates that the proposed
disturbance observer can estimate external disturbance within
a small bounded error. The adaptive parameters θi, i = 1, 2, 3
is shown in Fig. 12. In addition, the adaptive sliding model
controller u∗developed in [44] is applied to further show the
advantage of the control scheme proposed in this paper. The
simulation results are shown in Fig. 13 and 14, from Fig. 13
it can be seen that the tracking performance is very poor and
Fig. 14 indicates that our method can ensure the target signal
be tracked within a small bounded error.
5. Conclusion
In this paper, disturbance observer-based adaptive neural
tracking control is proposed for a class of multiple-input
multiple-output systems in the presence of unmodeled dynam-
ics, system uncertainties, time varying disturbance and input
dead-zone. The theory analysis and simulation results indicate
that the target signal can be converged to a small bounded er-
ror. In the future researches, we will present a control algorithm
for system (1) with both state and input constraints, and pay at-
tention to more complex systems such as stochastic time-delay
nonlinear systems.
6. Acknowledgment
This work was supported partially by the National Science
Foundation of China under Grant U1531101, and the Post-
graduate Research & Practice Innovation Program of Jiangsu
Province.
References
[1] I. Kanellakopoulos, P. V. Kokotovi, A. S. Morse, Systematic design of
adaptive controllers for feedback linearizable systems, IEEE Transactions
on Automatic Control 36 (1990) 1241–1253.
[2] M. Krsti, I. Kanellakopoulos, P. V. Kokotovi, Adaptive nonlinear control
without overparametrization, Systems & Control Letters 19 (1992) 177–
185.
[3] M. D. Bernardo, U. Montanaro, R. Ortega, S. Santini, Extended hybrid
model reference adaptive control of piecewise aﬃne systems, Nonlinear
Analysis Hybrid Systems 21 (2016) 11–21.
[4] B. Chen, X. Liu, K. Liu, C. Lin, Direct adaptive fuzzy control of nonlinear
strict-feedback systems, Automatica 45 (2009) 1530–1535.
[5] X. Su, P. Shi, L. Wu, Y. D. Song, A novel control design on discrete-time
takagisugeno fuzzy systems with time-varying delays, IEEE Transactions
on Fuzzy Systems 21 (2013) 655–671.
[6] Y. Li, S. Tong, T. Li, Composite adaptive fuzzy output feedback control
design for uncertain nonlinear strict-feedback systems with input satura-
tion., IEEE Transactions on Cybernetics 45 (2015) 2299.
[7] H. Li, H. Gao, P. Shi, X. Zhao, Fault-tolerant control of markovian jump
stochastic systems via the augmented sliding mode observer approach ,
Automatica 50 (2014) 1825–1834.
[8] S. Yin, X. Yang, H. R. Karimi, Data-driven adaptive observer for fault di-
agnosis, Mathematical Problems in Engineering,2012,(2012-10-24) 2012
(2012) 1094–1099.
[9] L. X. Wang, J. M. Mendel, Fuzzy basis functions, universal approxima-
tion, and orthogonal least-squares learning., IEEE Trans Neural Netw 3
(1992) 807–814.
[10] C. F. Hsu, Y. C. Chen, Microcontroller-based b-spline neural position
control for voice coil motors, IEEE Transactions on Industrial Electronics
62 (2015) 5644–5654.
[11] C. Yang, K. Huang, H. Cheng, Y. Li, C. Y. Su,
Haptic identiﬁcation
by elm-controlled uncertain manipulator, IEEE Transactions on Systems
Man & Cybernetics Systems PP (2017) 1–12.
[12] X. Wang, X. Yin, F. Shen, Robust adaptive neural tracking control for a
class of nonlinear systems with unmodeled dynamics using disturbance
observer, Neurocomputing 292 (2018) 49–62.
[13] M. M. Polycarpou, Stable adaptive neural control scheme for nonlinear
systems, Automatic Control IEEE Transactions on 41 (1996) 447–451.
[14] S. C. Tong, Y. M. Li, H. G. Zhang, Adaptive neural network decentral-
ized backstepping output-feedback control for nonlinear large-scale sys-
tems with time delays., IEEE Transactions on Neural Networks 22 (2011)
1073–1086.
[15] T. Wang, Y. Zhang, J. Qiu, H. Gao, Adaptive fuzzy backstepping control
for a class of nonlinear systems with sampled and delayed measurements,
IEEE Transactions on Fuzzy Systems 23 (2015) 302–312.
[16] M. Wang, X. Liu, S. Peng, Adaptive neural control of pure-feedback non-
linear time-delay systems via dynamic surface technique, IEEE Transac-
tions on Systems Man & Cybernetics Part B Cybernetics A Publication
of the IEEE Systems Man & Cybernetics Society 41 (2011) 1681–92.
[17] X. Wang, X. Yin, F. Shen, Disturbance observer based adaptive neural
prescribed performance control for a class of uncertain nonlinear systems
with unknown backlash-like hysteresis, Neurocomputing 299 (2018) 10–
19.
[18] S. S. Ge, C. Wang, Adaptive neural control of uncertain mimo nonlinear
systems, IEEE Transactions on Neural Networks 15 (2004) 674–692.
[19] B. Chen, K. Liu, X. Liu, P. Shi, C. Lin, H. Zhang, Approximation-based
adaptive neural control design for a class of nonlinear systems, IEEE
Transactions on Cybernetics 44 (2014) 610.
[20] X. Zhao, H. Yang, W. Xia, X. Wang, Adaptive fuzzy hierarchical sliding-
mode control for a class of mimo nonlinear time-delay systems with input
saturation, IEEE Transactions on Fuzzy Systems 25 (2017) 1062–1077.
[21] M. Hamdy, G. El-Ghazaly,
Adaptive neural decentralized control for
strict feedback nonlinear interconnected systems via backstepping, Neu-
ral Computing & Applications 24 (2014) 259–269.
[22] H. Wang, P. X. Liu, S. Li, D. Wang, Adaptive neural output-feedback con-
trol for a class of nonlower triangular nonlinear systems with unmodeled
dynamics, IEEE Transactions on Neural Networks & Learning Systems
PP (2017) 1–11.
[23] H. Wang, P. Shi, H. Li, Q. Zhou, Adaptive neural tracking control for a
class of nonlinear systems with dynamic uncertainties, IEEE Transactions
on Cybernetics 47 (2017) 3075–3087.
[24] T. Zhang, S. S. Ge, C. C. Hang, Adaptive neural network control for
strict-feedback nonlinear systems using backstepping design, Automatica
36 (2000) 1835–1846.
[25] S. S. Ge, C. C. Hang, H. L. Tong, T. Zhang, Stable adaptive neural net-
work control, Springer International 13 (2002).
[26] C. Yang, Y. Jiang, Z. Li, W. He, C.-Y. Su,
Neural control of biman-
ual robots with guaranteed global stability and motion precision, IEEE
Transactions on Industrial Informatics 13 (2017) 1162–1171.
[27] T. Zhang, S. S. Ge, Adaptive neural network tracking control of mimo
nonlinear systems with unknown dead zones and control directions, IEEE
Transactions on Neural Networks 20 (2009) 483.
[28] Y. Li, S. Tong, Adaptive fuzzy output-feedback stabilization control for
a class of switched nonstrict-feedback nonlinear systems, IEEE Transac-
tions on Cybernetics 47 (2017) 1007–1016.
[29] X. Zhao, L. Zhang, P. Shi, H. R. Karimi, Novel stability criteria for t–s
fuzzy systems, IEEE Transactions on Fuzzy Systems 22 (2014) 313–323.
[30] H. Zhang, M. Li, J. Yang, D. Yang, Fuzzy model-based robust networked
control for a class of nonlinear systems, IEEE Transactions on Systems,
Man, and Cybernetics - Part A: Systems and Humans 39 (2009) 437–447.
[31] S. Tong, Y. Li, P. Shi, Observer-Based Adaptive Fuzzy Backstepping Out-
put Feedback Control of Uncertain MIMO Pure-Feedback Nonlinear Sys-
tems, IEEE Press, 2012.
[32] M. L. Corradini, G. Orlando, Robust stabilization of nonlinear uncertain
plants with backlash or dead zone in the actuator, IEEE Transactions on
Control Systems Technology 10 (2002) 158–166.
[33] G. Lai, Z. Liu, Y. Zhang, C. L. P. Chen, S. Xie,
Adaptive inversion-
based fuzzy compensation control of uncertain pure-feedback systems
with asymmetric actuator backlash, IEEE Transactions on Fuzzy Sys-
tems 25 (2017) 141–155.
[34] X. S. Wang, C. Y. Su, H. Hong, Robust adaptive control of a class of
12

## Page 14

ACCEPTED MANUSCRIPT
ACCEPTED MANUSCRIPT
nonlinear systems with unknown dead-zone, Pergamon Press, Inc., 2004.
[35] J. Zhou, C. Wen, Y. Zhang, Adaptive output control of nonlinear systems
with uncertain dead-zone nonlinearity, IEEE Transactions on Automatic
Control 51 (2006) 504–511.
[36] C. Hu, B. Yao, Q. Wang, Performance-oriented adaptive robust control of
a class of nonlinear systems preceded by unknown dead zone with com-
parative experimental results, IEEE/ASME Transactions on Mechatronics
18 (2013) 178–189.
[37] G. Chen, Robust adaptive control of nonlinear output feedback systems
with unmodeled dynamics,
Intelligent Control & Automation .wcica
.world Congress on (2008) 5508 – 5513.
[38] Z. P. Jiang, L. Praly, Design of robust adaptive controllers for nonlinear
systems with dynamic uncertainties , Automatica 34 (1998) 825–840.
[39] Y. Liu, X. Y. Li, Decentralized robust adaptive control of nonlinear sys-
tems with unmodeled dynamics, IEEE Transactions on Automatic Con-
trol 47 (2002) 848–856.
[40] Z. Liu, F. Wang, Y. Zhang, X. Chen, C. L. Chen, Adaptive fuzzy output-
feedback controller design for nonlinear systems via backstepping and
small-gain approach., IEEE Transactions on Cybernetics 44 (2014) 1714–
1725.
[41] S. Tong, Y. Li, Fuzzy adaptive robust backstepping stabilization for siso
nonlinear systems with unknown virtual control direction , Information
Sciences 180 (2010) 4619–4640.
[42] H. Wang, W. Liu, J. Qiu, P. X. Liu, Adaptive fuzzy decentralized control
for a class of strong interconnected nonlinear systems with unmodeled
dynamics, IEEE Transactions on Fuzzy Systems 26 (2018) 836–846.
[43] Y. J. Liu, S. Tong, C. L. P. Chen, Adaptive fuzzy control via observer
design for uncertain nonlinear systems with unmodeled dynamics, IEEE
Transactions on Fuzzy Systems 21 (2013) 275–288.
[44] X. Liu, Q. Huang, Y. Chen, Robust adaptive controller with disturbance
observer for vehicular radar servo system, International Journal of Con-
trol Automation & Systems 9 (2011) 169–175.
[45] M. Chen, S. S. Ge, Adaptive neural output feedback control of uncertain
nonlinear systems with unknown hysteresis using disturbance observer,
IEEE Transactions on Industrial Electronics 62 (2015) 7706–7716.
[46] Y. Yuan, H. Yuan, Z. Wang, L. Guo, H. Yang, Optimal control for net-
worked control systems with disturbances: a delta operator approach, IET
Control Theory & Applications 11 (2017) 1325–1332.
[47] W. H. Chen, Disturbance observer based control for nonlinear systems,
IEEE/ASME Transactions on Mechatronics 9 (2006) 706–710.
[48] B. Xu, Disturbance observer-based dynamic surface control of transport
aircraft with continuous heavy cargo airdrop, IEEE Transactions on Sys-
tems Man & Cybernetics Systems 47 (2017) 161–170.
[49] Y. Yuan, L. Guo, Z. Wang, Composite control of linear quadratic games in
delta domain with disturbance observers, Journal of the Franklin Institute
354 (2017) 1673–1695.
[50] E. D. Sontag, Y. Wang, On characterizations of input-to-state stability
with respect to compact sets, Nonlinear Control Systems Design (1995)
203–208.
[51] Z. P. Jiang, A combined backstepping and small-gain approach to adap-
tive output feedback control , Automatica 35 (1999) 1131–1139.
[52] M. Chen, Y. Zhou, W. W. Guo, Robust tracking control for uncertain
MIMO nonlinear systems with input saturation using RWNNDO, Elsevier
Science Publishers B. V., 2014.
[53] S. Tong, Y. Li, P. Shi, Fuzzy adaptive backstepping robust control for siso
nonlinear system with dynamic uncertainties, Information Sciences 179
(2009) 1319–1332.
[54] S. S. Ge, K. P. Tee, Approximation-based control of nonlinear MIMO
time-delay systems, Pergamon Press, Inc., 2007.
[55] R. M. Sanner, J.-J. Slotine, Gaussian networks for direct adaptive control,
IEEE Transactions on neural networks 3 (1992) 837–863.
[56] J. Wu, W. Chen, F. Yang, J. Li, Q. Zhu, Global adaptive neural control
for strict-feedback time-delay systems with predeﬁned output accuracy,
Information Sciences 301 (2015) 27–43.
[57] Z. Qu, Robust control of nonlinear uncertain systems 37 (1998) 1437–
1442.
[58] Q. J. Li, C. Y. Zhou, X. Sun, J. Li, A new method of calibrating the
navigation deviation of ship, 5th International Symposium on Test and
Measurement 6 (2003) 2531–2534.
13

## Page 15

ACCEPTED MANUSCRIPT
ACCEPTED MANUSCRIPT
Xinjun Wang was born in Shandong
Province, China, on February 1. 1991. He received the B.S.
degree in Electrical engineering and automation from Binzhou
University, Binzhou, China, in 2013, and the M.S. degree in
Control Theory and Control Engineering from Bohai Univer-
sity, Jinzhou, China in 2016. He is currently working toward
the Ph.D. degree with Hohai University, Nanjing, China. His
research interests include intelligent control in the ﬁeld of AC
machines based on the DSP, ﬁeld-oriented control of PMSM,
adaptive control, nonlinear control, neural network control.
Xinghui Yin was born in Hunan, China, in
1962. He received the B.S. degree in electromagnetic engi-
neering from Xidian University, China, in 1983. Since 1983,
he has been with Purple Mountain Observatory, National As-
tronomical Observatories of China, Chinese Academy of Sci-
ences, Jiangsu, China, where he was engaged in several radio
telescopes, remote sensing radiometers, and satellite earth sta-
tion development projects. His research activities include radio-
heliograph, low noise receivers, and remote sensing measure-
ment.
Qinghui Wu received the B. S. and M. S.
degrees Electric automation from Liaoning Technical Univer-
sity, Fuxin, China in 2000 and 2003, and the Ph.D. degree in
Control Theory and Control Engineering from Dalian Univer-
sity of Technology, Dalian, China in 2006, respectively. He is
presently an associate professor of College of Engineering of
Bohai University. His research interest covers adaptive model-
ing, inverse decoupling control, intelligent control in the ﬁeld
of ac machines.
Fanqi Meng received his M.S degree in
Software Engineering from University of Science and Technol-
ogy of China. He is currently pursuing his Ph.D. degree at Ho-
hai University. His research interests include nonlinear control,
stability theory, neural networks, and nonlinear dynamics.
14
