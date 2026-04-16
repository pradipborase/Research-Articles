# Fully_Distributed_Low-Complexity_UAV_Formation_Control_With_Fixed-Time_Full-State_Error_Performance.pdf

## Page 1

Received 21 February 2025, accepted 26 March 2025, date of publication 4 April 2025, date of current version 25 April 2025.
Digital Object Identifier 10.1109/ACCESS.2025.3557921
Fully Distributed Low-Complexity UAV Formation
Control With Fixed-Time Full-State
Error Performance
PENGFEI YU
AND QING LI
School of Automation, Beijing Information Science and Technology University, Beijing 100192, China
Ministry of Education Key Laboratory of Modern Measurement and Control Technology, Beijing 100101, China
Corresponding author: Qing Li (liqing@bistu.edu.cn)
This work was supported by the National Key Research and Development Program of China and Beijing Scholars Program under Grant
2022YFF0607403.
ABSTRACT
This paper presents a fully distributed, low-complexity UAV formation controller design
with fixed-time full-state error performance, which is able to address the difficulties in obtaining global
information and suppressing external disturbances without observer or adaptive law in existing solutions.
The position of neighboring UAVs is the only information to be exchanged, and desired state observer is
not required, thereby reducing communication costs, which is well-suited to larger-scale UAV formation
systems. The proposed control scheme has the capability to handle external disturbances without observer
or adaptive law, simplifying the controller’s design and implementation process, reducing computational
burden. Moreover, by imposing fixed-time performance constraints on tracking error and virtual error, fixed-
time formation tracking error and virtual velocity tracking error can be achieved, which also improves the
response speed and accuracy of UAV formation, making it more capable of meeting the time requirements
of actual tasks and adapting to dynamically changing environments. Additionally, all closed-loop signals
are rigorously proven to be semi-globally ultimately uniformly bounded. Finally, numerical simulation is
conducted to verify the effectiveness of proposed control scheme.
INDEX TERMS
Fully distributed controller, UAV formation, low complexity, fixed-time preset
performance.
I. INTRODUCTION
In recent years, drone swarms have demonstrated broad
application prospects in various fields due to their flexibility,
low cost, and environmental adaptability [1], [2], [3],
[4]. However, facing dynamic and complex environments
and task requirements, the key issue that remains to be
researched is the formation of a swarm that can handle
complex dynamic environments, and ensure efficient and
stable communication [5], [6], [7].
Due to the nonlinear dynamics, insufficient driving force,
strong coupling, and sensitivity to interference of multi-
drone systems, the control of drone formations becomes
highly challenging under uncertain flight conditions. Early
control methods for drone formations based on graph
theory and leader-follower models can intuitively model
The associate editor coordinating the review of this manuscript and
approving it for publication was Xiwang Dong.
interactions between drones, flexibly structure topologies,
and analyze systems using graph theory tools, offering
flexibility and effectiveness [8], [9], [10]. Fuzzy control and
reinforcement learning algorithms provide powerful control
solutions for drone formations, adapting to nonlinear and
uncertain environments, capable of self-learning and real-
time decision-making, and functioning effectively without
precise models [11], [12], [13], [14], [15], [16]. Recursive
optimization methods, with their real-time dynamic adjust-
ments and efficient computations; event-driven control, with
its reduced computational burden and efficient response;
and port-Hamiltonian system methods, with their advantages
in energy management and stability design, collectively
enhance the performance, robustness, and adaptability of
drone formation systems [17], [18], [19].
However, the aforementioned control methods struggle
with dynamic and complex environments. Most distributed
results face difficulties in obtaining global information when
68224
 2025 The Authors. This work is licensed under a Creative Commons Attribution 4.0 License.
For more information, see https://creativecommons.org/licenses/by/4.0/
VOLUME 13, 2025

## Page 2

P. Yu, Q. Li: Fully Distributed Low-Complexity UAV Formation Control
the network scale is large and depend heavily on global
information, making the stability of multi-drone formations
an issue [20]. Current research in this area aims to reduce
communication and control update frequency among drones
to achieve tracking synchronization and simplify design
complexity. For instance, an event-triggered multi-aircraft
formation target tracking control algorithm was proposed to
address the frequent information exchange and control update
issues during multi-drone formations [21]. Another study
explored bandwidth-limited orderly communication in multi-
drone formations, introducing dynamic spectrum interaction
and reinforcement learning algorithms, proposing two drone
formation communication methods: information sharing and
dynamic time slot allocation [22]. A distributed formation
containment protocol based on adjacent information was
designed to achieve the expected formation of the leader’s
state and ensure the followers’ states converge to the convex
hull traversed by the leader while maintaining the leader’s
formation as a convex combination [23]. A novel relay
algorithm using Unscented Kalman Filter and Hybrid Particle
Swarm Optimization (UKF-HPSO) was proposed to optimize
communication throughput in drone mobile relay formations,
considering challenges such as obstacle avoidance, channel
complexity, high drone dynamics, and real-time task require-
ments, effectively optimizing system throughput through
real-time prediction and optimal deployment to address
unique challenges in drone communication in dynamic envi-
ronments [24]. Although these methods effectively reduce
communication burdens, their complexity remains high, and
they cannot effectively handle external disturbances.
Regarding the issue of multiple drones experiencing
nonlinear time-varying disturbances during coordinated for-
mation flight, there is still insufficient research on the
synchronization problem under disturbances [25], [26].
Although some formation control algorithms are specifically
designed for multi-drone systems [10], [27], they can-
not achieve disturbance suppression. External disturbances
reduce system performance and cause instability. Current
anti-disturbance approaches include active and passive distur-
bance rejection. Active disturbance rejection is more suitable
for applications requiring high disturbance response and
significant environmental changes [28], [29], [30], while pas-
sive disturbance rejection suits scenarios with relatively low
disturbance response requirements and minor environmental
changes [31]. To address disturbance rejection, a method
combining a distributed fixed-time sliding mode estimator
and fixed-time disturbance observer with a fixed-time sliding
mode controller was proposed, enabling each drone to
quickly estimate desired position information and generate
disturbance estimates to counteract compound disturbances,
achieving stable tracking of the desired trajectory [32].
Another study proposed a robust control method based
on disturbance observers, utilizing disturbance observers to
estimate unknown external disturbances and combining these
estimates with the controller to enhance system stability
and performance [33]. A finite-time disturbance observer
was proposed to handle unknown external disturbances, and
a non-singular terminal sliding mode control method was
designed based on the observer’s output to avoid singularity
issues faced by traditional terminal sliding mode control [30].
However, these methods cannot perfectly achieve disturbance
rejection. The established control schemes lack robustness
to uncertainties, requiring specific adaptive parameters and
additional observers for neighbor state estimation. Thus,
further research is needed to enhance the control effect
and robustness of quadrotor drone formation systems under
unknown external disturbances.
Besides the above issues, the convergence rate is crucial for
real-time formation systems. Asymptotic formation control
algorithm could only achieve exponential convergence [34],
[35]. Such control methods with infinite settling time are
not suitable for urgent formation task. To obtain rapid
convergence rate, finite-time control scheme is utilized for
formation control [36]. The problem of this method is that the
convergence time is depend on initial states of system. Thus,
fixed-time control method, proposed by [37], is employed
for controller design of formation to ensure settling time
independently on initial condition [38]. However, for systems
with uncertainties and disturbances, finite-time control may
have weak disturbance suppression effects, and if initial
conditions are large enough, the convergence time may
increase significantly [39]. Fixed-time control effectively
addresses this issue, as it requires no online parameter
adjustment [40], [41], providing a constant upper limit
on convergence time and offering more reliable control
performance.
To address the above issues, we propose a new distributed
performance-guaranteed control scheme to enhance system
robustness to uncertainties and offer more relaxed controll
ability conditions compared to the most advanced existing
methods. Additionally, the scheme ensures that the output
tracking error of each agent possesses arbitrarily preas-
signed convergence rates and features lower structural and
computational complexity since it completely avoids virtual
controllers and desired trajectory derivatives. Unlike the latest
methods, it does not use additional observers to estimate
neighbors’ states, and each agent’s control design only
requires its own state and its neighbors’ output information,
ensuring that all internal signals are semi-globally ultimately
uniformly bounded.
In summary, balancing control performance, convergence
speed, communication efficiency, disturbance rejection, and
system complexity is necessary. Therefore, a comprehensive
and efficient controller design are still needed. Based on
previous research, this paper aims to address the above issues
by proposing a fully distributed, low-complexity fixed-time
preset performance controller for drone formations. The main
contributions of this work are summarized as follows:
(1) Compared with [20], [23], only the position infor-
mation of neighbor is required to be transmitted for
communication, solving the difficulty of obtaining
global information without extra state observers.
This has reduced communication costs, suitable for
larger-scale UAV formation systems.
VOLUME 13, 2025
68225

## Page 3

P. Yu, Q. Li: Fully Distributed Low-Complexity UAV Formation Control
(2) Different from previous research [25], [26], [41], [42],
external disturbances have been effectively managed
without the need for adaptive parameters, observers,
or adaptive laws. This approach simplifies the design
and implementation process of the controller, reduces
computational load, and enhances the real-time perfor-
mance and stability of the system.
(3) By imposing fixed-time performance constraints on
the tracking error and virtual error, we have achieved
fixed-time formation tracking error and virtual speed
tracking error. Compared to the control methods
presented in [40], [41], error performance of the for-
mation control system, capability of handling external
disturbances, model errors, and variations of system
parameters are improved.
The discussion will proceed as follows: Section II
describes the problem formulation and prepares the intro-
duction of UAV formation dynamics models and control
objectives. Section III designs the controller and conducts
stability analysis. Section IV presents simulations and
demonstrations of the algorithm. Conclusions are drawn in
Section V.
II. PROBLEM FORMULATION AND PRELIMINARIES
A. DYNAMICS OF THE UAV FORMATION SYSTEM
In this brief, a multi-rotor UAV system consisting of N
four-rotor UAVs and a virtual pilot is studied. The internal
and external loop control architecture is adopted to solve the
formation control problem.
FIGURE 1. Control diagram of multi-UAV systems.
Outer loop: The position and velocity tracking controllers
are designed to make the quadcopters follow the desired
trajectory and maintain the prescribed formation pattern. The
outer loop is designed to achieve predetermined performance,
enable formation tracking, and handle the complexities of
multi-quadrotor dynamics such as nonlinearity, coupling,
underdrive, and external interference. The outer loop con-
troller is responsible for tracking the predetermined motion
trajectory and maintaining the predetermined formation.
Inner loop: This handles the attitude stability control to
stabilize the roll, pitch and yaw angles of the individual
quadrotor. The inner loop controller is responsible for
stabilizing the attitude angle.
The following equation represents the outer loop dynamics
of the quadrotor subjected to external aerodynamic forces and
disturbances:
¨xi = −P1
mi
˙xi + Ai
mi
cos φi sin θi cos ψi + Ai
mi
sin φi sin ψi + d1i
¨yi = −P2
mi
˙yi + Ai
mi
cos φi sin θi sin ψi −Ai
mi
sin φi cos ψi + d2i
¨zi = −P3
mi
˙zi + Ai
mi
cos φi cos θi −g + d3i
(1)
where mi is the mass of the quadrotor, g is the acceleration
of the gravity, and Ai denotes the thrust, Pj, j = 1, 2, 3 is the
aerodynamic damping coefficient, φi, θi and ψi represents the
roll, pitch and yaw angle of the i-th quadrotor, respectively,
d is the external disturbances.
To facilitate controller design of outer loop, we define the
following virtual control input:
uxi = Ai
mi
cos φi sin θi cos ψi + Ai
mi
sin φi sin ψi
uyi = Ai
mi
cos φi sin θi sin ψi −Ai
mi
sin φi cos ψi
uzi = Ai
mi
(cos φi cos θi) −g
(2)
Then, the kinematics and dynamics of i-th follower is given
by
˙xi = vi
˙vi = Civi + ui + di
(3)
B. GRAPH THEORY
In drone formation, graph theory is widely used to model
and analyze the communication and relationships between
drones. We can use a directed graph J = (Q, R) to represent
a drone formation, where Q = {q1, q2, · · · , qn} is the set of
nodes, each node represents a drone, R ⊆Q × Q is the
set of edges, and each edge represents the communication
link between drones. The adjacency matrix Aij is used to
describe the connection relationship of a graph, where Aij =
1 indicates the existence of a communication link between
node j and node i, otherwise Aij
= 0. For a formation
containing n drones, the size of its adjacency matrix A is
n × n.
The Laplace matrix L is another important matrix that
can be obtained from the adjacency matrix A and the degree
matrix D. The degree matrix D is a diagonal matrix, given by
Dii =
n
X
j=1
Aij
(4)
Dii indicates the degree of egress of node i, which is the
number of edges connected to node i.The Laplace matrix is
defined as L = D −A. The eigenvalues and eigenvectors
of L can be used to analyze the connectivity and stability
of the system. Specifically, for a formation composed of n
drones, its state can be expressed as a vector x ∈Rn, where
represents the state of the i-th drone (such as position or
68226
VOLUME 13, 2025

## Page 4

P. Yu, Q. Li: Fully Distributed Low-Complexity UAV Formation Control
velocity). Let
¯J =
 ¯Q, ¯R

be the augmented graph with
¯Q = {q0, q1, · · · , qn} and ¯R ⊆¯Q × ¯Q.
C. CONTROL OBJECTIVE
Let xd be the leader, the formation tracking error of i-th
follower can be described as
ei = xi −xd −δi
(5)
where δi is the relative position between i-th follower and the
virtual leader. In this paper, we devote to design a designing
a low-complexity distributed controller such that
1) The tracking error can be evolved in the prescribed
region, i.e., ∥ei∥
≤
ρ (t), where ρ (t) is a fixed-time
prescribed performance function, satisfying
ρ (t) =



(ρ0 −ρ∞)
T 2
(t −T)2 + ρ∞
t ≤T
ρ∞
t > T
(6)
Especially, every follower can only obtain position infor-
mation of its neighbors and only part of followers can
obtain the leader’s position information, which reduces
communication burden.
2) With the existence of external disturbances, all signals of
closed-loop distributed system are semi-globally ultimately
uniformly bounded. Especially, the adaptive parameters are
not necessary.
3) Both of tracking error and virtual velocity error are
restricted in fixed-time prescribed boundary.
Assumption 1: A spanning tree is contained in the aug-
mented graph ¯J with the leader served as the root.
Assumption 2: Part of followers are able to obtain the
desired trajectory xd and ˙xd is bounded.
Assumption 3: The uncertainty matrices Ci and external
disturbances di are bounded.
III. CONTROLLER DESIGN
A. PRESCRIBED PERFORMANCE TRANSFORMATION
FUNCTION
To alleviate the communication burden, we assume that every
follower can only obtain position information of its neighbors
and only part of followers can obtain the leader’s position
information. Hence, the tracking error ei =

ei,1, ei,2, ei,3
T
defined in (5) cannot be utilized for controller design. To this
end, let δi,k = δi −δk, then auxiliary tracking error
⌢ei is
utilized for controller design, given by
⌢ei =
X
k∈N
ai,k
xi −xk −δi,k

+ bi (xi −xd −δi)
(7)
In view of (5) and (7), it follows that
⌢e(t) = ((L + B) ⊗E3) e(t)
(8)
where e =
 e1, e1, · · · , eN
T ,
⌢e =
h
⌢e1,
⌢e2, · · · ,
⌢eN
i⊤
,
E3 is an identity matrix.
In what follows, we aim to prove that if

⌢ei,j
 < p (t) =
σmin {L + B} ρ (t) /
√
3N, then ∥ei∥< ρ (t) holds, where
σmin {L + B} ≤

N−1
N
 N−1
2
N 2+N−1
[42] is the minimum singular
value of L + B.
Theorem 1: If auxiliary tracking error
⌢ei satisfies

⌢ei,j
 ≤
p (t) = σmin {L + B} ρ (t) /
√
3N, then it holds that ∥ei∥≤
ρ (t).
proof : According to the fact that graph ¯E is connected,
it is able to verify that L + B is positive definite [43]. Note
that ∥X ⊗Y∥= ∥X∥∥Y∥, then, from (8), one can obtain that
∥e(t)∥=

E3 ⊗(L + B)−1
⌢e(t)
≤
(L + B)−1 ∥E3∥

⌢e(t)

≤

⌢e(t)
 /σmin {L + B} =
v
u
u
t
N
X
i=1
⌢e
2
i,j/σmin {L + B}
(9)
Since

⌢ei,j
 < p (t), then one has
∥e(t)∥<
√
3Np (t) /σmin {L + B} = ρ (t)
(10)
By means of definition of e, it follows that ∥ei∥≤∥e∥<
ρ (t). This completes the proof.
B. CONTROLLER DESIGN
In what follows, based on the backstepping method, we are
ready to design a low-complexity distributed controller
such that the prescribed performance constraints ∥ei∥<
ρ (t) and
εi,j
 < ρ (t) can be guaranteed, where ε
=

εT
1 , εT
2 , · · · , εT
N
T is the virtual tracking error, given by ε =
v −α, v =

vT
1 , vT
2 , · · · , vT
N
T , εi =

εi,1, εi,2, εi,3
T , α =

αT
1 , αT
2 , · · · , αT
N
T
is the virtual control law, αi
=

αi,1, αi,2, αi,3
T .
Let s =

sT
1 , sT
2 , · · · , sT
N
T , si =

si,1, si,2, si,3
T , si,j =
tanh−1 ζi,j

, z =

zT
1 , zT
2 , · · · , zT
N
T , zi =

zi,1, zi,2, zi,3
T ,
zi,j
=
tanh−1 ξi,j

, ζ
=

ζ T
1 , ζ T
2 , · · · , ζ T
N
T , ζ i
=

ζi,1, ζi,2, ζi,3
T , ζi,j =
⌢ei,j/p, ξ =

ξT
1 , ξT
2 , · · · , ξT
N
T , ξi =

ξi,1, ξi,2, ξi,3
T , ξi,j = εi,j/ρ (t), ψ
=

ζ ⊤, ξ⊤⊤, and
C = (−1, 1) × · · · × (−1, 1)
|
{z
}
6N
.
The boundedness of system signals is proven by the
following two steps. We first demonstrate the boundedness of
system signals in finite-time interval, ie., ∀t ∈[0, tmax). Sub-
sequently, based on classical Theorem [44], the boundedness
of system signals is established in infinite time interval, i.e.,
∀t ∈[0, tmax). Through these two components, the overall
bounded stability is rigorously proven.
Since p(t), ρ(t) and system (3) are bounded and smooth,
and ψ (0) ∈C is guaranteed by the choice of
⌢ei,j (0) < p (0)
and ∥εi (0)∥< ρ (0), it follows from Theorem 1 in [44] that
there exists a unique and maximal solution ψ(t) ∈C, ∀t ∈
[0, tmax), where tmax < ∞.
As proven in Theorem 1, to achieve ∥ei∥< ρ (t), we only
need to ensure

⌢ei,j
 < p (t). Towards this goal, we start by
VOLUME 13, 2025
68227

## Page 5

P. Yu, Q. Li: Fully Distributed Low-Complexity UAV Formation Control
defining the following candidate Lyapunov function
V1 = 1
2sT s
(11)
Then the time derivative of V1 yields
˙V1 = sT ˙s
= p−1sT G (((L + B) ⊗E3) ˙e(t) −˙pζ)
= p−1sT G
((L + B) ⊗E3)
˙x −˙¯xd

−˙pζ

(12)
where G
=
diag {G1, · · · , GN} and Gi
=
diag

1 −ζ 2
i,j
−1
, i = 1, 2, 3. Then, it can be obtained that
˙V1 = p−1sT G
((L + B) ⊗E3)
ε + α −˙¯xd

−˙pζ

(13)
The virtual control law is designed as below
αi = κ1Gisi
(14)
where κ1 > 0. By substituting (13) into (14), it yields
˙V1 = p−1sT G
((L + B) ⊗E3)
ε −κ1Gs −˙¯xd

−˙pζ

= −p−1κ1sT G ((L + B) ⊗E3) Gs
+ p−1sT G
((L + B) ⊗E3)
ε −˙¯xd

−˙pζ

(15)
Since ((L + B) ⊗E3) is positive matrix, then there exists a
positive constant λ1 ≥λmin {(L + B) ⊗E3}, where λmin {A}
is the minimum eigenvalue of matrix A. Then, (15) becomes
˙V1 ≤−p−1κ1λ1 ∥Gs∥
+ p−1sT G
((L + B) ⊗E3)
ε −˙¯xd

−˙pζ

(16)
Noting that ψ(t) ∈C, ∀t ∈[0, tmax), it follows that s, ε, ζ
and ξ are bounded ∀t ∈[0, tmax). Since p−1, (L + B) ⊗E3
and ˙¯xd are bounded by the given assumption and structure,
then we have
p−1 ((L + B) ⊗E3)
ε −˙¯xd

−˙pζ

≤ϑ1,
∀t ∈[0, tmax)
(17)
In view of (16) and (17), one has
˙V1 ≤−p−1κ1λ1 ∥Gs∥2 + ϑ1 ∥Gs∥
= −∥Gs∥(σ1 ∥Gs∥−ϑ1)
(18)
where σ1 = p−1κ1λ1. It is obvious that ˙V1 ≤0 if ∥Gs∥≥
ϑ1/σ1, which implies that Gs = β is bounded on ∀t ∈
[0, tmax). Since ζi,j ∈C, ∀t ∈[0, tmax), then one can obtain
that

1 −ζ 2
i,j
−1
> 0 is bounded. According to the definition
of G and the boundedness of β, it is straightforward to obtain
that ∥s∥=
G−1 ∥β∥is bounded ∀t ∈[0, tmax). From (14),
α is bounded ∀t ∈[0, tmax).
Then, in order to achieve prescribed performance con-
straints
εi,j
 < ρ (t), we define the following candidate
Lyapunov function
V2,i = 1
2z⊤
i zi
(19)
Then the time derivative of V2,i yields
˙V2,i = z⊤
i ˙zi = ρ−1z⊤
i Hi (˙εi −˙ρξi)
= ρ−1z⊤
i Hi (˙vi −˙αi −˙ρξi)
= ρ−1z⊤
i Hi (Civi + ui + di −˙αi −˙ρξi)
(20)
where Hi = diag

1 −ξ2
i,j
−1
, i = 1, 2, 3.
The control law is designed as below
ui = −κ2,i

∥Hizi∥2 + µi
 1
2 Hizi
(21)
where κ1 > 0. By substituting (21) into (20), it yields
˙V2,i = −ρ−1κ2,i

∥Hizi∥2 + µi
 1
2 z⊤
i HHizi
+ ρ−1z⊤
i Hi (Civi + di −˙αi −˙ρξi)
(22)
Since ψ(t) ∈C, ∀t ∈[0, tmax), then it is evident that s, ε, ζ
and ξ are bounded on ∀t ∈[0, tmax), which further implies
that α is bounded on ∀t ∈[0, tmax) by virtue of (14). In view
of the boundedness of e, ¯xd, ε and α, we have that x and v
are bounded. From ˙αi = ∂αi
∂xi ˙xi + ∂αi
∂t , the fact that ∂αi
∂xi and
∂αi
∂t are smooth on ∀t ∈[0, tmax) by the definition and the
boundedness of x and v on ∀t ∈[0, tmax), ˙αi is bounded
on ∀t ∈[0, tmax). Noting that p−1, Ci, vi, ˙αi, ˙p and ξi are
bounded on ∀t ∈[0, tmax), there exists positive constant µi
such that the following constraint holds
ρ−1z⊤
i Hi (Civi + di −˙αi −˙ρξi)

≤µi ∥Hizi∥, ∀t ∈[0, tmax)
(23)
In view of (22), (23) and the fact that ∥Hizi∥2 + µi ≥
∥Hizi∥2, one can obtain that
˙V2,i = −ρ−1κ2,i

∥Hizi∥2 + µi
 1
2 ∥Hizi∥2
+ µi ∥Hizi∥≤−∥Hizi∥

ρ−1κ2,i ∥Hizi∥−µi

(24)
It is obvious that ˙V2,i ≤0 if ∥Hizi∥≥µi/
ρ−1κ2,i

,
which implies that Hizi = σ i is bounded on ∀t ∈[0, tmax).
Since ψ(t) ∈C, ∀t ∈[0, tmax), then one can obtain that

1 −ξ2
i,j
−1
> 0 is bounded, which indicates that Hi is
bounded on ∀t ∈[0, tmax). According to the boundedness
of Hi and σ i, it is straightforward to obtain that ∥zi∥=
H−1
i
 ∥σ i∥is bounded on ∀t
∈[0, tmax). From(21), u
is bounded on ∀t
∈
[0, tmax). Then, according to the
definition of signals in closed-loop, all signals in closed-loop
are bounded ∀t ∈[0, tmax).
C. STABILITY ANALYSIS
Theorem 2: Suppose that Assumptions 1-3 hold. Applying
the virtual control law (14) and control law (21) into
formation system (3), if ψ (0) ∈C holds, the following
statements hold.
1) All signals are semi-globally ultimately uniformly
bounded.
2) The fixed-time full-state error performance ∥ei∥< ρ (t)
and
εi,j
 < ρ (t) can be guaranteed.
68228
VOLUME 13, 2025

## Page 6

P. Yu, Q. Li: Fully Distributed Low-Complexity UAV Formation Control
proof : We first prove that all signals of closed-loop
system are semi-globally ultimately uniformly bounded ∀t ∈
[0, tmax) with tmax = +∞. Since there exists a unique and
maximal solution ψ(t) ∈C, ∀t ∈[0, tmax), then, according to
Theorem 2 in [42], two cases are possible: either tmax = +∞
or
lim
t→tmax−
h
∥ψ∥+
1
dS(ψ,C)
i
= ∞. From (18) and (24), one
can obtain that
lim
t→tmax−
h
∥ψ∥+
1
dS(ψ,C)
i
< ∞.
Thus, we can conclude that all signals of closed-loop
system are semi-globally ultimately uniformly bounded.
Since si,j and zi,j are bounded, the fixed-time prescribed
performance constraints ∥ei∥< ρ (t) and
εi,j
 < ρ (t) can
be guaranteed. This completes the proof.
Remark 1: This paper investigates a high-gain control
method, which may produce high control gain. However,
additional observers or adaptive laws are not required for
addressing external disturbances and uncertainties. Mean-
while, the fixed-time full-state error performance for UAV
formation can be guaranteed and the computation burden and
communication burden are reduced.
Remark 2: This paper reduces computational complexity
by eliminating the need for backstepping and its associated
repeated differentiation steps. Unlike traditional backstep-
ping controllers, our proposed fully distributed controller
design avoids the iterative calculations and derivative
computations inherent in that method. This simplification
significantly reduces the computational burden on each UAV.
The absence of a state observer further decreases complexity.
Existing methods often rely on observers to estimate the
states of neighboring UAVs, adding significant computational
overhead. Our approach leverages only the readily available
position information from neighbors, bypassing the need for
this computationally expensive estimation process.
IV. SIMULATION EXAMPLE
Consider a UAV formation with one virtual leader and three
followers, whose communication relationship graph is shown
in FIGURE. 2. The relative position δi between i-th follower
and the virtual leader is given below
δ1 =
 10
0
0 ⊤
δ2 =
 0
10
0 ⊤
δ3 =
 −10
0
0 ⊤
(25)
The initial state and model parameters are given below
x0 = [0, 0, 10]⊤,
x1 = [20, 0, 5]⊤
x2 = [0, 20, 7]⊤,
x3 = [−6, 0, 2]⊤
v0 = [0, 0, 0]⊤,
v1 = [0.1, 0.1, 0.3]⊤
v2 = [0.01, 0.2, −0.05]⊤,
v3 = [0.1, 0.1, 0.2]⊤
C1 =


1
2
1

,
C2 =


2
1
1

, C3 =


3
2
1


d1 = 0.1
 sin (0.1t)
sin (0.3t)
cos (0.1t) ⊤
d2 = 0.2
 sin (0.1t)
sin (0.3t)
cos (0.1t) ⊤
d3 = 0.3
 sin (0.1t)
sin (0.3t)
cos (0.1t) ⊤
FIGURE 2. Architecture diagram of UAV formation control.
FIGURE 3. The communication graph.
FIGURE 4. The formation tracking errors under fixed-time predefined
performance.
The parameters of fixed-time prescribed performance
function in (6) are chosen as ρ0 = 1000, ρ∞= 0.001, T =
10s, With such design, initial value of formation tracking
error ei and virtual tracking error εi can satisfy ∥ei (0)∥<
ρ (0) and
εi,j (0)
 < ρ (0), where i = 1, 2, 3 and j = 1, 2, 3.
In addition, formation tracking error ei and virtual tracking
error εi can convergence into stability set ∥ei∥< ρ∞= 10−3
and
εi,j
 < ρ∞= 10−3 within fixed time T
= 10s,
respectively. The parameters of virtual controller (14) and
controller (21) are set as κ1,i = 2, κ2,i = 100, respectively.
Then, the simulation results are plotted in FIGURE. 4,
FIGURE. 5, FIGURE. 6, FIGURE. 7. FIGURE. 8.
Figure 4 and Figure 5 illustrate that the formation tracking
errors converge to predefined steady-state accuracy ∥ei∥<
10−3 within a fixed time T
=
10 s. Figure 4 shows
VOLUME 13, 2025
68229

## Page 7

P. Yu, Q. Li: Fully Distributed Low-Complexity UAV Formation Control
FIGURE 5. The partial magnification graph of formation tracking errors.
FIGURE 6. Virtual tracking error with fixed-time prescribed performance.
FIGURE 7. Velocity.
FIGURE 8. Control input.
the formation tracking errors under fixed-time predefined
performance and Figure 5 is the partial magnification graph
of formation tracking errors.
FIGURE. 6 shows the virtual velocity tracking errors of
three UAVs over time, and these errors are confined to a preset
performance boundary within a fixed time T = 10s.
FIGURE. 7 shows the speed variations of three UAVs.
As three UAVs reach a steady value around 10 seconds, which
aligns with the preset time. This indicates that the controller
design can effectively control the movement of the UAVs.
V. CONCLUSION
In this paper, we have developed a fully distributed, low-
complexity UAV formation controller with fixed-time full-
state error performance. Under the proposed control scheme,
only the position information of neighbors is required for
communication, thereby effectively reducing the need for
global information and decreasing the communication load,
making it ideal for large-scale UAV formations. Unlike exist-
ing control methods that depending on adaptive parameters
and complex laws, this approach is able to handle external
disturbances without such requirements, simplifying the con-
struction of controller and reducing computational demands
to enhance real-time performance. Additionally, fixed-time
full-state error performance in the presence of external
disturbance and model uncertainty. The effectiveness of the
proposed control method has been verified by conducting a
numerical simulation. Designing a formation controller with
practical physical constrains and fixed-time full-state error
performance is an interesting topic for future investigation.
ACKNOWLEDGMENT
The authors thank the editors and reviewers for their construc-
tive suggestions, which have significantly improved the qual-
ity of this article. They also acknowledge Beijing LinksTech
Company Ltd. for providing the Indoor Multi-Agent Cooper-
ative Control Experimental Platform and technical support.
REFERENCES
[1] S. Yang and B. Xian, ‘‘Energy-based nonlinear adaptive control design for
the quadrotor UAV system with a suspended payload,’’ IEEE Trans. Ind.
Electron., vol. 67, no. 3, pp. 2054–2064, Mar. 2020.
[2] X.-Z. Jin, W.-W. Che, Z.-G. Wu, and C. Deng, ‘‘Robust adaptive general
formation control of a class of networked quadrotor aircraft,’’ IEEE Trans.
Syst. Man, Cybern. Syst., vol. 52, no. 12, pp. 7714–7726, Dec. 2022.
[3] H. Zhao, J. Shan, L. Peng, and H. Yu, ‘‘Learning-based robust bipartite
consensus control for a class of multiagent systems,’’ IEEE Trans. Ind.
Electron., vol. 70, no. 4, pp. 4068–4076, Apr. 2023.
[4] W. Zhou, J. Li, Z. Liu, and L. Shen, ‘‘Improving multi-target cooperative
tracking guidance for UAV swarms using multi-agent reinforcement
learning,’’ Chin. J. Aeronaut., vol. 35, no. 7, pp. 100–112, Jul. 2022.
[5] Z. Han, K. Guo, L. Xie, and Z. Lin, ‘‘Integrated relative localization and
Leader–Follower formation control,’’ IEEE Trans. Autom. Control, vol. 64,
no. 1, pp. 20–34, Jan. 2019.
[6] X. Dong, B. Yu, Z. Shi, and Y. Zhong, ‘‘Time-varying formation control
for unmanned aerial vehicles: Theories and applications,’’ IEEE Trans.
Control Syst. Technol., vol. 23, no. 1, pp. 340–348, Jan. 2015.
[7] R. Wang, X. Dong, Q. Li, and Z. Ren, ‘‘Distributed time-varying output
formation control for general linear multiagent systems with directed
topology,’’ IEEE Trans. Control Netw. Syst., vol. 6, no. 2, pp. 609–620,
Jun. 2019.
[8] Z. Li, G. Wen, Z. Duan, and W. Ren, ‘‘Designing fully distributed
consensus protocols for linear multi-agent systems with directed graphs,’’
IEEE Trans. Autom. Control, vol. 60, no. 4, pp. 1152–1157, Apr. 2015.
[9] Y. Cao, W. Yu, W. Ren, and G. Chen, ‘‘An overview of recent progress in the
study of distributed multi-agent coordination,’’ IEEE Trans. Ind. Informat.,
vol. 9, no. 1, pp. 427–438, Feb. 2013.
[10] Z. Wang, Y. Zou, Y. Liu, and Z. Meng, ‘‘Distributed control algorithm
for Leader–Follower formation tracking of multiple quadrotors: Theory
and experiment,’’ IEEE/ASME Trans. Mechatronics, vol. 26, no. 2,
pp. 1095–1105, Apr. 2021.
68230
VOLUME 13, 2025

## Page 8

P. Yu, Q. Li: Fully Distributed Low-Complexity UAV Formation Control
[11] H. Mo and G. Farid, ‘‘Nonlinear and adaptive intelligent control techniques
for quadrotor UAV—A survey,’’ Asian J. Control, vol. 21, no. 2,
pp. 989–1008, Mar. 2019.
[12] J. Alcalá-Fdez and J. M. Alonso, ‘‘A survey of fuzzy systems software:
Taxonomy, current research trends, and prospects,’’ IEEE Trans. Fuzzy
Syst., vol. 24, no. 1, pp. 40–56, Feb. 2016.
[13] E. Karmanova, V. Serpiva, S. Perminov, A. Fedoseev, and D. Tsetserukou,
‘‘SwarmPlay: Interactive tic-tac-toe board game with swarm of nano-UAVs
driven by reinforcement learning,’’ in Proc. 30th IEEE Int. Conf. Robot
Hum. Interact. Commun. (RO-MAN), Aug. 2021, pp. 1269–1274.
[14] M. B. Bezcioglu, B. Lennox, and F. Arvin, ‘‘Self-organised swarm flocking
with deep reinforcement learning,’’ in Proc. 7th Int. Conf. Autom., Robot.
Appl. (ICARA), Feb. 2021, pp. 226–230.
[15] C. C. Anabeza and A. A. Bandala, ‘‘Fuzzy logic controller for autonomous
environment-based drone swarm formation,’’ in Proc. IEEE Region
Symp. (TENSYMP), Sep. 2023, pp. 1–5.
[16] M. A. S. Teixeira, F. Neves Jr., A. Koubaa, L. V. R. De Arruda,
and A. S. De Oliveira, ‘‘A quadral-fuzzy control approach to flight
formation by a fleet of unmanned aerial vehicles,’’ IEEE Access, vol. 8,
pp. 64366–64381, 2020.
[17] X. Yi, K. Liu, D. V. Dimarogonas, and K. H. Johansson, ‘‘Dynamic event-
triggered and self-triggered control for multi-agent systems,’’ IEEE Trans.
Autom. Control, vol. 64, no. 8, pp. 3300–3307, Aug. 2019.
[18] Z.-M. Wang, A. Wei, and H. Shen, ‘‘Adaptive stabilization and H∞
control for switched nonlinear port-controlled Hamiltonian systems with
parameter perturbations,’’ in Proc. 37th Chin. Control Conf. (CCC),
Wuhan, China, Jul. 2018, pp. 891–896.
[19] R. Rashad, F. Califano, and S. Stramigioli, ‘‘Port-Hamiltonian passivity-
based control on SE(3) of a fully actuated UAV for aerial physical
interaction near-hovering,’’ IEEE Robot. Autom. Lett., vol. 4, no. 4,
pp. 4378–4385, Oct. 2019.
[20] H. Zhao, X. Dai, Q. Zhang, and J. Ding, ‘‘Robust event-triggered
model predictive control for multiple high-speed trains with switching
topologies,’’ IEEE Trans. Veh. Technol., vol. 69, no. 5, pp. 4700–4710,
May 2020.
[21] Z. Yi, F. Guowei, Y. Xuxia, and Y. Xuan, ‘‘Multi-UAV for-mation target
tracking control based on event-triggered strategy,’’ J. Beijing Univ.
Aeronaut. Astronaut., vol. 47, no. 11, pp. 2215–2225, 2021.
[22] Y. Lin, M. Wang, X. Zhou, G. Ding, and S. Mao, ‘‘Dynamic spectrum
interaction of UAV flight formation communication with priority: A deep
reinforcement learning approach,’’ IEEE Trans. Cognit. Commun. Netw.,
vol. 6, no. 3, pp. 892–903, Sep. 2020.
[23] X. Dong, Y. Hua, Y. Zhou, Z. Ren, and Y. Zhong, ‘‘Theory and
experiment on formation-containment control of multiple multirotor
unmanned aerial vehicle systems,’’ IEEE Trans. Autom. Sci. Eng., vol. 16,
no. 1, pp. 229–240, Jan. 2019.
[24] Y. Li, R. Wu, L. Gan, and P. He, ‘‘Development of an effective relay
communication technique for multi-UAV wireless network,’’ IEEE Access,
vol. 12, pp. 74087–74095, 2024.
[25] W. Xiangke, C. Hao, and Z. Shulong, ‘‘Formation control of large-scale
fixed-wing unmanned aerial vehicle swarms,’’ Control Decis. Making,
vol. 36, no. 9, pp. 2063–2073, 2021.
[26] I.
Katsoukis
and
G.
A.
Rovithakis,
‘‘A
low
complexity
robust
output
synchronization
protocol
with
prescribed
performance
for
high-order
heterogeneous
uncertain
MIMO
nonlinear
multiagent
systems,’’ IEEE Trans. Autom. Control, vol. 67, no. 6, pp. 3128–3133,
Jun. 2022.
[27] D. Qian, C. Li, S. Lee, and C. Ma, ‘‘Robust formation maneuvers through
sliding mode for multi-agent systems with uncertainties,’’ IEEE/CAA J.
Autom. Sinica, vol. 5, no. 1, pp. 342–351, Jan. 2018.
[28] S. Shao, M. Chen, J. Hou, and Q. Zhao, ‘‘Event-triggered-based
discrete-time neural control for a quadrotor UAV using disturbance
observer,’’ IEEE/ASME Trans. Mechatronics, vol. 26, no. 2, pp. 689–699,
Apr. 2021.
[29] A. Asignacion, S. Suzuki, R. Noda, T. Nakata, and H. Liu, ‘‘Frequency-
based wind gust estimation for quadrotors using a nonlinear disturbance
observer,’’ IEEE Robot. Autom. Lett., vol. 7, no. 4, pp. 9224–9231,
Oct. 2022.
[30] F. Wang, H. Gao, K. Wang, C. Zhou, Q. Zong, and C. Hua, ‘‘Disturbance
observer-based finite-time control design for a quadrotor UAV with
external disturbance,’’ IEEE Trans. Aerosp. Electron. Syst., vol. 57, no. 2,
pp. 834–847, Apr. 2021.
[31] N. P. Nguyen, H. Oh, and J. Moon, ‘‘Continuous nonsingular terminal
sliding-mode control with integral-type sliding surface for disturbed
systems: Application to attitude control for quadrotor UAVs under external
disturbances,’’ IEEE Trans. Aerosp. Electron. Syst., vol. 58, no. 6,
pp. 5635–5660, Dec. 2022.
[32] Z. Weiming, X. Yang, and L. Lin, ‘‘Fixed-time formation control of
quadrotor UAV swarm with unknown disturbances,’’ J. Beijing Univ.
Aeronaut. Astronaut., vol. 50, no. 5, pp. 1702–1712, 2024.
[33] H. Hua, Y. Fang, X. Zhang, and B. Lu, ‘‘A novel robust observer-based
nonlinear trajectory tracking control strategy for quadrotors,’’ IEEE Trans.
Control Syst. Technol., vol. 29, no. 5, pp. 1952–1963, Sep. 2021.
[34] S. Q. Zhou, H. C. Hua, X. W. Dong, Q. D. Li, and Z. Ren, ‘‘Air-ground time
varying formation tracking control for heterogeneous UAV-UGV swarm
system,’’ Aero Weaponry, vol. 26, no. 4, pp. 54–59, Aug. 2019.
[35] C. Li, Q. Ren, F. Chen, and P. Li, ‘‘Vision-based formation control of a
heterogeneous unmanned system,’’ in Proc. IECON 45th Annu. Conf. IEEE
Ind. Electron. Soc., vol. 1, Oct. 2019, pp. 5299–5304.
[36] Y. Li, J. Yang, and K. Zhang, ‘‘Distributed finite-time cooperative control
for quadrotor formation,’’ IEEE Access, vol. 7, pp. 66753–66763, 2019.
[37] A. Polyakov, ‘‘Nonlinear feedback design for fixed-time stabilization of
linear control systems,’’ IEEE Trans. Autom. Control, vol. 57, no. 8,
pp. 2106–2110, Aug. 2012.
[38] B. Li, W. Gong, Y. Yang, and B. Xiao, ‘‘Distributed fixed-time
leader-following formation control for multi-quadrotors with prescribed
performance and collision avoidance,’’ IEEE Trans. Aerosp. Electron.
Syst., vol. 59, no. 5, pp. 7281–7294, Oct. 2023.
[39] Y. Liu and G.-H. Yang, ‘‘Fixed-time fault-tolerant consensus control for
multi-agent systems with mismatched disturbances,’’ Neurocomputing,
vol. 366, pp. 154–160, Nov. 2019.
[40] X. Wei, W. Yu, H. Wang, Y. Yao, and F. Mei, ‘‘An observer-based
fixed-time consensus control for second-order multi-agent systems with
disturbances,’’ IEEE Trans. Circuits Syst. II, Exp. Briefs, vol. 66, no. 2,
pp. 247–251, Feb. 2019.
[41] J. Ni and P. Shi, ‘‘Adaptive neural network fixed-time leader–follower
consensus for multiagent systems with constraints and disturbances,’’ IEEE
Trans. Cybern., vol. 51, no. 4, pp. 1835–1848, Apr. 2021.
[42] C. K. Verginis, A. Nikou, and D. V. Dimarogonas, ‘‘Robust formation
control in SE(3) for tree-graph structures with prescribed transient and
steady state performance,’’ Automatica, vol. 103, pp. 538–548, May 2019.
[43] Y. Hong and C.-T. Pan, ‘‘A lower bound for the smallest singular value,’’
Linear Algebra Appl., vol. 172, pp. 27–32, Jul. 1992.
[44] C. P. Bechlioulis and G. A. Rovithakis, ‘‘A low-complexity global
approximation-free
control
scheme
with
prescribed
performance
for unknown pure feedback systems,’’ Automatica, vol. 50, no. 4,
pp. 1217–1226, Apr. 2014.
PENGFEI YU received the bachelor’s degree
in automation from Beijing Information Science
and Technology University, in 2023, where he
is currently pursuing the master’s degree. His
main research interest includes cluster formation
control.
QING LI received the Ph.D. degree from China
Academy of Launch Vehicle Technology, Beijing,
China, in 2003. She is currently a Professor
with Beijing Information Science and Technology
University. Her current research interests include
control, inertial device, novel gyro sensor, and
integrated navigation.
VOLUME 13, 2025
68231
