# Multi-Source Data Fusion-Based Knowledge Transfer for Unmanned Aerial Vehicle Flight Data Anomaly Detection and Recovery.pdf

## Page 1

Multi-source data fusion-based 
knowledge transfer for unmanned 
aerial vehicle flight data anomaly 
detection and recovery
Lei Yang1, Shaobo Li2, Liya Yu1, Caichao Zhu3 & Congbao Wang1
Flight data anomaly detection (AD) is essential for unmanned aerial vehicle (UAV) health management. 
Despite the current dominance of data-driven approaches, their effectiveness often requires sufficient 
data for model training. However, in practice, it is inevitable to face the situation of limited data, such 
as the high cost of data acquisition and the difficulty of collecting data in special scenarios, resulting 
in the performance degradation of the traditional data-driven methods with limited samples. This 
paper proposes an innovative data-driven approach leveraging transfer learning to detect and recover 
abnormal UAV flight data with limited samples through multi-source data fusion. First, a data-driven 
framework based on one-dimensional convolutional neural network and bi-directional long short-term 
memory (1D CNN-BiLSTM) with parameter selection and residual smoothing (1DCB-PSRS) is proposed. 
It employs the designed 1D CNN-BiLSTM prediction model for fully extracting spatiotemporal 
features of flight data, the maximum information coefficient (MIC) for parameter selection, and the 
exponentially weighted moving average (EWMA) for residual smoothing, thereby improving the AD 
and recovery performance. Second, multiple source domains with sufficient data are fused to pre-train 
the model to gain initialized parameters for the target domain. Then, the model is fine-tuned using 
limited training samples in the target domain through model-based transfer learning method and is 
evaluated using test data of the target domain. Finally, the effectiveness of the proposed method is 
verified on real UAV flight data.
Keywords  Unmanned aerial vehicle (UAV), Anomaly detection (AD), Data recovery, Transfer learning, 
Multi-source data fusion
In recent years, the widespread application of unmanned aerial vehicles (UAVs) in fields such as the internet 
of things1,2, emergency monitoring3, and precision agriculture4 has propelled the rapid expansion of the UAV 
market5–7. However, as the UAV market continues to flourish, there is a growing demand for enhanced safety 
and reliability of UAVs. Compared with manned aircraft, UAVs have a higher accident rate due to factors such 
as strong autonomy, complex flight environments, and greater susceptibility to external disturbances, which 
results in significant economic losses for relevant countries and companies8. Thus, ensuring the flight safety 
and reliability of UAVs have become a crucial topic9. Flight data reflects the operational status of the UAV and 
the health status of each key component, providing an important basis for UAV health management operation 
and maintenance. By monitoring and analyzing flight data, potential faults or anomalies can be detected, and 
necessary preventive measures can be taken to reduce flight risks. Therefore, conducting research on flight data 
anomaly detection (AD) and recovery plays a crucial role in improving the safety and reliability of UAVs.
In recent years, many studies have been conducted on UAV flight data AD, including knowledge- and 
model-based, and data-driven approaches8. Knowledge- and model-based approaches rely on expert knowledge 
or accurate mathematical models to detect anomalies in flight data10–13. However, due to the complexity of 
UAV structures14,15, it is very difficult to obtain rich expert knowledge or build accurate mathematical models, 
making these methods limited in practical applications. In contrast, data-driven methods can effectively 
learn and detect anomalies from extensive UAV flight data without the need for expert knowledge or precise 
mathematical models and have received much attention and research. For example, He et al.16 proposed a 
1School of Mechanical Engineering, Guizhou University, Guiyang 550025, China. 2School of Mechanical Engineering, 
Guizhou Lnstitute of Technology, Guiyang 550025, China. 3State Key Laboratory of Mechanical Transmission, 
Chongqing University, Chongqing 400044, China. email: lishaobo@gzu.edu.cn
OPEN
Scientific Reports |        (2025) 15:20924 
1
| https://doi.org/10.1038/s41598-025-05322-4
www.nature.com/scientificreports

## Page 2

structured sparse subspace learning (SSL) AD (SSLAD) algorithm to detect and identify anomalous UAV flight 
data. Furthermore, they developed an online method based on subspace tracking to realized high-accuracy 
UAV AD and recovery performance17. Zhong et al.18 presented a spatiotemporal correlation based on long 
short-term memory (STC-LSTM) method that effectively identified anomalies in UAV roll angle. Guo et al.19 
proposed an approach based on uncertainty-aware LSTM (UA-LSTM) for UAV actuator fault detection. Wang 
et al.20 designed a data-driven UAV fault detection method using stacked LSTM. He et al.21 used an improved 
graph attention network (GAT) method for UAV fault detection. Park et al.22 proposed an unsupervised fault 
detection model based on a stacked auto-encoder (AE), which was trained using normal UAV flight data and 
differentiated between safe and abnormal states based on reconstruction errors. Yang et al.23 designed a model 
based on AE and LSTM and was verified on real flight data. Bae et al.24 used an model based on AE and LSTM to 
detect abnormal flight parameters. Bell et al.25 proposed an LSTM-based deep learning autoencoder combined 
with a dynamic thresholding algorithm for detecting abnormal flight data. Wang et al.26 used an LSTM model 
with residual filtering (LSTM-RF) to detect bias and drift anomalies of UAV flight data. Yang et al.27,28 used 
multivariate regression analysis to detect anomalies in real flight data and achieved good detection performance. 
Lu et al.29 proposed a novel multirate-aware LSTM data-driven approach for AD of UAV flight data. Wang et 
al.30 proposed a deeply integrated AE-based AD method to detect UAV flight data injected with anomalies. 
Jiang et al.31 introduced a robust spatialtemporal AE model and validated its effectiveness on real flight data. 
Despite some progress in existing data-driven approaches, their effectiveness often relies on the availability of 
sufficient data for model training. However, obtaining sufficient data for model training is not always feasible. 
For example, during the test flight of UAVs, data samples are limited because only specific flight phases or key 
performance indicators are tested, rather than conducting long-duration flights. In addition, formulating new 
flight plans to acquire sufficient flight data may also require expensive flight costs. This may make it difficult for 
existing methods to capture complex and diverse anomaly patterns from limited samples, resulting in lower AD 
accuracy. Therefore, enhancing flight data AD performance with limited UAV samples is still a major challenge 
and problem at present.
Transfer learning is an effective solution that significantly improves the performance of target domain tasks 
by transferring the knowledge learned from a source domain with abundant data to a target domain with limited 
data32. The benefits of transfer learning have been widely demonstrated in time series prediction33 and fault 
diagnosis34,35. For example, Zhang et al.33 used a bi-directional long short-term memory (BiLSTM) recurrent 
neural network-based transfer learning for remaining useful life (RUL) estimation. Lu et al.36 proposed a model-
based transfer learning approach to model the target prediction task using knowledge acquired from the source 
task, enabling heat load prediction. Tariq et al.37 developed a residual neural network-based transfer learning 
method for predicting subway platform PM2.5 health risk level sequences. Li et al.35 utilized a priori knowledge 
from multiple fault classification tasks with known operating conditions to achieve bearing fault diagnosis with 
unknown operating conditions. Zhang et al.38 used a decentralized joint transfer learning approach aided by 
blockchain technology for collaborative mechanical fault diagnosis. These studies provide valuable experience 
and insights for UAV flight data AD with limited samples. However, the performance of these methods often 
relies on single source domain information, which limits their applicability in a wider range of scenarios. This 
is because data from a single source domain may lack sufficient representative features, especially when there 
is a significant distribution difference between the source and target domains, making it difficult to obtain 
desirable results. Multi-source data fusion-based transfer learning methods serve as an effective extension and 
supplement. By integrating information from multiple source domains, they reduce over-reliance on data from 
any single source domain, thereby enhancing model performance39. However, in the field of UAV flight data AD, 
research on transfer learning methods based on multi-source data fusion is still limited.
To address the above challenges and inspired by transfer learning, a data-driven knowledge transfer 
approach based on multi-source data fusion is proposed in this paper for detecting and recovering abnormal 
UAV flight data. First, to reduce the negative impact of irrelevant flight parameters on the model, a correlation 
analysis method based on maximum information coefficient (MIC) is adopted to select flight parameters with 
correlation as model inputs. Second, combining the advantages of one-dimensional convolutional (1D CNN) 
in local feature extraction and BiLSTM in capturing long-term dependencies, a prediction model based on 1D 
CNN-BiLSTM is designed to fully extract the spatiotemporal features of flight data and obtain the predicted 
values of the monitored parameter. Third, multiple source domains with sufficient data are fused for pre-training 
the model, and the limited training samples and test data of the target domain are used to fine-tune and evaluate 
the model. Finally, the exponentially weighted moving average (EWMA) is further introduced to smooth the 
residuals, thus reducing the interference of random noise and improving the AD performance. Specifically, the 
main contributions of this paper are described as follows:
	1.	 A data-driven framework based on 1D CNN-BiLSTM with parameter selection and residual smoothing 
(1DCB-PSRS) is proposed. It inherits the strengths of 1D CNN and BiLSTM in extracting local features and 
capturing long-term dependencies, utilizes MIC to select relevant flight parameters as model inputs, and 
employs EWMA to smooth residuals, thereby fully extracting the spatiotemporal features of flight data and 
reducing the interference of irrelevant flight parameters and random noise on the model performance.
	2.	 A knowledge transfer method based on multi-source data fusion is proposed for UAV flight data AD and 
recovery with limited samples. It leverages data distribution information from multiple source domains and 
performs knowledge transfer through sharing the model parameters to avoid reliance a single source domain 
data and improve the AD and recovery performance in the target domain with limited samples.
	3.	 Taking complex high-dimensional real UAV flight data as the experimental object, the effectiveness of 
1DCB-PSRS as the pre-training framework and the knowledge transfer method based on multi-source data 
fusion is verified.
Scientific Reports |        (2025) 15:20924 
2
| https://doi.org/10.1038/s41598-025-05322-4
www.nature.com/scientificreports/

## Page 3

The rest of this paper are structured as follows. Section "Preliminaries" introduces the fundamental theory. 
Section "Methodology framework" outlines the proposed methodology framework. Section "Experiments" 
presents the experimental results and analysis. Section "Conclusion and prospects" summarizes this work and 
gives the future research directions.
Preliminaries
One-dimensional convolutional neural network
One-dimensional convolutional neural network (1D CNN) is easy to train and implement and has been widely 
used for time-series data processing and analysis40–42. The structure of 1D CNN is depicted in Fig.  1. The 
convolution layer is used to capture the local features of the input signal43, which is defined as follows:
	
Zl
j = σ
(Nl−1
∑
i=1
Conv 1D (
W l
i,j, xl−1
i
)
+ bl
j
)

(1)
where Zl
j is the jth attribute mapping of the jth layer. xl−1
i
 and Nl−1 are the ith attribute mapping and the number 
of attribute mappings of l-1th layer, respectively. Conv1D (•) denotes the convolution operation. W l−1
i,j  is the 
convolution kernel. bl
j is the bias. σ(•) is the activation function. Then, Zl
j is input into the pooling layer. 
Commonly used maximum and average pooling operations44 are defined as follows:
	
Zl+1
j
= Maxpooling(Zl
j)
(2)
	
Zl+1
j
= Averpooling(Zl
j)
(3)
where Zl+1
j
 denotes the jth attribute mapping of the l + 1th layer. Maxpooling (•) and Averpooling (•) denote 
maximum and average pooling operations, respectively. Finally, feature integration is performed through the 
fully connected layer, which is defined as follows:
	
Zl = f(Wfullxl−1 + bfull)
(4)
where Wfull is the weights, bfull is the bias, Zl is the output, and f (•) is the nonlinear activation function.
Bi-directional long short-term memory
Bi-directional long short-term memory (BiLSTM) overcomes the unidirectional information flow limitation of 
traditional LSTM45, thereby reducing the loss of crucial contextual information, as shown in Fig. 2. By processing 
the input sequences in forward and backward directions, BiLSTM obtains hidden state representations in 
these two directions. This bi-directional information flow allows BiLSTM to synthesize the information from 
the input sequences to better learn the feature representation of these sequences. Therefore, BiLSTM shows 
significant advantages in complex sequence modeling tasks, such as question-answering systems46, named entity 
recognition47, and text classification48.
Each LSTM unit of the BiLSTM network contains input (it), forget (ft), and output (ot) gates and a memory 
cell. At time step t, the two update processes of the LSTM unit, i.e., forward and backward propagation, are 
defined as follows:
	
−→
f t = σ(−→
W hf
−→
h t−1 + −→
W xf⃗xt + −→b f)
(5)
	
−→i t = σ(−→
W hi
−→
h t−1 + −→
W xi⃗xt + −→b i)
(6)
	
⃗ct = −→
f t ⊙⃗ct−1 + −→i t ⊙tanh(−→
W hc
−→
h t−1 + −→
W xc⃗xt + −→b c)
(7)
	
⃗ot = −→
W ho
−→
h t−1 + −→
W xo⃗xt + −→b o
(8)
Fig. 1.  Structure of 1D CNN.
 
Scientific Reports |        (2025) 15:20924 
3
| https://doi.org/10.1038/s41598-025-05322-4
www.nature.com/scientificreports/

## Page 4

−→
h t = ⃗ot ⊙tanh(⃗ct)
(9)
	
←−
f t = σ(←−
W hf
←−
h t−1 + ←−
W xf⃗xt + ←−b f)
(10)
	
←−i t = σ(←−
W hi
←−
h t−1 + ←−
W xi⃗xt + ←−b i)
(11)
	
←c
t = ←−
f t ⊙
←c
t−1 +←−I t ⊙tanh(←−
W hc
←−
h t−1 + ←−
W xc
←x
t +←−b c)
(12)
	
←o
t = ←−
W ho
←−
h t−1 + ←−
W xo
←x
t +←−b o
(13)
	
←−
h t =
←o
t ⊙tanh(
←c
t )
(14)
where → and ← denote forward and backward propagation, respectively. Whf, Whi, Whc, Who, Wxf, Wxi, 
Wxc, and Wxo are the weights in the model update process. bf, bi, bc, and bo are the biases in the model update 
process. ⨀ denotes the product. σ is the activation function. ct is the memory cell. After forward and backward 
propagation, the final output ht is defined as follows:
	
ht = −→
h t ⊙←−
h t
(15)
Transfer learning
Transfer learning aims to utilize knowledge acquired from one specific task (known as the source task) and 
apply it to another related task (known as the target task)49. Transfer learning includes domain D and task T. The 
domain D is the learning body that contains X = {x1, x2, . . . , xn} and P(X), where X = {x1, x2, . . . , xn} 
is the feature space and P(X) is the the marginal probability distribution. Similarly, for the task T that contains 
the label space li and the conditional probability distribution P(Y |X), where Y = {y1, y2, . . . , yn}. When 
solving practical problems, there usually includes the source domain Ds = {Xs, P(Xs)}, the source task 
Ts = {Ys, P(Ys|Xs)}, the target domain Dt = {Xt, P(Xt)}, and the target task Tt = {Yt, P(Yt|Xt)} of 
transfer learning, as shown in Fig. 3. Ds contains sufficient data and can train the model well while Dt is the 
opposite. In the process of transfer, the knowledge is represented by P(Ys|Xs) of the source task or fs(.)36, where 
P(Ys|Xs) is the conditional probability distribution and fs(.) is the prediction function.
Fig. 3.  The general process of transfer learning.
 
Fig. 2.  Structure of BiLSTM.
 
Scientific Reports |        (2025) 15:20924 
4
| https://doi.org/10.1038/s41598-025-05322-4
www.nature.com/scientificreports/

## Page 5

Methodology framework
Figure 4 illustrates the proposed methodology framework in this paper. First, the MIC is utilized to select 
relevant flight parameters as model inputs. Second, the raw multiple UAV flight datasets are normalized. Third, 
the processed UAV flight datasets are divided into multiple source domains and one target domain. Each source 
domain has sufficient data and can train the model well, while the target domain is the opposite. Fourth, these 
source domains are fused into a new source domain to pre-train the 1D CNN-BiLSTM model to obtain initialized 
parameters for the target domain, and the limited training samples and test data of the target domain are used 
to fine-tune and test the 1D CNN-BiLSTM model. Then, the training and test residuals are calculated based on 
the model’s predicted values and the original values. Next, the EWMA is applied to smooth the training and 
test residuals, and the threshold is calculated based on the smoothed training residuals. Finally, AD is achieved 
by comparing the smoothed test residuals with the threshold, and data recovery is realized by replacing the 
anomalous data with the model’s predicted values.
Data preprocessing
The normalization method50 shown in Eq. (16) is used to normalize the raw flight data xraw to eliminate 
magnitude differences.
	
xnorm = xraw −xraw
min
xraw
max −xraw
min

(16)
where xnorm is the normalized data. xraw
max is the maximum value and xraw
min is the minimum value of xraw, 
respectively.
Structure of 1D CNN-BiLSTM model
Many existing studies mainly use LSTM for modeling and feature extraction of UAV flight data18–20,26. This 
may result in problems such as inadequate feature extraction and insufficient flight data modeling capability. 
This is because LSTM focuses mainly on the extraction of time series features and ignores critical local features. 
To solve these problems, the prediction 1D CNN-BiLSTM model constructed based on 1D CNN and BiLSTM 
can better consider temporal and local features, which includes Conv1D, Max pooling, BiLSTM, Dense, and 
Dropout layers, as depicted in Fig. 5, with input and output sizes as shown in Table 1.
Fig. 4.  The proposed methodology framework for UAV flight data AD and recovery in this paper.
 
Scientific Reports |        (2025) 15:20924 
5
| https://doi.org/10.1038/s41598-025-05322-4
www.nature.com/scientificreports/

## Page 6

Model-based transfer learning method
Transfer learning includes instance-, feature-, relationship-, and model-based (parameter-based) transfer 
learning32. Instance-based transfer learning involves reusing data samples to facilitate knowledge transfer. 
Feature-based transfer learning facilitates knowledge transfer by transforming data features from source 
and target domains into a common feature space. Relation-based transfer learning leverages inter-domain 
relationships to facilitate knowledge transfer from the source domain to the target domain. Model-based transfer 
learning entails transferring a pre-trained model from the source domain to the target domain. Considering 
aspects such as data volume and task complexity, this paper chooses the model-based transfer learning method. 
The structure of transfer learning is shown in Fig. 6.
As mentioned earlier, there is sufficient data in the source domain to adequately train the model. However, 
the data in the target domain is limited and training the model directly on the target domain usually does 
not achieve the desired results. In addition, if the trained model in the source domain is directly applied to 
the target domain, the performance of the model may be degraded. For this purpose, a full-layer fine-tuning 
strategy is used. The modeling effect is enhanced by adjusting the model parameter to adapt as much as possible 
to the target domain requirement. However, when fine-tuning all parameters, the small amount of data in the 
target domain may lead to model overfitting. Therefore, to mitigate this problem, the Dropout technology is 
introduced into the designed network to reduce the model overfitting risk. The parameter passing relationship 
between the source and target tasks can be defined as follows:
	
θt = θs
(17)
where θt is the weight of the source model and θs is the weight of the target model. During the fine-tuning 
process, the updated model parameter is defined as follows:
	
θ∗
s = arg min
θs L(θs)
(18)
where θ∗
s is the optimized parameter of the model that minimizes the loss function L(θs).
Model training
For the regression model, the mean square error (MSE), which is the average of the squared difference between 
the predicted and true values, is used as the loss function for the model training in this paper. Assuming that 
at time t, the predicted output of the model is y(t) and the true value is y(t), the loss function L(θs) can be 
calculated by Eq. (19).
	
L(θs) = 1
l
∑l
i=1 (ˆyi −yi)2
(19)
Layer
Input size
Output size
Conv1D layer
(None, W, n)
(None, W, 32)
Max pooling layer
(None, W, 32)
(None, 1, 32)
Dropout layer
(None, 1, 32)
(None, 1, 32)
BiLSTM layer
(None, 1, 32)
(None, 1, 64)
Dropout layer
(None, 1, 64)
(None, 1, 64)
Fully connected layer
(None, 1, 64)
(None, 1, 1)
Table 1.  Input and output sizes of each layer.
 
Fig. 5.  Structure of the designed 1D CNN-BiLSTM.
 
Scientific Reports |        (2025) 15:20924 
6
| https://doi.org/10.1038/s41598-025-05322-4
www.nature.com/scientificreports/

## Page 7

where yi and yi are the ith elements of y(t) and y(t), respectively, and l is the sample length.
AD and recovery
In the pre-training model stage, assuming that e(t)train are the training residuals, which can be calculated by 
Eq. (20).
	
e(t)train = ˆy(t)train −y(t)train
(20)
where y(t)train and y(t)train are the predicted and true data of the training set, respectively. t is an index value. 
Since random noise makes the residuals fluctuate dramatically, the exponentially weighted moving average 
(EWMA)51 is introduced to smooth the residuals e(t)train, which can be defined as follows:
	
˜e(t)train = α˜e(t −1)train + (1 −α)e(t)train
(21)
where e(t)train and e(t)train are the smoothed and actual training residuals of the tth data point, respectively. α 
is an adjustable hyperparameter. Then, the mean value µtrain of  e(t)train can be calculated by Eq. (22).
	
µtrain = 1
l
l
∑
t=1
˜e(t)train
(22)
where l is the training data length. Based on Eqs. (21)–(22), the standard deviation of e(t)train can be calculated 
by Eq. (23).
	
σtrain =




1
l −1
l

t=1
(˜e(t)train −µtrian)2
(23)
Based on Eqs. (22) and (23), the anomaly determination threshold can be calculated by Eq. (24).
	
T = µtrain + ℓσtrain
(24)
where ℓ is a constant, which is set to 1 in this paper. For the test set, the smoothed test residuals e(t)test are also 
obtained based on Eq. (21). Then, AD can be calculated by Eq. (25).
	
AD =
{˜e(t)λ
test > T, abnormal
˜e(t)λ
test ≤T, normal

(25)
Fig. 6.  Structure of transfer learning.
 
Scientific Reports |        (2025) 15:20924 
7
| https://doi.org/10.1038/s41598-025-05322-4
www.nature.com/scientificreports/

## Page 8

where e(t)λ
test is the λth smoothed test residual. If e(t)λ
test is greater than T, it is recognized as abnormal and vice 
versa. For data recovery, it can be defined as follows:
	
ˆy(t)test = f1D CNN - BiLSTM(x(t)test)
(26)
where y(t)test is the predicted data for the test set x(t)test. f1DCNN−BiLST M(•) is the mapping function.
Experiments
Data description
This study uses UAV flight datasets without anomalies that are publicly available from the University of 
Minnesota52–54. These datasets include the Thor-type UAV flight data with different flight times and scenarios. 
Table 2 shows the information related to the datasets used in this paper in detail, including dataset name, 
flight number, raw parameter length, raw parameter number, experiment range, experiment length, sampling 
frequency, and domain type. It should be noted that the source domains Flight97 and Flight104 are fused to a new 
source domain, denoted as Flight97-104 dataset, and the specific fusion strategy will be described subsequently.
Given the high cost and extreme difficulty of obtaining real abnormal UAV flight data is extremely difficult, 
an anomaly injection method is used to generate anomalous data. This is in line with most research practices 
in the field at this stage18,21,26–28. The anomaly injection method can simulate many anomaly types and prevent 
accidents from occurring in UAVs caused by collecting abnormal data. In this paper, bias and drift anomalies are 
injected into real UAV flight data as shown in Eqs. (27)–(28), respectively, to validate the model performance. 
Specifically, bias or drift anomalies in UAV flight data mainly result from fixed or dynamic factors, leading to 
continuous or gradual deviations from the expected values.
	
y(t)bias = y(t) + ξ
(27)
	
y(t)drift = y(t) + ϑ(t)
(28)
where y(t) is the raw data and ξ is the deviation constant. ϑ(t) is a function of t.
NAV north velocity (navvn) is critical to the navigation precision and stability of UAVs, and it is selected 
as the detection parameter in this paper. In fact, ξ and ϑ(t) are not accurately known when the UAV suffers 
from bias or drift anomalies. Therefore, in this paper, the values of ξ are injected into the flight97, flight98, and 
flight104 datasets with values of 5, 3, and 5, respectively, to simulate bias anomaly, and the values of ϑ(t) are 
uniformly taken in the range of [3–6], and [5,6], respectively, to simulate drift anomaly. Specifically, anomalies 
are injected into the last 1000 data points of the Flight97, Flight98, and Flight104 datasets, with anomaly rates 
of 0.0741, 0.0625, and 0.0714, respectively. Figure 7 illustrates the parameter navvn after injection of bias and 
drift anomalies, with the blue curves representing normal data and the red curves representing abnormal data.
Since many irrelevant flight parameters could influence the model’s performance, selecting mission-relevant 
flight parameters for experiments before model training is necessary. Therefore, the maximal information 
coefficient (MIC)55 is employed to select correlation parameters for model inputs, effectively avoiding the crucial 
information loss of nonlinear correlation parameters. The related calculation process of MIC is shown in Eqs. 
(29) and (30).
	
MI(ℏ, ψ) =
∑
ℏ,ψ
P(ℏ, ψ) log2
P(ℏ, ψ)
P(ℏ)P(ψ)
(29)
	
MIC(ℏ, ψ) =
max
ℏψ<B(n)
MI(ℏ, ψ)
log2(min{|ℏ|, |ψ|})
(30)
where MI(ℏ,ψ) and P(ℏ,ψ), and P(ℏ) and P(ψ) are the mutual information and joint probability density, and 
the boundary probability densities of ℏ and ψ, respectively. Table 3 lists the 15 flight parameters with strong 
correlation with navvn according to the MIC correlation analysis results. The correlation determination 
threshold is taken as 0.6.
Experimental setup
The experimental datasets are divided into training and testing sets in an 8:2 ratio. The Flight97-104 dataset 
contains the training set of the Flight97 dataset and the entire Flight104 dataset. The experimental setup includes 
a Windows 10 (64-bit) operating system, an AMD Ryzen 5 3600 6-Core @3.6 GHz processor, and TensorFlow 
2.12.0. In particular, the optimal hyperparameter selection is determined using a grid search method during the 
Dataset name
Flight number
Raw parameter length
Raw parameter number
Experiment range
Experiment length
Sampling frequency
Domain type
Flight9752
97th
14,794
84
[1, 13491]
13,490
50HZ
Source domain
Flight9853
98th
21,015
84
[3501, 19501]
16,000
50HZ
Target domain
Flight10454
104th
25,836
84
[7001, 21001]
14,000
50HZ
Source domain
Table 2.  Description of the experimental datasets in this paper.
 
Scientific Reports |        (2025) 15:20924 
8
| https://doi.org/10.1038/s41598-025-05322-4
www.nature.com/scientificreports/

## Page 9

pre-training stage. The search ranges for the learning rate are set to [0.001, 0.0015, 0.002], for the dropout rate to 
[0.1, 0.2, 0.3], and for the batch size to [32, 64, 128]. The number of epochs is set to 100.
Evaluation metrics
This paper uses the true positive rate (TPR), false positive rate (FPR), and accuracy (ACC) rate as the evaluation 
metrics for AD, and the mean absolute error (MAE) and root mean square error (RMSE) as the evaluation 
metrics for data recovery, as shown in Eqs. (31)–(35)56,57, respectively.
	
TPR =
TP
TP + FN × 100%
(31)
	
FPR =
FP
TN + FP × 100%
(32)
	
ACC =
TP + TN
TP + TN + FP + FN × 100%
(33)
Name
Description
Unit
alt
GPS altitude (WGS84)
m
p_bias
Gyro bias, X-axis (roll)
rad/s
q_bias
Gyro bias, Y-axis (pitch)
rad/s
r_bias
Gyro bias, Z-axis (yaw)
rad/s
hx
X-axis magnetic field
Gauss
lat
GPS latitude
deg
lon
GPS longitude
deg
ax_bias
Accelerometer bias, X-axis
rad/s
ay_bias
Accelerometer bias, Y-axis
rad/s
az_bias
Accelerometer bias, Z-axis
rad/s
psi
Euler roll angle
rad
GPS_TOW
Time of week from GPS
[sec]
vd
GPS down velocity
m/s
ve
GPS east velocity
m/s
vn
GPS north velocity
m/s
Table 3.  Flight parameters with correlation to Navvn.
 
Fig. 7.  Flight data after injecting bias and drift anomalies.
 
Scientific Reports |        (2025) 15:20924 
9
| https://doi.org/10.1038/s41598-025-05322-4
www.nature.com/scientificreports/

## Page 10

MAE = 1
L
L
∑
i=1
|yi −ˆyi|
(34)
	
RMSE =



 1
L
L

i=1
(yi −ˆyi)2
(35)
where TP and TN, and FP and FN are correctly identified normal and abnormal data, and incorrectly identified 
normal and abnormal data, respectively. L is the parameter length. yi and yi are the raw data without anomalies 
and the inverse normalized data at point i, respectively. The smaller values of FPR, MAE, and RMSE and the 
higher values of TPR and ACC indicate better model performance.
AD and recovery results
Performance of direct training with different domains
AD
	1.	  AD
	To verify the effectiveness of 1DCB-PSRS as the pre-trained framework, the regression models based on LSTM-
RF26, STC-LSTM18, 1D CNN, BiLSTM, temporal convolutional network (TCN), and support vector regres­
sion (SVR) are used for the baseline methods. Figure 8 shows the bias AD results of these methods on all da­
tasets. 1DCB-PSRS obtains the highest ACC values for different datasets. For the Flight97 Flight98, Flight104, 
and Flight97-104 datasets, 1DCB-PSRS achieves the ACC values of 95.74%, 96.47%, 97.46%, and 95.87% 
respectively. Meanwhile, 1DCB-PSRS reaches TPR values of 93.76%, 96.09%, 96.44%, and 94.90% for the 
Flight97, Flight98, Flight104, and Flight97-104 datasets, respectively. In addition to ACC and TPR values, 
1DCB-PSRS also exhibits relatively low FPR values, varying from 0.30% to 2.70% on different datasets. In 
contrast, BiLSTM and 1D CNN have higher FPR values in most datasets, which means these methods iden­
tify more abnormal samples as normal. For example, the FPR values of BiLSTM for all datasets are 11.00%, 
24.20%, 6.40%, and 29.30%, respectively. 1D CNN achieves FPR values of 43.50%, 21.40%, and 23.50% for the 
Flight97, Flight98, and Flight97-104 datasets, respectively. Similarly, STC-LSTM also has high false detection 
rates on different datasets. This may be due not only to the insufficient feature extraction of STC-LSTM, but 
also to a certain extent to the influence of random noise. In contrast, the performance of LSTM-RF on dif­
ferent datasets is improved by residual smoothing compared STC-LSTM. However, this improvement is still 
relatively limited. For example, for the Flight98 dataset, LSTM-RF achieves an FPR value of 19.60%. The AD 
performance of TCN is relatively poor across different datasets. Specifically, for the Flight97 dataset, the TPR 
and ACC values of TCN are 76.27% and 84.36%, respectively; for the Flight98 dataset, the FPR value of TCN 
is as high as 21.10%; and for the Flight97-104 dataset, the FPR value of TCN reaches 31.20%. For different 
datasets, although SVR can correctly detect most or all abnormal samples, its overall performance is still low­
er than 1DCB-PSRS in terms of TPR and ACC values. Specifically, for different datasets, the TPR and ACC 
values of SVR are both below 87.00% and 91.00%, respectively.
	Figure 9 illustrates the drift AD results of the above methods on all datasets. The overall performance of 1DCB-
PSRS is still superior to baseline methods. For different datasets, the ACC, TPR, and FPR values of 1DCB-
PSRS vary from 94.11% to 98.68%, 91.35% to 97.94%, and 0.00% to 2.00%, respectively. The TPR values of 
BiLSTM for the Flight97 and Flight98 datasets are 92.35% and 100%, respectively, STC-LSTM for the Flight97 
dataset is 96.59%, 1D CNN for the Flight97-104 dataset is 99.29%, and TCN for the Flight97-104 dataset is 
Fig. 8.  The bias AD results of 1DCB-PSRS, 1D CNN, BiLSTM, LSTM-RF, STC-LSTM, TCN, and SVR.
 
Scientific Reports |        (2025) 15:20924 
10
| https://doi.org/10.1038/s41598-025-05322-4
www.nature.com/scientificreports/

## Page 11

96.29%, which are better than that of 1DCB-PSRS. The FPR values of SVR for the Flight98 and Flight97-104 
dataset are all 0.00%, which are also better than that of 1DCB-PSRS. However, these methods fail to strike a 
better balance between accuracy and false detection rate. In contrast, 1DCB-PSRS demonstrates more robust­
ness on different datasets and can maintain high accuracy and low false detection rates.
	Table 4 shows the average values of AD performance metrics for each method on all datasets, denoted by ACC, 
TPR, and FPR, respectively. Although the FPR value of 1DCB-PSRS for drift anomaly is 1.15%, which is 
higher than that of SVR, its FPR value for bias anomaly is 0.90%, significantly lower than that of SVR and 
other baseline methods. In addition, compared to the baseline methods, 1DCB-PSRS demonstrates the best 
average performance metrics in ACC and TPR values, achieving 96.59% and 95.43% for bias anomaly, and 
96.38% and 95.30% for drift anomaly, respectively. The average performance metrics of LSTM-RF are also 
relatively good with ACC, TPR, and FPR values of 93.08%, 91.69%, and 4.15%, and 93.30%, 92.49%, and 
5.30%, respectively, for bias and drift anomalies. Although the TPR values of BiLSTM for bias and drift 
anomalies are all 94.17%, second only to 1DCB-PSRS, its FPR values are equally high at 21.98% and 17.73%, 
respectively. The FPR values of 1D CNN, STC-LSTM, and TCN are also relatively high, ranging from 11.38% 
to 22.18%. SVR exhibits relatively poor performance in ACC and TPR values, with values of 88.41% and 
83.97% for bias anomaly, and 89.33% and 84.26% for drift anomaly, respectively.
	2.	  Data recovery.
	Table 5 presents the data recovery results of the above methods across all datasets. For different anomaly types 
of the Flight97, Flight98, and Flight104 datasets, 1DCB-PSRS obtains the smallest MAE and RMSE values. 
Specifically, for bias and drift anomalies of the Flight97 dataset, the MAE and RMSE values of 1DCB-PSRS 
are 1.3460 and 1.4298, and 1.7795 and 1.9103, respectively. For bias and drift anomalies of the Flight98 da­
taset, the MAE and RMSE values of 1DCB-PSRS are 0.5475 and 0.6234, and 0.7922 and 0.9071, respectively. 
Model
Anomaly type
−
ACC
TPR
FPR
1DCB-PSRS
Bias anomaly
96.59%
95.43%
0.90%
Drift anomaly
96.38%
95.30%
1.15%
1D CNN
Bias anomaly
91.80%
90.79%
11.38%
Drift anomaly
87.06%
90.90%
22.18%
BiLSTM
Bias anomaly
89.72%
94.17%
21.98%
Drift anomaly
91.09%
94.17%
17.73%
LSTM-RF
Bias anomaly
93.08%
91.69%
4.15%
Drift anomaly
93.30%
92.49%
5.30%
STC-LSTM
Bias anomaly
88.22%
91.44%
20.88%
Drift anomaly
88.93%
90.92%
16.93%
TCN
Bias anomaly
87.19%
86.98%
15.45%
Drift anomaly
90.07%
91.10%
15.25%
SVR
Bias anomaly
88.41%
83.97%
2.38%
Drift anomaly
89.33%
84.26%
0.35%
Table 4.  The average AD performance of the above methods.
 
Fig. 9.  The drift AD results of 1DCB-PSRS, 1D CNN, BiLSTM, LSTM-RF, STC-LSTM, TCN, and SVR.
 
Scientific Reports |        (2025) 15:20924 
11
| https://doi.org/10.1038/s41598-025-05322-4
www.nature.com/scientificreports/

## Page 12

For bias and drift anomalies of the Flight104 dataset, the MAE and RMSE values of 1DCB-PSRS are 1.0323 
and 0.9806, and 1.3077 and 1.2106, respectively. Although the RMSE value of 1DCB-PSR for bias anomaly of 
Flight97-104 dataset is 1.3544, slightly higher than that of LSTM-RF, its MAE value is the lowest compared to 
the baseline methods, at 0.9684. For drift anomaly of the Flight97-104 dataset, the MAE and RMSE values of 
1DCB-PSR are the lowest, at 0.9289 and 1.2751, respectively. This benefits from 1DCB-PSRS fully leveraging 
the advantages of 1D CNN and BiLSTM in time-series data modeling, enabling the comprehensive extraction 
of spatiotemporal features from flight data, thereby achieving more accurate predictions. In contrast, the 
data recovery performance of 1D CNN, BiLSTM, LSTM-RF, STC-LSTM, and TCN is relatively inferior, with 
MAE and RMSE values ranging from 0.6013 to 1.8954 and from 0.8707 to 2.3609, respectively, for different 
anomaly types of the Flight97, Flight98, Flight104, and Flight97-104 datasets. This is because 1D CNN, BiL­
STM, LSTM-RF, STC-LSTM, and TCN either focus on local feature extraction or temporal feature modeling, 
limiting their representation capability for complex flight data. Due to SVR focusing only on spatial feature 
modeling while ignoring temporal characteristics, its data recovery performance is the worst, with MAE and 
RMSE values for bias and drift anomalies across different datasets ranging from 1.9596 to 3.5461 and from 
2.8096 to 4.5183, respectively.
Performance of transfer learning with limited training or fine-tuning samples
The effectiveness of 1DCB-PSRS has been verified in the above experiments. Therefore, based on 1DCB-PSRS as 
the pre-trained framework, the feasibility and effectiveness of the knowledge transfer method based on multi-
source data fusion is further explored in the target domain with limited samples. Specifically, the first 10% 
and the first 20% data are used as the training or fine-tuning samples and the last 20% are used as the testing 
samples in the target domain Flight98 dataset. This helps to provide a more in-depth understanding of the 
knowledge transfer-based approach’s performance in the target domain with limited samples. In this subsection, 
four groups of experiments are set up, which are described as follows:
•	 Direct training with limited samples of the target domain Flight98 dataset, denoted by E1.
•	 Transfer from the source domain Flight97 dataset to the target domain Flight98 dataset, denoted by E2.
•	 Transfer from the source domain Flight104 dataset to the target domain Flight98 dataset, denoted by E3.
•	 Transfer from the source domain Flight97-104 dataset to the target domain Flight98 dataset, denoted by E4.
	1.	 AD
	Figure 10 displays the AD results of E1, E2, E3, and E4. For bias and drift anomalies, the ACC, TPR, and FPR 
values of E1 with 10% training samples are 28.72%, 13.41%, and 37.60%, respectively. Although the ACC and 
TPR values of E1 with 20% training samples are significantly improved, its FPR values are as high as 74.20% to 
75.40%, respectively, for bias and drift anomalies. The reason for E1’s poor performance is model underfitting 
due to insufficient training samples. The performances of E2, E3, and E4 are substantially improved compared 
to E1 with 10% fine-tuning samples. The overall AD performances of E2, E3, and E4 with 20% fine-tuning 
samples are also better than that of E1 with 20% training samples. This indicates that for the tasks in this pa­
per, it is feasible to enhance the performance of the target task with limited samples by transferring the source 
task knowledge to the target task. E3 shows the lowest FPR values under 10% and 20% fine-tuning samples, 
Dataset name
Anomaly type
Evaluation metrics
1DCB-PSRS
1D CNN
BiLSTM
LSTM-RF
STC-LSTM
TCN
SVR
Flight97
Bias anomaly
MAE
1.3460
1.8012
1.6515
1.4647
1.4194
1.7748
2.2398
RMSE
1.7795
2.2341
1.8063
1.9519
1.8880
2.1848
2.8450
Drift anomaly
MAE
1.4298
1.8954
1.8366
1.4446
1.6033
1.7029
2.4323
RMSE
1.9103
2.3609
2.0186
1.9122
2.2958
2.2389
3.1276
Flight98
Bias anomaly
MAE
0.5475
0.7172
0.6327
0.6013
0.9443
1.0352
1.9815
RMSE
0.7922
0.9132
0.9153
0.8707
1.1424
1.2837
2.8096
Drift anomaly
MAE
0.6234
0.7293
0.6931
0.7172
1.0456
1.3621
2.0858
RMSE
0.9071
0.9459
1.0361
1.0347
1.2995
1.7778
2.9770
Flight104
Bias anomaly
MAE
1.0323
1.4033
1.2211
1.1165
1.4929
1.5135
3.3621
RMSE
1.3077
1.7060
1.5244
1.5806
1.8974
1.8641
4.2998
Drift anomaly
MAE
0.9806
1.4526
1.4893
1.4063
1.5232
1.5296
3.5461
RMSE
1.2106
1.7577
1.9191
1.8286
1.8702
1.9404
4.5183
Flight97-104
Bias anomaly
MAE
0.9684
1.1275
1.0803
1.0060
1.0879
1.1863
1.9596
RMSE
1.3544
1.4437
1.5105
1.3211
1.5483
1.5926
2.8427
Drift anomaly
MAE
0.9289
1.1356
1.1407
1.1466
1.2211
1.1797
2.0605
RMSE
1.2751
1.5177
1.8176
1.4436
1.8052
1.6531
3.0259
Table 5.  Data recovery results for 1DCB-PSR, 1D CNN, BiLSTM, LSTM-RF, STC-LSTM, TCN, and SVR in all 
datasets.
 
Scientific Reports |        (2025) 15:20924 
12
| https://doi.org/10.1038/s41598-025-05322-4
www.nature.com/scientificreports/

## Page 13

ranging only from 1.10% to 1.60%, slightly better than E4. However, in terms of overall performance, E4 out­
performs E1, E2, and E3 in both 10% and 20% fine-tuning samples. In particular, E4 obtains the highest ACC 
and TPR values of 80.25% and 85.75%, and 73.95% and 80.36%, respectively, for bias and drift anomalies with 
20% fine-tuning samples. Meanwhile, E4 has relatively lower FPR values, ranging only from 2.30% to 5.80%. 
In addition, there is no significant improvement in the overall performance of E2 and E3 with 20% fine-tuning 
samples compared to 10% fine-tuning samples. This may be due to the large difference in data distribution 
between a single source domain and the target domain. This difference may result in the model that cannot fit 
the data of the target task well.
	Table 6 shows the difference of each corresponding performance metric for bias and drift anomalies of E1, 
E2, and E3 compared to E4 with 10% and 20% training or fine-tuning samples. “-” indicates a decrease and 
“ + ” indicates an increase. For bias and drift anomalies, the ΔACC, ∆TPR, and ∆FPR values of E1 with 10% 
and 20% training samples have the largest range of variations, which are − 45.91% to − 25.28%, − 50.32% to 
− 5.18%, and + 27% to + 71.80%, respectively. This is due to the limited training samples, which makes the 
model underfitting, as described earlier. Although E2’s TPR value with 10% fine-tuning samples increases 
by 2.27% compared to E4 for bias anomaly, its ACC and FPR values decrease by 12.19% and 15.47%, and 
increase by 45.00% and 47.80%, respectively, for bias and drift anomalies. The ranges of ∆ACC, ∆TPR, and 
∆FPR values for E2 with 20% fine-tuning samples are similarly large, at − 17.03% and − 21.25%, − 9.09% and 
− 16.22%, and + 34.60% and + 32.30%, respectively. Although E4 has slightly higher FPR values than E3 with 
10% and 20% fine-tuning samples, its ΔFPR ranges from only − 4.50% to − 0.80%, which is relatively lower. 
In contrast, for bias and drift anomalies, the △ACC and △TPR values of E3 with 10% fine-tuning samples 
are − 7.19% and − 6.75%, and − 11.09% and − 10.27%, respectively. The ΔACC and ΔTPR values of E3 with 
20% fine-tuning samples are -9.00% and -11.06%, and -15.18% and -17.31%, respectively, for bias and drift 
anomalies. The experimental results show that E4 exhibits a substantial overall increase in the TPR and ACC 
values while maintaining lower FPR values compared to E1, E2, and E3.
	2.	 Data recovery
	Figures 11 and 12 display the visualization of data recovery for E1, E2, E3, and E4 with 10% and 20% training 
or fine-tuning samples, respectively, where the blue curves are the original data without anomaly and the red 
curves are the predicted data. With 10% training or fine-tuning samples, E1, E2, and E3 exhibit varying de­
Experiment name
Anomaly type
△ACC
△TPR
△FPR
10%
20%
10%
20%
10%
20%
E1
Bias anomaly
− 45.56%
− 25.28%
− 50.32%
− 5.18%
 + 35.10%
 + 69.60%
Drift anomaly
− 45.91%
− 31.34%
− 54.50%
− 12.95%
 + 27.00%
 + 71.80%
E2
Bias anomaly
− 12.19%
− 17.03%
 + 2.72%
− 9.09%
 + 45.00%
 + 34.60%
Drift anomaly
− 15.47%
− 21.25%
− 0.77%
− 16.22%
 + 47.80%
 + 32.30%
E3
Bias anomaly
− 7.19%
− 9.00%
− 11.09%
− 15.18%
− 1.40%
− 4.50%
Drift anomaly
− 6.75%
− 11.66%
− 10.27%
− 17.31%
− 1.00%
− 0.80%
Table 6.  The difference of each corresponding performance metric for bias and drift anomalies of E1, E2, and 
E3 compared to E4 with 10% and 20% training or fine-tuning samples.
 
Fig. 10.  The AD results of E1, E2, E3, and E4.
 
Scientific Reports |        (2025) 15:20924 
13
| https://doi.org/10.1038/s41598-025-05322-4
www.nature.com/scientificreports/

## Page 14

grees of recovery deviations, as indicated by the black circles in Fig. 11. Notably, E1 shows the largest recovery 
bias with 10% training samples. As the number of training samples increases, the recovery bias of E1 improves 
significantly. However, the relatively obvious recovery bias of E1 remains, as depicted by the blue circles in 
Fig. 12. The recovery performances of E2 and E3 do not appear to show significant improvement with 10% 
and 20% fine-tuning samples, possibly due to the more pronounced difference in feature distribution between 
the source and target domains, as mentioned earlier. In contrast, through the multi-source fusion strategy, 
E4 effectively mitigates the negative impact of domain differences on the transfer learning process, leading to 
superior recovery performance.
 
Table 7 provides the MAE and RMSE values for E1, E2, E3, and E4 with 10% and 20% training or fine-tuning 
samples. For bias and drift anomalies, the MAE and RMSE values of E1 with 10% training samples are 2.6580 
Fig. 12.  Data recovery visualization for E1, E2, E3, and E4 with 20% training or fine-tuning samples.
 
Fig. 11.  Data recovery visualization for E1, E2, E3, and E4 with 10% training or fine-tuning samples.
 
Scientific Reports |        (2025) 15:20924 
14
| https://doi.org/10.1038/s41598-025-05322-4
www.nature.com/scientificreports/

## Page 15

and 2.6797, and 3.1705 and 3.1882, respectively. The MAE and RMSE values of E1 with 20% training samples 
improve dramatically, with 1.3148 and 1.3905, and 1.5768 and 1.6872 for bias and drift anomaly, respectively. 
The MAE and RMSE values of E2 and E3 are lower than E1 with 10% fine-tuning samples. This suggests that 
the target domain can efficiently leverage the knowledge from the single-source domain to alleviate the recovery 
bias. However, the MAE and RMSE values of E2 and E3 with 20% fine-tuning samples show an increment 
compared to E1, which may be attributed to the larger differences between the source and target domains, 
as described earlier. Compared to E1, E2, and E3, E4 with 10% and 20% fine-tuning samples demonstrates 
the lowest MAE and RMSE values, indicating that multi-source data fusion can provide a more enriched data 
information, reducing recovery deviation.
Discussion
The main findings of this study can be summarized as follows based on the above experimental results:
First, 1DCB-PSRS performed well in detecting bias and drift anomalies for different datasets, with average 
ACC values above 96.00%, average TPR values above 95.00%, and average FPR values below 1.20%, demonstrating 
good robustness and generalization. In addition, 1DCB-PSRS also achieved optimal data recovery performance, 
with MAE and RMSE values ranging from 0.5475 to 1.4298, and 0.7922 and 1.9103, respectively, for different 
anomaly types of different datasets. This was made possible by the fact that 1DCB-PSRS used 1D CNN and 
BiLSTM to construct the prediction model, which was able to fully extract the spatiotemporal features of 
flight data and realize the accurate prediction of the monitored parameter. Meanwhile, the anomaly detection 
performance was further improved by using MIC to select correlated flight parameters as model inputs and 
EWMA to smooth the residuals to reduce the effects of uncorrelated flight parameters and random noise. These 
results emphasize the significant advantages of 1DCB-PSRS in UAV flight data AD and data recovery, bringing 
important reference value for practical applications.
Second, using 1DCB-PSRS as the pre-training framework, a series of experiments were conducted with 
limited samples. E1 exhibited inferior performance primarily due to insufficient training samples, resulting in 
model underfitting. E2 and E3 mitigated the problem of model underfitting to some extent. Nevertheless, despite 
an increase in fine-tuning samples, the AD performances of E2 and E3 did not show substantial enhancement. 
This observation could be attributed to the large difference between the single-source and target domain, thus 
limiting the performance improvement of E2 and E3. E4 exhibited a noticeable advantage in AD performance 
over E1, E2, and E3, with higher ACC and TPR values and relatively low FPR values. For data recovery, E4 had 
the smallest MAE and RMSE values. The experimental results demonstrated that the knowledge transfer method 
based on multi-source data fusion exhibited remarkable advantages for the task addressed in this study and is 
expected to be widely used in practical scenarios.
However, it is important to recognize that there are some limitations to this study. First, the effectiveness 
of the proposed method is validated in this study by using anomaly injection to obtain bias and drift anomaly 
data. However, other anomaly types such as stuck anomalies and composite anomalies17,58 are not included in 
the experimental scope, resulting in the effectiveness of the proposed method in multiple anomaly types that 
has not yet been fully evaluated. Second, this paper utilizes FPR, TPR, ACC, MAE, and RMSE as AD and data 
recovery performance metrics, which may make the evaluation of the results less comprehensive. Finally, this 
paper leverages deep learning to achieve AD and data recovery, but its poor interpretability may hinder the 
credibility and generalization of the proposed method in practical applications.
Therefore, considering the above limitations, future research will incorporate more evaluation metrics (such 
as F1 score and t-tests) and anomaly types to comprehensively assess the model performance. Meanwhile, 
enhancing the model interpretability using methods like SHapley Additive exPlanations (SHAP)59 and Local 
Interpretable Model-agnostic Explanation (LIME)60 is also an important direction for future research.
Conclusion and prospects
To improve the AD and recovery performance of UAV flight data with limited samples, a novel data-driven 
framework 1DCB-PSRS was first proposed. It was based on the designed 1D CNN-BiLSTM prediction model to 
fully capture the complex spatiotemporal features of flight data while integrating MIC-based parameter selection 
and EWMA-based residual smoothing to reduce the interference of irrelevant flight parameters and random 
noise. Then, an innovative knowledge transfer approach based on multi-source data fusion was proposed for 
UAV flight data AD and recovery with limited samples. It employed 1DCB-PSRS as the pre-training framework 
Sample size
Evaluation metrics
Anomaly type
E1
E2
E3
E4
10%
MAE
Bias anomaly
2.6580
1.4953
1.4408
1.0107
Drift anomaly
2.6797
1.5515
1.3017
1.0502
RMSE
Bias anomaly
3.1705
1.9500
1.6574
1.1831
Drift anomaly
3.1882
2.0315
1.5319
1.2561
20%
MAE
Bias anomaly
1.3148
1.4802
1.3422
0.8870
Drift anomaly
1.3905
1.5318
1.2016
0.9048
RMSE
Bias anomaly
1.5768
1.9819
1.5400
1.0558
Drift anomaly
1.6872
2.0429
1.4140
1.1165
Table 7.  The MAE and RMSE values for E1, E2, E3, and E4 with 10% and 20% training or fine-tuning samples.
 
Scientific Reports |        (2025) 15:20924 
15
| https://doi.org/10.1038/s41598-025-05322-4
www.nature.com/scientificreports/

## Page 16

to transfer knowledge using data distribution information from multiple source domains, avoiding reliance on a 
single source domain data. Finally, extensive experiments were conducted on real UAV flight data. With sufficient 
training data, for the bias and drift anomalies of different datasets, the average ACC values of 1DCB-PSRS were 
all over 96.00%, the average TPR values were all over 95.00%, and the average FPR values were all below 1.20%. 
Meanwhile, for different anomaly types of different datasets, 1DCB-PSRS also achieved the best data recovery 
performance with sufficient data, with MAE and RMSE values ranging from 0.5475 to 1.4298, 0.7922 and 1.9103, 
respectively. With limited training or fine-tuning samples, E4 achieved a good AD performance. Particularly 
with 20% fine-tuning samples, E4 showed the highest ACC and TPR values of 80.25% and 85.75%, and 73.95% 
and 80.36%, respectively, for bias and drift anomalies. For data recovery, E4 consistently has the lowest MAE 
and RMSE values. The effectiveness of 1DCB-PSRS as the pre-training framework and the knowledge transfer 
method based on multi-source data fusion was proved according to the experimental results.
In future research, more metrics will be included to comprehensively assess the model performance. 
Meanwhile, the performance of the proposed method will be validated in more anomaly types. In addition, 
model interpretability will be actively explored in the future.
Data availability statement
All original data from this study can be accessed through the link https://conservancy.umn.edu. Researchers 
interested in accessing and analyzing these data can directly obtain resources from the specified repository.
Received: 25 November 2024; Accepted: 2 June 2025
References
	 1.	 Khan, M. A. & Farooq, F. A Comprehensive Survey on UAV-based Data Gathering Techniques in Wireless Sensor Networks.
	 2.	 Cheng, N. et al. AI for UAV-assisted IoT applications: A comprehensive review. IEEE Internet Things J. 10, 14438–14461 (2023).
	 3.	 Fan, Z., Lin, Y., Ai, Y. & Xu, H. Adaptive task migration strategy with delay risk control and reinforcement learning for emergency 
monitoring. Sci. Rep. 14, 17606 (2024).
	 4.	 Tahir, M. N. et al. Application of unmanned aerial vehicles in precision agriculture. In Precision agriculture 55–70 (Elsevier, 2023).
	 5.	 Unmanned aerial vehicle (UAV) market by product type, by wing type, by operation mode, by range, by maximum takeoff weight 
(MTOW), by system, by application, by end-user, forecasts to 2027. (2021). ​h​t​t​p​s​:​/​/​w​w​w​.​e​m​e​r​g​e​n​r​e​s​e​a​r​c​h​.​c​o​m​/​i​n​d​u​s​t​r​y​-​r​e​p​o​r​t​/​u​
n​m​a​n​n​e​d​-​a​e​r​i​a​l​-​v​e​h​i​c​l​e​-​m​a​r​k​e​t​/
	 6.	 Unmanned aerial vehicle (UAV) market by point of sale, systems, platform (civil & commercial, and defense & governement), 
function, end use, application, type, mode of operation, MTOW, range, and Region—Global forecast to 2026. (2021). ​h​t​t​p​s​:​/​/​w​w​w​
.​m​a​r​k​e​t​s​a​n​d​m​a​r​k​e​t​s​.​c​o​m​/​M​a​r​k​e​t​-​R​e​p​o​r​t​s​/​u​n​m​a​n​n​e​d​-​a​e​r​i​a​l​-​v​e​h​i​c​l​e​s​-​u​a​v​-​m​a​r​k​e​t​-​6​6​2​.​h​t​m​l
	 7.	 Ahmad, M. W., Akram, M. U., Ahmad, R., Hameed, K. & Hassan, A. Intelligent framework for automated failure prediction, 
detection, and classification of mission critical autonomous flights. ISA Trans. 129, 355–371 (2022).
	 8.	 Yang, L., Li, S., Li, C., Zhang, A. & Zhang, X. A survey of unmanned aerial vehicle flight data anomaly detection: technologies, 
applications, and future directions. Sci. Chin. Technol. Sci. https://doi.org/10.1007/s11431-022-2213-8 (2023).
	 9.	 Liang, S. et al. Data-driven fault diagnosis of FW-UAVs with consideration of multiple operation conditions. ISA Trans. 126, 
472–485 (2022).
	10.	 Qi, J., Zhao, X., Jiang, Z. & Han, J. An Adaptive Threshold Neural-Network Scheme for Rotorcraft UAV Sensor Failure Diagnosis. 
In Advances in Neural Networks – ISNN 2007 (eds Liu, D. et al.) 589–596 (Springer, Heidelberg, 2007).
	11.	 Bu, J. et al. Integrated method for the UAV navigation sensor anomaly detection. IET Radar Sonar Navig. 11, 847–853 (2017).
	12.	 Abbaspour, A., Aboutalebi, P., Yen, K. K. & Sargolzaei, A. Neural adaptive observer-based sensor and actuator fault detection in 
nonlinear systems: Application in UAV. ISA Trans. 67, 317–329 (2017).
	13.	 López-Estrada, F. R., Ponsart, J.-C., Theilliol, D., Zhang, Y. & Astorga-Zaragoza, C.-M. LPV model-based tracking control and 
robust sensor fault diagnosis for a quadrotor UAV. J. Intell. Rob. Syst. 84, 163–177 (2016).
	14.	 Ren, B., Liu, J., Zhang, S., Yang, C. & Na, J. On-line configuration identification and control of modular reconfigurable flight array. 
IECE Trans. Intell. Syst. 1, 91–101 (2024).
	15.	 Abro, G. E. M., Ali, Z. A. & Masood, R. J. Synergistic UAV motion: A comprehensive review on advancing multi-agent coordination. 
IECE Trans. Sens. Commun. Control 1, 72–88 (2024).
	16.	 He, Y., Peng, Y., Wang, S., Liu, D. & Leong, P. H. A structured sparse subspace learning algorithm for anomaly detection in UAV 
flight data. IEEE Trans. Instrum. Meas. 67, 90–100 (2017).
	17.	 He, Y., Peng, Y., Wang, S. & Liu, D. ADMOST: UAV flight data anomaly detection and mitigation via online subspace tracking. 
IEEE Trans. Instrum. Meas. 68, 1035–1044 (2018).
	18.	 Zhong, J., Zhang, Y., Wang, J., Luo, C. & Miao, Q. Unmanned aerial vehicle flight data anomaly detection and recovery prediction 
based on spatio-temporal correlation. IEEE Trans. Reliab. 71, 457–468 (2022).
	19.	 Guo, K., Wang, N., Liu, D. & Peng, X. Uncertainty-aware LSTM based dynamic flight fault detection for UAV actuator. IEEE Trans. 
Instrum. Meas. 72, 1–13 (2023).
	20.	 Wang, B., Peng, X., Jiang, M. & Liu, D. Real-time fault detection for UAV based on model acceleration engine. IEEE Trans. Instrum. 
Meas. 69, 9505–9516 (2020).
	21.	 He, K. et al. Graph attention network-based fault detection for UAVs with multivariant time series flight data. IEEE Trans. Instrum. 
Meas. 71, 1–13 (2022).
	22.	 Park, K. H., Park, E. & Kim, H. K. Unsupervised fault detection on unmanned aerial vehicles: Encoding and thresholding approach. 
Sensors 21, 2218 (2021).
	23.	 Yang, L. et al. Data-driven unsupervised anomaly detection and recovery of unmanned aerial vehicle flight data based on 
spatiotemporal correlation. Sci. Chin. Technol. Sci. 66, 1–13 (2023).
	24.	 Bae, G. & Joe, I. UAV anomaly detection with distributed artificial intelligence based on LSTM-AE and AE. Adv. Multimed. 
Ubiquitous Eng.: MUE/FutureTech. 2019(13), 305–310 (2020).
	25.	 Bell, V., Rengasamy, D., Rothwell, B. & Figueredo, G. P. Anomaly detection for unmanned aerial vehicle sensor data using a stacked 
recurrent autoencoder method with dynamic thresholding. arXiv preprintarXiv:2203.04734 (2022).
	26.	 Wang, B., Liu, D., Peng, Y. & Peng, X. Multivariate regression-based fault detection and recovery of UAV flight data. IEEE Trans. 
Instrum. Meas. 69, 3527–3537 (2020).
	27.	 Yang, L., Li, S., Zhu, C., Zhang, A. & Liao, Z. Spatio-temporal correlation-based multiple regression for anomaly detection and 
recovery of unmanned aerial vehicle flight data. Adv. Eng. Inform. 60, 102440 (2024).
	28.	 Yang, L., Li, S., Li, C. & Zhu, C. Data-driven multivariate regression-based anomaly detection and recovery of unmanned aerial 
vehicle flight data. J. Comput. Design and Eng. 11, 176–193 (2024).
Scientific Reports |        (2025) 15:20924 
16
| https://doi.org/10.1038/s41598-025-05322-4
www.nature.com/scientificreports/

## Page 17

29.	 Lu, H., Wang, Z. & Shi, Y. Unmanned aerial vehicle flight data anomaly detection based on multirate-aware LSTM. IEEE Trans. 
Instrum. Meas. 73, 1–13 (2024).
	30.	 Wang, Y. et al. Deeply integrated autoencoder-based anomaly detection and critical parameter identification for unmanned aerial 
vehicle actuators. IEEE Sensors J. 24, 24905–24920 (2024).
	31.	 Jiang, G., Nan, P., Zhang, J., Li, Y. & Li, X. Robust spatial-temporal autoencoder for unsupervised anomaly detection of unmanned 
aerial vehicle with flight data. IEEE Trans. Instrum. Meas. 73, 1–14 (2024).
	32.	 Pan, S. J. & Yang, Q. A survey on transfer learning. IEEE Trans. Knowl. Data Eng. 22, 1345–1359 (2009).
	33.	 Zhang, A. et al. Transfer learning with deep recurrent neural networks for remaining useful life estimation. Appl. Sci. 8, 2416 
(2018).
	34.	 Li, C., Li, S., Wang, H., Gu, F. & Ball, A. D. Attention-based deep meta-transfer learning for few-shot fine-grained fault diagnosis. 
Knowl.-Based Syst. 264, 110345 (2023).
	35.	 Li, C. et al. Meta-learning for few-shot bearing fault diagnosis under complex working conditions. Neurocomputing 439, 197–211 
(2021).
	36.	 Lu, Y., Tian, Z., Zhou, R. & Liu, W. A general transfer learning-based framework for thermal load prediction in regional energy 
system. Energy 217, 119322 (2021).
	37.	 Tariq, S. et al. Transfer learning driven sequential forecasting and ventilation control of PM2.5 associated health risk levels in 
underground public facilities. J. Hazard. Mater. 406, 124753 (2021).
	38.	 Zhang, W., Wang, Z. & Li, X. Blockchain-based decentralized federated transfer learning methodology for collaborative machinery 
fault diagnosis. Reliab. Eng. Syst. Saf. 229, 108885 (2023).
	39.	 Zhang, P. et al. Intelligent tool wear monitoring based on multi-channel hybrid information and deep transfer learning. J. Manuf. 
Syst. 69, 31–47 (2023).
	40.	 Kiranyaz, S. et al. 1D convolutional neural networks and applications: A survey. Mech. Syst. Signal Process. 151, 107398 (2021).
	41.	 Junior, R. F. R. et al. Fault detection and diagnosis in electric motors using 1d convolutional neural networks with multi-channel 
vibration signals. Measurement 190, 110759 (2022).
	42.	 Kim, J., Kang, H. & Kang, P. Time-series anomaly detection with stacked Transformer representations and 1D convolutional 
network. Eng. Appl. Artif. Intell. 120, 105964 (2023).
	43.	 Kim, T.-Y. & Cho, S.-B. Web traffic anomaly detection using C-LSTM neural networks. Expert Syst. Appl. 106, 66–76 (2018).
	44.	 Heaton, I. G., Bengio, Y. & Courville, A. Deep learning Deep Learning (USA MIT Press, Uk, 2016).
	45.	 Graves, A. & Schmidhuber, J. Framewise phoneme classification with bidirectional LSTM and other neural network architectures.
	46.	 Borroto, M. A. & Ricca, F. SPARQL-QA-v2 system for knowledge base question answering. Expert Syst. Appl. 229, 120383 (2023).
	47.	 Shen, M. et al. A TL_FLAT model for Chinese text datasets of UAV power systems: optimization and performance. Int. J. Intell. 
Syst. https://doi.org/10.1155/2023/3322735 (2023).
	48.	 Chang, G., Gao, H., Yao, Z. & Xiong, H. TextGuise: Adaptive adversarial example attacks on text classification model. 
Neurocomputing 529, 190–203 (2023).
	49.	 Zhuang, F. et al. A comprehensive survey on transfer learning. Proc. IEEE 109, 43–76 (2020).
	50.	 Jahan, A. & Edwards, K. L. A state-of-the-art survey on the influence of normalization techniques in ranking: Improving the 
materials selection process in engineering design. Mater. Des. 1980–2015(65), 335–342 (2015).
	51.	 Grigg, O. & Spiegelhalter, D. A simple risk-adjusted exponentially weighted moving average. J. Am. Stat. Assoc. 102, 140–152 
(2007).
	52.	 Taylor, B. Thor Flight 97. (2013). Thor Flight 97. Retrieved from the University of Minnesota Digital Conservancy. ​h​t​t​p​s​:​/​/​h​d​l​.​h​a​n​
d​l​e​.​n​e​t​/​1​1​2​9​9​/​1​7​4​3​7​4​.​
	53.	 Taylor, B. Thor Flight 98. (2013). Thor Flight 98. Retrieved from the University of Minnesota Digital Conservancy. ​h​t​t​p​s​:​/​/​h​d​l​.​h​a​n​
d​l​e​.​n​e​t​/​1​1​2​9​9​/​1​7​4​3​7​5​.​
	54.	 Taylor, B. Thor flight 104. (2014). Thor Flight 104. Retrieved from the University of Minnesota Digital Conservancy. ​h​t​t​p​s​:​/​/​h​d​l​.​h​
a​n​d​l​e​.​n​e​t​/​1​1​2​9​9​/​1​7​4​2​2​8​.​
	55.	 Kinney, J. B. & Atwal, G. S. Equitability, mutual information, and the maximal information coefficient. Proc. Natl. Acad. Sci. 111, 
3354–3359 (2014).
	56.	 Raschka, S. An Overview of General Performance Metrics of Binary Classifier Systems. Preprint at http://arxiv.org/abs/1410.5330 
(2014).
	57.	 Hodson, T. O. Root-mean-square error (RMSE) or mean absolute error (MAE): when to use them or not. Geosci. Model Develop. 
15, 5481–5487 (2022).
	58.	 Qi, X., Theilliol, D., Qi, J., Zhang, Y. & Han, J. A literature review on Fault Diagnosis methods for manned and unmanned 
helicopters. In: 2013 International Conference on Unmanned Aircraft Systems (ICUAS) 1114–1118 (2013). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​0​9​/​
I​C​U​A​S​.​2​0​1​3​.​6​5​6​4​8​0​1​.​
	59.	 Nohara, Y., Matsumoto, K., Soejima, H. & Nakashima, N. Explanation of machine learning models using shapley additive 
explanation and application for real data in hospital. Comput. Methods Programs Biomed. 214, 106584 (2022).
	60.	 Hassan, S. U., Abdulkadir, S. J., Zahid, M. S. M. & Al-Selwi, S. M. Local interpretable model-agnostic explanation approach for 
medical imaging analysis: A systematic literature review. Comput. Biol. Med. 185, 109569 (2025).
Acknowledgements
This work was supported by the National Natural Science Foundation of China (52275480). Especially thanks for 
the computing support of the State Key Laboratory of Public Big Data, Guizhou University.
Author contributions
Lei Yang: Writing-original draft, Writing—review & editing, Validation, Software, Methodology, Investigation, 
Formal analysis, Data curation, Visualization, Conceptualization. Shaobo Li: Supervision, Funding acquisition, 
Conceptualization. Liya Yu: Writing-review & editing, Methodology, Data curation. Caichao Zhu: Supervision, 
Conceptualization.  Congbao Wang: Writing—re-view & editing, Methodology.
Funding
National Natural Science Foundation of China, 52275480.
Declarations
Competing interests
The authors declare no competing interests.
Scientific Reports |        (2025) 15:20924 
17
| https://doi.org/10.1038/s41598-025-05322-4
www.nature.com/scientificreports/

## Page 18

Additional information
Correspondence and requests for materials should be addressed to S.L.
Reprints and permissions information is available at www.nature.com/reprints.
Publisher’s note  Springer Nature remains neutral with regard to jurisdictional claims in published maps and 
institutional affiliations.
Open Access   This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 
4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in 
any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide 
a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have 
permission under this licence to share adapted material derived from this article or parts of it. The images or 
other third party material in this article are included in the article’s Creative Commons licence, unless indicated 
otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence 
and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to 
obtain permission directly from the copyright holder. To view a copy of this licence, visit ​h​t​t​p​:​/​/​c​r​e​a​t​i​v​e​c​o​m​m​o​
n​s​.​o​r​g​/​l​i​c​e​n​s​e​s​/​b​y​-​n​c​-​n​d​/​4​.​0​/​.​
© The Author(s) 2025 
Scientific Reports |        (2025) 15:20924 
18
| https://doi.org/10.1038/s41598-025-05322-4
www.nature.com/scientificreports/
