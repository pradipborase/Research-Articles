# Distributed Multi-Agent Deep Reinforcement Learning Based Navigation and Control of UAV Swarm for Wildfire Monitoring.pdf

## Page 1

Distributed Multi-Agent Deep Reinforcement
Learning based Navigation and Control of UAV
Swarm for Wildfire monitoring
Adeeba Ali
Department of Computer Engineering
Aligarh Muslim University
Aligarh, India
aliadeeba98@gmail.com
Rashid Ali
Department of Computer Engineering
Aligarh Muslim University
Aligarh, India
rashidaliamu@rediffmail.com
M.F. Baig
Department of Mechanical Engineering
Aligarh Muslim University
Aligarh, India
drmfbaig@yahoo.co.uk
Abstract—Decentralized deep reinforcement learning is an
emerging and most effective approach to solve the problem of
resource allocation and coordination among the swarm of UAVs.
Nowadays, the use of autonomous aerial vehicles in wildfire
monitoring is increasing and considered as the reasonably feasible
option as surveillance in calamity-hit areas can benefit from this
kind of automation. The flocks of UAVs can generate maps of
affected areas which could improve the process of relief planning
so that necessary aid can be reached the burnt areas quickly. This
paper presents the Multi-agent Deep Q network-based technique
for planning optimized trajectories for the UAV swarm which
can sense the wildfire in the forests and nearby regions. In
this work, the UAV agents are trained over simulated wildfires
in virtually generated forests with two reward schemes. The
simulation results verify the effectiveness of the proposed strategy
for leveraging it in real-world scenarios.
Index Terms—swarms, reinforcement learning, navigation,
wildfire, decentralized control, UAV
I. INTRODUCTION
Since the last few years, the spread of massive wildfires
all across the world has caused substantial environmental,
economic, and social effects [1]. And, the most dreadful effects
of wildfire include the death of human beings, as well as
other medical problems that arise due to high temperature,
smoke inhalation, debris, and vehicle crashes. Similarly, the
adverse effects of wildfires on environmental health include
degradation of air quality and the change in the overall global
composition of the atmosphere as wildfires emit Carbon Diox-
ide (CO2) in large quantities, thus leading to global warming.
Furthermore, uncontrolled wildfires are also responsible for the
extinction of some species of flora and fauna in that particular
location.
In order to reduce the amount of loss caused due to
wildfires, it is important to keep account of the information
regarding the fuel map, movement, and spread of fire front and
climate conditions. The availability of this kind of accurate
real-time information can reduce the risk concerned with the
lives of firefighters and increase success in the efforts made
to control the spread of fire [2]. The images captured by the
satellites are one of the key ways to gather information about
wildfires in real-time. However, these images can only be made
available if the satellite goes over that particular region of
interest. Additionally, satellite photos with tiny flames have
low spatial resolution [3]. Man-made aerial aircraft, which are
rather expensive and need a highly competent human pilot, are
the other alternate option for getting useful information. One
of the most interesting alternatives is the use of autonomous
UAVs (Unmanned Aerial Vehicles) to monitor wildfires and
record the information in real-time [3]. In addition to the
commands transmitted via remote controller, the flight con-
troller used in the autonomous aerial vehicles can also ac-
cept commands guiding the exterior maneuver. The GNSS
coordinates and IMU (Inertial Measurement Unit) state data
are included in the external commands. External commands
may be sent directly from the processor incorporated in the
drone hardware and physically attached to the flight controller,
or they may be transmitted from a ground workstation via
a communication medium. However, in some nations, it is
needed to designate at least one safety pilot to manually send
commands to the drone in emergency situations, despite the
fact that autonomous UAVs often only require a single operator
to launch the system.
The use of multiple UAV agents instead of a single UAV
increases the robustness and efficiency of the system [2].
Furthermore, the use of multiple smaller and cheaper aerial
vehicles would minimize the overall cost of the system,
thereby increasing the adoption of this kind of system by orga-
nizations that possess comparatively fewer financial resources.
In contrast, some additional challenges are associated with
the use of multiple UAVs, such as the need for an efficient
algorithm that can establish proper coordination among the
UAVs. Although the UAVs equipped with lasers and infrared
sensors are barely used by all public and private services for
wildfire detection due to high operational costs, hence the
autonomous cooperative control of UAV swarms especially for
the task of wildfire monitoring is yet to be further investigated
[4-9]. In the literature, collaborative control of multiple UAV
agents can be achieved either by planning optimized and
predefined trajectories to the goal position or using techniques
2023 IEEE 4th Annual Flagship India Council International Subsections Conference (INDISCON)
979-8-3503-3355-8/23/$31.00 ©2023 IEEE
2023 IEEE 4th Annual Flagship India Council International Subsections Conference (INDISCON) | 979-8-3503-3355-8/23/$31.00 ©2023 IEEE | DOI: 10.1109/INDISCON58499.2023.10270198
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:43:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 2

based on decentralized control theory or RHO (Receding Hori-
zon Optimization). In [11] the authors proposed an approach
that outperforms the traditional RHO method for wildfire
monitoring with two aircraft. The technique presented in
[11] is based on deep reinforcement learning (Deep-RL), and
the results demonstrated in the paper shows that learning-
based mechanisms for cooperative control tasks are promising
alternatives. Typically, the researchers leverage off-policy Q-
learning [12-13] which is an uncomplicated and classical
approach in the field of navigation and control of multiple
robots. In [5] deep reinforcement learning has been previously
used for autonomous wildfire monitoring through multiple
UAVs.
The objective behind this research is to investigate and
validate the techniques that can efficiently deal with the chal-
lenges associated with collaborative multi-agent reinforcement
learning leveraged for surveillancing a wildfire with multiple
UAVs. Inspired by [5] we propose a DQN (Deep Q-Networks)
based solution for cooperative control of multiple UAVs while
monitoring the wildfire. In addition to this, the effect of reward
sharing is explored in this research, which is considered as
another possible feedback scheme in swarm applications [14].
The rest of the paper is organized as follows. The review of
related work is presented in Section II. Then the problem is
formally stated in Section III. Next, the implementation details
of the formulated problem as POMDP (Partially Observable
Markov Decision Process) are discussed in Section IV. This
is followed in Section V by a detailed description of the
proposed solution for wildfire monitoring. Then the proposed
methodology is validated through simulations in Section IV.
Finally, the summary of the paper is presented in Section VII.
II. RELATED WORK
UAVs are used to gather valuable data and information
through surveillance and continuous monitoring in a wide
range of applications, including smart agriculture [15], post-
disaster hazardous material [16], or wildfire monitoring [2].
In this work, the use of multiple UAVs in wildfire moni-
toring applications [2] is studied. Earlier, wildfire detection,
fire front tracking, and hotspot hunting after fire have all been
accomplished using thermal imagers and visible light cameras,
as well as a combination of both [3]. [17] provides an overview
of various infrared-light-based methods for monitoring wild-
fires from UAVs and satellites.
In contrast to satellite imaging, aerial wildfire detection,
and monitoring provide a high-quality temporal and spatial
resolution [3], [18]. The authors of [19] illustrated how a
remotely controlled UAV may be used to monitor wildfires
in sizable regions. In comparison to using a single UAV, using
many UAVs for surveillance and monitoring is more effective
[3]. Techniques to control the flock of UAVs during the
simulation of wildfire detection and monitoring were presented
in [2], [7-8], [20-22]. In [23], the authors demonstrated a
decentralized mechanism to estimate the wildfire model. The
proposed strategy was tested using real-time drone hardware
and a stochastic fire simulator was used for generating data.
Later, in [24] the authors validated their proposed cooperative
control algorithm in real-time field experiments.
The aforementioned methods use principles from control
theory to predict the movements of the UAVs. In [11], the au-
thors demonstrated that deep reinforcement learning methods
outperformed classical control theory techniques for the task
of monitoring wildfires with two airplanes using a random
wildfire simulator.
In [6] the authors put forward a deep reinforcement learning
strategy to search for burning trees and then utilize a retardant
to put out the fire. Similar to [25], the authors looked into an
equilibrium-based Q-learning variation to finish the coverage
challenge successfully. Moreover, deep reinforcement learning
has also been utilized to gather relevant information through
learning a particular task. In [27], the authors present the multi-
robot information-gathering method (Deep-IG) to allow the
agents to capture valuable and relevant information without
colliding with each other. With the use of three UAVs, the
suggested technique was tested for terrain mapping.
The algorithms proposed in [11], [25-27] were leveraged
for learning and establishing coordination among multi-robot
agents, thus exemplifying the challenges associated with col-
laborative multi-agent reinforcement learning problems.
III. PROBLEM FORMULATION
A. Environment
The simulated wildfire surveillance environment is repre-
sented through a 2-D map enclosing a 1 Km2 area which is
discretized into 100×100 grid of burnable cells. The generated
dynamic maps of the environment are of two types:
• B(s): Fuel map in which each cell represents the amount
of flammable material present in that particular region.
• F(s): Fire map which is a boolean representation of the
environment consisting of either the value ‘0’ or ‘1’ in
each cell where ‘1’ represents the presence of fire in that
particular cell.
The simulated wildfire environment with the evolution of fire
across the maps over an episode is shown in Fig. 1. The cells
of the fuel map are updated every 2.5 sec in accordance to the
following two equations:
Bt+1(s) =
(
max(0, Bt(s) −βp(s)), if F t(s) = 1
Bt(s),
otherwise
(1)
where β is the burning rate which is set to 1, and
p(s) =
(
1 −Q
s′|d(s,s′)<dmp(1 −P(s, s′)Ft(s′)), if Bt(s) > 0
0,
otherwise
(2)
where p(s) is the probability that the cell s of the environment
will catch fire, d(s, s′) is the distance between cells s and s’,
dmp is the maximum distance at which propagation can happen
and P(s, s′) is the probability that cell s′ ignites cell s which
is defined as follows:
P(s, s′) = w.d(s, s′)−2
(3)
where w is constant proportional to the wind speed.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:43:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 3

(a) t = 0s.
(b) t = 100s.
(c) t = 200s.
(d) t = 300s.
(e) t = 400s.
(f) t = 500s.
Fig. 1. An example wildfire evolution over time. Left: burning cells. Right: fuel left.
B. Agents
Fixed-wing aircraft are considered as agents for this prob-
lem. It is assumed that the aircraft will fly with a constant
velocity v of 20 ms-1 and each agent is allowed to decide the
increment or decrement of its bank angle (ϕ), also known as
angle of tilt, by 5 degrees at the 10 Hz frequency. The position
of the aircraft is updated according to the kinematic model of
a fixed-wing aerial vehicle. The maximum bank angle that a
UAV can take is fixed to 50 degrees and UAV maneuvers going
beyond this range will not be considered valid. This constraint
will set angular velocity within realistic limits.
IV. SWARMDP DESCRIPTION
Rather than using the ”Partially Observable Markov De-
cision Process” (POMDP) as a model [28], the navigation
problem is framed as a special case of Decentralized POMDP,
that is swarMDP [29]. Through this design, the multi-agent
settings can be explicitly modeled by assuming that all the
agents have similar configurations.
Definition 1. The swarMDP problem is formulated in two
parts. First, a vector ˙A = ⟨S, A, B, π⟩, where ˙A represents
the local attributes associated with each swarm agent and the
value of each tuple variable is determined as follows:
• S: collection of states.
• A: set of actions.
• B: collection of observations.
• π: policy (B →A).
In the second step, the swarMDP is finally defined using a
tuple of 7 dimensions ⟨N, ˙A, P, R, O, γ⟩where:
• N is the ordered collection of indices corresponding to
the aircraft. The index values in the set should be in the
range from 1 to N, where N represents the total number
of UAV agents.
•
˙A is the prototype of the agent as defined above.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:43:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 4

• P : S2 × A →[0, 1] is a function to compute the
probability of going from one state to another, where
P(s′|s, a) denotes the transition probability that the agent
will move to state s’ from state s after taking action a.
• R : S × A →R is the reward function, where R(s, a) is
the reward given to an agent when it takes action a in
state s.
• O : S × Z × A →[0, 1] is the observation model, where
O(z′|s, a) is the probability that an agent observes z’
after playing an action a in state s.
• γ ∈[0, 1] is the discount factor for the total reward
accumulated by the UAV agent in the future.
A. UAV State
The localization of each aircraft in the local environment
depends on the following factors:
• Fuel map B(s) which has to be updated every 2.5 sec by
the wildfire simulator.
• The positional coordinates (xi, yi).
• The angle of yaw (ψi).
• The angle of tilt (ϕi).
B. UAV Actions
For each agent the vector of UAV local actions is given by
A = ⟨decrease angle of tilt (ϕ) by 5 degrees, increase angle
of tilt (ϕ) by 5 degrees ⟩. Each agent in the swarm has to
select any of these actions at a period of 0.1 sec.
C. Observations
Every agent in the swarm receives two different types of
data: a feature vector that shows some information about the
UAV’s and other UAVs’ nearby conditions, and a picture that
shows a partial view of the wildfire as seen by the UAV.
With each agent i, a feature vector is associated which
is computed after the concatenation of four other vectors
related to the local state variables of UAVs: the set of
all
the
bank
angles
ϕ
=
{ϕk|k ranges from 1 to N};
the
range
of
distance
to
other
UAVs
ρi
=
{ρik|k ranges from 1 to N and k should not be equal to i};
the
relative
heading
angle
to
other
UAVs,
θi
=
{θik|k ranges from 1 to N and k should not be equal to i};
the
relative
heading
angle
of
other
UAVs,
ψi
=
{ψik|k ranges from 1 to N and k should not be equal to i}.
The optical hemispherical camera of the UAV is used to
take the photos, which have a maximum range of 500 m and a
view angle of 160 degrees pointing downhill. After processing
the image is downsampled to the resolution of 30 × 40 pixels
representing the burning trees and forest.
The image is captured after sampling the points of interest
at the horizontal angle of 40 degrees from the cardinal and at
30 degrees of elevation from the lowest point to 10 degrees
below the skyline. This strategy results in a high-quality image
of the region right below the UAV. The characteristics of this
image determine the degree of partial observability of the
environment.
D. Rewards
The reward received by each agent i is the sum of four
independent components:
r1 = −λ1
min
{s∈S|Ft(s)} ds,
(4)
r2 = −λ2
X
{s∈S|ds≤r0}
1 −Ft(s),
(5)
r3 = −λ3ϕ2
0,
(6)
r4 = −
X
{k∈1,2,...,N∧k̸=i}
λ4exp(−
ρik
ϵ )
(7)
where ds is the measure of displacement from the UAV to a
given cell s of the map. The aforementioned equations mention
negative rewards or penalties for the following:
• Distance from fire (r1): proportional to the distance of
the closest cell set on fire.
• Safe cells nearby (r2): proportional to the count of safe
cells that doesn’t ignite in a radius r0.
• High bank angles (r3): depends on the square of the UAV
bank angle (ϕ).
• Nearness to other UAV (r4): sum of work done by all
other agents, which, at the point of saturation, equals the
constant value of λ4.
The constant parameters used in the above equations have been
given the following values: λ1 = 10, λ2 = 1, λ3 = 100, λ4 =
1000, r0 = 10, c = 100.
The reason behind tuning the parameters to these values is
that going away from the burning region should be penalized
heavily and, the negative rewards obtained from the bank angle
and getting close to other UAVs should become dominant.
V. METHODOLOGY
A. Deep Reinforcement learning
The objective behind the presented approach is to determine
the policy π that can optimally map observations to actions.
The reward function R, which was defined in the preceding
section, determines how ideal the situation is. The value
Q(s, a) for each state-action pair can be calculated from
the optimal policy, π. When an agent, a, acts in a state s,
the expected cumulative reward is represented by the value
function Q(s, a). The following Bellman equation can be used
to calculate the value of the Q function:
Q(s, a) = r(s, a) + {γ
X
s′∈S
p(s′|s, a) max
a′∈A Q(s′, a′)}
(8)
For a given Q value function the optimal policy can be deduced
as:
π(s) = arg max
a∈A Q(s, a)
(9)
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:43:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 5

A deep neural network that can approximate the function can
be trained to estimate the Q-value using DQN [30, 31]. The
network is trained using the loss function defined as follows:
Li(θi) = Es,a,r,s′[e2]
(10)
where e is the Bellman error:
e = r(s, a) + {γ max
a′ Q(s′, a′|θ−) −Q(s, a|θ)}
(11)
The agent must make a choice between exploring the state-
action space using stochastic policy and using the prior infor-
mation that was gleaned from the estimation of the optimal
policy in earlier states while the network is being trained.
The most common method for solving this issue is to use
exploratory policy during the initial training iterations and
then gradually increase the percentage of activities involving
exploitation policy.
Deep Q Networks (DQN) circumvent the inherent instability
problem of deep reinforcement learning through two mecha-
nisms:
• By randomizing the training samples using the experience
replay method to reduce the correlation effect of the se-
quence. This can be implemented using a replay memory
E.
• By simultaneously training the second (target) network
(with parameters θ−) to predict Q(s′, a′) while training
it at a slower update rate than the former (first) network
(with parameters θ), the first network can learn the fixed
target.
B. Network Architecture
In the implemented method the deep Q networks deal with
two different types of observations separately. The feature vec-
tor ⟨N, ˙A, P, R, O, γ⟩goes through a series of dense hidden
layers each consisting of 100 neurons with ReLU activation
function. Following that, a series of dense convolutional and
max pooling layers downsampled the monocular image with
incomplete environmental information before feeding it to
the dense hidden layers of neurons. Two extra thick layers
combine and analyze the outputs from both networks before
estimating the Q-values for the agents. The complete network
architecture is represented in Fig. 2.
C. Reward Schemes
During the training of Deep Q networks, two different
kinds of reward approaches are compared according to their
degree of decentralization. Once the network is trained both
the models can be used for distributed control.
1) Independent rewards: Each agent obtains its own reward
separately from the environment.
2) Shared reward: It is calculated as the mean of the
independent rewards and shared by all the agents.
VI. EXPERIMENTAL RESULTS
A. Simulation Setup
Both the DQN-based fire detection models trained with
two different reward configurations are tested in simulated
environments. Training of the network is performed every 100
steps after the collection of 100 new samples. A small batch
size of 2000 samples is used in every iteration of training.
These training samples are arbitrarily taken from the last
100,000 examples buffer. The target network is updated after
every update of 10 action values, that is, once every 1000 steps.
In order to prevent the overfitting of the network with the first
sequence of samples, the learning of the network starts after
the first 2000 steps. The choice of training the network with
exploratory actions starts at a fraction of 1 and then linearly
decreases during the initial 80 percent of training time and
finally stays at the constant value of 0.1 until the training ends.
The simulation experiments have a duration of 10,000 steps
(20 minutes). Adam [32] is used as the stochastic optimizer
of the network and the learning rate is set to the value of
6 × 10−9.
B. Results
The major evaluation metric of the proposed approach is
the accumulated reward of all simulated episodes which is
determined as the sum of the instantaneous rewards earned by
all agents over an episode. Fig. 3 represents the simulation of
an episode demonstrating the behavior learned by the agents.
As the wildfire propagates in the region, the UAVs learn to
head toward the burning areas and start making wider circles.
The third component (r3) of the reward function, which is
the penalty for the collision between aircraft is effective in
making the agents fly around the burning region in the same
direction and at opposite endpoints of the fire while staying far
away from each other. In the small region of interest (ROI),
the penalty arises due to the nearness between the UAVs
outweighing the other and one of the UAVs stays there making
circles of small radii. Furthermore, As demonstrated in Fig. 4
with both the reward configurations agents are allowed to learn
the monitoring task effectively by minimizing their penalties
on average. It is expected that similar performance is obtained
with both the reward schemes for this problem as three of
the four reward components (r1, r2, r3) are independent of
the learning behavior of other UAV agents that is, only better
estimation of the local state of the UAV can affect the margin
of improvement.
VII. CONCLUSION
In this paper, a DQN-based approach is proposed to provide
decentralized control to multiple UAVs for monitoring the
spread of wildfires. The deep Q networks take a processed
monocular image consisting of partial observation of the
surroundings and the local state vectors of the UAV as input
and generate the control actions for the agents. The proposed
method is tested with 2 reward configurations which differ
in their degree of federating multiple UAV agents. Simulation
results show that UAVs can effectively monitor the wildfire in a
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:43:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 6

Fig. 2. Network Architecture
cooperative and coordinated manner with both types of reward
schemes. Thus, the presented control design can be applied
to real-time UAV-aided surveillance in wildfire regions to
minimize operational costs. The DQN are trained on simulated
fire maps from forests but the model should perform well on
all types of wildfires as long as enough data is available for
training.
Fig. 4: Comparison of reward schemes at the time of training
REFERENCES
[1] S. Doerr, and C. Santin, “Global trends in wildfire and its impacts:
Perceptions versus realities in a changing world,” Philosophical Trans-
actions of The Royal Society B Biological Sciences, vol. 23, no. 2, pp.
438–454, 2016.
[2] S. Sudhakar et al., “Unmanned Aerial Vehicle (UAV) based Forest
Fire Detection and monitoring for reducing false alarms in forest-fires,”
Computer Communications, Elsevier, 2020, pp. 6648–6653.
[3] F. Saffre et al., “Monitoring and Cordoning Wildfires with an Au-
tonomous Swarm of Unmanned Aerial Vehicles,” Drones, MDPI, vol.
6, no. 10, p. 301, 2022.
[4] F. Afghah, A. Razi, J. Chakareski, and J. Ashdown, “Wildfire Monitoring
in Remote Areas using Autonomous Unmanned Aerial Vehicles,” in
MiSARN 2019: Mission-Oriented Wireless Sensor, UAV and Robot
Networking, IEEE Infocom Workshops, 2019.
[5] S. Zhang, W. Wang, Z. Liu, and Z. Wu, “Forest Farm Fire Drone
Monitoring System Based on Deep Learning and Unmanned Aerial
Vehicle Imagery,” Mathematical Problems in Engineering, Hindawi, pp.
5181–5188, 2021.
[6] A. Sharma, and P.K. Singh, “UAV-based framework for effective data
analysis of forest fire detection using 5G networks: An effective ap-
proach towards smart cities solutions,” International Journal of Commu-
nication Systems, 2021, pp. 1067 1074.
[7] Y. Liu, “Forest Fire Monitoring Method Based on UAV Visual and
Infrared Image Fusion,” Remote Sensing, MDPI, vol. 39, no. 4, pp.
1530–1548, 2023.
[8] R, N. Haksar and M. Schwager, “Distributed Deep Reinforcement
Learning for Fighting Forest Fires with a Network of Aerial Robots,”
in 2018 IEEE/RSJ International Conference on Intelligent Robots and
Systems (IROS), pp. 835–840, 2019.
[9] P. Jain et al., ”A review of machine learning applications in wildfire
science and management,” Canadian Science Publishing, vol. 28, no. 4,
pp. 229–255, 2020.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:43:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 7

(a) t = 100s.
(b) t = 200s.
(c) t = 300s.
(d) t = 400s.
Fig. 3. An example of an episode in wildfires with two aircraft trained with DQN, team reward scheme.
[10] M.M. Shahzad et al., “A Review of Swarm Robotics in a NutShell,”
Drones, MDPI, vol. 7, no. 269, 2023.
[11] X. Mo, D. Peters, and C. Lel, “Low-Cost Autonomous UAV Swarm
Application in Wildfire Surveillance and Suppression,” in ICMLT ’21:
Proceedings of the 2021 6th International Conference on Machine
Learning Technologies, ACM, 2021.
[12] G. Lozengues, “On the Distributivity of Multi-agent Markov Decision
Processes for Mobile-Robotics,” International Symposium on Swarm
Behavior and Bio-Inspired Robotics, 2021.
[13] A. Oroojlooy, and D. Hajinezhad, “A review of cooperative multi-agent
deep reinforcement learning,” Applied Intelligence, Springer, vol. 53,
pp. 13677–13722, 2023.
[14] X. Zhu, F. Zhang, and H. Li, “Swarm Deep Reinforcement Learning for
Robotic Manipulation,” Procedia Computer Science, Elsevier, vol. 198,
pp. 472-479, 2022.
[15] N. Maurya et al., “Recent Advancement and Role of Drones in Forest
Monitoring,” Advances in Remote Sensing for Forest Monitoring, 2022.
[16] P. G. Martin, S. Kwong, N. Smith, Y. Yamashiki, O. D. Payton, F. Russell
Pavier, J. S. Fardoulis, D. Richards, and T. B. Scott, “3d unmanned
aerial vehicle radiation mapping for assessing contaminant distribution
and mobility,” International journal of applied earth observation and
geoinformation, vol. 52, pp. 12–19, 2016.
[17] F. Vivo, M. Battipede, and E. Johnson, “Infra-red line camera data-
driven edge detector in UAV forest fire monitoring,” Aerospace Science
and Technology, Elsevier, vol. 111, p. 106574, 2021.
[18] C. Maffei, R. Lidenbergh, M. Meneti, “Combining multi-spectral and
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:43:23 UTC from IEEE Xplore.  Restrictions apply.

## Page 8

thermal remote sensing to predict forest fire characteristics,” ISPRS
Journal of Photogrammetry and Remote Sensing, vol. 181, no. 8, pp.
400-412, 2021.
[19] C. Hyun, M. Park, W. Lee, “Remotely Piloted Aircraft System (RPAS)-
Based Wildlife Detection: A Review and Case Studies in Maritime
Antarctica,” Animals, MDPI, vol. 10, no. 12, p. 2387, 2020.
[20] V. Sherstjuk, M. Zharikova, and I. Sokol, “Forest Fire Monitoring
System Based on UAV Team, Remote Sensing, and Image Processing,”
in Proceedings of the 2018 IEEE Second International Conference on
Data Stream Mining and Processing (DSMP), 2018.
[21] J. Hu et al., “Fault-tolerant cooperative navigation of networked UAV
swarms for forest fire monitoring,” Aerospace Science and Technology,
Elsevier, vol. 123, p. 107494, 2022.
[22] S. Codgay and G. Secinti, “Phoenix: Aerial Monitoring for Fighting
Wildfires,” Drones, MDPI, vol. 7, no. 1, p. 19, 2023.
[23] I. Alsammaket et al., “Nature-Inspired Drone Swarming for Wildfires
Suppression Considering Distributed Fire Spots and Energy Consump-
tion,” IEEE Access, vol. 11, 2023.
[24] L. Merino, F. Caballero, J. R. Mart´ınez-de Dios, J. Ferruz, and A.
Ollero, “A cooperative perception system for multiple uavs: Application
to automatic detection of forest fires,” Journal of Field Robotics, vol.
23, no. 3-4, pp. 165–184, 2006.
[25] Z. Mou et al., “Three-Dimensional Area Coverage with UAV Swarm
based on Deep Reinforcement Learning,” in Proceedings of ICC 2021
- IEEE International Conference on Communications, 2021.
[26] A.Tan, F. Bejarano, Y. Zhu, R. Ren, and G. Nejat, “Deep Reinforce-
ment Learning for Decentralized Multi-Robot Exploration With Macro
Actions,” IEEE Robotics and Automation Letters, vol. 8, no. 1, pp. 272-
279, 2023.
[27] A. Viseras and R. Garcia, “DeepIG: Multi-robot information gathering
with deep reinforcement learning,” IEEE Robotics and Automation
Letters, vol. 4, no. 3, pp. 3059–3066, 2019.
[28] A. Viseras, M. Meissner, and J. Marchal, “Distributed wildfire surveil-
lance with autonomous aircraft using deep reinforcement learning,”
IEEE Access, vol. 4, pp. 1–11, 2016.
[29] K. Kim et al., “An Application of Inverse Reinforcement Learning to
Estimate Interference in Drone Swarms,” Entropy, MDPI, vol. 24, no.
10, pp. 1413–1421, 2022.
[30] V. Mnih, K. Kavukcuoglu, D. Silver, A. Graves, I. Antonoglou, D.
Wierstra, and M. Riedmiller, “Playing Atari with deep reinforcement
learning,” arXiv preprint arXiv:1312.5602, 2013.
[31] V. Mnih, K. Kavukcuoglu, D. Silver, A. A. Rusu, J. Veness, M. G.
Bellemare, A. Graves, M. Riedmiller, A. K. Fidjeland, G. Ostrovski et
al., “Human-level control through deep reinforcement learning,” Nature,
vol. 518, no. 7540, p. 529, 2015.
[32] D. P. Kingma and J. Ba, “Adam: A method for stochastic optimization,”
arXiv preprint arXiv:1412.6980, 2014.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:43:23 UTC from IEEE Xplore.  Restrictions apply.
