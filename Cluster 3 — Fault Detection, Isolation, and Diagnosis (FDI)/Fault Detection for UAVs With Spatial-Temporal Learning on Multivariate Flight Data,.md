# Fault Detection for UAVs With Spatial-Temporal Learning on Multivariate Flight Data,.pdf

## Page 1

IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 73, 2024
2529517
Fault Detection for UAVs With Spatial-Temporal
Learning on Multivariate Flight Data
Shengdong Wang , Zhenbao Liu , Senior Member, IEEE, Zhen Jia , Yong Tang, Guozhu Zhi, and Xiao Wang
Abstract— Precise fault detection is essential to enhance the
safety and reliability of unmanned aerial vehicle (UAV) system.
With poor generalization capability, model-based approaches
are greatly restricted by excessive dependence on aircrafts’
dynamics. In this study, a novel data-driven method, spatial-
temporal graph attention Transformer network (ST-GATrans),
is proposed to implement intelligent fault detection of UAVs
through joint spatial-temporal learning on multivariate flight
data. In the designed architecture, an enhanced graph attention
network (EGAT) with graph multiheaded self-attention (GMSA)
is first designed to excavate deep spatial connections inherent
in the high-dimensional multivariate flight data. After estab-
lishing the spatial association among different status variables,
one transformer encoder combining multiheaded self-attention
(MSA) and convolutional token fusion (CTF) is developed to mine
more comprehensive temporal features, whereby MSA enables
to model long time dependencies and the CTF operation can
capture indispensable local details. By modeling the spatial-
temporal connections, the future values of multivariate flight
data can be predicted precisely. The occurrence of faults will
be detected by judging if the residual between predicted value
and ground truth exceeds the predefined threshold. To eliminate
the negative impact of noise or large fluctuations in flight
data, a bidirectional adaptive exponential weighted moving aver-
age (Bi-AEWMA) method is proposed to smooth the residual
sequence and determine the fault threshold. Effectiveness of the
proposed methodology is verified on the collected real flight data.
In different fault sceneries, the accuracy (ACC), true positive
rate (TPR), and area under curve (AUC) of our approach can
reach above 96%, 97%, and 0.98, respectively. The comparative
experimental results demonstrate that our approach can obtain
better fault detection performance.
Index Terms— Anomaly detection, fault detection, flight data
mining, graph attention network (GAT), self-attention mecha-
nism, unmanned aerial vehicle (UAV).
I. INTRODUCTION
W
ITH the dramatic development of drone technologies
in recent years, unmanned aerial vehicles (UAVs)
have been widely applied in both military and civil domains
due to their exceptional maneuverability, high flexibility, and
Manuscript received 28 May 2024; revised 30 June 2024; accepted
12 July 2024. Date of publication 2 September 2024; date of current version
17 September 2024. This work was supported in part by the National
Natural Science Foundation Fund under Grant 52072309 and in part by the
Key Research and Development Program of Shaanxi Province under Grant
2019ZDLGY14-02-01. The Associate Editor coordinating the review process
was Dr. Lei Mao. (Corresponding author: Zhenbao Liu.)
The
authors
are
with
the
School
of
Civil
Aviation,
Northwestern
Polytechnical University, Xi’an 710072, China (e-mail: shengdongwang123@
foxmail.com;
liuzhenbao@nwpu.edu.cn;
jiazhen@mail.nwpu.edu.cn;
lzh0608@mail.nwpu.edu.cn; qxshang@mail.nwpu.edu.cn; wangxiao@nwpu.
edu.cn).
Digital Object Identifier 10.1109/TIM.2024.3440387
cost-effectiveness [1], [2], [3]. However, under the influence of
harsh operating conditions and persistent environmental stress,
the malfunctions of UAVs are inevitable which may induce
significant financial losses and human casualties [4], [5].
Compared to human-piloted aircrafts, UAVs have reduced
safety and reliability because there is no real-time status
monitoring and emergency operation from pilots. According
to statistics, the accident rate of UAVs is much higher than
that of manned aircraft [6], [7]. Therefore, it is crucial to
conduct precise fault detection for UAV systems to enhance
their security, reliability, and maintainability.
Generally, the fault detection schemes for UAV systems can
be roughly divided into two categories including model-based
and data-based methods. The model-based methodologies
include parameter estimation, equivalence space, and state
estimation approaches in which accurate dynamic modeling
for UAV systems or its subsystems are required [2], [8], [9],
[10], [11], [12]. However, with the increasing integration and
complexity of UAV architectures, high-fidelity failure models
are generally cumbersome to be established, which limits the
application of the model-based approaches to a certain degree.
In contrast to the model-based approaches, data-driven
approaches do not require to establish precise dynamic models
and can recognize faulty status through mining potential status
information from the collected massive flight data. The flight
data of UAV consists of a variety of indicators closely related
to the system status [13]. To complete the flight mission
more effectively and safely, the modern UAVs are equipped
with a growing number of sensors to monitor their working
status in real time, including the gyroscope, accelerometer,
barometer, magnetometer, global positioning system (GPS),
and so on. Hence, composed of a series of control commands
and flight status variables collected by sensors, the multivariate
time series flight data will have significant high-dimensional
characteristics.
As one of the most popular data-driven approaches, deep
learning technology flourished in recent years possesses
prominent feature learning capabilities and can automatically
excavate health information from massive collected data with
its deep network architecture [4], [13]. As a kind of special
time series data, multivariate flight data have significant
temporal characteristics. Thereby, time-oriented deep learning
methods including long short-term memory (LSTM) network,
temporal convolutional neural networks (TCNNs), and some
their variants have been applied to extract these temporal
features [14], [15], [16], [17], [18], [19]. Wang et al. [14]
1557-9662 © 2024 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:14:40 UTC from IEEE Xplore.  Restrictions apply.

## Page 2

2529517
IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 73, 2024
proposed
a
LSTM-based
multivariate
regression
model
to realize fault detection and data recovery for UAVs.
Sadhu et al. [15] combined bidirectional LSTM with con-
volutional operations to recognize the possible malfunctions
of UAV systems. Guo et al [16] applied short-time Fourier
transformation to convert the residual sequences into time-
frequency maps and introduced CNN to discriminate the UAV
sensor faults. In literature [17], one multioutput convolutional
LSTM (Conv-LSTM) is implemented to identify UAV sensor
faults by detecting the anomalies in multivariate flight data.
In literature [18], TCNN was employed to realize intelligent
detection for UAV sensor faults. However, the abovementioned
methods mainly focus on the temporal characteristics of mul-
tivariate flight data. Since UAV is an integrated intelligent
system, the flight status variables collected from different
components or subsystems will be interconnected with each
other. Hence, only extracting temporal features of flight data
is insufficient. It is essential to enhance the fault detection
performance by modeling the spatial correlation within the
multivariate flight data.
To address this issue, in this study, graph neural network
(GNN) is first introduced to capture the spatial characteristics
inherent in multivariate flight data. GNN is a kind of net-
work for processing graph structure data [20]. In GNN, each
node’s information is associated with that of its neighboring
nodes. In our methodology, the status variables in multivariate
flight data can be regarded as different graph nodes, and
thus, the spatial connection between any two flight variables
can be described by the weight of their edge. Eventually,
a novel data-driven method named spatial-temporal graph
attention transformer network (ST-GATrans) is proposed to
implement intelligent fault detection for UAVs through joint
spatial-temporal learning on multivariate flight data. In the
designed architecture, an enhanced graph attention network
(EGAT) with graph multiheaded self-attention (GMSA) is first
developed to mine deep spatial connections within the flight
data. Subsequently, a transformer encoder integrated with mul-
tiheaded self-attention (MSA) and convolutional token fusion
(CTF) operation is designed to excavate more comprehensive
temporal information. Since the multivariate time series flight
data are highly complex, LSTM and its extensive meth-
ods have some difficulty in capturing long-time associations
and modeling global temporal representations. Compared to
LSTM, MSA can model long-time dependencies of time-
series data from a global perspective [21], [22]. With the
help of convolution operation, CTF can capture more detail
information and facilitate MSA to extract more comprehensive
characteristics.
Through modeling the spatial-temporal connection, the
future values of multivariate flight data can be predicted,
and the UAV faults can be detected by judging if the
residuals between the estimation value and ground truth
exceed the predefined fault threshold. Appropriate fault
thresholds can help to improve the fault detection precision.
In order to remove the negative effect of random noise
or large fluctuations, a bidirectional adaptive exponential
weighted moving average (Bi-AEWMA) scheme is proposed
to determine the fault threshold by smoothing the residual
sequence between prediction values and ground truth.
Requiring
no
precise
physical
model,
the
designed
ST-GATrans is a data-driven approach and can mine potential
fault information through joint spatial-temporal learning on
multivariate flight data. The innovative contributions of this
research can be summarized as follows.
1) An EGAT with graph GMSA is developed to capture
deep spatial association within multivariate flight data.
The designed GMSA can extract spatial connections
from
different
perspectives
and
reduce
excessive
attention on univariate information.
2) A transformer encoder combining MSA and CTF oper-
ations is designed to extract comprehensive temporal
features. With the help of convolution operation, CTF
can capture more local details and facilitate MSA to
extract more comprehensive temporal information.
3) An Bi-AEWMA scheme is proposed to eliminate the
negative impact of noise and large fluctuations in flight
data. Effectiveness of our approach is verified on the
actual flight data collected from a real fixed-wing UAV.
The rest of this article is organized as follows. Section II
presents the fundamental theory of graph representation and
attention mechanism. Section III details the proposed joint
spatial-temporal learning-based fault detection approach. The
experimental results are analyzed and discussed in Section IV.
Section V gives the summarization of this article.
II. FUNDAMENTAL MODELING
A. Graph Representation of Flight Data
Graph is a kind of non-Euclidean data, which are composed
of a set of nodes and edges [23]. GNN is a kind of network
for processing graph-structure data. In GNN, each node’s
information has connection with that of its neighboring nodes.
The information of each node can be updated by aggregating
information of its adjacent nodes [24]. In this study, the
multivariate flight data are collected from different components
or subsystems of UAV, and these status variables will have
significant spatial correlations. Hence, GNN can be introduced
to extract spatial characteristics.
The multivariate flight data of UAV can be first modeled as
a completely connected graph G = (XG, VG, EG), in which
VG is the set of status variables and |VG| = n, n is the
number of flight variables. EG is the adjacency matrix which
represents the association weights between any two flight vari-
ables. Its each element EG(i, j) is nonnegative and describe
the connection weight between the flight variables i and j.
XG are the feature set of all graph nodes corresponding to
different flight variables. XG(i) is the feature representation
of the ith flight variable. The goal of GNN is to learn
the final feature representation of each node i ∈VG and
aggregate them to obtain the final network output. The update
process of the feature XG(i) of node i can be formulated as
follows:
XG(i) = f (XG(ne[i]), EG(i, ne[i]))
(1)
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:14:40 UTC from IEEE Xplore.  Restrictions apply.

## Page 3

WANG et al.: FAULT DETECTION FOR UAVs WITH SPATIAL-TEMPORAL LEARNING
2529517
Fig. 1.
Structure of the MSA in transformer network.
in which
f (·) is the aggregation function to update the
information of each node based on the its neighbors’ features.
XG(ne[i]) represents the features of the neighboring nodes
ne[i] of node i. EG(i, ne[i]) denotes the connection weights
between flight variable i and its neighboring node set ne[i].
B. MSA Mechanism of Transformer Network
Attention mechanism can facilitate to extract more repre-
sentative information through paying more attention on the
critical parts. As an extensive version, self-attention mecha-
nism has more prominent performance on feature extraction.
Completely composed of the self-attention mechanisms, trans-
former network can effectively establish the global association
within network input and output [25].
Scaled dot-product attention is one of the most used self-
attention mechanisms. As shown in (2), calculate the dot
product of the queries Q and keys K, and divide it by the
scaling factor (dk)1/2 to obtain the similarity, in which dk is
the length of key and query. Employing the scaling factor can
significantly reduce the negative effect of unstable gradients.
Finally, one softmax function is applied on the similarity to
obtain the final attention weights
Attention(Q, K, V ) = softmax
 QK T
√dk

V.
(2)
Compared to the general self-attention mechanism that
maps Q, K, and V to the same subspace, MSA can capture
the feature distribution of input from different perspectives.
As shown in the Fig. 1, MSA will map Q, K, and V into h
different subspaces and calculates the self-attention weights
separately. The process of MSA is parallel. The attention
information from h subspaces will be concatenated and then
linearly projected into the final output. Through utilizing h
heads to excavate the inherent information, MSA can observe
different important parts of input, and thus help to extract more
comprehensive feature information [26], [27].
III. JOINT SPATIAL-TEMPORAL LEARNING
BASED FAULT DETECTION MODEL
A. Model Architecture and Workflow
In our research, one ST-GATrans is developed to realize
joint spatial-temporal learning on multivariate flight data and
predict the future values of flight data. The occurrence of
UAV faults can be detected through judging if the deviation
of prediction values and ground truth values exceeds the
predefined threshold. As shown in Fig. 2, an EGAT combined
with GMSA operation is first utilized to mine the spatial
correlation within the graph representations of preprocessed
multivariate flight data. Subsequently, the temporal features
of flight data will be excavated by a transformer encoder
incorporating MSA and CTF operation. The spatial-temporal
features of flight data will be finally aggregated into the class
token (CT). The future values of flight data can be predicted
through projecting the CT information with a fully connected
layer. The procedure of the joint spatial-temporal learning-
based fault detection approach is as follows.
1) Data Acquisition and Preprocessing: A real fixed-wing
UAV is built to collect normal flight data. The flight
data will be first normalized and then reconstructed into
a training, validation, and test set by sliding window
operation.
2) Model Training: The designed ST-GATrans is first
trained on the training set to learn the spatial-temporal
correlation of flight data. Mean square errors (MSEs)
between the ground truth and prediction values will
be calculated to update the model parameter by back
propagation.
3) Threshold Calculation: After model training, a Bi-
AEWMA is applied to smooth the prediction residual
sequence of the training set to reduce the negative effect
of noise and large fluctuations. The threshold for fault
detection will be determined by the smoothed residual
sequence.
4) Model Validation: Inject faults on the test set to generate
fault samples. The trained model is evaluated on the
test set to verify the fault detection performance. The
occurrence of UAV faults can be identified by judging if
the residual of predicted values and ground truth values
exceed the fault threshold.
B. Data Collection and Preprocessing
A real UAV is built to collect actual flight data. The multi-
variate flight data x ∈RN×L can be downloaded from ground
station or on-board equipment, in which N is the number of
flight status variables and L is the length of time-series flight
data. The values of multivariate flight data at time t can be
denoted as x[t] ∈RN, and the flight status variable i can
be denoted as xi ∈RL. Z-score normalization will be first
conducted on each flight variable to reduce the negative effect
of inconsistent magnitude. The z-score normalization can be
formulated as follows:
exi = (xi −µi)/σi
(3)
in which µi and σi are the mean value and standard deviation
of flight status variable xi, respectively.
After data normalization, a sliding window with width K
is used to process the normalized flight data and obtain a
series of samples, which are then divided into a training set,
validation set, and test set. The ST-GATrans is a prediction-
based fault detection model. The multivariate flight data x[T +
K + 1] ∈RN at moment T + K + 1 can be predicted based
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:14:40 UTC from IEEE Xplore.  Restrictions apply.

## Page 4

2529517
IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 73, 2024
Fig. 2.
Architecture of the designed fault detection model.
Fig. 3.
Graph representation of flight data and the schematic for GMSA
with three heads.
on the historical K timestamp {x[T + 1], x[T + 2], x[T +
3], . . . , x[T + K]} ∈RN×K. Hence, the health status of UAV
at moment T +K +1 can be detected through judging whether
the deviation between predicted value x[T +K +1] and ground
truth x′[T + K + 1] exceeds the fault threshold. Specially,
the width K of sliding window is determined based on the
detection effect of trained model.
C. Multivariate Spatial Learning With GMSA-Based EGAT
1) Graph Representation of Multivariate Flight Data:
In order to extract the associations among different flight
status variables, the multivariate flight data is first modeled as
the graph-structured representations, and the inherent spatial
connections can be extracted by the GNN. As shown in
Fig. 3, the multivariate flight data including N flight variables
can be modeled as one graph with N nodes. The feature
representations of all N graph nodes can be represented as
h = {h1, h2, . . . , hN}, hi ∈RK is the normalized feature of
node i corresponding to the ith flight variable, K is the width
of the sliding window.
2) EGAT
With
GMSA:
In
order
to
capture
more
comprehensive
spatial
connections
of
multivariate
flight
data, one GMSA operation is proposed to enhance the
performance of graph attention networks (GATs). Compared
with general GNNs, GAT can pay more attention to the
neighboring nodes with higher importance by introducing the
attention mechanism [28]. During the information aggregation,
the neighboring nodes will be assigned with different weights
according to the feature similarity. To obtain the connections
among the ith flight variable and other variables, the similarity
coefficient ei j between the corresponding graph node i and
its neighboring node j ∈Ni can be calculated as follows:
ei j = aT σ
Whi||Wh j

.
(4)
In which, hi ∈RK and h j ∈RK are the features of node i
and node j, respectively. W ∈RK ′×K is the linear projection
(LP) layer. || denotes the concatenation operation. σ(·) is the
nonlinear activation function. a ∈R2K ′ is one shared attention
layer. The features of two node will be first linearly projected
with W and then be concatenated. After nonlinear activation
σ(·) and attention layer a ∈R2K ′, the similarity coefficient
between any to two nodes can be obtained. The similarity
values will be normalized by softmax function. The attention
weights ai j between node i and its neighboring nodes j ∈Ni
can be calculated as follows:
ai j = soft max
ei j

=
exp
ei j

P
k∈Ni exp(eik).
(5)
Since the collected flight data are typical time series, the
flight variable i will have high temporal correlation with its
own history data. In this case, the prediction of one variable
will be excessively dominated by its historical data, ignoring
the deep spatial connection with other flight parameters. There-
fore, during the process of multivariate spatial information
aggregation, in order to reduce the excessive self-attention
and avoid losing key information, the calculation of attention
weighs in (5) is further modified into the self-attention form
as follows:
ai j =



exp
ei j

P
k∈Ni/i exp(eik),
i ̸= j
1
N −1
X
k∈Ni/i
aik,
i = j.
(6)
The normalized attention weight ai j between node i and
its neighboring node j ∈Ni/i(except node i itself) will be
first calculated as (5). The self-attention weight aii of node i
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:14:40 UTC from IEEE Xplore.  Restrictions apply.

## Page 5

WANG et al.: FAULT DETECTION FOR UAVs WITH SPATIAL-TEMPORAL LEARNING
2529517
Fig. 4.
Calculation of the sub-space attention weight between any two nodes.
is calculated by averaging the attention weights of all its
neighboring nodes j ∈Ni/i (except node i itself). N is the
number of graph nodes. After obtaining the attention weights
between node i and its neighboring nodes, the features will be
weighted and activated by a nonlinear function to obtain the
final output of node i.
In order to mine deeper spatial connections among different
flight variables, a GMSA operation is further developed based
on the above graph self-attention mechanism. The proposed
GMSA will invoke K independent self-attention operations to
enhance the feature learning performance. In GMSA, the node
features will be first transformed into K different subspaces
with K different projection matrices. After calculating the
attention weights in different subspace, the output of each
node in different subspace can be obtained through linear
aggregation. In order to keep the dimension of node feature
unchanged, the feature output in K subspaces will be averaged
to obtain the final output. The process of GMSA can be
formulated as follows:
h′
i = σ

1
K
K
X
k=1
X
j∈Ni
ak
i jW kh j

.
(7)
In which ak
i j is the attention weight between node i and
node j in the kth subspace, and W k ∈RK ′×K is the linear
transformation matrix to project the node vector into the kth
subspace. In order to better retain the information in flight data,
the dimension of each node’s feature will keep unchanged, that
is, K = K ′.
Fig. 3 illustrates the schematic for one GMSA with three
heads. For the multivariate flight data with N variables, a graph
representation with N nodes will be first constructed, and then
the spatial connections among different nodes will be learned
by the GMSA. For the node h3, the attention weights with
its neighboring nodes {h1, h2, h3, h4, . . . , hN} will be first
calculated in three subspaces. The connection with different
colors represents the attention weight in different subspaces.
Fig. 4 presents the calculation of attention weight a1
3N between
node 3 and node N in the first subspace W1. The node features
in different subspaces will be further concatenated, and then
averaged to obtain the final output h′
3.
D. Temporal Feature Learning With MSA and CTF-Based
Transformer Feature Encoder
For the multivariate flight data, there are rich temporal
features which can help to predict the faults more precisely.
Fig. 5.
Structure of the designed temporal feature encoder.
In this study, an enhanced transformer encoder incorporating
MSA and CTF operation is developed to excavate more
comprehensive temporal features. As shown in Fig. 5, the
designed temporal feature extraction architecture consists of
three parts, including input embedding, Transformer encoder,
with the MSA and CTF modules, and a multilayer perception
(MLP) to predict future flight data.
1) Input Embedding: The input embedding can be divided
into two steps including patch embedding and position embed-
ding. In the patch embedding, the preliminary spatial features
h′ = {h′
1, h′
2, . . . , h′
N} ∈RN×K of multivariate flight data
after graph learning will be first divided into a patch sequence
x p = {x1
p, x2
p, . . . , x K
p } ∈RK×N along the time dimension. The
multivariate flight data at different time steps will be regard
as different patches. The number of patches is equal to the
number K of timestamps, and the length of each patch is equal
to the number N of flight variables. Subsequently, a learnable
LP E ∈RN×dmodel is applied on the patch sequence to obtain
the embedded tokens xq ∈RK×dmodel. The process of patch
embedding can be formulated as follows:
xq = x pE =

x1
q, x2
q, . . . , x K
q
	
(8)
in which dmodel is the token dimension which remains
unchanged in all subsequent layers. In particular, similar
with the BERT model in literature [29], one learnable CT
xclass ∈Rdmodel is appended to the start of the embedded token
sequence. This randomly initialized CT can help to aggregate
the information of different tokens and facilitate to extract
more comprehensive temporal features.
In order to preserve the position information in original
sequence, one-hot position embedding is applied to record
the temporal order of tokens. The encoding number is started
from 0 to K, 0 denotes the position of the CT and K is
the number of patches. The position encoding information
Epos ∈R(K+1)×dmodel will be directly added to the tokens
sequence, and the final embedded token sequence XET can
be represented as follows:
X ET =

xclass, x1
q, x2
q, . . . , x K
q

+ Epos.
(9)
2) Transformer Feature Encoder With MSA and CTF: For
the embedded token sequence, an enhanced transformer
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:14:40 UTC from IEEE Xplore.  Restrictions apply.

## Page 6

2529517
IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 73, 2024
Fig. 6.
Architecture of the proposed CTF operation.
encoder combining MSA and CTF operations is designed
to extract comprehensive temporal features. As described in
Section III-A, the MSA module can help to capture distant
temporal associations. In transformer encoder, MSA with h
heads (MSAh) is first used to map the embedded tokens to
h different subspaces and separately calculate the attention
weights, so as to obtain global temporal information from
different perspectives.
In the embedded token sequence, the neighboring tokens
have more temporal connections because they are transformed
from the adjacent segments of multivariate flight data. Only
applying MSA may ignore these local information interactions
of spatially neighboring tokens to some extent. Compared to
MSA, convolution operation possesses more powerful capa-
bility on local perception and can help to extract more local
information. Therefore, in order to model the local interactions
of spatially adjacent tokens, convolution token fusion opera-
tion is designed and introduced into the existing MSA-based
encoder layer to extract more comprehensive information.
As shown in Fig. 6, the convolution token fusion operation
is composed of two parts including convolution mixing and
pooling mixing. During the process of convolution mixing,
the information of all input tokens except the CT will be
first mapped to a higher dimension by a LP layer. Depthwise
convolution (DWConv) is then applied on the padded tokens
to aggregate the local information of spatially neighboring
tokens. For example, the size of convolution kernel is set as
three, and the information of every three neighboring tokens
will be aggregated into one new token. The number of tokens
can keep constant via the padding operation. During the pro-
cess of pooling mixing, the token sequence after convolution
mixing will be further padded, and local average pooling
(LAP) is applied to replace the original token with the average
result of its neighboring tokens. Similarly, the pooling size is
set as three, and the information of every three neighboring
tokens will be averaged as one new token. Finally, the pooling
results will be linearly projected into the final output tokens.
Through the DWConv and LAP operations, the local temporal
features inherent in the multivariate flight can be effectively
extracted.
The finally designed transformer encoder has L layers.
As shown in Fig. 5, each encoder layer is in a residual
connection to eliminate the influence of gradient disappearance
or explosion during network training. Layer normalization
(LN) is employed to stabilize the feature distribution. The flow
process of the embedded token sequence XET in each encoder
layer can be represented as follows:
XMSA = LN(MSAh(X ET ) + X)
(10)
XCT F = LN(CTF(XMSA)) + XMSA )
(11)
in which MSAh(·) represents the MSA operation with h heads.
CTF(·) is the convolution token fusion operation. XMSA and
XCTF are the output of MSA and CTF module, respectively.
Processed by transformer encoder with L layers, the global
temporal features of multivariate flight data will be aggregated
into the CT. The output of CT xclass will be further input to
one MLP composed of two feed-forward layers to predict the
future flight data x K+1
p
at moment K + 1.
E. Threshold Calculation With Bi-AEWMA
Due to the high complexity and harsh operating environment
of UAV systems, the collected flight data will be inevitably
contaminated by noise. The sensor data with huge noise may
be misidentified as anomalies. Hence, selecting an appropriate
fault threshold will be helpful to enhance the fault detection
performance since a too high or low threshold may lead to high
missed detection rates or false alarm rates, respectively. Expo-
nential moving average (EWMA) can smooth the sequence
with noise or large fluctuations by exponentially weighting the
current observation and historical values. Traditional EWMA
applies a fixed weighting factor for sequence smoothing, which
may result in a backward bias along the time dimension. The
larger the weighting factor, the more the smoothed sequence
is shifted backward. This offset will induce a large deviation
in the initial part of signal and thus deteriorate the final fault
detection performance.
To address this issue, one bidirectional EWMA with adap-
tive weighting factors, namely Bi-AEWMA, is proposed to
reduce the negative effect of noise and large fluctuations in
flight data. Bi-AEWMA applies a gradually increasing weight
factor to smooth the residual sequence. The smoothing process
with adaptive weighting factors can be formulated as follows:



E1 = r1
Et = βEt−1
1 −βt + (1 −β)rt
1 −βt
, t ≥2
(12)
in which r = [r1,r2,r3,..., rL] is the prediction residual
sequence of training set with length L. rt and Et are the
unsmoothed and smoothed residual value of the tth times-
tamp,respectively. β is the initial weighting factor. It can be
observed that the weighting factors can be adaptively updated
with the timestamp increasing.
Meanwhile, in order to eliminate the backward bias caused
by one-way smoothing, the original residual sequence will
be smoothed simultaneously both forward and backward, and
the minimum of bi-directional smoothing results is selected to
form the final smoothed residual sequence. In the backward
smoothing, the residual sequence will be first reversed and
then smoothed with adaptive weighting factor. The process
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:14:40 UTC from IEEE Xplore.  Restrictions apply.

## Page 7

WANG et al.: FAULT DETECTION FOR UAVs WITH SPATIAL-TEMPORAL LEARNING
2529517
of backward smoothing is similar with (12) and can be
represented as follows:



RL = rL
Rt =
β Rt+1
1 −β L−t+1 + (1 −β)rt
1 −β L−t+1 , t ≤L −1
(13)
in which r = [r1,r2,r3,..., rL] is the prediction residual
sequence of training set with length L. β is the initial
weighting factor. The minimum value of the forward smoothed
residual Et and reverse smoothed residual Rt at the times-
tamp t will be selected as the final smoothed value. The
residual series after Bi-AEWMA can be calculated as follows:
rsmooth,t = min(Rt, Et),
1 ≤t ≤L.
(14)
In the data preprocessing described in Section III-A, the
value of the current moment is assumed to be only related to
the previous K time steps. Therefore, the initial value of β
should be associated with the window width K and the initial
value is set as follows:
β = 1/(K + 1).
(15)
The final value of β will be fine-tuned according to the
effect on validation set. After smoothing the residual sequence
corresponding to the training set, the fault threshold TF can
be calculated as follows:
TF = µr + λσr
(16)
where µr and σr are the mean and standard deviation of
the smoothed residual sequence rsmooth, respectively. λ is
a constant which can be determined appropriately by the
performance on validation set.
IV. EXPERIMENTAL VERIFICATION AND
RESULT ANALYSIS
A. Data Description
To better verify the effectiveness of the proposed fault
detection method, the experimental data used in this study
are all collected from a self-developed “explorer” fixed-wing
UAV. As shown in Fig. 7(a), the UAV for data collection is
with a wingspan of 1890 mm, wing area of 44 dm2, body
length of 1480 mm, take-off weight of 3.5–4.5 kg, and cruising
speed of 55–75 km/h. The UAV system is built based on
an open source-flight controller Pixhawk 2.4.8. The system
composition of the developed UAV system is presented in
Fig. 7(b). The sensor module composed of an accelerometer,
gyroscope, barometer, compass, pitot tube, and GPS is used to
collect the critical status information including the information
about attitude, position, altitude, airspeed, acceleration, etc.
The collected information is further fed into the processor
module to calculate the control commands for the actuator
module according to the preset flight plan or remote-control
commands. Subsequently, the actuator module will execute
the controlling command from the processer module to adjust
the flight status. Specifically, the rotation speed of the motors
and propellers is controlled by the electronic speed control
(ESC) unit to adjust the propulsion, and the deflection angles
of the rudder surfaces are controlled by the servos to realize
Fig. 7.
Designed “explorer” fixed-wing UAV. (a) Hardware implementation.
(b) System composition.
attitude adjustment. It can be observed that the sensor module,
processor module, and actuator module have formed the flight
control system of the designed UAV. In addition, during the
flight mission, one receiver module is employed to receive
the controlling commands from the transmitter to realize
remote manual control, and one telemetry module is used to
communicate with the ground controlling station to realize the
real-time monitoring of UAV flight status. The critical flight
data during the flight mission will be stored in the memory
module. One debug module is used to check and calibrate
the status of each module before takeoff to guarantee the
flight safety. As for the power source, Li-polymer battery
is selected to power the designed UAV system. One power
module is used to adjust the battery output to obtain specific
voltage and stable current to power the actuator module and
processor module. Through connecting with the processor
module, the external modules including the sensor module,
telemetry module, receiver module, and memory module will
be indirectly powered.
In the processer module, one 32-bit STM32F427 chip
is used as the main processer to process the flight status
information, and one failsafe coprocessor STM32F103 is
employed in case of the failure of the main processer.
In the sensor module, MicroL3GD20H 16-bit gyroscope,
MicroLSM303D 14-bit accelerometer, CUAV SKYE-2 pitot
tube, and MS5611 barometer are selected. In addition, one
external navigation GPS module named Ublox NEO-M8N
with HMC5883L electronic compass is used to collect the
position information. In the actuator module, Sunnysky-X352
motors and EMAX servos are selected to drive propeller and
rudder surface, respectively. The power source of the whole
UAV system is selected as one 6800-mAh Li-polymer battery.
In the telemetry module, CUAV-XB radio telemetry module
working in 915-MHz frequency band is used to communicate
with the ground controlling station. In the receiver module,
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:14:40 UTC from IEEE Xplore.  Restrictions apply.

## Page 8

2529517
IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 73, 2024
Fig. 8.
Flight trajectory in ground control station.
the remote-control transmitter Futaba-T14SG and Futaba-
R7008SB receiver operating in 2.4 GHz are used to control the
UAV manually. The open-source firmware running on Pixhawk
is Copter v3.3.2 which can be fired with the ground controlling
station (QGC) named Mission Planner. Mission Planner can
be run on both Windows and Linux platform and can be used
to configure the critical parameters of flight mission.
The UAV flight is conducted in the specific experimental
area of our school. Six groups of flight data with different flight
trajectories and durations have been collected. We only select
part of valid flight data from them and the final durations of six
flight data are 242.4, 272.7, 327.6, 359.1, 202.5, and 301.7 s,
respectively. During the whole flight, the weather was sunny
with an outdoor temperature of 22 ◦C–28 ◦C and wind force
of 2–3 level. Since the main flight status of UAV is cruising,
the flight data in cruising stage is selected for experimental
verification. As shown in Fig. 8, the flight trajectory will be
predefined in the Mission Planer. After the flight mission,
the flight records including all sensor data and controlling
commands can be downloaded and visualized with Mission
Planer.
The originally collected multivariate flight data contained a
large number of status variables. To reduce the dimensionality
of the input, some irrelevant and redundant flight variables
will be excluded, and the final selected 24 flight variables are
shown in Table I, including angular rate, triaxial acceleration,
angle, velocity, height, etc. Part of the status variables are
presented in Fig. 9. The collected multivariate flight data
will be further normalized and reconstructed into a training,
Cvalidation, and test set according to the descriptions in
Section III-A. In this study, six groups of flight data with
different trajectories and durations are collected. Specially, the
first four sets of flight data are selected as the training dataset,
the fifth set of flight data is selected as the validation set,
and the sixth set of flight data is selected as the test dataset.
The sizes of the training, validation, and the test dataset are
12 000, 2000, and 3000, respectively. Each sample in dataset
is with the length of 256. A certain degree of Gaussian noise is
further added on the flight data to improve the noise robustness
of model.
B. Fault Setting
In actual missions, fault data of UAV are rather rare, and it
is impossible to collect adequate fault data covering all failure
TABLE I
SELECTED FLIGHT STATUS VARIABLES
Fig. 9.
Part of status variables in multivariate flight data.
modes. In contrast, a large amount of normal flight data can be
easily collected. The proposed joint spatial-temporal learning-
based fault detection method is unsupervised and only normal
flight data are used for model training. In order to verify
the effectiveness of the proposed method in the test stage,
the fault flight data will be produced by injecting faults on the
normal flight data. According to the literature [12] and [14],
three faults are selected, including bias, drift, and stuck faults.
The signals with bias fault, drift fault, and stuck fault can be
represented as yi(t) = xi(t)+a, yi(t) = xi(t)+b·t, yi(t) = c,
respectively. yi(t) is the fault signal, xi(t) is normal data, t is
a period of time. a, b, and c are constants.
In this work, roll rate is selected as the faulty parameter for
analysis which can directly reflect the effect of UAV attitude
controlling [14]. The collected multivariate flight data with
10 000 timestamps will be first preprocessed and divided into
a training and test set according to the proportion of 7:3.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:14:40 UTC from IEEE Xplore.  Restrictions apply.

## Page 9

WANG et al.: FAULT DETECTION FOR UAVs WITH SPATIAL-TEMPORAL LEARNING
2529517
Fig. 10.
Roll rate with fault injected. (a) Bias fault. (b) Drift fault. (c) Stuck
fault.
For the test set with length of 3000, faults will be injected
from the 1501-th timestamp to the end. Detailed procedures
of fault injection on roll rate are presented as follows.
1) Bia Fault: As shown in Fig. 10(a), the injected deviation
value is 0.17◦, which is equal to 0.25 times of the extreme
deviation of training set. The fault interval is [1501, 3000].
2) Drift Fault: As shown in Fig. 10(b), the drift fault is set
as 0.25◦/s2 since the sampling frequency of roll rate is 50 Hz.
The fault interval is [1501, 3000].
3) Stuck Fault: As shown in Fig. 10(c), the stuck value is
set as 0.32◦/s, which is equal to the standard deviation of the
training set. The interval of stuck fault is [1501, 3000].
C. Model Evaluation Metrics
The proposed ST-GATrans is a prediction-based fault
detection approach consisting of two parts, including future
flight data prediction and fault identification by comparing
the prediction residual with the predefined fault threshold.
Precise prediction of flight data is helpful to improve the
fault detection performance. In the prediction stage, in order
to assess the performance on future flight data prediction,
MSE, mean absolute error (MAE), root MSE (RMSE) are
selected as the evaluation metrics, which can be calculated
as following equations. As the commonly used metrics to
evaluate the prediction performance of model, MSE, MAE,
and RMSE have been validated to be effective in some
popular related literatures [5], [6], [12], [13], [14], [17],
[18], [30]. MSE can describe the average of the squared
difference between the predicted and actual values. RMSE
can describe the standard deviation between the predicted
and actual values. MAE can describe the average absolute
difference between the predicted and actual values. These
metrics are with different characteristics and can evaluate the
model’s prediction performance from different perspectives.
Therefore, in this study, these three metrics including MSE,
MAE, and RMSE have been combined to comprehensively
evaluate the model’s prediction performance
MSE = 1
N
N
X
i=1
bYi −Yi
2
(17)
MAE = 1
N
N
X
i=1
|bYi −Yi|
(18)
RMSE =
r
1
N
bYi −Yi

2
(19)
where N is the number of samples for prediction, bYi and Yi
are the prediction value and ground truth of the ith sample,
respectively. The model with poor prediction performance will
have a larger MSE, MAE, and RMSE.
In the fault detection stage, there are four different detection
results, including true positive (TP), false positive ( FP), true
negative ( TN), and false negative ( FN). TP and TN refer
to the number of correctly classified normal samples and fault
samples, respectively.
FP and
FN refer to the number of
misclassified normal samples and fault samples, respectively.
To evaluate the performance of model on fault detection, true
positive rate (TPR), false positive rate (FPR), and detection
accuracy (ACC) are selected as the evaluation metrics, which
can be calculated as follows. TPR, FPR, and ACC metrics
have been validated to be effective in evaluating the fault
detection performance of model [31], [32], [33], [34]. TPR
can describe how many normal samples have been classified
correctly. FPR can describe how many fault samples have
been misclassified. ACC can describe how many normal and
fault samples have been classified correctly. These metrics
with different characteristics are complementary. Hence, in this
study, TPR, FPR, and ACC are combined to evaluate the
performance on fault detection
TPR =
TP
TP + FN
(20)
FPR =
FP
FP + TN
(21)
ACC =
TP + TN
TP + FP + TN + FN.
(22)
A model with prominent fault detection performance will
have a high TPR and ACC closed to one and a low FPR closed
to zero. The receiver operating characteristic (ROC) curve uses
the FPR and TPR as horizontal and vertical coordinates to
depict the classifier’s performance with different thresholds.
The area under curve (AUC) is the area under the ROC curve
and can be used to assess the fault detection performance.
The closer the AUC value is to 1, the better the classifier’s
performance is.
D. Details of Model Structure
The designed ST-GATrans model is composed of two EGAT
layers and two transformer feature-encoder layers. The training
epoch is set as 600, the learning rate of Adam optimizer is
0.003, and the batch size is 256. More details about the model
structure have been given in Table II.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:14:40 UTC from IEEE Xplore.  Restrictions apply.

## Page 10

2529517
IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 73, 2024
TABLE II
STRUCTURE DETAILS OF THE PROPOSED ST-GATrans MODEL
E. Experimental Result Analysis
1) Comparison Analysis on the Prediction Result:
In
order to further verify the effectiveness of the proposed
ST-GATrans approach, one LSTM-based temporal prediction
method named Conv-LSTM [31] is first selected for compar-
ison. Meanwhile, since the proposed ST-GATrans method is
composed of one multivariate spatial feature encoder and one
temporal feature encoder, two group of ablation experiments
are further conducted to further validate the efficacy. The
first group of ablation experiments are aimed to verify the
effectiveness of the designed spatial feature encoder based on
the EGAT with GMSA. Four ablation approaches are designed
including removing the whole designed spatial encoder based
on EGAT (No EGAT), replacing the GMSA operation with
general graph attention mechanism (No GMSA), only remov-
ing the graph self-attention operation in GMSA (No GSA), and
only removing the graph multiheaded attention operation in
GMSA (No GMA). The second group of ablation experiments
are aimed to verify the effectiveness of the designed temporal
feature encoder based on the CTF and MSA. Three ablation
approaches are designed including only removing the designed
CTF operation (No CTF), only removing the MSA operation
(No MSA), and replacing the whole designed temporal feature
encoder with Conv-LSTM (EGAT-Conv-LSTM). In this study,
all machine learning models are implemented on one personal
laptop equipped with one 13th Gen Intel1 Core2 i7-13650HX
CPU (24 GB RAM) at 2.60 GHz and one NVIDIA GeForce
RTX4060 Laptop GPU (8 GB). The operating system of the
1Registered trademark.
2Trademarked.
Fig. 11.
Prediction results of different comparison methods. (a) ST-GATrans.
(b) Conv-LSTM. (c) EGAT-Conv-LSTM. (d) No CTF. (e) No GMSA.
used laptop is Windows 11 professional. All algorithms are
implemented by Python 3.8 with Pytorch framework. All codes
are written in the PyCharm editor (community version 2023.3).
Prediction results of the proposed ST-GATrans on the nor-
mal data are shown in Fig. 11. The blue solid lines represent
the normal roll rates, and the red dashed lines are the predicted
roll rate of our approach. It can be observed that the lines
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:14:40 UTC from IEEE Xplore.  Restrictions apply.

## Page 11

WANG et al.: FAULT DETECTION FOR UAVs WITH SPATIAL-TEMPORAL LEARNING
2529517
TABLE III
PREDICTION RESULTS OF DIFFERENT COMPARISON METHODS
are almost completely coincident, indicating that the proposed
method can predict the future flight data well. The predic-
tion results of four comparison methods are also presented.
It can be observed that compared to the other methods,
our proposed ST-GATrans has obtained the best prediction
result with minimal deviation. The Conv-LSTM model has
worst prediction result because it ignores the important spatial
connections among different status variables and only focuses
on the extraction of temporal features. Meanwhile, it can be
observed that after removing the designed CTF and GMSA
operations or replacing the temporal feature encoder with
Conv-LSTM, the prediction results will become worse, and
there will be large deviations at the stage of status switching.
The comparison results demonstrate the effectiveness of the
designed spatial-temporal feature encoders based on CTF and
GMSA.
To quantitatively evaluate the prediction performance, the
prediction metrics of all comparison methods on normal flight
data are presented in Table III. The prediction MSE, MAE, and
RMSE of the ST-GATrans have reached 3.78e−4, 1.13e−2,
and 1.94e−2, respectively. It can be observed that the MSE,
MAE, and RMSE of the proposed ST-GATrans are lowest.
The prediction errors of Conv-LSTM method are still larger
than that of other spatial-temporal learning based methods,
which indicate that the spatial connections among different
flight status variables are helpful to improve the prediction
performance.
Meanwhile,
the
prediction
performance
is
degraded after removing GMSA, GMA, GSA, or the whole
designed EGAT-based spatial encoder. The comparison results
demonstrates that the multivariate spatial features are helpful
to realize better fault detection performance and our designed
spatial encoder based on GMSA can effectively capture the
inherent connections of different flight variables.
Furthermore, after removing the designed CTF and MSA
operations, the prediction result of ST-GATrans on normal
data will becomes worse. This is because the CTF and MSA
operations can help to mine more comprehensive temporal
information of flight data through aggregating the local and
global information. After replacing the temporal encoder of
ST-GATrans with Conv-LSTM, the predicted effect will be
deteriorated. This is because the designed temporal encoder
has more powerful feature extraction ability and can capture
more comprehensive temporal information than the tradi-
tional Conv-LSTM. Through conducting joint spatial-temporal
TABLE IV
RESULTS OF THE FIRST GROUP OF ABLATION EXPERIMENTS TO VERIFY
THE EFFECTIVENESS OF THE DESIGNED SPATIAL FEATURE ENCODER
TABLE V
RESULTS OF THE SECOND GROUP OF ABLATION EXPERIMENTS TO
VERIFY THE EFFECTIVENESS OF THE DESIGNED TEMPORAL
FEATURE ENCODER
TABLE VI
RESULTS OF THE THIRD GROUP OF ABLATION EXPERIMENTS TO VERIFY
THE EFFECTIVENESS OF THE DESIGNED Bi-AEWMA STRATEGY
learning on multivariate flight data to extract deep features,
ST-GATrans can predict the future flight data more precisely.
2) Comparison Analysis on the Fault Detection Result:
Similar to the above comparative experiments on prediction
performance,
two
groups
of
ablation
experiments
are
conducted
to
verify
the
effectiveness
of
the
designed
GMSA-based
spatial
encoder
and
the
temporal
feature
encoder based on CTF and MSA. The fault detection results
of different comparison methods are shown in Tables IV–VI.
In particular, the third group of ablation experiment is further
added to verify the effectiveness of the proposed Bi-AEWMA.
Two ablation approaches are designed including removing
the designed bidirectional average strategy in Bi-AEWMA
(AEWMA) and removing the designed adaptive strategy in
Bi-AEWMA (Bi-EWMA).
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:14:40 UTC from IEEE Xplore.  Restrictions apply.

## Page 12

2529517
IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 73, 2024
Fig. 12.
ROC curves and AUC values with drift fault injected.
In the three different fault scenarios, the ST-GATrans
method has the highest TPR, ACC, and the lowest FPR. This
is because the ST-GATrans has the best prediction perfor-
mance, and the used Bi-AEWMA can help to significantly
eliminate the negative effect of noise and large fluctuations.
Instead, as shown in Table V, Conv-LSTM has the worst
detection performance since it ignores the spatial connection
of multivariate flight data. After adding the spatial feature
encoder EGAT, the performance of EGAT-Conv-LSTM will
be significantly improved; hence, only extracting temporal
features of multivariate flight data is insufficient. The fault
detection performance can be significantly enhanced through
mining the rich spatial-temporal features of multivariate flight
data. As shown in Table IV, after removing GMSA, GMA,
GSA, or the whole EGAT-based spatial encoder, the FPR is
increased while the TPR and ACC is decreased. The reason
is that with the reduced spatial information, the prediction
performance of these ablation approaches decreases. There
will be large prediction errors at the dramatically changing
point, which leads to the smoothed residual values exceed the
fault threshold.
Through the first group of ablation experiments, the effec-
tiveness the designed spatial encoder based on GMSA can be
verified.
Meanwhile, as shown in Table V, after removing the
designed CTF or MSA operation, the fault detection results of
ST-GATrans on three fault types will becomes worse. This is
because the CTF and MSA operations can help to mine more
comprehensive temporal information through simultaneously
aggregating the local and global information. Through the
second group of ablation experiments, the effectiveness of the
designed temporal encoder based on CTF and MSA can be
verified.
Since it is more difficult to detect the drift faults which
are gradually increasing, drift faults are selected for further
analysis. The ROC curve of four selected comparison methods
with injected drift fault is plotted in Fig. 12. The AUC
results are also calculated and labeled on the figure. The fault
detection model with better performance will have an AUC
value closed to one. For drift fault, the AUC results of our
proposed method are the largest, which is greater than 0.988.
Meanwhile, the ROC curves of the joint spatial-temporal
learning approaches including no CTF and no GMSA are
closer to the upper left corner than that of Conv-LSTM. The
reason is that the Conv-LSTM ignores the spatial connection
Fig. 13.
Smoothed residual sequence of the test set. (a) EWMA.
(b) Bi-AEWMA.
among flight variables and has the worst performance on
flight data prediction. We further analyze the effectiveness
of the designed Bi-AEWMA. As shown in Table VI, it can
be observed that the proposed Bi-AEWMA has better fault
detection performance than EWMA in all fault scenarios, espe-
cially in the early stage of drift faults. The smoothed residual
sequence corresponding to the test set are displayed in Fig. 13.
It can be observed that compared to EWMA, the smoothing
result of Bi-AEWMA has smaller fluctuations. With the adap-
tive bi-directional smoothing on residual sequence, the large
fluctuation can be eliminated and thus the minor anomaly
in the early stage of drift fault can be effectively identified.
Through the third group of ablation experiments, the effective-
ness of the designed Bi-AEWMA strategy can be verified.
3) Sensitivity Analysis on the Bi-AEWMA Parameters: We
have further examined the influence of the weighting fac-
tor β and the threshold factor λ specified in the Bi-AEWMA
algorithm. We test the fault detection performance under dif-
ferent values of β and λ. The AUC score is selected to evaluate
the model performance. A model with better performance
will have a higher AUC value close to one. As shown in
Figs. 14 and 15, it can be observed that the choice of weighting
factor β and threshold factor λ has great influence on the
AUC performance. The detection performance improved with
the increase of β and λ at first. However, when the parameters
reach above certain values, the model will show degraded AUC
performance. According to the sensitivity analysis results, the
optimal value of β is set within [0.02, 0.03], and the optimal
value of λ is set within [2.5, 3.5].
4) Model Robustness Analysis: Three groups of experi-
ments are further conducted to verify the robustness of the
designed approach.
a) Robustness to injected faults with different magnitude,
duration, and timing: Faults with different magnitude are
injected on the test data to further verify the performance
of our proposed approach. The detailed results have been
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:14:40 UTC from IEEE Xplore.  Restrictions apply.

## Page 13

WANG et al.: FAULT DETECTION FOR UAVs WITH SPATIAL-TEMPORAL LEARNING
2529517
Fig. 14.
AUC scores of ST-GATrans with different threshold factor λ.
Fig. 15.
AUC scores of ST-GATrans with different weighting factor β.
presented in Fig. 16. The amplification factors of the stuck
fault denote the multiple of standard deviation of the training
data. The amplification factors of the bias faults denote the
multiple of extreme deviation. The horizontal coordinate of the
detection result on drift faults is the drift rate. The AUC score
is selected to evaluate the model performance. A model with
better performance will have a higher AUC value close to one.
It can be observed that the fault detection performance of all
comparison methods degrades as the fault amplitude decreases.
This is because the features of low-amplitude faults will be
easily disrupted by noise, making it difficult to be detected.
With the least performance degradation, the detection results
of our approach still outperform the other models in all three
fault scenarios when the fault amplitude decreases.
In order to test the effect of fault duration on the per-
formance of each model, faults with different durations are
injected on the test data with length of 3000. Specially, the
faults are injected from a certain timestamp to the end of
the test data. Five different scaling factors α ={0.3,0.4,0.5,
0.6,0.7} are selected. The scaling factor represents the pro-
portion of the fault duration to the test data. For example, for
the scale factor 0.4, the fault duration is 1200 timesteps, and
the fault interval is [1801, 3000]. The detection results of all
comparison approaches on the test data with different fault
durations are presented in Fig. 17. The horizontal coordinates
indicate the proportion of the injected fault in the test data.
The AUC score is selected to evaluate the model performance.
A model with better performance will have a higher AUC
value close to one. It can be observed that the detection
performance of different comparison models are all improved
with the increases of fault durations. This is because the fault
characteristics that deviate from the normal status will be
more obvious to be detected as the fault duration increases,
especially for the drift faults. With the reduction of fault
duration, the discriminability of fault features is decreased and
the performance of different approaches are all degraded. With
the least performance degradation, the detection results of the
proposed ST-GATrans model consistently outperform the other
comparison models in all three fault scenarios when the fault
duration decreases.
Furthermore, we conducted experiments to analyze the
effect of the timing of faults on the performance of different
models. In the experiment, the duration of injected fault is
set as 1500 which is equal to 1/2 the length of test data.
The timing of injected faults are set as the start point,
1/10, 2/10, 3/10, 4/10, and 5/10 length of the test data, and
corresponding fault intervals are set as [0, 1500], [301, 1800],
[601, 2100], [901, 2400], [1201, 2700], and [1501, 3000],
respectively. The results of different comparison methods on
the test data with different timings of faults are presented in
Fig. 18. The horizontal coordinates indicate the timing of the
injected fault on the test data. The AUC score is selected
to evaluate the model performance. A model with better
performance will have a higher AUC value close to one. It can
be observed that the fault detection performance of different
methods will fluctuate with the change of the timing of fault.
Among them, the performance of Conv-LSTM fluctuates most
seriously. However, it can be observed there is no specific
pattern to describe how the timing of fault could affect the
model performance. With the most stable performance, our
approach ST-GATrans consistently outperforms the other four
comparison models in all three fault scenarios when the timing
of fault changes.
b) Robustness to the variations in environmental condi-
tions: In order to verify the model’s robustness to variations
in environmental conditions, two groups of flight data are
further collected to test the model performance. These two
groups of flight data with flight durations of 312.2 and
287.3 s are collected in the morning and afternoon under
different temperatures and wind speeds. Their flight altitudes
and trajectories are also different. The size of this new test
dataset is 6000. The injection process of the bias, drift, and
stuck faults are consistent with the previous fault settings
described in Section IV-B. The fault detection results of
the trained model on the new test dataset are presented in
Table VII. It can be observed that the proposed ST-GATrans
has obtained high TPR and ACC, and low FPR for all three
fault scenarios. The experimental results indicate that the
ST-GATrans possesses excellent robustness to the variations in
environmental conditions. Compared with other approaches,
ST-GATrans also has realized the better performance in all
three fault scenarios.
c) Robustness to multiple injected faults: In order to
further verify the robustness of the proposed method, a more
complex fault scenario is considered. In the previous single
fault cases, the faults are injected at 1/2 the length of data and
lasts to the end. In the scenarios with multiple injected faults,
the collected test set with length of 3000 is divided into six
segments [1, 500], [501, 1000], [1001, 1500], [1501, 2000],
[2001, 2500], and [2501, 3000]. Three fault types including
the drift, bias, and stuck faults are cyclically injected on the
fourth to the sixth segments.
The results of different comparison methods in the more
complex fault scenario are presented in Table VIII. It can
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:14:40 UTC from IEEE Xplore.  Restrictions apply.

## Page 14

2529517
IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 73, 2024
Fig. 16.
Performance of different methods on the faults with different magnitude. (a) Bias fault. (b) Stuck fault. (c) Drift fault.
Fig. 17.
Performance of different methods on the faults with different durations. (a) Bias fault. (b) Stuck fault. (c) Drift fault.
Fig. 18.
Performance of different methods on the faults with different timings. (a) Bias fault. (b) Stuck fault. (c) Drift fault.
TABLE VII
FAULT DETECTION RESULTS ON THE NEW TEST DATASET
be observed that the ST-GATrans approach outperforms other
models in term of all evaluation metrics. As shown in Fig. 19,
the ST-GATrans has obtained the higher AUC value than all
the other ablation approaches. After removing the designed
GMSA or CTF operations, the fault detection performance will
TABLE VIII
FAULT DETECTION RESULTS ON MULTIPLE INJECTED FAULTS
be degraded. In addition, it should be noted that compared to
the single-fault scenario, the performance of the model has
decreased. The reason is that the fault appears and disappears
more times, which increase the fault detection difficulty.
One group of experiment is further conducted to further
investigate the effects of fault duration on the performance
of different methods in the scenario of multiple faults. In the
experiment, the test data with length of 3000 is first divided
equally into 4, 10, 16, 22, and 28 segments. Then, the faults
are injected from the second to the last segment, and the fault
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:14:40 UTC from IEEE Xplore.  Restrictions apply.

## Page 15

WANG et al.: FAULT DETECTION FOR UAVs WITH SPATIAL-TEMPORAL LEARNING
2529517
Fig. 19.
ROC curves and AUC values with multiple injected faults.
Fig. 20.
AUC scores of different methods on the faults with different
durations in the scenario of multiple faults.
type for each segment is cyclically set to drift fault, bias
fault, and stuck fault. For example, when the test data with
length of 3000 is equally divided into ten segments including
[1, 300], [301, 600], [601, 900], [901, 1200], [1201, 1500],
[1501, 1800], [1801, 2100], [2101, 2400], [2401, 2700], and
[2701, 3000]. The first segment [1, 300] is not injected with
any fault, the second/fifth/eighth segments are injected with the
drift faults, the third/sixth/ninth segments are injected with the
bias faults, and the fourth/seventh/tenth segment are injected
with the stuck faults. It can be observed that as the number of
division segments increases from 4 to 28, the duration of each
single fault will decrease from (1/4)×X to (1/28)×X, and the
occurrence frequency of different faults increases from 1 to 9,
X = 3000 is the length of the test data. In particular, only the
integer parts of the above calculation results are retained.
The detection results of different comparison methods on
the test data with different fault durations are presented in
Fig. 20. The horizontal coordinates indicate the number of
division segments. The AUC score is selected to evaluate the
model performance. A model with better performance will
have a higher AUC value close to one. With the increas-
ing number of division segments, the fault duration will be
decreased and the switching frequency of different faults will
be increased. It can be observed that the detection performance
of all models decreases as the number of division segments
increases. This is because with the increasing number of
division segments, the fault duration will be decreased, and
the fault characteristics that deviate from the normal status
will be more unobvious to be detected. Another reason is that
the frequent switching between different fault patterns also
Fig. 21.
AUC scores of different methods on the faults with different timings
in the scenario of multiple faults.
may lead to more mis-detection. With the least performance
degradation, the detection results of our approach ST-GATrans
consistently outperform the other comparison models when the
fault duration decreases.
Furthermore, we conducted experiments to analyze the
effect of the timing of faults on the performance of different
models. In the previous study on multiple injected faults, test
data with length of 3000 is first divided into six equal parts
[1, 500], [501, 1000], [1001, 1500], [1501, 2000], [2001,
2500], and [2501, 3000]. Then, drift fault, bias fault and
stuck fault are cyclically injected on the fourth segment to
the sixth segment. We set this case of fault injection as
Case 1. In order to analyze the impact of the timing of
fault, another five cases {Case 2, Case 2, Case 3, Case 4,
Case 5} are generated through switching the injection order
of drift faults, bias faults, and stuck faults. The injection
orders of Case 2, Case 3, Case 4, Case 5, and Case 6 are
set as {bias fault, drift fault, stuck fault}, {stuck fault, drift
fault, bias fault}, {drift fault, stuck fault, bias fault}, {bias
fault, stuck fault, drift fault}, and {stuck fault, bias fault, drift
fault}, respectively. For example, in Case 4, the drift fault,
stuck fault, and bias fault are injected into the fourth segment
[1501, 2000], fifth segment [2001, 2500], and sixth segment
[2501, 3000], respectively. The results of different comparison
methods on different timings of faults are presented in the
following Fig. 21. The horizontal coordinates indicate the six
cases with different timing of fault. AUC score is selected
to evaluate the model performance. A model with better
performance will have a higher AUC value close to one. It can
be observed that the performance of different approaches will
fluctuate with the change of the timing of fault. Among them,
the performance of Conv-LSTM fluctuates most seriously.
However, it can be observed that there is no specific pattern
to describe how the timing of fault could affect the model
performance. Meanwhile, with the most stable performance,
our approach ST-GATrans consistently outperforms the other
four comparison models when the timing of fault changes.
d) Discussion on the effect of the unanticipated or more
subtle fault patterns encountered in real UAV operations: In
order to analyze how the more subtle fault patterns encoun-
tered in real UAV operations could affect the reported ACC,
TPR, and FPR. One group of experiments are designed to
test the performance of different comparison models on the
faults with low magnitude. Specifically, in the experiment,
faults with different magnitudes are injected on the test data
and test the detection result of different methods. The detailed
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:14:40 UTC from IEEE Xplore.  Restrictions apply.

## Page 16

2529517
IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 73, 2024
detection results of different comparison approached in three
fault scenarios have been presented in the above Fig. 16. The
amplification factors of the stuck fault denote the multiple
of standard deviation of the training data. The amplification
factors of the bias faults denote the multiple of extreme
deviation. The horizontal coordinates of the detection result
on drift faults is the drift rate. The AUC score is selected
as the vertical coordinate to evaluate the model performance.
The AUC is the area under the ROC curve using the FPR
and TPR as horizontal and vertical coordinates, respectively.
A model with better detection performance will have a higher
AUC value close to one. Meanwhile, a model with higher AUC
value will have higher TPR, ACC, and have lower FPR.
As shown in the above Fig. 16, it can be observed that
the fault detection performance of all comparison methods
will degrade as the fault amplitude decreases. This is because
the features of low-amplitude faults will be easily disrupted
by noise, making it difficult to be detected. In the real UAV
operation, the subtle faults with low amplitude are more prone
to be contaminated by external noise. Hence, when encoun-
tering more subtle fault patterns with lower magnitude in
real UAV operations, the reported detection result of different
methods will be degraded with a lower ACC, lower TPR, and
higher FPR. Similarly, with obvious fault characteristics, the
unanticipated faults with high fault magnitude will be easier to
be detected with a higher TPR, higher ACC, and a lower FPR.
On the contrary, if the magnitude of the unanticipated fault
pattern is quite low or the fault characteristics are not obvious,
the fault detection model may be less effective, resulting in a
lower TPR, lower ACC, and higher FPR. In the future work,
we will cooperate with the professional UAV companies and
build one UAV failure experimental platforms to collect more
fault data from the real UAV operations for model validation.
V. CONCLUSION
In order to enhance the safety and reliability of UAV system,
a novel method named ST-GATrans is proposed to implement
intelligent
fault
detection
through
joint
spatial-temporal
learning on multivariate flight data. Without requirement
on the precise physical model, our approach can precisely
identify system status by automatically mining comprehensive
spatial-temporal features from large amounts of flight data.
In the ST-GATrans, the designed GMSA can effectively extract
the spatial connections among different status variables and
reduce excessive attention on univariate flight data. For the
time-dimension feature extraction, the developed transformer
encoder combining MSA mechanism and CTF operation can
excavate more comprehensive temporal information, in which
MSA can model global temporal dependencies and the CTF
operation can help to capture more local details. Through
modeling the spatial-temporal association, the future values of
flight data can be predicted precisely. In order to eliminate the
negative effect of noise or large fluctuation in flight data, Bi-
AEWMA is designed to smooth the residual sequence, after
which the FPR metric is greatly reduced. A series of validation
experiments on actual UAV flight data are conducted, and the
proposed ST-GATrans has shown more prominent detection
performance compared to other popular approaches. In our
future researches, we will try to integrate the proposed
algorithm into the existing UAV platforms and realize the
real-time fault detection based on online flight data streams.
REFERENCES
[1] Z. Wang et al., “A survey on cybersecurity attacks and defenses
for unmanned aerial systems,” J. Syst. Archit., vol. 138, May 2023,
Art. no. 102870.
[2] A. Abbaspour, P. Aboutalebi, K. K. Yen, and A. Sargolzaei, “Neural
adaptive observer-based sensor and actuator fault detection in nonlin-
ear systems: Application in UAV,” ISA Trans., vol. 67, pp. 317–329,
Mar. 2017.
[3] A. Abbaspour, K. K. Yen, P. Forouzannezhad, and A. Sargolzaei,
“A neural adaptive approach for active fault-tolerant control design
in UAV,” IEEE Trans. Syst., Man, Cybern., Syst., vol. 50, no. 9,
pp. 3401–3411, Sep. 2020.
[4] O. Haim Anidjar, A. Barak, B. Ben-Moshe, E. Hagai, and S. Tuvyahu,
“A stethoscope for drones: Transformers-based methods for UAVs acous-
tic anomaly detection,” IEEE Access, vol. 11, pp. 33336–33353, 2023.
[5] Y. He, Y. Peng, S. Wang, and D. Liu, “ADMOST: UAV flight data
anomaly detection and mitigation via online subspace tracking,” IEEE
Trans. Instrum. Meas., vol. 68, no. 4, pp. 1035–1044, Apr. 2019.
[6] Y. He, Y. Peng, S. Wang, D. Liu, and P. H. W. Leong, “A structured
sparse subspace learning algorithm for anomaly detection in UAV flight
data,” IEEE Trans. Instrum. Meas., vol. 67, no. 1, pp. 90–100, Jan. 2018.
[7] T. Thanaraj, K. H. Low, and B. F. Ng, “Actuator fault detection
and isolation on multi-rotor UAV using extreme learning neuro-fuzzy
systems,” ISA Trans., vol. 138, pp. 168–185, Jul. 2023.
[8] Z. Hou, P. Lu, and Z. Tu, “Nonsingular terminal sliding mode control
for a quadrotor UAV with a total rotor failure,” Aerosp. Sci. Technol.,
vol. 98, Mar. 2020, Art. no. 105716.
[9] C. Hajiyev, D. Cilden-Guler, and U. Hacizade, “Two-stage Kalman filter
for fault tolerant estimation of wind speed and UAV flight parameters,”
Meas. Sci. Rev., vol. 20, no. 1, pp. 35–42, Feb. 2020.
[10] D. Guo, M. Zhong, and D. Zhou, “Multisensor data-fusion-based
approach to airspeed measurement fault detection for unmanned aerial
vehicles,” IEEE Trans. Instrum. Meas., vol. 67, no. 2, pp. 317–327,
Feb. 2018.
[11] L. Liu, Y. Ma, B. Xu, C. Xiang, and X. Yang, “Fault detection and
isolation based on UKFs for a novel ducted fan UAV,” in Proc. IEEE Int.
Conf. Aircr. Utility Syst. (AUS), Beijing, China, Oct. 2016, pp. 212–218.
[12] P. Freeman, R. Pandita, N. Srivastava, and G. J. Balas, “Model-based and
data-driven fault detection performance for a small UAV,” IEEE/ASME
Trans. Mechatronics, vol. 18, no. 4, pp. 1300–1309, Aug. 2013.
[13] J. Zhong, Y. Zhang, J. Wang, C. Luo, and Q. Miao, “Unmanned
aerial vehicle flight data anomaly detection and recovery prediction
based on spatio-temporal correlation,” IEEE Trans. Rel., vol. 71, no. 1,
pp. 457–468, Mar. 2022.
[14] B. Wang, D. Liu, Y. Peng, and X. Peng, “Multivariate regression-based
fault detection and recovery of UAV flight data,” IEEE Trans. Instrum.
Meas., vol. 69, no. 6, pp. 3527–3537, Jun. 2020.
[15] V. Sadhu, S. Zonouz, and D. Pompili, “On-board deep-learning-based
unmanned aerial vehicle fault cause detection and identification,” in
Proc. IEEE Int. Conf. Robot. Autom. (ICRA), Paris, France, May 2020,
pp. 5255–5261.
[16] D. Guo, M. Zhong, H. Ji, Y. Liu, and R. Yang, “A hybrid feature model
and deep learning based fault diagnosis for unmanned aerial vehicle
sensors,” Neurocomputing, vol. 319, pp. 155–163, Nov. 2018.
[17] A. Alos and Z. Dahrouj, “Using MLSTM and multioutput convolutional
LSTM algorithms for detecting anomalous patterns in streamed data of
unmanned aerial vehicles,” IEEE Aerosp. Electron. Syst. Mag., vol. 37,
no. 6, pp. 6–15, Jun. 2022.
[18] J. You, J. Liang, and D. Liu, “An adaptable UAV sensor data anomaly
detection method based on TCN model transferring,” in Proc. Prognos-
tics Health Manage. Conf. (PHM-London), London, U.K., May 2022,
pp. 73–76.
[19] B. Wang, Z. Wang, L. Liu, D. Liu, and X. Peng, “Data-driven anomaly
detection for UAV sensor data based on deep learning prediction model,”
in Proc. Prognostics Syst. Health Manage. Conf. (PHM-Paris), Paris,
France, May 2019, pp. 286–290.
[20] Z. Wu, S. Pan, F. Chen, G. Long, C. Zhang, and P. S. Yu,
“A comprehensive survey on graph neural networks,” IEEE Trans.
Neural Netw. Learn. Syst., vol. 32, no. 1, pp. 4–24, Jan. 2021.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:14:40 UTC from IEEE Xplore.  Restrictions apply.

## Page 17

WANG et al.: FAULT DETECTION FOR UAVs WITH SPATIAL-TEMPORAL LEARNING
2529517
[21] D.-K.
Kim
and
K.
Kim,
“A
convolutional
transformer
model
for
multivariate
time
series
prediction,”
IEEE
Access,
vol.
10,
pp. 101319–101329, 2022.
[22] J. Kim, H. Kang, and P. Kang, “Time-series anomaly detection with
stacked transformer representations and 1D convolutional network,” Eng.
Appl. Artif. Intell., vol. 120, Apr. 2023, Art. no. 105964.
[23] P. Goyal and E. Ferrara, “Graph embedding techniques, applications,
and performance: A survey,” Knowl.-Based Syst., vol. 151, pp. 78–94,
Jul. 2018.
[24] Y. Xie, Z. Xu, J. Zhang, Z. Wang, and S. Ji, “Self-supervised learning
of graph neural networks: A unified review,” IEEE Trans. Pattern Anal.
Mach. Intell., vol. 45, no. 2, pp. 2412–2429, Feb. 2023.
[25] A. Vaswani et al., “Attention is all you need,” in Proc. 31st Int. Conf.
Neural Inf. Process. Syst., 2017, pp. 145–152.
[26] Z. Jia, S. Wang, K. Zhao, Z. Li, Q. Yang, and Z. Liu, “An efficient
diagnostic strategy for intermittent faults in electronic circuit systems
by enhancing and locating local features of faults,” Meas. Sci. Technol.,
vol. 35, no. 3, Mar. 2024, Art. no. 036107.
[27] S. Wang, Z. Liu, Z. Jia, W. Zhao, and Z. Li, “Intermittent fault diagnosis
for electronics-rich analog circuit systems based on multi-scale enhanced
convolution transformer network with novel token fusion strategy,”
Expert Syst. Appl., vol. 238, Mar. 2024, Art. no. 121964.
[28] P. Velickovic, G. Cucurull, A. Casanova, and Y. Bengio, “Graph attention
networks,” in Proc. Int. Conf. Learn. Represent., 2017, pp. 1–12.
[29] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, “BERT: Pre-training
of deep bidirectional transformers for language understanding,” 2018,
arXiv:1810.04805.
[30] Z. Jia, Z. Li, K. Zhao, K. Wang, S. Wang, and Z. Liu, “CNN-DBLSTM:
A long-term remaining life prediction framework for lithium-ion battery
with small number of samples,” J. Energy Storage, vol. 97, Sep. 2024,
Art. no. 112947.
[31] S. Tariq, S. Lee, and Y. Shin, “Detecting anomalies in space using
multivariate convolutional LSTM with mixtures of probabilistic PCA,”
in Proc. 25th ACM SIGKDD Int. Conf. Knowl. Discovery Data Mining,
New York, NY, USA, 2019, pp. 2123–2133.
[32] S. Wang, Z. Liu, Z. Jia, and Z. Li, “Incipient fault diagnosis of
analog circuit with ensemble HKELM based on fused multi-channel
and multi-scale features,” Eng. Appl. Artif. Intell., vol. 117, Jan. 2023,
Art. no. 105633.
[33] B. Wang, X. Peng, M. Jiang, and D. Liu, “Real-time fault detection for
UAV based on model acceleration engine,” IEEE Trans. Instrum. Meas.,
vol. 69, no. 12, pp. 9505–9516, Dec. 2020.
[34] D. Liu, N. Wang, K. Guo, and B. Wang, “Ensemble transfer learning
based cross-domain UAV actuator fault detection,” IEEE Sensors J.,
vol. 23, no. 14, pp. 16363–16372, Jul. 2023.
Shengdong Wang received the B.E. degree in
automation (engineering experimental class) from
Chang’an University, Xi’an, China, in 2020. He is
currently pursuing the Ph.D. degree in means of
aeronautical and astronautical science and technol-
ogy with Northwestern Polytechnical University.
His main research interests include fault diagnosis,
health management and intelligent algorithms.
Zhenbao Liu (Senior Member, IEEE) received the
B.S. and M.S. degrees from Northwestern Polytech-
nical University, Xi’an, China, in 2001 and 2004,
respectively, and the Ph.D. degree from the Uni-
versity of Tsukuba, Tsukuba, Japan, in 2009, all in
electrical engineering and automation.
He was a Visiting Scholar with Simon Fraser
University, Burnaby, BC, Canada, in 2012. He is cur-
rently a Professor with Northwestern Polytechnical
University. His research interests include unmanned
aerial
vehicle
(UAV),
prognostics,
and
health
management.
Mr. Liu is an Associate Editor of IEEE ACCESS.
Zhen Jia received the Ph.D. degree in means of
transport applied engineering from Northwestern
Polytechnical University, Xi’an, China, in 2021.
She is currently a Post-Doctoral Researcher with
the School of Civil Aviation, Northwestern Poly-
technical University. Her main research interests
include prognostics and health management of com-
plex aviation equipment and intelligent diagnosis of
electromechanical equipment.
Yong Tang is currently pursuing the Ph.D. degree with Northwestern
Polytechnical University, Xi’an, China.
He is the Researcher at AVIC UAS Company Ltd., Chengdu, Xi’an.
Guozhu Zhi is currently pursuing the Ph.D. degree with Northwestern
Polytechnical University, Xi’an, China.
He is the Researcher at Qingan Group Company Ltd., China.
Xiao Wang received the B.Sc. and M.Sc. degrees
from
Northwestern
Polytechnical
University
(NWPU),
Xi’an,
China,
in
2013
and
2016,
respectively, and the Ph.D. degree from the Institute
of Information Engineering, Chinese Academy of
Sciences, Beijing, China, in 2022.
He is currently a Post-Doctoral Researcher at
the School of Civil Aviation, NWPU. His research
interests include image enhancement, unmanned
aerial vehicle (UAV) image processing, and machine
learning.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:14:40 UTC from IEEE Xplore.  Restrictions apply.
