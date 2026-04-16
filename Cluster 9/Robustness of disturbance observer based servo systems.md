# Robustness of disturbance observer based servo systems.pdf

## Page 1

IFAC PapersOnLine 56-2 (2023) 11570–11577
ScienceDirect
Available online at www.sciencedirect.com
2405-8963 Copyright © 2023 The Authors. This is an open access article under the CC BY-NC-ND license.
Peer review under responsibility of International Federation of Automatic Control.
10.1016/j.ifacol.2023.10.454
Copyright © 2023 The Authors. This is an open access article under the CC BY-NC-ND license 
(https://creativecommons.org/licenses/by-nc-nd/4.0/)
A disturbance observer is a control mechanism that esti-
mates disturbances and cancels their eﬀects. Ohishi et al.
(1983) proposed a disturbance observer as a combination
of the inverse system of the plant and a low pass ﬁlter.
Johnson (1971) proposed a Luenbergar observer-based
disturbance observer, which is an observer for an aug-
mented system including a disturbance generating model.
Independently of the above proposals, a new type of ob-
server called the Proportional-Integral (PI) observer was
proposed (Kaczorek, 1979). The PI observer includes an
additional integral path in the conventional observer and
is one of the higher-order controllers (Weinmann, 1991;
Bakhshande and S¨oﬀker, 2015). The disturbance observer
is regarded as a special case of the PI observer. Shafai
and Carroll (1985) proposed the design method of the PI-
observer for the time-varying multivariable systems, then
Beale and Shafai (1989) proposed the design method of
the PI-observer-based robust controller against the plant
parameter variations. Furthermore, Ohnishi et al. (1996)
proposed a structure of the servo controller with the
Luenbergar-based disturbance observer. These controllers
cancel out the eﬀect of the disturbance with the feedback
inputs of the estimated value.
The disturbance observers have a simple structure, and
they easily improve the robustness of the servo perfor-
mance. Therefore, disturbance observers are widely used
for practical applications, especially in the robotics ﬁeld.
⋆This work was supported by JSPS KAKENHI Grant Number
JP22H01512.
1. INTRODUCTION
Furthermore, servo controller design methods with distur-
bance observers have been intensively studied. For exam-
ple, Apte et al. (2020) applied disturbance observers for
robust speed control design against permanent magnet
synchronous motors. Liu et al. (2021) proposed to combine
a disturbance observer and a neural network controller
for the trajectory tracking controller design against the
aircraft with model parameter uncertainties and unknown
disturbances. Furthermore, a design method to obtain
the state feedback gain and observer gain by solving the
BMI problem based on the H∞norm was also proposed
by Do et al. (2020). However, the eﬀectiveness has yet
to be theoretically proved. Sariyildiz and Ohnishi (2015)
investigated the stability and robustness of the controllers
with inverse model-based disturbance observers. Beale and
Shafai (1989) discussed the robustness of the PI observers,
but only from the viewpoint of the loop transfer recovery
and not from the perspective of the variation of time
responses. Furthermore, Mita et al. (1998) claimed that
disturbance observers do not bring any advantage from
the viewpoint of servo system design compared to the H∞
control theory. Ogawa et al. (1993) showed that control
systems with disturbance observers can be constructed
from the general form of a two-degree-of-freedom (2-DOF)
controller using the coprime factorization.
This paper aims to clarify the advantage of disturbance
observers for the servo system with a servo compensator
and a disturbance observer. Such a structure is referred
to as the “disturbance-observer-based control system.”
This paper clariﬁes the robustness of disturbance-observer-
based controllers and the underlying reasons for the ro-
bustness. Speciﬁcally, this paper theoretically shows that
Keywords: Robust controller synthesis, Robustness analysis, Observers for linear systems,
Disturbance observer.
Abstract: This paper gives a theoretical analysis of the robustness of servo systems with
disturbance observers. The disturbance observers have been used as an easy way to enhance
the robustness of servo systems because of their simple structure. However, the eﬀectiveness
has yet to be theoretically proved. Therefore, this paper aims to clarify the advantage of the
disturbance observer. This paper considers the servo system consisting of a servo compensator
and a disturbance observer. The servo system has robustness in suppressing the response
variations against the system uncertainties. It is theoretically shown that the robustness comes
from the systems having zeros of multiplicity two at s = 0, while the systems are type-1 servo
systems. A numerical example is provided to conﬁrm the theoretical result and to demonstrate
the eﬀectiveness of disturbance observers.
∗Kyushu Institute of Technology, Japan
(e-mail: shikada.kana104@mail.kyutech.jp)
∗∗Kyushu Institute of Technology, Japan
(e-mail: sebe@ics.kyutech.ac.jp)
∗∗∗Kumamoto University, Japan
(e-mail: sato.masayuki@mech.kumamoto-u.ac.jp)
Kana Shikada ∗Noboru Sebe ∗∗Masayuki Sato ∗∗∗
Robustness of disturbance observer based
servo systems ⋆

## Page 2

Kana Shikada  et al. / IFAC PapersOnLine 56-2 (2023) 11570–11577	
11571
r
1
s
Kp
−
Ki
u
kg
up P(s)
yp
−
−
disturbance observer
Cp
ˆxp
1
s I2
Ap
Bp
Lx
Ld
1
s
Ad
ˆxd
Cd
−
d
Fig. 1. Servo system with additional disturbance observer
0
1
2
3
4
Time
0
0.2
0.4
0.6
0.8
1
1.2
Outputs
Fig. 2. Step responses without disturbance observer
the disturbance-observer-based control systems are type-1
servo systems, although they have double integrators in
the closed-loop systems. On the other hand, the transfer
function from disturbance to tracking error has zeros of
multiplicity two at s = 0 in the complex plane, which leads
to suppressing the variation of step response against the
uncertainties. This is the robustness that the disturbance-
observer-based control systems have. A numerical example
is also provided to conﬁrm the theoretical results and
to demonstrate the eﬀectiveness of the above discussion.
The simultaneous design of feedback and observer gains
can suppress the variation of the time response. However,
the numerical example also shows that the disturbance-
observer-based controller does not improve the rise time of
the step response, i.e., the control performance in tracking
performance.
Notations: The symbol R and C denote the sets of real
and complex numbers, respectively. The identity matrix of
size n is denoted by In, and the zero matrix of size m × n
is denoted by Om×n. The zero matrices are occasionally
denoted by O without the size. In general, signals are
functions of time t. However, we do not explicitly describe
they are functions of t for the sake of simplicity.
2. ADVANTAGES AND DISADVANTAGES OF
ADDING DISTURBANCE OBSERVER
This section brieﬂy reviews the advantages and disadvan-
tages of adding a disturbance observer to a servo system
through a numerical example. The considered servo sys-
0
1
2
3
4
Time
0
0.2
0.4
0.6
0.8
1
1.2
Outputs
Fig. 3. Step responses with disturbance observer
10 -1
10 0
10 1
10 2
10 3
-40
-35
-30
-25
-20
-15
-10
-5
0
5
Magnitude (dB)
Frequency  (rad/s)
Fig. 4. Magnitude plot of closed-loop system from d to u
tem is shown in Fig. 1, and the main servo controller is
constructed by a PI controller, whose gains are Kp and
Ki. As shown in Fig. 1, an additional disturbance observer
is attached to the PI servo system. Here, we show changes
in control characteristics when a disturbance observer is
added to the servo system with a PI controller. In Fig. 1,
P(s) represents the plant to be controlled, and its state-
space coeﬃcient matrices are given as follows:
[
Ap Bp
Cp
]
=


−1 −3 1
3 −3 3
−1
3

.
The signals d ∈R and u ∈R are used to evaluate
the robustness against the multiplicative uncertainty. The
parameter kg denotes the input-side gain perturbation of
the plant. The integral and proportional gains of the PI
controller are set to Kp = 2 and Ki = 5, respectively. The
disturbance observer is constructed with the observer gain
L = [4 14 100]T. (The deﬁnition of disturbance observer is
given in Section 3.) Figures 2 and 3 show the step responses
with and without the disturbance observer, respectively.
The step responses are shown for control input gains of
kg = 0.5, 1, 2. As shown in Fig. 3, the variations of the step
responses are suppressed against the uncertainties. Figure
4 shows the magnitude plots of the closed-loop systems
from d to u with kg = 1, with which we can examine
the robustness to the input-side multiplicative uncertainty.
The servo system with the disturbance observer has a
considerably large maximum gain. Therefore, it indicates

## Page 3

11572	
Kana Shikada  et al. / IFAC PapersOnLine 56-2 (2023) 11570–11577
r
e
1
s Im
ζ
Kx
Kζ
u
up P(s)
yp
−
−
standard observer
Cp
ˆxp
1
s In
Ap
Bp
Lx
d
Fig. 5. Servo system with standard observer-based con-
troller
r
e
1
s Im
ζ
Kx
Kζ
u
up P(s)
yp
−
−
disturbance observer
Cp
ˆxp
1
s In
Ap
Bp
Lx
Ld
1
s Im
Ad
ˆxd
Cd
−
d
Fig. 6. Servo system with disturbance-observer-based con-
troller
that the attached disturbance observer deteriorates the
robustness in the general sense. This disadvantage was
induced because the interaction between the disturbance
observer and the original controller was not appropriately
incorporated when designing them.
This paper theoretically clariﬁes the reason why the vari-
ations of time responses are suppressed with disturbance
observers. Furthermore, the numerical examples show that
the simultaneous design of feedback and observer gains can
suppress the variations in time responses.
3. CHARACTERISTIC ANALYSIS OF SERVO
SYSTEM WITH DISTURBANCE OBSERVER
3.1 Problem settings
This paper considers servo systems with observer-based
controllers. The overall servo systems are shown in Figs. 5
and 6. In these ﬁgures, P(s) denotes a given plant, and
its state-space representation is given by
˙xp = Apxp + Bpup,
(1a)
yp = Cpxp.
(1b)
The signals d ∈Rℓ, r ∈Rm, e = r −yp ∈Rm and ζ ∈Rm
are the disturbance, the reference input, the tracking error,
and the state of the servo compensator, respectively. The
gains Kx ∈Rℓ×n and Kζ ∈Rℓ×m are the state feedback
gain and the integral gain, respectively.
Assumption 1. The numbers of control inputs and mea-
surement outputs are the same, i.e., ℓ= m.
Assumption 2. The given plant (1) has no zero at s = 0.
Assumption 3. The matrix Ap of the plant (1) has no
zero eigenvalues.
Assumption 4. The pair (Ap, Bp) is stabilizable.
Assumption 5. The pair (Cp, Ap) is detectable.
Assumption 2 is required to construct a servo system, and
Assumptions 4 and 5 are necessary to stabilize the given
plant. On the other hand, Assumption 3 is a technical
assumption, and this paper only deals with the systems
satisfying Assumption 3.
This paper considers a servo system for a step reference
signal. Therefore, the state transition matrix of the servo
compensator is Ai = Om×m, and its state equation is given
as follows:
˙ζ = Aiζ + r −yp.
(2)
The augmented system with the servo compensator (2)
added to the plant (1) is given as follows:
[ ˙xp
˙ζ
]
=
[
Ap
O
−Cp Ai
] [
xp
ζ
]
+
[
Bp O
O Im
] [
u
r
]
.
(3)
From Assumptions 2 and 4, the augmented system (3) is
stabilizable.
Standard observer
The state equation of the full-order
observer constructed for the plant (1) is given as follows:
˙ˆxp = (Ap + LxCp)ˆxp + [ −Lx Bp ]
[
yp
u
]
,
(4)
where Lx ∈Rn×m is the observer gain. The standard
observer is referred to in Section 4 for comparison with
the disturbance observer.
Disturbance observer (Johnson, 1971)
Assume that the
disturbance d is generated by the following linear dynam-
ical model:
˙xd = Adxd,
(5a)
d = Cdxd,
(5b)
where (Cd, Ad) is detectable. A disturbance observer is an
observer for the augmented system consisting of the given
plant (1) and the disturbance generating model (5). The
augmented system is expressed as follows:
[
˙xp
˙xd
]
=
[
Ap BpCd
O
Ad
] [
xp
xd
]
+
[
Bp
O
]
u,
(6a)
yp = [ Cp O ]
[
xp
xd
]
.
(6b)
From Assumptions 2 and 5, the augmented system (6) is
detectable.
Let ˆxp ∈Rn and ˆxd ∈Rm be the estimated states of the
plant (1) and the disturbance (5), respectively, and the
state equation of the disturbance observer is expressed as
[ ˙ˆxp
˙ˆxd
]
=
[
Ap BpCd
O
Ad
][
ˆxp
ˆxd
]
+
[
Bp
O
]
u +
[
Lx
Ld
]
(Cpˆxp −yp)
=
[
Ap + LxCp BpCd
LdCp
Ad
][
ˆxp
ˆxd
]
+
[
−Lx Bp
−Ld O
][
yp
u
]
, (7)
where Ld ∈Rm×m is the observer gain concerning the
disturbance generating model. The control system shown
in Fig. 6 includes a feedback to cancel out the disturbance
estimated by the disturbance observer. In this paper,
following Meditch and Hostetter (1973); Ohnishi et al.
(1996), the disturbance is assumed to be a step signal,
and accordingly, Ad = Om×m and Cd = Im. This type of
disturbance observers have minor loops with integrators

## Page 4

Kana Shikada  et al. / IFAC PapersOnLine 56-2 (2023) 11570–11577	
11573
structurally regardless of the plant models (Shikada and
Sebe, 2023).
3.2 Poles of the closed-loop system
In the control system shown in Fig. 6, the servo compen-
sator is combined with the disturbance observer. There-
fore, there are two integrators, the servo compensator Ai
and the disturbance generating model Ad. In this case,
there are concerns about the servo system: i) The servo
system is to be a type-2 servo system, and ii) the two
integrators are uncontrollable or unobservable and not
internally stabilized. This subsection shows that these
problems do not arise.
The state-space representation of the closed-loop system
shown in Fig. 6 is represented as follows:


˙xp
˙ζ
˙ˆxp
˙ˆxd

=


Ap
BpKζ
BpKx
−BpCd
−Cp
Ai
O
O
−LxCp BpKζ Ap + BpKx + LxCp
O
−LdCp
O
LdCp
Ad




xp
ζ
ˆxp
ˆxd


+


O Bp
Im O
O
O
O
O


[
r
d
]
,
(8a)
[
yp
e
]
=
[
Cp
O O O
−Cp O O O
]


xp
ζ
ˆxp
ˆxd

+
[
O O
Im O
] [
r
d
]
.
(8b)
By applying the state transformation ˆxp →ˆxe = ˆxp −
xp to the representation (8), the following expression is
obtained:


˙xp
˙ζ
˙ˆxe
˙ˆxd

=


Ap + BpKx BpKζ
BpKx
−BpCd
−Cp
Ai
O
O
O
O
Ap + LxCp
BpCd
O
O
LdCp
Ad




xp
ζ
ˆxe
ˆxd


+


O
Bp
Im
O
O −Bp
O
O


[
r
d
]
,
(9a)
[
yp
e
]
=
[
Cp
O O O
−Cp O O O
]


xp
ζ
ˆxe
ˆxd

+
[
O O
Im O
] [
r
d
]
.
(9b)
From the representation (9), similar to the ordinary
observer-based control systems, the state of the distur-
bance observer [ˆxT
e ˆxT
d ]T is uncontrollable from r, and the
dynamics of the disturbance observer does not appear in
the transfer function from r to yp. In other words, the
dynamics from r to yp is determined by the upper left
2 × 2 block of the matrix in (9a) and is that of a type-1
servo system. For this reason, the tracking performance,
such as the faster response, is identical to the standard
observer-based controller and is not improved. On the
other hand, the dynamics of the disturbance observer is
characterized by the lower right 2 × 2 block of the matrix
in (9a). The closed-loop systems corresponding to the left
upper and right lower 2×2 block matrices are stabilized by
the feedback gains Kx and Kζ, and by the observer gains
Lx and Ld, respectively.
3.3 Zeros of the closed-loop system
Let xcl = [xT
p ζT ˆxT
e ˆxT
d ]T ∈Rncl be the state of the closed-
loop system (9), then the state-space representation of the
closed-loop system from d to e is given as follows:
˙xcl = Aclxcl + Bcld,
(10a)
e = Cclxcl + Dcld,
(10b)
where the matrices Acl ∈Rncl×ncl, Bcl ∈Rncl×m, Ccl ∈
Rm×ncl and Dcl = Om×m are the state-space matrices of
the closed-loop system from d to e.
The following theorem holds for the structure of zeros of
the closed-loop system (10).
Theorem 1. Suppose that the system (10) is stabilized by
Kx, Kζ, Lx and Ld. Then, the transfer function from d to
e of the closed-loop system (10) has m zeros of multiplicity
two at s = 0.
Proof. As shown in Proposition 1 in Appendix A, the
zeros of the system are characterized by the Rosenbrock
system matrix. First, we show that the closed-loop system
(10) has m zeros at s = 0. Let the matrices V11 and V12
be V11 = [O O O Im]T ∈Rncl×m and V12 = Im. Then,
remember that Ad = Om×m and Cd = Im, we have
[
Acl Bcl
Ccl Dcl
][
V11
V12
]
=


Ap + BpKx BpKζ
BpKx
−BpCd
Bp
−Cp
Ai
O
O
O
O
O
Ap + LxCp
BpCd
−Bp
O
O
LdCp
Ad
O
−Cp
O
O
O
O




O
O
O
Im
Im

=


O
O
O
O
O

.
(11)
The equation (11) implies that the system (10) has m
zeros at s = 0 and the corresponding zero vectors are the
columns of [V T
11 V T
12]T.
Next, we show that each zero at s = 0 is of multiplicity
two. If the multiplicities of the zeros are two, there exists
a matrix V2 ∈C(ncl+m)×m such that (12) holds.
[
Acl Bcl
Ccl Dcl
]
V2 =
[
V11
O
]
.
(12)
If the matrix V2 which satisﬁes the equation (12) exists,
each column is a zero vector corresponding to a zero of
multiplicity two. However, it is diﬃcult to construct V2
satisfying (12). Therefore, we show that the equation (12)
has a solution by showing that the equation (13) holds.
rank
[
Acl Bcl
Ccl Dcl
]
= rank
[
Acl Bcl V11
Ccl Dcl O
]
.
(13)
The left side of (13) is given as
rank


Ap + BpKx BpKζ
BpKx
−BpCd
Bp
−Cp
Ai
O
O
O
O
O
Ap + LxCp
BpCd
−Bp
O
O
LdCp
Ad
O
−Cp
O
O
O
O

. (14)
Remember that Ai = Om×m, subtracting the second row
from the ﬁfth row, (14) is equal to
rank


Ap + BpKx BpKζ
BpKx
−BpCd
Bp
−Cp
Ai
O
O
O
O
O
Ap + LxCp
BpCd
−Bp
O
O
LdCp
Ad
O
O
O
O
O
O

. (15)

## Page 5

11574	
Kana Shikada  et al. / IFAC PapersOnLine 56-2 (2023) 11570–11577
Since the closed-loop system (10) is stable, the matrix in
the upper left 4 × 4 block of the matrix in (15) has no
zero eigenvalues. Therefore, (15) is equal to ncl. The same
procedures lead to the right hand side of (13) is equal to
rank


Ap + BpKx BpKζ
BpKx
−BpCd
Bp
O
−Cp
Ai
O
O
O
O
O
O
Ap + LxCp
BpCd
−Bp O
O
O
LdCp
Ad
O
Im
O
O
O
O
O
O

.
(16)
The rank (16) is ncl for the same reason as (15). Therefore,
the equation (13) holds.
2
In the case of the servo systems with standard observers,
the transfer function from d to e has zeros of multiplicity
one at s = 0. Contrarily, as shown by Theorem 1, with
disturbance observers, the transfer function from d to e
has zeros of multiplicity two at s = 0. This fact implies
that the disturbance observer reduces the gain of the
transfer function in the low frequency range. As claimed by
Meditch and Hostetter (1973); Ohnishi et al. (1996), the
signal d represents not only the originally modeled distur-
bance but also the signal variation caused by uncertainties.
Therefore, the disturbance observer reduces the eﬀect of
uncertainties. Note that Theorem 1 also implies that the
transfer function from d to yp has zeros of multiplicity two
at s = 0.
4. NUMERICAL EXAMPLE
In this numerical example, two servo systems are con-
structed against a third-order system. One is with a stan-
dard observer-based controller, and the other is with a
disturbance-observer-based controller, which are the 2-
DOF versions of controllers shown in Figs. 5 and 6, re-
spectively. The controllers are designed based on the multi-
model design approach (Ackermann, 1985) by hinfstruct()
in MATLAB
®.
4.1 Problem settings
The matrices of the state-space representation of the plant
are given as follows:
[
Ap Bp
Cp
]
=


6 −4
0 0
6
1 −9 0
−8 −5
2 2
3
0
0

.
This numerical example considers the uncertainty (gain
ﬂuctuation) at the control input. Let δ be the gain ﬂuc-
tuation, and its magnitude is set to |δ| = 0.8. The con-
trollers, i.e., the feedback and observer gains, are designed
to minimize the worst H∞norms of the two systems
corresponding to the uncertainties δ = ±0.8.
The generalized plants used in the controller designs are
shown in Figs. 7 and 8, where the parameter kg denotes
the control input gain kg = 1+δ. The parameters α and β
are the parameters of the servo weight function. The pa-
rameter α speciﬁes the vibration suppression performance,
and the parameter β speciﬁes the rise time of the time
response. This numerical example sets these parameters
to α = 0.9 and β = 0.3. The input signal w1 is the input
disturbance corresponding to d in Figs. 5 and 6, and its
r
e
α
β
z1
wu
z2
1
s
ζ
Kx
Kζ
Kr
u
kg
P(s)
−
−
standard observer
Cp
ˆxp
1
s I3
Ap
Bp
Lx
w1 wd d
w2 wo
Fig. 7. Generalized plant for standard observer-based
controller design
r
e
α
β
z1
wu
z2
1
s
ζ
Kx
Kζ
Kr
u
kg
P(s)
−
−
disturbance observer
Cp
ˆxp
1
s I3
Ap
Bp
Lx
Ld
1
s
Ad
ˆxd
Cd
−
w1 wd d
w2 wo
Fig. 8. Generalized plant for disturbance-observer-based
controller design
magnitude is wd = 0.07. The output signal z2 evaluates the
magnitude of the control input, and its weight is wu = 0.1.
Also, the input signal w2 is an output disturbance, and its
magnitude is wo = 10−4. This output disturbance is added
to prevent the absolute values of the observer poles from
becoming excessively large.
4.2 Design results
The controllers are designed based on the multi-model
approach and minimize the H∞norm of the worst-case
models with uncertainties of δ = ±0.8. Let Kr ∈R be
the feed-forward gain. As a result, the following gains are
obtained for the standard observer-based controller.
[Kr Kζ] =
[
1.7518 1.0649 × 102 ]
,
Kx =
[
−1.3845 × 103 6.9148 × 102 −3.6325 × 102 ]
,
Lx =
[
2.9070 × 103 −1.8634 × 104 4.3660 × 105 ]T .
Similarly, the gains for the disturbance-observer-based
controller are obtained as follows:
[Kr Kζ] = [ 2.4688 6.1468 × 10 ] ,
Kx =
[
−1.0022 × 103 5.5966 × 102 −3.8035 × 102 ]
,
Ld = 4.3958 × 105,
Lx =
[
1.3594 × 103 −1.0549 × 104 2.0637 × 105 ]T .
The achieved H∞norms by the designed two controllers
are 0.9752 and 0.9745, respectively, and are almost identi-
cal. Let Ted(s) be the nominal transfer function from d to

## Page 6

Kana Shikada  et al. / IFAC PapersOnLine 56-2 (2023) 11570–11577	
11575
0
5
10
15
Time
0
0.2
0.4
0.6
0.8
1
1.2
Outputs
Fig. 9. Step responses with standard observer-based con-
troller
0
5
10
15
Time
0
0.2
0.4
0.6
0.8
1
1.2
Outputs
Fig. 10. Step responses with disturbance-observer-based
controller
e. The transfer function Ted(s) with the standard observer-
based controller is obtained as follows:
Ted(s) =
−216s
(s + 8690)(s + 707.2)(s + 0.5274)
×
(s + 697.2)(s + 8690)(s + 51.34)
(s2 + 9.786s + 61.67)(s2 + 22.11s + 5332).
(17)
Similarly, the transfer function Ted(s) with the disturbance-
observer-based controller is obtained as follows:
Ted(s) =
−216s2
(s + 4042)(s + 745.4)(s + 4.43)(s + 0.3992)
×
(s + 743.7)(s + 4043)(s + 52.58)
(s2 + 5.908s + 44.62)(s2 + 22.52s + 5302).
(18)
The transfer function (18) shows that the closed-loop
system with the disturbance-observer-based controller has
a zero of multiplicity two at s = 0, while the transfer
function (17) with the standard observer-based controller
has a zero of multiplicity one at s = 0.
Figures 9 and 10 show the step responses with the two
types of observers. In each simulation, the uncertainty
δ is set to δ = 0, ±0.8．As shown in Figs. 9 and 10,
the variations of the outputs of the servo system with
10-2
10-1
100
101
102
-120
-100
-80
-60
-40
-20
0
10
Magnitude (dB)
Frequency  (rad/s)
Fig. 11. Magnitude plot of the system from r to e
10-2
10-1
100
101
102
-120
-100
-80
-60
-40
-20
0
10
Magnitude (dB)
Frequency  (rad/s)
Fig. 12. Magnitude plot of the system from d to e
10-2
10-1
100
101
102
-120
-100
-80
-60
-40
-20
0
10
Magnitude (dB)
Frequency  (rad/s)
Fig. 13. Magnitude plot of the diﬀerence between the
nominal and perturbed systems G(s, δ) −G(s, 0)
the disturbance observer are smaller than those with the
standard observer.
Remark 1. Note that the step responses in Fig. 10 almost
coincide with the slowest step response in Fig. 9. This
implies that there is no performance improvement, such
as faster responses. Only the variation in step responses
is reduced. More precisely, the disturbance-observer-based
controller suppresses the response variations by slowing
down the faster responses of δ = 0 and 0.8.

## Page 7

11576	
Kana Shikada  et al. / IFAC PapersOnLine 56-2 (2023) 11570–11577
Figure 11 shows the magnitude plots of the systems from
r to e with the standard and disturbance observer-based
controllers. The gain ﬂuctuation δ is set to δ = 0, ±0.8.
All of them have slopes of 20 [dB/dec] at low frequencies,
which conﬁrms that the closed-loop systems are type-1
servo systems.
Figure 12 shows the magnitude plots of the systems
from d to e with the standard and disturbance observer-
based controller with the same gain ﬂuctuation values
as in Fig. 11. Contrarily to Fig. 11, the slopes of the
plots are 20 [dB/dec] for the systems with the standard
observer-based controller, and 40 [dB/dec] for the systems
with the disturbance-observer-based controller at the low
frequencies. This is because these two closed-loop systems
have zeros at s = 0 with diﬀerent multiplicities, as shown
in Section 3.
In order to evaluate the variations of the step responses,
let us deﬁne G(s, δ) as the closed-loop transfer function
from r to yp with the uncertainty δ. Since the closed-loop
systems with the standard and disturbance observers are
type-1 servo systems, the ordinary sensitivity functions
of both closed-loop systems have slopes of 20 [dB/dec].
Therefore, the ordinary sensitivity function is inadequate
for evaluating the robustness of the 2-DOF control sys-
tems. Instead of the ordinary sensitivity function, this
paper evaluates the diﬀerence G(s, δ) −G(s, 0) to clarify
the eﬀect of the disturbance observer on the variations
of the closed-loop systems caused by the uncertainties.
Figure 13 shows the magnitude plots of the diﬀerence
G(s, δ) −G(s, 0). These plots show that the servo systems
with the standard observer-based controllers have slopes of
20 [dB/dec] in the low-frequency range, whereas the servo
systems with the disturbance-observer-based controllers
have slopes of 40 [dB/dec] in the low-frequency range.
These are provoked by the frequency characteristics at
the low-frequency range as shown in Fig. 12. It indicates
that the eﬀect of the uncertainty is suppressed in the
low-frequency range. Furthermore, the diﬀerence in the
magnitude at low frequencies indicates the diﬀerence in the
robustness against the uncertainty. This diﬀerence shows
why the disturbance observers suppress the variations of
the step responses more eﬃciently.
5. CONCLUSION
This paper investigates the robust control performance of
disturbance observers and clariﬁes the theoretical reason
for the eﬀectiveness of disturbance observers. The control
system with a disturbance observer has zeros of multi-
plicity two at s = 0 in the transfer function from the
disturbance to the output while maintaining the type-
1 servo characteristics from the reference inputs to the
outputs. These double zeros improve the robustness at
the low frequencies and suppress the variation of the step
responses against the uncertainties.
Our future work is to propose a more practical design
procedure for disturbance observers. Since there should
be a trade-oﬀbetween the general tracking performance
and the robustness of the response variations, a design
procedure that considers such a trade-oﬀis required for
practical use.
REFERENCES
Ackermann, J. (1985). Multi-model approaches to robust
control system design.
IFAC Proceedings Volumes,
18(3), 1–6.
Apte, A., Joshi, V.A., Mehta, H., and Walambe, R.
(2020). Disturbance-Observer-Based Sensorless Control
of PMSM Using Integral State Feedback Controller.
IEEE Transactions on Power Electronics, 35(6), 6082–
6090.
Bakhshande, F. and S¨oﬀker, D. (2015).
Proportional-
integral-observer: A brief survey with special attention
to the actual methods using ACC benchmark. IFAC-
PapersOnLine, 48(1), 532–537.
8th Vienna Interna-
tional Conferenceon Mathematical Modelling.
Beale, S. and Shafai, B. (1989). Robust control system de-
sign with a proportional integral observer. International
Journal of Control, 50(1), 97–111.
Do, M.-H., Koenig, D., and Theilliol, D. (2020). Robust
H∞proportional-integral observer-based controller for
uncertain LPV system. Journal of the Franklin Institute,
357(4), 2099–2130.
Gantmacher, F. (ed.) (1989).
The Theory of Matrices.
Chelsea Publishing Company.
Johnson, C. (1971).
Accomodation of external distur-
bances in linear regulator and servomechanism prob-
lems. IEEE Transactions on Automatic Control, 16(6),
635–644.
Kaczorek, T. (1979). Proportional-integral observers for
linear multivariable time-varying systems.
Automa-
tisierungstechnik, 27(1-12), 359–363.
Liu, S., Whidborne, J.F., and Chumalee, S. (2021). Distur-
bance Observer Enhanced Neural Network LPV Control
for a Blended-Wing-Body Large Aircraft. IEEE Trans-
actions on Aerospace and Electronic Systems, 57(5),
2689–2703.
Meditch, J.S. and Hostetter, G.H. (1973). Observers for
systems with unknown and inaccessible inputs. In 1973
IEEE Conference on Decision and Control including the
12th Symposium on Adaptive Processes, 120–124.
Mita, T., Hirata, M., Murata, K., and Zhang, H. (1998).
H∞control versus disturbance-observer-based control.
IEEE Trans. Ind. Electron., 45, 488–495.
Ogawa, T., Suzuki, T., Matsumoto, K., Okuma, S.,
Kamiyama, K., and Ohno, K. (1993). Internal struc-
ture of two-degree-of-freedom controller and its applica-
tion to vibration suppression control. In IECON ’93 -
19th Annual Conference of IEEE Industrial Electronics,
2138–2143 vol.3.
Ohishi, K., Ohnishi, K., and Miyachi, K. (1983). Torque-
speed regulation of DC motor based on load torque
estimation method. In JIEE/1983 International power
electronics conference (IPEC), 1209–1218.
Ohnishi, K., Shibata, M., and Murakami, T. (1996). Mo-
tion control for advanced mechatronics. IEEE/ASME
Transactions on Mechatronics, 1(1), 56–67.
Sariyildiz, E. and Ohnishi, K. (2015).
Stability and
robustness of disturbance-observer-based motion control
systems. IEEE Transactions on Industrial Electronics,
62(1), 414–422.
Shafai,
B.
and
Carroll,
R. L.
(1985).
Design
of
proportional-integral observer for linear time-varying
multivariable systems.
In 24th IEEE Conference on
Decision and Control, 597–599.

## Page 8

Kana Shikada  et al. / IFAC PapersOnLine 56-2 (2023) 11570–11577	
11577
Shikada, K. and Sebe, N. (2023). Relation between dis-
turbance observer and model error compensator.
In
2023 SICE International Symposium on Control Sys-
tems (SICE ISCS). 6 pages.
Weinmann, A. (1991).
Uncertain Models and Robust
Control. Springer Vienna.
The MathWorks, Inc (2022). MATLAB. URL https://
www.mathworks.com/products/matlab.html. (Version
2022a).
Appendix A. STRUCTURE OF ZEROS
Let a given system be
˙x = Ax + Bu,
(A.1a)
y = Cx + Du,
(A.1b)
where x ∈Rn, u ∈Rm and y ∈Rm are the state, input and
output of the system, respectively. For the system (A.1),
the matrix
[
A −sIn B
C
D
]
(A.2)
is called the Rosenbrock system matrix of system (A.1).
Proposition 1. (Gantmacher, 1989). For a Rosenbrock
system matrix (A.2), there exist non-singular matrices P,
Q ∈C(n+m)×(n+m), a nonnegative integer r, a Jordan ma-
trix Λ ∈C(n−r)×(n−r) and a nilpotent N ∈C(r+m)×(r+m)
such that
P
[
A −sIn B
C
D
]
Q =
[
Λ −sIn−r
O
O
Ir+m −sN
]
(∀s ∈C).
(A.3)
Let us decompose Q as
Q =
[
Q11 Q12
Q21 Q22
]
,
(A.4)
where Q11 ∈Cn×(n−r), Q12 ∈Cn×(r+m), Q21 ∈Cm×(n−r)
and Q22 ∈Cm×(r+m). Then,
[
A B
C D
] [
Q11
Q21
]
=
[
Q11
O
]
Λ
(A.5)
holds. This equation represents the multiplicity structure
of the ﬁnite zeros of system (A.1).
