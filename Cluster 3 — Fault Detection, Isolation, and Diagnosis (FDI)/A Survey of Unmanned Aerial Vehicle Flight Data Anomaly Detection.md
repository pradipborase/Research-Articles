# A Survey of Unmanned Aerial Vehicle Flight Data Anomaly Detection.pdf

## Page 1

•Review•
April 2023 Vol.66 No.4: 901–919
https://doi.org/10.1007/s11431-022-2213-8
A survey of unmanned aerial vehicle flight data anomaly detection:
Technologies, applications, and future directions
YANG Lei1, LI ShaoBo1,2*, LI ChuanJiang1, ZHANG AnSi1,2 & ZHANG XuDong1
1 School of Mechanical Engineering, Guizhou University, Guiyang 550025, China;
2 State Key Laboratory of Public Big Data, Guizhou University, Guiyang 550025, China
Received May 17, 2022; accepted September 19, 2022; published online March 15, 2023
Flight data anomaly detection plays an imperative role in the safety and maintenance of unmanned aerial vehicles (UAVs). It has
attracted extensive attention from researchers. However, the problems related to the difficulty in obtaining abnormal data, low
model accuracy, and high calculation cost have led to severe challenges with respect to its practical applications. Hence, in this
study, firstly, several UAV flight data simulation softwares are presented based on a brief presentation of the basic concepts of
anomalies, the contents of UAV flight data, and the public datasets for flight data anomaly detection. Then, anomaly detection
technologies for UAV flight data are comprehensively reviewed, including knowledge-based, model-based, and data-driven
methods. Next, UAV flight data anomaly detection applications are briefly described and analyzed. Finally, the future trends and
directions of UAV flight data anomaly detection are summarized and prospected, which aims to provide references for the
following research.
unmanned aerial vehicle (UAV), flight data, anomaly detection, data-driven
Citation:
Yang L, Li S B, Li C J, et al. A survey of unmanned aerial vehicle flight data anomaly detection: Technologies, applications, and future directions. Sci
China Tech Sci, 2023, 66: 901–919, https://doi.org/10.1007/s11431-022-2213-8
1
Introduction
As an important area of future technology competition
among countries, unmanned aerial vehicle (UAV) technol-
ogy has applications in medical [1,2], agriculture [3,4], en-
vironmental monitoring [5,6], search and rescue operations
[7], and disaster management [8]. Hence, sales and produc-
tion value of UAVs have been increasing on an annual basis
[9]. Therefore, given the increasingly prominent role of
UAVs in various fields and their importance in economic
development, higher requirements are placed on their safety
and reliability, especially in complex operating environments
[10]. However, when compared with manned aircraft, the
safety and reliability of UAVs are compromised by the fol-
lowing shortcomings: (1) lack of pilots’ real-time observa-
tion, rapid decisions, and responses; (2) limited size, weight,
and power consumption; and (3) non-redundant or low-
redundant design [11,12]. These factors lead to higher in-
cidence of UAV accidents when compared with that of
manned aircraft. Based on American statistics, the accident
rate of UAVs is 100 times that of general aircraft [13], which
in turn causes serious economic losses to relevant en-
terprises.
In recent years, UAV accidents have been frequently re-
ported in China and abroad. The U.S. Air Force Accident
Investigation Board (AIB) accounted accidents involving 11
types of UAVs, including the RQ/MQ-1 Predator, RQ-4
Global Hawk, and MQ-9 Reaper. The survey showed that 21
accidents were due to human factors, 56 accidents were due
to system faults, and 4 accidents were due to environmental
and other factors [14]. Based on the civil UAVaccidents data
acquired by the U.S Federal Aviation Administration (FAA)
© Science China Press 2023
tech.scichina.com link.springer.com
SCIENCE CHINA
Technological Sciences
*Corresponding author (email: lishaobo@gzu.edu.cn)

## Page 2

via the UAS&I platform [15], 104 accidents, involving 44
types of UAVs, occurred. Among them, the number of ac-
cidents caused by faults in UAV system was as high as 90,
accounting for 86.54% of the total accidents. In June 2016,
institutions in China counted 47 domestic UAV accidents
caused by faults among which DJI UAVs caused 24 acci-
dents. According to Shenzhen DJI Innovation Technology
Co., Ltd., the manufacturer of DJI UAVs, more than 85% of
UAVaccidents are due to user misuse, and only a few of them
were due to component faults and other reasons involving.
Furthermore, the flight status information of UAVs is pri-
marily determined by flight data that include altitude, speed,
attitude angle, and other flight parameters. They compre-
hensively reflect the operating status of the UAV’s key
components and operators’ operation information [16]. With
the continuous accumulation of historical UAV flight data,
processing and analyzing their abnormal data information
have become the primary means for evaluating their flight
quality, analyzing the causes of accidents, enhancing work
efficiency, and improving their design [17]. Therefore, re-
searching effective UAV flight data anomaly detection
methods is an imperative way for improving the safety per-
formance of UAVs [18].
Many researchers reviewed flight data anomaly detection.
Peng et al. [9] reviewed the classification-based, clustering-
based, statistics-based, regression-based, and domain-based
flight data anomaly detection methods, and indicated re-
search directions that should be focused in the future. Peng
et al. [19] conducted a comprehensive review of the field of
anomaly detection in spacecraft telemetry data, including its
basic connotation, methods, and application status. Das et al.
[20] and Basora et al. [21] compared and analyzed different
flight data anomaly detection methods from an algorithmic
perspective. In an extant study, Igenewari et al. [22] reviewed
the strengths and weaknesses of current anomaly detection
methods and benefits of hybrid anomaly detection methods.
Khan et al. [23] described the current literature on solutions
to detect anomalies in known and unknown flight data.
Furthermore, they tested the practicability of the isolation
forest algorithm in engineering applications based on the
simulation data of aviation propulsion systems. However,
most of the aforementioned studies focused on flight data
anomaly detection for manned aircraft as opposed to UAVs.
Compared with manned aircraft, UAV flight data anomaly
detection is more challenging. The main reasons include: (1)
management and support for the production of the UAV in-
dustry is not perfect, and there is no flight operational quality
assurance (FOQA) [24] program similar to the civil aviation
field. There is also a lack of a standardized and unified
historical flight database. (2) Current anomaly detection
method is overly dependent on the analysis of ground control
stations. Given the limitation in the communication ability of
the network during the flight of UAV, the ground station
cannot obtain comprehensive flight statuses of UAV in real-
time. If anomalies in UAV flight data are not detected and
resolved in time, then there will be significant safety hazards,
which can result in serious accidents. Consequently, in this
study, we attempt to provide a comprehensive overview of
the technologies, applications, and future directions of UAV
flight data anomaly detection to offer some references for
future researchers.
The organization of the paper is as follows. In Section 2,
we describe the basic concept of anomalies, UAV flight data
content, flight data collector, and public UAV flight data
anomaly detection datasets-ALFA and University of Min-
nesota UAV real flight datasets. In Section 3, we discuss the
advantages and disadvantages of UAV flight data simulation
software. In Section 4, we analyze and summarize the re-
search progress of UAV flight data anomaly detection tech-
nologies, including knowledge-based, model-based, and
data-driven methods. In Section 5, we discuss some UAV
flight data anomaly detection platforms and frameworks,
along with the status of applications at research institutions at
home and abroad. In Section 6, we present a brief overview
of future research challenges, and in Section 7 we conclude
the paper.
2
UAV flight data anomaly
2.1
Basic concepts of anomalies
Hawkins [25] proposed that certain data types in a set are
abnormal, which are not due to random deviations but due to
completely different mechanisms. Keogh et al. [26] further
introduced the concept of time series anomaly based on the
chronological order of anomalies. They proposed that it did
not involve the size of the sliding window, and there is no
guarantee that the abnormal expansion between high-
dimensional and low-dimensional data features is consistent.
Although there is currently no clear definition of anomaly, it
can be considered as a pattern as opposed to normal. Fur-
thermore, data are the expression form and carrier of in-
formation and most of the behaviors expressed in the data are
regarded as normal. However, a few data behaviors that do
not conform to the norms considered as abnormal [27]. The
types of abnormal data behaviors can be categorized as point
anomalies [28], contextual anomalies [29], and collective
anomalies [30]. Their types, meanings, and examples are
listed in Table 1.
UAV flight data are typical time series data that are sam-
pled based on a time sequence. Therefore, according to the
definition of anomalies in time series, the anomalies of UAV
flight data can be classified into flight level anomalies and
instantaneous anomalies [9]. Flight level anomalies refer to
the abnormal sequence or subsequence of flight data that are
also termed as collective anomalies (as shown in Figure 1).
902
Yang L, et al.
Sci China Tech Sci
April (2023) Vol.66 No.4

## Page 3

Instantaneous anomalies refer to abnormal points in the in-
flight data that deviate from expected values. Given that the
adjacent points of the time series of in-flight data are de-
pendent on time or space, they can also be referred as con-
Table 1
Types, meanings, and examples of anomalies [31]. Copyright©2009, Association for Computing Machinery (ACM)
Type
Meaning
Example
Point anomalies
Data points are considered independent
in the time series, which significantly
differs from other data points.
Contextual anomalies
Several abnormal events in the entire
time series use point anomalies, which
make it extremely difficult to identify
the events associated with their deci-
sions data.
Collective anomalies
Some abnormal data points that are
significantly different from others
in a dataset.
Figure 1
(Color online) Example of fight level anomalies [32]. Copyright©2016, Elsevier.
903
Yang L, et al.
Sci China Tech Sci
April (2023) Vol.66 No.4

## Page 4

textual anomalies. Figure 2 shows an example of in-
stantaneous anomalies in-flight data.
As shown in Figure 1, most of the flight data of a specific
sortie differs from others under the same parameter settings.
This can be caused by the instability during landing [32].
Figure 2 shows four abnormal flight data parameters (navalt,
navvd, navve, and navvn at the top of Figure 2) and anomaly
score (at the bottom of Figure 2). Hence as the score in-
creases, the probability of becoming an outlier increases.
This is potentially due to the failure of GPS and navigation
filters [33]. The meanings of the relevant parameters men-
tioned above will be introduced in Section 2.3.
2.2
Overview of UAV flight data
Data is the information source of an analysis system. In the
era of big data, data is particularly important. To detect ab-
normal flight data of UAVs, data collection should be per-
formed first. UAV flight speed, acceleration, heading angle,
pitch angle, and other parameters during flights are recorded
using various sensors and measurement devices (as shown in
Figure 3) and are sent to the airborne recording system in a
specific data format for real-time storage. The UAV flight
data acquisition process is shown in Figure 4. The data
collectors involved are the core components of the flight data
acquisition system, such as the flight data recorder (FDR)
[34], quick access recorder (QAR) (termed as the black box
on the plane) [35,36], MMSC-800, AIFTDS-8000, and
DAMIEN-V1. Their advantages are listed in Table 2.
Given the aforementioned flight data collectors, FDR can
be used to acquire various flight parameters for UAVs.
However, inadequate recording parameters and insufficient
reliability of the protective device imply that its recorded
data cannot be preserved accurately. MMSC-800, AIFTDS-
8000, and DAMIEN-Vl exhibit excellent data acquisition
capabilities, but they are difficult to assemble. Conversely,
QAR has attracted considerable attention for its speed and
simplicity in accessing raw flight data [37–39]. It is often
used in flight simulation and reproduction, aircraft main-
tenance, safety quality assessment, and accident factor in-
vestigation by airlines and related departments. Furthermore,
QAR data can objectively and comprehensively display the
actual flight position of UAVs, including detailed flight data,
intuitive charts, and animations, which can enhance incident
investigation efficiency. During the entire flight phase, var-
Figure 2
(Color online) Example of flight data instantaneous anomalies
[33]. Copyright©2018, Institute of Electrical and Electronics Engineers Inc.
Figure 3
(Color online) UAV flight data are collected by sensors and measuring devices.
904
Yang L, et al.
Sci China Tech Sci
April (2023) Vol.66 No.4

## Page 5

ious parameters, such as position, motion, control, and alarm
information, are recorded by QAR. These parameters include
longitude, latitude, altitude, wind speed, wind direction, and
angle of attack (listed in Table 3).
2.3
UAV real flight datasets
The purpose of UAV flight data anomaly detection involves
detecting abnormal flight activities based on flight data.
However, abnormal UAV flight data are more difficult to
obtain than normal UAV flight data [40]. Hence, most of the
research findings on UAV flight data anomaly detection are
based on simulation data for verifying and evaluating the
proposed methods [33,41,42], which leads to challenges for
the practical applications of UAV flight data anomaly de-
tection technologies. To facilitate scholars in verifying the
practicability of their methods in a better manner, we will
introduce two public UAV flight datasets in this section:
ALFA and University of Minnesota UAV real flight datasets
[33,43,44].
ALFA datasets were collected and published by Keipour
et al. [43] and provide a benchmark for the research of UAV
fault detection and anomaly detection. They include many
hours of raw data from fully autonomous, autopilot-assisted,
and manual flights with tens of anomaly scenarios. To
evaluate the methods, the basic facts of the type and time of
the anomaly are presented for each scenario. The data types
and fault types of ALFA are listed in Tables 4 and 5, re-
spectively.
UAV real flight datasets were collected by the University
of Minnesota, including a wide range of flight modes, such
as rising, falling, turning, and flying. They are widely used
by researchers in anomaly detection research. The datasets
were collected from the Thor UAVs at different flight times
[45–50]. According to ref. [45], we listed the meanings of
some different flight variables of the Thor UAVs (Table 6),
which is convenient for scholars to quickly understand the
datasets. Table 7 shows the partial public datasets of the Thor
UAVs.
As an example of the partial public datasets of the Thor
UAVs, the Thor69 dataset contains 75 parameters and re-
presents the 69th flight data of the Thor UAV. Currently,
some researchers use its altitude data subsets, such as alt, h,
and navalt, to experiment and verify their proposed anomaly
detection methods [33].
3
UAV flight data simulation software
Research on UAV flight data anomaly detection is in-
extricably linked to data, which are essential factors of
Figure 4
(Color online) UAV flight data acquisition process.
Table 2
Advantages of each data collector
Data collector
Example
Advantages
FDR
(1) Record various states and operating parameters of UAVs;
(2) Can better protect parameters and system data;
(3) Provide flight conditions and data;
(4) Analyze system performance.
QAR
(1) Quick access to raw flight data;
(2) Record many flight parameters;
(3) Longer recording periods with a higher sampling rate.
MMSC-800, AIFTDS-8000,
DAMIEN-Vl
−
(1) With a central controller and several powerful external buses;
(2) Multiple collectors can be installed on one bus at the same time;
(3) Strong data acquisition capabilities and a high degree of flexibility in the equipment.
Table 3
Flight data parameters
Parameter category
Example
Position parameters
Altitude, longitude, latitude, etc.
Motion parameters
East speed, north speed, angular velocity, acceleration, etc.
Operation control parameters
PID parameters, steering gear command, pull rod speed, etc.
Alarm information
“Safe to fly”, “attitude mode!”, etc.
905
Yang L, et al.
Sci China Tech Sci
April (2023) Vol.66 No.4

## Page 6

production [51]. However, it is difficult to develop UAV
flight data anomaly detection research due to the high cost of
obtaining real flight data. In Section 2.2, we mentioned that
most of the current UAV flight data anomaly detection
methods are based on simulation data for testing and ver-
ifying the effectiveness of the proposed methods. Although
there are some differences between simulation data and real
data, it is still the main data source for scholars to conduct
academic research. Hence, software that generates simulated
flight data is an important tool for UAV flight data anomaly
detection, such as X-Plane [52], Flight Gear [53,54], Mi-
crosoft Flight Simulation (MFS) [55], MATLAB, and V-REP
[56], which significantly contributes to the advancement of
UAV flight data anomaly detection research. The flight data
generated by the software play an important role in evaluating
the rationality of flight dynamics model design. Additionally,
these simulation data can be used to evaluate the quality
of flight simulation training, flight evaluation, and flight
trajectory correction. The purpose of this section is to in-
troduce several UAV flight data simulation software, com-
monly used by scholars, to serve as a reference for
researchers to conduct future research on UAV flight data
anomaly detection.
Table 8 lists some commonly used softwares that can
generate simulated UAV flight data. Although X-Plane and
V-Rep can produce accurate and reliable simulation data,
they are time-consuming due to low operating efficiency,
which can adversely affect real-time anomaly detection and
analysis of UAV flight data. Flight Gear and Gazebo can
satisfy personal requirements of users although Flight Gear’s
storage capacity is limited and Gazebo lacks compatibility.
This affects the availability and quality requirements of its
Table 4
Information about ALFA datasets
Type
Content
Format
Processed
There are 47 autonomous flight data sequences, 7 types of faults, and 23 sudden engine failure scenarios.
.bag, .csv, .mat
Raw
Automated and manual flight data without processing.
.bag
Telemetry
Telemetry data are recorded via NVIDIA TX2 computer in airborne equipment.
.txt
Data flash
The data recorded on the Pixhawk autopilot during the tests.
.txt
Table 5
Fault types in the processed dataset [43]
Fault type
Test cases
Flight time before fault (s)
Flight time w/fault (s)
Engine full power loss
23
2282
362
Rudder stuck to left
1
60
9
Rudder stuck to right
2
107
32
Elevator stuck at zero
2
181
23
Left aileron stuck at zero
3
228
183
Right aileron stuck at zero
4
442
231
Both ailerons stuck at zero
1
66
36
Rudder & aileron at zero
1
116
27
No fault
10
558
–
Total
47
3935
777
Table 6
Description of some variables [45]
Field name
Units
Description
h
M
Barometric altitude above ground (AGL)
alt
m
GPS altitude (WGS84)
navvd
m/s
NAV down velocity
navve
m/s
NAV east velocity
q
rad/s
Y-axis angular rate (pitch)
r
rad/s
Z-axis angular rate (yaw)
hy
Gauss
Y-axis magnetic field
hz
Gauss
Z-axis magnetic field
ax
m/s
2
X-axis acceleration
ay
m/s2
Y-axis acceleration
navvn
m/s
NAV north velocity
navalt
m
NAV altitude (wGS84)
Table 7
Part of the public datasets of Thor UAVs
Name
Times
Parameters
Public year
Reference
Thor60
60th
93
2014
[45]
Thor69
69th
75
2012
[46]
Thor81
81st
95
2013
[47]
Thor83
83rd
85
2013
[48]
Thor97
97th
84
2013
[49]
Thor98
98th
84
2013
[50]
906
Yang L, et al.
Sci China Tech Sci
April (2023) Vol.66 No.4

## Page 7

simulated UAV flight data. Although MFS is friendly to
domestic users in terms of language settings and operations,
it is an expensive commercial software with many plug-ins
and low efficiency. Comparatively, MATLAB is increasingly
preferred as simulation tool for researchers due to its rich
functionality, easy user interface, strong extensibility, and
good interactivity. However, its computational efficiency and
encapsulation necessitate further improvements. Further-
more, softwares, such as Flight Gear, V-REP, and Gazebo,
are open-source software, which enables scholars to use
them more flexibly for secondary development to satisfy
some of their own personalized needs. Furthermore, it is
necessary to focus on the security and system reliability of
these softwares, which can lead to unnecessary issues.
4
UAV flight data anomaly detection technolo-
gies
The purpose of anomaly detection is to identify patterns in
data that do not conform to normal behavioral patterns. It is
vital to train models using labeled data or by verifying their
availability [57]. In recent years, anomaly detection tech-
nology exhibits significant advantages in many fields in-
cluding urban road traffic [58,59], Internet of things [60,61],
finance [62,63], and other critical fields.
Anomalies can occur when UAVs display abnormal flight
behaviors, sensors, and other abnormal information. These
anomalies are then analyzed to predict UAV faults. Given
that UAVs are less safe and have a higher failure rate
[11,12,64], they result in enormous economic losses to en-
terprises and departments in practical applications. Thus,
research on UAV flight data anomaly detection constitutes a
crucial basis for UAV operators to adopt appropriate emer-
gency measures and determine whether UAVs will continue
to work [11,33]. However, the challenge translates into de-
signing and developing effective UAV flight data anomaly
detection methods. The digital information of UAVs is
continuously intensifying, and thus anomaly detection
technology is gradually applied to UAV flight data. In extant
studies, advanced anomaly detection methods were proposed
that can be broadly categorized into three categories:
knowledge-based, model-based, and data-driven [11]. In this
section, we provide a more comprehensive analysis and
summary of the three categories.
4.1
Knowledge-based methods
Knowledge is a systematic and concise understanding ob-
tained by human beings in various ways. Hence, it is the sum
of the results of human beings exploring the material world,
studying the spiritual world, and understanding the objective
world (including humans themselves) in practice such as the
description of facts and information or skills acquired in
Table 8
Information about each simulation software
Name
Advantages
Disadvantages
Open-source
X-plane
(1) Provides aircraft flight parameters output port;
(2) Can freely select the required flight parameter data;
(3) Provides accurate and reliable simulation data;
(4) Easy to operate and has excellent visualization effects.
(1) Slow reaction;
(2) Large memory requirements.
No
Flight gear
(1) Realize cross-platform, network communication, and other
functions;
(2) Convenient for users in secondary development;
(3) Satisfies individualized requirements of users.
(1) Complex structure and organization;
(2) Difficult to comprehend;
(3) Data cannot be automatically stored;
(4) Limited amounts of data are recorded.
Yes
MFS
(1) Standardized operations;
(2) Easy to operate;
(3) Provides Chinese language operation.
(1) Lower operational efficiency;
(2) High memory demands;
(3) Excess resources due to redundant plug-ins.
No
MATLAB
(1) Can easily use the Simulink library to model, analyze, and
simulate various dynamic systems;
(2) Provides a graphical interactive environment;
(3) Provides powerful functions and an intuitive interface;
(4) Strong expansibility and great interaction.
(1) Inefficiency of low-cycle operation;
(2) Poor encapsulation.
No
V-REP
(1) Can simulate the entire UAV system or its subsystems;
(2) Offers many data interfaces;
(3) Variety of programming languages are available;
(4) Does not exclusively rely on a mathematical model and
aerodynamic parameters;
(5) Rapid modeling and verification of aircraft.
(1) High memory demands;
(2) Processing and transferring of data are time-
consuming;
(3) Added script can conflict with the built-in script.
Yes
Gazebo
(1) Realistic 3D environment and high-performance physics engine;
(2) Can be used to obtain simulation data and noise with respect to
sensors;
(3) Satisfies personalized needs of users;
(4) Easy to use system operation interface.
(1) Poor compatibility;
(2) May not apply to virtual machines or computers
with lower configuration.
Yes
907
Yang L, et al.
Sci China Tech Sci
April (2023) Vol.66 No.4

## Page 8

education and practice. Knowledge-based methods can fully
utilize prior knowledge and expert experience and are widely
used in recommendation systems [65], biomedicine [66],
smart city [67], and other fields. For UAV flight data
anomaly detection, methods can be used to detect flight data
anomalies by summarizing expert experience and knowledge
in the specific field of UAVs. Subsequently, it is necessary to
design
and
develop
corresponding
anomaly
detection
algorithms to detect different types of anomalies in UAV
flight data without accurately modeling UAVs. As shown in
Figure 5, the flight data (including telemetry data, altitude,
and data flash) are first combined with the UAV’s specific
knowledge or expert experience to establish flight data
anomaly types for UAVs such as point anomalies, context
anomalies, and collective anomalies. Based on different ab-
normal UAV flight modes, it is then possible to design
anomaly detection algorithms to realize anomaly detection.
The algorithms include adaptive threshold neural-network,
PF, and FIS [68,69].
There is a paucity of studies on knowledge-based methods
in the field of UAV flight data anomaly detection due to their
defects such as high dependence on prior knowledge, expert
experience, models, and rules. Although the methods do not
require accurate UAV models, it is challenging to transfer
them from one application to another. Additionally, it is
challenging to expand their use to various types of anoma-
lies. As listed in Table 9, the method proposed in a previous
study [69] offers high anomaly detection accuracy and early
anomaly prediction. However, the large calculation of the PF
and poor performance of the FIS limit its ability to detect
anomalies in terms of false-positive rate and processing, and
thus it is unable to detect the impact of unknown anomalies.
Although sparse modeling and T-Digest can capture in-
stantaneous anomalies and address complex correlation be-
tween sensors, T-Digest only focuses on instantaneous
events and does not filter over time [70]. This can lead to
more false positives and affect the performance of anomaly
detection. Furthermore, adaptive threshold neural-network
and clustering algorithms are significantly dependent on the
knowledge of experts in specific fields [68,71], which also
poses challenges to their practical application. Although
these methods exhibit certain limitations, they can also sa-
tisfy the accuracy of UAV anomaly detection to a certain
extent and decrease the time cost of anomaly identification
[70,71], which provides a reference for research in UAV
flight data anomaly detection. Additionally, when the
threshold is fixed, the performance of the UAV anomaly
detection algorithm can be guaranteed [68].
Figure 5
(Color online) The general flow of knowledge-based anomaly detection methods for UAV flight data.
Table 9
Knowledge-based anomaly detection methods for UAV flight data
Authors
Data
Methods
Benchmarks
Software
Advantages
Qi et al. [68]
Acceleration, position, an-
gular velocity, etc.
Adaptive threshold
neural-network
Neural-network
−
Can eliminate the requirement for changes in the
threshold based on changes in flight conditions
and can significantly enhance the performance of
fixed threshold algorithms.
Bu et al. [69]
Flight data information re-
lated to navigation sensors
PF + FIS
−
MATLAB
High level of anomaly detection accuracy and
ability to predict anomalies at an early stage.
Radke et al. [70]
Angular displacement,
acceleration, angular
velocity, etc.
Sparse modeling +
T-Digest
K-means
−
Can capture transient anomalies, handle complex
correlations between sensors, and provide clear
alarm trigger points that indicate faults.
Schmidt et al.
[71]
Log of CPS
Clustering algorithm
−
−
Significantly decrease time and effort required by
experts to identify anomalous events in logs.
908
Yang L, et al.
Sci China Tech Sci
April (2023) Vol.66 No.4

## Page 9

4.2
Model-based methods
Essentially, models constitute artificial simulations or ab-
stractions based on certain features and relationships that
exist in the objective world. Specifically, models correspond
to the forms and structures of objects and explain their re-
lation to each other through words, charts, formulae, com-
puter programs, or other mechanisms. They can be used to
objectively test models and analyze practical problems.
Therefore, these methods are used in UAV flight data
anomaly detection research to overcome the challenges and
cost of abnormal UAV flight data acquisition, and realize
high anomaly detection performance. Furthermore, these
methods can provide detailed and interpretable anomaly in-
formation when an accurate physical model of the UAV
system is obtained. As shown in Figure 6, the general flow of
the methods involves establishing the corresponding physi-
cal models for UAVs or their subsystems by combining ex-
pert domain knowledge. Secondly, it is necessary to
construct the observer system models. The residuals are then
calculated by comparing the estimated value with the actual
value to detect anomalies in UAV flight data. Furthermore,
research on model-based UAV flight data anomaly detection
methods has been developed in recent years (Table 10).
Model-based methods exhibit advantages of simplicity,
economy, and speed of operation. To obtain better anomaly
detection performance, the methods should combine UAV’s
domain knowledge or system mechanisms to establish ac-
curate UAV physical models. The reality is that it is difficult
to model accurate physical models of UAV’s every sub-
system. Moreover, few abnormal samples of real UAV flight
data exist in most cases, and thus their applicability and
superiority is accurately observed only when the abnormal
modes of UAVs are known. Hence, the methods exhibit
certain limitations. Based on Table 10, although EKF dis-
plays evident advantages in terms of computing cost, there
are no fault-tolerant strategies [72]. The methods in previous
studies [73,76,77] can be applied to nonlinear models al-
Figure 6
(Color online) The general flow of model-based anomaly detection methods for UAV flight data.
Table 10
Model-based anomaly detection methods for UAV flight data
Authors
Data
Methods
Benchmarks
Software
Advantages
Abbaspour et al.
[72]
Parameters related to rudder,
elevator, aileron deflection, etc.
EKF
RNN
MATLAB
Can satisfy real-time application needs
and provide high security and reliability
and quick computing time.
López-Estrada et al.
[73]
Position, velocity,
angular velocity, etc.
LPV
−
MATLAB
Can accurately represent nonlinear
model and independently design the
observer.
Suarez et al. [74]
Information about position,
visual sensors, etc.
Vision-based FDIR
system
−
−
Can guide UAVs with faulty sensors to
safe states.
Wang et al. [75]
Acceleration, angular
velocity, etc.
A novel sparse opti-
mization technique
Traditional model-based
anomaly detection
MATLAB
Can accurately detect anomalies.
Wang et al. [76]
Acceleration, velocity,
dynamic pressure, etc.
LSM + Bias com-
pensated terms
Anomaly detector based
on residual
−
Can transform the problem of anomaly
detection of multiple UAV formations
into a nonlinear system identification
problem.
Zhang [77]
Airspeed, angle of attack,
pitch angle, pitch rate, etc.
DUKF
−
MATLAB
Can separate state estimation and para-
meter estimation and can be directly
applied to nonlinear models.
Guo et al. [78]
University of Minnesota
UAVs real flight datasets
EKF + Ensemble al-
gorithm
−
−
Exhibits good anomaly detection per-
formance and displays a certain prac-
tical value.
909
Yang L, et al.
Sci China Tech Sci
April (2023) Vol.66 No.4

## Page 10

though the accuracy of parameter estimation directly affects
the performance of the designed anomaly detector [76].
However, separating state estimation and parameter estima-
tion [77] or independently designing the observer [73] leads
to more obvious advantages in UAV flight data anomaly
detection. Additionally, the methods in previous studies
[74,75] also rely on expert knowledge. Conversely, the
method proposed by Guo et al. [78] exhibits more ad-
vantages in terms of performance and practicability although
its computation cost should be further reduced.
4.3
Data-driven methods
Data-driven corresponds to data-centric methods for estab-
lishing the correlation relationship between their internal
characteristics to make decisions and actions as follows:
(1) collect considerable data using various softwares;
(2) organize data to form information, which is then in-
tegrated and refined; (3) an automatic decision model is
formed after training and fitting data. The potential value of
data was further improved with the rapid development of big
data technology [79], cloud computing technology [80,81],
and artificial intelligence algorithms [82,83]. The ex-
ponential growth of data has also spawned many new domain
terms such as agricultural big data, industrial big data, and
medical big data [84–86]. Hence, the technologies led to
many data-driven methods [87,88], which significantly
promoted the development of various fields. Therefore,
when compared with knowledge-based and model-based
methods, data-driven methods constitute a research hotspot
in the field of UAV flight data anomaly detection.
As shown in Figure 7, UAV flight data, including altitude,
telemetry data, and data flash, are acquired by sensors and
are considered as the source of analysis of UAV system be-
haviors. Subsequently, abnormal UAV flight data are iden-
tified
and
marked
via
data-driven
algorithms.
When
compared with model-based methods, data-driven methods
do not require complex modeling of the physical character-
istics of UAV systems and can maximize the use of the in-
formation contained in sensor data. Additionally, accurate
anomaly information can be detected via various data-driven
methods based on the modified characteristics of the flight
data information to ensure the safety and stability of UAVs.
Data-driven methods are widely applied to the anomaly de-
tection of key parts and systems of UAVs. Table 11 lists
recent studies on data-driven methods for UAV flight data
anomaly detection.
Internal dynamics of UAVs is not necessary to understand
in detail for data-driven anomaly detection methods. The
available flight data can be considered as a source of in-
formation with respect to the UAV systems’ behaviors. Al-
though the methods are based on statistical information to
detect abnormal data, they display high flexibility without
model analysis. In Table 11, PCA [89], ANFIS [74], and
mGMM [96] exhibit evident advantages and effects in terms
of detection accuracy, algorithm robustness, and real-time
anomaly detection. Furthermore, the methods proposed in
extant studies, refs. [90] and [93], can also decrease the cost
of data labeling [90] and false alarm rate of anomaly de-
tection [93]. However, defects still persist. For example, in a
previous study [90], the method performance is dependent on
sampling strategy where the assumption of improving S3VM
is unrealistic. Additionally, the model involves a long
training cycle. Although the method in previous work [91]
performs well in terms of anomaly detection time and ro-
bustness of the algorithm, the performance of their method
requires
further
improvement
such
as
improving
the
accuracy and decreasing the false alarm rate. Wang et al. [94]
used the Pearson correlation coefficient (PCC) to extract
correlation parameters as experimental data. However, PCC
only measures linear correlation present in the flight data.
Given the complex linear and nonlinear correlations in the
UAV flight data, nonlinear correlation parameters should be
further considered in future studies. The method proposed in
a previous work [97] can cope with small deviations from the
expected sampling time and exhibits good robustness and
Figure 7
(Color online) The general flow of data-driven methods for UAV flight data anomaly detection.
910
Yang L, et al.
Sci China Tech Sci
April (2023) Vol.66 No.4

## Page 11

high accuracy. However, the over-fitting problem due to the
limited training data samples of this method limits the
model’s generalization ability. Bae et al. [98] and Bell et al.
[99] used the LSTM-AE approach for UAV flight data
anomaly detection. Although their methods effectively de-
crease anomaly detection time, severe dimensionality re-
duction leads to the risk of high reconstruction loss using a
single AE [98]. In contrast, stacked AEs enable the model to
reduce dimensionality gradually. This in turn smooths the
slope and retains more relevant information in the low-di-
mensional space [99]. Conversely, GAN exhibits a larger
window to observe pattern anomalies and can detect abnor-
mal patterns that cannot be detected by AE [100].
5
Applications
In recent years, the development of UAV anomaly detection
technology has prompted domestic and international in-
stitutions to develop many platforms and frameworks that
can be used for UAV anomaly detection. Simultaneously,
domestic and foreign research institutions have also per-
formed considerable applied research in UAV anomaly de-
tection, which has further promoted the application process
of theoretical research. To this end, in this section, we pro-
vide a more comprehensive analysis and summary of the
platforms and frameworks and related studies performed by
the institutions in this field.
5.1
Platforms and frameworks
Anomaly detection technologies and applications gradually
matured following many years of development [101–103].
Several platforms and frameworks emerged for detecting
UAV flight data anomalies including, rt-R2U2 [104], Ardu-
pilot [105], embedded intelligent system (EIS) of UAVs
[106], and an online and noninvasive embedded anomaly
detection system (ONEADS) [107]. This significantly pro-
Table 11
Data-driven anomaly detection methods for UAV flight data
Authors
Data
Methods
Benchmarks
Software
Advantages
Alos et al. [89]
Longitude, latitude, alti-
tude, etc.
PCA
MKAD
−
Fewer training datasets and higher
detection accuracy.
Wang et al. [11]
North speed, pneumatic
lifting speed, etc.
LSTM
−
−
Strong approximation ability to complex
functions and evident advantages to
address time series anomalies and
automatic feature extraction.
Pan et al. [90]
Telemetry data
MS + S3VM
SVM + S3VM
−
Decreases labeling costs and improves
the performance of the anomaly classi-
fication model.
Sun et al. [91]
Climb, horizontal flight,
descent parameters, etc.
ANFIS
PF + FIS
MATLAB
Can quickly and accurately realize
anomaly detection of UAV flight data
with strong robustness of its algorithm.
Titouna et al.
[92]
ALFA
KLD + ANN
−
MATLAB
Exhibits high accuracy for anomaly
detection and use of spatial and tem-
poral correlations in the sensors’ data to
realize online detection.
Pan [93]
Simulated flight data +
University of Minnesota
UAVs real flight datasets
PAA + SVDD +
KPCA
SVDD + KPCA
Flight Gear
Excellent anomaly detection perfor-
mance, lower false positive rate, and
valuable practicability.
Wang et al. [94]
Latitude, longitude, alti-
tude, etc.
MRM
−
−
Excellent adaptability and anomaly
detection performance.
Duan et al. [95]
Remote sensing data
RVM
−
Flight Gear
Simple and easy to operate.
Li et al. [96]
Acceleration, rudder posi-
tion degrees, ailerons, etc.
mGMM
−
MATLAB + X-Plane
High detection sensitivity, calculation
efficiency, and lower calculation cost
and can realize real-time monitoring.
Bronz et al. [97]
Flight test log
SVM
−
−
Strong robustness and higher accuracy,
and a solution on a small deviation from
the expected sampling time.
Bae et al. [98]
Status information, position
information, speed infor-
mation, etc.
LSTM-AE + AE
−
−
Does not require a high number of
calculations, can effectively reduce the
anomaly detection time, and satisfy the
demand for anomaly detection in the
UAV environment.
Bell et al. [99]
ALFA
Stacked LSTM-AE
statistic
thresholding and without
the dynamic thresholding
−
Decreases latency of true anomalous
behavior detection and can be easily
applied to aircraft data from vehicles
with different characteristics.
Aksoy et al.
[100]
Trajectory data
GAN
−
−
Contextual anomalies in the sequential
data are successfully detected.
911
Yang L, et al.
Sci China Tech Sci
April (2023) Vol.66 No.4

## Page 12

moted the application of UAV flight data anomaly detection.
Table 12 provides a summary of the advantages and dis-
advantages of each platform and framework.
With respect to current platforms and frameworks, rt-
R2U2 can perform real-time monitoring although its fra-
mework includes high hardware requirements and relies on
prior knowledge, thereby increasing the cost of anomaly
detection to some extent and reducing the performance of
anomaly detection. Similarly, while Ardupilot supports a
variety of UAV models, its code is redundant and cannot
detect or diagnose more complex abnormal modes. There-
fore, its performance is limited in practical applications.
Comparatively, EIS and ONEADS include numerous algo-
rithms for anomaly detection and display the capability of
parallel data processing, which significantly improves
computational efficiency. Furthermore, they can satisfy real-
time anomaly detection requirements. Nevertheless, their
computing cost, hardware requirements, and system com-
plexity should be further reduced and optimized.
5.2
Application status
UAVs are ideal for military and civilian fields due to their
significant environmental adaptability, high degree of au-
tonomy, zero casualties, and long-term operability [108–
110]. Almost every country in the world has evidenced a
keen interest in UAVs. As the base of scientific research,
universities play a vital role in the process of scientific re-
search. Currently, when compared with other research in-
stitutions, universities lead research in abnormal detection of
UAV flight data. In addition to universities, research in-
stitutes and enterprises related to UAVs also significantly
contribute to the field of UAV flight data anomaly detection.
Therefore, to comprehensively analyze the current applica-
tion status of UAV flight data anomaly detection, we first
discuss representative domestic and foreign universities and
some of their research results in UAV flight data anomaly
detection and briefly analyze their application research re-
sults. Second, we summarize related work of some domestic
and international UAV flight data anomaly detection re-
search institutions except universities.
Table 13 provides a list of references of universities in
China and abroad involved in the application of UAV flight
data anomaly detection technology. Domestic research in-
cludes studies by He et al. [33,41,111,112] of the Harbin
Institute of Technology. They designed and developed UAV
anomaly detection technology based on OSPABP, subspace
learning, and subspace matrix. The effectiveness of the
methods is verified based on simulated and real UAV flight
data, and computational and storage complexity of the al-
gorithms can satisfy airborne processing requirements. Pei
[113] from the University of Electronic Science and Tech-
nology designed a set of comprehensive analysis software
that can detect UAV flight data anomalies. The key concept
involves using expert systems to detect abnormal flight data,
which can provide a scientific and effective basis for UAV
fault detection and maintenance. Liu et al. [16] from the
Beihang University proposed a method to detect UAV flight
data anomalies in real-time. They used KNN to provide rea-
sonable prediction values for different flight data anomaly
types, which can be easily applied to airborne systems and
provide real-time data preprocessing for other aviation sys-
tems and ground control systems. Furthermore, international
researchers, including Keipour et al. [43] from Carnegie
Mellon University and Taylor [45–50] from University of
Minnesota in America, Alos et al. [89] from University of
Damascus (Syria), Bae et al. [98] from Hanyang University
(Korea), White et al. [114] from University of Glasgow
(United Kingdom), and Titouna et al. [92] from University of
Paris (France), have also significantly contributed to appli-
cations of UAV flight data anomaly detection. They dis-
closed UAV flight data anomaly detection datasets [45–50]
and provided real-time online UAV flight data anomaly de-
tection methods [45–50,92,114].
Table 12
Advantages and disadvantages of each platform and framework
Name
Advantages
Disadvantages
rt-R2U2
(1) Detect faults and violations of safety or performance rules;
(2) Analyze and preprocess signals from sensors and software;
(3) Can detect fault anomalies in real-time.
Restricted by hardware, dependent on prior knowledge, and
can only be executed via a plug-and-play architecture.
ArduPilot
(1) Support multiple ground stations for flight planning and flight control;
(2) Simple and friendly user interface;
(3) Simulate flight of fixed-wing aircraft, multirotor aircraft, and other types
of aircrafts.
Sensor data analysis tool is limited to specific sensor data
and cannot diagnose or detect complex faults.
EIS
(1) Capable of receiving real-time flight data;
(2) Realize online anomaly detection for key sensors and components;
(3) Support acceleration of multiple algorithms.
High hardware requirements and high complexity of the
system.
ONEADS
(1) Include a high-speed, parallel, dynamic, and non-deterministic
computation;
(2) Include algorithms for detecting anomalies;
(3) Satisfy requirements for UAV flight data anomaly detection in real-time.
With a significant amount of computation, a more complex
algorithm model, and significantly higher requirements for
hardware and software.
912
Yang L, et al.
Sci China Tech Sci
April (2023) Vol.66 No.4

## Page 13

However, in general, there is a paucity of research on UAV
flight data anomaly detection in universities in China and
abroad. Most research findings remain in the theoretical
phase. Although the aforementioned authors claim that their
methods can realize positive results, there is a lack of prac-
tical engineering application verification. Given that many
uncertain factors exist in the practical application process,
the effectiveness of these methods should be further verified.
The authors recently conducted studies on UAV flight data
anomaly detection and purchased UAV ground control sta-
tions and different types of UAVs. The UAV is equipped with
multiple data collectors to collect different types of flight
data and transmit flight data to the UAV ground control
station in time. Additionally, the UAV ground control station
also exhibits data interfaces for exporting flight data. The
simulated flight data can also be obtained via the UAV model
built-in in the UAV ground control station, and the faults can
be injected manually, which provides anomaly data sources
for better research on anomaly detection of UAV flight data.
With the exception of the aforementioned universities,
NASA developed a UAV health management framework rt-
R2U2 based on swift UAV [104]. We introduced its ad-
vantages and disadvantages in Section 5.1 and will not detail
the same here. The specific process of rt-R2U2 includes the
following stages: (1) non-intrusion access to the UAV
hardware architecture; (2) obtain flight data from the existing
UAV airborne data bus; (3) monitor abnormal state of key
components, flight control software, and flight behavior via
built-in online anomaly detection algorithms; (4) the detec-
tion results are fed back to the flight control processor via the
airborne data bus, which is convenient for flight control
emergency handling. Industrial departments, including Chi-
na Aerospace Science and Industry Group, Beijing Institute
of Spacecraft Environment Engineering, Beijing Aerospace
Unmanned Vehicles System Engineering Research Institute,
and Centre for Transport Studies of Imperial College Lon-
don, examined the application of UAV flight data anomaly
detection technology [11,41,91,94,115]. Additionally, many
enterprises recently actively performed research on UAV
flight data anomaly detection. Based on the characteristics of
UAV sensor data, Duan et al. [116] from the Xi’an ASN
Technology Group Co., Ltd., China, proposed an anomaly
detection method based on KPCA to overcome high di-
mensionality and nonlinearity of UAV flight data. The flight
data generated by Flight Gear verified that the method rea-
lizes satisfactory anomaly detection performance.
6
Future directions
It is established that UAV flight data anomaly detection has
significantly advanced in terms of technologies and appli-
cations over the last few years. However, given that research
in this field commenced recently, many important issues
Table 13
Part of UAV flight data anomaly detection applications research literature of universities
Authors
Methods
Effects
University
Nation
He et al. [41]
OSPABP
Improve detection accuracy and decrease false alarms rate. Harbin Institute of Technology
China
Chen [27]
LS-SVM + K-means
With real-time anomaly detection, high performance, and
low power consumption.
Harbin Institute of Technology
China
He [111]
Subspace learning
High detection accuracy, low false detection rate, and high
calculation efficiency.
Harbin Institute of Technology
China
He et al. [33]
Subspace matrix
Low data recovery error rate and high accuracy of anomaly
detection.
Harbin Institute of Technology
China
Pei [113]
Rule-based forward
reasoning method
Can assist UAVs in detecting faults and improving their
efficiency.
University of Electronic Science
and Technology
China
Wang et al. [11]
LSTM
Strong data recovery capability and excellent anomaly
detection performance.
Harbin Institute of Technology
China
He et al. [112]
SSSLAD
High accuracy and rapid identification of anomalous sources
of flight data.
Harbin Institute of Technology
China
Liu et al. [16]
KNNS
More efficient and accurate than traditional methods of real-
time anomaly detection.
Beihang University
China
Keipour et al. [43]
−
Dataset of publicly available real flight data for fault
detection, isolation, and anomaly detection.
Carnegie Mellon University
America
Taylor [45–50]
−
Datasets for Thor UAVs during different flight regimes for
anomaly detection were made public.
University of Minnesota
America
Alos et al. [89]
PCA
Without flight anomaly false alarms and training mass data.
University of Damascus
Syria
Bae et al. [98]
LSTM-AE + AE
Can effectively reduce anomaly detection time.
Hanyang University
Korea
White et al. [114]
SDN + NFV
Can be modified to cater to specific UAV types and provide
operators with real-time and mobile deployment capabilities.
University of Glasgow
United Kingdom
Titouna et al. [92]
KLD + ANN
High accuracy is realized in anomaly detection, and the
spatial and temporal correlation of sensor data can be used to
realize online anomaly detection.
University of Paris
France
913
Yang L, et al.
Sci China Tech Sci
April (2023) Vol.66 No.4

## Page 14

persist and require resolution. In this section, we analyze and
summarize the future research directions and challenges of
UAV flight data anomaly detection based on the content
described in Sections 3–5 (Figure 8).
6.1
Developing simple and understandable simulation
software
It should be noted that although many UAV flight data si-
mulation generation softwares currently exist, most of them
involve complex operations and are not available in lan-
guages that are friendly to domestic users (such as Flight
Gear and Gazebo). Given the difficulty in obtaining real
UAV flight data, UAV flight data simulation software re-
mains an essential tool for researchers in the present and
future. Hence, development of software with an emphasis on
simple operation and Chinese language is an effective way to
accelerate domestic research in UAV flight data anomaly
detection. It also serves as a reference direction for future
research.
6.2
Improving the interpretability of models
Interpretability is the ability to help people understand or
explain [117,118]. Although model-based UAV flight data
anomaly detection methods can realize high detection per-
formance, their interpretability relies on accurate physical
models of UAV systems. Hence, it is difficult for researchers
to combine data, models, and problem understanding, and
thus, it is impossible to locate or track anomalies in UAV
flight data. Thus, interpretable models can be developed, or
interpretable methods can be used to analyze the models after
modeling. Additionally, we can also utilize LIME [119],
model substitution [120], and other technologies to enhance
the interpretability and traceability of abnormal information
from the perspective of local and global models, which
constitutes the main research direction for future research.
6.3
Exploring new data-driven algorithms
Data-driven methods are based on the data information ex-
tracted from the historical flight data without modeling the
accurate physical models of UAVs [11,89,90]. Although we
described many advantages of data-driven UAV anomaly
detection methods in Section 4.3, their limitation is that UAV
flight data corresponds to time series data that are spatially
and temporally correlated. However, most previous methods
only consider spatial correlation of multi-dimensional flight
parameters or temporal correlation of a single flight para-
meter. Additionally, the real UAV flight data contain random
noise that is not considered by scholars in their model ana-
lysis. This also poses a challenge to the applicability of the
proposed methods [18,96,121]. Thus, in the future, it is ne-
cessary to weigh the spatio-temporal correlation of UAV
flight data and reduce its random noise, which corresponds to
a key research direction of studying new data-driven meth-
ods for detecting UAV flight data anomalies. In addition to
the difficulty of algorithm innovation, the practicality and
scalability of algorithms are also important topics that should
be explored in future research.
Figure 8
(Color online) Structure diagram of future research directions.
914
Yang L, et al.
Sci China Tech Sci
April (2023) Vol.66 No.4

## Page 15

6.4
Study of hybrid models
Expert knowledge and experience can be used to detect
anomalies using knowledge-based anomaly detection meth-
ods. However, they are highly dependent on prior knowl-
edge, which results in poor anomaly detection ability. Model-
based anomaly detection methods for UAV flight data con-
struct an observer by establishing accurate system physical
models to obtain high anomaly detection performance.
Nevertheless, the difficulty in establishing accurate physical
models of UAVs limits their applications to a certain extent.
However, they exert a significantly positive effect on
anomaly detection performance when obtaining precise
physical models of UAVs. Additionally, although data-dri-
ven anomaly detection methods are not dependent on prior
structure information and avoid the difficulty of creating
physical models of UAVs, they are considerably affected by
training data, thereby resulting in high false–positive rates
[19]. It is possible to combine the advantages and dis-
advantages of the aforementioned methods to build hybrid
models for improving generalization and practicability of
models. Given the limitations of the aforementioned meth-
ods, researchers also face a major challenge in ensuring the
feasibility and effectiveness of hybrid models.
6.5
Multi-UAV anomaly detection based on federated
learning
Majority of the current knowledge-based, model-based, and
data-driven anomaly detection methods for UAV flight data
are limited to the detection of anomalies in a single UAV.
However, the increase in UAV cluster anomaly detection
[122,123] research poses a challenge to data transmission,
calculation, and storage in computers. New technologies are
urgently required to overcome this bottleneck. Hence, fed-
erated learning is considered as a solution. It is a new dis-
tributed machine learning paradigm driven by multi-party
data participation and maximizing data value through en-
crypted interaction [124–126]. It can be used to train models
without transmitting the local flight data of a single UAV.
This allows the central server to significantly reduce the
calculation and storage costs of analyzing multi-dimensional
UAV flight data. Although its effectiveness has not been
verified, it necessitates further investigation.
6.6
Few-shot/semi-supervised learning
It is not feasible to obtain significant real abnormal UAV
flight data for data anomaly detection tasks. Most abnormal
data are obtained via simulation software. Hence, few-shot
learning methods [127–129] can be used to train the model
by using many normal UAV flight data and small abnormal
ones to enhance its anomaly detection performance. Fur-
thermore, the UAV flight data anomaly detection tasks are
categorized as unsupervised model training, and thus it is
difficult to determine whether or not samples are normal.
This is a factor that adversely affects the performance of the
model. Thus, the semi-supervised learning method [130–
132] can be used to label abnormal and normal flight data to
improve the performance of anomaly detection. However,
collected anomaly samples are also characterized by in-
complete categories. Hence, an area of future research in-
volves ensuring the generalizability and scalability of the
models.
6.7
Anomaly detection based on transfer learning
Existing UAV flight data anomaly detection algorithms focus
on specific flight level anomaly detection or instantaneous
anomaly detection tasks. When the task changes, the model
should be rebuilt from scratch. Additionally, supervised
learning methods lead to strict requirements on the number
of data samples, uniformity of data distribution, and com-
pleteness of labels [133]. Therefore, a challenge in UAV
flight data anomaly detection model research involves
quickly modeling new data based on simulated data and
existing algorithmic models. The aim of transfer learning
involves transferring knowledge from existing models and
data to the target to be learned via exploiting correlation
between the learning target and existing knowledge. It is
widely used in fault diagnosis and can cope with problems
such as task variation [134], insufficient samples, and in-
complete labels [135,136]. Hence, transfer learning-based
methods can be employed to decrease the number of training
data samples and training time required for the target domain
model [137] in UAV flight data anomaly detection. Methods,
including convolutional neural network (CNN) [138,139],
can be used to simply tune parameters to provide unified,
end-to-end solutions for different flight data anomaly de-
tection tasks. However, with respect to flight data, issues
including what to transfer, how to transfer, and existence of
negative transfer and transfer boundaries should be further
examined and explored.
6.8
Research on lightweight real-time anomaly detec-
tion models
Most current UAV flight data anomaly detection algorithms
are offline and do not satisfy UAV real-time anomaly de-
tection requirements. Real-time anomaly detection of flight
data during UAV flight is necessary to monitor whether
anomalies occur during UAV flight in real-time for ensuring
safe and reliable operation of UAVs [140]. Additionally, the
actual deployment of the UAV flight data anomaly detection
algorithm is inseparable from the computing platform as a
carrier. When the complexity of the model increases, it re-
sults in higher requirement of computational resources. It is a
915
Yang L, et al.
Sci China Tech Sci
April (2023) Vol.66 No.4

## Page 16

significant challenge to satisfy computational and accuracy
requirements of real-time flight data processing with limited
computational resources and energy consumption. There-
fore, the focus of current research involves designing light-
weight real-time anomaly detection algorithms with low
model complexity.
6.9
Developing fully functional platforms and frame-
works
For the aforementioned UAV flight data anomaly detection
platforms and frameworks, rt-R2U2 is dependent on prior
knowledge and exhibits high hardware requirements. Ardu-
pilot’s code is redundant and not user-friendly and EIS and
EADS exhibit high calculation costs. These issues present
challenges to the performance and practicality of UAV flight
data anomaly detection. Although they exhibit certain lim-
itations, a research direction in the future can be utilized by
using their complementary advantages for developing ap-
plication platforms and frameworks that are optimized and
efficient.
7
Conclusions
The role of UAVs in various fields is more evident and im-
portant, and thus the safety of their operations has also re-
ceived unprecedented attention. To ensure the safe flight of
UAVs, it is crucial to detect anomalies in-flight data. Spe-
cifically, the study focuses on the following four aspects.
(1) Data constitutes the foundation for anomaly detection
in UAV flight data. Currently, most researchers focus on
simulated flight data and publicly available flight datasets.
Therefore, we briefly introduced and explained some public
datasets used for UAV flight data anomaly detection. We also
introduced simulation software that can obtain simulated
UAV flight data including their advantages and dis-
advantages. The aim of the study involves aiding in the se-
lection of relevant public datasets or simulation software to
obtain UAV flight data to improve the performance of UAV
anomaly detection research.
(2) Based on the content (1), we conduct a more com-
prehensive comparison and analysis of UAV flight data
anomaly detection technology. The advantages and dis-
advantages of knowledge-based, model-based, and data-
driven methods in the field of UAV flight data anomaly
detection are highlighted. In terms of extant literature, extant
studies focus on data-driven methods as opposed to knowl-
edge-based and model-based methods. This is attributed to
the rapid development of big data technology and artificial
intelligence algorithms in recent years, which provides
strong technical support for data analysis.
(3) To comprehensively analyze the current application
status of UAV flight data anomaly detection in China and
abroad, we briefly expounded the following three aspects:
universities, research institutes, and enterprises. Among
them, universities focus on the field of UAV flight data
anomaly detection, and most technologies involved in their
research results correspond to data-driven methods, which is
consistent with the current development trend of UAV flight
data anomaly detection technology described in the content
(2). However, systematic research on the same is not con-
ducted by UAV flight data anomaly detection research in-
stitutions including universities. Currently, there is no
systematic technical system for UAV flight data anomaly
detection, and most of the research results are still in the
theoretical research stage.
(4) Based on the contents (1)–(3), we provide some di-
rections for future research and specific implementation
details to provide references for subsequent research scho-
lars.
Evidently, existing UAV flight data anomaly detection
technologies and applications have realized satisfactory re-
sults. However, given the characteristics of multi-di-
mensionality, low rank, data flow, and relatively weak
anomaly detection technology of UAV flight data, the de-
velopment of UAV flight data anomaly detection has been
hindered to a certain extent. Therefore, it is necessary to
study the anomaly detection of UAV flight data in the future.
This work was supported by the National Key R&D Program of China
(Grant No. 2020YFB1713300), Guizhou Provincial Colleges and Uni-
versities Talent Training Base Project (Grant No. [2020]009), Guizhou
Province Science and Technology Plan Project (Grant Nos. [2015]4011 and
[2017]5788), Guizhou Provincial Department of Education Youth Science
and Technology Talent Growth Project (Grant No. [2022]142), the Scientific
Research Project for Introducing Talents from Guizhou University (Grant
No. (2021)74), and the Guizhou Province Higher Education Integrated
Research Platform Project (Grant No. [2020]005).
1
Ullah S, Kim K I, Kim K H, et al. UAV-enabled healthcare archi-
tecture: Issues and challenges. Future Gener Comput Syst, 2019, 97:
425–432
2
Zailani M A H, Sabudin R Z A R, Rahman R A, et al. Drone for
medical products transportation in maternal healthcare. Medicine,
2020, 99: e21967
3
Radoglou-Grammatikis P, Sarigiannidis P, Lagkas T, et al. A com-
pilation of UAVapplications for precision agriculture. Comput Netw,
2020, 172: 107148
4
Reddy Maddikunta P K, Hakak S, Alazab M, et al. Unmanned aerial
vehicles in smart agriculture: Applications, requirements, and chal-
lenges. IEEE Sens J, 2021, 21: 17608–17619
5
Gao T, Bai X. Bayesian optimization-based three-dimensional, time-
varying environment monitoring using an UAV. J Intell Robot Syst,
2022, 105: 1–2
6
Khosravi M R, Samadi S. BL-ALM: A blind scalable edge-guided
reconstruction filter for smart environmental monitoring through
green IoMT-UAV networks. IEEE Trans Green Commun Netw,
2021, 5: 727–736
7
Półka M, Ptak S, Kuziora Ł. The use of UAV’s for search and rescue
operations. Procedia Eng, 2017, 192: 748–752
8
Erdelj M, Natalizio E, Chowdhury K R, et al. Help from the sky:
916
Yang L, et al.
Sci China Tech Sci
April (2023) Vol.66 No.4

## Page 17

Leveraging UAVs for disaster management. IEEE Pervasive Comput,
2017, 16: 24–32
9
Peng Y, He Y F, Wang S J, et al. Flight data anomaly detection: A
survey (in Chinese). Chin J Sci Instrum, 2019, 40: 1–13
10
Yu Z, Sun F, Lu X, et al. Overview of research on 3D path planning
methods for rotor UAV. In: 2021 International Conference on Elec-
tronics, Circuits and Information Engineering (ECIE). Suzhou, 2021.
368–371
11
Wang B, Wang Z, Liu L, et al. Data-driven anomaly detection for
UAV sensor data based on deep learning prediction model. In: 2019
Prognostics and System Health Management Conference (PHM-
Paris). Paris, 2019. 286–290
12
Gao Y H, Zhao D, Li Y B. UAV sensor fault diagnosis technology: A
survey. Appl Mech Mater, 2012, 220-223: 1833–1837
13
Ding S T, Bao M Y, Du F R. Safety research on unmanned aircraft
system for airworthiness. J Aerosp Power, 2012, 27: 233–240
14
USAF Accident Investigation Board. AIB reports. USA, USAF
2010–2014. http://usaf.aib.law.af.mil
15
Joslin R. Insights into unmanned aircraft systems accidents and in-
cidents (2009–2014). In: Aviation, Aeronautics, Aerospace Interna-
tional Research Conference-2015. Washington, 2015
16
Liu Y, Ding W. A KNNS based anomaly detection method applied
for UAV flight data stream. In: 2015 Prognostics and System Health
Management Conference (PHM). Beijing, 2015
17
Zhao W, Li L, Alam S, et al. An incremental clustering method for
anomaly detection in flight data. Transp Res Part C-Emerg Technol,
2021, 132: 103406
18
Wang B, Liu D, Wang W, et al. A hybrid approach for UAV flight
data estimatio and based on flight mode recognition. Microelectron
Reliab, 2018, 84: 253–262
19
Peng X Y, Pang J Y, Peng Y, et al. Review on anomaly detection of
spacecraft telemetry data (in Chinese). Chin J Sci Instrum, 2016, 37:
1929–1945
20
Das S, Li L, Srivastava A, et al. Comparison of algorithms for
anomaly detection in flight recorder data of airline operations. In:
12th AIAA Aviation Technology, Integration, and Operations (ATIO)
Conference and 14th AIAA/ISSMO Multidisciplinary Analysis and
Optimization Conference. lndianapolis, 2012
21
Basora L, Olive X, Dubot T. Recent advances in anomaly detection
methods applied to aviation. Aerospace, 2019, 6: 117
22
Igenewari V R, Skaf Z, Jennions I K. A survey of flight anomaly
detection methods: Challenges and opportunities. In: Annual Con-
ference of the PHM Society. Scottsdale, 2019
23
Khan S, Liew C F, Yairi T, et al. Unsupervised anomaly detection in
unmanned aerial vehicles. Appl Soft Comput, 2019, 83: 105650
24
Megatroika A, Galinium M, Mahendra A, et al. Aircraft anomaly
detection using algorithmic model and data model trained on FOQA
data. In: 2015 International Conference on Data and Software En-
gineering (ICoDSE). Yogyakarta, 2015. 42–47
25
Hawkins D M. Identification of Outliers. London: Chapman and
Hall, 1980
26
Keogh E, Lin J, Lee S H, et al. Finding the most unusual time series
subsequence: Algorithms and applications. Knowl Inf Syst, 2007, 11:
1–27
27
Chen Y F. Real-time anomaly detection system for unmanned aerial
vehicle flight data (in Chinese). Dissertation for the Master’s Degree.
Harbin: Harbin University of Technology, 2017
28
Dong J Y, Pang J Y, Peng Y, et al. Spacecraft telemetry data anomaly
detection method based on ensemble LSTM (in Chinese). Chin J Sci
Instrum, 2019, 40: 22–29
29
Calikus E, Nowaczyk S, Bouguelia M R, et al. Wisdom of the
contexts: Active ensemble learning for contextual anomaly detection.
Data Min Knowl Disc, 2022, 36: 2410–2458
30
Meirman T, Stern R, Katz G. Anomaly detection for aggregated data
using multi-graph autoencoder. arXiv preprint, arXiv: 2101.04053,
2021
31
Chandola V, Banerjee A, Kumar V. Anomaly detection: A survey.
ACM Comput Surv, 2009, 41: 1–58
32
Li L, Hansman R J, Palacios R, et al. Anomaly detection via a
Gaussian Mixture Model for flight operation and safety monitoring.
Transp Res Part C-Emerg Technol, 2016, 64: 45–57
33
He Y, Peng Y, Wang S, et al. ADMOST: UAV flight data anomaly
detection and mitigation via online subspace tracking. IEEE Trans
Instrum Meas, 2018, 68: 1035–1044
34
Dalmau R, Prats X, Ramonjoan A, et al. Estimating fuel consumption
from radar tracks: A validation exercise using FDR and radar tracks
from descent trajectories. CEAS Aeronaut J, 2020, 11: 355–365
35
He X, He F, Zhu X, et al. Data-driven method for estimating aircraft
mass from quick access recorder using aircraft dynamics and mul-
tilayer perceptron neural network. arXiv preprint, arXiv: 2012.05907,
2020
36
Wang L, Wu C, Sun R. An analysis of flight Quick Access Recorder
(QAR) data and its applications in preventing landing incidents.
Reliab Eng Syst Saf, 2014, 127: 86–96
37
Li X, Shang J, Zheng L, et al. Curve cluster: Automated recognition
of hard landing patterns based on QAR curve clustering. In: 2019
IEEE Smart World, Ubiquitous Intelligence & Computing, Advanced
& Trusted Computing, Scalable Computing & Communications,
Cloud & Big Data Computing, Internet of People and Smart City
Innovation. Leicester, 2019. 602–609
38
Huang R, Sun H, Wu C, et al. Estimating eddy dissipation rate with
QAR flight big data. Appl Sci, 2019, 9: 5192
39
Huang L. The practical application of QAR data in civil aviation. In:
2020 International Conference on Computer Science and Manage-
ment Technology (ICCSMT). Shanghai, 2020. 96–99
40
Liu L S, Zhang Z Y, Wang Z L, et al. Anomalous attitude sensing
data generation method for quadrotor unmanned aerial vehicle (in
Chinese). Chin J Sci Instrum, 2020, 41: 58–67
41
He Y F, Wang S J, Wang W J, et al. UAVanomaly detection based on
oversampling projection approximation basis pursuit (in Chinese).
Chin J Sci Instrum, 2016, 37: 1468–1476
42
Freeman P, Pandita R, Srivastava N, et al. Model-based and data-
driven fault detection performance for a small UAV. IEEE ASME
Trans Mech, 2013, 18: 1300–1309
43
Keipour A, Mousaei M, Scherer S. Alfa: A dataset for UAV fault and
anomaly detection. Int J Rob Res, 2021, 40: 515–520
44
Peng Y, Shi S H, Guo K, et al. Fault simulation and data generation
of UAV flight control system (in Chinese). Chin J Sci Instrum, 2019,
40: 13–21
45
Taylor B. Thor flight 60. Retrieved from the University of Minnesota
Digital Conservancy, 2014. https://hdl.handle.net/11299/164228
46
Taylor B. Thor flight 69. Retrieved from the University of Minnesota
Digital Conservancy, 2012. https://hdl.handle.net/11299/174347
47
Taylor B. Thor flight 81. Retrieved from the University of Minnesota
Digital Conservancy, 2013. https://hdl.handle.net/11299/174357
48
Taylor B. Thor flight 83. Retrieved from the University of Minnesota
Digital Conservancy, 2013. https://hdl.handle.net/11299/174359
49
Taylor B. Thor flight 97. Retrieved from the University of Minnesota
Digital Conservancy, 2013. https://hdl.handle.net/11299/174374
50
Taylor B. Thor flight 98. Retrieved from the University of Minnesota
Digital Conservancy, 2013. https://hdl.handle.net/11299/174375
51
Cheng Y, Chen K, Sun H, et al. Data and knowledge mining with big
data towards smart production. J Ind Inf Integr, 2018, 9: 1–13
52
Hentati A I, Krichen L, Fourati M, et al. Simulation tools, environ-
ments and frameworks for UAV systems performance analysis. In:
2018 14th International Wireless Communications & Mobile Com-
puting Conference (IWCMC). Limassol, 2018. 1495–1500
53
Khalastchi E, Kalech M, Kaminka G A, et al. Online data-driven
anomaly detection in autonomous robots. Knowl Inf Syst, 2015, 43:
657–688
54
Hentati A I, Fourati L C, Elgharbi E, et al. Simulation tools, en-
vironments and frameworks for UAVs and multi-UAV-based systems
performance analysis (version 2.0). Int J Model Simul, 2022, 1–17
55
Mairaj A, Baba A I, Javaid A Y. Application specific drone simu-
917
Yang L, et al.
Sci China Tech Sci
April (2023) Vol.66 No.4

## Page 18

lators: Recent advances and challenges. Simul Model Pract Theor,
2019, 94: 100–117
56
de Souza J P C, Marcato A L M, de Aguiar E P, et al. Autonomous
landing of UAV based on artificial neural network supervised by
fuzzy logic. J Control Autom Electr Syst, 2019, 30: 522–531
57
Said Elsayed M, Le-Khac N A, Dev S, et al. Network anomaly
detection using LSTM based autoencoder. In: Proceedings of the
16th ACM Symposium on QoS and Security for Wireless and Mobile
Networks. Alicante, 2020. 37–45
58
Pustokhina I V, Pustokhin D A, Vaiyapuri T, et al. An automated
deep learning based anomaly detection in pedestrian walkways for
vulnerable road users safety. Saf Sci, 2021, 142: 105356
59
Kong X, Song X, Xia F, et al. LoTAD: Long-term traffic anomaly
detection based on crowdsourced bus trajectory data. World Wide
Web, 2018, 21: 825–847
60
Wang C. IoT anomaly detection method in intelligent manufacturing
industry based on trusted evaluation. Int J Adv Manuf Technol, 2020,
107: 993–1005
61
Lin X X, Lin P, Yeh E H. Anomaly detection/prediction for the
Internet of Things: State of the art and the future. IEEE Network,
2020, 35: 212–218
62
Anandakrishnan A, Kumar S, Statnikov A, et al. Anomaly detection
in finance: Editors’ introduction. In: KDD 2017 Workshop on
Anomaly Detection in Finance. Halifax, 2018. 1–7
63
Nourbakhsh A, Bang G. A framework for anomaly detection using
language modeling, and its applications to finance. arXiv preprint,
arXiv: 1908.09156, 2019
64
Shao G, Ma Y, Malekian R, et al. A novel cooperative platform
design for coupled USV-UAV systems. IEEE Trans Ind Inf, 2019, 15:
4913–4922
65
Rosa R L, Schwartz G M, Ruggiero W V, et al. A knowledge-based
recommendation system that includes sentiment analysis and deep
learning. IEEE Trans Ind Inf, 2018, 15: 2124–2135
66
Callahan T J, Tripodi I J, Pielke-Lombardo H, et al. Knowledge-
based biomedical data science. Annu Rev Biomed Data Sci, 2020, 3:
23–41
67
Badii C, Bellini P, Cenni D, et al. Analysis and assessment of a
knowledge based smart city architecture providing service APIs.
Future Gener Comput Syst, 2017, 75: 14–29
68
Qi J, Zhao X, Jiang Z, et al. An adaptive threshold neural-network
scheme for rotorcraft UAV sensor failure diagnosis. In: International
Symposium on Neural Networks. Berlin, 2007. 589–596
69
Bu J, Sun R, Bai H, et al. Integrated method for the UAV navigation
sensor anomaly detection. IET Radar Sonar Nav, 2017, 11: 847–853
70
Radke A J, Cymrot S, A’Heam K, et al. “Small data” anomaly de-
tection for unmanned systems. In: 2018 IEEE Autotestcon. National
Harbor, 2018. 1–7
71
Schmidt T, Hauer F, Pretschner A. Automated anomaly detection in
CPS log files. In: International Conference on Computer Safety,
Reliability, and Security. Cham, 2020. 179–194
72
Abbaspour A, Aboutalebi P, Yen K K, et al. Neural adaptive ob-
server-based sensor and actuator fault detection in nonlinear systems:
Application in UAV. ISA Trans, 2017, 67: 317–329
73
López-Estrada F R, Ponsart J C, Theilliol D, et al. LPV model-based
tracking control and robust sensor fault diagnosis for a quadrotor
UAV. J Intell Robot Syst, 2016, 84: 163–177
74
Suarez A, Heredia G, Ollero A. Cooperative sensor fault recovery in
multi-UAV systems. In: 2016 IEEE International Conference on
Robotics and Automation (ICRA). Stockholm, 2016. 1188–1193
75
Wang Y, Wang D, Wang J. A data driven approach for detection and
isolation of anomalies in a group of UAVs. Chin J Aeronaut, 2015,
28: 206–213
76
Wang J, Wang Y, Zhu Y. Bias compensation estimation in multi-
UAV formation and anomaly detection. J Control Syst Eng, 2016, 4:
40–50
77
Zhang Y M. Fault detection and diagnosis for NASA GTMUAV with
dual unscented kalman filter. In: Valavanis K, Vachtsevanos G (eds.).
Handbook of Unmanned Aerial Vehicles. Dordrecht: Springer, 2015.
1157–1181
78
Guo D, Zhong M, Zhou D. Multisensor data-fusion-based approach
to airspeed measurement fault detection for unmanned aerial ve-
hicles. IEEE Trans Instrum Meas, 2017, 67: 317–327
79
Singh N. Big data technology: Developments in current research and
emerging landscape. Enterprise Inf Syst, 2019, 13: 801–831
80
Kumar P, Kumar R. Issues and challenges of load balancing tech-
niques in cloud computing. ACM Comput Surv, 2019, 51: 1–35
81
Abbasi A A, Abbasi A, Shamshirband S, et al. Software-defined
cloud computing: A systematic review on latest trends and devel-
opments. IEEE Access, 2019, 7: 93294–93314
82
Wang Y B, Zheng P, Peng T, et al. Smart additive manufacturing:
Current artificial intelligence-enabled methods and future perspec-
tives. Sci China Tech Sci, 2020, 63: 1600–1611
83
Borges A F S, Laurindo F J B, Spínola M M, et al. The strategic use
of artificial intelligence in the digital era: Systematic literature review
and future research directions. Int J Inf Manage, 2021, 57: 102225
84
Ryan M. Agricultural big data analytics and the ethics of power. J
Agric Environ Ethics, 2020, 33: 49–69
85
Mourtzis D, Vlachou E, Milas N. Industrial big data as a result of IoT
adoption in manufacturing. Procedia Cirp, 2016, 55: 290–295
86
Price Ii W N, Cohen I G. Privacy in the age of medical big data. Nat
Med, 2019, 25: 37–43
87
Subramaniyan M, Skoogh A, Salomonsson H, et al. A data-driven
algorithm to predict throughput bottlenecks in a production system
based on active periods of the machines. Comput Ind Eng, 2018, 125:
533–544
88
Bansak K, Ferwerda J, Hainmueller J, et al. Improving refugee in-
tegration through data-driven algorithmic assignment. Science, 2018,
359: 325–329
89
Alos A M, Dahrouj Z, Dakkak M. A novel technique to assess UAV
behavior using PCA-based anomaly detection algorithm. Int J Mech
Eng Robot Res, 2020, 9: 721–726
90
Pan D, Nie L, Kang W, et al. UAV anomaly detection using active
learning and improved S3VM model. In: 2020 International Con-
ference on Sensing, Measurement & Data Analytics in the era of
Artificial Intelligence (ICSMD). Xi’an, 2020. 253–258
91
Sun R, Cheng Q, Wang G, et al. A novel online data-driven algorithm
for detecting UAV navigation sensor faults. Sensors, 2017, 17: 2243
92
Titouna C, Naït-Abdesselam F, Moungla H. An online anomaly de-
tection approach for unmanned aerial vehicles. In: 2020 International
Wireless Communications and Mobile Computing (IWCMC). Li-
massol, 2020. 469–474
93
Pan D. Hybrid data-driven anomaly detection method to improve
UAV operating reliability. In: 2017 Prognostics and System Health
Management Conference (PHM-Harbin). Harbin, 2017. 1–4
94
Wang B, Liu D, Peng X, et al. Data-driven anomaly detection of
UAV based on multimodal regression model. In: 2019 IEEE Inter-
national Instrumentation and Measurement Technology Conference
(I2MTC). Auckland, 2019. 1–6
95
Duan Y, Zhao Y, Pang J, et al. Unmanned aerial vehicle sensing data
anomaly detection by relevance vector machine. In: 2017 Interna-
tional Conference on Sensing, Diagnostics, Prognostics, and Control
(SDPC). Shanghai, 2017. 638–641
96
Li G, Rai A, Lee H, et al. Operational anomaly detection in flight
data using a multivariate gaussian mixture model. In: 10th Annual
Conference of the Prognostics and Health Management Society,
PHM 2018. Philadelphia, 2018
97
Bronz M, Baskaya E, Delahaye D, et al. Real-time fault detection on
small fixed-wing UAVs using machine learning. In: 2020 AIAA/
IEEE 39th Digital Avionics Systems Conference (DASC). San An-
tonio, 2020. 1–10
98
Bae G, Joe I. UAV anomaly detection with distributed artificial in-
telligence based on LSTM-AE and AE. In: Park J, Yang L, Jeong Y
S, et al. (eds.). Advanced Multimedia and Ubiquitous Engineering.
2019. Lecture Notes in Electrical Engineering, Vol. 590. Singapore:
918
Yang L, et al.
Sci China Tech Sci
April (2023) Vol.66 No.4

## Page 19

Springer, 2019. 305–310
99
Bell V, Rengasamy D, Rothwell B, et al. Anomaly detection for
unmanned aerial vehicle sensor data using a stacked recurrent au-
toencoder method with dynamic thresholding. arXiv preprint, arxiv:
2203.04734, 2022
100
Aksoy M, Ozdemir O, Guner G, et al. Flight trajectory pattern
generalization and abnormal flight detection with generative adver-
sarial network. In: AIAA Scitech 2021 Forum. Nashville, 2021
101
Xiong P, Zhu Y, Sun Z, et al. Application of transfer learning in
continuous time series for anomaly detection in commercial aircraft
flight data. In: 2018 IEEE International Conference on Smart Cloud
(SmartCloud). New York, 2018. 13–18
102
Sheridan K, Puranik T G, Mangortey E, et al. An application of
dbscan clustering for flight anomaly detection during the approach
phase. In: AIAA Scitech 2020 Forum. Orlando, 2020
103
Lee H, Li G, Rai A, et al. Real-time anomaly detection framework
using a support vector regression for the safety monitoring of com-
mercial aircraft. Adv Eng Inf, 2020, 44: 101071
104
Schumann J, Rozier K Y, Reinbacher T, et al. Towards real-time, on-
board, hardware-supported sensor and software health management
for unmanned aerial systems. Int J Progn Health Manag, 2015, 6: 1–
27
105
Baidya S, Shaikh Z, Levorato M. FlyNetSim: An open source syn-
chronized UAV network simulator based on ns-3 and ardupilot. In:
Proceedings of the 21st ACM International Conference on Modeling,
Analysis and Simulation of Wireless and Mobile Systems. Barcelona,
2018. 37–45
106
Wang B, Chen Y, Liu D, et al. An embedded intelligent system for
on-line anomaly detection of unmanned aerial vehicle. J Intell Fuzzy
Syst, 2018, 34: 3535–3545
107
Chen Y, Wang B, Liu W, et al. On-line and non-invasive anomaly
detection system for unmanned aerial vehicle. In: 2017 Prognostics
and System Health Management Conference (PHM-Harbin). Harbin,
2017. 1–7
108
Xiaoning Z. Analysis of military application of UAV swarm tech-
nology. In: 2020 3rd International Conference on Unmanned Systems
(ICUS). Harbin, 2020. 1200–1204
109
Shakhatreh H, Sawalmeh A H, Al-Fuqaha A, et al. Unmanned aerial
vehicles (UAVs): A survey on civil applications and key research
challenges. IEEE Access, 2019, 7: 48572–48634
110
Zhi Y, Fu Z, Sun X, et al. Security and privacy issues of UAV: A
survey. Mobile Netw Appl, 2020, 25: 95–101
111
He Y F. UAV flight data instantaneous anomalies detection based on
subspace learning (in Chinese). Dissertation for the Doctoral Degree.
Harbin: Harbin Institute of Technology, 2019
112
He Y, Peng Y, Wang S, et al. A structured sparse subspace learning
algorithm for anomaly detection in UAV flight data. IEEE Trans
Instrum Meas, 2017, 67: 90–100
113
Pei X L. Design and development of UAV flight test data integrated
analysis software (in Chinese). Dissertation for the Master’s Degree.
Chengdu: University of Electronic Science and Technology, 2016
114
White K J S, Denney E, Knudson M D, et al. A programmable SDN +
NFV-based architecture for UAV telemetry monitoring. In: 2017 14th
IEEE Annual Consumer Communications & Networking Conference
(CCNC). Las Vegas, 2017. 522–527
115
Pang Y, Wang S, Peng Y, et al. A microcoded kernel recursive least
squares processor using fpga technology. ACM Trans Reconfig
Technol Syst, 2017, 10: 1–22
116
Duan Y, Zhao Y, Xu Y, et al. Unmanned aerial vehicle sensor data
anomaly detection using kernel principle component analysis. In:
2017 13th IEEE International Conference on Electronic Measure-
ment & Instruments (ICEMI). Yangzhou, 2017. 241–246
117
Lipton Z C. The mythos of model interpretability. Commun ACM,
2018, 61: 36–43
118
Gilpin L H, Bau D, Yuan B Z, et al. Explaining explanations: An
overview of interpretability of machine learning. In: 2018 IEEE 5th
International Conference on Data Science and Advanced Analytics
(DSAA). Turin, 2018. 80–89
119
Kumarakulasinghe N B, Blomberg T, Liu J, et al. Evaluating local
interpretable
model-agnostic
explanations
on
clinical
machine
learning classification models. In: 2020 IEEE 33rd International
Symposium on Computer-Based Medical Systems (CBMS). Roche-
ster, 2020. 7–12
120
Na J, Bak J H, Sahinidis N V. Efficient Bayesian inference using
adversarial machine learning and low-complexity surrogate models.
Comput Chem Eng, 2021, 151: 107322
121
Wang B, Liu D, Peng Y, et al. Multivariate regression-based fault
detection and recovery of UAV flight data. IEEE Trans Instrum
Meas, 2019, 69: 3527–3537
122
Lin S, Clark R, Birke R, et al. Anomaly detection for time series
using vae-lstm hybrid model. In: ICASSP 2020–2020. IEEE Inter-
national Conference on Acoustics, Speech and Signal Processing
(ICASSP). Barcelona, 2020. 4322–4326
123
Ahn H, Choi H L, Kang M, et al. Learning-based anomaly detection
and monitoring for swarm drone flights. Appl Sci, 2019, 9: 5477
124
Jianhong W, Yanxiang W. Synthesis analysis for multi-UAVs for-
mation anomaly detection. AEAT, 2021, 93: 180–189
125
McMahan B, Moore E, Ramage D, et al. Communication-efficient
learning of deep networks from decentralized data. In: Proceedings
of the 20th International Conference on Artificial Intelligence and
Statistics (AISTATS). Fort Lauderdale, 2017. 1273–1282
126
Zhang C, Xie Y, Bai H, et al. A survey on federated learning. Knowl-
Based Syst, 2021, 216: 106775
127
Li T, Sahu A K, Talwalkar A, et al. Federated learning: Challenges,
methods, and future directions. IEEE Signal Process Mag, 2020, 37:
50–60
128
Wang Y, Yao Q, Kwok J T, et al. Generalizing from a few examples.
ACM Comput Surv, 2021, 53: 1–34
129
Zhou X, Liang W, Shimizu S, et al. Siamese neural network based
few-shot learning for anomaly detection in industrial cyber-physical
systems. IEEE Trans Ind Inf, 2020, 17: 5790–5798
130
Cheng G, Li R, Lang C, et al. Task-wise attention guided part
complementary learning for few-shot image classification. Sci China
Inf Sci, 2021, 64: 120104
131
Hussain B, Du Q, Ren P. Semi-supervised learning based big data-
driven anomaly detection in mobile wireless networks. China Com-
mun, 2018, 15: 41–57
132
Daneshpazhouh A, Sami A. Entropy-based outlier detection using
semi-supervised approach with few positive examples. Pattern Re-
cognition Lett, 2014, 49: 77–84
133
Li C, Li S, Zhang A, et al. Meta-learning for few-shot bearing fault
diagnosis under complex working conditions. Neurocomputing,
2021, 439: 197–211
134
He Z, Shao H, Lin J, et al. Transfer fault diagnosis of bearing in-
stalled in different machines using enhanced deep auto-encoder.
Measurement, 2020, 152: 107393
135
Ma G, Xu S, Yang T, et al. A transfer learning-based method for
personalized state of health estimation of lithium-ion batteries. IEEE
Trans Neural Netw Learn Syst, 2022, doi: 10.1109/TNNLS.2022.
3176925
136
Li W, Huang R, Li J, et al. A perspective survey on deep transfer
learning for fault diagnosis in industrial scenarios: Theories, appli-
cations and challenges. Mech Syst Signal Pr, 2022, 167: 108487
137
Pan S J, Yang Q. A survey on transfer learning. IEEE Trans Knowl
Data Eng, 2009, 22: 1345–1359
138
Yuan Y, Ma G, Cheng C, et al. A general end-to-end diagnosis
framework for manufacturing systems. Natl Sci Rev, 2020, 7: 418–
429
139
Cao H, Shao H, Zhong X, et al. Unsupervised domain-share CNN for
machine fault transfer diagnosis from steady speeds to time-varying
speeds. J Manuf Syst, 2022, 62: 186–198
140
Alam M S, Natesha B V, Ashwin T S, et al. UAV based cost-ef-
fective real-time abnormal event detection using edge computing.
Multimed Tools Appl, 2019, 78: 35119–35134
919
Yang L, et al.
Sci China Tech Sci
April (2023) Vol.66 No.4
