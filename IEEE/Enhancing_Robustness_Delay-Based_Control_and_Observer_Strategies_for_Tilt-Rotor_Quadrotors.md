# Enhancing_Robustness_Delay-Based_Control_and_Observer_Strategies_for_Tilt-Rotor_Quadrotors.pdf

## Page 1

Enhancing Robustness: Delay-Based Control and Observer Strategies
for Tilt-Rotor Quadrotors*
David Nieto-Hern´andez1, Juli´an-Alejandro Hern´andez-Gallardo1,2,
Liliana F´elix1 and C´esar-Fernando M´endez-Barrios1
Abstract— This paper presents a new control scheme, named
the Proportional Delayed Integral (PδI) controller, for achieving
tracking tasks on a tilt-rotor quadrotor. The proposed approach
integrates a nonlinear disturbance observer, which effectively
mitigates adverse effects stemming from parametric inaccura-
cies or unknown forces. By enhancing the traditional quadrotor
with a tilting mechanism, the operational range is extended,
enabling interaction with the surroundings via a robotic arm
with one degree of freedom. To ensure precision and adaptabil-
ity during operations, a comprehensive mathematical model
has been meticulously developed, accurately reflecting the
unique capabilities of the drone. The synergistic combination
of the PδI controller with the nonlinear disturbance observer
empowers the tilt-rotor quadrotor to tackle complex tasks
with efficiency and reliability. Through rigorous numerical
simulations demonstrating the effectiveness of this design, this
study lays the foundation for a new era of highly functional
and versatile drones, poised to revolutionize various industries
and applications.
I. INTRODUCTION
Unmanned aerial vehicles (UAVs) have come a long way,
with quadrotors emerging as a leading design. These versatile
and maneuverable aircraft, characterized by their four rotors
in a square configuration, have become the most popular
UAVs due to their simple design and ease of control. Each
rotor generates lift and thrust, allowing quadrotors to hover,
move in all directions, and perform vertical takeoff and
landing (VTOL) without a runway. This unique configuration
grants them exceptional agility, making them ideal for a vast
array of tasks and environments.
One promising application for quadrotors is urban air
mobility (UAM) [1] and cargo transportation. As cities
grapple with traffic congestion and pollution, flying taxis
offer a futuristic solution. Quadrotors, with their VTOL capa-
bilities and compact size, could navigate densely populated
areas, providing on-demand transportation and potentially
alleviating traffic woes and environmental concerns.
Furthermore, quadrotors excel at carrying payloads, rang-
ing from small packages to medical supplies. Their ability to
access remote locations makes them invaluable for delivering
essential goods during natural disasters or emergencies [2].
*The work of Nieto-Hern´andez and Hern´andez-Gallardo was financially
supported by CONAHCYT-Mexico.
1Universidad
Aut´onoma
de
San
Luis
Potos´ı
(UASLP),
Facultad
de
Ingenier´ıa,
Dr.
Manuel
Nava
No.
8,
Zona
Universitaria,
San
Luis
Potos´ı,
S.L.P.,
M´exico.
dnieto1591@gmail.com
lfelixa@uaslp.mx fernando.barrios@uaslp.mx
2Tecnol´ogico
Salesiano
Carlos
G´omez,
Jos´e
Mar´ıa
Venegas
No.
5,
Col.
Virreyes,
C.P.
78240,
San
Luis
Potos´ı,
S.L.P.,
M´exico.
julian @ieee.org
Advancements in payload capacity and flight range hold
the potential to revolutionize logistics and supply chain
management [3].
The impact of quadrotors extends beyond transportation.
In agriculture [4], they are used for crop monitoring, spraying
pesticides, and precision agriculture, improving yields and
reducing resource waste. Construction and infrastructure
benefit from their ability to survey sites, monitor progress,
and inspect structures [5]. Filmmaking and entertainment
leverage quadrotors to capture breathtaking aerial footage,
enhancing storytelling. Search and rescue operations, surveil-
lance and security, environmental monitoring, and scientific
research all utilize quadrotors due to their versatility and ma-
neuverability. They offer valuable tools in situations where
traditional methods are impractical or inaccessible.
As quadrotors become more sophisticated, advanced con-
trol approaches are essential for stable and precise flight,
especially in complex environments. Nonlinear control tech-
niques [6], such as model predictive control (MPC) [7]
and sliding mode control (SMC) [8], offer robustness and
adaptability to varying conditions and disturbances.
Delay-based controllers [9]–[15] specifically address chal-
lenges associated with communication delays and sensor
latency in UAV systems [16]. By incorporating predictive
algorithms and feedback mechanisms, they enhance respon-
siveness and reliability, enabling effective operation in dy-
namic environments.
Despite their potential, several challenges remain before
quadrotors become mainstream: regulatory hurdles, airspace
integration, safety concerns, and public acceptance. Col-
laboration between governments, industry stakeholders, and
developers is crucial for safe and efficient operation in urban
airspaces.
Technical challenges such as limited flight endurance,
payload capacity, and noise emissions also pose significant
barriers. Advancements in battery technology, propulsion
systems, and autonomous navigation algorithms are nec-
essary to overcome these limitations and unlock the full
potential of quadrotors in future mobility solutions.
Observing and mitigating disturbances are essential as-
pects of quadrotor control systems, particularly in dynamic
and uncertain environments. Disturbance observers [17] and
adaptive control strategies [18] enable quadrotors to detect
and counteract external factors like wind gusts, turbulence,
or payload variations, ensuring stable flight performance.
This paper enhances quadrotor control by combining a
PδI controller with disturbance observation techniques, im-
2024 10th International Conference on Control, Decision and Information Technologies 
CoDIT 2024 | Valletta, Malta / July 01-04, 2024
Technically co-sponsored by IEEE & IFAC
979-8-3503-7397-4/24/$31.00 ©2024 IEEE 
- 2790 -
2024 10th International Conference on Control, Decision and Information Technologies (CoDIT) | 979-8-3503-7397-4/24/$31.00 ©2024 IEEE | DOI: 10.1109/CoDIT62066.2024.10708440
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:37:14 UTC from IEEE Xplore.  Restrictions apply.

## Page 2

proving both tracking accuracy and system resilience against
perturbations. Unlike prior studies that separately focused
on PID controllers and Linear Quadratic Regulators, this
integrated approach offers a more robust solution.
II. MATHEMATICAL MODEL
In this work, we adopt a non-holonomic flight approach
to streamline the navigation task of an interactive tilt-rotor
quadcopter. Our primary goal is to achieve smooth and
precise movements, particularly to facilitate the manipulation
of its one-degree-of-freedom robotic arm. We focus on a
2 −D analysis within the h −z axis framework, as depicted
in Figure 1, emphasizing altitude and heading movements.
Consequently, our paper addresses the tracking task within
the Q−plane, considering the non-holonomic constraints
governing motion along this plane.
A. Generalized coordinates and control inputs
Generalized coordinates are a minimal set of parameters
used to describe the kinematics of a tilt-rotor quadcopter
during tracking tasks in the Q−plane. Let us define the
generalized coordinates as q :=
h
z
θ
γT , where h
and z represent lateral and vertical movements, respectively,
and θ and γ, denote the tilt of the aircraft and the motion of
the robotic arm, respectively.
For the fully actuated tilt-rotor quadcopter, the control
inputs are u :=
uh
uz
uθ
uγ
T , influencing the quad-
copter’s flight. These inputs relate to the thrust of each rotor
as follows:


uh
uz
uθ
uγ

=


T sin (θ + β)
T cos (θ + β)
(T1 −T2 + T3 −T4)ℓr cos (θ + β)
fplp

,
where β is the rotor tilt angle, ℓr is the distance from the
center of gravity to each rotor, fp is the force from the robotic
arm, lp is the distance from the center of gravity to the arm’s
force application point, and T is the total thrust from all
rotors (T = T1 + T2 + T3 + T4).
B. Dynamical model via Euler-Lagrange approach
The tilting-quadrotor configuration, as illustrated in Fig.
1, reveals two interconnected subsystems. The following
analysis considers the additive property of the Lagrangian
to obtain a dynamical model examining both subsystems
separately. Firstly, the analysis focuses on the kinetic and
potential energy of the quadrotor’s subsystem and then shifts
to the robotic arm system, conceptualized as a pendulum.
This analysis leads to the Lagrangian:
L = 1
2(mr+mp)

˙h2+ ˙z2
+mplp( ˙θ+ ˙γ)

cos(θ+γ)˙h+sin(θ+γ) ˙z

+ 1
2Ir ˙θ2 + 1
2Ip( ˙θ+˙γ)2−(mr+mp)gz + mpglp cos(θ),
(1)
where mr, mp are the masses of the quadrotor and pendulum,
θ is the rotation of the drone, γ angular position of the
pendulum, Ir, Ip denote the moments of inertia of the
quadrotor and pendulum, lp represents the length of the
robotic arm and g denotes the acceleration of gravity. For
further details, please review [19].
e2
h
z
e3
T2
θ
γ
T1
β
Fig. 1.
Forces exerted on tilt-rotor UAV in the Q−plane.
To obtain the dynamic motion of the system, we utilize
the Euler-Lagrange (E-L) approach, resulting in:
M(q)¨q + C( ˙q, q) ˙q + g(q) = u,
(2)
where the matrices M(q), C( ˙q, q) ∈R4×4 and g(q) ∈R4
are given as follows:
M(q) :=


mr + mp
0
ma
ma
0
mr + mp
mb
mb
ma
mb
Ir + Ip
Ip
ma
mb
Ip
Ip


C( ˙q, q) :=


0
0
cc
cc
0
0
cd
cd
0
0
0
0
0
0
0
0

, g(q):=


0
(mr + mp)g
mplpg sin(θ)
mplpg sin(θ)

,
whith ma := mplp cos(θ+γ), mb := mplp sin(θ+γ), cc :=
−mplp sin (θ + γ) ( ˙θ + ˙γ), cd := mplp cos (θ + γ) ( ˙θ + ˙γ).
III. CONTROL STRATEGY
This paper addresses trajectory tracking challenges in tilt-
rotor quadrotors. We propose a delay-based control approach
that ensures precise movement and minimal deviations.
Delay-based controllers offer the advantage of including an
additional degree-of-freedom parameter that can be adjusted
to improve performance. Building on prior work [20], we
reformulate the quadrotor dynamics (2) using a change of
variables. This new system, denoted by eq := q −qd where
qd is a smooth reference.
By exploiting this transformed system and applying prin-
ciples of nonlinear control, we develop a control law that
guarantees both stability and precise trajectory tracking. The
control input for this law is expressed as:
u(˙q,q)=M(q)[¨qd−Kp eq−Kieqτ]+C( ˙q, q) ˙q+g(q),
(4)
where Kp, Ki ∈R4×4 are the proportional and integral gains
of the PδI controller [15] and eqτ :=
Z t
0
eq(v−τ)dv. Firstly, to
tune the PδI controller, it must be ensured that the system is
stable in the closed loop, so the following result is presented.
CoDIT 2024 | Valletta, Malta / July 01-04, 2024
Technical Co-Sponsors: IEEE CSS, IEEE SMC, IEEE RAS & IFAC.
- 2791 -
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:37:14 UTC from IEEE Xplore.  Restrictions apply.

## Page 3

Proposition 1: Let qd be a suitably smooth desired tra-
jectory and τ a fixed delay. Consider the system (2) in
closed-loop with control (4), where Kp and Ki are real
diagonal matrices defined as Kp := diag{kp1, · · · , kp4},
Ki := diag{ki1, · · · , ki4}. For j ∈{1, . . . , 4} and ℓ∈N,
assume that the gains kpj and kij are chosen by satisfying
the following inequalities:
τ > 0,
(5)
(2ℓ−1)π
2τ
2
< kpj <
(2ℓ+ 1)π
2τ
2
,
(6)
0 < kij < kpj
 π
2τ

−
 π
2τ
3
.
(7)
Finally, the closed-loop system is asymptotically stable.
Remark 1: According to condition (5) stated in Proposi-
tion 1, it is evident that the system requires a positive delay,
meaning that it cannot be stabilized using a classical PI
controller, i.e., the polynomial ∆(s; kp, ki) := s3+kps+ki is
not stabilizable, since it does not satisfy the Stodola condition
[21].
On the other hand, the controller can also be tuned using
the D-Decomposition methodology which generates stability
maps in terms of the design parameters (kp, ki, τ).
Proposition 2: Let h > 0 be a fixed value, the set of all
stability crossing curves is composed by the following set of
lines:
ki := 0,
kp ∈R.
(8)
ki := (−1)ℓω3
ℓ−kpωℓ

,
kp ∈R.
(9)
where ωℓ= (2ℓ−1)π
2τ
, and ℓ∈N.
Fig. 2 depicts the behavior of the delay-based controller
parameters as τ varies from 0.5s to 1.5s. In particular, we see
that the stability zones collapse as the delay rises, resulting in
a smaller range of values from which to choose the controller
gains. As a result, the most crucial element to balance is the
delay, as a short delay maximizes the value of the benefits.
Fig. 2.
Stability regions (kp, ki, τ) where ℓ= 1, 2, . . . , 6.
In this sense, one of the main tools to design a controller
that guarantees such a convergence relation is the notion of
σ−stability. To state such a notion, let be σ ∈R+. Then, the
stability-problem can be described as the task of determining
the gains of the controller kj := (kpj, kij) for which the real
part of the rightmost roots of the characteristic function for
the closed-loop system is smaller than −σ.
Proposition 3: Let τ > 0 be a fixed value, σ > 0, the set
of all stability crossing curves is composed by
kp(ω, σ) = 3ω2 −σ2 + 2ω(ω2 + σ2) cos(ωh)
σ sin(ωh) −ω cos(ωh), (10)
ki(ω, σ) = e−hσ
2ω(ω2 + σ2)σ
σ sin(ωh) −ω cos(ωh).
(11)
Sketch of proof: The proof is performed in the same way as
for Proposition 2 with s = −σ + iω.
■
By choosing a delay value, the regions of stability are
delimited by the stability crossover curves shown in Fig.
3, where a range of possible combinations of kpj and kij
values are represented within the yellow zone, guaranteeing
the stability of the system.
Fig. 3.
Stability regions (kp, ki) where 0 < σ < 9 and τ = 0.1.
IV. NONLINEAR DISTURBANCE OBSERVER (NDO)
This work integrates an aerial robot with a robotic arm
to interact with its environment. The robotic arm’s payload
manipulation generates disturbances due to parametric inac-
curacies and external factors. To consider the disturbances,
the dynamical model is expanded to include uncertainties,
adjusting the equation to:
M(q)¨q + C( ˙q, q) ˙q + g(q) = u + d,
(12)
where d represents disturbances from unknown parameters
and external forces. The observation error, defined as the
difference between the measured and observed disturbances,
is:
eo := d −bd.
(13)
CoDIT 2024 | Valletta, Malta / July 01-04, 2024
Technical Co-Sponsors: IEEE CSS, IEEE SMC, IEEE RAS & IFAC.
- 2792 -
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:37:14 UTC from IEEE Xplore.  Restrictions apply.

## Page 4

Without prior knowledge of d, it is commonly assumed that:
˙d ≡0.
(14)
This assumption implies that disturbances change slowly
compared to the observer’s adaptation ability, allowing the
observer to keep up with variations. Assuming that (14)
holds, we need error dynamics that ensure the observation
error eventually goes to zero. Similar to classical nonlinear
observers, we propose the following error dynamics:
˙eo = −L(q, ˙q)eo.
(15)
It is important to consider that L(q, ˙q) matrix must be
positive definite and designed according to the E-L system,
and Ko is a diagonal gain matrix. With well-designed error
dynamics, a controller can effectively reduce disturbances.
We will use a nonlinear disturbance observer designed for
manipulator robots [22], adapted for rotorcraft disturbances.
Consider the variable change:
zo := bd −p(q, ˙q),
(16)
where p(q, ˙q) satisfies:
˙p(q, ˙q) = L(q, ˙q)M(q)¨q.
(17)
By analyzing the combined dynamics of (16) with (17) and
the observer dynamics (15) we can ensure the asymptotic
stability of the nonlinear disturbance observer.
Remark 2: Equation (17) offers a key advantage: it elim-
inates the need to directly measure the system’s acceleration
¨q. This translates to fewer sensors required for disturbance
estimation, simplifying the overall system design.
Thus, the NDO will be considered as:
bd = zo + p(q, ˙q),
(18)
where zo ∈R4 is the change of variable with time derivative
given by
˙zo=−L(q, ˙q)(zo+p(q, ˙q)−C(q, ˙q) ˙q−g(q)+u).
(19)
Finally yet importantly, p(q, ˙q) ∈R4 is the designed
function vector that ensures the positive definition of L(q, ˙q).
Considering this designed function vector as
p(q, ˙q) = K−1
o
˙h ˙z ˙θ ˙γ
T,
(20)
We can define Ko as a diagonal matrix with elements on
the diagonal denoted by ko1, ko2, ko3 and ko4. To achieve
good observer performance, we need to carefully select these
gains satisfying the following conditions:
(i) koj ∈R+, j ∈{1, . . . , 4},
(ii) max{ko1, ko2} < ko3 + ko4 <
2
Ωφmplp
,
where Ωφ is denoted as a positive constant that fulfills the
following condition,
 ˙θ(t) + ˙γ(t)
 ≤Ωφ,
∀t ∈R.
Then, the observer (18) converges asymptotically to the
disturbance d.
V. NUMERICAL EXAMPLES
This section explores how a delay-based controller and
a nonlinear disturbance observer can improve the flight
performance of a tilt-rotor quadcopter. We’ll first introduce
the design parameters of the aircraft, controller, and observer
used in this work. These specific aircraft parameters derived
through software are provided in Table I.
TABLE I
AIRCRAFT, CONTROL AND NDO PARAMETERS.
Parameter
Value
Parameter
Value
mr
0.5 kg
mp
0.125 kg
lp
0.35 m
g
9.81 m
s2
Ir
0.177 kg·m2
Ip
0.153 kg·m2
Controller gain
Value
Controller gain
Value ∗
Kp
750
Ki
5 × 103
τ
0.1 s
Observer gain
Value
Observer gain
Value
ko1
1
ko2
1
ko3
1.5
ko4
2.5
To demonstrate the effectiveness of our proposed control
approach, we conducted numerical simulations using a tilt-
rotor quadcopter model built with commonly available, off-
the-shelf components.
This scenario involves a circular path centered 6 m
above the ground with a radius of 4 m. This relatively
simple trajectory allows us to assess the controller’s basic
performance. The trajectory is described by the following
parametric equation:
qd :=


h(t)
z(t)
θ(t)
γ(t)

=


4 sin( π
2 t) + 10
4 cos( π
2 t) + 10
π
6
π
6 sin( π
2 t)


We evaluated the time-delay-based controller with the non-
linear disturbance observer. Fig. 4 illustrate the resulting
smooth and stable trajectory tracking, enabling precise con-
trol even in complex maneuvers. This improved performance
suggests the effectiveness of the delay-based approach paired
with the NDO in mitigating disturbances and achieving
accurate flight paths. A closer look reveals key characteristics
that help us understand specific aspects such as tracking
accuracy and control efforts in all states. This will provide
a nuanced understanding of the controller’s strengths and
weaknesses.
To perform a detailed analysis, let us focus on the states of
the trajectory (Fig. 5). All measured states converge well to
the desired trajectory. However, the rotational states exhibit
minimal deviations caused by perturbations.
The time-delay controller exhibits a slight overdamping
effect, particularly at the start of the path and during dis-
turbances. However, it’s important to note that these errors
are relatively small, remaining below 2 cm and 0.5 rad,
and converge to zero over time. This demonstrates the
controller’s effectiveness in reducing errors and achieving
CoDIT 2024 | Valletta, Malta / July 01-04, 2024
Technical Co-Sponsors: IEEE CSS, IEEE SMC, IEEE RAS & IFAC.
- 2793 -
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:37:14 UTC from IEEE Xplore.  Restrictions apply.

## Page 5

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
5
6
7
8
9
10
Desired trajectory
Delayed-based controller
Fig. 4.
Tracking of the aircraft’s circular trajectory.
0
5
10
15
20
25
30
35
40
45
50
0
5
10
Delayed-based controller
Desired state
0
5
10
15
20
25
30
35
40
45
50
0
5
10
Delayed-based controller
Desired state
0
5
10
15
20
25
30
35
40
45
50
0
0.5
1
Delayed-based controller
Desired state
0
5
10
15
20
25
30
35
40
45
50
-0.5
0
0.5
Delayed-based controller
Desired state
Fig. 5.
Aircraft states when following a circular trajectory.
accurate trajectory tracking. Analyzing the rotor thrust (Fig.
6) is important to ensure it remains within the actuators’
physical limits and prevents damage. The control strategy
achieves this by generating control inputs that require a
satisfactory level of effort within a short timeframe. This
efficient use of control keeps the rotor thrust well within
safe operating zones, enabling smooth and stable flight
throughout the trajectory tracking. To simulate lifting and
dropping a package, we introduced a square-wave distur-
bance representing the external force. The following Fig. 7
0
5
10
15
20
25
30
35
40
45
50
-10
0
10
20
Delayed-based controller
0
5
10
15
20
25
30
35
40
45
50
-5
0
5
10
15
Delayed-based controller
0
5
10
15
20
25
30
35
40
45
50
-5
0
5
Delayed-based controller
0
5
10
15
20
25
30
35
40
45
50
-10
-5
0
5
10
Delayed-based controller
Fig. 6.
Control inputs of the aircraft when following a circular trajectory.
analyze the resulting disturbances, their observations using
the time-delay controller, and the observer’s performance.
The observer effectively estimates these disturbances, pro-
viding reliable feedback for the control system. However,
it’s important to acknowledge that the NDO’s performance
exhibits limitations during rapid changes in the external load
(cargo appearance/disappearance) and at the trajectory start.
These limitations are likely due to the transient nature of
these events. Despite these limitations, the observer’s overall
performance remains satisfactory and has minimal impact on
the validation of its effectiveness in disturbance estimation.
VI. CONCLUSIONS
This research explores a unique flight configuration for
interactive quadcopters with tilting rotors. We developed
a precise mathematical model using the Euler-Lagrange
method, accurately reflecting the quadcopter’s behavior.
To achieve highly accurate trajectory following and ef-
fective disturbance resistance, we propose a novel PδI con-
troller. This controller offers greater flexibility for fine-tuning
the control system, making it a strong choice for various
quadcopter applications. Additionally, a modified Nonlinear
Disturbance Observer (NDO) is introduced to enhance the
quadcopter’s performance during cargo transportation tasks.
REFERENCES
[1] D. P. Thipphavong, R. Apaza, B. Barmore, V. Battiste, B. Burian,
Q. Dao, M. Feary, S. Go, K. H. Goodrich, J. Homola, et al., “Urban
air mobility airspace integration concepts and considerations,” in 2018
CoDIT 2024 | Valletta, Malta / July 01-04, 2024
Technical Co-Sponsors: IEEE CSS, IEEE SMC, IEEE RAS & IFAC.
- 2794 -
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:37:14 UTC from IEEE Xplore.  Restrictions apply.

## Page 6

0
5
10
15
20
25
30
35
40
45
50
0
2
4
6
Disturbance
Observed disturbance delayed-based controller
0
5
10
15
20
25
30
35
40
45
50
0
2
4
6
Disturbance
Observed disturbance delayed-based controller
0
5
10
15
20
25
30
35
40
45
50
-2
0
2
4
6
Disturbance
Observed disturbance delayed-based controller
0
5
10
15
20
25
30
35
40
45
50
0
2
4
6
Disturbance
Observed disturbance delayed-based controller
Fig. 7.
Applied disturbances to the aircraft when following a circular
trajectory.
Aviation Technology, Integration, and Operations Conference, p. 3676,
2018.
[2] E. Ackerman and M. Koziol, “The blood is here: Zipline’s medical
delivery drones are changing the game in Rwanda,” IEEE Spectrum,
vol. 56, no. 5, pp. 24–31, 2019.
[3] H. Ni, X. Deng, B. Gong, and P. Wang, “Design of regional logistics
system based on unmanned aerial vehicle,” in 2018 IEEE 7th Data
Driven Control and Learning Systems Conference (DDCLS), pp. 1045–
1051, 2018.
[4] T. H. Pham, D. Ichalal, and S. Mammar, “Complete coverage path
planning for pests-ridden in precision agriculture using UAV,” in 2020
IEEE International Conference on Networking, Sensing and Control
(ICNSC), pp. 1–6, 2020.
[5] K. Zhang, P. Chermprayong, F. Xiao, D. Tzoumanikas, B. Dams,
S. Kay, B. B. Kocer, A. Burns, L. Orr, T. Alhinai, and et al., “Aerial
additive manufacturing with multiple autonomous robots,” Nature,
vol. 609, p. 709–717, Sep 2022.
[6] D. Nieto-Hern´andez, M.-A. Lastras-Monta˜no, C.-F. M´endez-Barrios,
J. S. Murgu´ıa-Ibarra, P. Mart´ınez-Rodr´ıguez, and D. Langarica-
C´ordoba, “Controller Based on Combined Tracking Error Applied in
a Tilt-rotor MAV,” in 2022 IEEE International Autumn Meeting on
Power, Electronics and Computing (ROPEC), vol. 6, pp. 1–6, 2022.
[7] K. Benkhoud and S. Bouall`egue, “Model predictive control design
for a convertible quad tilt-wing UAV,” in 2016 4th International
Conference on Control Engineering & Information Technology, pp. 1–
6, 2016.
[8] G. Yu, Y. Chen, Z. Chen, H. Wu, and L. Cheng, “Design of terminal
sliding mode controller for a quadrotor uav with disturbance observer,”
in 2020 39th Chinese Control Conference, pp. 2072–2077, 2020.
[9] D. Torres-Garc´ıa, J.-A. Hern´andez-Gallardo, C.-F. M´endez-Barrios,
and S.-I. Niculescu, “Exploring Delay-Based Controllers. A Com-
parative Study for Stabilizing Angular Positioning,” in Advances in
Automation and Robotics Research (M. N. Cardona, J. Baca, C. Garcia,
I. G. Carrera, and C. Martinez, eds.), pp. 123–136, Cham: Springer
Nature Switzerland, 2024.
[10] C.-F. M´endez-Barrios, S.-I. Niculescu, A. Mart´ınez-Gonz´alez, and
A. Ram´ırez, “Characterizing some improperly posed problems in
proportional-derivative control,” International Journal of Robust and
Nonlinear Control, vol. 32, no. 18, pp. 9452–9474, 2022.
[11] C.-F. M´endez-Barrios, J.-D. Torres-Garc´ıa, and S.-I. Niculescu,
“Delay-difference approximations of pd-controllers. improperly-posed
systems in multiple delays case,” International Journal of Robust and
Nonlinear Control, vol. n/a, no. n/a.
[12] J. U. Alvarez-Mu˜noz, J. J. Castillo-Zamora, J. Escareno, I. Boussaada,
C.-F. M´endez-Barrios, and O. Labbani-Igbida, “Time-delay control of
a multi-rotor VTOL multi-agent system towards transport operations,”
in 2019 International Conference on Unmanned Aircraft Systems
(ICUAS), pp. 276–283, 2019.
[13] C.-F. M´endez-Barrios, S.-I. Niculescu, J. Chen, and M. Maya-M´endez,
“Output feedback stabilisation of single-input single-output linear sys-
tems with i/o network-induced delays. an eigenvalue-based approach,”
International Journal of Control, vol. 87, no. 2, pp. 346–362, 2014.
[14] R. Villafuerte-Segura, “Delayed controllers for time-delay systems,”
Communications in Nonlinear Science and Numerical Simulation,
vol. 117, p. 106934, 2023.
[15] J.-A. Hern´andez-Gallardo, A.-J. Guel-Cortez, E. J. Gonzalez-Galvan,
and C.-F. M´endez-Barrios, “Designing Proportional Delayed Integral
Control for Fast Regulation in Second-Order Systems: A Geometric
Approach,” in 2023 9th International Conference on Control, Decision
and Information Technologies (CoDIT), 2023.
[16] J. Zhang, X. Zhu, and Z. Zhou, “Design of time delayed control
systems in uav using model based predictive algorithm,” in 2010 2nd
International Asia Conference on Informatics in Control, Automation
and Robotics (CAR 2010), vol. 1, pp. 269–272, 2010.
[17] R. Jiao, W. Chou, and Y. Rong, “Disturbance observer-based back-
stepping control for quadrotor uav manipulator attitude system,” in
2020 Chinese Automation Congress (CAC), pp. 2523–2526, 2020.
[18] W. Cheng and Z. Hou, “Attitude control of quadrotor UAV based on
adaptive sliding mode control,” in 2022 34th Chinese Control and
Decision Conference (CCDC), pp. 5878–5884, 2022.
[19] D. Nieto-Hern´andez, J. Escareno, C.-F. M´endez-Barrios, I. Boussaada,
and D. Langarica-C´ordoba, “Modeling and control of an interactive
tilt-rotor MAV,” in 2017 Workshop on Research, Education and
Development of Unmanned Aerial Systems, pp. 270–275, 2017.
[20] D.
Nieto-Hern´andez,
J.
Escareno,
C.-F.
M´endez-Barrios,
S.-I.
Niculescu, I. Boussaada, E. Gonz´alez-Galv´an, and J. Alvarez-Mu˜noz,
“Modeling and control of an interactive tilt-rotor mav for in-contact
cracks-sensing operations,” IFAC-PapersOnLine, vol. 51, no. 22,
pp. 318–323, 2018.
[21] S. P. Bhattacharyya and L. H. Keel, “Robust control: the parametric
approach,” in Advances in control education 1994, pp. 49–52, Elsevier,
1995.
[22] W. Chen, D. J. Ballance, P. J. Gawthrop, and J. O’Reilly, “A nonlinear
disturbance observer for robotic manipulators,” IEEE Transactions on
Industrial Electronics, vol. 47, no. 4, pp. 932–938, 2000.
CoDIT 2024 | Valletta, Malta / July 01-04, 2024
Technical Co-Sponsors: IEEE CSS, IEEE SMC, IEEE RAS & IFAC.
- 2795 -
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:37:14 UTC from IEEE Xplore.  Restrictions apply.
