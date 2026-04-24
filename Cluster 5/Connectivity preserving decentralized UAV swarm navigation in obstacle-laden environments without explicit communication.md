# Connectivity preserving decentralized UAV swarm navigation in obstacle-laden environments without explicit communication.pdf

## Page 1

Advanced Robotics
ISSN: 0169-1864 (Print) 1568-5535 (Online) Journal homepage: www.tandfonline.com/journals/tadr20
Connectivity preserving decentralized UAV swarm
navigation in obstacle-laden environments
without explicit communication
Thiviyathinesvaran Palani, Hiroaki Fukushima & Shunsuke Izuhara
To cite this article: Thiviyathinesvaran Palani, Hiroaki Fukushima & Shunsuke Izuhara
(2025) Connectivity preserving decentralized UAV swarm navigation in obstacle-laden
environments without explicit communication, Advanced Robotics, 39:6, 305-321, DOI:
10.1080/01691864.2025.2478920
To link to this article:  https://doi.org/10.1080/01691864.2025.2478920
Published online: 25 Mar 2025.
Submit your article to this journal 
Article views: 136
View related articles 
View Crossmark data
Citing articles: 4 View citing articles 
Full Terms & Conditions of access and use can be found at
https://www.tandfonline.com/action/journalInformation?journalCode=tadr20

## Page 2

ADVANCED ROBOTICS
2025, VOL. 39, NO. 6, 305–321
https://doi.org/10.1080/01691864.2025.2478920
FULL PAPER
Connectivity preserving decentralized UAV swarm navigation in obstacle-laden
environments without explicit communication
Thiviyathinesvaran Palani
a, Hiroaki Fukushima
a and Shunsuke Izuhara
b
aGraduate School of Engineering, Kyoto University of Advanced Science, Kyoto, Japan; bFaculty of Environmental, Life, Natural Science and
Technology, Okayama University, Okayama, Japan
ABSTRACT
This paper presents a novel control method for a group of UAVs in obstacle-laden environments
while preserving sensing network connectivity without data transmission between the UAVs. By
leveraging constraints rooted in control barrier functions (CBFs), the proposed method aims to over-
come the limitations, such as oscillatory behaviors and frequent constraint violations, of the existing
method based on artificial potential fields (APFs). More specifically, the proposed method first deter-
mines desired control inputs by considering CBF-based constraints rather than repulsive APFs. The
desired inputs are then minimally modified by solving a numerical optimization problem with soft
constraints. In addition to the optimization-based method, we present a non-optimization-based
method without numerical optimization. The effectiveness of the proposed methods is evaluated
by extensive simulations to compare the performance of the CBF-based methods with an APF-based
approach. Experimental results using real quadrotors are also presented.
ARTICLE HISTORY
Received 5 October 2024
Revised 23 December 2024
and 2 February 2025
Accepted 26 February 2025
KEYWORDS
Leader–follower navigation;
non-communicative; control
barrier function; connectivity
preservation; collision
avoidance
1. Introduction
The realm of robotics has witnessed significant advance-
ments through research on cooperative control of mul-
tiple robot systems, driving technological advancements
for a wide range of applications [1–3]. This paper focuses
on the fundamental problem of how to move a group of
robots as a whole to a target area. Specifically, we assume
that only one of the robots, called the leader, knows the
path to the target area. Thus, since each robot in the group
has a limited sensing and communication range, the con-
nectivity of the sensing/communication network must be
preserved to avoid leaving some robots behind. Further-
more, to move through cluttered environments including
narrow spaces without getting stuck, robots need to flexi-
bly change their network topology in a decentralized way
while preserving the network connectivity.
To overcome this problem and to deal with environ-
ments where no wireless network is available for infor-
mation exchange, Sakai et al. [4] proposed a method that
does not rely on data transmission between robots. This
method can change network topology by deactivating
certain network links to allow the robots to pass through
narrow spaces while enhancing active links in open areas
to maintain group cohesion. The method proposed in [5]
extended the approach from [4] for 2D environments to
cater to multiple UAVs in 3D environments. However,
CONTACT Hiroaki Fukushima
fukushima.hiroaki@kuas.ac.jp
the method proposed in [5] often suffers from oscillatory
movements and frequent constraint violations, which
could be a serious problem especially for UAVs. To over-
come these problems, we aim to develop a new algorithm
inspired by control barrier functions (CBFs), which have
extensively studied in recent years.
1.1. Related work
CBFs were initially introduced to deal with inequality
constraints for collision avoidance [6–12]. Then they
were also applied to various problems, including main-
taining connectivity [13–15], coverage mission [16],
energy autonomy [17, 18], transporting payloads [19, 20],
and herding animals that have strayed [21]. However, the
effectiveness of CBFs in the control problem focused in
this paper has not been fully studied. Since this paper
considers the connectivity aspects of a sensing network
without relying on data transmission in the presence of
obstacles – a departure from existing studies – we incor-
porate CBF constraints for preserving line-of-sight (LOS)
while maintaining maximum and minimum distances
between neighboring robots. Another feature of our con-
trol problem is the difficulty of determining desired
control inputs, given the dense and complex obstacle-
laden environments under consideration, particularly
© 2025 Informa UK Limited, trading as Taylor & Francis Group and The Robotics Society of Japan

## Page 3

306
T. PALANI ET AL.
because robots, except for the leader, do not know their
destination.
In complicated control problems with multiple CBF
constraints, optimization problems of control inputs are
not necessarily feasible. To deal with this problem, Bree-
den and Panagou [22] presented an iterative algorithm
to obtain a set of CBFs which ensure that the set com-
posed of those CBFs is a viability domain. Molnar and
Ames [23] proposed an algorithmic approach to formu-
late a single continuously differentiable CBF to capture
complex safety specifications by multiple CBFs. In this
paper, we directly impose multiple CBF constraints in an
optimization process, mirroring the approach taken in
many other studies [7, 8, 14, 15, 18, 20, 24]. The infeasi-
bility of the optimization problems is addressed through
a classical method using soft constraints [25]. A possible
future work is the incorporation of more sophisticated
CBF construction algorithms, such as those outlined
in [22, 23], into our control method.
While these CBF-based methods resolve a numerical
optimization problem at each time step, many control
methods for multi-agent systems adopt simple control
algorithms without solving numerical optimization [4,
5, 26–30]. These methods determine control inputs
through a simple combination of repulsive and attractive
actions based on artificial potential fields (APFs) consid-
ering constraints among robots and obstacles. However,
as suggested in [10], APF-based methods tend to suffer
from more oscillations than CBF-based methods. Thus,
one important research direction is how to construct sim-
ple control algorithms without solving numerical opti-
mizations while taking advantage of CBFs capable of gen-
erating smooth behaviors. However, control algorithms
that incorporate CBFs into these simple approaches for
maneuvering through obstacle-laden environments have
not been fully studied.
1.2. Contribution
In this paper, we propose a novel CBF-based control
method for coordinating a group of robots in obstacle-
laden environments while preserving the connectivity of
the sensing network without data transmission between
robots. In this method, CBF constraints are constructed
to preserve LOS integrity in addition to the maximum
and minimum separation distances between neighboring
robots. This design is necessary to uphold the connectiv-
ity of a sensing network without data transmission in the
presence of obstacles, unlike existing CBF control meth-
ods [6–21]. Furthermore, unlike the existing method [5]
based on APFs, the desired inputs are determined based
on the CBF constraints to mitigate oscillatory movements
and frequent constraint violations for UAVs.
In addition to the optimization-based method, we
present a non-optimization-based method that does not
rely on numerical optimization. While CBFs are expected
to improve oscillatory behaviors, they entail higher com-
putational costs to solve numerical optimization prob-
lems. Thus, it is practically important to investigate sim-
ple CBF-based algorithms without solving numerical
optimization problems.
We perform extensive simulations to compare the per-
formance of the proposed CBF-based methods against
an APF-based method, considering aspects such as
constraint violations, computation time, and oscillation
of responses. Simulation results show that both the
optimization-based and non-optimization-based meth-
ods generate fewer oscillatory responses and constraint
violations than an APF-based method. Experimental
results using real quadrotors are also shown.
A preliminary version of this work was presented
in [31]. In this paper, we present a new non-optimization-
based method that does not necessitate the iterative mod-
ification of input, as outlined in [31]. The optimization-
based method is also introduced alongside intensive sim-
ulation results to compare the performance of the pro-
posed CBF-based methods (the optimization-based and
non-optimization-based methods) against an APF-based
method.
2. Problem formulation
We consider a group of N homogeneous robots that
operate in a 3D environment containing stationary obsta-
cles. Our control algorithm is constructed based on the
assumption that the movement of the ith robot (i =
1, 2, . . . , N) is described by the following second-order
system:
˙xi = vi,
˙vi = ui,
∥ui∥≤η,
(1)
where xi ∈Rn, vi ∈Rn, and ui ∈Rn are the position,
velocity, and control input of robot i, respectively. The
inclusion of a positive constant η > 0 in the input con-
straint accounts for hardware limitations.
We assume that a sufficient condition for collision
avoidance between robots i and j is given as follows:
∥xi −xj∥≥dc,
∀j ∈V \ {i},
(2)
where V := {1, 2, . . . , N} is the set of indices of all robots.
Although a robot is modeled as a point in (1), the param-
eter dc in (2) must be determined by taking into account
the size of the actual robots. We also assume that a

## Page 4

ADVANCED ROBOTICS
307
sufficient condition for obstacle avoidance is given as
∥xi −xo∥≥do,
∀xo ∈O,
(3)
where O is a set of all points on obstacles in the
workspace.
To describe the sensing model, we first define the line
segment joining p and q as
L(p, q) := {(1 −λ)p + λq, ∀λ ∈[0, 1]}.
(4)
We then assume that robot i can sense the position and
velocity of robot j ∈V \ {i} if the following conditions are
satisfied
∥xj −xi∥≤ds,
(5)
∥q −xo∥≥dls,
∀q ∈L(xi, xj),
∀xo ∈O.
(6)
The condition in (5) implies that the maximum sensing
range is given by a positive number ds. The condition
in (6) implies that the distance from L(xi, xj) to each
obstacle is at least the minimum clearance dls, ensuring
that obstacles do not interrupt the LOS between robots i
and j. We also assume that robot i can detect a point on
an obstacle xo ∈O, if
∥xo −xi∥≤ds,
(7)
∥xo −xi∥≤∥q −xi∥,
∀q ∈¯L(xi, xo) ∩O,
(8)
where ¯L(xi, xo) := {(1 −λ)xi + λxo, ∀λ ≥0}. While the
set L(xi, xo) includes only points between xi and xo, the
set ¯L(xi, xo) includes points behind xo along the line from
xi to xo, in addition to the points in L(xi, xo). Thus, the
condition in (8) implies that no other point on an obstacle
is closer to xi than xo on L(xi, xo). We denote Oi(t) as the
set of points on obstacles detected by robot i at time t.
In terms of the sensing described above, we rep-
resent the network topology of the multi-robot sys-
tem using a graph Gs(x(t)) = (V, Es(x(t))) where x :=
[x1, x2, . . . , xN]. We denote V and Es(x(t)) as the node
set and edge set, respectively. The elements of Es(x(t)) are
pairs of robot indices that can sense each other’s positions
at time t. A connected graph Gs implies that, for every pair
of nodes, there exists a path from one node to the other.
We assume that a target path is given only to the leader
of the N robots, whose index is set as N without loss of
generality. The remaining robots i (= 1, 2, . . . , N −1) are
called followers. Each follower is presumed to be unaware
of whether another robot serves as the leader. If Gs is
connected, a pathway exists between the leader and each
follower. Thus, since the maximum length of each link of
Gs is kept to no more than a given finite value ds, each fol-
lower is forced to follow the leader at a certain distance
(at most (N −1)ds). Furthermore, reducing the length
of the link to below ds allows for a decrease in the dis-
tance between the leader and a follower. Thus, in this
paper we aim to preserve the connectivity of the following
subgraph of Gs(x(t)),
Gm(x(t)) := (V, Em(x(t))),
Em(x(t)) := {(i, j) ∈Es(x(t)) | ∥xi(t) −xj(t)∥≤¯dm},
(9)
where dc < ¯dm < ds. Then, the neighbors of robot i are
defined as
Ni(x(t)) := {j | (i, j) ∈Em(x(t))}.
(10)
From the definition of Gm(x(t)), the connectivity of Gs is
preserved if that of Gm(x(t)) is preserved.
We assume that Gm is connected at the initial time
t = 0. Thus, the simplest way to preserve connectivity is
to control the robots such that the edges of Gm at t = 0
are not lost. However, in obstacle-laden environments,
it is often necessary to change the network topology to
facilitate navigation through a narrow space. Thus, it is
necessary to select edges to be maintained such that the
connectivity of Gm is preserved. To describe the edges to
be preserved, we define the symmetric indicator func-
tion σij(t) = σji(t) ∈{0, 1}. If σij = 1, there will be an
effort to preserve the edge (i, j). Essentially, robot i aims
to preserve the link to robot j in the following set:
N σ
i (x(t)) := {j ∈Ni(t) | σij(t) = 1}.
(11)
We also define the following subgraph of Gm(x(t)) as
Gσ(x(t)) := (V, Eσ(x(t))),
(12)
Eσ(x(t)) := {(i, j) ∈Em(x(t)) | σij(t) = 1}.
(13)
By ensuring that σij is set in a manner that renders
Gσ connected, the connectivity of Gm is maintained by
orchestrating the movement of the robots to avoid any
loss of edges within Gσ.
We propose an algorithm to compute ui in a manner
that upholds the connectivity ofGm, while adhering to the
collision avoidance conditions in (2) and (3). However,
when applied to UAVs, it is difficult to avoid constraint
violations completely due to modeling errors and distur-
bances, especially when multiple constraints are imposed
severely. Thus, for the constants satisfying dm < ¯dm, dc >
dc, do > do, and dls > dls, we control the robots so as to
satisfy the following constraints:
(i) The maximum distance constraint
∥xi −xj∥≤dm,
∀j ∈N σ
i (t).
(14)

## Page 5

308
T. PALANI ET AL.
(ii) The inter-robot collision avoidance constraint
∥xi −xj∥≥dc,
∀j ∈Ni(t).
(15)
(iii) The obstacle avoidance constraint
∥xi −xo∥≥do,
∀xo ∈Oi(t).
(16)
(iv) The LOS preservation constraint for each j ∈N σ
i (t)
∥q −xo∥≥dls,
∀xo ∈O,
∀q ∈L(xi, xj).
(17)
If all of these constraints are satisfied at time t, the
state is referred to as Normal mode. On the other hand,
if one or more constraints are violated at t, we use a
different control law to recover from the constraint vio-
lation, referred to as Recovery mode. In this paper, we
focus mainly on Normal mode and propose new control
methods based on CBFs.
3. Constraints based on CBFs
In this section, we derive CBF-based constraints used in
the proposed methods in the same way as in [7], after
summarizing the motivation to use them instead of APFs.
3.1. Motivation
To explain the motivation to use CBF-based constraints,
we describe a limitation of the APF-based approach used
in [4, 5].
For the constraints in (14) and (15), the following
repulsive APF is used in [4, 5],
col
i
(x) =

j∈N σ
i
col(∥xi −xj∥),
col(z)
:=
(z −dr)2(dm −z)
(dm −dc)2(z −dc) + (dr −dc)2(dm −z)/κ1
+
(z −dc)(z −dr)2
(dm −dc)2(dm −z) + (z −dc)(dm −dr)2/κ2
(18)
where κ1 and κ2 are design parameters whose values
are equivalent to col(z) at z = dc and z = dm, respec-
tively. Figure 1 illustrates an example of col(z) for dc =
0.3, dr = 0.7, dm = 1.0, κ1 = κ2 = 10. As the example
shows, col(z) at the minimum value at the desired
relative distance dr, and monotonically increases as z
approaches the maximum allowable distance dm or the
minimum allowable distance dc. Similarly, for the con-
straints in (16) and (17), repulsive APFs increase as the
Figure 1. Example of col(z) (dc = 0.3, dr = 0.7, dm = 1.0).
distance decreases towards the minimum limits do and
dls, respectively.
A limitation of the APF-based approach is that almost
no action is taken when the distance is far from the max-
imum and minimum limits, irrespective of how high the
robot’s speed in advancing towards a limit. As a result,
if the velocity aimed at reaching a constraint bound-
ary becomes too high, the constraint is violated even if
the maximum allowable repulsive acceleration is applied
near the constraint boundary to avoid violation. Fur-
thermore, the repulsive acceleration is large when the
distance is close to the maximum and minimum limits,
irrespective of how slow the robot is moving towards the
constraint boundary. Thus, when the robot approaches a
constraint boundary slowly, an excessively strong repul-
sive force is applied, which causes oscillatory behaviors.
Although a damping filter was used to suppress oscilla-
tions in [5], this approach does not address the root cause
of the problem. In other words, such a damping filter
increases the risk of constraint violations by potentially
eliminating essential actions required to avoid constraint
violations. On the other hand, CBF-based methods con-
sider velocity constraints depending on the proximity to
their limits, as described in Section 3.2.
3.2. Formulation of CBF constraints
For a constraint h(x) ≥0 to the position vector of robots,
x, CBF-based methods consider the following derivative
condition,
˙h(x, v) = ∇h(x)T ˙x = ∇h(x)Tv ≥−κ(h(x)),
(19)
where v := [v1, v2, . . . , vN]T, and κ(·) is an extended class
K function. In other words, the lower limit of ˙h(x, v)
is 0 when the constraint reaches its minimum limit,
h(x) = 0, and diminishes further as the distance from the

## Page 6

ADVANCED ROBOTICS
309
limit increases. Thus, this constraint aims to prevent high
speeds of h(x) towards the limit, h(x) = 0.
The constraint in (15) for collision avoidance between
robots can be described as
hc
ij(x) := ∥xi −xj∥−dc ≥0,
∀j ∈Ni.
(20)
To keep this constraint, we can obtain the following
derivative condition in a manner similar to (19) for
κ(hc
ij) = αchc
ij.
Gc
ij(x, v) := ˙hc
ij(x, v) + αchc
ij(x) ≥0,
∀j ∈Ni,
(21)
where
˙hc
ij(x, v) =

∇xihc
ij(x)
T
vi +

∇xjhc
ij(x)
T
vj.
(22)
Several approaches [7, 12, 32, 33] are available to deal
with derivative conditions which do not include the
control input as in (21). In this paper, we adopt the
approach in [7], considering a safety margin determined
by the maximum braking acceleration, as described
below. Comparing the control performance with other
approaches is a potential area for future exploration.
Considering a safety margin based on the maximum
relative deceleration 2η, the constraint in (20) is modified
as
hc
ij(x) + ¯vji(t)Tij + 2
 Tij
0
ητ dτ ≥0,
(23)
where ¯vji(t) :=
xT
ji (t)
∥xji(t)∥vji(t), xji := xi −xj, vji := vi −vj,
and Tij := 0−¯vji(t)
2η
.
When both robots i and j apply the maximum decel-
eration, the relative velocity ¯vji(t + Tij) = ¯vji(t) −2ηTij
diminishes to 0. From (23), a constraint ¯hc
ij(x, v) ≥0 is
obtained, where
¯hc
ij(x, v) :=

4ηhc
ij(x) +
xT
ji
∥xji∥vji.
(24)
Then, a derivative condition can be derived for (24) as
follows,
xT
ji uji + bc
ij ≥0,
(25)
where
bc
ij := αc(¯hc
ij)3∥xji∥−(¯vji)2 + ∥vji∥2 +

η
hc
ij
vT
ji xji. (26)
Based on (25), the following distributed constraint is
proposed in [7],
xT
ji ui + bc
ij/2 ≥0,
(27)
−xT
ji uj + bc
ij/2 ≥0.
(28)
Thus, the constraint for ui to adhere to the constraint
in (15) is described as
Ac
ijui + bc
ij/2 ≥0,
∀j ∈Ni,
(29)
where Ac
ij := xT
ji . Similarly, a CBF-based constraint to
maintain the constraint in (14) is described as
Gm
ij (x, v) := ˙hm
ij (x, v) + αmhm
ij (x) ≥0,
∀j ∈N σ
i ,
(30)
for hm
ij (x) := dm −∥xi −xj∥and a positive constant αm.
A similar constraint to (29) is derived as
Am
ij ui + bm
ij /2 ≥0,
∀j ∈N σ
i ,
(31)
where Am
ij := −xT
ji , and
bm
ij := αm(¯hm
ij )3∥xji∥+ (¯vji)2 −∥vji∥2 −

η
hm
ij
vT
ji xji,
¯hm
ij (x, v) :=

4ηhm
ij (x) −
xT
ji
∥xji∥vji.
(32)
For the obstacle avoidance constraint in (16), a CBF-
based constraint is described as
Gob
io (xi, xo, vi) := ˙hob
io (xi, xo, vi) + αobhob
io (xi, xo) ≥0,
(33)
for hob
io (xi, xo) := ∥xi −xo∥−do and a positive constant
αob. A modified constraint including ui is obtained as
Aob
io ui + bob
io ≥0,
(34)
where Aob
io := xT
oi, xoi := xi −xo, and
bob
io := αob(¯hob
io )3∥xoi∥−(vT
i xoi)2
∥xoi∥2 + ∥vi∥2 +

2η
hob
io
vT
i xoi,
¯hob
io (xi, xo, vi) :=

2ηhob
io (x) +
xT
oi
∥xoi∥vi.
(35)
For implementation, it is not realistic to consider the con-
straint in (34) for each xo ∈Oi(t). Therefore, we consider
the constraints in (34) for the nearest obstacle points from
robot i as described in Section 4.2.
In Section 3.3, we derive a CBF-based constraint to
keep the constraint in (17) for LOS preservation.
3.3. Constraints for LOS preservation
In the same way as in the case of (34), constraints for LOS
preservation are derived for the nearest obstacle point x∗
ijo
from the LOS line.

## Page 7

310
T. PALANI ET AL.
The position xq of the point q projected from x∗
ijo onto
the LOS between i and j, as shown in Figure 2, is described
as
xq := (1 −λ∗)xi + λ∗xj,
λ∗:=
(xi −x∗
ijo)Txji
∥xji∥2
, (36)
where x∗
ijo is the nearest obstacle point from L(xi, xj). For
xoq := xq −x∗
ijo, hls
ijo(x, x∗
ijo) := ∥xoq∥−dls, and a posi-
tive number αls, we consider the following CBF-based
constraint,
Gls
ijo(x, x∗
ijo, v) := ˙hls
ijo(x, x∗
ijo, v) + αlshls
ijo(x, x∗
ijo) ≥0,
∀j ∈N σ
i .
(37)
We define the velocity of point q as
vq := (1 −λ∗)vi + λ∗vj,
(38)
and its projection onto xoq as
¯voq :=
xT
oq
∥xoq∥vq.
(39)
In the same way as in (23), we consider the following con-
straint accounting for a safety margin in a scenario where
both robots i and j change the velocity of the LOS towards
x∗
ijo from ¯voq to 0 using the maximum deceleration η.
hls
ijo(x, x∗
ijo) + ¯voq(t)Tqo +
 Tqo
0
ητ dτ ≥0,
(40)
where Tqo := 0−¯voq(t)
η
. From (40), a constraint ¯hls
ijo
(x, x∗
ijo, v) ≥0 is obtained, where
¯hls
ijo(x, x∗
ijo, v) :=

2ηhls
ijo +
xT
oq
∥xoq∥vq.
(41)
A derivative condition can be derived for (41) as follows,

∇vi ¯hls
ijo
T
ui +

∇vj ¯hls
ijo
T
uj + bls
ijo ≥0,
(42)
where bls
ijo := (∇xi ¯hls
ijo)Tvi + (∇xj ¯hls
ijo)Tvj + αls(¯hls
ijo)3.
The constraint in (42) is distributed as follows:

∇vi ¯hls
ijo
T
ui + λ∗bls
ijo ≥0,
(43)

∇vj ¯hls
ijo
T
uj + (1 −λ∗)bls
ijo ≥0.
(44)
Thus, the constraint for robot i to maintain the LOS
preservation constraint in (17) is described as
Als
ijoui + λ∗bls
ijo ≥0,
(45)
where Als
ijo := (∇vi ¯hls
ijo)T.
Figure 2. Relative position and velocity between robots i and j,
and illustration of point q on LOS.
4. Control algorithm
The outline of the control algorithm for robot i is
described as follows.
Step 1: The indicator function σij(t) for all j ∈Ni(t) is
determined to select links in Gm to be preserved.
Step 2: The desired control input is determined by
considering the CBF-based constraints and APFs.
Step 3: If the desired control input violates CBF-based
constraints, it is minimally modified to obtain the actual
control input ui.
Each step of the algorithm is described in detail in
the following subsections. In Step 1, we use the same
algorithm as in [5]. The main difference from [5] is that
the CBF-based constraints described in Section 3 are
used in Steps 2 and 3 instead of APFs.
4.1. Link management (Step 1)
The purpose of link management is to achieve a slen-
der swarm shape with fewer links between robots when
navigating narrow passages and to enable the swarm to
navigate through dense obstacle-laden environments. To
achieve a slender shape with fewer links between robots,
it is necessary to deactivate some of the redundant edges
in the formation graph Gm. To avoid leaving some robots
behind, this deactivation process needs to be performed
while preserving connectivity. In this paper, we adopt
simple rules proposed in [4, 5] to deactivate edges in
a decentralized manner without data transmission, as
described below. See [4] for theoretical analysis on con-
nectivity preservation of Gσ after these decentralized
deactivation rules are applied.
The region Dij is defined for xi and xj, as shown in
Figure 3, to describe the link deactivation rule,
Dij := {q | (q −xi)Txij > 0, (q −xj)Txij < 0}.
(46)

## Page 8

ADVANCED ROBOTICS
311
Figure 3. 2D illustration of Dij and ∥ϕ(xik, xij)∥.
Furthermore, a projection function ϕ(p, q) is employed
to project the vector p onto the plane perpendicular
to vector q. The projection function can be defined as
follows,
ϕ(p, q) := p −pTq
∥q∥2 q.
(47)
As shown in Figure 3, the distance between xk and the
line connecting xi and xj can be computed as ∥ϕ(xik, xij)∥.
If robots i, j, and k satisfy the following condition, then
the link (i, j) ∈Em is deactivated:
∥ϕ(xik, xij)∥≤ddel, xk ∈Dij,
(i, j) ∈Em, (j, k) ∈Em, (k, i) ∈Em,
(48)
where ddel is a positive constant satisfying ddel < dc sin π
3 .
Another rule is that if only one edge of a connected
robot triangle has a length of dm, then that edge will be
deactivated. Specifically, the link (i, j) will be deactivated
if robots i, j, and k satisfy the following condition,
dm −δm < ∥xij∥≤dm, ∥xkj∥< dm −δm,
∥xik∥< dm −δm, (i, j) ∈Em, (j, k) ∈Em, (k, i) ∈Em,
(49)
where δm is a small positive number relative to dm. In
summary, σij is defined as follows:
σij =

0,
if (48) or (49)
1,
otherwise
.
(50)
4.2. Desired control input calculation ( Step 2 )
Since the leader is given a target path, the desired control
input for the leader is determined to follow that path. In
simulations and experiments, the following simple con-
troller is used for a sequence of waypoints on the target
Table 1. Description of acceleration components.
am
i
Acceleration to enforce maximum link length
ac
i
Acceleration to avoid collision with robots
aob
i
Acceleration to avoid collision with obstacles
als
i
Acceleration to preserve LOS between robots
ada
i
Acceleration to avoid deadlock
aag
i
Acceleration to make the group more cohesive
path:
aN = kp(xwp −xN),
kp > 0,
(51)
where xwp is the next waypoint on the target path.
Determining desired inputs for the follower robots is
more challenging because they do not have knowledge
of the target path. The desired control input for follower
robots, ai, is expressed by the following equation,
ai = acon
i
+ ada
i
+ aag
i ,
(52)
where acon
i
has four components as follows,
acon
i
= am
i + ac
i + aob
i + als
i .
(53)
The significance of each component in (52) and (53) is
elucidated in Table 1. It should be noted that although
CBF-based constraints are imposed in Step 3, acon
i
in Step
2 is necessary for the following reasons: First, merely sat-
isfying the given constraints in Step 3 is not enough for
robots to pass through narrow spaces without getting
stuck even if the link deactivation in Step 1 is applied.
Second, robots move extremely slowly without acon
i
. Since
Step 3 makes only the minimum change to a desired
input ai in (52) so as to satisfy the CBF-based con-
straints, distances between robots tend to become close
to the maximum limit so that the leader needs to wait
for the followers to satisfy the maximum distance con-
straint. Thus, the purpose of acon
i
is not only to satisfy the
constraints but also to generate accelerations to move fol-
lowers towards the leader without getting stuck in narrow
spaces.
In the previous work [5], desired inputs were deter-
mined by employing repulsive APFs based on speci-
fied constraints and an attractive APF to foster group
cohesion. However, the repulsive APFs caused oscilla-
tory behaviors in the desired inputs, as mentioned in
Section 3.1. In this paper, we use repulsive functions
based on CBFs to compute acon
i
instead of APFs.
The acceleration component am
i is determined using
the following repulsive force to satisfy the constraint
in (30)
am
i = 1
nσ
i

j∈N σ
i
ωm(Gm
ij ) ∇viGm
ij ,
(54)

## Page 9

312
T. PALANI ET AL.
Figure 4. Example of ωm(z) for μm = 1, βm = 0.1.
where nσ
i denotes the cardinality of the set N σ
i , and ωm
is defined as
ωm(z) :=
μm βm
|z| + z + βm
,
μm > 0, βm > 0.
(55)
Figure 4 illustrates an example of the function ωm(z) for
μm = 1, βm = 0.1. Here, the variable μm establishes the
maximum value of the function, while βm determines the
rate at which ωm(z) decreases for z ≥0. The purpose of
am
i in (54) is to increase Gm
ij when the constraint Gm
ij ≥0
in (21) is violated (Gm
ij < 0) or on the verge of violation
(Gm
ij ≃0). From (21), we have
˙Gm
ij (x, v, ui, uj) = (∇xiGm
ij )Tvi + (∇viGm
ij )Tui
+ (∇xjGm
ij )Tvj + (∇vjGm
ij )Tuj.
(56)
To increase Gm
ij , ui must make the second term of ˙Gm
ij
a positive large value. If ui = am
i is applied, the second
term is positive except in the case of ∇viGm
ij = 0. Fur-
thermore, the weighting coefficient ω(Gm
ij ) becomes large
when Gm
ij < 0 or Gm
ij ≃0 as shown in Figure 4 so that the
second term of ˙Gm
ij becomes large.
Similarly, ac
i is determined through the following
repulsive force to satisfy (21)
ac
i = 1
ni

j∈Ni
ωc(Gc
ij) ∇viGc
ij,
(57)
using ωc(z) defined in the same way as (55) for constants
μc and βc. ni denotes the cardinality of set Ni.
To define aob
i , we specify the set Oob
i
comprising the
nearest obstacle points detected from robot i,
Oob
i
= argmin
xo∈Oi
∥xi −xo∥.
(58)
The accelerations to avoid collision with obstacles is
determined by:
aob
i
= 1
nob
i

xo∈Oob
i
ωob(Gob
io ) ∇viGob
io .
(59)
where ωob(z) is defined in the same way as in (55) for
constants μo and βo.
To elaborate on the term als
i , we define the set LSi,
which represents the neighboring robot and the corre-
sponding obstacle that are nearest to the boundary of the
LOS preservation condition in (17), defined as follows:
LSi =
argmin
j∈N σ
i , xo∈Oi∩Dij
∥ϕ(xio, xij)∥.
(60)
The acceleration to preserve LOS is determined by the
following equation,
als
i = 1
nls
i

(j,x∗
ijo)∈LSi
ωls(Gls
ijo) ∇viGls
ijo.
(61)
A deadlock situation may occur when three robots
forming an isosceles triangle move into a narrow space, as
illustrated in Figure 5. In this scenario, the robots cannot
find the correct link to deactivate without losing connec-
tivity; thus the group will get stuck without being able to
enter into the narrow space. To prevent this situation, the
longest edge of the triangle formed by the three robots is
made longer than the other edges. To further address this
issue, we introduce an acceleration component, ada
i , that
aims to extend the longest edge of a triangle consisting of
robot triplets i, j, and k. Specifically, if there is an obstacle
between either (i, j) ∈Em or (j, k) ∈Em, and (i, k) ∈Em,
and ∥xji∥> ∥xjk∥> dc + δc, dc + δc > ∥xik∥> dc, then
robot i will generate an acceleration to extend the longest
edge (i, j) of the triangle further than the other edges. We
denote the set of robots j corresponding to long edges as
DAi. To enforce the deadlock avoidance constraint, the
acceleration ada
i
is determined as
ada
i
= βda
nda
i

j∈DAi
xji
∥xji∥,
βda > 0,
(62)
where nda
i denote the cardinality of set DAi. The acceler-
ation component ada
i
will generate an acceleration when
the lengths of the two longest links in a robot triplet con-
verge towards equal lengths, thereby averting the isosce-
les triangle shape.
To maintain cohesion among the robots, we introduce
the following attractive APF ag
i (x), which promotes
cohesion among the robots in the absence of obstacles.
ag
i (x) =
1
ncoh
i

j∈Si\N σ
i
φcoh(∥xji∥)

## Page 10

ADVANCED ROBOTICS
313
Figure 5. 2D illustration of deadlock isosceles triangle.
+

(j,k)∈CBi
φcb(∥ϕ(xij, xkj)∥),
(63)
φcoh(z) =
⎧
⎨
⎩
1
2(z −dm)2,
z > dm, Oi = ∅
0,
otherwise
,
(64)
CBi = {(j, k) ∈N σ
i | ∥xkj∥> dm},
(65)
φcb(z) =
⎧
⎨
⎩
(ddel + δdel −z)2
2
,
z < ddel + δdel, Oi = ∅
0,
otherwise.
(66)
The φcoh component of ag
i motivates robot i to approach
the robots within its sensing range, denoted by the set Si.
This cohesive behavior is achieved by minimizing the dis-
tance between robot i and the robots in Si \ N σ
i , which
represents the set of robots that have a direct LOS to robot
i but are not included in N σ
i . The cardinality of Si \ N σ
i
denoted as ncoh
i
. On the other hand, the φcb component of
ag
i
disrupts the straight-line formation between robot i
and its neighboring robots, facilitating the quick creation
of links to them and establishing new LOS for them. The
φcb component is defined based on the distance between
robot i and the nearest point on the line L(xj, xk), where
ddel + δdel represents the intended distance margin for
establishing new LOS. The CBi set is used to determine
the φcb component of the APF, encompassing the pair of
robots linked with robot i and separated by a distance
greater than the maximum link distance dm. The accel-
eration to enforce aggregation is determined as follows,
where βag is a design constant,
aag
i
= −βag∇xiag
i (x).
(67)
Overall, the APF ag
i (x) enables the follower robots
to gather around the leader robot, thus preventing the
swarm from dividing and allowing for better coordina-
tion among all robots.
4.3. Verification of constraint enforcement ( Step 3 )
For the desired input ai determined in Step 2, the con-
trol input ui is calculated by solving a numerical opti-
mization problem considering the given CBF constraints.
Since multiple constraints are severely imposed in our
control problem, the control input satisfying all the con-
straints does not necessarily exist. In this paper, a classical
approach utilizing soft bounds [25] is adopted to ensure
the feasibility of the optimization problem.
To describe the optimal control problem in a compact
form, we describe the CBF-based constraints in Section 3
as follows:
Aui + b ≥0,
(68)
where the inequality of each row is one of the constraints
in (29), (31), (34), and (45).
Robot i (= 1, . . . , N) determines ui by solving the
following optimization problem at each time step,
min
ui∈Rn, ϵ∈R {∥ui −ai∥2 + ρϵ}
subject to
Aui + b + ϵ1 ≥0,
∥ui∥≤η,
ϵ ≥0,
(69)
where 1 is a vector with all entries being one, and ϵ
is a slack variable which is non-zero only if the con-
straint in (68) is violated. Thus, ϵ indicates the amount
of constraint violation. By heavily penalizing ϵ in the cost
function using a large weight ρ > 0, the optimal solution
to the problem in (69) tries to minimize constraint vio-
lations as much as possible. This optimization is reduced
to a semi-definite programming problem and thus can be
solved efficiently.
4.4. Recovery control
In Step 3 of the algorithm, we relax the CBF-based con-
straints to obtain a control input. This relaxation may lead
to violations of the original position-based constraints
defined in Section 2. To address this issue, a recovery con-
trol law is introduced to manage constraint violations and
return the robot to a safe zone. The recovery control law
is activated when one or more constraints are violated. In
such cases, the control input for the robot is determined
solely by computing acceleration for the violated con-
straints, disregarding the other acceleration components.
More specifically, the recovery control input is computed
as follows,
ui = ar
i −krvi,
(70)
ar
i = cmamr
i
+ ccacr
i + cobaobr
i
+ clsalsr
i ,
(71)

## Page 11

314
T. PALANI ET AL.
amr
i
=

j∈Rm
i
∥xij∥−dm
¯dm −dm
xij
∥xij∥,
(72)
acr
i =

j∈Rc
i
∥xij∥−dc
dc −dc
xij
∥xij∥,
(73)
aobr
i
=

xo∈Rob
i
∥xio∥−do
do −do
xio
∥xio∥,
(74)
alsr
i
=

(j,x∗
ijo)∈Rls
i
∥xqo∥−dls
dls −dls
xqo
∥xqo∥,
(75)
xqo = −ϕ(x∗
ijo −xi, xij),
(76)
where cm > 0, cc > 0, cob > 0, cls > 0 are weights assig
ned for each recovery acceleration component. Here, Rm
i
denotes the robots that violate condition (14), while Rc
i
refers to robots in violation of condition (15). The set
Rob
i
includes obstacle points that breach condition (16),
and Rls
i comprises both robots and the corresponding
obstacle points that violate the LOS constraint specified
in (17).
5. Non-optimization-based method
Although the method in Section 4 requires to solve a
numerical optimization problem at each time step in Step
3, robots may not always possess sufficient computational
capacity for this task in some cases. Thus, many control
methods for multi-agent systems adopt simple control
algorithms without solving numerical optimization [4,
5, 26–30]. These methods determine control input by
employing a combination of repulsive and attractive
acceleration components based on APFs. In other words,
high priority is given to constraints with large repul-
sive acceleration, while constraints with small repulsive
acceleration are ignored.
In this section, we presents a new non-optimization-
based method based on CBF constraints. The proposed
method is based on a combination of repulsive and attrac-
tive acceleration components in the same way as in the
existing methods [4, 5, 26–30]. A significant difference
from those existing methods is that repulsive accelera-
tion components are constructed using CBF-based con-
straints rather than APFs. More specifically, the proposed
non-optimization-based method determines the direc-
tion of the control input using ai in (52), which is the
sum of repulsive and attractive acceleration components.
Then, the magnitude of the control input is adjusted, as
follows:
ui = λ ai
∥ai∥,
λ ∈[0, η].
(77)
For the rth row of the constraint in (68), Arui + br ≥0,
we determine an allowable region [λmin
r
, λmax
r
] depend-
ing on situations as follows:
Case 1 : Ar ai
∥ai∥≥0 and br ≥0.
In this case, λ can take any positive value as
the condition will always be satisfied. Thus, the
limits are set as λmin
r
= 0, λmax
r
= η.
Case 2 : Ar ai
∥ai∥< 0 and br ≥0.
In this case, the constraint will be satisfied for
λ ≤−br∥ai∥
Arai . Thus, the limits are set as λmin
r
=
0, λmax
r
= −br∥ai∥
Arai .
Case 3 : Ar ai
∥ai∥≤0 and br < 0.
In this scenario, the inequality cannot be sat-
isfied for a non-negative λ. Since there is no
choice other than to ignore this constraint, the
limits are set as λmin
r
= 0, λmax
r
= η.
Case 4 : Ar ai
∥ai∥> 0 and br < 0.
In this case, the constraint will be satis-
fied for λ ≥−br∥ai∥
Arai . Thus, if η < −br∥ai∥
Arai ,
the limits are set as λmin
r
= 0, λmax
r
= η, since
this constraint cannot be satisfied for λ ∈
[0, η]. Otherwise, the limits are set as λmin
r
=
−br∥ai∥
Arai , λmax
r
= η.
To determine λ in (77), we use the following λmin and
λmax
λmin := max
r
λmin
r
,
(78)
λmax := min
r
λmax
r
.
(79)
If λmin ≤λmax, it is easy to determine λ depending on the
∥ai∥. On the other hand, λmax < λmin implies that con-
straints in Cases 2 and 4 conflict with each other. In such
cases, we ignore λmin for the following reason: The value
of λmin is typically large when the difference between
the direction of ai and a repulsive acceleration of con-
straints in Case 4 is large. Since we prioritize constraints
with repulsive forces in directions similar to ai, the pri-
ority of constraints in Case 4 with a large λmin is low.
Therefore, we ignore λmin if λmax < λmin. In summary,
we determine λ as follows:
λ =
⎧
⎪⎨
⎪⎩
λmax,
∥ai∥≥λmax
λmin,
∥ai∥< λmin ≤λmax
∥ai∥,
otherwise.
(80)
Note that this method ignores constraints which are not
satisfied by a positive multiple of ai as in (77). Then, λ
in (80) is selected so that ∥ui −ai∥is minimized sub-
ject to the allowable region λmin ≤λ ≤λmax for the
constraints that are not ignored.

## Page 12

ADVANCED ROBOTICS
315
Table 2. Parameters used in the simulation.
ds
¯dm
dm
dc
dc
do
do
2
1.9
1
0
0.1
0
0.1
dls
dls
ddel
δm
δdel
αm
αc
0
0.05
0.05
0.05
0.05
0.1
0.1
αob
αls
βm
βc
βob
βls
βda
0.4
0.2
0.01
0.01
0.001
0.001
0.01
βag
ρ
cm
cc
cob
cls
η
0.5
106
1
1
0.4
0.5
1
6. Simulations
We applied the proposed method to a quadrotor model
given in [34] with inner-loop PD controllers for atti-
tude and velocity. The simulations were run on a com-
puter with an Intel Core i9 12900k processor, 32 GB
of RAM, and an NVIDIA GeForce RTX 3090 graph-
ics card. The control input was computed at intervals of
t = 0.1 s, and the system parameters were set as listed
in Table 2. The control input ui determined by the pro-
posed method was passed as the target velocity vi(t +
t) = vi(t) + tui(t) to the quadrotor model. Further-
more, considering the maximum acceleration limit, we
set μm = μc = μob = μls = η. Additionally, we limited
the maximum speed of the leader to 0.1 m/s, enabling
the follower robots to aggregate around the leader in
obstacle-free environments.
The parameters of the controllers were determined
taking into account the following points. As shown
in [10], for smaller values of αob, robots tend to take
larger margins from the limit of the obstacle avoidance
constraint in (16). It is expected that αm, αc, and αls
exhibit the same behavior for the constraints in (14), (15),
and (17), respectively. Thus, if these parameters are too
small, too large margins may negatively impact the satis-
faction of other constraints. Particularly, too small values
of αob and αls make it difficult for robots to go into nar-
row tunnels due to too large margins of distance from
walls. Similarly, if large values of βm, βc, βob, and βls are
selected, large repulsive accelerations for CBF-based con-
straints possibly cause a negative effect to satisfy other
constraints. Large values of βob and βls make it difficult
for robots to go into narrow tunnels due to strong repul-
sion from the walls. For large values of cm, cc, cob and cls,
accelerations to recover from constraints could generate a
speed large enough to violate other constraints right after
recovery, particularly in narrow tunnels. A small value
should be chosen for βda, since otherwise a large velocity
moving a robot in the opposite direction to the leader is
generated so that the entire group of robots slow down.
For the weighting coefficient of the attractive APF, βag, a
too large value could cause oscillatory behaviors of robots
particularly when part of robots are still inside the tun-
nel. The values of ddel, δm, and δdel were chosen smaller
than dc without parameter tuning. For ρ, a large value was
chosen without tuning.
We used the obstacle-laden environment configura-
tion depicted in Figure 6. The leader is given a target
path that passes through the center of the tunnel, start-
ing from the origin, as illustrated by the thick solid line.
The obstacle-laden environment is designed as a polyhe-
dron tunnel, with plane obstacles positioned on all four
sides of the path (left, right, top, bottom). To define the
3D relative angle between the (n + 1)th line segment and
the nth line segment, we use a pair of angles, denoted
as (θn ̸= 0, γn ̸= 0) for n = 1, . . . , M + 1. Here, θn rep-
resents the azimuth angle of the (n + 1)th line segment
with respect to the nth line segment, and γn represents the
elevation angle of the (n + 1)th line segment with respect
to the plane perpendicular to the nth line segment. Thus,
M represents the number of corners in the target path.
The first and last line segments were divided into parts
inside and outside the obstacle area, with ls and le rep-
resenting the lengths of the parts from the origin to the
center of the first obstacle segment and from the center
of the last segment to the end of the target path, respec-
tively. Additionally, the length of the nth line segment
inside the obstacle area is defined as ln. The minimum
distance between an obstacle and the leader’s target path
is denoted as ζ.
For the tunnel obstacle in Figure 6, Oi is defined as
the union of polygons forming the tunnel. The nearest
point on each polygon from robot i is calculated. Then,
among those points, the nearest point within the sens-
ing range of robot i are selected as the elements of Oob
i
in (58). Similarly, for each polygon, the nearest obstacle
point within the region Dij defined in (46) and closest to
Figure 6. Square tunnel obstacle conﬁguration.

## Page 13

316
T. PALANI ET AL.
the LOS between robot pairs is determined. The corre-
sponding robot and obstacle point pair are then included
as elements of LSi in (60).
Figure 7. Mean angle diﬀerences between consecutive target
velocities for diﬀerent path widths.
Figure 8. Executed trajectory of the ﬁrst follower robot: (a) APF approach, and (b) Proposed non-optimization-based method. The red
arrows indicate the direction of target velocity commands sent to the quadrotor model, while the black line represents the executed
trajectory. The top row shows the trajectories in the XY-plane, and the bottom row shows the trajectories in the XZ-plane. The obstacle
is represented by the gray-shaded area.
First, simulations were conducted for a single-segment
tunnel obstacle (M = 0) with various path widths (2ζ).
Other parameters were set as θ0 = 0, γ0 = π/2, ls =
0.5, l1 = (N −1)dm/2, and le = 20. For each path-width,
a total of 25 sets of simulation trials were conducted by
placing N = 10 robots in different initial positions. Since
the allowable minimum distance between a robot and an
obstacle is do = 0.1 m, a ζ value below 0.1 m was not
feasible. Therefore, we performed simulations for cases
where ζ ranged from 0.105 m to 0.4 m.
To analyze the oscillatory movement, the angle differ-
ence between control inputs at consecutive time steps of
the follower robots was calculated. Figure 7 represent the
mean angle difference for each path width of the tunnel,
with data collected from simulation trials. The analy-
sis was conducted from the start of the simulation until
the last robot passed through the tunnel. The results of
the APF method for 2ζ = 0.21 and 0.25 are not shown,

## Page 14

ADVANCED ROBOTICS
317
Figure 9. Simulation snapshots of a random trial for the proposed non-optimization-based method in obstacle conﬁguration 3 with
2ζ = 0.5 m. The leader and follower robots are represented by red and blue circles, respectively, while the black line segment represents
the LOS connectivity between the robots in Gσ .
since the robots were unable to pass through the tunnel
successfully. This failure occurred for either of two rea-
sons: the robots got stuck in the tunnel or some of them
were left behind since the connectivity of the sensing net-
work Gs was lost. The proposed approaches exhibit a low
mean, indicating consistent direction changes in consec-
utive control inputs and thus minimal vibratory behavior
in the robots. In contrast, the APF-based approach shows
a high mean, indicating inconsistent direction changes
and significant oscillatory movement of the robots.
A typical example of responses that indicate differ-
ences in oscillation is illustrated in Figure 8 for the first
follower robot. The oscillatory behavior of the robots in
the APF approach is clear, as the target velocity com-
mands are arbitrary and inconsistent. In contrast, the
proposed approach demonstrates a steady and minimal
change in the target velocity command.
Table 3 compares constraint violations, while Table 4
shows the mean computation times for Step 3 between
the optimization-based and non-optimization-based meth-
ods. To assess the constraint violations, we tallied for
each robot the time steps in which any of the constraints
in (14)–(17) were violated, across all 25 simulation trials.
We then calculated the percentage of these violated time
steps relative to the total number of time steps for each
tunnel widths. As expected, the non-optimization-based
method shows a slightly higher rate of constraint viola-
Table 3. Rate of constraint violation in percentage (%) for single
segment tunnel obstacle.
Tunnel width (2ζ)
APF approach
Proposed opt.
Proposed non-opt.
0.21
–
2.2×10−3
2.7×10−2
0.25
–
5.9×10−4
1.3×10−2
0.30
4.2
0
7.4×10−4
0.35
2.9
0
4.3×10−4
0.40
2.0
0
6.0×10−4
0.45
1.8
0
1.3×10−4
0.50
1.7
0
9.4×10−4
0.55
1.6
0
4.3×10−4
0.60
1.6
0
0
0.65
1.6
0
0
0.70
1.6
0
6.0×10−4
0.75
1.6
0
0
0.80
1.6
0
0
tions compared to the optimization-based method, albeit
with much shorter computation times, as illustrated in
Table 4.
It should be noted that as mentioned in Section 4.2,
acon
i
in (53) plays a crucial role in the proposed meth-
ods. Table 5 illustrates a comparison of moving speeds
of robots with and without acon
i
for the single-segment
tunnel, using the optimization-based controller across 25
simulation trials. Without acon
i
, the robots failed to pass
through the tunnels in all the trials for 2ζ ≤0.55 within
the maximum simulation time limited to 36,000 time

## Page 15

318
T. PALANI ET AL.
Table 4. Mean CPU time in milliseconds for Step 3 in single seg-
ment tunnel obstacle for the proposed methods.
Tunnel width (2ζ)
Opt.
Non-opt.
0.21
23.75
0.07
0.25
29.78
0.06
0.30
25.42
0.07
0.35
31.75
0.06
0.40
27.51
0.07
0.45
33.50
0.06
0.50
29.05
0.08
0.55
32.85
0.06
0.60
29.51
0.08
0.65
32.41
0.06
0.70
29.68
0.08
0.75
32.30
0.06
0.80
29.54
0.08
Table 5. Comparison with and without acon
i
in (53) for the single-
segment tunnel, using the optimization-based controller across
25 simulation trials.
Number of completed trials
Average time steps taken
Tunnel width (2ζ)
With acon
i
Without acon
i
With acon
i
Without acon
i
0.21
25
0
8609
–
0.25
25
0
5455
–
0.30
25
0
4804
–
0.35
25
0
4147
–
0.40
25
0
3539
–
0.45
25
0
3053
–
0.50
25
0
2701
–
0.55
25
0
2464
–
0.60
25
1
2305
35511
0.65
25
1
2209
33482
0.70
25
2
2135
34586
0.75
25
12
2035
33841
0.80
25
22
1992
32093
Table 6. Complex obstacle conﬁgurations.
Conﬁg.
M
l1, . . .
θ1, . . .
γ1, . . .
(1)
1
(N−1)dm
2
, (N−1)dm
4
π
3
π
2
(2)
1
(N−1)dm
2
, (N−1)dm
4
π
2
π
2
(3)
2
(N−1)dm
2
, (N−1)dm
4
, (N−1)dm
2
π
2 , −π
2
π
2 , π
2
steps, while they passed in all the trials with acon
i
. Fur-
thermore, although the robots passed through in some
trials without acon
i
for 2ζ ≥0.60, the required time steps
in completed trials were roughly over 15 times more than
the trials with acon
i
.
Next, we conducted simulations for more complex
configurations as listed in Table 6 with N = 10 robots.
Table 7. Rate of constraint violation in percentage (%) for obstacle conﬁguration 1–3.
Conﬁg. 1
Conﬁg. 2
Conﬁg. 3
Tunnel width (2ζ)
Opt.
Non-opt.
Opt.
Non-opt.
Opt.
Non-opt.
0.4
0
1.0×10−2
0
1.7×10−2
1.3×10−4
9.6×10−3
0.5
0
9.9×10−4
0
2.6×10−3
0
2.5×10−3
0.6
1.3×10−3
0
5.0×10−3
0
3.6×10−3
0
0.7
5.3×10−4
0
4.2×10−3
1.1×10−4
3.5×10−3
1.6×10−4
0.8
0
0
3.7×10−3
1.1×10−4
3.2×10−3
0
Table 7 presents the constraint violation rates across 25
simulation trials for obstacle configurations 1–3, while
Table 8 shows the CPU time taken in Step 3. The
results for 2ζ ≥0.4 are shown, since the robots fail
to navigate through the tunnel successfully in some
Figure 10. Experiment
snapshots
of
the
proposed
non-
optimization-based method. The red lines denote the edges of
the graph Gσ .

## Page 16

ADVANCED ROBOTICS
319
Table 8. Mean CPU time in milliseconds for obstacle conﬁguration 1–3.
Conﬁg. 1
Conﬁg. 2
Conﬁg. 3
Tunnel width (2ζ)
Opt.
Non-opt.
Opt.
Non-opt.
Opt.
Non-opt.
0.4
27.69
0.07
31.42
0.07
32.09
0.07
0.5
28.84
0.07
31.05
0.08
32.61
0.08
0.6
29.87
0.08
31.53
0.08
31.67
0.08
0.7
30.09
0.08
31.49
0.09
31.67
0.08
0.8
30.74
0.08
31.62
0.09
31.73
0.08
Figure 11. Experiment results: (a) Minimum and maximum distance between the robots in link, (b) Minimum distance between the
robot and obstacle, and (c) Minimum distance between the LOS between robots and obstacle at each time instances. The dashed lines
in the ﬁgures represent the allowable minimum or maximum distances deﬁned in (14)-(17).
cases for 2ζ ≤0.3. These results show that both pro-
posed methods exhibit few constraint violations. How-
ever, the computation time for Step 3 is very short for
the non-optimization-based method, around 0.08 mil-
liseconds, while the optimization-based method averages
around 30.94 milliseconds. Therefore, the proposed non-
optimization-based method is expected to be effective in
situations where the computer is not fast enough for the
optimization-based method to be applied.
Figure 9 displays snapshots of the proposed non-
optimization-based method simulation representing a
random trial with 2ζ = 0.5 m. The snapshots show the
successful disconnection of redundant links by the robots
upon entering the tunnel, resulting in a chain formation.
They also demonstrate the proposed algorithm’s ability
to allow the robots to navigate sharp turns without los-
ing LOS connectivity while traversing critical corners.
Once the robots have passed through the obstacle envi-
ronment, they effectively aggregate around the leader
robot.
7. Experiment
The experiments were conducted in an environment
where an obstacle wall was situated in the middle of the
leader’s target path, featuring a 0.6 m hole in the mid-
dle. The positions of the quadrotors were tracked using
the OptiTrack Prime17W motion capture system. A for-
mation of five Crazyflie 2.1 quadrotors was employed for
experimental validation. Control inputs were computed
on a single computer using the proposed method and
transmitted to the quadrotors as target velocities with a
constant yaw angle. Note that control inputs were calcu-
lated in a decentralized manner for each quadrotor based
on local information within its sensing range. The wall
obstacle is approximated using multiple spheres in the
same way as in [5]. The obstacle position data were pro-
vided to the robots only when they were within sensing
range, as obstacle recognition was not the focus of this
experiment. Velocity commands were sent to the robots
at every t = 0.1 s, with the same parameters detailed
in Table 2 except for ds = 1.5, ¯dm = 1.45, dc = 0.2, and
do = 0.15.
To deal with the downwash created by the quadrotors,
the following constraint is introduced to prevent robots
from aligning vertically.
∥¯xi(t) −¯xj(t)∥≥ddw,
∀j ∈Ni(t),
(81)
where ¯xi is defined by making the third element of
xi equal to zero to compute the horizontal distance
between robots, and ddw is the minimum allowable dis-
tance between robots to prevent the downwash effect.
Similar constraints to (28) were derived using a deriva-
tive condition as in (21). The parameter values were set
as ddw = 0.2, αdw = 0.5, and βdw = 10−4.
Figure 10 presents snapshots of the experiment
using the non-optimization-based method in Section 5.
Figure 11 illustrate the constraint enforcement status
in the experiment. These results show that although
the constraints given in (14)–(17) were violated a few
times, the robot passed through the obstacle without

## Page 17

320
T. PALANI ET AL.
collisions by combination with the recovery control in
Section 4.4.
8. Conclusion
In this study, we introduced a novel CBF-based control
method for guiding a swarm of UAVs through obstacle-
rich environments, while maintaining network connec-
tivity without explicit communication between UAVs.
The proposed approach addresses the limitations of exist-
ing APF-based methods, such as oscillatory behaviors
and frequent constraint violations, by utilizing CBF-
based constraints instead of repulsive APFs and opti-
mizing control inputs through a numerical optimiza-
tion problem with soft constraints. Additionally, a non-
optimization-based method without numerical opti-
mization was presented. The effectiveness of these meth-
ods was validated through extensive simulations and
real-world experiments using quadrotors, demonstrat-
ing improved performance in reducing vibratory move-
ments compared to APF-based methods. Both proposed
approaches showed comparable performance; however,
the non-optimization-based method was preferable to
the optimization-based method since it required less
computation time, making it advantageous for quadro-
tors with limited computational power. Future work will
explore the application of the proposed method in more
complex environments involving larger swarms of UAVs
equipped with onboard sensing and computation capa-
bilities.
Disclosure statement
No potential conflict of interest was reported by the author(s).
Funding
This work is supported in part by Japan Society for the Promo-
tion of Science (JSPS) KAKENHI [grant number 22K04171].
Notes on contributors
Thiviyathinesvaran Palani received the B.Sc. Eng. (Hons) in
Electrical and Electronics Engineering from South Eastern
University of Sri Lanka in 2017 and M.Eng. from Kyoto Uni-
versity of Advanced Science in 2022. He worked as a Lecturer at
the Faculty of Engineering, University of Sri Jayewardenepura,
Sri Lanka, from 2017 to 2021. He is currently working toward
the PhD degree at Kyoto University of Advanced Science, Japan.
His research interests include robotics and decentralized con-
trol of multi-robot systems.
Hiroaki Fukushima received the B.S. and M.S. degrees in engi-
neering and Ph.D. degree in informatics from Kyoto University,
Japan, in 1995, 1998 and 2001, respectively. From 1999 to 2004
he was a Research Fellow of Japan Society for the Promo-
tion of Science. From 2004 to 2009 he worked as a Research
Associate and Assistant Professor at the University of Electro-
Communications, Japan. From 2009 to 2019 he was a Junior
Associate Professor of Kyoto University, Japan. Currently he is
a Professor of Kyoto University of Advanced Science, Japan.
His research interests include control design of mobile robots,
predictive control, and system identification.
Shunsuke Izuhara received the Ph.D. degree in mechanical
engineering from Toyohashi University of Technology, Japan,
in 2022. He is currently an Assistant Professor with the Fac-
ulty of Environmental, Life, Natural Science and Technology,
Okayama University, Okayama, Japan. His research interest
includes micro piezoelectric actuators.
ORCID
Thiviyathinesvaran
Palani
http://orcid.org/0000-0002-
4863-047X
Hiroaki Fukushima
http://orcid.org/0000-0002-0646-6974
Shunsuke Izuhara
http://orcid.org/0000-0003-0492-4991
References
[1] Parker LE, Rus D, Sukhatme GS. Multiple mobile robot
systems. In: Siciliano B, Khatib O, editors. Springer hand-
book of robotics. Cham: Springer International Publish-
ing; 2016. Springer Handbooks; p. 1335–1384.
[2] Mesbahi M, Egerstedt M. Graph theoretic methods in
multiagent networks. Princeton (NJ): Princeton Univer-
sity Press; 2010.
[3] Dorigo M, Theraulaz G, Trianni V. Swarm robotics:
past, present, and future [point of view]. Proc IEEE.
2021;109(7):1152–1165.
doi:
10.1109/JPROC.2021.
3072740
[4] Sakai D, Fukushima H, Matsuno F. Leader–follower navi-
gation in obstacle environments while preserving connec-
tivity without data transmission. IEEE Trans Control Syst
Technol. 2018;26(4):1233–1248. doi: 10.1109/TCST.2017.
2705121
[5] Nomura Y, Fukushima H, Matsuno F. Navigation of mul-
tiple UAVs in 3d obstacle environments while preserving
connectivity without data transmission. In: 2021 IEEE
Conference on Control Technology and Applications
(CCTA). IEEE; 2021. p. 82–89.
[6] Ames AD, Xu X, Grizzle JW, et al. Control barrier func-
tion based quadratic programs for safety critical systems.
IEEE Trans Automat Contr. 2017;62(8):3861–3876. doi:
10.1109/TAC.2016.2638961
[7] Wang L, Ames AD, Egerstedt M. Safety barrier certificates
for collisions-free multirobot systems. IEEE Trans Robot.
2017;33(3):661–674. doi: 10.1109/TRO.8860
[8] Chen Y, Singletary A, Ames AD. Guaranteed obstacle
avoidance for multi-robot operations with limited actu-
ation: a control barrier function approach. IEEE Con-
trol Syst Lett. 2021;5(1):127–132. doi: 10.1109/LCSYS.778
2633
[9] Ames AD, Coogan S, Egerstedt M, et al. Control bar-
rier functions: theory and applications. In: 2019 18th
European Control Conference (ECC). IEEE; 2019. p.
3420–3431.

## Page 18

ADVANCED ROBOTICS
321
[10] Singletary A, Klingebiel K, Bourne J, et al. Comparative
analysis of control barrier functions and artificial poten-
tial fields for obstacle avoidance. In: 2021 IEEE/RSJ Inter-
national Conference on Intelligent Robots and Systems
(IROS). IEEE; 2021. p. 8129–8136.
[11] Origane Y, Hattori Y, Kurabayashi D. Control input
design for a robot swarm maintaining safety distances
in crowded environment. Symmetry. 2021;13(3):478. doi:
10.3390/sym13030478
[12] Ibuki T, Hirano T, Funada R, et al. Optimization-based
distributed safety control with applications to collision
avoidance for mobile robotic networks. Adv Robot.
2023;37(1-2):87–98.
doi:
10.1080/01691864.2022.211
9886
[13] Capelli B, Fouad H, Beltrame G, et al. Decentralized
connectivity maintenance with time delays using control
barrier functions. In: 2021 IEEE International Confer-
ence on Robotics and Automation (ICRA). IEEE; 2021.
p. 1586–1592.
[14] Fu J, Wen G, Yu X, et al. Distributed formation nav-
igation of constrained second-order multiagent sys-
tems with collision avoidance and connectivity mainte-
nance. IEEE Trans Cybern. 2022;52(4):2149–2162. doi:
10.1109/TCYB.2020.3000264
[15] Luo W, Yi S, Sycara K. Behavior mixing with minimum
global and subgroup connectivity maintenance for large-
scale multi-robot systems. In: 2020 IEEE International
Conference on Robotics and Automation (ICRA). IEEE;
2020. p. 9845–9851.
[16] Özkahraman O, Ögren P. Combining control barrier
functions and behavior trees for multi-agent underwa-
ter coverage missions. In: 2020 59th IEEE Conference on
Decision and Control (CDC). IEEE; 2020. p. 5275–5282.
[17] Notomista G, Ruf SF, Egerstedt M. Persistification of
robotic tasks using control barrier functions. IEEE Robot
Autom Lett. 2018;3(2):758–763. doi: 10.1109/LSP.2016.
[18] Fouad H, Beltrame G. Energy autonomy for robot sys-
tems with constrained resources. IEEE Trans Robot.
2022;38(6):3675–3693. doi: 10.1109/TRO.2022.3175438
[19] Hegde A, Ghose D. Multi-uav collaborative transporta-
tion of payloads with obstacle avoidance. IEEE Con-
trol Syst Lett. 2021;6:926–931. doi: 10.1109/LCSYS.2021.
3087339
[20] Herguedas R, Aranda M, López-Nicolás G, et al. Multi-
robot control with double-integrator dynamics and con-
trol barrier functions for deformable object transport. In:
2022 International Conference on Robotics and Automa-
tion (ICRA). IEEE; 2022. p. 1485–1491.
[21] Sebastián E, Montijano E, Sagüés C. Adaptive multi-
robot implicit control of heterogeneous herds. IEEE Trans
Robot. 2022;38(6):3622–3635. doi: 10.1109/TRO.2022.
3183537
[22] Breeden J, Panagou D. Compositions of multiple con-
trol barrier functions under input constraints. In: 2023
American Control Conference (ACC). IEEE; 2023. p.
3688–3695.
[23] Molnar TG, Ames AD. Composing control barrier func-
tions for complex safety specifications. IEEE Control Syst
Lett. 2023;7:3615–3620. doi: 10.1109/LCSYS.2023.333
9719
[24] Rauscher M, Kimmel M, Hirche S. Constrained robot
control using control barrier functions. In: 2016 IEEE/RSJ
International Conference on Intelligent Robots and Sys-
tems (IROS). IEEE; 2016. p. 279–285.
[25] Maciejowski JM. Predictive control with constraints.
Harlow: Prentice Hall, Pearson Education Limited;
2002.
[26] Mondal A, Bhowmick C, Behera L, et al. Trajectory
tracking by multiple agents in formation with colli-
sion avoidance and connectivity assurance. IEEE Syst J.
2018;12(3):2449–2460. doi: 10.1109/JSYST.4267003
[27] Qiao Y, Huang X, Yang B, et al. Formation tracking con-
trol for multi-agent systems with collision avoidance and
connectivity maintenance. Drones. 2022;6(12):419. doi:
10.3390/drones6120419
[28] Olfati-Saber R. Flocking for multi-agent dynamic sys-
tems: algorithms and theory. IEEE Trans Automat Contr.
2006;51(3):401–420. doi: 10.1109/TAC.2005.864190
[29] Su H, Wang X, Lin Z. Flocking of multi-agents with a vir-
tual leader. IEEE Trans Automat Contr. 2009;54(2):293–
307. doi: 10.1109/TAC.2008.2010897
[30] Sakai D, Fukushima H, Matsuno F. Flocking for multi-
robots without distinguishing robots and obstacles. IEEE
Trans Control Syst Technol. 2017;25(3):1019–1027. doi:
10.1109/TCST.2016.2581148
[31] Palani T, Fukushima H, Izuhara S. Control barrier func-
tion based decentralized UAV swarm navigation while
preserving connectivity without explicit communication.
In: 2023 American Control Conference (ACC). IEEE;
2023. p. 1767–1774.
[32] Nguyen Q, Sreenath K. Exponential control barrier func-
tions for enforcing high relative-degree safety-critical
constraints. In: 2016 American Control Conference
(ACC). IEEE; 2016. p. 322–328.
[33] Xiao W, Belta C. Control barrier functions for systems
with high relative degree. In: 2019 IEEE 58th Conference
on Decision and Control (CDC). IEEE; 2019. p. 474–479.
[34] Corke P. Robotics, vision and control: fundamental algo-
rithms in matlab. 2nd ed. Cham: Springer International
Publishing; 2017.
