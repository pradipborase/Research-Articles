# Continuous Transfer Learning for UAV Communication-Aware Trajectory Design.pdf

## Page 1

Continuous Transfer Learning for UAV
Communication-aware Trajectory Design
Chenrui Sun∗, Gianluca Fontanesi†, Swarna Bindu Chetty∗, Xuanyu Liang∗, Berk Canberk‡ and Hamed Ahmadi∗
∗School of Physics Engineering and Technology, University of York, United Kingdom
†Interdisciplinary Centre for Security, Reliability, and Trust (SnT), Luxembourg
‡, Edinbrough Napier University, Edinbrough, United Kingdom
Email: chenrui.sun@york.ac.uk, gianluca.fontanesi@ieee.org, swarna.chetty@york.ac.uk,
xuanyu.liang@york.ac.uk, b.canberk@napier.ac.uk, hamed.ahmadi@york.ac.uk
Abstract—Deep Reinforcement Learning (DRL) emerges as a
prime solution for Unmanned Aerial Vehicle (UAV) trajectory
planning, offering proficiency in navigating high-dimensional
spaces, adaptability to dynamic environments, and making se-
quential decisions based on real-time feedback. Despite these
advantages, the use of DRL for UAV trajectory planning requires
significant retraining when the UAV is confronted with a new
environment, resulting in wasted resources and time. Therefore,
it is essential to develop techniques that can reduce the overhead
of retraining DRL models, enabling them to adapt to constantly
changing environments. This paper presents a novel method to
reduce the need for extensive retraining using a double deep
Q network (DDQN) model as a pre-trained base, which is
subsequently adapted to different urban environments through
Continuous Transfer Learning (CTL). Our method involves
transferring the learned model weights and adapting the learning
parameters, including the learning and exploration rates, to suit
each new environment’s specific characteristics. The effectiveness
of our approach is validated in three scenarios, each with
different levels of similarity. CTL significantly improves learning
speed and success rates compared to DDQN models initiated
from scratch. For similar environments, Transfer Learning
(TL) improved stability, accelerated convergence by 65%, and
facilitated 35% faster adaptation in dissimilar settings.
Index Terms—Unmanned Aerial Vehicle, Deep Reinforcement
Learning, Trajectory Planning, Transfer Learning, 6G.
I. INTRODUCTION
Unmanned Aerial Vehicles (UAVs) are increasingly em-
ployed in a broad spectrum of applications, including surveil-
lance, agriculture, disaster management, and communication
infrastructure maintenance [1]. Efficient planning and opti-
mization of UAV trajectories is critical, since the success of
numerous UAV applications, such as real-time data transmis-
sion and remote sensing, heavily relies on a reliable trajectory.
One of the key challenges in UAV trajectory is ensuring robust
communication between UAVs and ground-based infrastruc-
ture, such as Base Stations (BSs). This challenge becomes
even more pronounced in complex urban environments with
obstacles and interference.
Beside conventional optimization methods, Reinforcement
Learning (RL) methods have emerged as suitable Machine
Learning (ML) solutions for UAV trajectory planning due to
its proficiency in handling high-dimensional spaces, adapt-
ability to dynamic environments, and capability for sequential
decision-making based on real-time interactions and feedback
[2]. The navigation of UAVs from an initial location to a
final destination through RL has been extensively explored in
various related works [3]. RL approaches for UAV trajectory
and communication scenarios proposed in literature vary from
classical RL [4], to Deep Reinforcement Learning (DRL)
algorithms [5], [6]. Adding communication constraints, as
discussed in [7], [8], these works address the challenge of
frequency band allocation in UAV trajectory design using
DRL to ensure equitable communication services. These
works highlight the importance of frequency management in
UAV operations. To further improve performance of trajec-
tory, in [9], cellular-connected UAV technology was utilized
to enhance 3D communication coverage, employing DRL
with a model-based approach for trajectory optimization. The
strength of Deep Q Learning (DQL) lies in its ability to learn
optimal policies for UAV navigation through interaction with
the environment, thus enabling precise trajectory planning and
robust communication strategies.
Nevertheless, the utilization of DQL comes with limitations.
Although it performs well in learning tasks within specific
environments, these solutions are often tailored to particular
locations or maps. Adapting these models to new tasks or
different environments often requires extensive retraining,
a process that can be both time-consuming and resource-
intensive. This limitation is particularly evident in UAV opera-
tions that demand rapid adaptation to new contexts. In fact, the
challenges and dynamics faced by UAVs during navigation can
vary significantly from one environment to another, making
the applicability of DQL solutions limited in scope.
Compared with these prior works, we do not focus on
designing a more advanced RL algorithm to improve the
performance of the system. Instead, we investigate how to
share prior model knowledge to improve the RL training
convergence speed when the UAV faces a new environment.
Transfer Learning (TL) has emerged as an effective approach
among researchers to address this challenge. [10] applied TL
979-8-3503-7786-6/24/$31.00 © 2024 IEEE
2024 11th International Conference on Wireless Networks and Mobile Communications (WINCOM) | 979-8-3503-7786-6/24/$31.00 ©2024 IEEE | DOI: 10.1109/WINCOM62286.2024.10657767
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 11:35:03 UTC from IEEE Xplore.  Restrictions apply.

## Page 2

to enhance tracking performance by learning from the tracking
errors of UAVs with different dynamics without requiring
baseline controller modifications. Furthermore, [11] utilized
the teacher policy trained in a sub-6 GHz domain, which
accelerates path learning in a new millimeter Wave (mmWave)
domain. The authors also considered outage constraints and
used a robust double deep Q network (DDQN) as the base
model. In this study, a pre-trained model involves initially
training a DDQN, but targeting different domains that facil-
itate the transfer of knowledge across various environments.
In [12], author utilizes TL to adapt UAV trajectory design
to emergency scenarios where user distribution and terrain
change. Mainly simulate the scenario of certain BSs losing
their functions in emergency situations. However, this method
falls short of addressing the challenge of knowledge transfer
across diverse urban settings. Thus, it’s crucial to explore
the capability for continuous learning across various environ-
ments, beyond just adapting to situational and task changes
within a single map.
A. Contributions
This article is dedicated to evolving UAV path planning
training models into adaptable frameworks that facilitate faster
and repeated retraining in different environments with Contin-
uous Transfer Learning (CTL). We propose a shift from the
vanilla approach of one-time model training to a paradigm
of continuous adaptation, where UAVs are retrained with
new data and conditions as they transition between tasks and
environments. While an ad hoc trained RL model can only be
applied to a specific environment, this approach is not limited
to a specific environment and provides a flexible solution for
different scenarios. We propose a CTL framework to enable
RL for UAVs trajectory with connectivity constraint to rapidly
adapt to different environments. This approach involves first
pre-training a model to achieve a specific convergence target,
serving as a foundational base to reduce the cost of training
the model in the new environments. To this aim, we train
a policy for UAV trajectory that tackles ground-to-air link
outages and we evaluate both Deep Q-Network (DQN) and
DDQN models. Among various models with differing hyper-
parameters, the higher-performing trained DDQN is chosen
as the foundational learning model. A detailed analysis is
provided in Section III. Then, our method involves transferring
the learned model weights and adjusting the learning param-
eters, including the learning rate and exploration rates, to the
specific characteristics of each new environment. Specifically,
we consider the problem space formed by three scenarios,
namely: Environment 1 (dense urban landscape with tall
buildings), Environment 2 (emergency scenario), Environment
3 (suburban residential area). We evaluate the effectiveness of
our CTL approach through various tasks, targeting different
destinations, and in emergency conditions involving BSs fail-
ures. Simulation results show significant improvements in both
convergence times and stability in new environments.
II. SYSTEM MODEL AND PROBLEM FORMULATION
A. System Model
We consider a singular UAV-aided cellular network. The
core objectives of UAV are to navigate swiftly and efficiently
toward a designated target location while ensuring seamless
communication with a terrestrial cellular network. This op-
erational versatility extends to diverse geographical regions,
denoted as space of Environments S (X1, X2, X3), as shown
in Fig. 1, where each region presents unique building distri-
bution and communication needs. Map distinctions between
different environments include factors such as urban building
type, building density, street width, base station height, and
other relevant parameters.
BSs are deployed at specific locations within the urban area.
Let M be the set of BSs. Each BS m ∈M is characterized
by its geographical location (xs, ys) and height hs with 3
sectors j. The UAV embarks on its mission from a designated
initial location, represented as qI ∈R3×1, which can vary
for each deployment. The primary goal is to navigate the
UAV to a predetermined target point, marked as qF ∈R3×1,
while ensuring uninterrupted communication links with the
terrestrial network during the mission, with the probability
of communication outage maintained below requirement. The
UAV moves at constant speed V = Vmax along a 3D trajectory
of duration T that can be divided into K discrete segments
with interval δk = T/K, k = {1, ..., K}. δk is chosen
arbitrarily small so that within each step the large scale
signal power received by the UAV remains approximately
unchanged. Each segment is thus described by its discrete
coordinates q(n) = (xn, yn, hn).
The channel model considers various factors, including
large-scale path loss, small-scale fading, and environmental
elements like terrain and buildings. Large-scale path loss
represents the signal attenuation over distance and frequency.
The path loss is typically classified into: LoS (Line-of-Sight)
Path Loss Model: lL(d) = XL × d−αL. And NLoS (Non-
Line-of-Sight): lNL(d) = XNL × d−αNL [13]. We utilize the
three-sector antenna model (downtilted to serve ground User
Equipments (UEs) [11]), as defined by the 3rd Generation
Partnership Project (3GPP) specifications [14]. The antenna
gain is a critical component of signal reception from ground
BS to a UAV, which can be represented as Gm,j(θ, ϕ) =
A3GP P E(θ, ϕ) + AF(θ, ϕ, n). It combines the 3GPP antenna
element pattern (A3GP P E(θ, ϕ)) and array factor (AF(θ, ϕ, n)
to represent beamforming effects [15].
Fading phenomena describe signal variations over time
due to environmental changes, particularly UAV movement.
Fading coefficients f(t) represent instantaneous fading levels,
while small-scale fading powers f 2
0,i for both LoS and NLoS
environments follow Nakagami-M fading models [13]. To
compute the Signal-to-Interference-plus-Noise Ratio (SINR)
at a UAV from a specific ground BS (m) sector (j), the
Signal Power Ps = Pt,m × Gm,j(θ, ϕ) × Lpath(d) × Lfading,
Interference Power Pi = P
i̸=m Pt,i×Gi(θi, ϕi)×Lpath(di)×
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 11:35:03 UTC from IEEE Xplore.  Restrictions apply.

## Page 3

(a) Environment 1
(b) Environment 2
(c) Environment 3
Fig. 1: Comparative Visualization of UAV Operational Environments: This figure illustrates the UAV’s navigation challenges and strategies
across three environments. Graph a depicts a dense urban landscape with tall buildings; Graph b shows a sparse urban area with two scenarios:
a standard mission and an emergency scenario, emphasizing the UAV’s adaptability to sudden environmental changes; Graph c shows a third,
more differentiated scenario, modelling a suburban residential area and varying the distribution of base stations
Lfadingi, and Noise Power Pn = N0 × B are considered. Ps
accounts for the desired signal power. Pi aggregates interfer-
ence from all other BSs, and Pn represents noise power. The
SINR is computed as SINRmax,m,j =
Ps,j
Pi+Pn , (j ∈J =
1, 2, 3).
During UAV’s path, we consider an outage occurs when the
SINR is less than or equal to φth, leading to an outage events:
β(q(n)) = 1 if (SINR(q(n)) ≤φth). The total outage events
is denoted by Γ = PT
n=0 β(q(n)) .
B. Problem Formulation
The objective of this research is to improve the adaptability
of RL models, specifically DDQN, to novel environments
using CTL.
Our general goal is to ensure that the training time for a
policy πs in Environment s ∈S is significantly less than the
time required to train a new model from scratch for each new
environment. We can thus formulate
P : min
Ttrain(πs)
(1a)
s.t.
π(0)
new = πpre-trained,
(1b)
where denoted by Ttrain(πs) is the training time of policy πs in
the new enviroment s and (1b) specifies that a policy π1 pre-
trained in Environment 1 ∈S is used as benchmark for the
UAV trajectory in the new environment. Policy π1 is trained
using a DDQN model and then utilized for transfer learning
across two additional maps or scenarios. This approach neces-
sitates that after the transfer, the model maintains its original
trajectory objectives, i.e., minimizing the steps n needed to
reach its destination and to keep the frequency of outage
events Γ below a certain threshold ˆΓ. Policy π1 is thus trained
to solve problem:
min
n,q(n)
n + K × Γ
(2)
s.t.
q(0) = qI,
q(T) = qF
(3)
Γ < ˆΓ
(4)
h(u) > hB
(5)
n ≤N.
(6)
The variable q(n) represents the UAV’s position at step n,
qI and qF signify the initial and final positions of the UAV,
while q(T) presents the target position. Constraint (4) ensures
that the maximum outage events throughout the flight remain
below the specified threshold. Here h(u) denotes the altitude
of the UAV, hB represents the highest altitude of the building,
and N signifies the maximum permissible movement step of
the UAV, considering battery constraints.
III. RL AND CONTINUOUS LEARNING FOR UAV
TRAJECTORY DESIGN
A. Preliminaries
DQN and its enhancement, Double DQN, represent signifi-
cant advancements in integrating reinforcement learning with
deep neural networks for autonomous decision-making. DQN
facilitates learning from complex sensory inputs, overcoming
challenges like instability and convergence issues through
techniques such as experience replay and fixed Q-targets.
DDQN further refines this by correcting DQN’s overestima-
tion of Q-values, ensuring more stable and accurate outcomes.
This progression makes DQN and DDQN highly effective for
UAV trajectory optimization in diverse urban environments,
improving navigation precision in complex scenarios.
TL further enhances the learning process by utilizing
knowledge acquired in one task to expedite learning in related
but distinct tasks. It operates on the principle of reusing a pre-
trained model as a starting point for new tasks, significantly
cutting down on the time and data needed for training in
new environments or missions. Continuous Learning com-
plements these methodologies by enabling UAVs to continu-
ally assimilate new information without discarding previously
learned knowledge. This is crucial for operating in dynamic
environments where conditions and obstacles may change
unpredictably. Continuous learning ensures that UAVs can
iteratively update their navigation strategies, maintaining peak
performance and adaptability over time.
B.
DQN and DDQN for UAV Trajectory Design
In our considered scenario, the UAV navigation task is
modeled in a 3D space, where the UAV must reach a target
position, starting at a random position within the set range.
Given our UAV trajectory optimization, we can formulate the
problem as an Markov Decision Process (MDP), which is
defined by a tuple (S, A, P, R, γ). Each state s represents
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 11:35:03 UTC from IEEE Xplore.  Restrictions apply.

## Page 4

the UAV’s current position, communication conditions, and
the environment. Formally:
s = {q(n), SINR(q(n))},
where q(n) and SINR(q(n)) are the UAV’s position and signal
quality, respectively. The action space comprises potential
directions in which the UAV can move at any given time:
A = {move f, move b, move l, move r}.
Given a state s and an action a, P(s′|s, a) represents the
probability of transitioning to state s′. Since the UAV’s move-
ment is deterministic, given its current state and action, it will
deterministically arrive at the next state. The reward function
captures the objectives of minimizing the completion time and
maintaining satisfactory communication. It is presented as
R1(s, a, s′) = −k1 × d(s, starget) −k2 × F(qn) −Rn + Rarrive
(7)
where k1 and k2 are weighting factors to prioritize moving
closer to the destination and penalize outage events during
the transition. d(s, starget) represents the distance between the
UAV’s current position and the target position. F(qn) denotes
the signal outage penalty function, which increases the loss
for navigating through areas with poor signal quality. Rn is the
step penalty, and Rarrive is the reward for reaching the target.
The discount factor γ determines the present value of future
rewards. Given the MDP framework for the UAV trajectory
optimization, our goal is to find a policy π∗that maximizing
an expected cumulative reward:
π∗= arg max
π
E
" T
X
t=0
γtR(st, at, st+1)
#
,
(8)
where E denotes the expectation. The DQL agent uses two
neural networks: a primary network for action selection and
a target network for stable learning. Both DQN and DDQN
utilize a similar network structure for action selection and
evaluation, but DDQN’s critical distinction lies in its action
evaluation mechanism, which separates action selection from
its value estimation. This separation ensures a more con-
servative and accurate assessment of the potential of each
action, thereby enhancing the performance of trajectory de-
sign. In addition to this, we have designed MDP that is more
compatible with our scenarios to improve performance. This
includes adding SINR information to the state to ensures that
the models for transfer have sufficient depth of learning and
understanding of the environment. The rewards will also be
fine-tuned according to the situation when migrating to a new
environment.
C. Continuous Learning for UAV Trajectory Design
1) Environments: We define the first environment that was
used to train the DDQN base model as a dense urban area,
characterized by a high concentration of tall buildings that de-
mand complex navigational strategies to maintain connectivity
and avoid obstacles. Transitioning to the second environment,
the UAV encounters a sparse urban landscape with shorter
buildings, a stark contrast to the first. This environment is ex-
plored under two distinct scenarios which are a standard mis-
sion mirroring the parameters of the dense urban environment,
and an emergency scenario necessitating a sudden change in
mission objectives due to a BS failure. The adaptability of the
UAV is further tested in the third environment, a residential
area with low housing blocks and a different BS distribution,
presenting new navigational challenges and testing the UAV’s
ability to generalize its learned strategies to markedly different
landscapes.
Algorithm 1 CTL with DDQN across Environments
1: Initialize DDQN in Environment 1: learning rate α1,
exploration ϵ1, and exploration decay ϵdecay,1.
2: Train the model with a replay buffer and a periodically
updated target network to stabilize updates.
3: Save the model weights ξEnv1 and policy πEnv1
4: Transfer to Env2:
5: Initialize Env2 with DDQN model weights ξEnv2 ←ξEnv1
and policy πEnv2 ←πEnv1
6: Adjust learning parameters for Env2: set new learning rate
α2, ϵ2, and ϵdecay,2
7: Apply the new reward function R2(optional).
8: Retrain transferred model in Env2 using the fixed param-
eters, maintaining the strategy of experience replay and
target network updates.
9: Save the updated model weights ξEnv2 and policy πEnv2
10: Transfer to Env3 with process above
11: Continue this process for any subsequent environments,
transferring weights and policy while adjusting learning
parameters as needed
2)
Training in different Domain: The TL process begins
with training a DDQN model in a dense urban setting, stream-
lining the training approach to enhance efficiency without
requiring full model convergence. A targeted termination
criterion focuses on achieving a high success rate at the
destination rather than optimizing the total reward, shorten-
ing training by 600-800 episodes. This method is chosen
because, after reaching success rate convergence, the agent’s
main improvements involve strategies to avoid outage events,
which may vary in effectiveness across different environments.
This efficient training strategy reduces overall duration and
improves the model’s suitability for CTL. Subsequent findings
affirm the benefits of this balanced approach, demonstrating
its practical success.
This pre-trained model is then transferred to accommo-
date sparse urban and residential areas. This process entails
transferring the learned model weights and adjusting learn-
ing parameters, including the learning rate and exploration
rates, to suit each new environment’s specific characteristics
(algorithm 1). Through this methodical adaptation, the UAV
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 11:35:03 UTC from IEEE Xplore.  Restrictions apply.

## Page 5

0
200
400
600
800
1000
1200
1400
1600
1800
2000
Episode
20000
17500
15000
12500
10000
7500
5000
2500
Average Reward
DDQN in ENV1 Total Reward
DDQN in ENV1 Moving Average (100 episodes)
DQN in ENV1 Total Reward
DQN in ENV1 Moving Average (100 episodes)
Fig. 2: Compare of DQN with DDQN for Trajectory Design in Env1
demonstrates not only enhanced learning efficiency but also
improved performance and adaptability across diverse oper-
ational environments. By leveraging the knowledge gained
in each successive environment, CTL enables the UAV to
rapidly adjust to new challenges. The objective in the new
environment remains aligned with our dual goals. The model,
now starting with policy π(0)
new, is further trained to adapt to
the new conditions. The fine-tuning process involves iterative
updates of the policy parameters:
π(0)
new = πpre-trained,
(9)
π(k+1)
new
= π(k)
new −α · ∇πnewL(π(k)
new)
(10)
where α is the learning rate, and L represents the loss function
tailored to the new environment.
Then we evaluate the performance of the transferred model
in the new environment using metrics such as convergence
time Tconvergence and improvements in stability or accuracy.
These metrics will demonstrate the effectiveness of TL in
reducing training time and enhancing model performance in
diverse urban scenarios.
TABLE I: Summary of Model Parameters
Parameter Name
Symbol
Value
Learning Rate(DDQN)
α
0.001
Initial Exploration Rate(DDQN)
ϵ
1.0
Exploration Decay Rate(DDQN)
ϵdecay
0.998
Learning Rate (Transfer)
αtransfer
0.0002
Initial Exploration Rate (Transfer)
ϵtransfer
0.5
Exploration Decay Rate (Transfer)
ϵdecay, transfer
0.995
Arrive Target for Env1
qF 1
1000,900
Arrive Target for Env2
qF 2
1250,1300
Discount Factor
γ
0.95
Weighting Factor for Distance length
k1
0.8
Weighting Factor for Outage Penalty
k2
1
Step Penalty
Rn
1
Reward for Reaching Target
Rarrive
2000
Max steps per eposode
steps
200
SINR Threshold for outage
φth
0 dB
UAV Height
h(u)
90 m
IV. RESULTS
The height of the BS on the horizontal plane ranges from 5
to 25 meters, reflecting typical real-world configurations. The
operational area for all maps is set to a size of 2 km×2 km with
a height limit of 100 meters. The maximum number of steps
per episode, representing the battery limitation, is set to 200
steps, with each step corresponding to a displacement of 10
meters. A UAV arriving within a 30 meters radius of the target
is considered to have successfully reached its destination.
The networks consist of 3 hidden layers with 64 units each,
using ReLU activation functions. The output layer has linear
activation corresponding to action values. The learning rate
in (9) was reduced to 0.0002 for fine-tuning, allowing for
more subtle weight adjustments in the later layers, thereby
refining the model’s policy without drastic deviations from its
pre-learned behaviors. Weighting factors for rewards (7) and
more training parameters can be found in Table I.
The agent’s performance improved over time, as indicated
by an increase in total reward and a decrease in the number of
steps required to reach the target. The learning progress was
captured through two plots: total rewards, success rate over
episodes, and average level of communication. To demonstrate
this, we compared how well DQN and DDQN adapted to our
scenarios, choosing the one that performed better as our base
model for continuous learning.
In Fig. 2 we illustrate the comparative performance between
the DQN and DDQN models within the initial environment.
The DQN model exhibits greater volatility throughout the
training phase, with a 10-15% lower peak in average rewards
for the optimum policy compared to the DDQN. Addition-
ally, the DQN demonstrates less stable convergence by the
2000 episode, accompanied by increased variability. Thus, the
DDQN model emerges as a more suitable foundational model
for TL.
A. CTL in environment 2 with multi scenarios
This section shows the outcomes of TL in the second
environment, encompassing two scenarios. Scenario one, illus-
trated in Fig. 3, involves utilizing the DDQN model from the
first environment as the foundational model and has the same
mission destinations as DDQN. The result in Fig.4 shows a
more challenging scenario, which has different target positions
and one of the BS is not working.
0
200
400
600
800
1000
1200
1400
1600
1800
2000
Episode
22500
20000
17500
15000
12500
10000
7500
5000
2500
Average Reward
DDQN in ENV2 Total Reward
DDQN in ENV2 Moving Average (100 episodes)
Transfer from ENV1 to ENV2 Reward
Transfer from ENV1 to ENV2 Moving Average (100 episodes)
(a) Average rewards against episodes
0
200
400
600
800
1000
1200
1400
1600
1800
2000
Episode
0.0
0.2
0.4
0.6
0.8
1.0
Successful rate
DDQN in ENV2  Successful rate Moving Average (100 episodes)
Transfer from ENV1 to ENV2  Successful rate Moving Average (100 episodes)
(b) Success rate against episodes
Fig. 3: TL from ENV1 to ENV2 against retraining DDQN in ENV2
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 11:35:03 UTC from IEEE Xplore.  Restrictions apply.

## Page 6

0
200
400
600
800
1000
1200
1400
1600
1800
2000
Episode
25000
20000
15000
10000
5000
Average Reward
DDQN in ENV2 with emergency situation Total Reward
DDQN in ENV2 with emergency situation Moving Average (100 episodes)
Transfer from ENV1 to ENV2 with emergency situation Reward
Transfer from ENV1 to ENV2 with emergency situation  Moving Average (100 episodes)
(a) Average rewards against episodes
0
200
400
600
800
1000
1200
1400
1600
1800
2000
Episode
0.0
0.2
0.4
0.6
0.8
1.0
Successful rate
Successful rate of DDQN in ENV2 with emergency situation
Successful rate of Transfer from ENV1 to ENV2 with emergency situatio
(b) Success rate against episodes
Fig. 4: TL from ENV1 to ENV2 with emergency scenario against
retraining DDQN in ENV2
Fig.3a demonstrates the role of TL by showing the average
rewards of the training, showcasing an earlier and more stable
convergence compared to the DDQN model trained from
scratch. The duration to achieve stable optimal rewards is
shortened by 600–700 episodes, underscoring the efficiency
of TL in accelerating performance and stability. The success
rate of reaching the destination during training also notably
underscores the efficiency of TL. As shown in Fig.3b, the
success rate stabilizes at least 99% over 250 episodes sooner
than the scratch-trained model, which means that the model
prioritizes finding the policy that reaches the destination and
then adapts the relevant policy for the communication much
faster, and this process for DDQN is much slower.
In navigating the challenges of training in a environment
where a base station BS was no longer functional and the
target position was further away, the UAV demonstrated com-
mendable adaptability. Fig.4a illustrates the average rewards
of TL, and Fig.4b shows the success rate in Environment 2
where, despite facing significant challenges, TL demonstrates
its effectiveness by converging 300 episodes earlier in terms of
average reward and 200 episodes earlier in reaching the target
than the model trained from scratch. This scenario limited the
CTL approach from fully exploiting all initial strategies as
compared to a model beginning from scratch. It shows slight
fluctuations during the training phase, these did not hinder the
overall process convergence, which showcases the robustness
of the UAV’s learning capabilities. The observed variations,
partly due to the task’s target location moving further away,
marginally slowed the learning speed but did not detract
from the UAV’s ability to readjust and progress. Therefore,
the performance of CTL is expected and acceptable when
faced with more challenging scenarios and altered tasks. The
CTL efficiently navigated these complexities, underlining the
effectiveness of its adaptive learning framework in dynamic
environments.
B. CTL in environment 3 more differences
0
200
400
600
800
1000
1200
1400
1600
1800
2000
Episode
25000
20000
15000
10000
5000
Average Reward
DDQN in ENV3 Total Reward
DDQN in ENV3 Moving Average (100 episodes)
Transfer from ENV1 to ENV3 Reward
Transfer from ENV1 to ENV3 Moving Average (100 episodes)
(a) Average rewards against episodes
0
200
400
600
800
1000
1200
1400
1600
1800
2000
Episode
0.0
0.2
0.4
0.6
0.8
1.0
Successful rate
Successful rate of DDQN in ENV3 Moving Average
Transfer from ENV1 to ENV3 Successful rate Moving Average
(b) Success rate against episodes
Fig. 5: TL from ENV1 to ENV3 against retraining DDQN in ENV3
In the third environment (Fig.5), the role is to test the po-
tential for CTL. We designed the third environment to be very
different from the environment used for the base model. This
includes the distribution of buildings, height, size, number
of BS locations, and changes in the target destination. The
CTL still demonstrates strong capabilities; the convergence
was 200 episodes faster and reached a stable success rate 150
episodes earlier. However, more fluctuations were encountered
later on, which is predictable for reasons similar to those
discussed in Environment 2, as not all environments were
explored completely. This serves as an effective illustration
of the capabilities of continuous learning to expedite model
training outcomes, even when faced with environments that
present significant disparities.
V. CONCLUSION
In conclusion, the performance of CTL across two distinct
environments demonstrated its effectiveness in accelerating
learning and achieving higher success rates compared to
training DDQN models from scratch. For transfer to similar
environments, TL showcased a notable advantage in terms
of stability and early convergence, with the second case
highlighting its capacity to adapt to more complex tasks and
scenarios, albeit with reduced efficiency and some late-stage
fluctuations. The third environment, significantly divergent
from the initial training context, further tested the limits of
CTL, where, despite faster convergence and commendable
performance, the model faced increased fluctuations due to in-
complete exploration of the new environment. These findings
underscore the potential of TL to enhance model adaptability
and efficiency, particularly in dynamically changing or pro-
gressively complex scenarios, while also pointing to the need
for strategies to mitigate late-stage performance variability. In
our future works we plan to investigate this issue and work
on strategies that deal with this performance variability, and
more in-depth study of energy conservation strategies.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 11:35:03 UTC from IEEE Xplore.  Restrictions apply.

## Page 7

ACKNOWLEDGMENT
This work was supported by Engineering and Physical Sciences Research
Council United Kingdom (EPSRC), Impact Acceleration Accounts (IAA),
Green Secure and Privacy Aware Wireless Networks for Sustainable Future
Connected and Autonomous Systems, under Grant EP/X525856/1.
REFERENCES
[1] J. Won, D.-Y. Kim, Y.-I. Park, and J.-W. Lee, “A survey on UAV
placement and trajectory optimization in communication networks:
From the perspective of air-to-ground channel models,” ICT Express,
2022.
[2] P. S. Bithas, E. T. Michailidis, N. Nomikos, D. Vouyioukas, and A. G.
Kanatas, “A survey on machine-learning techniques for UAV-based
communications,” Sensors, vol. 19, no. 23, p. 5170, 2019.
[3] C. Sun, G. Fontanesi, B. Canberk, A. Mohajerzadeh, S. Chatzinotas,
D. Graces, and H. Ahmadi, “Advancing uav communications: A com-
prehensive survey of cutting-edge machine learning techniques,” IEEE
Open Journal of Vehicular Technology, pp. 1–31, 2024.
[4] S. Yin, S. Zhao, Y. Zhao, and F. R. Yu, “Intelligent trajectory design
in UAV-aided communications with reinforcement learning,” IEEE
Transactions on Vehicular Technology, vol. 68, no. 8, pp. 8227–8231,
2019.
[5] J. Moon, S. Papaioannou, C. Laoudias, P. Kolios, and S. Kim, “Deep
reinforcement learning multi-UAV trajectory control for target tracking,”
IEEE Internet of Things Journal, vol. 8, no. 20, pp. 15 441–15 455, 2021.
[6] B. Zhu, E. Bedeer, H. H. Nguyen, R. Barton, and J. Henry, “UAV
trajectory planning in wireless sensor networks for energy consumption
minimization by deep reinforcement learning,” IEEE Transactions on
Vehicular Technology, vol. 70, no. 9, pp. 9540–9554, 2021.
[7] R. Ding, F. Gao, and X. S. Shen, “3D UAV trajectory design and fre-
quency band allocation for energy-efficient and fair communication: A
deep reinforcement learning approach,” IEEE Transactions on Wireless
Communications, vol. 19, no. 12, pp. 7796–7809, 2020.
[8] G. Fontanesi, A. Zhu, and H. Ahmadi, “Deep reinforcement learning
for dynamic band switch in cellular-connected uav,” in 2021 IEEE 94th
Vehicular Technology Conference (VTC2021-Fall), 2021, pp. 1–5.
[9] H. Yang, J. Zhang, S. Song, and K. B. Lataief, “Connectivity-aware
uav path planning with aerial coverage maps,” in 2019 IEEE Wireless
Communications and Networking Conference (WCNC).
IEEE, 2019,
pp. 1–6.
[10] Z. Chen, X. Liang, and M. Zheng, “Knowledge transfer between
different UAVs for trajectory tracking,” IEEE Robotics and Automation
Letters, vol. 5, no. 3, pp. 4939–4946, 2020.
[11] G. Fontanesi, A. Zhu, M. Arvaneh, and H. Ahmadi, “A transfer learning
approach for UAV path design with connectivity outage constraint,”
IEEE Internet of Things Journal, vol. 10, no. 6, pp. 4998–5012, 2022.
[12] X. Zhang, G. Zheng, and S. Lambotharan, “Trajectory design for UAV-
assisted emergency communications: A transfer learning approach,” in
GLOBECOM 2020-2020 IEEE Global Communications Conference.
IEEE, 2020, pp. 1–6.
[13] G. Fontanesi, A. Zhu, and H. Ahmadi, “Outage analysis for millimeter-
wave fronthaul link of UAV-aided wireless networks,” IEEE Access,
vol. 8, pp. 111 693–111 706, 2020.
[14] B. Mondal, T. A. Thomas, E. Visotsky, F. W. Vook, A. Ghosh, Y.-H.
Nam, Y. Li, J. Zhang, M. Zhang, Q. Luo et al., “3D channel model
in 3GPP,” IEEE Communications Magazine, vol. 53, no. 3, pp. 16–23,
2015.
[15] M. Rebato, L. Resteghini, C. Mazzucco, and M. Zorzi, “Study of
realistic antenna patterns in 5G mmwave cellular scenarios,” in 2018
IEEE International Conference on Communications (ICC). IEEE, 2018,
pp. 1–6.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 04,2026 at 11:35:03 UTC from IEEE Xplore.  Restrictions apply.
