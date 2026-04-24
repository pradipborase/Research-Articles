# Robust Control of UAV with Disturbances and Uncertainty Estimation.pdf

## Page 1

Citation: Domenico B.; Di Gennaro,
S.; Di Ferdinando, M.; Acosta Lùa, C.
Robust Control of UAV with
Disturbances and Uncertainty
Estimation. Machines 2023, 11, 352.
https://doi.org/10.3390/
machines11030352
Academic Editor: Ismael Minchala
Received: 4 January 2023
Revised: 13 February 2023
Accepted: 17 February 2023
Published: 3 March 2023
Copyright:
© 2023 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed
under
the
terms
and
conditions of the Creative Commons
Attribution (CC BY) license (https://
creativecommons.org/licenses/by/
4.0/).
machines
Article
Robust Control of UAV with Disturbances and
Uncertainty Estimation
Domenico Bianchi 1,2,*
, Stefano Di Gennaro 1,2
, Mario Di Ferdinando 1,2
and Cuauhtémoc Acosta Lùa 2,3
1
Department of Information Engineering, Computer Science and Mathematics, University of L’Aquila,
Via Vetoio, Loc. Coppito, 67100 L’Aquila, Italy
2
Center of Excellence DEWS, University of L’Aquila, Via Vetoio, Loc. Coppito, 67100 L’Aquila, Italy
3
Centro Universitario de la Ciénega, Universidad de Guadalajara, Av. Universidad No. 1115, Col. Lindavista,
Ocotlán 47820, Jalisco, Mexico
*
Correspondence: domenico.bianchi@univaq.it
Abstract: In this work, a nonlinear estimator-based robust controller is designed for the position
and yaw control of a quadrotor with uncertainty estimation. This controller ensures the tracking of
desired references in the presence of parameters variation and external disturbances, making use
of high-order sliding mode (HOSM) estimators to estimate these perturbations that can be canceled
by the control, thus improving the dynamic behavior of the controlled system. Its performance
is evaluated making use of a Simcenter Amesim quadrotor based on physical models generated
from experimental data in a co-simulation framework with Matlab–Simulink used to implement
the designed controller with FPGA implementation. A challenging and generic maneuver with
time-varying wind disturbances and uncertainty model parameters is considered.
Keywords: UAV control; robust control; estimators
1. Introduction
In recent years UAVs have attracted attention due to the vast range of applications that
can be addressed, and they have been widely utilized by researchers, law enforcement and
security, delivery companies, farmers, etc. Furthermore, UAVs are evolving from being only
important for the sensing action [1] to being fundamental also for the actuator action. In the
upcoming years, there will therefore be a remarkable development of drones for functional
applications such as payload delivery services to transport deformable linear objects such as
hoses and goods to carry organs for organ transplants, which helped reduce car journeys to
just a few minutes of ﬂight. Furthermore, a recent study showed that the delivery of UAVs
could even help reduce greenhouse gas emissions caused by the freight industry [2]. While
the application interest of UAVs is growing, on the other hand, there is a need to make the
system more and more efﬁcient. The main limitation that occurs in all applications, however,
is the limited amount of energy that batteries or other energy sources provide. In fact, in the
drones on the market, the average ﬂight time is between 15 and 45 min, which is a time
that highly limits the real application. Improvement and optimization of the source energy,
lightening of the drone, optimization of the path and improvement of the performance in the
presence of disturbances that modify its behavior and signiﬁcantly decrease performance
from an energy point of view are some of the actions investigated to solve the problem.
The execution of trajectories that allow for lower consumption is important. In fact, one
of the factors that often inﬂuences the consumption is linked to disturbances, such as
wind, which leads to a departure from the ideal trajectory, and it is then necessary to
compensate through additional time and higher battery consumption. In the same way,
the model on which the control is based is an approximation, the parameters are time-
varying, and it is therefore necessary to intervene also on the parametric uncertainties.
It is a challenge that must be faced from different points of view and that requires a
Machines 2023, 11, 352. https://doi.org/10.3390/machines11030352
https://www.mdpi.com/journal/machines

## Page 2

Machines 2023, 11, 352
2 of 23
multidisciplinary effort in order to achieve the goal. Motivated by the European project
COMP4DRONES (see [3]), it was necessary to study methodologies for controlling the
ﬂight of a drone in precision agriculture, to monitor the health status of plants, and possibly
spray fertilizer to the plants with time limits, trying to minimize the energy and to follow
desired trajectory in presence of disturbances and parametric uncertainties. This represents
a complex problem with different objectives. In [4], a robust ﬂight controller based on
linear active disturbance rejection control is proposed for the stability control of an aerial
robot quadrotor under wind gusts. The nonlinear dynamical model of the quadrotor,
considering the wind disturbance, is ﬁrstly established through Newton–Euler method.
In this control scheme, the linear extended state observer serves as a compensator which can
effectively reject the wind gusts. In this case, the disturbance due to the wind is therefore
compensated, but a perfect knowledge of the model and its parameters is assumed. In [5],
a robust dynamic sliding mode control algorithm using a nonlinear disturbance observer
for system dynamics is investigated. The proposed method is applied to provide a rapid
adaptation and strictly robust performance for the attitude and altitude control of UAVs.
The procedure of the proposed method consists of two stages. First, a nonlinear disturbance
observer is applied to estimate the exogenous perturbation. Second, a robust dynamic
sliding mode controller integrated with the estimated values of disturbances is presented
by a combination of a PID sliding surface and super twisting technique to compensate for
the effect of these perturbations on the system. Again, external noise is considered but not
model-related uncertainties. Furthermore, the control is tested on an ideal plant. In [6], a
novel extension of the classic Nonlinear Dynamic Inversion (NLDI) control architecture
for wind disturbance rejection is designed by using adaptive artiﬁcial neural networks.
In [7], an adaptive controller for a quadrotor UAV for carrying unknown payloads while
tracking any trajectory is proposed. The proposed adaptive controller is robust to modeling
uncertainties and does not require any a priori knowledge of the bounds of the uncertainties.
The controller is also robust to time-varying delays without any constraint on the derivative
of the time delay. The simulations are conducted on the simple basic model and do not
take into account possible disturbances, such as wind, which inﬂuence performance in
a non-negligible way. In [8], the deep reinforcement learning method, and robust deep
deterministic policy gradient, are proposed for developing a controller that allows robust
ﬂying of an unmanned aerial vehicle in dynamic uncertain environments. While a very
interesting work, it is tested in a simpliﬁed scenario, and the wind and the parametric
uncertainties of the model are not directly considered. Furthermore, there is no formal
proof of the stability of the controlled system.
The contribution of the paper is dual: on the one hand, it designs a controller that is
robust both to the uncertainties of the model and to external disturbances such as wind or
aerodynamic factors using HOSM estimators; on the other side, this controller is tested in a
co-simulation environment between Matlab–Simulink and Simcenter Amesim on FPGA.
In fact, to our best knowledge, results concerning the quadrotor tracking problem in the
case of variations of all the parameters emerging in the dynamics and in the presence of
environmental disturbances and/or unmodeled dynamics inﬂuencing dynamics of the
UAV are not available in the research literature. Moreover, after preliminary tests on Matlab–
Simulink implementation, that have not been included in this paper, the proposed controller
is tested on the quadrotor model provided by the Simcenter Amesim developed by Siemens,
based on physical models, in a co-simulation environment with FPGA implementation.
As a matter of fact, Simcenter Amesim is proven to accurately represent the dynamic
behavior of the drone, it was extensively validated with experimental tests, and it is used
by important aerospace enterprises worldwide. In fact, the Simcenter Amesim drone is
characterized by components with physical models, unmodeled dynamics, time-varying
parameters, disturbances, and parametric uncertainties that make the problem complicated
and validate the research conducted meaningfully. The work is organized as follows.
In Section 2, the quadrotor mathematical model is presented. The estimators of disturbances
and a nonlinear controller to ensure robustness and asymptotic convergence are designed in

## Page 3

Machines 2023, 11, 352
3 of 23
Section 3. In Section 4, the performance of the controller and estimators are presented with
respect to Matlab and Simcenter Amesim co-simulation environment implementation with
FPGA implementation. Some considerations and future research developments conclude
the work in Section 5.
2. Mathematical Model of A Quadrotor
The quadrotor considered in this work consists of a rigid frame equipped with
four rotors (see [9,10] for a detailed description). The rotors generate the propeller force
Fi = b · ω2
p,i, which is proportional to the propeller angular velocity ωp,i, i = 1, 2, 3, 4. Pro-
pellers 1 and 3 rotate counterclockwise; propellers 2 and 4 rotate clockwise. Quadrotor
orientation with Euler angles is used. Let us indicate with RC(O, e1, e2, e3), RΓ(Ω, ε1, ε2, ε3))
the frames ﬁxed with the Earth and the quadrotor, respectively, and Ωis coincident with
the center of mass of the quadrotor (see Figure 1).
Figure 1. Quadrotor orientation using Euler angles.
The absolute position of the quadrotor in RC is described by p = (x, y, z)T, whereas
its attitude is described by the Euler angles α = (φ, θ, ψ)T, with φ ∈[−π/2, π/2), θ ∈
(−π/2, π/2), ψ ∈[−π, π) the roll, pitch, yaw angles, respectively. The sequence 3–2–1
is here considered [11]. Moreover, v = (vx, vy, vz)T, ω = (ω1, ω2, ω3)T are the linear and
angular velocities of the center of mass of the quadrotor, expressed in RC and in RΓ,
respectively. The translation dynamics, expressed in RC, and rotation dynamics, expressed
in RΓ, of the quadrotor are
˙p = v
˙v = 1
m

fp + fg + fd

˙α = M(α)ω
˙ω = J−1
−˜ω Jω + τp + τgy + τd

(1)
where m is the mass of the quadrotor, fp = R(α)ϕp is the force in RC excerted by the
propellers (ϕp is the same force, but expressed in RΓ), J (positive deﬁnite symmetric matrix
in R3×3, expressed in RΓ) is the inertia matrix of the quadrotor, and
˜ω =


0
−ω3
ω2
ω3
0
−ω1
−ω2
ω1
0


(2)

## Page 4

Machines 2023, 11, 352
4 of 23
is the so–called dyadic representation of ω. Furthermore,
ϕp =


0
0
up

,
up =
4
∑
i=1
Fi,
fg =


0
0
−mg


(3)
τp =


τ1
τ2
τ3

=



ℓb(ω2
p,2 −ω2
p,4)
ℓb(ω2
p,3 −ω2
p,1)
c(ω2
p,1 −ω2
p,2 + ω2
p,3 −ω2
p,4)



(4)
are the input forces and moments produced by the propellers (expressed in RΓ), where
ℓis the distance between the center of mass CG to the rotor shaft, and b ([b]= N s2
rad2 ) and c
([c]= N s2 m
rad2 ) are, respectively, the so–called thrust and drag factor. Obviously,




F1
F2
F3
F4



=




1
1 1 1
0
ℓ
0 −ℓ
−ℓ0 ℓ
0
c
−c c −c




−1



up
τ1
τ2
τ3



,





ω2
p,1
ω2
p,2
ω2
p,3
ω2
p,4




=




1
4b
0
−1
2bℓ
1
4c
1
4b
1
2bℓ
0
−1
4c
1
4b
0
1
2bℓ
1
4c
1
4b
−1
2bℓ
0
−1
4c








up
τ1
τ2
τ3



,
(5)
ωp,i =
r
Fi
b ,
0 ≤Fi ≤Fi,max,
0 ≤ωp,i ≤ωp,i,max,
i = 1, 2, 3, 4
where Fi,max and ωp,i,max are, respectively, the maximum forces and the angular velocities
related to each propellers due to physical limitations. Moreover, fg in (3) is the force due to
the gravity, which is expressed in RC. The vectors expressed in RΓ are transformed into
vectors in RC by the rotation matrix
Rib = R(α) =



cθcψ
sφsθcψ −cφsψ
cφsθcψ + sφsψ
cθsψ
sφsθsψ + cφcψ
cφsθsψ −sφcψ
−sθ
sφcθ
cφcθ



(6)
where c⋆= cos(⋆), s⋆= sin(⋆), ⋆= φ, θ, ψ. The angular velocity dynamics are expressed
using the matrix
M(α) =



1 sφtgθ
cφtgθ
0
cφ
−sφ
0 sφscθ
cφscθ



with tg⋆= tan(⋆), sc⋆= sec(⋆), ⋆= φ, θ, ψ. Under the assumption of small angles φ (roll)
and θ (pitch), which is acceptable in the case of a quadrotor performing non-aggressive
maneuvers, this matrix can be approximated by the identity matrix, i.e., M(α) ≃I3x3 [12].
The rolling torque τ1 is produced by the forces F2 and F4. Similarly, the pitching torque
τ2 is produced by the forces F1 and F3. Due to the Newton’s third law, the propellers
produce a yawing torque τ3 on the body of the quadrotor in the opposite direction of the
propeller rotation. Moreover, τgy = ∑4
i=1(−1)iJp,iωp,i ˜ωϵ3 is the gyroscopic torque due to
the propeller rotations, with Jp,i, i = 1, 2, 3, 4, the inertia moment of the ith motor plus
propeller, with respect to its rotation axis. Finally, fd and τd are the forces and torques
due to the external disturbances, for example due to aerodynamic forces. Considering the

## Page 5

Machines 2023, 11, 352
5 of 23
nominal values m◦, J◦
p,i = J◦
p, i = 1, 2, 3, 4, J◦= diag{J◦
1, J◦
2, J◦
3 }, f ◦
p, τ◦
p, system (1) can be
rewritten as
˙p = v
˙v = 1
m◦f ◦
p + 1
m fg + d
˙α = ω
˙ω = −J◦−1 ˜ω J◦ω + J◦−1τ◦
p + J◦−1τ◦
gy + δ
(7)
where
d =


dx
dy
dz

=
 1
m −1
m◦

fp + 1
m fd + 1
m◦

fp −f ◦
p

δ =


δ1
δ2
δ3

= −

J−1 ˜ω Jω −J◦−1 ˜ω J◦ω

+

J−1 −J◦−1
τp +

J−1τgy −J◦−1τ◦
gy

+ J−1τd+
+ J◦−1(τp −τ◦
p )
(8)
are the perturbations acting on the drone, due to parametric uncertainties and external
disturbances, and
τ◦
gy =
4
∑
i=1
(−1)iJ◦
pωp,i ˜ωϵ3 = J◦
pωp


ω2
−ω1
0


(9)
is the nominal gyroscopic torque due to the propeller rotations, with ωp = −ωp,1 + ωp,2 −
ωp,3 + ωp,4 the so-called rotor relative speed. With these positions, mathematical model (7)
of the quadrotor can be expressed as
˙x = vx,
˙y = vy,
˙z = vz
˙vx =

cφsθcψ + sφsψ
 u◦
p
m◦+ dx
˙vy =

cφsθsψ −sφcψ
 u◦
p
m◦+ dy
˙vz = −g + cφcθ
u◦
p
m◦+ dz
˙φ = ω1,
˙θ = ω2,
˙ψ = ω3
˙ω1 = J◦
2 −J◦
3
J◦
1
ω2ω3 +
J◦
p
J◦
1
ωpω2 + 1
J◦
1
τ◦
1 + δ1
˙ω2 = J◦
3 −J◦
1
J◦
2
ω1ω3 −
J◦
p
J◦
2
ωpω1 + 1
J◦
2
τ◦
2 + δ2
˙ω3 = J◦
1 −J◦
2
J◦
3
ω1ω2 + 1
J◦
3
τ◦
3 + δ3.
(10)
Remark 1. Within the vectors d and δ, there are the variations of mass m, moments of inertia,
thrust coefﬁcient b and drag coefﬁcient c linked to the propulsion force Fp, as well as possible external
perturbations and unmodeled dynamics that are considered in Fd and τd, so as to incorporate the
parametric variations, the unmodeled dynamics and external perturbations (as wind) that act both
at the level of linear and angular velocity level (see Section 4.2).
Assumption 1. fp and τd, and their derivatives, are bounded.
3. Design of Nonlinear Controller
The output vector to be controlled is composed by the 3D position and yaw rate and
the control aim is to design a controller, in the presence of disturbances and parameters

## Page 6

Machines 2023, 11, 352
6 of 23
uncertainty, to ensure the asymptotic converge of the variables χ = (x, y, z, ψ) to some
reference trajectories χr = (xr, yr, zr, ψr). To this aim, let us consider the kinematic errors
eχ = χ −χr =




x −xr
y −yr
z −zr
ψ −ψr



=




ex
ey
ez
eψ




whose dynamics are
˙eχ =




˙ex
˙ey
˙ez
˙eψ



=




vx −˙xr
vy −˙yr
vz −˙zr
ω3 −˙ψr



=




evx
evy
evz
eω3




and with
¨eχ =




¨ex
¨ey
¨ez
¨eψ



=




˙vx −¨xr
˙vy −¨yr
˙vz −¨zr
˙ω3 −¨ψr



=




˙evx
˙evy
˙evz
˙eω1



=















cφsθcψ + sφsψ
 u◦
p
m◦+ dx −¨xr

cφsθsψ −sφcψ
 u◦
p
m◦+ dy −¨yr
−g + cφcθ
u◦
p
m◦+ dz −¨zr
J◦
1 −J◦
2
J◦
3
ω1ω2 + 1
J◦
3
τ◦
3 + δ3 −¨ψr














=
=















cφsθrcψ + sφrsψ
 u◦
p
m◦+ dx −¨xr

cφsθrsψ −sφrcψ
 u◦
p
m◦+ dy −¨yr
−g + cφcθ
u◦
p
m◦+ dz −¨zr
J◦
1 −J◦
2
J◦
3
ω1ω2 + 1
J◦
3
τ◦
3 + δ3 −¨ψr














+












(sθ −sθr)cφcψ + (sφ −sφr)sψ
 u◦
p
m◦

(sθ −sθr)cφsψ −(sφ −sφr)cψ
 u◦
p
m◦
0
0











.
Setting
 sφr
sθr

= 1
σ
 cφcθsψ −cφcθcψ
cθcψ
cθsψ
 
¨xr −ˆdx + wx
¨yr −ˆdy + wy
!
u◦
p = m◦
cφcθ

¨zr + g −ˆdz + wz

τ◦
3 = J◦
3

¨ψr −J◦
1 −J◦
2
J◦
3
ω1ω2 −ˆδ3 + wψ

wj = −kj,0Iej −kj,1ej −kj,2evj,
j = x, y, z
wψ = −kψ,0Ieψ −kψ,1eψ −kψ,2eω3
˙Iej = ej,
j = x, y, z, ψ
(11)
where σ = ¨zr + g −ˆdz + wz, kj,0, kj,2 > 0 and kj,1 > kj,0/kj,2, j = x, y, z, ψ, one gets
¨eχ =







wx
wy
wz
wψ







+








µx
u◦
p
m◦
µy
u◦
p
m◦
0
0








+







dx −ˆdx
dy −ˆdy
dz −ˆdz
δ3 −ˆδ3







,

## Page 7

Machines 2023, 11, 352
7 of 23
where
µx = [(sθ −sθr)cφcψ + (sφ −sφr)sψ],
µy = [(sθ −sθr)cφsψ −(sφ −sφr)cψ].
As far as the errors sφ −sφr, sθ −sθr are concerned, let us consider the roll error eφ = φ −φr
and the pitch error eθ = θ −θr, with φr = arcsin sφr, θr = arcsin sθr. Their dynamics are
˙eφ = ω1 −˙φr = eω1,
˙eθ = ω2 −˙θr = eω2
˙eω1 = J◦
2 −J◦
3
J◦
1
ω2ω3 +
J◦
p
J◦
1
ωpω2 + 1
J◦
1
τ◦
1 + δ1 −¨φr
˙eω2 = J◦
3 −J◦
1
J◦
2
ω1ω3 −
J◦
p
J◦
2
ωpω1 + 1
J◦
2
τ◦
2 + δ2 −¨θr
and the controls
τ◦
1 = J◦
1 ¨φr −(J◦
2 −J◦
3 )ω2ω3 −J◦
pωpω2 −J◦
1 ˆδ1 + J◦
1 wφ
τ◦
2 = J◦
2 ¨θr −(J◦
3 −J◦
1 )ω1ω3 + J◦
pωpω1 −J◦
2 ˆδ2 + J◦
2 wθ
wφ = −kφ,0Ieφ −kφ,1eφ −kφ,2eω1
wθ = −kθ,0Ieθ −kθ,1eθ −kθ,2eω2
(12)
with kj,0, kj,2 > 0, kj,1 > kj,2/kj,0, j = φ, θ. Therefore, one obtains


¨ex
¨ey
¨ez

=


wx
wy
wz

+






µx
u◦
p
m◦
µy
u◦
p
m◦
0






+



dx −ˆdx
dy −ˆdy
dz −ˆdz



(13a)


¨eφ
¨eθ
¨eψ

=


wφ
wθ
wψ

+


δ1 −ˆδ1
δ2 −ˆδ2
δ3 −ˆδ3


(13b)
Remark 2. For the computation of the ﬁrst and second derivatives of the signals φ and ψ, since it
is not possible to have a direct analytical expression, they will be implemented using the high-order
sliding mode differentiator (HOSMD) designed in [13].
Disturbances Estimator
To achieve robustness of the closed-loop system with respect to external disturbances,
a robust disturbance estimator is designed. In what follows, given the measured variables

## Page 8

Machines 2023, 11, 352
8 of 23
the HOSM estimator wants to converge in ﬁnite time to disturbances values, ﬁnally, based
on [14], one considers,
˙νx =

cφsθcψ + sφsψ
 u◦p
m◦−λx,1⌊νx −vx⌉1/2 + ˆdx
˙νy =

cφsθsψ −sφcψ
 u◦p
m◦−λy,1

νy −vy
1/2 + ˆdy
˙νz = −g + cφcθ
u◦p
m◦−λz,1⌊νz −vz⌉1/2 + ˆdz
˙ν1 = J◦
2 −J◦
3
J◦
1
ω2ω3 +
J◦p
J◦
1
ωpω2 + 1
J◦
1
τ◦
1 −λφ,1⌊ν1 −ω1⌉1/2 + ˆδ1
˙ν2 = J◦
3 −J◦
1
J◦
2
ω1ω3 −
J◦p
J◦
2
ωpω1 + 1
J◦
2
τ◦
2 −λθ,1⌊ν2 −ω2⌉1/2 + ˆδ2
˙ν3 = J◦
1 −J◦
2
J◦
3
ω1ω2 + 1
J◦
3
τ◦
3 −λψ,1⌊ν3 −ω3⌉1/2 + ˆδ3
˙ˆdj = −λk,2
j
νj −vj
m0
˙ˆδi = −λk,2⌊νi −ωi⌉0
(14)
which ensure the convergence in ﬁnite time of the estimation errors dj −ˆdj, j = x, y, z,
and δi −ˆδi, i = 1, 2, 3, for some λk,1, λk,2 with k = x, y, z, φ, θ, ψ, where ⌊σ⌉1/2 = |σ|1/2sign(σ),
⌊σ⌉0 = sign(σ) for any scalar signal σ.
Theorem 1. Given the reference χr, bounded along with its derivatives ˙χr, ¨χr, the controller (11),
(12), with the gains λη,1, λη,2 > 0 with η = x, y, z, φ, θ, ψ, ensures that the error eχ tends
to zero asymptotically and the perturbation estimations ˆdη, in (14) tends to dη in ﬁnite time,
with η = x, y, z, φ, θ, ψ.
Proof. Since the subsystems (13a) and
(13b), with

dx −ˆdx
dy −ˆdy
dz −ˆdz
δ1 −
ˆδ1
δ2 −ˆδ2
δ3 −ˆδ3
T
as input, is input-to-state stable (in fact, the dynamics matrix of
each subsystem is Hurwitz, and the ISS Lyapunov function is quadratic) and the system,
for η = x, y, z, φ, θ, ψ,
ξη = νη −vη, ˜dη = dη −ˆdη,
˙ξη = −λη,1

ξη
1/2 + ˜dη
˙˜dη = −λη,2

ξη
0
converges to the origin in ﬁnite time, and the systems (13a) and (13b) is globally uniformly
exponentially stable. In fact, considering the part relating to the position on the x-axis χx
(the demonstrations are analogous for the other variables taken into consideration), it is
possible to consider the following Lyapunov function
Ve,x = 1
2χT
x Pe,xχx,
χx =
 χx,1
χx,2

=
 
⌊νx −vx⌉1/2
dx −ˆdx
!
with
Pe,x = PT
e,x =

λ2
x,1 + 4λx,2
−λx,1
−λx,1
2

> 0.

## Page 9

Machines 2023, 11, 352
9 of 23
since λx,2 > 0. Notice that λPe,x
min∥χx∥2
2/2 ≤Ve,x ≤λPe,x
max∥χx∥2
2/2, with λPe,x
min, λPe,x
max the
minimum and maximum eigenvalues of Pe,x. To show the convergence, one computes the
derivative of the Lyapunov candidate
˙Ve,x = −
1
2χx,1
χT
x Pe,xAxχx = −λx,1
2χx,1
χT
x Qe,xχx
where
Qe,x =
 
(λ2
x,1 + 2λx,2) −λx,1
−λx,1
1
!
> 0
Pe,xAx =
 
λ2
x,1 + 4λx,2 −λx,1
−λx,1
2
! 
λx,1 −1
2λx,2
0
!
= λx,1Qe,x > 0
since λx,1, λx,2 > 0. Since ∥χx∥2
2 = |ξx| + ˜d2
x, clearly |ξx|1/2 ≤∥χx∥2 ≤
√
2 V1/2
e,x /
q
λPe,x
min,
so that
−
1
|ξx|1/2 ≤−
q
λPe,x
min
√
2
1
V1/2
e,x
and
˙Ve,x = −
λx,1
2|ξx|1/2 χT
x Qe,xχx ≤−λQe,x
min∥χx∥2
2 ≤−λQe,x
min
λPe,x
max
2Ve,x = −γe,x
minV1/2
e,x
γe,x
min = λx,1
q
λPe,x
min
√
2 λPe,x
max
λQe,x
min
where
λQe,x
min =
λ2
x,1 + 2λx,2 + 1
2
−1
2
q
(λ2
x,1 + 2λx,2 + 1)2 −8λx,2.
This implies that ξx, ˜dx converge to zero in ﬁnite time for λx,1, λx,2 > 0, since
q
λPe,x
min
√
2
∥χx(t)∥2 ≤V1/2
e,x (t0) −γe,x
min
2
(t −t0) ≤
q
λPe,x
max
√
2
∥χx(t0)∥2 −γe,x
min
2
(t −t0) = 0
for ¯t = t0 +
q
2λPe,x
max ∥χx(t0)∥2/γe,x
min.
The control scheme is divided into an inner and outer loop design. The inner loop
design is responsible for attitude and altitude control, while the outer loop is responsible
for controlling lateral and longitudinal motion. The desired trajectories for translation
and heading movements are provided externally, while the roll and pitch trajectories are
generated from the outer loop. The functional scheme of the proposed controller is the one
shown in Figure 2.

## Page 10

Machines 2023, 11, 352
10 of 23
𝑥, 𝑦
መ𝑑𝑥, መ𝑑𝑦
Desired reference trajectory
𝜓𝑟𝑒𝑓, 𝑥𝑟𝑒𝑓, 𝑦𝑟𝑒𝑓, 𝑧𝑟𝑒𝑓
Inner-loop control
𝜏to 𝜔
conversion 
QUADROTOR
Outer-loop control
Uncertainties and 
disturbances
estimators
መ𝑑𝑧, መ𝛿1, መ𝛿2, መ𝛿3
𝑥𝑟𝑒𝑓, 𝑦𝑟𝑒𝑓
𝜙𝑟𝑒𝑓, 𝜃𝑟𝑒𝑓
𝜓𝑟𝑒𝑓, 𝑧𝑟𝑒𝑓
𝑥, 𝑦, 𝑧, 𝜙, 𝜃, 𝜓
𝑧, 𝜙, 𝜃, 𝜓
𝜏1
𝑜
𝜏2
𝑜
𝜏3
𝑜
𝑢𝑝𝑜
𝜔𝑝,1 𝜔𝑝,2 𝜔𝑝,3 𝜔𝑝,4
Figure 2. Functional block diagram of the controller.
4. Simulation and Results Analysis
The performance of the proposed controller is discussed in this section. First of all,
the simulation environment used is brieﬂy described in Section 4.1; then, the main wind
models used in aerospace research are brieﬂy recalled in Section 4.2, and speciﬁcally, the
one used in the simulations of this paper is described. Finally, the results obtained by the
robust controller in a generic ﬂight mission are shown and compared in Section 4.3 with the
non-robust controller in the presence of disturbances and parameters uncertainty present
in the physical model of the chosen simulation environment.
4.1. Co-Simulation Environment with Matlab-Simulink and Simcenter Amesim with
FPGA Implementation
The software Simcenter Amesim (see [15]), a multi-physics system simulation tool
developed by Siemens Digital Industries Software, is used to model the different subsystems
of the UAV: batteries, propulsion chain and ﬂight dynamics. In general, the tool provides
off-the-shelf components available in libraries, covering several physical (ﬂuids, mechanical,
electrical, thermal...) and application (aerospace, automotive, gas turbines...) domains.
Those subsystem plant models have been favorably compared against experimental data
provided by the manufacturers ﬁrst. The use of this tool was therefore aimed at validating
the controller and the estimators, which in the ﬁrst instance were developed and tested
only in the Matlab–Simulink environment. The overall plant model was then integrated
in a co-simulation framework capable of modeling drone’s navigation sensors, mission
environment and algorithms to simulate the drone’s behavior under different scenarios. The
model present in Simcenter Amesim is complex with respect to the reference mathematical
model considered for the design of the controller presented in Section 2; therefore, it
contains both unmodeled dynamics and parameters that are time-varying and is therefore a
valid test bed to evaluate controller’s performance. In the present research, the UAV model
considered is seen as a black box model, and the parameters used in the model-based
controller have been preliminary identiﬁed with Least Square Method. For example, at the
modeling level, the aerodynamic coefﬁcients such as the thrust and drag coefﬁcient play an
important role in the design of the controller. In fact, several studies have shown that they
are variable based on the operating conditions of the drone. In both the physical models
used in the advanced, realistic simulator used in this paper (see [15]) and in experimental
studies, they are determined by multivariable functions (see [16,17]) such as orientation,

## Page 11

Machines 2023, 11, 352
11 of 23
angular and total velocity as well as the geometric characteristics themselves. For these
reasons, they are parameters that can be identiﬁed in a static way, and this is the practice
that can be followed, but they are actually time-varying during the simulation. For this
reason, it is necessary to take them into account in the design phase of the controller in order
to make it robust, and in our case, all these variations in propulsion level are also considered
in the disturbance term. The drone simulation parameters used in the model-based design
controller are presented in Table 1.
Table 1. Nominal quadrotor parameters.
m
Mass of the airframe
5 kg
l
Distance of CoG to the rotor
shaft
0.3 m
J1
Inertia in the x-axis
0.011521 kg · m2
J2
Inertia in the y-axis
0.0362132 kg · m2
J3
Inertia in the z-axis
0.029142 · m2
Jp
Inertia of the propellers
0.0003 · m2
g
Gravity acceleration
9.81 m · s−2
b
Trust factor
4.5625 × 10−5 N · s2 · rad−2
c
Drag factor
1.375 × 10−5 N · s2 · rad−2 · m
In addition to the use of the physical model of the Siemens drone with identical perfor-
mance to the real one, a perfect candidate for this application is the FPGA implementation,
since it can provide strict real–time execution, high power efﬁciency, small size, and high
reliability, at the cost of a reduced dynamic range. Speciﬁcally, the Intel Cyclone 10 LP
FPGA was available and corresponded to what was needed; then, it has been used as a
reference, and it comes on a minimal board, which is useful for actual power consumption
tests and fast prototyping, allowing installation on small UAVs for real-world tests. With-
out going into the details of the FPGA implementation, Figure 3 shows the structure of the
implemented controller, which is only part of a complete system architecture. During the
implementation on FPGA, the typical problems related to the operations of trigonometric
function, their inverse, reciprocal or division, square root, computation of the derivatives,
discrete approximation, variables normalization, as well as to the ﬁxed-point arithmetic of
the controller and input variables have been addressed. The simulations presented were
carried out in a co-simulation environment between Matlab and Simcenter Amesim in
order to have a complex model on which to test the controller and were implemented in
FPGA at the end.

## Page 12

Machines 2023, 11, 352
12 of 23
Figure 3. Some detail of the FPGA control architecture.
4.2. Environmental Disturbances Acting on the Quadrotor: Wind Modeling
The categories, features, and mathematical models of the wind, which have a big
inﬂuence on UAV in the low-altitude condition, can be classiﬁed in four groups: constant
wind, turbulent ﬂow, many kinds of wind shear, and the propeller vortex (see [18]). The
attitude, speed, and position of UAV are sensitive to wind disturbance, and consequently,
the wind is seen as a parameter that has the bigger inﬂuence on efﬁciency. The main
features of each wind category are shortly evoked below:
•
Constant wind deals with the average wind speed in a speciﬁed environment. Con-
stant wind does not exist in nature, because it is only the reference value of the wind
speed in a given environment. To perform a more realistic simulation test, other types
of wind need to be considered. Generally through statistical data, it is possible to
obtain its value in the different temporal or spatial conditions. The numerous relevant
websites that log wind data are supportive in this regard. Usually, constant wind
is used in simulation tests of UAVs at ﬁrst, but it is unable to reproduce the ﬂight
environment correctly.
•
Turbulent ﬂow is a continuous random change, which is always conducted by con-
stant wind. The source of turbulent ﬂow is coupled to many elements, such as wind
shear, heat exchange, topographical factors, etc. (see [19]). Stochastic Process Theory
is commonly used to describe atmospheric turbulence in engineering applications.
Turbulent ﬂow models incorporate the Dryden model and the Von Karman model,
both of which depend on a vast amount of measurements and statistics (see [20]).
The difference is that Dryden’s model ﬁnds the correlation function of turbulence
before giving rise to the spectral function, while Von Karman, on the contrary, ﬁrst es-
tablishes the spectral function and then deduces the correlation function of turbulence.
From the aforementioned literature, it emerges that between the two models, there is
no relevant difference for the application use in the simulation phase; therefore, both
can be used within engineering problems designed to simulate the wind.
•
Wind shear The American National Research Council deﬁnes the degree of wind
shear as the ratio of the difference between two wind vectors at two points and the
distance between those two points. There are many sources of wind shear. In UAV
ﬂight, common low-altitude wind shear contains frontal wind shear, topography-
induced wind shear, microdownburst and night jet wind shear. The frequency of the
wind shear is also not as large as the turbulent ﬂow, it changes every few seconds
as its maximum frequency. The speed of the wind shear is a function of the spatial
position, and its model is relatively simple. In the simulation test, the abrupt change
in constant wind speed is used to indicate the occurrence of wind shear. Wind shear
is a discrete or deterministic wind speed, which often occurs in a very short time,

## Page 13

Machines 2023, 11, 352
13 of 23
and it is a strong atmospheric perturbation. The wind shear model can be divided
into several categories based on its proﬁle geometry, including the rectangular model,
the trapezoidal model, and the ’1-consine’ model.
•
Propeller vortex is related to large manned aircraft. There are wake vortex caused
by aircraft wings that signiﬁcantly affect other aircraft. As for UAVs, due to their
slower ﬂight speed, the propeller vortex will no longer play an important role, while
here, another vortex caused by the propellers could be considered, just as the name
suggests, but it can be kept in consideration in the modeling phase of the system to
be controlled.
The Principle of Wind Affects the UAV
All kind of wind modify the speed of the UAV, as a result altering the angle of attack
and the angle of drift, which inﬂuences the values of the aerodynamic derivatives and
eventually causes disturbances to the outcome force and torque of the UAV. In general,
the most common approach to relate the consequences of winds on UAVs is from the point
of view of speed. The wind models cited above explain only the distribution of velocity
in space and time. Unfortunately, under most conditions, the induced speed of a certain
wind ﬁeld is not uniform, such as the wind gust ﬁeld and the vortex ﬁeld of the propeller,
which denotes that the speed is not a constant value and changes together with the different
parts of the UAV. To ﬁgure out this problem, in [21], we proposed an averaging way to
calculate the actual wind speed and the wind gradient in order to derive the relationships
between the variation of the air speed and the actual wind as well as between the variation
of the body angular velocities and wind gradient. On the other hand, from the point
of view of force, the effects of the non-uniform part of the ﬂow ﬁeld are considered an
external force on the UAV. It is a well-known fact that interaction forces are the essential
reason for the change in the kinetic states of objects, and the force caused by air is called
resistance. In the simulation results presented, the Dryden wind turbulence model is used.
The Dryden model considers the linear and angular velocity components of continuous
gusts as spatially varying stochastic processes and speciﬁes each component’s power
spectral density. The Dryden wind turbulence model is characterized by rational power
spectral densities, so exact ﬁlters can be designed that take white noise inputs and output
stochastic processes with the Dryden gusts’ power spectral densities. The trends of the
wind disturbances considered in the subsequent simulation are shown in Figure 4, dividing
the contributions with respect to the three reference axes by linear and angular speed. For
more mathematical details on the considered model, it is possible to refer to [22]. Table 2
shows the main parameters and the values used for the generation of disturbances with
reference to the Simulink block called “Dryden Wind Turbulence Model (Continuous)”.
The gains value of the HOSM controller and of the disturbances estimators used in the
simulations shown are reported in the Table 3. We want to emphasize that controller
parameters give a formal solution of the stated control problem. Nevertheless, in practice,
one often requires to calibrate the convergence rate, either to slow it down (relaxing the
burden on the actuators) or to accelerate it in order to meet some system requirements.
Consider, in this context, redundantly augmenting the magnitude parameter does not
accelerate the convergence but rather only increases the chattering, while its reduction may
lead to a loss of convergence.

## Page 14

Machines 2023, 11, 352
14 of 23
Table 2. Dryden Wind Turbulence Model Parameters.
Model
Continuos Dryden (+q −r): Use continuous
Type
representation of Dryden velocity
spectra with positive vertical
and negative lateral angular rates spectra.
Altitude
z
UAV
q
v2x + v2y + v2z
Velocity
Measured
15 m/s.
wind speed
Measured wind speed at a height of 6 m
speed
Wind
0
direction
Measured wind direction at a height of 6 m
(degrees clockwise from north)
to aid in transforming the low-altitude
turbulence model into a body coordinates.
Turbulence
10−2 -Light
intensity
Probability of the turbulence intensity being
exceeded
Wingspan
10 m
required in the turbulence calculation on the
angular rates.
Band limited
0.01 s
noise sample
Noise sample time at which
time
the unit variance white noise signal is
generated
Noise seeds
(23,341 23,342 23,343 23,344)
(ug vg wg pg)
Random noise seeds, speciﬁed as a
four-element vector one for each
of the three velocity components
and one for the roll rate.
Table 3. Parameters of HOSM Controller and Estimators.
kx,0 = 3
kx,1 = 10
kx,2 = 3
ky,0 = 3
ky,1 = 10
ky,2 = 2
kz,0 = 3
kz,1 = 10
kz,2 = 2
kφ,0 = 1.5
kφ,1 = 5
kφ,2 = 1
kθ,0 = 1.5
kθ,1 = 5
kθ,2 = 1
kψ,0 = 2.7
kψ,1 = 9
kψ,2 = 1.8
λx,1 = 10
λx,2 = 3
λy,1 = 10
λy,2 = 3
λz,1 = 10
λz,2 = 3
λφ,1 = 2
λφ,2 = 1
λθ,1 = 2
λθ,2 = 1
λψ,1 = 2
λψ,2 = 1

## Page 15

Machines 2023, 11, 352
15 of 23
0
1
2
3
4
5
6
7
8
9
10
−1
−0.5
0
0.5
1
Time [s]
[m/s]
(a)
0
1
2
3
4
5
6
7
8
9
10
−4
−2
0
2
4
Time [s]
[degree/s]
(b)
Figure 4. Disturbances for linear and angular velocity: (a) dx (green), dy (blue), dz (red), (b) δ1 (green),
δ2 (blue), δ3 (red).
4.3. Simulation Results
In the test mission shown, we consider a rest-to-rest maneuver of the quadrotor with
an initial state [x y z ψ] = [0 0 0 0] and a ﬁnal state [x y z ψ] = [4 5 15 π/4]. In fact, we
assumed zero linear and angular velocity of the UAV at the boundary states, with zero
body orientation at time t = 0. The reference generator of the trajectories to be tracked
is generated in such a way to have minimum accelerations and with a time suitable for
carrying out the mission (see [23] for more details). Figures 5–12 are representative of
the simulation considered in the cosimulation environment with FPGA implementation
described in (Section 4.1): they compare and show the tracked characteristic state variables
between the robust controller with disturbances compensation and the non-robust con-
troller and the errors, the control inputs, the disturbances dx, dy, dz, δ3 and their estimation
ˆdx, ˆdy, ˆdz, ˆδ3; the effectiveness of the robust controller compared to the non-robust one
and good estimation of the disturbances is evident. In fact, if the wind disturbance is
not compensated, it takes the drone away from the trajectory to follow and leads it to
dangerous states in terms of dynamics and greater energy consumption due to the removal
from the desired trajectory. In particular, Figures 5–7 show the trends of the longitudinal
(x), latitudinal (y), and altitudinal (z) positions, respectively, and their errors: in order to
make evident the tracking difference between the robust and non-robust controller, their
trends have been separated as well as their errors. The tracking errors of the non-robust
controller are always large due to disturbances and parametric variations, but in the ﬁnal
part of the simulation, it cannot even keep the drone stable. With the same philosophy at
the graphic level, Figure 8 shows the trend of yaw rate for the two controllers: the results
are similar; therefore, with better performance than the robust controller, it should be
emphasized that unlike the previous ﬁgures in this case, probably due to the wind and the
unknown time-varying dynamics of some coefﬁcients present in the simulator, the error
reaches values of 12 degrees while keeping it always bounded.
Figure 9 shows the control inputs of robust control expressed as angular velocities of
the four propellers. Modern-day ESC protocols can communicate at speeds of 37.5 kHz or

## Page 16

Machines 2023, 11, 352
16 of 23
greater (in general, it is between 30 and 60 kHz because of the relatively low inductance of
the high-speed motors and the potential interference to sensor boards), see [24]. The fre-
quency of the actuation signals of the robust controller is 100 Hz and thus abundantly meets
the requirements of modern commercial drones. The control inputs in the robust case have
more rapid variations, while in the non-robust case, they assume a smooth trend: this is due
to the terms of the estimators trying to compensate for what they see as possible parametric
disturbance or uncertainty. Figure 10 shows the three-dimensional spatial trajectories of
the two controlled drones in order to be able to visually quantify the error that occurs
when the controller is not made robust with respect to disturbances. It is evident that the
error that non-robust control makes at the 3D trajectory level is high, and therefore, there
is an increase in consumption and the risk of drone instability. Finally, the disturbances
dx-dy-dz-δ3 and their estimates used in robust control, together with their respective errors,
are shown in Figures 11 and 12. The estimates are good for all disturbances: we note the
presence of noise and a slightly larger error in δ3, which is an event that causes errors of
some degree in the tracking of the yaw rate, error due to the complex simulator considering
that it has variable parameters over time, dynamics not considered in our model, and
physical models based on experimental data; in fact, in the simulations not shown due to
the lack of space made with the plant in Matlab, this does not happen.
To compare the performance of two proposed controllers in the considered mission,
the Mean Absolute Error (MAE), Mean Square Error (MSE), Integral Squared Error (ISE),
Integral Absolute Error (IAE), Integral Time-Weighted Absolute Error (ITAE) and Integral
Time Square Error (ITSE) measures have been considered as comparative indices for the
tracking along x, y, z and ψ. These performance indices are deﬁned, for the variable x
(the argument is analogous for the other variables) with respect to the reference xre f to be
tracked, during the N sampling instants, as follows
MAE = ∑N
i=1[xre f,i −xi]
N
MSE = 1
N
N
∑
i=1
(xre f,i −xi)2
ISE =
Z
(xre f −x)2dt
IAE =
Z
| xre f −x | dt
ITAE =
Z
(t | xre f −x |)dt
where xre f,i and xi are, respectively, the values of the variable xre f and x at sampling time
i, and ISE, IAE and ITAE integrate over time. The results are reported in Table 4, which
shows the difference for each performance index of the tracked variables between the
non-robust and robust controller.

## Page 17

Machines 2023, 11, 352
17 of 23
0
2
4
6
8
10
0
1
2
3
4
Time [s]
x [m]
(a)
0
2
4
6
8
10
0
2
4
6
8
10
Time [s]
xnc [m]
(b)
0
2
4
6
8
10
−0.1
−5 · 10−2
0
5 · 10−2
0.1
Time [s]
ex [m]
(c)
0
2
4
6
8
10
−6
−4
−2
0
2
Time [s]
exnc [m]
(d)
Figure 5. (a) Longitudinal motion of the UAV: the reference xre f (black), x with robust control (blue);
(b) Longitudinal motion of the UAV: the reference xre f (black), xnc with non-robust control (red);
(c) Longitudinal error motion of the UAV with robust control ex (blue); (d) Longitudinal error motion
of the UAV with non-robust control exnc (red).
0
2
4
6
8
10
0
2
4
Time [s]
y [m]
(a)
0
2
4
6
8
10
0
2
4
6
8
10
Time [s]
ync [m]
(b)
0
2
4
6
8
10
−0.1
−5 · 10−2
0
5 · 10−2
0.1
Time [s]
ey [m]
(c)
0
2
4
6
8
10
−6
−4
−2
0
2
Time [s]
eync [m]
(d)
Figure 6. (a) Latitudinal motion of the UAV: the reference yre f (black), y with robust control (blue);
(b) Latitudinal motion of the UAV: the reference yre f (black), ync with non-robust control (red);
(c) Latitudinal error motion of the UAV with robust control ey (blue); (d) Latitudinal error motion of
the UAV with non-robust control eync (red).

## Page 18

Machines 2023, 11, 352
18 of 23
0
2
4
6
8
10
0
5
10
15
Time [s]
z [m]
(a)
0
2
4
6
8
10
0
5
10
15
Time [s]
znc [m]
(b)
0
2
4
6
8
10
−4
−2
0
2
4 ·10−2
Time [s]
ez [m]
(c)
0
2
4
6
8
10
0
1
2
Time [s]
eznc[m]
(d)
Figure 7. (a) Altitudinal motion of the UAV: the reference zre f (black), z with robust control (blue);
(b) Altitudinal motion of the UAV: the reference zre f (black), znc with non-robust control (red);
(c) Altitudinal error motion of the UAV with robust control ez (blue); (d) Altitudinal error motion of
the UAV with non-robust control eznc (red).
0
2
4
6
8
10
0
20
40
Time [s]
ψ [degree]
(a)
0
2
4
6
8
10
−100
0
100
Time [s]
ψnc [degree]
(b)
0
2
4
6
8
10
0
10
Time [s]
eψ [degree]
(c)
0
2
4
6
8
10
−100
0
100
200
Time [s]
eψnc[degree]
(d)
Figure 8. (a) UAV yaw angle: the reference ψre f (black), ψ with robust control (blue); (b) UAV yaw
angle: the reference ψre f (black), ψnc with non-robust control (red); (c) yaw angle error of the UAV
with robust control eψ (blue); (d) yaw angle error of the UAV with non-robust control eψnc (red).

## Page 19

Machines 2023, 11, 352
19 of 23
0
1
2
3
4
5
6
7
8
9
10
0
2,000
4,000
6,000
Time [s]
ωp,1 [rpm]
(a)
0
1
2
3
4
5
6
7
8
9
10
0
2,000
4,000
6,000
Time [s]
ωp,2 [rpm]
(b)
0
1
2
3
4
5
6
7
8
9
10
0
2,000
4,000
6,000
Time [s]
ωp,3 [rpm]
(c)
0
1
2
3
4
5
6
7
8
9
10
0
2,000
4,000
6,000
Time [s]
ωp,4 [rpm]
(d)
Figure 9. Propulsion angular velocities of robust (blue) and non-robust controller (red): ωp,1 (a),
ωp,2 (b), ωp,3 (c), ωp,4 (d).
0
2
4
6
8
10
0
2
4
6
8
10
0
5
10
15
x [m]
y [m]
z [m]
3D Trajectory
Figure 10. Three-dimensional (3D) drone trajectory: reference (black), robust control (blue), and non-
robust control (red). The red circle and the red cross indicate, respectively, the starting and ending
point of 3D reference trajectory.

## Page 20

Machines 2023, 11, 352
20 of 23
0
2
4
6
8
10
−1
−0.5
0
0.5
Time [s]
[m/s]
(a)
0
2
4
6
8
10
−0.5
0
0.5
Time [s]
[m/s]
(b)
0
2
4
6
8
10
−4
−2
0
2
4 ·10−2
Time [s]
[m/s]
(c)
0
2
4
6
8
10
−5
0
5 ·10−2
Time [s]
[m/s]
(d)
Figure 11. Disturbances estimations: (a) dx (blue) and ˆdx (red), (b) dy (blue) and ˆdy (red), (c) dx −ˆdx,
(d) dy −ˆdy.
0
2
4
6
8
10
−1
−0.5
0
0.5
1
Time [s]
[m/s]
(a)
0
2
4
6
8
10
−4
−2
0
2
4
Time [s]
[degree/s]
(b)
0
2
4
6
8
10
−0.1
−5 · 10−2
0
5 · 10−2
0.1
Time [s]
[m/s]
(c)
0
2
4
6
8
10
−0.2
−0.1
0
0.1
0.2
Time [s]
[degree/s]
(d)
Figure 12. Disturbances estimations: (a) dz (blue) and ˆdz (red), (b) δ3 (blue), and ˆδ3 (red), (c) dz −ˆdz,
(d) δ3 −ˆδ3.
Finally, the control effort for each of the two controllers is also reported in Table 5. It
is computed as the time integral of the square of the angular velocity for each propeller.
The effort of non-robust control is greater, but above all, it has not fulﬁlled the mission
it was supposed to carry out, and therefore, additional time and energy will be required.
In conclusion, Tables 4 and 5 point out, respectively, that the robust controller has better
performance in terms of tracking error and lower total actuation effort.

## Page 21

Machines 2023, 11, 352
21 of 23
Future work will deal with a comparison with another control strategy such as a
neuroadaptive learning algorithm for constrained nonlinear systems with disturbance
rejection [25] and asymptotic tracking with novel integral robust schemes for mismatched
uncertain nonlinear systems [26].
Table 4. Performance indices for the x, y, z and ψ tracking errors.
Controller
Controlled Variable
MAE
MSE
ISE
IAE
ITAE
ITSE
Non-robust
x
0.4312
1.3198
12.92
4.2777
35.9148
125.34
Robust
x
0.018
0.000063
0.0063
0.1798
0.9743
0.0339
Non-robust
y
0.3867
1.3198
7.0007
3.8442
32.3692
66.1772
Robust
y
0.036
0.0019
0.0196
0.3604
2.2055
0.127
Non-robust
z
0.216
0.1321
1.2969
2.1505
13.9362
11.0271
Robust
z
0.0124
0.000021
0.0021
0.1238
0.5591
0.0089
Non-robust
ψ
19.3308
1492.2
1475.3
1.9254
1655.83
138,009
Robust
ψ
3.0647
17.5
175.7
30.6552
1.3336
629
Table 5. Actuation effort of robust and non-robust controllers as propeller angular velocity square
integral along all the mission time.
Controller
Non-Robust
Robust
ωp,1
2.535937464 × 108
2.522437042 × 108
ωp,2
2.534601465 × 108
2.512100166 × 108
ωp,3
2.533127333 × 108
2.514066778 × 108
ωp,4
2.534819281 × 108
2.515695169 × 108
Total
1.013848554 × 109
1.006429915 × 109
5. Conclusions and Future Works
This paper presents a dynamic controller for a quadrotor where the user has partial
knowledge of the model and in the presence of environmental disturbances such as wind
along the linear and angular velocity. The proposed PI-like controller is able to compensate
these issues by means of the use of HOSM estimators. The performance of such a controller
has been tested in a co-simulation integrated environment between Matlab-Simulink and
Simcenter Amesim with FPGA implementation. The results obtained by the robust con-
troller are better than a basic version of the control both in terms of desired trajectories
tracking and of actuation effort.
Future investigations will concern the development of theoretical results concerning
the digital implementation of the proposed controller by exploiting the methodologies
provided, for instance, in [27,28], experimental simulation and multi-agent (quadrotor)
control systems in the presence of delay, quantization, and transmission errors (see [29]).
Author Contributions: Conceptualization, D.B. and S.D.G.; methodology, D.B. and S.D.G.; software,
D.B. and M.D.F.; validation, D.B., M.D.F. and C.A.L.; formal analysis, D.B. and S.D.G.; investi-
gation, D.B.; resources, D.B.; data curation, D.B.; writing—original draft preparation, Bianchi D.;
writing—review and editing, Bianchi D.; visualization, D.B.; supervision, D.B. and S.D.G.; project

## Page 22

Machines 2023, 11, 352
22 of 23
administration, S.D.G.; funding acquisition, S.D.G. All authors have read and agreed to the published
version of the manuscript.
Funding: This work is partially supported by the European Project ECSEL–JU RIA–2018 “Comp4Drones”
under grant agreement No. 826610, and by MAECI Project 2018–2020 “Coordination of autonomous
unmanned vehicles for highly complex performances” PGR01083.
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Data sharing not applicable.
Acknowledgments: The authors are grateful to the editor and anonymous reviewers for their con-
structive comments and suggestions, which have improved this paper.
Conﬂicts of Interest: The authors declare no conﬂict of interest.
References
1.
Lippitt, C.D.; Zhang, S. The impact of small unmanned airborne platforms on passive optical remote sensing: A conceptual
perspective. Int. J. Remote Sens. 2018, 39, 4852–4868. [CrossRef]
2.
Stolaroff, J.K.; Samaras, C.; O’Neill, E.R.; Lubers, A.; Mitchell, A.S.; Ceperley, D. Energy use and life cycle greenhouse gas
emissions of drones for commercial package delivery. Nat. Commun. 2018, 9, 409–422. [CrossRef] [PubMed]
3.
ECSEL JU Project “COMP4DRONES”, 2019–2022. Available online: https://www.comp4drones.eu/ (accessed on 3 January
2023).
4.
Ding, L.;Wang, Z. A Robust Control for an Aerial Robot Quadrotor under Wind Gusts. J. Robot. Hindawi 2018, 2018, 5607362.
[CrossRef]
5.
Ha, L.N.N.T.; Hong, S.K. Robust Dynamic Sliding Mode Control-Based PID–Super Twisting Algorithm and Disturbance Observer
for Second-Order Nonlinear Systems: Application to UAVs. Electronics 2019, 8, 760. [CrossRef]
6.
Verberne, J.; Moncayo, H. Robust Control Architecture for Wind Rejection in Quadrotors. In Proceedings of the International
Conference on Unmanned Aircraft Systems (ICUAS), Atlanta, GA, USA, 11–14 June 2019; pp. 152–161.
7.
Sankaranarayanan, V.N.; Satpute, S.; Nikolakopoulos, G. Adaptive Robust Control for Quadrotors with Unknown Time-Varying
Delays and Uncertainties in Dynamics. Drones 2022, 6, 220. [CrossRef]
8.
Wan, K.; Gao, X.; Hu, Z.; Wu, G. Robust Motion Control for UAV in Dynamic Uncertain Environments Using Deep Reinforcement
Learning. Remote Sens. 2020, 12, 640. [CrossRef]
9.
Lúa, C.A.; García, C.C.V.; Di Gennaro, S.; Castillo-Toledo, B.; Morales, M.E.S. Real-Time Hovering Control of Unmanned Aerial
Vehicles. J. Math. Probl. Eng. Hindawi 2020, 2020, 2314356.
10.
Guillén-Bonilla, J.T.; García, C.C.V.; Di Gennaro, S.; Morales, M.E.S.; Lúa, C.A. Vision-Based Nonlinear Control of Quadrotors
Using the Photogrammetric Technique. Math. Probl. Eng. 2020, 2020, 5146291. [CrossRef]
11.
Hughes, P.C. Spacecraft Attitude Dynamics; Dover Publications, Inc.: Mineola, NY, USA, 1986.
12.
Nagaty, A.; Saeedi, S.; Thibault, C.; Seto, M.; Li, H. Control and Navigation Framework for Quadrotor Helicopters. J. Intell. Robot.
Syst. 2013, 70, 1–12. [CrossRef]
13.
Shtessel, Y.; Edwards, C.; Fridman, L.; Levant, A. Sliding Mode Control and Observation; Birkhauser: New York, NY, USA, 2014.
14.
Fridman, L.; Shtessel, Y.; Edwards, C.; Yan, X.-G. Higher-order sliding-mode observer for state estimation and input reconstruction
in nonlinear systems. Int. J. Robust Nonlinear Control. 2008, 18, 399–412. [CrossRef]
15.
Cappuzzo, F.; Dezobry, V.; Bianchi, D.; Di Gennaro, S. A Novel Co-simulation framework for Veriﬁcation and Validation of GNC
Algorithms for Autonomous UAV. In Proceedings of the 78th Vertical Flight Society Annual Forum and Technology Display,
FORUM 2022, Fort Worth, TX, USA, 10–12 May 2022.
16.
Nguyen, D.H.; Liu, Y.; Mori, K. Experimental Study for Aerodynamic Performance of Quadrotor Helicopter. Trans. Jpn. Soc.
Aeronaut. Space Sci. 2018, 61, 29–39. [CrossRef]
17.
Six, D.; Briot, S.; Erskine, J.; Chriette, A. Identiﬁcation of the Propeller Coefﬁcients and Dynamic Parameters of a Hovering
Quadrotor From Flight Data. IEEE Robot. Autom. Lett. 2020, 5, 1063–1070. [CrossRef]
18.
Wang, B.H.; Wang, D.B.; Ali, Z.A.; Ting, B.T.; Wang, H. An overview of various kinds of wind effects on unmanned aerial vehicle.
Meas. Control. 2019, 52, 731–739. [CrossRef]
19.
Xiao, Y.; Jin, C. The Flight Principle in the Atmospheric Disturbance; National Defense Industry Press: Beijing, China, 1993.
20.
Beal, T.R. Digital simulation of atmospheric turbulence for Dryden and von Karman models. J. Guid. Control. Dyn. 1993, 16,
132–138. [CrossRef]
21.
Venkataramanan, S.; Dogan, A.; Blake, W. Vortex effect modelling in aircraft formation ﬂight. In Proceedings of the AIAA
Atmospheric Flight Mechanics Conference and Exhibit, Austin, TX, USA, 11–14 August 2003.
22.
Hakim, T.M.I.; Ariﬁanto, O. Implementation of Dryden Continuous Turbulence Model into Simulink for LSA-02 Flight Test
Simulation. Iop Conf. Ser. J. Phys. Conf. Ser. 2018, 1005, 012017. [CrossRef]

## Page 23

Machines 2023, 11, 352
23 of 23
23.
Bianchi, D.; Borri, A.; Di Gennaro, S.; Preziuso, M. UAV trajectory control with rule-based minimum-energy reference generation.
Proc. Eur. Control. Conf. (ECC) 2022, 1497–1502. [CrossRef]
24.
Mogensen, K.N. Motor-Control considerations for electronic speed control in drones. Analog. Appl. J. Tex. Instrum. 2016. Available
online: https://www.ti.com/lit/an/slyt692/slyt692.pdf (accessed on 2 January 2023).
25.
Yang, G.; Yao, J.; Dong, Z.; Neuroadaptive learning algorithm for constrained nonlinear systems with disturbance rejection. Int. J.
Robust Nonlinear Control. 2022, 32, 6127–6147. [CrossRef]
26.
Yang, G. Asymptotic tracking with novel integral robust schemes for mismatched uncertain nonlinear systems. Int. J. Robust
Nonlinear Control. 2022, 33, 1988–2002. [CrossRef]
27.
Di Ferdinando, M.; Pepe, P.; Di Gennaro, S. A new approach to the design of sampled-data dynamic output feedback stabilizers.
IEEE Trans. Autom. Control. 2022, 67, 1038–1045. [CrossRef]
28.
Di Ferdinando, M.; Pepe, P.; Di Gennaro, S. On Semi–Global Exponential Stability Under Sampling for Locally Lipschitz
Time–Delay Systems. IEEE Trans. Autom. Control. 2022, 99, 120–131. [CrossRef]
29.
Di Ferdinando, M.; Bianchi, D.; Di Gennaro, S.; Pepe, P. On the Robust Quantized Sampled–Data Leaderless Consensus Tracking
of Nonlinear Multi–Agent Systems. In Proceedings of the 60th IEEE Conference on Decision and Control (CDC), Austin, TX,
USA, 13–15 December 2021; pp. 3263–3268.
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.
