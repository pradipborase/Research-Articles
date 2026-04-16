# DDQN-Based 3D Path Planning Algorithm for UAVs in Dynamic Dense Obstacle Environments.pdf

## Page 1

DDQN-Based 3D Path Planning Algorithm for
UAVs in Dynamic Dense Obstacle Environments
Wenjie Zhang, Meng Yu, Yin Wang苣
(School of Astronautics, Nanjing University of Aeronautics and Astronautics,
Nanjing 211106, China)
Abstract:  Online three-dimensional (3D) path planning in dynamic environments is a fundamen-
tal problem for achieving autonomous navigation of unmanned aerial vehicles (UAVs). However,
existing methods struggle to model traversable dynamic gaps, resulting in conservative and subopti-
mal trajectories. To address these challenges, this paper proposes a hierarchical reinforcement learn-
ing  (RL)  framework  that  integrates  global  path  guidance,  local  trajectory  generation,  predictive
safety evaluation, and neural network-based decision-making. Specifically, the global planner pro-
vides long-term navigation guidance, and the local module then utilizes an improved 3D dynamic
window  approach  (DWA)  to  generate  dynamically  feasible  candidate  trajectories.  To  enhance
safety in dense dynamic scenarios, the algorithm introduces a predictive axis-aligned bounding box
(AABB) strategy to model the future occupancy of obstacles, combined with convex hull verifica-
tion for efficient trajectory safety assessment. Furthermore, a double deep Q-network (DDQN) is
employed with structured feature encoding, enabling the neural network to reliably select the opti-
mal trajectory from the candidate set, thereby improving robustness and generalization. Compara-
tive experiments conducted in a high-fidelity simulation environment show that the algorithm out-
performs existing algorithms, reducing the average number of collisions to 0.2 while shortening the
average task completion time by approximately 15%, and achieving a success rate of 97%.
Keywords:  unmanned  aerial  vehicle  (UAV)  three-dimensional  (3D)  path  planning;  3D  dynamic
window approach (DWA); predictive axis-aligned bounding box (AABB); double deep Q-network
(DDQN); autonomous navigation
 
 1    Introduction
The  application  of  unmanned  aerial  vehicles
(UAVs) in urban air mobility, emergency rescue,
and low-altitude logistics has demonstrated their
remarkable flexibility  and  efficiency.  In   particu-
lar, three-dimensional (3D) path planning allows
UAVs to achieve autonomous flight and dynamic
obstacle avoidance. Existing path planning meth-
ods  have  made  significant  progress  in  static  or
low-dynamic  environments.  However,  they  still
face  challenges  in  environments  with  dense  and
rapidly changing dynamic obstacles. These chal-
lenges  mainly  involve  insufficient  accuracy  in
modeling dynamic obstacles and the high compu-
tational  complexity  of  path  optimization.  These
challenges make it difficult for traditional meth-
ods  to  guarantee  safety  and  efficiency  in  high-
speed flight  or  complex  scenarios.  These   chal-
lenges  place  greater  demands  on  the  robustness
and efficiency of path planning algorithms.
In  complex  dynamic  environments,  UAVs
need  to  generate  executable  trajectories  that
meet  real-time  requirements  while  ensuring
  
Manuscript  received  Jul.  29,  2025;  revised  Sep.  4,  2025;
accepted Sep. 8, 2025. The associate editor coordinating the
review of this manuscript was Dr. Haibin Duan. This work
was  supported  by  the  Postgraduate  Research  &  Practice
Innovation  Program  of  Nanjing  University  of  Aeronautics
and Astronautics (NUAA) (No. xcxjh20251502).
苣Corresponding author. Email: yinwangee@nuaa.edu.cn
DOI: 10.15918/j.jbit1004-0579.2025.044
Journal of Beijing Institute of Technology，2026，Vol. 35，No. 1
—  84  —

## Page 2

global  efficiency  and  safety  in  a  time-varying,
partially observable  3D  airspace.  The   coexis-
tence  of  these  multiple  constraints  makes  path
planning  a  core  challenge  in  autonomous  drone
flight [1].
For  sampling-based  methods,  Karaman  and
Frazzoli  [2]  proposed  rapidly-exploring  random
tree star (RRT*), which efficiently explores high-
dimensional  spaces  with  asymptotic  optimality,
but  its  adaptability  in  dynamic  environments  is
limited. Kavraki et al. [3] developed probabilistic
roadmap method (PRM), which improves global
coverage  but  struggles  with  replanning  in
dynamic  scenarios.  In  search-based  planning,
Hart et al. [4] introduced A-star algorithm (A*),
and Likhachev et al. [5] proposed anytime repair-
ing  A*  (ARA*),  both  effective  in  ensuring  cost
consistency. However,  their  computational   bur-
den  in  3D  time-varying  fields  limits  real-time
UAV  navigation.  For  optimization  and  control
approaches, Fox et al. [6] presented the dynamic
window  approach  (DWA),  enabling  real-time
obstacle  avoidance  under  kinematic  constraints.
Qin and Badgwell [7] reviewed model predictive
control  (MPC),  and  Ljungqvist  [8]  extended
feedback control strategies to large vehicles. Yet
these methods are inherently local, prone to sub-
optimal traps, and restricted by field-of-view lim-
itations. Loquercio et al. [9] further showed that
such  drawbacks  become  critical  in  high-speed
UAV flight.
To  overcome  these  issues,  researchers  have
explored  deep  reinforcement  learning  (DRL).
Zhong et al. [10] employed a modified deep deter-
ministic  policy  gradient  (DDPG)  framework  to
optimize UAV trajectories with network connec-
tivity, improving efficiency. Chikhaoui et al. [11]
applied  proximal  policy  optimization  (PPO)-
based reinforcement learning (RL) to UAV navi-
gation in urban environments and demonstrated
its  adaptability.  Tai  et  al.  [12]  used  virtual-to-
real  transfer  to  enhance  sample  efficiency,  and
Pfeiffer  et  al.  [13]  combined  reinforcement  with
imitation learning to stabilize training. Hester et
al.  [14]  reduced  exploration  costs  by  integrating
demonstrations.  However,  Chou  [15]  highlighted
that end-to-end DRL policies remain sensitive to
noise and delays, often lacking safety margins in
practice.
A
 compromise
 approach
 has
 recently
emerged to  mitigate  such  instability  by   decom-
posing path planning into two stages: trajectory
generation  and  selection.  Faust  et al.  [16]  pro-
posed  PRM-RL,  combining  RL  with  roadmap
sampling  to  select  feasible  paths.  Liu  et al.  [17]
developed multi-agent path planning with evolu-
tionary
 reinforcement
 learning 
(MAPPER),
which  integrates  evolutionary  RL  with  global
planning  in  multi-agent environments,   improv-
ing  decision  robustness.  Argiliana  et  al.  [18]
reviewed adaptive multi-UAV strategies, confirm-
ing the benefits of frameworks that combine clas-
sical generation with learning-based selection.
Meanwhile, geometric  modeling  and   seman-
tic perception have been used to enhance safety
assessment. Cujó Blasco et al. [19] proposed real-
time  3D  reconstruction  using  UAVs,  improving
situational awareness. Chen et al. [20] developed
a  multi-view  3D  detection  network,  refining
obstacle  representation.  Wang  et al.  [21]  intro-
duced Omni-Explorer, which expands the field of
view to support rapid exploration. Jonnalagadda
et al.  [22]  presented  an  efficient  path  planning
strategy  for  multi-UAV  payload  environments.
These studies highlight the potential of integrat-
ing geometric approximation and perception with
trajectory  planning,  though  achieving  a  unified
balance of safety and efficiency remains an open
problem [23, 24].
The  main  contribution  of  this  study  is  the
development of the safety-aware global-local rein-
forcement  learning  (SGL-RL)  algorithm,  a  3D
path  planning  framework  that  integrates  global
guidance,  local  trajectory  generation,  safety
assessment,  and  RL-based  decision  making.  As
discussed above,  in  dynamic  obstacle   environ-
Wenjie Zhang et al.  /  DDQN-Based 3D Path Planning Algorithm for UAVs in Dynamic Dense Obstacle Environments
—  85  —

## Page 3

ments,  traditional  3D  path  planning  algorithms
face significant challenges in accurately modeling
obstacle  motion  and  achieving  real-time  avoid-
ance, often resulting in high computational com-
plexity  and  insufficient  path  safety.  To  address
these limitations, this study introduces a unified
solution, whose  specific  innovations  are   summa-
rized as follows.
1)  To  adapt  to  3D  environments  and
address  the  high  computational  cost  and  high
false alarm rate of traditional point-by-point col-
lision detection,  we  proposed  a  3D  DWA   algo-
rithm with an integrated safety assessment mod-
ule. This algorithm improves computational effi-
ciency  and  enhances  the  reliability  of  obstacle
detection,  thereby  improving  overall  planning
efficiency.
2)  We  introduced  a  predictive  axis-aligned
bounding  box  (AABB)  expansion  strategy  to
model the future occupancy of dynamic obstacles.
This method  effectively  alleviates  the   underesti-
mation of collision risks in time-varying environ-
ments and enhances the foresight and reliability
of safety assessment.
3)  To  overcome  the  lack  of  interpretability
and robustness in existing RL-based planning, we
designed  a  three-stage  decision  mechanism  that
includes  trajectory  scoring,  state  encoding,  and
deep  deterministic  policy  gradient  (DDQN)-
based selection.  This  mechanism  improves   deci-
sion quality  and  interpretability,  while  the   uni-
fied trajectory feature vector enhances generaliza-
tion  and  robustness,  reducing  reliance  on  large-
scale training datasets.
The remainder of this paper is organized as
follows.  Section  2 details  the  proposed  system
architecture and implementation of each module;
Section  3 presents  simulation-based  performance
evaluations  and  comparative  experiments  to
demonstrate  the  method’s  superiority  in  path
safety,  computational  efficiency,  and  trajectory
optimality; and  Section  4 summarizes  the   find-
ings  and  discusses  future  research  directions.
Through theoretical and experimental demonstra-
tion,  the  proposed  SGL-RL framework   demon-
strates  reliable  obstacle  avoidance  and  decision-
making  capabilities  in  complex  environments,
showing strong application potential.
 2    Problem Formulation  and  Plan-
ning Methods
 2.1    Problem Formulation
UAVs operating in real-world environments often
face dense and heterogeneous 3D obstacles at dif-
ferent altitudes. For example, in urban or indus-
trial areas,  ground  vehicles  and  pedestrians   cre-
ate moving barriers at lower levels, buildings and
infrastructures form structural constraints at mid-
levels, while  suspended  cables  or  aerial   equip-
ment  introduces  additional  uncertainties  at
higher levels. UAVs must rely on onboard sens-
ing systems to detect these obstacles in real time,
but ensuring strict safety while maintaining effi-
cient trajectory execution remains a major chal-
lenge. Existing methods face clear limitations in
such  scenarios:  global  planners  like  A*  impose
high computational  costs  under  frequent   replan-
ning, local methods such as DWA are inherently
shortsighted  and  prone  to  local  optima,  and
pointwise collision checking is inefficient in dense
obstacle  fields.  While  RL  provides  adaptability,
end-to-end policies still suffer from low efficiency,
unstable convergence,  and  limited   interpretabil-
ity, so their safety cannot be fully guaranteed in
practical operations.
To  overcome  these  challenges,  this  chapter
proposes  a  unified  3D  path  planning  framework
that  combines  global  guidance,  local  trajectory
sampling,  predictive  geometric  modeling,  and
DDQN-based  selection.  The  system  integrates
path  initialization,  trajectory  generation,  safety
evaluation,  and  learning-based  decision-making,
achieving  safe  and  efficient  UAV  navigation  in
complex dynamic environments.
 2.2    UAV Kinematic Model
To support  path  planning  in  complex   environ-
ments, a kinematic quadrotor model is employed.
Journal of Beijing Institute of Technology，2026，Vol. 35，No. 1
—  86  —

## Page 4

The  planner  generates  velocity  inputs  in  the
world  frame,  which  are  transformed  into  the
body-fixed  frame  according  to  the  UAV’s  atti-
tude  for  control  execution.  The  world  frame  is
defined  as  a  fixed  right-handed coordinate   sys-
tem,  while  the  body-fixed  frame  is  also  right-
handed.  The  origin  is  located  at  the  center  of
mass  of  the  UAV,  and  the  x-axis  points  in  the
forward direction, as shown in Fig. 1.
 
 
z
y
x
Yaw
Pitch
Z
Roll
Y
X
Fig. 1    The UAV body-fixed coordinate frame
 
The velocity command in the world frame is
v
w =
[
vw
x
vw
y
vw
z
]T
（1）
vw
x
vw
y
vw
z
where 
, 
, 
 are the desired global velocities.
To  obtain  executable  inputs,  this  command
is  transformed  into  the  body-fixed frame  as   fol-
lows
v
b = Rwbv
w
（2）
Rwb
(ϕ, θ, ψ)
Rwb
where 
  is  the  rotation  matrix  from  world  to
body-fixed  frame,  derived  from  ZYX-ordered
Euler angles 
 representing roll, pitch, and
yaw.  This  mapping  ensures  that  global  velocity
commands  are  converted  into  actionable  body-
frame  controls  for  trajectory  following.  The
explicit form of 
 is as follows
Rwb =


C (θ) C (ψ)
−C (θ) S (ψ)
−S (θ)
S(ϕ)S(θ)C(ψ) −C(ϕ)S(ψ)
−[S(ϕ)S(θ)S(ψ) + C(ϕ)C(ψ)]
S(ϕ)C(θ)
C(ϕ)S(θ)C(ψ) + S(ϕ)S(ψ)
−[C(ϕ)S(θ)S(ψ) −S(ϕ)C(ψ)]
C(ϕ)C(θ)


（3）
C(·)
S(·)
where 
  denotes  the  cosine  function, 
denotes the sine function.
 2.3    A* Algorithm
The  A*  algorithm  is  a  classical  heuristic-based
search  method  that  has  been  widely  applied  in
robotics  and  UAV  navigation  for  global  path
planning.  It  determines  the  optimal  path  from
the start to the goal by minimizing the total cost
function as follows
f (n) = g (n) + h (n)
（4）
g (n)
h (n)
n
where 
  represents  the  actual  cost  from  the
start  node  to  the  current  node, 
  is  the
heuristic  estimate  of  the  cost  from  the  current
node to the goal, and   represents a node in the
search graph.
f (n)
By  expanding  nodes  with  the  lowest 
,
A*  guarantees  cost-consistent  and  near-optimal
solutions in static or structured environments.
 2.4    DWA Algorithm
(v, ω)
The DWA is a local trajectory planning method
that  generates  feasible  control  commands  by
sampling  velocities  within  the  UAV’s  dynamic
limits. At each control cycle, candidate velocities
 are selected from a dynamic window, which
is defined  by  the  velocity  and  acceleration   con-
straints of the vehicle as follows
Vd = {(v, ω) | vmin ⩽v ⩽vmax, ωmin ⩽ω ⩽ωmax} （5）
v ∈[vcurr −˙vmax∆t, vcurr + ˙vmax∆t]
（6）
ω ∈[ωcurr −˙ωmax∆t, ωcurr + ˙ωmax∆t]
（7）
v
ω
ωmin
ωmax
˙vmax
˙ωmax
∆t
where 
  and 
  denote  the  linear  and  angular
velocities, 
  denotes  lower  bounds  of  angular
velocity, 
  denotes  upper  bounds  of  angular
velocity, vcurr denotes current linear velocity, ωcurr
denotes current angular velocity, 
 and 
 are
the  maximum  accelerations,  and 
  is the   con-
trol cycle.
For  each  sampled  velocity  command,  the
motion of the UAV is predicted by integrating its
kinematic model over a short time horizon as fol-
lows





xt+1 = xt + v cos(θt)Δt
yt+1 = yt + v sin(θt)Δt
θt+1 = θt + ωΔt
（8）
(xt, yt, θt)
where 
  represents  the  UAV’s  position
Wenjie Zhang et al.  /  DDQN-Based 3D Path Planning Algorithm for UAVs in Dynamic Dense Obstacle Environments
—  87  —

## Page 5

t
and heading at time step  .
Each  predicted  trajectory  is  then  scored
according  to  predefined  criteria,  such  as  goal
heading,  clearance  from  obstacles,  and  velocity
magnitude.  The  velocity  command  associated
with the  trajectory  of  the  highest  score  is   exe-
cuted, and the process repeats in the next cycle.
 3    Algorithm Framework Design
The  SGL-RL  algorithm  proposed  in  this  paper
follows a hierarchical RL framework that decom-
poses  the  planning  process  into  multiple  layers.
At the global layer, the planner provides a refer-
ence path to guide long-term navigation. At the
local layer, an improved 3D DWA is used to gen-
erate  dynamically  feasible  candidate  trajectories
under  motion  constraints.  These  trajectories  are
further evaluated through predictive safety mod-
eling, including AABB expansion and convex hull
verification. At the decision-making layer, struc-
tured feature encoding is applied, and a reinforce-
ment learning module selects the optimal trajec-
tory  for  execution.  The  UAV  then  follows  the
chosen trajectory while continuously updating its
state. The  overall  system  architecture  is   illus-
trated in Fig. 2.
 3.1    Global Path Planning
In the proposed framework, the A* algorithm is
employed to generate a sparse global path from
the start point to the goal on a discretized grid
map.  This  path  serves  as  a  long-term  reference
for  navigation  rather  than  a  directly  executable
trajectory.  To  enhance  adaptability  in  dynamic
environments,  the  system  adopts  a  local  target
guidance  mechanism.  Instead  of  steering  the
UAV directly toward the final goal, a waypoint is
selected from the global path according to a pre-
defined look-ahead distance.
qcur
{q1, q2, · · · , qN}
qref
Let the current UAV position be 
, and the
global  path  be  denoted  as 
.  The
reference  point 
  is  chosen  such  that  the
Euclidean distance satisfies
∥qref −qcur ∥≈dplan
（9）
dplan
where 
 is the look-ahead distance. This strat-
egy ensures that local trajectory planning is con-
sistently  guided  along  the  global  path,  while
maintaining  sufficient  flexibility  to  adapt  to
dynamic obstacles.
 
Global guidance
DDQN
Observation
Local planning
Obstacle
AABB expansion
A* algorithm
End Local
guide
Start
Convex hull
separation
Expanded
obstacle
Bexp = U B(t)
t∈[0, T]
Separating plane
3D-DWA
Dvi ∈[−amaxDt, amaxDt]
Trajectories
Convex hull
Critic
Actor
Policy
gradient
Gradient
Update
param-
eter
Online
network
(si, ai)
(si+1, ai+1)
Soft
update
Target
network
Gradient
Update
param-
eter
Online
network
Soft
update
Target
network
N*(st, at, rt, si+1)
Sample
mini-batch
Experience
replay buffer
Optimal
trajectories
Action
coding
Candidate
trajectories
, di, ci,
Trajectory
ki, li, ai]
Trajectory
index: i
fi = [vi
Fig. 2    System architecture diagram
Journal of Beijing Institute of Technology，2026，Vol. 35，No. 1
—  88  —

## Page 6

3.2    Local Trajectory Planning
(vx, vy, vz)
Unlike the conventional DWA that samples both
linear  and  angular  velocities  in  two-dimensional
(2D), the proposed framework extends the sam-
pling  process  to  the  3D  linear  velocity  space
, without explicit angular velocity con-
trol. The admissible velocity set is constrained by
physical limits as follows
vi ∈[vmin, vmax]
（10）
∆vi ∈[−amax∆t, amax∆t]
（11）
i ∈{x, y, z}
（12）
vmax
vmin
amax
where 
  and 
  represent  the  maximum  and
minimum speeds of the UAV, and 
 represents
the maximum acceleration of the UAV.
Thus, the feasible velocity set is as follows
Vd = {(vx, vy, vz)|vi, ∆vi satisfy constraints} （13）
v ∈Vd
For each sampled velocity 
, the UAV’s
motion  is  predicted  over  a  short  horizon  using
the discrete kinematic model as follows
qt+1 = qt + v∆t
（14）
qt = [xt, yt, zt]
T
（15）
qt
where 
 is the t-th trajectory point in the pre-
dicted trajectory and the trajectory is expressed
as follows
T = {qt, qt+1, · · · , qt+T}
（16）
Each  predicted  trajectory  is  evaluated  by  a
weighted function as follows
J(T) = αJh + βJc + γJv
（17）
α
β
γ
Jh
Jc
Jv
where 
, 
,   are the weighting coefficients, 
denotes heading consistency with the local refer-
ence point, 
 is the minimum clearance to obsta-
cles, and 
 represents the average velocity.
All trajectories generated by the local plan-
ner  must  undergo  safety  evaluation  to  ensure
safety.  However,  traditional  methods  often  lack
efficient  safety  detection  modules,  which  limits
their performance  in  dense  dynamic   environ-
ments.
 3.3    Trajectory  Safety  Evaluation  and  Collision
Detection
To  enhance  safety  in  dense  dynamic  scenarios,
this  study  introduces  a  two-stage  evaluation
framework  that  combines  predictive  AABB
expansion with convex hull-based collision detec-
tion, achieving a balanced approach between effi-
ciency and safety.
 3.3.1    Time-Predicted AABB Expansion
Ttotal
Obstacles  are  modeled  by  AABB.  Unlike  static
definitions  at  a  single  time  step,  the  bounding
volume  is  expanded  along  the  obstacle’s  pre-
dicted trajectory during the planning horizon 
as follows
B(t) =[xmin(t), xmax(t)]×
[ymin(t), ymax(t)] × [zmin(t), zmax(t)]
（18）
Bexp =
∪
t∈[0,Ttotal]B(t)
（19）
Bexp
Ttotal
where 
  denotes  the  minimum  bounding  box
covering  all  possible  obstacle  positions  within
, xmin(t) denotes minimum x-coordinate of the
object at time t, xmax(t) denotes maximum x-coor-
dinate  of  the  object  at  time  t,  ymin(t)  denotes
minimum  y-coordinate  of  the  object  at  time  t,
ymax(t)  denotes  maximum  y-coordinate  of  the
object at time t, zmin(t) denotes minimum z-coor-
dinate  of  the  object  at  time  t,  zmax(t)  denotes
maximum  z-coordinate  of  the  object  at  time  t.
This  prevents  underestimation  of  collision  risk
caused by obstacle movement.
 3.3.2    Convex Hull-Based Collision Checking
{p0, p1, p2, p3}
Candidate  UAV  trajectories  are  represented  by
the  third-order  piecewise  Bézier  curves,  fitted
from  consecutive  control  points 
.
Each segment is defined as
C(u) =
3
∑
i=0
( 3
i
)
(1 −u)
3−iu
ipi
（20）
u ∈[0, 1]
（21）
u
where   is the curve parameter, which is used to
control the position of the curve among the con-
trol points.
The  convex  hull  formed  by  these  control
Wenjie Zhang et al.  /  DDQN-Based 3D Path Planning Algorithm for UAVs in Dynamic Dense Obstacle Environments
—  89  —

## Page 7

m
points strictly encloses the entire curve, thus pro-
viding a conservative yet efficient spatial approx-
imation.  For  a  complete  trajectory  consisting  of
  segments, multiple  convex  hulls  are   con-
structed as follows
Hτ =
m∪
k=1Conv{pk,0, pk,1, pk,2, pk,3}
（22）
where  pk,0,  pk,1,  pk,2,  and  pk,3  are  the  four  control
points  of  the  k-th  cubic  Bézier  curve  segment.
Collision  detection  is  then  performed  by  testing
whether
Hτ ∩Bexp = ∅
（23）
If  the  convex  hull  of  a  trajectory  intersects
with any  expanded  obstacle  volume,  the   trajec-
tory is discarded. Otherwise, it is retained as fea-
sible.
Compared  to  pointwise  collision  checking,
the  convex  hull  method  significantly  reduces
computational  load  and  avoids  false  negatives
caused by sparse sampling, making it well-suited
for dense 3D environments.
 3.4    DDQN-Based Trajectory Selection
{Ti}N
i=1
After the AABB expansion and convex hull sepa-
ration procedure, a set of feasible candidate tra-
jectories 
  is  obtained.  To  formulate  the
decision-making problem,  the  trajectory   selec-
tion process is modeled as a Markov decision pro-
cess (MDP) as follows
M = {S, A, P, r, γ}
（24）
S
A
P
r
γ
where 
 denotes the state space, 
 denotes the
action  space, 
  denotes the  transition   probabil-
ity,   denotes the reward function, and   denotes
the discount factor.
Ti
During  each  planning  cycle,  the  3D  DWA
module generates  dynamically  feasible   trajecto-
ries,  from  which  the  top  five  are  retained  after
safety  evaluation.  Instead  of  directly  modeling
raw  trajectory  points,  each  candidate  trajectory
 is encoded into a six-dimensional feature vec-
tor as follows
fi = [vi, di, ci, κi, li, αi]
（25）
vi
di
ci
κi
li
αi
where 
  is  the  average  velocity, 
  is  the
Euclidean  distance  to  the  goal, 
  is the   mini-
mum obstacle clearance, 
 is the maximum cur-
vature,   is the total path length, and 
 is the
directional alignment with the goal. By concate-
nating  the  features  of  all  five  candidates,  the
state vector is constructed as follows
s = [f1, f2, · · · , f5] ∈R
30
（26）
f1, f2, · · · , f5
where 
 denote the feature vectors of
candidate  trajectories.  This  structured  encoding
abstracts high-level geometric and dynamic prop-
erties,  which  improves  generalization  across
unseen  environments  and  enhances  robustness
against  sensing  uncertainties.  The  action  is
defined as the selection of one trajectory among
the retained candidates as follows
a ∈A = {1, 2, · · · , 5}
（27）
This  formulation  transforms  the  original
high-dimensional continuous control problem into
a  discrete  decision-making  problem  with  lower
complexity and improved interpretability.
The  reward  function  integrates  multiple
terms to balance efficiency, safety, and task com-
pletion as follows
rt =λ1rtime + λ2rdis + λ3rcoll+
λ4rsucc + λ5rto
（28）
λi
rtime
rdis
where 
  represents  the  weight  coefficient  for
each  reward  term. 
  is  a  fixed  time  penalty
designed to encourage the UAV to reach the tar-
get  point  as  quickly  as  possible. 
  is the   dis-
tance-based reward, calculated as follows
rdis = ||pt −g||
D
（29）
||pt −g||
D
where 
  denotes  the  Euclidean  distance
between the UAV’s current position and the final
goal, and 
 is a normalization factor.
rcoll
rsucc
rto
, 
,  and 
  represent  the  collision
penalty,  goal-reaching  reward,  and  timeout
penalty, respectively. They are defined as follows
rcoll =
{
1,
if a collision is detected
0,
otherwise
（30）
Journal of Beijing Institute of Technology，2026，Vol. 35，No. 1
—  90  —

## Page 8

rsucc =
{
1,
if dt < ε
0,
otherwise
（31）
rto =
{
1,
if telap ⩾Tmax
0,
otherwise
（32）
dt
telap
Tmax
where 
 denotes the Euclidean distance between
the UAV and the final target, ε denotes success
distance  tolerance, 
  is  the  current  execution
time, and 
 is the maximum allowable time.
Qθ
Qθ−
To  further  improve  stability,  DDQN  is
employed to mitigate the overestimation bias of
conventional Q-learning. The online network 
is  used  for  action  selection,  whereas  the  target
network 
  evaluates  the  action.  The  target
value for updates is defined as
yt = rt + γQθ−(st+1, arg maxa′Qθ(st+1, a
′)) （33）
θ
θ−
where   and 
 are the parameters of the online
and  target  networks,  respectively,  arg maxa′
denotes the argument that maximizes the objec-
tive function, a′ denotes a candidate action. This
decoupling reduces optimistic bias, enhances con-
vergence  stability,  and  enables  reliable  training
under sparse and delayed rewards.
 4    Simulation Results
 4.1    Simulation Environment
We evaluated  the  proposed  approach  in  a   cus-
tom  3D  simulation  environment  that  integrates
dynamic obstacle  modeling,  a  global  path   plan-
ning  module,  a  3D  DWA-based  local  trajectory
sampler, and a DDQN-based trajectory selection
module,  with  support  for  multi-scenario  tasks
and  quantitative  performance  evaluation.  All
experiments  were  conducted  on  a  workstation
equipped with an Intel Core i7-14700HX central
processing unit (CPU) and an NVIDIA ray trac-
ing Texel eXtreme (RTX) 4 070 graphic process-
ing unit (GPU) with 16 GB memory. The soft-
ware  environment  was  configured  with  Python
3.9.20 and  PyTorch  2.6.0.  In  this  environment,
the results of the algorithm are shown in Fig. 3,
where the flight trajectory of the drone shows a
color gradient over time.
 
tmin
tmax
Fig. 3    Global  flight  trajectory  visualization  of  UAV  in  3D
dynamic environment
 
The  workspace  spans  80 m  ×  8 m  ×  8 m,
with  fifty  obstacles  per  run  drawn  from  two
motion  classes.  The  trajectory  of  the  complex
dynamic obstacle follows the cloverleaf knot tra-
jectory, and its motion formula is as follows





x(t) = λ1[sin(t) + 2 sin(2t)] + x0
y(t) = λ1[cos(t) −2 cos(2t)] + y0
z(t) = −λ1 sin(3t) + z0
（34）
x0
y0
z0
t
x(t)
y(t)
z(t)
λ1
where 
, 
  and 
  are  the  positions  of  the
obstacle  when  it  is  initialized,    is  the  current
time, 
, 
 and 
 are the positions of the
obstacle at the current time, and 
 is the ampli-
tude control coefficient.
The  periodic  dynamic  obstacle  oscillates
along the z-axis with a fixed period. The motion
formula is as follows
z(t) = −λ2 sin (t) + z0
（35）
z0
t
z(t)
λ2
where 
 is the position of the obstacle when it is
initialized,   is the current time, 
 is the posi-
tion of the obstacle at the current time, and 
 is
the amplitude control coefficient.
The  UAV  starts  at  [0,  0,  0],  and  goals  are
placed  at  x =  75 m  with  y  and  z  sampled  uni-
formly from a predefined feasible band.
 4.2    Training Settings
The  algorithm  is  trained  in  the  environment
described in  the  previous  section,  and  the   con-
trol  process  is  executed  in  discrete  time  steps.
Safety  assessment  uses  time-predicted  AABB
expansion and convex hull separation to conser-
vatively  filter  trajectories.  Full  environment
parameters and all RL hyperparameters are sum-
marized in Tab. 1 and Tab. 2.
To  evaluate  the  proposed  SGL-RL  algo-
Wenjie Zhang et al.  /  DDQN-Based 3D Path Planning Algorithm for UAVs in Dynamic Dense Obstacle Environments
—  91  —

## Page 9

rithm,  we  conducted  comparative  experiments
under various typical configurations. Tab. 3 sum-
marizes  the  technical  characteristics  of  each
method,  including  global  and  local  planning
strategies,  obstacle  modeling,  collision  detection,
and learning mechanisms.
 4.3    Experimental Results and Analysis
 4.3.1    Comparison of  Collision  Detection   Effi-
ciency
To validate the trajectory safety evaluation pro-
posed  in  this  paper,  we  benchmarked  it  against
the  conventional  pointwise  collision  test.  Fig. 4
presents a comparison with the traditional point-
by-point detection  method  with  varying   num-
bers of trajectory points. The experiment records
the average computational time required by each
method when processing different numbers of tra-
jectory points.
As shown in Fig 4, the computational time
of  traditional  point-by-point  detection  methods
increases almost linearly with the number of tra-
jectory  sampling  points,  and  the  computational
burden increases significantly under dense trajec-
tory  conditions.  For  example,  when  the  number
of sampling points reaches 50, the average detec-
tion time rises to approximate 0.015 s, and when
the  number  of  sampling  points  reaches  100,  the
average  detection  time  further  increases  to
0.028 s. In contrast, the method based on Bézier
fitting  and  convex  hull  construction  reduces
detection time  by  an  average  of  35%,   demon-
strating its practicality and scalability for large-
scale trajectory evaluation.
 4.3.2    Performance Comparison Experiments
We  conducted  200 Monte  Carlo  experiments
using the algorithms listed in Tab. 3 within the
simulation environment  described  in  the   previ-
ous  section.  In  each  experiment,  the  start  and
goal positions of the unmanned aerial vehicle, as
well as the spatial distribution of dynamic obsta-
cles,  were  randomly  varied  to  ensure  diversity
 
Tab. 1  Environment parameters
 
Parameter
Value
Map size
80 m×8 m×8 m
Grid resolution
0.5 m
Start coordinates
[0 m, 0 m, 0 m]
Goal coordinates
X = 75 m
Total number of obstacles
80
Proportion of complex dynamic obstacles
35%
Proportion of periodic dynamic obstacles
65%
Obstacle size
Complex dynamic
obstacles: 0.8 m;
periodic dynamic
obstacles: 1.6 m
Prediction horizon
1 s
Maximum UAV speed
1.5 m/s
Maximum UAV acceleration
3.0 m/s²
Control time step
0.1 s
UAV radius
0.2 m
Number of DWA trajectories
125
Number of RL candidate trajectories
5
Maximum simulation duration
60 s
 
Tab. 2  Hyperparameters for RL
 
Parameter
Value
Training episodes
10 000
Max steps
600
Replay buffer capacity
10 000
Batch size
64
Learning rate
0.001
Discount factor γ
0.99
Target update rate τ
0.01
Decay per episode ε
0.99
 
Tab. 3  Comparison of technical features of path planning algorithms
 
Algorithm
Global planning
Local planning
Obstacle modeling
Collision detection
Learning strategy
A* [4]
A* search
None
No modeling
None
No learning
DWA [6]
None
3D DWA
No modeling
Pointwise checking
No learning
A*D
A* search
3D DWA
No modeling
Pointwise checking
No learning
SA*D
A* search
3D DWA
Predictive AABB
Convex hull check
No learning
PPO [11]
None
End-to-end
Implicit policy
Implicit policy
End-to-end RL
SGL-RL
A* search
3D DWA
Predictive AABB
Convex hull check
DDQN selection
Note: A*D: Use A* algorithm globally and 3D DWA algorithm locally for planning. SA*D: Add predicted AABB and convex hull safety
detection based on A*D.
Journal of Beijing Institute of Technology，2026，Vol. 35，No. 1
—  92  —

## Page 10

and  robustness  in  evaluation.  The  aggregated
experimental results are summarized in Tab. 4.
 
 
Tab. 4  Comparison of average completion time and collision fre-
quency of different methods
 
Algorithm
Average
arrival
time (s)
Average
collisions
Average
path
length (m)
Average
arrival
rate (%)
A*
49.7
23.4
87.9
100
DWA
72.4
5.1
119.1
81
A*D
62.3
3.9
98.8
90
SA*D
60.1
0.3
96.3
88
PPO
68.2
4.7
108.6
85
SGL-RL
51.2
0.2
88.2
97
 
The results in Tab. 4 show that although the
A*  algorithm  achieved  the  shortest  arrival  time
of  49.7 s,  it  only  produced  a  static  global  path
without  dynamic  obstacle  modeling  or  safety
assessment. As  a  result,  the  UAV  collided   fre-
quently,  averaging  23.4 collisions,  which  makes
this approach  unsuitable  for  dynamic   environ-
ments. The DWA algorithm reduced collisions to
5.1  times by  considering  UAV  kinematics  and
velocity  limits,  but  without  global  guidance  or
predictive safety checks it often became trapped
in  local  minima,  extending  the  arrival  time  to
72.4 s.
With  global  guidance,  the  A*D  algorithm
reduced  detours  and  shortened  arrival  time  to
62.3 s. However, because it still relied on point-
wise  collision  checking,  it  incurred  3.9 collisions
on average,  indicating  that  discrete  checks   can-
not  fully  capture  risks  in  dense  environments.
The SA*D  algorithm  improved  safety  by   intro-
ducing  predictive  AABB  expansion  and  convex
hull  evaluation,  which  anticipated  obstacle
motion and  validated  entire  trajectories,   reduc-
ing collisions  to  0.3 while  maintaining  a   moder-
ate  arrival  time  of  60.1 s.  The  PPO  algorithm
achieved an arrival time of 68.2 s with 4.7 colli-
sions.  Its  end-to-end structure  provided   adapt-
ability  but  was  sensitive  to  reward  design  and
randomness, leading to unstable trajectories and
a reduced success rate of 85%.
In  contrast,  the  proposed  SGL-RL  algo-
rithm achieved 51.2 s arrival time, only 0.2 colli-
sions, and  a  97%  success  rate.  These   improve-
ments stem  from  the  integration  of   complemen-
tary  mechanisms:  global  A*  guidance  reduces
detours,  3D  DWA  sampling  ensures  feasibility,
predictive  AABB  expansion  provides  foresight,
convex hull evaluation strengthens safety checks,
and  DDQN-based  selection  enhances  robustness
and  interpretability.  This  design  explains  why
SGL-RL  outperforms  DWA  by  reducing  arrival
time by about 15% while nearly eliminating colli-
sions, and why it improves over PPO with 25%
faster  arrival  time  and  12%  higher  success  rate,
benefiting  from  predictive  safety  modeling  and
stable RL-based decision-making.
 4.3.3    Visualization Analysis
To  verify  the  algorithm’s  ability  to  detect  and
navigate  dynamic  gaps,  Fig. 5  shows  the  time
evolution of trajectories in a typical scenario. We
ran 100 steps  in  this  scenario.  Different   sub-
graphs  correspond  to  the  predicted  states  of
obstacles at  successive  moments  and  the   evolu-
tion of the UAV’s trajectory. We can see that as
obstacles move, new gaps gradually appear in the
local  environment.  The  UAV  is  able  to  exploit
these dynamic  changes  to  adjust  its  path,   suc-
cessfully  avoiding  surrounding  obstacles  and
selecting a  suitable  gap  to  traverse.  This   phe-
nomenon demonstrates that the algorithm’s pre-
diction-based AABB  expansion  modeling   effec-
tively  captures  the  space  that  obstacles  may
 
20
40
60
80
100
0
0.005
0.010
0.015
0.020
0.025
0.030
Number of sampled trajectory points
Method 2: Bézier + convex hull
Average detection time (s)
Method l: Point-wise check
Fig. 4    Comparison of collision detection time
Wenjie Zhang et al.  /  DDQN-Based 3D Path Planning Algorithm for UAVs in Dynamic Dense Obstacle Environments
—  93  —

## Page 11

occupy in the future, while the DDQN decision-
making mechanism selects the optimal path from
candidate trajectories,  demonstrating  the   algo-
rithm’s security  and  efficiency  in  dynamic   envi-
ronments.
 5    Conclusion
The  SGL-RL  algorithm  is  a  hierarchical  RL
framework  for  3D  path  planning  that  integrates
global guidance, local trajectory generation, pre-
dictive  safety  modeling,  and  neural-network-
based  decision-making. By  employing  a   predic-
tive AABB strategy to capture the future occu-
pancy  of  dynamic  obstacles  and  incorporating
convex  hull  verification  for  trajectory  safety
assessment, the framework ensures reliable obsta-
cle avoidance in dense environments. At the deci-
sion-making  layer,  structured  feature  encoding
combined
 with
 DDQN
 trajectory
 selection
enhances interpretability, robustness, and gener-
alization.  Comparative  experiments  demonstrate
that  SGL-RL  reduces  collision  rates  by  about
15%, achieves safer and more reliable trajectories,
and  shortens  flight  time  by  approximate  15%,
thereby significantly  improving  navigation   effi-
ciency in complex dynamic scenarios.
References： 
 D.  Debnath,  F.  Vanegas,  J.  Sandino,  A.  F.
Hawary, and F. Gonzalez,“A review of UAV path-
planning algorithms and obstacle avoidance meth-
ods for remote sensing applications,” Remote Sensing,
vol. 16, no. 21, pp. 4019, 2024.
[1]
 S. Karaman and E. Frazzoli,“Sampling-based algo-
rithms for optimal motion planning,” The Interna-
tional Journal of Robotics Research, vol. 30, no. 7,
pp. 846-894, 2011.
[2]
 L. E. Kavraki, P. Svestka, J. C. Latombe, and M.
H. Overmars, “Probabilistic roadmaps for path
planning in high-dimensional configuration spaces, ”
IEEE Transactions on Robotics and Automation,
vol. 12, no. 4, pp. 566-580, 2002.
[3]
 P. E. Hart, N. J. Nilsson, and B. Raphael,“A for-
mal basis for the heuristic determination of mini-
mum cost paths,” IEEE Transactions on Systems
Science and Cybernetics, vol. 4, no. 2, pp. 100-107,
1968.
[4]
 M.  Likhachev,  G.  J.  Gordon,  and  S.  Thrun,
“ARA*: Anytime A* with provable bounds on sub-
optimality, ” in Advances in Neural Information
Processing Systems, Vancouver and Whistler, BC,
Canada, pp. 767-774, 2003.
[5]
 
(d)
(b)
(e)
(c)
(f)
0
20
20
40
40
60
(a)
60
80
80
100
0
100
Steps
Steps
Steps
Steps
Steps
Steps
Fig. 5    Dynamic gap detection and trajectory evolution process (Gradient colors show positions at successive time steps.): (a) trajec-
tory of steps 0–20; (b) trajectory of steps 20–40; (c) trajectory of steps 40–60; (d) trajectory of steps 60–80; (e) trajectory of
steps 80–100; (f) trajectory of steps 0–100
Journal of Beijing Institute of Technology，2026，Vol. 35，No. 1
—  94  —

## Page 12

D. Fox, W. Burgard, and S. Thrun,“The dynamic
window approach to collision avoidance,” IEEE
Robotics & Automation Magazine, vol. 4, no. 1, pp. 23-
33, 2002.
[6]
 S. J. Qin and T. A. Badgwell,“A survey of indus-
trial model predictive control technology,” Control
Engineering Practice, vol. 11, no. 7, pp. 733-764,
2003.
[7]
 O. Ljungqvist, “Motion planning and feedback con-
trol techniques with applications to long tractor-
trailer vehicles,” Ph.D. dissertation, Linkopings
Universitet, 2020.
[8]
 A. Loquercio, E. Kaufmann, R. Ranftl, M. Müller,
V. Koltun, and D. Scaramuzza,“Learning high-
speed flight in the wild,” Science Robotics, vol. 6,
no. 59, pp. eabg5810, 2021.
[9]
 W. Zhong, X. Liu, H. Jin, Q. Zhu, Z. Lin, K. Mao,
and J. Wang, “Three-dimensional trajectory opti-
mization of rotary-wing UAV with cellular net-
work connectivity based on modified DDPG, ”
Physical Communication, vol. 72, 2025. https://www.
sciencedirect.com/science/article/abs/pii/S1874490
725001764.
[10]
 K. Chikhaoui, H. Ghazzai, and Y. Massoud, “PPO-
based reinforcement learning for UAV navigation
in urban environments, ” in 2022 IEEE 65th Inter-
national Midwest Symposium on Circuits and Sys-
tems (MWSCAS), Fukuoka, Japan, pp. 1-4, 2022.
[11]
 L. Tai, G. Paolo, and M. Liu, “Virtual-to-real deep
reinforcement  learning:  Continuous  control  of
mobile robots for mapless navigation, ” in 2017
IEEE/RSJ International Conference on Intelligent
Robots  and  Systems  (IROS),  Vancouver,  BC,
Canada, pp. 31-36, 2017.
[12]
 M. Pfeiffer, S. Shukla, M. Turchetta, C. Cadena,
A. Krause, R. Siegwart, and J. Nieto,“Reinforced
imitation:  Sample  efficient  deep  reinforcement
learning for mapless navigation by leveraging prior
demonstrations,” IEEE Robotics and Automation
Letters, vol. 3, no. 4, pp. 4423-4430, 2018.
[13]
 T. Hester, M. Vecerik, O. Pietquin, M. Lanctot, T.
Schaul,  B.  Piot,  D.  Horgan,  J.  Quan,  A.
Sendonaris, I. Osband, G. Dulac-Arnold, J. Aga-
piou, J. Z. Leibo, and A. Gruslys, “Deep Q-learn-
ing from demonstrations,” in Proceedings of the
AAAI Conference on Artificial Intelligence, New
Orleans, Louisiana, USA, pp. 3223-3230, 2018.
[14]
 G. Chou, “Safe end-to-end learning-based robot
autonomy via integrated perception, planning, and
control, ” Ph. D. dissertation, University of Michi-
gan, 2022.
[15]
 A. Faust, K. Oslund, O. Ramirez, A. Francis, L.
[16]
Tapia, M. Fiser, and J. Davidson, “PRM-RL: Long-
range robotic navigation tasks by combining rein-
forcement learning and sampling-based planning, ”
in 2018 IEEE International Conference on Robotics
and Automation, Brisbane, Australia, pp. 5113-
5120, 2018.
 Z. Liu, B. Chen, H. Zhou, G. Koushik, M. Hebert,
and D. Zhao, “Mapper: Multi-agent path planning
with evolutionary reinforcement learning in mixed
dynamic environments, ” in 2020 IEEE/RSJ Inter-
national Conference on Intelligent Robots and Sys-
tems (IROS), Las Vegas, NV, USA, pp. 11748-
11754, 2020.
[17]
 S. Argiliana, E. Ekawati, and F. Mukhlish,“Adap-
tive strategies for dynamic obstacle avoidance and
formation control in multi-agent drone systems: A
review,” Journal of Robotics and Control (JRC),
vol. 6, no. 4, pp. 1710-1720, 2025.
[18]
 J.  Cujó  Blasco,  S.  Bemposta  Rosende,  and  J.
Sánchez-Soriano,“Automatic real-time creation of
three-dimensional (3D) representations of objects,
buildings, or scenarios using drones and artificial
intelligence techniques,” Drones, vol. 7, no. 8, pp. 516,
2023.
[19]
 X. Chen, H. Ma, J. Wan, B. Li, and T. Xia, “Multi-
view 3D object detection network for autonomous
driving, ” in Proceedings of the IEEE Conference
on  Computer  Vision  and  Pattern  Recognition
(CVPR), Honolulu, HI, USA, pp. 1907-1915, 2017.
[20]
 Z. Wang, J. Wang, Z. Meng, G. Zhao, and C.
Jiang,“Omni-explorer: A rapid autonomous explo-
ration framework with FOV expansion mechanism,”
IEEE Transactions on Cybernetics, vol. 55, no. 9,
pp. 4219-4230, 2025.
[21]
 A. Jonnalagadda, Y. S. Verma, M. V. Bharat, and
E. Z. Ushus,“Efficient path planning in multi-agent
environment  of  UAVs  with  payloads,”  IEEE
Access, vol. 13, pp. 57932-57942, 2025.
[22]
 J. Gu, Y. Wang, M. Su, X. Kong, K. Duan, and M.
Yu,“Multi unmanned vehicle cooperative encir-
clement control based on bidirectional long short-
term memory and mixed reward functions,” Scien-
tia Sinica Technologica, vol. 54, no. 9, pp. 1665-
1675, 2024.
[23]
 J. Gu, Y. Wang, W. Ji, Z. Wei, and J. Wang,
“LLM-based dynamic event-triggered communica-
tion for multi-UAV formation control in urban
environments, ” IEEE Transactions on Cognitive
Communications  and  Networking,  early  access,
2025. https://ieeexplore.ieee.org/abstract/docu-
ment/11300260.
[24]
Wenjie Zhang et al.  /  DDQN-Based 3D Path Planning Algorithm for UAVs in Dynamic Dense Obstacle Environments
—  95  —

## Page 13

Wenjie Zhang received the B.E. degree
from Zhejiang University of Technology,
Hangzhou, China,  in  2020.  He  is   cur-
rently pursuing a postgraduate degree at
Nanjing  University  of  Aeronautics  and
Astronautics, Nanjing, China.
Meng  Yu received  the  B.S.  degree  in
thermal  and  power  engineering  from
Tianjin  University,  Tianjin,  China,  in
2010,  and  the  Ph.D.  degree  in  aircraft
design from Harbin Institute of Technol-
ogy, Harbin, China, in 2016. In 2016 he
joined  School  of  Astronautics,  Nanjing
University of  Aeronautics  and  Astronautics.  He  is   cur-
rently  an  Associate  Professor  at  School  of  Astronautics,
Nanjing  University  of  Aeronautics  and  Astronautics.  He
has been actively involved in research on unmanned sys-
tems  and  intelligent  decision-making.  He  participated  in
major  aerospace  projects  in  China,  including  Mars  EDL
(Entry, Descent, and Landing) guidance, navigation, and
control, polar lunar rover pre-research, and manned lunar
landing pre-research. He has led several research projects,
including  the  National  Natural  Science  Foundation  for
Young Scientists, Aeronautical Science Fund, Civil Avia-
tion  Research  Project,  and  Manned  Space  Research
Project.
Yin  Wang received  the  B.S.  degree  in
electrical  engineering  and  automation
from  Nanjing  University  of  Aeronautics
and  Astronautics,  Nanjing,  China,  in
2008, and the Ph.D. degree in biomedi-
cal  engineering  from  City  University
London,  London,  UK,  in  2011.  In  2012
he  joined  School  of  Astronautics,  Nanjing  University  of
Aeronautics  and  Astronautics.  He  is  currently  Professor
and Vice  Dean  at  School  of  Astronautics,  Nanjing   Uni-
versity  of  Aeronautics  and  Astronautics.  He  is  also  a
Senior  Member  of  the  Chinese  Society  of  Astronautics;
Committee  Member  of  the  Guidance,  Navigation,  and
Control Sub-Committee of the Chinese Aeronautical Soci-
ety;  Committee  Member  of  the  Unmanned  Aircraft
Autonomous Control Professional Committee of the Chi-
nese  Automation  Society;  Committee  Member  of  the
Trusted Control Systems Professional Committee. Addi-
tionally, he serves as the Editor-in-Chief for the Interna-
tional Journal of Applied Pattern Recognition and Edito-
rial  Board  Member  for  IEEE  Transactions  on  Circuits
and Systems II: Express Briefs and the Guidance, Naviga-
tion, and Control Journal.
Journal of Beijing Institute of Technology，2026，Vol. 35，No. 1
—  96  —
