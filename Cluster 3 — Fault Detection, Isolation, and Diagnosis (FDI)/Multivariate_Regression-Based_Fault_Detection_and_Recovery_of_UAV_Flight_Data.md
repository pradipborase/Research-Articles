# Multivariate_Regression-Based_Fault_Detection_and_Recovery_of_UAV_Flight_Data.pdf

## Page 1

IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 69, NO. 6, JUNE 2020
3527
Multivariate Regression-Based Fault Detection
and Recovery of UAV Flight Data
Benkuan Wang, Student Member, IEEE, Datong Liu
, Senior Member, IEEE,
Yu Peng, Member, IEEE, and Xiyuan Peng
Abstract—With the wide applications of the unmanned aerial
vehicle (UAV), operating safety becomes a critical issue. Thus,
fault detection (FD) has been focused, which can realize fault
alarm and schedule maintenance in time. Since the accurate
physical model of UAV is usually difﬁcult to obtain and ﬂight data
with random noise has both spatial and temporal correlation,
a huge challenge is posed to FD. In this article, a data-driven
multivariate regression approach based on long short-term mem-
ory with residual ﬁltering (LSTM-RF) is proposed to fulﬁll UAV
ﬂight data FD and recovery. First, an LSTM network is designed
as a regression model, which can extract the spatial–temporal
features from the ﬂight data and obtain an estimation of the
monitored parameter. Second, a ﬁlter is utilized to smooth
the residuals between real ﬂight data and estimated values,
which mitigates the effect of random noise and dramatically
improves the detection performance. Finally, FD is achieved by
comparing the smoothed residual with a statistical threshold.
Then, fault recovery is fulﬁlled by replacing fault data with the
estimated value. To validate the effectiveness of the proposed
method, experiments are conducted based on simulation data
and real ﬂight data. The experimental results demonstrate that
the proposed method has good performance in FD and recovery
of UAV ﬂight data.
Index Terms—Fault detection (FD), fault recovery,
long
short-term memory (LSTM), multivariate regression, unmanned
aerial vehicle (UAV).
I. INTRODUCTION
A
S a reusable unmanned aircraft which can be controlled
remotely or automatically [1], unmanned aerial vehicle
(UAV) has received extensive attention. The functions of UAV
are constantly enriched which make it possible to conduct
more complex tasks, such as aerial imagery [2], agriculture,
emergency rescue [3], [4], and riverbank monitoring [5].
However, compared with manned aircraft, UAV lacks real-time
control from the pilot, and there are restrictions on develop-
ment costs. Thus, the safety of the UAV is relatively lower.
To address this issue, UAV fault detection (FD) is widely
adopted, which can achieve FD in advance. Then, mainte-
nance scheduling or mission replanning can be carried out
Manuscript received May 13, 2019; revised July 8, 2019; accepted August 1,
2019. Date of publication August 15, 2019; date of current version May 12,
2020. This work was supported in part by the National Natural Sci-
ence Foundation of China under Grant 61571160, Grant 61803121, and
Grant 61771157. The Associate Editor coordinating the review process was
Massimo Lazzaroni. (Corresponding author: Datong Liu.)
The authors are with the School of Electronics and Information Engi-
neering, Harbin Institute of Technology, Harbin 150080, China (e-mail:
liudatong@hit.edu.cn).
Color versions of one or more of the ﬁgures in this article are available
online at http://ieeexplore.ieee.org.
Digital Object Identiﬁer 10.1109/TIM.2019.2935576
to prevent a catastrophic accident. Flight data made up by
a variety of sensor readings are the primary basis for UAV
FD, which usually include inertial measurement unit (IMU),
Global Positioning System (GPS), and Pitot tube. Analytical
redundancy can be obtained by FD of ﬂight data, which can
improve the UAV ﬂight safety and reliability [6].
Considerable research has been conducted for UAV FD,
which can be divided into two major categories: model-based
methods and data-driven methods. In general, the model-
based methods mainly integrate with Kalman ﬁlter (KF) or its
variants by establishing a physical model as the state transition
equation [7]. Yi and Zhang [8] presented a model-based FD
method based on particle ﬁlter (PF). Guo et al. [9] utilized
the extended Kalman ﬁlter (EKF) and the UAV kinematics
model to provide analytical redundancy. Vitanov and Aouf [10]
used an enhanced unscented Kalman ﬁlter (UKF) to detect
inertial navigation system faults. Liu et al. [11] introduced
an adaptive estimation method based on a bank of UKFs to
monitor the actuators’ health in a UAV. Abbaspour et al. [12]
developed an FD strategy for sensors and actuators based on
neural network and EKF. Although the model-based methods
can realize FD and parameter tracking, in most cases, it is
difﬁcult and costly to obtain or establish an accurate physical
model of the UAV system. Furthermore, the complex model
is usually hard to apply in an embedded platform to meet
real-time requirements.
The data-driven methods do not require accurate physical
models and can obtain information through historical ﬂight
data. Baskaya et al. [13] proposed a classiﬁcation method
based on support vector machine to detect faults of UAV
control surfaces. Wang et al. [14] designed an embedded
system for UAV anomaly detection based on least-squares
support vector machine (LS-SVM). Youseﬁet al. [15] pre-
sented a supervised UAV faults prediction method based
on the logistic regression and linear discriminant analysis.
Khalastchi et al. [16] developed an FD approach for UAV
based on Mahalanobis distance. He et al. [17], [18] proposed
an anomaly detection and mitigation algorithm based on online
subspace tracking. In addition, research on deep learning-
based monitoring method is developing rapidly [19], [20].
Nanduri and Sherry [21] utilized an FD method based
on recurrent neural networks (RNNs) to detect ﬂight data
faults. Hundman et al. [22] used long short-term mem-
ory (LSTM)-based anomaly thresholding approach to realize
anomaly detection. However, most of these methods only con-
0018-9456 © 2019 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:36:17 UTC from IEEE Xplore.  Restrictions apply.

## Page 2

3528
IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 69, NO. 6, JUNE 2020
sider the spatial correlation between multiple parameters or the
temporal correlation of a single parameter, which will reduce
the FD performance when the complex spatial–temporal cor-
relation is involved in the data. Furthermore, there is unpre-
dictable random noise in the ﬂight data; the performance of
the regression-based FD model will decline when dealing with
minor faults.
In summary, detecting the minor faults from ﬂight data
which has spatial–temporal correlation and random noise
remains a challenge. In addition, fault recovery or mitigation
is of great importance in practical applications when a fault
is discovered. Since UAV is a closed-loop control system and
the other ﬂight data will quickly return to normal when the
sensor has a minor fault [6], it provides the possibility of FD
and recovery by multivariate regression analysis [23]–[25].
In this article, to capture more fault information, mitigate
the impact of random noise in ﬂight data, and simultaneously
achieve rapid recovery from a failure, a data-driven FD
and recovery approach based on LSTM regression model
with residual ﬁltering (LSTM-RF) is proposed. The main
contributions are as follows. First, a multivariate regression
model based on LSTM is designed to automatically extract
the spatial–temporal features from ﬂight data and give a
more accurate estimation of the monitored parameter. Then,
FD and recovery requirements are turned into regression
issue. Second, a ﬁlter method is used to smooth the residuals
between the actual ﬂight data and the estimated values. The
effect of random noise on FD performance is reduced, which
means the sensitivity of the FD model to noise is decreased
and minor faults are more likely to be detected. Finally,
a statistical threshold is calculated by the smoothed residuals,
and FD can be realized by comparing the statistical threshold
and the residuals. It is worth mentioning that the designed
model can not only realize FD but also achieve the recovery
of the monitored parameter when a fault occurs, which is
very practical in real ﬂight.
The rest of this article is organized as follows. Section II
introduces the UAV research platform and fault scenarios
involved in this study. Section III presents the proposed
approach for UAV ﬂight data FD. Section IV introduced the
FD metrics and the experimental results. Section V concludes
this article and indicates future work.
II. UAV RESEARCH PLATFORM AND FAULT SCENARIOS
A. Research Platform
1) Simulation Platform: Due to fewer fault samples in
actual ﬂight data, the linear simulation model developed by the
University of Minnesota, Minneapolis, MN, USA, is adopted
to generate fault sensor data in this study [26]. The model
is built in the MATLAB simulation environment for a small
ﬁxed-wing UAV called the Ultrastick 25e, and the simulation
step size is 20 ms. The main components of the simulation
model are shown in Fig. 1.
Control input generator is utilized to set maneuver com-
mands, such as attitude angle, altitude, and velocity. The
control software can adjust the UAV to the desired attitude.
Actuators are used to simulate throttle, aileron, rudder, and
Fig. 1.
Structure of the linear simulation model.
Fig. 2.
Real UAV ﬂight platform and its normalized ﬂight trajectory.
elevator. Airframe linear module contains lateral directional
aircraft dynamics and longitudinal directional aircraft dynam-
ics. All simulated sensors are in the sensors module.
In this article, we focused on the FD of lateral directional
aircraft dynamics related sensors marked by a rectangle in
Fig. 1, and different fault patterns are injected. The ﬂight data
of interest is roll rate p, which is directly generated by the
gyroscope sensor. By monitoring the roll rate, it is possible to
detect whether the x-axis of the gyroscope sensor is faulty.
2) Real UAV Flight Platform: Besides the simulation model,
we also built an actual small ﬁxed-wing UAV shown in
Fig. 2 to generate actual ﬂight data.
The small UAV has a 2.1-m wingspan and 5.5-kg takeoff
weight. An open-source autopilot named Pixhawk2.4.6 is
used for ﬂight control and management of the UAV. The
hardware of the autopilot contains one main processor
(STM32F427), one coprocessor (STM32F103), MPU6000
IMU, MS5611 barometer, M8N GPS, etc. The software of
the autopilot is ardupilot ﬁrmware (version: 3.10.0), which
mainly realizes ﬂight mode and task management, attitude
control, and position control. The autopilot enables the UAV
to achieve manual or autonomous ﬂight. The actual ﬂight data
are collected by autonomous ﬂight, and the normalized ﬂight
trajectory of the UAV is also shown in Fig. 2. It can be seen
that the small UAV ﬂies to a stable altitude after taking off
and circulates in a rectangular trajectory.
B. Fault Scenarios Consideration
UAV senses its current attitude and position through air-
borne sensors. Then, the ﬂight control software calculates
the control value of the actuator, and the adjustment of the
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:36:17 UTC from IEEE Xplore.  Restrictions apply.

## Page 3

WANG et al.: MULTIVARIATE REGRESSION-BASED FD AND RECOVERY OF UAV FLIGHT DATA
3529
Fig. 3.
Roll angle command in ﬂight simulation.
UAV attitude is realized. Finally, the UAV will approach
the expected ﬂight status. In the closed-loop control system,
sensors provide measurement feedback. Hence, sensor faults
affect ﬂight safety if left undetected. The fault scenarios
considered in this work are gyroscope sensor faults.
The typical UAV airborne sensor faults are bias and drift.
These two fault patterns can be denoted as follows [27]:
yfault =

y(t) + d,
bias
y(t) + k × t, drift
(1)
where y(t) and yfault are normal and fault ﬂight data, respec-
tively. d is a constant, and k represents the rate of drift. Both
bias fault and drift fault are modeled as additive failures. Since
the roll angle control loop uses a roll rate p for feedback, bias
or drift on p will inﬂuence the command execution.
Assuming that minor fault occurs during the operation of
the gyroscope, the autopilot can overcome the effects of the
roll rate fault and return to the normal control quickly. Thus,
minor faults are easily ignored. To reproduce this situation,
two simulated minor fault scenarios applied to the simulation
model of Ultrastick 25e are considered:
1) 10◦/s roll rate bias;
2) 2.86◦/s2 roll rate drift.
Faulty ﬂight simulation is run for data collection. The
maneuver for ﬂight test is a series of roll doublets of random
varying magnitude. To fulﬁll this, roll angle command φcmd
shown in Fig. 3 is set in control input generator.
Two fault scenarios are injected into the gyroscope sensor
in the simulation model, and the roll rate affected by the faults
is shown in Fig. 4. The solid line indicates the normal roll rate
under the control of the given roll angle command φcmd. For
bias fault, it starts at the 750th sampling point and ends at the
end of the simulation. The bias is 10◦/s, which is marked as a
dashed line. Drift fault starts at the 750th sampling point and
ends at the end of the simulation. The drift is 2.86◦/s2, which
is marked as a dashed-dotted line.
After the faults are injected into the simulation model,
the response of the roll angle under the closed-loop control
is shown in Fig. 5. The solid line indicates the normal roll
angle under the control of φcmd. The dashed line is the roll
angle after bias fault injection. It can be seen that the roll
angle is affected at the beginning of the fault, but the deviation
from normal data is small. After that, the fault data are almost
identical to the normal data. The dashed-dotted line denotes
the roll angle after drift fault injection. Since the drift fault is
Fig. 4.
Roll rate of Ultrastick 25e model affected by different faults.
Fig. 5.
Roll angle of Ultrastick 25e model affected by different faults.
a gradual process, the fault data are similar to the normal data
under the closed-loop control.
In summary, the control software can successfully track the
reference signal φcmd. Despite the injection of minor faults
in the simulated gyroscope sensor, the overall impact on the
roll angle is small. This provides the possibility of sensor FD
by the other normal parameters. Furthermore, since there is no
fault in the actual ﬂight data, we apply the same fault scenarios
as the simulation model to the real ﬁxed-wing UAV, which
means these two types of faults are also injected into the real
gyroscope sensor data collected by the autopilot in Fig. 2.
III. MULTIVARIATE REGRESSION-BASED
FAULT DETECTION
In this section, ﬁrst, the LSTM neural network is introduced.
Then, a multivariate regression model is designed based on
LSTM. Finally, an FD method is proposed.
A. LSTM Neural Network
LSTM is a speciﬁc type of RNN which is designed to
improve the problem of gradient vanishing [28]. It has been
proved to be a powerful method to solve the issue of multidi-
mensional time-series prediction, especially for the series with
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:36:17 UTC from IEEE Xplore.  Restrictions apply.

## Page 4

3530
IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 69, NO. 6, JUNE 2020
Fig. 6.
Structure of LSTM memory cell in LSTM neural network.
long-term dependencies [29]. Therefore, LSTM is selected as
the prediction algorithm which can extract spatial and temporal
features from the multidimensional ﬂight data.
In the LSTM neural network, the hidden layer node referred
to LSTM memory cell is shown in Fig. 6 [30]. It contains
three gates: input gate, forget gate, and output gate. The new
information of the multidimensional ﬂight data can be updated
and outputted via this memory cell. This cell makes the LSTM
has strong ability of long-term temporal feature memory.
When a new input xt ∈Rd×1 of the d dimensional ﬂight
data enters the LSTM network at time t, the new information
is remembered by memory cell states updating. The number of
hidden nodes in the LSTM network is k, and the hidden states
and cell states of memory cells at time t −1 are denoted by
ht−1 ∈Rk×1 and ct−1 ∈Rk×1, respectively. The cell states ct
and hidden states ht update formulas in LSTM memory cells
are as follows:
ft = σ(w f · [ht−1, xt] + b f )
(2)
it = σ(wi · [ht−1, xt] + bi)
(3)
˜ct = tanh(wc · [ht−1, xt] + bc)
(4)
ct = ft ∗ct−1 + it ∗˜ct
(5)
ot = σ(wo · [ht−1, xt] + bo)
(6)
ht = ot ∗tanh(ct)
(7)
where w f ∈Rk×(d+k), wi ∈Rk×(d+k), wo ∈Rk×(d+k), and
wc ∈Rk×(d+k) represent the connection weights of the forget
gate ft, input gate it, output gate ot, and memory cell ˜ct,
respectively. b f ∈Rk×1, bi ∈Rk×1, bo ∈Rk×1, and bc ∈
Rk×1 are the biases of each gate. ct and ct−1 mean the states of
memory cell at the present moment and the previous moment,
respectively. ˜ct is the intermediate parameter used to update
the cell state. In addition, σ and tanh refer to sigmoid and
hyperbolic tangent activation function, respectively, and “∗”
denotes the Hadamard product.
With (2)–(7), the information up to time t is stored in these
LSTM memory cells, and ht is also the current output of the
LSTM network. By iterative updating, the hidden patterns of
ﬂight data will be automatically learned, and the predicted
value of the monitored parameter will be obtained based on
the input sequence.
B. Multivariate Regression Model Based on LSTM
An LSTM model is designed to fulﬁll time-series prediction,
which means that the value of next moment can be inferred
TABLE I
PARAMETERS USED FOR REGRESSION
Fig. 7.
Sliding process demonstration.
via historical data [31]. Hence, we can obtain an estimated
value of the monitored parameter by building an LSTM
regression model. In this work, 11 parameters related to UAV
attitude closed-loop control are used for regression, and their
corresponding units are shown in Table I.
Assuming the ﬂight parameters in Table I have L samples,
the ﬂight data can be denoted as follows:
X =
⎡
⎢⎢⎣
x11, x12, . . . , x1L
x21, x22, . . . , x2L
. . .
xd1, xd2, . . . , xdL
⎤
⎥⎥⎦,
xij ∈R
(8)
where d = 11, which is the number of the ﬂight parameters.
i is the ith parameter. j is the jth sampling point.
The roll rate p is selected as the monitored parameter for
demonstration. To realize the roll rate regression, the form of
the input time series needs to be reconstructed as follows:
Xt =
⎡
⎢⎢⎣
x1,t−D+1, x1,t−D+2, . . . , x1,t
x2,t−D+1, x2,t−D+2, . . . , x2,t
. . .
xd,t−D+1, xd,t−D+1, . . . , xd,t
⎤
⎥⎥⎦,
Yt = [xm,t+1]
(9)
where Xt is the input of the regression model at time t.
Yt is the target output which indicates the monitored para-
meter roll rate p. m is used to indicate which parameter is
being monitored. D is the length of a sliding window, which
determines the length of the data sequence associated with the
next moment. The sliding process is demonstrated in Fig. 7.
After the reconstruction, we get the inputs of the regression
model and the corresponding target outputs. Each element of
the inputs is a matrix Xt ∈Rd×D, and each element of the
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:36:17 UTC from IEEE Xplore.  Restrictions apply.

## Page 5

WANG et al.: MULTIVARIATE REGRESSION-BASED FD AND RECOVERY OF UAV FLIGHT DATA
3531
Fig. 8.
Structure of the designed multivariate regression model.
target outputs is a scalar Yt ∈R. Then, the LSTM-based
regression model needs to learn the mapping function Yt =
f (Xt), and the structure of the model is shown in Fig. 8.
There are three layers in total. To meet the needs of
mapping between a matrix and a scalar, the input dimension
of the model should be d, and the output dimension of the
model should be one. LSTM layer is composed of LSTM
memory cells shown in Fig. 6. Xt enters the memory cells
by column. When the nth column enters, the input xt is Xt,n;
then, the cell states ct and hidden states ht of these cells
are updated by (2)–(7). As the input data have temporal
correlation, the time step of LSTM layer is set to D, which
indicates that the ﬁnal hidden states ht of the memory cells
are output to the output layer after D updates. The ﬁnal output
of the regression model is obtained via Yt = wol · ht, where
wol ∈R1×k represent the connection weights of the output
layer.
In practice, the window length D and the number of LSTM
hidden nodes need to be optimized according to the model
performance, which will be determined during the training
phase of the regression model.
C. FD Method Based on LSTM With Residual Filtering
In order to realize the FD of ﬂight data, we take full
advantage of the characteristic of the closed-loop control
and turn FD issue into multivariate regression and threshold
comparison problem. The proposed FD method realizes the
reconstruction of the fault parameter while implementing FD,
which makes great sense for the rapid recovery of faults in
actual ﬂight. The schematic of the proposed method is shown
in Fig. 9, which is mainly divided into two parts: model
training and FD. Details are shown as follows:
1) Model Training: Since the proposed method is a semi-
supervised data-driven method, the ﬂight data used during the
training phase must be normal data. Thereby, the normal ﬂight
pattern can be learned by the regression model. The speciﬁc
steps are as follows.
1) Flight Data Normalization: Normalizing all ﬂight data
shown in Table I by using the z-score method, which is
denoted as follows:
Xz-score = X −μ
σ
(10)
where μ is the mean of raw data X, and σ is the standard
deviation of X.
2) Flight Data Reconstruction: Reconstructing the normal-
ized ﬂight data according to (9), and the length D of the
sliding window varies from 1 to 50. We select a window
length each time and build the input and output pairs for
model training as follows:

XR = {X1, X2, · · ·, XL−D},
Xi ∈Rd×D
YR ={xm,D+1, xm,D+2, · · ·, xm,L}, xm,i ∈R
(11)
where L is the length of the whole ﬂight data, and
m denotes the mth parameter in the ﬂight data.
3) Regression Model Training:
Using the structure of the designed LSTM regression
model shown in Fig. 8 to realize the mapping function
fLSTM(·)
ˆY R = fLSTM(XR).
(12)
The objective of the mapping function training is to
minimize the regression loss function J which can be
deﬁned as follows:
J = 1
2
L−D
	
i=1
(yi −ˆyi)2
(13)
where yi is the ith element in YR, and ˆyi is the estimated
value of yi, which is calculated by the regression model.
During the model training, L2 regularization is applied
to the loss function J to avoid overﬁtting. Since the
monitored parameter may also have temporal correla-
tion, the monitored parameter is retained at the input,
and a penalty factor C ∈[0, 1] is introduced to reduce
the impact of failure on the regression performance.
Moreover, the window length D is adjusted according
to the model performance, and the model training step
is repeated.
4) Detection Threshold Calculation: We assume that the
distribution of ﬂight data is similar in the same ﬂight
mode, so we calculate the threshold for FD by the
residuals between the estimated values ˆY R and actual
ﬂight data YR. The residuals are denoted as follows:
etrain = YR −ˆY R.
(14)
Due to the presence of noise, the ﬂuctuation of residuals
is drastic. To address this issue, we utilize a low-
pass inﬁnite impulse response (IIR) ﬁlter to smooth the
residuals for promoting the FD performance, which is
deﬁned as follows:

esmooth,1 = etrain,1
esmooth,i =βesmooth,i−1+(1−β)etrain,i,
i ≥2
(15)
where β is the ﬁlter coefﬁcient, and it varies from 0 to 1.
Calculating the FD threshold by the smoothed residuals
as follows:
T = μe + α × δe
(16)
where μe is the mean of esmooth, and δe is the standard
deviation of esmooth [32], [33]. α is a constant and usu-
ally sets to 2.6 when 99% conﬁdence level is required.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:36:17 UTC from IEEE Xplore.  Restrictions apply.

## Page 6

3532
IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 69, NO. 6, JUNE 2020
Fig. 9.
Schematic of the proposed multivariate regression FD model.
Fig. 10.
Flowchart of the proposed FD method.
2) Fault Detection: The detailed ﬂowchart of this FD
method is shown in Fig. 10 which can be illustrated from
the following two aspects.
1) Flight Data Preprocessing:
The ﬂight data X are normalized by using (10). Then,
the normalized data are reconstructed with the window
length D optimized during the model training phase by
using (11). The total length of the data to be detected
is N. The new ﬂight data are reconstructed in the form
as follows:

Xtest={X1, X2, . . . , XN−D},
Xi ∈Rd×D
Ytest={xm,D+1, xm,D+2, . . . , xm,N},
xm,i ∈R
(17)
2) Regression and FD: Substituting Xtest into the optimized
multivariate regression model (12), we get the estimated
values as follows:
ˆY test = fLSTM(Xtest).
(18)
Using (14) and (15) to calculate the smoothed residuals
esmooth. Then, FD is fulﬁlled by the following formula:
Fi =

1, |esmooth,i| > T
0, |esmooth,i| ≤T
(19)
Fig. 11.
Two different series of roll doublets commands.
where Fi = 1 indicates that the ith sampling point is
faulty, and the corresponding estimated value ˆyi in ˆYtest
can be used instead of this sampling point to realize
quick recovery from failure. Thereby, the safe operation
of the UAV is ensured.
IV. EXPERIMENTAL RESULTS AND ANALYSIS
In this section, simulation data and real ﬂight data are used
to verify the performance of the proposed method in FD and
fault data recovery. A state-of-the-art regression method is
used for comparison.
A. Data Description
In this work, the roll rate is selected as the demonstration
parameter for FD, which is the data directly from the gyro-
scope sensor. Its state directly affects the attitude control of the
UAV [26]. To realize the roll rate regression, the parameters
in Table I are utilized as the inputs. In the simulation data,
we simulated two different series of roll doublets with random
magnitudes as the maneuver commands, which are shown in
Fig. 11. The solid line is treated as a training command.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:36:17 UTC from IEEE Xplore.  Restrictions apply.

## Page 7

WANG et al.: MULTIVARIATE REGRESSION-BASED FD AND RECOVERY OF UAV FLIGHT DATA
3533
Fig. 12.
Normalized ﬂight trajectory of the intercepted ﬂight fragment.
Fig. 13.
Real roll rate in the training set.
The dashed line is used as the test command, which is the
same as the command shown in Fig. 3. Two failure patterns
in (1) are injected into the roll rate in the test set generated
by the simulation model. Both bias and drift faults occur from
the 750th sampling point to the end of the simulation, which
is shown in Fig. 4. There are 2500 sampling points in total.
For real ﬂight data generated by the UAV in Fig. 2, since
there are no fault samples, the same fault injection method
as the simulation is applied to the real roll rate. It has been
veriﬁed in the simulation that minor faults will not have a big
impact on other parameters under the control of the autopilot.
In addition, the main ﬂight state of UAV during ﬂight and
mission is cruise, so we intercepted a piece of ﬂight data in
cruise for veriﬁcation, and its normalized trajectory is shown
in Fig. 12.
The length of the real ﬂight data is 8000, and it is divided
into two parts. The ﬁrst 80% is used as a training set, and
the remaining data are used as a test set. The roll rate in the
training set is shown in Fig. 13. In the test set, the normal roll
rate and faulty roll rate are shown in Fig. 14. The solid line is
the normal roll rate, the dashed line indicates the roll rate with
bias fault, and the dashed-dotted line refers to the roll rate with
drift fault. Both bias fault and drift fault are injected from the
750th sampling point and continue to the end of the data set.
The magnitude of the bias fault is 2◦/s and the drift rate is
0.01◦/s2. It differs from the simulation data due to different
ranges of roll rate.
B. Evaluation Metrics
Since the proposed method has both FD capability and fault
data recovery capability, we use the regression metrics and the
FD metrics to evaluate the proposed method. For regression,
the commonly used metrics are mean square error (MSE)
Fig. 14.
Real roll rate in the test set with two different fault patterns injected.
and mean absolute error (MAE) [34]. MSE can evaluate the
degree of change in data, and MAE can better reﬂect the actual
situation of the predicted error. The smaller these two metrics,
the better is the estimation performance of the model. These
two metrics are calculated by
MSE = 1
N
N
	
i=1
(yi −ˆyi)2
(20)
MAE = 1
N
N
	
i=1
|yi −ˆyi|
(21)
where N is the length of test set, and yi and ˆyi are the
ith sampling point and the corresponding estimated value,
respectively.
For FD, true positive rate (TPR), false positive rate (FPR),
and accuracy (ACC) are commonly used FD metrics. The
closer the TPR and ACC are to 1, the closer the FPR is
to 0; the effect of FD is better. In addition, the receiver
operating characteristic (ROC) curve and the area under the
ROC curve (AUC) are utilized to evaluate the FD performance,
which shows the tradeoff between TPR and FPR. An AUC
close to 1 means that the FD performance is optimal.
C. Experimental Results
To verify the effectiveness of the proposed LSTM-RF
method,
a
state-of-the-art
regression
method
based
on
LS-SVM [14] and LSTM [22] is used for comparison. Since
the input of the LS-SVM model can only be a scalar or vector,
it should be noted that only spatial correlation is considered
in the LS-SVM-based method. We also ﬁlter the estimation
residuals of the LS-SVM-based method to improve its FD
performance.
1) Regression and FD Results on Simulation Data: In the
simulation experiment, the multivariate regression results of
different methods under different fault scenarios are shown
in Figs. 15 and 16. In these two simulated fault scenarios,
compared with the normal data, the LSTM-RF obtains the
best estimation effect. In addition, since the LSTM method
does not penalize the input fault data, the estimated value will
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:36:17 UTC from IEEE Xplore.  Restrictions apply.

## Page 8

3534
IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 69, NO. 6, JUNE 2020
TABLE II
MULTIVARIATE REGRESSION ESTIMATION
RESULTS OF SIMULATION DATA
TABLE III
FD RESULTS OF SIMULATION DATA
bias toward the fault data after the fault occurs. Although
the LS-SVM-based approach seems to work well, there is
a large deviation at some sampling points, as indicated by
the circle. To quantitatively evaluate the regression effect of
each method, the regression metrics of the three methods
are shown in Table II. Obviously, the MSE and MAE of
LSTM-RF method are both the smallest, which means that
the regression effect is the best under different failure modes.
The LS-SVM-based method is the worst, which is because
the temporal correlation is not considered. Compared with the
LSTM, better fault recovery results can be obtained because
the proposed method incorporates a penalty factor for the fault
parameter. Comparing the MSE and MAE of each method
under two faults, the values are similar except for that of
LSTM. This is because the LSTM model is greatly affected
by this fault pattern, and the drift fault gradually increases,
so the results in this scenario are smaller than that of the bias
fault.
The FD results of simulation data are shown in Table III.
In the two fault scenarios, ACC results of the LSTM-RF
method are the largest, which indicates better FD performance.
The proposed method has the highest TPR and ACC, but
the FPR is larger than that of the LSTM method. This is
because the regression effect of our method has a slight
decrease at the dramatically changing point, which leads to
the smoothed residual values exceed the detection threshold.
As a result, the FPR is slightly increased. Although the
TPR of LS-SVM-based method is higher than that of LSTM,
the FPR is larger, so the ACC of LSTM is greater than that
of the LS-SVM-based method in bias fault. For the drift fault,
the ACC of the LSTM is lower than that of the LS-SVM-based
approach, which is a decrease in detection performance due
Fig. 15.
Estimation results of simulation data with bias fault injected.
Fig. 16.
Estimation results of simulation data with drift fault injected.
to large ﬂuctuations of residuals, and the fault cannot be
effectively detected at the beginning.
In order to tradeoff TPR and FPR, the ROC curves
of
the
three
methods
in
two
faults
are
plotted
in
Figs. 17 and 18. The corresponding AUC results are also
marked in Figs. 17 and 18. AUC = 1 represents the optimal
FD model.
In both fault cases, the AUC results of our method are the
largest, which are greater than 0.939. The difference between
the two fault scenarios is mainly due to the fact that the
drift fault is gradually occurring. In the beginning, the fault
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:36:17 UTC from IEEE Xplore.  Restrictions apply.

## Page 9

WANG et al.: MULTIVARIATE REGRESSION-BASED FD AND RECOVERY OF UAV FLIGHT DATA
3535
Fig. 17.
ROC curve and AUC of simulation data with bias fault injected.
Fig. 18.
ROC curve and AUC of simulation data with drift fault injected.
amplitude is too small to be effectively detected. Moreover,
we can see that the ROC curve of LSTM is closer to the
upper left corner than that of the LS-SVM-based method.
This is because the LS-SVM-based method has more sampling
points of large estimation error, resulting in unstable detection
performance.
2) Regression and FD Results on Real Flight Data: In this
experiment, the data are collected by a small UAV, and it can
be directly seen from Fig. 14 that the ﬂight process is more
complicated than the simulation model. Since the minor faults
are added on the roll rate directly, small ﬂuctuations of other
parameters in an instant cannot be simulated, which leads to
more similar estimation effects in the two failure modes, but
this does not signiﬁcantly affect the veriﬁcation effect due to
the closed-loop control. According to the above assumption,
there is no difference in terms of estimation under the two
failure scenarios. Thus, we only give an estimation result
of one failure pattern. The multivariate regression results are
shown in Fig. 19. The solid line represents the raw faultless
roll rate, and the dashed lines indicate the recovered roll
rate of the three methods. The lines are basically coincident,
indicating that all three methods can recover the fault data.
In order to quantify the recovery performance, we calculated
the MSE and MAE of each method, as shown in Table IV.
The MSE and MAE of the LS-SVM-based method are larger
than those of the LSTM-based method, which means that the
LSTM-based method can obtain a better estimation effect than
the LS-SVM based method in this real ﬂight state. This is
because there is a strong temporal correlation between the
Fig. 19.
Estimation results of real data with fault injected.
TABLE IV
MULTIVARIATE REGRESSION ESTIMATION RESULTS OF REAL DATA
TABLE V
FD RESULTS OF REAL DATA
parameters in this ﬂight state compared with the simulation
model. However, the regression results of the LSTM-based
methods are not much different; this is because the regression
has low dependence on the fault parameter itself in this ﬂight
mode.
The detection results of the real ﬂight data with faults
injected are shown in Table V. Our method also obtains a
large TPR and ACC values under the two fault patterns. For
drift fault, the TPR of the LS-SVM-based method is larger
than that of the LSTM, but its FPR is larger, which results in a
smaller ACC. In addition, since the magnitude of the bias fault
injected in the actual data is small, the estimation residuals
of the normal data are close to that of the fault data, so the
performance of the LSTM is not good, whereas the estimation
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:36:17 UTC from IEEE Xplore.  Restrictions apply.

## Page 10

3536
IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT, VOL. 69, NO. 6, JUNE 2020
Fig. 20.
ROC curve and AUC of real data with bias fault injected.
Fig. 21.
ROC curve and AUC of real data with drift fault injected.
residuals of the LSTM-RF method and LS-SVM-based method
are smoothed by our framework, so the detection performance
is greatly improved.
The ROC curves of the three methods in two fault modes
are plotted in Figs. 20 and 21. In both fault cases, the AUCs
of our method are also the largest, which are greater than
0.980. Because the drift fault is gradually occurring, the fault
amplitude is small in the front part. Thus, the AUC of bias fault
scenario is higher than that of the drift fault scenario. More-
over, we can see that the ROC curve of the LS-SVM-based
method is closer to the upper left corner than that of LSTM,
which is different from the simulation results. This is because
the estimation performance of the LS-SVM based method is
promoted and the unsmoothed residuals of these methods are
similar. Eventually, the detection performance of the LSTM
model is declined.
In summary, the LSTM-based regression model is a multi-
input model, which can extract the spatial correlation feature
between multi-dimensional ﬂight data while achieving long-
term memory. Therefore, the ACC of estimation is better
than the LS-SVM-based method when there are both temporal
correlation and spatial correlation in ﬂight data. With a high-
precision regression model, fault data can be recovered more
accurately and quickly in the event of a fault. Although the pre-
diction ACC of the regression model is higher, random noise
cannot be effectively predicted. However, the fault modes have
a steady trend. Therefore, by introducing a residual ﬁltering
method, the interference of noise in the ACC of FD can be
effectively reduced. This explains that the FD performance of
the proposed LSTM-RF method is better than that of the basic
LSTM.
The results of the simulation experiment and real-data
experiment show that the proposed FD method is effective
when dealing with minor bias and drift faults, and it can also
quickly realize the recovery of fault data. Thereby, ﬂight safety
of UAV can be guaranteed.
V. CONCLUSION
In order to realize the FD of the UAV, an FD and recovery
method based on the multivariate regression is proposed. The
designed LSTM multivariate regression model can effectively
extract the spatial–temporal features between multiple ﬂight
parameters. Therefore, the FD model’s ability to capture fault
information is enhanced. Meanwhile, the performance of the
FD method is greatly improved by smoothing the estimated
residuals, and a statistical threshold based on smoothed resid-
uals can be effectively determined for the detection of two
fault scenarios. Moreover, the proposed model can effectively
recover the fault data by regression. The experimental results
of simulated ﬂight data and actual ﬂight data prove the
effectiveness of the FD and recovery method. For FD, the ACC
and AUC of the bias FD are greater than 0.978 and 0.994,
respectively. The ACC and AUC of the drift FD are greater
than 0.868 and 0.939, respectively. For data recovery, the MSE
and MAE are less than 0.078 and 0.205, respectively.
In the future, the inﬂuences of different fault amplitudes
on the FD performance will be considered, and the FD
performance under different ﬂight modes will be veriﬁed.
Other categories of data-driven methods will be compared.
In addition, the method will be implemented on the embedded
platform, such as onboard PHM unit (Zynq SoC), to improve
the real-time performance of FD, and the on-line real-time
ﬂight test will be attempted.
REFERENCES
[1] H. Chao, Y. Cao, and Y. Chen, “Autopilots for small unmanned aerial
vehicles: A survey,” Int. J. Control. Autom. Syst., vol. 8, no. 1, pp. 36–44,
2010.
[2] Y. Zhao, J. Ma, X. Li, and J. Zhang, “Saliency detection and deep
learning-based wildﬁre identiﬁcation in UAV imagery,” Sensors, vol. 18,
no. 3, p. 712, Feb. 2018.
[3] S. V. Sibanyoni, D. T. Ramotsoela, B. J. Silva, and G. P. Hancke,
“A 2-D acoustic source localization system for drones in search and res-
cue missions,” IEEE Sensors J., vol. 19, no. 1, pp. 332–341, Jan. 2019.
[4] H. Lu, Y. Li, S. Mu, D. Wang, H. Kim, and S. Serikawa, “Motor anomaly
detection for unmanned aerial vehicles using reinforcement learning,”
IEEE Internet Things J., vol. 5, no. 4, pp. 2315–2322, Aug. 2018.
[5] W. Boonpook, Y. Tan, Y. Ye, P. Torteeka, K. Torsri, and S. X. Dong,
“A deep learning approach on building detection from unmanned aerial
vehicle-based images in riverbank monitoring,” Sensors, vol. 18, no. 11,
p. 3921, Nov. 2018.
[6] P. Freeman and G. J. Balas, “Analytical fault detection for a small UAV,”
in Proc. AIAA Infotech Aerosp. (I@ A) Conf., 2013, p. 5217.
[7] E. D’Amato, M. Mattei, I. Notaro, and V. Scordamaglia, “UAV sen-
sor FDI in duplex attitude estimation architectures using a set-based
approach,” IEEE Trans. Instrum. Meas., vol. 67, no. 10, pp. 2465–2475,
Oct. 2018.
[8] Y. Yi and Y. Zhang, “Fault diagnosis of an unmanned quadrotor
helicopter based on particle ﬁlter,” in Proc. Int. Conf. Unmanned Aircr.
Syst. (ICUAS), Jun. 2017, pp. 1432–1437.
[9] D. Guo, M. Zhong, and D. Zhou, “Multisensor data-fusion-based
approach to airspeed measurement fault detection for unmanned aerial
vehicles,” IEEE Trans. Instrum. Meas., vol. 67, no. 2, pp. 317–327,
Feb. 2018.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:36:17 UTC from IEEE Xplore.  Restrictions apply.

## Page 11

WANG et al.: MULTIVARIATE REGRESSION-BASED FD AND RECOVERY OF UAV FLIGHT DATA
3537
[10] I. Vitanov and N. Aouf, “Fault diagnosis for MEMS INS using unscented
Kalman ﬁlter enhanced by Gaussian process adaptation,” in Proc.
NASA/ESA Conf. Adapt. Hardw. Syst. (AHS), Jul. 2014, pp. 120–126.
[11] L. Y. Liu, Y. Ma, B. Xu, C. Xiang, and X. B. Yang, “Fault detection and
isolation based on UKFs for a novel ducted fan UAV,” in Proc. IEEE
Int. Conf. Aircr. Utility Syst. (AUS), Oct. 2016, pp. 212–218.
[12] A. Abbaspour, P. Aboutalebi, K. K. Yen, and A. Sargolzaei, “Neural
adaptive observer-based sensor and actuator fault detection in nonlin-
ear systems: Application in UAV,” ISA Trans., vol. 67, pp. 317–329,
Mar. 2017.
[13] E. Baskaya, M. Bronz, and D. Delahaye, “Fault detection & diagnosis
for small UAVs via machine learning,” in Proc. IEEE/AIAA 36th Digit.
Avionics Syst. Conf. (DASC), Sep. 2017, pp. 1–6.
[14] B. Wang, Y. Chen, D. Liu, and X. Peng, “An embedded intelligent
system for on-line anomaly detection of unmanned aerial vehicle,”
J. Intell. Fuzzy Syst., vol. 34, no. 6, pp. 3535–3545, Jan. 2018.
[15] P. Youseﬁ, H. Fekriazgomi, M. A. Demir, J. J. Prevost, and M. Jamshidi,
“Data-driven
fault
detection
of un-manned
aerial
vehicles
using
supervised learning over cloud networks,” in Proc. World Automat.
Congr. (WAC), Jun. 2018, pp. 1–6.
[16] E. Khalastchi, M. Kalech, G. A. Kaminka, and R. Lin, “Online data-
driven anomaly detection in autonomous robots,” Knowl. Inf. Syst.,
vol. 43, no. 3, pp. 657–688, Jun. 2015.
[17] Y. F. He, Y. Peng, S. J. Wang, D. T. Liu, and P. H. W. Leong,
“A structured sparse subspace learning algorithm for anomaly detection
in UAV ﬂight data,” IEEE Trans. Instrum. Meas., vol. 67, no. 1,
pp. 90–100, Jan. 2018.
[18] Y. He, Y. Peng, S. Wang, and D. Liu, “ADMOST: UAV ﬂight data
anomaly detection and mitigation via online subspace tracking,” IEEE
Trans. Instrum. Meas., vol. 68, no. 4, pp. 1035–1044, Apr. 2019.
[19] R. Zhao, R. Yan, Z. Chen, K. Mao, P. Wang, and R. X. Gao, “Deep
learning and its applications to machine health monitoring,” Mech. Syst.
Signal Process., vol. 115, pp. 213–237, Jan. 2019.
[20] D. Liu, L. Li, Y. Song, L. Wu, and Y. Peng, “Hybrid state of charge
estimation for lithium-ion battery under dynamic operating conditions,”
Int. J. Electr. Power Energy Syst., vol. 110, pp. 48–61, Sep. 2019.
[21] A. Nanduri and L. Sherry, “Anomaly detection in aircraft data using
recurrent neural networks (RNN),” in Proc. Integr. Commun. Navigation
Surveill. (ICNS), Apr. 2016, pp. 5C2-1–5C2-8.
[22] K.
Hundman,
V.
Constantinou,
C.
Laporte,
I.
Colwell,
and
T. Soderstrom, “Detecting spacecraft anomalies using lstms and nonpara-
metric dynamic thresholding,” in Proc. 24th ACM SIGKDD Int. Conf.
Knowl. Discovery Data Mining, Jul. 2018, pp. 387–395.
[23] M. Sharifzadeh, A. Sikinioti-Lock, and N. Shah, “Machine-learning
methods for integrated renewable power generation: A comparative
study of artiﬁcial neural networks, support vector regression, and
Gaussian process regression,” Renew. Sustain. Energy Rev., vol. 108,
pp. 513–538, Jul. 2019.
[24] D. Liu, Y. Song, L. Li, H. Liao, and Y. Peng, “On-line life cycle health
assessment for lithium-ion battery in electric vehicles,” J. Cleaner Prod.,
vol. 199, pp. 1050–1065, Oct. 2018.
[25] L. Liu, Q. Guo, D. Liu, and Y. Peng, “Data-driven remaining useful
life prediction considering sensor anomaly detection and data recovery,”
IEEE Access, vol. 7, pp. 58336–58345, 2019.
[26] P. Freeman, R. Pandita, N. Srivastava, and G. J. Balas, “Model-based and
data-driven fault detection performance for a small UAV,” IEEE/ASME
Trans. Mechatronics, vol. 18, no. 4, pp. 1300–1309, Aug. 2013.
[27] K. Guo, L. Liu, S. Shi, D. Liu, and X. Peng, “UAV sensor fault detection
using a classiﬁer without negative samples: A local density regulated
optimization algorithm,” Sensors, vol. 19, no. 4, p. 771, Feb. 2019.
[28] S. Hochreiter and J. Schmidhuber, “Long short-term memory,” Neural
Comput., vol. 9, no. 8, pp. 1735–1780, 1997.
[29] H. Zhu et al., “Correlation coefﬁcient based cluster data preprocessing
and LSTM prediction model for time series data in large aircraft test
ﬂights,” in Proc. Int. Conf. Smart Comput. Commun., 2018, pp. 376–385.
[30] B. Hou, J. Yang, P. Wang, and R. Yan, “LSTM based auto-encoder model
for ECG arrhythmias classiﬁcation,” IEEE Trans. Instrum. Meas., to be
published.
[31] P. Filonov, A. Lavrentyev, and A. Vorontsov, “Multivariate industrial
time series with cyber-attack simulation: Fault detection using an
LSTM-based predictive data model,” 2016, arXiv:1612.06676. [Online].
Available: https://arxiv.org/abs/1612.06676
[32] J. Pang, D. Liu, Y. Peng, and X. Peng, “Collective anomalies detection
for sensing series of spacecraft telemetry with the fusion of probability
prediction and Markov chain model,” Sensors, vol. 19, no. 3, p. 722,
Feb. 2019.
[33] Y. Cheng, R. Wang, and M. Xu, “A combined model-based and
intelligent method for small fault detection and isolation of actuators,”
IEEE Trans. Ind. Electron., vol. 63, no. 4, pp. 2403–2413, Apr. 2016.
[34] Q. Sun, B. Jiang, H. Zhu, and J. G. Ibrahim, “Hard thresholding
regression,” Scandin. J. Statist., vol. 46, no. 1, pp. 314–328, Mar. 2019.
Benkuan Wang (S’19) received the B.Sc. degree
from the Harbin Institute of Technology (HIT), Wei-
hai, China, in 2013, and the M.Sc. degree from HIT,
Harbin, China, in 2015, where he is currently pursu-
ing the Ph.D. degree with the School of Electronics
and Information Engineering.
His current research interests include condition
monitoring, system health management, embedded
high-performance computing, and unmanned aircraft
system simulation and veriﬁcation.
Datong Liu (M’11–SM’16) received the Ph.D.
degree in instrumentation science and technology
from the Harbin Institute of Technology (HIT),
Harbin, China, in 2010.
From 2001 to 2003, he was with the Depart-
ment of Computer Science and Technology, HIT.
From 2013 to 2014, he was a Visiting Scholar
with the University of Arizona, Tucson, AZ, USA.
He is currently a Full Professor with the School of
Electronics and Information Engineering, HIT. His
current research interests include automatic test and
simulation, condition monitoring, system diagnostics and prognostics, indus-
trial big data and industrial intelligence, and lithium-ion battery management.
Yu Peng (M’10) received the Ph.D. degree in
instrumentation science and technology from the
Harbin
Institute
of
Technology
(HIT),
Harbin,
China, in 2004.
He is currently a Full Professor with the School of
Electronics and Information Engineering, HIT. His
current research interests include automatic test tech-
nologies, virtual instruments, system health manage-
ment, and reconﬁgurable computing.
Xiyuan Peng received the B.S., M.S., and Ph.D.
degrees from the Harbin Institute of Technology
(HIT), Harbin, China, in 1984, 1987, and 1992,
respectively.
He is currently a Full Professor with the School of
Electronics and Information Engineering, HIT. His
current research interests include automatic test and
advanced fault diagnostics technology.
Authorized licensed use limited to: Netaji Subhas University of Technology New Delhi. Downloaded on April 07,2026 at 11:36:17 UTC from IEEE Xplore.  Restrictions apply.
