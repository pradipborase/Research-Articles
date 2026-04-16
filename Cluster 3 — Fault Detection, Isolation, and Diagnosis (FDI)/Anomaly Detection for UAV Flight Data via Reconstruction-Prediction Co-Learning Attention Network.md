# Anomaly Detection for UAV Flight Data via Reconstruction-Prediction Co-Learning Attention Network.pdf

## Page 1

IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 74, 2025
3553013
Anomaly Detection for UAV Flight Data via
Reconstruction–Prediction Co-Learning
Attention Network
Zeyi Zhou , Jie Zhong , Yujie Zhang , Member, IEEE, and Qiang Miao , Senior Member, IEEE
Abstract—With the increasing deployment of unmanned aerial
vehicles (UAVs) in critical applications, ensuring the accuracy and
reliability of their onboard measurement systems is paramount.
The anomaly detection (AD) in UAV ﬂight control systems plays
a crucial role in identifying deviations in the sensor data that
may indicate system malfunctions. Traditional AD methods often
rely on single-task models, such as prediction or reconstruction,
which struggle to detect anomalies in complex ﬂight data. While
multitask approaches aim to combine these tasks, they often
suﬀer from task conﬂicts or fail to properly aggregate losses,
limiting their ability to prioritize anomaly-sensitive patterns.
To overcome this limitation, a novel reconstruction–prediction
co-learning attention network (RPCA-Net) is proposed. RPCA-
Net integrates both prediction and reconstruction tasks into
a uniﬁed framework, utilizing convolutional neural networks
(CNNs) for feature extraction and long short-term memory
(LSTM) networks to capture temporal dependencies in the data.
Attention mechanisms are incorporated for both tasks. The
temporal attention is designed for the prediction task, while the
channel attention is applied to the reconstruction task, enhancing
the model’s ability to focus on key features and improving its
performance in AD. Furthermore, a custom loss function that
combines prediction error and reconstruction error is designed
to increase the model’s sensitivity to anomalies. Experimental
results with the practical data demonstrate that RPCA-Net
achieves superior performance in detecting a wide range of ﬂight
parameter faults, outperforming contrast methods in terms of
detection accuracy and robustness.
Index Terms—Anomaly detection (AD), deep learning, ﬂight
data, joint prediction and reconstruction, unmanned aerial
vehicle (UAV).
I. INTRODUCTION
U
NMANNED aerial vehicles (UAVs) play a crucial
role in logistics, environmental monitoring, and infras-
tructure inspection, generating vast amounts of multivariate
spatiotemporal data from onboard sensors [1]. The accurate
Received 1 April 2025; revised 2 July 2025; accepted 18 July 2025. Date of
publication 29 July 2025; date of current version 12 August 2025. This work
was supported in part by the National Natural Science Foundation of China
under Grant 62303335 and Grant 52075349, in part by Sichuan Science and
Technology Program under Grant 2025YFHZ0157, in part by the Open Fund
of Intelligent Control Laboratory under Grant 2024ZKSYSKF0304, and in
part by China Postdoctoral Science Foundation under Grant 2022M712234.
The Associate Editor coordinating the review process was Dr. Marco Carrat`u.
(Corresponding author: Yujie Zhang.)
The authors are with the College of Electrical Engineering, Sichuan
University,
Chengdu
610065,
China
(e-mail:
zhangyj@scu.edu.cn;
mqiang@scu.edu.cn).
Digital Object Identiﬁer 10.1109/TIM.2025.3593530
measurement and interpretation of these sensor data are essen-
tial for ensuring UAV reliability, as system failures—often
caused by sensor degradation, motor faults, or control system
malfunctions—account for over 50% of military UAV inci-
dents and 86.54% of civilian UAV accidents [2], [3]. These
failures often manifest as anomalies in ﬂight parameters—such
as altitude, velocity, and attitude angles—which are critical
indicators of sensor degradation, environmental perturbations,
or control system malfunctions. Consequently, precise and
robust anomaly detection (AD) methodologies are required
to enhance UAV safety by identifying abnormal measurement
patterns and mitigating operational risks [4].
AD, as a fundamental measurement science technique,
enables proactive fault diagnosis by identifying deviations
from expected sensor data behavior. UAV ﬂight parameters
are typically recorded as multivariate time series, where
AD aims to detect anomalous data points or subsequences
while considering temporal dependencies and cross-sensor
correlations [5]. Given that UAV anomalies often emerge
due to complex interactions among interdependent ﬂight
parameters, eﬀective measurement frameworks must leverage
advanced signal processing, feature extraction, and machine
learning models to enhance the accuracy of anomaly iden-
tiﬁcation. Furthermore, as UAV instrumentation systems
increasingly integrate heterogeneous sensing modalities, devel-
oping methodologies that improve the precision, robustness,
and adaptability of AD in real-world ﬂight operations remains
a critical challenge.
AD methods can be broadly classiﬁed into three categories:
knowledge-based, model-based, and data-driven methods [5],
[6]. Knowledge-based methods rely on domain expertise
encoded in a knowledge base, using logical rules to detect
anomalies [7]. In the context of UAV ﬂight data AD, a
comprehensive knowledge base can be constructed by sum-
marizing domain-speciﬁc expert experiences and knowledge,
including the typical ranges of parameters and joint anomalies
over speciﬁc periods. While knowledge-based methods can
enhance AD accuracy, they are limited by the need for
extensive domain-speciﬁc knowledge and often fail to account
for unforeseen anomalies.
Model-based methods construct precise physical models of
systems to compare the actual data with predictions [8]. These
methods rely on simulating the normal operating state of
the system and detecting discrepancies between the predicted
1557-9662 © 2025 IEEE. All rights reserved, including rights for text and data mining, and training of artiﬁcial intelligence and
similar technologies. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:26:48 UTC from IEEE Xplore.  Restrictions apply.

## Page 2

3553013
IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 74, 2025
and actual data. For example, Zolghadri et al. [9] applied
model-based fault detection to aircraft electrical ﬂight control
systems, using real ﬂight data and Airbus test benchmarks.
Freeman et al. [8] combined robust linear ﬁltering with the data
analysis to generate system state estimates and isolate actuator
faults in UAVs. These methods are theoretically grounded,
oﬀering high-precision AD when the system dynamics are
well-understood. However, they struggle in the face of com-
plex or evolving conditions, leading to potential false positives
or missed detections.
In contrast, data-driven machine learning methods have
gained attention for UAV AD due to their ability to analyze
the ﬂight data directly and adapt to complex system behaviors.
For instance, Baskaya et al. [10] used support vector machines
(SVMs) to classify aircraft behavior during normal and fault
stages, achieving accurate fault detection. Al-Haddad et al.
[11] applied machine learning algorithms, such as stochastic
gradient descent, K-nearest neighbors (KNNs), and SVM
to improve the accuracy of UAV fault detection. Similarly,
Altinors et al. [12] used decision tree, SVM, and KNN
algorithms to detect common UAV motor faults, achieving
high accuracy with low computational cost. However, these
methods typically rely on the labeled data for training, which is
often diﬃcult and expensive to obtain in real-world scenarios.
This limitation has led to the growing adoption of deep
learning-based unsupervised methods, which do not require
prior anomaly knowledge and are better equipped to capture
complex, often hidden relationships within the ﬂight data.
Currently, deep learning-based AD methods involve two
important approaches: prediction-based and reconstruction-
based methods [13], [14]. Prediction-based methods utilize
historical patterns to estimate future values and identify
anomalies by assessing the deviation between predicted and
actual observations. If the deviation surpasses a deﬁned thresh-
old, the instance is ﬂagged as anomalous [15]. This approach
is eﬀective in scenarios where the time series follows stable
and predictable trends, but its performance may degrade
when handling rapidly ﬂuctuating or highly dynamic data.
Reconstruction-based methods, in contrast, aim to encode
the intrinsic structure of normal data by training models
to reconstruct input sequences. Anomalies are detected by
evaluating the reconstruction error—the diﬀerence between
the input and its reconstructed counterpart [16]. Instances
that exhibit unusually high reconstruction errors are likely
to be anomalous. Compared with prediction-based methods,
reconstruction-based approaches do not require future obser-
vations, making them more suitable for capturing irregular
patterns in complex time series. Wang et al. [17] pro-
posed a data-driven multivariate regression approach based on
long short-term memory (LSTM) with residual ﬁltering for
UAV ﬂight data fault detection and recovery, demonstrating
improved performance in both tasks. Luo et al. [18] proposed
a fault detection method for motor monitoring data, which
integrates tacholess order tracking and order harmonic extrac-
tion to address cross-condition challenges, achieving high
accuracy. Lu et al. [19] proposed a multirate-aware LSTM
network for AD, which captures temporal dependencies in
time series with varying sampling rates and demonstrated
superior performance. The method in [20] reconstructs altitude
measurement channels via symbolic regression and multisen-
sor fusion, dynamically suppressing sensor anomalies through
residual-aware conﬁdence adaptation while preserving sys-
tem observability. Liu et al. [16] proposed BeatGAN, an
unsupervised reconstruction model for time-series AD, which
provides a framework to adversarially learn to reconstruct and
improve the detection accuracy. These methods each have dis-
tinct advantages. Prediction-based methods excel at detecting
short-term trends, as they leverage complex dynamics within
time-series data to guide the model in capturing temporal
dependencies [21]. On the other hand, reconstruction-based
methods are better at identifying global pattern anomalies.
However, prediction-based methods face challenges in han-
dling fast and continuous time-series changes. As the number
of time steps increases, prediction errors tend to accumulate,
leading to lower accuracy and limiting the eﬀectiveness of
prediction models over longer periods [22]. Reconstruction
methods, while eﬀective at identifying pattern anomalies,
struggle with interference from anomalous data during the
learning process. Since the number of anomalies is unknown
and both normal and anomalous data points may appear in the
same sequence, it is diﬃcult for the model to learn a stable
representation of normal patterns [23].
Due to these limitations, relying solely on the pre-
diction or reconstruction methods is insuﬃcient to fully
address complex time-series AD tasks. Although recent
dual-task approaches seek to integrate these tasks, they
often encounter task conﬂicts, where shared representations
inadequately balance temporal dynamics and spatial hier-
archies or they fail to consider the aggregation of losses,
which limits their ability to prioritize patterns indicative of
anomalies. To overcome these limitations, a novel method
called reconstruction–prediction co-learning attention network
(RPCA-Net) is proposed. RPCA-Net integrates convolutional
neural networks (CNNs) and LSTM networks and employs
distinct attention mechanisms to optimize the outputs of both
prediction and reconstruction tasks. By integrating prediction-
based short-term variation capture and reconstruction-based
global pattern recovery, RPCA-Net enables multiscale AD in
UAV ﬂight data, oﬀering a comprehensive and robust solution
that leverages dual-task synergy. The main contributions of
our study are as follows.
1) A design of the joint prediction and reconstruction
model is carried out. A joint model combining prediction
and reconstruction channels is designed to address the
AD problem in the UAV ﬂight data. The model ﬁrst
extracts data features through the CNN–LSTM lay-
ers, while incorporating diﬀerent attention mechanisms
to enhance the model’s learning of speciﬁc temporal
features and global information, thereby improving its
performance in complex scenarios.
2) A custom loss function structure is developed. To eﬀec-
tively combine the prediction and reconstruction tasks,
a custom loss function is designed. The loss function
utilizes the mean squared error (mse) loss and Huber loss
to optimize the outputs of the two channels, respectively.
In addition, a cosine similarity (CS)-based correlation
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:26:48 UTC from IEEE Xplore.  Restrictions apply.

## Page 3

ZHOU et al.: AD FOR UAV FLIGHT DATA VIA RECONSTRUCTION–PREDICTION CO-LEARNING ATTENTION NETWORK
3553013
loss is introduced to encourage the model to maintain
feature consistency between the outputs. By evaluating
the similarity between prediction and reconstruction
outputs, the model’s ability to detect anomalous patterns
is further enhanced.
3) The experimental validation is conducted. AD is per-
formed on the real UAV data containing various faults.
The eﬀectiveness of our method is veriﬁed through com-
parison with other methods using multiple evaluation
metrics. During the training process, only unlabeled nor-
mal ﬂight data are used, while data containing anomalies
are solely used for testing.
II. METHODOLOGIES
A. 1-D Convolution
In the RPCA-Net model, the feature extraction process
begins with a 1-D CNN, which is designed to eﬀectively
capture local features within time-series data. The 1-D CNN
applies a convolutional operation over the input time series in
a sliding window manner, focusing on extracting short-term
dependencies. Let the input time series be X = [x1, x2, . . ., xT],
where T represents the sequence length, and the convolutional
operation employs a kernel of size k and a stride of s. The
output of the convolutional operation can be expressed as
follows:
zi =
k−1
X
j=0
W jxi·s+j + b
(1)
where W j represents the weight of the convolutional kernel,
while b and zi denote the bias term and the ith element of the
output sequence Z = [z1, z2, . . ., zT ′], respectively. By sliding
the kernel across the input sequence, the 1-D CNN generates
multiple feature maps, capturing signiﬁcant patterns and local
dependencies in the input data. These feature maps improve
the model’s discriminative capacity for identifying abnormal
patterns.
To improve training stability and accelerate convergence,
batch normalization (BN) is applied after the convolutional
operation. BN normalizes the input to each layer, reducing
internal covariate shift and maintaining stable input distri-
butions. For a given convolutional output zi within a batch,
BN performs the following transformation:
ˆzi =
zi −µB
q
σ2
B + ϵ
· γ + β
(2)
where µB and σ2
B denote the mean and variance of the current
batch, respectively. ϵ serves as a numerical stability term to
avoid denominator collapse, while γ and β constitute train-
able aﬃne transformation parameters for feature recalibration.
By standardizing the intermediate feature maps, BN enables
the model to adapt more eﬀectively to data distributions during
training and ensures improved generalization and robustness
in AD tasks.
B. Long Short-Term Memory Network
LSTM is a variant of recurrent neural networks (RNNs)
proposed by Schmidhuber et al. [24]. It is designed to mitigate
Fig. 1. Structure of LSTM.
Fig. 2. Structure of the dual-attention mechanism.
gradient instability issues encountered by standard RNNs
when processing long sequences, thereby enabling robust
capture of distant temporal relationships. Unlike the simple
hidden layer structure in ordinary RNNs, which contains only
a single Sigmoid or Tanh activation function, LSTM employs
a more complex memory cell structure, as shown in Fig. 1.
The architecture employs three regulatory gates to control the
information ﬂow
ft = σ
W f [ht−1; xt] + bf

(3)
it = σ (Wi [ht−1; xt] + bi)
(4)
˜Ct = tanh (WC [ht−1; xt] + bC)
(5)
Ct = ft ⊙Ct−1 + it ⊙˜Ct
(6)
ot = σ (Wo [ht−1; xt] + bo)
(7)
ht = ot ⊙tanh (Ct)
(8)
where σ is the sigmoid activation, ⊙denotes the elementwise
multiplication, and [·; ·] represents the vector concatenation.
The forget gate ( ft) controls information retention, the input
gate (it) regulates new information integration, and the output
gate (ot) determines the hidden state updates. This gating
mechanism eﬀectively prevents vanishing/exploding gradients
while capturing complex temporal dependencies in ﬂight data.
C. Dual-Attention Mechanism
The introduction of attention mechanisms in time-series AD
tasks can eﬀectively improve the model performance [15],
[25]. As shown in Fig. 2, two attention mechanisms are
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:26:48 UTC from IEEE Xplore.  Restrictions apply.

## Page 4

3553013
IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 74, 2025
introduced: a temporal attention mechanism for the prediction
task and a channel attention mechanism for the reconstruction
task, to enhance the model’s ability to capture key features in
processing UAV ﬂight data. The outputs of the two attention
mechanisms are fused downstream by concatenation, serving
as the complete output for the model.
1) Temporal Attention Mechanism: In the prediction task, a
self-attention-based multihead attention mechanism is adopted.
The core idea of this mechanism is to dynamically adjust
the importance weights of diﬀerent time steps by calculating
the dependencies between diﬀerent time steps in the input
sequence, thereby improving the model’s ability to model
temporal dependencies.
The computational process of the temporal attention mech-
anism involves constructing “query” (Q), “key” (K), and
“value” (V) matrices from the representation of the input
sequence X. Speciﬁcally, given an input sequence X ∈RT×d,
where T is the sequence length and d is the feature dimension,
Q, K, and V are computed as follows:
8
ˆ<
ˆ:
Q = XWQ
K = XWK
V = XWV
(9)
where WQ ∈Rd×dk, WK ∈Rd×dk, and WV ∈Rd×dv are
the learnable weight matrices for the query, key, and value,
respectively. Once Q, K, and V are obtained, the attention
weights are calculated using the following formula:
Attention (Q, K, V) = softmax
QKT
√dk

V.
(10)
In this process, dk is the dimension of the key vector, which
is used to scale the dot product between Q and K, ensuring
numerical stability during the softmax operation. The result
of the attention mechanism is a weighted sum of the value
vectors V, where the weights are determined by the similarity
between the query and key vectors. The multihead attention
mechanism performs this process in parallel across multiple
heads, concatenates the outputs from each head, and applies
a linear transformation to generate richer temporal features
MultiHead (X) = Concat (head1, . . ., headh) WO
(11)
where each headi is calculated as follows:
headi = Attention
QWQi, KWKi, VWVi

.
(12)
Multihead attention allows the model to capture long-range
dependencies in the sequence and generates feature represen-
tations that incorporate the global temporal information.
2) Channel Attention Mechanism: The channel attention
was initially applied to extract image features and has been
demonstrated in recent studies to exhibit excellent capabilities
in time-series feature extraction and fault detection [26]. In the
reconstruction task, a channel attention mechanism is applied
over the hidden feature dimensions output by the preceding
feature extractor, in order to dynamically reweight channels
based on their task-speciﬁc importance. The computation
process can be represented as follows:
Achannel = σ (W2 · ReLU (W1 · X))
(13)
where X represents the input feature matrix. W1 and W2 are
learnable weight matrices and σ is the Sigmoid activation that
scales the output to [0, 1]. The computed channel weights
are elementwise multiplied by the feature channels to obtain
the weighted channel features. This mechanism dynamically
adjusts the contribution of each channel to the reconstruction
task, highlighting the most important feature channels for
reconstruction. The ﬁnal weighted features are input into
the subsequent layers of the network for further use in the
reconstruction task.
In the joint prediction and reconstruction framework, the
temporal attention and channel attention mechanisms are
applied to diﬀerent tasks, allowing the model to focus on
both the long-range dependencies of time-series data and the
importance of diﬀerent feature channels.
D. Custom Loss Function
The custom loss function proposed combines the errors of
the prediction task, the reconstruction task, and the similarity
across tasks to improve the model’s performance in AD of
UAV ﬂight data.
For the prediction task, the primary reason for using the
Huber loss is its robustness to outliers [27]. The Huber loss
function is deﬁned as follows:
LH
yp, ˆyp

=
8
ˆ<
ˆ:
1
2 (y −ˆy)2 ,
if |y −ˆy| ≤δ
δ

|y −ˆy| −1
2δ

,
if |y −ˆy| > δ
(14)
where ˆy is the model’s predicted output at a given time
step, while y is the corresponding true value, and δ is a
hyperparameter that controls the sensitivity of the loss. The
Huber loss combines the advantages of both mse and abso-
lute error. When the prediction error is small (less than the
threshold δ), it behaves like mse, eﬀectively penalizing small
prediction errors; while for larger errors, it transitions to the
absolute error, thus reducing the inﬂuence of outliers on the
loss. For UAV ﬂight data, the Huber loss helps the model
better handle the presence of noise and outliers, improving
the model’s stability and generalization capability.
For the reconstruction task, mse is used to measure the
diﬀerence between the model’s reconstruction output and the
original input, deﬁned as follows:
LM (yr, ˆyr) = 1
n
n
X
i=1
(yr −ˆyr)2
(15)
where ˆyr is the model’s reconstruction output at time step n
and yr is the corresponding true value. In the calculation, mse
squares the error for each feature, emphasizing larger errors,
which encourages the model to focus more on accurately
matching the reconstruction output to the input data, ensuring
that the model can accurately reproduce the features of the
input data and thereby improve the quality and eﬀectiveness
of the reconstruction.
In addition, the CS loss is incorporated into the loss func-
tion to introduce cross-task correlation, measuring the feature
alignment between the prediction and reconstruction tasks.
This alignment encourages the two tasks to learn consistent
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:26:48 UTC from IEEE Xplore.  Restrictions apply.

## Page 5

ZHOU et al.: AD FOR UAV FLIGHT DATA VIA RECONSTRUCTION–PREDICTION CO-LEARNING ATTENTION NETWORK
3553013
Fig. 3. Architecture comparison of four approaches.
representations rather than diverging toward their own local
optima. By minimizing the angular distance between their
feature outputs, the CS loss eﬀectively reduces task conﬂict,
ensuring that shared representations are mutually beneﬁcial
rather than competitive. This promotes more stable optimiza-
tion and facilitates knowledge sharing between the prediction
and reconstruction branches. Speciﬁcally, the prediction output
is compared with the last time step of the reconstruction result,
and the similarity loss is deﬁned by CS as follows:
Lcos
ˆyp, ˆyr [−1]

= 1 −
ˆyp · ˆyr [−1]
ˆyp
 ∥ˆyr [−1]∥
(16)
where yr[−1] represents the last time step of the reconstruction
output.
The ﬁnal loss function is a combination of the predic-
tion loss, reconstruction loss, and similarity loss, deﬁned as
follows:
L = α · LH
yp, ˆyp

+ (1 −α) LM (yr, ˆyr)
+ Lcos
ˆyp, ˆyr [−1]

(17)
where α is a hyperparameter that controls the weight of LH
and LM to balance the contributions of each loss term.
Fig. 3 highlights RPCA-Net’s architectural distinctions from
representative AD models [23], [28]. While BeatGAN relies
solely on adversarial reconstruction and dual-task ADNet
employs shared-encoder multitasking, RPCA-Net implements
physically separated prediction/reconstruction branches with
task-speciﬁc
attention
mechanisms.
Unlike
DCDetector’s
pattern-disentanglement approach, RPCA-Net uniquely inte-
grates temporal–channel attention specialization and enforces
task coordination via CS alignment, enabling the synergistic
feature learning while minimizing interference.
III. PROPOSED FRAMEWORK
Before applying the proposed method, the collected ﬂight
data undergoes preprocessing, including frequency align-
ment, interpolation, normalization, and segmentation, to ensure
consistency and facilitate model input. After preprocessing,
temporal features are extracted to enhance the representative-
ness of the input. Then, AD is performed using the proposed
RPCA-Net model. As illustrated in Fig. 4, the framework
integrates data preprocessing, feature extraction, and AD into
a uniﬁed pipeline. The speciﬁc details are as follows.
A. Modeling Based on RPCA-Net
In the RPCA-Net model, feature extraction of time-series
data is ﬁrst performed using a 1-D CNN, as shown in (18).
Here, fconv denotes the mapping function based on the convolu-
tional and BN operations deﬁned in (1) and (2). Subsequently,
the convolutional output is fed into the LSTM network to
capture both short- and long-term dependencies in the time
series, as described in (19), where
fLSTM represents the
mapping function based on the LSTM computations outlined
in (3)–(8)
Z = fconv (X)
(18)
Y = fLSTM (Z)
(19)
where X, Z, and Y represent the input data, the output of the
convolutional layer, and the ﬁnal output after passing through
the LSTM network, respectively.
On top of the CNN–LSTM layer outputs, the aforemen-
tioned two attention mechanisms are introduced to enhance
the model’s focus on important features: a temporal atten-
tion mechanism and a channel attention mechanism. In the
prediction path, the time-step attention is computed based on
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:26:48 UTC from IEEE Xplore.  Restrictions apply.

## Page 6

3553013
IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 74, 2025
Fig. 4. Schematic of the proposed RPCA-Net method.
the multihead self-attention mechanism to obtain the predicted
output ˆypred as follows:
ˆypred = fFC
Temporal Attention (Y)

(20)
where fFC is the fully connected layer used for the prediction
task, and the temporal attention is the multihead attention
computation operation as deﬁned in (9)–(12).
In the reconstruction path, the channel attention mechanism
generates channel weights through a linear transformation, and
the reconstruction output ˆyrecon is computed as follows:
ˆyrecon = fFC (Y ⊙Channel Attention (yi))
(21)
where fFC is the fully connected layer for the reconstruction
task and the channel attention is the attention computational
operation as deﬁned in (13). With the addition of time-
step and channel attention mechanisms, the features from the
CNN–LSTM layer generate both the prediction result ˆypred and
the reconstruction result ˆyrecon. These outputs are optimized
using the joint loss function.
B. Anomaly Criterion
Unsupervised AD fundamentally operates by training mod-
els exclusively on nominal operational data to characterize
standard system behavior patterns [29]. When the model
receives data containing anomalies, the model ﬁnds it diﬃcult
to represent this data accurately because it deviates from the
normal patterns, leading to an increase in the anomaly score.
To quantify this characteristic, an anomaly score needs to be
deﬁned. For normal data, the model learns to produce lower
loss values during training, so the anomaly score for normal
data is low, while for anomalous data, the anomaly score will
be high.
The anomaly score is computed based on the loss values
during the training process. While the model exhibits lower
prediction and reconstruction losses when handling normal
data, anomalous data leads to higher losses. Therefore, a for-
mula similar to the loss function can be designed to compute
the anomaly score. In addition, considering that the impact
of prediction loss and reconstruction loss on AD might diﬀer,
diﬀerent weights are set for each and then summed, which
serves as the ﬁnal method for calculating the anomaly score.
The anomaly score is deﬁned as follows:
a-score = w · LH
yp,ˆyp

+ (1 −w) · LM (yr, ˆyr)
(22)
where w and 1 −w are the weights for the prediction loss
and reconstruction loss, respectively, determined to minimize
the anomaly score for normal data. LH and LM represent the
prediction and reconstruction losses, respectively. The CS loss
is excluded from the anomaly score as it is designed solely to
align the feature representations during training, rather than to
serve as a direct indicator for the anomalous behavior during
inference.
The proposed AD method learns the intrinsic patterns of
normal time-series data by training the model to perform
both step-by-step prediction and reconstruction within a time
window. Prediction is optimized via Huber Loss, while recon-
struction is guided by minimizing mse. After training, anomaly
scores are computed for each time point based on the model
outputs. A detection threshold T is set using the percentile
of scores from normal data. During testing, if a time point’s
anomaly score exceeds T, it is ﬂagged as potentially anoma-
lous. The AD criterion is deﬁned as follows:
Anomaly =
(
1,
a-score > T
0,
a-score ≤T
(23)
where anomaly score is the computed score and T is the preset
threshold.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:26:48 UTC from IEEE Xplore.  Restrictions apply.

## Page 7

ZHOU et al.: AD FOR UAV FLIGHT DATA VIA RECONSTRUCTION–PREDICTION CO-LEARNING ATTENTION NETWORK
3553013
TABLE I
ALFA DATASET DESCRIPTION
Fig. 5. Sample data variation curve.
IV. EXPERIMENTAL RESULTS AND ANALYSIS
A. Introduction of Experimental Dataset
To validate the eﬀectiveness of the proposed method, the
AirLab Fault and Anomaly (ALFA) dataset [30] provided by
Carnegie Mellon University is employed. This dataset was
collected by Keipour et al. [30] and is designed speciﬁcally
for aircraft fault detection and isolation, as well as AD
research. It contains various fault types from 47 autonomous
ﬂights of the ﬁxed-wing drone Carbon-Z T-28. As shown in
Table I, the dataset includes 23 instances of engine failure and
seven control surface (actuator) failure scenarios. The dataset
includes a total of 66 min of normal ﬂight data and 13 min of
postfault ﬂight data. We speciﬁcally focus on engine failure
data, as engine failure, being a key component of the aircraft,
can directly aﬀect ﬂight safety. An example of feature data
variations for samples containing engine faults is shown in
Fig. 5. The vertical line in the ﬁgure represents the point where
hardware faults were injected, with the subsequent data points
indicating anomalies.
B. Evaluation Metrics and Data Preprocessing
Before model training and evaluation, UAV ﬂight data
must be rigorously preprocessed due to the heterogeneity in
Fig. 6. Data preprocessing process.
sensor sampling rates and sequence lengths. UAV telemetry
often consists of multiple asynchronous sensors, resulting in
misaligned features and missing values across time steps.
A structured preprocessing pipeline is applied to ensure data
consistency and suitability for time-series AD, as illustrated
in Fig. 6.
The preprocessing begins with frequency alignment. All
sensor signals are upsampled to match the highest sampling
frequency using timestamps as a common reference. This
ensures that all features share a uniﬁed time axis. During
alignment, missing values are introduced due to diﬀering
original frequencies; these are imputed using nearest neighbor
interpolation, which preserves temporal continuity by assign-
ing the closest available value. In addition, for features that
are missing at the beginning of a ﬂight record (e.g., due to
delayed activation of a sensor), the zero padding is applied to
maintain consistent input dimensions across samples.
Following upsampling, redundant values may be introduced,
increasing computational overhead without contributing mean-
ingful information. To mitigate this, the downsampling is
conducted to remove duplicate or overly dense points, thereby
improving the eﬃciency without compromising data integrity.
After temporal alignment, the data are segmented using a
ﬁxed-size sliding window. This operation generates overlap-
ping subsequences from the continuous time series, allowing
the model to capture both short-term dynamics and long-term
patterns. Each window serves as an independent training or
testing sample, ensuring consistent input shapes for the model.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:26:48 UTC from IEEE Xplore.  Restrictions apply.

## Page 8

3553013
IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 74, 2025
Finally, to eliminate scale diﬀerences across sensor modal-
ities, z-score normalization is applied
x = xr −µ
s
(24)
where xr, µ, and s represent the raw value, the mean, and the
standard deviation of each feature, respectively. This transfor-
mation ensures that each feature contributes equally during
model optimization, avoiding bias toward high-magnitude
features.
To comprehensively evaluate the performance of the model,
several common evaluation metrics are used, including preci-
sion, recall, F1-score, receiver operating characteristic (ROC)
curve, and area under curve (AUC). Precision measures the
proportion of truly anomalous samples among those predicted
as anomalies, reﬂecting the model’s accuracy in detecting
anomalies. Recall, on the other hand, represents the propor-
tion of actual anomalous samples correctly identiﬁed, and is
used to assess the model’s ability to avoid false negatives.
F1-score is the harmonic mean of precision and recall, pro-
viding a balance between the two, especially useful when there
is a tradeoﬀbetween precision and recall. The formulas for
calculating precision, recall, and F1-score are given in the
following equations:
Precision =
TP
TP + FP
(25)
Recall =
TP
TP + FN
(26)
F1-score = 2 × Precision × Recall
Precision + Recall.
(27)
In addition, the ROC curve illustrates the model’s perfor-
mance at various thresholds, plotting the false positive rate
(FPR) against the true positive rate (TPR). AUC represents the
area under the ROC curve, with values closer to 1 indicating
better classiﬁcation performance.
C. Experimental Setup and Baseline Methods
The experiments in this study are conducted on a com-
puter equipped with an NVIDIA GeForce RTX 4090 GPU,
running Windows as the operating system. The development
environment is built on Anaconda, with PyTorch 2.10 serving
as the primary deep learning framework. All experiments are
implemented using the Python programming language.
The RPCA-Net model proposed in this study is compared
with prediction-based algorithms: LSTM [31], TSMixer [32],
iTransformer [33], TimesNet [34], reconstruction-based algo-
rithms: LSTM-VAE [35], deep autoencoding Gaussian mixture
model (DAGMM) [36], and dual-task algorithms: MTAD-GAT
[37], USAD-M [38], and MSCRED [39]. LSTM-based AD is
a prediction-based method using an LSTM model to capture
temporal dependencies in the data. TSMixer uses a mixer
layer that processes the dependencies between input sequences
through stacked multilayer perceptrons, while iTransformer
addresses temporal modeling issues by adjusting the Trans-
former architecture. Both are state-of-the-art prediction models
that leverage their predictive capabilities for AD. TimesNet
converts 1-D time-series data into 2-D tensors, allowing it to
TABLE II
ENGINE FAILURE SAMPLES AND CORRESPONDING
FAULT INJECTION TIMES
eﬀectively capture complex temporal patterns for AD. LSTM-
VAE combines LSTM with a variational autoencoder (VAE)
to capture both the temporal features of time series and
the latent space distribution, enabling the model to perform
reconstruction and prediction tasks. DAGMM integrates a
deep autoencoder with a Gaussian mixture model to achieve
data reconstruction, leveraging dimensionality reduction for
feature extraction and clustering to identify anomalies. MTAD-
GAT leverages temporal and graph attention mechanisms for
AD. USAD-M incorporates multitask learning into the USAD
framework, while MSCRED uses multiscale convolutional
representations to reconstruct and detect anomalies.
D. Experimental Results
In the experiments, only normal ﬂight data without anoma-
lies is used for training. The training set includes the “no
fault” data from Table I and the normal phases of partial
fault ﬂight records, while the remaining ﬂight data con-
taining anomalies are used for testing. For example, in the
main experiment on engine failure, the corresponding ﬁle
names and fault injection times are summarized in Table II.
The table covers 13 ﬂights conducted between July and
October 2018, with fault injection times ranging from approx-
imately 49–133 s. Table III presents the detection results
for four typical faults (engine, aileron, elevator, and rudder
faults) using various methods. For the engine fault with the
most data, RPCA-Net achieved the best performance, with
an F1-score of 94.02%, signiﬁcantly outperforming baseline
models such as LSTM (88.23%) and DAGMM (89.90%).
In the aileron fault scenario, RPCA-Net also achieved the high-
est F1-score (88.15%), followed by LSTM-VAE (85.49%) and
LSTM (83.56%). Among the multitask methods, MTAD-GAT
performed relatively well with an F1-score of 80.85%, while
USAD-M and MSCRED showed limited detection capability
in this case.
For elevator fault detection, RPCA-Net achieved the
second-best F1-score (90.76%), slightly lower than LSTM-
VAE (90.90%). DAGMM and TSMixer performed noticeably
worse, with F1-scores of 69.46% and 68.45%, respectively.
In rudder fault detection, RPCA-Net again delivered the best
result (F1 = 99.14%), showing strong robustness in complex
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:26:48 UTC from IEEE Xplore.  Restrictions apply.

## Page 9

ZHOU et al.: AD FOR UAV FLIGHT DATA VIA RECONSTRUCTION–PREDICTION CO-LEARNING ATTENTION NETWORK
3553013
TABLE III
AD RESULTS FOR ENGINE, AILERON, ELEVATOR, AND RUDDER FAULTS
TABLE IV
MODEL COMPLEXITY: PARAMETERS AND FLOPS COMPARISON
scenarios. MTAD-GAT also achieved high accuracy (98.31%),
close to that of RPCA-Net, while USAD-M and MSCRED
performed reasonably well but still fell short, highlighting their
limitations in modeling complex fault dynamics.
The computational analysis in Table IV reveals that RPCA-
Net’s parameter count (8.03M) mainly stems from its LSTM
modules (512 hidden units) and CNN feature extractor, which
together capture both spatial and temporal patterns in ﬂight
data. Although its complexity exceeds lightweight baselines,
its computational cost (137.24M FLOPs) remains reason-
able for UAV deployment—signiﬁcantly lower than TimesNet
(609.16M FLOPs) and comparable to LSTM-VAE (128.02M
FLOPs). Moreover, the adoption of a sliding window approach
ensures linear runtime scaling with data volume, guaranteeing
long-term feasibility as telemetry expands.
In contrast, models such as TimesNet and iTransformer
either incur excessive computation or rely heavily on global
temporal modeling, while USAD-M and MSCRED struggle to
represent high-frequency, nonstationary signals. These limita-
tions render them less eﬀective for UAV AD. In comparison,
Fig. 7. AD ROC curves.
the other models achieved better F1-scores. Therefore, we
further plotted the ROC curves for these ﬁve models for
a comprehensive comparison. As shown in Fig. 7, RPCA-
Net consistently achieved the highest AUC value across all
fault detection tasks, indicating that it can correctly identify
anomalies with a higher probability at various classiﬁcation
thresholds, while minimizing the misclassiﬁcation of normal
samples as anomalies, demonstrating excellent robustness.
Fig. 8 shows the visualized results of AD using RPCA-
Net. The anomaly score at each time point is plotted with
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:26:48 UTC from IEEE Xplore.  Restrictions apply.

## Page 10

3553013
IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 74, 2025
Fig. 8. Visualized results of AD.
Fig. 9. Attention map visualization.
the corresponding threshold. It is clear that the portion above
the threshold closely matches the red shaded area, which
represents the true anomalies, demonstrating that RPCA-Net
is capable of distinguishing between normal and anomalous
points eﬀectively.
The attention visualizations in Fig. 9 reveal clear contrastive
behavior between normal and abnormal patterns. During the
normal operation, the temporal attention is sharply focused
on early time steps, and feature channels derived from LSTM
hidden states receive uniform weights. In contrast, anomalous
segments trigger more dispersed temporal attention and a
reshuﬄing of channel priorities with globally reduced weight
magnitudes. This shift provides the model with a strong basis
TABLE V
ABLATION STUDY RESULTS (I)
TABLE VI
ABLATION STUDY RESULTS (II)
Fig. 10. Feature similarity.
Fig. 11. F1-score stability across diﬀerent training conﬁgurations.
for distinguishing between nominal and abnormal behavior in
both temporal and spatial domains.
E. Ablation Experiment
As shown in Table V, the impact of each component in the
model on the AD task is further explored. It can be observed
that the combination of both reconstruction and prediction
mechanisms yields the highest F1-score. In addition, incor-
porating CS into the joint loss function also resulted in an
improvement in the model’s AD performance. Furthermore,
Table VI analyzes the eﬀects of diﬀerent normalization meth-
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:26:48 UTC from IEEE Xplore.  Restrictions apply.

## Page 11

ZHOU et al.: AD FOR UAV FLIGHT DATA VIA RECONSTRUCTION–PREDICTION CO-LEARNING ATTENTION NETWORK
3553013
Fig. 12. Parameter sensitivity studies of main hyperparameters in RPCA-Net. (a) Alpha. (b) Window size. (c) Kernel size. (d) Hidden size. (e) T-percentile.
TABLE VII
DETECTION PERFORMANCE UNDER SIMULATED
SENSOR NOISE (MEAN ± STD)
ods, the use of CNN or LSTM alone for feature extraction,
and a comparison between dual-channel attention and shared
multihead attention. The results indicate that combining CNN
and LSTM contributes positively to detection accuracy, and
the dual-channel attention design outperforms the shared mul-
tihead attention mechanism.
To further quantify the eﬀectiveness of our CS loss in
alleviating task conﬂicts, we analyze the feature similarity
between the prediction and reconstruction outputs under three
loss designs: weighted loss, adversarial loss, and CS loss.
As shown in Fig. 10, CS achieves signiﬁcantly higher and
more stable similarity throughout training. Ablation results in
Table V further conﬁrm that CS leads to the best F1-scores,
validating that resolving task interference translates directly to
improve the detection accuracy.
F. Robustness Analysis Under Diverse Conditions
To assess the robustness of the proposed framework in real-
world UAV environments, we design three sets of experiments
covering sensor noise, cross-fault generalization, and limited
anomaly data. These experiments aim to evaluate the sta-
bility and adaptability of the model under various practical
constraints.
First, the Gaussian noise is injected into test data across
three sensor categories to simulate common sources of in-ﬂight
degradation, while the training data remain clean. Angu-
lar velocity signals (imu data angular velocity [x,y,z]) are
perturbed to mimic mechanical vibration, linear velocity read-
ings (local position velocity linear [x,y,z]) reﬂect aero-
dynamic turbulence, and control signals (rc out channels)
represent electromagnetic interference. Three noise levels are
deﬁned using signal-to-noise ratio (SNR) values: light (IMU:
35 dB, velocity: 30 dB, and RC: 40 dB), moderate (25, 20,
30 dB), and heavy (15, 10, 20 dB), reﬂecting increasing
severity. As shown in Table VII, across six randomized trials
per setting, the framework maintains stable performance under
light and moderate disturbances (F1 variation within ±0.85
TABLE VIII
BOOTSTRAP VERSUS ORIGINAL SCORES FOR ELEVATOR
AND RUDDER FAULT DETECTION
and max drop 0.33%). Under heavy noise, while mean F1
remains acceptable (89.06), performance variance increases
(±1.99), indicating higher output uncertainty. This design
mimics Monte Carlo-style uncertainty propagation and con-
ﬁrms the model’s robustness to sensor degradation.
Second, cross-fault generalization experiments are con-
ducted to test whether the model trained on one type of
fault can generalize to others. As shown in Fig. 11, for each
fault type under test, the resulting F1-scores remain stable
regardless of the training fault type. The maximum variation
in F1 is within 4% points, suggesting strong generalization
capability even when the training and test scenarios are not
perfectly aligned.
Finally, to address the concern regarding limited sample
sizes in the elevator and rudder fault scenarios, boot-
strap resampling is applied to the windowed test samples
(1000
iterations
with
replacement).
As
summarized
in
Table VIII, the bootstrapped precision, recall, and F1-scores
closely match the original metrics, conﬁrming the statistical
reliability of the proposed method under limited anomaly
samples.
G. Parameter Sensitivity
Further studies on key hyperparameters in the RPCA-Net
framework and their inﬂuence on model performance are illus-
trated in Fig. 12. The loss weight parameter α, which controls
the balance between prediction and reconstruction objectives,
demonstrates that stable performance is achieved when α is
set between 0.1 and 0.4. However, when α approaches either
extreme, the F1-score drops by up to 20%, indicating the
importance of maintaining a proper tradeoﬀbetween the two
losses. In addition, the sensitivity of several architectural and
postprocessing parameters has been evaluated. The sliding
window size, which determines the temporal context length,
yields the highest performance at 20 frames, while both shorter
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:26:48 UTC from IEEE Xplore.  Restrictions apply.

## Page 12

3553013
IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 74, 2025
and longer windows lead to over 6% degradation. The convo-
lutional kernel size aﬀects local feature extraction, with kernel
sizes around 3 found to be most eﬀective; excessively small
kernels tend to underﬁt, while large kernels may oversmooth
key patterns. The number of hidden units in the LSTM
also impacts performance, with 256 units oﬀering the best
results. Deviations in either direction result in more than 2.5%
performance loss. Finally, the anomaly threshold percentage T,
used in score ﬁltering, shows robust behavior within the range
of 95%–97%, but exhibits a sharp drop of over 10% when set
too conservatively.
V. CONCLUSION
The increasing deployment of UAVs in critical applications
underscores the critical need for reliable AD methods to ensure
ﬂight safety. A novel RPCA-Net model is proposed for UAV
ﬂight data AD, integrating joint prediction and reconstruction.
The model leverages CNN for local feature extraction and
LSTM for capturing global temporal dependencies. A tem-
poral attention mechanism is incorporated into the prediction
module to focus on key features at critical time steps, while
a channel attention mechanism in the reconstruction module
prioritizes important variable features. Experimental results
across various fault scenarios—including engine, aileron, ele-
vator, and rudder faults—demonstrate that RPCA-Net achieves
strong performance, particularly in engine failure detection,
where it yields high F1 and AUC scores. While RPCA-Net
generally performs favorably, its performance in the elevator
fault case is comparable to that of LSTM-VAE, indicating
room for further optimization.
Despite the promising results, several limitations should
be noted. The model’s scalability to diﬀerent UAV platforms
(e.g., rotary-wing systems) remains to be explored. Its perfor-
mance may also depend on the similarity between training and
test ﬂight proﬁles. Additionally, sensitivity to preprocessing
parameters could aﬀect detection outcomes. Moreover, current
loss functions are based on deterministic similarity measures;
future work could explore uncertainty-aware modeling to
further improve robustness and interpretability. Although the
threshold T was tested for sensitivity, future work could beneﬁt
from Bayesian calibration or distribution-based thresholding
methods to improve adaptivity across diverse conditions.
In conclusion, RPCA-Net demonstrates both eﬃciency and
robustness in UAV AD tasks and shows potential for practical
deployment. Future work may focus on improving generaliza-
tion across platforms, incorporating multimodal sensor fusion,
and reducing reliance on speciﬁc preprocessing conﬁgurations
to enhance real-world applicability.
REFERENCES
[1]
K. Mao et al., “A survey on channel sounding technologies and
measurements for UAV-assisted communications,” IEEE Trans. Instrum.
Meas., vol. 73, pp. 1–24, 2024.
[2]
C. Luo, J. Wang, and Q. Miao, “Transient current ratio dendrite net for
high-resistance connection diagnosis in BLDCM,” IEEE Trans. Power
Electron., vol. 39, no. 4, pp. 4746–4757, Apr. 2024.
[3]
L. Yang, S. Li, C. Li, A. Zhang, and X. Zhang, “A survey of
unmanned aerial vehicle ﬂight data anomaly detection: Technologies,
applications, and future directions,” Sci. China Technol. Sci., vol. 66,
no. 4, pp. 901–919, Apr. 2023.
[4]
J. Zhong, Y. Zhang, J. Wang, C. Luo, and Q. Miao, “Unmanned
aerial vehicle ﬂight data anomaly detection and recovery prediction
based on spatio-temporal correlation,” IEEE Trans. Rel., vol. 71, no. 1,
pp. 457–468, Mar. 2022.
[5]
A. Bl´azquez-Garc´ıa, A. Conde, U. Mori, and J. A. Lozano, “A review on
outlier/anomaly detection in time series data,” ACM Comput. Surveys,
vol. 54, no. 3, pp. 1–33, Apr. 2022.
[6]
H. Deng, Y. Lu, T. Yang, Z. Liu, and J. Chen, “Unmanned aerial vehicles
anomaly detection model based on sensor information fusion and hybrid
multimodal neural network,” Eng. Appl. Artif. Intell., vol. 132, Jun.
2024, Art. no. 107961.
[7]
A. Q. Khan, S. El Jaouhari, N. Tamani, and L. Mroueh, “Knowledge-
based anomaly detection: Survey, challenges, and future directions,”
Eng. Appl. Artif. Intell., vol. 136, Oct. 2024, Art. no. 108996.
[8]
P. Freeman, R. Pandita, N. Srivastava, and G. J. Balas, “Model-based and
data-driven fault detection performance for a small UAV,” IEEE/ASME
Trans. Mechatronics, vol. 18, no. 4, pp. 1300–1309, Aug. 2013.
[9]
A. Zolghadri et al., “Signal and model-based fault detection for aircraft
systems,” IFAC-PapersOnLine, vol. 48, no. 21, pp. 1096–1101, 2015.
[10] E. Baskaya, M. Bronz, and D. Delahaye, “Fault detection & diagnosis
for small UAVs via machine learning,” in Proc. IEEE/AIAA 36th Digit.
Avionics Syst. Conf. (DASC), Sep. 2017, pp. 1–6.
[11] L. A. Al-Haddad, A. A. Jaber, S. A. Al-Haddad, and Y. M. Al-Muslim,
“Fault diagnosis of actuator damage in UAVs using embedded recorded
data and stacked machine learning models,” J. Supercomput., vol. 80,
no. 3, pp. 3005–3024, Feb. 2024.
[12] A. Altinors, F. Yol, and O. Yaman, “A sound based method for fault
detection with statistical feature extraction in UAV motors,” Appl.
Acoust., vol. 183, Dec. 2021, Art. no. 108325.
[13] Y. Liu, Y. Zhou, K. Yang, and X. Wang, “Unsupervised deep learn-
ing for IoT time series,” IEEE Internet Things J., vol. 10, no. 16,
pp. 14285–14306, Aug. 2023.
[14] P. Yan et al., “A comprehensive survey of deep transfer learning for
anomaly detection in industrial time series: Methods, applications, and
directions,” IEEE Access, vol. 12, pp. 3768–3789, 2024.
[15] X. Chu, X. Zhou, Q. Bu, and Q. Miao, “Sensor fault detection for
UAVs using improved self-attention LSTM network with similarity
space mapping,” IEEE Trans. Instrum. Meas., vol. 73, pp. 1–12, 2024.
[16] S. Liu et al., “Time series anomaly detection with adversarial recon-
struction networks,” IEEE Trans. Knowl. Data Eng., vol. 35, no. 4,
pp. 4293–4306, Apr. 2023.
[17] B. Wang, D. Liu, Y. Peng, and X. Peng, “Multivariate regression-based
fault detection and recovery of UAV ﬂight data,” IEEE Trans. Instrum.
Meas., vol. 69, no. 6, pp. 3527–3537, Jun. 2020.
[18] C. Luo, J. Wang, E. Zio, and Q. Miao, “Subdomain adaptation order
network for fault diagnosis of brushless DC motors,” IEEE Trans.
Instrum. Meas., vol. 73, pp. 1–10, 2024.
[19] H. Lu, Z. Wang, and Y. Shi, “Unmanned aerial vehicle ﬂight data
anomaly detection based on multirate-aware LSTM,” IEEE Trans.
Instrum. Meas., vol. 73, pp. 1–13, 2024.
[20] J. Zhong, H. Zhang, and Q. Miao, “A novel altitude measurement chan-
nel reconstruction method based on symbolic regression and information
fusion,” IEEE Trans. Instrum. Meas., vol. 74, pp. 1–12, 2025.
[21] Q. Ma et al., “A survey on time-series pre-trained models,” IEEE Trans.
Knowl. Data Eng., vol. 36, no. 12, pp. 7536–7555, Dec. 2024.
[22] Z. Zamanzadeh Darban, G. I. Webb, S. Pan, C. Aggarwal, and M. Salehi,
“Deep learning for time series anomaly detection: A survey,” ACM
Comput. Surveys, vol. 57, no. 1, pp. 1–42, Jan. 2025.
[23] Y. Yang, C. Zhang, T. Zhou, Q. Wen, and L. Sun, “DCdetector: Dual
attention contrastive representation learning for time series anomaly
detection,” in Proc. 29th ACM SIGKDD Int. Conf. Knowl. Discovery
Data Mining (KDD), 2023, pp. 3033–3045.
[24] S. Hochreiter and J. Schmidhuber, “Long short-term memory,” Neural
Comput., vol. 9, no. 8, pp. 1735–1780, Nov. 1997.
[25] Z. Zheng, Q. He, G. Jiang, F. Yin, X. Wu, and P. Xie, “Spatio-
temporal attention-based neural network for wind turbine blade cracking
fault detection,” in Proc. Chin. Autom. Congr. (CAC), Nov. 2020,
pp. 7439–7444.
[26] S. Liao, H. Liu, J. Yang, and Y. Ge, “A channel-spatial–temporal
attention-based network for vibration-based damage detection,” Inf. Sci.,
vol. 606, pp. 213–229, Aug. 2022.
[27] P. J. Huber, “Robust estimation of a location parameter,” in Break-
throughs in Statistics: Methodology and Distribution. New York, NY,
USA: Springer, 1992, pp. 492–518.
[28] B. Zhou, S. Liu, B. Hooi, X. Cheng, and J. Ye, “BeatGAN: Anomalous
rhythm detection using adversarially generated time series,” in Proc.
28th Int. Joint Conf. Artif. Intell., Aug. 2019, pp. 4433–4439.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:26:48 UTC from IEEE Xplore.  Restrictions apply.

## Page 13

ZHOU et al.: AD FOR UAV FLIGHT DATA VIA RECONSTRUCTION–PREDICTION CO-LEARNING ATTENTION NETWORK
3553013
[29] X. Chen, L. Deng, Y. Zhao, and K. Zheng, “Adversarial autoencoder for
unsupervised time series anomaly detection and interpretation,” in Proc.
16th ACM Int. Conf. Web Search Data Mining, Feb. 2023, pp. 267–275.
[30] A. Keipour, M. Mousaei, and S. Scherer, “ALFA: A dataset for UAV
fault and anomaly detection,” Int. J. Robot. Res., vol. 40, nos. 2–3,
pp. 515–520, Feb. 2021.
[31] K. Hundman, V. Constantinou, C. Laporte, I. Colwell, and T. Soder-
strom, “Detecting spacecraft anomalies using LSTMs and nonparametric
dynamic thresholding,” in Proc. 24th ACM SIGKDD Int. Conf. Knowl.
Discovery Data Mining, Jul. 2018, pp. 387–395.
[32] S.-A. Chen, C.-L. Li, S. O. Arik, N. C. Yoder, and T. Pﬁster, “TSMixer:
An all-MLP architecture for time series forecast-ing,” Trans. Mach.
Learn. Res., vol. 2023, pp. 1–24, Mar. 2023.
[33] Y. Liu et al., “ITransformer: Inverted transformers are eﬀective for time
series forecasting,” in Proc. 12th Int. Conf. Learn. Represent., 2023,
pp. 1–25.
[34] H. Wu, T. Hu, Y. Liu, H. Zhou, J. Wang, and M. Long, “TimesNet:
Temporal 2D-variation modeling for general time series analysis,” in
Proc. 11th Int. Conf. Learn. Represent., 2023, pp. 1–23.
[35] D. Park, Y. Hoshi, and C. C. Kemp, “A multimodal anomaly detector for
robot-assisted feeding using an LSTM-based variational autoencoder,”
IEEE Robot. Autom. Lett., vol. 3, no. 3, pp. 1544–1551, Jul. 2018.
[36] B. Zong et al., “Deep autoencoding Gaussian mixture model for unsu-
pervised anomaly detection,” in Proc. Int. Conf. Learn. representations,
2018, pp. 2323–2332.
[37] H. Zhao et al., “Multivariate time-series anomaly detection via graph
attention network,” in Proc. IEEE Int. Conf. Data Mining (ICDM), Nov.
2020, pp. 841–850.
[38] J. Audibert, P. Michiardi, F. Guyard, S. Marti, and M. A. Zuluaga,
“USAD: Unsupervised anomaly detection on multivariate time series,”
in Proc. 26th ACM SIGKDD Int. Conf. Knowl. Disc. Data Min., 2020,
pp. 3395–3404.
[39] C. Zhang et al., “A deep neural network for unsupervised anomaly
detection and diagnosis in multivariate time series data,” in Proc. AAAI
Conf. Artif. Intell., vol. 33, 2019, pp. 1409–1416.
Zeyi Zhou received the B.E. degree in automation
from the School of Electrical Engineering, Sichuan
University, Chengdu, China, in 2023, where he is
currently pursuing the master’s degree.
His research interests include prognostics and
health management and anomaly detection.
Jie Zhong received the B.E. degree in mechan-
ical engineering from the College of Mechanical
Engineering, Chengdu University of Technology,
Chengdu, Sichuan, China, in 2020, and the M.S.
degree in aeronautical and astronautical science and
technology from Sichuan University, Chengdu, in
2023, where he is currently pursuing the Ph.D.
degree with the College of Electrical Engineering.
His research interests include anomaly detection
and deep learning.
Yujie Zhang (Member, IEEE) received the B.E.
degree from Harbin Institute of Technology, Weihai,
China, in 2014, and the Ph.D. degree from Harbin
Institute of Technology (HIT), Harbin, China, in
2021.
He is currently an Associate Professor with the
College of Electrical Engineering, Sichuan Univer-
sity, Chengdu, China. His current research interests
include prognostics and health management, condi-
tion monitoring, data-driven degradation modelling,
and electronic–mechanical system simulation.
Dr. Zhang is currently an Associate Editor of IEEE TRANSACTIONS ON
INSTRUMENTATION AND MEASUREMENT.
Qiang Miao (Senior Member, IEEE) received the
B.E. and M.S. degrees from Beihang University,
Beijing, China, in 1998 and 2001, respectively, and
the Ph.D. degree from the University of Toronto,
Toronto, ON, Canada, in 2005.
He
is
currently
a
Professor
with
the
Col-
lege of Electrical Engineering, Sichuan University,
Chengdu, China. He serves as the Director of
Sichuan Province International Science and Tech-
nology Cooperation Base for Aerospace Information
and Intelligent Equipment. His research focuses on
reliability, fault diagnosis, and health assessment.
Dr. Miao has been a Senior Member of the IEEE Reliability Society since
2012 and served as an IEEE RS AdCom Member from 2019 to 2021, as
well as the IEEE RS Vice President from 2020 to 2021. He is currently an
Associate Editor-in-Chief of IEEE TRANSACTIONS ON INSTRUMENTATION
AND MEASUREMENT and an Associate Editor of IEEE TRANSACTIONS
ON RELIABILITY. In addition, he serves as an Editorial Board Member for
Chinese Journal of Aeronautics.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:26:48 UTC from IEEE Xplore.  Restrictions apply.
