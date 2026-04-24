# Disturbance observer-based control of UAVs with prescribed performance.pdf

## Page 1

International Journal of Systems Science
ISSN: 0020-7721 (Print) 1464-5319 (Online) Journal homepage: www.tandfonline.com/journals/tsys20
Disturbance observer-based control of UAVs with
prescribed performance
Kazuya Sasaki & Zi-Jiang Yang
To cite this article: Kazuya Sasaki & Zi-Jiang Yang (2020) Disturbance observer-based control
of UAVs with prescribed performance, International Journal of Systems Science, 51:5, 939-957,
DOI: 10.1080/00207721.2020.1746436
To link to this article:  https://doi.org/10.1080/00207721.2020.1746436
Published online: 07 Apr 2020.
Submit your article to this journal 
Article views: 480
View related articles 
View Crossmark data
Citing articles: 13 View citing articles 
Full Terms & Conditions of access and use can be found at
https://www.tandfonline.com/action/journalInformation?journalCode=tsys20

## Page 2

INTERNATIONAL JOURNAL OF SYSTEMS SCIENCE
2020, VOL. 51, NO. 5, 939–957
https://doi.org/10.1080/00207721.2020.1746436
Disturbance observer-based control of UAVs with prescribed performance
Kazuya Sasaki and Zi-Jiang Yang
Department of Mechanical Systems Engineering, College of Engineering, Ibaraki University, Hitachi, Japan
ABSTRACT
This work proposes a novel robust nonlinear control method for trajectory tracking of a quadrotor
unmanned aerial vehicle using the prescribed performance control technique and disturbance
observers, in the presence of external disturbances and uncertainties of physical parameters. By
exploiting the cascaded structure of the position subsystems and the attitude subsystems, the con-
troller is designed in a backstepping manner, and the dynamic surface technique is adopted to avoid
the explosion of the controller complexity. For each axis of the subsystem with uncertainties, the pre-
scribed performance control technique is adopted to ensure a moderate control performance. Then
a disturbance observer is constructed to enhance the corresponding controller to achieve a suffi-
ciently small ultimate error. Not only the control performance of the overall control system, but also
the behaviour of all the internal error signals are analysed rigorously. Finally, the performance of the
proposed controller is confirmed by simulation studies.
ARTICLE HISTORY
Received 8 February 2019
Accepted 18 March 2020
KEYWORDS
Quadrotor; prescribed
performance control;
backstepping; dynamic
surface control; disturbance
observer
1. Introduction
Recent years have witnessed increasing research
activities of small-scale helicopters, because of their
extensive applications. Quadrotor unmanned aerial
vehicles (UAVs) enjoy the advantages of flying in any
direction, taking off and landing vertically, and hov-
ering at a desired altitude (Carrillo et al., 2013; Non-
ami et al., 2010). However, the quadrotor is a typical
underactuated, nonlinear coupled system and may suf-
fer from the inevitable unmodelled dynamics, aero-
dynamic disturbances and parameters’ perturbation
which may strongly affect the control performance.
Therefore, the control system design of a quadrotor is
a challenging task.
In addition to some traditional linear control meth-
ods, robust and adaptive nonlinear control methods
have received much attention in recent years. The total
model of a quadrotor can be viewed as a cascade of
two subsystems, i.e. translational and attitude sub-
systems (Carrillo et al., 2013; Nonami et al., 2010).
Therefore a typical controller may have an inner-outer
loop structure, and backstepping design is considered
to be a useful tool. It is found that robust control
(Raffo et al., 2011), sliding mode control (Chen, Jiang,
et al., 2016; Derafa et al., 2012; Luque-Vega et al., 2012;
CONTACT Zi-Jiang Yang
shikoh.yoh.zijiang@vc.ibaraki.ac.jp
Department of Mechanical Systems Engineering, College of Engineering, Ibaraki
University, 4-12-1 Nakanarusawa, Hitachi, Ibaraki 316-8511, Japan
Rios et al., 2019; Song & Sun, 2017b), adaptive control
(Tran et al., 2018; Zhang et al., 2017; Zhao et al., 2015;
Zuo & Wang, 2014), disturbance estimation control
(Aboudonia et al., 2017; Besnard et al., 2012; Chen,
Lei, et al., 2016; Jin et al., 2015; Liu et al., 2016; Tian
et al., 2018; Xiao & Yin, 2017) or their combina-
tions are the most typical approaches to quadrotor
control.
The robust controllers may have high control gains
to suppress the uncertainties and disturbances. The
sliding mode control techniques usually include dis-
continuous switching action or nonsmooth terms and
hence is often implemented in a very fast sampling
rate. The adaptive control technique can achieve a
small tracking error due to the ability to deal with
parameterizable uncertainties. However, an adaptive
control system may exhibit unsatisfactory transient
performance and cannot handle unparameterizable
disturbances.
As
an
alternative
approach,
the
disturbance
observer (DOB)-based control technique (Li et al.,
2014) which compensates for the uncertainties and
disturbances by using their estimates has also been
applied. The DOB-based control technique enjoys the
advantage of less complex structure to compensate
© 2020 Informa UK Limited, trading as Taylor & Francis Group

## Page 3

940
K. SASAKI AND Z.-J. YANG
for the uncertainties. In Xiao and Yin (2017), Jin
et al. (2015), Aboudonia et al. (2017), and Chen, Lei,
et al. (2016), the DOBs are incorporated into the inner-
outer loop or backstepping controller design based
on nominal models. In Liu et al. (2016), a linear
robust multi-loop controller combined with a DOB
is proposed. The finite-time sliding mode DOBs are
used in Besnard et al. (2012). The sliding mode state
observers and DOBs are incorporated into a multivari-
able finite-time output feedback trajectory tracking
controller (Tian et al., 2018). Typically, in the afore-
mentioned DOB-based controllers it is a prerequisite
that the disturbances and their derivatives up to nec-
essary orders are bounded on the feasible domain of
the system states. Therefore, it is desirable to first
ensure that the system states do not escape from the
feasible domain especially during the transient phase
(Yang, 2018, 2019).
In recent years, the concept and technique of pre-
scribed performance control (PPC) methodology have
been proposed in Bechlioulis and Rovithakis (2009,
2014). The idea is to transform the control error sig-
nal to be constrained into another unconstrained error
signal which may be amplified to suppress the uncer-
tainties when the original error signal moves towards
the prescribed bound. If the transformed error is con-
trolled to be bounded, then the original error signal
satisfies the prescribed constraint.
So far, however, there are not so many works of the
PPC technique on the quadrotors (Chang & Shi, 2017;
Hua et al., 2017, 2018; Song & Sun, 2017a). In Song
and Sun (2017a) and Chang and Shi (2017), the PPC
technique is used for adaptive control of the attitude
subsystem only. In Hua et al. (2018), the PPC tech-
nique is combined with the adaptive sliding mode
control method. In Hua et al. (2017), the PPC tech-
nique is used for leader-follower formation problem,
but the quadrotor model is however simplified around
the hovering condition.
In this paper, we propose a new approach of DOB-
based robust control employing the PPC technique
for reference tracking of a quadrotor subject to mod-
elling error and disturbance uncertainties. The fea-
tures and contributions of the proposed approach are
summarised as follows. (1) Exploiting the cascaded
dynamics, the controller is designed in a backstepping
manner. For each axis of the subsystem with uncer-
tainties, a robust feedback controller employing the
PPC technique is designed to guarantee the prescribed
performance so that the system states remain within
the feasible domain. (2) The virtual controller of the
translational dynamics and the final controller of the
attitude dynamics are all enhanced by a DOB in each
axis which estimates the corresponding disturbance
term with an arbitrarily small error. (3) To circum-
vent the shortcoming of ‘explosion of terms’ in the
backstepping design, the dynamics surface control
(DSC) technique (Swaroop et al., 2000) employing a
low-pass filter is employed to calculate the pseudo-
differentiation of the corresponding virtual controller.
(4) As our major theoretical contribution, the tran-
sient performance and ultimate error bounds of vari-
ous error signals (including the unconstrained errors
transformed by the PPC technique) are investigated
from a unified viewpoint of the input-to-state practi-
cal stable (ISpS) property (Jiang & Praly, 1998; Krstic
et al., 1995) such that it is easy to understand how the
design parameters affect the error signals of each step
of design. Additionally, the ISpS of the overall cascaded
dynamics of the error signals is established. It is clari-
fied how the ultimate reference tracking errors can be
made sufficiently small owing to the DOBs. (5) Owing
to the theoretical analysis, the design policy is inves-
tigated and made clear. The PPC technique is adopted
to ensure moderate constraints without very small pre-
scribed ultimate error bounds which may make some
internal signals sensitive, whereas the DOBs are used
to achieve sufficiently small ultimate control errors.
(6) Finally, extensive simulation results are provided to
verify the theoretical results.
2. Statement of problem and preliminaries
2.1. Problem statement and quadrotor’s model
Let B = {XB, YB, ZB} be the body-fixed frame, and
E = {Xe, Ye, Ze} be the earth-fixed frame as shown in
Figure 1. Define p = [px, py, pz]T and v = [vx, vy, vz]T
as the position and velocity vectors of the origin of
the body-fixed frame related to that of the earth-fixed
frame, q = [φ, θ, ψ]T as the Euler angle vector in the
earth-fixed frame, and  = [ωx, ωy, ωz]T as the atti-
tude angular velocity vector in the body-fixed frame.
The mathematical model is established as the follow-
ing (Carrillo et al., 2013; Nonami et al., 2010).
˙p = v,
m˙v = −mgsI + FT + d,
(1)
˙q = W(q),
J ˙ = − × J + τ + τ d,
(2)

## Page 4

INTERNATIONAL JOURNAL OF SYSTEMS SCIENCE
941
Figure 1. Quadrotor UAV scheme.
where, sI = [0, 0, 1]T, m is the total mass of the
quadrotor, g is the gravity acceleration, FT ∈R3
is the translational driving force vector, J(q) =
diag(Jx, Jy, Jz) is the inertial matrix, τ = [τx, τy, τz]T
is the driving torque vector. Notice d = [dx, dy, dz]
and τ d = [τdx, τdy, τdz]T are disturbance vectors due
to the influences from the environment, e.x., the wind.
Additionally,
W(q) =
⎡
⎣
1
sin φ tan θ
cos φ tan θ
0
cos φ
−sin φ
0
sin φ sec θ
cos φ sec θ
⎤
⎦,
 × J =
⎡
⎣
(Jz −Jy)ωyωz
(Jx −Jz)ωxωz
(Jy −Jx)ωxωy
⎤
⎦.
Define the rotational matrix
R(q) =
⎡
⎣
CθCψ
CψSθSφ −SψCφ
SψCθ
SψSθSφ + CψCφ
−Sθ
CθSφ
CψSθCφ + SψSφ
SψSθCφ −CψSφ
CθCφ
⎤
⎦,
where C· = cos(·) and S· = sin(·). Then FT = [Fx, Fy,
Fz]T is expressed as
FT = R(q)
⎡
⎣
0
0
Fp
⎤
⎦
=
⎡
⎣
cos φ sin θ cos ψ + sin φ sin ψ
cos φ sin θ sin ψ −sin φ cos ψ
cos φ cos θ
⎤
⎦Fp,
where Fp is the total thrust force exerted by the
rotors.
Our task is to design a controller that generates
the control signals Fp, τx, τy, τz to let the quadrotor
track the given reference trajectory characterised by
the reference positions (pxd, pyd, pzd) and the reference
yawing angle ψd. Once Fp, τx, τy, τz are determined,
the desired propellor rotors’ rotational velocities are
calculated (Carrillo et al., 2013; Nonami et al., 2010).
To facilitate controller design, we separate the trans-
lational dynamics (1) into the horizontal x-y-dynamics
and the vertical z-dynamics:
˙vx
˙vy

= m−1
Fx
Fy

+ m−1
dx
dy

,
˙vz = m−1Fz −g + m−1dz,
(3)
where
Fx
Fy

= Fp
cos φ cos ψ
sin ψ
cos φ sin ψ
−cos ψ
 sin θ
sin φ

,
Fz = cos φ cos θFp.
(4)
The thrust force Fp can be designed to control the
vertical z-dynamics. Given Fp and taking sin θ and
sin φ as the driving terms of the x-y-dynamics, we first
determine the desired angles θd and φd. Then we deter-
mine τx, τy, τz to make the Euler angle vector q track
qd = [φd, θd, ψd]T, where the reference yawing ψd is
externally given.
Define the feasible domain of the system states as
X = Xp × Xv × Xq × X, where
Xp = {px, py, pz||x| ≤Rpx, |y| ≤Rpy, 0 ≤z ≤Rpz,
∃Rpx, ∃Rpy, ∃Rpz > 0},
Xv = {vx, vy, vz||vx| ≤Rvx, |vy| ≤Rvy, |vz| ≤Rvz,
∃Rvx, ∃Rvy, ∃Rvz > 0},
Xq = {φ, θ, ψ|φ ∈(−π/2, π/2), θ ∈(−π/2, π/2),
|ψ| ≤∃Rψ > 0},
X = {ωx, ωy, ωz||ωx| ≤Rωx, |ωy| ≤Rωy,
|ωz| ≤Rωz, ∃Rωx, ∃Rωy, ∃Rωz > 0}.
The volumes of Xp, Xv, X can be fairly large. How-
ever, the following assumption is common in the liter-
ature (Carrillo et al., 2013; Nonami et al., 2010).
Assumption 2.1: The rolling angle and pitching angle
satisfy
φ ∈(−π/2, π/2),
θ ∈(−π/2, π/2)
respectively.

## Page 5

942
K. SASAKI AND Z.-J. YANG
Notice that if cos θ = 0 or cos φ = 0, then Fz = 0
in (4) and hence the vertical z-dynamics (3) will lose
control. We further impose the following assumption
on the smoothness of the reference signals for the DSC
technique (Swaroop et al., 2000).
Assumption 2.2: The reference signals pxd, pyd, pzd
and ψd are appropriately chosen as sufficiently smooth
functions satisfying
Xpxd = {pxd(t), ˙pxd(t), ¨pxd(t) | |pxd| ≤Rpxd,
|˙pxd| ≤R˙pxd, |¨pxd| ≤R¨pxd, ∃Rpxd, ∃R˙pxd,
∃R¨pxd > 0},
Xpyd = {pyd(t), ˙pyd(t), ¨pyd(t) | |pyd| ≤Rpyd,
|˙pyd| ≤R˙pyd, |¨pyd| ≤R¨pyd, ∃Rpyd, ∃R˙pyd,
∃R¨pyd > 0},
Xpzd = {pzd(t), ˙pzd(t), ¨pzd(t) | |pzd| ≤Rpzd,
|˙pzd| ≤R˙pzd, |¨pzd| ≤R¨pzd, ∃Rpzd, ∃R˙pzd,
∃R¨pzd > 0},
Xψd = {ψd, ˙ψd, ¨ψd | |ψd| ≤Rψd,
| ˙ψd| ≤R ˙ψd, | ¨ψd| ≤R ¨ψd, ∃Rψd, ∃R ˙ψd,
∃R ¨ψd > 0}.
And the system states remain within the feasible
domain of X if x, y, z, ψ are controlled to track
pxd, pyd, pzd, ψd with a guaranteed performance.
Remark 2.1: The introduction of the definition of the
feasible domain does not mean that the state variables
are assumed to be always bounded in all cases. We
should adopt some robustifying techniques to let the
system states be kept within the feasible domain. The
PPC technique (Bechlioulis & Rovithakis, 2009, 2014)
is therefore adopted to achieve prescribed transient
performance so that the system states remain within
the feasible domain. In the literature of DOBs (Li
et al., 2014), it is usually assumed that the distur-
bances and their derivatives are bounded on the feasi-
ble domain. In the DSC technique it is often assumed
that the inverses of the time-constants of the low-pass
filters should be large enough to overcome the maxi-
mal values of the virtual signals’ derivatives on the fea-
sible domain (Swaroop et al., 2000). A recommended
recipe to this issue is the PPC technique.
2.2. Disturbance estimation via DOB
2.2.1. Disturbance estimation for translational
dynamics
Rewrite each subsystem of (3) as
˙pi = vi,
˙vi = m−1
0 Fi + wpi,
i = x, y,
˙pz = vz,
˙vz = m−1
0 Fz −g + wpz,
(5)
where m0 is the nominal value of mass, px = x, py =
y, pz = z, and wpx, wpy, wpz denote the lumped distur-
bances:
wpi = (m−1 −m−1
0 )Fi + m−1di = ˙vi −m−1
0 Fi,
i = x, y
wpz = (m−1 −m−1
0 )Fz + m−1dz = ˙vz −m−1
0 Fz + g.
Since wpi is unknown, we have to estimate it by
the equation error (˙vi −m−1
0 Fi) or (˙vz −m−1
0 Fz + g).
Since calculation of ˙vi is usually contaminated with
noise, we pass wpi (the equation error) through a low-
pass filter to obtain its estimate:
wbpi = Qpi(s)wpi = Qpi(s)

svi −m−1
0 Fi
	
,
i = x, y,
wbpz = Qpz(s)wpz = Qpz(s)

svz −m−1
0 Fz + g
	
.
(6)
This is the so called DOB studied extensively in the
literature (Li et al., 2014). Here, we adopt a second-
order filter Qpi(s) = 1/(1 + λpis)2 for i = x, y, z, where
λpi > 0 is the time-constant, and for the convenience
of expression, s denotes both the Laplace operator and
the differential operator. The implementation of the
second-order filter can be performed in a cascaded
manner as
λpi ˙wapi + wapi = wpi,
λpi ˙wbpi + wbpi = wapi,
(7)
where wapi(0) = wbpi(0) = 0. As shown on the right
hand side of (6), instead of the unknown wpi itself, the
equation error is passed through the low-pass filter.
To ensure that the estimates of the disturbances
approximate the disturbances with sufficiently small
errors, we impose the following assumptions as in Li
et al. (2014).
Assumption 2.3: The lumped disturbance terms
wpi (i = x, y, z) and the derivatives ˙wpi have maximal
values on the feasible domain X, and there exists a
positive constant ˙wpi for each of i = x, y, z such that
| ˙wpi| ≤˙wpi on the feasible domain X.

## Page 6

INTERNATIONAL JOURNAL OF SYSTEMS SCIENCE
943
Assumption 2.4: The time-constant λpi for each of
i = x, y, z is chosen sufficiently small such that 1/λpi ≥
˙wpi/ϵbpi, where ϵbpi ∝λpi is a sufficiently small posi-
tive number.
Remark 2.2: Assumption 2.3 can be found in the
works of DOB based control. However, it does not
mean that | ˙wpi| ≤˙wpi always holds. It holds only when
the system states stay within the feasible domain X. As
mentioned in Remark 2.1, the PPC technique should
be adopted to ensure this prerequisite. Assumption 2.4
is introduced to ensure small estimation errors of the
DOBs.
Define the error signal 
wbpi = wbpi −wpi. Then we
have (see Appendix A for proof):
Lemma 2.5: Let Assumptions 2.1–2.4 hold. Then the
DOB’s estimation error decays such that |
wbpi| ≤
wbpi
within a short time interval Tbpi ∝ϵbpi ∝λpi, where

wbpi ∝ϵbpi ∝λpi.
Remark 2.3: To avoid any effects of possible peaking
behaviour of the derivative of wbpi during the transient
phase, we modify it as wpi(t) = (1 −e−t/γpi)wbpi(t)
with some γpi > λpi. In this study, we choose γpi =
10λpi. Define the disturbance estimation error as
wpi =
wpi −wpi for i = x, y, z. Then |
wpi(t ≥Tpi)| ≤ϵpi
where ∃ϵpi ∝ϵbpi ∝λpi and Tpi ∝γpi.
2.2.2. Disturbance estimation for attitude dynamics
Rewrite the attitude dynamics in (2) as ˙ = J−1
0 τ +
w, where J0 = diag(J0x, J0y, J0z) is the nominal inertia
matrix, w = [wωx, wωy, wωz]T is the lumped distur-
bance vector: w = (J−1 −J−1
0 )τ −J−1[ × J] +
J−1τ d. Then we write each subsystem of (2) as
˙ωi = J−1
0i τi + wωi,
i = x, y, z,
(8)
and pass wωi = ˙ωi −J−1
0i τi
(the equation error)
through a low-pass filter to obtain its estimate:
wbωi = Qωi(s)wωi = Qωi(s)

J0isωi −τi
	
,
(9)
where Qωi(s) = 1/(1 + λωis)2, and λωi > 0. The filter
can be implemented in a cascaded manner:
λωi ˙waωi + waωi = wωi,
λωi ˙wbωi + wbωi = waωi,
(10)
where waωi(0) = wbωi(0) = 0. We also impose the fol-
lowing assumptions.
Assumption 2.6: The lumped disturbance terms
wωi (i = x, y, z) and the derivatives ˙wωi have maximal
values on the feasible domain X, And there exists a
positive constant ˙wωi for each of i = φ, θ, ψ such that
| ˙wωi| ≤˙wωi on the feasible domain X.
Assumption 2.7: The time-constant λωi for each
of i = φ, θ, ψ is chosen sufficiently small such that
1/λωi ≥˙wωi/ϵbωi, where ϵbωi ∝λωi is a sufficiently
small positive number.
Define the error 
wbωi = wbωi −wωi. Then similar
to Lemma 2.5, we have the following result.
Lemma 2.8: Let Assumptions 2.1, 2.2, 2.6, 2.7 hold.
Then the DOB’s estimation error decays such that
|
wbωi| ≤
wbωi within a short time interval Tbωi ∝
ϵbωi ∝λωi, where 
wbωi ∝ϵbωi ∝λωi.
Remark
2.4: To
avoid
any
effects
of
peaking
behaviour of the derivative of wbωi during the transient
phase, we modify it as wωi(t) = (1 −e−t/γωi)wbωi(t)
with some γωi > λωi. In this study, we choose γωi =
10λωi. Define the disturbance estimation error 
wωi =
wωi −wωi for i = x, y, z. Then |
wωi(t ≥Tωi)| ≤ϵωi
where ∃ϵωi ∝ϵbωi ∝λωi and Tωi ∝γωi.
2.3. Brief review of PPC
The technique of PPC (Bechlioulis & Rovithakis,
2009, 2014; Yang, 2018, 2019) is briefly reviewed here.
To begin with, consider a simple scalar system as an
illustrative example:
˙s = u + d(s, t),
(11)
where s is the error signal (not the Laplace operator)
to be stabilised, d(s, t) is a disturbance, and u is the
control input.
Prescribed performance means that the error sig-
nal converges to a predefined small residual set, with
a predefined convergence rate. Define an enveloping
signal ρ(t) = (ρ0 −ρ∞) e−at + ρ∞, where ρ0, ρ∞, a
are predefined positive constants. The mathematical
expression of prescribed performance is expressed
as −ρ(t) < s(t) < ρ(t), provided |s(0)| < ρ0. To
satisfy the prescribed performance, the error sig-
nal s is transformed into an equivalent uncon-
strained signal η by a nonlinear function η = T(ξ),
or equivalently, s = ρ(t)S(η) and T(ξ) = S−1(η),

## Page 7

944
K. SASAKI AND Z.-J. YANG
where ξ = s(t)/ρ(t) is the normalised error satis-
fying −1 < ξ < 1. More specifically, we can choose
S(η) = (eη −e−η)/(eη + e−η), η = T(ξ) = 1
2 ln((1 +
ξ)/(1 −ξ)), satisfying (1) −1 < S(η) < 1 if η is
bounded, (2) limη→+∞S(η) = 1, limη→−∞S(η) =
−1. Thus if η is bounded, then −ρ(t) < s(t) < ρ(t).
Consider s(t) = ρ(t)S(η). Recalling the mean-
value theorem, we have S(η) = S′(θη)η, 0 < θ < 1,
where 0 < S′(η) = 4/(eη + e−η)2 ≤1. And hence
|s(t)| = |ρ(t)S′(θη)η| ≤ρ(t)|η|.
(12)
Therefore, we can make ρ(t) and/or |η| small so that
|s| becomes small. However, too small a ρ(t) may make
|ξ| get close to 1, so that η = T(ξ) is sensitive.
To make η bounded, we further deduce the dynam-
ics of the transformed error signal η:
˙η = ˙ξ ∂S−1(ξ)
∂ξ
= r(ξ)
ρ(t)(u + d −ξ ˙ρ),
(13)
where, 1 ≤r(ξ) = 1/(1 + ξ)(1 −ξ). Notice that as
long as |ξ| < 1, we have r(ξ) ≤r, ∃r > 0.
We can design a controller u = −cr(ξ)η, where
c>0 is the control gain. If the disturbance d is sig-
nificant so that s(t) grows to approach its envelop-
ing function ρ(t), then r(ξ) and η grow significantly
to overcome the term (d −ξ ˙ρ) in (13). Resultantly,
η is made bounded so that −ρ(t) < s(t) < ρ(t) is
ensured. However, this only ensures that η is bounded.
The amplitude of η itself may be large if (d −ξ ˙ρ) is rel-
atively strong. In this case, according to (12), to achieve
a small ultimate |s|, the ultimate bound ρ∞has to be
very small. Then ξ may be very close to the singular
points of the nonlinear functions, and hence r(ξ) and
η may be sensitive. Therefore, a very small ρ∞is not
recommended. If the term (d −ξ ˙ρ) is compensated by
the DOB, the burden of the PPC control technique can
be reduced.
Remark 2.5: In the sequel, the signal notations will be
added by indices k and i, e.x., ski, ξki, ηki, rki, ρki(t) =
(ρki0 −ρki∞) e−akit + ρki∞, etc., where i = x, y, z or
i = φ, θ, ψ, and k is the step index of backstepping
design.
3. Backstepping control design
According to the cascaded structure of (1) and (2), the
design procedure includes four steps. Steps 1 and 2 are
for translational position control, by which the thrust
force Fp, the rolling and pitching references φd and
θd are determined to let px, py, pz track their reference
values pxd, pyd, pzd. Steps 3 and 4 are for attitude con-
trol, by which (τx, τy, τz) are determined to let (φ, θ, ψ)
track (φd, θd, ψd).
3.1. Step 1: stabilisation of position tracking errors
s1x, s1y, s1z
Consider the position-velocity relation ˙pi = vi (i =
x, y, z) of the translational dynamics in (1) or (5).
Given the reference positions as pid (i = x, y, z), the
position tracking error signal of each axis bebomes
s1i = pi −pid. Since the real velocity vi cannot be used
directly for design, we introduce its corresponding vir-
tual controller α1i, and the error between vi and α1i
is defined as s2i = vi −α1i. Then we have the error
dynamics as ˙s1i = s2i + α1i −˙pid. And we design the
virtual controller as
α1i = −c1is1i + ˙pid,
(14)
where c1i > 0 is the control gain. Using α1i, we have
the error system as
˙s1i = −c1is1i + s2i, i = x, y, z,
(15)
Notice
˙α1i = −c1i(−c1is1i + s2i) + ¨pid.
As
summarised later in Lemma 4.1, if s2i is controlled to
satisfy prescribed performance, s1i naturally satisfies
an induced prescribed performance.
The next step is to stabilise s2i (i = x, y, z). Since
the vertical motion and the horizontal motion are
orthogonal, we design the vertical controller and hor-
izontal controller separately for transparency (Raffo
et al., 2011).
3.2. Step 2: stabilisation of transformed velocity
error η2z for vertical motion
Using (5) and (4), we have the error dynam-
ics of the vertical subsystem as ˙s2z = ˙vz −˙α1z =
m−1
0
cos θ cos φFp −g + wpz −˙α1z. According to (13),
the dynamics of the transformed error η2z by the PPC
technique is obtained as
˙η2z = r2z
ρ2z
cos θ cos φFp
m0
−g + wpz −˙α1z
−ξ2z ˙ρ2z

,
(16)

## Page 8

INTERNATIONAL JOURNAL OF SYSTEMS SCIENCE
945
where the notations of ρ2z, ξ2z, r2z, η2z are explained
in Remark 2.5. Then we can design the thrust force of
the rotors as
Fp =
m0
cos θ cos φ

−c2zr2zη2z + g + ˙α1z
+ ξ2z ˙ρ2z −wpz
	
,
(17)
where c2z > 0 is the control gain,wpz is the disturbance
estimate by DOB. Using Fp, we have
˙η2z = r2z
ρ2z

−c2zr2zη2z + 
wpz
	
,
(18)
where 
wpz is defined in Remark 2.3. At this step, the
tracking control design for the vertical z-dynamics is
completely finished and the total thrust force Fp is
obtained.
3.3. Step 2: stabilisation of transformed velocity
errors η2x, η2y for horizontal motion
3.3.1. Design of the reference rolling angle and
pitching angles φd and θd
Using (5) with i = x, y, we have the error dynam-
ics of the horizontal subsystems as ˙s2i = ˙vi −˙α1i =
m−1
0 Fi + wpi −˙α1i. According to (13), the dynamics
of the transformed error η2i by the PPC technique is
obtained as
˙η2i = r2i
ρ2i
 Fi
m0
+ wpi −˙α1i −ξ2i ˙ρ2i

,
(19)
where the notations of ρ2i, ξ2i, r2i, η2i are explained
in Remark 2.5. Then we can design the virtual control
signal corresponding to the translational force Fi (i =
x, y):
α2i = m0

−c2ir2iη2i + ˙α1i + ξ2i ˙ρ2i −wpi
	
,
(20)
where c2i > 0 is the control gain. Replacing Fx, Fy and
θ, φ in (4) by α2x, α2y and θα, φα, we have
α2x
α2y

= Fp
cos φα cos ψ
sin ψ
cos φα sin ψ
−cos ψ
 sin θα
sin φα

,
(21)
where θα and φα are the virtual references of θ and φ
which are obtained as the following.
φα = arcsin
α2x sin ψ −α2y cos ψ
Fp

,
θα = arcsin
α2x cos ψ + α2y sin ψ
Fp cos φα

.
(22)
Motivated by the DSC technique (Swaroop et al.,
2000), low-pass filters are used to avoid direct differ-
entiations of θα, φα for backstepping design. Then we
have
λ2θ ˙θd + θd = θα,
λ2φ ˙φd + φd = φα,
(23)
where λ2θ and λ2φ are small time-constants, θd(0) =
θα(0), φd(0) = φα(0). Then we obtain the rolling angle
and pitching references φd and θd. At Steps 3 and 4,
τx, τy, τz will be designed to let φ, θ, ψ track φd, θd,
ψd. Notice that the yawing reference ψd is externally
provided.
3.3.2. Derivation of the controlled error dynamics of
horizontal motion
Define the errors between φα, θα and their filtered
counterparts respectively:
y2θ = θd −θα = −λ2θ ˙θd,
y2φ = φd −φα = −λ2φ ˙φd.
(24)
Clearly, we have y2θ(0) = y2φ(0) = 0, ˙θd = y2θ/(−λ2θ),
˙φd = y2φ/(−λ2φ), and the error dynamics ˙y2θ =
−y2θ/λ2θ −˙θα, ˙y2φ = −y2φ/λ2φ −˙φ. To make the
error signals y2i (i = θ, φ) small, we impose the fol-
lowing assumption.
Assumption 3.1: The time-constants λ2θ, λ2φ of the
low-pass filters (24) are chosen sufficiently small such
that 1/λ2θ ≥2 ˙θα/ϵ2θ, 1/λ2φ ≥2 ˙φα/ϵ2φ, where ˙θα
and ˙φα are respectively the maximal values of | ˙θα|
and | ˙φα| on the feasible domain of the system signals,
ϵ2θ ∝λ2θ and ϵ2φ ∝λ2φ are sufficiently small positive
numbers.
Since ˙θα and ˙φα are never known in practice, usu-
ally, λ2θ and λ2φ are chosen to be sufficiently small.
According to Assumption 3.1, we have
d
dt

y2
2θ
2

≤−y2
2θ
2λ2θ
−y2
2θ
2λ2θ
+ |y2θ| ˙θα
≤−y2
2θ
2λ2θ
−|y2θ|
2λ2θ
(|y2θ| −ϵ2θ).
Notice that y2θ(0) = 0. Then y2θ(t) will satisfy |y2θ| ≤
ϵ2θ for t ≥0, since we have dy2
2θ/dt < −y2
2θ/2λ2θ if
|y2θ| grows beyond ϵ2θ. Similarly, we can also con-
clude |y2φ| ≤ϵ2φ for t ≥0, and hence ∥y2φθ∥2 ≤

ϵ2
2θ + ϵ2
2φ, where y2φθ = [y2φ, y2θ]T.

## Page 9

946
K. SASAKI AND Z.-J. YANG
By the filtered signals θd and φd, the relation (21)
changes to be
α2dx
α2dy

= Fp
cos φd cos ψ
sin ψ
cos φd sin ψ
−cos ψ
 sin θd
sin φd

,
(25)
where α2dx, α2dy are virtual forces due to φd and θd.
Noticing the horizontal driving forces Fx and Fy are
obtained by (4), we define the force error signals
s3αi = Fi −α2di,
y2αi = α2di −α2i,
i = x, y,
(26)
and denote s3α = [s3αx, s3αy]T, y2α = [y2αx, y2αy]T.
Then we can express the exact force signal Fi by Fi =
s3αi + y2αi + α2i. And using (20), we can rewrite (19)
as
˙η2i = r2i
ρ2i

−c2ir2iη2i + 
wpi + s3αi + y2αi
m0

,
(27)
where i = x, y, and 
wpi is defined in Remark 2.3.
Define the attitude tracking errors s3θ = θ −θd,
s3φ = φ −φd, and s3φθ = [s3φ, s3θ]T which will be sta-
bilised at Step 3. We then evaluate how the attitude
error s3φθ affects the force error s3α. Using (4) and (25),
we have
s3αx = Fp cos ψ(cos φ sin θ −cos φd sin θd)
+ Fp sin ψ(sin φ −sin φd),
s3αy = Fp sin ψ(cos φ sin θ −cos φd sin θd)
−Fp cos ψ(sin θ −sin θd).
(28)
Notice that Fp has already been determined by (17).
Then using the mean-value theorem to (28), we can
show that
∥s3α∥2 ≤Mpψ∥s3φθ∥2,
∃Mpψ > 0.
(29)
Similarly, we evaluate how y2φθ affects y2α. Using (21)
and (25), we have
y2αx = Fp cos ψ(cos φd sin θd −cos φα sin θα)
+ Fp sin ψ(sin φd −sin φα),
y2αy = Fp sin ψ(cos φd sin θd −cos φα sin θα)
−Fp cos ψ(sin θd −sin θα).
Then, similar to (29), we have
∥y2α∥2 ≤Mpψ∥y2φθ∥2 ≤Mpψ

ϵ2
2θ + ϵ2
2φ.
(30)
These results will be used for performance analysis in
Section 4.
3.4. Step 3: stabilisation of transformed angular
tracking error vector η3
Define the reference attitude angles as qd = [φd, θd,
ψd]T, where φd, θd were obtained at Step 2, and ψd
is externally provided. Then we consider how to let
the Euler angles track their references. Consider the
relation ˙q = W in (2). Define the error vector s3 =
q −qd = [sT
3φθ, ψ −ψd]T = [s3φ, s3θ, s3ψ]T. Then we
have ˙s3 = W −˙qd. According to (13), the dynamics
of the transformed error vector η3 = [η3φ, η3θ, η3ψ]T
by the PPC technique is obtained as
˙η3 = ρ−1
3 (t)R3

W −˙qd −˙ρ3ξ3

,
(31)
where R3 = diag(r3φ, r3θ, r3ψ), ξ3 = [ξ3φ, ξ3θ, ξ3ψ]T,
ρ3 = diag(ρ3φ, ρ3θ, ρ3ψ). The notations of ρ3i, ξ3i, r3i,
η3i (i = x, y, z) are explained in Remark 2.5. Then
we design the virtual controller vector corresponding
to :
α3 = W−1(−C3R3η3 + ˙qd + ˙ρ3ξ3)
= [α3x, α3y, α3z]T,
(32)
where C = diag(cx, cy, cz) > 0 is the control gain.
Again motivated by the DSC technique, a low-pass
filter is introduced to avoid direct differentiation of
α3i (i = x, y, z). Define the low-passed signal as α3di.
Then we have
λ3i ˙α3di + α3di = α3i,
(33)
where α3di(0) = α3i(0). The error signal is obtained as
y3i = α3di −α3i = −λ3i ˙α3di. Clearly, we have y3i(0) =
0, ˙α3di = y3i/(−λ3i), and ˙y3i = −y3i/λ3i −˙α3i. We
also impose the following assumption.
Assumption 3.2: For each of i = x, y, z, the time-
constant λ3i of the low-pass filter is chosen sufficiently
small such that 1/λ3i ≥2˙α3i/ϵ3i, where ˙α3i is the max-
imal value of of |˙α3i| on the feasible domain of the
system signals, ϵ3i ∝λ3i is a sufficiently small positive
number.
Similar to the previous results, we have |y3i| ≤ϵ3i
for t ≥0. Denote y3 = [y3x, y3y, y3z]T. Then we have
∥y3∥2 ≤

ϵ2
3x + ϵ2
3y + ϵ2
3z.
(34)
Denote α3d = [α3dx, α3dy, α3dz]T and define the error
signals of the angular velocities s4 =  −α3d =

## Page 10

INTERNATIONAL JOURNAL OF SYSTEMS SCIENCE
947
[s4x, s4y, s4z]T. Then we have  = s4 + α3 + y3, and
hence (31) becomes
˙η3 = ρ−1
3 (t)R3

−c3R3η3 + W(s4 + y3)

.
(35)
3.5. Step 4: stabilisation of transformed angular
velocity errors η4x, η4y, η4z
Using (8), we have the error dynamics as ˙s4i =
˙ωi −˙α3di = J−1
0i τi + wωi −˙α3di, i = x, y, z. According
to (13), the dynamics of the transformed error η4i is
obtained as
˙η4i = r4i
ρ4i
τi
J0
+ wωi −˙α3di −ξ4i ˙ρ4i

,
(36)
where the notations of ρ4i, ξ4i, r4i, η4i are explained in
Remark 2.5. Then we can design the control torques
τx, τy, τz as
τi = J0

−c4ir4iη4i + ˙α3di
+ ξ4i ˙ρ4i −wωi
	
,
i = x, y, z,
(37)
where c4i > 0. And hence we have
˙η4i = r4i
ρ4i
(−c4ir2zη4i + 
wωi) ,
(38)
where 
wωi is defined in Remark 2.4.
3.6. Summary of the overall controller
Now we have obtained the required control signals: the
thrust force Fp and the driving torques τx, τy, τz. Since
the design process is quite lengthy, we will summarise
the designed controller for convenience of the read-
ers. The block diagram of the overall control system
is shown in Figure 2.
3.6.1. Thrust force Fp
According to (3), the relative degree from Fp to the
vertical position pz is two. Thus the design includes
Figure 2. Diagram of the overall control system.
two steps. We obtain the virtual controller α1z (14) and
then the thrust force Fp (17).
3.6.2. Torques τx, τy, τz
According to (1) and (2), the relative degree from
(φ, θ) to the horizontal position (px, py) is two, and
that from (τx, τy, τz) to (φ, θ) is two. Therefore, we have
an inner-outer loop structure of controller.
For the horizontal motion, we obtain the virtual
controller α1i(i = x, y) (14) and the references of
rolling and pitching angles, i.e. φd and θd by (22)
and (23). Notice that the reference yawing angle ψd
is externally provided. For the rotational motion, we
first obtain the virtual controller α3 (32) and its fil-
tered version by (33). Then we obtain the torques
τx, τy, τz (37).
4. Performance analysis of backstepping design
We first perform detailed analysis for each step of
backstepping design. The analysis process is per-
formed in a step-by-step manner as done in Bech-
lioulis and Rovithakis (2014) and in Section 6.7 of
Krstic et al. (1995). In Section 5, the overall control
performance will be summarised.
4.1. Step 1: performance of position tracking errors
4.1.1. Prescribed performance
Consider (15). The solution is given as s1i(t) =
e−c1its1i(0) +
 t
0 e−c1i(t−τ)s2i(τ) dτ, where s2i will be
controlled at the next step to satisfy |si2(t)| < ρ2i(t) =
(ρ2i0 −ρ2i∞) e−a2it + ρ2i∞. Then we have |s1i(t)| <
e−c1it|s1i(0)| + ρ2i∞
 t
0 e−c1i(t−τ) dτ + (ρ2i0 −ρ2i∞)
 t
0 e−c1ite(c1i−a2i)τ dτ. Notice
 t
0 e−c1i(t−τ) dτ = (1 −
e−c1it)/c1i. When c1i ̸= a2i we have
 t
0 e−c1ite(c1i−a2i)τ
dτ = (e−a2it −e−c1it)/(c1i −a2i), and when c1i = a2i
we have
 t
0 e−c1it e(c1i−a2i)τ dτ = e−c1itt. Then we have
Lemma 4.1: If s2i (i = x, y, z) is controlled to satisfy the
prescribed performance |si2(t)| <(ρ2i0 −ρ2i∞)e−a2it +
ρ2i∞, then the performance of the translational position
tracking error s1i is prescribed as
|s1i(t)| < ρ2i∞
c1i
+ e−c1it

|s1i(0)| −ρ2i∞
c1i

+ ρ2i0 −ρ2i∞
c1i −a2i
(e−a2it −e−c1it),
c1i ̸= a2i,

## Page 11

948
K. SASAKI AND Z.-J. YANG
or
|s1i(t)| < ρ2i∞
c1i
+ e−c1it

|s1i(0)| −ρ2i∞
c1i

+ (ρ2i0 −ρ2i∞) e−c1itt,
c1i = a2i.
For further study, we then derive the input-to-state-
stable (ISS) property (Krstic et al., 1995) of (15), which
will be used later.
4.1.2. ISS property of vertical position’s tracking
error s1z
Using (15) for i = z and using the technique of com-
pleting the square, we have
d
dt
s2
1z
2

≤−c1zs2
1z + |s1z||s2z| ≤−c1z
2 s2
1z + s2
2z
2c1z
and
hence
|s1z(t)|2 ≤|s1z(0)|2 e−c1zt + (1/c2
1z)
sup0≤τ≤t |s2z(τ)|2. Using (12), we have |s2z(t)| ≤
ρ2z0|η2z(t)|. Notice η2z was handled in Subsection 3.2.
Then we have the ISS property:
Lemma 4.2: If the transformed error η2z is controlled
to be bounded at Step 2, then
|s1z(t)| ≤|s1z(0)| e−c1zt/2 + M1z sup
0≤τ≤t
|η2z(τ)|, (39)
where M1z = ρ2z0/c1z.
4.1.3. ISS property of horizontal position’s tracking
errors s1x and s1y
Recall (15) for i = x, y and define s1xy = [s1x, s1y]T.
Similarly, we have
d
dt

∥s1xy∥2
2
2

≤−
c1xy
2 ∥s1xy∥2
2 + ∥s2xy∥2
2
2c1xy
,
where c1xy = min(c1x, c1y), s2xy = [s2x, s2y]T. And
then
∥s1xy(t)∥2
2 ≤∥s1xy(0)∥2
2 e−c1xyt + (1/c2
1xy)
sup0≤τ≤t ∥s2xy(τ)∥2
2. According to (12), we have
∥s2xy∥2 ≤ρ2xy0∥η2xy∥2,
where
ρ2xy0 = max(ρ2x0,
ρ2y0), η2xy = [η2x, η2y]T. Notice η2xy was handled in
Subsection 3.3. Then we have the ISS property of s1xy:
Lemma 4.3: If the transformed error vector η2xy is
controlled to be bounded at Step 2, then
∥s1xy(t)∥2 ≤∥s1xy(0)∥2 e−c1xyt/2
+ M1xy sup
0≤τ≤t
∥η2xy(τ)∥2,
(40)
where M1xy = ρ2xy0/c1xy.
At Step 2, we will show that η2z and η2xy are con-
trolled to be bounded and sufficiently small.
4.2. Step2: performance of translational position
control
4.2.1. Performance of transformed velocity error η2z
for vertical motion
Define V2z = η2
2z/2. Then using (18) and the tech-
nique of completing the square, we have
˙V2z(t) = 1
ρ2z

−c2zr2
2zη2
2z + r2zη2z
wpz
	
,
≤1
ρ2z

−c2z
2 r2
2zη2
2z +

w2
pz
2c2z

≤−c2zV2z
ρ2z0
+

w2
pz
2c2zρ2z∞
.
Notice r2z ≥1 (see the definition below (13)).
As explained in Subsection 2.3 and in Bechlioulis and
Rovithakis (2014), if the term 
w2
pz/2c2zρ2z∞is signif-
icant so that the error signal s2z grows to approach
the prescribed bound ρ2z, then the transformed error
signal η2z also grows to suppress it, so that the
signals do not escape away. Considering Assump-
tions 2.1, 2.2, 2.3, it is clear that ˙V2z < 0 when η2
2z >
ρ2z0
w2
pz/c2
2zρ2z∞, where 
wpz is the maximal value
of 
wpz (see Remark 2.3 for the definition of 
wpz)
on the feasible domain. Then we can conclude that
η2z
is
bounded
and
hence
the
prescribed
performance −ρ2z(t) < s2z < ρ2z(t) is ensured. Then
we have V2z(t) ≤V2z(0) e−c2z/ρ2z0t + (ρ2z0/2c2
2zρ2z∞)
[sup0≤τ≤t 
w2
pz(τ)], which leads to the following ISS
property of η2z:
Lemma 4.4: Let Assumptions 2.1, 2.2, 2.3 hold. Then
|η2z(t)| ≤|η2z(0)| e−γ2zt/2 + M2z

sup
0≤τ≤t

wpz(τ)

,
(41)
where γ2z = c2z/ρ2z0, M2z =

ρ2z0/c2
2zρ2z∞.
4.2.2. Performance of vertical position control
According to Lemma C.4 of Krstic et al. (1995), the
cascaded combination of (39) and (41) is also ISS.
Furthermore, to show the improvement owing to the
DOB, we consider the cascade of (39) and (41) for

## Page 12

INTERNATIONAL JOURNAL OF SYSTEMS SCIENCE
949
t ≥Tpz (see Remark 2.3 for Tpz).
|s1z(t)| ≤|s1z(Tpz)| e−c1z(t−Tpz)/2
+ M1z
sup
Tpz≤τ≤t
|η2z(τ)|,
|η2z(t)| ≤|η2z(Tpz)| e−γ2z(t−Tpz)/2 + M2zϵpz,
(42)
where ϵpz is the DOB’s ultimate estimation error bound
(see Remark 2.3). Define sz = [s1z, η2z]T. By using
Lemma C.4 of Krstic et al. (1995) to the cascaded
inequalities (42) and using some tedious calculations,
we have ∥sz(t ≥Tpz)∥2 ≤βz∥sz(Tpz)∥2 e−γz(t−Tpz)/2 +
Ez, where γz is a constant depending on c1z, c2z, and βz
is a constant depending on M1z. Finally, Ez is a constant
depending on ϵpz and can be made sufficiently small
(see Remark 2.3). The derivation process is lengthy and
hence omitted due to the limitation of paper length. To
summarise, we have
Theorem 4.5 (Performance of vertical position con-
trol): Let Assumptions 2.1, 2.2, 2.3 hold. Then the
following results hold.
(1) The vertical position tracking error signal s1z satis-
fies Lemma 4.1.
(2) The internal error signal s2z corresponding to the
vertical dynamics satisfies −ρ2z(t) < s2z < ρ2z(t).
(3) Furthermore, if Assumption 2.4 holds, the error
signal vector sz satisfies
∥sz(t ≥Tpz)∥2 ≤βz∥sz(Tpz)∥2
× e−γz(t−Tpz)/2 + Ez,
(43)
where sz = [s1z, η2z]T, and Ez can be made suffi-
ciently small by choosing a sufficiently small time-
constant of the corresponding DOB.
The theorem implies that the vertical positon error
s1z can be made sufficiently small.
4.2.3. Performance of transformed velocity errors η2x,
η2y for horizontal motion
Define ηxy = [ηx, ηy]T and V2xy = ∥η2xy∥2
2/2. Then
noticing r2i ≥1 (see the definition below (13)) and
using (27), we have
˙V2xy(t) =

i=x,y
η2i
r2i
ρ2i
(−c2ir2iη2i + μ2i) ,
≤

i=x,y
1
ρ2i

−1
2c2xyr2
2iη2
2i + μ2
2i
2c2xy

,
≤−
c2xy
ρ2xy0
V2xy(t) +
1
2c2xyρ2xy∞

i=x,y
μ2
2i,
(44)
where c2xy = min(c2x, c2y), ρ2xy0 = max(ρ2x0, ρ2y0),
ρ2xy∞= min(ρ2x∞, ρ2y∞), μ2i = 
wpi + (s3αi + y2αi)/
m0 (i = x, y). Define μ2xy = [μ2x, μ2y]T and 
wpxy =
[
wpx,
wpy]T. Then we have μ2xy = 
wpxy + m−1
0 y2α +
m−1
0 s3α. And using (30), we have ∥μ2xy∥2 ≤∥
wpxy∥2 +
m−1
0 Mpψ

ϵ2
2θ + ϵ2
2φ + m−1
0 ∥s3α∥2.
According to Assumptions 2.1, 2.2, 2.3, the DOB’s
estimation error 
wpi has a maximal value on the fea-
sible domain. Furthermore, if the error signal s3αi is
made at the next step to satisfy the prescribed perfor-
mance so that −ρ3i(t) < s3αi < ρ3i(t) (i = φ, θ, ψ),
there exists a μ2xy which is the maximal value of
∥μ2xy∥2 on the feasible domain. Then, it is clear that
˙V2xy < 0 when V2xy > (ρ2xy0/2c2
2xyρ2xy∞)μ2
2xy. Then
we conclude that η2x and η2y are bounded and the pre-
scribed performance −ρ2i(t) < s2i < ρ2i(t) (i = x, y)
is ensured. Using (44), we have
∥η2xy(t)∥2 ≤∥η2xy(0)∥2 e−γ2xyt/2
+ Mρc2xy

sup
0≤τ≤t
∥μ2xy(τ)∥2

,
≤∥η2xy(0)∥2 e−γ2xyt/2
+ Mρc2xym−1
0 Mpψ

ϵ2
2θ + ϵ2
2φ
+ Mρc2xy

sup
0≤τ≤t

∥
wpxy(τ)∥2
+ m−1
0 ∥s3α(τ)∥2

,
where γ2xy = c2xy/ρ2xy0, Mρc2xy =

ρ2xy0/c2
2xyρ2xy∞.
According to (12), we have ∥s3φθ∥2 ≤ρ3φθ0∥η3φθ∥2,
where ρ3φθ0 = max(ρ3φ0, ρ3θ0). Using (29), we have
∥s3α∥2 ≤Mpψ∥s3φθ∥2 ≤Mpψρ3φθ0∥η3φθ∥2.
Notice
η3φθ was handled in Subsection 3.4. Then we have the
following ISpS property:

## Page 13

950
K. SASAKI AND Z.-J. YANG
Lemma 4.6: Let Assumptions 2.1, 2.2, 2.3 and 3.1 hold.
Then
∥η2xy(t)∥2 ≤∥η2xy(0)∥2 e−γ2xyt/2
+ Mρc2xym−1
0 Mpψ

ϵ2
2θ + ϵ2
2φ
+ Mρc2xy

sup
0≤τ≤t
∥
wpxy(τ)∥2

+ Mρc2xym−1
0 Mpψρ3φθ0
×

sup
0≤τ≤t
∥η3φθ(τ)∥2

.
To investigate the improvement owing to the
DOBs, we consider 
wpxy(t ≥Tpxy) where Tpxy =
max(Tpx, Tpy)
(see
Remark
2.3).
According
to
Remark 2.3, we have ∥
wpxy(t ≥Tpxy)∥2 ≤

ϵ2px + ϵ2py.
Then the ISpS property of η2xy in Lemma 4.6 is rewrit-
ten as
∥η2xy(t ≥Tpxy)∥2
≤∥η2xy(Tpxy)∥2 e−γ2xy(t−Tpxy)/2
+ M2xyϵ + M2xy
×

sup
Tpxy≤τ≤t
∥η3φθ(τ ≥Tpxy)∥2

,
(45)
where M2xy = Mρc2xym−1
0 Mpψρ3φθ0, M2xyϵ = Mρc2xy
(m−1
0 Mpψ

ϵ2
2θ + ϵ2
2φ +

ϵ2px + ϵ2py).
Notice
that
M2xyϵ is a constant depending on ϵpx, ϵpy, ϵ2θ, ϵ2φ,
which can all be made sufficiently small.
4.3. Step 3: performance of transformed angular
tracking error vector η3
Consider the error dynamics (35) and define μ3 =
W(s4 + y3) = [μ3φ, μ3θ, μ3ψ]T. Notice R3 and ρ3
in (35) are diagonal matrices and r3i ≥1 (i = φ, θ, ψ)
(see the definition below (13)). Define V3 = ∥η3∥2
2/2.
Then we have
˙V3(t) =

i=φ,θ,ψ
η3i
r3i
ρ3i
(−c3ir3iη3i + μ3i) ,
≤−c3
ρ30
V3(t) +
1
2c3ρ3∞
∥μ3∥2
2,
(46)
where c3 = min(c3φ, c3θ, c3ψ), ρ30 = max(ρ3φ0, ρ3θ0,
ρ3ψ0), ρ3∞= min(ρ3φ∞, ρ3θ∞, ρ3ψ∞).
According to (34), ∥y3∥2 is sufficiently small. Fur-
thermore, if s4i (i = x, y, z) is made at the next step to
satisfy the prescribed performance so that −ρ4i(t) <
s4i < ρ4i(t), there exists a μ3 which is the maxi-
mal value of ∥μ3∥2 on the feasible domain of the
system signals. It is clear that ˙V3 < 0 when V3 >
(ρ30/2c2
3ρ3∞)μ2
3. That is, we can conclude that the
vector η3 is bounded and hence the prescribed perfor-
mance −ρ3i(t) < s3i < ρ3i(t) (i = φ, θ, ψ) is ensured.
According to (12), we have ∥s4∥2 ≤ρ40∥η4∥2,
where
ρ40 = max(ρ4x0, ρ4y0, ρ4z0).
Furthermore,
define
σ w∞= sup0≤t≤∞σ[W(q(t))]
where
σ(·)
denotes the maximal singular value of a matrix.
Then we have ∥μ3∥2 ≤∥Wy3∥2 + ∥Ws4∥2 ≤σ w∞
(

ϵ2
3x + ϵ2
3y + ϵ2
3z + ρ40∥η4∥2). Using (46), we have
∥η3(t)∥2 ≤∥η3(0)∥2 e−(c3/ρ30)t/2 +

ρ30/c2
3ρ3∞
[sup0≤τ≤t ∥μ3(t)∥2]. Then we have the ISpS property
of μ3:
Lemma 4.7: Let Assumptions 2.1, 2.2, 2.3, 2.6, 3.1, 3.2
hold. Then
∥η3(t)∥2 ≤∥η3(0)∥2 e−γ3t/2
+ M3bϵ + M3a

sup
0≤τ≤t
∥η4(τ)∥2

, (47)
where
γ3 = c3/ρ30,
M3bϵ = σ w∞

ρ30/c2
3ρ3∞

ϵ2
3x + ϵ2
3y + ϵ2
3z, M3a = σ w∞ρ40

ρ30/c2
3ρ3∞.
4.4. Step 4: performance of transformed angular
velocity error vector η4
Consider the error dynamics (38). Define η4 =
[η4x, η4y, η4z]T, V4 = ∥η4∥2
2/2. Then similar to the
previous results, we have
˙V4(t) =

i=x,y,z
η4i
r4i
ρ4i
(−c4ir4iη4i + 
wωi) ,
≤−c4
ρ40
V4(t) +
1
2c4ρ4∞
∥
wω∥2
2,
(48)
where c4 = min(c4x, c4y, c4z), 
wω = [
wωx,
wωy,
wωz]T,
ρ4∞= max(ρ4x∞, ρ4y∞, ρ4z∞).
Similar to the previous analysis, according to
Assumptions 2.1, 2.2, 2.6, we also have ˙V4 < 0 when
V4 > (ρ40/2c2
4ρ4∞)
wω, where 
wω is the maximal
value of ∥
wω∥2 on the feasible domain. Thus the trans-
formed error vector η4 is bounded and hence the

## Page 14

INTERNATIONAL JOURNAL OF SYSTEMS SCIENCE
951
prescribed performance −ρ4i(t) < s4i < ρ4i(t) (i =
x, y, z) is ensured. Using (48), we have the ISS property
as
Lemma 4.8: Let Assumptions 2.1, 2.2, 2.3, 2.6, 3.1, 3.2
hold. Then
∥η4(t)∥2 ≤∥η4(0)∥2 e−γ4t/2
+ Mρc4

sup
0≤τ≤t
∥
wω(τ)∥2

,
where γ4 = c4/ρ40, Mρc4 =

ρ40/c2
4ρ4∞.
To investigate the improvement owing to the DOBs,
we consider 
wω(t ≥Tω) where Tω = max(Tωx, Tωy,
Tωz) (see Remark 2.4). According to Remark 2.4, we
have ∥
wω(t ≥Tω)∥2 ≤

ϵ2ωx + ϵ2ωy + ϵ2ωz. Then we
can rewrite the result of Lemma 4.8 as
∥η4(t ≥Tω)∥2 ≤∥η4(Tω)∥2 e−γ4(t−Tω)/2 + M4ϵ,
(49)
where M4ϵ = Mρc4

ϵ2ωx + ϵ2ωy + ϵ2ωz, and ϵωx, ϵωy,
ϵωz can be made sufficiently small.
4.5. Performance of horizontal position and
attitude control
The overall error dynamics of the horizontal and
attitude subsystems is the cascade of the error sys-
tems characterised in Lemmas 4.3, 4.6, 4.7, 4.8. By
repeatedly using Lemma C.4 of Krstic et al. (1995) to
these cascaded error systems, we can show that the
dynamics of the augmented error signal vector sxyψ =
[sT
1xy, ηT
2xy, ηT
3 , ηT
4 ]T is also ISpS.
Furthermore, to investigate the improvement owing
to the DOBs, we consider the cascaded inequalities
of (40), (45), (47), (49) for t ≥Txyψ = max(Tpxy, Tω).
By repeatedly using Lemma C.4 of Krstic et al. (1995)
to these cascaded inequalities and using some tedious
but inductive calculations, we have the following ISpS
property: ∥sxyψ(t ≥Txyψ)∥2 ≤βxyψ e−γxyψ(t−Txyψ)/2
∥sxyψ(Txyψ)∥2 + Exyψ, where γxyψ, βxyψ, Exyψ are
constants depending on the constants in (40), (45),
(47), (49). Especially, Exyψ is a constant depend-
ing on M2xyϵ, M3bϵ, M4ϵ in (45), (47), (49), where
M2xyϵ depends on ϵpx, ϵpy, ϵ2θ, ϵ2φ, M3bϵ depends
on ϵ3x, ϵ3y, ϵ3z, and M4ϵ depends on ϵωx, ϵωy, ϵωz.
Notice ϵpx, ϵpy, ϵωx, ϵωy, ϵωz are due to the small time-
constants of the DOB (Remarks 2.3,2.4), and ϵ2θ, ϵ2φ,
ϵ3x, ϵ3y, ϵ3z are due to the small time-constants of the
low-pass filters of the DSC technique (see (30), (34)).
These constants can be made sufficiently small so that
Exyψ is sufficiently small. Then we have the following
theorem:
Theorem 4.9 (Performance of horizontal position
and attitude control): Let Assumptions 2.1, 2.2, 2.3,
2.6 3.1, 3.2 hold. Then the following results hold.
(1) The horizontal position tracking error signals s1i
(i = x, y) satisfy Lemma 4.1.
(2) The internal error signals s2i (i = x, y) correspond-
ing to the horizontal dynamics satisfy −ρ2i(t) <
s2i < ρ2i(t).
(3) The attitude tracking error signals s3i (i = φ, θ, ψ)
satisfy −ρ3i(t) < s3i < ρ3i(t).
(4) The internal error signals s4i (i = x, y, z) corre-
sponding to the attitude dynamics satisfy −ρ4i(t) <
s4i < ρ4i(t).
(5) Furthermore, if Assumptions 2.4 and 2.7 hold, the
cascaded error dynamics of the horizontal and atti-
tude subsystems satisfies
∥sxyψ(t ≥Txyψ)∥2
≤βxyψ∥sxyψ(Txyψ)∥2 e−γxyψ(t−Txyψ)/2
+ Exyψ,
(50)
where sxyψ = [sT
1xy, ηT
2xy, ηT
3 , ηT
4 ]T, and Exyψ is a
constant which can be made sufficiently small by
choosing sufficiently small time-constants of the
low-pass filters corresponding to the DOBs and the
DSC technique.
Therefore the ultimate value of the horizontal posi-
tion tracking error vector s1xy = [px −pxd, py −pyd]T
and that of the transformed attitude tracking error
vector η3 = [η3φ, η3θ, η3ψ]T can be made sufficiently
small. According to (12), the ultimate value of the
Euler angles’ tracking error vector s3 corresponding to
the transformed error η3 can aslo be made sufficiently
small.
5. Performance of the overall control system
Remember that the purpose of this study is to
let the positions (px, py, pz) and the yawing angle
ψ track their reference values (pxd, pyd, pzd) and

## Page 15

952
K. SASAKI AND Z.-J. YANG
ψd. The tracking performance of the vertical posi-
tion z was characterised in Theorem 4.5, whereas
the tracking performance of (px, py) and ψ was
characterised in Theorem 4.9. To characterise the
overall control performance, we define the overall
error vector by concatenating the error signals of
Theorem 4.5 and Theorem 4.9 as s = [sT
z , sT
xyψ]T =
[s1z, η2z, sT
1xy, ηT
2xy, ηT
3 , ηT
4 ]T. The overall performance
is obtained by combining (43) and (50) in Theorem 4.5
and Theorem 4.9. Denote β = max(βz, βxyψ), γ =
min(γz, γxyψ),
Tf = max(Tpz, Txyψ),
E =
√
2(Ez
+ Exyψ). Then based on the relation
√
a2 + b2/
√
2 ≤
|a| + |b| ≤
√
2
√
a2 + b2 for any a and b, the com-
bination of (43) and (50) leads to s(t ≥Tf )∥2 ≤
2β∥s(Tf )∥2 e−γ (t−Tf )/2 + E. The results are sum-
marised as the following.
Theorem 5.1 (Performance of the overall error
system): Let Assumptions 2.1, 2.2, 2.3, 2.6 3.1, 3.2 hold.
Then the following results hold.
(1) All of the error signals s1i (i = x, y, z), s2i (i =
x, y, z), s3i (i = φ, θ, ψ), s4i (i = x, y, z) satisfy
their correspongding prescribed performances.
(2) Furthermore, if Assumptions 2.4 and 2.7 hold, the
overall cascaded error dynamics of the translational
and attitude subsystems satisfies
∥s(t ≥Tf )∥2 ≤2β∥s(Tf )∥2 e−γ (t−Tf )/2 + E,
(51)
where s = [s1z, η2z, sT
1xy, ηT
2xy, ηT
3 , ηT
4 ]T, and E is
a constant which can be made sufficiently small
by choosing sufficiently small time-constants of the
low-pass filters corresponding to the DOBs and the
DSC technique.
6. Simulation studies
The proposed method and the theoretical analy-
sis results are verified by simulation studies on the
quadrotor model (1) and (2), where the physical
parameters are m = 0.74 [kg], g = 9.81 [m/s2], Jx =
Jy = 0.004 [kgm2], Jz = 0.0084 [kgm2]. To verify the
robustness of our method, the nominal physical
parameters are chosen as m0 = 0.6 m, Jx0 = 0.6Jx,
Jy0 = 0.6Jy, Jz0 = 0.6Jz, the disturbance terms in (1)
and (2) are given as dx = dy = dz = cos(2πt/15) [N]
and τdx = τdy = τdz = 0.1 sin(2πt/15) [Nm]. The ref-
erence signals are given as pxd = 0.5 cos(t/3) [m],
pyd = 0.5 sin(t/3) [m], pzd = 1 + t/10 [m], ψd = 0.5
sin(πt/30) [rad]. The initial positions are [x(0), y(0),
z(0)] = [0, 0.5, 0.5] [m], and the initial Euler angles are
[φ(0), θ(0), ψ(0)] = [0, 0, 0.1] [rad]. The initial veloc-
ities are all zero. The design parameters are chosen as
follows.
Feedback control gains:
c1x = c1y = 2,
c2x = c2y = 2,
c1z = 4,
c2z = 4,
c3x = c3y = c3z = 4,
c4x = c4y = c4z = 4.
Figure 3. Translational trajectory and position tracking errors when the DOBs are used.

## Page 16

INTERNATIONAL JOURNAL OF SYSTEMS SCIENCE
953
Time-constants of DSC filters:
λ2φ = λ2θ = 0.03,
λ3x = λ3y = λ3z = 0.02.
Time-constants of DOB filters:
λpx = λpy = λpz = 0.03,
λωx = λωy = λωz = 0.02.
Parametrs of PPC’s performance function ρki(t) =
(ρki0 −ρkij∞) e−akit + ρki∞:
ρ2i0 = 3,
ρ2i∞= 0.2,
a2i = 0.3,
i = x, y, z,
ρ3i0 = 0.3,
ρ3i∞= 0.03,
a3i = 0.3,
i = φ, θ, ψ,
ρ4i0 = 3,
ρ4i∞= 0.2,
a4i = 0.3,
i = x, y, z,
Notice k = 2, 3, 4 is the step index of backstepping
design.
Figure 4. Translational velocities and errors when the DOBs are
used.
Figure 5. Euler angles and errors when the DOBs are used.
Figure 6. Attitude angular velocties and errors when the DOBs
are used.
Although there is no general theory of choosing
optimal design parameters, we briefly explain how
these parameters are chosen.
Usually, the horizontal motion is not so fast (notice
the relative degree from the driving torque to the posi-
tion is four), thus the feedback gains c1x, c1y, c2x, c2y
are chosen to be relatively low. On the other hand,
the vertical motion can be relatively fast (notice the
relative degree from the thrust force to the position
is two), thus the gains c1z, c2z are relatively high. The
feedback gains c3x, c3y, c3z, c4x, c4y, c4z for rotational
motion (inner-loop) are chosen to be relatively high.
The time constants of DSC and DOB filters are cho-
sen to be sufficienly small untill satisfactory results are
Figure 7. Disturbances and their estimates when the DOBs are
used.

## Page 17

954
K. SASAKI AND Z.-J. YANG
Figure 8. Control inputs when the DOBs are used.
obtained. Notice that the filters’ time-constants of the
inner-loop are smaller than those of the outer-loop.
Finally we consider how to choose the parameters of
the performance bounding functions ρki(t) = (ρki0 −
ρkij∞) e−akit + ρki∞where k = 2, 3, 4 is the step
index of backstepping design. We can roughly estimate
the decaying time of the error signals from Lem-
mas 4.4, 4.6, 4.7, 4.8. Therefore, the decaying parame-
ters aki (k = 2, 3, 4) are chosen such that the decaying
times of the bounding functions are slightly longer
than those of the transformed error signals. According
to (16), (19) and (36), since the systems of the trans-
formed errors are directly affected by the disturbances,
to avoid sensitive signals, the values for ρki0 and ρkij∞
(k = 2, 4) are not chosen to be very small. According
to (31), the transformed angular error system is not
directly affected by the disturbances. Addtionally, the
amplitudes of the Euler angles are not so large. Thus
we choose relatively small values for ρ3i0 and ρ3ij∞.
Clearly, the results of theoretical analysis are very help-
ful for choosing the design parameters.
The control results are shown in Figures 3–13 for
two different situations where the DOBs are used or
not used, as indicated in the figure captions. In the fig-
ures, the reference signals and the true disturbances are
plotted in dotted red lines, the prescribed performance
bounds are plotted in dotted cyan lines, the system
states, input signals and disturbance estimates are plot-
ted in blue lines, and the error signals are plotted in
black lines.
When the DOBs are used, it can be seen in Figures 3
and 5 that the positions and the Euler angles track
their references quite well. And it can be seen in Fig-
ures 3–6 that the error signals are sufficiently small and
far below the prescribed performance bounds, owing
to the DOBs. The disturbances and their estimates, and
the input signals are shown in Figures 7 and 8.
On the other hand, when the DOBs are not used,
it is found in Figures 9–12 that the trajectory tracking
performance is not satisfactory and the error signals
are not sufficiently small. Nevertheless the constrained
error signals ski (k = 1, 2, 3, 4, i = x, y, z or φ, θ, ψ)
still satisfy the prescribed bounds. It is found that some
error signals are close to their prescribed bounds. It
Figure 9. Translational trajectory and position tracking errors when the DOBs are not used.

## Page 18

INTERNATIONAL JOURNAL OF SYSTEMS SCIENCE
955
Figure 10. Translational velocities and errors when the DOBs are
not used.
Figure 11. Euler angles and errors when the DOBs are not used.
Figure 12. Attitude angular velocties and errors when the DOBs
are not used.
Figure 13. Control inputs when the DOBs are not used.
might be possible to further suppress the error signals
by choosing much smaller ultimate bounds. However,
as claimed in Section 2.3, if the prescribed bounds are
too tight, the error signals may be very close to the pre-
scribed bounds so that the nonlinear transformation
functions of the PPC technique become to be sensitive.
Therefore, our policy is to use the PPC technique to
ensure moderate prescribed constraints without very
small prescribed ultimate error bounds, and to use
the DOBs to achieve sufficiently small ultimate control
errors.
7. Conclusions
In this paper, we have proposed a novel robust nonlin-
ear control method for trajectory tracking of a quadro-
tor UAV using the PPC technique and DOBs, in the
presence of external disturbances and uncertainties
of physical parameters. By exploiting the cascaded
structure of the position subsystems and the attitude
subsystems, the controller is designed in a backstep-
ping manner, and the DSC technique is adopted to
avoid the explosion of the controller complexity. For
each axis of the subsystem with uncertainties, the PPC
technique is adopted to ensure a moderate control
performance. Then a DOB is constructed to enhance
the corresponding controller to achieve a small ulti-
mate error. The control performance of the overall
control system has been analysed rigorously. Finally,
the performance of the proposed controller has been
confirmed by simulation studies. And resultantly, the
design policy has been made clear. It is concluded

## Page 19

956
K. SASAKI AND Z.-J. YANG
that the PPC technique should be adopted to ensure
moderate constraints without very small prescribed
ultimate error bounds, whereas the DOBs are used to
achieve sufficiently small ultimate control errors.
Disclosure statement
No potential conflict of interest was reported by the author(s).
Notes on contributors
Kazuya Sasaki was born 1994. He received the bachelor’s
and master’s degrees in 2017 and 2019 respectively both from
Ibaraki University, Hitachi City, Japan. His research interests
include robust control of unmanned UAVs and optimal design
of electric vehicles.
Zi-Jiang Yang was born 1964. He is currently a professor of
Ibaraki Universty, Hitachi City, Japan. His research interests
include robust control, adaptive control and system identifica-
tion.
ORCID
Zi-Jiang Yang
http://orcid.org/0000-0003-3588-9906
References
Aboudonia, A., El-Badawy, A., & Rashad, R. (2017). Active
anti-disturbance control of a quadrotor unmanned aerial
vehicle using the command-filtering backstepping approach.
Nonlinear
Dynamics,
90,
581–597.
https://doi.org/
10.1007/s11071-017-3683-y
Bechlioulis, C. P., & Rovithakis, G. A. (2009). Adaptive con-
trol with guaranteed transient and steady state tracking
error bounds for strict feedback systems. Automatica, 45(2),
532–538. https://doi.org/10.1016/j.automatica.2008.08.012
Bechlioulis, C. P., & Rovithakis, G. A. (2014). A low-complexity
global approximation-free control scheme with prescribed
performance for unknown pure feedback systems. Automat-
ica, 50(4), 1217–1226. https://doi.org/10.1016/j.automatica.
2014.02.020
Besnard, L., Shtessel, Y. B., & Landrum, B. (2012). Quadrotor
vehicle control via sliding mode controller driven by sliding
mode disturbance observer. Journal of the Franklin Institute,
349(2), 658–684. https://doi.org/10.1016/j.jfranklin.2011.06.
031
Carrillo, L. R. G., Lopez, A. E. D., Lozano, R., & Pegard, C.
(2013). Quad rotorcraft control, vision-based hovering and
navigation. Springer-Verlag.
Chang, S., & Shi, W. (2017). Adaptive fuzzy time-varying slid-
ing mode control for quadrotor UAV attitude system with
prescribed performance. 29th Chinese control and decision
conference, Chongqing, China.
Chen, F., Jiang, R., Zhang, K., Jiang, B., & Tao, G. (2016). Robust
backstepping sliding-mode control and observer-based fault
estimation for a quadrotor UAV. IEEE Transactions on Indus-
trial Electronics, 63, 5044–5056. https://doi.org/10.1109/
TIE.2016.2552151
Chen, F., Lei, W., Zhang, K., Tao, G., & Jiang, B. (2016). A novel
nonlinear resilient control for a quadrotor UAV via backstep-
ping control and nonlinear disturbance observer. Nonlinear
Dynamics, 85, 1281–1295. https://doi.org/10.1007/s11071-
016-2760-y
Derafa, L., Benalleguel, A., & Fridman, L. (2012). Super twist-
ing control algorithm for the attitude tracking of a four
rotors UAV. Journal of the Franklin Institute, 349(2), 685–699.
https://doi.org/10.1016/j.jfranklin.2011.10.011
Hua, C., Chen, J., & Guan, X. (2018). Adaptive prescribed per-
formance control of QUAVs with unknown time-varying
payload and wind gust disturbance. Journal of the Franklin
Institute,
355(14),
6323–6338.
https://doi.org/10.1016/j.
jfranklin.2018.05.062
Hua, C., Chen, J., & Li, Y. (2017). Leader-follower finite-time
formation control of multiple quadrotors with prescribed
performance. International Journal of Systems Science,
48, 2499–2508. https://doi.org/10.1080/00207721.2017.132
3135
Jiang, Z. P., & Praly, L. (1998). Design of robust adaptive con-
trollers for nonlinear systems with dynamic uncertainties.
Automatica, 34(7), 825–840. https://doi.org/10.1016/S0005-
1098(98)00018-1
Jin, Z. C., Meng, G., & Lu, W. (2015). Backstepping based trajec-
tory tracking control for a quadrotor aircraft with nonlinear
disturbance observer. International Journal of Control and
Automation, 8, 169–182. https://doi.org/10.14257/ijca
Krstic, M. L., Kanellakopoulos, I., & Kokotovic, P. (1995). Non-
linear and adaptive control design. John Wiley & Sons, Inc.
Li, S. H., Yang, J., Chen, W. H., & Chen, X. S. (2014). Distur-
bance observer based control: methods and applications. CRC
Press.
Liu, H., Li, D., Zuo, Z., & Zhong, Y. (2016). Robust three-
loop trajectory tracking control for quadrotors with multiple
uncertainties. IEEE Transactions on Industrial Electronics, 63,
2263–2274. https://doi.org/10.1109/TIE.2016.2514339
Luque-Vega, L., Castillo-Toledo, B., & Loukianov, A. G. (2012).
Robust block second order sliding mode control for a
quadrotor. Journal of the Franklin Institute, 349(2), 719–739.
https://doi.org/10.1016/j.jfranklin.2011.10.017
Nonami, K., Kendoul, F., Suzuki, S., Wang, W., & Nakazawa, D.
(2010). Autonomous flying robots, unmanned aerial vehicles
and micro aerial vehicles. Springer-Verlag.
Raffo, G. V., Ortega, M. G., & Rubio, F. R. (2011). Path
tracking of a UAV via an underactuated H∞control
strategy. European Journal of Control, 17(2), 194–213.
https://doi.org/10.3166/ejc.17.194-213
Rios, H., Falcon, R., Gonzalez, O. A., & Dzul, A. (2019). Con-
tinuous sliding-mode control strategies for quadrotor robust
tracking: real-time application. IEEE Transactions on Indus-
trial Electronics, 66, 1264–1272. https://doi.org/10.1109/
TIE.41
Song, Z., & Sun, K. (2017a). Adaptive compensation control for
attitude adjustment of quad-rotor unmanned aerial vehicle.

## Page 20

INTERNATIONAL JOURNAL OF SYSTEMS SCIENCE
957
ISA Transactions, 69, 242–255. https://doi.org/10.1016/j.
isatra.2017.04.003
Song, Z., & Sun, K. (2017b). Attitude tracking control of a quad-
rotor with partial loss of rotation effectiveness. Asian Journal
of Control, 19, 1–11. https://doi.org/10.1002/asjc.v19.1
Swaroop, D., Hedrick, J. K., Yip, P. P., & Gerdes, J. C. (2000).
Dynamic surface control for a class of nonlinear systems.
IEEE Transactions on Automatic Control, 45, 1893–1899.
https://doi.org/10.1109/TAC.2000.880994
Tian, B., Lu, H., Zuo, Z., Zong, Q., & Zhang, Y. (2018). Multi-
variable finite-time output feedback trajectory tracking con-
trol of quadrotor helicopters. International Journal of Robust
and Nonlinear Control, 28, 281–295. https://doi.org/10.1002/
rnc.v28.1
Tran, T. T., Ge, S. S., & He, W. (2018). Adaptive con-
trol of a quadrotor aerial vehicle with input constraints
and uncertain parameters. International Journal of Control,
91(5), 1140–1160. https://doi.org/10.1080/00207179.2017.
1309572
Xiao, B., & Yin, S. (2017). A new disturbance attenuation
control scheme for quadrotor unmanned aerial vehicles.
IEEE Transactions on Industrial Informatics, 13, 2922–2932.
https://doi.org/10.1109/TII.2017.2682900
Yang, Z. J. (2018). Prescribed performance control for con-
sensus output tracking of nonlinear systems. Proceedings of
the 2018 IEEE 27th international symposium on industrial
electronics (ISIE), Cairns.
Yang, Z. J. (2019). Distributed prescribed performance con-
trol for consensus output tracking of nonlinear semi-strict
feedback systems using finite-time disturbance observers.
International Journal of Systems Science, 50, 989–1005.
https://doi.org/10.1080/00207721.2019.1586006
Zhang, C., Hu, H., & Wang, J. (2017). An adaptive neural net-
work approach to the tracking control of micro aerial vehi-
cles in constrained space. International Journal of Systems
Science, 48, 84–94. https://doi.org/10.1080/00207721.2016.
1157223
Zhao, B., Xian, B., Zhang, Y., & Zhang, X. (2015). Non-
linear robust adaptive tracking control of a quadro-
tor UAV via immersion and invariance methodology.
IEEE Transactions on Industrial Electronics, 62, 2891–2902.
https://doi.org/10.1109/TIE.41
Zuo, Z., & Wang, C. (2014). Adaptive trajectory tracking con-
trol of output constrained multi-rotors systems. IET Con-
trol Theory & Applications, 8, 1163–1174. https://doi.org/10.
1049/iet-cta.2013.0949
Appendix. Proof of Lemma 2.5
Considering (7), we define the errors between the signals
and their filtered ones as yapi = wapi −wpi, ybpi = wbpi −wapi,
whose initial values are yapi(0) = −wpi(0), ybpi(0) = 0, And we
have the relations ˙wapi = −yapi/λpi, ˙wbpi = −ybpi/λpi. To show
that yapi and ybpi successively decay to sufficiently low levels, we
derive the following cascaded error dynamics.
˙yapi = −1
λpi
yapi −˙wpi,
˙ybpi = −1
λpi
ybpi + yapi
λpi
.
(A1)
The solution of yapi is obtained as yapi(t) = e−t/λpi[yapi(0) +
 t
0 eτ/λpi(−˙wpi) dτ]. Noticing yapi(0) = −wpi(0) and Assump-
tion 2.4, we have |yapi(t)| ≤|wpi(0)| e−t/λpi + λpi ˙wpi(1 −
e−t/λpi) ≤|wpi(0)| e−t/λpi + ϵbpi(1 −e−t/λpi). Here, we only
consider the nontrivial case where |wpi(0)| > 2ϵbpi, whereas
the trivial case where |wpi(0)| ≤2ϵbpi is omitted. Then we
have |yapi(t)| ≤yapi = |wpi(0)| for t ≥0. And if |yapi(t)|
decays so that |yapi(t ≥Tia)| ≤2ϵbpi, we should have Tia =
λpi log[(|wpi(0)|
−ϵbpi)/ϵbpi].
Similarly, noticing ybpi(0) = 0 and (A1), we have |ybpi(t)| ≤
|ybpi(0)| e−t/λpi + yapi(1 −e−t/λpi) ≤|wpi(0)|.
Clearly
|ybpi(t)| ≤ybpi = |wpi(0)| for t ≥0. Then for t ≥Tia, we have
|ybpi(t ≥Tia)| ≤|wpi(0)| e−(t−Tia)/λpi + 2ϵbpi(1 −e−(t−Tia)/λpi).
If |ybpi(t)| decays so that |ybpi(t ≥Tib)| ≤3ϵbpi, we should have
Tib = Tia + λpi log[(|wpi(0)| −2ϵbpi)/ϵbpi].
Since the DOB’s error 
wbi = wbpi −wpi = yapi + ybpi, then
we have |
wbpi(t ≥Tib)| ≤|yapi(t ≥Tib)| + |ybpi(t ≥Tib)| =
5ϵbpi. According to Assumption 2.4, ϵbpi ∝λpi.
