# UAV Formation Flight Control Method Based on DQN.pdf

## Page 1

ARTICLE IN PRESS
Article in Press
UAV formation flight control method based on 
DQN
Discover Applied Sciences
Received: 16 October 2025
Accepted: 5 March 2026
Cite this article as: He Z. UAV formation 
flight control method based on DQN. 
Discov Appl Sci (2026). https://doi.
org/10.1007/s42452-026-08547-8
Zhenqi He
We are providing an unedited version of this manuscript to give early access to its 
findings. Before final publication, the manuscript will undergo further editing. Please 
note there may be errors present which affect the content, and all legal disclaimers 
apply.
If this paper is publishing under a Transparent Peer Review model then Peer 
Review reports will publish with the final article.
https://doi.org/10.1007/s42452-026-08547-8
© The Author(s) 2026. Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International 
License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit 
to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do 
not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this 
article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the 
article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain 
permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/.

## Page 2

UAV Formation Flight Control Method Based on DQN 
 
Zhenqi He1* 
1School of Artificial Intelligence, Xi'an Aeronautical Polytechnic Institute, Xi’an 710087, Shaanxi, China  
Corresponding Author’s Email: hq774@mail.nwpu.edu.cn 
 
Abstract: Currently, unmanned aerial vehicle (UAV) formation flight control still relies on model - based 
information, and the level of UAV intelligent control is relatively low. To address this issue, a deep reinforcement 
learning approach is investigated.Firstly, corresponding reinforcement learning elements are devised for 
formation control problems, and formation controllers based on the deep reinforcement learning Deep Q-Network 
(DQN) algorithm are designed. Simultaneously, a method integrating a priority strategy with a multi - layer action 
library is proposed to accelerate the algorithm convergence and enable the wingman to ultimately maintain the 
expected range.Finally, the designed controller is compared with the Proportional - Integral - Derivative (PID) 
controller through simulation, and the effectiveness of the DQN controller is verified. The simulation results 
indicate that the controller can be applied to UAV formation, enhance the intelligence of the wingman, maintain 
the expected distance through autonomous learning, and the controller design does not require accurate model 
information, which provides a basis and reference for the intelligent control of UAV formation.  
Keywords: formation flying; reinforcement learning; intelligent control; DQN 
 
Article Highlights:  
 
Integrates DQN with UAV dynamics to create a specialized structure for formation control.    
 
PyTorch-based simulation with tensor computing accelerates training, enabling rapid iteration and 
optimization of control strategies.    
 
Comparative analysis shows DQN outperforms PID and DDPG in accuracy and stability, making it ideal for 
UAV formation control.  
 
1. Introduction 
UAVs have been extensively utilized in military and civilian domains owing to their numerous characteristics, 
including light weight, low cost, and excellent concealment. On the basis of individual UAVs, UAV formation 
flying has significantly broadened the scope of UAV applications. This has emerged as the development trend of 
UAV technology in recent years and has been widely recognized by countries around the world.As the 
requirements of various military and civilian missions continue to increase and the complexity of these missions 
grows, the performance of a single UAV has become insufficient to meet both civilian and military needs. Through 
the study of swarm phenomena in organisms such as ants and bees, researchers have discovered that the 
cooperative behavior of biological colonies exhibits superior performance in a variety of complex tasks. By 
applying this concept of swarm intelligence to UAVs, the formation control technology of UAVs has been 
developed.In recent decades, the formation control technology of UAVs has been successfully implemented in 
various military and civilian missions. Consequently, the formation control technology of UAVs has become a 
research focus. [1]. 
Currently, substantial achievements have been attained in the formation control technology of unmanned 
aerial vehicles. The primary formation control structures in the existing literature encompass the navigator - 
following method, the virtual structure method, the behavior - based method, the graph - theory - based method, 
and the consistency theory [2-6]. Among these, the navigator - following method is the most prevalently employed 
approach at present, owing to its merits of structural stability and ease of implementation.Regarding control 
methods, domestic and foreign scholars have also applied PID and backstepping control to formation control and 
achieved corresponding outcomes[7]. The design of the PID controller is straightforward and does not necessitate 
model information; however, issues such as parameter adjustment still persist. Backstepping, as a classical 
nonlinear control method, yields favorable results in formation control. Nevertheless, it typically demands 
accurate models for controller design, which is challenging in practical applications. Simultaneously, these 
controllers lack sufficient intelligence to meet the current requirements of intelligent mission execution; hence, 
novel control methods need to be developed.  
Reinforcement learning (RL), a sub - field of machine learning, has witnessed rapid development in recent 
years and has been extensively applied in game theory, optimal scheduling, and robot control. Its fundamental 
principle is that when a task conforms to the Markovian Decision Process (MDP), the training agent aims to 
maximize the reward through interaction with the environment, ultimately learning the optimal strategy. The merit 
of this approach lies in its ability to autonomously learn the best strategy without prior knowledge of the exact 
model of the environment.Currently, the reinforcement learning method has been utilized in the domain of UAV 
control, such as path planning, collaborative decision - making, and single - machine control[7-8]. It has also been 
applied to the formation control of UAVs[9]. A Q-learning algorithm with a dynamically changing learning rate 
has been designed to achieve the clustering of fixed - wing UAVs in a random environment. Some literature takes 
ACCEPTED MANUSCRIPT
ARTICLE IN PRESS
ARTICLE IN PRESS

## Page 3

three UAVs as an example and uses the DDPG algorithm to implement clustering for navigation. A CACER 
algorithm based on the Actor - critic framework has been proposed to address the leader - wingman aggregation 
problem in a continuous state[9-10]. Certain literature employs the Q-Learning approach, enabling wingmen to 
learn to aggregate within a specific distance from a lead aircraft in a static random environment. Some literature 
has proposed a cluster reinforcement learning method to group UAVs into the desired formations at target 
points[11-13].  
Notable advancements have been achieved in both theoretical investigations and practical implementations 
of UAV formation control technology. Nevertheless, certain challenges and limitations persist and necessitate 
resolution.Firstly, extant formation control approaches frequently rely on accurate models or simplified 
suppositions, which may not be valid in intricate and dynamic settings. This restricts their adaptability and 
robustness in real - world situations. Secondly, current research predominantly centers on the formation control 
of a small number of UAVs, and the scalability of these methods for large - scale UAV formations remains a 
crucial concern. As the quantity of UAVs in the formation rises, the complexity of control problems escalates 
exponentially, rendering it arduous to attain stable and efficient formation control. Thirdly, the intelligence 
quotient of existing formation control methods is still relatively low. Therefore, the DQN, as an advanced 
approach integrating deep learning and reinforcement learning, possesses potent self - learning and decision - 
making capabilities. It can approximate the Q-function via deep neural networks to manage high-dimensional 
state spaces without depending on accurate environmental models. In UAV formation control, DQN empowers 
each UAV to function as an intelligent agent, continuously learning the optimal control strategy through 
interaction with the environment, so as to achieve stable flight of the formation, task coordination, and respond to 
diverse complex environments and emergencies. The incorporation of DQN is anticipated to substantially enhance 
the adaptability, robustness, and intelligence level of UAV formation control, offering more reliable technical 
support for the application of UAVs in complex tasks.  
 
2. Description of UAV Formation Control Problems 
During formation flight, relative motion exists between any two UAVs. The formation mode considered in 
this paper is the "leader-wingman" mode. Thus, the mathematical model of multiple UAV formations can be 
derived by analyzing UAVs in two - unit formations. This section takes two UAVs in formation flight as an 
example. The experimental coordinate system of the UAV is selected as the reference frame for research, with the 
leader and the wingman as the specific cases. Assuming that the track azimuth of the UAV is approximately 
equivalent to the heading angle, in all subsequent discussions, they are regarded as equal. That is, the heading 
angle can be used instead of the track azimuth in expressions. The relative motion of the two UAVs is presented 
in Figure 1.  
Y
X
V2
V1
r1
R12
r2
yr
O
xr
v2
v1
θ2
θ1
θ2
 
Figure. 1 Schematic diagram of relative motion of UAVs 
According to literature, the equations of relative motion for UAV formation flight are as follows: 






)
,
(
     
sin
    
cos
ic
i
i
i
i
i
i
f
v
Y
v
X








                                                           (1) 
Where: 
1
, 
2
 --Heading angle (track azimuth) of UAVs 
1V and 
2V ;  
1
, 
2
--Speed Scales for UAVs 
1V and 
2V ; 
12
R
--Relative position vector of UAVs 
1V and 
2V ;  
1r , 
2r --Position vector of UAVs 
1V  and 
2V  in the ground coordinate system. 
The objective of this study was to enable a wingman to maintain a consistent speed at varying altitudes while 
taking into account the formation distance in the y - direction. Moreover, the wingman should be capable of 
maintaining the desired formation distance by learning to adjust its own heading angle, as depicted in Figure 1. 
To attain the aforementioned objectives, the currently prevalent design methods for formation controllers 
frequently rely on model - based design. However, in practical scenarios, the modeling process is influenced by 
ACCEPTED MANUSCRIPT
ARTICLE IN PRESS
ARTICLE IN PRESS

## Page 4

numerous factors. Simultaneously, UAVs exhibit relatively low intelligence and lack autonomous learning 
capabilities. Therefore, reinforcement learning is employed to address this issue.  
 
3. Design of Formation Controller Based on DQN 
3.1 Reinforcement learning and DQN algorithm 
Figure 2 depicts a theoretical model of reinforcement learning. It is assumed that there exists an individual 
within the environment capable of implementing action strategies, referred to as an agent. At time t, the agent 
perceives the state information
ts  of the current environment and generates the action at via the policy. The agent 
executes an action to act upon the environment and transitions to a new state
1

ts
. Simultaneously, it receives the 
reward signal 
)
,
(
t
t a
s
r
fed back by the environment, thereby initiating a new cycle. Agents amass experience, 
modulate strategies, and ultimately acquire the optimal action strategy via continuous interactive trial - and - error 
with the environment, aiming to attain the maximum cumulative reward upon task completion.  
Agent
Environment
Agent
Reward r(st,at)
New State St+1
State St
Action at
 
Figure. 2 Theoretical Framework for Reinforcement Learning 
 
Deep Q-Network (DQN) employs a deep neural network to approximate the Q-value function, taking states 
as the input and the output corresponding to the Q-value of each action. Let the parameter of the neural network 
be θ; then, the Q-valued function can be represented as
)
;
,
(
Q

a
s
. Network parameters are optimized through 
the minimization of the loss function, which is defined as the mean square error between the predicted Q-value 
and the target Q-value:  
]
))
;
,
(
Q
-
[(y
E
)
L(
2
i
D
~
)
s
r,
,
(s,



a
s


                                                  (2) 
Where: the target Q value 
ty  is calculated as: 
)
;
,
(
max
y
1
t










s
Q
r
a
t
                                                        (3) 
Where:  is the discount coefficient θ− is the parameter of the target network, copied periodically from the 
policy network. 
 
3.2 Design of key elements 
The intelligent agent engages in interaction with the environment to ultimately acquire the optimal strategy. 
The environment is composed of state space, action space, and reward function. In this section, the key elements 
in the interaction process of the formation control problem are designed sequentially.  
State space: Based on the aforementioned relative kinematic model of the drone, it is evident that the distance 
in the y-direction and the relative heading angle between the leader and the wingman can be transmitted via a 
communication link. This information can serve as the state space. The state space S is defined as: 
ACCEPTED MANUSCRIPT
ARTICLE IN PRESS
ARTICLE IN PRESS

## Page 5


























F
y
y
y
s
e
s
e
s
e
•s
y
•s
e
•s
e
•s
e
•s
s




8
7
6
5
4
3
2
1


                                                                          (4) 
 
Where: 
F
L
e





 represents the relative heading angle between the leader and the follower; 
y
y
e
d
y


 denotes the error between the desired y-direction distance and the actual y-direction distance; 
y_d represents the desired y-direction distance. Based on the PID control concept, the integral and differential 
terms of 
y
e  and 
e  are incorporated into the state space, enabling the formation controller to better learn the 
strategy. 
Hierarchical action space: In the process of formation flight, the wingman sustains the desired distance in the 
y - direction through the adjustment of the heading angle. Consequently, the action space is defined as the desired 
heading angle command of the wingman. The action is updated by the controller after each sampling, and the 
command remains invariant during the sampling period. Given that the employed DQN is a discrete algorithm, 
the desired command necessitates discretization. With regard to control accuracy, the hierarchical heading angle 
action library is designed as follows: 
 
]
20
,
10
,
0,
10
,
20
[
max
max
1








action
                                            (5) 
]
10
2,
1,
0,
1
,
2
10
[
max
max
2








action
                                              (6) 
]
50
4
.
0,
2
.
0,
0,
2
.
0
,
4
.
0
50
[
max
max
3








action
                                       (7) 
In the formula, 
]
,
[
max
max 


 represents the range of heading angles, where <0 indicates that the drone 
is deviating to the left. i=1,2,3 denotes three different sets of actions, each with a different discrete interval. The 
purpose of designing different action sets is to enable the controller to select different action sets to output 
corresponding desired commands under different situations. For example, when the distance error is large, a larger 
action set with a larger spacing is selected to quickly reduce the distance error. When the distance error decreases, 
a smaller action set is selected for fine adjustment, which can effectively improve control accuracy. 
Reward Function: The formation control problem of unmanned aerial vehicles represents a typical sparse-
reward problem. In this context, the controlled entity encounters difficulties in obtaining rewards at the initial 
stage and necessitates a series of explorations and intricate operations to acquire them. Consequently, the design 
of the reward function is closely associated with the ultimate training outcomes. Simultaneously, the formation 
control problem diverges from other environments in that the intelligent agent does not halt upon attaining the 
maximum reward but persists in forward flight. The designed reward function should be as simplistic as feasible, 
which can empower the wingman to learn the optimal strategy while possessing strong transferability and low 
computational complexity. The designed reward function is: 





















   
          
otherwise
      
0
done
 
if
      
50
       
|
|
*
001
.
0
 
otherwise
      
0
 
0.1
|
| 
if
     
5
3
2
1
3
2
1
r
r
r
R
r
e
r
e
r
y
y
                                                      (8) 
In the formula: 
1r  is the reward, which is obtained when the distance error is reached; 
2r  is the punishment, 
and the size of the punishment depends on the distance. The larger the error, the greater the punishment, and vice 
ACCEPTED MANUSCRIPT
ARTICLE IN PRESS
ARTICLE IN PRESS

## Page 6

versa, the smaller it is, with a minimum of 0; 
3r  is the early stop penalty, which is obtained when the training 
process is stopped prematurely or unexpectedly; R  is the sum of all rewards and punishments obtained during 
the process. The value of 
1r  represents the ultimate control objective, while the functions of 
2r  and 
3r  are to 
guide the strategy towards obtaining rewards. The maximum penalty term of r3 is to avoid reaching the end 
condition as much as possible, while 
2
1
r
r 
 makes the final reward positive. 
Termination condition: In the training process, the validation duration for each round is Td. During the flight, 
if the distance in the y - direction is either excessively large or extremely small, it is unfavorable for formation 
flight. When the distance is overly large, it may augment communication complexity or even result in loss of 
contact. When the distance is too small, it may give rise to collisions. Consequently, the termination condition for 
the training process is established as follows: 




otherwise
      
          
          
0
T
T
 
or
 
y
y
 
 
y
y
 
if
    
1
d
max
min or
                                                   (9) 
Where： 
]
,y
[y
max
min
is the distance range set by the formation. 
 
3.3 Design of Formation Flight Controller 
The research aim of this section is to devise a formation controller founded on the Deep Q-Network (DQN) 
to generate the heading angle command for the wingman. This enables the wingman to autonomously acquire the 
ability to trail the leader and uphold the desired distance without any pre-existing knowledge. The control 
framework is presented in Figure 3 below. In this figure, the drone formation comprises two wingmen, possessing 
identical state spaces, action spaces, and rewards as those formulated in the preceding section. 
The controller segment encompasses a Memory unit, a DQN network, and an action selection strategy 
component. The Memory unit serves to store data from the interaction process and conducts random sampling at 
fixed time intervals to extract batch samples for the purpose of updating the DQN network. The neural network 
architecture outputs all action values, and subsequent to this, the action selection strategy generates the wingman's 
heading command. The wingman reacts to this command, modifies the state of the leader, accomplishes the state 
update, and computes the current reward in accordance with Equation (8). The reward and state are then fed back 
to the controller jointly, thereby establishing a comprehensive formation control structure.  
Menory
DQN
Action 
selection 
strategy
Ground 
station of 
UAV
Leader
Follower
Update batch 
samples
Rewards and Status
Heading angle 
command
 
Figure. 3 Control Structure of DQN Formation 
The pseudo code of the algorithm is shown in Table 1: 
Table. 1 Pseudo code Program of DQN 
Algorithm 1 Deep Q-learning with Experience Replay 
Initalize replay memory D to capacity N 
Initialize action-value function Q with random weights  
Initialize target action-value function Qˆ  with weights 



 
For episode=1,M do 
Initialize sequence 
}
{ 1
1
x
s 
 and preprocessed sequence
)
( 1
1
s


 
For t=1,T do 
With probability select a random action 
ta  
Otherwise select 
)
;
),
(
(
max
arg


a
s
Q
a
t
a
t 
 
Execute action 
t
a
 in emulator and observe reward 
tr  and image 
1

tx
 
ACCEPTED MANUSCRIPT
ARTICLE IN PRESS
ARTICLE IN PRESS

## Page 7

Set 
t
t
s
s

1
, 
ta , 
1

tx
 and preprocess 
)
(
1
1


t
t
s


 
Store transition
)
,
,
,
(
1

t
t
t
t
r
a


 in D 
Sample random minibatch of transitions
)
,
,
,
(
1

j
j
j
j
r
a


 from D 
Set 










otherwise
        
)
;
,
(
ˆ
max
1
j 
step
at 
 s
 terminate
episode
 
if
     
1



a
Q
r
r
y
j
a
j
j
j
 
Perform a gradient descent step on 
2
))
;
,
(
(


j
j
j
a
Q
y 
 with respect to the network parameters  
Every C steps reset 
Q
Q 
ˆ
 
End for 
End for 
 
3.4 Priority selection strategy 
The commonly used action selection strategy in current reinforcement learning algorithms is the 
greedy


 strategy, which randomly selects and explores actions with a probability of  when outputting 
actions through an action network, and selects the action with the highest Q value based on the action value 
function with a probability of 


1
. This random strategy can effectively learn the optimal strategy in simple 
environments, but in sparse reward environments such as formation control, it is difficult to obtain rewards 
through random strategies. At the same time, the algorithm converges slowly under random strategies, which does 
not meet the practical requirements of formation control. Therefore, a priority strategy is proposed, which is 
combined with the layered action space designed in the previous section, that is, wingmen prioritize certain actions 
based on observation states. The specific approach is to select the action library 
i
action  based on the current 
observed state values, and the most important factor in this environment is the error between the y-direction and 
the expected distance. When the distance is far, choose the action library with a larger interval, and when the 
distance is close, choose the action library with a smaller interval. Then, prioritize the selection based on the 
probability of . When the position of the wingman is observed to be left, prioritize the right deviation action, 
i.e. 
0


, and vice versa. To accelerate algorithm convergence and learn the optimal strategy quickly. 
 
4. Simulation verification based on PyTorch 
 
4.1 Parameter Settings 
The system employed Pytorch to construct a simulation environment for verification purposes. The DQN 
neural network utilized a three-layer convolutional neural network, where the activation function of each layer 
was the Relu function, and the optimization function was updated via the Adam algorithm. The remaining 
hyperparameters in the simulation program are presented in Table 2, encompassing parameters such as the 
iteration count and the learning rate.  
 
Table. 2 Other parameter settings 
parameter 
value 
parameter 
value 
i
epi  
10000 
Maxstep 
200 
max

 
180 
M
1e-6 
batchsize 
128 

0.95 
 
1
.
0
1 
 
 
0.9 
 
0.0001 
)
,
,
(
3
2
1



 
1 
)
,
(
2
1 

 
50 
3

 
20 
a


 
0.919 
b


 
0.919 
ACCEPTED MANUSCRIPT
ARTICLE IN PRESS
ARTICLE IN PRESS

## Page 8

In Table 2, 
i
epi  is the number of iterations; Maxstep is the maximum number of steps, which is the 
maximum number of iterations in a single training/optimization process. Once this value is reached, the current 
task is stopped; 
max

is the maximum threshold used to control the range of feature values or the upper limit 
of activation function output (such as the cutoff value of  ReLU); batchsizeis the batch size; ε is the attenuation 
factor, representing the attenuation coefficient of the weight, gradually decreasing from 1 to 0.1 to achieve 
dynamic adjustment;  is penalty coefficient used as a penalty term in the loss function to control the impact of 
outliers or noise; (μ₁, μ₂) and 
3

are the mean parameter, corresponding to the initialization of multimodal data 
or multi class features; is the learning rate;  is the smoothing coefficient used for momentum optimization; 
)
,
,
(
3
2
1



  is the set of distributed parameters; 
a


and 
b


are weight parameters. 
4.2 Simulation verification results 
Figure 4 depicts the average loss curve acquired during the training procedure of heading angle control via a 
Deep Q-Network (DQN) algorithm. From a holistic viewpoint, the curve exhibits a distinct downward tendency, 
mirroring the model's learning advancement over time. In the initial stage of training, when the iteration number 
is relatively small, the average loss stays at a high level, nearly attaining 0.175. This implies that at the onset of 
the learning process, the model's predictions deviate significantly from the actual values, leading to a large error 
signal and sub - optimal policy performance. 
As the training progresses and the iteration number rises, the average loss value decreases rapidly. By the 
time the iteration count nears 50, the average loss has already dropped below 0.025. This steep decline suggests 
that the model is effectively learning from interactions with the environment, gradually optimizing its decision - 
making strategy, and enhancing prediction precision. The substantial reduction in loss during this phase 
underscores the convergence ability of the DQN algorithm in this control task. 
In the subsequent phase, from approximately 50 to 700 iterations, the average loss value stabilizes at a low 
level with only minor oscillations. Although slight variations exist, the overall trend remains stable, indicating 
that the model has reached a relatively stable performance state. During this period, the algorithm continues to 
conduct fine - tuning, yet no significant further improvement or deterioration is observed. This stabilization 
implies that the model has converged towards an effective policy, and additional training does not result in 
substantial alterations in loss, demonstrating the robustness and suitability of the DQN approach for this particular 
control problem. 
This graph visually illustrates the fluctuation of the model's average loss value as the number of iterations 
increases during the training procedure of heading angle control via DQN. This phenomenon reflects the 
progression of the model from the initial learning phase to a state of gradual convergence and stable performance.  
 
 
 
Figure. 4 Average loss curve in heading angle control training using the DQN 
In the figure5, as the number of iterations approaches zero, the reward value rapidly declines to 
approximately -1750. Commencing from around 20 iterations, the reward value experiences a rapid increase and 
stabilizes at approximately 100 iterations, remaining at a level close to zero. At nearly 700 iterations, a slight 
decrease in the reward value is observed. Figure 5 illustrates the variation of the total reward value with the number 
ACCEPTED MANUSCRIPT
ARTICLE IN PRESS
ARTICLE IN PRESS

## Page 9

of iterations during DQN-based control training, which reflects the learning and convergence processes during 
training.  
The substantial upsurge commencing at approximately 20 iterations indicates that the DQN algorithm 
commences to acquire valuable patterns from the environment. It initiates the adjustment of control parameters in 
a manner that yields superior performance and consequently higher rewards. The stabilization of the reward value 
at around 100 iterations suggests that the algorithm has converged to a relatively stable control strategy. At this 
juncture, the system has learned a set of actions capable of sustaining a near - zero reward, which may signify an 
efficient and balanced operational state. 
The marginal decline at nearly 700 iterations can be attributed to diverse factors. It is possible that the 
environment has undergone a minor alteration, or the algorithm has reached a local optimum and is beginning to 
explore other regions of the solution space. This slight decrease in the reward value might serve as an indication 
of the necessity to further optimize the training process, potentially through the adjustment of the learning rate or 
the exploration rate of the DQN algorithm.  
 
Figure. 5 Total reward curve within control training founded on DQN 
 
As depicted in Figure 6, it is observable that under the control of the DQN, the yaw angle swiftly adjusts 
from the initial -80 degrees to 0 degrees and maintains stability subsequently. Figure 7 illustrates the rapid increase 
of the yaw angle from the initial -75 degrees to approximately 75 degrees under DQN control, followed by a 
process of stability maintenance. The DQN controllers in Figure 6 and Figure 7 can expeditiously and effectively 
adjust the yaw angle to the target value while ensuring the system's stability. 
In addition to the adjustment of the yaw angle, the simulation also reveals the performance of other 
parameters under the control of the Deep Q-Network (DQN). For example, the rotational speed of the equipment 
exhibits a stable and predictable pattern. During the adjustment of the yaw angle, the rotational speed gradually 
rises from the initial value and subsequently stabilizes at an appropriate level. This suggests that the DQN 
controller is not only capable of handling the yaw angle adjustment but also coordinating with other parameters 
to guarantee the overall stability and efficiency of the system. 
Overall, the simulation verification results illustrate the outstanding performance of the DQN controller in 
adjusting the yaw angle and coordinating other system parameters. It can ensure the stability and efficiency of the 
system while adapting effectively to different initial conditions. These results offer robust support for the practical 
application of the DQN controller in relevant fields.  
 
Figure. 6 Yaw angle under the control of DQN: ranging from -80 degrees to 0 degrees 
ACCEPTED MANUSCRIPT
ARTICLE IN PRESS
ARTICLE IN PRESS

## Page 10

Figure. 7 Yaw angle under the control of DQN: ranges from -75 degrees to nearly 75 degrees.  
Figure 8 depicts the alterations in the generated control variables at diverse time points. Noticeably, 
significant fluctuations, including both sharp increases and decreases, are evident at multiple time points, which 
illustrates the temporal dynamic characteristics of the control variables. These variations might be associated with 
the experimental procedure.  
 
Figure. 8 Regulate the quantity produced 
 
As depicted in Figure 9, it is evident that as time approaches 0 seconds, the adjustment speed of the yaw 
angle gradually decelerates and converges towards a value of 0°/s. Precisely commencing from the 0 - second 
point, the speed experiences a rapid and significant upsurge, reaching its peak magnitude within an approximate 
time span of 2 to 3 seconds. During this initial acceleration stage, the speed exceeds 40°/s, signifying a highly 
dynamic reaction. After attaining this maximum value, the speed initiates a rapid decline and subsequently enters 
a phase of oscillations, with the speed fluctuating between 30°/s and 40°/s. As time progresses, these oscillations 
gradually attenuate, and the speed trends towards a more stable state. 
From 20 seconds to 40 seconds, the adjustment speed remains relatively constant, maintaining an average 
value of approximately 35°/s, with only minor and sporadic fluctuations discernible during this period. As the 
time nears the 50 - second mark, there are again slight variations in speed; however, the amplitude of these 
disturbances is relatively small, and the overall speed continues to remain stable at around 35°/s. 
Overall, Figure 9 visually portrays the dynamic temporal evolution of the yaw angle adjustment speed under 
DQN control, highlighting an initial phase characterized by intense and rapid changes that ultimately transitions 
into a more stable and consistent behavioral pattern over the observed time frame.  
ACCEPTED MANUSCRIPT
ARTICLE IN PRESS
ARTICLE IN PRESS

## Page 11

Figure. 9 Yaw angle adjustment velocity under the control of DQN 
In the initial stage (approximately 0 - 5 seconds), the reward value in Figure 10 demonstrated notable 
fluctuations. The value initially ascended rapidly to a relatively high level near - 75, and subsequently declined 
swiftly to a lower level close to - 200. This phenomenon might imply that during the early operation of the system, 
the agent was in a state of exploration and environmental adaptation, and its decision - making behavior had not 
yet established stable patterns, leading to substantial fluctuations in the reward value. 
In the intermediate stage (approximately 5 - 10 seconds), the reward value underwent a short - term rebound 
subsequent to its initial decline, accompanied by a certain degree of fluctuation. These fluctuations could reflect 
the system's attempts to explore diverse strategies or actions in pursuit of a more optimal decision - making path. 
As a result, despite the overall adjustment period, the reward value still manifested a certain level of instability at 
specific moments. 
In the stabilization stage (approximately 10 - 50 seconds), the reward value gradually stabilized and remained 
at a relatively low level, fluctuating around - 225. This indicates that after the initial exploration and learning 
phase, the DQN control strategy has attained a relatively stable state. The system's decision - making behavior 
becomes consistent, and the reward value no longer exhibits significant fluctuations, suggesting that the agent has 
converged to a relatively optimal strategy to a certain extent.  
 
Figure. 10 Reward Variation Curve under DQN Control 
 
Overall, under the control of the DQN, the reward value undergoes significant fluctuations initially and then 
gradually stabilizes over time. This phenomenon reflects the transition of the DQN algorithm within the system 
from the exploration phase to the relatively stable strategy execution phase.  
The Figure 11 shows the trajectory comparison of the Leader Follower Formation. The horizontal axis of the 
chart represents control time, and the vertical axis represents distance error. In Figure 11, a comparison was made 
between the PID control method, DDPG control method, and DQN control method in terms of the performance 
of followers during the leader following process. These three control methods enable followers to roughly track 
the leader's path. However, at a specific stage, followers using DQN control method exhibit tracking performance 
closer to that of the leader, indicating its advantage in path following. 
In the comparison of PID control approaches, the DQN control approach exhibits greater adaptability and 
precision when addressing complex paths and dynamic variations. Although the PID control approach is 
straightforward and easy to implement, its performance is frequently restricted when dealing with nonlinear and 
ACCEPTED MANUSCRIPT
ARTICLE IN PRESS
ARTICLE IN PRESS

## Page 12

time-varying systems. Conversely, the DQN control approach can automatically learn and optimize control 
strategies via deep learning and reinforcement learning techniques, thereby attaining more accurate path tracking 
in complex environments. In the comparison with DDPG, the DQN effectively mitigates training instability and 
overestimation issues through techniques such as Experience Replay and Target Network, demonstrating 
favorable convergence and stability. It can handle high-dimensional state spaces, and the training process is 
relatively controllable. In contrast, although DDPG performs remarkably well in continuous action spaces, the 
simplicity and maturity of  DQN render it a more efficient option in discrete action scenarios. It should be noted 
that for DQN, although discrete actions may lead to control jitter, a hierarchical action space can effectively 
mitigate this issue. The advantages of choosing DQN are training stability and algorithm simplicity. The DQN 
architecture is more lightweight than RL algorithms such as DDPG, with lower memory consumption and latency 
in embedded unmanned aerial vehicle systems. For the formation flight control of unmanned aerial vehicles, the 
DQN algorithm is sufficient to meet the formation control requirements of unmanned aerial vehicles. 
In conclusion, the DQN control method has exhibited substantial advantages in the path tracking task of the 
Leader - Follower Formation. Its robust learning capability and adaptability empower it to attain more precise and 
stable path tracking in intricate environments, offering robust support for practical applications.  
 
 
Figure. 11 Leader-Follower Formation 
 
6. Conclusion 
In light of the limited intelligence level in drone formation flight and the high demand for model information 
in controller design, a formation controller based on DQN is devised. Via simulation experiments, it is ultimately 
demonstrated that precise model information is not requisite in the design of the DQN controller. Through training, 
the wingman can autonomously acquire the optimal strategy for following the leader, as well as tracking and 
maintaining the desired distance. By conducting a comparison with the PID control method, it is concluded that 
the DQN control method exhibits a swifter convergence speed and superior control efficacy.  
Moreover, the DQN based formation controller shows strong adaptability to different scenarios. It can 
effectively handle various complex situations during the drone formation flight, such as sudden changes in the 
leader's trajectory or environmental disturbances. This adaptability is mainly due to the self - learning ability of 
the DQN algorithm, which allows the controller to continuously adjust and optimize its strategy according to the 
actual situation. 
In addition, the research results also provide valuable insights for the further development of drone formation 
flight technology. The successful application of the DQN algorithm in this field opens up a new direction for the 
design of more intelligent and efficient formation controllers. Future research can focus on improving the 
performance of the DQN based controller in more extreme and dynamic environments, as well as exploring the 
combination of the DQN algorithm with other advanced technologies to further enhance the overall capabilities 
of drone formation flight systems. 
 
Data sharing agreement 
The datasets used and analyzed during the current study are available from the corresponding author on 
reasonable request. All relevant data are within the manuscript. All figures and tables are made by the author. 
 
ACCEPTED MANUSCRIPT
ARTICLE IN PRESS
ARTICLE IN PRESS

## Page 13

Declaration of Conflicting Interests 
The author declared no financial and non-financial conflicting interests. And the author declared no potential 
conflicts of interest with respect to the research, author-ship, and publication of this article.  
 
Acknowledgements 
UAV intelligent control technology innovation team (Gant: KJTD20-002), School level scien-tific research 
projects(Grant: 23XHZK-23), Project of Shaanxi Vocational and technical education society in 2022 (Gant: 
2022SZX096), School-level High-level Talent Research Startup Fund Project (Gant: 2024XHQDJ01). 
 
Ethical approval 
Not applicable  
 
Consent to participate 
Not applicable  
 
Consent to publish 
Not applicable  
 
Clinical trial number 
Not applicable. 
 
Author Contribution  
Zhenqi He contributed to the conception of the study, wrote the first draft of the manuscript and worked on 
the coding of tables and figures and approved the final manuscript. 
 
 
References 
[1] Cabral-Pacheco, EG; Villarreal-Reyes, S; Galaviz-Mosqueda, A, etc.(2019). Performance Analysis of Multi-
Hop Broadcast Protocols for Distributed UAV Formation Control Applications. IEEE ACCESS. 2019. 
7:113548-113577. DOI: 10.1109/ACCESS.2019.2935307. 
[2] Jin, YX; Song, TT;.  Dai, CJ. etc.(2024). Autonomous UAV Chasing with Monocular Vision: A Learning-
Based Approach. Aerospace. 2024.11(11). DOI: 10.3390/aerospace11110928. 
[3] Lu, J; Li, YY.(2024). Research on optimal deep learning-based formation flight positioning of UAV. 
CONCURRENCY AND COMPUTATION-PRACTICE & EXPERIENCE. 2024. 36(14). DOI: 
10.1002/cpe.8099. 
[4] Jiao, YK;  Fu, WX;  Cao, XY.etc.(2024) A Cooperative Decision-Making and Control Algorithm for UAV 
Formation Based on Non-Cooperative Game Theory. DRONES. 2024. 8(12). DOI: 10.3390/drones8120698. 
[5] Bai, TT; Bo, WD; Ali, ZA; Masroor, S. Formation control of multiple UAVs via pigeon inspired optimisation. 
INTERNATIONAL 
JOURNAL 
OF 
BIO-INSPIRED 
COMPUTATION. 
2022. 
19(3) 
:135-146. 
DOI:10.1504/IJBIC.2022.123106. 
[6] Li, P; Cao, J; Liang, DC.(2022). UAV-BS Formation Control Method Based on Loose Coupling Structure. 
IEEE ACCESS. 2022. 10: 88330-88339. DOI: 10.1109/ACCESS.2022.3197753. 
[7] Yang, YH; Xiong, XZ; Yan, YH.(2023). UAV Formation Trajectory Planning Algorithms: A Review. 
DRONES .2023. 7(1). DOI:10.3390/drones7010062. 
[8] Wang, JH; Ramirez-Mendoza, RA; Xu, Y.(2023). Nonlinear Direct Data-Driven Control for UAV Formation 
Flight System. JOURNAL OF SYSTEMS ENGINEERING AND ELECTRONICS. 2023. 34(6):1409–1418. 
DOI: 10.23919/JSEE.2023.000140. 
[9] Floriano, BRO; Borges, GA; Ferreira, HC; Ishihara, JY.(2021). Hybrid Dec-POMDP/PID Guidance System 
for Formation Flight of Multiple UAVs. JOURNAL OF INTELLIGENT & ROBOTIC SYSTEMS. 
2021.101(3). DOI: 10.1007/s10846-021-01342-0. 
[10] Huang, HJ; Yang, YC; Wang, H. etc.(2020). Deep Reinforcement Learning for UAV Navigation Through 
Massive MIMO Technique. IEEE TRANSACTIONS ON VEHICULAR TECHNOLOG. 2020. 69(1): 1117–
1121. DOI:10.1109/TVT.2019.2952549. 
[11] Chen, JM; Lv, S; Zhang, T. etc.(2025). The Semidouble DQN Resource Optimization Strategy for UAV-
Aided Networks: A Case Study. IEEE TRANSACTIONS ON AEROSPACE AND ELECTRONIC 
SYSTEMS. 2025. 61(3): 7852-7862. DOI: 10.1109/TAES.2025.3541168. 
[12] Zhenqi H.(2023). Research on UAV flight control and communication method based on fuzzy adaptive. 
2023. https://doi.org/10.1007/s11276-023-03408-3 
[13] Samma, H; El-Ferik, S.(2024). Autonomous UAV Visual Navigation Using an Improved Deep 
Reinforcement Learning. IEEE ACCESS. 2024. 12: 79967-79977. DOI: 10.1109/ACCESS.2024.3409780. 
ACCEPTED MANUSCRIPT
ARTICLE IN PRESS
ARTICLE IN PRESS
