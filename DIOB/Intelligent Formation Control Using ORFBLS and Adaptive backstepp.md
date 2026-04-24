# Intelligent Formation Control Using ORFBLS and Adaptive backstepp.pdf

## Page 1

Manuscript 2816 
Intelligent Formation Control Using ORFBLS and Adaptive backstepping 
Intelligent Formation Control Using ORFBLS and Adaptive backstepping 
Sliding-Mode Control to address Uncertain Tilting in multi-Quadrotors 
Sliding-Mode Control to address Uncertain Tilting in multi-Quadrotors 
during Wind Gusts 
during Wind Gusts 
Ching-Chih Tsai 
Chun-Fu Mao 
Kumail Hussain 
Follow this and additional works at: https://jmstt.ntou.edu.tw/journal 
 Part of the Fresh Water Studies Commons, Marine Biology Commons, Ocean Engineering Commons, 
Oceanography Commons, and the Other Oceanography and Atmospheric Sciences and Meteorology Commons

## Page 2

RESEARCH ARTICLE
Intelligent Formation Control Using ORFBLS and 
Adaptive backstepping Sliding-mode Control to 
Address Uncertain Tilting in Multi-quadrotors 
During Wind Gusts
Ching-Chih Tsai*, Chun-Fu Mao, Kumail Hussain
Department of Electrical Engineering, National Chung Hsing University, Taichung, Taiwan, ROC
Abstract
In terms of aerial robotics, stable and precise formation control is a significant challenge for tilting multi-quadrotors 
during disturbances. This paper proposes a fixed-time formation control strategy for tilting multi-quadrotors to address 
the effect of external wind gusts. The observer accurately predicts environmental disturbances and an adaptive 
backstepping sliding-mode control (ABSMC) method with an output recurrent fuzzy broad learning system (ORFBLS) 
addresses these disturbances within a finite time. ORFBLS dynamically adjusts its structure through a growing 
ORFBLS structure to allow nodes to be added as needed. The method's stability is validated using Lyapunov stability 
theory and ensures the convergence of the quadrotor's states within a fixed time, irrespective of mass variations. 
Comparative simulations and experimental validations using three cooperative tilting quadrotors demonstrate the 
proposed control system's effectiveness, which is enhanced by the ORFBLS structure and accurate disturbance 
detection and compensation. These simulations and experiments confirm the method's adaptability and its ability to 
maintain a stable formation during wind gusts.
Keywords: Adaptive backstepping sliding mode control, Airdrops, Formation control, Lyapunov stability, ORFBLS, 
Tilting multi-quadrotors, Wind gusts
1. Introduction
A 
utonomous 
aerial 
robotics, 
particularly 
multi-quadrotor formations, present tech­
nological challenges. Tilting quadrotors are used 
for surveillance and environmental monitoring and 
exhibit complex dynamics. Studies of cooperative 
control 
strategies 
across 
various 
platforms, 
including UAVs, sensor networks and multi-robot 
systems, have developed control solutions [1,2]. 
Intelligent nonlinear control and average consensus 
[3,4] 
are 
used 
to 
increase 
robustness 
and 
performance.
Marine science and technology applications 
involve navigation, route optimization and envi­
ronmental monitoring and require complex control 
systems to manage dynamic and challenging con­
ditions [5—7]. Multi-quadrotor systems are used in 
marine environments to enhance capabilities in 
marine surveillance, pollution tracking and search 
and rescue operations that require stable operation 
during environmental disturbance such as wind 
gusts. To optimize learning processes and minimize 
the complexities of system architecture, the Broad 
Learning System (BLS) was used to develop a Fuzzy 
BLS (FBLS). The FBLS increases the BLS's learning 
Received 4 August 2024; revised 17 November 2025; accepted 19 November 2025. 
Available online 16 March 2026 
* Corresponding author.
E-mail addresses: cctsai@nchu.edu.tw (C.-C. Tsai), d110064008@mail.nchu.edu.tw (C.-F. Mao), g111067075@mail.nchu.edu.tw (K. 
Hussain). 
https://doi.org/10.51400/2709-6998.2816 
2709-6998/© 2026 National Taiwan Ocean University.

## Page 3

capabilities by using the Takagi-Sugeno fuzzy sys-
tem and an enhancement node to increase learning 
efficiency [8—10]. FBLS is used in servo systems in 
tool-grinding machines [11,12] and in PID control-
lers in semiconductor wafer-cleaning machines 
[13,14]. Advances in Output Recurrent Fuzzy BLS 
(ORFBLS) and Recurrent FBLS (RFBLS) [15,19] 
enhance 
learning 
by 
incorporating 
feedback 
mechanisms and real-time parameter adjustments 
that use a gradient descent.
In the context of marine science and technology, 
ORFBLS and adaptive control methods offer sig-
nificant potential. Previous studies show the use of 
intelligent control systems to optimize fuel con-
sumption, allow better predictive maintenance and 
improve safety and security management in mari-
time operations [16,17]. Intelligent control systems 
have a crucial role in marine operations, as 
demonstrated by the real-time increases in the en-
ergy efficiency of ships by predicting operating 
conditions [18]. Few studies involve these advanced 
control systems in uncertain and dynamic marine 
settings. This study uses an adaptive formation 
control system for tilting multi-quadrotors for ma-
rine applications.
Using the results of previous studies [16,17], this 
study develops an output recurrent fuzzy broad 
learning system (ORFBLS) with adaptive back-
stepping sliding mode control (ABSMC). The 
growing ORFBLS structure uses incremental least 
squares learning for dynamic structural adjust-
ments by adding new nodes as needed. This 
significantly improves system adaptability and 
maneuverability. This technique uses a disturbance 
observer to predict environmental changes and 
uses Lyapunov stability to ensure consistent system 
stability and convergence in changing conditions. 
Simulations demonstrate that the ORFBLS-ABSMC 
controller is adaptive and robust in terms of aerial 
robotics and establishes a new standard in intelli-
gent control. Marine applications of this technology 
include monitoring sea traffic, pollution tracking 
and aerial data collection.
This paper is structured as follows. Section 2 de-
tails the modeling of tilting multi-quadrotors, a 
wind turbulence model, problem formulation and 
ORFBLS function approximation. Section 3 de-
scribes the growing ORFBLS structure. Section 4
describes the design of the disturbance-observer- 
based ORFBLS-ABSMC controller and conducts a 
closed-loop stability analysis of the proposed 
strategy. Section 5
presents three numerical 
simulations to demonstrate the proposed control 
strategy's effectiveness and robustness. Section 6
details experimental results to show the applica-
bility of the proposed method. Section 7 details the 
limitations of the proposed method and Section 8
gives conclusions.
2. Preliminary analysis and problem 
formulation
This section discusses the modelling of multiple 
cooperative tilting quadrotors, a wind turbulence 
model, problem formulation and ORFBLS function 
approximation.
A. Multiple Tilting Quadrotors Model
To determine the formation control law for a 
multi-quadrotor system that features a virtual 
leader, the dynamic state equation for the overall n- 
quadrotor system [16,17] is rewritten in vector-ma-
trix form as: 
[ _P
_q
]
=
⎡
⎣
ν
1
2Qω
⎤
⎦
(1)
[ _ν
_ω
]
=
[
G+Kmdiag
[
RI
b
(
qi
)]
T +Δaf
J−1[−SωJω+τ]+Δατ
]
;
[ _Ti
_τi
]
=Bαi;Ωi
[ _Ωi_Ωi
]
(2)
where P =
[
P1T; :::; PnT]T∈R3n, v =
[
vT
1 ; :::; vT
n
]T 
∈R3n, q =
[
qT
1 ; :::; qT
n
]T∈R4n, Q =
diag(Qi)ω =
[(
ωb
1
)T; :::;
(
ωb
n
)T]T
∈R3n, 
G =
1n ⊗
ĝe3, 
Km =
diag
(
m−1
i
)
⊗
I3, 
T =
[
TT
1 ; :::; TT
n
]T∈R3n, 
Δa =
[
ΔT
a1; :::; ΔT
an
]T
∈R3n, Δα =
[
ΔT
α1; :::; ΔT
αn
]T
∈R3n; Δaf =
[
Δa + Δf
]T∈R3n, Δατ = [Δα + Δτ]T∈R3n 
The proposed control law determines T and τ for 
the overall system, where Ti and τi are specified for 
each quadrotor, to achieve formation flight.
B. Graph Theory
To model the communication for quadrotor 
swarms, as shown in Fig. 1(a), the interconnection 
topology for n follower tilting quadrotors is a 
directed subgraph G, where n networking HOMRs 
(Heterogeneous Obstacle Mapping Robots) are 
110 
JOURNAL OF MARINE SCIENCE AND TECHNOLOGY 2026;34:109—121

## Page 4

regarded as n nodes. The adjacency matrix A of the 
subgraph G is described as: 
{
1
if node i receives information from node j
0
otherwise 
where, aij = 0 Therefore, the Laplacian matrix for 
the directed subgraph G is L = D-A, where 
D = diag(d1,d2, …,dn) is the degree matrix and A is 
the adjacency matrix.
Directed graph theory is used to model the 
overall swarm system. The formation system com-
prises n heterogeneous quadrotors and one virtual 
leader, which is regarded as the (n+1)th HOMR. 
Therefore, the connecting multi-quadrotor swarm 
system with a virtual leader is also modeled as a 
directed graph G, and its Laplacian matrix L is also 
expressed as L = D −
A.
The interconnected topology of this directed 
graph D is governed by a spinning tree and the 
virtual leader is the root. To model the accessibility 
of any HOMRs to its leader, the diagonal matrix B is 
written as: 
{
1 if node i receives formation commond from node
(n + 1)
0 otherwise 
The diagonal matrix B has at least one non-zero 
element so a follower can receive commands from 
the leader. Therefore, (L + B) is invertible according 
to the spinning tree assumption of the inter-
connected topology. To achieve formation control, 
three key assumptions about the system are 
proposed.
Assumption 1. The directed graph G is modeled as 
a spanning tree whose leader robot is virtual, 
denoted by the (n+1)th quadrotor.
Assumption 2. Each quadrotor is connected to the 
leader in the network but not all quadcopters 
require direct access to information from the 
leader.
Assumption 3. The leader moves independently 
within the formation system. 
By ensuring that the quadrotor swarms can main-
tain stable formation control, this graph theory 
model applies to various marine scenarios. Coor-
dinated quadrotor swarms that are used for marine 
surveillance can cover vast oceanic areas, track and 
monitor pollution levels and assist in search and 
rescue missions by quickly locating and responding 
to distress signals. The robustness of the control 
strategy ensures reliable performance in dynamic 
and uncertain marine conditions.
C. Wind Turbulence Model
This subsection describes a wind disturbance 
model to determine automatic landing performance 
in various wind conditions and these wind distur-
bances are modeled by the Dryden spectrum. The 
disturbance equations for the longitudinal wind 
and the vertical wind are written as: 
ug =ug1 + ugc
(3)
wg =σw
̅̅̅̅̅
aw
√
(
awwg1 +
̅̅
3
√
wg2
)
(4)
_ug1 =0:2
⃒⃒ugc
⃒⃒
̅̅̅̅̅̅̅
2au
√
N1 −auug1
(5)
_wg1 =wg2
(6)
_wg2 =N2 −aw
2wg1 −2awwg2
(7)
where 
ugc =
{
−u0(1 + ln(h=510)=ln(51));
h ≥10 ft
0;
h < 10 ft
, 
Fig. 1. Formation control system for multiple tilting Quadcopters: (a) 
System structure and (b) the block diagram for each quadrotor.
JOURNAL OF MARINE SCIENCE AND TECHNOLOGY 2026;34:109—121 
111

## Page 5

aw = U0=h 
au =
{
U0
/(
100
̅̅̅
h
3√)
;
h>230 ft
U0
/
600;
h ≤230 ft
;
σw =
{0:2
⃒⃒ugc
⃒⃒;
h>500 ft
0:2
⃒⃒ugc
⃒⃒(0:5 + 0:00098h);
h ≤500 ft 
and h is the altitude u0 is the wind speed at 
different altitudes and N1 and N2 are two Gaussian 
white noise processes with zero mean and a stan-
dard deviation of 10.
D. Problem Statement
The objective of the formation control system in 
Fig. 1
is to maintain position and follow a 
consensus-based trajectory for tilting quadrotors 
during wind gusts. Using an adaptive cooperative 
strategy guarantees the convergence of position, 
such that, lim
t→∞
{
Pi
I(t) −
Pj
I(t)
}
= 0, i; j∈{1; 2; :::; n +
1}, where P
I
i(t) = PI
i(t) −
f i(t), PiI(t) is the current 
position of the ith tilting quadrotor, PI
n+1(t) is the 
position of the virtual leader and f i(t) is the relative 
position vector of the ith tilting quadrotor with 
respect to the leader's position. f n+1(t) =
0, 
_f n+1(t) = 0, and the relative position vector for 
every tilting quadrotor must be real and distinct. 
For adaptive cooperative consensus-based forma-
tion control to overcome wind disturbance three 
assumptions are proposed.
Assumption 1. Pd is the trajectory command and its 
time derivatives, _Pd, €Pd, P
...
d, are defined and boun-
ded. This ensures stability and controllability if ug 
and wg model changing wind conditions.
Assumption 2. The state variables, P, v, q, ω, are 
measurable. This enables the control system to 
make adjustments in response to wind gusts.
Assumption 3. If ωi and αi are constrained within a 
reasonable bounded region, then B
−1
α;Ω
is well 
defined. Under this assumption, the system is 
“controllable”, so for any desired trajectory of 
[
TT; τT]T and 
[ _T
T; _τT]T, there exists a unique 
solution for 
[
ΩT; αT]T and 
[ _Ω
T; _α
T]T that satisfies (3) 
for the system constraints.
E. ORFBLS function approximation
Figure 2 shows the structure of the ORFBLS, which 
has five layers: an input, fuzzy subsystem, defuz-
zification, augmentation and output layers. Previ-
ous studies [2] show that the output from the output 
layer is the weighted sum of its input and is 
described as: 
y(3) =
(
W(3))Tx(3)
(8)
where W(3)∈R(N1+H2)×N is the weight matrix and 
y(3)∈RN is the output of the ORFBLS. To determine 
the ORFBLS function approximation for the un-
certainty vector, Δa, the ideal approximation result 
for the ORFBLS for, Δa, is: 
Δ* =y*(3) =
(
W*(3))Tx*(3) + ϵ*
(9)
Therefore, the approximation errors for the 
ORFBLS are written as: 
~Δ=Δ−Δ* = ̂
W
(3)T ∂̂x
(3)
∂̂
W
(2) ~W
(2) + ̂
W
(3)T∂̂x
(3)
∂̂β
~β+ ∂̂x
(3)
∂̂
W
(3) ~W
(3)
+∂̂x
(3)
∂̂σ ~σ+∂̂x
(3)
∂̂α ~α+∂̂x
(3)
∂̂c ~c+h
(10)
Fig. 2. Structure of the proposed ORFBLS.
112 
JOURNAL OF MARINE SCIENCE AND TECHNOLOGY 2026;34:109—121

## Page 6

where h = ̂
W
(3)T ~h + ϵ, and h is assumed to be 
bounded, i.e., ‖h‖∞< hmax < ∞. ~W
(1)
= vec
( ~W
(1))
, 
~W
(2)
= vec
( ~W
(2))
.
3. Growing ORFBLS structure
This subsection describes the development of the 
growing ORFBLS structure method, which uses the 
adaptive expansion principles of growing RBFNN 
structure learning with the efficient and fast 
expansion characteristics of BLS (Broad Learning 
System) incremental learning. The growing RBFNN 
in Fig. 3 uses new basis functions in a neural 
network so complexity and capability are increased 
if the observed error for the system exceeds this 
threshold. BLS incremental learning. The model 
expansion strategy does not require exhaustive 
retraining so the system is responsive to new data 
or different degrees of complexity [8].
In terms of the ORFBLS, if the output error ex-
ceeds the specified limit, the system enters the 
enhancement phase. The ORFBLS grows by adding 
more nodes to its fuzzy logic subsystem, which in-
creases the network's complexity. An optimal bal-
ance of system accuracy and adaptability requires 
fine-tuning of the node weights and thresholds. The 
growing ORFBLS structure increases system sta-
bility by continually adjusting weight vectors in the 
output layer to adjust newly added nodes, so the 
system adapts quickly to manage multi-quadrotors 
under varying wind conditions. In unpredictable 
scenarios such as quadcopter navigation, this 
structure is crucial for swift and precise adaptation. 
The growing ORFBLS structure maintains perfor-
mance, accuracy and adaptability. Algorithm 1 de-
scribes the dynamic weight adjustments for this 
structure and Table I lists the notations for Algo-
rithm 1. The fuzzy subsystem's weight adjustments 
are achieved as: 
Wnew =Wold + ΔW
(11)
Table I. List of notations.
Symbol
Definition
Symbol
Definition
x y z
Position coordinates of the quadcopter
Fd; Td
Disturbance force and torque
_x _y _z
Velocity components in the x y z frames
ωx; ωy; ωz
Angular velocity components
€x €y €z
Acceleration components in the x, y, z frames
L
Laplacian matrix representing the graph topology
ϕ θ ψ
Roll, pitch and yaw angles
B
Diagonal matrix for graph connectivity
_ϕ _θ _ψ
Angular velocities
τx τy τz
Torque components in the x,y,z axes
u1 u2 u3 u4
Control inputs
_S
Time derivative of the sliding surface derivative
m
Mass of the quadrotor
k; λ
Controller gains
Ix; Iy; Iz
Moments of inertia about x,y,z axes
ep ev
Position and velocity errors
g
Gravitational acceleration
h
Altitude
T
Thrust generated by rotors
u0
Wind speed
N1; N2
Gaussian noise processes
δ
Approximation error of ORFBLS
W; V
Weight matrices
α
Adaptive coefficient for backstepping control
μ; η
Parameters for Lyapunov function derivation
zf
Nodes in feature mapping layer of ORFBLS
H
Enhancement nodes in ORFBLS
∈
Threshold for node expansion in growing ORFBLS
x y z
Desired position coordinates
v
Velocity of the virtual leader
Initialize
Compute 
Output
Expand 
Structure 
Update 
Weights 
Check
Stability
End
Compute 
Error
stable
unstable
Fig. 3. Flowchart for the growing ORFBLS mechanism.
JOURNAL OF MARINE SCIENCE AND TECHNOLOGY 2026;34:109—121 
113

## Page 7

The new fuzzy subsystem parameters are initial-
ized as: 
mnew =round(x(t));σnew =k(mnew −mnearst)
(12)
The output layer weights are updated as: 
W(o) =Wo
old + ΔW(o)
(13)
and the weights of the enhancement nodes are 
improved as: 
W(e) =W(e)
old + ΔW(e)
(14)
This method I used to develop this adaptive 
ORFBLS structure growth. The raised ORFBLS 
adapts to new data and complex function approxi-
mations to retain learning accuracy.
4. Design of the disturbance-observer-based 
ORFBLS-ABSMFC controller
A. Disturbance Observer Design for Force Δf
One auxiliary equation for the translational dy-
namics is expressed as: 
̂_ν =G+Kmdiag
[
RI
b
(
qi
)]
T +Δaf + Kv1ve
(15)
The velocity error is defined as: 
ve =v −̂v
(16)
so the force disturbance estimator is written as: 
_̂Δaf =Kv1 _ve −Kv2̂ve
(17)
Using (1) and the auxiliary system equation (15), 
the error velocity error (16) is calculated to estimate 
the effect of disturbance, ̂Δf on the translational 
dynamics. Therefore, 
_ve = −Kv2ve + Δf −
̂Δf
(18)
B. 
Disturbance 
Observer 
Design 
for 
the 
Torque Δτ
There is one auxiliary system for the rotational 
dynamics: 
̂_ω =J−1[−SωJω+τ]+Δατ + Kw1ωe
(19)
The estimation error is defined as: 
ωe =ω −
̂ω
(20)
and the torque disturbance is calculated as: 
_̂Δατ =Kw1 _ωe −Kω2 ̂ωe
(21)
Using (2) and (19), the estimation error (20) is 
calculated. Similarly to a previous study (18), an 
estimate of the disturbance Δτ that affects the 
rotational dynamics is expressed as: 
_ωe = −Kw2ωe + Δτ −
̂Δτ
(22)
Algorithm 1. Growing ORFBLS Structure.
Algorithm 1: Growing_ORFBLS_Structure_ 
114 
JOURNAL OF MARINE SCIENCE AND TECHNOLOGY 2026;34:109—121

## Page 8

C. ORFBLS-ABSMFC Controller Design
The following section details the design of the 
proposed ORFBLS-ABSMFC controller for a multi- 
quadcopter formation, using ORFBLS and adaptive 
backstepping sliding mode control (ABSMC). The 
controller is shown in Fig. 4. The ABSMFC is the 
primary controller and ORFBLS compensates for 
uncertainties or un-modeled errors. The block of the 
least square method and Lyapunov stability are used 
to update the ORFBLS compensator parameters. The 
system dynamics are then described using error or 
regulatory variables. The sliding mode control is 
applied to these regulatory variables to bring the 
new variables to the origin. Similar to previous 
studies [5,18] the quadrotor model is rewritten as: 
[ _Pi
_qi
]
=
⎡
⎣
vi
1
2Qiωb
i
⎤
⎦;
[
_vi
_ωb
i
]
=
[
ĝe3 + m−1
i RI
b
(
qi
)
Ti + Δaf
J−1
i
[
−SωiJiωb
i + τi
]
+ Δατ
]
(23)
Modelling the first formation error with the 
communication topology gives: 
δ1 =((L + B)⊗I3)−1((L+B)⊗I3)
(
P−f −1n ⊗PL
)
= P−f −((L + B)⊗I3)−1[
(A⊗I3)
(
P−f
)
+b⊗PL
]
(24)
The time derivative of (24) gives: 
_δ1 =v−
_f −((L + B)⊗I3)−1[
(A⊗I3)
( _P−
_f
)
+b⊗_PL
]
(25)
The system's overall stability and parameter up-
date laws are determined after the ABSMC is 
updated using ORFBLS.
Step 1. The position tracking error and its time 
derivative are written as: 
δ1 =P −Pd; _δ1 = v −
_Pd
(26)
The attitude tracking error and its time derivative is 
given by 
~q=
[
~η ~ϵT]T =qd
−1 ∘q; _~q=
[ _~η
_~ϵ
]
=1
2
[
−~ϵT
~ηI + S(~ϵ)
]
~ω
(27)
Let the proposed Lyapunov function is V1 =
0:5δ1
Tδ1 + 2(1 −~η). By differentiating the Lyapunov 
function, one obtains: 
_V1 =δ1
T(v−
_Pd) +~ϵTRI
b
(
qd
)(
ωb −ωd
d
)
(28)
The virtual control law is defined as: 
[
v
ωb
]
=Φ1 =
[
Φ1a
Φ1b
]
=
[ _Pd −k1aδ1
−Rb
I
(
qd
)
k1b~ϵ
]
(29)
Substituting (29) into (28) gives: 
_V1 = −k1aδ1
Tδ1 −k1b~ϵT~ϵ −~ϵTRI
b
(
qd
)
ωd
d
(30)
Step 2. The velocity backstepping error is defined 
as: 
δ2 =
[
v
ωb
]
−Φ1 =
[
δ2a
δ2b
]
=
[
v
ωb
]
−
[
Φ1a
Φ1b
]
(31)
The time derivative of (31) is written as: 
_δ2 =
[ _δ2a
_δ2b
]
=
⎡
⎢⎣
−δ1 −k2aδ2a + ~Δaf −
_Φ1b + 1
mR1
b
(
q
)
δ3b
−Rb
1
(
qd
)~ϵ −k2bδ2b + ~Δατ −
_Φ1b + J−1δ3b
⎤
⎥⎦
=
[
−δ1 −k2aδ2a + ~Δaf −
_Φ1a
−Rb
1
(
qd
)~ϵ −k2bδ2b + ~Δατ −
_Φ1b
]
+
⎡
⎢⎣
1
mR1
b
(
q
)
0
0
J−1
⎤
⎥⎦δ3
(32)
which is rewritten as: 
_δ2 =
[
−δ1 −k2aδ2a + ~Δaf −
_Φ1a
−Rb
I
(
qd
)~ϵ −k2bδ2b + ~Δατ −
_Φ1b
]
+ Jδ3
(33)
The time derivative for the Lyapunov function 
V2 = V1 + 0:5δ2
Tδ2 is: 
_V2 = −k1aδ1
Tδ1 +δ1
Tδ2a −k1b~ϵT~ϵ−~ϵTRI
b
(
qd
)
ωd
d
+~ϵTRI
b
(
qd
)
δ2b +δ2a
T
[
ĝe3 + 1
mRI
b
(
q
)
T +Δaf −
_Φ1a
]
+δ2b
T{
J−1[
−S
(
ωb)
Jωb +τ
]
+Δατ −
_Φ1b
}
(34)
In terms of the backstepping error vector for the 
desired force and torque compared to the actual 
force and torque vector, the second virtual control 
law, Φ2 is defined as: 
[
T
τ
]
=Φ2 =
[
Φ2a
Φ2b
]
=
⎡
⎣mRb
I
(
q
)[
−δ1 −ĝe3 −
̂Δaf −k2aδ2a
]
S
(
ωb)
Jωb + J
[
−Rb
I
(
qd
)~ϵ −
̂Δατ −k2bδ2b
]
⎤
⎦
(35)
Substituting (35) into (34) gives: 
ABSMC
Position 
Tracking 
Error 
Sliding-
Mode 
Control
Backstepping 
Control
Disturbance
Observer
Fig. 4. Block diagram of the proposed ABSMC method with the 
disturbance observer.
JOURNAL OF MARINE SCIENCE AND TECHNOLOGY 2026;34:109—121 
115

## Page 9

_V2 = −k1aδ1
Tδ1 −k1b~ϵT~ϵ−~ϵTRI
b
(
qd
)
ωd
d −k2aδ2a
Tδ2a
+δ2a
T ~Δaf −δ2a
T _Φ1a −k2bδ2b
Tδ2b +δ2b
T ~Δατ −δ2b
T _Φ1b
(36)
Step 3. This step defines the backstepping error 
vector for the desired force and torque compared to 
the actual vector as: 
δ3 =
[
δ3a
δ3b
]
=
[
T
τ
]
−Φ2
(37)
Using the sliding surface design, a new surface S 
is written as: 
S=δ3
(38)
for which the time derivative is calculated as: 
_S= d
dt
[
T
τ
]
−
_Φ2 =Bαi;Ωi
[ _Ωi_Ωi
]
−
_Φ2
(39)
The actual control law is written as: 
[ _Ω
Ωα
]
=B
−1( _Φ2 −k3S−k4sgn(S)
)
(40)
where k3 and k4 are two positive design con-
stants. Using (39) gives 
ST _S= −wSTsgn(S) −k4STS<0
(41)
such that S = δ3 approaches zero in finite time. 
This does not show that _V2 in (36) is negative semi- 
definite.
E. Closed-Loop Stability Analysis and Parameter 
Updating
This subsection analyzes the system stability and 
parameter updating technique for the closed-loop. 
Two disturbance observers are used for each 
quadrotor to generate approximation errors for the 
ORFBLS estimators and these errors are used to 
train all observers for ̂Δaf and ̂Δατ. These errors are 
used to train and optimize ORFBLS estimators 
using the least squares method to increase preci-
sion and adaptability, as described by a previous 
study [17]. This method addresses uncertainties and 
allows dynamic aerial maneuvers for the control of 
a tilting multi-quadrotor formation. Incremental 
learning increases the estimators' ability to main-
tain formation during unpredictable environmental 
changes. Theoretically, two disturbance observers 
for each tilting quadrotor are proposed as: 
_̂vi =k6~vi +ĝe3 +m−1
i RI
b
(
qi
)
Ti + ̂Δafi
(42)
_̂ωi
b =k7 ~ωi
b +Ji
−1[
−SωiJiωi
b +τi
]
+ ̂Δατi
(43)
where ̂vi and ̂ωi
b are the estimations for the velocity 
of the inertial-axis and the body rotational velocity 
of the body-axis for the ith quadrotor: ~vi = vi −
̂vi, 
and ~ωi
b = ωib −
̂ωi
b. Therefore, the dynamics of the 
estimation errors for the overall system are: 
_~v= −k6~v + ~Δaf;
(44)
_~ω= −k7 ~ω + ~Δατ
(45)
in which ~v =
[~v1
T; :::; ~vn
T]T, ~ω =
[
~ω1
bT; :::; ~ωn
bT]T
, 
~Δaf =
[
~Δ
T
a + ~Δ
T
f ; :::::::~Δ
T
an + ~Δ
T
fn
]T 
and 
~Δaτ =
[~Δ
T
α + ~Δ
T
τ ; :::::::~Δ
T
αn + ~Δ
T
τn
]T
. To analyze the closed- 
loop stability and derive the parameter-updating 
laws, the Lyapunov function including ̂α, ̂c, ̂v, ̂
W
(2)
and ̂
W
(3) is used: 
V3 =V2 +1
2γ1~vT~v+1
2
1
λ1
tr
[
~W
(o)aT
~W
(o)
a
]
+1
2
1
λ2
~W
sub
a
T ~W
sub
a
+1
2
1
λ3
~σT
a ~σa + 1
2
1
λ4
~caT~ca +1
2
1
λ5
~αaT ~αa +1
2γ2 ~ωbT ~ωb
+1
2
1
λ6
tr
[ ~W
(o)T
α
~W
(o)
α
]
+ 1
2
1
λ7
~W
sub
α
T ~W
sub
α
+1
2
1
λ8
~σT
α~σα +1
2
9
λ9
~cαT~cα +1
2
1
λ10
~ααT ~αα +1
2STS
(46)
From (10), the estimation errors for the ORFBLS 
for the ith tilting quadrotor for Δaf and Δατ are: 
~Δafi = ~W
(3)
ai
T
̂x
(3)
ai + ̂
W
(3)
ai
T ∂̂x
(3)
∂̂
W
(2)
ai
~W
(2)
ai + ̂
W
(3)T∂̂x
(3)
∂̂αai
~αai
+̂
W
(3)T∂̂x
(3)
∂̂cai
~cai + ̂
W
(3)T∂̂x
(3)
∂̂βai
~βai +hai
(47)
~Δατi = ~W
(3)
αi
T
̂x
(3)
αi + ̂
W
(3)
αi
T ∂̂x
(3)
∂̂
W
(2)
αi
~W
(2)
αi + ̂
W
(3)T∂̂x
(3)
∂̂ααi
~ααi
+̂
W
(3)T∂̂x
(3)
∂̂cαi
~cαi + ̂
W
(3)T∂̂x
(3)
∂̂βαi
~βαi +hαi
(48)
so using (41), (36), (47) and (48), the time deriv-
ative of (46) is:in which U1i = δ2ai + γ1~vi, U2i = δ2ai +
γ2 ~ωi
b where γ1 and γ2 are two positive and real 
constants. From (50), the following online parame-
ters to update the rules for both ORFBLSs are 
written as: 
116 
JOURNAL OF MARINE SCIENCE AND TECHNOLOGY 2026;34:109—121

## Page 10

where, λi; i = 1 ∼10, are the updating rates for the 
parameters for the ORFBLS. Using the online 
parameter adjustment laws, the time derivative of 
the Lyapunov function is:which is negative semi- 
definite if the following conditions are satisfied: 
_V2 ≤−k1a‖δ1‖2 −k1b‖~ϵ‖
(
‖~ϵ‖ −
1
k1b
⃦⃦RI
b
(
qd
)
ωd
d
⃦⃦
)
−k2a‖δ2a‖
(
‖δ2a‖ −
1
k2a
‖ _Φ1a −ϵa‖
)
−k2b‖δ2b‖
(
‖δ2b‖ −
1
k2b
‖ _Φ1b −ϵα‖
)
−k3‖δ3‖
(
‖δ3‖ −
1
k3
‖ _Φ2‖
)
−k4‖δ4‖2
−k6γ1‖~v‖
(
‖~v‖ −
1
k5
‖ϵa‖
)
−k7γ2
⃦⃦~ωb⃦⃦
(⃦⃦~ωb⃦⃦−
1
k6
‖ϵα‖
)
−wSTsgn(S) −k4STS
(51)
which is negative semi-definite if the following 
conditions are satisfied: 
‖δ2a‖ ≥1
k2a
‖ _Φ1a −ϵa‖;‖δ2b‖ ≥1
k2b
‖ _Φ1b −ϵα‖
‖δ3‖ ≥1
k3
‖ _Φ2‖;‖~v‖ ≥1
k6
‖ϵa‖;
⃦⃦~ωb⃦⃦≥1
k7
‖ϵα‖;
‖~ϵ‖ ≥1
k1b
⃦⃦RI
b
(
qd
)
ωd
d
⃦⃦;
(52)
Theorem 1. If Assumptions 1 to 3 are true, all of the 
parameters, k0, k1, k2a, k2b, k3a, k3b, k4, k5, k0, k1a, k1b, 
k2a, k2b, k3a, k3b, γ1, γ2, and λi, i = 1 ∼10 are positive 
and real and the overall Lyapunov function is the 
same as that for a previous study (46). The incre-
mental least squares method is used to train and 
determine the structures and parameters for the 
ORFBLS estimators. Using the control laws of a 
previous study (40) and the online parameter up-
date rules of another (50), the origin of the overall 
closed-loop multiple tilting-quadrotor control sys-
tem is semi-globally uniformly and ultimately 
bounded (SUUB). All error variables, δ1, δ2, δ2a, δ2b, 
δ3a, δ3b, ~ϵ, ~ϵf, δ2a, δ2b, δ3a, δ3b, δ3, ~v and ~ωb also 
converge to the neighborhood of the origin, as 
t→∞.
_̂
W
(2)
αi
T
= −
_~W
(2)
αi
T
= λ7U2i
T ̂
W
(3)
αi
T ∂̂x
(3)
∂̂
W
(2)
αi
; _̂ααi
T = −_~ααi
T = λ8U2i
T ̂
W
(3)T∂̂x
(3)
∂̂ααi
_̂cαi
T = −_~cαi
T = λ9U2i
T ̂
W
(3)T∂̂x(3)
∂̂cαi
; _̂βαi
T
= −_~βαi
T
= λ10U2i
T ̂
W
(3)T∂̂x(3)
∂̂βαi
(50)
_V2 =−k1aδ1
Tδ1−k1b~ϵT~ϵ−~ϵTRI
b
(
qd
)
ωd
d−k2aδ2a
Tδ2a−wSTsgn(S)−k4STS+δ2a
T ~Δaf −δ2a
T _Φ1a−k2bδ2b
Tδ2b
+δ2b
T ~Δατ−δ2b
T _Φ1b+(δ2a+γ1~v)Tha−k7γ2 ~ωbT ~ωb+ 1
λ1
tr
[
~Wa
(o)T( _~Wa
(o)
+λ1xa
(0)Ua
T)]
+ 1
λ2
(
_~W
subaT
+λ2UT
aW(o)T
a
∂̂x
(o)
a
∂̂
W
sub
a
)
~W
sub
a + 1
λ3
(
_̂σaT +λ3UT
a ̂
W
(o)T
a
∂̂x
(o)
a
∂̂σa
)
~σa+ 1
λ4
(
_~caT +λ4UT
aW(o)T
a
∂̂x
(o)
a
∂̂ca
)
~ca
+ 1
λ5
(
_~αaT +λ5UT
aW(o)T
a
∂̂x
(o)
a
∂̂αa
)
~αa+ 1
λ6
trr
[
~W
(o)T
α
( _~W
(o)
α +λ6x(0)
α UT
α
)]
+ 1
λ7
(
_~W
subT
α
T
+λ7UT
αW(o)T
α
∂x(o)
α
∂̂
W
sub
α
)
~W
sub
α
+ 1
λ8
(
_̂σαT +λ8UT
α ̂
W
(o)T
α
∂̂x
(o)
α
∂̂σα
)
~σα+ 1
λ9
(
_~cαT +λ9UT
αW(o)T
α
∂̂x
(o)
α
∂̂cα
)
~cα+ 1
λ10
(
_~αaT +λ10UT
αW(o)T
α
∂̂x
(o)
a
∂̂αα
)
~αα+
(
δ2b+γ2 ~ωb)Tϵα
(49)
JOURNAL OF MARINE SCIENCE AND TECHNOLOGY 2026;34:109—121 
117

## Page 11

5. Simulations and discussion
This section uses three simulations to determine 
the effectiveness, advantages and robustness of a 
fixed-time formation controller that uses ORFBLS- 
ABSMC to address the effects of wind gusts. The 
key parameters for each tilting quadrotor are listed 
in Table II. Simulations use MATLAB/Simulink and 
the fourth-order Runge-Kutta method, using a step 
size of one m/s.
A. Formation Control during Wind Gusts
The first simulation for formation control during 
wind gusts tests the proposed method using more 
specific wind disturbances. Some wind-speed sce-
narios are used to ensure that the proposed method 
applies to winds from a light breeze to the strongest 
winds.
• At a wind speed (u0) of 5 m/s (approximately 
11.2 mph), which is classified as a gentle breeze 
on the Beaufort Scale (3)
• At a wind speed (u0) of 10 m/s (approximately 
22.4 mph), which is classified as a fresh breeze 
on the Beaufort Scale (Level 5)
• At a wind speed (u0) of 20 m/s (approximately 
44.7 mph), which is classified as a super hurri-
cane on the Beaufort Scale (Level 8).
Table III shows the performance indices for the 
formation errors for these three types of wind gusts 
and the results demonstrate the stability of the 
proposed formation control method.
B. Formation Control using a Growing ORFBLS 
Structure
This simulation determines the adaptability and 
performance of the growing ORFBLS structure in 
changing wind conditions. Initially, the ORFBLS 
has 3 nodes in its feature mapping layer (Zf = 3) 
and 3 and 5 nodes in its enhancement layers 
(N1 = 3, H2 = 5). To increase the capability to 
adapt to complex conditions, we added 4 nodes to 
each layer, which doubled its learning and adapt-
ability. Fig. 5 shows the simulation results for 
multiple tilting quadrotors flying in formation and 
tracking a sinusoidal trajectory using the ABSMC 
controller and the augmented ORFBLS at Beaufort 
scale 10. Table IV compares error metrics at 
Beaufort scale wind speeds of 10 and 20. This 
comparison 
demonstrates 
how 
the 
Growing 
ORFBLS imbues greater adaptability to aero-
dynamic disturbances, as evidenced by reduced 
error in the results in Table IV.
C. Formation Control with Airdrops under Wind 
Gusts
This subsection presents the results of the third set 
of simulations to determine the adaptive control 
responses of tilting multi-quadrotors to mass varia-
tions from airdrops in a changing wind environ-
ment. Airdrops present significant stabilization 
challenges due to a sudden release in payload, 
which causes abrupt mass changes. The ORFBLS- 
ABSMC formation controller's performance is 
determined for wind scales of 5 and 10. This corre-
sponds to +30 % and +40 % mass variations. The 
Table III. Performance indices for formation errors during wind gusts.
Wind Speed (m/sec)
Beaufort scale
MSE
ISE
IAE
ITAE
5
3
0.0083
0.6988
3.0048
148.09
10
5
0.0098
0.7200
3.0079
149.04
20
8
0.0108
0.8100
3.0102
153.07
Fig. 5. Simulated results for multiple tilting-quadrotors in formation 
tracking a sinusoidal trajectory using the ABSMC controller with 
ORFBLS: (a) actual (bolder line) and desired (thinner line) paths in 
meters and (b) tracking errors along the x, y, and z axes in meters and 
roll, pitch and yaw in degrees.
Table II. Parameters for the quadcopters for this study.
Parameter
Value
Parameter
Value
J [kg]
0.952
lbeam [m]
0.22
Jx [kg-m2]
0.013215
Imotor [kg-m2]
3:3 × 10−5
Jy [kg-m2]
0.012522
km [N-sec2]
1:3 × 10−5
Jz [kg-m2]
0.023527
b [N-m-sec2]
4:3 × 10−7
118 
JOURNAL OF MARINE SCIENCE AND TECHNOLOGY 2026;34:109—121

## Page 12

results are detailed in Table V. Despite significant 
disturbances, the controller-maintained formation 
accuracy shows minimal errors and efficiently re-
covers from disturbances. The simulation results 
demonstrate that the formation controller addresses 
complexities due to airdrop-induced mass variations 
to maintain stability in a dynamic environment.
6. Experimental results and discussion
This section shows how drone formations manage 
the challenges of wind gusts. To evaluate the pro-
posed formation control method under varying 
wind gust scenarios, an experiment uses three Ryze 
Tello drones. Wind disturbances are generated by 
three fans that are positioned to create vertical and 
horizontal gusts. The first fan operates at a wind 
speed of 5 m/s, the second fan operates at a wind 
speed of 10 m/s, and the third fan operate at 
10—20 m/s. Using the MATLAB support package, 
the drones are flown indoors in a triangular for-
mation. They are initially positioned at the origin 
and remain stationary for the first 7 s, in order to 
stabilize before initiating movement.
The experiment uses varying wind speed condi-
tions to determine the formation control method's 
effectiveness 
under 
different 
environmental 
stresses. The drones follow a linear trajectory in the 
x-y-z plane and maintain a constant altitude until 
the 50th second, as shown in Fig. 6. This setup en-
sures realistic wind conditions to accurately eval-
uate the control method. The overall performance 
of the drones is assessed to demonstrate the ability 
of the proposed method to maintain formation 
integrity. Fig. 7 shows the real-time trajectory and 
error tracking. The results show the drones' 
robustness to wind gusts.
Table IV. Increasing control performance metrics using growing 
ORFBLS.
Performance Index Wind 
Speed 
(m/sec)
MSE
ISE
IAE
ITAE
Without growing 
ORFBLS
10
0.3285
22.9951
39.5314
1815.70
20
0.3645
24.9871
43.406
2027.50
With growing 
ORFBLS
10
0.0098
0.7200
3.0079
149.04
20
0.0135
1.1994
2.8214
173.351
Improvement
10
97.1 % 96.87 % 92.39 % 91.79 %
20
96.3 % 95.2 %
93.5 %
91.45 %
Table V. Formation errors for two cases of airdrops during Wind Gusts.
Wind Scale
Airdrop Mass Variation
Control method
Formation Error (m)
Recovery Time (s)
05
+30 %
ORFBLS-ABSMC
0.2
3.5
10
+40 %
ORFBLS-ABSMC
0.4
5.0
Fig. 6. Experimental formation setup for Ryze Tello drones in a windy 
environment.
Fig. 7. Experimental results for the three Ryze Tello Drones in for-
mation during Wind Gusts: (a) Formation and trajectory Tracking 
results and (b) Tracking Errors.
JOURNAL OF MARINE SCIENCE AND TECHNOLOGY 2026;34:109—121 
119

## Page 13

The results show that the drones maintain for-
mation integrity with varying degrees of error, 
depending on the wind speed. At low wind speeds, 
the drones maintain a tight formation with minimal 
errors. As the wind speed increases, the formation 
exhibits more significant errors but remains intact, 
so the system is stable in moderate to severe 
disturbances. The control system is robust and 
maintains formation integrity under challenging 
conditions.
This experiment demonstrates the reliability and 
precision of the control systems for this study, 
which maintain formation integrity under varying 
wind conditions. The results show the effectiveness 
of the proposed formation control method in real- 
world scenarios. The system maintains stable and 
precise drone formations under significant envi-
ronmental changes.
7. Limitations of the proposed method
The proposed ORFBLS-ABSMC controller is robust 
for a small-to-medium quadrotor formations but has 
limitations. Scalability to larger formations incurs 
increased communication delays, synchronization 
issues and increased computational demands, which 
affect formation integrity. The method's sensitivity to 
parameter tuning, including gains and thresholds, 
means that adjustment is necessary to ensure stability 
and efficiency. Practical implementation is also 
limited by hardware constraints, such as sensor ac-
curacy and onboard computational power.
Environmental factors, such as unmodeled tur-
bulence or extreme weather, impact system per-
formance 
despite 
validation 
against 
wind 
disturbances. The system's adaptability to broader 
or unpredictable mass variations, beyond the tested 
scenarios, requires further study. Real-time imple-
mentation in dynamic outdoor environments, such 
as maritime or urban settings, may also introduce 
complexities. This method is designed for homo-
geneous formations and its application to hetero-
geneous systems, such as a mixture of aerial and 
autonomous underwater vehicles or ground robots, 
is a subject for future study.
8. Conclusions and future work
This paper demonstrates a fixed-time formation 
control method that uses an output recurrent fuzzy 
broad learning system (ORFBLS) with adaptive 
backstepping sliding-mode control (ABSMC) to 
overcome wind disturbances for a tilting multi- 
quadrotor systems. The incremental least squares 
method and Lyapunov stability theory are robust 
and ensure fixed-time convergence and consistent 
performance during wind disturbance. The method 
includes a “growing ORFBLS structure” that 
dynamically adapts to increase system performance 
and flexibility. The strategy is adaptable and robust 
in simulations that use cooperative tilting quad-
rotors and is a new control paradigm for autono-
mous aerial vehicles in uncertain environments.
The results of this study are relevant to marine 
applications, where robust and adaptive control 
systems are crucial for tasks such as marine sur-
veillance, environmental monitoring and search 
and rescue operations. By ensuring stable and 
precise formation control under dynamic condi-
tions, the method that is proposed by this study 
allows resilient and sustainable operations for ma-
rine-related science and technology. However, the 
method has limitations in terms of its scalability to 
larger formations, sensitivity to parameter tuning 
and hardware constraints, which affect real-world 
implementation. Environmental factors, such as 
sudden turbulence and unmodeled dynamics, and 
adaptability to broader or unpredictable mass var-
iations, are worthy of further study.
To address these limitations, future studies might 
develop adaptive tuning mechanisms to reduce 
sensitivity to parameter adjustments and ensure 
consistent performance across varying conditions. 
Optimizing communication protocols and distrib-
uted control strategies will allow scalability to 
larger formations. Validating the proposed method 
in real-world scenarios, particularly under diverse 
environmental conditions, will further demonstrate 
its robustness and practicality.
Integration with heterogeneous systems, such as 
autonomous underwater vehicles (AUVs) and sur-
face vessels, will enable collaborative operations in 
complex environments. Advanced experimental 
setups would also verify the system's performance 
under dynamic outdoor scenarios, including urban 
and maritime settings, to refine and extend its 
applicability. These strategies would increase the 
proposed control strategy's reliability, scalability 
and adaptability and increase its effectiveness in 
aerial and marine applications.
Ethics information
No animal or human experiments were conduct-
ed in this study.
Conflict of interest
The authors declare that there are no conflicts of 
interest regarding the publication of this paper.
120 
JOURNAL OF MARINE SCIENCE AND TECHNOLOGY 2026;34:109—121

## Page 14

Acknowledgements
The authors gratefully acknowledge the financial 
support of the National Science and Technology 
(NSTC), Taiwan, ROC, under contract NSTC 112- 
2622-8-005-005-TE1. 
References
[1] Murray R. Recent research in cooperative control of multi-
vehicle systems. J Dyn Syst Meas Control 2007;129:571—83.
[2] Tsai CC, Chen HY, Chan CC, Chen SC, Chen GM. Intelli-
gent actor-critic learning control for collision-free trajectory 
tracking of Mecanum-wheeled mobile robots. Int J Fuzzy 
Syst 2024;26(4):1133—42.
[3] Lin CK. H∞ reinforcement learning control of robot ma-
nipulators using fuzzy wavelet networks. Fuzzy Set Syst 
2009;160(12):1765—86.
[4] Ren W, et al. Information consensus in multivehicle coop-
erative Control. IEEE Control Syst Mag 2007;27(2):71—82.
[5] Zhang Y, Yi P, Hong Y. Cooperative safe trajectory planning 
for quadrotor swarms. Sensors 2024;24(2):707.
[6] Mwaffo V. Formation control and collision avoidance of 
unmanned water surface vehicles in maritime environ-
ments. J Franklin Inst 2024;361(7):106791.
[7] Tsai CC, Tai FC, Wang YC. Global localization using dead- 
reckoning and Kinect sensors for robots with omnidirec-
tional Mecanum wheels. J Mar Sci Technol 2014;22(3):6.
[8] Chen CLP, Liu Z. Broad learning system: an effective and 
efficient incremental learning system without the need for 
deep architecture. IEEE Transact Neural Networks Learn 
Syst 2018;29(1):10—24.
[9] Feng S, Chen CLP. Broad learning system for control of 
nonlinear dynamic systems. Proc. 2018 IEEE International 
Conference on Systems, Man, and Cybernetics. 2018. 
p. 2230—5.
[10] Feng S, Chen CLP. Fuzzy broad learning system: a novel 
neuro-fuzzy model for regression and classification. IEEE 
Trans Cybern 2020;50(2):414—24.
[11] Chen HS, Tsai CC, Tai FC. Adaptive model predictive 
control using iterative fuzzy broad learning system for 
nonlinear digital time-delay dynamics system. In: Proc. of 
2020 Intern. Conf. Fuzzy Theory and its Applications 
(iFuzzy2020); 2020. Hsinchu, Taiwan.
[12] Tsai CC, Chan C-C, Li Y-C, Tai F-C. Intelligent adaptive PID 
control using fuzzy broad learning system: an application to 
tool-grinding servo control systems. Int J Fuzzy Syst 2020; 
22(7):2149—62.
[13] Li YC. Intelligent auto-tuning of PID controllers using fuzzy 
broad learning system for tool-grinding servo control sys-
tems, Master Thesis, Department of Electrical Engineering. 
National Chung Hsing University; 2019.
[14] Chou CY. Intelligent adaptive PID temperature control 
using recurrent fuzzy broad learning systems: an applica-
tion to chemical heating process in a wafer cleaning ma-
chine, 
Master 
Thesis, 
Department 
of 
Electrical 
Engineering. Taichung, Taiwan: National Chung Hsing 
University; 2020.
[15] Chen CL, Liu PZ, Feng S. Universal approximation capa-
bility of broad learning system and its structural variations. 
IEEE Transact Neural Networks Learn Syst 2019;30(4): 
1191—204.
[16] Kuo C-W, Tsai CC. Quaternion-based adaptive back-
stepping FBLS formation control for networked multiple 
tilting quadrotors with uncertainties. In: Proc. of ARIS 2019, 
Taipei, Taiwan; 2019. 43-43.
[17] Hussain A, Tsai CC, Kuo CW, Mao CF. Improved quater-
nion-based adaptive backstepping formation control using 
RFBLS for uncertain networked multiple tilting quadrotors. 
In: Proc. of 2022 Intern. Conf. on Fuzzy Theory and its Ap-
plications (iFuzzy 2022), Golden Valla, Kaohsiung, Taiwan; 
2022.
[18] Wang K, Yan X, Yuan Y, Li F. Real-time optimization of ship 
energy efficiency based on the prediction technology of 
working condition. Transport Res Transport Environ 2016; 
46:81—93.
[19] Chen CLP, Liu Z. Broad learning system: an effective and 
efficient incremental learning system without the need for 
deep architecture. IEEE Trans Neural Network Learn Sys 
Jan. 2018;29(1):10—24.
JOURNAL OF MARINE SCIENCE AND TECHNOLOGY 2026;34:109—121 
121
