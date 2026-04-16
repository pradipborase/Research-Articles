# robust-formation-control-of-quadrotor-uavs-a-fully-actuated-control-approach.pdf

## Page 1

Robust Formation Control of Quadrotor UAVs: A Fully-Actuated
Control Approach
Zhihao Liu
*, Peng Li
†
School of Mechanical Engineering and Automation
Harbin Institute of Technology (Shenzhen) 518055, P. R. China
In this work, a fully actuated system (FAS) control scheme for the quadrotor UAV formation is designed. Deploying the FAS techniques,
two controllers are designed for position and angle tracking so that the UAV formation is driven along the given trajectory with enhanced
internal stability. Considering the scenario where the environment disturbances and actuator faults aﬀect UAV systems, an extended state
observer (ESO) is designed to estimate the uncertainty. Subsequently, the eﬀect of the fault and uncertainty is compensated in the FAS
controller to enhance the accuracy. As a result, the proposed formation coordination controller ensures that the UAV team completes the
desired ﬂight mission. According to the simulation results, the proposed method is more accurate and robust against the disturbance and
fault with the accurate estimation compared with traditional methods.
Keywords: Quadrotor UAV formation; fully actuated system control; fault identiﬁcation; extended state observer.
1.
Introduction
Quadrotor unmanned aerial vehicle (UAV) has been widely
used in military and civilian ﬁelds. Multi-UAV formation
control is a fundamental research topic in the ﬁeld of UAV
collaborative control. Presently, the control approaches of
UAV formation mainly include the leader–follower method
[1], the virtual structure method [2], the behavior-based
method [3], and the artiﬁcial potential ﬁeld method [4].
Additionally, drones may be aﬀected by external environ-
mental disturbances or internal component faults while
performing tasks. Therefore, it is of practical signiﬁcance to
consider both external environmental disturbances and
actuator faults in UAV formation problems. In [5], the high-
order consistency theory is applied in UAV formation ﬂight
control strategy, simplifying the nonlinear mathematical
model of the quadrotor UAV. In [6, 7], the control algo-
rithms of UAV time-varying formation are designed based
on consistency theory and are veriﬁed on a quadrotor
hardware platform. The consensus formation has been ex-
tensively studied. However, during maintaining formation,
there is still a large gain convergence oscillation in the
linear consensus algorithm. A case of follower UAV actuator
faults are is considered in [8] and the authors proposed a
distributed fault-tolerant formation control strategy based
on the virtual leader. A distributed fault-tolerant formation
control strategy based on adaptive sliding mode was pro-
posed in [9] to achieve rapid formation recovery in the
event of UAV fault. In [10], a disturbance observer was
designed to address the modeling coupling factors and ex-
ternal environmental disturbances to achieve formation
stability. However, the above literature did not consider
both UAV failures and the external environmental dis-
turbances simultaneously.
In recent years, the fully actuated system technique [11]
has introduced a new theoretical approach for the control
ﬁeld, characterized by its high convergence rate and simple
parameter design. A trajectory tracking controller based on
a second-order fully-actuated system model for a six-de-
gree-of freedom manipulator with uncertainties is designed
in [12]. In [13], an attitude control of a ﬂexible aerocraft is
transformed into a problem of time-varying nonlinear con-
trol through fully actuated system technique. Furthermore, a
Received 23 July 2024; Accepted 27 November 2024; Published 22 January
2025. This paper was recommended for publication in its revised form by
editorial board member, Shiyu Zhao.
Email Addresses: *liuzhihaotina@163.com, †lipeng2020@hit.edu.cn
†Corresponding author.
Unmanned Systems, Vol. 14, No. 1 (2026) 227–238
#.c World Scientiﬁc Publishing Company
DOI: 10.1142/S2301385025500918
227
Un. Sys. 2026.14:227-238. Downloaded from www.worldscientific.com
by NETAJI SUBHAS INSTITUTE OF TECHOLOGY on 03/15/26. Re-use and distribution is strictly not permitted, except for Open Access articles.

## Page 2

fully auactuated system model for the six degree-of-freedom
spacecraft motion is derived and a tracking controller based
on FAS approach is designed in [14]. However, few designed
the FAS controllers for UAV formation considering external
disturbances and actuator faults simultaneously. Therefore,
combined with the leader–follower formation control strat-
egy, this paper designs a fully actuated system control ap-
proach based on the expanded state observer to ensure
robust control of UAV formation. There exist some problems
using traditional methods. For example, the sliding mode
control has ﬂuctuation; the adaptive control may not guar-
antee global stability; the linear consensus algorithm leaves a
large gain convergence oscillation. Fortunately, the FAS al-
gorithm has no such problems. Liu and Li [15] has proofed
that FAS converges faster than SMC with less steady-state
error. However, it requires accurate knowledge of system
dynamics resulting in that it is not robust to large uncertainty
[14]. Thus one can combine some techniques such as the
extend state observer to estimate and compensate the un-
certainty for better control performance.
The main contributions of this paper are as follows:
(1) The under actuated UAV system with coupled terms is
transformed into a fully actuated one through the fully
actuated theorem, obtaining the direct input and solv-
ing the actual input according to the dynamics. The
proposed scheme ensures the stable convergence and
simpliﬁes the design of the controller.
(2) The combination of the FAS controller and the ESO
enhances the internal stability and robustness, as veri-
ﬁed by extensive numerical experiments.
(3) Compared with other traditional methods, the proposed
has a simpler form, less ﬂuctuation, and a higher con-
vergence rate, with guaranteed global convergence.
The rest of this paper is arranged as follows: Sec. 2
establishes a dynamic model of the UAV with external dis-
turbances and actuator faults and introduces the fully actu-
ated system theory. Section 3 discusses controller and extend
state observer designs for position and attitude layers with
the robustness analysis and stability proof. Speciﬁc examples
are given in Sec. 4 for simulation veriﬁcation. Section 5
summarizes the results and proposes further research
directions.
2.
Preliminaries
2.1.
Dynamic model of UAV
Suppose the quadcopter drone is a rigid body with the
geometric center consistent with the center of mass.
The UAV dynamic coordinate system model is shown in
Fig. 2. The roll angular , the pitch angular , and the yaw
angular  denote the rotation angles around the xb, yb, and
zb axes, respectively, which normally range within ð 
2 ; 
2Þ.
As in Fig. 1, kðk 2 ½1; 4Þ represents the combined thrust or
force provided by the kth motor. They can be combined into
four moments as [16]
U1;i ¼ 1 þ 2 þ 3 þ 4;
U2;i ¼ 2 þ 4;
U3;i ¼ 1 þ 3;
U4;i ¼ 1 þ 2  3 þ 4;
where U1;i represents the lift force of the ith UAV; Ur;i ðr 2
½2; 4Þ represents the roll, pitch or yaw force, respectively.
The control input of the ith quadcopter drone under
actuator fault is as follows:
Ura;i ¼ Ur;i þ fr;i;
ðr ¼ 1; 2; 3; 4Þ;
where r represents the torques with r ¼ 1 for the lift one
and r ¼ 2; 3; 4 for the attitudes ones; Ura;i is the actual
control input; Ur;i is the designed input; fr;i is the deviation
failure factor of the rth combined moment, and actuator
fault occurs when fr;i 6¼ 0.
Consider a multi-UAV system consists of NðN > 1Þ
UAVs with each one being aﬀected by environmental
disturbance and actuator fault. The dynamics of the ith
Fig. 1.
Four rotor propellers.
Fig. 2.
Coordinate system of the quadrotor.
228
Z. Liu & P. Li
Un. Sys. 2026.14:227-238. Downloaded from www.worldscientific.com
by NETAJI SUBHAS INSTITUTE OF TECHOLOGY on 03/15/26. Re-use and distribution is strictly not permitted, except for Open Access articles.

## Page 3

UAV [17] is expressed as
€xi ¼ cos i sin i cos  i þ sin i sin  i
mi
U1a;i
 kx;i
mi
x:
i þ dx;i;
€yi ¼ cos i sin i sin  i  sin i cos  i
mi
U1a;i
 ky;i
mi
y:
i þ dy;i;
z
::
i ¼ cos i cos i
mi
U1a;i  g  kz;i
mi
z:
i þ dz;i;

::
i ¼ Jy;i  Jz;i
Jx;i

:
i 
:
i þ U2a;i
Jx;i
di  k;i
Jx;i

:
i þ d;i;

::
i ¼ Jz;i  Jx;i
Jy;i

:
i 
:
i þ U3a;i
Jy;i
di  k;i
Jy;i

:
i þ d;i;
 
::
i ¼ Jx;i  Jy;i
Jz;i

:
i
:
i þ U4a;i
Jz;i
 k ;i
Jz;i
 
:
i þ d ;i;
8
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
<
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
:
ð1Þ
where xi, yi and zi are the positions of the ith UAV in the
inertial coordinate system; i, i and  i are the attitude
angles. Jx;i, Jy;i and Jz;i are the moments of inertia around
x-, y- and z-axes; g is the acceleration due to gravity; kx;i,
ky;i and kz;i are the air resistance coeﬃcients; k;i, k;i and
k ;i are aerodynamic drag coeﬃcients; dk;iðk ¼ x; y; z; ; ;
 Þ is environmental disturbance; di is the distance be-
tween the center of the ith drone and the center of its
rotor; mi is the mass of the ith UAV.
For convenience, we deﬁne the disturbance and fault
vectors in position and attitude layers as
¾p;i ¼
bx;if1;i þ dx;i
by;if1;i þ dy;i
bz;if1;i þ dz;i
2
64
3
75;
¾a;i ¼
b;if2;i þ d;i
b;if3;i þ d;i
b ;if4;i þ d ;i
2
64
3
75;
with
bx;i
by;i
bz;i
b;i
b;i
b ;i
2
66666664
3
77777775
¼
cos i sin i cos  i þ sin i sin  i
mi
cos i sin i sin  i  sin i cos  i
mi
cos i cos i
mi
di=Jx;i
di=Jy;i
1=Jz;i
2
6666666666666664
3
7777777777777775
:
We assume that the total uncertainty with disturbance and
fault is a bounded slow variable function and satisﬁes
limt!1 ¾:
p;iðtÞ ¼ 0 and limt!1 ¾:
a;iðtÞ ¼ 0 [18]. The large
and unbounded situation will be include in future work.
2.2.
Fully actuated system theory
Consider a second-order dynamic system
E€x ¼ f ðx; x:; tÞ þ Bðx; x:; tÞu;
ð2Þ
where E 2 Rnn is a matrix of constants that can be singu-
lar; x 2 Rn1 is the state of the system; f ðx; x:; tÞ 2 Rn1 is a
continuous vector function of state variables, their deriva-
tives and time; Bðx; x:; tÞ 2 Rnn is the matrix of coeﬃcients;
u 2 Rn1 is the control input. If the control distribution
matrix B satisﬁes
det Bðx; x:; tÞ 6¼ 0;
8 x; x: 2 Rn1; t  0;
then the system (2) is fully actuated. The following linear
and constant closed-loop system is obtained
E€x þ A1x: þ A0x ¼ v;
through selecting suitable constant matrices A1, A2 2 Rnn,
which produces the control law as
u ¼ B1ðA1x: þ A0x þ f  vÞ;
where v 2 Rn1 is the designed input of the closed-loop
system. Especially, let E ¼ In and v ¼ 0n1. Then the system
(2) is transformed into
€x ¼ A1x:  A0x:
Deﬁne z1 ¼ x, z2 ¼ x:. The target system is
z: ¼
z:
1
z:
2
"
#
¼
0
I
A0
A1


z1
z2


¼ Az:
ð3Þ
Select A1 and A0 properly so that the matrix A in (3) can be
Hurwitz. Then the system is stable consequently, which
means that one can expect that the states of (3) converge to
zero ﬁnally.
It is worth noting that there is diﬀerence between FAS
control and the feedback linearization control, since the FAS
approach directly designs parameters for the whole high-
order systems while the feedback linearization just designs
for the derivatives of the states. Although, for ﬁrst-order
system, they are the same. For second-order and higher
systems, the feedback linearization cannot ensure both the
states and their derivatives converge to zero while FAS can
according to Hurwitz criterion. For instance, considering a
second-order system as in (2), the following system can be
obtained through feedback linearization:
E€x0 ¼ Cx: 0;
Robust Formation Control of Quadrotor UAVs: A Fully-Actuated Control Approach
229
Un. Sys. 2026.14:227-238. Downloaded from www.worldscientific.com
by NETAJI SUBHAS INSTITUTE OF TECHOLOGY on 03/15/26. Re-use and distribution is strictly not permitted, except for Open Access articles.

## Page 4

where C is a constant matrix to be designed. Then one can
only conclude that x: 0 and €x0 will converge to zero, however
without the convergence guarantee of x0, since the target
system is
z: 0 ¼
z: 0
1
z: 0
2
"
#
¼
0
I
0
C

 z 0
1
z0
2


¼ A0z0;
where z0
1 ¼ x0, z0
2 ¼ x: 0; the matrix A0 cannot be Hurwitz as
detðA0Þ ¼ 0. This may cause the error accumulation on x0.
High-order fully actuated system approach can avoid the
problem since it guarantees the convergences of x, x: and €x
as in (3).
Moreover, the parameter design through FAS approach
is more ﬂexible and intuitive. However, FAS technique re-
quired accurate knowledge of system dynamics. Although it
is robust to small modeling errors, it is not suitable for large
uncertainty, for example, in the scenario where it lacks the
knowledge of system model. Consequently the closed-loop
system will be aﬀected by the uncertainty. On the other
hand, a disturbance observer can be instrumental in en-
hancing the closed-loop control performance.
Notations: k  k deﬁnes the norm of vectors; 0 repre-
sents zero matrix; I is identity matrix; and min and max
represent the largest and smallest eigenvalues of one ma-
trix, respectively.
3.
Main Results
The formation control problem is transformed into a ve-
locity and trajectory tracking problem under a leader–fol-
lower framework. One virtual leader is considered to
provide the given trajectory. Then one UAV follows it and
rest of each UAV has one corresponding leader. That is, each
UAV may have multiple followers but only follows one
leader itself. As shown in Fig. 3, for each pair of leader–
follower-, set a stationary relative position oﬀset ½Δxij; Δyij;
Δzij to obtain the desired formation.
We make some assumptions about the leader–follower
system:
(1) There is no communication delay between the leader
and follower.
(2) Each robot can detect its own pose, velocity and ac-
celeration.
(3) The leader can transmit its information mentioned
above to each of its followers through communication.
The formation goal is to obtain trajectory consistency.
Firstly, the desired trajectory of the whole UAV team is from
one virtual leader following a given trajectory. Then the
team follows the trajectory according to the leader–follower
strategy. The control inputs are the four torques Urðr 2
½1; 4Þ of UAV determining the position and attitude of each
drone.
Regarding the strong coupled dynamics as in (1), the
position layer and the attitude layer cannot be combined
into an overall second-order model to design the control
law [16]. Therefore, the control is considered in position
and attitude layers, respectively. Also the ESOs are designed
for position and attitude control, respectively. In general,
the attitude changes slowly and moderately, so that the
eﬀects of the angle variation on position control can be
reasonably ignored. The position control torque U1;i is
obtained based on FAS under the leader–follower tracking
framework. And the ESO is proposed to estimate the eﬀects
of actuator fault and the disturbance, so that it can be
compensated in the controller. Based on the dynamics
model (1), the desired attitude angles can be uniquely de-
termined with U1;i solved and compensation term ^¾a;i by
ESO. Then with the desired attitudes, we design the direct
inputs in attitude control layer deploying FAS technique
and obtain the control torques Ur;iðr 2 ½2; 4Þ according to
(1). With the four torques solved, UAVs’ position and
attitude can be maneuvered. The uncertainties caused by
disturbance and fault are estimated and compensated
through ESO that guarantees the robustness of the system.
The ﬂowchart of the algorithm applied is Fig. 4.
3.1.
Position control
Consider the ith UAV and its leader-the jth UAV. Deﬁne the
position error ep;i and the vector zp;i as
ep;i ¼
xi  xj  Δxij
yi  yj  Δyij
zi  zj  Δzij
2
4
3
5;
zp;i ¼
ep;i
e:
p;i
"
#
:
Fig. 3.
The relative kinematics of the leader–follower.
230
Z. Liu & P. Li
Un. Sys. 2026.14:227-238. Downloaded from www.worldscientific.com
by NETAJI SUBHAS INSTITUTE OF TECHOLOGY on 03/15/26. Re-use and distribution is strictly not permitted, except for Open Access articles.

## Page 5

The second derivative of position error system is
e
::
p;i ¼ ai  aj þ ¾p;i;
ð4Þ
where ai and aj are the theoretical linear accelerations of
the ith UAV and jth UAV, respectively. As in (4), the coeﬃ-
cient matrix of ai is identity matrix whose determinant is
1 6¼ 0. Therefore, the system (4) is fully actuated. The error
dynamics can be expressed as
z:
p;i ¼
e:
p;i
e
::
p;i
"
#
¼
x:
i  x:
j
y:
i  y:
j
z:
i  z:
j
€xi  €xj
€yi  €yj
z
::
i  z
::
j
2
6666666664
3
7777777775
¼
vi  vj
ai  aj


þ
0
¾p;i


;
ð5Þ
where vi and vj are the linear velocities of the ith UAV and
jth UAV, respectively. The total uncertainty term ¾p;i is
estimated through ESO as follows.
For position control layer, deﬁne the variables as
º1;i ¼ ½xi
yi
ziT;
º2;i ¼ ½x:
i
y:
i
z:
iT;
º3;i ¼ ¾p;i 
kx;i
ky;i
kz;i
2
64
3
75º2;i=mi 
0
0
g
2
4
3
5:
ð6Þ
where º3;i ¼ ½€xi
€yi
z
::
iT  ½bx;i
by;i
bz;iTU1;i is the sum
of the uncertainty and the known resistance. The state
equation of position layer can be obtained from (1)
º:
1;i ¼ º2;i;
º:
2;i ¼
bx;i
by;i
bz;i
2
64
3
75U1;i þ º3;i;
º:
3;i ¼ ½p;i;
8
>
>
>
>
>
>
<
>
>
>
>
>
>
:
where ½p;i is the derivative of º3;i. Let the input be
º1;i ¼ ½xi; yi; ziT. Deﬁne the following extended state ob-
server:
^º
:
1;i ¼ ^º2;i þ 1;i
"i
ðº1;i  ^º1;iÞ;
^º
:
2;i ¼
bx;i
by;i
bz;i
2
64
3
75U1;i þ ^º3;i þ 2;i
"2
i
ðº1;i  ^º1;iÞ;
^º
:
3;i ¼ 3;i
" 3
i
ðº1;i  ^º1;iÞ;
8
>
>
>
>
>
>
>
>
>
<
>
>
>
>
>
>
>
>
>
:
where ^º1;i, ^º2;i and ^º3;i are the estimates of position state
variables xi; yi; zi, their derivatives and the uncertainty term
º3;i, respectively; k;iðk ¼ 1; 2; 3Þ and "i are predetermined
positive constants.
Lemma 3.1. For a single-input linear system X
: ¼ AX þ BU,
if A is a Hurwitz matrix and U satisﬁes limt!1 UðtÞ ¼ 0, then
the system is asymptotic stable [19].
The error states and its dynamics follow that
&:
p;i ¼
^º
:
1;i  º:
1;i
^º
:
2;i  º:
2;i
^º
:
3;i  º:
3;i
2
6664
3
7775 ¼
 1;i
"i
I
I
0
 2;i
"2
i
I
0
I
 3;i
"3
i
I
0
0
2
66666664
3
77777775
&p;i þ
0
0
I
2
64
3
75½p;i
¼ Gp;i&p;i þ Hp;i½p;i;
ð7Þ
where
Gp;i ¼
 1;i
"i
I
I
0
 2;i
"2
i
I
0
I
 3;i
"3
i
I
0
0
2
66666664
3
77777775
;
&p;i ¼
^º1;i  º1;i
^º2;i  º2;i
^º3;i  º3;i
2
64
3
75;
Hp;i ¼
0
0
I
2
64
3
75:
Fig. 4.
The ﬂowchart of this work.
Robust Formation Control of Quadrotor UAVs: A Fully-Actuated Control Approach
231
Un. Sys. 2026.14:227-238. Downloaded from www.worldscientific.com
by NETAJI SUBHAS INSTITUTE OF TECHOLOGY on 03/15/26. Re-use and distribution is strictly not permitted, except for Open Access articles.

## Page 6

Assumption 3.2. The uncertainty term º3;i is a bounded
slowly-varying variable function and satisﬁes limt!1 º:
3;iðtÞ
¼ limt!1 ½p;iðtÞ ¼ 0 [18].
By choosing the parameters 1;i, 2;i, 3;i and "i appro-
priately, one can make the matrix Gp;i Hurwitz. Then based on
Lemma 3.1 and Assumption 3.2, the extended state observer
asymptotically converges to its true value, which guarantees
lim
t!1 ^º3;i ¼ º3;i:
ð8Þ
Then according to (6), the observed value and the known
dynamics, the acceleration compensation term is
^¾p;i ¼ ^º3;i þ
kx;i
ky;i
kz;i
2
64
3
75º2;i=mi;
directly using the original value º2;i ¼ ½x:
i; y:
i; z:
iT since it is
known by UAV itself according to our previous assumptions.
Therefore with (8), deﬁne ±p;i ¼ ¾p;i  ^¾p;i as the observe
error vector. It satisﬁes
lim
t!1 k±p;ik ¼ 0:
ð9Þ
With the estimation from ESO, choose two suitable ma-
trices A0, A1 2 R33 and design the linear acceleration as
ai ¼ aj  A1e:
p;i  A0ep;i  ^¾p;i:
ð10Þ
The system (5) is transformed into
z:
p;i ¼
0
I
A0
A1

 ep;i
e:
p;i
"
#
þ
0
±p;i


;
ð11Þ
where the coeﬃcient matrix can be Hurwitz by suitably
choosing A0 and A1. According to dynamics (1), the linear
acceleration ai satisﬁes the constraint that
ai ¼
cos i sin i cos  i þ sin i sin  i
mi
U1a;i
 kx;i
mi
x:
i þ dx;i
cos i sin i sin  i  sin i cos  i
mi
U1a;i
 ky;i
m y:
i þ dy;i
cos i cos i
mi
U1a;i  g  kz;i
m z:
i þ dz;i
2
66666666666666664
3
77777777777777775
:
Thus the torque U1;i is calculated as
U1;i ¼ mi ai  ^¾p;i þ kx;i
mi
x:
i; ky;i
m y:
i; g þ kz;i
m z:
i

T

2
:
ð12Þ
With U1;i solved, the actual linear acceleration ½€xi; €yi; z
::
iT
can be calculated based on the dynamics model (1).
3.2.
Attitude control
With U1;i solved, the desired angles are calculated from the
following equations according to (1):
cos d;i sin d;i cos  d;i þ sin d;i sin  d;i
¼ mi
U1;i
aið1Þ þ kx;i
mi
x:
i  ^¾p;ið1Þ


;
cos d;i sin d;i sin  d;i  sin d;i cos  d;i
¼ mi
U1;i
aið2Þ þ ky;i
mi
y:
i  ^¾p;ið2Þ


;
cos d;i cos d;i
¼ mi
U1;i
aið3Þ þ g þ kz;i
mi
z:
i  ^¾p;ið3Þ


:
8
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
<
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
:
ð13Þ
Change U1;i into an extremely small value if U1;i ¼ 0, which
is normally uncommon though.
Deﬁne the attitude error ea;i and the vector za;i as
ea;i ¼
i  d;i
i  d;i
 i   d;i
2
4
3
5;
za;i ¼
ea;i
e:
a;i
"
#
;
whose derivative writes
z:
a;i ¼
e:
a;i
e
::
a;i
"
#
¼

:
i  
:
d;i

:
i  
:
d;i
 
:
i   
:
d;i

::
i  
::
d;i

::
i  
::
d;i
 
::
i   
::
d;i
2
666666666664
3
777777777775
¼
wi  wd;i
hi  hd;i


þ
0
¾a;i


;
ð14Þ
where wi and hi are the angular velocity and acceleration of
the ith UAV, respectively.
Remark 3.3. The changes in attitude angles of UAV are
slowly-varying functions during the ﬂight [20].
From Remark 3.3, wd;i and hd;i are approximately 0.
Then (14) approximately equals to
z:
a;i ¼
e:
a;i
e
::
a;i
"
#

wi
hi


þ
0
¾a;i


:
ð15Þ
232
Z. Liu & P. Li
Un. Sys. 2026.14:227-238. Downloaded from www.worldscientific.com
by NETAJI SUBHAS INSTITUTE OF TECHOLOGY on 03/15/26. Re-use and distribution is strictly not permitted, except for Open Access articles.

## Page 7

Similarly, the total uncertainty term ¾a;i is estimated
through ESO as follows.
For attitude control layer, deﬁne the observed states as
v1;i ¼ ½i
i
 iT;
v2;i ¼ ½
:
i

:
i
 
:
iT;
v3;i ¼ ¾a;i þ
Jy;i  Jz;i
Jx;i

:
i 
:
i  k;i
Jx;i

:
i
Jz;i  Jx;i
Jy;i

:
i 
:
i  k;i
Jy;i

:
i
Jx;i  Jy;i
Jz;i

:
i
:
i  k ;i
Jz;i
 
:
i
2
66666664
3
77777775
:
ð16Þ
The state equation of attitude layer can be obtained
from (1):
v:
1;i ¼ v2;i;
v:
2;i ¼
b;iU2;i
b;iU3;i
b ;iU4;i
2
64
3
75 þ v3;i;
v:
3;i ¼ ½a;i;
8
>
>
>
>
>
>
<
>
>
>
>
>
>
:
where ½a;i is the derivative of the uncertainty term in-
cluding the known dynamics for the attitude layer. Let the
input be v1;i ¼ ½i; i;  iT. Deﬁne the following extended
state observer:
^v
:
1;i ¼ ^v2;i þ 1;i
"i
ðv1;i  ^v1;iÞ;
^v
:
2;i ¼
b;iU2;i
b;iU3;i
b ;iU4;i
2
64
3
75 þ ^v3;i þ 2;i
"2
i
ðv1;i  ^v1;iÞ;
^v
:
3;i ¼ 3;i
"3
i
ðv1;i  ^v1;iÞ;
8
>
>
>
>
>
>
>
>
>
<
>
>
>
>
>
>
>
>
>
:
where ^v1;i, ^v2;i and ^v3;i are the estimates of attitude state
variables i; i;  i, their derivatives and the uncertainty
term v3;i, respectively; k;iðk ¼ 1; 2; 3Þ and "i are the same
as those of position layer.
The attitude error states and its dynamics follow that
&:
a;i ¼
^v
:
1;i  v:
1;i
^v
:
2;i  v:
2;i
^v
:
3;i  v:
3;i
2
6664
3
7775 ¼
 1;i
"i
I
I
0
 2;i
"2
i
I
0
I
 3;i
"3
i
I
0
0
2
66666664
3
77777775
&a;i þ
0
0
I
2
64
3
75½a;i
¼ Ga;i&a;i þ Ha;i½a;i;
ð17Þ
where
Ga;i ¼
 1;i
"i
I
I
0
 2;i
"2
i
I
0
I
 3;i
"3
i
I
0
0
2
66666664
3
77777775
;
&a;i ¼
^v1;i  v1;i
^v2;i  v2;i
^v3;i  v3;i
2
64
3
75;
Ha;i ¼
0
0
I
2
64
3
75:
The matrix Ga;i can also be Hurwitz through suitably
choosing the parameters 1;i, 2;i, 3;i and "i. Then based on
Lemma 3.1 and Assumption 3.2, the extended state ob-
server asymptotically converges to its true value, which
guarantees
lim
t!1 ^v3;i ¼ v3;i:
ð18Þ
Then according to (16), the observed value and the known
dynamics, the compensation term is
^¾a;i ¼ ^v3;i 
Jy;i  Jz;i
Jx;i

:
i 
:
i  k;i
Jx;i

:
i
Jz;i  Jx;i
Jy;i

:
i 
:
i  k;i
Jy;i

:
i
Jx;i  Jy;i
Jz;i

:
i
:
i  k ;i
Jz;i
 
:
i
2
66666664
3
77777775
:
Therefore with (18), deﬁne ±a;i ¼ ¾a;i  ^¾a;i as the observed
error vector. It satisﬁes
lim
t!1 k±a;ik ¼ 0:
ð19Þ
Similar to position control (10), choose two suitable
matrices A0, A1 2 R33 and design the angular acceleration
with ESO as
hi ¼ A1e:
a;i  A0ea;i  ^¾a;i:
ð20Þ
The system (15) is transformed into
z:
a;i ¼
0
I
A0
A1

 ea;i
e:
a;i
"
#
þ
0
±a;i


;
ð21Þ
where the coeﬃcient matrix can be Hurwitz by suitably
choosing A0 and A1. From dynamics (1), the angular accel-
eration hi satisﬁes the constraint that
hi ¼
Jy;i  Jz;i
Jx;i

:
i 
:
i þ U2a;i
Jx;i
di  k;i
Jx;i

:
i þ d;i
Jz;i  Jx;i
Jy;i

:
i 
:
i þ U3a;i
Jy;i
di  k;i
Jy;i

:
i þ d;i
Jx;i  Jy;i
Jz;i

:
i
:
i þ U4a;i
Jz;i
 k ;i
Jz;i
 
:
i þ d ;i
2
66666664
3
77777775
:
Robust Formation Control of Quadrotor UAVs: A Fully-Actuated Control Approach
233
Un. Sys. 2026.14:227-238. Downloaded from www.worldscientific.com
by NETAJI SUBHAS INSTITUTE OF TECHOLOGY on 03/15/26. Re-use and distribution is strictly not permitted, except for Open Access articles.

## Page 8

Then the control inputs Uk;iðk ¼ 2; 3; 4Þ are solved as
U2;i ¼ Jx;i
di
hið1Þ  Jy;i  Jz;i
Jx;i

:
i 
:
i þ k;i
Jx;i

:
i  ^¾a;ið1Þ


;
U3;i ¼ Jy;i
di
hið2Þ  Jz;i  Jx;i
Jy;i

:
i 
:
i þ k;i
Jy;i

:
i  ^¾a;ið2Þ


;
U4;i ¼ Jz;i hið3Þ  Jx;i  Jy;i
Jz;i

:
i
:
i þ k ;i
Jz;i
 
:
i  ^¾a;ið3Þ


:
ð22Þ
With Uk;iðk ¼ 2; 3; 4Þ obtained, the actual angular acceler-
ation ½
::
i; 
::
i;  
::
iT can be calculated based on the dynamics
model (1).
3.3.
System robustness analysis
Combining the FAS control and ESO compensation, the
accelerations designed for position and attitude layers are
recalled as
ai ¼ aj  A1e:
p;i  A0ep;i  ^¾p;i;
ð23Þ
hi ¼ A1e:
a;i  A0ea;i  ^¾a;i:
ð24Þ
And the corresponding systems are
z:
p;i ¼
0
I
A0
A1

 ep;i
e:
p;i
"
#
þ
0
±p;i


;
ð25Þ
z:
a;i ¼
0
I
A0
A1

 ea;i
e:
a;i
"
#
þ
0
±a;i


:
ð26Þ
With (9) and (19), the system response output is bounded
based on BIBO stable criterion [21]. Moreover, deﬁne
zi ¼
zp;i
za;i


:
ð27Þ
The derivative of zi is
z: ¼
z:
p;i
z:
a;i
"
#
¼ Az þ Bu;
ð28Þ
where
A ¼
0
I
0
A0
 A1
0
I
0
A0
A1
2
64
3
75;
B ¼
0
0
I
0
0
0
0
I
2
664
3
775;
u ¼
±p;i
±a;i


:
From (9) and (19), we can conclude that
lim
t!1 kBuk ¼ 0:
ð29Þ
The solution of linear time-invariant system (28) is given by
zðtÞ ¼ eA
ðtt0Þzðt0Þ þ
Z t
t0
eA
ðtÞBuðÞd:
Since matrix A is Hurwitz, it satisﬁes
keA
ðtt0Þk 	 keðtt0Þ:
ð30Þ
With (30), one can conclude that
kzðtÞk 	 keðtt0Þkzðt0Þk þ
Z t
t0
keðtÞkBk
 kuðÞkd
	 keðtt0Þkzðt0Þk
þ k
 ð1  eðtt0ÞÞkBk sup
t0		t
kuðÞk
	 keðtt0Þkzðt0Þk þ k
 kBk sup
t0		t
kuðÞk:
So considering (29), the system (28) is input-to-state stable
(ISS).
3.4.
System stability analysis
Considering position and attitude layers together, deﬁne
&i ¼
&p;i
&a;i


;
Gi ¼
Gp;i
0
0
Ga;i


;
½i ¼
½p;i
½a;i


;
Hi ¼
Hp;i
0
0
Ha;i


:
Theorem 3.4. Consider the system (1) with the FAS-ESO.
The designed control laws (23) and (24) guarantee that the
error state zi converges into the following ellipsoid centered
at the origin:
£i;	ið0Þ ¼
zi
1
2 z T
i Pizi 	 i
	i


	
;
where i and 	i are given in the following proof.
The proofs stability of the system and convergence of the
state are as follows.
Proof. (1) Stability of the closed-loop system
From (7), (17), (25), and (26), the closed-loop system
can be presented as
z:
i
&:
i
"
#
¼
A
0
0
Gi


zi
&i


þ
Bu
Hi½i


:
ð31Þ
It is obvious that the eigenvalues satisfy
eig
A
0
0
Gi




¼ eigðAÞ [ eigðGiÞ:
234
Z. Liu & P. Li
Un. Sys. 2026.14:227-238. Downloaded from www.worldscientific.com
by NETAJI SUBHAS INSTITUTE OF TECHOLOGY on 03/15/26. Re-use and distribution is strictly not permitted, except for Open Access articles.

## Page 9

Since A and Gi can be Hurwitz and with the condition (29),
the nontrivial condition on the system (31) is the bound-
edness of ½i. This means that the generalized uncertainty
term must be diﬀerentiable, which is a reasonable as-
sumption.
Proof. (2) Convergence of zi
According to [22], let A 2 Rnn satisfy
RekðAÞ 	  
i
2 ;
k ¼ 1; 2; . . . ; n;
where 
i > 0, and then there exists a positive deﬁnite ma-
trix Pi 2 Rnn satisfying
ATPi þ PiA 	 
iPi:
Consider the following Lyapunov function:
Vi ¼ 1
2 z T
i Pizi:
The time derivative of Vi is
Vi ¼ 1
2 z: T
i Pizi þ 1
2 z T
i Piz:
i
¼ 1
2 ðA
zi þ B
u
ÞTPizi þ 1
2 z T
i PiðAzi þ BuÞ
¼ 1
2 z T
i ðATPi þ PiAÞzi þ z T
i PiBu
	 
i
2 z T
i Pizi þ kzik  kPik  kBuk
	 
i
2 z T
i Pizi þ i
2 kzik2 þ 1
2i
kPik2  kBuk2
	 1
2 z T
i ð
iPi  iIÞzi þ 1
2i
kPik2  kBuk2
	 minð
iPi  iIÞ
maxðPiÞ
Vi þ 1
2i
kPik2  kBuk2
	 	iVi þ i;
ð32Þ
where
	i ¼ minð
iPi  iIÞ
maxðPiÞ
; i ¼ 1
2i
kPik2  kBuk2:
It thus follows from the comparison lemma that
Vi 	 Við0Þe	it þ i
	i
ð1  e	itÞ;
which gives
Vi 	
Við0Þ  i
	i


e	it þ i
	i
! i
	i
; t ! 1:
Thus, the state zi eventually converges into the ellipsoid
£i;	ið0Þ in Theorem 3.4. This completes the proof.
It is worth noting that the system will not be stable or
the state zi cannot converge to the neighborhood of the
origin without ESO. Since the input u in (28) will be the
uncertainty ½¾p;i;
¾a;iT instead of the observed error
½±p;i;
±a;iT which is in the neighborhood of zero as in
(9) and (19), the convergence of the system (31) would
no longer hold due to the unknown value of the uncer-
tainty. Also, i in (32) containing the input u with un-
certainty may be not an extremely small value, which
cannot support the convergence proof of the state zi.
Thanks to the convergence of the ESO, the uncertainty
estimation error ½±p;i;
±a;iT tends to 0 as t ! 1. As a
result, the ultimate convergence of (27) and (31) can be
guaranteed.
4.
Examples
The results of the proposed method are compared with a
recent nonsingular fast terminal sliding mode control (SMC)
method in [23]. Consider a UAV team with four agents and
one virtual leader. Parameters related to the dynamics
model of the four UAVs are shown in Table 1.
The extended state observer parameters are set as
"i ¼ 1:2;
1;i ¼ 9;
2;i ¼ 22;
3;i ¼ 16 ði ¼ 1; . . . ; 4Þ:
The control parameters are designed as in Table 2.
The formation in this example is maintained on a hori-
zontal plane, and the communication topology is shown in
Fig. 5.
Let the virtual leader’s trajectory be
p0 ¼
2:5 cosð0:4tÞ
2:5 sinð0:4tÞ
0:5t þ 5
2
4
3
5:
The initial positions of UAV are listed in Table 3. The
initial attitudes are ½0; 0; 0T.
The UAVs are subject to disturbances dkðk ¼ x; y; z; ;
;  Þ after t ¼ 30 s which are modeled as
dx;y;z ¼ 2:5ðesinð0:1tþ 
5Þ  ecosð0:1t 
5ÞÞ
 0:5 sinð0:1tÞ þ 0:5 cosð0:1tÞ;
d;; ¼ 0:5 sinð0:1tÞ:
The actuator faults fr;i ðr; i ¼ 1; 2; 3; 4Þ occur after t ¼ 60 s
governed by the fault functions
f1 ¼ 1:5;
f2;3;4 ¼ 0:5 sinð0:1tÞ:
Robust Formation Control of Quadrotor UAVs: A Fully-Actuated Control Approach
235
Un. Sys. 2026.14:227-238. Downloaded from www.worldscientific.com
by NETAJI SUBHAS INSTITUTE OF TECHOLOGY on 03/15/26. Re-use and distribution is strictly not permitted, except for Open Access articles.

## Page 10

We deﬁne the loss function as lossi ¼ kep;ik2 to quantify
the error of both controllers. Deﬁne loss function as
Ek ¼ k±k;ik2, ðk ¼ a; pÞ to quantify the error of the extended
state observer in position and attitude layers respectively.
Additionally, we calculate the sum of the loss function lossi
with ESO or without to illustrate its eﬀect.
Taking the position x and the roll angle  as examples,
the observation results of the extended state observer are
shown in Fig. 6. Both the estimation errors in position and
attitude layers are shown in Fig. 7. The sum of loss values
with or without ESO in 80 s is in Table 4.
It can be seen that the observations of the extended state
observer are able to converge to the true values with small
error ﬂuctuations in a ﬁnite time when disturbances or
faults are added. And the errors are decreased with ESO.
(1) Results of position control
The trajectories in this example are shown in Fig. 8. The loss
functions of both methods are compared in Fig. 9. Figure 10
shows the formation shape and its projection to the hori-
zontal plane at the 80th second.
It can be seen that the proposed method results in higher
convergence rate and smaller steady errors.
Table 1.
Formation parameters.
Parameter
Value
m
2 kg
g
9.81 m/s2
kx;y;z
0.01 kg/s
k;; 
1:49  107 N  s=rad
Jx;y;z
1.25 N  s2=rad
d
0.3 m
Table 2.
FAS parameters.
A0
A1
A0
A1
6:25I
5I
36I
12I
Fig. 5.
Horizontal plane shape with communication topology.
Table 3.
Initial positions.
UAV
x½m
y½m
z½m
0
2.5
0
5
1
1
1
4
2
1
1
4
3
1
1
4
4
1
1
4
Fig. 6.
Observed versus true values of the total uncertainties.
Fig. 7.
The estimation errors in position and attitude layers.
236
Z. Liu & P. Li
Un. Sys. 2026.14:227-238. Downloaded from www.worldscientific.com
by NETAJI SUBHAS INSTITUTE OF TECHOLOGY on 03/15/26. Re-use and distribution is strictly not permitted, except for Open Access articles.

## Page 11

(2) Results of attitude control
Figure 11 illustrates the consistency of attitude angles
under FAS.
From Fig. 11, one can conclude that the proposed
scheme basically meets the attitude requirements.
5.
Conclusion
In this paper, we consider the formation control of UAVs
with both external disturbances and actuator faults. A fully
actuated system control scheme is designed to drive the
UAV formation to travel along the desired trajectory. An
extended state observer is designed to estimate uncertain-
ties, which is used to compensate the eﬀects of disturbances
and faults in the controller. In order to demonstrate the
eﬀectiveness of the proposed algorithm, extensive numeri-
cal experiments are conducted in comparison with a recent
SMC method. The results conﬁrm the convergence of the
uncertainty estimation by the ESO and the FAS algorithm
performs well both in position and attitude control. Overall,
FAS achieves accurate and fast tracking of formation tra-
jectory with little ﬂuctuation, small steady-state errors and
Table 4.
The sum of loss function ([m]).
Algorithm
UAV1
UAV2
UAV3
UAV4
FAS-ESO
144.2894
151.6355
222.7442
165.1304
FAS
175.2373
193.1059
273.9323
186.3116
Fig. 8.
Formation ﬂight trajectories.
Fig. 9.
Loss function of both methods.
Fig. 10.
Three-dimensional and top-down view of the formation.
Fig. 11.
Atitudes control curves.
Robust Formation Control of Quadrotor UAVs: A Fully-Actuated Control Approach
237
Un. Sys. 2026.14:227-238. Downloaded from www.worldscientific.com
by NETAJI SUBHAS INSTITUTE OF TECHOLOGY on 03/15/26. Re-use and distribution is strictly not permitted, except for Open Access articles.

## Page 12

well formation maintenance. Control eﬀorts will be devoted
to techniques for obstacle avoidance and navigation.
Acknowledgments
This work was supported in part by the National Natural
Science Foundation (NNSF) of China (Grant 62303133,
62188101) and in part by the Guangdong Basic and Applied
Basic Research Foundation (Grant 2022A1515011274).
ORCID
Zhihao Liu
https://orcid.org/0009-0000-0751-1557
Peng Li
https://orcid.org/0000-0002-8217-1326
References
[1]
J. Wang, W. B. Gu and L. Y. Dou, Leader-Follower formation control of
multiple UAVs with trajectory tracking design, Acta Aeronaut. As-
tronaut. Sin. 41(S1) (2020) 88–98.
[2]
W. W. Pan, D. P. Jiang, Y. J. Pang
et al., A multi-AUV formation
algorithm combining artiﬁcial potential ﬁeld and virtual structure,
Binggong Xuebao/Acta Armament. 38(2) (2017) 326–334.
[3]
Q. Luo and H. Duan, Distributed UAV ﬂocking control based on
homing pigeon hierarchical strategies, Aerosp. Sci. Technol. 70 (2017)
257–264.
[4]
M. Yang, Y. Shou, Y. Tang, C. Liu and B. Xu, Multi-quadrotor UAVs
formation maintenance and collision avoidance control, Aerosp. Sci.
Technol. 43(S1) (2020) 89–99.
[5]
Q. Wei, R. Liu and H. Zhang, High-order consistent formation control
method for quadrotor UAV, Electro-Opt. Control 26(8) (2019) 1–5.
[6]
B. Yu, X. Dong, S. Zongying et al., Formation control for quadrotor
swarm systems: Algorithms and experiments, in Proc. 32nd Chinese
Control Conf. (IEEE, 2013), pp. 7099–7104.
[7]
X. Dong, B. Yu, Z. Shi and Y. Zhong, Time varying formation control
for unmanned aerial vehicles: Theories and applications, IEEE Trans.
Control Syst. Technol. 23(1) (2014) 340–348.
[8]
H. Wang, B. Zheng, S. Lu et al., Adaptive fault-tolerant control of UAV
formation based on observer, Electron. Measur. Technol. 45(17)
(2022) 56–64.
[9]
D. Zhang, T. Liu and J. Song, Optimal cooperative fault-tolerant con-
trol of UAV formation based on dynamic programming, Electro-Opt.
Control 30(4) (2023) 34–39.
[10]
L. Dou, T. Chen and Q. Mao, Distributed quadrotor formation tracking
control based on a disturbance observer, J. Tianjin Univ. (Natural Sci.
Eng. Technol. Edition) 51(8) (2018) 817–824.
[11]
G.-R. Duan, High-order system approaches: I. Fully actuated systems
and parametric design, Acta Automat. Sin. 46(7) (2020) 1333–1345.
[12]
H. Sun, Research on trajectory tracking control of six-degree-of-
freedom manipulator based on high-order fully actuated system
model, Harbin Univ. Sci. Technol. (2023), doi: 10.27063/d.cnki.
ghlgu.2023.000814.
[13]
T. Zhao and G. Duan, Fully actuated system approach to attitude
control of ﬂexible spacecraft with nonlinear time-varying inertia, Sci.
China (Inform. Sci.) 65(11) (2022) 148–162.
[14]
Z. Qin and G. D. Ren, Fully actuated system approach for 6DOF
spacecraft control based on extended state observer, J. Syst. Sci.
Complex. 35(2) (2022) 604–622.
[15]
Z. Liu and P. Li, Robust multi-mobile robot formation control: A fully
actuated system control approach, 2024 3rd Conf. Fully Actuated Sys-
tem Theory and Applications (FASTA) (IEEE, 2024), pp. 1011–1016.
[16]
Y. Fei, Y. Sun and P. Shi, Robust hierarchical formation control of
unmanned aerial vehicles via neural-based observers, Drones 6(2)
(2022) 1119–1125.
[17]
W. Jun and L. Ang, Multi-quadrotor UAV formation adaptive fault-
tolerant control, J. Lanzhou Univ. Technol. 50(04) (2024) 69–76.
[18]
J. Wang and M. Luo, Robust global fast terminal sliding mode for-
mation fault-tolerant control of multi-quadrotor UAV, Flight Mech.
42(03) (2024) 68–75+88.
[19]
W. Zhang, J. Ma and K. Xing, State feedback control of interference
mismatched discrete systems based on a generalized expansion state
observer, Control Decis. Making 31(6) (2016) 1128–1132.
[20]
D. Qingfeng, J. Wuxing, G. Changsheng and A. Mingruo, Dual-loop
control of metamorphic centroid quadrotor UAV considering the
dynamic characteristics of the slider, J. Beijing Univ. Aeronaut. As-
tronaut. 50(3) (2024) 861–873.
[21]
J. P. Hespanha, Linear Systems Theory, 2nd edn. (Princeton University
Press, 2018).
[22]
G. R. Duan, High-order fully actuated system approaches: Part III.
Robust control and high-order backstepping, Int. J. Syst. Sci. 52(5)
(2021) 952–971.
[23]
H. Yulong, S. Wei, C. Baoshan, G. Xiaolin and L. Guoqiang, Study on
nonsingular fast terminal sliding mode control, Syst. Eng. Electron. 39
(2017) 1119–1125.
238
Z. Liu & P. Li
Un. Sys. 2026.14:227-238. Downloaded from www.worldscientific.com
by NETAJI SUBHAS INSTITUTE OF TECHOLOGY on 03/15/26. Re-use and distribution is strictly not permitted, except for Open Access articles.
