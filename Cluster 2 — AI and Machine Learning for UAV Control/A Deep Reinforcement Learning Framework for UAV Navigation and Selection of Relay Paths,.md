# A Deep Reinforcement Learning Framework for UAV Navigation and Selection of Relay Paths,.pdf

## Page 1

Vol.:(0123456789)
Int. j. inf. tecnol. (December 2025) 17(9):5167–5173 
https://doi.org/10.1007/s41870-025-02729-0
ORIGINAL RESEARCH
A deep reinforcement learning framework for UAV navigation 
and selection of relay paths
Sumati1 · Nikhil Kumar Marriwala1   · 
Ram Avtar Jaswal2 
Received: 24 February 2025 / Accepted: 3 September 2025 / Published online: 13 September 2025 
© Bharati Vidyapeeth’s Institute of Computer Applications and Management 2025
Abstract  The given paper proposes a deep reinforcement 
learning framework for unmanned aerial vehicles (UAVs) 
navigation to provide optimal communication for the users. 
It comprises gated recurrent unit enhanced with graph atten-
tion mechanism to make effective use of inter-UAV commu-
nication network for enhanced data retrieval and decisions. 
To further improve exploration and robustness, the proposed 
framework is trained using maximum-entropy reinforcement 
learning, enabling UAVs to learn stochastic policies. A heu-
ristic reward function, solely based on local observations, is 
designed to optimize global performance in terms of cover-
age, fairness, and energy efficiency. Extensive simulations 
validate the effectiveness of the approach, showing superior 
scalability, adaptability, and communication efficiency over 
existing methods.
Keywords  UAVs · GAT​ · GRU​ · DRL · Optimization · 
Relay paths
1  Introduction
With the advancement of cutting-edge technologies such as 
on-board computing systems, sophisticated flight control 
frameworks, and Ad-hoc networks, managing large-scale, 
intelligent UAV swarms for complex operations is now 
possible. Currently, UAV swarms are being used in vari-
ous domains such as surveillance, logistics, infrastructure 
inspection, and disaster response. A significant application 
includes UAV-mounted mobile base stations which can be 
used to extend communication coverage and performance 
in areas with insufficient infrastructure. Mobile base sta-
tions have the advantage of rapid and flexible deployment, 
especially in emergencies such as natural disasters that cause 
disruption to cellular communication networks. In recent 
years, UAV’s have been recognized as cost-effective alterna-
tives that can deliver high-quality communication services. 
The communication is facilitated among the UAVs while it 
allows access to the ground users. The limitations such as 
short communication ranges and high mobility do not favour 
the use of the centralized control approach [1, 2]. Moreo-
ver, since obtaining full global data is usually infeasible in 
real-world applications, training samples collected are only 
information collected by individual UAVs and their imme-
diate neighbors. This is different from previous approaches, 
which utilize global data during training to stabilize model 
convergence [3, 4]. It is typically infeasible to obtain global 
information in real tasks; we assume that the training sam-
ples of the model only consist of the information from itself 
and its interconnected neighbors. In other words, the policy 
is trained with only local information yet should achieve 
high performance in terms of the global metric [5, 6]. The 
present work addresses partial observability through a fly-
ing Ad-hoc network, where links of interconnected UAVs 
within the given communication range are formed and 
 *	 Sumati 
	
sumatiengineer@gmail.com
	
Nikhil Kumar Marriwala 
	
nmarriwala@kuk.ac.in
	
Ram Avtar Jaswal 
	
ramavtar.jaswal@gmail.com
1	
Department of Electronics and Communication Engineering, 
University Institute of Engineering and Technology, 
Kurukshetra University, Kurukshetra, Haryana, India
2	
Department of Electrical Engineering, University Institute 
of Engineering and Technology, Kurukshetra University, 
Kurukshetra, Haryana, India

## Page 2

5168
	
Int. j. inf. tecnol. (December 2025) 17(9):5167–5173
used for low-latency communication. This communication 
strategy of neighbouring UAVs helps alleviate this partial 
observability at the most minimal cost thereby developing 
the concept of GRU and GAT.
1.1  Key contributions
•	 The given paper introduces a DRL framework to provide 
effective communication among UAV’s. It comprises 
GAT + GRU for spatial data extraction and a memory 
unit for data retention.
•	 Self-attention mechanism using GAT enables the learn-
ing of stochastic policies through the proposed model. In 
GAT, each UAV is represented as a node within a graph, 
with node embedding. These embedding are shared via 
edges between nodes, enabling each UAV to process both 
its own and neighbouring nodes’ information.
•	 This approach ensures that all UAV’s follow the same 
policy for decentralized path planning and control, utiliz-
ing ad-hoc network communication.
•	 Extensive simulations validate the effectiveness of heu-
ristic reward function. Additionally, this study examines 
various aspects of the proposed framework, including its 
performance, scalability, transferability, robustness, and 
interpretability.
1.2  Organization
The remainder of this paper is structured as follows: Sect. 2 
discusses related works. Section 3 outlines the system model 
and the proposed approach. Section 4 deals with the results. 
Finally, Sect. 5 concludes the study followed by references.
2  Related works
Recent research [7] has extensively explored UAV deploy-
ment to enhance its practicality in real-world applications. 
Some studies have proposed multi-UAV control models that 
optimize deployment coverage while maintaining energy 
efficiency. Approaches have also been proposed for reducing 
the deployment delay and total operational latency. Further-
more, architectures have been devised for optimal deploy-
ment and mobility of multiple UAVs, thereby making effi-
cient use of energy resources on the ground equipment. With 
the development of Ad-hoc networking, in which all nodes 
that fall within a certain distance can easily form contacts, 
researchers have aimed at multi-UAV control strategies that 
reasonably assume that UAVs can maintain communication 
with their neighbors without even slight delay. When oper-
ating a UAV swarm in unobserved environments with low 
observation levels, an efficient exploration strategy is vital. 
Among the most popular strategies is the greedy strategy [8], 
which encompasses elements of introducing random action 
selection to enhance exploration while refining the decision-
making process step by step. Several advanced methods 
have been proposed for multi-UAV cooperative exploration. 
These include game-theoretic frameworks for collaborative 
search and monitoring, cooperative strategies specifically 
designed for UAV hybrid systems to minimize exploration 
distance that reduces data exchange by sharing only essen-
tial frontier points [9]. Various multi-objective optimization 
algorithms have been introduced to assign UAV tasks and 
plan routes efficiently, incorporating genetic algorithms to 
minimize processing time. Such algorithms lack mathemati-
cal aspects like coverage, observation radius, velocity vector 
and favourable points based on number of vehicles. Other 
approaches rely on station-based information to determine 
optimal paths for leading UAVs. The station-based infor-
mation requires graphical validation which is not possible 
with existing approaches. Further, some researchers have 
applied mean-field game control theory to achieve precise 
positioning while reducing flight energy consumption [10]. 
More recent studies have adopted reinforcement learning-
based strategies to optimize UAV swarm navigation, using 
lightweight policies with minimal computational overhead. 
DRL-based models seek to control each UAV independently, 
leveraging advancements in multi-agent deep reinforcement 
learning [11]. This approach has been used to develop UAV 
controllers for formation control and small fixed-wing UAV 
flocking, incorporating parameter-sharing techniques to 
accelerate learning convergence. The parameters need to be 
evaluated based on communication range and observation 
radius. To address instability issues in multi-agent environ-
ments, researchers have introduced centralized-decentralized 
training where decentralized UAV policies are trained using 
a centralized critic network that has access to global state 
information [12]. This method has been applied to optimize 
UAV trajectories for secure communication and to improve 
the efficiency of information aggregation through self-atten-
tion mechanisms. Thus, in order to alleviate above issues, 
the proposed framework is designed to ensure adequate com-
munication coverage under varying network conditions.
3  System description
Following parameters are used to define the proposed 
framework:
Maximum communication range of each UAV = ­Mcomm
Each UAV operates at fixed height = H
Coverage Radius = ­Rc
Observation radius = ­Ro
Time slot = T
Observation space = OS
Velocity vector = V

## Page 3

5169
Int. j. inf. tecnol. (December 2025) 17(9):5167–5173	
Favourable points = FP
Number of UAV’s = N
3.1  Evaluation metrics
To assess UAV swarm performance, three key evaluation 
metrics are introduced: coverage, fairness, and energy 
consumption. The objective is to optimize these metrics 
collectively.
•	 Coverage index (CI) [13]: this metric measure the pro-
portion of FP’s covered by at least one UAV over the past 
T time slots. A FP is classified as “covered” if it falls 
within the communication range of any UAV. The cover-
age index at a given time slot t is calculated in Eq. (1):
where S represents the total number of FPs, and wt (k) 
denotes the number of time slots during which FP is covered.
•	 Energy consumption (E) [14]: UAV energy expendi-
ture is assumed to be proportional to flight distance. The 
energy consumption per UAV at time slot T is given in 
in Eq. (2):
where e0 = 0.5e_0 = 0.5 represents the energy required for 
hovering, D is the normalized flight distance, and k is a coef-
ficient set to 0.5. The total energy index across N UAVs and 
T time slots is defined in Eq. (3):
To integrate these metrics, a combined Coverage-Fair-
ness-Energy (CFE) score [15] is introduced in in Eq. (4):
A higher CFE score indicates better performance, as it 
signifies increased coverage, balanced fairness, and efficient 
energy utilization.
3.2  Proposed mechanism
The proposed DRL framework (GRU + GAT) optimizes 
the placement of the UAV and the selection of relay paths 
under varying coverage environment. This approach ensures 
that all UAV’s follow the same policy for decentralized path 
planning and control, utilizing ad-hoc network communi-
cation. The proposed framework comprises encoder for 
processing input features, GAT and GRU (memory unit) as 
shown in Fig. 1.
Initially, the framework employs an encoder to process 
raw input in Eq. (5):
(1)
CI = Swt(k)St
(2)
E = e0 + k × D
(3)
E = 1tN
∑
휏
(4)
CFE = CI × E
where OS represents the local observation and ­Ro is observa-
tion radius by UAV. To embed the communication protocol 
within the network, GAT is incorporated. In GAT, each UAV 
is represented as a node within a graph, with node embed-
ding. These embedding are shared via edges between nodes, 
enabling each UAV to process both its own and neighbour-
ing nodes’ information. Figure 2 shows the working of GAT.
•	 Self-attention mechanism for computing attention coef-
ficients is represented using Eq. (6) as:
where:
(5)
EN = Ro(OS)
(6)
Aij = softmax j
Qii ⋅KT
jj
√
dk

Fig. 1   Blocks of the proposed framework
Fig. 2   Working of GAT​

## Page 4

5170
	
Int. j. inf. tecnol. (December 2025) 17(9):5167–5173
Qi = WQei—query vector for node i
Kj = Wkej—key vector for node j
dk—dimensionality of the key vectors
softmaxj — normalization across all neighbors of node i
•	 Graph Attention Update
where:
Vj = WVej− value vector of neighbor j
N(i) — neighborhood of node i
#ij — attention coefficient weighting neighbor j
•	 Temporal GRU Integration is represented as:
where:
hi—static embedding from GAT at time t
hi,t−1—previous hidden state of node i
hi,t—updated temporal embedding.
Figure 3 shows GRU structure used in the proposed 
framework.
4  Results and discussions
The proposed framework is comprehensively tested to 
ensure it is scalable, robust, and accurate in navigation. The 
(7)
hi =
∑
j∈N(i)
#ij ⋅Vj
(8)
hi,t = GRU(hi, hi,t−1
)
test was orchestrated to compare with state-of-the-art deep 
reinforcement learning (DRL) frameworks and conventional 
UAV navigation techniques across different conditions. All 
tests were carried out in a multi-UAV setup where 20 UAVs 
were used to train followed by testing across different scales 
(5 to 40 UAVs) to assess generalization. Each setting was 
simulated for 100 independent runs, and the results reported 
are averaged values.
•	 Scalability analysis
For measuring scalability, Coverage-Fairness-Energy 
(CFE) score is chosen as the major metric. Figure 4 pre-
sents how CFE values change with the number of UAVs. 
The results are compared with baseline models such as 
DRGN (deep recurrent graph network), DGN (deep graph 
network), MAAC (message authentication acceleration 
protocol), DQN (deep Q network), and CommNet (commu-
nication network). Classic DRL algorithms like DGN and 
DRGN exhibit reasonable flexibility as the number of UAVs 
increases, but performance drops precipitously for more than 
30 UAVs because of communication bottlenecks. Traditional 
baselines like DQN, CommNet, and MAAC degrade further, 
especially at high UAV density, with CFE scores dropping 
below 70 in most cases.
Conversely, the GRU + GAT approach in this work 
maintains consistently high CFE scores across scales, up 
to a level of over 90 in the 40-UAV case. This robustness is 
indicative of the capability of attention-based semantic com-
munication combined with temporal modeling to process 
larger fleets with little degradation.
•	 Robustness against communication drop rate
Another important assessment was performed by altering 
the drop rate of communication, emulating packet loss and 
unreliable channel conditions that are commonly found in 
actual UAV deployments. Figure 5 illustrates that increas-
ing drop rate makes all models decrease their CFE scores. 
Nevertheless, the introduced framework has much slower 
degradation, with CFE values exceeding 80 even at high 
drop rates. In comparison, DRGN and DGN fall in the 70–75 
categories, whereas baseline methods such as CommNet 
and DQN drop below 65. Such robustness validates that the 
graph attention mechanism successfully compensates for 
lost communication connections by focusing on the most 
important neighbors.
4.1  Navigation accuracy and error rate comparison 
with existing studies
In order to compare navigation accuracy, the presented 
GRU + GAT paradigm was compared to six popularly 
Fig. 3   GRU structure ­(ht denotes current hidden state, ­ht’ denotes 
previous hidden state, W denotes weight matrix)

## Page 5

5171
Int. j. inf. tecnol. (December 2025) 17(9):5167–5173	
referenced UAV coordination strategies: Flying Ad-hoc Net-
works (FANETs) [7], ε-greedy exploration [8], game-theo-
retic models [9], mean-field control theory [10], multi-agent 
DRL (MADRL) [11], and centralized training with decen-
tralized execution (CTDE) [12]. In raw accuracy, FANETs 
recorded 95.3%, ε-greedy recorded 96.1%, game-theoretic 
models recorded 97.0%, mean-field control theory recorded 
97.4%, MADRL recorded 98.0%, and CTDE recorded 
98.4%, but the proposed GRU + GAT surpassed all base-
lines with 99.2%.
While these absolute accuracy values are numeri-
cally close, a more distinct picture can be obtained when 
Fig. 4   CFE Score comparison
Fig. 5   Communication Drop 
Rate analysis

## Page 6

5172
	
Int. j. inf. tecnol. (December 2025) 17(9):5167–5173
converted to error rates (Fig. 6): FANETs are 4.7% errors, 
ε-greedy is 3.9%, game-theoretic models are 3.0%, mean-
field control theory are 2.6%, MADRL are 2.0%, CTDE are 
1.6%, and GRU + GAT is merely 0.8%. This way, the differ-
ences are consequential: GRU + GAT is twice as incorrect as 
CTDE and almost six times as incorrect as FANETs. Rela-
tive improvement once again emphasizes this trend, with 
ε-greedy decreasing errors by 17% relative to FANETs, 
game-theoretic by 36%, mean-field by 45%, MADRL by 
57%, CTDE by 66%, and the proposed GRU + GAT by a 
remarkable 83%. The comparative point of view frames 
the benefit of the proposed method graphically clear, since 
its error bar is smaller than a half of the best next alterna-
tive and in proportion to legacy baselines. The superiority 
results from the synergy of spatial attention using GAT and 
temporal modeling using GRU, which collectively facilitate 
accurate decision-making under partially observable and 
dynamic UAV settings (Table 1).
5  Conclusion and future scope
This paper presents a fully decentralized DRL-based 
approach for UAV navigation in varying network condi-
tions. It integrates GAT for self-attention mechanism and 
GRU-based memory units for temporal data retention, 
defined model effectively enables UAVs to collaborate and 
optimize communication coverage autonomously. Through 
extensive simulations, this study demonstrated that the pro-
posed framework outperforms traditional methods in terms 
of navigation accuracy, and adaptability. The results show 
that defined model can successfully manage large UAV 
swarms and navigate complex, randomly distributed envi-
ronments with partial observability constraints. The results 
show that the proposed GRU + GAT surpassed all baselines 
models with 99.2% navigation accuracy. Additionally, it has 
the ability to fine-tune the model in real-time which makes 
it highly practical for real-world deployment.
Future research can explore extending the proposed 
model to heterogeneous UAV swarms with varying capa-
bilities, incorporating adaptive communication and inves-
tigating real-world implementation challenges. By further 
refining decentralized learning methodologies, UAV swarms 
can become even more effective in addressing critical real-
world applications, such as emergency response and remote 
connectivity solutions.
Fig. 6   Error rate comparison
Table 1   Validation of proposed work
Existing/proposed
Methods used
Navigation accuracy (%) Error rate (%)
[7]
Flying Ad-hoc Networks (FANETs)
95.3
4.7
[8]
ε-greedy strategy
96.1
3.9
[9]
Game-theoretic frameworks
97.0
3.0
[10]
Mean-field game control theory
97.4
2.6
[11]
Multi-agent deep reinforcement learning (MADRL)
98.0
2.0
[12]
Centralized training with decentralized execution (CTDE)
98.4
1.6
Proposed
GAT + GRU​
99.2
0.8

## Page 7

5173
Int. j. inf. tecnol. (December 2025) 17(9):5167–5173	
Declarations 
Conflict of interest  No competing interests associated with the giv-
en study.
References
	 1.	 Xie H, He T, Wei S et al (2025) Blockchain-based entity access 
control scheme for ubiquitous UAV swarm tasks. Computing 
107:32. https://​doi.​org/​10.​1007/​s00607-​024-​01381-z
	 2.	 Mahmood A, Rehman F, Okasha M et al (2024) Neural adaptive 
sliding mode control for camera positioner quadrotor UAV. Int J 
Aeronaut Space Sci. https://​doi.​org/​10.​1007/​s42405-​024-​00781-x
	 3.	 Minh Nam P, Van Toan H, Hoang An N et al (2025) Average 
achievable rate analysis for reliable control in UAV-based short-
packet communication networks. Wireless Pers Commun. https://​
doi.​org/​10.​1007/​s11277-​024-​11718-8
	 4.	 Venkatasivarambabu P, Agrawal R (2024) Enhancing UAV navi-
gation with dynamic programming and hybrid probabilistic route 
mapping: an improved dynamic window approach. Int J Inf Tech-
nol 16:1023–1032. https://​doi.​org/​10.​1007/​s41870-​023-​01671-3
	 5.	 Hu C (2022) Attitude stability control of UAV gyroscope 
based on neutral statistics for smart cities. Int J Syst Assur 
Eng Manag 13(Suppl 1):281–290. https://​doi.​org/​10.​1007/​
s13198-​021-​01391-6
	 6.	 Xiong J, Yang Y, Cheng Z, Liu L, Wang Y and Fan H (2020) 
Observer-like model reference adaptive augmenting based fixed-
wing UAV control. In: 2020 39th Chinese control conference 
(CCC), Shenyang, China, pp 6804–6809. https://​doi.​org/​10.​
23919/​CCC50​068.​2020.​91892​64.
	 7.	 Jajala KK, Buduri R (2024) Efficient and secure routing with 
UAV: guidedpheromone update based on improved ant colony 
optimization and fuzzy logic for congestion control in vehicular 
ad-hoc network. Int J Inf Technol 16:4089–4110. https://​doi.​org/​
10.​1007/​s41870-​024-​01978-9
	 8.	 Vijaya J, Thangaraj M (2024) Analysis and optimization of path 
finding algorithm for unmanned aerial vehicles. Int J Inf Technol 
16:3973–3981. https://​doi.​org/​10.​1007/​s41870-​024-​01917-8
	 9.	 Sahoo B, Das D, Pujhari KC et al (2025) Optimization of route 
planning for the mobile robot using a hybrid Neuro-IWO tech-
nique. Int J Inf Technol 17:1431–1439. https://​doi.​org/​10.​1007/​
s41870-​024-​02231-z
	10.	 Mademlis I, Symeonidis C, Tefas A et al (2024) Vision-based 
drone control for autonomous UAV cinematography. Mul-
timed Tools Appl 83:25055–25083. https://​doi.​org/​10.​1007/​
s11042-​023-​15336-7
	11.	 Banerjee A, Mahato GK, Chakraborty SK (2025) Securing 
FANET using federated learning through homomorphic matrix 
factorization. Int J Inf Technol 17:17–36. https://​doi.​org/​10.​1007/​
s41870-​024-​02197-y
	12.	 Cheng ZH, Pei HL (2022) Control effectiveness enhance-
ment for the hovering/cruising transition control of a ducted 
fan UAV. J Intell Robot Syst 105:89. https://​doi.​org/​10.​1007/​
s10846-​022-​01689-y
	13.	 Yuvaraj R, Sarveshwaran V (2024) Modified hunter prey optimi-
zation to enable secure communication for UAV. Int J Inf Technol 
16:1569–1579. https://​doi.​org/​10.​1007/​s41870-​023-​01690-0
	14.	 Liu Y, Wang H, Fan J et al (2021) Trajectory stabilization control 
for aerial recovery of cable-drogue-UAV assembly. Nonlinear Dyn 
105:3191–3210. https://​doi.​org/​10.​1007/​s11071-​021-​06773-w
	15.	 Bai T, Wang D, Masood RJ (2022) Formation control of quad-
rotor UAV via PIO. Sci China Technol Sci 65:432–439. https://​
doi.​org/​10.​1007/​s11431-​020-​1794-2
Publisher’s Note  Springer Nature remains neutral with regard to 
jurisdictional claims in published maps and institutional affiliations.
Springer Nature or its licensor (e.g. a society or other partner) holds 
exclusive rights to this article under a publishing agreement with the 
author(s) or other rightsholder(s); author self-archiving of the accepted 
manuscript version of this article is solely governed by the terms of 
such publishing agreement and applicable law.
