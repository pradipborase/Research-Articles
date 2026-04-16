# Robust observer-based control designs for discrete.pdf

## Page 1

Recommended by Dr. A Zemouche
Accepted Manuscript
Robust observer-based control designs for discrete nonlinear
systems with disturbances
Cuong M. Nguyen, Pubudu N. Pathirana, Hieu Trinh
PII:
S0947-3580(18)30050-5
DOI:
https://doi.org/10.1016/j.ejcon.2018.09.002
Reference:
EJCON 284
To appear in:
European Journal of Control
Received date:
30 January 2018
Revised date:
18 June 2018
Accepted date:
1 September 2018
Please cite this article as: Cuong M. Nguyen, Pubudu N. Pathirana, Hieu Trinh, Robust observer-based
control designs for discrete nonlinear systems with disturbances, European Journal of Control (2018),
doi: https://doi.org/10.1016/j.ejcon.2018.09.002
This is a PDF ﬁle of an unedited manuscript that has been accepted for publication. As a service
to our customers we are providing this early version of the manuscript. The manuscript will undergo
copyediting, typesetting, and review of the resulting proof before it is published in its ﬁnal form. Please
note that during the production process errors may be discovered which could affect the content, and
all legal disclaimers that apply to the journal pertain.

## Page 2

ACCEPTED MANUSCRIPT
ACCEPTED MANUSCRIPT
Robust observer-based control designs for discrete
nonlinear systems with disturbances
Cuong M. Nguyena,∗, Pubudu N. Pathiranaa, Hieu Trinha
aDeakin University, Geelong, VIC 3217, Australia, School of Engineering
Abstract
In this paper, we consider the robust observer-based control design problem
for discrete nonlinear systems with disturbances. A new approach is proposed
to provide less conservative Linear Matrix Inequality control design conditions
and enhance the robustness of control designs, where the observer and controller
gains are computed independently. Both the one-sided Lipschitz condition and
the Linear Parameter Varying approach, which are two well-known alternatives
to the classical Lipschitz condition, are considered to address nonlinearities.
Two numerical examples are presented to illustrate the superiorities of the new
approach over the traditional H∞approach as well as relevant works in the
literature.
Keywords:
Observer-based control, Robust control design, Disturbance,
One-sided Lipschitz condition, Linear Parameter Varying (LPV) system,
Linear matrix inequality (LMI)
1. Introduction
Feedback control is a long-established topic and has been one of the key re-
search areas in control theory [1]. State feedback control is developed based on
the assumption that full information of system states is available. This assump-
tion, however, is hardly true in practice [2, 3]. Due to technical or economic
diﬃculties, the full knowledge of the states can rarely be measured or available
in most cases. Observer-based control, where the estimation of the true states
is provided by an auxiliary system driven by the control input and measured
output of the control system, has been a practical solution to this puzzle over
the past decades, with many results reported in the literature [4–21].
The observer-based control problem for linear systems has been well studied
based on the separation principle, where the observer and controller gains are
∗Corresponding author.
Email addresses: mc.nguyen@deakin.edu.au (Cuong M. Nguyen),
pubudu.pathirana@deakin.edu.au (Pubudu N. Pathirana), hieu.trinh@deakin.edu.au
(Hieu Trinh)
Preprint submitted to European Journal of Control
September 5, 2018

## Page 3

ACCEPTED MANUSCRIPT
ACCEPTED MANUSCRIPT
computed independently [12]. On the other hand, the observer-based control
problem for nonlinear counterparts is still open and challenging. In traditional
approaches for nonlinear observer-based control problem, the inseparability of
the observer and controller gains leads to the inevitable existence of the bilinear
terms in the development of design conditions. In order to derive LMI con-
ditions, the well-known Young inequality is usually required to linearize such
bilinear terms. The Young inequality is a useful means to deal with bilinear
terms. However, it further introduces conservativeness into the LMI conditions.
To lessen the conservativeness produced by the Young inequality, a less conser-
vative version of the Young inequality has been utilized instead of the classical
one in some works, e.g. [15]. Nevertheless, it is interesting to question whether
such bilinear terms can be avoided in the derivation of observer-based control
design conditions for nonlinear systems, especially in discrete-time, i.e. can we
circumvent the Young inequality in the development of nonlinear observer-based
control designs and accordingly provide less conservative conditions as well as
enhance the robustness of control designs? This question will be the main focus
of this paper.
The well-known Lipschitz condition has been the most common approach to
tackle nonlinearities in control theory. Because of its conservativeness and the
inherent conservativeness in control designs based on Lipschitz condition, many
approaches have been introduced as alternatives to the Lipschitz condition, e.g.
the one-sided Lipschitz condition [22–30], the Linear Parameter Varying (LPV)
approach [31, 32]. In the LPV approach, the Lipschitz condition is reformulated
and the Lipschitz systems are converted into LPV systems. This approach is
less conservative than the traditional Lipschitz approach and is useful to deal
with systems with large Lipschitz constants. The class of one-sided Lipschitz
systems, on the other hand, includes the class of Lipschitz systems as a special
case. The one-sided Lipschitz condition also possesses some superiorities over
the classical Lipschitz condition, e.g. the one-sided Lipschitz constant can be
positive, negative, or zero, while the Lipschitz constant is strictly positive. It is
also worth pointing out that there is a lack of works that address the observer-
based control design problem for discrete one-sided Lipschitz systems.
In addition, one of the basic requirements for any good control system is
the robustness against disturbances, system modeling errors, or parameter vari-
ations [1]. The presence of disturbances or errors is often unavoidable in many
control systems, which can degrade the performance of control systems or even
lead to instability if not taken into account. Robust control is developed to
guarantee satisfactory performance of control systems subject to disturbances
or errors [33–36]. To tackle this issue, H∞ﬁltering approach has long been a
practical and eﬀective method.
Motivated by the aforementioned works, in this paper, we study the robust
observer-based control problem for discrete nonlinear systems with disturbances.
The main contributions of this paper can be summarized as follows:
• A new approach, which can be considered as an extension of the traditional
H∞approach, is introduced with the expectations to be able to provide
2

## Page 4

ACCEPTED MANUSCRIPT
ACCEPTED MANUSCRIPT
less conservative LMI conditions and enhance the robustness of control
designs. In this approach, the observer and controller gains are computed
independently.
• One-sided Lipschitz condition and LPV approach, which are two well-
known alternatives to the restrictive Lipschitz condition, are considered
to address nonlinearities.
• Using two numerical examples, we show that the new approach can indeed
lead to less conservative observer-based control design conditions and im-
prove the robustness of control systems compared to the traditional H∞
approach as well as relevant works in the literature.
2. Problem Statement and Preliminaries
Consider the following class of discrete nonlinear systems with disturbances:
x(k + 1) = Ax(k) + Bu(k) + f(x(k)) + Wω(k), k ∈N,
(1a)
y(k) = Cx(k) + Dω(k),
(1b)
where x(k) ∈Rn, u(k) ∈Rm, and y(k) ∈Rp are the state vector, the control
input vector, and the output measurement vector of system (1), respectively.
ω(t) ∈ℓq
2 is the exogenous disturbance vector of system (1), which can represent
system modeling errors, parameter variations, or environmental noises. A ∈
Rn×n, B ∈Rn×m, W ∈Rn×q, C ∈Rp×n, and D ∈Rp×q are known, constant
matrices. The nonlinear function f(x(k)) is assumed to satisfy
f(0) = 0.
(2)
Due to technical or economical diﬃculties, the full knowledge of the state
vector x(k) of system (1) may not be available [2, 3]. Observer-based controller
u(k) = −Kˆx(k) is a practical solution in this case, where K is the controller
gain matrix and ˆx(k) ∈Rn is the estimate of x(k) computed by the observer
system
ˆx(k + 1) = Aˆx(k) + Bu(k) + f(ˆx(k)) + L(y(k) −Cˆx(k)),
(3)
where L is the observer gain matrix to be designed.
The state estimation error is deﬁned as e(k) = x(k)−ˆx(k). The error dynamics
can be computed as
e(k + 1) = (A −LC)e(k) + ∆f(k) + (W −LD)ω(k),
(4)
where ∆f(k) = f(x(k)) −f(ˆx(k)).
Consider the observer system (3), our goal is to design the observer-based
controller u(k) = −Kˆx(k) to robustly stabilize the closed-loop system (1):
x(k + 1) = Ax(k) −BKˆx(k) + f(x(k)) + Wω(k)
3

## Page 5

ACCEPTED MANUSCRIPT
ACCEPTED MANUSCRIPT
= (A −BK)x(k) + BKe(k) + f(x(k)) + Wω(k).
(5)
Consider the following augmented system
x(k + 1)
e(k + 1)

=
A −BK
BK
0
A −LC
 x(k)
e(k)

+
f(x(k))
∆f(k)

+

W
W −LD

ω(k). (6)
In traditional H∞approach, the gain matrices L and K are designed such that
system (6) is H∞asymptotically stable, i.e. the following relation holds under
zero initial condition:
∥xe∥ℓ2n
2
≤µ∥ω∥ℓq
2, µ > 0,
(7)
where xe(k) = [xT (k) eT (k)]T , and µ is the disturbance attenuation level to be
minimized.
(7) is ensured if there exists a Lyapunov-Krasovskii functional V(k) ≥0 such
that
∆V(k) + xT
e (k)xe(k) −µ2ωT (k)ω(k) < 0,
(8)
where ∆V(k) = V(k + 1) −V(k).
The inseparability of the gain matrices L and K in this approach leads to
the inevitable existence of the bilinear term BK = BY P −1
1
in the derivation of
observer-based control design conditions (Y , P1 are matrix variables in design
conditions). The linearization of the term BY P −1
1
is usually accomplished by
the use of the well-known Young inequality. The Young inequality provides an
convenient and eﬀective way to linearize such bilinear terms in the development
of LMI conditions. However, it clearly adds some conservativeness into the ob-
tained conditions. A less conservative form of the Young inequality has been
utilized in some recent works to reduce conservativeness, e.g. [15]. Nevertheless,
it is appealing to ask: is it possible to circumvent the use of Young inequality
in the development of observer-based control designs in order to provide less
conservative conditions and enhance the robustness of control designs? Bear in
mind that, in this paper, we introduce the following separation approach which
can be considered as an extension of the traditional H∞approach.
The objective of the new approach is to design the gain matrices L and K
such that the following relations simultaneously hold under zero initial condi-
tions:
∥x∥ℓn
2 ≤µe∥e∥ℓn
2 + µde∥ω∥ℓq
2, µe > 0, µde > 0,
(9)
∥e∥ℓn
2 ≤µds∥ω∥ℓq
2, µds > 0,
(10)
where µe, µde and µds are attenuation levels to be optimized.
From (9) and (10), we have ∥x∥ℓn
2 ≤µ∥ω∥ℓq
2, where µ = µeµds + µde, i.e. the
closed-loop system (5) is H∞asymptotically stable.
4

## Page 6

ACCEPTED MANUSCRIPT
ACCEPTED MANUSCRIPT
(9) and (10) are guaranteed if there exist Lyapunov-Krasovskii functionals
V1(k) ≥0 and V2(k) ≥0 such that
∆V1(k) + xT (k)x(k) −eT (k)P −1
1
e(k) −µ2
deωT (k)ω(k) < 0,
(11)
where µe =
p
1/λmin(P1), P1 > 0, and
∆V2(k) + eT (k)e(k) −µ2
dsωT (k)ω(k) < 0,
(12)
where ∆V1(k) = V1(k + 1) −V1(k), and ∆V2(k) = V2(k + 1) −V2(k).
Indeed, from (11) and the fact that eT (k)P −1
1
e(k) ≤λmax(P −1
1
)||e(k)||2 =
1/λmin(P1)||e(k)||2, we have
∞
X
k=0
∆V1(k) +
∞
X
k=0
xT (k)x(k) −
∞
X
k=0
eT (k)P −1
1
e(k) −
∞
X
k=0
µ2
deωT (k)ω(k) ≤0
(13)
⇒V1(∞) −V1(0) + ||x||2
ℓn
2 −µ2
e||e||2
ℓn
2 −µ2
de||ω||2
ℓq
2 ≤0.
(14)
Since V1(∞) ≥0 and V1(0) = 0 (zero initial condition), (14) ensures (9).
Similarly, we can prove that (10) is guaranteed by (12).
In the next sections, we will utilize the new method to study the robust
observer-based control design problems for one-sided Lipschitz systems and LPV
systems, respectively. First, let us recall the following useful well-known results.
Lemma 1 (Young inequality). Given matrices of appropriate dimensions Ω,
Φ, and Π > 0, the following inequality holds
ΩΦ + ΦT ΩT ≤εΩΠ−1ΩT + ε−1ΦT ΠΦ, ∀ε ∈R+.
(15)
Lemma 2 (Schur complement lemma). Given matrices of appropriate dimen-
sions Ω= ΩT , Φ, and Π > 0, we have Ω+ ΦT ΠΦ < 0 if and only if
−Π−1
Φ
ΦT
Ω

< 0.
(16)
3. One-sided Lipschitz Systems
In this section, the nonlinearity f(x(k)) is assumed to satisfy the one-sided
Lipschitz and the quadratically inner-bounded conditions in region D ⊂Rn[23]:
⟨f(x) −f(ˆx), x −ˆx⟩≤ρ||x −ˆx||2, ∀x, ˆx ∈D,
(17)
||f(x) −f(ˆx)||2 ≤β||x −ˆx||2 + γ⟨f(x) −f(ˆx), x −ˆx⟩,
(18)
where ρ, β, γ ∈R are known constants which can be positive, zero, or negative.
ρ is known as the one-sided Lipschitz constant of the nonlinear function f(x).
5

## Page 7

ACCEPTED MANUSCRIPT
ACCEPTED MANUSCRIPT
Without loss of generality, we assume that ρ ≥0 and β ≥0.
Suﬃcient conditions in terms of LMIs, which allow us to compute the gain
matrices L and K for the robust observer-based control design for one-sided
Lipschitz systems, will be presented in the next theorem which utilizes the new
approach. Similar to the H∞method, we wish for the attenuated levels µde and
µds to be minimal.
Theorem 1. Given a scalar ε0 > 0, the controller u(k) = −Kˆx(k) associated
with the observer system (3) will robustly stabilize system (1) by means of the
approach (9)-(10) with a minimum attenuated level µ if there exist matrices of
appropriate dimensions P1 > 0, P2 > 0, Y , Z, and scalars εi > 0 (i = 1, 3),
¯µde > 0, ¯µds > 0 such that the following convex optimization problems hold:
min(¯µde) subject to


−P1
AP1 −BY
BY
W
ε1I
0
0
∗
−P1
0
0
(γ −ε0)P1
P1
p
2(ε0ρ + β)P1
∗
∗
−P1
0
0
0
0
∗
∗
∗
−¯µdeI
0
0
0
∗
∗
∗
∗
−2ε1I
0
0
∗
∗
∗
∗
∗
−I
0
∗
∗
∗
∗
∗
∗
−ε1I


< 0,
(19)
and min(¯µds) subject to


−P2
P2A −ZC
P2W −ZD
P2
∗
Ξ
0
(γε3 −ε2)I
∗
∗
−¯µdsI
0
∗
∗
∗
−2ε3I

< 0,
(20)
where Ξ = I −P2 + 2(ρε2 + βε3)I.
K, L and the minimized µ are obtained as K = Y P −1
1
, L = P −1
2
Z and µ =
p
1/λmin(P1)√¯µds + √¯µde.
Proof. Consider the Lyapunov-Krasovskii functionals V1(k) = xT (k)P −1
1
x(k),
V2(k) = eT (k)P2e(k) (P1 > 0, P2 > 0). Denote
A1 = [A −BK
BK
W
I],
(21)
A2 = [A −LC
W −LD
I],
(22)
ζ1(k) = [xT (k) eT (k) ωT (k) f T (x(k))]T ,
(23)
ζ2(k) = [eT (k) ωT (k) ∆f T (k)]T .
(24)
We have
∆V1(k) = xT (k + 1)P −1
1
x(k + 1) −xT (k)P −1
1
x(k)
= ζT
1 (k)AT
1 P −1
1
A1ζ1(k) −xT (k)P −1
1
x(k),
(25)
∆V2(k) = eT (k + 1)P2e(k + 1) −eT (k)P2e(k)
6

## Page 8

ACCEPTED MANUSCRIPT
ACCEPTED MANUSCRIPT
= ζT
2 (k)AT
2 P2A2ζ2(k) −eT (k)P2e(k).
(26)
From (17), (18), and (2), we obtain the following
0 ≤2ε0ε−1
1 (ρxT (k)x(k) −f T (x(k))x(k)),
(27)
0 ≤2ε−1
1 (βxT (k)x(k) + γf T (x(k))x(k) −f T (x(k))f(x(k))),
(28)
0 ≤2ε2(ρeT (k)e(k) −∆f T (k)e(k)),
(29)
0 ≤2ε3(βeT (k)e(k) + γ∆f T (k)e(k) −∆f T (k)∆f(k)),
(30)
where εi (i = 0, 3) are positive scalars. Denote
Y = KP1, Z = P2L, ¯µde = µ2
de, ¯µds = µ2
ds.
(31)
We have
∆V1(k)+xT (k)x(k)−eT (k)P −1
1
e(k)−µ2
deωT (k)ω(k) ≤ζT
1 (k)(Φ1+AT
1 P −1
1
A1)ζ1(k),
(32)
where
Φ1 =


Υ1
0
0
(γ −ε0)ε−1
1 I
∗
−P −1
1
0
0
∗
∗
−¯µdeI
0
∗
∗
∗
−2ε−1
1 I

,
Υ1 = I −P −1
1
+ 2(ε0ρ + β)ε−1
1 I.
By the Schur complement lemma, Φ1 + AT
1 P −1
1
A1 < 0 is equivalent to
−P1
A1
∗
Φ1

< 0.
(33)
Pre- and post- multiplying the left-hand side of (33) by diag{I, P1, P1, I, ε1I},
i.e. applying a congruent transformation, we obtain the following equivalent
condition


−P1
AP1 −BY
BY
W
ε1I
∗
Υ2
0
0
(γ −ε0)P1
∗
∗
−P1
0
0
∗
∗
∗
−¯µdeI
0
∗
∗
∗
∗
−2ε1I


< 0,
(34)
where Υ2 = P1P1 −P1 + 2(ε0ρ + β)ε−1
1 P1P1.
From (32)-(34), by Schur complement lemma, (9) is guaranteed if (19) holds.
Similarly, we have
∆V2(k) + eT (k)e(k) −µ2
dsωT (k)ω(k) ≤ζT
2 (k)(Φ2 + AT
2 P2A2)ζ2(k),
(35)
where
Φ2 =


Ξ
0
(γε3 −ε2)I
∗
−¯µdsI
0
∗
∗
−2ε3I

.
7

## Page 9

ACCEPTED MANUSCRIPT
ACCEPTED MANUSCRIPT
By the Schur complement lemma, Φ2 + AT
2 P2P −1
2
P2A2 < 0 is equivalent to
−P2
P2A2
∗
Φ2

< 0.
(36)
From (35)-(36), (10) is ensured if (20) holds.
From (31), K, L and µ can be obtained as K = Y P −1
1
, L = P −1
2
Z and µ =
p
1/λmin(P1)√¯µds + √¯µde.
Remark 1. As can be seen from the proof of Theorem 1, condition (11) only
involves the controller gain matrix K, while condition (12) only involves the
observer gain matrix L. This separation, together with the well chosen term
−eT (k)P −1
1
e(k) in (11), allows us to manipulate the term BK into linear term
without having to deal with it as a bilinear term like the tradition H∞approach,
i.e. the Young inequality is not necessary in our approach.
The robust observer-based control design conditions for one-sided Lipschitz
systems using the traditional H∞approach will be provided in the next theorem.
The proof of this theorem is similar to the proof of Theorem 1 and will be
omitted for the sake of brevity.
Theorem 2. Given a scalar ε0 > 0, the controller u(k) = −Kˆx(k) associated
with the observer system (3) will robustly stabilize system (1) by means of the
traditional H∞approach (7) with a minimum attenuated level µ if there exist
matrices of appropriate dimensions P1 > 0, P2 > 0, Y , Z, and scalars εi > 0
(i = 1, 3), ¯µ > 0 such that the following convex optimization problem holds:
min(¯µ) subject to
Γ
Λ
⋆
Σ

< 0, where
Γ =


−P1
0
AP1 −BY
0
W
ε1I
0
∗
−P2
0
P2A −ZC
P2W −ZD
0
P2
∗
∗
−P1
0
0
(γ −ε0)P1
0
∗
∗
∗
Ξ
0
0
(γε3 −ε2)I
∗
∗
∗
∗
−¯µI
0
0
∗
∗
∗
∗
∗
−2ε1I
0
∗
∗
∗
∗
∗
∗
−2ε3I


,
Ξ = I −P2 + 2(ρε2 + βε3)I,
Λ =


0
0
P1
0
0
0
0
0
0
p
2(ε0ρ + β)P1
0
0
0
0
(BY )T
0
0
0
0
0
0
0
0
0
I
0
0
0


T
,
Σ = diag{−I, −ε1I, −P1, −P1}.
K, L and the minimized µ are obtained as K = Y P −1
1
, L = P −1
2
Z and µ = √¯µ.
Remark 2. In Theorem 1, in order to avoid bilinear term and the use of Young
inequality, the scalar ε0 is introduced as a priori rather than a variable.
In
8

## Page 10

ACCEPTED MANUSCRIPT
ACCEPTED MANUSCRIPT
Theorem 2, the scalar ε0 is also introduced as a priori to circumvent such bilinear
term. However, in Theorem 2, the use of Young inequality is unavoidable due
to the presence of BK = BY P −1
1
.
Therefore, in order to ﬁnd the minimal
value of µ in Theorem 1 and Theorem 2, we solve the convex optimization
problems with diﬀerent values of ε0. In the numerical examples section, the
following one-dimensional search strategy for ε0 is incorporated to solve the
convex optimization problems with diﬀerent values of ε0: we gradually increase
the value of ε0 from 0 to 104 with the step of 0.0001 on the interval (0, 1], the
step of 0.01 on the interval (1, 102] and the step of 1 on the interval (102, 104].
Note that, ε0 can be searched on a smaller interval with bigger steps to reduce
the computational cost. The obtained minimal value of µ, however, will be less
desirable. This is the trade-oﬀchoice between computational cost and system
performance in practice.
4. Linear Parameter Varying Systems
In this section, the nonlinear function f(x(k)) is assumed to be α-Lipschitz:
||f(x) −f(ˆx)|| ≤α ∥x −ˆx∥, ∀x, ˆx ∈Rn, α > 0.
(37)
For given vectors x = (x1, . . . , xn)T , y = (y1, . . . , yn)T ∈Rn, let us denote the
vector xyi ∈Rn(i = 0, . . . , n) as
(
xyi = (y1, . . . , yi, xi+1, . . . , xn)T , i = 1, . . . , n,
xy0 = x.
(38)
The following lemma is necessary for the development of our results in this
section.
Lemma 3. [31] Consider the nonlinear function f = (f1, . . . , fm)T : Rn →Rm,
the following properties are equivalent:
• Lipschitz property: f is α-Lipschitz with respect to its argument, i.e.
||f(x) −f(y)|| ≤α||x −y||, ∀x, y ∈Rn.
(39)
• Reformulated Lipschitz property: ∀i, j = 1, . . . , n, there exist functions
fij : Rn × Rn →R and constants αij and ¯αij such that ∀x, y ∈Rn:
f(x) −f(y) =
m
X
i=1
n
X
j=1
fijHij(x −y)
(40)
and
αij ≤fij ≤¯αij
(41)
where
fij = fij(xyj−1, xyj) =





0 if xj = yj
fi(xyj−1) −fi(xyj)
xj −yj
if xj ̸= yj
9

## Page 11

ACCEPTED MANUSCRIPT
ACCEPTED MANUSCRIPT
and Hmn
ij
= em(i)eT
n(j), where es(i) = (0, . . . , 0,
ith
z}|{
1 , 0, . . . , 0)T ∈Rs.
From (37) and (2), according to Lemma 3, there are functions fij : Rn×Rn →
R, and constants αij, ¯αij such that
αij ≤fij ≤¯αij,
(42)
∆f(k) = f(x(k)) −f(ˆx(k)) =
n
X
i=1
n
X
j=1
fij(xˆxj−1, xˆxj)Hnn
ij (x(k) −ˆx(k)), (43)
f(x(k)) =
n
X
i=1
n
X
j=1
fij(x0j−1, x0j)Hnn
ij x(k),
(44)
Denote
A⋄=
n
X
i=1
n
X
j=1
fij(xˆxj−1, xˆxj)Hnn
ij ∈Rn×n,
A∗=
n
X
i=1
n
X
j=1
fij(x0j−1, x0j)Hnn
ij ∈Rn×n.
The estimation error dynamics (4), the closed-loop system (5), and the aug-
mented system (6) can be rewritten as
e(k + 1) = (A + A⋄−LC)e(k) + (W −LD)ω(k),
(45)
x(k + 1) = (A + A∗−BK)x(k) + BKe(k) + Wω(k),
(46)
and
x(k + 1)
e(k + 1)

=
A + A∗−BK
BK
0
A + A⋄−LC
 x(k)
e(k)

+

W
W −LD

ω(k). (47)
From (42), the matrices A⋄and A∗are in the bounded convex set H of
which the vertices set is deﬁned by
VH = {Θ = (Θij) ∈Rn×n : Θij ∈{αij, ¯αij}}.
(48)
Suﬃcient LMIs conditions for the robust observer-based control design using
the approach (9)-(10) for LPV systems will be presented in the next theorem.
The theorem allows us to compute matrices K, L and the minimal µ.
Theorem 3. The controller u(k) = −Kˆx(k) associated with the observer system
(3) will robustly stabilize system (1) by means of the approach (9)-(10) with a
minimum attenuated level µ if there exist matrices of appropriate dimensions
P1 > 0, P2 > 0, Y , Z, and scalars ¯µde > 0, ¯µds > 0 such that the following
10

## Page 12

ACCEPTED MANUSCRIPT
ACCEPTED MANUSCRIPT
convex optimization problems hold ∀A∗, A⋄∈VH:
min(¯µde) subject to


−P1
(A + A∗)P1 −BY
BY
W
0
∗
−P1
0
0
P1
∗
∗
−P1
0
0
∗
∗
∗
−¯µdeI
0
∗
∗
∗
∗
−I


< 0,
(49)
and min(¯µds) subject to


−P2
P2(A + A⋄) −ZC
P2W −ZD
∗
I −P2
0
∗
∗
−¯µdsI

< 0.
(50)
K, L and the minimized µ are obtained as K = Y P −1
1
, L = P −1
2
Z and µ =
p
1/λmin(P1)√¯µds + √¯µde.
Proof. Consider the Lyapunov-Krasovskii functionals V1(k) = xT (k)P −1
1
x(k),
V2(k) = eT (k)P2e(k) (P1 > 0, P2 > 0). Denote
¯A1 = [A + A∗−BK
BK
W],
(51)
¯A2 = [A + A⋄−LC
W −LD],
(52)
¯ζ1(k) = [xT (k) eT (k) ωT (k)]T ,
(53)
¯ζ2(k) = [eT (k) ωT (k)]T .
(54)
We have
∆V1(k) = xT (k + 1)P −1
1
x(k + 1) −xT (k)P −1
1
x(k)
= ¯ζT
1 (k) ¯AT
1 P −1
1
¯A1¯ζ1(k) −xT (k)P −1
1
x(k),
(55)
∆V2(k) = eT (k + 1)P2e(k + 1) −eT (k)P2e(k)
= ¯ζT
2 (k) ¯AT
2 P2 ¯A2¯ζ2(k) −eT (k)P2e(k).
(56)
Denote
Y = KP1, Z = P2L, ¯µde = µ2
de, ¯µds = µ2
ds.
(57)
We have
∆V1(k)+xT (k)x(k)−eT (k)P −1
1
e(k)−µ2
deωT (k)ω(k) ≤¯ζT
1 (k)(¯Φ1+ ¯AT
1 P −1
1
¯A1)¯ζ1(k),
(58)
where ¯Φ1 = diag{I −P −1
1
, −P −1
1
, −¯µdeI}. By the Schur complement lemma,
¯Φ1 + ¯AT
1 P −1
1
¯A1 < 0 is equivalent to
−P1
¯A1
∗
¯Φ1

< 0.
(59)
11

## Page 13

ACCEPTED MANUSCRIPT
ACCEPTED MANUSCRIPT
Pre- and post- multiplying the left-hand side of (59) by diag{I, P1, P1, I}, we
obtain the following equivalent condition


−P1
(A + A∗)P1 −BY
BY
W
∗
P1P1 −P1
0
0
∗
∗
−P1
0
∗
∗
∗
−¯µdeI

< 0.
(60)
From (58)-(60), by Schur complement lemma, (9) is guaranteed if (49) holds.
Similarly, we have
∆V2(k) + eT (k)e(k) −µ2
dsωT (k)ω(k) ≤¯ζT
2 (k)(¯Φ2 + ¯AT
2 P2 ¯A2)¯ζ2(k),
(61)
where ¯Φ2 = diag{I −P2, −¯µdsI}.
By the Schur complement lemma, ¯Φ2 +
¯AT
2 P2P −1
2
P2 ¯A2 < 0 is equivalent to (50), i.e. (10) is ensured if (50) holds.
Note that, from (57), K, L and µ can be obtained as K = Y P −1
1
, L = P −1
2
Z
and µ =
p
1/λmin(P1)√¯µds + √¯µde.
Remark 3. In [19], the authors also addressed the observer-based control de-
sign problem for LPV systems using the separation method. However, diﬀerent
from condition (9) in this paper which is ∥x∥ℓn
2 ≤µe∥e∥ℓn
2 + µde∥ω∥ℓq
2, the
authors in [19] used the following corresponding condition
∥x∥ℓn
2 ≤√ν∥¯ω∥ℓm+q
2
,
where ¯ω = [(Ke)T ωT ]T .
(62)
This condition led to the LMI condition


−P1
0
P1(A + A∗)T −Y BT
P1
∗
−νI
[B
W]T
0
∗
∗
−P1
0
∗
∗
∗
−I

< 0.
(63)
It is easy to see that the minimized value of ν in (63) is directly aﬀected by
not only W but also B. On the other hand, the corresponding minimized value
of ¯µde in (49) is directly aﬀected by W only. Numerical comparisons will be
provided in Example 1 to show the diﬀerence.
The robust observer-based control design conditions for LPV systems using
the traditional H∞approach will be provided in the next theorem. The proof
of this theorem will be omitted for the sake of brevity as it is similar to the
proof of Theorem 3.
Theorem 4. The controller u(k) = −Kˆx(k) associated with the observer system
(3) will robustly stabilize system (1) by means of the traditional H∞approach
(7) with a minimum attenuated level µ if there exist matrices of appropriate
dimensions P1 > 0, P2 > 0, Y , Z, and scalar ¯µ > 0 such that the following
convex optimization problem holds: min(¯µ) subject to
¯Γ
¯Λ
⋆
¯Σ

< 0, ∀(A∗, A⋄) ∈
12

## Page 14

ACCEPTED MANUSCRIPT
ACCEPTED MANUSCRIPT
VH × VH, where
¯Γ =


−P1
0
(A + A∗)P1 −BY
0
W
∗
−P2
0
P2(A + A⋄) −ZC
P2W −ZD
∗
∗
−P1
0
0
∗
∗
∗
I −P2
0
∗
∗
∗
∗
−¯µI


,
¯Λ =


0
0
P1
0
0
(BY )T
0
0
0
0
0
0
0
I
0


T
,
¯Σ = diag{−I, −P1, −P1}.
K, L and the minimized µ are obtained as K = Y P −1
1
, L = P −1
2
Z and µ = √¯µ.
Remark 4. The one-sided Lipschitz condition and the LPV approach are two
well-known alternatives to the restrictive Lipschitz condition in the literature.
In the LPV approach, the Lipschitz condition is reformulated and the Lipschitz
system is converted into LPV system where all properties of the nonlinearity
are utilized.
For this reason, the LPV approach can well handle nonlinear
systems with large Lipschitz constants. However, the computational complexity
of the LPV approach can be quite high in some cases as the number of LMI
conditions in the LPV approach corresponds to the size of the vertices set. On
the other hand, the class of one-sided Lipschitz systems includes the class of
Lipschitz systems as a special case. The one-sided Lipschitz constant can be
found positive, zero, or negative, compared to the strictly positive Lipschitz
constant. While the one-sided Lipschitz condition is not as eﬀective as the LPV
approach in dealing with systems with large Lipschitz constants, it does not lead
to high computational complexity in some cases as the LPV approach. Thus,
depending on the the types of nonlinearities, the appropriate approach should
be chosen as will be shown in Example 2.
5. Numerical Examples
In this section, we present two examples to illustrate the eﬀectiveness and
advantages of the new approach over the traditional H∞approach, as well as
the edges of the new results over closely related works [12, 19] in the literature.
Example 1. Consider the single-link ﬂexible joint robotic system [31] with dis-
turbances in continuous-time as follows
˙x(t) = Acx(t) + Bcu(t) + fc(x(t)) + Wcω(t), t ≥0,
(64a)
y(t) = Ccx(t) + Dcω(t),
(64b)
where
Ac =


0
1
0
0
−48.6
−1.25
48.6
0
0
0
0
1
19.5
0
−19.5
0

, Bc =


0
21.6
0
0

, Wc =


1
0
0
0

,
13

## Page 15

ACCEPTED MANUSCRIPT
ACCEPTED MANUSCRIPT
Cc =

1
0
0
0
0
1
0
0

, Dc =
 1
0

,
fc(x(t)) = [0 0 0 −3.33 sin(x3(t))]T .
Applying the Euler discretization method with the sampling time ts = 1ms =
0.001s, we obtain the discrete-time system (1): A = I + tsAc, B = tsBc,
f(x) = tsfc(x), W = tsWc, C = Cc, D = Dc.
It is well-known that the type of nonlinearities in this example can be eﬀectively
handled by the LPV approach [31]. Hence, the results in Theorem 3 will be
utilized in this example. The vertices set can be determined as
VH =









0
0
0
0
0
0
0
0
0
0
0
0
0
0
ts3.33
0

,


0
0
0
0
0
0
0
0
0
0
0
0
0
0
−ts3.33
0









.
Via the Matlab LMI Control Toolbox, the convex optimization problems in
Theorem 3 are feasible with the following computed gain matrices
K = [5705.0767 33.3035
−3310.2808 401.3578] , L =


0.0010
−0.0857
0.0000
0.6452
0.0000
0.3858
0.0000
0.2444

,
and the minimized attenuation level µ = 1.0100. Note that although the gain
matrix K seems to be high, it actually compensates for the sampling time
ts = 0.001s.
For the purpose of simulation, we assume x(0) = [0.1
−0.1
0.2
−0.2]T ,
ˆx(0) = [0.2
−0.2 0.1
−0.1]T , and
ω(k) =



0.1 cos(0.5tsk)
if
k ∈
S
i∈N\{0}

20i−3
ts
, 20i
ts
i
,
0
otherwise.
The illustration of ω is shown in Figure 1. The responses of the uncontrolled
system (1), i.e. u(k) = 0, ∀k ∈N, and the responses of the closed-loop system
(5) are illustrated in Figure 2 and Figure 3, respectively. It can be observed from
Figure 2 and Figure 3 that the controlled system (1) is robustly stable and the
performance of the system has been noticeably improved by the observer-based
controller.
Now, solving the convex optimization problem in Theorem 4 via the Matlab LMI
Control Toolbox, the minimal attenuated level µ is computed as µ = 1.4392. It
can be seen that the result from Theorem 3 (µ = 1.0100) is considerably less
conservative than the result from Theorem 4 (µ = 1.4392). In other words, the
new approach can provide more robust observer-based control designs compared
to the traditional H∞approach.
On the other hand, the LMI condition of Theorem 3.1 in [12] is infeasible for the
14

## Page 16

ACCEPTED MANUSCRIPT
ACCEPTED MANUSCRIPT
system studied in this example (since we wish to robustly stabilize the closed-
loop system, the matrix ˜C in [12] is chosen as ˜C = [I
I]). As commented
in Remark 3, while the minimized attenuation level in Theorem 3 is directly
aﬀected by W only, the minimized attenuation level in Theorem 3.2 [19] is
directly aﬀected by not only W but also B. To facilitate numerical comparisons
between the two results, we will reconsider the system studied in this example
except B = ts[0 b 0 0]T , b ∈R. The minimized attenuation levels µ obtained
by Theorem 3 and Theorem 3.2 [19] corresponding to diﬀerent values of b are
listed in Table 1. From Table 1, we can see that while the minimized µ obtained
by Theorem 3 remains the same, the minimized µ obtained by Theorem 3.2 [19]
is aﬀected by the change of b.
Table 1: The minimized attenuation levels µ obtained by the two methods with diﬀerent
values of b.
b
1
10
102
103
104
Theorem 3
1.0100
1.0100
1.0100
1.0100
1.0100
Theorem 3.2 [19]
1.5400
1.0115
1.0048
1.0337
10.0505
Example 2. Consider the following continuous-time nonlinear system with dis-
turbances (64) of which the nonlinearity is from the motion of a moving object
[23]
Ac =
 −1
1
1.5
−0.5

, Bc =

0
−1

, Wc =
 2
1

, Cc = [0 1], D = 1,
fc(x(t)) =
 −x1(t)(x2
1(t) + x2
2(t))
−x2(t)(x2
1(t) + x2
2(t))

.
Applying the Euler discretization method with the sampling time ts = 1ms =
0.001s, we get the discrete-time system (1): A = I + tsAc, B = tsBc, f(x) =
tsfc(x), W = tsWc, C = Cc, D = Dc.
In the LPV approach, the number of LMI conditions corresponds to the number
of vertices. With regard to the nonlinearity in this example, the vertices set
VHn has 24 = 16 vertices. Due to the large number of LMI conditions, it is
not eﬀective to use the LPV approach. Hence, the results in Theorem 1 will be
utilized instead of the results in Theorem 3 in this example.
f(x) is globally one-sided Lipschitz with ρ = 0 [23]. Consider the region D =
{x ∈R2 : ||x|| ≤r}, r = 10. According to [23], f(x) is quadratically inner-
bounded in D with constants β = 0 and γ = −4r2ts. Furthermore, f(x) is
locally Lipschitz in D with the Lipschitz constant 3r2ts [23].
Using the Matlab LMI Control Toolbox, the convex optimization problems in
Theorem 1 are feasible with the given positive scalar ε0 = 0.0372 and the
following computed gain matrices
K = [−5.8992
−637.0308] , L =
 0.0020
0.0010

,
15

## Page 17

ACCEPTED MANUSCRIPT
ACCEPTED MANUSCRIPT
and the minimized attenuation level µ = 1.9956. For the purpose of simulation,
we assume x(0) = [0.1
−0.1]T , ˆx(0) = [−0.1
0.1]T , and ω(k) as in Exam-
ple 1. The responses of the uncontrolled system (1) and the responses of the
closed-loop system (5) in this example are illustrated in Figure 4 and Figure
5, respectively. It can be seen from Figure 4 and Figure 5 that the controlled
system (1) is robustly stable and the performance of the system has been sig-
niﬁcantly enhanced by the observer-based controller.
Now, solving the convex optimization problem in Theorem 2 via the Matlab LMI
Control Toolbox, the minimal attenuated level µ is computed as µ = 2.0214. It
can be seen that the result from Theorem 1 (µ = 1.9956) is less conservative
than the result from Theorem 2 (µ = 2.0214). This means the new approach can
provide more robust observer-based control designs compared to the traditional
H∞approach.
On the other hand, the LMI condition of Theorem 3.1 in [12] is infeasible for
the system in this example (the matrix ˜C in [12] is chosen as ˜C = [I
I]). As
mentioned earlier, the LPV approach is not suitable for the nonlinearity stud-
ied in this example. Thus, it is not suitable to apply the results in [19] to this
example.
6. Conclusion
In this paper, the robust observer-based control design problem for nonlin-
ear systems subject to disturbances in discrete-time has been studied. We have
proposed a new approach, where the observer and controller gains are computed
independently, to derive less conservative LMI control design conditions and im-
prove the robustness of control designs. Both the one-sided Lipschitz condition
and the LPV approach, which are two well-known alternatives to the traditional
Lipschitz condition, have been considered to address nonlinearities. Via two nu-
merical examples, the advantages of the new approach over the traditional H∞
approach as well as relevant works in the literature have been illustrated.
References
References
[1] G. F. Franklin, J. D. Powell, A. Emami-Naeini, Feedback Control of Dy-
namic Systems, Pearson, Upper Saddle River, 2010.
[2] H. Khalil, Nonlinear Systems, Prentice Hall, Upper Saddle River, 2002.
[3] H. Trinh, T. Fernando, Functional Observers for Dynamical Systems,
Springer, Berlin, 2012.
[4] M. Abbaszadeh, H. J. Marquez, LMI optimization approach to robust H∞
observer design and static output feedback stabilization for discrete-time
nonlinear uncertain systems, International Journal of Robust and Nonlinear
Control 19 (3) (2009) 313–340.
16

## Page 18

ACCEPTED MANUSCRIPT
ACCEPTED MANUSCRIPT
[5] S. Ahmad, M. Rehan, On observer-based control of one-sided Lipschitz
systems, Journal of the Franklin Institute 353 (4) (2016) 903–916.
[6] S. Ahmad, M. Rehan, K.-S. Hong, Observer-based robust control of one-
sided Lipschitz nonlinear systems, ISA Transactions 65 (2016) 230–240.
[7] M. Arcak, P. Kokotovic, Observer-based control of systems with slope-
restricted nonlinearities, IEEE Transactions on Automatic Control 46
(2001) 1146–1150.
[8] A. Barbata, M. Zasadzinski, H. S. Ali, H. Messaoud, Exponential observer
for a class of one-sided Lipschitz stochastic nonlinear systems, IEEE Trans-
actions on Automatic Control 60 (1) (2015) 259–264.
[9] M. Benallouch, M. Boutayeb, H. Trinh, H∞observer-based control for
discrete-time one-sided Lipschitz systems with unknown inputs, SIAM
Journal on Control and Optimization 52 (6) (2014) 3751–3775.
[10] F. Blanchini, S. Miani, Stabilization of LPV systems: state feedback, state
estimation, and duality, SIAM journal on control and optimization 42 (1)
(2003) 76–97.
[11] X. Cai, H. Gao, L. Liu, W. Zhang, Control design for one-sided Lipschitz
nonlinear diﬀerential inclusions, ISA Transactions 53 (2) (2014) 298–304.
[12] B. Grandvallet, A. Zemouche, H. Souley-Ali, M. Boutayeb, New LMI con-
dition for observer-based H∞stabilization of a class of nonlinear discrete-
time systems, SIAM Journal on Control and Optimization 51 (1) (2013)
784–800.
[13] S. Ibrir, Static output feedback and guaranteed cost control of a class of
discrete-time nonlinear systems with partial state measurements, Nonlinear
Analysis: Theory, Methods & Applications 68 (7) (2008) 1784–1792.
[14] S. Ibrir, S. Diopt, Novel LMI conditions for observer-based stabilization
of Lipschitzian nonlinear systems and uncertain linear systems in discrete-
time, Applied Mathematics and Computation 206 (2) (2008) 579–588.
[15] H. Khelouﬁ, A. Zemouche, F. Bedouhene, H. Souley-Ali, A robust H∞
observer-based stabilization method for systems with uncertain parameters
and Lipschitz nonlinearities, International Journal of Robust and Nonlinear
Control 26 (9) (2016) 1962–1979.
[16] L. Praly, M. Arcak, A relaxed condition for stability of nonlinear observer-
based controllers, Systems & control letters 53 (2004) 311–320.
[17] B. Song, J. K. Hedrick, Observer-based dynamic surface control for a class
of nonlinear systems: an LMI approach, IEEE Transactions on Automatic
Control 49 (11) (2004) 1995–2001.
17

## Page 19

ACCEPTED MANUSCRIPT
ACCEPTED MANUSCRIPT
[18] J. Song, S. He, Robust ﬁnite-time H∞control for one-sided Lipschitz
nonlinear systems via state feedback and output feedback, Journal of the
Franklin Institute 352 (8) (2015) 3250–3266.
[19] A. Zemouche, M. Boutayeb, LPV approach for the stabilization of a class
of dynamical systems, in: Proceedings of the 3rd International Conference
on Complex Systems and Applications, Le Havre, France, 2009.
[20] A. Zemouche, R. Rajamani, H. Khelouﬁ, F. Bedouhene, Robust observer-
based stabilization of Lipschitz nonlinear uncertain systems via LMIs -
discussions and new design procedure, International Journal of Robust and
Nonlinear Control 27 (11) (2017) 1915–1939.
[21] C. Bennani, F. Bedouhene, A. Zemouche, H. Bibi, A. Aitouche, A mod-
iﬁed two-step LMI method to design observer-based controller for linear
discrete-time systems with parameter uncertainties, in: Proceedings of the
6th International Conference on Systems and Control, Batna, Algeria, 2017,
pp. 279–284.
[22] G.-D. Hu, Observers for one-sided Lipschitz non-linear systems, IMA Jour-
nal of Mathematical Control and Information 23 (4) (2006) 395–401.
[23] M. Abbaszadeh, H. J. Marquez, Nonlinear observer design for one-sided
Lipschitz systems, in: Proceedings of the 2010 American Control Confer-
ence, Baltimore, USA, 2010, pp. 5284–5289.
[24] M. Benallouch, M. Boutayeb, M. Zasadzinski, Observer design for one-sided
Lipschitz discrete-time systems, Systems & Control Letters 61 (9) (2012)
879–886.
[25] M.C. Nguyen, H. Trinh, Observer design for one-sided Lipschitz discrete-
time systems subject to delays and unknown inputs, SIAM Journal on
Control and Optimization 54 (3) (2016) 1585–1601.
[26] M.C. Nguyen, H. Trinh, Reduced-order observer design for one-sided Lip-
schitz time-delay systems subject to unknown inputs, IET Control Theory
and Applications 10 (10) (2016) 1097–1105.
[27] M.C. Nguyen, H. Trinh, Unknown input observer design for one-sided Lip-
schitz discrete-time systems subject to time-delay, Applied Mathematics
and Computation 286 (2016) 57–71.
[28] W. Zhang, H. Su, F. Zhu, G. Azar, Unknown input observer design for
one-sided Lipschitz nonlinear systems, Nonlinear Dynamics 79 (2) (2015)
1469–1479.
[29] W. Zhang, H. Su, F. Zhu, S. P. Bhattacharyya, Improved exponential ob-
server design for one-sided Lipschitz nonlinear systems, International Jour-
nal of Robust and Nonlinear Control 26 (18) (2016) 3958–3973.
18

## Page 20

ACCEPTED MANUSCRIPT
ACCEPTED MANUSCRIPT
[30] M. Xu, G.-D. Hu, Y. Zhao, Reduced-order observer design for one-sided
Lipschitz non-linear systems, IMA Journal of Mathematical Control and
Information 26 (2009) 299–317.
[31] A. Zemouche, M. Boutayeb, On LMI conditions to design observers for
Lipschitz nonlinear systems, Automatica 49 (2) (2013) 585–591.
[32] M. C. Nguyen, H. Trinh, P. T. Nam, Non-linear observer design for a class
of singular time-delay systems with Lipschitz non-linearities, IMA Journal
of Mathematical Control and Information 34 (3) (2017) 919–935.
[33] S. S. Delshad, A. Johansson, M. Darouach, T. Gustafsson, Robust state
estimation and unknown inputs reconstruction for a class of nonlinear sys-
tems: Multiobjective approach, Automatica 64 (2016) 1–7.
[34] C.M. Nguyen, P.N. Pathirana, H. Trinh, Robust observer design for uncer-
tain one-sided Lipschitz systems with disturbances, International Journal
of Robust and Nonlinear Control 28 (2018) 1366–1380.
[35] M.C. Nguyen, H. Trinh, P.T. Nam, Linear functional observers with guar-
anteed ε-convergence for discrete time-delay systems with input/output
disturbances, International Journal of Systems Science 47 (13) (2016) 3193–
3205.
[36] M. Darouach, L. Boutat-Baddas, M. Zerrougui, H∞observers design for a
class of nonlinear singular systems, Automatica 47 (11) (2011) 2517–2525.
19

## Page 21

ACCEPTED MANUSCRIPT
ACCEPTED MANUSCRIPT
0
10
20
30
40
50
Time [sec]
-0.1
-0.05
0
0.05
0.1
Figure 1: The disturbance ω.
0
10
20
30
40
50
Time [sec]
-0.8
-0.6
-0.4
-0.2
0
0.2
0.4
0.4
x1
x2
x3
x4
Figure 2: The responses of the uncontrolled system (1) in Example 1.
20

## Page 22

ACCEPTED MANUSCRIPT
ACCEPTED MANUSCRIPT
0
10
20
30
40
50
Time [sec]
-0.8
-0.6
-0.4
-0.2
0
0.2
0.4
0.4
x1
x2
x3
x4
Figure 3: The responses of the controlled system (5) in Example 1.
0
10
20
30
40
50
Time [sec]
-0.8
-0.6
-0.4
-0.2
0
0.2
x1
x2
Figure 4: The responses of the uncontrolled system (1) in Example 2.
21

## Page 23

ACCEPTED MANUSCRIPT
ACCEPTED MANUSCRIPT
0
10
20
30
40
50
Time [sec]
-0.6
-0.4
-0.2
0
0.2
0.4
0.6
x1
x2
Figure 5: The responses of the controlled system (5) in Example 2.
22
