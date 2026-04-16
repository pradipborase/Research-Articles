# Multi-Source Ensemble Transfer Learning-Based Unmanned Aerial Vehicle Flight Data Anomaly Detection with Limited Data From Simulation to Reality,.pdf

## Page 1

Multi-source ensemble transfer learning-based unmanned aerial vehicle 
flight data anomaly detection with limited data: From simulation to reality
Lei Yang a, Shaobo Li b,*, Caichao Zhu c, Jian Liu d, Ansi Zhang e
a School of Mechanical Engineering, Guizhou University, Guiyang 550025, China
b School of Mechanical Engineering, Guizhou lnstitute of Technology, Guiyang 550025, China
c State Key Laboratory of Mechanical Transmission, Chongqing University, Chongqing 400044, China
d AVIC Guizhou Aircraft Co., Ltd, Anshun 561000, China
e State Key Laboratory of Public Big Data, Guizhou University, Guiyang 550025, China
A R T I C L E  I N F O
Keywords:
Unmanned aerial vehicle (UAV)
Multi-source ensemble transfer learning-based 
anomaly detection (MSETL-AD)
Dynamic time warping (DTW)
Long short-term memory with attention mech­
anism (LSTM-AM)
Adaptive anomaly detection
A B S T R A C T
Flight data anomaly detection is critical for ensuring the safety and reliability of unmanned aerial vehicles 
(UAVs). Traditional deep learning methods excel when sufficient data is available, but their performance 
significantly diminishes in data-scarce scenarios. Transfer learning is a promising solution; however, the per­
formance of single-source transfer methods is often limited when there is a significant discrepancy between the 
source and target domains. This paper proposes a multi-source ensemble transfer learning-based anomaly 
detection (MSETL-AD) framework, aiming to transfer knowledge from multiple simulated domains to a real 
domain for anomaly detection in UAV flight data with limited data. First, a similarity calculation method based 
on dynamic time warping (DTW) is utilized to select simulated source domains that are similar to the target 
domain to mitigate the negative transfer problem. Second, a modeling strategy based on long short-term memory 
with attention mechanism (LSTM-AM) integrating transfer learning and fine-tuning techniques is proposed, 
which constructs a fundamental LSTM-AM prediction model for each source domain and then fine-tunes it using 
limited data in the target domain during the transfer process. Then, a similarity-based transfer weight assignment 
method is designed to guide multi-source domains for integration. Next, a similarity-guided dynamic threshold 
calculation method based on extreme value theory with residual smoothing is introduced to overcome random 
noise interference and realize adaptive anomaly detection. Finally, the effectiveness of the proposed method is 
validated through experiments using multiple simulated UAV flight datasets as the source domains and a real 
UAV flight dataset as the target domain.
1. Introduction
Unmanned aerial vehicles (UAVs) are experiencing widespread 
adoption across diverse industries [1], attributed to their exceptional 
efficiency, flexibility, and cost-effectiveness, including intelligent traffic 
[2], agriculture [3,4], and marine monitoring [5] However, the absence 
of real-time monitoring by operators during UAV flights, combined with 
the complex and dynamic operational environment, presents numerous 
potential risks [6]. Factors like hardware malfunctions, adverse weather 
conditions, communication interference, and human errors can 
contribute to abnormal UAV operations, potentially leading to loss of 
control or accidents, posing a major challenge to the safe and reliable 
operation of UAVs. As UAV technology continues to evolve, ensuring 
their safety and reliability has emerged as a critical issue demanding 
urgent attention [7–9]. Flight data anomaly detection, an important 
aspect of UAV health management, has attracted much attention and 
research [9–13]. Through real-time monitoring and analysis of UAV 
flight data, anomalous behaviours or early signs of potential failure can 
be rapidly detected, enabling timely interventions to prevent further 
escalation and ensure operational safety. Therefore, flight data anomaly 
detection offers critical technical support for UAV health management 
and plays an essential role in maintaining the stability and safety of UAV 
operations in complex and dynamic environments.
In recent years, numerous studies related to UAV flight data anomaly 
detection have been conducted, including traditional machine learning- 
and deep learning-based methods [14]. The core idea of these methods is 
* Corresponding author.
E-mail address: lishaobo@gzu.edu.cn (S. Li). 
Contents lists available at ScienceDirect
Advanced Engineering Informatics
journal homepage: www.elsevier.com/locate/aei
https://doi.org/10.1016/j.aei.2025.103255
Received 28 November 2024; Received in revised form 28 February 2025; Accepted 9 March 2025  
Advanced Engineering Informatics 65 (2025) 103255 
Available online 14 March 2025 
1474-0346/© 2025 Elsevier Ltd. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

## Page 2

to utilize massive UAV flight data for the training of traditional machine 
learning or deep learning models to achieve good anomaly detection 
performance. However, obtaining sufficient historical flight data is not 
always feasible. For instance, during the test flight phase of a new type of 
UAV, the primary objective is to assess the fundamental functionality 
and system stability of the UAV, rather than to conduct extended or 
varied flight missions. Each flight may last only a few minutes, leading 
to a limited volume of flight data being collected during the initial 
stages. Moreover, designing and executing new flight plans to gather 
sufficient data often entails high operational costs, especially for me­
dium to large UAVs. This process involves various factors, including 
equipment transportation, mission planning, flight permit acquisition, 
and adaptation to weather conditions, all of which may contribute to 
expensive data collection costs. In such cases, most approaches often 
struggle to fully capture the underlying patterns within limited data. In 
the absence of sufficient historical flight data, developing effective 
anomaly detection methods is a major challenge.
Transfer learning has received much attention as a promising solu­
tion to effectively improve the performance of target tasks with limited 
samples [15–17]. According to the number of source domains, transfer 
learning methods can be categorized into single-source transfer learning 
methods and multi-source ensemble transfer learning methods [18]. 
Fig. 1 gives examples of single-source and multi-source ensemble 
transfer learning for time-series data prediction. As can be seen from 
Fig. 1(a), single-source transfer learning utilizes a single source domain 
data for model pre-training to learn the intrinsic patterns and features of 
the time series. The trained model is then transferred to the target 
domain with limited data. However, when there is a significant differ­
ence in the data distribution between the source domain and the target 
domain, the performance of single-source transfer learning methods can 
significantly degrade. Multi-source ensemble learning methods extract 
knowledge from multiple source domains with different data distribu­
tions, and then realize the prediction of time-series data in the target 
domain with limited data, as shown in Fig. 1(b). The advantage of such 
methods is to utilize diverse information from multiple source domains 
to enhance the generalization ability and robustness of the model. 
Despite this, there are still several issues and challenges that need to be 
considered and addressed, as outlined in section 2.2: (1) Insufficient 
exploration of multi-source ensemble transfer learning anomaly detec­
tion methods for UAV flight data. (2) Lack of effective source domain 
selection and transfer weight allocation strategies. (3) Access to real 
flight data for existing UAV types for model pre-training is still chal­
lenging due to commercial and security constraints.
To address the above-mentioned challenges, this paper proposes a 
multi-source ensemble transfer learning-based anomaly detection 
(MSETL-AD) framework for UAV flight data with limited data. First, 
multiple simulated UAV flight datasets collected are used as the source 
domains and a real UAV flight dataset collected is used as the target 
domain. Second, multiple simulated source domains similar to the target 
domain are selected using dynamic time warping (DTW). Then, a model 
based on long short-term memory with attention mechanism (LSTM- 
AM) is designed as the base prediction model, and a fine-tuning strategy 
is introduced to fully utilize the data distribution characteristics of the 
source and target domains to generate multiple base predictions for the 
target domain. Next, a similarity-based transfer weight assignment 
method is designed to guide multi-source domains for integration. 
Finally, guided by similarity, the extreme value theory and residual 
smoothing methods are combined to overcome random noise interfer­
ence and achieve adaptive anomaly detection. Specifically, the contri­
butions of this work are summarized as follows: 
1) A novel MSETL-AD framework for UAV flight data anomaly detec­
tion with limited data is proposed, leveraging knowledge transfer 
from multiple simulated domains to a real domain and avoiding the 
reliance on a large amount of real data for model pre-training.
2) A modeling strategy based on LSTM-AM integrating transfer learning 
and fine-tuning techniques is proposed to capture long-term de­
pendencies in data, enhance focus on critical information, and 
improve adaptability and performance in the target domain with 
limited data.
3) A similarity-based transfer weight assignment and dynamic 
threshold calculation method is proposed. It leverages DTW to assess 
the similarity between source and target domains, guiding the 
assignment of transfer weights to mitigate the negative transfer 
phenomenon. Meanwhile, a residual smoothing method and the 
extreme value theory are combined guided by similarity to reduce 
the effect of random noise and realize adaptive anomaly detection.
4) The effectiveness of MSETL-AD is validated by conducting extensive 
experiments using multiple simulated UAV flight datastes as the 
source domains and a real UAV flight dataset with limited data as the 
target domain.
The rest of this paper is organized as follows. Section 2 gives the 
related work. Section 3 outlines the detailed implementation steps of the 
proposed methodology framework. Section 4 analyzes and discusses the 
experimental results. Section 5 summarizes the study and indicates 
future research directions.
2. Related work
2.1. UAV flight data anomaly detection
Traditional machine learning techniques include k-nearest neighbors 
(KNN) [19], support vector machines (SVM) [20], decision tree (DT) 
[21], and kernel principal component analysis (KPCA) [22]. While these 
methods are effective under certain conditions, they have several limi­
tations when applied to complex and high-dimensional flight data. First, 
these methods often rely on manual feature extraction, a time- 
consuming process that is susceptible to errors. Second, most ap­
proaches assume that the data follow linear or simplistic patterns, 
Fig. 1. Examples of single-source domain and multi-source ensemble transfer learning for time-series data prediction.
L. Yang et al.                                                                                                                                                                                                                                    
Advanced Engineering Informatics 65 (2025) 103255 
2

## Page 3

whereas flight data typically exhibit nonlinear and time-varying char­
acteristics, making it challenging to capture complex dynamic re­
lationships. Furthermore, traditional methods lack effective noise 
suppression strategies, which often result in false positives and nega­
tives, affecting the accuracy and reliability of anomaly detection.
Deep learning-based methods have garnered significant attention in 
recent years due to their capability to autonomously extract and learn 
intricate features from data [14]. For example, Yang et al. [23] devel­
oped an unsupervised model based on long short-term memory and 
autoencoder (LSTM-AE) for anomaly detection in UAV altitude-related 
parameters. Jiang et al. [24] proposed a novel robust spatiotemporal 
autoencoder (RSTAE) model and validated the effectiveness of the 
method using real UAV flight data. Ahn H. and Chung S. [10] employed 
several autoencoder models to identify and detect anomalies in the flight 
data of individual UAV within a UAV swarm. Wang et al. [25] con­
structed a reconstruction model based on convolutional neural network 
(CNN) and autoencoder for anomaly detection in UAV actuators and 
achieved key parameter identification. Sadhu et al. [26] designed an 
autoencoder model integrating bidirectional long short-term memory 
(BiLSTM) and CNN, demonstrating robust fault detection capabilities on 
both real and simulated UAV flight data. Li et al. [27] proposed a novel 
convolutional variational autoencoder-generative adversarial network 
(CVAE-GAN) to detect anomalies in UAV sensor data. Wang et al. and 
Zhong et al. [28–30] utilized LSTM-based prediction models for anom­
aly detection in UAV flight data. He et al. [31] proposed a masked spatial 
graph attention network (GAT) with gated recurrent unit (GRU) 
(masked-SGAT-GRU) prediction model to detect anomalies in UAV flight 
data. Yang et al. [32] developed a prediction model using BiLSTM, one- 
dimensional CNN (1D CNN), and attention mechanism to detect 
anomalies in real UAV flight data. Liu et al. [33] constructed a predic­
tion model based on BiLSTM and incorporated transfer learning for 
cross-domain UAV actuator fault detection. Alos A. and Dahrouj Z. [34] 
developed an anomaly detection method based on convolutional LSTM 
model to detect anomaly patterns in UAV flight data. Wang et al. [35] 
proposed a fault detection method based on spatiotemporal graph 
attention transformer network (ST-GATrans) and validated the 
method’s effectiveness on collected UAV flight data. Yang et al. [36] 
designed an anomaly detection model based on 1D CNN-LSTM and 
verified its effectiveness on real UAV flight data. However, most 
methods rely on mass training data to achieve good detection perfor­
mance, and cannot achieve satisfactory detection results with limited 
training samples.
2.2. Transfer learning
Transfer learning has emerged as a promising paradigm to address 
data scarcity challenges in machine learning applications. However, 
there is still limited research on the application of transfer learning in 
anomaly detection for UAV flight data. In other domains, transfer 
learning-based anomaly or fault detection methods have demonstrated 
substantial success. For example, H. Wu, J. Zhao [37] utilized transfer 
learning to perform fault detection in the Tennessee Eastman (TE) pro­
cess with limited labeled samples. Mao et al. [38] proposed a deep one- 
class transfer learning algorithm with domain adversarial training and 
achieved good fault detection performance on image recognition 
detection and rolling bearings. Chen et al. [39] introduced a gaussian 
process-based adaptive self-transfer learning algorithm for anomaly 
detection in steam turbines. Zhao and Cai [40] employed transfer 
learning for cross-domain fault detection in aircraft engines with limited 
samples. Shang et al. [41] proposed an unsupervised transfer learning 
method for detecting faults in software defined network (SDN) con­
trollers. Although these studies provide valuable insights to address 
anomaly detection in UAV flight data with limited samples, they heavily 
rely on the data distribution of a single source domain. When there is a 
substantial discrepancy between the data distributions of the source and 
target domains, single-source transfer learning strategies may fail to 
deliver optimal results and could potentially result in negative transfer.
Multi-source ensemble transfer learning, as an effective approach, 
can effectively exploit the rich feature information across multiple 
source domains, without relying on a single source domain [42]. For 
example, Zhang et al. [43] proposed an approach based on a multi- 
channel hybrid information and deep transfer learning based approach 
for effective tool wear monitoring under variable conditions. Liu et al. 
[44] proposed a multi-source partial knowledge transfer method and a 
synthetic dataset and two manufacturing system datasets to validate the 
effectiveness of the proposed method. However, most approaches typi­
cally train models by directly integrating data from multiple source 
domains or assigning uniform weights to each source domain [43–46]. 
This can lead to increased computational overhead and may adversely 
impact the performance of transfer learning, particularly when there are 
substantial distributional discrepancies between the source domains and 
the target domain. Therefore, it is vital to effectively select source do­
mains and assign transfer weights in multi-source transfer ensemble 
learning; however, there is a dearth of related research in the field of 
anomaly detection for UAV flight data. In addition, most existing multi- 
source ensemble transfer learning methods usually rely on multiple real 
datasets as the source domains. However, for UAVs, it is difficult to 
obtain flight data for existing UAV types due to commercial and safety 
constraints, which makes it challenging to use real data for model pre- 
training.
3. The proposed methodology framework
Fig. 2 illustrates the proposed MSETL-AD framework for UAV flight 
data anomaly detection with limited data. First, the UAV multi-flight 
simulation data acquired by the simulation software is used as source 
domains, and the collected limited real UAV flight data is used as the 
target domain. Second, DTW is used to calculate the similarity between 
the multiple source domains and the target domain to select source 
domains that exhibit high similarity to the target domain for ensemble. 
Next, a fundamental LSTM-AM prediction model is constructed for each 
selected source domain, and model pre-training is conducted using the 
selected source domains. Then, each pre-trained model is fine-tuned and 
tested using the limited training samples and test data of the target 
domain. Subsequently, similarity is used to assign transfer weights to 
each basic predictions and weighted summation is performed to obtain 
the final prediction output for the target domain and the final prediction 
residuals for anomaly detection. Finally, a residual smoothing method is 
applied to smooth the residuals, and the extreme value theory is used to 
dynamically compute the thresholds based on the smoothed residuals, 
thus realizing adaptive anomaly detection. This section will detail each 
step of the framework, including similarity calculation, fundamental 
prediction model construction, multi-source ensemble transfer learning, 
and anomaly detection.
3.1. Similarity calculation
Selecting appropriate source domains for knowledge transfer is 
essential for enhancing the model performance of the target domain. 
Common methods for calculating similarity include cosine distance 
[47], Euclidean distance [48], and DTW [49–51]. The cosine distance 
quantifies the similarity between two vectors by computing the ratio of 
their inner product to the product of their magnitudes, with smaller 
values indicating higher similarity. The Euclidean distance assesses 
similarity by determining the straight-line distance between the source 
and target domains, where a smaller distance signifies greater similarity. 
However, both methods necessitate that the sequence lengths of the 
source and target domains be identical, as they perform pairwise com­
parisons between corresponding elements within the sequences. In 
practice, variations in data sources or inherent fluctuations within time 
series often render it challenging to ensure that the source and target 
domains possess identical sequence lengths. To address this challenge, 
L. Yang et al.                                                                                                                                                                                                                                    
Advanced Engineering Informatics 65 (2025) 103255 
3

## Page 4

this study employs DTW to evaluate the similarity between the source 
and target domains.
DTW employs dynamic programming algorithms to evaluate the 
similarity between temporal sequences, demonstrating superior 
robustness against minor temporal misalignments or phase shifts that 
frequently occur in practical applications [49]. Given two time series 
X = (x1, x2, ⋯, xM) and Y = (y1,y2,⋯,yN), where M and N represent the 
lengths of the time series X and Y, respectively. The distance between the 
mth sample in X and the nth sample in Y can be defined as follows: 
d(xm, yn) =
̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅
(xm −yn)2
√
, 1 ≤m ≤M, 1 ≤n ≤N
(1) 
where d
(
xm, yn
)
is the distance between the corresponding points. Then, 
the distance matrix about X and Y can be obtained, denoted as 
dm = (dmn)MN, where dij = d
(
xm,yn
)
. Based on this, DTW will continue 
to search the path Pa according to the dynamic programming method to 
get the shortest path between d11 and dMN as the similarity between X 
and Y. The expression can be defined as follows: 
ddtw(X, Y) = argmin(Pa) = argmin
̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅
∑
L
l=1
(xM −yN)2
√
√
√
√
(2) 
where ddtw(X, Y) is the final distance between X and Y, i.e., the 
similarity.
3.2. Fundamental prediction model construction
An effective model is vital for transfer learning success, offering a 
valuable initial model for the target task. LSTM has been widely 
demonstrated to be effective in anomaly detection for UAV flight data, 
owing to its exceptional capability to capture long-term dependencies 
[28,30,52]. However, when processing long sequences, the memory 
capacity of LSTM and its ability to capture long-range dependencies may 
be constrained, thus affecting model performance. To address this issue, 
the attention mechanism is introduced in this paper to focus more 
effectively on the most useful key information in the data and enhance 
the model’s capacity to capture complex patterns in long sequences.
3.2.1. LSTM
LSTM was first proposed in 1997 by Schmidhuber and Hochreiter to 
overcome the limitations of traditional recurrent neural networks 
(RNNs) in capturing long-term dependencies [53]. By incorporating 
memory cells and gates, LSTM can retain and update information over 
extended time periods, effectively mitigating issues such as vanishing 
and exploding gradients that hinder the learning process in standard 
RNNs [54]. The basic architecture of LSTM is shown in Fig. 3 and the 
related formulas are shown as follows: 
f(t) = σ
(
whfh(t −1) + wxfx(t) + bf
)
(3) 
i(t) = σ(whih(t −1) + wxix(t) + bi)
(4) 
̃C(t) = tanh(wxcx(t) + whch(t −1) + bc)
(5) 
C(t) = ft ⊙C(t −1) + i(t) ⊙̃C(t)
(6) 
o(t) = whoh(t −1) + wxox(t) + bo
(7) 
h(t) = o(t) ⊙tanh(C(t))
(8) 
where x(t) and h(t) are the input and output, C(t) is the cell state, f(t), 
i(t), and o(t) are the update information of the forget, input, and output 
gates, respectively, w and b are the weight and bias, σ and tanh are the 
Fig. 2. The overall process of the proposed MSETL-AD framework.
L. Yang et al.                                                                                                                                                                                                                                    
Advanced Engineering Informatics 65 (2025) 103255 
4

## Page 5

activation functions, and ⨀ denotes the dot product.
3.2.2. Attention mechanism
The attention mechanism aims to concentrate focus on relevant areas 
while diminishing attention to irrelevant ones [55]. This allows the 
model to prioritize more critical aspects when processing information, 
thereby enhancing both its performance and efficiency [56]. By selec­
tively emphasizing important features, the attention mechanism can 
improve the model’s ability to capture critical patterns and relation­
ships. At time t, for the output h(t) of LSTM, the related operation of the 
attention mechanism is shown in Eqs. (9)–(11). The structure of the 
attention mechanism is given in Fig. 4. 
e(t) = g(wah(t) + ba)
(9) 
a(t) = exp(e(t))
∑t
i=1e(i)
(10) 
S(t) =
∑
i
t=1
a(t)h(t)
(11) 
where e(t) is the attention rating function, a(t) is the attention proba­
bility distribution, g is the activation function, wa and ba are the weight 
and bias, and S(t) is the output of attention.
3.2.3. LSTM-AM model architecture
Combining the advantages of LSTM and the attention mechanism, 
LSTM-AM is designed as the fundamental prediction model in this paper, 
as illustrated in Fig. 5. This integrated approach leverages the sequential 
learning ability of LSTM along with the dynamic focus provided by the 
attention mechanism, resulting in the model that is better equipped to 
capture long-term dependencies and prioritize the most relevant infor­
mation in the data.
Specifically, the LSTM-AM model extracts hierarchical features and 
long short-term dependency information in time series through three 
LSTM layers. Meanwhile, two Dropout layers are incorporated to pre­
vent model overfitting. The attention mechanism is then added after the 
final LSTM layer to enhance the model’s ability to focus on critical time 
steps. Finally, the final prediction results are generated through two 
Dense layers. Table 1 gives the input and output shapes for each layer in 
the model architecture.
3.3. Multi-source ensemble transfer learning
3.3.1. Transfer learning
In transfer learning, domain and task are two core concepts [57]. A 
domain can be defined as Dom = {F, P(F)}, where F denotes the feature 
space and P(F) denotes the edge probability distribution of the feature 
space F. The feature space F can be further formalized as F =
{
f
⃒⃒fi ∈F,
i = 1,2,⋯,n
}
, i.e., the set consisting of specific features fi. After deter­
mining a particular domain Dom = {F, P(F)}, it is need to define the 
corresponding task, which can be represented as Task =
{
ylabel, g( • )
}
, 
where ylabel denotes the label space and g( • ) is a mapping function for 
Fig. 3. Structure of LSTM.
Fig. 4. Structure of the attention mechanism.
Fig. 5. Structure of the designed LSTM-AM model.
Table 1 
Input and output shapes of each layer.
Layer name
Input shape
Output shape
LSTM layer 1
(None, W, n)
(None, W, 128)
Dropout layer 1
(None, W, 128)
(None, W, 128)
LSTM layer 2
(None, W, 128)
(None, W, 64)
Dropout layer 2
(None, W, 64)
(None, W, 64)
LSTM layer 3
(None, W, 64)
(None, W, 32)
Attention layer
(None, W, 32)
(None, W, 32)
Dense layer 1
(None, W, 32)
(None, W, 16)
Dense layer 2
(None, W, 16)
(None, W, 1)
L. Yang et al.                                                                                                                                                                                                                                    
Advanced Engineering Informatics 65 (2025) 103255 
5

## Page 6

mapping instances of the feature space F to the label space ylabel. Given 
source and target domains Doms =
{(
fs,1, ys,1
label
)
,
(
fs,2, ys,2
label
)
, ⋯,
(
fs,n,
ys,n
label
)}
and Domt =
{(
ft,1, yt,1
label
)
,
(
ft,2, yt,2
label
)
, ⋯,
(
ft,n, yt,n
label
)}
, where 
fs,j ∈Fs and ft,j ∈Ft denote the observation samples in the source domain 
and the target domain, and ys,j
label ∈ys
label and yt,j
label ∈yt
label denote the la­
bels of fs,j and ft,j, respectively. The core of transfer learning involves 
passing the knowledge of the source domain to improve the performance 
of g( • ) in the target domain.
Transfer learning includes instance-, feature-, relationship-, and 
model (parameter)-based approaches [57]. Instance-based methods 
enhance learning in the target domain by selectively reusing samples of 
the source domain. Feature-based methods facilitate knowledge transfer 
by mapping data from the source and target domains to a shared feature 
space. Relationship-based approaches leverage the structural relation­
ship between the source and target domains to transfer knowledge from 
the source domain to the target domain. Model-based methods adapt 
specific tasks in the target domain by leveraging pre-trained models 
from the source domain. Considering the complexity and the size of the 
available data, this paper adopts the model-based transfer learning 
method to fully exploit the expressive power of pre-trained models and 
enhance task performance in the target domain.
3.3.2. Model pre-training
In this paper, the mean squared error (MSE) is employed as the 
training loss function in the model pre-training stage. MSE quantifies the 
discrepancy between the predicted and true values, and the model pa­
rameters are optimized by minimizing this loss function, thereby 
ensuring that the model’s predictions are closer to the actual values. 
Assuming that at moment t, the predicted output is ̂ytrain and the true 
value is ytrain, the loss function can be calculated by the following 
formula: 
L(̂ytrain, ytrain) = 1
λ
∑
λ
μ=1
( ̂y
μ
train −yμ
train
)2
(12) 
where L
( ̂ytrain, ytrain) is the loss function, λ is the length of training 
samples, and ̂yμ
train and yμ
train are the μth element of ̂ytrain and ytrain, 
respectively.
3.3.3. Model fine-tuning
In transfer learning, directly applying a pre-trained model from the 
source domain to the target domain often fails to achieve the desired 
performance. This is because the features of the target domain may 
differ significantly from those of the source domain. Therefore, this 
paper further employs a fine-tuning strategy that optimizes the pre- 
trained model, enabling it to better adapt to the features of the target 
domain. Meanwhile, the fine-tuning process uses a small amount of data 
from the target domain for retraining, effectively adjusting the model to 
the specific needs of the target domain, thereby indirectly addressing the 
problem of insufficient data in the target domain. In the fine-tuning 
stage, the parameters of the pre-trained model can be partially or fully 
frozen depending on the requirements. Specifically, we freeze the pa­
rameters of the first five layers of the LSTM-AM model and only fine- 
tune the last Attention layer and the two Dense layers, allowing the 
model to better learn the specific features of the target domain, as shown 
in Fig. 6.
Specifically, for a model containing K layers, the model parameters 
obtained after pre-training on the source domain can be defined as 
shown as follows: 
θsource = {θ1, θ2, ..., θK}
(13) 
where θsource is a parameter of the source domain model. For the frozen 
first η layers of parameters, i.e., θ1,θ2,⋯,θη, keep them θ1 = θ1
source, θ2 =
θ2
source, …,θη =
θη
source. For the unfrozen K −η layer parameters 
θη+1=θη+1
source, θη+2=θη+2
source, …, θK=θK
source that can be updated during the 
fine-tuning phase according to the following formula: 
θfine−tuned = argmin
θ L
(
̂y
fine−tuned
target
, yfine−tuned
target
)
(14) 
where yfine−tuned
target 
and ̂yfine−tuned
target 
are the original and predicted values of the 
fine-tuned samples, respectively, and L
(
̂yfine−tuned
target
, yfine−tuned
target 
is the loss 
Fig. 6. Fine-tuning process of the model.
L. Yang et al.                                                                                                                                                                                                                                    
Advanced Engineering Informatics 65 (2025) 103255 
6

## Page 7

function. θfine−tuned represents the fine-tuned parameters of the model. 
Therefor, θfine−tuned can be rewritten as follows: 
θfine−tuned =
{
θ1
source, ..., θη
source, θη+1
target, ..., θK
target
}
(15) 
where θη+1
target, …, θK
target is the model parameter after the update of θη+1,⋯,
θK. Therefore, when the model is tested using the test set of the target 
domain, the base predictions for each source domain can be obtained as 
follows: 
̂y
test
target = Model
(
θfine−tuned, xtest
target
)
(16) 
where ̂ytest
target is the prediction results, Model( • ) is the fine-tuned model 
of the target domain, and xtest
target is the test sample of the target domain.
3.3.4. Multi-source ensemble strategy
As mentioned earlier, relying only on a single source domain feature 
may lead to unsatisfactory prediction results. Multi-source ensemble 
aims to fully utilize information provided by models from other source 
domains to improve the overall prediction performance. This paper 
designs a similarity-based multi-source ensemble strategy to improve 
the performance of the target domain by rationally fusing multiple 
model prediction outputs. Fig. 7 displays the flowchart of the multi- 
source ensemble strategy.
For multiple source domains A = (a1, a2, ⋯, al ) and the target 
domain b, where l is the number of the source domains, the DTW values 
between each source domain and the target domains can be obtained 
based on Eq. (2), denoted as D = {ddtw(a1, b),ddtw(a2, b),⋯,ddtw(al , b)}. 
These DTW values are then summed as follows: 
dsum
dtw =
∑
ℓ
ε=1
ddtw(aε, b)
(17) 
where dsum
dtw is the total DTW value and ddtw(aε, b) denotes the DTW value 
between the ε th source domain and the target domain b. Based on Eq. 
(17), the transfer weights for each source domain can be obtained as 
follows: 
w(aε) = 1
ℓ
(
1 −ddtw(aε, b)
dsum
dtw
)
(18) 
where w(aε) is the transfer weight of the ε th source domain aε. 
Therefore, the final prediction result of the target domain can be defined 
as follows: 
yFER =
∑
ℓ
ε=1
w(aε)⋅Yε
(19) 
where yFER denotes the final ensemble result and Yε is the prediction 
result transferred from the ε th source domain aε.
3.4. Anomaly detection
Thresholds are particularly important for anomaly detection, and 
either too high or too low a threshold will lead to unreliable detection 
results [58]. Additionally, random noise can introduce uncertainty into 
the detection results, blurring the boundary between normal and 
abnormal data. However, on the one hand, most existing studies lack 
effective countermeasures against random noise [28]. They often over­
look the impact of noise on model performance. On the other hand, 
many studies rely on traditional statistical thresholds based on fixed 
distribution assumptions [23,28,30,32], which limits the model’s 
adaptability in complex scenarios, falling short of practical re­
quirements. To address these challenges, this paper introduces a 
similarity-guided dynamic threshold calculation method, and its flow­
chart is shown in Fig. 8. The core concept of the proposed approach and 
its implementation steps are detailed in the following sections.
3.4.1. Residual calculation
Residuals represent the difference between the model’s predicted 
values and the actual observed values. They effectively characterize the 
extent of anomalies in the data. When the residual value of a point ex­
ceeds a preset threshold, the point can be considered as an anomaly. 
Specifically, for the output of the training prediction results from each 
source domain’s, the training residuals can be computed using the 
following formula: 
rsource
train (ε) = ̂y
source
train (ε) −ysource
train (ε)
(20) 
where rsource
train (ε), ̂ysource
train (ε), and ysource
train (ε) are the training residuals, the 
predicted values of the training samples, and the true values of the ε th 
source domain, respectively. Similarly, the test residuals for the target 
domain test samples can be calculated for each of the fundamental 
prediction models using the following formula: 
Fig. 7. The flowchart of the multi-source ensemble strategy.
L. Yang et al.                                                                                                                                                                                                                                    
Advanced Engineering Informatics 65 (2025) 103255 
7

## Page 8

rtarget
test
( ε→) = ̂y
target
test ( ε→) −ytarget
test ( ε→)
(21) 
where rtarget
test ( ε→), ̂ytarget
test ( ε→), and ytarget
test ( ε→) are the test residuals, the 
predicted values, and the true values, respectively. Thus, based on Eq. 
(18), Eqs. (20) and (21), the final training and test residuals can be 
obtained by the following formula: 
rfinal
train =
∑
ℓ
ε=1
w(aε)⋅rsource
train (ε)
(22) 
rfinal
test =
∑
ℓ
ε=1
w(aε)⋅rtarget
test
( ε→)
(23) 
where rfinal
train and rfinal
test are the final training residuals and test residuals, 
respectively.
3.4.2. Residual smoothing
In real UAV flight data collection, the collected data is often affected 
by random noise. This noise arises from environmental factors such as 
wind speed variations, sensor limitations, and communication signal 
interference. From the predictive standpoint, random noise can prevent 
the model from accurately capturing the true trends or patterns in the 
data, thereby compromising prediction accuracy. Although the attention 
mechanism can effectively mitigate the interference of random noise on 
prediction results, from the anomaly detection perspective, random 
noise may still cause sharp fluctuations in the residuals. These sharp 
fluctuations not only increase the instability of the residuals but may 
also obscure potential anomalous patterns, thereby further complicating 
the anomaly detection process. To address this issue, the exponentially 
weighted moving average (EWMA) [59] method is introduced to smooth 
the residuals. Specifically, EWMA effectively retains the main trends in 
the data by assigning weights to historical values, while diminishing the 
impact of noise interference. Eqs. (24) and (25) give the smoothing 
formulas of EWMA for training residuals rfinal
train and test residuals rfinal
test . 
̃r
final
train(β) = α̃r
final
train(β −1) + (1 −α)rfinal
train(β)
(24) 
̃r
final
test (φ) = α̃r
final
test (φ −1) + (1 −α)rfinal
test (φ)
(25) 
where ̃rfinal
train(β) and rfinal
train(β) are the β th smoothed and original residuals of 
rfinal
train, ̃rfinal
test (φ) and rfinal
test (φ) are the φth smoothed and original residuals of 
rfinal
test , respectively, α is an adjustable weight parameter.
3.4.3. Anomaly determination
Traditional statistical thresholds rely on strict assumptions regarding 
the residual distribution like normality. However, when the residual 
distribution deviates from these assumptions, it may result in incorrect 
threshold settings, thus affecting the accuracy of anomaly detection. To 
address this issue, this paper introduces the streaming peaks-over- 
threshold (SPOT) method based on the extreme value theory [60]. It 
does not require strict assumptions about the residual distribution, thus 
overcoming the reliance on distributional assumptions of the traditional 
statistical thresholds.
Specifically, the SPOT utilizes the Pickands–Balkema–de Haan The­
orem, which rewrites (δ-Th) for the portion that exceeds the initial 
threshold Th and may follow the Generalized Pareto Distribution (GPD): 
F(t)(δ) = P(δ −Th > Δ|δ > Th) ∼
Th→τ
(
1 + γΔ
σ(t)
)−1
γ
(26) 
where γ and σ are the shape and scale parameters, respectively. GPD uses 
the maximum likelihood estimation to update the parameters γ and σ for 
SPOT updating as follows: 
logL(γ, σ) = −nThlogσ−
(
1 + 1
γ
) ∑
nTh
i=1
log
(
1 + γ
σ (δi −Th)
))
(27) 
where nTh denotes the total number of sample data points exceeding Th. 
Based on Eq. (27), the updated γ* and σ* can be obtained, and combined 
with Eq. (26), the following formula can be obtained: 
Fig. 8. The flowchart of the proposed anomaly detection method.
L. Yang et al.                                                                                                                                                                                                                                    
Advanced Engineering Informatics 65 (2025) 103255 
8

## Page 9

(
1 + γ∗
σ∗Φ
)−1
γ∗
= P(δ −Th > Φ)
P(δ > Th)
=
q
nTh/Ntotal
(28) 
where q represents the quantile of the extreme points and Ntotal is the 
total number of samples. Φ represents the difference between the final 
threshold zq and Th, i.e., Φ=zq −Th. Therefore, rewriting Eq. (28) can be 
obtained: 
zq = Th + γ∗
σ∗
((qNtotal
nTh
)−γ∗
−1
)
(29) 
Finally, anomaly detection is realized by comparing ̃r
final
test with the 
final threshold zq. Specifically, a point is considered anomalous when a 
smoothed residual ̃r
final
test (φ) of the φth sample is greater than the threshold 
zq(φ) corresponding to that sample, and vice versa. Thus, this process 
can be defined as follows: 
AD =
⎧
⎨
⎩
1,̃r
final
test (φ) > zq(φ)
0,̃r
final
test (φ) ≤zq(φ)
(30) 
where 1 means abnormal and 0 means normal.
4. Experimental results and analysis
4.1. Data description
4.1.1. Experimental data collection and selection
As previously discussed, obtaining large-scale real flight data for 
model pre-training is often difficult. However, with the assistance of 
simulation software, it is possible to efficiently generate abundant and 
varied flight data, thereby substantially reducing both the time and 
economic costs associated with data collection. Especially because UAVs 
are high-tech devices, they may be subject to strict data privacy and 
security protection measures [13]. Thus, flight data from existing UAVs 
are often inaccessible because of privacy concerns, which restricts data 
sharing and usage.Thus, in this paper, we use the XTDrone simulation 
software to obtain simulated flight data, which is based on PX4, ROS, 
and Gazebo, and has many built-in simulated UAVs [61]. A named 
“standard_vtol” composite wing UAV model was used. To closely 
simulate real-world scenarios, multiple flight paths are autonomously 
planned for this type of UAV. It is important to emphasize that, although 
the simulated data originates from the same UAV, the data distributions 
differ due to varying flight paths and the involvement of different flight 
conditions [62]. The real data used in this study came from the 
“Zhonghua Feng” composite wing UAV, which is an indigenously 
developed UAV. The UAV features a wingspan of 3900 mm, a payload 
capacity of 10 kg, and a maximum takeoff weight of 35 kg. The flight 
control system supports automatic, manual, and semi-automatic modes, 
enabling flexibility to meet many mission requirements. Flight data is 
transmitted to the ground station via a data transmission radio, facili­
tating continuous monitoring and analysis. Fig. 9 displays the simulated 
and real UAV flight data generation interface or acquisition platform.
Specifically, the simulated data was collected from five flights of the 
“standard_vtol” UAV, each conducted along different flight paths. For 
each flight, 12,000 sample points were extracted per feature for subse­
quent analysis. To distinguish the data, the flight data collected from 
these five flight paths are named SF1, SF2, SF3, SF4, and SF5, respec­
tively. Real data is from a single flight of the “Zhonghua Feng” UAV 
during the test flight phase is used. This data is named RF, and 6000 
sample points are extracted from the feature data for the experiment. 
SF1, SF2, SF3, SF4, and SF5 are used as source domains. RF is used as 
target domain. Sixteen flight parameters closely related to the flight 
attitude were selected as experimental data after carefully removing 
redundant and irrelevant parameters. Table 2 provides a detailed list of 
the names, meanings, and units of these parameters. Fig. 10 presents 
partial flight data curves for several source domains and the target 
domain.
4.1.2. Anomaly injection
This study is primarily concerned with evaluating the effectiveness of 
Fig. 9. UAV flight data generation interface or acquisition platform.
Table 2 
Flight data related to UAV attitude control used in this paper.
No.
Name
Meaning
Unit
1
GPSAlt
GPS altitude
m
2
GPSLat
GPS latitude
deg
3
GPSLon
GPS longitude
deg
4
Veast
East speed
m/s
5
Vnorth
North speed
m/s
6
VZ
Vertical speed
m/s
7
Airspeed
Air speed
m/s
8
Yaw
Yaw angle
deg
9
Pitch
Pitch angle
deg
10
Roll
Roll angle
deg
11
AccX
X-axis acceleration
m/s2
12
AccY
Y-axis acceleration
m/s2
13
AccZ
Z-axis acceleration
m/s2
14
WX
X-axis angular velocity
rad/s
15
WY
Y-axis angular velocity
rad/s
16
WZ
Z-axis angular velocity
rad/s
L. Yang et al.                                                                                                                                                                                                                                    
Advanced Engineering Informatics 65 (2025) 103255 
9

## Page 10

the proposed method in anomaly identification and detection. However, 
acquiring real abnormal flight data is challenging, as UAV failures and 
anomalous events are typically episodic and unpredictable. This chal­
lenge makes it difficult to obtain representative data of anomalies, and 
may incur substantial costs, particularly in the event of severe mal­
functions or accidents, which may lead to significant losses. To mitigate 
the risks and costs associated with actual flights, researchers typically 
employ anomaly injection methods to generate abnormal flight data 
[28,30–32,52]. In line with previous studies, this paper adopts the 
following formula for injecting bias and drift anomalies: 
y(t)anomaly =
{
y(t) + ϛ, bias
y(t) + ζ(t), drift
(31) 
where y(t) and y(t)anomaly are normal and abnormal flight data, respec­
tively, ϛ is a constant, and ζ(t) is a function of t. In this study, the x-axis 
angular velocity (WX) from the gyroscope is selected as the monitored 
parameter. The value of ϛ is taken as 3. Since the drift anomaly manifests 
in a more complex manner, we sample points at equal intervals within 
the range [3,4] to characterize ζ(t). Fig. 11 illustrates the monitored 
parameter WX after injecting bias and drift anomalies.
4.1.3. Data preprocessing
The maximum-minimum normalization method is used to normalize 
the raw data to eliminate the effect of flight features of different mag­
nitudes on the model performance, which is defined as follows: 
xnor =
xraw −xraw(min)
xraw(max) −xraw(min)
(32) 
where xnor, xraw(max), and xraw(min) are the normalized, maximum, and 
minimum values of the original data xraw, respectively.
Fig. 10. Partial flight data curves for some sources domains and the target domain.
Fig. 11. The monitored parameter WX with bias and drift anomalies.
L. Yang et al.                                                                                                                                                                                                                                    
Advanced Engineering Informatics 65 (2025) 103255 
10

## Page 11

4.2. Experimental setup
All experiments in this study were conducted on a server running 
Ubuntu 18.04.3, equipped with an Intel Xeon Silver 4210R CPU (2.40 
GHz) and 128 GB of RAM. During the model pre-training phase, the 
sliding window size was 1, the learning rate was 0.001, the number of 
training iterations was 100, and the batch size was 64. Adam was chosen 
as the optimizer, and a dropout rate of 0.3 was applied to reduce over­
fitting. SF1, SF2, SF3, SF4, and SF5 were used as training samples for 
model pre-training. During the model fine-tuning phase, the first 2000 
samples from the target domain RF, were used for fine-tuning, while the 
last 4000 samples were reserved for model performance evaluation. The 
hyperparameter settings for fine-tuning were further optimized: the 
learning rate was reduced to 0.0001, the batch size was adjusted to 32, 
and the number of training iterations was increased to 200. During the 
anomaly detection phase, the value of q was set to 1e-3. All code 
implementations were based on the TensorFlow framework.
4.3. Evaluation metrics
Mean absolute error (MAE) and root mean squared error (RMSE) 
[63,64] are used to evaluate model prediction performance, as defined 
in Eqs. (33)–(34). Smaller MAE and RMSE values indicate better pre­
diction accuracy. Accuracy (Acc), true positive rate (TPR), precision 
(Pr), false positive rate (FPR), and F1 score [65,66] are used to assess 
model anomaly detection performance, as defined in Eqs. (35)–(39). 
Higher values of Acc, TPR, Pr, and F1, along with a lower FPR, indicate 
superior anomaly detection performance. 
MAE = 1
N
∑
N
i=1
|yi −̂yi|
(33) 
RMSE =
̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅
1
N
∑
N
i=1
(yi −̂yi)2
√
√
√
√
(34) 
TPR =
TP
TP + FN × 100%
(35) 
FPR =
FP
TN + FP × 100%
(36) 
Acc =
TP + TN
TP + TN + FP + FN × 100%
(37) 
Pr =
TP
TP + FP × 100%
(38) 
F1 = 2 × Pr × TPR
Pr + TPR
× 100%
(39) 
where TP and TN represent the number of correctly identified abnormal 
and normal samples, respectively; FP and FN represent the number of 
normal samples misclassified as abnormal and abnormal samples mis­
classified as normal, respectively. yi and ̂yi denote the original and 
predicted values of the ith sample, respectively, and N denotes the 
sample length.
4.4. Experimental results and analysis
4.4.1. Source domain selection
Based on Section 3.1, the similarity between the target domain RF 
without injected anomalies and the source domains (SF1, SF2, SF3, SF4, 
and SF5) is calculated, and the results are presents in Table 3. It can be 
observed that the source domains most similar to the target domain RF 
are ranked as SF3, SF1, SF4, SF5, and SF2, with similarity values of 
1641956, 1678977, 1625462, 1643093, and 1672728, respectively. 
However, due to the challenge of defining a clear similarity threshold for 
source domain selection, directly integrating all source domains for 
transfer may lead to undesirable outcomes. To address this, we con­
ducted a comparative analysis of the model’s prediction performance 
using multi-source ensemble transfer methods. Without loss of gener­
ality, we also performed a comparative analysis of the model’s predic­
tion performance using single-source transfer methods. It is worth 
noting that multi-source ensemble transfer methods increase the number 
of source domains in descending order of similarity, ensuring that do­
mains more similar to the target domain are prioritized in the transfer 
process. The single-source ensemble transfer methods include five 
experimental groups, named SF1 → RF, SF2 → RF, SF3 → RF, SF4 → RF, 
and SF5 → RF. The multi-source ensemble transfer methods include four 
experimental groups, named SF31 → RF, SF314 → RF, SF3145 → RF, 
and SF31452 → RF. Fig. 12 shows the visualization of the prediction 
results for these methods. It can be observed that all methods capture the 
overall trend of the data well, but they exhibit noticeable prediction 
deviations in regions where the data undergoes sudden changes. This 
may be due to the strong nonlinearity and instability typically present in 
the change regions, where the model, with limited fine-tuning samples, 
is unable to effectively adapt to these characteristics, leading to an in­
crease in prediction errors. Table 4 lists the MAE and RMSE values for 
these methods. The MAE values for the single-source transfer methods 
are consistently higher than those for the multi-source ensemble transfer 
methods.
Specifically, the MAE values for SF1 → RF, SF2 → RF, SF3 → RF, SF4 
→ RF, and SF5 → RF are 1.61824, 1.67501, 1.72549, 1.65046, and 
1.70745, respectively, while the MAE values for the multi-source 
ensemble transfer methods are all below 1.60000. For the RMSE 
values, compared with the single-source transfer methods, the multi- 
source ensemble transfer methods also show more obvious advantages 
in most cases. This indicates that the multi-source ensemble transfer 
methods can improves the model prediction performance by integrating 
the information from multiple source domains and effectively reducing 
the prediction biases. It is observed that when the number of source 
domains is three, i.e., SF314 → RF, the minimum MAE and RMSE values 
are achieved. However, as the number of source domains increases, the 
MAE and RMSE values gradually rise. Although these results show only a 
small difference compared to SF314 → RF, it is still possible that the 
negative transfer phenomenon may be triggered to some extent when 
the subsequently added source domains are less similar to the target 
domain. Therefore, considering the computational efficiency and pre­
diction accuracy, this paper finally selects the three most similar source 
domains, i.e., SF3, SF1, and SF4, for ensemble transfer.
4.4.2. Model performance without model fine-tuning
To evaluate the model’s performance without model fine-tuning, 
four experiments are designed: transfer from the three most similar 
source domains individually, as well as integrating the transfer results 
from these three source domains. These experiments are named WSF3 
→ RF, WSF1 → RF, WSF4 → RF, and WSF314 → RF for easy differen­
tiation, respectively. We conduct these experiments using the real 
normal data without injected anomalies to thoroughly analyze and 
validate the prediction performance of these methods. Fig. 13 illustrates 
the visualization of the prediction results for these methods. It is readily 
apparent that, without model fine-tuning, these methods are unable to 
Table 3 
The similarity between the target domain and the source domains.
No.
Source domain name
DTW value
1
SF1
1,641,956
2
SF2
1,678,977
3
SF3
1,625,462
4
SF4
1,643,093
5
SF5
1,672,728
L. Yang et al.                                                                                                                                                                                                                                    
Advanced Engineering Informatics 65 (2025) 103255 
11

## Page 12

effectively fit the original data, resulting in significant prediction biases.
Table 5 presents the MAE and RMSE values for WSF3 → RF, WSF1 → 
RF, WSF4 → RF, and WSF314 → RF. The MAE and RMSE values for 
WSF3 → RF, WSF1 → RF, WSF4 → RF, and WSF314 → RF are as high as 
8.00000 and exceed 9.00000, respectively. In addition, it is observed 
that the MAE and RMSE values for WSF314 → RF are 15.69478 and 
16.52961, respectively. These values are significantly higher than those 
for WSF4 → RF. This disparity is attributed to the absence of model fine- 
tuning, which causes the model to produce large errors when directly 
predicting on the target domain test samples. Thus, despite the inte­
gration, the model’s prediction performance is not effectively improved. 
By comparing the prediction results of SF3 → RF, SF1 → RF, SF4 → RF, 
Fig. 12. The visualization of the prediction results for these methods.
Table 4 
The MAE and RMSE values for these methods.
Transfer method
MAE
RMSE
SF1 → RF
1.61824
3.40744
SF2 → RF
1.67501
3.49241
SF3 → RF
1.72549
3.32868
SF4 → RF
1.65046
3.54770
SF5 → RF
1.70745
3.42341
SF31 → RF
1.59844
3.30357
SF314 → RF
1.55943
3.27111
SF3145 → RF
1.56262
3.33790
SF31452 → RF
1.57252
3.34773
L. Yang et al.                                                                                                                                                                                                                                    
Advanced Engineering Informatics 65 (2025) 103255 
12

## Page 13

and SF314 → RF in Section 4.4.1, it is evident that fine-tuning plays a 
crucial and positive role in enhancing model performance, particularly 
when the number of available samples in the target domain is limited.
4.4.3. Model performance without transfer learning
To analyze the model’s performance without transfer learning, we 
first train the LSTM-AM model directly using the fine-tuned samples of 
the target domain RF. Subsequently, the model’s performance is eval­
uated using the test samples of the target domain RF. The method 
without transfer learning is named WTL-LSTM-AM. We conduct this 
experiment using data with injected anomalies. Fig. 14 displays the 
visualization of the prediction results for WTL-LSTM-AM for bias and 
drift anomalies. It can be observed that, although WTL-LSTM-AM seems 
to perform better in predicting during data transition regions compared 
to the methods mentioned earlier, it still exhibits noticeable prediction 
bias. This is because relying solely on a limited number of fine-tuned 
training samples from the target domain does not adequately capture 
the full range of feature variations, which negatively impacts the 
model’s prediction accuracy. In this case, the model suffers from over­
fitting. The MAE and RMSE values of WTL-LSTM-AM for bias and drift 
anomalies are 2.51502 and 3.79320, and 2.10179 and 3.35449, 
respectively.
Fig. 15 presents the visualization of bias and drift anomaly detection 
results for WTL-LSTM-AM. Although WTL-LSTM-AM is effective in 
correctly detecting normal samples across different anomaly types, it is 
prone to a high number of false positives, resulting in many missed 
detections. This indicates that while the model effectively identifies 
normal data, it struggles to distinguish anomalies, compromising 
detection performance. Specifically, for bias anomaly, the TPR, FPR, 
ACC, Pr, and F1 values of WTL-LSTM-AM are 99.67 %, 91.36 %, 42.79 
%, 39.57 %, and 56.65 %, respectively. For drift anomaly, the TPR, FPR, 
ACC, Pr, and F1 values of WTL-LSTM-AM are 99.27 %, 99.64 %, 37.46 
%, 37.42 %, and 54.35 %, respectively. Therefore, for the case of limited 
samples available in the target domain, WTL-LSTM-AM exhibits poor 
prediction and anomaly detection performance due to its inability to 
fully learn the features of the target domain during the model training 
phase. This highlights the effectiveness of the fine-tuning strategy 
employed in this paper.
4.4.4. Model performance of single-source transfer methods
This section evaluates the prediction and anomaly detection per­
formance of the single-source transfer methods. Fig. 16 illustrates the 
visualization of the prediction results for the single-source transfer 
methods. It can be observed that SF1 → RF, SF2 → RF, SF3 → RF, SF4 → 
RF, and SF5 → RF are equally effective in fitting the overall trend of the 
data. However, these methods still exhibit considerable deviations in 
regions where the data undergoes abrupt changes. The cause of this 
phenomenon is as described in Section 4.4.1. Table 6 lists the MAE and 
RMSE values for SF1 → RF, SF2 → RF, SF3 → RF, SF4 → RF, and SF5 → 
RF. The MAE and RMSE values for SF1 → RF, SF2 → RF, SF3 → RF, SF4 
→ RF, and SF5 → RF show little difference in prediction performance on 
Fig. 13. The visualization of prediction results without fine-tuning.
Table 5 
The MAE and RMSE values for above methods.
Experiment name
MAE
RMSE
WSF3 → RF
20.84240
22.61530
WSF1 → RF
22.21301
23.29603
WSF4 → RF
8.65067
9.06122
WSF314 → RF
15.69478
16.52961
L. Yang et al.                                                                                                                                                                                                                                    
Advanced Engineering Informatics 65 (2025) 103255 
13

## Page 14

normal data, as analyzed in Section 4.4.1. This indicates that transfer 
learning can effectively enhance the model’s robustness in handling 
abnormal data. Moreover, compared to WTL-LSTM-AM, SF1 → RF, SF2 
→ RF, SF3 → RF, SF4 → RF, and SF5 → RF demonstrate significant 
improvements in MAE and RMSE values for bias and drift anomalies. 
Specifically, these methods achieve MAE values ranging from 1.61000 
to 1.72000 and RMSE values ranging from 3.30000 to 3.60000.
Fig. 17 shows the visualization of the anomaly detection results for 
SF1 → RF, SF2 → RF, SF3 → RF, SF4 → RF, and SF5 → RF. It is evident 
that most methods are effective in identifying normal samples; however, 
they perform poorly in detecting abnormal samples. This can be 
observed from the distribution of TP and FP across these methods. SF3 
→ RF is an exception, as it accurately detects most abnormal samples, as 
evidenced by the distribution of TN. However, SF3 → RF exhibits a 
higher number of FN compared to other methods.
Table 7 lists the anomaly detection results for SF1 → RF, SF2 → RF, 
SF3 → RF, SF4 → RF, and SF5 → RF. SF3 → RF demonstrates relatively 
strong overall performance in anomaly detection, with TPR, FPR, ACC, 
Pr, and F1 values of 67.60 %, 5.04 %, 84.70 %, 88.95 %, and 76.82 % for 
bias anomaly, and 66.40 %, 1.84 %, 86.25 %, 95.59 %, and 78.36 % for 
drift anomaly, respectively. Despite the better performance of SF3 → RF 
in several metrics, there is still room for further improvement in its TPR 
and F1 values. The performance of SF1 → RF follows closely behind SF3 
→ RF, but its FPR values are higher, with 5.04 % for bias anomalies and 
9.96 % for drift anomalies. This indicates that although SF1 → RF is 
effective at identifying normal samples, it still faces challenges in 
accurately detecting abnormal samples. For SF2 → RF, SF4 → RF, and 
SF5 → RF, although the TPR values of these methods are equally 
excellent, with TPR values exceeding 90.00 % for both bias and drift 
anomalies, their performance in other performance metrics is deficient. 
Specifically, the variations of FPR, ACC, Pr, and F1 values for SF2 → RF, 
SF4 → RF, and SF5 → RF range from 63.83 % to 94.00 %, 39.58 % to 
57.01 %, 37.89 % to 46.31 %, and 54.26 % to 61.55 %, respectively. The 
results suggest that the performance of these methods is significantly 
constrained when relying solely on data features from a single source 
domain, particularly when transferring knowledge to the target domain. 
These results suggest that, while these methods demonstrate relatively 
good prediction accuracy, they struggle to achieve a balanced trade-off 
between prediction accuracy and anomaly detection performance. This 
may hinder their effectiveness in practical applications.
4.4.5. Model performance of multi-source ensemble transfer methods
The performance of the proposed MSETL-AD method is compre­
hensively analyzed and evaluated, encompassing both anomaly detec­
tion and prediction performance to provide a thorough assessment of its 
overall effectiveness. Meanwhile, to verify the effectiveness of MSETL- 
Fig. 14. The visualization of prediction results for WTL-LSTM-AM.
Fig. 15. The visualization of WTL-LSTM-AM’s anomaly detection results.
L. Yang et al.                                                                                                                                                                                                                                    
Advanced Engineering Informatics 65 (2025) 103255 
14

## Page 15

AD, a comparison experiment was conducted with the current state-of- 
the-art method in the field, as presented in the literature [33]. Since 
the study did not explicitly provide the name of the method, it is referred 
to as BiLSTM-TL in this paper for the purpose of facilitating the subse­
quent analysis. In addition, we also include an advanced multi-source 
transfer learning guided ensemble LSTM (MTE-LSTM) [51] method in 
the comparison experiments. Although MTE-LSTM was originally pro­
posed for predicting building multi-load, it is equally applicable to the 
task in this paper. Therefore, MTE-LSTM is also used as a benchmark to 
comprehensively evaluate the effectiveness of MSETL-AD. Fig. 18 shows 
the visualization of prediction results for MSETL-AD, BiLSTM-TL, and 
MTE-LSTM. Although these methods still exhibit a significant prediction 
bias in the mutated region of the data, they all capture the overall trend 
more effectively. However, further observation reveals that, compared 
to MSETL-AD and BiLSTM-TL, MTE-LSTM exhibits overfitting to the 
noisy data. This is because MTE-LSTM utilizes the LSTM structure, 
which is prone to memorizing noise features when handling long 
sequence data, leading to overfitting to the noise. In contrast, although 
BiLSTM-TL mitigates overfitting to noise to some extent by leveraging 
the interaction of bidirectional information, its effect is still relatively 
limited. Compared to MTE-LSTM and BiLSTM-TL, MSETL-AD captures 
the long-term dependencies in time series using LSTM and emphasizes 
important features by integrating the attention mechanism, thereby 
enhancing its ability to model data trends while effectively reducing 
noise interference.
The above analysis is also reflected in Table 8, which lists the MAE 
and RMSE values. The MAE and RMSE values for MTE-LSTM are the 
highest for both bias and drift anomalies, with values of 1.98678 and 
3.91059, respectively. The MAE and RMSE values for BiLSTM-TL are 
1.63844 and 3.48378 for bias anomaly, and 1.63848 and 3.48375 for 
drift anomaly, respectively. In comparison, MSETL-AD achieves the 
lowest MAE and RMSE values, with 1.55935 and 3.27438 for bias 
anomaly, and 1.56028 and 3.28292 for drift anomaly, respectively. This 
indicates that MSETL-AD possesses stronger prediction capability, and 
its performance in extracting key features and suppressing noise inter­
ference is superior to that of MTE-LSTM and BiLSTM-TL. Further anal­
ysis of the prediction performance of single-source transfer methods as 
analyzed in Section 4.4.4 shows that MSETL-AD also achieves the lowest 
MAE and RMSE values. This further demonstrates that the model’s 
prediction performance can be significantly enhanced through multi- 
source ensemble transfer.
Fig. 19 presents the visualization of anomaly detection results for 
MTE-LSTM, BiLSTM-TL, and MSETL-AD. It should be emphasized that to 
ensure fairness, we adopt the threshold calculation method proposed in 
this paper for all the baseline methods. As shown in Fig. 19, these 
methods all exhibit a relatively large number of TP, with MTE-LSTM and 
BiLSTM-TL being the most notable. However, it is encouraging to see 
that these methods can effectively detect most abnormal samples, as 
evidenced by the distribution of TN. Table 9 lists the anomaly detection 
results for MTE-LSTM, BiLSTM-TL, and MSETL-AD for different anomaly 
types. Specifically, compared to other methods, MTE-LSTM achieves the 
lowest FPR and the highest Pr values for drift anomaly, with values of 
0.40 % and 98.99 %, respectively. Its ACC and F1 values are also rela­
tively high. For bias anomaly, MTE-LSTM performs similarly well on 
these metrics. BiLSTM-TL obtains FPR, ACC, Pr, and F1 values of 2.76 %, 
86.47 %, 93.71 %, and 79.17 %, and 1.52 %, 87.27 %, 96.44 %, and 
80.17 % for bias and drift anomalies, respectively. Compared to other 
methods, BiLSTM-TL achieves the smallest FPR value for bias anomaly. 
Fig. 16. The visualization of prediction results for single-source transfer methods.
Table 6 
The MAE and RMSE values for single-source transfer methods.
Anomaly type
Transfer method
MAE
RMSE
Bias anomaly
SF1 → RF
1.61520
3.40762
SF2 → RF
1.67518
3.49218
SF3 → RF
1.71306
3.32974
SF4 → RF
1.64772
3.54712
SF5 → RF
1.70966
3.42654
Drift anomaly
SF1 → RF
1.61542
3.40985
SF2 → RF
1.67223
3.49038
SF3 → RF
1.71919
3.32874
SF4 → RF
1.64829
3.54745
SF5 → RF
1.70846
3.42510
L. Yang et al.                                                                                                                                                                                                                                    
Advanced Engineering Informatics 65 (2025) 103255 
15

## Page 16

However, for the TPR values, MTE-LSTM and BiLSTM-TL fall below 
70.00 %. In contrast, MSETL-AD achieves the highest TPR value of 
83.87 % for bias and drift anomalies, and delivers optimal performance 
across several other metrics, including ACC and F1 values. Specifically, 
in addition to the TPR values, the FPR, ACC, Pr, and F1 values of MSETL- 
AD for bias and drift anomalies are 3.28 %, 91.90 %, 93.88 %, and 88.59 
%, and 1.48 %, 93.02 %, 97.14 %, and 90.02 %, respectively. It is also 
observed that although MSETL-AD’s TPR values are not as high as most 
of the single-source transfer methods analyzed in Section 4.4.4, these 
single-source methods achieve their performance at the cost of other 
important metrics. In contrast, MSETL-AD strikes a better balance be­
tween TPR values and other performance metrics. These results 
emphasize the superior anomaly detection performance of MSETL-AD 
compared to the baseline methods and the single-source transfer 
methods.
4.4.6. Model performance without source domain selection
To validate the necessity and effectiveness of source domain selec­
tion, the model performance without source domain selection is 
analyzed, i.e., all source domains are directly merged and used for model 
pre-training, which is named SF6 → RF. Fig. 20 illustrates the visuali­
zation of prediction results for SF6 → RF. Similar to the results of the 
aforementioned experiments, SF6 → RF still exhibited noticeable re­
covery deviations in regions with abrupt data changes. Specifically, the 
MAE and RMSE values of SF6 → RF for bias and drift anomalies are 
1.61957 and 3.49847, and 1.61463 and 3.49601, respectively, both 
lower than those of MSETL-AD. Fig. 21 illustrates the visualization of 
anomaly detection results for SF6 → RF. It is clearly observed that, 
compared to MSETL-AD, SF6 → RF exhibits poorer discrimination 
ability for anomalous samples, resulting in a higher number of FP. For 
bias and drift anomalies, the TPR, FPR, ACC, Pr, and F1 values of SF6 → 
RF are 92.87 %, 79.43 %, 47.69 %, 41.24 %, and 57.11 %, and 93.00 %, 
Fig. 17. The visualization of the anomaly detection results for SF1 → RF, SF2 → RF, SF3 → RF, SF4 → RF, and SF5 → RF.
Table 7 
Anomaly detection of single-source domain transfer methods.
Transfer method
Anomaly type
TPR
FPR
ACC
Pr
F1
SF1 → RF
Bias anomaly
90.20 %
21.13 %
83.12 %
71.93 %
80.04 %
Drift anomaly
90.27 %
9.96 %
90.12 %
84.47 %
87.27 %
SF2 → RF
Bias anomaly
91.67 %
66.47 %
55.34 %
45.29 %
60.63 %
Drift anomaly
91.73 %
63.83 %
57.01 %
46.31 %
61.55 %
SF3 → RF
Bias anomaly
67.60 %
5.04 %
84.70 %
88.95 %
76.82 %
Drift anomaly
66.40 %
1.84 %
86.25 %
95.59 %
78.36 %
SF4 → RF
Bias anomaly
94.33 %
81.63 %
46.86 %
40.96 %
57.11 %
Drift anomaly
94.33 %
77.23 %
49.61 %
42.30 %
58.41 %
SF5 → RF
Bias anomaly
95.53 %
94.00 %
39.58 %
37.89 %
54.26 %
Drift anomaly
95.60 %
91.80 %
40.99 %
38.47 %
54.86 %
L. Yang et al.                                                                                                                                                                                                                                    
Advanced Engineering Informatics 65 (2025) 103255 
16

## Page 17

72.03 %, 52.36 %, 43.66 %, and 59.42 %, respectively. Although the 
TPR values of SF6 → RF exceed that of MSETL-AD, its performance in 
other metrics is poorer, such as the FPR values of SF6 → RF all exceed 72 
%, while the ACC, Pr, and F1 values are all below 60 %. The results 
indicate that directly merging all source domains for model pre-training 
may negatively impact model performance. This is primarily due to the 
inclusion of source domains with low similarity, which can undermine 
the overall effectiveness of the model.
4.4.7. Model performance using statistical thresholds without residual 
smoothing
To evaluate the effectiveness of the dynamic threshold with residual 
smoothing method used in this paper, the model performance using 
statistical thresholds without residual smoothing is analyzed. Specif­
ically, this section uses the commonly used n-sigma statistical threshold 
for anomaly detection for residuals that are not smoothed. The n-sigma 
statistical threshold can be described as ℷ+t δ, where ℷ is the mean of the 
training residuals, δ is the standard deviation of the training residuals, 
Fig. 18. The visualization of prediction results for MTE-LSTM, BiLSTM-TL,and MSETL-AD.
Table 8 
The MAE and RMSE values for MTE-LSTM, BiLSTM-TL, and MSETL-AD.
Anomaly type
Method
MAE
RMSE
Bias anomaly
MTE-LSTM
1.98678
3.91059
BiLSTM-TL
1.63844
3.48378
MSETL-AD
1.55935
3.27438
Drift anomaly
MTE-LSTM
1.98678
3.91059
BiLSTM-TL
1.63848
3.48375
MSETL-AD
1.56028
3.28292
Fig. 19. The visualization of anomaly detection results for MTE-LSTM, BiLSTM-TL, and MSETL-AD.
L. Yang et al.                                                                                                                                                                                                                                    
Advanced Engineering Informatics 65 (2025) 103255 
17

## Page 18

and t is a constant. In this paper, the value of t is taken as 1, 2, and 3 to 
comprehensively examine the effects of different thresholds on the 
model performance. For ease of analysis, the model using statistical 
thresholds without residual smoothing is named MST-WRS. Table 10
lists the anomaly detection results of MST-WRS. It can be found that the 
TPR value increases significantly as the t value increases, but the FPR 
Table 9 
Anomaly detection results of MTE-LSTM, BiLSTM-TL,and MSETL-AD.
Method
Anomaly type
TPR
FPR
ACC
Pr
F1
MTE-LSTM
Bias anomaly
65.47 %
4.16 %
84.45 %
90.42 %
75.95 %
Drift anomaly
65.53 %
0.40 %
86.82 %
98.99 %
78.86 %
BiLSTM-TL
Bias anomaly
68.53 %
2.76 %
86.47 %
93.71 %
79.17 %
Drift anomaly
68.60 %
1.52 %
87.27 %
96.44 %
80.17 %
MSETL-AD
Bias anomaly
83.87 %
3.28 %
91.90 %
93.88 %
88.59 %
Drift anomaly
83.87 %
1.48 %
93.02 %
97.14 %
90.02 %
Fig. 20. The visualization of prediction results for SF6 → RF.
Fig. 21. The visualization of anomaly detection results for SF6 → RF.
L. Yang et al.                                                                                                                                                                                                                                    
Advanced Engineering Informatics 65 (2025) 103255 
18

## Page 19

value also increases dramatically, leading to a decrease in the ACC and 
Pr values. For example, when t increases from 1 to 3, the TPR value of 
bias anomaly increases from 67.93 % to 91.93 %, but the FPR value 
sharply increases from 7.56 % to 48.42 %, and the ACC value decreases 
from 83.25 % to 66.72 %. These results further demonstrate the effec­
tiveness of the dynamic threshold with residual smoothing proposed in 
this paper.
4.4.8. Discussion
The main findings of this study through a series of experiments are 
described as follows: 
(1) This study systematically validates the effectiveness of knowl­
edge transfer from the simulated domains to the real domain with 
limited data. The results demonstrate that selecting highly 
correlated simulated source domains and through methods such 
as transfer learning and fine-tuning strategy can significantly 
improve the prediction and anomaly detection performance of 
the model in the real domain with limited data. This finding 
provides strong theoretical support and practical validation for 
solving the model pre-training problem in scenarios where real 
data is difficult to obtain, and has important practical application 
value.
(2) The proposed framework MSETL-AD significantly outperforms 
single-source transfer methods and other comparison methods in 
prediction accuracy and anomaly detection performance. MSETL- 
AD incorporates methods such as similarity computation, resid­
ual smoothing, and dynamic thresholding, which suppresses the 
negative transfer phenomenon while efficiently reduces the 
interference of random noise and enhances the adaptive capa­
bility of the detection threshold. The synergy of these techniques 
not only optimizes the overall performance of the model, but also 
provides a more accurate and reliable solution for anomaly 
detection in complex scenarios.
Although this study revealed some important findings, there are still 
some limitations. First, since this study involves multiple source do­
mains, the integration and processing of data is relatively time- 
consuming. Second, this study utilizes only a single real UAV flight 
dataset for experiments, lacking sufficient validation of the model’s 
generalization. Third, this study lacks a systematic analysis of different 
noise intensities and types and their specific effects on prediction ac­
curacy and threshold selection, which may lead to difficulties in effec­
tively guaranteeing the robustness and reliability of the model in real 
complex environments. Therefore, lightweight models can be adopted to 
reduce computational costs in future research. Furthermore, systematic 
verification of multi-flight real UAV flight data and comprehensive 
assessment of noise impact are also key directions for future research to 
further improve the generalization ability and robustness of the model.
5. Conclusion
To achieve UAV flight data anomaly detection with limited data, this 
paper proposed a novel MSETL-AD framework. First, DTW was 
employed to select multiple source domains similar to the target 
domain, mitigating the negative transfer phenomenon. Second, a 
modeling strategy based on LSTM-AM incorporating transfer learning 
and fine-tuning was proposed, which constructed a fundamental LSTM- 
AM prediction model for each source domain, and then fine-tuned it to 
generate multiple base predictions using limited target domain data. 
Then, a similarity-based transfer weight assignment method was 
designed to guide the integration of multiple source domains. Subse­
quently, a dynamic threshold calculation method based on extreme 
value theory with residual smoothing guided by similarity was intro­
duced to mitigate noise interference and enable adaptive anomaly 
detection. Finally, extensive experiments were conducted using multiple 
simulated UAV flight datasets as the source domains and a real UAV 
flight dataset as the target domain. The TPR, FPR, ACC, Pr, F1, MAE, and 
RMSE values of MSETL-AD for bias anomaly were 83.87 %, 3.28 %, 
91.90 %, 93.88 %, 88.59 %, 1.55935, and 3.27438, respectively, and for 
drift anomaly were 83.87 %, 1.48 %, 93.02 %, 97.14 %, 90.02 %, 
1.56028, and 3.28292, respectively. The experimental results demon­
strated that MSETL-AD exhibits significant advantages in prediction and 
anomaly detection performance compared to methods without model 
fine-tuning, transfer learning and source domain selection, single-source 
transfer methods, multi-source ensemble transfer baseline methods, and 
statistical threshold-based without residual smoothing methods.
Future research will further improve the performance of the pro­
posed method. Meanwhile, reducing computational costs is also a di­
rection for future research. In addition, the proposed method will be 
applied to more types of UAVs and provide a comprehensive analysis 
and assessment of the effect of noise on model performance in the future.
CRediT authorship contribution statement
Lei Yang: Writing – review & editing, Writing – original draft, 
Visualization, Validation, Software, Methodology, Investigation, Formal 
analysis, Data curation, Conceptualization. Shaobo Li: Supervision, 
Funding acquisition, Conceptualization. Caichao Zhu: Supervision, 
Conceptualization. Jian Liu: Writing – review & editing, Methodology, 
Data curation. Ansi Zhang: Writing – review & editing, Methodology.
Declaration of competing interest
The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper.
Acknowledgments
The authors would like to thank the National Natural Science 
Foundation of China (52275480) and the National Natural Science 
Foundation of China (52365061) for providing support for this paper. 
Especially, thanks for the computing support of the State Key Laboratory 
of Public Big Data, Guizhou University.
Appendix A. Supplementary data
Supplementary data to this article can be found online at https://doi. 
org/10.1016/j.aei.2025.103255.
Data availability
Data will be made available on request.
References
[1] A. Altan, Performance of metaheuristic optimization algorithms based on swarm 
intelligence in attitude and altitude control of unmanned aerial vehicle for path 
following, IEEE, 2020, pp. 1–6.
Table 10 
Anomaly detection results of MST-WRS.
Anomaly 
type
t 
value
TPR
FPR
ACC
Pr
F1
Bias 
anomaly
1
67.93 %
7.56 %
83.25 %
84.35 %
75.26 %
2
85.33 %
22.93 %
80.17 %
69.08 %
76.35 %
3
91.93 %
48.42 %
66.72 %
53.26 %
67.45 %
Drift 
anomaly
1
68.13 %
6.04 %
84.27 %
87.13 %
76.47 %
2
85.27 %
16.85 %
83.95 %
75.24 %
79.94 %
3
92.00 %
37.90 %
73.32 %
59.30 %
72.12 %
L. Yang et al.                                                                                                                                                                                                                                    
Advanced Engineering Informatics 65 (2025) 103255 
19

## Page 20

[2] Y. Ji, K. Song, H. Wen, X. Xue, Y. Yan, Q. Meng, UAV applications in intelligent 
traffic: RGBT image feature registration and complementary perception, Adv. Eng. 
Inform. 63 (2025) 102953.
[3] J. Su, X. Zhu, S. Li, W.-H. Chen, AI meets UAVs: A survey on AI empowered UAV 
perception systems for precision agriculture, Neurocomputing 518 (2023) 
242–270.
[4] ˙I. Ya˘g, A. Altan, Artificial intelligence-based robust hybrid algorithm design and 
implementation for real-time detection of plant diseases in agricultural 
environments, Biology 11 (2022) 1732.
[5] Z. Yang, X. Yu, S. Dedman, M. Rosso, J. Zhu, J. Yang, Y. Xia, Y. Tian, G. Zhang, 
J. Wang, UAV remote sensing applications in marine monitoring: Knowledge 
visualization and review, Sci. Total Environ. 838 (2022) 155939.
[6] X. Sun, Y. Hu, Y. Qin, Y. Zhang, Risk assessment of unmanned aerial vehicle 
accidents based on data-driven Bayesian networks, Reliab. Eng. Syst. Saf. 248 
(2024) 110185.
[7] H. Li, Q. Sun, Y. Zhong, Z. Huang, Y. Zhang, A soft resource optimization method 
for improving the resilience of UAV swarms under continuous attack, Reliab. Eng. 
Syst. Saf. 237 (2023) 109368.
[8] Y. Zhang, S. Li, A. Zhang, X. An, FW-UAV fault diagnosis based on knowledge 
complementary network under small sample, Mech. Syst. Signal Process. 215 
(2024) 111418.
[9] L. Yang, S. Li, C. Li, A. Zhang, X. Zhang, A survey of unmanned aerial vehicle flight 
data anomaly detection: technologies, applications, and future directions, Sci. 
China Technol. Sci. (2023) 1–19, https://doi.org/10.1007/s11431-022-2213-8.
[10] H. Ahn, S. Chung, Deep learning-based anomaly detection for individual drone 
vehicles performing swarm missions, Expert Syst. Appl. (2023) 122869.
[11] J. Yang, D. Tang, J. Yu, J. Zhang, H. Liu, Explaining anomalous events in flight data 
of UAV with deep attention-based multi-instance learning, IEEE Trans. Veh. 
Technol. (2023).
[12] H. Deng, Y. Lu, T. Yang, Z. Liu, J. Chen, Unmanned Aerial Vehicles anomaly 
detection model based on sensor information fusion and hybrid multimodal neural 
network, Eng. Appl. Artif. Intell. 132 (2024) 107961.
[13] Y. Lu, T. Yang, C. Zhao, W. Chen, R. Zeng, A swarm anomaly detection model for 
IoT UAVs based on a multi-modal denoising autoencoder and federated learning, 
Comput. Ind. Eng. 196 (2024) 110454.
[14] L. Yang, S. Li, Y. Zhang, C. Zhu, Z. Liao, Deep learning-assisted unmanned aerial 
vehicle flight data anomaly detection: a review, IEEE Sens. J. (2024).
[15] P. Wang, H. Tao, J. Qi, P. Li, Machining quality prediction of complex thin-walled 
parts using multi-task dual domain adaptive deep transfer learning, Adv. Eng. 
Inform. 62 (2024) 102640.
[16] Z. Yan, Z. Xu, Y. Zhang, J. Sun, L. Liu, Y. Sun, FTSDC: A novel federated transfer 
learning strategy for bearing cross-machine fault diagnosis based on dual- 
correction training, Adv. Eng. Inform. 61 (2024) 102499.
[17] J. Lee, J. Heo, J. Lee, Enhancement of virtual data quality using pre-trained 
Bayesian transfer learning under inaccurate and insufficient measurement data, 
Adv. Eng. Inform. 59 (2024) 102241.
[18] M. Huang, J. Yin, S. Yan, P. Xue, A fault diagnosis method of bearings based on 
deep transfer learning, Simul. Model. Pract. Theory 122 (2023) 102659.
[19] A. Alos, Z. Dahrouj, Detecting contextual faults in unmanned aerial vehicles using 
dynamic linear regression and k-nearest neighbour classifier, Gyroscopy Navig. 11 
(2020) 94–104.
[20] B. Wang, Y. Chen, D. Liu, X. Peng, An embedded intelligent system for on-line 
anomaly detection of unmanned aerial vehicle, J. Intell. Fuzzy Syst. 34 (2018) 
3535–3545.
[21] A. Alos, Z. Dahrouj, Decision tree matrix algorithm for detecting contextual faults 
in unmanned aerial vehicles, J. Intell. Fuzzy Syst. 38 (2020) 4929–4939.
[22] L. Liu, M. Liu, Q. Guo, D. Liu, Y. Peng, MEMS Sensor data anomaly detection for the 
UAV flight control subsystem, in: IEEE Sens., IEEE, 2018, pp. 1–4.
[23] L. Yang, S. Li, C. Li, C. Zhu, A. Zhang, G. Liang, Data-driven unsupervised anomaly 
detection and recovery of unmanned aerial vehicle flight data based on 
spatiotemporal correlation, Sci. China Technol. Sci. (2023) 1–13.
[24] G. Jiang, P. Nan, J. Zhang, Y. Li, X. Li, Robust spatio-temporal autoencoder for 
unsupervised anomaly detection of unmanned aerial vehicle with flight data, IEEE 
Trans. Instrum. Meas. (2024).
[25] Y. Wang, S. Li, L. Yang, Y. Zhang, C. Li, A. Zhang, X. An, Deeply integrated 
autoencoder-based anomaly detection and critical parameter identification for 
unmanned aerial vehicle actuators, IEEE Sens. J. (2024).
[26] V. Sadhu, K. Anjum, D. Pompili, On-board deep-learning-based unmanned aerial 
vehicle fault cause detection and classification via fpgas, IEEE Trans. Robot. 
(2023).
[27] C. Li, K. Luo, L. Yang, S. Li, H. Wang, X. Zhang, Z. Liao, A zero-shot fault detection 
method for UAV sensors based on a novel CVAE-GAN model, IEEE Sens. J. (2024).
[28] J. Zhong, Y. Zhang, J. Wang, C. Luo, Q. Miao, Unmanned aerial vehicle flight data 
anomaly detection and recovery prediction based on spatio-temporal correlation, 
IEEE Trans. Reliab. 71 (2022) 457–468, https://doi.org/10.1109/ 
TR.2021.3134369.
[29] B. Wang, X. Peng, M. Jiang, D. Liu, Real-time fault detection for UAV based on 
model acceleration engine, IEEE Trans. Instrum. Meas. 69 (2020) 9505–9516.
[30] B. Wang, D. Liu, Y. Peng, X. Peng, Multivariate regression-based fault detection and 
recovery of UAV flight data, IEEE Trans. Instrum. Meas. 69 (2020) 3527–3537, 
https://doi.org/10.1109/TIM.2019.2935576.
[31] K. He, D. Yu, D. Wang, M. Chai, S. Lei, C. Zhou, Graph attention network-based 
fault detection for UAVs with multivariant time series flight data, IEEE Trans. 
Instrum. Meas. 71 (2022) 1–13.
[32] L. Yang, S. Li, C. Zhu, A. Zhang, Z. Liao, Spatio-temporal correlation-based multiple 
regression for anomaly detection and recovery of unmanned aerial vehicle flight 
data, Adv. Eng. Inform. 60 (2024) 102440, https://doi.org/10.1016/j. 
aei.2024.102440.
[33] D. Liu, N. Wang, K. Guo, B. Wang, Ensemble transfer learning based cross-domain 
UAV actuator fault detection, IEEE Sens. J. 23 (2023) 16363–16372, https://doi. 
org/10.1109/JSEN.2023.3280571.
[34] A. Alos, Z. Dahrouj, Using MLSTM and multioutput convolutional LSTM algorithms 
for detecting anomalous patterns in streamed data of unmanned aerial vehicles, 
IEEE Aerosp. Electron. Syst. Mag. 37 (2022) 6–15, https://doi.org/10.1109/ 
MAES.2021.3053108.
[35] S. Wang, Z. Liu, Z. Jia, Y. Tang, G. Zhi, X. Wang, Fault detection for uavs with 
spatial-temporal learning on multivariate flight data, IEEE Trans. Instrum. Meas. 
(2024).
[36] L. Yang, S. Li, C. Li, C. Zhu, Data-driven multivariate regression-based anomaly 
detection and recovery of unmanned aerial vehicle flight data, J. Comput. Des. 
Eng. 11 (2024) 176–193.
[37] H. Wu, J. Zhao, Fault detection and diagnosis based on transfer learning for 
multimode chemical processes, Comput. Chem. Eng. 135 (2020) 106731.
[38] W. Mao, G. Wang, L. Kou, X. Liang, Deep domain-adversarial anomaly detection 
with one-class transfer learning, IEEECAA J. Autom. Sin. 10 (2023) 524–546.
[39] Z. Chen, D. Zhou, E. Zio, T. Xia, E. Pan, Adaptive transfer learning for multimode 
process monitoring and unsupervised anomaly detection in steam turbines, Reliab. 
Eng. Syst. Saf. 234 (2023) 109162.
[40] Y.-P. Zhao, W. Cai, The perceptron algorithm with uneven margins based transfer 
learning for turbofan engine fault detection, Eng. Appl. Artif. Intell. 127 (2024) 
107249.
[41] F. Shang, F. Sun, J. Wen, An adaptive fault detection model based on variational 
auto-encoders and unsupervised transfer learning, Appl. Soft Comput. 157 (2024) 
111515.
[42] X. Li, H. Jiang, M. Xie, T. Wang, R. Wang, Z. Wu, A reinforcement ensemble deep 
transfer learning network for rolling bearing fault diagnosis with multi-source 
domains, Adv. Eng. Inform. 51 (2022) 101480.
[43] P. Zhang, D. Gao, D. Hong, Y. Lu, Z. Wang, Z. Liao, Intelligent tool wear monitoring 
based on multi-channel hybrid information and deep transfer learning, J. Manuf. 
Syst. 69 (2023) 31–47.
[44] X. Liu, Y. Li, L. Chen, G. Chen, B. Zhao, Multiple source partial knowledge transfer 
for manufacturing system modelling, Robot. Comput.-Integr. Manuf. 80 (2023) 
102468.
[45] B. Qiang, K. Shi, N. Liu, J. Ren, Y. Shi, Integrating physics-informed recurrent 
Gaussian process regression into instance transfer for predicting tool wear in 
milling process, J. Manuf. Syst. 68 (2023) 42–55.
[46] W. Li, Z. Chen, G. He, A novel weighted adversarial transfer network for partial 
domain fault diagnosis of machinery, IEEE Trans. Ind. Inform. 17 (2020) 
1753–1762.
[47] M. Miao, P. Yang, S. Yue, R. Zhou, J. Yu, Multi-source self-supervised domain 
adaptation network for VRLA battery anomaly detection of data center under non- 
ideal conditions, Energy 299 (2024) 131392.
[48] B. Yao, G. Ling, F. Liu, M.-F. Ge, Multi-source variational mode transfer learning for 
enhanced PM2. 5 concentration forecasting at data-limited monitoring stations, 
Expert Syst. Appl. 238 (2024) 121714.
[49] D. Song, Y. Cheng, A. Zhou, C. Lu, J. Chong, J. Ma, Remaining useful life prediction 
and cycle life test optimization for multiple-formula battery: a method based on 
multi-source transfer learning, Reliab. Eng. Syst. Saf. (2024) 110166.
[50] B. Qiang, K. Shi, J. Ren, Y. Shi, Multi-source online transfer learning based on 
hybrid physics-data model for cross-condition tool health monitoring, J. Manuf. 
Syst. 77 (2024) 1–17.
[51] C. Peng, Y. Tao, Z. Chen, Y. Zhang, X. Sun, Multi-source transfer learning guided 
ensemble LSTM for building multi-load forecasting, Expert Syst. Appl. 202 (2022) 
117194.
[52] K. Guo, N. Wang, D. Liu, X. Peng, Uncertainty-aware LSTM based dynamic flight 
fault detection for UAV actuator, IEEE Trans. Instrum. Meas. 72 (2023) 1–13, 
https://doi.org/10.1109/TIM.2022.3225040.
[53] S. Hochreiter, J. Schmidhuber, Long short-term memory, Neural Comput. 9 (1997) 
1735–1780, https://doi.org/10.1162/neco.1997.9.8.1735.
[54] C. Barıs¸, C. Yanarates¸, A. Altan, A robust chaos-inspired artificial intelligence 
model for dealing with nonlinear dynamics in wind speed forecasting, PeerJ 
Comput. Sci. 10 (2024) e2393.
[55] D. Bahdanau, K. Cho, Y. Bengio, Neural Machine Translation by Jointly Learning to 
Align and Translate, (2016). http://arxiv.org/abs/1409.0473.
[56] Y. Mao, X. Li, M. Duan, Y. Feng, J. Wang, H. Men, H. Yang, A novel mooring system 
anomaly detection framework for SEMI based on improved residual network with 
attention mechanism and feature fusion, Reliab. Eng. Syst. Saf. 245 (2024) 109970.
[57] F. Zhuang, Z. Qi, K. Duan, D. Xi, Y. Zhu, H. Zhu, H. Xiong, Q. He, A comprehensive 
survey on transfer learning, Proc. IEEE 109 (2020) 43–76.
[58] H. Chen, H. Liu, X. Chu, Q. Liu, D. Xue, Anomaly detection and critical SCADA 
parameters identification for wind turbines based on LSTM-AE neural network, 
Renew. Energy 172 (2021) 829–840.
[59] O. Grigg, D. Spiegelhalter, A simple risk-adjusted exponentially weighted moving 
average, J. Am. Stat. Assoc. 102 (2007) 140–152.
[60] A. Siffer, P.-A. Fouque, A. Termier, C. Largouet, Anomaly detection in streams with 
extreme value theory, in: Proc. 23rd ACM SIGKDD Int. Conf. Knowl. Discov. Data 
Min., 2017: pp. 1067–1075.
[61] K. Xiao, S. Tan, G. Wang, X. An, X. Wang, X. Wang, XTDrone: A customizable multi- 
rotor UAVs simulation platform, in: 2020 4th Int. Conf. Robot. Autom. Sci. ICRAS, 
2020: pp. 55–61. Doi: 10.1109/ICRAS49812.2020.9134922.
[62] B. Wang, X. Peng, D. Liu, Airborne sensor data-based unsupervised recursive 
identification for UAV flight phases, IEEE Sens. J. 20 (2020) 10733–10743.
L. Yang et al.                                                                                                                                                                                                                                    
Advanced Engineering Informatics 65 (2025) 103255 
20

## Page 21

[63] Q. Sun, B. Jiang, H. Zhu, J.G. Ibrahim, Hard thresholding regression, Scand. J. Stat. 
46 (2019) 314–328.
[64] T.O. Hodson, Root-mean-square error (RMSE) or mean absolute error (MAE): when 
to use them or not, Geosci. Model Dev. 15 (2022) 5481–5487.
[65] X. Miao, Y. Liu, H. Zhao, C. Li, Distributed online one-class support vector machine 
for anomaly detection over networks, IEEE Trans. Cybern. 49 (2018) 1475–1488.
[66] R. Yacouby, D. Axman, Probabilistic extension of precision, recall, and f1 score for 
more thorough evaluation of classification models, in: Proc. First Workshop Eval. 
Comp. NLP Syst., 2020: pp. 79–91.
L. Yang et al.                                                                                                                                                                                                                                    
Advanced Engineering Informatics 65 (2025) 103255 
21
