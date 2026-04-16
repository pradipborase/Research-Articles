# Robust MADER Decentralized Multiagent Trajectory Planning Under Communication Delays.pdf

## Page 1

Robust MADER: Decentralized and Asynchronous Multiagent
Trajectory Planner Robust to Communication Delay
Kota Kondo, Jesus Tordesillas, Reinaldo Figueroa,
Juan Rached, Joseph Merkel, Parker C. Lusk, and Jonathan P. How
Abstract— Although
communication
delays
can
disrupt
multiagent systems, most of the existing multiagent trajectory
planners lack a strategy to address this issue. State-of-
the-art approaches typically assume perfect communication
environments,
which
is
hardly
realistic
in
real-world
experiments. This paper presents Robust MADER (RMADER),
a
decentralized
and
asynchronous
multiagent
trajectory
planner that can handle communication delays among agents.
By broadcasting both the newly optimized trajectory and
the committed trajectory, and by performing a delay check
step, RMADER is able to guarantee safety even under
communication
delay.
RMADER
was
validated
through
extensive simulation and hardware flight experiments and
achieved a 100% success rate of collision-free trajectory
generation, outperforming state-of-the-art approaches.
SUPPLEMENTARY MATERIAL
Video: https://youtu.be/vH09kwJOBYs
I. INTRODUCTION
Multiagent UAV trajectory planning has been extensively
studied in the literature for its wide range of applications.
These planners can be centralized [1], [2], [3] (one machine
plans every agent’s trajectory) or decentralized [4], [5], [6]
(each agent plans its own trajectory). Decentralized planners
are more scalable and robust to failures of the centralized
machine. Despite these advantages, a decentralized scheme
requires communication between the agents, and commu-
nication delays could potentially introduce failure in the
trajectory deconfliction between the agents, which is essential
to guarantee safety [7]. multiagent planners can also be
classified according to whether or not they are asynchronous.
In an asynchronous setting, each agent independently triggers
the planning step without considering the planning status
of other agents. Asynchronous approaches do not require a
synchronous mechanism among agents and therefore more
scalable than synchronous approaches, but they are also
more susceptible to communication delays since agents are
planning and executing trajectories independently.
Many decentralized state-of-the-art trajectory planners do
not consider communication delays or explicitly state as-
sumptions about communication. For example, the planners
presented in SCP [8], decNS [9], and LSC [10] are decen-
tralized and synchronous, but SCP and decNS implicitly and
Aerospace Controls Laboratory, MIT, 77 Massachusetts Ave, Cambridge,
MA,
USA
{kkondo, jtorde, reyfp, jrached, jamerkel,
plusk, jhow}@mit.edu
(a) Hardware experiments: 6 UAVs running RMADER onboard.
Despite the existence of communication delays between the agents,
RMADER can guarantee safety.
(b) Simulation experiments: 50 UAVs in a circle configuration
successfully exchange their positions despite the 100 ms communi-
cation delay introduced on purpose. The color denotes the velocity
(red higher and blue lower).
Fig. 1.
RMADER Hardware and Simulation Results
LSC explicitly assume a perfect communication environment
without any communication delays.
The algorithm decMPC [11] is decentralized, but it re-
quires synchronicity and communication delays to be within
a fixed planning period. decGroup [12] is a decentralized
semi-asynchronous planner, which solves joint optimization
as a group. decGroup cooperatively tackles the path-planning
problem but implicitly assumes no communication delays.
1

## Page 2

TABLE I.
State-of-the-art Decentralized Multiagent Planners.
Method
Asynchronous?
Handles Comm.
Delay?
Hardware
Demonstration
SCP [8]
decNS [9]
LSC [10]
No
No
Yes
decMPC [11]
No
Yes
No
decGroup [12]
Yes/No2
No
Yes
ADPP [13]
Yes3
No
Yes
MADER [4]
Yes
No
No
EGO-
Swarm [5]
Yes
No
Yes
AsyncBVC [14]
Yes
Yes
No
RMADER
(proposed)
Yes
Yes
Yes
2decGroup triggers joint-optimization in dense environments and switches
to a centralized, synchronous planner.
3Asynchronous but requires priority information for planning.
ADPP [13] is asynchronous1 and decentralized, but it as-
sumes perfect communication without delay. Our previous
work MADER [4] is asynchronous and decentralized but
assumes no communication delays. EGO-Swarm [5] also
proposes a decentralized, asynchronous planner that requires
agents to periodically broadcast a trajectory at a fixed
frequency, and each agent immediately performs collision
checks upon receiving the message. EGO-Swarm is the first
fully decentralized, asynchronous trajectory planner success-
fully demonstrating hardware experiments, yet it still suffers
from a collision due to communication delays, as shown
in Section III. AsyncBVC [14] proposes an asynchronous
decentralized trajectory planner that can guarantee safety
even with communication delays. However, the future tra-
jectories are constrained by past separating planes, which
can overconstrain the solution space and hence increase the
conservatism. Also, they only presented simulation results
with up to 4 agents, and no hardware experiments were
implemented. In addition, it relies on discretization when
solving the optimization problem, meaning that safety is
only guaranteed on the discretization points. Our approach
instead is able to guarantee safety in a continuous approach
by leveraging the MINVO basis [15].
To address these shortcomings, we propose Robust
MADER (RMADER), a decentralized and asynchronous
multiagent trajectory planner capable of generating collision-
free trajectories in the presence of realistic communication
delays. As shown in Table I, RMADER is the first ap-
proach to demonstrate decentralized, asynchronous trajectory
planning robust to communication delays. RMADER builds
on convex MADER, which is a modified version of the
nonconvex MADER presented in our previous work [4]
(more details are available in Appendix I). Our contributions
include:
1) An algorithm that guarantees collision-free trajectory
generation even with the existence of communication
1As in [4], we define asynchronous planning to be when the agent triggers
trajectory planning independently without considering the planning status of
other agents. However, ADPP [13] implements a prioritized asynchronous
approach, meaning plannings are not fully independently triggered.
delays among vehicles.
2) Extensive simulations comparing our approach to state-
of-the-art methods under communication delays that
demonstrate a 100% success rate of collision-free
trajectory generation (see Table V).
3) Extensive set of decentralized hardware experiments
using 6 UAVs, and achieving velocities up to 3.4 m/s.
II. TRAJECTORY DECONFLICTION
In MADER [4] and RMADER, UAVs plan trajectories
asynchronously and broadcast the results to each other.
Each agent uses these trajectories as constraints in the
optimization problem. Assuming no communication delays
exist, safety can be guaranteed using our previous approach
presented in MADER (summarized in Section II-A). This
safety guarantee, however, breaks when an agent’s planned
trajectory is received by other agents with some latency.
Section II-B shows how RMADER guarantees safety even
with communication delays. We use the definitions shown in
Table II.
A. MADER Deconfliction
MADER [4] guarantees collision-free trajectories under
ideal communication through the use of the planning stages
shown in Fig. 2. An agent plans its initial trajectory during
Optimization (O), followed by Check (C) to ensure its plan
does not lead to a collision. Finally, Recheck (R) is used to
check if the agent received any trajectory updates from other
agents during C - if so, an agent starts over planning at O.
Although MADER does not have explicit safety guarantees
in the presence of communication delays, its trajectories are
still collision free for cases 1 and 2 shown in Fig. 2. However,
collisions may occur in cases 3 and 4 of Fig. 2. These four
cases are summarized in Fig. 2 and Table III.
B. Robust MADER Deconfliction
To achieve robustness to communication delays, we re-
place the Recheck with Delay Check (DC), where each
agent repeatedly checks if its newly optimized trajectory
conflicts with other agents’ trajectories. If an agent detects
conflicts during DC, it discards the new trajectory and starts
another O while executing its previous trajectory. If no
collisions are detected in DC, it starts executing the new
trajectory. To guarantee collision-free trajectory generation,
DC needs to be longer than the possible longest commu-
nication delay (i.e., δDC ≥δmax). That way, an agent can
always keep at least one collision-free trajectory. It could,
TABLE II.
Definitions of the different delay quantities: Note that, by
definition, 0 ≤δintrod ≤δactual ≤δmax. See also Figs 6f and 7 for the
actual histogram of the delays in simulation and hardware, respectively.
δactual
Actual communication delays among agents.
δmax
Possible maximum communication delay.
δintrod
Introduced communication delay in simulations.
δDC
Length of Delay Check in RMADER.
To guarantee safety, δmax ≤δDC must be satisfied.
2

## Page 3

Agent A
Agent B
tA
trajA
time
trajA
case 1
case 2
case 3
case 4
Optimization (OA)
Check (CA)
Recheck (RA)
OB
CB
RB
Prev. iter.
Next iter.
Prev. iter.
Next iter.
Fig. 2.
MADER deconfliction: Agent A solves OA to find its optimal tra-
jectory, constrained by other agents’ trajectories. Agent A then begins CA to
determine if that generated trajectory has any conflicts with trajectories received
during OA. Finally, in RA, Agent A checks if it received any trajectories during
C. The four cases shown in the figure correspond to different communication
delays, resulting in trajA being received by Agent B at different times. Designed
to guarantee safety when there is no communication delays, MADER also
guarantees safety when trajA arrives during OB (Case 1) or CB (Case 2), but
could cause collisions if trajA is received during/after (Case 3/4) RB.
Agent A
Agent B
ttrajAnew
ttrajA
time
trajAnew
trajA
case 1 case 2
case 3
case 4
OA
CA
DCA
OB
CB
DCB
Prev. iter.
Next iter.
Prev. iter.
Next iter.
Fig. 3.
RMADER deconfliction: After CA Agent A keeps executing
the trajectory from the previous iteration, trajAprev, while checking
potential collisions of newly optimized trajectory, trajAnew. This is
because trajAnew might have conflicts due to communication delays and
need to be checked in DCA, and trajAprev is ensured to be collision-
free. If collisions are detected in either CA or DCA, Agent A keeps
executing trajAprev
(i.e., trajA ←trajAprev ). If DCA does not detect
collisions, Agent A broadcasts and starts implementing trajAnew (i.e.,
trajA ←trajAnew).
TABLE III.
Safety guarantees under communication delays: Depending on
when trajA is received by Agent B, the deconfliction takes place at different
stages. MADER does not guarantee safety if trajA is received during RB
or during the following iteration, while RMADER guarantees safety in all
the cases. Note that in RMADER, if Agent B does not receive trajA by the
end of DCB, then the deconfliction is performed by Agent A (specifically,
in CA or DCA) and not by Agent B. Agent A will use trajBnew and/or trajB
for this.
MADER
When trajA received
OB
(Case 1)
CB
(Case 2)
RB
(Case 3)
Next iter.
(Case 4)
trajA deconflicted?
When?
Yes
CB
Yes
RB
No
No
RMADER
When trajAnew/trajA
received
OB
(Case 1)
CB
(Case 2)
DCB
(Case 3)
Next iter.
(Case 4)
trajAnew/trajA
deconflicted? When?
Yes
CB
Yes
DCB
Yes
DCB
Yes
CA or DCA
however, not be ideal for introducing such a long δDC,
and therefore, in Section III we also tried δDC < δmax
and measure its performance. Fig. 3 shows how RMADER
deals with communication delays. Furthermore, Table III
shows all the possible cases in which communication delays
could occur and how these are handled by RMADER to
generate collision-free trajectories even with communication
delays. The pseudocode of RMADER deconfliction is given
in Algorithm 1. First, Agent B runs O to obtain trajBnew
and broadcasts it if C is satisfied (Line 6). This C aims
to determine if trajBnew has any conflicts with trajectories
received in O. Then, Agent B commits either
trajBprev
or
trajBnew - if DC detects conflicts, Agent B commits to trajBprev
(Line 8), and if DC detects no conflicts, trajBnew (Line 10).
This committed trajectory is then broadcast to the other
agents (Line 11). Table IV highlights the differences between
MADER and RMADER.
Agent B stores the trajectories received from other agents
in a set QB; for example, for each Agent J, Agent B will
store the committed trajectory of Agent J, trajJ, and possibly
the newly optimized trajectory trajJnew if any new committed
trajectory has still not been broadcast. Figure 4 shows the
way Agent B stores trajectories from Agent A. QB is used
in O, Check, and DC, where Agent B checks for collision
Algorithm 1 Robust MADER - Agent B
Require: trajB, a feasible trajectory
1: while not goal reached do
2:
trajBnew = Optimization()
3:
if Check(trajBnew) == False then
4:
Go to Line 2
5:
end if
6:
Broadcast trajBnew
7:
if Delay Check(trajBnew) == False then
8:
trajB ←trajBprev , and go to Line 11
9:
end if
10:
trajB ←trajBnew
11:
Broadcast trajB
12: end while
TABLE IV.
Differences between MADER and RMADER
MADER
RMADER
Upon successful C and R, the
newly optimized trajectory is
broadcast to other agents
Upon successful C, trajJnew is
broadcast. After DC, the
committed trajectory trajJ (which
is either trajJnew and trajJprev
depending on whether DC is
satisfied or not) is broadcast
R is a Boolean check to see if the
agent received traj. in C
DC is a sequence of collision
checks
R is very short
DC lasts δDC seconds
Algorithm 2 Delay Check - Agent B
1: function Delay Check(trajBnew)
2:
for δDC seconds do
3:
if trajBnew collides with any trajectory in QB then
4:
return False
5:
end if
6:
end for
7:
return True
8: end function
3

## Page 4

Fig. 4.
Agent B stores in QB the last committed trajectory of Agent A.
It will also contain the newly optimized trajectory trajAnew while the new
committed trajectory has still not been received by Agent B.
(a) For Agent J, the colored trajectory
is the committed (safety-guaranteed)
trajectory (trajJ), and the grey trajec-
tory is the newly optimized trajectory
(trajJnew).
(b) Actual trajectories flown by the
agents. All 10 agents successfully
swap their positions in a circle con-
figuration.
Fig. 5.
10 agents employing RMADER exchange their positions in a circle
of radius 20 m. In the colored trajectories, red represents a high speed while
blue denotes a low speed.
against all the trajectories stored in QB. Note that QB is
updated in parallel with O and DC. At the beginning of OB,
an agent generates an optimal trajectory, trajBnew, using all the
trajectories stored in QB as constraints, and then, Agent B
checks for trajBnew’s potential collisions against QB, which is
updated in optimization. Finally, Agent B repeatedly checks
for collisions against QB in DCB, which lasts for δDC. Note
that C is not necessary to guarantee safety in RMADER - O
followed by DC alone can generate collision-free trajectories
as long as δDC ≥δmax holds. Though C detects collisions
before broadcasting any (possibly conflicted) trajectories
and allows an agent to start another O, which prevents
unnecessary communication.
III. SIMULATION RESULTS
We
tested
Slow
EGO-Swarm,
EGO-Swarm
[5],
MADER [4], and RMADER (proposed) on a general-
purpose-N2 Google Cloud instance with 32 Intel Core
i7s. In each scenario, we conducted 100 simulations with
10 agents positioned in a 10 m radius circle, exchanging
positions diagonally as shown in Fig. 5. Note that this paper
convexified MADER optimization problem as detailed in
Appendix I, and we used the convex optimization problem
for both MADER and RMADER. The maximum dynamic
limits (velocity, acceleration, and jerk) for these algorithms
are set to 10 m/s, 20 m/s2, and 30 m/s3. EGO-Swarm
carries out a sequential startup - agents commits their first
trajectory in a pre-determined order to avoid unnecessary
trajectory conflicts. We also introduced 0.25 s-apart startup
into MADER and RMADER.
Slow EGO-Swarm is EGO-Swarm with smaller dynamic
limits. We first tested EGO-Swarm with default parameters
provided in [5] and saw a significant number of conflicts.
Therefore we increased the weights of the collision costs in
EGO-Swarm’s cost function up to 1000 (we tried more than
1000, but it did not change the results) while other weights
(s.t. trajectory feasibility) are on the order of single digits;
however, we still observed collisions (as seen in the second
row of Table V). We thus decreased the maximum velocity
and acceleration of EGO-Swarm down to 5 m/s and 10 m/s2,
which we define as Slow EGO-Swarm.
Although we introduced a fixed δintrod for simulated com-
munications, δactual can be larger due to the simulation
computer’s computational limitations. The communication
delays observed in simulation are shown in Fig. 6f for five
nominal values of δintrod (δintrod = 0, 50, 100, 200, and 300
ms). As long as δDC ≥δmax holds, RMADER can generate
collision-free trajectories.
Table V and Fig. 6 showcase each approach’s performance
in simulations. RMADER was implemented in the case of
(1) δDC ≥δmax (δDC > 100th percentile of δactual) and (2)
δmax ≥δDC (δDC ≈75th percentile of δactual). When δDC ≥
δmax holds, collision-free trajectory planning is guaranteed,
and therefore RMADER generates 0 collisions for all the
δintrod, while other approaches suffer collisions. As expected,
the longer δintrod more collisions Slow EGO-Swarm, EGO-
Swarm, and MADER generate. In the case of (2) δmax ≥δDC,
although safety is not theoretically guaranteed, since δDC is
long enough, RMADER succeeds to generate collision-free
trajectories. Note that Case (2) could have collisions in case
agents have conflicted trajectories and their trajectories fall
into the rest of ≈25%.
It is also worth mentioning that RMADER’s robustness
to communication delays is obtained by layers of conflict
checks and agents periodically occupying two trajectory
spaces, which can result in generating conservative trajecto-
ries and trading off UAV performance. Avg. Number of Stops
in Table V, for instance, suggests more stoppage than other
approaches. As
R
∥a∥2 dt and
R
∥j∥2 dt show RMADER’s
trajectories are less smooth than MADER, and RMADER
takes longer Travel Time than others (Slow EGO-Swarm
takes more but that is because of its smaller dynamic limits,
and therefore a direct comparison is not fair).
IV. HARDWARE EXPERIMENTS
A total of 10 hardware experiments (5 flights for each)
demonstrate RMADER’s robustness to communication de-
lays as well as MADER’s shortcomings. Each flight test
had 6 UAVs in the 9.2 m × 7.5 m × 2.5 m flight space and
lasted ≈1 min. The collision-safety boundary box around
each UAV was set to 0.8 m × 0.8 m × 1.5 m. Note that the z
component of this boundary box is larger to avoid the effects
of downwash from other agents. All the planning and control
run onboard the UAV, and the state estimation is obtained by
4

## Page 5

TABLE V.
Cases δintrod = 0 ms, δintrod = 50 ms, δintrod = 100 ms, (see Fig. 6f for actual message delays). The bold values represent the case where
δDC ≥δmax, which is the necessary condition to ensure safety.
Method
δDC [ms]
Collision
[%]
Avg number
of stops
R
∥a∥2 dt
[m2/s3]
R
∥j∥2 dt
[m2/s5]
Travel Time [s]
Avg
Max
Slow
EGO-Swarm
N/A
14|25|22
0|0|0
109.8|113.2|113.5
15388.2|15491.5|15486.2
11.65|11.67|11.76
11.93|11.99|12.97
EGO-Swarm
N/A
64|84|84
0.004|0.0|0.01
662.5|700.7|787.9
90721.9|94611.9|104160.3
7.19|7.24|7.28
7.38|7.51|7.63
MADER
(convex)
N/A
15|38|42
0.0|0.001|0.0
78.09|74.19|74.74
1595.9|1643.6|1638.5
6.28|6.25|6.26
7.15|7.35|7.04
RMADER
(proposed)
100|130|200
(>100th percentile of δactual
and δDC ≥δmax holds)
0|0|0
0.46|0.347|1.751
127.7|147.9|190.5
2939.4|3712.4|5942.1
7.28|7.95|10.35
8.41|8.80|11.91
25|56|105
(≈75th percentile of δactual
so δDC ≥δmax does not hold)
0|0|0
0.001|0.007|0.086
99.52|112.0|137.7
1844.3|2142.3|3056.2
6.80|6.87|7.30
7.66|8.02|8.89
0
50
100
150
200
250
300
δintrod [ms]
0
20
40
60
80
100
Collision-free Traj. Rate [%]
RMADER (proposed)
MADER
EGO-Swarm
Slow EGO-Swarm
(a) Collision-free Trajectory Rate
0
50
100
150
200
250
300
δintrod [ms]
6
7
8
9
10
11
12
13
14
15
16
17
18
Travel Time [s]
RMADER (proposed)
MADER
EGO-Swarm
Slow EGO-Swarm
(b) Travel Time - shaded parts indicate its maximum
and minimum value.
0
50
100
150
200
250
300
δintrod [ms]
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
Number of Stops
RMADER (proposed)
MADER
EGO-Swarm
Slow EGO-Swarm
(c) Number of Stops
0
50
100
150
200
250
300
δintrod [ms]
100
200
300
400
500
600
700
800
R
∥a∥2 dt [m2/33]
RMADER (proposed)
MADER
EGO-Swarm
Slow EGO-Swarm
(d) Trajectory Smoothness (Acceleration)
0
50
100
150
200
250
300
δintrod [ms]
0
20000
40000
60000
80000
100000
120000
R
∥j∥2 dt [m2/35]
RMADER (proposed)
MADER
EGO-Swarm
Slow EGO-Swarm
(e) Trajectory Smoothness (Jerk)
0
50
100
150
200
250
300
350
actual [ms]
0%
20%
40%
60%
80%
Probability
introd. =0ms
introd. =50ms
introd. =100ms
introd. =200ms
introd. =300ms
(f) Distribution of δactual in simulations. Due to
computer’s computational limits, messages do not
travel instantly.
Fig. 6.
100 Flight Simulation Results: Fig. 6a shows RMADER generates collision-free trajectory at 100%, while other state-of-the-art approaches fail
when communication delays are introduced. To maintain collision-free trajectory generation, RMADER periodically occupies two trajectories, and other
agents need to consider two trajectories as a constraint, which could lead to conservative plans - longer Travel Time and more Avg. Number of Stops. This
is a trade-off between safety and performance. MADER reports a few collided trajectory because δactual > 0 ms.
0
100
200
300
400
500
600
actual [ms]
0.0%
5.0%
10.0%
15.0%
20.0%
Probability
MADER
RMADER
Fig. 7.
Distribution of δactual in hardware experiments: Both MADER and
RMADER were tested in 5 flight experiments. Compared to simulations
(see the case δintrod = 0 ms in Fig. 6f), δactual is much larger in hardware.
TABLE VI.
RMADER hardware experiments: Maximum velocity and
flight distance (sum of the distances of each UAV) in the five experiments
Exp. 1
Exp. 2
Exp. 3
Exp. 4
Exp.5
Max vel. [m/s]
2.6
2.7
3.4
2.8
2.7
Flight distance [m]
268.7
330.7
309.3
354.0
351.6
fusing IMU measurements with an external motion capture
system. A safety mechanism running in parallel reports
potential collisions and sends commands to the UAVs to
avoid colliding.
During the MADER hardware experiments due to the
effects of communication delays, 7 potential collisions were
detected by the safety mechanism. RMADER, on the other
5

## Page 6

t = 0 s: Agent 1 is following its trajectory
t = 0.15 s: Agent 1 and Agent 2 published their trajnew only 10 ms apart. Due to
communication delays each agent did not consider the other trajectory, and thus these
two trajectories are in conflicts. Note that we have a 1.5 m-tall boundary box, and
thus these trajectories are in collision.
t = 1.01 s: During Delay Check both agents detected conflicts and did not commit
their trajectory.
t = 1.97 s: Collision avoided.
Fig. 8.
RMADER Successful Deconfliction under Communication Delays
hand, did not generate conflicts. A snapshot of one of the
RMADER experiments is shown in Fig. 1a, and a successful
trajectory deconfliction despite the communication delay is
shown in Fig. 8. The maximum velocities and flight distances
achieved during the RMADER hardware experiments are
shown in Table VI. The UAVs achieved maximum velocity
of 3.4 m/s in the third RMADER experiment.
V. CONCLUSIONS AND FUTURE WORK
We proposed RMADER, a decentralized and asyn-
chronous multiagent trajectory planner that is robust to
communication delays. The key property of RMADER is
TABLE VII.
Convex MADER vs Nonconvex MADER
Method
Computation
Time [ms]
R
∥a∥2 dt
[m2/s3]
R
∥j∥2 dt
[m2/s5]
Number
of Stops
Travel
Time [s]
Travel
Distance [m]
Avg
Max
convex
MADER
31.08
433.0
103.5
2135.0
0.18
16.05
75.24
nonconvex
MADER 39.23
724.0
441.93
20201.8
0.16
9.93
75.80
that it guarantees safety even when there are communication
delays. RMADER guarantees collision-free trajectories by
introducing a delay check mechanism and keeping at least
one collision-free trajectory available throughout planning.
Simulation and hardware experiments showed RMADER’s
robustness to communication delays and the trade-off be-
tween safety and performance. Potential future work includes
implementing VIO for localization and larger scale hardware
experiments.
APPENDIX I
CONVEX VS NONCONVEX MADER
Our prior work MADER [4] formulated a nonconvex
optimization problem by using both the control points and
the separating planes as decision variables [4, Section VI-D].
This could, however, cause expensive onboard computation.
Therefore we re-formulated the problem as convex by fix-
ing the separating planes in the optimization (i.e., by not
including these planes as decision variables). In addition, to
generate smoother trajectories, we added a constraint on the
maximum jerk.
We
compared
both
version
on
a
general-purpose-N2 Google Cloud instance with 32
Intel® Core i7. The flight space contains 250 dynamic and
static obstacles, and the UAV must fly through the space to
reach a goal 75 m away. Maximum velocity/acceleration/jerk
are set to 10 m/s / 20 m/s2 / 30 m/s3. The performance
was measured in terms of Computation Time, trajectory
smoothness indicated by
R
∥a∥2 dt and
R
∥j∥2 dt, Number
of Stops, Travel Time, and Travel Distance. The results are
shown in Table VII, where all data is the average of 100
simulations. The notation
R
∥a∥2 dt and
R
∥j∥2 dt refers
to the time integral of squared norm of the acceleration
and jerk along the trajectory, respectively. Higher values
therefore represent a less smooth trajectory. Number of
Stops is the number of times the UAV had to stop on its
way to the goal. Table VII indicates that convex MADER
is computationally less expensive and generates smoother
trajectories, but nonconvex MADER performs better in
terms of the Number of Stops and Travel Time. Since convex
MADER has a computational advantage and can generate
smoother trajectories, we implemented convex MADER for
MADER and RMADER in all the simulations and hardware
experiments in this paper.
ACKNOWLEDGMENT
We would like to thank Nick Rober, Lakshay Sharma,
Miguel Calvo-Fullana, Andrea Tagliabue, Dong-Ki Kim,
and Jeremy Cai, for their help, discussions, and insightful
6

## Page 7

comments on this paper. This research is funded in part by
Boeing Research & Technology.
REFERENCES
[1] J. Park, J. Kim, I. Jang, and H. J. Kim, “Efficient Multi-Agent Tra-
jectory Planning with Feasibility Guarantee using Relative Bernstein
Polynomial,” in 2020 IEEE International Conference on Robotics and
Automation (ICRA), May 2020, pp. 434–440, iSSN: 2577-087X.
[2] G. Sharon, R. Stern, A. Felner, and N. R. Sturtevant, “Conflict-based
search for optimal multi-agent pathfinding,” Artificial Intelligence,
vol.
219,
no.
C,
pp.
40–66,
Feb.
2015.
[Online].
Available:
https://doi.org/10.1016/j.artint.2014.11.006
[3] D. R. Robinson, R. T. Mar, K. Estabridis, and G. Hewer, “An Effi-
cient Algorithm for Optimal Trajectory Generation for Heterogeneous
Multi-Agent Systems in Non-Convex Environments,” IEEE Robotics
and Automation Letters, vol. 3, no. 2, pp. 1215–1222, Apr. 2018,
conference Name: IEEE Robotics and Automation Letters.
[4] J. Tordesillas and J. P. How, “Mader: Trajectory planner in multiagent
and dynamic environments,” IEEE Transactions on Robotics, vol. 38,
no. 1, pp. 463–476, 2022.
[5] X. Zhou, J. Zhu, H. Zhou, C. Xu, and F. Gao, “EGO-Swarm: A
Fully Autonomous and Decentralized Quadrotor Swarm System in
Cluttered Environments,” Nov. 2020, arXiv:2011.04183 [cs] version:
1. [Online]. Available: http://arxiv.org/abs/2011.04183
[6] P. C. Lusk, X. Cai, S. Wadhwania, A. Paris, K. Fathian, and J. P. How,
“A Distributed Pipeline for Scalable, Deconflicted Formation Flying,”
IEEE Robotics and Automation Letters, vol. 5, no. 4, pp. 5213–5220,
Oct. 2020, conference Name: IEEE Robotics and Automation Letters.
[7] J.
Gielis,
A.
Shankar,
and
A.
Prorok,
“A
Critical
Review
of Communications in Multi-robot Systems,” Current Robotics
Reports, Aug. 2022. [Online]. Available: https://doi.org/10.1007/
s43154-022-00090-9
[8] Y. Chen, M. Cutler, and J. P. How, “Decoupled multiagent path
planning via incremental sequential convex programming,” in 2015
IEEE International Conference on Robotics and Automation (ICRA),
May 2015, pp. 5954–5961, iSSN: 1050-4729.
[9] S. Liu, K. Mohta, N. Atanasov, and V. Kumar, “Towards Search-
based Motion Planning for Micro Aerial Vehicles,” Oct. 2018,
arXiv:1810.03071 [cs]. [Online]. Available: http://arxiv.org/abs/1810.
03071
[10] J. Park, D. Kim, G. C. Kim, D. Oh, and H. J. Kim, “Online Distributed
Trajectory Planning for Quadrotor Swarm With Feasibility Guarantee
Using Linear Safe Corridor,” IEEE Robotics and Automation Letters,
vol. 7, no. 2, pp. 4869–4876, Apr. 2022, conference Name: IEEE
Robotics and Automation Letters.
[11] C. Toumieh and A. Lambert, “Decentralized Multi-Agent Planning
Using Model Predictive Control and Time-Aware Safe Corridors,”
IEEE Robotics and Automation Letters, vol. 7, no. 4, pp. 11 110–
11 117, Oct. 2022, conference Name: IEEE Robotics and Automation
Letters.
[12] J. Hou, X. Zhou, Z. Gan, and F. Gao, “Enhanced Decentralized
Autonomous Aerial Swarm with Group Planning,” Mar. 2022,
arXiv:2203.01069 [cs]. [Online]. Available: http://arxiv.org/abs/2203.
01069
[13] M. C´ap, P. Nov´ak, M. Seleck´y, J. Faigl, and J. Vokffnek, “Asyn-
chronous decentralized prioritized planning for coordination in multi-
robot system,” in 2013 IEEE/RSJ International Conference on Intel-
ligent Robots and Systems, Nov. 2013, pp. 3822–3829, iSSN: 2153-
0866.
[14] S. Baskin and G. Sukhatme, “Asynchronous Real-time Decentralized
Multi-Robot Trajectory Planning,” IEEE/RSJ International Conference
on Intelligent Robots and Systems, Oct. 2022.
[15] J. Tordesillas and J. P. How, “MINVO Basis: Finding Simplexes
with Minimum Volume Enclosing Polynomial Curves,” Computer-
Aided Design, vol. 151, no. C, Oct. 2022. [Online]. Available:
https://doi.org/10.1016/j.cad.2022.103341
7
