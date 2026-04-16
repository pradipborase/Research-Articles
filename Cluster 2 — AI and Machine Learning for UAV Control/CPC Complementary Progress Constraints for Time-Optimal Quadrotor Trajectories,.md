# CPC Complementary Progress Constraints for Time-Optimal Quadrotor Trajectories,.pdf

## Page 1

1
CPC: Complementary Progress Constraints for
Time-Optimal Quadrotor Trajectories
Philipp Foehn, Davide Scaramuzza
Abstract—In many mobile robotics scenarios, such as drone
racing, the goal is to generate a trajectory that passes through
multiple waypoints in minimal time. This problem is referred to
as time-optimal planning. State-of-the-art approaches either use
polynomial trajectory formulations, which are suboptimal due to
their smoothness, or numerical optimization, which requires way-
points to be allocated as costs or constraints to speciﬁc discrete-
time nodes. For time-optimal planning, this time-allocation is a
priori unknown and renders traditional approaches incapable
of producing truly time-optimal trajectories. We introduce a
novel formulation of progress bound to waypoints by a com-
plementarity constraint. While the progress variables indicate
the completion of a waypoint, change of this progress is only
allowed in local proximity to the waypoint via complementarity
constraints. This enables the simultaneous optimization of the
trajectory and the time-allocation of the waypoints. To the best of
our knowledge, this is the ﬁrst approach allowing for truly time-
optimal trajectory planning for quadrotors and other systems.
We perform and discuss evaluations on optimality and convexity,
compare to other related approaches, and qualitatively to an
expert-human baseline.
I. INTRODUCTION
Autonomous aerial vehicles are nowadays being used for
inspection, delivery, cinematography, search-and-rescue, and
recently even drone racing. The most prominent aerial system
is the quadrotor, thanks to its vertical take-off and hover
capabilities, its simplicity, and its versatility ranging from
smooth maneuvers to extremely aggressive trajectories. How-
ever, quadrotors have limited range dictated by their battery
capacity, which in turn limits how much time can be spent
on a speciﬁc task. If the tasks consists of visiting multiple
waypoints (delivery, inspection, drone racing [1, 2]), doing so
in minimal time is often viable, and in the context of search
and rescue or drone racing even the ultimate goal.
Truly time-optimal quadrotor trajectories exploit the full
actuator potential at every point in time, which excludes
using continuous polynomial formulations due to their inherent
smoothness. This leaves planning time-discretized trajectories
as the only option, which is typically solved using numerical
optimization. Unfortunately, such formulations require the al-
location of waypoints as costs or constraints to speciﬁc discrete
time nodes, which is a priori unknown. We investigate this
problem and provide a solution that allows to simultaneously
optimize the trajectory and waypoint allocation. Our approach
formulates a progress measure for each waypoint along the
trajectory, indicating completion of a waypoint (see Fig. 1).
We then introduce a complementary progress constraint, that
allows completion only in proximity to a waypoint.
For simple point-mass systems, time-optimal trajectories
can be computed in closed-form resulting in bang-bang accel-
State-of-the-Art: Waypoint Allocation using Constraints
Our Method: Waypoint Progress Variables λ and their Completion (Arrows)
Fig. 1: Top: state-of-the-art ﬁxed allocation of waypoints to speciﬁc
nodes. Bottom: our method of deﬁning one progress variable per
waypoint. The progress variable can switch from 1 (incomplete) to
0 (completed) only when in proximity of the relevant waypoint,
implemented as a complementary constraint (details in Fig. 3).
eration trajectories, which can easily be sampled over multiple
waypoints. However, quadrotors are underactuated systems
that need to rotate to adjust their acceleration direction, which
always lies in the body z-axis. Both the linear and rotational
acceleration are controlled through the rotor thrusts, which are
physically limited by the actuators. This introduces a coupling
in the achievable linear and rotational accelerations. Therefore,
time-optimal planning becomes the search for the optimal
tradeoff between maximizing these accelerations.
There exist two approaches in formulating the underlying
state space for trajectory planning: (i) polynomial representa-
tions and (ii) discretized state space formulations.
The ﬁrst approach exploits the quadrotor’s differentially-ﬂat
output states represented by smooth polynomials. Their com-
putation is extremely efﬁcient and trajectories through multiple
waypoints can be represented by concatenating polynomial
segments, where sampling over segment times and boundary
conditions provides minimal-time solutions. However, these
polynomial, minimal-time solutions are still suboptimal for
quadrotors, since they (i) are smooth and cannot represent
rapidly-changing states, such as bang-bang trajectories, and
(ii) can only touch the constant boundaries in inﬁnitesimal
points, but never stay at the limit for durations different than
the total segment time. Both problems are visualized in Fig.
2 and further explained in Sec. II.
The second approach uses non-linear optimization to plan
trajectories described by a time-discretized state space, where
the system dynamics and input boundaries are enforced as
constraints. In contrast to the polynomial formulation, this
allows the optimization to pick any input within bounds for
each discrete time step. For a time-optimal solution, the tra-
jectory time tN is part of the optimization variables and is the

## Page 2

2
sole term in the cost function. However, if multiple waypoints
must be passed, these must be allocated as constraints to
speciﬁc nodes on the trajectory. Since the fraction of overall
time spent between any two waypoints is unknown, it is
a priori undeﬁned to which nodes on the trajectory such
waypoint constraints should be allocated. This problem renders
traditional discretized state space formulations ineffective for
time-optimal trajectory generation through multiple waypoints.
In this work, we answer the following research questions:
1) How can we revise the waypoint constraints to optimize
simultaneously time-allocation, while exploiting the sys-
tem dynamics and actuation limits?
2) What are the resulting properties regarding initialization
and convergence due to (non-) convex constraints?
3) What are the characteristics of time-optimal trajectories?
Contribution
Our approach optimizes a time-discretized state and input
space for minimum execution time, with the quadrotor dynam-
ics and input bounds implemented as equality and inequality
constraints, respectively. Our contribution is a formulation
of progress over the trajectory, where the completion of a
waypoint is represented as a progress variable (see Fig. 1).
We introduce a complementarity constraint, which allows the
progress variable of a waypoint to switch from incomplete to
complete only at the time nodes where the vehicle is within
tolerance of the waypoint. This allows us to encapsulate the
task of reaching multiple waypoints without specifying at
which time a waypoint is reached, solving the time-allocation
problem. We evaluate our approach experimentally in a multi-
tude of scenarios, covering basic optimality and convergence
tests, verifying time alignment of waypoints, many-waypoint
scenarios, and ﬁnally comparing against human performance.
II. PREFACE: TIME-OPTIMAL QUADROTOR TRAJECTORY
A. Point-Mass Bang-Bang
Time-optimal trajectories encapsulate the best possible ac-
tion to reach one or multiple targets in the lowest possible time.
We ﬁrst investigate a point mass in R3 controlled by bounded
acceleration a ∈R3 | ∥a∥≤amax, starting at rest position p0
and translating to rest position p1. The time-optimal solution
takes the form of a bang-bang trajectory over the time topt,
accelerating with amax for topt/2, followed by decelerating
with amax for topt/2. A trajectory through multiple waypoints
can be generated similarly by optimizing over the switching
times and intermittent waypoint velocities. For the general
solution and applications we refer to [3].
B. Bang-Bang Relation for Quadrotors
A quadrotor would exploit the same maximal acceleration
by generating the maximal possible thrust with its rotors.
However, due to the quadrotor’s underactuation, it can not
instantaneously change the acceleration direction, but needs to
rotate by applying differential thrust over its rotors. The linear
and rotational acceleration are both controlled through the
rotor thrusts, which in turn are limited, introducing a coupling
0.0
0.5
1.0
1.5
2.0
0
2
4
6
p [m]
9th order
t = 2.165s
7th order
t = 1.938s
5th order
t = 1.699s
bang-bang
t = 1.614s
0.0
0.5
1.0
1.5
2.0
t [s]
−10
−5
0
5
10
a [m/s2]
amax
−amax
Fig. 2: Multiple orders of polynomial trajectories and one bang-bang
trajectory with limited slope. The polynomial trajectories only touch
the input extrema in two points, while the bang-bang spends more
time at the limit and achieves a lower overall time.
of the achievable linear and rotational acceleration (visualized
later in Fig. 4). Therefore, a time-optimal trajectory is the
optimal tradeoff between rotational and linear acceleration,
where the rotor thrusts only deviate from the maximum to
adjust the rotational rates. Indeed, our experiments conﬁrm
exactly this behavior (see e.g. Fig, 5), as in Sec. VIII.
C. Sub-Optimality of Polynomial Trajectories
The quadrotor is a differentially ﬂat system [4] that can be
described based on its four ﬂat output states, position and yaw.
This allows to represent the evolution of the ﬂat output states
as smooth differentiable polynomials of the time t. To generate
such polynomials, one typically deﬁnes its boundary condi-
tions at start and end time, and solves for a smooth polynomial,
optionally minimizing one of the derivatives, commonly the
snap (4th derivative of position, as in [5]). The intention
behind such minimum-snap trajectories is to minimize and
smooth the needed body torques and, therefore, single motor
thrust differences, which are dependent on the snap. Since the
polynomials are extremely efﬁcient to compute, trajectories
through many waypoints can be generated by concatenating
segments of polynomials, and minimal-time solutions can be
found by optimizing or sampling over the segment times and
boundary conditions. However, these polynomials are smooth
by deﬁnition, which stands in direct conﬂict with maximizing
the acceleration at all times while simultaneously adapting the
rotational rate, as explained in the previous Sec. II-B. In fact,
due to the polynomial nature of the trajectories, the boundaries
of the reachable input spaces can only be touched at one or
multiple points, or constantly, but not at subsegments of the
trajectory. This problem is visualized in Fig. 2, and not only
applies to polynomial trajectories, but partially also to direct
collocation methods for optimization [6].
D. Real-World Deployment
Note that the time optimal solutions cannot be tracked on a
real system, because disturbances could not be corrected, since
the system is at the boundary of the reachable input space [3].

## Page 3

3
III. RELATED WORK
A. Basic Quadrotor Control
The quadrotor model, its underactuated nature, and control-
lability have been extensively study in [7, 8] even with exten-
sions to aerodynamic modelling [9, 10]. Control algorithms
for quadrotors are well established and reach from cascaded
control [11] to model predictive control (MPC) [12–14]. Such
MPC systems allow to track even aggressive trajectories with
high reliability, thanks to their prediction and optimization
over a sliding time window. However, even those sophisticate
control approaches rely on references from high-level planning
approaches, considering the whole time horizon of a task.
B. Polynomial Trajectory Planning
The ﬁrst category of such planning algorithms is based on
polynomial trajectories. The work by [5, 4] established the
now widely used minimum-snap trajectories, minimizing the
4th derivative of the position to generate smooth trajectories.
The approach by [15] builds on [5], but extends the cost
on an n-th order derivative by the trajectory time, effectively
achieving a trade-off between lowest time and smoothness.
Exploiting polynomial formulations allows for extremely fast
computation of trajectory solutions, which [16] further exploits
by limiting the approach to ﬁfth order polynomials, which can
then be solved in closed form.
In [17] a multilevel system is proposed in the context of
obstacle avoidance, ﬁrst approximating the system dynamics
by assuming acceleration as the bounded control input. The
simpliﬁed system is used to sample minimum-time bang-
bang trajectories, which are then reﬁned and optimized for
quadrotors using polynomial representations.
By searching over boundary and intermittent conditions,
or scaling the polynomials, many different problems can be
solved with fast sampling based approaches. However, as
elaborated in Sec. II-C, the smoothness does conﬂict with the
desired maximization of the acceleration.
C. Optimization-based Trajectory Planning
Trajectory planning through numerical optimization on dis-
cretized state spaces has been widely used in the ﬁeld of
manipulators [18], legged [19], and aerial robots [20].
To formulate trajectory planning as an optimization prob-
lem, multiple approaches exist, such as direct multiple shoot-
ing [21] and direct collocation [6]. Direct collocation uses
low-order splines between discrete time nodes, which can be
beneﬁcial for certain problems, but is inferior when dealing
with a high number of inequality constraints. Direct multiple
shooting methods discretize the time horizon of the trajectory
in N steps and include both the state and inputs in the
optimization variables. The system dynamics are enforced
as equality constraints over a timestep, and input limits are
represented as inequality constraints.
Many approaches on numerical optimal control [13, 14] and
trajectory generation [22, 20] deploy these schemes success-
fully for quadrotors. They typically formulate goals and tasks
as cost and/or constraints on the state and input space. Smooth
trajectories i.e. be enabled by penalizing high input deviations,
similar to minimum-snap trajectories.
A simpliﬁed approach is followed by [23] in the context
of multi-vehicle planning, where the optimization variables
only contain the vehicles acceleration, and no rotation is
represented. Position, velocity and jerk are deﬁned as afﬁne
functions of the acceleration, rendering this scheme a single-
shooting approach with an approximative model but compu-
tationally very efﬁcient. Unfortunately it does only impose
box-constraints on acceleration and jerk to approximate the
actuation limits, which does not represent the thrust limitations
well, rendering it unﬁt for time-optimal planning.
While these approaches allow to solve for complex tasks
and maneuvers, they still rely on the user to allocate cost
and constraints to speciﬁc time steps. Normally this is not
a problem, since the costs are allocated to the whole time
horizon and e.g. waypoint constraints can be allocated to
speciﬁc times. However, this is no longer possible for the
problem of time-optimal waypoint ﬂight, since the exact time
or fraction at which a waypoint is passed is a priori unknown.
D. Time-Optimal Approaches
For simple systems, so called bang-bang or bang-singular
approaches have been widely established and proven to second
order sufﬁcient conditions as in [24, 25, 3]. These approaches
apply to systems with bounded input space, breaking down
to a boundary value problem (e.g. switching between maxi-
mal and minimal inputs), capable of producing closed form
solutions for a multitude of dynamic systems. However, if the
input bounds are not independent, these approaches become
infeasible. [26] proposes an approach to generate time-optimal
trajectories between two known states based on the aforemen-
tioned bang-bang approaches using numerical optimization of
the switching times. However, the approach is only developed
for 2-dimensional maneuvers in a plane and with collective
thrust and bodyrates as independent input modalities, which do
not correctly represent the limited thrust inputs of a quadrotor.
[27] represents the trajectory of a quadrotor as a convex
combination of multiple paths given by analytical functions,
which can additionally fulﬁll spatial constraints, such as ob-
stacles. The authors compare their approach to the one of [26]
an verify their experimental results. However also [27] limit
their results to 2-dimensional experiments with only start and
end states, without intermediate waypoints.
[28] provides a very thorough literature review and problem
analysis, also solving the problem of time allocation to way-
points. This approach uses a geometric reference path and a
change of variables that puts the state space of the quadrotor
into a traverse dynamics formulation along this path. This
allows to deﬁne progress along the track as the arc length
along the geometric reference path, as well as writing cost and
constraints based on the arc length and therefore independent
of time. While this approach is very elegant, it approximates
the quadrotor’s actuation constraints as bodyrates and thrust
limits, not realistically representing the rotor thrust bounds.
Furthermore, the vehicles orientation is restricted in magnitude
of the individual rotation axis, to keep the dynamics well-
deﬁned, since their representation uses Euler angles. This

## Page 4

4
limits the space of solutions and therefore the optimality of
the resulting trajectory.
Finally, [29] provides a method to generate close to
time-optimal segment times for polynomial trajectories using
Bayesian Optimization. The approach is based on learning
Gaussian Classiﬁcation models predicting feasibility of a
trajectory based on multi-ﬁdelity data from analytic models,
simulation and real-world data. While this approach puts high
emphasis on real-world applicability and can even account for
aerodynamic effects, it is still constrained to polynomials and
requires real-world data speciﬁcally collected for the given
vehicle. Furthermore, it is an approximative method rather than
the true time-optimal solution.
IV. PROBLEM FORMULATION
A. General Trajectory Optimization
The general optimization problem of ﬁnding the minimizer
x∗for cost J(x) in the state space x ∈X n can be stated as
x∗= min
x L(x)
(1)
subject to
g(x) = 0 and h(x)
≤0
where g(x) and h(x) contain all equality and inequality con-
straints respectively. The full state space x is used equivalent
to the term optimization variables. The cost L(x) typically
contains one or multiple quadratic costs on the deviation from
a reference, costs on the systems actuation inputs, or other
costs describing any desired behaviors.
1) Multiple Shooting Method: To represent a dynamic
system in the state space, the system state xk is described
at discrete times tk = dt ∗k at k ∈(0, N), also called nodes,
where its actuation inputs between two nodes are uk at tk with
k ∈(0, N]. The systems evolution is deﬁned by the dynamics
f dyn(x, u) = ˙x, anchored at x0 = xinit, and implemented
as an equality constraint of the ﬁrst order forward integration:
xk+1 −xk −dt · f dyn(xk, uk) = 0
(2)
which is part of g(x) = 0 in the general formulation. Both
xk, uk are part of the state space and can be summarized as
the vehicles dynamic states xdyn,k at node k.
2) Integration Scheme: Additionally we can change the for-
mulation to use a higher order integration scheme to suppress
linearization errors for highly non-linear systems. In this work,
we deploy a 4th order Runge-Kutta scheme:
xk+1 −xk −dt · f RK4(xk, uk) = 0
(3)
f RK4(xk, uk) = 1/6 · (k1 + 2k2 + 2k3 + k4)
(4)
k1 = f dyn(xk, uk)
k2 = f dyn(xk + dt/2 · k1, uk)
k3 = f dyn(xk + dt/2 · k2, uk)
k4 = f dyn(xk + dt · k3, uk).
B. Time-Optimal Trajectory Optimization
Optimizing for a time-optimal trajectory means that the only
cost term is the overall trajectory time L(x) = tN. Therefore,
tN needs to be in the optimization variables x = [tN, . . . ]⊺,
and must be positive tN > 0. The integration scheme can then
be adapted to use dt = tN/N.
C. Passing Waypoints through Optimization
To generate trajectories passing through a sequence of
waypoints pwj with j ∈[0, . . . , M] called track, one would
typically deﬁne a distance cost or constraint and allocate it to
a speciﬁc state xdyn,k at node k with time tk. For cost-based
formulations, quadratic distance costs are robust in terms of
convergence and implemented as
Ldist,j = (pk −pwj)⊺(pk −pwj)
(5)
where pk, part of x, is the position state at a user deﬁned
time tk. However, such a cost-based formulation is only a soft
requirement and if summed with other cost terms does not
imply that the waypoint is actually passed within a certain
tolerance. To guarantee passing within a tolerance, constraint-
based formulations can be used, such as
(pk −pwj)⊺(pk −pwj) <= τ 2
j
(6)
which in the general problem is part of h(x) ≤0, and requires
the trajectory to pass by waypoint j at position pwj within
tolerance τj at time tk.
D. The Problem of Time Allocation and Optimization
Adding waypoints to a trajectory means that their costs or
constraints need to be allocated to speciﬁc nodes (at times tk)
on the trajectory. This ﬁxes the time at which a waypoint is
passed, or even if we optimize over the total time tN, it still
ﬁxes the fractional time tk = tN/N · k. However, it is not
always possible to know a priori how much time or what
fraction of the total time is spent between two waypoints.
Therefore, it is not possible to allocate waypoint costs or
constraints to nodes at speciﬁc times.
One approach is to spread the cost of reaching the waypoint
over multiple nodes, which is done in [13] with an exponential
weight spread. Even though this allows to shift the time of
passing a waypoint, the width and mean of the weight spread
are still user-deﬁned, suboptimal in most scenarios, and does
not allow to freely shift the time at which a waypoint is passed.
There are two possible ways to solve this: (i) change
the time between ﬁxed nodes, which implies changing dt
for each timestep by adding all dtk to the optimization
variables; or (ii) change the node k to which a waypoint
is allocated. The ﬁrst option is to allow varying timeteps
dtk. This however negatively impacts the linearization quality
and makes it inconsistent over the trajectory, allows trivial or
suboptimal solutions, or even leads the optimization to exploit
linearization errors. The second option requires a formulation
that allows the optimization to change the node k to which
a waypoint is allocated. Since this tackles the fundamental
underlying allocation problem, we base our approach on this
second option.
E. Problem Formulation Summary
In conclusion, the goal of this work is to ﬁnd an opti-
mization problem formulation which (i) satisﬁes the system
dynamics and input limitations, (ii) minimizes total trajectory
time, (iii) passes by multiple waypoints in sequence, and (iv)
ﬁnds the optimal time at which to pass each waypoint.

## Page 5

5
V. APPROACH:
COMPLEMENTARY PROGRESS CONSTRAINTS
Our approach consists of two main steps: (i) adding a
measure of progress throughout the track, and (ii) adding
a measure of how this progress changes. In the following
sections we explain how these two steps can be formulated
and added to an numerical optimization problem.
A. Progress Measure Variables
To describe the progress throughout a track we want a
measure that fulﬁlls the following requirements: (i) it starts at
a deﬁned value, (ii) it must reach a different value by the end
of the trajectory, and (iii) it can only change when a waypoint
is passed within a certain tolerance. To achieve this, let the
vector λk ∈RM deﬁne the progress variables λj
k at timestep
tk for all M waypoints indexed by j. All progress variables
start at 1 as in λ0 = 1 and must reach 0 at the end of the
trajectory as in λN = 0. The progress variables λ are chained
together and their evolution is deﬁned by
λk+1 = λk −µk
(7)
where the vector µk ∈RM indicates the progress step at
every timestep. Note that the progress can only be positive,
therefore µj
k ≤0. Both λk and µk for every timestep are part
of the optimization variables x, which replicates the multiple
shooting scheme for the progress variables.
To deﬁne when and how the progress variables can change,
we now imply constraints on µk, in it’s general form as
ϵ−
k ≤f prog(xk, µk) ≤ϵ+
k
(8)
where ϵ−, ϵ+ can form equality or inequality constraints.
Finally, to ensure that the waypoints are passed in the
given sequence, we enforce subsequent progress variables to
be bigger than their prequel at each timestep by
µj
k ≤µj+1
k
∀k ∈[0, N], j ∈[0, M).
(9)
B. Complementary Progress Constraints
In the context of waypoint following, the goal is to allow
µk to only be non-zero at the time of passing a waypoint.
Therefore, f prog and ϵ−= ϵ+ = 0 are chosen to represent a
complementarity constraint, as
f prog(xk, µk) =
h
µj
k · ∥pk −pwj∥2
2
i
j∈[0,M)
!= 0
(10)
which can be interpreted as a mathematical ”or” function,
since either µj
k or ∥pk −pwj∥must be 0. Intuitively, the two
elements complement each other.
C. Tolerance Relaxation
With Eqn. 10 the trajectory is forced to pass exactly through
a waypoint. Not only is this impractical, since often a certain
tolerance is admitted or even wanted, but it also negatively
impacts the convergence behavior and time-optimality, since
the system dynamics are discretized and one of the discrete
timesteps must coincide with the waypoint. Therefore, it is
Fig. 3: Illustration of the Complementary Progress Constraint. µ can
only be non-zero if the distance to the waypoint pw is less than the
tolerance dtol. This is not the case for x0, but for x1, and allowing
the progress variable to switch to 0 (complete).
desirable to relax a waypoint constraint by a certain tolerance
which is achieved by extending Eqn. 10 to
f prog(xk, µk) =
h
µj
k ·

∥pk −pwj∥2
2 −νj
k
i
j∈[0,M)
(11)
subject to
0 ≤νj
k ≤d2
tol
where νj
k is a slack variable to allow the distance to the
waypoint to be relaxed to zero when it is smaller than dtol,
the maximal distance tolerance. This now enforces that the
progress variables can not change, except for the timesteps at
which the system is within tolerance to the waypoint.
VI. FULL PROBLEM FORMULATION
The full space of optimization variables x consists of the
overall time and all variables assigned to nodes k as xk. All
nodes k include the robots dynamic state xdyn,k, its inputs
uk, and all progress variable, therefore:
x = [tN, x0, . . . , xN]
(12)
where
xk =
(
[xdyn,k, uk, λk, µk, νk]
for k ∈[0, N)
[xdyn,N, λN]
for k = N.
(13)
Based on this representation, we write the full problem as
x∗= min
x tN
(14)
subject to the system dynamics and initial constraint
xk+1 −xk −dt · f RK4(xk, uk) = 0
(15)
x0 = xinit,
(16)
the input constraints
umin −uk ≤0
uk −umax ≤0,
(17)
the progress evolution, boundary, and sequence constraints
λk+1 −λk + µk = 0
(18)
λ0 = 0
λN −1 = 0
(19)
λj
k −λj+1
k
≤0
∀j ∈[0, m),
(20)
and the complementarity constraint with tolerance
µj
k ·

∥pk −pwj∥2
2 −νj
k

= 0
(21)
−νj
k ≤0
νj
k −d2
tol ≤0.
(22)

## Page 6

6
(a) Acceleration Space
20
10
0
10
20
ax [m/s2]
30
20
10
0
10
20
ay [m/s2]
g
amax
amin
a
a + g
(b) Thrust and Torque Space
1.0
0.5
0.0
0.5
1.0
 [Nm]
0
4
8
12
16
20
T [N]
Tmax
Tmean
Tmin
Fig. 4: Acceleration- (Fig.4a) and thrust/torque-space (Fig. 4b) of the
STD quadrotor conﬁguration (see Tab. I). Note that the acceleration
space in Fig. 4a is non-convex due to Tmin > 0 and the thrust and
torque limits are dependent on each other in 4b.
VII. APPLICATION TO QUADROTORS
To apply our time-optimal planning method to a quadrotor,
we ﬁrst deﬁne its state space, input modality, and dynamics.
A. Quadrotor Dynamics
The quadrotor’s state space is described between the inertial
frame I and body frame B, as x = [pIB, qIB, vIB, wB]⊤
corresponding to position pIB ∈R3, unit quaternion rotation
qIB ∈R4 given ∥qIB∥= 1, velocity vIB ∈R3, and bodyrate
ωB ∈R3. The input modality is on the level of collective
thrust T B = [00TBz]⊺and body torque τ B. From here on we
drop the frame indices since they are consistent throughout
the description. The dynamic equations are given by
˙p = v
˙q = 1
2Λ(q)

0
ω

(23)
˙v = g + 1
mR(q)T
˙ω = J−1 (τ −ω × Jω)
(24)
where Λ represents a quaternion multiplication, R(q) the
quaternion rotation, m the quadrotor’s mass, and J its inertia.
B. Quadrotor Inputs
The input space given by T and τ is further decomposed
into the single rotor thrusts u = [T1, T2, T3, T4]. where T is
the thrust at rotor i ∈{1, 2, 3, 4}.
T =


0
0
P Ti


and τ =


l/
√
2(T1 + T2 −T3 −T4)
l/
√
2(−T1 + T2 + T3 −T4)
cτ(T1 −T2 + T3 −T4)


(25)
with with the quadrotor’s arm length l and the rotor’s torque
constant cτ. The quadrotor’s actuators limit the applicable
thrust for each rotor, effectively constraining Ti as
0 ≤Tmin ≤Ti ≤Tmax
(26)
where Tmin, Tmax are positive for typical quadrotor setups.
In Fig. 4 we visualize the acceleration space and the thrust
torque space of a quadrotor in the xz-plane. Note that, the
acceleration space in Fig. 4a is not convex due to Tmin > 0
for the depicted model parameters from the STD conﬁguration
of Tab. I. The torque space is visualized in Fig. 4b, where the
coupling between the achievable thrust and torque is visible.
TABLE I: Quadrotor Conﬁgurations
Property
RQ
MS
SIM
STD
m [kg]
0.76
1.0
3.2
1.0
l [m]
0.17
0.23
0.232
0.15
diag(J) [gm2]
[3, 3, 5]
[10, 10, 20]
[50, 23, 67]
[5, 5, 10]
Tmin [N]
0.0
0.0
0.5
0.25
Tmax [N]
16.0
4.179
12
5.0
cτ [1]
0.01
0.0133
0.0133
0.01
ωmax [rad s−1]
15
10
3
10
vmax [m s−1]
42
19
20
−
C. Approximative Linear Aerodynamic Drag
Finally, we extend the quadrotor’s dynamics to include a
linear drag model, to approximate the most dominant aerody-
namic effects with drag coefﬁcient cD by
˙v = g + 1
mR(q)T −cD ∗v.
(27)
We approximate cD =
q
(4 ∗Tmax/m)2 −g2/vmax to can-
cle the full thrust in horizontal steady-state ﬂight at vmax.
VIII. EXPERIMENTAL EVALUATION
To demonstrate the capabilities and applicability of our
method, we test it on a series of experiments. We ﬁrst evaluate
a simple point-to-point scenario and compare to [26, 27] in
Sec. VIII-A. Next we investigate the time alignment for mul-
tiple waypoints in Sec. VIII-B, followed by an experimental
investigation of the convergence characteristics on short tracks
in terms of initialization in Sec. VIII-C and (non-) convexity
in Sec VIII-D. Then we demonstrate applicability to longer
tracks with ≥10 waypoints (Sec. VIII-E, VIII-F). Finally, we
compare time-optimal trajectories to human trajectories ﬂown
in simulation (Sec. VIII-G and real-world (Sec. VIII-H).
All evaluations are performed using CASADI [30] with
IPOPT [31] as solver backend. We use multiple different
quadrotor conﬁgurations, as listed in Tab. I. The ﬁrst con-
ﬁguration represents a typical race quadrotor, the second one
is parameterized after the MicroSoft AirSim [32] SimpleFlight
quadrotor, and the third one resembles the drone used in
simulation ﬂown by a human pilot. The last standard ”STD”
conﬁguration resembles the one used in [26, 27].
Initialization Setup
If not stated differently, the optimization is initialized with
identity orientation, zero bodyrates, 1 m s−1 velocity, linearly
interpolated position between the waypoints, and hover thrusts.
The total time is set as the distance through all waypoints
divided by the velocity guess. The node of passing a waypoint
(respectively where the progress variables λ switch to zero)
is initialized as equally distributed, i.e. for waypoint j the
passing node is kj = N ∗j/M. We deﬁne the total number of
nodes N based on the number of nodes per waypoint Nw so
that N = MNw. We typically chose roughly Nw ∈(50, 100)
nodes per waypoint, to get a good linearization depending on
the overall length, complexity, and time of the trajectory. Note
that high numbers of Nw >> 100 help with convergence and
achieved stability of the underlying optimization algorithm,
but on longer tracks can cause very long computation times
of multiple hours on average laptop computers in 2020.

## Page 7

7
px
Time of [26]
Time of [27]
Time of ours
3 m
0.898 s
0.890 s
0.918 s
6 m
1.231 s
1.223 s
1.255 s
9 m
1.488 s
1.478 s
1.517 s
12 m
1.705 s
1.694 s
1.736 s
15 m
1.895 s
1.885 s
1.933 s
TABLE II: Comparison of the resulting timings between our approach
and [26, 27]. Note that our approach is 2.00% slower than [26] and
2.68% slower than [27], because it accounts for rotation dynamics
and true actuator limits.
A. Time-Optimal Hover-to-Hover Trajectories
We ﬁrst evaluate trajectory generation between two known
position states in hover, one at the origin, and one at px =
[3, 6, 9, 12, 15]m, as in [26, 27]. Additionally to the problem
setup explained in Sec. V, we add constraints to the end
state to be in hover, i.e. vN = 0 and q = [10]. We use
N = Nw = 50 nodes and a tolerance of dtol = 10−3.
Different from [26, 27], we compute the solution in full 3D
space, which however does not matter for this experiment,
since the optimal trajectory stays withing the y-plane. We
deﬁned the model properties so that it meets the maximal
and minimal acceleration [amin, amax] = [1, 20]m s−2 and
maximal bodyrate ωmax = 10 rad s−1 as in [26, 27], given
by our STD conﬁguration (see Tab. I).
The solutions are depicted in the xy-plane in Fig. 6 and
the timings are stated and compared to [26, 27] in Tab. II.
Note that our approach is 2.00% slower than [26] and 2.68%
slower than [27] because, differently from those works, it also
models the full rotational dynamics and accounts for realistic
actuation limits.
B. Optimal Time Allocation on Multiple Waypoints
In this experiment, we deﬁne a straight track between origin
and px = 50 m trough multiple waypoints. The goal is to show
(a) Hover-to-Hover Trajectories
0
3
6
9
12
15
px [m]
1
0
1
2
py [m]
T3
T6
T9
T12
T15
(b) Velocity Proﬁle
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
2.00
t [s]
0
10
20
v [m/s]
|v3|
|v6|
|v9|
|v12|
|v15|
Fig. 6: Time-optimal hover-to-hover trajectories between states
spaced px = [3, 6, 9, 12, 15]m apart as in [26, 27]. The top Fig. 6a
depicts the position on the xy-plane, while the lower Fig. 6b depicts
the velocity proﬁle.
how that our method can choose the optimal time at which
a waypoint is passed, and we expect to see both setups to
converge to the same solution. Therefore, we test two different
distributions of the waypoints pwj over the straight track;
speciﬁcally, we deﬁne a regular (px,reg = [1, 20, 30, 40, 50]m),
and an irregular (px,ireg = [10, 15, 20, 25, 50]m) distribution.
We chose N = 125 and a tolerance of dtol = 0.4 m, with the
STD quadrotor (see Table I).
As expected, both setups converge to the same solution of
tN = 2.430 s, depicted in Fig. 5, with an equal trajectory and
inputs, despite the different waypoint distribution. Since the
waypoints are located at different intervals, we can observe a
different distribution of the progress variables in Fig. 5, while
the trajectory time, dynamic states, and inputs stay the same.
(a) Regular Waypoint Distribution tN = 2.340 s
xy-position
0
10
20
30
40
50
px [m]
2.5
0.0
2.5
pz [m]
Inputs
0.0
0.5
1.0
1.5
2.0
2.5
t [s]
2
4
u [N]
u0, u1
u2, u3
Progress
0.0
0.5
1.0
1.5
2.0
2.5
t [s]
0
1
progress
sol
init
(b) Irregular Waypoint Distribution tN = 2.340 s
xy-position
0
10
20
30
40
50
px [m]
2.5
0.0
2.5
pz [m]
Inputs
0.0
0.5
1.0
1.5
2.0
2.5
t [s]
2
4
u [N]
u0, u1
u2, u3
Progress
0.0
0.5
1.0
1.5
2.0
2.5
t [s]
0
1
progress
sol
init
Fig. 5: A trajectory along waypoints distributed on a line over 50 m, ﬂown in < 2.430 s. In Fig. 5a the waypoints are equally distributed
over the total distance, while in Fig. 5b the ﬁrst 4 of 5 waypoints lie withing the ﬁrst half of the total distance. The bottom plot depicts
the progress variables as initialized (dashed −−) and as in the ﬁnal solution (solid −). Note that both settings converge to the exact same
solution, while the time of passing the waypoints was signiﬁcantly adjusted from the initialization, and is differs between the settings.

## Page 8

8
(a) Initialized passing through both waypoints.
tN = 3.600 s
0
5
10
15
20
px [m]
4
2
0
2
4
py [m]
(b) Initialized passing through only one waypoints.
tN = 3.600 s
0
5
10
15
20
px [m]
4
2
0
2
4
py [m]
Fig. 7: Convergence in an open hairpin turn from two different initializations in red (—) over the iterations in light blue (—), to the ﬁnal
solution in dark blue(—). The trajectory starts at the top left and goes through the two waypoints (×). While the good initialization of Fig.
7a needs 216 iterations, the poor guess in Fig. 7b needs 303 iterations, but both converge to exactly the same solution with tN = 3.600 s.
C. Initialization & Convergence
As a next step, the method is tested for convergence
properties given different initializations. For this, we again use
the STD quadrotor conﬁguration and discretize the problem
into N = 160 nodes with a tolerance of dtol = 0.4 m. We use
a track consisting of a so-called open hairpin, consisting of two
waypoints as seen on the xy-plane in Fig. 7, starting on the
top left and passing the waypoint to the far right and bottom
left, where the end point is not in hover. Two setups are tested,
where the ﬁrst one is initialized with the position interpolated
between the waypoints as in Fig. 7a, and the second one is
initialized with a poor guess interpolated only from start to
end point, as in Fig. 7b.
The expected outcome is that both initialization setups
should converge to the same solution. Indeed we can observe
this behavior in Fig. 7, where we depict the initial position
guess in red and the convergence from light to dark blue.
The good initial guess in Fig. 7a results in 216 iterations
until convergence, while the poor guess in Fig. 7b needs 303
iterations, all plotted in Fig. 7. This indicates that our method
is not sensitive to correct initializations, but proﬁts from good
guesses. However, since the acceleration space of a quadrotor
is not necessarily convex and the resulting problem is highly
non-convex, the next experiment elaborates on how to provoke
and circumvent this issue.
D. Provoking Non-Convexity Issues
Since quadrotors can only produce thrust in body z-axis and
the motors of most real-world systems cannot turn off, and
therefore always produce a positive minimal thrust Tmin > 0,
the resulting acceleration space is non-convex. We evaluate
this on a vertical turn where we ﬂy from hover at the origin
through two waypoints directly above each other, back to the
origin but not in hover. The Track can be seen in Fig. 8. First,
the STD quadrotor conﬁguration is used, with N = 150 nodes
and a tolerance of dtol = 0.1 m, with the general initialization
setup where the orientation is kept at identity. A second
setup uses a different initialization, where we interpolate the
orientation around the y-axis between αinit = 0, α0 = π for
the second waypoint and α1 = α2 = 2π for the remaining
waypoints. The solutions and associated initializations are
depicted in Fig. 8a, in which it is obvious that they do not
converge to the same solution and the second setup actually
performs a ﬂip which is slightly faster. This is expected due
to the non-convex properties of the problem.
However, a second set of experiments is performed with the
same initialization setups but the RQ quadrotor conﬁguration.
This conﬁguration has a minimum thrust of Tmin = 0 N,
which renders the achievable acceleration space convex. Both
setups for the RQ conﬁguration are depicted in Fig.8b. Indeed,
both initializations now converge to the same solution, which
overlay each other.
(a) Convergence to different solutions due to non-convex acceleration space.
0
5
10
15
20
px [m]
2
0
2
4
6
8
pz [m]
Initialization 1
Solution 1 
 tN = 4.171s
Initialization 2
Solution 2 
 tN = 4.115s
(b) Convergence to equal solutions due to convex acceleration space.
0
5
10
15
20
px [m]
0
2
4
6
8
pz [m]
Initialization 1
Solution 1 
 tN = 2.393s
Initialization 2
Solution 2 
 tN = 2.393s
Fig. 8: A vertical turn ﬂown starting at the origin in hover and passing through both waypoints from top to bottom, and back to the origin.
Two quadrotor conﬁgurations are used (STD in Fig. 8a and RQ in Fig. 8b), with two different initialization setups each. The ﬁrst setup
is as described in VIII with identity orientation, while the second setup uses a linearly interpolated orientation guess. The arrows indicate
the thrust direction of the quadrotor. The STD quadrotor conﬁguration converges to two different solutions in Fig. 8a depending on the
initialization due to its non-convex acceleration space with Tmin > 0 N, while the RQ quadrotor conﬁguration converges to equal (and
overlaying) solutions in Fig. 8b, due to its convex acceleration space with Tmin = 0 N.

## Page 9

9
Slalom Track
tN = 8.644 s
(a) xy-Position
20
10
0
10
20
30
40
50
60
px [m]
10
0
py [m]
(b) Velocity Proﬁle
0
2
4
6
8
t [s]
25
0
25
v [m/s]
vx
vy
vz
|v|
(c) Progress Variables
0
2
4
6
8
t [s]
0.0
0.5
1.0
progress
init
sol
Fig. 9: A track consisting of a slalom, an open hairpin and a long
stretch back, ﬂown with the RQ quadrotor conﬁguration in tN =
8.644 s. In Fig. 9a the black arrows denote the acceleration direction.
Note how the velocity approaches a steady state due to the linear
aerodynamic drag on this quadrotor, and how the progress variables
are being signiﬁcantly shifted from their initial guess.
A simple solution would be to ﬁrst solve the same problem
using a linear and therefore convex point-mass model and
using this to initialize the problem with the full quadrotor
model. We further elaborate on the convexity property in the
discussion Sec. IX-A.
E. Slalom
In a next step, a longer track is created, including a slalom
and a long straight part, with 10 waypoints in total, as in Fig.
9. The trajectory is discretized into N = 800 nodes with a
tolerance of dtol = 0.4 m. The RC quadrotor conﬁguration
is deployed in this experiment. We expect the trajectory to
smoothly slalom through the ﬁrst 6 waypoints, take an sharp
turn and accelerate back through the long straight segment.
The straight segment is on purpose spanned by 4 unequally
spaced waypoints, which together with the 6 previous way-
point provide a poor initial guess for the progress variables.
The resulting time-optimal trajectory is plotted in xy-plane
in Fig. 9a, with the velocity in Fig. 9b and the progress
variables in Fig. 9c. Note the dashed initial guess for the
progress variables in Fig. 9c, which are signiﬁcantly shifted
to enable a time-optimal waypoint allocation. Furthermore, the
velocity approaches its limit at the end of the straight segment,
due to linear aerodynamic drag in this quadrotor conﬁguration.
F. Microsoft AirSim, NIPS 2019 Qualiﬁcation 1
As an additional demonstration, we apply our algorithm on a
track from the 2019 NeurIPS AirSim Drone racing Challenge
NeurIPS Airsim Qualiﬁcation 1 Track
tN = 24.11 s
(a) xy-Position
25
0
25
50
px [m]
80
60
40
20
0
py [m]
(b) xz-Position
20
0
20
40
px [m]
0
20
40
60
pz [m]
(c) Velocity Proﬁle
0
5
10
15
20
25
t [s]
20
0
20
v [m/s]
vx
vy
vz
|v|
(d) Progress Variables
0
5
10
15
20
25
t [s]
0.0
0.5
1.0
progress
Fig. 10: The NeurIPS Airsim Qualiﬁcation 1 track, covered in tN =
24.11 s, as opposed to the best team’s 30.11 s. The top row depicts
the trajectory in xy- and xy-plane, while the second and thrid row
depict the velocity and progress respectively, plotted over time.
[33], speciﬁcally on the Qualiﬁer Tier 1 setup. We chose a
quadrotor with roughly the same properties, described as the
MS conﬁguration in Tab. I. The track is set up with the initial
pose and 21 waypoints as deﬁned in the environment provided
in [33]1. We use a discretization of N = 3360 nodes and a
tolerance of dtol = 0.1 m.
The original work by [33] also provides a simple and
conservative baseline performance of ttotal ≈110 s under
maximal velocity and acceleration of vmax = 30 m s−1 and
amax
=
15 m s−1, respectively. However, the best team
achieved a time of ttotal = 30.11 s according to the evaluation
page2. Our method generates a trajectory that passes all way-
points at a mere tN = 24.11 s. Please note that this trajectory
should only serve as a theoretical lower bound on the possibly
achievable time given the model parameters. However, the
model parameters were chosen slightly more conservative than
the actual simulated drone for the qualiﬁcation, to provide a
reasonable optimal-time solution.
1https://github.com/microsoft/AirSim-NeurIPS2019-Drone-Racing, as of
May 2020
2https://microsoft.github.io/AirSim-NeurIPS2019-Drone-Racing/
leaderboard.html, as of May 2020

## Page 10

10
25
20
15
10
5
0
5
10
15
20
25
px [m]
10
5
0
5
10
15
py [m]
Huma vs. Time-Optimal Trajectory
human tN = 10.338s
optimal tN = 9.621s
Fig. 11: Comparison of a human trajectory of tN = 10.338 s ﬂown in
simulation by an expert pilot and a time optimal trajectory of tN =
9.621 s generated by our proposed method. Note that the human pilot
is commanding collective thrust and bodyrates, which are tracked by
controller. This means that the human can not fully exploit the single
rotor thrust and therefore the true actuation limit.
G. Qualitative Human-Comparison in Simulation
In this experiment, a comparison to human ﬂown trajectories
is established. As a short foreword, we want to point out that
the human trajectories were collected in a experimental third-
party simulation, focused on good ﬂight characteristics for
human pilots, but enabling logging of the drone state.
We setup the experiment as a ﬁgure-8-shaped track as
depicted in Fig. 11. The used quadrotor model is the SIM
conﬁguration listed in Tab. I. While the mass, inertia, size,
and drag constant is set as in the nominal model, the maximal
thrust and bodyrates were ﬁxed to the maximal values the
human pilot was able to achieve with this platform in the
simulation for a more fair comparison. (corresponding to the
listed values in Tab. I). Therefore, the maximal bodyrate
was set to ωmax = 3 rad s−1, and the maximal thrust to
Tmax = 16 N. We use N = 1000 discretization nodes and
a tolerance of dtol = 0.4 m.
The human had multiple tries for preparation and also at
testing time > 10 consecutive rounds through the ﬁgure-8
track were collected, where one round starts and ends at the
trajectory point passing closest to the origin, corresponding to
the center intersection. The best lap with the lowest time was
used and is depicted in Fig. 11, with a time of 10.338 s. The
generated time-optimal trajectory takes only 9.621 s, exploit-
ing the maximal available thrust at all times, except for when
introducing and stopping quick rotations to realign the thrust
through the gate passes.
Note that the human commands bodyrate and collective
thrust, where the single rotor thrust control is left to a
simulated low-level controller, as usual for human drone ﬂight.
This however imposes limits on how much of the input space
the human can exploit, which is especially signiﬁcant given the
low thrust=to-weight ration of this drone conﬁguration. Due
to these limitations we also perform a real-world comparison
of a high-speed maneuver in the next section.
(a) xy-Position
2
0
2
4
px [m]
2
1
0
1
2
3
4
py [m]
human
optimal
(b) Acceleration Space
0.0
0.2
0.4
0.6
0.8
t [s]
40
20
0
20
40
f [N]
Thrust
fx
fy
fz
|f|
Fig. 12: Comparison of a human-ﬂown real-world trajectory to a
time-optimal trajectory, starting in the lower right corner (see Fig.
12a). The human-ﬂown maneuver was recorded in a motion capture
system and timed at thuman = 0.984 s while the optimal trajectory
reached a timing of tN = 0.874 s. The optimal trajectory exploits the
full acceleration of the quadrotor as long as possible (see Fig. 12b),
and rotates into deceleration later than the human (see Fig. 12a).
H. Qualitative Human-Comparison in Real-World
As a last experiment, we provide a qualitative comparison
of a time-optimal trajectory to a real human-ﬂown trajectory
recorded in a motion capture system. The trajectory represents
a hairpin turn around a pole (see Fig. 12), which was picked
because of its simplicity and repeatability for the human,
and because it is a common element in drone racing where
often the maximal available acceleration is exploited. the
optimization is initialized at the point where the human pilot
entered the trackable region and initial position and velocity of
the vehicle are set equal to the human’s, while the orientation
and bodyrate is left open for optimization. We then add 3
waypoints forcing the drone to pass around the pole further
away than the human, and leading the trajectory to exit at
the same point and with roughly the same exit direction as
the human. The problem is solved with N = 150 nodes and
dtol = 0.4 m using the RC quadrotor conﬁguration, modelled
after the human’s real quadrotor used for this experiment. As
in the previous experiment, we restrict the maximal thrust to
the same limit the human was able to exploit over a signiﬁcant
period of time as measured by the onboard IMU.
The maneuver is extremely quick and even the human
trajectory only lasts for 0.984 s, while the optimal solution
reduces this to 0.874 s. We can see that the time-optimal
solution has a different acceleration direction at the beginning
(see Fig. 12a), and starts to break later than the human
trajectory, achieving a slightly better time. Additionally, we
plot the the thrust (absolute and directional) in Fig. 12b and
see the common behavior of the optimization exploiting the
maximal thrust, only lowering for adjusting the rotational rates
at the beginning.
Please note that, as before, the optimization uses the nom-
inal model and is not aware of complex aerodynamic effects,
noise or disturbances. It should serve as a theoretical ceiling
or guidance for what could be achieved and as a demonstrator
that our method does indeed work.

## Page 11

11
IX. DISCUSSION
A. Convexity
While the problem of trajectory optimization quickly be-
comes non-convex when using complex and/or non-linear
dynamic models, constraints, or even cost formulations (e.g.
obstacle avoidance), it is often a valid approache to generate
feasible (in terms of model dynamics) and near optimal trajec-
tories. In our experiments, we have provoked and demonstrated
one such non-convex property, and also quickly elaborate
how one could support the optimization with an advanced
initialization scheme to start close to the global optimum.
This can be achieved by reducing the non-linear quadrotor
model into a linear point-mass model with bounded 3D
acceleration input u = a ∀∥a∥≤amax. This linear model
renders the problem convex and allows to ﬁnd a solution from
which the original problem with the quadrotor model can be
initialized, both in terms of translational trajectory, and also
with an orientation guess based on the point-mass acceleration
direction. While this initial guess is not yet a dynamically
feasible trajectory due to the absent rotational dynamics, it
serves as a good initial guess in close proximity to the optimal
solution.
B. Optimality
Our approach does not provide optimality guarantees, since
the problem by deﬁnition is non-convex and the optimal
solution, while always guaranteed to be locally optimal, does
not necessarily need to be globally optimal. Additionally, the
used implementation framework [30] and solver backend [31]
might inﬂuence the convergence behavior and the applicable
guarantees. The previously described initialization scheme
allows to mitigate these problems and, by running multiple
setups (e.g. with different orientation guesses), one could cross
check different solutions to ﬁnd the optimal one with certainty
(comparable to sampling methods).
C. Real-World Applicability
There are two problems hindering our approach from being
applied in real world scenarios.
The ﬁrst problem is posed by the nature of time-optimal
trajectories themselves, as the true solution for a given plat-
form is nearly always at the actuator constraints, and leaves
no control authority. This means that even the smallest dis-
turbance could potentially have fatal consequences for the
drone and render the remainder of the trajectory unreachable.
One has to deﬁne a margin lowering the actuator constraints
used for the trajectory generation to add control authority and
therefore robustness against disturbances. However, this also
leads to a slower solution, which is no longer the platform-
speciﬁc time-optimal one. In the context of a competition,
this effectively becomes a risk-management problem with
interesting connections to game theory.
Second, our method is computationally demanding, on a
modern laptop taking many minutes (≈1 −40min) for
scenarios as in Sec. VIII-A-VIII-D or sometimes even hours
for larger scenarios such as VIII-E-VIII-G. However, this is
highly implementation-dependent and could be vastly broken
down to usable times, or precomputed for static race tracks
and other non-dynamic environments.
X. CONCLUSION
In this work, we proposed a novel complementary progress
constraint that allows to dynamically allocate waypoints to
unknown nodes on an trajectory, and therefore ﬁnd a time-
optimal waypoint-ﬂight solution without having to sample
or allocate waypoint-completion timings. We validated our
method with many experiments in a bottom-up fashion, check-
ing against existing work, verifying the dynamic time allo-
cation, provoking and elaborating on unwanted non-convex
properties and initialization dependence. Finally, we demon-
strated our method on longer tracks with more than M ≥10
waypoints, and in a qualitative comparison against a human
expert. We conclude that our method can be used to generate
theoretical time-optimal trajectories at the actuation limit of
the platform, which serve as an upper-bound of the achievable
performance and guidance to develop fast and agile quadrotor
ﬂight.
XI. ACKNOWLEDGEMENTS
The authors want to thank Elia Kaufmann, Thomas Laengle,
Christian Pfeiffer, and our professional pilot and collaborator
Gabriel Kocher for their support and contribution throughout
this work. This work was supported by the National Centre of
Competence in Research Robotics (NCCR) through the Swiss
National Science Foundation, the SNSF-ERC Starting Grant,
and the EU H2020 Research and Innovation Program through
the AERIAL-CORE project (H2020-2019-871479).
REFERENCES
[1] H.
Moon,
J.
Martinez-Carranza,
T.
Cieslewski,
M. Faessler, D. Falanga, A. Simovic, D. Scaramuzza,
S. Li, M. Ozo, C. De Wagter, G. de Croon, S. Hwang,
S. Jung, H. Shim, H. Kim, M. Park, T.-C. Au, and
S. J. Kim.
Challenges and implemented technologies
used in autonomous drone racing.
2019.
URL https:
//link.springer.com/article/10.1007/s11370-018-00271-6.
[2] P. Foehn, D. Brescianini, E. Kaufmann, T. Cieslewski,
M. Gehrig, M. Muglikar, and D. Scaramuzza. Alphapilot:
Autonomous drone racing. Robotics: Science and Sys-
tems (RSS), 2020. URL https://link.springer.com/article/
10.1007/s11370-018-00271-6.
[3] S. M. LaValle. Planning algorithms. Cambridge univer-
sity press, 2006. URL http://planning.cs.uiuc.edu.
[4] D. Mellinger, N. Michael, and V. Kumar.
Trajectory
generation and control for precise aggressive maneuvers
with quadrotors.
Int. J. Robot. Research, 2012.
doi:
10.1177/0278364911434236.
[5] D. Mellinger and V. Kumar. Minimum snap trajectory
generation and control for quadrotors. In IEEE Int. Conf.
Robot. Autom. (ICRA), 2011. doi: 10.1109/ICRA.2011.
5980409.

## Page 12

12
[6] C. R. Hargraves and S. W. Paris.
Direct trajectory
optimization using nonlinear programming and colloca-
tion. J. Guidance, Control, and Dynamics, 1987. doi:
10.2514/3.20223.
[7] S. Bouabdallah and R. Siegwart.
Full control of a
quadrotor.
In IEEE/RSJ Int. Conf. Intell. Robot. Syst.
(IROS), 2007. doi: 10.1109/IROS.2007.4399042.
[8] R. Mahony, V. Kumar, and P. Corke. Multirotor aerial
vehicles: Modeling, estimation, and control of quadrotor.
IEEE Robot. Autom. Mag., 2012.
doi: 10.1109/MRA.
2012.2206474.
[9] M. Faessler, A. Franchi, and D. Scaramuzza. Differential
ﬂatness of quadrotor dynamics subject to rotor drag
for accurate tracking of high-speed trajectories.
IEEE
Robot. Autom. Lett., April 2018. doi: 10.1109/LRA.2017.
2776353.
[10] T. Tomi´c, P. Lutz, K. Schmid, A. Mathers, and S. Had-
dadin.
Simultaneous contact and aerodynamic force
estimation (s-cafe) for aerial robots.
Int. J. Robot.
Research, 2020. doi: 10.1177/0278364920904788.
[11] M. Faessler, D. Falanga, and D. Scaramuzza.
Thrust
mixing, saturation, and body-rate control for accurate
aggressive quadrotor ﬂight. IEEE Robot. Autom. Lett.,
April 2017. doi: 10.1109/LRA.2016.2640362.
[12] M. Bangura and R. Mahony. Real-time model predictive
control for quadrotors. IFAC World Congress, 2014. doi:
10.3182/20140824-6-za-1003.00203.
[13] M. Neunert, C. de Crousaz, F. Furrer, M. Kamel,
F. Farshidian, R. Siegwart, and J. Buchli. Fast nonlinear
model predictive control for uniﬁed trajectory optimiza-
tion and tracking.
In IEEE Int. Conf. Robot. Autom.
(ICRA), 2016. doi: 10.1109/icra.2016.7487274.
[14] D. Falanga, P. Foehn, P. Lu, and D. Scaramuzza.
PAMPC: Perception-aware model predictive control for
quadrotors. In IEEE/RSJ Int. Conf. Intell. Robot. Syst.
(IROS), 2018.
[15] C. Richter, A. Bry, and N. Roy.
Polynomial Tra-
jectory Planning for Aggressive Quadrotor Flight in
Dense Indoor Environments.
2016.
doi: 10.1007/
978-3-319-28872-7-37.
[16] M. W. Mueller, M. Hehn, and R. D’Andrea. A computa-
tionally efﬁcient algorithm for state-to-state quadrocopter
trajectory generation and feasibility veriﬁcation.
In
IEEE/RSJ Int. Conf. Intell. Robot. Syst. (IROS), 2013.
doi: 10.1109/iros.2013.6696852.
[17] R. Allen and M. Pavone. A real-time framework for kino-
dynamic planning with application to quadrotor obstacle
avoidance. In AIAA Guidance, Navigation, and Control
Conference, 2016. doi: 10.2514/6.2016-1374.
[18] N. Ratliff, M. Zucker, J A. Bagnell, and S. Srinivasa.
CHOMP: Gradient optimization techniques for efﬁcient
motion planning.
In IEEE Int. Conf. Robot. Autom.
(ICRA), 2009. doi: 10.1109/ROBOT.2009.5152817.
[19] M. Posa, S. Kuindersma, and R. Tedrake. Optimization
and stabilization of trajectories for constrained dynamical
systems. In IEEE Int. Conf. Robot. Autom. (ICRA), 2016.
doi: 10.1109/ICRA.2016.7487270.
[20] P. Foehn, D. Falanga, N. Kuppuswamy, R. Tedrake, and
D. Scaramuzza.
Fast trajectory optimization for agile
quadrotor maneuvers with a cable-suspended payload. In
Robotics: Science and Systems (RSS), 2017.
[21] M. Diehl, H. G. Bock, H. Diedam, and P. B. Wieber.
Fast direct multiple shooting algorithms for optimal robot
control. In Fast motions in biomechanics and robotics.
Springer, 2006.
[22] M. Geisert and N. Mansard. Trajectory generation for
quadrotor based systems using numerical optimal control.
In IEEE Int. Conf. Robot. Autom. (ICRA), 2016.
doi:
10.1109/ICRA.2016.7487460.
[23] F. Augugliaro, A. P. Schoellig, and R. D’Andrea. Gen-
eration of collision-free trajectories for a quadrocopter
ﬂeet: A sequential convex programming approach.
In
IEEE/RSJ Int. Conf. Intell. Robot. Syst. (IROS), 2012.
doi: 10.1109/IROS.2012.6385823.
[24] S. Vakhrameev. A bang-bang theorem with a ﬁnite num-
ber of switchings for nonlinear smooth control systems.
J. Math. Sciences, June 1997. doi: 10.1007/BF02355111.
[25] L. Poggiolini and G. Stefani. Minimum time optimality
for a bang-singular arc: Second order sufﬁcient condi-
tions. In IEEE Eur. Control Conf. (ECC), January 2006.
doi: 10.1109/CDC.2005.1582360.
[26] M. Hehn, R. Ritz, and R. D’Andrea.
Performance
benchmarking of quadrotor systems using time-optimal
control.
Auton. Robots, March 2012.
doi: 10.1007/
s10514-012-9282-3.
[27] W. Van Loock, G. Pipeleers, and J. Swevers.
Time-
optimal quadrotor ﬂight.
In IEEE Eur. Control Conf.
(ECC), 2013. doi: 10.23919/ECC.2013.6669253.
[28] S. Spedicato and G. Notarstefano. Minimum-time tra-
jectory generation for quadrotors in constrained environ-
ments. IEEE Transactions on Control Systems Technol-
ogy, 2018. doi: 10.1109/TCST.2017.2709268.
[29] G. Ryou, E. Tal, and S. Karaman. Multi-ﬁdelity black-
box optimization for time-optimal quadrotor maneuvers.
arXiv prepring: arXiv:2006.02513, June 2020.
URL
https://arxiv.org/abs/2006.02513.
[30] J. A. E. Andersson, J. Gillis, G. Horn, J. B. Rawlings,
and M. Diehl. CasADi – A software framework for non-
linear optimization and optimal control. Mathematical
Programming Computation, 2018.
[31] A. W¨achter and L. Biegler. On the implementation of an
interior-point ﬁlter line-search algorithm for large-scale
nonlinear programming.
Mathematical programming,
2006. doi: 10.1007/s10107-004-0559-y.
[32] S. Shah, D. Dey, C. Lovett, and A. Kapoor.
Air-
Sim: High-ﬁdelity visual and physical simulation for
autonomous vehicles. In Field and Service Robot., pages
621–635, 2017.
[33] R.
Madaan,
N.
Gyde,
S.
Vemprala,
M.
Brown,
K. Nagami, T. Taubner, E. Cristofalo, D. Scaramuzza,
M. Schwager, and A. Kapoor.
Airsim drone racing
lab.
PMLR post-proceedings of the NeurIPS 2019’s
Competition Track, 2020.
