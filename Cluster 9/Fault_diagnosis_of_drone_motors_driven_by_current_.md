# Fault_diagnosis_of_drone_motors_driven_by_current_.pdf

## Page 1

Measurement Science and Technology
Meas. Sci. Technol. 35 (2024) 086202 (19pp)
https://doi.org/10.1088/1361-6501/ad3d00
Fault diagnosis of drone motors driven
by current signal data with few samples
Guanglin Chen1, Shaobo Li1,2,∗, Qiuchen He3,∗, Peng Zhou1, Qianfu Zhang1,
Guilin Yang1 and Dongchao Lv1
1 School of Mechanical Engineering, Guizhou University, Guiyang 550025, People’s Republic of China
2 State Key Laboratory of Public Big Data, Guizhou University, Guiyang 550025, People’s Republic of
China
3 School of Management, Guizhou University, Guiyang 550025, People’s Republic of China
E-mail: lishaobo@gzu.edu.cn and he_qiuchen@163.com
Received 23 November 2023, revised 17 March 2024
Accepted for publication 10 April 2024
Published 10 May 2024
Abstract
Multi rotor unmanned aerial vehicles (UAVs) are extensively utilized across various domains,
and the motor constitutes a pivotal element in the UAV power system. The majority of UAV
failures and crashes stem from motor malfunctions, underscoring the imperative need for
comprehensive research on fault diagnosis in UAV motors to ensure the stable and reliable
execution of flight tasks. This study focuses on quadrotor UAVs as the research subject and
devises targeted fault simulation experiments based on the structural features and operational
characteristics of the DC brushless motor used in quadrotor UAVs, specifically examining the
stator, rotor, and bearings. To address challenges related to the UAV’s own loads, limited space
for redundant parts, and the high cost and difficulty associated with installing sensors for
traditional fault diagnostic signals such as vibration and temperature, this study opts to use
current signals as a substitute. This approach resolves the issue of challenging data collection for
UAVs and investigates a current signal based fault diagnosis method for UAV motors. Lastly, in
response to the limited training samples available for fault data due to the UAV’s highly sensitive
characteristics regarding the health status of its components and flight stability, traditional
machine learning and deep learning methods encounter difficulties in identifying representative
features with a small number of training samples, leading to the risk of overfitting and reduced
model accuracy in fault diagnosis. To overcome this challenge, we propose a hybrid neural
network fault diagnosis model that incorporates a width learning system and a convolutional
neural network (CNN). The width learning system eliminates temporal characteristics from the
original current signal, capturing more comprehensive and representative sample features in the
width feature space. Subsequently, the CNN is employed for feature extraction and
classification tasks. In empirical small sample fault diagnosis experiments using current signal
data for UAV motors, our proposed model outperforms other models used for comparison.
Keywords: UAV motor, current signal, small sample learning, fault diagnosis
∗Authors to whom any correspondence should be addressed.
Original content from this work may be used under the terms
of the Creative Commons Attribution 4.0 licence. Any fur-
ther distribution of this work must maintain attribution to the author(s) and the
title of the work, journal citation and DOI.
1
© 2024 The Author(s). Published by IOP Publishing Ltd

## Page 2

Meas. Sci. Technol. 35 (2024) 086202
G Chen et al
1. Introduction
In recent years, unmanned aerial vehicle (UAV) technology
has undergone rapid development, expanding its application
scenarios and use cases. Owing to its user friendly operation,
robust scalability, and cost effectiveness, UAVs have found
widespread utilization in diverse fields such as agriculture,
plant protection [1, 2], and disaster rescue [3]. However, exten-
ded operations, challenging working environments, and delib-
erate damage can impact the overall health status of UAVs,
leading to system failures, loss of control, substantial eco-
nomic losses, and even casualties. While hardware redund-
ancy has conventionally been favored to enhance UAV flight
reliability, this approach introduces increased operational bur-
dens and manufacturing costs, it does not apply to unmanned
aircraft systems [4]. To address these challenges and reduce
costs, it is imperative to research straightforward, efficient, and
precise UAV fault diagnosis methods. The shift from hardware
redundancy to fault diagnosis involves extracting fault inform-
ation from UAV system and sensor data, analyzing the causes
of faults, and ensuring the stable and reliable execution of UAV
flight tasks [5, 6].
The mainstream fault diagnosis methods encompass three
approaches: signal analysis [7, 8], model based [9–11], and
data driven [12]. Signal based processing methods mainly
achieve fault diagnosis through some kind of information pro-
cessing and extraction of signal features, usually using sig-
nal models such as spectral analysis and wavelet transform
of correlation function to analyze their correlation signals and
determine whether a fault occurs or not, the method reduces
the dependence on mathematical models, but the lack of accur-
ate mathematical models makes it insufficient to diagnose
early potential faults. Model based methods necessitate accur-
ate physical mathematical models or prior expert knowledge.
As nonlinearity becomes more pronounced in UAV dynamics,
the enhancement of physical mathematical models is imper-
ative; otherwise, they struggle to capture and reflect nonlin-
ear characteristics. Data driven UAV fault diagnosis meth-
ods rely on the utilization of system and sensor monitor-
ing data during operation for fault diagnosis. This approach
effectively circumvents the challenges associated with sys-
tem modeling complexities and the limited a priori know-
ledge of experts. Commonly employed techniques encom-
pass multivariate statistical analysis [13], traditional machine
learning [14–16] (such as support vector machine (SVM)),
and deep learning [17, 18]. Notably, deep learning based fault
diagnosis methods harness the robust feature extraction cap-
abilities of neural networks to directly extract fault inform-
ation from raw signal data. This results in high fault dia-
gnosis accuracy and strong generalization. Guo et al [19] pro-
posed an uncertainty aware long short term memory (LSTM)
based fault diagnosis method for UAV actuator assembly.
This method excels in comparison to other models concern-
ing fault degree detection and fault type classification. It takes
into consideration the uncertainty in fault diagnostic model-
ing within the LSTM method and the variations under dif-
ferent flight conditions. Sadhu et al [20] introduced a novel
UAV fault diagnosis framework relying on deep convolu-
tional and LSTM neural networks, enabling fault diagnosis
based on actual sensor data. Al-Haddad and Jaber [21] presen-
ted a fault diagnosis scheme using a discrete wavelet with
a hybrid transform and deep neural network with multiple
hidden layers for UAV fault diagnosis and prediction. They
employed various feature selection methods to enhance the
model’s fault diagnosis capabilities. The aim was to achieve
a faster and more efficient UAV fault diagnosis method, mak-
ing the fault diagnosis timeliness align more closely with real
world scenarios. Certain existing literature combines elements
of both model based and data-driven approaches: Thanaraj
et al [22] introduced a hybrid fault diagnosis model by integ-
rating the extreme learning neuro fuzzy algorithm with exten-
ded Kalman filtering to address the challenge of identifying
undetected actuator faults in UAVs. Experimental evidence
confirmed the model’s high diagnostic efficiency and sensitiv-
ity. Song et al [23] sought to address the challenge of identify-
ing and localizing rotor faults in quadcopter UAVs, which can
be complex. They fused the extended state observer and deep
forest methodologies to enable fault diagnosis in quadcopters
of unknown fault size. Zhang et al [24] introduced a fault
detection framework based on a hybrid deep domain adaptive
BiLSTM network and Hampel filtering. The primary goal of
this framework is to leverage the collected data to detect faults
in fixed wing UAVs, even when operating under unknown
conditions.
When investigating the data driven method for diagnos-
ing faults in multirotor UAV motors, the foremost consider-
ation is the practicality of the data and the feasibility of data
acquisition. Existing sources of UAV fault diagnosis data pre-
dominantly include the UAV flight control system, vibration
signal data, acoustic signal data, and temperature signal data,
as detailed in table 1 through specific literature research. The
primary function of the flight control system is to facilitate
positioning, with a low sampling frequency in its data acquis-
ition. Multirotor UAVs derive power from motor driven pro-
pellers to execute flight tasks, and a majority of historical acci-
dents have been precipitated by failures in the UAV power
system. The motor serves as the fundamental power source
for the UAV’s propulsion system, constituting the essential
component for UAV flight. However, it is also a primary
locus for faults. When the UAV engages in in-flight tasks, the
motor’s operational speed can reach as high as 5000 r min−1
or even exceed this threshold. The flight control system is
unable to discern variations in rotational speed, rendering
the data acquired by the flight control system inadequate for
addressing the diagnostic requirements of multirotor UAV
motor faults [25]. The cost associated with sensors required
for the acquisition of vibration, sound, and temperature signal
data is prohibitively high. Additionally, the limited installa-
tion space and payload capacity of the UAV pose constraints,
making the excessive installation of supplementary sensor
modules detrimental to the UAV’s stability during flight.
During motor operation, the current signal undergoes changes
corresponding to variations in motor working conditions.
Leveraging the current signal enables real time monitoring
2

## Page 3

Meas. Sci. Technol. 35 (2024) 086202
G Chen et al
Table 1. UAV fault diagnostic data research.
Data sources
References
Characteristics
Flight control system
[13, 28–30]
Low sampling
frequency
Vibration signals
[31–36]
Sensitive to
mechanical faults,
high cost
Acoustic signals
[37–39]
Sensitive,
inconvenient to
install
Temperature signals
[27]
Sensitive, high cost,
inconvenient to
install
of the motor’s operational status, and the convenience and
low cost of the current signal collection are noteworthy.
Moreover, the sensors demonstrate high integration levels,
with many mid to high end electronic speed control sys-
tems incorporating built in current and voltage detection mod-
ules. Consequently, the investigation into UAV motor fault
diagnosis methods based on the current signal proves to be
more practical. Nevertheless, the inherent weakness of mech-
anical fault characteristics in the current signal restricts its
diagnostic efficacy, necessitating a thorough consideration in
the study of fault diagnosis methods based on current signals
[26, 27].
Most existing fault diagnosis studies based on current sig-
nals focus on industrial motors or related components [40–42].
However, UAV motors present unique challenges due to their
compact size, faster rotational speed, and frequency transitions
compared to industrial counterparts. Moreover, conventional
UAV fault diagnosis models often rely on ample training data
[43, 44]. Yet, UAV fault diagnosis poses a typical small sample
problem. This arises from the stability characteristics of UAV
flights, which primarily operate under normal conditions.
Conducting faulty flight tests is costly and perilous, while data
obtained from simulation software often fails to reflect real
world scenarios [45]. Consequently, acquiring UAV fault data
remains challenging. Traditional small sample fault diagnosis
methods such as transfer learning [46], meta learning [47], and
generative adversarial networks [30] necessitate complex pro-
cessing techniques and significant computational resources.
Moreover, authenticity concerns regarding virtual samples fur-
ther complicate the situation. These approaches are ill-suited
for addressing the need for fast and accurate UAV motor fault
diagnosis in the face of high rotational speeds and frequent fre-
quency transformations. Therefore, there is a pressing need to
develop a small sample fault diagnosis method for UAVs that
is characterized by simplicity, practicality, and swift response
based on real data.
This paper focuses on the motor of a quadrotor UAV and
investigates a data driven fault diagnosis method based on cur-
rent signals. Considering the requirements for UAV flight sta-
bility and the limited training data due to the UAV’s sensitiv-
ity to component health status, traditional machine learning
and deep learning methods struggle to identify representat-
ive features and suffer from low fault classification accuracy
when dealing with a small number of training samples [45,
48]. Treating the fault diagnosis of UAV motors as a small
sample classification problem, a hybrid neural network with
small sample learning capabilities is proposed, leveraging the
broad learning system (BLS) [49] and convolutional neural
network (CNN) [50] for the analysis of current signal data to
address the challenges of small sample fault diagnosis in UAV
motors. BLS is different from the traditional neural network
model in the ‘depth’ of the superposition of the ‘lateral expan-
sion’ approach, simple structure, fast response, strong gener-
alization, can obtain more representative features from the ori-
ginal data, and then use the CNN powerful local feature extrac-
tion capabilities, to achieve a limited sample of UAV motor
fast and accurate fault diagnosis. In the experimental section,
we compared the proposed model with traditional SVMs [51],
SVM combined with handcrafted feature extraction methods
(including db4 and sym4 wavelet packet transforms, Fourier
transforms), LSTM [52], CNN, and BLS models. This valid-
ation demonstrated the ability of the proposed model in data
driven fault diagnosis of small sample drone motor faults using
current signal data. The main contributions of this study are as
follows:
1. The paper gathers and publicly discloses a dataset of cur-
rent signals for diagnosing motor faults in quadrotor UAVs,
providing a foundational data resource for research in UAV
motor fault diagnosis.
2. Investigating a UAV motor fault diagnosis method based
on current signals as a replacement for traditional vibration
and sound signal data. The use of current signals is charac-
terized by lower acquisition costs, ease of installation, and
enhanced feasibility.
3. Based on BLS and CNN, the proposed BLSCNN fault dia-
gnosis model involves the mapping of raw current signals
by BLS, generating new representations of samples in a
wide feature space. This enriched feature space provides
CNN with more diverse characteristics. The model exhibits
superior fault diagnosis capabilities for UAV motors even
with limited training samples.
The remainder of the paper is structured as follows:
section 2 introduces the BLSCNN fault diagnosis model based
on the width learning system and CNN. Section 3 delves into
the design of fault experiments and data collection for UAV
motors. Section 4 assesses the efficacy of the proposed method
using the acquired data. Lastly, in section 5, conclusions are
drawn, and future directions are outlined.
2. Broad convolutional hybrid neural network
model
Deep learning models are renowned for their potent feature
extraction capabilities and have found extensive application
across various domains. However, these models thrive under
the assumption of having substantial training data. In the case
3

## Page 4

Meas. Sci. Technol. 35 (2024) 086202
G Chen et al
Figure 1. Network structure of the BLS.
of UAV operations, the aircraft’s flight stability is profoundly
sensitive to the condition of its actuators. Given the incap-
ability of operating for extended durations in a faulty state,
collecting a large volume of fault sample data proves to be
immensely challenging. This presents a formidable obstacle
for UAV fault diagnosis. In this paper, the challenge of UAV
fault diagnosis with limited samples is addressed by framing
it as a small sample classification problem. A hybrid neural
network model is proposed, combining the BLS and CNN to
tackle this issue.
2.1. BLS feature mapping
The BLS is a novel random weight neural network model,
introduced by Chen and Liu [49], and built upon the founda-
tion of the random vector functional link neural network [53].
In contrast to traditional neural networks, the width learn-
ing system adopts a ‘lateral expansion’ approach to elimin-
ate depth based superposition, thereby reducing the complex-
ity of the neural network model. Its straightforward structure
and swift responsiveness have led to its widespread use across
various domains [54]. The BLS primarily comprises an input
layer, a feature mapping layer, an augmentation node layer,
and an output layer. In this model, the network node weights
of the feature mapping layer and the enhancement node layer
are randomly generated. This results in a more diverse rep-
resentation of the original sample features following network
mapping. The specific network structure is illustrated in
figure 1.
The algorithmic flow of the BLS is as follows.
Assuming the sample dataset is denoted as X, it con-
sists of N samples, with each sample having M dimen-
sions represented as a matrix X ∈RN×M. The correspond-
ing labeling matrix is Y ∈RN×C. Within the feature mapping
layer of the BLS, there are n feature mapping windows, each
with K nodes. In each of these feature mapping windows,
normalized data undergoes linear mapping using a feature
mapping function φ i (i = 1, …, n). As a result, the data can
be represented as follows after feature mapping in the ith
window:
Zi = φ i (XWei + βei).
(1)
Style: The matrix Wei ∈RM×K represents a randomly gen-
erated optimal feature mapping weight matrix, which is
determined through a sparse self-encoder. Matrix βei ∈RN×1
corresponds to the randomly generated bias matrix. In prac-
tical applications, we employ matrix φ i and use linear map-
ping functions.
The results of feature mapping obtained from all n windows
are combined to form Zin = (Z1,Z2,··· ,Zn), Zin ∈RN×nk,
which serves as the output of the feature mapping layer. Zin
is then forwarded to the augmentation node layer. The struc-
ture of the augmentation node layer mirrors that of the feature
mapping layer. Assuming there are m windows and q nodes,
each window conducts nonlinear mapping using the activa-
tion function ζj(j = 1, …, m) pairs. The result of feature map-
ping for the jth window in the augmentation node layer is
given by:
Hj = ζj (ZinWhj + βhj).
(2)
Style: The matrix Whj ∈Rnk×q represents the randomly
generated node weight matrix for the augmentation layer,
while βhj ∈RN×1 is the corresponding bias matrix. The activ-
ation function ζj can be chosen from various nonlinear activ-
ation functions to effectively extract the nonlinear features
within the data.
Likewise, the results of feature mapping from the m win-
dows in the augmentation node layer are consolidated to
4

## Page 5

Meas. Sci. Technol. 35 (2024) 086202
G Chen et al
Table 2. Structural parameters of convolutional neural network.
Name
Number
of cores
Nucleus size
Output size
Imageinput
—
[T,1]
T
Conv_1
32
[5,1]
[T-4,32]
Batchnorm_1
—
—
[T-4,32]
Relu_1
—
—
[T-4,32]
Conv_2
64
[3,1]
[T-6,64]
Batchnorm_2
—
—
[T-6,64]
Relu_2
—
—
[T-6,64]
Conv_3
128
[3,1]
[T-8,128]
Batchnorm_3
—
—
[T-8,128]
Relu_3
—
—
[T-8,128]
Conv_4
128
[3,1]
[T-10,128]
Batchnorm_4
—
—
[T-10,128]
Relu_4
—
—
[T-10,128]
Fc
9
—
[9,1]
Softmax
—
—
[9,1]
Classoutput
—
—
[9,1]
derive Hjm = (H1,H2,··· ,Hm), Hjm ∈RN×mq. The final fea-
ture matrix A is obtained by merging the outcomes of the fea-
ture mapping layer Zin with the results of the augmentation
node layer Hjm,
A = (Zin|Hjm).
(3)
The network structure of the BLS is characterized by its
simplicity. Through a sequence of linear and nonlinear fea-
ture mapping processes executed by the feature mapping layer
and the augmentation node layer, the initial data is projected
into the width feature space. This minimizes the reliance on
temporal characteristics of the original samples, while simul-
taneously affording the samples more extensive and logically
sound feature variations.
2.2. CNN feature extraction
The original UAV motor current signal data exhibit clear tem-
poral characteristics. Traditional deep learning models such
as CNN and LSTM tend to depend on and extract these tim-
ing features from the original signal for feature extraction.
However, with a limited number of training samples, they
struggle to obtain representative features, leading to a dimin-
ished accuracy in fault diagnosis. In this paper, we employ
the BLS to transform the features of the original current sig-
nal data. This mapping effectively renders the sample features
independent of the time series, incorporating more varied char-
acteristics. The resultant features are then input into a one
dimensional CNN for tasks related to feature extraction and
classification. For a deeper understanding of the CNN’s the-
oretical foundations, readers can refer to the literature [50].
Assuming the number of input data features for the network is
denoted as T, the network’s structural parameters were determ-
ined through exploratory experiments, as detailed in table 2.
Figure 2. Flowchart of BLSCNN algorithm.
The CNN possesses a robust capability for local feature
extraction. The CNN used in this paper comprises four con-
volutional layers. To ensure the seamless transition of data
from one convolutional layer to the next, a batch normalization
layer is introduced after each convolutional layer. This layer
standardizes the convolutional output data, ensuring network
training stability and generalization capacity. Subsequently,
a ReLu activation layer is added to guarantee the network’s
ability for nonlinear fitting. The ReLu activation layer further
reinforces the network’s nonlinear fitting capability. Model
training is conducted using the cross entropy loss function as
the target function, thereby accomplishing the classification
task.
2.3. Fault diagnosis algorithm flow
Deep learning models are celebrated for their feature extrac-
tion capabilities, but their insatiable appetite for vast training
datasets presents a substantial hurdle when dealing with the
constraints of limited data in UAV motor fault diagnosis. In
this paper, we approach UAV motor fault diagnosis as a small
sample classification problem. Our approach begins by utiliz-
ing the BLS to map the original data’s features. This step helps
eliminate the temporal characteristics present in the original
data and projects it into a width feature space. We then lever-
age the powerful local feature extraction capabilities of the
CNN to extract features from this projected data. Our method
involves identifying the sample features within the context of
the width feature space. Training for the small sample classi-
fication task is carried out using the cross entropy loss func-
tion as the target loss function. This allows us to achieve
UAV motor fault diagnosis within a small sample background.
The flowchart of the algorithm and the overall pseudo-code
of the BLSCNN model are shown in figure 2 and table 3,
respectively.
5

## Page 6

Meas. Sci. Technol. 35 (2024) 086202
G Chen et al
Table 3. BLSCNN model pseudo code.
BLSCNN training and testing pseudocode
BLSCNN training and testing pseudocode
1. Inputs: data set, number of classifications
2. BLS: number of feature mapping layer windows n, number of
nodes k,
number of enhancement node layer windows m, number of
nodes q
CNN: loss function L, optimizer Adam, learning rate α
3. Output: Troubleshooting probability
4. Training:
5. Input normalized training data matrix X ∈RN×M
6. Broad feature mapping layer feature mapping:
7. For i = 1:n
8. Randomly generated feature mapping weights
Wei ∈RM×K βei ∈RN×1 ;
9.
Linear projection: Zi = φ i(XWei + βei)
10.
Retention Wei; βei
11. End
12. Broad augmented node layer feature mapping:
13. For j = 1:m
14.
Randomly generated feature mapping weights
Whj ∈Rnk×q; βhj ∈RN×1;
15. Non linear activation function activation
Hj = ζj(ZinWhj + βhj)
16.
Retention Whj;βhj
17. End
18. Merge the results of the feature mapping layers Zin and
augmented node layer results
Hjm: A = (Zin|Hjm)
19. Pass width feature mapping result A into CNN
20. Using the cross entropy loss function as the objective
function and setting the learning rate to 0.01
The Train convolutional neural network based on Adam
optimizer
21. Preserving Convolutional Neural Network Model
Parameters
22. End of training
23. Retention of the BLSCNN model
24. Testing:
25. Testing the fault diagnosis capability of the BLSCNN model
obtained from training
26. Investigating the performance of models with different numbers
of training samples
27. End
3. Experimental design and data acquisition for
UAV motor failure
3.1. Construction of the data acquisition system
The core components of a quadrotor UAV motor comprise
the motor casing, rotor, stator, bearings, end caps, and ter-
minals. Among these, the stator, rotor, and bearings are the
Figure 3. Data acquisition system.
primary elements responsible for electronic operation. When
the motor is in operation, the coil windings on the stator gener-
ate a magnetic field, and this magnetic field interacts with the
permanent magnets on the rotor, supplying the power neces-
sary for the rotor’s rotation. The bearings are positioned at
the ends of the motor’s rotating shaft. Their role is to reduce
heat and wear resulting from friction, in addition to providing
vibration dampening and noise reduction. This ensures that the
rotor rotates smoothly, accurately, and efficiently, ultimately
guaranteeing the stability and flight performance of the UAV
[55]. The three main modules of the stator, rotor, and bearing
are susceptible to failures, and any failure within these mod-
ules can result in reduced operational performance of the UAV
motor. Such failures may lead to increased motor temperature
and elevated vibration, and, in severe cases, affect the UAV’s
flight, potentially leading to a crash [56]. To comprehensively
investigate UAV motor failure characteristics and validate the
practical applicability of the theoretical methods proposed in
this paper, we selected the QM2812 980 kv DC brushless
motor of the F450 quadcopter UAV as our research subject. We
designed failure simulation experiments targeting the stator,
rotor, and bearings, taking into account the motor’s operational
characteristics. Data was collected at three different motor
speeds: 5000 r min−1, 5500 r min−1, and 6000 r min−1, to
verify the effectiveness of the theoretical methods across these
varying operating conditions.
Figure 3 illustrates the developed system for acquiring
fault data from the quadrotor UAV motor and the associated
fault diagnosis platform. The data acquisition system primar-
ily comprises the UAV system, Hall current sensor, constant
current source adapter, data acquisition card, and computer
host. One of the fixed three phase motor lines passes through
the Hall current sensor, which converts the motor’s current
change data into voltage signals. These voltage signals are then
transmitted to the data acquisition card. The data acquisition
card is responsible for analog to digital conversion of the cur-
rent signal and subsequently transmits the collected data to
the computer for analysis. The parameters of each component
are detailed as follows. The parameters of each component are
shown in table 4.
6

## Page 7

Meas. Sci. Technol. 35 (2024) 086202
G Chen et al
Table 4. Data acquisition system component parameters.
Name
Model number
Parameters
Quadcopter drone
motors
QM2812 980 kv type
Brushless DC motor
Rotation speed: 5,
5.5, 6 (K min−1)
Sampling frequency:
100 kHz
Motor bearings
693ZZ
Hall current sensors
WCS1800
Working supply
voltage 5 V;
Current detection
range:
DC: ±35 A;
AC: 25 A
Output mode:
Analog signal
(+A: 2.5 V ∼4.7 V;
−A: 2.5 V ∼0.3 V)
Level signal
(high level: 5 V;
low level: 0 V)
Data acquisition card HK_USB6202_S
Maximum sampling
rate: 250 KS s−1
Constant current
adapter
DK39-1
3.2. Experimental design for UAV motor failure
The stator, rotor, and bearing are critical components of UAV
motor operation, and they are also the primary modules where
faults may occur. Any failure within these modules can res-
ult in a decline in the UAV motor’s operational performance,
increased motor temperature, heightened vibration, and, in
severe instances, it may even affect the UAV’s flight, poten-
tially leading to a crash. To comprehensively investigate the
characteristics of UAV motor failures and enable accurate fault
diagnosis, this paper focuses on designing faults within these
three modules. The motor fault locations of the corresponding
modules are shown in figures 4–6.
3.2.1. Bearing fault.
Bearings installed on the drone are
positioned at both ends of the motor rotor shaft, serving the
crucial role of supporting the rotating components of the
motor. They effectively reduce heat and wear generated by
friction, while also providing damping for vibration and noise
reduction. This ensures that the motor rotor rotates smoothly,
with precision and efficiency, ultimately contributing to the
stability and flight performance of the drone. Should a bearing
experience a failure, it can lead to uneven motor rotation, noise
generation, and in more severe cases, motor damage. Given
the operational characteristics of bearings, this study simulates
wear and failures in the outer ring, cage, rolling body, and
rolling elements of the bearing at the drive end of the motor
using micro milling cutters.
3.2.2. Rotor fault.
The rotor, comprising permanent mag-
nets and the rotor shaft, is pivotal to motor functionality.
Figure 4. Bearing fault location.
Figure 5. Rotor fault location.
Figure 6. Stator fault location.
During operation, magnetic fields interact, inducing rota-
tional force in the rotor. However, motor overload caused
by high temperatures can diminish or eradicate mag-
netism in the permanent magnets. Additionally, severe
external impacts can cause rotor shaft bending, lead-
ing to axis misalignment and disrupting motor operation.
Rotor failure design encompasses external impacts result-
ing in rotor shaft bending, axis misalignment, and par-
tial demagnetization of permanent magnets due to high
temperatures.
3.2.3. Stator fault.
The stator, serving as the stationary com-
ponent of the motor, comprises a coil of copper wire wound
7

## Page 8

Meas. Sci. Technol. 35 (2024) 086202
G Chen et al
Figure 7. 5K rmp current timing signals.
within the motor casing. When current flows through the
stator, it generates a magnetic field, which interacts with the
rotor’s magnetic field to produce motor rotation. Motor over-
load, resulting in elevated temperatures, is the primary cause
of stator failure due to insulation layer breakdown in the stator
winding. This paper investigates two types of stator failures:
turn to turn short circuits within the copper coil and partial
wear of the outer connecting wire leading to interline short
circuits. Fault injection involves using a micro milling cutter
to remove the insulation layer of the wire. The specific fault
location is illustrated in the figure below.
This paper encompasses a fault simulation design for the
three key components of the UAV motor: the stator, rotor,
and bearing. To evaluate the efficacy of the proposed UAV
fault diagnosis method, vibration and three phase current sig-
nals from the motor were concurrently collected at speeds of
5 k rpm, 5.5 k rpm, and 6 k rpm under both normal and various
fault conditions.
To mitigate the impact of noise during the synchronous
operation of multiple motors, we collect the current signal
from a single motor. Simultaneously, to safeguard the motor
and ensure the experiment’s safety, the UAV motor operates
under a no load condition concerning the industrial control
blade equipment. Adhering to the sampling theorem, which
posits that for analog to digital signal conversion, a sampling
frequency exceeding twice the highest frequency in the signal
guarantees complete information retention in the digital signal.
In our study, we employ a sampling frequency of 100 kHz,
equivalent to 100 000 samples per second. With motor
operating speeds at 5000, 5500, and 6000 rpm, corresponding
to operating frequencies of 83.33 kHz, 91.67 kHz, and
100 kHz, respectively, our experimental sampling frequency
significantly surpasses the motor operating frequency. This
ensures precise sampling and reconstruction of the sig-
nal, capturing 10 000 data points for each state and
speed.
The
dataset
encompasses
the
UAV
motor
data
in
eight faulty and normal states, across three rotational
speeds. Timing diagrams for each dataset are depicted in
figures 7–9.
This study utilizes the WCS1800 Hall current sensor to
capture the current signal within the UAV motor circuit. The
sensor transforms the current signal ranging from −35 A to
35 A into a voltage signal spanning 0.3 V to 4.7 V, which
is then relayed to the signal acquisition card. Notably, when
the current signal in the circuit reaches 0 A, the Hall cur-
rent sensor outputs a consistent 2.5 V to the signal acquis-
ition card. The output voltage timing diagrams, represent-
ing the motor current signal converted by the WCS180 Hall
current sensor at three distinct rotational speeds (5000 rpm,
5500 rpm, and 6000 rpm), are depicted in figures 7–9, respect-
ively. Each figure is organized from top to bottom, showcas-
ing the timing diagrams of the current signal under nine dif-
ferent states: healthy operation, bearing support frame fail-
ure, outer ring failure, rolling body failure, inner ring fail-
ure, motor shaft bending, rotor permanent magnet demagnet-
ization, stator phase to phase short circuit, and turn to turn
short circuit. Upon examining the figures above, it is evident
8

## Page 9

Meas. Sci. Technol. 35 (2024) 086202
G Chen et al
Figure 8. 5.5K rmp current timing signals.
Figure 9. 6K rmp current timing signals.
that the UAV motor’s current signal data exhibits distinct tim-
ing characteristics, and the timing signals are similar under
various operating states. If the data driven UAV motor fault
diagnosis model is simply constructed based on the original
signal, it will exhibit an excessive reliance on the timing
characteristics of the current signal. Consequently, accurately
distinguishing the operational state of the UAV motor from
a variety of similar signals becomes challenging, and this
problem is further exacerbated when dealing with a limited
number of training samples. Addressing this challenge is a
key aspect of the experiments discussed in section 4 of this
paper.
9

## Page 10

Meas. Sci. Technol. 35 (2024) 086202
G Chen et al
Table 5. Corresponding codes for motor operating states.
Nicknames
C1
C2
C3
C4
C5
C6
C7
C8
C9
Motor status
Healthy
Cage fault
Outer
ring fault
Rolling
body fault
Inner
ring fault
Bent shaft
Loss of
magnetism
Short circuit
between
phases
Short circuit
between turns
Rotation speed
5 K, 5.5 K, 6 K
Sampling point
10 000 K
4. Experimental analysis
4.1. Experimental sample preparation and model parameter
setting
Aiming at the operating characteristics of quadrotor UAV
motors, this paper designs nine operating states, namely,
healthy operation, bearing support bracket failure, outer ring
failure, rolling element failure, inner ring failure, motor shaft
bending, rotor permanent magnet demagnetization, stator
phase to phase short circuit, and turn to turn short circuit,
which are denoted by the code names C1–C9, in order and are
shown in table 5. The current signal data of the UAV motor in
each operating state and at three operating speeds of 5k rmp,
5.5k rmp, and 6k rmp were also collected at a sampling fre-
quency of 100 kHz, resulting in a total of 27 groups of data,
with each group containing 10 000 K sample points. Samples
for model training and testing are prepared by segmenting the
data into non overlapping slices of 10 000 K sample points per
dataset. Each slice has a size of 2048 sample points and moves
one sample point per slice. The samples obtained from these
slices are then normalized to create the training and testing
sample sets.
The BLSCNN model is derived through the fusion of BLS
and CNN, with its primary characteristic being the utiliza-
tion of BLS to map features from the original current sig-
nal. Subsequently, these mapped features are conveyed to
the CNN for feature extraction and classification tasks. It is
noteworthy that the structural composition of each compon-
ent within the model mirrors that of the original model, as
detailed in section 2. The learning rate, a pivotal hyperpara-
meter in deep learning, exerts control over the model’s learn-
ing progress, influencing the network’s potential success and
the duration required to effectively locate the global minimum
for completing prediction or classification tasks. The training
efficacy of the BLSCNN model is notably influenced by the
learning rate of the CNN. Within the scope of this paper, we
initiate our discussion by conducting experiments about the
selection of CNN’s learning rate. Our investigation delves into
the impact of distinct learning rates denoted as α on the model,
all while maintaining an identical number of samples and iter-
ation steps. Specifically, when α assumes values of 0.05, 0.01,
0.005, 0.0001, and 0.0005, the nuanced variations in accuracy
and loss throughout the model training process are graphically
illustrated in figures 10 and 11.
Upon examination of figures 10 and 11, it is evident that
within identical experimental settings, an excessively large
Figure 10. Variation of accuracy during CNN training at different
learning rates.
Figure 11. Variation of loss during CNN training at different
learning rates.
learning rate (e.g. 0.05) causes the model to fail to con-
verge. Instead, it hovers around a particular value, neglect-
ing the optimal value. Conversely, a learning rate set too
small (e.g. 0.0001) leads to slow model convergence, result-
ing in instances where it falls into a local optimum and fails
to achieve optimal training results. A learning rate of 0.001
allows the CNN to converge swiftly and accurately when con-
fronted with UAV motor current data, reaching and stabilizing
at a 100% accuracy rate at the fastest rate. This paper opts for
a learning rate of 0.001 for both CNN and BLSCNN.
In addition to the CNN’s learning rate, it is imperative to
discuss and ascertain the values of several key parameters
10

## Page 11

Meas. Sci. Technol. 35 (2024) 086202
G Chen et al
Table 6. BLS parameter selection experiment results.
Name
Value
N1
20
20
20
20
50
100
N11
10
10
100
50
10
10
N2
1
1
1
1
1
1
N22
500
1000
500
500
500
500
Time
0.130
0.240
0.925
0.522
0.136
0.466
Accuracy (%)
86.56
82.89
86.11
87.11
85.22
86.56
Precision (%)
86.87
83.65
86.16
87.14
85.31
86.70
Recall (%)
86.56
82.89
86.11
87.11
85.22
86.56
F1 (%)
86.52
82.72
86.12
87.13
85.26
86.61
for the BLS model: the number of feature mapping windows
N1, the number of feature mapping nodes N11 per feature
mapping window, the fixed number of enhancement windows
N2 (set to 1 in this paper), and the number of enhancement
nodes N22. These parameters collectively define the complex-
ity and computational accuracy of the BLS model. An overly
simplistic model is vulnerable to interference and noise, which
does not align with practical requirements. Drawing upon
insights from BLS and exploratory experiments, this paper ini-
tially sets N1, N11, and N22 to 10, 20, and 500, respectively.
Subsequently, the model’s performance is evaluated as each
parameter increases, with the experimental results presented
below.
Combined with the algorithmic process and theoretical for-
mulas of the BLS model, it is evident that the number of feature
mapping windows and the number of feature mapping nodes
per feature mapping window correspond to the degree of lin-
ear mapping of the original signal data and the dimensional-
ity of the features after mapping, respectively. Additionally,
the number of enhancement nodes represents the dimension-
ality of the nonlinear mapping and the dimensionality after
activation. In the experimental results presented in table 6, we
augmented the number of windows or nodes in both the lin-
ear and activation parts of the BLS model’s nonlinear map-
ping. Consequently, the model became more complex, result-
ing in longer test completion times, and exhibited significant
enhancements across all fault diagnosis indicators. This con-
firms that the parameters utilized in this paper are suitable for
fault diagnosis experiments on UAV motor current signals.
Table 7 presents the other model parameters and algorithms
used for comparing them, where the parameters of the
BLSCNN align with those of the BLS and CNN models.
Similarly, the parameters of the SVM model, when combined
with db4, sym4 wavelet packet transform, and Fourier trans-
form for classification tasks, remain consistent with those of
the standalone SVM model.
4.2. Analysis of experimental results
To assess the model’s fault diagnosis capability in the context
of limited samples, this study examines the impact of vary-
ing numbers of training samples on the model’s performance
at three operational speeds: 5k rmp, 5.5k rmp, and 6k rmp,
Table 7. Main parameters of BLSCNN model components.
Model
Name
Value
BLS
Number of feature mapping
layer windows
10
Number of nodes in the feature
mapping layer
20
Enhanced node layer window
count
1
Number of nodes in the
enhanced node layer
500
CNN
Learning rate
1 × 10−3
L2 regularization parameter
1 × 10−4
LSTM
Hidden layer node count
500
Learning rate
1 × 10−3
SVM
Classification method
Multiclass
classification
Kernel function
RBF
WPT + SVM
Db4
8 layers
Sym4
8 layers
FFT + SVM
Length of Fourier transform
2048
using the prepared samples. The prepared samples were cat-
egorized based on rotational speed into three groups, each
encompassing data from the nine motor states (C1–C9). From
each category within each group, random samples (N = 10,
20, 50, 80, 100, 300, 500, 800, 1000, 2000) were selected
for the training set using non repeated random sampling from
the dataset. Additionally, 100 samples were randomly chosen
from each category to form the test set, ensuring that the
test set samples did not overlap with those in the training
set. The neural network models used for comparison in this
paper include SVM, Db4 WPT + SVM, Sym4 WPT + SVM,
FFT + SVM, LSTM, BLS, and CNN. SVM, a commonly
used classification model in machine learning, is among the
models considered. In addition to a standalone SVM model,
this paper also investigates commonly used handcrafted fea-
ture extraction methods, including wavelet packet transform
and Fourier transform combined with SVM. LSTM and CNN,
belonging to the realm of deep learning methods, exhibit dis-
tinctive characteristics: LSTM is sensitive to temporal data and
boasts robust temporal feature extraction capabilities, while
CNN excels in local feature extraction. This study introduces a
novel approach by combining BLS feature mapping with CNN
feature extraction, resulting in a simplified BLSCNN model
tailored for fault diagnosis in the context of small samples. The
experiment is repeated five times for each model used, and the
average accuracy is calculated as the experimental result. The
specific experimental results are as follows.
Figures 12–14 illustrate the outcomes of the explorat-
ory experiments regarding the influence of various sample
sizes on the model’s fault diagnosis capabilities at three rota-
tional speeds: 5 K, 5.5 K, and 6 K, respectively. The table
presents the classification accuracy of each model with vary-
ing numbers of training samples, while the bar chart visually
11

## Page 12

Meas. Sci. Technol. 35 (2024) 086202
G Chen et al
Figure 12. Classification accuracy of the model with different numbers of training samples at 5 K rpm.
Figure 13. Classification accuracy of the model with different numbers of training samples at 5.5 K rpm.
12

## Page 13

Meas. Sci. Technol. 35 (2024) 086202
G Chen et al
Figure 14. Classification accuracy of the model with different numbers of training samples at 6 K rpm.
represents the tabulated information. Figure 15 presents a line
graph depicting the classification accuracy of each model as
a function of the number of samples across three rotational
speeds.
A noticeable disparity in classification accuracy among
models becomes apparent when dealing with a limited num-
ber of training samples. Remarkably, the WPT + SVM model,
incorporating Db4 and Sym4 wavelets, and the proposed
BLSCNN model exhibit considerably higher classification
accuracy compared to other models, surpassing 50% even with
only 10 training samples. However, the WPT + SVM model
is found to be less sensitive to an increase in training samples
compared to the BLSCNN model. Specifically, the BLSCNN
model achieves a rapid 90% classification accuracy when the
training samples reach 300. The gap in classification accuracy
among models diminishes as the number of training samples
increases to 300. Progressing from 10 to 80 training samples,
the BLSCNN model attains 90% accuracy more swiftly, and
the gap among models further narrows as the number of train-
ing samples reaches 300.
Moreover, the rate of accuracy improvement stabilizes
with a continued increase in training samples, indicating the
gradual release of the model’s feature extraction capability.
Notably, when the number of training samples reaches 1000
or even 2000, the gap in classification accuracy among models
becomes less than 5%. The WPT + SVM model demonstrates
less sensitivity to an increase in sufficient training samples
compared to the BLSCNN model. The SVM model, in general,
performs less favorably than other models under ample train-
ing samples. This combination of manual feature extraction
and machine learning typically requires intricate and rigorous
feature extraction engineering to reach a higher upper limit.
Throughout these experiments, the BLSCNN model consist-
ently exhibits the highest classification accuracy across all
three speeds.
Additionally, a notable finding in the experiment is the
subpar performance of the FFT + SVM model compared to
the original SVM model across various numbers of training
samples. This discrepancy arises from the fact that, during nor-
mal operation of the UAV motor, the circuit current maintains a
fixed operating frequency. The fault experiments in this study
involve introducing fault frequencies of each component onto
the fixed operating frequency of the current. As the fault fre-
quency weakens, analyzing faults from the frequency domain
results in inherent challenges, as the circuit’s current operating
frequency domain dominates the fault frequency domain fea-
tures, making feature extraction challenging. Consequently,
FFT + SVM, when approaching fault diagnosis from a fre-
quency perspective, yields inferior results.
Of the other algorithmic models used to compare, LSTM is
a typical deep learning method for extracting temporal signal
features from data. It places a strong emphasis on capturing
the overall temporal characteristics of the data. When deal-
ing with UAV motor current signals, LSTM requires a larger
amount of training data to accurately distinguish feature differ-
ences between different classes. In comparison, CNN also falls
within the realm of deep learning, but it specializes in local
feature extraction. CNN assigns greater significance to local-
ized features and relies less on the overall temporal charac-
teristics of the samples when compared to LSTM. Therefore,
13

## Page 14

Meas. Sci. Technol. 35 (2024) 086202
G Chen et al
Figure 15. Line graph of model classification accuracy with sample
size at each speed.
with the same number of training samples, CNN excels in cap-
turing and identifying a wider range of diverse features, con-
sistently achieving higher classification accuracy compared to
LSTM.
However, in all experiments, CNN consistently performed
worse than the BLSCNN model. For instance, when using 10
samples for training, the classification accuracy of CNN stood
at 51.89%, 45.24%, and 35.84% at 5 K, 5.5 K, and 6 K RPMs,
respectively. This accuracy was notably lower than that of
BLSCNN by margins of 3.8%, 12.87%, and 17.27%. As the
number of training samples increased, the performance gap
between CNN and BLSCNN persisted. It was only after the
number of training samples exceeded 500 that the gap gradu-
ally diminished to less than 5%. This trend continued until
the number of training samples reached 2000, at which point
BLSCNN still exhibited slightly superior performance com-
pared to CNN.
Interestingly, BLS consistently underperforms in compar-
ison to the other models as the number of training samples
increases. It ranks at the bottom of the list among the several
methods used. This can be attributed to the simpler structure
of BLS, which was originally designed to address the chal-
lenge of training deep learning models with vast amounts of
data. However, it cannot effectively select and extract features
when confronted with a limited number of training samples.
In this paper, we present an alternative perspective on BLS
as a method for rapidly processing temporal data. Leveraging
BLS, the original current signal timing data is transformed
into a broader feature space, and CNN is employed to perform
feature extraction and classification tasks. As a result, we pro-
pose a UAV motor fault diagnosis model based on BLSCNN.
The feature mapping layer of BLS comprises multiple win-
dows, each containing multiple neural network nodes. This
multilevel parallel network structure allows BLS to analyze
the complex structure and characteristics of the data from vari-
ous perspectives. Unlike traditional methods such as FFT or
wavelet packet transforms, which rely on linear transforma-
tion for feature extraction, BLS utilizes activation functions
in the augmentation node layer to perform nonlinear mapping
of linear mapping results. This parallel multi angle mapping
nonlinear feature enhancement approach empowers BLS with
the capability for both linear and nonlinear feature extrac-
tion. The experimental findings indicate that the process of
initially subjecting the original current timing signal data to
BLS feature mapping, followed by input into CNN, serves to
substantially reduce CNN excessive reliance on timing char-
acteristics for identification. In the expanded feature space,
the samples exhibit a more reasonable and diverse set of fea-
tures. Consequently, even with a limited number of samples,
it becomes possible to capture the majority of characteristics
shared by the same type of samples. When combined with
CNN feature extraction and classification capabilities, this
approach enables BLSCNN to outperform CNN with a small
number of training samples, even surpassing the performance
of other methods used for comparison.
For a more detailed exploration of each model’s ability to
accomplish fault diagnosis tasks based on UAV motor cur-
rent signals, this paper presents the confusion matrix for the
test results of each model using 80 training samples for visual
analysis (notably, BLSCNN achieves an accuracy close to or
reaching 90% with 80 training samples). Figure 16 displays
the confusion matrices for test results at three different speeds.
From left to right the working speeds are 5K, 5.5K, 6K.
In the series of confusion matrix sets displayed in figure 16,
blue squares represent correct classifications, while orange
squares represent incorrect classifications, with the numbers
within the squares indicating the count of classified samples.
The darkness of the square corresponds to the magnitude of
the count, with darker colors indicating a higher number of
samples. Upon inspecting the confusion matrix group in the
figure, it becomes evident that SVM, LSTM, and BLS rarely
achieve a perfect classification for C1–C9 (where a square on
the diagonal shows a 100% correct classification in blue, while
the horizontal and vertical squares represent 0% correct clas-
sification). This is attributed to the limited feature extraction
14

## Page 15

Meas. Sci. Technol. 35 (2024) 086202
G Chen et al
Figure 16. Confusion matrix of test results for each model at each rotational speed for 80 training samples.
15

## Page 16

Meas. Sci. Technol. 35 (2024) 086202
G Chen et al
Table 8. Comparison of time on test sets for each model (unit:
seconds).
5k
5.5k
6k
SVM
0.5257
0.3828
0.4280
Db4 WPT + SVM
42.6249
44.1019
39.9376
Sym4 WPT + SVM
43.0309
43.7414
44.1417
FFT + SVM
0.8388
0.466
0.7846
LSTM
0.0750
0.0862
0.0810
BLS
0.0721
0.0863
0.0981
CNN
0.5827
0.5596
0.5743
BLSCNN
0.1463
0.1520
0.1247
capabilities of BLS when working with a small number of
training samples. Regarding SVM, the training samples are not
adequately representative of the entire dataset. Consequently,
SVM struggles to grasp the intricate structure of the data, res-
ulting in difficulty when identifying accurate decision bound-
aries over sufficiently large intervals. The traditional manual
feature extraction combined with SVM has a low upper model
limit. As a result, their classification effectiveness diminishes
when confronted with new data. LSTM encounters a similar
issue, wherein its heavy reliance on and extraction of tem-
poral features hinder its ability to discern representative and
distinctive features when only a limited number of samples
are accessible.
The confusion matrices for CNN and BLSCNN indicate
their capability to precisely classify the types of faults related
to the current in the motor signals (C8–C9). When diag-nosing
mechanical component faults based on the current signals,
which exhibit weak variability, the model must possess a
robust feature extraction and recognition capability of CNN
and BLSCNN, it is evident that the most significant differ-
ence in the experimental results lies in their ability to identify
mechanical faults (C2–C7). BLSCNN conducts feature extrac-
tion, classification, and identification from the BLS feature
space, thereby avoiding excessive dependence on the tem-
poral characteristics of the original signals. It can effectively
identify mechanical faults with weaker transformations in the
current signals. The classification performance for C3 and C4
is slightly poorer than for other categories, but this limitation
is also overcome by the increase in the number of training
samples.
Moreover, during UAV flight operations, its sensitivity to
the health status of each power system component is crucial.
If it fails to promptly detect and identify faults, thereby signal-
ing the operator to return for maintenance, it may lead to cata-
strophic crashes, resulting in significant economic losses and
endangering lives. In this study, each trained model was evalu-
ated with 80 training samples, and the recognition time for new
test data was compared. There are 100 test data samples for
each motor’s operating state, totaling 900 test data points. The
specific experimental results obtained are presented in table 8
and figure 17. The better experimental results are bolded in
table 8.
The LSTM and BLS models exhibit significantly shorter
processing
times,
mainly
because
LSTM
features
are
Figure 17. Histogram of time spent on test data for each model.
simplistic time series characteristics, and the BLS model
boasts a straightforward structure. However, both of these
models have notably lower fault diagnosis accuracy compared
to the BLSCNN model (refer to figures 12–14). While the tra-
ditional manual extraction and SVM combination of methods
feature extraction requires a lot of time, which can be seen
in figure 14 (because the gap with other methods models is
too large to show uniformly, the specific values are labeled
in the figure). In the BLSCNN model proposed in this paper,
the CNN component is responsible for feature extraction from
the data after BLS feature mapping, resulting in lower dimen-
sional yet more diverse and distinctive features. This makes
it outperform traditional CNN in terms of response time and
accuracy. In the BLSCNN model introduced here, the CNN
part extracts features from data after BLS feature mapping,
which has lower dimensions and more diverse, distinguishable
features, surpassing traditional CNN in terms of response time
and accuracy. Furthermore, the response and recognition times
for individual pieces of test data at three rotational speeds are
1.62 × 10−4 s, 1.68 × 10−4 s, and 1.38 × 10−4 s, respectively,
satisfying the practical response time requirements.
In summary, this paper presents a study on UAV motor fault
diagnosis driven by current signals. The challenges arise from
the limited availability of research data due to the UAV’s flight
stability characteristics and its sensitivity to the health of its
internal components. This limitation results in a constrained
number of samples available for training. Traditional SVM
struggles to find decision boundaries with significant margins,
potentially leading to suboptimal classification performance
on new data. LSTM and CNN both exhibit varying degrees
of dependence on the timing characteristics of the original
signal for feature extraction. In this scenario, when dealing
with a limited number of training samples, the representative-
ness of the samples is compromised. Consequently, it becomes
challenging to capture the underlying structural characterist-
ics of the data, resulting in lower classification accuracy. In
this paper, BLS is used as a fast response feature mapping
method to map the original timing signal into the width fea-
ture space to obtain richer and more representative features,
which effectively avoids the dependence of CNN on the tim-
ing features of the original signal, and the BLSCNN model
16

## Page 17

Meas. Sci. Technol. 35 (2024) 086202
G Chen et al
obtained by combining BLS and CNN outperforms the mod-
els used for the comparison with the same number of train-
ing samples; meanwhile, the response time of this model to
face the new test data meets the requirements of practical
use.
5. Conclusions and future work
When researching data driven multi rotor UAV motor fault
diagnosis methods, current signals are undoubtedly based on
feasibility and practicality when compared to commonly used
data such as flight control system, sound, and temperature.
This paper initially designs fault simulation experiments to
mimic the structure and operational characteristics of UAV
motors. It collects relevant current signal data, laying the
foundation for research on UAV motor fault diagnosis meth-
ods, particularly in the context of limited sample availability.
To tackle the challenges related to fault data acquisition diffi-
culties, limited data availability, and low diagnosis accuracy,
this paper introduces a hybrid neural network model that com-
bines BLS and CNN. Initially, BLS is employed to perform
feature mapping on the original current signal data, extracting
more representative sample features within a broader feature
space. Subsequently, CNN is utilized for feature extraction and
fault diagnosis tasks. The proposed model features a simple
structure and quick response times. Experimental results have
demonstrated that, by utilizing BLS for feature mapping on
the original current signal data, over reliance on and extraction
of time domain features by CNN is reduced. Consequently,
CNN can extract more representative and distinguishable fea-
tures even from a limited number of samples, enhancing its
fault diagnosis capabilities compared to SVM, manual feature
extraction combined with SVM, LSTM, and standalone CNN
or BLS models. Additionally, the response and recognition
time for new test data is considerably lower than that of tradi-
tional CNN, presenting a practical and straightforward theor-
etical approach for researching motor fault diagnosis in multi
rotor UAVs.
The research presented in this paper focuses on unloaded
paddle scenarios, which deviate somewhat from actual UAV
motor operating conditions. Our future research endeavors
will explore methods for UAV motor fault diagnosis under
load, hover, and flight conditions while ensuring safety.
Additionally, it is important to note that faults in multi rotor
UAVs are not confined solely to motors, and occurrences
of faults are not always isolated. Therefore, synchronously
considering faults across various UAV system components is
essential. Addressing this challenge involves developing meth-
odologies for identifying and detecting multi fault scenarios
when multiple faults occur simultaneously, requiring in depth
research and analysis.
Data availability statement
All data that support the findings of this study are included
within the article (and any supplementary files).
The dataset collected and utilized in this paper has been
publicly released on GitHub for research purposes. The spe-
cific URL can be found at: https://github.com/Guanglinchen1/
Quadcopter-Motor-Operation-Status-Current-Dataset.
It
is
intended for research use only, and any organization or indi-
vidual using the dataset should acknowledge its source and
cite this article.
Acknowledgments
Grateful acknowledgments are extended to the individuals and
organizations who have contributed to the completion of this
article. Special thanks to the experts and scholars for their
valuable insights and suggestions during the writing and pub-
lication of this paper.
Funding
This work was supported by the National Key Research
and
Development
Program
of
China
(Project
No.
2020YFB1713300) and the Qiankehe platform talents (Project
No. GHB [2023]001).
Conflict of interest
The authors declare no conflict of interest.
ORCID iD
Guanglin Chen https://orcid.org/0009-0002-3229-2370
References
[1] Maes W H and Steppe K 2019 Perspectives for remote sensing
with unmanned aerial vehicles in precision agriculture
Trends Plant Sci. 24 152–64
[2] Zheng Q, Lin N, Fu D, Liu T, Zhu Y, Feng X and Ruan J 2023
Smart contract-based agricultural service platform for drone
plant protection operation optimization
IEEE Int. Things J. 10 21363–76
[3] Chowdhury S, Emelogu A, Marufuzzaman M, Nurre S G and
Bian L 2017 Drones for disaster response and relief
operations: a continuous approximation model Int. J. Prod.
Econ. 188 167–84
[4] Saied M, Shraim H and Francis C 2023 A review on recent
development of multirotor UAV fault-tolerant control
systems IEEE Aerosp. Electron. Syst. Mag. pp 1–30
[5] Liu Z, Wang L, Song Y, Dang Q and Ma B 2022 Fault
diagnosis and accommodation for multi-actuator faults of a
fixed-wing unmanned aerial vehicle Meas. Sci. Technol.
33 075903
[6] Fourlas G K and Karras G C 2021 A survey on fault diagnosis
and fault-tolerant control methods for unmanned aerial
vehicles Machines 9 197
[7] Tiwari P and Upadhyay S H 2021 Novel self-adaptive
vibration signal analysis: concealed component
decomposition and its application in bearing fault diagnosis
J. Sound Vib. 502 116079
[8] Attoui I, Oudjani B, Boutasseta N, Fergani N, Bouakkaz M-S
and Bouraiou A 2020 Novel predictive features using a
17

## Page 18

Meas. Sci. Technol. 35 (2024) 086202
G Chen et al
wrapper model for rolling bearing fault diagnosis based on
vibration signal analysis Int. J. Adv. Manuf. Technol.
106 3409–35
[9] Ding S X 2008 Model-Based Fault Diagnosis Techniques:
Design Schemes, Algorithms, and Tools (Springer) (https://
doi.org/10.1007/978-3-540-76304-8)
[10] Wang B, Peng X, Jiang M and Liu D 2020 Real-time fault
detection for UAV based on model acceleration engine
IEEE Trans. Instrum. Meas. 69 9505–16
[11] Freeman P, Pandita R, Srivastava N and Balas G J 2013
Model-based and data-driven fault detection performance
for a small UAV IEEE/ASME Trans. Mechatronics
18 1300–9
[12] Jieyang P, Kimmig A, Dongkun W, Niu Z, Zhi F, Jiahai W,
Liu X and Ovtcharova J 2023 A systematic review of
data-driven approaches to fault diagnosis and early warning
J. Intell. Manuf. 34 3277–304
[13] Zhang X, Luo H, Li K and Kaynak O 2022 Time-domain
frequency estimation with application to fault diagnosis of
the unmanned aerial vehicles’ blade damage IEEE Trans.
Ind. Electron. 69 5257–66
[14] Liang S, Zhang S, Huang Y, Zheng X, Cheng J and Wu S 2022
Data-driven fault diagnosis of FW-UAVs with consideration
of multiple operation conditions ISA Trans. 126 472–85
[15] Dutta A, Niemiec R, Kopsaftopoulos F and Gandhi F 2023
Machine-learning based rotor fault diagnosis in a
multicopter with strain data AIAA J. 61 1–13
[16] Nie W, Han Z-C, Li Y, He W, Xie L-B, Yang X-L and Zhou M
2022 UAV detection and localization based on
multi-dimensional signal features IEEE Sens. J. 22 5150–62
[17] Guo D, Zhong M, Ji H, Liu Y and Yang R 2018 A hybrid
feature model and deep learning based fault diagnosis for
unmanned aerial vehicle sensors Neurocomputing
319 155–63
[18] Ahmad M W, Akram M U, Ahmad R, Hameed K and
Hassan A 2022 Intelligent framework for automated failure
prediction, detection, and classification of mission critical
autonomous flights ISA Trans. 129 355–71
[19] Guo K, Wang N, Liu D and Peng X 2023 Uncertainty-aware
LSTM based dynamic flight fault detection for UAV
actuator IEEE Trans. Instrum. Meas. 72 1–13
[20] Sadhu V, Anjum K and Pompili D 2023 On-board
deep-learning-based unmanned aerial vehicle fault cause
detection and classification via FPGAs IEEE Trans. Robot.
39 3319–31
[21] Al-Haddad L A and Jaber A A 2023 An intelligent fault
diagnosis approach for multirotor UAVs based on deep
neural network of multi-resolution transform features
Drones 7 82
[22] Thanaraj T, Low K H and Ng B F 2023 Actuator fault
detection and isolation on multi-rotor UAV using extreme
learning neuro-fuzzy systems ISA Trans. 138 168–85
[23] Song J, Shang W, Ai S and Zhao K 2022 Model and
data-driven combination: a fault diagnosis and localization
method for unknown fault size of quadrotor UAV actuator
based on extended state observer and deep forest Sensors
22 7355
[24] Zhang Y, Li S, He Q, Zhang A, Li C, Liao Z and Caraffini F
2023 An intelligent fault detection framework for FW-UAV
based on hybrid deep domain adaptation networks and the
Hampel filter Int. J. Intell. Syst. 2023 1–19
[25] Namuduri S, Narayanan B N, Davuluru V S P, Burton L and
Bhansali S 2020 Review—deep learning methods for
sensor based predictive maintenance and future perspectives
for electrochemical sensors J. Electrochem. Soc.
167 037552
[26] Gu F, Shao Y, Hu N, Naid A and Ball A D 2011 Electrical
motor current signal analysis using a modified bispectrum
for fault diagnosis of downstream mechanical equipment
Mech. Syst. Signal Process. 25 360–72
[27] Hoang D T and Kang H J 2020 A motor current signal-based
bearing fault diagnosis using deep learning and information
fusion IEEE Trans. Instrum. Meas. 69 3325–33
[28] Guo Y, Ning W and Wan F 2020 Deep belief net-based fault
diagnosis of flight control system sensors J. Phys.: Conf.
Ser. 163 1
[29] Taimoor M, Lu X, Maqsood H and Sheng C 2023 A novel
fault diagnosis in sensors of quadrotor unmanned aerial
vehicle J. Ambient Intell. Humaniz. Comput. 14 14081–99
[30] He K, Yu D, Wang D, Chai M, Lei S and Zhou C 2022 Graph
attention network-based fault detection for UAVs with
multivariant time series flight data IEEE Trans. Instrum.
Meas. 71 1–13
[31] Jiang F, Yu F, Du C, Kuang Y, Wu Z, Ding K and He G 2023 A
novel dual attention convolutional neural network based on
multisensory frequency features for unmanned aerial
vehicle rotor fault diagnosis IEEE Access 11 99950–60
[32] Du C, Zhang X, Zhong R, Li F, Yu F, Rong Y and Gong Y
2022 Unmanned aerial vehicle rotor fault diagnosis based
on interval sampling reconstruction of vibration signals and
a one-dimensional convolutional neural network deep
learning method Meas. Sci. Technol. 33 065003
[33] Ghalamchi B, Jia Z and Mueller M W 2020 Real-time
vibration-based propeller fault diagnosis for multicopters
IEEE/ASME Trans. Mechatronics 25 395–405
[34] Baldini A, Felicetti R, Ferracuti F, Freddi A, Iarlori S and
Monteri`u A 2023 Real-time propeller fault detection for
multirotor drones based on vibration data analysis Eng.
Appl. Artif. Intell. 123 106343
[35] Ambroziak L, Ołdziej D and Koszewnik A 2023 Multirotor
motor failure detection with piezo sensor Sensors 23 1048
[36] Xiao Y, Shao H, Wang J, Yan S and Liu B 2024 Bayesian
variational transformer: a generalizable model for rotating
machinery fault diagnosis Mech. Syst. Signal Process.
207 110936
[37] Altinors A, Yol F and Yaman O 2021 A sound based method
for fault detection with statistical feature extraction in UAV
motors Appl. Acoust. 183 108325
[38] Veras F C, Lima T L V, Souza J S, Ramos J G G S, Lima
Filho A C and Brito A V 2019 Eccentricity failure detection
of brushless DC motors from sound signals based on
density of maxima IEEE Access 7 150318–26
[39] Bondyra A, Kołodziejczak M, Kulikowski R and Giernacki W
2022 An acoustic fault detection and isolation system for
multirotor UAV Energies 15 3955
[40] Segovia Ramírez I, Das B and García Márquez F P 2022 Fault
detection and diagnosis in photovoltaic panels by
radiometric sensors embedded in unmanned aerial vehicles
Prog. Photovolt., Res. Appl. 30 240–56
[41] Eren L, Ince T and Kiranyaz S 2019 A generic intelligent
bearing fault diagnosis system using compact adaptive 1D
CNN classifier J. Signal Process. Syst. 91 179–89
[42] Cheng F, Qu L, Qiao W, Wei C and Hao L 2019 Fault
diagnosis of wind turbine gearboxes based on DFIG stator
current envelope analysis IEEE Trans. Sustain. Energy
10 1044–53
[43] Jiang H, Shao H, Chen X and Huang J 2017 Aircraft fault
diagnosis based on deep belief network Int. Conf. on
Sensing, Diagnostics, Prognostics, and Control (SDPC)
(IEEE) pp 123–7
[44] Miao J, Wang J, Wang D and Miao Q 2021 Experimental
investigation on electro-hydraulic actuator fault diagnosis
with multi-channel residuals Measurement 180 109544
[45] Xiong P, Li Z, Li Y, Huang S, Liu C and Gu F 2023 Fault
diagnosis of UAV based on adaptive Siamese network with
limited data IEEE Trans. Instrum. Meas. 72 1–11
18

## Page 19

Meas. Sci. Technol. 35 (2024) 086202
G Chen et al
[46] Li C, Li S, Wang H, Gu F and Ball A D 2023 Attention-based
deep meta-transfer learning for few-shot fine-grained fault
diagnosis Knowl.-Based Syst. 264 110345
[47] Luo J, Shao H, Lin J and Liu B 2024 Meta-learning with
elastic prototypical network for fault transfer diagnosis of
bearings under unstable speeds Reliab. Eng. Syst. Saf.
245 110001
[48] Li C, Li S, Zhang A, Yang L, Zio E, Pecht M and Gryllias K
2022 A Siamese hybrid neural network framework for
few-shot fault diagnosis of fixed-wing unmanned aerial
vehicles J. Comput. Des. Eng. 9 1511–24
[49] Chen C L P and Liu Z 2018 Broad learning system: an
effective and efficient incremental learning system without
the need for deep architecture IEEE Trans. Neural Netw.
Learn. Syst. 29 10–24
[50] Ince T, Kiranyaz S, Eren L, Askar M and Gabbouj M 2016
Real-time motor fault detection by 1-D convolutional
neural networks IEEE Trans. Ind. Electron.
63 7067–75
[51] Suthaharan S 2016 Support vector machine Learning Models
and Algorithms for Big Data Classification: Thinking with
Examples for Effective Learning Integrated Series in
Information Systems ed S Suthaharan (Springer)
pp 207–35
[52] Zhao H, Sun S and Jin B 2018 Sequential fault diagnosis based
on LSTM neural network IEEE Access 6 12929–39
[53] Pao Y-H, Park G-H and Sobajic D J 1994 Learning and
generalization characteristics of the random vector
functional-link net Neurocomputing 6 163–80
[54] Gong X, Zhang T, Chen C L P and Liu Z 2022 Research
review for broad learning system: algorithms, theory, and
applications IEEE Trans. Cybern. 52 8922–50
[55] Gong A, MacNeill R and Verstraete D 2018 Performance
testing and modeling of a brushless dc motor, electronic
speed controller and propeller for a small UAV application
Joint Propulsion Conf. vol 4584 (https://doi.org/10.2514/
6.2018-4584)
[56] Awadallah M A, Morcos M M, Gopalakrishnan S and
Nehl T W 2005 A neuro-fuzzy approach to automatic
diagnosis and location of stator inter-turn faults in CSI-fed
PM brushless DC motors IEEE Trans. Energy Convers.
20 253–9
19
