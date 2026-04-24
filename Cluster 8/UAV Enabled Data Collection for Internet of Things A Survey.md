# UAV Enabled Data Collection for Internet of Things A Survey.pdf

## Page 1

arXiv:2211.09555v1  [cs.RO]  17 Nov 2022
1
UAV Assisted Data Collection for Internet of
Things: A Survey
Zhiqing Wei, Member, IEEE, Mingyue Zhu, Ning Zhang, Senior Member, IEEE, Lin Wang,
Yingying Zou, Zeyang Meng, Huici Wu, Member, IEEE, and Zhiyong Feng, Senior Member, IEEE
Abstract—Thanks to the advantages of ﬂexible deployment
and high mobility, unmanned aerial vehicles (UAVs) have been
widely applied in the areas of disaster management, agricultural
plant protection, environment monitoring and so on. With the
development of UAV and sensor technologies, UAV assisted data
collection for Internet of Things (IoT) has attracted increasing
attentions. In this article, the scenarios and key technologies of
UAV assisted data collection are comprehensively reviewed. First,
we present the system model including the network model and
mathematical model of UAV assisted data collection for IoT. Then,
we review the key technologies including clustering of sensors,
UAV data collection mode as well as joint path planning and
resource allocation. Finally, the open problems are discussed
from the perspectives of efﬁcient multiple access as well as joint
sensing and data collection. This article hopefully provides some
guidelines and insights for researchers in the area of UAV assisted
data collection for IoT.
Index terms— Unmanned Aerial Vehicle; Wireless Sensor
Networks; Data Collection; Internet of Things; Clustering;
Data Collection Mode; Path Planning; Resource Allocation;
Multiple Access; Joint Sensing and Data Collection; Review;
Survey
I. INTRODUCTION
With the development of Internet of Things (IoT), sensors
are widely deployed in the scenarios such as intelligent trans-
portation, forest monitoring, smart city and smart ocean. It is
estimated that by 2030, the number of sensors in the world
will exceed 100 trillion [1]. Hence, the collection of the huge
amount of data from sensors faces great challenge. The data
collection techniques of IoT require low energy consumption,
low delay and high reliability.
Unmanned aerial vehicle (UAV) with wide coverage and
high mobility provides new opportunities for data collection
of IoT [2, 3]. UAV assisted data collection has the advantages
of high agility, high ﬂexibility and low cost. In addition, UAV
can collect data in close proximity to sensors, which greatly
Zhiqing Wei, Mingyue Zhu, Lin Wang, Yingying Zou, Zeyang Meng, and
Zhiyong Feng are with the Key Laboratory of Universal Wireless Communica-
tions, Ministry of Education, School of Information and Communication Engi-
neering, Beijing University of Posts and Telecommunications, Beijing 100876,
China (email: {weizhiqing; mingyue zhu; wlwl; zouyingying; mengzeyang;
fengzy }@bupt.edu.cn).
Ning Zhang is with the Department of Electrical and Computer Engi-
neering, University of Windsor, Windsor, ON, N9B 3P4, Canada. (e-mail:
ning.zhang@uwindsor.ca).
Huici Wu is with the National Engineering Lab for Mobile Network
Technologies, Beijing University of Posts and Telecommunications, Beijing
100876, China, and also with Peng Cheng Laboratory, Shenzhen 518066,
China (e-mail: dailywu@bupt.edu.cn)
UAV Assisted Data Collection for Internet of Things
Section Ⅱ : System Model
Section Ⅲ : Clustering of Sensors
Section Ⅳ : Data Collection Mode
Section Ⅶ  : Conclusion
Section Ⅴ : Joint Path Planning and Resource Allocation
Clustering Algorithms
Clustering of Sensors in UAV Assisted Data Collection
Hovering Mode
Flying Mode
Hybrid Mode
Graph Theory based Algorithms
Optimization Theory based Algorithms
Artificial Intelligence based Algorithms
Supervised Learning Algorithms
Intelligent Optimization  Algorithms
Reinforcement Learning Algorithms
Section Ⅵ : Future Trends
Efficient Multiple Access
Joint Sensing and Data Collection
Network Model
Problem Formulation
Fig. 1. The organization of this article.
reduces the energy consumption of IoT. The combination of
UAV and IoT facilitates timely and effective data collection,
especially in the complex, harsh or remote environments [4–
8]. As an ideal tool for data collection, UAV assisted data
collection for IoT has the following advantages.
• High efﬁciency and ﬂexiblility of data collection: UAV
reduces the data collection time because its trajectory can
be optimized [9–11].
• Low energy consumption and long network lifetime for
IoT: UAV not only reduces the energy consumption of
data transmission in IoT, but also can charge the sen-
sors wirelessly, which collectively improve the network
lifetime of IoT [12, 13].

## Page 2

2
TABLE I
GLOSSARY.
Abbr.
Deﬁnition
Abbr.
Deﬁnition
Abbr.
Deﬁnition
3D
Three-Dimensional.
DRL
Deep Reinforcement Learning.
MTCDs Machine-Type
Communication
Devices.
5G
5th Generation Mobile Networks.
FDMA
Frequency Division Multiple Ac-
cess.
NOMA
Non-Orthogonal
Multiple-
Access.
ACO
Ant Colony Optimization.
G2A
Ground-to-Air.
PRM
Probabilistic Roadmap
AWGN
Additive White Gaussian Noise.
GA
Genetic Algorithm.
PSO
Particle Swarm Optimization.
AI
Artiﬁcial Intelligence.
GBD
Generalized Benders Decomposi-
tion.
QoS
Quality of Service.
AoI
Age of Information.
GTOA
Group-based
Trajectory
Optimization Algorithm.
RL
Reinforcement Learning.
AP
Access Point.
HCP
Hybrid Clustering Routing Proto-
col.
RSSI
Rreceived Signal Strength Indica-
tor.
BB
Branch and Bound.
Het-
IoT
Heterogeneous
Internet
of
Things.
SA
Simulated Annealing.
BCD
Block Coordinate Descent.
HHPS
Hybrid hovering points Selection.
SCA
Successive Convex Approxima-
tion.
BRB
Branch Reduction and Bound.
IoT
Internet of Things.
SFLA
Shufﬂed
Frog
Leaping
Algo-
rithm.
BS
Base Station.
KKT
Karush-Kuhn-Tucker.
SIC
Successive Interference Cancela-
tion.
CH
Cluster Head.
LEACH Low Energy Adaptive Clustering
Hierarchy.
STOA
Segment-based Trajectory Opti-
mization Algorithm.
CP
Data collection Point.
LoS
Line of Sight.
TDMA
Time Division Multiple Access.
CRB
Cram´er-Rao Bound.
MA
Memetic Algorithm.
TSP
Traveling Salesman Problem.
CS
Cuckoo Search Algorithm.
MAC
Multiple Access Control.
TSPN
Traveling Salesman Problem with
the Neighborhood.
DDPG
Depth Deterministic Gradient De-
scent.
MDP
Markov Decision Process.
UAV
Unmanned Aerial Vehicle.
DE
Differential Evolution.
MIMO
Multiple Input Multiple Output.
UKF
Unscented Kalman Filter.
DFP
Direct Future Prediction.
MLE
Maximum Likelihood Estimation.
VNS
Variable Neighborhood Search.
DL
Deep Learning.
MM
Majorize-Minimize or Minorize-
Maximize.
VoI
Value of Information.
DP
Dynamic Programming.
MPT
Microwave Power Transfer.
WSN
Wireless Sensor Network.
• Wide coverage: Due to the high altitude of UAV, there
is a higher chance for line of sight (LoS) connections
between UAV and sensors, which improves the success
probability and coverage of communication [8, 14].
Along with the above advantages, there are also several
challenges in UAV assisted data collection.
• The clustering of sensors and selection of data collection
mode: The deployment and clustering of sensors, as well
as the selection of data collection mode will greatly
affect the performance of UAV assisted data collection.
Hence, there exists a complex air-ground coupling in the
optimization of the performance of data collection.
• Joint path planning and resource allocation of UAV: The
resource allocation problem is coupled with the path
planning of UAV, which further complicates the problem
of resource allocation.
Therefore, in view of the challenges of UAV assisted data
collection, this article provides in-depth survey on three key
technologies including the clustering of sensors, the modes of
UAV assisted data collection, and the joint UAV path planning
and resource allocation.
A. Existing Surveys and Tutorials
Recently, a few related surveys and tutorials have been
published. Li et al. [15] summarize the UAV communication
for 5G/B5G wireless networks. They summarize and review
the air-ground integrated network architecture and various 5G
technologies implemented on UAV platform. In UAV assisted
IoT, media access control (MAC) has a crucial impact on
spectrum efﬁciency and energy efﬁciency of battery powered
sensor networks. In [12], various MAC protocols for UAV
assisted IoT are reviewed. Heaphy et al. [16] describe the
potential application of UAV in forestry. UAV makes up for
the shortcomings of satellites and manned aircraft, and collects
images with higher temporal and spatial resolution to support
forest inventory, health monitoring, silviculture and harvesting
operations. Pham et al. [17] focus on the application of UAV in
trafﬁc data collection. This paper not only compares various
UAV operation frameworks and popular platforms, but also
applies UAV in speed behavior analysis, gap acceptance and
merging behavior. In [18], Dan et al. introduce the mode and
latest progress of cooperation among various functional com-
ponents in UAV assisted wireless sensor network (WSN). For
large-scale IoT deployed in complex environment, Yang et al.

## Page 3

3
8$9
'DWD/LQN
&RQWURO6WDWLRQ
&RQWURO/LQN
6HUYHU
8$9)OLJKW3DWK
%DVH6WDWLRQ$FFHVV3RLQW
6HQVRU
Fig. 2. The system model of UAV assisted data collection.
[19] review four technologies, including sensor deployment,
UAV conﬁguration (such as ﬂight speed and radius), UAV path
planning and UAV autonomous navigation. However, existing
articles have the following limitations.
• There is a lack of investigation and discussion on the data
collection modes using UAV.
• The clustering algorithms of sensors are not discussed in
details.
• The joint path planning and resource allocation schemes
for UAV assisted data collection are not reviewed.
B. Contributions and Organization
This article aims to review the development status and future
trends of UAV assisted data collection techniques. To this end,
we conduct a comprehensive review on the relevant literatures
in recent years. The scenario of UAV assisted data collection
is not a simple combination of UAV networking and IoT.
They need to cooperate with each other to improve the system
efﬁciency, which is the perspective of this article. The main
contributions of this article are summarized as follows.
• Three key technologies of UAV assisted data collection
for IoT including the clustering of sensors, the data
collection modes, and the joint UAV path planning and
resource allocation methods, are reviewed in details.
• The complete solution of UAV assisted data collection
including the key technologies such as joint sensing and
data collection, clustering of sensors, efﬁcient access of
large-scale sensors, and efﬁcient routing in WSN, and
joint path planning and resource allocation, is designed.
Among these key technologies, efﬁcient multiple access
and joint sensing and data collection have a large proba-
bility to be the future research trends.
As shown in Fig. 1, the rest of this article is organized
as follows. Section II introduces the system model of UAV
assisted data collection for IoT. In Section III, the clustering
algorithms of sensors are introduced. Section IV investigates
three data collection modes, analyzing the advantages and
disadvantages of each data collection mode. Section V reviews
the joint UAV path planning and resource allocation methods
in details. Section VI discusses the complete solution and
future trends of UAV assisted data collection. Finally, Section
VI summarizes this article.
II. SYSTEM MODEL
In this section, we introduce the network model and math-
ematical model in UAV assisted data collection.
A. Network Model
As illustrated in Fig. 2, the network elements of UAV
assisted data collection consist of sensor, UAV, control station
and server, which are explained as follows.
• Sensor: In order to sense the environment, the sensors
are deployed and the sensing data are sent to UAV. The
type of sensors depends on the application scenarios.
For instance, the temperature and humidity sensors are
deployed in the forest monitoring scenario.
• UAV: The UAV ﬂies above the sensors to collect data,
which is then brought back to the server.
• Control station: The control station plans UAVs’ ﬂight
path for efﬁcient data collection.
• Base station (BS)/Access point (AP): The BS/AP collects
the sensing data directly from the surrounding sensors,
as well as the UAVs.
• Server: The server stores and processes the data from
sensors.
As shown in Fig. 2, in the scenario of UAV assisted data
collection, UAV takes off from a control station and ﬂies above
sensors to collect data, such as the potential of hydrogen (PH)
and salinity in the ocean, the wildlife and ﬁre in the forest, the
trafﬁc and weather in the smart city. Then the UAV delivers the
data to the BS/AP and ﬁnally returns to the control station. The
scheme of UAV assisted data collection aims at high efﬁciency,
low energy consumption and low delay during data collection.

## Page 4

4
&RQWURO6WDWLRQ
%DVH
6WDWLRQ
s1
s2
sk
uK
u2
u1
ggg
ggg
&OXVWHU0XPEHU
&OXVWHU+HDG
'DWD/LQN
u0
uK+1
'DWD&ROOHFWLRQ3RLQW
Fig. 3. Optimization of UAV assisted data collection.
In addition, some standard IoT technologies are applied
in UAV assisted data collection, such as NB-IoT and LoRa.
LoRa can be used as a gateway for UAV assisted data col-
lection to extend the coverage to rural and remote areas [20].
Delafontaine et al. [21] present a UAV assisted localization
system using LoRa networks in which a UAV is deployed to
improve the positioning accuracy of sensor. Because NB-IoT
can support large coverage and meet the low-power and low-
cost operation of sensors, it is also applied in UAV assisted
data collection, such as soil detection [22], city open water
monitoring [23] and air quality monitoring [24].
B. Mathematical Model
As shown in Fig. 3, the system of UAV assisted data
collection is composed of a UAV, a BS, a control station and M
sensors. The set of sensors is denoted by M
∆= {1, 2, . . ., M}.
The UAV collects and sends the data of sensors back to the
BS. The control station plans the ﬂight path of the UAV
and charges the UAV before ﬂight. There are the following
assumptions [25, 26].
• Distribution of sensors: Sensors are randomly distributed
in the target area. Their position coordinates are known
and expressed as sm = (xm, ym, h)T ∈R3×1, m ∈M.
The sensor is equipped with omni-directional antenna and
the communication range is rc.
• Clustering of sensors: When the number of sensors is
small or the locations are scattered, each sensor can
directly upload the data to the UAV. When the number
of sensors is large, the sensors need to be clustered.
Hence there are two types of nodes, namely, cluster head
(CH) and cluster member (CM). The CH collects the
data of CMs within the cluster, and is responsible for
communicating with the UAV [27].
• Self-positioning of UAV: UAV acquires its location via the
installed positioning module such as Global Navigation
Satellite System (GNSS) module [28].
• Number and type of UAVs: The number of UAVs depends
on the number of sensors and the amount of data to be
collected. The type of UAVs consists of rotor UAV and
ﬁxed-wing UAV [29]. Therefore, three data collection
modes, i.e., hovering mode, ﬂying mode and hybrid
mode, exist in the literatures.
• Mobility, energy and capacity of UAVs: UAV can ﬂy at
a ﬁxed altitude H and speed v (When v = 0, it means
that the UAV is hovering), and Vmax is the maximum
speed that UAV can reach. The maximum ﬂight distance
and energy of UAV are Lmax and Emax, respectively
[30]. The buffer size of UAV is also taken into account,
limiting the amount of data that can be collected.
• Ground-to-air communication and transmission rate:
There will be LoS channel between sensors and UAV
with a certain probability. This probability depends on
the environment and the angle between the sensor and
the UAV. As shown in [26, 31], the probability of LoS
transmission is
PLoS (sm, u) =
1
1 + a exp [−b (θ (sm, u) −a)],
(1)
where θ (sm, u) is the angle between the sensor sm, m ∈
M and the UAV at position u ∈R3×1. a and b are
environmental parameters, which mainly depend on the
ratio of building area to total land area, the average
number of buildings in a unit area and the height of
buildings [26]. Then the transmission rate between the
sensor sm and the UAV located at u is [32]
R (sm, u) = Blog2
 
1 + |h (sm, u)|2Pm
N0
!
,
(2)
where B is the channel bandwidth, h (sm, u) is the
channel gain between UAV and the sensor, Pm is the
transmit power of each sensor when communicating with
UAV, N0 is the power of additive Gaussian white noise.
Combined with the model in Fig. 3 and the above assump-
tions, it is assumed that M sensors in the IoT are divided
into K clusters, expressed as K
∆= {1, 2, . . . , K}. Each cluster
has only one CH sk, and the sensors in the cluster can
communicate with each other. The goal of UAV is to collect
data from the CHs quickly and efﬁciently. In order to achieve
this goal, the distance, ﬂight time, and energy consumption for
path planning need to be jointly optimized [19]. Meanwhile,
the data collection mode between UAV and CH, such as
hovering mode, ﬂying mode and hybrid mode, has an impact
on the efﬁciency of data collection [33]. Taking hovering
mode as an example, the UAV collects data of CH sk at the
data collection point uk, k ∈K [34]. Other data collection
modes have corresponding constraints. Before formulating the
problem, the following constraints need to be considered.
1) Sensor energy consumption constraint: This constraint
ensures that the energy consumption of each sensor sk does
not exceed Ek.
tkPk ≤Ek
∀k,
(3)
Pk > 0
∀k.
(4)
In hovering mode, the channel conditions between UAV and
sensors remain unchanged, hence the sensor sk can transmit
data with constant transmit power Pk. tk is the hovering time

## Page 5

5
of UAV at data collection point uk.
2) Data collection constraint: The sensor sk needs to meet
the minimum data collection requirements rk.
tkBlog2
 
1 + |h (sk, uk)|2Pk
N0
!
≥rk
∀k.
(5)
3) UAV energy consumption constraint: The total energy
consumption of UAV cannot exceed its maximum energy
Emax.
Pu (0)
K
X
k=1
tk + Pu (v)
K+1
P
i=0
K+1
P
j=0
xi,jdi,j
v
≤Emax,
(6)
where Pu (v) is the power of UAV ﬂying at constant speed v
(0 < v ≤Vmax) [35, 36], di,j is the distance from ui to uj.
4) UAV trajectory constraint: This constraint ensures that
the UAV starts from the control station, traverses all data
collection points and then returns to the BS.
K
X
i=1
xi,j = 1
i ̸= j, ∀j ∈K,
(7)
K
X
j=1
xi,j = 1
i ̸= j, ∀i ∈K,
(8)
K
X
j=1
x0,j =
K
X
i=1
xi,K+1 = 1 ∀i, j ∈K,
(9)
xi,j, x0,j,xi,K+1 ∈{0, 1} i ̸= j, ∀i, j ∈K,
(10)
where xi,j is a binary variable. xi,j = 1 indicats that the UAV
ﬂies from the data collection point ui to uj. u0 and uK+1
represent the starting point (control station) and ending point
(BS) of the UAV, respectively.
5) Age of information constraint: The age of information
(AoI) is a performance indicator to measure the timeliness of
data. Compared with the latency, AoI includes not only the
transmission delay of data packets, but also the waiting time
of data packets at the source node and the residence time
at the destination node [37, 38]. AoI constraint reveals the
requirements for data timeliness.
Ak
j ≤Ak,th
j
∀k ∈K, j ∈Jk,
(11)
where Ak
j and Ak,th
j
are the AoI and its threshold for the j-th
uploaded packet of CH sk, respectively. Jk
∆= {1, 2, . . . , Jk}
is the number of data packets in sk. Without considering the
sampling time and communication overhead, the AoI of the
data collected at CH sk consists of the time of data upload,
the time of UAV returning to the data center and the time of
data unloading [9, 39]. If the UAV accesses CHs sequentially
(from s1 to sK), the AoI of the j-th uploaded packet from the
CH sk can be expressed as [9]
Ak
j =
K
X
i=k
Jk
X
j=1
ςi
j −
j−1
X
l=1
ςk
l + ς0 +
K
P
i=k
∥ui −ui+1∥
v
,
(12)
where ςi
j is the time of uploading the j-th data packet for the
i-th CH, ς0 is the data unloading time of UAV. For the data
packets of CHs not accessed by UAV, the AoI is 0. If further
considering the possibility of packet expiration, AoI can be
expressed as [40]
Ak
j =





K
P
i=k
Jk
P
j=1
ςi
j −
j−1
P
l=1
ςk
l + ς0 +
K
P
i=k
∥ui−ui+1∥
v
, tk
j < tk,ex
j
Ttotal, otherwise,
(13)
where tk
j is the time interval from the generation of the j-
th data packet of sk to the completion of data collection by
UAV, tk,ex
j
is the effective time of the data packet. If the data
packet expires, its AoI is set as the overall time for the UAV
to complete the task.
The above parameters about queuing delay need to be
modiﬁed according to the queuing models, such as First-
Come-First-Service (FCFS), Last-Come-First-Service (LCFS),
priority based and limited buffer strategies [41, 42]. The
application scenarios of FCFS, LCFS and priority based model
are increasingly sensitive to data timeliness. The scenarios
requiring comprehensive data such as agricultural monitoring
and marine monitoring often adopt the FCFS model. The
LCFS model is more suitable for the scenarios that value the
latest data, such as driverless vehicle monitoring and ﬁeld ﬁre
monitoring.
UAV assisted data collection schemes usually aim at max-
imizing the amount of collected data, minimizing ﬂight time
of UAV, minimizing energy consumption of UAV or sensor,
minimizing AoI and so on. Overall, there are three key issues
in UAV assisted data collection, namely, the clustering of
sensors, the data collection mode of UAVs, and the path
planning and resource allocation of UAVs. The application
and optimization of the three key technologies are helpful to
improve the efﬁciency of data collection, ensure the timeliness
of data, as well as save the energy consumption of UAV
and sensors. Besides, it is essential to consider the clustering
algorithm of sensors and the data collection mode of UAV for
an effective path planning algorithm. In the following sections,
we will provide a thorough survey on these topics.
III. CLUSTERING OF SENSORS
In this section, we ﬁrst review the clustering algorithms in
conventional sensor network, and then discuss the clustering
of sensors in UAV assisted data collection.
A. Clustering Algorithms
When the number of sensors is large, the topology of sensor
network becomes complicated and the cost of routing between
sensors is relatively large. Therefore, it is necessary to utilize
a clustering algorithm to divide the network into several sub-
networks. The basic idea of clustering algorithms is to merge
neighboring nodes into a cluster and select a CH from each
cluster that is responsible for aggregating the data from other
sensors in the cluster.
Depending on different performance metrics, there are vari-
ous clustering algorithms. According to the selection methods

## Page 6

6
TABLE II
FACTORS AFFECTING CLUSTERING ALGORITHMS.
Reference
Methodologies
Reference
Methodologies
[43]
Select the sensor with the highest power as the
cluster head (CH).
[25]
Distributed clustering.
[9]
Afﬁﬁnity propagation.
[27, 44]
K-means clustering algorithm.
[26, 45]
Problem decomposition.
[46]
α-hop clustering algorithm.
[47]
Base station (BS) assisted clustering.
of CH, the clustering algorithms are classiﬁed into determinis-
tic CH selection algorithms, random CH selection algorithms
and adaptive CH selection algorithms [48]. According to
the control methods of clustering algorithms, the clustering
algorithms can be classiﬁed into distributed clustering algo-
rithms, hybrid clustering algorithms and centralized clustering
algorithms [49].
The widely applied clustering protocol is the low energy
adaptive clustering hierarchy (LEACH) because of its sim-
plicity [50]. More speciﬁcally, at the beginning of LEACH,
each sensor generates a random number between 0 and 1. If
the number is greater than a given threshold, it is selected
as CH. Then, the CH broadcasts a packet to other sensors in
the same network. Each node decides which cluster to join
according to the strength of the received signal, and transmits
a feedback packet to the CH in a time division multiple access
(TDMA) manner. With LEACH, the energy consumption of
each sensor is distributed evenly by periodically switching the
CHs, thereby prolonging network lifetime [48]. Recently, there
are some literatures to improve LEACH [50–52]. Basavaraj
and Jaidhar [53] propose a new threshold by calculating the
average remaining energy of sensors, the average distance
between sensors and BS, and the optimal number of CHs.
In the scenario of UAV assisted data collection, since LEACH
randomly selects CH, some sensors with less energy may be
selected, so that the communication with the UAV cannot be
completed. Chen and Shen [54] comprehensively consider the
factors such as the residual energy and the communication
range of sensor to select CH, which extend the network life.
The malicious node may be selected as CH under LEACH.
Therefore, Wang et al. [55] improve LEACH and apply UAV
to collect sensor information such as energy and ID, so as to
avoid selecting the sensor affected by malicious node as CH.
B. Clustering of Sensors in UAV Assisted Data Collection
In the scenario of UAV assisted data collection, due to the
limited energy of UAV, the energy consumption brought by
the ﬂight of UAV needs to be reduced. A large number of
clusters will reduce the energy consumption within the cluster
to forward data, but will increase the energy consumption
of UAV for ﬂight. In contrast, a small number of clusters
will reduce the energy consumption of UAV during ﬂight, but
the energy consumption of sensors will increase. Therefore,
it is necessary to jointly optimize the energy consumption of
sensors, the energy consumption of UAV, clustering of sensors
and CH selection, path planning of UAV [44]. The clustering
methods of sensors used in relevant literatures are shown in
Table II.
Chen et al. [43] and Salih et al. [25] consider the energy
constraints of sensors for clustering. Chen et al. [43] select the
sensor with the highest power as the CH to extend the lifetime
of sensors. The data forwarding rule in the cluster is that only
when the value of information (VoI), which is highest when
an event ﬁrst occurs and decays with time, is greater than a
certain threshold, the sensors in the cluster will send the data
to the CH, thereby greatly reducing the energy consumption
of the sensors. Salih et al. [25] utilize a distributed clustering
method to minimize the average sending distance from the
sensors in the cluster to the CH. In order to minimize the
AoI, Tong and Moh [9] jointly optimize the CH selection and
ﬂight path of UAV, in which an algorithm based on afﬁnity
propagation is used to determine the locations of the CH and
the associated sensor.
In addition, most of the literatures considers the energy
consumption of sensors, ﬂight time of UAV and path planning
in the clustering algorithms. Ebrahimi et al. [44] and Alfattani
et al. [27] apply the k-means clustering algorithm, and update
the sensors in the cluster through iterations. Sujit et al. [45] and
Ghorbel et al. [26] decompose the joint UAV path planning
and energy consumption optimization problem into several
sub-problems. In [45], the initial problem is decomposed
into the sub-problems of ﬁnding clusters, connecting clusters,
route planning, and UAV path planning. Ghorbel et al. [26]
decompose the problem into three sub-problems: optimizing
the position of CH, assigning sensors into clusters and UAV
path planning. The α-hop clustering algorithm designed by
Wu et al. [46] adjust the hop number in each cluster to
reduce energy consumption and delay. A large α determines
small number of clusters, which reduces the UAV path and
decreases the ﬂight time. When α is relatively small, each
cluster is small, which reduces energy consumption of data
forwarding in sensor network. Haider et al. [47] apply UAV
to get the remaining energy of sensors, channel conditions
and the distance between sensors. Then the BS utilizes these
information from UAV and determines which sensors are CHs,
which greatly extends the lifetime of the sensors.
IV. DATA COLLECTION MODE
According to the movement status of UAV during data
collection, the data collection modes are classiﬁed into three
types, namely, hovering mode, ﬂying mode and hybrid mode.
Their characteristics are summarized in Table III. Table IV is a
summary of the literatures on the three data collection modes.

## Page 7

7
TABLE III
COMPARISON OF DATA COLLECTION MODES.
Data collection
mode
Hovering at data
collection point (CP)
Continuing data
collection after
passing through CP
Energy
consumption
Flight time
The AoI of data
collected from
sensors
Hovering mode
√
×
High
High
Low
Flying mode
×
√
Low
Low
High
Hybrid mode
√
√
Medium
Medium
Medium
1 √denotes the existence of the feature, × denotes the absence of the feature
TABLE IV
THE OPTIMIZATION SCHEMES UNDER DIFFERENT DATA COLLECTION MODES.
Data collection mode
Reference
Objective function
Decision variables
Hovering mode
[56]
Minimization of the total task
duration.
The number of subregions, hovering point,
hovering time of each position, trajectory
between hovering points.
[27]
Minimization of ﬂight time of
UAV.
The number and trajectory of UAV.
[13]
Maximum of minimum energy of
sensors after data collection.
Hovering point, residence time of UAV.
[9]
Minimization of node upload time
and ﬂight time of UAV.
Position correlation between sensors and hover
points, trajectory of UAV.
Flying mode
[57]
Minimization of ﬂight time of
UAV.
Continuous optimization of interval, speed of
UAV, transmit power of sensors.
[58]
Minimization of the weighted sum
of energy consumption of UAV
and sensors.
Trajectory of UAV, wake-up scheduling of
sensors, data collection time.
Hovering and
Flying mode
[32]
Minimum of maximum data
collection time.
Trajectory of UAV, wake-up scheduling of
sensors, sensor association.
[34]
Minimization of ﬂight time of
UAV.
Data collection interval, speed of UAV, transmit
power of sensors.
Hybrid mode
[59]
Minimization of battery
consumption and Maximization of
UAV throughput.
Energy consumption and throughput of UAV,
delay of machine-type communications devices
(MTCDs) tasks, collection and computing
efﬁciency of different priorities.
[33]
Minimization of the average age
of information (AoI).
The age of collected data, data collection mode,
energy consumption of each sensor.
A. Hovering Mode
In hovering mode, the UAV stays above the data collection
point for a period of time to collect data. The data collection
point can be the location of the CH or near the CH. In [56],
the entire region is divided into several sub-regions, and UAV
hovering over these sub-regions collects data from sensors.
Hovering mode can provide relatively stable data transmission,
but the energy consumption is relatively large.
The UAV hovering locations and duration have a great
impact on the reliable data collection and the shortest ﬂight
time. A framework design for IoT based on multiple UAVs is
proposed in [33]. This work ﬁrstly optimize the number and
location of CHs to minimize the data collection time. Then,
the number of UAVs and their trajectories are optimized in
order to minimize the ﬂight time. And reliable data collection
shortens the AoI of data collected from sensors, which is
the time that the data is transmitted from sensor to the data
center. In [9], in order to minimize the maximum AoI of all
sensors, a joint sensor association and path planning strategy
is proposed to balance the ﬂight time of UAV and the upload
time of sensors which is affected by the quality of ground-to-
air communication link under hovering mode.
In addition, to maximize the lifetime of sensors, the UAV
hovering height and duration should be considered. Under the
constraints of transmit power of sensors and energy consump-
tion of UAV, Baek et al. [13] optimize the hovering point
and dwell time of UAV to maximize the minimum energy of
sensors during data transmission and energy collection periods.
B. Flying Mode
Under ﬂying mode, when UAV passes through the data
collection point, it slows down and collects the data of sensors
until it leaves the communication range of the sensors. With
the characteristics of moving while collecting data in ﬂying
mode, the collection task can be completed quickly. However,
if the amount of data is large, the UAV in ﬂighting mode may
not satisfy the the requirement of timely data collection.
Under ﬂying mode, the shortest ﬂight time is commonly
chosen as the objective function. In UAV assisted data col-
lection, it is observed that the optimal speed of UAV is

## Page 8

8
TABLE V
COMPARISON OF GRAPH THEORY BASED ALGORITHMS
Algorithm
Reference
Objective function
Decision variables
AoCD
TE
EE
AoI
Voronoi
diagram
[60]
Maximum of minimum
residual energy of sensors.
Hovering point, UAV path
planning.
×
×
√
×
[61]
Minimization of ﬂight time
of UAV.
UAV task area allocation,
UAV path planning.
×
√
√
×
Probabilistic
roadmap
[62]
Maximization of the
amount of collected data.
UAV path planning.
√
×
×
×
Hilbert
curve
[63]
Maximization of data
collection rate.
UAV path planning.
√
×
×
×
1 √denotes the existence of the feature, × denotes the absence of the feature
2 AoCD: Amount of collected data, TE: Time efﬁciency, EE: Energy efﬁciency, AoI: Age of information
proportional to the energy and density of sensors. However,
it is inversely proportional to the amount of data to be
uploaded. Thus, to minimize the ﬂight time of UAV during
data collection, the horizontal distance that the sensors can
upload data to the UAV, the speed of UAV, and the transmit
power of sensors are jointly optimized in [57] and [34]. In
the multi-UAV enabled IoT, Zhan et al. [32] focus on the
problem of minimizing the maximum completion time of
data collection among all UAVs. They jointly optimize the
trajectories of UAVs, wake-up scheduling and association for
sensors, while ensuring that sensors can successfully upload a
given amount of data with limited energy budget.
In the above literatures, the constraint is that the energy
of UAV or sensor is limited. Zhan and Huang [58] study the
fundamental tradeoff between the energy consumption of UAV
and that of all sensors. In order to characterize this tradeoff
relation, they formulate an optimization problem to minimize
the weighted sum of the energy consumption of UAV and
sensors. Then, the trajectory of UAV, mission completion time
and wake-up scheduling for all sensors are jointly optimized.
C. Hybrid Mode
The hybrid mode combines the characteristics of hovering
mode and ﬂying mode. The UAV stays above the data col-
lection point for data collection. When the UAV ﬂies to the
next collection point after a period of time, data collection can
still be carried out until the UAV is out of the communication
range of the sensor. The energy consumption and ﬂight time
under hybrid mode are smaller than that under hovering mode,
but larger than that under ﬂying mode. Different data collec-
tion modes are usually chosen according to the application
scenarios and performance requirements.
The hybrid mode can adjust the data collection mode
dynamically according to the energy consumption of UAV.
To minimize the average AoI of data collection, Jia et al.
[33] lower the AoI of data collection under three data col-
lection modes, energy consumption at each node and age
evolution of collected data. When the initialized energy of
sensor increases, hybrid mode has better performance than the
other modes. Because of the limited battery of machine-type
communications devices (MTCDs) and UAV, Zhu et al. [59]
propose a hybrid hovering points selection (HHPS) algorithm
to select the hovering points of UAV with the minimum power
consumption of MTCDs.
V. JOINT PATH PLANNING AND RESOURCE ALLOCATION
Path planning of UAV refers to the calculation of the optimal
path of UAV from the source to the destination under speciﬁed
conditions [64]. The UAV path planning has a crucial inﬂuence
on the performance of data collection. There are various goals
for path planning, such as the shortest path, the shortest
ﬂight time and the lowest energy consumption of UAV. The
characteristics of UAV, such as high mobility and ﬂexible
deployment, bring challenges for UAV path planning. Besides,
considering the limited energy and radio resources of UAV, the
UAV path planning is usually combined with resource alloca-
tion to efﬁciently optimize the resource utilization [65, 66].
Hence, the complexity of joint path planning and resource
allocation is high because the decision space is huge.
In this section, according to the techniques in the algo-
rithms, the updating methods, objective functions and so on,
we classify the path planning algorithms into graph theory
based algorithms, optimization theory based algorithms and
artiﬁcial intelligence (AI) based algorithms. Then, the relevant
literatures of UAV path planning are reviewed in the scenario
of UAV assisted data collection.
A. Graph Theory based Algorithms
Graph theory based path planning algorithms include
Voronoi diagram algorithm, probabilistic roadmap (PRM) al-
gorithm, Hilbert curve algorithm, and so on. Using graph
theory based algorithm, the geographical space where UAV
is ﬂying is converted into a graph and the path between
source and destination is searched. The comparison of different
algorithms is listed in Table V, where the key metrics are
explained as follows.
• Amount of collected data (AoCD): The amount of data
collected by UAV.
• Time efﬁciency (TE): The time duration for UAV to
complete data collection.
• Energy efﬁciency (EE): The energy consumption of UAV
and sensors in terms of battery or fuel.
• Age of information (AoI): Freshness of collected data,
which needs to be distinguished from the latency and

## Page 9

9
Obstacle
Source
Destination
Trajectory
Fig. 4. The principle diagram of Voronoi diagram.
is deﬁned as the time interval between the time when
the sensor data is generated and the time when the UAV
returns and uploads the collected data to the data center.
Speciﬁcally, the latency is the time interval between the
sending time and the receiving time of data, while AoI
is the time interval between the generation time and the
use time of data [37–39].
In UAV assisted data collection, AoCD, TE, EE, AoI are
the key performance metrics that may be considered in the
algorithm design.
1) Voronoi diagram:
Voronoi diagram, also known as
Tyson polygon or Dirichlet diagram, is a set of polygons
composed of vertical bisectors connecting two adjacent points,
where the points are the obstacles [67, 68]. The advantage of
Voronoi diagram is that the generated path is far away from
obstacles. Thus collision can be avoided. As shown in Fig.
4, the circular is regarded as the obstacle and the plane is
divided in light of the nearest neighbor principle. The point
within a polygon is nearest to the obstacle within this polygon
compared with other obstacles. Then, the shortest path is
searched along the edges of the polygons as the ﬂight path of
UAV [69], which is denoted by the dotted line in Fig. 4. The
Voronoi diagram can be constructed using four algorithms:
incremental algorithm, intersect of half planes, divide and
conquer algorithm and plane sweep algorithm [70–72].
Aiming to design the energy-saving path of UAV for data
collection, Baek et al. [60] modify the Voronoi diagram which
determines the optimal hovering point of UAV according to the
residual energy of sensors, so as to maximize the minimum
remaining energy of sensors, extending the network lifetime.
Compared with the path planning of UAV based on Voronoi
diagram in [73–75], the total length of ﬂight path of UAV
is shortened. However, in practical application scenarios, it is
difﬁcult for a single UAV to deal with too many sensors. Wang
et al. [61] study the cooperative data collection system using
multiple UAVs, which applied Voronoi diagram to allocate the
collection areas of each UAV. Combined with the optimization
of the speed, collection position and transmit power of UAV,
the trajectories of multiple UAVs are obtained, which effec-
tively shorten the completion time of data collection.
2) Probabilistic roadmap: PRM consists of sampling points
and collision-free straight-line edges [76–78], as shown in
Source
Destination
Trajectory
Obstacle
Sampling Points
Fig. 5. The principle diagram of PRM.
Fig. 5. The sampling points are selected in the space without
obstacles. PRM based path searching algorithm consists of
the stages of learning and query. In the learning stage, PRM
randomly scatters points in the region to construct an undi-
rected graph. In the query stage, PRM applies the shortest path
algorithms to ﬁnd the ﬂight path of UAV. This method uses
relatively few random sampling points to ﬁnd a solution. And
the probability of ﬁnding a path tends to 1 with the increase
of the number of sampling points.
(a) The ﬁrst step.
(b) The second step.
(c) The third step.
(d) The fourth step.
Fig. 6. The ﬁrst three steps of the Hilbert space-ﬁlling curve.
Penicka et al. [62] consider the existence of obstacles in
UAV assisted data collection. The data collection mission is
considered as a physical orienteering problem, which aims at
ensuring a feasible, collision-free trajectory to maximize the
collected data (reward) with the constraint of energy (bud-
get). The asymptotically optimal sampling-based probabilis-
tic roadmap (PRM*) combined with variable neighborhood
search (VNS) algorithm is proposed. The proposed algorithm
applies VNS algorithm to expand the initial roadmap with
low-density nodes, and the PRM* algorithm is applied to
build a shortened collision-free trajectory. The low-density
initial roadmap brought an advantage of lower computational

## Page 10

10
TABLE VI
COMPARISON OF OPTIMIZATION THEORY BASED ALGORITHMS
Algorithm
Reference
Objective function
Decision variables
AoCD
TE
EE
AoI
Dynamic
programming
[34]
Minimization of ﬂight time
of UAV.
Time slot, speed of UAV,
transmit power of sensors.
√
√
√
×
[57]
Minimization of ﬂight time
of UAV.
Time slot, transmit power of
sensors, data collection
interval.
√
√
√
×
[9]
Minimization of AoI.
The number and location of
data collection points, UAV
path planning, associations of
sensors and data collection
points.
×
√
×
√
[33]
Minimization of AoI.
Data collection mode, energy
consumption of sensors, age
evolution of collected data.
×
×
√
√
[80]
Minimization of the
average AoI.
Energy harvesting time, data
collection time for each
sensor, UAV path planning.
×
×
×
√
[81]
Minimization of AoI.
The number of data collection
points, transmission priority of
sensors, the balance between
ﬂight time of UAV and data
upload time, UAV path
planning.
×
√
×
√
Branch and
bound
[82]
Maximization of the
number of sensors and
minimization of the amount
of collected data with time
constraint.
Radio resource allocation,
UAV path planning.
√
×
×
√
1 √denotes the existence of the feature, × denotes the absence of the feature
2 AoCD: Amount of collected data, TE: Time efﬁciency, EE: Energy efﬁciency, AoI: Age of information
complexity compared with other algorithms with high-density
initial roadmaps.
3) Hilbert curve: The Hilbert curve plays an important role
in image processing, multidimensional data index, and so on,
which is a space-ﬁlling curve mapping from one-dimensional
space to the two-dimensional space [79]. As shown in Fig. 6,
a space is divided into subspaces, and the Hilbert curve can
pass through all the subspaces. Fig. 6 shows the Hilbert curve
from ﬁrst order to fourth order.
The construction of Hilbert curve is an iteration of the order.
The curve is organized by straight lines, and always pass
through the center of subspaces. Each subspace is divided into
four subspaces in each iteration, such that the curve can have
better granularity after iteration. Finally, a curve covering the
entire space is formed, which provides the optimal trajectory
for the UAV to cover the area of data collection. In [63], a UAV
using delay tolerant network protocol is applied to realize data
collection in the large-area IoT scenarios without pre-deployed
network infrastructure. In particular, Liang et al. [63] apply the
path planning algorithm based on Hilbert curve to determine
the ﬂight path of UAV. The coordinates of sensors are applied
as one of the inputs of the algorithm. As shown in Fig. 7, the
trajectory generated by the algorithm based on Hilbert curve
can traverse all the cells where sensors are deployed and skip
the cells without sensors.
7UDMHFWRU\
6HQVRU
Fig. 7. Trajectory of UAV based on Hilbert curve.
B. Optimization Theory based Algorithms
In the problem of joint path planning and resource allocation
of UAV for data collection, the algorithms based on optimiza-
tion theory, such as dynamic programming (DP), branch and
bound, successive convex approximation (SCA), can ﬁnd the
optimal or suboptimal solution. However, for some NP-hard
problems, the time complexity is exponential and intolerable.
When the decision space is huge, the heuristic methods can
be applied to ﬁnd the feasible solution. Table VI and Table
VII compare the literatures using optimization theory based
algorithms.
1) Dynamic programming: DP is a nonlinear optimization
method proposed by Bellman [90]. DP transforms multi-stage
decision-making problem into a series of single-stage decision-

## Page 11

11
TABLE VII
COMPARISON OF OPTIMIZATION THEORY BASED ALGORITHMS
Algorithm
Reference
Objective function
Decision variables
AoCD
TE
EE
AoI
Successive
convex
approximation
[83]
Minimization of propulsion
energy consumption of
UAV.
Length and curvature of UAV
path.
×
×
√
×
[84]
Minimum-maximum energy
consumption of UAV and
sensors.
Communication scheduling
between UAV and sensors,
transmit power of sensors,
UAV path planning.
×
×
√
×
[58]
Weighted minimization of
energy consumption for
UAV and sensors.
UAV path planning, data
collection time, wake-up
scheduling of sensors.
×
√
√
×
[32]
Minimization of data
collection time.
Wake-up scheduling of
sensors, UAV path planning.
√
√
√
×
[85]
Maximum of minimum
data collection rate.
UAV time allocation, UAV
path planning.
√
√
√
×
[86]
Maximization of throughput
between UAV and sensors.
Resource allocation, UAV
path planning.
×
×
×
×
[10]
Minimization of ﬂight time
of UAV.
Resource allocation of
sensors, UAV path planning.
√
√
√
×
[87]
Maximization of power
transmission efﬁciency.
Power of the charging station,
UAV path planning,
communication scheduling
between of UAV and sensors.
×
×
√
×
[88]
Maximization of throughput
of air-to-ground networks.
Communication scheduling
between of UAV and sensors,
UAV path planning, transmit
power of sensor/UAV-CHs.
×
×
√
×
Matrix
completion
[89]
Minimization of energy
consumption of UAV and
redundant data.
Sampling point selection,
UAV path planning.
√
×
√
×
1 √denotes the existence of the feature, × denotes the absence of the feature
2 AoCD: Amount of collected data, TE: Time efﬁciency, EE: Energy efﬁciency, AoI: Age of information
making problems [91]. The optimal path can be obtained
recursively. According to the types of objective functions, the
DP based joint path planning and resource allocation methods
are summarized as follows.
• Minimization of ﬂight time of UAV
Minimizing the ﬂight time of UAV can fundamentally
reduce the energy consumption of UAV. The sensors are
deployed in a straight line in [35] and the trajectory of UAV is
divided into non-overlapping intervals for data collection. The
interval for data collection is optimized using DP to minimize
the ﬂight time of UAV. And the optimal speed of UAV and
transmit power of sensors are found. Furthermore, Gong et al.
[57] apply DP to optimize the partition of intervals.
• Minimization of AoI
In terms of the average AoI, taking AoI as objective function
is better than taking ﬂight time of UAV as optimization
objective. Especially when the sensor buffer is limited or
data is covered regularly, timely data collection becomes very
critical. Jia et al. [33] ﬁnd the best path for UAV by jointly
considering the access sequence of sensors and data collection
mode. A solution based on DP is proposed to determine the
optimal access sequence of sensors and minimize the average
AoI. Hu et al. [80] decompose the problem of minimizing the
average AoI of collected data into time allocation and energy
transfer problem, and trajectory of UAV optimization problem.
Different from other models considering that UAV has limited
energy and needs to be powered by a BS, Hu et al. [80] assume
that UAV acting as a mobile power source collects the data of
sensors and powers the sensors. However, the algorithms using
DP are complex and inefﬁcient when the number of sensors
is large.
• Minimization of maximum AoI or average AoI
Aiming at the problem of data collection with optimal AoI,
sensor association and path planning are jointly optimized to
reveal the optimal tradeoff between data transmission time of
sensors and the ﬂight time of UAV in [9]. It is veriﬁed that
the path maximizing AoI is the shortest Hamiltonian path.
When the number of data collection points, ﬂight path of UAV
and sensors scheduling are jointly optimized, maximum AoI
can be greatly reduced. Liu et al. [81] study the problem of
UAV assisted data collection based on AoI. On the basis of
determining the hover point and sensors access sequence of
UAV, they use DP to calculate optimal trajectories to minimize
the maximum AoI or average AoI.
2) Branch and bound: Branch and bound (BB) is a kind
of search and iteration method [92, 93]. BB decomposes the
given problem into sub-problems iteratively. The sub-problem
decomposing process is called branching. The boundary of the
sub-problem’s objective function is called the bound.
In order to collect data from as many sensors as possible

## Page 12

12
tx
1
+
tx
)
(x
f
(
)
;
SCA
t
g
x x
(
)
1
;
SCA
t
g
x x +
(a) The schematic diagram of SCA.
tx
1
+
tx
)
(x
f
(
)
;
MM
t
g
x x
(
)
1
;
MM
t
g
x x +
(b) The schematic diagram of MM.
Fig. 8. Comparison of MM and SCA for solving optimization problems.
and ensure a minimum amount of uploaded data per sensor,
Samir et al. [82] design a high-complexity branch, reduce
and bound (BRB) algorithm to ﬁnd the global optimal so-
lution in relatively small scale IoT. In the BRB algorithm,
a set of N non-overlapping hyper-rectangles that cover the
optimization problem of maximizing the number of served
sensors is maintained. The hyper-rectangle contains all feasible
solutions of the optimization model. And three operations,
namely, branching, reduction and bounding, are conducted for
each iteration in the BRB to improve the lower and upper
bounds of the objective function until the difference between
the lower and upper bounds is smaller than a predeﬁned
value. Accordingly, the hyper-rectangle is constantly reduced
to update the upper and lower bounds and remove the part that
does not meet the feasible solution.
3) Successive convex approximation: SCA transforms the
original nonconvex optimization problem into a series of
convex optimization problems which can be solved efﬁciently.
As shown in Fig. 8, the principle of SCA is similar to majorize-
minimize or minorize-maximize (MM), which can solve a
series of convex optimization problems similar to the original
problem iteratively [94, 95]. When the ﬁnal convergence
condition is satisﬁed, the solution is approximately regarded
as the solution of the original problem. MM requires that the
approximation function UMM(xt) is the upper bound of the
original function at the approximation point, which is one
feasible solution of objective function. Besides, SCA requires
that the approximation function USCA(xt) is convex. Then,
we summarize the SCA based joint path planning and resource
allocation methods according to the objective functions.
• Minimization of energy consumption
The path planning of UAV needs to take into account time
and energy consumption. Dong et al. [83] ﬁrstly propose a
mobility model for ﬁxed wing UAV, which is composed of
straight line segment and circle segment. And they apply
path discretization approach and SCA to optimize the straight
circular trajectory to minimize the propulsion energy con-
sumption of UAV on the premise of satisfying the throughput
requirements. Zhan and Lai [84] focus on the propulsion
energy model of rotary wing UAV. Under the premise of
limited UAV energy, they jointly optimize the communication
scheduling of sensors, transmit power allocation and trajectory
of UAV to minimize the maximum energy consumption of
UAV and sensors. For the non-convex problem, an efﬁcient
suboptimal solution by applying the alternating optimization
and SCA is proposed. In particular, Zhan and Huang [58]
reveal a basic trade-off between the energy consumption of
UAV and sensors. In [58], they optimize the trajectory of
UAV, data collection time and wake-up schedule to minimize
the weighted energy consumption of UAV and sensors. In
addition, SCA and block coordinate descent (BCD) techniques
are applied to obtain the local optimal solution.
• Maximization of ﬂight time of UAV
Zhan and Zeng [32] minimize the completion time of the
maximum task of multiple UAVs and ensure that the energy of
all sensors are sufﬁcient to upload data. By levering bisection
method and time discretization technique, the original problem
is transformed into a discrete equivalent problem, which con-
tains a ﬁnite number of optimization variables. And a Karush-
Kuhn-Tucker (KKT) solution is obtained by using SCA. In
[10], two orthogonal multiple access schemes, namely, TDMA
and frequency division multiple access (FDMA), are designed
and compared. Zong et al. use a binary search algorithm based
on SCA to minimize the completion time of data collection. It
is proved that the completion time in FDMA scheme is shorter
than that in TDMA scheme.
• Maximization of the amount of collected data
In [85], Luo et al. propose an efﬁcient iterative algorithm
to optimize the 3D path planning and time allocation for
UAV. The algorithm jointly utilizes epigraph equivalent rep-
resentation, variable substitution, equivalent representation by
using SCA. In addition, the combination of wireless power
transmission and data collection effectively solves the problem
of data collection with limited energy. In [96], considering
the velocity constraint of UAV, the corresponding transmission
scheduling and power allocation for sensors are designed by
applying BCD and SCA under the given initial trajectory.
• Maximization of throughput
With the goal of maximization of average throughput be-
tween UAV and sensors, Sun et al. [86] propose a two-
tier UAV communication strategy. In the ﬁrst tier of the
strategy, sensors transmit data to their CHs via a multi-channel
ALOHA-based random access scheme. And in the second
tier, CHs deliver the aggregated data to the UAV through
coordinated TDMA. A low complexity iterative algorithm
based on SCA is designed to jointly optimize the trajectory
and resource allocation of UAV. Under the constraints of UAV
mobility and transmit power of sensors or UAV, Hua et al. [88]
combine transmit power and communication scheduling of
sensor or UAV to maximize the total throughput of the system.
And they use SCA to obtain the global optimal solution and
suboptimal solution maximizing throughput, respectively.

## Page 13

13
Artificial intelligence based algorithms
Machine learning algorithms
Intelligent optimization algorithms
Supervised learning 
algorithms
Swarm intelligence based algorithms
Deep reinforcement 
learning algorithms
Regression 
algorithms
Simulated annealing 
algorithm
Individual behavior 
based algorithms
Reinforcement learning 
algorithms
Classification
algorithms
Q-learning 
algorithms
Genetic algorithm
Ant colony 
optimization
Particle swarm 
optimization
Differential evolution 
algorithm
Cuckoo search 
algorithm
Shuffled frog leaping 
algorithm
Fig. 9. Artiﬁcial intelligence based algorithms for joint path planing and resource allocation.
• Maximization of power transmission efﬁciency
Chen et al. [87] introduce the adaptive resonant beam
charging system to charge the UAV. In addition to ensuring
the quality of service, the power transmission efﬁciency is
maximized by jointly optimizing the trajectory of UAV and the
power of charging station. In particular, SCA and Dinkelbach
methods are used to deal with the problems of trajectory design
and power control, respectively.
4) Matrix completion method: Matrix completion uses the
observed matrix elements to estimate the unknown elements
and recover the entire matrix [97, 98]. These data matrices
are usually low rank, and there are some missing data. The
problem of low rank matrix completion is to predict those
missing data through the observed data and then recover the
matrix, using the low rank property of the matrix. Based on the
above characteristics, matrix completion method can be used
to select the UAV data sampling points and recover the missing
data. Because of the high correlation between the collected
data, even if the UAV only collects limited amount of data, it
can recover the data of the entire monitoring area by exploring
the data correlation [99, 100].
Matrix completion method is applied to guide UAV to select
data collection points from the perspective of time and space in
[89]. The data collected at different positions/times can form a
position/time matrix. Taking the location matrix as an example,
according to the number of selected sampling points in the row
of the sampling points in the location matrix, [89] dynamically
adjust the probability of the selected sampling points, which
effectively reduces the data redundancy. Based on the results
of matrix completion method, ant colony optimization (ACO)
is used to minimize the trajectory of UAV. According to the
path selection probability, the sampling points are gradually
selected by UAV until their number reaches a certain value.
C. Artiﬁcial Intelligence based Algorithms
Compared with the traditional algorithms, AI based algo-
rithms can deal with the uncertainty of path planning more
effectively and get the approximately optimal solution. AI
based the path planning algorithms are classiﬁed into machine
learning algorithms and intelligent optimization algorithms.
The detailed classiﬁcation is shown in Fig. 9.
1) Supervised learning: A machine learning algorithm is
able to acquire knowledge autonomously. According to learn-
ing methods, machine learning algorithms can be classiﬁed
into semi-supervised learning, unsupervised learning, super-
vised learning, ensemble learning, reinforcement learning (RL)
and deep learning (DL). Among them, supervised learning
and RL are widely used in UAV path planning. Table VIII
compares the literatures using supervised learning based algo-
rithms.
a) Classiﬁcation algorithms:
The classiﬁcation algo-
rithms mainly construct the classiﬁcation model in the labeled
training data, and then classify the new data based on this
model. In [101], the path planning problem is modeled as
a traveling salesman problem (TSP) with the neighborhood
(TSPN). And two trajectory design methods, segment-based
trajectory optimization algorithm (STOA) and group-based tra-
jectory optimization algorithm (GTOA), are proposed. STOA
calculates the visit order of all sensors and data collection
points. While GTOA divides all sensors into clusters and
calculates the visit order and locations based on clusters.
UAV only needs to pass through the cross region of common
transmission region of the grouped sensors. In particular, the
sensor that has the largest number of neighbor sensors is
selected as CH. The limited ﬂight time of UAV is a challenge
for data collection. Aiming to minimizing the total energy
consumption of sensors while ensuring data collection through
joint optimization of trajectory of UAV, data transmission
scheduling of sensors and transmit power. Zhao et al. [102]
innovatively use non-orthogonal multiple-access (NOMA) in
UAV data collection. In addition, the generalized benders
decomposition (GBD) is used to decouple sensers scheduling
and transmit power.
b) Regression algorithms: The regression algorithms ex-
tract features from the sample data and predict the continuous
target values corresponding to the new data. Chen et al. [43]
introduce the concept of measurement stream to transform the

## Page 14

14
TABLE VIII
COMPARISON OF SUPERVISED LEARNING BASED ALGORITHMS
Algorithm
Reference
Objective function
Decision variables
AoCD
TE
EE
AoI
Classiﬁcation
algorithm
[101]
Minimization of ﬂight time
of UAV.
Height and speed of UAV, link
scheduling, UAV path
planning.
×
√
×
×
[102]
Minimization of total
energy consumption of
sensors.
Transmission scheduling of
sensors, transmit power of
sensors, UAV path planning.
√
×
√
×
Regression
algorithm
[43]
Maximization of the
amount of data collected.
Clustering of sensors, value of
information (VoI), power of
sensors, UAV path planning.
√
×
√
×
1 √denotes the existence of the feature, × denotes the absence of the feature
2 AoCD: Amount of collected data, TE: Time efﬁciency, EE: Energy efﬁciency, AoI: Age of information
TABLE IX
COMPARISON OF Q-LEARNING BASED ALGORITHMS
Algorithm
Reference
Objective function
Decision variables
AoCD
TE
EE
AoI
Q-learning
[103]
Maximization of the
amount of data collected.
Time slot, UAV path planning.
√
√
×
×
[104]
Asymptotic minimization
of packet loss in IoT.
scheduling of microwave
power transfer (MPT) of UAV,
UAV path planning.
√
×
√
×
[40]
Minimization of data
expiration and loss.
UAV path planning.
√
×
×
√
[105]
Minimization of ﬂight path
length of UAV.
UAV collision avoidance,
UAV path planning.
×
√
×
×
[106]
Minimization of the total
energy consumption of
UAV.
The real-time amount of data
collected, the transmission
time between the UAV and
aerial BS, UAV path planning.
√
√
√
×
1 √denotes the existence of the feature, × denotes the absence of the feature
2 AoCD: Amount of collected data, TE: Time efﬁciency, EE: Energy efﬁciency, AoI: Age of information
traditional RL problem into a supervision learning problem.
On the premise of deﬁning VoI, [43] divides all sensors into
clusters, and determines the CHs and data forwarding rules
according to the power of sensors and VoI. Finally, the UAV
collects the aggregated data from CHs. And direct future
prediction (DFP) model is applied in the path planning of UAV,
so that UAV can deal with multi-objective tasks, maximizing
the VoI of collected data and ensuring the UAV charging.
2) Reinforcement learning algorithms: RL applies the in-
teraction with the environment to explore the mapping between
the optimal state and the action, and ﬁnally achieves an
optimal strategy and maximizes the cumulative revenue. The
training data of supervised learning is generally independent
with each other. However, RL deals with sequential decision-
making problems, which are dependent with each other in the
sequencing. RL is usually applied in obstacle avoidance and
path planning of UAV.
a) Q-learning algorithms: Q-learning is a model-free
RL algorithm using a time-series difference method, which
can carry out off-policy learning [117]. Q-learning selects
new actions and updates value function. Table IX compares
the literatures using Q-learning algorithms. We summarize Q-
learning based methods according to the optimization objec-
tives.
• Maximization of the amount of collected data and mini-
mization of data loss rate
On the premise that the sensor position is unknown, Cui et
al. model UAV path planning as a Markov decision process
(MDP) in [103], as well as divide the target area into multiple
identical rectangular cells. [103] proposes an RL problem to
maximize the cumulative amount of data collected and ﬁnd
the optimal trajectory of UAV. Two trajectory optimization
algorithms are proposed based on state-action-reward-state-
action and Q-learning so that the ﬂight path of UAV can be
optimized without the information on the network’s topology.
However, [103] does not consider energy consumption of
UAV and sensors and the packet loss of sensors. In this
regard, Li et al. [104] use UAV with microwave power transfer
(MPT) capability and propose a double-Q learning scheduling
algorithm, which jointly optimizes the schedule of MPT and
data collection without prior information on battery levels
and data queue lengths of sensors. This algorithm effectively
minimizes the packet loss of sensors in a long time. Facing
the requirement of time-sensitive data collection, Li et al. [40]
propose an RL method to obtain a minimum-maximum AoI
optimal path. And they combine AoI, the deadline constraints
of data and Q-learning to optimize the ﬂight path of UAV for
the ﬁrst time. The data loss rate is closely related to the ﬂight
time of UAV and the ﬂight order over sensors. The results

## Page 15

15
TABLE X
COMPARISON OF DEEP REINFORCEMENT LEARNING BASED ALGORITHMS
DRL method
Reference
Objective function
Decision variables
AoCD
TE
EE
AoI
Deep
Q-network
(Deep
Q-learning)
[107]
Minimization of the
weighted sum of AoI,
packet drop rate and the
energy consumption of
UAV.
Random or ﬁxed sampling,
buffer management, UAV
path planning.
√
×
√
√
[108]
Minimization of weighted
sum of AoI.
Transmission scheduling of
sensors, UAV path planning.
×
√
√
√
[109]
Minimization of buffer
overﬂow and transmission
failure of sensors.
Instantaneous waypoint of
UAV.
√
×
×
×
[110]
Minimization of the
average AoI.
Transmission scheduling and
energy harvesting of sensors,
UAV path planning.
×
×
√
√
[111]
Minimization of ﬂight path
length of UAV and
maximization of the
amount of data collected.
UAV path planning.
√
√
×
×
Deep
deterministic
strategy
gradient
[112]
Minimization of AoI under
minimum throughput
constraints.
Scheduling strategy of UAV,
UAV path planning.
×
×
×
√
[113]
Minimization of ﬂight time
of UAV.
Time window of data
collection, priority of
sensors, UAV path planning.
×
√
√
×
[114]
Long term freshness of
UAV situation awareness.
Resource allocation, UAV
path planning.
×
×
√
√
[115]
Minimization of the
weighted sum of expected
AoI, propulsion energy
consumption of UAV and
energy consumption of
sensors.
Hovering points and ﬂight
speed of UAV, transmission
scheduling of sensors.
×
×
√
√
Proximal
policy
optimization
[116]
UAV crowdsensing.
The number of UAV and
charging station, UAV path
planning.
×
×
√
×
1 √denotes the existence of the feature, × denotes the absence of the feature
2 AoCD: Amount of collected data, TE: Time efﬁciency, EE: Energy efﬁciency, AoI: Age of information
show that the optimization method based on RL has low time
consumption and data loss rate.
• UAV collision avoidance and minimization of energy
consumption
Facing the possible collision of multiple UAVs in data
collection, Hsu and Gau [105] focus on the collision avoidance
algorithm based on RL to obtain an optimal trajectory of UAV.
Considering the inﬂuence of limited energy and communica-
tion resources on ﬂight endurance and data collection of UAV,
Ni et al. [106] use an RL algorithm to optimize the real-time
ﬁeld data size collected by the on-board camera, transmission
time between UAV and aerial BS, ﬂight path of UAV, so as
to minimize the total energy consumption of UAV during data
collection.
b) Deep reinforcement learning algorithms:
DL has
strong perception, but it lacks decision-making ability. RL has
the ability of decision-making, but it lacks perceptual ability.
The combination of them, namely, the deep reinforcement
learning (DRL), can complement each other and decide the
action to maximize revenue [118]. Using DPL to solve the
joint optimization problem is also the cutting-edge scheme of
UAV assisted data collection. We compare the literatures using
DRL algorithms in Table X and summarize them according to
the objective functions as follows.
• Minimization of AoI
Modeling DPL problem as MDP is a common method for
simpliﬁcation. [107, 108, 110] all apply a DRL algorithm
called deep Q-network (DQN) to achieve the optimal strategy
and effectively overcome the disaster of dimensionality. In
[107], the data collection problem is modeled as an MDP
with ﬁnal state and action space. Further, the weighted sum
of AoI, packet loss rate and energy consumption of UAV is
minimized by optimizing the ﬂight path of UAV. Yi et al.
[108] establish a MDP to ﬁnd the best ﬂight path of UAV and
the transmission scheduling of sensors, so as to minimize the
weighted sum of AoI. Liu et al. [110] establish an MDP with
large state spaces to minimize the average AoI, and the ﬂight
path of UAV, transmission scheduling and energy harvesting
of sensors are jointly optimized. The simulation results show
that the increase of ﬂight time of UAV/transmit power or the
decrease of the packet size will reduce the average AoI.
In [112], the UAV assisted vehicular network is considered,

## Page 16

16
Fig. 10. Illustration of ant colony seeking optimal path in foraging.
where UAVs are used to collect and process the data of
sensors. Samir et al. develop the deep deterministic strategy
gradient (DDPG) to process the trajectory and the scheduling
policy of UAVs to minimize the expected weighted sum of
AoI. In order to minimize the weighted sum of AoI and the
number of sensors as well as energy consumption of UAV,
Sun et al. [115] comprehensively consider the data collection
points, ﬂight speed and bandwidth allocation of UAVs.
• UAV collision avoidance and minimization of data trans-
mission failure rate
In order to avoid the possible collisions among UAVs when
collecting data from IoT, Liu et al. [116] transforms the
problem of UAV collision avoidance into a partially observable
MDP and present a DRL model named “j-PPO+ConvNTM”.
The model can make continuous (path planning) and dis-
crete (data collection and charging) decisions for all UAVs.
To minimize the buffer overﬂow probability of sensors and
transmission failure due to the path loss of air-ground channel,
Li et al. [109] propose a path planning algorithm named Deep
Reinforcement Learning based Trajectory Planning. Consider-
ing the battery levels and buffer lengths of sensors, the location
of UAV and channel conditions, a DRL algorithm is applied
in the path planning of UAV to minimize the data loss.
• Maximization of the amount of collected data
Considering the limited energy and ﬂight time of UAV,
Nguyen et al. [111] take minimizing the ﬂight path and
maximizing the amount of collected data as the optimization
objectives. Through the deep Q-learning and dueling DQL,
the UAV can independently decide the next action at each
position, so as to obtain a 3D trajectory that can balance the
performance of throughput, data collection time and length
of ﬂight path. In [119], adopting the full duplex mode, UAV
collects data and charges the sensors within its coverage
while hovering. A multi-objective optimization problem is
proposed, including maximizing the sum data rate and the
total harvested energy of sensors as well as minimizing the
energy consumption of UAV. The UAV realizes online path
planning through a DRL algorithm based on DDPG.
• Minimization of data collection time
Bouhamed et al. [113] use a combination algorithm of
DDPG and Q-learning to minimize data collection time.
Furthermore, DDPG is used to realize UAV autonomous
navigation in the environment with obstacles, while Q-learning
is used to determine the task arrangement of UAV to complete
data collection as soon as possible.
• Minimization of energy consumption
To minimize the energy consumption of UAV, Fan et
al. [114] present a freshness function based on AoI and a
DRL algorithm that can solve the continuous online decision-
making problem involving multiple UAVs. In the rapidly
changing environment, the algorithm can markedly reduce
energy consumption and AoI.
3) Intelligent optimization algorithms: Intelligent optimiza-
tion algorithms are the combination of random search and local
search. In the process of intelligent optimization algorithm,
learning strategies are used to obtain the information to effec-
tively ﬁnd the approximately optimal solution. Then, through
a comprehensive searching algorithm, the superiority of the
solution is improved.
a) Individual behavior based algorithms: Individual be-
havior based algorithms ﬁrstly initialize a feasible solution.
Then, the algorithm optimize this feasible solution and proba-
bilistically jump out of local optimum to search the near global
optimal solution. Taking simulated annealing (SA) algorithm
as an example, it is often used to search the approximately
global optimal solution in a large solution space. Different
from genetic algorithm (GA), simulated annealing algorithm
has the feature of probabilistic jumping out of local optimum,
which can accelerate path planning. Table XI compares the
literatures using intelligent optimization algorithms.
With a goal of improving the energy efﬁciency of UAV, Liu
et al. [120] propose a path planning scheme of UAV based on
matrix completion and SA. Firstly, the sampling points with
degrees from high to low are selected as dominator sampling
points, virtual dominator sampling points and follower sam-
pling points. And all data in the monitoring area is recovered
by matrix completion. Then, based on the number and location
of selected sampling points, SA is used to determine the visit
order of each sampling point. The proposed scheme can reduce
the data redundancy by 50% and extend the network lifetime
of sensors by 17% compared with the scheme using random
sampling point.
b) Swarm intelligence based algorithms: Swarm intelli-
gence algorithms consists of GA, ACO, particle swarm opti-
mization (PSO), differential evolution (DE) algorithm, shufﬂed
frog leaping algorithm (SFLA), cuckoo search (CS) algorithm.
They applied a large amount of individuals to mimic the
solutions. Then, the learning and evolution mechanisms are
applied to improve the superiority of solutions.
• Genetic algorithm
GA simulates the process of biological evolution. A solution
to the problem is expressed as a chromosome. The algorithm

## Page 17

17
TABLE XI
COMPARISON OF INTELLIGENT OPTIMIZATION BASED ALGORITHMS
Algorithm
Reference
Objective function
Decision variables
AoCD
TE
EE
AoI
Simulated
annealing
[120]
Maximization of UAV
energy utilization.
UAV path planning, sampling
points.
√
×
√
×
Genetic
algorithm
[27]
Minimization of ﬂight time
of UAV.
The number of UAV, the
number and location of CHs,
UAV path planning.
×
√
×
×
[121]
Minimization of energy
consumption of UAV
hovering and
communication.
MTCDs clustering, UAV
hovering point, UAV path
planning.
×
×
√
×
[122]
Minimization of energy
consumption of UAV.
UAV path planning.
×
√
√
×
Ant colony
optimization
[31]
Maximization of the
per-node capacity of UAV.
The number of UAV and
service cell, UAV path
planning.
√
×
×
×
[123]
Minimization of ﬂight cost
of UAV.
Clustering of sensors, UAV
path planning.
×
×
√
×
Particle swarm
optimization
[124]
Minimization of energy
consumption of UAV.
Battery capacity, network
quality of service (QoS), area
coverage, UAV path planning.
×
×
√
×
Differential
evolution
[125]
Minimum-maximum the
energy consumption of
UAV, BSs and sensors.
Devices transmission
schedule, UAV path planning.
×
√
√
×
[126]
Minimization of data
collection time.
The selection of CHs, UAV
path planning.
×
√
×
×
Shufﬂed frog
leaping
[127]
Minimization of energy
consumption of UAV.
Data collection time, UAV
path planning.
×
×
√
×
Cuckoo search
[59]
Minimization of energy
consumption of UAV and
sensors.
UAV path planning, UAV
hovering point.
×
×
√
×
1 √denotes the existence of the feature, × denotes the absence of the feature
2 AoCD: Amount of collected data, TE: Time efﬁciency, EE: Energy efﬁciency, AoI: Age of information
obtains the most suitable chromosome through the operations
of population reproduction, crossover, and mutation, so as to
obtain the optimal solution.
To solve the path planning problem of UAV, Alfattani et al.
[27] ﬁrstly optimize the number and locations of CHs. Then,
GA is applied to optimize the number and paths of UAVs to
minimize the data collection time. Shen et al. [121] convert the
path planning problem of UAV into a TSP, which is then solved
by GA with a goal of minimizing the energy consumption of
UAV and sensors. Joseph et al. [122] propose GA based path
planning of UAV, which minimizes energy consumption of
sensors and UAV under the data ofﬂoading time windows and
communication constraints.
• Ant colony optimization
As shown in Fig. 10, ACO simulates the process that ants
ﬁnd the shortest path during foraging. An ant is regarded
as a solution of the path planning problem. Ants spread the
pheromone during path searching process and the optimal path
accumulates the most pheromone [128]. Thus, the ants are
guided to the optimal path, namely, the optimal scheme is
searched. In addition, the diversity of ant colony can avoid
local optimization.
Aiming at maximizing the per-node capacity of UAV and
the amount of collected data, Wei et al. [31] adjust the number
of UAVs and service cells, and design two path planning algo-
rithms. Among them, the ACO based path planning algorithm
can minimize the time of data collection time and achieve
the per-node capacity closer to its theoretical upper bound.
Lin et al. [123] use precise algorithm and GA to achieve a
hierarchical sensor data collection scheme. A path planning
algorithm based on ACO is used to improve the scheme to
minimize the energy consumption of UAV.
• Particle swarm optimization
PSO originated from the study of birds foraging. Using
information sharing mechanism, individuals learn from each
other to ﬁnd food faster [129]. PSO has great advantages in
dealing with continuous optimization problems.
In generally, data retrieving and processing are carried out
when UAV completes data collection. In these cases, Shi and
Xu [124] propose a path planning problem with the constraint
called network quality of service (QoS). For the NP hard
problem, a PSO based algorithm is used to minimize the ﬂight
time of multiple UAVs.
• Differential evolution algorithm
Similar to GA, DE is a kind of intelligent optimization
search through the cooperation and competition among indi-
viduals in the population [130]. It has strong global conver-
gence performance and robustness, which is mainly used to

## Page 18

18
solve global optimization problems with continuous variables.
Wang et al. [125] study data collection and 3D positioning
of sensors. As a mobile data collector and aerial anchor
node, UAV assists BSs to realize sensor positioning and data
collection of sensors far away from BSs. A DE Algorithm
is proposed to optimize UAV path and transmission priority
of sensors to minimize-maximize the energy consumption of
UAV, sensors and BSs. And the Cram´er-Rao Bound (CRB)
is derived to evaluate the performance of the algorithm. The
ﬁnal path in the optimization scheme reduces the energy
consumption of UAV by 32%. With the selection of optimal
CHs and clustering of sensors, Chawra and Gupta [126]
propose a meta-heuristic method based on DE to estimate the
delay effective path of each UAV to minimize data collection
time. The algorithm consists of four steps including initial
population generation, mutation, crossover and selection.
• Shufﬂed frog leaping algorithm
SFLA simulates the information sharing and communication
of frogs in foraging. It combines the advantages of the memetic
algorithm (MA) and PSO [131].
In [127], Kong et al. propose an energy efﬁcient algorithm
for data collection in sparse sensor network. The improved
SFLA is used to further optimize the location and traversal
order of data collection points. Then, these orderly data
collection points are used to plan the UAV path with minimum
energy consumption of UAV. However, the obstacles in the
environment are not considered in this paper.
• Cuckoo search algorithm
CS algorithm simulates the unique breeding behavior of
cuckoo parasitic brood and lvy ﬂight search mechanism to ﬁnd
the optimal solution. It has a better searching performance than
GA and PSO algorithm. In the path planning problem, CS can
accurately search the global optimal path in a path planning
area with fast speed.
Aiming at minimizing the energy consumption of UAV and
sensors, Zhu et al. [59] propose a hybrid hover location selec-
tion algorithm based on a non-service-tolerance mechanism,
which ensures that a few highly scattered MTCDs are directly
served by the BS to reduce the trajectory length of UAV. On
this basis, a path planning method based on CS is proposed
to jointly optimize the energy consumption and throughput of
UAV, the latency of MTCDs and data collection efﬁciency.
VI. FUTURE TRENDS
It is revealed from the above literature review that most
literatures focus on the clustering algorithm of sensors and
the path planning algorithm of UAV in order to achieve
high efﬁciency, low energy consumption and low delay data
collection. However, the following two challenges have not
attracted sufﬁcient attention.
• In the large-scale IoT, a large amount of sensors transmit
data to UAV, which leads to data congestion.
• UAV assisted data collection may be carried out without
the knowledge of the locations of sensors.
For example, in the scenario of ocean monitoring, there are
many buoy sensors widely distributed on the sea surface [132],
which may lead to transmission conﬂicts between competing
6ROXWLRQ*RDO
5HDOL]HGDWDFROOHFWLRQZLWKKLJKHIILFLHQF\ORZ
HQHUJ\FRQVXPSWLRQDQGORZGHOD\
-RLQWVHQVLQJDQG
GDWDFROOHFWLRQ
-RLQWSDWKSODQQLQJDQGUHVRXUFHDOORFDWLRQ
&OXVWHULQJRI
VHQVRUV
(IILFLHQWDFFHVV
RIODUJHVFDOH
VHQVRUV
(IILFLHQWURXWLQJ
LQ:61
2SWLPL]DWLRQ
0HFKDQLVP
.H\
7HFKQRORJLHV
6\VWHPPRGHODQGSHUIRUPDQFHDQDO\VLVIRUGDWD
FROOHFWLRQ
7KHRUHWLFDO
6XSSRUW
Fig. 11. Scheme of UAV assisted data collection.
sensors. In addition, due to insufﬁcient communication cov-
erage of coastal BSs and high positioning costs such as GPS
positioning, it is difﬁcult to obtain the locations of sensors in
advance. Similar scenarios include agricultural monitoring and
soil monitoring [22–24]. Therefore, we propose a complete
solution for UAV assisted data collection in Fig. 11. Joint
sensing and data collection, clustering of sensors, efﬁcient
access of large-scale sensors and efﬁcient routing in WSN
are introduced as key technologies, and joint path planning
and resource allocation are applied to provide optimization
mechanism with these key technologies.
In the future, we need to focus on but not limited to the
following two research trends.
A. Efﬁcient Multiple Access
MAC protocol is designed to satisfy the performance re-
quirements of the network, including solving the potential
transmission conﬂicts between competing sensors, reducing
the average packet delay, increasing network throughput, sup-
porting the access of a large number of sensors, balancing
energy consumption of UAV and sensors, and so on. The
efﬁcient multiple access between UAV and sensors has a
crucial impact on the efﬁciency of data collection and the
freshness of data.
In [12], the performance of MAC protocol is improved by
scheduling resources in the dimensions of time, frequency and
space. Sotheara et al. [133] divide the coverage area of UAV
into priorities, and sensors access channels according to the
priorities of their own regions to reduce transmission conﬂicts.
Due to the limitation of bandwidth, the performance of MAC
protocol will reach the bottleneck, especially when the number
of sensors is large. The ISM (Industrial, Scientiﬁc and Med-
ical) bands including license-free communication frequencies
173 MHz, 433 MHz, 868 MHz and 915 MHz and 2.4 GHz
are commonly applied to WSN [134]. In order to expand
the bandwidth of WSN, 800/900/1800/2100 MHz of 4G (4th
generation mobile communication system) [135] and 5.15-5.85
GHz band of Wi-Fi [136] are also provided for WSN. The

## Page 19

19
8$9
:RUVW3RVLWLRQIRU
6HQVRUWR8$9
'DWD7UDQVPLVVLRQ
r0
Fig. 12. Data collection with uncertain position of sensor.
application of mmWave in 5G-A (5G Advanced) and Teraherz
(THz) in 6G will solve the problem of spectrum shortage
[137, 138], which has great potential in providing high data
rate and low latency for WSN, providing opportunities for the
design of efﬁcient MAC protocol.
When the number of sensors is huge, bandwidth and
scheduling schemes cannot always satisfy the requirements
of fast and efﬁcient access to channels. In this situation, the
NOMA technique is promising to further improve the efﬁ-
ciency of MAC protocol [12, 139]. The combination of UAVs
and NOMA can deﬁnitely provide high spectral efﬁciency and
support massive connectivity in IoT scenarios [140]. To the
best of our knowledge, the investigation on the application
of NOMA in UAV data collection is still in its infancy stage
[132, 141]. In order to better exploit both the mobility of the
UAV and the efﬁciency of NOMA to improve the UAV assisted
data collection performance in ocean observation networks,
Chen et al. [132] formulated a joint optimization problem
of the location of UAV, sensor grouping, and power control
in terms of sum rate. When the number of sensors is large,
their scheme is able to select sensors with less interference
to access the channel, improving the overall performance.
Different from [132], the UAV only allows a limited number
of nearby devices to be connected to the uplink NOMA
network in each time slot, leading to better LoS and successive
interference cancelation (SIC) with lower complexity in [141].
Mu et al. [142] deploy an intelligent reﬂecting surface (IRS)
to enhance the transmission from UAVs to their intended users
while mitigating the interference caused to other unintended
users. However, the SIC decoding technology of NOMA may
bring large delay, which needs to be solved when designing the
NOMA based MAC protocol in the scenario of UAV assisted
data collection.
B. Joint Sensing and Data Collection
Sensors are usually randomly distributed in the target area.
Most of the existing technologies that support positioning are
not suitable for UAV assisted data collection. For example, the
cost of installing GNSS chips in a large number of sensors
is too high [143]. And the energy consumption of GNSS
positioning is high. Therefore, the position information of
sensors is generally unknown before data collection. The joint
sensing and data collection technology enables the UAV to
locate sensors while data collection, as well as satisfying the
requirements of low cost and low energy consumption of the
IoT.
However, few literatures take sensing and data collection
into consideration together in the scenario of UAV assisted
data collection. In order to minimize the maximum energy
consumption of all sensors, Wang et al. [125] apply a UAV
as mobile anchor node and data collector to assist BSs in
sensor positioning and data collection. A differential evolution
algorithm is proposed to jointly optimize the trajectory of
UAV and the transmission schedule of sensors over time. This
paper provides a new scheme for the IoT, which realizes low-
energy data collection and high-precision 3D positioning. At
present, there are many separate studies of UAV assisted sensor
positioning and UAV assisted data collection.
1) UAV assisted sensor positioning: Due to the ﬂexibility
of ﬂight, UAV can select the appropriate position, adjust the
posture, and locate the sensors in the target area from different
angles, which effectively improves the positioning accuracy.
In [144], Xu et al. design a target location algorithm based
on Unscented Kalman ﬁlter (UKF) to improve the accuracy
of passive target location of small UAV. The nonlinear target
location system with additive white Gaussian noise (AWGN) is
considered. The simulation results show that the mean square
deviation of the ﬁlter estimation error has approached the
Cramer-Rao lower bound of the nonlinear system. Han et
al. [145] propose an autonomous navigation system based
on Microcontroller in [144], which obtains the 3D position
of the target through the mathematical relationship between
the UAV and the ground target. This method signiﬁcantly
improves the accuracy and conﬁdence of measurement. Xu et
al. [146] propose a positioning method combining maximum
likelihood estimation (MLE) and square root volume Kalman
ﬁlter (SRVKF). The MLE method is applied to locate the
unknown sensors. The SRVKF algorithm is then introduced
to further improve the positioning accuracy. In particular, the
update strategy of threshold selection is used to reduce the
inﬂuence of nonlinear factors. This method not only improves
the positioning accuracy, but also greatly reduces the cost of
loading GPS module. In the process of perceptual positioning,
data loss or error is inevitable. Due to the uncertainty of
wireless signal propagation, Li et al. [147] propose an adaptive
positioning algorithm combining packet loss rate and received
signal strength indicator (RSSI). It makes up for the measure-
ment error without increasing the cost of wireless nodes.
2) UAV assisted data collection: For UAV assisted data
collection, most studies are carried out under the assumption
that the sensor position is known. Generally, key performance
indicators such as energy consumption of UAV and sensors,
ﬂight time of UAV and AoI will be taken as the objective func-
tions of data collection algorithm. Zhan et al. [36] consider the
general fading channel model between UAV and sensors and
jointly optimize the sensors’ wake-up schedule and trajectory
of UAV with the goal of minimizing the maximum energy
consumption of all sensors. In [148], You and Zhang initially
optimize the communication scheduling of sensors and 3D
trajectory of UAV in Rician Fading Channel to improve
the data collection efﬁciency. Due to lacking the value of
effective fading power, the parameters are approximated by

## Page 20

20
logic function and solved by BCD and SCA. Han et al. [149]
take AoI as an index to reveal the freshness of data, and
analyze the single IoT device model and the multi-sensor
model respectively with ﬁrst come ﬁrst service (FCFS) M/M/1
queuing model. In addition, Markov chain is used to predict
the amount of collected data and packet loss rate, so as to
collect data more efﬁciently.
In the future, low-power sensing and data collection need to
be carried out simultaneously. Meanwhile, because the process
of positioning is easily affected by the external environment
[150, 151], data collection algorithms with missing location
information of sensors or positioning results with large errors
need to be designed. Facing the positioning errors, the model
of positioning uncertainty is considered in [125]. The initially
estimated position coordinates of sensors are taken as the
sketchy prior information. Then, the uncertain space of each
sensor position is modeled as a sphere with initially estimated
position as the center of the sphere. As shown in Fig. 12, it
is assumed that the sensor is located furthest from the UAV.
B-Spline curves based UAV path is designed, which makes
sensors complete the reliable data transmission under the worst
data transmission conditions.
VII. CONCLUSION
In this paper, we summarize the scenarios and related
technologies of UAV assisted data collection for IoT. The key
technologies are reviewed including clustering of SNs, UAV
data collection mode, and joint path planning and resource
allocation. Hovering mode, ﬂying mode and hybrid mode of
UAV are considered. In terms of joint path planning and
resource allocation, according to the optimization algorithms
used, we review the literatures from the perspectives of graph
theory based algorithms, optimization theory based algorithms
and AI based algorithms. Finally, we discuss the future trends
from two aspects, i.e, efﬁcient multiple access as well as
joint sensing and data collection. This article may provide a
reference for the research of UAV assisted data collection for
IoT.
ACKNOWLEDGMENTS
The authors appreciate editor and anonymous reviewers for
their precious time and great effort in improving this paper.
REFERENCES
[1] Ehret and Michael, “The zero marginal cost society:
The internet of things, the collaborative commons, and
the eclipse of capitalism,” The Journal of Sustainable
Mobility, vol. 2, no. 2, pp. 67–70, 2015.
[2] S. Liu, Z. Wei, Z. Guo, X. Yuan, and Z. Feng, “Perfor-
mance analysis of uavs assisted data collection in wire-
less sensor network,” IEEE 87th Vehicular Technology
Conference (VTC Spring), pp. 1–5, 2018.
[3] Z. Wei, Z. Feng, H. Zhou, L. Wang, and H. Wu, “Ca-
pacity and delay of unmanned aerial vehicle networks
with mobility,” IEEE Internet of Things Journal, vol. 6,
no. 2, pp. 1640–1653, 2019.
[4] Y. Pang, Y. Zhang, Y. Gu, M. Pan, Z. Han, and P. Li,
“Efﬁcient data collection for wireless rechargeable sen-
sor clusters in harsh terrains using uavs,” IEEE Global
Communications Conference, pp. 234–239, 2014.
[5] R. J. Dobson, C. Brooks, C. Roussi, and T. Colling,
“Developing an unpaved road assessment system for
practical deployment with high-resolution optical data
collection using a helicopter uav,” International Confer-
ence on Unmanned Aircraft Systems (ICUAS), pp. 235–
243, 2013.
[6] B. Zhang, C. H. Liu, J. Tang, Z. Xu, J. Ma, and
W. Wang, “Learning-based energy-efﬁcient data col-
lection by unmanned vehicles in smart cities,” IEEE
Transactions on Industrial Informatics, vol. 14, no. 4,
pp. 1666–1676, 2018.
[7] I. Cermakova and J. Komarkova, “Modelling a process
of uav data collection and processing,” International
Conference on Information Society (i-Society), pp. 161–
164, 2016.
[8] C. M. de A. Lima, E. A. da Silva, and P. B. Velloso,
“Performance evaluation of 802.11 iot devices for data
collection in the forest with drones,” IEEE Global
Communications Conference (GLOBECOM), pp. 1–7,
2018.
[9] P. Tong, J. Liu, X. Wang, B. Bai, and H. Dai, “Uav-
enabled age-optimal data collection in wireless sensor
networks,” IEEE International Conference on Commu-
nications Workshops (ICC Workshops), pp. 1–6, 2019.
[10] J. Zong, C. Shen, J. Cheng, J. Gong, T.-H. Chang,
L. Chen, and B. Ai, “Flight time minimization via uavs
trajectory design for ground sensor data collection,”
16th International Symposium on Wireless Communi-
cation Systems (ISWCS), pp. 255–259, 2019.
[11] Z. Wei, X. Liu, C. Han, and Z. Feng, “Neighbor
discovery for unmanned aerial vehicle networks,” IEEE
Access, vol. 6, pp. 68 288–68301, 2018.
[12] S. Poudel and S. Moh, “Medium access control proto-
cols for unmanned aerial vehicle-aided wireless sensor
networks: A survey,” IEEE Access, vol. 7, pp. 65 728–
65 744, 2019.
[13] J. Baek, S. I. Han, and Y. Han, “Optimal uav route in
wireless charging sensor networks,” IEEE Internet of
Things Journal, vol. 7, no. 2, pp. 1327–1335, 2020.
[14] Z. Wei, H. Wu, S. Huang, and Z. Feng, “Scaling laws of
unmanned aerial vehicle network with mobility pattern
information,” IEEE Communications Letters, vol. 21,
no. 6, pp. 1389–1392, 2017.
[15] B. Li, Z. Fei, and Y. Zhang, “Uav communications for
5g and beyond: Recent advances and future trends,”
IEEE Internet of Things Journal, vol. 6, no. 2, pp. 2241–
2263, 2019.
[16] M. Heaphy, M. S. Watt, J. P. Dash, and G. D.
Pearse, “Uavs for data collection-plugging the gap,”
New Zealand Journal of Forestry, vol. 62, no. 1, pp.
23–30, 2017.
[17] H. Q. Pham, M. Camey, K. D. Pham, K. V. Pham,
and L. R. Rilett, Review of Unmanned Aerial Vehicles
(UAVs) Operation and Data Collection for Driving

## Page 21

21
Behavior Analysis.
CIGOS 2019, Innovation for
Sustainable Infrastructure, 2020.
[18] P. Dan, F. Stoican, G. Stamatescu, O. Chenaru, and
L. Ichim, “A survey of collaborative uavwsn systems
for efﬁcient monitoring,” Sensors (Basel, Switzerland),
vol. 19, no. 21, 2019.
[19] X. Yang, S. Fu, B. Wu, and M. Zhang, “A survey
of key issues in uav data collection in the internet of
things,” IEEE Intl Conf on Dependable, Autonomic and
Secure Computing, Intl Conf on Pervasive Intelligence
and Computing, Intl Conf on Cloud and Big Data
Computing, Intl Conf on Cyber Science and Technology
Congress (DASC/PiCom/CBDCom/CyberSciTech), pp.
410–413, 2020.
[20] A. Moheddine, F. Patrone, and M. Marchese, “Uav
and iot integration: A ﬂying gateway,”
26th IEEE
International Conference on Electronics, Circuits and
Systems (ICECS), pp. 121–122, 2019.
[21] V. Delafontaine, F. Schiano, G. Cocco, A. Rusu, and
D. Floreano, “Drone-aided localization in lora iot net-
works,”
IEEE International Conference on Robotics
and Automation (ICRA), pp. 286–292, 2020.
[22] G. Castellanos, M. Deruyck, L. Martens, and W. Joseph,
“System assessment of wusn using nb-iot uav-aided
networks in potato crops,” IEEE Access, vol. 8, pp.
56 823–56836, 2020.
[23] H. Sui, G. Zheng, J. Zhou, H. Li, and Z. Gu, “Appli-
cation of nb-iot technology in city open water moni-
toring,”
6th International Symposium on System and
Software Reliability (ISSSR), pp. 95–98, 2020.
[24] Z. Hu, Z. Bai, Y. Yang, Z. Zheng, K. Bian, and
L. Song, “Uav aided aerial-ground iot for air quality
sensing in smart city: Architecture, technologies, and
implementation,” IEEE Network, vol. 33, no. 2, pp. 14–
22, 2019.
[25] A. T. Albu-Salih and S. A. H. Seno, “Energy-efﬁcient
data gathering framework-based clustering via multiple
uavs in deadline-based wsn applications,” IEEE Access,
vol. 6, pp. 72 275–72286, 2018.
[26] M. B. Ghorbel, D. Rodrguez-Duarte, H. Ghazzai, M. J.
Hossain, and H. Menouar, “Joint position and travel
path optimization for energy efﬁcient wireless data
gathering using unmanned aerial vehicles,” IEEE Trans-
actions on Vehicular Technology, vol. 68, no. 3, pp.
2165–2175, 2019.
[27] S. Alfattani, W. Jaafar, H. Yanikomeroglu, and A. Yon-
gacoglu, “Multi-uav data collection framework for wire-
less sensor networks,” IEEE Global Communications
Conference (GLOBECOM), pp. 1–6, 2019.
[28] J. Grigulo and L. B. Becker, “Experimenting sen-
sor nodes localization in wsn with uav acting as
mobile agent,”
IEEE 23rd International Conference
on Emerging Technologies and Factory Automation
(ETFA), vol. 1, pp. 808–815, 2018.
[29] A. Filippone, “Flight performance of ﬁxed and rotary
wing aircraft,” CA, 2006.
[30] J. Wang, C. Jiang, Z. Wei, C. Pan, H. Zhang, and
Y. Ren, “Joint uav hovering altitude and power control
for space-air-ground iot networks,” IEEE Internet of
Things Journal, vol. 6, no. 2, pp. 1741–1753, 2019.
[31] Z. Wei, Q. Chen, S. Liu, and H. Wu, “Capacity of
unmanned aerial vehicle assisted data collection in
wireless sensor networks,” IEEE Access, vol. 8, pp.
162 819–162829, 2020.
[32] C. Zhan and Y. Zeng, “Completion time minimization
for multi-uav-enabled data collection,” IEEE Transac-
tions on Wireless Communications, vol. 18, no. 10, pp.
4859–4872, 2019.
[33] Z. Jia, X. Qin, Z. Wang, and B. Liu, “Age-based
path planning and data acquisition in uav-assisted iot
networks,” IEEE International Conference on Commu-
nications Workshops (ICC Workshops), pp. 1–6, 2019.
[34] J. Gong, T.-H. Chang, C. Shen, and X. Chen, “Flight
time minimization of uav for data collection over wire-
less sensor networks,” IEEE Journal on Selected Areas
in Communications, vol. 36, no. 9, pp. 1942–1954,
2018.
[35] X. Mu, Y. Liu, L. Guo, J. Lin, and Z. Ding, “Energy-
constrained uav data collection systems: Noma and
oma,” IEEE Transactions on Vehicular Technology,
vol. 70, no. 7, pp. 6898–6912, 2021.
[36] C. Zhan, Y. Zeng, and R. Zhang, “Energy-efﬁcient
data collection in uav enabled wireless sensor network,”
IEEE Wireless Communications Letters, vol. 7, no. 3,
pp. 328–331, 2018.
[37] R. D. Yates, Y. Sun, D. R. Brown, S. K. Kaul, E. Modi-
ano, and S. Ulukus, “Age of information: An introduc-
tion and survey,” IEEE Journal on Selected Areas in
Communications, vol. 39, no. 5, pp. 1183–1210, 2021.
[38] Z. Fang, J. Wang, C. Jiang, Q. Zhang, and Y. Ren, “Aoi-
inspired collaborative information collection for auv-
assisted internet of underwater things,” IEEE Internet
of Things Journal, vol. 8, no. 19, pp. 14 559–14571,
2021.
[39] Z. Fang, J. Wang, Y. Ren, Z. Han, H. V. Poor, and
L. Hanzo, “Age of information in energy harvesting
aided massive multiple access networks,” IEEE Journal
on Selected Areas in Communications, vol. 40, no. 5,
pp. 1441–1456, 2022.
[40] W. Li, L. Wang, and A. Fei, “Minimizing packet expi-
ration loss with path planning in uav-assisted data sens-
ing,” IEEE Wireless Communications Letters, vol. 8,
no. 6, pp. 1520–1523, 2019.
[41] S. Kaul, R. Yates, and M. Gruteser, “Real-time status:
How often should one update?”
Proceedings IEEE
INFOCOM, pp. 2731–2735, 2012.
[42] M. Costa, M. Codreanu, and A. Ephremides, “On the
age of information in status update systems with packet
management,” IEEE Transactions on Information The-
ory, vol. 62, no. 4, pp. 1897–1910, 2016.
[43] J. Chen, F. Yan, S. Mao, F. Shen, W. Xia, Y. Wu, and
L. Shen, “Efﬁcient data collection in large-scale uav-
aided wireless sensor networks,”
11th International
Conference on Wireless Communications and Signal
Processing (WCSP), pp. 1–5, 2019.
[44] D. Ebrahimi, S. Sharafeddine, P.-H. Ho, and C. Assi,

## Page 22

22
“Data collection in wireless sensor networks using
uav and compressive data gathering,”
IEEE Global
Communications Conference (GLOBECOM), pp. 1–7,
2018.
[45] P. Sujit, D. Lucani, and J. Sousa, “Joint route planning
for uav and sensor network for data retrieval,”
IEEE
International Systems Conference (SysCon), pp. 688–
692, 2013.
[46] Q. Wu, P. Sun, and A. Boukerche, “Unmanned
aerial vehicle-assisted energy-efﬁcient data collection
scheme for sustainable wireless sensor networks,” Com-
puter networks, vol. 165, no. Dec.24, pp. 106 927.1–
106 927.11, 2019.
[47] S. K. Haider, M. A. Jamshed, A. Jiang, H. Pervaiz, and
Q. Ni, “Uav-assisted cluster-head selection mechanism
for wireless sensor network applications,”
UK/China
Emerging Technologies (UCET), pp. 1–2, 2019.
[48] L. Xu, R. Collier, and G. M. P. OHare, “A survey of
clustering techniques in wsns and consideration of the
challenges of applying such to 5g iot scenarios,” IEEE
Internet of Things Journal, vol. 4, no. 5, pp. 1229–1249,
2017.
[49] H. E. Xiao-Yu and Y. X. Yao, “Survey of clustering
algorithms for wireless sensor networks,” Computer
Knowledge and Technology, 2017.
[50] S. K. Singh, P. Kumar, and J. P. Singh, “A survey on
successors of leach protocol,” IEEE Access, vol. 5, pp.
4298–4328, 2017.
[51] J. Gnanambigai, D. N. Rengarajan, and K. Anbukkarasi,
“Leach and its descendant protocols: A survey.”
[52] A. Kaur and A. Grover, “Leach and extended leach
protocols in wireless sensor network-a survey,” Inter-
national Journal of Computer Applications, vol. 116,
no. 10, pp. 1–5, 2015.
[53] G. N. Basavaraj and C. D. Jaidhar, “H-leach protocol
with modiﬁed cluster head selection for wsn,”
Inter-
national Conference On Smart Technologies For Smart
Nation (SmartTechCon), pp. 30–33, 2017.
[54] Y. Chen and S. Shen, “A uav-based data collection
approach for wireless sensor network,”
7th Interna-
tional Conference on Information Science and Control
Engineering (ICISCE), pp. 2298–2302, 2020.
[55] G. Wang, B.-S. Lee, and J. Y. Ahn, “Uav-assisted cluster
head election for a uav-based wireless sensor network,”
IEEE 6th International Conference on Future Internet
of Things and Cloud (FiCloud), pp. 267–274, 2018.
[56] O. M. Bushnaq, A. Celik, H. Elsawy, M.-S. Alouini, and
T. Y. Al-Naffouri, “Aeronautical data aggregation and
ﬁeld estimation in iot networks: Hovering and traveling
time dilemma of uavs,” IEEE Transactions on Wireless
Communications, vol. 18, no. 10, pp. 4620–4635, 2019.
[57] J. Gong, T.-H. Chang, C. Shen, and X. Chen, “Aviation
time minimization of uav for data collection from
energy constrained sensor networks,”
IEEE Wireless
Communications and Networking Conference (WCNC),
pp. 1–6, 2018.
[58] C. Zhan and R. Huang, “Energy minimization for data
collection in wireless sensor networks with uav,” IEEE
Global Communications Conference (GLOBECOM),
pp. 1–6, 2019.
[59] K. Zhu, X. Xu, and S. Han, “Energy-efﬁcient uav
trajectory planning for data collection and computation
in mmtc networks,” IEEE Globecom Workshops (GC
Wkshps), pp. 1–6, 2018.
[60] J. Baek, S. I. Han, and Y. Han, “Energy-efﬁcient uav
routing for wireless sensor networks,” IEEE Transac-
tions on Vehicular Technology, vol. 69, no. 2, pp. 1741–
1750, 2020.
[61] Y. Wang, X. Wen, Z. Hu, Z. Lu, J. Miao, C. Sun,
and H. Qi, “Multi-uav collaborative data collection
for iot devices powered by battery,”
IEEE Wireless
Communications and Networking Conference (WCNC),
pp. 1–6, 2020.
[62] R. Pnika, J. Faigl, and M. Saska, “Physical orienteer-
ing problem for unmanned aerial vehicle data collec-
tion planning in environments with obstacles,” IEEE
Robotics and Automation Letters, vol. 4, no. 3, pp.
3005–3012, 2019.
[63] H. Liang, W. Gao, J. H. Nguyen, M. F. Orpilla, and
W. Yu, “Internet of things data collection using un-
manned aerial vehicles in infrastructure free environ-
ments,” IEEE Access, vol. 8, pp. 3932–3944, 2020.
[64] Y. S. Jiao, X. M. Wang, H. Chen, and Y. Li, “Research
on the coverage path planning of uavs for polygon
areas,” in Industrial Electronics & Applications, 2010.
[65] C. Qiu, Z. Wei, Z. Feng, and P. Zhang, “Backhaul-aware
trajectory optimization of ﬁxed-wing uav-mounted base
station for continuous available wireless service,” IEEE
Access, vol. 8, pp. 60 940–60950, 2020.
[66] X. Yuan, Z. Feng, W. Xu, W. Ni, J. A. Zhang, Z. Wei,
and R. P. Liu, “Capacity analysis of uav communica-
tions: Cases of random trajectories,” IEEE Transactions
on Vehicular Technology, vol. 67, no. 8, pp. 7564–7576,
2018.
[67] X. Chen and X. Chen, “The uav dynamic path planning
algorithm research based on voronoi diagram,” The 26th
Chinese Control and Decision Conference (CCDC), pp.
1069–1071, 2014.
[68] W. T. Zhao and J. Y. Peng, “Voronoi diagram-based
path planning for uavs,” Journal of System Simulation,
2006.
[69] Y. Zhou, H. Zhao, and Y. Liu, “An evaluative review
of the vtol technologies for unmanned and manned
aerial vehicles,” Computer Communications, vol. 149,
no. Jan., pp. 356–369, 2020.
[70] Qiang, Du, Faber, and Vance, “Centroidal voronoi tes-
sellations: Applications and algorithms.” Siam Review,
1999.
[71] T. Nishida, S. Ono, and K. Sugihara, “Direct diffusion
method for the construction of generalized voronoi
diagrams,” 4th International Symposium on Voronoi
Diagrams in Science and Engineering (ISVD), pp. 145–
151, 2007.
[72] M. Berg, M. Kreveld, and M. H. Overmars, Com-
putational Geometry: Algorithms and Applications.
Computational Geometry: Algorithms and Applications,

## Page 23

23
2008.
[73] Y. Eun and H. Bang, “Cooperative task assignment/path
planning of multiple unmanned aerial vehicles using
genetic algorithm,” Journal of Aircraft, vol. 46, no. 1,
pp. 338–343, 2012.
[74] Y. V. Pehlivanoglu, “A new vibrational genetic al-
gorithm enhanced with a voronoi diagram for path
planning of autonomous uav,” Aerospace Science and
Technology, vol. 16, no. 1, pp. 47–55, 2012.
[75] S. Meguerdichian, F. Koushanfar, M. Potkonjak, and
M. B. Srivastava, “Coverage problems in wireless ad-
hoc sensor networks,” INFOCOM. Twentieth Annual
Joint Conference of the IEEE Computer and Communi-
cations Societies. Proceedings. IEEE, 2001.
[76] D. Hsu, “On the probabilistic foundations of prob-
abilistic roadmap planning,” International Journal of
Robotics Research, vol. 25, no. 7, pp. 83–97, 2007.
[77] R. Geraerts and M. Overmars, A comparitive study of
probabilistic roadmap planners, 2003.
[78] A.
A.
Ravankar,
A.
Ravankar,
T.
Emaru,
and
Y. Kobayashi, “Hpprm: Hybrid potential based prob-
abilistic roadmap algorithm for improved dynamic path
planning of mobile robots,” IEEE Access, vol. 8, pp.
221 743–221766, 2020.
[79] L. Xian, “Four alternative patterns of the hilbert curve,”
Applied Mathematics and Computation, vol. 147, no. 3,
pp. 741–752, 2004.
[80] H. Hu, K. Xiong, G. Qu, Q. Ni, P. Fan, and K. B.
Letaief, “Aoi-minimal trajectory planning and data col-
lection in uav-assisted wireless powered iot networks,”
IEEE Internet of Things Journal, vol. 8, no. 2, pp. 1211–
1223, 2021.
[81] J. Liu, P. Tong, X. Wang, B. Bai, and H. Dai, “Uav-
aided data collection for information freshness in wire-
less sensor networks,” IEEE Transactions on Wireless
Communications, vol. 20, no. 4, pp. 2368–2382, 2021.
[82] M. Samir, S. Sharafeddine, C. M. Assi, T. M. Nguyen,
and A. Ghrayeb, “Uav trajectory planning for data col-
lection from time-constrained iot devices,” IEEE Trans-
actions on Wireless Communications, vol. 19, no. 1, pp.
34–46, 2020.
[83] F. Dong, L. Li, Z. Lu, Q. Pan, and W. Zheng, “Energy-
efﬁciency for ﬁxed-wing uav-enabled data collection
and forwarding,”
IEEE International Conference on
Communications Workshops (ICC Workshops), pp. 1–
6, 2019.
[84] C. Zhan and H. Lai, “Energy minimization in internet-
of-things system based on rotary-wing uav,” IEEE Wire-
less Communications Letters, vol. 8, no. 5, pp. 1341–
1344, 2019.
[85] W. Luo, Y. Shen, B. Yang, S. Wang, and X. Guan,
“Joint 3-d trajectory and resource optimization in multi-
uav-enabled iot networks with wireless power transfer,”
IEEE Internet of Things Journal, vol. 8, no. 10, pp.
7833–7848, 2021.
[86] Z. Sun, Z. Wei, N. Yang, and X. Zhou, “Two-tier
communication for uav-enabled massive iot systems:
Performance analysis and joint design of trajectory and
resource allocation,” IEEE Journal on Selected Areas in
Communications, vol. 39, no. 4, pp. 1132–1146, 2021.
[87] W. Chen, S. Zhao, Q. Shi, and R. Zhang, “Resonant
beam charging-powered uav-assisted sensing data col-
lection,” IEEE Transactions on Vehicular Technology,
vol. 69, no. 1, pp. 1086–1090, 2020.
[88] M. Hua, L. Yang, Q. Wu, and A. L. Swindlehurst,
“3d uav trajectory and communication design for si-
multaneous uplink and downlink transmission,” IEEE
Transactions on Communications, vol. 68, no. 9, pp.
5908–5923, 2020.
[89] X. Liu, H. Song, and A. Liu, “Intelligent uavs trajectory
optimization from space-time for data collection in so-
cial networks,” IEEE Transactions on Network Science
and Engineering, vol. 8, no. 2, pp. 853–864, 2021.
[90] M. L. Puterman, “Dynamic programming,” Encyclo-
pedia of Physical Science and Technology (Third
Edition), third edition ed., R. A. Meyers, Ed.
New
York: Academic Press, pp. 673–696, 2003.
[91] A. MOKRANE, A. C. BRAHAM, and B. CHERKI,
“Uav path planning based on dynamic programming
algorithm on photogrammetric dems,”
International
Conference on Electrical Engineering (ICEE), pp. 1–5,
2020.
[92] E. K. Lee, “Branch-and-bound methods,” Handbook of
Applied Optimization, 2002.
[93] J. Binney and G. S. Sukhatme, “Branch and bound
for informative path planning,”
IEEE International
Conference on Robotics and Automation, pp. 2147–
2154, 2012.
[94] Y. Sun, P. Babu, and D. P. Palomar, “Majorization-
minimization
algorithms
in
signal
processing,
communications,
and
machine
learning,”
IEEE
Transactions on Signal Processing, vol. 65, no. 3, pp.
794–816, 2017.
[95] T. Wang and L. Vandendorpe, “Successive convex
approximation based methods for dynamic spectrum
management,”
IEEE International Conference on
Communications (ICC), pp. 4061–4065, 2012.
[96] J. Zhang, Y. Zeng, and R. Zhang, “Multi-antenna uav
data harvesting: Joint trajectory and communication
optimization,”
Journal
of
Communications
and
Information Networks, vol. 5, no. 1, pp. 86–99,
2020.
[97] M. Huang, K. Zhang, Z. Zeng, T. Wang, and Y. Liu,
“An auv-assisted data gathering scheme based on
clustering and matrix completion for smart ocean,”
IEEE Internet of Things Journal, vol. 7, no. 10, pp.
9904–9918, 2020.
[98] J. He, G. Sun, Y. Zhang, and Z. Wang, “Data
recovery
in
wireless
sensor
networks
with
joint
matrix completion and sparsity constraints,” IEEE
Communications Letters, vol. 19, no. 12, pp. 2230–
2233, 2015.
[99] A.
Singh,
S.
Garg,
S.
Batra,
N.
Kumar,
and
J. Rodrigues, “Bloom ﬁlter based optimization scheme
for massive data handling in iot environment,” Future
Generation Computer Systems, vol. 82, no. MAY, pp.

## Page 24

24
440–449, 2017.
[100] K. Jin, X. Cheng, X. Ge, and X. Yin, “Three
dimensional modeling and space-time correlation for
uav channels,”
IEEE 85th Vehicular Technology
Conference (VTC Spring), pp. 1–5, 2017.
[101] J. Li, H. Zhao, H. Wang, F. Gu, J. Wei, H. Yin,
and B. Ren, “Joint optimization on trajectory, altitude,
velocity, and link scheduling for minimum mission
time in uav-aided data collection,” IEEE Internet of
Things Journal, vol. 7, no. 2, pp. 1464–1475, 2020.
[102] J. Zhao, Y. Wang, Z. Fei, X. Wang, and Z. Miao,
“Noma-aided uav data collection system: Trajectory
optimization and communication design,” IEEE Access,
vol. 8, pp. 155 843–155858, 2020.
[103] J. Cui, Z. Ding, Y. Deng, A. Nallanathan, and
L. Hanzo, “Adaptive uav-trajectory optimization under
quality of service constraints: A model-free solution,”
IEEE Access, vol. 8, pp. 112 253–112265, 2020.
[104] K. Li, W. Ni, B. Wei, and E. Tovar, “Onboard double
q-learning for airborne data capture in wireless powered
iot networks,” IEEE Networking Letters, vol. 2, no. 2,
pp. 71–75, 2020.
[105] Y.-H. Hsu and R.-H. Gau, “Reinforcement learning-
based
collision
avoidance
and
optimal
trajectory
planning
in
uav
communication
networks,”
IEEE
Transactions on Mobile Computing, pp. 1–1, 2020.
[106] W. Ni, H. Tian, S. Fan, and G. Nie, “Optimal
transmission
control
and
learning-based
trajectory
design for uav-assisted detection and communication,”
IEEE
31st
Annual
International
Symposium
on
Personal, Indoor and Mobile Radio Communications,
pp. 1–6, 2020.
[107] P. Tong, J. Liu, X. Wang, B. Bai, and H. Dai, “Deep
reinforcement learning for efﬁcient data collection in
uav-aided internet of things,”
IEEE International
Conference
on
Communications
Workshops
(ICC
Workshops), pp. 1–6, 2020.
[108] M. Yi, X. Wang, J. Liu, Y. Zhang, and B. Bai,
“Deep reinforcement learning for fresh data collection
in uav-assisted iot networks,” IEEE INFOCOM - IEEE
Conference on Computer Communications Workshops
(INFOCOM WKSHPS), pp. 716–721, 2020.
[109] K.
Li,
W.
Ni,
E.
Tovar,
and
M.
Guizani,
“Deep reinforcement learning for real-time trajectory
planning in uav networks,”
International Wireless
Communications and Mobile Computing (IWCMC), pp.
958–963, 2020.
[110] L. Liu, K. Xiong, J. Cao, Y. Lu, P. Fan, and K. B.
Letaief, “Average aoi minimization in uav-assisted
data collection with rf wireless power transfer: A
deep reinforcement learning scheme,” IEEE Internet of
Things Journal, vol. 9, no. 7, pp. 5216–5228, 2022.
[111] K. K. Nguyen, T. Q. Duong, T. Do-Duy, H. Claussen,
and L. Hanzo, “3d uav trajectory and data collection
optimisation via deep reinforcement learning,” IEEE
Transactions on Communications, pp. 1–1, 2022.
[112] M. Samir, C. Assi, S. Sharafeddine, D. Ebrahimi,
and A. Ghrayeb, “Age of information aware trajectory
planning of uavs in intelligent transportation systems:
A deep learning approach,” IEEE Transactions on
Vehicular Technology, vol. 69, no. 11, pp. 12 382–
12 395, 2020.
[113] O. Bouhamed, H. Ghazzai, H. Besbes, and Y. Massoud,
“A uav-assisted data collection for wireless sensor
networks: Autonomous navigation and scheduling,”
IEEE Access, vol. 8, pp. 110 446–110460, 2020.
[114] W. Fan, K. Luo, S. Yu, Z. Zhou, and X. Chen, “Aoi-
driven
fresh
situation
awareness
by
uav
swarm:
Collaborative
drl-based
energy-efﬁcient
trajectory
control and data processing,” IEEE/CIC International
Conference on Communications in China (ICCC), pp.
841–846, 2020.
[115] M. Sun, X. Xu, X. Qin, and P. Zhang, “Aoi-energy-
aware uav-assisted data collection for iot networks: A
deep reinforcement learning method,” IEEE Internet
of Things Journal, vol. 8, no. 24, pp. 17 275–17289,
2021.
[116] C. H. Liu, C. Piao, and J. Tang, “Energy-efﬁcient
uav crowdsensing with multiple charging stations by
deep learning,” IEEE INFOCOM - IEEE Conference
on Computer Communications, pp. 199–208, 2020.
[117] K.-S. Hwang and Y.-J. Chen, “An adaptive state
aggregation approach to q-learning with real-valued
action function,”
IEEE International Conference on
Systems, Man and Cybernetics, pp. 164–170, 2010.
[118] Y. Li, S. Zhang, F. Ye, T. Jiang, and Y. Li, “A uav
path planning method based on deep reinforcement
learning,”
IEEE USNC-CNC-URSI North American
Radio Science Meeting (Joint with AP-S Symposium),
pp. 93–94, 2020.
[119] Y. Yu, J. Tang, J. Huang, X. Zhang, D. K. C.
So, and K.-K. Wong, “Multi-objective optimization
for uav-assisted wireless powered iot networks based
on extended ddpg algorithm,” IEEE Transactions on
Communications, vol. 69, no. 9, pp. 6361–6374, 2021.
[120] X. Liu, Y. Liu, N. Zhang, W. Wu, and A. Liu,
“Optimizing trajectory of unmanned aerial vehicles
for efﬁcient data acquisition: A matrix completion
approach,” IEEE Internet of Things Journal, vol. 6,
no. 2, pp. 1829–1840, 2019.
[121] L. Shen, N. Wang, Z. Zhu, Y. Fan, X. Ji, and X. Mu,
“Uav-enabled data collection for mmtc networks: Aem
modeling and energy-efﬁcient trajectory design,” IEEE
International Conference on Communications (ICC),
pp. 1–6, 2020.
[122] J. Joseph, M. Radmanesh, M. N. Sadat, R. Dai,
and M. Kumar, “Uav path planning for data ferrying
with communication constraints,”
IEEE 17th Annual
Consumer Communications Networking
Conference
(CCNC), pp. 1–9, 2020.
[123] C. Lin, G. Han, X. Qi, J. Du, T. Xu, and M. Martnez-
Garca, “Energy-optimal data collection for unmanned
aerial vehicle-aided industrial wireless sensor network-
based agricultural monitoring system: A clustering
compressed sampling approach,” IEEE Transactions on
Industrial Informatics, vol. 17, no. 6, pp. 4411–4420,

## Page 25

25
2021.
[124] L. Shi and S. Xu, “Uav path planning with qos
constraint
in
device-to-device
5g
networks
using
particle swarm optimization,” IEEE Access, vol. 8, pp.
137 884–137896, 2020.
[125] Z. Wang, R. Liu, Q. Liu, J. S. Thompson, and
M.
Kadoch, “Energy-efﬁcient data
collection
and
device positioning in uav-assisted iot,” IEEE Internet
of Things Journal, vol. 7, no. 2, pp. 1122–1139, 2020.
[126] V. K. Chawra and G. P. Gupta, “Multiple uav path-
planning for data collection in cluster-based wireless
sensor network,”
First International Conference on
Power, Control and Computing Technologies (ICPC2T),
pp. 194–198, 2020.
[127] B. Kong, H. Huang, and X. Jia, “Path planning
for sensor data collection by using uavs,”
14th
International
Conference
on
Mobile
Ad-Hoc
and
Sensor Networks (MSN), pp. 199–205, 2018.
[128] M. Dorigo and L. M. Gambardella, “Ant colonies for
the traveling salesman problem,” Biosystems, vol. 43,
no. 2, pp. 73–81, 1997.
[129] J.
Kennedy
and
R.
Eberhart,
“Particle
swarm
optimization,” in Icnn95-international Conference on
Neural Networks, 2002.
[130] S. Das and P. N. Suganthan, “Differential evolution: A
survey of the state-of-the-art,” IEEE Transactions on
Evolutionary Computation, vol. 15, no. 1, pp. 4–31,
2011.
[131] O. Bozorg-Haddad, M. Solgi, and H. Loiciga, Shufﬂed
Frog-Leaping Algorithm, 2017.
[132] W. Chen, S. Zhao, R. Zhang, Y. Chen, and L. Yang,
“Uav-assisted
data
collection
with
nonorthogonal
multiple access,” IEEE Internet of Things Journal,
vol. 8, no. 1, pp. 501–511, 2021.
[133] S. Sotheara, N. Aomi, T. Ando, L. Jiang, N. Shiratori,
and S. Shimamoto, “Effective data gathering protocol in
wsn-uav employing priority-based contention window
adjustment scheme,” IEEE Globecom Workshops (GC
Wkshps), pp. 1475–1480, 2014.
[134] S. K. Gupta and P. Sinha, “Overview of wireless sensor
network: a survey,” Telos, vol. 3, no. 15µW, p. 38mW,
2014.
[135] Rashmi, Sharan, Sinha, Yiqiao, Wei, Seung-Hoon, and
Hwang, “A survey on lpwa technology: Lora and nb-iot
- sciencedirect,” ICT Express, vol. 3, no. 1, pp. 14–21,
2017.
[136] M. Ayyash, H. Elgala, A. Khreishah, V. Jungnickel,
T. Little, S. Shao, M. Rahaim, D. Schulz, J. Hilt,
and R. Freund, “Coexistence of wiﬁand liﬁtoward
5g: concepts, opportunities, and challenges,” IEEE
Communications Magazine, vol. 54, no. 2, pp. 64–71,
2016.
[137] D.-T.
Ho
and
S.
Shimamoto,
“Highly
reliable
communication protocol for wsn-uav system employing
tdma and pfs scheme,” IEEE GLOBECOM Workshops
(GC Wkshps), pp. 1320–1324, 2011.
[138] D.-T. Ho, J. Park, and S. Shimamoto, “Performance
evaluation of the pfsc based mac protocol for wsn
employing uav in rician fading,”
IEEE Wireless
Communications
and
Networking
Conference,
pp.
55–60, 2011.
[139] X. Zhu, C. Jiang, L. Kuang, N. Ge, and J. Lu, “Non-
orthogonal multiple access based integrated terrestrial-
satellite networks,” IEEE Journal on Selected Areas
in Communications, vol. 35, no. 10, pp. 2253–2267,
2017.
[140] Y.
Liu,
Z.
Qin,
Y.
Cai,
Y.
Gao,
G.
Y.
Li,
and
A.
Nallanathan, “Uav
communications based
on non-orthogonal multiple access,” IEEE Wireless
Communications, vol. 26, no. 1, pp. 52–57, 2019.
[141] W. Wang, N. Zhao, L. Chen, X. Liu, Y. Chen,
and
D.
Niyato,
“Uav-assisted
time-efﬁcient
data
collection via uplink noma,” IEEE Transactions on
Communications, vol. 69, no. 11, pp. 7851–7863, 2021.
[142] X.
Mu,
Y.
Liu,
L.
Guo,
J.
Lin,
and
H.
V.
Poor, “Intelligent reﬂecting surface enhanced multi-uav
noma networks,” IEEE Journal on Selected Areas in
Communications, vol. 39, no. 10, pp. 3051–3066, 2021.
[143] X.
Lin,
J.
Bergman, F.
Gunnarsson, O.
Liberg,
S. M. Razavi, H. S. Razaghi, H. Rydn, and Y. Sui,
“Positioning
for
the
internet
of
things:
A
3gpp
perspective,” IEEE Communications Magazine, vol. 55,
no. 12, pp. 179–185, 2017.
[144] C. Xu, D. Huang, and F. Kong, “Small uav passive
target localization approach and accuracy analysis,”
Chinese Journal of Scientiﬁc Instrument, no. 05, pp.
1115–1122, 2015.
[145] D. I. Han, J. H. Kim, C. O. Min, S. J. Jo, J. H.
Kim, and D. W. Lee, “Development of unmanned
aerial vehicle (uav) system with waypoint tracking and
vision-based reconnaissance,” International Journal of
Control Automation & Systems, vol. 8, no. 5, pp.
1091–1099, 2010.
[146] W. Xu, G. Wang, and M. Chen, “Node localization of
wireless sensor networks based on SR-CKF assisted
by unmanned aerial vehicles,” CAAI Transactions on
Intelligent Systems, 2019.
[147] F. Li, P. Han, and T. Luo, “Adaptive area location
algorithm combining with packet lost rate and RSSI in
wireless sensor networks,” Journal on Communications,
vol. 30, no. 9, pp. 15–23, 2009.
[148] C. You and R. Zhang, “3d trajectory optimization in
rician fading for uav-enabled data harvesting,” IEEE
Transactions on Wireless Communications, vol. 18,
no. 6, pp. 3192–3207, 2019.
[149] R. Han, J. Wang, L. Bai, J. Liu, and J. Choi, “Age
of information and performance analysis for uav-aided
iot systems,” IEEE Internet of Things Journal, vol. 8,
no. 19, pp. 14 447–14457, 2021.
[150] G. Zaho, B. Liu, and C. Gao, “Moving horizon
estimation of uav with random parameter ncertainty and
data missing,” Systems Engineering and Electronics,
vol. 041, no. 012, pp. 2849–2854, 2019.
[151] P. Wang, P. Yao, and Y. Nie, “Distributed uav formation
cooperative control with measurement noise and data
packet loss,” 4th China Conference on Command and

## Page 26

26
Control.
