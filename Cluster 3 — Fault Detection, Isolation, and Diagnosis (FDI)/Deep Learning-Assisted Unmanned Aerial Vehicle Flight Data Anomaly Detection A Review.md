# Deep Learning-Assisted Unmanned Aerial Vehicle Flight Data Anomaly Detection A Review.pdf

## Page 1

IEEE SENSORS JOURNAL, VOL. 24, NO. 20, 15 OCTOBER 2024
31681
Deep Learning-Assisted Unmanned Aerial
Vehicle Flight Data Anomaly
Detection: A Review
Lei Yang , Shaobo Li , Yizong Zhang , Caichao Zhu, and Zihao Liao
Abstract—Flight data anomaly detection is crucial for
ensuring the flight safety of unmanned aerial vehicles (UAVs).
By monitoring and analyzing flight data, anomalies can be
detected in time to avoid potential risks. Deep learning can
automatically extract complex patterns and features from
data and has been widely used in UAV flight data anomaly
detection in recent years. Given the lack of a comprehensive
survey of research related to deep learning in UAV flight data
anomaly detection, this article conducts a systematic and
in-depth literature review. First, the basic concepts of UAV
flight data are briefly introduced, followed by an analysis and
summary of the applications of deep learning methods based
on prediction and reconstruction in UAV flight data anomaly
detection. Emphasis is placed on the research progress of
deep learning methods based on recurrent neural network
(RNN), convolutional neural network (CNN), auto-encoder
(AE), and variational AE (VAE) for UAV flight data anomaly detection. Second, an in-depth analysis of the threshold
calculation methods utilized in existing research is conducted and the advantages and limitations of these thresholds in
practical applications are discussed. Finally, some insightful research directions are given based on the shortcomings
of existing research. This work aims to provide a reference and insight for future research, inspire further studies, and
jointly promote the development of this promising field.
Index Terms— Anomaly detection, deep learning, flight data, unmanned aerial vehicle (UAV).
I. INTRODUCTION
W
ITH the advancing technology and expanding market
scale of unmanned aerial vehicles (UAVs), their appli-
cations in forest health monitoring [1], marine monitoring [2],
agriculture [3], and search and rescue [4] are becoming more
and more widespread and important. However, UAVs may face
various environmental and technical challenges, which may
Manuscript
received
21
July
2024;
revised
27
August
2024;
accepted 27 August 2024. Date of publication 5 September 2024;
date of current version 16 October 2024. This work was supported in
part by the National Natural Science Foundation of China under Grant
52275480 and in part by the National Natural Science Foundation of
China under Grant 52365061. The associate editor coordinating the
review of this article and approving it for publication was Dr. Chiman
Kwan. (Corresponding author: Shaobo Li.)
Lei Yang and Yizong Zhang are with the School of Mechani-
cal Engineering, Guizhou University, Guiyang 550025, China (e-mail:
yl19971007@163.com; yizongzhang1@163.com).
Shaobo
Li
is
with
the
School
of
Mechanical
Engineering,
Guizhou Institute of Technology, Guiyang 550025, China (e-mail:
lishaobo@gzu.edu.cn).
Caichao Zhu is with the State Key Laboratory of Mechanical Trans-
missions, Chongqing University, Chongqing 400044, China (e-mail:
cczhu@cqu.edu.cn).
Zihao Liao is with the State Key Laboratory of Public Big Data,
Guizhou University, Guiyang 550025, China (e-mail: gs.zhliao22@
gzu.edu.cn).
Digital Object Identifier 10.1109/JSEN.2024.3451648
lead to anomalies or accidents involving UAVs. Therefore,
although UAVs provide convenience for performing various
tasks [5], their frequent accidents in recent years have caused
huge economic losses to relevant countries and enterprises [6],
[7]. In this context, the demands for the safety and reliability of
UAVs are increasing. However, as closed-loop control systems,
UAVs lack real-time decision-making by pilots, presenting
significant challenges in ensuring their safe and reliable flight.
Thus, many studies on UAVs prognostics and health man-
agement (PHM) [8], [9], [10], [11], [12], [13], [14], [15],
[16] have emerged to address these challenges. For example,
redundant system design can be used to improve the reliability
and fault tolerance of UAVs [17]. This ensures that even if
certain components or sensors are abnormal or failure, the
system can continue to operate or maintain functionality by
switching to alternate components. With the rapid development
of artificial intelligence and big data technology, the potential
value of data has been further explored. Flight data are an
important indicator to assess the performance of UAV flight
status. Therefore, detecting possible anomalies in flight data
is important to ensure the safety of UAVs [18], [19].
Anomaly detection refers to identifying potential anomalies
by analyzing data or behavioral patterns that significantly
differ from the normal state [20]. It focuses on discovering
1558-1748 © 2024 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:03:14 UTC from IEEE Xplore.  Restrictions apply.

## Page 2

31682
IEEE SENSORS JOURNAL, VOL. 24, NO. 20, 15 OCTOBER 2024
data points or patterns that deviate significantly from normal
behavior. In contrast, fault detection aims to identify and
detect faults within a system or device, typically manifested
as abnormalities in its operational state [21]. Thus, fault
detection can be considered a part of anomaly detection and
is included in the broader topic of anomaly detection in flight
data for analysis and discussion in this article. Anomaly or
fault detection requires establishing a model of the normal
operating state and subsequently detecting anomalies or faults
by comparing deviations against predefined thresholds. Tra-
ditional machine learning-based methods like k-means [22],
[23], [24], [25], k-nearest neighbors (KNNs) [26], [27], [28],
[29], kernel principal component analysis (KPCA) [30], [31],
[32], [33], support vector machine (SVM) [29], [33], [34],
[35], [36], [37], [38], [39], Bayesian network (BN) [40], [41],
decision tree (DT) [29], [42], [43], Kalman filter (KF) [7],
[44], [45], [46], [47], [48], [49], [50], [51], [52], [53], random
forest (RF) [54], [55], as well as statistics-based methods like
Least square [56], [57], [58], [59] and Mahalanobis distance
(MD) [60], which have been widely used for UAV flight
data anomaly or fault detection. However, these methods may
demonstrate limited flexibility and adaptability when handling
complex flight data due to the complex meteorological con-
ditions and diverse task requirements in UAV operational
environments, coupled with UAV systems’ nonlinearity and
high dynamics. Driven by this demand, significant progress
has been made in UAV flight data anomaly detection with
the assistance of deep learning in recent years. Deep learning
reduces the reliance on manual feature engineering through
end-to-end learning [61], thus providing a more powerful tool
to address the complexities of dynamic flight environments
of UAVs. For example, deep learning methods such as con-
volutional neural network (CNN) [62] and long short-term
memory (LSTM) [63], [64] network can automatically learn
data patterns, which allows more flexibility in detecting com-
plex anomaly patterns in flight data.
Several review studies have reported on the research
progress of UAV flight data anomaly or fault detection.
Puchalski and Giernacki [21] systematically surveyed papers
on UAV fault detection included in the Web of Science and
Google Scholar between January 2016 and August 2022. They
focused on the research progress of data- and model-based
and hybrid data- and model-based approaches, and analyzed
and summarized their advantages and disadvantages in detail.
Yang et al. [6] discussed and summarized the knowledge-
based, model-based, and data-driven anomaly detection meth-
ods for UAV flight data and their applications and presented
related datasets and UAV simulation software. On this basis,
they pointed out the future directions that were worth research-
ing in model interpretability, data-driven algorithms, hybrid
models, and transfer learning-based and UAV cluster anomaly
detection. However, these reviews lack a detailed discussion
on the application of deep learning methods for flight data
anomaly detection of UAVs. Particularly, in recent years,
data-driven methods based on deep learning have gradually
emerged as mainstream approaches. However, there remains
a lack of comprehensive summary and evaluation of the
application of deep learning in this area.
To fill this gap, we conduct a systematic review aiming at
deeply analyzing the research progress of deep learning-based
methods for UAV flight data anomaly detection. This study
specifically addresses problems stemming from anomalies in
flight data. It does not consider related issues such as power
system and structural failures, as well as the influence of flight
dynamics variations and external environmental disturbances
on the data. The main contributions of this article compared
to previous studies are described as follows.
1) We
provide
a
comprehensive
overview
of
deep
learning-assisted anomaly detection methods for UAV
flight data. So far, there is almost no comprehensive
review literature in the field dedicated to deep learning
methods. Especially with the rapid development of deep
learning technology, it is necessary to deeply investigate
its latest research progress in UAV flight data anomaly
detection. Therefore, we provide sufficient details about
the deep learning-assisted anomaly detection methods
for UAV flight data.
2) We analyze and summarize commonly used anomaly
determination threshold calculation methods in order to
gain insight into the field, especially the description
of threshold aspect content not covered in the existing
review literature.
3) We determine some future research directions for UAV
flight data anomaly detection.
The rest of this article is organized as follows. Section II
describes the research methodology. Section III introduces
the basic concepts of UAV flight data. Section IV pro-
vides an in-depth analysis of deep learning-assisted UAV
flight data anomaly detection methods. The commonly used
anomaly detection determination thresholds are highlighted in
Section V. Section VI gives the future directions. Section VII
summarizes this work.
II. RESEARCH METHODOLOGY
A. Keywords and Databases
To comprehensively consider the relevant literature reported
in the field of UAV flight data anomaly detection, a series of
keywords that include UAV, drone, flight data, fault detec-
tion, and anomaly detection were combined. These keywords
were then extensively searched in several reputable academic
databases, including IEEE EXPLORE, Google Scholar, and
Web of Science. This search strategy was designed to ensure
that we could cover a broad and related field. The specific
timeframe of the search was from 2013 to 2023 to ensure a
more comprehensive collection of literature associated with
anomaly detection in UAV flight data.
B. Statistics and Analysis of Literature
Based on Section II-A, the collected related literature was
systematically counted and analyzed, as shown in Fig. 1.
From 2013 to 2023, a total of 108 papers were screened,
as shown in Fig. 1(a), among which the number of papers
for 2022 and 2023 stands out with 16 and 18 papers, respec-
tively. These papers were categorized in detail based on their
publication channels and formats, including conference papers,
journal papers, and preprints, numbering 45, 61, and 1, respec-
tively, as shown in Fig. 1(b). These papers are further divided
into deep learning-, traditional machine learning-, statistics-,
reinforcement learning-based, and other methods. Specifically,
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:03:14 UTC from IEEE Xplore.  Restrictions apply.

## Page 3

YANG et al.: DEEP LEARNING-ASSISTED UAV FLIGHT DATA ANOMALY DETECTION: A REVIEW
31683
Fig. 1. Statistics of field-related literature (a) published papers per year from 2013 to 2023, (b) published article types, and (c) methods used in the
papers.
Fig. 2. Distribution of literature based on deep learning methods.
48 papers used traditional machine learning-based methods,
five papers used statistics-based methods, two papers used
reinforcement learning-based methods, 36 papers used deep
learning-based methods, and 13 papers used other methods or
review papers, as shown in Fig. 1(c).
C. Selection Standard
According to the collected literature as described in
Section II-B, we retained the articles that only employ deep
learning. As shown in Fig. 2, deep learning-based methods are
mainly concentrated from 2019 to the present, with an increas-
ing trend year by year. Although some of the literature titles or
abstracts involve anomaly or fault detection, a closer reading
reveals that they focus more on fault classification [65], [66],
[67], [68]. Given that this article is primarily concerned with
binary classification, i.e., normal or abnormal, the choice is
to exclude this part of the literature. It was also noted that
some journal papers were extended versions of conference
papers. For example, [69] is a journal paper based on the
conference [70]. Therefore, these more informative journal
papers are the main objects discussed in this article. After
a series of analyses and selection, 25 papers were finally
included in the discussion of this article.
III. BASIC CONCEPTS OF UAV FLIGHT DATA
Flight data is a series of parameters related to the flight
and operational status of aircraft. Considerable studies have
been focusing on analyzing and modeling flight data from
UAVs [71], [72], commercial aircraft [73], [74], [75], [76], and
helicopters [77], [78] to develop health monitoring methods.
In this case, flight data serves as a crucial carrier of informa-
tion, and it is necessary to understand the detailed information
associated with flight data. Therefore, this section provides a
more comprehensive analysis and summary of UAV flight data
characteristics and common anomaly types.
A. Characteristics of UAV Flight Data
UAV flight data include flight parameters such as attitude,
acceleration, pitch, roll, longitude, and latitude of UAVs. These
parameters are collected by sensors equipped with UAVs and
cover flight data in different periods and flight stages, as shown
in Fig. 3. Therefore, UAV flight data have the characteristics
of multisource, time-varying, and multistage.
1) Multisource: UAV flight data are typically collected from
multiple sensors, including Global Positioning Systems (GPS),
gyroscopes, accelerometers, and gaussmeter sensors. Each
sensor records one or more flight parameters. This multisource
makes UAV flight data high dimensional and complex spatial-
temporal correlation [79].
2) Time-Varying:
Flight
data
belong
to
typical
time-
sequence data and is time-varying. This means that UAVs will
constantly change their flight data, such as position, speed, and
attitude. These flight data will be generated continuously as
data streams and contain UAV flight data at each moment.
3) Multistage: The flight process of UAVs involves several
flight stages, such as taxi, takeoff, cruise, descent, and land-
ing [80]. Each flight stage is characterized differently. For
example, during the takeoff stage, more attention may be paid
to the acceleration and altitude changes. The cruise stage may
be more concerned with speed and flight path.
B. Common Anomaly Types of UAV Flight Data
There seems no consensus on the definition of the outlier so
far [81]. The more classical view is that outliers are observed
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:03:14 UTC from IEEE Xplore.  Restrictions apply.

## Page 4

31684
IEEE SENSORS JOURNAL, VOL. 24, NO. 20, 15 OCTOBER 2024
Fig. 3. Multisource, time-varying, and multistage characteristics of UAV flight data.
Fig. 4. Common types of UAV flight data (a) point, (b) bias, (c) drift, (d) stuck, and (e) compound anomalies.
results that are not consistent with expected behavior [20].
Considering the temporal characteristics of UAV flight data,
its anomaly types can be broadly categorized into point,
contextual, and collective anomalies [82]. In this context, it can
be further divided into point, bias, drift, stuck, and compound
anomalies based on existing studies [63], [71], [79]. Fig. 4
briefly illustrates the behavior of each anomaly type.
1) Point Anomaly: Point anomaly refers to the sudden devi-
ation of UAV flight data from the expected value at a certain
moment, showing instantaneous abnormal changes, as shown
in Fig. 4(a). For example, when the GPS satellite search
conditions are poor, the GPS sensor output has a large error
at one point and then the output is correct [83]. Factors
such as environmental noise, measurement system errors, and
operational errors can also cause flight data to exhibit multiple
discrete outliers [26]. Its expression is defined as follows:
ypoint(t) = y(t) + α
(1)
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:03:14 UTC from IEEE Xplore.  Restrictions apply.

## Page 5

YANG et al.: DEEP LEARNING-ASSISTED UAV FLIGHT DATA ANOMALY DETECTION: A REVIEW
31685
where ypoint(t) and y(t) are the point anomaly and normal
data, respectively, t is a discontinuous time point, and α is a
constant or a variable constant.
2) Bias Anomaly: Bias anomaly refers to UAV flight data
that continuously deviates from the expected value with a
constant deviation value over a period, as shown in Fig. 4(b).
Factors such as sensor, actuator, and control surface faults
may cause bias anomalies in flight data [59], [83], [84]. For
example, temperature change or vibration disturbance causes
bias current or bias voltage [83]. A bias difference between
the actual and commanded deflections reflected on the control
surface due to slipping servo actuator gears or bent control
linkages [84]. Its expression is defined as follows:
ybias(t) = y(t) + β
(2)
where ybias(t) is the bias anomaly data and β is a fixed bias
constant.
3) Drift Anomaly: Drift anomaly refers to the UAV’s flight
data gradually deviating from the expected value within a
certain period of time during the flight process, showing
a continuous increasing or decreasing trend, as shown in
Fig. 4(c). Unlike bias anomaly, drift anomaly changes grad-
ually over time. Factors contributing to drift anomalies may
include sensor or actuator faults such as temperature change,
uncalibrated sensor, change in elevator leveling, servo power
reduction, and main rotor power reduction [59], [83], [85].
Its expression is defined as follows:
ydrift(t) = y(t) + η(t)
(3)
where ydrift(t) is the drift anomaly data and η(t) is a func-
tion of t. In some studies, η(t) can also be expressed as
η(t) = k × t, where k is the drift rate [63], [86].
4) Stuck Anomaly: Stuck anomaly means that the UAV
flight data suddenly stops changing at a certain moment and
stays at a fixed value that no longer fluctuates, as shown
in Fig. 4(d). For example, a stuck rudder or engine failure
will result in a constant output [59]. Servo power and main
rotor power decline will cause the actuator to stay in a fixed
position whatever the input value is [87]. Factors such as the
broken control linkage and broken servo gears can lead to
the control surfaces being stuck in a certain position [84].
Communication link and power interruption anomalies can
also cause the sensor to output a zero or constant value at
a certain point [83]. Its expression is defined as follows:
ystuck(t) = ε
(4)
where ystuck(t) is the stuck anomaly data and ε is a constant.
5) Compound Anomaly: Compound anomaly is a phe-
nomenon in which multiple anomalies, such as simultaneous
bias, drift, and point anomalies, occur in UAV flight data
at a given period of time, as shown in Fig. 4(e). Factors
contributing to the anomaly may include the combined effects
of various factors like temperature change, sensor and actuator
faults, power interruptions, environmental noise, etc., as men-
tioned above, resulting in complex anomalies in the UAV
during flight. Its expression is defined as follows:
ycompound(t) = y(t) + γ (t)
(5)
where ycompound(t) is the compound anomaly data and γ (t) is
a function of t. It contains several terms and the form of each
term corresponding to time t may not be identical.
It needs to be emphasized that while different types of
UAVs, such as fixed-wing and multirotor UAVs, may exhibit
similar anomalies in flight data, the specific components asso-
ciated with these anomalies may differ significantly, especially
the differences in control surfaces and flight behaviors. Some
anomalies are unique to fixed-wing UAVs such as elevator and
aileron control failures. Anomalies such as propeller damage
are unique to multirotor UAVs.
IV. DEEP LEARNING-ASSISTED ANOMALY
DETECTION FOR UAV FLIGHT DATA
As seen from Section II, researchers have been actively
exploring various deep learning-based methods since 2019 for
UAV flight data anomaly detection. Based on existing stud-
ies, deep learning-based approaches can be divided into
prediction- and reconstruction-based methods [63], [79], [88],
[89]. Prediction-based approaches detect anomalies by pre-
dicting future data and comparing the residuals between
predicted and actual values with a given threshold, while
reconstruction-based methods detect anomalies by reconstruct-
ing existing data and comparing reconstruction errors with a
given threshold. The former focuses on the prediction error
of future data, while the latter focuses on the reconstruction
error of existing data. Based on deep learning algorithms,
prediction-based methods can be categorized into recurrent
neural network (RNN)- and CNN-based approaches [62],
[79], [90], [91], and reconstruction-based methods can be
divided into auto-encoder (AE)- and variational AE (VAE)-
based approaches [88], [89], [92], [93]. This section focuses
on the research progress of these methods in UAV flight data
anomaly detection based on the introduction of the problem
definition.
A. Problem Definition
The aim of UAV flight data anomaly detection is to identify
data points that deviate from normal flight patterns. After
model testing, each test data point x is assigned a score s.
The larger the value of s, the more likely that x is an anomaly.
The specific determination is made by comparing s to a given
threshold T . If s > T , then x is abnormal, and vice versa.
B. Prediction-Based Anomaly Detection Methods
Prediction-based anomaly detection methods are used to
identify anomalies in data by building prediction models [94].
These methods assume that the farther the data points are from
the normal data distribution learned by prediction models, the
more significant the differences between the actual and pre-
dicted values are. Therefore, the basic idea of prediction-based
anomaly detection methods is first to create a deep learning
model. This model is then used to learn the normal data
distribution to predict future data. During the model testing
phase, the error between the original and predicted data points
is compared to the threshold to determine if the data point
is anomalous. Prediction-based methods are better able to
adapt to changes in data distribution and complexity, thus
improving the generalization ability of the model. However,
their detection performance is significantly affected by the
model’s prediction ability and the accumulation of prediction
errors. In addition, prediction-based methods tend to focus on
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:03:14 UTC from IEEE Xplore.  Restrictions apply.

## Page 6

31686
IEEE SENSORS JOURNAL, VOL. 24, NO. 20, 15 OCTOBER 2024
Fig. 5. General flow of prediction-based methods for UAV flight data anomaly detection.
monitoring a single parameter and lack an accurate grasp of
the overall anomalies of the system.
Fig. 5 shows the general flow of prediction-based UAV
flight data anomaly detection methods. In addition to nor-
malizing the original UAV flight data using the max-min or
Z-score methods, approaches such as the maximal information
coefficient (MIC) [91], [104] and Pearson correlation coeffi-
cient (PCC) [64] can be used for parameter selection, or data
can be denoised using wavelet analysis (WA) [98]. Next, the
processed flight data are divided into training and test sets.
In this phase, it is usually necessary to determine a detected
parameter. The training set only contains normal data, while
the test set contains anomalous data either injected artificially
or actually occurs. Then, 1-D CNN-, temporal convolutional
network (TCN)-, LSTM-, or gate recurrent unit (GRU)-based
prediction models are used to model the flight data. These
methods can be used alone, in combination, or with other
components, such as graph attention network (GAT) [99]
and attention mechanism (AM) [104], to construct prediction
models that are trained and evaluated on training and test sets.
Finally, anomaly detection is realized by comparing the predic-
tion errors of the detected parameter with the threshold. In this
stage, methods like the low-pass infinite impulse response
(IIR) filter [63] and exponentially weighted moving average
(EWMA) [99] can be used to smooth the prediction errors or
dynamic thresholds can be used to improve anomaly detection
performance. Table I lists the prediction-based anomaly detec-
tion methods, including critical information such as paper,
year, paper type, method, data type, input data, and detected
component (parameter).
1) RNN-Based Anomaly Detection Methods:
Traditional
RNN [105] suffers from problems like gradient vanishing
and gradient explosion, which limits its performance on long
sequence data [106]. To overcome these problems, existing
studies mainly use variants of RNN like LSTM, GRU, and
bi-directional LSTM (BiLSTM). Wang et al. [95] designed an
LSTM-based prediction model for detecting anomalies in UAV
sensor data, which successfully identified all anomalies in the
north speed and pneumatic lifting speed. Point anomalies are
relatively easily identified and detected as they often stand
out clearly in data. However, more complex anomaly patterns,
such as bias or drift anomalies, may require more effective
detection strategies. As an effective solution, Wang et al.
[63] chose the roll rate generated by the gyroscope sensor
as the detected parameter and proposed a fault detection
method based on LSTM with residual filtering (LSTM-RF).
Experiments were conducted on simulated and real UAV
flight data using parameters like roll angle, pitch angle, and
yaw angle as model inputs, which showed that the average
accuracy and area under the curve (AUC) of the method in
dealing with bias and drift faults exceeded 0.928 and 0.967,
respectively. In [90], a fault detection model acceleration
engine (FDMAE) approach was proposed, which included an
LSTM-based prediction model, an IIR-based residual filtering
method, a field-programmable gate array (FPGA) acceleration
method, and a PCA-based pruning method. This approach used
GPS altitude, GPS longitude, pitch rate, and other parameters
related to the position and attitude control of the UAV as model
inputs and achieved accuracy and AUC of 0.986 and 0.998 for
the roll rate with injected bias fault, respectively. Similarly,
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:03:14 UTC from IEEE Xplore.  Restrictions apply.

## Page 7

YANG et al.: DEEP LEARNING-ASSISTED UAV FLIGHT DATA ANOMALY DETECTION: A REVIEW
31687
TABLE I
LITERATURE RELATED TO PREDICTION-BASED ANOMALY DETECTION METHODS IN RECENT YEARS∗
in [101] and [102], the authors also used LSTM prediction
models and an IIR-based residual smoothing approach for
UAV flight data anomaly detection. The former successfully
detected all the point anomalies in the roll angle, while
the latter achieved accuracy and F1 scores of 0.9615 and
0.9600 for parameters such as roll rate and y-velocity where
anomalies existed. Chen et al. [98] utilized parameters such
as pitch, yaw, and altitude as model inputs and denoised them
using WA before model training. Then, they used an enhanced
GRU prediction model to detect the roll parameter with bias
fault.
The above studies often lack effective parameter selection
when faced with multiple input parameters. Since numerous
flight parameters exist, selecting appropriate parameters as
model inputs is crucial. This is because unrelated parameters
may have a negative impact on the model. Several studies have
gradually realized the problem of complex high-dimensional
parameter input and taken corresponding measures to deal with
it. A typical example is a correlation analysis method based on
PCC for selecting model input parameters [64]. In this exam-
ple, a prediction model based on a novel uncertainty-aware
LSTM (UA-LSTM) was proposed for modeling pitch angle,
pitch rate, air speed, and other parameters that have a
correlation with the actuator, and combined with dynamic
thresholds for detecting the actuator injected with bias fault.
However, PCC can only capture linear correlation of flight
parameters, which means that the positive impact of some
nonlinear correlation parameters on model performance may
be lost. In this context, some studies introduced more sophis-
ticated correlation analysis methods to address the problem.
For example, Zhong et al. [79] proposed a spatio-temporal
correlation-based LSTM (STC-LSTM) method for UAV flight
data anomaly detection. They first selected seven parameters
related to the roll angle as model inputs, such as pitch angle
rate, right aileron command, and yaw angle rate, through
artificial neural network correlation analysis (ANNCA). Then,
they constructed an LSTM prediction model with a false
positive rate (FPR) of 0, a false negative rate (FNR) of 0,
and an accuracy of 1 for the roll angle injected with point,
bias, and stuck anomalies. He et al. [99] used GAT to ignore
irrelevant variables and finally selected 36 variables, such as
roll angle, pitch angle, and yaw angle, which are significant to
UAV flight as input parameters. Subsequently, they detected
the roll rate injected with multiple fault types based on the
proposed masked spatial GAT with the GRU (masked-SGAT-
GRU) model. Apart from this, some information theory-based
methods are also used for parameter selection. For example,
Zhou et al. [104] proposed a sensor fault detection method
based on MIC and LSTM with AM (MICA-LSTM). They first
used roll rate as the detected parameter and selected seven
parameters related to it using MIC, such as X-axis angular
rate, Euler roll angle, and Euler yaw angle, as model inputs.
Then, a prediction model was constructed based on LSTM and
AM with a fault detection accuracy of more than 0.9900 for
the roll rate injected with bias and drift faults. Although
Keipour et al. [59] may lose some key nonlinear correlation
parameter information compared to [79], [99], and [104],
it could dynamically detect anomalies in the flight data. This is
particularly important since UAV operating environments are
often complex and variable and fixed thresholds often fail to
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:03:14 UTC from IEEE Xplore.  Restrictions apply.

## Page 8

31688
IEEE SENSORS JOURNAL, VOL. 24, NO. 20, 15 OCTOBER 2024
change with dynamic flight changes. However, considering the
complex relationship between UAV flight parameters, relying
only on LSTM or GRU may lead to inadequate feature
extraction, affecting the model’s accuracy and generalization
ability. In contrast, by combining GAT and AM, [99], [104]
can perform finer feature extraction and modeling of UAV
flight data. However, the increase in model complexity may
further lead to an increase in computational cost, and thus the
effectiveness of these methods in practical applications needs
to be further validated.
The effectiveness of the above methods relies on suffi-
cient data for model training. However, obtaining adequate
flight data may be costly in practice. In recent research,
Liu et al. [103] proposed an innovative cross-domain approach
for UAV actuator fault detection. This method utilized param-
eters such as airspeed, eastward velocity, and roll angle
as inputs to the BiLSTM prediction model and introduced
a method to compute similarity metrics between different
domains using MIC. The fault detection results on the actuator
injected with bias and drift faults were better than 0.0250 for
FPR, and the true positive rate (TPR) and accuracy were both
higher than 0.9779. The uniqueness of this approach is that it
alleviates the dependence on massive training data in the target
domain and provides a more flexible solution for anomaly
detection of UAV flight data with limited samples. However,
this work did not explore the performance of the model with
different fine-tuning samples. This is because in some cases,
when a certain number of fine-tuning samples are reached
the model can be trained directly without transfer learning
to achieve satisfactory results.
2) CNN-Based Anomaly Detection Methods: Unlike RNN
methods like LSTM, GRU, and BiLSTM, CNN captures local
features and patterns in the input data through its convolution
and pooling layers [107], [108]. In addition, CNN can be
computed in parallel, which is more efficient when dealing
with large-scale data. For example, Ahn et al. [96] used 1-D
CNN and a fully connected multilayer perceptron to detect
a single UAV anomaly in swarm UAVs by modeling flight
data such as gyroscope, acceleration, and position. Similarly,
Galvan et al. [97] designed a CNN-based prediction model
and utilized inertial measurement unit (IMU) sensor data as
model input. The experimental results showed that the AUC
for different components of the IMU sensor injected with
anomaly was 0.937. In [91], a fault detection method based
on MIC and 1-D CNN (MIC-1-D CNN) was proposed, which
utilized MIC to select the parameters, such as Euler yaw angle,
GPS east velocity, and GPS latitude, as model inputs. Then,
a prediction model based on 1-D CNN was used to detect
the actuator’s bias and drift faults. This method maintained
a lower FPR while its TPR and AUC exceeded 0.9400 and
0.9800, respectively, and possessed a faster detection speed.
However, CNN mainly focuses on local feature extraction.
This may result in CNN ignoring long-term dependencies
and contextual relationships when processing time-series data.
As an alternative to CNN, You et al. [100] proposed a UAV
sensor anomaly detection method based on fine-tuned TCN
(FTCN). The method utilized ten variables like roll rate, pitch
rate, and yaw rate as model inputs and achieved an accuracy of
0.9476 on the pitch angle with the injected anomaly. Another
approach is to combine CNN and LSTM to construct a
prediction model, such as the multioutput convolutional LSTM
(MOConvLSTM) method in [62]. This method modeled the
input parameters such as airspeed, altitude, and right aileron
command, and effectively detected the parameters like roll
rate, airspeed, and angle of attack with anomalies. Compared
with the previous studies, this work combined the advantages
of CNN in local feature and LSTM in temporal feature
extraction to better extract spatio-temporal features of UAV
flight data, thus improving anomaly detection performance.
C. Reconstruction-Based Anomaly Detection Methods
Reconstruction-based approaches map input data to the
latent space and learn how to reconstruct it accurately to
detect anomalies [109]. These approaches can effectively
capture anomaly patterns in the data and focus more on
monitoring the overall anomalies of the system. When there
are anomalies in the input data, it becomes exceptionally
difficult to accurately reconstruct the original data. This is
because the latent space may lose information about rare
anomalies, leading to increased reconstruction errors [94],
[110]. However, reconstruction-based approaches often require
more computational resources than prediction-based methods,
making them possibly challenging when dealing with large-
scale data. In addition, information may be lost during the
reconstruction process, especially if the data are highly com-
plex or noisy, which may lead to a high false alarm rate.
Fig. 6 illustrates the general flow of the reconstruction-
based methods. Specifically, in the data preprocessing stage,
the input data can be denoised using the Savitzky–Golay (S-G)
filter [88] in addition to normalizing the original flight data.
Next, the processed data are divided into training and test sets.
It is worth emphasizing that reconstruction-based methods
usually do not need to determine the detected parameter
because they focus on multivariate anomaly detection, as pre-
viously mentioned. Then, the deep learning models are trained
and evaluated with training and test sets, including LSTM-
AE [88], [89], [111], [112] or 1-D CNN-based VAE [92].
Finally, the anomaly detection of UAV flight data is realized
by comparing the reconstruction errors with the threshold.
Table II lists the reconstruction-based methods for UAV flight
data anomaly detection in recent years.
1) AE-Based Anomaly Detection Methods: Sequential infor-
mation in time series data is important for data reconstruction.
Traditional AE may ignore this sequential information when
reconstructing the input data [115], [116]. Therefore, a com-
mon practice is to combine AE with LSTM. This is because
LSTM can more effectively capture flight data’s temporal
patterns and regularities. For example, Bae and Joe [111]
used an LSTM-AE reconstruction model for different anomaly
detection tasks through a targeted selection of parameters,
such as position, battery, and attitude, as model inputs. The
AUC of this method was more than 0.9200 for low-level and
high-level anomaly detection. Similarly, Gao et al. [113] used
navigation altitudes from six flights as inputs to an LSTM-AE
reconstruction model, where the normal flights were used for
model training and the abnormal flights with anomaly were
used for evaluating the model. The average FI score and
accuracy of LSTM-AE exceeded 0.93 and 0.89, respectively.
Another approach is to utilize BiLSTM and CNN to construct
an AE model. BiLSTM has a better contextual understanding
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:03:14 UTC from IEEE Xplore.  Restrictions apply.

## Page 9

YANG et al.: DEEP LEARNING-ASSISTED UAV FLIGHT DATA ANOMALY DETECTION: A REVIEW
31689
Fig. 6. General flow of reconstruction-based methods for UAV flight data anomaly detection.
TABLE II
LITERATURE RELATED TO RECONSTRUCTION-BASED ANOMALY DETECTION METHODS IN RECENT YEARS∗
when processing temporal data compared to LSTM [117]. For
example, Sadhu et al. [69] constructed an AE model using
BiLSTM and CNN and utilized accelerometer, gyroscope, and
magnetometer data as model inputs with an anomaly detection
accuracy of over 90%. Although AE can filter out some
noise, its effectiveness in suppressing random noise may be
limited. Considering this challenge, an STC-LSTM and AE
(STC-LSTM-AE) was proposed in [88], which denoised the
determined parameters based on MIC, such as GPS latitude,
Euler roll angle, and X-axis acceleration, by using S-G before
LSTM-AE model training. The method effectively reduced the
effect of random noise and achieved an anomaly detection
accuracy as high as 98.75%.
However, the studies mentioned above mainly used fixed
thresholds, which may not be effectively adapted to the dynam-
ics and complexity of the UAV flight environment, and thus
may lead to a higher false alarm rate. To address this issue,
some studies adopted dynamic threshold generation methods
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:03:14 UTC from IEEE Xplore.  Restrictions apply.

## Page 10

31690
IEEE SENSORS JOURNAL, VOL. 24, NO. 20, 15 OCTOBER 2024
that adaptively adjust the thresholds for more accurate anomaly
detection. For example, Jeon et al. [89] utilized the power
and pulsewidth modulation value of each motor as input to
the designed LSTM-AE model and used an adaptive decision
score method to detect manually created propeller, motor,
and frame anomalies. The experimental results showed that
the average specificity and sensitivity of the method were
98.6% and 90.3%, respectively. Similarly, Arce et al. [112]
focused on detecting engine fault in the ALFA dataset [11]
based on an LSTM-AE model with dynamic thresholding and
dynamically weighted loss function (LSTM-AE + DT + DW).
Unlike [89], [112], Ma et al. [114] introduced a more advanced
Transformer as a coding module and combined it with BN and
graph convolutional network (GCN) and proposed an anomaly
detection method based on graphical normalizing flows (GNF).
The method used parameters like roll, pitch, and yaw, as model
inputs and combined them with dynamic thresholds to detect
abnormal components such as Compass and GPS. In particular,
this work collected and organized the first dataset of small
unmanned aerial systems (sUASs), including 41 flight logs
labeled with various anomaly types. However, the model may
have a high computational cost and model complexity due to
the use of multiple modules [114].
2) VAE-Based Anomaly Detection Methods: Compared with
AE, VAE introduces a hidden variable distribution [118]. This
allows VAE to take into account the probabilistic structure in
the latent space, making it more expressive and interpretive,
thus better capturing the underlying patterns and variations
in the input data [119]. In recent years, VAE has also been
actively introduced into the UAV flight data anomaly detection
field. For example, Dhakal et al. [93] detected abnormal
components, such as the left rudder, right rudder, and left
aileron, using the ALFA dataset as input to AE and VAE
models. The results showed that the VAE-based method could
effectively detect anomalies with an average accuracy of
95.6%. However, as revealed in this work, it was mainly
limited to offline operation and could not fulfill the needs
of real-time anomaly detection. Different from traditional
VAE, Ahn [92] constructed a 1-D-CNN-based VAE model to
model the signals collected by sensors, such as accelerator,
magnetometer, and barometer, to detect anomalies in a single
UAV. However, the method may result in higher computational
costs and resource requirements for model training due to the
use of a deeper network structure.
V. COMMONLY USED ANOMALY
DETERMINATION THRESHOLDS
Thresholds play a vital role in anomaly detection and
directly affect model performance and reliability [61]. Thresh-
olds that are too high or too low may result in a higher
false alarm rate [120]. Therefore, it is important to choose
proper thresholds to ensure the model is robust and reliable in
practical applications. Therefore, we analyze and summarize
the threshold calculation methods used in existing studies more
comprehensively, aiming to provide a reference for subsequent
research in threshold selection.
A. Mean Squared Error
Mean square error (mse) is a metric that is used to measure
the difference between predicted or reconstructed and actual
data [121]. It first calculates the sum of squares of the residuals
for each data sampling point and then averages them, i.e.,
mse = 1/n Pn
i=1 ( ˆytr
i −ytr
i )
2, where ˆytr
i and ytr
i are the pre-
dicted or reconstructed and the actual data of the original
ith sample in the training set, respectively, and n is the
sample length. MSE as a threshold is commonly used in
reconstruction-based methods [88], [93], [113]. The advantage
of mse is that it is simple to calculate and very sensitive to
rapidly fluctuating anomalies. This sensitivity allows mse to
detect small but significant changes in the data to take the
necessary action in advance to ensure system reliability and
safety. However, this method requires the model to be very
precise in prediction or reconstruction, which may cause the
model to be too critical of some otherwise decent results, thus
reducing the model’s accuracy and robustness. Therefore, there
is a trade-off between simplicity and sensitivity to anomaly
when using mse as the anomaly detection threshold.
B. N-Sigma
N-sigma
is
a
commonly
used
threshold
calculation
method
[122].
It
first
requires
calculating
the
mean
µ = 1/n Pn
i=1 ( ˆy
tr
i −ytr
i ) and standard deviation σ
=
1/(n −1) Pn
i=1 [( ˆy
tr
i −ytr
i ) −µ]
2}
1/2
.
Then,
the
threshold
T = µ ± lσ, i.e., [µ −l σ, µ + lσ], is obtained, where l is
the coefficient that is usually set according to the confidence
level required. For example, when a 99% confidence level is
required, l can be set to 2.6 [63]. Prediction-based methods
mostly use n-sigma as the anomaly detection threshold [63],
[79], [90], [95]. Compared with mse, n-sigma can adjust the
value of parameter l to meet the needs of detecting more
complex anomaly patterns. This flexibility allows n-sigma
to better recognize anomalies when dealing with various
complex data. Although the calculation of n-sigma is also
relatively simple, it assumes that the data distribution is nor-
mal, which may not hold true in many practical applications.
For nonnormal distribution data, n-sigma may not be able to
accurately identify anomalies, leading to an increase in false
or missed alarms [123]. Therefore, when dealing with data
with nonnormal or complex distributions, it is necessary to
combine other methods or adjust the strategy to obtain more
accurate detection results.
C. Dynamic Thresholds
Compared with fixed thresholds, dynamic thresholds can
be more flexible to adapt to complex flight environments,
thereby improving model detection performance [64], [89],
[112], [114]. For example, in [112], a static threshold con-
stant L = µtrain + σtrain, the mean loss value for the
j instances M = 1/j Pn
i=n−j xi, and the standard deviation
S = σ(xn−j, . . . , xn−1) are first computed, where µtrain and
σtrain are the mean and standard deviation of the training
reconstruction loss, and xi is the loss of the ith data point.
Then, the threshold Tn = T (xn) = WyL + Wz(M + S) for
the nth instance is obtained, where Wy and WZ are the
weight constants of L and M, respectively. However, this
approach requires dynamic calculation of the mean loss and
standard deviation, which is computationally expensive when
dealing with large-scale datasets. Especially in real-time or
near real-time anomaly detection tasks, it can significantly
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:03:14 UTC from IEEE Xplore.  Restrictions apply.

## Page 11

YANG et al.: DEEP LEARNING-ASSISTED UAV FLIGHT DATA ANOMALY DETECTION: A REVIEW
31691
increase the system load and affect the processing efficiency
with frequent computations. Other dynamic thresholds, such
as [64] and [89], similarly require dynamic calculation of
the mean and standard deviation to determine if the current
data point is abnormal. Although using the sliding window to
obtain thresholds can reduce computational overhead, there is
a trade-off between time and space complexity in determining
the window size to ensure that anomalies can be accurately
detected without losing important information [114].
VI. FUTURE PERSPECTIVES
Existing studies have made some progress in coping with
the characteristics of complex high dimensional and random
noise in UAV flight data, deep learning model construction,
and threshold calculation. For example, researchers use S-
G [88], WA [98], IIR [63], [101], [102], and EWMA [99]
to denoise the data in the preprocessing stage or smooth
the residuals in the anomaly detection stage to minimize
the effect of random noise. Meanwhile, some studies utilize
PCC [64], ANNCA [79], and MIC [88], [104] to select
features with correlation as inputs from high-dimensional
parameters to improve model performance. For deep learning
model construction, some advanced methods are proposed,
such
as
MOConvLSTM
[62],
masked-SGAT-GRU
[99],
MICA-LSTM [104], deep CNN and LSTM-based neural net-
work [69], and GNF [114], for better modeling and feature
extraction of flight data. In terms of threshold computa-
tion, since 2022, researchers have gradually adopted dynamic
thresholds for anomaly detection in UAV flight data, which
improves the flexibility of anomaly detection in complex
conditions [64], [89], [112], [114]. Despite this, there are
still some issues and challenges that need to be addressed.
Therefore, in this section, we provide some directions for
future research that are worthwhile for reference.
A. Critical Parameter Identification
Current studies focus on the model’s ability to detect
anomalies and lack a comprehensive understanding of the
deeper causes behind anomalies [63], [64], [79], [88], [89],
[90], [114]. Anomalies that occur in UAVs may be caused by
one or more flight parameters. Identifying flight parameters
that contribute significantly to anomalies is of great reference
value and significance for UAV maintenance. An information
theory approach, nonparametric estimation based on copula
entropy, can be first used to measure the mutual information
(MI) values between variables. These MI values are then used
as the contribution degree to anomalies that caused the system
to occur, thus identifying the monitoring parameters associated
with anomalies [124]. Meanwhile, the monitoring parameters’
scores contributing to anomalies can be calculated by a multi-
ple self-AM to identify critical parameters [125]. It utilizes an
advanced neural network to capture the complex relationships
between variables more accurately, providing deeper insights
into explaining the causes of anomalies. Further, the anomaly
scores can be transformed using a multivariate Gaussian
distribution to identify the critical parameters contributing
to anomalies [110]. Therefore, future research can actively
carry out critical parameter identification studies to provide
more targeted guidance for the maintenance and optimization
of UAVs.
B. Adaptive Anomaly Detection for Multivariate UAV
Flight Data
Existing prediction-based methods focus mainly on anomaly
detection of univariate flight parameters, which have certain
limitations in practical applications [63], [64], [90], [91], [95],
[98], [99], [100]. In practice, anomalies that occur in UAVs
usually cause multiple flight parameters to deviate from the
expected values, making these methods lack a comprehensive
grasp of UAV anomalies. Despite the reconstruction-based
methods being able to achieve multivariate anomaly detec-
tion, they are slightly less effective in modeling and feature
extraction for complex flight data. A good anomaly detection
performance relies on the accurate reconstruction or prediction
performance of models. The key is the need for finer feature
extraction and modeling of the complex relationships of UAV
flight data. As a revolutionary deep learning architecture,
Transformer can effectively capture long-range dependencies
in sequences and transform them into meaningful feature rep-
resentations [126]. Therefore, UAV flight data can be modeled
with the help of a Transformer to extract richer and more
abstract features. These features can better reflect the complex
relationship of UAV flight data and provide stronger support
for the subsequent anomaly detection task. In addition, UAV
flight environments are complex and variable, which poses a
challenge to the adaptability of traditional statistical threshold-
based methods. Considering the computational efficiency,
a dynamic threshold generation method based on SVR can
be used [124]. In particular, the method can effectively cope
with the dynamic changes of flight data without considering
the data distribution and improve the model’s accuracy and
robustness.
C. Real-Time Anomaly Detection Research Under
Limited On-Board Resources
In recent years, many studies have utilized more com-
plex deep learning models to extract complex spatio-temporal
correlation features of UAV flight data to improve model
performance. In this case, these models may suffer from
high complexity and computational cost [62], [99], [104],
[114]. Therefore, although these methods have been proven
to be effective in anomaly detection, they lack practical
application scenario constraints, such as the accuracy and
real-time anomaly detection problems under limited on-board
computing resources, making the practicality and effectiveness
of these methods need further verification. To address this
issue, lightweight models can be considered, such as compact
neural networks [127], to reduce computation and memory
usage while maintaining the excellent performance of the
model. It is possible to use PCA to prune the model and
reduce the computational effort of the model, thus improving
the efficiency of model inference [90]. The model inference
process can be also accelerated using FPGA [69], [90]. FPGA
can real-time inferences in resource-constrained environments
due to its processing capability and low power consump-
tion, making the model more suitable for situations where
on-board computing resources are limited. In addition, a novel
distributed redundant flight control computer architecture can
be adopted [17]. This architecture includes a distributed task
scheduling and communication model and an optimal static
scheduling and real-time analysis algorithm, etc., which can
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:03:14 UTC from IEEE Xplore.  Restrictions apply.

## Page 12

31692
IEEE SENSORS JOURNAL, VOL. 24, NO. 20, 15 OCTOBER 2024
detect anomalies or faults in real time while maintaining low
power consumption.
D. Model Generalization and Interpretability Research
Model generalization and interpretability are key challenges
in applying deep learning to engineering practices. For model
generalization, most current methods focus on model training
and construction for specific UAVs or problems, resulting
in limited model generalization. Since UAV flight data may
be affected by various factors, a model trained for a specific
dataset may not cope with anomalies in datasets from other
environments, resulting in its performance degradation in
new environments. To improve the model generalization, the
dataset size can be expanded to cover a wider range of scenar-
ios to train the model. This allows the model to be exposed to
more diverse contexts during training and improves its adapt-
ability. Second, developing accurate deep learning models is
also an effective way to enhance the model generalization. For
example, it is possible to utilize AM to better handle long-term
dependencies and enhance the learning of key features, thereby
improving the model’s prediction or reconstruction accuracy
of the data [128]. Furthermore, transfer learning [129] can
also be effective in improving the model’s generalizability
by sharing knowledge among different tasks. In terms of
model interpretability, traditional methods, such as sensitivity
analysis,
the
partial
dependence
test
[130],
and
local
interpretable model-agnostic explanations (LIME) [131], can
improve model global or local interpretability. In addition, the
more advanced layer-wise relevance propagation method can
be used to reveal how the relationship between different input
features at different time steps affects the model’s output,
thus enhancing model interpretability [132].
VII. CONCLUSION
Flight data anomaly detection is important and significant
to ensure the safety and stability of UAVs. Deep learning
methods have been widely used in the field of UAV flight data
anomaly detection and have gradually become mainstream.
Therefore, this article presented a comprehensive review of
the research progress of deep learning-assisted UAV flight
data anomaly detection. First, we presented the multistage,
multisource, and time-varying characteristics of UAV flight
data and described point, bias, drift, stuck, and compound
anomaly types. Then, the research progress of prediction- and
reconstruction-based deep learning methods was analyzed
and summarized in detail, focusing on RNN-, CNN-, AE-,
and VAE-based methods. Finally, several insightful future
research directions were given, including critical parameter
identification, adaptive multivariate anomaly detection, real-
time anomaly detection research, and model generalizability
and interpretability research. These directions are expected
to provide new theoretical and technical support for building
more robust and reliable UAV flight data anomaly detection
methods in the future.
This work aims to lay the foundation for future research and
provide insights into developing new innovative methods and
techniques of UAV flight data anomaly detection. Meanwhile,
we expect this work to encourage and inspire more researchers
to conduct in-depth studies to address current challenges and
promote greater progress in the field.
REFERENCES
[1] S. Ecke et al., “UAV-based forest health monitoring: A systematic
review,” Remote Sens., vol. 14, no. 13, p. 3205, Jul. 2022.
[2] Z. Yang et al., “UAV remote sensing applications in marine monitoring:
Knowledge visualization and review,” Sci. Total Environ., vol. 838,
Sep. 2022, Art. no. 155939.
[3] A. Rejeb, A. Abdollahi, K. Rejeb, and H. Treiblmaier, “Drones in
agriculture: A review and bibliometric analysis,” Comput. Electron.
Agricult., vol. 198, Jul. 2022, Art. no. 107017.
[4] M. Lyu, Y. Zhao, C. Huang, and H. Huang, “Unmanned aerial vehicles
for search and rescue: A survey,” Remote Sens., vol. 15, no. 13, p. 3266,
Jun. 2023.
[5] C. Titouna, F. Naït-Abdesselam, and H. Moungla, “An online anomaly
detection approach for unmanned aerial vehicles,” in Proc. Int. Wireless
Commun. Mobile Comput. (IWCMC), Jun. 2020, pp. 469–474.
[6] L. Yang, S. Li, C. Li, A. Zhang, and X. Zhang, “A survey of unmanned
aerial vehicle flight data anomaly detection: Technologies, applications,
and future directions,” Sci. China Technolog. Sci., vol. 66, no. 4,
pp. 901–919, Apr. 2023, doi: 10.1007/s11431-022-2213-8.
[7] A. Abbaspour, P. Aboutalebi, K. K. Yen, and A. Sargolzaei, “Neural
adaptive observer-based sensor and actuator fault detection in nonlinear
systems: Application in UAV,” ISA Trans., vol. 67, pp. 317–329,
Mar. 2017, doi: 10.1016/j.isatra.2016.11.005.
[8] C. Li et al., “A Siamese hybrid neural network framework for few-shot
fault diagnosis of fixed-wing unmanned aerial vehicles,” J. Comput.
Design Eng., vol. 9, no. 4, pp. 1511–1524, Aug. 2022.
[9] M. Taimoor, X. Lu, H. Maqsood, and C. Sheng, “A novel fault diagno-
sis in sensors of quadrotor unmanned aerial vehicle,” J. Ambient Intell.
Humanized Comput., vol. 14, no. 10, pp. 14081–14099, Oct. 2023.
[10] S. Liang, S. Zhang, Y. Huang, X. Zheng, J. Cheng, and S. Wu, “Data-
driven fault diagnosis of FW-UAVs with consideration of multiple
operation conditions,” ISA Trans., vol. 126, pp. 472–485, Jul. 2022,
doi: 10.1016/j.isatra.2021.07.043.
[11] A. Keipour, M. Mousaei, and S. Scherer, “ALFA: A dataset for UAV
fault and anomaly detection,” Int. J. Robot. Res., vol. 40, nos. 2–3,
pp. 515–520, Feb. 2021.
[12] T. Li, Z. Hong, Q. Cai, L. Yu, Z. Wen, and R. Yang, “BISSIAM:
Bispectrum Siamese network based contrastive learning for UAV
anomaly detection,” IEEE Trans. Knowl. Data Eng., vol. 35, no. 12,
pp. 12109–12124, Dec. 2023.
[13] H. Dui, C. Zhang, G. Bai, and L. Chen, “Mission reliability modeling
of UAV swarm and its structure optimization based on importance
measure,” Rel. Eng. Syst. Saf., vol. 215, Nov. 2021, Art. no. 107879.
[14] B. Lian et al., “Anomaly detection and correction of optimizing
autonomous systems with inverse reinforcement learning,” IEEE
Trans. Cybern., vol. 53, no. 7, pp. 4555–4566, Jul. 2023, doi:
10.1109/TCYB.2022.3213526.
[15] K. Guo, Z. Ye, D. Liu, and X. Peng, “UAV flight control sensing
enhancement with a data-driven adaptive fusion model,” Rel. Eng. Syst.
Saf., vol. 213, Sep. 2021, Art. no. 107654.
[16] H. Lu, Y. Li, S. Mu, D. Wang, H. Kim, and S. Serikawa, “Motor
anomaly detection for unmanned aerial vehicles using reinforcement
learning,” IEEE Internet Things J., vol. 5, no. 4, pp. 2315–2322,
Aug. 2018.
[17] X. Zhang and X. Zhao, “Architecture design of distributed redundant
flight control computer based on time-triggered buses for UAVs,” IEEE
Sensors J., vol. 21, no. 3, pp. 3944–3954, Feb. 2021.
[18] L. Yang, S. Li, C. Zhu, A. Zhang, and Z. Liao, “Spatio-temporal
correlation-based multiple regression for anomaly detection and recov-
ery of unmanned aerial vehicle flight data,” Adv. Eng. Informat., vol. 60,
Apr. 2024, Art. no. 102440, doi: 10.1016/j.aei.2024.102440.
[19] L. Yang, S. Li, C. Li, and C. Zhu, “Data-driven multivariate regression-
based anomaly detection and recovery of unmanned aerial vehicle flight
data,” J. Comput. Design Eng., vol. 11, no. 2, pp. 176–193, Mar. 2024.
[20] D. M. Hawkins, Identification of Outliers. Cham, Switzerland:
Springer, 1980.
[21] R. Puchalski and W. Giernacki, “UAV fault detection methods, state-
of-the-art,” Drones, vol. 6, no. 11, p. 330, Oct. 2022.
[22] Y. Wang, D. Wang, and J. Wang, “A data driven approach for detection
and isolation of anomalies in a group of UAVs,” Chin. J. Aeronaut.,
vol. 28, no. 1, pp. 206–213, Feb. 2015, doi: 10.1016/j.cja.2014.12.003.
[23] H. Fan, H. Fang, Y. Dong, H. Shi, and S. Ren, “UAV engine fault and
diagnosis with parameter models based on telemetry data,” in Proc.
Prognostics Syst. Health Manage. Conf. (PHM-Harbin), Jul. 2017,
pp. 1–6.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:03:14 UTC from IEEE Xplore.  Restrictions apply.

## Page 13

YANG et al.: DEEP LEARNING-ASSISTED UAV FLIGHT DATA ANOMALY DETECTION: A REVIEW
31693
[24] A. M. Alos and Z. Dahrouj, “Using the statistical features of the data
to detect potential failure of unmanned aerial vehicles,” Int. J. Appl.
Eng. Res., vol. 14, no. 20, pp. 3946–3952, 2019.
[25] J. Cabahug and H. Eslamiat, “Failure detection in quadcopter
UAVs using K-means clustering,” Sensors, vol. 22, no. 16, p. 6037,
Aug. 2022.
[26] Y. Liu and W. Ding, “A KNNS based anomaly detection method applied
for UAV flight data stream,” in Proc. Progn. Syst. Health Manag. Conf.
(PHM), 2015, pp. 1–8.
[27] A. Manukyan, M. A. Olivares-Mendez, T. F. Bissyande, H. Voos,
and Y. Le Traon, “UAV degradation identification for pilot notifica-
tion using machine learning techniques,” in Proc. IEEE 21st Int.
Conf. Emerg. Technol. Factory Autom. (ETFA), vol. 43, Sep. 2016,
pp. 1–8.
[28] A. Alos and Z. Dahrouj, “Detecting contextual faults in unmanned
aerial vehicles using dynamic linear regression and K-nearest neighbour
classifier,” Gyroscopy Navigat., vol. 11, no. 1, pp. 94–104, Jan. 2020.
[29] S. Shaw et al., “Anomaly detection in drones with machine learning
algorithms,” in Futuristic Communication and Network Technologies.
Cham, Switzerland: Springer, 2022, pp. 433–441.
[30] D.
Yong,
Z.
Yuanpeng,
X.
Yaqing,
P.
Yu,
and
L.
Datong,
“Unmanned aerial vehicle sensor data anomaly detection using ker-
nel principle component analysis,” in Proc. 13th IEEE Int. Conf.
Electron. Meas. Instrum. (ICEMI), Oct. 2017, pp. 241–246, doi:
10.1109/ICEMI.2017.8265777.
[31] D. Pan, “Hybrid data-driven anomaly detection method to improve
UAV operating reliability,” in Proc. Prognostics Syst. Health Manage.
Conf. (PHM-Harbin), Jul. 2017, pp. 1–4.
[32] L. Liu, M. Liu, Q. Guo, D. Liu, and Y. Peng, “MEMS sensor data
anomaly detection for the UAV flight control subsystem,” in Proc. IEEE
Sensors, Oct. 2018, pp. 1–4.
[33] L. Liu, Q. Guo, D. Liu, and Y. Peng, “Data-driven remaining useful
life prediction considering sensor anomaly detection and data recovery,”
IEEE Access, vol. 7, pp. 58336–58345, 2019.
[34] E. Baskaya, M. Bronz, and D. Delahaye, “Fault detection & diagnosis
for small UAVs via machine learning,” in Proc. IEEE/AIAA 36th Digit.
Avionics Syst. Conf. (DASC), Sep. 2017, pp. 1–6.
[35] Y. Chen, B. Wang, W. Liu, and D. Liu, “On-line and non-invasive
anomaly detection system for unmanned aerial vehicle,” in Proc.
Prognostics Syst. Health Manage. Conf. (PHM-Harbin), Jul. 2017,
pp. 1–7.
[36] D. Liu, Z. Wang, S. Wang, Y. Pang, and L. Liu, “UAV sensor data
anomaly detection using predictor with uncertainty estimation and its
acceleration on FPGA,” in Proc. IEEE Int. Instrum. Meas. Technol.
Conf. (I2MTC), May 2018, pp. 1–6.
[37] B. Wang, Y. Chen, D. Liu, and X. Peng, “An embedded intel-
ligent system for on-line anomaly detection of unmanned aerial
vehicle,” J. Intell. Fuzzy Syst., vol. 34, no. 6, pp. 3535–3545,
Jun. 2018.
[38] D. Pan, L. Nie, W. Kang, and Z. Song, “UAV anomaly detection using
active learning and improved S3VM model,” in Proc. Int. Conf. Sens.
Meas. Data Anal. Era Artif. Intell. (ICSMD), 2020, pp. 253–258, doi:
10.1109/ICSMD50554.2020.9261709.
[39] M. Bronz, E. Baskaya, D. Delahaye, and S. Puechmore, “Real-time
fault detection on small fixed-wing UAVs using machine learning,” in
Proc. AIAA/IEEE 39th Digit. Avionics Syst. Conf. (DASC), Oct. 2020,
pp. 1–10, doi: 10.1109/DASC50938.2020.9256800.
[40] D. Muniraj and M. Farhood, “A framework for detection of sensor
attacks on small unmanned aircraft systems,” in Proc. Int. Conf.
Unmanned Aircr. Syst. (ICUAS), Jun. 2017, pp. 1189–1198.
[41] C. Iamsumang, A. Mosleh, and M. Modarres, “Monitoring and learning
algorithms for dynamic hybrid Bayesian network in on-line sys-
tem health management applications,” Rel. Eng. Syst. Saf., vol. 178,
pp. 118–129, Oct. 2018.
[42] E. Khalastchi, M. Kalech, and L. Rokach, “A hybrid approach for
improving unsupervised fault detection for robotic systems,” Expert
Syst. Appl., vol. 81, pp. 372–383, Sep. 2017.
[43] A. Alos and Z. Dahrouj, “Decision tree matrix algorithm for detecting
contextual faults in unmanned aerial vehicles,” J. Intell. Fuzzy Syst.,
vol. 38, no. 4, pp. 4929–4939, Apr. 2020.
[44] M. Ushaq and J. Fang, “A robust data fusion scheme for integrated navi-
gation systems employing fault detection methodology augmented with
fuzzy adaptive filtering,” in Proc. 6th Int. Symp. Precis. Mech. Meas.,
Oct. 2013, pp. 972–986.
[45] X. Yang, M. Warren, B. Arain, B. Upcroft, F. Gonzalez, and L. Mejias,
“A UKF-based estimation strategy for actuator fault detection of
UASs,” in Proc. Int. Conf. Unmanned Aircr. Syst. (ICUAS), May 2013,
pp. 516–525.
[46] C. Hajiyev and H. E. Soken, “Robust adaptive Kalman filter for
estimation of UAV dynamics in the presence of sensor/actuator faults,”
Aerosp. Sci. Technol., vol. 28, no. 1, pp. 376–383, Jul. 2013.
[47] F. Caliskan and C. Hajiyev, “Active fault-tolerant control of UAV
dynamics against sensor-actuator failures,” J. Aerosp. Eng., vol. 29,
no. 4, Jul. 2016, Art. no. 04016012.
[48] S. Y. Vural and C. Hacızade, “Sensor/actuator fault detection, isolation
and accommodation applied to UAV model,” J. Aeronaut. Space
Technol., vol. 9, pp. 1–12, Jan. 2016.
[49] D. Guo, M. Zhong, and D. Zhou, “Multisensor data-fusion-based
approach to airspeed measurement fault detection for unmanned aerial
vehicles,” IEEE Trans. Instrum. Meas., vol. 67, no. 2, pp. 317–327,
Feb. 2018.
[50] R. Sun, Q. Cheng, G. Wang, and W. Ochieng, “A novel online data-
driven algorithm for detecting UAV navigation sensor faults,” Sensors,
vol. 17, no. 10, p. 2243, Sep. 2017.
[51] X. Han et al., “Quadratic-Kalman-filter-based sensor fault detection
approach for unmanned aerial vehicles,” IEEE Sensors J., vol. 22,
no. 19, pp. 18669–18683, Oct. 2022.
[52] C.-C. Peng and Y.-H. Chen, “Fixed-wing unmanned aerial vehicle
rotary engine anomaly detection via online digital twin methods,” IEEE
Trans. Aerosp. Electron. Syst., vol. 60, no. 1, pp. 741–758, Feb. 2024.
[53] T. T., K. H. Low, and B. F. Ng, “Actuator fault detection and isolation
on multi-rotor UAV using extreme learning neuro-fuzzy systems,” ISA
Trans., vol. 138, pp. 168–185, Jul. 2023.
[54] S. Lee, W. Park, and S. Jung, “Fault detection of aircraft system
with random forest algorithm and similarity measure,” Sci. World J.,
vol. 2014, pp. 1–7, Jan. 2014.
[55] Z. Yao, C. Yang, Y. Peng, X. Zhang, and F. Chen, “A data-driven
fault detection approach for modular reconfigurable flying array based
on the improved deep forest,” Measurement, vol. 206, Jan. 2023,
Art. no. 112217.
[56] J.-H. Wang, Y.-X. Wang, and Y.-H. Zhu, “Bias compensation estimation
in multi-UAV formation and anomaly detection,” J. Control Syst. Eng.,
vol. 4, no. 1, pp. 40–50, Dec. 2016.
[57] Z. Birnbaum, A. Dolgikh, V. Skormin, E. O’Brien, D. Müller, and
C. Stracquodaine, “Unmanned aerial vehicle security using recursive
parameter estimation,” J. Intell. Robotic Syst., vol. 84, nos. 1–4,
pp. 107–120, Dec. 2016.
[58] W. Han, Z. Wang, and Y. Shen, “Fault estimation for a quadrotor
unmanned aerial vehicle by integrating the parity space approach with
recursive least squares,” Proc. Inst. Mech. Eng., G, J. Aerosp. Eng.,
vol. 232, no. 4, pp. 783–796, Mar. 2018.
[59] A. Keipour, M. Mousaei, and S. Scherer, “Automatic real-time
anomaly detection for autonomous aerial vehicles,” in Proc. Int.
Conf.
Robot.
Autom.
(ICRA),
May
2019,
pp. 5679–5685,
doi:
10.1109/ICRA.2019.8794286.
[60] E. Khalastchi, M. Kalech, G. A. Kaminka, and R. Lin, “Online data-
driven anomaly detection in autonomous robots,” Knowl. Inf. Syst.,
vol. 43, no. 3, pp. 657–688, Jun. 2015.
[61] G. Li and J. J. Jung, “Deep learning for anomaly detection in multivari-
ate time series: Approaches, applications, and challenges,” Inf. Fusion,
vol. 91, pp. 93–102, Mar. 2023.
[62] A. Alos and Z. Dahrouj, “Using MLSTM and multioutput convolutional
LSTM algorithms for detecting anomalous patterns in streamed data of
unmanned aerial vehicles,” IEEE Aerosp. Electron. Syst. Mag., vol. 37,
no. 6, pp. 6–15, Jun. 2022, doi: 10.1109/MAES.2021.3053108.
[63] B. Wang, D. Liu, Y. Peng, and X. Peng, “Multivariate regression-
based fault detection and recovery of UAV flight data,” IEEE Trans.
Instrum. Meas., vol. 69, no. 6, pp. 3527–3537, Jun. 2020, doi:
10.1109/TIM.2019.2935576.
[64] K. Guo, N. Wang, D. Liu, and X. Peng, “Uncertainty-aware
LSTM
based
dynamic
flight
fault
detection
for
UAV
actua-
tor,” IEEE Trans. Instrum. Meas., vol. 72, pp. 1–13, 2023, doi:
10.1109/TIM.2022.3225040.
[65] M. W. Ahmad, M. U. Akram, R. Ahmad, K. Hameed, and A. Hassan,
“Intelligent framework for automated failure prediction, detection,
and classification of mission critical autonomous flights,” ISA Trans.,
vol. 129, pp. 355–371, Oct. 2022, doi: 10.1016/j.isatra.2022.01.014.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:03:14 UTC from IEEE Xplore.  Restrictions apply.

## Page 14

31694
IEEE SENSORS JOURNAL, VOL. 24, NO. 20, 15 OCTOBER 2024
[66] K. H. Park, E. Park, and H. K. Kim, “Unsupervised fault detection
on unmanned aerial vehicles: Encoding and thresholding approach,”
Sensors, vol. 21, no. 6, p. 2208, Mar. 2021, doi: 10.3390/s21062208.
[67] H. Deng, Y. Lu, T. Yang, and X. Tang, “MMF: A fault detection model
for UAVs based on multimodal model fusion,” J. Phys. Conf. Ser.,
vol. 2593, Sep. 2023, Art. no. 012004.
[68] Y. Zhang, S. Li, Q. He, A. Zhang, C. Li, and Z. Liao, “An intel-
ligent fault detection framework for FW-UAV based on hybrid deep
domain adaptation networks and the Hampel filter,” Int. J. Intell. Syst.,
vol. 2023, pp. 1–19, Jun. 2023.
[69] V. Sadhu, K. Anjum, and D. Pompili, “On-board deep-learning-based
unmanned aerial vehicle fault cause detection and classification via
FPGAs,” IEEE Trans. Robot., vol. 39, no. 4, pp. 3319–3331, Aug. 2023,
doi: 10.1109/TRO.2023.3269380.
[70] V. Sadhu, S. Zonouz, and D. Pompili, “On-board deep-learning-based
unmanned aerial vehicle fault cause detection and identification,”
in
Proc.
IEEE
Int.
Conf.
Robot.
Autom.
(ICRA),
May
2020,
pp. 5255–5261.
[71] Y. He, Y. Peng, S. Wang, and D. Liu, “ADMOST: UAV flight
data anomaly detection and mitigation via online subspace track-
ing,” IEEE Trans. Instrum. Meas., vol. 68, no. 4, pp. 1035–1044,
Apr. 2019.
[72] Y. He, Y. Peng, S. Wang, D. Liu, and P. H. W. Leong, “A structured
sparse subspace learning algorithm for anomaly detection in UAV
flight data,” IEEE Trans. Instrum. Meas., vol. 67, no. 1, pp. 90–100,
Jan. 2018.
[73] W. Zhao, L. Li, S. Alam, and Y. Wang, “An incremental clustering
method for anomaly detection in flight data,” Transp. Res. C, Emerg.
Technol., vol. 132, Nov. 2021, Art. no. 103406.
[74] H. Lee, G. Li, A. Rai, and A. Chattopadhyay, “Real-time anomaly
detection framework using a support vector regression for the safety
monitoring of commercial aircraft,” Adv. Eng. Informat., vol. 44,
Apr. 2020, Art. no. 101071, doi: 10.1016/j.aei.2020.101071.
[75] L. Li, R. J. Hansman, R. Palacios, and R. Welsch, “Anomaly detec-
tion via a Gaussian mixture model for flight operation and safety
monitoring,” Transp. Res. C, Emerg. Technol., vol. 64, pp. 45–57,
Mar. 2016.
[76] E. Smart, D. Brown, and J. Denman, “A two-phase method of detecting
abnormalities in aircraft flight data and ranking their impact on
individual flights,” IEEE Trans. Intell. Transp. Syst., vol. 13, no. 3,
pp. 1253–1265, Sep. 2012.
[77] J. Wu, C. Hu, C. Sun, Z. Zhao, R. Yan, and X. Chen, “Helicopter
transmission system anomaly detection in variable flight regimes with
decoupling variational autoencoder,” Aerosp. Sci. Technol., vol. 144,
Jan. 2024, Art. no. 108764.
[78] V. Camerini, G. Coppotelli, and S. Bendisch, “Fault detection in
operating helicopter drivetrain components based on support vec-
tor data description,” Aerosp. Sci. Technol., vol. 73, pp. 48–60,
Feb. 2018.
[79] J. Zhong, Y. Zhang, J. Wang, C. Luo, and Q. Miao, “Unmanned
aerial vehicle flight data anomaly detection and recovery prediction
based on spatio-temporal correlation,” IEEE Trans. Rel., vol. 71, no. 1,
pp. 457–468, Mar. 2022, doi: 10.1109/TR.2021.3134369.
[80] Y. Wang, B. Wang, and D. Liu, “A subdivision method of flight phases
based on divide-and-conquer Gaussian mixture model,” IEEE Trans.
Instrum. Meas., vol. 72, pp. 1–11, 2023.
[81] A. Blázquez-García, A. Conde, U. Mori, and J. A. Lozano, “A review
on outlier/anomaly detection in time series data,” ACM Comput. Surv.,
vol. 54, no. 3, pp. 1–33, Apr. 2022.
[82] E. Keogh, J. Lin, S.-H. Lee, and H. V. Herle, “Finding the most unusual
time series subsequence: Algorithms and applications,” Knowl. Inf.
Syst., vol. 11, no. 1, pp. 1–27, Dec. 2006.
[83] Y. H. Gao, D. Zhao, and Y. B. Li, “UAV sensor fault diagnosis tech-
nology: A survey,” Appl. Mech. Mater., vols. 220–223, pp. 1833–1837,
Nov. 2012.
[84] P. Freeman, R. Pandita, N. Srivastava, and G. J. Balas, “Model-
based and data-driven fault detection performance for a small UAV,”
IEEE/ASME Trans. Mechatronics, vol. 18, no. 4, pp. 1300–1309,
Aug. 2013, doi: 10.1109/TMECH.2013.2258678.
[85] Q. I. Jun-Tong and H. Jian-Da, “Fault diagnosis and fault-tolerant
control of rotorcraft flying robots: A survey,” CAAI Trans. Intell. Syst.,
vol. 2, no. 2, pp. 31–39, 2007.
[86] K. Guo, L. Liu, S. Shi, D. Liu, and X. Peng, “UAV sensor fault
detection using a classifier without negative samples: A local density
regulated optimization algorithm,” Sensors, vol. 19, no. 4, p. 771,
Feb. 2019.
[87] X. Qi, D. Theilliol, J. Qi, Y. Zhang, and J. Han, “A literature review
on fault diagnosis methods for manned and unmanned helicopters,”
in Proc. Int. Conf. Unmanned Aircr. Syst. (ICUAS), May 2013,
pp. 1114–1118, doi: 10.1109/ICUAS.2013.6564801.
[88] L. Yang, S. Li, C. Li, C. Zhu, A. Zhang, and G. Liang, “Data-
driven unsupervised anomaly detection and recovery of unmanned
aerial vehicle flight data based on spatiotemporal correlation,” Sci.
China Technolog. Sci., vol. 66, no. 5, pp. 1304–1316, May 2023.
[89] S. Jeon, J. Kang, J. Kim, and H. Cha, “Detecting structural
anomalies of quadcopter UAVs based on LSTM autoencoder,” Per-
vas. Mobile Comput., vol. 88, Jan. 2023, Art. no. 101736, doi:
10.1016/j.pmcj.2022.101736.
[90] B. Wang, X. Peng, M. Jiang, and D. Liu, “Real-time fault detection
for UAV based on model acceleration engine,” IEEE Trans. Instrum.
Meas., vol. 69, no. 12, pp. 9505–9516, Dec. 2020.
[91] N. Wang, J. Ren, Y. Luo, K. Guo, and D. Liu, “UAV actuator fault
detection using maximal information coefficient and 1-D convolutional
neural network,” in Proc. Global Rel. Prognostics Health Manage.
(PHM-Nanjing), Oct. 2021, pp. 1–6.
[92] H. Ahn, “Deep learning based anomaly detection for a vehicle in swarm
drone system,” in Proc. Int. Conf. Unmanned Aircr. Syst. (ICUAS),
Sep. 2020, pp. 557–561.
[93] R. Dhakal, C. Bosma, P. Chaudhary, and L. N. Kandel, “UAV fault
and anomaly detection using autoencoders,” in Proc. IEEE/AIAA 42nd
Digit. Avionics Syst. Conf. (DASC), Oct. 2023, pp. 1–8.
[94] J. Kim, H. Kang, and P. Kang, “Time-series anomaly detection with
stacked transformer representations and 1D convolutional network,”
Eng. Appl. Artif. Intell., vol. 120, Apr. 2023, Art. no. 105964.
[95] B. Wang, Z. Wang, L. Liu, D. Liu, and X. Peng, “Data-driven anomaly
detection for UAV sensor data based on deep learning prediction
model,” in Proc. Prognostics Syst. Health Manage. Conf. (PHM-Paris),
May 2019, pp. 286–290, doi: 10.1109/PHM-Paris.2019.00055.
[96] H. Ahn, H.-L. Choi, M. Kang, and S. Moon, “Learning-based anomaly
detection and monitoring for swarm drone flights,” Appl. Sci., vol. 9,
no. 24, p. 5477, Dec. 2019.
[97] J. Galvan, A. Raja, Y. Li, and J. Yuan, “Sensor data-driven UAV
anomaly detection using deep learning approach,” in Proc. MILCOM
IEEE Mil. Commun. Conf. (MILCOM), Nov. 2021, pp. 589–594.
[98] B. Chen, Y. Peng, B. Gu, Y. Luo, and D. Liu, “A fault detection method
based on enhanced GRU,” in Proc. Int. Conf. Sens., Meas. Data Anal.
Era Artif. Intell. (ICSMD), Oct. 2021, pp. 1–4.
[99] K. He, D. Yu, D. Wang, M. Chai, S. Lei, and C. Zhou, “Graph attention
network-based fault detection for UAVs with multivariant time series
flight data,” IEEE Trans. Instrum. Meas., vol. 71, pp. 1–13, 2022.
[100] J. You, J. Liang, and D. Liu, “An adaptable UAV sensor data anomaly
detection method based on TCN model transferring,” in Proc. Prog-
nostics Health Manage. Conf. (PHM- London), May 2022, pp. 73–76,
doi: 10.1109/PHM2022-London52454.2022.00021.
[101] J.-H. Park, S. Shanbhag, and D. E. Chang, “Model-free unsupervised
anomaly detection of a general robotic system using a stacked LSTM
and its application to a fixed-wing unmanned aerial vehicle,” in
Proc. IEEE/RSJ Int. Conf. Intell. Robots Syst. (IROS), Oct. 2022,
pp. 4287–4293.
[102] M. Jia, A. Raja, and J. Yuan, “A hybrid delay-aware approach towards
UAV flight data anomaly detection,” in Proc. Int. Conf. Comput., Netw.
Commun. (ICNC), Feb. 2023, pp. 176–180.
[103] D. Liu, N. Wang, K. Guo, and B. Wang, “Ensemble transfer
learning based cross-domain UAV actuator fault detection,” IEEE
Sensors J., vol. 23, no. 14, pp. 16363–16372, Jul. 2023, doi:
10.1109/JSEN.2023.3280571.
[104] X. Zhou, X. Chu, and Y. Zou, “Sensor fault detection for UAVs
based on MIC-LSTM with attention mechanism,” in Proc. CAA Symp.
Fault Detection, Supervision Saf. Tech. Processes (SAFEPROCESS),
Sep. 2023, pp. 1–6.
[105] J. Elman, “Finding structure in time,” Cognit. Sci., vol. 14, no. 2,
pp. 179–211, Jun. 1990.
[106] A. Graves, “Long short-term memory,” in Supervised Sequence
Labelling with Recurrent Neural Networks. Berlin, Germany: Springer,
2012, pp. 37–45, doi: 10.1007/978-3-642-24797-2_4.
[107] T. Kattenborn, J. Leitloff, F. Schiefer, and S. Hinz, “Review on
convolutional neural networks (CNN) in vegetation remote sensing,”
ISPRS J. Photogramm. Remote Sens., vol. 173, pp. 24–49, Mar. 2021.
[108] Z. Li, F. Liu, W. Yang, S. Peng, and J. Zhou, “A survey of convolutional
neural networks: Analysis, applications, and prospects,” IEEE Trans.
Neural Netw. Learn. Syst., vol. 33, no. 12, pp. 6999–7019, Dec. 2022.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:03:14 UTC from IEEE Xplore.  Restrictions apply.

## Page 15

YANG et al.: DEEP LEARNING-ASSISTED UAV FLIGHT DATA ANOMALY DETECTION: A REVIEW
31695
[109] Y. Zhang, Y. Chen, J. Wang, and Z. Pan, “Unsupervised deep anomaly
detection for multi-sensor time-series signals,” IEEE Trans. Knowl.
Data Eng., vol. 35, no. 2, pp. 2118–2132, Feb. 2023.
[110] Z. Xu, Z. Cheng, and B. Guo, “A multivariate anomaly detector for
satellite telemetry data using temporal attention-based LSTM autoen-
coder,” IEEE Trans. Instrum. Meas., vol. 72, pp. 1–13, 2023.
[111] G. Bae and I. Joe, “UAV anomaly detection with distributed artificial
intelligence based on LSTM-AE and AE,” in Proc. Int. Conf. Multi-
media Ubiquitous Eng., Aug. 2020, pp. 305–310.
[112] I.
M.
Arce,
J.
M.
Mase,
D.
Rengasamy,
B.
Rothwell,
and
G. P. Figueredo, “Anomaly detection for unmanned aerial vehicle sen-
sor data using a stacked recurrent autoencoder method with dynamic
thresholding,” SAE Int. J. Aerosp., vol. 15, no. 2, pp. 219–229,
Sep. 2022, doi: 10.4271/01-15-02-0017.
[113] L. Gao, C. Xu, F. Wang, J. Wu, and H. Su, “Flight data outlier detection
by constrained LSTM-autoencoder,” Wireless Netw., vol. 29, no. 7,
pp. 3051–3061, Oct. 2023.
[114] Y. Ma, M. N. A. Islam, J. Cleland-Huang, and N. V. Chawla, “Detecting
anomalies in small unmanned aerial systems via graphical normalizing
flows,” IEEE Intell. Syst., vol. 38, no. 2, pp. 46–54, Mar. 2023.
[115] D. E. Rumelhart, G. E. Hinton, and R. J. Williams, “Learning rep-
resentations by back-propagating errors,” Nature, vol. 323, no. 6088,
pp. 533–536, Oct. 1986.
[116] W. Sun, S. Shao, R. Zhao, R. Yan, X. Zhang, and X. Chen, “A sparse
auto-encoder-based deep neural network approach for induction motor
faults classification,” Measurement, vol. 89, pp. 171–178, Jul. 2016.
[117] M. Schuster and K. K. Paliwal, “Bidirectional recurrent neural net-
works,” IEEE Trans. Signal Process., vol. 45, no. 11, pp. 2673–2681,
Sep. 1997, doi: 10.1109/78.650093.
[118] Y. Li, Q. Pan, S. Wang, H. Peng, T. Yang, and E. Cambria, “Disentan-
gled variational auto-encoder for semi-supervised learning,” Inf. Sci.,
vol. 482, pp. 73–85, May 2019.
[119] T. Jing, P. Zheng, L. Xia, and T. Liu, “Transformer-based hierarchical
latent space VAE for interpretable remaining useful life prediction,”
Adv. Eng. Informat., vol. 54, Oct. 2022, Art. no. 101781.
[120] D. Chakraborty and H. Elzarka, “Early detection of faults in HVAC
systems using an XGBoost model with a dynamic threshold,” Energy
Buildings, vol. 185, pp. 326–344, Feb. 2019.
[121] Z. Wang and A. C. Bovik, “Mean squared error: Love it or leave it?
A new look at signal fidelity measures,” IEEE Signal Process. Mag.,
vol. 26, no. 1, pp. 98–117, Jan. 2009.
[122] L. S. Nelson, “The shewhart control chart—Tests for special causes,”
J. Quality Technol., vol. 16, no. 4, pp. 237–239, Oct. 1984.
[123] J. U. Ko, K. Na, J.-S. Oh, J. Kim, and B. D. Youn, “A new auto-
encoder-based dynamic threshold to reduce false alarm rate for anomaly
detection of steam turbines,” Expert Syst. Appl., vol. 189, Mar. 2022,
Art. no. 116094.
[124] H. Chen, H. Liu, X. Chu, Q. Liu, and D. Xue, “Anomaly detection
and critical SCADA parameters identification for wind turbines based
on LSTM-AE neural network,” Renew. Energy, vol. 172, pp. 829–840,
Jul. 2021.
[125] A. Wang, Y. Pei, Z. Qian, H. Zareipour, B. Jing, and J. An, “A two-stage
anomaly decomposition scheme based on multi-variable correlation
extraction for wind turbine fault detection and identification,” Appl.
Energy, vol. 321, Sep. 2022, Art. no. 119373.
[126] N. Madan et al., “Self-supervised masked convolutional transformer
block for anomaly detection,” IEEE Trans. Pattern Anal. Mach. Intell.,
vol. 46, no. 1, pp. 525–542, Jan. 2024.
[127] Y. Fu et al., “DepthShrinker: A new compression paradigm towards
boosting real-hardware efficiency of compact neural networks,” in Proc.
Int. Conf. Mach. Learn., 2022, pp. 6849–6862.
[128] C. Ding, S. Sun, and J. Zhao, “MST-GAT: A multimodal spatial–
temporal graph attention network for time series anomaly detection,”
Inf. Fusion, vol. 89, pp. 527–536, Jan. 2023.
[129] G. Michau and O. Fink, “Unsupervised transfer learning for anomaly
detection: Application to complementary operating condition transfer,”
Knowl.-Based Syst., vol. 216, Mar. 2021, Art. no. 106816.
[130] M. Christoph, Interpretable Machine Learning: A Guide for Mak-
ing Black Box Models Explainable. Victoria, BC, Canada: Leanpub,
2020.
[131] M.T. Ribeiro, S. Singh, and C. Guestrin, “‘Why should I trust
you?’ Explaining the predictions of any classifier,” in Proc. 22nd
ACM SIGKDD Int. Conf. Knowl. Discovery Data Mining, 2016,
pp. 1135–1144.
[132] Y. Gao, S. Miyata, and Y. Akashi, “How to improve the application
potential of deep learning model in HVAC fault diagnosis: Based
on pruning and interpretable deep learning method,” Appl. Energy,
vol. 348, Oct. 2023, Art. no. 121591.
Lei
Yang
received
the
B.S.
degree
in
mechanical
engineering
from
Guizhou
University, Guiyang, China, in 2020, where
he is currently pursuing the Ph.D. degree with
the School of Mechanical Engineering.
His
research
interests
include
unmanned
aerial vehicles, anomaly detection, intelligent
fault diagnosis, deep learning, and machine
learning.
Shaobo Li received the Ph.D. degree in com-
puter software and theory from the Chinese
Academy of Sciences, Beijing, China, in 2003.
From 2007 to 2015, he was the Vice Director
of the Key Laboratory of Advanced Manufactur-
ing Technology, Ministry of Education, Guizhou
University, Guiyang, China, where he was the
Dean of the School of Mechanical Engineering,
from 2015 to 2021. Since 2021, he has been the
Director of the State Key Laboratory of Public Big
Data, Guizhou University, where he is currently
a Professor. Since 2024, he has been the Vice Dean of the School
of Mechanical Engineering, Guizhou Institute of Technology, Guiyang.
He is also a part-time Doctoral Tutor with the Chinese Academy of
Sciences. He has authored or co-authored more than 200 papers in
major journals and international conferences. His research has been
supported by the National Science Foundation of China and the National
High-Tech Research and Development Program (863 Program). His cur-
rent research interests include big data on manufacturing and intelligent
manufacturing.
Dr. Li received honors and awards from the New Century Excellent
Talents of University of Ministry of Education of China and the Excel-
lent Expert and Innovative Talent of Guizhou, the Group Leader of
Manufacturing Informatization, and the Alliance Vice Chairperson of the
Intelligent Manufacturing Industry, Guizhou, China.
Yizong Zhang is currently pursuing the Ph.D.
degree with the School of Mechanical Engineer-
ing, Guizhou University, Guiyang, China.
His research interests include fault diagnosis
and signal processing.
Caichao Zhu received the Ph.D. degree from
Chongqing
University,
Chongqing,
China,
in 1998.
He is currently a Professor with the State Key
Laboratory
of
Mechanical
Transmissions,
Chongqing
University.
His
current
research
interests include key technologies for gear
transmission design and manufacturing of high-
end equipment, new precision gear transmission
and drive, and transmission system dynamics.
Zihao Liao is currently pursuing the Ph.D.
degree with the State Key Laboratory of Public
Big Data, Guizhou University, Guiyang, China.
His research interests include deep learning
and time series data prediction.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:03:14 UTC from IEEE Xplore.  Restrictions apply.
