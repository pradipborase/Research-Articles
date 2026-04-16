# Unmanned_Aerial_Vehicle_Flight_Data_Anomaly_Detection_and_Recovery_Prediction_Based_on_Spatio-Temporal_Correlation.pdf

## Page 1

IEEE TRANSACTIONS ON RELIABILITY, VOL. 71, NO. 1, MARCH 2022
457
Unmanned Aerial Vehicle Flight Data Anomaly
Detection and Recovery Prediction Based on
Spatio-Temporal Correlation
Jie Zhong
, Yujie Zhang
, Member, IEEE, Jianyu Wang
, Chong Luo
, and Qiang Miao
, Senior Member, IEEE
Abstract—With the development of unmanned aerial vehicle
(UAV) technology, a UAV is gradually applied to a variety of civil
ﬁelds, such as photography, power line inspection, and environ-
mental monitoring. At the same time, the safety and reliability of a
UAV also attract wide attention. Anomaly detection is one of the key
technologies to improve the safety of an UAV. The structure of the
UAV system is complex, and there are complex spatio-temporal
correlations among the high-dimensional ﬂight data with many
parameters. However, the existing methods often ignore the spatio-
temporal correlation of data and lack parameter selection, which
is used to abandon the parameters without a positive impact on
anomaly detection results. This article proposes a spatio-temporal
correlation based long short-term memory (LSTM) method for
anomaly detection and recovery prediction of UAV ﬂight data.
First, an artiﬁcial neural network correlation analysis is proposed
to preliminarily mine the spatio-temporal correlation in ﬂight data
and to obtain the correlation parameter sets. Second, the LSTM
model is established, and the mapping among different parameters
is realized. Finally, anomaly detection and recovery prediction are
carried out based on parameter sets mapping model. The effective-
ness of the proposed method is veriﬁed by generating sample sets
with anomaly injection on real UAV ﬂight data.
Index Terms—Anomaly detection, correlation analysis, recovery
prediction, spatio-temporal correlation based long short-term
memory (STC-LSTM), unmanned aerial vehicle (UAV).
I. INTRODUCTION
W
ITH the rapid development of unmanned aerial vehicle
(UAV) technology, manufacturing and operation costs
of a UAV are greatly reduced, which promotes the use of UAVs
in different civil ﬁelds, including UAV photography, power line
inspection, environmental monitoring, and express delivery [1]–
[3]. Meanwhile, more and more attention has been paid to the
Manuscript received September 20, 2021; revised November 7, 2021; ac-
cepted December 2, 2021. Date of publication December 31, 2021; date of
current version March 2, 2022. This work was supported in part by the National
Natural Science Foundation of China (52075349), in part by the Sichuan Science
and Technology Program (2020YFH0022), and in part by the Aeronautical
Science Foundation of China (201905019001). Associate Editor: R. Gao. (Cor-
responding author: Yujie Zhang.)
Jie Zhong and Jianyu Wang are with the School of Aeronautics
and Astronautics, Sichuan University, Chengdu 610065, China (e-mail:
zhongjie_scu@outlook.com; jian.yu_wang@hotmail.com).
Yujie Zhang, Chong Luo, and Qiang Miao are with the College of Elec-
trical Engineering, Sichuan University, Chengdu 610065, China (e-mail:
zhangyj@scu.edu.cn; luochong33@foxmail.com; mqiang@scu.edu.cn).
Color versions of one or more ﬁgures in this article are available at
https://doi.org/10.1109/TR.2021.3134369.
Digital Object Identiﬁer 10.1109/TR.2021.3134369
safety and reliability of a UAV [4]. A UAV is a complex system
composed of mechanical, hydraulic, and electrical subsystems
with complex software and control modules. UAV ﬂight data are
collected by sensors, which directly reﬂect UAV ﬂight states. To
reduce property loss and environmental damage caused by UAV
accidents, it is very important to carry out anomaly detection and
recovery prediction research on UAV ﬂight data, to effectively
improve the safety and reliability of UAVs.
Anomaly detection is one of the key technologies to ensure
the safety of the system, and it refers to the problem of ﬁnding
patterns in data that do not conform to the expected behavior
[5]. Anomaly detection has a wide range of applications, such
as ﬁnance, medical treatment, industry, and the Internet [6].
Recently, data-driven methods are widely used in these appli-
cation scenarios with sufﬁcient available data. According to the
scale of algorithms in data-driven methods, it can be divided
into shallow structure and deep structure [7]. Nonparametric
learning methods, such as support vector machine (SVM) [8]–
[10], one-class SVM [11], and extended isolation forest [12],
can be regarded as shallow structure methods. The ability of
shallow structure methods to learn high-dimensional functions
is very limited. The shallow structure methods are suitable
for processing low-dimensional, small sample data. The deep
structure methods are neural networks with multiple hidden
layers, generally composed of multiple parameterized nonlin-
ear modules, such as convolutional neural networks [13], [14],
variational autoencoder [15], and generative adversarial network
[16]. The deep structure methods can perform high-level and
abstract representation of data and have strong generalization
capabilities.
Generally, there are three main objectives for anomaly de-
tection of UAV ﬂight data, which are highlighted as follows:
ﬁrst, detect anomaly in time to avoid serious consequences;
second, locate anomaly source to guide subsequent operation
and maintenance; and third, predict recovery value of anomaly
point to minimize damage caused by the anomaly. In gen-
eral, current UAV anomaly detection methods can be divided
into three categories: knowledge-based methods, model-based
methods, and data-driven methods [17], [18]. The knowledge-
based methods usually require experts in the research ﬁeld
to summarize the anomaly detection model, which includes
two processes: knowledge acquisition and knowledge engineer-
ing. Knowledge acquisition refers to obtaining solutions to
0018-9529 © 2021 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:38:52 UTC from IEEE Xplore.  Restrictions apply.

## Page 2

458
IEEE TRANSACTIONS ON RELIABILITY, VOL. 71, NO. 1, MARCH 2022
problems from experts. Knowledge engineering represents a
largeamountofknowledgeintoasetofpreciserulesthatareused
to construct an expert knowledge system. The main difﬁculty of
knowledge-based methods is that expert knowledge is difﬁcult
to obtain and express. In this aspect, a knowledge-based method
often requires time-consuming collaborative development be-
tween developers and experts [19]. Model-based methods usu-
ally require the establishment of an accurate physical model. The
residual between the estimated value and the actual measure-
ment is evaluated to determine whether an anomaly has occurred
[20]. However, a UAV is a complex system that integrates me-
chanical, electronic, hydraulic, and other parts. It is very difﬁcult
to establish a complete and accurate physical model of UAVs.
Data-driven methods received a lot of attention recently, which
beneﬁts from the rapid improvement of computing power and in-
telligent algorithms. Data-driven methods consider that data can
describe the running process and state of the system. Compared
withknowledge-basedmethodsandmodel-basedmethods,data-
driven methods do not require a large amount of expert knowl-
edge or a complicated UAV system model [18]. Data-driven
methods can be carried out directly by using ﬂight data.
A UAV is a complex system with lots of sensors, so the ﬂight
data of UAV have the characteristics of high dimensionality.
Due to the inﬂuence of the UAV structure and ﬂight process,
there is spatio-temporal correlation [21] within the ﬂight data.
The existing data-driven UAV anomaly detection methods can
be mainly divided into two categories: temporal correlation
methods and spatio-temporal correlation methods. Temporal
correlation methods consider that the ﬂight data are correlated
in the time dimension, and learn the characteristics or represen-
tations of the data only from the historical data of the detected
parameter. When the new data do not conform to the historical
characteristics or representations, it will be judged as anomaly
[2], [18], [22]. However, temporal correlation methods only
consider the correlation of the data in the time dimension, and
ignore the mutual inﬂuence of the data in the spatial dimension.
Spatio-temporal correlation methods comprehensively consider
the relationship among the data in the time dimension and the
spatial dimension, use multiparameter historical data to build
model, and fully explore the relationship among the data in
the time dimension and the space dimension. When new data
do not satisfy the relationship, it is considered as anomaly
[23]–[25]. The deep structure methods are a common way for
mining spatio-temporal correlation in data, and long short-term
memory (LSTM) occupies an important position in processing
time-series data. Benkuan et al. [23] used an LSTM model
to mine the spatio-temporal correlation in ﬂight data, but it
relies on prior knowledge in the selection of model’s input
parameters. In the absence of prior knowledge, a simple solution
is to directly select all parameters. However, there are many
parameters in UAV ﬂight data, and not all parameters in the
ﬂight data have a positive effect on results. Too many useless
parameters will lead to many problems, such as underﬁtting, the
curse of dimensionality, and excessive volume. In this article,
the correlation methods are used to mine the spatial relationship
of the ﬂight data, and the correlation analysis results are used
as the basis for selecting the input parameters of the anomaly
detection model.
Correlation analysis refers to measuring the closeness of the
correlation among the two variables. Commonly used correla-
tion analysis methods include Pearson correlation coefﬁcient
(PCC) [26], time lag correlation (TLC), dynamic time warp-
ing (DTW) [27], and maximal information coefﬁcient (MIC)
[28]. PCC is the ratio between the covariance of two variables
and the product of their standard deviations, which can only
reﬂect a linear correlation of variables. TLC is a measure of the
PCC of the misalignment of two time series, which can deﬁne
the directionality among the two variables, such as the follow
relationship. DTW is a method of calculating the path among
two variables. It can minimize the distance between the two
variablesandprocessdataofdifferentlengths.MICmeasuresthe
correlations among two variables through mutual information
and has nonlinear analysis capability. A UAV is a complex
system, and there are also complex spatio-temporal correlations
in ﬂight data. However, the existing correlation analysis methods
are weak in analyzing these correlations.
To solve the difﬁculty of choosing the parameters, and to
achieve high-precision detection and recovery value prediction,
this article proposes a spatio-temporal correlation based LSTM
(STC-LSTM) deep structure data-driven method. First, artiﬁcial
neural network correlation analysis (ANNCA) is used to pre-
liminarily reﬂect the spatio-temporal correlation within ﬂight
data and obtain the parameter sets with correlation. Second,
the STC-LSTM model is established for the parameter sets
with spatio-temporal correlation, and the mapping model among
different parameters is realized. Finally, anomaly detection
and recovery prediction are carried out based on the param-
eter set mapping model. The contributions of this article are
as follows.
1) A correlation analysis method ANNCA based on a fully
connected neural network is proposed, which solves the
difﬁcult problem of reﬂect complex and nonlinear corre-
lation in ﬂight data.
2) An STC-LSTM anomaly detection framework for UAV
ﬂight data is proposed, which includes correlation analy-
sis, anomaly detection, and recovery prediction. By using
correlation analysis as the basis of parameter selection,
the dependence on expert knowledge and the number of
model parameters are reduced effectively. STC-LSTM can
greatly improve the accuracy of anomaly detection and
provide high-precision predictive recovery values.
3) Taking the real UAV ﬂight data with high-dimensional and
complex correlation characteristics as the object, the deep
structure method is used to carry out anomaly detection
research. Meanwhile, three anomalous implantation meth-
ods are used to construct anomalous samples to verify the
effectiveness of the STC-LSTM.
The rest of this article is organized as follows. Section II
introduces the fundamental theory and STC-LSTM framework.
Section III introduces the anomaly detection and recovery pre-
diction process and experiment in detail. Section IV summarizes
the work of this article and points out the future direction.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:38:52 UTC from IEEE Xplore.  Restrictions apply.

## Page 3

ZHONG et al.: UNMANNED AERIAL VEHICLE FLIGHT DATA ANOMALY DETECTION AND RECOVERY PREDICTION
459
II. FUNDAMENTAL THEORY AND MODELING
A. Correlation Analysis
1) Linear Correlation Analysis Based on PCC: PCC is a
commonly used method for correlation analysis, which has the
characteristics of simple principle and small calculation loss.
PCC is suitable for ﬁnding linear correlation among ﬂight data,
which can be formulated as follows:
ρ(X, Y ) = Cov(X, Y )
σXσY
.
(1)
where σX and σY are the standard deviations of variables X
and Y , respectively. Cov(X, Y ) is the covariance of them in
practice. Covariance and standard deviation can only be esti-
mated from a limited number of samples. Therefore, the sample
of PCC is
rX,Y =
n
i=1
(Xi −X)(Yi −Y )

n
i=1

Xi −X
2(Yi −Y )
2
=
1
n −1
n

i=1
Xi −X
sX
 Yi −Y
sY

(2)
X = 1
n
n

i=1
Xi
(3)
sX =
	



1
n −1
n

i=1
(Xi −X)
2
(4)
where rx,y is the correlation coefﬁcient, and ¯X and ¯Y are the
mean values of the variables X and Y , respectively. n is the
number of samples. The value of rx,y is among [−1, 1] . The
closer the absolute value of rx,y to 1 is, the higher the correlation
between the variables X and Y .
2) Nonlinear Correlation Analysis Based on ANNCA: An
artiﬁcial neural network (ANN) is an algorithmic mathemati-
cal model that imitates the characteristics of an animal neural
network and carries out distributed parallel information process-
ing. An ANN is formed by stacking single-layer or multilayer
neurons. Each layer is connected by weight and bias, and the
activation function makes the ANN have the ability of nonlinear
representation. The goal of an ANN is to establish the mapping
model between the input and the output, and to minimize the
distance between the model output and the real output. The
ﬂow direction of data in the ANN contains forward propagation
and backpropagation. Forward propagation is used to pass the
information of the input to each neuron in the network. Back-
propagation is to reversely update the parameters in the model
according to the loss between the model output and the real
output. To establish the neural network model more quickly and
stably, the stochastic gradient descent method is often used for
backpropagation.
ANNCA can be divided into two parts: ANN and PCC. If
there is a correlation among two variables X
and Y , the
correlation can be expressed by Y = f(X)
or X = f(Y ) .
Fig. 1.
ANNCA structure.
Based on this idea, X and Y are taken as the input and output
of the neural network, respectively. A large number of X and Y
samples are used to train the neural network model. If the input
X without participating in the training can accurately predict
the corresponding Y , it is considered that there is a prominent
correlation between X and Y . The PCC between the model
output and the real output is used to measure this relationship.
The ANNCA framework is shown in Fig. 1.
In Fig. 1, xi is the value of variable X at time i. yi is the value
of variable Y at time i. ˆyi is the predicted value of variable Y at
time i. d is the delay length. The implementation of ANNCA is
summarized as follows. First, the input variable X and output
variable Y are, respectively, used to obtain the sample dataset by
sliding window operation. In particular, the ith sample has an
inputof[xi−d, xi+d] andanoutputofyi .Thedataof[xi−d, xi−1]
, xi , and [xi+1, xi+d], respectively, represent the past, present,
and future data of variable X at time i . Second, the dataset is
divided into training, validation, and testing sets. The training
and validation sets are used to train and adjust the ANN model
of ANNCA. The test set is used to generate ˆy from the ANN
model. Note that the samples in the test dataset need to be time-
continuous data. Finally, the PCC value between Y
and ˆY
is
calculated as the degree of correlation between variables X and
Y . The result of ANNCA is among [−1, 1]. The closer the
absolute value of result to 1 is, the higher the correlation between
the variables X and Y is.
ANNCA comprehensively considers the past, present, and
future information of two variables, which has powerful non-
linear processing capabilities and can effectively extract spatio-
temporal correlation information. Different from PCC, ANNCA
analysis results may be related to the positions of X and Y .
ANNCA analysis results of X and Y may be different from
those of Y and X .
B. Long Short-Term Memory (LSTM)
LSTM was ﬁrst proposed by Hochreiter and Schmidhuber
[29], which can be regarded as a special recurrent neural network
(RNN). Theoretically, an RNN should learn all the dependencies
from the historical data. However, with the increase of network
layers, an RNN has problems, such as gradient explosion and
gradient disappearance, so LSTM comes into being. Compared
with an RNN, the structure of LSTM is more complex. The
LSTM model often contains an input layer, an output layer, and
some hidden layers. There are many layers in the hidden layers,
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:38:52 UTC from IEEE Xplore.  Restrictions apply.

## Page 4

460
IEEE TRANSACTIONS ON RELIABILITY, VOL. 71, NO. 1, MARCH 2022
Fig. 2.
LSTM cell structure.
and each layer is composed of three gates and a storage state,
which are forget gate, input gate, output gate, and memory cell,
respectively. The structure of LSTM is shown in Fig. 2.
The forget gate is the ﬁrst to receive the information and
controls the amount of historical information ﬂowing into the
current state. Its expression is as follows:
ft = δ (Wfht−1 + Ufxt + bf) .
(5)
The input gate is used to update the current input data and
determines which data are entered into the memory cell. It can
be expressed as follows:
it = δ (Wiht−1 + Uixt + bi)
(6)
Ct = ft · Ct−1 + it · at.
(7)
The output gate controls the output of the model and the
information ﬂowing into the next hidden layer in the memory
unit of the current LSTM. It can be expressed as follows:
ot = Woht−1 + Uoxt + bo
(8)
ht = ot · tanh (Ct) .
(9)
The memory cell determines the information currently stored
and ﬂowing to the next layer. It can be expressed as follows:
at = tanh (Waht−1 + Uaxt + ba) .
(10)
In the above formulas, Wf
and Uf
represent the weights
of forget gate. Wi and Ui represent the weights of the input
gate. Wo and Uo represent the weights of output gate. Wa and
Ua represent the weights of the memory cell. bf , bi , bo , and
ba represent the bias of forget gate, input gate, output gate, and
memory cell, respectively. ht−1 represent the value of the hidden
state of the last layer. δ represent the sigmod function. xt is the
input information of the current moment.
C. Framework of Anomaly Detection Based on STC-LSTM
This article proposes an STC-LSTM framework for the de-
tection and recovery value prediction of UAV ﬂight data. The
process is shown in Fig. 3.
The speciﬁc process of STC-LSTM is as follows. First, ﬂight
data are collected from the UAV. Second, the data are prepro-
cessed. Third, ANNCA and PCC are used to mine the correlation
in ﬂight data, and to establish correlation parameter sets. The
input and the output parameters of the LSTM model are selected
according to the correlation parameters sets. Fourth, the ﬂight
data are reconstructed to make the dataset. The dataset is divided
into training, validation, and testing sets. Training and validation
sets are used to train and adjust the LSTM model. The test set
containing anomaly data is used to obtain the deﬁned range
of anomaly and to verify the performance of the STC-LSTM.
Finally, the anomaly detection and recovery prediction of UAV
ﬂight data are realized.
III. EXPERIMENT RESULTS AND ANALYSIS
A. Data Description
1) FlightDataCollection: Theexperimentaldatausedinthis
article are all collected from the actual ﬂight data of UAV, which
is shown in Fig. 4.
The UAV is a “Clouds” ﬁxed-wing airplane with a wingspan
of 1880 mm, fuselage length of 960 mm, fuselage thickness of
260 mm, weight of 850 g, payload of 600–1200 g, and cruising
speed of 50–80 km/h. The UAV ﬂight data are collected by
Pixhawk 4. The collected data include 63 sensor data, such as
pitch angle, roll angle, pitch angle rate, roll angle rate, yaw angle
rate, sky speed, airspeed, ground speed, and altitude. A total of
37 ﬂight data are collected. The maximum ﬂight time is 15 min.
The minimum is 10 min. The ﬂight tasks include take off, level
ﬂight, turn, head up, landing, and other operations.
2) Data Preprocessing: The data obtained from UAV have
some problems, such as missing value, repeated value, and
inconsistent sampling frequency. The ﬂight data need to be
preprocessed. Aiming at the problem of data missing, the linear
interpolation is used to ﬁll in the missing data. The method of
deleting repeated timestamps is used to solve the problem of
repeated records. Due to the different sensors to collect the UAV
ﬂight data, the sampling frequency is inevitably different. This
article uses the resampling method to unify the UAV ﬂight data
on the timeline, and the sampling interval of the ﬁnal sample
is 30 ms. In addition, the data need to be normalized. The data
processed through the above steps can be used for experimental
research.
3) Anomaly Injection: Under real conditions, the anomaly
in the operation of the system is rare and difﬁcult to collect.
Therefore, in the sample set, the number of normal samples is far
greater than the number of anomaly samples. However, anomaly
samples are needed to verify the STC-LSTM method. In this
article, anomaly samples are generated by injecting anomalies
in normal data. Three kinds of anomaly injection methods are
used in this article, which are deviation anomaly, static anomaly,
and drift anomaly, respectively [23], [24].
Deviation anomaly: yf(t) = y(t) + β , where β is a constant.
y(t) is normal data and t is a period of time.
Static anomaly: yf(t) = β , where β is a constant. t is a
time period. The static anomaly shows that the ﬂight data are a
constant value in a time period.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:38:52 UTC from IEEE Xplore.  Restrictions apply.

## Page 5

ZHONG et al.: UNMANNED AERIAL VEHICLE FLIGHT DATA ANOMALY DETECTION AND RECOVERY PREDICTION
461
Fig. 3.
Framework of anomaly detection based on STC-LSTM.
Fig. 4.
“Clouds” ﬁxed-wing UAV.
Point anomaly: yf(t) = y(t) + β . Different from the devia-
tion anomaly, the point anomaly occurs at multiple independent
time points, whereas the deviation anomaly occurs within a time
period.
Roll angle is one of the important parameters to reﬂect the safe
operation of UAVs. This article takes roll angle as a detected
parameter. A section of ﬂight data with a length of 25 000 is
selected as the analysis object. The normal data of roll angle
are shown in Fig. 5(a). The anomaly dataset of roll angle is
generated manually by the above anomaly injection methods.
Fig. 5(b) shows the deviation anomaly, where the anomaly range
is [7000, 20000] and anomaly degree of deviation anomaly is
the difference between the maximum and minimum of normal
data timing 0.2. Fig. 5(c) shows the static anomaly, where the
anomaly data are stuck at −7° and the range is [10200, 18500].
Fig. 5(d) shows the point anomalies, which contains 50 random
point anomaly and anomaly degree is the difference between the
maximum and minimum of normal data timing 0.2.
TABLE I
FLIGHT PARAMETERS
B. Correlation Analysis of High-Dimensional Flight Data
UAV ﬂight data contain 63 parameters, and some parame-
ters adopt the redundant design. In the analysis of correlation,
redundant parameters are removed. A total of 18 parameters
(shown in Table I) need to be analyzed for correlation. Based
on data preprocessing, PCC and ANNCA are, respectively, used
for correlation analysis of ﬂight data. The analysis results are
shown in Figs. 6 and 7.
PCC can only ﬁnd the linear correlation in data. ANNCA
can ﬁnd both linear and nonlinear correlations. The result of
PCC and ANNCA are among [−1, 1] . For the convenience of
comparison, the values of ANNCA and PCC results are taken
absolutely, respectively, so that the result is among [0, 1] .
Figs. 6 and 7, respectively, show the correlation analysis
results between PCC and ANNCA. The ﬂight parameters corre-
sponding to the serial number of coordinate axes are shown in
Table I. The values in Figs. 6 and 7 is the correlation among two
parameters, and the value is among [0, 1] . Note that a high value
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:38:52 UTC from IEEE Xplore.  Restrictions apply.

## Page 6

462
IEEE TRANSACTIONS ON RELIABILITY, VOL. 71, NO. 1, MARCH 2022
Fig. 5.
Anomaly injection. (a) normal data. (b) Implantation of bias anomaly.
(c) Implantation of static anomaly. (d) Implantation of point anomaly.
indicates a high correlation of two parameters. The results of
PCC analysis were symmetric with the main diagonal, whereas
ANNCA analysis was asymmetric. The reason is that the result
of ANNCA was related to the positional order of parameters,
whereas PCC does not need to consider the positional order of
parameters.
Generally, if the value of PCC is greater than 0.6, it is consid-
ered that the correlation among two parameters is strong. This
article uses 0.6 as the threshold for the strong correlation for PCC
and ANNCA. Comparing Figs. 6 with 7, the ﬂight parameter
pairs that have a strong correlation in the PCC results also have
a strong correlation in ANNCA. However, ANNCA contains
some correlations that do not exist in PCC, and it indicates that
ANNCA can ﬁnd more abundant correlations than PCC.
In this article, 0.6 is used as the threshold for parameter selec-
tion of ANNCA and PCC to establish the correlation parameter
TABLE II
CORRELATION PARAMETER SET OF THE ROLL ANGLE
sets. Taking the roll angle as an example, in the analysis results
of ANNCA, there are seven parameters (shown in Table II) that
have a correlation with the roll angle greater than 0.6. But in the
result of PCC, there are only two parameters (shown in Table II)
that have a correlation with the roll angle greater than 0.6. In this
article, the results of ANNCA are used to establish an anomaly
detection and recovery value prediction model. Such condition
means there are seven parameters in the correlation parameter
set of roll angle, which are pitch angle rate, roll rotation rate,
yaw angle rate, normal overload, sideslip angle, right aileron
command, and left aileron command.
The method of parameter selection using correlation anal-
ysis can effectively reduce the dependence on expert knowl-
edge. Taking UAV anomaly detection as an example, even if
researchers do not understand the speciﬁc meaning of each
ﬂight parameter and UAV system structure, they can effectively
carry out anomaly detection research on UAV ﬂight data. The
knowledge of a speciﬁc ﬁeld is abstracted through correlation
analysis and transforms into a general data analysis problem.
C. Anomaly Detection and Recovery Prediction Based on
STC-LSTM
1) Model Training With Spatio-Temporal Correlation: The
core of STC-LSTM is to establish the anomaly detection and
recovery prediction model by mining the spatio-temporal cor-
relation information of correlation parameter sets. In particular,
STC-LSTM is used to predict the current data of the detected
parameter through the historical data of correlation parameter
sets. Unlike STC-LSTM, ANNCA makes comprehensive use
of historical, present, and future ﬂight data. However, in online
anomaly detection, present and future ﬂight data cannot be used
for analysis, and only historical data can be used for analysis for
STC-LSTM.
Before training the model, the data need to be reconstructed
so that it can meet the input and output of the model. The formula
is expressed as follows:
X(t) =
⎡
⎢⎢⎢⎣
x1(t −1), x1(t −2) · · · x1(t −D)
x2(t −1), x2(t −2) · · · x2(t −D)
...
xn(t −1), xn(t −2) · · · xn(t −D)
⎤
⎥⎥⎥⎦
(11)
Y (t) = y(t)
(12)
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:38:52 UTC from IEEE Xplore.  Restrictions apply.

## Page 7

ZHONG et al.: UNMANNED AERIAL VEHICLE FLIGHT DATA ANOMALY DETECTION AND RECOVERY PREDICTION
463
Fig. 6.
Parameter sets of PCC.
Fig. 7.
Parameter sets of ANNCA.
where X(t) is the input of the model, and its dimension is n × D
. n is the number of parameters in the correlation parameter set.
D is the length of the sliding window. xn(t −1) is the data of
the correlation parameter at time t . Y (t) is the target value of
the model output. y(t) is the data of the detected parameter at
time t . The actual collected ﬂight data are made into a training
set and a test set in the form of X(t) and Y (t) . In the process of
training the model, the training set X(t) is the input of the model,
and the output ˆY (t) is obtained, which is the predicted value
of the detected parameter. The model is trained to minimize
the difference between ˆY (t) and Y (t) . This article mainly
builds the anomaly detection and recovery prediction model of
STC-LSTM based on LSTM. The model contains three LSTM
layers and two fully connected layers. The input dimension of
the model is D × n , and the output dimension is 1. The LSTM
model is shown in Fig. 8.
2) Anomaly Discrimination: This article uses the 3σ princi-
ple to locate the anomaly points [30]. First, we input X(t) (data
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:38:52 UTC from IEEE Xplore.  Restrictions apply.

## Page 8

464
IEEE TRANSACTIONS ON RELIABILITY, VOL. 71, NO. 1, MARCH 2022
Fig. 8.
LSTM model.
before the anomaly are implanted) in the test dataset into the
trained model to get ˆY (t) . Second, the residual R(t) between
ˆY (t) and Y (t) is calculated as follows:
R(t) = ˆY (t) −Y (t).
(13)
Third, the mean M and standard deviation S are calculated
as follows:
M = 1
n
n

t=1
R(t)
(14)
S =
	



1
n −1
n

t=1
(R(t) −M)2.
(15)
Finally, the allowable upper and lower limits of R(t) are
calculated as follows:
C = M + 3 × S
(16)
F = M −3 × S
(17)
where C is the upper limitation of 3σ principle. F is the lower
limitation of the 3σ principle. If R(t) is within the 3σ interval,
Y (t) is considered normal data, otherwise, Y (t) is considered
anomaly data.
3) Anomaly Detection Evaluation Criteria and Results: In
anomaly detection, the main concern is the ability of the model
to ﬁnd anomalies. In this article, false positive rate (FPR), false
negative rate (FNR), and accuracy (ACC) are used as evaluation
metrics, which are given as follows:
FPR =
FP
FP + TN
(18)
FNR =
FN
TP + FN
(19)
ACC =
TP + TN
FP + TP + TN + FN
(20)
where TN is true negative, FN is false negative, FP is false
positive, and TP is true positive. FPR is the proportion of all
anomaly data detected as normal by the model, reﬂecting the
probability that the model misses reporting when anomalies
occur in the system. Note that a small FPR indicates good
performance of anomaly detection and is desired. FNR is the
proportionofallnormaldatadetectedasanomaliesbythemodel,
reﬂecting the probability of false positives of the model when the
system is in normal operation. Note that a small FNR indicates
good performance of anomaly detection and is desired. ACC
is a comprehensive index that reﬂects the ability of the model
to make correct actions. Note that a large ACC indicates good
performance of anomaly detection and is desired.
Fig. 9 shows the results of anomaly detection using the STC-
LSTM method. The yellow line is the output of the model, which
represents the prediction value of the real output. The blue line
is the real output value of the roll angle. The pink band is the
upper and lower limit of the 3δ principle, which is distributed
on both sides of the yellow line. If the blue line is not inside the
pink band, the data are considered to be abnormal.
Fig. 9(a) shows the results of anomaly detection on normal
data. FPR is 0 in the result, indicating that STC-LSTM does not
detect normal data as anomaly. Fig. 9(b) shows the results of the
detection of the deviation anomalies. STC-LSTM detected all
13 000 deviation anomalies. Fig. 9(c) shows the results of the
detection of static anomalies detection. STC-LSTM detected
all 8300 deviation anomalies. Fig. 9(d) shows the results of
the detection of point anomalies. STC-LSTM detected all 50
deviation anomalies.
It can be seen intuitively from Fig. 9 that STC-LSTM can
accurately ﬁnd and locate data anomalies. To verify the superior-
ity and effectiveness of STC-LSTM, k nearest neighbor (KNN)
[22], support vector regression (SVR), and LSTM are selected
for comparison. KNN is the temporal correlation algorithm,
which builds an anomaly detection model by using the historical
dataofthedetectedparameters.TheinputsizeofKNNis400and
the number of neighbors is 20. There are few anomaly detection
methods only using spatial correlation in ﬂight data, and the
input parameters of SVR are selected with the results from
ANNCA. The input size of SVR is n , where n is the number of
parameters in the correlation parameter set. The output size is
1. In an LSTM method, 63 parameters are directly used to train
the LSTM model without parameter selection. In the following,
we will evaluate the four methods of STC-LSTM, LSTM, SVR,
and KNN in combination with the three metrics of FNR, FPR,
and ACC.
Table III shows the anomaly detection results of the four
algorithms. “/” represents a null value. The KNN algorithm is
a temporal correlation anomaly detection method. For instan-
taneous anomalies, such as point anomalies, the duration of
the anomaly is very short, and it has a good detection effect.
FNR, FPR, and ACC are all maintained at a good level. But for
continuous anomalies, such as static anomalies and deviation
anomalies, where the anomaly lasts for a long time, KNN cannot
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:38:52 UTC from IEEE Xplore.  Restrictions apply.

## Page 9

ZHONG et al.: UNMANNED AERIAL VEHICLE FLIGHT DATA ANOMALY DETECTION AND RECOVERY PREDICTION
465
Fig. 9.
Anomaly detection results of three types of anomaly data in our method. (a) normal data. (b) Deviation anomaly. (c) Static anomaly. (d) Point anomaly.
ﬁnd anomalies in the data. The SVR algorithm is a spatial
correlation algorithm, and its core idea is multiple regression.
For deviation anomalies, static anomalies, and point anomalies,
FPR is 2.5%, 2.0%, and 0, respectively, which indicates that
SVR has good anomaly detection capabilities. However, for
detecting data without anomalies implanted, the SVR algorithm
produces 17.3% of false detections. The LSTM method does
not execute parameter selection, and all 63 parameters are used
to train the model. For deviation anomalies, static anomalies,
and point anomalies, FNR is 0 and FPR is 1, which means that
LSTM judges all data as normal data and cannot ﬁnd anomaly
data. From the results of LSTM model training, the LSTM model
is underﬁtting due to too many parameters, and the output of the
model is always 0, which proves that the LSTM method has no
ability of anomaly detection. Compared with KNN, SVR, and
LSTM, STC-LSTM greatly improves accuracy in anomaly de-
tection. For no anomalies, point anomalies, static anomalies, and
deviationanomalies,theFNRandFPRare0andACCis1,which
means that STC-LSTM can perfectly ﬁnd anomalies in the ﬂight
data and avoid causing missed detection. Compared with LSTM,
parameters in ﬂight data of STC-LSTM are reduced by 88.7%.
STC-LSTM deﬁnes the internal relationship of ﬂight parameters
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:38:52 UTC from IEEE Xplore.  Restrictions apply.

## Page 10

466
IEEE TRANSACTIONS ON RELIABILITY, VOL. 71, NO. 1, MARCH 2022
Fig. 10.
Comparison of prediction effects between SVR and STC-LSTM.
(a) SVR recovery value prediction. (b) STC-LSTM recovery value prediction.
TABLE III
COMPARATIVE EVALUATION OF THREE METHODS:
KNN, SVR, AND STC-LSTM
and provides certain interpretability. Reducing parameters in
ﬂight data can greatly reduce the amount of calculation, and
reduce the difﬁculty of troubleshooting and maintenance.
4) Recovery Value Prediction: The anomaly detection of
UAV ﬂight data can minimize the impact of anomalies. In addi-
tion to timely detection of anomalies and accurate positioning of
TABLE IV
SVR AND STC-LSTM EVALUATION RESULTS
anomalies when anomalies occur, it is also necessary to predict
the recovery value of anomalies. The recovery value prediction
can help the operator better grasp the ﬂight status of the UAV and
execute emergency plans when an anomaly occurs. Meanwhile,
for closed-loop control of the UAV, the recovery prediction can
convert anomaly data into normal data in time. In this article, we
use mean square error (MSE) and mean absolute error (MAE) to
evaluate the ability of STC-LSTM to predict the recovery value
as follows:
MSE = 1
n
n

i=1
(ˆyi −yi)2
(21)
MAE = 1
n
n

i=1
|ˆyi −yi|
(22)
where ˆyi is the output of the model at time i , and yi are real
data. There are two valuation metrics that reﬂect the ability of
the prediction data to track the actual data. Consider that the
values of the model are normalized. The closer the value of the
three evaluations index is to 0, the better the accuracy of the
model will be.
When the detected parameter is an anomaly or completely
invalid, the recovery value of the anomaly data can be predicted
through correlation parameters. Among the above three anomaly
detection methods, SVR, LSTM, and STC-LSTM can be ex-
ploited for spatial correlation and used to recovery prediction,
but the LSTM method is underﬁtting. This article chooses SVR
and STC-LSTM to test the recovery value prediction.
Fig. 10 shows the visualization of recovery value prediction.
On the whole, both SVR and STC-LSTM algorithms can follow
the changing trend of real data. However, from a local point
of view, there is much noise in the prediction data of SVR,
which cannot accurately match the real data. In contrast to the
STC-LSTM, the degree of overlap between the predicted data
and the real data is big, the noise in the predicted data is small,
and accurate prediction can be achieved.
It can be seen from Table IV that in terms of recovery value
prediction, the three metrics of STC-LSTM are signiﬁcantly
lower than those of SVR. MSE and MAE of STC-LSTM are
0.000343 and 0.014651, respectively. Compared with SVR, the
MSE and the MAE of STC-LSTM are reduced by 92.1% and
70.0%, respectively. It shows that STC-LSTM can accurately
predict the recovery value of anomalies.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:38:52 UTC from IEEE Xplore.  Restrictions apply.

## Page 11

ZHONG et al.: UNMANNED AERIAL VEHICLE FLIGHT DATA ANOMALY DETECTION AND RECOVERY PREDICTION
467
IV. CONCLUSION
Aiming at the problem of anomaly detection and recovery
value prediction of UAV ﬂight data, this article designed an STC-
LSTM framework.
First, ANNCA was used to ﬁnd the correlation in the data
and obtain the correlation parameter set, which was used as the
basis for the selection of the input parameters of the STC-LSTM
model. Second, the STC-LSTM model was used to mine the
spatio-temporal correlations among multiple ﬂight parameters,
and the 3σ principle was used as the basis for anomaly determi-
nation. Then, three types of abnormal samples were made by the
method of anomaly injection. Finally, anomaly sample sets were
used to test the STC-LSTM method. Meanwhile, STC-LSTM
could also predict the recovery value of abnormal data.
In this article, the ﬂight data collected from a ﬁxed-wing UAV
were used for experiments. The detection results of STC-LSTM
were FPR = 0, FNR = 0, and ACC = 1 for deviation, static, and
point anomaly. For normal data, there was no false detection.
For anomaly data recovery value prediction, MSE and MAE
were 0.000343 and 0.014651, respectively, which were 92.1%
and 70.0% lower than SVR method. Compared with LSTM,
parameters of STC-LSTM were reduced by 88.7%. Through
the above-mentioned results of experiments, it was proved that
using the correlation method to select parameters could effec-
tively avoid the dependence on expert knowledge and greatly
reduce the parameters of model. Meanwhile, STC-LSTM could
accurately locate the anomalies of UAV ﬂight data and provide
high-precision recovery prediction values.
In the future, we will consider applying this method to an em-
bedded platform and organically combine it with ﬂight control
of UAV to realize real-time anomaly detection.
REFERENCES
[1] P. Dawei, “Hybrid data-driven anomaly detection method to improve UAV
operating reliability,” in Proc. Prognostics Syst. Health Manage. Conf.,
2017, pp. 1–4.
[2] W. Benkuan, C. Yafeng, L. Datong, and P. Xiyuan, “An embedded intel-
ligent system for on-line anomaly detection of unmanned aerial vehicle,”
J. Intell. Fuzzy Syst., vol. 34, no. 6, pp. 3535–3545, Jun. 2018.
[3] C. Zhang and W. Fu, “Optimal model for patrols of UAVs in power
GRID under time constraints,” Int. J. Performability Eng., vol. 17, no. 1,
pp. 103–113, Jan. 2021.
[4] Z. Heng, M. Zhenling, W. Jianyu, and M. Qiang, “Nonlinear-drifted frac-
tional Brownian motion with multiple hidden state variables for remaining
useful life prediction of lithium-ion batteries,” IEEE Trans. Rel., vol. 69,
no. 2, pp. 768–780, Jun. 20200.
[5] C. Varun, B. Arindam, and K. Vipin, “Anomaly detection: A survey,” ACM
Comput. Surv., vol. 41, no. 15, pp. 1–58, Jul. 2009.
[6] Y. Qibo, J. Xiaodong, L. Xiang, F. Jianshe, L. Wenzhe, and L. jay,
“Evaluating feature selection and anomaly detection methods of hard
drive failure prediction,” IEEE Trans. Rel., vol. 70, no. 2, pp. 749–760,
Jun. 2021.
[7] B. Yoshua and L. Yann, “Scaling learning algorithms towards AI,” Large-
Scale Kernel Mach., vol. 34, pp. 1–41, Jan. 2007.
[8] P. Afrooz, G. H. Amir, and E. Mohammad, “A data mining approach for
fault diagnosis: An application of anomaly detection algorithm,” Measure-
ment, vol. 55, pp. 343–352, Sep. 2014.
[9] S. A. Vasilis, T. W. Peter, and P. G. Michael, “Anomaly detection through
a Bayesian support vector machine,” IEEE Trans. Rel., vol. 59, no. 2,
pp. 277–286, Jun. 2010.
[10] G. Xie, S. Xie, X. Peng, and Z. Li, “Prediction of number of software
defects based on smote,” Int. J. Performability Eng., vol. 17, no. 1,
pp. 123–134, Jan. 2021.
[11] K.Gisung,L.Seungmin,andK.Sehun,“Anovelhybridintrusiondetection
method integrating anomaly detection with misuse detection,” Expert Syst.
Appl., vol. 41, pp. 1690–1700, Mar. 2014.
[12] H. Sahand, K. C. Matias, and B. J. Robert, “Extended isolation forest,”
IEEE Trans. Knowl. Data Eng., vol. 33, no. 4, pp. 1479–1489, Apr. 2021.
[13] W. Jianyu, M. Jianguo, W. Jinglin, Y. Fangfang, T. Kwok-leung, and M.
Qiang, “Fault diagnosis of electrohydraulic actuator based on multiple
source signals: An experimental investigation,” Neurocomputing, vol. 417,
pp. 224–238, Dec. 2020.
[14] M. Jianguo, W. Jianyu, W. Dong, and M. Qiang, “Lectro-hydraulic actuator
fault diagnosis with multi-channel residuals,” Measurement, vol. 180,
Aug. 2021, Art. no. 109544, doi: 10.1016/j.measurement.2021.109544.
[15] W. Tian et al., “Generative neural networks for anomaly detection in
crowded scenes,” IEEE Trans. Inf. Forensics Secur., vol. 14, no. 5,
pp. 1390–1399, May 2019.
[16] L. Ruff et al., “A unifying review of deep and shallow anomaly detection,”
Proc. IEEE, vol. 109, no. 5, pp. 756–795, May 2021.
[17] P. Dawei, N. Longqiang, K. Weixin, and S. Zhe, “UAV anomaly de-
tection using active learning and improved S3VM model,” in Proc. Int.
Conf. Sens., Meas. Data Analytics Era Artif. Intell., 2020, pp. 253–258,
doi: 10.1109/ICSMD50554.2020.9261709.
[18] W. Benkuan, W. Zeyang, L. Liansheng, L. Datong, and P. Xiyuan, “Data-
driven anomaly detection for UAV sensor data based on deep learning
prediction model,” in Proc. Prognostics Syst. Health Manage. Conf., 2019,
pp. 286–290, doi: 10.1109/PHM-Paris.2019.00055.
[19] T. Andreas, “Detecting known and unknown faults in automotive systems
using ensemble-based anomaly detection,” Knowl.-Based Syst., vol. 123,
pp. 163–173, May 2017.
[20] F. Paul, P. Rohit, S. Nisheeth, and B. J. Gary, “Model-based and data-
driven fault detection performance for a small UAV,” IEEE/ASME Trans.
Mechatronics, vol. 18, no. 4, pp. 1300–1309, May 2013.
[21] V. C. Mehmet, A. B. Ozgur, and A. F. Lan, “Spatio-temporal correlation:
Theory and applications for wireless sensor networks,” Comput. Netw.,
vol. 45, no. 3, pp. 245–259, Jun. 2004.
[22] L. Yu and D. Wenrui, “A KNNS based anomaly detection method applied
for UAV ﬂight data stream,” in Proc. Prognostics Syst. Health Manage.
Conf., 2016, pp. 1–8, doi: 10.1109/PHM.2015.7380051.
[23] W. Benkuan, L. Datong, Y. Peng, and P. Xiyuan, “Multivariate regression-
based fault detection and recovery of UAV ﬂight data,” IEEE Trans.
Instrum. Meas., vol. 69, no. 6, pp. 3527–3537, Jun. 2020.
[24] K. Azarakhsh, M. Mohammadreza, and S. Sebastian, “Automatic real-time
anomaly detection for autonomous aerial vehicles,” in Proc. Int. Conf.
Robot. Autom., 2019, pp. 5679–5685, doi: 10.1109/ICRA.2019.8794286.
[25] Z.
Chuxu
et
al.,
“A
deep
neural
network
for
unsupervised
anomaly detection and diagnosis in multivariate time series data,”
in
Proc.
33rd
AAAI
Conf.
Artif.
Intell.,
2019,
pp. 1409–1416,
doi: 10.1609/aaai.v33i01.33011409.
[26] G. Florian, C. Elizabeth, and D. Tharam, “CorrCorr: A feature selection
method for multivariate correlation network anomaly detection tech-
niques,” Comput. Secur., vol. 83, pp. 234–245, Jun. 2019.
[27] B. Zoltán and A. János, “Correlation based dynamic time warping of
multivariate time series,” Expert Syst. Appl., vol. 39, pp. 12814–12823,
Dec. 2012, doi: 10.1016/j.eswa.2012.05.012.
[28] F. Bo, Y. Wangjun, C. Xiaolong, Y. Tian, Z. Xilin, and L. Chaoshun,
“Correlation analysis and augmentation of samples for a bidirectional gate
recurrent unit network for the remaining useful life prediction of bearings,”
IEEE Sensors J., vol. 21, no. 6, pp. 7989–8001, Mar. 2015.
[29] S. Hochreiter and J. Schmidhuber, “Long short-term memory,” Neural
Comput., vol. 9, pp. 1735–1780, Nov. 1997.
[30] W. Dong, M. Qiang, and K. Rui, “Robust health evaluation of gearbox sub-
ject to tooth failure with wavelet decomposition,” J. Sound Vib., vol. 324,
pp. 1141–1157, Jul. 2009.
Jie Zhong received the B.Eng. degree in mechanical
engineering from the College of Mechanical Engi-
neering, Chengdu University of Technology, Sichuan,
China, in 2020. He is currently working toward the
M.S. degree in aerospace science and technology with
the School of Aeronautics and Astronautics, Sichuan
University, Chengdu, China.
His research interests include anomaly detection
and deep learning.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:38:52 UTC from IEEE Xplore.  Restrictions apply.

## Page 12

468
IEEE TRANSACTIONS ON RELIABILITY, VOL. 71, NO. 1, MARCH 2022
Yujie Zhang (Member, IEEE) received the B.S. de-
gree in instrumentation science and technology from
the Harbin Institute of Technology at Weihai, Weihai,
China, in 2014, and the Ph.D. degree in information
and communication engineering from the Harbin In-
stitute of Technology, Harbin, China, in 2021.
He is currently an Assistant Professor with the Col-
lege of Electrical Engineering, Sichuan University,
Chengdu, China. His current research interests in-
clude prognostics and health management, condition
monitoring, data-driven degradation modeling, and
electronic–mechanical system simulation.
Jianyu Wang received the B.Eng. degree in mechan-
ical engineering from the Chongqing Technology and
Business University, Chongqing, China, in 2017, and
the M.S. degree in aeronautical and astronautical
science and technology in 2020 from Sichuan Univer-
sity, Chengdu, China, where he is currently working
toward the Ph.D. degree in mechanical engineering
with the School of Aeronautics and Astronautics.
His research interests include mechanical fault di-
agnosis and deep learning.
Chong Luo received the B.Eng. degree in mechan-
ical engineering from the Chongqing Technology
and Business University, Chongqing, China, in 2017,
and the M.S. degree in aeronautical and astronauti-
cal science and technology from Sichuan University,
Chengdu, China, in 2021. He is currently working
toward the Ph.D. degree with the School of Electrical
Engineering, Sichuan University, Sichuan, China.
His current research interests include cyclostation-
ary analysis, mechanical fault diagnosis, and un-
manned aerial vehicle anomaly detection.
Qiang Miao (Senior Member, IEEE) received the
B.E. degree in reliability engineering and the M.S.
degree in mechanical engineering from the Beijing
University of Aeronautics and Astronautics, Beijing,
China, in 1998 and 2001, respectively, and the Ph.D.
degree in industrial engineering from the University
of Toronto, Toronto, ON, Canada, in 2005.
He is currently a Professor in prognostics and
health management with the College of Electrical
Engineering, Sichuan University, Chengdu, China. In
2011, he was selected as the New Century Excellent
Talents in University and the Reserve Candidate of Sichuan Province Academic
and Technology Leadership. In 2012, he was appointed as the Adjunct Professor
with the City University of Hong Kong. In 2013, he was selected as the Excellent
Expert of Sichuan Province with Great Accomplishments. In the past years, he
received more than 20 research grants, and authored or coauthored more than 80
research papers and holds nine patents. His current research focuses on reliability
and machinery condition monitoring and health assessment.
Dr. Miao has been a Senior Member of the IEEE Reliability Society since
2012. He was the recipient of the Ministry of Education Natural Science Award
(Second Class) in 2009.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:38:52 UTC from IEEE Xplore.  Restrictions apply.
