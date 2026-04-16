# Unmanned Aerial Vehicle Flight Data Anomaly Detection Based on Multirate-Aware LSTM.pdf

## Page 1

IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 73, 2024
3526713
Unmanned Aerial Vehicle Flight Data Anomaly
Detection Based on Multirate-Aware LSTM
Hui Lu , Senior Member, IEEE, Zan Wang , and Yuhui Shi , Fellow, IEEE
Abstract— With the widespread use of unmanned aerial vehicle
(UAV), health status monitoring is critical for flight safety, making
anomaly detection a focus of attention. In general, UAV flight
data are multirate multivariate time series (MR-MTS) acquired
by multiple sensors at different sampling rates, while the existing
methods are mainly designed for multivariate time series (MTS).
Moreover, traditional methods that tune MR-MTS to MTS
may artificially change naturally occurring temporal dependen-
cies. To address these challenges, a novel multirate-aware long
short-term memory (LSTM), called MRA-LSTM, is proposed
for UAV flight data anomaly detection. First, without manual
tuning, a multirate-aware structure is proposed to directly model
MR-MTS UAV flight data. Second, to avoid the higher rate
variates “masking” the multiple temporal dependencies present
in the lower rate variates, a multiscale update mechanism is
proposed to trade off information entropy from different rates.
Finally, a hierarchical state excitation (HSE) is proposed to
adaptively control the importance of each inferred compressed
representation to the output module. The experimental results
demonstrate the effectiveness of the proposed method, as well as
its superiority to other state-of-the-art peer competitors.
Index
Terms— Anomaly
detection,
deep
learning,
long
short-term memory (LSTM), multirate multivariate time series
(MR-MTS), unmanned aerial vehicle (UAV).
I. INTRODUCTION
U
NMANNED aerial vehicles (UAVs) are complex systems
consisting of electronic equipment, mechanical devices,
hardware hydraulics, platform, and control modules [1]. The
rapid growth in the use of UAVs has increased concerns about
their safety and reliability [2]. According to Industry 4.0 and
Smart Industry, with the development of instrumentations,
measurements, and sensor data collection, monitoring various
equipment has become a common and simple task [3], such as
gearboxes [4], rotating machine [5], turbofan engine [6], and
electrical systems [7]. The automation of condition monitoring
and timely warning has become an essential requirement. As a
key technology, multivariate time series (MTS) analysis has
Manuscript received 7 May 2024; revised 7 July 2024; accepted 15 July
2024. Date of publication 8 August 2024; date of current version 21 August
2024. This work was supported in part by the National Natural Science
Foundation of China under Grant 62371030 and Grant 61827901 and in part
by Beijing Municipal Natural Science Foundation under Grant 4222008. The
Associate Editor coordinating the review process was Dr. Anant Kumar Verma.
(Corresponding author: Hui Lu.)
Hui Lu and Zan Wang are with the School of Electronic and Infor-
mation Engineering, Beihang University, Beijing 100191, China (e-mail:
mluhui@buaa.edu.cn; by2002141@buaa.edu.cn).
Yuhui Shi is with Guangdong Provincial Key Laboratory of Brain-Inspired
Intelligent Computation, School of Computer Science and Engineering, South-
ern University of Science and Technology, Shenzhen 518055, China (e-mail:
shiyh@sustech.edu.cn).
Digital Object Identifier 10.1109/TIM.2024.3440379
attracted attention [8] and has been widely applied in UAV
flight data anomaly detection (UAV-FDAD) tasks [9].
Unlike univariate time series, MTS observations generally
come from multiple sensors at various sampling rates, namely,
multirate MTS (MR-MTS). Take Holybro PX4 2.4.6 autopilot
and Nvidia Jetson TX2 onboard computer as an example,
a lot of important variates are recorded between 2 Hz (climb,
throttle, and so on) and 25 Hz (roll, pitch, and so on).
In extreme cases, the ratio of data volumes between certain
variates can reach 1:50 per unit time, posing a great challenge
for time series analysis.
In recent years, due to adaptive learning and powerful ability
in nonlinear approximation, deep learning has yielded fruitful
achievements in UAV-FDAD [10]. A majority of methods are
based on reconstructing or predicting normal behavior [11]
and thus can be divided into two categories: 1) reconstruction-
based methods, such as autoencoder, variational inference,
and variants [12], [13], [14], [15], [16]; 2) prediction-based
methods, such as long short-term memory (LSTM) network
and other variants [9], [17], [18]. The basic idea behind them
is that a model cannot fit unforeseen patterns of abnormal data.
When a model is trained on normal data, its reconstruction
or prediction error on abnormal data will be high, indicating
anomaly.
Briefly, reconstruction-based methods can be generalized
into a modular framework, consisting of two parts: an encoder
(network) learns a compressed representation of the input
data and a decoder (network) maps this representation to
reconstruct the target data. The target is the input itself (input:
x1, . . . , xT and target: ˆx1, . . . , ˆx T ). Similarly, prediction-based
methods can also be divided into two parts: an inference mod-
ule (network) learns a compressed representation of the input
data and an output module (network) maps this representation
to predict the future data. The future is the next step of the
input (input: x1, . . . , xT and future: xT +1, . . . , xT +n). Thus,
suitable networks for learning compressed representation have
motivated a great deal of interest, such as graph neural net-
work (GNN) [19], convolutional neural network (CNN) [20],
LSTM, gated recurrent unit (GRU) [2], temporal convolutional
network (TCN) [21], and other variants.
Despite the great success of the above methods, they were
primarily designed for MTS, while MR-MTS UAV-FDAD has
received little attention. In general, to handle MR-MTS, they
first converted MR-MTS into MTS by data filling [22] and
then conducted follow-up studies. However, it is inevitable that
some naturally occurring temporal dependencies will be artifi-
cially introduced or removed. Even though this intuition eludes
1557-9662 © 2024 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:29:09 UTC from IEEE Xplore.  Restrictions apply.

## Page 2

3526713
IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 73, 2024
theoretical explanation, Che et al. [23] empirically proved
that upsampling will introduce long-term dependencies. In this
article, we embrace these observations and strive to propose a
suitable network that can directly process MR-MTS to obtain
a good representation. Even better, this network can also serve
as an upstream network for other methods to directly process
MR-MTS. Naturally suited for time series modeling, LSTM
has been successful in serving as the aforementioned networks.
More importantly, it has also been widely integrated into other
methods as an upstream network.
Specifically, in the field of reconstruction-based methods,
Zhou et al. [12] used the attention mechanism as encoder and
LSTM as decoder, while Longari et al. [13] and Maleki et al.
[14] used LSTM as both encoder and decoder. These methods
captured the latent representation, while based on variational
inference, a preferable idea is to learn probability distribution.
Guha et al. [15] adopted wavelet coefficients and variational
autoencoder (VAE) to model the potential distribution, wherein
LSTM serves as both encoder and decoder. Park et al. [16]
incorporated LSTM into VAE to reconstruct log likelihood.
In the field of prediction-based methods, Zhong et al. [17]
proposed a spatiotemporal-based LSTM. Wang et al. [1]
proposed a PCA-based LSTM and a filtering-based LSTM [9].
Combined with TCN and transformer, Lai et al. [18] pro-
posed LightCTS. Combined with transfer learning and GNN,
Panagopoulos et al. [19] proposed MPNN-LSTM. Combined
with GRU and GNN, Zhao et al. [22] and Bai et al. [24]
proposed T-GCN and AGCRN, respectively. They benefit more
or less from LSTM. It is because LSTM possesses a significant
superiority in handling historical information [25], namely, the
long-term temporal dependencies maintaining capacity.
Motivated by these methods, we build a UAV-FDAD model
based on LSTM to capture multiple temporal dependencies
(i.e., multiple feature patterns) present in MR-MTS by jointly
modeling time series (a time series is a feature corresponding
to a particular variate) with different sampling rates. To this
end, several crucial issues need to be addressed.
1) Regarding multirate modeling, most of the recent con-
temporary methods are structurally infeasible, as they
employ the fixed dimension, while the dimension of
MR-MTS varies over time.
2) Regarding representation learning, most existing infer-
ence processes are executed at every time step, espe-
cially the self-loop-based contemporary methods. In this
premise, when modeling MR-MTS, the higher rate time
series will have more opportunities to participate in
inference. The higher rate time series may “mask” the
temporal dependencies present in the lower rate time
series, causing lower rate information loss.
3) Multirate is naturally accompanied by multiple temporal
dependencies. In this article, we embrace these observa-
tions and propose a novel multirate-aware LSTM, called
MRA-LSTM, to address these issues.
The main contributions are given as follows.
1) Without
manual
tuning,
a
multirate-aware
struc-
ture
is
proposed
to
directly
capture
the
tempo-
ral dependencies present in the original MR-MTS.
In turn, MRA-LSTM can directly conduct UAV-FDAD,
avoiding artificially changing some naturally occurring
dependencies.
2) To alleviate the “masking” problem, we propose a novel
multiscale update mechanism. Unlike updating at every
time step, interaction among cross-rate time series is
only permitted when the abstraction-level representation
is completely extracted.
3) The output module receives the representations inferred
from a multirate-aware structure for future prediction.
To adaptively control the importance of each represen-
tation, a hierarchical state excitation (HSE) is proposed
to focus on channel–element-wise representation rela-
tionships. If necessary, it is also an interface to other
downstream neural networks to match the required ten-
sor format.
The above purposes have been validated on real-world UAV-
FDAD tasks. For comprehensive demonstrations, experiments
(comparison result, statistical analysis, sensitivity analysis, and
ablation study) are conducted based on three feature selection
methods and two thresholding methods.
The
remainder
of
this
article
is
organized
as
fol-
lows. In Section II, the fundamental theory is presented.
In Section III, the details of the proposed method are detailed.
In Section IV, the experimental results and the analysis are
discussed. Finally, Section V concludes this article.
II. FUNDAMENTAL THEORY
In this section, we first present MR-MTS in Section II-A
and then briefly introduce multilayer LSTM in Section II-B.
A. Multirate MTS
Given a traditional MTS, xt ∈Rd is adopted to represent
multivariate observations at time step t, t = 1, . . . , T . d is a
fixed dimension. In contrast, given an MR-MTS of N different
sampling rates, xn
t
∈Rdn,t, n = 1, . . . , N, is adopted to
represent the observations of the nth rate at time step t. dn,t
is the variable-length dimension of the nth rate variates at
step t. Namely, the dimension d of MTS is a constant, while
the dimension dn,t of MR-MTS changes over time. Here, N
sampling rates are in descending order. For instance, n = 1 and
n = N correspond to the highest and lowest sampling rate,
respectively.
B. Multilayer LSTM
LSTM is capable of maintaining long-term dependencies by
introducing memory cell to remember past information while
accumulating it. Fig. 1(c) shows the structure of a memory cell.
It is common to stack multilayer cells to improve the perfor-
mance, as shown in Fig. 1(b). Given an MTS of length T , the
process of N-layer LSTM extracting the compressed represen-
tation (hN
t , t = 1, . . . , T ) is shown in Fig. 1(a). In detail, each
memory cell adopts three multiplicative gates (forget gate f ,
input gate i, and output gate o) and a cell proposal g to update
state (cell state c and hidden state h) at every time step [17].
For the kth layer cell at step t, t = 1, . . . , T , its cell state ck
t
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:29:09 UTC from IEEE Xplore.  Restrictions apply.

## Page 3

LU et al.: UAV FLIGHT DATA ANOMALY DETECTION BASED ON MULTIRATE-AWARE LSTM
3526713
TABLE I
NOTATIONS OF LSTM MEMORY CELL IN THE kTH LAYER AT TIME STEP t
Fig. 1.
(a) Multilayer LSTM (xt ∈Rd, where d is a constant). (b) N-layer
memory cells at time step t. (c) Memory cell in the kth layer at time step t.
and hidden state hk
t update formulas can be described by the
following equations:
f k
t = σ
W k
f yk
t + U k
f hk
t−1 + bk
f

(1)
gk
t = tanh
W k
g yk
t + U k
g hk
t−1 + bk
g

(2)
ik
t = σ
W k
i yk
t + U k
i hk
t−1 + bk
i

(3)
ok
t = σ
W k
o yk
t + U k
o hk
t−1 + bk
o

(4)
ck
t = f k
t ⊙ck
t−1 + ik
t ⊙gk
t
(5)
hk
t = ok
t ⊙tanh
ck
t

(6)
where yk
t is the cell input. If k == 1 (namely, the first layer),
yk
t
= xt; otherwise, yk
t
= hk−1
t
, 1 < k ≤N. A symbol
⊙denotes Hadamard multiplication and other corresponding
notations are shown in Table I.
III. MRA-LSTM-BASED UAV-FDAD
This section first presents the overview of UAV-FDAD in
Section III-A and then details the main components of the
proposed MRA-LSTM model in Section III-A1.
A. UAV-FDAD Overview
As shown in Fig. 2, the framework of UAV-FDAD consists
of two parts: offline modeling and online detection. The details
are presented as follows.
1) Offline Modeling:
MRA-LSTM is an unsupervised
method and thus needs to be trained on normal data to capture
the normal patterns. It consists of the following three phases.
1) Phase 1—Data Acquisition: Flight-critical sensors are
installed on UAV to monitor multivariate under different
flights. As mentioned earlier, the collected flight data are
MR-MTS. Moreover, normal flight data refer to the data
collected during no-fault (normal) flights.
2) Phase 2—Samples Generation: MR-MTS is normalized
to [0, 1] and split into segments of length ls + lp
using sliding window. Unlike MTS, ls determines the
maximum number of points input to the model (X) for
predicting the next lp steps (Y). Suppose that there are
three variables with two sampling rates in a segment.
If the number of points for these three variables is 5,
5, and 8, then ls is 8. To what extent, is the proposed
multirate-based model useful to UAV-FDAD? Based on
different degrees of multirate, its performance will be
demonstrated later in Section IV-C.
3) Phase 3—MRA-LSTM Training: MRA-LSTM can be
seen as a mapping function ˆY = F(X, Y, θ, δ). Here,
X and Y are the samples generated in phase 2. θ and δ
are the weight set (optimized by backpropagation) and
hyperparameter set (segment length, batch size, and so
on), respectively. The objective of training is to find
the optimal θ and δ to minimize the error between the
observed and predicted values. The details will be given
later in Section III-B.
2) Online Detection: After that, the well-trained model and
adjusted hyperparameters are used for UAV-FDAD. It consists
of the following four phases.
1) Phases 1 and 2—Data Acquisition and Samples Genera-
tion: In contrast to phases 1 and 2 in model training, the
differences are that the flight health status is unknown.
2) Phase 3—MRA-LSTM Predicting: The well-trained
model is used to feed the first ls steps to predict the next
lp steps. In general, MTS prediction can be classified
into predicting values for single variable or multiple
variables. Since UAV anomaly is not reflected in only
one variable, multiple variables prediction is adopted.
3) Phase 4—Labeling: Based on the thresholding function,
the error between Y and
ˆY is evaluated to classify
each time step as anomalous or healthy. To enable an
exhaustive comparison, two kinds of functions (static
and dynamic) are adopted. The details will be given in
Section IV-B.
B. Proposed MRA-LSTM Model
The capability of MRA-LSTM model comes from the
proposed strategies: 1) multirate-aware structure; 2) multiscale
update mechanism; and 3) HSE.
1) Multirate-Aware Structure (S1): Unlike MTS xt ∈Rd
(d is a constant), for MR-MTS xk
t ∈Rdk,t, t = 1, . . . ,ls and
k = 1, . . . , N, dk,t changes over time. In Fig. 3, we adopt
N layer memory cells to construct a multirate-aware structure
such that each rate corresponds to one layer that should be
noted that this structure is not a traditional multilayer LSTM or
a concatenation of multiple single-channel prediction models
since each channel is not modeled independently. Specifically,
to infer the kth layer memory cell at step t, this structure
has four different information sources: 1) the previous same
layer states ck
t−1 and hk
t−1; 2) the previous higher layer states
ck+1
t−1 and hk+1
t−1; and 3) the current lower layer states ck−1
t
and hk−1
t
; and 4) the current input xk
t
(if it is available).
However, these states are not necessarily involved in the
update of the current states ck
t and hk
t . Otherwise, the states
corresponding to the higher rate layers may mask the multiple
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:29:09 UTC from IEEE Xplore.  Restrictions apply.

## Page 4

3526713
IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 73, 2024
Fig. 2.
Flowchart of the proposed MRA-LSTM-based UAV-FDAD, consisting of (a): offline modeling and (b): online detection.
Fig. 3.
Proposed multirate-aware structure for MR-MTS. Each xk
t is MTS,
while (x1
t , . . . , x N
t ) is MR-MTS. Meanwhile, this structure combines the
proposed multiscale update mechanism to alleviate the “masking” problem
caused by multiple rates itself.
temporal dependencies present in the states corresponding
to the lower rate layers. Thus, the proposed multirate-aware
structure combines a multiscale update mechanism (different
colored circles correspond to the completion degree of the
abstraction-level representation in different sources) to address
this issue. In general, the highest level states hN
t , t = 1, . . . ,ls
are served as inputs to the output module to predict future
values. However, our inferred states hk
t , t = 1, . . . ,ls and
k = 1, . . . , N, are not structurally symmetric. To adaptively
control the importance of each inferred state, an HSE is
proposed and connected behind a multirate-aware structure to
address this issue.
2) Multiscale Update Mechanism (S2): Despite the variety
of information sources, not all of them are involved in the
update of the current memory cell. It is only permitted
when the abstraction-level feature is completely extracted.
In Fig. 3, take blue circles in the kth layer as an example, the
(k −1)th layer, corresponding to the higher rate time series,
can participate in updating them (solid arrow). In contrast,
for pink circles in the kth layer, the (k −1)th layer cannot
participate in updating them (dashed arrow). It means that the
abstraction-level feature at the lower layer is not complete.
In other words, at some steps, even the lower rate time
series is missing values, and the state may not be masked
by the higher rate time series. In addition, unlike traditional
LSTM, it is not necessary to calculate three gates (forget
gate f , input gate i, and output gate o) and cell proposal
g at every time step. In Fig. 4 (right), there are different
operators (corresponding to different colored circles), which
are determined by the learnable boundaries sk
t−1 and sk−1
t
.
However, it raises a new problem about nondifferentiability
(discrete function) that renders the neural network unable to
be trained by gradient descent-based backpropagation.
To tackle this problem, the straight-through estimator fste(·)
[26] is introduced to train the network with discrete function,
as shown in Fig. 4 (left). Based on the straight-through
estimator, the nondifferentiable function in the forward propa-
gation will be replaced by a differentiable function during the
backward propagation. In this article, the learnable boundary
used in forward propagation is determined by the step function
(sk
t = 1 if ˜sk
t > 0.5; 0 otherwise), which will be replaced by
hard sign function max(0, min(1, ((x + 1)/2))) in backward
propagation. Moreover, at some time steps, some layers may
have no current input. For the kth layer at step t, zk
t = 1
indicates the presence of input and zk
t = 0 indicates no input.
It is worth noting that sk
t−1 and sk−1
t
are part of the output of
the network, while zk
t is only for ease of the description of the
subsequent formulas and thus has no practical significance.
Based on the obtained boundaries, at each time step, each
cell will be updated based on the selected operator, as shown
in Fig. 4 (right). We take the kth layer memory cell at step t
as an example. Its cell state ck
t , hidden state hk
t , and boundary
sk
t formulas can be described by the following equation:
ck
t , hk
t , sk
t = Fkck
t−1, hk+1
t−1, hk
t−1, hk−1
t
, xk
t , sk
t−1, sk−1
t

.
(7)
Unlike traditional LSTM, it is not necessary to compute
both gates f k
t , ik
t , and ok
t and cell proposal gk
t at every step.
Whenever needed, f k
t , gk
t , ik
t , ok
t , and sk
t are calculated by the
following equations:
f k
t =



σ

W k
f hk
t−1+U k
f

hk−1
t
, xk
t

+bk
f

,
if
(
sk
t−1 =0
sk−1
t
=zk
t =1
σ

W k
f hk
t−1+V k
f hk−1
t
+bk
f

,
if
(
sk
t−1 =zk
t =0
sk−1
t
=1
No need for calculation, otherwise
(8)
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:29:09 UTC from IEEE Xplore.  Restrictions apply.

## Page 5

LU et al.: UAV FLIGHT DATA ANOMALY DETECTION BASED ON MULTIRATE-AWARE LSTM
3526713
Fig. 4.
Proposed multiscale update mechanism, consisting of straight-through estimator and four types of operators. (a) Operator 1. (b) Operator 2.
(c) Operator 3. (d) Operator 4.
gk
t =



tanh
W k
g hk
t−1+U k
g

hk−1
t
, xk
t

+bk
g

,
if
(
sk
t−1 =0
sk−1
t
=zk
t =1
tanh
W k
g hk
t−1+V k
g hk−1
t
+bk
g

,
if
(
sk
t−1 =zk
t =0
sk−1
t
=1
tanh
Zk
ghk+1
t−1+J k
g xk
t +bk
g

,
if
(
sk
t−1 =zk
t =1
sk−1
t
=0
tanh
Zk
ghk+1
t−1+bk
g

,
if
(
sk
t−1 =1
sk−1
t
=zk
t =0
tanh
Zk
ghk+1
t−1+U k
g

hk−1
t
, xk
t

+bk
g

,
if
(
sk
t−1 =sk−1
t
=1
zk
t =1
tanh
Zk
ghk+1
t−1+V k
g hk−1
t
+bk
g

,
if
(
sk
t−1 =sk−1
t
=1
zk
t =0
No need for calculation,
otherwise.
(9)
The formulas for ik
t , ok
t , and sk
t are similar to gk
t . For ik
t ,
ok
t , and sk
t , it is required to replace: 1) W k
g with W k
i , W k
o , and
W k
s ; 2) U k
g with U k
i , U k
o , and U k
s ; 3) V k
g with V k
i , V k
o , and V k
s ;
4) Zk
g with Zk
i , Zk
o, and Zk
s ; 5) J k
g with J k
i , J k
o , and J k
s ; and
6) bk
g with bk
i , bk
o, and bk
s in (9). Unlike the tangent activation
function (tanh) of gk
t , the activation function of ik
t and ok
t is
replaced by the sigmoid activation function (σ). Moreover, for
sk
t , the tanh activation function is replaced by the step function,
as explained earlier.
Then, the cell state ck
t
is calculated by the following
equation:
ck
t =



σ
f k
t

⊙ck
t−1 + σ
ik
t

⊙tanh
gk
t

,
if
(
sk
t−1 = 0
sk−1
t
= 1
σ
ik
t

⊙tanh
gk
t

,
if sk
t−1 = 1
ck
t−1,
otherwise.
(10)
Finally, the hidden state hk
t is calculated by the following
equation:
hk
t =



ok
t ⊙tanh
ck
t

,
if
(
sk
t−1 = 0
sk−1
t
= 0
hk
t−1,
otherwise.
(11)
Here, we use W k
f , W k
g , W k
i , W k
o , W k
s , U k
f , U k
g, U k
i , U k
o , U k
s ,
V k
f , V k
g , V k
i , V k
o , V k
s , Zk
f , Zk
g, Zk
i , Zk
o, Zk
s , J k
f , J k
g , J k
i , J k
o , and
J k
s to denote different hidden layer connection weight matrices
of the kth layer memory cell. bk
f , bk
g, bk
i , bk
o, and bk
s are biases
of the kth layer memory cell. Four specific cases are given
as follows, which help the readers to better understand the
multiscale update mechanism during the process of capturing
the multiple temporal dependencies presented in MR-MTS.
Operator 1: When sk
t−1 = 0, sk−1
t
= 1, and zk
t = 1, there are
three gates f k
t , ik
t , and ok
t and cell proposal gk
t and sk
t that need
to be calculated [see Fig. 4(a)] by the following equations:
f k
t = σ
W k
f hk
t−1 + U k
f

hk−1
t
, xk
t

+ bk
f

(12)
gk
t = tanh
W k
g hk
t−1 + U k
g

hk−1
t
, xk
t

+ bk
g

(13)
ik
t = σ
W k
i hk
t−1 + U k
i

hk−1
t
, xk
t

+ bk
i

(14)
ok
t = σ
W k
o hk
t−1 + U k
o

hk−1
t
, xk
t

+ bk
o

(15)
sk
t = hard sigm
W k
s hk
t−1 + U k
s

hk−1
t
, xk
t

+ bk
s

(16)
then, the cell state ck
t is calculated by the following equation:
ck
t = f k
t ⊙ck
t−1 + ik
t ⊙gk
t
(17)
and then, the hidden state hk
t is calculated by the following
equation:
hk
t = ok
t ⊙tanh
ck
t

.
(18)
Operator 2: When sk
t−1 = 1, sk−1
t
= 0 and zk
t = 0, there
are two gates ik
t , ok
t , cell proposal gk
t and sk
t that need to be
calculated [see Fig. 4(b)] by the following equations:
gk
t = tanh
Zk
ghk+1
t−1 + bk
g

(19)
ik
t = σ
Zk
i hk+1
t−1 + bk
i

(20)
ok
t = σ
Zk
ohk+1
t−1 + bk
o

(21)
sk
t = hard sigm
Zk
s hk+1
t−1 + bk
s

(22)
then, the cell state ck
t is calculated by the following equation:
ck
t = ik
t ⊙gk
t
(23)
and then, the hidden state hk
t is calculated by the following
equation:
hk
t = ok
t ⊙tanh
ck
t

.
(24)
Operator 3: When sk
t−1 = 1, sk−1
t
= 1 and zk
t = 1, there
are two gates ik
t , ok
t , cell proposal gk
t and sk
t that need to be
calculated [see Fig. 4(c)] by the following equations:
gk
t = tanh
Zk
ghk+1
t−1 + U k
g

hk−1
t
, xk
t

+ bk
g

(25)
ik
t = σ
Zk
i hk+1
t−1 + U k
i

hk−1
t
, xk
t

+ bk
i

(26)
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:29:09 UTC from IEEE Xplore.  Restrictions apply.

## Page 6

3526713
IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 73, 2024
ok
t = σ
Zk
ohk+1
t−1 + U k
o

hk−1
t
, xk
t

+ bk
o

(27)
sk
t = hard sigm
Zk
s hk+1
t−1 + U k
s

hk−1
t
, xk
t

+ bk
s

(28)
then, the cell state ck
t is calculated by the following equation:
ck
t = ik
t ⊙gk
t
(29)
and then, the hidden state hk
t is calculated by the following
equation:
hk
t = ok
t ⊙tanh
ck
t

.
(30)
Operator 4: When sk
t−1 = 0, sk−1
t
= 0 and zk
t = 0, cell is
not updated and only sk
t is calculated [see Fig. 4(d)] by the
following equation:
sk
t = hard sigm
W k
s hk−1
t
+ bk
s

(31)
then, the cell state ck
t is calculated by the following equation:
ck
t = ck
t−1
(32)
and then, the hidden state hk
t is calculated by the following
equation:
hk
t = hk
t−1.
(33)
3) Hierarchical State Excitation (S3):
After that, the
inferred states (compressed representation) are served as inputs
to the output module for prediction. In general, these states
refer to the highest level states hN
t , t = 1, . . . ,ls. However,
it disregards whether the state comes from higher rate time
series or lower rate time series. To adaptively control the
importance of each inferred state hk
t , t
=
1, . . . ,ls and
k = 1, . . . , N, an HSE is proposed to focus on channel–
element-wise relationships. In Fig. 5, HSE takes all inferred
states hk
t , t = 1, . . . ,ls, k = 1, . . . , N as input and produces
a collection of per-channel–element modulation coefficients
(rk
t , t = 1, . . . ,ls and k = 1, . . . , N). These coefficients
are applied to the inferred states to generate the aggregation
(et, t = 1, . . . ,ls), which are served as input to the output
module. Among them, the modulation coefficient rk
t is calcu-
lated by the following equation:
rk
t = σ
Qk
r

h1
t ; . . . ; hN
t

(34)
and then, the aggregation et is calculated by the following
equation:
et = ReLU
 N
X
k=1
rk
t Rk
r hk
t
!
(35)
where Qk
r and Rk
r are weight matrices. ReLU is the ReLU
activation function. Finally, the future steps are predicted by
a fully connected layer, ˆyk
t+1, . . . , ˆyk
t+lp = Linear1(et).
IV. EXPERIMENTAL RESULTS AND ANALYSIS
In this section, MRA-LSTM is validated on real-world UAV-
FDAD tasks. First, dataset, evaluation metrics, and parameter
setting are given in Section IV-A. Then, two thresholding
methods are provided in Section IV-B. Finally, comparison
results with peer competitors, statistical analysis, sensitivity
analysis, ablation studies, and more discussion are detailed in
Section IV-C.
1torch.nn.Linear: a common fully connected layer provided by Pytorch.
Fig. 5.
Proposed HSE.
TABLE II
DETAILS OF 47 REAL-WORLD UAV FLIGHTS
A. Dataset, Evaluation Metrics, and Parameter Setting
1) Dataset: AirLab Failure and Anomaly (ALFA) dataset2
is collected by a fixed-wing UAV platform. In Table II, flight
data consist of ten no-fault flights and 37 flights (one of them
has no ground truth, so it is not used) with single or multiple
types of anomaly. The data files in mat and bag formats contain
three types of data.
1) Data collected by MAVROS, including GPS information
and wind estimation. The names of these data files start
with “mavros/*,” such as “mavros/imu.” These topics
can be viewed on the MAVROS website.3
2) Data collected from each control surface such as aileron
and rudder, indicating the ground truth information. The
names of these data files start with “failure_status/*,”
such as “failure_status/rudder.”
3) Data collected from measurements or commands, such
as pitch and airspeed. The names of these files start with
“mavros/nav_info/*,” such as “mavros/nav_info/pitch.”
These topics can be viewed on the ArduPilot website.4
The most important details mentioned above are shown
in Table III. It can be seen that the ALFA dataset is an
MR-MTS dataset collected by multiple sensors.
2) Evaluation Metrics:
The accuracy (Acc), specificity
(Spe), precision (Pre), recall (Rec), F1-score (F1), and area
under curve (AUC) [11] are adopted as evaluation metrics.
The larger Acc, Spe, Pre, Rec, F1, AUC, and the better the
performance.
3) Parameter Setting: The ALFA dataset contains more
than 300 features. Most of them are not relevant to detection
and increase the difficulty of model training. In Table IV,
2ALFA dataset: http://theairlab.org/alfa-dataset
3MAVROS website: http://wiki.ros.org/mavros
4ArduPilot website: http://ardupilot.org/plane
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:29:09 UTC from IEEE Xplore.  Restrictions apply.

## Page 7

LU et al.: UAV FLIGHT DATA ANOMALY DETECTION BASED ON MULTIRATE-AWARE LSTM
3526713
TABLE III
LIST OF POTENTIALLY USEFUL FIELDS IN THE ALFA DATASET
we adopt the same 29 features as in literature [27] for the
experiment. They are selected from the features recommended
by the ALFA dataset creators [28] according to two rules:
1) the feature will be discarded if it is a derived feature
such as covariance between features and 2) the feature will
be discarded if the sensor stability is inadequate such as
the log source changes during flight. To enable a compre-
hensive comparison of different degrees of multirate, these
features are further divided into three feature sets, as shown
in Table V. Among them, Set C contains all the above
29 features. Based on literature [29], Sets A and B contain
eight and 21 features, respectively. It can be seen that the
MR-MTS formed by the selected features contains a great
span of sampling rates. In general, the critical experimen-
tal setups consist of two types: training hyperparameters
and network architecture hyperparameters. Regarding training
hyperparameter setups, all methods are trained (with Adam
optimizer) and validated (with fivefold cross validation) on
ten no-fault flights and tested on 36 anomaly flights with
single or multiple types of anomalies. For all methods, the
train set and valid set are split as 9:1, 30 epochs are used
for training, the batch size is 100, the dropout rate is 0.2,
the weight decay is 1e−3, and the initial learning rate is
2e−3 (lowered by ten times at epochs 10 and 20). Regarding
network architecture hyperparameter setups, other methods
are consistent with the original literature. The corresponding
codes are available from LightCTS,5 MPNN-LSTM,6 T-GCN,7
5https://github.com/AI4CTS/lightcts
6https://github.com/geopanag/pandemic_tgnn
7https://github.com/lehaifeng/T-GCN
TABLE IV
FEATURES EXTRACTED FROM THE ALFA DATASET
TABLE V
THREE SETS OBTAINED BY DIFFERENT FEATURE SELECTION METHODS
VAE-LSTM,8 AGCRN,9 and Dynamic-LSTM.10 To avoid
randomness, in statistical analysis, the mean and standard
deviation (mean ± std) of eight independent runs are reported.
In sensitivity analysis, 1.1 (or 10) and 0.9 (or 0.1) times the
original values are adopted. The experiments are performed on
GeForce RTX 3090 GPU and Intel11 Xeon11 CPU E5-2620 v4
with 128-GB RAM.
B. Thresholding Methods
As mentioned earlier, a high error (anomaly score) indicates
anomaly. In actual use, an error needs to be thresholded
and classified as anomalous or healthy. Ideally, supervised
learning methods could use a valid set with anomalies to learn
thresholds. However, sufficient anomaly data are not available
in UAV flight scenario. To enable an exhaustive comparison,
we adopt two thresholding methods to evaluate the algorithms.
1) Static Threshold: It is a static method [11] that uses
whole errors e to determine a threshold η from p thresholds
η. In turn, compare each et in e with the qth threshold. If
et > ηq, it is an anomaly and vice versa. Based on indications,
such as true positives (TPs), false positives (FPs), and false
8https://github.com/carrtesy/LSTMVAE-Pytorch
9https://github.com/LeiBAI/AGCRN
10https://github.com/khundman/telemanom
11Registered trademark.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:29:09 UTC from IEEE Xplore.  Restrictions apply.

## Page 8

3526713
IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 73, 2024
negatives (FNs), calculate Pre, Rec, and F1, respectively. After
p attempts, a threshold η corresponding to the best F1 is
finalized. Briefly, η is selected from the set
η = [η1, . . . , ηq, . . . , ηp]
(36)
such that
ηq = q
p max(e),
1 ≤q ≤p
(37)
where η is determined by
argmax(η) = F1(e, η)
(38)
then, all metrics are evaluated based on threshold η. However,
it requires the use of whole errors. Thus, it cannot be used in
practice and can only be used for algorithm comparison.
2) Dynamic Threshold: It is a dynamic method [25] that
uses partial errors e = [et−h, . . . , et−1] to determine a thresh-
old η. Thus, it can be used in practice. Briefly, the threshold
η is selected from the set
η = µ(es) + zσ(es)
(39)
where η is determined by
argmax(η) = 1µ(es)/µ(es) + 1σ(es)/µ(es)
|ea| + |Eseq|2
(40)
such that
1µ(es) = µ(es) −µ({es ∈es|es < η})
(41)
1σ(es) = σ(es) −σ({es ∈es|es < η})
(42)
ea = {es ∈es|es > η}
(43)
Eseq = continuous sequences of ea ∈ea
(44)
where z is an ordered set of positive integers and is recom-
mended to set it to 2–10. Once the threshold η is determined,
compare et with η. If et > η, it is an anomaly and vice versa.
Based on indications, all metrics are evaluated.
Due to the presence of random noise, the fluctuation of
residuals (i.e., errors e) may be significant [9]. To miti-
gate the effect of random noise, the exponentially weighted
average-based filter (EWAF) in literature [25] is adopted
to smooth the residuals for promoting the UAV-FDAD
performance.
C. Experimental Results and Analysis
In Table VI, five categories and 11 topics are designed to
demonstrate the performance of the proposed MRA-LSTM.
1) Comparison Results and Statistical Analysis: MRA-
LSTM is compared with VAE + LSTM (VAE-LSTM)
[16], TCN + Transformer (LightCTS) [18], Transfer learn-
ing + LSTM + GNN (MPNN-LSTM) [19], GNN + GRU
(T-GCN [22], AGCRN [24]), and Adaptation + LSTM
(Dynamic-LSTM) [25] in terms of Acc, Spe, F1 (synthesis
of Pre and Rec), and AUC. For a comprehensive comparison,
experiments are conducted on three feature sets (as shown
in Table V) and two thresholding methods (static threshold
and dynamic threshold). ST-A/B/C indicate the use of static
threshold and Sets A/B/C. DT-A/B/C indicate the use of
dynamic threshold and Sets A/B/C. At the bottom of Table VII,
TABLE VI
FIVE CATEGORIES AND 11 TOPICS ABOUT THE EXPERIMENT
“nos. +/−/ =” shows the count of instances for whether the
method is better, worse, or same as the others. As shown in
Table VII, in most cases (three 41/1/0 and one 40/2/0), MRA-
LSTM succeeds to achieve the best performance (highlighted
in bold letters). In terms of ST-A, ST-C, DT-A, and DT-C,
there is a significant improvement. It is worth noting that
MRA-LSTM performs well on feature Set A, while the
performance on feature Set B is unsatisfactory. However, it still
outperforms the other methods. In fact, it is also the reason for
adopting different feature selection methods to get different
feature sets. It is desired to exclude the effect of feature
selection to compare the performance with other algorithms
under different feature selection methods.
Each value in Table VII is obtained by statistical analysis,
namely, each method runs eight times independently. In detail,
the statistical results of MRA-LSTM are shown in Table VIII.
It can be seen that the maximum standard deviation (std) on
Set A does not exceed 0.4%. Even the maximum std on Set B
is 3.44%, this fluctuation is not significant compared to its
poor basis (65.06%). In other words, MRA-LSTM is stable.
Each value in Table VIII is the mean of the detection results
from 36 flights. Take ST-A as an example, and the results
are shown in Table IX. However, only from Table IX, MRA-
LSTM has no intuitive advantage. Its advanced competitors,
published on AAAI [19], NeurIPS [24], SIGKDD [25], and
so on, have also shown high performance on certain flights.
However, as shown in Fig. 6, in most cases, its competitors are
slightly better (in the local enlargement of the purple shadow)
when they are good and significantly worse when they are
bad. On balance, MRA-LSTM achieves an excellent overall
performance (highlighted in red line). Take AGCRN [24],
which dominates the most times, as an example; in the 1st and
27th flights, its accuracy is slightly better than ours (99.88%
versus 99.87% and 100.00% versus 99.88%). However, in the
22th and 26th flights, its accuracy is significantly worse than
ours (79.36% versus 95.59% and 51.47% versus 99.41%).
Regarding computational time cost, the average forward propa-
gation time (in seconds) of a batch (as shown in Section IV-A3,
consistent batch size for all methods) is given as follows:
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:29:09 UTC from IEEE Xplore.  Restrictions apply.

## Page 9

LU et al.: UAV FLIGHT DATA ANOMALY DETECTION BASED ON MULTIRATE-AWARE LSTM
3526713
TABLE VII
COMPARISON RESULTS BETWEEN MRA-LSTM AND PEER COMPETITORS
MRA-LSTM (2.03), VAE-LSTM (1.80), LightCTS (3.01),
MPNN-LSTM (2.53), T-GCN (2.39), AGCRN (4.52), and
Dynamic-LSTM (1.61). MRA-LSTM is ranked third out of
seven, which is acceptable considering its performance (in
terms of Acc, Spe, F1, and AUC). In addition, as shown in
Fig. 7, MRA-LSTM is more stable (the shorter the box, the
more stable it is) than its peer competitors for different flight
scenarios.
However, among 36 flights, MRA-LSTM has three invalid
cases (Acc < 60%), while its excellent competitors also have
four, five, five, four, five, and five invalid cases. Meanwhile,
these cases are almost identical (such as 16th, 23th, and 24th
flight). It may be because some normal patterns have not been
learned during the training phase. In turn, they will also be
treated as abnormal. This issue may be alleviated through
cross-domain few-shot learning [30], but it is not the focus
of this article.
2) Sensitivity Analysis: The critical hyperparameters consist
of training parameters, architecture parameters, and segment
length. Since their variations and combinations are countless,
TABLE VIII
STATISTICAL ANALYSIS OF MRA-LSTM VIA EIGHT INDEPENDENT RUNS.
EACH VALUE IS THE MEAN OF 36 DETECTION RESULTS, E.G., THE NO.
1 RUN IN CASE ST-A DERIVED FROM TABLE IX
Fig. 6.
Detection results of 36 flights in terms of Acc, Spe, F1, and AUC.
Fig. 7.
Boxplot of the detection results from 36 flights.
it is hard to enumerate all possibilities. We gradually modify
partial parameters to conduct sensitivity analysis. Baseline is
the recommended value adopted in this article. In Table X,
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:29:09 UTC from IEEE Xplore.  Restrictions apply.

## Page 10

3526713
IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 73, 2024
TABLE IX
BASED ON ST-A, IN TERMS OF 36 FLIGHTS, THE ANOMALY DETECTION RESULTS IN TERMS OF ACC (%), SPE (%), F1 (%), AND AUC (%)
it can be seen that MRA-LSTM is robust when changing
the parameters around the recommended parameter settings.
Especially, in terms of ST-A (as well as DT-A), the highest
Acc, Pre, Rec, Spe, F1, and AUC minus the lowest Acc,
Spe, F1, and AUC, the differences hover around only 0.3
(0.56), 0.47 (1.39), 0.23 (2.01), and 0.41 (1.19), respectively.
Since training is very time-consuming, this experiment is not
repeated to get the mean value. Thus, even if other parameter
setting performs better in a certain case, it cannot be said
that the recommended values are unsatisfactory. Taken overall,
minor hyperparameter changes have a small impact. It is
because an excellent network can compensate for the shortage
of hyperparameter settings.
3) Ablation Studies: For MR-MTS, we conduct experi-
ments to answer the following questions: 1) is the better
performance due to more computing resources? and 2) how
does each strategy contribute to the overall MRA-LSTM?
For the first question, as shown in the first row of Table XI,
the proposed multirate-aware structure is compared with
the traditional multilayer LSTM (denoted as baseline1 and
baseline2). For fairness, we adopt roughly the same computing
resource, including the number of layers and hidden state size.
For the second question, based on baseline1 (multirate-
aware structure), in the second row of Table XI, MR-MTS is
first compared with MTS obtained by data filling [22] (denoted
as S11 and S12). After that, based on baseline1 and S11, the
proposed multiscale update mechanism is compared with the
traditional continuous self-loop update mechanism (denoted
as S21 and S22). Finally, based on baseline1, S11, and S21,
the proposed HSE is compared with the traditional method
(denoted as S31 and S32).
As shown in the last three columns of Table XI, baseline1
is better than baseline2 in most cases, while adopting S11,
the performance can be further improved. Take ST-A as an
example, in terms of Acc, Spe, F1, and AUC, baseline2 values
are 84.42%, 77.82%, 80.04%, 82.88% lower than baseline1
86.69%, 80.73%, 83.02%, 82.99%, and further lower than
S11 89.91%, 84.33%, 90.84%, 86.82%. The same conclusion
can also be obtained based on ST-B, ST-C, DT-A, DT-B and
DT-C. It means that the improvement is more attributed to the
multirate-aware structure itself. In addition, as shown in the
third to sixth columns of Table XI, S21 is better than S22 in
all cases, while adopting S31, the performance can be further
improved. In sum, in most cases, the entirety (baseline1,
S11, S21, and S31) yields the best results (highlighted in
bold letters) and each strategy contributes to the overall
MRA-LSTM.
4) More Discussions: As mentioned earlier, to mitigate
the effect of random noise, the EWAF in literature [25] is
adopted to smooth the residuals. As shown in Fig. 8, in most
cases, EWAF succeeds to achieve the better performance
(the larger the blue area and the better the performance).
Taking the first row (Acc) and the first column (ST-A) as an
example, in terms of MRA-LSTM, VAE-LSTM, LightCTS,
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:29:09 UTC from IEEE Xplore.  Restrictions apply.

## Page 11

LU et al.: UAV FLIGHT DATA ANOMALY DETECTION BASED ON MULTIRATE-AWARE LSTM
3526713
TABLE X
SENSITIVITY ANALYSIS OF CRITICAL HYPERPARAMETER IN TERMS
OF ACC (%), SPE (%), F1 (%), AND AUC (%)
MPNN-LSTM, T-GCN, AGCRN, and Dynamic-LSTM (cor-
responding to 1, 2, 3, 4, 5, 6, and 7 in the radar chart), Acc with
EWAF (93.83%, 89.05%, 88.11%, 84.31%, 84.85%, 89.63%,
and 86.48%) is better than Acc without EWAF (93.66%,
83.87%, 83.03%, 83.86%, 84.17%, 89.52%, and 83.83%).
In detail, at the bottom and right of Fig. 8, “+/−/ =” shows
the count of instances for whether EWAF is better, worse,
or same than without EWAF. It can be seen that residual
filter EWAF can effectively mitigate the effect of random
noise.
As discussed earlier, MRA-LSTM can serve as an upstream
network for other methods to directly perform MR-MTS
anomaly detection. Taking the reconstruction-based VAE-
LSTM [16] as an example, our MRA-LSTM serves as an
encoder to demonstrate the above ability, denoted as MRA-
VAE-LSTM. In Table XII, MRA-VAE-LSTM succeeds to
achieve better performance in most cases. Especially in the
DT-B and the DT-C, there is a significant improvement.
It is worth noting that except for the encoder part, we have
not adjusted any of the hyperparameters of the original
VAE-LSTM to demonstrate the effectiveness and efficiency
of our MRA-LSTM to combine with other methods.
TABLE XI
ABLATION STUDY OF THE PROPOSED STRATEGIES IN TERMS OF ACC (%),
SPE (%), F1 (%), AND AUC (%)
Fig. 8.
Comparison results between considering random noise (with EWAF)
and not considering random noise (without EWAF).
For comprehensive demonstrations, an additional real-world
flight dataset12 is adopted. In Fig. 9, the flight test system
consists of an aircraft, a ground control station, and an
RC transmitter. From July 3 to 23, 2020, flight logs were
recorded. Moreover, we adopt the same features recommended
by the dataset creators to generate training and testing sam-
ples, which include the linear accelerations (ax, ay, and az),
angular rates (wx, wy, and wz), and autopilot commands
12https://github.com/mrtbrnz/fault_detection
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:29:09 UTC from IEEE Xplore.  Restrictions apply.

## Page 12

3526713
IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 73, 2024
TABLE XII
COMPARISON RESULTS BETWEEN THE ORIGINAL VAE-LSTM AND THE
PROCESSED VAE-LSTM (MRA-VAE-LSTM)
Fig. 9.
Flight test system of an additional real-world flight dataset [31].
Fig. 10.
Comparison results between MRA-LSTM and peer competitors in
terms of the 21st and 23rd flights.
(ucom1 and ucom2) [31]. The last two flights (July 21 and
23) containing anomaly patterns and static threshold [11] are
used for testing (anomaly detection). Normal data from other
flights are used for training. For both methods, the EWAF
is adopted to mitigate the effect of random noise. For the
critical experimental setups, except for the input and output
dimensions, most of the training hyperparameters and network
architecture hyperparameters are consistent with those outlined
in Section IV-A3.
Comparison results between MRA-LSTM and its competi-
tors are shown in Fig. 10. It can be seen that, in five of the eight
cases (four rows and two columns), MRA-LSTM is superior
to others. Even though MRA-LSTM is not ranked No.1 in
three cases, it is not too bad (No.3). Moreover, in most cases,
its state-of-the-art peer competitors are slightly better when
they are good and significantly worse when they are bad. For
instance, in terms of 21st flight, the accuracy of VAE-LSTM
and LightCTS (No. 1 and No. 2) is slightly better than that
of MRA-LSTM (93.5% and 92.8% versus 91.5%, i.e., 2.0%
and 1.3%). However, in terms of 23rd flight, their accuracy is
significantly worse than MRA-LSTM (86.8% and 88.9% ver-
sus 91.0%, i.e., −4.2% and −2.1%). The same conclusion can
also be derived in most other cases. Furthermore, in all cases,
other methods cannot always maintain the top three, but the
proposed MRA-LSTM could. MRA-LSTM still demonstrates
excellent performance.
V. CONCLUSION
In this article, a novel prediction-based MRA-LSTM has
been proposed for UAV-FDAD with MR-MTS data. In contrast
to previous multivariate regression models, the most merit of
the proposed method remains in its “multirate” characteristic.
Its major advantages are reflected in three contributions and
the ultimate aim is to directly conduct UAV-FDAD without
artificially tuning MR-MTS to MTS. The above purposes
have been validated on real-world UAV-FDAD tasks. In the
experiment, the comparison results show that MRA-LSTM
outperforms its state-of-the-art peer competitors. The statistical
analysis results and sensitivity analysis results indicate that
MRA-LSTM is stable and robust, respectively. The ablation
study results indicate that the overall MRA-LSTM yields the
best results and each strategy contributes to MRA-LSTM.
It should be noted that this article does not focus on the impact
of few-shot conditions, nor does it provide an in-depth study
of flight data recovery. In the future, we will focus on these
two fields and their applications in UAV few-shot flight data
anomaly detection and recovery prediction.
REFERENCES
[1] B. Wang, X. Peng, M. Jiang, and D. Liu, “Real-time fault detection for
UAV based on model acceleration engine,” IEEE Trans. Instrum. Meas.,
vol. 69, no. 12, pp. 9505–9516, Dec. 2020.
[2] K. He, D. Yu, D. Wang, M. Chai, S. Lei, and C. Zhou, “Graph attention
network-based fault detection for UAVs with multivariant time series
flight data,” IEEE Trans. Instrum. Meas., vol. 71, pp. 1–13, 2022.
[3] M. Carratù et al., “A novel methodology for unsupervised anomaly
detection in industrial electrical systems,” IEEE Trans. Instrum. Meas.,
vol. 72, 2023, Art. no. 3532812.
[4] X. Zhang et al., “Feature enhancement based on regular sparse model for
planetary gearbox fault diagnosis,” IEEE Trans. Instrum. Meas., vol. 71,
pp. 1–16, 2022.
[5] X. Chen, H. Wang, S. Lu, and R. Yan, “Bearing remaining use-
ful life prediction using federated learning with Taylor-expansion
network pruning,” IEEE Trans. Instrum. Meas., vol. 72, pp. 1–10,
2023.
[6] L. Ren, H. Wang, Z. Jia, Y. Laili, and L. Zhang, “Time-varying Gaussian
encoder-based adaptive sensor-weighted method for turbofan engine
remaining useful life prediction,” IEEE Trans. Instrum. Meas., vol. 72,
pp. 1–11, 2023.
[7] M. Carratù et al., “Anomaly detection on industrial electrical systems
using deep learning,” in Proc. IEEE Int. Instrum. Meas. Technol. Conf.
(I2MTC), May 2023, pp. 1–6.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:29:09 UTC from IEEE Xplore.  Restrictions apply.

## Page 13

LU et al.: UAV FLIGHT DATA ANOMALY DETECTION BASED ON MULTIRATE-AWARE LSTM
3526713
[8] R. Jin, Z. Chen, K. Wu, M. Wu, X. Li, and R. Yan, “Bi-LSTM-based
two-stream network for machine remaining useful life prediction,” IEEE
Trans. Instrum. Meas., vol. 71, 2022, Art. no. 3511110.
[9] B. Wang, D. Liu, Y. Peng, and X. Peng, “Multivariate regression-based
fault detection and recovery of UAV flight data,” IEEE Trans. Instrum.
Meas., vol. 69, no. 6, pp. 3527–3537, Jun. 2020.
[10] S. Liang, S. Zhang, Y. Huang, X. Zheng, J. Cheng, and S. Wu, “Data-
driven fault diagnosis of FW-UAVs with consideration of multiple
operation conditions,” ISA Trans., vol. 126, pp. 472–485, Jul. 2022.
[11] A. Garg, W. Zhang, J. Samaran, R. Savitha, and C.-S. Foo, “An eval-
uation of anomaly detection and diagnosis in multivariate time series,”
IEEE Trans. Neural Netw. Learn. Syst., vol. 33, no. 6, pp. 2508–2517,
Jun. 2022.
[12] H. Zhou, K. Yu, X. Zhang, G. Wu, and A. Yazidi, “Contrastive
autoencoder for anomaly detection in multivariate time series,” Inf. Sci.,
vol. 610, pp. 266–280, Sep. 2022.
[13] S. Longari, D. H. Nova Valcarcel, M. Zago, M. Carminati, and
S. Zanero, “CANnolo: An anomaly detection system based on LSTM
autoencoders for controller area network,” IEEE Trans. Netw. Service
Manage., vol. 18, no. 2, pp. 1913–1924, Jun. 2021.
[14] S. Maleki, S. Maleki, and N. R. Jennings, “Unsupervised anomaly
detection with LSTM autoencoders using statistical data-filtering,” Appl.
Soft Comput., vol. 108, Sep. 2021, Art. no. 107443.
[15] D. Guha, R. Chatterjee, and B. Sikdar, “Anomaly detection using LSTM-
based variational autoencoder in unsupervised data in power grid,” IEEE
Syst. J., vol. 17, no. 3, pp. 4313–4323, Sep. 2023.
[16] D. Park, Y. Hoshi, and C. C. Kemp, “A multimodal anomaly detector for
robot-assisted feeding using an LSTM-based variational autoencoder,”
IEEE Robot. Autom. Lett., vol. 3, no. 3, pp. 1544–1551, Jul. 2018.
[17] J. Zhong, Y. Zhang, J. Wang, C. Luo, and Q. Miao, “Unmanned
aerial vehicle flight data anomaly detection and recovery prediction
based on spatio-temporal correlation,” IEEE Trans. Rel., vol. 71, no. 1,
pp. 457–468, Mar. 2022.
[18] Z. Lai, D. Zhang, H. Li, C. S. Jensen, H. Lu, and Y. Zhao, “LightCTS:
A lightweight framework for correlated time series forecasting,” Proc.
ACM Manag. Data, vol. 1, no. 2, pp. 1–26, Jun. 2023.
[19] G. Panagopoulos, G. Nikolentzos, and M. Vazirgiannis, “Transfer graph
neural networks for pandemic forecasting,” in Proc. AAAI Conf. Artif.
Intell., May 2021, vol. 35, no. 6, pp. 4838–4845.
[20] Z. Wang, H. Lu, Y. H. Shi, and X. P. Wang, “Lightweight CNN
architecture design based on spatial–temporal tensor and its application
in bearing fault diagnosis,” IEEE Trans. Instrum. Meas., vol. 73, 2023,
Art. no. 3504112, doi: 10.1109/TIM.2023.3336435.
[21] S. Bai, J. Zico Kolter, and V. Koltun, “An empirical evaluation of generic
convolutional and recurrent networks for sequence modeling,” 2018,
arXiv:1803.01271.
[22] L. Zhao et al., “T-GCN: A temporal graph convolutional network for
traffic prediction,” IEEE Trans. Intell. Transp. Syst., vol. 21, no. 9,
pp. 3848–3858, Sep. 2020.
[23] Z. Che, S. Purushotham, G. Li, B. Jiang, and Y. Liu, “Hierarchical deep
generative models for multi-rate multivariate time series,” in Proc. Int.
Conf. Mach. Learn., Jul. 2018, pp. 783–792.
[24] L. Bai, L. Yao, C. Li, X. Wang, and C. Wang, “Adaptive graph
convolutional recurrent network for traffic forecasting,” in Proc. Adv.
Neural Inf. Process. Syst., vol. 33, Dec. 2020, pp. 1–12.
[25] K.
Hundman,
V.
Constantinou,
C.
Laporte,
I.
Colwell,
and
T. Söderström, “Detecting spacecraft anomalies using LSTMs and
nonparametric dynamic thresholding,” in Proc. 24th ACM SIGKDD Int.
Conf. Knowl. Discovery Data Min., Jul. 2018, pp. 387–395.
[26] M. Courbariaux, I. Hubara, D. Soudry, R. El-Yaniv, and Y. Bengio,
“Binarized neural networks: Training deep neural networks with weights
and activations constrained to +1 or -1,” 2016, arXiv:1602.02830.
[27] K. H. Park, E. Park, and H. K. Kim, “Unsupervised fault detection
on unmanned aerial vehicles: Encoding and thresholding approach,”
Sensors, vol. 21, no. 6, p. 2208, Mar. 2021.
[28] A. Keipour, M. Mousaei, and S. Scherer, “ALFA: A dataset for UAV fault
and anomaly detection,” Int. J. Robot. Res., vol. 40, no. 2, pp. 515–520,
Feb. 2021.
[29] M.
W.
Ahmad,
M.
U.
Akram,
R.
Ahmad,
K.
Hameed,
and
A. Hassan, “Intelligent framework for automated failure prediction,
detection, and classification of mission critical autonomous flights,” ISA
Trans., vol. 129, pp. 355–371, Oct. 2022.
[30] J. Oh, S. Kim, N. Ho, J. Kim, H. Song, and S. Yun, “Understanding
cross-domain few-shot learning based on domain similarity and few-shot
difficulty,” in Proc. Adv. Neural Inf. Process. Syst., vol. 35, Dec. 2022,
pp. 2622–2636.
[31] M. Bronz, E. Baskaya, D. Delahaye, and S. Puechmore, “Real-time
fault detection on small fixed-wing UAVs using machine learning,” in
Proc. AIAA/IEEE 39th Digit. Avionics Syst. Conf. (DASC), Oct. 2020,
pp. 1–10.
Hui
Lu
(Senior Member, IEEE) received the
Ph.D. degree in navigation, guidance and control
from Harbin Engineering University, Harbin, China,
in 2004.
She is currently a Professor with the School of
Electronic and Information Engineering, Beihang
University, Beijing, China. Her research interests
include information and communication systems,
intelligent optimization, and fault diagnosis and
prediction.
Zan Wang received the B.S. and M.S. degrees
from Northeastern University, Shenyang, China, in
2015 and 2020, respectively. He is currently pursu-
ing the Ph.D. degree with the School of Electronic
and Information Engineering, Beihang University,
Beijing, China.
His current research interests include evolutionary
computation, deep learning, anomaly detection, fault
diagnosis, and their applications.
Yuhui Shi (Fellow, IEEE) received the Ph.D. degree
in electrical and electronic engineering from South-
east University, Nanjing, China, in 1992.
From January 2008 to August 2017, he was at the
Department of Electrical and Electronic Engineer-
ing, Xi’an Jiaotong–Liverpool University, Suzhou,
China. From October 1998 to December 2007,
he was at Electronic Data Systems Corporation, Indi-
anapolis, IN, USA. From October 1995 to September
1998, he was at the Purdue School of Engineering
and Technology, Indianapolis. He is currently a
Chair Professor with the Department of Computer Science and Engineering,
Southern University of Science and Technology, Shenzhen, China. His main
research interests include swarm intelligence and applications.
Dr. Shi is the Editor-in-Chief of International Journal of Swarm Intelligence
Research.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 09:29:09 UTC from IEEE Xplore.  Restrictions apply.
