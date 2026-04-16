# Trajectory_Tracking_Control_of_Quadrotor_Drones_Based_on_Disturbance_Observers.pdf

## Page 1

Trajectory Tracking Control of Quadrotor Drones 
Based on Disturbance Observers 
Feiming Wang 
School of Automation, Beijing Information Science Technology University 
Beijing, China 
1281809241@qq.com 
 
Abstract—A composite control method is proposed by 
combining a disturbance observer with sliding mode control to 
address the uncertainties of parameters, models and external 
disturbances in the position and attitude control system for 
quadrotor unmanned aerial vehicles (UAVs). The observer 
estimates the equivalent disturbances in real-time, and a sliding 
mode controller is designed based on these estimates to track the 
desired signals. The designed controller not only ensures the 
system's asymptotic stability but also effectively suppresses the 
impact of internal and external disturbances. Finally, simulations 
verify the effectiveness of the proposed method.  
Keywords-Quadrotor drones; sliding mode control; disturbance 
observers; trajectory tracking 
I. INTRODUCTION 
Quadrotor drones, due to their outstanding flight 
characteristics and superior flexibility, have been applied in 
multiple fields such as search and rescue, logistics 
transportation, and aerial photography, showcasing their 
immense potential for application. However, the challenges 
remain significant in the development of high-precision control 
systems, especially when facing multiple disturbances such as 
external environmental conditions, and uncertainties in internal 
parameters and models. 
In the realm of controller design for quadrotor drones, 
literature [1] proposed a method that combines PID with 
genetic algorithms, optimizing PID controller parameters to 
effectively reduce tracking errors. PID control performs well in 
controlling linear systems but is less suited for nonlinear 
dynamic systems and strongly coupled systems, such as 
quadrotors. Literature [2-4] demonstrated the use of active 
disturbance rejection control to overcome the challenges faced 
by traditional PID control in handling objects with high 
uncertainty. However, this method's parameter adjustment is 
relatively complex and not convenient for engineering 
applications. Sliding mode control, as a powerful nonlinear 
control strategy, has been applied to the control of quadrotor 
drones in literature [5-6]. These methods have achieved 
significant success in suppressing nonlinear dynamics and 
coupling effects, but the sliding mode controller can cause 
chattering phenomena when its output is large, and the control 
performance is not ideal under various disturbances. 
Regarding the control strategy for disturbance attenuation, 
observers can estimate unknown disturbances and effectively 
compensate for them through a feedforward mechanism [7]. 
Literature [8] introduced a method that combines disturbance 
observers with optimal control techniques aimed at estimating 
and compensating for wind disturbances, achieving precise 
position and attitude control of the drone. Literature [9] 
addressed the control issues of quadrotor drones under mixed 
disturbances such as periodic disturbances and wind 
disturbances, proposing a combination scheme of disturbance 
observers (DO) and extended state observers (ESO), effectively 
suppressing these composite disturbances and achieving 
precise trajectory tracking. In literature [10-11], by combining 
NDO and other methods, the study focused on composite 
controllers with a hierarchical structure and established the 
stability of the closed-loop system. Disturbance observers not 
only achieve disturbance attenuation but are also easy to 
integrate with other traditional control methods. 
Based on the analysis above, facing challenges such as 
parameter uncertainty, external time-varying disturbances, and 
uncertainties in the dynamic model, a composite control 
strategy that integrates Nonlinear Disturbance Observers (NDO) 
with Sliding Mode Control (SMC) is proposed to enhance the 
position tracking accuracy of quadrotors, thereby improving 
their trajectory tracking precision. On the one hand, the 
nonlinear disturbance observer estimates and mitigates the 
effects of both internal and external disturbances on the attitude 
loop through a feedforward approach; on the other hand, the 
disturbance 
observer 
compensates 
for 
the 
equivalent 
disturbances in the position loop in real-time, reducing their 
impact on position tracking. Finally, the stability of the closed-
loop system is analyzed using the Lyapunov method, and anti-
disturbance 
experiments 
are 
designed 
to 
verify 
the 
effectiveness of the proposed control method. 
II. QUADROTOR DYNAMICS MODEL 
Assuming that the quadrotor drone has a rigid body 
structure with its geometric center coinciding with the center of 
gravity, the coordinate system is illustrated in Figure 1, where   
represents the world-fixed frame, and represents the body-fixed 
frame. 
1
ϖ
2
ϖ
3
ϖ
4
ϖ
bY
Y
X
Z
b
Z
ψ
φ
θ
b
X
 
Figure 1. Schematic diagram of the quadrotor drone structure. 
2024 3rd International Symposium on Aerospace Engineering and Systems (ISAES)
979-8-3503-5041-8/24/$31.00 ©2024 IEEE
398
2024 3rd International Symposium on Aerospace Engineering and Systems (ISAES) | 979-8-3503-5041-8/24/$31.00 ©2024 IEEE | DOI: 10.1109/ISAES61964.2024.10751312
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:34:42 UTC from IEEE Xplore.  Restrictions apply.

## Page 2

The rotational speeds of the propellers are defined as 
1
ϖ ,
2
ϖ ,
3
ϖ , and 
4
ϖ , respectively, with the total lift force 
along the
b
Z axis denoted as f , and the rotational torques 
about the
b
X ,
bY , and
b
Z  axes represented by
φτ ,
θτ , and
ψ
τ
, 
respectively. The relationship between the lift force f , 
rotational torques τ , and the propeller speeds is as follows: 
2
1
2
2
2
3
2
4
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
T
T
T
T
T
T
T
T
T
T
T
T
M
M
M
M
c
c
c
c
f
dc
dc
dc
dc
dc
dc
dc
dc
c
c
c
c
φ
θ
ψ
ϖ
τ
ϖ
τ
ϖ
τ
ϖ









−
−








= 






−
−


















      (1) 
where d represents the distance from the drone's center to 
the motor's axis of rotation, with
Tc denoting the propeller 
thrust coefficient and
M
c
the propeller torque coefficient. 
The positional and attitudinal dynamics of the quadrotor 
drone can be represented as follows: 
(
)
(
)
(
)
x
t
x
y
t
y
z
t
z
x
y
z
rp
y
z
x
rp
z
x
y
mx
F
k x
d
my
F
k y
d
mz
F
mg
k z
d
I
I
I
J
d
I
I
I
J
d
I
I
I
d
φ
φ
θ
θ
ψ
φ
φ
θψ
τ
θ
θ
φψ
τ
φ
ψ
φθ
τ
=
+
+


=
+
+


=
−
+
+

=
−
+
−
Ω
+


=
−
+
+
Ω+


=
−
+
+


























        (2) 
where m  represents the total mass of the drone and its 
payload, , ,
x y z represent the positions of the drone along 
three axes in world-fixed frame, respectively, and 
,
,
x
y
z
F F F  
are the equivalent control forces in the three axes of the 
position loop, respectively. g is the gravity acceleration, 
tk  is 
the drag coefficient, and 
,
,
x
y
z
d
d
d
denote the external 
disturbance forces encountered in the three axes of the position 
loop, respectively. 
,
,
x
y
z
I
I
I


 represent the rotational inertias of 
the quadrotor, with , ,
φ θ ψ  corresponding to the roll, pitch, 
and yaw angles, respectively. 
rp
J
 signifies the rotational 
inertia of the propellers, and 
1
2
3
4
ϖ
ϖ
ϖ
ϖ
Ω= −
−
+
+
.dφ , 
dθ  , dψ represent the external disturbance torques affecting the 
attitudinal loop. 
The relationship between the equivalent control force 
F and the total lift force f  of the drone can be expressed as 
follows: 
cos
sin
cos
sin
sin
=
sin
sin
cos
cos
sin
cos cos
x
y
z
F
F
F
f
F
ψ
θ
φ
ψ
φ
ψ
θ
φ
ψ
φ
φ
θ
+








=
−












    (3) 
During flight, drones may carry heavy loads, which, when 
not perfectly aligned with the drone's geometric center, can 
affect its rotational inertia. The quadrotor's rotational inertia 
iIis a combination of nominal (
iI ) and uncertain (
iI
∆
) parts 
as 
(
, , )
i
i
i
I
I
I i
x y z
=
+ ∆
=

                     (4) 
The position and attitude kinematics of the quadrotor drone 
can be reformulated as follows: 
1
1
1
1
1
1
1
1
1
x
x
y
y
z
z
y
z
x
x
x
z
x
y
y
y
x
y
z
z
z
x
F
d
m
y
F
d
m
z
F
d
m
I
I
d
I
I
I
I
I
d
I
I
I
I
I
d
I
I
I
φ
φ
θ
θ
ψ
φ
φ
θψ
τ
θ
φψ
τ
ψ
φθ
τ
=
+



=
+


=
+

−
=
+
+



−
=
+
+



−

=
+
+
















              (5) 
And 
1
1
1
t
x
x
t
y
y
t
z
z
y
z
x
rp
x
z
x
y
rp
y
x
y
z
z
k
d
x
d
m
m
k
d
y
d
m
m
k
d
z
d
m
m
I
I
d
I
J
d
I
I
I
d
I
J
d
I
I
I
d
I
d
I
φ
φ
θ
θ
ψ
ψ
φ
θψ
θ
θ
φψ
φ
ψ
φθ

=
+



=
+



=
+

∆
−∆
= −∆
+
−
Ω
+

∆


∆
−∆
= −∆
+
+
Ω+

∆


∆
−∆

= −∆
+
+

∆




















    (6) 
where
,
,
x
y
z
d
d
d


 represent the equivalent disturbances in 
the position loop, and
,
,
d
d
d
φ
θ
ψ



denote the equivalent 
disturbances in the attitude loop. 
399
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:34:42 UTC from IEEE Xplore.  Restrictions apply.

## Page 3

Assumption 1. The roll, pitch, and yaw angles of the 
drone all satisfy 
(
,
)
2 2
π π
φ ∈−
, 
(
,
)
2 2
π π
θ ∈−
, 
(
,
)
2 2
π π
ψ ∈−
. 
Assumption 
2. The equivalent disturbance 
id
is 
continuous and bounded, and its derivative is also bounded 
and there exist two constants 
max,
d
d such that 
max
id
d
≤

, 
id
d
≤

.(
, , , , ,
)
i
x y z φ θ ψ
=
 
III.  DESIGN OF CONTROL SYSTEMS 
A. Design of the Observer 
The designed nonlinear disturbance observer (NDO) and 
disturbance observer (DO) in this section are aimed at 
respectively estimating unknown disturbances in the attitude 
and position loops for compensation. 
1) Design of the Nonlinear Disturbance Observer 
The attitude dynamics of system (5) are reformulated as 
follows: 
a
a
f
B
B d
η
τ
=
+
+


                           (7) 
where 
[
]
T
η
φ
θ
ψ
=
denotes the system state variable, 
T
y
z
x
y
z
x
x
y
z
I
I
I
I
I
I
f
I
I
I
θψ
φψ
φθ


−
−
−
= 










,
1
1
1
(
)
a
x
y
z
B
diag I
I
I
=
,
T
φ
θ
ψ
τ
τ
τ
τ


= 
, 
T
a
d
d
d
d
φ
θ
ψ


= 





. 
To estimate the equivalent disturbance
a
d, a nonlinear 
disturbance observer is selected as follows [12]: 
( ){
( )
]
(
)
ˆ
)}
(
[
a
a
a
a
a
a
a
a
B
f
B
d
z
l
z
z
η
λ η
τ
λ η

=

= −
+
+
+
+






      (8) 
where ˆ
a
ddenotes the estimated disturbance, 
az  represents 
the observer state variable, 
( )
al η is the gain matrix of the 
disturbance observer, and 
( )
a
λ η is a nonlinear function, with 
their relationship defined as follows: 
( )
( )
a
al
λ η
η
η
∂
=
∂



                                (9) 
Theorem 1: By selecting the gain 
3 3
( )
al
PI
η
×
=

 of the 
nonlinear disturbance observer and the nonlinear function 
( )
a
P
λ η
η
=

, where 
1
2
3
(
)
P
diag P
P
P
=
 , 
3 3
I ×
is the 
identity matrix and 
1
2
3
,
,
P P P are positive, it is guaranteed that 
the steady-state error of the disturbance estimation is bounded. 
Proof: Define the attitude loop disturbance estimation 
error  
ˆ
a
a
a
d
d
e =
−

                                  (10) 
Upon differentiation, it yields: 
ˆ
( )
a
a
a
a
a
a
a
a
a
e
z
d
d
d
d
l
B e
x
λ
−
=
−
−
=
−
=











     (11) 
Define the Lyapunov function as: 
1
1
2
T
a
a
V
e e
=
                                  (12) 
Differentiating, one obtains: 
1
2
 
   
[
( )
]
(
 
 
 
)
 
 
T
T
a
a
a
a
a
a
T
T
a
a
a
a
a
a
a
a
a
T
T
a
a
a
a
a
a
a
a
d
d
d
d
V
e e
e
l
x B e
e l
x B e
e
p
e e
e
p
e
e
µ
µ
−
≤
−
≤
=
=
=
+
−
+
−
+





          (13) 
where
ap  represents the minimum eigenvalue of matrix 
P , 
a
µ signifies the minimum eigenvalue of matrix 
a
B . 
Since matrices
a
B and P are positive definite, it follows 
that
0
a
µ >
and
0
ap >
. When 
/
a
a
a
d
e
p µ
>
is chosen, 
1
V becomes negative definite. Hence, an upper bound for the 
steady-state estimation error can be derived as: 
a
a
a
e
d
p µ
<
                                  (14) 
Therefore, it is reasonable to choose the disturbance 
observer gain to keep the estimation error within a certain 
range. At this point, the disturbance observer estimates the 
equivalent disturbance 
a
dwith a certain level of accuracy. 
2) Design of the Disturbance Observer 
To estimate the equivalent disturbance
a
d, the disturbance 
observers for channels
, ,
X Y Z are designed as follows 
(
, , )
j
x y z
=
: 
0
0
0
0
(
)
1
(
)
p
q
j
d
j
j
j
j
j
j
p
q
j
p
j
j
j
j
d
k
Tsat
z
v
z
k
Tsat
F
m
ρ
ερ
ρ
ρ
ρ
ερ
ρ


= −
−
−

=
−



= −
−
−
+



  (15) 
400
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:34:42 UTC from IEEE Xplore.  Restrictions apply.

## Page 4

where ˆ
j
d represents the disturbance estimation of position 
loop,
0
0
, ,
,
,
dk
p q T
ε
are observer gains, and 
,
j
jz
ρ
denote 
the internal states of the observer. The saturation function S is 
defined as follows: 
1,
( )
,
1,
x
k
x
sat x
k
x
k
k
x
k
>


=
−≤
≤


−
< −

                          (16) 
Theorem 2: By selecting appropriate disturbance observer 
gain
0
0
, ,
,
dk
p q
ε
all 
positive, 
and 
satisfying 
0
0
max
,
p
q T
d
<
>
. It ensures that the disturbance observer 
can track the equivalent disturbance
,
,
x
y
z
d
d
d


effectively. 
Proof: Define the position loop disturbance estimation 
error (
, , )
j
x y z
=
:  
0
0
0
0
ˆ
=
(
)
1
    =
(
)
    =
    =
p
q
j
j
d
j
j
j
j
p
q
d
j
j
j
j
j
j
j
j
j
d
d
k
Tsat
d
k
Tsat
F
v
m
z
e
v
ρ
ερ
ρ
ρ
ερ
ρ
ρ
−
−
−
−
−
−
−
−
+
−
−
= 






   (17) 
Define the Lyapunov function as: 
2
2
1
2
j
V
ρ
=
                                   (18) 
Differentiating, one obtains: 
0
0
0
0
0
0
0
0
2
2
2
(
)
]
   
  
=
[
 
p
q
d
j
j
j
j
p
q
q
d
j
j
j
j
j
p
q
q
d
j
j
j
j
j
k
Tsa
T
V
t
d
k
d
k
ρ
ερ
ρ
ρ
ερ
ρ
ρ
ρ
ε
ρ
ρ
ρ
ρ
+
+
−
−
−
−
≤−
−
−
≤−
−
=
+




   (19) 
From equation (24), it follows that: 
0
0
0
0
0
0
2
2
2
2
2
2
2
p
q
p
q
q
q
d
V
V
V
k
ε
+
+
≤−
−

                    (20) 
Based on [13], it is evident that variable
j
ρ converges to 
0 within a finite time dt , thereby ensuring the convergence of 
j
je
ρ
= within a finite time. 
B. Design of the controller 
UAV
Attitude 
SMC
NDO
c
τ
d
τ
+
ˆ
a
d
d
η
η
,
η η
η
−
+
−
F
,v
γ
v
d
F
,
,
d
d
d
v
v
γ

,
a
p
d
d


 
Figure 2. Scheme diagram of the quadrotor drone structure. 
The specific structure of the sliding mode control with 
composite disturbance observer adopted in this paper is shown 
in Figure 2. The sliding mode controller mainly controls the 
attitude and position so that the desired value can be reached 
quickly and makes the control system robust, while the 
disturbance observer is used to estimate and compensate for 
the disturbance, which is used to improve the control accuracy 
of the system. 
1) Design of attitude controller 
The attitude angle tracking error is defined as 
d
eη
η
η
=
−
, 
where
[
]
T
d
d
d
d
η
φ
θ
ψ
=
represents the desired attitude 
angle. 
For system (5), the sliding mode surface is chosen in the 
following form: 
1
1
q
p
a
a
a
s
s
s
e
e
e
s
φ
θ
η
η
η
ψ
α
β




=
=
+
+







               (21) 
where 
1
2
3
(
)
a
diag
α
α
α
α
=
 and 
1
2
3
(
)
a
diag
β
β
β
β
=
 
are positive definite matrices, and 
1
1
0
q
p
<
<
. 
Taking the derivative of the sliding mode surface yields: 
1
1
1
1
1
q
p
a
a
a
q
s
e
e
e
e
p
η
η
η
η
α
β
−
=
+
+



                 (22) 
the convergence rate 
a
u is selected as follows: 
1
2
1
2
1
2
(
)
(
)
(
)
a
sat s
s
u
sat s
s
sat s
s
φ
φ
φ φ
θ
θ
θ
θ
ψ
ψ
ψ
ψ
ρ
ρ
ρ
ρ
ρ
ρ


−
−


=
−
−




−
−


                    (23) 
For attitude motion systems, a sliding mode attitude 
controller can be defined as follows: 
1
1
1
1
1
1
(
)
q
p
c
a
d
a
a
a
q
B
f
e
e
e
u
p
η
η
η
τ
η
α
β
−
−
=
−
+
−
−
+



   (24) 
The composite sliding mode control law based on 
nonlinear disturbance observer is defined as follows: 
401
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:34:42 UTC from IEEE Xplore.  Restrictions apply.

## Page 5

1
1
1
1
1
1
ˆ
(
 
)
q
p
d
a
d
a
a
a
a
q
B
f
e
e
e
u
d
p
η
η
η
τ
η
α
β
−
−
=
−
+
−
−
+
−



(25) 
The desired attitude angular velocity
,
d
d
η η

are set to zero, 
which is applicable to quadrotor UAVs operating within a 
small angle range. 
Theorem 3: For system (5), when the control law is 
chosen 
as 
(25) 
and 
gains 
satisfy 
{
}
1
1
1
min
/
a
a
d
p
φ
θ
ψ
ρ
ρ
ρ
µ
µ
>
 and 
2
2
2
,
,
φ
θ
ψ
ρ
ρ
ρ
 
both are positive, the system is asymptotically stable. 
Proof: Substituting equation (25) into equation (5) yields: 
a
a
a
a
s
u
B e
=
+

                               (26) 
Define the Lyapunov function as: 
1
2
T
a
a
a
V
s s
=
                                 (27) 
Differentiating, one obtains: 
2
1
2
2
1
2
2
1
2
2
1
2
2
1
2
2
1
2
1
(
)
1
     
(
)
1
     
(
)
1
1
     
1
     
(
)
   =
  
T
T
a
a
a
a
a
x
y
z
x
z
a
y
a
s
sat s
s
I
sat s
s
I
sat s
s
I
s
B
I
s
I
V
s s
s
u
e
s
s e
s
s e
s
s e
s
s
e
s
e
s
s
e
s
I
φ
φ
φ φ
θ
θ
θ
θ
θ
θ
θ
ψ
ψ
ψ
ψ
ψ
ψ
ψ
φ
φ φ
θ
θ
θ
θ
θ
θ
ψ
ψ
ψ
ψ
ψ
ψ
φ
φ φ
φ
φ
φ
ρ
ρ
ρ
ρ
ρ
ρ
ρ
ρ
ρ
ρ
ρ
ρ
−
−
+
−
−
+
−
−
+
−
−
+
−
−
+
−
−
+
=
=
+
≤


        (28) 
where 
T
ae
e
e
e
φ
θ
ψ


= 
. 
Let µ be defined as the maximum eigenvalue of 
matrix
a
B . From equation (28), it is evident that when 
{
}
1
1
1
min
/
a
a
d
p
φ
θ
ψ
ρ
ρ
ρ
µ
µ
>
and 
2
2
2
,
,
φ
θ
ψ
ρ
ρ
ρ
 
are all positive,
0
V <

. Therefore, the closed-loop system is 
asymptotically stable. 
2) Design of attitude controller 
Define the position tracking error 
d
eγ
γ
γ
=
−
, velocity 
tracking error
v
d
e
v
v
=
−
, where 
[
]T
x
y
z
γ =
 and 
[
]
T
v
x
y
z
= 


 represent the position and velocity vectors in 
the drone's world-fixed frame, and 
,
d
dv
γ
 are the desired 
position and desired velocity, respectively. 
For the position motion system (5), we select the following 
form of sliding mode surface: 
2
2
q
x
p
p
y
p
p
z
s
s
s
e
e
e
s
γ
γ
γ
α
β




=
=
+
+







               (29) 
where 
4
5
6
(
)
p
diag
α
α
α
α
=
 and 
4
5
6
(
)
a
diag
β
β
β
β
=
 
are positive definite matrices, and 
2
2
0
q
p
<
<
. 
Taking the derivative of the sliding mode surface yields: 
2
2
1
2
2
q
p
p
p
p
q
s
e
e
e
e
p
γ
γ
γ
γ
α
β
−
=
+
+



               (30) 
the convergence rate 
p
u is selected as follows: 
1
2
1
2
1
2
(
)
(
)
(
)
x
x
x
x
p
y
y
y
y
z
z
z
z
sat s
s
u
sat s
s
sat s
s
ρ
ρ
ρ
ρ
ρ
ρ
−
−




= −
−




−
−


                    (31) 
For position motion systems, a sliding mode attitude 
controller can be defined as follows: 
2
2
1
2
2
q
p
c
d
p
v
p
p
q
F
mv
m
e
m
e
e
mu
p
γ
γ
α
β
−
=
−
−
+


   (32) 
Therefore, the composite sliding mode position control law 
based on disturbance observer is: 
1
ˆ
q
p
d
d
p
v
p
p
p
q
F
mv
m
e
m
e
e
mu
md
p
γ
γ
α
β
−
=
−
−
+
−



  (33) 
where
ˆ
ˆ
ˆ
ˆ
T
p
x
y
z
d
d
d
d


= 


 represents 
the 
estimated 
disturbance by the observer. 
Theorem 4: For system (7), when the control law is 
selected 
as 
(32) 
and 
the 
gains 
satisfy 
1
1
1
min(
)
max(
)
x
y
z
x
y
z
ρ
ρ
ρ
ρ
ρ
ρ
>



, and 
2
2
2
,
,
x
y
z
ρ
ρ
ρ
 
are all positive, the system is asymptotically stable. 
proof: substituting equations (17), (31), and (33) into 
equation (5) yields: 
1
2
1
2
1
2
(
)
(
)
(
)
x
x
x
x
x
y
y
y
y
z
y
z
z
z
z
x
p
z
y
sat s
s
sat s
s
s
s
sat s
s
s
s
ρ
ρ
ρ
ρ
ρ
ρ
ρ
ρ
ρ








=
=








−
−
−
−
−
−
−
−


−









        (34) 
Define the Lyapunov function as: 
402
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:34:42 UTC from IEEE Xplore.  Restrictions apply.

## Page 6

1
2
T
p
p
p
V
s
s
=
                               (35) 
Differentiating, one obtains: 
2
1
2
2
1
2
2
1
2
2
1
2
2
1
2
2
1
2
(
)
     
(
)
     
(
)
    
 
 
 
=
 
 
 
  
  
 
x
x
x
x
x
y
y
y
y
y
z
z
z
z
z
x
x
x
x
y
y
y
y
z
z
z
z
T
p
p
p
x
x
y
y
z
z
x
x
y
y
z
z
sat s
s
sat s
s
sat s
s
s
s
s
V
s
s
s
s
s
s
s
s
s
s
s
s
s
s
ρ
ρ
ρ
ρ
ρ
ρ
ρ
ρ
ρ
ρ
ρ
ρ
ρ
ρ
ρ
ρ
ρ
ρ
−
−
−
−
−
−
−
−
−
−
−
+
−
−
+
=
−
−
≤
+








             (36) 
From equation (36), it can be observed that when 
1
1
1
min(
)
max(
)
x
y
z
x
y
z
ρ
ρ
ρ
ρ
ρ
ρ
>



 and 
2
2
2
,
,
x
y
z
ρ
ρ
ρ
 
are all positive,
0
p
V <

,thus indicating that the closed-loop 
system is asymptotically stable. 
3) Attitude estimation 
According to (3) and (33), the desired input for the attitude 
loop is driven by 
cos cos
sin
cos
arctan(cos
)
cos
sin
arctan(
)
z
x
y
d
z
x
y
d
z
F
f
F
F
F
F
F
F
φ
θ
ψ
ψ
φ
θ
ψ
ψ
θ

=



−

=



+

=

        (37) 
where 
d
ψ set to zero in the paper. 
IV.  SIMULATION RESULTS 
In this section, the effectiveness of the proposed composite 
control method is validated through MATLAB/Simulink 
simulations. Comparative tests with and without disturbances 
observer in a quadrotor subjected to a combination of internal 
and external disturbances. 
The structural parameters of the quadcopter attitude system 
are set as follows: 
1.5kg
m =
,
2
2
2.103 10
xI
kg m
−
=
×
⋅
,
2
2
2.163 10
yI
kg m
−
=
×
⋅
,
2
2
3.942 10
zI
kg m
−
=
×
⋅
,
0.187
d
m
=
,
5
2
0.938 10
/
/
Tc
N rad s
−
=
×
,
7
2
1.479 10
/ (
/ )
M
c
N m
rad s
−
=
×
⋅
,
5
2
8.19 10
/
rp
J
kg m
−
=
×
. 
The observer parameters are: 
{
}
5
5
3
p
diag
=
10
dk =
,
10
ε =
,
0
2
p =
,
0
3
q =
,
80
T =
. 
The sliding mode controller parameters are:  
1
30
φ
ρ
=
 , 
1
50
θ
ρ
=
, 
1
30
ψ
ρ
=
, 
2
20
φ
ρ
=
, 
2
20
θ
ρ
=
, 
2
20
ψ
ρ
=
. 
1
10
x
ρ
=
 , 
1
10
y
ρ
=
, 
1
10
z
ρ
=
, 
2
8
x
ρ
=
, 
2
8
y
ρ
=
, 
2
8
z
ρ
=
. 
The initial values of position and velocity for the quadrotor 
UAV 
are 
set 
to 
[
]
(0)= 0.2
0.2
0
(m)
T
γ
 and 
[
]
(0)= 0
0
0
(m/s)
T
v
, 
respectively. 
To 
validate 
the 
effectiveness of the composite controller, we assume uncertain 
parameters
iI
∆
to be 20% of the nominal system parameters 
iI .(
, ,
)
i
φ θ ψ
=
 
The desired position and velocity for the quadrotor UAV 
are set to: 
[
]
( )= 1.8sin
1.8cos
0.5
T
d t
t
t
γ
 
[
]
( )= 0.9cos
0.9sin
0.5
T
dv t
t
t
−
 
The external disturbances in the position and attitude loops 
of the quadrotor UAV are respectively designated as: 
1
2
3
2.9R cos(1.5
)
4
( )
1.8R cos(1.2
)
3
1.4R cos(
)
6
x
p
y
z
t
d
d
t
d
t
d
t
π
π
π


+










=
=
+












+




 
4
5
6
0.9R cos(5
)
4
( )
0.8R cos(6
)
3
0.4R cos(5
)
6
a
t
d
d t
d
t
d
t
φ
θ
ψ
π
π
π


+










=
=
+












+




 
Where 
1
R  to 
6
R  are random numbers between -1 and 1. 
0
2
4
6
8
-2
-1
0
1
2
dφ
 disturbance dφ
 Estimated dφ
 
403
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:34:42 UTC from IEEE Xplore.  Restrictions apply.

## Page 7

0
2
4
6
8
-2
-1
0
1
2
dθ
 disturbance dθ
 Estimated dθ
 
0
2
4
6
8
-1
0
1
 disturbance dψ
 Estimated dψ
dψ
t(s)
 
Figure 3. Comparison of disturbance in attitude loop. 
0
2
4
6
8
-2
0
2
4
 disturbance dx
 Estimated dx
dx
 
0
2
4
6
8
-2
0
2
 Disturbance dy
 Estimated dy
dy
 
0
2
4
6
8
8
10
12
 disturbance dz
 Estimated dz
dz
t(s)
 
Figure 4. Comparison of disturbance in position loop. 
-2
-1
0
1
2
-2
-1
0
1
2
y/m
x/m
 Dedired
 Actual Trajactory
-2
-1
0
1
2
-2
-1
0
1
2
 Dedired
 Actual Trajactory
y/m
x/m
 
Figure 5. Comparison of trajectory tracking performance: the left image 
without any observer, and the right image with two observers. 
-2
-1
0
1
2
-2
-1
0
1
2
y/m
x/m
 Dedired
 Actual Trajactory
-2
-1
0
1
2
-2
-1
0
1
2
y/m
x/m
 Dedired
 Actual Trajactory
 
Figure 6. Comparison of trajectory tracking performance: the left image with 
only NDO, and the right image with only DO. 
0
2
4
6
8
0.0
0.2
0.4
0.6
z/m
 Desired
 DO+NDO+SMC
 SMC
t(s)
 
Figure 7. Quadrotor z-direction time response. 
Figures 3 and 4 show the estimation of the equivalent 
disturbance by the nonlinear disturbance observer of the 
attitude loop and the disturbance observer of the position loop, 
respectively, from which it can be seen that both observers can 
estimate the disturbance effectively. From Figures 5 and 6, it 
can be seen that in the absence of an observer, the maximum 
error between the position of the quadcopter and the desired 
position is 0.23m , and there is a significant error in 
trajectory tracking compared to the desired trajectory. When a 
nonlinear disturbance observer is incorporated into the attitude 
loop, the position error of the quadcopter decreases to 0.19m , 
and the influence of disturbances on the UAV's attitude angles 
is reduced, leading to an improvement in trajectory tracking. 
Introducing a disturbance observer into the position loop while 
the attitude loop does not include a nonlinear disturbance 
observer results in a position error of 0.11m  for the 
quadcopter, indicating a noticeable attenuation of disturbances 
in the position loop by the observer. Finally, with both 
position and attitude loops equipped with observers, the 
position error decreases to 0.06m , significantly enhancing 
the control performance. Furthermore, from Figure 7, it can be 
observed that compared to relying solely on the sliding mode 
controller and compensating for disturbances with two 
observers, the final steady-state error is reduced from 
0.015m  to 0.003m . 
V. CONCLUSION 
This study proposes a hybrid control strategy integrating 
disturbance observer and sliding mode control to enhance the 
404
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:34:42 UTC from IEEE Xplore.  Restrictions apply.

## Page 8

robustness of quadrotor UAV trajectory control system against 
external disturbances. In this control strategy, a nonlinear 
disturbance observer is designed to estimate all unknown 
disturbances in the attitude control loop, while another 
disturbance observer is employed to estimate unknown 
disturbances in the position loop, effectively compensating the 
sliding mode controller via feedforward mechanism. The 
developed control scheme ensures smooth execution of 
attitude control tasks in diverse disturbance environments. 
Simulation results validate the effective disturbance estimation 
capability of the proposed disturbance observers and 
demonstrate significant reduction of disturbance effects on 
quadrotor 
UAV 
control 
system 
performance 
through 
feedforward compensation mechanism. The proposed hybrid 
controller effectively enhances the robustness and trajectory 
tracking precision of quadrotor UAVs. 
ACKNOWLEDGMENT 
The preferred spelling of the word “acknowledgment” in 
America is without an “e” after the “g”. Avoid the stilted 
expression, “One of us (R. B. G.) thanks . . .”  Instead, try “R. 
B. G. thanks”. Put sponsor acknowledgments in the unnum-
bered footnote on the first page. 
REFERENCES 
[1] Alkamachi A, Erçelebi E. （2017）Modelling and genetic algorithm 
based-PID control of H-shaped racing quadcopter.J. Arabian Journal for 
Science and Engineering, 42: 2777-2786. 
[2] Gong, X., Tian, Y., Bai, Y., & Zhao, C. (2012, August). Trajectory 
tacking control of a quad-rotor based on active disturbance rejection 
control. In:2012 IEEE International Conference on Automation and 
Logistics. Zhengzhou, China .pp. 254-259.  
[3] Peng, C., Tian, Y., Bai, Y., Gong, X., Zhao, C., Gao, Q., & Xu, D. (2013, 
June). ADRC trajectory tracking control based on PSO algorithm for a 
quad-rotor. In:2013 IEEE 8th Conference on Industrial Electronics and 
Applications (ICIEA). Melbourne, Australia  .pp. 800-805. 
[4] Yang, S., **, L., Gong, G., & Dong, H. (2020). Attitude Stabilization 
Control Method for Quadrotor UAV Based on ADRC. In: 
Communications, Signal Processing, and Systems: Proceedings of the 
2018 CSPS Volume III: Systems 7th . Singapore.pp. 836-844.  
[5] Gonzalez-Hernandez, I., Salazar, S., Lopez, R., & Lozano, R. (2016, 
June). Altitude control improvement for a Quadrotor UAV using integral 
action in a sliding-mode controller. In :2016 International Conference on 
Unmanned Aircraft Systems (ICUAS). Arlington, VA, USA .pp. 711-
716. 
[6] Shaik, M. K., & Whidborne, J. F. (2016, August). Robust sliding mode 
control of a quadrotor. In: 2016 UKACC 11th International Conference 
on Control (CONTROL). Belfast, UK .pp. 1-6.  
[7] Chen W H, Yang J, Guo L, et al．(2016) Disturbance-observer based 
control and related methods: an overview.J.IEEE Transactions on 
Industrial Electronics, 63 ( 2) : 1083-1095. 
[8] Sini, S., & Ananthan, T. (2022, March). A disturbance observer based 
control for quadrotor aircraft subject to wind gusts. In: 2022 IEEE 
International 
Conference 
on 
Signal 
Processing, 
Informatics, 
Communication and Energy Systems (SPICES) . India.pp. 491-496.  
[9] Guo K, Jia J, Yu X, et al. (2020) Multiple observers based anti-
disturbance control for a quadrotor UAV against payload and wind 
disturbances.J. Control Engineering Practice, 102: 104560. 
[10] Chen M, Chen W H. (2010) Sliding mode control for a class of uncertain 
nonlinear system based on disturbance observer.J. International journal 
of adaptive control and signal processing, 24(1): 51-64 
[11] Wang Z, Wu Z. (2015) Nonlinear attitude control scheme with 
disturbance observer for flexible spacecrafts.J. Nonlinear Dynamics , 81: 
257-264. 
[12] Yang J, Li S, Chen W H. (2012) Nonlinear disturbance observer-based 
control for multi-input multi-output nonlinear systems subject to 
mismatching condition.J. International Journal of Control , 85(8): 1071-
1082. 
[13] Xu, Y. T., Dong, R. Q., Huang, J., & Wu, A. G. (2021, July). Attitude 
Control for Rigid Spacecraft via Disturbance Observer based Terminal 
Sliding Mode Controller. In: 2021 40th Chinese Control Conference 
(CCC) . Shanghai, China.pp. 7803-7808.  
 
 
405
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on June 13,2025 at 04:34:42 UTC from IEEE Xplore.  Restrictions apply.
